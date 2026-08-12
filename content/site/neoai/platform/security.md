---
route: /platform/security/
title: Security-first architecture
host: neoai.myneogroup.com
source: PUB copy, SITE_COPY_neoai.myneogroup.com.md
classification: A
---

# Security-first architecture

## Header

**Security is a filter, not a weight**

## Body

The design decision that matters most here is a small one and it is structural. Security, policy, tenant isolation, residency and sub-processor constraints are evaluated as **admissibility filters before any scoring takes place**. They are never terms in a score.

The difference is the whole thing. A weighted term can be outvoted by an attractive quality or cost number, thousands of times a day, inside a function nobody reads. A filter cannot be outvoted. There is no score at which the trade becomes available.

A change that improves quality, cost or latency is refused if it increases exfiltration risk, weakens tenant isolation, circumvents permissioning, weakens approval, increases unsafe tool execution, exposes secrets, or materially increases injection risk.

## What is not on this page

Threat models, attack surfaces, control implementations and assessment findings. Those are shared under obligation with a party that needs them, and publishing them would assist exactly the reader they are meant to defend against.

---
