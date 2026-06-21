# TRACE Invariant v0.2 External Review Aggregation v0.1

Status: external review aggregation / pressure synthesis.  
Sources: Claude, Qwen, Gemini, Z.ai reviews supplied by Mark.  
Not: validation, canon promotion, proof of universality, expert endorsement, or applied patch.

## 0. Reviewed instrument

Instrument reviewed:

```text
TRACE_invariant_review_pack_v0_2_with_questions
```

Core grammar:

```text
TRACE_form(D) := {S, T, C, O, K, B, I}
```

with:

```text
I-slot type/directionality
+ loss register
+ original back-translation question
+ independent back-translation question
```

## 1. Aggregate result

Current aggregate label:

```text
TRACE_INVARIANT_TRANSLATION_PARTIAL
```

Reason:

```text
The invariant/back-translation grammar is stronger than the earlier clock/correction review instrument, but independent back-translation exposes repeated native-mechanism loss and flattening risks.
```

Not validated:

```text
TRACE_INVARIANT_TRANSLATION_STRONG_GLOBAL
```

Not failed globally:

```text
TRACE_LANGUAGE_COVERAGE_FAILED
```

## 2. Repeated findings

### 2.1 I-slot type/directionality defect

Repeated by:

```text
Claude
Qwen
Z.ai
Gemini indirectly in topology and epidemiology via partial/measure typing
```

Shared defect:

```text
I := invariant / measure is not enough.
```

Required hardening:

```text
Every I entry must declare:
- complete_invariant
- partial_invariant
- measure
and directionality:
- bidirectional
- one_directional_difference_only
- readout_only
```

Status:

```text
APPLY_TO_NEXT_PACKET_VERSION
```

### 2.2 Independent back-translation is harder than original back-translation

Repeated by:

```text
Claude
Qwen
Gemini
Z.ai
```

Pattern:

```text
original author-selected back-translation often passes
independent reviewer/question back-translation often fails or becomes partial
```

This is not a reason to abandon TRACE.

It is the falsifier doing work.

Status:

```text
KEEP_IN_REVIEW_INSTRUMENT
```

### 2.3 QIT native mechanism loss

Repeated by:

```text
Qwen
Gemini
Z.ai
Claude partially
```

Defect:

```text
TRACE risks reducing quantum error correction to generic redundancy/noise-resistant backup.
```

Required hardening:

```text
T must distinguish isometric encoding / noisy channel / syndrome-related correction
K must explicitly include no-cloning, non-commutativity, measurement limits, and code-space constraints
O must distinguish syndrome extraction from logical-state readout
I may need layered entries: logical_state_equivalence and syndrome_readout
```

Status:

```text
PATCH_QIT_ENTRY
```

### 2.4 Organic synthesis selectivity flattening

Repeated by:

```text
Claude
Gemini
Z.ai
```

Defect:

```text
TRACE risks collapsing chemoselectivity, regioselectivity, and stereoselectivity into generic route-control/selectivity language.
```

Required hardening:

```text
T/K/B/I must identify which selectivity dimension is at stake.
```

Status:

```text
PATCH_ORGANIC_SYNTHESIS_ENTRY
```

### 2.5 Topology partial-invariant trap

Repeated by:

```text
Claude
Qwen earlier
Gemini
Z.ai earlier
```

Defect:

```text
A named invariant may be partial; same value does not prove equivalence.
```

Required hardening:

```text
I must mark complete vs partial invariant and back-translation must state directionality.
```

Status:

```text
PATCH_TOPOLOGY_ENTRY
```

### 2.6 Epidemiology mechanism pluralism

Repeated by:

```text
Gemini
Claude partially
```

Defect:

```text
R_t as a measure can hide whether spread is driven by biological transmissibility, contact network structure, delayed observation, intervention delay, or compliance failure.
```

Required hardening:

```text
T and C must distinguish pathogen dynamics from network/contact composition and behavioural/institutional response.
```

Status:

```text
PATCH_EPIDEMIOLOGY_ENTRY
```

### 2.7 DSGE expectations / equilibrium thinness

Repeated by:

```text
Claude
Gemini indirectly
Z.ai earlier
```

Defect:

```text
TRACE risks translating DSGE into generic shock/lag without preserving forward-looking expectations, optimisation, and equilibrium constraints.
```

Required hardening:

```text
T/C/K must name expectations/optimisation/equilibrium mechanism explicitly.
```

Status:

```text
PATCH_DSGE_ENTRY
```

### 2.8 Geodynamics recurrence / prediction trap

Repeated by:

```text
Claude
independent-question logic
```

Defect:

```text
Recurrence interval can imply periodic predictability if untyped.
```

Required hardening:

```text
I must mark recurrence interval as measure/estimate/readout_only, not deterministic invariant.
```

Status:

```text
PATCH_GEODYNAMICS_ENTRY
```

## 3. What survived

The following survived better than in the v0.1 clock/correction pack:

```text
K/I separation
loss register
back-translation gate
ethics/governance boundary discipline
native distinction framing
```

Boundary discipline remains strong:

```text
technical failure does not automatically become moral harm
correction/control does not automatically become justice
non-subject domains are not moral subjects
human-system bridge required for responsibility claims
```

## 4. What did not survive strongly

Global strong claim did not survive.

Current result is not:

```text
TRACE_INVARIANT_TRANSLATION_STRONG_GLOBAL
```

because:

```text
independent back-translation fails or becomes partial in several domains
I-slot directionality was under-specified
some native mechanisms remain too generic without explicit slot hardening
```

## 5. Patch decision

The repeated-review threshold is met for applying the I-slot type/directionality hardening to the next review packet.

Also patch the domain entries minimally for:

```text
QIT
algebraic topology
organic synthesis
epidemiology
DSGE macro
geodynamics
```

Neurophysiology remains watchlisted for mechanism pluralism and subject/experience boundary, but the current signal is less repeated than QIT/synthesis/topology.

## 6. Next artifact

Build:

```text
04_COVERAGE/TRACE_Cross_Domain_Invariant_Backtranslation_Review_Packet_v0_3.md
```

Status:

```text
patched review instrument / not validation
```

v0.3 must include:

```text
I-slot type/directionality mandatory
independent back-translation questions mandatory
QIT layered I entries
organic synthesis selectivity dimensions
Topology partial invariant warning
Epidemiology T/C split
DSGE expectations/equilibrium split
Geodynamics recurrence-as-estimate warning
```

## 7. Control note

The review process is now doing real work.

It did not merely approve or reject TRACE.

It identified which part of the bridge grammar carries precision and where the native mechanism leaks out.
