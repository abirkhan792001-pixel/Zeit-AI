#!/usr/bin/env python3
"""
Build Abir Khan's email signature.

Everything is table-based with inline styles and base64 PNGs, because that is
the only markup that survives Gmail, Outlook desktop, Outlook web and Apple
Mail intact. No flexbox, no <style> block, no SVG, no external requests.

Outputs -> signature/dist/
    signature.html          full version, logo marks + contact icons
    signature-minimal.html  no images at all (survives image blocking)
    signature.txt           plain-text fallback
    preview.html            the preview / hand-off page (publishable as-is)
"""
import base64
import html
import os
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(ROOT, "assets")
DIST = os.path.join(ROOT, "dist")

# ---------------------------------------------------------------- palette ---
INK = "#101720"   # name, emphasised words
ROLE = "#2F3845"  # role lines
MUTED = "#5E6875"  # captions, secondary contact text
FAINT = "#9AA4B2"  # separators
ACCENT = "#17405F"  # rail, org names, links

SERIF = "Georgia,'Times New Roman',Times,serif"
SANS = "'Helvetica Neue',Helvetica,Arial,sans-serif"

# ------------------------------------------------------------------ facts ---
NAME = "Abir Khan"
PHONE = "+91 75969 47806"
PHONE_HREF = "tel:+917596947806"
LOCATION = "Munich / Lisbon"
LINKEDIN = "linkedin.com/in/khan-abir"
LINKEDIN_HREF = "https://www.linkedin.com/in/khan-abir"

# (mark, alt, lead, [orgs], footnote, lead_is_label)
# lead_is_label renders the lead as a quiet prefix ("prev.") rather than a role.
ROLES = [
    ("novasbe", "Nova SBE", "MSc. Finance Candidate",
     ["Nova SBE"], "FT RANK #8 WORLDWIDE", False),
    ("scaile", "scaile Technologies", "ex-Founders Associate",
     ["scaile Technologies GmbH"], None, False),
    ("am", "Alvarez &amp; Marsal", "prev.",
     ["Alvarez &amp; Marsal", "ex-VC"], None, True),
]


def b64(name):
    with open(os.path.join(ASSETS, name), "rb") as fh:
        return "data:image/png;base64," + base64.b64encode(fh.read()).decode()


def img(asset, alt, px):
    """An <img> that holds its box in every client: attrs *and* inline style."""
    return (
        f'<img src="{b64(asset)}" width="{px}" height="{px}" alt="{alt}" '
        f'style="display:block;border:0;outline:none;text-decoration:none;'
        f'width:{px}px;height:{px}px;" />'
    )


def table(inner, extra=""):
    return (
        f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" '
        f'style="border-collapse:collapse;{extra}">{inner}</table>'
    )


def spacer(px):
    return f'<tr><td style="font-size:0;line-height:0;height:{px}px;">&nbsp;</td></tr>'


# ------------------------------------------------------------------ rows ----
def role_row(slug, alt, lead, orgs, note, lead_is_label, images=True):
    """One credential line: mark, role, org(s), optional small-caps footnote."""
    dot = f'<span style="color:{FAINT};"> &middot; </span>'
    orgs_html = dot.join(
        f'<span style="font-weight:600;color:{ACCENT};">{o}</span>' for o in orgs
    )
    if lead_is_label:
        # "prev. Alvarez & Marsal · ex-VC" -- no separator after the label.
        text = f'<span style="color:{MUTED};">{lead}</span> {orgs_html}'
    else:
        text = f'<span style="font-weight:600;color:{INK};">{lead}</span>{dot}{orgs_html}'

    body = (
        f'<div style="font-family:{SANS};font-size:13px;line-height:19px;color:{ROLE};">{text}</div>'
    )
    if note:
        body += (
            f'<div style="font-family:{SANS};font-size:10px;line-height:16px;'
            f'letter-spacing:0.7px;color:{MUTED};">{note}</div>'
        )

    if not images:
        # No marks to align to, so the roles sit flush with the contact lines.
        return f'<tr><td style="padding-bottom:6px;">{body}</td></tr>'

    cells = (
        f'<tr>'
        f'<td width="18" valign="top" style="width:18px;padding-top:1px;">{img(slug + ".png", alt, 18)}</td>'
        f'<td width="9" style="width:9px;font-size:0;line-height:0;">&nbsp;</td>'
        f'<td valign="top">{body}</td>'
        f'</tr>'
    )
    return f'<tr><td style="padding-bottom:6px;">{table(cells)}</td></tr>'


def contact_item(asset, alt, text, href, images=True):
    """Icon + label pair, returned as <td>s so the row stays one table."""
    label = (
        f'<span style="font-family:{SANS};font-size:12px;line-height:18px;color:{MUTED};">{text}</span>'
    )
    if href:
        label = (
            f'<a href="{href}" style="font-family:{SANS};font-size:12px;line-height:18px;'
            f'color:{ACCENT};text-decoration:none;">{text}</a>'
        )
    if not images:
        return f'<td valign="middle">{label}</td>'
    return (
        f'<td width="15" valign="middle" style="width:15px;">{img(asset, alt, 15)}</td>'
        f'<td width="7" style="width:7px;font-size:0;line-height:0;">&nbsp;</td>'
        f'<td valign="middle">{label}</td>'
    )


def divider():
    return (
        f'<td style="padding:0 10px;font-family:{SANS};font-size:12px;'
        f'line-height:18px;color:#C7CFDA;">|</td>'
    )


def build(images=True):
    rows = []

    # Name
    rows.append(
        f'<tr><td style="font-family:{SERIF};font-size:22px;line-height:27px;'
        f'font-weight:700;color:{INK};letter-spacing:0.2px;padding-bottom:8px;">{NAME}</td></tr>'
    )
    # Short accent rule, standing in for the user's dashed divider
    rows.append(
        '<tr><td style="font-size:0;line-height:0;padding-bottom:12px;">'
        + table(
            f'<tr><td width="46" height="2" bgcolor="{ACCENT}" '
            f'style="width:46px;height:2px;background-color:{ACCENT};font-size:0;'
            f'line-height:0;">&nbsp;</td></tr>'
        )
        + "</td></tr>"
    )

    for slug, alt, lead, orgs, note, lead_is_label in ROLES:
        rows.append(role_row(slug, alt, lead, orgs, note, lead_is_label, images))

    rows.append(spacer(8))

    # Contact line 1: location | phone
    line1 = (
        "<tr>"
        + contact_item("icon-pin.png", "Location", LOCATION, None, images)
        + divider()
        + contact_item("icon-phone.png", "Phone", PHONE, PHONE_HREF, images)
        + "</tr>"
    )
    rows.append(f'<tr><td style="padding-bottom:4px;">{table(line1)}</td></tr>')

    # Contact line 2: linkedin
    line2 = "<tr>" + contact_item("icon-linkedin.png", "LinkedIn", LINKEDIN, LINKEDIN_HREF, images) + "</tr>"
    rows.append(f"<tr><td>{table(line2)}</td></tr>")

    inner = table("".join(rows))

    # Outer shell: 3px accent rail + content
    shell = (
        "<tr>"
        f'<td width="3" style="width:3px;background-color:{ACCENT};font-size:0;'
        f'line-height:0;">&nbsp;</td>'
        f'<td style="padding-left:18px;">{inner}</td>'
        "</tr>"
    )
    return table(shell, extra="max-width:520px;")


def plain_text():
    return "\n".join(
        [
            NAME,
            "-" * 22,
            "MSc. Finance Candidate | Nova SBE  (FT Rank #8 worldwide)",
            "ex-Founders Associate | scaile Technologies GmbH",
            "prev. Alvarez & Marsal | ex-VC",
            "",
            f"{LOCATION}  |  {PHONE}",
            LINKEDIN_HREF,
        ]
    )


PAGE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>{title}</title></head>
<body style="margin:0;padding:32px;background:#ffffff;">
{sig}
</body></html>
"""

# ------------------------------------------------------------ preview page --
MANIFEST = [
    ("dist/signature.html", "Full signature &mdash; logo marks and contact icons"),
    ("dist/signature-minimal.html", "Same content, no images at all"),
    ("dist/signature.txt", "Plain-text fallback"),
    ("dist/preview.html", "This page"),
    ("build_signature.py", "Builds the three variants and this page"),
    ("build_assets.py", "Rasterises the icons and monogram marks"),
    ("embed_logo.py", "Swaps a real logo file into a mark"),
    ("signature-preview.png", "Rendered preview used by the README"),
]


def human(n):
    return f"{n/1024:.1f} KB" if n >= 1024 else f"{n} B"


def preview_page():
    tpl = open(os.path.join(ROOT, "src", "page.html")).read()

    rows = []
    for rel, what in MANIFEST:
        full = os.path.join(ROOT, rel)
        size = human(os.path.getsize(full)) if os.path.exists(full) else "&mdash;"
        rows.append(f"<tr><td>{rel}</td><td>{what}</td><td class=\"size\">{size}</td></tr>")

    for token, value in [
        ("<!--SIG_FULL-->", build(images=True)),
        ("<!--SIG_MIN-->", build(images=False)),
        ("<!--SIG_TXT-->", html.escape(plain_text())),
        ("<!--MANIFEST-->", "".join(rows)),
        ("<!--BUILD_DATE-->", date.today().strftime("%d %B %Y")),
    ]:
        tpl = tpl.replace(token, value)
    return tpl


if __name__ == "__main__":
    os.makedirs(DIST, exist_ok=True)
    written = []
    for fname, title, imgs in [
        ("signature.html", "Abir Khan — email signature", True),
        ("signature-minimal.html", "Abir Khan — email signature (no images)", False),
    ]:
        path = os.path.join(DIST, fname)
        with open(path, "w") as fh:
            fh.write(PAGE.format(title=title, sig=build(images=imgs)))
        written.append(path)

    txt = os.path.join(DIST, "signature.txt")
    with open(txt, "w") as fh:
        fh.write(plain_text() + "\n")
    written.append(txt)

    # Built last so the manifest can size the files above it. The page lists
    # its own size, so writing it changes it -- rewrite until that settles.
    page = os.path.join(DIST, "preview.html")
    for _ in range(6):
        body = preview_page()
        if os.path.exists(page) and open(page).read() == body:
            break
        with open(page, "w") as fh:
            fh.write(body)
    written.append(page)

    for p in written:
        print(f"  {os.path.relpath(p, ROOT):28} {os.path.getsize(p):>7,} bytes")
