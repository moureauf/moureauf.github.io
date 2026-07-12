#!/usr/bin/env python3
"""Regenerate sitemap.xml and feed.xml from the post pages.

Each writing/<slug>/index.html is the source of truth: title, description
and date are read from its meta tags. Run from anywhere; writes relative
to the repo root. CI fails if the committed files are out of sync.
"""
import re
import sys
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://francoismoureau.com"


def meta(html, pattern):
    m = re.search(pattern, html)
    if not m:
        return None
    return m.group(1)


def main():
    posts = []
    for page in sorted(ROOT.glob("writing/*/index.html")):
        html = page.read_text(encoding="utf-8")
        slug = page.parent.name
        title = meta(html, r'<meta property="og:title" content="([^"]*)"')
        desc = meta(html, r'<meta name="description" content="([^"]*)"')
        date = meta(html, r'<meta property="article:published_time" content="([^"]*)"')
        if not (title and desc and date):
            sys.exit(f"error: {page} is missing og:title, description or article:published_time")
        posts.append({"slug": slug, "title": title, "desc": desc, "date": date})

    if not posts:
        sys.exit("error: no posts found under writing/*/index.html")
    posts.sort(key=lambda p: (p["date"], p["slug"]), reverse=True)

    urls = [f"{SITE}/", f"{SITE}/writing/"]
    urls += [f"{SITE}/writing/{p['slug']}/" for p in posts]
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sitemap += ["  <url>", f"    <loc>{u}</loc>", "  </url>"]
    sitemap.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")

    updated = max(p["date"] for p in posts)
    feed = ['<?xml version="1.0" encoding="utf-8"?>',
            '<feed xmlns="http://www.w3.org/2005/Atom">',
            "  <title>François Moureau — Writing</title>",
            "  <subtitle>Plain text, git, and tools.</subtitle>",
            f"  <id>{SITE}/</id>",
            f'  <link href="{SITE}/writing/"/>',
            f'  <link rel="self" href="{SITE}/feed.xml"/>',
            f"  <updated>{updated}T00:00:00Z</updated>",
            "  <author>",
            "    <name>François Moureau</name>",
            "  </author>"]
    for p in posts:
        url = f"{SITE}/writing/{p['slug']}/"
        feed += ["  <entry>",
                 f"    <title>{escape(p['title'])}</title>",
                 f"    <id>{url}</id>",
                 f'    <link href="{url}"/>',
                 f"    <published>{p['date']}T00:00:00Z</published>",
                 f"    <updated>{p['date']}T00:00:00Z</updated>",
                 f"    <summary>{escape(p['desc'])}</summary>",
                 "  </entry>"]
    feed.append("</feed>")
    (ROOT / "feed.xml").write_text("\n".join(feed) + "\n", encoding="utf-8")

    print(f"wrote sitemap.xml ({len(urls)} urls) and feed.xml ({len(posts)} entries)")


if __name__ == "__main__":
    main()
