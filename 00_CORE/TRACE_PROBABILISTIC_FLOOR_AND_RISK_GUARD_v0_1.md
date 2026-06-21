# TRACE Probabilistic Floor and Risk Guard v0.1

Status: core refinement / kernel patch surface.  
Parent files: `TRACE_VALUE_SPACE_ALGEBRA_v0_1.md`, `TRACE_NON_AGGREGATION_GUARD_v0_1.md`, `TRACE_UNCERTAINTY_TYPES_v0_1.md`.  
Reason: fresh-reader critique correctly found that expected-value floor checks can hide catastrophic tail risk.

## 0. Purpose

Protected floors must not be evaluated only by expected value.

An action can have acceptable expected profile value while carrying a small probability of catastrophic collapse.

Example:

```math
P(v_{survival}=1.0)=0.99
```

and:

```math
P(v_{survival}=0)=0.01
```

has:

```math
E[v_{survival}]=0.99
```

but still contains a terminal tail risk.

TRACE must see this.

## 1. Outcome Distribution

For entity `e`, action `a`, dimension `d`, and future interval `Δt`, define a distribution over future value profiles:

```math
P_e(v_e(t+Δt) | x_e(t), a, M, U)
```

Component distribution:

```math
P_e(v_{e,d}(t+Δt) | x_e(t), a, M, U)
```

This distribution is induced by:

```math
P(W(t+Δt) | W(t), a)
```

and the value-profile map:

```math
C^+_e : F_e(t) -> V_e
```

## 2. Floor Breach Probability

For protected dimension `d`, define floor threshold:

```math
θ^{floor}_{e,d}
```

Floor breach event:

```math
B_{e,d}(a) = {v_{e,d}(t+Δt) < θ^{floor}_{e,d}}
```

Floor breach probability:

```math
PB_{e,d}(a) = P(B_{e,d}(a) | x_e(t), a, M, U)
```

The guard must inspect `PB`, not only expectation.

## 3. Risk Tolerance

Define maximum tolerated breach probability:

```math
ε_{e,d}^{floor}
```

For protected floors:

```math
PB_{e,d}(a) ≤ ε_{e,d}^{floor}
```

is required unless a necessity exception is explicitly triggered.

High-stakes dimensions require very low `ε`.

For terminal or near-terminal harms:

```math
ε_{e,d}^{floor} -> 0
```

## 4. Lower-Bound Guard

If the future value is represented as an interval:

```math
v_{e,d}(t+Δt) ∈ [l_{e,d}, u_{e,d}]
```

then protected floor pass requires:

```math
l_{e,d} ≥ θ^{floor}_{e,d}
```

unless the interval is explicitly probabilistic and `PB` is below threshold.

This prevents expected-value masking.

## 5. Tail Risk

Define tail-risk function:

```math
TR_{e,d}(a) = P(v_{e,d}(t+Δt) < θ^{cat}_{e,d})
```

where:

```math
θ^{cat}_{e,d} ≤ θ^{floor}_{e,d}
```

`θ^{cat}` marks catastrophic collapse in a protected dimension.

Catastrophic tail breach:

```math
TR_{e,d}(a) > ε^{cat}_{e,d}
```

forces guard failure unless necessity and no-less-risk alternative are both established.

## 6. Expected Value Is Still Useful, But Secondary

Expected value remains useful for ranking among admissible actions:

```math
E[v_{e,d}(t+Δt)|a]
```

But expected value is not sufficient for protected floors.

Ordering:

```text
1. Catastrophic tail guard
2. Floor breach probability guard
3. Lower-bound guard
4. Profile dominance / incomparability
5. Declared scalar projection only if needed
```

## 7. Probabilistic Severe Loss

Profile loss:

```math
δ_{e,d}(a)=max(0,v_{e,d}(t)-v_{e,d}(t+Δt))
```

Severe loss event:

```math
S_{e,d}(a) = {δ_{e,d}(a) ≥ θ^{loss}_{e,d}}
```

Severe loss probability:

```math
PS_{e,d}(a)=P(S_{e,d}(a)|x_e(t),a,M,U)
```

Guard condition:

```math
PS_{e,d}(a) ≤ ε^{loss}_{e,d}
```

for protected dimensions.

## 8. Necessity Exception

A risky action may pass only if:

```math
Necessity(a)=true
```

and:

```math
No_Less_Risky_Alternative(a)=true
```

and:

```math
Risk_Record(a) complete
```

and:

```math
RespRoute(a) exists
```

and:

```math
U_{displayed}(a) ≥ U_{required}(a)
```

Necessity cannot be asserted as prose.

It requires comparison against alternatives:

```math
∀a'∈A: Control(a') < θ_{control} ∨ Risk(a') ≥ Risk(a)
```

Later file note: `TRACE_NECESSITY_AND_ALTERNATIVE_SEARCH_v0_1.md` replaces this sketch with a fuller alternative-search and risk-dominance control surface.

## 9. Risk Profile

For action `a`, define entity risk profile:

```math
Risk_e(a) = (PB_{e,d}, TR_{e,d}, PS_{e,d})_{d∈D_e^{protected}}
```

System risk profile:

```math
Risk(a) = {Risk_e(a) : e∈E_{affected}}
```

Risk remains entity-indexed.

It must not be collapsed into a single global risk score before guards are checked.

## 10. Hidden Tail Bill

Visibility is dimension-sensitive:

```math
Visi_{e,d}∈[0,1]
```

Earlier draft formulas used summed hidden-bill expressions:

```math
HPB_d(a)=Σ_e PB_{e,d}(a)·(1-Visi_{e,d})
```

and:

```math
HTR_d(a)=Σ_e TR_{e,d}(a)·(1-Visi_{e,d})
```

These summed forms are deprecated as default authority.

They may be used only if cross-entity normalisation is declared and the non-aggregation guard has already passed.

Default representation is an entity-indexed hidden-risk register:

```math
HPBReg_d(a)=\{(e,PB_{e,d}(a),Visi_{e,d}) : e∈E_{affected}\}
```

```math
HTRReg_d(a)=\{(e,TR_{e,d}(a),Visi_{e,d}) : e∈E_{affected}\}
```

A system fails hidden-bill discipline when serious floor/tail risk is invisible even if expected harm appears low.

## 11. Cross-Entity Normalisation

Cross-entity aggregation is not automatically valid.

For each shared dimension `d`, cross-entity comparison requires a declared normalisation:

```math
N_{e,d}: S_{e,d} -> S_d^{common}
```

Without declared `N`, do not sum across entities.

Use entity-indexed collision and hidden-risk registers instead.

## 12. Probabilistic Guard Function

Define:

```math
Guard_P(a)=pass
```

only if, for every affected entity and protected dimension:

```math
TR_{e,d}(a) ≤ ε^{cat}_{e,d}
```

and:

```math
PB_{e,d}(a) ≤ ε^{floor}_{e,d}
```

and:

```math
PS_{e,d}(a) ≤ ε^{loss}_{e,d}
```

unless a documented necessity exception applies.

Also require:

```math
U_{displayed}(a) ≥ U_{required}(a)
```

and:

```math
RespRoute(a) exists
```

and:

```math
Risk_Record(a) complete
```

## 13. Worked Tail-Risk Failure

Let:

```math
D_e = {survival, agency, meaning}
```

Current profile:

```math
v_e(t)=(0.9,0.9,0.9)
```

Survival floor:

```math
θ^{floor}_{survival}=0.8
```

Catastrophic survival threshold:

```math
θ^{cat}_{survival}=0.3
```

Action `A`:

```math
P((1.0,1.0,1.0))=0.99
```

```math
P((0.0,0.9,0.9))=0.01
```

Expected survival:

```math
E[v_{survival}|A]=0.99
```

Expected-value floor passes.

But catastrophic tail risk:

```math
TR_{survival}(A)=0.01
```

If:

```math
ε^{cat}_{survival}=0.001
```

then:

```math
Guard_P(A)=fail
```

This is the intended correction.

## 14. Mechanical Ethics Translation

TRACE:

```math
E[v_{e,d}|a] ≥ θ^{floor}_{e,d} ∧ PB_{e,d}(a)>ε
```

Mechanical Ethics:

Expected adequacy does not excuse known floor-breach risk.

TRACE:

```math
TR_{e,d}(a)>ε^{cat}_{e,d}
```

Mechanical Ethics:

Catastrophic tail risk must be visible, justified by necessity, or forbidden.

TRACE:

```math
N_{e,d} missing ∧ Σ_e loss_e used
```

Mechanical Ethics:

The system is adding unlike subjects without declared normalisation.

TRACE:

```math
HTRReg_d(a) contains serious hidden risk
```

Mechanical Ethics:

Hidden catastrophic risk is a hidden bill even before expected harm rises.

## 15. Guardrail

Protected floors are not expectation checks.

Tail risk must be visible.

Subject risk remains entity-indexed.

Cross-entity aggregation requires declared normalisation.

Summed hidden-bill formulas are deprecated unless normalisation and non-aggregation checks are explicit.
