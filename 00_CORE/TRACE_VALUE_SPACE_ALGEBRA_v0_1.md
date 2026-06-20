# TRACE Value-Space Algebra v0.1

Status: core refinement / kernel patch surface.  
Parent files: `TRACE_FUTURE_SPACE_AND_CONTINUATION_v0_1.md`, `TRACE_NON_AGGREGATION_GUARD_v0_1.md`.  
Reason: fresh-reader critique correctly found that profile-valued `C^+_e` and scalar `ΔH_e` / `max` / `sum` operations were not yet reconciled.

## 0. Purpose

This note defines the value/profile space used by positive continuation and harm comparison.

It prevents TRACE from pretending that relation, play, meaning, capability, and survival can be naively added as one scalar.

It also prevents non-aggregation guards from relying on undefined `max` or `sum` over profile-valued harm.

## 1. Value Profile Space

For entity `e`, define a set of value dimensions:

```math
D_e = \{d_1, d_2, ..., d_k\}
```

Example dimensions may include:

```text
survival
bodily_integrity
agency
capability
relation
belonging
play
meaning
growth
truth_access
repair_access
continuity
```

Define the profile space:

```math
V_e = \prod_{d∈D_e} S_d
```

where each `S_d` is a bounded ordered scale:

```math
S_d = [0,1]
```

or another explicitly declared bounded partially ordered set.

A value profile is:

```math
v_e ∈ V_e
```

and has components:

```math
v_{e,d}
```

## 2. Positive Continuation as Profile Map

Positive continuation is a map from future states to value profiles:

```math
C^+_e : F_e(t) \to V_e
```

For future state `f`:

```math
C^+_e(f) = v_e(f)
```

This is not a scalar unless a scalar projection is explicitly declared.

## 3. Partial Order

Define weak dominance:

```math
v_1 \succeq v_2 \iff \forall d∈D_e: v_{1,d} ≥ v_{2,d}
```

Define strict dominance:

```math
v_1 \succ v_2 \iff v_1 \succeq v_2 \land \exists d: v_{1,d} > v_{2,d}
```

If neither profile dominates the other, they are incomparable:

```math
v_1 \parallel v_2
```

This is expected, not a bug.

Many ethical collisions are cases of profile incomparability.

## 4. Profile Loss

Given action `a`, expected future profile:

```math
E[v_e(t+\Delta t) | a]
```

Current profile:

```math
v_e(t)
```

Profile loss:

```math
\delta_e(a) = \max(0, v_e(t) - E[v_e(t+\Delta t) | a])
```

Componentwise:

```math
\delta_{e,d}(a) = \max(0, v_{e,d}(t) - E[v_{e,d}(t+\Delta t) | a])
```

So `δ_e(a)` is a vector/profile of losses, not automatically a scalar.

## 5. Scalar Harm Projection

A scalar harm value is permitted only after declaring a projection:

```math
σ_e : V_e \to \mathbb{R}
```

The projection must be monotone:

```math
v_1 \succeq v_2 \Rightarrow σ_e(v_1) ≥ σ_e(v_2)
```

Projected harm:

```math
\Delta H^σ_e(a) = σ_e(v_e(t)) - E[σ_e(v_e(t+\Delta t)) | a]
```

This is a declared modelling choice, not the root truth.

If no projection is declared, use profile loss `δ_e(a)` and partial-order comparison.

## 6. Floors

For protected dimensions, define floor thresholds:

```math
Floor_e = \{\theta_{e,d}^{floor} : d∈D_e^{protected}\}
```

A floor breach occurs when:

```math
E[v_{e,d}(t+\Delta t)|a] < \theta_{e,d}^{floor}
```

for any protected dimension `d`.

Floor breaches cannot be hidden inside scalar aggregation.

## 7. Severe Individual Loss

Define severe loss per dimension:

```math
Severe_{e,d}(a) = 1 \iff \delta_{e,d}(a) ≥ \theta_{e,d}^{loss}
```

Define severe individual loss:

```math
Severe_e(a) = 1 \iff \exists d∈D_e^{protected}: Severe_{e,d}(a)=1
```

or:

```math
\exists d∈D_e^{protected}: E[v_{e,d}(t+\Delta t)|a] < \theta_{e,d}^{floor}
```

This replaces unsafe scalar-only conditions such as:

```math
max_e \Delta H_e(a) ≥ \theta_{severe}
```

unless `ΔH_e` has already been explicitly projected.

## 8. Non-Aggregation Guard with Profiles

Define admissible action set:

```math
A_{admissible} = \{a∈A : Guard(a)=pass\}
```

The guard fails if:

```math
\exists e: Severe_e(a)=1
```

unless:

```math
Necessity(a)=true ∧ No_Less_Irreversible_Alternative(a)=true
```

The guard also fails if:

```math
HB(a) > \theta_{HB}
```

or:

```math
U_{displayed}(a) < U_{required}(a)
```

or:

```math
RespRoute(a) missing
```

Only after guard pass may scalar aggregation be used for ranking.

## 9. Hidden Bill with Profiles

Visibility may differ by entity and dimension.

Define:

```math
Visi_{e,d} ∈ [0,1]
```

Profile hidden bill:

```math
HB_d(a) = \sum_e \delta_{e,d}(a) · (1 - Visi_{e,d})
```

Hidden bill profile:

```math
HB_V(a) = (HB_d(a))_{d∈D}
```

Scalar hidden bill is allowed only through a declared projection:

```math
HB^σ(a) = σ_{HB}(HB_V(a))
```

## 10. Uncertainty Over Value Profiles

If uncertainty is high, value profiles should be represented as intervals or distributions:

```math
v_{e,d}(t) ∈ [l_{e,d}, u_{e,d}]
```

or:

```math
P(v_e | data)
```

Under uncertainty, dominance should be conservative.

Robust dominance:

```math
v_1 \succeq_R v_2 \iff \forall d: l_{1,d} ≥ u_{2,d}
```

If robust dominance fails, record uncertainty rather than forcing false precision.

## 11. Closure Mode Interaction

Closure mode does not automatically become a scalar multiplier.

Instead it affects:

```text
repair route
responsibility route
floor sensitivity
violation status
required uncertainty visibility
```

For example:

```math
CM=deception -> truth_access and agency dimensions receive protected-floor attention
```

```math
CM=coercion -> agency and reachable-exit dimensions receive protected-floor attention
```

```math
CM=predation -> bodily_integrity, agency, continuity, and protection dimensions receive protected-floor attention
```

## 12. Mechanical Ethics Translation

TRACE:

```math
δ_e(a) is profile-valued
```

Mechanical Ethics:

Do not collapse plural human losses into one number without declaring the projection.

TRACE:

```math
\exists d: floor breach
```

Mechanical Ethics:

Some dimensions cannot be traded away by aggregate benefit.

TRACE:

```math
v_1 \parallel v_2
```

Mechanical Ethics:

Some choices are real value collisions, not optimisation errors.

TRACE:

```math
scalar score used without σ declaration
```

Mechanical Ethics:

The system is hiding a value judgement inside arithmetic.

## 13. Minimal Worked Shape

If action `a` reduces an entity's profile:

```math
v_e(t) = (survival=.95, agency=.80, relation=.70, truth=.90)
```

and expected post-action profile is:

```math
E[v_e(t+\Delta t)|a] = (survival=.95, agency=.20, relation=.65, truth=.10)
```

then profile loss is:

```math
δ_e(a) = (0, .60, .05, .80)
```

If `agency` floor is `.40` and `truth` floor is `.50`, then action `a` breaches protected floors even though survival is preserved.

This is a TRACE-visible failure.

## 14. Guardrail

Do not use scalar convenience as source authority.

Profile first.

Partial order second.

Floors third.

Scalar projection only when declared.
