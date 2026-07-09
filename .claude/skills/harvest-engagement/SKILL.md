---
name: harvest-engagement
description: Run the knowledge-flywheel harvest at an engagement milestone (roadmap confirmed, wave delivered, engagement closed). Drafts effort-baseline recalibrations, catalog evidence entries, stale-pattern challenges, and assumption-default calibrations — the human approves, nothing auto-merges. Use at any milestone, or when asked to "harvest", "capture evidence", or "recalibrate baselines".
---

<!-- model: sonnet — comparison and drafting mechanics against fixed conventions; no judgment call an approval gate doesn't already cover, per the agent toolkit (Holding 06-agent-toolkit/model-selection-guide.md) -->

# /harvest-engagement — make the engagement feed the engine

Usage: `/harvest-engagement 03-clients/<slug> [milestone]`. Everything below is
**DRAFTED for approval** — present each output as a diff/block the consultant
accepts or rejects. Never write to `07-roadmap-engine/` without an explicit
accept per block; a harvest that auto-merges is a bug, not a time-saver.

Only real engagements feed the flywheel: demo workspaces (slug starting with
`_`) may illustrate conventions but their entries are always marked `(demo)`
and never count as validation.

## Steps

1. **Effort-baseline recalibration.** Compare
   `07-roadmap-engine/baselines/effort-baselines.json` seeds against this
   engagement's actuals: implementation days per delivered OPP (ask the
   consultant for time-writing per initiative, or use pilot-charter /
   delivery-log dates as a proxy) versus `days(allocatie, effort) × day_rate`.
   Draft per-cell adjustments (`implementation_days[<allocatie>][<S|M|L>]`),
   **bump `version`**, and note the calibration source in `notes`. One
   engagement rarely justifies a big swing — propose conservative moves and
   say how many data points sit behind each cell.

2. **Evidence harvesting.** From the *approved* AS-IS content and the
   *confirmed* OPPs (per `analysis/opportunities.md` statuses and
   `proposal/decision-log.md` — never from `proposed`/`deferred` ones),
   determine which catalog processes, leak patterns, and opportunity patterns
   this engagement confirmed. Draft, per confirmed process in
   `07-roadmap-engine/catalog/departments.json`:
   - an appended `"evidence"` entry — format
     `"<client-slug> <artifact-path> <YYYY-MM>"` (artifact path relative to
     the client workspace, no spaces, optional `#OPP-x` anchor; suffix
     ` (demo)` only for demo workspaces);
   - `"last_validated": "YYYY-MM"` set to the harvest month.
   Where the engagement surfaced an opportunity pattern (or caveat) the
   catalog authoring pages lack, draft the addition to the matching
   `07-roadmap-engine/catalog/departments/NN-*.md` process block —
   generalised, client facts stripped, never the client's name in the prose.

3. **Stale sweep.** Run
   `python3 07-roadmap-engine/tools/catalog_report.py` and present the
   challenge list: catalog processes and opportunity patterns with no (or
   demo-only) evidence across all engagements to date, plus anything
   `[STALE]`. This is a challenge to the catalog, not a to-do — the
   consultant decides per item: keep (still plausible), rewrite, or drop.

4. **Assumption calibration.** Compare the slider values the client vouched
   for in `proposal/decision-log.md` (confirmed OPPs only) against the
   `default` values in `analysis/assumptions.json`. Where the workshop value
   diverges from the default, draft: (a) the pattern for future engagements
   (e.g. "SMEs systematically overestimate quotes/month by ~25%") destined
   for the relevant catalog page or `06-knowledge/`, and (b) a note on
   whether the engagement's own assumption `source` fields promised a
   calibration that never happened.

## Output & close

One summary block per step with the proposed edits ready to apply on approval.
After the consultant accepts/rejects each block and accepted edits are applied:

- run `python3 07-roadmap-engine/tools/catalog_report.py --strict` (must exit 0)
  and `python3 07-roadmap-engine/tools/check_engagement.py 03-clients/<slug>`;
- close by updating the engagement log: a dated "harvest run" line in the
  client's `client-context.md` (which milestone, which blocks accepted) and
  the `notes` column of `03-clients/engagements.csv`.

## Rules

- Drafts only — the human approves; rejected blocks are dropped without debate.
- Confirmed evidence only: an OPP that never reached `Status: confirmed` and
  content never `Status: approved` prove nothing.
- Skepticism cuts both ways: the stale sweep exists so unproven catalog
  patterns get challenged, not silently accumulated.
- Never client names in catalog prose; slugs in evidence entries are fine.
