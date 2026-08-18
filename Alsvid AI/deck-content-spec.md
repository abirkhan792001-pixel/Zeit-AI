# Alsvid AI leadership deck — content spec

**Status:** v4 — rebuilt on the 8-theme structure, in the Zeit AI template. Deck: [alsvid-ai-leadership-deck.html](alsvid-ai-leadership-deck.html).
**Audience:** Zeit AI leadership, internal. They know the company and the product.
**Branding:** Zeit AI logo on every slide; Alsvid AI is the product line inside it. 5U AI appears nowhere.
**Source research:** [5U-AI-pitch-deck-brief.md](5U-AI-pitch-deck-brief.md), plus external benchmarks cited on appendix C.

---

## The structure, and what changed from the draft

| # | Theme | Origin |
|---|---|---|
| 1 | **Problem** — what the work is, who has it, why it persists | as drafted |
| 2 | **Solution** — connect not migrate · agents complete the task · automation rate is the meter | moved ahead of market size |
| 3 | **Market size** — €3.4bn labour value, €117m reachable, 29× gap, break-even needs 30% of 213 | as drafted, plus the break-even framing |
| 4 | **Why now** — 89%/19% conviction gap, seven funded teams in one quarter | **new** — absorbed the standalone "how much have they raised" slide |
| 5 | **Competition** — fragmentation, 2×2 position, distribution risk | merged draft slides 4 and 5 |
| 6 | **ICP + GTM** — who they are, how we identify them, where we reach them | merged draft slides 6 and 7 |
| 7 | **Unit economics** — inference COGS against AI-native benchmarks, ACV, payback | draft slide 8, widened past COGS alone |
| 8 | **The ask** — four levers, gates, three approvals | **new** — the draft ended on COGS with nothing to approve |

**Four reasons for the changes.** The draft never closed on a decision. Competition took a quarter
of the deck with funding — a why-now argument — carrying a slide of its own. ICP and GTM were one
job split across two slides, since you identify these buyers *by* the channel that reaches them.
And COGS alone gives gross margin, not the economics question leadership actually asks.

**Cover and close** sit outside the eight. Four appendix slides: scenarios, hiring benchmarks,
sources, held-back material.

---

## Judgement calls worth knowing about

**Slide 5's 2×2 is a proposal.** Axes are *generic ↔ freight-native* and *reports on the work ↔
does the work* — chosen because they separate us from both the BI tools and the booking platforms
in one frame. Placements for cargo.one, Nexcade and the agent cohort are my read, not sourced
positioning. The slide says so in its footer. Replace with the competitor grid's own axes if it
defines them.

**Slide 3 carries the break-even finding.** The old deck opened on S0-vs-S5; in this structure that
argument is stronger inside market size, because the point is that reachable market and required
revenue are set by the same constraint — who we sell to.

**Slide 7 leads with benchmarks, not our numbers.** Three of the four "our numbers" rows are marked
*to fill* rather than estimated. What the slide does supply is the bar: AI-native P&L profiles
target 50–60% gross margin, not the SaaS 80%. That reframes the question from "is 60% good" to "are
we AI-native or AI-enabled", which is the more useful argument to have in the room.

**The insight on slide 7 is the pricing-COGS coupling.** Price ramps against automation rate — and
so does the inference bill. Margin holds only if price ramps faster than compute. That is the
relationship to instrument first, and it is specific to this pricing model rather than generic
AI-margin commentary.

---

## Still open

**Blocking nothing — the deck presents as-is. These improve it:**

1. **Inference cost per automated task, gross margin, CAC and payback** — slide 7's four rows.
   Three are placeholders. Everything else on the deck is real.
2. **S1–S4 Year 3 ARR and EBITDA** — appendix A1 has the rows waiting.
3. **Competitor grid axes and placements** — to replace the proposal on slide 5.
4. **Per-workstream split of the €66.5k**, owners and day-90 outputs.
5. **Buyer persona detail for slide 1** — who signs, and what they do today. The slide currently
   describes the *segment* precisely and the *person* not at all, because the ICP report was not
   supplied. This is the weakest slide as a result.

**The template — resolved.** Figma itself is still blocked by this environment's egress policy, but
the PDF export supplied everything needed. Values taken from `Zeit_AI__Logistics.pdf` and applied
verbatim: sage `#DBDBCD`, block grey `#EFEFED`, ink `#000000`, and the warm/olive body grey
`#797972` — that last one is what makes the palette cohere, and a neutral grey in its place reads
wrong immediately. Type is Inter on a 1920×1080 canvas: 120px cover title, 62px slide headline,
26px section head, 20px body, 13px letterspaced caps. The logo is lifted from page 1 of the PDF,
keyed to transparency and embedded as a data URI, so the deck stays self-contained.

Template patterns reused rather than invented: sage cover with the eight-arm asterisk, logo
top-right on content slides, thin full-width rule under the headline, section heads over a 2.5px
black rule, hairline-separated numbered rows, sage and black chips, the big-numeral band over grey
blocks along the bottom, and the 2×2 with dot-capped axes and a tinted winning quadrant.

**One thing to confirm before presenting.** Every financial figure traces to the 5U AI research
pack. If Alsvid AI's own model differs, the deck inherits the difference.

---

## Numbers ledger

| Figure | Value | Slide | Source |
|---|---|---|---|
| Labour value | €3.4bn/yr | 1, 3 | research pack |
| Reachable at today's ICP | €117m/yr | 3 | research pack |
| Gap multiple | 29× | 3 | research pack |
| Beachhead / full ICP | 213 / 1,479 | 1, 3, 6 | research pack |
| Break-even ARR | €2.92m | 3 | research pack |
| Break-even penetration | ~30% of 213 | 3 | research pack |
| Accounts implied | ~64 | 3, 6, 7 | **derived** (30% × 213) |
| Implied ACV | ≈€45k | 7 | **derived** (€2.92m ÷ 64) |
| Capacity guardrail | 1 FDE ≈ 10 accounts | 6 | research pack |
| FDEs at 64 accounts | 6–7 | 6 | **derived** |
| S0 / S5 Y3 ARR | €1.56m / €5.26m | 8, A1 | research pack |
| S0 / S5 Y3 EBITDA | −€0.89m / +€1.52m | 8, A1 | research pack |
| Combined-shock EBITDA | −€270k | A1 | research pack |
| 90-day budget | ~€66.5k, ~2% runway | 8 | research pack |
| Vendors mapped | 16 | 5 | research pack |
| Publish pricing | 2 of 27 | 5 | research pack |
| cargo.one reach | 28,000 forwarders | 5 | research pack |
| IBM intent / conviction | 89% / 19% | 4 | IBM vendor deck |
| AI-native target GM | 50–60% | 7 | Avante Ventures |
| Average AI product GM 2026 | 52% | 7 | SaaS Mag |
| Inference share of revenue | ~23% scaling-stage | 7 | The SaaS Academy |
| Disclosed inference ratios | 4–9% | 7 | Second Order Labs |
| Partner manager load | 5–7 regional partners | A2 | Partnership Leaders |
| Channel viability bar | ≥3:1 revenue-to-cost | A2 | Partnership Leaders |
| FDE prevalence | ~70% of AI/software cos | A2 | Sloane Staffing |
| Partner mgr comp DACH | avg €45.8k, €32k–€100k | A2 | StepStone, TalentUp |
| Engineer comp Munich | €77.5k–€99k, senior to €110k | A2 | Glassdoor, Levels.fyi |

**Excluded on credibility grounds:** the IBM "34% revenue growth / 326% profitability" figures — a
2017–2020 pre-gen-AI correlation the analyst brief itself flags as the weakest claim in the source.
