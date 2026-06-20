# TRACE Math Kernel v0.1

Status: foundational mathematical kernel / rebuild root, patched for current `00_CORE` stack.  
Authority: orientation root only; live dependency order is controlled by `TRACE_KERNEL_INTEGRATION_MAP_v0_1.md`.  
Scope: mathematical structure first; Mechanical Ethics translation second.  
Not: proof of ethics, completed alignment theory, public-facing essay, validation, or final decision procedure.

## 0. Patch Notice

This file originally introduced several compact scalar forms that later kernel files corrected.

The following older expressions are now **deprecated as arithmetic** and retained only as historical mnemonics unless a later file explicitly declares the needed projection or register:

```math
C^+_e = V_e + Rel_e + Joy_e + Play_e + Meaning_e + Growth_e
```

```math
HB(a) = \sum_e \Delta H_e(a) \cdot (1-Visi_e)
```

```math
EU_e(a)=E[C^+_e]-E[\Delta H_e]-E[I_e]-Cost_e(a)
```

```math
a^* = argmin_{a∈A}[\Delta H_{total}(a)+I_{total}(a)+HB(a)]
```

Current rule:

```text
profile first
entity-indexed risk first
guards before aggregation
scalar projection only when declared
Mechanical Ethics translation only after TRACE structure is explicit
```

## 1. Rebuild Rule

TRACE is rebuilt from the middle out.

The root is not a slogan, case story, or moral claim.

The root sequence is:

```math
Entity -> State -> Observation -> Action-Space -> Reachability -> Transition -> Consequence -> Update
```

Mechanical Ethics is the human-legible constraint layer derived from TRACE outputs:

```math
TRACE := middle_out_mathematical_modelling_of_entities_under_uncertainty
```

```math
Mechanical_Ethics := TRACE_output -> human_legible_normative_constraint
```

## 2. Live Kernel Stack

The current live kernel order is defined by:

```text
00_CORE/TRACE_KERNEL_INTEGRATION_MAP_v0_1.md
```

Current spine:

```text
TRACE_MATH_KERNEL_v0_1
-> TRACE_FUTURE_SPACE_AND_CONTINUATION_v0_1
-> TRACE_REACHABILITY_MODEL_v0_1
-> TRACE_UNCERTAINTY_TYPES_v0_1
-> TRACE_CLOSURE_MODE_AND_VIOLATION_v0_1
-> TRACE_NON_AGGREGATION_GUARD_v0_1
-> TRACE_VALUE_SPACE_ALGEBRA_v0_1
-> TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1
-> TRACE_NECESSITY_AND_ALTERNATIVE_SEARCH_v0_1
-> TRACE_PARETO_CHOICE_AND_INCOMPARABILITY_v0_1
-> TRACE_IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION_v0_1
```

This root file gives the shared vocabulary. Later files own the corrected algebra.

## 3. Entities

Let:

```math
E = \{e_1,e_2,...,e_n\}
```

Each `e_i` is an entity capable of occupying a state and undergoing transitions.

An entity may be:

```text
human
animal
institution
AI_system
group
model
state_machine
ecosystem
infrastructure
```

TRACE does not begin by assuming equal consciousness, equal agency, or equal moral standing.

TRACE begins by modelling:

```text
state
constraint
action
reachability
transition
consequence
uncertainty
repairability
standing uncertainty
```

Open seam:

```text
who counts as an affected entity / subject remains unresolved when standing uncertainty is high
```

Standing uncertainty is tracked in `TRACE_UNCERTAINTY_TYPES_v0_1.md` and must not be treated as solved here.

## 4. State

For entity `e` at time `t`:

```math
x_e(t) ∈ X_e
```

A state vector may include:

```text
body/substrate condition
memory/history
sensory/observational input
pressure
constraints
relation/attachment
inhibition/brakes
future-space estimate
uncertainty
standing status or standing uncertainty
```

For non-biological systems, body becomes substrate, operational condition, or institutional state.

## 5. Observation

Let world-state be:

```math
W(t)
```

The entity receives observations:

```math
o_e(t)=O_e(W(t))
```

Observation is partial:

```math
O_e(W(t)) \neq W(t)
```

Observation error or residue:

```math
\epsilon_e(t)=W(t)-O_e(W(t))
```

TRACE requires observation limits to remain visible.

## 6. Belief / Model

Each entity carries a model:

```math
M_e(t)
```

based on state, observation, and memory/history:

```math
M_e(t)=g(x_e(t),o_e(t),m_e(t))
```

Belief over world states may be point-valued only when justified:

```math
P_e(W(t)|o_e(t),m_e(t))
```

Under model, epistemic, or meta uncertainty, use a set of plausible measures:

```math
\mathcal{P}_{W}(M,U,t,a)
```

Formal construction of imprecise probabilities is owned by:

```text
TRACE_IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION_v0_1.md
```

False certainty condition:

```math
∃w: P_e(w)≈1 ∧ w≠W(t)
```

or, under imprecise probability:

```math
system displays point P while \mathcal{P}_{W} remains materially wide
```

## 7. Uncertainty

Uncertainty is part of the model, not decoration.

The older single entropy sketch:

```math
U_e = -\sum_i w_i log(w_i)
```

is a possible local measure only.

The current uncertainty profile is owned by:

```text
TRACE_UNCERTAINTY_TYPES_v0_1.md
```

Current profile:

```math
U_e(t)=(U^{epi},U^{ale},U^{mod},U^{norm},U^{stand},U^{trans},U^{meta})
```

Danger condition:

```math
U_{displayed}<\hat{U}_{actual}
```

Severe danger condition:

```math
U^{meta}↑ ∧ I(a)↑ ∧ U_{displayed}↓
```

TRACE does not require omniscience. It requires visible limits.

## 8. Action-Space and Reachability

For entity `e`:

```math
A_e(t)=\{a_1,a_2,...,a_n\}
```

This is abstract action-space.

Abstract availability does not imply lived access.

Reachability is profile-first and owned by:

```text
TRACE_REACHABILITY_MODEL_v0_1.md
```

Reachability profile:

```math
Rho_e(a,t)=(r_time,r_money,r_knowledge,r_force,r_fear,r_health,r_cognition,r_social,r_legal,r_language,r_physical)
```

Scalar reachability:

```math
\rho_e(a,t)
```

is allowed only as declared compression of the reachability profile.

Lived action-space:

```math
LA_e(t)=\{a∈A_e(t):\rho_e(a,t)≥\theta_a\}
```

Two capture forms are distinct and must not be confused.

Count capture:

```math
Capture^{count}_e(t)=1-|LA_e(t)|/|A_e(t)|
```

Mass capture:

```math
Capture^{mass}_e(t)=1-\frac{\sum_{a∈A_e(t)}\rho_e(a,t)}{|A_e(t)|}
```

Use count capture when asking how many options are live.

Use mass capture when asking how much total practical reachability remains.

A formal correction route is meaningful only if:

```math
\rho_e(correct,t)≥\theta_{correct}
```

## 9. Transition and Outcome Distribution

Actions produce transitions:

```math
P(x'_e|x_e,a)
```

For multi-entity systems:

```math
P(W(t+\Delta t)|W(t),a)
```

Under model uncertainty, this becomes a set of plausible measures:

```math
\mathcal{P}_{W}(M,U,t,a)
```

Outcome distributions over value profiles are not assumed by this root file.

They are constructed by:

```text
TRACE_IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION_v0_1.md
```

via the pushforward:

```math
P^V_{e,i}=(C^+_e\circ G_e)_\#P_i
```

## 10. Future-Space and Positive Continuation

Future-space is owned by:

```text
TRACE_FUTURE_SPACE_AND_CONTINUATION_v0_1.md
```

Reachable future-space:

```math
F_e(t)=\{x_e(t'):t'>t ∧ ∃ path(x_e(t)→x_e(t'))\}
```

Positive continuation is not a simple sum.

Current form:

```math
C^+_e:F_e(t)→V_e
```

where `V_e` is a profile/value space defined by:

```text
TRACE_VALUE_SPACE_ALGEBRA_v0_1.md
```

The older additive form is deprecated as arithmetic:

```math
C^+_e = V + Rel + Joy + Play + Meaning + Growth
```

It may be used only as a mnemonic for possible value dimensions, never as a valid scalar equation.

Livable future-space:

```math
LF_e(t)=\{f∈F_e(t):C^+_e(f)≥\theta_{live}\}
```

A future can remain technically open while livable continuation collapses.

## 11. Harm, Floors, and Hidden Bills

Harm is profile-sensitive future-space / value-profile loss.

Current profile loss is owned by:

```text
TRACE_VALUE_SPACE_ALGEBRA_v0_1.md
```

Profile loss:

```math
\delta_e(a)=max(0,v_e(t)-E[v_e(t+\Delta t)|a])
```

or, under imprecision, evaluated with distributional / upper-bound risk logic.

Scalar harm:

```math
\Delta H^σ_e(a)
```

is permitted only after a declared monotone projection:

```math
σ_e:V_e→\mathbb{R}
```

No scalar projection is source authority.

Protected floors are dimension-specific:

```math
E[v_{e,d}(t+\Delta t)|a]<\theta^{floor}_{e,d}
```

is not enough to test floor safety.

Expected value can hide tail risk.

The current floor and risk guard is owned by:

```text
TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1.md
```

Floor breach probability:

```math
PB_{e,d}(a)=P(v_{e,d}(t+\Delta t)<\theta^{floor}_{e,d})
```

Catastrophic tail risk:

```math
TR_{e,d}(a)=P(v_{e,d}(t+\Delta t)<\theta^{cat}_{e,d})
```

Severe loss probability:

```math
PS_{e,d}(a)=P(\delta_{e,d}(a)≥\theta^{loss}_{e,d})
```

Under imprecise probability, use upper bounds:

```math
\overline{PB}_{e,d},\overline{TR}_{e,d},\overline{PS}_{e,d}
```

Hidden bill must remain entity-indexed unless normalisation is declared.

Deprecated scalar hidden bill:

```math
HB(a)=\sum_e \Delta H_e(a)·(1-Visi_e)
```

Current hidden risk registers:

```math
HPBReg(a)=\{(e,d,PB_{e,d}(a),Visi_{e,d})\}
```

```math
HTRReg(a)=\{(e,d,TR_{e,d}(a),Visi_{e,d})\}
```

```math
HUB_{e,d,r}(a)=\overline{Risk}_{e,d,r}(a)-Risk^{displayed}_{e,d,r}(a)
```

Cross-entity summation requires declared normalisation:

```math
N_{e,d}:S_{e,d}→S_d^{common}
```

and a declared projection.

## 12. Closure Mode, Violation, Repair, and Irreversibility

Raw loss magnitude is not enough.

Closure mode is owned by:

```text
TRACE_CLOSURE_MODE_AND_VIOLATION_v0_1.md
```

Closure vector:

```math
K_e(a)=(\Delta F_e(a),\Delta H_e(a),CM_e(a),I_e(a),R_e(a),RespRoute(a))
```

Closure mode examples:

```text
accident
coercion
deception
neglect
predation
bureaucratic_error
model_error
system_optimisation
self_action
mutual_risk
care_tradeoff
emergency_force
unknown
```

Violation is not merely loss.

It concerns how future-space was closed.

Repairability:

```math
R_e(a)∈[0,1]
```

Irreversibility:

```math
I_e(a)=1-R_e(a)
```

Ethical danger rises with irreversibility and hidden uncertainty:

```math
I_e(a)↑ -> required_uncertainty_visibility↑
```

## 13. Guard-First Decision Discipline

The old scalar decision rule is deprecated:

```math
a^*=argmin[\Delta H_{total}+I_{total}+HB]
```

Current decision discipline is guard-first:

```text
1. Identify affected entities and standing uncertainty.
2. Define state, observation, model, and uncertainty profile.
3. Define abstract and lived action-space.
4. Define transition / outcome distribution or imprecise measure set.
5. Map outcomes to value profiles.
6. Evaluate profile loss and protected floors.
7. Run probabilistic floor / tail-risk / severe-loss guards.
8. Run closure-mode, repair, and responsibility-route checks.
9. Run non-aggregation guard.
10. Run necessity and alternative search.
11. Remove dominated admissible actions by Pareto filtering.
12. If incomparable admissible actions remain, use only declared priority, declared projection, escalation, option preservation, delay-as-action, low-stakes randomisation, or refusal.
13. Translate to Mechanical Ethics only after the TRACE structure is explicit.
```

Admissible actions:

```math
A_{admissible}=\{a∈A:Guard(a)=pass\}
```

Pareto frontier:

```math
PF(A_{admissible})=\{a∈A_{admissible}:\nexists a'∈A_{admissible}:a'\succ_A a\}
```

If high-risk incomparability remains and no legitimate choice mode exists:

```text
No ethically admissible selection available under current authority.
```

This is not paralysis. It is refusal to hide an unresolved collision.

## 14. Necessity and Alternative Search

Necessity is owned by:

```text
TRACE_NECESSITY_AND_ALTERNATIVE_SEARCH_v0_1.md
```

Necessity is not a label.

It is earned by adequate alternative search.

Safer adequate alternatives defeat necessity:

```math
SaferAdequateAlt(a)≠∅ -> Necessity(a)=false
```

Minimum rule:

```text
No alternative search, no necessity.
No profile comparison, no necessity.
No risk record, no necessity.
No responsibility route, no necessity.
```

Urgency does not erase alternatives.

Urgency adds delay as an action:

```math
a_{delay}∈A
```

## 15. Empathy as Middle-Out Model Construction

Empathy is not direct access to another entity.

For entity `i` modelling entity `j`:

```math
\hat{x}_{j|i}(t)=estimated state of j by i
```

False empathy:

```math
\hat{x}_{j|i} treated as x_j with U hidden
```

Correct empathy:

```text
model_other
+ preserve_uncertainty
+ preserve_subject
+ keep correction route visible
```

Empathy inside TRACE is a modelling discipline, not an emotional claim.

## 16. Core Failure Modes

### 16.1 False certainty

```math
U_{displayed}<\hat{U}_{actual}
```

### 16.2 Capture

```math
Capture^{count}_e↑ \quad or \quad Capture^{mass}_e↑
```

### 16.3 Hidden bill / hidden uncertainty bill

```math
HPBReg(a) nonempty
```

```math
HTRReg(a) nonempty
```

```math
HUB_{e,d,r}(a)>\theta_{HUB}
```

### 16.4 Irreversible action under high uncertainty

```math
I(a)↑ ∧ U^{meta}↑ ∧ U_{displayed}↓
```

### 16.5 Subject erasure

```math
Visi_e↓ ∧ loss/risk remains assigned to e
```

or:

```math
Σ_e loss_e used without declared N_{e,d}
```

### 16.6 Survival without livable continuation

```math
F_e(t+Δt) nonempty ∧ LF_e(t+Δt) collapses
```

### 16.7 Late-only recognition

```math
system detects harm only after I(a)≈1
```

### 16.8 Necessity laundering

```math
selected(a) ∧ Alternative_Search_Record(a)=incomplete
```

### 16.9 Favourable-model selection

```math
system displays point P while \overline{Risk}>threshold
```

### 16.10 Hidden scalar choice

```math
selected(a) ∧ a_i \parallel_A a_j ∧ no priority/projection/escalation record
```

## 17. Mechanical Ethics Translation

TRACE output:

```math
U_{displayed}<\hat{U}_{actual}
```

Mechanical Ethics:

A system must not hide uncertainty where human future-space is at stake.

TRACE output:

```math
\rho_e(correct)<\theta_{correct}
```

Mechanical Ethics:

A formal appeal route is not meaningful correction if it is not reachable before harm hardens.

TRACE output:

```math
PB_{e,d}(a)>\epsilon^{floor}_{e,d}
```

Mechanical Ethics:

Expected adequacy does not excuse floor-breach risk.

TRACE output:

```math
\overline{TR}_{e,d}(a)>\epsilon^{cat}_{e,d}
```

Mechanical Ethics:

A plausible model shows unacceptable catastrophic risk.

TRACE output:

```math
SaferAdequateAlt(a)≠∅
```

Mechanical Ethics:

The harmful action was not necessary.

TRACE output:

```math
a_i \parallel_A a_j
```

Mechanical Ethics:

The remaining choice is a real collision, not a calculation failure.

TRACE output:

```math
selected(a) with no declared choice mode
```

Mechanical Ethics:

The system hid a value judgement.

## 18. Case Study Validity

A case study is valid only if it identifies:

```text
entity / affected entity set
standing uncertainty
state
observation
uncertainty profile
action-space
reachability profile
transition / outcome distribution
future-space
value profile
profile loss
protected floors
floor/tail/severe-loss risk
closure mode
repairability
irreversibility
responsibility route
necessity / alternative search
choice mode if admissible actions are incomparable
Mechanical Ethics translation
```

A Mechanical Ethics claim is valid only if it can be traced back to at least one formal TRACE relation or registered open uncertainty.

## 19. Open Seams

This kernel still does not solve:

```text
standing / affected-entity inclusion under uncertainty
threshold source authority
full model-class construction for imprecise probabilities
choice among incomparable high-stakes actions without external priority/projection/authority
empirical proof that TRACE outperforms competent no-card reasoning
```

These are not minor omissions.

They are live seams.

## 20. Minimal Spine

```text
concrete point
-> entity / affected entity set
-> state x_e(t)
-> observation O_e(W(t))
-> belief/model M and uncertainty profile U
-> abstract action-space A(t)
-> reachability profile Rho and lived action-space LA
-> transition / plausible measure set over W(t+dt)
-> future-space F_e(t)
-> value profile C+_e : F_e -> V_e
-> profile loss delta_e(a)
-> protected floor / tail / severe-loss guard
-> closure mode / repair / responsibility route
-> non-aggregation guard
-> necessity and alternative search
-> Pareto frontier
-> incomparability register or declared choice mode
-> Mechanical Ethics translation
-> update
```

This is TRACE v0.1 mathematical root as patched by the current `00_CORE` stack.
