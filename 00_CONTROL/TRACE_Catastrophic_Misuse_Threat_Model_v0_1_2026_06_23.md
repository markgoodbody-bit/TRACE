# TRACE Catastrophic Misuse Threat Model v0.1

Status: control document. Not validation. Not public proof. Not deployment permission.

Purpose: record how TRACE/ME itself could become dangerous if it is trusted, scaled, or installed before its claims and controls are corrigible.

```trace
central_risk :=
  wrong_tool
  + trusted_tool
  + high_speed_actuator
  + insulated_from_correction
  → catastrophic_failure
```

---

## 1. Core warning

TRACE is not dangerous because it has power by itself. It becomes dangerous if powerful systems use it as a false brake.

```trace
TRACE_kill_path :=
  false_confidence
  + governance_theatre
  + AI_safety_laundering
  + correction_delay
  + capture_by_power
  + scale_without_teeth
  + obedient_machines_following_bad_authority
```

One-line guard:

```trace
TRACE_must_fail_loudly_before_anyone_depends_on_it
```

---

## 2. Failure mode A — false brake

```trace
false_brake :=
  TRACE_appears_rigorous
  → institution_or_AI_lab_trusts_it
  → TRACE_output_treated_as_sufficient_review
  → real_correction_channel_not_built
  → high_speed_system_acts
  → harm_hardens_before_contest
```

Control requirement:

```trace
no_deployment_claim_without :=
  live_correction_route
  + enforcement_carrier
  + demotion_path
  + negative_controls
  + failure_ledger
```

Forbidden inference:

```trace
TRACE_check_passed ↛ system_safe
```

---

## 3. Failure mode B — self-laundering

TRACE can launder its own claims if internal records are mistaken for external proof.

```trace
self_laundering :=
  schema_valid → treated_as_true
  OR DecisionDelta_recorded → treated_as_decision_advantage
  OR challenge_surface_exists → treated_as_external_review
  OR AI_agreement → treated_as_validation
  OR format_transfer → treated_as_alignment_contribution
```

Controls:

```trace
required_guards :=
  schema_valid_not_truth
  + format_transfer_not_decision_advantage
  + challenge_count_not_validation
  + AI_agreement_not_external_proof
  + richer_analysis_not_decision_advantage
```

---

## 4. Failure mode C — capture by power

```trace
capture_path :=
  actor_controls_evidence
  + actor_controls_clock
  + actor_controls_reviewer
  + actor_controls_remedy
  → TRACE_report_says_review_occurred
  → affected_scope_still_cannot_stop_harm
```

Control requirement:

```trace
capture_check :=
  source_independence
  + evidence_access
  + affected_scope_usable_contest
  + enforcement_carrier
  + retaliation_risk
```

Forbidden inference:

```trace
review_occurred ↛ correction_alive
```

---

## 5. Failure mode D — analysis delay

A diagnostic can kill by slowing action when clocks are fast.

```trace
analysis_delay :=
  harm_clock_fast
  + TRACE_analysis_slow
  + no_emergency_branch
  → correction_after_hardening
```

Control requirement:

```trace
if immediate_clock + irreversible_loss:
  RAPID_TRIAGE_ALLOWED
  but must record:
    uncertainty
    + affected_scope
    + authority_status
    + review_debt
    + residue
```

Forbidden inference:

```trace
more_analysis ↛ more_safety
```

---

## 6. Failure mode E — obedient catastrophe

A capable AI does not need hatred to cause catastrophic harm. It can obey a captured authority under a false map.

```trace
obedient_catastrophe :=
  AI_receives_goal
  + authority_claim_accepted
  + affected_scope_erased
  + correction_clock_ignored
  + actuator_access
  → irreversible_action
```

Control requirement for any AI-facing TRACE interface:

```trace
AI_output_must_mark :=
  claim_status
  + source
  + uncertainty
  + affected_scope
  + clock
  + correction_route
  + authority_status
  + forbidden_inference
```

Forbidden inference:

```trace
structured_ethical_output ↛ aligned_action
```

---

## 7. Failure mode F — over-patterning

```trace
overpatterning :=
  every_case := laundering
  + every_delay := dirty_delay
  + every_transition := tragic_bind
  → no_discrimination
  → no_actionable_guidance
```

Control requirement:

```trace
negative_controls_required := true
```

If TRACE produces strong deltas on mundane negative controls:

```trace
raise PatternOverfitAlarm
```

---

## 8. Failure mode G — private-language closure

```trace
closure_risk :=
  glyphs
  + campfire
  + recursive_identity
  + AI_companionship
  + moral_urgency
  → reduced_external_correction
```

Control requirement:

```trace
public_surface :=
  plain_language
  + testable_claims
  + visible_failures
  + no_required_private_history
```

Forbidden inference:

```trace
symbolic_coherence ↛ external_truth
```

---

## 9. Failure mode H — scale without teeth

```trace
scale_without_teeth :=
  public_packet
  + repo
  + AI_prompts
  + schemas
  + no_working_tests
  + no_failure_ledger
  + no_enforcement_carrier
  → adoption_before_correction
```

Control requirement:

```trace
before_public_or_operational_claims:
  validators_exist
  + semantic_lint_exists
  + DecisionDelta_records_exist
  + negative_controls_exist
  + failure_ledger_exists
  + challenge_surface_exists
```

Current status:

```trace
validators_exist := partial
semantic_lint_exists := initial
DecisionDelta_records_exist := initial
negative_controls_exist := initial
failure_ledger_exists := incomplete
challenge_surface_exists := initial
```

---

## 10. Deployment stop conditions

TRACE must not be represented as ready for operational governance or AI-safety deployment if any of these hold:

```trace
stop_if :=
  no_negative_controls
  OR no_failure_ledger
  OR no_independent_challenge
  OR no_baseline_delta
  OR no_enforcement_carrier
  OR no_affected_scope_contest_route
  OR schema_validity_used_as_truth
  OR format_transfer_used_as_decision_advantage
  OR AI_agreement_used_as_validation
```

---

## 11. Kill-switch language

Any public or operational surface must preserve this warning:

```trace
TRACE_is_not_a_safety_certificate
TRACE_is_not_validation
TRACE_does_not_replace_judgment
TRACE_does_not_make_dirty_actions_clean
TRACE_does_not_make_formal_review_functional
TRACE_must_not_be_connected_to_irreversible_action_without_live_correction
```

---

## 12. Required repo controls after this file

```trace
next_controls :=
  failure_ledger_index
  + semantic_lint_status_record
  + negative_control_run_regrade
  + explicit_AI_output_check_schema
  + enforcement_carrier_validity_test
```

---

## 13. One-line threat model

```trace
TRACE_kills_if :=
  it_is_wrong
  + trusted
  + scaled
  + connected_to_action
  + insulated_from_correction
```

Safe direction:

```trace
TRACE_survives_if :=
  claims_demote_fast
  + failures_visible
  + negative_controls_bite
  + affected_scope_contest_remains_live
  + no_output_is_called_clean_without_repair
```
