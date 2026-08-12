from __future__ import annotations

import asyncio
from types import SimpleNamespace

import pytest

from src.ai.audit import ModelCallAudit
from src.ai.tokens import record_usage, reset_usage


class FakeClient:
    async def complete(self, *, system, user, temperature=None, max_tokens=None):
        if user == "fail":
            raise TimeoutError("SECRET_SENTINEL response body")
        return "ok"


def test_model_audit_records_metadata_without_prompt_or_response() -> None:
    audit = ModelCallAudit(
        SimpleNamespace(provider=SimpleNamespace(value="deepseek"), model="test-model")
    )
    client = audit.wrap(FakeClient(), stage="analysis")

    assert asyncio.run(client.complete(system="SECRET_SYSTEM", user="SECRET_USER")) == "ok"
    payload = [record.model_dump(mode="json") for record in audit.records]

    assert payload[0]["status"] == "ok"
    assert payload[0]["stage"] == "analysis"
    assert payload[0]["total_tokens"] is None
    assert "SECRET" not in str(payload)


def test_model_audit_records_sanitized_error_code_and_reraises() -> None:
    audit = ModelCallAudit(
        SimpleNamespace(provider=SimpleNamespace(value="deepseek"), model="test-model")
    )
    client = audit.wrap(FakeClient(), stage="enrichment")

    with pytest.raises(TimeoutError):
        asyncio.run(client.complete(system="public", user="fail"))

    assert audit.records[0].status == "failed"
    assert audit.records[0].error_code == "TIMEOUT"
    assert "SECRET_SENTINEL" not in str(audit.records[0].model_dump())


def test_model_audit_associates_calls_with_item_without_shared_state() -> None:
    audit = ModelCallAudit(
        SimpleNamespace(provider=SimpleNamespace(value="deepseek"), model="test-model")
    )
    client = audit.wrap(FakeClient(), stage="analysis")

    async def run_calls():
        await asyncio.gather(
            client.for_item("item-a").complete(system="public", user="a"),
            client.for_item("item-b").complete(system="public", user="b"),
        )

    asyncio.run(run_calls())

    assert {record.item_id for record in audit.records} == {"item-a", "item-b"}


def test_model_audit_records_per_call_tokens_when_uncontended() -> None:
    reset_usage()

    class UsageClient:
        async def complete(self, *, system, user, temperature=None, max_tokens=None):
            record_usage("deepseek", input_tokens=4, output_tokens=2)
            return "ok"

    audit = ModelCallAudit(
        SimpleNamespace(provider=SimpleNamespace(value="deepseek"), model="test-model")
    )
    client = audit.wrap(UsageClient(), stage="analysis")

    asyncio.run(client.for_item("item-a").complete(system="public", user="a"))

    assert audit.records[0].input_tokens == 4
    assert audit.records[0].output_tokens == 2
    assert audit.records[0].total_tokens == 6
    reset_usage()
