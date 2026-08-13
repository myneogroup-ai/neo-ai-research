---
status: PENDING IMPORT
classification: A - approved for publication, text not yet cleared
---

# Pending import: technical notes

**No file in this directory is a placeholder for a publication. Nothing is invented here.**

Three technical notes are approved for Public Wave 1 with named changes. Two of those changes remove material classified above PUBLIC, which is why the sources cannot enter this repository at all before the change is applied.

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
| `NEO-AI-TN-001` Bounding the Autonomy Budget | Remove the stale unregistered-identifier note; reconcile the trigger list without importing values | Execution steps 12 and 14 |
| `NEO-AI-TN-002` Detecting Circular Corroboration in an Evidence Chain | Reduce the procedure; publish no distinct-origin threshold | Execution steps 12 and 14 |
| `NEO-AI-TN-003` What Belongs in a Mission Event | Cut the section 3.3 store table | Execution steps 12 and 14 |

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
