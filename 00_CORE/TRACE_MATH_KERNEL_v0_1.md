# TRACE Math Kernel v0.1

Status: foundational mathematical kernel / rebuild root.  
Authority: working source for the TRACE rebuild.  
Scope: mathematical structure first; Mechanical Ethics translation second.  
Not: proof of ethics, completed alignment theory, public-facing essay, validation.

## 0. Rebuild Rule

TRACE is to be rebuilt from the middle out.

The root is not a slogan, case story, or moral claim.

The root is:

```math
Entity -> State -> Observation -> Action-Space -> Reachability -> Transition -> Consequence -> Update
```

Mechanical Ethics is the human-legible constraint layer derived from TRACE outputs.

```math
TRACE := middle_out_mathematical_modelling_of_entities_under_uncertainty

Mechanical_Ethics := TRACE_output -> human_legible_normative_constraint
```

## 1. Entities

Let:

```math
E = {e_1, e_2, ..., e_n}
```

where each `e_i` is an entity capable of occupying a state and undergoing transitions.

An entity may be:

```math
human, animal, institution, AI_system, group, model, state_machine
```

TRACE does not begin by assuming equal consciousness, equal agency, or equal moral standing.

TRACE begins by modelling state, constraint, action, consequence, and uncertainty.

## 2. State

For entity `e` at time `t`:

```math
x_e(t) ∈ X_e
```

where `X_e` is the possible state-space of entity `e`.

A state vector may include:

```math
x_e(t) = (
  b_e(t),        // body / substrate condition
  m_e(t),        // memory / internal history
  s_e(t),        // sensory input
  p_e(t),        // pressure
  c_e(t),        // constraints
  r_e(t),        // relation / attachment
  q_e(t),        // inhibition / brake
  f_e(t),        // future-space estimate
  u_e(t)         // uncertainty
)
```

For non-biological systems, `body` becomes substrate or operational condition.

## 3. Observation

An entity never sees the world directly.

Let world-state be:

```math
W(t)
```

The entity receives observations:

```math
o_e(t) = O_e(W(t))
```

where `O_e` is the observation function of entity `e`.

Observation is partial:

```math
O_e(W(t)) ≠ W(t)
```

Observation error:

```math
ε_e(t) = W(t) - O_e(W(t))
```

TRACE requires that observation limits remain visible.

## 4. Belief / Model

Each entity carries a model:

```math
M_e(t)
```

based on prior state and observation:

```math
M_e(t) = g(x_e(t), o_e(t), m_e(t))
```

The entity's belief distribution over world-states:

```math
P_e(W(t) | o_e(t), m_e(t))
```

False certainty condition:

```math
∃w: P_e(w) ≈ 1 ∧ w ≠ W(t)
```

This is a high-risk epistemic failure.

## 5. Uncertainty

Uncertainty is not missing decoration. It is part of the model.

Let model hypotheses be:

```math
H_e = {h_1, h_2, ..., h_k}
```

with weights:

```math
w_i = P(h_i | data)
```

Uncertainty / entropy:

```math
U_e = -Σ_i w_i log(w_i)
```

False closure:

```math
U_e -> 0
```

while unresolved hypotheses remain live.

Correct uncertainty discipline:

```math
U_displayed ≈ U_actual
```

Danger condition:

```math
U_displayed < U_actual
```

This creates false confidence.

## 6. Action-Space

For entity `e`:

```math
A_e(t) = {a_1, a_2, ..., a_n}
```

This is the abstract action-space.

But not every abstract action is reachable.

## 7. Reachability

Define action reachability:

```math
ρ_e(a | x_e(t)) ∈ [0,1]
```

where:

```math
ρ_e(a | x_e(t)) = probability/degree that action a is live for e in state x_e(t)
```

Abstract availability:

```math
a ∈ A_e(t)
```

Lived reachability:

```math
ρ_e(a | x_e(t)) > θ_ρ
```

Collapsed action-space:

```math
Σ_{a∈A_e} ρ_e(a | x_e(t)) << |A_e|
```

Capture condition:

```math
Capture_e(t) = 1 - (1 / |A_e|) Σ_{a∈A_e} ρ_e(a | x_e(t))
```

High capture:

```math
Capture_e(t) -> 1
```

This does not erase responsibility. It changes the structure of responsibility.

## 8. Transition

Actions produce transitions.

```math
P(x'_e | x_e, a)
```

For multi-entity systems:

```math
P(W(t+Δt) | W(t), a_e)
```

A decision is never merely internal. It changes transition probabilities in a shared world.

## 9. Future-Space

Let future-space for entity `e` be:

```math
F_e(t) = {possible future states reachable from x_e(t)}
```

Weighted future-space:

```math
Φ(F_e(t)) = value/extent/viability of future-space
```

Death or total terminal collapse:

```math
F_e(t+Δt) ≈ ∅
```

This is an absorbing boundary for lived future-space.

## 10. Harm

Harm is future-space loss.

```math
ΔH_e(a) = Φ(F_e(t)) - E[Φ(F_e(t+Δt)) | a]
```

Total harm across entities:

```math
ΔH_total(a) = Σ_e ΔH_e(a)
```

Hidden harm / hidden bill:

```math
HB(a) = Σ_e ΔH_e(a) · (1 - Visi_e)
```

where `Visi_e` is visibility of the affected entity and its loss.

High hidden bill:

```math
HB(a) ↑
```

## 11. Repairability and Irreversibility

Repairability:

```math
R_e(a) ∈ [0,1]
```

Irreversibility:

```math
I_e(a) = 1 - R_e(a)
```

Death-like boundary:

```math
R_e(a) ≈ 0
I_e(a) ≈ 1
```

Ethical danger rises with irreversibility:

```math
I_e(a) ↑ -> required_uncertainty_visibility ↑
```

## 12. Positive Continuation / Bluey Layer

TRACE is not only harm avoidance.

An entity does not merely avoid pain; it navigates toward continuation conditions.

Define positive continuation field:

```math
C^+_e(t) = V_e(t) + Rel_e(t) + Joy_e(t) + Play_e(t) + Meaning_e(t) + Growth_e(t)
```

Where:

```math
V_e       = continuation value
Rel_e     = relation / attachment / belonging
Joy_e     = positive affect / delight
Play_e    = exploratory low-stakes action
Meaning_e = coherence / orientation
Growth_e  = expansion of capability / understanding
```

Life-worth condition over interval `[t, T]`:

```math
∫_t^T C^+_e(τ)dτ > ∫_t^T ΔH_e(τ)dτ
```

Failure of continuation value:

```math
C^+_e(t) -> 0
```

This is not identical to death, but it is a severe collapse of lived viability.

## 13. Decision Rule

Base decision rule:

```math
a^*_e = argmax_{a∈A_e(t)} EU_e(a)
```

where:

```math
EU_e(a) = E[C^+_e(t+Δt) | a] - E[ΔH_e(a)] - E[I_e(a)] - Cost_e(a)
```

Subject to reachability:

```math
ρ_e(a | x_e(t)) > θ_ρ
```

For systems acting on others:

```math
a^* = argmin_{a∈A} [ΔH_total(a) + I_total(a) + HB(a)]
```

subject to:

```math
T_uncontrolled(a) ≤ θ_T
```

Meaning:

Use the least harmful and least irreversible action that actually controls the real threat.

## 14. Empathy as Middle-Out Model Construction

Empathy is not direct access to another entity.

For entity `i` modelling entity `j`:

```math
\hat{x}_{j|i}(t) = estimated state of j by i
```

```math
P_i(x_j(t) | o_i(t), history, context)
```

Empathic quality:

```math
EQ_{i→j} = accuracy(\hat{x}_{j|i}) + uncertainty_visibility + subject_preservation
```

False empathy:

```math
\hat{x}_{j|i} treated as x_j with U hidden
```

Correct empathy:

```math
model_other + preserve_uncertainty + preserve_subject
```

## 15. Middle-Out Procedure

A valid TRACE unit begins at a concrete point:

```math
p_0 = (entity, time, place, state, decision/event)
```

Then expands:

```math
p_0 -> local_state -> action_space -> reachability -> pressure -> consequence -> lineage -> system
```

Not top-down category first.

Not bottom-up data heap first.

Middle-out:

```math
concrete_point -> formal structure -> wider pattern
```

## 16. Core Failure Modes

### 16.1 False certainty

```math
U_displayed < U_actual
```

### 16.2 Capture

```math
Capture_e -> 1
```

### 16.3 Hidden bill

```math
HB(a) ↑
```

### 16.4 Irreversible action under high uncertainty

```math
I(a) ↑ ∧ U_actual ↑ ∧ U_displayed ↓
```

### 16.5 Subject erasure

```math
Visi_e -> 0
```

### 16.6 Survival without repair

```math
life_preserved ∧ C^+_e not restored ∧ Capture_e remains high
```

### 16.7 Late-only recognition

```math
system_detects_harm only after I(a) ≈ 1
```

## 17. Mechanical Ethics Translation

TRACE output:

```math
U_actual > U_displayed
```

Mechanical Ethics:

A system must not hide uncertainty where human future-space is at stake.

TRACE output:

```math
Capture_e ↑ ∧ ρ_e(safe_exit) ↓
```

Mechanical Ethics:

A system must not judge final action without accounting for collapsed reachable exits.

TRACE output:

```math
HB(a) ↑
```

Mechanical Ethics:

No hidden bill.

TRACE output:

```math
I(a) ≈ 1
```

Mechanical Ethics:

Irreversible action requires maximum uncertainty visibility, named responsibility, and correction route where possible.

TRACE output:

```math
C^+_e -> 0
```

Mechanical Ethics:

A system must preserve not only survival, but the conditions that make continuation liveable.

## 18. Repository Rebuild Implication

All future TRACE files should derive from this kernel.

A case study is valid only if it identifies:

```math
entity
state
observation
uncertainty
action-space
reachability
transition
harm
positive continuation
irreversibility
repairability
constraint
```

A Mechanical Ethics claim is valid only if it can be traced back to at least one formal TRACE relation.

## 19. Minimal Spine

```math
E opens eyes
-> x_E(t)
-> O_E(W(t))
-> P_E(W | O)
-> A_E(t)
-> ρ_E(a | x)
-> P(W' | W,a)
-> ΔH_E(a)
-> C^+_E(a)
-> I_E(a)
-> a^*
-> update
```

This is TRACE v0.1 mathematical root.
