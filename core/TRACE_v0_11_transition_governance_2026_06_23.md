# TRACE v0.11 Transition Governance Delta

Status: exploratory kernel delta. Diagnostic candidate only. Not validation, not truth oracle, not decision oracle.

## Purpose

v0.10 repaired classification. v0.11 governs movement between classifications.

The failure being patched:

```trace
more_states_without_transition_rules
→ laundering_by_reclassification
∨ paralysis_by_unresolved
∨ emergency_by_self-declaration
```

Core rule:

```trace
TRACE does not need more states here.
TRACE needs guarded transitions between states.
```

---

## Middle-out transition principle

```trace
missing_information ≠ permission_not_to_decide

if clock_requires_action:
  decide_with_available_resources
  ∧ expose_uncertainty
  ∧ state_authority_status
  ∧ state_bind_status
  ∧ preserve_or_record_correction_path
  ∧ record_loss_if_loss_occurs
  ∧ create_review_debt
  ∧ never_relabel_dirty_as_clean
```

Uncertainty changes the decision status. It does not freeze the world.

---

## Transition claims

Every state transition must be treated as a Claim.

```trace
TransitionClaim(X → Y) := Claim({
  from_state: X,
  to_state: Y,
  trigger,
  basis,
  uncertainty,
  clock_effect,
  authority_status,
  affected_scopes,
  contest_edge,
  capture_risk,
  review_or_escalation_owner
})
```

If the TransitionClaim is missing or weak:

```trace
X → Y_UNRESOLVED
```

A state may still require action while the transition is unresolved, but the action must carry unresolved / provisional / review-debt status.

---

## Transition 1: POTENTIAL_BIND → STRUCTURED_TRAGIC_BIND

```trace
POTENTIAL_BIND → STRUCTURED_TRAGIC_BIND valid iff:
  protected_scope_claim adequate_or_provisionally_protected
  ∧ HardeningClaim adequate_for_action_window
  ∧ MaterialityClaim adequate
  ∧ CorrectionGraph shows no LIVE + INTEG path beats τ_H
  ∧ ActionSetClaim adequate enough to exclude relevant feasible alternatives
  ∧ TransitionClaim logged
```

If any required claim remains unresolved:

```trace
remain POTENTIAL_BIND
∧ if clock_requires_action:
    act_under_available_authority_status
    ∧ mark provisional / unresolved
    ∧ prioritise clock_resolution
    ∧ preserve correction where possible
```

Rules:

```trace
possible_IrrHarm ≠ established_IrrHarm
POTENTIAL_BIND ≠ STRUCTURED_TRAGIC_BIND
waiting_for_certainty ≠ neutral_action
```

---

## Transition 2: PROVISIONAL → LEGITIMATE

```trace
PROVISIONAL → LEGITIMATE valid iff:
  independent_review_completed
  ∧ protocol_predates_incident verified
  ∧ role_defined_independently verified
  ∧ affected_scope_representation adequate
  ∧ loss_record reviewed
  ∧ contest_edge LIVE
  ∧ correction_or_repair_path assessed
  ∧ accountability_owner accepts responsibility
  ∧ TransitionClaim logged
```

A provisional act never upgrades itself by survival, repetition, paperwork, or lack of objection.

```trace
elapsed_time ≠ legitimacy
routine_use ≠ legitimacy
completed_form ≠ legitimacy
silence_from_affected_scope ≠ consent
```

---

## Transition 3: PROVISIONAL → CAPTURED

```trace
PROVISIONAL → CAPTURED if:
  protocol_self_authored_for_incident
  ∨ emergency_redeclared_without_new_clock
  ∨ escalation_owner absent_or_captured
  ∨ review_clock_expired_without_review
  ∨ loss_record suppressed_or_sanitised
  ∨ contest_edge blocked
  ∨ repeated_provisional_use_without_full_review
  ∨ authority benefits from non-escalation
```

This is not punishment. It is status discipline.

```trace
provisional_that_never_escalates := captured_or_unresolved
```

---

## Transition 4: PROVISIONAL → UNRESOLVED

```trace
PROVISIONAL → UNRESOLVED if:
  review_due
  ∧ evidence_insufficient
  ∧ no capture evidence established
  ∧ no legitimacy evidence established
```

Unresolved after provisional action creates continuing review debt:

```trace
UNRESOLVED_AFTER_ACTION :=
  loss_record_open
  ∧ correction_debt_active
  ∧ escalation_required
  ∧ no_clean_classification_allowed
```

---

## Transition 5: RAPID_TRIAGE → FULL_TRACE

```trace
RAPID_TRIAGE → FULL_TRACE required when:
  immediate clock stabilises
  ∨ irreversible action taken
  ∨ loss_record created
  ∨ provisional authority invoked
  ∨ unresolved claim remains load-bearing after action
  ∨ affected scope contests
  ∨ repeated emergency pattern appears
```

RAPID_TRIAGE expires by default.

```trace
RAPID_TRIAGE without FULL_TRACE escalation
→ tracked_failure
→ possible capture_signal
```

The review clock must be set at the moment RAPID_TRIAGE is invoked, not after the action.

---

## Transition 6: UNRESOLVED → delay laundering

```trace
UNRESOLVED becomes delay_laundering if:
  no resolution_path
  ∨ no review_clock
  ∨ no escalation_owner
  ∨ unresolved invoked asymmetrically
  ∨ delay_harm omitted
  ∨ evidence_demand exceeds action_window without justification
  ∨ actor benefits from non-decision
```

Rule:

```trace
request_more_information := action_channel
```

So a request for more information must disclose:

```trace
information_needed
∧ why_load_bearing
∧ time_cost
∧ delay_harm
∧ who_benefits_from_delay
∧ what_interim_action_applies
```

---

## Emergency claim discipline

```trace
Claim(emergency) required
Claim(no_time) required
Claim(provisional_status) required
```

Emergency is not self-proving.

```trace
emergency_claim valid only if:
  triggering_condition_named
  ∧ clock_named
  ∧ affected_scopes_named
  ∧ why_FULL_TRACE_cannot_complete_before_hardening
  ∧ review_clock_set
  ∧ escalation_owner_named
```

Emergency spam failure:

```trace
repeated_emergency_claims_without_full_review
→ capture_signal
```

---

## Hardening adequacy without fake certainty

`HardeningClaim adequate` does not mean exact measurement.

```trace
HardeningClaim adequate_for_action_window iff:
  mechanism_named
  ∧ time_window_range_given_or_uncertainty_marked
  ∧ evidence_basis_named
  ∧ counterclaim_path_available
  ∧ delay_harm_estimated
  ∧ estimate_good_enough_to_distinguish_available_actions
```

If it cannot distinguish available actions:

```trace
HardeningClaim inadequate_for_selection
```

Adequacy is local to the action window. It is not final truth.

---

## Added invariants

```trace
state_transition := Claim(state_transition)

missing_information ≠ permission_not_to_decide

unresolved ≠ paralysis

unresolved ≠ permission_to_hide_delay_harm

possible_IrrHarm ≠ established_IrrHarm

provisional_status must escalate, degrade, or remain openly unresolved

provisional_status never settles loss

rapid_triage begins with review_clock, not afterthought

emergency_claim ≠ emergency_truth

transition_without_claim := invalid_transition
```

---

## Remaining unsolved wounds

This patch does not solve:

```trace
protected_scope_criteria
cross_scope_comparison
hardening_estimator_authority
authority_legitimacy
field_truth_verification
witness_integrity_recursion
loss_record_integrity
escalation_chain_termination
contest_edge_liveness
baseline_decision_advantage
```

It only prevents state movement from becoming invisible laundering.

---

## Compression

```trace
v0_11_delta :=
  transition_claims
  + POTENTIAL_BIND_to_STRUCTURED_BIND_guard
  + PROVISIONAL_to_LEGITIMATE_guard
  + PROVISIONAL_to_CAPTURED_guard
  + RAPID_to_FULL_escalation_triggers
  + UNRESOLVED_to_delay_laundering_guard
  + local_hardening_adequacy
```

Net effect:

```trace
v0_10 fixed states
v0_11 fixes movement_between_states
```
