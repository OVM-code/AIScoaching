# 06 — Knowledge System (field notes → compounding advantage)

Every real number, objection and insight from the field gets captured on your phone in seconds, merged into structured knowledge files by Claude, and flows back out into business cases, previews, content and the call script. In a year this is the moat: claims and benchmarks no competitor has.

**Cost: €0. Dependencies: none. Maintenance: one HTML file and three markdown files.**

## The flow

```
PHONE (during/after visits, calls, events)
  capture.html → pick type → 3-6 big fields → queue (offline, localStorage)
        │  end of day: "Exporteer alles" → share/copy
        ▼
CLAUDE (mobile app chat or this repo session)
  paste blocks + the MERGE prompt below
        │
        ▼
KNOWLEDGE FILES (this folder, git-versioned)
  benchmarks.md · objections.md · patterns.md   (+ lead updates → your leads sheet)
        │
        ▼
USED BY: business cases (D10) · AI Strategy Previews (P-B) · content (M4)
         call script objection table · FAQ · the acquisition deal lens (M2 §0)
```

## Setup (once, 5 minutes)

1. **Phone access to capture.html** — pick one:
   - *Simplest:* upload `capture.html` to your Netlify site (e.g. as `/capture`), open it on your phone, "Add to home screen". It has `noindex` and no data leaves the page.
   - *No hosting:* send the file to your phone (mail/AirDrop/Drive), open in browser, add to home screen. Works fully offline either way; the queue survives closing the browser.
2. Add `C001 = first client` to `clients.md` when the first client lands.

## The capture grammar (schema v1 — the stable interface)

Every entry the phone tool produces looks like:

```
@CAPTURE v1 benchmark 2026-07-06 14:30
client: C003
sector: HVAC
size: 12
metric: uren offerte-opmaak per week
value: 9u
confidence: told-by-owner
context: twee zaakvoerders doen offertes 's avonds
@END
```

Five types: `benchmark`, `objection`, `pattern`, `lead`, `note`. The grammar is the contract: **files and tools may evolve, the grammar stays**, so the phone tool never needs rework. Version bumps (`v2`) only add fields, never rename.

## PROMPT — KNOWLEDGE MERGE (paste with your exported blocks)

```
You maintain my field-notes knowledge system (06-knowledge/). Below are
capture blocks in my @CAPTURE v1 grammar. Process them:

1. Route each block: benchmark → benchmarks.md table row; objection →
   objections.md (if the objection already exists, increment its count and
   improve the best-response cell if mine landed better); pattern →
   patterns.md row; lead → format as a row for my leads sheet and return
   it separately (it does NOT go in the knowledge files); note → propose
   where it belongs and ask me if unclear.
2. Anonymize: client codes only, never names, in the knowledge files.
3. Keep the existing table schemas exactly; append, never rewrite history.
4. Then tell me, in 3 bullets max: which existing [ESTIMATE] in my system
   these new numbers could replace, which objection is now frequent enough
   (3+) to earn a content post or FAQ entry, and anything contradicting
   what the knowledge base already says.

Return the updated file sections ready to commit (or apply them directly
if you have repo access).

BLOCKS:
{{PASTE EXPORT}}
```

## PROMPT — ENGAGEMENT RETRO (after each Kickstart / pilot / lost deal)

```
Engagement retro for {{CLIENT CODE}} ({{won & delivered / lost at stage X}}).
I answer these 6 questions below: What numbers did we measure (baseline →
result)? Which use cases were chosen and why those? What resistance
appeared and what dissolved it? What would I do differently? What did the
client say verbatim that I should remember? What does this teach the
acquisition lens (margin quality, contracts, owner situation)?

Mine my answers into: benchmark rows (measured confidence), objection
updates, pattern rows, a testimonial/case-quote candidate list (with
consent status), and any correction to my frameworks or copy (flag file +
section, don't rewrite yet). Same rules as the merge prompt.

MY ANSWERS: {{...}}
```

## Scaling path (designed in, so nothing needs redesign later)

| Stage | Volume | Storage | What changes |
|---|---|---|---|
| 1 (now) | 0–50 entries | Markdown tables in this folder | Nothing — Claude merges, git versions |
| 2 | 50–500 | `benchmarks.md` splits per sector; optionally mirror to CSV/Google Sheet for pivots | Same grammar, same prompts |
| 3 | 500+ / team | Move tables to a real database (Notion/SQLite/CRM); capture tool posts to it | Only the merge destination changes; capture.html untouched |

Rules that make it scale: append-only · one schema per file, documented in the file header · client codes everywhere · every row carries date + source confidence, so old/weak data can be filtered instead of cleaned.

## Maintenance notes

- `capture.html` is one file, zero dependencies, works offline, dark-mode aware. If you change the schema, bump the version string in one place.
- The queue lives in your phone browser's localStorage: export before switching phones or clearing browser data. Exporting does not clear; clearing asks for confirmation.
- Weekly ritual (2 min, part of the Friday scorecard): export → merge → commit. Captures are cheap; unmerged captures are worthless.
