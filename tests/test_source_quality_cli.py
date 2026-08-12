from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from pathlib import Path

import pytest

from src.main import build_parser, main as cli_main
from src.mcp.run_store import RunStore
from src.models import (
    AIConfig,
    Config,
    ContentItem,
    ContentProvenance,
    FilteringConfig,
    QualityPolicy,
    SourceRunResult,
    SourceLevel,
    SourceType,
    SourcesConfig,
    VerificationStatus,
)
from src.orchestrator import HorizonOrchestrator, SourceQualityRunError
from src.source_health import SourceFetchBatch
from src.ai.tokens import record_usage, reset_usage


NOW = datetime(2026, 8, 12, 12, tzinfo=timezone.utc)


def _config() -> Config:
    return Config(
        ai=AIConfig(
            provider="openai",
            model="test",
            api_key_env="TEST_API_KEY",
            languages=[],
        ),
        sources=SourcesConfig(),
        filtering=FilteringConfig(ai_score_threshold=7.0),
        quality_policy=QualityPolicy(
            enabled=True,
            candidate_limits={"default_per_source": 2, "max_candidates_before_ai": 4},
            selection={
                "max_items": 2,
                "target_verified_original_items": 1,
                "max_l3_only_items": 1,
            },
            run_health={"min_healthy_source_ratio": 0.5},
        ),
    )


def _item(ident: str, score: float, level: str = "L1") -> ContentItem:
    return ContentItem(
        id=ident,
        source_type=SourceType.RSS,
        title=ident,
        url=f"https://example.com/{ident}",
        published_at=NOW,
        metadata={"source_id": "official" if level == "L1" else "community"},
        provenance=ContentProvenance(
            discovery_source_id="official" if level == "L1" else "community",
            discovery_level=level,
            original_level="L1" if level == "L1" else None,
            verification_status="direct" if level == "L1" else "unverified",
        ),
        ai_score=score,
        ai_reason=f"Reason {ident}",
    )


def _health(source_id: str, status: str, count: int = 0) -> SourceRunResult:
    return SourceRunResult(
        source_id=source_id,
        source_type=SourceType.RSS,
        status=status,
        item_count=count,
        started_at=NOW,
        finished_at=NOW,
        latency_ms=1,
        attempts=1,
        error_code="NETWORK" if status == "failed" else None,
        error_message="NetworkError" if status == "failed" else None,
    )


def test_cli_quality_flags_are_opt_in() -> None:
    args = build_parser().parse_args([])
    assert args.config is None
    assert args.save_stages is False
    assert args.no_pages is False
    assert args.run_id is None
    custom = build_parser().parse_args(
        ["--config", "v2.json", "--save-stages", "--no-pages", "--run-id", "shadow-1"]
    )
    assert custom.config == Path("v2.json")
    assert custom.save_stages is True
    assert custom.no_pages is True
    assert custom.run_id == "shadow-1"


def test_v2_pipeline_persists_health_decisions_and_manifest(
    tmp_path: Path, monkeypatch
) -> None:
    monkeypatch.setenv("TEST_API_KEY", "test")
    orchestrator = HorizonOrchestrator(_config(), object())
    values = [_item("keep", 9.0), _item("drop", 5.0, "L3")]
    batch = SourceFetchBatch(
        items=values,
        source_results=[_health("official", "success", 1), _health("community", "failed")],
    )

    async def fetch(since):
        orchestrator.last_source_results = batch.source_results
        return batch

    async def analyze(items):
        return items

    async def topic(items):
        return items

    async def expand(items):
        return None

    async def enrich(items):
        return None

    monkeypatch.setattr(orchestrator, "fetch_all_sources_with_health", fetch)
    monkeypatch.setattr(orchestrator, "_analyze_content", analyze)
    monkeypatch.setattr(orchestrator, "merge_topic_duplicates", topic)
    monkeypatch.setattr(orchestrator, "_expand_twitter_discussion", expand)
    monkeypatch.setattr(orchestrator, "_enrich_important_items", enrich)
    monkeypatch.chdir(tmp_path)
    store = RunStore(tmp_path / "runs")

    outcome = asyncio.run(
        orchestrator.run(
            force_hours=24,
            artifact_store=store,
            artifact_run_id="v2-test",
            publish_pages=False,
        )
    )

    assert outcome.status == "partial"
    assert [item.id for item in outcome.selected_items] == ["keep"]
    assert store.load_manifest("v2-test")["status"] == "partial"
    assert store.load_model_calls("v2-test") == []
    assert {result["source_id"] for result in store.load_source_health("v2-test")} == {
        "official",
        "community",
    }
    decisions = store.load_decisions("v2-test")
    assert len({decision["item_id"] for decision in decisions}) == 2
    assert {decision["reason_code"] for decision in decisions} >= {
        "SELECTED_VERIFIED_ORIGINAL",
        "BELOW_AI_THRESHOLD",
    }
    assert not (tmp_path / "docs").exists()


def test_v2_all_source_failure_generates_artifacts_and_raises(
    tmp_path: Path, monkeypatch
) -> None:
    monkeypatch.setenv("TEST_API_KEY", "test")
    orchestrator = HorizonOrchestrator(_config(), object())
    batch = SourceFetchBatch(items=[], source_results=[_health("official", "failed")])

    async def fetch(since):
        return batch

    monkeypatch.setattr(orchestrator, "fetch_all_sources_with_health", fetch)
    monkeypatch.chdir(tmp_path)
    store = RunStore(tmp_path / "runs")

    with pytest.raises(SourceQualityRunError) as exc_info:
        asyncio.run(
            orchestrator.run(
                artifact_store=store,
                artifact_run_id="v2-failed",
                publish_pages=False,
            )
        )

    assert exc_info.value.exit_code == 2
    assert store.load_manifest("v2-failed")["status"] == "failed"
    assert store.load_source_health("v2-failed")[0]["status"] == "failed"
    assert store.load_model_calls("v2-failed") == []


def test_v2_health_ratio_below_minimum_is_fatal() -> None:
    orchestrator = HorizonOrchestrator(_config(), object())
    health = orchestrator._classify_source_health(
        [
            _health("healthy", "success", 1),
            _health("failed-one", "failed"),
            _health("failed-two", "failed"),
        ]
    )

    assert health["healthy_source_ratio"] == pytest.approx(1 / 3, abs=0.0001)
    assert health["status"] == "failed"


def test_v2_manifest_token_usage_is_scoped_to_the_current_run() -> None:
    reset_usage()
    record_usage("deepseek", input_tokens=100, output_tokens=10)
    orchestrator = HorizonOrchestrator(_config(), object())
    record_usage("deepseek", input_tokens=5, output_tokens=2)

    manifest = orchestrator._build_manifest(
        run_id="token-scope",
        status="complete",
        health={"healthy_source_ratio": 1.0, "failed_source_ids": []},
        source_results=[],
        pipeline_counts={},
    )

    assert manifest["token_usage"] == {"input": 5, "output": 2, "total": 7}
    reset_usage()


def test_cli_config_failure_writes_safe_artifacts_and_exits_two(
    tmp_path: Path, monkeypatch
) -> None:
    bad_config = tmp_path / "invalid-v2.json"
    bad_config.write_text("{}", encoding="utf-8")
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(
        "sys.argv",
        [
            "horizon",
            "--config",
            str(bad_config),
            "--save-stages",
            "--run-id",
            "config-failure",
            "--no-pages",
        ],
    )

    with pytest.raises(SystemExit) as exc_info:
        cli_main()

    assert exc_info.value.code == 2
    store = RunStore(tmp_path / "data" / "runs")
    assert store.load_manifest("config-failure")["failed_stages"] == [
        "configuration"
    ]
    assert store.load_source_health("config-failure") == []
    assert store.load_decisions("config-failure") == []
    assert store.load_model_calls("config-failure") == []


def test_v2_preflight_failure_writes_safe_failure_report_before_fetch(
    tmp_path: Path, monkeypatch
) -> None:
    orchestrator = HorizonOrchestrator(_config(), object())
    fetched = False

    def fail_preflight(stage):
        raise ValueError("missing provider configuration")

    async def fetch(since):
        nonlocal fetched
        fetched = True
        raise AssertionError("fetch must not run after failed preflight")

    monkeypatch.setattr(orchestrator, "_create_ai_client", fail_preflight)
    monkeypatch.setattr(orchestrator, "fetch_all_sources_with_health", fetch)
    store = RunStore(tmp_path / "runs")

    with pytest.raises(SourceQualityRunError) as exc_info:
        asyncio.run(
            orchestrator.run(
                artifact_store=store,
                artifact_run_id="v2-preflight-failed",
                publish_pages=False,
            )
        )

    assert exc_info.value.exit_code == 2
    assert fetched is False
    manifest = store.load_manifest("v2-preflight-failed")
    assert manifest["status"] == "failed"
    assert manifest["failed_stages"] == ["preflight"]
    assert store.load_source_health("v2-preflight-failed") == []
    assert store.load_model_calls("v2-preflight-failed") == []


def test_v2_generated_run_id_survives_preflight_failure(
    tmp_path: Path, monkeypatch
) -> None:
    orchestrator = HorizonOrchestrator(_config(), object())

    def fail_preflight(stage):
        raise ValueError("missing provider configuration")

    monkeypatch.setattr(orchestrator, "_create_ai_client", fail_preflight)
    store = RunStore(tmp_path / "runs")

    with pytest.raises(SourceQualityRunError):
        asyncio.run(
            orchestrator.run(
                artifact_store=store,
                artifact_run_id=None,
                publish_pages=False,
            )
        )

    [run] = store.list_runs()
    run_id = run["run_id"]
    assert store.load_manifest(run_id)["failed_stages"] == ["preflight"]
    assert store.load_decisions(run_id) == []


def test_v2_late_failure_preserves_computed_decisions(
    tmp_path: Path, monkeypatch
) -> None:
    monkeypatch.setenv("TEST_API_KEY", "test")
    orchestrator = HorizonOrchestrator(_config(), object())
    values = [_item("keep", 9.0), _item("drop", 5.0, "L3")]
    batch = SourceFetchBatch(
        items=values,
        source_results=[_health("official", "success", 2)],
    )

    async def fetch(since):
        orchestrator.last_source_results = batch.source_results
        return batch

    async def identity(items):
        return items

    async def expand(items):
        return None

    async def fail_enrichment(items):
        raise RuntimeError("enrichment failed")

    monkeypatch.setattr(orchestrator, "fetch_all_sources_with_health", fetch)
    monkeypatch.setattr(orchestrator, "_analyze_content", identity)
    monkeypatch.setattr(orchestrator, "merge_topic_duplicates", identity)
    monkeypatch.setattr(orchestrator, "_expand_twitter_discussion", expand)
    monkeypatch.setattr(orchestrator, "_enrich_important_items", fail_enrichment)
    store = RunStore(tmp_path / "runs")

    with pytest.raises(SourceQualityRunError):
        asyncio.run(
            orchestrator.run(
                artifact_store=store,
                artifact_run_id="v2-late-failure",
                publish_pages=False,
            )
        )

    decisions = store.load_decisions("v2-late-failure")
    assert {decision["item_id"] for decision in decisions} == {"keep", "drop"}
    assert store.load_manifest("v2-late-failure")["failed_stages"] == ["enrichment"]


def test_v2_refills_source_after_resolved_history_duplicate(
    tmp_path: Path, monkeypatch
) -> None:
    monkeypatch.setenv("TEST_API_KEY", "test")
    config = _config().model_copy(deep=True)
    config.sources = SourcesConfig(
        hackernews={"enabled": False},
        rss=[
            {
                "name": "Official",
                "url": "https://official.example/feed.xml",
                "source_id": "official-feed",
                "source_level": "L1",
            }
        ],
        reddit={"enabled": False},
        telegram={"enabled": False},
    )
    config.quality_policy = QualityPolicy(
        enabled=True,
        candidate_limits={"default_per_source": 1, "max_candidates_before_ai": 1},
        provenance={"resolve_l3_original": True},
        selection={
            "max_items": 1,
            "target_verified_original_items": 1,
            "max_l3_only_items": 1,
        },
        run_health={"min_healthy_source_ratio": 0.5},
    )
    orchestrator = HorizonOrchestrator(config, object())
    first = _item("first", 9.5, "L3")
    first = ContentItem.model_validate(
        {**first.model_dump(mode="json"), "url": "https://community.example/first"}
    )
    first.metadata["source_id"] = "community"
    first.provenance.discovery_source_id = "community"
    second = _item("second", 9.0, "L3")
    second = ContentItem.model_validate(
        {**second.model_dump(mode="json"), "url": "https://example.com/new"}
    )
    second.metadata["source_id"] = "community"
    second.provenance.discovery_source_id = "community"
    batch = SourceFetchBatch(
        items=[first, second],
        source_results=[_health("community", "success", 2)],
    )

    async def fetch(since):
        orchestrator.last_source_results = batch.source_results
        return batch

    async def identity(items):
        return items

    async def no_op(items):
        return None

    monkeypatch.setattr(orchestrator, "fetch_all_sources_with_health", fetch)
    monkeypatch.setattr(orchestrator, "_analyze_content", identity)
    monkeypatch.setattr(orchestrator, "merge_topic_duplicates", identity)
    monkeypatch.setattr(orchestrator, "_expand_twitter_discussion", no_op)
    monkeypatch.setattr(orchestrator, "_enrich_important_items", no_op)

    def resolve(items, config):
        resolved = []
        for value in items:
            if value.id != "first":
                resolved.append(value)
                continue
            provenance = value.provenance.model_copy(
                update={
                    "original_url": "https://official.example/already-published",
                    "original_level": SourceLevel.L1,
                    "verification_status": VerificationStatus.RESOLVED,
                },
                deep=True,
            )
            resolved.append(
                value.model_copy(update={"provenance": provenance}, deep=True)
            )
        return resolved

    monkeypatch.setattr("src.orchestrator.resolve_known_originals", resolve)
    monkeypatch.setattr(
        orchestrator,
        "_load_recent_history",
        lambda *args, **kwargs: [
            {
                "item_id": "prior",
                "url": "https://official.example/already-published",
                "published_at": datetime.now(timezone.utc),
            }
        ],
    )
    monkeypatch.chdir(tmp_path)
    store = RunStore(tmp_path / "runs")

    outcome = asyncio.run(
        orchestrator.run(
            artifact_store=store,
            artifact_run_id="v2-refill",
            publish_pages=False,
        )
    )

    assert [item.id for item in outcome.selected_items] == ["second"]
    assert any(
        decision.item_id == "first"
        and decision.reason_code.value == "DUPLICATE_PRIOR_EVENT"
        for decision in outcome.decisions
    )
