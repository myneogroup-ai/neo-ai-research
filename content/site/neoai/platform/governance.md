---
route: /platform/governance/
title: Human authority
host: neoai.myneogroup.com
source: NEO AI x100 architecture authority (2026), sections 20, 21
classification: A
updated: 2026-10-18
---

# Human authority

## Header

**Human authority by design. Who decided, and were they entitled to.**

## Body

Most AI governance is a document. A document does not stop anything at runtime. In NEO AI, autonomy is bounded by construction.

**Approval policy.** The person sets ASK ME, AUTO or AUTONOMOUS, and that policy can only narrow what is approved automatically. `[D] (human-gates, S3)`

**Mandatory Human Gates.** They sit outside every policy, and no setting, profile or mode reaches them: production DNS changes, publishing to a public domain, act-class connector actions, and the release of a deployment. They are refused at platform level; interface enforcement is a courtesy. `[D] (human-gates, S3)`

**Agents get capabilities, never credentials.** Connecting an external service is one click for the person, and NEO still runs the shortest valid flow, never skipping OAuth, an operating-system permission, an enterprise administrator approval or a health-data consent.

Two questions are kept separate, because collapsing them produces an audit trail that records permission without entitlement: **may this happen**, and **who was entitled to decide it happens**. An approval is an object with a scope and a lifetime, not a click. A Mission runs inside an envelope set when it is created; the envelope can contract automatically and expands only by explicit authority. Recovery from a fault never expands it. `[D] (mission.envelope, S3)` `[D] (core.governance, S3)`

## Separations that never collapse

Connected is not personal context, is not memory, is not training consent, is not authority to act, is not local compute permission, is not computer control. A connected mailbox does not authorise sending. A connected DNS provider does not authorise publishing. A GPU made available for inference does not authorise reading files or acting. A build that completed locally still waits for human authority before release. More intelligence, more agents or more compute never create more authority.

## Autonomy is derived, not configured

How much a system may do without asking is derived from how reversible the action is and how consequential it would be if wrong. The derivation is published.

[Bounding the Autonomy Budget](/research/technical-notes/bounding-the-autonomy-budget/)

## Status

Approval policy, Human Gates, the Mission Envelope and policy enforcement are implemented and in validation. `[D] (human-gates, S3)` `[D] (mission.envelope, S3)` `[D] (core.governance, S3)`

---
