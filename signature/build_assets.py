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
SS = 4             # extra supersampling for the vector-drawn marks
ALPHA_LEVELS = 16  # these are flat-colour shapes; smooth alpha just costs bytes

ICON_COLOR = "#3E6485"   # mid-tone: legible on white AND on dark-mode grounds
ICON_CSS_PX = 15
TILE_CSS_PX = 18

# Stylised monogram marks. These are typographic stand-ins, not the official
# trademarks -- swap in real artwork with embed_logo.py.
# Set at the same cap height and baseline as the NOVA letters, so the three
# marks line up as a logo row rather than a grab-bag of shapes.
WORDMARKS = [
    ("scaile", "scaile", "#1F2328"),
    ("am",     "A&M",    "#C8102E"),
]

# The Nova SBE wordmark, reconstructed from the official logo: an 720x205 box
# with the ringed O riding above the N/V/A line and a bar beneath it.
NOVA_W, NOVA_H = 720, 205


def render_nova():
    """Draw the NOVA wordmark and save it at the signature's 18px line height."""
    ss = 3
    im = Image.new("RGBA", (NOVA_W * ss, NOVA_H * ss), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    poly = lambda pts: d.polygon([(x * ss, y * ss) for x, y in pts], fill="#000000")
    rect = lambda a, b, c, e: d.rectangle([a * ss, b * ss, c * ss, e * ss], fill="#000000")

    # N -- two stems joined by a diagonal band
    rect(0, 60, 46, 205)
    rect(104, 60, 150, 205)
    poly([(0, 60), (46, 60), (150, 205), (104, 205)])
    # O -- a ring sitting above the other letters
    d.ellipse([233 * ss, 0, 397 * ss, 164 * ss], fill="#000000")
    d.ellipse([275 * ss, 42 * ss, 355 * ss, 122 * ss], fill=(0, 0, 0, 0))
    rect(185, 172, 430, 205)  # the bar beneath the O
    # V
    poly([(450, 60), (496, 60), (515, 155), (534, 60), (580, 60), (525, 205), (505, 205)])
    # A -- no crossbar
    poly([(585, 205), (631, 205), (652, 110), (674, 205), (720, 205), (663, 60), (642, 60)])

    h = TILE_CSS_PX * SCALE
    w = round(h * NOVA_W / NOVA_H)
    return save(im.resize((w, h), Image.LANCZOS), "novasbe.png")


def save(img, name):
    """Quantise alpha before writing -- ~23% smaller, no visible difference."""
    a = img.getchannel("A").point(
        lambda v: round(v / 255 * (ALPHA_LEVELS - 1)) * 255 // (ALPHA_LEVELS - 1)
    )
    img = img.copy()
    img.putalpha(a)
    img.save(os.path.join(OUT, name), optimize=True)
    return name, img.size


def render_icon(name, out_name):
    """Rasterise a Lucide stroke icon at 3x in ICON_COLOR."""
    svg = open(os.path.join(SRC, f"{name}.svg")).read()
    svg = svg.replace("currentColor", ICON_COLOR)
    # Lucide ships stroke-width 2; nudge up so it holds together when downscaled.
    svg = re.sub(r'stroke-width="[\d.]+"', 'stroke-width="2.25"', svg)
    px = ICON_CSS_PX * SCALE
    data = cairosvg.svg2png(bytestring=svg.encode(), output_width=px, output_height=px)
    return save(Image.open(io.BytesIO(data)).convert("RGBA"), out_name)


def render_wordmark(slug, word, colour):
    """Set a word at the NOVA letters' cap height, baseline-aligned."""
    box_h = TILE_CSS_PX * SCALE                  # 54px, same box as NOVA
    cap_h = round(box_h * 145 / NOVA_H)          # NOVA's N/V/A occupy 145 of 205
    ss = 4
    path = os.path.join(FONTS, "InstrumentSans-Bold.ttf")

    # Solve for the point size whose cap height matches NOVA's letters.
    probe = ImageFont.truetype(path, 100)
    l, t, r, b = probe.getbbox("H")
    size = max(1, round(100 * (cap_h * ss) / (b - t)))
    font = ImageFont.truetype(path, size)

    im = Image.new("RGBA", (box_h * ss * 6, box_h * ss), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.text((10, box_h * ss), word, font=font, fill=colour, anchor="ls")  # ls = left/baseline

    bb = im.getbbox()
    im = im.crop((bb[0], 0, bb[2], box_h * ss))
    return save(im.resize((max(1, round(im.width / ss)), box_h), Image.LANCZOS), f"{slug}.png")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    built = [
        render_nova(),
        render_icon("map-pin", "icon-pin.png"),
        render_icon("phone", "icon-phone.png"),
        render_icon("linkedin", "icon-linkedin.png"),
    ]
    built += [render_wordmark(*w) for w in WORDMARKS]
    for name, size in built:
        print(f"  {name:22} {size[0]}x{size[1]}")
    print(f"{len(built)} assets -> {OUT}")
