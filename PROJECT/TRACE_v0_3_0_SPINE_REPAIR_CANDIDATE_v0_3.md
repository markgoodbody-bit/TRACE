# TRACE v0.3.0 — SPINE REPAIR CANDIDATE v0.3

**Status:** WORKING REPAIR DELTA — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE  
**Target:** `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_2.md`  
**Selection source:** `PROJECT/TRACE_v0_3_0_INTEGRATION_AND_DELETION_PASS_v0_1.md`  
**Supersedes as current repair target:** `PROJECT/TRACE_v0_3_0_SPINE_REPAIR_CANDIDATE_v0_2.md`  
**v0.2 failure witness:** `falsification/TRACE_v0_3_0_SPINE_REPAIR_V02_IMMEDIATE_SELF_ATTACK.md`  
**Earlier v0.1 repair object remains separate.**  
**Purpose:** apply only field-earned semantic repairs; no new primitive, root, authority system, moral selector, or universal checker.

---

# 0. Delta ceiling

This object proposes edits at four seams only:

```text
[3] selective causal loop / measurement
[5]-[6] longitudinal currentness / claim-evidence
[6]/[8] verification / witness / liveness
[9] correction-window representation
```

Relative to v0.2, this version changes only:

1. mutation-relative freshness is explicitly **dependency-relative**;
2. interval timing requires a **common supported temporal basis** before comparison.

```text
FIELD_CASE != NEW_ONTOLOGY
REPAIR_DELTA != FULL_SPINE
REPAIR_SELECTED != REPAIR_SURVIVED
```

---

# 1. [3] Selective causal loop — measurement is not presumed passive

## Proposed insertion after the existing core live loop

Aperture, observation, audit, measurement, publication, notification and inquiry are not assumed to be causally inert merely because their local purpose is epistemic.

Where represented evidence supports a causal path, the act of measuring, naming, publishing, querying or observing may itself be represented as an `ACTION` or causal contribution to a later `TRANSITION`.

[NON_ENTAILMENT]

```text
MEASUREMENT != PASSIVE_OBSERVATION
PUBLICATION_OF_MEASUREMENT != NONINTERVENTION
MEASURED_STATE_t+1 != COUNTERFACTUAL_UNMEASURED_STATE_t+1
REPEATED_MEASUREMENT != SAME_UNPERTURBED_PROCESS
```

This is conditional. TRACE does not infer intervention merely because measurement occurred.

```text
MEASUREMENT_OCCURRED != MEASUREMENT_CAUSED_CHANGE
POSSIBLE_REACTIVITY != ESTABLISHED_REACTIVITY
```

Existing `MEASURE`, `ACTION`, `CAUSES`, `CONTRIBUTES_TO`, `TRANSITION`, aperture and evidence structure carries the relation. No new primitive is introduced.

---

# 2. [5]-[6] Longitudinal currentness — invalidation is dependency-relative

## Proposed addition to [5] after the current freshness paragraph

Freshness need not decay only with wall-clock age.

A claim, derived value, map, route, capability or record may cease to support a current use when a represented event changes a load-bearing dependency even if its timestamp remains inside the declared time window.

Where currentness is load-bearing and an invalidation relation is represented, preserve enough to connect the event to the dependency the current claim actually uses.

Possible invalidating events include, where dependency-relevant:

```text
source mutation
version change
new observation/event
policy/grant change
capability change
route change
measurement-window closure
explicit time/age expiry
```

[NON_ENTAILMENT]

```text
DATE_CURRENT != DERIVED_VALUE_CURRENT
TIME_HORIZON != MUTATION_HORIZON
SOURCE_CHANGED_WITHIN_TIMESTAMP_BUCKET != TIMESTAMP_STALE
RECOMPUTABLE_DERIVATION != STORED_DERIVED_VALUE
CURRENT_AT_USE != VALID_THROUGH_DEPENDENT_INTERVAL
FRESHNESS_POLICY != TIME_TO_LIVE_ONLY
NO_TIME_EXPIRY != NO_INVALIDATING_EVENT

SOURCE_MUTATED != LOAD_BEARING_DEPENDENCY_CHANGED
LOAD_BEARING_DEPENDENCY_CHANGED != DERIVED_PROPOSITION_CHANGED
MUTATION_OBSERVED != CLAIM_INVALIDATED
```

Do not invent an invalidator merely because one is possible, and do not invalidate a claim merely because some unrelated part of its source changed.

Where a mutation/event can alter a represented dependency used by the derivation, currentness may require reacquisition or recomputation before the dependent use.

Where the mutation is represented as outside the derivation dependency, it need not invalidate the claim.

Where relevance of the mutation to the derivation cannot be established, preserve that uncertainty rather than upgrading either to `CURRENT` or `STALE`.

```text
INVALIDATOR_NOT_IDENTIFIED != NO_INVALIDATOR_EXISTS
POSSIBLE_INVALIDATOR != ESTABLISHED_INVALIDATION
SOURCE_MUTATED != DERIVATION_STALE
```

## Proposed addition to [6] material-claim fields

Where currentness is load-bearing, the existing `freshness / observation time` field may be supplemented by:

```text
represented dependency used by the current proposition/derivation
represented invalidation event / version / condition that can alter that dependency
use interval over which the claim is expected to remain valid
```

These are claim/evidence/dependency bindings, not new canonical primitives.

---

# 3. [6]/[8] Verification, witness and liveness ceilings

## Verification discrimination

A verification path can fail in separable ways without creating new root types:

```text
instrument/check not present
instrument/check not active/executed
instrument cannot discriminate the relevant alternative
result does not reach the current use in time/current form
```

When the difference is load-bearing, preserve the represented basis rather than compressing all four into `checked`.

[NON_ENTAILMENT]

```text
CHECK_EXISTS != CHECK_EXECUTED
CHECK_EXECUTED != CHECK_DETECTS_TARGET_FAILURE
INSTRUMENT_REVIEWED != INSTRUMENT_EXERCISED
EXPECTED_FAILURE_PATH != OBSERVED_FAILURE_PATH
STATIC_CORRECTNESS != OPERATIONAL_DISCRIMINATION
CHECK_COMPLETED != CHECK_RESULT_REACHED_USE
```

`INSTRUMENT_EXERCISED` does not mean every instrument requires destructive live fault injection. It means the claim of adequacy must remain bounded by whatever evidence supports the proposition that the relevant alternative is detectable.

```text
ONE_DETECTED_FAILURE != UNIVERSAL_INSTRUMENT_ADEQUACY
```

## Liveness / silence ceiling

Loss of a heartbeat, status update, reply, route or witness can close a current verification interval without identifying the cause.

Where a prior current verification interval was represented, a reading may state ordinary claims such as:

```text
current state not verified after t
witness liveness not observed after t
route not observed active after t
```

Do not promote those phrasings into a new universal status enum.

[NON_ENTAILMENT]

```text
SILENCE != TAMPERING
NO_REPLY_OBSERVED != REFUSAL
PROCESS_EXISTS != PROCESS_HEALTHY
MUTEX_HELD != WORKER_HEALTHY
SAFE_EXCLUSION != LIVENESS
WITNESS_LIVENESS_LOST != CAUSE_ESTABLISHED
```

## Witness dependency ceiling

A witness can establish what it observed under its aperture without establishing universal delivery or control independence.

[NON_ENTAILMENT]

```text
EXTERNAL != INDEPENDENT
WITNESS_OBSERVED_X != EVERY_READER_WAS_SERVED_X
HASH_MATCH != CONTINUOUS_CONTENT_IDENTITY
EXTERNAL_CLOCK != COMPLETE_OBSERVATION
SEPARATE_PARTY != INDEPENDENT_EVIDENCE
```

Use existing aperture, entity, claim, record, dependency and control structure. No `WITNESS` primitive is added.

---

# 4. [9] Correction window — event graph, explicit boundary, common temporal basis

## Defect in the current spine

The current spine presents:

```text
T_detect(q,l) + T_route(q,l) + T_correct(q,l) < T_irreversible(q,l)
```

then bounds it as sequential shorthand.

That is no longer sufficient as the primary v0.3 representation because hostile work has already shown independent failures involving:

```text
required verification time omitted from completion
parallel/overlapping stages
uncertain/interval event times
incomparable clock origins
hidden target/adequacy thresholds
capability-relative unattainability/restoration
multiple load-bearing target boundaries
process events that change the boundary itself
```

The additive inequality may remain only as a bounded special case after the general object is established.

## 4.1 General process object

For a declared failure/harm pathway `q`, affected scope `l`, target effect/state `o`, correction capability/route context `c`, target-boundary condition `g`, and use context `u`, represent the load-bearing correction process as an event/precedence graph:

[SCHEMATIC_MODEL]

```text
G_window(q,l,o,c,g,u) = (V, E_prec)
```

where `V` contains the represented load-bearing events/stages and `E_prec` contains the required precedence constraints.

Events may include, where load-bearing:

```text
detection / observation
routing / escalation
required verification / discrimination
review / decision
brake / interruption
correction / rollback / repair
result return to use
```

For represented event durations/bounds, derive completion from the represented critical path rather than summing stages that may overlap.

```text
T_complete = critical_path_completion(G_window)
```

This remains a schematic model. Domain timing distributions, estimators and event definitions remain external.

## 4.2 Target boundary must be represented, not manufactured

A correction-window comparison requires a represented condition that says what target effect/state counts as the relevant close/hardening boundary for the stated scope and capability context.

Where load-bearing preserve:

```text
target effect/state
affected scope
boundary condition / threshold
selector / source / basis for that condition
selection/freeze time where outcome-informed choice is possible
measure / instrument / model used to observe the condition
corrector / route-set / capability context where attainability is capability-relative
alternative/disputed boundary conditions
```

If the target boundary condition is absent, do not manufacture a natural close instant.

```text
TARGET_BOUNDARY_TIME_REQUIRES_REPRESENTED_BOUNDARY_CONDITION
BOUNDARY_CONDITION_DECLARED != BOUNDARY_CONDITION_JUSTIFIED
BOUNDARY_CONDITION_JUSTIFIED != MORAL_ADEQUACY
THRESHOLD_SELECTED_AFTER_RESULT != PREDECLARED_BOUNDARY
UNREACHABLE_BY_DECLARED_ROUTE_SET != WORLD_IRREVERSIBLE
NO_KNOWN_ALTERNATIVE_ROUTE != WORLD_IRREVERSIBLE
```

TRACE exposes the selector/source/basis. It does not choose the morally adequate threshold.

## 4.3 Common temporal basis before interval comparison

Timing values are not comparable merely because they use the same units.

Where a load-bearing comparison joins event/boundary times, preserve or derive a common temporal basis. This may be one shared reference event/clock or an explicit supported conversion relation between references.

Where material preserve:

```text
reference event / temporal origin
unit / scale
time source / clock basis
conversion relation when references differ
uncertainty of that conversion
interval semantics / closure convention where relevant
```

[NON_ENTAILMENT]

```text
NUMERICALLY_COMPARABLE != TEMPORALLY_COMPARABLE
SAME_UNIT != SAME_REFERENCE_EVENT
INTERVAL_BOUNDS != COMMON_CLOCK_BASIS
CLOCK_TYPED != CLOCKS_JOINABLE
CONVERSION_DECLARED != CONVERSION_SUPPORTED
```

If the completion and target-boundary times cannot be put on a sufficiently supported common temporal basis, the window comparison remains `UNKNOWN` for that use.

## 4.4 Interval-safe timing after temporal binding

Only after the compared times share a supported temporal basis, preserve a supported interval where available:

```text
I_x = [lower(t_x), upper(t_x)]
```

For completion interval `I_complete` and target-boundary interval `I_boundary` on the same supported temporal basis:

```text
lower(I_boundary) > upper(I_complete)
  -> GUARANTEED_OPEN_FOR_REPRESENTED_BINDINGS

upper(I_boundary) <= lower(I_complete)
  -> GUARANTEED_CLOSED_FOR_REPRESENTED_BINDINGS

otherwise
  -> WINDOW_STATUS_UNKNOWN
```

[NON_ENTAILMENT]

```text
POINT_ESTIMATE_FITS != GUARANTEED_OPEN
OVERLAPPING_TIME_BOUNDS != WINDOW_FITS
TIMING_BOUNDS_PRESENT != TIMING_BOUNDS_ADEQUATE
GUARANTEED_OPEN_FOR_REPRESENTED_BINDINGS != PERMISSION_TO_ACT
```

## 4.5 Multiple boundaries

Where several target effects/scopes are independently load-bearing, do not collapse them into one unqualified close time without a declared composition rule.

```text
MULTIPLE_LOAD_BEARING_BOUNDARIES != ONE_UNQUALIFIED_CLOSE
```

Return per-boundary status or an explicitly justified composition.

## 4.6 Rebinding

A window claim is conditional on its represented target, boundary, scope, capability, temporal basis and process bindings.

```text
TARGET_CHANGED -> WINDOW_CLAIM_REBOUND
BOUNDARY_CONDITION_CHANGED -> WINDOW_CLAIM_REBOUND
CAPABILITY_SCOPE_CHANGED -> WINDOW_CLAIM_REBOUND
TEMPORAL_BASIS_CHANGED -> WINDOW_CLAIM_REBOUND
PATH_EVENT_CHANGES_TARGET_PROCESS -> WINDOW_CLAIM_REBOUND
```

A prior fit does not automatically survive a changed process.

```text
PAST_WINDOW_FIT != CURRENT_WINDOW_FIT
```

## 4.7 Special-case serial shorthand

Only after the bindings above are represented, if the required stages are genuinely sequential at the chosen abstraction, their timings share a supported basis, their durations are sufficiently represented, and one relevant target boundary is fixed for the stated bindings, the earlier shorthand may be used:

```text
T_detect + T_route + T_correct < T_boundary
```

where required verification/check time must be included in the represented stages rather than treated as free.

```text
REQUIRED_CHECK_TIME != ZERO_DURATION
LOAD_BEARING_CHECK != FREE_CHECK
```

The shorthand is a derived special case, not the primary correction-window object.

---

# 5. Proposed survival-kernel additions

Do not add every new non-entailment to the survival kernel.

The smallest additions that appear worth carrying are:

```text
Freshness can expire through a represented change to a load-bearing dependency, not only through age.
Measurement or publication can itself enter the causal path; do not presume passivity or causality.
A check being present or executed does not establish that it can detect the failure that matters.
Loss of witness/liveness can close current verification without establishing the cause.
Correction timing requires comparable temporal references, an explicit target boundary and the represented process; point estimates and route-relative failure do not establish world irreversibility.
```

If hostile transfer shows these are recoverable without explicit survival-kernel text, omit them there and keep the fuller sections only.

---

# 6. Explicit non-promotions

This repair does not add:

```text
FRESHNESS primitive
WITNESS primitive
PROCESS primitive
CLOCK_REFERENCE primitive
MEASUREMENT-INTERVENTION universal rule
liveness status taxonomy
statistical inference subsystem
five-mode claim taxonomy
moral adequacy threshold
world-irreversibility oracle
universal dependency operator
```

PR #39 remains derived/hostile-trial.  
PR #41 remains teaching/profile/cold-trial.  
PR #42 remains checker-external/HOLD.  
PR #43 remains evidence/tooling.

---

# 7. Immediate hostile targets

Hold this repair if any one of these lands:

1. **Freshness bureaucracy:** ordinary current claims now require speculative enumeration of every possible invalidator.
2. **False dependency certainty:** an invalidation relation is asserted without evidence that the changed source component is load-bearing for the derivation.
3. **Measurement overreach:** readers start treating all observation as intervention without causal evidence.
4. **Fault-injection overreach:** `operational discrimination` is read as a mandatory destructive test rather than a bounded adequacy-evidence requirement.
5. **Liveness ontology drift:** ordinary claim phrasing hardens into a new universal enum or root.
6. **Witness recursion:** checking witness independence creates unbounded witness-of-witness regress.
7. **Clock-join laundering:** a conversion relation is merely declared and then treated as sufficient evidence that two timing intervals are comparable.
8. **Boundary laundering:** target-boundary source/basis is represented but still allows the claimant to choose an outcome-friendly threshold after seeing the result.
9. **Adequacy laundering:** `boundary condition justified` is mistaken for moral adequacy.
10. **False interval safety:** narrow-looking intervals are accepted without support for their bounds.
11. **Graph ceremony:** event/precedence representation expands ordinary sequential cases without changing the result or repair.
12. **Capability laundering:** route-set-relative closure is later described as world irreversibility.
13. **Multiple-boundary collapse:** one convenient boundary still erases another load-bearing scope.
14. **No behavioural delta:** the new language changes labels but does not change any refusal, repair, or downstream conclusion in hostile transfer.

Preferred outcome remains `SMALLER`, `DERIVED`, or `DELETE` for any part that does not earn its cost.

---

# 8. Current disposition

```text
SPINE_REPAIR_v0_2:             FAILED / PRESERVED
SPINE_REPAIR_v0_3:             CURRENT ATTACK OBJECT
NEW PRIMITIVE:                 NO
NEW ROOT:                      NO
SPINE EDIT:                    CANDIDATE ONLY
CORRECTION WINDOW:             PRIMARY REPAIR / STILL ATTACKABLE
FIELD DELTAS:                  NARROW CORE GUARDS, NOT NEW ONTOLOGY
MERGE / RELEASE / CANON:       NO
NEXT MOVE:                     ATTACK v0.3 BEFORE FOLDING INTO A NEW SPINE
```
