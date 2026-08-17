#!/usr/bin/env python3
"""Add Claude to the day-0 panel: 20 prompts x 2 runs, merged into a v2 panel."""
import csv, json, os, re, sys
sys.path.insert(0, "/Users/khana/.claude/skills/scaile-tracking-prompts/scripts")
from env_loader import require
# Resolve credentials once on the main thread and pin them to the process
# environment. env_loader is not thread-safe and calls sys.exit() on a miss,
# which kills the pool instead of failing a single probe.
_l, _p = require("DATAFORSEO_LOGIN", "DATAFORSEO_PASSWORD")
os.environ["DATAFORSEO_LOGIN"], os.environ["DATAFORSEO_PASSWORD"] = _l, _p
from d4s_client import call_many

MODEL = "claude-sonnet-5"
RUNS = 2
MD_LINK = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")

prompts = [r["prompt_local"].strip() for r in
           csv.DictReader(open("03_tracking_prompts.csv", encoding="utf-8"))]
jobs = [(p, run) for p in prompts for run in range(RUNS)]
payloads = [[{"user_prompt": p, "model_name": MODEL, "web_search": True}]
            for p, _ in jobs]
print(f"{len(payloads)} Claude probes ({MODEL}, web search on)...")

outs = call_many("ai_optimization/claude/llm_responses/live", payloads, workers=8)

name_re = re.compile(r"zeit\s?ai|zeitmind", re.I)
new = []
for (p, run), out in zip(jobs, outs):
    if not out:
        continue
    text, doms = [], set()
    for res in out["tasks"][0].get("result") or []:
        for it in res.get("items") or []:
            for sec in it.get("sections") or []:
                if sec.get("type") == "text":
                    text.append(sec.get("text", ""))
                elif sec.get("type") == "annotation" and sec.get("url"):
                    try:
                        doms.add(sec["url"].split("/")[2].lower().replace("www.", ""))
                    except IndexError:
                        pass
    ans = " ".join(text)
    for u in MD_LINK.findall(ans):
        try:
            d = u.split("/")[2].lower().replace("www.", "")
            if d and "anthropic.com" not in d:
                doms.add(d)
        except IndexError:
            pass
    new.append({"prompt": p, "model": "claude", "run": run,
                "fanout_queries": [], "cited_domains": sorted(doms),
                "answer": ans,
                "client_cited": any("zeit-ai.com" in d for d in doms),
                "client_mentioned": bool(name_re.search(ans))})

panel = json.load(open("panel_day0.json", encoding="utf-8"))
panel["probes"].extend(new)
json.dump(panel, open("panel_day0_v2.json", "w"), ensure_ascii=False, indent=1)

ok = len(new)
cited = sum(p["client_cited"] for p in new)
ment = sum(p["client_mentioned"] for p in new)
print(f"\nclaude probes landed: {ok}/{len(jobs)}")
print(f"Zeit AI in Claude answers -> mentioned {ment}, cited {cited}")
print(f"panel total now {len(panel['probes'])} probes -> panel_day0_v2.json")
