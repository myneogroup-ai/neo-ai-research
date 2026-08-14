# NEO-AI-P-001 - Introducing NEO AI: Intelligence Orchestrated

**Capability has become abundant. Orchestration has not. This is a statement of what the platform is designed to be, and an account of how much of it exists.**

| Field | Value |
|---|---|
| Identifier | NEO-AI-P-001 |
| Title | Introducing NEO AI: Intelligence Orchestrated |
| Family | PUBLICATION |
| Type | Institutional Publication (`P`) |
| Version | v1.0 |
| Status | DRAFT |
| Date | 2026-08-09 |
| Author | Mickael Mosse |
| Capability keys | `lili` (S4), `mission-control` (S4), `brain` (S4), `brain.task-graph` (S4), `brain.router` (S4), `brain.memory` (S4), `brain.knowledge-graph` (S4), `brain.validation` (S4), `brain.cost-engine` (S4), `brain.event-bus` (S4), `brain.governance` (S4), `foundation-model` (S5), `neo-intelligence` (S4), `deployment.cloud` (S4), `deployment.vpc` (S5), `deployment.onprem` (S5), `public-website` (S1), `dataroom.frontend` (S3), `dataroom.backend` (S3), `pilots` (S2), `brain.evidence-layer` (S4), `brain.evidence-ledger` (S4), `mission.envelope` (S4) |
| Claim-class counts | `[E]` 6 . `[A]` 25 . `[D]` 39 . `[O]` 6 . Counted mechanically over the body and back matter, excluding this row |
| Figures | SYS-02 |
| Reading time | 24 min |
| Canonical URL | `https://neoai.myneogroup.com/publications/neo-ai-p-001` (placeholder, not yet resolvable) |

Founder's Annotations are attributed editorial annotations prepared for and approved by Mickael Mosse. They are not historical quotations and carry no claim class.


---

## 1. The position

An organisation of any size can reach a dozen capable models in an afternoon, across language, code, vision, audio and structured reasoning, at a price that no longer requires a business case. That access has not turned into an operating capability, and the gap is not closing on its own. The NEO AI Research Program holds that the durable layer in enterprise artificial intelligence is the system that decides which model runs, on what data, under whose authority, against what evidence, and with what record left behind. `[A]` Models are workers. The layer that governs them is the institution's asset, because it is the only part that survives the next model release. `[A]`

Everything described in this publication is design intent unless stated otherwise. Sixteen of the twenty entries in the capability register are at `S4`, designed and specified, or `S5`, planned or exploratory. Section 8 states the status of each one, by name, without softening. A reader who wants to know what exists today should read that section first and then decide whether the rest is worth their time.

## 2. What the problem looks like from inside an organisation

The failure is not dramatic. Nothing crashes and no error is logged, because nothing is recording.

**Context is rebuilt by hand, repeatedly, by different people.** An analyst opens a supplier file on Monday: three corporate registry extracts, two contracts, a sanctions screen, eleven pages of prior correspondence, and a working view of who owns what. The session ends. On Tuesday a colleague picks up the same file, assembles the same material again in a different order, misses one of the contracts, and reaches an answer that differs at the margin. Neither person did anything wrong. The organisation has no object that holds the assembled state, so the assembly is performed again each time, and the cost is paid in the one resource nobody meters.

**There is no record of what was decided, only of what was produced.** Somebody accepted the output. That acceptance happened by copying text out of a chat window into a document, and it left no trace that names the person, the moment, the version accepted or what they were shown when they accepted it. Six months later the organisation can produce the wording that went to the counterparty. It cannot produce the approval. The distinction matters to exactly one class of reader, and that class includes regulators, litigators, auditors and insurers.

**There is no way to tell which output can be relied on.** Two paragraphs arrive in the same session, in the same typeface, at the same level of fluency. One is grounded in a licensed registry extract from this week. The other is the model's recollection of a company's ownership structure as it stood some time before its training cut-off, expressed with the same composure. Nothing in the presentation distinguishes them.

The third symptom is not an implementation defect that better engineering removes. Confidently stated content that is not grounded in any source is identified in the standards literature as a characteristic risk of generative systems, alongside information integrity and the configuration of human oversight `[E]`. The third symptom is also the one that gets worse as models improve. A less capable model produces recognisably weaker prose when it is guessing, and the weakness is a signal. A more capable model produces prose of even quality whether or not it has grounds, which removes the signal while leaving the problem. `[A]` Capability improvements therefore raise the value of a system that can separate a grounded assertion from an ungrounded one, and they do not supply it.

None of this is solved by procuring a better model, because none of it is a model defect. It is the absence of an operating layer between the human objective and the model call.

## 3. Three elements, and what each refuses to do

The platform is described in three parts. The relationship between them is fixed, and the constraints matter more than the labels.

**LILI is the interface** `[D]` (lili, S4). It is designed as the surface through which a person states an objective in their own language, is asked for the clarifications the objective is missing, and is shown what is being proposed. LILI is specified to propose missions into the platform and never to grant the authority to run them `[D]` (lili, S4). That single restriction is what stops a natural language surface from becoming a permission surface. Stating an objective is not the same act as authorising every means of achieving it, and a system that treats the two as one has moved authorisation into a text box. `[A]` Figure `SYS-03` draws the separation.

**NEO AI is the operating system** `[D]` (brain, S4). The orchestration layer, referred to as the Brain, is specified to hold the representation of work, the policy context, the record of what happened and the decision about what happens next `[D]` (brain, S4). It is specified to contain no model weights and to perform no inference of its own `[D]` (brain, S4). Models sit outside it and are addressed through adapters. The NEO AI Foundation Model, when it exists, is intended to sit in that same worker layer and to be addressed through the same adapter contract as any external model `[D]` (foundation-model, S5).

That last point is worth dwelling on because it is counter-intuitive for a company that intends to build a model. If the orchestration layer contained a model, policy would degrade into prompt instructions, substitution would become a migration rather than a registry operation, and the audit record would become a sequence of generations with plausible explanations attached rather than a sequence of decisions with named rules. `[A]` The architecture treats the Program's own future model as a replaceable worker for the same reason it treats everyone else's that way.

**Mission Control is the command and governance environment** `[D]` (mission-control, S4). It is specified to read the platform's append-only event log and to render mission state, evidence, active agents, validation results, permissions in force and decisions awaiting a person `[D]` (mission-control, S4). It is specified to permit an authorised user to pause, redirect, contain or terminate work `[D]` (mission-control, S4). Commands issued from it re-enter through the same policy path as any other proposal, which means the supervisory console holds no privileged bypass `[D]` (mission-control, S4). Figure `SYS-01` draws the four views it resolves from one event-sourced state.

Calling the platform an operating system describes an architectural role: a layer that allocates scarce resources, mediates access, and outlives the programs that run on it. It is not a claim that one model performs every task autonomously.

## 4. The eight planes, for a reader who does not build systems

Architecture documents usually decompose a platform by kind of component: an agent layer, a model layer, a tool layer. It is easy to draw and it answers the wrong questions. Ask it who is allowed to decide that this piece of work may send an email to a client, and the answer is distributed across three of its layers and owned by none of them. `[A]`

The NEO AI Plane Model decomposes the platform by question answered instead. There are exactly eight planes, and the model is normative within the Program.

| # | Plane | The question it owns |
|---|---|---|
| 1 | Interaction | What does the person want, and what can they see |
| 2 | Reasoning | How is the objective turned into work |
| 3 | Execution | What actually happened outside the system |
| 4 | Memory | What does the system remember about itself, and may it |
| 5 | Knowledge | What is being claimed about the world, and on what evidence |
| 6 | Policy | May this happen |
| 7 | Authority | Who may decide that it happens |
| 8 | Assurance | Can this be checked, challenged and reconstructed |

Three of these divisions are conventional. Five are the substance of the design, and one of the five is the reason the model exists.

### 4.1 Policy and Authority are two questions, not one

Most enterprise systems have a governance component, and inside it one mechanism answers two questions that are not the same question.

The first is whether an action is permitted. That is a rule evaluated against attributes: this actor, this data classification, this jurisdiction, this kind of side effect, therefore permit or deny. It is fast, deterministic, and indifferent to whether the actor is a person, a software agent or a scheduled job. The Policy Plane owns it.

The second is who was entitled to permit it. That is a fact about the organisation: who holds which mandate, what they delegated and to whom, which approval exists, what it was bound to, and who authorised the last expansion of the bounds. The Authority Plane owns it.

An institutional reader will recognise the distinction because their organisation already makes it elsewhere. A bank's payment system enforces limits, and that is policy. Separately, the bank maintains a mandate register recording which officer may raise a limit and under what conditions, and that is authority. No competent institution keeps the second in the first. `[A]`

Collapsing them produces an audit trail with a specific and recognisable gap. It records that an action was allowed. It does not record who was entitled to allow it. The gap is invisible during normal operation and it surfaces at the worst possible moment, the first time the organisation is asked to explain a decision to somebody outside it, and the answer is a rule identifier with no human being at the end of the chain. `[A]` Standards work already points at this ground without closing it: an AI management system is expected to make roles, responsibilities and decision rights explicit and auditable `[E]`, and AI risk management is expected to be traceable through the lifecycle rather than asserted at release `[E]`. The plane split is the Program's reading of what "auditable" has to mean mechanically. `[A]`

The split has a cost, and the honest version of this section states it. Two mechanisms means two failure domains, two availability requirements on the path that matters, and a class of confusing incident in which policy permits something that authority does not, or the reverse. The Program accepts that cost. The alternative is an unanswerable question in front of an audience that will not accept "the system allowed it" as an answer. `[A]`

The rule that governs the interaction is short. A policy decision may reference an approval and may never create one. An approval may narrow what policy permits and may never widen it. Where the two disagree, the intersection governs, and the disagreement is recorded as its own event class, because a persistent disagreement is a configuration defect and should be visible as one `[D]` (brain.governance, S4).

### 4.2 Three things a plane is not

A plane is not a place where software runs. Policy enforcement is deliberately distributed into every component that can cause an effect, so the Policy Plane has no cluster of its own. `[A]`

A plane is not an order of operations. Nothing calls downward through the eight in sequence. A single tool invocation touches Execution, Policy, Authority, Assurance and Memory in an order set by the operation. Drawing the planes stacked vertically implies a call order that does not exist, and the Program prohibits the drawing for that reason. `[A]`

One component sits in several planes, and the overlaps are the point. The Event Bus is specified as the substrate of the Execution Plane, because an event is how a side effect becomes known, and as the substrate of the Assurance Plane, because replay is a fold over the same log `[D]` (brain.event-bus, S4). Where two planes overlap in one component is exactly where a contract is needed, and the model earns its keep by locating those places.

## 5. From conversation to mission

Most products of this generation begin and end with a conversation. NEO AI is designed to begin with an objective, and the difference is structural rather than stylistic.

A conversation has no acceptance criteria, so "finished" is a judgment the participants make and do not write down. It has no bounds, so the question of what the system was permitted to do never arises until it has already done it. It has no state that outlives the window, no record of who accepted the result, and no representation of the work itself, which means there is nothing to inspect between the request and the answer.

A mission is a different object. It is specified to carry an immutable objective with non-empty acceptance criteria, a bounded envelope, a structured representation of the work, an evidence position, an append-only authority chain and a defined terminal condition `[D]` (brain.task-graph, S4). A mission with empty acceptance criteria is specified to be rejected at creation rather than admitted with a default, because a default converts every later evaluation question into an argument about what was originally intended `[D]` (brain.task-graph, S4).

Four components carry most of the weight, and each is defined as much by what it refuses as by what it does.

**The Task Graph** is specified to hold the durable representation of the work: typed nodes, their dependencies, the data flowing between them, the points at which an approval is required, and the reverse action for anything that had an external effect `[D]` (brain.task-graph, S4). It is specified to evaluate completion itself and never to accept an actor's assertion that its own node is done `[D]` (brain.task-graph, S4). That rule closes the most common failure in agent systems, in which the component with the strongest incentive to declare success is the component permitted to declare it. `[A]` Figure `SYS-06` draws it as a control structure rather than as a picture of a workflow.

**The Router** is specified to select a model or other worker per task, scored against quality, latency, resource cost, deployment boundary fit and independence `[D]` (brain.router, S4). The ordering is the contract: policy computes the set of admissible workers first, and only members of that set are scored `[D]` (brain.router, S4). A prohibited model is never scored, so it can never win on capability. When the registry is unavailable the Router is specified to fail closed with no default worker, because a router that falls back to a hard-coded model at the moment its registry is down has reintroduced provider coupling precisely when it is least visible `[D]` (brain.router, S4).

**Memory and the Knowledge Graph** are two things, deliberately. Memory is specified to hold what the system retains about itself across five typed stores with separate retention, access and write rules, and to refuse to treat retrieved content as instruction `[D]` (brain.memory, S4). Content arriving from a retrieved document or a tool result is treated as untrusted data in the agentic threat-modelling literature, not as a directive the system may follow `[E]`. The Knowledge Graph is specified to hold what the system asserts about the world, with every material edge carrying its evidence class and its lineage back to a source, and asserted, extracted, inferred, hypothesised and disputed never merged into one edge type `[D]` (brain.knowledge-graph, S4). Provenance of that shape is expressible because the modelling of entities, activities, agents and derivation relations is already standardised `[E]`. Figures `SYS-05` and `SYS-04` draw the two.

**Validation** is specified as a heterogeneous system rather than a persona: schema checks, deterministic tests, source reconciliation, independent model review and human judgment, in that order of preference where a choice exists `[D]` (brain.validation, S4). The producing model is specified never to be a blocking validator of its own output `[D]` (brain.validation, S4).

Around all of it sits the Mission Envelope: the bounded set of permissions, data scope, resource budget, autonomy level and terminal conditions within which the mission may operate. It is set at mission creation, is specified to contract automatically on defined signals, and is specified to expand only by an explicit act of human authority carrying an actor, a scope, a justification and an expiry `[D]` (mission-control, S4).

The Cost Engine makes resource use part of the mission boundary rather than an after-the-fact accounting exercise. Resource consumption is metered in physical units and enforced against the mission budget through reservation. The public edition does not disclose the underlying unit list, reservation mechanics or implementation parameters.

The Event Bus is specified to record material state changes to an append-only log with no update and no delete path in the interface `[D]` (brain.event-bus, S4). Mission state is then derived by folding that log. Where a stored view and the log disagree, the view is specified to be quarantined and rebuilt, and the log is never reconciled to the view `[D]` (brain.event-bus, S4).

## 6. One system, several deployment boundaries

Enterprise environments are not uniform, and the common response is a global privacy setting that routes everything to the most restrictive environment available. That is expensive, and it is a poor control besides: it erases the distinction between a workload that needs the restriction and one that does not, which is the distinction the organisation is being asked to manage. `[A]`

The unit of placement is designed to be the workload, not the enterprise `[D]` (brain.governance, S4). A placement policy is specified to evaluate the sensitivity and legal classification of inputs and outputs, jurisdiction and residency requirements, the model capability and modality required, latency and availability needs, whether retention or learning is permitted, the tool and connector dependencies, audit and deletion obligations, and the reversibility and impact of the action `[D]` (brain.governance, S4). The result may place one task on an external service, another in a single-tenant private cloud environment, and a third on infrastructure with no external egress, within one mission, because policy and mission state live in the orchestration layer rather than in any one inference endpoint `[D]` (brain, S4). Figure `SYS-15` draws the continuum.

Private artificial intelligence is an operating model rather than a hosting choice, and this is the part most procurement processes get wrong. Running weights on infrastructure an organisation controls is a real technical property and it is not a privacy guarantee. `[A]` The dependency graph of an AI workload is wider than the weights: prompts, retrieved documents, embeddings, vector indexes, tool credentials, observability data, model artefacts, software updates, evaluation datasets and support workflows. If any of those transmits sensitive material outside the approved boundary, the system is not private in the sense the buyer intended. If administrators can read content without control, locality has not produced confidentiality. If the organisation cannot patch, evaluate or replace the model, ownership of the compute coexists with strategic dependence. `[A]` Standards guidance on AI risk management treats these as lifecycle and supply-chain concerns rather than as siting concerns `[E]`, and the Program's reading is that "private" should therefore be defined as effective control over data, execution, identity, lifecycle and exit `[A]`. Figure `SYS-17` draws the full dependency graph.

Now the honest part. Platform cloud deployment is at `S4`, designed and specified `[D]` (deployment.cloud, S4). Client VPC deployment is at `S5`, planned or exploratory `[D]` (deployment.vpc, S5). On-premise and sovereign deployment is at `S5`, planned or exploratory `[D]` (deployment.onprem, S5). No client VPC deployment has been performed. No sovereign deployment has been performed. The continuum described above is an architecture the Program intends to build and has not yet built, and any reader evaluating the platform against a residency obligation should treat this section as a design position rather than as an available option.

## 7. Verticals as configuration of one Brain

A vertical is designed as a configuration of the same orchestration layer: its own sources, workflows, tools, validators, evidence policy and domain governance, over shared services `[D]` (brain, S4). Reuse occurs at the level of orchestration, memory, governance and evidence. Figure `SYS-13` draws a vertical as configuration rather than as a separate product.

NEO Intelligence is the worked case. It is specified as an investigation and intelligence layer designed to orchestrate lawful access to public sources, commercial interfaces, enterprise-licensed databases and client-controlled information, to resolve entities, reconstruct timelines, map relationships and produce evidence-linked findings under human review `[D]` (neo-intelligence, S4). It is designed and specified. It has not launched. An earlier internal title for the corresponding text asserted a launch that has not occurred, and that assertion was corrected against the Program's own record rather than quietly dropped.

The caveat is the load-bearing part of this section, and it cuts against the commercial attraction of the architecture. Shared orchestration does not make two domains interchangeable. `[A]` A platform that works in supplier due diligence has demonstrated nothing about clinical documentation, and the shared Task Graph, Router, Memory and Evidence Layer are precisely the components that could not tell the difference. Domain validity has to be earned separately in each vertical, and earning it means at minimum: a validator set matched to the domain's failure modes, an evidence policy naming what counts as a sufficient source there, a licence position for each data source, an approval topology matched to who is professionally accountable in that domain, and an evaluation against tasks drawn from the domain rather than from a general benchmark. `[A]`

There is a specific fallacy this section exists to refuse. Orchestration generalises; domain validity does not; and the appearance of the first is routinely sold as evidence of the second. `[A]` The Program has no measurement of how much validation effort transfers between two verticals sharing a Brain, and does not currently know how to estimate it `[O]`.

## 8. Capability status

This section states where the platform actually stands. It is unusual for a company publication and it is included because a reader who has been misled by vendors before has no reason to accept any of the preceding sections without it.

The status codes are fixed and their glosses are not paraphrased anywhere in the Program: `S1` operational and publicly available; `S2` operational in a controlled pilot or limited deployment; `S3` implemented, undergoing validation; `S4` designed and specified; `S5` planned or exploratory.

| Capability | Key | Status | Plain reading |
|---|---|---|---|
| Public website | `public-website` | `S1` | Live and publicly reachable. |
| Signed paid pilots | `pilots` | `S2` | Operational in a controlled pilot or limited deployment. Count and identity are not disclosed publicly, in this document or any other. |
| Investor Data Room frontend | `dataroom.frontend` | `S3` | Implemented, undergoing validation. |
| Investor Data Room backend | `dataroom.backend` | `S3` | Implemented, undergoing validation. |
| LILI | `lili` | `S4` | Designed and specified. Not a deployed interface. |
| Mission Control | `mission-control` | `S4` | Designed and specified. Every governance behaviour described in section 3 and section 5 is a specification. |
| The Brain | `brain` | `S4` | Designed and specified. |
| Task Graph | `brain.task-graph` | `S4` | Designed and specified. |
| Router | `brain.router` | `S4` | Designed and specified. |
| Memory | `brain.memory` | `S4` | Designed and specified. |
| Knowledge Graph | `brain.knowledge-graph` | `S4` | Designed and specified. |
| Validation | `brain.validation` | `S4` | Designed and specified. |
| Cost Engine | `brain.cost-engine` | `S4` | Designed and specified. Named in five source texts before it was specified in any of them, which is recorded as an audit finding against the Program. |
| Event Bus | `brain.event-bus` | `S4` | Designed and specified. |
| Governance | `brain.governance` | `S4` | Designed and specified. |
| NEO Intelligence | `neo-intelligence` | `S4` | Designed and specified. Not launched. |
| Platform cloud deployment | `deployment.cloud` | `S4` | Designed and specified. |
| Client VPC deployment | `deployment.vpc` | `S5` | Planned or exploratory. |
| On-premise and sovereign deployment | `deployment.onprem` | `S5` | Planned or exploratory. |
| NEO AI Foundation Model | `foundation-model` | `S5` | Planned or exploratory. Phase 2. The base open-weights architecture is not named publicly. |

Sixteen of twenty entries are `S4` or `S5`. One is `S1`, one is `S2`, two are `S3`. A reader should draw the obvious conclusion: most of this platform is a specification, and the specification is the thing currently on offer for scrutiny.

Two further statements belong here rather than in a footnote. The register itself is marked PROVISIONAL and has not yet been confirmed by the Founder at the Program's own gate, which means the statuses above could move before this document leaves DRAFT, and if any of them moves the affected sentences move with it `[O]`. And no independent third party has verified any status in the table. The Program has designed a control that blocks a publication when a referenced capability status is unconfirmed or below the required level, and that control reads a register nobody outside the Program has audited `[O]`.

## 9. What NEO AI is not

**It is not a chatbot.** The interaction surface is one plane of eight, and it is specified to hold no authority of its own `[D]` (lili, S4). A product whose architecture terminates at the conversation cannot answer the questions in section 2, because those questions are about objects the conversation does not create.

**It is not a model.** The orchestration layer is specified to contain no weights and to run no inference `[D]` (brain, S4). Nothing in this publication should be read as a claim about model quality, and no benchmark result belonging to any model, including the intended NEO AI Foundation Model, is a statement about this platform. That argument is made in full in `NEO-AI-P-007`.

**It is not a replacement for regulated professionals.** In high-impact domains the platform is designed to support qualified professionals and authorised institutions, and not to substitute for licensing, fiduciary responsibility, clinical judgment, legal advice or regulatory decision-making. The boundary is specified to be carried in the product as permissions and approval gates rather than as a disclaimer at the foot of a page `[D]` (brain.governance, S4).

**It is not an independent auditor of itself.** The Assurance Plane is internal. It is designed to make a mission's conduct reconstructible by someone who was not present, which is a genuine and useful property, and it is not third-party attestation. `[A]` An internal validation record is evidence that can be examined by an external party; it is not the examination. The Program has no external certification, no completed third-party security assessment published against the platform, and no independent evaluation of any capability in section 8 `[O]`.

**It is not finished, and this document does not describe a deployed system.** Every present-tense sentence in sections 3 through 7 that describes platform behaviour is a specification, tagged as such, resolving to a register entry at `S4` or `S5`.

## 10. How this position can be tested

Publish the architecture in enough detail that an engineer can find the errors, and record the errors when they are found. The Program's architecture documents state contracts with named failure modes, idempotency keys and the assumptions callers may not make, which is a form that admits contradiction.

Show a mission with its record intact. The falsifiable version of section 5 is a mission whose event log, evidence chain, runtime decision records and approval trail can be handed to somebody who was not present, and from which that person can reconstruct what happened and identify who was entitled to cause each consequential step. That artefact does not exist yet.

Have the capability register audited by somebody outside the Program, and publish the result including the corrections. Then evaluate at the level of the mission rather than the model, because a benchmark score for a component says nothing about a trajectory through a task graph with policy gates, validation and human approval in it. `[A]` The mission-level evaluation methodology for that is `[NEO-AI-ENG-008]`, which is in Wave 1 at DRAFT and specifies nine measures together with what it cannot measure. No measurement has been taken against it and none of the nine has been run on a real mission `[O]`.

## 11. What would change this position

The central proposition is that orchestration is the durable layer. It would be substantially weakened if frontier models absorbed planning, tool use, memory and policy enforcement to the point where an external orchestration layer added latency and cost without adding control `[O]`. The Program's reading is that the governance properties in sections 4 and 5 are the part least likely to be absorbed, because they concern the organisation rather than the task, but this is a reading and not a finding. `[A]`

It would also be weakened by evidence that enterprises do not in practice want the record. If organisations consistently accept ungoverned output because the governed path is slower, the value of the Authority and Assurance planes is theoretical and the market has answered the question. `[A]` The Program has no data on this, and would rather say so than model it.

---

**FOUNDER'S ANNOTATION | MICKAEL MOSSE**

I started from a practical irritation: a person should not have to assemble models, tools and specialist workflows before they are allowed to state what they want. The interface should get simpler while the operating system underneath it gets stricter. What I will not trade away is the record. If the platform ever produces work that nobody can reconstruct, or an approval that names no one, then it has become the thing I set out to replace, whatever it says on the front page.

---

## Scope and Limitations

This publication states a position and describes an intended architecture. It reports no operational data, no benchmark result, no measurement of any kind, and no evaluation performed by anyone inside or outside the Program. It contains no financial information, no terms of any financing instrument, no valuation, no client name and no reference to any listed vehicle.

Not covered: component internals, wire formats, security control requirements, evaluation methodology, tenant isolation, the connector fabric and the mission event schema. Each is held elsewhere in the corpus or is reserved and unwritten.

The eight-plane model is architectural interpretation. Neither ISO/IEC 42001, ISO/IEC 23894, NIST AI 100-1 nor NIST AI 600-1 prescribes or endorses it. Where this document cites those sources it cites them for the obligation, never for the mechanism.

This document would be falsified by any of the following: a demonstration that the Policy and Authority planes can be collapsed without losing the entitlement question; evidence that domain validity transfers across verticals sharing an orchestration layer; a deployed system that meets the section 2 problems without an orchestration layer; or a material error in the capability register in section 8, which is provisional and unaudited.

## Related Research

- `NEO-AI-R-001` The End of the Single-Model Enterprise (DRAFT) - behind section 3 and the Router in section 5.
- `NEO-AI-R-003` Mission Control: A Governance Architecture for Autonomous Work (DRAFT) - sections 3 and 4.
- `NEO-AI-R-004` Private AI Is an Operating Model, Not a Deployment Choice (DRAFT) - the argument compressed into section 6.
- `NEO-AI-R-005` Evidence, Memory and Accountability in Agentic Systems (DRAFT) - the Memory and Knowledge separation in section 5.
- `NEO-AI-R-002` From AI Assistants to Governed Agent Systems (DRAFT) - bounded autonomy, underlying the Mission Envelope.
- `NEO-AI-R-008` The New Enterprise Stack (DRAFT) - the generic industry reference stack, a comparison and not the plane model.

## Related Publications

- `NEO-AI-P-007` A Note on Responsible AI Capability Claims (DRAFT) - the standard section 8 is written under.
- `NEO-AI-P-002` Why NEO AI Is Being Built Around Human Authority (DRAFT) - expands section 4.1.
- `NEO-AI-P-006` NEO Intelligence: A Governed Reasoning Layer for Evidence-Intensive Investigation (DRAFT) - section 7.
- `NEO-AI-P-008` Research, Governance and the NEO AI Public Record (DRAFT) - makes section 8 checkable over time.
- `NEO-AI-P-003` LILI: A New Interface for Complex Work (DRAFT). `NEO-AI-P-004` NEO AI and the Future of Enterprise Creation (DRAFT). `NEO-AI-P-005` Building an AI Ecosystem With Discipline (DRAFT).

## Related Technical Notes

- `NEO-AI-TN-001` Bounding the Autonomy Budget (DRAFT) - the autonomy dimension of the Mission Envelope in section 5.
- `NEO-AI-TN-002` Detecting Circular Corroboration in an Evidence Chain (DRAFT).
- `NEO-AI-TN-003` What Belongs in a Mission Event (DRAFT) - the event log referenced in sections 3 and 5.

## Related Architecture

- `NEO-AI-ARCH-002` The Brain: Component Architecture and Contracts (DRAFT) - the normative source for the plane model and the components in section 5.
- `NEO-AI-ARCH-001` Mission Control (RESERVED) - Mission Envelope construction and the supervisory surface.
- `NEO-AI-ARCH-003` LILI (RESERVED).
- `NEO-AI-ARCH-008` Deployment (RESERVED) - the placement policy in section 6.
- `NEO-AI-ARCH-013` Cost and Resource Governance (RESERVED) - the Cost Engine paragraph in section 5.

RESERVED entries are forward references. None is cited in support of a claim.

## Related Engineering

- `NEO-AI-ENG-008` Mission-Level Evaluation Methodology (RESERVED) - the open problem recorded in section 10.
- `NEO-AI-ENG-005` Deployment Runtime (RESERVED).

Forward references only.

## Related Figures

- `SYS-02` The Brain - the single conceptual diagram for this publication, referenced in section 3. The model layer is drawn explicitly outside the orchestration services.
- Referenced in passing: `SYS-01` Mission Control and `SYS-03` LILI (section 3); `SYS-04` Knowledge Graph, `SYS-05` Memory Graph and `SYS-06` Task Graph (section 5); `SYS-15` Deployment Models and `SYS-17` Private AI (section 6); `SYS-13` Vertical Architecture (section 7).

## Related Terms

Mission . Mission State . Mission Envelope . Task Graph . Router . Interaction Plane . Reasoning Plane . Execution Plane . Memory Plane . Knowledge Plane . Policy Plane . Authority Plane . Assurance Plane . Evidence Layer . Evidence Chain . Evidence Ledger . Validation Layer . Capability Register . Capability Gate . Human Authority . Decision Record . Claim Class . Capability Status . Bounded Autonomy . Containment . Graceful Substitution.

## References

ISO/IEC (2023). ISO/IEC 42001:2023 Information technology - Artificial intelligence - Management system. International Organization for Standardization. Accessed 2026-08-09.

ISO/IEC (2023). ISO/IEC 23894:2023 Information technology - Artificial intelligence - Guidance on risk management. International Organization for Standardization. Accessed 2026-08-09.

Lebo, T., Sahoo, S. and McGuinness, D. (2013). PROV-O: The PROV Ontology. W3C Recommendation, 30 April 2013. World Wide Web Consortium. https://www.w3.org/TR/prov-o/. Accessed 2026-08-09.

National Institute of Standards and Technology (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. doi:10.6028/NIST.AI.100-1. Accessed 2026-08-09.

National Institute of Standards and Technology (2024). Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile. NIST AI 600-1. doi:10.6028/NIST.AI.600-1. Accessed 2026-08-09. REQUIRES VERIFICATION: publication year and exact title.

OWASP GenAI Security Project (2025). Securing Agentic Applications Guide 1.0. OWASP Foundation. https://genai.owasp.org/resource/securing-agentic-applications-guide-1-0/. Accessed 2026-08-09. REQUIRES VERIFICATION: document version, publication date and stable citation form.

All entries are UNVERIFIED under the Program publication standard until the verification ledger records otherwise.

## Version History

| Version | Date | Status | Change |
|---|---|---|---|
| v1.0 | 2026-08-09 | DRAFT | Initial public draft. |
