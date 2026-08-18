# 5U AI — Internal Pitch Deck: Conversation Summary & Build Brief

**Purpose of this doc:** Handoff summary of a planning conversation for an internal pitch deck. Use this as context to generate the actual deck content/artifact.

---

## 1. Project context

- **What:** Internal pitch deck to leadership, arguing for a specific GTM expansion strategy for 5U AI (an AI-agent startup for European freight forwarding).
- **Audience:** Internal stakeholders (leadership team) — not investors. Ask is not yet finalized but centers on approving budget/hiring/roadmap for the expansion strategy.
- **Framing requested by user:** Show **What** (the recommendation), **Why** (the research case), **How** (the execution plan).
- **Constraint:** Max **7 slides**, excluding cover slide, ending slide, and appendix.

## 2. Source material provided

1. **5U-AI-ICP-Report.docx** — ICP definition, buyer personas, market sizing (beachhead ~213 companies, full ICP ~1,479), channel ranking, expansion whitespace.
2. **5U-AI-Research-Dossier.docx** — Full company/product research: origin, funding ($3.2M pre-seed, 28 Jul 2026, led by Emerge Capital), product architecture, pricing recommendation, market sizing (two methods), 16-competitor GTM synthesis, diligence risks.
3. **5U-AI-MECE-Strategy.docx** — Six MECE growth scenarios (S0–S5), stress tests against 5 shock types, gates/kill criteria, event calendar.
4. **5U-AI-90-Day-Roadmap.docx** — Week-by-week 90-day plan executing S1+S2 first, S4 pilot, S3 gated; budget (~€66.5k); RACI; risks.
5. **5U-AI-Strategy-Deck.html** — Existing full/dense internal strategy deck (12+ slides) covering all of the above — this new deck is a **sharper, leadership-ready cut** of that material, not a replacement for it.
6. **IBM_Supply_Chain_AI_Analyst_Brief.md** — Third-party analyst brief on IBM's "Put AI to Work: Supply Chains" vendor deck. Used for **top-down demand-side validation** (with explicit caveats — see §5).

## 3. Core research findings (the spine of the deck)

- **The binding constraint is the ICP, not the product.** Three independent models (market sizing, unit economics, MECE scenario modeling) converge: the beachhead alone (S0, ~213 DACH+Benelux companies) cannot reach break-even and burns cash.
- **Break-even ARR is €2.92m.** No single growth lever reaches it alone. Only the **combined strategy (S5)** — partner channel (S1) + ACV expansion (S2) + self-serve tail (S3) + road freight via Timocom (S4) — crosses into profit: **€5.26m Y3 ARR, +€1.52m EBITDA, +€3.43m cash**, vs. S0's €1.56m ARR / −€0.89m EBITDA.
- **Market sizing gap:** labour-value ceiling ≈ €3.4bn/yr vs. reachable revenue at today's ICP/pricing ≈ €117m/yr — a **29x gap**, reframing ambition without needing VC-style TAM slides.
- **Stress-test robustness:** S5 stays EBITDA-positive under every single shock (price, demand, churn, capacity), degrading to a survivable −€270k only when all four hit simultaneously.
- **Competitive whitespace:** no partner channel despite built CargoWise/Timocom integrations; one reference logo (TCI) vs. competitors' several; cargo.one owns distribution (28,000 forwarders) as the biggest structural risk; pricing-publish race (only 2 of 27 vendors publish pricing — first-mover sets the DACH anchor).
- **Governance already built:** the MECE strategy doc has defined gates/kill-criteria (Q+2 partner channel, Q+2 pricing, Q+3 road, Q+4 self-serve) and a hard capacity guardrail (1 FDE ≈ 10 accounts) — useful as a trust-building "we've already thought about downside" element.

## 4. Agreed 7-slide skeleton (main deck)

| # | Slide | Content | Why it's here |
|---|---|---|---|
| 1 | **The finding + the ask** | S0 vs. S5 headline comparison (€1.56m→€5.26m ARR; −€0.89m→+€1.52m EBITDA). State the ask (fund S5) directly. | BLUF — leadership knows the ask in the first 90 seconds; everything after is proof, not build-up. |
| 2 | **Why the ceiling is so low** | Two stacked numbers: 29x labour-value gap (€3.4bn vs €117m), and break-even needs ~30% penetration of just 213 beachhead companies. | Same idea at two zoom levels — category is huge, current playbook reaches a sliver. |
| 3 | **Scenario comparison S0–S5** | Bar chart, Y3 ARR/EBITDA across all six scenarios. Small annotation: S5 robustness under stress tests (EBITDA-positive under every single shock; −€270k only under combined shock). | The single best/most persuasive visual — proves the finding rather than asserting it. |
| 4 | **Why now** *(expanded per latest discussion — see §5)* | Two signal blocks: (a) top-down — IBM's 89%/19% intent-vs-conviction gap, framed as "even IBM's own sales material shows..."; (b) bottom-up — 5U AI, Willidrop (Munich, vehicle logistics, funded same week), and the wider YC cohort (SpaceFlow, Lighthouz AI, Derya, Haladir, Peer, FleetWorks, Lanesurf) all racing into the same category thesis simultaneously. | Answers "why hasn't someone already done this, why move now" — combines demand-side and supply-side validation. |
| 5 | **The four levers (MECE)** | S1 partner channel, S2 pricing, S3 self-serve (gated), S4 road pilot — one clean diagram, one phrase each. | Pivot from why to how. |
| 6 | **90 days, budget, guardrail** | Workstream-at-a-glance table + ~€66.5k (~2% of runway) + the FDE capacity rule (1 FDE ≈ 10 accounts). | "How much, how fast" in one slide — budget and roadmap didn't earn separate slides at 7-slide length. |
| 7 | **Gates, kill criteria, and the ask** | Day-90 gate table (scale/kill thresholds per workstream) + concrete asks (budget sign-off, hiring reqs, pricing-publish approval). | Closes on control, not enthusiasm — shows exactly what's being approved and when leadership finds out if it's not working. |

**Structure logic:** Act 1 (slide 1) states the decision. Act 2 (slides 2–4) proves it. Act 3 (slides 5–7) shows how it gets executed. This is a pyramid-principle / BLUF structure chosen deliberately for a time-constrained leadership audience, as opposed to a build-up-to-the-ask narrative.

## 5. Latest addition — external market signal (this turn)

User requested strengthening the case with external signals beyond 5U AI's own data: IBM's analyst brief plus comparable funded startups (5U AI, Willidrop, other YC-backed companies).

**Verified via search:**
- **Willidrop** (Munich) — emerged from stealth 30 Jul 2026, agent-based OS for vehicle logistics, funding round just closed (amount undisclosed). Same city, same week as 5U AI's own funding news, adjacent vertical.
- **YC-backed cohort** building the same "AI agents replace manual freight/logistics ops" thesis from different angles: SpaceFlow (managed runtime for supply-chain agents), Lighthouz AI (AP/AR/collections automation for freight brokers), Derya (AI-native logistics office), Haladir (decisional AI layer over WMS/TMS/OMS), Peer, FleetWorks, Lanesurf.

**IBM brief — key usable data point:**
- **89% vs. 19% gap**: 89% of execs say gen AI will be part of automation investment; only 19% call it *critically important*. This is the single most useful stat — describes a market of budget-holders who haven't committed yet, i.e., a closing window.

**Explicit caution given to user (carry into deck):**
- **Do NOT use** the "34% more revenue growth / 326% more profitability" stat — it's a 2017–2020, pre-gen-AI correlation, and the analyst brief itself flags it as the weakest claim in the source deck. Using it would hand a sharp audience a reason to distrust the rest of the evidence.
- **Frame IBM data as vendor material, not neutral research** — 6 of 9 footnotes in the original IBM deck are IBM's own self-commissioned survey data. Correct framing: "even IBM's own sales material, aimed at converting Fortune 500 CSCOs, shows..." — this is more persuasive than presenting it as independent research, and protects credibility if challenged.

**Where it lands:** Upgrades **Slide 4 ("Why now")** into two stacked evidence blocks (top-down IBM signal + bottom-up funded-startup signal) rather than adding an 8th slide. Flagged one open consideration: this shifts slide 4's argument from "gap competitors haven't closed" toward "the category is heating up, move before it's crowded" — both true, not contradictory, but worth being deliberate about which framing leads.

## 6. What was deliberately cut to appendix (and why)

- **Company/product origin story** (founders, funding round narrative) — audience already knows this; re-explaining wastes attention.
- **Full 16-vendor competitor grid** — synthesis bullets carry the insight; grid is backup if asked.
- **Full week-by-week roadmap and RACI table** — leadership needs the shape of the plan, not operating detail.
- **Full pricing mechanics** (hybrid model, ramp-against-automation-rate, discount guardrails) — one line in main deck; detail is a pricing-committee document.
- **Full event calendar** — one line ("3 events, pre-booked meetings") vs. 10 rows of conference logistics.
- **Detailed diligence risks** (DPA hosting contradiction, no SOC 2, 2-year lock-in, Clause 10.3 data-use ambiguity) — real, but a "fix before scaling" list, not a growth-pitch slide. Urgency-relevant fragments (Nexcade might publish pricing first, cargo.one distribution risk) were folded into the "why now" slide instead.
- **Full stress-test 6×6 grid** — one summary line on slide 3 instead of the full matrix.

## 7. Open items / next steps

- [ ] Draft actual slide-by-slide content for slide 4 (headline, the two signal blocks, chart/layout notes, and the hand-off into slide 5) — this was the immediate next step requested before this summary was asked for.
- [ ] Then draft full slide-by-slide content (headlines, key numbers, chart specs) for all 7 slides.
- [ ] Decide appendix slide list explicitly (candidates listed in §6).
- [ ] Confirm final "ask" wording for slide 7 (budget sign-off / hiring reqs / pricing-publish approval) — not yet finalized by user.
- [ ] Build actual deck file (likely .pptx or HTML matching the existing 5U-AI-Strategy-Deck.html visual style) once content is approved.
