# flows/ — client-adapted AS-IS flow (Step 3)

**The standard flow is the default — start by copying, never from scratch.**

```bash
cp 07-roadmap-engine/flows/NN-<dept>.process.json \
   03-clients/<slug>/departments/NN-<dept>/flows/
```

Then adapt it to the client's real process: extra channels, missing approval
steps, steps done by a different lane, … A file here with the same `domain`
number **overrides** the standard flow at build time; if this folder stays
empty, `build_asis.py` uses the standard flow as-is.

Format: `*.process.json` per the spec in `07-roadmap-engine/README.md` —
`id`, `domain` (this department's catalog number), `title`, `lanes`, `nodes`
(types `start | end | task | subprocess | gateway | gateway-parallel`), `flows`.
Node `process` codes make steps clickable and color-coded and must exist in the
catalog. Keep flows at 10–20 nodes; split bigger ones into a `subprocess` +
`goto`. Labels: plain string or `{nl,en}`.

`check_engagement.py` validates every `*.process.json` here: lane and node
references, node types, process codes.
