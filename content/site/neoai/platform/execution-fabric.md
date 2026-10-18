---
route: /platform/execution-fabric/
title: Execution Fabric and Edge Compute
host: neoai.myneogroup.com
source: NEO AI x100 architecture authority (2026), sections 07, 08, 09, 10
classification: A
updated: 2026-10-18
---

# Execution Fabric and Edge Compute

## Header

**Cloud when needed. Local when sufficient. NEO decides.**

## The NEO Execution Fabric

Dynamic Capability Routing answers two questions at once: which capability should do the work, and where should it execute. Every unit of work sits at the intersection of three envelopes, and NEO optimises cost, latency and energy only inside that valid space. `[D] (execution-fabric, S4)`

| Envelope | Question |
|---|---|
| Intelligence | How much reasoning and verification, set by the Intelligence Profile |
| Policy | Where data and actions may go |
| Capability | What resources exist now, from the Device Compute Profile to reserved cloud capacity |

Four normalised execution zones: **Edge** (the person's devices), **Customer Private** (workstations, servers, private cloud, private models, enterprise data), **NEO Controlled** (NEO cloud, NEO models, managed runtime, verifiers) and **External** (frontier APIs and approved specialist systems only).

Execution zones are a policy object. Public research may run in any zone. A confidential corporate document may run at the Edge, in Customer Private or in NEO Controlled. A device-only document runs at the Edge only. Frontier reasoning runs in NEO Controlled or External under data minimisation. With no compliant path, NEO fails safely and never routes around policy.

Minimum necessary data movement: only the data the selected path needs moves. Sensitive sources are processed and minimised in their zone so that only permitted derived context reaches stronger models, and local preprocessing does not by itself make external processing compliant.

## NEO Edge Compute (roadmap)

NEO is designed to use not only external APIs and NEO-controlled infrastructure but also, where technically available, permitted and beneficial, the compute and AI capabilities already present on the person's own device. The person still chooses an Intelligence Profile, never a model, a vendor or a location. `[D] (edge-compute, S4)`

Eight canonical principles: local when sufficient; quality-gated, so a local model never wins because it is already paid for; policy-first; cloud-escalated; cross-platform, with Apple, Windows and Linux as execution ecosystems rather than separate products and no Mac required; user-controlled, so local resources are permissioned, bounded, observable and revocable and never harvested; one Mission state as execution moves between devices and clouds; and vendor-agnostic, with models, runtimes and hardware backends replaceable behind one capability abstraction.

The NEO Device Capability Engine detects CPU, GPU, NPU, memory, storage, supported runtimes, battery, thermal and network state through safe benchmarks rather than spec sheets, and builds a Device Compute Profile that tells the router what can, should and cannot run on that machine. A phone, a laptop and a GPU workstation receive different local envelopes; the Mission quality target is the same.

Edge Compute enhances NEO and is not a prerequisite: a device without local AI support runs NEO fully through NEO-controlled and approved external resources. A person's device serves that person's own Missions; no cross-customer compute network is implied. User-owned compute is not free compute: it consumes electricity, hardware and attention, and what it can reduce is NEO's direct external inference and centralised infrastructure spend.

Named technologies such as Apple Silicon, the Foundation Models framework, Core ML, MLX, NVIDIA, AMD, Intel and Qualcomm are third-party ecosystems NEO is designed to integrate where supported. No ownership, endorsement or partnership is implied, and exact framework support is verified per release.

## Status

The NEO Controlled and External zones are the ones in use under the managed deployment in operation today. `[D] (deployment.managed, S2)` The full four-zone Execution Fabric and NEO Edge Compute are designed and specified, on the roadmap, and not yet a measured result. `[D] (execution-fabric, S4)` `[D] (edge-compute, S4)`

---
