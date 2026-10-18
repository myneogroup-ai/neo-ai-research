# Evidence, Memory and Accountability in Agentic Systems

**Why durable intelligence is a governance problem before it is a storage problem**

| Field | Value |
|---|---|
| Identifier | `NEO-AI-R-005` |
| Edition | **Public edition** of `NEO-AI-R-005 v1.0`. Reduced, not paraphrased |
| Version | v1.1-public |
| Status | DRAFT |
| Date | 2026-10-18 |
| Author | Mickael Mosse, NEO AI Research Program |
| Capability keys | `core` S2 . `core.memory` S3 . `core.knowledge-graph` S4 . `core.evidence-layer` S4 . `core.evidence-ledger` S4 . `core.verification` S3 . `core.governance` S3 . `compounding-loop` S4 |
| Claim-class counts | `[E]` 10 . `[A]` 18 . `[D]` 13 . `[O]` 12 . Counted by script over the body and back matter, excluding this row |
| Reading time | 17 min |
| Canonical URL | `https://neoai.myneogroup.com/research/papers/evidence-memory-accountability/` |
| Relations | `applies` NEO-AI-R-009 . `refines` NEO-AI-TN-002 . `evidences` NEO-AI-P-001 |
| Withheld | One section removed entirely, three reduced. Section 7 states what and why |

---

## Abstract

Two questions are routinely confused and the confusion is expensive. *What has this system seen* is a memory question. *What does this system assert about the world, and on what basis* is a knowledge question. A store designed to answer the first cannot answer the second, however large its context window and however good its retrieval.

This paper separates them. The **Memory Plane** holds what a system retains about its own operation. The **Knowledge Plane** holds what it asserts about the world, with evidence attached, temporal validity, and a traversable path back to origin.

Three consequences follow. Deletion becomes a lineage problem rather than a search problem. Corroboration has to be counted by distinct origin rather than by document. And the write path, not the read path, is where accountability is won or lost.

This public edition withholds the store model's authority column, the promotion rule set, the claim record structure, and one section in full. Nothing withheld is paraphrased.

---

## 1. Problem framing

An agentic system that runs for a year accumulates two different things and they need different treatment.

It accumulates **operational history**: what it was asked, what it did, what worked, what failed, which strategy it used, how long things took. This is memory about itself. Its consumer is the system and its operators.

It accumulates **assertions about the world**: this counterparty is registered in that jurisdiction, this clause caps liability at that level, this entity has that beneficial owner. This is knowledge. Its consumer is a person who will act on it, and who will be asked to justify having done so.

Storing both in one place, which is what a general-purpose vector store invites, produces three failures `[A]`.

**The first is that an assertion loses its basis.** Retrieved as text, a claim arrives without the source that supported it, the date on which it was true, or the process that validated it. It is indistinguishable from a claim the system generated.

**The second is that deletion becomes impossible to reason about.** Removing a document does not remove the claims derived from it, the summaries that absorbed it, or the embeddings computed from it.

**The third is that corroboration becomes a count of documents.** Five retrieved passages agreeing looks like strong support, and if all five restate one press release it is one source.

The paper's position is that these are governance failures with a storage symptom, not storage failures. They are solved by structure at the write path, not by a better index at the read path.

---

## 2. What the established work supports

**Retrieval grounds generation and does not validate the source.** Retrieval-augmented generation established that grounding output in retrieved documents reduces unsupported assertion on knowledge-intensive tasks `[E]` (Lewis et al., 2020). What it did not establish, and what this paper is about, is whether the retrieved document is itself reliable.

**Provenance has a published standard and a settled data model.** The W3C PROV data model provides an established vocabulary for entities, activities and agents, and the derivation relations between them `[E]` (W3C, 2013). The Program uses its distinctions rather than reinventing them.

**Bitemporal modelling is an established solution to the two-dates problem.** Distinguishing the time a fact was true in the world from the time a system recorded it is standard practice in data management `[E]` (Snodgrass, 1999).

**Data protection law imposes erasure obligations that reach derived data.** Published regulation requires that erasure extend to data derived from the erased subject, which is why deletion is a lineage problem `[E]` (Regulation (EU) 2016/679).

**What none of this establishes.** No published work known to the Program establishes a complete method for erasing a subject's contribution from a model-derived artefact such as an embedding or a fine-tuned weight `[O]`. That gap is real and section 6 records it.

---

## 3. Two planes, five stores, one claim

### 3.1 The Memory Plane and the Knowledge Plane are different things

The **Memory Plane** holds what the system retains about its own operation: episodes, outcomes, strategies used, failures encountered. Its questions are of the form *have I done this before, and how did it go*.

The **Knowledge Plane** holds what the system asserts about the world: claims, their evidence, their temporal validity, their origin. Its questions are of the form *what do we hold to be true about this entity, on what basis, and as at when* `[A]`.

The separation is not organisational tidiness. It is that the two have **different write authorities, different retention rules, different erasure obligations and different failure modes**. An episode is a record of something the system did and is true by construction. A claim is an assertion about the world and can be wrong. Treating a claim as though it were an episode is how a generated statement acquires the authority of a recorded fact.

### 3.2 What the five stores are for

Reduced in this edition. The source specifies each store's write authority and read scope, and that column is withheld, because it is the differentiating design.

Publishable: the Memory Plane comprises an **episodic** store of what happened and a **semantic** store of what has been learned from repetition. In NEO AI, Memory, persistent, verified and carrying provenance, is implemented and in validation `[D] (core.memory, S3)`. The Knowledge Plane is specified to hold a **claim** store of assertions, an **evidence** store of the records supporting them, and an **entity** store resolving the things claims are about; it is designed and specified and is not yet in operation `[D] (core.knowledge-graph, S4)`.

### 3.3 What promotion requires

Reduced. The complete rule set is withheld.

The publishable principle is a single sentence and it is the important one. **Promotion from episodic to semantic requires evidence that is not the episode itself**: a verification result, a recorded human judgement, or corroboration from a distinct origin. An episode repeating is not evidence that it was right; it is evidence that it happened again `[A]`.

The prohibited transition is direct promotion of a generated assertion into the claim store without an evidence record. That is the single edit that would collapse the whole structure into a vector store with extra vocabulary.

### 3.4 What a claim must carry

Withheld. The source specifies the record's fields and the structure is CONFIDENTIAL TECHNICAL ARCHITECTURE.

What is publishable is what a claim must carry, expressed as obligations rather than as fields: **its origin, the evidence supporting it, the period over which it is asserted to hold, and the actor and process that recorded it.** A claim missing any of the four is not usable in a justification, which is the only use a claim has.

### 3.5 Evidence Layer, Evidence Chain, Evidence Ledger

Three objects with non-overlapping meanings, and using one for another is a terminology failure the corpus treats as a defect.

| Term | Is | Is not |
|---|---|---|
| **Evidence Layer** | A component grouping in the Knowledge Plane that produces, grades and serves evidence | Not a store, not a path |
| **Evidence Chain** | The traversal path from one material claim back through its transformations to its originating sources; per claim, computed on demand | Not a component, not a store |
| **Evidence Ledger** | An append-only, hash-addressed store of evidence records | Not a graph, not a path |

The only correct phrasing of the relationship, as NEO AI specifies it: **the Evidence Layer writes records to the Evidence Ledger; an Evidence Chain is traversed across those records for a given claim** `[D] (core.evidence-layer, S4)`. The Evidence Layer and the Evidence Ledger are both designed and specified and are not yet in operation `[D] (core.evidence-ledger, S4)`.

### 3.6 Temporal validity has three dates and a fourth obligation

A claim carries three dates and they answer different questions.

**Valid from** is when the fact became true in the world. **Recorded at** is when the system learned it. **Asserted until** is the point beyond which the claim is not held without rechecking.

The three are independent. A fact may have become true two years before the system recorded it, and a system that conflates the two will answer *what did we believe in March* with what it believes now.

The fourth obligation is the one usually missed: **a claim must carry a recheck condition, not only an expiry.** Some facts decay on a schedule and some decay on an event. A registered address expires by time. A beneficial ownership claim expires when the entity restructures, which is not on a calendar. A model that supports only time-based expiry will hold stale claims confidently `[A]`.

---

## 4. Architectural interpretation

### 4.1 Deletion is a lineage problem, and without lineage it is probabilistic

An erasure obligation is not satisfied by deleting the document. The document contributed to claims, the claims contributed to conclusions, the conclusions were summarised, and the summaries were embedded.

If the system did not record the derivation at the time of writing, then at deletion time it can only **search** for the subject's contribution. Search finds what matches. It does not find a paraphrase, an inference or an aggregate `[A]`.

The consequence is structural and it decides an architecture. **Erasure capability is created at the write path or it does not exist.** A system that records what each artefact was derived from can compute the closure of an erasure and act on it. A system that does not can only make a probabilistic effort, and a probabilistic effort against a legal obligation is a compliance position nobody wants to defend.

Two residues remain honest to name. An embedding computed from erased text is a derived artefact whose relationship to the source is not invertible, and no complete published method exists for removing a subject's contribution from it `[O]`. And an append-only record designed never to change is in genuine tension with an obligation to delete, which section 6 records rather than resolves.

### 4.2 The write path is the attack surface

Most attention on agentic memory goes to the read path: retrieval quality, ranking, context assembly. The security problem is on the write path.

Content reaching a persistent store can influence every later retrieval from it. An instruction embedded in an ingested document, an assertion planted in a source the system trusts, or a poisoned summary promoted into semantic memory persists and is re-served, and it arrives at the reader carrying the authority of the store rather than of the source `[E]` (OWASP, 2025).

The design consequence: **the write path requires the same governance as an action**, because it is one. What may be written, by what authority, into which store, with what evidence, is a policy decision evaluated per write, and promotion between stores is a governed transition rather than a background process.

### 4.3 Circular corroboration: five articles, one origin

Corroboration counted by document is not corroboration.

Five retrieved articles asserting the same fact appear to be five independent supports. If all five derive from one press release, they are one support that has been reprinted, and the apparent independence is an artefact of the retrieval unit `[A]`.

This is not an edge case in evidence-intensive work; it is the normal condition of open-source material. A fact enters circulation once and is restated by aggregators, syndicators and secondary analysts, each of which is a distinct document and none of which is a distinct origin.

The requirement is therefore that **corroboration is counted over distinct origins rather than over retrieved artefacts**, which means an evidence record has to carry enough derivation information to establish whether two records share an origin. Below a policy-set number of distinct origins a claim stays unverified. **The number is not published**, because a published threshold is a published evasion target.

The detection method is published separately in a technical note.

### 4.4 Feedback contamination

A system that learns from its own outputs will, without a barrier, learn from its own errors.

The path is short. An assertion is generated, it enters the claim store, it is retrieved later as context, it supports a new assertion, and the new assertion is now corroborated by the first. Two claims, one origin, and the origin was the system `[A]`.

Three controls follow. An assertion generated by the system is marked as such at the point of writing and never acquires a different provenance later. A system-generated assertion **never counts as a distinct origin** for the corroboration test in section 4.3. And promotion out of episodic memory requires evidence that is not the episode, which is section 3.3 doing the same work from the other direction.

The general principle: **provenance is assigned at write time and is immutable thereafter.** A system that can relabel the origin of a claim can launder its own output into evidence.

The same barrier applies one level up, to a system that learns from its own operation. In NEO AI the system-level learning loop, the compounding loop, is designed to improve allocation from Mission execution data, evaluation signals, routing performance, outcome telemetry and verification performance, and is specified so that no model weights change `[D] (compounding-loop, S4)`. Training-eligible data is specified as a separate category under explicit policy, consent and lawful basis; Help Improve NEO is specified to be off by default; and customer confidential information is never to be used automatically to train models `[D] (compounding-loop, S4)`. The loop is not in operation, and the contamination argument of this section is one of the reasons its design keeps what improves allocation apart from what could become training material `[A]`.

---

## 5. Application to the NEO AI target architecture

Reduced in this edition.

Publishable: NEO AI is designed with the Memory Plane and Knowledge Plane separated; with derivation recorded at write time so that erasure is computable rather than searched for; with provenance assigned at write time and immutable; with corroboration counted over distinct origins; and with promotion between stores as a governed transition. The parts are not at the same status, and each is stated separately.

NEO Core, the orchestration layer of the Intelligence Operating System, is in operational deployment inside My NEO Group and in controlled pilot programmes with external users `[D] (core, S2)`. Memory, persistent, verified and with provenance assigned at write time, is implemented and in validation `[D] (core.memory, S3)`. Verification, which supplies the evidence that promotion requires, is implemented and in validation `[D] (core.verification, S3)`. Policy enforcement on the write path is implemented and in validation `[D] (core.governance, S3)`. The Knowledge Graph, the Evidence Layer and the Evidence Ledger, which carry the Knowledge Plane, the distinct-origin count and the computable erasure closure, are designed and specified and are not yet in operation `[D] (core.evidence-layer, S4)`.

The argument of section 3.1 extends to a separation the architecture keeps on every Mission: what is in a Mission's context, what is retained in memory, what is eligible for training, and what authority exists to act are four different things. Being connected to a source is not memory, memory is not training consent, and none of the three is authority to act `[A]`. Context is not promoted to memory by being seen, and memory is not made training-eligible by being retained; each transition is a governed one, which is the write-path argument of section 4.2 applied to the whole lifecycle `[A]`.

No independent party has verified any of these statuses, and this edition reports no measurement of them.

---

## 6. Failure modes and open problems

**Erasure from model-derived artefacts is unsolved** `[O]`. No complete published method removes a subject's contribution from an embedding or a fine-tuned weight. The Program does not claim one.

**Append-only integrity and erasure are in genuine tension** `[O]`. A record designed never to change and an obligation to delete pull in opposite directions. The Program has an approach and it is not published here.

**Origin resolution is hard and partially manual** `[O]`. Establishing that two documents share an origin is straightforward when one cites the other and difficult when both restate a third silently.

**Recheck conditions require domain knowledge** `[O]`. Knowing that a beneficial ownership claim expires on restructuring rather than on a date is not derivable from the claim itself.

**The write-path governance cost is unmeasured** `[O]`. Evaluating policy per write is more expensive than writing, and the Program holds no measurement of how much.

---

## 7. What this edition withholds, and why

| Withheld | Class | Reason |
|---|---|---|
| The store model's write-authority and read-scope columns | CONFIDENTIAL TECHNICAL ARCHITECTURE | The differentiating design. Section 3.2 publishes the five stores and their purposes |
| The complete promotion rule set and prohibited-transition matrix | CONFIDENTIAL TECHNICAL ARCHITECTURE | Section 3.3 publishes the governing principle |
| The claim record structure | CONFIDENTIAL TECHNICAL ARCHITECTURE | The exact memory implementation. Section 3.4 publishes the four obligations |
| The distinct-origin threshold | **TRADE SECRET** | A policy value. Naming the condition is publishable; naming the number is a published evasion target |
| **Source section 4.5, in full** | CONFIDENTIAL TECHNICAL ARCHITECTURE | **Removed entirely. Not reduced, not paraphrased, not summarised, and its subject is not named here.** It is a self-authored analysis of a security surface, and publishing it in any form would assist exactly the reader it is written to defend against. No derivative of it exists or will be attempted |

The last row is the one to notice. Everything else in this edition is a reduction: a principle published, a parameter withheld. That section is a deletion, and it is recorded as a deletion so that a reader comparing the public edition to a future internal reference does not conclude that something was hidden by accident.

---

## Scope and Limitations

This is a **public edition** of `NEO-AI-R-005 v1.0`: a reduction, with one section deleted in full. Withheld material is listed in section 7. **No withheld material is paraphrased, summarised or reconstructed**, and the deleted section's subject matter does not appear anywhere in this edition or in any other public artefact.

The paper reports **no measurement and no evaluation**. It makes no comparative claim against any named system.

**Correction (v1.1-public).** The first public edition stated that every capability named was at S4 in a provisional register and that nothing described was running. That is no longer true. On Founder determination of 2026-10-18, NEO Core is in operational deployment inside My NEO Group and in controlled pilot programmes with external users (S2). Memory, Verification and policy enforcement are implemented and in validation (S3). The Knowledge Graph, the Evidence Layer, the Evidence Ledger and the compounding loop are designed and specified (S4) and are not yet in operation. General public availability, global, is targeted for early 2027, a target and not a commitment. Register v1.3 was Founder-ratified on 2026-08-13; register v2.0 (2026-10-18) restructures it to the x100 architecture and is pending Founder ratification; no status has been verified by an independent third party.

It would be falsified by a demonstration that a general-purpose retrieval store, with no separation of memory from knowledge and no write-time derivation, supports erasure, corroboration and justification as well as the structure proposed here.

## Related Research

- `NEO-AI-R-009` From Model Intelligence to System Intelligence. Places evidence and memory among the eight operations.
- `NEO-AI-R-003` Mission Control: A Governance Architecture for Autonomous Work. Public edition. The record half.
- `NEO-AI-R-006` The Intelligence Layer. Registered, not drafted. Retitle pending, per the recorded editorial determination.

## Related Publications

- `NEO-AI-P-001` Introducing NEO AI: Intelligence Orchestrated.
- `NEO-AI-P-007` A Note on Responsible AI Capability Claims.

## Related Technical Notes

- `NEO-AI-TN-002` Detecting Circular Corroboration in an Evidence Chain. The method behind section 4.3.
- `NEO-AI-TN-003` What Belongs in a Mission Event.

## Related Architecture

None in this wave. CONFIDENTIAL TECHNICAL ARCHITECTURE.

## Related Engineering

None in this wave.

## Related Figures

None in Wave 1.

## Related Terms

`Memory Plane` . `Knowledge Plane` . `Evidence Layer` . `Evidence Chain` . `Evidence Ledger` . `Circular Corroboration` . `Claim Class` . `Verification Layer` . `Human Authority`

## Evidence Table

| # | Claim | Class | Source | Capability |
|---|---|---|---|---|
| 1 | Grounding generation in retrieved documents reduces unsupported assertion | `[E]` | Lewis et al., 2020 | |
| 2 | A published provenance data model exists with settled entity, activity and agent distinctions | `[E]` | W3C, 2013 | |
| 3 | Bitemporal modelling separates world time from record time | `[E]` | Snodgrass, 1999 | |
| 4 | Data protection law extends erasure obligations to derived data | `[E]` | Regulation (EU) 2016/679 | |
| 5 | Content reaching a persistent store can influence every later retrieval from it | `[E]` | OWASP, 2025 | |
| 6 | Memory and knowledge have different write authorities, retention rules and failure modes | `[A]` | | `core.memory` S3 |
| 7 | Promotion requires evidence that is not the episode itself | `[A]` | | `core.knowledge-graph` S4 |
| 8 | A claim requires a recheck condition, not only an expiry | `[A]` | | |
| 9 | Erasure capability is created at the write path or it does not exist | `[A]` | | |
| 10 | The write path requires the same governance as an action | `[A]` | | `core.governance` S3 |
| 11 | Corroboration counted by document is not corroboration | `[A]` | | `core.evidence-layer` S4 |
| 12 | Provenance assigned at write time must be immutable thereafter | `[A]` | | |
| 13 | Memory, persistent, verified and with provenance, is implemented and in validation | `[D]` | | `core.memory` S3 |
| 14 | The compounding loop is designed so that no weights change and training eligibility is a separate, consented category | `[D]` | | `compounding-loop` S4 |
| 15 | Context, memory, training eligibility and authority to act are four separate things | `[A]` | | |
| 16 | Erasure from model-derived artefacts is unsolved | `[O]` | | |
| 17 | Append-only integrity and erasure are in genuine tension | `[O]` | | |
| 18 | Origin resolution is hard and partially manual | `[O]` | | |
| 19 | Recheck conditions require domain knowledge not derivable from the claim | `[O]` | | |
| 20 | The write-path governance cost is unmeasured | `[O]` | | |

## References

Lewis, P. et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. Advances in Neural Information Processing Systems 33. Accessed 2026-08-12.

OWASP (2025). Top 10 for Large Language Model Applications. Accessed 2026-08-12.

Regulation (EU) 2016/679 of the European Parliament and of the Council on the protection of natural persons with regard to the processing of personal data. Accessed 2026-08-12.

Snodgrass, R. T. (1999). *Developing Time-Oriented Database Applications in SQL*. Morgan Kaufmann. Accessed 2026-08-12.

W3C (2013). PROV-DM: The PROV Data Model. W3C Recommendation. Accessed 2026-08-12.

**Verification note.** Every reference is verified against the published version and its accessed date corrected before this edition leaves DRAFT. The OWASP entry must resolve to the specific threat identifier covering injected content reaching persistent stores.

## Version History

| Version | Date | Status | Change |
|---|---|---|---|
| v1.1-public | 2026-10-18 | DRAFT | Aligned with the NEO x100 Intelligence Operating System architecture and capability register v2.0. Terminology migrated to the x100 vocabulary. Sections 3.2, 4.4 and 5 now connect the argument to Memory (persistent, verified, with provenance), to the compounding loop (no weights change, no automatic training on customer content, Help Improve NEO off by default) and to the separation of context, memory, training eligibility and authority. Published correction of the statement that nothing described was running: NEO Core is in operational deployment inside My NEO Group and in controlled pilots with external users (S2); Memory, Verification and policy enforcement are in validation (S3); the Knowledge Graph, Evidence Layer, Evidence Ledger and compounding loop remain designed and specified (S4); general public availability is targeted for early 2027. Thesis, withholdings, the section 4.5 removal and falsifier unchanged. |
| v1.0-public | 2026-08-12 | DRAFT | First public edition, on Founder determination of 2026-08-12. Reduces the store model, the promotion rule set and the claim record to their governing principles. Withholds the distinct-origin threshold. **Removes source section 4.5 in full**, without paraphrase, summary or reconstruction, on the ground that a self-authored analysis of a security surface assists an attacker; the removal is recorded rather than silent, and no derivative of that section exists or will be attempted. |
| v1.0 | 2026-08-09 | DRAFT | First full draft. |

## How to Cite

Mosse, M. (2026). *Evidence, Memory and Accountability in Agentic Systems*, public edition. NEO AI Research Program, `NEO-AI-R-005` v1.1-public. `https://neoai.myneogroup.com/id/NEO-AI-R-005`
