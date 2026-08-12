# The End of the Single-Model Enterprise

**Why enterprise AI is becoming a constrained routing problem**

| Field | Value |
|---|---|
| Identifier | `NEO-AI-R-001` |
| Edition | **Public derivative** of `NEO-AI-R-001 v1.1`. Reduced, not paraphrased |
| Version | v1.1-public |
| Status | DRAFT |
| Date | 2026-08-12 |
| Author | Mickael Mosse, NEO AI Research Program |
| Capability keys | `brain` S4 . `brain.router` S4 . `brain.task-graph` S4 . `brain.validation` S4 . `mission-control` S4 . `foundation-model` S5 . `deployment.cloud` S4 . `deployment.vpc` S5 . `deployment.onprem` S5 |
| Claim classes | Computed from the Evidence Table at build time |
| Reading time | 18 min |
| Canonical URL | `https://neoai.myneogroup.com/research/papers/end-of-the-single-model-enterprise/` |
| Relations | `evidences` NEO-AI-P-001 . `extends` by NEO-AI-R-009 (requested, not allocated) . `depends-on` NEO-AI-STD-001 |
| Withheld | Four sections of the source are withheld as TRADE SECRET and two as CONFIDENTIAL TECHNICAL ARCHITECTURE. Section 6 of this edition states what and why |

---

## Abstract

Enterprise AI programmes still treat provider selection as the primary architectural decision, binding workflows to one vendor's interface, safety policy and deprecation schedule. This paper reframes the decision: executor selection is a **constrained optimisation performed per task rather than per organisation**.

Policy computes an admissible set first, from data class, jurisdiction, residency, reversibility, tool permission and evidence obligation. Only inside that set does anything get scored. The ordering is the argument, and it is not a formality: a constraint expressed as a heavily weighted term in a scoring function can be outvoted, and one expressed as an admissibility filter cannot.

The paper also argues against the claim most often made in its support. A multi-model architecture does not remove vendor lock-in. It relocates concentration risk from the provider to the orchestration layer, which is a materially better position and is not independence.

**This public edition withholds the analytical machinery.** The decision structure is described; the objective function, its coefficients, the admissibility predicates, the worked example and the router error analysis are not published. The principle is publishable and its parameters are the work.

---

## 1. The model-selection fallacy

The dominant enterprise pattern is to select a foundation model and build on it. Procurement runs an evaluation, a vendor wins, and the organisation's AI capability becomes a function of that vendor's roadmap.

The pattern is not stupid. It is how enterprises buy software, it produces a single commercial relationship, one security review and one support contract, and those are real goods. It is wrong here for a reason specific to this class of component: **model quality is conditional on the task, and the procurement decision discards the conditioning variable** `[A]`.

A model that extracts obligations from a French supply agreement well is not thereby the model that writes a migration script well, and neither is necessarily the model that summarises a board pack for a reader who will act on it. An organisation that selects once has selected the average, and the average is not what any individual task receives.

Three consequences follow, and they compound.

**The organisation inherits a deprecation schedule.** Model versions are withdrawn on the provider's timetable. A workflow bound to a version is bound to that timetable, and the migration is not a version bump: behaviour changes, and behaviour is what was tested.

**The organisation inherits a safety policy.** Every provider applies its own refusal boundaries. Those boundaries are a product decision made by somebody else about what an organisation's own staff may ask, and they are not negotiable, not versioned in a way the buyer can pin, and not aligned to any particular jurisdiction's requirements.

**The organisation inherits an interface.** Prompt formats, tool-calling conventions, streaming semantics and error taxonomies differ. Code written against one becomes an implicit dependency on it, and the dependency is invisible until the day it matters.

The alternative is not to use several models because variety is good. It is to treat the choice as a decision taken per unit of work, under constraints, with the constraints binding first.

---

## 2. What the established work supports

Four lines of published work bear on the argument, and each is cited for what it established rather than for more.

**Model performance varies by task.** Multi-task benchmark work established that relative model ordering changes across task families rather than holding uniformly `[E]` (Hendrycks et al., 2021; Srivastava et al., 2023). This is the empirical foundation of the whole argument and it is not contentious.

**Routing between models is a studied problem.** Work on model routing and cascades established that selecting among candidates per query, rather than fixing one, can improve the cost-quality frontier on the tasks studied `[E]` (Chen et al., 2023). Cited for the existence and direction of the effect, not for any magnitude and not as evidence about NEO.

**Constrained decision-making is a solved formalism.** Constrained optimisation, where a feasible region is computed before an objective is maximised over it, is standard `[E]`. The contribution here is not the mathematics; it is the claim that policy belongs in the feasible region rather than in the objective.

**Abstraction over providers is an established software pattern with a known failure mode.** Portability layers over heterogeneous backends succeed at interface uniformity and routinely fail at behavioural uniformity `[E]`. Section 4.1 is about that failure mode applied here.

**What none of this establishes.** No published work known to the Program establishes that a specific routing architecture produces a specific improvement on governed enterprise tasks, because the evaluation methodology for that question is unsettled and the benchmark does not exist `[O]`.

---

## 3. The decision structure, without its parameters

This section is deliberately short. The source paper develops the decision formally. That development is withheld and section 6 says why.

What is publishable is the **shape** of the decision, and the shape is where the argument lives.

**Step one is admissibility, and it is a filter.** Before any candidate is compared to any other, policy computes the set of executors that may perform this task at all. The inputs are the properties of the task: the classes of data involved, the jurisdictions and residency obligations attaching to them, whether the action is reversible, which tools it requires, and what standard of evidence its output must carry.

**Step two is selection, and it happens only inside that set.** Candidates admitted by step one are compared on quality for this task class, latency against the interaction mode, resource cost, deployment-boundary fit, and independence from a candidate already carrying load.

**The ordering is the whole thing.** A constraint expressed as a weighted term in a scoring function is a preference: a sufficiently attractive quality or cost number outvotes it, and the trade is made silently, thousands of times a day, inside a function nobody reads. The same constraint expressed as an admissibility filter cannot be outvoted, because the candidate that violates it was never a candidate `[A]`.

That is the sentence the paper exists to defend, and it is the one an architect should take away. Security, policy, tenant isolation, residency and sub-processor constraints are admissibility filters evaluated before any scoring, never weighted terms. **There is no score at which the trade becomes available.**

---

## 4. Architectural interpretation

### 4.1 Syntactic portability is not semantic substitutability

An abstraction layer that normalises request and response formats gives **syntactic portability**: the same code can call either candidate. It does not give **semantic substitutability**: the same code calling either candidate does not thereby receive equivalent behaviour `[A]`.

The two are confused constantly and the confusion is expensive, because the first is easy and looks like the second. Candidates differ in instruction adherence, refusal boundaries, output shape stability, tool-call argument construction, handling of ambiguous input, and behaviour at the edges of a context window. None of that is normalised by an interface layer, and all of it is what a downstream component depends on.

The consequence for an agent architecture is direct. If an agent's declared contract, meaning its role, accepted inputs, permitted tools, output type, evidence obligations and refusal behaviour, varies with which admissible executor served it, then the agent is a label over several behaviours sharing a name, and the user is the person who discovers this `[A]`.

Substitutability therefore has to be **demonstrated rather than declared**. The Program's answer is a substitution conformance suite: each agent's contract tests are executed once per admissible executor, and the suite fails where the contract holds under one and not another `[D] (brain.validation, S4)`. Quality, latency and cost are expected to vary, because they are what selection is for. The contract must not.

The suite is specified and has not been run, because there is nothing to run it against.

### 4.2 Router evaluation is an obligation in its own right

A router is a component that makes a consequential decision on every unit of work, and a component of that kind is subject to the same evaluation obligations as anything else that decides.

Two properties matter and they are different. **Admissibility correctness** is whether the filter ever admits a candidate that policy forbids, and it is a safety property: one violation is a violation, and an average is not a defence. **Selection quality** is whether the choice made inside the admissible set was the better one, and it is a performance property measured in aggregate.

Conflating them produces the failure that matters: a router reported as performing well on average while occasionally admitting a candidate it should not have. The aggregate hides the violation, because a violation is rare by construction and an average is dominated by the common case `[A]`.

The evaluation of the router is therefore two evaluations with different acceptance rules, and the safety one has no tolerance band.

### 4.3 Concentration risk changes topology, it does not disappear

**The claim that a multi-model architecture removes vendor lock-in is false, and repeating it damages the argument it is meant to support** `[A]`.

What changes is the topology of the dependency. Before, the organisation depended on one provider, and that provider's outage, price change, policy change or deprecation was the organisation's problem directly. After, the organisation depends on an orchestration layer that can substitute providers. The provider dependency is genuinely reduced. A new dependency is created, on the layer.

That is a better position, for a reason worth stating precisely: the new dependency is on something the organisation controls, specifies and can change, and the old one was not. It is not independence, and calling it independence invites the first well-briefed procurement officer to point out that it is not, at which point the rest of the argument is discounted too.

The honest formulation is **provider replaceability under a contract**: an executor can be substituted without changing what an agent is, what it may do, or what its output must look like, provided the contract defines those things independently of the executor `[A]`. Everything in section 4.1 is about whether that proviso actually holds.

Two further honesties belong in the same passage. The orchestration layer becomes a single point of failure for every workflow that depends on it, and its availability requirement is therefore higher than any individual provider's. And an organisation that builds this layer has taken on the cost of maintaining it, which a single-provider organisation has not.

---

## 5. Application to the NEO AI target architecture

Reduced in this edition. The component inventory and deployment topology of the source are CONFIDENTIAL TECHNICAL ARCHITECTURE.

What is publishable: NEO AI is designed so that executor selection occurs at a single, declared decision point rather than in application code; so that every selection is attributable to a rule, a manifest, a policy or a recorded decision; and so that no component selects a model, an agent, a tool or an execution path by logic existing only in code `[D] (brain.router, S4)`.

Every capability named in this paper is at S4 or S5. **None of it is running.**

---

## 6. What this edition withholds, and why

Stated rather than left as a gap, because an unexplained absence in a research paper reads as an evasion.

| Withheld | Class | Reason |
|---|---|---|
| The admissible set, formally: the task descriptor and its predicates | TRADE SECRET | This is the routing implementation. Publishing the predicate list publishes the filter |
| The objective function, its terms, its coefficients and their derivation | TRADE SECRET | An outcome optimisation formula. It took measurement and iteration to arrive at and is copyable in full from one disclosure |
| The worked example, including candidate quality, cost and latency figures and the acceptance threshold | TRADE SECRET | Model-specific measured performance thresholds. Anonymising the candidates does not declassify their measured quality |
| Router error analysis: exploration policy, propensity logging, off-policy estimation, the router loss | TRADE SECRET | Router tuning |
| The capability contract schema | CONFIDENTIAL | An interface contract, and the mechanism substitutability depends on |
| The component inventory and deployment topology of section 5 | CONFIDENTIAL | Deployment architecture |

The governing rule is that **a principle may be published while its parameters remain withheld, and publishing the principle is never permission to publish the parameters.** The decision structure in section 3 is the principle. The four withheld sections are the parameters.

---

## 7. Failure modes and open problems

**The cost-of-defect number is political** `[O]`. What it costs the organisation when a defect reaches a client is supplied by the organisation, is rarely measured, and is frequently negotiated rather than derived. Nothing in this architecture solves that. What it buys is that the number is explicit, versioned and attached to a criticality class, so that a challenged decision locates the disagreement in a stated assumption rather than in an opaque score.

**Per-task selection multiplies the evaluation burden** `[O]`. Every admissible executor for every agent must be evaluated, and the burden grows with the product rather than the sum.

**The abstraction can rot by accretion** `[A]`. Nobody proposes to name an agent after a vendor. The failure arrives in four individually reasonable steps: a model is pinned for a task it does well, the pin is justified in a document, the document is copied, and within a year the pin is part of what people believe the agent is.

**No reproducible comparison exists** `[O]`. The Program holds no measured comparison of this architecture against a single-model baseline, or against any other system, and does not claim one. Section 2's citations establish that routing can improve a cost-quality frontier in the studied settings. They establish nothing about NEO AI.

---

## 8. Conclusion

Selecting one foundation model for an organisation answers a question the organisation does not have. The question is not which model is best. It is which executor may perform this task, under these constraints, and which of those is the better choice for it.

Framing it that way makes policy a filter rather than a preference, makes substitutability a testable property rather than a marketing claim, and makes the resulting concentration risk visible rather than absent.

It also costs more, and the paper does not pretend otherwise. The layer has to be built, evaluated and maintained, and it becomes a dependency in its own right.

---

## Scope and Limitations

This is a **public derivative** of `NEO-AI-R-001 v1.1`. It is a reduction of that document, not a rewriting of it. Four sections classified TRADE SECRET and two classified CONFIDENTIAL TECHNICAL ARCHITECTURE are withheld and are listed in section 6. No withheld section is paraphrased, summarised or reconstructed.

The paper reports **no measurement, no benchmark result and no evaluation**. It makes no comparative claim against any named model or provider, and no reproducible comparison exists.

Every capability named is at S4 or S5 in a register that is itself provisional. Nothing described here is running.

It would be falsified by a demonstration that per-task selection does not improve outcomes over a well-chosen single executor on governed enterprise work, once the cost of the orchestration layer is counted.

## Related Research

- `NEO-AI-R-009` From Model Intelligence to System Intelligence. Identifier requested at `PUB-ACT-02` and not allocated; cite by title until it lands. Extends this argument from selection to the full operation set.
- `NEO-AI-R-003` Mission Control: A Governance Architecture for Autonomous Work. Public edition. Supplies the record half.
- `NEO-AI-R-007` Multi-Model Architecture: Resilience Beyond Provider Dependence. Registered, not yet drafted.

## Related Publications

- `NEO-AI-P-001` Introducing NEO AI: Intelligence Orchestrated.
- `NEO-AI-P-007` A Note on Responsible AI Capability Claims. Governs sections 2, 5 and 7.

## Related Technical Notes

- `NEO-AI-TN-001` Bounding the Autonomy Budget.

## Related Architecture

None in this wave. The architecture documents supporting this paper are CONFIDENTIAL TECHNICAL ARCHITECTURE and are not published.

## Related Engineering

None in this wave.

## Related Figures

None in Wave 1.

## Related Terms

`Router` . `Admissible Set` . `Graceful Substitution` . `Provider Replaceability` . `Capability Register` . `Capability Status` . `Task Graph` . `Trajectory` . `Bounded Autonomy`

## Evidence Table

| # | Claim | Class | Source | Capability |
|---|---|---|---|---|
| 1 | Relative model ordering changes across task families | `[E]` | Hendrycks et al., 2021; Srivastava et al., 2023 | |
| 2 | Per-query selection among candidates can improve the cost-quality frontier | `[E]` | Chen et al., 2023 | |
| 3 | Constrained optimisation over a computed feasible region is a standard formalism | `[E]` | Boyd and Vandenberghe, 2004 | |
| 4 | Portability layers achieve interface uniformity and routinely fail at behavioural uniformity | `[E]` | Established software engineering practice | |
| 5 | Procurement-time model selection discards the conditioning variable | `[A]` | | |
| 6 | A constraint as a weighted term can be outvoted; as a filter it cannot | `[A]` | | `brain.router` S4 |
| 7 | Syntactic portability does not confer semantic substitutability | `[A]` | | |
| 8 | Admissibility correctness and selection quality are different properties with different acceptance rules | `[A]` | | |
| 9 | Multi-model architecture relocates concentration risk and does not remove it | `[A]` | | |
| 10 | A substitution conformance suite is specified and has not been run | `[D]` | | `brain.validation` S4 |
| 11 | Selection occurs at a single declared decision point | `[D]` | | `brain.router` S4 |
| 12 | The cost-of-defect number is supplied rather than measured | `[O]` | | |
| 13 | Per-task selection multiplies the evaluation burden | `[O]` | | |
| 14 | No reproducible comparison against a single-model baseline exists | `[O]` | | |

## References

Boyd, S. and Vandenberghe, L. (2004). *Convex Optimization*. Cambridge University Press. Accessed 2026-08-12.

Chen, L. et al. (2023). FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance. Accessed 2026-08-12.

Hendrycks, D. et al. (2021). Measuring Massive Multitask Language Understanding. International Conference on Learning Representations. Accessed 2026-08-12.

Srivastava, A. et al. (2023). Beyond the Imitation Game: Quantifying and Extrapolating the Capabilities of Language Models. Transactions on Machine Learning Research. Accessed 2026-08-12.

**Verification note.** Every reference is verified against the published version and its accessed date corrected before this edition leaves DRAFT.

## Version History

| Version | Date | Status | Change |
|---|---|---|---|
| v1.1-public | 2026-08-12 | DRAFT | First public derivative, on Founder determination of 2026-08-12. Withholds sections 3.2, 3.4, 3.5 and 3.6 of the source as TRADE SECRET, and 4.2 and part of 5 as CONFIDENTIAL TECHNICAL ARCHITECTURE. Section 3 replaces the withheld analytical development with a prose statement of the decision structure carrying no formula, no predicate list and no figures. Section 4.3 adopts **provider replaceability** as the public term, per `VA-PUB-001`. The withheld list is published rather than left as a gap. |
| v1.1 | 2026-08-12 | DRAFT | Source correction. `PUB-BLOCK-01`. See `PUB_10`. |
| v1.0 | 2026-08-09 | DRAFT | First full draft. |

## How to Cite

Mosse, M. (2026). *The End of the Single-Model Enterprise*, public edition. NEO AI Research Program, `NEO-AI-R-001` v1.1-public. `https://neoai.myneogroup.com/id/NEO-AI-R-001`
