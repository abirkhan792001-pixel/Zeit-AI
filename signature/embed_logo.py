#!/usr/bin/env python3
"""
Replace a stylised monogram mark with a real logo file.

scaile and A&M ship as their names set in type; Nova SBE is a reconstruction of
the real wordmark. Drop in official artwork with, for example:

    python3 embed_logo.py novasbe ~/Downloads/nova-sbe.png
    python3 embed_logo.py am ~/Downloads/am-logo.svg --bg "#C8102E" --pad 3
    python3 build_signature.py          # re-embed and rebuild dist/

Slugs: novasbe | scaile | am
Accepts PNG, JPG, WEBP or SVG. The logo is scaled to the signature's 18px line
height and keeps its own aspect ratio, so wide wordmarks work as well as square
marks. Transparent background by default; pass --bg to sit it on a rounded tile.
"""
import argparse
import io
import os
import sys

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(ROOT, "assets")
SLUGS = ("novasbe", "scaile", "am")
HEIGHT = 54  # 18px display at 3x; width follows the logo's own aspect ratio
SS = 4       # supersample so a tile's corner radius stays smooth


def load(path):
    if path.lower().endswith(".svg"):
        import cairosvg  # only needed for SVG input
        png = cairosvg.svg2png(url=path, output_height=HEIGHT * SS)
        return Image.open(io.BytesIO(png)).convert("RGBA")
    return Image.open(path).convert("RGBA")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", choices=SLUGS)
    ap.add_argument("image")
    ap.add_argument("--bg", default="none", help='tile colour, e.g. "#C8102E" (default: transparent)')
    ap.add_argument("--pad", type=int, default=0, help="inset in display px (default: 0)")
    ap.add_argument("--radius", type=float, default=0.24, help="corner radius as a fraction (default: 0.24)")
    a = ap.parse_args()

    if not os.path.isfile(a.image):
        sys.exit(f"no such file: {a.image}")

    logo = load(a.image)
    pad = a.pad * SS
    inner_h = HEIGHT * SS - pad * 2
    scale = inner_h / logo.height
    logo = logo.resize((max(1, round(logo.width * scale)), inner_h), Image.LANCZOS)

    big_w, big_h = logo.width + pad * 2, HEIGHT * SS
    canvas = Image.new("RGBA", (big_w, big_h), (0, 0, 0, 0))
    if a.bg.lower() != "none":
        ImageDraw.Draw(canvas).rounded_rectangle(
            [0, 0, big_w - 1, big_h - 1], radius=int(big_h * a.radius), fill=a.bg
        )
    canvas.alpha_composite(logo, (pad, pad))

    out = os.path.join(ASSETS, f"{a.slug}.png")
    final = canvas.resize((max(1, round(big_w / SS)), HEIGHT), Image.LANCZOS)
    final.save(out, optimize=True)
    print(f"wrote {os.path.relpath(out, ROOT)}  ({final.width}x{final.height}"
          f" -> {round(final.width/3)}x{round(final.height/3)} in the signature)")
    print("now run: python3 build_signature.py")


if __name__ == "__main__":
    main()
