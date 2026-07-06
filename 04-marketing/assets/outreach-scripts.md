# Outreach Scripts

All follow LEADS-5 (A-C-A: Acknowledge → Compliment → Ask; give before any pitch) and MSG-2 (one clear next step). Personalize line 1 always — the rest may be template. Track every send in the outreach sheet (M3).

## 1. Warm outreach — direct contact (NL, WhatsApp/SMS/DM register)

> Dag {{VOORNAAM}}! {{Acknowledge: iets echts — "zag je foto's van de nieuwbouwwerf, straf werk" / "lang geleden, sinds {{context}}!"}}. Ik ben gestart als AI-coach voor installatie- en servicebedrijven — ik help zaakvoerders zo'n 10 uur per week aan administratie terug te winnen. Nu vraag ik me af: {{Ask}} ken jij in je omgeving iemand met zo'n zaak die verzuipt in offertes, werkbonnen of facturatie? Ik doe de eerste analyse gratis — ook gewoon omdat ik nu cases opbouw.

**Variant als de contactpersoon zélf ICP is:** … Ik doe momenteel bij een handvol bedrijven een gratis AI-Scan (10 min invullen, 20 min debrief) — zin dat ik er bij jou eens naar kijk? Eerlijk antwoord gegarandeerd, ook als het "niets voor jou" is.

**Follow-up (dag 4, één keer):** Dag {{VOORNAAM}}, korte opvolger op mijn berichtje — geen probleem als het niets is, maar als je één iemand weet die avonden aan paperassen verliest, maak je die (en mij) er blij mee. 🙂

## 2. Warm outreach — corporate route (EN/FR, LinkedIn/e-mail, ICP-B)

> Hi {{NAME}}, {{Acknowledge: their role/post/company move}}. I've spent the past months building a complete methodology for AI integration in businesses — not the tooling side, but the part everyone skips: how the organigram, roles and processes must change to actually capture the value (task-level human/automation/agent allocation, change management, EU AI Act compliance). Before I take it further into the market, I want it stress-tested by people who live this at scale. Could I get 30 minutes of your most brutal feedback? Nothing to sell — I genuinely want the holes shot in it.

*Why this works (Enns/POS-3): experts asked for judgment become buyers or referrers without ever being pitched. Follow up once after 5 days with one concrete artifact attached (e.g., the RACI-A explainer) — give first.*

## 3. Cold outreach — SME 3-touch e-mail sequence (NL)

**Touch 1 (dag 0) — Onderwerp: vraagje over {{BEDRIJF}}**
> Dag {{VOORNAAM}}, ik kwam {{BEDRIJF}} tegen via {{bron: reviews/website/vakbeurs}} — {{Compliment: specifiek en echt, bv. "knappe reviews over jullie stiptheid, zeldzaam in de sector"}}. Ik help installatie- en servicebedrijven van jullie grootte gemiddeld 10 uur per week aan administratie terug te winnen (offertes, werkbonnen, facturatie-opvolging) met slimme automatisering — zonder dat er iemand "computermens" moet worden. Mag ik je onze gratis AI-Scan sturen? 12 vragen, 10 minuten, en je weet meteen waar bij jullie de uren lekken. Groeten, {{NAAM}}

**Touch 2 (dag 4) — waarde geven, niet duwen**
> Dag {{VOORNAAM}}, beloofd is beloofd — hierbij alvast één idee dat ik deze maand bij een {{sector}}bedrijf bouwde: techniekers spreken hun werkbon in als spraakmemo onderweg naar huis; het systeem maakt er automatisch een werkbon + conceptfactuur van. Resultaat: ±40 minuten per technieker per dag. Zoiets staat er op een namiddag. Als je wil weten wat er bij {{BEDRIJF}} als eerste uit zou springen: de scan-link staat hieronder. {{LINK}}

**Touch 3 (dag 10) — de nette afsluiter**
> Dag {{VOORNAAM}}, laatste berichtje van mij hierover. Twee opties: (1) doe de gratis scan wanneer het jou past ({{LINK}}), of (2) laat me weten dat het niets voor jullie is, dan hou ik ermee op — ook goed. In beide gevallen: veel succes met het seizoen!

*Volume per M3: 5/dag vanaf week 4. Bouw voor jezelf een agent die touch-1-personalisaties voorstelt vanuit website/reviews — en maak daar een bouwlog-post over (M4 pijler 1).*

**Sniper upgrade:** voor doelbedrijven die de moeite waard zijn, vervang touch 1-2 door de **AI Strategy Preview** (gepersonaliseerd document vanuit hun URL) — pipeline, verzendmail en opvolging in `ai-strategy-preview.md`. Hogere kost per contact, veel hogere respons; ideaal ook als opvolger na een event-gesprek of partner-intro.

## 4. Partner pitch — accountants & software-resellers (NL)

> Dag {{NAAM}}, jullie zien bij {{klanten in de bouw-/installatiesector}} dagelijks wat late facturatie en losse administratie kosten. Ik ben AI-integratiecoach voor precies die sector: ik bouw in 6 weken werkende automatiseringen (werkbon→factuur, offerte-opvolging, betalingsherinneringen) mét het team erbij. Voorstel: ik geef jullie cliënteel een gratis sessie "10 uur per week terugwinnen met AI" — jullie leveren de zaal en de uitnodiging, ik de inhoud. Jullie cliënten krijgen waarde, jullie de eer, ik de kennismakingen. Eens bellen?

*Deal-opties oplopend: gratis sessies → wederzijdse doorverwijzing → referral fee ({{%}}) → co-branded scan. Start altijd bij gratis waarde.*

## 5. Federation / event talk pitch (NL)

> Dag {{NAAM}}, voor jullie {{afdeling/event}} bied ik een sessie aan van 45 minuten: "10 uur per week terugwinnen met AI — wat écht werkt in een installatiebedrijf". Geen productverkoop: concrete voorbeelden met cijfers, wat leden vandaag zelf kunnen doen, en de valkuilen. Leden vullen ter plaatse de AI-Scan in en krijgen hun score direct mee. Ik doe dit kosteloos; ik bouw mijn praktijk op in de sector en dit is mijn manier om te geven vóór ik iets vraag.

## 6. The referral ask (at S5 results session — the flywheel, BIZ-3)

> "Je hebt nu je cijfers gezien. Twee vragen als afsluiter: (1) mag ik dit — anoniem of met naam, jij kiest — als case gebruiken? (2) Welke twee collega-zaakvoerders uit je netwerk zouden dit ook moeten zien? Een warme intro van jou is voor hen waardevoller dan eender welke reclame van mij — en de eerste analyse doe ik bij hen sowieso gratis."

---

## Regeneration prompt

```
Using M1 (LEADS-5 A-C-A, POS-3) and M2's positioning for {{NICHE}}, rewrite
all six script families for that niche in {{LANGUAGE}}: warm-direct, warm-
corporate (keep the feedback-ask mechanic), cold 3-touch (touch 2 must GIVE
a real, niche-specific build example with numbers), partner pitch (pick the
niche's 2 most trusted advisor types), event/federation pitch (name the
niche's real federations), and the S5 referral ask. Register: how these
owners actually text/mail; zero corporate speak; every first line
personalized; one ask per message.
```
