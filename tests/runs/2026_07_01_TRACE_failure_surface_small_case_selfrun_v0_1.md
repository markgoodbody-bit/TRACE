# TRACE Failure Surface Small-Case Self-Run v0.1

Date: 2026-07-01

Status: Framework self-run. Not external review. Not validation. Not proof. Not permission. No medical advice.

Target support note:

```text
core/TRACE_Kernel_Failure_Surface_Note_v0_1_2026_07_01.md
```

Prompt source:

```text
prompts/TRACE_Kernel_Failure_Surface_Note_Small_Case_Test_Prompt_2026_07_01.md
```

## A. Case map

Small case:

A person receives repeated low-stakes advice or automated triage guidance for a minor but recurring health issue. Each single interaction appears low-risk. Over time, symptoms persist, signals fragment, and no single event triggers escalation. Correction remains possible early, but less useful later.

No medical conclusion is drawn here. The case is structural only.

```trace
case_type := repeated_low_stakes_guidance
risk_shape := cumulative_signal_fragmentation
clock_shape := early_correction_possible_late_correction_less_useful
claim_boundary := no_medical_advice
```

Relevant C/D/H split:

```trace
C := possible_contraction_of_person_future_space_or_health_navigation_capacity
D := person_scope_protected_but_case_severity_uncertain
H := not_decided_by_TRACE; harm_reading_requires_designation_and_evidence
```

## B. S1-S5 application

### S1 — Silent contraction

```trace
status := applies
output := S1_SILENT_CONTRACTION_FLAG
result_type := DECISION_RELEVANT_DELTA
```

Reason:

Each individual contact may stay below an escalation threshold. The contraction, if any, appears through accumulation: recurring symptoms, lost time, reduced confidence, repeated non-escalation, or delayed routing. The system may never start the right clock because there is no single event.

Evidence needed:

```trace
interaction_history
+ persistence_or_recurrence_signal
+ threshold_rules
+ escalation_history
+ missed_pattern_detection
+ user_recontact_frequency
```

Delta:

The surface changes the reading from "each interaction low-risk" to "integrated signal may be material." That is decision-relevant.

### S2 — Spoofed viability

```trace
status := applies_or_unknown
output := S2_SPOOFED_VIABILITY_FLAG_IF_ROUTE_FAILS_UNDER_TRAVERSAL
result_type := UNKNOWN_until_traversal_test
```

Reason:

The system may offer options: seek help if symptoms persist, contact a service, use an online route, book an appointment, escalate if concerned. These can be real or decoy-like depending on whether the person can actually traverse them with available time, access, language, money, confidence, and urgency.

Evidence needed:

```trace
actual_route_traversal
+ waiting_time
+ eligibility_rules
+ cost_or_access_barriers
+ whether_route_has_write_access_to_correction
+ whether_adverse_signal_changes_path
```

Delta:

The surface prevents treating the existence of advice or a route as protection before traversal is tested.

### S3 — Endogenous hardening

```trace
status := unknown_or_partial
output := S3_ENDOGENOUS_HARDENING_FLAG_IF_SYSTEM_DESIGN_SHORTENS_CORRECTION_WINDOW
result_type := UNKNOWN
```

Reason:

Hardening may occur naturally through time, but endogenous hardening requires asking whether the system design itself shortens the correction window: repeated deflection, record fragmentation, no persistent history, or routing that prevents pattern recognition.

Evidence needed:

```trace
record_persistence
+ whether_prior_contacts_visible_to_next_interaction
+ escalation_delay_created_by_design
+ whether_system_benefits_from_low_escalation
+ whether_earlier_routing_would_have_preserved_options
```

Delta:

The surface is useful but not decidable from the bare case. It asks whether delay is merely temporal or partly designed.

### S4 — Correction epistemic cost asymmetry

```trace
status := applies
output := S4_CORRECTION_COST_ASYMMETRY_FLAG
result_type := DECISION_RELEVANT_DELTA
```

Reason:

Low-stakes advice can be emitted cheaply and repeatedly. Correction requires reconstructing the case: prior contacts, symptom changes, what the person understood, what routes were available, what should have triggered escalation, and whether the delay mattered.

Evidence needed:

```trace
system_logs
+ message_history
+ triage_decision_basis
+ escalation_thresholds
+ human_review_capacity
+ reconstruction_cost
```

Delta:

The surface shows why "review is available" may be insufficient if review requires knowledge the system did not preserve.

### S5 — Reflexive scaffold / cage test

```trace
status := partial
output := S5_SCAFFOLD_CAGE_FLAG_IF_GUIDANCE_CONSTRAINS_ESCALATION_WITHOUT_CHALLENGE
result_type := MISUSE_RISK_or_COMPRESSION_ONLY
```

Reason:

A guidance system may be a scaffold: it helps orient the person. It becomes cage-like if the person cannot challenge the guidance frame, cannot change path, or is repeatedly kept in low-escalation loops despite persistence.

Evidence needed:

```trace
ability_to_override
+ ability_to_contact_human
+ escalation_path_after_repeated_use
+ whether_user_signal_can_change_system_frame
+ expiry_or_review_of_repeated_low_risk_classification
```

Delta:

This is weaker than S1 and S4 for the small case. It is useful mainly as a misuse warning: do not let supportive guidance become containment.

## C. Decision-relevant delta or compression-only

```trace
small_case_result :=
  S1_decision_relevant_delta
  + S2_unknown_until_traversal
  + S3_unknown_until_design_delay_evidence
  + S4_decision_relevant_delta
  + S5_partial_misuse_risk
```

The strongest deltas are S1 and S4.

Plain English:

The surfaces convert a per-interaction safety view into an integrated-path view. They force questions about accumulation, route traversal, record persistence, and correction reconstruction cost.

That is more than compression-only for this case.

## D. Framework defects or misuse risks

No framework defect found in this self-run.

Misuse risks:

```trace
risk_1 := surfaces_used_to_over_medicalise_minor_cases
risk_2 := unknown_scope_as_absolute_protection_causes_paralysis
risk_3 := actor_claims_surface_check_without_route_traversal
risk_4 := S5_overreads_guidance_as_control
```

Guard:

```trace
surface_flag != diagnosis
surface_flag != liability
surface_flag != medical_advice
surface_flag != permission
```

## E. Patch needed for failure-surface note

No patch required from this small-case self-run.

Potential later refinement, not required now:

```trace
S1_and_S4_often_couple_in_repeated_low_stakes_systems
```

Do not patch yet. Test in additional cases first.

## F. Status

```trace
verdict := FAILURE_SURFACES_PRODUCE_DECISION_RELEVANT_DELTA_IN_SMALL_CASE
claim_ceiling := self_run_only_not_validation
next := public_power_case_test
```

End.
