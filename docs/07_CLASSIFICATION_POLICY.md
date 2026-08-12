# Classification policy

The single most important document in this repository. Everything else can be corrected;
a disclosure cannot.

## The rule, in one line

**Publish the mechanism, withhold the setting.**

A public paper may describe that the system selects an executor against an objective under
constraints. It may not publish the objective, its terms, its coefficients, the
admissibility predicates or the acceptance threshold. The distinction is not about how
interesting the material is. It is about whether the material is the thing that took
measurement and iteration to arrive at.

## Three classes

| Class | Name | May appear here |
|---|---|---|
| **A** | PUBLIC RESEARCH | Yes |
| **B** | CONFIDENTIAL TECHNICAL ARCHITECTURE | No |
| **C** | TRADE SECRET | No, and no derivative |

A class B item may become class A through a **reduction**: a principle published, a
parameter withheld. A reduction is a new artefact reviewed on its own terms. It is never
a paraphrase of a withheld passage, because a paraphrase of a withheld passage is the
withheld passage with the words changed.

A class C item produces no derivative at all.

## What never appears in this repository

Not in `main`, not in a branch, not in a commit that a later commit removes, not in a
comment, not in a test fixture, not in a commit message, not in an issue, not in CI
output pasted into an issue.

**Architecture and implementation**

- Component contracts between internal components
- Message, event or approval schemas, field by field
- Service inventories, deployment topology, partition or shard counts
- The trusted computing base and its boundaries
- Integrity chain construction and expungement design

**Mechanism settings**

- Router score vectors, scoring weights, objective functions and their coefficients
- Admissible-set task descriptors and their predicates
- Acceptance thresholds, routing thresholds, autonomy thresholds by value
- Cost model specification and its parameters
- Exploration policy, propensity logging, off-policy estimation, router loss

**Evaluation**

- Evaluation denominators and gate rules
- Benchmark datasets, in whole or in sample
- Measured per-executor performance figures
- Any result without a published reproducible configuration

**Programme**

- Internal programme stages and their audit trails
- The Engineering Constitution and the Data Program
- Internal registers, internal governance instrument references, internal file paths
- Internal ticket, repository or hostname references

**Commercial and personal**

- Named pilot clients, contract values, any financial figure
- Personal data of any kind
- Credentials, tokens and keys, in any form

## What is class A and is published

- The position, the argument, and the reasoning that supports it
- The claim class of every material statement
- The capability status of every capability named, resolved from the published register
- Named open problems, including ones the Program has not solved
- What is withheld, and why. **A withholding declaration is not a disclosure**, and
  publishing the list of what is withheld is part of the corpus being trustworthy
- Falsifiers: the conditions under which the Program's thesis fails

## Claims the corpus does not make

**Never state that NEO AI is more capable than any named model, product or vendor.** Not
smarter, not better, not stronger, not state of the art. The Program publishes no
benchmark, holds no reproducible comparison against any other system, and claims none. A
contribution introducing such a comparison is closed rather than revised.

**Never describe a capability as deployed unless the register says so.** Most capabilities
in this corpus are at S4, designed and specified, or S5, planned. Every page says so.

**Never expose private reasoning.** The corpus describes what a system is designed to
record and to show. It does not publish the intermediate reasoning of any model, and no
example in the corpus contains one.

**A claim may be weakened between an internal document and a public one. It is never
strengthened.**

## Derivatives inherit the floor

A reduction, a summary, a slide, a feed entry, a JSON-LD block or an `llms.txt` line
derived from a class B or C item carries that item's classification. There is no
transformation that launders a withheld setting into a publishable one. In particular, a
withheld item may never appear in a machine-readable payload, where it is easier to
extract than from prose and harder for a human to notice.

## How this is enforced

| Layer | Mechanism |
|---|---|
| Author | `CONTRIBUTING.md`, and the classification declaration in the pull request template |
| Machine | `scripts/verify_public.py`, checks `CLS-01` to `CLS-13` and `CMP-01` to `CMP-04` |
| Machine, against itself | `verify_public.py --self-test`, which asserts every check fires on a positive case and does not fire on a withholding declaration |
| Review | A code owner, and for `docs/07` and the detector itself, the security group |
| Platform | Secret scanning with push protection, and a full-history secret scan in CI |
| Release | `--strict`, in which no deferral may be outstanding |

**The machine layer is a floor, not a ceiling.** A pattern matcher catches shapes it was
told about. It does not catch a paragraph that reveals an architecture through careful
description without using any of the words in the list. That is what review is for, and
it is why `CODEOWNERS` puts a second pair of eyes on every path that could carry one.

## If something is published in error

Do not open an issue. Follow `SECURITY.md`. Withdrawal is same-day on confirmation.
Removing the page limits further exposure; it does not undo the exposure that already
happened, and the handling of that is separate from this repository.
