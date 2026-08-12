from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import pytest

from src.audit import AuditExportError, export_safe_audit
from src.mcp.run_store import RunStore


def _source_result(error_message: str | None = None) -> dict:
    return {
        "schema_version": "1",
        "source_id": "official-feed",
        "source_type": "rss",
        "status": "failed" if error_message else "success",
        "item_count": 0,
        "started_at": datetime(2026, 8, 12, tzinfo=timezone.utc).isoformat(),
        "finished_at": datetime(2026, 8, 12, 0, 0, 1, tzinfo=timezone.utc).isoformat(),
        "latency_ms": 1000,
        "attempts": 1,
        "fallback_used": None,
        "error_code": "NETWORK" if error_message else None,
        "error_message": error_message,
    }


def _decision() -> dict:
    return {
        "schema_version": "1",
        "item_id": "rss:item-1",
        "status": "selected",
        "stage": "selection",
        "reason_code": "SELECTED_VERIFIED_ORIGINAL",
        "reason": "Selected within the verified-original allocation.",
        "title": "A verified release",
        "url": "https://example.com/release",
        "ai_score": 9.1,
        "source_id": "official-feed",
        "source_level": "L1",
        "verification_status": "direct",
        "policy_values": {
            "ai_score": 9.1,
            "discovery_level": "L1",
            "original_level": "L1",
        },
        "prior_event_id": None,
    }


def _model_call() -> dict:
    return {
        "schema_version": "1",
        "call_id": "analysis-0001",
        "provider": "deepseek",
        "model": "deepseek-v4-flash",
        "stage": "analysis",
        "item_id": None,
        "status": "ok",
        "error_code": None,
        "attempts": 1,
        "latency_ms": 25,
        "input_tokens": None,
        "output_tokens": None,
        "total_tokens": None,
        "started_at": "2026-08-12T00:00:00+00:00",
        "finished_at": "2026-08-12T00:00:00.025000+00:00",
    }


def test_safe_audit_exports_only_allowlisted_files_and_fields(tmp_path: Path) -> None:
    store = RunStore(tmp_path / "runs")
    run_id = store.create_run("run-safe")
    store.save_source_health(run_id, [_source_result()])
    store.save_decisions(run_id, [_decision()])
    store.save_model_calls(run_id, [_model_call()])
    store.save_manifest(
        run_id,
        {
            "schema_version": "1",
            "run_id": run_id,
            "status": "complete",
            "healthy_source_ratio": 1.0,
            "source_counts": {"success": 1, "empty": 0, "partial": 0, "failed": 0},
            "pipeline_counts": {"fetched": 1, "selected": 1},
            "failed_source_ids": [],
            "generated_at": "2026-08-12T00:00:00+00:00",
        },
    )
    store.save_items(
        run_id,
        "raw",
        [{"id": "rss:item-1", "content": "SECRET_SENTINEL private full text"}],
    )

    output = export_safe_audit(store.run_dir(run_id), tmp_path / "safe")

    assert {path.name for path in output.iterdir()} == {
        "manifest.json",
        "source_health.json",
        "decisions.json",
        "model_calls.json",
        "index.html",
    }
    serialized = "\n".join(
        path.read_text(encoding="utf-8") for path in output.iterdir() if path.is_file()
    )
    assert "SECRET_SENTINEL" not in serialized
    assert "content" not in json.dumps(json.loads((output / "decisions.json").read_text()))
    assert "Source health" in (output / "index.html").read_text(encoding="utf-8")
    page = (output / "index.html").read_text(encoding="utf-8")
    assert "A verified release" in page
    assert 'href="https://example.com/release"' in page
    assert "SELECTED_VERIFIED_ORIGINAL" in page


def test_safe_audit_rejects_non_https_decision_links(tmp_path: Path) -> None:
    store = RunStore(tmp_path / "runs")
    run_id = store.create_run("run-insecure-link")
    store.save_source_health(run_id, [_source_result()])
    decision = _decision()
    decision["url"] = "http://example.com/release"
    store.save_decisions(run_id, [decision])
    store.save_model_calls(run_id, [_model_call()])
    store.save_manifest(
        run_id, {"schema_version": "1", "run_id": run_id, "status": "complete"}
    )

    with pytest.raises(AuditExportError):
        export_safe_audit(store.run_dir(run_id), tmp_path / "safe")


def test_safe_audit_rejects_unknown_manifest_fields(tmp_path: Path) -> None:
    store = RunStore(tmp_path / "runs")
    run_id = store.create_run("run-unknown")
    store.save_source_health(run_id, [_source_result()])
    store.save_decisions(run_id, [_decision()])
    store.save_model_calls(run_id, [_model_call()])
    store.save_manifest(
        run_id,
        {
            "schema_version": "1",
            "run_id": run_id,
            "status": "complete",
            "private_debug": "must fail closed",
        },
    )

    with pytest.raises(AuditExportError):
        export_safe_audit(store.run_dir(run_id), tmp_path / "safe")


@pytest.mark.parametrize(
    "field_name",
    [
        "response_body",
        "request-headers",
        "completionText",
        "stack.trace",
        "api_key",
        "access-token",
    ],
)
def test_safe_audit_rejects_prohibited_field_name_variants(
    tmp_path: Path, field_name: str
) -> None:
    store = RunStore(tmp_path / "runs")
    run_id = store.create_run("run-prohibited-field")
    store.save_source_health(run_id, [_source_result()])
    decision = _decision()
    decision["policy_values"][field_name] = "SECRET_SENTINEL"
    store.save_decisions(run_id, [decision])
    store.save_model_calls(run_id, [_model_call()])
    store.save_manifest(
        run_id, {"schema_version": "1", "run_id": run_id, "status": "complete"}
    )

    with pytest.raises(AuditExportError):
        export_safe_audit(store.run_dir(run_id), tmp_path / "safe")


def test_safe_audit_rejects_invalid_nested_manifest_shapes(tmp_path: Path) -> None:
    store = RunStore(tmp_path / "runs")
    run_id = store.create_run("run-invalid-manifest")
    store.save_source_health(run_id, [_source_result()])
    store.save_decisions(run_id, [_decision()])
    store.save_model_calls(run_id, [_model_call()])
    store.save_manifest(
        run_id,
        {
            "schema_version": "1",
            "run_id": run_id,
            "status": "complete",
            "failed_source_ids": [{"debug": "must fail closed"}],
        },
    )

    with pytest.raises(AuditExportError):
        export_safe_audit(store.run_dir(run_id), tmp_path / "safe")


@pytest.mark.parametrize(
    "needle",
    [
        "token=SECRET_SENTINEL",
        "Authorization: Bearer SECRET_SENTINEL",
        "-----BEGIN PRIVATE KEY-----SECRET_SENTINEL-----END PRIVATE KEY-----",
        "<script>alert(1)</script>",
    ],
)
def test_safe_audit_rejects_secrets_and_escapes_untrusted_html(
    tmp_path: Path, needle: str
) -> None:
    store = RunStore(tmp_path / "runs")
    run_id = store.create_run("run-hostile")
    message = needle if "<script>" not in needle else None
    store.save_source_health(run_id, [_source_result(message)])
    decision = _decision()
    if "<script>" in needle:
        decision["reason"] = needle
    store.save_decisions(run_id, [decision])
    store.save_model_calls(run_id, [_model_call()])
    store.save_manifest(run_id, {"schema_version": "1", "run_id": run_id, "status": "partial"})

    if "<script>" not in needle:
        with pytest.raises(AuditExportError):
            export_safe_audit(store.run_dir(run_id), tmp_path / "safe")
    else:
        output = export_safe_audit(store.run_dir(run_id), tmp_path / "safe")
        page = (output / "index.html").read_text(encoding="utf-8")
        assert "<script>alert(1)</script>" not in page
        assert "&lt;script&gt;alert(1)&lt;/script&gt;" in page


def test_shadow_workflow_is_read_only_and_uploads_only_safe_bundle() -> None:
    root = Path(__file__).resolve().parents[1]
    workflow = (root / ".github/workflows/source-quality-shadow.yml").read_text(
        encoding="utf-8"
    )

    assert "workflow_dispatch:" in workflow
    assert "contents: read" in workflow
    assert "contents: write" not in workflow
    assert "retention-days: 14" in workflow
    assert "path: .source-quality-safe" in workflow
    assert "path: data/runs" not in workflow
    assert "peaceiris/actions-gh-pages" not in workflow
    assert "schedule:" not in workflow
    assert "inputs:" not in workflow
    assert "uv run horizon" in workflow
    assert "--config data/config.sources-v2.local.json" in workflow
    assert "--save-stages" in workflow
    assert "--no-pages" in workflow
    assert "GITHUB_TOKEN: ${{ github.token }}" in workflow
    assert "tests/test_model_audit.py" in workflow
    assert "tests/test_enricher_status.py" in workflow
