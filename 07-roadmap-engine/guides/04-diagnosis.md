# Stage 4 — Diagnosis

> New to this system? Read [`README.md`](README.md) first.
> Spec for the OPP block, score math, and enums: [`../README.md`](../README.md).

## What this stage is

Engine step 5: the approved AS-IS becomes an argued register of
opportunities. Scan maturity (F1), generate candidates from pains and value
pools (F2), allocate each to human/automation/agent/hybrid (F4), score Value
× Feasibility (F3), and attach a **falsifiable verdict** to every one. The
default posture is skepticism: a use case is a discard until the evidence
says otherwise, and discards are recorded, never deleted.

## Entry criteria

- **Every** in-scope department `Status: approved`
  ([`03-asis-review.md`](03-asis-review.md)). The tools refuse partial
  diagnosis around an unapproved department — so does the method.

## What you produce

| Deliverable | Where | Done when |
|---|---|---|
| Maturity scan (F1) | `analysis/maturity.md` | scored, with evidence from discovery |
| Opportunity register | `analysis/opportunities.md` | one `## OPP-x` block per candidate incl. discards: allocation, scores, effort, wave, formula, verdict |
| Assumption model | `analysis/assumptions.json` | 4–8 sliders; every € figure derives from them; each names its calibration path in `source` |

## How to work

The heavy lifting is `/build-roadmap-proposal <slug>` — its first half
invokes the `opportunity-diagnostician` agent for everything below, and it
stops honestly if the register is all discards (a well-reasoned "few real
opportunities here" is a valid outcome, not a failure).

1. **Maturity (F1).** Score `analysis/maturity.md` per
   [`../../01-frameworks/F1-ai-maturity-scan.md`](../../01-frameworks/F1-ai-maturity-scan.md)
   — it calibrates how ambitious the waves may be.
2. **Candidates.** Generate opportunities (verb + object + mechanism) from
   approved pains, F2 value pools, and the catalog's opportunity patterns.
3. **Allocate (F4 HAA).** `automation | agent-T1 | agent-T2 | agent-T3 |
   hybrid` — every agent starts at T1 and earns promotion; the tier is also
   your EU AI Act human-oversight story (F6).
4. **Score (F3).** `Value = 0.50*hours + 0.25*quality + 0.25*strategic`;
   `Feasibility = 0.40*data + 0.30*technical + 0.30*ownership` (each 1–5,
   adoption as tie-break). The `Verdict` — `quick-win | big-bet | fill-in |
   discard` — must match the computed quadrant ("high" = ≥ 3.5); mismatches
   are checker errors.
5. **Verdicts, falsifiable.** Every OPP carries confidence **and** a "what
   would change this" line — the concrete observation that would flip it.
6. **Assumptions.** Define 4–8 sliders in `assumptions.json`. Each OPP's
   `Waardeformule` is plain arithmetic over assumption ids; `Aannames` lists
   the bare ids the formula uses (exactly that set). Substantiation prose
   goes in a free-form `Cijferbasis` bullet, which the tools ignore.
7. **Check.** After every authoring step:
   ```bash
   python3 07-roadmap-engine/tools/check_engagement.py 03-clients/<slug>
   ```
   Unknown codes, dangling PAIN/OPP references, formula tokens not in
   `assumptions.json`, out-of-range scores, verdict/quadrant mismatches — all
   errors.

## What you must judge yourself

- **Challenge every verdict.** The agent drafts skeptically, but you own the
  claim: is the falsifier real, would you defend the confidence to the
  sponsor? Honest ROI: self-reported savings inflate 2–3× — the proposal
  says so, so the diagnosis must survive that discount.
- **The discard line.** Deciding a candidate is *not* worth proposing is
  consulting judgment, not a scoring artifact.

## Definition of done

- Register complete including discards; every verdict falsifiable; every €
  OPP has a formula over declared assumptions.
- `check_engagement.py` clean; csv row at `diagnosis` → ready for `proposal`.

## Common pitfalls

- **Verdicts without falsifiers.** "Quick-win, high confidence" with no
  what-would-change line is an opinion wearing a label.
- **Magic numbers in formulas.** A € figure hard-coded in the formula
  instead of driven by a slider can't be challenged in the workshop — which
  is the whole point of the assumption model.
- **Inflating scores to make a proposal happen.** Few real opportunities is
  a deliverable; a padded register is a liability with your name on it.
- **Deleting discards.** The discard list is presented in the workshop as
  evidence of rigor — a register with only winners hasn't looked properly.
- **Assumption sprawl.** More than 8 sliders and the client stops
  understanding what drives the numbers.

**Next stage:** [5 — Proposal](05-proposal.md) once the register is
checker-clean.
