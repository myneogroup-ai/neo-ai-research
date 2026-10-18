# Mission Control: A Governance Architecture for Autonomous Work

**Turning oversight from a document into a state transition**

| Field | Value |
|---|---|
| Identifier | `NEO-AI-R-003` |
| Edition | **Public edition** of `NEO-AI-R-003 v1.0`. Reduced, not paraphrased |
| Version | v1.1-public |
| Status | DRAFT |
| Date | 2026-10-18 |
| Author | Mickael Mosse, NEO AI Research Program |
| Capability keys | `mission-control` S3 . `mission.state` S2 . `mission.envelope` S3 . `human-gates` S3 . `core` S2 . `core.governance` S3 . `core.event-bus` S3 . `core.verification` S3 . `lili` S2 |
| Claim-class counts | `[E]` 8 . `[A]` 26 . `[D]` 20 . `[O]` 9 . Counted by script over the body and back matter, excluding this row |
| Reading time | 21 min |
| Canonical URL | `https://neoai.myneogroup.com/research/papers/mission-control-governance-architecture/` |
| Relations | `applies` NEO-AI-R-009 . `refines` NEO-AI-TN-001 . `refines` NEO-AI-TN-003 . `evidences` NEO-AI-P-001 |
| Withheld | One section as TRADE SECRET in part, three as CONFIDENTIAL TECHNICAL ARCHITECTURE. Section 7 states what and why |

---

## Abstract

AI governance is mostly written as policy. A policy document does not stop anything at runtime.

This paper argues that governance of autonomous work has to be expressed as a **state transition** rather than as a statement of intent, and that the governable unit is the mission: an objective, a permitted action set, an authority context and a required record.

Two claims do the work. The first is that **Policy and Authority are different planes**, answering *may this happen* and *who was entitled to decide it happens*, and that collapsing them produces an audit trail recording permission without entitlement. The second is that **reasoning tokens are deliberately excluded from the governance record**, on three independent grounds, the first of which would be sufficient alone.

This public edition withholds the event schema, the event-type vocabulary, the approval object structure, the integrity chain construction and the containment trigger list. The principles are published; the implementation is not.

---

## 1. The execution gap

An organisation adopting autonomous AI writes a policy. The policy says which actions require approval, what may be spent, what data may leave, and who is accountable. It is reviewed, signed and filed.

Then the system runs, and the policy is not in the execution path.

This is the execution gap and it is not a failure of will. It is structural: a policy is prose about intent, and a running system consumes attributes and emits actions. Nothing converts one into the other unless something is built to convert it `[A]`.

The gap has a characteristic signature. Everybody can say what the policy is. Nobody can say, for a specific action taken eight months ago, which rule applied, what it consumed, who had authorised the exception, and whether that authorisation was still valid at the moment the action executed. The policy exists. The answer does not.

Closing it requires three things that are easy to state and expensive to build. Governance must be **evaluated at runtime**, not asserted at design time. Its decisions must be **recorded as facts** rather than reconstructed from logs. And the record must support **a later question**, which is a harder requirement than it sounds: a log is written for the person watching now, and a record is written for the person asking in eighteen months who was not there.

---

## 2. What the established work supports

**Event sourcing is an established pattern for reconstructible state.** Deriving current state by folding an append-only log of events, rather than mutating a state record in place, is a standard architecture with known trade-offs `[E]` (Fowler, 2005; Vernon, 2013). Cited for the pattern and for the reconstruction property, which is the property this paper needs.

**Append-only integrity structures are well understood.** Hash-linked logs, and the verification properties they provide and do not provide, are established `[E]` (Haber and Stornetta, 1991; Crosby and Wallach, 2009). What they establish is tamper-evidence, not tamper-resistance, and the distinction matters to what a record can honestly claim.

**Attribute-based access control separates policy from code.** Evaluating an access decision against attributes at a policy decision point, rather than embedding rules in application logic, is established practice with published reference architectures `[E]` (NIST SP 800-162).

**Human oversight is a regulatory requirement, not only a design preference.** Published regulatory frameworks for high-risk AI require effective human oversight and record-keeping sufficient to trace a decision `[E]`.

**What none of this establishes.** No published work known to the Program establishes that a particular supervisory architecture produces measurably better oversight outcomes on real autonomous work, because the outcome measure is unsettled `[O]`.

---

## 3. Mission state and the record

### 3.1 Why the mission is the governable unit

A prompt is too small to govern: it has no objective, no boundary and no authority context, and a governance regime attached to it degenerates into per-request permission checking that nobody can reason about.

A project is too large: it spans months, its boundaries move, and its authority context changes underneath it.

A **mission** is the unit that has all four properties governance needs at once. It has an objective somebody asked for. It has a permitted action set fixed when it starts. It is performed under a named authority. And it produces a record whose completeness can be tested `[A]`.

Mission state is **derived by folding an append-only event log** rather than stored and mutated. That choice is what makes reconstruction possible: the question *what was true at the moment that decision was taken* is answered by folding the log to that point, which is a computation, rather than by consulting a state record that has since changed, which is impossible.

### 3.2 What the record must answer

The source paper specifies the event record field by field, and that specification is withheld. What is publishable is the requirement it satisfies.

**Every event in a mission record answers six questions**: what happened, when, to what subject, under whose authority, on what basis, and with what result. An event that cannot answer all six is not a governance event, whatever else it may be useful for `[A]`.

Events of one kind are named publicly and are worth distinguishing from a term they are often confused with. An **Operational Decision Event** announces that a meaningful system-level execution decision was taken: verification activated, contradiction detected, specialist deployed, source rejected, model replaced, tool failed, human approval requested, risk threshold exceeded. It is **not a `Decision Record`**, which is the machine-readable record a policy decision point emits, and it is not a `Design Decision Record`, which is an ADR. Where a policy decision point was involved, the event references the Decision Record rather than containing it, and it never carries a threshold value.

Two properties follow and both are load-bearing. The record is **append-only**, so a correction is a new event referencing the old one rather than an edit. And the record is **about the system rather than by it**: it captures observations of what occurred, not statements the system makes about itself. The next section is why that distinction is the most important one in the paper.

### 3.3 What must be stable across a reconstruction

Reconstruction is frequently confused with replay, and the two are different operations with different guarantees.

**Reconstruction** answers what was true at a point in time. It folds the recorded events to that point and yields the state as it stood. It is deterministic, because it is arithmetic over a fixed log.

**Replay** re-executes the work. It is not deterministic, because the executors are not deterministic, because external sources have changed, and because the same inputs need not produce the same outputs. A system that offers replay and calls it reconstruction has promised something it cannot deliver `[A]`.

What must be stable across a reconstruction is therefore the **recorded facts**, not the outputs: which decisions were taken, on what attributes, under which authority, with which approvals valid at the time, and which artefacts were produced. A supervisory interface that shows a reconstructed state must be explicit about which of the two it is doing.

### 3.4 Why reasoning tokens are not part of the record

Systems that expose a model's intermediate reasoning offer an obvious temptation: put it in the log and the audit trail will explain itself. The Program's position is that **reasoning tokens are deliberately excluded from the mission record**, for three independent reasons `[A]`.

**The first is reliability.** An emitted chain of thought is a generated artefact, produced by the same process that produced the answer and not an observation of the computation behind it. Treating it as the system's reason is a category error with a specific governance consequence: if the audit trail's explanatory content is generated text, the audit trail can be confabulated. **A record that can be confabulated by the component it records is not a control.** This reason would be sufficient on its own.

**The second is exposure.** Reasoning traces restate the input at length, including whatever privileged, personal or commercially sensitive material it held, multiplying the surface subject to retention and erasure obligations for the content of least evidential value in the record.

**The third is uniformity.** Availability of reasoning tokens is a provider decision varying by candidate and version. A trail rich for one candidate and empty for another is a bias in the record correlated with the routing decision, and routing must stay free to move between candidates.

What the record captures instead are operationally relevant events: the inputs, the retrieved artefacts and their provenance, the tool calls proposed and their arguments, the policy decisions and the attributes they consumed, the verification results, the approvals, and the actions executed. **These are observations of the system rather than statements by it.**

This loses something real, and the paper does not pretend otherwise. When an output is wrong, the first thing an engineer wants is the model's reasoning, and this record will not have it. The compensating controls are heavier: verification that tests the output rather than the explanation, evidence linkage making each material claim traversable to its source, and enough structure in the tool-call record to see what the system was attempting even where it cannot see why. Those cost more than logging a trace and satisfy less in an incident review. It is a genuine cost of the design rather than a costless choice.

An organisation that wants reasoning traces for debugging should keep them in a **short-retention diagnostic channel that is explicitly not part of the governance record and is never cited in one.**

---

## 4. Architectural interpretation

### 4.1 Policy and Authority are different planes

The **Policy Plane** owns what is permitted and answers *may this happen*. The **Authority Plane** owns who may permit it and answers *who decided, and were they entitled to* `[A]`. They differ in almost every property that matters to an implementation.

| | Policy Plane | Authority Plane |
|---|---|---|
| Question | May this happen | Who may decide that it happens |
| Evaluated | Per request, many times per mission | Per grant, few times per mission |
| Lifetime of the answer | Instantaneous | Durable; changes on organisational timescales |
| Input | Attributes of the request and the context | Entitlements, roles, delegations, separation-of-duties constraints |
| Output | A runtime Decision Record | An approval object, a delegation, an envelope change |
| Failure mode | An action is wrongly permitted or denied | An action is correctly permitted by someone who had no standing to permit it |
| Changes when | A rule is edited | An organisation restructures |

**Collapsing them is easy to do and hard to notice, because a collapsed system passes every test anyone writes for it.** The action was checked. A rule fired. A record exists. The record even names an approver.

Then a question arrives eighteen months later. Was that person entitled to approve that amount, for that entity, on that date, under what delegation, and did the delegation carry a scope limit the action exceeded. **The Policy Plane's record cannot answer it, because the rule consumed the approval as an attribute.** A boolean. It was satisfied by the *existence* of an approval, not by its validity `[A]`.

So a stale approval satisfies it. So does one granted for a different artefact version, one from a since-revoked entitlement, one outside its scope, and one obtained through a delegation chain nobody would have authorised had they seen it written out. Each produces a permitted action with a clean policy record. **The trail records permission and not entitlement, and the gap between those two words is where the loss happens.**

The fix is to make an approval an **object** with identity, provenance, scope and validity conditions, held in the Authority Plane, which the Policy Plane references rather than consuming as a derived boolean. Reconstruction then traverses action to approval to delegation to entitlement. Three hops, each a recorded fact.

Two derived failures follow from the collapse and both are worth naming.

**Overrides become policy rules.** Every real system has a way to do the thing the rules forbid, because operations require it. Collapsed, that way becomes a rule saying a particular role bypasses the check, and the record then shows nothing about entitlement, reason, scope or expiry. An override belongs in the Authority Plane as a time-boxed, scoped, separately approved entitlement with its own event, visible where a supervisor looks rather than buried in the same stream as every routine permit `[A]`.

**Authority amplifies through delegation.** An agent acts for a user, through a delegated role, creating a sub-agent, inheriting a credential. At each hop *is authorised* is preserved and *within what scope* is quietly widened, because scope is expensive to propagate and its absence is invisible until an incident. The result is an agent with more effective authority than the human who launched it. Three controls: a maximum delegation depth held at the Authority Plane, **scope intersection rather than scope inheritance** at every hop, and a sub-agent envelope that is a strict subset of its parent's with no exceptions `[A]`. In NEO AI the corresponding rule, that agents receive capability tools and never credentials and that more intelligence, more agents or more compute never create more authority, is implemented in policy enforcement and is being validated `[D] (core.governance, S3)`.

The cost is admitted. Two planes are two systems, two latency sources on a consequential action, and a bug class in which the planes disagree about an approval's state. A collapsed component is genuinely simpler and, where every action is reversible and low-value, may be the right choice. **The split earns its complexity where actions are irreversible, where the organisation is regulated, or where an investigation eighteen months later is a realistic prospect** `[A]`.

### 4.2 Approval is an object, not a click

Reduced in this edition; the source specifies the object and its invalidation conditions and both are withheld.

Four properties are publishable and they are the ones a buyer should ask about. An approval has an **identity**, so it can be referenced. It has a **scope**, so it authorises something specific rather than everything. It has a **validity period**, so it expires rather than persisting. And it can be **invalidated by a change in what it was granted against**, so that approving version 3 of an artefact does not silently authorise version 4 `[A]`.

An approval mechanism missing any of the four produces a record that names an approver and cannot establish entitlement.

### 4.3 Four views over one state

One event-sourced mission state resolves into four supervisory views, and organisations reliably build three of them.

**Operational state**: what is running now, which nodes are active, what is blocked. Everyone builds this.

**Decision history**: what was decided, when, on what basis, under whose authority. Most organisations build a partial version.

**Evidence and provenance**: which claims rest on what, and whether the support resolves to distinct origins. Some build this.

**The one everyone omits is the counterfactual view**: what the system considered and did not do. Which candidate executors were admissible and which were excluded, which sources were retrieved and rejected, which strategies were available and not taken `[A]`.

It is omitted because it is the only view with no operational use: nothing depends on it while the mission runs. It is the view an investigation needs, because the question after an incident is rarely *why did it do that* and is usually *why did it not do the other thing*. A system that records only what happened cannot answer the question it will actually be asked.

These four are views of the record, and they are not to be confused with the projections of the interface. In NEO AI, Mission Control is the operating-system view, and FOCUS, NORMAL and JARVIS are three projections of one Mission state, sharing one composer and one right inspector with Progress, Output and Context; it is implemented and in validation `[D] (mission-control, S3)`. Each Mission has one Mission state `[D] (mission.state, S2)`. The rule that switching projection changes only how much of that state is visible, never which state is shown, and never restarts execution, is implemented with Mission Control and is being validated `[D] (mission-control, S3)`. The argument of this section applies to that design directly: a projection may show less of the record, and it must never show a different one `[A]`.

### 4.4 Governance usability is a safety property

An approval queue that presents a supervisor with fifty items an hour, each requiring context the interface does not supply, will be cleared rather than reviewed. The approvals will be recorded. The oversight will not have happened.

This is not a user-experience concern that can be deferred. **If the governance interface is unusable, the governance is fictional, and the record will show it was performed** `[A]`. The failure is worse than having no approval step, because the record now carries evidence of an oversight that did not occur.

Three consequences for design. The number of approvals a mission generates is a governed quantity and belongs in the mission's own budget. An approval request must carry the context required to decide it, or it is a request to guess. And the rate at which approvals are granted without the supporting context being opened is a measurable signal that the regime has degenerated.

NEO AI addresses the governed quantity with an approval policy, ASK ME, AUTO or AUTONOMOUS, built so that a policy can only narrow what is auto-approved and never widen it, and with mandatory Human Gates placed outside every policy, so that production DNS changes, publishing to a public domain, act-class connector actions and the release of a deployment require a human decision whatever the policy says; both are implemented and in validation `[D] (human-gates, S3)`. The policy reduces the volume of approvals; it does not by itself solve the fatigue problem of section 6, and the paper does not claim that it does `[A]`.

### 4.5 What Mission Control must not be

Three things, each of which it would drift into without a rule against it.

**It must not be a chat interface with a progress bar.** The value is in the task graph, the decision history, the evidence and the counterfactual, none of which is a conversation. In NEO AI the conversation with LILI, the conversational face of NEO AI, is the surface the user works through `[D] (lili, S2)`. The FOCUS projection, conversation and decision, is a projection of the Mission state and not a substitute for it `[A]`. NORMAL and JARVIS, which add the execution plan, agents, artefacts, evidence and task graph beneath the same conversation, are implemented and in validation `[D] (mission-control, S3)`.

**It must not display anything that does not correspond to a real event.** Simulated activity, decorative progress and anticipatory rendering are prohibited. A supervisory surface whose contents are partly fabricated cannot be used for supervision, and the user cannot tell which parts `[A]`. The NEO AI product rule, implemented in Mission Control and being validated with it, is stated in the same terms: nothing is simulated, and there are no fake agents, progress, tests, evidence, cost or verified state `[D] (mission-control, S3)`.

**It must not expose private reasoning traces**, for the three reasons in section 3.4. What Mission Control shows in their place, as implemented and in validation, is visible progressive work: the events, artefacts, verification results and approvals as they occur, never a private chain of thought `[D] (mission-control, S3)`.

---

## 5. Application to the NEO AI target architecture

Reduced in this edition.

Publishable, with the status of each part stated separately, because the parts are not at the same status.

NEO Core, the orchestration layer of the Intelligence Operating System, and LILI are in operational deployment inside My NEO Group and in controlled pilot programmes with external users `[D] (core, S2)`. Each Mission has one Mission state, from which every surface reads `[D] (mission.state, S2)`.

Derivation of that state by folding an append-only event log, the Event log (Event Bus), is implemented and in validation `[D] (core.event-bus, S3)`. Policy enforcement at a single declared point rather than in application code is implemented and in validation `[D] (core.governance, S3)`. Authority held separately from policy, with approvals as objects, Human Gates and the approval policy, is implemented and in validation `[D] (human-gates, S3)`. The Mission Envelope is implemented and in validation `[D] (mission.envelope, S3)`. Verification, which tests the output rather than the explanation, is implemented and in validation `[D] (core.verification, S3)`. Mission Control, including the rule that every element presented to a user resolves to a real event about its own subject, is implemented and in validation `[D] (mission-control, S3)`.

No independent party has verified any of these statuses, and this edition reports no measurement of them.

---

## 6. Failure modes and open problems

**Governance overhead is real and unmeasured** `[O]`. Two planes, an approval object model and an append-only record cost latency, storage and engineering time. The Program holds no measurement of that cost.

**Approval fatigue is a design problem without a settled answer** `[O]`. Section 4.4 states the requirement and does not solve it.

**Tamper-evidence is not tamper-resistance** `[A]`. A hash-linked record proves that a change occurred, to a party who checks. It does not prevent one, and it does not help if nobody checks.

**Erasure against an append-only record is unresolved in the general case** `[O]`. A record designed never to change and a legal obligation to delete are in genuine tension. The Program has an approach and it is not published here.

**The counterfactual view has an unbounded cost** `[O]`. Recording everything considered and rejected is more expensive than recording what happened, and where the boundary sits is not settled.

---

## 7. What this edition withholds, and why

| Withheld | Class | Reason |
|---|---|---|
| The event record, field by field, and the closed event-type vocabulary | CONFIDENTIAL TECHNICAL ARCHITECTURE | The exact telemetry schema and the detailed event protocol. Section 3.2 publishes what the record must answer, which is the principle |
| The integrity chain construction and the expungement design | CONFIDENTIAL TECHNICAL ARCHITECTURE | Publishing the construction assists an attacker and is not required by the argument |
| The approval object schema and its invalidation conditions | CONFIDENTIAL TECHNICAL ARCHITECTURE | Section 4.2 publishes the four properties, which is the principle |
| The containment trigger list | **TRADE SECRET** | A policy combination. Naming the conditions is publishable; naming the values is not |
| The containment response ladder | CONFIDENTIAL TECHNICAL ARCHITECTURE | |

**Containment, stated at the level this edition permits.** A mission can be suspended, contracted, quarantined and terminated. The envelope may contract automatically and expands only by explicit authority. Recovery from a fault never expands it. The conditions that trigger each response are configured per mission class by policy and **are not published**, because a published trigger list is a published evasion list.

---

## Scope and Limitations

This is a **public edition** of `NEO-AI-R-003 v1.0`: a reduction, not a rewriting. Four bodies of material are withheld and are listed in section 7. No withheld material is paraphrased, summarised or reconstructed, and no threshold value appears anywhere in this edition.

The paper reports **no measurement and no evaluation**. It makes no comparative claim against any named system.

**Correction (v1.1-public).** The first public edition stated that every capability named was at S4 in a provisional register and that nothing described was running. That is no longer true. On Founder determination of 2026-10-18, NEO Core, LILI and the single Mission state are in operational deployment inside My NEO Group and in controlled pilot programmes with external users (S2). Mission Control, the Mission Envelope, Human Gates, policy enforcement, the Event log and Verification are implemented and in validation (S3). General public availability, global, is targeted for early 2027, a target and not a commitment. Register v1.3 was Founder-ratified on 2026-08-13; register v2.0 (2026-10-18) restructures it to the x100 architecture and is pending Founder ratification; no status has been verified by an independent third party.

It would be falsified by a demonstration that a collapsed policy-and-authority component supports post-hoc investigation as well as a split one, on real regulated work.

## Related Research

- `NEO-AI-R-009` From Model Intelligence to System Intelligence. Supplies the argument for why the record is a durable asset.
- `NEO-AI-R-001` The End of the Single-Model Enterprise. Public edition. Supplies the selection half.
- `NEO-AI-R-005` Evidence, Memory and Accountability in Agentic Systems. Public edition.

## Related Publications

- `NEO-AI-P-001` Introducing NEO AI: Intelligence Orchestrated.
- `NEO-AI-P-007` A Note on Responsible AI Capability Claims.

## Related Technical Notes

- `NEO-AI-TN-001` Bounding the Autonomy Budget. Derives the autonomy level section 4 assumes.
- `NEO-AI-TN-003` What Belongs in a Mission Event. The publishable companion to the withheld section 3.2.

## Related Architecture

None in this wave. CONFIDENTIAL TECHNICAL ARCHITECTURE.

## Related Engineering

None in this wave.

## Related Figures

None in Wave 1.

## Related Terms

`Mission` . `Mission State` . `Mission Envelope` . `Policy Plane` . `Authority Plane` . `Assurance Plane` . `Human Authority` . `Decision Record` . `Design Decision Record` . `Containment` . `Bounded Autonomy` . `Observable Intelligence` . `Operational Decision Event`

## Evidence Table

| # | Claim | Class | Source | Capability |
|---|---|---|---|---|
| 1 | Event sourcing derives reconstructible state from an append-only log | `[E]` | Fowler, 2005; Vernon, 2013 | |
| 2 | Hash-linked logs provide tamper-evidence, not tamper-resistance | `[E]` | Haber and Stornetta, 1991; Crosby and Wallach, 2009 | |
| 3 | Attribute-based access control separates policy from application code | `[E]` | NIST SP 800-162 | |
| 4 | Published regulatory frameworks require effective human oversight and traceability for high-risk AI | `[E]` | Regulation (EU) 2024/1689 | |
| 5 | A policy document is not in the execution path | `[A]` | | |
| 6 | The mission is the smallest unit carrying objective, boundary, authority and record | `[A]` | | `mission.envelope` S3 |
| 7 | Reconstruction and replay are different operations with different guarantees | `[A]` | | |
| 8 | A record confabulable by the component it records is not a control | `[A]` | | |
| 9 | A collapsed policy and authority component records permission without entitlement | `[A]` | | `core.governance` S3 |
| 10 | Scope intersection rather than inheritance is required at every delegation hop | `[A]` | | |
| 11 | The counterfactual view is the one omitted and the one an investigation needs | `[A]` | | |
| 12 | An unusable governance interface produces recorded oversight that did not occur | `[A]` | | |
| 13 | Mission state is derived by folding an append-only event log; implemented and in validation | `[D]` | | `core.event-bus` S3 |
| 14 | FOCUS, NORMAL and JARVIS are three projections of one Mission state | `[D]` | | `mission-control` S3 |
| 15 | Approval policy can only narrow what is auto-approved; mandatory Human Gates sit outside every policy | `[D]` | | `human-gates` S3 |
| 16 | Governance overhead is unmeasured | `[O]` | | |
| 17 | Approval fatigue has no settled answer | `[O]` | | |
| 18 | Erasure against an append-only record is unresolved in the general case | `[O]` | | |
| 19 | The counterfactual view has an unbounded cost | `[O]` | | |

## References

Crosby, S. A. and Wallach, D. S. (2009). Efficient Data Structures for Tamper-Evident Logging. USENIX Security Symposium. Accessed 2026-08-12.

Fowler, M. (2005). Event Sourcing. Accessed 2026-08-12.

Haber, S. and Stornetta, W. S. (1991). How to Time-Stamp a Digital Document. Journal of Cryptology 3(2). Accessed 2026-08-12.

NIST (2014). SP 800-162, Guide to Attribute Based Access Control Definition and Considerations. Accessed 2026-08-12.

Regulation (EU) 2024/1689 of the European Parliament and of the Council laying down harmonised rules on artificial intelligence. Accessed 2026-08-12.

Vernon, V. (2013). *Implementing Domain-Driven Design*. Addison-Wesley. Accessed 2026-08-12.

**Verification note.** Every reference is verified against the published version and its accessed date corrected before this edition leaves DRAFT.

## Version History

| Version | Date | Status | Change |
|---|---|---|---|
| v1.1-public | 2026-10-18 | DRAFT | Aligned with the NEO x100 Intelligence Operating System architecture and capability register v2.0. Terminology migrated to the x100 vocabulary. Sections 4.3 to 4.5 now connect the argument to Mission Control as the operating-system view, with FOCUS, NORMAL and JARVIS as three projections of one Mission state, the right inspector, the ASK ME / AUTO / AUTONOMOUS approval policy, mandatory Human Gates and visible progressive work. Published correction of the statement that nothing described was running: NEO Core, LILI and the Mission state are in operational deployment inside My NEO Group and in controlled pilots with external users (S2); Mission Control, the Mission Envelope, Human Gates, policy enforcement, the Event log and Verification are in validation (S3); general public availability is targeted for early 2027. Thesis, withholdings and falsifier unchanged. |
| v1.0-public | 2026-08-12 | DRAFT | First public edition, on Founder determination of 2026-08-12. Withholds the source's event schema and closed event-type vocabulary, the integrity chain construction, the approval object schema and invalidation conditions, and the containment trigger list and response ladder. Section 3.2 replaces the withheld schema with a statement of the six questions every governance event answers. Section 4.2 replaces the withheld object with its four required properties. Section 3.4 is retained essentially verbatim from the source, because it is the strongest public argument in the corpus and reducing it would weaken the edition. A section connecting the record to the orchestration it records is added at 4.3. |
| v1.0 | 2026-08-09 | DRAFT | First full draft. |

## How to Cite

Mosse, M. (2026). *Mission Control: A Governance Architecture for Autonomous Work*, public edition. NEO AI Research Program, `NEO-AI-R-003` v1.1-public. `https://neoai.myneogroup.com/id/NEO-AI-R-003`
