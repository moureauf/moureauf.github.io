# moureauf.github.io

[![checks](https://github.com/moureauf/moureauf.github.io/actions/workflows/checks.yml/badge.svg)](https://github.com/moureauf/moureauf.github.io/actions/workflows/checks.yml)

Personal homepage — plain HTML/CSS, no framework, no build step.

Custom domain: francoismoureau.com (DNS + HTTPS already configured and live).

Preview locally: `python3 -m http.server` then open http://localhost:8000.

`og.png` (the social-share card) is a 1200×630 screenshot of
`assets/og-card.html` — edit that file and re-screenshot to regenerate.

New post checklist (no build step, so all manual):
1. `writing/<slug>/index.html` — the post itself
2. `writing/index.html` — add it to the list
3. `index.html` — add it to the writing section
4. `sitemap.xml` — add the URL
5. `feed.xml` — add an `<entry>` and bump the feed `<updated>`
