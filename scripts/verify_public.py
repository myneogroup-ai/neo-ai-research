#!/usr/bin/env python3
"""Public-repository conformance gate.

This is not the Program's release audit. It is the repository's CI guard: the smallest
set of mechanical checks that stop a public repository from acquiring something it must
not contain, and stop the corpus from drifting away from its own registers.

Three outcomes exist.

  FAIL      the repository is wrong. CI stops.
  DEFERRED  a known occurrence, declared in scripts/known_deferrals.json, each entry
            naming the execution step that clears it. Printed, does not stop CI.
  PASS      nothing found.

A deferral that no longer matches anything is itself a FAIL. A suppression list that
nobody prunes becomes a way of hiding findings, so the list is checked against reality
on every run.

Exit codes: 0 pass, 1 failures, 2 the repository is malformed.
"""

from __future__ import annotations

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
REGISTERS = os.path.join(ROOT, "registers")

CANON_HOST = "neoai.myneogroup.com"
FOUNDER_HOST = "mickaelmosse.ai"
ROUTE = "https://{h}/research/{cat}/{slug}/"
PUBLICATION_DIRS = ("papers", "institutional", "technical-notes")

findings: list[dict] = []
deferred: list[dict] = []
matched_deferrals: set[str] = set()


def load_deferrals() -> list[dict]:
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "known_deferrals.json")
    if not os.path.exists(p):
        return []
    return json.load(open(p, encoding="utf-8"))["deferrals"]


DEFERRALS = load_deferrals()


def deferral_for(check: str, path: str, evidence: str):
    for d in DEFERRALS:
        if d["check"] != check:
            continue
        if d["path"] not in ("*", path):
            continue
        if re.search(d["match"], evidence):
            return d
    return None


def report(check: str, path: str, line: int, evidence: str, detail: str) -> None:
    d = deferral_for(check, path, evidence)
    rec = {"check": check, "path": path, "line": line,
           "evidence": evidence[:160], "detail": detail}
    if d:
        matched_deferrals.add(d["id"])
        rec["deferral"] = d["id"]
        rec["clears_at"] = d["clears_at"]
        deferred.append(rec)
    else:
        findings.append(rec)


def walk(base: str, exts=(".md",)):
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fn in sorted(filenames):
            if fn.endswith(exts):
                yield os.path.relpath(os.path.join(dirpath, fn), ROOT)


def read(rel: str) -> str:
    return open(os.path.join(ROOT, rel), encoding="utf-8").read()


# --------------------------------------------------------------------------------------
# CLS. Classification. The reason this file exists.
# --------------------------------------------------------------------------------------

# A withholding declaration is not a disclosure. Saying "the objective function is
# withheld" is the corpus doing its job; publishing its coefficients is the failure. The
# distinction is made two ways, because either alone is too weak: by section, where the
# nearest preceding heading announces a withholding table, and by sentence, where the
# governing clause says the thing is not published.
#
# CLS-04 and CLS-06 are the two checks that need it. The rest do not, because no
# withholding declaration contains a credential, a coefficient value or a client name.

WITHHOLDING_HEADING = re.compile(
    r"(?i)^#{1,6}\s.*\b(withheld|withholding|what is not published|not published here|"
    r"classification|what this edition (?:withholds|does not)|limits of this edition|"
    r"version history|scope and limitations)\b")

WITHHOLDING_SENTENCE = re.compile(
    r"(?i)\b(withheld|withholds|withholding|not published|never published|is not "
    r"disclosed|does not (?:disclose|publish|state|report|include)|do not publish|"
    r"we publish no|removed entirely|not reduced, not paraphrased|prohibited|excluded|"
    r"redacted|is a reduction|are removed|is removed|no derivative|policy|"
    r"must never|may not appear)\b")


def sentence_of(text: str, index: int) -> str:
    """The sentence containing `index`, across soft line wraps and table cells."""
    start = max(text.rfind(". ", 0, index), text.rfind(".\n", 0, index),
                text.rfind("\n\n", 0, index), text.rfind("| ", 0, index),
                text.rfind("\n- ", 0, index), text.rfind(": ", 0, index)) + 1
    ends = [e for e in (text.find(". ", index), text.find(".\n", index),
                        text.find(" |", index), text.find("\n", index)) if e != -1]
    end = min(ends) if ends else len(text)
    return text[start:end]


def in_withholding_section(lines: list[str], line_no: int) -> bool:
    for i in range(line_no - 1, -1, -1):
        if lines[i].startswith("#"):
            return bool(WITHHOLDING_HEADING.match(lines[i]))
    return False


# Files whose whole purpose is to enumerate what must not be published. Naming a
# category is what they are for; carrying a value is still a failure, so only the
# category-naming checks are relaxed here and every value-shaped check still applies.
POLICY_FILES = {
    "docs/07_CLASSIFICATION_POLICY.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
}


def is_withholding(text: str, lines: list[str], index: int, line_no: int,
                   rel: str = "") -> bool:
    return (rel.replace(os.sep, "/") in POLICY_FILES
            or in_withholding_section(lines, line_no)
            or bool(WITHHOLDING_SENTENCE.search(sentence_of(text, index))))


CLASSIFIED_PATTERNS = [
    ("CLS-01", r"\b[0-9a-f]{40,}\b", False,
     "a long hexadecimal string. Package digests and internal hashes are not published"),
    ("CLS-02", r"(?i)\b(api[_-]?key|secret[_-]?key|access[_-]?token|bearer\s+[A-Za-z0-9._-]{16,}|BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY)\b", False,
     "a credential shape"),
    ("CLS-03", r"/(?:home|Users|var|opt|srv)/[A-Za-z0-9._-]+/", False,
     "an absolute filesystem path from a machine"),
    # A handling marker, not a classification label. `TRADE SECRET` and `CONFIDENTIAL
    # TECHNICAL ARCHITECTURE` appear legitimately in a public edition's withholding
    # table, where they name what is being withheld. These strings do not.
    # Case sensitive on the shouted forms. "We do not publish routing parameters" is a
    # policy statement and is the corpus working correctly; "DO NOT PUBLISH" is a marker
    # somebody forgot to remove.
    ("CLS-04", r"(?:\bDO NOT (?:PUBLISH|DISTRIBUTE)\b|\bNOT FOR (?:PUBLICATION|EXTERNAL|CIRCULATION)\b"
               r"|\b[Ii]nternal [Oo]nly\b|\bINTERNAL ONLY\b"
               r"|\b[Ff]or internal use\b|\bFOR INTERNAL USE\b"
               r"|\b[Ii]nternal draft\b|\bINTERNAL DRAFT\b"
               r"|\b[Ii]nternal circulation\b)", False,
     "an internal-handling marker"),
    # An internal governance or register reference. Correct inside the Program, wrong on
    # a public page: it names artefacts a reader cannot reach and exposes the internal
    # control structure.
    ("CLS-13", r"(?:\bdata/(?:identifiers|capabilities)\.json\b|\baudit/[a-z_]+\.py\b|"
               r"\bPUB_\d\d\b|\bEXE_\d\d\b|\b(?:FA|VA)-PUB-\d\d\d\b|"
               r"\bPUB-(?:OPEN|BLOCK|ACT)-\d\d\b|\bFDR-[A-Z0-9-]+\b|"
               r"\bCORPUS_LOCK\b|\bLOCK_v2\b|\bGATE\s+[A-Z0-9-]+\b|"
               r"\bNEO-AI-STD-00\d\b|\bRULE\s+STD-\d\d\d-[A-Z]\d)", False,
     "an internal governance or register reference on a public surface"),
    ("CLS-05", r"(?i)\bstage\s*[23]\b|\bengineering constitution\b|\bdata program\b|\bdata gate\b", True,
     "a reference to an internal programme stage or governing document"),
    ("CLS-06", r"(?i)(?:score vector|objective function|loss function|router loss|propensity logging|admissible[- ]set predicate|acceptance threshold|cost model coefficient|scoring weight|routing threshold)[^.\n|]{0,90}?[0-9]", True,
     "a trade-secret mechanism named together with a value"),
    ("CLS-07", r"(?i)\bthreshold\s+(?:of|is|=|set to)\s*[0-9]", True,
     "a numeric threshold"),
    ("CLS-08", r"(?i)\b(?:p_d|w_[a-z]|lambda|alpha|beta)\s*\(?t?\)?\s*=\s*[0-9.]", True,
     "a coefficient with a value"),
    ("CLS-09", r"(?i)(?:EUR|USD|GBP|€|\$|£)\s?[0-9][0-9,.]*\s?(?:k|m|bn|million|billion)?\b", False,
     "a financial figure"),
    ("CLS-10", r"(?i)\b(?:our|the)\s+(?:pilot\s+)?client\s+[A-Z][A-Za-z]+\b", False,
     "what reads as a named client"),
    ("CLS-11", r"(?i)\b(?:kubernetes namespace|service mesh topology|partition counts?|shard counts?|topic partitions?)\b", True,
     "deployment topology detail"),
    ("CLS-12", r"(?i)\bgithub\.com/myneogroup-ai/(?!neo-ai-research\b)[a-z0-9-]+", False,
     "another repository in the organisation. Only this repository is public"),
]

# Never state that NEO is more capable than a named system. The prohibition is absolute
# and the check is written to catch the shape, not one phrasing of it.
COMPARISON_VENDORS = r"(?:GPT|ChatGPT|Claude|Gemini|Grok|Kimi|Llama|Mistral|OpenAI|Anthropic|Google DeepMind|xAI)"
CLAIM_PATTERNS = [
    ("CMP-01", rf"(?i)\b(?:smarter|better|stronger|more capable|outperform\w*|beats?|superior)\b[^.\n]{{0,60}}\b{COMPARISON_VENDORS}\b", True,
     "a capability comparison against a named system"),
    ("CMP-02", rf"(?i)\b{COMPARISON_VENDORS}\b[^.\n]{{0,60}}\b(?:worse|weaker|less capable|cannot match|falls short)\b", True,
     "a capability comparison against a named system"),
    ("CMP-03", r"(?i)\bstate[- ]of[- ]the[- ]art\b|\bbest[- ]in[- ]class\b|\bindustry[- ]leading\b|\bworld[- ]class\b", True,
     "an unsupported superlative"),
    ("CMP-04", r"(?i)\bwe (?:benchmarked|measured|evaluated)\b|\bour benchmark (?:shows|results)\b", True,
     "a reported measurement. The Program publishes none"),
]

STYLE_PATTERNS = [
    ("STY-01", r"[—–]", "an em dash or en dash. The house style prohibits both"),
    ("STY-02", r"(?i)\[[^\]]*\]\(\s*(?:https?://)?[^)]*\)\s*", None),  # handled separately
    ("STY-03", r"(?i)\b(?:organiz|analyz|behavior|color|defense|license\s+to\s+use|catalog)\b",
     "United States orthography. The house style is British"),
]

BAD_ANCHORS = re.compile(r"\[(click here|read more|here|this paper|this document|link|more)\]\(",
                         re.I)


def check_classification():
    for rel in list(walk(CONTENT)) + list(walk(os.path.join(ROOT, "docs"))) + \
            list(walk(ROOT, (".json", ".jsonld", ".cff", ".txt"))):
        if os.sep + "scripts" + os.sep in rel or rel.startswith("scripts"):
            continue
        try:
            text = read(rel)
        except (UnicodeDecodeError, IsADirectoryError):
            continue
        lines = text.split("\n")
        for cid, pat, withholding_exempt, detail in CLASSIFIED_PATTERNS + CLAIM_PATTERNS:
            for m in re.finditer(pat, text):
                line = text.count("\n", 0, m.start()) + 1
                if withholding_exempt and is_withholding(text, lines, m.start(),
                                                         line - 1, rel):
                    continue
                report(cid, rel, line, lines[line - 1].strip(), detail)


def check_style():
    for rel in walk(CONTENT):
        text = read(rel)
        lines = text.split("\n")
        for cid, pat, detail in STYLE_PATTERNS:
            if detail is None:
                continue
            for m in re.finditer(pat, text):
                line = text.count("\n", 0, m.start()) + 1
                report(cid, rel, line, lines[line - 1].strip(), detail)
        for m in BAD_ANCHORS.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            report("STY-04", rel, line, lines[line - 1].strip(),
                   "prohibited anchor text. Use the exact title")


# --------------------------------------------------------------------------------------
# REG. The registers and the content tree must agree, mechanically.
# --------------------------------------------------------------------------------------

def check_registers():
    pubs = json.load(open(os.path.join(REGISTERS, "publications.json"), encoding="utf-8"))
    caps = json.load(open(os.path.join(REGISTERS, "capabilities.json"), encoding="utf-8"))
    voc = json.load(open(os.path.join(REGISTERS, "vocabulary.json"), encoding="utf-8"))

    seen_slugs, seen_ids = {}, set()
    for e in pubs["entries"]:
        pid = e["id"]
        if pid in seen_ids:
            report("REG-01", "registers/publications.json", 0, pid, "duplicate identifier")
        seen_ids.add(pid)

        expected = ROUTE.format(h=CANON_HOST, cat=e["category_slug"], slug=e["slug"])
        if e["canonical_url"] != expected:
            report("REG-02", "registers/publications.json", 0, e["canonical_url"],
                   f"canonical URL disagrees with the route template. Expected {expected}")

        if e["category_slug"] not in PUBLICATION_DIRS:
            report("REG-03", "registers/publications.json", 0, e["category_slug"],
                   "category slug has no matching directory under content/")

        want = f"content/{e['category_slug']}/{e['slug']}.md"
        if e["content_path"] != want:
            report("REG-04", "registers/publications.json", 0, e["content_path"],
                   f"content path is not derivable from the slug. Expected {want}")

        key = (e["category_slug"], e["slug"])
        if key in seen_slugs:
            report("REG-05", "registers/publications.json", 0, str(key), "duplicate slug")
        seen_slugs[key] = pid

        present = os.path.exists(os.path.join(ROOT, e["content_path"]))
        if e.get("content_present") != present:
            report("REG-06", "registers/publications.json", 0, pid,
                   "content_present disagrees with the filesystem. Regenerate the register")
        if e.get("publish") and not present:
            report("REG-07", "registers/publications.json", 0, pid,
                   "marked for publication and no text is present")
        if e.get("publish") and e.get("status") != "APPROVED_FOR_WAVE_1":
            report("REG-08", "registers/publications.json", 0, pid,
                   "publish is true and the status is not an approval")

    # Every publication file must belong to a register entry. Nothing publishes by
    # existing on disk.
    registered = {e["content_path"] for e in pubs["entries"]}
    for d in PUBLICATION_DIRS:
        base = os.path.join(CONTENT, d)
        if not os.path.isdir(base):
            continue
        for rel in walk(base):
            if os.path.basename(rel).startswith("_"):
                continue
            if rel.replace(os.sep, "/") not in registered:
                report("REG-09", rel, 0, rel,
                       "a publication file with no register entry. It would never be built")

    # Capability register
    if caps.get("version") and str(caps.get("status", "")).upper().find("PROVISIONAL") < 0:
        report("REG-10", "registers/capabilities.json", 0, str(caps.get("status")),
               "the capability register is no longer marked provisional. If the "
               "ratification gate has closed, this check is what needs updating")

    # Vocabulary arithmetic. Derived, never typed.
    before, added, after = (voc["count_before_amendment"], voc["terms_added"],
                            voc["count_after_amendment"])
    if before != len(voc["locked_terms"]):
        report("REG-11", "registers/vocabulary.json", 0, str(before),
               f"count disagrees with the list, which holds {len(voc['locked_terms'])}")
    if added != len(voc["added_terms"]):
        report("REG-12", "registers/vocabulary.json", 0, str(added),
               f"count disagrees with the list, which holds {len(voc['added_terms'])}")
    if before + added != after:
        report("REG-13", "registers/vocabulary.json", 0, f"{before}+{added}!={after}",
               "the vocabulary counts do not add up")
    overlap = set(voc["locked_terms"]) & set(voc["added_terms"])
    if overlap:
        report("REG-14", "registers/vocabulary.json", 0, ", ".join(sorted(overlap)),
               "a term is in both the locked list and the added list")
    return pubs, caps, voc


# --------------------------------------------------------------------------------------
# VOC, CAP, CLM. Corpus discipline.
# --------------------------------------------------------------------------------------

def check_corpus(pubs, caps, voc):
    cap_keys = set(caps.get("capabilities", {}).keys()) if isinstance(
        caps.get("capabilities"), dict) else {c.get("key") for c in caps.get("capabilities", [])}
    prohibited = voc["prohibited_synonyms"]

    for rel in walk(CONTENT):
        text = read(rel)
        lines = text.split("\n")

        for term in prohibited:
            for m in re.finditer(rf"\b{re.escape(term)}\b", text):
                line = text.count("\n", 0, m.start()) + 1
                if re.search(r"(?i)prohibit|refus|never|instead of|not\s+$", lines[line - 1]):
                    continue
                report("VOC-01", rel, line, lines[line - 1].strip(),
                       f"'{term}' is a prohibited synonym")

        for m in re.finditer(r"`([a-z][a-z0-9.-]*(?:\.[a-z0-9-]+)+|brain|lili|pilots|"
                             r"mission-control|foundation-model|neo-intelligence|"
                             r"public-website)`\s*\(?(S[1-5])\)?", text):
            key = m.group(1)
            if cap_keys and key not in cap_keys:
                line = text.count("\n", 0, m.start()) + 1
                report("CAP-01", rel, line, m.group(0),
                       "a capability key that is not in the register")

        is_pub = any(rel.startswith(f"content/{d}/") for d in PUBLICATION_DIRS)
        if is_pub and not os.path.basename(rel).startswith("_"):
            classes = re.findall(r"`\[([EADO])\]`|\[([EADO])\]", text)
            n = len(classes)
            if n == 0:
                report("CLM-01", rel, 0, rel,
                       "a publication carrying no claim class at all")
            body_words = len(text.split())
            if n and body_words / n > 900:
                report("CLM-02", rel, 0, f"{n} classes over {body_words} words",
                       "claim-class density is far below the corpus norm. Statements are "
                       "probably unclassed")


def check_structure():
    required = [
        "README.md", "LICENSE", "LICENSE-CODE", "SECURITY.md", "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md", "CITATION.cff", "CHANGELOG.md",
        ".github/CODEOWNERS", ".github/PULL_REQUEST_TEMPLATE.md",
        ".github/ISSUE_TEMPLATE/config.yml",
        "registers/publications.json", "registers/capabilities.json",
        "registers/vocabulary.json",
        "static/robots.neoai.txt", "static/robots.mickaelmosse.txt",
        "docs/07_CLASSIFICATION_POLICY.md",
    ]
    for r in required:
        if not os.path.exists(os.path.join(ROOT, r)):
            report("STR-01", r, 0, r, "a required repository file is missing")

    for rel in walk(CONTENT):
        text = read(rel)
        h1 = [ln for ln in text.split("\n") if ln.startswith("# ")]
        if len(h1) > 1:
            report("STR-02", rel, 0, f"{len(h1)} level-one headings",
                   "more than one h1. The heading tree is how a retrieval system segments "
                   "the document")
        prev = 0
        for i, ln in enumerate(text.split("\n"), 1):
            m = re.match(r"^(#{1,6}) ", ln)
            if m:
                lvl = len(m.group(1))
                if prev and lvl > prev + 1:
                    report("STR-03", rel, i, ln.strip(),
                           f"heading level jumps from {prev} to {lvl}")
                prev = lvl


def check_deferrals_are_live():
    for d in DEFERRALS:
        if d["id"] not in matched_deferrals:
            findings.append({
                "check": "DEF-01", "path": "scripts/known_deferrals.json", "line": 0,
                "evidence": d["id"],
                "detail": "a declared deferral matched nothing. It is stale and must be "
                          "removed, or the thing it described has silently changed"})


# --------------------------------------------------------------------------------------
# Self-test. A check that cannot fail is not a check, and an exemption that swallows
# everything is worse than no check at all. Each pattern carries a string it must catch
# and, where an exemption exists, a string it must not.
# --------------------------------------------------------------------------------------

SELF_TEST = [
    ("CLS-01", "digest 5bc3c1ceb24d1db8f01c28d4be7a2c53eb4b21dc62880c1bc2e0ce2add038000", None),
    ("CLS-02", "set api_key to something", None),
    ("CLS-03", "see /home/build/neo/corpus/", None),
    ("CLS-04", "DO NOT PUBLISH this section", None),
    ("CLS-13", "resolved from `data/identifiers.json` v1.5", None),
    ("CLS-05", "carried forward from Stage 3",
     "The Engineering Constitution is not published and no derivative of it is."),
    ("CLS-06", "the objective function weights quality at 0.62",
     "The objective function, its terms and its coefficients are withheld as TRADE SECRET."),
    ("CLS-07", "escalates above a threshold of 0.85",
     "No routing threshold is published. The threshold is withheld."),
    ("CLS-08", "with p_d(t) = 0.85 in the worked example",
     "The coefficients are withheld and no value is published."),
    ("CLS-09", "a contract worth EUR 2.4m", None),
    ("CLS-10", "the pilot client Meridian reported", None),
    ("CLS-11", "sixteen topic partitions per stream",
     "The partition count is withheld as CONFIDENTIAL."),
    ("CLS-12", "https://github.com/myneogroup-ai/neo-ai-platform", None),
    ("CMP-01", "NEO is smarter than GPT on this class of task",
     "We do not publish any comparison and no claim that NEO outperforms GPT is made here."),
    ("CMP-02", "Gemini is weaker at multi step retrieval",
     "No claim that Claude is less capable is made or published anywhere in this corpus."),
    ("CMP-03", "a state-of-the-art orchestration layer",
     "The phrase state of the art is prohibited and appears on no page."),
    ("CMP-04", "we benchmarked the router across four providers",
     "No benchmark is published and we do not publish measured results."),
]


def self_test() -> int:
    by_id = {c[0]: c for c in CLASSIFIED_PATTERNS + CLAIM_PATTERNS}
    missed, swallowed, untested = [], [], []
    for cid, positive, negative in SELF_TEST:
        cid_, pat, exempt, _ = by_id[cid]
        lines = ["## Body", positive]
        text = "\n".join(lines)
        m = re.search(pat, text)
        fired = bool(m) and not (exempt and is_withholding(text, lines, m.start(), 1))
        if not fired:
            missed.append((cid, positive))
        if negative is not None:
            nlines = ["## What this edition withholds", negative]
            ntext = "\n".join(nlines)
            nm = re.search(pat, ntext)
            nfired = bool(nm) and not (
                exempt and is_withholding(ntext, nlines, nm.start(), 1))
            if nfired:
                swallowed.append((cid, negative))
        elif exempt:
            untested.append(cid)

    for cid, s in missed:
        print(f"SELF-TEST FAIL  {cid} did not fire on: {s}")
    for cid, s in swallowed:
        print(f"SELF-TEST FAIL  {cid} fired on a withholding declaration: {s}")
    for cid in untested:
        print(f"SELF-TEST FAIL  {cid} has an exemption and no negative case")
    # The policy-file exemption relaxes category naming. It must not relax a value.
    # CLS-02 is a credential shape and has no exemption at all, so it must still fire
    # inside a policy file; CLS-05 names a category and must not.
    pol = "docs/07_CLASSIFICATION_POLICY.md"
    for cid, must_fire in (("CLS-02", True), ("CLS-05", False)):
        _, pat, exempt, _d = by_id[cid]
        pos = dict((c[0], c[1]) for c in SELF_TEST)[cid]
        lines = ["## Body", pos]
        text = "\n".join(lines)
        m = re.search(pat, text)
        fired = bool(m) and not (exempt and is_withholding(text, lines, m.start(), 1, pol))
        if fired != must_fire:
            swallowed.append((cid, f"policy-file exemption behaved wrongly: fired={fired}"))
            print(f"SELF-TEST FAIL  {cid} in a policy file: fired={fired}, "
                  f"expected {must_fire}")

    tested = len(SELF_TEST)
    negatives = sum(1 for _, _, n in SELF_TEST if n is not None)
    bad = len(missed) + len(swallowed) + len(untested)
    print(f"\nself-test: {tested} checks exercised, {negatives} negative cases, {bad} failed.")
    return 1 if bad else 0


def main() -> int:
    argv = sys.argv[1:]
    if "--self-test" in argv:
        return self_test()
    strict = "--strict" in argv

    if not os.path.isdir(CONTENT) or not os.path.isdir(REGISTERS):
        print("repository is malformed: content/ or registers/ is missing", file=sys.stderr)
        return 2

    check_structure()
    pubs, caps, voc = check_registers()
    check_classification()
    check_style()
    check_corpus(pubs, caps, voc)
    check_deferrals_are_live()

    for rec in deferred:
        print(f"DEFERRED {rec['check']} {rec['path']}:{rec['line']}  {rec['detail']}\n"
              f"         {rec['evidence']}\n"
              f"         deferral {rec['deferral']}, clears at {rec['clears_at']}")
    for rec in findings:
        print(f"FAIL     {rec['check']} {rec['path']}:{rec['line']}  {rec['detail']}\n"
              f"         {rec['evidence']}")

    total = len(findings) + len(deferred)
    print(f"\nverify_public: {total} finding(s). "
          f"{len(findings)} fail, {len(deferred)} deferred."
          + ("  STRICT: deferrals count as failures." if strict else ""))
    if findings:
        print("Repository is not publishable in this state.")
        return 1
    if strict and deferred:
        print("Repository is not releasable: every deferral must be cleared by its named "
              "execution step before a release tag is cut.")
        return 1
    print("Repository conformance: PASS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
