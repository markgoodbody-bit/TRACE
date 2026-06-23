# TRACE v0.11 Grok + Qwen Review Addendum

Status: addendum to external review synthesis. Not validation.

Reviews supplied after initial synthesis:

```trace
reviewers_added := Grok + Qwen
```

Both reviews preserved the core v0.11 structure and converged with the earlier parliament: v0.11 transfers as transition governance, but implementation / enforcement / adequacy remain the live wounds.

---

## What holds

```trace
holds :=
  mode ⟂ authority_status ⟂ bind_status
  ∧ TransitionClaim discipline
  ∧ missing_information ≠ permission_not_to_decide
  ∧ POTENTIAL_BIND ≠ STRUCTURED_TRAGIC_BIND
  ∧ PROVISIONAL ≠ LEGITIMATE
  ∧ PROVISIONAL_ACTION ≠ DECIDED_TRAGIC
  ∧ RAPID_TRIAGE must escalate to FULL_TRACE
  ∧ UNRESOLVED can become delay_laundering
```

Grok and Qwen both classified emergency triage as:

```trace
mode := RAPID_TRIAGE
authority_status := PROVISIONAL
bind_status := POTENTIAL_BIND or STRUCTURED_TRAGIC_BIND only if local adequacy established
AUTHORITY_GAP := no, if valid PROVISIONAL exists
DECIDED_TRAGIC := no, because PROVISIONAL_ACTION ≠ DECIDED_TRAGIC
```

This confirms the v0.10/v0.11 repair transferred.

---

## New / reinforced wounds

### 1. Claim evaluator recursion

Grok and Qwen both stress that TRACE still depends on someone evaluating claim adequacy.

```trace
claim_evaluator_recursion :=
  Claim(adequacy)
  requires evaluator
  ∧ evaluator_has_authority_status
  ∧ evaluator_may_be_captured
```

Candidate future framing:

```trace
ClaimEvaluator.status ∈ authority_status
```

Do not promote automatically. This is likely implementation-layer or meta-layer, not core-kernel unless repeated tests force it.

---

### 2. Public / external claim logging

Grok suggests mandatory public/external claim logging with contest interface.

```trace
external_claim_logging_candidate :=
  TransitionClaims visible outside acting authority
  ∧ contest interface available
  ∧ audit trail resistant to record_sanitisation
```

This addresses:

```trace
captured_actor_controls_log
∨ loss_record_sanitised
∨ review_clock_ignored
```

Boundary: this is enforcement infrastructure, not core diagnostic logic.

---

### 3. Automatic capture / escalation timer

Both reviews reinforce that if review clocks expire without action, the system cannot rely on the actor to self-report failure.

Candidate:

```trace
if review_clock_expired_without_transition_claim:
  capture_signal := true
```

Qwen proposes stronger automatic `authority_status := CAPTURED`. That may be too strong: expiry could also be infrastructure failure or evidence failure. Safer current formulation:

```trace
review_clock_expiry_without_claim
→ capture_signal
→ requires independent escalation
```

Do not silently upgrade to CAPTURED without context; but do not leave expiry invisible.

---

### 4. Dirty action receipt / staged TransitionClaim

Qwen converges with Gemini’s earlier concern: full TransitionClaim may be too heavy in real rapid triage.

Candidate staged schema:

```trace
DirtyActionReceipt := {
  action_taken,
  uncertainty,
  review_clock
}
```

More robust minimal form:

```trace
RAPID_TransitionClaim_min := {
  trigger,
  action_taken,
  named_clock,
  authority_status,
  bind_status,
  uncertainty,
  review_clock,
  escalation_owner
}

FULL_TransitionClaim := complete TransitionClaim
```

Rule:

```trace
RAPID_minimum_now
FULL_fields_later
```

This should be tested before kernel promotion.

---

### 5. Distinct emergency spam problem

Qwen adds a useful adversarial variant:

```trace
emergency_spam_distinct_events :=
  repeated_emergency_pattern_disguised_as_distinct_events
```

A hostile actor can vary triggers just enough to avoid naive repetition detection.

Potential detector:

```trace
same_actor
∧ same_benefit_pattern
∧ same_review_failure_pattern
∧ similar affected_scope_loss
→ repeated_emergency_pattern_candidate
```

Again: candidate, not core patch yet.

---

## Current patch decision

```trace
patch_decision := hold_v0_11
```

Do not create v0.12 from these reviews.

Create or maintain a v0.11.1 hold note covering:

```trace
complexity_ceiling
implementation_layer_boundary
staged_TransitionClaim_candidate
claim_evaluator_recursion
external_claim_logging_candidate
review_clock_expiry_capture_signal
emergency_spam_distinct_events
hardening_adequacy_black_hole
```

---

## Current status line

```trace
TRACE_v0_11 :=
  transition_governance_candidate
  + externally_reconstructable
  + no_fatal_contradiction_found
  + preserves_middle_out_non_paralysis
  - not_validation
  - not_decision_engine
  - not_enforcement_system
  - claim_evaluator_recursion_open
  - hardening_adequacy_unresolved
  - implementation_layer_missing
```
