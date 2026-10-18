---
route: /platform/security/
title: Security-first architecture
host: neoai.myneogroup.com
source: NEO AI x100 architecture authority (2026), sections 06, 09, 21
classification: A
updated: 2026-10-18
---

# Security-first architecture

## Header

**Security is a filter, not a weight**

## Body

The design decision that matters most here is a small one and it is structural. Legal constraints, policy, authority, security, privacy, tenant isolation, residency and sub-processor constraints are evaluated as **admissibility filters before any optimisation takes place**. They are never terms in a score. `[D] (core.governance, S3)`

The order of precedence is fixed: first legal, policy and authority; then security and privacy; then quality and verification; then capability and availability; and only then latency, cost and energy. `[D] (core.routing, S2)`

The difference is the whole thing. A weighted term can be outvoted by an attractive quality or cost number, thousands of times a day, inside a function nobody reads. A filter cannot be outvoted. There is no score at which the trade becomes available, and when no compliant path exists NEO fails safely rather than routing around policy.

A change that improves quality, cost or latency is refused if it increases exfiltration risk, weakens tenant isolation, circumvents permissioning, weakens approval, increases unsafe tool execution, exposes secrets, or materially increases injection risk.

## What the architecture enforces

- **Capabilities, not credentials.** Agents receive capability tools and never credentials. `[D] (human-gates, S3)`
- **Platform gates.** Mandatory Human Gates are refused at platform level; interface enforcement is a courtesy.
- **Provenance.** Every artefact carries its lineage, verification status and audit trail.
- **Jurisdiction.** Routing is constrained by jurisdiction, security policy and authority before cost is considered.
- **Edge runtime.** The planned NEO Edge Runtime is signed, sandboxed and least-privilege, with integrity-verified models, and it is not a remote-code-execution channel: every local capability is defined, permissioned, auditable and revocable. `[D] (edge-compute, S4)`

## What is not on this page

Threat models, attack surfaces, control implementations and assessment findings. Those are shared under obligation with a party that needs them, and publishing them would assist exactly the reader they are meant to defend against. No independent security assessment has been published against the platform.

---
