# moureauf.github.io

[![checks](https://github.com/moureauf/moureauf.github.io/actions/workflows/checks.yml/badge.svg)](https://github.com/moureauf/moureauf.github.io/actions/workflows/checks.yml)

Personal homepage — plain HTML/CSS, no framework, no build step.

Custom domain: francoismoureau.com (DNS + HTTPS already configured and live).

Preview locally: `python3 -m http.server` then open http://localhost:8000.

`og.png` (the social-share card) is a 1200×630 screenshot of
`assets/og-card.html` — edit that file and re-screenshot to regenerate.

New post checklist (no build step):
1. `writing/<slug>/index.html` — the post itself
2. `writing/index.html` — add it to the list
3. `index.html` — add it to the writing section
4. `python3 scripts/generate-feeds.py` — regenerates `sitemap.xml` and
   `feed.xml` from the post pages' meta tags (CI fails if out of sync)
5. per-post share card: screenshot
   `assets/og-card-post.html?title=…&date=…&path=writing/<slug>` at
   1200×630 to `writing/<slug>/og.png`, and point the post's
   `og:image` / `twitter:image` at it
