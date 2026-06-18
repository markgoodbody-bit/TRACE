# TRACE Domain Translation Registry v0.1

Date: 2026-06-18
Status: domain translation registry / mapping layer / hostile-audit patched / not active operator registry / not validation / not proof / not Kernel v0.3

## 0. Control header

This file records how local domains can enter TRACE without becoming new operators by default.

It does not add operators.

It does not promote candidates.

It does not validate TRACE.

Hostile-audit patch, 2026-06-18: the prior version over-leveled several domains as T2/T3 despite its own rule that no domain starts above T1 without evidence. This revision caps all untested domains at T1 and caps war/emergency at T0 pending a Tragic Remainder Action Map.

```trace
purpose :=
  map_domains_to_TRACE
  + preserve_scope
  + prevent_domain_phrase_operator_bloat
  + require_comparators
  + require_demoters
  + enforce_status_caps
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

```trace
domain_entry_schema :=
  domain
  + current_status
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

```trace
T0_recognition_only := helps_readers_notice_pattern - operational_claim
T1_translation_note := maps_domain_language_to_existing_TRACE_operator
T2_mapping_candidate := may_reveal_new_interaction_but_not_operator
T3_test_ready_translation := has_comparator + demoter + worked_case_plan + evidence_basis
T4_cross_domain_invariant_candidate := survives_unrelated_domains + prior_art_pressure + falsifier
```

Hard rule after hostile audit:

```trace
no_domain_above_T1_without_worked_delta := true
war_emergency_status_cap := T0_until_tragic_remainder_map
```

## 4. Registry table after hostile audit

| Domain | Status after audit | Main TRACE mapping | Main comparator pressure | Demoter |
|---|---|---|---|---|
| Law / administrative governance | T1 | correction-before-hardening; K-gate; method floor; option-space restoration | administrative law; public law; due process; procedural justice; human rights; access to justice | demote if existing law covers timing/correction better or TRACE relabels due process |
| Finance / debt / welfare recovery | T1/T0 | correction-before-hardening, debt-scoped; stay-like pause; burden under time pressure | debt law; administrative review; poverty law; welfare rights; moratoria/stays | demote if debt/admin/poverty law covers it better or it relabels correction-before-hardening |
| AI alignment / deployment governance | T1 | correction before deployment hardening; K-gate for model action; rollback/pause carrier; affected-subject contestability | AI safety; safety cases; assurance cases; evals; incident response; monitoring; governance | demote if standard AI governance/safety cases cover it better or TRACE adds only moral vocabulary |
| Mechanistic interpretability | T1 | internal evidence channel; intervention point; deployment hardening window; subject harm path; rollback/correction channel | MI; causal ablation; representation analysis; evals; red teaming; safety monitoring | demote if MI explanation does not change intervention/correction window |
| Medicine / healthcare / triage | T1 | treatment before deterioration hardens; live review; consent/contestability; record preservation | clinical safety; medical ethics; triage; patient safety; duty of candour; consent law | demote if clinical safety/triage covers timing and correction better |
| Care / family / dependency | T1 | preserve subject future-space; support without seizure; burden routing; repair/trust under dependency | care ethics; safeguarding; disability rights; capability approach; family law; social care | demote if care ethics/safeguarding covers it better or TRACE turns care into control |
| Religion / myth / meaning systems | T0/T1 | love/death/meaning structure; authority claim; correction channel; capture-or-repair | theology; sociology; anthropology; moral psychology; political theology; cultic-abuse studies | demote if TRACE restates secular suspicion or fails to distinguish care from capture |
| Infrastructure / energy / basement systems | T1 | values require carriers; maintenance before failure hardens; hidden basement costs; repair capacity | resilience engineering; reliability engineering; safety engineering; systems engineering; critical infrastructure studies | demote if resilience/reliability covers it better or TRACE only says infrastructure matters |
| Climate / disaster / survival gates | T1 | warning before hardening; gated survival; infrastructure capacity; repair/adaptation window | disaster risk reduction; climate adaptation; emergency management; environmental justice; resilience planning | demote if disaster-risk frameworks cover warning/gate timing better |
| War / emergency / force | T0 | tragic remainder pointer only; method floor under pressure; record preservation; no moral victory claim | just war theory; IHL; emergency ethics; disaster ethics; command responsibility | blocked until Tragic Remainder Action Map; demote if TRACE becomes permission language for force |
| Education / development / training loops | T1 | correction as learning before label hardens; record trust; agency-preserving scaffold | pedagogy; developmental psychology; assessment theory; special education law; restorative discipline | demote if existing pedagogy/assessment covers it better or TRACE relabels feedback |
| Labour / platform power / workplace systems | T1 | metric capture; contest before termination/deprivation hardens; subject-facing record; burden routing | labour law; employment law; algorithmic management; industrial relations; workplace due process | demote if labour/platform research covers it better |
| Media / spectacle / public reality systems | T1 | captured voice; sincerity under spectacle; record poisoning; public reality as correction/capture | media studies; propaganda studies; sociology; platform governance; epistemology | demote if field literature covers it better or TRACE becomes generic suspicion of media |
| Memory / identity / continuity | T1 | continuity requires record and correction; reconstruction not recall; identity under memory loss | memory studies; psychology; trauma studies; identity philosophy; evidence law | demote if memory/identity theory covers it better or TRACE turns continuity into private mythology |
| Policing / security / preemption | T1 | prediction confiscates actual future; contestability before restriction hardens; record/witness integrity | criminal procedure; administrative law; surveillance studies; civil liberties; risk assessment | demote if due process/surveillance research covers it better or TRACE relabels all risk as predation |

## 5. AI alignment and mechanistic interpretability boundary

AI alignment and mechanistic interpretability remain separate entries only provisionally.

```trace
AI_alignment_focus :=
  deployment_governance
  + rollback_or_pause_carrier
  + affected_subject_contestability
  + model_action_under_power

MI_focus :=
  internal_evidence_channel
  + causal_role
  + intervention_point
  + deployment_hardening_window
```

Merge or demote if:

```trace
merge_AI_MI_if :=
  MI_translation_only_repeats_AI_deployment_governance
  OR no_MI_case_shows_changed_correction_window
```

Must not claim:

```trace
must_not_claim :=
  TRACE_solves_alignment
  OR evaluation_equals_correction
  OR model_interpretation_equals_control
  OR interpretability_equals_accountability
```

## 6. Religion boundary

Religion remains T0/T1 only.

```trace
religion_translation :=
  love_death_meaning_structure
  + authority_claim
  + correction_channel
  + capture_or_repair
```

Must not claim:

```trace
must_not_claim :=
  all_religion_is_same
  OR religion_explains_all_evil
  OR meaning_systems_are_all_insanity
  OR TRACE_settles_metaphysics
```

## 7. War / emergency block

War/emergency/force is capped at T0 until a Tragic Remainder Action Map exists.

```trace
war_emergency_status :=
  T0_recognition_only
  + tragic_remainder_pending
  - operational_permission
```

Must not claim:

```trace
must_not_claim :=
  TRACE_authorises_violence
  OR no_admissible_branch_equals_clean_decision
  OR tragic_action_removes_accountability
```

## 8. Missing domains flagged by hostile audit

Top missing domains by structural importance:

```trace
missing_domains_priority :=
  disability
  + animals_and_ecology
  + prisons_and_carceral_systems
  + markets_and_trade
  + migration_border_asylum
```

Reason:

```trace
missing_domain_reason :=
  disability_tests_subject_agency_and_usable_route
  + animals_ecology_tests_standing_and_non_person_not_substrate
  + prisons_test_correction_channel_as_harm_carrier
  + markets_trade_test_externality_and_basement_routing
  + migration_asylum_tests_gated_survival_and_exit_under_hostile_authority
```

Do not add them automatically. They should enter only through a later hostile-reviewed registry patch.

## 9. Cross-domain pressure points

Likely pressures visible across domains:

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

These are not yet all operators. They should feed the Failure Mode Atlas only after at least one worked delta.

## 10. Hostile review questions

```trace
hostile_questions :=
  are_domains_too_many?
  + are_translations_too_thin_or_repetitive?
  + which_entries_are_only_existing_fields?
  + does_TRACE_add_anything_after_comparators?
  + are_must_not_claim_rules_strong_enough?
  + does_any_translation_smuggle_operator_promotion?
  + what_should_be_demoted_to_T0_recognition_only?
```

## 11. Next build relation

Hostile audit changed the next action.

```trace
next_action :=
  one_worked_delta
  not:
    Design_Pattern_Library_yet
```

Candidate worked-delta targets:

```trace
worked_delta_candidates :=
  AI_deployment_failure
  OR mechanistic_interpretability_case
  OR public_administration_case
```

A design pattern library is still likely needed later, but not before a worked delta.

## 12. Final compression

```trace
Domain_Translation_Registry_v0_1_after_hostile_audit :=
  local_domains
  mapped_to:
    primitives
    + active_operators
    + comparators
    + demoters
    + must_not_claim_rules
  with:
    all_unworked_domains_capped_at_T1
    + war_emergency_capped_at_T0
  while:
    domain_translation != operator
    domain_vocabulary != novelty
    story_or_case != evidence
```

Plain conclusion:

TRACE can fit many domains without pretending to own them. Each domain keeps its local knowledge. TRACE asks whether its primitives and narrow operators clarify correction, time, power, record, agency, repair, and hardening. If the existing field already does the work better, the translation demotes. No domain translation is promoted above T1 until a worked delta earns it.

End.
