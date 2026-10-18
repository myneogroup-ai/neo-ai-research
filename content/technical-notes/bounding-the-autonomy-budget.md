# NEO-AI-TN-001 - Bounding the Autonomy Budget

**Deriving an autonomy level from reversibility and potential loss, and never from model confidence**

| Field | Value |
|---|---|
| Identifier | NEO-AI-TN-001 |
| Title | Bounding the Autonomy Budget |
| Family | NOTE |
| Type | Technical Note (`TN`) |
| Version | v1.1 |
| Status | DRAFT |
| Date | 2026-10-18 |
| Author | Mickael Mosse |
| Capability keys | `mission-control` (S3), `core.governance` (S3), `core.task-graph` (S2), `core.verification` (S3), `core.event-bus` (S3), `mission.envelope` (S3), `human-gates` (S3) |
| Claim-class counts | `[E]` 2 . `[A]` 17 . `[D]` 9 . `[O]` 3 |
| Figures | SYS-12 |
| Reading time | 9 minutes |
| Canonical URL | `https://neoai.myneogroup.com/research/technical-notes/bounding-the-autonomy-budget/` |


---

## 1. Problem statement

An agent needs a permission decision for every consequential step, and the decision has to be made before the step runs. The common implementation reads the model's own confidence and acts unsupervised above a threshold. That couples permission to a number the acting component produced about itself, which fails in the one case that matters: the confidently wrong action. This note derives the autonomy level from properties of the task instead, contracts it on defined signals, and blocks automatic expansion.

## 2. Context and constraints

The Mission Envelope, the bound on a mission's permissions, data scope, resource budget, autonomy level and terminal conditions, is implemented and in validation `[D]` (mission.envelope, S3). Autonomy is one dimension of that envelope, and this note concerns only that dimension. Envelope construction as a whole belongs to `NEO-AI-ARCH-001`.

Four constraints are fixed and this note does not revisit them. The Policy Plane decides whether an action may happen and the Authority Plane decides who may permit it; the collapsed alternative, in which one mechanism answers both, is named and refuted at `[NEO-AI-ARCH-002 s2.4]` `[A]`. Recording the two decisions separately is implemented in policy enforcement and is in validation `[D]` (core.governance, S3). Autonomy is a property of a task node, not of a mission, because a single mission routinely contains steps of very different consequence. `[A]` Contraction must be available synchronously, since a contraction that lands after the action has executed is a log entry rather than a control. `[A]` And the derivation must be computable before execution from attributes known at planning time, which excludes anything that depends on the result.

NIST AI 600-1 treats human oversight configuration as a risk-management action for generative systems and does not prescribe a derivation. `[E]` ISO/IEC 42001 requires documented roles and decision rights for AI processes, which is the governance obligation this note operationalises rather than the mechanism. `[E]` The mechanism below is architectural interpretation.

## 3. The note

### 3.1 Two axes, four levels

The autonomy level for a task node is derived from two task properties.

**Reversibility.** The cost and latency of undoing the effect. `[A]` Four bands: reversible by the system within the mission; reversible by the operator within the retention window; reversible only by a counterparty or an external process; irreversible. A file written to a scratch bucket is the first. A payment instruction accepted by a bank is the third at best.

**Potential loss.** The worst credible consequence if the action is wrong, expressed in units the organisation already uses for risk, not in currency. `[A]` Four bands: negligible, contained, material, severe. Units are deliberately abstract because the note must not state financial figures and because the bands have to survive being read by an insurer, a regulator and an engineer.

Both are attributes of the action type and its parameters, and both are knowable at planning time. `[A]` Neither depends on how the model feels about its plan.

Four autonomy levels result.

| Level | Name | Meaning |
|---|---|---|
| A0 | Propose | The agent produces a plan or draft. No side effect. |
| A1 | Execute with pre-approval | A named human approves this specific action before it runs. |
| A2 | Execute with notification and hold | The action runs after a hold window during which a supervisor may cancel. |
| A3 | Execute and report | The action runs; the record is available for review afterwards. |

### 3.2 Derivation

The level is the more restrictive of the two axes. `[A]` The lookup is a table rather than a formula, because a formula invites tuning and a table invites argument, and argument is the correct behaviour when someone wants an action to be less supervised.

| Reversibility | Negligible | Contained | Material | Severe |
|---|---|---|---|---|
| System-reversible in mission | A3 | A3 | A2 | A1 |
| Operator-reversible in window | A3 | A2 | A1 | A1 |
| Externally reversible only | A2 | A1 | A1 | A0 |
| Irreversible | A1 | A1 | A0 | A0 |

Model confidence appears nowhere in the table, and that omission is the substance of this note. `[A]` A model's confidence is a statement about its own output distribution. Permission is a statement about what the organisation is willing to lose. They are different quantities and the first is not evidence for the second. `[A]`

### 3.3 Contraction

Contraction is automatic, immediate, and applies to the remaining task nodes in the mission. `[A]` Five triggers, each producing a one-level reduction, floored at A0.

- The Evidence Chain for a claim the task depends on shows fewer than two distinct origins. See `NEO-AI-TN-002`.
- A verification step returns a failure or an unresolved conflict.
- A tool returns an error class the plan did not anticipate.
- Resource consumption crosses a defined fraction of the mission budget, which is a proxy for the plan having been wrong about the work.
- A policy decision point returns DENY for any node in the mission.

Two triggers firing produce two levels of contraction. `[A]` The reductions compose, and there is no decay: a mission that has contracted stays contracted for its duration. Restoring the level within the same mission would let a system that recovered from a failure treat the recovery as evidence that the failure did not matter.

### 3.4 Expansion is never automatic

Expansion requires a human authority decision, recorded with the actor, the scope, the justification and an expiry. `[A]` It is scoped to a task class rather than to a mission, so that granting it does not silently raise autonomy for unrelated work in the same run. `[A]`

The attraction of automatic expansion is genuine and should be stated. A system that has completed four hundred instances of a task class without incident is being supervised at a level the evidence does not support, and the supervision has a real cost in operator attention, which is finite and which is being spent on the wrong steps. `[A]` It was rejected anyway. Success history is a measure of how often the action was taken and did not visibly fail, and for actions whose failures are silent or delayed, that is not the same as a measure of correctness. `[A]` The relevant asymmetry is that expansion is the change that removes a control, so its evidential bar should be higher than the bar for the change that adds one, and history satisfies the lower bar.

## 4. Worked example

Four task classes from a supplier due-diligence mission, derived against the table.

| Task class | Reversibility | Potential loss | Level | Note |
|---|---|---|---|---|
| Retrieve and extract from a licensed corporate registry | System-reversible in mission | Negligible | A3 | Read-only. Licence scope is enforced by policy, not by autonomy. |
| Write a resolved entity to semantic memory | Operator-reversible in window | Material | A1 | Wrong merges propagate to every later claim about the entity. |
| Send a clarification request to the supplier | Externally reversible only | Contained | A1 | Cannot be unsent. Signals an investigation to its subject. |
| Publish the finding to the client's vendor system | Irreversible | Severe | A0 | Enters the client's record of decision. Proposal only. |

Row two is the one that surprises people. The write is technically easy to undo and the class is A1 anyway, because reversibility is measured on the effect and not on the operation. `[A]` Reverting the memory row does not revert the eleven downstream claims that were asserted against the merged entity in the interim, and enumerating those requires the lineage traversal described in `NEO-AI-R-005 s4.1`.

Now apply contraction. During the mission, the Evidence Chain for the ownership claim underlying row four resolves to one origin. Every remaining node drops one level. Row one falls to A2, row two to A0, row three to A0, row four stays at A0. `[A]` The mission continues and produces a proposal, which is the intended outcome: weak evidence narrows what may be done with it, in the same run, without an operator noticing first.

## 5. Design intent for NEO AI

The Task Graph of NEO Core carries autonomy as a per-node attribute, derived at planning time and re-evaluated on each contraction trigger. `[D] (core.task-graph, S2)` Governed configuration for the derivation table, versioned rather than coded, with changes emitting a runtime Decision Record, is implemented in policy enforcement and is in validation. `[D] (core.governance, S3)` Contraction driven by events on the event log (Event Bus) and by Verification outcomes, applied before the next node is dispatched, is implemented and in validation. `[D] (core.event-bus, S3)` `[D] (core.verification, S3)` The requirement that expansion carry a Human Authority decision with actor, scope, justification and expiry, and be refused to any non-human actor, is implemented and in validation. `[D] (mission-control, S3)` The approval policy ASK ME / AUTO / AUTONOMOUS and the mandatory Human Gates are implemented and in validation, and they compose with the derived level in one direction only: the policy can only narrow what is auto-approved at a given level, and a mandatory Human Gate sits outside every policy and every level, so an action it covers waits for a human decision even where the table yields A3. `[D] (human-gates, S3)` The Mission Control display of the current level per node, the triggers that fired, and the level the node would have held without them is implemented and in validation. `[D] (mission-control, S3)` Figure `SYS-12` draws the budget and its contraction path.

## 6. Limits of this note

The loss bands are ordinal and this note does not define them. Mapping an organisation's risk taxonomy onto four bands is the work that determines whether the table produces sensible answers, and it is deployment-specific. `[O]`

Composite actions defeat the derivation. A single tool call that both writes a record and notifies a counterparty has two reversibility profiles, and the note's answer, which is to take the worse one, is a blunt instrument that will over-restrict useful tools. Decomposing such tools is the better fix and is not always available. `[O]`

Delegated autonomy is unspecified. When an agent spawns a sub-agent, whether the child inherits the parent's level or a strictly lower one is not settled, and it interacts with the actor-identity gap recorded in `NEO-AI-R-005 s6`. `[O]`

Not covered: the approval routing mechanism, the hold-window duration policy, the operator interface, and any measurement of whether these levels produce better outcomes. No such measurement exists.

## Scope and Limitations

This note specifies a derivation and its contraction behaviour. It establishes no property of an implementation, and reports no operational data. Section 5 states the status of each component it names; this note reports no measurement of any of them, and no status has been verified by an independent third party. The four-level scale and the table are architectural interpretation, not an external finding, and neither NIST AI 600-1 nor ISO/IEC 42001 prescribes them.

The note would be falsified by a demonstration that model-reported confidence predicts action-level harm better than reversibility and loss do, on a task distribution resembling enterprise work with delayed and silent failures included.

## Related Research

- `NEO-AI-R-005` Evidence, Memory and Accountability in Agentic Systems (DRAFT) - the Evidence Chain trigger in section 3.3 and the lineage argument in section 4.
- `NEO-AI-R-003` Mission Control: A Governance Architecture for Autonomous Work (DRAFT).

## Related Publications

- `NEO-AI-P-002` Why NEO AI Is Being Built Around Human Authority (DRAFT).

## Related Technical Notes

- `NEO-AI-TN-002` Detecting Circular Corroboration in an Evidence Chain (DRAFT) - supplies the first contraction trigger.
- `NEO-AI-TN-003` What Belongs in a Mission Event (DRAFT) - the contraction event record.

## Related Architecture

- `NEO-AI-ARCH-001` Mission Control (RESERVED) - Mission Envelope construction.
- `NEO-AI-ARCH-013` Cost and Resource Governance (RESERVED) - the budget-fraction trigger.

Forward references only. Neither is cited in support of a claim.

## Related Engineering

- `NEO-AI-ENG-001` Mission Control Runtime (RESERVED).

Forward reference only.

## Related Figures

- `SYS-12` Human Authority - autonomy as an allocated budget with dynamic contraction. Referenced in section 5.

## Related Terms

Mission Envelope . Bounded Autonomy . Human Authority . Task Graph . Decision Record . Policy Plane . Authority Plane . Containment . Circular Corroboration.

## References

NIST (2024). Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile. National Institute of Standards and Technology. NIST AI 600-1. doi:10.6028/NIST.AI.600-1. Accessed 2026-08-09. VERIFICATION REQUIRED: publication year and exact title.

ISO/IEC (2023). ISO/IEC 42001:2023 Information technology - Artificial intelligence - Management system. International Organization for Standardization. ISO/IEC 42001:2023. Accessed 2026-08-09.

Rose, S. et al. (2020). Zero Trust Architecture. National Institute of Standards and Technology. NIST SP 800-207. doi:10.6028/NIST.SP.800-207. Accessed 2026-08-09.

OWASP GenAI Security Project (2025). Securing Agentic Applications Guide 1.0. OWASP Foundation. Version 1.0. https://genai.owasp.org/resource/securing-agentic-applications-guide-1-0/. Accessed 2026-08-09. VERIFICATION REQUIRED: document version and publication date.

All entries are UNVERIFIED under the Program publication standard until the verification ledger records otherwise.

## Version History

| Version | Date | Status | Change |
|---|---|---|---|
| v1.0 | 2026-08-09 | DRAFT | Initial public draft. |
| v1.1 | 2026-10-18 | DRAFT | Aligned with the NEO x100 Intelligence Operating System architecture and capability register v2.0: capability keys migrated to v2.0, statuses and verbs corrected (Task Graph in operation at S2; Mission Envelope, Mission Control, policy enforcement, Verification and the event log implemented and in validation at S3). Added the composition of the derived level with the ASK ME / AUTO / AUTONOMOUS approval policy and mandatory Human Gates. The derivation, table and contraction rules are unchanged. |
