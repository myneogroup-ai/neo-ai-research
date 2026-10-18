# NEO-AI-TN-002 - Detecting Circular Corroboration in an Evidence Chain

**Distinguishing independent origin from reformulation, and what to do when the graph converges**

| Field | Value |
|---|---|
| Identifier | NEO-AI-TN-002 |
| Title | Detecting Circular Corroboration in an Evidence Chain |
| Family | NOTE |
| Type | Technical Note (`TN`) |
| Version | v1.1 |
| Status | DRAFT |
| Date | 2026-10-18 |
| Author | Mickael Mosse |
| Capability keys | `core.knowledge-graph` (S4), `core.verification` (S3), `mission-control` (S3), `neo-intelligence` (S4), `core.governance` (S3), `core.evidence-layer` (S4), `core.evidence-ledger` (S4) |
| Claim-class counts | `[E]` 1 . `[A]` 21 . `[D]` 8 . `[O]` 4 |
| Figures | SYS-08 |
| Reading time | 10 minutes |
| Canonical URL | `https://neoai.myneogroup.com/technical-notes/neo-ai-tn-002` (placeholder, not yet resolvable) |


---

## 1. Problem statement

A finding supported by five documents scores higher than a finding supported by one, and a corroboration count computed from document identity cannot tell whether the five documents are five observations or one observation restated four times. Restatement is the ordinary condition of published material, so the count is inflated by default rather than in adversarial cases only. This note gives the traversal that resolves a claim's supporting set to distinct origins, the fingerprinting that survives paraphrase, and the action taken when the graph converges.

## 2. Context and constraints

An Evidence Chain is the traversal path from one material claim back through its transformations to the originating sources, and the Evidence Layer is specified to compute it on demand over records in the Evidence Ledger `[D]` (core.evidence-layer, S4) `[D]` (core.evidence-ledger, S4). It is a query result. Nothing in this note is a stored corroboration score, and section 5 explains why storing one is unsafe.

The traversal depends on three things being present in the records, all of which the Evidence Layer is specified to guarantee at ingestion `[D]` (core.evidence-layer, S4). A content hash per artefact. A derivation edge per transformation, in PROV-O terms `wasDerivedFrom` between entities and `wasGeneratedBy` against the activity that produced them. `[E]` And a citation edge where an artefact references another artefact, which is distinct from a derivation edge because the platform did not perform the transformation and can only observe the reference.

Two limits are fixed. The graph contains only what the platform ingested, so an origin the platform never saw is invisible to the traversal and appears as a root. `[A]` And the platform cannot observe unattributed borrowing except through text similarity, which is a heuristic. `[A]`

## 3. The note

### 3.1 Origin fingerprinting

An origin is the earliest node in a derivation-and-citation path that the platform can identify, together with the party that produced it. `[A]` Two supporting artefacts share an origin when their paths reach the same origin node, and the detection problem is that the same origin often appears under different identities.

Three fingerprints are computed per artefact and compared pairwise.

**Exact.** The content hash. Catches redistribution of the identical file through different channels, which is common with wire copy and with regulatory filings mirrored by aggregators. `[A]`

**Structural.** A shingle set over normalised text, compared by Jaccard similarity. Normalisation lowercases, collapses whitespace, strips boilerplate and removes the citation apparatus. This catches near-verbatim reuse with light editing, which is what most syndication is. `[A]`

**Assertional.** The set of `(subject, predicate, object, temporal_scope)` tuples extracted from the artefact, compared for overlap after entity resolution. Two texts sharing no wording can assert an identical claim set with identical unusual specifics, and a shared error is the strongest signal available. `[A]` If both artefacts state a date that turns out to be wrong in the same way, they are one origin, and no amount of paraphrase hides it.

Fingerprints are compared in that order and the first match settles the pair. `[A]` The assertional comparison is the expensive one and is run only on pairs the first two did not resolve.

### 3.2 Independent corroboration and reformulation

The distinction the procedure has to draw:

- **Reformulation.** Artefact B's claim set derives from artefact A, by citation, by paraphrase or by shared unusual content. B adds no evidential weight. `[A]`
- **Independent corroboration.** Artefacts A and B reach the claim from observations neither took from the other. Weight is additive, subject to source class. `[A]`
- **Overlapping observation.** A and B are independent as documents and rest on a shared underlying observation, such as two reporters interviewing the same source. `[A]` Neither additive nor reducible to one.

The third case has no numerical answer, and the procedure does not invent one. `[A]` It reports the document count and the observed overlap separately and refuses to combine them. A single independence score here would be a fabricated quantity presented with the same typography as a measured one.

### 3.3 The detection procedure

1. Collect the direct supporting set `S(c)`: every evidence record referenced by `c` through its `source_ref` field or through a derivation rule named on the claim.

2. Partition `O(c)` by exact fingerprint. Merge identical hashes.

3. Partition the remaining classes by structural fingerprint at threshold `theta`. Merge classes above it.

4. Emit the result: distinct origin count, party count, unresolved external references, cycle alerts, and the merge reason for every merged pair.

Step 10 is not optional output formatting. `[A]` A detection result a reviewer cannot audit is a second opaque score replacing the first one, and the merge reasons are what let a reviewer overturn a merge the fingerprints got wrong.

The convergence threshold is governed configuration and is not published in this public edition.

### 3.4 Complexity

Let `n` be the number of nodes reachable from `S(c)` and `e` the number of edges among them. The traversal in steps 2 to 4 is `O(n + e)` with the visited set. `[A]`

The partitioning dominates. Step 6 is `O(m)` for `m` candidate origins, by hash bucket. Step 7 is `O(m^2)` pairwise in the naive form. The reduction available from MinHash with locality-sensitive hashing over the shingle sets is an established result in the published literature, and this note cites no primary source for it because the Program's bibliography has not been extended to cover it. `[A]` No complexity claim in this note depends on the reduction; `O(m^2)` is the bound the design is sized against. Step 8 is `O(p * t)` for `p` surviving pairs and `t` the mean claim-tuple count, and `p` is small because the earlier steps merged the easy cases.

The practical cost is dominated by the fan-out of step 2, which is unbounded in a graph where a widely cited source appears in many derivation paths. `[A]` A depth limit is required, and a limit that truncates a path yields a truncated-path flag rather than an origin, since a truncated path is a fact about the traversal and not about the evidence.

## 4. Worked example

The five-item case from `NEO-AI-R-005 s4.3`, run through the procedure.

Supporting set: a trade-press article (March 2024), a market research note (May 2024), an encyclopaedia paragraph (June 2024), a competitor investor presentation (September 2024), and a news wire story (January 2025).

Step 2 walks derivations and produces five branch terminals, because each artefact was ingested independently and no transformation links them. A count taken here reports five, and is wrong.

Step 3 follows citation edges. The market research note cites the trade press article; merged. The encyclopaedia paragraph cites the market research note; merged. The competitor presentation cites "public sources" with no resolvable target, so its branch terminates as an external unresolved reference rather than as a corroborating origin. The trade press article cites a company statement of February 2024, which was ingested, and the branch continues to it.

The wire story carries no citation edge. Step 7 catches it: its background paragraph and the trade press article share a shingle set above `theta`. Merged, reason recorded as structural.

Result: one distinct origin, being the February company statement. One party, being the subject of the question. One external unresolved reference. Four merges, each with a reason. `[A]`

The output presented to a reviewer is that the finding rests on a single self-reported origin with four derivative restatements, and not that five sources agree.

## 5. What to do on convergence

Convergence below `k` distinct origins produces four actions, and displaying a warning is not among them. `[A]`

The claim's verification status is set to unverified regardless of the document count, and stays there until an independent origin is found. `[A]` Promotion to semantic memory is refused, since the promotion rule requires an evidence reference that is not a restatement of the claim's own origin. `[A]` The autonomy level of every remaining task node contracts by one, per `NEO-AI-TN-001 s3.3`. And where the single origin is the subject of the question, the finding is labelled self-reported, which says more than uncorroborated does. `[A]`

A stored corroboration count cannot support any of this. `[A]` It is computed against the Ledger as it stood at write time, and a sixth artefact arriving next week may merge with an existing origin and reduce the true count while leaving the stored one unchanged. Caching the traversal result is permitted with an invalidation subscription to the Ledger; treating the cache as the answer is not.

Design intent. Convergence detection is specified as a required check before a relationship or ownership finding is presented, rather than as an analytical view a user may enable. `[D] (neo-intelligence, S4)` `[D] (core.knowledge-graph, S4)` Retaining the merge reasons with the result and showing them on inspection in Mission Control is implemented and in validation. `[D] (mission-control, S3)` Writing verification status changes arising from convergence to the claim record, and not only to the mission output, is implemented in the Verification Layer and is in validation. `[D] (core.verification, S3)` Holding the threshold `theta` and the requirement `k` as governed configuration, versioned, with changes emitting a runtime Decision Record, is implemented in policy enforcement and is in validation. `[D] (core.governance, S3)` Figure `SYS-08` draws the traversal with the convergence path marked.

## 6. Limits of this note

The procedure detects shared origin among ingested artefacts. It says nothing about whether the origin is reliable, and one strong independent origin can be worth more than four weak ones. `[O]` Origin counting is a check against inflation, not a measure of quality.

Threshold selection is unaddressed. `[O]` A `theta` that is too low merges genuinely independent reporting on the same event; too high and syndication survives as corroboration. The Program has not measured the error rates at any threshold and has no reference set on which to measure them.

Assertional overlap depends on entity resolution, which is itself uncertain, so a resolution error can cause a false merge or a false split. `[O]` The dependency is circular in a mild way and is not resolved here.

Adversarial evasion is out of scope. `[O]` A party seeding several genuinely distinct-looking origins with no shared wording and no shared error defeats all three fingerprints, and the defence is source-class analysis rather than lineage.

Not covered: source reliability grading, entity resolution itself, the storage layout of the Ledger, and any measurement of the procedure's precision or recall. No such measurement exists.

## Scope and Limitations

This note specifies a procedure and its complexity. It establishes no property of an implementation and reports no accuracy data. The components that would run the procedure are at different statuses, stated in section 5: the Evidence Layer, the Evidence Ledger and the Knowledge Graph are designed and specified, while Mission Control, Verification and policy enforcement are implemented and in validation; no status has been verified by an independent third party. The fingerprinting scheme is architectural interpretation. PROV-O supplies the derivation vocabulary and does not supply this procedure.

The note would be falsified by a demonstration that document-level corroboration counts and origin-resolved counts agree closely on a realistic corpus of published material, which would make the traversal unnecessary work.

## Related Research

- `NEO-AI-R-005` Evidence, Memory and Accountability in Agentic Systems (DRAFT) - defines the Evidence Chain and states the five-article case this note formalises.
- `NEO-AI-R-006` The Intelligence Layer: From Fragmented Data to Defensible Decisions (DRAFT) - entity resolution, on which step 8 depends.

## Related Publications

- `NEO-AI-P-006` NEO Intelligence: A Governed Reasoning Layer for Evidence-Intensive Investigation (DRAFT).

## Related Technical Notes

- `NEO-AI-TN-001` Bounding the Autonomy Budget (DRAFT) - consumes the convergence signal as a contraction trigger.
- `NEO-AI-TN-003` What Belongs in a Mission Event (DRAFT) - the event emitted on convergence.

## Related Architecture

- `NEO-AI-ARCH-006` Evidence (RESERVED) - will specify the Ledger record and its edges.
- `NEO-AI-ARCH-007` Knowledge Graph (RESERVED).

Forward references only. Neither is cited in support of a claim.

## Related Engineering

- `NEO-AI-ENG-003` Knowledge Graph (RESERVED).

Forward reference only.

## Related Figures

- `SYS-08` Evidence Layer - traversal from artefact to source with a circular corroboration path detected and marked. Referenced in section 5.

## Related Terms

Evidence Layer . Evidence Chain . Evidence Ledger . Circular Corroboration . Claim Class . Verification Layer . Knowledge Plane . Decision Record . Bounded Autonomy.

## References

Lebo, T., Sahoo, S. and McGuinness, D. (2013). PROV-O: The PROV Ontology. World Wide Web Consortium. W3C Recommendation, 2013-04-30. https://www.w3.org/TR/prov-o/. Accessed 2026-08-09.

W3C (2014). RDF 1.1 Primer. World Wide Web Consortium. W3C Working Group Note, 2014-06-24. https://www.w3.org/TR/rdf11-primer/. Accessed 2026-08-09. VERIFICATION REQUIRED: document maturity level and dated version.

NIST (2024). Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile. National Institute of Standards and Technology. NIST AI 600-1. doi:10.6028/NIST.AI.600-1. Accessed 2026-08-09. VERIFICATION REQUIRED: publication year and exact title.

Pushkarna, M., Zaldivar, A. and Kjartansson, O. (2022). Data Cards: Purposeful and Transparent Dataset Documentation for Responsible AI. ACM Conference on Fairness, Accountability, and Transparency. arXiv:2204.01075. Accessed 2026-08-09.

All entries are UNVERIFIED under the Program publication standard until the verification ledger records otherwise.

## Version History

| Version | Date | Status | Change |
|---|---|---|---|
| v1.0 | 2026-08-09 | DRAFT | Initial public draft. |
| v1.1 | 2026-10-18 | DRAFT | Aligned with the NEO x100 Intelligence Operating System architecture and capability register v2.0: capability keys migrated to v2.0 and statuses and verbs corrected (Mission Control, Verification and policy enforcement implemented and in validation at S3; Evidence Layer, Evidence Ledger, Knowledge Graph and NEO Intelligence remain specified at S4). Terminology migrated to the x100 vocabulary (Verification, Verification Layer). The procedure, fingerprints, `theta`, `k` and complexity bounds are unchanged. |
