#!/usr/bin/env python3
"""
banner.py — generate the LinkedIn banner (1584 x 396) from the logo's chain logic.

Same two-phase random walk as ../logo/mark.py (zigzag flight outward, then a
Gaussian knot), same length-mapped colour ramp. The difference is where the
chains start and which way they go:

  * Every chain launches from the centre of the LinkedIn profile photo
    (AVATAR below), so the first stretch of each walk is hidden behind the
    photo and the fan appears to erupt from behind it, sweeping right.
  * Most chains (right_frac) launch into a wedge pointing up-right; a few
    short ones launch up-left so small sprigs break over the photo's rim.
  * Chain length tapers with launch steepness:
        length factor = (1 - taper) + taper * cos(angle)^2
    so near-horizontal chains run furthest and near-vertical ones stay short.
    That is what lets the fan fill a 4:1 strip without stretching any
    individual shape much.
  * `bias` > 1 or < 1 pushes the right-wedge launch angles toward the
    steep or the flat end of the wedge.

Variants (as delivered on 2026-10-03):
    A  64 chains, seed 7202, 7 flight steps, bias 0.55  (denser, longer arms)
    B  56 chains, seed 7202, defaults

Usage
-----
    python banner.py                         # all variants, light + dark, SVG + PNG
    python banner.py --variant A --theme dark
    python banner.py --preview               # also draw the avatar disc as a grey circle
    python banner.py --no-png                # SVG only (no cairosvg needed)

Requires: numpy; cairosvg for PNG output.
Determinism: numpy.random.default_rng(seed) is stable across numpy versions,
so the same seed + parameters always produce the same banner.
"""

import argparse
from pathlib import Path

import numpy as np

W, H = 1584, 396                 # LinkedIn banner spec
AVATAR = (203, 358, 155)         # profile photo centre x, y and radius, in banner px,
                                 # measured off a desktop LinkedIn screenshot
RIGHT_MARGIN, TOP_MARGIN = 36, 28

RAMP_LIGHT = ["#2B3A67", "#2C5480", "#2A6E8C", "#26878A",
              "#2E9A6E", "#5AA243", "#96952B", "#B4552A"]
RAMP_DARK = ["#7A8FD0", "#63A0D2", "#4FB4C6", "#45C0B0",
             "#4FC98C", "#85CC55", "#D3C24A", "#E08048"]

THEMES = {
    #         ramp        ground     stroke
    "light": (RAMP_LIGHT, "#F2F4F6", 2.4),
    "dark":  (RAMP_DARK,  "#11161C", 2.2),
}

VARIANTS = {
    "A": dict(n=64, seed=7202, bias=0.55, flight_steps=7),
    "B": dict(n=56, seed=7202),
}


def emanate(n, seed, right_frac=0.86, right_wedge=(-68, -2), left_wedge=(-92, -138),
            flight_steps=6, knot_steps=9, knot_sigma=2.8, turn_range=(0.32, 0.78),
            scale_right=(0.60, 1.40), scale_left=(0.35, 0.60), taper=0.85, bias=0.65):
    """Return (scales, coords); coords has shape (n, points, 2), origin at (0, 0).

    Angles are in degrees, SVG convention (y points down, so negative = upward).
    """
    rng = np.random.default_rng(seed)
    scales, chains = [], []
    n_r = int(round(n * right_frac))
    n_l = n - n_r
    groups = [(right_wedge, scale_right, n_r, bias),
              (left_wedge, scale_left, n_l, 1.0)]

    for (w0, w1), srange, m, b in groups:
        for i in range(m):
            # spread launch angles evenly across the wedge, jittered, then skewed by `b`
            frac = np.clip((i + rng.uniform(-0.45, 0.45)) / max(m - 1, 1), 0, 1) ** b
            base = np.radians(w0 + (w1 - w0) * frac)
            s = rng.uniform(*srange) * ((1 - taper) + taper * np.cos(base) ** 2)

            p = np.zeros(2)
            pts = [tuple(p)]
            sign = 1
            for j in range(flight_steps):
                length = s * (11 + 19 * ((j + 1) / flight_steps) ** 1.15
                              * rng.uniform(0.7, 1.3))
                theta = base + sign * rng.uniform(*turn_range)
                sign = -sign
                p = p + length * np.array([np.cos(theta), np.sin(theta)])
                pts.append(tuple(p))

            for _ in range(knot_steps):
                p = p + rng.normal(0, knot_sigma, 2)
                pts.append(tuple(p))

            scales.append(s)
            chains.append(np.array(pts))

    return np.array(scales), np.stack(chains)


def place(coords, ox, oy, reach_x, reach_up, cap=1.5):
    """Scale chains so the highest point reaches `reach_up` above the origin and the
    rightmost reaches `reach_x` right of it, with x stretched at most `cap` times y."""
    x, y = coords[..., 0], coords[..., 1]
    ky = reach_up / max(-y.min(), 1e-6)
    kx = min(reach_x / max(x.max(), 1e-6), ky * cap)
    out = coords.copy()
    out[..., 0] = x * kx + ox
    out[..., 1] = y * ky + oy
    return out


def paths(scales, coords, ramp):
    """One <path> per chain, coloured by its length scale (short = cool, long = warm)."""
    lo, hi = scales.min(), scales.max()
    out = []
    for s, pts in zip(scales, coords):
        idx = int(round((s - lo) / (hi - lo) * (len(ramp) - 1))) if hi > lo else 0
        d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
        out.append(f'<path stroke="{ramp[idx]}" d="{d}"/>')
    return "".join(out)


def build(params, theme, preview=False):
    ramp, ground, stroke = THEMES[theme]
    ax, ay, ar = AVATAR
    scales, coords = emanate(**params)
    coords = place(coords, ax, ay, W - RIGHT_MARGIN - ax, ay - TOP_MARGIN)
    disc = (f'<circle cx="{ax}" cy="{ay}" r="{ar}" fill="#8A8F94"/>' if preview else "")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'width="{W}" height="{H}">'
            f'<rect width="{W}" height="{H}" fill="{ground}"/>'
            f'<g fill="none" stroke-width="{stroke}" stroke-linejoin="round" '
            f'stroke-linecap="round">{paths(scales, coords, ramp)}</g>{disc}</svg>')


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--variant", choices=sorted(VARIANTS), action="append",
                    help="repeatable; default: all")
    ap.add_argument("--theme", choices=sorted(THEMES), action="append",
                    help="repeatable; default: all")
    ap.add_argument("--outdir", default=Path(__file__).resolve().parent / "output",
                    type=Path)
    ap.add_argument("--preview", action="store_true",
                    help="draw the avatar footprint as a grey disc (not for upload)")
    ap.add_argument("--no-png", action="store_true")
    a = ap.parse_args()

    a.outdir.mkdir(parents=True, exist_ok=True)
    for v in a.variant or sorted(VARIANTS):
        for t in a.theme or sorted(THEMES):
            name = f"linkedin-banner-{v}-{t}" + ("-preview" if a.preview else "")
            svg = build(VARIANTS[v], t, preview=a.preview)
            (a.outdir / f"{name}.svg").write_text(svg)
            if not a.no_png:
                import cairosvg
                cairosvg.svg2png(bytestring=svg.encode(),
                                 write_to=str(a.outdir / f"{name}.png"),
                                 output_width=W, output_height=H)
            print(f"wrote {a.outdir / name}.svg" + ("" if a.no_png else " + .png"))


if __name__ == "__main__":
    main()
