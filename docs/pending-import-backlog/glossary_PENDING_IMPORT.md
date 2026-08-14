---
status: NON_RELEASE_BACKLOG
source_location: content/glossary/_PENDING_IMPORT.md
release_blocking: false
---

# Non-release content backlog

This record was moved outside the public `content/` tree during the final Wave-1 repository closure because it is not represented by a publishable entry in `registers/publications.json` and is not protected by an active release deferral. Its outstanding editorial work is preserved here without falsely representing that content as published.

---

---
status: PENDING IMPORT
classification: A - the term set is public, the source standard is not
---

# Pending import: the glossary

The controlled vocabulary is already machine readable at `registers/vocabulary.json`:
30 locked terms, 9 added by amendment, 39 in total, with the prohibited synonym and the
three disambiguation clauses. `scripts/build_indexes.py` generates the glossary index
from it today.

**What is missing is the definitions.** The source is an internal editorial standard, and
it is not publishable as it stands for three reasons.

1. It carries editorial notes flagging defects in inherited definitions for decision.
   Those are working annotations, not published text.
2. One section holds definitions marked as requiring approval and having no force until
   approved. Publishing an unapproved definition as canonical is exactly the kind of
   overclaim the corpus exists to avoid.
3. It records collisions and contradictions against internal governing documents by
   internal reference.

## What the public glossary is

A **reduction**: one page per term, carrying the definitional sentence, the expanded
note where the one-line form leaves an operational question open, the distinguish-from
line, related terms and the publications that use it. Editorial notes, approval markers
and internal cross-references do not survive the reduction.

The `DefinedTerm` description in structured data must be byte-identical to the
definitional sentence rendered on the page, and a divergence is a build failure. That
constraint is why the reduction is mechanical rather than a rewrite.

## What clears this

| Step | Owner |
|---|---|
| Approve the definitions currently marked as requiring approval, or drop those terms from the public set | Founder |
| Reduce the standard to the public term set, dropping editorial notes and internal references | Research Program |
| Import one file per term under `content/glossary/terms/` | Research Program |
| Regenerate the glossary sitemap, which is currently the set page alone | Build |

Until then the glossary index page renders the term list without definitions, and says
so. A term list without definitions is honest. An invented definition is not.
