"""Core data models for Horizon."""

from datetime import datetime, timezone
from enum import Enum
from typing import Annotated, Literal, Optional, List, Dict, Any, Union
import hashlib
import re

from pydantic import BaseModel, ConfigDict, HttpUrl, Field, field_validator, model_validator


_SOURCE_ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{0,127}$")
_CREDENTIAL_QUERY_RE = re.compile(
    r"(?i)(^|[?&\s])"
    r"(api[_-]?key|key|access[_-]?token|token|sig(?:nature)?|auth|code|secret|password)"
    r"=([^&#\s]*)"
)
_PROHIBITED_AUDIT_FIELD_KEYS = {
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


def _validate_source_id(value: str) -> str:
    if not isinstance(value, str) or not _SOURCE_ID_RE.fullmatch(value):
        raise ValueError(
            "source_id must match ^[a-z0-9][a-z0-9._-]{0,127}$"
        )
    return value


def stable_source_id(prefix: str, material: str) -> str:
    """Synthesize the same non-secret source ID used by runtime scrapers."""
    safe_prefix = re.sub(r"[^a-z0-9._-]+", "-", prefix.lower()).strip("-._")
    digest = hashlib.sha256(material.encode("utf-8")).hexdigest()[:12]
    return f"{safe_prefix or 'source'}-{digest}"


def _sanitize_error_message(value: str | None) -> str | None:
    if value is None:
        return None
    # Error text is an audit field, never a traceback or a transport body.
    value = re.sub(r"[\r\n\t]+", " ", str(value)).strip()
    value = _CREDENTIAL_QUERY_RE.sub(
        lambda match: f"{match.group(1)}{match.group(2)}=[REDACTED]",
        value,
    )
    value = re.sub(
        r"(?i)\bauthorization\s*:\s*[^,;]+",
        "Authorization: [REDACTED]",
        value,
    )
    value = re.sub(r"(?i)\bbearer\s+\S+", "Bearer [REDACTED]", value)
    value = re.sub(
        r"(?is)-----BEGIN [^-]*PRIVATE KEY-----.*?-----END [^-]*PRIVATE KEY-----",
        "[REDACTED PRIVATE KEY]",
        value,
    )
    return value[:240]


class SourceType(str, Enum):
    """Supported information source types."""

    GITHUB = "github"
    HACKERNEWS = "hackernews"
    RSS = "rss"
    REDDIT = "reddit"
    TELEGRAM = "telegram"
    TWITTER = "twitter"
    OPENBB = "openbb"
    OSSINSIGHT = "ossinsight"
    GDELT = "gdelt"
    GOOGLE_NEWS = "google_news"


class SourceLevel(str, Enum):
    """Distance between a discovery channel and the original event."""

    L1 = "L1"
    L2 = "L2"
    L3 = "L3"


class ProfileStatus(str, Enum):
    """Whether a source profile came from the registry or legacy input."""

    KNOWN = "known"
    CUSTOM = "custom"
    MISSING = "missing"


class VerificationStatus(str, Enum):
    """Strength of the evidence resolved for a content item."""

    DIRECT = "direct"
    RESOLVED = "resolved"
    CORROBORATED = "corroborated"
    UNVERIFIED = "unverified"
    NOT_APPLICABLE = "not_applicable"


class SourceRunStatus(str, Enum):
    """Outcome for one configured source invocation."""

    SUCCESS = "success"
    EMPTY = "empty"
    PARTIAL = "partial"
    FAILED = "failed"
    SKIPPED = "skipped"


class SourceErrorCode(str, Enum):
    HTTP_403 = "HTTP_403"
    HTTP_429 = "HTTP_429"
    AUTH = "AUTH"
    CONFIG = "CONFIG"
    TIMEOUT = "TIMEOUT"
    NETWORK = "NETWORK"
    PARSE = "PARSE"
    POLICY = "POLICY"
    UNKNOWN = "UNKNOWN"


class ContentProvenance(BaseModel):
    """Additive provenance metadata for a :class:`ContentItem`."""

    schema_version: Literal["1"] = "1"
    discovery_source_id: str
    discovery_url: HttpUrl | None = None
    discovery_level: SourceLevel | None = None
    profile_status: ProfileStatus = ProfileStatus.KNOWN
    original_url: HttpUrl | None = None
    original_domain: str | None = None
    original_level: SourceLevel | None = None
    verification_status: VerificationStatus = VerificationStatus.UNVERIFIED
    evidence_urls: List[HttpUrl] = Field(default_factory=list, max_length=5)
    resolved_at: datetime | None = None

    _validate_discovery_source_id = field_validator("discovery_source_id")(
        _validate_source_id
    )

    @field_validator("original_domain")
    @classmethod
    def _validate_original_domain(cls, value: str | None) -> str | None:
        if value is None:
            return None
        normalized = value.strip().lower().rstrip(".")
        if (
            len(normalized) > 253
            or not normalized
            or any(
                not label
                or len(label) > 63
                or not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", label)
                for label in normalized.split(".")
            )
        ):
            raise ValueError("original_domain must be a normalized DNS name")
        return normalized

    @model_validator(mode="after")
    def _validate_provenance_consistency(self) -> "ContentProvenance":
        urls = [self.discovery_url, self.original_url, *self.evidence_urls]
        if any(
            value is not None
            and (value.scheme != "https" or value.username or value.password)
            for value in urls
        ):
            raise ValueError("provenance URLs must be HTTPS without user-info")
        if self.verification_status is VerificationStatus.DIRECT:
            if self.discovery_level is not SourceLevel.L1:
                raise ValueError("direct evidence requires an L1 discovery source")
        if self.verification_status in {
            VerificationStatus.RESOLVED,
            VerificationStatus.CORROBORATED,
        }:
            if self.original_url is None or self.original_level is None:
                raise ValueError(
                    "resolved/corroborated evidence requires an original URL and level"
                )
        return self

    @field_validator("evidence_urls")
    @classmethod
    def _unique_evidence_urls(cls, values: List[HttpUrl]) -> List[HttpUrl]:
        # Preserve input order while ensuring the bounded list is unique.
        result: List[HttpUrl] = []
        seen: set[str] = set()
        for value in values:
            key = str(value)
            if key not in seen:
                seen.add(key)
                result.append(value)
        return result


class SourceRunResult(BaseModel):
    """Sanitized, structured outcome for one configured sub-source."""

    model_config = ConfigDict(extra="forbid")

    schema_version: Literal["1"] = "1"
    source_id: str
    source_type: SourceType
    status: SourceRunStatus
    item_count: int = Field(default=0, ge=0)
    started_at: datetime
    finished_at: datetime
    latency_ms: int = Field(default=0, ge=0)
    attempts: int = Field(default=1, ge=1)
    fallback_used: str | None = Field(default=None, max_length=64)
    error_code: SourceErrorCode | None = None
    error_message: str | None = None

    _validate_source_id_field = field_validator("source_id")(_validate_source_id)
    _sanitize_error = field_validator("error_message", mode="before")(
        _sanitize_error_message
    )

    @model_validator(mode="after")
    def _validate_run_window(self) -> "SourceRunResult":
        if self.finished_at < self.started_at:
            raise ValueError("finished_at cannot precede started_at")
        return self


class ModelCallRecord(BaseModel):
    """Allowlisted model-call metadata; prompts and responses have no fields."""

    model_config = ConfigDict(extra="forbid")

    schema_version: Literal["1"] = "1"
    call_id: str = Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")
    provider: str = Field(min_length=1, max_length=64)
    model: str = Field(min_length=1, max_length=128)
    stage: str = Field(min_length=1, max_length=64)
    item_id: str | None = Field(default=None, max_length=500)
    status: Literal["ok", "failed", "blocked"]
    error_code: str | None = Field(default=None, max_length=64)
    attempts: int = Field(default=1, ge=1)
    latency_ms: int = Field(ge=0)
    input_tokens: int | None = Field(default=None, ge=0)
    output_tokens: int | None = Field(default=None, ge=0)
    total_tokens: int | None = Field(default=None, ge=0)
    started_at: datetime
    finished_at: datetime

    @model_validator(mode="after")
    def _validate_call_window(self) -> "ModelCallRecord":
        if self.finished_at < self.started_at:
            raise ValueError("finished_at cannot precede started_at")
        if self.input_tokens is not None and self.output_tokens is not None:
            calculated = self.input_tokens + self.output_tokens
            if self.total_tokens is not None and self.total_tokens != calculated:
                raise ValueError("total_tokens must equal input_tokens + output_tokens")
        return self


class AuditSourceCounts(BaseModel):
    """Strict source-count shape for a safe run manifest."""

    model_config = ConfigDict(extra="forbid")

    success: int = Field(default=0, ge=0)
    empty: int = Field(default=0, ge=0)
    partial: int = Field(default=0, ge=0)
    failed: int = Field(default=0, ge=0)
    skipped: int = Field(default=0, ge=0)


class AuditTokenUsage(BaseModel):
    """Aggregate token metadata; null means the provider did not expose it."""

    model_config = ConfigDict(extra="forbid")

    input: int | None = Field(default=None, ge=0)
    output: int | None = Field(default=None, ge=0)
    total: int | None = Field(default=None, ge=0)

    @model_validator(mode="after")
    def _validate_total(self) -> "AuditTokenUsage":
        if self.input is not None and self.output is not None and self.total is not None:
            if self.total != self.input + self.output:
                raise ValueError("total must equal input + output")
        return self


class AuditManifest(BaseModel):
    """Strict, metadata-only manifest accepted by the safe exporter."""

    model_config = ConfigDict(extra="forbid")

    schema_version: Literal["1"] = "1"
    run_id: str = Field(
        min_length=1,
        max_length=128,
        pattern=r"^[A-Za-z0-9][A-Za-z0-9._-]*$",
    )
    status: Literal["complete", "partial", "empty", "failed"]
    generated_at: datetime | None = None
    healthy_source_ratio: float = Field(default=0.0, ge=0.0, le=1.0)
    source_counts: AuditSourceCounts = Field(default_factory=AuditSourceCounts)
    pipeline_counts: Dict[str, int] = Field(default_factory=dict)
    failed_source_ids: List[str] = Field(default_factory=list, max_length=500)
    failed_stages: List[str] = Field(default_factory=list, max_length=64)
    token_usage: AuditTokenUsage | None = None

    @field_validator("pipeline_counts")
    @classmethod
    def _validate_pipeline_counts(cls, values: Dict[str, int]) -> Dict[str, int]:
        if len(values) > 64:
            raise ValueError("pipeline_counts is too large")
        for key, value in values.items():
            if not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", key) or value < 0:
                raise ValueError(
                    "pipeline_counts must contain safe non-negative counters"
                )
        return values

    @field_validator("failed_source_ids")
    @classmethod
    def _validate_failed_source_ids(cls, values: List[str]) -> List[str]:
        if len(values) != len(set(values)):
            raise ValueError("failed_source_ids must be unique")
        return [_validate_source_id(value) for value in values]

    @field_validator("failed_stages")
    @classmethod
    def _validate_failed_stages(cls, values: List[str]) -> List[str]:
        if len(values) != len(set(values)):
            raise ValueError("failed_stages must be unique")
        for value in values:
            if not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", value):
                raise ValueError("failed_stages contains an invalid stage")
        return values


class ContentItem(BaseModel):
    """Unified content item model from any source."""

    id: str  # Format: {source}:{subtype}:{native_id}
    source_type: SourceType
    title: str
    url: HttpUrl
    content: Optional[str] = None
    author: Optional[str] = None
    published_at: datetime
    fetched_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    metadata: Dict[str, Any] = Field(default_factory=dict)
    provenance: Optional[ContentProvenance] = None

    # AI analysis results
    ai_score: Optional[float] = None  # 0-10 importance score
    ai_reason: Optional[str] = None
    ai_summary: Optional[str] = None
    ai_tags: List[str] = Field(default_factory=list)


class DecisionStatus(str, Enum):
    SELECTED = "selected"
    REJECTED = "rejected"


class DecisionReasonCode(str, Enum):
    SOURCE_CANDIDATE_CAP = "SOURCE_CANDIDATE_CAP"
    DUPLICATE_CANONICAL_URL = "DUPLICATE_CANONICAL_URL"
    DUPLICATE_PRIOR_EVENT = "DUPLICATE_PRIOR_EVENT"
    BELOW_AI_THRESHOLD = "BELOW_AI_THRESHOLD"
    MODEL_ANALYSIS_FAILED = "MODEL_ANALYSIS_FAILED"
    TOPIC_DUPLICATE = "TOPIC_DUPLICATE"
    L3_ONLY_LIMIT = "L3_ONLY_LIMIT"
    DISCOVERY_CHANNEL_LIMIT = "DISCOVERY_CHANNEL_LIMIT"
    CATEGORY_LIMIT = "CATEGORY_LIMIT"
    GLOBAL_ITEM_LIMIT = "GLOBAL_ITEM_LIMIT"
    SELECTED_VERIFIED_ORIGINAL = "SELECTED_VERIFIED_ORIGINAL"
    SELECTED_ANALYSIS = "SELECTED_ANALYSIS"
    SELECTED_DISCOVERY = "SELECTED_DISCOVERY"
    PROFILE_MISSING = "PROFILE_MISSING"
    MATERIAL_UPDATE = "MATERIAL_UPDATE"


DecisionScalar = Union[str, int, float, bool, None]


def _validate_policy_values(
    values: Dict[str, Any]
) -> Dict[str, Any]:
    """Keep decision records to JSON scalars or lists of strings only."""

    if not isinstance(values, dict):
        raise ValueError("policy_values must be an object")
    if len(values) > 32:
        raise ValueError("policy_values is too large")
    clean: Dict[str, Any] = {}
    for key, value in values.items():
        if not isinstance(key, str) or len(key) > 64:
            raise ValueError("policy_values keys must be strings")
        normalized_key = re.sub(r"[^a-z0-9]", "", key.lower())
        if normalized_key in _PROHIBITED_AUDIT_FIELD_KEYS:
            raise ValueError("policy_values contains a prohibited audit field")
        if isinstance(value, list):
            if len(value) > 32 or not all(
                isinstance(entry, str) and len(entry) <= 1000 for entry in value
            ):
                raise ValueError("policy_values lists may only contain strings")
            if any(_CREDENTIAL_QUERY_RE.search(entry) for entry in value):
                raise ValueError("policy_values contains credential-like text")
            clean[key] = list(value)
        elif value is not None and not isinstance(value, (str, int, float, bool)):
            raise ValueError("policy_values values must be JSON scalars or string lists")
        elif isinstance(value, str):
            if len(value) > 1000:
                raise ValueError("policy_values strings are too long")
            if _CREDENTIAL_QUERY_RE.search(value):
                raise ValueError("policy_values contains credential-like text")
            clean[key] = value
        else:
            clean[key] = value
    return clean


class DecisionRecord(BaseModel):
    """One deterministic accept/reject decision for one item."""

    model_config = ConfigDict(extra="forbid")

    schema_version: Literal["1"] = "1"
    item_id: str = Field(max_length=500)
    status: DecisionStatus
    stage: str = Field(min_length=1, max_length=64)
    reason_code: DecisionReasonCode
    reason: str = Field(min_length=1, max_length=1000)
    title: str | None = Field(default=None, max_length=500)
    url: HttpUrl | None = None
    ai_score: float | None = Field(default=None, ge=0, le=10)
    source_id: str | None = None
    source_level: SourceLevel | None = None
    verification_status: VerificationStatus | None = None
    policy_values: Dict[str, Any] = Field(default_factory=dict)
    prior_event_id: str | None = Field(default=None, max_length=500)

    _validate_policy_values_field = field_validator("policy_values")(
        _validate_policy_values
    )

    @field_validator("source_id")
    @classmethod
    def _validate_optional_source_id(cls, value: str | None) -> str | None:
        return _validate_source_id(value) if value is not None else None

    @field_validator("url")
    @classmethod
    def _validate_public_url(cls, value: HttpUrl | None) -> HttpUrl | None:
        if value is None:
            return None
        if value.scheme != "https" or value.username or value.password:
            raise ValueError("public decision URLs must be HTTPS without user-info")
        return value


class CandidateLimitsPolicy(BaseModel):
    default_per_source: int = Field(default=5, gt=0)
    max_candidates_before_ai: int = Field(default=60, gt=0)
    overrides: Dict[str, int] = Field(default_factory=dict)

    @field_validator("overrides")
    @classmethod
    def _validate_overrides(cls, values: Dict[str, int]) -> Dict[str, int]:
        for source_id, cap in values.items():
            _validate_source_id(source_id)
            if cap <= 0:
                raise ValueError("candidate source caps must be positive")
        return values


class ProvenancePolicy(BaseModel):
    resolve_l3_original: bool = True
    max_evidence_urls: int = Field(default=5, ge=0, le=5)


class ChannelGroupLimit(BaseModel):
    source_ids: List[str] = Field(min_length=1)
    max_items: int = Field(gt=0)

    @field_validator("source_ids")
    @classmethod
    def _unique_source_ids(cls, values: List[str]) -> List[str]:
        if len(values) != len(set(values)):
            raise ValueError("channel group source_ids must be unique")
        for source_id in values:
            _validate_source_id(source_id)
        return values


class SelectionPolicy(BaseModel):
    max_items: int = Field(default=10, gt=0)
    target_verified_original_items: int = Field(default=5, ge=0)
    max_l3_only_items: int = Field(default=2, ge=0)
    default_max_items_per_discovery_source: int = Field(default=3, gt=0)
    channel_group_limits: Dict[str, ChannelGroupLimit] = Field(default_factory=dict)
    default_max_items_per_category: int = Field(default=4, gt=0)

    @model_validator(mode="after")
    def _validate_selection_bounds(self) -> "SelectionPolicy":
        if self.target_verified_original_items > self.max_items:
            raise ValueError("target_verified_original_items cannot exceed max_items")
        if self.max_l3_only_items > self.max_items:
            raise ValueError("max_l3_only_items cannot exceed max_items")
        for group_name, group in self.channel_group_limits.items():
            if not group_name or not isinstance(group_name, str):
                raise ValueError("channel group names must be non-empty strings")
            if group.max_items > self.max_items:
                raise ValueError("channel group max_items cannot exceed max_items")
        return self


class DeduplicationPolicy(BaseModel):
    history_days: int = Field(default=7, gt=0)
    allow_material_updates: bool = True


class RunHealthPolicy(BaseModel):
    required_source_ids: List[str] = Field(default_factory=list)
    min_healthy_source_ratio: float = Field(default=0.50, ge=0.0, le=1.0)

    @field_validator("required_source_ids")
    @classmethod
    def _validate_required_ids(cls, values: List[str]) -> List[str]:
        if len(values) != len(set(values)):
            raise ValueError("required_source_ids must be unique")
        for source_id in values:
            _validate_source_id(source_id)
        return values


class QualityPolicy(BaseModel):
    """Optional deterministic V2 policy; disabled retains legacy behavior."""

    enabled: bool = False
    candidate_limits: CandidateLimitsPolicy = Field(default_factory=CandidateLimitsPolicy)
    provenance: ProvenancePolicy = Field(default_factory=ProvenancePolicy)
    selection: SelectionPolicy = Field(default_factory=SelectionPolicy)
    deduplication: DeduplicationPolicy = Field(default_factory=DeduplicationPolicy)
    run_health: RunHealthPolicy = Field(default_factory=RunHealthPolicy)

    def validate_source_references(self, enabled_source_ids: set[str]) -> "QualityPolicy":
        """Validate policy IDs against a configured source set.

        Keeping this check explicit lets callers use a policy as a standalone
        value while ``Config`` enforces it when the enabled source registry is
        available.
        """

        references = set(self.candidate_limits.overrides)
        references.update(self.run_health.required_source_ids)
        for group in self.selection.channel_group_limits.values():
            references.update(group.source_ids)
        unknown = sorted(references - enabled_source_ids)
        if unknown:
            raise ValueError(
                "quality_policy references unknown or disabled source IDs: "
                + ", ".join(unknown)
            )
        return self


class AIProvider(str, Enum):
    """Supported AI providers."""

    ANTHROPIC = "anthropic"
    OPENAI = "openai"
    AZURE = "azure"
    ALI = "ali"
    GEMINI = "gemini"
    DOUBAO = "doubao"
    MINIMAX = "minimax"
    DEEPSEEK = "deepseek"
    OLLAMA = "ollama"


# Default models and API key env vars for each provider
AI_PROVIDER_DEFAULTS = {
    AIProvider.ANTHROPIC: {
        "model": "claude-3-5-sonnet-20241022",
        "api_key_env": "ANTHROPIC_API_KEY",
    },
    AIProvider.OPENAI: {
        "model": "gpt-4",
        "api_key_env": "OPENAI_API_KEY",
    },
    AIProvider.AZURE: {
        "model": "gpt-4",
        "api_key_env": "AZURE_OPENAI_API_KEY",
    },
    AIProvider.ALI: {
        "model": "qwen-plus",
        "api_key_env": "DASHSCOPE_API_KEY",
    },
    AIProvider.GEMINI: {
        "model": "gemini-1.5-flash",
        "api_key_env": "GOOGLE_API_KEY",
    },
    AIProvider.DOUBAO: {
        "model": "doubao-pro-32k",
        "api_key_env": "DOUBAO_API_KEY",
    },
    AIProvider.MINIMAX: {
        "model": "MiniMax-Text-01",
        "api_key_env": "MINIMAX_API_KEY",
    },
    AIProvider.DEEPSEEK: {
        "model": "deepseek-chat",
        "api_key_env": "DEEPSEEK_API_KEY",
    },
    AIProvider.OLLAMA: {
        "model": "llama3.1",
        "api_key_env": "",
    },
}


class AIConfig(BaseModel):
    """AI client configuration."""

    provider: AIProvider
    provider_chain: Optional[str] = None
    model: str
    base_url: Optional[str] = None
    api_key_env: str
    temperature: float = 0.3
    max_tokens: int = 4096
    throttle_sec: float = 0.0
    analysis_concurrency: int = 1
    enrichment_concurrency: int = 1
    languages: List[str] = Field(default_factory=lambda: ["en"])
    # Azure OpenAI specific; required when provider == AZURE
    azure_endpoint_env: Optional[str] = None
    api_version: Optional[str] = None


class GitHubSourceConfig(BaseModel):
    """GitHub source configuration."""

    type: str  # "user_events", "repo_releases", etc.
    username: Optional[str] = None
    owner: Optional[str] = None
    repo: Optional[str] = None
    enabled: bool = True
    category: Optional[str] = None
    source_id: Optional[str] = None
    source_level: Optional[SourceLevel] = None

    _validate_source_id_field = field_validator("source_id")(_validate_source_id)


class HackerNewsConfig(BaseModel):
    """Hacker News configuration."""

    enabled: bool = True
    fetch_top_stories: int = 30
    min_score: int = 100
    category: Optional[str] = None
    source_id: Optional[str] = None
    source_level: Optional[SourceLevel] = None

    _validate_source_id_field = field_validator("source_id")(_validate_source_id)


class ExtractorType(str, Enum):
    TRAFILATURA = "trafilatura"


class TrafilaturaExtractorConfig(BaseModel):
    type: Literal[ExtractorType.TRAFILATURA] = ExtractorType.TRAFILATURA
    favor_precision: bool = False
    favor_recall: bool = False


ExtractorConfig = Annotated[
    Union[TrafilaturaExtractorConfig],
    Field(discriminator="type"),
]


class RSSSourceConfig(BaseModel):
    """RSS feed source configuration."""

    name: str
    url: HttpUrl
    enabled: bool = True
    category: Optional[str] = None
    content_extractor: Optional[str] = None
    source_id: Optional[str] = None
    source_level: Optional[SourceLevel] = None

    _validate_source_id_field = field_validator("source_id")(_validate_source_id)


class RedditSubredditConfig(BaseModel):
    """Configuration for monitoring a specific subreddit."""

    subreddit: str
    enabled: bool = True
    sort: str = "hot"  # hot, new, top, rising
    time_filter: str = (
        "day"  # hour, day, week, month, year, all (only for top/controversial)
    )
    fetch_limit: int = 25
    min_score: int = 10
    category: Optional[str] = None
    source_id: Optional[str] = None
    source_level: Optional[SourceLevel] = None

    _validate_source_id_field = field_validator("source_id")(_validate_source_id)


class RedditUserConfig(BaseModel):
    """Configuration for monitoring a specific Reddit user."""

    username: str  # without u/ prefix
    enabled: bool = True
    sort: str = "new"
    fetch_limit: int = 10
    category: Optional[str] = None
    source_id: Optional[str] = None
    source_level: Optional[SourceLevel] = None

    _validate_source_id_field = field_validator("source_id")(_validate_source_id)


class RedditConfig(BaseModel):
    """Reddit source configuration."""

    enabled: bool = True
    subreddits: List[RedditSubredditConfig] = Field(default_factory=list)
    users: List[RedditUserConfig] = Field(default_factory=list)
    fetch_comments: int = 5  # top comments per post, 0 to disable


class TelegramChannelConfig(BaseModel):
    """Configuration for monitoring a specific Telegram channel."""

    channel: str  # channel username, e.g. "zaihuapd"
    enabled: bool = True
    fetch_limit: int = 20
    category: Optional[str] = None
    source_id: Optional[str] = None
    source_level: Optional[SourceLevel] = None

    _validate_source_id_field = field_validator("source_id")(_validate_source_id)


class TelegramConfig(BaseModel):
    """Telegram source configuration."""

    enabled: bool = True
    channels: List[TelegramChannelConfig] = Field(default_factory=list)


class TwitterConfig(BaseModel):
    """Twitter source configuration.

    Two modes are supported:
    - "apify": Use Apify scweet actor (requires APIFY_TOKEN, more reliable)
    - "playwright": Use Playwright + browser cookies (free, no token needed)
    """

    enabled: bool = True
    mode: str = "apify"  # "apify" or "playwright"
    users: List[str] = Field(default_factory=list)
    fetch_limit: int = 10
    category: Optional[str] = None
    fetch_reply_text: bool = False
    max_replies_per_tweet: int = 3
    max_tweets_to_expand: int = 10
    reply_min_likes: int = 0
    # Apify settings (used when mode == "apify")
    apify_token_env: str = "APIFY_TOKEN"
    actor_id: str = "altimis~scweet"
    # Playwright settings (used when mode == "playwright")
    cookie_dir: str = "data"
    cookie_file_pattern: str = "x_cookies_*.json"


class OpenBBWatchlist(BaseModel):
    """A named watchlist of tickers fetched from one OpenBB provider.

    Each watchlist produces one news.company() call per run, so group
    symbols by provider rather than creating one watchlist per symbol.
    """

    name: str
    symbols: List[str] = Field(default_factory=list)
    enabled: bool = True
    provider: str = "yfinance"
    fetch_limit: int = 20
    category: Optional[str] = None


class OpenBBConfig(BaseModel):
    """OpenBB Platform source configuration.

    Uses the installed `openbb` SDK to fetch news and filings for a set of
    tickers. The SDK is an optional dependency; if it is not installed the
    scraper will no-op with a console warning rather than crash the run.

    Provider credentials (FMP, Benzinga, Polygon, Intrinio, Tiingo, etc.)
    are resolved by openbb from environment variables / its own user
    settings file, so Horizon does not need to pass them explicitly.
    """

    enabled: bool = True
    watchlists: List[OpenBBWatchlist] = Field(default_factory=list)
    fetch_filings: bool = False
    filings_provider: str = "sec"


class OSSInsightConfig(BaseModel):
    """OSS Insight trending repos source configuration.

    Pulls top star-gain repositories from the OSS Insight public API and
    emits them as ContentItems. Optional `keywords` filter limits results
    to repos whose description, repo name, or collection names contain at
    least one of the listed substrings (case-insensitive). Leave
    `keywords` empty to ingest everything trending in the configured
    languages.
    """

    enabled: bool = False
    period: str = "past_24_hours"  # past_24_hours, past_28_days
    languages: List[str] = Field(
        default_factory=lambda: ["All", "Python", "TypeScript"]
    )
    keywords: List[str] = Field(default_factory=list)
    min_stars: int = 5
    max_items: int = 30
    category: Optional[str] = None


class GDELTConfig(BaseModel):
    """GDELT 2.0 DOC API source configuration.

    Queries the key-less GDELT DOC API
    (https://api.gdeltproject.org/api/v2/doc/doc) for recent news articles
    matching a search query and emits them as ContentItems. No API key is
    required. The DOC API caps results at 250 records per request, so keep
    `max_records` modest.
    """

    enabled: bool = False
    query: str = "artificial intelligence"
    mode: str = "ArtList"
    max_records: int = 75  # GDELT DOC API caps at 250; keep modest
    timespan: Optional[str] = None  # e.g. "24h"; overrides since-derived window
    language: Optional[str] = None  # sourcelang filter, e.g. "english"; None = no filter
    country: Optional[str] = None  # sourcecountry filter; None = no filter
    category: Optional[str] = None  # Horizon category label for downstream grouping


class GoogleNewsConfig(BaseModel):
    """Google News RSS search source configuration.

    Builds Google News RSS search URLs
    (https://news.google.com/rss/search) for a query and parses the
    resulting feed via feedparser. No API key is required.
    """

    enabled: bool = False
    query: str = "artificial intelligence"
    language: str = "en"  # hl
    country: str = "US"  # gl
    ceid: Optional[str] = None  # when None scraper derives it as "{country}:{language}"
    max_results: int = 100  # cap ~100
    category: Optional[str] = None


class SourcesConfig(BaseModel):
    """All sources configuration."""

    github: List[GitHubSourceConfig] = Field(default_factory=list)
    hackernews: HackerNewsConfig = Field(default_factory=HackerNewsConfig)
    rss: List[RSSSourceConfig] = Field(default_factory=list)
    reddit: RedditConfig = Field(default_factory=RedditConfig)
    telegram: TelegramConfig = Field(default_factory=TelegramConfig)
    twitter: Optional[TwitterConfig] = None
    openbb: Optional[OpenBBConfig] = None
    ossinsight: OSSInsightConfig = Field(default_factory=OSSInsightConfig)
    gdelt: Optional[GDELTConfig] = None
    google_news: Optional[GoogleNewsConfig] = None


class WebhookConfig(BaseModel):
    """Webhook notification configuration."""

    url_env: Optional[str] = (
        None  # Environment variable name containing the webhook URL
    )
    request_body: Optional[Union[str, dict, list]] = (
        None  # POST body: real JSON object or string with #{key} placeholders; if empty, will use GET
    )
    headers: Optional[str] = None  # Custom headers, "Key: Value" per line
    delivery: str = "summary"  # summary, or summary_and_items
    overview_position: str = "first"  # For summary_and_items: first, or last
    platform: str = "generic"  # generic, feishu, lark, dingtalk, slack, discord
    layout: str = "markdown"  # markdown, or collapsible
    fallback_layout: str = (
        "markdown"  # Layout to use when the requested layout is unsupported
    )
    languages: Optional[List[str]] = (
        None  # Optional language filter for webhook delivery; defaults to all AI languages
    )
    enabled: bool = False

    @field_validator("delivery")
    @classmethod
    def validate_delivery(cls, v: str) -> str:
        allowed = {"summary", "summary_and_items"}
        if v not in allowed:
            raise ValueError(f"webhook.delivery must be one of {allowed}, got '{v}'")
        return v

    @field_validator("platform")
    @classmethod
    def validate_platform(cls, v: str) -> str:
        allowed = {"generic", "feishu", "lark", "dingtalk", "slack", "discord"}
        if v not in allowed:
            raise ValueError(f"webhook.platform must be one of {allowed}, got '{v}'")
        return v

    @field_validator("layout")
    @classmethod
    def validate_layout(cls, v: str) -> str:
        allowed = {"markdown", "collapsible"}
        if v not in allowed:
            raise ValueError(f"webhook.layout must be one of {allowed}, got '{v}'")
        return v

    @field_validator("fallback_layout")
    @classmethod
    def validate_fallback_layout(cls, v: str) -> str:
        allowed = {"markdown", "collapsible"}
        if v not in allowed:
            raise ValueError(
                f"webhook.fallback_layout must be one of {allowed}, got '{v}'"
            )
        return v

    @field_validator("overview_position")
    @classmethod
    def validate_overview_position(cls, v: str) -> str:
        allowed = {"first", "last"}
        if v not in allowed:
            raise ValueError(
                f"webhook.overview_position must be one of {allowed}, got '{v}'"
            )
        return v


class EmailConfig(BaseModel):
    """Email configuration for updates/subscriptions."""

    imap_server: str
    imap_port: int = 993
    imap_enabled: bool = True
    smtp_server: str
    smtp_port: int = 465
    smtp_username: Optional[str] = None
    email_address: str
    password_env: str = "EMAIL_PASSWORD"
    sender_name: str = "Horizon Daily"
    subscribe_keyword: str = "SUBSCRIBE"
    unsubscribe_keyword: str = "UNSUBSCRIBE"
    enabled: bool = False


class CategoryGroupConfig(BaseModel):
    """A quota group containing one or more source categories."""

    name: Optional[str] = None
    limit: int = Field(gt=0)
    categories: List[str] = Field(min_length=1)


class FilteringConfig(BaseModel):
    """Content filtering configuration."""

    ai_score_threshold: float = 7.0
    time_window_hours: int = 24
    max_items: Optional[int] = Field(default=None, gt=0)
    category_groups: Dict[str, CategoryGroupConfig] = Field(default_factory=dict)
    default_group: str = "other"
    default_group_limit: Optional[int] = Field(default=None, gt=0)


class Config(BaseModel):
    """Main configuration model."""

    version: str = "1.0"
    ai: AIConfig
    sources: SourcesConfig
    filtering: FilteringConfig
    quality_policy: Optional[QualityPolicy] = None
    extractors: Dict[str, ExtractorConfig] = Field(default_factory=dict)
    email: Optional[EmailConfig] = None
    webhook: Optional[WebhookConfig] = None

    @model_validator(mode="after")
    def _validate_quality_source_references(self) -> "Config":
        if self.quality_policy is None or not self.quality_policy.enabled:
            return self
        source_ids: set[str] = set()
        for source in self.sources.github:
            if source.enabled:
                material = (
                    f"{source.type}:{source.username or ''}:"
                    f"{source.owner or ''}:{source.repo or ''}"
                )
                source_ids.add(
                    source.source_id or stable_source_id("github", material)
                )
        if self.sources.hackernews.enabled:
            source_ids.add(self.sources.hackernews.source_id or "hacker-news")
        for source in self.sources.rss:
            if source.enabled:
                source_ids.add(
                    source.source_id or stable_source_id("rss", str(source.url))
                )
        if self.sources.reddit.enabled:
            for source in (*self.sources.reddit.subreddits, *self.sources.reddit.users):
                if not source.enabled:
                    continue
                if isinstance(source, RedditSubredditConfig):
                    material = f"subreddit:{source.subreddit}"
                else:
                    material = f"user:{source.username}"
                source_ids.add(
                    source.source_id or stable_source_id("reddit", material)
                )
        if self.sources.telegram.enabled:
            for source in self.sources.telegram.channels:
                if source.enabled:
                    source_ids.add(
                        source.source_id
                        or stable_source_id("telegram", source.channel)
                    )
        self.quality_policy.validate_source_references(source_ids)
        return self
