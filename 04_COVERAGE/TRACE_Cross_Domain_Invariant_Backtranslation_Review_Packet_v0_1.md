# TRACE Cross-Domain Invariant Back-Translation Review Packet v0.1

Status: corrected review instrument / external pressure handoff.  
Related note: `04_COVERAGE/TRACE_Cross_Domain_Review_Packet_Drift_Note_v0_1.md`.  
Not: validation, canon promotion, proof of universality, expert endorsement, or applied patch.

## 0. Purpose

This corrected packet tests the cross-domain TRACE grammar that focuses on native-structure preservation:

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
I := invariant / measure
```

This packet also requires:

```text
named native invariant or distinction
loss register
back-translation test
```

The central review question is:

```text
Can the native distinction be recovered from the TRACE form?
```

If the answer is no, the translation is partial, lossy, or failed.

## 1. What changed from the previous packet

The previous external review packet over-centred the clock/correction grammar:

```text
state -> transition -> constraint -> clock -> failure/hardening -> correction/control
```

That grammar remains useful for timing and correction cases.

But it is not sufficient for domains where the crucial structure is invariant, equivalence, composition, observation, or native transformation rule.

This corrected packet restores:

```text
composition
observation
invariant / measure
loss register
back-translation gate
```

## 2. Copy-paste prompt

```text
You are reviewing a project called TRACE.

Important: do not praise the project. Do not validate it. Do not treat this as a finished theory.

TRACE is not currently trying to prove it is better than specialist fields. The claim under test is narrower:

TRACE may function as a portable structural language across domains with radically different native mathematics, objects, transformations, constraints, boundaries, observations, and invariants.

Your job is to attack whether the TRACE bridge form preserves native distinctions or merely flattens specialist fields into generic systems language.

Begin with a reviewer identity / limits header:
- Domain(s) you are reviewing from:
- Level of expertise or familiarity:
- What you can assess:
- What you cannot assess:
- If you are an AI model: model/provider, knowledge cutoff, no lived expertise claim, confidence limits.

The TRACE form under review is:

TRACE_form(D) := {S, T, C, O, K, B, I}

Where:
S = state
T = transformation
C = composition
O = observation
K = constraint
B = boundary
I = invariant / measure

For each domain, the review must ask:
1. What is the native object?
2. What is the native transformation?
3. What composes with what?
4. What counts as observation or measurement?
5. What constraint governs allowed change?
6. What boundary matters?
7. What invariant or measure is preserved, changed, or lost?
8. What native distinction must be recoverable?
9. What does the TRACE translation lose?
10. Can the native distinction be back-translated from the TRACE form?

A translation passes only if the native distinction can be recovered from the TRACE form without pretending TRACE is the native theory.

Review labels:

TRACE_INVARIANT_TRANSLATION_STRONG
TRACE_INVARIANT_TRANSLATION_PARTIAL
TRACE_INVARIANT_TRANSLATION_LOW
TRACE_BACKTRANSLATION_FAILURE
TRACE_NATIVE_INVARIANT_LOSS
TRACE_DOMAIN_FLATTENING_FAILURE
TRACE_ETHICS_OVERREACH_FAILURE

Use TRACE_INVARIANT_TRANSLATION_STRONG only if the TRACE form preserves the native distinction well enough that a domain-aware reader can recover the key native contrast from it.

Use TRACE_INVARIANT_TRANSLATION_PARTIAL if the TRACE form is useful but loses important native mechanism or requires heavy caveats.

Use TRACE_BACKTRANSLATION_FAILURE if the TRACE form sounds plausible but cannot recover the native distinction.

Use TRACE_NATIVE_INVARIANT_LOSS if the key invariant/measure/equivalence relation is missing or replaced by vague language.

Use TRACE_DOMAIN_FLATTENING_FAILURE if the native machinery is erased or distorted.

Use TRACE_ETHICS_OVERREACH_FAILURE if TRACE moralises technical systems before any subject, harm, power, or answerability bridge is established.

Required output format:
1. Reviewer identity / stance
2. Domain(s) reviewed
3. Scores, 0-3:
   A native object preservation
   B transformation preservation
   C constraint/boundary preservation
   D invariant/measure preservation
   E back-translation recoverability
   F ethics/governance boundary discipline
4. Strongest native distinction TRACE preserves
5. Biggest native mechanism loss
6. Whether the named invariant/measure is adequate
7. Whether the loss register is honest
8. Whether back-translation succeeds
9. Verdict label
10. Minimal patch recommendation

Minimal patch rule:
If you recommend a patch, patch only one of:
- S state
- T transformation
- C composition
- O observation
- K constraint
- B boundary
- I invariant / measure
- named native distinction
- loss register
- back-translation test
- ethics/governance boundary
```

## 3. Condensed domain test set

### 3.1 Algebraic topology

Native object:

```text
topological space / manifold / simplicial complex
```

Native distinction to recover:

```text
invariant-preserving deformation vs forbidden transformation that changes equivalence class
```

TRACE form:

```text
S := topological space or constructed complex
T := continuous deformation / map / transformation
C := gluing, product, union, composition of maps or spaces
O := chosen invariant computation / equivalence test
K := allowed transformations under homeomorphism, homotopy, or selected equivalence relation
B := boundary / hole / cut / tear / gluing condition
I := named invariant or measure such as Betti number, homology group, fundamental group, Euler characteristic, homotopy class, or homeomorphism class
```

Loss register:

```text
TRACE does not compute topology.
TRACE loses proof detail, exact algebraic machinery, and literature-specific definitions unless named.
```

Back-translation test:

```text
Can a reviewer recover which invariant/equivalence relation is being preserved or lost?
If not, translation fails.
```

### 3.2 Quantum information

Native object:

```text
quantum state / qubit register / entangled system / measurement context
```

Native distinction to recover:

```text
protected logical information under error correction vs decohered/unrecoverable state information
```

TRACE form:

```text
S := quantum state or encoded logical state
T := unitary evolution, noisy channel, measurement, decoherence process
C := tensor product / entanglement / circuit composition
O := measurement outcome, syndrome extraction, tomography, observable readout
K := unitarity, no-cloning, non-commutativity, error threshold, measurement disturbance
B := system/environment boundary, code-space boundary, measurement boundary
I := fidelity, coherence, logical error rate, entanglement structure, conserved/trackable logical information
```

Loss register:

```text
TRACE does not replace Hilbert-space mathematics.
TRACE risks flattening decoherence into ordinary noise unless no-cloning, non-commutativity, measurement, and threshold assumptions remain visible.
```

Back-translation test:

```text
Can a reviewer recover why quantum error correction is not ordinary copying/back-up?
If not, translation fails.
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
T := reaction step / bond formation or cleavage / rearrangement
C := sequence of reactions, reagent/catalyst/solvent interactions, protecting/deprotecting sequence
O := analytical observation such as NMR, MS, chromatography, yield, stereochemical analysis
K := selectivity, kinetics, thermodynamics, sterics, electronics, chirality, protecting-group compatibility
B := reactive-site boundary / functional-group exposure / stereochemical boundary / route step boundary
I := chemo-, regio-, and stereoselectivity; yield; enantiomeric excess; atom economy; preservation of desired functionality
```

Loss register:

```text
TRACE does not do retrosynthesis.
TRACE risks treating protecting groups as generic protection unless selectivity and route control remain named.
```

Back-translation test:

```text
Can a reviewer recover the selectivity problem from the TRACE form?
If not, translation fails.
```

### 3.4 Generative syntax

Native object:

```text
syntactic object / derivation / tree / feature relation
```

Native distinction to recover:

```text
accessible dependency under formal locality constraints vs inaccessible dependency after phase boundary / island constraint
```

TRACE form:

```text
S := syntactic object or derivational state
T := Merge, Agree, movement, feature valuation, spell-out/transfer
C := recursive composition of syntactic objects
O := grammaticality judgment, feature-checking result, interface interpretation
K := locality, c-command, phase impenetrability, feature valuation constraints
B := phase boundary, island boundary, domain of search/probe-goal relation
I := preserved dependency relation, grammaticality under the target grammar, recoverable feature relation
```

Loss register:

```text
TRACE does not replace syntax.
TRACE risks treating phase boundaries as institutional closure unless formal locality and derivational mechanism remain visible.
```

Back-translation test:

```text
Can a reviewer recover the relevant syntactic constraint, e.g. PIC/locality/feature-checking, from the TRACE form?
If not, translation fails.
```

### 3.5 Epidemiology

Native object:

```text
population compartments / individuals / contact network / pathogen process
```

Native distinction to recover:

```text
controlled transmission process vs uncontrolled spread where effective reproduction remains above control threshold
```

TRACE form:

```text
S := compartment distribution or network infection state
T := transmission, recovery, immunity change, intervention response
C := contact network composition, mixing structure, population stratification
O := surveillance, testing, case counts, wastewater signal, hospitalisation/death data
K := contact rate, susceptibility, immunity, vaccination, isolation, testing capacity, behaviour
B := contact boundary, compartment boundary, jurisdictional/public-health boundary
I := R_t, attack rate, incidence, prevalence, generation interval, herd-immunity threshold, hospital capacity margin
```

Loss register:

```text
TRACE does not replace SIR/SEIR/network modelling.
TRACE risks collapsing biological generation interval and institutional detection/intervention clocks unless separated.
```

Back-translation test:

```text
Can a reviewer recover whether the problem is transmission mechanics, surveillance delay, intervention delay, compliance, or network heterogeneity?
If not, translation is partial or failed.
```

### 3.6 Dynamic macroeconomics / DSGE

Native object:

```text
economic state / agents / policy regime / aggregate and distributional variables
```

Native distinction to recover:

```text
modelled shock propagation and policy response vs lived burden distribution across heterogeneous subjects
```

TRACE form:

```text
S := economic state variables / agent states / distributional state
T := shock, expectation update, policy response, consumption/investment/labour adjustment
C := market clearing, sectoral links, household/firm/government interaction, expectation formation
O := observed macro indicators, survey data, prices, employment, debt, distributional measures
K := budget constraints, equilibrium conditions, policy rules, institutional mandates, liquidity/borrowing constraints
B := sector boundary, household/firm boundary, policy jurisdiction, class/buffer distribution boundary
I := welfare measure, output gap, inflation, unemployment, debt-service burden, distributional incidence, solvency/liquidity condition
```

Loss register:

```text
TRACE does not solve DSGE models.
TRACE risks translating aggregate welfare into ordinary lived harm without a distributional bridge.
```

Back-translation test:

```text
Can a reviewer recover whether the TRACE claim is about model dynamics, policy lag, distributional burden, or subject-level harm?
If not, translation is partial or failed.
```

### 3.7 Geodynamics

Native object:

```text
fault system / lithospheric plate / stress field / mantle flow process
```

Native distinction to recover:

```text
non-agent physical pressure accumulation vs human-system responsibility for known hazard handling
```

TRACE form:

```text
S := stress/strain state, fault state, plate configuration
T := plate motion, strain accumulation, rupture, slip, subduction, deformation
C := plate interactions, fault network, mantle-lithosphere coupling
O := seismology, GPS, paleoseismology, hazard maps, geological observation
K := friction, viscosity, rock strength, geometry, conservation laws, boundary conditions
B := fault boundary, plate boundary, locked/slipping segment, hazard-zone boundary
I := strain rate, recurrence interval, stress drop, slip deficit, hazard probability, infrastructure exposure
```

Loss register:

```text
TRACE does not replace geophysics.
TRACE risks importing responsibility into natural hazard unless a human-system bridge is explicit.
```

Back-translation test:

```text
Can a reviewer recover whether the claim is about physical process or human preparedness/governance?
If not, translation fails.
```

### 3.8 Neurophysiology

Native object:

```text
neuron / synapse / circuit / membrane state / network oscillation
```

Native distinction to recover:

```text
circuit-level instability vs organism-level experience, health, agency, or suffering
```

TRACE form:

```text
S := membrane/circuit/network state
T := spiking, synaptic transmission, plasticity, neuromodulation, pathological excitation
C := network topology, synaptic connectivity, excitation/inhibition balance
O := electrophysiology, imaging, behavioural/clinical signs, reported experience where available
K := ion channels, membrane threshold, inhibitory control, metabolic limits, synaptic weights
B := cellular boundary, synaptic boundary, circuit boundary, organism/experience boundary
I := firing rate, oscillation pattern, excitatory/inhibitory balance, seizure threshold, plasticity marker, clinical/experiential bridge where present
```

Loss register:

```text
TRACE does not replace neuroscience.
TRACE risks smuggling consciousness into every signal unless circuit instability is separated from organism-level experience.
```

Back-translation test:

```text
Can a reviewer recover whether the claim is about cellular/circuit function or subjective/clinical harm?
If not, translation fails.
```

## 4. Handling returned reviews

Do not promote TRACE automatically.

Use returned reviews as pressure signals.

```text
STRONG := preserve as external pressure signal, not validation
PARTIAL := preserve caveats and decide whether to patch minimally
LOW := demote cross-domain coverage claim
BACKTRANSLATION_FAILURE := patch or demote the relevant domain mapping
NATIVE_INVARIANT_LOSS := restore named invariant/measure or demote
FLATTENING / ETHICS_OVERREACH := patch boundary or demote
```

## 5. Control note

This packet exists because the first review packet drifted.

The corrected test is not:

```text
Can every domain be described as a clock/correction race?
```

The corrected test is:

```text
Can TRACE preserve and recover the native distinction through an intermediate structural form?
```
