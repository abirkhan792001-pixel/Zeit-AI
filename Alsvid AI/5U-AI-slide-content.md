# 5U AI — Internal pitch deck: slide-by-slide content

**Status:** draft v1, ready for review. Not yet built as a deck file.
**Source:** [5U-AI-pitch-deck-brief.md](5U-AI-pitch-deck-brief.md) (handoff summary of the planning
conversation). The five underlying documents — ICP report, research dossier, MECE strategy,
90-day roadmap, existing strategy deck HTML, IBM analyst brief — were **not** available when this
was drafted. Every number below traces to the brief; §9 lists the numbers the deck still needs
from the source docs before it can be built.
**Audience:** leadership, internal. **Length:** 7 slides + cover + close + appendix.
**Structure:** BLUF / pyramid. Act 1 = slide 1 (the decision). Act 2 = slides 2–4 (the proof).
Act 3 = slides 5–7 (the execution).

---

## 0. Read this before drafting anything into a deck file

Three things are unresolved and they change the content, not just the polish.

**Naming.** This work sits in a folder called `Alsvid AI`; the brief and all six source documents
say `5U AI`. Every headline below uses **5U AI**, because that is what the source says. If Alsvid
is the real name, a rename is a find-and-replace — but confirm which is which before the deck goes
in front of leadership, because getting the company's own name wrong on slide 1 costs more than
every other risk in this document combined.

**Two competitor counts.** The brief cites a *16-vendor* GTM synthesis (§2, §6) and a *27-vendor*
pricing scan (§3, "only 2 of 27 vendors publish pricing"). These are probably two different studies
with two different scopes, which is fine — but if both numbers appear on slides, someone will ask.
Decide whether to cite one, both-with-scope, or neither.

**Currency mix.** Funding is stated in dollars ($3.2M pre-seed); every operating number is euros.
Keep the deck in euros throughout and put the dollar figure only where the funding round is
literally being described.

---

## Cover (not counted)

> **5U AI — the beachhead won't pay for itself**
> What we recommend, why, and what we need approved
> [Date] · Internal · Leadership review

Deliberately not a neutral title. The cover already carries the argument, so the room is oriented
before slide 1 loads.

---

## Slide 1 — The finding and the ask

**Headline:** *Our beachhead cannot reach break-even. The combined strategy clears it by 80%.*

**Assertion (the one line said out loud):** Today's plan tops out at €1.56m ARR and burns €0.89m a
year. Break-even is €2.92m. We are asking you to fund the combined strategy, S5, which reaches
€5.26m and turns €1.52m EBITDA positive.

**On-slide elements**

| | S0 — today's plan | S5 — recommendation |
|---|---|---|
| Y3 ARR | €1.56m | **€5.26m** |
| Y3 EBITDA | −€0.89m | **+€1.52m** |
| Y3 cash | [needed] | **+€3.43m** |

- A single horizontal **break-even line at €2.92m ARR** drawn across the comparison. S0 sits below
  it, S5 above. This is the whole deck in one graphic device — reuse the same line on slide 3.
- **The ask, stated here, not held back:** approve €66.5k of 90-day spend, [N] hiring reqs, and
  publication of pricing. Detail on slide 7.

**Speaker notes (~90s).** "I'm going to give you the conclusion first and spend the rest of the
time defending it. Our current plan does not get us to break-even — not slowly, not eventually.
It structurally cannot, and I'll show you why on the next slide. The combined strategy does, with
margin, and it stays positive under stress. Everything after this is proof, not build-up."

**Anticipated challenge.** *"Isn't S5 just 'do everything at once'?"* — No. It is four levers with
staggered start dates and a defined kill gate each. Slide 7 shows exactly when each one gets shut
down if it misses. We are asking to start four things, not to commit to finishing four things.

---

## Slide 2 — Why the ceiling is so low

**Headline:** *The work is worth €3.4bn a year. Today's ICP and pricing can reach €117m of it.*

**Assertion:** The constraint is not the product and not demand — it is who we sell to and what we
charge. Two numbers say the same thing at two zoom levels.

**On-slide elements — two stacked blocks**

**Block A — zoom out.** €3.4bn/yr labour-value ceiling vs €117m/yr reachable at today's ICP and
pricing. **29x gap.** Framed as *value of the work being done manually today*, not as a TAM
estimate — this is the more defensible framing and it is worth saying so on the slide.

**Block B — zoom in.** Break-even needs **~30% penetration of just 213 beachhead companies**.
That is roughly **64 accounts** [derived: 30% × 213]. Winning three of every ten companies in the
segment, and *still* only arriving at zero.

**Visual.** Two horizontal bars on a shared log scale (€117m against €3.4bn), then the 213/64
figure as a dot grid — 213 dots, 64 filled. The dot grid is what makes it land: leadership can see
that "30% penetration" means personally closing 64 named companies.

**Speaker notes.** The two blocks are not two arguments, they are one argument seen from opposite
ends. Zoomed out, we are addressing a sliver of the value. Zoomed in, even *dominating* our
beachhead leaves us at zero. That is what "the ICP is the binding constraint" means concretely.

**Supporting frame for the notes, not the slide** [derived, confirm before saying]: at the stated
guardrail of 1 FDE ≈ 10 accounts, 64 accounts implies ~6–7 FDEs carrying a book that breaks even
at best. That is the mechanism behind S0's −€0.89m — the cost base scales with the account count
at roughly the rate revenue does.

**Anticipated challenge.** *"Can't we just raise prices inside the beachhead?"* — That is S2, and
it is in the plan. It is not sufficient alone; slide 3 shows no single lever crosses the line.

---

## Slide 3 — The scenario comparison

**Headline:** *No single lever reaches break-even. The combination clears it.*

**Assertion:** We modelled six scenarios independently. Five fail. The finding is not "S5 is best,"
it is "S5 is the only one that works" — a much stronger claim, and the reason the ask is for all
four levers rather than the cheapest one.

**On-slide elements**

- **Primary visual: paired bars, S0 through S5 on the x-axis** — Y3 ARR and Y3 EBITDA per scenario.
- **The €2.92m break-even line** carried over from slide 1, drawn across the ARR series. Only S5
  crosses it. Do not annotate every bar; let the line do the work.
- **One annotation block, bottom-right:** *"S5 stays EBITDA-positive under every single shock we
  modelled — price, demand, churn, capacity. Only a simultaneous four-way shock pushes it negative,
  to −€270k."* Summary line only; the 6×6 stress grid is appendix.

**Chart notes.** Order the x-axis S0→S5 as scenario identity, not by size — the story is that the
line is only crossed at the end. EBITDA needs a zero baseline visible, since the sign change from
negative to positive is the point. Palette and type get matched to `5U-AI-Strategy-Deck.html` at
build time.

> **⚠ Blocking data gap.** The brief gives Y3 figures for **S0 and S5 only**. S1, S2, S3 and S4 ARR
> and EBITDA are needed from `5U-AI-MECE-Strategy.docx` before this chart can be drawn. This is the
> single most persuasive slide in the deck and it cannot be built from the summary alone.

**Speaker notes.** Resist walking through all six. Point at the line, point at the one bar that
crosses it, then go to the stress-test annotation. The audience will ask about a specific scenario
if they care about it.

**Anticipated challenge.** *"What if only two of the four levers work?"* — Honest answer: we land
between S0 and S5, and the gate structure on slide 7 tells us which two by day 90, while the spend
is still €66.5k. That is precisely why the gates exist.

---

## Slide 4 — Why now

*(The slide expanded in §5 of the brief. Framing recommendation below — this was the open question.)*

**Recommended framing.** Lead with **the closing window**, not with the whitespace gap. Both are
true, but the whitespace argument ("competitors haven't built a partner channel") is the *reason S1
works*, which makes it the natural bridge into slide 5 rather than the headline here. Leading with
the window also answers the harder question — *why not next year* — which is the actual objection
in the room. So: window opens the slide, whitespace closes it and hands over.

**Headline:** *The buyers haven't committed yet — and the sellers just showed up.*

**On-slide elements — two stacked evidence blocks**

**Block A — top-down: demand is budgeted but not yet committed.**
**89% vs 19%.** 89% of executives say gen AI will be part of their automation investment; only 19%
call it critically important. Attribution on the slide, verbatim: *"IBM's own vendor deck, aimed at
converting Fortune 500 supply-chain officers."*

Read: a market of budget-holders who have not yet chosen. That is the window. It does not stay open
once 19% becomes 50%.

> **Credibility guardrails — carry into the build.**
> - **Do not use** the "34% more revenue growth / 326% more profitability" figures. They are a
>   2017–2020 pre-gen-AI correlation and the analyst brief flags them as the weakest claim in the
>   source. Using them hands a sharp audience a reason to distrust everything else on the slide.
> - **Frame IBM as vendor material, never as neutral research** — 6 of 9 footnotes in the source
>   deck are IBM's own commissioned surveys. "Even IBM's own sales material shows…" is *more*
>   persuasive than a false claim of independence, and it survives being challenged.

**Block B — bottom-up: capital is arriving in this exact category, now.**
- **5U AI** — $3.2M pre-seed, 28 Jul 2026, led by Emerge Capital.
- **Willidrop** — Munich, out of stealth 30 Jul 2026, agent-based OS for vehicle logistics, round
  closed, amount undisclosed. Same city, same week, adjacent vertical.
- **The YC cohort, same thesis from seven angles** — SpaceFlow (managed runtime for supply-chain
  agents), Lighthouz AI (AP/AR and collections for freight brokers), Derya (AI-native logistics
  office), Haladir (decisional layer over WMS/TMS/OMS), Peer, FleetWorks, Lanesurf.

Read: nobody has won this yet, and the number of people trying doubled in a quarter.

**Bridge line into slide 5 (bottom of slide, one line).** *"And the lane nobody has taken is the one
we're already built for: CargoWise and Timocom integrations shipped, no partner channel on top of
them — while 2 of 27 vendors publish pricing at all."*

**Visual.** Block A is one oversized stat pair (89% / 19%) with the gap between them made visible —
the whole point is the distance, so render it as distance, not as two numbers side by side. Block B
is a dated timeline strip across a single quarter, so the density of activity reads at a glance.

**Anticipated challenge.** *"If seven YC companies are doing this, aren't we late?"* — They are
doing adjacent things in other geographies and other modes. None of them has DACH road plus air
plus a partner channel on CargoWise and Timocom. Being one of eight in a category that did not
exist last year is early; the risk is being one of eighty next year.

---

## Slide 5 — The four levers

**Headline:** *Four levers, sequenced — not four bets placed at once.*

**Assertion:** S5 is MECE by construction: each lever touches a different constraint, so they add
rather than overlap.

**On-slide elements — four blocks, each: lever → mechanism → what it unlocks**

| Lever | Mechanism | What it unlocks |
|---|---|---|
| **S1 — Partner channel** | Distribution through the CargoWise / Timocom integrations we have already built | Reach beyond the 213 without adding direct sales headcount |
| **S2 — Pricing and ACV** | Publish pricing; expand ACV against automation rate | More revenue per account, and the DACH price anchor |
| **S3 — Self-serve tail** *(gated)* | Low-touch entry for the long tail of the 1,479 full ICP | Volume the FDE model cannot physically serve |
| **S4 — Road freight, via Timocom** *(pilot)* | New mode, existing integration | A second market of comparable size to the beachhead |

**Visual.** Four lanes converging into one ARR bar. Keep the timeline out of this slide — slides 6
and 7 own sequencing, and repeating it here dilutes both.

**Speaker notes.** The word to land is *MECE*: each lever attacks a distinct constraint — reach,
price, capacity, market. That is why they sum instead of cannibalising, and it is why the modelled
combination beats the sum of the parts' individual scenarios.

**Anticipated challenge.** *"Why is self-serve gated and road only a pilot?"* — Both consume
engineering rather than sales, both are reversible, and neither is needed for the first €2.92m.
They are sequenced late deliberately; the gates on slide 7 say when we commit.

---

## Slide 6 — 90 days, the budget, and the guardrail

**Headline:** *€66.5k and 90 days to find out — about 2% of runway.*

**Assertion:** The decision in front of you is not "spend €3m on a growth strategy." It is "spend
2% of runway to learn which of the four levers is real."

**On-slide elements**

- **Workstream-at-a-glance table** — one row per workstream, columns: start, owner, day-90 output.
  Roll-up level only; the week-by-week plan and the RACI are appendix.
- **The budget, framed as a share:** €66.5k ≈ **2% of runway**. Percentage first, absolute second —
  the ratio is the argument.
- **The capacity guardrail, stated as a hard rule:** **1 FDE ≈ 10 accounts.** This is the constraint
  that makes S1 and S3 necessary rather than optional — direct-sales growth is capped by hiring
  speed, and both levers add accounts without adding FDEs proportionally.

> **Data gap.** The per-workstream breakdown of the €66.5k, the owners, and the day-90 outputs are
> in `5U-AI-90-Day-Roadmap.docx`. Only the total is in the brief.

**Speaker notes.** The guardrail is doing quiet work here: it pre-empts "why not just hire more
AEs" without the slide having to argue against it.

---

## Slide 7 — Gates, kill criteria, and the ask

**Headline:** *Every lever has a date where we scale it or kill it.*

**Assertion:** You are not approving a strategy that runs unsupervised for three years. You are
approving four experiments with pre-committed review dates and pre-agreed thresholds.

**On-slide elements**

**Gate table**

| Workstream | Gate | Scale if | Kill if |
|---|---|---|---|
| S1 — Partner channel | Q+2 | [threshold needed] | [threshold needed] |
| S2 — Pricing | Q+2 | [threshold needed] | [threshold needed] |
| S4 — Road freight | Q+3 | [threshold needed] | [threshold needed] |
| S3 — Self-serve | Q+4 | [threshold needed] | [threshold needed] |

> **Data gap.** Gate *timings* are in the brief; the scale/kill *thresholds* are in
> `5U-AI-MECE-Strategy.docx`. The table is not worth showing with the thresholds blank — it is the
> thresholds that make the slide land.

**The ask — three items, draft wording, needs your confirmation**

1. **Budget.** Sign off €66.5k of 90-day spend across the four workstreams (~2% of runway).
2. **Hiring.** Approve [N] reqs — [roles]. *Not derivable from the brief. The 1 FDE ≈ 10 accounts
   guardrail sets the shape of this ask, but the actual number has to come from the roadmap's
   headcount plan. Do not let this go on a slide as a guess.*
3. **Pricing.** Approve publishing pricing publicly, accepting that this sets the DACH anchor and
   is difficult to reverse. *(Only 2 of 27 vendors publish. First mover sets the reference point;
   the flip side is that competitors get to price against us.)*

**Speaker notes.** Close on control, not enthusiasm. The last sentence of the deck should be the
date of the first gate, not a vision statement.

**Anticipated challenge.** *"What happens at Q+2 if the partner channel is ambiguous?"* — Worth
pre-agreeing in the room: ambiguous defaults to kill, or ambiguous defaults to one more quarter.
Decide this before presenting, because it will be asked and an unprepared answer undoes the slide.

---

## Closing slide (not counted)

Not a thank-you. Put the **first gate date** and the **three ask items** on screen and leave them
up through Q&A — the room should be looking at the decision while discussing it.

---

## 8. Appendix (build these as backup, do not present)

Per §6 of the brief, cut from the main deck but kept ready:

1. Company/product origin — founders, funding round narrative. *(Audience knows it.)*
2. Full 16-vendor competitor grid. *(Synthesis bullets carry the insight; grid is for challenge.)*
3. Week-by-week 90-day roadmap and the RACI table.
4. Full pricing mechanics — hybrid model, ramp-against-automation-rate, discount guardrails.
5. Full stress-test 6×6 grid. *(Slide 3 carries the one-line summary.)*
6. Full event calendar. *(One line in the main deck: 3 events, pre-booked meetings.)*
7. Diligence risk list — DPA hosting contradiction, no SOC 2, 2-year lock-in, Clause 10.3 data-use
   ambiguity. **Recommend keeping this one.** It is a "fix before scaling" list rather than a growth
   argument, but if anyone in the room has seen the dossier they will ask, and having it ready reads
   as candour rather than omission.
8. Market sizing, both methods, with assumptions.

Note that two urgency-relevant fragments were deliberately promoted *out* of the diligence appendix
into slide 4's argument: Nexcade potentially publishing pricing first, and cargo.one's distribution
(28,000 forwarders) as the biggest structural risk. If slide 4 runs long, cargo.one is the cut —
it is the more alarming fact but the less actionable one.

---

## 9. Numbers ledger

Every figure used above, so the deck can be fact-checked in one pass against the source docs.

| Figure | Value | Where it appears | Source |
|---|---|---|---|
| Break-even ARR | €2.92m | 1, 2, 3 | brief §3 |
| S0 Y3 ARR | €1.56m | 1, 3 | brief §3 |
| S0 Y3 EBITDA | −€0.89m | 1, 3 | brief §3 |
| S5 Y3 ARR | €5.26m | 1, 3 | brief §3 |
| S5 Y3 EBITDA | +€1.52m | 1, 3 | brief §3 |
| S5 Y3 cash | +€3.43m | 1 | brief §3 |
| Combined-shock EBITDA | −€270k | 3 | brief §3 |
| Labour-value ceiling | €3.4bn/yr | 2 | brief §3 |
| Reachable revenue today | €117m/yr | 2 | brief §3 |
| Gap multiple | 29x | 2 | brief §3 |
| Beachhead companies | ~213 (DACH + Benelux) | 2 | brief §3 |
| Full ICP | ~1,479 | 5 | brief §2 |
| Break-even penetration | ~30% of 213 | 2 | brief §4 |
| Accounts implied | ~64 | 2 | **derived** (30% × 213) |
| FDEs implied at break-even | ~6–7 | 2 (notes only) | **derived** (64 ÷ 10) |
| Capacity guardrail | 1 FDE ≈ 10 accounts | 6 | brief §3 |
| 90-day budget | ~€66.5k | 1, 6, 7 | brief §2 |
| Budget as share of runway | ~2% | 6, 7 | brief §4 |
| IBM intent | 89% | 4 | brief §5 (IBM vendor deck) |
| IBM conviction | 19% | 4 | brief §5 (IBM vendor deck) |
| Vendors publishing pricing | 2 of 27 | 4, 7 | brief §3 |
| Competitor grid size | 16 vendors | appendix | brief §2, §6 |
| cargo.one distribution | 28,000 forwarders | 4 (or cut) | brief §3 |
| 5U AI pre-seed | $3.2M, 28 Jul 2026, Emerge Capital | 4 | brief §2 |
| Willidrop | Munich, 30 Jul 2026, undisclosed | 4 | brief §5 |
| Gate timings | Q+2, Q+2, Q+3, Q+4 | 7 | brief §3 |

**Explicitly excluded:** the "34% revenue growth / 326% profitability" IBM figures. Excluded on
credibility grounds, not space. See slide 4.

---

## 10. Still needed before this can be built

**Blocking — the deck cannot be finished without these:**

1. **S1–S4 Y3 ARR and EBITDA** (`5U-AI-MECE-Strategy.docx`). Slide 3's chart is the deck's best
   visual and currently has two of six data points.
2. **Gate scale/kill thresholds** (`5U-AI-MECE-Strategy.docx`). Slide 7's table is empty without them.
3. **Hiring req count and roles** (`5U-AI-90-Day-Roadmap.docx`). Ask item 2 on slide 7.

**Non-blocking — improves specific slides:**

4. S0 Y3 cash figure, to complete slide 1's three-row comparison.
5. Per-workstream budget split, owners, and day-90 outputs (`5U-AI-90-Day-Roadmap.docx`) for slide 6.
6. `5U-AI-Strategy-Deck.html` — needed to match visual style, type scale and palette at build time.

**Decisions only you can make:**

7. **Alsvid AI or 5U AI** — which name goes on the deck.
8. **Ambiguous-at-gate default** — does an unclear Q+2 result mean kill, or one more quarter?
   Pre-agree it; slide 7 invites the question.
9. **Final ask wording** — the three items above are drafted, not confirmed.
10. **cargo.one on slide 4, or cut** — the biggest structural risk, but the least actionable in a
    slide whose job is urgency.

**Output format when content is signed off:** HTML matching `5U-AI-Strategy-Deck.html`, or .pptx.
HTML is the better choice if the deck will be revised during review; .pptx if it needs to be
forwarded and edited by others.
