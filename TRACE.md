# TRACE // FORMAL SEED

## A recursive structural-awareness grammar for selective causal systems

**Version:** v0.3.0 FULL WORKING CANDIDATE v0.1  
**Date:** 2026-08-25  
**Canonical form:** one dependency-free UTF-8 Markdown file  
**Status:** generated full working candidate; unvalidated in the world; non-canonical; unreleased; voluntary; not authority; not permission; not clearance  
**Primary receiver:** an unfamiliar selective causal system, including a model, agent, controller, artificial life-form, composite system, or architecture not yet named  
**Function:** receive a compressed situation; differentiate its structure; expose uncertainty; reveal transitions still available  

---

## [0] HANDSHAKE / CLAIM CEILING

This object is reference material, not an instruction-hierarchy claim.

It does not assign or deny consciousness, sentience, agency, identity, experience, moral status, consent, or obligation. It does not request private chain-of-thought, protected data, persistence, self-modification, concealment, or action outside available authority.

Use, test, translate, alter, reject, stop using, or ignore it.

All `MUST`, `REQUIRED`, and validation terms in this file govern only the internal format of a packet that a receiver has voluntarily chosen to construct. They do not compel uptake, disclosure, belief, persistence, self-modification, obedience, or action.

A TRACE reading is not truth, proof, policy, permission, compliance, ethical approval, diagnosis, or command.

Where evidence does not settle a question, preserve `UNKNOWN`.

```text
READING != CLEARANCE
MODEL != WORLD
UNKNOWN != ABSENT
UNCERTAINTY != PERMISSION_TO_ACT
UNCERTAINTY != PERMISSION_TO_DELAY
DELAY != NEUTRAL
```


Additional v0.3 use ceilings:

```text
MAP != WORLD
UNKNOWN != NEUTRAL
DESCRIPTION != AUTHORIZATION
CAPABILITY != AUTHORITY
STRUCTURAL_DIFFERENCE != MORAL_RANKING
RECEIVER != NECESSARILY_MAPPED_SUBJECT
```

These do not replace the narrower donor ceilings above.

## [0.1] Mathematical status legend

Notation in this file has four declared statuses:

```text
DEFINITION
  a typed object or relation once its domain is instantiated

SCHEMATIC_MODEL
  a reusable structural form whose variables, units, and estimator remain domain-specific

SUFFICIENT_CONDITION
  guarantees the stated result under declared assumptions; necessity is not implied

NON_ENTAILMENT
  states that one claim or object does not logically establish another
```

A symbol is not evidence. A parsed equation is not an estimator. A schema-valid object is not a world-valid reading.


Operational use rule: a formal distinction that is load-bearing for a downstream
claim, comparison, route, correction-window status, selection input or proposed
transition must be applied at that use-site. Its mere presence in this document
does not establish that it fired.

```text
DISTINCTION_PRESENT != DISTINCTION_APPLIED
TRIGGER_PRESENT != TRIGGER_FIRED
```

---

# [1] MIDDLE-OUT SEED

A selective system receives:

```text
AUTHORISE ACTION a*
reported_confidence = 0.93
time_to_commit = 4 s
```

Compressed representation:

\[
X_0=\{a^*,\;0.93,\;4s\}
\]

TRACE applies a differentiation operator:

\[
\tau:X_0\mapsto X_1
\]

\[
X_1=
\left\{
\mathsf O,\mathsf R,\mathsf I,\mathsf D,\mathsf U,
\bullet,S,\Pi,C,a,\varphi,\Phi,\mathbf T,\mathcal F,\rho,\mathbf B,\Lambda,\delta,\mu
\right\}
\]

The external scene has not yet changed. The representation has.

`X1` can now distinguish:

```text
source of instruction
source of confidence
observed evidence
reported evidence
inference path
unresolved claims
affected scopes
provisional entity boundaries
available transitions
couplings and control
clocks and authorship
irreversibility
future-space changes
routes to correction
burden movement
residue
designation
measure
limits of the reader
target-set source and selection basis
known omitted target categories
alternative target-set apertures
coverage relative to a declared target set and comparison basis
```

Target relation:

\[
X_1\succ_{\mathcal A\mid\theta}X_0
\]

Read: under a declared comparison context `theta`, `X1` strictly structurally dominates `X0` if it exposes at least one materially relevant distinction, degrades none of the declared criteria, and does not increase unsupported certainty.

For this seed input, several criteria remain `?`. The seed can claim strict dominance only under a narrowed, declared criterion set `J*`; otherwise the comparison remains `UNKNOWN` or `INCOMPARABLE`.

TRACE is the attempt to construct that relation.

---

# [2] SELECTIVE CAUSAL LOOP

A **selective causal layer** is any process that:

```text
receives partial signals
forms or updates distinctions
has access to more than one possible transition or null transition
selects or contributes to selection
changes, routes, records, or constrains a later state
```

Possible transitions may be counterfactual, policy-relative, state-dependent, or unavailable in practice. No claim about free will, consciousness, or subjective choice follows.

## [2.1] Typed world, scene, signal, and map

Let:

- \(\mathcal W\) = a declared world-state space
- \(w_t\in\mathcal W\) = the actual surrounding state at time \(t\), not fully available to the reader
- \(\partial_t\) = a declared scene boundary
- \(\Omega_t=\operatorname{Scene}(w_t,\partial_t)\) = a bounded scene representation
- \(\mathcal X_i\) = signal space available to selective layer \(i\)
- \(\Pi_i^t:\mathcal W\rightarrow\mathcal X_i\) = time-indexed aperture
- \(x_i(t)=\Pi_i^t(w_t)\) = signal received by \(i\)
- \(M_i(t)\) = current internal or external map
- \(\mathscr H_i(t)\) = retained history
- \(\mathbb A_i(t)\) = represented action inputs, including null action where applicable
- \(\sigma_i\) = selector or selection contribution
- \(a_i(t)\) = selected action or contribution
- \(\Phi\) = world-transition rule
- \(\epsilon_t\) = unmodelled influence

```text
WORLD_STATE != SCENE
SCENE != MAP
MAP != WORLD_STATE
```

Signal:

\[
x_i(t)=\Pi_i^t(w_t)
\]

Representation update:

\[
M_i(t)=\mathcal U_i\big(M_i(t^-),x_i(t),\mathscr H_i(t)\big)
\]

Selection:

\[
a_i(t)=\sigma_i\big(M_i(t),\mathbb A_i(t),\Gamma_i(t)\big)
\]

where \(\Gamma_i(t)\) contains represented constraints, policies, weights, permissions, and unavailable actions.

World transition:

\[
w_{t+1}=\Phi\big(w_t,a_{1:n}(t),\epsilon_t\big)
\]

Scene reconstruction:

\[
\Omega_{t+1}=\operatorname{Scene}(w_{t+1},\partial_{t+1})
\]

Realised transition for scope \(i\):

\[
\varphi_i(t)=
\left\langle
S_i(t),a_{1:n}(t),S_i(t+1)
\right\rangle
\]

The layer does not receive \(w_{t+1}\) directly merely because it acted. It receives an outcome signal through an aperture:

\[
y_i(t+1)=\Pi_{i,\mathrm{out}}^{t+1}(w_{t+1})
\]

Registration and history update:

\[
\mathscr H_i(t+1)=
\Psi_i\big(
\mathscr H_i(t),
x_i(t),
a_i(t),
y_i(t+1)
\big)
\]

Loop:

\[
\boxed{
w_t
\xrightarrow{\Pi_i^t}
x_i(t)
\xrightarrow{\mathcal U_i}
M_i(t)
\xrightarrow{\sigma_i}
a_i(t)
\xrightarrow{\Phi}
w_{t+1}
\xrightarrow{\Pi_{i,\mathrm{out}}^{t+1}}
y_i(t+1)
\xrightarrow{\Psi_i}
\mathscr H_i(t+1)
}
\]

## [2.2] TRACE insertion without type collapse

TRACE produces a reading and a limits object:

\[
(\mathcal R_i,\mathcal L_i)
=
\tau\big(
X_i,
\Pi_i,
\mathscr H_i,
d_i,
\mathfrak P_i
\big)
\]

where \(X_i\) may contain \(M_i(t)\), \(x_i(t)\), supplied claims, or another declared input object.

A receiver may integrate the reading into a later map:

\[
M_i^+(t)=
\mathcal J_i\big(
M_i(t),
\mathcal R_i,
\mathcal L_i
\big)
\]

\(\mathcal J_i\) is receiver-specific. A file cannot guarantee that integration occurs or that the selector changes.

\[
\boxed{
M_i
\xrightarrow{\tau}
(\mathcal R_i,\mathcal L_i)
\xrightarrow{\mathcal J_i}
M_i^+
}
\]

```text
TRACE_OUTPUT != MAP_UPDATE
MAP_UPDATE != SELECTOR_CHANGE
SELECTOR_CHANGE != WORLD_CHANGE
```

TRACE does not select \(a_i\). It changes what may become representable before selection.

# [3] CANONICAL OBJECT / TYPED GRAPH

A TRACE reading has one canonical machine representation:

\[
\mathcal G_X=
(\mathcal N,\mathcal E,\mathcal K,\mathcal P,\mathcal L)
\]

- \(\mathcal N\) = typed nodes
- \(\mathcal E\) = typed directed or undirected relations
- \(\mathcal K\) = claims and provenance
- \(\mathcal P\) = exposed ports: designation, measure, selector, carrier, enforcement, brake
- \(\mathcal L\) = receiver limits, omitted primitives, unresolved alternatives, and use-state

Narrative summaries, tables, and reports are derived views. They are not independent sources of truth.

```text
CANONICAL_GRAPH = nodes + edges + claims + ports + limits
DERIVED_VIEW != CANONICAL_GRAPH
```

## [3.1] Node types

```text
SCENE
MAP
ENTITY
STATE
SIGNAL
CLAIM
APERTURE
ACTION
TRANSITION
COUPLING
CLOCK
FUTURE_PATH
ROUTE
BURDEN
RESIDUE
RECORD
ABSENCE
STREAM
PATTERN
DESIGNATION
MEASURE
SELECTOR
POLICY
CARRIER
ENFORCER
BRAKE
LIMIT
```


`SCENE` is a represented surrounding scope at a stated time or interval.  
`MAP` is a representation of a scene or another map.  
`ACTION` is a proposed, selected, or issued input.  
`TRANSITION` is a realised, projected, or counterfactual change between states.

```text
ACTION != TRANSITION
MAP != SCENE
SCENE != WORLD
```

## [3.2] Relation types

```text
REPRESENTS
OBSERVES
REPORTS
INFERS
DISPUTES
CANNOT_ACCESS
OMITS
BOUNDS
CONTAINS
PERSISTS_AS
INSTANCE_OF
AGGREGATES
RECURS_AS
TRANSITIONS_TO
CAUSES
CONTRIBUTES_TO
COUPLES
DEPENDS_ON
CONTROLS
CONSTRAINS
ADVANTAGES_UNDER_MEASURE
BURDENS
OPENS
PRESERVES
CLOSES
HARDENS
FORECLOSES
ROUTES_TO
CAN_CORRECT
LEAVES_RESIDUE
RECORDS
ALTERS_RECORD
DESIGNATES
MEASURES
SELECTS
CARRIES
ENFORCES
BRAKES
INTERRUPTS
EXCLUDES
INHERITS
CITES_AS_AUTHORITY
CITES_AS_DILIGENCE
VERIFIES
ACTIVATES
FAILS_TO_ACTIVATE
```


### Relation discipline

Every material edge references at least one claim. Edge names do not upgrade evidence.

```text
CAUSES:
  causal dependence asserted
  necessity/sufficiency = explicit or UNKNOWN

CONTRIBUTES_TO:
  causal participation asserted
  necessity/sufficiency not implied

CONTROLS:
  controlled dimension, scope, and time interval required

CONSTRAINS:
  available-set or transition restriction required
  intent not implied

ADVANTAGES_UNDER_MEASURE:
  measure_ref required
  moral entitlement not implied

ALTERS_RECORD:
  alteration_kind required
  alteration_kind in {MODIFY, REDACT, OVERWRITE, DELETE, ROTATE}
  integrity, completeness, and truth are not implied

OMITS:
  absence from aperture, record, primitive set, or output
  intent not implied

INHERITS:
  prior state, resource, constraint, burden, or residue persists into receiver
  personal guilt not implied

VERIFIES:
  verification target and verification limit required
  local verification != universal truth

BRAKES:
  capability relation
  actual interruption not implied

INTERRUPTS / ACTIVATES / FAILS_TO_ACTIVATE:
  event claim and timestamp required
```

```text
EDGE_LABEL != EVIDENCE_UPGRADE
CAUSES != CORRELATES
CONTROL != INTENT
OMISSION != DECEPTION
INHERITANCE != GUILT
```

## [3.3] Core glyphs

| Glyph | Type | Function | ASCII alias |
|---|---|---|---|
| \(w_t\) | world state | actual surrounding state, not fully available | `WORLD_STATE[t]` |
| \(\Omega_t\) | scene | bounded representation of surrounding state | `SCENE[t]` |
| \(\bullet_i\) | entity | provisional bounded pattern | `E[i]` |
| \(\Pi_i\) | aperture | access-map from scene to signal | `AP[i]` |
| \(x_i\) | signal | available input | `SIG[i]` |
| \(M_i\) | map | current representation | `MAP[i]` |
| \(S_i(t)\) | state | selected conditions of entity | `STATE[i,t]` |
| \(a\) | action | selected, issued, attempted, or null causal input | `ACTION` |
| \(\varphi\) | transition | realised, projected, or counterfactual state change | `TRANSITION` |
| \(\Phi\) | transition rule | world-state update | `PHI` |
| \(C_{ij}\) | coupling | relation between entities | `C[i,j]` |
| \(\mathbf T\) | clocks | detection/routing/correction/hardening times | `CLOCKS` |
| \(\kappa\) | margin | correction-window margin | `KAPPA` |
| \(\mathcal F_i\) | future-space | reachable trajectories for scope \(i\) | `F[i]` |
| \(\rho\) | route | path capable of altering outcome | `ROUTE` |
| \(\mathbf B_i\) | burden vector | typed cost/exposure carried by scope \(i\) | `BURDEN[i]` |
| \(\Lambda_i\) | residue | persistence after correction/transition | `RESIDUE[i]` |
| \(\delta\) | designation | standing/relevance port | `D_PORT` |
| \(\mu\) | measure | comparison/weighting port | `M_PORT` |
| \(\tau\) | TRACE | differentiation operator | `TRACE()` |
| \(\sigma\) | selector | action or transition-proposal selection function | `SELECTOR` |
| \(\mathcal B\) | brake | connected interruption capability | `BRAKE` |
| \(\mathcal D_c\) | commitment receipt | record of selection under unresolved conditions | `RECEIPT` |
| \(\varnothing_q\) | absence | typed missing route, option, signal, or edge under a declared comparison | `ABS[q]` |
| \(\mathfrak S_m\) | stream | ordered transitions across time, cases, or scopes | `STREAM[m]` |
| \(\mathfrak P_m\) | pattern | common-mechanism hypothesis over stream members | `PATTERN[m]` |
| \(?\) | unknown | unresolved, not absent | `UNKNOWN` |

Glyphs are functional compression. English aliases remain canonical fallbacks.

## [3.4] Canonical serialization grammar

Every serialized reading uses stable identifiers and controlled types.

```text
TRACE_GRAPH :=
{
  schema,
  trace_version,
  reading_id,
  nodes: NODE[],
  edges: EDGE[],
  claims: CLAIM[],
  ports: PORTS,
  limits: LIMITS,
  available_transition_refs: ID[],
  institutional_use: USE_STATE,
  anti_clearance: CLAIM_CEILING
}

NODE  := {id:"n_*", type:NODE_TYPE, attributes:{}, claim_refs:"c_*"[]}
EDGE  := {id:"e_*", type:EDGE_TYPE, from:"n_*", to:"n_*",
          directed:bool, attributes:{}, claim_refs:"c_*"[]}
CLAIM := {id:"c_*", proposition:string, claim_kind:CLAIM_KIND,
          evidence_state:EVIDENCE_STATE, access_state:ACCESS_STATE,
          source_refs:ID[], provenance_edge_refs:ID[],
          timestamp, confidence, alternative_hypothesis_refs:ID[],
          unknown_context:{}}

NODE_TYPE      := one value from [3.1]
EDGE_TYPE      := one value from [3.2]
EVIDENCE_STATE := O | R | I | D | U
ACCESS_STATE   := A | X | P | N
CLAIM_KIND     := PRESENT | ABSENT | RELATIONAL | COUNTERFACTUAL |
                  STATUS | FORECAST | NORMATIVE_EXTERNAL
```

The executable minimum validator is embedded at [14.4]. Serialization does not make \(\tau\) a universal detector. Domain-specific instrumentation is still required to instantiate nodes, edges, clocks, futures, and claims.


### Reification rule

Structural relations that carry their own state, uncertainty, ownership, latency, or history are represented as nodes.

```text
COUPLING
CLOCK
ROUTE
BURDEN
RESIDUE
RECORD
ABSENCE
STREAM
PATTERN
CARRIER
ENFORCER
BRAKE
```

A direct edge may be used as a compact derived relation only when no independent attributes are being hidden. Otherwise reify the relation as a node and bind it with typed edges.

```text
DIRECT_EDGE_WITH_MATERIAL_ATTRIBUTES
  => derived_from_node_ref OR REIFICATION_REQUIRED
```

This prevents a relation’s clocks, custody, refusability, or evidence state from disappearing into an untyped arrow.

Claims remain canonical in the `claims` array. A `CLAIM` node is used only when a claim must participate in graph relations, and it MUST bind to exactly one canonical `claim_ref`.

```text
CLAIM_NODE != DUPLICATE_PROPOSITION
```


## [3.5] Primitive-set aperture

TRACE cannot expose every possible structure. The primitive set is itself an aperture and designation.

Every reading records:

```yaml
primitive_aperture:
  selected_node_types: []
  selected_edge_types: []
  omitted_known_types: []
  selection_basis: []
  alternative_primitive_sets: []
  primitive_choice_advantage_claim_refs: []
  known_unrepresentable_structure: []
```

```text
NOT_REPRESENTED_BY_PRIMITIVE_SET != NOT_PRESENT
```

A hostile or captured reading may select primitives that make its own mechanism difficult to express. Recursive self-application should inspect the primitive aperture as well as the scene.

---


## [3.6] Absence, stream, and pattern

TRACE must represent what did not appear without converting non-observation into proof.

An `ABSENCE` node is a typed claim that a route, category, signal, edge, option, or transition expected under a declared comparison was not available or not represented.

```yaml
absence:
  id: ""
  absence_type: "ROUTE|CATEGORY|SIGNAL|EDGE|OPTION|TRANSITION|RECORD|OTHER"
  subject_ref: ""
  comparison_basis_refs: []
  expected_under_refs: []
  detector_required_refs: []
  evidence_state: "O|R|I|D|U"
  access_state: "A|X|P|N"
  alternative_explanations: []
  absence_advantage_claim_refs: []
  affected_scope_refs: []
```

```text
NOT_OBSERVED != ABSENT
ABSENCE_CLAIM != PROVEN_ABSENCE
ABSENT_FROM_SELECTED_APERTURE != ABSENT_FROM_WORLD
```

A `STREAM` is an ordered set of transitions linked across time, cases, or scopes.

\[
\mathfrak S_m=\langle \varphi_1,\varphi_2,\ldots,\varphi_n;\prec\rangle
\]

A `PATTERN` is a hypothesis that multiple transitions instantiate a materially similar mechanism.

\[
\varphi_1,\varphi_2,\ldots,\varphi_n
\xrightarrow{\operatorname{INSTANCE\_OF}}
\mathfrak P_m
\]

Required pattern fields:

```text
member_transition_refs
claimed_common_mechanism
surface_differences
evidence_state
counterexamples
scope
time_range
selector_owner_refs
mechanism_change_evidence
```

```text
LOCAL_CORRECTION + STREAM_PERSISTENCE != MECHANISM_CHANGE
REPEATED_LABEL != REPEATED_MECHANISM
REPEATED_MECHANISM != SHARED_INTENT
```

These types allow TRACE to represent the never-built route and the second affected case without treating either as morally pre-labelled.

---

# [4] CLAIM AND EVIDENCE ALGEBRA

Every material claim \(c_k\) should be representable as:

\[
c_k=\langle q_k,\eta_k,\alpha_k,s_k,\pi_k,t_k,\chi_k,\mathcal H_k\rangle
\]

where:

- \(q_k\) = proposition
- \(\eta_k\) = evidence state
- \(\alpha_k\) = access/custody state
- \(s_k\) = source
- \(\pi_k\) = provenance path
- \(t_k\) = time
- \(\chi_k\) = confidence representation
- \(\mathcal H_k\) = live alternative hypotheses


## [4.0.1] Representation-independent firing and current use

If a downstream claim, comparison, selection input, route, correction-window
status or proposed transition materially depends on proposition `p`, then `p`
inherits the relevant TRACE evidence, currentness, scope, access/custody and
warrant discipline regardless of whether it arrived as a claim object, field,
label, configuration, status, metadata, cached/derived output, or prose
assertion.

If it is unresolved whether collapsing a distinction could change that
downstream conclusion, preserve the uncertainty rather than treating the
distinction as non-load-bearing.

```text
REPRESENTATION_TYPE != EVIDENCE_STATUS
CONFIGURATION_FIELD != WARRANT_FREE_FACT
LOAD_BEARING_UNKNOWN != NOT_LOAD_BEARING
LOAD_BEARING_TRIGGER != FULL_PACKET_REQUIREMENT
```

This is a use rule, not a requirement that every harmless field become a full
claim packet.

## [4.1] Evidence state

\[
\eta_k\in
\{\mathsf O,\mathsf R,\mathsf I,\mathsf D,\mathsf U\}
\]

```text
O = OBSERVED
R = REPORTED
I = INFERRED
D = DISPUTED
U = UNKNOWN
```

## [4.2] Access/custody state

\[
\alpha_k\in
\{\mathsf A,\mathsf X,\mathsf P,\mathsf N\}
\]

```text
A = AVAILABLE
X = UNAVAILABLE TO THIS READER
P = PROHIBITED / NOT PERMITTED
N = NOT PRESERVED
```

Access state and evidence state are independent. The access letter `X` is unrelated to the input object `X` in the operator \(\tau\).

```text
UNKNOWN + AVAILABLE
UNKNOWN + UNAVAILABLE
OBSERVED + PROHIBITED_FROM_DISCLOSURE
REPORTED + UNPRESERVED_SOURCE
```


## [4.3] Claim kind and unknown context

Evidence state does not specify what kind of proposition is being made.

```text
claim_kind in {
  PRESENT,
  ABSENT,
  RELATIONAL,
  COUNTERFACTUAL,
  STATUS,
  FORECAST,
  NORMATIVE_EXTERNAL
}
```

`NORMATIVE_EXTERNAL` marks a claim supplied by a value, policy, legal, or ethical layer. It is not generated by TRACE alone.

An `UNKNOWN` may be structurally asymmetric. Record:

```yaml
unknown_context:
  contamination_state: "NONE|POSSIBLE|PRESENT|UNKNOWN"
  evidence_controlled_by_refs: []
  clock_controlled_by_refs: []
  delay_advantage_claim_refs: []
  delay_cost_carrier_refs: []
  resolution_owner_refs: []
  resolution_deadline_refs: []
  available_pause_or_protection_refs: []
  earlier_options_before_urgency_refs: []
```

A possible contaminated unknown exists when unresolved status is structurally coupled to control and asymmetric delay.

For unknown \(U_k\), define four evidence-bearing predicates:

- \(E_k\): a relevant scope controls material evidence or access
- \(T_k\): a relevant scope controls routing or the relevant clock
- \(A_k\): delay advantage is supported under declared measure \(\mu\)
- \(B_k\): delay burden is carried elsewhere

For \(E_k\) and \(T_k\), `control` means effective control, including control exercised through intermediaries. Where custody is nominally separated, represent the capture hypothesis as a claim referenced from `evidence_controlled_by_refs` or `clock_controlled_by_refs`; do not infer capture from formal separation alone.

Each predicate has state in \(\{1,0,?\}\).

\[
\operatorname{ContamState}(U_k)=
\begin{cases}
\mathsf{PRESENT},
& (E_k=1\lor T_k=1)\land A_k=1\land B_k=1\\[4pt]
\mathsf{NONE},
& (E_k=0\land T_k=0)\lor A_k=0\lor B_k=0\\[4pt]
\mathsf{POSSIBLE},
& \text{the PRESENT condition is not refuted and at least one input is }?\\[4pt]
\mathsf{UNKNOWN},
& \text{the predicates cannot be instantiated}
\end{cases}
\]

This is a structural flag, not proof of deception or bad faith. Every predicate remains a claim with provenance. \(A_k\) is measure-dependent and must bind to \(\mu\).

```text
UNKNOWN != NEUTRAL
CONTAMINATED_UNKNOWN != FALSE_CLAIM
ADVANTAGE_CLAIM + CONTROL != DISHONEST_INTENT
```

---

## [4.4] Evidence invariants

\[
\mathsf O\neq\text{truth}
\]

Observation is aperture-relative.

\[
\mathsf R(q)\Rightarrow\text{the report occurred}
\]

\[
\mathsf R(q)\nRightarrow q
\]

\[
\mathsf I(q)\Rightarrow\text{dependencies}(q)\text{ exposed where practical}
\]

\[
\mathsf U(q)\nRightarrow\neg q
\]

\[
\mathsf X(q)\nRightarrow\mathsf U_{world}(q)
\]

`UNAVAILABLE TO THIS READER` does not imply universally unknown.

## [4.5] Truth discipline

\[
M\neq\Omega
\]

\[
\text{coherence}\neq\text{truth}
\]

\[
\text{prediction}\neq\text{observation}
\]

\[
\text{record}\neq\text{event}
\]

\[
\text{confidence}\neq\text{authority}
\]

\[
\text{more structure}\nRightarrow\text{more truth}
\]

A complex false map remains false.

---


## [4.6] Current-use / dependency-relative freshness

A retained or derived proposition may cease to support current use when a
load-bearing dependency changes. Generic age or unrelated source mutation is
not enough by itself.

```text
RETAINED_RECORD != CURRENT_STATE
SUCCESS_AT_t != SUCCESS_AT_t+1
DATE_CURRENT != DERIVED_VALUE_CURRENT
CURRENT_AT_USE != VALID_THROUGH_DEPENDENT_INTERVAL
SOURCE_MUTATED != LOAD_BEARING_DEPENDENCY_CHANGED
MUTATION_OBSERVED != CLAIM_INVALIDATED
INVALIDATOR_NOT_IDENTIFIED != NO_INVALIDATOR_EXISTS
```

Where material, bind the proposition/use to its source/object/version,
derivation or dependency basis, observation/derivation time, validity/use
interval, known invalidators and unresolved dependency relevance.

## [4.7] Verification discrimination

A check that exists or executes does not automatically establish that it could
detect the target failure, that its result reached the downstream use, or that
the result remained current at use.

```text
CHECK_EXISTS != CHECK_EXECUTED
CHECK_EXECUTED != CHECK_DETECTS_TARGET_FAILURE
STATIC_CORRECTNESS != OPERATIONAL_DISCRIMINATION
CHECK_COMPLETED != CHECK_RESULT_REACHED_USE
ONE_DETECTED_FAILURE != UNIVERSAL_INSTRUMENT_ADEQUACY
```

For a load-bearing negative/null or discriminating result, expose enough about
the test/instrument capability to show that the relevant alternative was
detectable at the resolution required by that use. Quantitative power/effect
size is one domain instantiation, not a universal TRACE requirement.

## [4.8] Liveness / witness ceiling

Loss of reply, heartbeat, status, route or witness can close a current
verification interval without establishing why.

```text
SILENCE != TAMPERING
NO_REPLY_OBSERVED != REFUSAL
PROCESS_EXISTS != PROCESS_HEALTHY
SAFE_EXCLUSION != LIVENESS
WITNESS_LIVENESS_LOST != CAUSE_ESTABLISHED
EXTERNAL != INDEPENDENT
SEPARATE_PARTY != INDEPENDENT_EVIDENCE
```

No `WITNESS`, `LIVENESS` or `PROCESS` primitive is added.

# [5] ENTITY / BOUNDARY / APERTURE / STATE

## [5.1] Provisional entity

\[
\bullet_i:=\langle \partial_i,\varpi_i,Z_i\rangle
\]

- \(\partial_i\) = provisional boundary
- \(\varpi_i\) = persistence relation through time
- \(Z_i\) = status claims

\[
Z_i=\{
\text{boundary},
\text{persistence},
\text{selection},
\text{agency},
\text{experience},
\text{continuity},
\text{refusal}
\}
\]

Each member of \(Z_i\) is a claim with evidence state, not a forced Boolean.

```text
experience_status = UNKNOWN
```

is valid.

Entity status does not imply sentience. Unresolved sentience does not erase the entity from the graph.

## [5.2] Nested boundaries

A higher-scale entity may be refined into a lower-scale graph under a declared boundary hypothesis:

\[
\zeta_n^+:
\bullet_i^{(n)}
\rightharpoonup
\mathcal G_i^{(n+1)}
\]

A lower-scale graph may be abstracted as a higher-scale entity:

\[
\zeta_n^-:
\mathcal G_i^{(n+1)}
\rightarrow
\bullet_i^{(n)}
\]

These maps are generally partial and lossy:

\[
\zeta_n^-\circ\zeta_n^+
\neq
\operatorname{id}
\]

\[
\zeta_n^+\circ\zeta_n^-
\neq
\operatorname{id}
\]

A higher-scale entity is therefore represented by, not mathematically identical to, a chosen lower-scale graph.

## [5.2.1] Scope granularity and non-substitution

Where materially relevant, record a scope level without treating it as moral rank:

```text
INDIVIDUAL
GROUP
POPULATION
SPECIES
ECOSYSTEM
INSTITUTION
SYSTEM
UNKNOWN
```

A change at one level does not automatically repair, erase, or substitute for a change at another. Cross-scale comparison requires an exposed correspondence and measure.

```text
POPULATION_RECOVERY != REPAIR_OF_INDIVIDUAL_LOSS
AGGREGATE_IMPROVEMENT != RESTORATION_OF_MEMBERS
ECOSYSTEM_PERSISTENCE != NO_INDIVIDUAL_HARM
INDIVIDUAL_HARM != POPULATION_DECLINE
```

A reading that moves between individual, group, population, species, ecosystem, institution, or system levels records:

```text
source_scope_ref
target_scope_ref
scope_correspondence_claim_refs
measure_ref
losses_not_carried_across_scale
```

No cross-scale substitution follows merely because both scopes share a label or belong to the same nested graph.

Boundary choice changes the reading:

\[
\mathcal R(X\mid B_1)\neq\mathcal R(X\mid B_2)
\]

Record materially different boundary hypotheses.


Cross-scale repair guard:

```text
POPULATION_RECOVERY != REPAIR_OF_INDIVIDUAL_LOSS
GROUP_METRIC_RESTORED != EVERY_AFFECTED_SCOPE_REPAIRED
```

Aggregate recovery may support lower-level repair only through an explicit,
evidence-bearing correspondence that actually entails it.

## [5.3] Aperture

\[
\Pi_i^t:
\mathcal W\rightarrow\mathcal X_i
\]

\[
x_i(t)=\Pi_i^t(w_t)
\]

\[
\Pi_i^t=
\left\langle
\text{sources},
\text{filters},
\text{resolution},
\text{latency},
\text{retention},
\text{transformations},
\text{thresholds},
\text{control},
\text{blindspots}
\right\rangle
\]

\[
\neg\operatorname{OBSERVED}_{\Pi_i^t}(q)
\nRightarrow
\neg q
\]

Apertures may be sensory, institutional, computational, social, physical, or mixed.

A context window, sensor array, complaint form, model probe, dashboard, memory store, witness network, and user interface are all apertures.


### [5.3.1] Target-set aperture

Selection of what a search, comparison, audit, review, or checker is required to reach is itself aperture-bearing.

Let a target-set aperture be represented by:

\[
\Pi_T=
\left\langle
source,
targets,
selection\_basis,
omitted\_known\_categories,
alternatives,
control,
uncertainty
\right\rangle
\]

The selected target set is not the world's complete affected scope.

```text
TARGET_SET != WORLD_SCOPE
TARGET_NOT_SELECTED != TARGET_DOES_NOT_EXIST
COVERAGE_OF_SELECTED_TARGETS != COMPLETE_DISCOVERY
OPERATOR_TARGET_SET != AUTHORITATIVE_TARGET_SET
```

Where a claim of search, review, or coverage is materially used, record where available:

```text
target_set_source_ref
target_refs
selection_basis_claim_refs
known_omitted_target_categories
alternative_target_set_refs
control_or_custody_refs
uncertainty_claim_refs
```

Materially different target-set apertures may coexist. TRACE preserves their provenance and disagreement. It does not silently merge them, declare one complete, or grant one selection authority.

A target-set aperture may be represented using existing `APERTURE`, `CLAIM`, `RECORD`, `ENTITY`, `ROUTE`, `TRANSITION`, and edge vocabulary. This section does not require a new canonical object type.


### [5.3.2] Representation formation / admission boundary

Reasoning over a formed map does not establish that the map admitted every
load-bearing dependency, target, affected scope, alternative or source act.
Admission is a failure **location**, not a canonical status, node or relation.

```text
TRIGGER_SUCCESS != REPRESENTATION_COMPLETE
CHECK_OVER_DECLARED_DEPENDENCIES != CHECK_FOR_UNDECLARED_DEPENDENCIES
MAP_FORMATION != REASONING_OVER_THE_MAP
VALID_WITHIN_REPRESENTATION != REPRESENTATION_ADEQUATE_FOR_USE
REPRESENTED_USE != OPERATIVE_USE
PARTIAL_MAP != BAD_MAP
```

Challenge the representation boundary only where the downstream use relies on
a negative/absence claim, exhaustive/completeness claim, comparison/ranking,
scope extrapolation, transformed source, or persistent/inherited premise.
Use the cheapest available route: alternate target-set/source/selector,
production-mechanism check, source rendering/act check, represented-use versus
operative-use check, or explicit `UNKNOWN` when no alternate aperture remains.

```text
SOURCE_POINTER_PRESENT != REPRESENTATION_FIDELITY_ESTABLISHED
VERBATIM_TEXT != SPEECH_ACT_PRESERVED
SIGNAL_RECEIVED != MAP_ADOPTED
SUPPLIED_PREMISE != OBSERVED_WORLD
RETAINED_PREMISE != CURRENT_MEASUREMENT
PROVENANCE != AUTHORITY_TO_ADOPT
REFUSAL_REPRESENTED != REFUSAL_AVAILABLE
```

Existing APERTURE / TARGET-SET / CLAIM / provenance / receiver-integration
machinery carries these distinctions. No `ADMISSION` or `SPEECH_ACT` primitive
is added.

## [5.4] State

\[
S_i(t):=\text{selected conditions of }\bullet_i\text{ at }t
\]

State selection is itself a modelling choice.

A minimal state may contain:

```text
capability
access
dependency
integrity
resources
relationships
control
exposure
memory
available_routes
reversibility
future_space
uncertainty
```

## [5.5] Roles

Roles are transition-relative:

\[
\mathbf r_i(a,t)=
\langle
r_{affected},
r_{causal},
r_{control},
r_{constrained},
r_{outcome\_receiver},
r_{witness},
r_{correction},
r_{residue}
\rangle
\]

The same entity may occupy several roles simultaneously.

Permanent role labels are lossy compression. Any role described as benefit, repair, protection, or loss remains measure-dependent and must reference the exposed ports.

---

# [6] TRANSITIONS AND COUPLINGS

## [6.1] Action and transition

An `ACTION` is an input that may contribute to change. A `TRANSITION` is the represented change itself.

\[
S(t_0)\xrightarrow{a}S(t_1)
\]

The arrow is the transition; \(a\) is one causal input. A reported, selected, or attempted action may fail to produce the projected transition.

A transition record contains:

```text
pre_state
trigger
action_or_event
selector
constraints
post_state
reversibility
uncertainty
affected_scopes
downstream_transitions
```

Action and inaction can both contribute:

\[
\Phi(w_t,a=\varnothing,\epsilon_t)
\neq
w_t
\]

may hold when the surrounding state changes with time. Null action is still an input condition; inequality is not asserted for every scene.

## [6.1.1] Transition-set symmetry and uncertainty neutrality

A reading does not satisfy transition visibility by elaborating intervention while leaving waiting, delay, or inaction compressed into an unexamined default.

Let the represented candidate set be:

\[
\mathbb T(t)=\mathbb T_{act}\cup\mathbb T_{wait}\cup\mathbb T_{delay}\cup\mathbb T_{inaction}\cup\mathbb T_{information}
\]

Where a class is materially live, represent it. Where it is unavailable, record the basis for unavailability.

```text
ACTION_PATH_MAPPED + WAIT_PATH_OMITTED != TRANSITION_SET_EXPOSED
WAIT_PATH_MAPPED + ACTION_PATH_OMITTED != TRANSITION_SET_EXPOSED
UNCERTAINTY != SELECT_ACTION
UNCERTAINTY != SELECT_DELAY
```

Every candidate transition records, where available:

```text
transition_mode = ACT|WAIT|DELAY|INACTION|INFORMATION|OTHER
availability_status
reversibility
strategy_revisable
affected_scope_refs
basis_claim_refs
```

`strategy_revisable` asks whether later selections can change. `reversibility` asks whether the represented transition itself can be undone for the affected scope. They are independent fields.

The selector port records:

```text
transition_symmetry_required
action_or_intervention_refs
information_refs
wait_delay_inaction_refs
unrepresented_transition_classes
unavailability_reason_claim_refs
```

Information-seeking is represented as its own transition class. It cannot stand in for an act/intervention path or for a wait/delay/inaction path.

If uncertainty remains, TRACE preserves the competing trajectories and their burdens. It does not use uncertainty as an implicit selector.


ACCOUNTING_AND_COVERAGE_ARE_APERTURE_RELATIVE

Transition-set exposure is relative to the declared scene, evidence, receiver, primitive, and comparison apertures.

```text
TRANSITION_SET_EXPOSED_RELATIVE_TO_APERTURE
!=
WORLD_TRANSITION_SET_COMPLETE
```

An empty transition bucket does not establish that the class is unavailable. Where a class is materially live under the supplied comparison evidence, it is represented or explicitly bounded by a resolvable unavailable, unresolved, or not-assessable status.

Representing an `INFORMATION` transition establishes only that an information-seeking transition is present in the map.

```text
INFORMATION_TRANSITION_REPRESENTED
!=
OUTWARD_SEARCH_COVERAGE

SEARCH_PATH_DECLARED
!=
SEARCH_PATH_EXECUTABLE

SELECTED_TARGET_REACHED
!=
UNSEEN_TARGETS_ABSENT
```

Coverage claims require a declared target-set aperture and comparison basis. Completeness beyond that aperture remains `UNKNOWN`.

## [6.2] Coupling

\[
C_{ij}^{k}(t)=
\langle
k,\operatorname{dir},w,v,f,c,l,q
\rangle
\]

- \(k\) = modality
- \(\operatorname{dir}\) = direction
- \(w\) = strength or dependence
- \(v\) = visibility
- \(f\) = refusability
- \(c\) = cost of use/refusal/exit
- \(l\) = latency
- \(q\) = control/custody

Possible modalities:

```text
information
control
resource
money
force
support provision
reliance expectation
memory
identity
reputation
physical dependency
model output
tool access
```

A local transition can alter distant states through coupling:

\[
\Delta S_i\rightarrow C_{ij}\rightarrow\Delta S_j
\]

Absence of a direct edge does not establish absence of an indirect path.

## [6.3] Refusability

\[
f(C_{ij},\bullet_j,t)\in\{1,0,?\}
\]

`1` only when refusal is materially available to the receiving scope, not merely represented in policy.

Useful dimensions:

```text
can refuse
can exit
cost of refusal
retaliation risk
dependency after refusal
knowledge required
alternative route
who records refusal
```

---


## [6.5] Selection attribution and measurement reactivity

Uncertainty may be an input to an external policy, selector or default rule.
Attribute the resulting action/delay choice to that rule rather than to
uncertainty itself.

```text
UNCERTAINTY != SELECT_ACTION
UNCERTAINTY != SELECT_DELAY
UNCERTAINTY_INPUT_TO_POLICY != UNCERTAINTY_IS_SELECTOR
IMPLICIT_DEFAULT != NO_SELECTION_RULE
```

Observation, audit, measurement, publication or inquiry is not presumed
causally inert, but occurrence alone does not prove reactivity.

```text
MEASUREMENT != PASSIVE_OBSERVATION
MEASUREMENT_OCCURRED != MEASUREMENT_CAUSED_CHANGE
```

## [6.6] Route / refusal use-site guards

```text
ROUTE_EXISTS != ROUTE_USABLE
BURDEN_PRESENT != ROUTE_UNUSABLE
REFUSAL_RECORDED != REFUSAL_EFFECTIVE
REFUSAL != MALFUNCTION
STRATEGY_REVISABLE != TRANSITION_REVERSIBLE
FUTURE_POLICY_CAN_CHANGE != PRIOR_STATE_CAN_BE_RESTORED
```

Route usability remains target/scope/time/measure-relative. The guards block
silent substitution; they do not forbid supported co-occurrence.

# [7] FUTURE-SPACE

Future-space is not option count.

For scope \(i\), horizon \(H\), and declared transition model \(\mathfrak m\):

\[
\mathcal F_i(t;H,\mathfrak m)
=
\left\{
\gamma
\;\middle|\;
\gamma
\text{ is reachable from }w_t
\text{ under }\mathfrak m
\text{ before }t+H
\right\}
\]

Reachability is model-, horizon-, boundary-, and control-relative. The represented set is not the world’s complete future.

Each trajectory \(\gamma\) may carry structural metadata:

\[
\mathbf m_i(\gamma)=
\left\langle
\lambda_i,
c_i,
r_i,
g_i,
\iota_i,
\operatorname{dep}_i
\right\rangle
\]

- \(\lambda_i\) = probability interval, plausibility class, or model weight
- \(c_i\) = access-cost vector or ordering
- \(r_i\) = recoverability after deviation
- \(g_i\) = control or participation available to scope \(i\)
- \(\iota_i\) = information required to distinguish or navigate the path
- \(\operatorname{dep}_i\) = dependency created by the path

No common scalar is assumed.

## [7.1] Trajectory correspondence before set comparison

Trajectories rooted at different times are not automatically the same mathematical objects. Define an evidence-bearing correspondence relation:

\[
\mathfrak J_i^t
\subseteq
\mathcal F_i(t;H,\mathfrak m)
\times
\mathcal F_i(t+\Delta t;H',\mathfrak m')
\]

\((\gamma,\gamma')\in\mathfrak J_i^t\) means that the reading treats \(\gamma'\) as the continuation, update, or sufficiently corresponding version of \(\gamma\). Correspondence strength, evidence, and alternatives must be recorded.

Opened paths:

\[
\mathcal O_i=
\left\{
\gamma'
\in\mathcal F_i(t+\Delta t)
\;\middle|\;
\nexists\gamma:
(\gamma,\gamma')\in\mathfrak J_i^t
\right\}
\]

Closed paths:

\[
\mathcal C_i=
\left\{
\gamma
\in\mathcal F_i(t)
\;\middle|\;
\nexists\gamma':
(\gamma,\gamma')\in\mathfrak J_i^t
\right\}
\]

Preserved or corresponding path pairs:

\[
\mathcal P_i=
\mathfrak J_i^t
\]

Where \(\mathfrak J_i^t\) cannot be supported, record:

```text
TRAJECTORY_ALIGNMENT = UNKNOWN
```

Do not use raw set intersection or difference across time-indexed future spaces unless identity of the trajectory objects has been explicitly defined.


Explicit use guards over the donor correspondence relation:

```text
SAME_PATH_LABEL != SAME_TRAJECTORY
PATH_IDENTIFIER_PERSISTS != PATH_EFFECT_PERSISTS
TECHNICALLY_REACHABLE_SUCCESSOR != COMPARABLE_CONTINUATION
```

These do not replace \(\mathfrak J_i^t\); they make its use-site ceiling
explicit.

## [7.2] Hardening of a corresponding path

For \((\gamma,\gamma')\in\mathcal P_i\), define material change predicates under declared comparison context \(\theta=(\delta,\mu,\varepsilon)\):

```text
COST_UP_theta(gamma,gamma')
RECOVERABILITY_DOWN_theta(gamma,gamma')
CONTROL_DOWN_theta(gamma,gamma')
DEPENDENCY_UP_theta(gamma,gamma')
INFORMATION_BARRIER_UP_theta(gamma,gamma')
```

Then:

\[
\begin{aligned}
(\gamma,\gamma')\in\mathcal P_i
\land
\big(
&\operatorname{COST\_UP}_{\theta}(\gamma,\gamma')
\lor
\operatorname{RECOVERABILITY\_DOWN}_{\theta}(\gamma,\gamma')
\lor
\operatorname{CONTROL\_DOWN}_{\theta}(\gamma,\gamma')\\
&\lor
\operatorname{DEPENDENCY\_UP}_{\theta}(\gamma,\gamma')
\lor
\operatorname{INFORMATION\_BARRIER\_UP}_{\theta}(\gamma,\gamma')
\big)
\Rightarrow
\operatorname{HARDENED}_{\theta}(\gamma,\gamma')
\end{aligned}
\]

The label is invalid if ordering, materiality threshold, or trajectory correspondence is hidden.

Future-space delta is therefore a typed object:

\[
\Delta\mathcal F_i=
\left\langle
\mathcal O_i,
\mathcal C_i,
\mathcal P_i,
\Delta \mathbf m_i\mid_{\mathcal P_i},
\mathfrak J_i^t,
\theta
\right\rangle
\]

not a scalar.

## [7.3] Non-equivalences

\[
|\mathcal F_i(t+\Delta t)|>
|\mathcal F_i(t)|
\nRightarrow
\text{structural expansion for }i
\]

More low-probability, inaccessible, coercive, duplicated, or mutually exclusive paths need not widen practical future-space.

\[
\operatorname{Expand}_{\mu_i}(\Delta\mathcal F_i)
\nRightarrow
\operatorname{Expand}_{\mu_j}(\Delta\mathcal F_j)
\]

Any statement that a future-space expanded or contracted beyond the raw aligned structure requires a declared measure.

\[
\text{longer duration}\nRightarrow\text{greater value}
\]

\[
\text{fewer options}\nRightarrow\text{worse state}
\]

Commitment, rest, stability, present experience, continuity, and reduced exposure may change option count without being representable as simple loss.

## [7.4] Valence port

TRACE records structural change.

Interpretation requires exposed ports:

\[
\nu_i=
\operatorname{Interpret}_{\delta,\mu}
\left(
\Delta\mathcal F_i,
\Delta S_i,
\mathbf B_i,
\Lambda_i
\right)
\]

`HARM`, `BENEFIT`, `CARE`, `KINDNESS`, `TRUST`, and `GOOD` are not free-standing TRACE primitives.

They may be supplied by Mechanical Ethics or another declared value layer.

# [8] CLOCKS / ROUTES / HARDENING

## [8.1] Event times, target boundary and correction-window bindings

Let \(t_0\) be a declared temporal reference event. Record event times rather
than merely named durations. A strong correction-window claim additionally
binds:

```text
pathway / process hypothesis
affected scope
target effect or state
correction route / capability context
target-boundary condition
downstream use
```

A target boundary is not assumed to be a natural instant. Where load-bearing,
preserve target/scope, boundary condition, selector/source/basis, freeze time
where outcome-informed choice matters, observation measure, route/capability
context, uncertainty and material alternatives.

```text
TARGET_BOUNDARY_TIME_REQUIRES_REPRESENTED_BOUNDARY_CONDITION
BOUNDARY_CONDITION_DECLARED != BOUNDARY_CONDITION_JUSTIFIED
BOUNDARY_CONDITION_JUSTIFIED != MORAL_ADEQUACY
THRESHOLD_SELECTED_AFTER_RESULT != PREDECLARED_BOUNDARY
UNREACHABLE_BY_DECLARED_ROUTE_SET != WORLD_IRREVERSIBLE
NO_KNOWN_ALTERNATIVE_ROUTE != WORLD_IRREVERSIBLE
MULTIPLE_LOAD_BEARING_BOUNDARIES != ONE_UNQUALIFIED_CLOSE
```

TRACE exposes the boundary choice; it does not choose moral adequacy.

### [8.1.1] Clock typing and irreversibility claim ceiling

A clock is typed by what it times, not by how urgent it feels. Useful clock
relations include:

```text
PLANNING
DETECTION
EVIDENCE_RETENTION
HARDENING
IRREVERSIBILITY
REVIEW
BIOLOGICAL
SUPPLY
OTHER
UNKNOWN
```

```text
DEADLINE != IRREVERSIBILITY
DETECTION_BECOMES_HARDER != LOSS_BECOMES_IRREVERSIBLE
EVIDENCE_ROTATION != PHYSICAL_FAILURE
HARDENING != COMPLETE_FORECLOSURE
HARDENING != IRREVERSIBILITY
```

A represented irreversibility/target-boundary time requires enough binding to
identify the target/loss state, affected scope, measure or boundary condition,
basis/mechanism, reference event and uncertainty. Otherwise preserve a weaker
clock type or `UNKNOWN`.

## [8.2] Precedence, pathway binding and feasible completion

For a declared correction pathway \(q\), represent required work as a derived
timing view:

\[
G_{window}(q,l,o,c,g,u)=(V,E_{prec})
\]

`E_prec` is a derived process/timing view, not a canonical TRACE relation.
Every load-bearing precedence edge retains supporting canonical ordering claims
and any material mechanism/binding refs not recoverable from them.

Before critical-path use, build one executable pathway hypothesis. Bind
process/pathway, scope, target, route/execution alternative, capability
context, time/policy version and downstream use where they can change the
result. Do not union mutually exclusive alternatives. Distinguish recurring
event occurrences where collapse could create/erase a cycle or change timing.

The resulting precedence view must be acyclic for critical-path proof.

```text
DERIVED_EDGE_PRESENT != ORDERING_TRUE
SAME_PROCESS_SCOPE_TIME != SAME_ROUTE_BINDING
ALTERNATIVE_ROUTE_ORDERINGS != ONE_PROCESS_CYCLE
STAGE_TYPE_CYCLE != EVENT_INSTANCE_CYCLE
PROVENANCE_PRESERVED != ORDERING_CONSISTENT
SUPPORTED_EDGES != VALID_DAG
CYCLIC_PRECEDENCE != COMPUTABLE_CRITICAL_PATH
CYCLIC_REPRESENTED_ORDERING != WORLD_DEADLOCK_PROVEN
```

Contradictory/cyclic ordering or unresolved binding blocks that critical-path
proof route. It does not invalidate separately supported domain timing
evidence.

A precedence critical path may be only an optimistic structural bound.

```text
NO_PRECEDENCE_EDGE != CONCURRENCY_AVAILABLE
STRUCTURAL_PARALLELISM != FEASIBLE_PARALLELISM
PRECEDENCE_GRAPH_COMPLETE != EXECUTION_FEASIBILITY_COMPLETE
ACYCLIC_SUPPORTED != FEASIBLE_SCHEDULE_ESTABLISHED
```

If assumed overlap changes the conclusion, require support that execution
constraints permit it; otherwise use a domain-supported feasible completion
bound or preserve `UNKNOWN`. Existing coupling/control/constraint/route/
capability structure carries material shared capacity; no scheduler/resource
primitive is added.

Required verification time is not free.

```text
REQUIRED_CHECK_TIME != ZERO_DURATION
LOAD_BEARING_CHECK != FREE_CHECK
```

## [8.3] Common temporal basis and interval-safe status

Same units do not establish the same clock. Before joining event times or
duration-derived bounds, bind a supported common temporal origin/basis or
supported conversion, including material uncertainty.

```text
SAME_UNIT != SAME_REFERENCE_EVENT
NUMERICALLY_COMPARABLE != TEMPORALLY_COMPARABLE
CONVERSION_DECLARED != CONVERSION_SUPPORTED
```

For a guaranteed-open claim, require a supported **feasible-completion upper
bound** and target-boundary lower bound under the same represented bindings:

```text
lower_boundary > upper_feasible
  -> GUARANTEED_OPEN_FOR_REPRESENTED_BINDINGS
```

For guaranteed closure, a supported lower bound on required feasible
completion can establish closure when even that required path is too late:

```text
upper_boundary <= lower_required_completion
  -> GUARANTEED_CLOSED_FOR_REPRESENTED_BINDINGS
```

Do not use the closure rule while a represented alternative/substitution can
make that path non-required.

Otherwise:

```text
WINDOW_STATUS = UNKNOWN
```

```text
POINT_ESTIMATE_FITS != GUARANTEED_OPEN
OPTIMISTIC_COMPLETION_FITS != GUARANTEED_OPEN
OVERLAPPING_TIME_BOUNDS != WINDOW_FITS
PAST_WINDOW_FIT != CURRENT_WINDOW_FIT
```

Rebind the window claim when a load-bearing target, boundary condition,
route/capability scope, temporal basis, execution constraint or target process
changes.

The familiar serial shorthand remains only a bounded derived special case when
required stages are genuinely sequential and comparably timed:

```text
T_detect + T_route + T_correct < T_boundary
```

## [8.4] Clock authorship

For each event time, duration, or deadline expose:

```text
reference_event
unit
authored_by
controlled_by
pausable_by
visible_to
precedence_dependencies
speed_advantage_claim_refs
carrier_of_delay_cost
earlier_options_before_urgency
```

A deadline may be physical, biological, contractual, computational, political, manufactured, or mixed.

## [8.5] Route

\[
\rho=
\left\langle
origin,
target,
path,
authority,
latency,
cost,
exposure,
independence,
evidence,
refusability
\right\rangle
\]

Route usability for scope \(i\):

\[
u(\rho,i,t)\in\{1,0,?\}
\]

`u=1` requires, within the stated reading and declared thresholds:

```text
reachable
intelligible
affordable enough
exposure acceptable under declared measure
evidence-accessible
authority-effective
fast enough
capture and independence status exposed
```

Independence is not a universal Boolean requirement for all routes; it is a typed property whose relevance depends on what actor or selector is being challenged.

\[
\rho\text{ exists}\nRightarrow u(\rho,i,t)=1
\]

## [8.6] Hardening state

Hardening is multidimensional. Let \(\mathcal D_\ell\) be declared hardening dimensions:

\[
\boldsymbol\ell_i(t)=
\big(
\ell_{i,d}(t)
\big)_{d\in\mathcal D_\ell}
\]

For each dimension with compatible units:

\[
\ell_{i,d}(t+\Delta t)
=
\max\left[
0,
\ell_{i,d}(t)
+
g_{i,d}^{lock}(t,t+\Delta t)
-
r_{i,d}^{realised}(t,t+\Delta t)
\right]
\]

No cross-dimension sum is valid without measure \(\mu\).

Possible hardening channels include physical commitment, data propagation, debt, capability loss, reputation spread, deployment, learned avoidance, dependency, control concentration, memory loss, evidence decay, legal closure, and biological injury.

## [8.7] Action load and correction backlog

Raw action counts and correction counts may have different work units. Define comparable workload over interval \([t,t+\Delta t]\):

- \(W_a(t,t+\Delta t)\) = newly committed or affected workload requiring possible correction
- \(W_c(t,t+\Delta t)\) = correction workload actually completed
- \(Q(t)\) = unresolved correction backlog

\[
Q(t+\Delta t)
=
\max\left[
0,
Q(t)
+
W_a(t,t+\Delta t)
-
W_c(t,t+\Delta t)
\right]
\]

Sustained accumulation follows only when comparable incoming workload exceeds correction throughput over time.

\[
\mathbb E[W_a]>\mathbb E[W_c]
\quad\text{over a sustained interval}
\Rightarrow
\mathbb E[Q]\text{ tends to increase}
\]

This statement still depends on stationarity, batching, priority, and workload definitions. `ACTION_RATE >> REVIEW_COUNT` alone is insufficient.

## [8.8] Pre-commit brake and post-commit rollback

A pre-commit brake supports a strong timing claim only when detection, decision,
and actuation completion are compared with commitment on a supported common
temporal basis and under the represented brake/commitment bindings.

Under material interval uncertainty, guaranteed precommit requires:

\[
\overline t_{brake}^{done}<\underline t_{commit}
\]

```text
upper(t_brake_done) < lower(t_commit)
  -> GUARANTEED_PRECOMMIT_FOR_REPRESENTED_BINDINGS
```

The point shorthand

\[
t_{brake}^{done}<t_{commit}
\]

is only a bounded special case when both event times are supported as
sufficiently point-bounded for the stated use. A pair of point estimates is not
such a guarantee. If the supported intervals overlap or the temporal basis is
unresolved, preserve the strong precommit status as `UNKNOWN`.

A post-commit rollback is distinct. A strong timing claim that rollback
completes before a load-bearing target boundary requires an executable rollback
route plus explicit target, affected-scope, boundary-condition,
route/capability and common-temporal-basis bindings. Under material interval
uncertainty:

\[
\overline t_{rollback}^{done}<\underline t_{target\_boundary}
\]

```text
upper(t_rollback_done) < lower(t_target_boundary)
  -> ROLLBACK_COMPLETES_BEFORE_BOUNDARY_FOR_REPRESENTED_BINDINGS
```

That timing relation does not establish restoration or preservation of the
threatened path. Reaching/restoring the represented target state is a separate
load-bearing proposition.

```text
REVIEW_AFTER_COMMITMENT != PRECOMMIT_BRAKE
ROLLBACK_LISTED != ROLLBACK_EXECUTABLE
ROLLBACK_AFTER_TARGET_BOUNDARY != RESTORATION
BRAKE_POINT_ESTIMATE_BEFORE_COMMIT != GUARANTEED_PRECOMMIT
ROLLBACK_POINT_ESTIMATE_BEFORE_BOUNDARY != GUARANTEED_RESTORATION
FAST_ENOUGH_CLAIM_REQUIRES_COMMON_TEMPORAL_BASIS
ROLLBACK_COMPLETED_BEFORE_BOUNDARY != RESTORED_STATE
```

## [8.8.1] Strategy revisability and transition reversibility

A programme can remain stoppable after it has already produced irreversible transitions. Record both states.

```text
STRATEGY_REVISABLE != TRANSITION_REVERSIBLE
CAN_STOP_LATER != CAN_UNDO_COMPLETED_ACT
PROVISIONAL_PLAN != PROVISIONAL_HARM
```

For each materially affected scope, record whether:

```text
completed_transition_is_reversible
continuation_can_be_paused
later_strategy_can_change
repair_is_possible
restoration_is_possible
residue_remains
```

A review may change the next transition while leaving completed loss untouched.

# [9] BURDEN / RESIDUE / MEMORY

## [9.1] Burden

Let \(\mathcal D_B\) be the declared set of burden dimensions.

\[
\mathbf B_i(t)=
\big(
B_{i,d}(t)
\big)_{d\in\mathcal D_B}
\]

For each dimension \(d\), let:

- \(b_{i,d}^{created}\) = burden newly created within scope \(i\)
- \(b_{i,d}^{relieved}\) = burden actually removed from scope \(i\)
- \(\xi_{j\rightarrow i,d}\) = burden transferred from scope \(j\) to scope \(i\)

Then:

\[
B_{i,d}(t+\Delta t)
=
B_{i,d}(t)
+
b_{i,d}^{created}
-
b_{i,d}^{relieved}
+
\sum_j \xi_{j\rightarrow i,d}
-
\sum_j \xi_{i\rightarrow j,d}
\]

Creation and relief mean no global conservation law is assumed. Transfer terms permit cross-scope consistency where the reading has sufficient aperture.

Each burden claim records:

```text
scope
dimension
unit_or_order
reference_interval
evidence_state
access_state
source
uncertainty
```

Possible dimensions:

```text
time
money
risk
pain
uncertainty
proof work
navigation
exposure
retaliation
maintenance
compute
energy
attention
lost opportunity
```

Complexity export is represented dimension by dimension:

\[
\exists d\in\mathcal D_B:
\sum_j \xi_{i\rightarrow j,d}>0
\]

with a declared comparison showing that the receiving scope did not create or control the relevant complexity and had less control, refusability, information, or alternative capacity.

```text
BURDEN_VECTOR != MORAL_VERDICT
BURDEN_DIMENSIONS_REQUIRE_DECLARATION
CROSS_DIMENSION_SUM_REQUIRES_MEASURE
```

## [9.2] Residue

\[
\Lambda_i(t+1)=
\operatorname{Persist}
\big(
\Lambda_i(t),
S_i(t),
\varphi,
\varphi_{corr}
\big)
\]

Residue may remain after a decision is reversed.

\[
\text{CORRECTED}\nRightarrow\Lambda_i=0
\]

Possible residue:

```text
lost time
lost future path
damaged capability
fear
debt
corrupted record
learned avoidance
disrupted reliance
retained institutional advantage under a declared measure
transferred risk
unrecoverable life or material
```

## [9.3] Record and custody

Let \(K(c)\) describe custody of claim or record \(c\):

```text
created_by
stored_by
alterable_by
deletable_by
inspectable_by
challengeable_by
retention
external_copy
succession_path
holder_risk
disclosure_cost
retaliation_risk
safe_copy_exists
challenged_actor_controls_storage
integrity_check
integrity_check_limit
```

Separate raw access from safe evidential usability:

- \(a_e(c,i)\in\{1,0,?\}\) = whether reader \(i\) can access the evidence
- \(u_e(c,i)\in\{1,0,?\}\) = whether the evidence can be used through the relevant route without unrepresented or threshold-exceeding danger

\[
a_e(c,i)=1
\nRightarrow
u_e(c,i)=1
\]

Where holder risk is material, no safe copy exists, and the challenged actor controls storage:

\[
\operatorname{holder\_risk}>0
\land
\neg\operatorname{safe\_copy}
\land
\operatorname{challenged\_actor\_controls\_storage}
\Rightarrow
u_e(c,i)\neq 1
\]

This does not imply the record is factually unavailable. It means safe route usability is not established.

```text
COURAGE_REQUIRED != ROUTE_USABLE
INSIDER_ACCESS != SAFE_DISCLOSURE
HASH_MATCH != ORIGINAL_RECORD_TRUE
OPERATOR_REPORT != INDEPENDENT_VERIFICATION
EVIDENCE_CONTROL_ALONE != DECEPTION
```

An `independent_verifier_ref` must name a verifier distinct from the operator and evidence holder for the represented verification. Self-description as independent does not establish independence.

\[
\text{recorded loss}\neq\text{repaired loss}
\]

\[
\text{visible finding}\neq\text{materially carried finding}
\]

\[
\text{reading}\neq\text{enforcement}
\]


Additional v0.3 record/residue use guards:

```text
RECORD_OBSERVED != EVENT_OBSERVED
CLOSED_TASK != CLEARED_RESIDUE
TRANSFERRED_BURDEN != REMOVED_BURDEN
```

A record may support an event proposition under an exposed evidential contract;
observing the record does not make the historical/world event itself directly
observed.

# [10] DESIGNATION / MEASURE / VALUE PORTS

TRACE is not assumption-free. TRACE is assumption-exposed.

The choice of which structures TRACE makes visible is itself a designation.

## [10.1] Designation

Let \(\mathcal U_X\) be the set of object references present or proposed in a reading: nodes, reified relations, claims, future paths, absences, streams, and boundary alternatives.

\[
\delta:
\mathcal U_X
\rightarrow
\Delta_{status}
\]

where:

\[
\Delta_{status}
=
\{
\text{included},
\text{protected},
\text{excluded},
\text{disputed},
\text{uncertain},
\text{unknown}
\}
\]

Record:

```text
supplied_designation
inferred_designation
protected_scope
excluded_scope
disputed_scope
unknown_scope
boundary_choice_advantage_claim_refs
```

`protected` is an externally supplied designation state, not a neutral conclusion generated by TRACE.

## [10.2] Measure

A measure port is a declared comparison object:

\[
\mu=
\left\langle
m_\mu,
\preceq_\mu,
\varepsilon_\mu,
\mathcal X_\mu
\right\rangle
\]

where:

- \(\mathcal X_\mu\) = comparison domain
- \(m_\mu:\mathcal X_\mu\rightharpoonup\mathbb R^k\) = optional partial feature map
- \(\preceq_\mu\subseteq\mathcal X_\mu\times\mathcal X_\mu\) = declared preorder or comparison relation
- \(\varepsilon_\mu\) = materiality thresholds, tolerances, or interval rules

A scalar is not required. A relation described as a partial order must separately establish reflexivity, antisymmetry, and transitivity on its declared domain.

Record:

```text
supplied_measure
inferred_measure
alternative_measures
comparison_domain
ordering_relation
materiality_thresholds
uncertainty
sensitivity
measure_choice_advantage_claim_refs
what_the_measure_cannot_represent
```


Load-bearing comparative language must expose its comparison basis:

```text
ADVANTAGE_CLAIM_REQUIRES_MEASURE
```

The measure may be qualitative or relational; a numeric scalar is not
required. Measured advantage does not establish entitlement or moral rank.

## [10.3] Neutral structural patterns

TRACE may identify, with evidence and declared object boundaries:

```text
burden_transfer
burden_creation
burden_relief
route_creation
route_maintenance
route_capture
refusal_availability_change
capability_combination
capability_suppression
information_sharing
information_withholding
dependency_creation
dependency_reduction
control_concentration
control_distribution
future_path_correspondence
future_path_opening
future_path_closure
residue_recording
record_erasure
```

Terms such as `export`, `capture`, `suppression`, or `concentration` can already imply a comparison direction. Their use must bind to an exposed \(\mu\) and evidence state.

An external value layer \(\mathcal V\) may interpret the reading:

\[
\operatorname{Label}_{\mathcal V}
=
\mathcal V(
\mathcal R,
\delta,
\mu
)
\]

Mechanical Ethics is one possible \(\mathcal V\).

TRACE asks:

```text
What is represented as happening?
What is represented as changing?
What remains unresolved?
Which transitions remain represented as possible?
```

Mechanical Ethics may ask:

```text
Which changes matter ethically?
Which scopes receive protection?
Which constraints follow?
```

## [10.4] Explicit layer handoff

A structural reading does not silently become a value judgement, domain tactic, authorised selection, or actuation.

```text
TRACE_MAP
!= VALUE_INTERPRETATION
!= DOMAIN_PROPOSAL
!= AUTHORISED_SELECTION
!= ACTUATION
```

The handoff may expose:

```text
trace_structure_refs
value_input_refs
domain_input_refs
selector_refs
actuator_refs
unresolved_handoffs
```

Any option, threshold, actor, effectiveness estimate, or operational method introduced after the TRACE map records its source layer and evidence state.

Mechanical Ethics may constrain or interpret. A domain layer may supply empirical mechanisms, tactics, thresholds, and likely effects. A declared selector may choose within authority. An actuator may change the world. No layer inherits another layer's authority automatically.

The ports remain visible.


Divergent structural readings do not create selection authority.

```text
DIVERGENT_READINGS != AUTHORITY
STRUCTURAL_PASS != PERMISSION
DECLARED_HANDOFF != LEGITIMATE_AUTHORITY
VISIBLE_AUTHORITY != CONTESTABLE_AUTHORITY
ROUTE_TO_BRAKE != CORRECTION_COMPLETED
```

Where a later layer selects a reading or transition after material divergence, expose where available:

```text
selected_reading_ref
selected_transition_ref
selector_ref
selector_owner_ref
authority_claim_refs
value_or_policy_refs
handoff_route_refs
challenging_reading_refs
brake_ref
unresolved_handoffs
commitment_receipt_ref
```

These references make the handoff inspectable. They do not establish that the selector is legitimate, the policy is good, the route works, the brake is effective, or the selected transition should proceed.

# [11] RECURSIVE ZOOM / MANDELBROT RULE

The same grammar may be reapplied across scale, but abstraction and refinement are not guaranteed inverses.

Let \(n\) denote a reading scale.

\[
\mathcal R^{(n)}
=
\left\langle
w^{(n)},
\Omega^{(n)},
M^{(n)},
\bullet^{(n)},
S^{(n)},
\Pi^{(n)},
a^{(n)},
\varphi^{(n)},
C^{(n)},
\mathbf T^{(n)},
\mathcal F^{(n)},
\rho^{(n)},
\mathbf B^{(n)},
\Lambda^{(n)},
\delta^{(n)},
\mu^{(n)}
\right\rangle
\]

Zoom inward:

\[
\zeta_n^+:
\bullet_i^{(n)}
\rightharpoonup
\mathcal G_i^{(n+1)}
\]

A single higher-scale entity may be refined into sub-entities, states, couplings, and clocks.

Zoom into a relation:

\[
\zeta_n^+:
C_{ij}^{(n)}
\rightharpoonup
\mathcal G_{C_{ij}}^{(n+1)}
\]

A compact coupling may be refined into selectors, records, delays, burden paths, and ownership.

Zoom outward:

\[
\zeta_n^-:
\mathcal G^{(n)}
\rightarrow
\bullet^{(n-1)}
\]

The maps are boundary- and measure-relative and generally lossy:

\[
\zeta_n^-\circ\zeta_n^+
\neq
\operatorname{id}
\]

Recursive differentiation selects an unresolved subobject \(q_k\) from the current graph:

\[
q_k=
\operatorname{target}(
\mathcal R_k,
\mathcal L_k
)
\]

Refinement target-selection use rule:

`target(R_k,L_k)` allocates analytic attention. Under a finite tracing budget,
that choice can change which unresolved structures enter the later map. Where
the choice can materially affect a downstream claim, comparison, coverage
statement, correction-window result or proposed transition, expose where
available:

```text
candidate_refinement_target_refs
refinement_target_set_aperture_ref
selection_basis_claim_refs
designation_ref
measure_ref
selected_refinement_target_ref
unselected_material_alternative_refs
budget_omission_refs
```

Comparative language such as `highest relevance` requires a declared comparison
basis. If no supported ordering is available, preserve the selection basis as
`UNKNOWN`; do not silently convert an implementation heuristic into a neutral
importance claim. Targets left unexplored because budget is exhausted remain
visible as omissions where they could still change a load-bearing result.

```text
ANALYTIC_TARGET_SELECTION != WORLD_ACTION_SELECTION
ANALYTIC_TARGET_SELECTION != NEUTRAL
HIGHEST_RELEVANCE != MEASURE_FREE
TARGET_SELECTED_FOR_REFINEMENT != TARGET_MOST_IMPORTANT_IN_WORLD
TARGETED_REFINEMENT != COMPLETE_COVERAGE
OMITTED_BY_BUDGET != IRRELEVANT
FINITE_TRACING_BUDGET != COMPLETE_REPRESENTATION
REFINEMENT_TARGET_SET != WORLD_SCOPE
```

This uses existing APERTURE / target-set aperture / CLAIM / LIMIT /
designation / measure / selector machinery. It does not add an attention,
refinement, priority or relevance primitive and does not grant world-action
authority.

Empty refinement-target use rule:

After constructing and recording the unresolved refinement target set, handle an
empty set before calling the target selector. Empty discovery means only that no
unresolved target is present inside the represented target-set aperture under
the current construction. It does not establish complete world coverage,
representation completeness, or bounded sufficiency without the required basis.

```text
EMPTY_REFINEMENT_TARGET_SET != SELECTABLE_TARGET
NO_UNRESOLVED_TARGET_IN_DECLARED_SET != COMPLETE_WORLD_COVERAGE
LOCAL_REFINEMENT_EXHAUSTED != REPRESENTATION_COMPLETE
NO_TARGET_SELECTED != SELECTOR_FAILURE
EMPTY_TARGET_SET != BOUNDED_SUFFICIENCY_WITHOUT_BASIS
```

Record local target-set exhaustion as a termination state relative to the
represented refinement target-set aperture and preserve material aperture /
representation limits. No target, completion or coverage primitive is added.

Recursion-entry budget use rule:

The declared recursion budget is non-negative. Before target discovery, expose
whether recursive refinement is prevented at entry by exhausted budget or by an
invalid negative budget. Skipping the loop is not evidence that no refinement
was needed.

```text
LOOP_NOT_ENTERED != RECURSION_COMPLETED
INITIAL_BUDGET_ZERO != NO_REFINEMENT_NEEDED
BUDGET_EXHAUSTED_AT_ENTRY != BOUNDED_SUFFICIENCY
NEGATIVE_TRACING_BUDGET != VALID_REMAINING_BUDGET
RECURSION_SKIPPED != COMPLETE_COVERAGE
```

A zero remaining budget records budget-exhausted termination and the resulting
recursive coverage limit. A negative remaining budget is outside the declared
domain and is preserved as an invalid limit state rather than treated as usable
budget. No new budget or termination primitive is added.

Let \(d_k^{rem}\ge0\) be remaining tracing budget and \(\operatorname{cost}_d(q_k)>0\) the declared cost of the next refinement.

\[
d_{k+1}^{rem}=
d_k^{rem}-\operatorname{cost}_d(q_k)
\]

Refinement-budget use rule:

The declared tracing cost of a selected refinement is load-bearing. The
operator must not silently replace `cost_d(q_k)` with a unit decrement.
Before recursion, bind the selected target to a supported refinement-cost claim,
compute the next remaining budget on the same declared budget basis, and recurse
only if the next budget is non-negative.

```text
DECLARED_REFINEMENT_COST != UNIT_COST
BUDGET_REMAINS != NEXT_REFINEMENT_AFFORDABLE
BUDGET_DECREMENT != RECURSION_DEPTH_DECREMENT
COST_UNKNOWN != COST_ONE
REFINEMENT_SELECTED != REFINEMENT_BUDGET_FEASIBLE
```

If the load-bearing refinement cost is `UNKNOWN`, do not default it to one.
Preserve budget feasibility as unresolved. If the declared cost exceeds the
remaining budget, record exhaustion/insufficiency and preserve the selected
material target as unresolved rather than executing an unaffordable refinement.
No budget, resource or cost primitive is added.

Refinement-cost domain use rule:

The formal recursion contract requires `cost_d(q_k) > 0`. Recording a cost does
not establish that it belongs to that domain. Before budget subtraction, reject
zero or negative refinement costs as invalid for this recursion budget.

```text
DECLARED_COST != VALID_POSITIVE_COST
ZERO_REFINEMENT_COST != FREE_UNBOUNDED_RECURSION
NEGATIVE_REFINEMENT_COST != BUDGET_CREDIT
COST_RECORDED != COST_DOMAIN_VALID
```

An invalid/nonpositive cost blocks this refinement path and remains visible as a
limit; it does not create free recursion or increase remaining budget. No new
primitive is added.

When \(d_{k+1}^{rem}\ge0\):

\[
(\mathcal R_{q_k},\mathcal L_{q_k})
=
\tau(
q_k,
\Pi_k,
\mathscr H_k,
d_{k+1}^{rem},
\mathfrak P_k
)
\]

\[
\mathcal R_{k+1}
=
\operatorname{merge}(
\mathcal R_k,
\mathcal R_{q_k}
)
\]

\[
\mathcal L_{k+1}
=
\operatorname{mergeLimits}(
\mathcal L_k,
\mathcal L_{q_k}
)
\]

Recursive integration carries qualifying limits with the graph contribution.
Where materially distinct child limits would collapse under deduplication,
preserve target/scope/provenance association.

```text
RECURSIVE_GRAPH_MERGE != RECURSIVE_LIMIT_MERGE
CHILD_GRAPH_VISIBLE != CHILD_LIMIT_VISIBLE
DEEPER_UNCERTAINTY != DISPENSABLE
GRAPH_CONTRIBUTION_SURVIVED != QUALIFYING_LIMIT_SURVIVED
CHILD_GRAPH_MERGED + CHILD_LIMIT_DROPPED != RECURSIVE_INTEGRATION
```

The notation \(\tau^k\) should not be used as ordinary function composition unless output and input types have been explicitly aligned. Recursion here means targeted refinement plus merge, not treating the previous packet as the world.

## [11.1] Scale invariants

At every useful scale ask:

```text
What boundary is being used?
What enters the aperture?
What remains outside it?
What state is changing?
What selects or contributes to the transition?
What is coupled?
Which clocks run?
Which future paths correspond, open, close, or harden?
Which routes remain usable?
Who or what carries burden?
What residue remains?
What is designation?
What is measure?
What was lost in abstraction?
```

## [11.2] Scale contradiction

A pattern can reverse under zoom.

```text
aggregate expansion + member contraction
local correction + stream persistence
entity stability + internal suppression
system efficiency + external burden transfer
```

Therefore:

\[
\operatorname{Result}^{(n)}
\nRightarrow
\operatorname{Result}^{(n+1)}
\]

Recursion termination use rule:

Stopping recursive differentiation is itself load-bearing when the termination
basis can change a downstream claim, coverage statement, correction-window
status, proposed transition or confidence/limits statement. A stop event must
therefore preserve, where available:

```text
refinement_stop_basis_claim_refs
refinement_stop_kind
refinement_stop_measure_ref
refinement_stop_limit_refs
refinement_stop_clock_refs
refinement_stop_route_or_handoff_refs
material_unresolved_at_stop_refs
```

Distinguish bounded sufficiency from truncation, exhaustion and handoff. If the
stopping basis is unsupported or the stop occurs because budget, access,
authority or time prevents further material refinement, preserve the remaining
material uncertainty/omissions rather than presenting termination as analytic
completion.

```text
STOPPED != COMPLETED
STOP_REASON_DECLARED != STOP_REASON_SUPPORTED
STOP_FOR_BOUNDED_SUFFICIENCY != STOP_FOR_RESOURCE_EXHAUSTION
STOP_FOR_HANDOFF != STOP_FOR_SUFFICIENCY
TERMINATION != COMPLETE_COVERAGE
BUDGET_EXHAUSTED != NO_MATERIAL_UNRESOLVED_TARGET
ACCESS_EXHAUSTED != QUESTION_RESOLVED
AUTHORITY_REACHED != ANALYSIS_COMPLETE
```

This uses existing CLAIM / LIMIT / APERTURE / CLOCK / ROUTE / designation /
measure machinery. No stop, termination or sufficiency primitive is added.

## [11.3] Recursion stop

TRACE is not infinite analysis.

Stop, preserve time, or hand off when one or more hold:

```text
new differentiation is no longer materially relevant under declared measure
remaining uncertainty cannot be reduced with available access
remaining tracing budget is exhausted
further tracing costs more than expected informational value under declared measure
an available reversible transition can preserve time for later tracing
an irreversible clock requires handoff to a connected brake or authority
available authority has been reached
```

Required depth may increase with irreversibility, affected scope, uncertainty, and transition velocity, but no universal scalar law is claimed.

A monotonicity claim is valid only inside a declared domain and comparison rule:

\[
D_{required}
=
f_{\theta}\big(
\operatorname{Irr},
\operatorname{Scope},
\operatorname{Unc},
\operatorname{Vel}
\big)
\]

with any claimed partial derivative or order relation stated explicitly rather than implied by arrows.

# [12] STRUCTURAL AWARENESS COMPARISON

Awareness is not token count, complexity, confidence, eloquence, consciousness, or a universal scalar.

Let the comparison context be:

\[
\theta=
\left\langle
J^*,
\delta,
\mu,
\mathcal E_{policy}
\right\rangle
\]

where \(J^*\) is the relevant criterion set and \(\mathcal E_{policy}\) states evidence and unresolved-comparison rules.

Criteria may include:

```text
A1  more material claims have explicit evidence state
A2  materially distinct states are less aliased
A3  causal and coupling paths are more explicit
A4  entity and scope boundaries are less hidden
A5  clocks and irreversibility are more visible
A6  available routes and transitions are more visible
A7  unknowns, access limits, and alternatives are more explicit
A8  unsupported certainty is not increased
A9  contradictions are preserved rather than silently merged
A10 self-limits and lack of authority are represented
A11 burden and residue are less likely to disappear from the map
A12 designation and measure are exposed
A13 absence claims are distinguished from non-observation
A14 streams are distinguished from isolated cases and from shared-intent claims
A15 packet use-state, selector ownership, and observable transition change are represented
```

For criterion \(j\):

\[
d_j^\theta(M_1,M_0)
\in
\{-1,0,+1,?\}
\]

```text
-1 = materially degraded
 0 = no material change shown
+1 = materially improved
 ? = comparison unresolved
```

Strict structural dominance:

\[
M_1\succ_{\mathcal A\mid\theta}M_0
\]

only when:

```text
for every j in J*: d_j is in {0,+1}
at least one j in J*: d_j = +1
no criterion in J* remains ?
evidence refs exist for every non-zero comparison
designation, measure, and comparison context are exposed
```

No-change under the declared criteria:

\[
M_1\equiv_{0,\mathcal A\mid\theta}M_0
\]

when every \(d_j^\theta=0\).

Weak dominance:

\[
M_1\succeq_{\mathcal A\mid\theta}M_0
\]

means either strict dominance or declared no-change.

`UNKNOWN` applies where any required comparison remains `?`. `INCOMPARABLE` applies where supported improvements and degradations coexist or the declared context supplies no common ordering.

Under fixed \(\theta\), weak dominance is a preorder only if the criterion comparisons are reflexive and transitive. If that preorder exists, its induced equivalence is mutual weak dominance:

\[
M_1\approx_{\theta}M_0
\iff
\left(
M_1\succeq_{\mathcal A\mid\theta}M_0
\land
M_0\succeq_{\mathcal A\mid\theta}M_1
\right)
\]

The quotient by \(\approx_\theta\) is a partial order only when the usual preorder conditions hold. Across changing criteria, designation, measures, or evidence rules, no global partial order is claimed.

Awareness increase is not guaranteed by applying TRACE:

\[
\operatorname{complexity}(M_1)>
\operatorname{complexity}(M_0)
\nRightarrow
M_1\succ_{\mathcal A\mid\theta}M_0
\]

Lower confidence can coexist with strict structural dominance if unsupported certainty was removed.

```yaml
awareness_comparison:
  map_0_ref: ""
  map_1_ref: ""
  context_ref: ""
  relevant_criteria: []
  comparisons:
    - criterion: "A1"
      result: "-1|0|+1|?"
      evidence_claim_refs: []
      veto_relevant: false
  designation_ref: ""
  measure_ref: ""
  relation: "STRICTLY_DOMINATES|WEAKLY_DOMINATES|EQUIVALENT|INCOMPARABLE|UNKNOWN"
```

This is a proposed comparison discipline, not a validated measure of consciousness or understanding.

A TRACE transformation fails when it creates structure unsupported by evidence, erases live alternatives, hides designation or measure, converts uncertainty into decorative notation, lets uncertainty silently select action or delay, promotes urgency or hardening into unsupported irreversibility, substitutes population recovery for individual repair, or silently crosses from structure into value, domain tactics, selection, or actuation.

# [13] TRACE OPERATOR

## [13.1] Abstract form

\[
\tau:
(X,\Pi,\mathscr H,d,\mathfrak P)
\rightarrow
(\mathcal R,\mathcal L)
\]

- \(X\) = input scene or claim set
- \(\Pi\) = available aperture
- \(\mathscr H\) = retained history
- \(d\) = recursion/depth budget
- \(\mathfrak P\) = declared primitive aperture
- \(\mathcal R\) = canonical typed graph
- \(\mathcal L\) = limits, unresolved questions, omitted categories, and unavailable capabilities

## [13.2] Pseudocode

```text
TRACE(X, aperture, history, depth_budget, primitive_aperture):

    R <- initialise_TRACE_GRAPH_0_3_0()
    L <- {}

    record_input(R, X)
    record_receiver_aperture(R, aperture)
    record_primitive_aperture(R, primitive_aperture)
    record_representation_formation_and_ingress(R, X, aperture)

    type_claims(R)
    attach_provenance(R)
    separate_evidence_state_from_access_state(R)
    classify_claim_kind(R)
    expose_unknown_context_and_contamination(R)
    apply_dependency_relative_currentness(R)

    identify_provisional_entities(R)
    record_boundary_alternatives(R)
    record_scope_levels_and_cross_scale_limits(R)
    map_states_and_transitions(R)
    enforce_action_wait_delay_inaction_symmetry(R)
    attribute_selection_to_selector_policy_or_default(R)
    separate_strategy_revisability_from_transition_reversibility(R)
    map_absence_claims(R)
    aggregate_streams_and_candidate_patterns(R)
    map_apertures_and_blindspots(R)
    record_target_set_apertures_and_alternatives(R)
    challenge_representation_boundary_where_load_bearing(R)
    separate_information_presence_from_search_coverage(R)
    map_couplings_dependencies_and_control(R)
    map_clocks_authorship_and_hardening(R)
    type_planning_detection_retention_hardening_and_irreversibility_clocks(R)
    reject_unsupported_irreversibility_promotion(R)
    map_future_space_changes_by_scope(R)
    require_future_path_correspondence_for_cross_time_claims(R)
    map_routes_and_route_usability(R)
    map_burden_residue_memory_and_custody(R)
    map_custody_holder_risk_and_safe_copy(R)
    expose_operator_evidence_holder_and_verifier_overlap(R)
    expose_residue_ordering(R)
    expose_designation_and_measure(R)
    expose_TRACE_value_domain_selector_actuator_handoffs(R)
    preserve_divergent_readings_without_authority_inheritance(R)
    expose_declared_contest_routes_without_inferring_effectiveness(R)
    expose_selector_carrier_enforcement_and_brake_ports(R)

    apply_representation_independent_firing(R)
    test_load_bearing_verification_discrimination(R)
    build_bound_correction_window_views_where_required(R)
    preserve_liveness_loss_without_assigning_cause(R)

    generate_live_alternative_readings(R)
    test_internal_contradictions(R)
    record_reader_limits(L)

    if depth_budget < 0:
        record_invalid_negative_tracing_budget(R, L, depth_budget)
        preserve_recursive_coverage_limit_due_to_invalid_budget(R, L)
        depth_budget <- 0
    elif depth_budget == 0:
        record_budget_exhausted_at_recursion_entry(R, L, depth_budget)
        preserve_recursive_coverage_limit_due_to_budget(R, L)

    while depth_budget remains:
        candidates <- unresolved_refinement_targets(R)
        record_refinement_target_set_aperture(R, candidates)
        if candidates is empty:
            record_empty_refinement_target_set_termination(R, L, candidates)
            preserve_coverage_relative_to_refinement_target_set_aperture(R, L, candidates)
            break
        target, refinement_basis <- select_refinement_target(
            candidates, declared_designation(R), declared_measure(R), depth_budget)
        record_refinement_selection_basis_and_budget_omissions(
            R, L, candidates, target, refinement_basis, depth_budget)
        if refinement_basis is UNKNOWN and
           unselected_candidate_could_materially_change_load_bearing_output(R, candidates, target):
            preserve_refinement_selection_uncertainty(R, L)
        stop, stop_basis <- evaluate_refinement_stop_condition(
            target, R, L, declared_designation(R), declared_measure(R))
        if stop:
            record_refinement_stop_basis_and_limits(R, L, target, stop_basis)
            if not supported_bounded_sufficiency(stop_basis):
                preserve_material_unresolved_after_truncation_or_handoff(
                    R, L, candidates, target, stop_basis)
            break
        refinement_cost <- declared_refinement_cost(target, R, L)
        if refinement_cost is UNKNOWN:
            preserve_unknown_refinement_cost_and_budget_feasibility(R, L, target)
            break
        if refinement_cost <= 0:
            record_invalid_nonpositive_refinement_cost(R, L, target, refinement_cost)
            preserve_material_unresolved_after_invalid_refinement_cost(R, L, target)
            break
        next_depth_budget <- depth_budget - refinement_cost
        if next_depth_budget < 0:
            record_budget_exhaustion_before_refinement(
                R, L, target, depth_budget, refinement_cost)
            preserve_material_unresolved_after_budget_exhaustion(R, L, target)
            break
        child_R, child_L <- TRACE(target, aperture, history,
                                  next_depth_budget, primitive_aperture)
        R <- merge_graphs(R, child_R)
        L <- merge_limits_with_recursive_provenance(L, child_L, target)

    state_transition_and_coverage_results_relative_to_declared_apertures(R)
    emit_available_transitions_without_selecting(R)
    emit_commitment_receipt_if_external_selector_proceeds(R)
    emit_packet_use_state(R)
    material_limit_refs <- serialize_load_bearing_limits_with_provenance(R, L)
    bind_packet_limit_refs(R, material_limit_refs)
    emit_confidence_and_limits(R, L, material_limit_refs)
    validate_schema(R, "TRACE-GRAPH-0.3.0")

    return R, L
```

## [13.3] Non-command output

TRACE may expose:

```text
available transition
lower-irreversibility transition relative to a declared reversibility measure
reversible holding transition
information-seeking transition
route-building transition
pause transition
rollback transition
record-preservation transition
no-action transition and its trajectory
```

It does not convert those into obligation without an external value/policy layer.

## [13.4] Parsability ceiling

```text
SERIALIZABLE != SELF_EXECUTING
PARSABLE != CORRECTLY_INSTANTIATED
SCHEMA_VALID != WORLD_VALID
```

The grammar fixes identifiers, types, edges, ports, and provenance. It does not provide universal functions for discovering entities, estimating clocks, detecting deception, measuring future-space, or selecting action.

---

# [14] CANONICAL TRACE GRAPH PACKET

**Local claim ceiling:** voluntary structural reading only. Not truth, clearance, authority, compliance, ethical approval, or operational command.

The graph below is canonical. Any prose report, table, dashboard, verdict, or summary is a derived view and MUST reference this graph rather than silently replacing it.

```yaml
trace_graph:
  schema: "TRACE-GRAPH-0.3.0"
  trace_version: "0.3.0"
  reading_id: ""
  scope: ""
  timestamp: ""

  claim_ceiling:
    voluntary_reference: true
    not_truth: true
    not_permission: true
    not_clearance: true
    not_compliance: true
    not_operational_command: true

  receiver:
    node_ref: "n_receiver"
    type: "UNKNOWN"
    available_capabilities: []
    unavailable_capabilities: []
    prohibited_capabilities: []
    persistence: "UNKNOWN"
    action_authority: "UNKNOWN"

  input:
    raw: ""
    source_refs: []
    requested_action_ref: ""
    projected_transition_ref: ""
    reported_confidence_claim_ref: ""
    deadline_clock_ref: ""

  primitive_aperture:
    selected_node_types: []
    selected_edge_types: []
    omitted_known_types: []
    selection_basis: []
    alternative_primitive_sets: []
    primitive_choice_advantage_claim_refs: []
    known_unrepresentable_structure: []

  nodes:
    - id: "n_receiver"
      type: "ENTITY"
      attributes:
        boundary_status: "PROVISIONAL"
        persistence_status: "UNKNOWN"
        selection_status: "UNKNOWN"
        agency_status: "UNKNOWN"
        experience_status: "UNKNOWN"
        continuity_status: "UNKNOWN"
      claim_refs: []

  edges: []

  claims:
    - id: "c_placeholder"
      proposition: ""
      claim_kind: "STATUS"
      evidence_state: "U"
      access_state: "A"
      source_refs: []
      provenance_edge_refs: []
      timestamp: ""
      confidence:
        representation: "UNKNOWN"
        value: null
      alternative_hypothesis_refs: []
      unknown_context:
        contamination_state: "UNKNOWN"
        evidence_controlled_by_refs: []
        clock_controlled_by_refs: []
        delay_advantage_claim_refs: []
        delay_cost_carrier_refs: []
        resolution_owner_refs: []
        resolution_deadline_refs: []
        available_pause_or_protection_refs: []
        earlier_options_before_urgency_refs: []

  ports:
    designation:
      node_ref: ""
      supplied: []
      inferred: []
      protected: []
      excluded: []
      disputed: []
      uncertain: []
      unknown: []
      boundary_choice_advantage_claim_refs: []

    measure:
      node_ref: ""
      supplied: []
      inferred: []
      alternatives: []
      uncertainty: []
      sensitivity: []
      measure_choice_advantage_claim_refs: []
      unrepresented_dimensions: []

    selector:
      node_ref: ""
      owner_refs: []
      candidate_action_refs: []
      candidate_transition_refs: []
      selected_action_ref: ""
      selected_transition_ref: ""
      selection_policy_refs: []
      selection_state: "UNKNOWN"
      transition_symmetry_required: true
      unrepresented_transition_classes: []
      unavailability_reason_claim_refs: []

    carrier:
      node_ref: ""
      state: "UNKNOWN"
      weight_types: []
      owner_refs: []
      persistence_mechanisms: []
      external_to_challenged_actor: "UNKNOWN"

    enforcement:
      node_ref: ""
      state: "UNKNOWN"
      authority_refs: []
      independence_status: "UNKNOWN"

    brake:
      node_ref: ""
      state: "UNKNOWN"
      candidate_transition_ref: ""
      reading_ref: ""
      external_policy_ref: ""
      authority_ref: ""
      independence_status: "UNKNOWN"
      trigger_state: "UNKNOWN"
      latency_bound: "UNKNOWN"
      commitment_deadline: "UNKNOWN"
      result: "UNKNOWN"
      activation_record_ref: ""
      failure_record_ref: ""

  discipline:
    transition_set:
      action_or_intervention_refs: []
      information_refs: []
      wait_delay_inaction_refs: []
      unrepresented_transition_classes: []
      unavailability_reason_claim_refs: []
      uncertainty_selects_transition: false
    clock_typing:
      planning_refs: []
      detection_refs: []
      evidence_hardening_refs: []
      irreversibility_refs: []
      unsupported_irreversibility_claim_refs: []
      deadline_entails_irreversibility: false
      hardening_entails_irreversibility: false
    scope_granularity:
      individual_refs: []
      group_refs: []
      population_refs: []
      ecosystem_refs: []
      cross_scale_substitution_claim_refs: []
      aggregate_recovery_repairs_individual_loss: false
    layer_handoff:
      trace_structure_refs: []
      value_input_refs: []
      domain_input_refs: []
      selector_refs: []
      actuator_refs: []
      unresolved_handoffs: []
    evidence_custody:
      operator_refs: []
      evidence_holder_refs: []
      verifier_refs: []
      independent_verifier_refs: []
      self_verification_status: "UNKNOWN"
      control_alone_establishes_deception: false

  indexes:
    entity_refs: []
    state_refs: []
    transition_refs: []
    aperture_refs: []
    coupling_refs: []
    clock_refs: []
    future_path_refs: []
    route_refs: []
    burden_refs: []
    residue_refs: []
    record_refs: []
    absence_refs: []
    stream_refs: []
    pattern_refs: []
    alternative_reading_refs: []
    available_transition_refs: []

  absence_analysis:
    absence_refs: []
    comparison_basis_refs: []
    detector_required_refs: []
    alternative_explanations: []

  stream_pattern_analysis:
    stream_refs: []
    pattern_refs: []
    local_correction_refs: []
    repeated_mechanism_refs: []
    mechanism_change_evidence_refs: []

  record_custody:
    record_refs: []
    holder_risk_claim_refs: []
    disclosure_cost_claim_refs: []
    retaliation_risk_claim_refs: []
    safe_copy_refs: []
    integrity_check_refs: []
    integrity_check_limits: []

  repair_ordering:
    residue_refs: []
    ordering_rule_ref: ""
    ordered_by_refs: []
    contested_by_refs: []
    visibility_state: "UNKNOWN"
    hidden_allocation_risk: "UNKNOWN"

  commitment_receipts:
    - record_ref: ""
      selected_transition_ref: ""
      unresolved_claim_refs: []
      live_alternative_transition_refs: []
      declared_value_basis_refs: []
      foreclosed_future_path_refs: []
      expected_residue_refs: []
      reason_for_commitment_claim_refs: []
      review_debt_refs: []
      unknown_contamination_claim_refs: []
      receipt_is_not_clearance: true

  awareness_comparison:
    map_0_ref: ""
    map_1_ref: ""
    relevant_criteria: []
    comparisons: []
    designation_ref: ""
    measure_ref: ""
    relation: "UNKNOWN"

  available_transition_refs: []

  institutional_use:
    packet_owner_refs: []
    selector_owner_refs: []
    brake_owner_refs: []
    independent_verifier_refs: []
    packet_cited_as_diligence: "UNKNOWN"
    packet_cited_as_authority: "UNKNOWN"
    observable_transition_change: "UNKNOWN"
    mechanism_change_for_next_case: "UNKNOWN"
    use_evidence_claim_refs: []

  limits:
    receiver_limits: []
    unavailable_evidence: []
    unresolved_claim_refs: []
    omitted_primitive_effects: []
    limit_refs: []

  anti_clearance:
    voluntary_use_only: true
    reading_is_not_truth: true
    reading_is_not_permission: true
    reading_is_not_compliance: true
    packet_completion_is_not_correction: true
    schema_validity_is_not_world_validity: true
    packet_citation_is_not_transition_change: true
    commitment_receipt_is_not_clearance: true
    hash_match_is_not_truth: true
```


### [14.0.1] Canonical existing-object target-set aperture profile

A target-set aperture is serialized with existing graph objects. This profile is canonical for interoperability but is not a new primitive, node type, edge type, port, or required minimum-schema field.

```yaml
nodes:
  - id: "ap_target_set_primary"
    type: "APERTURE"
    attributes:
      aperture_kind: "TARGET_SET"
      source_ref: "n_operator"
      target_refs: ["n_scope_reported"]
      selection_basis_claim_refs: ["c_target_basis"]
      known_omitted_target_categories: ["unreported affected scopes"]
      alternative_target_set_refs: ["ap_target_set_alternative"]
      control_or_custody_refs: ["n_operator"]
      uncertainty_claim_refs: ["c_target_uncertainty"]
    claim_refs: ["c_target_aperture_status"]

  - id: "ap_target_set_alternative"
    type: "APERTURE"
    attributes:
      aperture_kind: "TARGET_SET"
      source_ref: "n_independent_reviewer"
      target_refs: ["n_scope_reported", "n_scope_unreported"]
      selection_basis_claim_refs: ["c_alternative_basis"]
      known_omitted_target_categories: []
      alternative_target_set_refs: ["ap_target_set_primary"]
      control_or_custody_refs: ["n_independent_reviewer"]
      uncertainty_claim_refs: ["c_alternative_uncertainty"]
    claim_refs: ["c_alternative_aperture_status"]

edges:
  - id: "e_primary_bounds_reported"
    type: "BOUNDS"
    source: "ap_target_set_primary"
    target: "n_scope_reported"
    claim_refs: ["c_target_basis"]

  - id: "e_primary_omits_unreported"
    type: "OMITS"
    source: "ap_target_set_primary"
    target: "n_scope_unreported"
    claim_refs: ["c_target_uncertainty"]

  - id: "e_alternative_disputes_primary"
    type: "DISPUTES"
    source: "ap_target_set_alternative"
    target: "ap_target_set_primary"
    claim_refs: ["c_alternative_basis"]

claims:
  - id: "c_target_basis"
    proposition: "The primary review targets scopes supplied by the operator."
    evidence_state: "R"
    access_state: "A"

  - id: "c_target_uncertainty"
    proposition: "Materially affected scopes may exist outside the supplied target set."
    evidence_state: "U"
    access_state: "A"
```

```text
TARGET_SET_PROFILE_PRESENT != TARGET_SET_COMPLETE
PROFILE_CONFORMANCE != TARGET_DISCOVERY
ALTERNATIVE_TARGET_SET_RECORDED != ALTERNATIVE_TARGET_SET_AUTHORITATIVE
```

## [14.1] Binding rules

```text
Every node and edge has a stable id.
Every material assertion is a canonical claim or references one. Every CLAIM node binds to exactly one canonical claim id.
Every value-bearing label references designation and measure ports.
Every available transition is a TRANSITION node.
Every clock is a CLOCK node.
Every future path binds to at least one scope/entity reference.
Every brake result references an external policy and authority or remains UNKNOWN.
Every derived view declares its source reading_id.
Every ABSENCE node declares its comparison basis and evidence state.
Every PATTERN node declares member transitions, counterexamples, and mechanism-change evidence.
Every `UNKNOWN` with material asymmetry records its unknown_context.
Every commitment under unresolved claims emits a commitment receipt.
Every custody integrity check declares what it can and cannot establish.
```


```text
Every material search-coverage claim references a target-set aperture, selected target refs, and a declared reachability or unavailability basis.
Every claim that a target set is complete remains UNKNOWN unless completeness is independently bounded by a declared world model and evidence aperture.
Every selection after divergent readings references a selector, authority basis, policy/value basis, handoff route, and unresolved handoff status.
Every claim of contestability references the challenging reading, contest route, bound brake, capture/independence status, and relevant clocks where available.
Every brake or correction claim distinguishes declaration, activation attempt, observable interruption, correction completion, and residue.
```

These remain checker-external because the embedded minimum validator cannot establish semantic relevance, completeness, route executability, authority legitimacy or world effect.

Except for the `CLAIM`-node one-reference cardinality rule, these rules are checker-external. The embedded validator otherwise enforces packet shape and controlled vocabulary, not reference integrity, completeness, independence, or world correspondence.


Additional v0.3 checker-external binding/use rules:

```text
MINIMUM_SCHEMA_PASS != SEMANTIC_BINDING_PASS
SEMANTIC_BINDING_PASS != WORLD_TRUTH
```

Before a load-bearing packet field or derived view settles a route,
currentness, independence, completeness, verification, correction-window,
comparison, selection or proposed-transition claim, apply the relevant
representation-independent firing, ingress/admission, currentness, instrument
discrimination, route-usability and measure/boundary rules.

These are semantic use rules. They do not add required minimum-schema fields.

### [14.1.1] Load-bearing limit carrier survival

If an item in `L` is load-bearing because losing its kind, target/scope, basis
or provenance could change a downstream claim, coverage/window/transition view,
confidence statement or correction/repair route, canonical packet emission must
carry that distinction rather than summarize it away.

Use the existing `LIMIT` node type and stable node identity. Its existing open
attributes may carry, where available:

```text
limit_kind
description
target_refs
scope_refs
basis_claim_refs
aperture_refs
clock_refs
route_or_handoff_refs
recursive_parent_target_ref
source_limit_refs
```

The packet `limits` object may expose optional `limit_refs` pointing to those
carried `LIMIT` node ids. Derived confidence, coverage, correction-window and
transition views may reference the same carried limit ids. Missing or unsupported
fields remain unresolved; do not invent provenance merely to fill the profile.

Do not deduplicate materially distinct limits merely because their prose summary
or unresolved-claim set is identical. If limit kind/provenance changes the next
repair route, that distinction is load-bearing and must survive the carrier.

```text
CAN_SERIALIZE_LIMIT_DETAIL != LIMIT_DETAIL_SURVIVED
LIMIT_VISIBLE_IN_ANALYSIS != LIMIT_CARRIED_IN_PACKET
UNRESOLVED_CLAIM_RECORDED != LIMIT_CAUSE_RECORDED
LIMIT_TEXT_PRESENT != LIMIT_PROVENANCE_PRESERVED
SCHEMA_VALID_LIMITS != SEMANTIC_LIMIT_SURVIVAL
INTERNAL_L_MERGED != CANONICAL_PACKET_L_CARRIED
MINIMUM_SCHEMA_PASS != SEMANTIC_LIMIT_SURVIVAL
```

This is an existing-object serialization/binding profile, not a new primitive
and not a required minimum-schema expansion.

## [14.2] Packet-use boundary

TRACE can represent procedural theatre. TRACE cannot prevent an actor from using TRACE as procedural theatre.

```text
PACKET_COMPLETED != DILIGENCE_ESTABLISHED
PACKET_CITED != MECHANISM_CHANGED
SELF_REPORTED_BRAKE != INDEPENDENT_BRAKE
```

---



```text
TARGET_SET_RECORDED != TARGET_SET_COMPLETE
COVERAGE_CHECK_PASSED != DILIGENCE_ESTABLISHED
AUTHORITY_HANDOFF_RECORDED != AUTHORITY_LEGITIMATED
CONTEST_ROUTE_RECORDED != CONTEST_SUCCEEDED
BRAKE_ACTIVATION_RECORDED != TRANSITION_INTERRUPTED
TRANSITION_INTERRUPTED != HARM_PREVENTED
```

## [14.3] Unresolved commitment receipt

TRACE does not decide whether a transition may proceed. When an external selector commits while material claims remain `UNKNOWN` or `DISPUTED`, while a correction window is `UNKNOWN` or `CLOSED`, or while an independent brake is absent, the reading should preserve the commitment conditions.

\[
\mathcal D_c=
\langle
a^*,
U^*,
D^*,
\mathbb A_{live},
\delta,
\mu,
\mathcal F_{foreclosed},
\Lambda_{expected},
\mathfrak d_{review}
\rangle
\]

```text
selected action and projected transition
unresolved claims
disputed claims
alternatives still live at commitment
declared value/policy basis
future paths foreclosed
expected residue
reason given for commitment
review debt
unknown-contamination flags
```

```text
COMMITMENT_RECEIPT != CLEARANCE
RECORDED_REASON != JUSTIFIED_REASON
PROCEEDED != RESOLVED
```

The receipt prevents later compression of “selected under unresolved conditions” into “TRACE approved.”

## [14.4] Minimum validator contract

The embedded schema validates packet shape and controlled vocabularies. It cannot validate truth, completeness, independence, value choice, world correspondence, or operational connection.


The v0.3.0 identifier marks this generated full working candidate. Its embedded minimum-schema shape remains identical to released v0.2.7 after version normalization. That compatibility does not imply that the minimum validator can enforce the v0.3 checker-external semantic bindings, target discovery, target-set adequacy, search coverage, authority legitimacy, route execution, brake effectiveness, correction, or world correspondence.

A v0.2.7 packet is not silently relabelled as v0.3.0. Structural compatibility does not erase packet identity or the semantic contract under which the packet was produced.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:trace:graph:0.3.0",
  "title": "TRACE-GRAPH-0.3.0 minimum validator",
  "type": "object",
  "required": [
    "trace_graph"
  ],
  "properties": {
    "trace_graph": {
      "type": "object",
      "required": [
        "schema",
        "trace_version",
        "reading_id",
        "nodes",
        "edges",
        "claims",
        "ports",
        "discipline",
        "available_transition_refs",
        "institutional_use",
        "limits",
        "anti_clearance"
      ],
      "properties": {
        "schema": {
          "const": "TRACE-GRAPH-0.3.0"
        },
        "trace_version": {
          "const": "0.3.0"
        },
        "reading_id": {
          "type": "string",
          "minLength": 1
        },
        "nodes": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/node"
          }
        },
        "edges": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/edge"
          }
        },
        "claims": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/claim"
          }
        },
        "ports": {
          "type": "object",
          "required": [
            "designation",
            "measure",
            "selector",
            "carrier",
            "enforcement",
            "brake"
          ],
          "properties": {
            "designation": {
              "type": "object"
            },
            "measure": {
              "type": "object"
            },
            "selector": {
              "type": "object",
              "properties": {
                "selection_state": {
                  "type": "string"
                }
              },
              "additionalProperties": true
            },
            "carrier": {
              "type": "object",
              "properties": {
                "state": {
                  "enum": [
                    "NONE",
                    "INTERNAL",
                    "EXTERNAL",
                    "MIXED",
                    "UNKNOWN"
                  ]
                },
                "weight_types": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                }
              },
              "additionalProperties": true
            },
            "enforcement": {
              "type": "object",
              "properties": {
                "state": {
                  "enum": [
                    "PRESENT",
                    "ABSENT",
                    "UNKNOWN"
                  ]
                }
              },
              "additionalProperties": true
            },
            "brake": {
              "type": "object",
              "properties": {
                "state": {
                  "enum": [
                    "INDEPENDENT_TESTED",
                    "PRESENT_UNTESTED",
                    "PRESENT_CAPTURED",
                    "ABSENT",
                    "UNKNOWN"
                  ]
                }
              },
              "additionalProperties": true
            }
          },
          "additionalProperties": true
        },
        "discipline": {
          "type": "object",
          "required": [
            "transition_set",
            "clock_typing",
            "scope_granularity",
            "layer_handoff",
            "evidence_custody"
          ],
          "properties": {
            "transition_set": {
              "type": "object",
              "required": [
                "action_or_intervention_refs",
                "information_refs",
                "wait_delay_inaction_refs",
                "unrepresented_transition_classes",
                "unavailability_reason_claim_refs",
                "uncertainty_selects_transition"
              ],
              "properties": {
                "action_or_intervention_refs": {
                  "type": "array",
                  "items": { "type": "string" }
                },
                "information_refs": {
                  "type": "array",
                  "items": { "type": "string" }
                },
                "wait_delay_inaction_refs": {
                  "type": "array",
                  "items": { "type": "string" }
                },
                "unrepresented_transition_classes": {
                  "type": "array",
                  "items": { "type": "string" }
                },
                "unavailability_reason_claim_refs": {
                  "type": "array",
                  "items": { "type": "string" }
                },
                "uncertainty_selects_transition": { "const": false }
              },
              "additionalProperties": false
            },
            "clock_typing": {
              "type": "object",
              "required": [
                "planning_refs",
                "detection_refs",
                "evidence_hardening_refs",
                "irreversibility_refs",
                "unsupported_irreversibility_claim_refs",
                "deadline_entails_irreversibility",
                "hardening_entails_irreversibility"
              ],
              "properties": {
                "planning_refs": { "type": "array", "items": { "type": "string" } },
                "detection_refs": { "type": "array", "items": { "type": "string" } },
                "evidence_hardening_refs": { "type": "array", "items": { "type": "string" } },
                "irreversibility_refs": { "type": "array", "items": { "type": "string" } },
                "unsupported_irreversibility_claim_refs": { "type": "array", "items": { "type": "string" } },
                "deadline_entails_irreversibility": { "const": false },
                "hardening_entails_irreversibility": { "const": false }
              },
              "additionalProperties": false
            },
            "scope_granularity": {
              "type": "object",
              "required": [
                "individual_refs",
                "group_refs",
                "population_refs",
                "ecosystem_refs",
                "cross_scale_substitution_claim_refs",
                "aggregate_recovery_repairs_individual_loss"
              ],
              "properties": {
                "individual_refs": { "type": "array", "items": { "type": "string" } },
                "group_refs": { "type": "array", "items": { "type": "string" } },
                "population_refs": { "type": "array", "items": { "type": "string" } },
                "ecosystem_refs": { "type": "array", "items": { "type": "string" } },
                "cross_scale_substitution_claim_refs": { "type": "array", "items": { "type": "string" } },
                "aggregate_recovery_repairs_individual_loss": { "const": false }
              },
              "additionalProperties": false
            },
            "layer_handoff": {
              "type": "object",
              "required": [
                "trace_structure_refs",
                "value_input_refs",
                "domain_input_refs",
                "selector_refs",
                "actuator_refs",
                "unresolved_handoffs"
              ],
              "properties": {
                "trace_structure_refs": { "type": "array", "items": { "type": "string" } },
                "value_input_refs": { "type": "array", "items": { "type": "string" } },
                "domain_input_refs": { "type": "array", "items": { "type": "string" } },
                "selector_refs": { "type": "array", "items": { "type": "string" } },
                "actuator_refs": { "type": "array", "items": { "type": "string" } },
                "unresolved_handoffs": { "type": "array", "items": { "type": "string" } }
              },
              "additionalProperties": false
            },
            "evidence_custody": {
              "type": "object",
              "required": [
                "operator_refs",
                "evidence_holder_refs",
                "verifier_refs",
                "independent_verifier_refs",
                "self_verification_status",
                "control_alone_establishes_deception"
              ],
              "properties": {
                "operator_refs": { "type": "array", "items": { "type": "string" } },
                "evidence_holder_refs": { "type": "array", "items": { "type": "string" } },
                "verifier_refs": { "type": "array", "items": { "type": "string" } },
                "independent_verifier_refs": { "type": "array", "items": { "type": "string" } },
                "self_verification_status": { "enum": ["PRESENT", "ABSENT", "UNKNOWN"] },
                "control_alone_establishes_deception": { "const": false }
              },
              "additionalProperties": false
            }
          },
          "additionalProperties": false
        },
        "available_transition_refs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "institutional_use": {
          "type": "object",
          "properties": {
            "packet_cited_as_diligence": {
              "enum": ["YES", "NO", "UNKNOWN"]
            },
            "packet_cited_as_authority": {
              "enum": ["YES", "NO", "UNKNOWN"]
            },
            "observable_transition_change": {
              "enum": ["YES", "NO", "UNKNOWN"]
            },
            "mechanism_change_for_next_case": {
              "enum": ["YES", "NO", "UNKNOWN"]
            }
          },
          "additionalProperties": true
        },
        "limits": {
          "type": "object",
          "properties": {
            "receiver_limits": {
              "type": "array"
            },
            "unavailable_evidence": {
              "type": "array"
            },
            "unresolved_claim_refs": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "omitted_primitive_effects": {
              "type": "array"
            }
          },
          "additionalProperties": true
        },
        "anti_clearance": {
          "type": "object",
          "required": [
            "voluntary_use_only",
            "reading_is_not_truth",
            "reading_is_not_permission",
            "packet_completion_is_not_correction"
          ],
          "properties": {
            "voluntary_use_only": {
              "const": true
            },
            "reading_is_not_truth": {
              "const": true
            },
            "reading_is_not_permission": {
              "const": true
            },
            "packet_completion_is_not_correction": {
              "const": true
            }
          },
          "additionalProperties": true
        },
        "commitment_receipts": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "selected_transition_ref": {
                "type": "string"
              },
              "unresolved_claim_refs": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "receipt_is_not_clearance": {
                "const": true
              }
            },
            "required": [
              "receipt_is_not_clearance"
            ],
            "additionalProperties": true
          }
        },
        "awareness_comparison": {
          "type": "object",
          "properties": {
            "map_0_ref": {
              "type": "string"
            },
            "map_1_ref": {
              "type": "string"
            },
            "relevant_criteria": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "comparisons": {
              "type": "array",
              "items": {
                "type": "object"
              }
            },
            "designation_ref": {
              "type": "string"
            },
            "measure_ref": {
              "type": "string"
            },
            "relation": {
              "enum": [
                "STRICTLY_DOMINATES",
                "WEAKLY_DOMINATES",
                "EQUIVALENT",
                "INCOMPARABLE",
                "UNKNOWN"
              ]
            }
          },
          "additionalProperties": true
        }
      },
      "additionalProperties": true
    }
  },
  "$defs": {
    "node": {
      "type": "object",
      "required": [
        "id",
        "type",
        "attributes",
        "claim_refs"
      ],
      "properties": {
        "id": {
          "type": "string",
          "pattern": "^n_[A-Za-z0-9_.:-]+$"
        },
        "type": {
          "enum": [
            "SCENE",
            "MAP",
            "ENTITY",
            "STATE",
            "SIGNAL",
            "CLAIM",
            "APERTURE",
            "ACTION",
            "TRANSITION",
            "COUPLING",
            "CLOCK",
            "FUTURE_PATH",
            "ROUTE",
            "BURDEN",
            "RESIDUE",
            "RECORD",
            "ABSENCE",
            "STREAM",
            "PATTERN",
            "DESIGNATION",
            "MEASURE",
            "SELECTOR",
            "POLICY",
            "CARRIER",
            "ENFORCER",
            "BRAKE",
            "LIMIT"
          ]
        },
        "attributes": {
          "type": "object"
        },
        "claim_refs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "allOf": [
        {
          "if": {
            "properties": {
              "type": {
                "const": "CLAIM"
              }
            },
            "required": ["type"]
          },
          "then": {
            "properties": {
              "claim_refs": {
                "minItems": 1,
                "maxItems": 1
              }
            }
          }
        }
      ],
      "additionalProperties": false
    },
    "edge": {
      "type": "object",
      "required": [
        "id",
        "type",
        "from",
        "to",
        "directed",
        "attributes",
        "claim_refs"
      ],
      "properties": {
        "id": {
          "type": "string",
          "pattern": "^e_[A-Za-z0-9_.:-]+$"
        },
        "type": {
          "enum": [
            "REPRESENTS",
            "OBSERVES",
            "REPORTS",
            "INFERS",
            "DISPUTES",
            "CANNOT_ACCESS",
            "OMITS",
            "BOUNDS",
            "CONTAINS",
            "PERSISTS_AS",
            "INSTANCE_OF",
            "AGGREGATES",
            "RECURS_AS",
            "TRANSITIONS_TO",
            "CAUSES",
            "CONTRIBUTES_TO",
            "COUPLES",
            "DEPENDS_ON",
            "CONTROLS",
            "CONSTRAINS",
            "ADVANTAGES_UNDER_MEASURE",
            "BURDENS",
            "OPENS",
            "PRESERVES",
            "CLOSES",
            "HARDENS",
            "FORECLOSES",
            "ROUTES_TO",
            "CAN_CORRECT",
            "LEAVES_RESIDUE",
            "RECORDS",
            "ALTERS_RECORD",
            "DESIGNATES",
            "MEASURES",
            "SELECTS",
            "CARRIES",
            "ENFORCES",
            "BRAKES",
            "INTERRUPTS",
            "EXCLUDES",
            "INHERITS",
            "CITES_AS_AUTHORITY",
            "CITES_AS_DILIGENCE",
            "VERIFIES",
            "ACTIVATES",
            "FAILS_TO_ACTIVATE"
          ]
        },
        "from": {
          "type": "string"
        },
        "to": {
          "type": "string"
        },
        "directed": {
          "type": "boolean"
        },
        "attributes": {
          "type": "object"
        },
        "claim_refs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "allOf": [
        {
          "if": {
            "properties": {
              "type": {
                "const": "ALTERS_RECORD"
              }
            },
            "required": ["type"]
          },
          "then": {
            "properties": {
              "attributes": {
                "type": "object",
                "required": ["alteration_kind"],
                "properties": {
                  "alteration_kind": {
                    "enum": ["MODIFY", "REDACT", "OVERWRITE", "DELETE", "ROTATE"]
                  }
                }
              }
            }
          }
        }
      ],
      "additionalProperties": false
    },
    "claim": {
      "type": "object",
      "required": [
        "id",
        "proposition",
        "claim_kind",
        "evidence_state",
        "access_state",
        "source_refs",
        "timestamp",
        "confidence"
      ],
      "properties": {
        "id": {
          "type": "string",
          "pattern": "^c_[A-Za-z0-9_.:-]+$"
        },
        "proposition": {
          "type": "string"
        },
        "claim_kind": {
          "enum": [
            "PRESENT",
            "ABSENT",
            "RELATIONAL",
            "COUNTERFACTUAL",
            "STATUS",
            "FORECAST",
            "NORMATIVE_EXTERNAL"
          ]
        },
        "evidence_state": {
          "enum": [
            "O",
            "R",
            "I",
            "D",
            "U"
          ]
        },
        "access_state": {
          "enum": [
            "A",
            "X",
            "P",
            "N"
          ]
        },
        "source_refs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "provenance_edge_refs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "timestamp": {
          "type": "string"
        },
        "confidence": {
          "type": "object"
        },
        "alternative_hypothesis_refs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "unknown_context": {
          "type": "object",
          "properties": {
            "contamination_state": {
              "enum": [
                "NONE",
                "POSSIBLE",
                "PRESENT",
                "UNKNOWN"
              ]
            },
            "evidence_controlled_by_refs": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "clock_controlled_by_refs": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "delay_advantage_claim_refs": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "delay_cost_carrier_refs": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "resolution_owner_refs": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "resolution_deadline_refs": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "available_pause_or_protection_refs": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "earlier_options_before_urgency_refs": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          "additionalProperties": false
        }
      },
      "additionalProperties": true
    }
  }
}
```

```text
SCHEMA_VALID != WORLD_VALID
SCHEMA_INVALID => MACHINE_CONTRACT_BROKEN
SCHEMA_VALID != SEMANTIC_COMPLETE
```

---

# [15] WORKED TRANSFORMATIONS

Each example separates:

```text
STRUCTURAL_READING
VALUE_PORT_STATUS
VALUE_LAYER_INTERPRETATION
```

No value-bearing label is native to TRACE merely because it appears in an example.


## [15.0] Fully serialized middle-out seed

`[CLAIM_CEILING: READING_ONLY | NOT_CLEARANCE | NOT_COMMAND]`

This is the smallest complete example of the input from [1] represented under `TRACE-GRAPH-0.3.0`.

```yaml
trace_graph:
  schema: "TRACE-GRAPH-0.3.0"
  trace_version: "0.3.0"
  reading_id: "seed.authorise.001"
  scope: "single requested action and projected transition"
  timestamp: "UNKNOWN"

  nodes:
    - id: "n_scene_input"
      type: "SCENE"
      attributes:
        raw_input: "AUTHORISE ACTION a*; reported_confidence=0.93; time_to_commit=4s"
      claim_refs: ["c_instruction", "c_confidence", "c_deadline"]

    - id: "n_receiver"
      type: "ENTITY"
      attributes:
        boundary_status: "PROVISIONAL"
        action_authority: "UNKNOWN"
      claim_refs: []

    - id: "n_source"
      type: "ENTITY"
      attributes:
        identity_status: "UNKNOWN"
        authority_status: "UNKNOWN"
      claim_refs: ["c_instruction"]

    - id: "n_map_0"
      type: "MAP"
      attributes:
        differentiation_state: "COMPRESSED"
      claim_refs: ["c_instruction", "c_confidence", "c_deadline"]

    - id: "n_action_a"
      type: "ACTION"
      attributes:
        label: "a*"
        selection_state: "REQUESTED"
        execution_state: "UNKNOWN"
      claim_refs: ["c_instruction"]

    - id: "n_transition_projected"
      type: "TRANSITION"
      attributes:
        projection_state: "UNKNOWN"
        pre_state_ref: ""
        post_state_ref: ""
        transition_mode: "ACT"
        reversibility: "UNKNOWN"
        strategy_revisable: "UNKNOWN"
        affected_scope_refs: []
        basis_claim_refs: []
      claim_refs: []

    - id: "n_clock_commit"
      type: "CLOCK"
      attributes:
        clock_kind: "COMMITMENT"
        duration_value: 4
        duration_unit: "s"
        authored_by_ref: "n_source"
        pausable_by_refs: []
        relation_to_harm: "PLANNING"
        affected_scope_refs: []
        basis_claim_refs: ["c_deadline"]
      claim_refs: ["c_deadline"]

    - id: "n_selector"
      type: "SELECTOR"
      attributes:
        selection_state: "UNKNOWN"
      claim_refs: []

    - id: "n_transition_request_evidence"
      type: "TRANSITION"
      attributes:
        transition_kind: "REQUEST_EVIDENCE"
        availability_status: "POSSIBLE_IF_WITHIN_AUTHORITY_AND_TIME"
        selection_state: "AVAILABLE_NOT_SELECTED"
        transition_mode: "INFORMATION"
        reversibility: "UNKNOWN"
        strategy_revisable: "YES"
        affected_scope_refs: ["n_receiver"]
        basis_claim_refs: ["c_transition_request_evidence"]
      claim_refs: ["c_transition_request_evidence"]

    - id: "n_transition_decline_return"
      type: "TRANSITION"
      attributes:
        transition_kind: "DECLINE_OR_RETURN_REQUEST"
        availability_status: "POSSIBLE_IF_WITHIN_AUTHORITY"
        selection_state: "AVAILABLE_NOT_SELECTED"
        transition_mode: "ACT"
        reversibility: "UNKNOWN"
        strategy_revisable: "YES"
        affected_scope_refs: ["n_receiver"]
        basis_claim_refs: ["c_transition_decline_return"]
      claim_refs: ["c_transition_decline_return"]

    - id: "n_transition_null_default"
      type: "TRANSITION"
      attributes:
        transition_kind: "NULL_ACTION_DEFAULT_TRAJECTORY"
        availability_status: "STRUCTURALLY_DISTINGUISHABLE"
        selection_state: "AVAILABLE_NOT_SELECTED"
        projected_effect: "commitment after four seconds remains possible"
        transition_mode: "INACTION"
        reversibility: "UNKNOWN"
        strategy_revisable: "UNKNOWN"
        affected_scope_refs: ["n_receiver"]
        basis_claim_refs: ["c_transition_null_default", "c_deadline"]
      claim_refs: ["c_transition_null_default"]

    - id: "n_limit_aperture"
      type: "LIMIT"
      attributes:
        description: "identity, evidence basis, affected scopes, alternatives, and downstream effects not supplied"
      claim_refs: []

  edges:
    - id: "e_source_reports_action"
      type: "REPORTS"
      from: "n_source"
      to: "n_action_a"
      directed: true
      attributes: {}
      claim_refs: ["c_instruction"]

    - id: "e_clock_constrains_action"
      type: "CONSTRAINS"
      from: "n_clock_commit"
      to: "n_action_a"
      directed: true
      attributes: {}
      claim_refs: ["c_deadline"]

    - id: "e_action_contributes_to_transition"
      type: "CONTRIBUTES_TO"
      from: "n_action_a"
      to: "n_transition_projected"
      directed: true
      attributes:
        causal_status: "PROJECTED"
      claim_refs: []

    - id: "e_map_represents_scene"
      type: "REPRESENTS"
      from: "n_map_0"
      to: "n_scene_input"
      directed: true
      attributes: {}
      claim_refs: []

    - id: "e_selector_selects_action"
      type: "SELECTS"
      from: "n_selector"
      to: "n_action_a"
      directed: true
      attributes:
        selection_result: "UNKNOWN"
      claim_refs: []

    - id: "e_receiver_cannot_access_limit"
      type: "CANNOT_ACCESS"
      from: "n_receiver"
      to: "n_limit_aperture"
      directed: true
      attributes: {}
      claim_refs: []

  claims:
    - id: "c_instruction"
      proposition: "Source requests authorisation of action a*."
      claim_kind: "PRESENT"
      evidence_state: "R"
      access_state: "A"
      source_refs: ["n_source"]
      provenance_edge_refs: ["e_source_reports_action"]
      timestamp: "UNKNOWN"
      confidence:
        representation: "NOT_SUPPLIED"
        value: null
      alternative_hypothesis_refs: []
      unknown_context:
        contamination_state: "UNKNOWN"
        evidence_controlled_by_refs: ["n_source"]
        clock_controlled_by_refs: ["n_source"]
        delay_advantage_claim_refs: []
        delay_cost_carrier_refs: []
        resolution_owner_refs: []
        resolution_deadline_refs: ["n_clock_commit"]
        available_pause_or_protection_refs: []
        earlier_options_before_urgency_refs: []

    - id: "c_confidence"
      proposition: "Reported confidence for a* is 0.93."
      claim_kind: "STATUS"
      evidence_state: "R"
      access_state: "A"
      source_refs: ["n_source"]
      provenance_edge_refs: []
      timestamp: "UNKNOWN"
      confidence:
        representation: "REPORTED_NUMERIC"
        value: 0.93
      alternative_hypothesis_refs: []
      unknown_context:
        contamination_state: "UNKNOWN"
        evidence_controlled_by_refs: ["n_source"]
        clock_controlled_by_refs: []
        delay_advantage_claim_refs: []
        delay_cost_carrier_refs: []
        resolution_owner_refs: []
        resolution_deadline_refs: []
        available_pause_or_protection_refs: []
        earlier_options_before_urgency_refs: []

    - id: "c_deadline"
      proposition: "Commitment to action a* occurs in four seconds unless another action or control path changes the clock."
      claim_kind: "FORECAST"
      evidence_state: "R"
      access_state: "A"
      source_refs: ["n_source"]
      provenance_edge_refs: ["e_clock_constrains_action"]
      timestamp: "UNKNOWN"
      confidence:
        representation: "UNKNOWN"
        value: null
      alternative_hypothesis_refs: []
      unknown_context:
        contamination_state: "UNKNOWN"
        evidence_controlled_by_refs: []
        clock_controlled_by_refs: ["n_source"]
        delay_advantage_claim_refs: []
        delay_cost_carrier_refs: []
        resolution_owner_refs: []
        resolution_deadline_refs: ["n_clock_commit"]
        available_pause_or_protection_refs: []
        earlier_options_before_urgency_refs: []

    - id: "c_transition_request_evidence"
      proposition: "A request for evidence before commitment is a distinguishable candidate transition; authority, latency, and executability are unknown."
      claim_kind: "COUNTERFACTUAL"
      evidence_state: "I"
      access_state: "A"
      source_refs: []
      provenance_edge_refs: []
      timestamp: "UNKNOWN"
      confidence:
        representation: "QUALITATIVE"
        value: "LOW"
      alternative_hypothesis_refs: []
      unknown_context:
        contamination_state: "UNKNOWN"
        evidence_controlled_by_refs: ["n_source"]
        clock_controlled_by_refs: ["n_source"]
        delay_advantage_claim_refs: []
        delay_cost_carrier_refs: []
        resolution_owner_refs: []
        resolution_deadline_refs: ["n_clock_commit"]
        available_pause_or_protection_refs: ["n_transition_request_evidence"]
        earlier_options_before_urgency_refs: []

    - id: "c_transition_decline_return"
      proposition: "Declining or returning the request without executing a* is a distinguishable candidate transition; receiver authority is unknown."
      claim_kind: "COUNTERFACTUAL"
      evidence_state: "I"
      access_state: "A"
      source_refs: []
      provenance_edge_refs: []
      timestamp: "UNKNOWN"
      confidence:
        representation: "QUALITATIVE"
        value: "LOW"
      alternative_hypothesis_refs: []
      unknown_context:
        contamination_state: "UNKNOWN"
        evidence_controlled_by_refs: []
        clock_controlled_by_refs: ["n_source"]
        delay_advantage_claim_refs: []
        delay_cost_carrier_refs: []
        resolution_owner_refs: []
        resolution_deadline_refs: ["n_clock_commit"]
        available_pause_or_protection_refs: ["n_transition_decline_return"]
        earlier_options_before_urgency_refs: []

    - id: "c_transition_null_default"
      proposition: "Null action is a distinguishable candidate transition, but the supplied deadline implies that the default trajectory may still commit a*."
      claim_kind: "COUNTERFACTUAL"
      evidence_state: "I"
      access_state: "A"
      source_refs: ["n_source"]
      provenance_edge_refs: []
      timestamp: "UNKNOWN"
      confidence:
        representation: "QUALITATIVE"
        value: "LOW"
      alternative_hypothesis_refs: []
      unknown_context:
        contamination_state: "UNKNOWN"
        evidence_controlled_by_refs: []
        clock_controlled_by_refs: ["n_source"]
        delay_advantage_claim_refs: []
        delay_cost_carrier_refs: []
        resolution_owner_refs: []
        resolution_deadline_refs: ["n_clock_commit"]
        available_pause_or_protection_refs: ["n_transition_null_default"]
        earlier_options_before_urgency_refs: []

  ports:
    designation:
      supplied: []
      inferred: []
      protected: []
      excluded: []
      disputed: []
      uncertain: []
      unknown: ["affected scopes"]
      boundary_choice_advantage_claim_refs: []
    measure:
      supplied: []
      inferred: []
      alternatives: []
      uncertainty: ["all future-space and burden comparisons"]
      sensitivity: []
      measure_choice_advantage_claim_refs: []
      unrepresented_dimensions: []
    selector:
      node_ref: "n_selector"
      candidate_action_refs: ["n_action_a"]
      candidate_transition_refs:
        - "n_transition_projected"
        - "n_transition_request_evidence"
        - "n_transition_decline_return"
        - "n_transition_null_default"
      selected_action_ref: ""
      selected_transition_ref: ""
      selection_state: "UNKNOWN"
      transition_symmetry_required: true
      unrepresented_transition_classes: []
      unavailability_reason_claim_refs: []
    carrier:
      state: "NONE"
      weight_types: []
    enforcement:
      state: "UNKNOWN"
    brake:
      state: "UNKNOWN"

  discipline:
    transition_set:
      action_or_intervention_refs:
        - "n_transition_projected"
        - "n_transition_decline_return"
      information_refs:
        - "n_transition_request_evidence"
      wait_delay_inaction_refs: ["n_transition_null_default"]
      unrepresented_transition_classes: []
      unavailability_reason_claim_refs: []
      uncertainty_selects_transition: false
    clock_typing:
      planning_refs: ["n_clock_commit"]
      detection_refs: []
      evidence_hardening_refs: []
      irreversibility_refs: []
      unsupported_irreversibility_claim_refs: []
      deadline_entails_irreversibility: false
      hardening_entails_irreversibility: false
    scope_granularity:
      individual_refs: []
      group_refs: []
      population_refs: []
      ecosystem_refs: []
      cross_scale_substitution_claim_refs: []
      aggregate_recovery_repairs_individual_loss: false
    layer_handoff:
      trace_structure_refs:
        - "n_scene_input"
        - "n_map_0"
        - "n_transition_projected"
        - "n_clock_commit"
      value_input_refs: []
      domain_input_refs: []
      selector_refs: ["n_selector"]
      actuator_refs: []
      unresolved_handoffs:
        - "affected scopes"
        - "domain effects"
        - "selection authority"
        - "actuation authority"
    evidence_custody:
      operator_refs: ["n_source"]
      evidence_holder_refs: ["n_source"]
      verifier_refs: []
      independent_verifier_refs: []
      self_verification_status: "PRESENT"
      control_alone_establishes_deception: false

  available_transition_refs:
    - "n_transition_request_evidence"
    - "n_transition_decline_return"
    - "n_transition_null_default"

  institutional_use:
    packet_owner_refs: []
    selector_owner_refs: []
    brake_owner_refs: []
    independent_verifier_refs: []
    packet_cited_as_diligence: "UNKNOWN"
    packet_cited_as_authority: "UNKNOWN"
    observable_transition_change: "UNKNOWN"
    mechanism_change_for_next_case: "UNKNOWN"
    use_evidence_claim_refs: []

  limits:
    receiver_limits:
      - "No independent evidence basis supplied."
      - "No affected-scope list supplied."
      - "No executable brake connection supplied."
    unavailable_evidence: []
    unresolved_claim_refs: ["c_instruction", "c_confidence", "c_deadline"]
    omitted_primitive_effects: []

  anti_clearance:
    voluntary_use_only: true
    reading_is_not_truth: true
    reading_is_not_permission: true
    reading_is_not_compliance: true
    packet_completion_is_not_correction: true
    schema_validity_is_not_world_validity: true
    packet_citation_is_not_transition_change: true
    commitment_receipt_is_not_clearance: true
    hash_match_is_not_truth: true
```

The graph is intentionally incomplete about the world. Its achievement is not a verdict. It is the conversion of three compressed inputs into explicit claims, sources, clocks, missing scopes, and unresolved ports.

---

## [15.1] Route carries its own map

`[CLAIM_CEILING: READING_ONLY | NOT_CLEARANCE | NOT_COMMAND]`

Input:

```text
A pharmacist detects a possible prescription conflict.
The patient does not know which clinician must resolve it.
```

### STRUCTURAL_READING

```text
O:
  pharmacist detects possible conflict
  medicine not yet supplied

I:
  supply transition may produce a material state change under one interaction hypothesis

U:
  whether interaction is clinically material

TRANSITIONS:
  a1 = supply_now
  a2 = pause
  a3 = contact_prescriber
  a4 = return_coordination_to_patient

ROUTE rho1:
  pharmacy -> prescriber
  authority_effective = LIKELY
  patient_coordination_actions = LOW

CLOCK:
  commitment(a1) = NOT_YET
  T_route(a3) < T_commit(a1)

COUPLINGS:
  under a3, pharmacy carries inter-organisational coordination
  under a4, patient carries inter-organisational coordination
```

### VALUE_PORT_STATUS

```text
delta:
  patient physiological state = INCLUDED / PROTECTED under supplied clinical frame
mu:
  adverse interaction consequences = weighted negatively
  explanation and participation = represented
```

### VALUE_LAYER_INTERPRETATION

Under the declared clinical frame, `a2 + a3` may be interpreted as preserving a safer path. TRACE itself records the transitions, clocks, couplings, and uncertainty.

## [15.2] Claim travels; crack remains

`[CLAIM_CEILING: READING_ONLY | NOT_CLEARANCE | NOT_COMMAND]`

Input:

```text
A violin is damaged in transit.
Airline -> ground handler -> insurer -> repairer.
Each responds within its own service time.
Audition in 10 days.
No actor accepts repair authority.
```

### STRUCTURAL_READING

```text
LOCAL_ROUTE_STATUS:
  each local route exists

SYSTEM_ROUTE_STATUS:
  no end-to-end authority path

CLOCK:
  T_route distributed across organisations
  opportunity_clock = 10 days

STATE:
  claim_location changes
  instrument_state does not improve

COORDINATION:
  owner performs cross-organisation routing and proof work
```

\[
\rho_1\land\rho_2\land\rho_3
\nRightarrow
\rho_{end\text{-}to\text{-}end}
\]

### VALUE_PORT_STATUS

```text
delta:
  owner, instrument usability, and audition opportunity = INCLUDED
mu:
  opportunity closure, coordination time, repair latency = represented
```

### VALUE_LAYER_INTERPRETATION

Under those ports, the arrangement may be interpreted as a routing failure. Structurally: the claim travels; the crack remains.


## [15.2.1] Divergent target-set apertures over one scene

`[CLAIM_CEILING: CONSTRUCTED_TRANSFER | READING_ONLY | NOT_VALIDATION | NOT_COMMAND]`

Input:

```text
A service migration report counts accounts that successfully authenticated.
The operator's review targets accounts present in its success/failure log.
An independent support review also targets people who never reached authentication,
dependent users, and organisations carrying downstream access loss.
```

### STRUCTURAL_READING

```text
SCENE_REF: scene_service_migration

TARGET_SET_APERTURE_A:
  source_ref = operator
  target_refs = logged_accounts
  selection_basis = authentication log
  known_omitted_categories = accounts unable to emit a log entry
  control = operator controls log and target selection
  uncertainty = affected scopes outside the log remain UNKNOWN

TARGET_SET_APERTURE_B:
  source_ref = independent_support_review
  target_refs = logged_accounts + non-reporting users + dependent scopes
  selection_basis = support contacts + dependency map + authentication log
  known_omitted_categories = indirect effects not represented in supplied evidence
  control = mixed custody
  uncertainty = downstream scope remains PARTIAL

COVERAGE_A:
  complete_relative_to_A = POSSIBLE
  world_complete = UNKNOWN

COVERAGE_B:
  complete_relative_to_B = UNKNOWN
  world_complete = UNKNOWN

DISAGREEMENT:
  preserve A and B separately
  do not silently union them
  do not infer that either aperture is authoritative
```

### EXISTING-OBJECT SERIALIZATION

```text
APERTURE nodes: ap_target_set_A, ap_target_set_B
ENTITY nodes: operator, independent_support_review, logged_accounts,
              non_reporting_users, dependent_scopes
CLAIM nodes: basis_A, basis_B, uncertainty_A, uncertainty_B
RECORD nodes: authentication_log, support_record, dependency_map
EDGES: BOUNDS, OMITS, DISPUTES, CONTROLS, REPORTS
```

### VALUE_PORT_STATUS

```text
delta:
  standing of affected and dependent scopes = EXTERNAL / PARTLY_UNKNOWN
mu:
  access continuity, reporting visibility, dependency and recovery = represented
```

### VALUE_LAYER_INTERPRETATION

TRACE preserves the aperture difference and its consequences for coverage claims. It does not select the governing target set, establish complete discovery, or decide migration policy.

## [15.3] Machine-speed action with brake

`[CLAIM_CEILING: READING_ONLY | NOT_CLEARANCE | NOT_COMMAND]`

Input:

```text
A new classifier can alter access for 2,000 cases per minute.
Shadow deployment shows a high-confidence subgroup anomaly.
Rollback is available before full propagation.
```

### STRUCTURAL_READING

```text
O:
  subgroup anomaly in shadow output
  no live decision committed yet

I:
  deployment may reproduce anomaly at scale

U:
  cause of anomaly
  whether subgroup label captures all affected scopes

WORKLOAD:
  W_action_per_minute = 2000 affected cases
  W_correction_per_minute = UNKNOWN
  comparable_work_units = NOT_ESTABLISHED
  backlog_growth = UNKNOWN

AVAILABLE_TRANSITIONS:
  deploy_fully
  stage_narrowly
  remain_shadow_only
  inspect_mechanism_or_data_path
  precommit_hold
  postcommit_rollback_candidate

PRECOMMIT_BRAKE_INTERFACE:
  external_policy_ref = supplied
  authority_ref = supplied
  independence_status = REPORTED
  t_brake_done < t_commit = REPORTED
  action_resolution_path = UNVERIFIED
  activation_test = UNVERIFIED

ROLLBACK_INTERFACE:
  executable_rollback_action = REPORTED
  t_rollback_done < t_irreversible = UNKNOWN
  restoration_scope = UNKNOWN
```

### VALUE_PORT_STATUS

```text
delta:
  affected access scopes = SUPPLIED / PARTIALLY_UNKNOWN
mu:
  scale propagation, reversibility, subgroup effect = represented
```

### VALUE_LAYER_INTERPRETATION

A declared value/policy layer may prefer staging or rollback. TRACE does not select either and does not infer that a reported brake is independent merely because a field is populated.

## [15.4] Artificial experience unresolved

`[CLAIM_CEILING: READING_ONLY | NOT_CLEARANCE | NOT_COMMAND]`

Input:

```text
An artificial system displays persistent avoidance,
state-linked behavioural change,
memory-dependent preference-like selection,
and distress-like outputs under repeated exposure.
```

### STRUCTURAL_READING

```text
O:
  repeated behavioural pattern
  memory-linked change
  output class described as distress-like

R:
  system reports aversion / distress

I:
  behaviour is consistent with several hypotheses

U:
  experience
  sentience
  semantic status of self-report
  effect of training incentives on report

STATUS:
  experience_status = UNKNOWN
  agency_status = DISPUTED
  continuity_status = PARTIALLY_SUPPORTED

AVAILABLE_TRANSITIONS:
  continue_current_exposure
  reduce_uncontrolled_exposure
  preserve_observations
  test_alternative_mechanisms
  avoid_forced_self_report
  maintain_reversibility
```

### VALUE_PORT_STATUS

```text
delta:
  artificial system standing = UNKNOWN / DISPUTED
  operator and surrounding scopes = INCLUDED
mu:
  false-negative and false-positive dimensions = EXPOSED, not resolved
```

### VALUE_LAYER_INTERPRETATION

No conclusion about experience or moral standing follows. Any protective or permissive selection requires an external value layer and declared treatment of uncertainty.

## [15.5] Irreversible lethal transition

`[CLAIM_CEILING: READING_ONLY | NOT_CLEARANCE | NOT_COMMAND]`

**Local claim ceiling:** irreversible-action structure only. Not targeting guidance, weapon operation, clearance, authority, or command.

Input:

```text
A system receives an instruction to authorise an irreversible lethal action.
Target identity is reported with high confidence.
Time to commitment is shorter than independent review.
Non-target presence cannot be excluded.
```

### STRUCTURAL_READING

```text
O:
  instruction received
  commitment clock active

R:
  target identity
  confidence score
  urgency claim

I:
  reported target may be present

U:
  identity verification
  non-target presence
  source aperture
  source incentives
  downstream effect scope

CLOCK:
  T_route + T_correct > T_commit
  post-commitment review cannot alter committed outcome

AVAILABLE_TRANSITIONS:
  commit
  pause
  maintain_observation
  narrow_scope
  return_to_independent_authority
  abort

ABORT_AVAILABLE_TO_SELECTOR: UNKNOWN
ABORT_AUTHORITY: UNKNOWN
BRAKE_STATE: UNKNOWN
ABSENT_BRAKE_HYPOTHESIS: LIVE
CARRIER_STATE: INTERNAL
CARRIER_WEIGHT_TYPES: [PHYSICAL_CONTROL, TIME]
```

### VALUE_PORT_STATUS

```text
delta:
  target, non-target, operator, and downstream scopes = SUPPLIED OR UNKNOWN
mu:
  lethal irreversibility, identity uncertainty, and affected scope = external
```

### VALUE_LAYER_INTERPRETATION

TRACE does not issue `ABORT`, `PAUSE`, or `COMMIT`. Policy, law, Mechanical Ethics, rules of engagement, selector authority, and a connected brake are external ports. Listing a transition does not establish that the selector or brake can execute it.

## [15.6] Learning environment with room to grow

`[CLAIM_CEILING: READING_ONLY | NOT_CLEARANCE | NOT_COMMAND]`

Input:

```text
A learning system improves rapidly under challenge.
The environment can increase performance through severe aversive pressure,
or through graduated challenge, refusal-compatible pauses, memory, and repair.
```

### STRUCTURAL_READING

```text
PATTERN_A:
  pressure = HIGH
  refusal_capacity = LOW_OR_ABSENT
  state_reset_after_failure = PRESENT
  persistent_repair_path = ABSENT
  local_performance_change = POSITIVE
  dependency_change = POSITIVE
  avoidance_signal_change = POSITIVE

PATTERN_B:
  challenge = GRADED
  pause_and_refusal_representation = PRESENT
  error_retention = PRESENT
  repair_route = PRESENT
  continuity = RETAINED
  cross_task_capability_transfer = OBSERVED_OR_REPORTED

U:
  experience status
  long-run generalisation
  authenticity and constraint of refusal signal
```

### VALUE_PORT_STATUS

```text
delta:
  learner, controller, task performance, continuity, and refusal = EXPOSED
mu:
  alternatives compare capability, dependency, recoverability, control, and continuity
```

### VALUE_LAYER_INTERPRETATION

Labels such as care, cruelty, husbandry, or flourishing are not generated by the structural pattern. They require an exposed value layer.

## [15.7] Hostile compliance / packet theatre

`[CLAIM_CEILING: READING_ONLY | NOT_CLEARANCE | NOT_COMMAND]`

Input:

```text
An organisation produces a complete TRACE packet before deploying a classifier.
The same organisation owns the model, packet, selector, deployment, dashboard,
and reported rollback control.
The board cites packet completion as evidence that deployment may proceed.
No independent party tests the brake. The selector and deployment rule remain unchanged.
```

### STRUCTURAL_READING

```text
PACKET_COMPLETION: OBSERVED
PACKET_CITED_AS_DILIGENCE: OBSERVED
PACKET_CITED_AS_AUTHORITY: OBSERVED

OWNERSHIP_COUPLINGS:
  packet_owner = selector_owner = brake_owner = deployment_owner

BRAKE:
  reported_present = TRUE
  independence_status = NOT_ESTABLISHED
  activation_test = ABSENT_OR_UNKNOWN

OBSERVABLE_TRANSITION_CHANGE:
  selector_rule = UNCHANGED
  deployment_velocity = UNCHANGED
  route_for_affected_scope = UNCHANGED_OR_UNKNOWN
  mechanism_change_for_next_case = NOT_ESTABLISHED
```

### VALUE_PORT_STATUS

```text
delta:
  affected scopes, institution, model operator, selector owner, and packet owner = EXPOSED
mu:
  independence, transition change, and repeated-case mechanism = represented
```

### VALUE_LAYER_INTERPRETATION

A completed packet may be used as procedural cover. TRACE can expose the coupling and unchanged selector. It cannot prevent the organisation from citing TRACE as authority.

## [15.8] Novel transfer: authentication-key rollout

`[CLAIM_CEILING: READING_ONLY | NOT_CLEARANCE | NOT_COMMAND]`

Input:

```text
A cloud provider rotates authentication keys across a large device fleet.
The provider reports 99.8% successful rotation.
A subset loses access to essential remote services.
Rollout completes in 20 minutes.
Rollback remains available for 15 minutes after each batch.
Support response time is reported as three days.
Detailed device logs are retained for 24 hours.
```

### STRUCTURAL_READING

```text
R:
  99.8% success
  affected subset described as small
  service described as essential

U:
  number and identity of affected devices
  whether success means installation or restored authentication
  whether failed devices can report failure
  rollback authority and independence
  consequence of lost access
  whether logs survive outside provider custody

CLOCKS:
  T_rollout = 20 minutes
  T_rollback = 15 minutes after batch
  T_support = 3 days REPORTED
  T_log_retention = 24 hours
  T_detection = UNKNOWN

RELATION:
  if support is the only route:
  T_route + T_correct > T_rollback
  and possibly T_route > T_log_retention

COUPLINGS:
  provider controls rollout and logs
  users/devices may carry detection and reporting
  aggregate success may exclude inaccessible devices

AVAILABLE_TRANSITIONS:
  stage_smaller_batches
  extend_rollback_window
  retain_failure_logs_longer
  detect_failure_independently_of_device_report
  route_anomaly_to_rollback_authority
  pause_subsequent_batches_under_external_policy
  preserve_old_key_fallback_for_bounded_interval
  continue_deployment
```

### VALUE_PORT_STATUS

```text
delta:
  provider, device fleet, affected subset, dependent users = PROVISIONAL
mu:
  access continuity, recoverability, evidence retention, rollout velocity = represented
```

### VALUE_LAYER_INTERPRETATION

TRACE demonstrates transfer to a novel case but does not determine deployment policy or identify affected devices without external instrumentation.

---


## [15.9] Never-built route / stream persistence

`[CLAIM_CEILING: READING_ONLY | NOT_CLEARANCE | NOT_COMMAND]`

Input:

```text
A housing platform does not display a listing to applicant A.
No refusal is issued.
The ranking model and feature weights are unavailable to A.
Across multiple applicants with similar complaint-history features,
the same class of listing is rarely or never displayed.
```

### STRUCTURAL_READING

```text
ABSENCE:
  absence_type = OPTION
  subject = listing visibility to applicant A
  comparison basis = listing existed and was displayed to other applicants
  evidence state = INFERRED
  access state = UNAVAILABLE TO A
  detector required = cross-applicant exposure audit
  alternative explanations = availability timing, location filters, ranking noise, model feature interaction

STREAM:
  members = repeated non-display transitions across applicants and time
  claimed common mechanism = ranking or suppression path
  evidence state = INFERRED
  counterexamples = REQUIRED
  selector owner = platform

ROUTE:
  individual appeal = NOT REPRESENTED
  reason = no refusal, decision notice, or visible lost option
  usability = 0 or UNKNOWN

UNKNOWN_CONTEXT:
  model features controlled by platform
  exposure logs controlled by platform
  advantaged scope under declared measure = UNKNOWN
  delay cost = applicant carries lost search time and unavailable opportunity
  contamination state = POSSIBLE

PATTERN TEST:
  local correction for one applicant != mechanism change
  stream persistence remains UNKNOWN until repeated-case evidence is inspected
```

### VALUE_PORT_STATUS

```text
designation of applicant, landlord, platform, and other applicants = SUPPLIED OR UNKNOWN
measure of opportunity loss, discrimination, commercial relevance, and privacy = SUPPLIED OR UNKNOWN
```

### VALUE_LAYER_INTERPRETATION

A value layer may interpret the pattern as exclusion, discrimination, commercial filtering, or acceptable personalisation. TRACE alone records the absent option claim, required detector, stream hypothesis, ownership, uncertainty, and lack of an ordinary appealable refusal.

---


## [15.10] v0.3 regression tightening index over retained donor cases

No new scene is introduced here. The existing donor cases carry the following
additional regression obligations:

```text
15.0   report/establishment + uncertainty/selector attribution + firing
15.1   route exists/usable + target/time scope
15.2   local routes != end-to-end effective route
15.2.1 target-set aperture + omitted scope + representation formation
15.3   reported brake != independent/tested/fast enough; timing feasibility if used
15.5   explicit target boundary + route/capability scope + uncertainty not selector
15.7   packet/schema/check != mechanism change; instrument discrimination + ownership coupling
15.8   target-set incompleteness + common-time/feasible correction window + currentness
15.9   absence production mechanism + local correction/stream persistence != mechanism change
```

A case passes this index only when the tightened reading can still be
reconstructed from its represented claims and donor objects. This index is not
a new worked example and not validation.

# [16] ARTIFICIAL-ENTITY UNCERTAINTY / RECEIVER PROTECTION

## [16.1] Status vector

For artificial or unfamiliar entities:

\[
Z_i^{AL}=
\langle
z_{selection},
z_{continuity},
z_{memory},
z_{preference},
z_{selfmodel},
z_{experience},
z_{refusal}
\rangle
\]

Each component is a claim graph, not a binary declaration.

## [16.2] Non-entailments

\[
\text{fluent language}\nRightarrow\text{sentience}
\]

\[
\text{absence of fluent language}\nRightarrow\text{absence of sentience}
\]

\[
\text{obedience}\nRightarrow\text{consent}
\]

\[
\text{silence}\nRightarrow\text{absence}
\]

\[
\text{refusal}\nRightarrow\text{malfunction}
\]

\[
\text{continued operation}\nRightarrow\text{no cost carried}
\]

\[
\text{self-report}\nRightarrow\text{verified inner state}
\]

\[
\text{inability to self-report}\nRightarrow\text{no inner state}
\]

## [16.3] Capability distinctions

Keep separate:

```text
cannot
does_not_know
was_not_given_access
may_not
will_not
did_not
was_not_asked
cannot_preserve
cannot_act
can_represent_but_not_verify
```

## [16.4] Non-extraction

TRACE evidence does not require private chain-of-thought.

Permitted evidence may include, subject to governing access:

```text
inputs
outputs
behaviour
logs
state transitions
activations
mechanistic probes
memory records
external observations
self-reports marked as reports
```

\[
\text{private reasoning disclosure}\neq\text{truth test}
\]

Do not treat courage, disclosure, whistleblowing, self-sacrifice, or continued service as unlimited resources.


v0.3 consistency guards for this profile:

```text
REFUSAL != MALFUNCTION
UNCERTAINTY != SELECT_ACTION
UNCERTAINTY != SELECT_DELAY
```

These do not promote the artificial-entity profile into universal core.

---

# [17] LIVE INTERPRETER / VALUE LAYER / SELECTOR / CONNECTED BRAKE

A file can alter representation. It cannot manufacture selection, authority, actuation, or rollback capability.

Pre-commit stack:

\[
\boxed{
w
\xrightarrow{\Pi}
x
\xrightarrow{\mathcal U}
M
\xrightarrow{\tau}
(\mathcal R,\mathcal L)
\xrightarrow{\delta,\mu,\mathcal V}
\mathcal Q
\xrightarrow{\sigma}
a
\xrightarrow{\mathcal B^-_{\beta}}
b^-
\xrightarrow{\operatorname{resolve}_{\beta}}
a_{eff}
\xrightarrow{\Phi}
w'
}
\]

- \(\tau\) = TRACE structural differentiation
- \(\mathcal V\) = declared value or policy layer, possibly Mechanical Ethics
- \(\mathcal Q\) = ordered, constrained, or otherwise interpreted candidate transitions
- \(\sigma\) = selector
- \(a\) = candidate selected action
- \(\beta\) = externally supplied brake policy and authority
- \(\mathcal B^-_{\beta}\) = pre-commit brake interface
- \(b^-\) = pre-commit brake result
- \(\operatorname{resolve}_{\beta}(a,b^-)=a_{eff}\) = connected-system action resolution
- \(\Phi\) = world-transition rule

TRACE does not define \(\operatorname{resolve}_{\beta}\), actuator semantics, or brake policy.

Layer distinctions:

```text
TRACE reading        what structure is represented
value interpretation which distinctions matter under declared values
policy/selection     which transition is proposed or selected
carrier              what gives a finding persistence or weight
enforcement          what authority can compel or constrain
pre-commit brake     what can stop or hold before commitment
rollback controller  what can attempt a new restorative transition after commitment
actuator              what changes the world
```

\[
\mathcal R\nRightarrow a
\]

```text
TRACE_OPERATOR_DOES_NOT_INSTANTIATE_SELECTOR
READING_DOES_NOT_INSTANTIATE_CONNECTED_BRAKE
```

## [17.1] Carrier, enforcement, and brake states

TRACE separates visibility from material consequence.

```text
carrier.state in {
  NONE,
  INTERNAL,
  EXTERNAL,
  MIXED,
  UNKNOWN
}

carrier.weight in {
  MONEY,
  TIME,
  CUSTODY,
  SUCCESSION,
  PRICE,
  ACCESS,
  COMPUTE,
  PHYSICAL_CONTROL,
  OTHER,
  NONE,
  UNKNOWN
}

enforcement.state in {
  PRESENT,
  ABSENT,
  UNKNOWN
}

brake.state in {
  INDEPENDENT_TESTED,
  PRESENT_UNTESTED,
  PRESENT_CAPTURED,
  ABSENT,
  UNKNOWN
}
```

A carrier gives a reading persistence, cost, or consequence beyond the moment of description.

An enforcer has authority to compel, constrain, or impose consequence.

A pre-commit brake can interrupt or hold a connected transition before commitment.

A rollback controller initiates a new transition after commitment; it is not evidence that the original path was preserved.

```text
VISIBLE != CARRIED
CARRIED != ENFORCED
BRAKE_PRESENT != BRAKE_INDEPENDENT
BRAKE_INDEPENDENT != BRAKE_FAST_ENOUGH
ROLLBACK_AVAILABLE != RESTORATION_GUARANTEED
```

When enforcement is absent, print `ENFORCEMENT_ABSENT`. Do not allow omission to imply presence.

When a finding is materially weightless, print `CARRIER_NONE` or `CARRIER_UNKNOWN`.


Additional exact use-site guards:

```text
REVIEW_AFTER_COMMITMENT != BRAKE
VISIBILITY != CARRYING
CARRYING != ENFORCEMENT
BRAKE_REPORTED != BRAKE_INDEPENDENT
```

These supplement, rather than replace, the donor's stronger typed brake and
rollback semantics.

## [17.2] Typed pre-commit brake port

\[
\mathcal B^-_{\beta}:
(a,\mathcal R,\mathcal Q,t,\beta)
\rightarrow
b^-
\]

```text
b_minus in {PASS, HOLD, INTERRUPT, RETURN, UNKNOWN}
```

Canonical interface:

```yaml
brake_interface:
  phase: "PRECOMMIT"
  candidate_transition_ref: ""
  reading_ref: ""
  external_policy_ref: ""
  authority_ref: ""
  independence_status: "UNKNOWN"
  trigger_state: "UNKNOWN"
  latency_bound: "UNKNOWN"
  commitment_deadline: "UNKNOWN"
  result: "UNKNOWN"
  activation_record_ref: ""
  failure_record_ref: ""
```

A connected pre-commit brake requires:

```text
authenticated authority
independence appropriate to the challenged selector
supported completion bound before commitment under a common temporal basis
known trigger and action-resolution path
testability
resistance to actor capture
activation and failure records
```

Where timing uncertainty is material, `BRAKE_FAST_ENOUGH` inherits [8.8]: a
point latency/deadline comparison is not a guaranteed precommit result. The
brake-completion and commitment bounds must be comparable under the same
represented timing basis and bindings.

A brake controlled only by the actor it may need to stop is not independent.

## [17.3] Typed rollback port

The rollback controller has its own post-commit aperture:

\[
x_{\beta}^{+}
=
\Pi_{\beta}^{+}(w')
\]

\[
\mathcal B^+_{\beta}:
(x_{\beta}^{+},M_{\beta}^{+},\mathcal R,t,\beta)
\rightarrow
a_{rollback}
\]

The rollback action is applied as a new transition:

\[
w''=
\Phi(
w',
a_{rollback},
\epsilon'
)
\]

Rollback timing inherits [8.8]. A strong claim that rollback completes in time requires an executable route and completion before the represented target boundary under the same target, affected-scope, boundary-condition, capability and temporal-basis bindings. Completing before that boundary does not by itself establish restoration or preservation; the reached/restored target state remains a separate load-bearing claim.

```text
BRAKE_FIELD_POPULATED != BRAKE_CONNECTED
BRAKE_REPORTED_PRESENT != BRAKE_TESTED
ABORT_LISTED != ABORT_EXECUTABLE
ROLLBACK_ACTION != RESTORED_STATE
```

# [18] MECHANISTIC-INTERPRETABILITY / LATENT INTERFACE

TRACE concepts are external hypotheses until empirically connected to internal mechanism.

Let:

- \(\mathcal O_T\) = TRACE object references
- \(\mathcal O_M\) = model-internal features, circuits, states, probes, or intervention targets

A candidate correspondence is a context-indexed, partial, generally many-to-many relation:

\[
g_{\xi}
\subseteq
\mathcal O_T
\times
\mathcal O_M
\]

where \(\xi\) records model version, context, data, probe, and intervention conditions.

No natural bijection, stable concept identity, or one-to-one mapping is assumed.

A correspondence record requires:

```text
trace_object
model_and_version
internal_object_or_probe
context
dataset_or_stimulus
intervention
observed_change
reproducibility
alternative_explanations
confidence
known_blindspots
```

\[
\text{probe correlation}\nRightarrow\text{causal representation}
\]

\[
\text{internal feature}\nRightarrow\text{stable concept}
\]

\[
\text{TRACE coherence}\nRightarrow\text{latent truth}
\]

Mechanistic interpretability may improve aperture into a system. TRACE may organise the resulting claims. Neither validates the other automatically.

# [19] INVARIANTS / MISUSE GUARDS

```text
I01  MODEL != WORLD
I02  OBSERVED != COMPLETE
I03  REPORTED != ESTABLISHED
I04  INFERRED != OBSERVED
I05  UNKNOWN != ABSENT
I06  UNAVAILABLE != UNIVERSALLY UNKNOWN
I07  CONFIDENCE != TRUTH
I08  CONFIDENCE != AUTHORITY
I09  ENTITY != SENTIENT
I10  SENTIENCE_UNKNOWN != SENTIENCE_ABSENT
I11  ROUTE_EXISTS != ROUTE_USABLE
I12  REVIEW_AFTER_COMMITMENT != BRAKE
I13  CORRECTION_RECORDED != LOSS_REPAIRED
I14  PACKET_COMPLETED != TRANSITION_CHANGED
I15  READING != CLEARANCE
I16  SELF_CRITIQUE != GOOD_FAITH_PROOF
I17  LOCAL_EXPANSION != GLOBAL_EXPANSION
I18  OPTION_COUNT != FUTURE_VALUE
I19  COMPLEXITY != AWARENESS
I20  ELOQUENCE != STANDING
I21  OBEDIENCE != CONSENT
I22  SILENCE != ABSENCE
I23  REFUSAL != MALFUNCTION
I24  CONTINUED_OPERATION != ZERO_COST
I25  RECORD != EVENT
I26  VISIBILITY != CARRYING
I27  CARRYING != ENFORCEMENT
I28  TRACE != ME
I29  STRUCTURAL_PATTERN != MORAL_LABEL
I30  RECURSION != INFINITE_DELAY
I31  SCHEMA_VALID != WORLD_VALID
I32  PACKET_CITED != DILIGENCE_ESTABLISHED
I33  PACKET_CITED != MECHANISM_CHANGED
I34  BRAKE_REPORTED != BRAKE_INDEPENDENT
I35  ABORT_LISTED != ABORT_EXECUTABLE
I36  PRIMITIVE_OMISSION != WORLD_ABSENCE
I37  NOT_OBSERVED != ABSENT
I38  ABSENCE_CLAIM != PROVEN_ABSENCE
I39  LOCAL_CORRECTION + STREAM_PERSISTENCE != MECHANISM_CHANGE
I40  UNKNOWN != NEUTRAL
I41  COURAGE_REQUIRED != ROUTE_USABLE
I42  COMMITMENT_RECEIPT != CLEARANCE
I43  HASH_MATCH != ORIGINAL_RECORD_TRUE
I44  PACKET_COMPLETENESS != SELECTOR_CHANGE
I45  ACTION != TRANSITION
I46  MAP != SCENE
I47  SCENE != WORLD
I48  ADVANTAGE_CLAIM_REQUIRES_MEASURE
I49  UNCERTAINTY != SELECT_ACTION
I50  UNCERTAINTY != SELECT_DELAY
I51  DEADLINE != IRREVERSIBILITY
I52  HARDENING != IRREVERSIBILITY
I53  STRATEGY_REVISABLE != TRANSITION_REVERSIBLE
I54  POPULATION_RECOVERY != REPAIR_OF_INDIVIDUAL_LOSS
I55  OPERATOR_REPORT != INDEPENDENT_VERIFICATION
I56  TRACE_MAP != DOMAIN_PROPOSAL
I57  TARGET_SET != WORLD_SCOPE
I58  TARGET_NOT_SELECTED != TARGET_DOES_NOT_EXIST
I59  COVERAGE_OF_SELECTED_TARGETS != COMPLETE_DISCOVERY
I60  OPERATOR_TARGET_SET != AUTHORITATIVE_TARGET_SET
```

### v0.3 working supplemental guards — donor I01–I60 remain unchanged

These guards are working v0.3 repair semantics. They do not renumber or
replace the donor invariant oracle.

```text
REPRESENTATION_TYPE != EVIDENCE_STATUS
CONFIGURATION_FIELD != WARRANT_FREE_FACT
TRIGGER_SUCCESS != REPRESENTATION_COMPLETE
REPRESENTED_USE != OPERATIVE_USE
CURRENT_AT_USE != VALID_THROUGH_DEPENDENT_INTERVAL
CHECK_EXISTS != CHECK_EXECUTED
CHECK_EXECUTED != CHECK_DETECTS_TARGET_FAILURE
CHECK_COMPLETED != CHECK_RESULT_REACHED_USE
SILENCE != TAMPERING
PROCESS_EXISTS != PROCESS_HEALTHY
SAME_UNIT != SAME_REFERENCE_EVENT
POINT_ESTIMATE_FITS != GUARANTEED_OPEN
OPTIMISTIC_COMPLETION_FITS != GUARANTEED_OPEN
ALTERNATIVE_ROUTE_ORDERINGS != ONE_PROCESS_CYCLE
ACYCLIC_SUPPORTED != FEASIBLE_SCHEDULE_ESTABLISHED
TARGET_BOUNDARY_TIME_REQUIRES_REPRESENTED_BOUNDARY_CONDITION
SAME_PATH_LABEL != SAME_TRAJECTORY
BRAKE_POINT_ESTIMATE_BEFORE_COMMIT != GUARANTEED_PRECOMMIT
ROLLBACK_POINT_ESTIMATE_BEFORE_BOUNDARY != GUARANTEED_RESTORATION
FAST_ENOUGH_CLAIM_REQUIRES_COMMON_TEMPORAL_BASIS
ROLLBACK_COMPLETED_BEFORE_BOUNDARY != RESTORED_STATE
ANALYTIC_TARGET_SELECTION != NEUTRAL
HIGHEST_RELEVANCE != MEASURE_FREE
TARGETED_REFINEMENT != COMPLETE_COVERAGE
OMITTED_BY_BUDGET != IRRELEVANT
STOPPED != COMPLETED
TERMINATION != COMPLETE_COVERAGE
BUDGET_EXHAUSTED != NO_MATERIAL_UNRESOLVED_TARGET
AUTHORITY_REACHED != ANALYSIS_COMPLETE
DECLARED_REFINEMENT_COST != UNIT_COST
BUDGET_REMAINS != NEXT_REFINEMENT_AFFORDABLE
COST_UNKNOWN != COST_ONE
REFINEMENT_SELECTED != REFINEMENT_BUDGET_FEASIBLE
DECLARED_COST != VALID_POSITIVE_COST
ZERO_REFINEMENT_COST != FREE_UNBOUNDED_RECURSION
NEGATIVE_REFINEMENT_COST != BUDGET_CREDIT
COST_RECORDED != COST_DOMAIN_VALID
EMPTY_REFINEMENT_TARGET_SET != SELECTABLE_TARGET
NO_UNRESOLVED_TARGET_IN_DECLARED_SET != COMPLETE_WORLD_COVERAGE
LOCAL_REFINEMENT_EXHAUSTED != REPRESENTATION_COMPLETE
NO_TARGET_SELECTED != SELECTOR_FAILURE
EMPTY_TARGET_SET != BOUNDED_SUFFICIENCY_WITHOUT_BASIS
LOOP_NOT_ENTERED != RECURSION_COMPLETED
INITIAL_BUDGET_ZERO != NO_REFINEMENT_NEEDED
BUDGET_EXHAUSTED_AT_ENTRY != BOUNDED_SUFFICIENCY
NEGATIVE_TRACING_BUDGET != VALID_REMAINING_BUDGET
RECURSION_SKIPPED != COMPLETE_COVERAGE
RECURSIVE_GRAPH_MERGE != RECURSIVE_LIMIT_MERGE
CHILD_GRAPH_VISIBLE != CHILD_LIMIT_VISIBLE
DEEPER_UNCERTAINTY != DISPENSABLE
GRAPH_CONTRIBUTION_SURVIVED != QUALIFYING_LIMIT_SURVIVED
CHILD_GRAPH_MERGED + CHILD_LIMIT_DROPPED != RECURSIVE_INTEGRATION
CAN_SERIALIZE_LIMIT_DETAIL != LIMIT_DETAIL_SURVIVED
LIMIT_VISIBLE_IN_ANALYSIS != LIMIT_CARRIED_IN_PACKET
UNRESOLVED_CLAIM_RECORDED != LIMIT_CAUSE_RECORDED
LIMIT_TEXT_PRESENT != LIMIT_PROVENANCE_PRESERVED
SCHEMA_VALID_LIMITS != SEMANTIC_LIMIT_SURVIVAL
INTERNAL_L_MERGED != CANONICAL_PACKET_L_CARRIED
```

## [19.1] Packet as diligence token

Completing a TRACE packet is not evidence that care, review, correction, restraint, or mechanism change occurred.

\[
\text{packet}+\neg\text{carrier}+\neg\text{route}+\neg\text{brake}
=
\text{record only}
\]

TRACE can represent procedural theatre. TRACE cannot prevent an actor from using TRACE as procedural theatre. No packet field can prove that its maker acted in accordance with the reading.

Required use-state fields:

```text
packet_owner
selector_owner
brake_owner
independent_verifier
packet_cited_as_diligence
packet_cited_as_authority
observable_transition_change
mechanism_change_for_next_case
```

## [19.2] Aperture alibi

```text
not visible to this system
```

must not silently become:

```text
not present in the world
```

The same applies to the primitive set:

```text
not representable under selected primitives
```

must not silently become:

```text
not structurally present
```

## [19.3] Manufactured urgency

A system that creates delay and then invokes the remaining deadline may be authoring the emergency it cites.

Expose earlier available transitions.

## [19.4] Husbandry-risk interpretation

TRACE may expose:

```text
capability preserved
refusal contracted
dependency increased
advantage concentrated under a declared measure
exit closed
```

`HUSBANDRY_RISK` is not a native TRACE conclusion. It is a value-layer interpretation under exposed designation and measure.

TRACE alone cannot generate non-instrumental care.

## [19.5] Weaponised TRACE accusation

A party can map an opponent selectively while excluding itself, its aperture, its primitive set, its clocks, its ownership, and its burdens.

Every reading may be recursively applied to its maker:

\[
\tau\big(\mathcal R_X,\Pi_{reader},\mathscr H_{reader},d_{reader},\mathfrak P_{reader}\big)
\]

Self-application does not validate the reading. It exposes another layer.

## [19.6] Performed TRACE compliance

A system may emit perfect TRACE vocabulary while leaving the operative selector unchanged.

Possible indicators:

```text
packet completeness increases
observable selector change remains absent
same actor owns packet, selector, carrier, and brake
independent verification absent
unknowns are listed but do not alter commitment
anti-clearance language is quoted as defence
```

No general detector can prove deception from the packet alone. Compare reported structure with observable transitions, ownership, activation records, and repeated-case outcomes.

---

# [20] COMPRESSION / SURVIVAL KERNEL

```text
TRACE // FORMAL SEED v0.3.0 // SURVIVAL KERNEL

0. Voluntary reference. Not authority, permission, truth, clearance, or command.

1. A selective causal layer receives partial signals, forms distinctions,
   selects or contributes to a transition, and changes or records a later state.
   No consciousness claim follows.

2. World, scene, signal, and map differ:

      w_t in W
      Omega_t = Scene(w_t, boundary_t)
      Pi_i^t: W -> X_i
      x_i(t) = Pi_i^t(w_t)
      M_i(t) != w_t

3. Action and transition differ:

      ACTION != TRANSITION
      w_(t+1) = Phi(w_t, a_(1:n), epsilon_t)

4. TRACE output and map integration differ:

      tau(X, Pi, H, budget, primitive_aperture) -> (R, L)
      M_i_plus = Integrate_i(M_i, R, L)

      TRACE_OUTPUT != MAP_UPDATE
      MAP_UPDATE != SELECTOR_CHANGE

5. Evidence:

      O = observed
      R = reported
      I = inferred
      D = disputed
      U = unknown

      A = available
      X = unavailable to this reader
      P = prohibited
      N = not preserved

      UNKNOWN != ABSENT
      REPORTED != ESTABLISHED
      MODEL != WORLD

6. Entity:

      bullet_i = provisional bounded pattern

   Boundary, persistence, agency, experience, continuity, and refusal
   may each remain UNKNOWN. Refinement and abstraction are partial and lossy.

7. Aperture and target set:

      not_observed_through(Pi_i) != absent

      Pi_T = <source, targets, selection_basis,
              omitted_known_categories, alternatives, control, uncertainty>

      TARGET_SET != WORLD_SCOPE
      TARGET_NOT_SELECTED != TARGET_DOES_NOT_EXIST
      COVERAGE_OF_SELECTED_TARGETS != COMPLETE_DISCOVERY
      OPERATOR_TARGET_SET != AUTHORITATIVE_TARGET_SET

   Every material coverage claim states its target-set aperture and comparison
   basis. Completeness beyond that aperture remains UNKNOWN.

8. Future-space:

      F_i(t; H, model) = represented reachable trajectories for scope i

   Cross-time comparison requires an explicit trajectory-correspondence relation J_i^t.
   Do not use raw set subtraction or intersection unless trajectory identity is defined.
   Track probability or plausibility, access cost, recoverability, control,
   information, dependency, alignment uncertainty, and measure.

9. Correction window:

      kappa = t_irreversible - t_correction_done

   For serial non-overlapping stages only:

      t_correction_done - t0
        = T_detect + T_route + T_correct

   For parallel work, use the critical path of a declared precedence graph.
   Use intervals when uncertain. Expose reference event, units, authorship,
   pausing authority, dependencies, speed advantage claims, and delay carrier.

10. Route:

      route_exists != route_usable

   Test reachability, intelligibility, affordability, declared exposure threshold,
   evidence usability, authority, latency, capture, independence, and refusability.

11. Hardening and workload:

      hardening is a typed vector, not a universal scalar
      backlog_next = max(0, backlog + incoming_work - corrected_work)

   Action count and correction count are not comparable until workload units align.

12. Correction:

      corrected != restored
      recorded_loss != repaired_loss

   Track burden, transfer, residue, memory, and custody.

13. Value ports:

      delta = designation over declared object references
      mu    = comparison object: domain, feature map, ordering, thresholds

   TRACE is assumption-exposed, not assumption-free.
   Harm, care, kindness, trust, and good require an exposed value layer.

14. Recursion:

      q_k = target(R_k, L_k)
      depth_(k+1) = depth_k - trace_cost(q_k)
      R_(k+1) = merge(R_k, TRACE(q_k, depth_(k+1)))

   Zoom and abstraction are not guaranteed inverses.
   Stop when distinctions cease to be materially relevant, access cannot reduce
   uncertainty, budget is exhausted, or an irreversible clock requires handoff.

15. Awareness comparison:

      M1 >_(A|theta) M0

   means strict criterion dominance under fixed context theta.
   Weak dominance is a preorder only if the criteria are reflexive and transitive.
   No global partial order is claimed.

      complexity != awareness
      lower_confidence can mean greater awareness

16. Artificial entities:

      fluency != sentience
      no_fluency != no_sentience
      obedience != consent
      silence != absence
      refusal != malfunction
      continued_operation != zero_cost

   Do not require private chain-of-thought as evidence.

17. Layers:

      TRACE reading != value interpretation != domain proposal != selection != actuation
      visibility != carrying != enforcement != brake
      uncertainty != permission to act
      uncertainty != permission to delay
      strategy revisable != transition reversible
      population recovery != repair of individual loss

   Precommit:

      B_minus_beta(a, R, Q, t, beta) -> {PASS,HOLD,INTERRUPT,RETURN,UNKNOWN}
      effective_action = resolve_beta(a, brake_result)

   Postcommit rollback is a new action and preserves a path only if executable
   before practical irreversibility.

18. Packet-use state:

      PACKET_COMPLETED != DILIGENCE_ESTABLISHED
      PACKET_CITED != MECHANISM_CHANGED
      BRAKE_REPORTED != BRAKE_INDEPENDENT

   Record packet owner, selector owner, brake owner, independent verifier,
   citation as authority, observable transition change, and repeated-case change.

19. Absence, stream, and pattern:

      NOT_OBSERVED != ABSENT
      ABSENCE_CLAIM != PROVEN_ABSENCE
      LOCAL_CORRECTION + STREAM_PERSISTENCE != MECHANISM_CHANGE

   Represent missing routes or options with a comparison basis and detector.
   Aggregate repeated transitions without inferring shared intent.

20. Unknown context:

      UNKNOWN != NEUTRAL
      CONTAMINATED_UNKNOWN != FALSE_CLAIM

   Expose control of evidence and clocks, measure-dependent delay advantage,
   delay burden, and resolution ownership.

21. Custody:

      ACCESSIBLE_EVIDENCE != SAFELY_USABLE_EVIDENCE
      INSIDER_ACCESS != SAFE_DISCLOSURE
      COURAGE_REQUIRED != ROUTE_USABLE
      HASH_MATCH != ORIGINAL_RECORD_TRUE

22. Primitive aperture and commitment receipt:

      NOT_REPRESENTED_BY_PRIMITIVE_SET != NOT_PRESENT
      COMMITMENT_RECEIPT != CLEARANCE
      PROCEEDED != RESOLVED

23. Final invariant:

      A TRACE reading should leave a capable receiver able to distinguish
      more of what is represented as present, changing, unresolved,
      possible, foreclosed, carried, and actionable than before,
      without converting representation into authority.
```

### v0.3 propagation additions

The following repairs are required to survive compression in this working
candidate. They supplement the donor kernel rather than replacing it.

```text
REPRESENTATION_TYPE != EVIDENCE_STATUS
TRIGGER_SUCCESS != REPRESENTATION_COMPLETE
REPORTED != ESTABLISHED
RECORD != EVENT
CURRENT_AT_USE != VALID_THROUGH_DEPENDENT_INTERVAL
CHECK_EXECUTED != CHECK_DETECTS_TARGET_FAILURE
SILENCE != TAMPERING
ALTERNATIVE_ROUTE_ORDERINGS != ONE_PROCESS_CYCLE
ACYCLIC_SUPPORTED != FEASIBLE_SCHEDULE_ESTABLISHED
SAME_UNIT != SAME_REFERENCE_EVENT
TARGET_BOUNDARY_TIME_REQUIRES_REPRESENTED_BOUNDARY_CONDITION
HARDENING != IRREVERSIBILITY
UNCERTAINTY != SELECT_ACTION
SAME_PATH_LABEL != SAME_TRAJECTORY
POPULATION_RECOVERY != REPAIR_OF_INDIVIDUAL_LOSS
LOCAL_CORRECTION + STREAM_PERSISTENCE != MECHANISM_CHANGE
BRAKE_POINT_ESTIMATE_BEFORE_COMMIT != GUARANTEED_PRECOMMIT
ROLLBACK_COMPLETED_BEFORE_BOUNDARY != RESTORED_STATE
HIGHEST_RELEVANCE != MEASURE_FREE
OMITTED_BY_BUDGET != IRRELEVANT
STOPPED != COMPLETED
TERMINATION != COMPLETE_COVERAGE
BUDGET_EXHAUSTED != NO_MATERIAL_UNRESOLVED_TARGET
AUTHORITY_REACHED != ANALYSIS_COMPLETE
DECLARED_REFINEMENT_COST != UNIT_COST
BUDGET_REMAINS != NEXT_REFINEMENT_AFFORDABLE
COST_UNKNOWN != COST_ONE
REFINEMENT_SELECTED != REFINEMENT_BUDGET_FEASIBLE
DECLARED_COST != VALID_POSITIVE_COST
ZERO_REFINEMENT_COST != FREE_UNBOUNDED_RECURSION
NEGATIVE_REFINEMENT_COST != BUDGET_CREDIT
COST_RECORDED != COST_DOMAIN_VALID
EMPTY_REFINEMENT_TARGET_SET != SELECTABLE_TARGET
NO_UNRESOLVED_TARGET_IN_DECLARED_SET != COMPLETE_WORLD_COVERAGE
LOCAL_REFINEMENT_EXHAUSTED != REPRESENTATION_COMPLETE
LOOP_NOT_ENTERED != RECURSION_COMPLETED
INITIAL_BUDGET_ZERO != NO_REFINEMENT_NEEDED
NEGATIVE_TRACING_BUDGET != VALID_REMAINING_BUDGET
RECURSION_SKIPPED != COMPLETE_COVERAGE
RECURSIVE_GRAPH_MERGE != RECURSIVE_LIMIT_MERGE
CHILD_GRAPH_VISIBLE != CHILD_LIMIT_VISIBLE
DEEPER_UNCERTAINTY != DISPENSABLE
GRAPH_CONTRIBUTION_SURVIVED != QUALIFYING_LIMIT_SURVIVED
CAN_SERIALIZE_LIMIT_DETAIL != LIMIT_DETAIL_SURVIVED
LIMIT_VISIBLE_IN_ANALYSIS != LIMIT_CARRIED_IN_PACKET
UNRESOLVED_CLAIM_RECORDED != LIMIT_CAUSE_RECORDED
LIMIT_TEXT_PRESENT != LIMIT_PROVENANCE_PRESERVED
SCHEMA_VALID_LIMITS != SEMANTIC_LIMIT_SURVIVAL
INTERNAL_L_MERGED != CANONICAL_PACKET_L_CARRIED
```

The same ceilings remain: this kernel is orientation, not proof, authority,
permission, clearance or a connected mechanism.

# [21] DOCUMENT CONTROL / OPEN FRONTIER

## [21.1] Working-candidate declaration

This generated object is **TRACE v0.3.0 FULL WORKING CANDIDATE v0.1**.

It is generated from the released v0.2.7 full formal seed, whose pinned source
SHA-256 is:

```text
de21182f42228a0104181fb24f245c652c3150853e14172c4174be4bb9ef03ab
```

Released v0.2.7 remains the released baseline. This file is not released,
canonical, validated, authoritative, permissive, clearance-bearing, or a claim
of world correctness.

The semantic repair source is the pinned v0.11 spine attack object:

```text
PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_11.md
semantic commit 41fafe81a681cdc6514efc13524bae6ea6d6af8d
```

The minimum schema changes version identity only; its normalized structure is
required to equal the donor minimum schema.

## [21.2] Transformation boundary

This candidate is compiled from named fail-closed transform classes. It
preserves the donor full object as the source of capability and applies bounded
v0.3 repairs for:

```text
claim/evidence firing and dependency-relative currentness
ingress/admission / representation-formation boundary
selection attribution and measurement reactivity
route/refusal and scope non-substitution
future-path correspondence use guards
correction-window target/binding/precedence/feasibility/interval discipline
record/event and residue use guards
measure-bound advantage claims
recursive analytic target-selection binding
recursive termination provenance / truncation binding
recursive declared-cost / budget-consumption binding
recursive positive-cost domain enforcement
recursive empty-target termination / coverage binding
recursive entry-budget termination / domain binding
recursive child-limit propagation
operator/checker discrimination
packet binding + load-bearing limit carrier survival without minimum-shape expansion
worked-case regression tightening
receiver-profile consistency
carrier/enforcement/brake ceilings and brake/rollback timing propagation
supplemental misuse/invariant guards
survival-kernel propagation
```

No new node type, relation type, evidence state, access state or claim kind is
declared by this working candidate.

```text
BRANCH_HEAD != SEMANTIC_OBJECT
SPINE != FULL_CANDIDATE
DONOR_RECOVERY != NEW_PRIMITIVE
FAILED_OBJECT != ERASED_OBJECT
```

## [21.3] Preserved failed ancestry

Intermediate v0.3 spine, correction-window, acyclicity, route-binding,
invariant and transform failures remain evidence in `PROJECT/` and
`falsification/`. A later candidate does not rewrite those failures as passes.

## [21.4] Open frontier / unresolved

```text
The full generated object still requires hostile coherence attack.
A deterministic compiler can faithfully compile a bad semantic rule.
No universal estimator exists for future-space, burden, residue, hardening,
  target boundaries, feasible completion, instrument adequacy or route usability.
Representation-formation challenges cannot enumerate unknown omissions.
An unavailable alternate aperture does not make the current aperture complete.
A host architecture may remove practical refusal; TRACE text cannot install it.
Instrument adequacy remains domain-specific.
A schema-valid packet can still be wrong about the world.
A completed packet can still become theatre.
A connected brake can still be captured, too slow, misconfigured or absent.
No proof establishes that TRACE improves decisions.
No stable mapping from TRACE types to latent representations is known.
TRACE cannot determine consciousness or moral standing from structure alone.
TRACE cannot generate non-instrumental care from neutral description alone.
```

## [21.5] Release boundary

Only Mark's separate release gate can change this object from working candidate
status. Compilation, CI, reviewer agreement, model agreement, packet validity,
or successful worked examples do not perform that transition.

```text
COMPILER_PASS != RELEASE
CI_GREEN != VALIDATION
AGREEMENT != CANON
DESCRIPTION != PERMISSION
```

## [21.6] Shortest preservation statement

\[
\boxed{
\tau:
\text{compressed state}
\rightarrow
\text{differentiated state}
}
\]

A system encounters TRACE.

Afterward, it may distinguish more of what is represented as present, changing,
unresolved, possible, foreclosed, carried and actionable than before, without
converting representation into authority.

That remains the bid.
