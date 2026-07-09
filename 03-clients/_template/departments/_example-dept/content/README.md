# content/ — AS-IS documentation (Step 2)

One file per department: `NN-<dept>.md` (e.g. `02-sales.md`). It opens with the
**status header table** — the approval gate the whole pipeline hangs on — then
one `## <CODE>` block per in-scope catalog process describing how it runs today.

## Status header table (first thing in the file)

```markdown
| Client | Afdeling | Status | Laatst gereviewd |
|---|---|---|---|
| InstallTech BV | Verkoop & offertes | draft | 2026-06-20 |
```

**Status** enum: `draft | consultant-review | client-review | approved`.
Only set `approved` when consultant **and** client agree the AS-IS is a
faithful picture — no diagnosis before that. Date is `YYYY-MM-DD`.

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
