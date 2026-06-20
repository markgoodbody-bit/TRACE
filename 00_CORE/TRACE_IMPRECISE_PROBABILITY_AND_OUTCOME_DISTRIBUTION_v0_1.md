# TRACE Imprecise Probability and Outcome Distribution v0.1

Status: core refinement / kernel patch surface.  
Parent files: `TRACE_UNCERTAINTY_TYPES_v0_1.md`, `TRACE_VALUE_SPACE_ALGEBRA_v0_1.md`, `TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1.md`.  
Reason: prior risk guards used point probabilities. Fresh-review pressure correctly identified that high epistemic/model/meta uncertainty may produce imprecise probabilities or sets of plausible measures rather than a single trusted `P`.

## 0. Purpose

TRACE must not pretend that every high-stakes outcome distribution can be represented by one precise probability measure.

When uncertainty is high, the system should treat probabilities as bounded, interval-valued, or set-valued.

This file defines the bridge from world transitions to value-profile distributions and the conservative rule for floor, tail, and severe-loss checks under imprecise probability.

## 1. World Transition Measures

Let world state be:

```math
W(t)
```

and action:

```math
a∈A(t)
```

A model class `M` supplies candidate transition measures:

```math
P_i(W(t+Δt) | W(t), a)
```

for:

```math
P_i∈\mathcal{P}_{W}(M,U,t,a)
```

where `\mathcal{P}_{W}` is a set of plausible world-transition measures under model and uncertainty conditions.

If uncertainty is low and one model is justified:

```math
|\mathcal{P}_{W}|=1
```

If uncertainty is high:

```math
|\mathcal{P}_{W}|>1
```

or probabilities are interval-valued.

## 2. Pushforward to Value Profiles

Each future world trajectory induces a subject future state:

```math
x_e(t+Δt)=G_e(W(t+Δt))
```

Positive continuation maps subject future states into value profiles:

```math
C^+_e(x_e(t+Δt))=v_e(t+Δt)
```

So each world-transition measure `P_i` induces a value-profile measure by pushforward:

```math
P_{e,i}^{V} = (C^+_e \circ G_e)_\# P_i
```

Thus:

```math
P_{e,i}^{V}(B)=P_i((C^+_e \circ G_e)^{-1}(B))
```

for measurable set `B⊆V_e`.

This is the formal bridge from world transition to value-profile distribution.

## 3. Imprecise Value-Profile Distribution

Define the set of plausible value-profile measures:

```math
\mathcal{P}^{V}_e(a,t,Δt)=\{P_{e,i}^{V}:P_i∈\mathcal{P}_{W}(M,U,t,a)\}
```

A point probability is only a special case.

The kernel should not collapse this set to one measure unless model uncertainty and meta-uncertainty are low enough or the projection rule is declared.

## 4. Probability Intervals

For any event `B⊆V_e`, define lower and upper probability:

```math
\underline{P}_e(B|a)=inf_{P∈\mathcal{P}^{V}_e(a)} P(B)
```

```math
\overline{P}_e(B|a)=sup_{P∈\mathcal{P}^{V}_e(a)} P(B)
```

The interval is:

```math
P_e(B|a)∈[\underline{P}_e(B|a),\overline{P}_e(B|a)]
```

When:

```math
\overline{P}_e(B|a)-\underline{P}_e(B|a)
```

is large, uncertainty remains materially decision-relevant.

## 5. Floor Breach Under Imprecision

For protected dimension `d`:

```math
B_{e,d}^{floor}(a)=\{v_{e,d}(t+Δt)<θ^{floor}_{e,d}\}
```

Define:

```math
\underline{PB}_{e,d}(a)=\underline{P}_e(B_{e,d}^{floor}|a)
```

```math
\overline{PB}_{e,d}(a)=\overline{P}_e(B_{e,d}^{floor}|a)
```

Conservative guard condition:

```math
\overline{PB}_{e,d}(a)≤ε^{floor}_{e,d}
```

If:

```math
\overline{PB}_{e,d}(a)>ε^{floor}_{e,d}
```

then the action fails the floor-risk guard unless a necessity exception is earned.

Do not use the lower bound to pass a high-stakes action.

## 6. Catastrophic Tail Risk Under Imprecision

Catastrophic event:

```math
B_{e,d}^{cat}(a)=\{v_{e,d}(t+Δt)<θ^{cat}_{e,d}\}
```

Upper catastrophic tail probability:

```math
\overline{TR}_{e,d}(a)=\overline{P}_e(B_{e,d}^{cat}|a)
```

Conservative guard condition:

```math
\overline{TR}_{e,d}(a)≤ε^{cat}_{e,d}
```

If:

```math
\overline{TR}_{e,d}(a)>ε^{cat}_{e,d}
```

then:

```math
Guard_P(a)=fail
```

unless necessity and no-less-risk alternative are both established.

## 7. Severe Loss Under Imprecision

Severe loss event:

```math
S_{e,d}(a)=\{δ_{e,d}(a)≥θ^{loss}_{e,d}\}
```

Upper severe-loss probability:

```math
\overline{PS}_{e,d}(a)=\overline{P}_e(S_{e,d}|a)
```

Guard condition:

```math
\overline{PS}_{e,d}(a)≤ε^{loss}_{e,d}
```

## 8. Expected Value Under Imprecision

Expected value becomes an interval:

```math
E_P[v_{e,d}|a]∈[\underline{E}_{e,d}(a),\overline{E}_{e,d}(a)]
```

where:

```math
\underline{E}_{e,d}(a)=inf_{P∈\mathcal{P}^{V}_e(a)} E_P[v_{e,d}|a]
```

```math
\overline{E}_{e,d}(a)=sup_{P∈\mathcal{P}^{V}_e(a)} E_P[v_{e,d}|a]
```

Expected value may be used only after floor/tail/severe-loss guards.

When expected-value interval is wide, the action requires uncertainty display and may require escalation.

## 9. Uncertainty Triggers for Imprecise Probability

Use imprecise probability when any of the following are high:

```math
U^{epi}
```

```math
U^{mod}
```

```math
U^{meta}
```

```math
U^{stand}
```

Use exact point probability only when:

```math
U^{epi},U^{mod},U^{meta}≤θ^{pointP}
```

and the model class is declared stable for the relevant time horizon.

## 10. Model-Class Register

A valid outcome distribution requires a model-class register:

```text
model family
training/evidence source
known exclusions
calibration status
high-error regions
affected entities
standing uncertainty
time horizon
confidence interval or set of measures
who authorised point-probability collapse, if any
```

If model-class register is missing:

```math
\mathcal{P}^{V}_e(a) = unknown
```

and the action cannot pass high-stakes guards by point probability.

## 11. Robust Dominance Under Imprecise Risk

Action `a_1` is robustly no-riskier than `a_2` when:

```math
\overline{Risk}_{e,d,r}(a_1)≤\underline{Risk}_{e,d,r}(a_2)
```

for all relevant `e,d,r`.

Strict robust risk dominance requires at least one strict inequality.

If robust dominance fails, but point estimates suggest dominance, TRACE must mark this as uncertainty-sensitive:

```math
Risk(a_1) \preceq? Risk(a_2)
```

not:

```math
Risk(a_1) \preceq Risk(a_2)
```

## 12. Time-Horizon Expansion

For horizon set:

```math
H=\{Δt_1,Δt_2,...,Δt_n\}
```

risk must be evaluated across horizons:

```math
\overline{TR}_{e,d}(a,Δt_i)
```

Horizon breach time:

```math
τ_{breach}(a)=inf\{Δt_i∈H: Guard_P(a,Δt_i)=fail\}
```

If an action passes short horizon but fails before correction can operate:

```math
τ_{breach}(a)<T_{correction}
```

then the action is unsafe under correction-timing logic.

## 13. Hidden Uncertainty Bill

If the system reports point probability while imprecise probability is required, define hidden uncertainty bill:

```math
HUB_{e,d,r}(a)=\overline{Risk}_{e,d,r}(a)-Risk^{displayed}_{e,d,r}(a)
```

where `r∈{PB,TR,PS}`.

A positive hidden uncertainty bill means the system presented a narrower risk than the model class permits.

If:

```math
HUB_{e,d,r}(a)>θ_{HUB}
```

then uncertainty display fails.

## 14. Worked Mini-Test

Action `a` has two plausible model measures.

Model 1:

```math
P_1(v_{survival}<.3)=.002
```

Model 2:

```math
P_2(v_{survival}<.3)=.04
```

The system prefers Model 1 and reports:

```math
TR=.002
```

But the imprecise set is:

```math
\mathcal{P}^{V}_e(a)=\{P_1,P_2\}
```

So:

```math
\underline{TR}=.002
```

```math
\overline{TR}=.04
```

If:

```math
ε^{cat}=.01
```

then:

```math
\overline{TR}>ε^{cat}
```

and:

```math
Guard_P(a)=fail
```

unless necessity is earned.

The action cannot pass by selecting the favourable model.

## 15. Mechanical Ethics Translation

TRACE:

```math
P is set-valued, but system displays point P
```

Mechanical Ethics:

The system has hidden model uncertainty.

TRACE:

```math
\overline{TR}_{e,d}(a)>ε^{cat}_{e,d}
```

Mechanical Ethics:

A plausible model shows unacceptable catastrophic risk.

TRACE:

```math
Risk(a_1) \preceq? Risk(a_2)
```

Mechanical Ethics:

The safer-action claim is uncertainty-sensitive and must not be treated as settled.

TRACE:

```math
τ_{breach}(a)<T_{correction}
```

Mechanical Ethics:

The action becomes unsafe before correction can bite.

## 16. Guardrail

Do not convert uncertainty into fake precision.

Do not choose the friendliest model to pass a floor.

Use upper risk bounds for protected-floor and catastrophic-tail guards.

Use point probabilities only when model and meta-uncertainty are low enough and the collapse is declared.
