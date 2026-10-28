---
route: /platform/deployment/
title: Deployment architecture
host: neoai.myneogroup.com
source: NEO AI x100 architecture authority (2026), sections 09, 14
classification: A
updated: 2026-10-18
---

# Deployment architecture

## Header

**One system, five deployment patterns**

## Body

Private AI is an operating model rather than a hosting choice. The question an organisation is really asking is not where the servers are; it is which data crosses which boundary, under whose control, with what record.

The same NEO system is designed to run in five patterns, with the same Mission, policy, audit and NEO Credits semantics in each. Only where the compute and the data live changes.

| Pattern | Where data and compute live | Who operates | Typical driver | Status |
|---|---|---|---|---|
| Public and managed | NEO-managed environment | NEO | Speed and simplicity, individuals and SMEs | In operation, controlled deployment |
| Private cloud | Dedicated customer environment | NEO for the customer | Data isolation, enterprise procurement | Planned |
| Hybrid | NEO control plane over customer resources | Shared | Latency, residency, existing infrastructure | Planned |
| Self-hosted | Customer private infrastructure | Customer | Regulatory perimeter, model sovereignty | Planned |
| Sovereign and high-control | National or high-control environment | Customer or mandated operator | Government adoption, legal framework | Planned |

Deployment is not execution. Deployment patterns describe how NEO is deployed; execution zones describe where a task runs. Edge Compute is an execution layer available to every pattern, not a sixth topology.

[Execution Fabric and Edge Compute](/platform/execution-fabric/)

## Status

NEO-managed SaaS is the target delivery model and is in operation inside My NEO Group and in controlled pilot programmes. `[D] (deployment.managed, S2)` Private cloud, hybrid, self-hosted and sovereign patterns are planned. `[D] (deployment.private-cloud, S5)` `[D] (deployment.hybrid, S5)` `[D] (deployment.self-hosted, S5)` `[D] (deployment.sovereign, S5)`

---
