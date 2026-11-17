#!/usr/bin/env python3
"""build_site.py - renders the Wave 1 corpus to static, server-rendered HTML in _site/.

Two modes:
  --preview     the private reading copy for the gate B and gate C readers (docs/13_WAVE1_READINESS.md): relative
                links, a PREVIEW banner on every page, noindex on every page, no sitemap, no identifier resolver.
  (default)     the production layout for phase A: absolute canonical URLs, and an Apache .htaccess carrying the
                identifier resolver /id/<PUBID> -> 302 to the canonical URL (docs/06_CANONICAL_URL_MAP.md).

Only register entries with publish = true and their content files are rendered; nothing else in content/ is read,
so a held document cannot leak into the build. The text is rendered as written: no word is added, removed or
reordered, and the claim-class tags stay visible. Output is never committed (.gitignore: /_site/).

Usage:
  python3 scripts/build_site.py --preview [--out _site]
  python3 scripts/build_site.py [--out _site]
  python3 scripts/build_site.py --check        builds into a temporary folder and checks the result
"""
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

try:
    import markdown  # python-markdown 3.x
except ImportError:  # pragma: no cover
    sys.exit("build_site: python-markdown is required (pip install markdown)")

ROOT = Path(__file__).resolve().parent.parent
HOST = "https://neoai.myneogroup.com"
ARCHIVE_CSS = ROOT / "archive/superseded/neoai.myneogroup.com_research-delta-v1.0.0/assets/css/research.min.css"
SITE_PAGES = [  # (content file, route, title)
    ("content/site/neoai/research/methodology.md", "/research/methodology/", "Methodology"),
    ("content/site/neoai/research/capability-register.md", "/research/capability-register/", "Capability Register"),
]
CATEGORY_TITLES = {"papers": "Research papers", "technical-notes": "Technical notes", "institutional": "Institutional"}
CLAIM = {"E": "Established", "A": "Architectural interpretation", "D": "Design intent", "O": "Open problem"}

BASE_CSS = """
:root{--bg:#0b0d10;--fg:#e8ecf1;--muted:#9aa4b2;--line:#252b33;--accent:#7cc4ff;--warn:#f5c26b}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 Inter,system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
a{color:var(--accent)}main{max-width:860px;margin:0 auto;padding:32px 20px 80px}
h1,h2,h3{font-family:"Space Grotesk",Inter,system-ui,sans-serif;line-height:1.25}h1{font-size:2rem}h2{margin-top:2.2em;border-top:1px solid var(--line);padding-top:1em}
table{border-collapse:collapse;width:100%;margin:1em 0;font-size:.92rem}th,td{border:1px solid var(--line);padding:6px 9px;vertical-align:top;text-align:left}th{background:#12161b}
code{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:.88em;background:#151a20;padding:1px 4px;border-radius:4px}
pre{overflow:auto;background:#151a20;padding:12px;border-radius:6px}
.p-banner{position:sticky;top:0;z-index:9;background:var(--warn);color:#1b1300;font-weight:600;text-align:center;padding:8px 12px;font-size:.9rem}
.p-nav{border-bottom:1px solid var(--line);padding:12px 20px;display:flex;gap:18px;flex-wrap:wrap;font-size:.92rem}
.p-meta{color:var(--muted);font-size:.9rem}.cc{font-family:"JetBrains Mono",monospace;font-size:.78em;padding:1px 5px;border-radius:4px;border:1px solid var(--line);white-space:nowrap}
.cc-E{color:#8be28b}.cc-A{color:#7cc4ff}.cc-D{color:#f5c26b}.cc-O{color:#ff9a9a}
.p-list li{margin:.5em 0}footer{border-top:1px solid var(--line);color:var(--muted);font-size:.85rem;padding:20px;text-align:center}
"""


def load_register() -> list[dict]:
    data = json.loads((ROOT / "registers/publications.json").read_text(encoding="utf-8"))
    return [e for e in data["entries"] if e.get("publish") is True]


def strip_front_matter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text


def tag_claims(rendered: str) -> str:
    """`[E]` etc. are rendered as <code>[E]</code>; give them a visible class without changing the text."""
    def repl(m: re.Match[str]) -> str:
        k = m.group(1)
        return f'<span class="cc cc-{k}" title="{CLAIM[k]}">[{k}]</span>'
    return re.sub(r"<code>\[([EADO])\]</code>", repl, rendered)


def rewrite_links(rendered: str, route: str, preview: bool) -> str:
    """Absolute links to the canonical host become relative in the preview, so the copy reads offline."""
    if not preview:
        return rendered
    depth = len([p for p in route.strip("/").split("/") if p])
    up = "../" * depth

    def repl(m: re.Match[str]) -> str:
        path = m.group(2)
        target = path.lstrip("/")
        if target and not target.endswith("/") and "." not in target.split("/")[-1]:
            target += "/"
        return f'{m.group(1)}"{up}{target}index.html"' if target.startswith("research/") or target == "" else m.group(0)
    rendered = re.sub(r'(href=)"' + re.escape(HOST) + r'(/[^"#]*)"', repl, rendered)
    return re.sub(r'(href=)"(/research/[^"#]*)"', repl, rendered)


def md_to_html(text: str) -> str:
    return markdown.markdown(strip_front_matter(text), extensions=["tables", "fenced_code", "sane_lists"], output_format="html5")


def page(title: str, body: str, route: str, preview: bool, canonical: str | None) -> str:
    depth = len([p for p in route.strip("/").split("/") if p])
    up = "../" * depth if preview else "/"
    home = f"{up}research/index.html" if preview else "/research/"
    robots = "noindex, nofollow" if preview else "index, follow, max-snippet:-1"
    canon = "" if preview or canonical is None else f'<link rel="canonical" href="{html.escape(canonical)}">'
    banner = ('<div class="p-banner">PREVIEW - NOT PUBLISHED. Private reading copy for the independent readers '
              '(gate B and gate C). Do not share or cite.</div>') if preview else ""
    css = f"{up}assets/css/preview.css" if preview else "/assets/css/research-wave1.css"
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} - NEO AI Research</title><meta name="robots" content="{robots}">{canon}
<link rel="stylesheet" href="{css}"></head>
<body>{banner}
<nav class="p-nav" aria-label="Research"><a href="{home}">Research library</a><a href="{up}research/methodology/index.html" >Methodology</a><a href="{up}research/capability-register/index.html">Capability Register</a></nav>
<main id="main">
{body}
</main>
<footer>NEO AI is operated by NEO TECH LABS TECHNOLOGY L.L.C, a subsidiary of My NEO Group. Research content is licensed CC BY 4.0.
Nothing in this corpus describes a deployed system unless its capability status says so.</footer>
</body></html>
""".replace('index.html" >', 'index.html">') if preview else f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} - NEO AI Research</title><meta name="robots" content="{robots}">{canon}
<link rel="stylesheet" href="{css}"></head>
<body>
<nav class="p-nav" aria-label="Research"><a href="/research/">Research library</a><a href="/research/methodology/">Methodology</a><a href="/research/capability-register/">Capability Register</a></nav>
<main id="main">
{body}
</main>
<footer>NEO AI is operated by NEO TECH LABS TECHNOLOGY L.L.C, a subsidiary of My NEO Group. Research content is licensed CC BY 4.0.
Nothing in this corpus describes a deployed system unless its capability status says so.</footer>
</body></html>
"""


def write(out: Path, route: str, content: str) -> Path:
    target = out / route.strip("/") / "index.html" if route.strip("/") else out / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    return target


def build(out: Path, preview: bool) -> dict:
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    entries = load_register()
    rendered: list[dict] = []
    for e in entries:
        src = ROOT / e["content_path"]
        if not src.is_file():
            raise SystemExit(f"build_site: {e['id']}: content file missing: {e['content_path']}")
        route = e["canonical_url"].replace(HOST, "")
        body = rewrite_links(tag_claims(md_to_html(src.read_text(encoding="utf-8"))), route, preview)
        head = (f'<p class="p-meta">{html.escape(CATEGORY_TITLES.get(e["category_slug"], e["category_slug"]))} &middot; '
                f'{html.escape(e["id"])} &middot; {html.escape(str(e.get("version") or ""))} &middot; register status '
                f'{html.escape(e["status"])}</p>')
        write(out, route, page(e["title"], head + body, route, preview, e["canonical_url"]))
        rendered.append({"id": e["id"], "title": e["title"], "route": route, "category": e["category_slug"]})
    for rel, route, title in SITE_PAGES:
        body = rewrite_links(tag_claims(md_to_html((ROOT / rel).read_text(encoding="utf-8"))), route, preview)
        write(out, route, page(title, body, route, preview, HOST + route))
    # library index: what exists, grouped, no count presented as an achievement (gate C)
    items = []
    for cat in ("institutional", "papers", "technical-notes"):
        group = [r for r in rendered if r["category"] == cat]
        if not group:
            continue
        lis = "".join(
            f'<li><a href="{(".." + r["route"] + "index.html") if preview else r["route"]}">{html.escape(r["title"])}</a> '
            f'<span class="p-meta">{html.escape(r["id"])}</span></li>' for r in group)
        items.append(f"<h2>{html.escape(CATEGORY_TITLES[cat])}</h2><ul class=\"p-list\">{lis}</ul>")
    intro = ("<h1>Research library</h1><p>The public research corpus of the NEO AI Research Program. Every material "
             "statement carries a claim class: <span class=\"cc cc-E\">[E]</span> established, <span class=\"cc cc-A\">[A]</span> "
             "architectural interpretation, <span class=\"cc cc-D\">[D]</span> design intent with a capability status, "
             "<span class=\"cc cc-O\">[O]</span> open problem.</p>")
    write(out, "/research/", page("Research library", intro + "".join(items), "/research/", preview, HOST + "/research/"))
    css_dir = out / "assets/css"
    css_dir.mkdir(parents=True, exist_ok=True)
    (css_dir / ("preview.css" if preview else "research-wave1.css")).write_text(BASE_CSS.strip() + "\n", encoding="utf-8")
    if preview:
        (out / "index.html").write_text('<!DOCTYPE html><meta charset="UTF-8"><meta name="robots" content="noindex, nofollow">'
                                        '<meta http-equiv="refresh" content="0; url=research/index.html">'
                                        '<a href="research/index.html">Research library (preview)</a>\n', encoding="utf-8")
        (out / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
    else:
        rules = ["# Identifier resolver (docs/06_CANONICAL_URL_MAP.md): /id/<PUBID> -> 302 to the canonical URL", "RewriteEngine On"]
        for e in entries:
            rules.append(f"RewriteRule ^id/{re.escape(e['id'])}/?$ {e['canonical_url']} [R=302,L]")
        (out / ".htaccess").write_text("\n".join(rules) + "\n", encoding="utf-8")
    return {"documents": len(rendered), "pages": len(rendered) + len(SITE_PAGES) + 1, "mode": "preview" if preview else "production"}


def check(out: Path, preview: bool) -> list[str]:
    problems: list[str] = []
    entries = load_register()
    for e in entries:
        route = e["canonical_url"].replace(HOST, "")
        f = out / route.strip("/") / "index.html"
        if not f.is_file():
            problems.append(f"{e['id']}: page missing at {route}")
            continue
        t = f.read_text(encoding="utf-8")
        if preview and ("noindex" not in t or "PREVIEW - NOT PUBLISHED" not in t):
            problems.append(f"{e['id']}: preview page without noindex or banner")
        if not preview and f'<link rel="canonical" href="{e["canonical_url"]}">' not in t:
            problems.append(f"{e['id']}: canonical link missing")
        # the source text survives: every heading of the source appears in the page
        src = strip_front_matter((ROOT / e["content_path"]).read_text(encoding="utf-8"))
        for h in re.findall(r"^#{1,3} (.+)$", src, flags=re.M):
            plain = re.sub(r"[`*_]", "", h).strip()
            if html.escape(plain, quote=False) not in t and plain not in t:
                problems.append(f"{e['id']}: heading not rendered: {plain[:60]}")
    held = [e for e in json.loads((ROOT / "registers/publications.json").read_text(encoding="utf-8"))["entries"] if not e.get("publish")]
    for e in held:
        route = e["canonical_url"].replace(HOST, "")
        if (out / route.strip("/") / "index.html").exists():
            problems.append(f"{e['id']}: held document rendered")
    if not preview:
        ht = (out / ".htaccess").read_text(encoding="utf-8")
        for e in entries:
            if f"^id/{re.escape(e['id'])}/?$ {e['canonical_url']} [R=302,L]" not in ht:
                problems.append(f"{e['id']}: identifier route missing")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--preview", action="store_true")
    ap.add_argument("--out", default=str(ROOT / "_site"))
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if a.check:
        failures: list[str] = []
        for preview in (True, False):
            with tempfile.TemporaryDirectory() as tmp:
                out = Path(tmp) / "site"
                build(out, preview)
                failures += [("preview: " if preview else "production: ") + p for p in check(out, preview)]
        for f in failures:
            print("FAIL", f)
        print(f"build_site --check: {'OK' if not failures else str(len(failures)) + ' problem(s)'}")
        return 1 if failures else 0
    info = build(Path(a.out), a.preview)
    problems = check(Path(a.out), a.preview)
    for p in problems:
        print("FAIL", p)
    print(f"build_site: {info['mode']}, {info['documents']} documents, {info['pages']} pages -> {a.out}; {'OK' if not problems else str(len(problems)) + ' problem(s)'}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
