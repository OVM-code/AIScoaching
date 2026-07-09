# briefings/ — pre-workshop briefing packs (Step 0a)

Before each department workshop, generate a briefing pack here:
`YYYY-MM-DD-briefing.md`. It primes the workshop so no interview time is wasted
rediscovering what intake already told us.

## Briefing pack format

```markdown
# Briefing — <department> workshop <date>

## 1. Known facts (from intake / client-context.md)
What we already know about this department: headcount, systems, volumes,
pains already hinted at. Cite the source ([VERIFY] items stay tagged).

## 2. Hypothesis scope per catalog process
One row per process of this department from
07-roadmap-engine/catalog/departments.json:
| Code | Proces | Hypothese in scope? | Waarom / signaal uit intake |
|---|---|---|---|

## 3. Numbered questions
Q1, Q2, … — what the workshop must answer. Stories, not opinions
("tell me about the last time X went wrong"); quantify on the spot.

## 4. Applicable patterns
Value-leak and AI-opportunity patterns worth probing, pulled from
07-roadmap-engine/catalog/departments/NN-*.md and 06-knowledge/ —
each with the tell-tale sign to listen for.
```
