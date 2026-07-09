# content/ — AS-IS documentation (Step 2)

One file per department: `NN-<dept>.md` (e.g. `02-sales.md`). It opens with the
**status header table** — the approval gate the whole pipeline hangs on — then
a `## Gate` section with the reviewers' directives, then one `## <CODE>` block
per in-scope catalog process describing how it runs today.

## Status header table (first thing in the file)

```markdown
| Client | Afdeling | Status | Laatst gereviewd | Goedgekeurd door | Datum |
|---|---|---|---|---|---|
| InstallTech BV | Verkoop & offertes | draft | 2026-06-20 | — | — |
```

**Status** enum: `draft | consultant-review | client-review | approved`.
Only set `approved` when consultant **and** client agree the AS-IS is a
faithful picture — no diagnosis before that. On approval fill in
`Goedgekeurd door` (who approved) and `Datum`; until then both are `—`.
Dates are `YYYY-MM-DD`.

## `## Gate` section — directives (before the first `## <CODE>` block)

```markdown
## Gate

**Directieven**

- [ ] doorlooptijd per offerte ook opnemen in SAL.030
- [x] volume gecorrigeerd naar 40/maand (toegepast 2026-06-18)
```

Directives are the consultant's/client's change instructions from a review:
record them here, apply them to this file, and tick them off with the date
applied. `Status: approved` with any open `- [ ]` directive is a
`check_engagement.py` error — apply or withdraw them first.

## `## <CODE>` block per process

```markdown
## SAL.030 — Offerte opstellen
- **Huidige werkwijze:** Binnendienst hertypt aanvraag uit e-mail in Excel-sjabloon, …
- **Wie:** binnendienst (2 pers.)
- **Systemen:** Outlook, Excel, boekhoudpakket
- **Volume & tijd:** 40/maand, ±45 min per offerte
- **Pijn:** PAIN-3, PAIN-4
- **Severity:** major
- **Automability:** agent
```

- `Pijn` references must resolve to `## PAIN-x` blocks in this department's
  `pains.md`; a process without pain simply omits the line.
- **Severity** (drives the flow color): `none | minor | major | critical`.
- **Automability** (F4 first look): `human | automation | agent | hybrid`.
- Codes must exist in `07-roadmap-engine/catalog/departments.json`; processes
  out of scope get a one-line reason in `../coverage.md` instead of a block.
