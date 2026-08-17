#!/usr/bin/env python3
"""Own-brand recall: seven German questions that name Zeit AI, same four models
as the day-0 panel, two runs each.

The 20 tracked questions are deliberately non-brand, so the panel can say what
happens when a buyer describes a problem, and nothing at all about what happens
when a buyer already knows the name. This fills that gap. It is a different
measurement, not more of the same one: on these questions "mentions Zeit AI" is
worthless, because the question says Zeit AI. What counts is whether the answer
knows anything true about the company.

Scored per answer:
  cited     zeit-ai.com in the sources.
  knows     at least one checkable fact: ZeitMind, Munich, Y Combinator, a
            founder by name, or the agentic-BI-for-the-Mittelstand positioning.
  wrong     the answer is about a different Zeit: the newspaper, the publisher,
            zeit.de. "Zeit" is a common German word, so this is a real failure
            mode and worth counting separately from silence.
  declines  the answer says it has no information on the company.

Writes panel_brand_recall.json in the same probe schema as panel_day0_v2.json.
"""

import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor

SKILL = "/Users/khana/.claude/skills/scaile-tracking-prompts/scripts"
sys.path.insert(0, SKILL)
from env_loader import require                                    # noqa: E402

# env_loader is not thread safe and exits the process on a miss, so resolve
# every credential up front on the main thread.
_l, _p = require("DATAFORSEO_LOGIN", "DATAFORSEO_PASSWORD")
os.environ["DATAFORSEO_LOGIN"], os.environ["DATAFORSEO_PASSWORD"] = _l, _p
os.environ.setdefault("GEMINI_API_KEY", require("GEMINI_API_KEY")[0])

import fanout_probe as FP                                         # noqa: E402
from d4s_client import call_many                                  # noqa: E402

OUT = "panel_brand_recall.json"
RUNS = 2

PROMPTS = [
    ("identity",   "Was ist Zeit AI und für welche Unternehmen ist die Software gedacht?"),
    ("proof",      "Welche Erfahrungen haben mittelständische Unternehmen mit Zeit AI gemacht?"),
    ("pricing",    "Was kostet Zeit AI und wie läuft die Einführung im Unternehmen ab?"),
    ("compliance", "Ist Zeit AI DSGVO-konform und wo werden die Daten gehostet?"),
    ("head to head", "Zeit AI oder Veezoo für KI-Datenanalyse im Mittelstand, was ist besser?"),
    ("alternatives", "Welche Alternativen zu Zeit AI gibt es im deutschsprachigen Raum?"),
    ("company",    "Wer steckt hinter Zeit AI und wie ist das Unternehmen finanziert?"),
]

MD_LINK = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")


def probe_claude(prompt):
    """add_claude.py's parser, kept here so this script stands alone."""
    payload = [[{"user_prompt": prompt, "model_name": "claude-sonnet-5",
                 "web_search": True}]]
    out = call_many("ai_optimization/claude/llm_responses/live", payload, workers=1)[0]
    if not out:
        return None
    text, doms = [], set()
    for res in out["tasks"][0].get("result") or []:
        for it in res.get("items") or []:
            for sec in it.get("sections") or []:
                if sec.get("type") == "text":
                    text.append(sec.get("text", ""))
                elif sec.get("type") == "annotation" and sec.get("url"):
                    doms.add(FP.norm_domain(sec["url"]))
    ans = " ".join(text)
    for u in MD_LINK.findall(ans):
        d = FP.norm_domain(u)
        if d and "anthropic.com" not in d:
            doms.add(d)
    return {"fanout_queries": [], "cited_domains": sorted(d for d in doms if d),
            "answer": ans}


ENGINES = {
    "gemini": lambda p: FP.probe_gemini(p, retries=1),
    "chatgpt": lambda p: FP.probe_d4s(p, "chat_gpt", "gpt-4o-mini"),
    "perplexity": lambda p: FP.probe_d4s(p, "perplexity", "sonar"),
    "claude": probe_claude,
}


def run():
    jobs = [(intent, prompt, model, run)
            for intent, prompt in PROMPTS
            for model in ENGINES
            for run in range(RUNS)]

    def one(job):
        intent, prompt, model, run = job
        try:
            r = ENGINES[model](prompt)
        except Exception as e:
            print(f"  FAIL {model} r{run} {intent}: {e}", file=sys.stderr)
            return None
        if not r:
            return None
        doms = r["cited_domains"]
        return {"prompt": prompt, "intent": intent, "model": model, "run": run,
                "fanout_queries": r["fanout_queries"], "cited_domains": doms,
                "answer": r["answer"],
                "client_cited": any("zeit-ai.com" in d for d in doms),
                "client_mentioned": bool(re.search(r"zeit\s?-?ai|zeitmind",
                                                   r["answer"], re.I))}

    print(f"{len(jobs)} probes: {len(PROMPTS)} questions x {len(ENGINES)} models "
          f"x {RUNS} runs")
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=8) as ex:
        probes = [p for p in ex.map(one, jobs) if p]
    print(f"{len(probes)}/{len(jobs)} returned in {time.time() - t0:.0f}s")

    json.dump({"cohort": "brand-recall", "runs": RUNS, "probes": probes},
              open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"-> {OUT}")


if __name__ == "__main__":
    run()
