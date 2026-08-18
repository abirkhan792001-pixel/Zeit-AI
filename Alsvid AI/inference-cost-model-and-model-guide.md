# AI Infrastructure: Cost Model & Open-Source Model Selection Guide

*Companion to freight-ai-pitch-brief.md — covers inference cost modeling (self-hosted EU GPU vs. Lyceum pay-per-token) and which open-source model fits which layer.*

**Caveat on all numbers below:** these are illustrative estimates built from stated vendor pricing (Lyceum's July/Aug 2026 rate card) and typical token/throughput assumptions, not measured data from your actual documents. Treat this as a framework to plug real pilot numbers into, not a final budget line.

---

## 1. Cost Model: Self-Hosted GPU vs. Lyceum Pay-Per-Token

### Assumptions
- **Document extraction (Layer 1, OCR/VLM):** ~1,500 input tokens (page image + prompt) + ~400 output tokens (extracted JSON) per page
- **Email/quote drafting (Layer 1, text):** ~2,000 input tokens (thread + rate context) + ~600 output tokens (draft) per interaction
- **Self-hosted GPU baseline:** one L40S-class instance, ~€1.00–1.10/hr, run continuously (~€780/month fixed, regardless of volume, up to its throughput ceiling)

### Document extraction: cost per page

| Volume/month | Lyceum (Qwen2.5-VL-72B, $0.25in/$0.75out per 1M) | Self-hosted L40S (fixed ~€780/mo) | Cheaper option |
|---|---|---|---|
| 5,000 pages | ~$4 | ~€780 (idle capacity) | **Lyceum, by a wide margin** |
| 100,000 pages | ~$70 | ~€780 (still well under capacity) | **Lyceum** |
| 500,000 pages | ~$350 | ~€780 (near capacity for a specialist OCR model) | **Lyceum** |
| ~1.1M+ pages | ~$770+ | ~€780 (fully utilized) | **Roughly breaks even — self-host starts to win above this** |

**Read:** at pilot-through-mid-growth volumes, pay-per-token is cheaper than running your own GPU, not just operationally simpler — the fixed cost of a self-hosted instance only pays for itself once you're pushing well over a million pages/month through it continuously. This is a materially higher breakeven point than the ~50–100K pages/month figure cited in general OCR-vs-managed-API comparisons, because that comparison was against expensive commercial OCR APIs (e.g. Textract), not a cheap token-priced open VLM.

**The catch:** this comparison uses Lyceum's *general-purpose* VLM (Qwen2.5-VL-72B), because the specialist OCR models with the best benchmark accuracy (PaddleOCR-VL, DeepSeek-OCR, dots.ocr) aren't confirmed in Lyceum's catalog as of this deck. If accuracy on messy freight documents requires those specialists, the real comparison is "self-host a cheap specialist model" vs. "Lyceum's general VLM at lower accuracy" — not a clean apples-to-apples cost comparison. Worth a direct question to Lyceum before finalizing.

### Email/quote automation: cost per interaction

| Model | Cost/interaction | Cost at 10K/mo | Cost at 100K/mo | Fit |
|---|---|---|---|---|
| Qwen3.5-9B ($0.15in/$0.20out) | ~$0.0004 | ~$4 | ~$42 | Triage, simple classification/routing |
| GLM-5.2 ($1.50in/$4.50out) | ~$0.006 | ~$60 | ~$600 | Actual quote drafting, nuanced replies |
| DeepSeek-V4-Pro ($1.75in/$3.50out) | ~$0.005 | ~$50 | ~$500 | Comparable tier to GLM-5.2 |

At these volumes, self-hosting a text LLM isn't worth considering — the serverless cost is trivial next to the engineering cost of running your own inference stack for a general-purpose LLM. Reserve self-hosting for the day you're fine-tuning a model on your own proprietary quote data and need a private, tunable deployment.

---

## 2. Why Lyceum (or a comparable EU pay-per-token host) is the better starting point

- **Cheaper than self-hosting until well past pilot scale** (see breakeven above), because you're not paying for idle GPU time.
- **No infra/MLOps overhead** during the phase where you should be validating product-market fit, not building a serving stack.
- **EU-hosted, OpenAI-compatible** — matches the DACH/EU data-residency story your customers will ask about, without a rebuild if you later move to a different backend.
- **Smart routing tiers** (Simple/Complex/Reasoning) map naturally onto your own task tiers — cheap model for triage, stronger model for anything customer-facing or liability-sensitive.

**What to verify before relying on this for customer commitments:** get the actual DPA and sub-processor list, confirm "zero retention" is contractual (not just current practice), and directly ask whether specialist OCR models are available or roadmapped — Lyceum's own technical content is careful to note that "sovereignty" isn't a legally defined status, which is a more honest framing than the pitch deck's headline claims.

---

## 3. Open-Source Model Guide by Task

### Layer 1 — Document extraction (BLs, invoices, customs docs, rate sheets)
| Model | Good at | Notes |
|---|---|---|
| PaddleOCR-VL | Broadest language/layout coverage, strong table extraction | Small (~0.9B), leads on OmniDocBench for multilingual/mixed-script docs — good default if document language varies |
| DeepSeek-OCR | High-throughput bulk batch OCR | MoE architecture, cheap at scale, MIT-licensed |
| dots.ocr | Compact, fast, good general layout parsing | 1.7B, MIT-licensed |
| GLM-OCR | Fastest normal-case throughput | Good default if you want one model without heavy evaluation |
| Qwen2.5-VL-72B (general VLM, on Lyceum) | Flexible fallback, no self-hosting needed | Not document-specialized — needs more prompt engineering, likely lower accuracy on complex tables/degraded scans than specialists above |

**How to go about it:** don't pick from a leaderboard alone — build a ~50–100 page internal benchmark from your own BLs/invoices/customs forms (mixed languages, scan quality) and test 2–3 candidates against it. Start via Lyceum/PoC credits or Hugging Face inference for the eval; self-host or find an EU host for the winner once volume justifies it.

### Layer 1 — Email/quote automation (text generation)
| Model | Good at | Notes |
|---|---|---|
| Qwen3.5-9B / DeepSeek-V4-Flash | Cheap, fast triage, routing, classification | Use for high-volume, low-stakes steps |
| GLM-5.2 / DeepSeek-V4-Pro | Nuanced drafting, multi-step reasoning | Use where getting a quote or reply wrong has real cost |
| Kimi K3 | Frontier-tier reasoning/agentic tasks | Priciest open option in this set — reserve for genuinely hard cases |

**How to go about it:** tier your tasks by stakes, not by defaulting to your strongest model everywhere. Route simple email classification to the cheap model; escalate anything touching rates, commitments, or customer-facing drafts to the stronger tier.

### Layer 2 — HS classification & sanctions screening
This isn't primarily a generative-LLM task — treat it as retrieval + classification, not free-text generation, given the liability stakes your brief already flags.
- **Qwen3-Embedding-8B** (multilingual, available on Lyceum) for embedding-based retrieval against your HS taxonomy and sanctions lists.
- A small LLM (Qwen3.5-9B tier) for reranking/tie-breaking ambiguous matches.
- Traditional NER + fuzzy matching for sanctions-list screening — more deterministic and auditable than pure LLM generation, which matters when a wrong call has legal consequences.

**How to go about it:** build this as a retrieval-augmented pipeline with a human-review step for low-confidence matches, not an LLM asked to "just classify this." Auditability should drive the architecture here more than raw accuracy.

### Layer 3 — Risk signal → plain-language rebooking recommendation
The LLM's job here is narrow: turning an already-structured risk signal and PO context into readable recommendation text. Any mid-tier model (GLM-5.2, DeepSeek-V4-Pro) handles this fine — it's not where your differentiation or your cost risk lives. The hard, differentiating part is the signal ingestion and forecasting pipeline upstream of the LLM (AIS data, news, port congestion feeds), which is a data engineering problem, not a model-selection one.

---

## 4. Sequencing recommendation

1. **Pilot:** run everything serverless/pay-per-token (Lyceum or comparable). Track token and page volume by task — this is the data you need to validate the cost model above.
2. **Validate accuracy on your own documents** before trusting any leaderboard ranking, especially for Layer 1 extraction and Layer 2 classification.
3. **Keep Layer 2 deterministic where possible** — retrieval/classification architecture, not generation, given liability exposure.
4. **Revisit self-hosting** only once volume approaches the breakeven point *and* you have proprietary data worth fine-tuning on (LoRA) — that's the point where owning the stack starts paying for itself twice over.
