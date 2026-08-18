# Deck slides as SVG

Thirteen slides, one SVG each, at **1920 × 1080**. Two variants of the same artwork —
pick per slide, they are interchangeable.

| Folder | Text is | Use it when |
|---|---|---|
| **`outlined/`** | vector outlines | You want it to look exactly right the moment you paste. Nothing depends on fonts being installed. Text is no longer editable. |
| **`editable/`** | live text in Inter | You want to retype copy inside Figma. Requires Inter, which Figma ships with by default. |

**Pasting into Figma:** drag the `.svg` file onto the canvas, or open the file in a text
editor, copy everything, and paste straight into Figma — both produce the same frame. Each
lands as a 1920 × 1080 group; wrap it in a frame of the same size to make it a slide.

**The logo** rides along inside every file as an embedded image, so nothing links out and the
files stay self-contained.

Regenerate after editing the deck: print `alsvid-ai-leadership-deck.html` to PDF at
1920 × 1080 with backgrounds on, then split the pages. The `@page` rule in the deck's
stylesheet already sets that size.
