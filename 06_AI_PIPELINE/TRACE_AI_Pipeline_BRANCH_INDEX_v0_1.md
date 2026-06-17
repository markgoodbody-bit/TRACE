# TRACE AI Pipeline Branch Index v0.1

Date: 2026-06-17
Status: branch index / document-control surface / not validation

## Plain purpose

This index prevents version drift inside `06_AI_PIPELINE`.

It declares the current authority order, marks superseded files, and blocks accidental reuse of older dry runs or mappings as if they were current.

```trace
branch_index :=
  declare_current_files
  + mark_superseded_files
  + preserve_scar_records
  + prevent_filename_version_confusion
  - silent_overwrite
  - validation_claim
```

## Current branch verdict

```trace
AI_pipeline_branch_state :=
  viable_as_systems_diagnostic_branch
  + actor_claim_laundering_patched
  + operator_inflation_reduced
  + evidence_discipline_stronger
  + document_control_now_indexed
  - validated
  - alignment_solution
```

Plain version:

The branch is usable as a systems diagnostic branch. It is not validated and does not solve AI alignment.

## Current authority order

Use files in this order when interpreting the AI pipeline branch.

```trace
current_authority_order :=
  1 := TRACE_AI_Pipeline_BRANCH_INDEX_v0_1.md
  2 := TRACE_AI_Pipeline_Drift_Check_v0_2.md
  3 := TRACE_AI_Pipeline_Operator_Table_v0_1.md internal_v0_3
  4 := TRACE_AI_Dry_Run__GPT4o_System_Card_v0_2.md
  5 := TRACE_Operator_Registry_Claude_AI_Branch_Patch_v0_1.md
  6 := TRACE_AI_Pipeline_Mapping_v0_1.md subject_to_v0_3_corrections
  7 := TRACE_AI_Dry_Run__GPT4o_System_Card_v0_1.md scar_record_only
  8 := TRACE_AI_Pipeline_Drift_Check_v0_1.md superseded_by_v0_2
```

## File status table

| File | Current status | Use now? | Notes |
|---|---|---:|---|
| `TRACE_AI_Pipeline_BRANCH_INDEX_v0_1.md` | current index | yes | Use first. This file controls branch reading order. |
| `TRACE_AI_Pipeline_Drift_Check_v0_2.md` | current drift check | yes | Latest branch verdict after actor-evidence cap. |
| `TRACE_AI_Pipeline_Operator_Table_v0_1.md` | current table despite filename | yes | Internal title is v0.3. Use v0.3 content. Filename mismatch preserved as scar/document-control warning. |
| `TRACE_AI_Dry_Run__GPT4o_System_Card_v0_2.md` | current GPT-4o dry run | yes | Uses E2 actor split and actor-source cap. |
| `../05_OPERATORS/TRACE_Operator_Registry_Claude_AI_Branch_Patch_v0_1.md` | current operator patch note | yes | Records accepted Claude corrections for the AI branch. |
| `TRACE_AI_Pipeline_Mapping_v0_1.md` | background map | limited | Read subject to v0.3 operator table and v0.2 drift check. Older broader attachments are superseded. |
| `TRACE_AI_Dry_Run__GPT4o_System_Card_v0_1.md` | scar record | no, except history | Superseded for evidence discipline. Do not use for current conclusions. |
| `TRACE_AI_Pipeline_Drift_Check_v0_1.md` | scar record | no, except history | Superseded by v0.2 drift check. |

## Supersession rules

```trace
supersession_rules :=
  if_conflict:
    branch_index > drift_check_v0_2 > operator_table_internal_v0_3 > dry_run_v0_2 > Claude_patch > mapping_v0_1 > old_dry_run > old_drift_check
```

```trace
old_file_rule :=
  older_files_remain_as_scar_records
  but:
    cannot_raise_current_claim_strength
```

## Current evidence discipline

```trace
evidence_grade_current :=
  E0_none
  OR E1_claimed
  OR E2_actor_documented
  OR E2_independent_documented
  OR E3_independent_corrobated
  OR E4_replayable
```

```trace
actor_source_cap :=
  if evidence <= E2_actor_documented:
    operator_status_claim <= weak_signal_or_unknown
```

```trace
source_support_rule :=
  finding_above_E1_requires:
    specific_passage_or_artifact
    + claim_supported_by_that_passage
```

## Current operator routing for AI branch

```trace
routing_current :=
  contestability_clock -> affected_subject_route + rollback_repair
  prediction_authority_gate -> tool_action + affected_subject_route + classifier_access_gate
  future_space_closure_at_gate -> linked_consequence_of(prediction_authority_gate + contestability_clock_failure)
  technical_opacity_as_route_block -> linked_component_at_route_failure
  correction_before_hardening -> global_timing_check
  live_record -> global_liveness_check
  lever_realism -> global_state_change_check
```

## Current must-not-claim set

```trace
must_not_claim_current :=
  TRACE_validated
  OR TRACE_solves_alignment
  OR actor_document_proves_structure
  OR system_card_is_independent_audit
  OR deployment_gate_equals_prediction_authority_gate
  OR future_space_closure_is_independent_primitive
  OR broad_operator_attachment_equals_strength
  OR TRACE_defines_alignment_truth_condition
```

## Current live claims

```trace
live_claims :=
  AI_pipeline_branch_is_viable_as_systems_diagnostic
  + actor_document_laundering_has_been_identified_and_patched
  + GPT4o_dry_run_v0_2_preserves_unknowns_better_than_v0_1
  + branch_needs_no_new_case_until_doc_control_stable
```

## Current unknowns

```trace
unknowns_preserved :=
  whether_TRACE_improves_real_AI_safety_outcomes
  + whether_TRACE_outperforms_existing_AI_audit_methods
  + whether_actor_system_cards_are_sufficient_for_diagnosis
  + whether_subject_routes_exist_in_real_deployments
  + whether_rollback_levers_work_under_pressure
```

## Stop rule

```trace
stop_rule :=
  no_new_AI_cases
  until:
    branch_index_exists
    + supersession_order_clear
    + current_authority_order_followed
```

This condition is now satisfied.

## Next permitted move

```trace
next_permitted_move :=
  either:
    pause_AI_branch
  OR:
    run_one_second_documented_case
    only_if:
      source_path_exists
      + actor_evidence_cap_applied
      + unknowns_preserved
      + no_claim_strength_upgrade
```

Recommended next move:

```trace
recommended_next :=
  pause_AI_branch
  and_return_to:
    operator_registry_consolidation
    OR memory_preservation_index
```

Plain version:

The AI branch has enough structure for now. A second AI case is permitted but not required. The safer move is to pause and avoid case sprawl.
