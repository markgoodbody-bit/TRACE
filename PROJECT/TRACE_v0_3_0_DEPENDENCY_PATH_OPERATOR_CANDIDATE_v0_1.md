# TRACE v0.3.0 — DEPENDENCY-PATH OPERATOR CANDIDATE v0.1

**Status:** WORKING DERIVED OPERATOR — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE — NO NEW PRIMITIVE CLAIM  
**Predecessors:** `TRACE_v0_3_0_OPERATOR_INTERFACES_CANDIDATE_v0_1.md`; `TRACE_v0_3_0_OPERATOR_TRANSFER_MATRIX_v0_1.md`  
**Purpose:** collapse the named I/X/C architecture into the smallest inspection rule that still changes repair in demonstrated failures.

---

## 0. Current compression

The transfer matrix found that representation-route, receiver-integration, activation and check failures can require different repairs, but it also found that they are recursive and aperture-relative rather than universal execution stages.

So do not make `INGRESS`, `ACTIVATION`, `CHECK`, `R`, `J`, `X`, or `C` new semantic kinds.

Current preferred move:

> **Start from a declared downstream use. Walk backward through the represented dependencies and the representation paths that supplied them. Preserve only distinctions whose collapse can change that use. Where the use relies on a check, walk the check forward through exact proposition, instrument, coverage, dependencies, timing and return. Stop when further traversal cannot change the use under the represented model; preserve specific unresolved omissions rather than pretending the map is complete.**

This is a derived inspection operator over existing TRACE structure.

---

# 1. BOUNDED BACKWARD WALK

Let `U` be a represented downstream use: a claim, comparison, ranking, qualifier, routing choice, transition condition, correction claim, or other declared use.

For each represented dependency `k` feeding `U`:

```text
U
<- represented dependency k
<- standing map / retained relation
<- supplied claim / record / signal
<- representation / target / source path where material
<- source or bounded world-facing aperture where available
```

At each traversed relation ask only:

```text
Could collapsing this distinction change the interpretation or status of U
under the represented model?
```

If NO, stop that branch.

If YES, preserve the existing TRACE distinction required to keep the two states separate.

If UNKNOWN and a **specific unresolved alternative** would change `U`, preserve the fork as unresolved.

Do not expand merely because some unspecified omitted fact might exist.

```text
GENERIC_POSSIBLE_OMISSION != MATERIAL_UNRESOLVED_FORK
UNKNOWN != AUTOMATIC_STOP
MORE_FIELDS != BETTER_READING
```

---

# 2. REPRESENTATION PATH IS PART OF THE DEPENDENCY PATH

A dependency can be wrong or misleading before downstream inference begins even when every represented statement is internally coherent.

Where the path itself can change meaning, scope, evidence state or use, preserve enough existing structure to distinguish transformations such as:

```text
world/source -> target-set selection
source object -> observed rendering
utterance -> paraphrase / speech-act typing
record -> supplied excerpt
supplied claim -> retained map relation
historical report -> current-state use
```

Existing machinery should carry this:

```text
APERTURE
MAP
CLAIM / EVIDENCE
PROVENANCE
SOURCE / ROUTE
TARGET-SET
BOUNDS / OMITS / DISPUTES
RETAINED HISTORY
receiver-specific integration J_receiver where relevant
```

No new representation primitive is proposed.

Useful ceilings:

```text
APERTURE_OUTPUT != COMPLETE_SCENE
OBSERVED_RENDERING != SOURCE_OBJECT
RETAINED_HISTORY != CURRENT_WORLD
TRACE_OUTPUT != RECEIVER_MAP_UPDATE
SOURCE_PROVENANCE != PROPOSITION_SUPPORT
NOT_TARGETED != ABSENT
```

---

# 3. ACTIVATION BECOMES A PROPERTY OF THE WALK, NOT A SEPARATE STAGE

A TRACE distinction is active for `U` when the backward walk reaches a dependency for which collapsing that distinction can change `U`.

No universal `TRIGGER` object is required.

```text
DISTINCTION_PRESENT != DISTINCTION_APPLIED
TRIGGER_SUCCESS != REPRESENTATION_COMPLETE
REPRESENTED_USE != OPERATIVE_USE
UNDECLARED_DEPENDENCY != ABSENT_DEPENDENCY
```

If a **specific broader operative use** can be named that would change the traversed dependency set, preserve that use-scope fork.

Do not inspect all hypothetical future uses.

Where represented interactions are joint, preserve joint dependence; one-at-a-time perturbation is insufficient for XOR-like, threshold or path-dependent relations.

---

# 4. FORWARD CHECK WALK

When `U` relies on a verification, test, audit, matcher, correction route or other checking process, the check itself becomes a causal path to inspect.

Walk forward through, where material:

```text
exact proposition / alternative to discriminate
-> selected evidence / coverage aperture
-> instrument / matcher capability and resolution
-> evidence / control / adaptivity dependencies
-> answer-information / precommitment state
-> execution
-> completion time
-> result route
-> return to the using aperture
```

Preserve:

```text
CHECK_PATH_EXISTS != CHECK_EXECUTED
CHECK_EXECUTED != CHECK_WAS_ADEQUATE
CHECKED_EVIDENCE != CHECKED_LOAD_BEARING_PROPOSITION
PROCEDURE_PRECOMMITTED != INSTRUMENT_ADEQUATE
TEST_RAN != RELEVANT_ALTERNATIVE_DETECTABLE
CHECK_COMPLETED != CHECK_RESULT_REACHED_USE
EVENTUALLY_CHECKABLE != CHECKABLE_BEFORE_USE
CHECKER_SEPARATE != EVIDENCE_DEPENDENCY_SEPARATE
```

A successful check may itself create a record that becomes input to a later reading. Therefore the operator is recursive, not a one-way phase pipeline.

```text
CHECK_RESULT -> NEW_RECORD -> LATER_DEPENDENCY_PATH
CORRECTION -> WORLD_CHANGE / RESIDUE -> NEW_APERTURE
```

---

# 5. DIAGNOSTIC LOCATION WITHOUT NEW ROOTS

When useful for repair, describe the first currently actionable defect in ordinary language or with local shorthand:

```text
R  representation route / target / rendering / retyping
J  receiver integration / retained-map relation
X  represented distinction dormant at use
C  checking / actuation / return path
```

These are diagnostic locations only.

```text
DIAGNOSTIC_LOCATION != SEMANTIC_PRIMITIVE
OBSERVED_FAILURE_LOCATION != UNIQUE_CAUSAL_ORIGIN
DIAGNOSTIC_LOCATION != BLAME
FIRST_VISIBLE_FAILURE != ONLY_FAILURE
```

If naming `R/J/X/C` does not change the next repair, omit the labels.

---

# 6. REPAIR CONSEQUENCE TEST

The operator earns its place only when locating the path failure changes the next corrective move.

Examples from the transfer matrix:

```text
representation target omitted alias
  -> change/reacquire target/search aperture

inherited/current distinction represented but dormant
  -> activate source/freshness relation at current use

check reruns same blind matcher
  -> change matcher/coverage/evidence dependency

precommitted null test under-resolved
  -> change instrument/resolution or narrow proposition

corrective rendering uses broken decoder
  -> reacquire source through independent observation path
```

If the same generic repair follows regardless of location, the diagnostic decomposition is not doing work and should be deleted.

---

# 7. WORKED COMPRESSION — CLINICAL HANDOVER

Supplied handover:

```text
Patient 14 is anxious, medically stable, frequent caller.
```

Assume the earlier statements were supportable when written.

Later new information arrives.

The dependency-path operator does not say `distrust the handover`.

It asks which proposition is now feeding the current use and walks backward:

```text
current assessment U
<- `medically stable` used as current dependency
<- retained handover relation
<- previous-team report
<- observation/evidence route at earlier time
```

The historical/current and reported/observed distinctions become active only because collapsing them can change the status of the current assessment.

If the current assessment then relies on a test, the operator walks forward through the test's proposition, resolution, execution and return.

No new clinical primitive, moral selector or universal re-derivation rule is required.

---

# 8. FALSIFICATION TARGETS

Reject or demote this operator if hostile use shows any of the following:

1. **Backward-walk explosion:** routine uses expand toward the whole TRACE packet.
2. **Framing game:** a narrow represented `U` hides a broader operative use without a specific unresolved fork being recoverable.
3. **Representation laundering:** a selector can define the map/target/paraphrase so every represented dependency is clean while the consequential world relation remains invisible.
4. **Source recursion:** following representation paths creates an unbounded demand to inspect the provenance of every provenance record.
5. **Inheritance bureaucracy:** ordinary inherited knowledge requires re-derivation merely because it is inherited.
6. **Check recursion:** checks of checks expand indefinitely without a stopping rule.
7. **Instrument laundering:** a perfectly precommitted checker gains authority despite inability to discriminate the relevant alternative.
8. **Dependency laundering:** nominally separate checkers share the failure-producing evidence/control root.
9. **Unknown inflation:** generic uncertainty forces every branch open.
10. **Moral leakage:** `material`, `consequential`, `affected`, or `operative` silently selects what ought to matter rather than binding a declared downstream use.
11. **No repair delta:** the operator's location never changes the next corrective route.
12. **Existing grammar already fires:** ordinary disciplined use of TRACE already performs this walk without needing the operator statement.

The preferred falsification outcome is deletion.

---

# 9. STOPPING RULE

The walk stops branchwise when one of the following holds:

```text
A. collapsing the next available distinction cannot change U under the represented model;
B. the branch reaches a declared source/aperture boundary and further world access is unavailable;
C. a specific unresolved omission is preserved and no available bounded route can reduce it before the use;
D. further checking cannot change the status available before the relevant clock/hardening boundary;
E. the requested depth exceeds the declared profile/use boundary and the omitted depth is not itself load-bearing for U.
```

Stopping does not upgrade uncertainty to certainty.

```text
WALK_STOPPED != WORLD_COMPLETE
BOUNDED_READING != COMPLETE_WORLD_MODEL
NO_AVAILABLE_FURTHER_CHECK != CLAIM_TRUE
```

---

# 10. CURRENT DISPOSITION

Current preference:

```text
SEMANTIC ROOT:       NO
NEW PRIMITIVE:       NO
I/X/C AS PIPELINE:   REJECT
R/J/X/C AS ROOTS:    REJECT
R/J/X/C AS LOCAL DIAGNOSTIC SHORTHAND: POSSIBLY USEFUL
DEPENDENCY-PATH OPERATOR: HOSTILE-REVIEW CANDIDATE
```

The strongest deletion test is now:

> Can an unfamiliar receiver derive this bounded backward/forward walk directly from the existing spine quickly and reliably enough that this entire file adds no corrective work?

If yes, delete the file and carry only the surviving sentence into the spine or a profile.