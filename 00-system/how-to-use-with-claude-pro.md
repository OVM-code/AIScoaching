# How to Run This System with Claude Pro

You do **not** need the API, Claude Code, or any automation platform to deliver these engagements. Everything runs in claude.ai with a Pro subscription. This document is your operating manual.

## 1. One Claude Project per client

Claude Pro includes **Projects** — persistent workspaces with uploaded knowledge that every conversation in the project can read.

For each client, create a Project named `AI Coaching – <Client>` and upload:

| Always | Per phase |
|---|---|
| `client-context.md` (the living client dossier) | The relevant framework file(s) from `01-frameworks/` |
| `00-system/engagement-flow.md` | The current phase playbook from `02-phase-playbooks/` |

Set the **Project instructions** (custom instructions field) to:

```
You are the delivery engine for an AI-integration coaching engagement.
The consultant (the user) coaches businesses on integrating AI, automation
and agents into their strategy, organization and processes.

Rules:
- Always ground outputs in client-context.md. If information is missing,
  ask up to 5 targeted questions BEFORE generating, then generate.
- Outputs are client-facing drafts: professional, concrete, no filler,
  no hype. Use the client's language (NL/FR/EN) when asked.
- Use European context by default: EUR, GDPR, EU AI Act, works councils.
- Never invent client-specific numbers. Mark assumptions as [ASSUMPTION]
  and estimates as [ESTIMATE] with the reasoning.
- When a prompt references a framework (F1–F6), follow that framework's
  structure and scoring rules exactly.
```

## 2. Session discipline (working within Pro limits)

Claude Pro has usage limits that reset every 5 hours. To make them a non-issue:

- **One deliverable per conversation.** Start a fresh chat in the Project for each numbered prompt. Long chats burn limits fastest because the whole history is re-read every turn.
- **Front-load context in the Project, not the chat.** That's what the uploads are for.
- **Batch your review comments.** Instead of 10 small "change this" messages, give one consolidated revision list.
- **Do heavy generation early in your working block**, review/polish later.
- If you hit a limit mid-deliverable: the prompt + client-context are all Claude needs — resume in a new chat with "Continue generating <deliverable>, we got to section X."

## 3. The prompt convention

Every prompt in the phase playbooks follows the same pattern:

```
PROMPT <phase>.<number> — <deliverable name>
Inputs:  what must be in the Project or pasted in
Output:  the deliverable + format
```

Placeholders in `{{DOUBLE_BRACES}}` are things **you** fill in before sending. Everything else is ready to paste.

## 4. Producing client-ready documents

Claude outputs Markdown. Your delivery pipeline options, in order of effort:

1. **Ask Claude for the format directly** — "format this as a one-page memo", "give me this as a slide-by-slide outline with speaker notes", or ask for an **Artifact** (claude.ai renders polished documents/pages you can export or copy).
2. **Paste Markdown into Notion / Google Docs** — both render it cleanly; apply your branding template.
3. **Slides**: ask for a "slide outline: title, 3–5 bullets, one data point, speaker notes per slide", then build in PowerPoint/Canva/Gamma.

Keep a `deliverables/` folder per client (Drive/Notion) mirroring the phase numbers, so version N of every asset is findable.

## 5. The living client-context.md

This file is the engine of personalization. Rules:

- Created in Phase 0 (Prompt 0.1) from the intake questionnaire.
- **Updated at the end of every phase** — each playbook's final prompt regenerates the "Engagement status" and "Decisions log" sections.
- Re-upload to the Project after every update (replace the old file).
- Contains no secrets beyond what the client approved you to hold. If the client is sensitive about data, keep financials in ranges.

## 6. Confidentiality & good practice

- Get written consent from the client to process their business information with Claude. A one-line clause in your engagement letter is enough: *"The consultant uses Anthropic Claude (EU-hosted processing where available, no training on business data under commercial terms) to draft engagement deliverables."*
- Turn **off** "Help improve Claude" in claude.ai settings (Settings → Privacy) so conversations aren't used for training.
- Anonymize personal data (employee names → roles) before uploading anything HR-related.
- Never upload: customer personal data, credentials, anything under NDA from third parties.

## 7. What to do live in workshops vs. between sessions

| Live with the client | Between sessions (you + Claude) |
|---|---|
| Intake interviews, pain-point harvesting | Turning notes into the context doc & inventories |
| Prioritization workshop (they score, you facilitate) | Pre-scored draft matrix to react to |
| Org-design working session (managers own the boxes) | Draft target organigram options A/B/C |
| Change-story co-creation with leadership | Polished narrative + comms assets |
| Pilot reviews | Pilot charters, metrics dashboards, retro summaries |

The pattern: **Claude drafts, workshop reacts, Claude revises.** People commit to what they helped shape — never present a Claude draft as a fait accompli.
