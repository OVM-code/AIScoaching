# Stage 5 — Proposal and confirmation (the second human gate)

> New to this system? Read [`README.md`](README.md) first.
> Spec: [`../README.md`](../README.md) — proposal build, cost model, gates.

## What this stage is

Engine step 6: compile the diagnosis into the interactive roadmap proposal,
verify it actually works in a browser, run the F3 workshop where the
**client** challenges scores and adjusts assumptions, and record their
confirmation. The client operates the page — sliders, quadrant, wave ROI,
select & confirm — because a roadmap the client rescored is a roadmap the
client owns.

## Entry criteria

- Diagnosis complete and checker-clean ([`04-diagnosis.md`](04-diagnosis.md));
  all departments still `Status: approved`.

## What you produce

| Deliverable | Where | Done when |
|---|---|---|
| Keep list | `proposal/keep.md` | what works today and stays untouched: evidence per item, strengths, explicit non-goals |
| Proposal HTML | `proposal/output/ROADMAP-<slug>.html` | builds clean; sliders, filters, scatter, select-&-confirm verified in a real browser |
| Workshop pack | with the proposal | agenda, discard list, sponsor decisions to table |
| Decision log | `proposal/decision-log.md` | workshop outcomes: per OPP confirmed/deferred/discarded, slider changes, who decided |
| Confirmation | client's exported JSON + updated OPP statuses | at least one OPP `Status: confirmed`; csv stage `confirmed` |

## How to work

`/build-roadmap-proposal <slug>` drives the `proposal-builder` agent through
steps 1–3 and stops at the workshop; `/build-roadmap-proposal <slug> record`
runs step 5 afterwards.

1. **Fill `keep.md`.** The page renders it — clients adopt change faster
   when they hear what stays.
2. **Build.**
   ```bash
   python3 07-roadmap-engine/tools/build_proposal.py 03-clients/<slug>
   python3 07-roadmap-engine/tools/check_engagement.py 03-clients/<slug>
   ```
   (`--dry-run` to validate; `--baselines <path>` to override the effort
   seeds.) The build refuses on unapproved departments or a missing
   register/assumptions; formulas compile to static JS — a bad token is a
   build error, not a runtime surprise. Costs come from
   [`../baselines/effort-baselines.json`](../baselines/effort-baselines.json):
   `days(allocatie, effort) × day_rate`, year-1 adds 12 × tooling, payback in
   months.
3. **Verify in a real browser.** Sliders recompute the € figures, filters
   filter, scatter points open their OPP, select & confirm exports JSON,
   both themes render. A broken interaction never reaches a workshop agenda.
4. **Run the F3 workshop.** You present; the **client rescores**: challenge
   Value/Feasibility scores line by line, adjust sliders to their numbers,
   walk the discard list, select initiatives, put the sponsor decisions
   (capacity-dividend allocations) on the table, export the confirmation.
5. **Record.** Write `proposal/decision-log.md`, update each OPP `Status`
   (`confirmed | deferred | discarded`), set the csv row to `confirmed`, and
   re-run the checker — stage `confirmed` requires the decision log plus at
   least one confirmed OPP.

Like the AS-IS gate, confirmation carries a **`## Gate` block**: status, a
named approver, a date, and a checklist of directives that must all be
checked before approval — post-workshop corrections ("re-verify OPP-4's
feasibility with IT before wave 1") are directives, not loose notes.

## What you must judge yourself

- **The gate is the client's.** Only the client's workshop confirmation
  (export or recorded decision) moves anything to `confirmed` — never mark
  it yourself, and never send the proposal to the client directly; handover
  is consultant-mediated.
- **Score ownership.** If the client didn't change a single score or slider,
  they haven't engaged — provoke the challenge rather than defend the draft.

## Definition of done

- Verified HTML, held workshop, decision log written, OPP statuses updated,
  gate block approved with all directives checked, csv `confirmed`,
  `check_engagement.py` clean.

## Common pitfalls

- **Skipping the discard list in the workshop.** Presenting only winners
  hides the rigor that justifies them — the discards are your credibility.
- **Owning the scores yourself.** A consultant-scored roadmap gets politely
  shelved; the workshop exists to transfer ownership.
- **Confirming without the export.** "They seemed enthusiastic" is not a
  confirmation; the JSON or a recorded decision is.
- **Skipping browser verification.** A slider that doesn't recompute in
  front of the sponsor costs more trust than a week's delay.
- **An empty `keep.md`.** A consultant who only sees problems hasn't looked
  properly.

**Next stage:** [6 — Delivery & aftercare](06-delivery-aftercare.md) for the
confirmed wave-1 initiatives.
