# TRACE Relational Syntax QEC Hostile Review Prompt v0.1

Status: hostile review prompt / single-domain R candidate pressure test.  
Target file: `04_COVERAGE/TRACE_Relational_Syntax_QEC_Single_Domain_Test_v0_1.md`.  
Not: validation, canon promotion, v0.5 review packet, proof of universality, or core R adoption.

## 0. Purpose

This prompt asks an external reviewer to attack the QEC-only `R` candidate.

The review question is narrow:

```text
Does adding explicit relation edges reduce the structured-envelope failure, or merely add another place to paste native claims?
```

Do not review broad TRACE.

Do not decide whether TRACE is a universal language.

Do not validate QEC translation.

Attack only the candidate `R` layer.

## 1. Reviewer identity header

Begin with:

```text
Reviewer identity / stance:
Domain reviewed:
Level of expertise or familiarity:
What I can assess:
What I cannot assess:
If AI: model/provider, knowledge cutoff, no lived expertise claim, confidence limits:
```

## 2. Source material

The candidate extension is:

```text
TRACE_rel(QEC) := {S, T, C, O, K, B, I, R}
```

Where:

```text
R := relation_edge(source, relation_type, target, epistemic_status)
```

Baseline QEC slots:

```text
S := encoded logical state plus physical substrate state
T := isometric encoding / unitary evolution / noisy channel / syndrome-conditioned correction / measurement-decoherence process
C := tensor_or_entanglement_composition / circuit_composition / code_block_composition
O := syndrome_extraction / physical_measurement_outcome / logical_state_readout_where_valid
K := no_cloning_constraint / non_commutativity_constraint / measurement_constraint / code_space_constraint / threshold_assumption
B := system-environment boundary / code-space boundary / logical-physical boundary / syndrome-logical readout boundary
I := logical_state_equivalence / syndrome_readout / logical_error_rate / fidelity
```

Typed I entries:

```text
logical_state_equivalence := complete_invariant / bidirectional within protected code assumptions
syndrome_readout := measure / readout_only
logical_error_rate := measure / readout_only
fidelity := measure / readout_only
```

Candidate R edges:

```text
R(T:isometric_encoding, embeds, S:logical_state_into_code_space, native_external_dependency)
R(K:no_cloning_constraint, blocks, T:ordinary_copying_of_unknown_quantum_state, native_external_dependency)
R(K:code_space_constraint, constrains, T:syndrome_conditioned_correction, native_external_dependency)
R(O:syndrome_extraction, reads, I:syndrome_readout, native_external_dependency)
R(O:syndrome_extraction, must_not_be_treated_as, I:logical_state_equivalence, native_external_dependency)
R(T:noisy_channel, perturbs, S:physical_substrate_state, native_external_dependency)
R(T:syndrome_conditioned_correction, attempts_to_restore, I:logical_state_equivalence, native_external_dependency)
```

The internal test verdict was:

```text
R_REDUCES_STRUCTURED_ENVELOPE_RISK_PARTIALLY
```

Internal claim:

```text
R is useful as an honesty/epistemic-status layer.
R is not yet a mechanism-validation layer.
```

## 3. Review task

Score 0-3:

```text
A. Does R add clarity beyond prose?
B. Does R reduce the structured-envelope problem?
C. Does R prevent QEC from collapsing into classical redundancy?
D. Does R correctly mark native dependencies as external rather than TRACE-enforced?
E. Does R avoid pretending to validate QEC mechanisms?
F. Does R deserve to remain as a candidate review/control surface?
```

## 4. Attack questions

Answer directly:

```text
1. Is R doing real work, or is it just prose in edge notation?
2. Does `native_external_dependency` honestly limit TRACE's claim, or does it merely launder native authority through TRACE notation?
3. Can the R edges detect a false QEC relation, or only record a relation supplied by the author?
4. Does the edge format make the logical/physical/syndrome distinction clearer than prose alone?
5. Does the edge format reduce author-selected-question bias?
6. Does the QEC R test justify trying R on another domain?
7. What would make R fail immediately?
```

## 5. Verdict labels

Use one or more:

```text
R_KEEP_AS_EPISTEMIC_STATUS_LAYER
R_DEMOTE_TO_PROSE_AID
R_KILL_AS_CORE_CANDIDATE
R_STRUCTURED_ENVELOPE_REMAINS
R_REDUCES_ENVELOPE_RISK_PARTIALLY
R_NATIVE_AUTHORITY_LAUNDERING_RISK
R_FANCY_SENTENCE_LABEL_FAILURE
R_READY_FOR_SECOND_DOMAIN_TEST
R_NOT_READY_FOR_SECOND_DOMAIN_TEST
```

## 6. Required output format

```text
1. Reviewer identity / stance
2. Domain reviewed
3. Scores A-F
4. Strongest thing R adds
5. Biggest remaining structured-envelope risk
6. Whether R adds clarity beyond prose
7. Whether R prevents overclaim or launders native authority
8. Whether R can detect false relations
9. Whether to keep, demote, or kill R
10. Whether to test R on a second domain
11. Verdict label(s)
12. Minimal patch recommendation
```

## 7. Patch rule

Patch only one of:

```text
relation_type vocabulary
epistemic_status vocabulary
edge syntax
loss register
kill/demote condition
second-domain test condition
```

Do not patch TRACE core.

Do not propose broad R adoption.

## 8. Control note

A negative review is useful.

If R is only fancy prose, demote it.

If R only helps disclose epistemic status, keep it as a review/control surface but do not promote it.

If R can actually expose false relation claims better than prose, then and only then consider a second-domain test.
