#!/usr/bin/env python3
"""
Replace a stylised monogram mark with a real logo file.

The marks shipped in assets/ are typographic stand-ins. Drop in official
artwork with, for example:

    python3 embed_logo.py novasbe ~/Downloads/nova-sbe.png
    python3 embed_logo.py am ~/Downloads/am-logo.svg --bg "#C8102E" --pad 3
    python3 build_signature.py          # re-embed and rebuild dist/

Slugs: novasbe | scaile | am
Accepts PNG, JPG, WEBP or SVG. Transparent background by default; pass --bg to
sit the logo on a rounded tile like the stand-ins do.
"""
import argparse
import io
import os
import sys

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(ROOT, "assets")
SLUGS = ("novasbe", "scaile", "am")
SIZE = 54  # 18px display at 3x
SS = 4     # supersample the tile so the corner radius stays smooth


def load(path):
    if path.lower().endswith(".svg"):
        import cairosvg  # only needed for SVG input
        png = cairosvg.svg2png(url=path, output_width=SIZE * SS, output_height=SIZE * SS)
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

    big = SIZE * SS
    canvas = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    if a.bg.lower() != "none":
        ImageDraw.Draw(canvas).rounded_rectangle(
            [0, 0, big - 1, big - 1], radius=int(big * a.radius), fill=a.bg
        )

    logo = load(a.image)
    inner = big - (a.pad * SS * 2)
    logo.thumbnail((inner, inner), Image.LANCZOS)  # preserves aspect ratio
    canvas.alpha_composite(logo, ((big - logo.width) // 2, (big - logo.height) // 2))

    out = os.path.join(ASSETS, f"{a.slug}.png")
    canvas.resize((SIZE, SIZE), Image.LANCZOS).save(out, optimize=True)
    print(f"wrote {os.path.relpath(out, ROOT)}  ({SIZE}x{SIZE})")
    print("now run: python3 build_signature.py")


if __name__ == "__main__":
    main()
