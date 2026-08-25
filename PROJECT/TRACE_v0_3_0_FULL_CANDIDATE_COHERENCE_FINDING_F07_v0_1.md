# TRACE v0.3.0 full-candidate coherence finding F07

**Date:** 2026-08-25  
**Object attacked:** generated full working candidate after F06 repair  
**Status:** MATERIAL FINDING / WORKING / NON-CANON / UNVALIDATED

## Finding

The repaired recursive operator constructs the unresolved refinement target set and immediately calls the target selector:

```text
candidates <- unresolved_refinement_targets(R)
record_refinement_target_set_aperture(R, candidates)
target, refinement_basis <- select_refinement_target(candidates, ...)
```

There is no explicit branch for `candidates = empty` before target selection.

That is a distinct executable-state defect. A reading with no unresolved refinement targets should be able to terminate cleanly and record that bounded state. It should not require a selector to manufacture a target, return an undefined/null target, or infer that empty target-set discovery proves complete world coverage.

## Counterexample

Hold the represented graph, aperture, designation, measure and budget fixed.

```text
unresolved_refinement_targets(R) = empty
remaining tracing budget > 0
```

The current operator still calls `select_refinement_target(empty, ...)` before any stop evaluation. The formal recursion therefore has no explicit executable path for the ordinary case in which the declared unresolved target set is exhausted.

This matters because:

```text
NO_UNRESOLVED_TARGET_IN_DECLARED_SET
!= COMPLETE_WORLD_COVERAGE
```

Clean local completion and world completeness are different claims.

## Narrow diagnosis

No new primitive or semantic root is required. Existing target-set APERTURE, LIMIT, CLAIM, coverage and termination machinery is sufficient.

Required distinctions:

```text
EMPTY_REFINEMENT_TARGET_SET != SELECTABLE_TARGET
NO_UNRESOLVED_TARGET_IN_DECLARED_SET != COMPLETE_WORLD_COVERAGE
LOCAL_REFINEMENT_EXHAUSTED != REPRESENTATION_COMPLETE
NO_TARGET_SELECTED != SELECTOR_FAILURE
EMPTY_TARGET_SET != BOUNDED_SUFFICIENCY_WITHOUT_BASIS
```

## Repair contract

Before target selection:

1. record the discovered refinement target set and its aperture as already required;
2. if the declared unresolved target set is empty, do not call the selector;
3. record local target-set exhaustion as a termination state relative to the represented target-set aperture;
4. do not promote that state to complete coverage/world completeness;
5. preserve any existing aperture/representation limits that prevent the empty set from supporting stronger completeness claims;
6. keep the minimum schema unchanged and add no canonical primitive.

## Claim boundary

This is a source-level coherence finding against the current full working candidate. It is not a world-validity result, release recommendation, new primitive, new semantic root, validation, or canon change.
