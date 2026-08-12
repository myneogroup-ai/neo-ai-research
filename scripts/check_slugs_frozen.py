#!/usr/bin/env python3
"""Compare slugs against a previous release. A slug is frozen at first publication.

Changing a published slug breaks every citation of it, and it is the failure a release is
most likely to introduce without anybody noticing, because a slug change usually arrives
as a tidy-up rather than as a decision.

    python3 scripts/check_slugs_frozen.py <previous-publications.json>
"""
import json
import sys


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    prev = {e["id"]: e["slug"]
            for e in json.load(open(sys.argv[1], encoding="utf-8"))["entries"]}
    cur = {e["id"]: e["slug"]
           for e in json.load(open("registers/publications.json", encoding="utf-8"))["entries"]}
    bad = [(k, prev[k], cur[k]) for k in prev if k in cur and prev[k] != cur[k]]
    gone = [k for k in prev if k not in cur]
    for k, a, b in bad:
        print(f"::error::slug for {k} changed from '{a}' to '{b}'. Slugs are frozen at "
              f"first publication.")
    for k in gone:
        print(f"::error::{k} was in the previous release and is absent now. A published "
              f"identifier is never withdrawn from the register.")
    if not bad and not gone:
        print(f"slugs frozen: {len(prev)} compared, none changed.")
    return 1 if (bad or gone) else 0


if __name__ == "__main__":
    sys.exit(main())
