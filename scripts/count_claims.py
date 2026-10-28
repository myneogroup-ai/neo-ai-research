#!/usr/bin/env python3
"""Count applied claim-class tags in a publication, the way the front matter must state
them: over the body and back matter, excluding the front-matter table itself.

    python3 scripts/count_claims.py content/papers/<slug>.md

Front-matter counts are produced by this script, never typed. P-007 section 11 records
why: two documents once declared counts their own text falsified.
"""
import re
import sys


def count(path: str) -> dict:
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    body = [ln for ln in lines if not ln.startswith("| Claim-class counts")]
    joined = "\n".join(body)
    out = {}
    for c in "EADO":
        out[c] = len(re.findall(rf"\[{c}\]", joined))
    return out


if __name__ == "__main__":
    for p in sys.argv[1:]:
        c = count(p)
        print(f"{p}: `[E]` {c['E']} . `[A]` {c['A']} . `[D]` {c['D']} . `[O]` {c['O']}")
