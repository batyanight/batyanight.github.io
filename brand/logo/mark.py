#!/usr/bin/env python3
"""
mark.py — generate the "chains" mark as a standalone SVG.

The mark is N independent random walks starting at a common centre.
Each walk has two phases:

  flight — a few long, sharply-turning steps that carry it outward.
           Turn direction alternates sign, so the path zigzags while
           its net motion stays radial. Step length grows with each
           step, which is what makes the centre quiet and the rim busy.

  knot   — many small Gaussian steps in place, which tangle into a
           dense scribble. This is what saturates the outer region
           once you have enough chains.

Every chain also gets a random length scale, so knots land at
different radii and the rim reads as a gradient rather than a ring.

Colour is optional and is mapped from each chain's own length scale,
not from position. Short arms physically cannot reach far, so this
produces a cool-centre / warm-rim gradient for free, with no need to
split any path.

Usage
-----
    python mark.py --seed 7202 --out mark-7202.svg
    python mark.py --seed 7202 --mode length --out mark-colour.svg
    python mark.py --seed 7202 --mode dark   --out mark-dark.svg
    python mark.py --seed 7202 --chains 24 --stroke 1.6 --out mark-small.svg

Requires: numpy
"""

import argparse
import numpy as np

# --- palettes -------------------------------------------------------------
# Eight stops, cool to warm. The light and dark sets are the same hues with
# lightness shifted, so a mark keeps its identity on either ground.
RAMP_LIGHT = ["#2B3A67", "#2C5480", "#2A6E8C", "#26878A",
              "#2E9A6E", "#5AA243", "#96952B", "#B4552A"]
RAMP_DARK = ["#7A8FD0", "#63A0D2", "#4FB4C6", "#45C0B0",
             "#4FC98C", "#85CC55", "#D3C24A", "#E08048"]

INK_LIGHT = "#1B2430"
INK_DARK = "#C6CDD6"
GROUND_DARK = "#11161C"


def make_chains(n, seed, flight_steps=4, knot_steps=11, knot_sigma=2.9,
                scale_range=(0.52, 1.30), turn_range=(0.40, 0.95),
                extent=96.0, box=200.0):
    """Return (scales, coords) where coords has shape (n, points, 2).

    scale_range is the single biggest lever on how balanced a seed looks.
    Wide (0.52, 1.30) gives a deep, uneven rim and high variance between
    seeds. Narrow (0.70, 1.15) gives a rim that closes evenly every time
    but loses some of the depth.
    """
    rng = np.random.default_rng(seed)
    centre = box / 2.0
    sector = 2 * np.pi / n
    scales, chains = [], []

    for i in range(n):
        # Evenly spaced launch directions, jittered within the chain's own
        # sector so the spokes do not look mechanical. No hard clamp: chains
        # are allowed to cross into their neighbours, and that crossing is
        # what builds density at the rim.
        base = 2 * np.pi * i / n + rng.uniform(-0.55, 0.55) * sector - np.pi / 2
        scale = rng.uniform(*scale_range)

        p = np.array([centre, centre], dtype=float)
        pts = [tuple(p)]
        sign = 1
        for j in range(flight_steps):
            # Step length grows along the flight: short near the centre,
            # long at the rim.
            length = scale * (11 + 19 * ((j + 1) / flight_steps) ** 1.15
                              * rng.uniform(0.7, 1.3))
            theta = base + sign * rng.uniform(*turn_range)
            sign = -sign
            p = p + length * np.array([np.cos(theta), np.sin(theta)])
            pts.append(tuple(p))

        for _ in range(knot_steps):
            p = p + rng.normal(0, knot_sigma, 2)
            pts.append(tuple(p))

        scales.append(scale)
        chains.append(np.array(pts))

    coords = np.stack(chains)

    # Normalise so the furthest point sits at `extent` from centre. This keeps
    # every seed inside the same frame without altering any shape.
    v = coords - centre
    r = np.hypot(v[..., 0], v[..., 1])
    coords = centre + v * (extent / r.max())
    return np.array(scales), coords


def fmt(v):
    s = f"{v:.1f}"
    return s[:-2] if s.endswith(".0") else s


def to_svg(scales, coords, mode="mono", stroke=0.8, box=200.0, seed=None):
    lo, hi = scales.min(), scales.max()
    ramp = RAMP_DARK if mode == "dark" else RAMP_LIGHT

    # Palette exposed as CSS custom properties so a project can retheme the
    # mark without touching geometry: override --c0..--c7 (and --ink) in the
    # host page or in this file's <style> block.
    tokens = "\n".join(f"    --c{i}: {c};" for i, c in enumerate(ramp))
    ink = INK_DARK if mode == "dark" else INK_LIGHT

    out = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {fmt(box)} {fmt(box)}"',
        f'     role="img" aria-label="Generative chains mark{"" if seed is None else f", seed {seed}"}">',
        "  <style>",
        "  svg {",
        tokens,
        f"    --ink: {ink};",
        "  }",
        "  </style>",
    ]
    if mode == "dark":
        out.append(f'  <rect width="{fmt(box)}" height="{fmt(box)}" fill="{GROUND_DARK}"/>')
    out.append(f'  <g fill="none" stroke-width="{stroke}" '
               'stroke-linejoin="round" stroke-linecap="round">')

    for scale, pts in zip(scales, coords):
        d = "M" + " L".join(f"{fmt(x)} {fmt(y)}" for x, y in pts)
        if mode == "mono":
            colour = "var(--ink)"
        else:
            k = min(len(ramp) - 1, int((scale - lo) / (hi - lo + 1e-9) * len(ramp)))
            colour = f"var(--c{k})"
        out.append(f'    <path stroke="{colour}" d="{d}"/>')

    out += ["  </g>", "</svg>", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seed", type=int, default=7202)
    ap.add_argument("--chains", type=int, default=40)
    ap.add_argument("--mode", choices=("mono", "length", "dark"), default="mono")
    ap.add_argument("--stroke", type=float, default=0.8)
    ap.add_argument("--knot-steps", type=int, default=11)
    ap.add_argument("--scale-min", type=float, default=0.52)
    ap.add_argument("--scale-max", type=float, default=1.30)
    ap.add_argument("--out", default="mark.svg")
    a = ap.parse_args()

    scales, coords = make_chains(
        a.chains, a.seed,
        knot_steps=a.knot_steps,
        scale_range=(a.scale_min, a.scale_max),
    )
    svg = to_svg(scales, coords, mode=a.mode, stroke=a.stroke, seed=a.seed)
    with open(a.out, "w") as fh:
        fh.write(svg)
    print(f"wrote {a.out}  (seed {a.seed}, {a.chains} chains, mode {a.mode})")


if __name__ == "__main__":
    main()
