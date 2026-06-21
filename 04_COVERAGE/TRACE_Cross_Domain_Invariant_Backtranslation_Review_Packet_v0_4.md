# TRACE Cross-Domain Invariant Back-Translation Review Packet v0.4

Status: patched review instrument / external pressure handoff.  
Basis: v0.3 external review aggregation.  
Not: validation, canon promotion, proof of universality, expert endorsement, or TRACE theory patch.

## 0. Purpose

v0.4 hardens the review instrument after Qwen, Gemini, and Z.ai reviewed v0.3.

v0.3 fixed the I-slot type/directionality defect.

v0.4 addresses the next repeated defect:

```text
T transformation and C composition remained too generic.
```

The test now asks not only:

```text
Are the right native terms present?
```

but:

```text
Do the relations between S/T/C/O/K/B/I preserve the native mechanism?
```

## 1. Core grammar

```text
TRACE_form(D) := {S, T, C, O, K, B, I}
```

Expanded:

```text
S := state
T := transformation, with native_mechanism_class
C := composition, with composition_type
O := observation
K := constraint, with mechanism_type where needed
B := boundary
I := invariant / measure / typed readout
```

## 2. Mandatory typing rules

### 2.1 T native_mechanism_class

Every T entry must declare a native mechanism class.

Examples:

```text
isometric_encoding
unitary_evolution
noisy_channel
syndrome_conditioned_correction
continuous_deformation
homotopy_or_homeomorphism_map
bond_forming_reaction
bond_cleaving_reaction
stereoselective_transformation
regioselective_transformation
chemoselective_transformation
Merge
Agree
movement
spellout_or_transfer
pathogen_transmission
behavioural_response
expectation_update
optimisation_response
equilibrium_adjustment
physical_strain_accumulation
rupture_or_slip
neural_spiking
synaptic_transmission
plasticity_update
neuromodulation
```

If T is generic, mark:

```text
TRACE_T_TRANSFORMATION_FLATTENING
```

### 2.2 C composition_type

Every C entry must declare a composition type.

Examples:

```text
structural_coupling
temporal_sequence
recursive_composition
network_mixing
topological_construction
tensor_or_entanglement_composition
circuit_composition
reaction_sequence
convergent_coupling
market_clearing_coupling
expectation_equilibrium_coupling
fault_network_coupling
neural_network_topology
```

If C is generic, mark:

```text
TRACE_C_COMPOSITION_FLATTENING
```

### 2.3 I type/directionality

Every I entry must declare type and directionality.

Allowed I types:

```text
complete_invariant
partial_invariant
measure
status_condition
bridge_marker
```

Directionality:

```text
bidirectional
one_directional_difference_only
readout_only
bridge_only
```

If I is untyped or directionality is unclear, mark:

```text
TRACE_I_SLOT_DIRECTIONALITY_FAILURE
```

### 2.4 K mechanism_type where needed

Where the native mechanism depends on constraint kind, K must declare mechanism type.

Examples:

```text
algebraic_constraint
geometric_constraint
steric_constraint
electronic_constraint
thermodynamic_constraint
kinetic_constraint
computational_locality_constraint
measurement_constraint
code_space_constraint
equilibrium_constraint
budget_constraint
physical_material_constraint
network_constraint
behavioural_constraint
```

If K hides the mechanism, mark:

```text
TRACE_K_CONSTRAINT_FLATTENING
```

## 3. Relational back-translation gate

A review now fails or becomes partial if it only checks slot contents.

Reviewers must answer:

```text
Which relation between S/T/C/O/K/B/I carries the native mechanism?
```

Examples:

```text
QEC: K(no-cloning/code-space) constrains T(isometric encoding/noisy channel/syndrome correction), while O(syndrome extraction) must not collapse I(logical_state_equivalence).

Organic synthesis: K(steric/electronic/kinetic constraint) shapes T(selective reaction), while C(reaction sequence/convergent coupling) determines whether the route preserves I(selectivity/yield/readout).

DSGE: C(expectation/equilibrium coupling) conditions T(expectation update/optimisation response), with K(budget/equilibrium/liquidity constraints) limiting reachable S states.
```

If the reviewer cannot identify a relation between slots, mark:

```text
TRACE_RELATIONAL_BACKTRANSLATION_FAILURE
```

## 4. Review task

For each domain, answer:

```text
1. Are S, T, C, O, K, B, I populated with native-specific content?
2. Is T typed by native_mechanism_class?
3. Is C typed by composition_type?
4. Is I typed by type/directionality?
5. Is K typed where constraint kind matters?
6. Does the original back-translation question pass?
7. Does the independent back-translation question pass?
8. Which relation between slots carries the native mechanism?
9. What remains lost?
```

## 5. Domain stress entries

### 5.1 Quantum information / QEC

Required hardening:

```text
T native_mechanism_class:
- isometric_encoding
- unitary_evolution
- noisy_channel
- syndrome_conditioned_correction
- measurement_or_decoherence_process

C composition_type:
- tensor_or_entanglement_composition
- circuit_composition
- code_block_composition

K mechanism_type:
- no_cloning_constraint
- non_commutativity_constraint
- measurement_constraint
- code_space_constraint
- threshold_assumption

O:
- syndrome_extraction
- logical_state_readout_where_valid
- physical_measurement_outcome

I:
- logical_state_equivalence := complete_invariant / bidirectional within protected code assumptions
- syndrome_readout := measure / readout_only
- logical_error_rate := measure / readout_only
- fidelity := measure / readout_only
```

Relational test:

```text
Can the reviewer explain how K constrains T and O so that syndrome_readout does not become logical_state_equivalence?
```

Fail if:

```text
QEC becomes classical redundancy, backup, or generic noise resistance.
```

### 5.2 Algebraic topology

Required hardening:

```text
T native_mechanism_class:
- continuous_deformation
- homotopy_or_homeomorphism_map
- quotient_or_gluing_map where applicable

C composition_type:
- topological_construction
- structural_coupling
- composition_of_maps

K mechanism_type:
- equivalence_relation_constraint
- continuity_constraint
- boundary_constraint

I:
- Betti numbers := partial_invariant / one_directional_difference_only
- homology group := partial_invariant unless restricted problem says otherwise
- homeomorphism class := complete_invariant / bidirectional only if established
```

Relational test:

```text
Can the reviewer explain which T transformations are allowed by K and which I is preserved or insufficient under those transformations?
```

Fail if:

```text
same partial invariant value is treated as proof of equivalence.
```

### 5.3 Organic synthesis

Required hardening:

```text
T native_mechanism_class:
- chemoselective_transformation
- regioselective_transformation
- stereoselective_transformation
- bond_forming_reaction
- bond_cleaving_reaction

C composition_type:
- reaction_sequence
- convergent_coupling
- protecting_deprotecting_sequence

K mechanism_type:
- steric_constraint
- electronic_constraint
- thermodynamic_constraint
- kinetic_constraint
- geometric_constraint

I:
- chemoselectivity := measure_or_route_descriptor / readout_only
- regioselectivity := measure_or_route_descriptor / readout_only
- stereoselectivity := measure_or_route_descriptor / readout_only
- enantiomeric_excess := measure / readout_only
- yield := measure / readout_only
```

Relational test:

```text
Can the reviewer explain how K shapes T and how C route structure changes the meaning of I?
```

Fail if:

```text
TRACE only says desired route vs side reaction, or merely labels selectivity without identifying the active constraint mechanism.
```

### 5.4 Generative syntax

Required hardening:

```text
T native_mechanism_class:
- Merge
- Agree
- movement
- feature_valuation
- spellout_or_transfer

C composition_type:
- recursive_composition
- derivational_sequence

K mechanism_type:
- computational_locality_constraint
- phase_impenetrability_constraint
- c_command_constraint
- feature_matching_constraint

I:
- preserved_dependency_relation := status_condition / readout_only
- grammaticality_under_target_grammar := grammar_relative_status / readout_only
- recoverable_feature_relation := status_condition / readout_only
```

Relational test:

```text
Can the reviewer explain which K constraint blocks which T operation inside which C derivational sequence?
```

Fail if:

```text
TRACE only says access closed after packaging.
```

### 5.5 Epidemiology

Required hardening:

```text
T native_mechanism_class:
- pathogen_transmission
- recovery
- immunity_change
- intervention_response
- behavioural_response
- observation_delay_effect

C composition_type:
- network_mixing
- spatial_coupling
- population_stratification
- institutional_response_coupling

K mechanism_type:
- network_constraint
- behavioural_constraint
- capacity_constraint
- immunity_constraint
- observation_constraint

I:
- R_t := measure / readout_only
- R_0 := measure_or_model_parameter / readout_only
- incidence := measure / readout_only
- prevalence := measure / readout_only
- generation_interval := measure_distribution / readout_only
```

Relational test:

```text
Can the reviewer explain whether high R_t comes from T(pathogen dynamics), C(network mixing), O(observation lag), K(capacity/behaviour), or some relation among them?
```

Fail if:

```text
TRACE only says spread outruns control.
```

### 5.6 Dynamic macroeconomics / DSGE

Required hardening:

```text
T native_mechanism_class:
- expectation_update
- optimisation_response
- policy_response
- shock_propagation
- consumption_investment_labour_adjustment

C composition_type:
- market_clearing_coupling
- expectation_equilibrium_coupling
- sectoral_coupling
- household_firm_government_coupling

K mechanism_type:
- equilibrium_constraint
- budget_constraint
- Euler_style_optimisation_constraint
- liquidity_constraint
- borrowing_constraint
- policy_rule_constraint

I:
- welfare_measure := measure / readout_only
- output_gap := measure / readout_only
- inflation := measure / readout_only
- unemployment := measure / readout_only
- debt_service_burden := measure / readout_only
- solvency_liquidity_condition := status_condition / readout_only
```

Relational test:

```text
Can the reviewer explain how C(expectation/equilibrium coupling) changes the interpretation of T(shock or expectation update), rather than treating DSGE as generic shock/lag?
```

Fail if:

```text
forward-looking expectations and equilibrium constraints are not recoverable.
```

### 5.7 Geodynamics

Required hardening:

```text
T native_mechanism_class:
- physical_strain_accumulation
- rupture_or_slip
- subduction
- deformation

C composition_type:
- fault_network_coupling
- plate_interaction
- mantle_lithosphere_coupling

K mechanism_type:
- friction_constraint
- viscosity_constraint
- material_strength_constraint
- geometry_constraint
- boundary_condition

I:
- strain_rate := measure / readout_only
- recurrence_interval := measure_or_estimate / readout_only, not deterministic prediction
- stress_drop := measure / readout_only
- slip_deficit := measure_or_model_estimate / readout_only
- hazard_probability := measure_or_model_output / readout_only
```

Relational test:

```text
Can the reviewer explain how C(fault/plate coupling) and K(physical constraints) condition T(rupture/slip) without treating recurrence interval as prediction?
```

Fail if:

```text
recurrence interval implies reliable periodic predictability.
```

### 5.8 Neurophysiology

Required hardening:

```text
T native_mechanism_class:
- neural_spiking
- synaptic_transmission
- plasticity_update
- neuromodulation
- pathological_excitation
- metabolic_stress_response

C composition_type:
- neural_network_topology
- synaptic_connectivity
- circuit_coupling

K mechanism_type:
- ion_channel_constraint
- membrane_threshold_constraint
- inhibitory_control_constraint
- metabolic_constraint
- synaptic_weight_constraint

I:
- firing_rate := measure / readout_only
- oscillation_pattern := measure_or_status_condition / readout_only
- excitatory_inhibitory_balance := measure_or_status_condition / readout_only
- seizure_threshold := threshold_status_condition / readout_only
- clinical_experiential_bridge := bridge_marker / bridge_only
```

Relational test:

```text
Can the reviewer explain whether runaway activity is caused by T(spiking/plasticity), C(network topology), K(ion-channel/inhibitory/metabolic constraint), or their relation?
```

Fail if:

```text
TRACE only says amplification exceeds control.
```

## 6. Review labels

Use:

```text
TRACE_INVARIANT_TRANSLATION_STRONG
TRACE_INVARIANT_TRANSLATION_PARTIAL
TRACE_INVARIANT_TRANSLATION_LOW
TRACE_BACKTRANSLATION_FAILURE
TRACE_NATIVE_INVARIANT_LOSS
TRACE_DOMAIN_FLATTENING_FAILURE
TRACE_ETHICS_OVERREACH_FAILURE
TRACE_I_SLOT_DIRECTIONALITY_FAILURE
TRACE_T_TRANSFORMATION_FLATTENING
TRACE_C_COMPOSITION_FLATTENING
TRACE_K_CONSTRAINT_FLATTENING
TRACE_RELATIONAL_BACKTRANSLATION_FAILURE
TRACE_AUTHOR_SELECTED_QUESTION_BIAS
```

## 7. Control note

v0.4 should be harder to pass than v0.3.

It tests slot relations, not just slot contents.

If it still passes too easily, the form is probably too permissive.
