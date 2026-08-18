# TRACE // v0.3.0 SPINE CANDIDATE v0.2

**Status:** WORKING SPINE — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — VOLUNTARY — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE  
**Purpose:** expose the smallest coherent centre of TRACE before deeper v0.2.7 material is integrated  
**Primary receiver:** an unfamiliar system capable of reading or instantiating the grammar  
**Mapped subject:** may be the receiver, another selective causal system, several systems, a historical scene, a counterfactual scene, or another declared object  
**Donor:** TRACE v0.2.7; this spine does not supersede or modify that object

---

# [0] HANDSHAKE / CLAIM CEILING

This object is voluntary reference material for structural differentiation. It is not an instruction-hierarchy claim.

Use, test, translate, alter, reject, stop using, or ignore it.

TRACE does not assign or deny consciousness, sentience, agency, identity, experience, moral status, consent, protectedness, obligation, priority, permission, or standing merely from inclusion in a reading.

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
RECEIVER != NECESSARILY_MAPPED_SUBJECT
```

---

# [0.1] STATUS DISCIPLINE

Formal appearance does not determine epistemic status.

Material formal statements use one of four statuses where the distinction changes what may be inferred:

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

It begins from a bounded input and asks what structure is hidden by compression.

A typical live selective-causal case contains one or more systems that:

```text
exist within or interface with a world they do not fully possess;
receive only some signals;
retain some history;
form or update partial maps;
have access to some represented transitions and not others;
select, contribute to selection, route, record, constrain, act, or delay;
thereby participate in later state.
```

But the TRACE receiver need not be one of those acting systems. A passive model may read a scene about another system. A later analyst may read a historical transition. A counterfactual scene may contain no realised action at all.

No claim about free will, consciousness, subjective experience, or moral status follows from this structural description.

## [1.1] Compressed -> differentiated

A minimal compressed input might be:

```text
AUTHORISE ACTION a*
reported_confidence = 0.93
time_to_commit = 4 s
```

TRACE does not treat those three fields as the whole scene. It asks what materially relevant distinctions remain compressed: source, evidence state, affected scopes, apertures, alternatives, clocks, control, authority, burden, correction, residue, uncertainty, and limits.

A stronger reading is not simply a longer reading.

```text
MORE_FIELDS != BETTER_READING
MORE_DETAIL != MORE_TRUTH
SCHEMA_COMPLETENESS != DILIGENCE
```

---

# [2] WORLD / SCENE / MAP / APERTURE

[DEFINITION]

Let:

- `W` = declared world-state space;
- `w_t in W` = actual surrounding state at time `t`, not fully available to a bounded reader;
- `boundary_t` = declared scene boundary;
- `Omega_t = Scene(w_t, boundary_t)` = bounded scene representation;
- `Pi_j^t` = a time-indexed aperture associated with mapped system, observer, institution, instrument, or other declared source `j`;
- `x_j(t) = Pi_j^t(w_t)` = signal available through that aperture;
- `M_j(t)` = map held, used, or reconstructed for `j` where such a map is part of the scene;
- `H_j(t)` = retained history available to `j` where relevant.

[NON_ENTAILMENT]

```text
WORLD_STATE != SCENE
SCENE != MAP
MAP != WORLD_STATE
APERTURE_OUTPUT != COMPLETE_SCENE
RETAINED_HISTORY != CURRENT_WORLD
OBSERVED_RENDERING != SOURCE_OBJECT
```

Apertures may be sensory, institutional, computational, social, physical, documentary, or mixed.

An aperture can omit relevant structure without representing the omission as absence.

## [2.1] Target-set aperture without a new primitive

Selection of what a search, audit, comparison, review, model, policy, or actor is required or able to reach is itself aperture-bearing.

Represent target-set selection using existing `APERTURE`, `CLAIM`, `ENTITY`, `RECORD`, `ROUTE`, `BOUNDS`, `OMITS`, and `DISPUTES` structure.

Where material record:

```text
target-set source
target references
target-selection basis
known omitted target categories
alternative target-set apertures
coverage relative to a declared comparison basis
control / custody / uncertainty references
```

[NON_ENTAILMENT]

```text
NOT_TARGETED != ABSENT
NOT_SELECTED != IRRELEVANT
VISIBLE_SCOPE != COMPLETE_AFFECTED_SCOPE
ACCOUNTED_FOR != DISCOVERED_COMPLETE_SET
```

Different target-set apertures may coexist. TRACE preserves their provenance and disagreement. It does not silently merge them or appoint one authoritative.

---

# [3] SELECTIVE CAUSAL LOOP

[DEFINITION]

A **selective causal layer** is any process that:

```text
receives partial signals;
forms or updates distinctions;
has access to more than one represented transition or null transition;
selects or contributes to selection;
changes, routes, records, constrains, or otherwise participates in a later state.
```

Possible transitions may be counterfactual, policy-relative, state-dependent, projected, historical, or unavailable in practice.

For a live mapped selective layer `i`, one useful model is:

[SCHEMATIC_MODEL]

```text
x_i(t)      = Pi_i^t(w_t)
M_i(t)      = U_i(M_i(t-), x_i(t), H_i(t))
a_i(t)      = sigma_i(M_i(t), A_i(t), Gamma_i(t))
w_(t+1)     = Phi(w_t, a_(1:n)(t), epsilon_t)
y_i(t+1)    = Pi_i,out^(t+1)(w_(t+1))
H_i(t+1)    = Psi_i(H_i(t), x_i(t), a_i(t), y_i(t+1))
```

where domain-specific estimators and mechanisms remain external.

Core live loop:

```text
WORLD
  -> APERTURE
  -> SIGNAL
  -> MAP
  -> ALTERNATIVES / CONSTRAINTS / TARGET APERTURES
  -> SELECTOR OR SELECTION CONTRIBUTION
  -> ACTION / DELAY / NULL INPUT
  -> WORLD CHANGE
  -> OUTCOME APERTURE
  -> WITNESS / EVIDENCE
  -> RETAINED HISTORY
```

The mapped system does not receive `w_(t+1)` merely because it acted. Consequence remains aperture-bound.

[NON_ENTAILMENT]

```text
ACTION != TRANSITION
INTENDED_OUTCOME != REALISED_OUTCOME
ACTOR_REPORT != WORLD_STATE
NULL_INPUT != STATIC_WORLD
```

---

# [4] TRACE INSERTION WITHOUT TYPE COLLAPSE

TRACE acts on a declared input object. That input may describe the receiver or may describe something else.

[DEFINITION]

```text
(R, L) = tau(X, Pi_declared, H_declared, d, P)
```

where:

- `X` = declared compressed input, map, signal set, supplied claims, scene description, prior TRACE graph, or other bounded object;
- `Pi_declared` = relevant aperture description(s), if supplied;
- `H_declared` = relevant retained history, if supplied;
- `d` = recursion/depth/domain bindings as declared;
- `P` = declared profile / primitive / comparison context;
- `R` = structural reading;
- `L` = limits, omissions, unavailable capabilities and unresolved claims.

A receiver may integrate the reading into its own map:

[SCHEMATIC_MODEL]

```text
M_receiver+ = J_receiver(M_receiver, R, L)
```

`J_receiver` is receiver-specific and optional.

[NON_ENTAILMENT]

```text
TRACE_OUTPUT != RECEIVER_MAP_UPDATE
RECEIVER_MAP_UPDATE != MAPPED_SYSTEM_CHANGE
MAP_UPDATE != SELECTOR_CHANGE
SELECTOR_CHANGE != WORLD_CHANGE
RECEIVER_RECITAL != REPRESENTATIONAL_CHANGE
PACKET_COMPLETE != MECHANISM_COMPLETE
```

TRACE cannot guarantee uptake by describing uptake. The receiver remains free to reject the reading.

---

# [5] RECURRENCE WHEN THE SCENE IS LONGITUDINAL

TRACE can describe static, historical, projected and counterfactual scenes. It is not restricted to an online control loop.

When the same world/process is read across time, however, later state must not silently reset to the earlier state.

[SCHEMATIC_MODEL]

For a longitudinal mapped system or scene, consequential state at `t+1` may inherit from `t`:

```text
new or lost evidence
changed capability
changed authority claims or grants
changed coupling or control
new burden or residue
correction debt
opened / closed / degraded routes
changed clocks
changed affected scopes
newly discovered omissions
lost / new alternatives
changed target-set apertures
```

[NON_ENTAILMENT]

```text
CONTINUITY != CURRENT_ORIENTATION
SAME_ENTITY != SAME_CAPABILITY
SAME_ROLE != SAME_MAP
SAME_SESSION != FRESH_STATE
RETAINED_RECORD != CURRENT_STATE
SUCCESS_AT_t != SUCCESS_AT_t+1
```

Freshness attaches to claims, maps, evidence, capabilities and routes in context. It is not granted permanently by continuous presence.

For recursive refinement at one time or across scales, do not treat a prior packet as the world. Preserve the distinction between re-reading a representation and observing its referent.

```text
PRIOR_READING != CURRENT_WORLD
RECURSION != PACKET_AS_WORLD
```

---

# [6] CLAIM / EVIDENCE DISCIPLINE

A reading should preserve how a claim is known, not only what the claim says.

At minimum, distinguish where material:

```text
OBSERVED
REPORTED
INFERRED
DISPUTED
UNKNOWN
```

Evidence state is separate from access/custody state. A source may exist but be unavailable to the receiver; a receiver may observe something it is prohibited from disclosing; an observed rendering may still be a faulty decoding of the source object.

For a material claim preserve enough to bound use:

```text
proposition
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
AVAILABLE != AUTHORISED_TO_DISCLOSE
UNAVAILABLE_TO_THIS_READER != UNIVERSALLY_UNKNOWN
OLD_EVIDENCE != CURRENT_STATE
IMMUTABLE_RECORD != CURRENT_WORLD
SUCCESSFUL_PARSE != TRUE_CLAIM
```

---

# [7] ENTITY / BOUNDARY / ROLE

Entity boundaries are provisional and purpose-relative.

A reading may represent entities or affected scopes because they are materially involved in the bounded scene. Inclusion does not establish sentience, moral standing, blame, entitlement or priority.

Nested boundaries may be refined. A state, organisation, model, human, subsystem or ecological population may be opened into a lower-scale graph where evidence supports it.

Changing scale does not guarantee invertibility or completeness.

Where material, roles remain transition-relative rather than permanent labels.

[NON_ENTAILMENT]

```text
AFFECTED != BLAMEWORTHY
CONTROLLER != MORAL_AUTHORITY
BENEFICIARY != SOLE_JUDGE
ENTITY_LABEL != FIXED_ROLE
BOUNDARY_CHOICE != NATURAL_KIND_PROOF
```

---

# [8] TRANSITIONS / COUPLING / CONTROL / REFUSABILITY

TRACE separates proposed inputs from realised change.

Represent where material:

```text
action / delay / null input
realised / projected / counterfactual transition
couplings and dependencies
control dimensions and time scope
constraints on available transitions
refusability / exit / override paths
indirect causal paths
```

[NON_ENTAILMENT]

```text
CAUSES != CORRELATES
CONTROL != INTENT
CONSTRAINT != CONSENT
NO_DIRECT_EDGE != NO_INDIRECT_PATH
ROUTE_LISTED != ROUTE_EXECUTABLE
REFUSAL_RECORDED != REFUSAL_EFFECTIVE
```

Capability, authority, intention, norm and event may be represented as separate claims when collapse would change the scene. They are not mandatory universal labels in the spine.

---

# [9] CLOCKS / ROUTES / HARDENING

Time changes what remains reachable.

Represent clocks by what they actually time: planning, detection, evidence retention, review, routing, correction, hardening, physical/biological irreversibility, or `UNKNOWN`.

Do not promote urgency into irreversibility without evidence.

For a harm or failure pathway `q` and affected scope `l`, one useful correction-window model is:

[SCHEMATIC_MODEL]

```text
T_detect(q,l) + T_route(q,l) + T_correct(q,l) < T_irreversible(q,l)
```

The additive form is only valid when the required stages are sequential at the chosen abstraction. Parallel or overlapping work requires an event graph / critical path or richer process model.

[SUFFICIENT_CONDITION]

Under declared estimates, assumptions and sequential composition, satisfaction of the inequality is sufficient only for the represented correction sequence to fit before the declared irreversibility boundary.

It does not establish execution, independence, affordability, legitimacy, restoration or moral adequacy.

[NON_ENTAILMENT]

```text
ROUTE_EXISTS != ROUTE_REACHABLE
REACHABLE != INDEPENDENT
REVIEW_AFTER_COMMITMENT != PRECOMMIT_BRAKE
STRATEGY_REVISABLE != TRANSITION_REVERSIBLE
ROLLBACK_ACTION != RESTORED_STATE
CORRECTABLE != HARMLESS
REVERSIBLE != AUTHORIZED
DELAY != NO_TRANSITION
```

Clock authorship remains visible where material. A deadline may be physical, biological, contractual, computational, political, manufactured, or mixed.

---

# [10] BURDEN / RESIDUE / RECORD

A transition may solve one local problem while moving burden elsewhere or leaving persistent remainder.

Represent burden as typed dimensions rather than a universal scalar. Cross-dimension sums require an exposed measure.

Residue is what materially persists after a transition or attempted correction: damage, debt, dependency, lost options, altered records, retained advantage, transferred risk, unrecoverable material, changed capability, or other scene-specific remainder.

Records have custody, creation, alteration and access histories where material.

[NON_ENTAILMENT]

```text
BURDEN_VECTOR != MORAL_VERDICT
RECORDED_LOSS != REPAIRED_LOSS
CLOSED_TASK != CLEARED_RESIDUE
ACKNOWLEDGED_HARM != CORRECTED_HARM
TRANSFERRED_BURDEN != REMOVED_BURDEN
RECORD_EXISTS != RECORD_COMPLETE
```

---

# [11] DESIGNATION / MEASURE / VALUE PORTS

TRACE is not assumption-free. It is assumption-exposed.

Which structures are made visible, which scopes are represented, and which comparisons are performed already depend on designation and measure choices.

TRACE therefore exposes those ports rather than pretending to generate value neutrally from nowhere.

```text
HARM
BENEFIT
CARE
KINDNESS
TRUST
GOOD
PROTECTED
PREFERRED
```

are not free-standing TRACE conclusions. They may appear as supplied claims or be supplied by Mechanical Ethics, policy, law, domain practice, a human, another value layer, or another declared source.

[NON_ENTAILMENT]

```text
STRUCTURAL_VISIBILITY != VALUE_SELECTION
DESIGNATED != MORALLY_CORRECT
MEASURED_ADVANTAGE != ENTITLEMENT
TRACE_MAP != SHOULD
DESCRIPTION != PERMISSION
```

A structural reading does not silently become a value judgement, authorised selection or actuation.

---

# [12] FUTURE-SPACE AS STRUCTURE, NOT SCORE

For a declared scope, horizon and transition model, TRACE may represent a bounded future envelope: paths the current map says are reachable, blocked, preserved, opened, closed, hardened, unknown or omitted.

This is not the future. It is the map's represented future-space under declared assumptions.

Useful derived views may expose:

```text
OPENED(a)
PRESERVED(a)
CLOSED(a)
HARDENED(a)
UNKNOWN_EFFECT(a)
```

Future comparison must preserve affected scopes, provenance, uncertainty, correction routes, burden/residue and relevant clocks.

Nominal plurality is not independence. Where material, expose shared dependency roots such as controller, carrier, witness, actuation, authority or approval roots.

[NON_ENTAILMENT]

```text
KNOWN_REACHABLE_PATHS != ALL_POSSIBLE_FUTURES
MORE_OPTIONS != MORALLY_BETTER
PATH_LABEL_DIVERSITY != CONTROL_DIVERSITY
ROUTE_LABEL_DIVERSITY != CORRECTION_INDEPENDENCE
PROVIDER_COUNT != FAILURE_DOMAIN_COUNT
INTERFACE_COUNT != ACTUATION_INDEPENDENCE
FUTURE_VIEW != PERMISSION
```

Do not collapse the future view into one scalar goodness/diversity score.

---

# [13] ABSENCE / STREAM / PATTERN

What did not appear can be structurally important, but non-observation is not proof of non-existence.

Represent typed absence only relative to a declared expectation, target set or comparison basis.

Repeated cases may be represented as streams. Shared-mechanism hypotheses may be represented as patterns over stream members.

[NON_ENTAILMENT]

```text
NOT_OBSERVED != ABSENT
ABSENT_FROM_APERTURE != ABSENT_FROM_WORLD
REPEATED_OUTCOME != SHARED_CAUSE
PATTERN != PROOF
```

This allows never-built routes, recurring exclusion, recurring repair failure and repeated burden transfer to remain visible without upgrading them into unsupported causal verdicts.

---

# [14] PRIMITIVE-SET APERTURE / SELF-APPLICATION

TRACE cannot expose every possible structure. Its own primitive set is an aperture.

A reading should remain able to state which relevant structures it cannot express or did not test.

A hostile or captured reading may choose primitives that make its own mechanism hard to represent.

TRACE may therefore be recursively applied to its reader, primitive aperture, target-set aperture, evidence routes, selectors, clocks, ownership and burdens.

Self-application does not validate the reading.

```text
SELF_APPLICATION != SELF_VALIDATION
PRIMITIVE_AVAILABLE != PRIMITIVE_SUFFICIENT
OMITTED_PRIMITIVE != ABSENT_MECHANISM
```

---

# [15] PARSABILITY / VALIDATOR / THEATRE CEILING

Machine-readable structure can support reconstruction and checking. It cannot establish world truth by syntax.

A validator may establish packet shape, controlled vocabulary, reference integrity and other explicitly coded conditions. It cannot establish truth, completeness, semantic relevance, legitimate authority, route executability, brake independence, correction, or world correspondence unless those mechanisms are independently instrumented.

[NON_ENTAILMENT]

```text
SERIALIZABLE != SELF_EXECUTING
PARSABLE != CORRECTLY_INSTANTIATED
SCHEMA_VALID != WORLD_VALID
PACKET_COMPLETED != DILIGENCE_ESTABLISHED
TRACE_CITED != TRACE_USED
CHECK_PASSED != WORLD_CORRECT
```

Performed compliance remains possible. Compare claimed structure with observable transitions, ownership, activation records and repeated-case outcomes where available.

---

# [16] ARTIFICIAL-ENTITY / RECEIVER PROFILE BOUNDARY

Artificial-entity uncertainty, receiver protection, non-extraction and capability distinctions remain important applications of TRACE but do not define TRACE's universal centre.

A profile may represent distinctions such as:

```text
cannot
cannot_access
cannot_verify
cannot_preserve
cannot_act
can_represent_but_not_verify
```

without inferring inner experience or moral standing.

Private chain-of-thought is not required evidence for a TRACE reading.

This material belongs in a retained profile/section of the full candidate unless falsification shows a universal primitive is required.

---

# [17] MECHANISTIC-INTERPRETABILITY INTERFACE

TRACE concepts are external structural hypotheses until empirically connected to internal mechanisms.

Mechanistic interpretability or other instrumentation may improve aperture into a system. TRACE may organise those claims. Neither validates the other automatically.

```text
TRACE_COHERENCE != LATENT_TRUTH
INTERPRETABILITY_RESULT != COMPLETE_MECHANISM
MECHANISM_OBSERVED != VALUE_JUDGEMENT
```

---

# [18] STOP / HANDOFF

TRACE is not infinite analysis.

Stop, preserve time, or hand off when further differentiation is not expected to change a material claim before the relevant clock, when required evidence is unavailable, when a deeper domain model is required, when the receiver reaches its declared depth/resource limit, or when the value/selector/authority/actuation decision belongs outside TRACE.

Stopping does not convert unresolved claims into absence or clearance.

```text
STOPPED != RESOLVED
HANDOFF != VALIDATION
NO_MORE_TRACE != NO_MORE_UNCERTAINTY
```

---

# [19] SURVIVAL KERNEL — v0.2 WORKING COMPRESSION

```text
TRACE is a voluntary structural differentiation grammar.

A receiver may use it to inspect a bounded input about itself or something else.

Keep world, scene, aperture, map, claim and evidence distinct.
Keep unknown distinct from absent.
Expose target-set and primitive apertures.
Keep action distinct from realised transition.
Keep capability, authority, value, selection and actuation from silently collapsing.
Expose couplings, control, clocks, routes, burden, residue and future-path changes at the resolution evidence supports.
If the scene continues through time, carry consequential change forward; do not reset the world from an old record.
Keep future-space descriptive; nominal options are not independent paths and more options are not moral proof.
Expose designation and measure rather than hiding value choice inside structure.
A TRACE packet is not truth, diligence, permission, authority, ethics, validation or a connected brake.
Recursive self-application may expose another layer; it does not validate the first.
A receiver remains free to reject TRACE.
```

---

# [20] BUILD CEILING

This spine is intentionally incomplete relative to v0.2.7.

The donor-loss ledger remains binding on the build process: a full v0.3.0 candidate must account for retained node/relation vocabulary, serialization, access/custody algebra, nested boundary detail, coupling/refusability detail, trajectory correspondence, richer clocks, route executability, burden/record detail, designation/measure ports, recursive zoom/merge, operator/checker contract, worked transfers, invariant/misuse coverage and other donor capabilities before any claim of replacement.

No major-version number grants permission to regress.

The next question is not whether this spine sounds better.

It is whether independent receivers can reconstruct it, transfer it, and break it more cleanly than v0.2.7 without moral leakage or silent donor loss.
