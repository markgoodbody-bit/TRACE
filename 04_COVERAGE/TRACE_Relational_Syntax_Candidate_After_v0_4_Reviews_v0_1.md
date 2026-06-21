# TRACE Relational Syntax Candidate After v0.4 Reviews v0.1

Status: candidate note / not applied / not review packet / not validation.  
Source: v0.4 external review aggregation.  
Not: canon promotion, proof of universality, expert endorsement, or replacement for native domain formalism.

## 0. Trigger

v0.4 hardened slot typing:

```text
T native_mechanism_class
C composition_type
K mechanism_type where needed
I type/directionality
```

External review still found a repeated weakness:

```text
TRACE can still function as a structured envelope for pasted native terms.
```

The remaining issue is not primarily slot naming.

The issue is relation representation.

## 1. Current honest status

Earned claim:

```text
TRACE is useful as a disciplined descriptive bridge and pressure language.
```

Unearned claim:

```text
TRACE has a native relational formalism that validates cross-domain mechanisms.
```

Do not make the unearned claim.

## 2. Problem statement

Current form:

```text
TRACE_form(D) := {S, T, C, O, K, B, I}
```

v0.4 improves the typing of each slot.

But a set of typed slots is still mostly node-like.

The missing layer is edge-like:

```text
which slot modifies, constrains, composes, observes, preserves, or updates which other slot?
```

Without an edge layer, the relation is often asserted in prose.

## 3. Candidate relational syntax

Possible extension:

```text
R := typed relation between TRACE slots
```

Candidate expanded form:

```text
TRACE_rel(D) := {S, T, C, O, K, B, I, R}
```

Where:

```text
R := relation_edge(source_slot, relation_type, target_slot, epistemic_status)
```

Example shape:

```text
R(K, constrains, T, declaratively_asserted)
R(C, conditions, T, declaratively_asserted)
R(O, reads, I, declaratively_asserted)
R(T, updates, S, declaratively_asserted)
R(I, preserves_or_tracks, S, declaratively_asserted)
```

This is only a candidate.

## 4. Candidate relation types

Possible relation types:

```text
constrains
conditions
updates
composes
observes
reads
preserves
tracks
blocks
enables
couples
feeds_back_into
routes_to
separates
bridges_to
```

These must remain subordinate to native domain meaning.

## 5. Epistemic status of relations

Every asserted relation should declare epistemic status.

Candidate statuses:

```text
structurally_enforced
native_external_dependency
declaratively_asserted
unverified_claim
metaphor_only
```

Definitions:

```text
structurally_enforced := TRACE itself imposes or checks the dependency
native_external_dependency := native domain formalism establishes the relation, TRACE records it
declaratively_asserted := author states relation; TRACE does not verify it
unverified_claim := relation is plausible but unsupported in the packet
metaphor_only := relation is analogical and should not be treated as native mechanism
```

Current likely status for most v0.4 relations:

```text
native_external_dependency
or
declaratively_asserted
```

Not:

```text
structurally_enforced
```

unless a real checking rule exists.

## 6. Why this matters

The v0.4 reviews exposed that TRACE can appear stronger than it is if relations are merely written in prose.

Example:

```text
K(no_cloning) constrains T(isometric_encoding)
```

This is meaningful only because the native quantum formalism makes it meaningful.

TRACE currently records that dependency.

It does not derive it.

That must be explicit.

## 7. Candidate review question

Future review instruments could add:

```text
For each relation R, state whether TRACE structurally enforces it, whether the native domain externally supplies it, or whether it is only declaratively asserted.
```

And:

```text
If all key relations are declaratively asserted, mark TRACE as descriptive audit language, not relational formalism.
```

## 8. Candidate domain examples

### 8.1 QEC

```text
R(K:no_cloning_constraint, constrains, T:isometric_encoding, native_external_dependency)
R(O:syndrome_extraction, reads, I:syndrome_readout, native_external_dependency)
R(O:syndrome_extraction, must_not_collapse, I:logical_state_equivalence, native_external_dependency)
```

### 8.2 Organic synthesis

```text
R(K:steric_constraint, conditions, T:stereoselective_transformation, native_external_dependency)
R(C:reaction_sequence, conditions, I:yield/readout, declaratively_asserted unless native mechanism specified)
```

### 8.3 DSGE

```text
R(C:expectation_equilibrium_coupling, conditions, T:expectation_update, native_external_dependency)
R(K:budget_constraint, constrains, S:reachable_agent_state, native_external_dependency)
```

### 8.4 Epidemiology

```text
R(C:network_mixing, conditions, T:pathogen_transmission, native_external_dependency)
R(O:surveillance_delay, distorts_or_delays, I:observed_incidence, native_external_dependency)
```

## 9. Risk

Adding R may look like progress while simply moving pasted native prose into another slot.

Avoid this failure:

```text
R as fancy sentence label
```

The useful test is not whether R can be written.

The useful test is whether R forces epistemic status disclosure.

## 10. Decision rule

Do not add R to core TRACE yet.

First test as a candidate review/control surface.

Possible next review question:

```text
Does adding R with epistemic_status reduce the structured-envelope failure, or merely add another place to paste native claims?
```

## 11. Control note

The project should not pretend it has crossed from description into validation.

Current best compression:

```text
TRACE can discipline cross-domain description.
TRACE does not yet enforce cross-domain mechanism.
```
