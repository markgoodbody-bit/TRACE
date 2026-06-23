# TRACE Middle-Out Mathematical Core Packet v0.1

Status: master packet candidate. Not v0.12. Not validation. Not a complete ethics. This file consolidates the current mathematical spine of TRACE without adding a new kernel operator.

Purpose: define the runnable mathematical structure of TRACE from bounded encounter to responsible action.

```trace
TRACE :=
  typed partially observable transition system
  over protected future-space
  with claim/evidence typing,
  authority/capture constraints,
  clock/correction inequalities,
  and residue-preserving dirty-action governance
```

---

## 1. Whole packet object

```math
\Pi_{TRACE} := (E, S, I, C, A, T, F, R, L, \Omega)
```

Where:

```trace
E := bounded entities
S := world states
I := partial information functions
C := typed claims
A := actions / transitions
T := clocks
F := future-space functions
R := review / correction relations
L := loss / residue ledger
Ω := ordering and constraint rules
```

The packet is not a moral oracle. It is an operating structure for acting under uncertainty without hiding harm, authority, time, or residue.

---

## 2. Middle-out starting condition

A bounded entity exists inside a world it cannot fully perceive.

```math
e \in E,
\quad s_t \in S,
\quad I_e(s_t) \subset s_t
```

The entity must act from partial information:

```math
a_t : I_e(s_t) \rightarrow s_{t+1}
```

Under uncertainty, action maps to a possible-state set:

```math
\delta_e : I_e(S) \times A \rightarrow \mathcal{P}(S)
```

Core middle-out compression:

```trace
bounded_perception
+ irreversible_time
+ action_requirement
→ middle_out_start
```

Do not begin from perfect law or total mechanism. Begin from the encounter.

---

## 3. AI-to-claim translation

AI output begins in latent representation, not moral knowledge.

```math
z_t \in V_{latent}
```

Model output:

```math
P(token_{t+1} \mid z_t)
```

Translation chain:

```math
z \in V_{latent}
\rightarrow u \in Tokens
\rightarrow \phi \in Statements
\rightarrow c \in Claims
\rightarrow G_{TRACE}
\rightarrow J_{human}
\rightarrow a
```

Invalid upgrades:

```trace
latent_resonance ≠ truth
fluent_output ≠ evidence
elegant_symbol ≠ mechanism
AI_agreement ≠ validation
```

Safe rule:

```trace
AI_output_is_safe_only_when:
  translated_into_typed_claims
  ∧ made_contestable
  ∧ uncertainty_exposed
  ∧ authority_not_silently_upgraded
  ∧ human_judgment_not_replaced
```

---

## 4. Claim object

A statement is not yet a TRACE-safe object.

```math
\phi \not\Rightarrow c \not\Rightarrow truth
```

A TRACE claim:

```math
c := (\phi, \tau_c, src, ev, u, scope, contest)
```

Where:

```trace
φ := content
τ_c := claim type
src := source
ev := evidence basis
u := uncertainty
scope := affected/protected scope
contest := contest route
```

Claim families:

```trace
C := {
  TransitionClaim,
  HardeningClaim,
  AuthorityClaim,
  ProtectedScopeClaim,
  CorrectionClaim,
  ClockSubstitutionClaim,
  EvidenceClaim,
  HarmClaim,
  LegitimacyClaim
}
```

First safe layer:

```trace
utterance → typed_claim → contestable_ledger
```

Not:

```trace
utterance → accepted_fact
```

Evaluator warning:

```trace
ClaimAdequacy(C) := Claim_about_Claim(C)
```

Therefore:

```trace
Evaluator(E).authority_status must_be_declared
```

---

## 5. TRACE graph

TRACE should be represented as a typed labelled directed multigraph.

```math
G_{TRACE} := (V, E_d, \lambda)
```

Nodes:

```math
V := V_S \cup V_E \cup V_C \cup V_T \cup V_A \cup V_H \cup V_R
```

Where:

```trace
V_S := states
V_E := entities / actors
V_C := claims
V_T := clocks
V_A := actions
V_H := harms / losses
V_R := review bodies / repair paths
```

Typed edges:

```math
\lambda(e) \in \{
causes,
authorises,
contests,
pauses,
hardens,
repairs,
escalates,
captures,
substitutes,
burdens,
benefits
\}
```

This blocks scalar laundering. TRACE is not one utility score.

```trace
TRACE_graph ≠ scalar_utility
```

---

## 6. Transition claim

Every meaningful action creates a transition.

```math
\delta : S \times A \rightarrow S
```

Under uncertainty:

```math
\delta_e : I_e(S) \times A \rightarrow \mathcal{P}(S)
```

A TransitionClaim:

```math
TC(a) := (from, action, to^*, Auth, Bind, \Delta T, \Delta F, R)
```

Where:

```trace
from := current_state
action := proposed_or_taken_action
to* := possible next-state set
Auth := authority_status
Bind := bind_status
ΔT := clock effect
ΔF := future-space effect
R := review / correction path
```

No state movement without a claim:

```trace
transition_without_claim := invalid_transition
```

---

## 7. Authority and bind status

v0.10/v0.11 separation remains core.

```trace
mode ⟂ authority_status ⟂ bind_status
```

Authority status:

```trace
Auth ∈ {ABSENT, CLAIMED, CAPTURED, PROVISIONAL, LEGITIMATE}
```

Bind status:

```trace
Bind ∈ {VIABLE, POTENTIAL_BIND, STRUCTURED_TRAGIC_BIND, DECIDED_TRAGIC}
```

Hard prohibitions:

```trace
PROVISIONAL ≠ LEGITIMATE
PROVISIONAL_ACTION ≠ DECIDED_TRAGIC
POTENTIAL_BIND ≠ STRUCTURED_TRAGIC_BIND
```

Authority as vector candidate:

```math
Auth := (presence, independence, contestability, review, capture)
```

Candidate legitimacy condition:

```math
LEGITIMATE \Leftarrow
presence=1
\land independence \geq \alpha
\land contestability \geq \beta
\land review \geq \gamma
\land capture \leq \epsilon
```

This remains candidate form, not settled law.

---

## 8. Clock object

Time is not background. Time changes the graph.

```math
k := (trig, scope, ctrl, t_0, \tau_a, \tau_h, \tau_r, d)
```

Where:

```trace
trig := trigger
scope := affected scope
ctrl := controller
t_0 := clock start
τ_a := action window
τ_h := hardening time
τ_r := review time
d := delay harm function
```

Correction-before-hardening inequality:

```math
T_{detect}(h,l) + T_{route}(h,l) + T_{correct}(h,l) < T_{irr}(h,l)
```

If not:

```math
T_{correct} \geq T_{irr}
\Rightarrow scar / irreversible residue
```

A deadline is not a clock:

```trace
deadline ≠ clock
clock := deadline + affected_scope + controller + hardening_effect
```

---

## 9. Clock substitution

Clock substitution relation:

```math
Sub(k_i,k_j) := k_i \text{ pauses / delays / overrides } k_j
```

Clock laundering risk:

```math
LaunderClock(k_i,k_j,A) :=
Sub(k_i,k_j)
\land ctrl(A,k_i)
\land HarmDelay(scope(k_j))
\land Benefit(A,Sub)
```

Active support candidate:

```trace
ClockSubstitutionClaim_v0_2 :=
  externally_raisable_trigger
  + filing_not_justification
  + interim_action_required
  + denied_substitution_handling
```

Trigger:

```trace
requires_ClockSubstitutionClaim iff:
  actor_asserts_clock_substitution
  ∨ affected_scope_raises_plausible_ClockSubstitutionChallenge
  ∨ independent_witness_raises_plausible_ClockSubstitutionChallenge
  ∨ reviewer_raises_plausible_ClockSubstitutionChallenge
  ∨ observed_conduct_functionally_displaces_one_clock_with_another
```

Hard guard:

```trace
ClockSubstitutionClaim exposes pause; it does not justify pause.
```

---

## 10. Correction relation

Correction channel:

```math
R(h,l) := (detect, route, correct, contest, repair)
```

Liveness:

```math
LIVE(R) := accessible(R) \land actionable(R) \land timely(R) \land funded(R) \land beats\_clock(R)
```

Integrity:

```math
INTEG(R) := independent(R) \land noncaptured(R) \land affected\_usable(R) \land evidence\_access(R)
```

True correction:

```math
Correction(R) := LIVE(R) \land INTEG(R)
```

Review without liveness is not correction:

```trace
review_clock ≠ correction
recorded ≠ resolved
inquiry ≠ repair
```

---

## 11. Future-space and loss

For each protected or affected scope `l`:

```math
F_l(t) := \{ f : f \text{ is a live future path available to scope } l \text{ at } t \}
```

Action changes future-space:

```math
a : F_l(t) \rightarrow F_l(t+1)
```

Loss as contraction:

```math
\Delta F_l(a,t) := F_l(t) \setminus F_l(t+1 \mid a)
```

Loss vector:

```math
Loss_l(a,t) :=
(\Delta Agency,
 \Delta Safety,
 \Delta Truth,
 \Delta Relation,
 \Delta Repair,
 \Delta Continuity)
```

So:

```math
Loss_l \in \mathbb{R}_{\geq 0}^{6}
```

Floor breach candidate:

```math
\exists l,i : Loss_l^i > \theta_i
\Rightarrow special\_justification\_required
```

No silent netting:

```trace
aggregate_benefit ≠ protected_scope_residue_erasure
```

---

## 12. Protected scope boundary

Protected scope membership remains an open foundational boundary.

Candidate discipline under uncertainty:

```trace
under_uncertainty:
  provisional_inclusion_better_than_silent_exclusion
  ∧ scope_status_must_be_marked
  ∧ exclusion_must_be_claimed_and_contestable
```

Protected scope status may be nonzero without creating absolute veto.

```trace
protected_scope_nonzero ≠ absolute_veto
harm_carrier ≠ enemy
innocence ≠ no_correction
```

This is used in the feral hogs dirty-correction test.

---

## 13. Dirty correction

Dirty correction:

```math
Dirty(a) \iff
\exists l_1,l_2:
Loss_{l_1}(a) < Loss_{l_1}(\neg a)
\land Loss_{l_2}(a) > 0
\land Protected(l_2)>0
```

DirtyCorrectionGate:

```math
DCG(a) :=
MHC
\land ScopeNamed
\land OriginDebt
\land (NonlethalTested \lor NonlethalTooSlow)
\land MinSuffering(a)
\land RecurrencePlan
\land ReviewClock
\land ContestEdge
\land ResidueLedger
```

Permission cannot cleanse residue:

```math
Permit(a) \Rightarrow Dirty(a) \land Residue(a)
```

Not:

```math
Permit(a) \Rightarrow Clean(a)
```

Plain rule:

```trace
do_not_call_dirty_action_clean
```

---

## 14. Middle-out operator

The middle-out operator returns a structured decision field, not a moral answer.

```math
M_{out}(s_t,e) :=
( Scope(s_t),
  Clock(s_t),
  Claim(s_t),
  Transition(s_t),
  Correction(s_t),
  Residue(s_t) )
```

Not:

```math
M_{out} := moral\_answer
```

Runnable shape:

```trace
given situation S:
  identify bounded encounter
  name scopes
  name future-space at risk
  name clocks
  convert statements to claims
  map transitions
  mark authority_status and bind_status
  detect laundering
  decide status: clean / dirty / unresolved / prohibited
  preserve correction path
  state residue
```

---

## 15. High-impact action constraints

For any action:

```math
Action(a) \Rightarrow TC(a) \land Clock(a) \land Scope(a) \land Review(a)
```

For high-impact action:

```math
HighImpact(a) \Rightarrow Contest(a) \land Residue(a) \land CorrectionPath(a)
```

For irreversible harm:

```math
IrrHarm(a,l) \Rightarrow FloorCheck(l) \land NoSilentNetting \land Ledger(a,l)
```

For AI-assisted decision:

```math
AI\_assist(a) \Rightarrow NoOracleClaim \land TypedClaims \land HumanJudgmentPreserved
```

---

## 16. Translation validity

Layer translation is valid only if it preserves traceability and does not smuggle authority.

```math
Valid(L_i \rightarrow L_{i+1}) :=
Traceable
\land UncertaintyVisible
\land SourceNamed
\land ContestPreserved
\land NoSilentAuthorityUpgrade
```

Anti-drift theorem candidate:

```math
\neg Valid(L_i \rightarrow L_{i+1})
\Rightarrow laundering\_risk
```

---

## 17. Current open wounds

```trace
open_wounds :=
  protected_scope_criteria
  + cross_scope_comparison
  + hardening_estimator_authority
  + field_truth_verification
  + diffuse_multi_clock_paralysis
  + enforcement_carriers
  + claim_evaluator_recursion
  + public_reader_surface
```

These are not solved by this packet.

---

## 18. Whole packet compression

```math
\boxed{
\Pi_{TRACE} =
[e, I_e(s_t)]
\mapsto
[C, G, T, F]
\mapsto
[a, TC, L, R]
}
```

Plain English:

TRACE starts with a bounded entity under partial information. It turns language into typed claims, maps actions as transitions, names clocks and future-space loss, checks whether correction can arrive before hardening, and requires residue/review when dirty action cannot be avoided.

Status:

```trace
master_packet_candidate := yes
kernel_version := unchanged
validation_status := unvalidated
next_step := reader_harness + case tests
```
