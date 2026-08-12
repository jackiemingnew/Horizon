"""Pure, deterministic source-quality helpers.

The V2 policy is intentionally kept out of the network-facing scrapers.  This
module only receives validated models and returns new, integration-friendly
result objects.  It does not inspect content bodies or call external services.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from hashlib import sha256
import re
from typing import Any, Iterable, Iterator, Mapping, Sequence
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from .models import (
    Config,
    ContentItem,
    ContentProvenance,
    DecisionReasonCode,
    DecisionRecord,
    DecisionStatus,
    DeduplicationPolicy,
    ProfileStatus,
    QualityPolicy,
    SourceLevel,
    VerificationStatus,
)


_TRACKING_QUERY_KEYS = {
    "fbclid",
    "gclid",
    "dclid",
    "mc_cid",
    "mc_eid",
    "igshid",
    "ref_src",
    "spm",
    "yclid",
    "_ga",
    "_gl",
}
_CREDENTIAL_QUERY_KEY_RE = re.compile(
    r"^(?:api[_-]?key|key|access[_-]?token|token|sig(?:nature)?|auth|code|secret|password)$",
    re.IGNORECASE,
)


def canonicalize_url(url: Any) -> str:
    """Return a stable, secret-safe canonical URL.

    Host names and schemes are case-insensitive.  Default ports, fragments,
    common tracking parameters, and credential-like query parameters are
    removed.  All remaining query pairs are retained and sorted, including
    repeated keys and blank values.
    """

    raw = str(url).strip()
    if not raw:
        return ""
    parts = urlsplit(raw)
    scheme = parts.scheme.lower()
    try:
        hostname = (parts.hostname or "").lower()
        port = parts.port
    except ValueError:
        # Malformed ports cannot be made safer by guessing.  Keep the input
        # deterministic while still dropping fragments and query credentials.
        hostname = (parts.netloc.rsplit("@", 1)[-1]).lower()
        port = None
    if hostname.startswith("www."):
        hostname = hostname[4:]
    if ":" in hostname and not hostname.startswith("["):
        netloc_host = f"[{hostname}]"
    else:
        netloc_host = hostname
    if port is not None and not ((scheme == "http" and port == 80) or (scheme == "https" and port == 443)):
        netloc_host = f"{netloc_host}:{port}"

    path = parts.path or ""
    if path != "/":
        path = path.rstrip("/")
    query_pairs: list[tuple[str, str]] = []
    for key, value in parse_qsl(parts.query, keep_blank_values=True):
        lowered = key.lower()
        if lowered.startswith("utm_") or lowered in _TRACKING_QUERY_KEYS:
            continue
        if _CREDENTIAL_QUERY_KEY_RE.fullmatch(key):
            continue
        query_pairs.append((key, value))
    query_pairs.sort(key=lambda pair: (pair[0], pair[1]))
    query = urlencode(query_pairs, doseq=True)
    return urlunsplit((scheme, netloc_host, path, query, ""))


def source_id_for_item(item: ContentItem) -> str:
    """Resolve an item's discovery source without consulting a registry."""

    if item.provenance and item.provenance.discovery_source_id:
        return item.provenance.discovery_source_id
    metadata = item.metadata if isinstance(item.metadata, Mapping) else {}
    source_id = metadata.get("source_id")
    if isinstance(source_id, str) and source_id:
        return source_id
    source_type = getattr(item.source_type, "value", str(item.source_type))
    stable_material = "|".join(
        (source_type, str(item.id), canonicalize_url(item.url))
    )
    return "legacy-" + sha256(stable_material.encode("utf-8")).hexdigest()[:16]


def attach_provenance(
    item: ContentItem,
    source_id: str | None = None,
    source_level: SourceLevel | str | None = None,
    profile_status: ProfileStatus | str | None = None,
) -> ContentItem:
    """Return a copy with provenance attached, preserving existing metadata."""

    if item.provenance is not None:
        return item.model_copy(deep=True)
    explicit_source = source_id is not None
    resolved_source_id = source_id or source_id_for_item(item)
    level = SourceLevel(source_level) if source_level is not None else None
    if profile_status is None:
        status = ProfileStatus.KNOWN if explicit_source else ProfileStatus.MISSING
    else:
        status = ProfileStatus(profile_status)
    verification = (
        VerificationStatus.DIRECT
        if level is SourceLevel.L1
        else VerificationStatus.UNVERIFIED
    )
    provenance = ContentProvenance(
        discovery_source_id=resolved_source_id,
        discovery_url=item.url,
        discovery_level=level,
        profile_status=status,
        original_url=(item.url if level is SourceLevel.L1 else None),
        original_domain=(
            (urlsplit(str(item.url)).hostname or "").lower()
            if level is SourceLevel.L1
            else None
        ),
        original_level=(SourceLevel.L1 if level is SourceLevel.L1 else None),
        verification_status=verification,
    )
    return item.model_copy(update={"provenance": provenance}, deep=True)


def resolve_known_originals(
    items: list[ContentItem],
    config: Config,
    *,
    resolved_at: datetime | None = None,
) -> list[ContentItem]:
    """Resolve L3 links only against configured L1 hosts and repositories.

    This first-phase resolver performs no DNS lookup or HTTP request.  It can
    therefore strengthen a discovery link only when its HTTPS target already
    matches a locally configured direct publisher or exact GitHub repository.
    """

    policy = config.quality_policy
    if (
        policy is None
        or not policy.enabled
        or not policy.provenance.resolve_l3_original
    ):
        return items

    direct_hosts: set[str] = set()
    github_prefixes: set[str] = set()
    for source in config.sources.rss:
        if source.enabled and source.source_level is SourceLevel.L1:
            host = (urlsplit(str(source.url)).hostname or "").lower()
            if host:
                direct_hosts.add(host)
    for source in config.sources.github:
        if (
            source.enabled
            and source.source_level is SourceLevel.L1
            and source.owner
            and source.repo
        ):
            github_prefixes.add(f"/{source.owner}/{source.repo}".lower())

    resolved_values: list[ContentItem] = []
    timestamp = resolved_at or datetime.now(timezone.utc)
    for item in items:
        provenance = item.provenance
        if (
            provenance is None
            or provenance.discovery_level is not SourceLevel.L3
            or provenance.verification_status is not VerificationStatus.UNVERIFIED
        ):
            resolved_values.append(item)
            continue
        parts = urlsplit(str(item.url))
        host = (parts.hostname or "").lower()
        path = parts.path.rstrip("/").lower()
        matched = parts.scheme.lower() == "https" and host in direct_hosts
        if parts.scheme.lower() == "https" and host == "github.com":
            matched = matched or any(
                path == prefix or path.startswith(prefix + "/")
                for prefix in github_prefixes
            )
        if not matched:
            resolved_values.append(item)
            continue
        evidence = list(provenance.evidence_urls)
        if str(item.url) not in {str(value) for value in evidence}:
            evidence.append(item.url)
        evidence = evidence[: policy.provenance.max_evidence_urls]
        resolved_provenance = provenance.model_copy(
            update={
                "original_url": item.url,
                "original_domain": host,
                "original_level": SourceLevel.L1,
                "verification_status": VerificationStatus.RESOLVED,
                "evidence_urls": evidence,
                "resolved_at": timestamp,
            },
            deep=True,
        )
        resolved_values.append(
            item.model_copy(update={"provenance": resolved_provenance}, deep=True)
        )
    return resolved_values


def _as_policy(policy: QualityPolicy | Mapping[str, Any] | None) -> QualityPolicy:
    if policy is None:
        return QualityPolicy()
    if isinstance(policy, QualityPolicy):
        return policy
    return QualityPolicy.model_validate(policy)


def _datetime_value(value: datetime | None) -> float:
    if value is None:
        return float("-inf")
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    try:
        return value.timestamp()
    except (OverflowError, OSError, ValueError):
        return float("-inf")


def _engagement_value(item: ContentItem) -> float:
    metadata = item.metadata if isinstance(item.metadata, Mapping) else {}
    for key in ("engagement", "score", "points", "likes", "comments", "popularity"):
        value = metadata.get(key)
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return float(value)
    return 0.0


def _item_sort_key(item: ContentItem) -> tuple[float, float, str, str]:
    return (
        -_datetime_value(item.published_at),
        -_engagement_value(item),
        str(item.id),
        canonicalize_url(item.url),
    )


def _selection_sort_key(item: ContentItem) -> tuple[float, float, str, str]:
    score = item.ai_score
    normalized_score = (
        float(score)
        if isinstance(score, (int, float)) and not isinstance(score, bool)
        else float("-inf")
    )
    return (
        -normalized_score,
        -_datetime_value(item.published_at),
        str(item.id),
        canonicalize_url(item.url),
    )


def decision_for_item(
    item: ContentItem,
    status: DecisionStatus,
    reason_code: DecisionReasonCode,
    reason: str,
    policy_values: Mapping[str, Any] | None = None,
    *,
    prior_event_id: str | None = None,
    stage: str = "selection",
) -> DecisionRecord:
    # Never copy item metadata/content into a decision.  Values supplied here
    # are intentionally limited to scalars and string lists by the model.
    safe_values = dict(policy_values or {})
    provenance = item.provenance
    canonical_url = canonicalize_url(item.url)
    public_url = canonical_url if canonical_url.startswith("https://") else None
    return DecisionRecord(
        item_id=str(item.id),
        status=status,
        stage=stage,
        reason_code=reason_code,
        reason=reason,
        title=str(item.title),
        url=public_url,
        ai_score=item.ai_score,
        source_id=source_id_for_item(item),
        source_level=(provenance.discovery_level if provenance else None),
        verification_status=(provenance.verification_status if provenance else None),
        policy_values=safe_values,
        prior_event_id=prior_event_id,
    )


@dataclass
class SameRunDedupResult:
    items: list[ContentItem]
    decisions: list[DecisionRecord]


def _provenance_strength(item: ContentItem) -> int:
    provenance = item.provenance
    if provenance is None:
        return 0
    if (
        provenance.verification_status is VerificationStatus.DIRECT
        and provenance.discovery_level is SourceLevel.L1
    ):
        return 4
    if (
        provenance.verification_status
        in {
            VerificationStatus.RESOLVED,
            VerificationStatus.CORROBORATED,
        }
        and provenance.original_level is SourceLevel.L1
    ):
        return 3
    if provenance.discovery_level is SourceLevel.L2:
        return 2
    if provenance.discovery_level is SourceLevel.L3:
        return 1
    return 0


def deduplicate_same_run(items: list[ContentItem]) -> SameRunDedupResult:
    """Merge exact canonical-URL repeats and preserve a decision per duplicate.

    Primary selection is deterministic and provenance-aware: direct evidence
    wins over discovery copies, then richer content, freshness, and stable ID.
    """

    groups: dict[str, list[ContentItem]] = {}
    for item in items:
        canonical = canonicalize_url(item.url)
        key = canonical or f"item:{item.id}"
        groups.setdefault(key, []).append(item)

    kept: list[ContentItem] = []
    decisions: list[DecisionRecord] = []
    for key in sorted(groups):
        group = groups[key]
        ranked = sorted(
            group,
            key=lambda value: (
                -_provenance_strength(value),
                -len(value.content or ""),
                -_datetime_value(value.published_at),
                str(value.id),
            ),
        )
        primary = ranked[0].model_copy(deep=True)
        source_ids = sorted({source_id_for_item(value) for value in group})
        source_types = sorted({value.source_type.value for value in group})
        for duplicate in ranked[1:]:
            for metadata_key, metadata_value in duplicate.metadata.items():
                if metadata_key not in primary.metadata or not primary.metadata[metadata_key]:
                    primary.metadata[metadata_key] = metadata_value
            if duplicate.content and duplicate.content not in (primary.content or ""):
                label = source_id_for_item(duplicate)
                primary.content = (
                    (primary.content or "")
                    + f"\n\n--- From {label} ---\n"
                    + duplicate.content
                )
            decisions.append(
                decision_for_item(
                    duplicate,
                    DecisionStatus.REJECTED,
                    DecisionReasonCode.DUPLICATE_CANONICAL_URL,
                    "Merged into the stronger same-run canonical URL record.",
                    {
                        "canonical_url": key,
                        "kept_item_id": primary.id,
                        "source_id": source_id_for_item(duplicate),
                    },
                    stage="same_run_deduplication",
                )
            )
        primary.metadata["merged_source_ids"] = source_ids
        primary.metadata["merged_sources"] = source_types
        kept.append(primary)

    kept.sort(key=_item_sort_key)
    decisions.sort(key=lambda value: value.item_id)
    return SameRunDedupResult(kept, decisions)


@dataclass
class CandidateLimitResult:
    """Candidates retained for scoring, bounded overflow, and cap decisions."""

    items: list[ContentItem]
    overflow: dict[str, list[ContentItem]] = field(default_factory=dict)
    decisions: list[DecisionRecord] = field(default_factory=list)

    @property
    def candidates(self) -> list[ContentItem]:
        return self.items

    def __iter__(self) -> Iterator[Any]:
        yield self.items
        yield self.overflow
        yield self.decisions


def apply_candidate_limits(
    items: list[ContentItem],
    policy: QualityPolicy | Mapping[str, Any] | None,
) -> CandidateLimitResult:
    """Apply deterministic per-source and global pre-AI candidate caps."""

    quality_policy = _as_policy(policy)
    if not quality_policy.enabled:
        return CandidateLimitResult(items=items, overflow={}, decisions=[])

    grouped: dict[str, list[ContentItem]] = {}
    for value in items:
        grouped.setdefault(source_id_for_item(value), []).append(value)
    for source_id in grouped:
        grouped[source_id].sort(key=_item_sort_key)

    default_cap = quality_policy.candidate_limits.default_per_source
    overrides = quality_policy.candidate_limits.overrides
    trimmed: dict[str, list[ContentItem]] = {}
    overflow: dict[str, list[ContentItem]] = {}
    decisions: list[DecisionRecord] = []
    for source_id in sorted(grouped):
        cap = overrides.get(source_id, default_cap)
        trimmed[source_id] = grouped[source_id][:cap]
        overflow[source_id] = list(grouped[source_id][cap:])
        for excluded in grouped[source_id][cap:]:
            decisions.append(
                decision_for_item(
                    excluded,
                    DecisionStatus.REJECTED,
                    DecisionReasonCode.SOURCE_CANDIDATE_CAP,
                    "Excluded by the configured per-source candidate cap.",
                    {"source_id": source_id, "cap": cap, "scope": "source"},
                    stage="candidate_limiting",
                )
            )

    global_cap = quality_policy.candidate_limits.max_candidates_before_ai
    available = sum(len(values) for values in trimmed.values())
    if available <= global_cap:
        kept = [value for source in sorted(trimmed) for value in trimmed[source]]
        kept.sort(key=_item_sort_key)
        return CandidateLimitResult(kept, overflow, decisions)

    # Reserve one slot per non-empty source first.  Remaining slots are
    # allocated by weighted deficit round-robin; ties use source IDs.
    selected_by_source: dict[str, list[ContentItem]] = {source: [] for source in trimmed}
    sources = [source for source in sorted(trimmed) if trimmed[source]]
    remaining = global_cap
    for source in sources:
        if remaining <= 0:
            break
        selected_by_source[source].append(trimmed[source][0])
        remaining -= 1

    default_weight = max(1, default_cap)
    deficits = {source: 0.0 for source in sources}
    next_index = {source: len(selected_by_source[source]) for source in sources}
    while remaining > 0:
        eligible = [source for source in sources if next_index[source] < len(trimmed[source])]
        if not eligible:
            break
        for source in eligible:
            cap = overrides.get(source, default_cap)
            # Cap the ratio so an explicit override cannot monopolize the pool.
            deficits[source] += min(4.0, max(1.0, cap / default_weight))
        highest_deficit = max(deficits[source] for source in eligible)
        chosen = min(
            source for source in eligible if deficits[source] == highest_deficit
        )
        selected_by_source[chosen].append(trimmed[chosen][next_index[chosen]])
        next_index[chosen] += 1
        deficits[chosen] -= 1.0
        remaining -= 1

    kept: list[ContentItem] = []
    for source in sources:
        kept.extend(selected_by_source[source])
    kept_ids = {id(value) for value in kept}
    for source in sources:
        # Global-cap exclusions are retained in each source's overflow queue.
        extra = [value for value in trimmed[source] if id(value) not in kept_ids]
        if extra:
            overflow[source].extend(extra)
            for excluded in extra:
                decisions.append(
                    decision_for_item(
                        excluded,
                        DecisionStatus.REJECTED,
                        DecisionReasonCode.SOURCE_CANDIDATE_CAP,
                        "Excluded by the global pre-AI candidate cap.",
                        {"cap": global_cap, "scope": "global", "source_id": source},
                        stage="candidate_limiting",
                    )
                )
    kept.sort(key=_item_sort_key)
    return CandidateLimitResult(kept, overflow, decisions)


@dataclass
class SelectionResult:
    selected: list[ContentItem]
    decisions: list[DecisionRecord]

    @property
    def items(self) -> list[ContentItem]:
        return self.selected

    @property
    def rejected(self) -> list[DecisionRecord]:
        return [decision for decision in self.decisions if decision.status is DecisionStatus.REJECTED]

    def __iter__(self) -> Iterator[Any]:
        yield self.selected
        yield self.decisions


def _bucket(item: ContentItem) -> str:
    provenance = item.provenance
    if provenance is None:
        return "l3_only"
    verification = provenance.verification_status
    if verification in {
        VerificationStatus.DIRECT,
        VerificationStatus.RESOLVED,
        VerificationStatus.CORROBORATED,
    } and provenance.original_level is SourceLevel.L1:
        return "verified_original"
    if verification is VerificationStatus.DIRECT and provenance.discovery_level is SourceLevel.L1:
        return "verified_original"
    if provenance.original_level is SourceLevel.L2 or provenance.discovery_level is SourceLevel.L2:
        return "analysis"
    return "l3_only"


def _category_for_item(item: ContentItem) -> str:
    metadata = item.metadata if isinstance(item.metadata, Mapping) else {}
    category = metadata.get("category")
    return category if isinstance(category, str) and category else "other"


def _channel_groups_for_source(policy: QualityPolicy, source_id: str) -> list[tuple[str, int]]:
    return sorted(
        (
            (group_name, group.max_items)
            for group_name, group in policy.selection.channel_group_limits.items()
            if source_id in group.source_ids
        ),
        key=lambda value: value[0],
    )


def _selection_rejection(
    item: ContentItem,
    bucket: str,
    policy: QualityPolicy,
    selected: Sequence[ContentItem],
    source_counts: Mapping[str, int],
    group_counts: Mapping[str, int],
    category_counts: Mapping[str, int],
) -> tuple[DecisionReasonCode, str, dict[str, Any]] | None:
    source_id = source_id_for_item(item)
    if bucket == "l3_only" and sum(1 for value in selected if _bucket(value) == "l3_only") >= policy.selection.max_l3_only_items:
        return (
            DecisionReasonCode.L3_ONLY_LIMIT,
            "Excluded because the L3-only item ceiling is full.",
            {"max_l3_only_items": policy.selection.max_l3_only_items},
        )
    source_cap = policy.selection.default_max_items_per_discovery_source
    if source_counts.get(source_id, 0) >= source_cap:
        return (
            DecisionReasonCode.DISCOVERY_CHANNEL_LIMIT,
            "Excluded because the discovery-source ceiling is full.",
            {"source_id": source_id, "max_items": source_cap},
        )
    for group_name, group_cap in _channel_groups_for_source(policy, source_id):
        if group_counts.get(group_name, 0) >= group_cap:
            return (
                DecisionReasonCode.DISCOVERY_CHANNEL_LIMIT,
                "Excluded because the configured channel-group ceiling is full.",
                {"channel_group": group_name, "max_items": group_cap},
            )
    category = _category_for_item(item)
    if category_counts.get(category, 0) >= policy.selection.default_max_items_per_category:
        return (
            DecisionReasonCode.CATEGORY_LIMIT,
            "Excluded because the category ceiling is full.",
            {"category": category, "max_items": policy.selection.default_max_items_per_category},
        )
    if len(selected) >= policy.selection.max_items:
        return (
            DecisionReasonCode.GLOBAL_ITEM_LIMIT,
            "Excluded because the global digest item limit is full.",
            {"max_items": policy.selection.max_items},
        )
    return None


def select_digest(
    items: list[ContentItem],
    policy: QualityPolicy | Mapping[str, Any] | None,
) -> SelectionResult:
    """Select thresholded items with deterministic provenance and quota rules."""

    quality_policy = _as_policy(policy)
    if not quality_policy.enabled:
        selected = items
        decisions = [
            decision_for_item(
                value,
                DecisionStatus.SELECTED,
                DecisionReasonCode.SELECTED_DISCOVERY,
                "Selected by legacy behavior because the V2 policy is disabled.",
            )
            for value in items
        ]
        return SelectionResult(selected, decisions)

    indexed = list(enumerate(items))
    ranked = sorted(indexed, key=lambda pair: _selection_sort_key(pair[1]))
    verified = [pair for pair in ranked if _bucket(pair[1]) == "verified_original"]
    decisions: dict[int, DecisionRecord] = {}
    selected: list[ContentItem] = []
    selected_indexes: set[int] = set()
    source_counts: dict[str, int] = {}
    group_counts: dict[str, int] = {}
    category_counts: dict[str, int] = {}

    def consider(index: int, value: ContentItem) -> bool:
        bucket = _bucket(value)
        rejection = _selection_rejection(
            value, bucket, quality_policy, selected, source_counts, group_counts, category_counts
        )
        if rejection:
            reason_code, reason, values = rejection
            decisions[index] = decision_for_item(
                value, DecisionStatus.REJECTED, reason_code, reason, values
            )
            return False
        if value.ai_score is None:
            decisions[index] = decision_for_item(
                value,
                DecisionStatus.REJECTED,
                DecisionReasonCode.BELOW_AI_THRESHOLD,
                "Item did not have an above-threshold AI score.",
            )
            return False
        selected.append(value)
        selected_indexes.add(index)
        source_id = source_id_for_item(value)
        source_counts[source_id] = source_counts.get(source_id, 0) + 1
        for group_name, _ in _channel_groups_for_source(quality_policy, source_id):
            group_counts[group_name] = group_counts.get(group_name, 0) + 1
        category = _category_for_item(value)
        category_counts[category] = category_counts.get(category, 0) + 1
        selected_reason = {
            "verified_original": DecisionReasonCode.SELECTED_VERIFIED_ORIGINAL,
            "analysis": DecisionReasonCode.SELECTED_ANALYSIS,
            "l3_only": DecisionReasonCode.SELECTED_DISCOVERY,
        }[bucket]
        prior_event_id = value.metadata.get("prior_event_id")
        if prior_event_id:
            selected_reason = DecisionReasonCode.MATERIAL_UPDATE
        decisions[index] = decision_for_item(
            value,
            DecisionStatus.SELECTED,
            selected_reason,
            "Selected within the deterministic V2 selection policy.",
            {
                "bucket": bucket,
                "source_id": source_id,
                **(
                    {"prior_event_id": str(prior_event_id)}
                    if prior_event_id
                    else {}
                ),
            },
            prior_event_id=(str(prior_event_id) if prior_event_id else None),
        )
        return True

    target = quality_policy.selection.target_verified_original_items
    verified_selected = 0
    for index, value in verified:
        if verified_selected >= target or len(selected) >= quality_policy.selection.max_items:
            break
        if consider(index, value):
            verified_selected += 1

    # Fill remaining slots by the global rank, retaining the verified target
    # choices above and assigning exactly one decision to every input item.
    for index, value in ranked:
        if index in selected_indexes or index in decisions:
            continue
        if len(selected) >= quality_policy.selection.max_items:
            decisions[index] = decision_for_item(
                value,
                DecisionStatus.REJECTED,
                DecisionReasonCode.GLOBAL_ITEM_LIMIT,
                "Excluded because the global digest item limit is full.",
                {"max_items": quality_policy.selection.max_items},
            )
            continue
        consider(index, value)

    # Defensive completion for unusual input sequences (e.g. NaN sort values).
    for index, value in indexed:
        if index not in decisions:
            decisions[index] = decision_for_item(
                value,
                DecisionStatus.REJECTED,
                DecisionReasonCode.GLOBAL_ITEM_LIMIT,
                "Excluded by the deterministic selection policy.",
            )
    ordered_decisions = [decisions[index] for index, _ in indexed]
    return SelectionResult(selected, ordered_decisions)


@dataclass
class HistoryFilterResult:
    items: list[ContentItem]
    decisions: list[DecisionRecord]
    updates: list[ContentItem] = field(default_factory=list)

    @property
    def retained(self) -> list[ContentItem]:
        return self.items

    def __iter__(self) -> Iterator[Any]:
        yield self.items
        yield self.decisions


def _record_value(record: Any, key: str, default: Any = None) -> Any:
    if isinstance(record, Mapping):
        return record.get(key, default)
    return getattr(record, key, default)


def _record_timestamp(record: Any) -> datetime | None:
    value = _record_value(record, "published_at") or _record_value(record, "created_at")
    if isinstance(value, str):
        try:
            return datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return None
    return value if isinstance(value, datetime) else None


def _native_ids_for_item(item: ContentItem) -> set[str]:
    metadata = item.metadata if isinstance(item.metadata, Mapping) else {}
    values = {str(item.id)}
    for key in ("native_id", "source_native_id", "stable_native_id"):
        value = metadata.get(key)
        if value is not None and str(value):
            values.add(str(value))
    values.add(f"{source_id_for_item(item)}:{metadata.get('native_id', item.id)}")
    return values


def filter_exact_history(
    items: list[ContentItem],
    history: Iterable[Any] | Mapping[str, Any],
    policy: QualityPolicy | Mapping[str, Any] | None = None,
    *,
    now: datetime | None = None,
    history_days: int | None = None,
    allow_material_updates: bool | None = None,
) -> HistoryFilterResult:
    """Remove exact URL/native-ID repeats from the bounded history window."""

    quality_policy = _as_policy(policy)
    dedup: DeduplicationPolicy = quality_policy.deduplication
    days = history_days if history_days is not None else dedup.history_days
    allow_updates = (
        allow_material_updates if allow_material_updates is not None else dedup.allow_material_updates
    )
    current_time = now or datetime.now(timezone.utc)
    if current_time.tzinfo is None:
        current_time = current_time.replace(tzinfo=timezone.utc)
    records = list(history.values()) if isinstance(history, Mapping) else list(history)
    indexed_urls: dict[str, Any] = {}
    indexed_natives: dict[str, Any] = {}
    for record in records:
        timestamp = _record_timestamp(record)
        if timestamp is not None:
            if timestamp.tzinfo is None:
                timestamp = timestamp.replace(tzinfo=timezone.utc)
            age = (current_time - timestamp).total_seconds()
            if age < 0 or age > days * 86400:
                continue
        record_url = _record_value(record, "canonical_url") or _record_value(record, "url")
        if record_url:
            indexed_urls[canonicalize_url(record_url)] = record
        native_values = {
            _record_value(record, key)
            for key in ("native_id", "source_native_id", "stable_native_id", "item_id", "id")
        }
        for value in native_values:
            if value is not None and str(value):
                indexed_natives[str(value)] = record

    kept: list[ContentItem] = []
    updates: list[ContentItem] = []
    decisions: list[DecisionRecord] = []
    for value in items:
        candidate_urls = [canonicalize_url(value.url)]
        if value.provenance and value.provenance.original_url:
            candidate_urls.append(canonicalize_url(value.provenance.original_url))
        match = next(
            (indexed_urls[url] for url in candidate_urls if url in indexed_urls),
            None,
        )
        if match is None:
            for native_id in _native_ids_for_item(value):
                if native_id in indexed_natives:
                    match = indexed_natives[native_id]
                    break
        if match is None:
            kept.append(value)
            continue
        prior_event_id = (
            _record_value(match, "prior_event_id")
            or _record_value(match, "event_id")
            or _record_value(match, "item_id")
            or _record_value(match, "id")
        )
        metadata = value.metadata if isinstance(value.metadata, Mapping) else {}
        marker = metadata.get("material_update_marker")
        prior_marker = _record_value(match, "material_update_marker")
        is_material_update = bool(
            allow_updates and marker is not None and str(marker) and str(marker) != str(prior_marker or "")
        )
        if is_material_update:
            updated_metadata = dict(metadata)
            updated_metadata["prior_event_id"] = str(prior_event_id) if prior_event_id is not None else ""
            updated = value.model_copy(update={"metadata": updated_metadata}, deep=True)
            kept.append(updated)
            updates.append(updated)
        else:
            decisions.append(
                decision_for_item(
                    value,
                    DecisionStatus.REJECTED,
                    DecisionReasonCode.DUPLICATE_PRIOR_EVENT,
                    "Excluded because its canonical URL or stable native ID is in history.",
                    {"prior_event_id": str(prior_event_id) if prior_event_id is not None else ""},
                    prior_event_id=str(prior_event_id) if prior_event_id is not None else None,
                    stage="history_deduplication",
                )
            )
    return HistoryFilterResult(kept, decisions, updates)


__all__ = [
    "CandidateLimitResult",
    "HistoryFilterResult",
    "SameRunDedupResult",
    "SelectionResult",
    "apply_candidate_limits",
    "attach_provenance",
    "canonicalize_url",
    "decision_for_item",
    "deduplicate_same_run",
    "filter_exact_history",
    "resolve_known_originals",
    "select_digest",
    "source_id_for_item",
]
