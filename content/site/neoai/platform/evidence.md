---
route: /platform/evidence/
title: Evidence, memory and provenance
host: neoai.myneogroup.com
source: NEO AI x100 architecture authority (2026), sections 02, 20, 25
classification: A
updated: 2026-10-18
---

# Evidence, memory and provenance

## Header

**Where an answer came from, and what the system is allowed to keep**

## Body

Two different questions get confused and the confusion is expensive. *What has this system seen* is a memory question. *What does this system assert about the world, and on what basis* is a knowledge question. A store designed to answer the first cannot answer the second, however large its context window.

NEO AI separates them. Memory holds what the system retains about its own operation, persistent, verified and with provenance. `[D] (core.memory, S3)` The Knowledge Plane holds what it asserts about the world, with evidence attached. `[D] (core.knowledge-graph, S4)`

Three evidence objects, with non-overlapping meanings: the **Evidence Layer** produces, grades and serves evidence; the **Evidence Ledger** stores evidence records; an **Evidence Chain** is the traversal from a claim back through its transformations to its originating sources. `[D] (core.evidence-layer, S4)` `[D] (core.evidence-ledger, S4)`

## Minimum authoritative context

Rather than sending an entire history to every model invocation, NEO builds the minimum authoritative context a task needs, with provenance and continuity preserved. `[D] (x100.context-optimisation, S3)`

## Corroboration is counted by origin, not by document

Five documents that all restate one press release are one source. Detecting that is a specific technical problem, it has a name, and the method is published.

[Detecting Circular Corroboration in an Evidence Chain](/research/technical-notes/circular-corroboration/)

## Compounding without training on customer content

Mission execution data, evaluation signals, routing performance, outcome telemetry and verification performance improve how NEO allocates resources. No weights change. Training-eligible data is a separate category, governed by explicit policy, consent and lawful basis. Help Improve NEO is off by default and independent of every context grant, and customer confidential information is never automatically used to train models. `[D] (compounding-loop, S4)`

## Status

Memory: implemented and in validation. `[D] (core.memory, S3)` Knowledge Graph and the evidence objects: designed and specified. `[D] (core.evidence-layer, S4)` The learning loop: designed and specified. `[D] (compounding-loop, S4)`

---
