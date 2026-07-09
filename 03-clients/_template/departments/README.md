# Per-department discovery workspaces

One folder per in-scope department, named `NN-<dept>` where `NN` is the
**two-digit catalog department number** from
`07-roadmap-engine/catalog/departments.json` and `<dept>` its id — e.g.
`02-sales/`. The `departments` list in `engagement-config.json` defines which
numbers are in scope; `check_engagement.py` verifies a workspace exists for
each of them (folders starting with `_` are ignored by the checker).

To start a department: copy `_example-dept/` to `NN-<dept>/` and work through
the pipeline steps below (full detail: `07-roadmap-engine/README.md`).

## Workspace layout

| Path | Step | Contents |
|---|---|---|
| `briefings/` | 0a — Brief | Pre-workshop briefing packs (known facts, hypothesis scope, numbered questions, applicable patterns) |
| `inputs/` | 0 — Collect | Raw meeting material, one file per meeting: `YYYY-MM-DD-<topic>-<type>.md`, source quality noted in the header |
| `pains.md` | 1 — Extract | Discrete pain points as `## PAIN-x` blocks (literal quote + source citation, type, severity, volume) |
| `content/NN-<dept>.md` | 2 — Document | AS-IS per catalog process as `## <CODE>` blocks, with the status header table that carries the approval gate |
| `coverage.md` | 2 — Document | Scope matrix — every catalog process of this department is either documented or gets a one-line out-of-scope reason |
| `flows/NN-<dept>.process.json` | 3 — Flows | Client-adapted AS-IS flow (optional; the standard flow in `07-roadmap-engine/flows/` is the default) |

## Rules that bite

- **No diagnosis before approval.** Opportunities may only be written once every
  in-scope department's content file says `Status: approved` (consultant AND
  client agree the AS-IS is a faithful picture). The checker enforces this.
- Every PAIN keeps a **literal client quote** and a **source citation**
  (`<file> §<n>`). Contradictions between meetings go to the consultant as a
  question, never silently resolved.
- Process codes come from the catalog (`<PREFIX>.<NNN>`) — the controlled
  vocabulary everything maps to. Unknown codes are check errors.
- After every authoring step:
  `python3 07-roadmap-engine/tools/check_engagement.py 03-clients/<slug>`
