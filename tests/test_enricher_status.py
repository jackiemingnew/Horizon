from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from types import SimpleNamespace

from src.ai.enricher import ContentEnricher
from src.models import ContentItem, SourceType


def _item() -> ContentItem:
    return ContentItem(
        id="rss:one",
        source_type=SourceType.RSS,
        title="One",
        url="https://example.com/one",
        published_at=datetime.now(timezone.utc),
    )


def test_enrichment_failure_marks_failed_when_translation_also_fails(monkeypatch):
    enricher = ContentEnricher(SimpleNamespace(config=SimpleNamespace()))
    item = _item()

    async def fail(value):
        raise RuntimeError("enrichment failed")

    async def no_translation(value):
        return False

    monkeypatch.setattr(enricher, "_enrich_item", fail)
    monkeypatch.setattr(enricher, "_translate_item", no_translation)
    asyncio.run(enricher.enrich_batch([item]))

    assert item.metadata["enrichment_status"] == "failed"


def test_enrichment_failure_marks_incomplete_fallback(monkeypatch):
    enricher = ContentEnricher(SimpleNamespace(config=SimpleNamespace()))
    item = _item()

    async def fail(value):
        raise RuntimeError("enrichment failed")

    async def translated(value):
        return True

    monkeypatch.setattr(enricher, "_enrich_item", fail)
    monkeypatch.setattr(enricher, "_translate_item", translated)
    asyncio.run(enricher.enrich_batch([item]))

    assert item.metadata["enrichment_status"] == "fallback"
