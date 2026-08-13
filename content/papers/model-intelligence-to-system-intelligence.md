# From Model Intelligence to System Intelligence

**How orchestration compounds capability, and why a stronger model raises the value of the layer above it**

| Field | Value |
|---|---|
| Identifier | **Requested, not allocated.** `NEO-AI-R-009` is requested at `PUB-ACT-02` and is not present in `data/identifiers.json` v1.5. Cite this paper by title and version until the allocation lands |
| Title | From Model Intelligence to System Intelligence: How Orchestration Compounds Capability |
| Family | RESEARCH |
| Type | R - Research Paper |
| Version | v1.0 |
| Status | DRAFT |
| Date | 2026-08-12 |
| Author | Mickael Mosse, NEO AI Research Program |
| Capability keys | `brain` S4 . `brain.router` S4 . `brain.task-graph` S4 . `brain.memory` S4 . `brain.knowledge-graph` S4 . `brain.evidence-layer` S4 . `brain.evidence-ledger` S4 . `brain.validation` S4 . `brain.cost-engine` S4 . `brain.governance` S4 . `brain.event-bus` S4 . `mission-control` S4 . `mission.envelope` S4 . `lili` S4 . `assurance.eval-harness` S5 . `foundation-model` S5 . `neo-intelligence` S4 |
| Claim classes | Counted mechanically over the body and back matter at build time. Not entered by hand |
| Reading time | 29 min |
| Canonical URL | `https://neoai.myneogroup.com/research/papers/model-intelligence-to-system-intelligence/` (placeholder, gated by `PUB-OPEN-01`) |
| Relations | `extends` NEO-AI-R-001 . `applies` NEO-AI-R-003 . `applies` NEO-AI-R-005 . `depends-on` NEO-AI-P-007 . `evidences` NEO-AI-P-001 |
| Register note | Capability statuses resolve from the Founder-ratified canonical Capability Register. Register-level ratification confirms the approved representation of the current S1-S5 maturity classifications; it does **not** operationally ratify individual capabilities. Individual lifecycle ratification remains evidence-dependent. **Nothing in this paper describes a running system unless its capability status says so.** |

---

## Abstract

The industry measures intelligence at the model. Benchmarks score a model, procurement selects a model, and product claims inherit a model's results by adjacency. This paper argues that the measurement is taken at the wrong boundary for most enterprise work, and that the quantity an organisation actually cares about is a property of a system rather than of a component inside it.

The argument has three parts. First, the unit of enterprise work is a task with a required outcome, a permitted set of actions, an authority under which it is performed and a record it must leave, and none of those four is a property a model has. Second, the operations that convert a model call into a completed unit of work, which are decomposition, selection, tool use, retrieval, verification, memory, evidence and approval, are compositional: each raises the probability that the whole is correct, and their effects multiply rather than add. Third, and this is the part that determines whether any of it is worth building, model improvement moves the ceiling on what a single call can do and does not touch attribution, authority, retention, verification or the record. A rising ceiling therefore makes the unsolved parts a **larger** fraction of the remaining problem, not a smaller one.

That third claim is the paper's thesis and it is falsifiable. Section 9 states the conditions under which it fails, in terms specific enough to be tested against. **No measurement is reported here, because none has been taken.** The Program has published no benchmark, holds no reproducible comparison against any other system, and does not claim one.

---

## 1. Where the measurement is taken

A model benchmark answers a well-posed question. Given this input, does the model produce an acceptable output. The question is well-posed because the boundary is clean: input in, output out, score computed.

Enterprise work is not well-posed at that boundary. Consider a task an organisation would actually pay for. Assess whether a counterparty presents an unacceptable risk, given twelve documents in three languages, an internal policy, a regulatory perimeter, a deadline and an obligation to justify the answer to somebody who was not in the room.

Four things are required of the result and none of them is a model output property `[A]`.

**It has to be attributable.** Somebody must be able to ask where a particular assertion came from and receive an answer that resolves to a source rather than to a generation. A model can produce a citation; it cannot make the citation true, and the property that matters is whether the chain from the assertion back to its origin can be traversed after the fact.

**It has to be performed under an authority.** The question is not only whether an action is permitted but who was entitled to decide it is permitted. Those are different questions and a system that answers only the first produces a record showing permission without entitlement `[A]`.

**It has to be bounded.** The set of actions available while performing the task is narrower than the set of actions the components are capable of. That boundary is a property of the task, set before the work starts, and it has no representation inside a model call.

**It has to leave a record.** Not a transcript. A record that supports a later question of the form: at the point that conclusion was reached, what was known, what had been verified, who had approved what, and what had already been ruled out.

A model that improves on every published benchmark improves the raw material for all four and supplies none of them `[A]`. This is the observation the rest of the paper builds on, and it is the reason the measurement boundary matters more than the measurement.

### 1.1 The transfer error

`[NEO-AI-P-007 s2]` names the error this section is describing and it is worth stating in its own terms. A model's measured capability is transferred to a product built on that model by adjacency, without any claim being made explicitly. The product inherits an adjective. The inheritance is not argued and therefore cannot be rebutted `[E]`.

The transfer runs in the other direction too, and that error is less discussed and more damaging to a company in NEO's position. If a system's value is assumed to be its model's value, then a better model available to everyone appears to erase the system's advantage. Both directions rest on the same mistake, which is treating the system as a wrapper over the component rather than as the thing that turns a component into a completed unit of work.

---

## 2. What the established work supports

Four lines of published work bear on the argument. Each is cited for what it established and not for more.

**Decomposition changes what is reachable.** Chain-of-thought prompting established that eliciting intermediate steps improves performance on multi-step reasoning tasks relative to direct answering `[E]` (Wei et al., 2022). The finding is about elicitation within a single model call and it is cited here only for the direction of the effect, not for any magnitude and not as evidence about NEO.

**Interleaving reasoning with actions is a workable control pattern.** ReAct established that alternating between reasoning steps and environment actions produces better task completion than either alone on the tasks studied `[E]` (Yao et al., 2023). Again cited for the pattern, not for the numbers.

**Retrieval changes what a system can be right about.** Retrieval-augmented generation established that grounding generation in retrieved documents reduces unsupported assertion on knowledge-intensive tasks `[E]` (Lewis et al., 2020). What it did not establish, and what matters here, is whether the retrieved document is itself reliable, which is a separate problem requiring separate machinery.

**Verification is a distinct operation from generation.** Work on self-consistency and on verifier models established that checking a candidate answer is a different computation from producing one, and that the check can be performed by a different process `[E]` (Wang et al., 2023). This is the technical basis for treating verification as an architectural component rather than as a prompt instruction.

**What none of this establishes.** No published work known to the Program establishes that a specific orchestration architecture produces a specific improvement on enterprise tasks under governance constraints, because the evaluation methodology for that question is not settled and the benchmark does not exist `[O]`. Section 8 is about that gap. It is a real gap and the paper does not write around it.

---

## 3. System intelligence, defined so it can be argued with

**NEO System Intelligence** is the architectural layer above models, agents, tools, memory, knowledge, evidence and evaluation. It is not a model, it is not a router, and it is not a synonym for the platform. It is the layer that decides what work is done, by what, under whose authority, against what evidence, and with what record `[A]` `[D] (brain, S4)`.

The name matters because a near-identical one is already in use. **NEO Intelligence** is the intelligence and investigation vertical covering open-source intelligence, blockchain intelligence, anti-money-laundering and risk intelligence, cyber intelligence and due diligence workflows `[D] (neo-intelligence, S4)`. The two are one word apart and they are different objects. This paper concerns the layer. Where a document means the vertical, it writes NEO Intelligence without System, and the distinction is never elided.

The layer is defined by eight operations. The list is not a component inventory and deliberately does not describe how any of it is built.

| Operation | The question it answers | Why a model does not answer it |
|---|---|---|
| **Decomposition** | What smaller units is this work made of, and in what order | The unit boundaries depend on the organisation's process, not on the input text |
| **Selection** | Which executor performs this unit | Requires comparing candidates the executor cannot see |
| **Tool use** | What may be invoked, with what authority, against what side effects | Permission is external to the component exercising it |
| **Retrieval** | What is brought into scope, and from where | Depends on what the organisation holds and who may read it |
| **Verification** | Is this result acceptable, judged by something that did not produce it | A component cannot be its own check without circularity |
| **Memory** | What persists, under what promotion rule, retrievable by whom | Persistence and read scope are governance decisions |
| **Evidence** | What supports this claim, and does the support resolve to distinct origins | Requires a record structure across calls |
| **Approval** | Who authorised this, and is that authorisation still valid | Authority is a property of people and roles |

Each operation is specified in the Program's architecture and none of them is running `[D] (brain, S4)`. Section 7 says exactly how much exists.

### 3.1 Why these eight and not others

Two tests were applied. An operation is in the list if removing it makes at least one of the four required properties in section 1 unobtainable, and if no improvement in the executing model supplies it. Prompt engineering fails the second test, because a better model needs less of it. Caching fails the first, because removing it costs money and latency and does not make a result unattributable.

Two candidates were considered and left out. **Planning** is not separate from decomposition at this level of description, and separating them produces two words for one operation. **Learning** is deliberately excluded, and section 6 explains why at length: it is the operation most likely to be described in a way that cannot be checked.

---

## 4. Why the effects compound

The claim in the paper's title is that orchestration compounds capability. Compounding is a specific claim and it should be argued rather than asserted `[A]`.

Take a unit of work that a single model call completes acceptably with probability `q`. Now consider the same unit performed by a system that decomposes it into steps, selects an executor per step, retrieves grounding material, verifies the result against something that did not produce it, and escalates to a person when a stated condition is met.

Three structural things happen and they are different from each other.

**Decomposition changes the exponent.** A single call must be right about everything at once. A decomposed task must be right about each part, and the parts are individually easier. This cuts both ways and honest treatment requires saying so: if five steps each succeed with probability 0.9 and all five must succeed, the product is 0.59, which is worse than a single call at 0.7. Decomposition helps when the per-step probability rises enough to beat the multiplication, and it does not always. This is the first place the argument could be wrong and section 9 treats it as a falsifier rather than as a caveat.

**Verification changes the failure mode, not the success rate.** A verifier that catches a proportion of defects does not make the generator better. It converts an undetected error into a detected one, and a detected error is recoverable: it can be retried, escalated, or reported as an inability to answer. The value is not in the arithmetic of the success rate. It is that a system which knows when it has failed can be governed, and a system which does not cannot be `[A]`.

**Selection converts variance into an advantage.** Executors differ by task, and the differences are frequently large enough to dominate every other consideration for that task `[A]`. A system that fixes one executor at procurement time is choosing a single point on a distribution and holding it. A system that selects per task can take the better point each time. This is the argument of `[NEO-AI-R-001]` and it is not restated here beyond the one sentence.

The compounding claim, stated precisely: **the operations are not independent contributions to one number. Each changes the conditions under which the others operate.** Retrieval improves what verification is checking against. Verification makes escalation meaningful, because there is something to escalate on. Memory makes selection better informed over time. Evidence makes approval a decision rather than a formality. That interaction structure is why the system is not the sum of its parts, and it is also why the system is hard to evaluate, which is section 8.

### 4.1 What compounding does not mean

It does not mean the result is better than the best available model on a model benchmark. That comparison is not defined, because a model benchmark measures a model and this measures a system doing a task the benchmark does not contain.

It does not mean more components is better. Each operation adds latency, cost and a failure surface. A system with eight operations where two would do is worse than the two, and the fact that the eight are individually justified does not make the eight justified together.

It does not mean the effect has been measured. It has not `[O]`.

---

## 5. Provider replaceability, stated honestly

The most common claim made for multi-model architecture is that it removes vendor lock-in. **That claim is false and repeating it damages the argument it is meant to support** `[A]`. `[NEO-AI-R-001 s4.4]` establishes the point and this paper follows it rather than softening it.

What a multi-model architecture provides is **replaceability under a contract**: an executor can be substituted without changing what an agent is, what it may do, or what its output must look like, provided a contract defines those things independently of the executor `[A]` `[D] (brain.router, S4)`. That is a real and valuable property. It is not independence.

Two honest limits belong in the same paragraph as the claim.

**Concentration risk relocates rather than disappearing.** An organisation that depended on one provider now depends on one orchestration layer. The dependency is on something it controls rather than on something it does not, which is a materially better position, and it is a dependency.

**Substitutability has to be demonstrated rather than declared.** If an agent's behaviour changes when the executor beneath it changes, the abstraction is a label rather than a contract. The Program's answer is a substitution conformance suite that runs each agent's contract tests once per admissible executor and fails where the contract holds under one and not another `[D] (brain.validation, S4)`. That suite is specified and has not been run, because there is nothing to run it against.

This section exists because the honest version is more persuasive to the reader who matters. An enterprise architect who has been sold vendor independence before will discount a paper that sells it again.

---

## 6. Learning, and what this paper will not say about it

A system that records outcomes can, in principle, use them. This is the most commercially attractive claim available and it is the one most likely to be stated in a form nobody can check.

The Program's public position has three parts and stops there.

**First, recording and taking effect are separate acts.** A record of what happened may be written at any time. A change to what the system does as a result is a governed change: it is proposed, reviewed, recorded, reversible, and never in effect silently `[D] (brain.governance, S4)`. The reason is not caution for its own sake. A system whose behaviour changes without a governed act cannot be audited afterwards, because the auditor cannot establish which behaviour was in force at the time of the decision under review.

**Second, an outcome is not a label.** For most enterprise work the ground truth arrives late, arrives partially, or does not arrive. A risk assessment that recommended proceeding and was followed by no loss is not thereby correct. Treating it as a positive label trains a system on survivorship `[A]` `[O]`.

**Third, the mechanism is not published.** How the Program proposes to convert recorded outcomes into changed behaviour is not described here, in any form, at any level of detail. This is a deliberate withholding and it is stated rather than concealed. `[NEO-AI-P-007]` requires that the corpus distinguish what is unknown from what is not disclosed, and this is the second of those.

A reader is entitled to discount the paper accordingly, and should. An undisclosed mechanism is not evidence.

---

## 7. What exists, stated plainly

`[NEO-AI-P-007 s3]` sets the standard this section obeys: every capability reference resolves to a key in the public register and carries its status, and a capability at S4 or S5 is not described in the present tense as though deployed.

At the date of this paper, of the capabilities named in its front matter: **none is operational, none is in pilot, none is undergoing validation. Fifteen are at S4, designed and specified. Two are at S5, planned or exploratory** `[D]`. The register's S1-S5 classifications are Founder-ratified as the approved public representation of maturity. That register-level ratification does not promote any individual capability to lifecycle status RATIFIED and does not imply deployment beyond the S-status shown.

The eight operations in section 3 are specified in architecture and specification documents. None of them is running. No mission has been executed. No evaluation has been performed. The evaluation harness that would perform one is at S5 `[D] (assurance.eval-harness, S5)`.

This paper is therefore an argument about how such a system should be built and why the layer is where the value sits. It is not a description of a system that exists, and no sentence in it should be quoted as evidence that NEO AI performs any operation described here.

The current status of every capability is published and updated at the public Capability Register. A reader checking this paper against the ledger later will find the statuses have moved, or will find that they have not, and either finding is the point of publishing it.

---

## 8. Measuring a system rather than a model

If the argument is right, the measurement has to move with it, and the measurement is the hardest unsolved part `[O]`.

Four difficulties, each real.

**The unit of measurement is a mission, not a prompt.** A mission has an objective, a permitted action set, an authority context and a required record. Scoring it requires a rubric covering correctness, attribution, boundary conformance and record completeness, and the last three have no established scoring convention.

**The denominator is contested.** Compared against what. A single strong model given the same brief and no tools is one baseline and a weak one, because it is not permitted to retrieve. A human analyst is a better baseline and is expensive, slow and variable. There is no settled answer and the Program does not have one.

**Governance constraints change the achievable score.** A system that refuses to proceed without an approval will score worse on completion than one that proceeds, and be correct to do so. A benchmark that does not model the cost of an unauthorised action rewards the ungoverned system.

**Disturbance matters more than the clean run.** The interesting question is not how a system performs when everything works. It is what happens when a provider degrades, a source turns out to be circular, a tool fails halfway, or an approval is invalidated after the work depending on it has started. Measuring that requires deliberately injecting the disturbance, which is a methodology rather than a benchmark.

The Program has specified a methodology addressing these and **has not run it** `[D] (assurance.eval-harness, S5)`. When a result exists it will be published with its configuration, or it will not be published. `LOCK_v2` makes that binding: a benchmark attributed to NEO AI without a reproducible configuration must never appear.

Until then, the honest statement of the thesis is the one this paper opens with. NEO is designed to produce stronger system-level outcomes than an individual model used in isolation **where orchestration, tools, memory, evidence, verification and governance provide measurable benefit**. The conditional is not hedging. It is the claim.

---

## 9. Why a better model raises the value of the layer, and how that could be wrong

This is the argument the paper exists to make.

A stronger foundation model raises the ceiling on what a single call can achieve. It does not, and by construction cannot, supply attribution, authority, boundedness or the record, because none of those is a property of a text-to-text function `[A]`. So model improvement moves one term and leaves the others where they were.

The consequence is counter-intuitive and is the thesis. **As models improve, the unsolved parts become a larger fraction of the remaining problem.** When a model completes 40 per cent of the reasoning an organisation needs, the reasoning gap dominates and governance looks like overhead. When it completes 90 per cent, what stands between the organisation and a usable result is almost entirely the four properties in section 1. The layer's relative importance rises with the model's absolute capability.

There is a second effect and it points the same way. A more capable model is entrusted with longer chains of consequential action, and the cost of an unattributable or unauthorised action rises with the length of the chain `[A]`. Capability and required governance move together.

### 9.1 How a stronger model actually enters the system

The argument above is abstract and the Founder determination that authorised this paper asked for
the concrete path, so it is stated. A new foundation model does not become available to work by
being announced. It enters through a sequence, and every stage is a place it can stop
`[D] (brain.router, S4)`.

| Stage | What it establishes |
|---|---|
| **Qualification** | That the model exists in a form the platform can address at all: an adapter, a stable interface, terms permitting the intended use, a deployment boundary the organisation's obligations allow |
| **Evaluation** | How it performs on the task classes the platform actually runs, measured as a system rather than inherited from a published model benchmark |
| **Security assessment** | What it does under adversarial input, what it discloses, what it will execute, and what its provider retains |
| **Capability mapping** | Which capability classes it is a candidate for, expressed in capability terms rather than as a name |
| **Admissibility** | Which policy conditions it satisfies: data class, jurisdiction, residency, sub-processor status, tool permission, evidence obligation. **This is a filter and it is evaluated before anything is scored** |
| **Routing eligibility** | Whether it enters the candidate set for a task class, and under what constraint |

Two things follow that matter more than the sequence itself.

**Absorption is a governed act, not an upgrade.** A model becoming eligible changes what the
platform will do, which makes it a change to production behaviour and therefore something that is
proposed, recorded and reversible rather than something that happens because a provider shipped.

**A model can pass evaluation and fail admissibility, and that outcome is correct.** A model that
is better on every quality measure and cannot satisfy a residency obligation is not a better
choice. It is not a choice. This is the ordering of section 3 applied to the absorption path, and
it is the reason the path exists as a sequence rather than as a score.

What this paper does not publish, and will not: the evaluation results, the datasets and scenarios,
the security assessment findings, the capability mapping for any named model, the admissibility
predicates, any threshold at any stage, and any weight used in scoring within the candidate set.
The pipeline is the mechanism. Its settings are the work.

### 9.2 What would falsify this

The paper is worth publishing only if it can be wrong. Five conditions, each of which the Program would treat as falsifying rather than as a setback. A serious research paper states the conditions under which it is wrong, and these are the five.

1. **A frontier model absorbs the operations.** If a single model, given a task, reliably decomposes it, selects and invokes tools under externally enforced permission, retrieves and grades evidence by distinct origin, verifies its own output through a mechanism that is not itself, and emits a record an auditor accepts, then the layer is a temporary artefact of current model limitations. This is the strongest falsifier and it is not fanciful.
2. **The record turns out not to be required.** If enterprises and regulators accept ungoverned agentic output at scale, the governance argument loses its buyer regardless of whether it is correct.
3. **Decomposition loses.** If per-step reliability does not rise enough to beat the multiplication in section 4, decomposed systems will underperform single strong calls on real work.
4. **The orchestration layer commoditises.** If routing, tool contracts and evidence structures converge on an open standard implemented by every platform, the layer stops being an asset and becomes infrastructure.
5. **Measurement never arrives.** If no reproducible system-level methodology emerges, the thesis stays unfalsifiable, and an unfalsifiable thesis should not be believed, including by the Program that wrote it.

Condition 1 is the one to watch and the Program watches it deliberately. Progress against it is progress against this paper.

The thesis restated so it can be quoted accurately: **NEO does not depend on possessing the strongest individual foundation model, and is designed so that improvements in foundation models compound the capability of the system rather than commoditise it.** Whether that design holds is what section 9.1's absorption path and section 8's unbuilt measurement exist to determine.

---

## 10. Conclusion

The measurement is taken at the model because that is where the boundary is clean. The value, for an organisation, sits at a boundary that is harder to measure: a completed unit of work that is attributable, authorised, bounded and recorded.

The operations that produce those properties are compositional, they interact, and none of them is supplied by a better model. That is why they compound, and it is why model improvement raises rather than lowers the value of the layer above.

None of it is running. The argument is published now, before there is anything to demonstrate, so that the claim is on the record ahead of the result rather than assembled after it.

---

## Scope and Limitations

This paper argues an architectural position. It does not describe a deployed system, and every capability it names is at S4 or S5 in a register that is itself PROVISIONAL.

It reports **no measurement, no benchmark result, no evaluation, and no comparison against any other system, model or vendor**. No such comparison exists and its absence is recorded as an open problem rather than left implicit `[O]`.

It names no model provider, and it makes no claim about the relative quality of any named model. The permitted comparative thesis is system-level and conditional, and it is stated as such in section 8.

It does not disclose: any routing threshold, any scoring weight or objective function, any admissibility predicate, any measured per-executor performance figure, any evaluation dataset or scenario, any prompt or policy, any memory or event schema, or any mechanism by which recorded outcomes are converted into changed behaviour. Several of these exist internally. Their absence here is a classification decision, stated in section 6 rather than concealed.

It would be falsified by any of the five conditions in section 9.2. Condition 1 is the one the Program considers most likely.

---

## Related Research

- `[NEO-AI-R-001]` The End of the Single-Model Enterprise. This paper extends its argument from selection to the full operation set, and follows its position on vendor lock-in without softening it.
- `[NEO-AI-R-003]` Mission Control: A Governance Architecture for Autonomous Work. Supplies the authority and record half of section 1.
- `[NEO-AI-R-005]` Evidence, Memory and Accountability in Agentic Systems. Supplies the memory and evidence operations of section 3.
- `[NEO-AI-R-007]` Multi-Model Architecture: Resilience Beyond Provider Dependence. Registered, not yet drafted. It will own section 5 in full.

## Related Publications

- `[NEO-AI-P-001]` Introducing NEO AI: Intelligence Orchestrated.
- `[NEO-AI-P-007]` A Note on Responsible AI Capability Claims. Governs sections 1.1, 7 and 8 of this paper.

## Related Technical Notes

- `[NEO-AI-TN-001]` Bounding the Autonomy Budget.
- `[NEO-AI-TN-002]` Detecting Circular Corroboration in an Evidence Chain. Section 3's evidence operation depends on it.
- `[NEO-AI-TN-003]` What Belongs in a Mission Event. Section 1's record property depends on it.

## Related Architecture

None in this wave. The architecture documents supporting this paper are classified CONFIDENTIAL TECHNICAL ARCHITECTURE and are not published.

## Related Engineering

None in this wave. The evaluation methodology referenced in section 8 is classified CONFIDENTIAL TECHNICAL ARCHITECTURE and is not published.

## Related Figures

None in Wave 1. A figure for the eight operations of section 3 is specified and not drawn.

## Related Terms

`Mission` . `Mission State` . `Mission Envelope` . `Task Graph` . `Router` . `Evidence Layer` . `Evidence Chain` . `Evidence Ledger` . `Validation Layer` . `Capability Register` . `Capability Status` . `Human Authority` . `Decision Record` . `Claim Class` . `Admissible Set` . `Bounded Autonomy` . `Graceful Substitution` . `Circular Corroboration` . `NEO System Intelligence` (pending the vocabulary amendment at `PUB-ACT-04`)

## Evidence Table

| # | Claim | Class | Source | Capability |
|---|---|---|---|---|
| 1 | Eliciting intermediate steps improves multi-step reasoning relative to direct answering | `[E]` | Wei et al., 2022 | |
| 2 | Interleaving reasoning with environment actions is a workable control pattern | `[E]` | Yao et al., 2023 | |
| 3 | Grounding generation in retrieved documents reduces unsupported assertion on knowledge-intensive tasks | `[E]` | Lewis et al., 2020 | |
| 4 | Checking a candidate answer is a distinct computation from producing one | `[E]` | Wang et al., 2023 | |
| 5 | The four required properties of an enterprise result are not model output properties | `[A]` | | |
| 6 | The eight operations interact rather than contributing independently | `[A]` | | |
| 7 | Multi-model architecture provides replaceability under contract and not independence | `[A]` | `[NEO-AI-R-001 s4.4]` | `brain.router` S4 |
| 8 | Model improvement raises the relative importance of the layer above | `[A]` | | |
| 9 | The eight operations are specified and none is running | `[D]` | | `brain` S4 |
| 10 | A substitution conformance suite is specified and has not been run | `[D]` | | `brain.validation` S4 |
| 11 | A system-level evaluation methodology is specified and has not been run | `[D]` | | `assurance.eval-harness` S5 |
| 12 | No published work establishes that a specific orchestration architecture produces a specific improvement on governed enterprise tasks | `[O]` | | |
| 13 | Late, partial and absent ground truth makes outcome labelling unreliable for most enterprise work | `[O]` | | |
| 14 | No reproducible comparison against any other system exists | `[O]` | | |

## References

Lewis, P. et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. Advances in Neural Information Processing Systems 33. Accessed 2026-08-12.

Wang, X. et al. (2023). Self-Consistency Improves Chain of Thought Reasoning in Language Models. International Conference on Learning Representations. Accessed 2026-08-12.

Wei, J. et al. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. Advances in Neural Information Processing Systems 35. Accessed 2026-08-12.

Yao, S. et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. International Conference on Learning Representations. Accessed 2026-08-12.

**Verification note.** Each reference above must be verified against the published version, and its accessed date corrected, before this paper leaves DRAFT. `NEO-AI-STD-003` requires an external primary source for every `[E]` claim, and a citation carried forward from another document without verification does not satisfy it.

## Version History

| Version | Date | Status | Change |
|---|---|---|---|
| v1.0 | 2026-08-12 | DRAFT | First issue. Written for the public research release to supply the missing centre of the public corpus: the argument that intelligence is a property of the system rather than of the model, and that model improvement raises rather than lowers the value of the layer above. Discloses no routing parameter, no evaluation dataset, no learning mechanism and no measured result. Identifier requested and not allocated. |

## How to Cite

Mosse, M. (2026). *From Model Intelligence to System Intelligence: How Orchestration Compounds Capability*. NEO AI Research Program, v1.0. Cite by title and version until an identifier is allocated at `PUB-ACT-02`.
