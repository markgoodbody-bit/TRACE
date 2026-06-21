# TRACE Invariant I-Slot Type Directionality Patch Candidate v0.1

Status: candidate patch / not applied / pending repeated review or consolidation choice.  
Source: Claude review of `TRACE_Cross_Domain_Invariant_Backtranslation_Review_Packet_v0_1`.  
Not: applied patch, validation, canon promotion, proof of universality, or new operator layer.

## 0. Purpose

This file preserves the minimal patch candidate identified in the first returned review of the corrected invariant/back-translation pack.

The issue:

```text
The I slot currently combines invariant and measure.
```

This is useful shorthand, but it can hide directionality.

## 1. Problem

Current slot:

```text
I := invariant / measure
```

Problem:

```text
complete invariants, partial invariants, and measures are not the same thing.
```

If this is left untyped, a reviewer may mistake:

```text
same value
```

for:

```text
same native class / same system state / same equivalence relation
```

when that inference is not warranted.

## 2. Type distinction

Patch candidate:

```text
Every I entry must declare type and directionality.
```

Allowed types:

```text
complete_invariant
partial_invariant
measure
```

Definitions:

```text
complete_invariant := determines the equivalence class; back-translation is bidirectional
partial_invariant := one-directional only; different value may prove difference, same value does not prove equivalence
measure := varying readout or diagnostic quantity, not class-determining
```

Directionality field:

```text
bidirectional := same I means same class, different I means different class
one_directional_difference_only := different I may show difference; same I does not prove equivalence
readout_only := tracks state or behaviour but does not define equivalence class
```

## 3. Domain examples

### 3.1 Algebraic topology

Existing I examples:

```text
Betti number
homology group
fundamental group
Euler characteristic
homotopy class
homeomorphism class
```

Patch discipline:

```text
Do not mark all topology I entries as complete invariants.
```

Example:

```text
Betti numbers := partial_invariant / one_directional_difference_only
```

Reason:

```text
Equal Betti numbers do not necessarily prove homeomorphism or full equivalence.
```

### 3.2 Quantum information

Existing I examples:

```text
fidelity
coherence
logical error rate
entanglement structure
conserved/trackable logical information
```

Patch discipline:

```text
Most entries are measures/readouts or structural descriptors, not complete invariants.
```

Example:

```text
logical error rate := measure / readout_only
```

### 3.3 Organic synthesis

Existing I examples:

```text
chemo-, regio-, and stereoselectivity
yield
enantiomeric excess
atom economy
preservation of desired functionality
```

Patch discipline:

```text
These are mostly measures or route-quality descriptors, not equivalence-class invariants.
```

Example:

```text
enantiomeric excess := measure / readout_only
selectivity := measure_or_structural_route_descriptor / readout_only unless tied to a specific equivalence claim
```

### 3.4 Generative syntax

Existing I examples:

```text
preserved dependency relation
grammaticality under target grammar
recoverable feature relation
```

Patch discipline:

```text
Mark whether I is a formal well-formedness condition, dependency relation, or grammar-relative measure.
```

Example:

```text
grammaticality under target grammar := grammar_relative_status / readout_only
```

### 3.5 Epidemiology

Existing I examples:

```text
R_t
attack rate
incidence
prevalence
generation interval
herd-immunity threshold
hospital capacity margin
```

Patch discipline:

```text
These are measures/readouts or thresholds, not invariants in the topology sense.
```

Example:

```text
R_t := measure / readout_only
generation interval := measure/distribution / readout_only
```

### 3.6 DSGE macroeconomics

Existing I examples:

```text
welfare measure
output gap
inflation
unemployment
debt-service burden
distributional incidence
solvency/liquidity condition
```

Patch discipline:

```text
Most are model variables, diagnostics, or welfare measures, not invariants.
```

Example:

```text
output gap := measure / readout_only
solvency condition := constraint/status condition, not complete invariant
```

### 3.7 Geodynamics

Existing I examples:

```text
strain rate
recurrence interval
stress drop
slip deficit
hazard probability
infrastructure exposure
```

Patch discipline:

```text
These are measures, estimates, or risk descriptors; recurrence interval must not imply reliable periodicity.
```

Example:

```text
recurrence interval := measure/estimate / readout_only
hazard probability := measure/model_output / readout_only
```

### 3.8 Neurophysiology

Existing I examples:

```text
firing rate
oscillation pattern
excitatory/inhibitory balance
seizure threshold
plasticity marker
clinical/experiential bridge where present
```

Patch discipline:

```text
These are measures, thresholds, or bridge markers, not class-determining invariants.
```

Example:

```text
firing rate := measure / readout_only
clinical/experiential bridge := evidence bridge, not invariant
```

## 4. Proposed wording patch for future packets

Add after `I := invariant / measure`:

```text
Every I entry must declare its type and directionality:
- complete_invariant: determines the equivalence class; bidirectional back-translation
- partial_invariant: different value may show difference, but same value does not prove equivalence
- measure: varying readout or diagnostic quantity, not class-determining
```

Add to back-translation test:

```text
Back-translation must state whether the I entry is complete, partial, or only a measure/readout. If directionality is unclear, mark the translation PARTIAL.
```

## 5. Application rule

Do not apply automatically.

Apply if:

```text
another reviewer repeats this defect
or internal logic confirms the patch as clearly necessary
or Mark chooses consolidation mode
```

If applied, patch:

```text
04_COVERAGE/TRACE_Cross_Domain_Invariant_Backtranslation_Review_Packet_v0_1.md
```

and any derived downloadable packet.

## 6. Control note

This patch is not theory expansion.

It is instrument hardening.

It prevents a successful-looking back-translation from hiding false equivalence.
