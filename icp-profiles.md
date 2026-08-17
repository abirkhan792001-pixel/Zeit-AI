# Zeit AI — ICP deep dive

**Date:** 15 Aug 2026
**Method:** reverse-engineered from the actual customer base (8 logos, 3 named testimonials,
4 named references), the 3 published use cases, the delivery model, and the JD's vertical
disclosure — then each customer entity researched independently for size, ownership and
ownership-change history. Nothing here is taken from Zeit AI's own segment language, which
is checked against the evidence in §7.

**Provenance:** [verified] = independent source · [company] = Zeit AI self-reported ·
[inferred] = my read of the pattern, stated as hypothesis.

---

## 1. The one fact that defines this ICP

**Every named testimonial is from the owner or the top of the house — not from a data leader.**

| Customer | Named person | Title |
|---|---|---|
| Kolbenschmidt Pistons Brazil | Claus von Heydebreck | **President** |
| Allgaier Agrarhandel | Karl Allgaier | **Managing Director** (5th-gen family owner) |
| Jetfly | Maxime Bouchard | **Managing Director** (bought the company in 2010) |

Three for three. There is no CDO, no VP Data, no Head of Analytics anywhere in the public
proof. That is not an accident of who agreed to be quoted — it is the structural reality of
the segment. These companies do not have a data function, which is precisely why they buy
an "autonomous data engineer."

**Consequences that flow from this single fact:**

- The economic buyer and the champion are often the *same person*, which is why deals can
  close in ~10 weeks and why a 24-hour pilot works as a sales device.
- The buyer does not know the category vocabulary. They do not search "agentic BI" or
  "natural-language analytics." They search the *symptom*.
- There is no procurement gauntlet, but there is a hard trust gate — the same person who
  signs also personally owns the risk of putting company data into an AI system.
- Nobody internally is defending an existing BI investment. The competitor is Excel and
  the incumbent is inertia, not another vendor.

---

## 2. Segment A — PE-owned industrial carve-outs

**The anchor logo, and the most repeatable trigger in the portfolio.**

**Evidence.** Kolbenschmidt Pistons: ~€700M annual revenue, ~3,650 employees across
Neckarsulm (DE), Marinette (US), Celaya (MX), Nova Odessa (BR), Trmice (CZ), Hiroshima (JP)
plus the KSHP JV in China. Rheinmetall announced the divestment 20 Dec 2023; the sale to
**Comitans Capital AG** — a Munich private equity firm founded in 2020 — closed **1 Apr
2024**. Comitans runs it as a standalone company under the Kolbenschmidt Pistons brand.
[verified]

Zeit AI was founded July 2024 and won "first major customers from the automotive industry"
about 10 weeks after starting [verified, Business Insider DE]. That places the win roughly
**six months into the carve-out.**

**Why this is the sharpest trigger.** A carve-out loses its parent's shared services on a
transition-services-agreement clock. Group BI, group controlling templates, group data
warehouse — all of it either expires or gets expensively re-licensed. The new standalone
entity must produce board-grade monthly reporting for a PE owner, from ERP data it now owns
but has no team to query. It has a deadline, a budget, and no internal option. That is the
cleanest possible fit for forward-deployed delivery in weeks.

**Note the entity that actually bought:** *Kolbenschmidt Pistons **Brazil***, with a
President as the reference — one plant/region of a multi-site group, not group HQ. This is a
land-and-expand motion inside a carve-out, not a group-level enterprise sale. [verified]

- **Firmographics:** €100M–€1B revenue, 500–5,000 employees, multi-entity, multi-country,
  SAP or mixed ERP estate, 12–36 months post-separation.
- **Buying committee:** PE operating partner (pressure) → entity President/MD (signs) →
  Head of Controlling (champion) → group IT (blocker, often skeletal post-carve-out).
- **In their words:** "Wir müssen das Konzernreporting ersetzen, aber wir haben das Team
  dafür nicht mehr."
- **Channel implication [inferred]:** Comitans is Munich-based, like Zeit AI, and holds a
  portfolio. One PE relationship is a repeatable route to many portfolio companies with an
  identical trigger. Whether Zeit AI has actually worked this channel is **unverified** and
  is the single highest-value question in this document.

---

## 3. Segment B — Family-owned trading and distribution Mittelstand

**The truest "Mittelstand" segment and the one the positioning is actually written for.**

**Evidence.** Allgaier Agrarhandel GmbH & Co. KG, Allmendingen (Alb-Donau-Kreis): founded
**1858**, still family-owned and run by the Allgaier family in the **fifth generation**;
~€30M balance sheet total in 2024 (+17.3% YoY); six locations across southern Germany
(Allmendingen, Bondorf, Gussenstadt, Suppingen, Plochingen, Stuttgart); seeds, fertiliser,
crop protection, animal feed, agricultural produce. [verified] "Raiffeisen" on the logo wall
is plausibly the same agricultural-trading cluster, but the entity is **not identified** —
do not assert it.

**Why they buy.** Trading and distribution businesses live on thin, volatile commodity
margins across many SKUs and locations. Working capital is tied up in inventory; purchasing
price consistency across sites is invisible; the owner wants to know which products actually
made money. Zeit AI's three published use cases — controlling cockpit, overstock/understock
detection, procurement spend cube — map onto this business model almost exactly. The
homepage claim "90 unprofitable products uncovered in one month" is a distribution claim.

- **Firmographics:** €20M–€150M revenue, 50–400 employees, multi-site, family-owned,
  generational management, ERP present but under-exploited, zero data staff.
- **Buying committee:** owner-MD (buyer + champion, same person) → controller/bookkeeper
  (user) → the *Steuerberater* or long-standing Systemhaus (quiet influencer, often the real
  blocker because it threatens their scope).
- **Trigger:** generational handover, a new ERP that nobody can get numbers out of, a bad
  margin year, or a bank/lender asking for better reporting.
- **In their words:** "Ich will einmal im Monat sehen, welche Artikel wirklich Geld
  verdienen — ohne dass jemand drei Tage in Excel sitzt."
- **Risk:** longest trust cycle of any segment, lowest ACV, and the most sensitive to
  "unsere Daten gehen in eine KI" objections. The GDPR / German-hosting / no-model-training
  stack exists for this segment.

---

## 4. Segment C — Owner-operated, asset-heavy service operators

**Evidence.** Jetfly (Luxembourg): ~300 staff including ~150 pilots, a fleet of ~60 Pilatus
aircraft (48 PC-12, 12 PC-24 — the largest such fleet in the world), operating on behalf of
~300 fractional co-owners. Incorporated 1999; **bought in 2010 by Cédric Lescop and Maxime
Bouchard**, the latter being the named reference. [verified]

**Why they buy.** The economics here are genuinely hard: utilisation per tail, cost
allocation across fractional owners, maintenance scheduling, crew rostering, fuel and
positioning. It is not a factory and not a trading book — it is a shared-asset P&L that
Excel models badly. The testimonial itself points at this: appreciation for a
"user-oriented approach" against work that "can quickly become very theoretical and
complex."

- **Firmographics:** €50M–€300M revenue, 150–800 employees, asset-heavy, operationally
  complex, owner-operator or founder-bought, ERP plus several specialist operational systems
  that do not talk to each other.
- **Buying committee:** owner-MD (buyer) → operations director (champion) → finance
  (validator).
- **Trigger:** growth outrunning the spreadsheet; a new investor or lender; an operational
  shock (fuel, maintenance, capacity) that nobody can explain quickly.
- **Adjacent expansion:** MRO, fleet logistics, shipping, rental/leasing, energy services,
  multi-site healthcare — same shape, same pain.

---

## 5. Segment D — Consultancy and investor-adjacent (a channel, not a market)

RISE (financial consultancy, named on the YC profile) and **Stern Stewart** (Munich
management consultancy) are on the customer list. Stern Stewart's venture arm, **Stern
Stewart Ventures, is also an investor in Zeit AI** [verified] — so it is simultaneously
logo, customer and shareholder.

There is also a visible **Swiss cluster**: Capomondo SA (Geneva / Wollerau — services to a
restaurant group: management systems, accounting, logistics) and "SwissGroup"
(**unidentified**), alongside Geneva-based investor ACE Ventures on the cap table.

**Read this as distribution, not demand [inferred].** Consultancies do not represent a
scalable product segment; they represent referral routes into their own client bases, and
the geographic clustering around investor cities (Munich, Geneva) suggests much of the
early logo wall is investor-referred rather than inbound- or outbound-won. That is normal at
this stage and it is exactly the dependency the JD is trying to break.

**Handle with care in the pitch:** never cite Stern Stewart as independent third-party proof.
It is an investor.

**Unidentified and not to be asserted:** ATS, SwissGroup, Raiffeisen.

---

## 6. Anti-ICP — who to actively disqualify

| Disqualifier | Why |
|---|---|
| Already runs a modern data stack (Snowflake/dbt/Looker) | That is Dot/GetDot's ICP; they self-serve and don't need FDEs |
| Has a real BI/data team | The "autonomous data engineer" pitch inverts into a threat to their jobs |
| Under ~€10–20M revenue | Cannot carry a mid-five- to six-figure ACV with a 6-month engagement |
| Cloud-native digital business | No legacy ERP mess — the wedge disappears |
| Mid-S/4HANA migration | Budget and attention frozen; IT will say "after go-live" |
| Hard on-prem mandate | Tracked prompt #18 exists for this segment, but Zeit AI's public posture is EU-hosted SaaS, not on-prem |

---

## 7. The positioning tension worth naming

Zeit AI's own language is "**the autonomous data engineer for the European mid-market**."
The IfM/EU definition of Mittelstand tops out around €50M revenue and 500 employees.

But the anchor logo, Kolbenschmidt Pistons, is **~€700M revenue and ~3,650 employees** —
roughly 14× the revenue ceiling of the segment the homepage claims. Jetfly at ~300 staff and
Allgaier at ~€30M do fit. So the real customer base spans from a €30M family trader to a
€700M PE-owned industrial group.

Two possible readings, and they lead to opposite marketing:

1. **The positioning under-sells.** The best-fitting, fastest-closing, highest-ACV
   customer is the carve-out / PE-owned mid-large industrial — and "mid-market" language
   actively repels them. Ex-Palantir founders selling a Palantir-shaped delivery model to
   €700M industrials is a coherent, differentiated story.
2. **Kolbenschmidt is unrepresentative** — one plant-level deal in Brazil that flatters the
   logo wall, while the repeatable business is genuinely €20–150M German Mittelstand.

Which one is true determines keyword strategy, ad targeting, ACV assumptions and event
selection. **It cannot be resolved from public data** — it needs one question to Deepika or
Leopold: *"Of your last ten deals, what was the revenue band and who signed?"* That is the
highest-value question to walk into the meeting with.

---

## 8. Cross-segment buying committee

| Role | Who | What they need |
|---|---|---|
| **Economic buyer** | Geschäftsführer / MD / President / owner. In PE-owned: entity head under operating-partner pressure | Proof it works on *their* data, fast. The 24h pilot is aimed here. |
| **Champion** | Head of Controlling / Leiter Controlling | Relief from the monthly Excel close. Feels the pain daily, has no budget authority. |
| **Users** | Controller, analyst, Einkäufer, Disponent | Answers without SQL. Will quietly resist if it looks like surveillance of their numbers. |
| **Blocker** | IT lead, Datenschutzbeauftragter, and in larger German firms the Betriebsrat | GDPR, German hosting, no model training, roles & permissions. |
| **Shadow influencer** | Steuerberater / Wirtschaftsprüfer, incumbent Systemhaus, PE operating partner | The Systemhaus loses scope if this lands — expect quiet opposition. |

---

## 9. Trigger events, ranked by sharpness

1. **Carve-out or divestment; TSA expiry** — hard deadline, budget attached, no internal option. *(Kolbenschmidt/Comitans)*
2. **New PE or family-office owner** demanding monthly reporting discipline.
3. **Open data-engineer req that cannot be filled** — tracked prompt #21 is literally this decision.
4. **ERP migration just completed** — data is in the new system and nobody can get it out.
5. **Generational handover** in a family firm — incoming generation will not run the business on the founder's spreadsheets.
6. **Margin shock or cost program** — the €450K margin-risk and €700K inventory claims are the pitch here.
7. **A failed BI project** — Power BI was bought, nobody adopted it, the consultancy left.

---

## 10. What this changes for the Scaile engagement

The 20 tracked German BOFU prompts encode **one** buyer: a generic Mittelstand software
evaluator who already knows the category. Against the ICP evidence, three gaps:

1. **No trigger-state language.** Nothing in the set covers carve-out/TSA reporting,
   post-ERP-migration, or PE reporting requirements. These are the sharpest-intent moments
   and almost certainly an *uncontested* answer set — Power BI and Tableau do not own
   "Reporting nach Carve-out aufbauen."
2. **No vertical cuts.** Agriculture (Agrarhandel, Warengenossenschaft) and aviation (fleet
   ops, MRO) are absent, despite being two of the three verticals the JD names and two of the
   three named testimonials. The generic BI answer set is 76% owned by Power BI/Tableau/SAP
   and is unwinnable near-term; vertical answer sets are thin.
3. **Wrong register.** The prompts are written in software-buyer voice ("Welche KI-Software
   kann…"). The person who actually signs is a Geschäftsführer who asks the symptom:
   "Warum stimmen unsere Zahlen aus SAP nicht?" / "Wie bekomme ich endlich verlässliche
   Monatszahlen ohne eigenes Team?" Worth testing both registers before the next baseline —
   they may retrieve entirely different answer sets.

Prompt #15 ("Ad-hoc-Datenanfragen der Geschäftsführung automatisieren, ohne ein eigenes
BI-Team aufzubauen") is the one that already speaks in the right voice. It is the template.

---

## 11. Corrections required to the existing KB

**`kb/zeit-ai-customers-proof.md` is factually stale and is currently uploaded as AI
grounding material.** It states:

> Kolbenschmidt Pistons Brazil (automotive supplier, **Rheinmetall group**)

Rheinmetall divested the small-bore piston business to Comitans Capital AG; the sale closed
**1 April 2024** [verified]. Kolbenschmidt Pistons has not been Rheinmetall group since. A
grounding file whose job is to feed correct facts to LLMs is currently feeding a wrong one.
Fix to: *"Kolbenschmidt Pistons Brazil — small-bore piston manufacturer, carved out of
Rheinmetall and owned by Comitans Capital AG (Munich PE) since April 2024; ~€700M revenue,
~3,650 employees group-wide."*

The same file's vertical line should also gain **aviation as a named, testimonial-backed
vertical** (Jetfly), rather than sitting under "company-claimed additionally."

---

## 12. Open questions to resolve before the meeting

1. **Of the last ten deals — revenue band, industry, and who signed?** Resolves §7 and
   everything downstream. Ask Deepika.
2. **Is the Comitans/PE portfolio channel real or a coincidence?** If real, it is the most
   scalable motion Zeit AI has and it is entirely absent from the inbound plan.
3. **Is aviation one customer or a segment?** Jetfly is impressive but may be n=1.
4. **What is the actual ACV and sales cycle** by segment? Drives whether inbound or events
   is the better spend.
5. **Who are ATS, SwissGroup and Raiffeisen?** Three of eight logos are unidentified, which
   is a third of the public proof.
6. **Does the German site version have real localised content**, or is it a partial
   translation? The buyer in Segments A and B is German-speaking; the AIV baseline was run
   in German.
