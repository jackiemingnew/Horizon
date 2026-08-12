"""Shared source-health contracts and provenance attachment helpers."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from time import perf_counter
from typing import Iterable
from urllib.parse import urlparse

import httpx

from .models import (
    ContentItem,
    ContentProvenance,
    ProfileStatus,
    SourceErrorCode,
    SourceLevel,
    SourceRunResult,
    SourceRunStatus,
    SourceType,
    VerificationStatus,
    stable_source_id,
)


@dataclass
class SourceFetchBatch:
    """Fetched items plus exactly one result per configured sub-source."""

    items: list[ContentItem]
    source_results: list[SourceRunResult]


def error_code_for_exception(error: Exception) -> SourceErrorCode:
    if isinstance(error, httpx.HTTPStatusError):
        if error.response.status_code == 403:
            return SourceErrorCode.HTTP_403
        if error.response.status_code == 429:
            return SourceErrorCode.HTTP_429
    if isinstance(error, httpx.TimeoutException):
        return SourceErrorCode.TIMEOUT
    if isinstance(error, httpx.HTTPError):
        return SourceErrorCode.NETWORK
    if isinstance(error, (ValueError, KeyError, TypeError)):
        return SourceErrorCode.PARSE
    return SourceErrorCode.UNKNOWN


def safe_error_message(error: Exception, label: str = "Source") -> str:
    """Return a response-body-free and credential-free error description."""
    if isinstance(error, httpx.HTTPStatusError):
        return f"HTTP {error.response.status_code} from configured source host"
    if isinstance(error, httpx.TimeoutException):
        return f"{label} request timed out"
    if isinstance(error, httpx.HTTPError):
        return type(error).__name__
    return f"{label} failed: {type(error).__name__}"


def attach_source_provenance(
    items: Iterable[ContentItem],
    *,
    source_id: str,
    source_level: SourceLevel | None,
    discovery_url: str | None = None,
) -> list[ContentItem]:
    """Attach additive provenance in place at the trusted config boundary."""
    result: list[ContentItem] = []
    for item in items:
        item.metadata["source_id"] = source_id
        if item.provenance is None:
            item_url = str(item.url)
            is_direct = source_level is SourceLevel.L1
            item.provenance = ContentProvenance(
                discovery_source_id=source_id,
                discovery_url=discovery_url or item.url,
                discovery_level=source_level,
                profile_status=(
                    ProfileStatus.KNOWN if source_level is not None else ProfileStatus.MISSING
                ),
                original_url=(item.url if is_direct else None),
                original_domain=(
                    urlparse(item_url).hostname if is_direct else None
                ),
                original_level=(SourceLevel.L1 if is_direct else None),
                verification_status=(
                    VerificationStatus.DIRECT
                    if is_direct
                    else VerificationStatus.UNVERIFIED
                ),
            )
        result.append(item)
    return result


def source_run_result(
    *,
    source_id: str,
    source_type: SourceType,
    started_at: datetime,
    started_clock: float,
    items: list[ContentItem],
    error: Exception | None = None,
    partial: bool = False,
    fallback_used: str | None = None,
) -> SourceRunResult:
    """Build one bounded result using only allowlisted error metadata."""
    if error is not None and (partial or items):
        status = SourceRunStatus.PARTIAL
    elif error is not None:
        status = SourceRunStatus.FAILED
    elif items:
        status = SourceRunStatus.SUCCESS
    else:
        status = SourceRunStatus.EMPTY
    return SourceRunResult(
        source_id=source_id,
        source_type=source_type,
        status=status,
        item_count=len(items),
        started_at=started_at,
        finished_at=datetime.now(timezone.utc),
        latency_ms=max(0, int((perf_counter() - started_clock) * 1000)),
        attempts=1,
        fallback_used=fallback_used,
        error_code=error_code_for_exception(error) if error is not None else None,
        error_message=safe_error_message(error) if error is not None else None,
    )


__all__ = [
    "SourceFetchBatch",
    "attach_source_provenance",
    "error_code_for_exception",
    "safe_error_message",
    "source_run_result",
    "stable_source_id",
]
