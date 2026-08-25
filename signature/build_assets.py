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
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
LOGOS = os.path.join(SRC, "logos")
OUT = os.path.join(ROOT, "assets")

SCALE = 3          # 3x for retina
ALPHA_LEVELS = 16  # these are flat-colour shapes; smooth alpha just costs bytes

ICON_COLOR = "#3E6485"   # mid-tone: legible on white AND on dark-mode grounds
ICON_CSS_PX = 15
TILE_CSS_PX = 18

# Official logo marks, from the artwork in src/logos/. scaile and A&M are
# full-bleed square tiles used as supplied; the Nova SBE file is the full
# lockup, so only its wordmark band is used (see render_nova).
TILE_LOGOS = ["scaile", "am"]


def ink_bbox(img):
    """Bounding box of the visible ink, whatever the source's background is."""
    flat = Image.alpha_composite(Image.new("RGBA", img.size, (255,) * 4), img).convert("L")
    w, h = flat.size
    px = flat.load()
    xs = [x for x in range(w) if any(px[x, y] < 128 for y in range(h))]
    ys = [y for y in range(h) if any(px[x, y] < 128 for x in range(w))]
    return xs[0], ys[0], xs[-1] + 1, ys[-1] + 1


def scale_to_line(mark, name):
    """Resize a mark to the signature's line height, keeping its aspect ratio."""
    h = TILE_CSS_PX * SCALE
    w = max(1, round(h * mark.width / mark.height))
    return save(mark.resize((w, h), Image.LANCZOS), name)


def render_nova():
    """Crop the wordmark out of the official logo and set it to the line height.

    The source is the full lockup; its descriptor line ("NOVA SCHOOL OF
    BUSINESS & ECONOMICS") is two 23px lines in a 630px image -- under 2px
    tall at signature size -- so the wordmark stands alone, which is how the
    mark is meant to be set when small.
    """
    src = Image.open(os.path.join(LOGOS, "nova-sbe-source.png")).convert("RGBA")
    # Rows 152-361 hold the wordmark; everything below is the descriptor.
    band = src.crop((0, 0, src.width, 380))
    return scale_to_line(src.crop(ink_bbox(band)), "novasbe.png")


def render_tile(slug):
    """An official square mark, trimmed of any padding and set to line height."""
    src = Image.open(os.path.join(LOGOS, f"{slug}-source.png")).convert("RGBA")
    return scale_to_line(src.crop(ink_bbox(src)), f"{slug}.png")


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


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    built = [
        render_nova(),
        render_icon("map-pin", "icon-pin.png"),
        render_icon("phone", "icon-phone.png"),
        render_icon("linkedin", "icon-linkedin.png"),
    ]
    built += [render_tile(slug) for slug in TILE_LOGOS]
    for name, size in built:
        print(f"  {name:22} {size[0]}x{size[1]}")
    print(f"{len(built)} assets -> {OUT}")
