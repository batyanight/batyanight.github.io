# batyanight.github.io

Personal site for Batya R. Nightingale, served by GitHub Pages at
<https://batyanight.github.io/>.

## What's here

| Path | What it is |
|---|---|
| `index.html` | The whole website: one self-contained page (inline CSS, inline SVG logo) |
| `og-image.png` | 1200 × 630 link-preview image used by the `og:image` / Twitter card tags |
| `batya-nightingale-cv.md` | CV source text |
| `batya-nightingale-cv.pdf` | Rendered CV, linked from the site's download button |
| `brand/` | Logo and LinkedIn banner generators plus their rendered SVG/PNG output. See [`brand/README.md`](brand/README.md). All rights reserved. |

Every file under the repo root is publicly served by GitHub Pages, including
`brand/` and the CV markdown. Don't commit anything you wouldn't put on the
open web.

## Updating

- **Site text:** edit `index.html`, commit, push to `main`. Pages redeploys in about a minute.
- **CV:** update `batya-nightingale-cv.md`, re-export the PDF under the same filename so the site link keeps working.
- **Logo / banner:** regenerate from the scripts in `brand/` rather than editing the SVGs by hand.
