# Release strategy, versioning and tags

## Two version scales, never conflated

| Scale | Applies to | Where it lives |
|---|---|---|
| **Document version** `v<MAJOR>.<MINOR>` | One publication | The document's front matter and its version history table |
| **Corpus version** `corpus-v<MAJOR>.<MINOR>.<PATCH>` | The whole repository at a point in time | Git tags and `CHANGELOG.md` |

A reader cites a document version. The corpus version exists so that a build can be
reproduced. Citing the corpus version instead of the document version is the mistake this
separation exists to prevent.

## Document versioning

| Change | Version | Also required |
|---|---|---|
| Typography, formatting, a broken link | None | Nothing |
| A correction that changes what a sentence asserts | MINOR | An erratum on `/research/updates/` |
| A change to an argument, a conclusion, or a claim class | MAJOR | A version-pinned archive of the previous version, and a supersession banner |

**A pinned archive is immutable.** It is self-canonical, `noindex, follow`, excluded from
every sitemap, and it is never redirected forward. Redirecting a pinned version to the
current one is silent falsification of the citation record, and it is the one failure in
this corpus that no rollback repairs.

A MAJOR version never reuses the slug of an earlier version in a way that changes what the
current URL resolves to. The current URL always serves the current version; the previous
version moves to its pinned address and stays there.

## Corpus versioning

| Bump | When |
|---|---|
| MAJOR | A publication is withdrawn, a URL scheme changes, or the claim-class scheme changes. Anything that can break an external citation |
| MINOR | A publication is added, or a document takes a MAJOR version |
| PATCH | Corrections, copy, build, discovery, documentation |

## Tags

| Tag | Meaning | Cut by |
|---|---|---|
| `corpus-v<M>.<m>.<p>` | The corpus at a point in time. Immutable | The release workflow |
| `wave-1`, `wave-1b`, `wave-2` | A publication wave completed | By hand, at the wave's close |

Annotated tags, signed. **A tag is never moved and never deleted.** A tag that moves
breaks reproducibility for anybody who pinned to it, which is the only reason to have one.

## What a release is, and is not

A release **is** a statement about what the corpus contained at a point in time, an
archive bundle with a checksum, and a reproducible input to a build.

A release **is not** a deployment. Tagging changes nothing on any public host. Deployment
is a separate act, separately authorised, in `docs/04_DEPLOYMENT.md`. The separation
exists because a tag is cheap and reversible and a public change is neither.

## The release gate

`.github/workflows/release.yml` runs `verify_public.py --strict`, in which every declared
deferral counts as a failure. A release cannot be cut while any deferral is outstanding.
This is the mechanism that stops a tag being applied to a corpus that is mid-sequence,
and it is why the deferral list in `scripts/known_deferrals.json` names the step that
clears each entry rather than merely suppressing it.

The gate also fails if any `_PENDING_IMPORT.md` remains, if a generated file is stale, if
`CHANGELOG.md` has no entry for the tag, or if a slug has changed since the previous
release.

## Pre-release

`corpus-v1.0.0-rc.1` for a staging build under review. A pre-release tag never deploys to
production and is not announced.
