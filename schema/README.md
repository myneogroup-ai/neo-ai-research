# Structured data

Every entity has one `@id` and is referenced by `@id` everywhere. A node is never
restated inline in a second block, because two nodes describing one work with different
identifiers is the duplicate signal this architecture exists to avoid.

## The governing rule

**Structured data must never assert more than the visible page.** Every property in a
JSON-LD block corresponds to something a reader can see. No hidden authorship, no
invented date, no rating, no count that is not rendered, no `about` entity the page does
not discuss.

The build validates each property against the rendered DOM and fails on any property
without a rendered counterpart. That check is the reason the property set below is fixed
rather than open.

## Files

| File | Contains |
|---|---|
| `entities.jsonld` | The graph: Person, the three Organizations, the SoftwareApplication, the DefinedTermSet, the Dataset. Emitted once, referenced everywhere |
| `article.template.jsonld` | ScholarlyArticle and TechArticle. One per publication page |
| `breadcrumb.template.jsonld` | BreadcrumbList. Publication, category, term and figure pages |
| `collectionpage.template.jsonld` | Library, category and topic hub indexes |
| `founder.template.jsonld` | BlogPosting for thesis, notes and essays; WebPage for a selection page |
| `capabilities-v1.json` | JSON Schema for the capability register |

## Type selection

| Type | Applied to |
|---|---|
| `ScholarlyArticle` | Research papers and institutional publications |
| `TechArticle` | Technical notes |
| `DefinedTermSet`, `DefinedTerm` | The glossary |
| `Dataset` with `DataDownload` | The Capability Register and `capabilities.json` |
| `BlogPosting` | Thesis pieces, essays and notes on the founder site |
| `WebPage` with `about` | Platform and company pages |
| `CollectionPage` | Library, category and topic hub indexes |

## The claim-class property set

The most valuable structured-data decision available to this corpus, and it is specific
to it. Each article carries a `variableMeasured` set of four `PropertyValue` nodes
holding the claim-class counts, computed from the evidence table at build time and
rendered on the page. A retrieval system reading only the structured data learns that
this corpus distinguishes evidence from interpretation from intent from an open question.

The counts are computed, never typed. A typed count goes stale on the next edit and
becomes a false machine-readable claim made by a corpus whose whole argument is about not
making false claims.

## What must never appear

- Any property without a rendered counterpart
- `Review`, `AggregateRating`, `Rating` or any review-adjacent type. The corpus has no
  reviews and inventing the markup invents the reviews
- `interactionStatistic`, view counts, download counts, citation counts
- A `BreadcrumbList` that exists only in markup
- A `datePublished` earlier than the real one, or a `dateModified` advanced by a rebuild
- A `citation` the page does not render in its references or related sections
- A second `ScholarlyArticle` node for a work already in the graph
- A capability status not resolved from the register at build time
- A `DefinedTerm` description differing by one byte from the rendered definitional
  sentence
- `citation_technical_report_number` where no identifier is allocated. It is omitted
  rather than filled with a requested one
