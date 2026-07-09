---
name: build-roadmap-proposal
description: Run Roadmap Engine steps 5–6 for a client whose AS-IS is fully approved — diagnosis (maturity, opportunities, verdicts, assumptions), proposal build with browser verification, and workshop prep — stopping at the client workshop gate. Use to produce the roadmap proposal end-to-end rather than invoking the diagnostician and builder separately.
---

# /build-roadmap-proposal

Chains `opportunity-diagnostician` → `proposal-builder` because the proposal
is only worth building on a diagnosis that survived its own gates: the chain
refuses to start on an unapproved AS-IS, and stops entirely if the diagnosis
honestly finds little worth proposing. It ends at the client workshop —
nothing after the build is this skill's call.

## Input

`$ARGUMENTS`: a client slug (folder under `03-clients/`). Optionally
"record" plus the workshop results / confirmation-export location, to run
only the post-workshop recording step.

## Steps

1. **Gate-check approvals.** Read every in-scope department's content-file
   header in `03-clients/<slug>/departments/*/content/`. Stop condition:
   **any department not `Status: approved`, or approved with an open `- [ ]`
   directive in its `## Gate` section → refuse**, listing the unapproved
   departments and what's pending (consultant review, client walkthrough,
   unresolved directives). No partial diagnosis around the gap.
2. **Diagnosis (step 5).** Invoke `opportunity-diagnostician`. Stop
   conditions:
   - **No viable opportunities** — the register is all discards or
     near-discards → stop and say so plainly. A well-reasoned "few real
     opportunities here" is a valid engagement outcome, not a failure;
     do not inflate scores to make a proposal happen.
   - **Checker errors** that trace to AS-IS gaps → stop and route back to
     `/analyze-department` for that department.
3. **Proposal (step 6, pre-workshop).** Invoke `proposal-builder`: `keep.md`,
   `build_proposal.py`, the Playwright/Chromium verification (sliders,
   filters, scatter-click, select-&-confirm export, theme), workshop pack.
   Stop condition: **a failed build or a broken interaction** — fix and
   re-verify before anything reaches a workshop agenda.
4. **Stop for the client workshop.** Report the proposal path, verification
   results, workshop pack, and the sponsor decisions to put on the table
   (capacity-dividend allocations). The client rescoring and the
   confirmation export happen in the workshop, run by the consultant.
5. **Record (post-workshop, separate invocation).** With the workshop
   results in hand, invoke `proposal-builder` to write
   `proposal/decision-log.md`, update OPP statuses, and set the
   `engagements.csv` stage to `confirmed`.

## Rules

- Never bypass the approval gate — a diagnosis on an unapproved AS-IS is
  worthless by definition (see `07-roadmap-engine/README.md`, gates).
- Skepticism is the default verdict posture; discards are recorded, never
  deleted, and the discard list is presented, not hidden.
- Never mark anything `confirmed` without the client's confirmation export
  or recorded workshop decision; never send the proposal to the client —
  handover is consultant-mediated.
- `check_engagement.py` after every authoring step; zero errors and warnings
  is the definition of done.
