# TRACE v0.3.0 full-candidate coherence finding F05

**Date:** 2026-08-25  
**Object attacked:** generated full working candidate after F04 repair  
**Status:** MATERIAL FINDING / WORKING / NON-CANON / UNVALIDATED  

## Finding

The recursive formal rule and executable operator disagree about tracing-budget consumption.

The formal rule defines a declared positive refinement cost:

```text
cost_d(q_k) > 0

d_(k+1)^rem = d_k^rem - cost_d(q_k)
```

and permits the next refinement only when the resulting remaining budget is non-negative.

The generated operator instead recurses with:

```text
depth_budget - 1
```

That silently assumes every refinement costs exactly one budget unit even though the formal semantics explicitly allow a declared non-unit cost.

## Counterexamples

### Undercharging

```text
remaining budget = 2
cost_d(selected target) = 3
```

The formal rule does not permit the refinement. The operator's `depth_budget - 1` leaves 1 and recurses.

### Overcharging

```text
remaining budget = 2
cost_d(selected target) = 0.25
```

The formal rule leaves 1.75. The operator leaves 1. A later refinement can therefore be suppressed solely by the implementation's hidden unit-cost assumption.

The mismatch can change which structures are admitted into the later map and therefore can change coverage, uncertainty, correction-window and proposed-transition outputs.

## Narrow diagnosis

No new primitive or semantic root is required. Existing `LIMIT`, `CLAIM`, measure, target-selection and termination machinery is sufficient.

Required distinctions:

```text
DECLARED_REFINEMENT_COST != UNIT_COST
BUDGET_REMAINS != NEXT_REFINEMENT_AFFORDABLE
BUDGET_DECREMENT != RECURSION_DEPTH_DECREMENT
COST_UNKNOWN != COST_ONE
REFINEMENT_SELECTED != REFINEMENT_BUDGET_FEASIBLE
```

## Repair contract

At the recursive use-site:

1. obtain the declared refinement cost for the selected target;
2. preserve `UNKNOWN` rather than defaulting an unresolved cost to one;
3. compute next remaining budget using that declared cost;
4. do not recurse when the next budget would be negative;
5. record budget exhaustion / unaffordability as a limit and preserve the unresolved target;
6. pass the computed remaining budget into the recursive call;
7. keep the minimum schema unchanged and add no canonical primitive.

## Claim boundary

This is a source-level coherence finding against the current full working candidate. It is not a world-validity result, release recommendation, new primitive, new semantic root, validation, or canon change.
