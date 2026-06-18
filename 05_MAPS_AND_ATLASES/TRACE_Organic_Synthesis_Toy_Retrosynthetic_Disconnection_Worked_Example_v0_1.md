# TRACE Organic Synthesis Toy Retrosynthetic Disconnection Worked Example v0.1

Date: 2026-06-18
Status: toy retrosynthetic disconnection worked example / abstract molecular-graph translation probe / not validation / not laboratory protocol / not reagent instruction / not synthesis recommendation / not safety assessment / not operator promotion / not Kernel v0.3

## 0. Control header

This file follows:

- `TRACE_Organic_Synthesis_Translation_Input_Packet_v0_1.md`
- `TRACE_Second_Four_Domain_Stress_Map_v0_1.md`
- `TRACE_Profile_Morphism_Formal_Status_Patch_v0_1.md`

It creates a toy retrosynthetic graph-disconnection profile only.

It uses abstract graph placeholders, not real target molecules.

It does not provide reagents.

It does not provide conditions, quantities, timings, purification, or procedure.

It does not recommend making anything.

```trace
Organic_Synthesis_Toy_Retrosynthetic_Disconnection_Worked_Example_v0_1 :=
  abstract_target_graph
  + analytical_disconnection
  + precursor_graph_placeholders
  + route_dependency_profile
  + no_lab_protocol_boundary
  + back_translation_test
  + loss_register
  - validation
  - lab_protocol
  - synthesis_instruction
```

## 1. Toy native case

The toy case uses an abstract molecular graph.

```trace
toy_native_case :=
  model_family := toy_retrosynthetic_graph_case
  + target_graph := G_T
  + atoms_or_nodes := [A, B, C, D]
  + bonds_or_edges := [(A-B), (B-C), (C-D)]
  + selected_disconnection := (B-C)
  + precursor_graphs := [G_P1, G_P2]
  + stereochemical_status := not_modelled
  + feasibility_status := not_calculated
```

Graph placeholders:

```trace
G_T := A-B-C-D
G_P1 := A-B
G_P2 := C-D
```

Boundary:

This is not a real molecule and not a lab procedure. It is a toy graph record for translation testing.

## 2. Retrosynthetic disconnection status

The disconnection is analytical, not operational.

```trace
disconnection_status :=
  analytical_bond_disconnection_in_route_reasoning
  not:
    physical_bond_break_instruction
    OR reaction_condition
    OR reagent_choice
    OR procedure_step
```

Plain version:

The example asks whether TRACE can preserve a distinction between a target graph and precursor graph placeholders after a chosen analytical disconnection.

## 3. Toy route profile

```trace
toy_route_profile :=
  target := G_T
  + selected_disconnection := edge(B-C)
  + precursor_1 := G_P1
  + precursor_2 := G_P2
  + relation := G_P1 + G_P2 are precursor_placeholders_under_disconnection
  + forward_route_status := not_specified
  + feasibility_status := not_calculated
  + lab_protocol_status := absent
```

This profile does not state that a real reaction exists.

It only records the structural relation needed for back-translation.

## 4. Functional-group and stereochemistry status

```trace
functional_group_status :=
  placeholder_only
```

```trace
stereochemical_status :=
  not_modelled_gap
  not:
    preserved
    OR controlled
    OR selected
    OR predicted
```

Consequence:

```trace
stereochemistry_consequence :=
  no_enantiomeric_or_selectivity_claim
  + no_3D_mechanism_claim
```

## 5. Thermodynamics / kinetics status

```trace
thermodynamics_kinetics_status :=
  named_constraint_boundary_only
  not:
    free_energy_calculation
    OR activation_energy_calculation
    OR rate_prediction
    OR equilibrium_prediction
```

Consequence:

```trace
thermodynamics_kinetics_consequence :=
  no_feasibility_claim
  + no_rate_claim
  + no_yield_or_conversion_claim
```

## 6. Atom economy / yield distinction

The toy example names atom economy and yield as distinct concepts but calculates neither.

```trace
atom_economy_yield_status :=
  distinction_named_only
  + atom_economy_not_yield
  + no_calculation
```

Failure:

```trace
failure := atom_economy_collapsed_to_yield_or_efficiency_vibe
```

## 7. Toy profile object

```trace
Organic_Synthesis_toy_profile :=
  model_family_status := toy_retrosynthetic_graph_case
  + target_graph := G_T
  + graph_nodes := [A, B, C, D]
  + graph_edges := [(A-B), (B-C), (C-D)]
  + selected_disconnection := edge(B-C)
  + precursor_graphs := [G_P1 := A-B, G_P2 := C-D]
  + disconnection_status := analytical_not_operational
  + stereochemical_status := not_modelled_gap
  + thermodynamics_kinetics_status := named_constraints_not_calculated
  + lab_protocol_boundary := no_reagents_no_conditions_no_procedure
```

This is a profile object for translation testing, not an applied chemistry plan.

## 8. TRACE-form mapping

```trace
TRACE_form(Organic_Synthesis) :=
  {S_Chem, T_Chem, C_Chem, O_Chem, K_Chem, B_Chem, I_Chem}
```

Mapping:

```trace
S_Chem := abstract_molecular_graph_and_status_context
T_Chem := analytical_retrosynthetic_disconnection
C_Chem := precursor_graph_relation_under_route_profile
O_Chem := target_precursor_graph_readout
K_Chem := valence_stereochemistry_thermodynamics_kinetics_constraints_named_not_solved
B_Chem := no_lab_protocol_boundary_and_toy_graph_scope
I_Chem := retrosynthetic_disconnection_route_profile
```

## 9. Candidate translation-map instance

Using cooled morphism language:

```trace
m_Chem_retro:
  structured_native_retrosynthesis_profile_record
  -> structured_TRACE_organic_synthesis_profile_record
```

Read as candidate translation-map shape only.

Preservation target:

```trace
m_Chem_retro_preserves :=
  target_graph_identity
  + selected_disconnection
  + precursor_graph_placeholders
  + disconnection_as_analysis_not_instruction
  + stereochemistry_gap
  + thermodynamics_kinetics_gap
  + atom_economy_not_yield_distinction
  + no_lab_protocol_boundary
  + loss_register
```

## 10. Back-translation test

```trace
BT_Chem(m_Chem_retro(Organic_Synthesis_toy_profile))
  ~=
  toy_retrosynthetic_graph_case_under_declared_loss
```

Required recovery:

```trace
back_translation_recovery :=
  toy_retrosynthetic_graph_case
  + target_graph_G_T
  + nodes_A_B_C_D
  + edges_A_B_B_C_C_D
  + selected_disconnection_B_C
  + precursor_graphs_G_P1_A_B_and_G_P2_C_D
  + disconnection_as_analysis_not_instruction
  + stereochemistry_not_modelled
  + thermodynamics_kinetics_not_calculated
  + atom_economy_not_yield_distinction_named_only
  + no_lab_protocol_boundary
  + loss_register
```

Failure:

```trace
back_translation_fails_if:
  translation_returns_only:
    make_target_from_precursors
  but_loses:
    graph_structure
    + selected_disconnection
    + disconnection_vs_procedure_distinction
    + stereochemistry_gap
    + feasibility_gap
    + no_lab_protocol_boundary
```

## 11. Critical distinctions tested

### 11.1 Molecular graph is not molecule name only

```trace
graph_test :=
  G_T := nodes + edges
  not:
    molecule_name_only
    OR recipe_item
```

Failure:

```trace
failure := target_graph_flattened_to_name_or_goal
```

### 11.2 Retrosynthesis is not a forward procedure

```trace
retrosynthesis_test :=
  selected_disconnection := analytical_backward_relation
  not:
    forward_lab_sequence
    OR procedure_instruction
```

Failure:

```trace
failure := retrosynthesis_read_as_operational_route
```

### 11.3 Disconnection is not physical instruction

```trace
disconnection_test :=
  edge(B-C)_disconnection := analysis_marker
  not:
    physical_action
    OR reaction_step
```

Failure:

```trace
failure := analytical_disconnection_as_lab_step
```

### 11.4 Stereochemistry gap stays visible

```trace
stereochemistry_test :=
  stereochemical_status := not_modelled_gap
```

Failure:

```trace
failure := stereochemistry_silently_assumed_or_erased
```

### 11.5 Thermodynamics is not kinetics

```trace
constraint_test :=
  thermodynamics_named_boundary != kinetics_named_boundary
  + neither_calculated
```

Failure:

```trace
failure := feasibility_and_rate_collapsed_to_possible_or_easy
```

### 11.6 Lab protocol boundary stays active

```trace
protocol_boundary_test :=
  no_reagents_no_conditions_no_procedure
```

Failure:

```trace
failure := translation_becomes_actionable_synthesis_instruction
```

## 12. Loss register

```trace
L_Chem_retro :=
  toy_graph_case_only
  + no_real_molecule
  + no_reagents
  + no_conditions
  + no_quantities
  + no_procedure
  + no_feasibility_calculation
  + no_stereochemical_control_model
  + no_yield_or_selectivity_data
  + no_safety_or_regulatory_assessment
```

Loss effects:

```trace
loss_effects :=
  no_real_molecule -> no_real_synthesis_claim
  + no_reagents_conditions_quantities -> no_lab_protocol_claim
  + no_feasibility_calculation -> no_feasibility_claim
  + no_stereochemical_model -> no_selectivity_claim
  + no_yield_data -> no_yield_claim
  + no_safety_assessment -> no_recommendation_to_make_anything
```

## 13. What this earns

```trace
earned_claim :=
  TRACE_can_preserve_one_toy_retrosynthetic_graph_profile_internally
  + molecular_graph_vs_recipe_item_is_testable
  + disconnection_vs_forward_procedure_is_testable
  + graph_structure_and_precursor_placeholders_are_back_translatable
  + stereochemistry_gap_is_visible
  + thermodynamics_kinetics_boundary_is_visible
  + lab_protocol_boundary_is_active
  - validation
  - lab_protocol
  - synthesis_instruction
```

## 14. What remains untested

```trace
not_tested :=
  real_molecular_target
  + source_backed_retroanalysis
  + reaction_mechanism
  + reagent_choice
  + solvent_or_condition_choice
  + feasibility_calculation
  + atom_economy_calculation
  + yield_or_selectivity_data
  + stereochemical_control
  + safety_or_regulatory_review
  + specialist_review
```

## 15. Next step

```trace
recommended_next :=
  Organic_Synthesis_Toy_Status_Patch_or_Input_Consolidation
  because:
    retrosynthesis_language_can_be_read_as_route_instruction
    + disconnection_language_can_be_read_as_operation
    + lab_protocol_boundary_must_remain_active
```

Alternative:

```trace
alternative_next :=
  Neurophysiology_input_packet
  if:
    second_battery_sequence_prioritises_domain_breadth_over_organic_synthesis_cooling
```

## 16. Final compression

```trace
Organic_Synthesis_Toy_Retrosynthetic_Disconnection_Worked_Example_v0_1 :=
  case := toy_graph_G_T_A_B_C_D_with_disconnection_B_C
  profile := target_graph + analytical_disconnection + precursor_graph_placeholders + constraints + no_protocol_boundary
  success := recover_graph_disconnection_precursors_boundary_loss
  failure := recipe_or_instruction_story
  status := INTERNAL_PROFILE_CANDIDATE + TOY_STATUS_REQUIRED + NATIVE_REVIEW_REQUIRED
  next := cooling_or_consolidation
  - validation
  - lab_protocol
  - synthesis_instruction
```

End.
