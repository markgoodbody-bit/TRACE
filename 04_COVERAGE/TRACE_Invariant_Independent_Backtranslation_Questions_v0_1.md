# TRACE Invariant Independent Back-Translation Questions v0.1

Status: adversarial test-question set / not validation / not applied patch.  
Source: Claude review of `TRACE_Cross_Domain_Invariant_Backtranslation_Review_Packet_v0_1`.  
Not: canon promotion, proof of universality, expert endorsement, or new operator layer.

## 0. Purpose

The corrected invariant/back-translation review packet asks pre-selected back-translation questions.

Claude's process warning:

```text
The back-translation gate is the falsifiable part, but the packet partially grades its own well-chosen exam.
```

This file adds second, independent back-translation questions per domain.

Use them to test whether TRACE can recover native distinctions it did not pre-select.

## 1. Test rule

For each domain, a reviewer should answer:

```text
Can the TRACE form recover this independent native distinction?
```

Scores:

```text
0 := no, back-translation fails
1 := weakly, but key native mechanism is lost
2 := mostly, with caveats
3 := yes, native distinction is recoverable as bridge language
```

If the reviewer cannot answer because the TRACE form lacks the required native invariant, mark:

```text
TRACE_BACKTRANSLATION_FAILURE
```

or:

```text
TRACE_NATIVE_INVARIANT_LOSS
```

## 2. Independent questions by domain

### 2.1 Algebraic topology

Original packet question:

```text
Can a reviewer recover which invariant/equivalence relation is being preserved or lost?
```

Independent question:

```text
Can the TRACE form distinguish between two spaces sharing the same selected homology/Betti profile but not being equivalent under the target relation?
```

Reason:

```text
This tests whether the I slot marks complete vs partial invariant and prevents the false converse: same invariant value implies same native class.
```

Fail condition:

```text
If TRACE cannot say whether the named invariant is complete, partial, or only diagnostic, mark partial or failed.
```

### 2.2 Quantum information

Original packet question:

```text
Can a reviewer recover why quantum error correction is not ordinary copying/back-up?
```

Independent question:

```text
Can the TRACE form distinguish ordinary classical redundancy from quantum error correction that preserves logical information without cloning an unknown quantum state?
```

Reason:

```text
This tests whether no-cloning, syndrome extraction, code-space boundary, and logical-vs-physical state distinction are recoverable.
```

Fail condition:

```text
If TRACE reduces QEC to backup/redundancy under noise, mark native mechanism loss.
```

### 2.3 Organic synthesis

Original packet question:

```text
Can a reviewer recover the selectivity problem from the TRACE form?
```

Independent question:

```text
Can the TRACE form distinguish chemoselectivity, regioselectivity, and stereoselectivity rather than treating all selectivity as one generic route-control constraint?
```

Reason:

```text
This tests whether selectivity is a named native mechanism or just an umbrella term.
```

Fail condition:

```text
If TRACE can only say desired route vs side reaction, but cannot identify which selectivity dimension is at stake, mark partial.
```

### 2.4 Generative syntax

Original packet question:

```text
Can a reviewer recover the relevant syntactic constraint, e.g. PIC/locality/feature-checking, from the TRACE form?
```

Independent question:

```text
Can the TRACE form distinguish a dependency blocked by phase impenetrability from one blocked by island constraints, feature mismatch, or c-command failure?
```

Reason:

```text
This tests whether formal locality machinery is recoverable, not merely generic access/closure.
```

Fail condition:

```text
If TRACE only says structure is inaccessible after closure, mark partial or native mechanism loss.
```

### 2.5 Epidemiology

Original packet question:

```text
Can a reviewer recover whether the problem is transmission mechanics, surveillance delay, intervention delay, compliance, or network heterogeneity?
```

Independent question:

```text
Can the TRACE form distinguish high R_t due to biological transmissibility from high effective spread due to contact network structure, delayed detection, or behavioural compliance failure?
```

Reason:

```text
This tests whether I and T separate pathogen dynamics, network structure, observation lag, and intervention response.
```

Fail condition:

```text
If TRACE only says spread outruns control, mark partial.
```

### 2.6 Dynamic macroeconomics / DSGE

Original packet question:

```text
Can a reviewer recover whether the TRACE claim is about model dynamics, policy lag, distributional burden, or subject-level harm?
```

Independent question:

```text
Can the TRACE form distinguish a reduced-form shock-response story from a DSGE-style forward-looking expectations mechanism with equilibrium constraints?
```

Reason:

```text
This tests whether expectations, optimisation, and equilibrium structure remain visible rather than collapsing into generic shock and lag.
```

Fail condition:

```text
If TRACE cannot recover the expectations/equilibrium mechanism, mark partial or native mechanism loss.
```

### 2.7 Geodynamics

Original packet question:

```text
Can a reviewer recover whether the claim is about physical process or human preparedness/governance?
```

Independent question:

```text
Can the TRACE form distinguish recurrence interval as a statistical/historical estimate from reliable periodic prediction of rupture?
```

Reason:

```text
This tests whether I slot measures are typed as uncertain readouts rather than deterministic invariants.
```

Fail condition:

```text
If TRACE implies periodic predictability from recurrence language, mark native mechanism loss or measure-directionality failure.
```

### 2.8 Neurophysiology

Original packet question:

```text
Can a reviewer recover whether the claim is about cellular/circuit function or subjective/clinical harm?
```

Independent question:

```text
Can the TRACE form distinguish excitatory/inhibitory imbalance, ion-channel dysfunction, network topology failure, and metabolic stress as different native mechanisms behind similar runaway activity?
```

Reason:

```text
This tests whether the form preserves mechanism pluralism rather than flattening everything into signal amplification.
```

Fail condition:

```text
If TRACE only says amplification exceeds control, mark partial.
```

## 3. Aggregate review instruction

For a corrected external review, ask each reviewer to answer both:

```text
A. the original back-translation question
B. the independent back-translation question
```

Then compare:

```text
original pass + independent pass := stronger signal
original pass + independent fail := possible author-selected-question bias
original fail := translation weak or under-specified
```

## 4. Handling labels

Use:

```text
TRACE_INDEPENDENT_BACKTRANSLATION_PASS
TRACE_INDEPENDENT_BACKTRANSLATION_PARTIAL
TRACE_INDEPENDENT_BACKTRANSLATION_FAILURE
TRACE_AUTHOR_SELECTED_QUESTION_BIAS
TRACE_NATIVE_MECHANISM_LOSS
TRACE_I_SLOT_DIRECTIONALITY_FAILURE
```

## 5. Control note

This file makes TRACE easier to falsify.

That is the point.

A universal bridge language that only survives its own chosen examples is not yet a universal bridge language.
