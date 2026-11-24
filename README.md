# news-image-20261124-entry

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Van7art/news-image-20261124-entry/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Van7art/news-image-20261124-entry/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A one-image summary of the world's news on Tuesday 24 November 2026, drawn
as a classic broadsheet front page titled **THE WORLD**. Variant A of the
news-image-20261124 entry for make.fun.

## The image

`entry.png` (1024×1024) is a newspaper front page titled **THE WORLD**:

- **Lead story:** Ukraine sinks a Russian warship off Libya — Zelenskyy
  confirms naval drones sank the corvette Merkury at Benghazi. Illustrated
  with a drawn harbour scene (PIL shapes only; no photographs, no real
  people depicted).
- **The day in brief:** nine further stories in a 3×3 grid, each with a
  short headline, a one-line deck, and a small drawn icon.
- **Also today:** fourteen nations back the ICJ genocide ruling on Myanmar,
  and a magnitude 5.6 earthquake strikes Nepal near the China border.

## Stories covered

1. Ukraine sinks Russian warship off Libya (Zelenskyy confirms)
2. NATO vows to defend space as Russia nuclear-satellite reports alarm allies
3. China sentences official to death for spying
4. US drone helped catch "El Chapo Isidro"; Mexico to try him
5. Russian strike on Zaporizhzhia kills 2, wounds 22
6. Huang returns to Nvidia; markets surge
7. Russian aircraft enter South Korea air-defence zone
8. Pentagon rebukes Canada over defence spending, F-35 review
9. US blacklists Megaspeed in Nvidia spy scandal
10. Zelenskyy urges four-way peace talks "as soon as possible"
11. Fourteen nations back ICJ genocide ruling on Myanmar
12. Nepal earthquake, magnitude 5.6, near China border

All twelve stories are from Tuesday 24 November 2026. See `NOTES.md` for
one-line source notes.

## Run it

```sh
python3 vA/gen.py           # regenerate entry.png (needs Pillow)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` uses only the Python standard library and copies the bundled
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). It
needs no network access and is fully deterministic — repeated runs write
identical bytes.

## Variants

- `vA/` — broadsheet front page (this entry, chosen)
- `vB/` — magazine cover with hero scene and numbered cover lines
- `vC/` — world map with numbered story pins and a listed index

## License

MIT — see `LICENSE`.

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
