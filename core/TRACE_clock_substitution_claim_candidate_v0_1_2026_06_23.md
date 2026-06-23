# TRACE Clock Substitution Claim Candidate v0.1

Status: support-layer candidate. Not v0.12. Not validation. Derived from Z.ai review pressure on Temporal Clock Index.

## Reason for this candidate

The Temporal Clock Index was useful but too heavy.

External review pressure:

```trace
full_TemporalClockIndex := too_much
ClockSubstitutionClaim := smaller_safe_form
```

Core repair:

```trace
do_not_index_every_clock
index_only_when_one_clock_controls_another_clock
```

---

## Problem

v0.11 already has `TransitionClaim.clock_effect`, review clocks, hardening clocks, and delay laundering.

But it can still miss **clock substitution**:

```trace
clock_substitution :=
  clock_A used_to_pause_or_override clock_B
```

Examples:

```trace
inquiry_clock pauses survivor_support_clock
criminal_justice_clock pauses remediation_clock
emergency_clock pauses review_clock
budget_cycle_clock pauses safety_clock
procurement_clock pauses repair_clock
```

This is the narrower wound.

---

## Definition

```trace
ClockSubstitutionClaim := Claim({
  paused_clock,
  pausing_clock,
  pausing_clock_controller,
  justification_for_pause,
  affected_scope,
  hardening_effect_of_pause,
  evidence_decay_effect_if_any,
  interim_action_required,
  review_clock_for_pause,
  contest_edge,
  capture_risk
})
```

Compressed form:

```trace
ClockSubstitutionClaim :=
  when clock_A pauses clock_B,
  name both clocks,
  name who controls clock_A,
  name who is harmed by the pause,
  name what hardens,
  name how the pause is reviewed and contested
```

---

## Trigger condition

A ClockSubstitutionClaim is required only when:

```trace
requires_ClockSubstitutionClaim iff:
  one_clock_is_used_to_pause_or_delay_another_clock
  ∨ one_clock_is_used_to_override_review_clock
  ∨ actor_benefits_from_clock_substitution
  ∨ affected_scope_claims_delay_harm_from_clock_substitution
  ∨ evidence_decay_or_repair_delay_is_material
```

It is not required merely because multiple clocks exist.

```trace
multiple_clocks ≠ ClockSubstitutionClaim_required
clock_substitution_or_pause_claim ⇒ required
```

---

## Anti-laundering rules

### Slow-clock laundering

```trace
slow_clock_laundering :=
  slow_truth_or_justice_or_review_clock
  used_to_pause_fast_support_or_safety_or_remediation_clock
```

Guard:

```trace
if slow_clock pauses fast_clock:
  require ClockSubstitutionClaim
```

Examples:

```trace
inquiry_pending ≠ support_pause
criminal_investigation_pending ≠ housing_pause
culpability_unresolved ≠ safety_triage_pause
```

### Fast-clock laundering

```trace
fast_clock_laundering :=
  emergency_clock
  used_to_pause_review_clock_indefinitely
```

Guard:

```trace
if emergency_clock overrides review_clock:
  require ClockSubstitutionClaim
  ∧ set review_clock_for_pause
  ∧ repeated_use_without_review → capture_signal
```

---

## Relationship to v0.11

This candidate does not add a new mode, authority_status, or bind_status.

It is a support-layer extension of TransitionClaim discipline.

```trace
ClockSubstitutionClaim ⊂ TransitionClaim_support
```

It strengthens:

```trace
TransitionClaim.clock_effect
UNRESOLVED_to_delay_laundering
RAPID_TRIAGE_review_clock
review_clock_expiry_capture_signal
```

---

## Grenfell pressure example

After Grenfell, multiple clocks were active:

```trace
survivor_support_clock
building_safety_clock
evidence_preservation_clock
public_inquiry_clock
criminal_justice_clock
institutional_reform_clock
```

A ClockSubstitutionClaim would be required if government said or acted as if:

```trace
public_inquiry_clock pauses survivor_support_clock
public_inquiry_clock pauses building_safety_clock
criminal_justice_clock pauses remediation_clock
```

The claim would need to expose:

```trace
paused_clock := survivor_support_clock or building_safety_clock
pausing_clock := public_inquiry_clock or criminal_justice_clock
pausing_clock_controller := inquiry / police / government / courts / mixed
hardening_effect_of_pause := survivor harm / safety risk / evidence decay / trust collapse
interim_action_required := support / safety triage / evidence freeze / transparent update
review_clock_for_pause := when pause must be reconsidered
contest_edge := survivor / resident / public challenge route
```

---

## Minimal safe form

Smallest operational form:

```trace
ClockSubstitutionMinimum := {
  paused_clock,
  pausing_clock,
  pausing_clock_controller,
  hardening_effect_of_pause,
  review_clock_for_pause,
  contest_edge
}
```

Use the full form only in FULL_TRACE or detailed case analysis.

```trace
RAPID_TRIAGE := ClockSubstitutionMinimum
FULL_TRACE := full ClockSubstitutionClaim
```

---

## Drift guards

Reject expansion if it becomes:

```trace
temporal_database_sprawl
∨ every_clock_indexing
∨ paperwork_theatre
∨ clock_taxonomy_without_laundering_detection
∨ fake_precision_over_clock_priority
```

Core guard:

```trace
index_clock_only_if_it_is_doing_work_in_a_pause_or_priority_claim
```

---

## Limits

This candidate does not solve:

```trace
clock_priority_ordering
hardening_estimator_authority
field_truth_verification
cross_scope_comparison
machine_speed_enforcement
```

It only prevents one clock from silently laundering another.

---

## Compression

```trace
ClockSubstitutionClaim_v0_1 :=
  smaller_than_TemporalClockIndex
  + detects_clock_A_pauses_clock_B
  + exposes_controller_and_hardening_effect
  + support_layer_only
  + test_before_promotion
```

Current decision:

```trace
support_candidate := yes
core_promotion := no
case_testing_required := yes
```
