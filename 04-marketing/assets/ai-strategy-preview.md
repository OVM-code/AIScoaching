# AI Strategy Preview — personalized lead magnet from a company URL

A 4-page, company-specific preview of an AI strategy, generated **entirely from public information** (their website, job postings, reviews, LinkedIn, news, annual reports). You feed the pipeline a URL; it produces a document good enough to impress, deliberately incomplete enough to require the paid engagement — and every reaction the prospect gives feeds straight into the client-context system.

Implements: LEADS-2 (narrow problem solved: "what would AI even mean for *us specifically*?"), LEADS-5 (a give, not a pitch), OFFER-1 (personalization = perceived likelihood ↑), POS-3 (demonstrate diagnosis, never give away prescription).

## Where it sits in the funnel

The **AI-Scan** (self-serve) stays the volume lead magnet. The **Preview** is the *sniper* lead magnet: for named targets — cold outreach to specific SMEs you want, partner introductions, corporate-track door-openers, and event follow-ups. Budget ~30–45 min of your time per preview (Claude does the heavy lifting; you verify). Use it when the target is worth that.

```
URL ─► Prompt P-A (research dossier) ─► Prompt P-B (preview doc) ─► your QA ─► send
                                                                        │
                             20-min reaction call ("what did we get wrong?")
                                                                        │
        Prompt P-C: reactions ─► seed client-context.md + tailored next-step pitch
```

## The three design rules (why it converts instead of satisfying)

1. **The 80% mirror.** The preview says out loud that it's built from outside signals and is "80% right at best — you correct the rest in 20 minutes." Errors and gaps are not weaknesses; they are the **reason for the call**. A perfect document would end the conversation.
2. **Show 3, name 10.** It presents the 3 opportunities visible from outside (with value *ranges*), and states that a full scan typically surfaces 8–12 — including the biggest ones, which live in data no outsider can see (their calendars, mailboxes, ERP). The visible value proves method; the named invisible value creates pull.
3. **Diagnosis shown, prescription withheld.** One opportunity gets a vivid before/after scene ("Monday morning, version 2") — but never the how: no tool names, no build steps, no roadmap, no org design. What we'd *validate first*, yes; what we'd *build and how*, no. (Withhold-list at the end of this file — check it before sending, every time.)

---

## PROMPT P-A — Research dossier (run first, with web search ON)

```
You are researching a company for me, an AI-integration coach, so I can
write a personalized "AI Strategy Preview" for them. Use web search
extensively. Company: {{URL}} {{+ COMPANY NAME / LOCATION if ambiguous}}.

Build a research dossier from PUBLIC sources only:

1. Business basics: what they do, for whom, services/segments, locations,
   languages; size signals (team page, LinkedIn employee count, fleet
   photos, "since 19XX", revenue if published)
2. Commercial signals: how leads contact them (form/phone/WhatsApp?),
   response promises ("offerte binnen X dagen"?), certifications, brands
   they carry, maintenance-contract offerings
3. Pain signals — the gold, look hard:
   - Job postings (what roles can't they fill? admin roles = process pain;
     "flexibele duizendpoot" = chaos)
   - Google/Facebook reviews: recurring complaints (slow quotes, no
     callbacks, invoicing issues) AND what customers praise
   - Website copy that betrays process ("wij antwoorden binnen 5 werkdagen")
   - News/interviews/podcasts with the owner; growth or succession signals
   - For corporates: annual report priorities, investor communications,
     transformation programs, works-council news
4. Tech footprint: visible systems (career-page ATS, webshop platform,
   booking tools, planning software mentioned in vacancies), any AI
   mentions by them
5. Competitive frame: 2-3 similar local/sector players and anything they
   visibly do better/worse
6. People/culture signals: team size split (field vs office) if visible,
   tone of voice, family business markers

Rules: cite the source (URL) for every claim; never present inference as
fact — tag [INFERRED] with your reasoning; if reviews or jobs data are
thin, say so rather than padding; flag anything sensitive we should NOT
use in a commercial document (e.g., a lawsuit, a bad year).

Output the dossier + a final section "The 5 strongest hooks" — the five
findings most likely to make the owner think 'they actually looked at US'.
```

## PROMPT P-B — The preview document (run second, same conversation)

```
Now write the AI Strategy Preview for this company, using the dossier
above plus my positioning (M2) and the sector use-case library if this is
a home-services company. Language: {{NL for Flemish SMEs / EN or FR for
corporates}}. Length: max 4 pages. Tone: vakman-taal / boardroom register
to match the target; zero hype; every claim sourced or tagged [AANNAME].

VOICE: follow M5-voice-and-tone.md throughout (mid-form register; the
observed authority position: noticing, not diagnosing; u-register; no
em-dashes, no hype). The document reports what public signals suggest and
says plainly what only they can confirm.

EXACT STRUCTURE:

── Cover ──
"AI Strategy Preview — {{COMPANY}}" + one-line promise in their terms.
The honesty line, prominent: "Gebaseerd op wat wij publiek konden zien.
Reken op 80% juist. De overige 20% verbetert u in één gesprek van 20
minuten, en precies dat gesprek stellen we voor."

── 1. Wat wij zagen (the mirror, ~1 page) ──
Their business in 6-8 sharp observations WITH the signal that produced
each ("jullie vacature voor een X suggereert...", "in 14 recente reviews
komt Y 3× terug"). Include 1-2 genuine compliments (what they do well —
credibility + likability). This page must trigger: "they did their
homework."

── 2. Waar AI bij {{COMPANY}} waarschijnlijk waarde creëert (~1 page) ──
The 3 opportunities visible from outside. Per opportunity, exactly this
format:
  • Naam (verb + object)
  • Het signaal (why we think this applies to THEM, sourced)
  • Wat het typisch oplevert bij vergelijkbare bedrijven: RANGE in
    uren/week of €/jaar [ESTIMATE, with the one-line math]
  • Zekerheid: hoog/middel/laag — en wat het zou bevestigen (something
    only THEY can see: their planning data, mailbox, quote log)
Close the page: "Een volledige scan bij bedrijven zoals {{COMPANY}} vindt
er doorgaans 8 à 12. De grootste zitten bijna altijd in wat van buitenaf
onzichtbaar is."

── 3. Maandagochtend, versie 2 (the vacation, ~half page) ──
ONE opportunity made vivid: a 150-word before/after scene of a concrete
moment in their week, with their real context (their trade, their region,
their customer type). No tools, no build steps — outcome only.

── 4. Eerste indruk AI-maturiteit + wat we níet kunnen zien (~half page) ──
3 outside-visible maturity signals (not the full 6-dimension scan —
present as "eerste indruk"). Then, explicitly, the section "De twee vragen
die publieke informatie niet beantwoordt": the 2 highest-value unknowns
for this specific company (e.g., "hoeveel uur zit er écht tussen werf en
factuur?"). These 2 questions ARE the hook — make them itch.

── 5. Volgende stap (one CTA) ──
"Vertel ons wat we fout hebben. 20 minuten, u verbetert dit document, wij
zeggen eerlijk of en waar AI bij u de moeite loont — en u houdt dit
document én die inschatting, wat u ook beslist."
Booking link + signature line + footer: "Alle vaststellingen op basis van
publieke bronnen (website, vacatures, reviews, pers). Geen vertrouwelijke
of persoonsgegevens verwerkt."

HARD RULES (the withhold-list — check yourself before finishing):
- NO full use-case list beyond the 3; NO tool or vendor names; NO
  implementation steps, roadmap, timeline or org-design specifics; NO
  business case beyond the per-opportunity range; NO maturity scores.
- Nothing negative that could embarrass them if the PDF gets forwarded
  (they WILL forward it). Critique processes, never people; skip anything
  the dossier flagged as sensitive.
- Numbers only as ranges with visible logic. If the dossier is thin on a
  section, shrink the section — never pad.

After the document, give me separately (not in the doc): the QA checklist
result — every factual claim with its source so I can verify in 5 minutes,
plus the 2 claims you're least sure of.
```

## Your QA before sending (10 min, non-negotiable)

1. Verify the 5 strongest hooks and the 2 least-sure claims against the sources — one wrong "fact" about their own business kills the entire effect.
2. Check the withhold-list held (no tools, no roadmap, no full list).
3. Would you be comfortable if their competitor read it? (It will be forwarded.)
4. Layout: paste into your branded template (Canva/Gamma/Docs), or ask Claude for an Artifact version — max 4 pages, their logo NOT on it (it's about them, not from them), your one-liner + photo in the footer.

## Sending it (outreach integration)

Replaces touch 1-2 of the cold sequence for sniper targets:

> **Onderwerp: wat AI voor {{BEDRIJF}} kan betekenen, alvast uitgezocht**
> Dag {{VOORNAAM}}, in plaats van u een folder te sturen heb ik mijn huiswerk gedaan: in bijlage vindt u een korte AI-preview specifiek voor {{BEDRIJF}}, gebaseerd op wat publiek te zien is (uw site, vacatures, reviews). Reken op 80% juist, want de overige 20% kent alleen u. Als u me in twintig minuten vertelt wat ik fout heb, krijgt u er mijn eerlijke inschatting bovenop of AI bij u de moeite loont. Ik vermoed dat minstens één van de drie kansen op pagina twee u bekend zal voorkomen. {{CALENDLY}} Groeten, {{NAAM}}

Corporate variant (EN/FR): same mechanic, reference their public transformation priorities instead of reviews; CTA = "30 minutes of your corrections" (the Enns feedback-ask, now with a personalized artifact attached).

## PROMPT P-C — Feedback capture → the system takes over

Run after the reaction call, in the same Project. This is the bridge into `00-system` / Phase 0.

```
Below are my notes from the reaction call about the AI Strategy Preview
for {{COMPANY}} (what they confirmed, corrected, dismissed, got excited
about, plus any numbers/frustrations they volunteered).

Produce three things:

1. SEED CLIENT CONTEXT: a pre-intake client-context.md following my
   standard structure (Prompt 0.1's 11 sections), populated from: the
   research dossier (P-A) + the preview + these reactions. Tag every item
   [PUBLIC], [CONFIRMED], [CORRECTED: old→new], [THEY VOLUNTEERED] or
   [STILL UNKNOWN]. Sections we can't fill yet stay as targeted questions —
   this doc must make my eventual intake interview 30 minutes shorter, not
   replace it.

2. READ-OUT OF THE REACTIONS: what their likes/dislikes reveal —
   which value pool pulls them (P1-P4), where the resistance sits (money/
   time/people/trust, per my discovery-call objection set), who else was
   mentioned as involved in deciding, and their language: 5 phrases they
   used that I should mirror in everything that follows.

3. THE TAILORED NEXT STEP: based on 1+2, recommend ONE: (a) straight to
   Kickstart offer — draft the 5-line proposal email in their words;
   (b) AI-Scan/debrief first — draft the invite; (c) corporate: paid
   Phase 0-1 diagnostic — draft the scoping note; or (d) polite park —
   draft the stay-in-touch note + what signal would reopen. Justify the
   pick in 3 lines against the reactions.

MY CALL NOTES: {{PASTE}}
```

If they convert, the seed context from P-C becomes the input to **Prompt 0.1** — intake now only fills the `[STILL UNKNOWN]` gaps. The preview's corrected claims carry forward as `[CONFIRMED]` facts, so nothing learned in the funnel is ever re-asked. (Phase-0 playbook notes this path.)

## Tone calibration snippet (what "good" reads like — fictional example)

> **Wat wij zagen:** U belooft op de site "offerte binnen 5 werkdagen", en uw 4,6★ op Google bevestigt dat klanten uw stiptheid op de werf prijzen, maar in 3 van de 14 recente reviews klinkt "lang moeten wachten op de offerte". Tegelijk zoekt u al vier maanden een administratief bediende (vacature op VDAB, hernieuwd in mei). Onze lezing: het kantoor is de flessenhals, niet de werf, en de arbeidsmarkt gaat die vacature waarschijnlijk niet voor u oplossen. [PUBLIC — bronnen: website/offertepagina, Google Reviews mei-juni, VDAB]

## Regeneration prompt (new niche)

```
Re-target this asset for {{NICHE}}: keep the pipeline (P-A research →
P-B document → QA → P-C feedback-to-context) and the three design rules
(80% mirror / show 3 name 10 / diagnosis not prescription) intact.
Rewrite: the pain-signal hunting list in P-A for where THIS niche's pain
shows publicly ({{e.g., for accountants: vacancy texts, Google reviews on
responsiveness, software partner pages}}), P-B's section titles and
register in {{LANGUAGE}}, the Monday-morning scene archetype, the send
email, and the tone snippet. Value ranges must come from the niche's
use-case list (M2 niche-swap output).
```
