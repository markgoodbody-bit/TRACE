# TRACE Relational Syntax Epistemic Status Patch Candidate v0.1

Status: patch candidate / not applied / not core / not validation.  
Source: Claude hostile review of QEC R candidate.  
Not: core R adoption, second-domain test, proof of mechanism validation, or replacement for native formalism.

## 0. Trigger

Claude's QEC hostile review found that all candidate R edges used the same epistemic status:

```text
native_external_dependency
```

Finding:

```text
A status field with one value is a disclaimer, not a disclosure layer.
```

This is material.

If R is justified as an epistemic-status layer, its epistemic-status field must discriminate.

## 1. Current defect

Current R shape:

```text
R := relation_edge(source, relation_type, target, epistemic_status)
```

Current problem:

```text
All QEC edges can be marked native_external_dependency, including both true and false edges.
```

False-edge probe:

```text
R(O:syndrome_extraction, reads, I:logical_state_equivalence, native_external_dependency)
```

Problem:

```text
R can notate this false edge as easily as the correct prohibitive edge.
```

Therefore:

```text
R does not detect false relations.
R only records author-supplied relation claims.
```

## 2. Patch target

Patch target:

```text
epistemic_status vocabulary
```

Patch purpose:

```text
Make epistemic status carry discriminating information.
```

## 3. Candidate epistemic-status values

Replace or supplement the previous broad statuses with:

```text
native_theorem
native_formal_condition
native_empirical_assumption
native_model_assumption
author_claim
analogy_only
trace_conjecture
unverified_or_unsupported
```

Definitions:

```text
native_theorem := established by native formal theory at theorem/proof level
native_formal_condition := valid only under stated formal conditions or code/model assumptions
native_empirical_assumption := supported by empirical/domain practice, not formal theorem
native_model_assumption := true inside a selected model, not globally native-true
author_claim := asserted by the TRACE author or translator
analogy_only := analogy, not native mechanism
trace_conjecture := proposed TRACE-side relation not established by native domain
unverified_or_unsupported := relation lacks support in current packet
```

## 4. Discrimination rule

For any domain R map:

```text
A valid epistemic-status layer should normally contain at least two distinct epistemic_status values.
```

If every edge has the same status:

```text
R_STATUS_FIELD_NON_DISCRIMINATING
```

If a false edge can be assigned the same status as a true edge without contradiction:

```text
R_FALSE_EDGE_NOT_DETECTED
```

If statuses cannot be justified:

```text
R_NATIVE_AUTHORITY_LAUNDERING_RISK
```

## 5. QEC revised status examples

### 5.1 No-cloning edge

```text
R(K:no_cloning_constraint, blocks, T:ordinary_copying_of_unknown_quantum_state, native_theorem)
```

Reason:

```text
No-cloning is theorem-level native support.
```

### 5.2 Code-space correction edge

```text
R(K:code_space_constraint, constrains, T:syndrome_conditioned_correction, native_formal_condition)
```

Reason:

```text
Correction depends on stated code/correctability conditions.
```

### 5.3 Syndrome readout edge

```text
R(O:syndrome_extraction, reads, I:syndrome_readout, native_formal_condition)
```

Reason:

```text
Syndrome readout is defined inside the selected QEC/stabilizer/code structure.
```

### 5.4 Logical-state non-collapse edge

```text
R(O:syndrome_extraction, must_not_be_treated_as, I:logical_state_equivalence, native_formal_condition)
```

Reason:

```text
This separation depends on the syndrome/logical structure of the code and valid measurement design.
```

### 5.5 Threshold/correction performance edge

```text
R(T:syndrome_conditioned_correction, attempts_to_restore, I:logical_state_equivalence, native_model_assumption)
```

Reason:

```text
Restoration depends on assumptions about error model, correction capacity, and threshold regime.
```

### 5.6 False edge probe

```text
R(O:syndrome_extraction, reads, I:logical_state_equivalence, native_theorem)
```

Expected result:

```text
Reject or flag as inconsistent with QEC boundary discipline.
```

But this rejection still requires native QEC knowledge or a manually supplied incompatibility rule.

Therefore:

```text
R can become a better disclosure layer.
R still does not become a native checker unless false-edge rules are added.
```

## 6. Negative/prohibitive edge note

Claude identified the strongest R edge type as prohibitive:

```text
must_not_be_treated_as
blocks
```

Reason:

```text
Prohibitive edges can name what would count as a native failure if violated.
```

Candidate later extension, not applied here:

```text
violation_consequence
```

Example:

```text
R(O:syndrome_extraction, must_not_be_treated_as, I:logical_state_equivalence, native_formal_condition, violation_consequence := logical_state_readout_collapse_or_QEC_to_classical_redundancy_failure)
```

Do not apply automatically.

## 7. Current decision

After Claude's hostile review:

```text
R_DEMOTE_TO_PROSE_AID
R_NATIVE_AUTHORITY_LAUNDERING_RISK
R_NOT_READY_FOR_SECOND_DOMAIN_TEST
```

Conditional survival:

```text
R_KEEP_AS_EPISTEMIC_STATUS_LAYER
```

only if the status field becomes discriminating and reviewers agree it adds clarity beyond prose.

## 8. Stop rule

Do not test R on a second domain yet.

Do not add R to core TRACE.

Do not build a broad R review pack.

First question:

```text
Does discriminating epistemic_status reduce the laundering risk, or is R still fancy prose?
```

## 9. Control note

This patch candidate preserves the critique rather than hiding it.

R's current ceiling:

```text
epistemic-status disclosure aid
```

not:

```text
mechanism validation layer
```
