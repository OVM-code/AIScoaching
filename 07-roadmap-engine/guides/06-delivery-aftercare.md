# Stage 6 — Delivery & aftercare

> New to this system? Read [`README.md`](README.md) first.
> Playbooks: [`../../02-phase-playbooks/phase-4-pilots.md`](../../02-phase-playbooks/phase-4-pilots.md)
> (pilots) and phases 5–6 (adoption, scale & governance).

## What this stage is

The confirmed roadmap becomes running pilots, and the engagement's actuals
flow back into the system. Delivery here means **wave 1 as pilots** — each
confirmed OPP's `Eerste stap` (first step) becomes a chartered 60–90 day
pilot with a baseline, kill criteria, and an explicit scale/iterate/kill
decision. Aftercare is the periodic pulse afterwards; close is when you
harvest what the engagement taught the system.

## Entry criteria

- Stage `confirmed`: decision log written, at least one OPP
  `Status: confirmed` ([`05-proposal.md`](05-proposal.md)).

## What you produce

| Deliverable | Where | Done when |
|---|---|---|
| Pilot charter per wave-1 OPP | client workspace, per phase-4 playbook (D19) | signed by the pilot owner **before** anything is built; kill criteria written in |
| Agent/automation spec | per phase-4 playbook (D20) | tier (T1 start) and promotion criteria stated; F6 deployer checklist done pre-go-live |
| Scorecards & G4 decisions | per phase-4 playbook (D22) | per pilot an explicit scale/iterate/kill call against pre-agreed criteria |
| Recalibrated baselines | [`../baselines/effort-baselines.json`](../baselines/effort-baselines.json) | actual days vs. estimate folded in at close; `version` bumped |
| Harvested lessons | [`../catalog/departments/`](../catalog/departments/) patterns · `06-knowledge/` | patterns the engagement confirmed or contradicted, written back |
| Stage updates | `03-clients/engagements.csv` | `delivery` → `aftercare` → `closed`, `next_action` current |

## How to work

1. **Charter each wave-1 pilot.** Start from the OPP block — the `Eerste
   stap`, allocation, enablers, and risk line are the charter's raw material.
   Follow the phase-4 playbook: baseline before build, real work at small
   scope, the affected team co-builds, kill criteria written before start.
2. **Deploy at the OPP's tier.** An `agent-T1` OPP ships as draft-only with
   a human deciding every item; promotion to T2/T3 is earned via measured
   accuracy per the spec — this is also the F6 human-oversight story.
3. **Run the pilot rhythm.** Weekly reviews against the charter's metrics;
   at the end, the G4 decision. A killed pilot with a clean retro is a
   success of the system, not a failure of yours.
4. **Aftercare pulse.** Deferred OPPs get revisited as waves 2–3 come due;
   pilot actuals recalibrate the assumption sliders the client set in the
   workshop (each assumption's `source` named its calibration path).
5. **Harvest at close.** Compare actual implementation days against
   `effort-baselines.json` and fold them in (bump `version`); write
   confirmed/contradicted patterns back to the catalog and `06-knowledge/`;
   set the csv row to `closed`. Then verify:
   ```bash
   python3 07-roadmap-engine/tools/check_engagement.py 03-clients/<slug>
   ```

## What you must judge yourself

- **The G4 call per pilot.** Scale, iterate, or kill against the pre-agreed
  criteria — honoring a kill criterion you wrote is the hardest and most
  valuable judgment in the stage.
- **What gets harvested.** One engagement's quirk versus a pattern worth
  writing into the catalog is a generalisation call only you can make.

## Definition of done

- Every wave-1 OPP chartered, run, and decided at G4 with a scorecard.
- Baselines recalibrated and versioned; lessons written back.
- Csv row current at every transition; `check_engagement.py` clean.

## Common pitfalls

- **Building before the baseline.** Without a week of measuring the old way,
  the scorecard proves nothing and the honest-ROI discount can't be applied.
- **Pilots without kill criteria.** A pilot that can't fail can't prove
  value either — write the criteria before the start, honor them at G4.
- **Taking self-reported savings at face value.** They inflate 2–3×; the
  proposal said so, so the scorecard must measure, not survey.
- **Closing without recalibrating.** The effort baselines are seeds that
  only become credible through actuals — skipping the harvest keeps every
  future payback estimate as uncalibrated as this one's.
- **Launching all waves at once.** Waves exist because F1 maturity limits
  absorption; wave 2 starts on wave-1 evidence, not on the calendar.

**Close of the loop:** the recalibrated baselines and harvested patterns are
what the *next* engagement's [intake](01-intake.md) starts smarter with.
