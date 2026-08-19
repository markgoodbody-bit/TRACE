# TRACE v0.3.0 — DEPENDENCY-PATH OPERATOR CANDIDATE v0.3

**Status:** WORKING DERIVED OPERATOR — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE — NO NEW PRIMITIVE CLAIM  
**Evidence:** `TRACE_v0_3_0_DEPENDENCY_PATH_TRANSFER_REPORT_v0_1.md`

## Core operator

For a declared downstream use or transition:

1. Walk backward through the represented dependencies and representation paths that supply it.
2. Preserve an existing TRACE distinction only where collapsing it can change that use under the represented model.
3. If a specific unresolved omission or alternate use would change the dependency set, preserve that fork; generic possible omission does not keep every branch open.
4. Where the use relies on a check, walk the check forward through exact proposition, evidence/target aperture, instrument resolution, dependency/control structure, timing, execution, result route and return to use.
5. Stop branchwise when further traversal cannot change the declared use, when a declared access boundary is reached, or when further checking cannot change the status available before the relevant use/hardening boundary.

This is a derived inspection rule over existing TRACE structure, not a new semantic kind.

## Use scope is aperture-bound

A declared use may be narrower than the transition actually selected or justified. Where that matters, reuse existing aperture/target-set machinery for the use scope:

```text
DECLARED_USE != EXHAUSTIVE_USE
REPRESENTED_USE != OPERATIVE_USE
USE_SCOPE_DECLARED != USE_SCOPE_COMPLETE
NOT_REPRESENTED_AS_USE != NO_DOWNSTREAM_EFFECT
```

Keep a broader-use fork only when a specific alternate use/transition can be named that would change the traversed dependencies.

## Representation path is part of the dependency path

Existing TRACE structure should carry transformations such as:

```text
source/world -> target-set selection
source object -> observed rendering
utterance -> paraphrase / speech-act typing
record -> supplied excerpt
supplied claim -> retained map relation
historical report -> current-state use
```

Use existing `APERTURE / MAP / CLAIM / EVIDENCE / PROVENANCE / SOURCE / ROUTE / TARGET-SET / BOUNDS / OMITS / DISPUTES / RETAINED HISTORY` machinery. No representation primitive is proposed.

```text
APERTURE_OUTPUT != COMPLETE_SCENE
OBSERVED_RENDERING != SOURCE_OBJECT
RETAINED_HISTORY != CURRENT_WORLD
TRACE_OUTPUT != RECEIVER_MAP_UPDATE
SOURCE_PROVENANCE != PROPOSITION_SUPPORT
NOT_TARGETED != ABSENT
```

## Check path

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

A check result can become a new record/world input, so this is recursive rather than a one-way stage pipeline.

## Invocation ceiling

The operator can itself remain dormant.

```text
OPERATOR_DEFINED != OPERATOR_INVOKED
OPERATOR_AVAILABLE != OPERATOR_USED
DISTINCTION_RECOVERABLE != DISTINCTION_APPLIED
```

TRACE core does not claim a universal invocation trigger. A domain profile may bind invocation to an executable transition boundary, but:

```text
PROFILE_BOUND_TRIGGER != UNIVERSAL_TRACE_TRIGGER
UNEXECUTABLE_OPERATOR != INSTALLED_GUARD
MACHINE_CHECK_AVAILABLE != MACHINE_CHECK_RAN
```

Where no executable invocation surface exists, dependence on aperture discipline stays explicit.

## Pre-claim / pre-use integration

Supplied material may shape standing map before a later explicit claim exists. If the receiving architecture exposes an integration/retention transition, that transition may itself be the local downstream use for this operator.

```text
RECEPTION != ADOPTION
TRACE_OUTPUT != RECEIVER_MAP_UPDATE
INHERITED != FALSE
INHERITED != UNUSABLE
ADOPTION != VALIDATION
CONCEPTUAL_REFUSAL != PRACTICAL_REFUSAL_ROUTE
```

If no observable integration boundary exists, TRACE can describe that limitation but cannot install one by description.

## Optional diagnostic location

When it changes the repair, ordinary language may locate the first actionable defect at representation route, receiver integration, dormant distinction, or check/return path. Short labels are optional and local only.

```text
DIAGNOSTIC_LOCATION != SEMANTIC_PRIMITIVE
OBSERVED_FAILURE_LOCATION != UNIQUE_CAUSAL_ORIGIN
DIAGNOSTIC_LOCATION != BLAME
FIRST_VISIBLE_FAILURE != ONLY_FAILURE
```

If the location does not change the next corrective route, omit it.

## Stopping ceiling

```text
WALK_STOPPED != WORLD_COMPLETE
BOUNDED_READING != COMPLETE_WORLD_MODEL
NO_AVAILABLE_FURTHER_CHECK != CLAIM_TRUE
```

Stopping is a resource/use boundary, not an epistemic upgrade.

## Falsification targets

Hold or delete this operator if hostile use shows any of the following:

- routine walks expand toward the whole TRACE packet;
- use-scope aperture merely relocates self-declared materiality;
- a narrow use declaration hides a consequential transition without a specific recoverable fork;
- representation/check provenance creates unbounded recursion;
- inherited knowledge becomes universal re-derivation bureaucracy;
- an executable profile trigger is mistaken for a universal TRACE requirement;
- stopping closes a branch that later proves load-bearing under information available at the time;
- `material`, `consequential`, `affected`, or use-scope selection imports a hidden value selector;
- locating the defect does not change the available repair;
- ordinary TRACE already derives and invokes this walk reliably enough that the operator adds no corrective work.

One counterexample is enough to hold integration.

## Current disposition

```text
NEW PRIMITIVE:               NO
I/X/C AS PIPELINE:           REJECT
R/J/X/C AS ROOTS:            REJECT
USE-SCOPE NEW PRIMITIVE:     NO
UNIVERSAL INVOCATION RULE:   NO
DEPENDENCY-PATH OPERATOR:    HOSTILE-REVIEW CANDIDATE
PREFERRED FINAL STATUS:      DERIVED / SMALLER / POSSIBLY DELETE
```

The remaining question is practical:

> Can an unfamiliar receiver invoke and stop this bounded walk cheaply enough in real use that it changes behaviour without becoming another correct rule that sits dormant?

If not, this candidate has rediscovered the problem rather than repaired it.
