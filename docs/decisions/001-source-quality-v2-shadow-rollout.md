# ADR-001: Roll out source-quality V2 through an isolated shadow workflow

## Status

Accepted for local and manual shadow evaluation; not accepted for production Pages promotion

## Date

2026-08-12

## Context

The existing daily workflow publishes a useful digest, but source failure is often indistinguishable from an empty window, discovery channels can dominate selection, and the AI relevance score does not represent source credibility. Full local stages may contain scraped public text and therefore are not suitable for indiscriminate Actions artifact or Pages publication.

## Decision

Keep legacy behavior as the default and add Source Quality V2 behind `quality_policy.enabled`. Evaluate it with the 29-source local configuration and a separate `workflow_dispatch` shadow workflow. The shadow job has read-only repository permissions, never writes `docs/` or `gh-pages`, and uploads only the strict safe-export allowlist for 14 days.

L1/L2/L3 describes provenance distance, not truth. The initial resolver performs no outbound resolution requests; it only recognizes links whose HTTPS target matches a configured L1 host or exact GitHub repository. Unknown targets stay unverified.

## Alternatives considered

### Replace the daily workflow immediately

Rejected because no seven-day qualification set exists and an implementation defect could interrupt the already-running digest or publish unsafe diagnostic data.

### Upload complete `data/runs` artifacts

Rejected because stage files can include full scraped bodies and are outside the public audit contract.

### Treat every external community link as resolved evidence

Rejected because an outbound link alone does not prove first-party provenance. Only locally known L1 targets are upgraded in the first slice.

### Build a network resolver immediately

Deferred because correct DNS, redirect, address-range, size, content-type, timeout, and access-control enforcement is a separate security boundary. The no-network resolver provides measurable value without creating that attack surface.

## Consequences

- Existing configs and the scheduled Pages workflow remain behaviorally unchanged.
- Manual shadow runs require the existing `DEEPSEEK_API_KEY` secret and use `github.token` only for read-only GitHub API access.
- Failures remain observable through source, decision, model-call, and manifest metadata without publishing prompts, responses, headers, credentials, summaries, or full scraped content.
- The safe artifact is retained for 14 days by Actions. Local `--save-stages` runs prune recorded run directories older than 14 days before creating the next run.
- Production scheduling or Pages publication requires qualification evidence and separate explicit authorization.

## Review status

The high-risk AGY implementation review is partial: Gemini completed, while the required Sonnet review failed without retry or model substitution. Repository mode did not include newly created untracked V2 files. Those files have local Sol and test coverage, but must be tracked before an external repository-mode review can cover the complete implementation.
