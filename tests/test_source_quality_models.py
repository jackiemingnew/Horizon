from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from src.models import (
    Config,
    ContentItem,
    ContentProvenance,
    DecisionReasonCode,
    DecisionRecord,
    DecisionStatus,
    GitHubSourceConfig,
    HackerNewsConfig,
    ModelCallRecord,
    QualityPolicy,
    RSSSourceConfig,
    RedditSubredditConfig,
    RedditUserConfig,
    SourceErrorCode,
    SourceLevel,
    SourceRunResult,
    SourceRunStatus,
    SourceType,
    TelegramChannelConfig,
    stable_source_id,
)


def _item() -> ContentItem:
    return ContentItem(
        id="rss:one",
        source_type=SourceType.RSS,
        title="An item",
        url="https://example.com/one",
        published_at=datetime(2026, 8, 12, tzinfo=timezone.utc),
    )


def test_new_models_are_additive_and_legacy_item_still_validates():
    item = _item()
    assert item.provenance is None
    assert GitHubSourceConfig(type="user_events", username="alice").source_id is None
    assert HackerNewsConfig().source_level is None
    assert RSSSourceConfig(name="feed", url="https://example.com/feed").source_id is None
    assert RedditSubredditConfig(subreddit="python").source_id is None
    assert RedditUserConfig(username="alice").source_level is None
    assert TelegramChannelConfig(channel="news").source_id is None


def test_source_id_and_provenance_validation():
    assert GitHubSourceConfig(
        type="repo_releases", owner="o", repo="r", source_id="github-releases", source_level="L1"
    ).source_level is SourceLevel.L1
    with pytest.raises(ValidationError):
        RSSSourceConfig(name="feed", url="https://example.com", source_id="Not Valid")
    with pytest.raises(ValidationError):
        RSSSourceConfig(name="feed", url="https://example.com", source_id="x/y")

    provenance = ContentProvenance(
        discovery_source_id="rss-feed",
        discovery_url="https://example.com/feed",
        discovery_level="L2",
        profile_status="custom",
        evidence_urls=["https://example.com/a", "https://example.com/a"],
    )
    assert provenance.discovery_level is SourceLevel.L2
    assert len(provenance.evidence_urls) == 1
    with pytest.raises(ValidationError):
        ContentProvenance(
            discovery_source_id="rss-feed",
            evidence_urls=[f"https://example.com/{idx}" for idx in range(6)],
        )
    with pytest.raises(ValidationError):
        ContentProvenance(
            discovery_source_id="rss-feed",
            discovery_url="http://example.com/feed",
        )
    with pytest.raises(ValidationError):
        ContentProvenance(
            discovery_source_id="rss-feed",
            discovery_level="L3",
            verification_status="direct",
        )
    with pytest.raises(ValidationError):
        ContentProvenance(
            discovery_source_id="rss-feed",
            discovery_level="L3",
            verification_status="resolved",
        )


def test_source_run_result_sanitizes_error_and_rejects_negative_counters():
    result = SourceRunResult(
        source_id="rss-feed",
        source_type=SourceType.RSS,
        status=SourceRunStatus.FAILED,
        started_at=datetime.now(timezone.utc),
        finished_at=datetime.now(timezone.utc),
        latency_ms=3,
        attempts=1,
        error_code=SourceErrorCode.NETWORK,
        error_message="line one\nline two https://example.com/?token=SECRET_SENTINEL",
    )
    assert "\n" not in (result.error_message or "")
    assert "SECRET_SENTINEL" not in (result.error_message or "")
    assert len(result.error_message or "") <= 240
    assert "attempt_count" not in result.model_dump()
    with pytest.raises(ValidationError):
        SourceRunResult(
            source_id="rss-feed",
            source_type=SourceType.RSS,
            status="success",
            started_at=datetime.now(timezone.utc),
            finished_at=datetime.now(timezone.utc),
            latency_ms=-1,
        )
    with pytest.raises(ValidationError):
        SourceRunResult(
            source_id="rss-feed",
            source_type=SourceType.RSS,
            status="success",
            started_at=datetime.now(timezone.utc),
            finished_at=datetime.now(timezone.utc),
            latency_ms=1,
            unexpected="must fail closed",
        )


def test_quality_policy_cross_field_validation_and_legacy_config():
    policy = QualityPolicy(
        enabled=True,
        candidate_limits={
            "default_per_source": 2,
            "max_candidates_before_ai": 4,
            "overrides": {"rss-feed": 3},
        },
        selection={
            "max_items": 4,
            "target_verified_original_items": 2,
            "max_l3_only_items": 2,
            "channel_group_limits": {
                "rss": {"source_ids": ["rss-feed"], "max_items": 2}
            },
        },
    )
    assert policy.enabled is True
    assert QualityPolicy().enabled is False

    with pytest.raises(ValidationError):
        QualityPolicy(
            enabled=True,
            selection={"max_items": 2, "target_verified_original_items": 3},
        )
    with pytest.raises(ValidationError):
        QualityPolicy(
            enabled=True,
            selection={
                "max_items": 2,
                "channel_group_limits": {
                    "bad": {"source_ids": ["rss-feed", "rss-feed"], "max_items": 1}
                },
            },
        )
    with pytest.raises(ValidationError):
        QualityPolicy(enabled=True, run_health={"min_healthy_source_ratio": 1.1})

    # Optional V2 policy does not invalidate a legacy config when omitted.
    assert Config.model_fields["quality_policy"].default is None


def test_decision_record_policy_values_are_safe_scalars_only():
    record = DecisionRecord(
        item_id="rss:one",
        status=DecisionStatus.REJECTED,
        stage="selection",
        reason_code=DecisionReasonCode.PROFILE_MISSING,
        reason="The source profile was not available.",
        policy_values={"cap": 2, "levels": ["L3"], "enabled": False},
    )
    assert record.reason_code is DecisionReasonCode.PROFILE_MISSING
    with pytest.raises(ValidationError):
        DecisionRecord(
            item_id="rss:one",
            status="rejected",
            stage="selection",
            reason_code="PROFILE_MISSING",
            reason="unsafe URL evidence",
            policy_values={
                "urls": [
                    "https://example.com/a?token=SECRET_SENTINEL",
                    "https://example.com/b",
                ]
            },
        )
    with pytest.raises(ValidationError):
        DecisionRecord(
            item_id="rss:one",
            status="rejected",
            stage="selection",
            reason_code="PROFILE_MISSING",
            reason="bad",
            policy_values={"nested": {"secret": "x"}},
        )
    with pytest.raises(ValidationError):
        DecisionRecord(
            item_id="rss:one",
            status="rejected",
            stage="selection",
            reason_code="PROFILE_MISSING",
            reason="bad",
            unknown_field="must fail closed",
        )
    with pytest.raises(ValidationError):
        DecisionRecord(
            item_id="rss:one",
            status="rejected",
            stage="selection",
            reason_code="PROFILE_MISSING",
            reason="bad",
            policy_values={"response_body": "must fail closed"},
        )
    with pytest.raises(ValidationError):
        DecisionRecord(
            item_id="rss:one",
            status="rejected",
            stage="selection",
            reason_code="PROFILE_MISSING",
            reason="bad",
            policy_values={"api_key": "SECRET_SENTINEL"},
        )


def test_quality_policy_accepts_deterministic_default_source_ids():
    rss_url = "https://example.com/feed"
    rss_id = stable_source_id("rss", rss_url)
    config = Config.model_validate(
        {
            "ai": {
                "provider": "openai",
                "model": "test",
                "api_key_env": "TEST_API_KEY",
            },
            "sources": {
                "hackernews": {"enabled": True},
                "rss": [{"name": "Feed", "url": rss_url}],
                "reddit": {"enabled": False},
                "telegram": {"enabled": False},
            },
            "filtering": {},
            "quality_policy": {
                "enabled": True,
                "candidate_limits": {
                    "overrides": {"hacker-news": 3, rss_id: 2}
                },
            },
        }
    )
    assert config.quality_policy is not None
    assert set(config.quality_policy.candidate_limits.overrides) == {
        "hacker-news",
        rss_id,
    }


def test_model_call_record_is_metadata_only_and_strict():
    record = ModelCallRecord(
        call_id="analysis-0001",
        provider="deepseek",
        model="deepseek-v4-flash",
        stage="analysis",
        item_id=None,
        status="ok",
        attempts=1,
        latency_ms=20,
        started_at=datetime.now(timezone.utc),
        finished_at=datetime.now(timezone.utc),
    )
    assert record.total_tokens is None
    with pytest.raises(ValidationError):
        ModelCallRecord(
            **record.model_dump(),
            prompt="must never be accepted",
        )
