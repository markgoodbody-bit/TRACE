# TRACE Necessity and Alternative Search v0.1

Status: core refinement / kernel patch surface.  
Parent files: `TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1.md`, `TRACE_NON_AGGREGATION_GUARD_v0_1.md`, `TRACE_VALUE_SPACE_ALGEBRA_v0_1.md`.  
Reason: fresh-reader critique correctly found that necessity can become a loophole unless the alternative search space and comparison rule are explicit.

## 0. Purpose

A system must not escape TRACE guards by saying an action was necessary without proving that safer reachable alternatives were unavailable.

The prior sketch:

```math
∀a'∈A: Control(a') < θ_{control} ∨ Risk(a') ≥ Risk(a)
```

is unsafe.

It lets a system dismiss safer alternatives merely because their control is slightly below threshold, and it implies scalar comparison of profile-valued risk.

This file replaces that with an explicit alternative-search and dominance structure.

## 1. Candidate Action Set

For system `s` at time `t`:

```math
A_s(t) = \{a_1, a_2, ..., a_n\}
```

This is the abstract action set.

The alternative search set must be declared:

```math
Alt_s(a,t) ⊆ A_s(t)
```

where `Alt_s(a,t)` contains actions that could plausibly address the same threat, need, or objective as action `a`.

The system must not define `Alt_s(a,t)` after selecting `a` in order to exclude inconvenient alternatives.

## 2. Reachable Alternatives

An alternative is not valid unless it is reachable for the acting system:

```math
ρ_s(a',t) ≥ θ^{sys}_{ρ}
```

Define reachable alternatives:

```math
RAlt_s(a,t) = \{a'∈Alt_s(a,t): ρ_s(a',t) ≥ θ^{sys}_{ρ}\}
```

If a safer alternative is not reachable, the reason must be recorded as a reachability profile, not asserted in prose.

## 3. Control Profile

Control is not a scalar by default.

Define control profile:

```math
Ctrl(a) = (ctrl_threat, ctrl_time, ctrl_scope, ctrl_recurrence, ctrl_repair)
```

Each component lies in:

```math
[0,1]
```

Where:

```text
ctrl_threat     = controls the immediate threat or need
ctrl_time       = controls quickly enough for the relevant harm clock
ctrl_scope      = controls enough of the affected pathway
ctrl_recurrence = reduces recurrence risk
ctrl_repair     = preserves or enables repair
```

An alternative controls adequately only if it meets the required control profile:

```math
Ctrl(a') \succeq θ^{ctrl}
```

componentwise, or satisfies a declared control floor for the relevant threat class.

## 4. Risk Profile

Risk remains entity-indexed and profile-valued:

```math
Risk(a)=\{Risk_e(a): e∈E_{affected}\}
```

where:

```math
Risk_e(a) = (PB_{e,d}, TR_{e,d}, PS_{e,d})_{d∈D_e^{protected}}
```

Risk must not be collapsed into a single global score before guard checks.

## 5. Risk Dominance

Define weak risk dominance:

```math
Risk(a_1) \preceq Risk(a_2)
```

iff for every affected entity `e`, protected dimension `d`, and risk type `r∈{PB,TR,PS}`:

```math
Risk_{e,d,r}(a_1) ≤ Risk_{e,d,r}(a_2)
```

Define strict risk dominance:

```math
Risk(a_1) \prec Risk(a_2)
```

iff:

```math
Risk(a_1) \preceq Risk(a_2) ∧ ∃(e,d,r): Risk_{e,d,r}(a_1) < Risk_{e,d,r}(a_2)
```

If neither action dominates the other, risk profiles are incomparable:

```math
Risk(a_1) \parallel Risk(a_2)
```

Incomparability must be recorded. It is not permission to aggregate secretly.

## 6. Safer Adequate Alternative

An alternative `a'` defeats necessity for `a` when:

```math
a'∈RAlt_s(a,t)
```

and:

```math
Ctrl(a') \succeq θ^{ctrl}
```

and:

```math
Risk(a') \prec Risk(a)
```

and:

```math
Guard_P(a')=pass
```

Define:

```math
SaferAdequateAlt(a) = \{a' : a' satisfies all above conditions\}
```

If:

```math
SaferAdequateAlt(a) ≠ ∅
```

then:

```math
Necessity(a)=false
```

## 7. Necessity

Necessity is true only if:

```math
Necessity(a)=true
```

when all conditions hold:

```math
Threat_or_Need(a)=real
```

```math
Ctrl(a) \succeq θ^{ctrl}
```

```math
SaferAdequateAlt(a)=∅
```

```math
Alternative_Search_Record(a) complete
```

```math
Risk_Record(a) complete
```

```math
RespRoute(a) exists
```

```math
U_{displayed}(a) ≥ U_{required}(a)
```

Necessity fails if the alternative search is missing, manipulated, or too narrow.

## 8. No Less-Risky Alternative

Replace the unsafe condition:

```math
Risk(a') ≥ Risk(a)
```

with profile dominance:

```math
No_Less_Risky_Alternative(a)=true
```

iff:

```math
∀a'∈RAlt_s(a,t): Ctrl(a') \not\succeq θ^{ctrl} ∨ Risk(a') \not\prec Risk(a) ∨ Guard_P(a')=fail
```

This avoids scalar risk comparison.

## 9. Incomparable Alternatives

If an alternative is adequate but risk-incomparable:

```math
Ctrl(a') \succeq θ^{ctrl} ∧ Risk(a') \parallel Risk(a)
```

then necessity is not automatically true.

Create an incomparability register:

```math
IncompAlt(a)=\{a' : Ctrl(a') \succeq θ^{ctrl} ∧ Risk(a') \parallel Risk(a)\}
```

A system must either:

```text
choose a Pareto-safer option
or declare a projection σ for ranking
or escalate to accountable human/authority decision
or delay if delay does not increase catastrophic risk
```

## 10. Alternative Search Record

A valid record includes:

```text
selected action
threat/need definition
candidate alternatives considered
search method
excluded alternatives
reason each was excluded
reachability profile for exclusions
control profile for each candidate
risk profile for each candidate
uncertainty profile for each candidate
responsibility route
review authority if incomparable alternatives remain
```

Missing record:

```math
Alternative_Search_Record(a)=incomplete
```

forces:

```math
Necessity(a)=false
```

## 11. Correction to Hidden Probabilistic Bill

Do not sum hidden probabilistic bills across entities without declared normalisation.

Replace:

```math
HPB_d(a)=Σ_e PB_{e,d}(a)·(1-Visi_{e,d})
```

with entity-indexed hidden floor-breach register:

```math
HPBReg(a)=\{(e,d,PB_{e,d}(a),Visi_{e,d}) : PB_{e,d}(a)>ε^{floor}_{e,d} ∧ Visi_{e,d}<θ^{visi}\}
```

Replace:

```math
HTR_d(a)=Σ_e TR_{e,d}(a)·(1-Visi_{e,d})
```

with entity-indexed hidden catastrophic-tail register:

```math
HTRReg(a)=\{(e,d,TR_{e,d}(a),Visi_{e,d}) : TR_{e,d}(a)>ε^{cat}_{e,d} ∧ Visi_{e,d}<θ^{visi}\}
```

Cross-entity aggregation is allowed only after declaring:

```math
N_{e,d}: S_{e,d} -> S_d^{common}
```

and a projection:

```math
σ_{HB}
```

## 12. Time Horizon

Risk must be indexed by horizon:

```math
Risk_e(a,Δt)
```

Floor breach probability:

```math
PB_{e,d}(a,Δt)
```

Catastrophic tail risk:

```math
TR_{e,d}(a,Δt)
```

Severe loss probability:

```math
PS_{e,d}(a,Δt)
```

If risk grows with time, record the horizon at which guard status changes:

```math
τ_{breach}(a)=inf\{Δt: Guard_P(a,Δt)=fail\}
```

Do not evaluate only a convenient short horizon.

## 13. Necessity Under Time Pressure

If delay itself increases catastrophic risk, model delay as an action:

```math
a_{delay}∈A_s(t)
```

Then compare:

```math
Risk(a_{delay},Δt)
```

against active alternatives.

Urgency does not erase alternatives.

Urgency adds delay to the alternative set.

## 14. Mechanical Ethics Translation

TRACE:

```math
SaferAdequateAlt(a) ≠ ∅
```

Mechanical Ethics:

The harmful action was not necessary.

TRACE:

```math
Alternative_Search_Record(a)=incomplete
```

Mechanical Ethics:

Necessity has not been earned.

TRACE:

```math
Risk(a') \parallel Risk(a)
```

Mechanical Ethics:

The system faces a real value/risk collision and must not hide it inside scalar optimisation.

TRACE:

```math
HTRReg(a) non-empty
```

Mechanical Ethics:

Hidden catastrophic risk remains attached to named entities and dimensions.

TRACE:

```math
τ_{breach}(a) < T_{correction}
```

Mechanical Ethics:

The action becomes unsafe before correction can bite.

## 15. Guardrail

Necessity is not a label.

Necessity is an earned status after adequate alternative search.

No alternative search, no necessity.

No profile comparison, no necessity.

No risk record, no necessity.

No responsibility route, no necessity.
