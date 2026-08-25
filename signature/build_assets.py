#!/usr/bin/env python3
"""
Build the email-safe PNG assets used by the signature.

Email clients do not reliably render SVG, so every glyph in the signature is a
raster PNG embedded as a base64 data URI. This script produces them at 3x the
CSS display size so they stay crisp on retina displays.

Outputs -> signature/assets/*.png
"""
import io
import os
import re

import cairosvg
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
OUT = os.path.join(ROOT, "assets")
FONTS = "/mnt/skills/examples/canvas-design/canvas-fonts"

SCALE = 3          # 3x for retina
SS = 4             # extra supersampling for the vector-drawn tiles

ICON_COLOR = "#3E6485"   # mid-tone: legible on white AND on dark-mode grounds
ICON_CSS_PX = 15
TILE_CSS_PX = 18

# Stylised monogram marks. These are typographic stand-ins, not the official
# trademarks -- swap in real artwork with embed_logo.py.
TILES = [
    ("novasbe", "N", "#0A2F5C"),
    ("scaile",  "s", "#0E7A80"),
    ("am",      "&", "#C8102E"),
]


def render_icon(name, out_name):
    """Rasterise a Lucide stroke icon at 3x in ICON_COLOR."""
    svg = open(os.path.join(SRC, f"{name}.svg")).read()
    svg = svg.replace("currentColor", ICON_COLOR)
    # Lucide ships stroke-width 2; nudge up so it holds together when downscaled.
    svg = re.sub(r'stroke-width="[\d.]+"', 'stroke-width="2.25"', svg)
    px = ICON_CSS_PX * SCALE
    data = cairosvg.svg2png(bytestring=svg.encode(), output_width=px, output_height=px)
    img = Image.open(io.BytesIO(data)).convert("RGBA")
    img.save(os.path.join(OUT, out_name), optimize=True)
    return out_name, img.size


def render_tile(slug, glyph, bg):
    """Draw a rounded-square monogram tile with an optically centred glyph."""
    px = TILE_CSS_PX * SCALE
    big = px * SS
    img = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, big - 1, big - 1], radius=int(big * 0.24), fill=bg)

    font = ImageFont.truetype(os.path.join(FONTS, "InstrumentSans-Bold.ttf"), int(big * 0.62))
    # Centre on the glyph's actual ink box, not its advance/line metrics.
    l, t, r, b = d.textbbox((0, 0), glyph, font=font)
    d.text(((big - (r - l)) / 2 - l, (big - (b - t)) / 2 - t), glyph, font=font, fill="#FFFFFF")

    img = img.resize((px, px), Image.LANCZOS)
    out = f"{slug}.png"
    img.save(os.path.join(OUT, out), optimize=True)
    return out, img.size


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    built = [
        render_icon("map-pin", "icon-pin.png"),
        render_icon("phone", "icon-phone.png"),
        render_icon("linkedin", "icon-linkedin.png"),
    ]
    built += [render_tile(*t) for t in TILES]
    for name, size in built:
        print(f"  {name:22} {size[0]}x{size[1]}")
    print(f"{len(built)} assets -> {OUT}")
