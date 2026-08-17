# Research agenda derived from the Zeit AI marketing JD

**Date:** 15 Aug 2026
**Source doc:** [jd-marketing-inbound-brand.md](jd-marketing-inbound-brand.md)
**Framing:** written as account intel for the live Scaile → Zeit AI engagement (day-0 AIV
baseline + `deck/`). Most items below are framing-neutral — they are just "understand Zeit
AI's marketing" — but the *So what* lines are written from the Scaile side.

---

## 0. Why this posting matters at all

The JD is a self-authored admission of the exact gap the day-0 baseline measured:

> "Most customers and hires still come from outbound. Your job is to change that."
> "What we do not have is a brand that carries that story for us."

Baseline says: 0.0% mention, 0.0% citation across 102 AI answers. The JD says: we know,
and we are budgeting €60–120K/yr against it. That is a stated buying trigger with a
stated budget — the strongest sales artifact in this folder, stronger than the chart.

---

## Tier 1 — Cheap, fast, changes the pitch immediately

### 1. Is the site blocked to AI crawlers?
Check `robots.txt` for GPTBot, ClaudeBot, PerplexityBot, Google-Extended, CCBot. Check for
`llms.txt`. Check whether Webflow is serving the content server-side (it does by default —
confirm, don't assume).
**So what:** if they're blocking or under-serving AI crawlers, the 0.0% has a mechanical
cause, and there is a same-day fix to lead the pitch with. If they're wide open, the 0.0%
is purely a content/authority problem and the grounding-page play is the whole answer.

### 2. Full site inventory
Domain (confirm the live one), `sitemap.xml`, indexed page count via `site:`, page types,
blog existence and post cadence, DE vs EN split, `hreflang` setup.
**So what:** the deck's "grounding pages" step needs a page count to be concrete. "You have
9 pages, all English, none quotable" is a slide; "you should do content" is not.

### 3. German-language coverage
The baseline ran 20 **German** BOFU prompts. Does zeit.ai have German pages at all, or is
it English-only with German buyers?
**So what:** if English-only, that single fact explains most of the 0.0% and is the
cheapest, highest-leverage recommendation in the deck.

### 4. Structured data / entity clarity
Organization, Product, FAQPage schema. Is there a page an assistant could cite for "Was ist
Zeit AI?" — founders, funding, customers, verticals, all in one machine-readable place?
**So what:** direct input to the grounding-page standard. Also: the JD itself contains
facts (Oxford Seed Fund, three verticals, $1M ARR) that are *nowhere on the site* if the
site is thin — the JD is better grounding copy than their homepage.

### 5. Are they running Google Ads today?
Google Ads Transparency Center + LinkedIn Ad Library for Zeit AI and for Veezoo, Dot,
Jedox, Celonis.
**So what:** JD says SEA is "yours to own" — implying it barely exists. Confirms whether
Scaile is proposing into a vacuum or against a running account, and gives competitor ad
copy to quote.

---

## Tier 2 — The two new verticals (highest strategic upside)

The JD reveals customers in **agriculture** and **aviation**. Neither was in the prior
research. The 20 tracked prompts are generic Mittelstand/BI — they do not cover these.

### 6. Vertical demand universe: Landwirtschaft + Luftfahrt
German query space for agentic BI / ERP-Auswertung / Datenanalyse in agriculture and
aviation. Volume will be small; contest will be near-zero.
**So what:** the baseline shows Power BI/Tableau/SAP owning 76% of the generic answer set —
unwinnable near-term. Vertical-specific answer sets are probably *uncontested*. This is a
credible "you can be #1 in 90 days" claim, which the generic set cannot support.

### 7. Named customers per vertical
Which manufacturing / agriculture / aviation customers are public and quotable? Logos on
site, case studies, LinkedIn posts, YC profile, press.
**So what:** grounding pages need proof. Also determines whether vertical landing pages can
name a reference or must stay abstract.

### 8. Who already ranks and gets cited in those verticals
The baseline's cited sources were vendor content and listicles: proalpha.com, oneagent.de,
qymatix.de, g2.com. Are there vertical equivalents (agritech / aviation-MRO trade media)?
**So what:** these are the placement and displacement targets — the concrete "where the
citations come from" answer.

---

## Tier 3 — People and buying process

### 9. Deepika, GTM Lead
New name. Described as "your closest partner in this role" — i.e. she owns GTM and will own
the marketing hire.
**So what:** she is almost certainly the buyer or the champion for Scaile, not Leopold.
Research her background, prior stack, whether she's run SEO/SEA before, what she posts.

### 10. Elisa
First-screen contact — recruiting/ops. Lower priority; useful only for org mapping.

### 11. Is the seat empty right now, and for how long?
When was the posting first published? Still live?
**So what:** decides the entire positioning. Seat empty → Scaile is the marketing function
in the interim. Seat filled → Scaile is the engine the new hire operates, and the pitch
must not read as a threat to their mandate. Get this before the meeting.

### 12. Quantify the "organic reach" they claim
Leopold's and Marvin's LinkedIn cadence, follower counts, engagement. Podcasts, panels,
YC-channel appearances.
**So what:** JD says "We already have organic reach, now we push further." If that reach is
founder-LinkedIn only, it is unindexed and uncitable — reach that generates zero AI
visibility. That gap ("your reach doesn't survive into the answer layer") is a sharp line.

---

## Tier 4 — Verify and correct the record

### 13. Oxford Seed Fund
New backer, not previously in the dossier. Confirm, and check ticket size / date.

### 14. "Sequoia Scout" ≠ Sequoia
The prior dossier flagged "Sequoia backing unverified." The JD says **Sequoia Scout** — a
scout-program angel check, materially smaller and different from Sequoia the fund. Identify
the scout if public.
**So what:** corrects a fact already carried in the dossier and the KB files. Worth fixing
in `kb/zeit-ai-company-profile.md` and `kb/zeit-ai-founders-team.md`.

### 15. ARR figure
JD says "$1M+ ARR" (USD); dossier has €1M self-reported. Same claim, different currency,
still self-reported. Note the inconsistency; do not upgrade it to verified.

### 16. Press coverage to date
Gründerszene, Munich Startup, t3n, Handelsblatt, Business Insider DE, YC blog.
**So what:** JD lists press as a channel to push on. Backlink and citation source inventory.

---

## Tier 5 — Channel-specific detail

### 17. Webflow constraints
CMS collections for programmatic/templated landing pages, redirect handling, `hreflang`,
custom code injection limits, page-count limits on their plan.
**So what:** every recommendation has to be shippable in Webflow by one non-engineer. A
plan that assumes Next.js is dead on arrival here.

### 18. Measurement stack
GA4 is named. What else — GSC verified? CRM (HubSpot?)? Is conversion tracking wired to
"qualified meetings," which is the metric the JD explicitly names?
**So what:** JD says SEA is "measured on qualified inbound, not impressions." If there is no
plumbing from form-fill to qualified meeting, that measurement claim is aspirational and
building it is a deliverable Scaile can own.

### 19. Events
Which DACH fairs match the three verticals — Hannover Messe, EMO, Agritechnica, ILA Berlin,
Bits & Pretzels, and the aviation/MRO circuit. Which has Zeit AI actually attended?
**So what:** lower priority for Scaile, but event pages and speaker bios are indexable,
citable assets — the bridge between their brand budget and the answer layer.

### 20. Backlink profile
Who links to zeit.ai today: YC directory, Oxford Seed Fund portfolio page, customer sites,
press, job boards.
**So what:** baseline authority number, and the JD names backlinks as an explicit
responsibility.

---

## Commercial read

- Budget signal: €60–120K/yr for one person to do website + SEO + SEA + content + events.
  That band is the reference price for anything Scaile proposes.
- Timing: a new marketing hire's first 30 days are keyword research and a content map.
  Scaile can hand them that on day one — arriving *with* the demand map, not pitching to
  build one.
- Risk to manage: the hire is explicitly promised "a real path into owning marketing." Any
  proposal that reads as outsourcing their mandate will be resisted by the person who has
  the most influence over it. Position as the engine they operate.

---

## Open question for the user

This agenda assumes the account-intel framing. If the intent is application prep instead,
items 9–12 and the Commercial read swap out for craft-portfolio and interview prep — say
the word and I'll rewrite those sections.
