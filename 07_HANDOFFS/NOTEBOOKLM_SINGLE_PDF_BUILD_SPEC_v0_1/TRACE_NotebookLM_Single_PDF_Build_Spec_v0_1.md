# TRACE NotebookLM Single PDF Build Spec v0.1

Status: future build specification. Not a PDF. Not an export. Not a release package. This file exists because Mark wants, later, to give NotebookLM one large PDF containing as much of TRACE / Mechanical Ethics structure as possible and see what it makes of the whole project.

```trace
NotebookLM_Single_PDF_Build_Spec_v0_1 :=
  future_export_plan
  + ordering_logic
  + inclusion_rules
  + exclusion_rules
  + claim_control
  - actual_PDF
  - publication
  - validation
```

## Purpose

The eventual single PDF should let NotebookLM ingest the broadest useful structure without confusing status, treating drafts as proof, or collapsing live-use tools, atlases, reviews, and history into one undifferentiated canon.

```trace
purpose :=
  maximise_structure_visibility
  + minimise_status_confusion
  + preserve_claim_boundaries
  + expose_pressure_tests
```

Plain version: the PDF should show the project clearly, not flatter it.

## Build rule

Do not build the PDF automatically yet.

```trace
build_rule :=
  wait_until_requested
  + use_current_repo_state
  + include_manifest
  + preserve_file_paths
  + preserve_status_labels
```

## Proposed high-level PDF order

```trace
PDF_order :=
  cold_reader_front_door
  -> live_use_stack
  -> claim_control
  -> core_spine
  -> translation_and_scope
  -> atlases
  -> pressure_tests
  -> comparator_and_demotion_records
  -> hostile_reviews
  -> bootstrap_history
  -> manifest
```

## Section 1 — Cold reader front door

Include first:

1. `00_START_HERE/TRACE_FOR_NEW_READERS_v0_1.md`
2. `00_START_HERE/USE_TRACE_ON_ONE_PROBLEM_v0_1.md`
3. `00_START_HERE/WHAT_TRACE_IS_NOT_v0_1.md`
4. `00_START_HERE/START_HERE_NOW_v0_1.md`
5. `00_START_HERE/READ_ORDER.md`

Reason:

```trace
front_door_reason :=
  reader_needs_entry
  + use_before_theory
  + claim_boundaries_before_depth
```

## Section 2 — Live-use stack

Include:

1. `02_CURRENT_SURFACE/LIVE_USE_CARD_v0_2_1/TRACE_LIVE_USE_CARD_v0_2_1.md`
2. `02_CURRENT_SURFACE/PRE_ESCALATION_GUARD_v0_1/TRACE_Pre_Escalation_Guard_v0_1.md`
3. `02_CURRENT_SURFACE/LAST_TOUCH_LOCAL_FIX_SWEEP_v0_1/TRACE_Last_Touch_Local_Fix_Sweep_v0_1.md`
4. `02_CURRENT_SURFACE/REAL_USE_CAPTURE_v0_1/TRACE_Real_Use_Capture_Sheet_v0_1.md`
5. `02_CURRENT_SURFACE/REAL_USE_CAPTURE_v0_1/TRACE_Real_Use_Capture__Energy_Switch_2026_06_19_v0_1.md`

Reason:

```trace
live_use_reason :=
  shows_TRACE_as_tool
  + preserves_real_use_signal
  + prevents_theory_only_read
```

## Section 3 — Claim control and spine discipline

Include:

1. `00_CONTROL/TRACE_Current_Control_Index_v0_1.md`
2. `00_CONTROL/TRACE_Anti_Self_Deception_and_Loss_Guard_v0_1.md`
3. `00_CONTROL/TRACE_Spine_Wording_Drift_Note_v0_1.md`
4. `00_CONTROL/TRACE_Kimi_Break_Register_v0_1.md`
5. `01_CANONICAL_MEMORY/CLAIMS_AND_DEMOTION/CLAIMS_LEDGER_v0_5/TRACE_ME_Claims_Ledger_v0_5.md`
6. `01_CANONICAL_MEMORY/CLAIMS_AND_DEMOTION/DEMOTION_PROTOCOL_v0_1/TRACE_ME_Claims_Demotion_Protocol_v0_1.md`
7. `01_CANONICAL_MEMORY/OPERATOR_REGISTRY/TRACE_OPERATOR_REGISTRY_v0_2.md`

Reason:

```trace
claim_control_reason :=
  stop_validation_drift
  + show_demotion_discipline
  + keep_operator_status_bounded
```

## Section 4 — Diagnostic kernel and test scaffolding

Include:

1. `04_KERNEL_AND_TESTS/DIAGNOSTIC_KERNEL_v0_2/TRACE_ME_Diagnostic_Kernel_v0_2.md`
2. `04_KERNEL_AND_TESTS/PREREG_TEST_TEMPLATE_v0_1/TRACE_ME_PreRegistered_Test_Template_v0_1.md`

Reason:

```trace
kernel_reason :=
  expose_core_test_surface
  + prevent_atlas_material_from_becoming_spine
```

## Section 5 — Translation and scope maps

Include:

1. `05_MAPS_AND_ATLASES/TRACE_Universality_Map_v0_1.md`
2. `05_MAPS_AND_ATLASES/TRACE_AI_Alignment_MI_Translation_Bridge_v0_1.md`
3. `01_CANONICAL_MEMORY/PRIMITIVE_REGISTRY/TRACE_Primitive_Registry_v0_1.md`
4. `01_CANONICAL_MEMORY/DOMAIN_TRANSLATION_REGISTRY/TRACE_Domain_Translation_Registry_v0_1.md`
5. `05_MAPS_AND_ATLASES/CONCORDANCE_v0_7/TRACE_ME_Concordance_v0_7.md`

Reason:

```trace
translation_reason :=
  show_cross_domain_ambition
  + preserve_scope_limits
  + expose_external_overlap_and_non_originality_risk
```

## Section 6 — Positive systems atlas

Include:

1. `05_MAPS_AND_ATLASES/POSITIVE_TRACE_ATLAS_v0_1/TRACE_Positive_TRACE_Atlas_v0_1.md`
2. `05_MAPS_AND_ATLASES/POSITIVE_TRACE_ATLAS_v0_1/TRACE_Positive_Primitive_Demoter_Table_v0_1.md`

Reason:

```trace
positive_reason :=
  show_what_TRACE_protects
  + prevent_harm_only_read
  + preserve_life_conditions
```

## Section 7 — Life / Biology / Ecology atlas

Include:

1. `05_MAPS_AND_ATLASES/LIFE_BIOLOGY_ECOLOGY_ATLAS_v0_1/README.md`
2. `05_MAPS_AND_ATLASES/LIFE_BIOLOGY_ECOLOGY_ATLAS_v0_1/TRACE_Life_Biology_Ecology_Atlas_v0_1.md`
3. `05_MAPS_AND_ATLASES/LIFE_BIOLOGY_ECOLOGY_ATLAS_v0_1/TRACE_Life_Primitive_Demoter_Table_v0_1.md`
4. `05_MAPS_AND_ATLASES/LIFE_BIOLOGY_ECOLOGY_ATLAS_v0_1/TRACE_Ecology_Hidden_Bill_Note_v0_1.md`
5. `05_MAPS_AND_ATLASES/LIFE_BIOLOGY_ECOLOGY_ATLAS_v0_1/TRACE_Predation_Symbiosis_Contrast_v0_1.md`

Reason:

```trace
life_reason :=
  ground_TRACE_in_bodies_ecology_repair_and_death
  + block_biology_as_decorative_metaphor
```

## Section 8 — Agency / Free Will / Mandelbrot atlas

Include:

1. `05_MAPS_AND_ATLASES/AGENCY_FREE_WILL_MANDELBROT_ATLAS_v0_1/README.md`
2. `05_MAPS_AND_ATLASES/AGENCY_FREE_WILL_MANDELBROT_ATLAS_v0_1/TRACE_Agency_Free_Will_Mandelbrot_Atlas_v0_1.md`
3. `05_MAPS_AND_ATLASES/AGENCY_FREE_WILL_MANDELBROT_ATLAS_v0_1/TRACE_Agency_Primitive_Demoter_Table_v0_1.md`

Reason:

```trace
agency_reason :=
  show_choice_without_free_will_overclaim
  + map_responsibility_under_constraint
  + control_Mandelbrot_language
```

## Section 9 — Cross-atlas pressure tests

Include:

1. `05_MAPS_AND_ATLASES/CROSS_ATLAS_PRESSURE_TESTS_v0_1/README.md`
2. `05_MAPS_AND_ATLASES/CROSS_ATLAS_PRESSURE_TESTS_v0_1/TRACE_Cross_Atlas_Pressure_Test_WALL_E_v0_1.md`
3. `05_MAPS_AND_ATLASES/CROSS_ATLAS_PRESSURE_TESTS_v0_1/TRACE_Cross_Atlas_Pressure_Test_Maisie_v0_1.md`

Reason:

```trace
pressure_reason :=
  test_whether_atlases_add_structure
  + prevent_pretty_language_sprawl
```

## Section 10 — Comparator / worked-delta / demotion record

Include selected files only:

1. `04_COVERAGE/TRACE_Debt_Clock_Comparator_Queue_v0_1.md`
2. `04_COVERAGE/TRACE_Debt_Clock_Robodebt_Comparator_Run_v0_1.md`
3. `04_COVERAGE/TRACE_Robodebt_Worked_Delta_v0_1.md`
4. `04_COVERAGE/TRACE_Tay_Worked_Delta_v0_1.md`
5. `04_COVERAGE/TRACE_CrowdStrike_Worked_Delta_v0_1.md`
6. `04_COVERAGE/TRACE_Clock_Carrier_Compression_Note_v0_1.md`
7. `04_COVERAGE/TRACE_Clock_Carrier_Compression_Note_v0_1_PATCH_after_CrowdStrike.md`
8. `04_COVERAGE/TRACE_Bootstrap_Worked_Navigation_Comparison_Apollo13_v0_1.md`

Reason:

```trace
worked_delta_reason :=
  show_demotion_record
  + show_where_decision_advantage_was_not_proven
  + preserve_honesty
```

## Section 11 — Reviews and hostile compression

Include:

1. `06_REVIEWS_AND_AUDITS/TRACE_Atlas_Expansion_Hostile_Compression_Pass_v0_1.md`
2. Any current hostile reviews that directly changed claims or structure.

Do not include every review loop automatically.

```trace
review_inclusion_rule :=
  include_if_changed_claim_or_structure
  exclude_if_only_praise_or_repeat
```

## Section 12 — Bootstrap / history layer

Include selectively. Full bootstrap material may be too large and may confuse source/history with current status.

Suggested include:

1. `03_BOOTSTRAPS/BOOTSTRAP_V2/00_READ_ME_FIRST__BOOTSTRAP_V2.md`
2. `03_BOOTSTRAPS/BOOTSTRAP_V2/README.md`
3. `03_BOOTSTRAPS/BOOTSTRAP_V2/07_SOURCE_AND_HISTORY_MAP_v0_1.md`
4. `03_BOOTSTRAPS/BOOTSTRAP_V2/08_CROSS_CONNECTION_AUDIT_v0_1.md`

Optional if space permits:

```trace
optional_bootstrap_clusters :=
  Memory_Identity_Recursion
  + Hope_Future_Space_Collapse
  + Judgment_Uncertainty_Irreversible_Harm
  + Power_Method_Coercion_Creator_Responsibility
  + Energy_Infrastructure_Basement
  + Late_Warning_Gated_Survival
```

## Section 13 — Manifest and hashes

The final PDF should end with:

```trace
manifest :=
  file_list
  + source_paths
  + commit_or_export_date
  + known_exclusions
  + status_warning
```

This matters because NotebookLM output may sound authoritative. It needs a visible source ledger.

## Exclusion rules

Exclude:

```trace
exclude :=
  duplicate_exports
  + obsolete_packet_copies
  + raw_chat_transcripts_unless_needed
  + praise_only_reviews
  + files_marked_archive_if_current_equivalent_exists
  + private_material_not_needed_for_structure
```

Do not include private medical/veterinary detail beyond already-structural summaries unless Mark explicitly approves.

## Required warning page

The PDF should include a first-page warning:

```trace
warning :=
  this_document_is_a_working_research_bundle
  + not_validation
  + not_policy_or_medical_or_legal_advice
  + not_a_finished_ethics_theory
  + NotebookLM_summary_may_overstate_coherence
```

Plain wording:

This bundle is a structured working record of TRACE / Mechanical Ethics. It is intended for summarisation and stress-reading, not as proof that the framework is correct.

## NotebookLM prompt candidate

When the PDF exists, use a prompt like:

```trace
NotebookLM_task :=
  summarise_structure
  + identify_repeated_primitives
  + identify_claim_overreach
  + identify_status_confusion
  + identify_best_public_front_door
  + identify_what_to_cut
  + do_not_treat_internal_reviews_as_validation
```

Plain prompt:

Read this as a hostile but fair structural auditor. Explain what TRACE / Mechanical Ethics is trying to do, what its strongest recurring primitives are, where it overclaims, where status is confusing, what a new reader should open first, and what should be cut or demoted. Do not treat AI review agreement, worked examples, or internal coherence as validation.

## Build conditions

Only build the PDF when:

```trace
build_conditions :=
  Mark_requests_export
  + current_front_door_stable
  + major_new_files_paused
  + source_list_reviewed
```

## Current recommendation

Do not build now.

```trace
current_recommendation :=
  preserve_spec
  + wait
  + continue_using_front_door_and_pressure_tests
```

End.
