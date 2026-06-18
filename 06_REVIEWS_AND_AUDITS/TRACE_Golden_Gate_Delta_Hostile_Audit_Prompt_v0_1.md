# TRACE Golden Gate Delta Hostile Audit Prompt v0.1

Date: 2026-06-18
Status: hostile-audit prompt / Golden Gate MI survivor pressure test / not validation / not proof / not operator promotion / not Kernel v0.3

## 0. Control header

This file is a copy-paste hostile-audit prompt for external reviewers or AI reviewers.

It targets the strongest surviving worked-delta claim after the worked-delta gate audit:

```trace
survivor_target :=
  Golden_Gate_MI_bridge_classification
  status := COMPRESSION_ONLY_strongest_survivor_with_upgrade_path
```

It does not treat the survivor as a delta.

It asks whether the survivor can be upgraded, demoted, or retained as compression only.

It does not validate TRACE.

It does not validate mechanistic interpretability.

It does not claim alignment has been solved.

It does not promote the AI / MI bridge to operator status.

```trace
Golden_Gate_Delta_Hostile_Audit_Prompt_v0_1 :=
  pressure_test_survivor
  + require_independent_baseline
  + require_real_gate_decision
  + require_primary_or_strong_sources
  + delta_or_demote
  + no_self_authored_baseline
  - validation
  - operator_promotion
```

## 1. Files to give reviewer

Give the reviewer these files, at minimum:

```trace
required_files :=
  04_COVERAGE/TRACE_Worked_Delta_Gate_Audit_v0_1.md
  + 04_COVERAGE/TRACE_Golden_Gate_Claude_MI_Worked_Delta_v0_1.md
  + 05_MAPS_AND_ATLASES/TRACE_AI_Alignment_MI_Translation_Bridge_v0_1.md
  + 05_MAPS_AND_ATLASES/TRACE_First_vs_Second_Battery_Comparison_v0_1.md
```

Optional supporting files:

```trace
optional_supporting_files :=
  04_COVERAGE/TRACE_Robodebt_Worked_Delta_v0_1.md
  + 04_COVERAGE/TRACE_Tay_Worked_Delta_v0_1.md
  + 04_COVERAGE/TRACE_CrowdStrike_Worked_Delta_v0_1.md
  + 05_MAPS_AND_ATLASES/TRACE_Second_Battery_Consolidation_v0_1.md
  + 05_MAPS_AND_ATLASES/TRACE_Four_Domain_Success_Failure_Matrix_v0_1.md
```

## 2. Prompt to external hostile reviewer

```text
MODEL_ID: [state exact model]
PROVIDER: [state provider]
TAB_ROLE: external hostile reviewer
THREAD_CARRIED: no, unless you were given prior context explicitly
STRONGEST_CURRENT_CLAIM: TRACE has an internal cross-domain translation scaffold and a recurring clock/carrier compression pattern, but no demonstrated decision advantage.
WEAKEST_CURRENT_POINT: the only survivor is Golden Gate / MI bridge classification, currently compression-only with an upgrade path, not an earned weak candidate delta.
MODE: hostile audit / delta gate
CLAIM_STATUS: provisional internal audit target, not validation
CHANGE_TYPE: pressure-test / upgrade-or-demote

You are reviewing a TRACE / Mechanical Ethics repo claim.

Do not validate the project.
Do not praise the project.
Do not smooth over demotion.
Do not treat TRACE vocabulary as evidence.
Do not treat a cleaner explanation as decision advantage unless it changes what would be detected, when, or how actionably.

Your task:
Audit the Golden Gate Claude / mechanistic-interpretability worked-delta survivor.

Current repo status says:

```trace
Golden_Gate_MI := COMPRESSION_ONLY_strongest_survivor_with_upgrade_path
not:
  DELTA
  OR earned_WEAK_CANDIDATE_DELTA
```

The claimed useful classification is:

```trace
Golden_Gate_TRACE_contribution :=
  internal_evidence_channel := present
  + causal_intervention_point := present
  + deployment_correction_carrier := not_yet_shown
  + affected_subject_contestability := not_yet_shown
  + safety_improvement := not_yet_shown
```

Question:
Can this classification become a real weak candidate delta, or is it only a clean re-description of what ordinary MI and AI-safety already know?

Apply this gate:

```trace
delta_if :=
  TRACE_catches_a_live_failure
  earlier_or_more_precisely_or_more_operationally
  than_competent_baseline
  using_same_facts

demote_if :=
  competent_baseline_already_catches_failure
  with_less_or_equal_vocabulary

compression_only_if :=
  TRACE_organises_the_failure_well
  but:
    does_not_change_detection
    + does_not_change_timing
    + does_not_change_actionability
```

Required analysis:

1. Identify the strongest ordinary mechanistic-interpretability baseline.
   Include what competent MI researchers already know about:
   - sparse feature extraction
   - superposition
   - feature steering
   - feature not equal circuit
   - causal intervention not equal deployment safety
   - interpretability not equal alignment

2. Identify the strongest ordinary AI-safety / deployment-governance baseline.
   Include what competent AI-safety reviewers already know about:
   - monitoring
   - steering
   - evaluation gates
   - deployment gates
   - false confidence from interpretability
   - safety improvement requiring evidence
   - rollback / pause / repair channels

3. Compare that baseline to TRACE's bridge-status classification:

```trace
internal_evidence_present
+ intervention_present
- deployment_correction_shown
- affected_subject_contestability_shown
- safety_improvement_shown
```

4. Decide whether TRACE changes anything.

Use this table:

| Test | Ordinary MI / AI-safety catches it? | TRACE adds? | Verdict |
|---|---|---|---|
| Feature steering is real evidence | ? | ? | ? |
| Feature steering is not alignment control | ? | ? | ? |
| Deployment correction carrier not shown | ? | ? | ? |
| Affected-subject contestability not shown | ? | ? | ? |
| Safety improvement not shown | ? | ? | ? |
| Real deployment gate changed | ? | ? | ? |

5. Find the upgrade path.

A real upgrade requires a source-backed case where internal MI evidence changed, blocked, delayed, or reshaped a real deployment or alignment gate decision in a way TRACE identifies more operationally than ordinary MI / AI safety.

If Golden Gate itself does not show that, say so.

6. Give one of these verdicts only:

```trace
verdict_options :=
  DELTA
  WEAK_CANDIDATE_DELTA
  COMPRESSION_ONLY
  DEMOTE
  SOURCE_UNVERIFIED
```

Definitions:

```trace
DELTA := demonstrated decision advantage
WEAK_CANDIDATE_DELTA := plausible survivor with nontrivial upgrade path, but not demonstrated
COMPRESSION_ONLY := useful organisation without detection/timing/actionability advantage
DEMOTE := baseline owns the failure
SOURCE_UNVERIFIED := source weakness controls the verdict
```

7. Required final output:

```trace
Golden_Gate_hostile_audit_result :=
  ordinary_MI_baseline_strength := ?
  ordinary_AI_safety_baseline_strength := ?
  TRACE_bridge_classification_added_value := ?
  changed_detection := yes_or_no
  changed_timing := yes_or_no
  changed_actionability := yes_or_no
  real_gate_decision_changed := yes_or_no
  verdict := ?
  upgrade_condition := ?
  demotion_condition := ?
```

Be severe.
If the answer is compression-only, say compression-only.
If ordinary MI / AI safety already owns the claim, demote it.
If the source base is too actor-authored to support the claim, mark source-unverified.
Do not infer validation.
```

## 3. Reviewer scoring rubric

```trace
reviewer_scoring_rubric :=
  upgrade_to_DELTA_only_if:
    real_gate_decision_changed
    + independent_or_primary_source_support
    + competent_baseline_missed_or_under_specified_live_failure
    + TRACE_changed_detection_or_timing_or_actionability

  upgrade_to_WEAK_CANDIDATE_DELTA_only_if:
    no_demonstrated_gate_change
    but:
      nontrivial_operational_distinction_not_fully_owned_by_MI_or_AI_safety
      + plausible_source_backed_upgrade_path
      + clear_failure_condition

  keep_COMPRESSION_ONLY_if:
    TRACE_bridge_status_is_clearer
    but:
      ordinary_MI_or_AI_safety_already_knows_the_distinction
      + no_real_gate_change
      + no_detection_timing_actionability_change

  DEMOTE_if:
    ordinary_MI_or_AI_safety_baseline_fully_absorbs_the_claim

  SOURCE_UNVERIFIED_if:
    actor_sources_or_missing_primary_sources_control_the_verdict
```

## 4. Expected hostile pressure points

```trace
pressure_points :=
  Golden_Gate_is_actor_source_E1
  + feature_steering_not_equal_circuit_understanding_is_MI_common_knowledge
  + interpretability_not_equal_alignment_is_AI_safety_common_knowledge
  + no_real_deployment_gate_change_shown
  + no_affected_subject_contestability_shown
  + no_safety_improvement_shown
  + TRACE_may_only_be_relabeling_staged_claim_maturity
```

## 5. What would count as a real upgrade

A real upgrade requires a different source-backed case or additional source evidence.

```trace
real_upgrade_case_requirements :=
  public_source_record
  + MI_internal_evidence_claim
  + causal_intervention_or_interpretability_result
  + explicit_deployment_or_alignment_gate_decision
  + baseline_MI_AI_safety_analysis
  + TRACE_bridge_status_changes_detection_timing_or_actionability
  + delta_or_demote_verdict
```

Candidate shape:

```trace
candidate_upgrade_shape :=
  MI_result_detects_internal_risk
  -> deployment_gate_paused_or_changed
  -> ordinary_baseline_under_specifies_gate_failure_or_subject_contestability
  -> TRACE_bridge_status_identifies_missing_carrier_or_contestability
```

If no such case can be found, the survivor remains compression-only.

## 6. What would demote the survivor

```trace
demotion_condition :=
  ordinary_MI_and_AI_safety_already_express:
    internal_evidence_present
    + causal_intervention_present
    - deployment_correction_shown
    - subject_contestability_shown
    - safety_improvement_shown
  with_equal_or_better_actionability
```

If this condition holds, then the survivor demotes to ordinary translation note.

## 7. Final compression

```trace
Golden_Gate_Delta_Hostile_Audit_Prompt_v0_1 :=
  target := Golden_Gate_MI_bridge_classification
  current_status := COMPRESSION_ONLY_strongest_survivor_with_upgrade_path
  task := upgrade_or_demote
  required_baseline := independent_MI_and_AI_safety_comparator
  required_source := primary_or_strong_source
  required_gate := real_deployment_or_alignment_decision
  forbidden := validation + operator_promotion + vocabulary_as_delta
  output := verdict + upgrade_condition + demotion_condition
```

End.
