"""Main orchestrator coordinating the entire workflow."""

import asyncio
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, List, Dict, Optional, Protocol
from urllib.parse import urlparse
import httpx
from rich.console import Console

from .models import (
    Config,
    ContentItem,
    DecisionReasonCode,
    DecisionRecord,
    DecisionStatus,
    SourceRunStatus,
)
from .storage.manager import StorageManager
from .services.email import EmailManager
from .services.webhook import WebhookNotifier
from .scrapers.github import GitHubScraper
from .scrapers.hackernews import HackerNewsScraper
from .scrapers.rss import RSSScraper
from .scrapers.reddit import RedditScraper
from .scrapers.telegram import TelegramScraper
from .scrapers.twitter import TwitterScraper
from .scrapers.twitter_playwright import TwitterPlaywrightScraper
from .scrapers.openbb import OpenBBScraper
from .scrapers.ossinsight import OSSInsightScraper
from .scrapers.gdelt import GDELTScraper
from .scrapers.google_news import GoogleNewsScraper
from .ai.client import create_ai_client
from .ai.audit import ModelCallAudit
from .ai.analyzer import ContentAnalyzer
from .ai.summarizer import DailySummarizer
from .ai.enricher import ContentEnricher
from .ai.tokens import get_usage_snapshot, usage_delta
from .source_health import SourceFetchBatch, source_run_result, stable_source_id
from .models import SourceType
from time import perf_counter
from .source_quality import (
    apply_candidate_limits,
    canonicalize_url,
    decision_for_item,
    deduplicate_same_run,
    filter_exact_history,
    resolve_known_originals,
    select_digest,
    source_id_for_item,
)


@dataclass
class BalancedDigestResult:
    """Items and selection statistics from balanced digest filtering."""

    items: List[ContentItem]
    enabled: bool = False
    group_counts: Dict[str, int] = field(default_factory=dict)
    group_limits: Dict[str, Optional[int]] = field(default_factory=dict)
    duplicate_categories: List[str] = field(default_factory=list)


class ArtifactStore(Protocol):
    def create_run(self, run_id: str | None = None) -> str: ...
    def save_items(self, run_id: str, stage: str, items: list[dict[str, Any]]) -> Any: ...
    def save_summary(self, run_id: str, language: str, markdown: str) -> Any: ...
    def save_source_health(self, run_id: str, results: list[dict[str, Any]]) -> Any: ...
    def save_decisions(self, run_id: str, decisions: list[dict[str, Any]]) -> Any: ...
    def save_manifest(self, run_id: str, manifest: dict[str, Any]) -> Any: ...
    def save_model_calls(self, run_id: str, records: list[dict[str, Any]]) -> Any: ...
    def update_meta(self, run_id: str, updates: dict[str, Any]) -> dict[str, Any]: ...


@dataclass
class RunOutcome:
    status: str
    selected_items: List[ContentItem] = field(default_factory=list)
    source_results: list[Any] = field(default_factory=list)
    decisions: List[DecisionRecord] = field(default_factory=list)
    run_id: str | None = None


class SourceQualityRunError(RuntimeError):
    """Fatal V2 status with an explicit CLI/Actions exit contract."""

    def __init__(self, message: str, *, exit_code: int = 2):
        super().__init__(message)
        self.exit_code = exit_code


class HorizonOrchestrator:
    """Orchestrates the complete workflow for content aggregation and analysis."""

    def __init__(self, config: Config, storage: StorageManager):
        """Initialize orchestrator.

        Args:
            config: Application configuration
            storage: Storage manager
        """
        self.config = config
        self.storage = storage
        self.console = Console()
        self.last_source_results = []
        self._model_audit: ModelCallAudit | None = None
        self._pipeline_failures: set[str] = set()
        self._current_stage = "idle"
        self._current_run_id: str | None = None
        self._current_decisions: list[DecisionRecord] = []
        self._usage_start = get_usage_snapshot()
        self._pipeline_counts: dict[str, int] = {}
        self.email_manager = EmailManager(config.email, console=self.console) if config.email else None
        self.webhook_notifier = (
            WebhookNotifier(config.webhook, console=self.console)
            if config.webhook and config.webhook.enabled
            else None
        )

    async def run(
        self,
        force_hours: int = None,
        *,
        artifact_store: ArtifactStore | None = None,
        artifact_run_id: str | None = None,
        publish_pages: bool = True,
    ) -> RunOutcome | None:
        """Execute the complete workflow.

        Args:
            force_hours: Optional override for time window in hours
        """
        if self.config.quality_policy and self.config.quality_policy.enabled:
            try:
                return await self._run_source_quality(
                    force_hours=force_hours,
                    artifact_store=artifact_store,
                    artifact_run_id=artifact_run_id,
                    publish_pages=publish_pages,
                )
            except SourceQualityRunError:
                raise
            except Exception as exc:
                self._persist_unexpected_v2_failure(
                    artifact_store,
                    artifact_run_id or self._current_run_id,
                    stage=self._current_stage,
                )
                raise SourceQualityRunError(
                    "Source-quality stage failed: "
                    f"{self._current_stage} ({type(exc).__name__})"
                ) from exc

        self.console.print("[bold cyan]🌅 Horizon - Starting aggregation...[/bold cyan]\n")

        # Check email subscriptions if configured
        if (
            self.email_manager
            and self.config.email
            and self.config.email.enabled
            and self.config.email.imap_enabled
        ):
            self.console.print("📧 Checking for new email subscriptions...")
            self.email_manager.check_subscriptions(self.storage)

        try:
            # 1. Determine time window
            since = self._determine_time_window(force_hours)
            self.console.print(f"📅 Fetching content since: {since.strftime('%Y-%m-%d %H:%M:%S')}\n")

            # 2. Fetch content from all sources
            all_items = await self.fetch_all_sources(since)
            self.console.print(f"📥 Fetched {len(all_items)} items from all sources\n")

            if not all_items:
                self.console.print("[yellow]No new content found. Exiting.[/yellow]")
                return

            # 3. Merge cross-source duplicates (same URL from different sources)
            merged_items = self.merge_cross_source_duplicates(all_items)
            if len(merged_items) < len(all_items):
                self.console.print(
                    f"🔗 Merged {len(all_items) - len(merged_items)} cross-source duplicates "
                    f"→ {len(merged_items)} unique items\n"
                )

            # 4. Analyze with AI
            analyzed_items = await self._analyze_content(merged_items)
            self.console.print(f"🤖 Analyzed {len(analyzed_items)} items with AI\n")

            # 5. Filter by score threshold
            threshold = self.config.filtering.ai_score_threshold
            important_items = [
                item for item in analyzed_items
                if item.ai_score and item.ai_score >= threshold
            ]
            important_items.sort(key=lambda x: x.ai_score or 0, reverse=True)

            self.console.print(
                f"⭐️ {len(important_items)} items scored ≥ {threshold}\n"
            )

            # 5.5 Semantic deduplication: drop items covering the same topic
            deduped_items = await self.merge_topic_duplicates(important_items)
            if len(deduped_items) < len(important_items):
                self.console.print(
                    f"🧹 Removed {len(important_items) - len(deduped_items)} topic duplicates "
                    f"→ {len(deduped_items)} unique items\n"
                )
            important_items = deduped_items

            # 5.6 Optional second-stage Twitter reply expansion + targeted re-analysis
            await self._expand_twitter_discussion(important_items)

            # 5.7 Apply per-category and global digest limits before enrichment
            balanced_result = self.apply_balanced_digest(important_items)
            important_items = balanced_result.items

            # Show per-sub-source selection breakdown
            selected_counts: Dict[str, int] = defaultdict(int)
            for item in important_items:
                key = f"{item.source_type.value}/{self._sub_source_label(item)}"
                selected_counts[key] += 1
            for source_key, count in sorted(selected_counts.items()):
                self.console.print(f"      • {source_key}: {count}")
            self.console.print("")

            # 6. Search related stories + enrich with background knowledge (2nd AI pass)
            await self._enrich_important_items(important_items)

            # 7. Generate and save daily summaries for each configured language
            today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            for lang in self.config.ai.languages:
                summarizer = DailySummarizer()
                summary = await summarizer.generate_summary(important_items, today, len(all_items), language=lang)

                # Save to data/summaries/
                summary_path = self.storage.save_daily_summary(today, summary, language=lang)
                self.console.print(f"💾 Saved {lang.upper()} summary to: {summary_path}\n")

                if publish_pages:
                    try:
                        dest_path = self._write_pages_post(today, lang, summary)
                        self.console.print(
                            f"📄 Copied {lang.upper()} summary to GitHub Pages: {dest_path}\n"
                        )
                    except Exception as e:
                        self.console.print(
                            f"[yellow]⚠️  Failed to copy {lang.upper()} summary to docs/: {e}[/yellow]\n"
                        )

                # Send email if configured
                if self.email_manager and self.config.email and self.config.email.enabled:
                    self.console.print(f"📧 Sending {lang.upper()} email summary...")
                    subscribers = self.storage.load_subscribers()
                    subject = f"Horizon Summary ({lang.upper()}) - {today}"
                    self.email_manager.send_daily_summary(summary, subject, subscribers)

                # Send webhook notification if configured
                if self.webhook_notifier:
                    await self.webhook_notifier.send_daily_summary(
                        summary=summary,
                        important_items=important_items,
                        all_items_count=len(all_items),
                        date=today,
                        lang=lang,
                        summarizer=summarizer,
                    )

            self.console.print("[bold green]✅ Horizon completed successfully![/bold green]")
            usage = get_usage_snapshot()
            if usage.total_tokens > 0:
                self.console.print(
                    f"\n🧮 Token usage this run: "
                    f"{usage.total_tokens} tokens "
                    f"(input: {usage.total_input_tokens}, output: {usage.total_output_tokens})"
                )
                for provider, u in sorted(usage.per_provider.items()):
                    if u.total <= 0:
                        continue
                    self.console.print(
                        f"   • {provider}: {u.total} tokens "
                        f"(in: {u.input_tokens}, out: {u.output_tokens})"
                    )

        except Exception as e:
            self.console.print(f"[bold red]❌ Error: {e}[/bold red]")

            # Send webhook failure notification if configured
            if self.webhook_notifier:
                await self.webhook_notifier.send_failure(
                    date=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                    error_message=str(e),
                )

            raise

    async def _run_source_quality(
        self,
        *,
        force_hours: int | None,
        artifact_store: ArtifactStore | None,
        artifact_run_id: str | None,
        publish_pages: bool,
    ) -> RunOutcome:
        """Execute the opt-in V2 pipeline without changing legacy defaults."""
        policy = self.config.quality_policy
        if policy is None or not policy.enabled:  # pragma: no cover - dispatch guard
            raise RuntimeError("Source Quality V2 is not enabled")
        self._model_audit = ModelCallAudit(self.config.ai)
        self._pipeline_failures = set()
        self._current_decisions = []
        self._pipeline_counts = {}
        self._usage_start = get_usage_snapshot()
        run_id = (
            artifact_store.create_run(artifact_run_id)
            if artifact_store is not None
            else artifact_run_id
        )
        self._current_run_id = run_id
        self._current_stage = "preflight"
        # Client construction validates provider configuration and required
        # environment variables without making a remote model request.
        self._create_ai_client("preflight")
        since = self._determine_time_window(force_hours)
        self.console.print("[bold cyan]🌅 Horizon Source Quality V2[/bold cyan]\n")
        self.console.print(
            f"📅 Fetching content since: {since.strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        self._current_stage = "fetch"
        batch = await self.fetch_all_sources_with_health(since)
        source_results = batch.source_results
        self._pipeline_counts["fetched"] = len(batch.items)
        health = self._classify_source_health(source_results)
        if artifact_store is not None and run_id is not None:
            artifact_store.save_source_health(
                run_id, [value.model_dump(mode="json") for value in source_results]
            )
            artifact_store.save_items(
                run_id,
                "fetched",
                [item.model_dump(mode="json") for item in batch.items],
            )

        if health["status"] == "failed":
            manifest = self._build_manifest(
                run_id=run_id,
                status="failed",
                health=health,
                source_results=source_results,
                pipeline_counts={"fetched": len(batch.items), "selected": 0},
            )
            if artifact_store is not None and run_id is not None:
                artifact_store.save_decisions(run_id, [])
                artifact_store.save_model_calls(run_id, [])
                artifact_store.save_manifest(run_id, manifest)
                artifact_store.update_meta(run_id, manifest)
            raise SourceQualityRunError(
                "Source-quality health gate failed: "
                + ", ".join(health["failed_source_ids"] or ["no healthy source"])
            )

        self._current_stage = "deduplication"
        fetched = batch.items
        same_run_result = deduplicate_same_run(fetched)
        merged = same_run_result.items
        self._pipeline_counts["same_run_unique"] = len(merged)
        history = self._load_recent_history(
            artifact_store, run_id, history_days=policy.deduplication.history_days
        )
        initial_history_result = filter_exact_history(merged, history, policy)
        self._pipeline_counts["history_unique"] = len(initial_history_result.items)
        candidate_result = apply_candidate_limits(initial_history_result.items, policy)
        resolved = resolve_known_originals(candidate_result.items, self.config)
        resolved_history_result = filter_exact_history(resolved, history, policy)
        resolved_ids = {item.id for item in resolved_history_result.items}
        post_resolution_history_decisions = [
            decision
            for decision in resolved_history_result.decisions
            if decision.item_id not in {
                existing.item_id for existing in initial_history_result.decisions
            }
        ]
        candidates = list(resolved_history_result.items)
        refilled_ids: set[str] = set()
        for removed in resolved:
            if removed.id in resolved_ids:
                continue
            source_id = source_id_for_item(removed)
            for replacement in candidate_result.overflow.get(source_id, []):
                if replacement.id in refilled_ids:
                    continue
                [resolved_replacement] = resolve_known_originals(
                    [replacement], self.config
                )
                replacement_history = filter_exact_history(
                    [resolved_replacement], history, policy
                )
                if replacement_history.items:
                    candidates.extend(replacement_history.items)
                    refilled_ids.add(replacement.id)
                    break
                post_resolution_history_decisions.extend(
                    replacement_history.decisions
                )
        candidate_decisions = [
            decision
            for decision in candidate_result.decisions
            if decision.item_id not in refilled_ids
        ]
        self._pipeline_counts["known_originals_resolved"] = sum(
            item.provenance is not None
            and item.provenance.verification_status.value == "resolved"
            for item in candidates
        )
        self._pipeline_counts["ai_candidates"] = len(candidates)
        if artifact_store is not None and run_id is not None:
            artifact_store.save_items(
                run_id, "raw", [item.model_dump(mode="json") for item in candidates]
            )

        self._current_stage = "analysis"
        analyzed = await self._analyze_content(candidates) if candidates else []
        self._pipeline_counts["scored"] = len(analyzed)
        if artifact_store is not None and run_id is not None:
            artifact_store.save_items(
                run_id, "scored", [item.model_dump(mode="json") for item in analyzed]
            )
        threshold = self.config.filtering.ai_score_threshold
        thresholded: list[ContentItem] = []
        threshold_decisions: list[DecisionRecord] = []
        for item in analyzed:
            if item.ai_score is not None and item.ai_score >= threshold:
                thresholded.append(item)
                continue
            failed = item.ai_score is None or item.metadata.get("ai_status") == "failed"
            threshold_decisions.append(
                decision_for_item(
                    item,
                    DecisionStatus.REJECTED,
                    (
                        DecisionReasonCode.MODEL_ANALYSIS_FAILED
                        if failed
                        else DecisionReasonCode.BELOW_AI_THRESHOLD
                    ),
                    (
                        "Model analysis failed; the item was not assigned a synthetic zero."
                        if failed
                        else "AI relevance score was below the configured threshold."
                    ),
                    {
                        "ai_score": item.ai_score,
                        "threshold": threshold,
                    },
                    stage="analysis",
                )
            )
        thresholded.sort(key=lambda item: item.ai_score or 0, reverse=True)
        self._pipeline_counts["above_threshold"] = len(thresholded)
        if artifact_store is not None and run_id is not None:
            artifact_store.save_items(
                run_id,
                "thresholded",
                [item.model_dump(mode="json") for item in thresholded],
            )

        self._current_stage = "semantic_deduplication"
        deduped = await self.merge_topic_duplicates(thresholded)
        self._pipeline_counts["semantic_unique"] = len(deduped)
        deduped_ids = {item.id for item in deduped}
        topic_decisions = [
            decision_for_item(
                item,
                DecisionStatus.REJECTED,
                DecisionReasonCode.TOPIC_DUPLICATE,
                "Removed as a same-run semantic topic duplicate.",
                stage="semantic_deduplication",
            )
            for item in thresholded
            if item.id not in deduped_ids
        ]
        if artifact_store is not None and run_id is not None:
            artifact_store.save_items(
                run_id, "deduped", [item.model_dump(mode="json") for item in deduped]
            )

        self._current_stage = "selection"
        await self._expand_twitter_discussion(deduped)
        selection = select_digest(deduped, policy)
        selected = selection.selected
        self._pipeline_counts["selected"] = len(selected)
        decisions = self._unique_decisions(
            [
                *same_run_result.decisions,
                *initial_history_result.decisions,
                *candidate_decisions,
                *post_resolution_history_decisions,
                *threshold_decisions,
                *topic_decisions,
                *selection.decisions,
            ]
        )
        self._current_decisions = decisions
        if artifact_store is not None and run_id is not None:
            artifact_store.save_items(
                run_id, "filtered", [item.model_dump(mode="json") for item in selected]
            )
            artifact_store.save_decisions(
                run_id, [value.model_dump(mode="json") for value in decisions]
            )

        self._current_stage = "enrichment"
        await self._enrich_important_items(selected)
        if artifact_store is not None and run_id is not None:
            artifact_store.save_items(
                run_id, "enriched", [item.model_dump(mode="json") for item in selected]
            )
        self._current_stage = "summary"
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        for lang in self.config.ai.languages:
            summary = await DailySummarizer().generate_summary(
                selected, today, len(fetched), language=lang
            )
            summary_path = self.storage.save_daily_summary(today, summary, language=lang)
            self.console.print(f"💾 Saved {lang.upper()} summary to: {summary_path}\n")
            if artifact_store is not None and run_id is not None:
                artifact_store.save_summary(run_id, lang, summary)
            if publish_pages:
                self._write_pages_post(today, lang, summary)

        self._current_stage = "artifacts"
        if artifact_store is not None and run_id is not None:
            artifact_store.save_decisions(
                run_id, [value.model_dump(mode="json") for value in decisions]
            )
            self._save_published_history(artifact_store, run_id, selected)
        pipeline_counts = dict(self._pipeline_counts)
        failed_stages = set(self._pipeline_failures)
        if any(
            value.reason_code is DecisionReasonCode.MODEL_ANALYSIS_FAILED
            for value in threshold_decisions
        ):
            failed_stages.add("analysis")
        if any(
            item.metadata.get("enrichment_status") in {"failed", "fallback"}
            for item in selected
        ):
            failed_stages.add("enrichment")
        run_status = health["status"]
        if failed_stages and run_status in {"complete", "empty"}:
            run_status = "partial"
        manifest = self._build_manifest(
            run_id=run_id,
            status=run_status,
            health=health,
            source_results=source_results,
            pipeline_counts=pipeline_counts,
            failed_stages=sorted(failed_stages),
        )
        if artifact_store is not None and run_id is not None:
            artifact_store.save_model_calls(
                run_id,
                [value.model_dump(mode="json") for value in self._model_audit.records],
            )
            artifact_store.save_manifest(run_id, manifest)
            artifact_store.update_meta(run_id, manifest)
        self.console.print(
            f"[bold green]✅ Horizon V2 completed with status: {run_status}[/bold green]"
        )
        return RunOutcome(
            status=run_status,
            selected_items=selected,
            source_results=source_results,
            decisions=decisions,
            run_id=run_id,
        )

    def _persist_unexpected_v2_failure(
        self,
        artifact_store: ArtifactStore | None,
        run_id: str | None,
        *,
        stage: str,
    ) -> None:
        """Best-effort safe failure envelope for local and shadow runs."""
        if artifact_store is None or run_id is None:
            return
        try:
            artifact_store.create_run(run_id)
            source_results = list(self.last_source_results)
            health = (
                self._classify_source_health(source_results)
                if source_results
                else {
                    "status": "failed",
                    "healthy_source_ratio": 0.0,
                    "failed_source_ids": [],
                    "required_failed_source_ids": [],
                }
            )
            artifact_store.save_source_health(
                run_id,
                [value.model_dump(mode="json") for value in source_results],
            )
            artifact_store.save_decisions(
                run_id,
                [value.model_dump(mode="json") for value in self._current_decisions],
            )
            records = self._model_audit.records if self._model_audit else []
            artifact_store.save_model_calls(
                run_id, [value.model_dump(mode="json") for value in records]
            )
            manifest = self._build_manifest(
                run_id=run_id,
                status="failed",
                health=health,
                source_results=source_results,
                pipeline_counts=dict(self._pipeline_counts),
                failed_stages=[stage],
            )
            artifact_store.save_manifest(run_id, manifest)
            artifact_store.update_meta(run_id, manifest)
        except Exception:
            # Never replace the original typed failure with reporting failure.
            return

    def _classify_source_health(self, results: list[Any]) -> dict[str, Any]:
        policy = self.config.quality_policy
        if policy is None:
            raise RuntimeError("Source Quality V2 is not configured")
        healthy = [
            result
            for result in results
            if result.status in {SourceRunStatus.SUCCESS, SourceRunStatus.EMPTY}
        ]
        failed = [
            result
            for result in results
            if result.status in {SourceRunStatus.FAILED, SourceRunStatus.PARTIAL}
        ]
        failed_ids = [result.source_id for result in failed]
        required_failed = sorted(
            set(failed_ids) & set(policy.run_health.required_source_ids)
        )
        ratio = len(healthy) / len(results) if results else 0.0
        if (
            not results
            or not healthy
            or required_failed
            or ratio < policy.run_health.min_healthy_source_ratio
        ):
            status = "failed"
        elif failed:
            status = "partial"
        elif not any(result.item_count for result in results):
            status = "empty"
        else:
            status = "complete"
        return {
            "status": status,
            "healthy_source_ratio": round(ratio, 4),
            "failed_source_ids": failed_ids,
            "required_failed_source_ids": required_failed,
        }

    @staticmethod
    def _unique_decisions(values: list[DecisionRecord]) -> list[DecisionRecord]:
        """Keep the first terminal stage decision for every candidate."""
        result: list[DecisionRecord] = []
        seen: set[str] = set()
        for value in values:
            if value.item_id in seen:
                continue
            seen.add(value.item_id)
            result.append(value)
        return result

    def _build_manifest(
        self,
        *,
        run_id: str | None,
        status: str,
        health: dict[str, Any],
        source_results: list[Any],
        pipeline_counts: dict[str, int],
        failed_stages: list[str] | None = None,
    ) -> dict[str, Any]:
        source_counts = {key: 0 for key in ("success", "empty", "partial", "failed", "skipped")}
        for result in source_results:
            source_counts[result.status.value] += 1
        usage = usage_delta(self._usage_start)
        return {
            "schema_version": "1",
            "run_id": run_id or "ephemeral",
            "status": status,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "healthy_source_ratio": health["healthy_source_ratio"],
            "source_counts": source_counts,
            "pipeline_counts": pipeline_counts,
            "failed_source_ids": health["failed_source_ids"],
            "failed_stages": failed_stages or [],
            "token_usage": {
                "input": usage.total_input_tokens,
                "output": usage.total_output_tokens,
                "total": usage.total_tokens,
            },
        }

    @staticmethod
    def _load_recent_history(
        store: ArtifactStore | None,
        current_run_id: str | None,
        *,
        history_days: int,
    ) -> list[dict[str, Any]]:
        if store is None or not hasattr(store, "list_runs") or not hasattr(store, "read_json"):
            return []
        cutoff = datetime.now(timezone.utc) - timedelta(days=history_days)
        records: list[dict[str, Any]] = []
        for run in store.list_runs(limit=max(20, history_days * 10)):
            run_id = run.get("run_id")
            if not run_id or run_id == current_run_id:
                continue
            try:
                values = store.read_json(run_id, "published_history.json")
            except FileNotFoundError:
                continue
            for value in values if isinstance(values, list) else []:
                published = value.get("published_at")
                try:
                    stamp = datetime.fromisoformat(str(published).replace("Z", "+00:00"))
                except (TypeError, ValueError):
                    continue
                if stamp >= cutoff:
                    records.append(value)
        return records

    @staticmethod
    def _save_published_history(
        store: ArtifactStore, run_id: str, items: list[ContentItem]
    ) -> None:
        if not hasattr(store, "write_json"):
            return
        values = []
        for item in items:
            metadata = item.metadata
            values.append(
                {
                    "item_id": item.id,
                    "event_id": metadata.get("event_id") or item.id,
                    "url": canonicalize_url(item.url),
                    "native_id": metadata.get("native_id") or item.id,
                    "material_update_marker": metadata.get("material_update_marker"),
                    "published_at": item.published_at.isoformat(),
                }
            )
        store.write_json(run_id, "published_history.json", values)

    @staticmethod
    def _write_pages_post(today: str, lang: str, summary: str) -> Path:
        post_filename = f"{today}-summary-{lang}.md"
        posts_dir = Path("docs/_posts")
        posts_dir.mkdir(parents=True, exist_ok=True)
        dest_path = posts_dir / post_filename
        front_matter = (
            "---\n"
            "layout: default\n"
            f'title: "Horizon Summary: {today} ({lang.upper()})"\n'
            f"date: {today}\n"
            f"lang: {lang}\n"
            "---\n\n"
        )
        summary_content = summary
        first_line = summary_content.strip().split("\n")[0]
        if first_line.startswith("# "):
            parts = summary_content.split("\n", 1)
            if len(parts) > 1:
                summary_content = parts[1].strip()
        dest_path.write_text(front_matter + summary_content, encoding="utf-8")
        return dest_path

    def _determine_time_window(self, force_hours: int = None) -> datetime:
        if force_hours:
            since = datetime.now(timezone.utc) - timedelta(hours=force_hours)
        else:
            hours = self.config.filtering.time_window_hours
            since = datetime.now(timezone.utc) - timedelta(hours=hours)
        return since

    async def fetch_all_sources(self, since: datetime) -> List[ContentItem]:
        """Fetch content from all configured sources.

        This is a stable stage entry point for integrations such as MCP.

        Args:
            since: Fetch items published after this time

        Returns:
            List[ContentItem]: All fetched items
        """
        batch = await self.fetch_all_sources_with_health(since)
        return batch.items

    async def fetch_all_sources_with_health(self, since: datetime) -> SourceFetchBatch:
        """Fetch all sources and retain one structured result per sub-source.

        The legacy :meth:`fetch_all_sources` continues to return only items so
        MCP and third-party callers do not observe a breaking shape change.
        """
        async with httpx.AsyncClient(timeout=30.0) as client:
            tasks = []

            # GitHub sources
            if self.config.sources.github:
                github_scraper = GitHubScraper(self.config.sources.github, client)
                tasks.append(self._fetch_with_health_progress("GitHub", SourceType.GITHUB, github_scraper, since))

            # Hacker News
            if self.config.sources.hackernews.enabled:
                hn_scraper = HackerNewsScraper(self.config.sources.hackernews, client)
                tasks.append(self._fetch_with_health_progress("Hacker News", SourceType.HACKERNEWS, hn_scraper, since))

            # RSS feeds
            if self.config.sources.rss:
                from .extractors import ExtractorRegistry
                rss_scraper = RSSScraper(
                    self.config.sources.rss,
                    client,
                    ExtractorRegistry(self.config.extractors),
                )
                tasks.append(self._fetch_with_health_progress("RSS Feeds", SourceType.RSS, rss_scraper, since))

            # Reddit
            if self.config.sources.reddit.enabled:
                reddit_scraper = RedditScraper(self.config.sources.reddit, client)
                tasks.append(self._fetch_with_health_progress("Reddit", SourceType.REDDIT, reddit_scraper, since))

            # Telegram
            if self.config.sources.telegram.enabled:
                telegram_scraper = TelegramScraper(self.config.sources.telegram, client)
                tasks.append(self._fetch_with_health_progress("Telegram", SourceType.TELEGRAM, telegram_scraper, since))

            # Twitter (Apify or Playwright mode)
            if self.config.sources.twitter and self.config.sources.twitter.enabled:
                tw_cfg = self.config.sources.twitter
                if tw_cfg.mode == "playwright":
                    twitter_scraper = TwitterPlaywrightScraper(tw_cfg)
                else:
                    twitter_scraper = TwitterScraper(tw_cfg, client)
                tasks.append(self._fetch_with_health_progress("Twitter", SourceType.TWITTER, twitter_scraper, since))

            # OpenBB (financial news / filings via the OpenBB Platform SDK)
            if self.config.sources.openbb and self.config.sources.openbb.enabled:
                openbb_scraper = OpenBBScraper(self.config.sources.openbb, client)
                tasks.append(self._fetch_with_health_progress("OpenBB", SourceType.OPENBB, openbb_scraper, since))

            # OSS Insight trending repos
            if self.config.sources.ossinsight and self.config.sources.ossinsight.enabled:
                oss_scraper = OSSInsightScraper(self.config.sources.ossinsight, client)
                tasks.append(self._fetch_with_health_progress("OSS Insight", SourceType.OSSINSIGHT, oss_scraper, since))

            # GDELT 2.0 DOC API (key-less global news)
            if self.config.sources.gdelt and self.config.sources.gdelt.enabled:
                gdelt_scraper = GDELTScraper(self.config.sources.gdelt, client)
                tasks.append(self._fetch_with_health_progress("GDELT", SourceType.GDELT, gdelt_scraper, since))

            # Google News RSS (key-less news search)
            if self.config.sources.google_news and self.config.sources.google_news.enabled:
                gn_scraper = GoogleNewsScraper(self.config.sources.google_news, client)
                tasks.append(self._fetch_with_health_progress("Google News", SourceType.GOOGLE_NEWS, gn_scraper, since))

            # Fetch all concurrently
            results = await asyncio.gather(*tasks, return_exceptions=True)

            # Flatten results
            all_items = []
            source_results = []
            for result in results:
                if isinstance(result, Exception):
                    self.console.print(f"[red]Error fetching source: {result}[/red]")
                elif isinstance(result, SourceFetchBatch):
                    all_items.extend(result.items)
                    source_results.extend(result.source_results)

            self.last_source_results = source_results
            return SourceFetchBatch(items=all_items, source_results=source_results)

    async def _fetch_with_health_progress(
        self,
        name: str,
        source_type: SourceType,
        scraper,
        since: datetime,
    ) -> SourceFetchBatch:
        """Use structured scraper health when available; degrade explicitly otherwise."""
        self.console.print(f"🔍 Fetching from {name}...")
        started_at = datetime.now(timezone.utc)
        started_clock = perf_counter()
        try:
            if hasattr(scraper, "fetch_with_results"):
                batch = await scraper.fetch_with_results(since)
            else:
                items = await scraper.fetch(since)
                fallback_error = RuntimeError(
                    "Structured per-sub-source health is not implemented"
                )
                batch = SourceFetchBatch(
                    items=items,
                    source_results=[
                        source_run_result(
                            source_id=stable_source_id(source_type.value, name),
                            source_type=source_type,
                            started_at=started_at,
                            started_clock=started_clock,
                            items=items,
                            error=fallback_error,
                            partial=True,
                        )
                    ],
                )
        except Exception as exc:
            batch = SourceFetchBatch(
                items=[],
                source_results=[
                    source_run_result(
                        source_id=stable_source_id(source_type.value, name),
                        source_type=source_type,
                        started_at=started_at,
                        started_clock=started_clock,
                        items=[],
                        error=exc,
                    )
                ],
            )
        self.console.print(f"   Found {len(batch.items)} items from {name}")
        for result in batch.source_results:
            if result.status.value in {"failed", "partial"}:
                self.console.print(
                    f"      [yellow]• {result.source_id}: {result.status.value} "
                    f"({result.error_code.value if result.error_code else 'UNKNOWN'})[/yellow]"
                )
        return batch

    async def _fetch_with_progress(self, name: str, scraper, since: datetime) -> List[ContentItem]:
        """Fetch from a scraper with progress indication.

        Args:
            name: Source name for display
            scraper: Scraper instance
            since: Fetch items after this time

        Returns:
            List[ContentItem]: Fetched items
        """
        self.console.print(f"🔍 Fetching from {name}...")
        items = await scraper.fetch(since)
        self.console.print(f"   Found {len(items)} items from {name}")

        # Show per-sub-source breakdown when there are multiple sub-sources
        sub_counts: Dict[str, int] = defaultdict(int)
        for item in items:
            sub_counts[self._sub_source_label(item)] += 1
        if len(sub_counts) > 1:
            for sub, count in sorted(sub_counts.items()):
                self.console.print(f"      • {sub}: {count}")

        return items

    @staticmethod
    def _sub_source_label(item: ContentItem) -> str:
        """Return a human-readable sub-source label for an item."""
        meta = item.metadata
        if meta.get("subreddit"):
            return f"r/{meta['subreddit']}"
        if meta.get("feed_name"):
            return meta["feed_name"]
        if meta.get("channel"):
            return f"@{meta['channel']}"
        if meta.get("period") and meta.get("repo"):
            return f"ossinsight:{meta.get('primary_language', 'all')}"
        if meta.get("repo"):
            return meta["repo"]
        if meta.get("watchlist"):
            return meta["watchlist"]
        if meta.get("source_name"):
            return meta["source_name"]
        if meta.get("gn_query"):
            return f"google_news:{meta['gn_query']}"
        if meta.get("domain"):
            return meta["domain"]
        return item.author or "unknown"

    def merge_cross_source_duplicates(self, items: List[ContentItem]) -> List[ContentItem]:
        """Merge items that point to the same URL from different sources.

        This is a stable stage helper for integrations such as MCP.

        Keeps the item with the richest content and combines metadata.

        Args:
            items: Items to deduplicate

        Returns:
            List[ContentItem]: Deduplicated items
        """
        def normalize_url(url: str) -> str:
            parsed = urlparse(str(url))
            # Strip www prefix, trailing slashes, and fragments
            host = parsed.hostname or ""
            if host.startswith("www."):
                host = host[4:]
            path = parsed.path.rstrip("/")
            return f"{host}{path}"

        # Group by normalized URL
        url_groups: Dict[str, List[ContentItem]] = {}
        for item in items:
            key = normalize_url(str(item.url))
            url_groups.setdefault(key, []).append(item)

        merged = []
        for key, group in url_groups.items():
            if len(group) == 1:
                merged.append(group[0])
                continue

            # Pick the item with the richest content as primary
            primary = max(group, key=lambda x: len(x.content or ""))

            # Merge metadata and source info from other items
            all_sources = set()
            for item in group:
                all_sources.add(item.source_type.value)
                # Merge metadata (engagement, discussion, etc.)
                for mk, mv in item.metadata.items():
                    if mk not in primary.metadata or not primary.metadata[mk]:
                        primary.metadata[mk] = mv

                # Append content (e.g., comments from another source)
                if item is not primary and item.content:
                    if primary.content and item.content not in primary.content:
                        primary.content = (primary.content or "") + f"\n\n--- From {item.source_type.value} ---\n" + item.content

            primary.metadata["merged_sources"] = list(all_sources)
            merged.append(primary)

        return merged

    async def merge_topic_duplicates(self, items: List[ContentItem]) -> List[ContentItem]:
        """Merge items covering the same topic using AI semantic deduplication.

        This is a stable stage helper for integrations such as MCP.

        Sends all item titles, tags, and summaries to AI in a single call.
        Items must already be sorted by ai_score descending so that the first
        item in each duplicate group is always the highest-scored one.
        Content (comments) from duplicate items is merged into the primary.

        Falls back to returning items unchanged if the AI call fails.
        """
        if len(items) <= 1:
            return items

        from .ai.prompts import TOPIC_DEDUP_SYSTEM, TOPIC_DEDUP_USER
        from .ai.utils import parse_json_response

        # Build the item list for the prompt
        lines = []
        for i, item in enumerate(items):
            tags = ", ".join(item.ai_tags) if item.ai_tags else "—"
            summary = item.ai_summary or "—"
            lines.append(f"[{i}] {item.title}\n    Tags: {tags}\n    Summary: {summary}")
        items_text = "\n\n".join(lines)

        try:
            ai_client = self._create_ai_client("semantic_deduplication")
            response = await ai_client.complete(
                system=TOPIC_DEDUP_SYSTEM,
                user=TOPIC_DEDUP_USER.format(items=items_text),
            )
            result = parse_json_response(response)
            if result is None:
                self._pipeline_failures.add("semantic_deduplication")
                self.console.print("[yellow]  dedup: could not parse AI response, skipping[/yellow]")
                return items

            duplicate_groups = result.get("duplicates", [])
        except Exception as e:
            self._pipeline_failures.add("semantic_deduplication")
            self.console.print(f"[yellow]  dedup: AI call failed ({e}), skipping[/yellow]")
            return items

        if not duplicate_groups:
            return items

        # Build a set of indices to drop (all non-primary duplicates)
        drop_indices: set[int] = set()
        for group in duplicate_groups:
            if not isinstance(group, list) or len(group) < 2:
                continue
            primary_idx = group[0]
            if primary_idx < 0 or primary_idx >= len(items):
                continue
            primary = items[primary_idx]
            for dup_idx in group[1:]:
                if not isinstance(dup_idx, int) or dup_idx < 0 or dup_idx >= len(items):
                    continue
                if dup_idx == primary_idx:
                    continue
                dup = items[dup_idx]
                # Merge comments/content from the duplicate into the primary
                if dup.content:
                    if not primary.content or dup.content not in primary.content:
                        label = dup.source_type.value
                        primary.content = (primary.content or "") + f"\n\n--- From {label} ---\n{dup.content}"
                self.console.print(
                    f"   [dim]dedup: keep [{primary_idx}] {primary.title}[/dim]\n"
                    f"   [dim]       drop [{dup_idx}] {dup.title}[/dim]"
                )
                drop_indices.add(dup_idx)

        return [item for i, item in enumerate(items) if i not in drop_indices]

    def apply_balanced_digest(
        self,
        items: List[ContentItem],
        *,
        log: bool = True,
    ) -> BalancedDigestResult:
        """Apply configured category quotas and the final item cap.

        Categories are read from ``item.metadata["category"]``. If a category
        appears in more than one configured group, the first group in config
        order wins.
        """
        filtering = self.config.filtering
        groups = filtering.category_groups
        max_items = filtering.max_items

        if not groups and max_items is None:
            return BalancedDigestResult(items=items)

        sorted_items = sorted(
            items,
            key=lambda item: item.ai_score or 0,
            reverse=True,
        )

        category_to_group: Dict[str, str] = {}
        duplicate_categories: List[str] = []
        for group_key, group in groups.items():
            for category in group.categories:
                if category in category_to_group:
                    if category_to_group[category] != group_key:
                        duplicate_categories.append(category)
                    continue
                category_to_group[category] = group_key

        if log:
            for category in sorted(set(duplicate_categories)):
                first_group = category_to_group[category]
                self.console.print(
                    f"[yellow]Warning: category '{category}' is configured in multiple "
                    f"groups; using '{first_group}'.[/yellow]"
                )

        selected: List[tuple[ContentItem, str]] = []
        group_counts: Dict[str, int] = defaultdict(int)
        default_group = filtering.default_group

        for item in sorted_items:
            category = item.metadata.get("category")
            group_key = (
                category_to_group.get(category, default_group)
                if isinstance(category, str)
                else default_group
            )

            if group_key in groups:
                limit = groups[group_key].limit
            else:
                limit = filtering.default_group_limit

            if limit is not None and group_counts[group_key] >= limit:
                continue

            selected.append((item, group_key))
            group_counts[group_key] += 1

        if max_items is not None:
            selected = selected[:max_items]

        final_counts: Dict[str, int] = defaultdict(int)
        for _, group_key in selected:
            final_counts[group_key] += 1

        group_limits: Dict[str, Optional[int]] = {
            group_key: group.limit for group_key, group in groups.items()
        }
        group_limits.setdefault(default_group, filtering.default_group_limit)

        if log:
            self.console.print(
                f"⚖️ Balanced digest selected {len(selected)}/{len(items)} items"
            )
            for group_key, group in groups.items():
                label = group.name or group_key
                self.console.print(
                    f"      • {label}: {final_counts.get(group_key, 0)}/{group.limit}"
                )
            if (
                final_counts.get(default_group, 0)
                or filtering.default_group_limit is not None
            ):
                limit_label = (
                    str(filtering.default_group_limit)
                    if filtering.default_group_limit is not None
                    else "unlimited"
                )
                self.console.print(
                    f"      • {default_group}: "
                    f"{final_counts.get(default_group, 0)}/{limit_label}"
                )
            self.console.print("")

        return BalancedDigestResult(
            items=[item for item, _ in selected],
            enabled=True,
            group_counts=dict(final_counts),
            group_limits=group_limits,
            duplicate_categories=sorted(set(duplicate_categories)),
        )

    async def _expand_twitter_discussion(self, items: List[ContentItem]) -> None:
        """Second-stage: fetch reply text for important Twitter items and re-analyze.

        Only runs when sources.twitter.fetch_reply_text is True.
        Bounded by max_tweets_to_expand to control cost.
        """
        tw_cfg = self.config.sources.twitter
        if not tw_cfg or not tw_cfg.enabled or not tw_cfg.fetch_reply_text:
            return

        from .models import SourceType

        twitter_items = [
            item for item in items
            if item.source_type == SourceType.TWITTER
        ][:tw_cfg.max_tweets_to_expand]

        if not twitter_items:
            return

        self.console.print(
            f"💬 Fetching reply text for {len(twitter_items)} Twitter items..."
        )

        async with httpx.AsyncClient(timeout=30.0) as client:
            if tw_cfg.mode == "playwright":
                self.console.print(
                    "   [yellow]Reply expansion not yet supported in Playwright mode.[/yellow]"
                )
                return
            scraper = TwitterScraper(tw_cfg, client)
            expanded = []
            for item in twitter_items:
                try:
                    reply_lines = await scraper.fetch_replies_for_item(item)
                    if TwitterScraper.append_discussion_content(item, reply_lines):
                        expanded.append(item)
                        self.console.print(
                            f"   💬 {len(reply_lines)} replies added to: {item.title[:60]}"
                        )
                except Exception as exc:
                    self.console.print(
                        f"   [yellow]⚠️  Reply fetch failed for {item.id}: {exc}[/yellow]"
                    )

        if not expanded:
            return

        self.console.print(
            f"   Re-analyzing {len(expanded)} Twitter items with reply context...\n"
        )
        ai_client = self._create_ai_client("twitter_reanalysis")
        failure_score = (
            None
            if self.config.quality_policy and self.config.quality_policy.enabled
            else 0.0
        )
        analyzer = ContentAnalyzer(ai_client, failure_score=failure_score)
        await analyzer.analyze_batch(expanded)

    async def _enrich_important_items(self, items: List[ContentItem]) -> None:
        """Enrich items with background knowledge (2nd AI pass).

        For each item that passed the score threshold, call AI to generate
        background knowledge based on the item's actual content.

        Args:
            items: Important items to enrich (modified in-place)
        """
        if not items:
            return

        self.console.print("📚 Enriching with background knowledge...")
        ai_client = self._create_ai_client("enrichment")
        enricher = ContentEnricher(ai_client)
        await enricher.enrich_batch(items)
        self.console.print(f"   Enriched {len(items)} items\n")

    async def _analyze_content(self, items: List[ContentItem]) -> List[ContentItem]:
        """Analyze content items with AI.

        Args:
            items: Items to analyze

        Returns:
            List[ContentItem]: Analyzed items
        """
        self.console.print("🤖 Analyzing content with AI...")

        ai_client = self._create_ai_client("analysis")
        failure_score = (
            None
            if self.config.quality_policy and self.config.quality_policy.enabled
            else 0.0
        )
        analyzer = ContentAnalyzer(ai_client, failure_score=failure_score)

        return await analyzer.analyze_batch(items)

    def _create_ai_client(self, stage: str):
        """Create the configured client and attach metadata-only V2 auditing."""
        client = create_ai_client(self.config.ai)
        if self._model_audit is None:
            return client
        return self._model_audit.wrap(client, stage=stage)

    async def _generate_summary(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
    ) -> str:
        """Generate daily summary.

        Args:
            items: Important items to include (already enriched with background/related)
            date: Date string
            total_fetched: Total items fetched
            language: Output language ("en" or "zh")

        Returns:
            str: Markdown summary
        """
        self.console.print("📝 Generating daily summary...")

        summarizer = DailySummarizer()

        return await summarizer.generate_summary(items, date, total_fetched, language=language)
