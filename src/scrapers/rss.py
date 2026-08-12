"""RSS feed scraper implementation."""

import calendar
import hashlib
import logging
import os
import re
from datetime import datetime, timezone
from time import perf_counter
from typing import List, Optional
from email.utils import parsedate_to_datetime
import httpx
import feedparser

from .base import BaseScraper
from ..extractors import ExtractorRegistry
from ..models import (
    ContentItem,
    ContentProvenance,
    ProfileStatus,
    RSSSourceConfig,
    SourceErrorCode,
    SourceLevel,
    SourceRunResult,
    SourceRunStatus,
    SourceType,
    VerificationStatus,
)
from ..source_health import SourceFetchBatch

logger = logging.getLogger(__name__)


class RSSScraper(BaseScraper):
    """Scraper for RSS/Atom feeds."""

    def __init__(
        self,
        sources: List[RSSSourceConfig],
        http_client: httpx.AsyncClient,
        extractors: Optional[ExtractorRegistry] = None,
    ):
        """Initialize RSS scraper.

        Args:
            sources: List of RSS feed configurations
            http_client: Shared async HTTP client
            extractors: Optional registry of content extractors for full article fetching
        """
        super().__init__({"sources": sources}, http_client)
        self._extractors = extractors

    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch RSS feed items.

        Args:
            since: Only fetch items published after this time

        Returns:
            List[ContentItem]: Fetched content items
        """
        return (await self.fetch_with_results(since)).items

    async def fetch_with_results(self, since: datetime) -> SourceFetchBatch:
        """Fetch feeds without conflating a genuine empty window with failure."""
        items: List[ContentItem] = []
        results: List[SourceRunResult] = []
        for source in self.config["sources"]:
            if not source.enabled:
                continue
            source_items, result = await self._fetch_feed_result(source, since)
            items.extend(source_items)
            results.append(result)
        return SourceFetchBatch(items=items, source_results=results)

    async def _fetch_feed(
        self, source: RSSSourceConfig, since: datetime
    ) -> List[ContentItem]:
        """Fetch items from a single RSS feed.

        Args:
            source: RSS feed configuration
            since: Only fetch items after this time

        Returns:
            List[ContentItem]: Feed content items
        """
        items, _ = await self._fetch_feed_result(source, since)
        return items

    async def _fetch_feed_result(
        self, source: RSSSourceConfig, since: datetime
    ) -> tuple[List[ContentItem], SourceRunResult]:
        """Fetch one feed and return its typed, sanitized outcome."""
        items: List[ContentItem] = []
        started_at = datetime.now(timezone.utc)
        started_clock = perf_counter()
        error_code: SourceErrorCode | None = None
        error_message: str | None = None

        try:
            # Expand environment variables in URL (e.g. ${LWN_TOKEN})
            feed_url = re.sub(
                r"\$\{(\w+)\}",
                lambda m: os.environ.get(m.group(1), m.group(0)).strip(),
                str(source.url),
            )

            # Fetch feed content
            response = await self.client.get(feed_url, follow_redirects=True)
            response.raise_for_status()

            # Parse feed
            feed = feedparser.parse(response.text)
            has_feed_identity = bool(
                feed.entries
                or getattr(feed, "feed", {}).get("title")
                or getattr(feed, "version", "")
            )
            if getattr(feed, "bozo", False) or not has_feed_identity:
                error_code = SourceErrorCode.PARSE
                error_message = "RSS parse failed: malformed feed"

            for entry in feed.entries:
                # Parse published date
                published_at = self._parse_date(entry)
                if not published_at or published_at < since:
                    continue

                # Generate unique ID from feed URL and entry ID
                feed_id = str(source.url).split("//")[1].replace("/", "_")
                entry_id = entry.get("id", entry.get("link", ""))
                entry_hash = hashlib.sha256(str(entry_id).encode("utf-8")).hexdigest()[
                    :16
                ]

                # Extract content
                content = self._extract_content(entry)

                if source.content_extractor and self._extractors:
                    extractor = self._extractors.get(source.content_extractor)
                    if extractor:
                        url = entry.get("link", "")
                        if url:
                            full = await extractor.extract(url, self.client)
                            if full:
                                content = full

                item = ContentItem(
                    id=self._generate_id("rss", feed_id, entry_hash),
                    source_type=SourceType.RSS,
                    title=entry.get("title", "Untitled"),
                    url=entry.get("link", str(source.url)),
                    content=content,
                    author=entry.get("author", source.name),
                    published_at=published_at,
                    metadata={
                        "feed_name": source.name,
                        "source_id": self._source_id(source),
                        "category": source.category,
                        "tags": [tag.term for tag in entry.get("tags", [])],
                    },
                    provenance=ContentProvenance(
                        discovery_source_id=self._source_id(source),
                        discovery_url=source.url,
                        discovery_level=source.source_level,
                        profile_status=(
                            ProfileStatus.KNOWN
                            if source.source_id and source.source_level
                            else ProfileStatus.MISSING
                        ),
                        original_url=entry.get("link") if source.source_level == SourceLevel.L1 else None,
                        original_domain=(
                            httpx.URL(entry.get("link")).host
                            if source.source_level == SourceLevel.L1 and entry.get("link")
                            else None
                        ),
                        original_level=(
                            SourceLevel.L1 if source.source_level == SourceLevel.L1 else None
                        ),
                        verification_status=(
                            VerificationStatus.DIRECT
                            if source.source_level == SourceLevel.L1
                            else VerificationStatus.UNVERIFIED
                        ),
                    ),
                )
                items.append(item)

        except httpx.HTTPError as e:
            logger.warning("Error fetching RSS feed %s: %s", source.name, e)
            error_code = self._http_error_code(e)
            error_message = self._safe_error_message(e)
        except Exception as e:
            logger.warning("Error parsing RSS feed %s: %s", source.name, e)
            error_code = SourceErrorCode.PARSE
            error_message = self._safe_error_message(e)

        finished_at = datetime.now(timezone.utc)
        if error_code is not None:
            status = SourceRunStatus.PARTIAL if items else SourceRunStatus.FAILED
        elif items:
            status = SourceRunStatus.SUCCESS
        else:
            status = SourceRunStatus.EMPTY
        result = SourceRunResult(
            source_id=self._source_id(source),
            source_type=SourceType.RSS,
            status=status,
            item_count=len(items),
            started_at=started_at,
            finished_at=finished_at,
            latency_ms=max(0, int((perf_counter() - started_clock) * 1000)),
            attempts=1,
            error_code=error_code,
            error_message=error_message,
        )
        return items, result

    @staticmethod
    def _source_id(source: RSSSourceConfig) -> str:
        if source.source_id:
            return source.source_id
        digest = hashlib.sha256(str(source.url).encode("utf-8")).hexdigest()[:12]
        return f"rss-{digest}"

    @staticmethod
    def _http_error_code(error: httpx.HTTPError) -> SourceErrorCode:
        if isinstance(error, httpx.HTTPStatusError):
            status = error.response.status_code
            if status == 403:
                return SourceErrorCode.HTTP_403
            if status == 429:
                return SourceErrorCode.HTTP_429
        if isinstance(error, httpx.TimeoutException):
            return SourceErrorCode.TIMEOUT
        return SourceErrorCode.NETWORK

    @staticmethod
    def _safe_error_message(error: Exception) -> str:
        if isinstance(error, httpx.HTTPStatusError):
            return f"HTTP {error.response.status_code} from configured feed host"
        if isinstance(error, httpx.TimeoutException):
            return "RSS request timed out"
        if isinstance(error, httpx.HTTPError):
            return type(error).__name__
        return f"RSS parse failed: {type(error).__name__}"

    def _parse_date(self, entry: dict) -> datetime:
        """Parse publication date from feed entry.

        Args:
            entry: Feed entry data

        Returns:
            datetime: Parsed publication date or None
        """
        # Try different date fields
        for field in ["published", "updated", "created"]:
            if field in entry:
                try:
                    # Try parsing structured time first
                    if f"{field}_parsed" in entry and entry[f"{field}_parsed"]:
                        return datetime.fromtimestamp(
                            calendar.timegm(entry[f"{field}_parsed"]), tz=timezone.utc
                        )
                    # Fallback to string parsing
                    date_str = entry[field]
                    return parsedate_to_datetime(date_str)
                except Exception:
                    continue

        return None

    def _extract_content(self, entry: dict) -> str:
        """Extract text content from feed entry.

        Args:
            entry: Feed entry data

        Returns:
            str: Extracted text content
        """
        # Try different content fields
        if "summary" in entry:
            return entry.summary
        if "description" in entry:
            return entry.description
        if "content" in entry and entry.content:
            # content is usually a list
            return entry.content[0].get("value", "")

        return ""
