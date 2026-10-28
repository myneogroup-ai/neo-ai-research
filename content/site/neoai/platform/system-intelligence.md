---
route: /platform/system-intelligence/
title: NEO System Intelligence
host: neoai.myneogroup.com
source: NEO AI x100 architecture authority (2026), sections 01, 04, 15, 26
classification: A
updated: 2026-10-18
---

# NEO System Intelligence

## Header

**An AI organisation, not an AI assistant**

NEO Core is the orchestration layer of the Intelligence Operating System, above models, agents, tools, memory, knowledge, evidence, verification and compute.

## Body

A model answers a question. A system completes a unit of work, which is a different thing: it has to be attributable, performed under an authority, bounded, and recorded.

NEO Core supplies those four properties. It decomposes a Mission into coordinated sub-tasks, assigns each one to the most suitable capability and a permitted execution zone, executes them in parallel, cross-checks their results through independent verifiers, escalates only the difficult parts to more powerful models and assembles the verified output. `[D] (core, S2)` `[D] (core.task-graph, S2)` `[D] (core.verification, S3)`

The organisation is logical and its execution is heterogeneous. A document agent may work on the person's device, a financial model in deterministic local computation, a research agent through external tools, a strategy agent through frontier reasoning and a verifier through an independent route, all under one Mission.

There is no reason to assume one model, or one place to run it, will always be the best at every component of every task. One model may be strongest at deep reasoning, another at coding, another at latency, another dramatically cheaper for extraction; a local model may be the right choice where privacy or proximity matters, and a specialist tool may outperform every general-purpose model for a particular operation. NEO combines the best capability and the best execution location for each component instead of forcing one model to do everything. That is an architectural position, not a benchmark.

## Models remain replaceable. The architecture compounds.

GPT, Claude, Gemini, Grok, Kimi, Qwen, DeepSeek, private and open models can be swapped as the market evolves, and so can API providers, clouds, runtimes, GPUs and NPUs; if one deteriorates, NEO routes around it. `[D] (core.routing, S2)` Orchestration, routing, evaluation, memory, verification, provenance, integrations and vertical configurations accumulate with every Mission. External models are named only as third-party systems NEO can orchestrate; no ownership, endorsement or partnership is implied.

Eight operations, and the argument for why they compound rather than add, is published in full.

[From Model Intelligence to System Intelligence](/research/papers/model-intelligence-to-system-intelligence/)

## A distinction that matters

**NEO System Intelligence** is this layer. **NEO Intelligence** is the investigation vertical, covering open-source intelligence, registries and beneficial ownership, blockchain and wallet intelligence, AML and sanctions screening through licensed providers, and adverse media. The names are one word apart and they are different things.

[NEO Intelligence](/platform/neo-intelligence/)

## Status

NEO Core, the Task Graph and Dynamic Capability Routing are in operation inside My NEO Group and in controlled pilot programmes. `[D] (core, S2)` Verification is implemented and in validation. `[D] (core.verification, S3)`

---
