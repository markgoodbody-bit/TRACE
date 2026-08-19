# TRACE v0.3.0 — DEPENDENCY-PATH OPERATOR CANDIDATE v0.4

**Status:** WORKING DERIVED OPERATOR — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE — NO NEW PRIMITIVE CLAIM  
**Evidence:** `TRACE_v0_3_0_DEPENDENCY_PATH_TRANSFER_REPORT_v0_2.md`

## 0. Invocation boundary

TRACE already has a voluntary reading operator:

```text
(R, L) = tau(X, Pi_declared, H_declared, d, P)
```

Do not add a universal `TRIGGER` primitive.

Instead, when the declared profile/comparison context `P` includes a downstream use or transition whose support depends on the reading, the dependency-path walk is a **conditional subroutine of that TRACE reading**.

```text
TRACE_READING_INVOKED + DECLARED_USE_CONTEXT
  -> DEPENDENCY_PATH_WALK_APPLICABLE
```

This does not claim that a surrounding system will invoke TRACE at the right time.

```text
TRACE_AVAILABLE != TRACE_INVOKED
TRACE_READING_INVOKED != SYSTEM_GUARD_INSTALLED
OPERATOR_DEFINED != WORLD_LEVEL_ENFORCEMENT
```

Where no declared use/transition context exists, the operator does not invent one merely to keep itself active.

## 1. Core walk

For the declared downstream use/transition bound in `P`:

1. Walk backward through the represented dependencies and representation paths that supply it.
2. Preserve an existing TRACE distinction only where collapsing it can change that use under the represented model.
3. Preserve a specific unresolved omission or alternate-use fork when it would change the traversed dependency set; generic possible omission does not keep every branch open.
4. Where the use relies on a check, walk the check forward through exact proposition, evidence/target aperture, instrument resolution, dependency/control structure, timing, execution, result route and return to use.
5. Stop branchwise when further traversal cannot change the declared use, when a declared access boundary is reached, or when further checking cannot change the status available before the relevant use/hardening boundary.

No new semantic object is required.

## 2. Use scope remains aperture-bound

Binding a use in `P` does not make that use exhaustive.

Where use-scope completeness itself changes the walk, reuse existing aperture/target-set machinery:

```text
DECLARED_USE != EXHAUSTIVE_USE
REPRESENTED_USE != OPERATIVE_USE
USE_SCOPE_DECLARED != USE_SCOPE_COMPLETE
NOT_REPRESENTED_AS_USE != NO_DOWNSTREAM_EFFECT
```

Keep a broader-use fork only when a specific alternate use/transition can be named that changes the dependency set.

This does not require inspection of every imaginable future use.

## 3. Representation path is part of the dependency path

Existing TRACE machinery should carry relevant transformations:

```text
source/world -> target-set selection
source object -> observed rendering
utterance -> paraphrase / speech-act typing
record -> supplied excerpt
supplied claim -> retained map relation
historical report -> current-state use
```

Use existing `APERTURE / MAP / CLAIM / EVIDENCE / PROVENANCE / SOURCE / ROUTE / TARGET-SET / BOUNDS / OMITS / DISPUTES / RETAINED HISTORY` structure.

```text
APERTURE_OUTPUT != COMPLETE_SCENE
OBSERVED_RENDERING != SOURCE_OBJECT
RETAINED_HISTORY != CURRENT_WORLD
TRACE_OUTPUT != RECEIVER_MAP_UPDATE
SOURCE_PROVENANCE != PROPOSITION_SUPPORT
NOT_TARGETED != ABSENT
```

## 4. Check path

Where load-bearing, preserve:

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

A check result can become later input, so the walk is recursive rather than a one-way stage pipeline.

## 5. Pre-claim integration

Supplied material can shape standing map before a later explicit claim exists.

If a receiving architecture exposes an integration/retention transition and that transition is bound as the declared use context in `P`, the same walk can inspect it.

```text
SUPPLIED_MATERIAL -> DECLARED RETAIN / INTEGRATE TRANSITION
```

This is conditional, not a universal memory-audit requirement.

```text
RECEPTION != ADOPTION
TRACE_OUTPUT != RECEIVER_MAP_UPDATE
INHERITED != FALSE
INHERITED != UNUSABLE
ADOPTION != VALIDATION
CONCEPTUAL_REFUSAL != PRACTICAL_REFUSAL_ROUTE
```

If the architecture exposes no integration boundary, TRACE can describe that limit but cannot install the missing mechanism by description.

## 6. Optional repair location

Where it changes the next corrective route, ordinary language may locate the first actionable defect at:

```text
representation / target / rendering path
receiver integration / retained relation
dormant distinction at declared use
check / instrument / execution / return route
```

Do not promote these to roots.

```text
DIAGNOSTIC_LOCATION != SEMANTIC_PRIMITIVE
OBSERVED_FAILURE_LOCATION != UNIQUE_CAUSAL_ORIGIN
DIAGNOSTIC_LOCATION != BLAME
FIRST_VISIBLE_FAILURE != ONLY_FAILURE
```

If the location does not change the repair, omit it.

## 7. Stopping ceiling

```text
WALK_STOPPED != WORLD_COMPLETE
BOUNDED_READING != COMPLETE_WORLD_MODEL
NO_AVAILABLE_FURTHER_CHECK != CLAIM_TRUE
```

Stopping is a use/resource boundary, not an epistemic upgrade.

## 8. Remaining invocation ceiling

Binding the walk inside `tau` repairs only **intra-reading dormancy**.

It does not repair failure to invoke TRACE at all.

```text
INTRA_READING_OPERATOR_INSTALLED != EXTERNAL_INVOCATION_GUARANTEED
```

A domain profile may mechanically invoke TRACE at an executable transition boundary, but that is profile/software machinery, not a universal TRACE truth.

Where no executable invocation surface exists, dependence on aperture discipline remains explicit.

## 9. Falsification targets

Hold or delete this candidate if hostile use shows:

- binding use context in `P` is semantically incompatible with the spine's current meaning of `P`;
- the receiver can game `P` by declaring an artificially narrow use without a recoverable specific fork;
- routine walks expand toward the full TRACE packet;
- representation/check provenance creates unbounded recursion;
- pre-claim integration becomes universal memory/learning bureaucracy;
- the stopping rule closes a branch that later proves load-bearing under information available at the time;
- the conditional subroutine is still routinely skipped inside otherwise valid TRACE readings;
- `material`, `consequential`, `affected`, or use-scope selection imports a hidden value selector;
- locating the defect does not change the available repair;
- existing TRACE already derives and invokes this walk reliably enough that this candidate is redundant.

One counterexample is enough to hold integration.

## 10. Current disposition

```text
NEW PRIMITIVE:                        NO
I/X/C AS PIPELINE:                    REJECT
R/J/X/C AS ROOTS:                     REJECT
USE-SCOPE NEW PRIMITIVE:              NO
UNIVERSAL WORLD-LEVEL TRIGGER:        NO
CONDITIONAL tau SUBROUTINE:           HOSTILE-REVIEW CANDIDATE
EXTERNAL INVOCATION GUARANTEE:        NONE
PREFERRED FINAL STATUS:               DERIVED / SMALLER / POSSIBLY DELETE
```

The remaining empirical question is now narrower:

> When an unfamiliar receiver has already chosen to make a TRACE reading with a declared use context, does this conditional walk fire and stop cheaply enough to prevent the demonstrated collapses?

That can be tested cold.
