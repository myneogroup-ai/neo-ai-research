# Branch strategy

Trunk based, with one long-lived branch and short-lived work branches. There is no
`develop`. A second long-lived branch on a corpus this size produces merge cost and
buys nothing, because the corpus does not have concurrent major versions in flight.

## Branches

| Branch | Lifetime | Meaning |
|---|---|---|
| `main` | Permanent | The corpus as it currently stands. Always deployable to staging. Protected |
| `content/<id>-<slug>` | Days | A new publication or a new version of one |
| `fix/<id>-<what>` | Hours | A correction to a published document |
| `copy/<page>` | Hours | Website copy that is not a publication |
| `build/<what>` | Days | Scripts, workflows, schema, discovery |
| `docs/<what>` | Hours | Repository documentation |
| `release/corpus-v<M>.<m>` | Weeks | Cut only when a release needs stabilising while `main` moves on. Usually absent |

Examples: `content/r-009-system-intelligence`, `fix/tn-001-identifier-note`,
`build/sitemap-pinned-exclusion`.

## Protection on `main`

| Setting | Value | Why |
|---|---|---|
| Require a pull request | Yes | No direct push, including for maintainers |
| Required approvals | 1, and 2 for `content/**` and `registers/**` | A publication is read by a second person before it exists in public |
| Dismiss stale approvals on new commits | Yes | An approval describes what was read |
| Require review from code owners | Yes | See `.github/CODEOWNERS` |
| Required status checks | `conformance`, `build`, `link-check` | Green before merge, and up to date with `main` |
| Require conversation resolution | Yes | |
| Require signed commits | Yes | A public research corpus is a provenance claim. Unsigned commits weaken it |
| Require linear history | Yes | Squash merge only |
| Allow force push | No | |
| Allow deletion | No | |
| Enforce for administrators | Yes | The rule that gets waived at 2 a.m. is the one that needed enforcing |

## The rule GitHub cannot enforce

**A reviewer may not approve a document they wrote.** Branch protection can require a
code-owner review; it cannot know who drafted the prose. The rule is carried at the
review gate and it is the control most likely to be compressed when a launch date exists,
so it is written here rather than assumed.

## Merge policy

Squash merge, always. The commit subject becomes the changelog line, so it is written for
a reader of `git log` rather than for the author.

```
content(R-009): add From Model Intelligence to System Intelligence v1.0
fix(TN-001): remove the stale identifier note
build(seo): exclude pinned versions from every sitemap
docs(rollback): name both executing officers
```

Rebase, never merge, to bring `main` into a work branch. Linear history is required.

## What never enters any branch

A branch is public the moment it is pushed, and deleting a branch does not remove its
commits from a fork or from anybody's clone. Everything in `docs/07_CLASSIFICATION_POLICY.md`
that must not be in `main` must not be in a branch either, not even briefly, not even in
a commit that a later commit removes.
