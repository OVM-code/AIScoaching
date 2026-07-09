# Engagement workspace template

Per-client workspace for the Roadmap Engine (`07-roadmap-engine/README.md` is
the binding spec). To start an engagement:

1. Copy this folder to `03-clients/<slug>/` (kebab-case slug).
2. Edit `engagement-config.json` — set `slug` to the folder name (they must
   match), real client/sector, `language` (`nl`|`en`), in-scope catalog
   department numbers, day rate. Delete the `_template_note`.
3. Add one row for the slug to `03-clients/engagements.csv` — the single source
   of truth for engagement stage; update it on **every** stage change. The CSV
   ships header-only; each engagement adds its own row (the worked example row
   is the `_demo-installtech` demo engagement). Stage enum: `intake | discovery
   | asis-review | diagnosis | proposal | confirmed | delivery | aftercare |
   closed`.
4. Per in-scope department, copy `departments/_example-dept/` to
   `departments/NN-<dept>/` (NN = catalog number, two digits).

After **every** authoring step, and before every delivery:

```bash
python3 07-roadmap-engine/tools/check_engagement.py 03-clients/<slug>
```

Zero errors and warnings is the definition of done. Never skip a gate to save
time.

## Stage-by-stage checklist

### intake
- [ ] `intake/intake.md` filled from the interview
      (`00-system/client-intake-questionnaire.md`)
- [ ] `client-context.md` generated via Prompt 0.1; sponsor validated the facts
      (`[VERIFY]` tags resolved or explicitly kept)
- [ ] Row in `engagements.csv`; config departments = agreed scope
- [ ] `python3 07-roadmap-engine/tools/check_engagement.py 03-clients/<slug>`

### discovery (per department)
- [ ] Step 0a — briefing pack in `departments/NN-<dept>/briefings/`
- [ ] Step 0 — meeting material in `inputs/` (`YYYY-MM-DD-<topic>-<type>.md`,
      quality header)
- [ ] Step 1 — pains extracted into `pains.md` (quote + source per PAIN)
- [ ] Step 2 — AS-IS blocks in `content/NN-<dept>.md`; out-of-scope reasons in
      `coverage.md`
- [ ] Step 3 — flow copied from `07-roadmap-engine/flows/` and adapted (optional)
- [ ] Checker clean after each step

### asis-review  [HUMAN GATE: consultant + client]
- [ ] `python3 07-roadmap-engine/tools/build_asis.py 03-clients/<slug>`
      → walk `asis/output/ASIS-<slug>.html` through with the client
- [ ] Corrections fed back into steps 1–3; rebuild until faithful
- [ ] Every department's content header set to `Status: approved`
- [ ] Checker clean — **no diagnosis before approval**

### diagnosis
- [ ] `analysis/maturity.md` — F1 scan, binding constraint named
- [ ] `analysis/opportunities.md` — OPP blocks scored (F3), allocated (F4),
      falsifiable verdicts; discards recorded, not deleted
- [ ] `analysis/assumptions.json` — 4–8 sliders every € figure derives from
- [ ] `proposal/keep.md` — what NOT to change
- [ ] Checker clean

### proposal  [CLIENT GATE: workshop]
- [ ] `python3 07-roadmap-engine/tools/build_proposal.py 03-clients/<slug>`
      → `proposal/output/ROADMAP-<slug>.html`
- [ ] F3 workshop: client challenges scores, adjusts sliders, selects, exports
      confirmation JSON

### confirmed
- [ ] `proposal/decision-log.md` filled (attendees, per-wave decisions, exported
      JSON pasted, next steps)
- [ ] OPP statuses updated: `confirmed` / `deferred` / `discarded`
      (≥ 1 confirmed — checker-enforced)
- [ ] `engagements.csv` stage → `confirmed`; checker clean

### delivery → aftercare
- [ ] Pilot charters for confirmed Wave 1 initiatives (phase 4 playbook)
- [ ] Effort actuals fed back to `07-roadmap-engine/baselines/` at close
- [ ] Re-run the F1 maturity scan to show progress; stage → `closed`

## Workspace map

```
engagement-config.json     client, slug, language, in-scope departments, day rate
client-context.md          master context (Prompt 0.1) — single source of truth
intake/intake.md           interview answers (questions live in 00-system/)
departments/NN-<dept>/     per-department discovery (see departments/README.md)
analysis/maturity.md       F1 scan + binding constraint
analysis/opportunities.md  OPP register (F3 × F4)
analysis/assumptions.json  slider model behind every € figure
proposal/decision-log.md   confirmation workshop record
proposal/keep.md           what NOT to change
```
