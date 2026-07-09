# Stage 2 — Discovery (per department)

> New to this system? Read [`README.md`](README.md) first.
> Spec for every block format and enum: [`../README.md`](../README.md).

## What this stage is

Engine steps 0a–2, run **per in-scope department**: prepare each workshop
with a briefing, collect the raw material, distil it into cited pain points,
and document how every in-scope process runs today. Discovery ends when a
department's AS-IS content is complete enough to build and review — it is the
evidence base; everything after it is interpretation.

## Entry criteria

- Stage `intake` done: config, scope, and fact base in place.
- A department workshop planned, or discovery material already in hand.

## What you produce

| Deliverable | Where | Done when |
|---|---|---|
| Briefing pack (step 0a) | `departments/NN-<dept>/briefings/` | one per workshop, generated *before* it happens |
| Meeting inputs (step 0) | `departments/NN-<dept>/inputs/YYYY-MM-DD-<topic>-<type>.md` | text only, one file per meeting, source quality noted in the header |
| Pain register (step 1) | `departments/NN-<dept>/pains.md` | `## PAIN-x` blocks: literal quote, citation (`<file> §<n>`), type, severity, volume |
| AS-IS content (step 2) | `departments/NN-<dept>/content/NN-<dept>.md` | one `## <CODE>` block per in-scope process: working, who, systems, volume & time, linked pains, severity, automability |
| Coverage matrix (step 2) | `departments/NN-<dept>/coverage.md` | every catalog process of the department in or out, one-line reason for each out |

## How to work

The heavy lifting is one skill — run it per department:

```
/analyze-department <slug> <department>          # e.g. /analyze-department acme-hvac sales
/analyze-department <slug> <department> briefing # pre-workshop: step 0a only
```

It drives the `process-analyst` agent through briefing → pains → AS-IS →
coverage → build, checking after every step, and **stops** on missing/thin
inputs and on contradictions between meetings.

1. **Brief (0a).** Before each workshop, generate the briefing pack: known
   facts from intake, hypothesis scope per catalog process, numbered
   questions, applicable patterns from
   [`../catalog/departments/`](../catalog/departments/) and `06-knowledge/`.
   Walk in with questions, walk out with answers.
2. **Collect (0).** Drop meeting material in `inputs/`, one file per meeting.
   Transcribe recordings first — text only.
3. **Extract pains (1).** Each `## PAIN-x` keeps a literal client quote and a
   source citation. PAIN ids are numbered **once across the whole
   engagement**, not per department — OPP blocks reference them globally.
4. **Document AS-IS (2).** For every in-scope process a `## <CODE>` block,
   including the first-look `Automability` (F4:
   [`../../01-frameworks/F4-operating-model-org-design.md`](../../01-frameworks/F4-operating-model-org-design.md)).
   Out-of-scope processes get a one-line reason in `coverage.md`.
5. **Check.** After every authoring step:
   ```bash
   python3 07-roadmap-engine/tools/check_engagement.py 03-clients/<slug>
   ```

## What you must judge yourself

- **Contradictions.** When two meetings disagree, the agent presents both
  versions with citations and stops — *you* decide which holds.
- **Thin material.** A process in scope with zero coverage in the material is
  your call: get more material, or an explicit out-of-scope decision in
  `coverage.md`. The agent never invents facts to fill a gap.

## Definition of done

- Every in-scope process documented or explicitly out with a reason.
- Every pain quoted and cited; no dangling PAIN/process references.
- `check_engagement.py` clean; csv row at `discovery` with `next_action`
  tracking which departments remain.

## Common pitfalls

- **Pains without a literal quote and citation.** An uncited pain is an
  opinion; the diagnosis later builds € figures on these blocks.
- **Guessing through a contradiction.** Silently picking one meeting's
  version bakes an error into the approved AS-IS — always ask.
- **Documenting only the painful processes.** The AS-IS is a faithful
  picture, not a complaint list; `severity: none` blocks and the coverage
  matrix are what make the review credible.
- **Reusing PAIN numbers across departments.** Ids are engagement-global;
  a duplicate makes every OPP reference ambiguous (and the checker fail).
- **Briefing after the workshop.** The briefing's value is that *you* choose
  what to ask; generate it the day before.

**Next stage:** [3 — AS-IS review](03-asis-review.md) once a department's
content is complete.
