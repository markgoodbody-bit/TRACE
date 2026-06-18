# TRACE Primitive Registry v0.1

Date: 2026-06-18
Status: primitive registry / composition layer / not active operator registry / not validation / not proof / not Kernel v0.3

## 0. Control header

This file records the primitive layer implied by the Universality Map.

It does not add operators.

It does not promote candidates.

It does not validate TRACE.

It gives the project a wider base so the active operator spine can remain narrow.

```trace
purpose :=
  define_primitives
  + prevent_operator_bloat
  + support_domain_translation
  + support_formal_bridge
  + support_universality
  - validation
  - proof
  - Kernel_v0_3
```

## 1. Primitive vs operator

A primitive is a basic recurring quantity, relation, or pressure.

An operator is a diagnostic move built from primitives.

A domain translation is local language mapped onto primitives and operators.

```trace
primitive != operator
operator != domain_translation
story_carrier != evidence
```

Plain version:

TRACE can become more universal by naming more primitives without turning every primitive into a claim of novelty.

## 2. Core primitive set

```trace
TRACE_primitives_v0_1 :=
  Time
  + Harm
  + Correction
  + Subject
  + Agency
  + Witness
  + Record
  + Power
  + Constraint
  + Enforcement
  + Repair
  + Memory
  + Future_Space
  + Irreversibility
  + Infrastructure
  + Energy
  + Trust
  + Boundary
  + Uncertainty
```

This is a working set, not a closed ontology.

## 3. Primitive definitions

### 3.1 Time

```trace
Time :=
  ordering
  + delay
  + window
  + deadline
  + duration
  + tempo
  + hardening_rate
```

TRACE use:

Time matters because correction can arrive too late even when it formally exists.

Primary operator dependence:

```trace
OP_001_Correction_Before_Hardening := tau_correct < tau_harden
OP_004_Harm_Clock := time_until_loss_hardens
```

Demoter:

```trace
Demote_Time_if :=
  time_language_used_as_metaphor_only
  OR no_clock_can_be_defined_even_approximately
```

### 3.2 Harm

```trace
Harm :=
  loss_or_collapse_of_real_future_options
  + degradation_of_subject_position
  + pain_or_burden_where_relevant
  + irreversibility_risk
```

TRACE use:

Harm is not merely rule violation. Harm is what happens to the subject's live future-space.

Demoter:

```trace
Demote_Harm_claim_if :=
  no_affected_subject
  OR no_future_space_loss
  OR only_aesthetic_or_preference_disagreement
```

### 3.3 Correction

```trace
Correction :=
  change_that_reaches_the_subject
  + changes_actual_route_or_burden
  + occurs_before_hardening
  + leaves_record_or_repair_path
```

TRACE use:

Correction is not apology, formality, review existence, or symbolic response unless it changes the subject's live position.

Demoter:

```trace
Demote_Correction_claim_if :=
  response_occurs_after_hardening
  OR response_does_not_change_subject_position
  OR correction_channel_is_only_theatrical
```

### 3.4 Subject

```trace
Subject :=
  entity_or_being
  whose_future_space
  can_be_wronged_or_preserved
```

TRACE use:

Subject marks where harm, correction, agency, and repair must be routed. Systems can be objects of analysis without being subjects.

Open wound:

```trace
standing_not_solved := true
```

Demoter:

```trace
Demote_Subject_claim_if :=
  subject_status_asserted_without_wrongability_route
  OR institution_treated_as_subject_to_hide_human_subjects
```

### 3.5 Agency

```trace
Agency :=
  capacity_to_select
  + continue
  + refuse
  + contest
  + update
  under_constraint
```

TRACE use:

Agency is not unlimited freedom. It is the remaining live capacity to move, contest, and preserve future paths.

Demoter:

```trace
Demote_Agency_claim_if :=
  agency_language_used_to_blame_subject_for_blocked_options
  OR formal_choice_exists_but_usable_route_absent
```

### 3.6 Witness

```trace
Witness :=
  signal_source
  that_can_register:
    state
    + harm
    + contradiction
    + correction_failure
```

TRACE use:

Witness supports K-gate. A captured or generated witness can fail independence.

Demoter:

```trace
Demote_Witness_claim_if :=
  witness_controlled_by_audited_system
  OR witness_cannot_record_subject_position
  OR witness_exists_only_as_performance
```

### 3.7 Record

```trace
Record :=
  replayable_memory_surface
  + provenance
  + contestable_trace
  + retention
```

TRACE use:

Record protects against story replacement, memory collapse, and correction theatre.

Demoter:

```trace
Demote_Record_claim_if :=
  record_is_not_replayable
  OR actor_controls_all_record_surfaces
  OR record_preservation_does_not_enable_correction
```

### 3.8 Power

```trace
Power :=
  capacity_to_shape
  constrain
  close
  route
  or preserve
  subject_future_options
```

TRACE use:

Power is what makes method, gate, correction, and responsibility matter.

Demoter:

```trace
Demote_Power_claim_if :=
  power_named_generically
  but_no_lever_or_routing_capacity_identified
```

### 3.9 Constraint

```trace
Constraint :=
  boundary_or_rule
  that_changes_available_action_paths
```

TRACE use:

Constraint can protect or capture. Its moral valence depends on subject position, carrier, appeal, and repair.

Demoter:

```trace
Demote_Constraint_claim_if :=
  constraint_has_no_carrier
  OR constraint_only_binds_weak_subjects
  OR constraint_launders_power_without_correction
```

### 3.10 Enforcement

```trace
Enforcement :=
  carrier_that_makes_constraint_real
  + consequence_path
  + authority_or_mechanism
```

TRACE use:

Without enforcement, a safeguard can be false teeth.

Demoter:

```trace
Demote_Enforcement_claim_if :=
  no_carrier
  OR carrier_controlled_by_actor_under_review
  OR consequence_falls_on_subject_not_lever_holder
```

### 3.11 Repair

```trace
Repair :=
  restoration_of_real_future_options
  + burden_reversal_where_possible
  + scar_record_where_not_possible
```

TRACE use:

Repair is not closure. Repair is judged by affected subject position and future-space, not institutional declaration.

Demoter:

```trace
Demote_Repair_claim_if :=
  repair_declared_without_subject_position_change
  OR repair_requires_subject_to_absorb_new_burden
  OR repair_erases_record_of_harm
```

### 3.12 Memory

```trace
Memory :=
  continuity_bridge
  across:
    past_state
    + present_identity
    + record
    + future_correction
```

TRACE use:

Memory supports identity, learning, evidence, and recurrence prevention. It is not proof by recollection.

Demoter:

```trace
Demote_Memory_claim_if :=
  memory_is_uncorroborated_where_record_needed
  OR memory_used_to_override_subject_contest
  OR reconstruction_presented_as_recall
```

### 3.13 Future Space

```trace
Future_Space :=
  live_set_of_paths
  available_to_subject_or_system
  under_current_constraints
```

TRACE use:

Future-space is where harm, hope, repair, and agency become visible.

Demoter:

```trace
Demote_Future_Space_claim_if :=
  future_space_named_without_subject
  OR system_future_substituted_for_subject_future
  OR speculative_future_used_to_justify_present_harm
```

### 3.14 Irreversibility

```trace
Irreversibility :=
  condition_where_later_correction
  cannot_restore_lost_path
```

TRACE use:

Irreversibility defines hardening. Death is the clearest case but not the only case.

Demoter:

```trace
Demote_Irreversibility_claim_if :=
  loss_is_repairable
  OR hardening_asserted_without_threshold
  OR irreversible_language_used_for_rhetorical_intensity_only
```

### 3.15 Infrastructure

```trace
Infrastructure :=
  material_layer
  + procedural_layer
  + energetic_layer
  + authority_layer
  + maintenance_layer
  + correction_layer
```

TRACE use:

Infrastructure decides whether values have carriers. It can preserve correction or hide basement costs.

Demoter:

```trace
Demote_Infrastructure_claim_if :=
  infrastructure_named_but_no_material_or_procedural_dependency_mapped
  OR maintenance_and_failure_modes_absent
```

### 3.16 Energy

```trace
Energy :=
  capacity_to_change_state
  + sustain_action
  + maintain_transition
```

TRACE use:

Energy is the physical and institutional capacity behind action, infrastructure, escape, repair, and survival.

Demoter:

```trace
Demote_Energy_claim_if :=
  energy_used_as_metaphor_only
  OR energy_cost_not_routed_to_subject_or_system_burden
```

### 3.17 Trust

```trace
Trust :=
  cooperation
  + verification
  + memory
  + consequence
  + repair_path
```

TRACE use:

Trust is not belief or vibes. Trust is a bounded relation with verification and enforceable correction.

Demoter:

```trace
Demote_Trust_claim_if :=
  trust_requested_without_record
  OR trust_requested_without_consequence
  OR trust_used_to_disable_contest
```

### 3.18 Boundary

```trace
Boundary :=
  distinction_that_changes:
    standing
    + routing
    + permission
    + burden
    + responsibility
```

TRACE use:

Boundaries decide who counts, where duties route, and what cannot be traded away.

Demoter:

```trace
Demote_Boundary_claim_if :=
  boundary_is_declared_without_effect
  OR boundary_masks_exclusion
  OR boundary_used_to_end_correction
```

### 3.19 Uncertainty

```trace
Uncertainty :=
  incomplete_state_knowledge
  under_action_pressure
```

TRACE use:

Uncertainty changes evidence requirements, reversibility preferences, and escalation. It does not excuse inaction where delay hardens harm.

Demoter:

```trace
Demote_Uncertainty_claim_if :=
  uncertainty_used_to_delay_until_harm_hardens
  OR certainty_theatre_replaces_evidence
  OR uncertainty_eliminates_subject_precaution
```

## 4. Love / Death / Robots placement

The Love / Death / Robots triad from the Universality Map is a carrier for primitive clusters, not an operator.

```trace
Love_cluster :=
  Subject
  + Future_Space
  + Trust
  + Repair
  + Memory
  + Agency

Death_cluster :=
  Harm
  + Time
  + Irreversibility
  + Correction
  + Future_Space

Robots_cluster :=
  Power
  + Infrastructure
  + Energy
  + Constraint
  + Enforcement
  + Record
  + Uncertainty
  + Agency
```

Plain version:

Love tells TRACE why preservation matters. Death tells TRACE why timing matters. Robots tell TRACE why delegated power and created systems need answerability.

## 5. Primitive composition examples

### 5.1 Correction before hardening

```trace
Correction_Before_Hardening :=
  Time
  + Harm
  + Correction
  + Irreversibility
  + Subject
```

### 5.2 K-gate

```trace
K_Gate :=
  Witness
  + Record
  + Authority_or_Power
  + Time
  + Enforcement
  + Repair
```

### 5.3 Exit route

```trace
Exit_Route :=
  Subject
  + Power
  + Boundary
  + Agency
  + Time
  + Infrastructure
  + Protective_Secrecy
  + Future_Space
```

### 5.4 Option-space restoration

```trace
Option_Space_Restoration :=
  Repair
  + Future_Space
  + Subject
  + Agency
  + Memory
```

### 5.5 Method floor

```trace
Method_Floor :=
  Boundary
  + Harm
  + Power
  + Subject
  + Constraint
```

## 6. Domain translation support

Each domain translation should identify which primitives are active before claiming an operator applies.

```trace
domain_translation_schema :=
  domain
  + active_primitives
  + candidate_operator_if_any
  + comparator
  + demoter
  + must_not_claim
```

Example:

```trace
finance_and_debt_translation :=
  active_primitives:
    Time
    + Harm
    + Correction
    + Subject
    + Power
    + Constraint
    + Repair
  operator:
    Correction_Before_Hardening
  translation_note:
    stay_like_pause
  demoter:
    if_existing_debt_law_or_admin_review_covers_it_better
```

## 7. Formal bridge support

Primitive registry supports later formalisation.

```trace
formal_bridge_from_primitives :=
  x_t := state
  a_t := action
  H := harm_or_future_space_loss_function
  C := correction_function
  R := repair_function
  K := correction_gate_function
  tau_correct := correction_time
  tau_harden := hardening_time
```

Do not treat symbols as proof.

```trace
formal_notation != validation
model != measurement
compression != causation
```

## 8. Standing / subject caution

The `Subject` primitive is necessary but dangerous.

It must not be used to smuggle solved personhood.

```trace
Subject_primitive_status :=
  needed_for_wrongability
  + not_personhood_solution
  + standing_layer_pending
```

Boundary:

```trace
must_not_claim :=
  every_system_is_subject
  OR current_AI_personhood_proven
  OR uncertainty_about_standing_permits_irreversible_harm
  OR institutions_can_replace_human_subjects
```

## 9. Primitive failure modes

Primitive misuse can generate false universality.

```trace
primitive_failure_modes :=
  metaphor_inflation
  + operator_smuggling
  + subject_erasure
  + system_future_over_subject_future
  + certainty_theatre
  + enforcement_without_carrier
  + repair_without_subject_change
  + boundary_as_exclusion
  + trust_without_consequence
```

## 10. Hostile review questions

A hostile reviewer should attack this registry by asking:

```trace
hostile_questions :=
  are_these_primitives_too_many?
  + are_any_primitives_really_operators?
  + are_any_definitions_circular?
  + does_Subject_smuggle_standing?
  + does_Harm_smuggle_capability_theory_without_credit?
  + does_Energy_add_anything_or_only_metaphor?
  + does_Trust_duplicate_K_gate?
  + does_Boundary_do_too_much?
  + can_each_primitive_fail?
```

## 11. Next build relation

This file enables, but does not complete:

```trace
next_builds_enabled :=
  Domain_Translation_Registry_v0_1
  + Design_Pattern_Library_v0_1
  + Failure_Mode_Atlas_v0_1
  + Formal_MI_Bridge_v0_1
  + Standing_Wrongability_Map_v0_1
```

Do not build all at once.

## 12. Final compression

```trace
Primitive_Registry_v0_1 :=
  base_layer_for_TRACE_universality
  + primitives_not_operators
  + domain_translation_support
  + formal_bridge_support
  + hostile_review_needed
  - validation
  - Kernel_v0_3
```

Plain conclusion:

TRACE can get more encompassing by naming the primitives that recur across domains. The operator spine stays narrow. The primitive layer gets wider. That is how the project grows without turning every useful word into a false operator.

End.
