---
route: /platform/mission-control/
title: Mission Control
host: neoai.myneogroup.com
source: PUB copy, SITE_COPY_neoai.myneogroup.com.md
classification: A
---

# Mission Control

## Header

**Mission Control**

Observable operational intelligence. Not a chat window with a progress bar.

## Body

Mission Control is designed to be the surface on which governed autonomous work is watched, questioned, redirected and approved.

A chat interface shows you an answer. Mission Control is designed to show you the work: the task graph as it executes, which specialist is on which node, which model was used for what, where the evidence came from, what has been verified, what has been rejected, and which decisions are waiting on a person.

## What it is designed to show

- The **live task graph**, with the state of each node
- **Named specialists coordinated by LILI**, and what each is doing
- **Real model activity**, recorded as execution provenance of a completed unit of work
- **Evidence flow**, and the chain from a claim back to its origins
- **Operational decision events**: a contradiction detected, verification activated, evidence coverage below policy threshold, a specialist deployed, a model replaced, a source rejected, a tool failed, a human approval required, a risk threshold exceeded
- **Human approvals**, and whether one is still valid
- **Confidence evolution** as evidence accumulates, derived from a stated basis rather than from a model's opinion of itself
- **Mission Replay**, to watch a completed mission again
- **Decision Time Machine**, to see what was known at the moment a decision was taken
- **Alternative Strategy**, to ask what a different approach would have done
- **Challenge This Conclusion**, to force a conclusion back through verification
- **Intelligence Branches**, to run a variant without discarding the original
- **Mission DNA**, the shape of a mission as it was actually executed
- **Memory Lens**, to see what the system retained and why
- **Intelligence Budget**, the effort allocated and consumed

## What it will never show

**Private chain-of-thought.** Reasoning tokens are deliberately excluded from the record, and the reason is not squeamishness. If the explanatory content of an audit trail is generated text, the audit trail can be confabulated, and a record that can be confabulated by the component it records is not a control.

What is shown is what happened: an event, with an actor, an authority and a subject. Not a narration of why a model thinks it happened.

## Status

Specified. Not running. `[D] (mission-control, S4)`

---
