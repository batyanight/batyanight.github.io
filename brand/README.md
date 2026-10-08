# Brand assets

Source and generated files for the chains logo and the LinkedIn banner.
Everything here is deterministic: the same seed and parameters always produce
the same output, so the scripts are the real source of truth and the SVG/PNG
files are just cached renders.

**All rights reserved.** The logo, banner, and generator scripts are not
licensed for reuse. See [`LICENSE`](LICENSE).

```
brand/
├── LICENSE                all rights reserved
├── environment.yml        conda env (numpy, cairosvg)
├── logo/
│   ├── mark.py            logo generator
│   └── mark-*.svg         rendered marks (see table)
└── banner/
    ├── banner.py          LinkedIn banner generator (1584 × 396)
    └── output/            rendered banners, SVG + PNG
```

## Setup

```bash
conda env create -f brand/environment.yml
conda activate brand
```

## Logo

The mark is 40 random walks from a shared centre: a short zigzag flight
outward, then a Gaussian "knot". Colour comes from each chain's length scale
(navy core → burnt-orange rim). The palette is exposed as CSS variables
`--c0`…`--c7` and `--ink`, so a page can retheme it without touching geometry.
The website hero uses the paths from `mark-7202-colour.svg`.

Run from `brand/logo/`:

| File | Command |
|---|---|
| `mark-7202.svg` | `python mark.py --seed 7202 --out mark-7202.svg` |
| `mark-7202-colour.svg` | `python mark.py --seed 7202 --mode length --out mark-7202-colour.svg` |
| `mark-7202-dark.svg` | `python mark.py --seed 7202 --mode dark --out mark-7202-dark.svg` |
| `mark-7202-small.svg` | `python mark.py --seed 7202 --chains 24 --stroke 1.6 --out mark-7202-small.svg` |
| `mark-7201.svg` | `python mark.py --seed 7201 --out mark-7201.svg` |
| `mark-7203.svg` | `python mark.py --seed 7203 --out mark-7203.svg` |

All six were checked to regenerate identically. The committed SVGs also carry
a `<metadata>` provenance block that the script doesn't write; that is the only
difference.

## LinkedIn banner

Same walk logic as the logo, but every chain launches from the centre of the
profile photo (`AVATAR` in `banner.py`), so the fan appears to come out from
behind the photo and sweep right. Chain length tapers with launch steepness so
flat chains run furthest. See the docstring for the details.

Run from `brand/banner/`:

```bash
python banner.py                              # all variants × themes → output/
python banner.py --variant A --theme light    # just one
python banner.py --preview --outdir /tmp/p    # grey disc where the photo sits (for checking, not uploading)
```

| Variant | Settings |
|---|---|
| A | 64 chains, seed 7202, 7 flight steps, bias 0.55 (denser, longer arms) |
| B | 56 chains, seed 7202, defaults |

If LinkedIn changes where the photo sits, re-measure it from a desktop
screenshot and update `AVATAR` (x, y, radius in banner pixels).

Upload the PNG to LinkedIn. The SVGs are for re-rendering at other sizes.
