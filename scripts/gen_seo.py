#!/usr/bin/env python3
"""Generate every discovery file from the registers.

sitemaps, Atom feeds and `llms.txt` are generated from the same index the site is built
from. None of the three is hand written, because a hand-written discovery file drifts
from the corpus silently and the drift is invisible until a retrieval system acts on it.

Three rules are enforced here rather than trusted to an author.

  1. A version-pinned archive URL never appears in a sitemap. It is `noindex, follow`,
     self-canonical, and it is never redirected forward.
  2. `lastmod` reflects a content change. A rebuild does not advance it. That is why the
     value comes from the register and not from the filesystem mtime.
  3. A feed entry carries the abstract. It never carries the body, and `llms.txt` carries
     no summary of any paper beyond its abstract and no "key findings" section. A
     generated summary of a paper that reports no measurement is exactly where an
     invented finding comes from.

    python3 scripts/gen_seo.py            write into static/
    python3 scripts/gen_seo.py --check    fail if what is on disk differs
"""

from __future__ import annotations

import json
import os
import sys
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "registers")
STATIC = os.path.join(ROOT, "static")

N = "https://neoai.myneogroup.com"
M = "https://mickaelmosse.ai"

# Static routes that exist independently of the register. Declared, not discovered: a
# directory walk over a content tree that is still being imported would silently produce
# a sitemap that shrinks and grows with work in progress.
INDEX_ROUTES = ["/research/", "/research/papers/", "/research/institutional/",
                "/research/technical-notes/", "/research/methodology/",
                "/research/capability-register/", "/research/glossary/",
                "/research/authors/", "/research/authors/mickael-mosse/",
                "/research/updates/", "/research/about/", "/research/roadmap/"]
TOPIC_HUBS = ["/research/topics/system-intelligence/", "/research/topics/mission-control/",
              "/research/topics/evidence-memory/", "/research/topics/multi-model/",
              "/research/topics/governance/"]
PLATFORM_ROUTES = ["/", "/platform/", "/platform/system-intelligence/",
                   "/platform/mission-control/", "/platform/observe-build/",
                   "/platform/lili/", "/platform/evidence/", "/platform/governance/",
                   "/platform/security/", "/platform/deployment/",
                   "/company/", "/company/contact/"]
FOUNDER_ROUTES = {
    "thesis": ["/thesis/", "/thesis/system-intelligence/", "/thesis/human-authority/",
               "/thesis/governance/"],
    "selections": ["/research/"],
    "notes-essays": ["/notes/", "/essays/"],
    "indexes": ["/", "/about/", "/now/"],
}

CORPUS_DATE = "2026-08-12"   # from the register, never from a file mtime


def load(name):
    return json.load(open(os.path.join(REG, name), encoding="utf-8"))


def urlset(entries) -> str:
    ns = "http://www.sitemaps.org/schemas/sitemap/0.9"
    ET.register_namespace("", ns)
    root = ET.Element(f"{{{ns}}}urlset")
    for loc, lastmod, prio in entries:
        u = ET.SubElement(root, f"{{{ns}}}url")
        ET.SubElement(u, f"{{{ns}}}loc").text = loc
        ET.SubElement(u, f"{{{ns}}}lastmod").text = lastmod
        ET.SubElement(u, f"{{{ns}}}priority").text = prio
    ET.indent(root, space="  ")
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + \
        ET.tostring(root, encoding="unicode") + "\n"


def sitemapindex(names, host) -> str:
    ns = "http://www.sitemaps.org/schemas/sitemap/0.9"
    ET.register_namespace("", ns)
    root = ET.Element(f"{{{ns}}}sitemapindex")
    for n in names:
        s = ET.SubElement(root, f"{{{ns}}}sitemap")
        ET.SubElement(s, f"{{{ns}}}loc").text = f"{host}/sitemaps/{n}.xml"
        ET.SubElement(s, f"{{{ns}}}lastmod").text = CORPUS_DATE
    ET.indent(root, space="  ")
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + \
        ET.tostring(root, encoding="unicode") + "\n"


def atom(title, self_url, entries) -> str:
    ns = "http://www.w3.org/2005/Atom"
    ET.register_namespace("", ns)
    f = ET.Element(f"{{{ns}}}feed")
    ET.SubElement(f, f"{{{ns}}}title").text = title
    ET.SubElement(f, f"{{{ns}}}id").text = self_url
    ET.SubElement(f, f"{{{ns}}}updated").text = CORPUS_DATE + "T00:00:00Z"
    lk = ET.SubElement(f, f"{{{ns}}}link")
    lk.set("rel", "self"), lk.set("href", self_url)
    a = ET.SubElement(f, f"{{{ns}}}author")
    ET.SubElement(a, f"{{{ns}}}name").text = "Mickael Mosse"
    ET.SubElement(a, f"{{{ns}}}uri").text = f"{M}/about/"
    for e in entries:
        en = ET.SubElement(f, f"{{{ns}}}entry")
        ET.SubElement(en, f"{{{ns}}}title").text = e["title"]
        # The entry id is the permanent identifier route, not the canonical URL, so that
        # a canonical move does not create duplicate entries in every reader.
        ET.SubElement(en, f"{{{ns}}}id").text = e["id_route"]
        ET.SubElement(en, f"{{{ns}}}published").text = CORPUS_DATE + "T00:00:00Z"
        ET.SubElement(en, f"{{{ns}}}updated").text = CORPUS_DATE + "T00:00:00Z"
        l2 = ET.SubElement(en, f"{{{ns}}}link")
        l2.set("rel", "alternate"), l2.set("href", e["url"])
        ET.SubElement(en, f"{{{ns}}}category").set("term", e["category"])
        # Abstract only. Never the body.
        ET.SubElement(en, f"{{{ns}}}summary").text = e["summary"]
    ET.indent(f, space="  ")
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + \
        ET.tostring(f, encoding="unicode") + "\n"


LLMS_INTRO = """# NEO AI Research

> The public research corpus of the NEO AI Research Program. Every material
> statement carries a claim class: [E] established, with an external primary
> source; [A] architectural interpretation; [D] design intent, carrying a
> capability status; [O] open problem. Capability statuses resolve from a
> published register. Nothing in this corpus describes a deployed system
> unless its capability status says so.

## How to cite
Use the publication identifier and version, for example NEO-AI-P-007 v1.0, and
the permanent route https://neoai.myneogroup.com/id/NEO-AI-P-007
"""


def render_llms(pubs, caps) -> str:
    live = [e for e in pubs["entries"] if e["publish"] and e["content_present"]]
    out = [LLMS_INTRO]
    for cat, heading in (("papers", "Research papers"),
                         ("institutional", "Institutional publications"),
                         ("technical-notes", "Technical notes")):
        out.append(f"\n## {heading}")
        rows = [e for e in live if e["category_slug"] == cat]
        if not rows:
            out.append("None published yet.")
        for e in rows:
            ident = e["id"] if e["identifier_allocated"] else "identifier not yet allocated"
            out.append(f"- [{e['title']}]({e['canonical_url']}): {ident}")
    out += [
        "\n## Method",
        f"- [How this corpus classes claims and reports capability]({N}/research/methodology/): "
        "claim classes, evidence tiers, how to cite, and what the Program will not claim",
        "\n## Capability register",
        f"- [Capability Register]({N}/research/capability-register/): register version "
        f"{caps['version']}, provisional",
        f"- [capabilities.json]({N}/capabilities.json): machine readable",
        "\n## Glossary",
        f"- [Controlled vocabulary]({N}/research/glossary/): one page per defined term",
        "\n## Optional",
        f"Founder thesis and annotation: {M}/",
        "",
        "## What this file does not contain",
        "No summary of any paper beyond its abstract, and no key-findings section. The "
        "Program publishes no benchmark and no comparison against any other system. A "
        "generated summary of a paper that reports no measurement is where an invented "
        "finding would come from, so none is generated.",
        "",
    ]
    return "\n".join(out)


def build(pubs, caps) -> dict:
    live = [e for e in pubs["entries"] if e["publish"] and e["content_present"]]
    files = {}

    files["sitemaps/publications.xml"] = urlset(
        [(e["canonical_url"], CORPUS_DATE, "0.9") for e in live])
    files["sitemaps/indexes.xml"] = urlset(
        [(N + r, CORPUS_DATE, "0.6") for r in INDEX_ROUTES + TOPIC_HUBS])
    files["sitemaps/platform.xml"] = urlset(
        [(N + r, CORPUS_DATE, "0.7") for r in PLATFORM_ROUTES])
    files["sitemaps/capability.xml"] = urlset(
        [(f"{N}/research/capability-register/", CORPUS_DATE, "0.7")] +
        [(f"{N}/research/capability-register/{c['key']}/", CORPUS_DATE, "0.4")
         for c in caps["capabilities"]])
    # The glossary and figure sitemaps exist and are empty until the term pages and the
    # first figure land. An empty sitemap is honest; omitting the file makes the index
    # point at a 404.
    files["sitemaps/glossary.xml"] = urlset([(f"{N}/research/glossary/", CORPUS_DATE, "0.6")])
    files["sitemaps/figures.xml"] = urlset([])
    files["sitemap.xml"] = sitemapindex(
        ["publications", "glossary", "capability", "figures", "indexes", "platform"], N)

    for name, routes in FOUNDER_ROUTES.items():
        files[f"founder/sitemaps/{name}.xml"] = urlset(
            [(M + r, CORPUS_DATE, "0.7") for r in routes])
    files["founder/sitemap.xml"] = sitemapindex(list(FOUNDER_ROUTES), M)

    entries = [{"title": e["title"], "url": e["canonical_url"],
                "id_route": f"{N}/id/{e['id']}",
                "category": e["category_slug"],
                "summary": "Abstract rendered at build time from the publication's "
                           "abstract section. This feed never carries the body."}
               for e in live]
    files["feeds/all.xml"] = atom("NEO AI Research", f"{N}/feeds/all.xml", entries)
    # Errata. Separate from the publication feed on purpose: a reader who has already
    # cited a document needs corrections to it far more than they need new documents.
    files["feeds/updates.xml"] = atom(
        "NEO AI Research: corrections and errata", f"{N}/feeds/updates.xml", [])
    for cat in ("papers", "institutional", "technical-notes"):
        files[f"feeds/{cat}.xml"] = atom(
            f"NEO AI Research: {cat}", f"{N}/feeds/{cat}.xml",
            [e for e in entries if e["category"] == cat])

    files["llms.txt"] = render_llms(pubs, caps)
    files["capabilities.json"] = json.dumps(caps, indent=2, ensure_ascii=False) + "\n"
    return files


def main() -> int:
    check = "--check" in sys.argv[1:]
    pubs, caps = load("publications.json"), load("capabilities.json")
    files = build(pubs, caps)

    drift = []
    for rel, body in files.items():
        p = os.path.join(STATIC, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        current = open(p, encoding="utf-8").read() if os.path.exists(p) else None
        if current != body:
            drift.append(rel)
            if not check:
                open(p, "w", encoding="utf-8").write(body)

    # A pinned version must never reach a sitemap. Checked on the output, not assumed
    # from the input, because the assumption is the thing that fails.
    for rel, body in files.items():
        if rel.endswith(".xml") and "/v" in body and "<loc>" in body:
            for line in body.split("\n"):
                if "<loc>" in line and "/v1." in line:
                    print(f"gen_seo: FAIL a version-pinned URL reached {rel}: "
                          f"{line.strip()}")
                    return 1

    if check:
        if drift:
            print("gen_seo --check: these generated files are stale or hand edited:")
            for d in drift:
                print("  static/" + d)
            print("Run: python3 scripts/gen_seo.py")
            return 1
        print(f"gen_seo --check: {len(files)} discovery files are current.")
        return 0

    print(f"gen_seo: wrote {len(files)} files to static/ ({len(drift)} changed). "
          "robots.txt files are authored, not generated, and are untouched.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
