# moureauf.github.io

Personal homepage. Plain static HTML/CSS, no framework, no build step —
served directly by GitHub Pages.

- `index.html` — the whole site (single page)
- `css/styles.css` — all styles, incl. `@font-face` declarations
- `fonts/` — self-hosted woff2 fonts (Inter, subset; JetBrains Mono, subset).
  See `fonts/*-OFL.txt` for license text (SIL Open Font License).
- `writing/` — scaffold for a future `/writing/` posts section (see `writing/README.md`).
  No posts yet.

## Custom domain (francoismoureau.com)

`CNAME` in this repo is already set to `francoismoureau.com`, and GitHub Pages
is confirmed serving from the `master` branch, root (`/`), with HTTPS enforced
and the certificate approved.

The one DNS record to set at your registrar/DNS provider (if not already
present): an **apex `ALIAS`/`ANAME`/flattened `CNAME` record** for
`francoismoureau.com` pointing at `moureauf.github.io`. If your DNS provider
doesn't support apex ALIAS records, use four `A` records at the apex instead,
pointing at GitHub Pages' IPs:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

(Optional) add a `CNAME` record for `www` → `moureauf.github.io` if you want
`www.francoismoureau.com` to resolve too — GitHub's cert already covers it.
