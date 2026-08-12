---
route: /platform/evidence/
title: Evidence, memory and provenance
host: neoai.myneogroup.com
source: PUB copy, SITE_COPY_neoai.myneogroup.com.md
classification: A
---

# Evidence, memory and provenance

## Header

**Where an answer came from**

## Body

Two different questions get confused and the confusion is expensive. *What has this system seen* is a memory question. *What does this system assert about the world, and on what basis* is a knowledge question. A store designed to answer the first cannot answer the second, however large its context window.

NEO AI is designed to separate them. The Memory Plane holds what the system retains about its own operation. The Knowledge Plane holds what it asserts about the world, with evidence attached.

Three evidence objects, with non-overlapping meanings: the **Evidence Layer** produces, grades and serves evidence; the **Evidence Ledger** stores evidence records; an **Evidence Chain** is the traversal from a claim back through its transformations to its originating sources.

## Corroboration is counted by origin, not by document

Five documents that all restate one press release are one source. Detecting that is a specific technical problem, it has a name, and the method is published.

[Detecting Circular Corroboration in an Evidence Chain](/research/technical-notes/circular-corroboration/)

## Status

Specified. Not running. `[D] (brain.evidence-layer, S4)` `[D] (brain.memory, S4)`

---
