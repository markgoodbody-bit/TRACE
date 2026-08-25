# TRACE v0.3.0 — REMAINING FULL-CANDIDATE TRANSFORM CLASSES v0.1

**Status:** WORKING COMPILER CONTRACT — NOT FULL CANDIDATE — NOT VALIDATION — NOT RELEASE/CANON  
**Donor:** released `TRACE_FORMAL_SEED_v0_2_7.md`  
**Semantic repair source:** `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_11.md`  
**Rule:** donor capability is retained unless a later worked failure earns a bounded change.

This file specifies transform classes not already separately attacked as `T_CLOCK_ROUTE` and `T_CLAIM_EVIDENCE`.

```text
DONOR_HAS_PROTECTION != REWRITE_REQUIRED
SEMANTIC_REPAIR != VOCABULARY_REVISION
FULL_CANDIDATE != EXPANDED_SPINE
```

---

## T_SELECTION_ATTRIBUTION

**Donor surfaces:** `[2] SELECTIVE CAUSAL LOOP`, `[6] TRANSITIONS AND COUPLINGS`, `[10.4] Explicit layer handoff`, `[13] TRACE OPERATOR`, packet selector/discipline fields in `[14]`.

**Carry unchanged:** selector remains external to TRACE; action/transition distinction; wait/delay/inaction symmetry; layer handoff; selector ownership; `uncertainty_selects_transition: false`.

**Bounded repairs:** make operative at the point of use:

```text
UNCERTAINTY != SELECT_ACTION
UNCERTAINTY != SELECT_DELAY
UNCERTAINTY_INPUT_TO_POLICY != UNCERTAINTY_IS_SELECTOR
IMPLICIT_DEFAULT != NO_SELECTION_RULE
```

Where a downstream transition is selected under uncertainty, attribute the selection to the represented selector/policy/default/authority path. Do not require a selector node merely because uncertainty exists.

Measurement/publication may be represented as an ACTION/transition contributor where evidence supports that causal claim:

```text
MEASUREMENT != PASSIVE_OBSERVATION
MEASUREMENT_OCCURRED != MEASUREMENT_CAUSED_CHANGE
```

No new selector or measurement primitive.

---

## T_ROUTE_REFUSABILITY

**Donor surfaces:** `[6.2] Coupling`, `[6.3] Control`, `[6.4] Constraint and refusability`, `[8.5] Route`, `[9.3] Record and custody`, `[16] artificial-entity profile`, `[17] connected brake`.

**Carry unchanged:** route tuple, scope-relative usability `u(rho,i,t)`, access vs safe evidential usability, control/constraint/refusal machinery, brake/rollback distinction.

**Bounded repairs:** add operative non-entailments at route/refusal use-sites:

```text
ROUTE_EXISTS != ROUTE_USABLE
BURDEN_PRESENT != ROUTE_UNUSABLE
REFUSAL_RECORDED != REFUSAL_EFFECTIVE
REFUSAL != MALFUNCTION
STRATEGY_REVISABLE != TRANSITION_REVERSIBLE
FUTURE_POLICY_CAN_CHANGE != PRIOR_STATE_CAN_BE_RESTORED
```

`route_usable` remains target/scope/time/measure-relative. A route can be usable generally while not usable to alter one target before one boundary.

No universal independence or permission taxonomy.

---

## T_SCOPE_AGGREGATION

**Donor surfaces:** `[5.2.1] Scope granularity and non-substitution`, burden/residue `[9]`, packet scope discipline `[14]`, invariants `[19]`.

**Carry unchanged:** nested-boundary mapping, cross-scale correspondence/measure requirement, population/member non-substitution.

**Bounded repairs:** make the downstream repair claim explicit:

```text
POPULATION_RECOVERY != REPAIR_OF_INDIVIDUAL_LOSS
GROUP_METRIC_RESTORED != EVERY_AFFECTED_SCOPE_REPAIRED
```

Aggregate repair may support lower-level repair only through an explicit evidence-bearing correspondence that actually entails it. No moral priority follows from granularity.

---

## T_FUTURE_CORRESPONDENCE

**Donor surfaces:** `[7] FUTURE-SPACE`, especially `[7.1] Trajectory correspondence before set comparison`.

**Carry unchanged:** donor `J_i^t` correspondence relation, `TRAJECTORY_ALIGNMENT = UNKNOWN`, no raw set subtraction across times, typed future metadata, measure-relative hardening and valence port.

**Bounded repair:** add the explicit regression guards:

```text
SAME_PATH_LABEL != SAME_TRAJECTORY
PATH_IDENTIFIER_PERSISTS != PATH_EFFECT_PERSISTS
TECHNICALLY_REACHABLE_SUCCESSOR != COMPARABLE_CONTINUATION
```

These are firing/interpretation guards over donor correspondence; they do not replace `J_i^t` and do not add a relation type.

---

## T_RECORD_RESIDUE

**Donor surfaces:** truth discipline `[4.5]`, `[9] BURDEN / RESIDUE / MEMORY`, record/custody `[9.3]`, packet custody surfaces `[14]`.

**Carry unchanged:** typed burden, residue persistence, custody, safe-copy/holder-risk, integrity-check ceilings.

**Bounded repairs:** ensure operative at evidential and repair use-sites:

```text
RECORD != EVENT
RECORD_OBSERVED != EVENT_OBSERVED
RECORDED_LOSS != REPAIRED_LOSS
CLOSED_TASK != CLEARED_RESIDUE
TRANSFERRED_BURDEN != REMOVED_BURDEN
```

A record may support an event proposition under an exposed evidential contract; observing the record does not convert the historical/world event to direct observation.

---

## T_MEASURE_ADVANTAGE

**Donor surfaces:** `[10.2] Measure`, `[10.3] Neutral structural patterns`, `[10.4] layer handoff`, future-space comparisons `[7]`.

**Carry unchanged:** measure may be partial/vector/relational; scalar not required; alternative measures/sensitivity/unrepresented dimensions remain explicit.

**Bounded repair:** fire:

```text
ADVANTAGE_CLAIM_REQUIRES_MEASURE
```

for any load-bearing comparative claim such as `better`, `worse`, `advantage`, `improved`, `expanded`, `safer`, or domain synonym where the ordering is not already explicit and sourced. A qualitative or relational measure is sufficient. Measured advantage does not establish entitlement or moral rank.

---

## T_OPERATOR_CHECKER

**Donor surfaces:** `[13] TRACE OPERATOR`, `[14.1] Binding rules`, `[14.4] Minimum validator`.

**Carry unchanged:** abstract `tau`, recursion/depth budget, non-command output, parsability ceiling, minimum-schema/world-validity ceiling.

**Bounded repairs to operator sequence:**

1. before a load-bearing proposition is used downstream, apply representation-independent evidence/currentness/scope/warrant firing;
2. distinguish evidence state from access/custody at the use-site;
3. distinguish report from establishment and record from event;
4. for negative/null or discriminating test results, expose enough instrument/test capability to establish that the relevant alternative was detectable at the resolution required by the downstream use;
5. distinguish check existence, execution, discrimination, completion, return-to-use and currentness;
6. construct correction-window timing only after exact target/boundary/route/capability/temporal/process bindings are supported;
7. preserve liveness loss as a verification/currentness event without assigning cause.

```text
CHECK_EXISTS != CHECK_EXECUTED
CHECK_EXECUTED != CHECK_DETECTS_TARGET_FAILURE
CHECK_COMPLETED != CHECK_RESULT_REACHED_USE
ONE_DETECTED_FAILURE != UNIVERSAL_INSTRUMENT_ADEQUACY
```

Do not require destructive fault injection universally.

---

## T_PACKET_BINDING

**Donor surfaces:** `[14] CANONICAL TRACE GRAPH PACKET`, `[14.0.1] target-set profile`, `[14.1] binding rules`, `[14.2] packet-use boundary`, `[14.3] commitment receipt`, `[14.4] validator.

**Shape rule:** packet shape, six ports, discipline blocks and controlled vocabularies remain unchanged. Version identity changes only through `T_VERSION_IDENTITY` / deterministic minimum-schema compiler.

**Bounded repairs:** add checker-external binding/use rules for representation-independent firing, currentness, report/establishment, record/event, route usability, measure-bound advantage, target-bound correction window and liveness. These are semantic use rules; do not add required minimum-schema fields merely to encode them.

```text
MINIMUM_SCHEMA_PASS != SEMANTIC_BINDING_PASS
SEMANTIC_BINDING_PASS != WORLD_TRUTH
```

Target-set existing-object profile and commitment receipt are retained.

---

## T_WORKED_CASES

**Donor surfaces:** `[15.0]` through `[15.9]`, including `[15.2.1]`.

**Rule:** retain all donor cases. Tighten existing cases before adding new examples.

Required regression hooks using existing cases:

```text
15.0 compressed instruction:
  report/establishment + uncertainty/selector attribution + firing

15.1 pharmacist route:
  route exists/usable + target/time scope

15.2 violin route:
  local routes != end-to-end effective route

15.2.1 migration target sets:
  target-set aperture / omitted scope / representation formation

15.3 classifier brake:
  reported brake != independent/tested/fast enough; DAG feasibility if timing used

15.5 lethal irreversible transition:
  explicit target boundary + route/capability scope + uncertainty not selector

15.7 hostile packet theatre:
  packet/schema/check != mechanism change; instrument discrimination and ownership coupling

15.8 key rollout:
  target-set incompleteness + correction-window common basis/feasibility + record currentness

15.9 never-built route/stream:
  absence production mechanism + local correction/stream persistence != mechanism change
```

No new worked case is currently required solely to duplicate an invariant sentence.

---

## T_RECEIVER_PROFILE

**Donor surface:** `[16] ARTIFICIAL-ENTITY / RECEIVER` profile.

**Carry/profile boundary:** retain artificial-entity uncertainty, non-extraction, private-reasoning ceiling, capability distinctions and safe-refusal exposure. Do not universalise this profile.

Align exact guards where present:

```text
REFUSAL != MALFUNCTION
UNCERTAINTY != SELECT_ACTION
UNCERTAINTY != SELECT_DELAY
```

No consciousness, persistence or moral-standing conclusion follows.

---

## T_CONNECTED_BRAKE

**Donor surface:** `[17] LIVE INTERPRETER / VALUE LAYER / SELECTOR / CONNECTED BRAKE`.

The donor already carries most of the required full-object semantics. Retain them.

Make exact at local use-sites:

```text
REVIEW_AFTER_COMMITMENT != BRAKE
VISIBILITY != CARRYING
CARRYING != ENFORCEMENT
BRAKE_REPORTED != BRAKE_INDEPENDENT
BRAKE_PRESENT != BRAKE_INDEPENDENT
BRAKE_INDEPENDENT != BRAKE_FAST_ENOUGH
BRAKE_FIELD_POPULATED != BRAKE_CONNECTED
ROLLBACK_ACTION != RESTORED_STATE
```

No connected brake is instantiated by TRACE. No carrier/enforcer supplies moral or selection authority merely by existing.

---

## T_INVARIANT_MISUSE

**Donor surface:** `[19] INVARIANTS / MISUSE GUARDS`.

**Hard carry:** retain donor I01–I60 verbatim and in order.

Add a separate v0.3 repair block after I60 rather than renumbering donor invariants in this working candidate. Candidate repair guards should include only distinctions earned by worked failures and not already equivalent to an existing donor invariant, including at least:

```text
REPRESENTATION_TYPE != EVIDENCE_STATUS
CONFIGURATION_FIELD != WARRANT_FREE_FACT
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
```

This supplemental block is working v0.3 semantics, not a claim that the canonical invariant count has permanently changed.

Retain all donor misuse sections `[19.1]`–`[19.6]`; add a bounded regression note for instrument discrimination and representation formation rather than creating a new misuse ontology.

---

## T_SURVIVAL_KERNEL

**Donor surface:** `[20] COMPRESSION / SURVIVAL KERNEL`.

Rebuild from donor kernel, preserving its numbered conceptual structure where practical. Do not replace it with the short v0.11 kernel.

Mandatory propagated v0.3 repairs:

```text
representation-independent firing
report != establishment
record != event
dependency-relative currentness
measurement may enter causal path but does not prove reactivity
instrument discrimination
liveness-loss cause ceiling
route/pathway/occurrence-bound precedence
acyclic precedence != feasible schedule
common temporal basis
explicit target boundary
hardening != irreversibility
uncertainty != selector
future path identifier != trajectory correspondence
aggregate recovery != individual repair
local correction + stream persistence != mechanism change
```

Hard gate:

```text
FULL_OBJECT_REPAIR -> SURVIVAL_KERNEL_PROPAGATION
```

If an admitted repair intended to survive compression is absent from the rebuilt kernel, the full-candidate build fails.

---

## T_DOCUMENT_CONTROL

**Donor surface:** `[21] REVISION / DOCUMENT CONTROL / UNRESOLVED`.

Rebuild, do not mechanically carry stale v0.2.7 release/unresolved wording.

Working candidate must state:

```text
v0.2.7 remains released baseline
v0.3.0 object is working candidate only
compiler identity and donor SHA-256
minimum-schema candidate identity and shape-preservation result
controlled vocabulary unchanged unless later falsification earns change
v0.11 semantic overlay identity
failed intermediate spine/repair objects remain evidence
known full-candidate debts and unresolved attack surfaces
no validation / release / canon / permission / authority / clearance claim
```

Document control must not call a generated object `released`, `validated`, `canonical`, or `baseline` before Mark's release gate.

---

# Compiler binding requirements

Every transform class implemented by the full compiler must provide:

```text
class_id
source_heading(s)
source section SHA-256(s) from donor section manifest
exact anchor(s)
expected anchor count(s)
mutation type: INSERT_AFTER | INSERT_BEFORE | REPLACE_EXACT | VERSION_ONLY | REBUILD_SECTION
postcondition token(s)
regression check(s)
```

Compiler failure policy:

```text
ANCHOR_COUNT != EXPECTED -> FAIL
DONOR_SECTION_SHA_MISMATCH -> FAIL
UNDECLARED_MUTATION -> FAIL
MISSING_REQUIRED_PROPAGATION -> FAIL
```

No fuzzy matching in the compiler.

---

# Current disposition

```text
T_CLOCK_ROUTE          separately specified + attacked
T_CLAIM_EVIDENCE       separately specified + attacked
remaining classes      specified here
full compiler           NOT YET WRITTEN
full candidate          NOT YET GENERATED
```

One material counterexample to a transform class holds that class without blocking unrelated donor carry.