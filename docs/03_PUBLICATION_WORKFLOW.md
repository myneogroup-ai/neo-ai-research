# Publication workflow

How a document becomes a page. Seven stages, and no stage is skipped because a date
exists.

```
draft -> classification review -> reduction, if needed -> gate A, machine
      -> gate B, independent read -> gate C, release read -> publish
```

## 1. Draft

Drafted outside this repository. A public repository is not a drafting surface: a draft
pushed to a branch is public, and a draft is exactly where an unreduced sentence lives.

## 2. Classification review

Before any text enters `content/`, the document is classed against
`docs/07_CLASSIFICATION_POLICY.md`. Three outcomes.

| Outcome | Next |
|---|---|
| Class A as written | Straight to gate A |
| Class A after reduction | Produce the public edition. It is a new artefact |
| Class B or C | Not published. Recorded in the register as withheld, with the reason |

## 3. Reduction, where required

A **reduction** publishes the principle and withholds the parameter. It is not a summary
and it is never a paraphrase of a withheld passage.

The reduction states, on the page, what was withheld and why. Readers are more willing to
trust a corpus that says "the coefficients are withheld" than one that quietly has no
coefficients in it.

## 4. Register entry

`registers/publications.json` gains the entry: identifier, title, category slug, slug,
canonical URL, schema type, wave, related. The canonical URL is derived from the route
template rather than typed, and `verify_public.py` check `REG-02` fails if it disagrees.

The slug is chosen once here and is frozen from first publication.

## 5. Gate A, machine

```
python3 scripts/verify_public.py --self-test
python3 scripts/verify_public.py
python3 scripts/build_indexes.py --check
python3 scripts/gen_seo.py --check
```

Everything mechanical: classification patterns, comparison prohibitions, claim classes,
capability keys against the register, house style, structure, register agreement.

Gate A cannot pass a document that is not in the register, and it cannot pass a register
entry with no document. Neither half publishes alone.

## 6. Gate B, independent read

One named reviewer per document. **The reviewer may not be the document's author.** This
is the largest human item in a release and it is the one that gets compressed when a
launch date exists, which is why it is a named person per document rather than a team
sign-off.

The reviewer reads for what the machine cannot see.

| Question | Why it is here |
|---|---|
| Does any paragraph reveal an architecture through description without using a listed word | The pattern matcher catches shapes it was told about |
| Does any sentence read as deployed when the status says specified | Tense does this silently |
| Is any claim stronger than its class permits | Weakening is allowed. Strengthening is not |
| Does any `[E]` claim rest on a source that does not support it | A cited source is not a supporting source |
| Would a competitor learn a setting from this | The reduction test, applied by a person |

## 7. Gate C, release read

Run once per release, not per document.

- Every gate B sheet signed, none by the document's author
- The corpus reads honestly as a whole: the library lists what exists, the roadmap carries
  no dates, no page presents a publication count as an achievement
- **The adversarial read**: a reviewer who has not worked on the corpus reads the site and
  answers one question. *Does this read as a description of a system that exists?* If the
  answer is yes, the release stops. Most capabilities are at S4 and S5, and a site that
  reads as a product tour has overclaimed regardless of what each status token says

## 8. Publish

`docs/04_DEPLOYMENT.md`. Phase A places content live and unlinked. Phase B links it into
navigation and is the publication moment.

## Corrections after publication

Errata, never silent fixes. The policy is the reason a correction is welcome rather than
embarrassing.

| Change | Version | Public record |
|---|---|---|
| Typography, formatting, a link | None | None |
| A correction changing what a sentence asserts | MINOR | An erratum on `/research/updates/` |
| A change to an argument, a conclusion or a claim class | MAJOR | An erratum, a pinned archive of the previous version, a supersession banner |
