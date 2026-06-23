# TRACE Clock Substitution Claim Candidate v0.2

Status: support-layer candidate. Not v0.12. Not validation. Supersedes v0.1 as the active candidate after Claude hostile review.

## Summary

v0.1 correctly shrank the bloated Temporal Clock Index into a narrower detector:

```trace
clock_A pauses_or_delays clock_B
```

Claude review found the live defect: the v0.1 trigger depended too much on the pausing actor recognising or admitting that substitution was occurring.

v0.2 repairs this by making the trigger externally raisable and by adding a filing-not-justification guard.

```trace
v0_2_delta :=
  externally_raisable_trigger
  + filing_neq_justification
  + interim_action_guard
```

No new state category is added.

---

## Problem

v0.11 has:

```trace
TransitionClaim.clock_effect
review_clock
delay_laundering
hardening_clock
RAPID_TRIAGE → FULL_TRACE
missing_information ≠ permission_not_to_decide
```

But v0.11 does not force one specific relation into view:

```trace
legitimate_or_plausible_clock_A
used_to_pause_or_delay
legitimate_or_urgent_clock_B
```

This is not empty delay. It is filled delay: delay justified by another process, inquiry, review, litigation, budget, procurement, or emergency clock.

```trace
filled_delay := delay_with_apparent_process_reason
```

ClockSubstitutionClaim exists to expose this relation.

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
  name who bears delay harm,
  name what hardens,
  name interim action,
  name review and contest route
```

---

## Minimum form

For RAPID_TRIAGE or low-bandwidth use:

```trace
ClockSubstitutionMinimum := {
  paused_clock,
  pausing_clock,
  pausing_clock_controller,
  hardening_effect_of_pause,
  interim_action_required,
  review_clock_for_pause,
  contest_edge
}
```

v0.2 adds `interim_action_required` to the minimum form because filing alone must not legitimise the pause.

---

## Trigger rule

A ClockSubstitutionClaim is required when:

```trace
requires_ClockSubstitutionClaim iff:
  actor_asserts_clock_substitution
  ∨ affected_scope_raises_plausible_ClockSubstitutionChallenge
  ∨ independent_witness_raises_plausible_ClockSubstitutionChallenge
  ∨ reviewer_raises_plausible_ClockSubstitutionChallenge
  ∨ observed_conduct_functionally_displaces_one_clock_with_another
```

This is the main v0.2 repair.

```trace
self_trigger_only := invalid_detector
```

---

## Clock Substitution Challenge

An affected scope or independent witness need not prove substitution conclusively to force a response.

They must make a plausible challenge:

```trace
ClockSubstitutionChallenge := Claim({
  paused_clock,
  suspected_pausing_clock,
  basis_for_suspicion,
  affected_scope,
  suspected_delay_harm,
  requested_response
})
```

If raised:

```trace
ClockSubstitutionChallenge_raised
→ controller_must_file_ClockSubstitutionClaim_or_rebut_on_record
```

Failure to respond becomes a capture/delay signal:

```trace
challenge_raised
∧ no_file_or_rebuttal
→ delay_laundering_signal
∨ capture_signal
```

---

## Filing is not justification

```trace
filing ≠ justification
```

A filed ClockSubstitutionClaim only records and exposes the pause. It does not make the pause legitimate.

A pause remains suspect unless it includes interim action while the paused clock continues to run.

```trace
filed_pause
∧ no_interim_action_required
→ delay_laundering_signal
```

```trace
filed_pause
∧ interim_action_required_but_not_taken
→ delay_laundering_signal
```

The review clock for the pause must not become the new laundering clock.

```trace
review_clock_for_pause
used_to_pause_interim_action
→ second_order_clock_laundering
```

---

## Slow-clock laundering

```trace
slow_clock_laundering :=
  slow_truth_or_justice_or_review_clock
  used_to_pause_fast_support_or_safety_or_remediation_clock
```

Examples:

```trace
public_inquiry_clock pauses survivor_support_clock
criminal_justice_clock pauses remediation_clock
legal_review_clock pauses building_safety_clock
procurement_clock pauses repair_clock
```

Rule:

```trace
slow_clock pauses fast_clock
→ ClockSubstitutionClaim_or_rebuttal_required
```

---

## Fast-clock laundering

```trace
fast_clock_laundering :=
  emergency_clock
  used_to_pause_review_clock_indefinitely
```

Rule:

```trace
emergency_clock overrides review_clock
→ ClockSubstitutionClaim_required
∧ review_clock_for_pause_required
∧ repeated_use_without_review → capture_signal
```

---

## Denied substitution

v0.2 explicitly targets denied or implicit substitution.

Institutional language may say:

```trace
support_is_ongoing
∧ inquiry_handles_accountability
∧ remediation_is_complex
```

But observed conduct may show:

```trace
inquiry_clock functionally_pauses support_clock
∨ litigation_clock functionally_pauses remediation_clock
∨ budget_clock functionally_pauses safety_clock
```

If an affected scope plausibly alleges this, the controller must answer on record.

```trace
denied_substitution
∧ plausible_external_challenge
→ response_required
```

---

## Diffuse paralysis warning

ClockSubstitutionClaim remains pairwise and may miss multi-clock paralysis.

```trace
budget_clock + procurement_clock + litigation_clock + inquiry_clock
→ remediation_stall
```

No single pair may appear decisive.

Therefore:

```trace
pairwise_substitution_claim := useful_but_incomplete
```

If multiple weak pauses aggregate into material delay:

```trace
multi_clock_paralysis_candidate
→ case_method_FULL_TRACE_required
```

This is not solved in v0.2.

---

## Hardening estimator warning

`hardening_effect_of_pause` cannot be treated as self-validating.

```trace
hardening_effect_of_pause := Claim
```

If estimated by the pausing-clock controller:

```trace
capture_risk ↑
```

Evaluator authority remains unresolved:

```trace
hardening_estimator_authority := open_wound
```

---

## Relationship to v0.11

ClockSubstitutionClaim does not replace v0.11 machinery.

It strengthens:

```trace
TransitionClaim.clock_effect
UNRESOLVED_to_delay_laundering
RAPID_TRIAGE_review_clock
review_clock_expiry_capture_signal
ClockSubstitutionClaim_v0_1
```

It does not add:

```trace
new_mode
new_authority_status
new_bind_status
new_core_gate
```

---

## Grenfell pressure example

Active clocks:

```trace
survivor_support_clock
building_safety_clock
evidence_preservation_clock
public_inquiry_clock
criminal_justice_clock
institutional_reform_clock
```

Possible denied substitutions:

```trace
public_inquiry_clock functionally_pauses survivor_support_clock
public_inquiry_clock functionally_pauses building_safety_clock
criminal_justice_clock functionally_pauses remediation_clock
```

If survivors, residents, independent reviewers, or affected parties plausibly allege such substitution:

```trace
ClockSubstitutionChallenge_raised
→ government_or_controller_must_file_or_rebut_on_record
```

Any filed pause must name interim action:

```trace
interim_action_required := support / safety triage / evidence freeze / transparent update / partial remediation
```

If not:

```trace
filing_without_interim_action → delay_laundering_signal
```

---

## Drift guards

Reject use if it becomes:

```trace
paperwork_theatre
∨ filing_as_legitimacy
∨ review_clock_as_new_delay_clock
∨ actor_self_certification
∨ temporal_database_sprawl
∨ pairwise_blindness_to_diffuse_paralysis
```

Hard guard:

```trace
ClockSubstitutionClaim exposes pause; it does not justify pause.
```

---

## Limits

v0.2 still does not solve:

```trace
clock_priority_ordering
hardening_estimator_authority
field_truth_verification
cross_scope_comparison
diffuse_multi_clock_paralysis
machine_speed_enforcement
```

Status remains:

```trace
support_layer_candidate
not_core
not_v0_12
case_test_before_promotion
```

---

## Compression

```trace
ClockSubstitutionClaim_v0_2 :=
  v0_1
  + externally_raisable_trigger
  + filing_not_justification
  + interim_action_required
  + denied_substitution_handling
  - full_temporal_index
  - core_promotion
```

One-line form:

When one clock is alleged to be pausing another, the controller must name the clocks, name who controls the pausing clock, name the delay harm, provide interim action, and either justify the pause under review or rebut the allegation on record.
