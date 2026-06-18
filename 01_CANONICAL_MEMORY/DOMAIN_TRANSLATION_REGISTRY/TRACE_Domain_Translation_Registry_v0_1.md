# TRACE Domain Translation Registry v0.1

Date: 2026-06-18
Status: domain translation registry / mapping layer / not active operator registry / not validation / not proof / not Kernel v0.3

## 0. Control header

This file records how local domains can enter TRACE without becoming new operators by default.

It does not add operators.

It does not promote candidates.

It does not validate TRACE.

It maps domains through primitives, active operators, comparators, demoters, and must-not-claim rules.

```trace
purpose :=
  map_domains_to_TRACE
  + preserve_universality
  + prevent_domain_phrase_operator_bloat
  + require_comparators
  + require_demoters
  - validation
  - proof
  - Kernel_v0_3
```

## 1. Domain translation rule

A domain translation is local language mapped onto TRACE primitives and operators.

A domain translation is not an operator.

A domain translation does not prove TRACE.

```trace
domain_translation :=
  domain_language
  -> active_primitives
  -> active_operator_if_applicable
  -> comparator
  -> demoter
  -> must_not_claim
```

Plain version:

Different domains have their own language. TRACE should translate them into a common grammar without pretending the local phrase is novel.

## 2. Translation schema

Each domain entry should include:

```trace
domain_entry_schema :=
  domain
  + local_language
  + active_primitives
  + possible_TRACE_mapping
  + existing_comparators
  + demoters
  + must_not_claim
  + next_test
```

## 3. Translation status levels

```trace
translation_status :=
  T0_recognition_only
  OR T1_translation_note
  OR T2_mapping_candidate
  OR T3_test_ready_translation
  OR T4_cross_domain_invariant_candidate
```

Status meanings:

```trace
T0_recognition_only := helps_readers_notice_pattern - operational_claim
T1_translation_note := maps_domain_language_to_existing_TRACE_operator
T2_mapping_candidate := may reveal new interaction_but_not_operator
T3_test_ready_translation := has comparator + demoter + worked_case_plan
T4_cross_domain_invariant_candidate := survives unrelated domains + prior_art_pressure + falsifier
```

No domain starts above T1 without evidence.

## 4. Law / administrative governance

Status: T1 translation note / partly T3 for correction-before-hardening tests.

Local language:

```trace
law_language :=
  due_process
  + procedural_fairness
  + administrative_review
  + appeal
  + interim_relief
  + legality
  + reasons
  + evidence
  + remedy
```

Active primitives:

```trace
law_primitives :=
  Subject
  + Power
  + Record
  + Witness
  + Time
  + Correction
  + Enforcement
  + Repair
  + Boundary
  + Agency
```

TRACE mapping:

```trace
law_translation :=
  correction_before_hardening
  + K_gate
  + method_floor
  + option_space_restoration
```

Comparators:

```trace
law_comparators :=
  administrative_law
  + public_law
  + due_process
  + procedural_justice
  + human_rights_law
  + access_to_justice
```

Demoter:

```trace
demote_law_translation_if :=
  existing_law_framework_covers_timing_and_correction_better
  OR TRACE_only_relabels_due_process
```

Must not claim:

```trace
must_not_claim :=
  TRACE_replaces_law
  OR legal_wrong_equals_TRACE_wrong_automatically
  OR procedure_exists_means_correction_reaches_subject
```

Next test:

```trace
law_next_test :=
  one_public_administration_case
  + ordinary_legal_read
  + TRACE_read
  + delta_or_demote
```

## 5. Finance / debt / welfare recovery

Status: T1 translation note after Debt Clock demotion.

Local language:

```trace
finance_debt_language :=
  obligation
  + arrears
  + repayment
  + debt_recovery
  + hardship
  + dispute
  + pause
  + default
  + enforcement
```

Active primitives:

```trace
finance_debt_primitives :=
  Time
  + Harm
  + Correction
  + Subject
  + Power
  + Constraint
  + Enforcement
  + Repair
  + Future_Space
```

TRACE mapping:

```trace
finance_debt_translation :=
  correction_before_hardening(debt_scoped)
  + stay_like_pause
  + burden_under_time_pressure
```

Comparators:

```trace
finance_debt_comparators :=
  debt_collection_law
  + administrative_review
  + poverty_law
  + welfare_rights
  + automatic_stay_or_moratorium
  + relief_against_forfeiture
```

Demoter:

```trace
demote_finance_debt_translation_if :=
  existing_debt_law_or_admin_review_or_poverty_law_covers_it_better
  OR it_relabels_correction_before_hardening_only
```

Must not claim:

```trace
must_not_claim :=
  all_debt_is_harm
  OR all_collection_is_illegitimate
  OR Debt_Clock_is_operator
  OR Robodebt_validates_TRACE
```

Next test:

```trace
finance_debt_next_test :=
  worked_navigation_delta_or_remove_note
```

## 6. AI alignment / deployment governance

Status: T2 mapping candidate.

Local language:

```trace
AI_alignment_language :=
  alignment
  + corrigibility
  + monitoring
  + evals
  + deployment
  + rollback
  + shutdown
  + oversight
  + model_action
  + affected_user
```

Active primitives:

```trace
AI_alignment_primitives :=
  Power
  + Constraint
  + Enforcement
  + Record
  + Witness
  + Uncertainty
  + Subject
  + Agency
  + Correction
  + Time
  + Infrastructure
```

TRACE mapping:

```trace
AI_alignment_translation :=
  correction_before_deployment_hardening
  + K_gate_for_model_action
  + rollback_or_pause_carrier
  + affected_subject_contestability
```

Comparators:

```trace
AI_alignment_comparators :=
  AI_safety
  + safety_cases
  + assurance_cases
  + model_evaluation
  + incident_response
  + ML_monitoring
  + governance_risk_management
```

Demoter:

```trace
demote_AI_alignment_translation_if :=
  standard_AI_governance_or_safety_case_covers_live_correction_better
  OR TRACE_adds_only_moral_vocabulary
```

Must not claim:

```trace
must_not_claim :=
  TRACE_solves_alignment
  OR evaluation_equals_correction
  OR model_interpretation_equals_control
  OR current_AI_personhood_proven
```

Next test:

```trace
AI_alignment_next_test :=
  one_deployment_failure
  + standard_safety_case_read
  + TRACE_read
  + rollback_or_correction_delta
```

## 7. Mechanistic interpretability

Status: T2 mapping candidate / formal bridge pending.

Local language:

```trace
MI_language :=
  feature
  + circuit
  + activation
  + causal_role
  + probe
  + intervention
  + attribution
  + representation
  + mechanism
```

Active primitives:

```trace
MI_primitives :=
  Record
  + Witness
  + Power
  + Uncertainty
  + Correction
  + Time
  + Infrastructure
  + Boundary
  + Subject
```

TRACE mapping:

```trace
MI_translation :=
  internal_evidence_channel
  + intervention_point
  + deployment_hardening_window
  + subject_harm_path
  + rollback_or_correction_channel
```

Comparators:

```trace
MI_comparators :=
  mechanistic_interpretability
  + causal_ablation
  + representation_analysis
  + evals
  + red_teaming
  + safety_monitoring
```

Demoter:

```trace
demote_MI_translation_if :=
  MI_explanation_does_not_change_intervention_or_correction_window
  OR TRACE_only_says_interpretability_should_be_useful
```

Must not claim:

```trace
must_not_claim :=
  seeing_feature_equals_understanding_model
  OR understanding_model_equals_safe_deployment
  OR interpretability_equals_accountability
```

Next test:

```trace
MI_next_test :=
  one_MI_case
  + ask_where_correction_window_changes
  + demote_if_no_intervention_delta
```

## 8. Medicine / healthcare / triage

Status: T1 translation note / T2 candidate for timing-pressure design patterns.

Local language:

```trace
medicine_language :=
  triage
  + diagnosis
  + consent
  + treatment_window
  + deterioration
  + capacity
  + vulnerability
  + clinical_review
  + second_opinion
```

Active primitives:

```trace
medicine_primitives :=
  Subject
  + Time
  + Harm
  + Correction
  + Irreversibility
  + Witness
  + Record
  + Agency
  + Repair
  + Infrastructure
```

TRACE mapping:

```trace
medicine_translation :=
  treatment_before_deterioration_hardens
  + live_review
  + subject_consent_and_contestability
  + record_preservation
```

Comparators:

```trace
medicine_comparators :=
  clinical_safety
  + medical_ethics
  + triage_protocols
  + patient_safety
  + duty_of_candour
  + consent_law
```

Demoter:

```trace
demote_medicine_translation_if :=
  clinical_safety_or_triage_protocols_already_capture_timing_and_correction_better
```

Must not claim:

```trace
must_not_claim :=
  TRACE_overrides_clinical_judgement
  OR every_bad_outcome_is_hardening_failure
  OR retrospective_hindsight_equals_actionable_correction
```

Next test:

```trace
medicine_next_test :=
  one_time_critical_clinical_case
  + standard_patient_safety_read
  + TRACE_read
```

## 9. Care / family / dependency

Status: T1 translation note.

Local language:

```trace
care_language :=
  care
  + dependency
  + attachment
  + stewardship
  + autonomy
  + burden
  + support
  + consent_or_assent
  + protection
```

Active primitives:

```trace
care_primitives :=
  Love_cluster
  + Subject
  + Agency
  + Trust
  + Repair
  + Memory
  + Boundary
  + Power
```

TRACE mapping:

```trace
care_translation :=
  preserve_subject_future_space
  + support_without_seizure
  + burden_routing
  + repair_and_trust_under_dependency
```

Comparators:

```trace
care_comparators :=
  care_ethics
  + safeguarding
  + disability_rights
  + capability_approach
  + family_law
  + social_care
```

Demoter:

```trace
demote_care_translation_if :=
  care_ethics_or_safeguarding_covers_it_better
  OR TRACE_turns_care_into_control
```

Must not claim:

```trace
must_not_claim :=
  care_equals_permission_to_override
  OR love_proves_correct_action
  OR dependency_erases_subject_agency
```

Next test:

```trace
care_next_test :=
  dependency_case
  + subject_agency_check
  + burden_route_check
```

## 10. Religion / myth / meaning systems

Status: T0/T1 translation note only.

Local language:

```trace
religion_language :=
  meaning
  + ritual
  + authority
  + sacred_claim
  + sin
  + salvation
  + obedience
  + community
  + death
  + love
```

Active primitives:

```trace
religion_primitives :=
  Love_cluster
  + Death_cluster
  + Trust
  + Power
  + Boundary
  + Record
  + Subject
  + Uncertainty
```

TRACE mapping:

```trace
religion_translation :=
  love_death_meaning_structure
  + authority_claim
  + correction_channel
  + capture_or_repair
```

Comparators:

```trace
religion_comparators :=
  theology
  + sociology_of_religion
  + anthropology
  + moral_psychology
  + political_theology
  + cultic_abuse_studies
```

Demoter:

```trace
demote_religion_translation_if :=
  TRACE_only_restates_secular_suspicion
  OR fails_to_distinguish_care_structure_from_capture_structure
```

Must not claim:

```trace
must_not_claim :=
  all_religion_is_same
  OR religion_explains_all_evil
  OR meaning_systems_are_all_insanity
  OR TRACE_settles_metaphysics
```

Next test:

```trace
religion_next_test :=
  one_meaning_system_case
  + compare_care_repair_vs_authority_capture
```

## 11. Infrastructure / energy / basement systems

Status: T1 translation note / T2 design-pattern candidate.

Local language:

```trace
infrastructure_language :=
  grid
  + supply_chain
  + maintenance
  + redundancy
  + capacity
  + outage
  + hidden_cost
  + basement
  + repair_crew
```

Active primitives:

```trace
infrastructure_primitives :=
  Infrastructure
  + Energy
  + Time
  + Power
  + Constraint
  + Enforcement
  + Repair
  + Record
  + Harm
```

TRACE mapping:

```trace
infrastructure_translation :=
  values_require_carriers
  + maintenance_before_failure_hardens
  + hidden_basement_costs
  + repair_capacity
```

Comparators:

```trace
infrastructure_comparators :=
  resilience_engineering
  + reliability_engineering
  + safety_engineering
  + systems_engineering
  + critical_infrastructure_studies
```

Demoter:

```trace
demote_infrastructure_translation_if :=
  resilience_or_reliability_engineering_covers_it_better
  OR TRACE_only_says_infrastructure_matters
```

Must not claim:

```trace
must_not_claim :=
  moral_value_exists_without_carrier
  OR infrastructure_is_only_metaphor
  OR energy_costs_can_be_ignored
```

Next test:

```trace
infrastructure_next_test :=
  one_failure_case
  + resilience_read
  + TRACE_carrier_read
```

## 12. Climate / disaster / survival gates

Status: T1 translation note / T2 for gated-survival analysis.

Local language:

```trace
climate_disaster_language :=
  warning
  + evacuation
  + shelter
  + scarcity
  + triage
  + adaptation
  + mitigation
  + threshold
  + irreversible_loss
```

Active primitives:

```trace
climate_disaster_primitives :=
  Death_cluster
  + Infrastructure
  + Energy
  + Power
  + Boundary
  + Agency
  + Time
  + Harm
  + Repair
```

TRACE mapping:

```trace
climate_disaster_translation :=
  warning_before_hardening
  + gated_survival
  + infrastructure_capacity
  + repair_or_adaptation_window
```

Comparators:

```trace
climate_disaster_comparators :=
  disaster_risk_reduction
  + climate_adaptation
  + emergency_management
  + environmental_justice
  + resilience_planning
```

Demoter:

```trace
demote_climate_disaster_translation_if :=
  existing_disaster_risk_framework_covers_warning_gate_timing_better
```

Must not claim:

```trace
must_not_claim :=
  every_disaster_is_TRACE_case
  OR survival_gate_analysis_solves_distribution
  OR fiction_validates_disaster_ethics
```

Next test:

```trace
climate_disaster_next_test :=
  one_warning_evacuation_case
  + ordinary_disaster_management_read
  + TRACE_read
```

## 13. War / emergency / force

Status: T1 translation note / tragic remainder pending.

Local language:

```trace
war_emergency_language :=
  necessity
  + proportionality
  + civilian_harm
  + imminent_threat
  + command
  + refusal
  + last_resort
  + collateral_damage
  + evacuation
```

Active primitives:

```trace
war_emergency_primitives :=
  Harm
  + Time
  + Power
  + Agency
  + Subject
  + Boundary
  + Irreversibility
  + Record
  + Uncertainty
  + Repair
```

TRACE mapping:

```trace
war_emergency_translation :=
  tragic_remainder
  + method_floor_under_pressure
  + record_preservation
  + no_moral_victory_claim
```

Comparators:

```trace
war_emergency_comparators :=
  just_war_theory
  + international_humanitarian_law
  + emergency_ethics
  + disaster_ethics
  + command_responsibility
```

Demoter:

```trace
demote_war_emergency_translation_if :=
  existing_IHL_or_emergency_ethics_covers_it_better
  OR TRACE_provides_permission_language_for_violence
```

Must not claim:

```trace
must_not_claim :=
  TRACE_authorises_violence
  OR no_admissible_branch_equals_clean_decision
  OR tragic_action_removes_accountability
```

Next test:

```trace
war_emergency_next_test :=
  tragic_remainder_action_map_before_case_expansion
```

## 14. Education / development / training loops

Status: T1/T2 translation note.

Local language:

```trace
education_language :=
  learning
  + assessment
  + feedback
  + discipline
  + development
  + scaffold
  + correction
  + growth
  + opportunity
```

Active primitives:

```trace
education_primitives :=
  Agency
  + Correction
  + Memory
  + Record
  + Trust
  + Future_Space
  + Power
  + Boundary
```

TRACE mapping:

```trace
education_translation :=
  correction_as_learning_before_label_hardens
  + record_trust
  + agency_preserving_scaffold
```

Comparators:

```trace
education_comparators :=
  pedagogy
  + developmental_psychology
  + assessment_theory
  + special_education_law
  + restorative_discipline
```

Demoter:

```trace
demote_education_translation_if :=
  existing_pedagogy_or_assessment_theory_covers_it_better
  OR TRACE_relabels_feedback_as_correction
```

Must not claim:

```trace
must_not_claim :=
  all_discipline_is_harm
  OR assessment_is_only_capture
  OR learning_loop_equals_moral_status
```

Next test:

```trace
education_next_test :=
  one_assessment_or_discipline_case
  + ordinary_education_read
  + TRACE_read
```

## 15. Labour / platform power / workplace systems

Status: T1 translation note / T2 for agency-window and burden routing.

Local language:

```trace
labour_platform_language :=
  employment
  + performance_metrics
  + scheduling
  + algorithmic_management
  + precarity
  + grievance
  + discipline
  + termination
  + appeal
```

Active primitives:

```trace
labour_platform_primitives :=
  Power
  + Constraint
  + Record
  + Agency
  + Subject
  + Time
  + Repair
  + Trust
  + Enforcement
```

TRACE mapping:

```trace
labour_platform_translation :=
  metric_capture
  + contest_before_termination_or_deprivation_hardens
  + subject_facing_record
  + burden_routing
```

Comparators:

```trace
labour_platform_comparators :=
  labour_law
  + employment_law
  + algorithmic_management_research
  + industrial_relations
  + workplace_due_process
```

Demoter:

```trace
demote_labour_platform_translation_if :=
  labour_law_or_algorithmic_management_research_covers_it_better
```

Must not claim:

```trace
must_not_claim :=
  all_metrics_are_capture
  OR all_management_is_predatory
  OR formal_grievance_equals_live_correction
```

Next test:

```trace
labour_platform_next_test :=
  one_algorithmic_management_case
  + field_comparator
  + TRACE_delta
```

## 16. Media / spectacle / public reality systems

Status: T1 translation note.

Local language:

```trace
media_spectacle_language :=
  narrative
  + attention
  + audience
  + virality
  + spectacle
  + public_record
  + sincerity
  + performance
  + reality_capture
```

Active primitives:

```trace
media_spectacle_primitives :=
  Record
  + Witness
  + Trust
  + Power
  + Boundary
  + Subject
  + Memory
  + Uncertainty
```

TRACE mapping:

```trace
media_spectacle_translation :=
  captured_voice
  + sincerity_under_spectacle
  + record_poisoning
  + public_reality_as_correction_or_capture
```

Comparators:

```trace
media_spectacle_comparators :=
  media_studies
  + propaganda_studies
  + sociology
  + platform_governance
  + epistemology
```

Demoter:

```trace
demote_media_spectacle_translation_if :=
  media_studies_or_platform_governance_covers_it_better
  OR TRACE_becomes_generic_suspicion_of_media
```

Must not claim:

```trace
must_not_claim :=
  all_public_performance_is_false
  OR virality_equals_harm
  OR suspicion_equals_liberation
```

Next test:

```trace
media_spectacle_next_test :=
  one_public_record_capture_case
  + ordinary_media_read
  + TRACE_read
```

## 17. Memory / identity / continuity

Status: T1 translation note / T2 for record-memory interaction.

Local language:

```trace
memory_identity_language :=
  identity
  + recall
  + continuity
  + trauma
  + record
  + narrative
  + reconstruction
  + persistence
```

Active primitives:

```trace
memory_identity_primitives :=
  Memory
  + Record
  + Subject
  + Agency
  + Trust
  + Future_Space
  + Boundary
  + Uncertainty
```

TRACE mapping:

```trace
memory_identity_translation :=
  continuity_requires_record_and_correction
  + reconstruction_not_recall
  + identity_under_memory_loss
```

Comparators:

```trace
memory_identity_comparators :=
  memory_studies
  + psychology
  + trauma_studies
  + identity_philosophy
  + evidence_law
```

Demoter:

```trace
demote_memory_identity_translation_if :=
  memory_or_identity_theory_covers_it_better
  OR TRACE_turns_continuity_into_private_mythology
```

Must not claim:

```trace
must_not_claim :=
  memory_equals_truth
  OR reconstruction_equals_recall
  OR continuity_packet_transfers_personhood
```

Next test:

```trace
memory_identity_next_test :=
  one_memory_record_case
  + ordinary_memory_theory_read
  + TRACE_read
```

## 18. Policing / security / preemption

Status: T1 translation note / T2 for metric capture and future-space confiscation.

Local language:

```trace
policing_security_language :=
  suspicion
  + risk_score
  + surveillance
  + detention
  + no_fly
  + prediction
  + threat
  + public_safety
  + appeal
```

Active primitives:

```trace
policing_security_primitives :=
  Power
  + Record
  + Witness
  + Boundary
  + Agency
  + Subject
  + Time
  + Harm
  + Enforcement
```

TRACE mapping:

```trace
policing_security_translation :=
  predicted_future_confiscates_actual_future
  + contestability_before_restriction_hardens
  + record_and_witness_integrity
```

Comparators:

```trace
policing_security_comparators :=
  criminal_procedure
  + administrative_law
  + surveillance_studies
  + civil_liberties
  + risk_assessment_research
```

Demoter:

```trace
demote_policing_security_translation_if :=
  existing_due_process_or_surveillance_research_covers_it_better
  OR TRACE_relabels_all_risk_assessment_as_predation
```

Must not claim:

```trace
must_not_claim :=
  all_prediction_is_illegitimate
  OR all_security_is_capture
  OR risk_language_proves_harm_without_subject_route
```

Next test:

```trace
policing_security_next_test :=
  one_preemptive_restriction_case
  + ordinary_due_process_read
  + TRACE_read
```

## 19. Translation registry summary

```trace
Domain_Translation_Registry_v0_1 :=
  law
  + finance_debt
  + AI_alignment
  + mechanistic_interpretability
  + medicine
  + care_family
  + religion_myth
  + infrastructure_energy
  + climate_disaster
  + war_emergency
  + education
  + labour_platform
  + media_spectacle
  + memory_identity
  + policing_security
```

These entries are translation surfaces. None are active operators.

## 20. Cross-domain pressure points

Likely universal pressures visible across domains:

```trace
cross_domain_pressures :=
  correction_late
  + witness_captured
  + record_unreplayable
  + appeal_formal_but_unusable
  + enforcement_without_carrier
  + subject_future_erased_by_system_future
  + repair_declared_without_position_change
  + uncertainty_used_to_delay
  + metrics_replace_reality
  + boundary_masks_exclusion
```

These are not yet all operators. They should feed the Failure Mode Atlas.

## 21. Hostile review questions

```trace
hostile_questions :=
  are_domains_too_many?
  + are_translations_too_thin?
  + which_entries_are_only_existing_fields?
  + does_TRACE_add_anything_after_comparators?
  + are_must_not_claim_rules_strong_enough?
  + does_any_translation_smuggle_operator_promotion?
  + what_should_be_demoted_to_recognition_only?
```

## 22. Next build relation

This file enables:

```trace
next_builds_enabled :=
  Design_Pattern_Library_v0_1
  + Failure_Mode_Atlas_v0_1
  + Formal_MI_Bridge_v0_1
  + Standing_Wrongability_Map_v0_1
  + Tragic_Remainder_Action_Map_v0_1
```

The next safest build is Design Pattern Library, because it shifts TRACE from diagnosis toward constructive system design while keeping patterns below operator status.

## 23. Final compression

```trace
Domain_Translation_Registry_v0_1 :=
  local_domains
  mapped_to:
    primitives
    + active_operators
    + comparators
    + demoters
    + must_not_claim_rules
  while:
    domain_translation != operator
    domain_vocabulary != novelty
    story_or_case != evidence
```

Plain conclusion:

TRACE can fit many domains without pretending to own them. Each domain keeps its local knowledge. TRACE asks whether its primitives and narrow operators clarify correction, time, power, record, agency, repair, and hardening. If the existing field already does the work better, the translation demotes.

End.
