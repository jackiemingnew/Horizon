# Horizon UI Design Context

## Product intent

Horizon turns a mixed stream of technical sources into a small, inspectable daily brief. The documentation site should feel like an evidence desk: calm enough for reading, dense enough for source comparison, and explicit about where information came from.

The source configurator is a workbench inside the documentation site, not a marketing landing page. Its primary task is to let a technically comfortable reader discover sources, understand their provenance and evidence level, select a practical set, and export a valid partial `sources` configuration for Horizon.

## Reference decisions

- Primary reference: Airtable. Borrow its restrained editorial canvas, structured-data clarity, small-radius controls, and use of borders instead of decorative shadow.
- Secondary reference: Mintlify. Borrow its documentation-grade density, monospace configuration preview, compact badges, and clear loading/error/empty states.
- Secondary reference: Linear. Borrow its precise filter controls, scarce use of accent color, and hierarchy built from surface steps and hairline borders.
- Do not reproduce the references' brand colors, proprietary fonts, hero treatments, or marketing layouts. Horizon's existing sunrise palette and Cayman/Jekyll structure remain authoritative.

## Visual language

### Color tokens

Use the existing tokens from `docs/assets/css/horizon.css` as the source of truth:

- `--hz-bg`: page canvas
- `--hz-surface`: controls, selected summaries, and quiet panels
- `--hz-border`: dividers and card outlines
- `--hz-text`: primary copy
- `--hz-text-muted`: metadata and helper copy
- `--hz-link`: links and keyboard focus rings
- `--hz-code-bg`: configuration preview
- `--hz-accent`: primary action and selected state

The sunrise orange is scarce: selection markers, the primary export action, and one or two high-signal accents. Source levels must use a label plus color; color alone never communicates trust.

### Typography

- UI and prose: system sans stack led by PingFang SC on Chinese systems.
- Configuration and technical identifiers: `ui-monospace`, SFMono-Regular, Menlo, Consolas, monospace.
- Page title: 32-40px depending on viewport, weight 700-800.
- Section title: 20-24px, weight 700.
- Source title: 16px, weight 700.
- Body: 15-16px with at least 1.5 line-height.
- Metadata and badges: 12-13px; never smaller than 12px.

### Geometry and depth

- Base spacing unit: 4px. Prefer 8, 12, 16, 24, 32, and 48px.
- Inputs and buttons: 6px radius, minimum 44px touch target.
- Source rows/cards: 8px radius, 1px border, no default shadow.
- Large panels: 10px radius.
- Depth comes from surface and border contrast, not gradients or layered shadows.

## Layout

- Desktop: compact introduction, one horizontal filter bar, then a two-column workbench. The catalog is the flexible main column; the selected/configuration panel is 320-360px and sticky within the viewport.
- Source catalog: two columns at wide desktop, one column below 960px. Cards may differ in height according to content; do not force a decorative uniform grid.
- Tablet and mobile: all content stacks. The selected/configuration panel follows the catalog and is not sticky. Filters wrap without horizontal overflow.
- Maximum workbench width: 1280px. The page may widen beyond Cayman's default prose width only for this tool.

## Core components and states

### Research note

A compact evidence strip shows the size of the public Horizon Hub catalog, the number of curated sources in this page, the latest verification date, and a short warning that availability does not equal reliability.

### Filter bar

- Search input with visible label.
- Category and evidence-level selects.
- Result count announced through an `aria-live` region.
- Reset action appears only when filters are active.

### Source card

- Native checkbox is the selection control; the whole label area may be clickable.
- Show source name, one-line description, type, language, category, provenance, and evidence-level badge.
- A source link opens its canonical public page or feed in a new tab with an explicit accessible label.
- Selected state uses a stronger border and a small accent inset; it must remain legible in light and dark color schemes.
- If a source has a caveat, show it as text beneath metadata, not as a tooltip-only warning.

### Evidence levels

- L1 Direct: official project, company, maintainer, research publisher, or release channel. Direct does not mean automatically true.
- L2 Analysis: specialist reporting or analysis that interprets primary material.
- L3 Discovery: community, ranking, discussion, or broad aggregation used to discover leads.

These labels describe distance from the original event, not an absolute accuracy score.

### Configuration panel

- Selected count and a grouped source summary.
- Read-only JSON preview using monospace type.
- Copy and download actions; both export a partial object containing only `sources`, with helper text explaining that it must be merged into the user's existing config.
- Empty state explains what selection does. Copy/download are disabled until at least one source is selected.
- Copy success and load errors are announced via `aria-live`.

## Interaction and data constraints

- Pure HTML, CSS, and JavaScript; no new client framework or build step.
- Catalog data lives in a static JSON file and records its provenance and last verification date.
- Filtering and selection happen locally. The page sends no data and stores no credentials.
- Export must map catalog types to Horizon's actual schema: RSS list, GitHub `user_events`/`repo_releases`, Hacker News object, Reddit subreddits, and Telegram channels.
- Export is deterministic: the same selected IDs produce the same ordered JSON.
- Do not claim that a feed was content-quality reviewed merely because its endpoint returned successfully.

## Accessibility and responsive behavior

- Maintain WCAG 2.1 AA contrast for text and focus indicators.
- Preserve semantic heading order and native form controls.
- Every control has a visible label or an accessible name.
- Keyboard focus uses a 2px `--hz-link` outline with offset.
- Dynamic counts and copy/error messages use polite live regions.
- Test at 320, 768, 1024, and 1440px. No horizontal page scrolling at any target width.
- Respect `prefers-reduced-motion`; functionality must not depend on animation.

## Do / do not

Do:

- Keep provenance, evidence level, and caveats visible at selection time.
- Prefer compact rows, hairline borders, and real source names over decorative illustration.
- Keep the generated configuration inspectable before export.
- Preserve Horizon light/dark system color behavior.

Do not:

- Present L1/L2/L3 as a truth score.
- Preselect a large opaque bundle or silently mutate a repository config.
- Add a generic gradient hero, oversized padding, pill-shaped controls everywhere, or heavy card shadows.
- Fetch credentials, write secrets, or send selected source data to a server.
