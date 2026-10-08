# Logo files

Generative radial mark used on batyanight.github.io. Each file is a 200×200 viewBox SVG.

| File | What it is |
|---|---|
| `mark-full-seed7202.svg` | Full hero mark: 40 chains from a common centre, seed 7202, light-mode colour ramp |
| `mark-brand.svg` | 10-chain header mark in deep ink (`#2B3A67`) |
| `mark-brand-currentcolor.svg` | Same header mark using `currentColor`, so it inherits text colour when inlined |
| `favicon.svg` | 8-chain favicon |

These were extracted from `index.html`. The original generator script (`mark.py`, which defines
`RAMP_LIGHT`, `RAMP_DARK`, `INK_LIGHT`, `INK_DARK`, `GROUND_DARK`) is not in this repo yet and
should be added here so the mark can be regenerated.

Colour ramps (c0 → c7):

- Light: `#2B3A67 #2C5480 #2A6E8C #26878A #2E9A6E #5AA243 #96952B #B4552A`
- Dark:  `#7A8FD0 #63A0D2 #4FB4C6 #45C0B0 #4FC98C #85CC55 #D3C24A #E08048`
