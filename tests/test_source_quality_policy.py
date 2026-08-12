from datetime import datetime, timedelta, timezone

from src.models import (
    AIConfig,
    Config,
    ContentItem,
    ContentProvenance,
    QualityPolicy,
    RSSSourceConfig,
    FilteringConfig,
    HackerNewsConfig,
    RedditConfig,
    SourceType,
    SourcesConfig,
    TelegramConfig,
)
from src.source_quality import (
    apply_candidate_limits,
    attach_provenance,
    canonicalize_url,
    deduplicate_same_run,
    filter_exact_history,
    resolve_known_originals,
    select_digest,
    source_id_for_item,
)


NOW = datetime(2026, 8, 12, 12, tzinfo=timezone.utc)


def item(
    ident: str,
    source: str,
    score: float,
    *,
    level: str | None = "L3",
    verification: str = "unverified",
    category: str = "ai",
    published: datetime = NOW,
    native_id: str | None = None,
    marker: str | None = None,
) -> ContentItem:
    metadata = {"source_id": source, "category": category, "engagement": int(score * 10)}
    if native_id:
        metadata["native_id"] = native_id
    if marker:
        metadata["material_update_marker"] = marker
    provenance = None
    if level is not None:
        provenance = ContentProvenance(
            discovery_source_id=source,
            discovery_level=level,
            verification_status=verification,
            original_level="L1" if verification in {"direct", "resolved", "corroborated"} else None,
            original_url="https://original.example/event" if verification == "resolved" else None,
        )
    return ContentItem(
        id=ident,
        source_type=SourceType.RSS,
        title=ident,
        url=f"https://example.com/{ident}",
        content="SECRET_SENTINEL should never be in a decision",
        published_at=published,
        metadata=metadata,
        provenance=provenance,
        ai_score=score,
    )


def test_canonicalization_preserves_meaningful_query_and_drops_tracking():
    assert canonicalize_url(
        "HTTPS://WWW.Example.COM:443/a?utm_source=x&b=2&a=1#fragment"
    ) == "https://example.com/a?a=1&b=2"
    assert canonicalize_url(
        "https://example.com/path?token=SECRET_SENTINEL&meaningful=1&utm_medium=x"
    ) == "https://example.com/path?meaningful=1"
    assert canonicalize_url(
        "https://example.com/path?key=SECRET_SENTINEL&meaningful=1"
    ) == "https://example.com/path?meaningful=1"


def test_source_id_and_attach_provenance_do_not_overwrite_existing():
    base = item("one", "rss-feed", 8)
    assert source_id_for_item(base) == "rss-feed"
    existing = base.model_copy(
        update={"provenance": ContentProvenance(discovery_source_id="already", discovery_level="L1")}
    )
    attached = attach_provenance(existing, source_id="new", source_level="L3", profile_status="missing")
    assert attached.provenance is not None
    assert attached.provenance.discovery_source_id == "already"
    assert attached is not existing
    legacy = base.model_copy(update={"provenance": None, "metadata": {}})
    assert source_id_for_item(legacy).startswith("legacy-")
    filled = attach_provenance(legacy, source_id="custom", source_level="L2", profile_status="custom")
    assert filled.provenance.discovery_source_id == "custom"
    assert filled.provenance.discovery_level.value == "L2"


def test_candidate_limits_disabled_is_identity_noop():
    values = [item("one", "rss", 8)]
    result = apply_candidate_limits(values, QualityPolicy())
    assert result.items is values
    assert result.decisions == []


def test_same_run_dedup_prefers_direct_evidence_and_records_the_duplicate():
    discovered = item("community-copy", "hn", 0, level="L3")
    discovered.url = "https://example.com/release?utm_source=hn"
    discovered.content = "long community discussion"
    direct = item("official-copy", "official", 0, level="L1", verification="direct")
    direct.url = "https://example.com/release"
    direct.content = "official release"

    result = deduplicate_same_run([discovered, direct])

    assert [value.id for value in result.items] == ["official-copy"]
    assert result.items[0].metadata["merged_source_ids"] == ["hn", "official"]
    assert [decision.item_id for decision in result.decisions] == ["community-copy"]
    assert result.decisions[0].reason_code.value == "DUPLICATE_CANONICAL_URL"
    assert result.decisions[0].stage == "same_run_deduplication"


def test_decision_omits_non_https_item_url_instead_of_crashing():
    insecure = item("insecure", "legacy", 8, level="L2")
    insecure.url = "http://example.com/insecure"

    result = select_digest(
        [insecure],
        QualityPolicy(
            enabled=True,
            selection={
                "max_items": 1,
                "target_verified_original_items": 0,
                "max_l3_only_items": 1,
            },
        ),
    )

    assert result.decisions[0].url is None


def test_known_l1_domain_resolves_l3_link_without_a_network_request():
    config = Config(
        ai=AIConfig(provider="openai", model="test", api_key_env="TEST"),
        sources=SourcesConfig(
            hackernews=HackerNewsConfig(enabled=False),
            rss=[
                RSSSourceConfig(
                    name="Official",
                    url="https://official.example/feed.xml",
                    source_id="official-feed",
                    source_level="L1",
                )
            ],
            reddit=RedditConfig(enabled=False),
            telegram=TelegramConfig(enabled=False),
        ),
        filtering=FilteringConfig(),
        quality_policy=QualityPolicy(
            enabled=True,
            provenance={"resolve_l3_original": True},
        ),
    )
    discovery = item("community", "hn", 9, level="L3")
    discovery.url = "https://official.example/release"

    [resolved] = resolve_known_originals([discovery], config)

    assert resolved.provenance is not None
    assert resolved.provenance.verification_status.value == "resolved"
    assert resolved.provenance.original_level.value == "L1"
    assert str(resolved.provenance.original_url) == "https://official.example/release"


def test_known_github_repository_requires_https_for_resolution():
    config = Config(
        ai=AIConfig(provider="openai", model="test", api_key_env="TEST"),
        sources=SourcesConfig(
            github=[
                {
                    "type": "repo_releases",
                    "owner": "org",
                    "repo": "project",
                    "source_id": "project-releases",
                    "source_level": "L1",
                }
            ],
            hackernews=HackerNewsConfig(enabled=False),
            reddit=RedditConfig(enabled=False),
            telegram=TelegramConfig(enabled=False),
        ),
        filtering=FilteringConfig(),
        quality_policy=QualityPolicy(
            enabled=True,
            provenance={"resolve_l3_original": True},
        ),
    )
    discovery = item("community", "hn", 9, level="L3")
    discovery.url = "http://github.com/org/project/releases/tag/v1"

    [unresolved] = resolve_known_originals([discovery], config)

    assert unresolved.provenance is not None
    assert unresolved.provenance.verification_status.value == "unverified"
    assert unresolved.provenance.original_url is None


def test_candidate_limits_apply_source_and_global_caps_with_overflow():
    values = [
        item("r1", "rss", 9), item("r2", "rss", 8), item("r3", "rss", 7),
        item("h1", "hn", 6), item("h2", "hn", 5),
    ]
    policy = QualityPolicy(
        enabled=True,
        candidate_limits={"default_per_source": 2, "max_candidates_before_ai": 3},
    )
    result = apply_candidate_limits(values, policy)
    assert len(result.items) == 3
    assert {source_id_for_item(x) for x in result.items} == {"rss", "hn"}
    assert len(result.overflow["rss"]) == 2
    assert all(d.reason_code.value == "SOURCE_CANDIDATE_CAP" for d in result.decisions)
    assert "SECRET_SENTINEL" not in str(result.decisions)


def test_selection_enforces_verified_target_l3_source_channel_and_category_limits():
    values = [
        item("verified", "official", 7.1, level="L1", verification="direct", category="ai"),
        item("analysis", "analysis", 9.9, level="L2", verification="unverified", category="ai"),
        item("l3-a", "hn", 9.8, category="security"),
        item("l3-b", "hn", 9.7, category="security"),
        item("l3-c", "telegram", 9.6, category="security"),
        item("other", "reddit", 9.5, category="ai"),
    ]
    policy = QualityPolicy(
        enabled=True,
        selection={
            "max_items": 4,
            "target_verified_original_items": 1,
            "max_l3_only_items": 1,
            "default_max_items_per_discovery_source": 1,
            "default_max_items_per_category": 2,
            "channel_group_limits": {
                "community": {"source_ids": ["hn", "telegram"], "max_items": 1}
            },
        },
    )
    result = select_digest(values, policy)
    assert len(result.selected) == 3
    assert result.selected[0].id == "verified"
    assert sum(x.provenance.discovery_level.value == "L3" for x in result.selected if x.provenance) == 1
    assert sum(d.status.value == "selected" for d in result.decisions) == 3
    assert len({d.item_id for d in result.decisions}) == len(values)
    assert any(d.reason_code.value == "L3_ONLY_LIMIT" for d in result.decisions)


def test_history_filter_duplicate_and_material_update():
    duplicate = item("new", "rss", 8, native_id="native-1")
    update = item("update", "rss", 8, native_id="native-2", marker="v2")
    history = [
        {
            "item_id": "prior-1",
            "url": "https://example.com/new?utm_source=old",
            "native_id": "native-1",
            "published_at": NOW - timedelta(days=2),
            "event_id": "prior-event-1",
        },
        {
            "item_id": "prior-2",
            "url": "https://example.com/update",
            "native_id": "native-2",
            "material_update_marker": "v1",
            "published_at": NOW - timedelta(days=2),
            "event_id": "prior-event-2",
        },
    ]
    result = filter_exact_history([duplicate, update], history, now=NOW)
    assert [x.id for x in result.items] == ["update"]
    assert result.items[0].metadata["prior_event_id"] == "prior-event-2"
    assert any(d.reason_code.value == "DUPLICATE_PRIOR_EVENT" for d in result.decisions)
    assert all(d.item_id != "update" for d in result.decisions)

    selected = select_digest(
        result.items,
        QualityPolicy(
            enabled=True,
            selection={
                "max_items": 1,
                "target_verified_original_items": 0,
                "max_l3_only_items": 1,
            },
        ),
    )
    assert selected.decisions[0].reason_code.value == "MATERIAL_UPDATE"
    assert selected.decisions[0].prior_event_id == "prior-event-2"


def test_history_filter_accepts_mapping_values():
    duplicate = item("new", "rss", 8, native_id="native-1")
    history = {
        "prior": {
            "item_id": "prior-1",
            "url": "https://example.com/new",
            "native_id": "native-1",
            "published_at": NOW - timedelta(days=1),
        }
    }

    result = filter_exact_history([duplicate], history, now=NOW)

    assert result.items == []
    assert result.decisions[0].reason_code.value == "DUPLICATE_PRIOR_EVENT"


def test_selection_ranks_by_ai_score_before_freshness():
    values = [
        item("newer-low", "analysis", 7.1, level="L2", published=NOW),
        item(
            "older-high",
            "official",
            9.8,
            level="L1",
            verification="direct",
            published=NOW - timedelta(hours=2),
        ),
    ]
    policy = QualityPolicy(
        enabled=True,
        selection={
            "max_items": 1,
            "target_verified_original_items": 0,
            "max_l3_only_items": 1,
        },
    )

    result = select_digest(values, policy)

    assert [value.id for value in result.selected] == ["older-high"]
