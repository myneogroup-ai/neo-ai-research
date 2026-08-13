# Deployment

Five phases. The first three are reversible in minutes; the fourth is not reversible at
all in one specific respect, and that is why seven days sit in front of it.

| Phase | What happens | Reversible | Authorisation |
|---|---|---|---|
| **S** | Staging: no-index, HTTP authentication, no sitemap submitted | Entirely | Release authorisation |
| **A** | Content live on the canonical host, unlinked from navigation | Minutes, by unlinking | Publication authorisation, part 1 |
| **B** | `/research/` linked into primary navigation. **The publication moment** | Under 30 minutes, by reverting the build | Publication authorisation, part 1 |
| **D** | Redirects and canonical transfer | Routing yes. **An external citation made in the window, no** | Publication authorisation, part 2, at least seven days after B |
| **E** | Observation to day 21 against the rollback triggers | Not applicable | Standing |

There is no phase C. The lettering follows the publication plan the phases were named in
and is left alone rather than renumbered, because the authorisation documents refer to
these letters.

## Before anything: staging

Staging is verified against the same checks production will be, and **the rollback is
rehearsed and timed**. If the rehearsal takes over thirty minutes, publication is held
until it does not. A rollback plan that has never been executed is a document, not a
capability.

## Phase A, content live and unlinked

The content is reachable by direct URL and appears in no navigation, no index and no
submitted sitemap. It is real, it is public, and almost nobody will find it. That is the
point: it is the last cheap moment to discover that something renders wrongly in
production that rendered correctly in staging.

**Verify in production what was verified in staging.** A staging pass is not a production
pass, and the differences that matter are exactly the ones staging cannot reproduce.

## Phase B, the publication moment

`/research/` enters primary navigation. Both sitemaps are submitted. The publication date
and version of every document are recorded in the register.

## Phase D, redirects. The irreversible one.

Single-hop `301` from every retired route. `410 Gone` where no equivalent exists. The
identifier resolver moves and retains its `302`. The redirect block is retained for at
least 24 months.

**A version-pinned archive is never redirected forward.** It moves host with a `301` to
the pinned URL at the new host, never to the current version. Every migration tidies
redirects, and forwarding a pinned version to the current one looks like tidiness. It
falsifies the citation record and no rollback recovers it.

Verify before issuing, not after: every pinned URL resolves to its own pinned address.

### Why seven days

A redirect can be removed. **An external citation of a new canonical URL made during the
window cannot be recalled.** The seven days exist to find problems before any third party
has cited the new addresses. The observation record for those seven days is a
precondition of signing part 2, not a formality after it.

## Phase E, observation

| Day | Measure | Trigger |
|---|---|---|
| 7 | `hreflang` reciprocity errors | above 2 per cent |
| 14 | Indexed URLs against baseline | below 50 per cent |
| 21 | Organic entrances against the 28-day baseline | below 60 per cent |
| Continuous | Server errors | above 0.5 per cent |
| Continuous | Redirect chain or loop | any occurrence |
| Continuous | Pinned version redirected forward | any occurrence |
| Continuous | Classified material on a public page | any occurrence |

## The workflow

`.github/workflows/deploy.yml`, dispatched with a target, a site and a signed
authorisation reference. Both production targets are GitHub Environments with required
reviewers, so the deploy stops for a human approval at the moment it runs rather than
relying on one having happened earlier.

## Stop conditions

Stop and do not proceed if any of these occurs.

| Condition | At |
|---|---|
| Conformance does not pass without an explained change | Any phase |
| Any gate B sheet is unsigned, or signed by the document's author | Before S |
| The adversarial read answers yes to "does this read as a system that exists" | Before S |
| The rollback rehearsal exceeds 30 minutes | S |
| Any pinned version resolves to anything but its own address | D |
| Classified material is found on a public page | Any phase from A |
