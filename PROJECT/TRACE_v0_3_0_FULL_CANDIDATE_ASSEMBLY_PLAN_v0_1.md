# TRACE v0.3.0 — FULL-CANDIDATE ASSEMBLY PLAN v0.1

**Status:** WORKING BUILD PLAN — NOT FULL CANDIDATE — NOT RELEASE — NOT CANON — NOT VALIDATED  
**Assembly direction:** released v0.2.7 full object -> declared v0.3 repairs  
**Do not assemble from the short spine as replacement source.**

---

## 0. Frozen inputs

### Released donor object

```text
repository: markgoodbody-bit/TRACE
commit: 4694ff57bb5d8cdd3a361ba34eeedfefc0ce0b26
file: TRACE_FORMAL_SEED_v0_2_7.md
blob: 9238986ddc18c34709906b2fc4510d827c68d2b2
```

Released v0.2.7 remains the capability donor and regression oracle.

### Current semantic overlay

```text
file: PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_11.md
semantic commit: 41fafe81a681cdc6514efc13524bae6ea6d6af8d
blob: 1ae5e8b8640b9506db585599a6cae5192087d870
bytes: 25,355
status: WORKING / ATTACK OBJECT
```

The spine is an earned semantic overlay / compression surface. It is **not** the full-object donor.

### Minimum-schema boundary

```text
file: PROJECT/TRACE_v0_3_0_MINIMUM_SCHEMA_CANDIDATE_v0_1.json
```

Its deterministic build witness establishes that after four version-identity leaves are normalized, the minimum schema equals released v0.2.7's embedded schema.

No node, relation, claim-kind, evidence-state, access-state, required packet property, required port role or required discipline block has been earned as a schema change.

### Donor-accounting surfaces

```text
PROJECT/TRACE_v0_2_7_TO_v0_3_0_DONOR_MAP_v0_1.md
PROJECT/TRACE_v0_3_0_INVARIANT_SEMANTIC_DISPOSITION_v0_2.md
PROJECT/TRACE_v0_3_0_INVARIANT_LEXICAL_COVERAGE_v0_4.json
```

---

## 1. Assembly invariant

The full v0.3 working candidate begins as a deterministic transformation of the released v0.2.7 full object.

```text
FULL_v0.3 = TRANSFORM(RELEASED_FULL_v0.2.7, DECLARED_REPAIRS)
```

Not:

```text
FULL_v0.3 = EXPAND(SPINE_v0.11, remembered donor fragments)
```

Why:

```text
SPINE != SCHEMA
SPINE != FULL_CANDIDATE
COMPRESSION_OMISSION != DONOR_DELETION_PERMISSION
MEMORY_OF_DONOR != DONOR_OBJECT
```

Every donor byte/section survives unless one of the following is explicit:

```text
UNCHANGED
VERSION_IDENTITY_ONLY
REPLACED_BY_DECLARED_REPAIR
MOVED_WITH_EXACT_CAPABILITY_MAP
DELETED_WITH_REDUNDANCY_PROOF
```

No silent deletion class exists.

---

## 2. Build strategy

Create a deterministic full-candidate compiler rather than hand-editing a new long seed.

Proposed tool:

```text
tools/compile_trace_v030_full_candidate.py
```

Compiler contract:

1. read exact released `TRACE_FORMAL_SEED_v0_2_7.md` donor;
2. verify donor SHA-256 / blob identity expected by the build;
3. update document/machine version identity to v0.3.0 only where declared;
4. apply a finite, named set of exact-anchor semantic transformations;
5. preserve untouched donor text byte-for-byte;
6. extract/insert the v0.3 minimum-schema candidate rather than hand-rewriting schema JSON;
7. emit a build manifest listing every changed donor surface;
8. fail if an anchor count differs from expectation;
9. fail if controlled vocabulary or required packet structure changes without an admitted schema delta;
10. provide a reverse/normalization witness for every transformation class that is intended to be donor-preserving.

```text
DETERMINISTIC_BUILD != SEMANTIC_VALIDATION
DECLARED_TRANSFORM != JUSTIFIED_TRANSFORM
```

The compiler makes change visible; falsification still decides whether the change survives.

---

## 3. Preserve donor architecture first

Carry forward the released full-object architecture before integrating v0.11 deltas:

```text
[0]    handshake / claim ceiling
[0.1]  formal-status legend
[1]    concrete middle-out seed + structural comparison discipline
[2]    selective causal loop / receiver-specific TRACE insertion
[3]    canonical graph, vocabularies, relation discipline, glyphs, serialization
[3.5]  primitive-set aperture
[3.6]  absence / stream / pattern
[4]    full claim/evidence/access/custody algebra
[5]    entity/boundary/aperture/state including nested boundaries
[6]    transitions/coupling/refusability/null-action symmetry
[7]    future-space and comparison/correspondence discipline
[8]    clocks/routes/hardening/correction machinery
[9]    burden/residue/record/custody
[10]   designation/measure/value ports and explicit layer handoff
[11]   recursive zoom/merge/stop discipline
[12]   structural-awareness comparison with its scalar/global ceilings
[13]   TRACE operator/pseudocode/non-command output/parsability ceiling
[14]   canonical packet / profiles / binding rules / use boundary / receipt / validator
[15]   worked transformations
[16]   artificial-entity/receiver profiles and non-extraction
[17]   live interpreter / selector / carrier / enforcement / brake / rollback
[18]   mechanistic-interpretability interface
[19]   invariant + misuse suite
[20]   survival kernel
[21]   revision/document-control/unresolved register/layer relationship
```

A v0.11 repair may tighten these sections. It does not make the untouched capabilities optional.

---

## 4. Integrate v0.11 as use-rule repairs, not a parallel ontology

The full candidate must import the semantic repairs that survived the current spine attacks.

At minimum, integrate the following into their corresponding donor sections:

### Claim / evidence / firing

```text
REPRESENTATION_TYPE != EVIDENCE_STATUS
CONFIGURATION_FIELD != WARRANT_FREE_FACT
LOAD_BEARING_UNKNOWN != NOT_LOAD_BEARING
REPORTED != ESTABLISHED
RECORD != EVENT
EVIDENCE_STATE != ACCESS_CUSTODY_STATE
UNAVAILABLE_TO_THIS_READER != UNIVERSALLY_UNKNOWN
AVAILABLE != AUTHORISED_TO_DISCLOSE
```

### Verification / liveness

```text
CHECK_EXISTS != CHECK_EXECUTED
CHECK_EXECUTED != CHECK_DETECTS_TARGET_FAILURE
STATIC_CORRECTNESS != OPERATIONAL_DISCRIMINATION
CHECK_COMPLETED != CHECK_RESULT_REACHED_USE
WITNESS_LIVENESS_LOST != CAUSE_ESTABLISHED
EXTERNAL != INDEPENDENT
```

### Transition / route / scope

```text
ROUTE_EXISTS != ROUTE_USABLE
REFUSAL != MALFUNCTION
STRATEGY_REVISABLE != TRANSITION_REVERSIBLE
POPULATION_RECOVERY != REPAIR_OF_INDIVIDUAL_LOSS
```

### Selection attribution

```text
UNCERTAINTY != SELECT_ACTION
UNCERTAINTY != SELECT_DELAY
UNCERTAINTY_INPUT_TO_POLICY != UNCERTAINTY_IS_SELECTOR
IMPLICIT_DEFAULT != NO_SELECTION_RULE
```

### Correction-window / timing

```text
E_prec = derived timing/process view, not canonical relation
source/provenance retained on every load-bearing derived ordering
one executable pathway/route hypothesis per critical-path view
mutually exclusive route orderings are not unioned
recurring event occurrences remain distinguishable where timing depends on occurrence
precedence view must be acyclic for critical-path proof
acyclicity does not establish execution feasibility
required verification time is not free
common temporal basis before comparison
explicit target-boundary condition + selector/source/basis
route/capability-relative unattainability != world irreversibility
strong window status rebinds when load-bearing target/boundary/capability/time/process/execution changes
```

### Hardening / burden / recurrence

```text
HARDENING != IRREVERSIBILITY
LOCAL_CORRECTION + STREAM_PERSISTENCE != MECHANISM_CHANGE
LOCAL_CASE_REPAIRED != GENERATING_MECHANISM_REPAIRED
STREAM_PERSISTENCE != SAME_MECHANISM_PROVEN
ADVANTAGE_CLAIM_REQUIRES_MEASURE
```

No repair above currently earns a new node/relation/state/root.

---

## 5. Seven full-candidate invariant obligations

The short spine deliberately leaves seven donor guards to full-object machinery. Assembly must discharge them explicitly, not merely retain their text in I01–I60.

### I12 — `REVIEW_AFTER_COMMITMENT != BRAKE`

Carry forward donor precommit-brake vs postcommit rollback/review phase separation.

Required capability:

```text
precommit interruption != postcommit review
rollback action != proof original state/path was preserved
```

Expected donor surfaces: clock/action-load/precommit-brake material plus [17] live brake/rollback machinery.

### I19 — `COMPLEXITY != AWARENESS`

Carry forward [12] structural-awareness comparison as a declared-criteria comparison discipline, including `UNKNOWN/INCOMPARABLE` and the ceiling against treating more structure/complexity as a global awareness scalar.

Do not allow the v0.3 firing improvements to become a claim of consciousness or universal awareness measurement.

### I26 — `VISIBILITY != CARRYING`

Carry forward canonical CARRIER semantics and port state. A visible/recorded reading is not thereby persistent, costly, consequential, or delivered beyond the moment of description.

### I27 — `CARRYING != ENFORCEMENT`

Carry forward ENFORCER semantics and authority separation. Persistence/consequence of a carrier does not instantiate authority to compel.

### I34 — `BRAKE_REPORTED != BRAKE_INDEPENDENT`

Carry forward typed brake independence/test state, control/capture analysis, trigger/latency records and actual activation/failure distinction.

### I41 — `COURAGE_REQUIRED != ROUTE_USABLE`

Carry forward route usability with the donor's access/custody/holder-risk/safe-copy/contest-route detail. A route that requires unsafe exposure or extraordinary personal risk may exist while its practical usability for the stated scope remains unresolved or false.

Do not convert courage, sacrifice, fear or reluctance into a TRACE value score.

### I42 — `COMMITMENT_RECEIPT != CLEARANCE`

Carry forward [14.3] unresolved-commitment receipt and its anti-clearance ceiling. A receipt preserves what was unresolved/foreclosed/selected; it does not approve the selection.

---

## 6. Packet and checker boundary

Full assembly must preserve the donor distinction between:

```text
canonical packet shape
checker-external semantic binding rules
world validity
```

Minimum schema remains shape/vocabulary validation only.

Checker-external rules must continue to carry, where material:

```text
claim-reference integrity
semantic relevance
coverage/target-set binding
authority scope/currentness
route executability
brake connection / activation / independence
correction completion / residue
world correspondence
```

```text
SCHEMA_VALID != SEMANTIC_COMPLETE
CHECKER_RULE_PRESENT != CHECKER_EXECUTED
CHECKER_EXECUTED != WORLD_TRUE
```

v0.11's firing rule belongs in the operator/checker contract so a load-bearing proposition cannot escape discipline by arriving as configuration/status/metadata rather than an explicit CLAIM object.

---

## 7. Worked-transformation gate

Do not carry worked examples merely because their text existed in v0.2.7. Use them as capability regressions.

Build a worked-case matrix with at least:

```text
DONOR CASE / PURPOSE / REQUIRED CAPABILITY / v0.3 RESULT / CHANGE NEEDED
```

Known donor regression cases to preserve or replace only with explicit equivalent coverage:

```text
[15.0]   fully serialized middle-out seed
[15.2.1] divergent target-set apertures over one scene
[15.7]   hostile compliance / packet theatre
[15.8]   authentication-key rollout
[15.9]   never-built route / stream persistence
```

Also inventory every other [15] case before claiming the gate complete.

The v0.3 worked suite must include direct regressions for newly repaired seams:

```text
reported != established
record != event
refusal != malfunction
uncertainty != selector
strategy revisability != transition reversibility
population recovery != individual repair
local correction != mechanism change
route exists != route usable
hardening != irreversibility
route-specific/occurrence-specific precedence DAG
precedence DAG != feasible schedule
advantage claim requires measure
```

Prefer augmenting/retargeting donor cases where they already exercise the seam; do not create twelve decorative examples solely to repeat invariants.

---

## 8. Misuse / hostile-regression gate

Retain the donor misuse families and test v0.3 repairs against them:

```text
packet as diligence token
aperture alibi
manufactured urgency
weaponised TRACE / selective mapping of opponent only
performed TRACE compliance / unchanged selector
self-application mistaken for validation
```

Add explicit misuse regressions for:

```text
configuration field bypasses claim discipline
route alternatives unioned into false precedence cycle
uncertainty silently selects action/delay
report silently upgraded to established
record silently upgraded to event
hardening silently upgraded to irreversibility
aggregate recovery launders individual residue
```

---

## 9. Donor-map update rule

Do not overwrite `TRACE_v0_2_7_TO_v0_3_0_DONOR_MAP_v0_1.md` merely because its comparison target was spine v0.1.

Create a v0.2 donor map against the assembled full candidate.

Each donor row gets one of:

```text
EXACT_CARRY
SEMANTIC_REPAIR
PROFILE_CARRY
DERIVED_CARRY
MOVED_WITH_MAP
OPEN
MATERIAL_LOSS
```

No `REDUNDANT` or `DELETE` disposition without a separate redundancy witness.

---

## 10. Full-candidate build gates

A generated full candidate may become an **attack object** only after all of these mechanical gates pass:

```text
G1 exact donor identity verified before transformation
G2 deterministic compiler succeeds from clean donor
G3 minimum schema normalized equality passes
G4 controlled vocabulary equality passes
G5 required packet/port/discipline structure equality passes
G6 every declared textual transformation appears exactly once
G7 all untouched donor sections survive byte-identically where declared unchanged
G8 no stale v0.2.7 machine identifier remains outside explicit historical references
G9 worked-case inventory complete
G10 seven full-candidate invariant obligations mapped to operative machinery
G11 unresolved/document-control register rebuilt for v0.3
```

Passing these gates means the object is mechanically assembled, not correct.

---

## 11. Attack sequence after first assembly

Do **not** start with broad stylistic review.

Attack in this order:

```text
1 donor-loss / accidental deletion
2 false warrant or status upgrade
3 correction-window false OPEN / false CLOSED
4 route/brake/authority leakage
5 scope/aggregation laundering
6 value/moral leakage
7 packet-as-authority / performed compliance
8 cold reconstruction / transfer
```

Maximum attention goes to worked counterexamples that change a load-bearing conclusion.

```text
STYLE_DISAGREEMENT != MATERIAL_FINDING
MODEL_CONFUSION_WITHOUT_CONSEQUENCE != SCHEMA_CHANGE
```

---

## 12. Current disposition

```text
FULL CANDIDATE: NOT YET ASSEMBLED
SCHEMA CHANGE EARNED: NO
NEW PRIMITIVE EARNED: NO
NEW ROOT EARNED: NO
INVARIANT DONOR-LOSS GATE: CLEAR_WITH_RESIDUAL_LIMITS
SEVEN FULL-OBJECT OBLIGATIONS: OPEN
WORKED-CASE CAPABILITY GATE: OPEN
OPERATOR/CHECKER FULL ASSEMBLY: OPEN
DOCUMENT-CONTROL / UNRESOLVED REGISTER: OPEN
```

Next executable work:

1. build the exact donor worked-case inventory;
2. build the full-object transformation manifest by section;
3. only then write the first deterministic full-candidate compiler.

No merge/release/canon follows from this plan.
