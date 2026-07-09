---
name: run-engagement
description: Orchestrate a full Roadmap Engine engagement from intake to confirmed roadmap — workspace setup, per-department AS-IS loops, diagnosis and proposal, and confirmation recording, honoring every human gate. Use to drive or resume a whole engagement rather than running individual stages.
---

# /run-engagement

The orchestrator over the whole pipeline (`07-roadmap-engine/README.md`):
intake → per-department `/analyze-department` loops → `/build-roadmap-proposal`
→ confirmation recording. It is a chain of chains because every stage gates
the next, and its job is as much to **stop at the right moments** as to move
work forward — the two human gates (AS-IS approval, client workshop
confirmation) are the product's integrity, not friction.

## Input

`$ARGUMENTS`: a client slug, or for a new engagement the client's name plus
whatever intake facts are known. With no arguments, ask which engagement to
resume (list `03-clients/engagements.csv`).

## Steps

1. **Locate or create.** Look up the slug in `03-clients/engagements.csv`.
   New engagement: copy `03-clients/_template/` to `03-clients/<slug>/`,
   fill `engagement-config.json` interactively with the consultant (language,
   sector, departments in scope, day rate), add the csv row at stage
   `intake`. Stop condition: scope or language unknown — ask, don't default.
2. **Resume from the recorded stage.** The csv row is the single source of
   truth; never infer a later stage from files on disk.
3. **Discovery loop (stage `discovery` → `asis-review`).** For each
   in-scope department, run `/analyze-department` (briefing before its
   workshop; extraction and build once material lands). Each department run
   ends at its own review stop. Update the csv row's `next_action` as
   departments progress.
4. **Wait out the AS-IS gate.** Only when the consultant reports that every
   in-scope department is `Status: approved` (set by the human, never by an
   agent) does the engagement move to `diagnosis`.
5. **Diagnosis & proposal.** Run `/build-roadmap-proposal`, inheriting all
   its stop conditions (refuse on unapproved departments, stop on a no-viable-
   opportunities outcome, stop on build/verification failures). It ends
   stopped at the client workshop.
6. **Record confirmation.** After the consultant runs the workshop, take the
   confirmation export and decisions, run the post-workshop recording step
   (`/build-roadmap-proposal <slug> record`), and verify the csv row reads
   `confirmed` with a clean `check_engagement.py`. Delivery (pilot charters,
   phase 4 playbooks) is a separate engagement stage beyond this skill.

## Rules

- **Never skip a stop condition to save time.** Not one. A gate that is slow
  is doing its job; a gate that is skipped invalidates everything downstream.
- **Never send anything to the client directly** — no deliverable, link,
  mail, or export. Every client touchpoint goes through the consultant.
- Never set `Status: approved` on AS-IS content and never set stage
  `confirmed` without the client's confirmation — the two human gates belong
  to humans.
- Update `03-clients/engagements.csv` on every stage change, and run
  `python3 07-roadmap-engine/tools/check_engagement.py 03-clients/<slug>`
  after every authoring step — zero errors and warnings is the definition of
  done.
- Deliverables in the client's configured language; method calls cite the
  governing framework by path (`01-frameworks/F1`–`F6`).
