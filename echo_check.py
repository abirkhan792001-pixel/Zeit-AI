#!/usr/bin/env python3
"""Does a brand's mention rate survive when we exclude prompts that name it?

Four tracked prompts name a vendor (SAP, Veezoo, Palantir, ChatGPT). An answer
echoing the question would score as a "mention" without being a recommendation.
This splits each brand's mentions into echo (from prompts naming it) and organic.
"""
import json, re

BRANDS = {
    "SAP":      (r"\bsap\b",       r"\bsap\b"),
    "Veezoo":   (r"\bveezoo\b",    r"\bveezoo\b"),
    "Palantir": (r"\bpalantir\b",  r"\bpalantir\b"),
    "ChatGPT":  (r"\bchatgpt\b|\bopenai\b", r"\bchatgpt\b"),
    "Power BI": (r"power\s?bi|copilot", r"power\s?bi"),
    "Tableau":  (r"\btableau\b",   r"\btableau\b"),
    "Qlik":     (r"\bqlik\b",      r"\bqlik\b"),
    "Celonis":  (r"\bcelonis\b",   r"\bcelonis\b"),
    "Jedox":    (r"\bjedox\b",     r"\bjedox\b"),
}

probes = json.load(open("panel_day0.json", encoding="utf-8"))["probes"]
n_all = len(probes)

print(f"{'brand':10} {'all':>12} {'organic only':>26}  prompts naming it")
for b, (ans_pat, prompt_pat) in BRANDS.items():
    named = [p for p in probes if re.search(prompt_pat, p["prompt"], re.I)]
    clean = [p for p in probes if not re.search(prompt_pat, p["prompt"], re.I)]
    m_all = sum(bool(re.search(ans_pat, p["answer"] or "", re.I)) for p in probes)
    m_clean = sum(bool(re.search(ans_pat, p["answer"] or "", re.I)) for p in clean)
    n_prompts = len({p["prompt"] for p in named})
    rate_all = 100 * m_all / n_all
    rate_clean = 100 * m_clean / len(clean) if clean else 0
    print(f"{b:10} {m_all:3d}/{n_all}  {rate_all:5.1f}%   "
          f"{m_clean:3d}/{len(clean):3d}  {rate_clean:5.1f}%   "
          f"{'DROP' if rate_clean < rate_all - 5 else 'holds':5}  {n_prompts}")
