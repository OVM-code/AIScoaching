# Branding — optional white-label tokens for built deliverables

This folder is the **white-label hook** for every built deliverable (AS-IS
review, roadmap proposal). It ships **empty by design** — vendor-neutral, no
assets checked in. Drop a `tokens.css` (and logo files) here to brand every
build; swap the folder's contents to rebrand for another consultancy. When the
folder holds no `tokens.css`, the builders behave exactly as if it didn't
exist — byte-identical output.

## The contract

| File | What it is |
|---|---|
| `tokens.css` | One `:root { … }` block of CSS custom properties (see below) |
| `*.png` / `*.svg` | Logo files referenced by `tokens.css` via `url(...)` — inlined as data-URIs at build time |

Recognised custom properties (all optional):

```css
:root {
  --brand-accent: #0055aa;    /* primary brand colour */
  --brand-ink: #111418;       /* body-text colour */
  --brand-paper: #ffffff;     /* page/surface background */
  --brand-logo-dark: url("logo-dark.svg");   /* logo for light surfaces */
  --brand-logo-light: url("logo-light.svg"); /* logo for dark surfaces  */
}
```

`--brand-logo-dark` / `--brand-logo-light` may be written as data-URIs
directly, or as `url()` references to png/svg files in this folder — the
builders (`tools/build_asis.py`, `tools/build_proposal.py`, via their
`branding_css()` helper) base64-inline any referenced local file so the built
HTML stays fully self-contained and offline.

## How it flows into a build

At build time `branding_css()` prepends the token block(s) **before** the
viewer/proposal CSS, in this order (later wins by the CSS cascade):

1. `07-roadmap-engine/branding/tokens.css` — engine-wide brand (this folder);
2. `03-clients/<slug>/branding/tokens.css` — optional per-client override
   (same contract, images resolved against the client's branding folder);
3. the stock viewer/proposal CSS;
4. the per-client `accentColor` from `engagement-config.json` — which
   therefore **always wins** for the accent, branding or not (the AS-IS build
   appends it as `--accent`; the proposal page applies it at runtime from its
   data payload).

The stock viewer/proposal stylesheets consume the `--brand-*` properties only
where they opt in; a `tokens.css` may additionally override any custom
property those stylesheets define (e.g. `--accent`) — subject to rule 4.

No build ever references these files at view time; deliverables stay
self-contained. Keep logos small (< ~50 KB) — they are embedded into every
built HTML file.
