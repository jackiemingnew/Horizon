from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

import httpx

from src.models import (
    ContentItem,
    GitHubSourceConfig,
    HackerNewsConfig,
    AIConfig,
    Config,
    FilteringConfig,
    RSSSourceConfig,
    SourceRunStatus,
    SourceType,
    TelegramChannelConfig,
    TelegramConfig,
    RedditConfig,
    SourcesConfig,
)
from src.orchestrator import HorizonOrchestrator
from src.scrapers.github import GitHubScraper
from src.scrapers.hackernews import HackerNewsScraper
from src.scrapers.rss import RSSScraper
from src.scrapers.telegram import TelegramScraper
from src.source_health import attach_source_provenance


SINCE = datetime(2026, 8, 12, tzinfo=timezone.utc)


def test_rss_fetch_with_results_distinguishes_empty_from_failed() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:
        if request.url.host == "empty.example":
            return httpx.Response(
                200,
                text="<?xml version='1.0'?><rss><channel><title>Empty</title></channel></rss>",
            )
        return httpx.Response(403, text="SECRET_SENTINEL response body")

    client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    scraper = RSSScraper(
        [
            RSSSourceConfig(
                source_id="empty-feed",
                source_level="L1",
                name="Empty",
                url="https://empty.example/feed.xml",
            ),
            RSSSourceConfig(
                source_id="blocked-feed",
                source_level="L2",
                name="Blocked",
                url="https://blocked.example/feed.xml",
            ),
        ],
        client,
    )

    batch = asyncio.run(scraper.fetch_with_results(SINCE))
    asyncio.run(client.aclose())

    assert batch.items == []
    assert [result.source_id for result in batch.source_results] == [
        "empty-feed",
        "blocked-feed",
    ]
    assert [result.status for result in batch.source_results] == [
        SourceRunStatus.EMPTY,
        SourceRunStatus.FAILED,
    ]
    assert batch.source_results[1].error_code.value == "HTTP_403"
    assert "SECRET_SENTINEL" not in str(batch.source_results[1].model_dump())


def test_rss_malformed_success_response_is_parse_failure() -> None:
    client = httpx.AsyncClient(
        transport=httpx.MockTransport(
            lambda request: httpx.Response(200, text="<html>not a feed</html>")
        )
    )
    scraper = RSSScraper(
        [
            RSSSourceConfig(
                source_id="malformed-feed",
                source_level="L2",
                name="Malformed",
                url="https://malformed.example/feed.xml",
            )
        ],
        client,
    )

    batch = asyncio.run(scraper.fetch_with_results(SINCE))
    asyncio.run(client.aclose())

    assert batch.source_results[0].status is SourceRunStatus.FAILED
    assert batch.source_results[0].error_code.value == "PARSE"


def test_rss_fetch_with_results_attaches_runtime_provenance() -> None:
    feed = """<?xml version="1.0"?><rss><channel><title>Official</title>
      <item><guid>1</guid><title>Release</title>
      <link>https://publisher.example/release</link>
      <pubDate>Wed, 12 Aug 2026 12:30:00 GMT</pubDate></item>
    </channel></rss>"""

    client = httpx.AsyncClient(
        transport=httpx.MockTransport(lambda request: httpx.Response(200, text=feed))
    )
    scraper = RSSScraper(
        [
            RSSSourceConfig(
                source_id="official-feed",
                source_level="L1",
                name="Official",
                url="https://publisher.example/feed.xml",
            )
        ],
        client,
    )

    batch = asyncio.run(scraper.fetch_with_results(SINCE))
    asyncio.run(client.aclose())

    assert len(batch.items) == 1
    assert batch.source_results[0].status is SourceRunStatus.SUCCESS
    assert batch.source_results[0].item_count == 1
    assert batch.items[0].metadata["source_id"] == "official-feed"
    assert batch.items[0].provenance is not None
    assert batch.items[0].provenance.discovery_level.value == "L1"
    assert batch.items[0].provenance.verification_status.value == "direct"


def test_discovery_link_is_not_promoted_to_verified_l1_without_resolution() -> None:
    item = ContentItem(
        id="hn:1",
        source_type=SourceType.HACKERNEWS,
        title="Community discovery",
        url="https://analysis.example/story",
        published_at=SINCE,
    )

    [attached] = attach_source_provenance(
        [item],
        source_id="hacker-news",
        source_level="L3",
        discovery_url="https://news.ycombinator.com/item?id=1",
    )

    assert attached.provenance is not None
    assert attached.provenance.discovery_level.value == "L3"
    assert attached.provenance.original_level is None
    assert attached.provenance.verification_status.value == "unverified"


def test_run_store_persists_versioned_health_and_decisions(tmp_path: Path) -> None:
    from src.mcp.run_store import RunStore

    store = RunStore(tmp_path)
    run_id = store.create_run("run-quality")

    source_path = store.save_source_health(
        run_id,
        [{"schema_version": "1", "source_id": "official-feed", "status": "empty"}],
    )
    decision_path = store.save_decisions(
        run_id,
        [{"schema_version": "1", "item_id": "one", "status": "selected"}],
    )
    manifest_path = store.save_manifest(
        run_id,
        {"schema_version": "1", "run_id": run_id, "status": "empty"},
    )

    assert source_path.name == "source_health.json"
    assert decision_path.name == "decisions.json"
    assert manifest_path.name == "manifest.json"
    assert store.load_source_health(run_id)[0]["source_id"] == "official-feed"
    assert store.load_decisions(run_id)[0]["item_id"] == "one"
    assert store.load_manifest(run_id)["status"] == "empty"


def test_github_health_is_per_configured_repository() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if "/good/releases" in request.url.path:
            return httpx.Response(200, json=[])
        return httpx.Response(403, json={"message": "SECRET_SENTINEL"})

    client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    scraper = GitHubScraper(
        [
            GitHubSourceConfig(
                type="repo_releases",
                owner="org",
                repo="good",
                source_id="github-good",
                source_level="L1",
            ),
            GitHubSourceConfig(
                type="repo_releases",
                owner="org",
                repo="blocked",
                source_id="github-blocked",
                source_level="L1",
            ),
        ],
        client,
    )

    batch = asyncio.run(scraper.fetch_with_results(SINCE))
    asyncio.run(client.aclose())

    assert [result.status for result in batch.source_results] == [
        SourceRunStatus.EMPTY,
        SourceRunStatus.FAILED,
    ]
    assert batch.source_results[1].error_code.value == "HTTP_403"
    assert "SECRET_SENTINEL" not in str(batch.source_results[1].model_dump())


def test_github_parse_failure_is_not_reported_as_empty() -> None:
    client = httpx.AsyncClient(
        transport=httpx.MockTransport(
            lambda request: httpx.Response(200, json={"unexpected": "shape"})
        )
    )
    scraper = GitHubScraper(
        [
            GitHubSourceConfig(
                type="repo_releases",
                owner="org",
                repo="broken",
                source_id="github-broken",
                source_level="L1",
            )
        ],
        client,
    )

    batch = asyncio.run(scraper.fetch_with_results(SINCE))
    asyncio.run(client.aclose())

    assert batch.source_results[0].status is SourceRunStatus.FAILED
    assert batch.source_results[0].error_code.value == "PARSE"


def test_hackernews_outer_failure_is_not_reported_as_empty() -> None:
    client = httpx.AsyncClient(
        transport=httpx.MockTransport(lambda request: httpx.Response(403))
    )
    scraper = HackerNewsScraper(
        HackerNewsConfig(source_id="hacker-news", source_level="L3"), client
    )

    batch = asyncio.run(scraper.fetch_with_results(SINCE))
    asyncio.run(client.aclose())

    assert batch.source_results[0].status is SourceRunStatus.FAILED
    assert batch.source_results[0].error_code.value == "HTTP_403"


def test_telegram_failure_is_per_channel_and_sanitized() -> None:
    client = httpx.AsyncClient(
        transport=httpx.MockTransport(
            lambda request: httpx.Response(403, text="SECRET_SENTINEL")
        )
    )
    scraper = TelegramScraper(
        TelegramConfig(
            channels=[
                TelegramChannelConfig(
                    channel="news", source_id="telegram-news", source_level="L3"
                )
            ]
        ),
        client,
    )

    batch = asyncio.run(scraper.fetch_with_results(SINCE))
    asyncio.run(client.aclose())

    assert batch.source_results[0].status is SourceRunStatus.FAILED
    assert batch.source_results[0].error_code.value == "HTTP_403"
    assert "SECRET_SENTINEL" not in str(batch.source_results[0].model_dump())


def test_orchestrator_preserves_legacy_item_api_and_exposes_health(
    monkeypatch,
) -> None:
    feed = """<?xml version="1.0"?><rss><channel><title>Official</title>
      <item><guid>1</guid><title>Release</title>
      <link>https://publisher.example/release</link>
      <pubDate>Wed, 12 Aug 2026 12:30:00 GMT</pubDate></item>
    </channel></rss>"""
    client = httpx.AsyncClient(
        transport=httpx.MockTransport(lambda request: httpx.Response(200, text=feed))
    )

    class ClientContext:
        async def __aenter__(self):
            return client

        async def __aexit__(self, *args):
            await client.aclose()

    monkeypatch.setattr(
        "src.orchestrator.httpx.AsyncClient", lambda **kwargs: ClientContext()
    )
    config = Config(
        ai=AIConfig(provider="openai", model="test", api_key_env="TEST"),
        sources=SourcesConfig(
            hackernews=HackerNewsConfig(enabled=False),
            rss=[
                RSSSourceConfig(
                    source_id="official-feed",
                    source_level="L1",
                    name="Official",
                    url="https://publisher.example/feed.xml",
                )
            ],
            reddit=RedditConfig(enabled=False),
            telegram=TelegramConfig(enabled=False),
        ),
        filtering=FilteringConfig(),
    )
    orchestrator = HorizonOrchestrator(config, SimpleNamespace())

    batch = asyncio.run(orchestrator.fetch_all_sources_with_health(SINCE))

    assert len(batch.items) == 1
    assert batch.source_results[0].source_id == "official-feed"
    assert orchestrator.last_source_results == batch.source_results
