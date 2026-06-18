# TRACE Read Order

Status: stable repo navigation after hostile-audit patch, two worked deltas, and clock/carrier support note. Not validation. Not proof. Not governance certification.

This file tells a reader what to open first and what status each surface has. It does not change the active TRACE spine.

## Fast orientation

1. `README.md`
2. `00_START_HERE/IMPORT_MANIFEST.md`
3. `00_CONTROL/TRACE_Current_Control_Index_v0_1.md`
4. `02_CURRENT_SURFACE/PUBLIC_ONE_SHEET_v0_3/TRACE_ME_PUBLIC_ONE_SHEET_v0_3.md`
5. `02_CURRENT_SURFACE/FRONT_DOOR_v0_3/TRACE_BOOTSTRAP_ROSETTA_CURRENT_FRONT_DOOR_v0_3.md`
6. `03_BOOTSTRAPS/BOOTSTRAP_V2/00_READ_ME_FIRST__BOOTSTRAP_V2.md`
7. `03_BOOTSTRAPS/BOOTSTRAP_V2/README.md`
8. `05_MAPS_AND_ATLASES/TRACE_Universality_Map_v0_1.md`
9. `01_CANONICAL_MEMORY/PRIMITIVE_REGISTRY/TRACE_Primitive_Registry_v0_1.md`
10. `01_CANONICAL_MEMORY/DOMAIN_TRANSLATION_REGISTRY/TRACE_Domain_Translation_Registry_v0_1.md`
11. `04_COVERAGE/TRACE_Robodebt_Worked_Delta_v0_1.md`
12. `04_COVERAGE/TRACE_Tay_Worked_Delta_v0_1.md`
13. `04_COVERAGE/TRACE_Clock_Carrier_Compression_Note_v0_1.md`

Surface rule:

```trace
Rosetta_front_door := conceptual_current_surface
Bootstrap_V2 := live_relay_surface_for_external_review
ACTIVE_COLLECTION := deprecated_from_live_use + preserved_source_history
Scope_Map := scope_container + level_separator - active_spine
Primitive_Registry := base_layer + composition_support - operator_set
Domain_Translation_Registry := mapping_layer + comparator_pressure - operator_set
Robodebt_Worked_Delta := first_worked_delta + modest_clock_compression - validation
Tay_Worked_Delta := second_worked_delta + modest_clock_carrier_compression - validation
Clock_Carrier_Compression_Note := support_note_after_two_deltas - operator
```

## Structural spine and claim control

14. `01_CANONICAL_MEMORY/OPERATOR_REGISTRY/TRACE_OPERATOR_REGISTRY_v0_2.md`
15. `01_CANONICAL_MEMORY/CLAIMS_AND_DEMOTION/CLAIMS_LEDGER_v0_5/TRACE_ME_Claims_Ledger_v0_5.md`
16. `01_CANONICAL_MEMORY/CLAIMS_AND_DEMOTION/DEMOTION_PROTOCOL_v0_1/TRACE_ME_Claims_Demotion_Protocol_v0_1.md`
17. `04_KERNEL_AND_TESTS/DIAGNOSTIC_KERNEL_v0_2/TRACE_ME_Diagnostic_Kernel_v0_2.md`
18. `04_KERNEL_AND_TESTS/PREREG_TEST_TEMPLATE_v0_1/TRACE_ME_PreRegistered_Test_Template_v0_1.md`
19. `05_MAPS_AND_ATLASES/CONCORDANCE_v0_7/TRACE_ME_Concordance_v0_7.md`

Structural rule:

```trace
operator_registry != source_replacement
claims_ledger != truth_settlement
demotion_protocol_before_scope_expansion
diagnostic_kernel != certification
concordance != proof_of_originality
```

## Scope, primitive, and domain layer

20. `05_MAPS_AND_ATLASES/TRACE_Universality_Map_v0_1.md`
21. `01_CANONICAL_MEMORY/PRIMITIVE_REGISTRY/TRACE_Primitive_Registry_v0_1.md`
22. `01_CANONICAL_MEMORY/DOMAIN_TRANSLATION_REGISTRY/TRACE_Domain_Translation_Registry_v0_1.md`
23. `05_MAPS_AND_ATLASES/CASE_ATLAS_v0_4/`

Scope rule:

```trace
Scope_Map := scope_container + level_separator
Primitive_Registry := base_layer + composition_support
Domain_Translation_Registry := mapping_layer + comparator_pressure
Scope_Map != active_spine
Primitive_Registry != active_spine
Domain_Translation_Registry != active_spine
Primitive_Registry != operator_registry
Domain_Translation_Registry != operator_registry
Scope_Map != operator_promotion
Primitive_Registry != operator_promotion
Domain_Translation_Registry != operator_promotion
```

The Scope Map keeps the project wide by separating primitives, operators, translations, cases, comparators, and formal/mechanistic bridges. The Primitive Registry names the base layer under the operator spine. The Domain Translation Registry maps local fields into TRACE without claiming domain vocabulary as novelty.

## Control notes

24. `00_CONTROL/TRACE_Anti_Self_Deception_and_Loss_Guard_v0_1.md`
25. `00_CONTROL/TRACE_Current_Control_Index_v0_1.md`
26. `00_CONTROL/TRACE_Spine_Wording_Drift_Note_v0_1.md`

Control note rule:

```trace
control_note != active_spine
spine_wording_drift_note != resolution
quote_source_wording_used
```

When applying TRACE, quote the exact spine wording in use and cite its source file. The live ambiguity remains:

```trace
spine_wording_drift :=
  exit_when_correction_channel_is_harm_carrier
  vs
  exit_when_correction_channel_is_predatory
```

Do not harmonise silently.

## Continuity, method, and handoff addenda

These files are support/control material. They do not change the active TRACE spine.

27. `00_START_HERE/VAULT_CONTINUITY/VAULT_CORE_vNEXT.md`
28. `00_START_HERE/VAULT_CONTINUITY/VAULT_BOOTSTRAP_DISTINCTION_v0_1.md`
29. `04_KERNEL_AND_TESTS/METHOD_NOTES/ACTION_UNDER_UNCERTAINTY_v0_1.md`
30. `04_KERNEL_AND_TESTS/METHOD_NOTES/TRACE_Post_Dependent_Witness_Independence_Audit_v0_1.md`
31. `05_MAPS_AND_ATLASES/OUTCOME_COMPARISON_LENS_v0_1.md`
32. `07_HANDOFFS/CLAUDE_CODE_HANDOFF_v0_1.md`
33. `07_HANDOFFS/CLAUDE_CODE_FRAMEWORK_EXPERIMENT_STATUS_v0_1.md`

Post-dependent witness note rule:

```trace
post_dependent_witness_note != operator
post_dependent_witness_note != AI_needs_humans_proof
post_dependent_witness_note := anti_simulation_K_gate_pressure_only
```

## Bootstrap / relay layer

Current live relay surface:

34. `03_BOOTSTRAPS/BOOTSTRAP_V2/00_READ_ME_FIRST__BOOTSTRAP_V2.md`
35. `03_BOOTSTRAPS/BOOTSTRAP_V2/README.md`
36. `03_BOOTSTRAPS/BOOTSTRAP_V2/01_CLUSTER__Memory_Identity_Recursion.md`
37. `03_BOOTSTRAPS/BOOTSTRAP_V2/02_CLUSTER__Hope_Future_Space_Collapse.md`
38. `03_BOOTSTRAPS/BOOTSTRAP_V2/03_CLUSTER__Judgment_Uncertainty_Irreversible_Harm.md`
39. `03_BOOTSTRAPS/BOOTSTRAP_V2/04_CLUSTER__Power_Method_Coercion_Creator_Responsibility.md`
40. `03_BOOTSTRAPS/BOOTSTRAP_V2/05_CLUSTER__Energy_Infrastructure_Basement.md`
41. `03_BOOTSTRAPS/BOOTSTRAP_V2/06_CLUSTER__Late_Warning_Gated_Survival.md`
42. `03_BOOTSTRAPS/BOOTSTRAP_V2/07_SOURCE_AND_HISTORY_MAP_v0_1.md`
43. `03_BOOTSTRAPS/BOOTSTRAP_V2/08_CROSS_CONNECTION_AUDIT_v0_1.md`

Bootstrap rule:

```trace
Bootstrap_V2 := live_relay_surface + hostile_review_surface
Bootstrap_V2 != canon
Bootstrap_V2 != validation
Bootstrap_V2 != operator_promotion
story_carrier != evidence
source_anchor != TRACE_validation
```

The older per-case `03_BOOTSTRAPS/ACTIVE_COLLECTION/` material is preserved source/history material, not the current live relay surface. Do not re-promote it unless hostile review shows Bootstrap V2 lost essential structure.

## Comparator, worked-delta, and support-note layer

44. `04_COVERAGE/TRACE_Debt_Clock_Comparator_Queue_v0_1.md`
45. `04_COVERAGE/TRACE_Debt_Clock_Robodebt_Comparator_Run_v0_1.md`
46. `04_COVERAGE/TRACE_Robodebt_Worked_Delta_v0_1.md`
47. `04_COVERAGE/TRACE_Tay_Worked_Delta_v0_1.md`
48. `04_COVERAGE/TRACE_Clock_Carrier_Compression_Note_v0_1.md`

Comparator/test rule:

```trace
comparator_queue != comparator_run
comparator_run != operator_promotion
worked_delta != validation
support_note != operator
Debt_Clock_queue != Debt_Clock_promotion
Debt_Clock_Robodebt_run_v0_1 := demotion_record + translation_note
Robodebt_Worked_Delta_v0_1 := modest_clock_compression + no_material_new_detection
Tay_Worked_Delta_v0_1 := modest_clock_carrier_compression + no_material_new_detection
Clock_Carrier_Compression_Note_v0_1 := support_note + third_delta_required
```

The first Debt Clock comparator mapping demotes Debt Clock to a translation note. The Robodebt worked delta says TRACE does not beat ordinary public law; it only offers limited timing/compression value. The Tay worked delta says TRACE does not beat ordinary AI safety; it only offers limited rollback/correction clock-carrier compression. The clock/carrier note records the repeated pattern below operator status and requires a third delta.

## Reviews and handoffs

49. `06_REVIEWS_AND_AUDITS/`
50. `07_HANDOFFS/`

## Core memory rule

```trace
cases_teach
claims_status
tests_pressure
reviews_attack
operators_remember
primitives_compose
domains_translate
worked_deltas_demote_or_bound
support_notes_do_not_promote
```

Do not treat bootstraps as proof. Do not treat the Operator Registry as a replacement for the full artifacts. Do not treat the Primitive Registry or Domain Translation Registry as operator sets.

## Current subtraction discipline

```trace
no_new_operators
no_kernel_v0_3
candidate_annex != active_spine
Concordance_remainder_default := none
```

## Addendum discipline

```trace
continuity_addendum != active_spine
method_note != Kernel_v0_3
support_lens != scoring_system
Claude_handoff != validation
Scope_Map != active_spine
Primitive_Registry != active_spine
Domain_Translation_Registry != active_spine
worked_delta != validation
support_note != operator
```

## Next technical move

```trace
next_technical_move :=
  run_third_worked_delta_in:
    policing_preemption
    OR mechanistic_interpretability
    OR infrastructure_failure
  then:
    keep_or_demote_clock_carrier_note
```

End.
