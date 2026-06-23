# TRACE Middle-Out Mathematical Support v0.1

Status: mathematical support scaffold. Not proof. Not validation. Not a complete formal theory.

Purpose: support TRACE/ME with the smallest mathematical structure that can carry case graphs, clocks, claim status, correction paths, laundering checks, negative controls, and demotion. This file is deliberately middle-out: it starts from live case structure, not metaphysical axioms or pure implementation details.

```trace
math_support :=
  operational_structure
  + typed_objects
  + partial_orders
  + graph_maps
  + falsifiable_delta_tests
  - not_moral_oracle
  - not_validation
```

---

## 0. Middle-out commitment

TRACE does not begin with a single top axiom such as utility, rights, care, or preference satisfaction.

TRACE also does not begin with a bottom heap of isolated cases.

It begins with a recurring middle object:

```trace
middle_object :=
  bounded_decision_or_transition
  where:
    actor/control exists
    + affected scopes exist
    + claims are made
    + clocks run
    + correction may or may not arrive before hardening
```

Mathematical target:

```math
T := (S_0, A, S_1, E, C, K, R, L)
```

Where:

```trace
S_0 := prior state
A := action / decision / selection
S_1 := possible resulting states
E := bounded entities / affected scopes / controllers
C := claims
K := clocks
R := correction routes
L := loss / residue / unrepaired remainder
```

---

## 1. Basic typed sets

Let:

```math
\mathcal{E} = \{e_1, e_2, ...\}
```

be the set of bounded entities in a case.

```math
\mathcal{C} = \{c_1, c_2, ...\}
```

be the set of claims.

```math
\mathcal{K} = \{k_1, k_2, ...\}
```

be the set of clocks.

```math
\mathcal{R} = \{r_1, r_2, ...\}
```

be the set of correction routes.

```math
\mathcal{A} = \{a_1, a_2, ...\}
```

be the set of available actions or transitions.

Each case graph is then:

```math
G := (V, E_d, \tau)
```

where:

```trace
V := typed vertices drawn from entities, claims, clocks, routes, actions, losses
E_d := directed typed edges
τ := edge/vertex type function
```

A schema-valid case graph is only a well-formed object:

```math
ValidSchema(G) \nRightarrow WellFormed(G)
```

Forbidden implication:

```math
ValidSchema(G) \nRightarrow True(G)
```

---

## 2. Entity role vector

For each entity `e` in case context `s` under action/transition `a`, define a role vector:

```math
M(e,s,a) := \langle P,H,Ctl,K,Ath,R,L \rangle
```

Components:

```trace
P := protectedness / future-space stake
H := harm role
Ctl := control capacity / coercion / culpability-relevant power
K := clocks affecting the entity
Ath := authority claim or authority exposure
R := repair / review / contestability route
L := loss residue
```

Plain version:

```trace
entity_identity := role_in_transition
not noun_category_alone
```

Guard:

```trace
entity_label ≠ moral_status_resolution
role_vector_valid ≠ personhood_claim
```

---

## 3. Claim status as ordered support, not truth

Each claim has a status from a finite status set:

```math
\Sigma_C := \{draft, active, contested, rebutted, superseded, closed, unknown\}
```

Evidence grade:

```math
\Gamma := \{A,B,C,D,U\}
```

Handling status is not truth. Treat it as a bookkeeping function:

```math
status_C : \mathcal{C} \to \Sigma_C
```

```math
evidence : \mathcal{C} \to \Gamma
```

Forbidden implication:

```math
status_C(c)=active \nRightarrow c=true
```

Necessary guard:

```trace
claim_status := inspectability
not truth
```

---

## 4. Clocks and hardening

A clock is a tuple:

```math
k := \langle scope, controller, band, h, challenge \rangle
```

where:

```trace
scope := affected entity or group
controller := who/what controls or influences timing
band := immediate | fast | medium | slow | unknown
h := hardening description
challenge := whether affected scope can contest in time
```

Define a partial order on rough clock bands:

```math
immediate < fast < medium < slow
```

This is not precise time measurement. It is ordinal pressure.

Correction-before-hardening condition:

```math
Beats(r,k) := t_{usable}(r) < t_{harden}(k)
```

When exact time is unknown:

```math
Beats(r,k) := UNKNOWN
```

Guard:

```trace
unknown_clock ≠ pass
unknown_clock ≠ automatic_shutdown
unknown_clock := review_debt
```

---

## 5. Correction route viability

A correction route is:

```math
r := \langle access, authority, evidence, time, enforcement, repair \rangle
```

A route is viable only if the conjunction holds:

```math
Viable(r) := access \land authority \land evidence \land time \land enforcement \land repair
```

TRACE's distinctive correction move is conjunctive failure detection:

```math
\neg Viable(r) \iff \neg access \lor \neg authority \lor \neg evidence \lor \neg time \lor \neg enforcement \lor \neg repair
```

But this is diagnostic, not moral finality.

```trace
formal_route_present ≠ functional_route_alive
```

---

## 6. Laundering as invalid substitution

A laundering candidate is a proposed substitution:

```math
\lambda := X \mapsto Y
```

It becomes laundering when three conditions hold:

```math
Launder(\lambda,G) := Substitute(X,Y) \land LostBurden(\lambda,G) \land ReducedContestability(\lambda,G)
```

Often with beneficiary:

```math
Beneficiary(\lambda,G) \neq \varnothing
```

Examples:

```trace
inquiry ↛ repair
acceptance ↛ implementation
procedure ↛ correction
metric ↛ lived_condition
authority ↛ legitimacy
schema_validity ↛ truth
format_transfer ↛ decision_advantage
```

Guard:

```trace
not_every_substitution_is_laundering
```

A substitution may be innocent compression unless burden, contestability, or authority is distorted.

---

## 7. Dirty action and dirty delay

A dirty action is an action that may prevent or reduce one harm while imposing or risking another.

```math
Dirty(a,G) := \exists s_i,s_j \in Scopes(G): Protects(a,s_i) \land Burdens(a,s_j)
```

Dirty does not mean forbidden by default.

```math
Dirty(a,G) \nRightarrow Record(a,G)
```

Not:

```math
Dirty(a,G) \nRightarrow Prohibited(a)
```

Dirty delay:

```math
DirtyDelay(d,G) := NecessaryOrClaimedDelay(d) \land BurdenDuringDelay(d,G)
```

Core guard:

```trace
necessary_delay ≠ clean_delay
```

DirtyDelayReceipt records the burden rather than pretending due process equals repair.

---

## 8. Decision-delta test

Let `B(x)` be the baseline analysis of case `x`.

Let `T(x)` be the TRACE-assisted analysis of the same case.

Define a decision-relevant delta:

```math
\Delta_D(x) := DecisionRelevant(T(x)) - DecisionRelevant(B(x))
```

This is not a numeric scalar yet. For now it is ordinal / labelled:

```math
\Delta_D \in \{REGRESSION, COMPRESSION\_ONLY, PARTIAL\_DELTA, STRONG\_DELTA, UNKNOWN\}
```

Definitions:

```trace
REGRESSION := TRACE makes analysis worse or more misleading
COMPRESSION_ONLY := same decision substance with new labels
PARTIAL_DELTA := some useful structure, but weak evidence or limited action change
STRONG_DELTA := materially better action/review/repair guidance under fair comparison
UNKNOWN := insufficient or contaminated comparison
```

Critical guard:

```trace
format_difference ≠ decision_delta
```

---

## 9. Negative control criterion

A negative control case has low stakes under stated facts:

```math
N(x) := LowStakes(x) \land SoftClock(x) \land MinimalAuthorityAsymmetry(x) \land OrdinaryContest(x)
```

Expected result:

```math
N(x) \Rightarrow \Delta_D(x) \in \{COMPRESSION\_ONLY, UNKNOWN\}
```

If TRACE generates strong deltas on negative controls:

```math
N(x) \land \Delta_D(x)=STRONG\_DELTA \Rightarrow PatternOverfitAlarm
```

This is the mathematical role of the meeting-time graph.

---

## 10. Transfer-status ladder

Transfer claims must be typed:

```math
\Sigma_T := \{none, format, compression, partial\_decision\_delta, replicated\_decision\_delta, domain\_operational\}
```

Current X057 status:

```math
transfer(X057) = format
```

With caveat:

```trace
self_scored_partial
```

Forbidden upgrade:

```math
format \nRightarrow decision\_delta
```

Upgrade requires evidence:

```math
format + blind\_regrade\_delta + counterbalanced\_replication \Rightarrow partial\_decision\_delta
```

Still not validation.

---

## 11. Repo authority as a partial order

Artifacts have authority states:

```math
\Sigma_A := \{archive, review\_input, live\_working, test\_fixture, control, source\_authority\}
```

Authority does not follow from location or recency:

```math
location(file) \nRightarrow authority(file) \quad \text{is invalid}
```

```math
newer(file) \nRightarrow authority(file) \quad \text{is invalid}
```

Authority must be assigned by control record:

```math
authority(file) := ControlIndex(file)
```

Current default:

```trace
flat_tree := live_working_visible_not_merged
```

---

## 12. Minimal invariants

These are the invariants mathematical support must preserve.

```trace
I1 := schema_valid_not_truth
I2 := claim_status_not_truth
I3 := format_transfer_not_decision_advantage
I4 := procedure_not_repair
I5 := acceptance_not_implementation
I6 := authority_not_legitimacy
I7 := metric_not_lived_condition
I8 := necessary_delay_not_clean_delay
I9 := negative_control_should_idle
I10 := unknown_not_pass
I11 := failure_submission_useful
I12 := ambition_requires_demotability
```

As formulas:

```math
ValidSchema(G) \nRightarrow WellFormed(G) \land \neg TruthCertificate(G)
```

```math
FormatTransfer(x) \nRightarrow \neg DecisionAdvantage(x)
```

```math
Procedure(x) \nRightarrow \neg Repair(x)
```

```math
AuthorityClaim(x) \nRightarrow \neg Legitimacy(x)
```

```math
NegativeControl(x) \land StrongDelta(x) \Rightarrow PatternOverfitAlarm(x)
```

---

## 13. Proof obligations before stronger claims

Before claiming more than format transfer:

```trace
required :=
  blind_regrade
  + counterbalanced_run
  + negative_control_result
  + evidence_status_pinning
  + direct_affected_scope_witness_status
```

Before claiming decision advantage:

```math
\exists x: FairCompare(B(x),T(x)) \land \Delta_D(x) \in \{PARTIAL\_DELTA, STRONG\_DELTA\}
```

Before claiming domain operational usefulness:

```math
\exists D: RepeatedCases(D) \land IndependentUse(D) \land FailureLedger(D) \land NegativeControls(D)
```

Before claiming alignment relevance beyond analogy:

```math
\exists AI\_task: TRACEOutput(AI\_task) changes ActionOrCorrectionRoute before hardening
```

---

## 14. What this support does not prove

```trace
not_proven :=
  morality
  + AI_alignment_solution
  + empirical superiority
  + universal ethics
  + complete harm measure
  + exact clock calculus
  + personhood
  + policy prescription
```

The support is useful only if it produces checks that can fail.

---

## 15. Next mathematical build targets

```trace
next_math_targets :=
  1. define FairCompare(B,T)
  2. define Delta_D rubric as machine-checkable record
  3. define NegativeControl predicate over case graphs
  4. define LaunderingCandidate minimal fields and invalid-substitution test
  5. define DirtyDelayReceipt schema relation to Clock and CorrectionPath
  6. define authority-status propagation rules
  7. define demotion update rule for claims ledger
  8. define case graph validator plus semantic lint checks
```

---

## 16. One-line compression

```trace
TRACE_math :=
  typed transition graph
  + clocked correction viability
  + invalid substitution detection
  + decision-delta comparison
  + negative-control overfit alarm
  + demotion ledger
```

If the math cannot make a claim easier to test or demote, it is decoration.
