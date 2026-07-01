# TRACE Harm Primitive Split v0.1

Date: 2026-07-01

Status: structural clarification candidate. Not canon. Not validation. Not proof. Not permission.

Layer: TRACE core / ME boundary clarification.

Purpose: separate descriptive contraction from protected-scope designation so TRACE does not hide normative scope selection inside the harm primitive.

```trace
harm_primitive_split_v0_1 :=
  descriptive_contraction
  + explicit_designation
  + composed_harm_reading
  + visible_scope_blocker
  - hidden_protectedness
  - permission_machine
```

## 1. Problem

Current compressed formulation:

```trace
H := Delta_minus(F)
```

Often glossed as:

```text
harm := reduction in protected future-space under transition
```

This formulation is useful but overloaded.

The term `protected` is doing work inside the harm primitive. That means the supposedly descriptive layer already contains a designation decision: which future-space counts, which entity or scope counts, and which contraction matters.

That is not a fatal defect. It is a boundary issue.

The issue is:

```trace
harm := contraction + protected_designation
```

If the protected designation is hidden, TRACE can appear to describe harm neutrally while silently importing scope membership and value decisions.

## 2. Core clarification

Separate three operations:

```trace
C := descriptive_contraction
D := designation
H := harm_reading_after_designation
```

In plain terms:

1. Something's reachable future-space contracts.
2. A scope is designated as protected, disputed, uncertain, excluded, or unknown.
3. A harm reading is made only after that designation is explicit.

## 3. Descriptive contraction

Define:

```trace
C_e(a,t) := Delta_minus(R_e(t) -> R_e(t+1) | a)
```

Where:

- `e` = entity, system, scope, or candidate scope.
- `a` = action or inaction.
- `R_e(t)` = reachable future-space from state at time `t`.
- `Delta_minus` = reduction, collapse, narrowing, or degradation of reachable future-space under transition.

This is descriptive.

It does not yet say:

- that the contraction is morally wrong;
- that the scope is protected;
- that intervention is justified;
- that repair is owed;
- that a decision-maker has permission to act.

It only says:

```trace
something_reachable_became_less_reachable
```

## 4. Designation

Define:

```trace
D(e,t) in {protected, disputed, uncertain, excluded, unknown}
```

`D` is not derived by TRACE alone.

It may be supplied, contested, revised, or challenged by:

- human ethical reasoning;
- Mechanical Ethics;
- law or institutional rule;
- affected witness;
- scientific model;
- system specification;
- precautionary uncertainty handling;
- later correction.

This is where the scope blocker lives.

```trace
scope_membership_not_solved := true
protectedness_not_machine_derived := true
```

## 5. Harm reading

Define harm as composed:

```trace
H_e(a,t) := C_e(a,t) where D(e,t) in {protected, disputed, uncertain}
```

Stronger form:

```trace
H_e(a,t) := Delta_minus(R_e(t) intersection P_e(t))
```

Where `P_e(t)` is the explicitly designated protected portion of reachable future-space.

If `D(e,t) = unknown`, TRACE should not silently drop the scope. It should carry an uncertainty mark.

```trace
unknown_scope != unprotected_scope
```

## 6. Why this matters

The split prevents four errors.

### 6.1 Hidden normativity

Without the split:

```trace
protected_future_space
```

can look descriptive while carrying an unexamined value decision.

With the split:

```trace
contraction_first
protectedness_explicit
harm_reading_second
```

### 6.2 False clearance

If a system cannot identify a protected scope, it may infer that no protected scope exists.

This is invalid.

```trace
not_seen != not_present
not_designated != not_protected
unknown != safe_to_ignore
```

### 6.3 Scope gerrymandering

A powerful actor can narrow `D` to make contraction invisible.

```trace
scope_control := power_over_harm_visibility
```

Therefore designation itself is a power-relevant act and must be visible to answerability.

### 6.4 Machine translation failure

Descriptive contraction can translate into machine terms: reachability, recoverability, thresholds, feedback loops, integrated drift.

Protectedness does not translate cleanly. It must be supplied as an exogenous designation or loss-shaping choice.

This means the TRACE/ME boundary should not pretend protectedness is machine-discovered.

## 7. Revised layer split

A cleaner stack:

```trace
Layer_0_description :=
  state
  + transition
  + reachable_set
  + contraction
  + propagation
  + recoverability
  + residue
  + clock

Layer_1_designation :=
  protected
  + disputed
  + uncertain
  + excluded
  + unknown

Layer_2_harm_reading :=
  contraction_under_designation

Layer_3_answerability :=
  who_designated
  + who_benefits
  + who_can_challenge
  + whether_correction_remains_reachable
```

Mechanical Ethics carries the human-facing argument about value, protectedness, care, witness, obligation, and why some contractions matter.

TRACE carries the inspectable structure of contraction, time, correction, residue, propagation, designation status, and answerability pressure.

## 8. Behavioural consequence

Under uncertainty, an actor must not rely on `D` being complete.

Minimum operating rule:

```trace
if C_e(a,t) material
and D(e,t) in {protected, disputed, uncertain, unknown}
and correction_after_transition_unreliable
then avoid_or_delay_irreversible_escalation
```

Plain English:

If something may materially reduce a future you do not fully understand, and you cannot correct it later, do not treat missing designation as clearance.

## 9. Relation to correction inequality

The correction inequality remains:

```trace
T_det + T_route + T_corr < T_irr
```

But the split clarifies what the clock is attached to.

There may be:

```trace
C_clock := contraction_detected_before_irreversibility
D_clock := designation_dispute_resolved_before_irreversibility
H_clock := protected_contraction_corrected_before_irreversibility
```

Failure can occur when contraction is visible but designation is delayed past irreversibility.

```trace
designation_latency_can_be_harm_latency
```

## 10. Relation to local operating rules

This split supports the candidate local ruleset without making it authoritative:

```trace
keep_undo := preserve reversibility when D uncertain
keep_door := allow affected scopes to contest D and C
keep_ledger := track repeated C even before final D
keep_slack := preserve correction capacity under D uncertainty
keep_expiry := constraints over candidate scopes require decay and challenge
```

These rules remain constructed-not-tested. They do not certify actions as good.

## 11. Failure modes of this split

### 11.1 Over-expansion

Treating every unknown as protected can paralyse action.

```trace
unknown_scope_as_absolute_protection -> paralysis_risk
```

### 11.2 Under-expansion

Treating only already-recognised scopes as protected hides new or weakly perceived entities.

```trace
recognition_limit -> harm_blindness
```

### 11.3 Designation capture

Whoever controls `D` can control what appears as harm.

```trace
control(D) -> control(harm_visibility)
```

### 11.4 Measurement laundering

A system may measure `C` precisely while manipulating `D` quietly.

```trace
high_precision_contraction_metric + captured_designation := laundering_risk
```

### 11.5 False machine neutrality

A machine system can claim to be merely tracking contractions while its designated set `P` encodes human, institutional, commercial, or adversarial choices.

```trace
machine_neutrality_claim != designation_neutrality
```

## 12. Claim ceiling

This note does not:

- solve scope membership;
- define value;
- decide moral status;
- prove TRACE;
- validate ME;
- grant permission for action;
- provide a final harm metric.

It only:

- separates contraction from designation;
- makes protectedness explicit;
- prevents hidden normativity inside the harm primitive;
- improves translation between ME, TRACE, and machine-facing layers;
- keeps the scope blocker visible.

## 13. Next tests

Apply this split to:

```text
small_case: medical advice drift, e.g. nosebleeds / burns
medium_case: institutional correction delay
extreme_case: irreversible-force decision under uncertainty
machine_case: AI system with side-effect / reachability penalty
```

For each case, ask:

```trace
what_contracts?
who_or_what_is_designated?
who_controls_designation?
what_is_unknown?
can_designation_or_correction_arrive_before_irreversibility?
what_residue_remains?
```

## 14. Minimal kernel

```trace
contraction != harm_until_designation_visible
unknown_designation != clearance
scope_designation_is_power_relevant
TRACE_tracks_contraction_and_clocks
ME_argues_protectedness_and_value
answerability_guards_the_boundary
```

End.
