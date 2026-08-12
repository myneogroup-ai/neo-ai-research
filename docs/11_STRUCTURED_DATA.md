# Structured data

See `schema/README.md` for the files. This document states the rules the files implement.

## The governing rule

**Structured data must never assert more than the visible page.**

Every property in a JSON-LD block corresponds to something a reader can see. No hidden
authorship, no invented date, no rating, no count that is not rendered, no `about` entity
the page does not discuss. The build validates each property against the rendered DOM and
fails on any property without a rendered counterpart.

This is the rule the corpus is most likely to break, because emitting a richer block is
always tempting and nothing visibly goes wrong when you do. A `ScholarlyArticle` asserting
citations the page does not render is a false machine-readable claim made by a corpus whose
entire argument is about not making false claims.

## The entity graph

One `@id` per entity, referenced by `@id` everywhere, never restated inline.

| Entity | `@id` |
|---|---|
| `Person`, Mickael Mosse | `https://mickaelmosse.ai/about/#person` |
| `Organization`, NEO AI Research | `https://neoai.myneogroup.com/research/about/#neo-ai-research` |
| `Organization`, NEO TECH LABS | `https://neoai.myneogroup.com/company/#neo-tech-labs` |
| `Organization`, My NEO Group | `https://myneogroup.com/#my-neo-group` |
| `SoftwareApplication` and `Brand`, NEO AI | `https://neoai.myneogroup.com/#neo-ai` |
| `DefinedTermSet` | `https://neoai.myneogroup.com/research/glossary/#set` |
| `DefinedTerm` | `https://neoai.myneogroup.com/research/glossary/<term>/#term` |
| `Dataset`, Capability Register | `https://neoai.myneogroup.com/research/capability-register/#dataset` |
| `ScholarlyArticle` or `TechArticle` | `<canonical-url>#article` |
| `BreadcrumbList` | `<canonical-url>#breadcrumb` |

Footer link elements on every page of both hosts:

```html
<link rel="me"        href="https://mickaelmosse.ai/about/">
<link rel="author"    href="https://mickaelmosse.ai/about/">
<link rel="publisher" href="https://neoai.myneogroup.com/research/about/">
```

A person writes; an organisation publishes. The split is the correct expression of the
model.

**`sameAs` discipline is strict.** Real, controlled, and reciprocal where the platform
allows. A `sameAs` to a profile that does not link back is an unverifiable assertion and is
removed. **An ORCID identifier is registered before first publication** and appears on the
`Person` and on every article's author reference.

## The claim-class property set

The most valuable structured-data decision available to this corpus.

```json
"variableMeasured": [
  {"@type": "PropertyValue", "name": "claims-established",
   "value": 13, "description": "Statements of established fact, each with an external primary source"},
  {"@type": "PropertyValue", "name": "claims-architectural-interpretation",
   "value": 23, "description": "Inferences from established premises, held by the Program and not proved"},
  {"@type": "PropertyValue", "name": "claims-design-intent",
   "value": 13, "description": "Statements of design intent, each carrying a capability status"},
  {"@type": "PropertyValue", "name": "claims-open-problem",
   "value": 6,  "description": "Named unsolved problems"}
]
```

Counts are computed from the evidence table at build time and rendered on the page. A typed
count goes stale on the next edit and becomes exactly the false claim the rest of this
document exists to prevent.

## Typed relations

| Relation | schema.org | Note |
|---|---|---|
| `extends`, `refines`, `depends-on` | `isBasedOn` | |
| `evidences`, `applies` | `citation` | |
| `supersedes` | `sameAs` on the archived version, plus a visible banner | |
| `contradicts` | `citation`, plus a visible relation block naming the contradiction | No faithful property exists. The visible page is authoritative and the markup does not attempt to encode disagreement it cannot express |

## Highwire tags

On every publication canonical page: `citation_title`, `citation_author`,
`citation_publication_date`, `citation_technical_report_institution`,
`citation_technical_report_number`, `citation_pdf_url`.

**`citation_technical_report_number` is omitted where no identifier is allocated**, rather
than filled with a requested one. R-009 therefore carries no report number until its
identifier lands, and the page says so.

## Validation, in the build

| # | Check |
|---|---|
| SD1 | Every JSON-LD block parses and validates against schema.org |
| SD2 | Every property has a rendered counterpart in the DOM |
| SD3 | Every referenced `@id` resolves to a node defined once in the graph |
| SD4 | Every `sameAs` target returns 200 and links back |
| SD5 | Every `DefinedTerm` description is byte-identical to the rendered definitional sentence |
| SD6 | `variableMeasured` counts equal the counts rendered on the page and in the evidence table |
| SD7 | No prohibited type appears |
| SD8 | `citation_technical_report_number` is absent where no identifier is allocated |
| SD9 | No two `ScholarlyArticle` nodes share a `name` across both hosts |
| SD10 | Every capability status in markup matches `capabilities.json` at build time |

## Never

A `Review`, `AggregateRating` or `Rating`; the corpus has no reviews and the markup would
invent them. `interactionStatistic`, view counts, download counts, citation counts. A
`BreadcrumbList` that exists only in markup. A `datePublished` earlier than the real one or
a `dateModified` advanced by a rebuild. An `about` entity the page does not discuss. A
`citation` the page does not render. A second `ScholarlyArticle` for a work already in the
graph. A capability status not resolved from the register at build time. An `offers` node
on the `SoftwareApplication`, because the product is not generally available and markup
saying otherwise is a false claim in the plainest sense.
