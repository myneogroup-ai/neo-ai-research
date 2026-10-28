# Canonical URL map

**The rule, once.** Each site is canonical for what it wrote. Neither renders the other's
body. Where substantially the same institutional research would exist on both,
`neoai.myneogroup.com` is canonical and the other carries an explicit cross-host
canonical to it.

Every canonical URL in this repository is **derived** from
`registers/publications.json` through the route template, and `verify_public.py` check
`REG-02` fails on any disagreement. A URL is never typed into a page.

```
https://neoai.myneogroup.com/research/{category_slug}/{slug}/
```

## 1. neoai.myneogroup.com

### 1.1 Research

| Route | Renders | Canonical | Robots | Sitemap |
|---|---|---|---|---|
| `/research/` | Library index, from the register | self | `index, follow` | indexes |
| `/research/papers/` | Category index, R | self | `index, follow` | indexes |
| `/research/papers/<slug>/` | A research paper | self | `index, follow, max-snippet:-1, max-image-preview:large` | publications |
| `/research/institutional/` | Category index, P | self | `index, follow` | indexes |
| `/research/institutional/<slug>/` | An institutional publication | self | as above | publications |
| `/research/technical-notes/` | Category index, TN | self | `index, follow` | indexes |
| `/research/technical-notes/<slug>/` | A technical note | self | as above | publications |
| `/research/methodology/` | Claim classes, evidence tiers, how to cite, review process | self | `index, follow` | indexes |
| `/research/capability-register/` | The ledger, from the register | self | `index, follow` | capability |
| `/research/capability-register/<key>/` | One page per capability, 24 | self | `index, follow` | capability |
| `/research/glossary/` | The term set | self | `index, follow` | glossary |
| `/research/glossary/<term>/` | One page per defined term | self | `index, follow` | glossary |
| `/research/authors/`, `/research/authors/mickael-mosse/` | Author index and page | self | `index, follow` | indexes |
| `/research/updates/` | Corpus changelog: versions, errata, corrections | self | `index, follow` | indexes |
| `/research/about/` | **`Organization` entity page** | self | `index, follow` | indexes |
| `/research/roadmap/` | Registered and not drafted. **No dates** | self | `index, follow` | indexes |

**`max-snippet:-1` is deliberate.** Restricting snippet length reduces the probability
that a retrieval system can quote enough of the material to attribute it correctly. For a
corpus whose purpose is to be cited, an unrestricted snippet is the correct trade.

### 1.2 Topic hubs

Cross-category, labelled on the page as topic hubs.

| Route | Gathers |
|---|---|
| `/research/topics/system-intelligence/` | R-009, P-001, R-001 |
| `/research/topics/mission-control/` | R-003, TN-001, TN-003 |
| `/research/topics/evidence-memory/` | R-005, TN-002 |
| `/research/topics/multi-model/` | R-001, R-009 |
| `/research/topics/governance/` | R-003, P-007, TN-001 |

`/research/topics/private-ai/` is **not created**, because R-004 is registered and not drafted
and the hub would list nothing. A hub that lists a title which does not resolve is a
broken-link surface and reads as inflation.

### 1.3 Identifier, binary and figure routes

| Route | Behaviour |
|---|---|
| `/id/<PUBID>` | **`302`** to the canonical. The single resolver |
| `/id/<PUBID>/v<M>.<m>` | `302` to the pinned version |
| `/pdf/<PUBID>/v<M>.<m>.pdf` | The binary. `X-Robots-Tag: index, noarchive`. HTTP `Link` header canonical to the HTML |
| `/pdf/<PUBID>/latest.pdf` | `302` to the current version |
| `/research/figures/<PUBID>-<n>/` | Figure permalink. None in Wave 1 |
| `/capabilities.json` | The machine-readable register |
| `/llms.txt`, `/robots.txt`, `/sitemap.xml` | Generated |

### 1.4 Version-pinned archives

`/research/<category>/<slug>/v<M>.<m>/`

**Self-canonical. `noindex, follow`. Excluded from every sitemap. Never redirected
forward.** Carries a banner naming the version, the date it was superseded and the
version that superseded it.

`gen_seo.py` asserts on its own output that no pinned URL reached a sitemap, rather than
assuming it from the input. The assumption is the thing that fails.

### 1.5 Platform and company

`/`, `/platform/`, `/platform/system-intelligence/`, `/platform/mission-control/`,
`/platform/observe-build/`, `/platform/lili/`, `/platform/evidence/`,
`/platform/governance/`, `/platform/security/`, `/platform/deployment/`,
`/platform/x100/`, `/platform/execution-fabric/`, `/platform/intelligence-profiles/`,
`/platform/model-sovereignty/`, `/platform/verticals/`, `/platform/neo-intelligence/`,
`/platform/business-model/` (added 2026-10-18 with corpus 0.2.0), `/company/`,
`/company/contact/`. All self-canonical, `index, follow`.

The live site navigation (NEO AI, Platform, LILI and Product, Live demo, x100,
Architecture, Solutions, Business, Research, Investors) may present these routes as
sections of fewer pages. The routes above remain the canonical, citable addresses of the
content in this repository. The Investors area is access-controlled and none of its
content is, or may be, in this repository.

`/search/` is `noindex, follow`. Any filtered index carrying a query parameter canonicals
to the unfiltered index and is `noindex, follow`.

## 2. mickaelmosse.ai

| Route | Renders | Canonical | Robots |
|---|---|---|---|
| `/` | Thesis in one screen | self | `index, follow` |
| `/thesis/`, `/thesis/<slug>/` | Original founder writing | **self** | `index, follow, max-snippet:-1` |
| `/research/` | Curated index. Titles plus one line each | self | `index, follow` |
| `/research/<slug>/` | **200-word verbatim abstract plus original framing** | **self** | `index, follow` |
| `/research/<slug>/notes/` | Founder annotation | self | `index, follow` |
| `/notes/`, `/essays/` | Working notes and essays. **Non-publication banner** | self | `index, follow` |
| `/about/` | **`Person` entity page** | self | `index, follow` |
| `/now/` | Current work | self | `index, follow` |

**Why the selection page is self-canonical.** A cross-host canonical tells a search engine
to attribute the page to the target and drop this one. That is right for a duplicate. It
is wrong for 200 words of quotation inside original framing, and it would discard the
founder site's authority over its own writing. The bound is what makes it safe, and the
build enforces the bound rather than trusting the author.

**The one condition that reverses it.** If a selection page ever renders more than the
bounded abstract it becomes a duplicate and must carry a cross-host canonical to
`neoai.myneogroup.com`. The build fails before that ships.

**The non-publication banner.** Every page under `/notes/` and `/essays/` declares that it
is not a NEO AI Research publication, carries no publication identifier and makes no
capability claim. The build fails on any occurrence of a capability register key in those
source trees.

## 3. Cross-host canonical direction, complete

| Content | Canonical owner | The other site |
|---|---|---|
| Publication full text | `neoai` | never renders it |
| Publication abstract | `neoai` | 200 words verbatim, bounded |
| Founder framing, annotation, thesis, essays, notes | `mickaelmosse.ai` | `neoai` links, never reproduces |
| Glossary | `neoai` | links only |
| Capability Register | `neoai` | links only |
| Identifier resolver | `neoai` | `301` |
| PDF binaries | `neoai` | links only |
| `Person` entity | `mickaelmosse.ai` | referenced by `@id` |
| `Organization`, NEO AI Research | `neoai` | referenced by `@id` |
| `Organization`, NEO TECH LABS | `neoai` | referenced by `@id` |

**Zero cross-host canonicals point away from `neoai.myneogroup.com` for institutional
research.**

## 4. Language

**English lives at the root. No `/en/` prefix, now or ever.**

A future language is added under a reserved prefix, `/<iso-639-1>/`, mirroring the English
tree exactly: `/fr/research/papers/<slug>/`. English URLs never move, so a multilingual
wave requires no migration and breaks no citation.

`hreflang` is reciprocal on every translated pair and `x-default` points at the English
URL. A translation is a separate `@id` in the entity graph and carries a cross-language
`sameAs` to its English original, never a canonical to it: a translation is not a
duplicate.

Reserved and unusable as a first path segment for any other purpose: every ISO 639-1
two-letter code.

## 5. Rules that survive any host move

Slugs frozen at first publication. No date and no version number in a path. No category
word duplicated in the path. One full text per publication, never a second rendering.
Three URL classes with three different guarantees: a canonical never redirects, an
identifier route always `302`s, a pinned version is immutable and is never redirected
forward. Filter parameters `noindex, follow`. The 200-word abstract bound. `lastmod`
advances only on a content change.

## 6. Structure frozen

The slug review is complete and this structure is frozen. Three decisions were taken at
the freeze and are not reopened.

| Decision | Refused alternative | Reason |
|---|---|---|
| `/research/institutional/` | `/research/publications/` | A paper *is* a publication. A sibling category named with a superset of its siblings is a taxonomy defect that never stops causing ambiguity |
| `/research/glossary/` | `/glossary/` | The term set is published by NEO AI Research and belongs inside its namespace. Root-level would split the corpus across two namespaces for one sitemap's benefit |
| `/research/topics/<topic>/` | `/research/<topic>/` | A flat namespace put topic hubs, categories and utility pages in one segment, where a future category named `governance` would collide with an existing hub. It also produced two URLs with the identical final slug on one host, competing for one query |
| `/research/capability-register/` | `/research/capability-ledger/` | `Capability Register` is a locked vocabulary term and the Dataset is already named that. A URL that disagrees with the locked term for the same entity is a permanent inconsistency |
