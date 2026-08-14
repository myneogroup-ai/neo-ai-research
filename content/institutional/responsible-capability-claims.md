# NEO-AI-P-007 - A Note on Responsible AI Capability Claims

**Precision is part of product quality. This note sets the standard the rest of the corpus is written under, and applies it to the Program that wrote it.**

| Field | Value |
|---|---|
| Identifier | NEO-AI-P-007 |
| Title | A Note on Responsible AI Capability Claims |
| Family | PUBLICATION |
| Type | Institutional Publication (`P`) |
| Version | v1.0 |
| Status | DRAFT |
| Date | 2026-08-09 |
| Author | Mickael Mosse |
| Capability keys | `brain` (S4), `lili` (S4), `mission-control` (S4), `brain.task-graph` (S4), `brain.validation` (S4), `brain.governance` (S4), `brain.knowledge-graph` (S4), `brain.event-bus` (S4). Section 4.1 names `brain.router` (S4) inside a worked illustration of a claim-class defect and does not assert it, `brain.evidence-ledger` (S4), `mission.envelope` (S4), `neo-intelligence` (S4) |
| Claim-class counts | `[E]` 7 . `[A]` 38 . `[D]` 14 . `[O]` 17 . Counted by script, excluding this row and the four class names introduced in section 4. The A-to-E ratio is high; section 4.1 explains why that is a weakness |
| Figures | None in Wave 1 |
| Reading time | 23 min |
| Canonical URL | `https://neoai.myneogroup.com/publications/neo-ai-p-007` (placeholder, not yet resolvable) |

Founder's Annotations are attributed editorial annotations prepared for and approved by Mickael Mosse. They are not historical quotations and carry no claim class.

---

## 1. The position

Artificial intelligence is sold in an environment of compressed timelines, and the compression shows in the language before it shows anywhere else. A model's published result becomes a statement about a product. A rehearsed demonstration becomes a description of autonomous capability. An architecture that exists as a document is written in the present tense, and the tense does the work that evidence has not yet done.

The NEO AI Research Program holds that this is a defect in the product rather than a matter of tone. `[A]` A public claim is an interface. It sets what a buyer expects, what an integrator builds against, what a regulator will later measure the system by, and what an engineer inside the company believes has already been solved. A wrong claim corrupts all four, and the last is the one nobody plans for: teams stop building the thing the marketing said was finished.

This note sets the standard governing how the platform is described across every surface the Program controls. The standard is a set of mechanisms rather than a set of intentions, because intentions do not survive a quarter in which a competitor has announced something. Section 11 applies it to the Program itself and records where the Program has already failed it.

## 2. The transfer error: model capability is not system capability

A benchmark result belongs to a model, a version, a configuration and an evaluation method. It belongs to the prompt template, the decoding parameters, the number of attempts allowed, the scoring function, and the contamination status of the evaluation set. Detach the number from any of those and it stops being a measurement. `[A]` The point is not novel: the established risk management framework for artificial intelligence treats measurement as context-dependent, tied to the system as deployed and to its intended use rather than to a component assessed in isolation `[E]`.

An agentic system is a different object from the model inside it. It adds prompt construction, a routing decision, a retrieval path, a memory, tools with their own failure modes, a policy layer that can refuse things, an execution path with retries and timeouts, and a validation step. Each can raise end-to-end performance and each can lower it. `[A]` A retrieval layer that returns the wrong document turns a capable model into a confidently wrong system. A validator that rejects correct output lowers task completion while raising precision. A router that avoids the strongest model on a policy constraint produces a worse answer for a good reason.

The transfer error is usually made in one of five ways, worth naming because they are rarely deliberate.

**The bare inheritance.** A company builds on a model that scores well on a public evaluation and describes its product using that score, or an adjective derived from it. No claim is made about the product explicitly. It is made by adjacency, which is harder to retract and just as effective.

**The unstated configuration.** A figure is quoted without the version, the sampling settings, the attempt budget or the scoring method. A result at one attempt and a result at eight attempts with an oracle picking the best are different quantities with the same name. `[A]`

**The component result reported as a system result.** A retrieval component is measured in isolation, achieves a high recall figure on a curated corpus, and the number appears in material describing what the platform will do for a client's own documents.

**The demonstration generalised.** A workflow succeeds on the three cases it was developed against, and the description moves from "this ran" to "the system does this", which is a claim about a distribution rather than three cases.

**The tense slip.** A component specified in a design document is described in the present indicative. The most common of the five, and the easiest to commit by accident, because the design document is written in the present tense for good editorial reasons and the sentence is copied straight out of it.

Three rules follow. Where a model result is referenced, the reference identifies the tested system and its source and is not attached to a NEO AI capability in the same sentence `[D]` (brain, S4). Where the Program reports platform performance, the evaluation concerns the actual NEO AI configuration and task, and states that configuration `[D]` (brain, S4). Comparative language implying independently validated parity or superiority is not used without a reproducible comparison, and no such comparison exists `[O]`.

The discipline has a genuine cost, conceded here rather than in the limitations. A company that will not inherit a model's benchmark competes against companies that will, in a market where buyers frequently cannot tell the difference at the point of purchase. The Program accepts that disadvantage on the argument in section 10, which is commercial and not moral. `[A]`

## 3. Capability status as an operating discipline

Five statuses. The glosses are fixed and are not paraphrased in any Program document.

| Code | Gloss |
|---|---|
| `S1` | Operational and publicly available |
| `S2` | Operational in a controlled pilot or limited deployment |
| `S3` | Implemented, undergoing validation |
| `S4` | Designed and specified |
| `S5` | Planned or exploratory |

The taxonomy is often read as hedging. It is the opposite, and the difference is mechanical. A hedge is a softening word applied to a sentence: "aims to", "is positioned to", "can help you". It attaches to prose, it is unfalsifiable, and it costs nothing. A status attaches to a named component in a register, holds exactly one value at any time, changes only as an event, and can be wrong in a way somebody can point at. `[A]`

Four rules make it do work rather than decorate.

**The status attaches to the component, not the platform.** A platform-level status is meaningless, because a public interface may be live while a connector, a private deployment or an autonomous workflow is not. Every capability reference in Program prose resolves to a register key and carries that key's status token `[D]` (brain, S4). An AI management system is expected to keep documented information under control, with defined responsibilities and internal audit `[E]`. A capability register with one value per component and a change history is the Program's reading of that obligation made public rather than kept in a quality file. `[A]`

**The status governs the verb.** A design-intent claim uses "is specified to", "is designed to" or "is intended to". Present-tense operational verbs are reserved for `S1`, `S2` and, with care, `S3`. Writing "the platform routes tasks across models" for an `S4` component is the tense slip from section 2, committed against the Program's own register.

**Status may move downward.** A capability undergoing validation that fails it returns to `S4`. Downgrade is the case the discipline exists for; everybody remembers the upgrade path.

**A control reads the register.** The Capability Gate is specified to block a transition, in code promotion and publication approval alike, when a referenced status is unconfirmed or below the required level `[D]` (brain.governance, S4).

The taxonomy has a defect the Program has recorded against itself. An automated rebuild that reinjects a changed status token into an already-published document changes the badge and leaves the prose verb untouched, so a sentence written when a capability was `S2` can render an `S4` badge beside an unchanged operational verb. The check that would catch it is a verb-to-status lint that has not been built `[O]`. Until it exists, the second rule is enforced by a person reading their own text, which is the weakest kind of control there is. `[A]`

A second limit. The five bands are coarse, and the gap between `S3` and `S4` is where most of the interesting distance in a platform's life sits. A component with a working prototype and one with only a specification document are both `S4`, and a reader cannot tell them apart from the token `[O]`.

## 4. The claim classes, and the one that does not work yet

Every material statement in the Program's corpus carries one of four tags, written inline: `[E]`, `[A]`, `[D]` and `[O]`. A reader can then separate, in one pass, what is externally established from what the author inferred from it, from what the organisation intends to build, from what nobody knows.

Below, the classes are named without brackets, as E, A, D and O, so that a mechanical count of applied tags in this file is exact. The reason for that precaution is in section 11.

| Class | Means | What it requires |
|---|---|---|
| E | Established by a source external to NEO AI | A primary external source in the reference list |
| A | The author's interpretation of that material | The established claims it rests on must be identifiable nearby |
| D | NEO AI design intent | A capability key resolvable in the register, with its status token |
| O | An open problem | No capability may be asserted in the same sentence |

One class per sentence. A sentence needing two tags is two sentences. An untagged sentence is a promise that it carries no material claim, and if it does, that is a violation rather than a style preference.

Publishing this rather than applying it silently changes what a hostile reader can do. Ordinary corporate prose forces a reader to assess a document's credibility as one undifferentiated quantity. Tagged prose lets them audit it in pieces: check the established claims against the sources, argue with the interpretations on the merits, discount the design intent to the probability that the company builds what it says, and read the open problems as the honest part. `[A]` A document that survives that treatment is worth more than one that has to be taken whole.

### 4.1 The A class is not falsifiable, and the Program has recorded that against itself

An independent red team retained to argue for rejection found the weakness. It is stated here in the red team's terms rather than in a softened version.

Compare what each class must satisfy. An E claim needs an external primary source, is subject to a self-citation ratio cap and passes two automated citation checks. A D claim needs a capability key, is restricted to three permitted verbs, and passes twelve capability gate checks. An O claim may assert no capability. An A claim needs only to name the established claims it rests on, which is a referential test rather than an inferential one. There is no verb ladder for A, no capability-key requirement, and no prohibition on describing NEO AI. `[O]`

The consequence is a hole with a specific shape. The same proposition can be written two ways. As design intent: NEO AI is specified to select models by capability contract rather than by provider name, tagged D with the router key, carrying a status token, a restricted verb and twelve gate checks. As interpretation: the correct architecture for model selection is a capability contract rather than a provider name, and NEO AI is built on that principle, tagged A, asserting the same thing about the product with no status token and passing every machine-checkable gate. `[A]` In a corpus that is largely design intent, A is where design intent migrates when a writer wants it to sound established.

The recorded position is that the A class must be given a falsifiability test or be removed. The item remains open `[O]`: the test is not adopted, no inter-rater agreement has been measured, and on the mechanisable portion of its own criteria most of the class does not pass. Two partial mitigations are stated, neither is sufficient, and the Wave 1 audit found both breached: an A sentence describing a NEO AI component is required to carry the capability token in the surrounding paragraph, and the ratio of A to E is reported in the front matter so a reader can see when interpretation has outrun evidence. Ten A sentences defined registered capabilities with no token anywhere in the paragraph, and nine of twelve documents declared front-matter counts their own text falsified. Both mitigations are enforced by human reading and by nothing else `[O]`.

Publishing this is not a display of humility. It is the admission a sophisticated reader would otherwise make on the Program's behalf, in worse terms, at a worse moment. `[A]`

## 5. Demonstrations must reflect real state

A demonstration is an evidential act whether presented as one or not, because the audience will treat what they saw as something the system did. `[A]` Information integrity and the configuration of human oversight are both identified as risk areas specific to generative systems in the standards literature `[E]`, and a demonstration is where an organisation makes its first public statement about both. `[A]`

Three rules apply to anything the Program shows. A supervisory demonstration presented as live execution displays real events from the real event log, or it is not presented as live execution `[D]` (brain.event-bus, S4). Screens, timelines, counters and confidence values correspond to actual system state at the moment they are shown.

Simulated or precomputed elements are labelled where they appear, not disclosed afterwards in answer to a question. The label names what is simulated: data, timing, model output, approval, or the whole run.

A scripted demonstration is a legitimate instrument for explaining a design and is not evidence of operational autonomy `[D]` (mission-control, S4). The two uses are separated in the material rather than left to the audience.

The failure this guards against has a recognisable shape and it is rarely a lie. A team builds a demonstration environment with fixtures, because fixtures make a demonstration reliable. Everybody in the room knows which parts are real. Then the recording circulates without the room. `[A]` Six months later a prospect asks why the deployed system cannot do the thing they saw, and nobody involved intended to mislead anyone.

Visual realism is the specific hazard and it grows with design quality. A well-designed console showing a fabricated mission is more persuasive than a plain one showing a real mission, so investment in the interface increases the obligation on the fixtures. `[A]`

## 6. Confidence is not certainty

A confidence value without a stated reference set and a stated calibration is decoration. `[A]` It communicates the precision of a measurement that was never made.

Three separate problems sit under the word.

The first is that a model's self-reported confidence is a statement about its own output distribution and not a measurement of whether the output is correct. Nothing in the training objective makes it one. Using it as a permission threshold couples the decision to act to a number produced by the component that wants to act, and it fails in the case that matters, which is the confidently wrong action. `[A]`

The second is that "confidence" names at least four quantities in a system of this kind: the quality grade of a source, the probability that two records refer to the same entity, the degree of agreement among validators, and an estimate that a task met its criteria. Different units, different failure modes, different consumers. Averaging them, or displaying them as one number, produces a figure that means nothing and looks like it means something. The Program's rule is that every confidence value carries a scale identifier and that values on different scales are never combined or compared `[D]` (brain.validation, S4).

The third is calibration. A number is calibrated when, across a reference set, the events assigned 0.7 occur about seventy per cent of the time. The Program holds no such reference set for any of the four quantities and therefore publishes no calibrated confidence figures `[O]`. Building those reference sets is the work, it is domain-specific, and it is unstarted.

Where evidence conflicts, the conflict stays visible. The Knowledge Graph is specified to hold disputed edges as disputed rather than resolving them into one value at write time `[D]` (brain.knowledge-graph, S4). Converting a disagreement into a clean number destroys the one thing the reader needed.

## 7. Anthropomorphic overstatement, and the specific case of LILI

An agent can plan, call a tool, hold state across steps and revise a plan when a step fails. Those are real capabilities and should be described plainly. They do not establish understanding, judgment, intention or professional competence, and the vocabulary describing them should not borrow from the vocabulary describing people doing those things. `[A]`

Agentic threat-modelling work treats an agent as a principal with excessive potential agency rather than an actor with judgment, and reasons about tool misuse, delegation and the boundary at which untrusted content enters `[E]`. That framing is the right one for public description as well as for security. `[A]` The Program's practical rule is provenance in the output rather than adjectives in the marketing: the platform is specified to indicate, for each material element of a result, whether it was generated by a model, computed by a deterministic tool, retrieved from a named source, or approved by a person `[D]` (mission-control, S4). A reader who can see that does not need to be told what the system is.

LILI is where the Program's own practice is most exposed, so it is stated rather than avoided. LILI is a conversational interface at `S4`, designed and specified `[D]` (lili, S4). The interface has a name and a voice, and product material uses a feminine pronoun in a small number of places. That is a voice convention retained from established product language, and it is constrained: the pronoun appears only in sentences that also constrain the system, never in technical documents, never in figure labels or alt text, and never in a sentence attributing a mental state, a judgment, a belief, a preference or a professional opinion. She should not hide a material fact or state a conclusion more firmly than its evidence supports, and sentences of that shape are the only ones in which the pronoun is permitted at all.

LILI is given no age, no biography, no nationality and no physical description, and is not described as an assistant with feelings, a colleague, an employee or an expert. Any sentence in which the pronoun does work that "the interface" could not do is a sentence the Program rewrites. `[A]`

Whether a named, voiced interface can carry that constraint at scale, once it is used daily by people who did not read this note, is uncertain. The Program's view is that the constraint holds because the interface repeatedly discloses the provenance of what it says, and that view is untested `[O]`.

## 8. The professional and regulatory perimeter, expressed as product design

NEO AI is being built as technology and workflow infrastructure. In high-impact domains its output is intended to support qualified professionals and authorised institutions, and it is not a substitute for licensing, fiduciary responsibility, clinical judgment, legal advice or regulatory decision-making.

The sentence above is a disclaimer, and disclaimers do not work. They are read once, by the wrong person, at the wrong time, and they have no effect on what the system permits at four in the afternoon on a deadline. `[A]` A perimeter that exists only in prose is a perimeter the product does not have.

The perimeter belongs in the permission model instead. Four mechanisms, all specified and none deployed. Actions crossing a professional boundary are declared at plan time and carry a blocking approval gate bound to a role holding the relevant standing, so the approval is not satisfiable by whoever happens to be available `[D]` (brain.governance, S4). The autonomy level for such a node is derived from reversibility and consequence rather than any confidence value, and it is capped `[D]` (brain.task-graph, S4). An output intended for regulated use carries its provenance and validation record, so the professional who signs it can see what they are signing `[D]` (brain.validation, S4). The mission envelope cannot be expanded into a regulated action by the system itself, only by a recorded act of human authority with an actor, a scope, a justification and an expiry `[D]` (mission-control, S4).

Professional standing is an attribute the platform reads from an identity provider it does not control, and a system that gates on a role attribute is only as good as the register issuing it `[O]`. Standards guidance on AI management systems requires documented roles and decision rights `[E]`, and the Program's reading is that the obligation extends to the correctness of the role source, which the corpus does not currently address `[A]`.

## 9. Corrections and negative results

An organisation that publishes only its successes has published nothing checkable, because the sample is selected. `[A]` A correction record makes the rest of the record credible by demonstrating that the process which produced it can fail and be seen to fail. Four commitments, all mechanical.

Every substantive publication carries a Scope and Limitations section naming what it does not cover and what would falsify it. A publication that nothing could falsify is a position statement rather than a finding, and is labelled accordingly.

Material corrections are dated and preserved in version history, with the wrong claim struck through and the correction recorded beside it. The identifier is never reissued. Removing an incorrect claim silently protects the appearance of the record while destroying its function. `[A]`

Superseded material stays resolvable and is marked superseded, so a reader arriving from an old link learns that the position changed rather than reading a document that no longer holds. A retired identifier resolves to a page naming its successors and never returns a not-found response.

Negative results are published. Where an approach was tried and did not work, or a measurement came out unfavourably, the record says so. The Program has few such results because it has performed few measurements, and that absence is reported rather than allowed to read as a clean sheet `[O]`.

Structured documentation artefacts that state provenance, intended use and known limitations are a recognised transparency mechanism in the dataset documentation literature rather than an editorial nicety `[E]`. Applying that idea to capability status and to corrections is the Program's extension of it, not something the source prescribes. `[A]`

## 10. Why precision is commercially valuable

The argument that precision is ethical is true and does not survive contact with a sales-driven organisation, because it competes with a quarter. The argument that survives is that imprecision is expensive, and that the expense is deferred, concentrated, and paid at the worst moments. `[A]`

**Sophisticated buyers test the gap.** Enterprise procurement for a system of this scope involves a security questionnaire, an architecture review, a data protection assessment, a reference call and usually a proof of concept against the buyer's own material. Each measures the distance between what was claimed and what is there. A vendor whose public material was precise arrives with expectations already calibrated. One whose material was not spends the proof of concept explaining, and the explanation is heard as a retreat however reasonable it is. `[A]`

**The cost is concentrated in the deals worth having.** Small buyers rarely test. The large, regulated, long-contract buyers who make a platform of this kind viable test thoroughly, and they compare notes. `[A]` Imprecision filters the customer base in the wrong direction, silently, because a buyer who discounts a vendor's claims does not explain why.

**Credibility compounds and it is asymmetric.** Accurate statements accumulate into a reputation for accuracy, which lowers the cost of every subsequent claim because the next one is believed without verification. One demonstrated overstatement resets that balance and imposes verification on everything, including the statements that were true. `[A]` The upside accrues in small increments over years. The downside arrives whole.

**Regulators and technical partners read differently from customers.** A regulator reads for the gap between the stated control and the implemented control, and a documented `S4` is a defensible position while an operational verb over the same component is a misstatement. Guidance on integrating AI risk into an organisation's existing risk management expects the treatment to be traceable to the system's actual lifecycle stage `[E]`. A technical partner reads for what they can build against, and a claim they build against and find absent costs them a release cycle. `[A]`

**Imprecision constrains the architecture, the cost least often anticipated.** A capability described publicly in the present tense becomes a commitment that outlives the design decision producing it. Teams build toward the description rather than the better design that emerged since, because changing the description is now an external event. Precise status language keeps the architecture free to change, worth more in a platform's first years than any single claim. `[A]`

**Internally, the register is a management instrument.** It tells a leadership team what is real, in one table, without asking anybody. An organisation that overstates externally eventually overstates internally, because the external language becomes the internal shorthand, and then nobody can answer the simplest question about their own product. `[A]` That failure is slow and it is not recoverable in a quarter.

The Program does not need to understate its thesis to be precise about its state. The thesis appears at full strength in `NEO-AI-P-001`: an intelligence operating layer built around model orchestration, governed agents, memory, evidence and human authority. Section 8 of that publication then states, for each of twenty components, where the thesis currently stands. Ambition and accuracy are separable, and keeping them separable is the whole technique. `[A]`

## 11. Applying the standard to the Program itself

A standard applied only to other people is a rule, not a discipline. What follows is where the Program has failed its own standard, using its own findings, before anyone else uses them.

**The epistemic system was not applied to the Program's own documents.** The Program's central claim to defensibility is that every claim in its corpus carries a declared evidence class. An independent red team counted applied tags across seven of the Program's own standards. Five contained none at all. `[O]`

**Two documents declared claim-class counts in their front matter that their own text falsified.** One declared eighty-two design-intent tags and contained twenty-two occurrences of the token, including occurrences that merely named the class. A second declared fifty-eight and contained fifteen. The overstatement was roughly fourfold on the class governing what the organisation says about a product that does not yet exist. `[O]` No gate checked the count. A hostile reader with a text editor could falsify the Program's central claim about itself in under a minute.

That finding is why the front matter of this document states how its counts were produced, and why they were produced by a script rather than typed. The fix is small. The failure was not: a false statement of fact, in the front matter of a normative standard, in the one mechanism the Program's charter identifies as the thing a competitor cannot copy. `[A]`

**The A class has no falsifiability test.** Recorded in section 4.1. It remains open. `[O]`

**No citation in the corpus has been verified.** Every reference in every Program publication, including those at the foot of this one, is marked UNVERIFIED pending a verification ledger that has not been populated. `[O]`

**No capability status has been confirmed.** The register is PROVISIONAL and awaits Founder confirmation. Nothing in it has been audited by anyone outside the Program. `[O]`

**No technical claim in the corpus has been checked for correctness by an external reviewer.** The architecture has been reviewed adversarially from inside, which is useful and is not independent. The Program's own assurance report says so in those terms. `[A]`

**A verb-to-status lint is described as an enforced check and does not exist.** Four checks in the Program's gate documentation are advisory or unbuilt while being written about in the language of enforcement. `[O]` Either they are built or the standards stop describing themselves as enforced.

Two observations follow. Eighty-eight distinct defects were found across two review rounds with the discovery rate not yet falling, so a third round would find more, and the absence of a finding is not evidence of correctness. `[A]` And publishing this list costs the Program something real with readers who will take it for disarray; the Program judges that this is not the reader it is trying to reach. `[A]`

## 12. What this note does not claim

It does not claim that the Program has achieved the standard it sets. Section 11 is the evidence that it has not.

It does not claim that the taxonomy or the claim classes are correct in design. Both are the Program's own constructions, neither derives from an external standard, and sections 3 and 4.1 each name a defect.

It does not claim that precise language is sufficient for trustworthiness. Precise language about an untrustworthy system is a precise description of an untrustworthy system.

It does not claim that any competitor overstates. Nothing here characterises another company's material. The failure modes in section 2 are described because they are easy to commit, including by the Program.

## 13. How this position can be tested, and what would change it

The standard is observable. A reader can take any Program publication and check three things mechanically: that every capability mentioned resolves to a register key and carries a status token, that the declared claim-class counts match the file, and that no sentence describing an `S4` or `S5` component uses an operational verb. Failures are defects and should be reported as such.

The correction record is the second test. If material corrections appear, dated, with the superseded text still resolvable, the process is real. If the record stays clean over a long period during which the platform changed substantially, the record is being managed rather than kept. `[A]`

One argument would change the position, and it is not a weak one. If precise status language demonstrably prevents an organisation from reaching the buyers who would have benefited, because the market at this stage selects on confidence rather than accuracy, then the discipline carries a cost the Program has not measured and may be paying blindly `[O]`. There is no data on the commercial effect of the Program's own precision in either direction, and saying so is preferable to assuming the flattering answer.

---

**FOUNDER'S ANNOTATION | MICKAEL MOSSE**

I want NEO AI judged by what it can demonstrate, not by adjectives. The ambition can be very large while the description stays exact about what is live, what is being validated and what is still a drawing, and I have never found a case where holding both cost me anything I wanted to keep. Precision protects the company. What matters more to me is that it is the only way to earn the kind of trust that survives a bad quarter.

---

## Scope and Limitations

This note states an editorial and product-communication standard. It reports no operational data, no benchmark, no measurement and no external evaluation. It contains no financial information, no terms of any financing instrument, no valuation, no client name and no reference to any listed vehicle.

Not covered: the citation format and verification ledger; the publication lifecycle and its gates; the figure standard; the mission-level evaluation methodology, reserved and unwritten; and the security review process. Each is held elsewhere in the corpus.

The capability status taxonomy and the claim-class system are the Program's own constructions. Neither ISO/IEC 42001, ISO/IEC 23894, NIST AI 100-1, NIST AI 600-1 nor the dataset documentation literature prescribes or endorses them. Where this note cites them it cites them for an obligation or a recognised risk, never for a mechanism.

This note would be falsified by a demonstration that status-qualified public claims produce worse outcomes for buyers, regulators or partners than unqualified ones on the dimensions section 10 asserts, or by a workable falsifiability test for the A class that the Program has failed to find.

## Related Research

- `NEO-AI-R-001` The End of the Single-Model Enterprise (DRAFT) - the model and system distinction in section 2.
- `NEO-AI-R-002` From AI Assistants to Governed Agent Systems (DRAFT) - the autonomy taxonomy behind section 8.
- `NEO-AI-R-003` Mission Control: A Governance Architecture for Autonomous Work (DRAFT) - the approval mechanisms in section 8.
- `NEO-AI-R-005` Evidence, Memory and Accountability in Agentic Systems (DRAFT) - the conflict handling in section 6.

## Related Publications

- `NEO-AI-P-001` Introducing NEO AI: Intelligence Orchestrated (DRAFT) - the publication whose section 8 applies this standard.
- `NEO-AI-P-008` Research, Governance and the NEO AI Public Record (DRAFT) - the correction and supersession mechanisms in section 9.
- `NEO-AI-P-006` NEO Intelligence (DRAFT) - retitled under this standard after an earlier title asserted a launch that had not occurred.
- `NEO-AI-P-003` LILI: A New Interface for Complex Work (DRAFT) - the pronoun constraint in section 7. Also `NEO-AI-P-002` and `NEO-AI-P-005` (both DRAFT).

## Related Technical Notes

- `NEO-AI-TN-001` Bounding the Autonomy Budget (DRAFT) - autonomy derived from reversibility and consequence rather than confidence, referenced in sections 6 and 8.
- `NEO-AI-TN-002` Detecting Circular Corroboration in an Evidence Chain (DRAFT) - why counting agreeing sources is not a confidence measure.
- `NEO-AI-TN-003` What Belongs in a Mission Event (DRAFT) - the event record underlying section 5.

## Related Architecture

- `NEO-AI-ARCH-002` The Brain: Component Architecture and Contracts (DRAFT) - the components referenced by capability key throughout.
- `NEO-AI-ARCH-001` Mission Control (RESERVED) - the supervisory surface subject to section 5.
- `NEO-AI-ARCH-006` Evidence (RESERVED) - the confidence scales named in section 6.

RESERVED entries are forward references and neither is cited in support of a claim.

## Related Engineering

- `NEO-AI-ENG-008` Mission-Level Evaluation Methodology (RESERVED) - the missing methodology that makes section 2's system-level claim untestable today.
- `NEO-AI-ENG-012` Benchmark and Evaluation Harness (RESERVED).

Forward references only.

## Related Figures

None in Wave 1. This note carries no figure deliberately: a diagram of a claim discipline would be decoration, and section 5 is about not doing that.

## Related Terms

Capability Status . Capability Register . Capability Gate . Claim Class . Decision Record . Design Decision Record . Human Authority . Bounded Autonomy . Mission Envelope . Evidence Chain . Evidence Ledger . Validation Layer . Circular Corroboration . Trajectory.

## References

ISO/IEC (2023). ISO/IEC 42001:2023 Information technology - Artificial intelligence - Management system. International Organization for Standardization. Accessed 2026-08-09.

ISO/IEC (2023). ISO/IEC 23894:2023 Information technology - Artificial intelligence - Guidance on risk management. International Organization for Standardization. Accessed 2026-08-09.

National Institute of Standards and Technology (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. doi:10.6028/NIST.AI.100-1. Accessed 2026-08-09.

National Institute of Standards and Technology (2024). Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile. NIST AI 600-1. doi:10.6028/NIST.AI.600-1. Accessed 2026-08-09. REQUIRES VERIFICATION: publication year and exact title.

OWASP GenAI Security Project (2025). Multi-Agentic System Threat Modeling Guide. OWASP Foundation. https://genai.owasp.org/. Accessed 2026-08-09. REQUIRES VERIFICATION: exact title, version, publication date and stable citation form.

Pushkarna, M., Zaldivar, A. and Kjartansson, O. (2022). Data Cards: Purposeful and Transparent Dataset Documentation for Responsible AI. arXiv:2204.01075. Accessed 2026-08-09. REQUIRES VERIFICATION: venue of record and final published title.

All entries are UNVERIFIED under the Program publication standard until the verification ledger records otherwise. Section 11 treats this as an open failure against the Program's own standard, not as a footnote.

## Version History

| Version | Date | Status | Change |
|---|---|---|---|
| v1.0 | 2026-08-09 | DRAFT | Initial public draft. |