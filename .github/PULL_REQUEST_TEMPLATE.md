## What this changes

<!-- One or two sentences. What a reader of the site sees differently after this merges. -->

## Type

- [ ] Correction to a published document
- [ ] New publication or a new version of one
- [ ] Website copy
- [ ] Glossary or vocabulary
- [ ] Build, script, workflow, schema
- [ ] Documentation or housekeeping

## Classification declaration

Required on every pull request. Tick both or explain why not.

- [ ] This change adds **no** information about NEO AI internals that was not already
      published in this repository
- [ ] This change contains no service name, schema, contract, topology, threshold,
      coefficient, objective function, evaluation denominator, benchmark dataset, client
      name, financial figure, internal path, credential or token

If you cannot tick both, **stop and read `SECURITY.md`**. Do not open this pull request.

## Claim discipline

Complete for any change touching `content/papers/`, `content/institutional/` or
`content/technical-notes/`.

- [ ] Every new or changed material statement carries a claim class: `[E]`, `[A]`, `[D]`
      or `[O]`
- [ ] Every new `[E]` claim cites an external primary source
- [ ] Every new `[D]` claim carries a capability status resolved from
      `registers/capabilities.json`
- [ ] No claim has been **strengthened**. Weakening is permitted; strengthening is not
- [ ] No comparison against any named model, product or vendor has been introduced
- [ ] No capability is described as deployed unless its register status says so

## Versioning and errata

- [ ] No version change: typography, formatting, a broken link
- [ ] MINOR: a correction that changes what a sentence asserts. **An erratum entry is
      included in this pull request**
- [ ] MAJOR: a change to an argument, a conclusion or a claim class. **A pinned archive of
      the previous version is included**

Document and version affected: `NEO-AI-______` v___ to v___

## Canonical and citation integrity

Complete for any change touching a URL, a slug, a redirect or `registers/`.

- [ ] No slug of a published document has changed. Slugs are frozen at first publication
- [ ] No version-pinned archive URL is redirected forward
- [ ] The identifier route still resolves
- [ ] `registers/publications.json` and the content tree still agree

## Verification

```
python3 scripts/verify_public.py
python3 scripts/build_indexes.py --check
python3 scripts/gen_seo.py --check
```

- [ ] Run locally and passing
- [ ] CI green

Paste the conformance summary line:

```
```

## Review

- [ ] A code owner is assigned
- [ ] **I am not the author of the document this pull request reviews**, or this pull
      request is not a review

## Related

Closes #
