"""Safe exporter for source-quality audit bundles.

Full pipeline stages are intentionally excluded.  This module accepts only the
versioned, metadata-only contracts that are safe to inspect in CI artifacts or
render on a public audit page.
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from .models import AuditManifest, DecisionRecord, ModelCallRecord, SourceRunResult


class AuditExportError(ValueError):
    """Raised when an input bundle does not satisfy the public audit contract."""


_PROHIBITED_TEXT_RE = re.compile(
    r"(?i)(?:authorization\s*:|bearer\s+|private[_ -]?key|"
    r"(?:^|[?&\s])(?:api[_-]?key|key|access[_-]?token|token|sig(?:nature)?|auth|code|secret|password)=)"
)

_PROHIBITED_FIELD_KEYS = {
    "accesskey",
    "accesstoken",
    "apikey",
    "auth",
    "authorization",
    "body",
    "clientsecret",
    "code",
    "completion",
    "completiontext",
    "content",
    "cookie",
    "credential",
    "credentials",
    "headers",
    "inputtext",
    "key",
    "password",
    "privatekey",
    "prompt",
    "requestbody",
    "requestheaders",
    "responsebody",
    "responseheaders",
    "secret",
    "sig",
    "signature",
    "stacktrace",
    "token",
}


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise AuditExportError(f"Required audit input is missing: {path.name}") from exc
    except json.JSONDecodeError as exc:
        raise AuditExportError(f"Invalid JSON in audit input: {path.name}") from exc


def _validate_text_tree(value: Any, path: str = "root") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            normalized = re.sub(r"[^a-z0-9]", "", str(key).lower())
            if normalized in _PROHIBITED_FIELD_KEYS:
                raise AuditExportError(f"Prohibited audit field: {path}.{key}")
            _validate_text_tree(child, f"{path}.{key}")
        return
    if isinstance(value, list):
        for index, child in enumerate(value):
            _validate_text_tree(child, f"{path}[{index}]")
        return
    if isinstance(value, str) and _PROHIBITED_TEXT_RE.search(value):
        raise AuditExportError(f"Credential-like text rejected at {path}")


def _manifest(payload: Any) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise AuditExportError("manifest.json must contain an object")
    _validate_text_tree(payload, "manifest_input")
    try:
        manifest = AuditManifest.model_validate(payload)
    except ValidationError as exc:
        raise AuditExportError("manifest.json violates its schema") from exc
    clean = manifest.model_dump(mode="json")
    _validate_text_tree(clean, "manifest")
    return clean


def _source_results(payload: Any) -> list[dict[str, Any]]:
    if not isinstance(payload, list):
        raise AuditExportError("source_health.json must contain an array")
    _validate_text_tree(payload, "source_health_input")
    try:
        results = [SourceRunResult.model_validate(value) for value in payload]
    except ValidationError as exc:
        raise AuditExportError("source_health.json violates its schema") from exc
    clean = [value.model_dump(mode="json") for value in results]
    _validate_text_tree(clean, "source_health")
    return clean


def _decisions(payload: Any) -> list[dict[str, Any]]:
    if not isinstance(payload, list):
        raise AuditExportError("decisions.json must contain an array")
    _validate_text_tree(payload, "decisions_input")
    try:
        decisions = [DecisionRecord.model_validate(value) for value in payload]
    except ValidationError as exc:
        raise AuditExportError("decisions.json violates its schema") from exc
    clean = [value.model_dump(mode="json") for value in decisions]
    _validate_text_tree(clean, "decisions")
    return clean


def _model_calls(payload: Any) -> list[dict[str, Any]]:
    if not isinstance(payload, list):
        raise AuditExportError("model_calls.json must contain an array")
    _validate_text_tree(payload, "model_calls_input")
    try:
        records = [ModelCallRecord.model_validate(value) for value in payload]
    except ValidationError as exc:
        raise AuditExportError("model_calls.json violates its schema") from exc
    clean = [value.model_dump(mode="json") for value in records]
    _validate_text_tree(clean, "model_calls")
    return clean


def _render_page(
    manifest: dict[str, Any],
    sources: list[dict[str, Any]],
    decisions: list[dict[str, Any]],
    model_calls: list[dict[str, Any]],
) -> str:
    def escaped(value: Any) -> str:
        return html.escape(str(value), quote=True)

    source_rows = "".join(
        f'<tr data-status="{escaped(value["status"])}">'
        f'<td data-label="来源"><code>{escaped(value["source_id"])}</code></td>'
        f'<td data-label="状态"><span class="badge">{escaped(value["status"])}</span></td>'
        f'<td data-label="条目">{int(value["item_count"])}</td>'
        f'<td data-label="耗时">{int(value["latency_ms"])} ms</td>'
        f'<td data-label="回退">{escaped(value.get("fallback_used") or "—")}</td>'
        f'<td data-label="错误">{escaped(value.get("error_code") or "—")}</td>'
        "</tr>"
        for value in sources
    ) or '<tr><td colspan="6">没有来源结果</td></tr>'
    decision_rows = "".join(
        f'<tr data-status="{escaped(value["status"])}">'
        '<td data-label="条目">'
        + (
            f'<a href="{escaped(value["url"])}" rel="noopener noreferrer">'
            f'{escaped(value.get("title") or value["item_id"])}</a>'
            if value.get("url")
            else f'<strong>{escaped(value.get("title") or value["item_id"])}</strong>'
        )
        + f'<small><code>{escaped(value["item_id"])}</code></small></td>'
        f'<td data-label="结果"><span class="badge">{escaped(value["status"])}</span></td>'
        f'<td data-label="评分">{escaped(value.get("ai_score") if value.get("ai_score") is not None else "—")}</td>'
        f'<td data-label="来源层级">{escaped(value.get("source_level") or "—")}</td>'
        f'<td data-label="证据状态">{escaped(value.get("verification_status") or "—")}</td>'
        f'<td data-label="理由"><code>{escaped(value["reason_code"])}</code><small>{escaped(value["reason"])}</small></td>'
        "</tr>"
        for value in decisions
    ) or '<tr><td colspan="6">没有条目决策</td></tr>'
    model_rows = "".join(
        f'<tr data-status="{escaped(value["status"])}">'
        f'<td data-label="阶段"><code>{escaped(value["stage"])}</code></td>'
        f'<td data-label="状态"><span class="badge">{escaped(value["status"])}</span></td>'
        f'<td data-label="延迟">{int(value["latency_ms"])} ms</td>'
        f'<td data-label="错误">{escaped(value.get("error_code") or "—")}</td>'
        f'<td data-label="Token">{escaped(value.get("total_tokens") if value.get("total_tokens") is not None else "不可用")}</td>'
        "</tr>"
        for value in model_calls
    ) or '<tr><td colspan="5">本次没有模型调用</td></tr>'
    status = escaped(manifest.get("status", "unknown"))
    run_id = escaped(manifest.get("run_id", "unknown"))
    generated_at = escaped(manifest.get("generated_at", "—"))
    health_ratio = float(manifest.get("healthy_source_ratio") or 0) * 100
    pipeline = manifest.get("pipeline_counts") or {}
    source_counts = manifest.get("source_counts") or {}
    successful_calls = sum(value["status"] == "ok" for value in model_calls)
    model_success = (
        f"{successful_calls / len(model_calls) * 100:.1f}%"
        if model_calls
        else "不可用"
    )
    latencies = sorted(int(value["latency_ms"]) for value in model_calls)
    p50 = latencies[(len(latencies) - 1) // 2] if latencies else None
    p95 = latencies[int((len(latencies) - 1) * 0.95)] if latencies else None
    return f"""<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark"><title>Horizon 来源质量审计</title>
<style>
:root {{ color-scheme:light dark; font-family:Inter,ui-sans-serif,system-ui,sans-serif; --line:#8884; --panel:#8881; }}
* {{ box-sizing:border-box; }} body {{ max-width:82rem; margin:auto; padding:1.5rem; line-height:1.5; }}
header {{ display:flex; justify-content:space-between; gap:1rem; align-items:end; margin-bottom:1.5rem; }}
h1,h2 {{ letter-spacing:-.025em; }} h1 {{ margin:0; }} h2 {{ margin:2rem 0 .75rem; }} p {{ margin:.25rem 0; }}
.muted,small {{ color:#888; }} .status,.badge {{ display:inline-block; padding:.18rem .5rem; border:1px solid currentColor; border-radius:999px; font-size:.8rem; }}
.stats {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(11rem,1fr)); gap:.75rem; }}
.stat {{ background:var(--panel); border:1px solid var(--line); border-radius:.75rem; padding:1rem; }} .stat strong {{ display:block; font-size:1.35rem; }}
.table-wrap {{ overflow:auto; border:1px solid var(--line); border-radius:.75rem; }} table {{ width:100%; border-collapse:collapse; }}
th,td {{ padding:.7rem .8rem; border-bottom:1px solid var(--line); text-align:left; vertical-align:top; }} tr:last-child td {{ border-bottom:0; }}
td small {{ display:block; margin-top:.2rem; max-width:42rem; }} a {{ color:inherit; text-underline-offset:.2em; }} code {{ overflow-wrap:anywhere; }}
tr[data-status="failed"] .badge,tr[data-status="rejected"] .badge {{ color:#d34b4b; }} tr[data-status="partial"] .badge {{ color:#d29322; }}
tr[data-status="success"] .badge,tr[data-status="selected"] .badge {{ color:#26965b; }}
@media (max-width:720px) {{ body {{ padding:.85rem; }} header {{ display:block; }} .stats {{ grid-template-columns:repeat(2,minmax(0,1fr)); }}
  .decisions thead,.sources thead {{ display:none; }} .decisions tr,.sources tr {{ display:block; padding:.45rem .7rem; border-bottom:1px solid var(--line); }}
  .decisions td,.sources td {{ display:grid; grid-template-columns:6.5rem 1fr; gap:.5rem; border:0; padding:.35rem 0; }}
  .decisions td::before,.sources td::before {{ content:attr(data-label); color:#888; }} }}
</style></head><body>
<header><div><h1>Horizon 来源质量审计</h1><p class="muted">Run <code>{run_id}</code> · {generated_at}</p></div><span class="status">{status}</span></header>
<main><section class="stats" aria-label="运行摘要">
<div class="stat"><strong>{health_ratio:.1f}%</strong><span>健康来源率</span></div>
<div class="stat"><strong>{sum(int(value) for value in source_counts.values())}</strong><span>已配置来源</span></div>
<div class="stat"><strong>{int(pipeline.get("fetched", 0))}</strong><span>采集条目</span></div>
<div class="stat"><strong>{int(pipeline.get("selected", 0))}</strong><span>最终入选</span></div>
<div class="stat"><strong>{model_success}</strong><span>模型调用成功率</span></div>
</section>
<section><h2>来源健康 / Source health</h2><div class="table-wrap"><table class="sources"><thead><tr><th>来源</th><th>状态</th><th>条目</th><th>耗时</th><th>回退</th><th>错误</th></tr></thead><tbody>{source_rows}</tbody></table></div></section>
<section><h2>条目决策 / Item decisions</h2><div class="table-wrap"><table class="decisions"><thead><tr><th>条目</th><th>结果</th><th>评分</th><th>来源层级</th><th>证据状态</th><th>理由</th></tr></thead><tbody>{decision_rows}</tbody></table></div></section>
<section><h2>模型健康 / Model health</h2><p class="muted">P50 {escaped(str(p50) + " ms" if p50 is not None else "不可用")} · P95 {escaped(str(p95) + " ms" if p95 is not None else "不可用")}</p><div class="table-wrap"><table><thead><tr><th>阶段</th><th>状态</th><th>延迟</th><th>错误</th><th>Token</th></tr></thead><tbody>{model_rows}</tbody></table></div></section>
</main></body></html>"""


def export_safe_audit(run_dir: Path | str, output_dir: Path | str) -> Path:
    """Create a fresh allowlisted audit directory from one local run."""
    source = Path(run_dir)
    output = Path(output_dir)
    if output.exists() and any(output.iterdir()):
        raise AuditExportError("Audit output directory must be empty")
    output.mkdir(parents=True, exist_ok=True)

    manifest = _manifest(_load_json(source / "manifest.json"))
    sources = _source_results(_load_json(source / "source_health.json"))
    decisions = _decisions(_load_json(source / "decisions.json"))
    model_calls = _model_calls(_load_json(source / "model_calls.json"))
    payloads = {
        "manifest.json": manifest,
        "source_health.json": sources,
        "decisions.json": decisions,
        "model_calls.json": model_calls,
    }
    for filename, payload in payloads.items():
        (output / filename).write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    (output / "index.html").write_text(
        _render_page(manifest, sources, decisions, model_calls), encoding="utf-8"
    )
    return output


def main() -> None:
    """CLI entry point used by the read-only shadow workflow."""
    import argparse

    parser = argparse.ArgumentParser(description="Export a safe Horizon audit bundle")
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    export_safe_audit(args.run_dir, args.output)


__all__ = ["AuditExportError", "export_safe_audit", "main"]
