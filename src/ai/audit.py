"""Metadata-only audit wrapper for Horizon model calls."""

from __future__ import annotations

from datetime import datetime, timezone
from itertools import count
from time import perf_counter
from typing import Any

import httpx

from ..models import ModelCallRecord
from .tokens import get_usage_snapshot


def _error_code(error: Exception) -> str:
    if isinstance(error, (TimeoutError, httpx.TimeoutException)):
        return "TIMEOUT"
    response = getattr(error, "response", None)
    status_code = getattr(error, "status_code", None) or getattr(
        response, "status_code", None
    )
    if status_code in {401, 403}:
        return "AUTH"
    if status_code == 429:
        return "RATE_LIMIT"
    if isinstance(error, httpx.HTTPError):
        return "NETWORK"
    return "MODEL_ERROR"


class _AuditedClient:
    def __init__(
        self,
        base: Any,
        audit: "ModelCallAudit",
        stage: str,
        item_id: str | None = None,
    ):
        self._base = base
        self._audit = audit
        self._stage = stage
        self._item_id = item_id
        self.config = getattr(base, "config", None)

    def for_item(self, item_id: str) -> "_AuditedClient":
        """Return an immutable per-item view safe for concurrent calls."""
        return _AuditedClient(
            self._base,
            self._audit,
            self._stage,
            item_id=str(item_id),
        )

    async def complete(
        self,
        system: str,
        user: str,
        temperature: float | None = None,
        max_tokens: int | None = None,
    ) -> str:
        call_number = next(self._audit._counter)
        started_at = datetime.now(timezone.utc)
        started_clock = perf_counter()
        usage_before = get_usage_snapshot()
        self._audit._active_calls += 1
        status = "ok"
        error_code = None
        try:
            return await self._base.complete(
                system=system,
                user=user,
                temperature=temperature,
                max_tokens=max_tokens,
            )
        except Exception as error:
            status = "failed"
            error_code = _error_code(error)
            raise
        finally:
            usage_after = get_usage_snapshot()
            before = usage_before.per_provider.get(self._audit.provider)
            after = usage_after.per_provider.get(self._audit.provider)
            input_tokens = (
                max(
                    0,
                    after.input_tokens - (before.input_tokens if before else 0),
                )
                if after is not None
                else None
            )
            output_tokens = (
                max(
                    0,
                    after.output_tokens - (before.output_tokens if before else 0),
                )
                if after is not None
                else None
            )
            # Concurrent calls share provider counters, so only attach per-call
            # usage when this call ran without another audited call in flight.
            tokens_available = (
                self._audit._active_calls == 1
                and input_tokens is not None
                and output_tokens is not None
            )
            self._audit.records.append(
                ModelCallRecord(
                    call_id=f"{self._stage}-{call_number:04d}",
                    provider=self._audit.provider,
                    model=self._audit.model,
                    stage=self._stage,
                    item_id=self._item_id,
                    status=status,
                    error_code=error_code,
                    attempts=1,
                    latency_ms=max(0, int((perf_counter() - started_clock) * 1000)),
                    input_tokens=(input_tokens if tokens_available else None),
                    output_tokens=(output_tokens if tokens_available else None),
                    total_tokens=(
                        int(input_tokens) + int(output_tokens)
                        if tokens_available
                        else None
                    ),
                    started_at=started_at,
                    finished_at=datetime.now(timezone.utc),
                )
            )
            self._audit._active_calls -= 1


class ModelCallAudit:
    """Collect model-call envelopes without observing their text payloads."""

    def __init__(self, config: Any):
        provider = getattr(config, "provider", "unknown")
        self.provider = str(getattr(provider, "value", provider))
        self.model = str(getattr(config, "model", "unknown"))
        self.records: list[ModelCallRecord] = []
        self._counter = count(1)
        self._active_calls = 0

    def wrap(self, client: Any, *, stage: str) -> _AuditedClient:
        return _AuditedClient(client, self, stage)


__all__ = ["ModelCallAudit"]
