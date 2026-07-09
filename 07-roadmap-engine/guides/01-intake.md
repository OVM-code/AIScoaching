# Stage 1 — Intake

> New to this system? Read [`README.md`](README.md) first — it explains the
> pipeline and every term used below. Spec: [`../README.md`](../README.md).

## What this stage is

Everything before the first department workshop: create the client's
workspace, record what we already know, and decide the engagement's scope in
the catalog's vocabulary. A well-run intake means discovery starts producing
on day one — and the config you write here (language, departments, day rate)
drives every deliverable and € figure downstream.

## Entry criteria

- A client (or serious prospect) with a name, a sector, and an intent to get
  an AI integration roadmap.

## What you produce

| Deliverable | Where | Done when |
|---|---|---|
| Client workspace | `03-clients/<slug>/` | copied from `03-clients/_template/`, slug is stable (it keys everything) |
| Engagement config | `03-clients/<slug>/engagement-config.json` | client, slug, language, sector, departments (catalog numbers), day rate all set |
| Intake notes | `03-clients/<slug>/intake/intake.md` | every field filled or explicitly marked unknown |
| Client context | `03-clients/<slug>/client-context.md` | single source of truth on the company, current systems, constraints |
| Pipeline row | `03-clients/engagements.csv` | one row, stage `intake`, `next_action` set |

## How to work

1. **Create the workspace.** Copy `03-clients/_template/` to
   `03-clients/<slug>/`. The template contains every folder later stages need
   — leave the ones you don't use yet alone.
2. **Fill the config interactively.** `/run-engagement <client name>` does
   this with you: it asks for language, sector, departments in scope, and day
   rate, then writes `engagement-config.json` and adds the
   `engagements.csv` row. It stops and asks when scope or language is unknown
   — it never defaults them.
3. **Scope departments against the catalog.** Pick catalog department
   *numbers* from [`../catalog/departments.json`](../catalog/departments.json)
   — the scope list in the config is what discovery, the AS-IS build, and the
   gates all iterate over. Per-process relevance is decided later, in each
   department's `coverage.md`.
4. **Capture the fact base.** Fill `intake/intake.md` and
   `client-context.md` from whatever exists (call notes, website, proposal).
   Facts you record here feed the workshop briefings; gaps here become
   numbered questions there.
5. **Verify.**
   ```bash
   python3 07-roadmap-engine/tools/check_engagement.py 03-clients/<slug>
   ```
   Zero errors and warnings is the definition of done — here and after every
   authoring step in every later stage.

## What you must judge yourself

- **Scope.** Which departments are in — and, as important, which are out and
  why. Agents ask; they never assume scope.
- **Language and day rate.** Deliverable language (`nl`/`en`) and the day
  rate for cost estimates are commercial decisions, not defaults.

## Definition of done

- Config complete, csv row at stage `intake` with a concrete `next_action`.
- Intake and client-context filled, unknowns explicit.
- `check_engagement.py` clean.

## Common pitfalls

- **Defaulting language or scope to move faster.** The whole engagement
  inherits it; the tools refuse to guess for a reason.
- **An unstable slug.** The folder name is the key in `engagements.csv` and
  every command — renaming it later breaks the paper trail.
- **Skipping the csv row.** Agents and humans both read `engagements.csv` as
  pipeline status; work not on the board doesn't exist.
- **Treating intake as paperwork.** A vague fact base produces vague
  briefings, which burn workshop time on company basics instead of pains.

**Next stage:** [2 — Discovery](02-discovery.md), the moment the first
workshop is planned.
