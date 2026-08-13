# Rollback

**Standing authority. Signed in advance, executed on trigger, reported afterwards.**

A rollback that requires an approval is a rollback that happens hours late, at night, by
somebody who cannot reach the person with authority. The authorisation is granted before
publication and is not sought at the moment it is needed.

The executing officer rolls back on any trigger below and informs afterwards. That order
is deliberate and is the whole design.

## Triggers. Measured, not judged.

Any single trigger is sufficient. None requires a second opinion.

| # | Trigger | Threshold | Action |
|---|---|---|---|
| **T1** | A pinned version redirected forward | **Any occurrence** | Immediate rollback of the whole redirect block |
| **T2** | Redirect chain or loop | Any occurrence | Fix immediately; roll back if not fixed within 30 minutes |
| **T3** | Server errors | Above 0.5 per cent | Roll back |
| **T4** | `hreflang` reciprocity errors at day 7 | Above 2 per cent | Fix or roll back |
| **T5** | Indexed URLs at day 14 | Below 50 per cent of baseline | Roll back |
| **T6** | Organic entrances at day 21 | Below 60 per cent of the 28-day baseline | Roll back |
| **T7** | Classified material on a public page | **Any occurrence** | Immediate withdrawal of the page, then full rollback if the source is unclear |
| **T8** | A capability described as deployed that is not | Any occurrence | Withdraw the page, correct, re-run gate A and gate B |

**T1 and T7 have no tolerance band.** T1 falsifies the citation record. T7 cannot be
undone by removing the page, because the page has already been read; the rollback limits
further exposure and the disclosure is handled under `SECURITY.md`, separately.

## Reversal by phase

| Phase reached | Reversal | Time | Recoverable |
|---|---|---|---|
| A, content live and unlinked | Unlink | Minutes | Fully |
| B, linked into navigation | Revert the build | Under 30 minutes | Fully |
| D, redirects issued | Remove the redirect block. Both canonicals resolve. Accept a temporary duplicate period | Under 30 minutes | Fully, as to routing |
| Any | **An external citation of a new canonical made in the window** | Not applicable | **No.** This is why phase D waits seven days behind phase B |

A temporary duplicate-content period is a smaller harm than a broken citation graph, and
the plan accepts it deliberately rather than reluctantly.

## Execution

```bash
gh workflow run rollback.yml \
  -f trigger="T7 classified material on a public page" \
  -f scope="revert the build, phase B" \
  -f ref=corpus-v1.0.0
```

`.github/workflows/rollback.yml` targets **no GitHub Environment** and therefore has no
required reviewer. It is the single place in this repository where a production change
bypasses review, and that is the point of it.

## Verify the reversal

A rollback that leaves a pinned version forwarded has not fixed the thing that mattered.

- No redirect chain, no loop
- Every pinned URL resolves to its own address
- The withdrawn page returns `410`, not `404`, where the withdrawal is permanent
- The register records the withdrawal

## Rehearsal, required before publication

| | |
|---|---|
| Rehearsed by | |
| Date | |
| Phase rehearsed | phase B revert / phase D redirect removal |
| Time taken | ______ minutes |
| Result | under 30 minutes / **over, publication held** |

## Event record

One row per rollback. Completed after the fact, never in advance.

| Date and time | Trigger | Phase | Action | Time to complete | Executed by | Founder informed |
|---|---|---|---|---|---|---|
| | | | | | | |
