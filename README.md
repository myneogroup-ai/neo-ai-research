# NEO AI Research

The public research corpus of the NEO AI Research Program.

This repository is the canonical public source for the Program's research papers,
institutional publications, technical notes, glossary, public architecture pages,
website content, and the SEO, structured data and AI discovery files that make all of
it machine readable.

Canonical host: **https://neoai.myneogroup.com**
Founder thesis layer: **https://mickaelmosse.ai**

---

## How to read this corpus

Every material statement carries a claim class. The classes are the point of the
corpus, not decoration on it.

| Class | Meaning | What it obliges |
|---|---|---|
| `[E]` | Established | An external primary source is cited |
| `[A]` | Architectural interpretation | An inference the Program holds and has not proved |
| `[D]` | Design intent | Carries a capability status from the register |
| `[O]` | Open problem | Named and unsolved |

A claim may be weakened between an internal document and a public one. It is never
strengthened.

Capability statuses resolve from `registers/capabilities.json`.

| Status | Meaning |
|---|---|
| S1 | Operational |
| S2 | In pilot |
| S3 | Validating |
| S4 | Designed and specified |
| S5 | Planned |

**Nothing in this corpus describes a deployed system unless its capability status says
so.** Most of what is described is at S4 or S5. That is stated on every page rather
than left to be discovered.

The Capability Register is Founder-ratified as the approved public representation of
the Program's S1-S5 maturity classifications. This register-level ratification does not
mean that every capability has lifecycle status RATIFIED: individual lifecycle states
remain separately evidence-gated. Pages render the register version so that maturity
claims remain traceable to the exact register state.

## What is here

```
content/papers/            Research papers          R
content/institutional/     Institutional papers     P
content/technical-notes/   Technical notes          TN
content/glossary/          Controlled vocabulary
content/site/neoai/             neoai.myneogroup.com site content
content/site/founder/           mickaelmosse.ai site content
registers/                 Machine readable state: publications, capabilities, vocabulary
schema/                    JSON-LD entity graph and templates
scripts/                   Index, SEO and conformance generators
static/                    robots.txt, llms.txt and generated discovery files
docs/                      Workflows: branch, release, publication, deployment, rollback
```

## What is deliberately not here

This repository is public. The following never enter it, in any form, including in a
branch, a draft, a comment, a commit message or a test fixture.

- Internal programme stages and their audit trails
- The Engineering Constitution and the Data Program
- Confidential technical architecture: component contracts, schemas, service inventories,
  deployment topology
- Trade secrets: the router score vector, objective functions, coefficients, thresholds,
  admissible-set predicates, the cost model
- Internal registers, internal evaluation methodology, benchmark datasets
- Named pilot clients and financial figures

`docs/07_CLASSIFICATION_POLICY.md` states the rule in full and `scripts/verify_public.py`
enforces the machine-checkable part of it in CI.

**The governing principle: publish the mechanism, withhold the setting.** A public paper
may describe that the system selects a model against an objective. It may not publish the
objective, its coefficients or its thresholds.

## Claims this corpus does not make

The Program publishes no benchmark, holds no reproducible comparison against any other
system and claims none. No page in this repository asserts that NEO AI is more capable
than any named model or product. A pull request that introduces such a comparison is
closed rather than revised.

## How to cite

Use the publication identifier and version, and the permanent identifier route.

```
NEO AI Research Program. "A Note on Responsible AI Capability Claims."
NEO-AI-P-007 v1.0. https://neoai.myneogroup.com/id/NEO-AI-P-007
```

The identifier route issues a `302` to the current canonical URL. A version-pinned
archive URL is immutable, self-canonical, and is never redirected forward, because
redirecting a pinned version silently falsifies the citation record.

`CITATION.cff` carries the machine-readable form.

## Contributing

Corrections are welcome and errata are published rather than quietly fixed. See
`CONTRIBUTING.md`. The fastest useful contribution is a factual correction with a
primary source attached.

## Licence

Content is licensed **CC BY 4.0** (`LICENSE`). Code, scripts and schema templates are
licensed **MIT** (`LICENSE-CODE`). Attribution requirements are in both files.

## Security and disclosure

`SECURITY.md`. Report a suspected disclosure of classified material through the private
channel named there, not as a public issue.
