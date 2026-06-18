# TRACE Primitive Registry v0.1

Date: 2026-06-18
Status: primitive registry / composition layer / hostile-audit patched / not active operator registry / not validation / not proof / not Kernel v0.3

## 0. Control header

This file records the primitive layer implied by the Scope / Applicability Map.

It does not add operators. It does not promote candidates. It does not validate TRACE. It does not create Kernel v0.3.

Hostile-audit patch, 2026-06-18: this registry now separates core primitives from derived/support terms. The prior version treated too many composites as primitives.

```trace
purpose :=
  define_primitives
  + prevent_operator_bloat
  + support_domain_translation
  + support_formal_bridge
  + support_scope_growth
  - validation
  - proof
  - Kernel_v0_3
```

## 1. Primitive vs operator vs derived support

```trace
primitive != operator
derived_support != active_spine_operator
operator != domain_translation
story_carrier != evidence
mnemonic != structure
```

A primitive is a recurring basic quantity, relation, or pressure.

A derived/support term is a composed concept built from primitives.

An operator is a diagnostic move built from primitives and support terms.

A domain translation is local language mapped onto primitives and operators.

## 2. Core primitives

```trace
TRACE_core_primitives_v0_1 :=
  Time
  + Future_Space
  + Subject
  + Power
  + Agency
  + Witness
  + Record
  + Constraint
  + Uncertainty
  + Irreversibility
  + Infrastructure
  + Harm
```

This is a working set, not a closed ontology.

## 3. Derived / support terms

```trace
TRACE_derived_support_terms_v0_1 :=
  Correction
  + Repair
  + Enforcement
  + Memory
  + Trust
  + Energy
  + Boundary
```

```trace
derived_support_reason :=
  Correction := operator_adjacent_to_correction_before_hardening
  Repair := option_space_restoration_support
  Enforcement := K_gate_component_and_carrier_question
  Memory := Record + Time + continuity
  Trust := Witness + Record + Enforcement + Repair + bounded_cooperation
  Energy := Infrastructure + Power + capacity_to_act
  Boundary := routing_or_permission_distinction_not_full_responsibility_theory
```

## 4. Core primitive definitions

```trace
Time := ordering + delay + window + deadline + duration + tempo + hardening_rate

Future_Space := live_set_of_paths_available_to_subject_or_system_under_current_constraints

Subject := entity_or_being_whose_future_space_can_be_wronged_or_preserved

Power := capacity_to_shape_constrain_close_route_or_preserve_subject_future_options

Agency := capacity_to_select_continue_refuse_contest_or_update_under_constraint

Witness := signal_source_that_can_register_state_harm_contradiction_or_correction_failure

Record := replayable_memory_surface + provenance + contestable_trace + retention

Constraint := boundary_or_rule_that_changes_available_action_paths

Uncertainty := incomplete_state_knowledge_under_action_pressure

Irreversibility := condition_where_later_correction_cannot_restore_lost_path

Infrastructure := material_layer + procedural_layer + energetic_capacity + authority_layer + maintenance_layer + correction_layer

Harm := degradation_or_collapse_of_subject_future_space + pain_or_burden_where_relevant + irreversibility_risk
```

## 5. Comparator pressure on Future Space and Harm

Future Space and Harm are not novel merely because TRACE names them.

```trace
Future_Space_comparators :=
  capability_approach
  + option_value
  + agency_theory
  + opportunity_set_analysis

Harm_comparators :=
  capability_approach
  + harm_principle
  + tort_and_causation
  + welfare_and_burden_analysis
```

Demoter:

```trace
demote_if :=
  capability_or_harm_theory_covers_the_claim_better
  OR no_affected_subject
  OR no_future_space_loss
  OR only_aesthetic_or_preference_disagreement
```

## 6. Standing / subject caution

The `Subject` primitive is necessary but dangerous.

It must not be used to smuggle solved personhood.

```trace
Subject_primitive_status :=
  needed_for_wrongability
  + not_personhood_solution
  + standing_layer_pending
```

```trace
must_not_claim :=
  every_system_is_subject
  OR current_AI_personhood_proven
  OR uncertainty_about_standing_permits_irreversible_loss
  OR institutions_can_replace_human_subjects
```

## 7. Love / Death / Robots placement

The Love / Death / Robots triad from the Scope Map is a mnemonic only.

It should not cluster primitives or carry analytic load in this registry.

```trace
LDR_status_here :=
  U0_mnemonic
  - primitive_cluster
  - operator
  - evidence
```

## 8. Primitive composition examples

```trace
Correction_Before_Hardening :=
  Time
  + Harm
  + Correction
  + Irreversibility
  + Subject

K_Gate :=
  Witness
  + Record
  + Power_or_Authority
  + Time
  + Enforcement
  + Repair

Exit_Route :=
  Subject
  + Power
  + Boundary
  + Agency
  + Time
  + Infrastructure
  + Protective_Secrecy
  + Future_Space

Option_Space_Restoration :=
  Repair
  + Future_Space
  + Subject
  + Agency
  + Memory

Method_Floor :=
  Boundary
  + Harm
  + Power
  + Subject
  + Constraint
```

## 9. Formal bridge support

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

## 10. Failure modes

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
  + mnemonic_as_structure
```

## 11. Hostile review questions

```trace
hostile_questions :=
  are_core_primitives_still_too_many?
  + are_derived_terms_correctly_demoted?
  + are_any_definitions_circular?
  + does_Subject_smuggle_standing?
  + does_Harm_smuggle_capability_theory_without_credit?
  + does_Energy_add_structure_or_only_metaphor?
  + does_Trust_duplicate_K_gate?
  + does_Boundary_still_do_too_much?
  + can_each_core_primitive_fail?
```

## 12. Final compression

```trace
Primitive_Registry_v0_1_after_hostile_audit :=
  base_layer_for_TRACE_scope
  + core_primitives
  + derived_support_terms
  + primitives_not_operators
  + domain_translation_support
  + formal_bridge_support
  + hostile_review_needed
  - validation
  - Kernel_v0_3
```

Plain conclusion:

TRACE can get more encompassing by naming the primitives that recur across domains. The operator spine stays narrow. The primitive layer is now split into core primitives and derived support terms so useful composites do not masquerade as base primitives.

End.
