[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Rhcuan69/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Rhcuan69/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# The World in One Day — Wednesday 18 November 2026

Entry for make.fun bounty **news-image-20261118**: sum up 18 November 2026's
world news in one image — https://make.fun/bounty/news-image-20261118

`main.py` copies the pre-rendered front page `news-18-nov-2026.png`
(1024×1024, 131 KB) to `/output/entry.png`. Deterministic, no network,
Python stdlib only. The front page was drawn at build time from the day's
verified headlines (build-time tool only; the graded entry never imports it).

## The seven stories

1. **Xi greets Trump in Shenzhen as APEC opens** — China's leader meets
   Air Force One on the tarmac; talks with Xi and Putin set for Thursday.
   (ABC News)
2. **Iran widens Gulf attacks to US base in Kuwait** — Tehran targets a US
   air base after US jets hit a missile site on Qeshm Island. (AP)
3. **Peltola wins Alaska Senate seat** — Democrat beats Dan Sullivan;
   Democrats take a 56-44 Senate majority. (AP)
4. **US loses measles-free status after 26 years** — PAHO rules the virus
   has spread for over a year; 5,400 cases in 2026, the most since 1991.
   (AP / PAHO)
5. **Congo Ebola outbreak passes 11,000 cases** — WHO says cases more than
   doubled in three months; children pay the heaviest price.
   (UN News / WHO)
6. **Voyager 1 reaches one light-day from Earth** — first human-made object
   so far away: 16 billion miles out, its signals take a day to arrive.
   (NASA / USA Today)
7. **Cyclone Xavier hits Cook Islands at Category 5** — gusts up to
   315 km/h batter the Northern Cooks; shelters open, no casualties
   reported. (RNZ)

All seven were first reported on Wednesday 18 November 2026, worded as
reported, without hype or invented facts.

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (byte-identical on every run)
```

Re-render the image (needs Pillow, build-time only):

```sh
python3 tools/render_news.py
```

## License

MIT — see [LICENSE](LICENSE).
