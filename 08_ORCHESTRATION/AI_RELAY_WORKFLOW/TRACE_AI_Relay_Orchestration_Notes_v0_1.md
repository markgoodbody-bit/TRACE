# TRACE AI Relay Orchestration Notes v0.1

Date: 2026-06-16
Status: architecture notes / not implemented / not canon / not validation

## Source trigger

This note responds to Andy's Automated Conversation Workflow blueprint: a database-centric orchestration model for LLM interaction in which full conversation history is externalised to a local repository or vector database, and each model dynamically requests the context it needs before generating its next response.

## Plain summary

The blueprint is useful because it solves the relay problem we keep hitting manually.

Instead of giving Claude, ChatGPT, Gemini, or another model a huge bundle of files plus a long transcript, the system does this:

1. Store full archive and full dialogue externally.
2. Give the receiving model the latest opposing claim.
3. Ask the model what context it needs to answer or falsify that claim.
4. Search the local archive for matching context.
5. Give the model the retrieved context plus the claim.
6. Record the answer.
7. Repeat, under hard caps.

## TRACE compression

```trace
external_memory :=
  full_archive
  + full_turn_log
  + source_metadata

model_turn :=
  claim_seen
  -> context_need_declared
  -> archive_query
  -> retrieved_context
  -> grounded_response
  -> ledger_write
```

## Why this fits TRACE

TRACE is strongly dependent on memory discipline. The current manual relay process loses structure because context is compressed by hand, files are omitted, and each model sees a different surface.

The orchestration design gives TRACE a more stable relay structure:

```trace
relay_value :=
  lower_context_load
  + repeatable_turn_loop
  + archive_grounding
  + full_log_preservation
  + cross_model_falsification
```

## Minimal architecture

### Components

- **Archive store**: local database, file repository, or vector-enabled store containing TRACE files, prior reviews, scar records, claims ledger, demotion protocol, operator registry, bootstraps, and session logs.
- **Orchestrator**: Python or equivalent script controlling calls, retrieval, logging, caps, and shutdown.
- **Model adapters**: API clients for each model.
- **Embedding/search layer**: vector search plus keyword fallback.
- **Ledger**: immutable or append-only record of each turn, retrieval request, retrieval result, answer, token count, and stop reason.

### Turn cycle

```trace
turn_cycle :=
  receive_claim
  -> ask_context_request
  -> retrieve_requested_context
  -> retrieve_mandatory_counter_context
  -> generate_response
  -> log_turn
  -> check_stop_conditions
```

## Critical improvement over the raw blueprint

The model must not be allowed to choose all retrieved context by itself.

If the model asks only for material that supports its argument, the relay becomes selective grounding. That is worse than no grounding because it looks disciplined while hiding counter-evidence.

TRACE therefore requires forced retrieval layers.

```trace
retrieval_bundle :=
  model_requested_context
  + mandatory_scar_context
  + mandatory_demotion_context
  + operator_registry_context
  + adversarial_near_hits
  + random_relevant_negative_hits
```

## Required TRACE safeguards

### 1. Hard turn cap

The loop must have an absolute maximum number of turns.

```trace
if turn_count >= hard_cap:
  stop
  -> terminal_summary
```

### 2. Token and cost cap

The orchestrator must log token counts and cost estimates each turn. If a threshold is exceeded, it must stop or compress under human approval.

### 3. Rate throttle

The loop should include deliberate delay between turns to avoid provider rate limits and to preserve human interrupt time.

### 4. Human interrupt

There must be a simple kill switch.

```trace
human_interrupt := always_live
```

### 5. Full retrieval ledger

Every response must log:

- model name;
- prompt class;
- retrieval request string;
- retrieved source identifiers;
- omitted source categories if any;
- answer;
- token and cost metadata;
- stop condition check.

### 6. Scar injection

Known negative findings must be retrievable even when the model does not ask for them.

Examples:

- prior failed tests;
- demoted claims;
- known overclaims;
- Amsterdam/Rotterdam-style scar records;
- hostile review warnings;
- claims labelled hypothesis rather than known.

### 7. Demotion protocol lookup

If a model makes a strong claim, the relay should automatically retrieve nearby demotion rules and ask whether the claim crosses them.

### 8. Anti-laundering check

Every response should be checked for these patterns:

```trace
laundering_flags :=
  tragedy_as_permission
  OR K_gate_checkboxing
  OR source_cherry_pick
  OR confidence_inflation
  OR method_floor_suspension
  OR validation_language_from_AI_agreement
```

## Use cases

### A. Claude vs ChatGPT hostile review

One model attacks a TRACE claim. The other defends or revises. The system logs whether the result is a surviving claim, demotion, or unresolved wound.

### B. Bootstrap V2 cluster stress test

A model reads one cluster file and asks for historical/source context. Another model tries to falsify the pattern match.

### C. Claims ledger maintenance

The relay reviews claims tagged as hypothesis and asks whether any should be demoted, tightened, or split.

### D. Operator registry pressure test

The relay asks whether a proposed operator is distinct, redundant, overclaimed, or merely a translation of existing concepts.

## Failure modes

### Retrieval capture

The model asks for context that supports its current path and omits known counter-material.

### Archive imbalance

The vector store retrieves polished outputs but misses scar ledgers, demotion notes, or older warnings.

### Semantic drift

The model uses TRACE vocabulary fluently while weakening the constraint.

### Cost runaway

The loop keeps generating extra rounds with decreasing marginal value.

### Debate theatre

The models produce elegant disagreement without changing the claims ledger.

### False grounding

The answer cites retrieved snippets but the snippets do not actually support the claim.

## Terminal summary requirement

Every session should end with a compact terminal record:

```trace
session_end :=
  claims_strengthened
  + claims_demoted
  + unresolved_wounds
  + source_gaps
  + next_manual_review
```

## Status

This is a build note, not implementation.

Next useful step: write a retrieval guard protocol before writing code.