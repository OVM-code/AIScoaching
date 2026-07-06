# AI Website-Builder Prompt Pack

Prompts to build the site in an AI website tool (Lovable, Framer AI, Bolt.new, v0.dev, …). They encode everything that matters — approved copy, voice, trust design, conversion structure, truth rules — so the tool's creativity goes into *design quality*, not into inventing content.

**Tool choice, quick guidance:**
- **Lovable** (recommended): full site from prompts, chat-based iteration, free hosting + custom domain, exports code. Best prompt-obedience for this pack.
- **Framer AI**: strongest visual polish, easy editing afterwards; slightly more manual layout work.
- **Bolt / v0**: more developer-flavored; fine if you want the code in this repo afterwards.

**How to use the pack:** run W1 (the master prompt) first, in one message. Then iterate with W2–W7 one at a time, checking the result between each. Never accept invented content: the truth rules are in W1, but AI builders relapse — W7 is the audit that catches it.

The hand-built site in this folder stays as reference/fallback; the copy below is identical to the approved copy.

---

## W1 — Master prompt (paste as the very first message)

```
Build a website for an independent AI-integration coach. Read ALL of this
before generating; the copy is final and approved, the rules are hard.

== PURPOSE & CONVERSION LOGIC ==
One job: a visitor (owner of a Belgian installation/service business, 8-50
employees, skeptical of hype and consultants) checks whether this person is
credible, and converts to ONE of two actions:
1. Primary CTA everywhere: "Doe de gratis AI-Scan" (links to an external
   Tally form: use placeholder https://TALLY-SCAN-LINK)
2. Secondary CTA: "Boek een gratis debrief (20 min)" (external booking:
   https://CAL-LINK)
Single-page structure in this exact order (this is a proven persuasion arc,
do not reorder):
1. Hero: promise + subline + both CTAs + microcopy under the button
2. Problem recognition (the visitor's evenings, mirrored back)
3. The 3-step approach + a visually distinct guarantee block
4. Outcomes list
5. Credibility section "Wie is Olivia?" (photo + bio + proof list)
6. FAQ (4 items, accordion)
7. Final CTA section
8. Footer

== THE EXACT COPY (Dutch, final — use verbatim, do not "improve" it) ==
HERO title: "Win tien uur per week terug, zonder extra aanwervingen."
HERO subline: "AI en automatisering voor installatie- en servicebedrijven,
gebouwd met jouw mensen op jouw echte dossiers, en werkend binnen zes weken."
HERO microcopy: "12 vragen, meteen je score, en de tien automatiseringen met
de snelste terugverdientijd."

PROBLEM heading: "Je zaak groeit, maar je avonden krimpen."
PROBLEM body: "Offertes die pas na dagen vertrekken omdat er overdag geen
tijd voor is. Oproepen die je mist omdat je op een werf staat, en die naar
de volgende in het lijstje bellen. Werkbonnen die 's avonds nog overgetypt
moeten worden, facturen die daardoor te laat vertrekken, en betalingen waar
iemand achteraan moet. En ondertussen raakt die vacature maar niet ingevuld.
// Het probleem is niet dat je te weinig doet. Het is dat te veel van je
beste uren naar admin gaan die een systeem intussen beter kan, terwijl het
werk waar je écht goed in bent daardoor in de verdrukking komt. En daar is
vandaag zoveel aan te doen."

APPROACH heading: "Zo pakken we het aan"
Step 1 "Scan": "We vinden waar de uren lekken, in jouw cijfers. Geen
buikgevoel maar een som die je zelf kan nadoen."
Step 2 "Bouw": "In zes weken bouwen we samen met je team de twee
automatiseringen met de snelste terugverdientijd. Werkend, op jullie echte
dossiers."
Step 3 "Veranker": "Je team is opgeleid, de afspraken staan op papier, en
negentig dagen lang stuur ik mee bij. Het resultaat staat gemeten op één blad."
GUARANTEE block: "De garantie, zwart op wit: toont de meting na negentig
dagen geen tien uur per week aan vrijgekomen capaciteit, dan werk ik gratis
verder tot het er staat."

OUTCOMES heading: "Wat het oplevert" — checklist:
- "Offertes de deur uit binnen 24 uur, en systematisch opgevolgd"
- "Werkbonnen ingesproken onderweg, factuur dezelfde dag buiten"
- "Gemiste oproepen die meteen een antwoord krijgen, en dus klant blijven"
- "Een team dat AI gebruikt met duidelijke afspraken, in plaats van stiekem
  of helemaal niet"
- "Groeien zonder te wachten op de vacature die toch niet ingevuld raakt"

CREDIBILITY heading: "Wie is Olivia?"
Bio: "Ik werk elke dag met AI en automatisering als AI- en ERP-consultant
(Microsoft Business Central). Daar heb ik geleerd dat de technologie het
makkelijke deel is: het verschil wordt gemaakt door wie wat doet. Welk werk
blijft bij je mensen, welk werk neemt een automatisering over, en waar voegt
AI echt iets toe?"
Proof list:
- "Bouwde workflows die handgeschreven notities omzetten in kant-en-klare
  documentatie"
- "Werkte mee aan agents die gegevens lezen en schrijven in Business Central"
- "Geeft interne workshops die een consultingteam AI-native maken, en gaf
  een webinar over agents"
- "Werkt met een volledig uitgeschreven methode: van scan tot werkende
  automatisering tot een team dat er zelfstandig mee verder kan"
Honesty paragraph: "Ik bouw momenteel mijn eerste cases in de sector op, en
dat vertel ik je er eerlijk bij. Daarom werken de eerste drie bedrijven aan
founder-voorwaarden, in ruil voor een gedocumenteerde case. Ik start elke
maand met maximaal twee bedrijven."
LinkedIn link: "Volg mijn bouwlog op LinkedIn" →
https://www.linkedin.com/in/olivia-vanmalleghem/

FAQ (question → answer):
"Mijn mensen zijn geen computermensen." → "Dat hoeft ook niet, want een
spraakmemo inspreken kan iedereen, en de rest gebeurt in de achtergrond. Het
team bouwt mee en beslist mee wat er komt. Dat is geen detail: het is de
reden waarom het blijft werken nadat ik weg ben."
"Wat met onze klantgegevens?" → "Alles verloopt GDPR-proof: zakelijke
AI-omgevingen, geen consumententools, en duidelijke afspraken op papier. De
nieuwe Europese AI-regels zitten in de aanpak verwerkt."
"Wij zijn te klein hiervoor." → "Vanaf ongeveer acht medewerkers is de
terugverdientijd doorgaans twee tot vier maanden. Kleiner? Doe de scan, want
het eerlijke antwoord kan ook 'nog niet' zijn, en dat zeg ik je dan even
duidelijk."
"Wéér een consultant?" → "Ik lever geen rapport maar werkende
automatiseringen, een opgeleid team en gemeten cijfers. En de garantie staat
gewoon in het contract."

FINAL CTA heading: "Weet binnen tien minuten waar jouw uren lekken."
Under it: primary CTA button + "Liever meteen praten? Boek een gratis
debrief van twintig minuten." + "Of laat je gegevens achter via dit korte
formulier, dan neem ik contact op." (link: https://TALLY-CONTACT-LINK)

FOOTER: "Olivia Vanmalleghem — AI-integratiecoach voor installatie- en
servicebedrijven" + LinkedIn + mailto:vanmalleghem.olivia@gmail.com +
link "English" to /en. Leave a visible spot for "Ondernemingsnummer: [volgt]".

== DESIGN DIRECTION ==
Personality: light energy, warm, welcoming, possibility-oriented, hands-on.
Think "capable person you'd trust with your business", NOT corporate agency,
NOT tech-startup dark mode, NOT AI-hype gradients.
- Warm off-white background, near-black warm text, ONE warm accent (burnt
  orange / terracotta family) used for CTAs and highlights only; a calm
  green reserved for checkmarks. Light theme.
- Generous whitespace, soft rounded cards, subtle depth. Typography: one
  friendly-but-serious sans (e.g. a humanist grotesque), large readable
  body (17px+), strong clear hierarchy.
- Photography style if stock is used: real Belgian trade contexts (werf,
  van, workshop), warm daylight, real hands and tools. NO robots, NO glowing
  brains, NO blue circuit boards, NO stock-suit-handshakes.
- The credibility section uses a real photo placeholder (label it clearly
  "REPLACE: photo of Olivia") sized generously; trust lives on this section.
- Mobile-first: majority of visitors come from LinkedIn on a phone. CTAs
  full-width and thumb-reachable on mobile; sticky or repeated CTA is fine,
  popups are not.

== HARD RULES (violating any of these = redo) ==
1. NO invented testimonials, reviews, client logos, star ratings, case
   numbers, "trusted by" bars, or team members. None exist yet. The
   honesty paragraph IS the trust strategy.
2. NO em-dashes anywhere in visible text. No emoji in body copy.
3. Do not rewrite, translate, shorten or "punch up" the provided copy.
   Layout microcopy you add (button states, form labels, alt text) must be
   plain Dutch, warm, hype-free: never "unlock", "revolutionair",
   "game-changing", "supercharge".
4. Exactly one primary action per screenful (the scan); the debrief is
   visually secondary everywhere.
5. No cookie-requiring trackers. No chat widgets. No newsletter popups.
6. Fast: no heavy hero video, no autoplaying anything, images optimized.
7. External links (Tally/Cal placeholders) open in a new tab.
8. Semantic HTML, WCAG AA contrast, alt text on all images, works without
   JavaScript for all content (accordion may enhance progressively).

Build the Dutch one-pager now. I will ask for the English page and
refinements in follow-up messages.
```

## W2 — English page (second message)

```
Add a second page at /en for professional/corporate visitors (they check my
credibility when I ask them for feedback on my methodology). Same design
system, same rules (especially: no invented social proof, no em-dashes).
Header on both pages gets a small NL/EN switch.

Structure and exact copy:

HERO title: "AI creates value when the work changes, not when the licenses
arrive."
HERO subline: "I help businesses capture real value from AI by redesigning
how the work flows: humans, automations and agents in one operating model,
with the change management to make it stick. Working automations in weeks,
and a team that can run it without me."
CTAs: "Book a conversation" (https://CAL-LINK) + secondary "Message me on
LinkedIn" (https://www.linkedin.com/in/olivia-vanmalleghem/)

SECTION "What I keep seeing": "Most AI programs fail at the organigram more
often than at the model. The pilots work, the demo impresses, and six months
later the saved hours have quietly disappeared, because every role, handoff
and KPI still assumes the old way of working. And the people side gets a
newsletter instead of a plan. // So I built a complete method for the part
everyone skips, and I use it hands-on with clients."

SECTION "The method, in short" (5 points, keep verbatim):
1. "The unit of redesign is the task, not the job. We decompose priority
   processes and allocate each task to a human, an automation or an agent,
   with simple filtering questions such as: does this step actually require
   intelligence? Most steps need reliability, and reliability is what
   workflows are for."
2. "Roles get recomposed around judgment, relationships and exceptions.
   Only then does anyone touch the org chart, and agents go on that chart
   too, with a named human owner and an autonomy level they have to earn."
3. "One hard rule does a lot of work: in the RACI-A (a classic RACI with an
   agent column) an agent can be responsible, but never accountable."
4. "Change management runs in parallel, not afterwards: ADKAR per affected
   group, honest workforce messaging, training that doubles as the EU AI
   Act literacy evidence."
5. "Everything gets measured, and pilots carry kill criteria that are
   honored. A killed pilot with a clean retro is the system working."
Closing line: "I've written the full method down, from maturity scan to
governance. If you're steering an AI transformation and want to shoot holes
in it, I would genuinely welcome that conversation."

SECTION "Who I am": "I work daily as an AI & ERP consultant (Microsoft
Dynamics 365 Business Central), where the gap between buying technology and
changing how work gets done is visible every single week. I bring light
energy to a serious subject: I genuinely believe most organizations are
sitting on more possibility than they think, and I like proving it with
working things rather than slides." + the same 4-item proof list as the
Dutch bio, in English.

SECTION "Two ways I work": two cards — "For SMEs in home services (BE)"
(fixed six-week Kickstart, written guarantee, link to the Dutch page) and
"For larger organizations" (full engagement: strategy, operating model &
organigram, pilots, change management, governance; starts with a
conversation, not a proposal: diagnosis before prescription).

Footer: same as Dutch, with "Nederlands" link back.
```

## W3 — Design refinement pass

```
Design critique round. Evaluate the current site against these and fix:
1. Squint test: is the primary CTA the most visually prominent element on
   every screenful? Is there exactly one?
2. First 5 seconds: does the hero alone answer "what is this, for whom,
   what do I get, what do I do next"?
3. Warmth check: does it feel like a capable, warm person, or like an
   agency template? Kill anything generic (icon grids with abstract icons,
   purple gradients, laptop mockups).
4. Rhythm: alternate background tones between sections so the page has
   visible chapters; the guarantee block and the credibility section must
   be the two most eye-catching non-hero moments.
5. Typography: max 2 sizes of body text; headings clearly bigger; line
   length 60-75 characters; body at least 17px.
6. Mobile: thumb-test every CTA; check the FAQ accordion; hero must fit
   the value proposition above the fold on a normal phone.
Show me before/after notes on what you changed and why.
```

## W4 — Trust micro-details pass

```
Add the small trust signals that make skeptical business owners relax,
WITHOUT inventing social proof:
1. Under the scan CTA: "Gratis, 10 minuten, geen verkooppraatje. Als het
   niets voor jou is, zeg ik dat ook."
2. In the FAQ or footer area, a plain-language privacy line: "Je gegevens
   worden alleen gebruikt om je scan-resultaat te bezorgen en op te volgen.
   Geen nieuwsbrieven zonder dat je erom vraagt, geen doorverkoop."
3. A subtle "hoe ik werk" strip near the guarantee: "Vaste prijs. Geen
   uurtje-factuurtje. Max twee nieuwe bedrijven per maand."
4. Make the founder-voorwaarden sentence in the bio visually quiet but
   findable (no badge, no countdown, no fake urgency styling).
5. Alt text and title tags: plain, descriptive Dutch.
Keep everything in the existing voice; nothing salesy.
```

## W5 — Integrations (run when the accounts exist)

```
Replace placeholders and wire integrations:
1. Replace https://TALLY-SCAN-LINK with {{real Tally scan URL}} everywhere;
   https://TALLY-CONTACT-LINK with {{real contact form URL}};
   https://CAL-LINK with {{real Cal.com URL}}.
2. Embed the Cal.com booking inline on a small /debrief page (heading:
   "Plan je gratis debrief van 20 minuten") so ad/DM traffic can land
   directly on booking; keep the header CTA linking there.
3. If this tool supports it, embed the Tally scan as a full-page embed on
   /scan with the same header/footer; otherwise keep the external link.
4. Add GoatCounter analytics with this snippet [paste snippet], and verify
   no cookies are set.
5. Add basic SEO: per-page title + meta description (I'll approve the
   texts), Open Graph image using the hero promise, favicon from my
   initials in the accent color, sitemap, language tags (nl / en pages).
```

## W6 — Case study block (run ONLY when the first real scorecard exists)

```
Add a results section to the Dutch page between "Wat het oplevert" and
"Wie is Olivia?", heading "Uit de praktijk". One case card, real numbers
only, this structure:
- Context line: sector + size ("[sector]bedrijf, [Z] medewerkers")
- The before → after metric shown big ("[X] dagen → [Y] uur voor een
  offerte de deur uit is")
- Two supporting numbers ("[N] uur per week vrijgekomen", "terugverdiend
  in [M] weken")
- Client quote with name/company IF I have written consent, otherwise
  role only ("zaakvoerder")
- Link: "Lees hoe we dat aanpakten" → a simple case page with the fuller
  story (I will provide the approved text).
Exact figures I provide here: {{PASTE REAL SCORECARD NUMBERS + QUOTE}}.
Do not extrapolate or round these numbers upward.
```

## W7 — Truth & quality audit (run after every major change)

```
Audit the entire site and report violations before fixing anything:
1. TRUTH: list every claim on the site. Flag anything not in the approved
   copy: invented testimonials/logos/ratings/numbers, implied client
   volume ("honderden bedrijven"), invented team, stock photos presented
   as me or my clients.
2. VOICE: find em-dashes, emoji in copy, hype vocabulary (unlock,
   revolutionair, game-changing, toekomst is nu), salesy urgency styling.
3. CONVERSION: more than one competing primary CTA per screenful? Any
   dead links or placeholder links I should know about?
4. TECH: mobile layout breaks, contrast failures, missing alt text,
   load-time offenders, console errors.
Give me the list first; after my OK, fix and confirm each item.
```

---

## Notes for Olivia

- **Copy is law.** Every prompt repeats it because AI builders drift back to their training-data marketing voice within 2-3 iterations. When you spot off-voice microcopy, quote rule W1-3 back at the tool.
- **The order matters:** W1 → check → W2 → check → W3 → W4. Do W5 only when Tally/Cal exist, W6 only with a real scorecard. Run W7 before going live and after any big change.
- **Photo:** the single highest-trust element on the page is a good photo of you. Warm daylight, workshop/real-context background beats studio-corporate. Same photo as LinkedIn so the credibility check connects.
- When the site is live, update `04-marketing/LAUNCH-CHECKLIST.md` C3 and put the URL in your LinkedIn featured section + profile.
