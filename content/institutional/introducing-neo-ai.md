# NEO-AI-P-001 - Introducing NEO AI: Intelligence Orchestrated

**Capability has become abundant. Orchestration has not. This is a statement of what the platform is, what it is designed to become, and an exact account of how much of it is in operation.**

| Field | Value |
|---|---|
| Identifier | NEO-AI-P-001 |
| Title | Introducing NEO AI: Intelligence Orchestrated |
| Family | PUBLICATION |
| Type | Institutional Publication (`P`) |
| Version | v1.1 |
| Status | DRAFT |
| Date | 2026-10-18 |
| Author | Mickael Mosse |
| Capability keys | `core` (S2), `x100` (S5), `lili` (S2), `availability.general` (S5), `intelligence-profiles` (S3), `lili.always-on` (S4), `model-sovereignty.api-first` (S2), `model-sovereignty.hybrid` (S4), `model-sovereignty.neo-optimised` (S5), `mission-control` (S3), `mission.state` (S2), `core.governance` (S3), `human-gates` (S3), `core.event-bus` (S3), `core.task-graph` (S2), `core.routing` (S2), `core.memory` (S3), `core.knowledge-graph` (S4), `core.verification` (S3), `mission.envelope` (S3), `core.resource-accounting` (S3), `neo-credits` (S4), `x100.mixture-of-agents` (S3), `x100.adaptive-cascades` (S3), `x100.semantic-reuse` (S4), `x100.speculative-parallel` (S4), `x100.verification-driven-allocation` (S4), `x100.hybrid-execution` (S4), `x100.context-optimisation` (S3), `execution-fabric` (S4), `edge-compute` (S4), `deployment.managed` (S2), `deployment.private-cloud` (S5), `deployment.hybrid` (S5), `deployment.self-hosted` (S5), `deployment.sovereign` (S5), `verticals.pilot-anchored` (S2), `verticals.shared-core` (S4), `verticals.zero-counted` (S5), `market.b2g` (S5), `neo-intelligence` (S4), `compounding-loop` (S4) |
| Claim-class counts | `[E]` 6 . `[A]` 31 . `[D]` 71 . `[O]` 10. Counted mechanically by `scripts/count_claims.py` over the body and back matter, excluding this row |
| Figures | SYS-02 |
| Reading time | 26 min |
| Canonical URL | `https://neoai.myneogroup.com/research/institutional/introducing-neo-ai/` |

Founder's Annotations are attributed editorial annotations prepared for and approved by Mickael Mosse. They are not historical quotations and carry no claim class.

**Correction notice for v1.1.** Version 1.0 stated that the platform was a specification and that most of the capability register stood at designed and specified or planned. That was accurate on 2026-08-09 and it is no longer accurate. NEO AI and LILI are now in operational deployment inside My NEO Group and in controlled pilot programmes with external users, and this version also aligns the text with the NEO x100 Intelligence Operating System architecture. The superseded wording remains resolvable at the pinned v1.0 route, and section 8 states the current status of every component by register key.

---

## 1. The position

An organisation of any size can reach a dozen capable models in an afternoon, across language, code, vision, audio and structured reasoning, at a price that no longer requires a business case. That access has not turned into an operating capability, and the gap is not closing on its own. The NEO AI Research Program holds that the durable layer in enterprise artificial intelligence is the system that decides which model runs, on what data, under whose authority, against what evidence, and with what record left behind. `[A]` Models are workers. The layer that governs them is the institution's asset, because it is the only part that survives the next model release. `[A]`

NEO AI is built as that layer: an Intelligence Operating System that orchestrates leading models, autonomous agents, tools, data sources, memory, verification, enterprise controls and heterogeneous compute as one coordinated system `[D]` (core, S2). The objective is not simply a more capable assistant. It is a system that is more efficient, more reliable and more accountable than any of its parts used alone, and that multiplies useful intelligence per unit of compute over time `[D]` (x100, S5).

The platform is no longer only a specification. NEO Core and LILI are in operational deployment inside My NEO Group and in controlled pilot programmes with external users `[D]` (core, S2) `[D]` (lili, S2). That is an operational product at real scale, not a demonstration, and it is not yet generally available: general public availability, global, is targeted for early 2027 `[D]` (availability.general, S5). Much of what this publication describes beyond the core is still implemented and in validation, designed, or planned. Section 8 states the status of each component, by name and by register key, without softening in either direction. A reader who wants to know what runs today should read that section first.

## 2. What the problem looks like from inside an organisation

The failure is not dramatic. Nothing crashes and no error is logged, because nothing is recording.

**Context is rebuilt by hand, repeatedly, by different people.** An analyst opens a supplier file on Monday: three corporate registry extracts, two contracts, a sanctions screen, eleven pages of prior correspondence, and a working view of who owns what. The session ends. On Tuesday a colleague picks up the same file, assembles the same material again in a different order, misses one of the contracts, and reaches an answer that differs at the margin. Neither person did anything wrong. The organisation has no object that holds the assembled state, so the assembly is performed again each time, and the cost is paid in the one resource nobody meters.

**There is no record of what was decided, only of what was produced.** Somebody accepted the output. That acceptance happened by copying text out of a chat window into a document, and it left no trace that names the person, the moment, the version accepted or what they were shown when they accepted it. Six months later the organisation can produce the wording that went to the counterparty. It cannot produce the approval. The distinction matters to exactly one class of reader, and that class includes regulators, litigators, auditors and insurers.

**There is no way to tell which output can be relied on.** Two paragraphs arrive in the same session, in the same typeface, at the same level of fluency. One is grounded in a licensed registry extract from this week. The other is the model's recollection of a company's ownership structure as it stood some time before its training cut-off, expressed with the same composure. Nothing in the presentation distinguishes them.

The third symptom is not an implementation defect that better engineering removes. Confidently stated content that is not grounded in any source is identified in the standards literature as a characteristic risk of generative systems, alongside information integrity and the configuration of human oversight `[E]`. The third symptom is also the one that gets worse as models improve. A less capable model produces recognisably weaker prose when it is guessing, and the weakness is a signal. A more capable model produces prose of even quality whether or not it has grounds, which removes the signal while leaving the problem. `[A]` Capability improvements therefore raise the value of a system that can separate a grounded assertion from an ungrounded one, and they do not supply it.

There is a fourth symptom, and it is economic. Sending every unit of work to the largest available model is the simplest way to use artificial intelligence and the most expensive one, and a simple extraction then consumes the same class of compute as difficult strategic reasoning. `[A]` Inference cost, GPU capacity and energy become central constraints as adoption scales, which makes the allocation of compute a design problem rather than a procurement line. `[A]`

None of this is solved by procuring a better model, because none of it is a model defect. It is the absence of an operating layer between the human objective and the model call.

## 3. Three elements, and what each refuses to do

The platform is described in three parts. The relationship between them is fixed, and the constraints matter more than the labels.

**LILI is the face of the platform** `[D]` (lili, S2). A private user, a professional or an enterprise team opens NEO the way they would open any assistant: one conversation, one objective, one result. Open NEO, ask LILI, receive the result. LILI receives an objective in the person's own language, asks for the clarifications it is missing, and shows what is being proposed and what is happening `[D]` (lili, S2). The person accepts an Intelligence Profile, a resource envelope, and never chooses from a list of models `[D]` (intelligence-profiles, S3). LILI proposes Missions into the platform and never grants the authority to run them `[D]` (lili, S2). That single restriction is what stops a natural language surface from becoming a permission surface. Stating an objective is not the same act as authorising every means of achieving it, and a system that treats the two as one has moved authorisation into a text box. `[A]` LILI Always-on, a continuous presence with a wake word and hands-free voice that follows running Missions and alerts the person when a decision is theirs, is on the roadmap and always remains inside Human Gates `[D]` (lili.always-on, S4). Figure `SYS-03` draws the separation.

**NEO AI is the Intelligence Operating System** `[D]` (core, S2). Its orchestration layer, NEO Core, holds the representation of work, the policy context, the record of what happened and the decision about what happens next `[D]` (core, S2). NEO Core contains no model weights and performs no inference of its own `[D]` (core, S2). Models sit outside it and are addressed through adapters. Leading external systems are orchestrated through their APIs today, without any one provider being structurally mandatory `[D]` (model-sovereignty.api-first, S2). Open-weight and private models deployed on NEO-controlled infrastructure are the next phase `[D]` (model-sovereignty.hybrid, S4), and a NEO-optimised layer of fine-tuned, distilled and task-specific models is a later one `[D]` (model-sovereignty.neo-optimised, S5). Any such model is intended to sit in the same worker layer and be addressed through the same adapter contract as any external model. NEO does not own a frontier foundation model today and does not claim to.

That last point is worth dwelling on because it is counter-intuitive for a company that intends to optimise its own models. If the orchestration layer contained a model, policy would degrade into prompt instructions, substitution would become a migration rather than a registry operation, and the audit record would become a sequence of generations with plausible explanations attached rather than a sequence of decisions with named rules. `[A]` The architecture treats the Program's own future models as replaceable workers for the same reason it treats everyone else's that way. Models remain replaceable; the system around them is what accumulates.

**Mission Control is the operating-system view** `[D]` (mission-control, S3). It renders one Mission state in three projections: FOCUS keeps the conversation and the decision; NORMAL adds the execution plan, the active agents, artefacts and evidence; JARVIS adds the command core, live orchestration, the observed build and the task graph `[D]` (mission-control, S3). The three are projections and not applications. Switching mode changes what the person sees and never what NEO is doing: execution is not restarted and no second Mission is created `[D]` (mission.state, S2). A universal right inspector exposes Progress, Output and Context in every mode. Mission Control is implemented and in validation. It permits an authorised user to pause, redirect, contain or terminate work, and commands issued from it re-enter through the same policy path as any other proposal, which means the supervisory surface holds no privileged bypass `[D]` (mission-control, S3). Figure `SYS-01` draws the projections resolved from one event-sourced state.

Calling the platform an operating system describes an architectural role: a layer that allocates scarce resources, mediates access, and outlives the programs that run on it. It is not a claim that one model performs every task autonomously.

## 4. The eight planes, for a reader who does not build systems

Architecture documents usually decompose a platform by kind of component: an agent layer, a model layer, a tool layer. It is easy to draw and it answers the wrong questions. Ask it who is allowed to decide that this piece of work may send an email to a client, and the answer is distributed across three of its layers and owned by none of them. `[A]`

The NEO AI Plane Model decomposes the platform by question answered instead. There are exactly eight planes, and the model is normative within the Program.

| # | Plane | The question it owns |
|---|---|---|
| 1 | Interaction | What does the person want, and what can they see |
| 2 | Reasoning | How is the objective turned into work |
| 3 | Execution | What actually happened outside the system, and where it ran |
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

The rule that governs the interaction is short. A policy decision may reference an approval and may never create one. An approval may narrow what policy permits and may never widen it. Where the two disagree, the intersection governs, and the disagreement is recorded as its own event class, because a persistent disagreement is a configuration defect and should be visible as one `[D]` (core.governance, S3).

In the product this appears as two separate controls. The person sets an approval policy, ASK ME, AUTO or AUTONOMOUS, and that policy can only narrow what is approved automatically. Mandatory Human Gates sit outside every policy, and no setting, profile or mode reaches them: production DNS changes, publishing to a public domain, act-class connector actions and the release of a deployment `[D]` (human-gates, S3). Agents receive capability tools, never credentials, and the gates are refused at platform level rather than only in the interface `[D]` (human-gates, S3). More intelligence, more agents or more compute never create more authority.

### 4.2 Three things a plane is not

A plane is not a place where software runs. Policy enforcement is deliberately distributed into every component that can cause an effect, so the Policy Plane has no cluster of its own. `[A]`

A plane is not an order of operations. Nothing calls downward through the eight in sequence. A single tool invocation touches Execution, Policy, Authority, Assurance and Memory in an order set by the operation. Drawing the planes stacked vertically implies a call order that does not exist, and the Program prohibits the drawing for that reason. `[A]`

One component sits in several planes, and the overlaps are the point. The event log is the substrate of the Execution Plane, because an event is how a side effect becomes known, and of the Assurance Plane, because replay is a fold over the same log `[D]` (core.event-bus, S3). Where two planes overlap in one component is exactly where a contract is needed, and the model earns its keep by locating those places.

## 5. From conversation to Mission

Most products of this generation begin and end with a conversation. NEO AI begins with an objective, and the difference is structural rather than stylistic.

A conversation has no acceptance criteria, so "finished" is a judgment the participants make and do not write down. It has no bounds, so the question of what the system was permitted to do never arises until it has already done it. It has no state that outlives the window, no record of who accepted the result, and no representation of the work itself, which means there is nothing to inspect between the request and the answer.

A Mission is a different object. It carries an objective with non-empty acceptance criteria, a bounded envelope, a structured representation of the work, an evidence position, an authority chain and a defined terminal condition `[D]` (core.task-graph, S2). NEO Core decomposes a Mission into coordinated sub-tasks, tens or hundreds today and in principle thousands, assigns each one to the most suitable capability and permitted execution zone, executes them in parallel, cross-checks their results, escalates only the difficult parts to more powerful models and assembles the verified output `[D]` (core, S2). A Mission with empty acceptance criteria is rejected at creation rather than admitted with a default, because a default converts every later evaluation question into an argument about what was originally intended `[D]` (core.task-graph, S2).

The components carrying most of the weight are each defined as much by what they refuse as by what they do.

**The Task Graph** holds the durable representation of the work: typed nodes, their dependencies, the data flowing between them, the points at which an approval is required, and the reverse action for anything that had an external effect `[D]` (core.task-graph, S2). It evaluates completion itself and never accepts an actor's assertion that its own node is done `[D]` (core.task-graph, S2). That rule closes the most common failure in agent systems, in which the component with the strongest incentive to declare success is the component permitted to declare it. `[A]` Figure `SYS-06` draws it as a control structure rather than as a picture of a workflow.

**The Router**, Dynamic Capability Routing, selects for each unit of work among models, agents, tools, runtimes, data sources, verifiers, human capabilities and execution zones, by capability and never by brand `[D]` (core.routing, S2). The ordering is the contract: legal constraints, policy and authority compute the set of admissible paths first, security and privacy narrow it, quality and verification thresholds are applied next, and only then are availability, latency, cost and energy optimised inside what remains `[D]` (core.routing, S2). A prohibited model is never scored, so it can never win on capability. When no compliant path exists the Router fails safely rather than routing around policy, and when the registry is unavailable it fails closed with no default worker, because a router that falls back to a hard-coded model at the moment its registry is down has reintroduced provider coupling precisely when it is least visible `[D]` (core.routing, S2).

**Memory and the Knowledge Graph** are two things, deliberately. Memory holds what the system retains about itself across typed stores with separate retention, access and write rules, and refuses to treat retrieved content as instruction; it is implemented and in validation `[D]` (core.memory, S3). Content arriving from a retrieved document or a tool result is treated as untrusted data in the agentic threat-modelling literature, not as a directive the system may follow `[E]`. The Knowledge Graph is specified to hold what the system asserts about the world, with every material edge carrying its evidence class and its lineage back to a source, and asserted, extracted, inferred, hypothesised and disputed never merged into one edge type `[D]` (core.knowledge-graph, S4). Provenance of that shape is expressible because the modelling of entities, activities, agents and derivation relations is already standardised `[E]`. Figures `SYS-05` and `SYS-04` draw the two.

**Verification** is a heterogeneous system rather than a persona: schema checks, deterministic tests, source reconciliation, independent model review and human judgment, in that order of preference where a choice exists `[D]` (core.verification, S3). The producing model is never a blocking verifier of its own output `[D]` (core.verification, S3). Verification is implemented and in validation.

Around all of it sits the Mission Envelope: the bounded set of permissions, data scope, resource budget, autonomy level and terminal conditions within which the Mission may operate. It is set at Mission creation, contracts automatically on defined signals, and expands only by an explicit act of human authority carrying an actor, a scope, a justification and an expiry `[D]` (mission.envelope, S3).

Resource use is part of the Mission boundary rather than an after-the-fact accounting exercise. Provider usage, provider cost and a normalised NEO resource are metered internally and enforced against the Mission budget `[D]` (core.resource-accounting, S3). The person sees one unit, NEO Credits, and never the provider tokens or the mix of execution locations behind it `[D]` (neo-credits, S4). The public edition does not disclose the underlying unit list, reservation mechanics or implementation parameters.

The event log records material state changes in an append-only form with no update and no delete path in the interface `[D]` (core.event-bus, S3). Mission state is then derived by folding that log. Where a stored view and the log disagree, the view is quarantined and rebuilt, and the log is never reconciled to the view `[D]` (core.event-bus, S3). The same rule is what makes the product truth principle enforceable: no simulated agents, progress, tests, evidence, cost or verified state, and visible progressive work rather than private chain-of-thought `[D]` (mission-control, S3).

### 5.1 Intelligence per compute

The same architecture that governs the work also decides how much compute the work deserves. The Program's long-term R&D objective, called NEO x100, is an order-of-magnitude improvement in verified intelligence delivered per unit of total compute, through orchestration rather than through larger models or more GPUs `[D]` (x100, S5). It is an objective and not a measured result, and no multiple is stated or guaranteed here.

Eight optimisation layers carry the objective. Mixture-of-Agents coordinates independent specialised agents on parts of one Mission `[D]` (x100.mixture-of-agents, S3). Adaptive Model Cascades start a task on the least expensive capable model and escalate on confidence, complexity, verification or policy `[D]` (x100.adaptive-cascades, S3). Dynamic Capability Routing chooses what performs each unit of work and where it executes `[D]` (core.routing, S2). Semantic Compute Reuse is designed to reuse verified, still-valid work instead of regenerating it `[D]` (x100.semantic-reuse, S4). Speculative Parallel Intelligence is designed to explore candidate approaches, prune weak branches early and concentrate compute on disputed paths `[D]` (x100.speculative-parallel, S4). Verification-Driven Compute Allocation is designed to spend additional reasoning only where an independent verifier finds it necessary `[D]` (x100.verification-driven-allocation, S4). Hybrid API, private and self-hosted execution is designed to place workloads across the execution zones described in section 6 `[D]` (x100.hybrid-execution, S4). Memory and Context Optimisation builds the minimum authoritative context each invocation needs instead of resending full history `[D]` (x100.context-optimisation, S3).

The constraint that matters is the envelope. The cheapest model does not automatically win: cost, latency, data movement and energy are minimised only inside the Mission's required quality, verification, security, jurisdiction, authority, privacy and availability. `[A]` The unit of optimisation is the cost of a verified Mission outcome, not the price of each call, because a cheap first call that causes five retries costs more than one stronger call, and high-stakes Missions may deliberately spend more on independent analysis and deeper verification. `[A]` Whether the layers compound as the architecture intends is unmeasured, and the measurement is the Program's to publish when it exists `[O]`.

## 6. One system, several deployment patterns and execution zones

Enterprise environments are not uniform, and the common response is a global privacy setting that routes everything to the most restrictive environment available. That is expensive, and it is a poor control besides: it erases the distinction between a workload that needs the restriction and one that does not, which is the distinction the organisation is being asked to manage. `[A]`

The unit of placement is designed to be the workload, not the enterprise. The NEO Execution Fabric defines four normalised execution zones, Edge, Customer Private, NEO Controlled and External, and every unit of work is placed at the intersection of three envelopes: Intelligence, set by the profile; Policy, which says where data and actions may go; and Capability, which says what resources exist now `[D]` (execution-fabric, S4). A placement policy evaluates the sensitivity and legal classification of inputs and outputs, jurisdiction and residency requirements, the model capability and modality required, latency and availability needs, whether retention or learning is permitted, the tool and connector dependencies, audit and deletion obligations, and the reversibility and impact of the action `[D]` (core.governance, S3). The result may place one task on an external service, another in a single-tenant private environment, and a third on infrastructure with no external egress, within one Mission, because policy and Mission state live in the orchestration layer rather than in any one inference endpoint `[D]` (core, S2). Only the data the selected path needs moves, and local preprocessing does not by itself make external processing compliant. `[A]` Figure `SYS-15` draws the continuum.

NEO Edge Compute extends the same logic to the person's own device: local when sufficient, quality-gated, policy-first and escalated to stronger resources when the local path does not satisfy the envelope `[D]` (edge-compute, S4). It is cross-platform by design, across Apple, Windows and Linux, it is permissioned, bounded and revocable, and a person's device serves only that person's own Missions. User-owned compute is not free compute: it consumes electricity, hardware and attention. `[A]`

Deployment is a separate question from execution. The same system is designed to run in five patterns: public and managed, private cloud, hybrid, self-hosted, and sovereign or high-control where required and legally supported, with the same Mission, policy, audit and NEO Credits semantics in each.

Private artificial intelligence is an operating model rather than a hosting choice, and this is the part most procurement processes get wrong. Running weights on infrastructure an organisation controls is a real technical property and it is not a privacy guarantee. `[A]` The dependency graph of an AI workload is wider than the weights: prompts, retrieved documents, embeddings, vector indexes, tool credentials, observability data, model artefacts, software updates, evaluation datasets and support workflows. If any of those transmits sensitive material outside the approved boundary, the system is not private in the sense the buyer intended. If administrators can read content without control, locality has not produced confidentiality. If the organisation cannot patch, evaluate or replace the model, ownership of the compute coexists with strategic dependence. `[A]` Standards guidance on AI risk management treats these as lifecycle and supply-chain concerns rather than as siting concerns `[E]`, and the Program's reading is that "private" should therefore be defined as effective control over data, execution, identity, lifecycle and exit `[A]`. Figure `SYS-17` draws the full dependency graph.

Now the exact part. The NEO-managed deployment is the target delivery model and it is in operation today, inside My NEO Group and in controlled pilot programmes `[D]` (deployment.managed, S2). Private cloud deployment is planned `[D]` (deployment.private-cloud, S5). Hybrid deployment is planned `[D]` (deployment.hybrid, S5). Self-hosted deployment is planned `[D]` (deployment.self-hosted, S5). Sovereign and high-control deployment is planned `[D]` (deployment.sovereign, S5). No private cloud, hybrid, self-hosted or sovereign deployment has been performed. Any reader evaluating the platform against a residency obligation should treat those four patterns, the Customer Private zone and Edge Compute as a design position rather than as an available option.

## 7. Verticals as configuration of one core

A vertical is a configuration of the same Intelligence Operating System: its own sources, workflows, tools, verifiers, evidence policy and domain governance, over shared services `[D]` (core, S2). Reuse occurs at the level of orchestration, identity, models, agents, memory, governance, verification and compute, and no vertical builds its own execution stack. NEO AI is one product, configured per industry. Figure `SYS-13` draws a vertical as configuration rather than as a separate product.

Thirteen verticals are defined on the shared core. Three are pilot-anchored today, Hospitality and Nightlife, Micro-Credit, and Trading and Treasury, and are exercised in pilot programmes whose counts and client identities are never disclosed `[D]` (verticals.pilot-anchored, S2). Software Factory, Company Builder, Fintech Studio, Payments, Sport and Wellness and RWA Studio are designed on the same core and built when demand is proven `[D]` (verticals.shared-core, S4). Health and Care, Legal Ops and Travel are counted at zero `[D]` (verticals.zero-counted, S5). The same core serves individuals and professionals, organisations and, where applicable, government users, with a different capability envelope for each class; government and sovereign programmes are subject to the relevant product and legal framework `[D]` (market.b2g, S5).

NEO Intelligence is the worked case. It is specified as an orchestration and reasoning layer above intelligence providers, designed to orchestrate lawful access to public sources, commercial interfaces, enterprise-licensed databases and client-controlled information, to resolve entities, reconstruct timelines, map relationships and produce evidence-linked findings under human review `[D]` (neo-intelligence, S4). It orchestrates screening results and is not an adjudication authority. It is designed and specified, it has not launched, and it is counted at zero. An earlier internal title for the corresponding text asserted a launch that has not occurred, and that assertion was corrected against the Program's own record rather than quietly dropped.

The caveat is the load-bearing part of this section, and it cuts against the commercial attraction of the architecture. Shared orchestration does not make two domains interchangeable. `[A]` A platform that works in supplier due diligence has demonstrated nothing about clinical documentation, and the shared Task Graph, Router, Memory and Evidence Layer are precisely the components that could not tell the difference. Domain validity has to be earned separately in each vertical, and earning it means at minimum: a verifier set matched to the domain's failure modes, an evidence policy naming what counts as a sufficient source there, a licence position for each data source, an approval topology matched to who is professionally accountable in that domain, and an evaluation against tasks drawn from the domain rather than from a general benchmark. `[A]`

There is a specific fallacy this section exists to refuse. Orchestration generalises; domain validity does not; and the appearance of the first is routinely sold as evidence of the second. `[A]` The Program has no measurement of how much verification effort transfers between two verticals sharing one core, and does not currently know how to estimate it `[O]`.

## 8. Capability status

This section states where the platform actually stands. It is unusual for a company publication and it is included because a reader who has been misled by vendors before has no reason to accept any of the preceding sections without it. It now cuts both ways: understating a component that is in operation is as much a misstatement as overstating one that is not.

The status codes are fixed and their glosses are not paraphrased anywhere in the Program: `S1` operational and publicly available; `S2` operational in a controlled pilot or limited deployment; `S3` implemented, undergoing validation; `S4` designed and specified; `S5` planned or exploratory.

The table is rendered from capability register version 2.0. The full register, including retired keys and their successors, is at the Capability Register page and in `capabilities.json`.

| Capability | Key | Status |
|---|---|---|
| NEO Core, the Intelligence Operating System orchestration layer | `core` | S2 |
| LILI, the conversational face of NEO AI | `lili` | S2 |
| LILI Always-on: continuous presence and hands-free voice | `lili.always-on` | S4 |
| One Mission state | `mission.state` | S2 |
| Mission Envelope | `mission.envelope` | S3 |
| Mission Control: FOCUS, NORMAL and JARVIS projections | `mission-control` | S3 |
| Observe Build | `observe-build` | S3 |
| NEO Intelligence Profiles: NEO AUTO, PULSE, PRIME, AXIOM, APEX | `intelligence-profiles` | S3 |
| Human Gates and approval policy: ASK ME, AUTO, AUTONOMOUS | `human-gates` | S3 |
| Task Graph | `core.task-graph` | S2 |
| Dynamic Capability Routing (NEO Router) | `core.routing` | S2 |
| Memory: persistent, verified, with provenance | `core.memory` | S3 |
| Knowledge Graph | `core.knowledge-graph` | S4 |
| Verification: independent verifiers and cross-checking | `core.verification` | S3 |
| Resource accounting and NEO Credits metering | `core.resource-accounting` | S3 |
| Event log (Event Bus) | `core.event-bus` | S3 |
| Policy enforcement | `core.governance` | S3 |
| Evidence Layer | `core.evidence-layer` | S4 |
| Evidence Ledger | `core.evidence-ledger` | S4 |
| NEO x100: verified intelligence per unit of compute | `x100` | S5 |
| Mixture-of-Agents | `x100.mixture-of-agents` | S3 |
| Adaptive Model Cascades | `x100.adaptive-cascades` | S3 |
| Semantic Compute Reuse | `x100.semantic-reuse` | S4 |
| Speculative Parallel Intelligence | `x100.speculative-parallel` | S4 |
| Verification-Driven Compute Allocation | `x100.verification-driven-allocation` | S4 |
| Hybrid API, Private and Self-Hosted Execution | `x100.hybrid-execution` | S4 |
| Memory and Context Optimisation | `x100.context-optimisation` | S3 |
| NEO Execution Fabric: four execution zones | `execution-fabric` | S4 |
| NEO Edge Compute and Device Compute Profile | `edge-compute` | S4 |
| Model sovereignty Phase 1: multi-provider API orchestration | `model-sovereignty.api-first` | S2 |
| Model sovereignty Phase 2: hybrid execution | `model-sovereignty.hybrid` | S4 |
| Model sovereignty Phase 3: NEO-optimised model and execution layer | `model-sovereignty.neo-optimised` | S5 |
| Public and managed deployment (NEO-managed SaaS) | `deployment.managed` | S2 |
| Private cloud deployment | `deployment.private-cloud` | S5 |
| Hybrid deployment | `deployment.hybrid` | S5 |
| Self-hosted deployment | `deployment.self-hosted` | S5 |
| Sovereign and high-control deployment | `deployment.sovereign` | S5 |
| Pilot-anchored verticals: Hospitality and Nightlife, Micro-Credit, Trading and Treasury | `verticals.pilot-anchored` | S2 |
| Further verticals on the shared core: Software Factory, Company Builder, Fintech Studio, Payments, Sport and Wellness, RWA Studio | `verticals.shared-core` | S4 |
| Verticals counted at zero: Health and Care, Legal Ops, Travel | `verticals.zero-counted` | S5 |
| NEO Intelligence | `neo-intelligence` | S4 |
| General public availability, global, B2C and B2B | `availability.general` | S5 |
| Government and sovereign programmes | `market.b2g` | S5 |
| NEO Credits, the customer-facing usage unit | `neo-credits` | S4 |
| System-level learning loop | `compounding-loop` | S4 |
| NEO orchestration and compute-optimisation stack as licensable infrastructure | `infrastructure-licensing` | S5 |
| Pilot programmes | `pilots` | S2 |
| Public website | `public-website` | S1 |
| Investor Data Room frontend | `dataroom.frontend` | S3 |
| Investor Data Room backend | `dataroom.backend` | S3 |
| Mission Evaluation Harness | `assurance.eval-harness` | S5 |

Of 51 entries in register version 2.0, 1 is `S1`, 9 are `S2`, 15 are `S3`, 15 are `S4` and 11 are `S5`. A reader should draw the right conclusion from both ends of that distribution. The core experience, a Mission stated to LILI, decomposed, routed across providers, verified and delivered, is in operation in controlled deployment. Much of the surrounding architecture, including the projections, the profiles, the Human Gates and several x100 layers, is implemented and in validation. Edge Compute, the Execution Fabric's private zones, LILI Always-on, every deployment pattern other than the managed one, NEO Intelligence and the later model sovereignty phases are designed or planned, and nothing in this publication should be read as saying otherwise.

Three further statements belong here rather than in a footnote. Register version 1.3 was ratified by the Founder on 2026-08-13; version 2.0, which restructures the register to the x100 architecture and records the Founder determination of 2026-10-18 on the operational state, is pending the Founder's ratification at the Program's own gate, and if any status moves before ratification the affected sentences move with it `[O]`. No independent third party has verified any status in the table. And the Program has built a control that fails the build when a status token in any public text disagrees with the register, which closes one gap recorded in `NEO-AI-P-007`, while the register that control reads has still not been audited by anyone outside the Program `[O]`.

## 9. What NEO AI is not

**It is not a chatbot.** The conversation is the surface and one plane of eight, and it holds no authority of its own `[D]` (lili, S2). A product whose architecture terminates at the conversation cannot answer the questions in section 2, because those questions are about objects the conversation does not create.

**It is not a model, and it is not a model switcher.** The orchestration layer contains no weights and runs no inference `[D]` (core, S2). Nothing in this publication should be read as a claim about model quality, and no benchmark result belonging to any model, including any model NEO may later optimise, is a statement about this platform. External models are named in Program material only as third-party systems NEO can orchestrate, with no ownership, endorsement or partnership implied. That argument is made in full in `NEO-AI-P-007`.

**It is not a replacement for regulated professionals.** In high-impact domains the platform is designed to support qualified professionals and authorised institutions, and not to substitute for licensing, fiduciary responsibility, clinical judgment, legal advice or regulatory decision-making. The boundary is carried in the product as permissions and approval gates rather than as a disclaimer at the foot of a page `[D]` (human-gates, S3).

**It does not train on what it is given.** Mission execution data, evaluation signals, routing performance and verification performance are designed to improve how the system allocates resources, with no change to model weights `[D]` (compounding-loop, S4). Personal context is read access and never training consent, customer confidential information is never automatically used to train models, and the explicit choice to help improve NEO is off by default. `[A]`

**It is not an independent auditor of itself.** The Assurance Plane is internal. It makes a Mission's conduct reconstructible by someone who was not present, which is a genuine and useful property, and it is not third-party attestation. `[A]` An internal verification record is evidence that can be examined by an external party; it is not the examination. The Program has no external certification, no completed third-party security assessment published against the platform, and no independent evaluation of any capability in section 8 `[O]`.

**It is not finished, and it is not generally available.** It is in operation in controlled deployment, inside My NEO Group and with external pilot users. General public availability is targeted for early 2027, and a target is not a commitment `[D]` (availability.general, S5). Every sentence in sections 3 through 7 carries the status of the component it describes, and the verb follows the status.

## 10. How this position can be tested

Publish the architecture in enough detail that an engineer can find the errors, and record the errors when they are found. The Program's architecture documents state contracts with named failure modes, idempotency keys and the assumptions callers may not make, which is a form that admits contradiction.

Show a Mission with its record intact. The falsifiable version of section 5 is a Mission whose event log, evidence chain, runtime decision records and approval trail can be handed to somebody who was not present, and from which that person can reconstruct what happened and identify who was entitled to cause each consequential step. Missions now run in controlled deployment; a Mission record of that kind has not yet been handed to an outside party and published `[O]`.

Have the capability register audited by somebody outside the Program, and publish the result including the corrections. Then evaluate at the level of the Mission rather than the model, because a benchmark score for a component says nothing about a trajectory through a task graph with policy gates, verification and human approval in it. `[A]` The mission-level evaluation methodology for that is `[NEO-AI-ENG-008]`, which specifies nine measures together with what it cannot measure. No measurement taken against it has been published `[O]`. The same holds for x100: the claim is testable only as verified intelligence delivered per unit of total compute, including the cost of NEO itself, and no such figure has been published `[O]`.

## 11. What would change this position

The central proposition is that orchestration is the durable layer. It would be substantially weakened if frontier models absorbed planning, tool use, memory and policy enforcement to the point where an external orchestration layer added latency and cost without adding control `[O]`. The Program's reading is that the governance properties in sections 4 and 5 are the part least likely to be absorbed, because they concern the organisation rather than the task, but this is a reading and not a finding. `[A]`

It would also be weakened by evidence that enterprises do not in practice want the record. If organisations consistently accept ungoverned output because the governed path is slower, the value of the Authority and Assurance planes is theoretical and the market has answered the question. `[A]` Controlled deployment is now producing the first operational experience of that question; the Program has not measured it and would rather say so than model it `[O]`.

---

**FOUNDER'S ANNOTATION | MICKAEL MOSSE**

I started from a practical irritation: a person should not have to assemble models, tools and specialist workflows before they are allowed to state what they want. The interface should get simpler while the operating system underneath it gets stricter. What I will not trade away is the record. If the platform ever produces work that nobody can reconstruct, or an approval that names no one, then it has become the thing I set out to replace, whatever it says on the front page.

---

## Scope and Limitations

This publication states a position, describes an architecture and reports the status of each of its components. It reports no benchmark result, no measurement of any kind, and no evaluation performed by anyone inside or outside the Program; the operational state in section 8 is a Founder determination, not a measured result. It contains no financial information, no terms of any financing instrument, no valuation, no client name and no reference to any listed vehicle.

Not covered: component internals, wire formats, security control requirements, evaluation methodology, tenant isolation, the connector fabric and the mission event schema. Each is held elsewhere in the corpus or is reserved and unwritten.

The eight-plane model is architectural interpretation. Neither ISO/IEC 42001, ISO/IEC 23894, NIST AI 100-1 nor NIST AI 600-1 prescribes or endorses it. Where this document cites those sources it cites them for the obligation, never for the mechanism.

This document would be falsified by any of the following: a demonstration that the Policy and Authority planes can be collapsed without losing the entitlement question; evidence that domain validity transfers across verticals sharing an orchestration layer; a deployed system that meets the section 2 problems without an orchestration layer; or a material error in the capability register in section 8, which is pending ratification at version 2.0 and is unaudited.

## Related Research

- `NEO-AI-R-001` The End of the Single-Model Enterprise (DRAFT) - behind section 3 and the Router in section 5.
- `NEO-AI-R-003` Mission Control: A Governance Architecture for Autonomous Work (DRAFT) - sections 3 and 4.
- `NEO-AI-R-004` Private AI Is an Operating Model, Not a Deployment Choice (DRAFT) - the argument compressed into section 6.
- `NEO-AI-R-005` Evidence, Memory and Accountability in Agentic Systems (DRAFT) - the Memory and Knowledge separation in section 5.
- `NEO-AI-R-002` From AI Assistants to Governed Agent Systems (DRAFT) - bounded autonomy, underlying the Mission Envelope.
- `NEO-AI-R-008` The New Enterprise Stack (DRAFT) - the generic industry reference stack, a comparison and not the plane model.
- `NEO-AI-R-009` From Model Intelligence to System Intelligence (DRAFT) - why orchestration compounds, behind section 5.1.

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

- `NEO-AI-ARCH-002` NEO Core: Component Architecture and Contracts (DRAFT) - the normative source for the plane model and the components in section 5.
- `NEO-AI-ARCH-001` Mission Control (RESERVED) - Mission Envelope construction and the supervisory surface.
- `NEO-AI-ARCH-003` LILI (RESERVED).
- `NEO-AI-ARCH-008` Deployment (RESERVED) - the placement policy in section 6.
- `NEO-AI-ARCH-013` Cost and Resource Governance (RESERVED) - the resource accounting paragraph in section 5.

RESERVED entries are forward references. None is cited in support of a claim.

## Related Engineering

- `NEO-AI-ENG-008` Mission-Level Evaluation Methodology (RESERVED) - the open problem recorded in section 10.
- `NEO-AI-ENG-005` Deployment Runtime (RESERVED).

Forward references only.

## Related Figures

- `SYS-02` NEO Core - the single conceptual diagram for this publication, referenced in section 3. The model layer is drawn explicitly outside the orchestration services.
- Referenced in passing: `SYS-01` Mission Control and `SYS-03` LILI (section 3); `SYS-04` Knowledge Graph, `SYS-05` Memory Graph and `SYS-06` Task Graph (section 5); `SYS-15` Deployment Models and `SYS-17` Private AI (section 6); `SYS-13` Vertical Architecture (section 7).

## Related Terms

Intelligence Operating System . NEO Core . Mission . Mission State . Mission Envelope . Task Graph . Router . Dynamic Capability Routing . Interaction Plane . Reasoning Plane . Execution Plane . Memory Plane . Knowledge Plane . Policy Plane . Authority Plane . Assurance Plane . Evidence Layer . Evidence Chain . Evidence Ledger . Verification Layer . Human Gate . Approval Policy . Intelligence Profile . FOCUS . NORMAL . JARVIS . Execution Fabric . Execution Zone . NEO Edge Compute . NEO Credits . Intelligence-per-Compute . Model Sovereignty . Capability Register . Capability Gate . Human Authority . Decision Record . Claim Class . Capability Status . Bounded Autonomy . Containment . Graceful Substitution.

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
| v1.1 | 2026-10-18 | DRAFT | Correction of status. NEO Core and LILI are in operational deployment inside My NEO Group and in controlled pilots with external users (S2), and general public availability is targeted for early 2027; sections 1, 3, 5, 6, 7, 8, 9 and 10 restated accordingly. Aligned with the NEO x100 Intelligence Operating System architecture and capability register v2.0: terminology migrated, section 5.1 on intelligence per compute added, Human Gates and approval policy added to section 4.1, five deployment patterns and four execution zones in section 6, thirteen verticals in section 7, section 8 rendered from the register, and the canonical URL corrected. |
