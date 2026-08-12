# Contributing

Thank you for reading closely enough to want to contribute. The most valuable
contribution to this corpus is a correction with a primary source attached.

## Before anything else: the classification rule

This repository is public. Contributors outside the Program cannot know what is
classified, so the rule is simple and one-directional.

**Never add information about NEO AI internals that is not already published here.** If
you know something about the system that this repository does not say, do not add it,
even if you believe it is harmless and even if it would improve the page. Open an issue
describing the gap instead and let the Program decide what may be published.

If you believe something already published should not be, see `SECURITY.md`. Report it
privately.

## What we want

| Contribution | How |
|---|---|
| A factual correction to an `[E]` claim | Issue: Correction. Attach the primary source |
| A broken link, a wrong identifier, a wrong version | Issue: Correction |
| A definition that is unclear or collides with another | Issue: Glossary term |
| A capability described in a way that reads as deployed when it is not | Issue: Capability claim. This is a serious report and is treated as one |
| A typographical or formatting fix | Pull request directly |
| A build, script or workflow improvement | Pull request, with the reasoning in the description |

## What we will decline

| | Why |
|---|---|
| A rewrite of a research argument | The corpus is versioned and argued. Disagreement is published as a response, not merged as an edit |
| A comparison against a named model or product | The Program publishes no such comparison and will not host one |
| A capability claim strengthened beyond its status token | A claim may be weakened. It is never strengthened |
| Marketing language, superlatives, keyword-targeted text | The corpus competes on being worth citing |
| A summary or "key findings" section generated from a paper | A generated summary of a paper that reports no measurement is exactly where an invented finding comes from |
| A new synonym for a locked term | See the controlled vocabulary below |

## The controlled vocabulary

`registers/vocabulary.json` is the single source of terminology. A term in that file is
used exactly as written. Introducing a synonym for a locked term fragments the entity
graph and breaks first-occurrence glossary linking.

`Provider Independence` is a prohibited synonym. Use `Provider Replaceability`. The
Program refused the former because it contradicts a position published in
`NEO-AI-R-001` section 4.4, and the refusal is deliberate rather than stylistic.

Proposing a new term is a governance act, not an edit. Open a Glossary term issue.

## House style

The build enforces these. A pull request that breaks one fails CI rather than being
argued about in review.

- British orthography
- No em dash and no en dash. Use a comma, a full stop, or restructure the sentence
- One `<h1>` per document, headings descending without skipping a level
- Every date as `YYYY-MM-DD`
- Anchor text is the exact title, optionally prefixed with the identifier. `click here`,
  `read more`, `this paper`, `here` and bare URLs fail the build
- Every `[E]` claim carries at least one external primary-source link
- Every capability key mentioned links to its ledger page

## Claim classes are mandatory

Every material statement in a paper, publication or technical note carries `[E]`, `[A]`,
`[D]` or `[O]`. A new sentence with no class fails conformance. If you are unsure which
class applies, that uncertainty is itself informative: say so in the pull request and a
maintainer will class it.

## Pull request workflow

1. Branch from `main` using the naming in `docs/01_BRANCH_STRATEGY.md`
2. Make the change. Run `python3 scripts/verify_public.py` locally
3. Open the pull request against `main` and complete the template honestly
4. CI runs conformance, build and link checks
5. A code owner reviews. Content changes need a Research Program reviewer; a reviewer may
   not approve a document they wrote

## Errata, not silent fixes

A correction to a published document produces a visible erratum on
`/research/updates/` and a version increment. We do not quietly change a published
sentence. That policy is the reason a correction is welcome rather than embarrassing.

| Change | Version |
|---|---|
| Typography, formatting, a broken link | No version change |
| A correction that changes what a sentence asserts | MINOR, plus an erratum entry |
| A change to an argument, a conclusion or a claim class | MAJOR, plus a new pinned archive of the previous version |

## Developer certificate of origin

By contributing you certify that you wrote the contribution or have the right to submit
it, and that it may be published under the licences in `LICENSE` and `LICENSE-CODE`.

## Conduct

`CODE_OF_CONDUCT.md`. In short: argue with the work, not the person.
