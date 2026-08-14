# NEO-AI-TN-003 - What Belongs in a Mission Event

**The event record: required fields, what is hashed, what is referenced, and what survives a replay**

| Field | Value |
|---|---|
| Identifier | NEO-AI-TN-003 |
| Title | What Belongs in a Mission Event |
| Family | NOTE |
| Type | Technical Note (`TN`) |
| Version | v1.0 |
| Status | DRAFT |
| Date | 2026-08-09 |
| Author | Mickael Mosse |
| Capability keys | `brain.event-bus` (S4), `mission-control` (S4), `brain.governance` (S4), `brain.memory` (S4), `brain.cost-engine` (S4), `brain.evidence-ledger` (S4), `brain.task-graph` (S4), `mission.envelope` (S4) |
| Claim-class counts | `[E]` 3 . `[A]` 23 . `[D]` 10 . `[O]` 4 |
| Figures | SYS-19 |
| Reading time | 10 minutes |
| Canonical URL | `https://neoai.myneogroup.com/technical-notes/neo-ai-tn-003` (placeholder, not yet resolvable) |


---

## 1. Problem statement

Mission State is derived by folding an append-only event log, so the log is the system of record and everything else is a projection. Two failure directions follow. An event that omits a field the fold needs makes the state underivable, and a state nobody can rebuild is a state nobody can audit. An event that copies content it should have referenced turns the log into an uncontrolled duplicate of every store it touched, defeating retention and deletion. This note fixes the record.

## 2. Context and constraints

Mission State is the current state of a mission, derived by folding its append-only event log; Mission is the objective and its governance context. `[A]` The distinction matters here because the log must be sufficient to derive the first and must not attempt to contain the second.

Three constraints are fixed. Events are immutable once written, so a correction is a compensating event and never an edit. `[A]` The log crosses a trust boundary into audit and supervision, which means an event must be legible to a reader who has no access to the stores it references. `[A]` And events outlive missions, so the retention rule for the log is independent of the retention rule for anything it points at, which forces the reference-rather-than-copy discipline of section 3.3.

ISO/IEC 42001 requires documented information sufficient to demonstrate that AI processes operate as intended, which is the obligation this record serves. `[E]` NIST AI 600-1 treats traceability of generative system operation as a risk-management concern. `[E]` Neither specifies an event schema, and the schema below is architectural interpretation.

## 3. The note

### 3.1 The record

```
MissionEvent {
  event_id            : ULID, monotonic within the mission stream
  mission_id          : stable, opaque
  sequence            : monotonic integer within mission_id, gapless
  event_type          : from a closed, versioned vocabulary
  schema_version      : the version of this record's shape
  occurred_at         : when the fact happened, from the emitting component
  recorded_at         : when the log accepted it
  actor               : { type, id, delegation_chain }
  authority_ref       : Decision Record identifier, where the event is an
                        action that required one
  envelope_ref        : Mission Envelope version in force at emission
  causation_id        : the event this one is a direct consequence of
  correlation_id      : the request or task node that groups related events
  task_node_ref       : Task Graph node, where applicable
  payload             : type-specific, small, no free text over a fixed limit
  refs                : [ { kind, address, content_hash } ]
  payload_hash        : hash over the canonical serialisation of payload
  prev_hash           : hash of the previous event in the mission stream
  event_hash          : hash over the whole record including prev_hash
}
```

Four fields carry more weight than their size suggests.

**`occurred_at` and `recorded_at` are both present** in the event record `[D]` (brain.event-bus, S4). They are both present because they diverge, and the divergence is the signal. `[A]` A connector that buffered for ninety seconds during an outage produces events whose ordering by `occurred_at` differs from their ordering by `recorded_at`, and a replay that uses the wrong one reconstructs a mission that never happened. The fold uses `sequence` for order and `occurred_at` for temporal reasoning.

**`actor.delegation_chain`** records the authority path when an agent was spawned by another agent `[D]` (brain.event-bus, S4). Without it the log answers who acted and not on whose authority, which fails the Authority Plane distinction: the record shows the action was permitted, and not who was entitled to permit it. `[A]` This field is where the open problem in `NEO-AI-R-005 s6` about delegated actor identity lands.

**`envelope_ref`** pins the Mission Envelope version in force at emission `[D]` (brain.event-bus, S4). Envelopes contract during a mission, so an event evaluated against the envelope as it stands at replay time will be judged against bounds that did not exist when it ran.

**`causation_id` distinct from `correlation_id`.** Correlation groups; causation orders. `[A]` A retry storm produces forty events with one correlation and forty distinct causations, and an operator asked why the budget was exhausted needs the causation chain, not the group.

### 3.2 What is hashed

Three hashes with three purposes. `[A]`

`payload_hash` covers the canonical serialisation of the payload alone, so a payload can be validated independently of the envelope fields around it.

`prev_hash` chains the event to its predecessor in the mission stream. Any deletion or reordering breaks the chain at the point of tampering and every event after it, which is the property that makes the log evidential rather than merely stored.

`event_hash` covers the whole record including `prev_hash`, and is the address by which the event is referenced from elsewhere.

Canonical serialisation is required before hashing, with a fixed field order, fixed number formatting and fixed unicode normalisation. `[A]` Two components that serialise the same event differently produce different hashes for identical facts, and the chain becomes unverifiable across a deployment boundary. This is dull and it is where the implementation will break.

### 3.3 What is referenced rather than copied

The rule: an event carries the identity of content and never the content, wherever the content lives in a store with its own retention and access policy. `[A]`


Three reasons, and the third is the one that decides it. `[A]` Copying inflates the log until replay becomes impractical. Copying duplicates access-controlled content into a store whose access model is audit-shaped rather than content-shaped, so a reader entitled to the log becomes entitled to everything the mission touched. And copying places content under the log's retention rule, which is the longest in the system, so a deletion request that succeeds against every content store still leaves the content in the log. `[A]` A log that cannot be pruned and cannot be redacted has converted an audit asset into a liability.

The content hash in the reference is what keeps the reference honest. `[A]` Without it the event points at an address whose content may have changed, and the replay reconstructs a mission using material the mission never saw.
### 3.4 What must survive a replay

Replay folds the log to reconstruct state. Three levels of reconstruction, with different guarantees.

**State replay** rebuilds Mission State. `[A]` It requires the envelope fields and the fold-relevant payloads, and nothing referenced. It is deterministic and must remain so across schema versions, which is why `schema_version` is on every record and why the fold retains handlers for retired versions.

**Decision replay** answers why an action was permitted. `[A]` It requires `authority_ref`, `envelope_ref`, `actor` and the runtime Decision Records those point at. It is deterministic where the policy version is pinned, and the Decision Record carries the policy version for that reason.

**Evidential replay** answers what the mission relied on. `[A]` It requires the referenced artefacts to still exist and to still hash correctly. It is not deterministic, because a referenced artefact may have been deleted under a legitimate request, and the correct outcome is a reconstruction with an explicit gap rather than a failure or a silent omission.

Model output is not reproducible and the note does not pretend otherwise. `[A]` A replay reconstructs what the system did, decided and relied on. It does not regenerate the model's output, and any claim that a mission is fully reproducible is false in the presence of a non-deterministic worker.

### 3.5 Reasoning tokens are excluded, deliberately

Intermediate model reasoning is not written to the event log. The exclusion is a design decision and its attractions are real, so they are stated first. `[A]`

Reasoning traces are the most useful debugging artefact available when an agent behaves strangely, and an incident review without them is slower and sometimes inconclusive. They also look like an explanation, which is precisely why a governance surface wants them.

Four reasons override that. `[A]`

A reasoning trace is not a record of a decision. It is a record of text a model produced on the way to an output, and the relationship between that text and the computation is not established. Storing it in an evidential log invites a reader to treat it as the reason an action was taken, when the reason an action was permitted is the Decision Record and nothing else. `[A]`

Reasoning traces carry content from every store the context touched, unstructured, which defeats the reference-not-copy rule of 3.3 entirely. A trace that quotes a document places that document's content in the log. `[A]`

Traces are provider-specific, unversioned in any way the platform controls, and change shape between model releases. `[A]` A log field whose semantics are set by a third party is not a stable schema.

And a trace is the ideal carrier for content injected by an adversarial document, since it is high-volume, unstructured and, unlike the payload, subject to no schema check. `[A]` OWASP's agentic security work treats injected content reaching persistent stores as a threat pattern. `[E]`

What is retained instead: the model and version identifier, the prompt template identifier with a parameter hash, a context manifest naming what was assembled without its content, token counts, latency, and the structured output. `[A]` That set supports the cost, routing and incident questions the trace was wanted for, without the four costs. Traces may be retained in a separate short-retention diagnostic store with its own access policy, and that store is not the mission log.

## 4. Design intent for NEO AI

The event record is specified as the single system of record for Mission State, with Mission Control views derived from it rather than maintained beside it. `[D] (mission-control, S4)` A supervision view that renders a state the log does not support is a defect. `[D] (mission-control, S4)` The hash chain is specified per mission stream, with `prev_hash` verified on read for audit queries. `[D] (brain.event-bus, S4)` Deletion and supersession are specified to be emitted as events that derived stores and caches subscribe to. `[D] (brain.event-bus, S4)` `[D] (brain.memory, S4)` Cost and token accounting are specified to derive from the retained counters rather than from reasoning traces. `[D] (brain.cost-engine, S4)` The event-type vocabulary and the payload limit are specified as governed configuration, versioned, with changes emitting a runtime Decision Record. `[D] (brain.governance, S4)` Figure `SYS-19` draws the lifecycle these events fold into, including the denial and containment paths.

## 5. Limits of this note

Retention is stated as a constraint and not as a schedule. `[O]` How long a mission log is held, and under what legal-hold mechanism, is jurisdiction-specific and deployment-specific, and the note asserts only that the log's retention is independent of the retention of what it references.

Cross-mission causation is unhandled. `[O]` Where a mission is triggered by an event in another mission, `causation_id` points outside the stream and the hash chain does not span the two. A cross-stream causation index is required and is not specified here.

Schema evolution has a known cost the note does not price. `[O]` Retaining fold handlers for every retired `schema_version` is what makes old missions replayable, and it accumulates indefinitely. No pruning strategy preserves replayability.

The diagnostic store for traces is named and not specified. `[O]` Its access policy, retention and relationship to the mission log need their own treatment, and an under-specified diagnostic store reintroduces every problem section 3.5 excluded.

Not covered: transport, ordering guarantees across partitions, exactly-once semantics, the projection layer, and any throughput or storage measurement. No such measurement exists.

## Scope and Limitations

This note specifies a record and the reasoning behind three of its rules. It establishes no property of an implementation, reports no operational data, and does not describe a deployed log. The schema is architectural interpretation; ISO/IEC 42001 and NIST AI 600-1 supply the documentation and traceability obligations, not the fields.

The note would be falsified by a demonstration that state, decision and evidential replay can all be satisfied from a log that copies content rather than referencing it, without breaching the retention independence in section 2, or by a demonstration that reasoning traces bear a stable and verifiable relationship to the computation that produced an output.

## Related Research

- `NEO-AI-R-005` Evidence, Memory and Accountability in Agentic Systems (DRAFT) - the episodic promotion rule this record implements, and the deletion-event requirement in its section 4.1.
- `NEO-AI-R-003` Mission Control: A Governance Architecture for Autonomous Work (DRAFT).

## Related Publications

- `NEO-AI-P-008` Research, Governance and the NEO AI Public Record (DRAFT).

## Related Technical Notes

- `NEO-AI-TN-001` Bounding the Autonomy Budget (DRAFT) - contraction events and `envelope_ref`.
- `NEO-AI-TN-002` Detecting Circular Corroboration in an Evidence Chain (DRAFT) - the convergence event.

## Related Architecture

- `NEO-AI-ARCH-014` Observability Architecture (RESERVED) - the diagnostic store named in section 3.5.
- `NEO-AI-ARCH-001` Mission Control (RESERVED).

Forward references only. Neither is cited in support of a claim.

## Related Engineering

- `NEO-AI-ENG-001` Mission Control Runtime (RESERVED).
- `NEO-AI-ENG-010` Incident Response for Agentic Systems (RESERVED) - the debugging use case section 3.5 declines to serve from the log.

Forward references only.

## Related Figures

- `SYS-19` Mission Lifecycle - the eight states these events fold into, with the denial, containment and bounded-replan paths drawn. Referenced in section 4.

## Related Terms

Mission . Mission State . Mission Envelope . Task Graph . Decision Record . Design Decision Record . Human Authority . Assurance Plane . Authority Plane . Containment.

## References

ISO/IEC (2023). ISO/IEC 42001:2023 Information technology - Artificial intelligence - Management system. International Organization for Standardization. ISO/IEC 42001:2023. Accessed 2026-08-09.

NIST (2024). Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile. National Institute of Standards and Technology. NIST AI 600-1. doi:10.6028/NIST.AI.600-1. Accessed 2026-08-09. VERIFICATION REQUIRED: publication year and exact title.

OWASP GenAI Security Project (2025). Securing Agentic Applications Guide 1.0. OWASP Foundation. Version 1.0. https://genai.owasp.org/resource/securing-agentic-applications-guide-1-0/. Accessed 2026-08-09. VERIFICATION REQUIRED: document version, publication date, and the threat identifier covering injected content reaching persistent stores.

Lebo, T., Sahoo, S. and McGuinness, D. (2013). PROV-O: The PROV Ontology. World Wide Web Consortium. W3C Recommendation, 2013-04-30. https://www.w3.org/TR/prov-o/. Accessed 2026-08-09.

All entries are UNVERIFIED under the Program publication standard until the verification ledger records otherwise.

## Version History

| Version | Date | Status | Change |
|---|---|---|---|
| v1.0 | 2026-08-09 | DRAFT | Initial public draft. |
