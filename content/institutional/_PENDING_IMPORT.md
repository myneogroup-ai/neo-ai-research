---
status: PENDING IMPORT
classification: A - approved for publication, text not yet cleared
---

# Pending import: institutional publications

**No file in this directory is a placeholder for a publication. Nothing is invented here.**

Two institutional publications are approved for Public Wave 1 and their public texts are not yet cleared. They are recorded in `registers/publications.json` with `content_present: false`, so the library index does not list them and no page links to a title that does not resolve.

## Why the sources are not simply copied in

Each of these documents is approved for publication **with named changes**, and two of
those changes remove material classified above PUBLIC. Copying the unedited source into
a public repository would put that material into a public git history, where removing it
later removes it from the working tree and not from the history.

The rule this repository follows: **a document enters `content/` only after its public
text exists.** An approval to publish is not a public text.

## What clears this

| Document | Change required | Cleared at |
|---|---|---|
| `NEO-AI-P-001` Introducing NEO AI | The cost engine paragraph is softened before publication | Execution step 14 |
| `NEO-AI-P-007` A Note on Responsible AI Capability Claims | One internal path is deleted. Otherwise approved as written | Execution step 14 |

`scripts/verify_public.py` raises `REG-07` for each of these against the register, and
the finding is deferred against `scripts/known_deferrals.json` with the step that clears
it. `--strict`, which the release workflow runs, treats every deferral as a failure. That
is what stops a release being cut while this file still exists.

## When the text arrives

1. Add the file at the path the register already records in `content_path`
2. Regenerate: `python3 scripts/build_indexes.py && python3 scripts/gen_seo.py`
3. Set `content_present` from the filesystem, never by hand
4. Remove the matching deferral from `scripts/known_deferrals.json`
5. Delete this file
