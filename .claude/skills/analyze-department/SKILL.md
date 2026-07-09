---
name: analyze-department
description: Take one client department through Roadmap Engine steps 0a–4 — briefing, pain extraction, AS-IS documentation, flow adaptation, and the AS-IS build — stopping at the consultant+client review gate. Use when a department has new discovery material or a workshop coming up, rather than driving the pipeline stages by hand.
---

# /analyze-department

Runs the `process-analyst` agent through the per-department AS-IS stages in
one pass. It is a chain because each stage's output gates the next (no pains
without cited inputs, no AS-IS blocks without pains, no build with checker
errors) — and it exists to stop, hard, at the one point that matters: the
human review of the built AS-IS.

## Input

`$ARGUMENTS`: a client slug (folder under `03-clients/`) and a department
(catalog number or id), e.g. `_demo-installtech 2` or `acme-hvac sales`.
Optionally "briefing" to run only the pre-workshop step 0a.

## Steps

1. **Resolve scope.** Read `03-clients/<slug>/engagement-config.json` and
   `03-clients/engagements.csv`. Stop conditions: no such engagement, or the
   department is not in the configured scope — ask, don't assume scope.
2. **Briefing (step 0a).** If the request is pre-workshop or `inputs/` is
   empty, invoke `process-analyst` to produce the briefing pack, then stop —
   there is nothing to extract yet.
3. **Extraction & documentation (steps 1–3).** Invoke `process-analyst` on
   the department's inputs. Stop conditions, in all cases reporting exactly
   what is needed rather than guessing:
   - **Missing or thin inputs** (no transcripts, unreadable files, a process
     in scope with zero coverage in the material) → stop and ask the
     consultant for the material or an explicit out-of-scope decision.
   - **Contradictions between meetings** → stop and present both versions
     with citations; the consultant decides which holds.
4. **Build & check (step 4).** `build_asis.py` then `check_engagement.py`.
   Stop condition: **checker errors or warnings that can't be mechanically
   fixed** from the existing material — report them; do not paper over a
   contract violation to get a green build.
5. **Stop at the review gate.** Report the built HTML path, open questions,
   and per-process status. The consultant walks the AS-IS through with the
   client; corrections re-enter at step 3.

## Rules

- **Never mark `Status: approved`** in any content file — only the human
  consultant does that, after the client walkthrough. This skill's output is
  always at most `consultant-review`.
- Never invent facts to fill a gap; a stop-and-ask is the correct output for
  thin material.
- `check_engagement.py` runs after every authoring step, not just at the
  end; zero errors and warnings is the definition of done.
- Deliverable content in the client's configured language.
