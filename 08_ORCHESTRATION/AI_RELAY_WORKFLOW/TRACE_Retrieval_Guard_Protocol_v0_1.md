# TRACE Retrieval Guard Protocol v0.1

Date: 2026-06-16
Status: guard protocol / not implemented / not canon

## Plain purpose

This protocol prevents an AI relay system from becoming a cherry-picking machine.

If a model chooses all the context it receives, it can accidentally or deliberately retrieve only the material that helps its current argument. TRACE requires the retrieval step to include hostile and corrective context by default.

## Core rule

```trace
retrieval_valid_if :=
  requested_context
  + counter_context
  + scar_context
  + demotion_context
  + source_ids
  + omission_log
```

## Retrieval bundle

Every model turn should receive a bundle with five layers.

### Layer 1 — Model-requested context

The model states what it thinks it needs.

Example prompt:

> Review the opponent claim. Name the precise concepts, source files, prior objections, or case records you need to answer or falsify it. Return only retrieval terms.

### Layer 2 — Mandatory scar retrieval

The orchestrator retrieves known failures and negative findings related to the requested topic.

Examples:

- failed tests;
- prior demotions;
- hostile review warnings;
- known overclaim notes;
- unresolved wounds;
- cases where TRACE did not improve over baseline.

### Layer 3 — Demotion protocol retrieval

The orchestrator retrieves rules that could demote, narrow, or block the claim.

### Layer 4 — Operator registry retrieval

The orchestrator retrieves current operator status:

- active spine;
- candidate annex;
- demoted terms;
- must-not-claim notes.

### Layer 5 — Adversarial near-hit retrieval

The orchestrator retrieves nearby material that may contradict, complicate, or weaken the model's intended response.

This should include keyword search as well as vector search, because vector search can miss exact scar labels or version markers.

## Omission log

Every retrieval response must log what was not found or not included.

```trace
omission_log :=
  no_scar_found?
  + no_demotion_found?
  + no_operator_status_found?
  + low_confidence_retrieval?
  + source_gap?
```

No answer should be treated as grounded unless the omission state is visible.

## Anti-laundering flags

The orchestrator should flag responses that contain any of the following patterns:

```trace
laundering_flags :=
  tragedy_as_permission
  OR no_clean_branch_as_method_floor_bypass
  OR K_gate_checkboxing
  OR uncertainty_erasure
  OR source_cherry_pick
  OR validation_from_AI_agreement
  OR candidate_annex_promoted_silently
  OR bootstrap_pattern_treated_as_proof
  OR historical_echo_overclaimed
```

## Response classification

Each model answer should be classified as one of:

- strengthens claim;
- narrows claim;
- demotes claim;
- finds source gap;
- finds contradiction;
- produces theatre;
- inconclusive.

The classification should be written to the ledger.

## Stop conditions

The relay should stop when any of these occur:

- hard turn cap reached;
- token/cost cap reached;
- both models repeat without new material;
- claim status changed and no further evidence is needed;
- source gap blocks further progress;
- human interrupt triggered;
- laundering flag repeats without resolution.

## Human review requirement

Automated relay can propose claim status changes, but should not silently promote claims.

```trace
auto_relay_may :=
  suggest_demote
  + suggest_narrow
  + suggest_source_gap
  + suggest_followup_test

auto_relay_must_not :=
  promote_to_core
  OR validate_TRACE
  OR create_new_operator_without_review
```

## Minimum terminal report

Every relay run should end with:

1. Claim tested.
2. Files retrieved.
3. Scar records retrieved.
4. Demotion records retrieved.
5. Strongest attack.
6. Strongest surviving response.
7. Claim status after run.
8. Open wound.
9. Recommended next action.

## Compact terminal form

```trace
relay_terminal :=
  claim
  + retrieval_bundle_ids
  + strongest_attack
  + strongest_survival
  + status_change
  + open_wound
  + next_action
```

## Falsifier for this protocol

This protocol fails if:

- a model can repeatedly avoid scar records;
- citations are present but non-load-bearing;
- demotion rules are retrieved but ignored;
- the relay produces agreement without claim-status change;
- the archive search misses known negative records;
- the process becomes too complex for a human to audit.

## Current status

This is a guard design only. It should be tested manually before code implementation.