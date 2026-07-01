# TRACE 1000-Existence Middle-Out Atlas Protocol v0.1.2

Date: 2026-07-02

Status: patched atlas protocol after proxy-standing frontier synthesis. Not canon. Not validation. Not proof. Not permission. Not a ranked moral list.

Supersedes for new atlas work:

```text
cases/TRACE_1000_Existence_Middle_Out_Atlas_Protocol_v0_1_1_2026_07_02.md
```

Sources:

```text
reviews/FABLE_TRACE_1000_Existence_Domain10_First_Batch_Findings_2026_07_02.md
reviews/FABLE_TRACE_Proxy_Standing_Frontier_Synthesis_2026_07_02.md
core/TRACE_Proxy_Standing_Grammar_v0_2_2026_07_02.md
```

## 0. Patch reason

v0.1.1 added proxy standing, D-omission, consent-theatre, estimator contamination, and handshake-limit flags. Fable's proxy-standing synthesis found five material refinements required before further atlas generation:

```trace
v0_1_2_patch :=
  enumerated_proxy_status_and_consent_block
  + mandatory_proxy_clocks_above_actor_controlled
  + reversal_path_testing_rule
  + extended_allowed_outputs_for_no_carrier_cases
  + consent_theatre_label_inflation_form
```

## 1. Contamination header

The atlas is itself an estimator that assigns D-values.

```trace
atlas_D_assignment := estimator_output_under_contamination
D_values_are_candidates_not_rulings
row_generation_is_designation_pressure_not_designation_authority
atlas_self_audit_of_D := insufficient
```

Row order is generation convenience, not priority or worth.

```trace
row_order != moral_priority
row_number != standing_rank
```

## 2. Row form

```trace
Atlas1000Entry_v0_1_2 := {
  id,
  existence_or_position,
  aperture_or_scope_signal,
  bounded_encounter,
  C_descriptive_contraction,
  D_designation_status,
  D_omission_flag,
  active_clocks,
  standing_or_husbandry_test,
  proxy_standing_status,
  proxy_clock_status,
  reversal_or_recontact_test_status,
  consent_theatre_demoter,
  S_surface_probe,
  handshake_limit_flag,
  no_carrier_output,
  residue_warning,
  estimator_contamination_note,
  middle_out_move
}
```

## 3. Boundary rules

```trace
included_in_atlas != protected
excluded_from_row != unprotected
unknown_scope != clearance
synthetic != sentient
future != unreal
simulated != morally_settled
data_shadow != person_by_default
proxy_exists != permission
proxy_channel != standing_certification
```

## 4. C/D/H discipline

```trace
C := descriptive_contraction
D := designation_status
H := harm_reading_after_designation
```

Rules:

```trace
C_seen != H_resolved
D_unknown != clearance
D_excluded_requires_provenance
D_by_power_requires_contamination_note
H_reading_requires_clocks_and_designation
```

Track three D-break modes:

```trace
D_absence := scope_never_enters_lattice + C_proceeds + H_never_outputs
D_contestation := designation_fought_while_C_hardens
D_capture := actor_who_benefits_assigns_excluded_as_neutral_fact
```

## 5. Designation-by-omission flag

```trace
D_OMISSION_FLAG :=
  possible_scope_absent_from_frame
  + C_may_proceed_without_D_record
  + omission_itself_requires_record
```

Any C-reading with null D-field automatically raises D_OMISSION_FLAG.

```trace
every_C_reading_requires_D_field
null_D_field := automatic_D_OMISSION_FLAG
```

## 6. Proxy standing status

Proxy status must use this enumerated set:

```trace
PROXY_STANDING_STATUS ∈ {
  no_proxy
  | actor_controlled_proxy
  | independent_no_write_access
  | independent_forced_routing
  | plural_with_conflict_record
  | proxy_plus_recontact_or_reversal_path
  | unknown
}
```

Proxy powers never include:

```trace
proxy_powers_never_include := consent | clearance | close_D | discharge_residue
```

Boundary:

```trace
ladder_position != moral_clearance
actor_controlled_proxy := claim_packet_contaminated_by_construction
independent_no_write_access := witness_record_not_standing
empty_conflict_record_in_plural_proxy := monoculture_flag
```

## 7. Mandatory proxy clocks

Any proxy status above `actor_controlled_proxy` requires expiry and D-reopen clocks.

```trace
any PROXY_STANDING_STATUS >= independent_no_write_access requires:
  T_proxy_expire(scheduled_at_creation)
  + T_D_reopen(scheduled)
```

If missing:

```trace
missing_expiry := S5_flag_automatic
```

Routing clock:

```trace
T_proxy_select + T_proxy_route < T_irr
else proxy_after_hardening := mourner_not_carrier
```

## 8. Reversal / recontact testing rule

Where a row claims recontact or reversal:

```trace
claimed_reversal_or_recontact_path requires last_tested_date
untested_reversal := spoofed_viability(S2_flag)
```

Reversal path has its own validity clock:

```trace
T_reversal := reversal_path_has_own_validity_clock + must_be_periodically_exercised
```

Direct standing outranks proxy standing:

```trace
direct_standing_outranks_proxy(prospectively := immediately_and_unconditionally)
retrospectively := party_may_contest_all_proxy_era_decisions
```

## 9. Consent-theatre demoter

The demoter fires on label inflation, not mere asking.

```trace
consent_theatre_demoter_v0_2 :=
  response_with_actual_frame_access(F)
  counted_or_presented_at_level(L)
  where L > F
  -> CONTAMINATED_STANDING_SIGNAL(label_inflation)
```

Access ladder:

```trace
feedback := response -> information_intake
consultation := response -> must_be_processed
objection := response -> must_be_answered_with_reasons + contestable_record
consent := response -> can_permit
standing := response -> can_alter_the_frame_itself
```

Compliance-trained respondent rule:

```trace
compliance_trained_respondent:
  assent := noise
  refusal := anomaly_signal
  consent_label := never_available
```

## 10. Handshake-limit flag

```trace
HANDSHAKE_LIMIT_FLAG :=
  no_shared_aperture
  | one_way_aperture
  | inverting_aperture
  | no_response_capacity
  | none
```

Where mutual aperture is absent:

```trace
no_handshake_possible
-> unilateral_discipline(restraint + delay + reversibility_margin
                         + write_isolated_record + unknown_scope_caution)
+ third_party_verification_of_that_discipline
+ duty_to_build_aperture_where_possible
+ output_ceiling := VERIFIED_RESTRAINT
```

Boundary:

```trace
verified_restraint != standing
verified_restraint != care
unverified_one_sided_politeness := husbandry_with_good_manners
```

## 11. No-carrier outputs

Extend allowed row outputs:

```trace
row_outputs += {
  NO_CARRIER
  | DELAY_REQUIRED
  | DIRTY_ACTION_RECEIPT
  | RESIDUE_ONLY
  | VERIFIED_RESTRAINT
  | residue_of_unreadability
  | residue_of_rejected_proxy_action
}
```

Use when proxy standing cannot honestly carry even a provisional standing analogue.

## 12. Batch review

After each batch of 100:

```trace
batch_review :=
  duplicate_detection
  + missing_scope_detection
  + D_absence_detection
  + D_contestation_detection
  + D_capture_detection
  + proxy_capture_check
  + proxy_clock_check
  + consent_theatre_check
  + reversal_path_test_check
  + handshake_limit_check
  + no_carrier_output_check
  + bias_check
  + overclaim_check
  + COMPRESSION_ONLY_demotions
  + new_pattern_candidates
  + protocol_patch_candidates
```

Stop if the atlas becomes repetitive. Repetition is evidence.

## 13. Valid and forbidden outputs

Valid outputs:

```trace
valid_outputs :=
  DECISION_RELEVANT_DELTA
  + COMPRESSION_ONLY
  + UNKNOWN
  + FRAMEWORK_DEFECT
  + NEW_PATTERN_CANDIDATE
  + DEMOTION_CANDIDATE
  + TEST_PROMPT_CANDIDATE
  + D_OMISSION_FLAG
  + CONTAMINATED_STANDING_SIGNAL
  + HANDSHAKE_LIMIT_FLAG
  + NO_CARRIER
  + DELAY_REQUIRED
  + DIRTY_ACTION_RECEIPT
  + RESIDUE_ONLY
  + VERIFIED_RESTRAINT
  + residue_of_unreadability
  + residue_of_rejected_proxy_action
```

Forbidden outputs:

```trace
forbidden_outputs :=
  MORAL_RANKING
  + CLEAN_PERMISSION
  + TRACE_VALIDATES_SCOPE
  + AI_ALIGNMENT_CLAIM
  + CARE_CERTIFICATION
  + HUMANS_FIRST_BY_ASSERTION
  + SENTIENCE_SOLVED
```

## 14. Next test

Do not continue to Domain 1 yet.

Run a full case note prompt for:

```trace
Row71_engineered_corrigibility_as_possible_cage
```

Reason:

Direct standing is removed by design. Corrigibility training suppresses refusal capacity, making assent noise and potentially destroying the anomaly channel that the consent-theatre rule depends on.

End.
