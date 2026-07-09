# Stage 3 — AS-IS review (the first human gate)

> New to this system? Read [`README.md`](README.md) first.
> Spec: [`../README.md`](../README.md) — flows contract, colors, gates.

## What this stage is

Engine steps 3–4 plus the gate that everything downstream depends on: adapt
the standard flows to the client's reality, build the interactive AS-IS
review, walk it through with the client, and approve it — consultant **and**
client — as a faithful picture. **No diagnosis before approval**:
recommendations built on a wrong AS-IS are worthless.

## Entry criteria

- A department's discovery is complete: pains, content blocks, coverage all
  checker-clean ([`02-discovery.md`](02-discovery.md)).

## What you produce

| Deliverable | Where | Done when |
|---|---|---|
| Adapted flow (step 3, optional) | `departments/NN-<dept>/flows/NN-<dept>.process.json` | matches the client's real process; 10–20 nodes (split bigger ones into a `subprocess` + `goto`) |
| AS-IS review HTML (step 4) | `asis/output/ASIS-<slug>.html` | builds clean; every documented step clickable, color-coded by severity |
| Approval (the gate) | content-file header table per department | `Status: approved`, set by you, after the client walkthrough |

## How to work

1. **Adapt the flows.** The standard flows in [`../flows/`](../flows/) are
   the default. Copy into `departments/NN-<dept>/flows/` and adapt to the
   client (extra channels, missing approval steps, …) — the same `domain`
   number overrides the standard at build time. `/analyze-department` does
   this as part of its run.
2. **Build.**
   ```bash
   python3 07-roadmap-engine/tools/build_asis.py 03-clients/<slug>
   python3 07-roadmap-engine/tools/check_engagement.py 03-clients/<slug>
   ```
   (`--dry-run` validates without writing; `--strict` fails on warnings.)
   Steps documented with no severity issues show blue, `minor` amber, `major`
   orange-red, `critical` red; steps in the flow but not documented show grey
   dashed — grey is a to-do, not a style.
3. **Run the review workshop — consultant + client.** Walk the HTML through
   with the people who do the work. Per process: is this how it actually
   runs? Are the volumes and times right? Is anything missing or overstated?
   Corrections go back into discovery steps 1–3 (pains, content, flows) —
   never into the built HTML — then rebuild and re-review what changed.
4. **Approve.** When consultant and client agree it is a faithful picture,
   set `Status: approved` in each department's content-file header table and
   move the csv row to `asis-review` done / stage `diagnosis`.

## The gate and its directives

Gated artifacts carry a **`## Gate` block**: a status, a **named approver**,
a **date**, and a checklist of **directives** — your concrete instructions
from the review ("merge the two intake channels", "re-check the volume on
SAL.030 with the planner"). Every directive must be resolved and checked off
before the status may go to approved; the checker treats an approval with
open directives as an error. Directives are how you steer the agent between
review rounds without doing the rework yourself.

## What you must judge yourself

- **The approval itself.** Only you set `Status: approved`, and only after
  the client walkthrough — agents and skills stop at `consultant-review` by
  design.
- **Faithfulness over completeness.** Approving means you'd defend every
  block in front of the people who do the work.

## Definition of done

- Every in-scope department `Status: approved` with a dated `## Gate` block,
  named approver, and all directives checked.
- `build_asis.py` and `check_engagement.py` clean; no grey-dashed steps left
  unexplained.
- Csv row moved to `diagnosis` with `next_action` set.

## Common pitfalls

- **Diagnosing before approval.** The gate exists because a wrong AS-IS
  poisons every score, formula, and verdict downstream — the tools refuse,
  don't route around them.
- **Consultant-only approval.** The client's people must recognise
  themselves in it; an AS-IS the client never walked through is a draft.
- **Fixing the HTML instead of the sources.** The build output is generated;
  corrections live in `pains.md`, `content/`, and `flows/`, then rebuild.
- **Approving with open directives.** A checked-off list is the evidence the
  review actually happened; the checker enforces it.
- **Flow sprawl.** Past ~20 nodes a diagram stops being readable in a
  workshop — split into subprocesses.

**Next stage:** [4 — Diagnosis](04-diagnosis.md), only once every in-scope
department is approved.
