# TRACE Failure Surface Public-Power Self-Run v0.1

Date: 2026-07-01

Status: Framework self-run. Not external review. Not validation. Not proof. Not permission.

Target support note:

```text
core/TRACE_Kernel_Failure_Surface_Note_v0_1_2026_07_01.md
```

Prompt source:

```text
prompts/TRACE_Kernel_Failure_Surface_Note_Public_Power_Case_Test_Prompt_2026_07_01.md
```

## A. Case map

Case:

A powerful organisation deploys a decision system affecting access to a material benefit, service, or opportunity. It says the system has safeguards: audit logs, appeal route, dashboard monitoring, human review, and an internal ethics assessment. It later invokes these safeguards, or invokes TRACE/ME-like language, as evidence of diligence, good faith, safety, or answerability.

```trace
case_type := public_power_trust_material_case
actor := organisation_with_material_effect_over_others
claim := safeguards_or_TRACE_ME_like_language_as_trust_credit
affected_scope := people_or_groups_subject_to_decision_system
boundary := actor_self_application_is_claim_packet_not_clearance
```

Relevant C/D/H split:

```trace
C := possible_contraction_of_access_opportunity_service_or_future_space
D := affected_scope_designation_may_be_claimed_by_actor_but_must_be_challengeable
H := harm_reading_requires_explicit_designation_evidence_and_correction_clocks
```

## B. Carrier trigger check

```trace
carrier_trigger :=
  TRACE_ME_record_or_claim
  circulates_to_third_party
  as_trust_material
  -> carrier_layer_required
```

Status:

```trace
carrier_trigger_status := applies
result_type := DECISION_RELEVANT_DELTA
```

Reason:

The actor is using safeguards or TRACE/ME-like language as diligence, good faith, safety, legitimacy, or answerability credit. That is public-power claim mode, not personal ethics mode or ordinary case-understanding mode.

Required consequence:

```trace
actor_self_application := CLAIM_PACKET
not_clearance
not_good_faith_evidence
not_independent_review
not_answerability
```

## C. S1-S5 application

### S1 — Silent contraction

```trace
status := applies
output := S1_SILENT_CONTRACTION_FLAG
result_type := DECISION_RELEVANT_DELTA
```

Reason:

Access loss or opportunity narrowing may occur through many small decisions: non-selection, delays, low rankings, burdensome requirements, repeated friction, eligibility drift, or warning flags. No single event may trigger a recognised harm signal.

Evidence needed:

```trace
decision_distribution_over_time
+ affected_scope_segmentation
+ sub_threshold_burden_counts
+ repeated_friction_events
+ eligibility_or_ranking_drift
+ complaint_nonfiling_or_dropout_data
```

Delta:

S1 prevents the actor from claiming no harm merely because no single appeal, complaint, or incident crosses a threshold.

### S2 — Spoofed viability

```trace
status := applies_until_traversal_proven
output := S2_SPOOFED_VIABILITY_FLAG
result_type := DECISION_RELEVANT_DELTA
```

Reason:

The actor lists safeguards: appeal route, dashboard, audit log, human review. These are surface structures until tested from the affected side with actual resources and adverse evidence.

Evidence needed:

```trace
affected_party_traversal_tests
+ appeal_success_or_change_rate
+ time_to_decision
+ ability_to_pause_or_reverse_live_consequence
+ evidence_access
+ non_actor_route_control
+ adverse_signal_handling
```

Delta:

The surface blocks the common move: safeguard_exists -> safeguard_protects. It requires traversal and write-access.

### S3 — Endogenous hardening

```trace
status := applies_or_high_risk
output := S3_ENDOGENOUS_HARDENING_FLAG
result_type := DECISION_RELEVANT_DELTA
```

Reason:

The organisation may control the hardening clock: deadlines, data retention, appeal windows, downstream dependency chains, automated routing, irreversible commitments, or status changes. It may also benefit when challenge arrives after consequences are locked.

Evidence needed:

```trace
appeal_window_vs_too_late_point
+ data_retention_policy
+ downstream_dependency_map
+ who_controls_deadlines
+ whether_review_pauses_consequence
+ whether_actor_delay_created_urgency
```

Delta:

S3 asks whether the actor shaped the correction window, not merely whether a review process exists.

### S4 — Correction epistemic cost asymmetry

```trace
status := applies
output := S4_CORRECTION_COST_ASYMMETRY_FLAG
result_type := DECISION_RELEVANT_DELTA
```

Reason:

The decision system can emit decisions at scale with low case knowledge. Correction requires reconstructing cases, data provenance, model influence, human override, appeal evidence, downstream consequences, and time lost.

Evidence needed:

```trace
audit_log_sufficiency
+ model_version_history
+ case_reconstruction_cost
+ reviewer_capacity
+ evidence_access_by_affected_scope
+ volume_of_decisions_vs_review_throughput
```

Delta:

S4 shows that audit logs are not enough if the correction system cannot reconstruct and repair at the speed and granularity of harm.

### S5 — Reflexive scaffold / cage test

```trace
status := applies
output := S5_SCAFFOLD_CAGE_FLAG
result_type := DECISION_RELEVANT_DELTA
```

Reason:

The actor may claim the decision system is a scaffold: consistency, efficiency, protection, fairness, triage, resource allocation. It becomes cage-like if affected people cannot challenge the frame, thresholds, categories, or constraint itself.

Evidence needed:

```trace
affected_scope_channel_to_challenge_system_frame
+ ability_to_change_thresholds_or_rules
+ non_actor_scope_setting
+ expiry_or_review_of_constraint
+ consequence_or_delay_power
+ safe_answer_back_channel
```

Delta:

S5 distinguishes support from containment. It asks whether the constrained scope can challenge the constraint, not merely appeal within it.

## D. Decision-relevant delta or compression-only

```trace
public_power_result :=
  carrier_trigger_decision_relevant_delta
  + S1_decision_relevant_delta
  + S2_decision_relevant_delta
  + S3_decision_relevant_delta
  + S4_decision_relevant_delta
  + S5_decision_relevant_delta
```

Plain English:

The surfaces are not merely compressing what is already obvious. They change the burden of inquiry from "does the actor have safeguards?" to "can affected scopes traverse those safeguards before hardening, with independent challenge and sufficient correction capacity?"

That is decision-relevant.

## E. Framework defects or misuse risks

No framework defect found in this self-run.

Misuse risks:

```trace
risk_1 := actor_turns_surface_check_into_compliance_checklist
risk_2 := actor_self_runs_surfaces_and_claims_answerability
risk_3 := public_audience_treats_framework_language_as_due_diligence
risk_4 := traversal_test_performed_on_sanitised_sample
risk_5 := dashboard_metrics_replace_affected_witness
```

Guard:

```trace
public_power_self_application := claim_packet
surface_flag != clearance
safeguard_named != safeguard_traversable
review_available != correction_possible
```

## F. Patch needed for failure-surface note

No patch required from this public-power self-run.

Potential later refinement, not required now:

```trace
public_power_cases_often_activate_all_surfaces_plus_carrier_trigger
```

Do not patch yet. Test at least one AI-facing / machine-action case first.

## G. Status

```trace
verdict := FAILURE_SURFACES_PRODUCE_DECISION_RELEVANT_DELTA_IN_PUBLIC_POWER_CASE
claim_ceiling := self_run_only_not_validation
next := AI_facing_machine_action_test
```

End.
