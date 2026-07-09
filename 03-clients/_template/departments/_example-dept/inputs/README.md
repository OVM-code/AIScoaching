# inputs/ — raw discovery material (Step 0)

One file per meeting, **text only** (transcribe recordings first):

```
YYYY-MM-DD-<topic>-<type>.md
```

- `<topic>` — short kebab-case subject, e.g. `verkoop`, `planning-walkthrough`
- `<type>` — `transcript` | `notes` | `walkthrough` | `email` | `doc`

Examples: `2026-06-12-verkoop-transcript.md`, `2026-06-15-planning-notes.md`.

## Quality header

Every input file starts with a header noting the source quality — pain
extraction weighs evidence by it:

```markdown
| Bron | Datum | Type | Kwaliteit |
|---|---|---|---|
| workshop verkoop (2 pers., binnendienst) | 2026-06-12 | transcript | high — volledige opname, sprekers gelabeld |
```

Quality: `high` (full recording/transcript), `medium` (live notes),
`low` (recollection, second-hand) — always with a short reason.

Number the sections or paragraphs (`§1`, `§2`, …) so `pains.md` can cite
`inputs/2026-06-12-verkoop-transcript.md §14`.
