#!/usr/bin/env python3
"""Share-of-voice analysis over a fanout_probe panel.json.

Computes, per brand: answer mention rate (share of probes whose answer text
matches the brand pattern), share of voice (brand's mentions / all tracked-brand
mentions), and citation counts (probes citing the brand's domain). Zeit AI plus
the DACH/EU competitor set from the KB landscape file.
"""
import collections, json, re, sys

PANEL = sys.argv[1] if len(sys.argv) > 1 else "panel_day0.json"

# brand -> (answer-text regex, [citation domains])
BRANDS = {
    "Zeit AI":        (r"\bzeit\s?ai\b|\bzeitmind\b", ["zeit-ai.com"]),
    "Veezoo":         (r"\bveezoo\b", ["veezoo.com"]),
    "Jedox":          (r"\bjedox\b", ["jedox.com"]),
    "Dot (GetDot)":   (r"\bgetdot\b", ["getdot.ai"]),
    "SAP (SAC/Joule)":(r"\bsap\b", ["sap.com"]),
    "Power BI/Copilot":(r"power\s?bi|microsoft\s(365\s)?copilot|\bfabric\b", ["microsoft.com", "powerbi.microsoft.com"]),
    "Palantir":       (r"\bpalantir\b", ["palantir.com"]),
    "Celonis":        (r"\bcelonis\b", ["celonis.com"]),
    "ThoughtSpot":    (r"\bthoughtspot\b", ["thoughtspot.com"]),
    "Tableau":        (r"\btableau\b", ["tableau.com"]),
    "Qlik":           (r"\bqlik\b", ["qlik.com"]),
    "Snowflake":      (r"\bsnowflake\b|cortex analyst", ["snowflake.com"]),
    "Databricks":     (r"\bdatabricks\b|\bgenie\b", ["databricks.com"]),
    "Lucanet":        (r"\blucanet\b", ["lucanet.com"]),
    "Board":          (r"\bboard international\b", ["board.com"]),
    "Anaplan":        (r"\banaplan\b", ["anaplan.com"]),
    "Pigment":        (r"\bpigment\b", ["pigment.com", "gopigment.com"]),
    "DATEV":          (r"\bdatev\b", ["datev.de"]),
    "Julius AI":      (r"\bjulius\s?ai\b", ["julius.ai"]),
    "ChatGPT/OpenAI": (r"\bchatgpt\b|\bopenai\b", ["openai.com", "chatgpt.com"]),
}

data = json.load(open(PANEL, encoding="utf-8"))
probes = data["probes"]
n = len(probes)
models = sorted({p["model"] for p in probes})

hits = {b: {"mention": 0, "cited": 0, "by_model": collections.Counter(),
            "prompts": set()} for b in BRANDS}
for p in probes:
    text = p.get("answer") or ""
    domains = set(p.get("cited_domains") or [])
    for b, (pat, doms) in BRANDS.items():
        mentioned = bool(re.search(pat, text, re.I))
        cited = any(any(d == cd or cd.endswith("." + d) for cd in domains) for d in doms)
        if mentioned or cited:
            hits[b]["prompts"].add(p["prompt"])
        if mentioned:
            hits[b]["mention"] += 1
            hits[b]["by_model"][p["model"]] += 1
        if cited:
            hits[b]["cited"] += 1

total_mentions = sum(h["mention"] for h in hits.values()) or 1
rows = sorted(hits.items(), key=lambda kv: -kv[1]["mention"])

print(f"panel: {n} probes · models: {', '.join(models)} · prompts: "
      f"{len({p['prompt'] for p in probes})}\n")
print(f"{'brand':18} {'mention%':>9} {'SoV%':>6} {'cited':>5}  per-model mentions")
for b, h in rows:
    if h["mention"] == 0 and h["cited"] == 0:
        continue
    pm = " ".join(f"{m}:{h['by_model'].get(m,0)}" for m in models)
    print(f"{b:18} {100*h['mention']/n:8.1f}% {100*h['mention']/total_mentions:5.1f}% "
          f"{h['cited']:5d}  {pm}")

zh = hits["Zeit AI"]
print(f"\nZeit AI appears in {len(zh['prompts'])}/20 tracked prompts "
      f"(any model, mention or citation)")
if zh["prompts"]:
    for pr in sorted(zh["prompts"]):
        print("  ·", pr[:90])

absent = [b for b, h in hits.items() if h["mention"] == 0 and h["cited"] == 0]
print(f"\nbrands never appearing: {', '.join(absent) if absent else 'none'}")

s = data["summary"]
print(f"\nofficial client rates -> cited: {s['overall_cited_rate']}, "
      f"mentioned: {s['overall_mention_rate']}")
print("top cited domains overall:",
      ", ".join(f"{d}({c})" for d, c in s["top_cited_domains"][:12]))
