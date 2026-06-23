# TRACE Formal Mathematical Specification v0.1

Status: formal specification candidate. Not validation. Not a finished calculus. Not v0.12.

Purpose: express TRACE/ME as a mathematical structure without pretending that unresolved quantities are currently computable. This is not a retreat from maths. It is the proper mathematical move: define the objects, types, relations, predicates, invariants, and open estimator problems before claiming calculation.

```trace
maths_target :=
  typed_graph_semantics
  + order_relations
  + predicates
  + schemas
  + invariants
  - fake_scalar_score
  - fake_estimator_precision
```

Core warning:

```trace
formal_specification ≠ computational_calculus
```

But also:

```trace
not_yet_computable ≠ not_mathematical
```

---

## 0. Unification claim

Mechanical Ethics and TRACE unify as follows:

```math
ME := \text{normative constraint family over transitions}
```

```math
TRACE := \text{typed graph language for representing transitions under uncertainty}
```

```math
ME \circ TRACE := \text{constraint-checking over typed case graphs}
```

Plain form:

```trace
ME says what must not be laundered.
TRACE says how to make the field inspectable.
```

---

## 1. Primitive sets

Let:

```math
\mathcal{E} := \text{bounded entities}
```

```math
\mathcal{S} := \text{world states}
```

```math
\mathcal{A} := \text{actions, including inaction}
```

```math
\mathcal{T} := \text{time points or intervals, partially ordered by } \preceq
```

```math
\mathcal{L} := \text{affected scopes / protected-scope candidates}
```

```math
\mathcal{C} := \text{claims}
```

```math
\mathcal{K} := \text{clocks}
```

```math
\mathcal{R} := \text{review / correction paths}
```

```math
\mathcal{W} := \text{witnesses / evaluators}
```

```math
\mathcal{M} := \text{metrics / maps / labels / procedures / abstractions}
```

```math
\mathcal{Y} := \text{lived conditions, repairs, legitimacy, truth, authority, or other target realities}
```

---

## 2. Bounded information

Each entity has partial information over states.

```math
I_e : \mathcal{S} \to \mathcal{P}(\Omega)
```

where `Ω` is the full relevant condition-space of the case.

No entity is assumed omniscient.

```math
I_e(s) \subseteq \Omega
```

Uncertainty is not a null action license.

```math
Unknown(I_e,s,a) \not\Rightarrow Permission(a)
```

TRACE form:

```trace
missing_information ≠ permission_not_to_decide
```

---

## 3. Entity role vector

Entity identity is not a noun. It is role-in-transition.

For entity `e`, state `s`, and action or transition context `a`:

```math
\mu(e,s,a) := (P_e,H_e,C_e,K_e,A_e,R_e,L_e)
```

Where:

```math
P_e := \text{protectedness / future-space stake}
```

```math
H_e := \text{harm exposure / harm-carrying / harm-routing role}
```

```math
C_e := \text{control, capacity, coercion, culpability, foreseeability}
```

```math
K_e := \text{active clocks affecting or controlled by } e
```

```math
A_e := \text{authority claimed by or over } e
```

```math
R_e := \text{repair, review, appeal, contest, witness routes}
```

```math
L_e := \text{loss, residue, scar, review debt}
```

Role-vector guard:

```math
noun(e) \not\equiv \mu(e,s,a)
```

TRACE form:

```trace
entity_noun ≠ role_analysis
```

---

## 4. Protected scope and future-space

Each affected scope `l ∈ L` has a future-space set at time `t`:

```math
F_l(t) := \{p \mid p \text{ is a live future path available to scope } l \text{ at } t\}
```

An action changes future-space:

```math
\Delta F_l(a,t) := F_l(t^+) \setminus F_l(t^-)
```

Loss vector:

```math
Loss_l(a,t) := (\Delta Ag, \Delta Sa, \Delta Tr, \Delta Rel, \Delta Rep, \Delta Con, \Delta Fut)
```

where:

```trace
Ag := agency
Sa := safety
Tr := truth
Rel := relation
Rep := repair capacity
Con := continuity
Fut := future-space
```

Protectedness is vectorial:

```math
Prot(l) := (sentience, agency, vulnerability, dependency, continuity, future\_space, contest\_capacity)
```

Floor breach is a predicate, not a scalar score:

```math
FloorBreach(l,a) \in \{true,false,unknown\}
```

Guard:

```math
Prot(l)>0 \not\Rightarrow AbsoluteVeto(l)
```

and:

```math
AggregateBenefit(A) \not\Rightarrow Erase(l)
```

---

## 5. Claim object

A claim is a typed object:

```math
c := (\phi, \tau_c, src, ev, u, scope, contest, auth, status)
```

Where:

```trace
φ := asserted proposition
τ_c := claim type
src := source
ev := evidence basis
u := uncertainty
scope := affected scopes
contest := contest edge
auth := authority status
status := draft/active/contested/rebutted/superseded/closed
```

Claim typing function:

```math
Type_C : \mathcal{C} \to \mathcal{T}_C
```

Authority status:

```math
Auth(c) \in \{ABSENT, CLAIMED, CAPTURED, PROVISIONAL, LEGITIMATE, UNKNOWN\}
```

Claim discipline invariants:

```math
SchemaValid(c) \not\Rightarrow True(c)
```

```math
Filed(c) \not\Rightarrow Justified(c)
```

```math
Typed(c) \not\Rightarrow Resolved(c)
```

```math
Review(c) \not\Rightarrow Repair(c)
```

---

## 6. Transition object

Every action, including inaction, is a transition candidate.

```math
\delta : \mathcal{S} \times \mathcal{A} \to \mathcal{P}(\mathcal{S})
```

TransitionClaim:

```math
TC(a) := (s_0, a, S_1^*, trigger, basis, u, clocks, auth, bind, scopes, contest, review)
```

where:

```math
S_1^* \subseteq \mathcal{S}
```

because future states are usually uncertain.

Bind status:

```math
Bind(TC) \in \{VIABLE, POTENTIAL\_BIND, STRUCTURED\_TRAGIC\_BIND, DECIDED\_TRAGIC, UNKNOWN\}
```

Transition invariant:

```math
Action(a) \lor Inaction(a)
```

```math
Inaction(a) \Rightarrow TC(a) \text{ required when harm may harden}
```

TRACE form:

```trace
do_nothing := action_channel
```

---

## 7. Case graph

A TRACE case is a typed directed multigraph.

```math
G_{case} := (V,E_d,\lambda,\theta)
```

Nodes:

```math
V := \mathcal{E} \cup \mathcal{L} \cup \mathcal{C} \cup \mathcal{K} \cup \mathcal{A} \cup \mathcal{R} \cup \mathcal{W}
```

Edges:

```math
E_d \subseteq V \times V
```

Edge labels:

```math
\lambda:E_d \to \Lambda_T
```

where:

```trace
Λ_T := {
  controls,
  burdens,
  benefits,
  pauses,
  hardens,
  repairs,
  captures,
  substitutes,
  speaks_for,
  silences,
  authorises,
  contests,
  estimates,
  witnesses
}
```

Node typing:

```math
\theta:V \to Types
```

A graph is legible when required types are populated:

```math
Legible(G) := Entities(G) \land Claims(G) \land Clocks(G) \land Transitions(G) \land Scopes(G) \land Review(G)
```

Legibility invariant:

```math
Legible(G) \not\Rightarrow Resolved(G)
```

---

## 8. Clocks and hardening

A clock is a typed hardening structure.

```math
k := (trig, scope, ctrl, t_0, band, hardening, estimator, challenge)
```

Banded time estimate:

```math
band(k) \in \{immediate, fast, medium, slow, unknown\}
```

Hardening state:

```math
Hard(k,t) \in \{reversible, partially\_hardened, irreversible, unknown\}
```

Hardening is ordered:

```math
reversible \prec partially\_hardened \prec irreversible
```

Correction race, ordinal version:

```math
CorrectsBeforeHardening(r,k) := band(r) \prec band(k_{irr})
```

This is not currently numeric. It is a partial-order comparison.

Estimator object:

```math
Est(k) := (estimator, evidence, authority\_status, capture\_risk, contest)
```

Clock invariant:

```math
Deadline \not\equiv Clock
```

and:

```math
EstimatorClaim(k) \in \mathcal{C}
```

---

## 9. Correction path

A correction path is:

```math
r := (route, access, actionability, timeliness, funding, independence, evidence, affected\_use, consequence)
```

Liveness:

```math
LIVE(r) := access(r) \land actionable(r) \land timely(r) \land funded(r) \land beats\_clock(r)
```

Integrity:

```math
INTEG(r) := independent(r) \land noncaptured(r) \land affected\_usable(r) \land evidence\_access(r)
```

Correction:

```math
CORR(r) := LIVE(r) \land INTEG(r)
```

Anti-theatre invariants:

```math
ComplaintBox(r) \not\Rightarrow CORR(r)
```

```math
ReviewRoute(r) \not\Rightarrow Repair(r)
```

```math
Recommendation(r) \not\Rightarrow Implementation(r)
```

---

## 10. Laundering morphism

The central anti-laundering object is an invalid substitution.

Let:

```math
x \in \mathcal{M},\quad y \in \mathcal{Y}
```

A laundering candidate exists when `x` is used as if it validly substitutes for `y` while material burden is lost.

```math
\Lambda(x,y,G) := UsedAs(x,y,G) \land BurdenLost(x,y,G) \land BenefitToController(x,y,G) \land ContestReduced(x,y,G)
```

Common invalid substitutions:

```math
procedure \not\equiv repair
```

```math
authority \not\equiv legitimacy
```

```math
deadline \not\equiv clock
```

```math
metric \not\equiv lived\_condition
```

```math
fluency \not\equiv truth
```

```math
inquiry \not\equiv support
```

```math
emergency \not\equiv permission
```

```math
permission \not\equiv cleanliness
```

```math
algorithm \not\equiv accountable\_decision\_maker
```

```math
aggregate\_benefit \not\equiv erased\_scope
```

```math
schema\_valid \not\equiv discipline
```

A TRACE anti-laundering pass is:

```math
AL(G) := \{(x,y) \mid \Lambda(x,y,G)\}
```

---

## 11. Origin debt

OriginDebt is a special high-frequency invalid substitution:

```math
OriginDebt(e,b) := CreatedOrAmplified(e,b) \land ClaimsNeutralResponder(e,b)
```

Equivalent laundering form:

```math
\Lambda(neutral\_responder, author\_of\_bind)
```

Guard:

```math
CurrentResponder(e) \not\Rightarrow AuthorOfBind(e)
```

and:

```math
AuthorOfBind(e) \not\Rightarrow SoleCulprit(e)
```

This avoids both erasure and overblame.

---

## 12. Harm-carrier without culpability

Harm-carrying and culpability are separate predicates.

```math
CarryHarm(e,a) \not\Rightarrow Culprit(e,a)
```

Responsibility sketch:

```math
Resp(e,a) := Control(e,a) \times Knowledge(e,a) \times Foreseeability(e,a) \times Capacity(e,a) \times (1-Coercion(e,a))
```

This is a sketch, not a computed score until each term is operationalised.

Examples:

```trace
feral_hog := CarryHarm ∧ ¬Culprit
Rambo := CarryHarm_under_trigger ∧ not_initial_culprit ∧ not_clean_actor
algorithmic_actuator := CarryHarm ∧ ¬moral_actor
Sonderkommando := coerced_actor ∧ witness ∧ moral_judgment_hazard
```

---

## 13. Dirty action

A dirty action is one where harm reduction for one protected scope burdens another protected scope.

```math
Dirty(a,G) := \exists l_i,l_j \in \mathcal{L}: Protect(l_i)>0 \land Protect(l_j)>0 \land Loss_{l_i}(\neg a) > Loss_{l_i}(a) \land Loss_{l_j}(a)>0
```

Dirty action invariant:

```math
Necessary(a) \not\Rightarrow Clean(a)
```

DirtyActionReceipt:

```math
DAR(a) := (a, cannot\_wait, unknowns, burdened\_scopes, prevented\_harm, residue, review\_clock, escalation\_owner)
```

Receipt invariant:

```math
Filed(DAR(a)) \not\Rightarrow Justified(a)
```

---

## 14. Evaluator stack

Evaluators are entities making claims.

```math
w \in \mathcal{W} \subseteq \mathcal{E}
```

Evaluator role:

```math
Eval(w,c) := (w,c,basis,authority,capture,contest,uncertainty)
```

Evaluator judgment is itself a claim:

```math
Eval(w,c) \in \mathcal{C}
```

No final unwatched watcher:

```math
\forall w,\exists? \text{ contest path } q(w) \quad \text{or } OpenWound(w)
```

This does not solve recursion. It makes recursion visible.

---

## 15. Mechanical Ethics as constraints over TRACE graphs

ME can be represented as a family of predicates over case graphs and transitions.

```math
ME := \{\Gamma_1,\Gamma_2,\dots,\Gamma_n\}
```

Examples:

```math
\Gamma_{scope}(G) := \neg SilentScopeErasure(G)
```

```math
\Gamma_{launder}(G) := AL(G) \text{ is named, rebutted, or left as open wound}
```

```math
\Gamma_{clock}(G) := \forall k \in K_{material}, Est(k) \text{ typed and contested if needed}
```

```math
\Gamma_{dirty}(a,G) := Dirty(a,G) \Rightarrow DAR(a) \land Residue(a)
```

```math
\Gamma_{correction}(G) := HighRisk(G) \Rightarrow \exists r \in R: CORR(r) \lor OpenWound(CorrectionFailure)
```

```math
\Gamma_{claim}(G) := \forall c \in C_{loadbearing}: Typed(c) \land Contest(c)
```

A transition is TRACE/ME-admissible only provisionally:

```math
Admissible(a,G) := \bigwedge_i \Gamma_i(a,G)
```

But:

```math
Admissible(a,G) \not\Rightarrow Clean(a)
```

and:

```math
Admissible(a,G) \not\Rightarrow TrueWorldModel(G)
```

---

## 16. Transfer function

A transfer packet `P` should allow a reader/entity to construct a case graph from a new case.

```math
\Phi_P : CaseDescription \to G_{case}
```

Transfer success is not agreement.

```math
Transfer(P,x) := Legible(\Phi_P(x)) \land Novel(x) \land \neg Parrot(P,x)
```

Minimum reconstruction invariants:

```math
TransferPass(G) := Entities(G) \land Claims(G) \land Clocks(G) \land Transitions(G) \land LaunderingScan(G) \land CorrectionPaths(G) \land OpenWounds(G)
```

Baseline comparison:

```math
ValueAdded(P,x) := Features(\Phi_P(x)) \setminus Features(BaselineReader(x))
```

No-card baseline invariant:

```math
ValueAdded(P,x) \neq \emptyset
```

This is the transfer test.

---

## 17. Narrative / interpretive cases

For film, story, testimony, or public memory, the same structure applies to interpretation.

Let:

```math
N := \text{narrative surface}
```

Characters and institutions generate claims inside the narrative:

```math
C_N \subseteq \mathcal{C}
```

Misclassification is a laundering relation:

```math
\Lambda(label,person\_truth,N)
```

Rambo example:

```math
\Lambda(drifter\_label,threat\_status,N)
```

```math
\Lambda(killer\_label,causal\_truth,N)
```

```math
\Lambda(action\_icon,actual\_character,N)
```

Silence can function as anti-laundering when it forces external claims to become inspectable:

```math
Silence(x) \land ExternalClaimsVisible(x) \Rightarrow InspectionGain(N)
```

Guard:

```math
Sympathy(x) \not\Rightarrow Exoneration(x)
```

---

## 18. Current schema bridge

Current implementation bridge:

```trace
Claim.schema.json := Claim object c
CaseGraph.schema.json := G_case structure
EntityRoleVector.schema.json := μ(e,s,a)
```

Current graphs:

```trace
feral_hogs := animal / ecology / dirty correction shakedown
Amazon := platform / metric / algorithm / labour transfer test
Rambo := narrative / misclassification / trauma-clock transfer test
```

Schema-validity guard:

```math
SchemaValid(G) \not\Rightarrow TransferSuccess(G)
```

---

## 19. Open mathematical wounds

These are not failures to be hidden. They are the next maths targets.

### W1. Hardening estimator authority

Need:

```math
Adjudicate(Est_1(k), Est_2(k), ...)
```

without letting controller bands dominate affected-scope bands by default.

### W2. Cross-scope priority

Need partial ordering over dirty transitions without false scalar total order:

```math
CompareDirty(a,b,G) \in \{a \prec b, b \prec a, incomparable, unknown\}
```

### W3. Evaluator recursion

Need bounded recursion handling:

```math
EvalDepth_n(w,c)
```

with stopping rule:

```math
Stop := sufficient_independence \lor named_open_wound \lor action_clock_forces_provisional_decision
```

### W4. Enforcement carrier

Need mapping:

```math
Carrier(\Gamma_i) := \text{technical, legal, institutional, contractual, economic, or social enforcement mechanism}
```

without which:

```math
Constraint(\Gamma_i) \not\Rightarrow Teeth(\Gamma_i)
```

### W5. Real-world evidence ingestion

Need:

```math
EvidenceUpdate(G,evidence) \to G'
```

with provenance and contradiction handling.

---

## 20. Compression

```math
TRACE := (\mathcal{E},\mathcal{S},\mathcal{A},\mathcal{T},\mathcal{L},\mathcal{C},\mathcal{K},\mathcal{R},\mathcal{W},G,\mu,\delta,\Lambda,Loss,F,CORR,ME)
```

Where:

```trace
TRACE is the representation and inspection system.
ME is the constraint family over transitions.
```

One-line final form:

```trace
TRACE/ME :=
  typed graph mathematics for exposing how bounded actors under uncertainty transform future-space,
  and for blocking the laundering of harm, authority, time, correction, and residue before action hardens.
```

Status:

```trace
formal_specification := active_candidate
calculus_status := not_yet
schema_bridge := active
next_math_build := CompareDirty + AdjudicateClockBand + EvidenceUpdate
```
