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

# The official Nova SBE logo, supplied as src/logos/nova-sbe-source.png. The
# lockup's descriptor ("NOVA SCHOOL OF BUSINESS & ECONOMICS") is two 23px lines
# in a 630px image -- it would be under 2px tall in the signature -- so only the
# wordmark is used, which is how the mark is meant to be set at small sizes.
NOVA_SRC = os.path.join(ROOT, "src", "logos", "nova-sbe-source.png")


def ink_bbox(img):
    """Bounding box of the visible ink, whatever the source's background is."""
    flat = Image.alpha_composite(Image.new("RGBA", img.size, (255,) * 4), img).convert("L")
    w, h = flat.size
    px = flat.load()
    xs = [x for x in range(w) if any(px[x, y] < 128 for y in range(h))]
    ys = [y for y in range(h) if any(px[x, y] < 128 for x in range(w))]
    return xs[0], ys[0], xs[-1] + 1, ys[-1] + 1


def render_nova():
    """Crop the wordmark out of the official logo and set it to the line height."""
    src = Image.open(NOVA_SRC).convert("RGBA")
    # Rows 152-361 hold the wordmark; everything below is the descriptor.
    band = src.crop((0, 0, src.width, 380))
    x0, y0, x1, y1 = ink_bbox(band)
    mark = src.crop((x0, y0, x1, y1))

    h = TILE_CSS_PX * SCALE
    w = max(1, round(h * mark.width / mark.height))
    return save(mark.resize((w, h), Image.LANCZOS), "novasbe.png")


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
    cap_h = round(box_h * 0.71)  # matches the N/V/A cap height in the Nova mark
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
