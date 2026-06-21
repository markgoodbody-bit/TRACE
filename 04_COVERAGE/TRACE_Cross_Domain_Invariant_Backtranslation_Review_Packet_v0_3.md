# TRACE Cross-Domain Invariant Back-Translation Review Packet v0.3

Status: patched review instrument / external pressure handoff.  
Basis: v0.2 external review aggregation.  
Not: validation, canon promotion, proof of universality, expert endorsement, or TRACE theory patch.

## 0. Purpose

This v0.3 packet hardens the invariant/back-translation review instrument after repeated external AI review findings.

It keeps the core grammar:

```text
TRACE_form(D) := {S, T, C, O, K, B, I}
```

Expanded:

```text
S := state
T := transformation
C := composition
O := observation
K := constraint
B := boundary
I := invariant / measure / typed readout
```

v0.3 changes:

```text
I-slot type/directionality is mandatory.
Independent back-translation questions are mandatory.
Domain entries are hardened where repeated reviews found native-mechanism loss.
```

## 1. I-slot rule

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
bidirectional := same I means same class; different I means different class
one_directional_difference_only := different I may show difference; same I does not prove equivalence
readout_only := tracks state/behaviour; does not define equivalence class
bridge_only := connects technical state to subject/ethics/governance only when separately evidenced
```

Back-translation must state whether I is complete, partial, measure, status condition, or bridge marker.

If directionality is unclear, mark:

```text
TRACE_I_SLOT_DIRECTIONALITY_FAILURE
```

## 2. Review task

For each domain, reviewers must answer both:

```text
A. original back-translation question
B. independent back-translation question
```

Interpretation:

```text
original pass + independent pass := stronger signal
original pass + independent fail := author-selected-question bias or under-specified TRACE form
original fail := weak translation
```

## 3. Domain entries

### 3.1 Algebraic topology

Native object:

```text
topological space / manifold / simplicial complex
```

Native distinction to recover:

```text
invariant-preserving deformation vs forbidden transformation that changes the target equivalence class
```

TRACE form:

```text
S := topological space or constructed complex
T := continuous deformation / map / transformation
C := gluing, product, union, composition of maps or spaces
O := chosen invariant computation / equivalence test
K := allowed transformations under homeomorphism, homotopy, or selected equivalence relation
B := boundary / hole / cut / tear / gluing condition
I := named invariant or equivalence marker, with type/directionality declared
```

I examples:

```text
Betti numbers := partial_invariant / one_directional_difference_only
homology group := partial_invariant unless declared complete for a restricted classification problem
fundamental group := partial_invariant unless declared complete for the target class
homeomorphism class := complete_invariant / bidirectional, if actually established
```

Loss register:

```text
TRACE does not compute topology.
TRACE loses proof detail, exact algebraic machinery, and literature-specific definitions unless named.
Named invariants may be necessary but not sufficient; same invariant value does not automatically prove equivalence.
```

Original back-translation question:

```text
Can a reviewer recover which invariant/equivalence relation is being preserved or lost?
```

Independent back-translation question:

```text
Can the TRACE form distinguish between two spaces sharing the same selected homology/Betti profile but not being equivalent under the target relation?
```

Fail condition:

```text
Fail or mark partial if I is not typed, if directionality is unstated, or if same invariant value is treated as proof of equivalence without justification.
```

### 3.2 Quantum information / QEC

Native object:

```text
quantum state / encoded logical state / physical qubit register / entangled system / measurement context
```

Native distinction to recover:

```text
protected logical information under QEC vs classical redundancy or generic noise-resistant backup
```

TRACE form:

```text
S := encoded logical state plus physical substrate state
T := isometric encoding, unitary evolution, noisy channel, syndrome-conditioned correction, measurement/decoherence process
C := tensor product / entanglement / circuit composition / code-block composition
O := syndrome extraction, measurement outcome, tomography, observable readout, logical-state readout where valid
K := no-cloning, non-commutativity, measurement disturbance, Knill-Laflamme/code-space condition, threshold assumptions
B := system/environment boundary, code-space boundary, logical/physical boundary, syndrome/logical readout boundary
I := layered I entries, typed separately
```

I entries:

```text
logical_state_equivalence := complete_invariant within the protected code space / bidirectional only under stated code assumptions
syndrome_readout := measure / readout_only
logical_error_rate := measure / readout_only
fidelity := measure / readout_only
entanglement_structure := structural descriptor; type must be declared for the specific claim
```

Loss register:

```text
TRACE does not replace Hilbert-space mathematics or stabilizer formalism.
TRACE fails if QEC is reduced to ordinary copying, backup, or generic redundancy.
TRACE must preserve the distinction between logical information, physical error, and syndrome readout.
```

Original back-translation question:

```text
Can a reviewer recover why quantum error correction is not ordinary copying/back-up?
```

Independent back-translation question:

```text
Can the TRACE form distinguish ordinary classical redundancy from QEC that preserves logical information without cloning an unknown quantum state?
```

Fail condition:

```text
Fail if no-cloning, code-space boundary, syndrome extraction, and logical/physical state distinction are not recoverable.
```

### 3.3 Organic synthesis

Native object:

```text
molecule / functional group / reaction route / stereochemical configuration
```

Native distinction to recover:

```text
desired selectivity-controlled route vs unwanted side reaction or wrong product
```

TRACE form:

```text
S := molecular state / precursor / intermediate
T := reaction step with selectivity dimension named: chemoselective, regioselective, stereoselective, or other specified mechanism
C := sequence of reactions, reagent/catalyst/solvent interactions, protecting/deprotecting sequence
O := analytical observation such as NMR, MS, chromatography, yield, stereochemical analysis
K := selectivity, kinetics, thermodynamics, sterics, electronics, chirality, protecting-group compatibility
B := reactive-site boundary / functional-group exposure / stereochemical boundary / route step boundary
I := selectivity/yield/readout entries with type declared
```

I examples:

```text
chemoselectivity := measure_or_route_descriptor / readout_only unless tied to a specific equivalence claim
regioselectivity := measure_or_route_descriptor / readout_only
stereoselectivity := measure_or_route_descriptor / readout_only
enantiomeric excess := measure / readout_only
yield := measure / readout_only
preserved functionality := status_condition / readout_only
```

Loss register:

```text
TRACE does not do retrosynthesis.
TRACE fails if it treats all selectivity as generic route control.
TRACE must preserve which selectivity dimension is at stake.
```

Original back-translation question:

```text
Can a reviewer recover the selectivity problem from the TRACE form?
```

Independent back-translation question:

```text
Can the TRACE form distinguish chemoselectivity, regioselectivity, and stereoselectivity rather than treating all selectivity as one generic route-control constraint?
```

Fail condition:

```text
Fail or mark partial if TRACE can only say desired route vs side reaction without identifying the native selectivity dimension.
```

### 3.4 Generative syntax

Native object:

```text
syntactic object / derivation / tree / feature relation
```

Native distinction to recover:

```text
accessible dependency under formal locality constraints vs inaccessible dependency after phase boundary, island constraint, feature mismatch, or c-command failure
```

TRACE form:

```text
S := syntactic object or derivational state
T := Merge, Agree, movement, feature valuation, spell-out/transfer
C := recursive composition of syntactic objects
O := grammaticality judgment, feature-checking result, interface interpretation
K := locality, c-command, phase impenetrability, feature valuation constraints
B := phase boundary, island boundary, domain of search/probe-goal relation
I := typed formal status or dependency marker
```

I examples:

```text
preserved dependency relation := status_condition / readout_only
grammaticality under target grammar := grammar_relative_status / readout_only
recoverable feature relation := status_condition / readout_only
```

Loss register:

```text
TRACE does not replace syntax.
TRACE fails if phase/access is treated as institutional closure rather than formal derivational constraint.
TRACE must preserve which formal mechanism blocks the dependency.
```

Original back-translation question:

```text
Can a reviewer recover the relevant syntactic constraint, e.g. PIC/locality/feature-checking, from the TRACE form?
```

Independent back-translation question:

```text
Can the TRACE form distinguish a dependency blocked by phase impenetrability from one blocked by island constraints, feature mismatch, or c-command failure?
```

Fail condition:

```text
Fail or mark partial if TRACE only says structure is inaccessible after closure.
```

### 3.5 Epidemiology

Native object:

```text
population compartments / individuals / contact network / pathogen process
```

Native distinction to recover:

```text
controlled transmission process vs uncontrolled spread where effective reproduction remains above control threshold, with causal source disambiguated
```

TRACE form:

```text
S := compartment distribution or network infection state
T := pathogen transmission dynamics, recovery, immunity change, intervention response, behavioural response
C := contact network composition, mixing structure, spatial coupling, population stratification, institutional response coupling
O := surveillance, testing, case counts, wastewater signal, hospitalisation/death data, seroprevalence sampling
K := contact rate, susceptibility, immunity, vaccination, isolation, testing capacity, behaviour, population conservation assumptions where valid
B := contact boundary, compartment boundary, jurisdictional/public-health boundary, quarantine/demographic boundary
I := typed measures/readouts
```

I examples:

```text
R_t := measure / readout_only
R_0 := measure/model parameter / readout_only
incidence := measure / readout_only
prevalence := measure / readout_only
generation interval := measure/distribution / readout_only
hospital capacity margin := measure/status_condition / readout_only
```

Loss register:

```text
TRACE does not replace SIR/SEIR/network modelling.
TRACE fails if high R_t is treated as one generic spread signal without separating biological transmissibility, contact network structure, delayed detection, compliance, and intervention response.
```

Original back-translation question:

```text
Can a reviewer recover whether the problem is transmission mechanics, surveillance delay, intervention delay, compliance, or network heterogeneity?
```

Independent back-translation question:

```text
Can the TRACE form distinguish high R_t due to biological transmissibility from high effective spread due to contact network structure, delayed detection, or behavioural compliance failure?
```

Fail condition:

```text
Fail or mark partial if TRACE only says spread outruns control.
```

### 3.6 Dynamic macroeconomics / DSGE

Native object:

```text
economic state / heterogeneous or representative agents / policy regime / aggregate and distributional variables
```

Native distinction to recover:

```text
DSGE-style forward-looking expectations/equilibrium mechanism vs reduced-form shock-response story; and model dynamics vs lived burden distribution
```

TRACE form:

```text
S := economic state variables / agent states / distributional state
T := shock, expectation update, optimisation response, policy response, consumption/investment/labour adjustment
C := market clearing, sectoral links, household/firm/government interaction, expectation formation, equilibrium coupling
O := observed macro indicators, survey data, prices, employment, debt, distributional measures
K := budget constraints, equilibrium conditions, Euler-style optimisation constraints, policy rules, institutional mandates, liquidity/borrowing constraints
B := sector boundary, household/firm boundary, policy jurisdiction, class/buffer distribution boundary
I := typed model variables/measures/status conditions
```

I examples:

```text
welfare measure := measure / readout_only
output gap := measure / readout_only
inflation := measure / readout_only
unemployment := measure / readout_only
debt-service burden := measure / readout_only
distributional incidence := measure / readout_only
solvency/liquidity condition := status_condition / readout_only
```

Loss register:

```text
TRACE does not solve DSGE models.
TRACE fails if it reduces DSGE to generic shock/lag without preserving expectations, optimisation, and equilibrium structure.
TRACE fails if aggregate welfare is translated into ordinary lived harm without a distributional bridge.
```

Original back-translation question:

```text
Can a reviewer recover whether the TRACE claim is about model dynamics, policy lag, distributional burden, or subject-level harm?
```

Independent back-translation question:

```text
Can the TRACE form distinguish a reduced-form shock-response story from a DSGE-style forward-looking expectations mechanism with equilibrium constraints?
```

Fail condition:

```text
Fail or mark partial if expectations/equilibrium mechanism is not recoverable.
```

### 3.7 Geodynamics

Native object:

```text
fault system / lithospheric plate / stress field / mantle flow process
```

Native distinction to recover:

```text
non-agent physical pressure accumulation vs human-system responsibility for known hazard handling; recurrence estimate vs reliable periodic prediction
```

TRACE form:

```text
S := stress/strain state, fault state, plate configuration
T := plate motion, strain accumulation, rupture, slip, subduction, deformation
C := plate interactions, fault network, mantle-lithosphere coupling
O := seismology, GPS, paleoseismology, hazard maps, geological observation
K := friction, viscosity, rock strength, geometry, conservation laws, boundary conditions
B := fault boundary, plate boundary, locked/slipping segment, hazard-zone boundary
I := typed measures/model outputs/risk descriptors
```

I examples:

```text
strain rate := measure / readout_only
recurrence interval := measure_or_estimate / readout_only; not deterministic prediction
stress drop := measure / readout_only
slip deficit := measure/model estimate / readout_only
hazard probability := measure/model_output / readout_only
infrastructure exposure := measure/bridge_marker / bridge_only
```

Loss register:

```text
TRACE does not replace geophysics.
TRACE fails if recurrence interval implies reliable periodic prediction.
TRACE risks importing responsibility into natural hazard unless a human-system bridge is explicit.
```

Original back-translation question:

```text
Can a reviewer recover whether the claim is about physical process or human preparedness/governance?
```

Independent back-translation question:

```text
Can the TRACE form distinguish recurrence interval as a statistical/historical estimate from reliable periodic prediction of rupture?
```

Fail condition:

```text
Fail or mark partial if TRACE implies periodic predictability from recurrence language.
```

### 3.8 Neurophysiology

Native object:

```text
neuron / synapse / circuit / membrane state / network oscillation
```

Native distinction to recover:

```text
specific circuit-level instability mechanism vs organism-level experience, health, agency, or suffering
```

TRACE form:

```text
S := membrane/circuit/network state
T := spiking, synaptic transmission, plasticity, neuromodulation, pathological excitation
C := network topology, synaptic connectivity, excitation/inhibition balance
O := electrophysiology, imaging, behavioural/clinical signs, reported experience where available
K := ion channels, membrane threshold, inhibitory control, metabolic limits, synaptic weights
B := cellular boundary, synaptic boundary, circuit boundary, organism/experience boundary
I := typed measures/status markers/bridge markers
```

I examples:

```text
firing rate := measure / readout_only
oscillation pattern := measure_or_status_condition / readout_only
excitatory/inhibitory balance := measure_or_status_condition / readout_only
seizure threshold := threshold/status_condition / readout_only
plasticity marker := measure / readout_only
clinical/experiential bridge := bridge_marker / bridge_only
```

Loss register:

```text
TRACE does not replace neuroscience.
TRACE fails if it collapses ion-channel dysfunction, E/I imbalance, topology failure, and metabolic stress into generic amplification.
TRACE risks smuggling consciousness into every signal unless circuit instability is separated from organism-level experience.
```

Original back-translation question:

```text
Can a reviewer recover whether the claim is about cellular/circuit function or subjective/clinical harm?
```

Independent back-translation question:

```text
Can the TRACE form distinguish excitatory/inhibitory imbalance, ion-channel dysfunction, network topology failure, and metabolic stress as different native mechanisms behind similar runaway activity?
```

Fail condition:

```text
Fail or mark partial if TRACE only says amplification exceeds control.
```

## 4. Review labels

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
TRACE_AUTHOR_SELECTED_QUESTION_BIAS
```

## 5. Handling returned reviews

Do not promote TRACE automatically.

```text
STRONG := preserve as pressure signal, not validation
PARTIAL := preserve caveats and decide whether to patch minimally
LOW := demote cross-domain coverage claim
BACKTRANSLATION_FAILURE := patch or demote domain mapping
NATIVE_INVARIANT_LOSS := restore named invariant/measure or demote
FLATTENING / ETHICS_OVERREACH := patch boundary or demote
I_SLOT_DIRECTIONALITY_FAILURE := patch I typing/directionality
AUTHOR_SELECTED_QUESTION_BIAS := keep independent-question requirement
```

## 6. Control note

This is a review instrument, not the theory itself.

It makes TRACE easier to fail.

That is the point.
