# F6 — Governance, Risk & EU AI Act

Right-sized governance: enough to be safe and legal, light enough that it doesn't strangle adoption. Scales from a 2-page SME policy to an enterprise governance charter.

> ⚠️ You are a coach, not a law firm. This framework structures the questions and produces solid drafts; final policy/legal sign-off on AI Act & GDPR positions belongs to the client's counsel. Say this in every governance deliverable.

## 1. The minimum viable governance stack

| Layer | SME version | Enterprise version |
|---|---|---|
| **Usage policy** (D29) | 2 pages: allowed tools, forbidden data, verification duty, disclosure rules | Full policy + tool whitelist process + role-specific annexes |
| **Risk register** (D30) | Top-10 list reviewed quarterly by AI Lead | Register per use case, owner, mitigations, review cadence |
| **Human oversight** | Autonomy tiers (F4) written into each agent spec | + escalation paths, audit sampling, incident process |
| **Decision rights** | AI Lead decides tools & use cases; owner/CEO signs policy | AI board (quarterly): portfolio, risk acceptance, policy changes; CoE executes |
| **Lifecycle** | Review each agent quarterly: accuracy, complaints, cost | Full MLOps-lite: versioned prompts, eval sets, change log, benefit tracking |

## 2. EU AI Act — practical posture (in force; obligations phased 2025–2027)

Most coaching clients are **deployers** of general-purpose AI systems, not providers — the burden is real but manageable. Timeline that matters (verify current dates when delivering — guidance still evolving):

- **Since Feb 2025**: prohibited practices banned (social scoring, emotion recognition at work except safety/medical, manipulative systems) + **AI literacy duty (Art. 4)** — staff using AI must be adequately trained. Your training curriculum (D26) *is* the compliance artifact; say so.
- **Since Aug 2025**: GPAI model obligations (mostly on providers — Anthropic/OpenAI etc., not your client).
- **Aug 2026**: high-risk system obligations bite. Relevant to clients mainly for **employment-related AI** (Annex III): CV screening, performance evaluation, task-allocation systems that materially affect workers → if a client wants these, treat as high-risk: DPIA/FRIA, human oversight, logging, works-council information.
- **Transparency duties**: chatbots must disclose they are AI; AI-generated content marked where required.

**Deployer checklist per use case** (this is Prompt 6.3's engine):
1. Prohibited practice? → stop.
2. Annex III high-risk (esp. employment, credit, essential services)? → full high-risk track or descope.
3. Interacts with people? → disclosure design.
4. Personal data involved? → GDPR track below.
5. All cases → literacy (trained users), human oversight per tier, logging of material decisions, vendor terms checked.

## 3. GDPR essentials for AI use cases

- **Legal basis & purpose**: reusing customer data to feed an agent = new processing purpose → update privacy notice/register (ROPA).
- **Processor terms**: use business/commercial tiers of AI tools (no training on your data, DPA available, EU processing where offered). Consumer-tier tools for personal data = no.
- **Data minimization**: agents get the fields they need, not database dumps; anonymize/pseudonymize in prompts where possible.
- **DPIA triggers**: systematic monitoring, large-scale sensitive data, employee evaluation → do the DPIA before the pilot, not after.
- **Employee data**: anything touching performance signals → HR + works council early (see F4 §6).

## 4. Risk register — the recurring top risks

| Risk | Typical mitigation |
|---|---|
| Hallucinated content reaches a customer | Autonomy tier T1/T2, verification duty in policy, spot audits |
| Confidential data pasted into consumer tools | Sanctioned-tool availability + policy + training (ban alone fails) |
| Vendor lock-in / price shock | Assemble-over-build default, exportable data, annual vendor review |
| Agent quality drift after model updates | Eval set per agent (10–30 golden test cases), re-run on every change |
| Key-person risk (the one builder) | Documentation standard, second maintainer, coach retainer |
| Adoption collapse after novelty fades | F5 reinforcement + monthly usage metrics with owner |
| Works-council conflict over monitoring | Involve early; design data collection to measure processes, not people |

## 5. Vendor/tool selection (D21) — scoring dimensions

Fit-for-task (weight 30) · Data protection & residency, DPA, no-training terms (25) · Integration with existing stack (20) · Cost at realistic volume incl. seats vs. usage (15) · Maturity/support/exit-ability (10). Default stack bias: tools the client already pays for (M365/Google + their ERP's AI features) + one LLM workspace (e.g., Claude) + one automation platform (Make/Zapier/Power Automate) — then specialize only where a gap is proven.
