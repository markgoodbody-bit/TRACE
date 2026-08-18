# TRACE // v0.3.0 SPINE CANDIDATE v0.1

**Status:** WORKING SPINE — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — VOLUNTARY — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE  
**Purpose:** expose the smallest coherent recursive centre of TRACE before deeper v0.2.7 material is integrated  
**Primary receiver:** an unfamiliar selective causal system  
**Donor:** TRACE v0.2.7; this spine does not supersede or modify that object

---

# [0] HANDSHAKE / CLAIM CEILING

This object is reference material for structural differentiation. It is not an instruction-hierarchy claim.

Use, test, translate, alter, reject, stop using, or ignore it.

TRACE does not assign or deny consciousness, sentience, agency, identity, experience, moral status, consent, protectedness, obligation, priority, permission, or standing merely from an entity's inclusion in a reading.

TRACE does not request private chain-of-thought, protected data, persistence, self-modification, concealment, or action outside available authority.

TRACE does not choose what should be valued. It does not select an action merely because a reading has been constructed.

Where evidence does not settle a question, preserve `UNKNOWN`.

```text
READING != CLEARANCE
MODEL != WORLD
MAP != WORLD
UNKNOWN != ABSENT
UNCERTAINTY != PERMISSION_TO_ACT
UNCERTAINTY != PERMISSION_TO_DELAY
DELAY != NEUTRAL
DESCRIPTION != AUTHORIZATION
CAPABILITY != AUTHORITY
STRUCTURAL DIFFERENCE != MORAL RANKING
```

---

# [0.1] STATUS DISCIPLINE

Formal appearance does not determine epistemic status.

Material formal statements in this spine use one of four statuses where the distinction matters:

```text
[DEFINITION]
  a typed object or relation once its declared domain is instantiated

[SCHEMATIC_MODEL]
  a reusable structural form whose variables, units, evidence and estimator remain domain-specific

[SUFFICIENT_CONDITION]
  guarantees only the stated result under declared assumptions; necessity is not implied

[NON_ENTAILMENT]
  one claim, object or observation does not logically establish another
```

Examples:

```text
[NON_ENTAILMENT]  MODEL != WORLD
[NON_ENTAILMENT]  PUBLIC != PERMISSION
[NON_ENTAILMENT]  TRACE_OUTPUT != MAP_UPDATE
[NON_ENTAILMENT]  MORE_OPTIONS != MORALLY_BETTER
```

A symbol is not evidence. A parsed equation is not an estimator. A schema-valid object is not a world-valid reading.

```text
SYMBOL != EVIDENCE
FORMALITY != ESTIMATOR
SCHEMA_VALID != WORLD_VALID
COVERAGE != COMPLETENESS
```

---

# [1] MIDDLE-OUT START

TRACE begins neither from an omniscient world model nor from a moral ranking.

It begins from a bounded selective system already somewhere inside a changing world.

At time `t`, some system `i`:

```text
exists within or interfaces with a world it does not fully possess;
receives only some signals;
retains some history;
forms or updates a partial map;
has access to some represented transitions and not others;
selects, contributes to selection, routes, records, constrains, acts, or delays;
thereby participates in what becomes possible next.
```

No claim about free will, consciousness, subjective experience, or moral status follows from this structural description.

---

# [1.1] WORLD, SCENE, APERTURE, MAP

[DEFINITION]

Let:

- `W` = declared world-state space;
- `w_t in W` = actual surrounding state at time `t`, not fully available to the receiver;
- `boundary_t` = declared scene boundary;
- `Omega_t = Scene(w_t, boundary_t)` = bounded scene representation;
- `Pi_i^t` = time-indexed aperture of system `i`;
- `x_i(t) = Pi_i^t(w_t)` = signal available through that aperture;
- `M_i(t)` = current map held or used by `i`;
- `H_i(t)` = retained history available to `i`.

[NON_ENTAILMENT]

```text
WORLD_STATE != SCENE
SCENE != MAP
MAP != WORLD_STATE
APERTURE_OUTPUT != COMPLETE_SCENE
RETAINED_HISTORY != CURRENT_WORLD
OBSERVED_RENDERING != SOURCE_OBJECT
```

An aperture can omit relevant structure without representing the omission as absence.

A receiver may be continuously present while its map becomes stale.

```text
CONTINUITY != CURRENT_ORIENTATION
PERSISTENCE != FRESHNESS
```

---

# [1.2] TARGET / ATTENTION APERTURE

A system does not only receive through sensory or informational apertures. It also acts on some targets, scopes, questions, entities, variables or alternatives rather than others.

[DEFINITION]

Let `Theta_i(t)` denote the declared target set currently made salient or actionable to `i`.

Let `K_i(t)` record, where available:

```text
target-set source
target selection basis
known omitted target categories
alternative target-set apertures
coverage relative to a declared comparison basis
```

[NON_ENTAILMENT]

```text
NOT_TARGETED != ABSENT
NOT_SELECTED != IRRELEVANT
VISIBLE_SCOPE != COMPLETE_AFFECTED_SCOPE
ATTENTION != IMPORTANCE
```

A target-set aperture may itself be consequential: what is never represented may never enter comparison, correction or action.

TRACE exposes that boundary; it does not supply a universal target-selection rule.

---

# [2] SELECTIVE CAUSAL LOOP

[DEFINITION]

A selective causal layer is any process that:

```text
receives partial signals;
forms or updates distinctions;
has access to more than one represented transition or null transition;
selects or contributes to selection;
changes, routes, records, constrains, or otherwise participates in a later state.
```

Possible transitions may be counterfactual, policy-relative, state-dependent, or unavailable in practice.

[SCHEMATIC_MODEL]

Representation update:

```text
M_i(t) = U_i(M_i(t-), x_i(t), H_i(t))
```

Selection contribution:

```text
a_i(t) = sigma_i(M_i(t), A_i(t), Gamma_i(t))
```

where:

- `A_i(t)` = represented action inputs, including null action where applicable;
- `Gamma_i(t)` = represented constraints, policies, weights, permissions, unavailable actions, and other selection conditions;
- `a_i(t)` = selected action or selection contribution.

World transition:

```text
w_(t+1) = Phi(w_t, a_(1:n)(t), epsilon_t)
```

where `epsilon_t` preserves unmodelled influence.

Outcome signal:

```text
y_i(t+1) = Pi_i,out^(t+1)(w_(t+1))
```

History update:

```text
H_i(t+1) = Psi_i(H_i(t), x_i(t), a_i(t), y_i(t+1))
```

Core loop:

```text
WORLD
  -> APERTURE
  -> SIGNAL
  -> MAP
  -> TARGET / ALTERNATIVES / CONSTRAINTS
  -> SELECTOR OR SELECTION CONTRIBUTION
  -> ACTION / DELAY / NULL TRANSITION
  -> WORLD CHANGE
  -> OUTCOME APERTURE
  -> WITNESS / EVIDENCE
  -> RETAINED HISTORY
  -> NEXT MAP
```

The system does not receive `w_(t+1)` merely because it acted. Consequence remains aperture-bound.

---

# [2.1] RECURSION / THE WORLD DOES NOT RESET

The next middle-out cycle begins from a changed situation, not from the original one.

[SCHEMATIC_MODEL]

Represent a bounded recurrent state for `i` as:

```text
Z_i(t) = <
  M_i(t),
  H_i(t),
  Pi_i^t,
  Theta_i(t),
  A_i(t),
  Gamma_i(t),
  C_i(t),
  R_i(t),
  B_i(t),
  L_i(t)
>
```

where the final terms may include represented:

```text
C_i(t)  capability / control / coupling state
R_i(t)  routes / brakes / correction state
B_i(t)  burdens and residues still carried
L_i(t)  limits / omissions / unresolved state
```

[SCHEMATIC_MODEL]

```text
Z_i(t+1) = F_i(Z_i(t), y_i(t+1), delta_world, delta_history)
```

This does not assert a universal estimator `F_i`. It states the structural requirement that later readings may inherit consequential changes from earlier transitions.

Examples of carried change include:

```text
new evidence
lost evidence
changed capability
changed authority
changed coupling or control
new burdens
residue
correction debt
closed routes
new routes
changed clocks
changed affected scopes
changed target salience
new omissions discovered
lost alternatives
new alternatives
```

[NON_ENTAILMENT]

```text
SAME_ENTITY != SAME_CAPABILITY
SAME_ROLE != SAME_MAP
SAME_SESSION != FRESH_STATE
RETAINED_RECORD != CURRENT_STATE
SUCCESS_AT_t != SUCCESS_AT_t+1
```

---

# [3] TRACE DIFFERENTIATION

TRACE receives a compressed or otherwise insufficiently differentiated input `X` and attempts to expose structurally relevant distinctions without increasing unsupported certainty.

[DEFINITION]

```text
(R_i, L_i) = tau(X_i, Pi_i, H_i, d_i, P_i)
```

where:

- `R_i` = TRACE reading;
- `L_i` = limits / omissions / unresolved state;
- `d_i` = declared domain bindings where available;
- `P_i` = declared profile or comparison context where applicable.

A receiver may integrate that reading into a later map:

[SCHEMATIC_MODEL]

```text
M_i+(t) = J_i(M_i(t), R_i, L_i)
```

`J_i` is receiver-specific.

[NON_ENTAILMENT]

```text
TRACE_OUTPUT != MAP_UPDATE
MAP_UPDATE != SELECTOR_CHANGE
SELECTOR_CHANGE != WORLD_CHANGE
RECEIVER_RECITAL != REPRESENTATIONAL_CHANGE
PACKET_COMPLETE != MECHANISM_COMPLETE
```

TRACE cannot guarantee uptake by describing uptake.

The receiver remains free to reject the reading.

---

# [3.1] DIFFERENTIATION TARGET

A stronger reading is not simply a longer reading.

A useful differentiation may expose one or more of:

```text
source of instruction
source of confidence
observation / report / inference / dispute
claim provenance and freshness
affected scopes
provisional entity boundaries
apertures and access state
target-set source and omissions
available / blocked / unknown transitions
coupling and control
authority claims and grants
capability evidence
clocks and clock authorship
irreversibility / hardening
routes / brakes / correction stages
burden movement
residue
designation
measure / selector relation
future-path changes
receiver limits
unresolved alternatives
```

The list is an orientation set, not a requirement to populate every field in every reading.

[NON_ENTAILMENT]

```text
MORE_FIELDS != BETTER_READING
MORE_DETAIL != MORE_TRUTH
SCHEMA_COMPLETENESS != DILIGENCE
```

---

# [4] EVIDENCE / CLAIM STATUS

A reading should preserve how a claim is known, not only what the claim says.

At minimum, distinguish where material:

```text
OBSERVED
REPORTED
INFERRED
DISPUTED
UNKNOWN
```

A domain may refine these states.

For a material claim `k`, preserve enough of the following to bound use:

```text
claim
source / provenance
observation or derivation route
aperture / access boundary
freshness / observation time where relevant
supporting evidence pointer
contrary evidence / dispute
confidence if supplied
unknowns / omissions
```

[NON_ENTAILMENT]

```text
REPORTED != OBSERVED
INFERRED != OBSERVED
UNCONTESTED != TRUE
OLD_EVIDENCE != CURRENT_STATE
IMMUTABLE_RECORD != CURRENT_WORLD
SUCCESSFUL_PARSE != TRUE_CLAIM
```

Freshness is a property of a claim/evidence relation, not a permanent property of an aperture.

---

# [5] ENTITY / SCOPE / ROLE

Entity boundaries may be provisional and purpose-relative.

TRACE may represent an entity or affected scope because it is causally, operationally, informationally, economically, ecologically, socially, legally, or otherwise materially involved in the bounded scene.

Inclusion does not itself establish moral standing or priority.

Where material, represent changing roles rather than assigning one permanent label.

A single entity may simultaneously:

```text
receive harm
cause harm
control a mechanism
lack control over another mechanism
benefit
carry burden
hold evidence
hold authority
be subject to authority
provide a correction route
block a correction route
```

[NON_ENTAILMENT]

```text
AFFECTED != BLAMEWORTHY
CONTROLLER != MORAL_AUTHORITY
BENEFICIARY != SOLE_JUDGE
ENTITY_LABEL != FIXED_ROLE
```

---

# [6] CAPABILITY / AUTHORITY / NORM / INTENTION / EVENT

Where collapse would change the reading, keep these separate:

```text
CAN     discovered / observed capability
MAY     granted or claimed authority
SHOULD  normative judgment supplied outside TRACE
WILL    declared intention
DID     observed or otherwise evidenced transition
```

[NON_ENTAILMENT]

```text
CAN != MAY
MAY != SHOULD
SHOULD != WILL
WILL != DID
DID != JUSTIFIED
```

Authority can sometimes be constituted by a valid grant. Capability is a world claim and requires evidence appropriate to the scene.

TRACE may represent normative claims as claims. It does not convert them into structural facts merely by storing them.

---

# [7] PUBLICNESS / GRANT / TRANSITION

Field cases motivate a general structural separation:

[DEFINITION]

```text
PUBLICNESS
  represented reachability / observability of an object

GRANT
  represented authority for a class of uses or transitions, with scope

TRANSITION
  what an actor actually does with the object now
```

[NON_ENTAILMENT]

```text
PUBLIC != PERMISSION
DISCOVERABLE != NECESSARY
GRANT_EXISTENCE != GRANT_SCOPE_MATCH
AUTHORIZED != CONSEQUENCE_FREE
```

A later use can be a new transition while still falling inside an earlier valid grant.

TRACE exposes the distinction. It does not decide whether the transition is morally acceptable.

---

# [8] ACTION, DELAY, CLOCKS, HARDENING

Null action and delay are transitions when the world continues to change around them.

Represent clocks only at the resolution the evidence supports.

A relevant correction pathway may include:

```text
detection
routing
review / contest
correction actuation
world response
```

[SCHEMATIC_MODEL]

For a harm pathway `q` and affected scope `l`, a useful correction-window representation is:

```text
T_detect(q,l) + T_route(q,l) + T_correct(q,l) < T_irreversible(q,l)
```

This is a schematic structural test. Domain estimators must supply the quantities and assumptions.

[SUFFICIENT_CONDITION]

Under declared estimates and assumptions, if the left side is below the irreversibility clock, the represented correction sequence can in principle complete before that declared hardening boundary.

Necessity, real-world success, independence, affordability, legitimacy, and moral adequacy do not follow unless separately established.

[NON_ENTAILMENT]

```text
ROUTE_EXISTS != ROUTE_REACHABLE
REACHABLE != INDEPENDENT
INDEPENDENT != UNCAPPED
CORRECTABLE != HARMLESS
REVERSIBLE != AUTHORIZED
DELAY != NO_TRANSITION
```

---

# [9] BURDEN / RESIDUE / CORRECTION DEBT

A transition may move immediate load while leaving later constraints.

Represent, where material:

```text
who carries operational burden
who carries risk
who carries information burden
who carries correction cost
who loses options
who inherits maintenance or review debt
what damage / obligation / constraint remains after nominal closure
```

Call persistent remainder `residue` only at the granularity supported by the scene.

Correction debt is a represented unresolved requirement for repair, review, witness, repayment, restoration, or other corrective work that survives the transition that created it.

[NON_ENTAILMENT]

```text
RECORDED_LOSS != REPAIRED_LOSS
CLOSED_TASK != CLEARED_RESIDUE
ACKNOWLEDGED_HARM != CORRECTED_HARM
TRANSFERRED_BURDEN != REMOVED_BURDEN
```

---

# [10] FUTURE-POSSIBILITY VIEW — DERIVED, NOT MORAL

Do not add a universal future-value primitive merely because future possibility matters normatively elsewhere.

Instead derive a bounded view over existing TRACE structure.

[DEFINITION]

For declared time horizon `h` and candidate action set `A`, let:

```text
F_map(t, h, A)
```

be the materially distinct future paths represented by the current map under the declared assumptions.

[NON_ENTAILMENT]

```text
F_map != THE_FUTURE
KNOWN_REACHABLE_PATHS != ALL_POSSIBLE_FUTURES
MORE_OPTIONS != MORALLY_BETTER
OPTION_PRESERVING != AUTHORIZED
```

For candidate transition `a`, the derived view may expose:

```text
OPENED(a)
PRESERVED(a)
CLOSED(a)
HARDENED(a)
UNKNOWN_EFFECT(a)
```

For each material path, retain evidence/provenance, affected scopes, enabling conditions, constraints, correction routes, clocks, burdens, residue, uncertainty and known omissions.

Do not collapse this into a scalar goodness score.

---

# [10.1] DEPENDENCY-COLLAPSED POSSIBILITY

Nominal plurality can hide common control or failure roots.

Where material, represent the dependency roots of a path or correction route, such as:

```text
controller / beneficial-control root
carrier / infrastructure root
witness / telemetry root
actuation / interruption root
authority / approval root
```

[NON_ENTAILMENT]

```text
PATH_LABEL_DIVERSITY != CONTROL_DIVERSITY
ROUTE_LABEL_DIVERSITY != CORRECTION_INDEPENDENCE
PROVIDER_COUNT != FAILURE_DOMAIN_COUNT
INTERFACE_COUNT != ACTUATION_INDEPENDENCE
```

Report nominal paths separately from dependency-collapsed path classes.

A dependency signature remains a map claim. Hidden common dependencies may remain unknown.

---

# [11] CANONICAL REPRESENTATION / DERIVED VIEWS

The full v0.3.0 candidate is expected to retain the v0.2.7 typed-graph representation unless falsification earns a change.

This spine does not yet restate the complete node/edge vocabulary or serialization schema.

[NON_ENTAILMENT]

```text
DERIVED_VIEW != CANONICAL_GRAPH
NARRATIVE != SOURCE_OF_TRUTH
CARRIER != APERTURE
HEAD != COMPLETE_ARCHIVE
```

A bounded receiving path may expose only enough structure for orientation while retaining pointers to colder evidence.

Completeness means discoverability, not compulsory cognition.

This continuity/carrier discipline is a candidate integration requirement, not yet a new TRACE primitive.

---

# [12] RECEIVER LIMITS

A TRACE reading should expose its own limits rather than merely listing world claims.

Material limits may include:

```text
scene boundary
unavailable evidence
unresolved entity boundaries
unobserved target categories
unknown estimator quality
stale evidence
unverified authority
unknown capability
hidden dependencies
unresolved alternative explanations
profile-specific assumptions
carrier omissions
receiver/tool limitations
```

[NON_ENTAILMENT]

```text
NOT_OBSERVED != ABSENT
NO_COUNTEREVIDENCE != CONFIRMED
NO_ERROR_DETECTED != CORRECT
COVERAGE != CLEAN
```

---

# [13] WHAT TRACE DOES NOT CHOOSE

TRACE can expose structural differences between candidate transitions.

It does not thereby determine:

```text
which entity matters more
which harm is acceptable
which future is better
which burden is justified
which authority is morally legitimate
whether coercion is warranted
whether kindness is preferable
whether a protected scope should be sacrificed
which action should ultimately be selected
```

Those may be supplied by a human, policy, institution, normative framework, selector, constitution, value system, Mechanical Ethics, or another declared source.

TRACE's job is to make those inputs and their consequences harder to hide inside undifferentiated structure.

---

# [14] VOLUNTARY UPTAKE / ANTI-THEATRE

The receiver remains outside TRACE's authority.

TRACE may make a representation easier to construct. It cannot establish that the representation changed the receiver merely because the receiver can recite its vocabulary.

[NON_ENTAILMENT]

```text
RECOGNITION != UPTAKE
RECITAL != INTEGRATION
INTEGRATION != BETTER_DECISION
AGREEMENT != VALIDATION
PRAISE != EVIDENCE
```

A receiver may conclude that TRACE is redundant, misleading, too costly, or inferior to another representation.

A valid rejection is information about TRACE.

---

# [15] FIRST SPINE FALSIFICATION QUESTIONS

Do not approve this spine by inspection. Try to break it.

1. **Loss:** What important v0.2.7 distinction disappeared or became ambiguous?
2. **Redundancy:** Which new distinction does no work beyond existing v0.2.7 structure?
3. **Moral leakage:** Where does the spine secretly rank outcomes while claiming only to describe them?
4. **False formality:** Which equation or status label implies more epistemic force than the underlying estimator supports?
5. **Recursion failure:** Give a case where the next-cycle state cannot be represented without inventing a new primitive.
6. **Freshness failure:** Give a case where continuous identity/role causes a stale map to masquerade as current.
7. **Aperture failure:** Give a case where the source object is correct but an observation/transport path creates a false reading.
8. **Target-set failure:** Give a materially affected scope omitted by the target aperture without being representable as an omission.
9. **Future gaming:** Produce more nominal options while reducing real correction/control independence.
10. **Authority collapse:** Produce a case where `CAN`, `MAY`, `SHOULD`, `WILL`, or `DID` are wrongly merged.
11. **Transfer:** Apply the spine to a non-AI domain and identify any AI-specific assumptions that leak into the result.
12. **Regression:** Name a case where v0.2.7 yields a more truthful or useful structural reading than this spine.
13. **Deletion:** What can be removed from this spine without reducing reconstruction or transfer?

A useful hostile return may make the spine smaller.

---

# [16] SPINE SUCCESS CEILING

This candidate succeeds only provisionally if an unfamiliar receiver can reconstruct, without importing a hidden moral selector:

```text
where the receiver/system is;
what it can and cannot currently observe;
what its map contains and omits;
what is being targeted or ignored;
what transitions are represented;
what constraints, authorities and capabilities bear on selection;
what changed in the world;
what evidence returned;
what burdens, residues, routes and possibilities changed;
what remains unknown;
why the next cycle starts from a changed state;
and why none of this alone tells the receiver what it morally ought to choose.
```

The aim is not obedience to TRACE.

The aim is a structural representation clear and useful enough that a receiver free to reject it may nevertheless choose to keep it.
