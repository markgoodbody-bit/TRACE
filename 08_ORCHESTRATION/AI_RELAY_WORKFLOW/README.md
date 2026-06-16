# AI Relay Workflow

Date: 2026-06-16
Status: build workspace / orchestration architecture / not canon / not validation

## Plain purpose

This folder captures a practical architecture for running TRACE-style adversarial AI review without passing an ever-growing conversation transcript between models.

It is based on Andy's Automated Conversation Workflow blueprint: an external data store holds the conversation history and archive, while an orchestrator asks each model what context it needs, retrieves targeted material, and then asks the model to answer with that retrieved context.

## TRACE translation

```trace
AI_relay_workflow :=
  external_memory
  + targeted_retrieval
  + adversarial_turn_loop
  + full_logging
  + hard_caps
  + human_interrupt
```

## Why this matters

TRACE work has a practical relay problem:

- external AIs can often read long files;
- many cannot handle too many files;
- full conversation history quickly becomes too large;
- manual handoff causes drift, cherry-picking, and memory loss.

This folder explores a way to make the relay more mechanical.

## Core design principle

The model should not receive everything.

The model should first state what it needs, then receive targeted context plus mandatory adversarial context.

```trace
turn_cycle :=
  opponent_claim
  -> context_request
  -> retrieval
  -> forced_counter_retrieval
  -> grounded_response
  -> ledger_write
```

## Non-claims

This folder does not claim:

- automated AI debate produces truth;
- vector search retrieves all relevant context;
- model-selected retrieval is neutral;
- an orchestration script removes the need for human judgment;
- this is an implemented production system.

## Main danger

The main risk is retrieval capture.

A model may retrieve only the evidence that helps its current argument. A vector store may miss scar records, demotion notes, or relevant counterexamples. An apparently grounded answer can still be selectively grounded.

Therefore any TRACE relay must include mandatory hostile retrieval.

## Required safeguards

Every relay loop should include:

- hard turn cap;
- rate throttle;
- token and cost cap;
- full turn ledger;
- source identifiers for retrieved material;
- mandatory scar ledger retrieval;
- mandatory demotion protocol retrieval;
- adversarial counter-hit retrieval;
- human interrupt;
- terminal session summary.

## First files

1. `TRACE_AI_Relay_Orchestration_Notes_v0_1.md` — architecture translation and TRACE critique.
2. `TRACE_Retrieval_Guard_Protocol_v0_1.md` — anti-cherry-picking and scar-injection rules.

## Build rule

Do not turn this into a grand automation project yet.

First capture the structure and the failure modes. Then test manually. Only then write code.