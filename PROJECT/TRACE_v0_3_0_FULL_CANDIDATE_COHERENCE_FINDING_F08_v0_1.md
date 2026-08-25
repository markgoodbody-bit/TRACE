# TRACE v0.3.0 full-candidate coherence finding F08

**Date:** 2026-08-25  
**Object attacked:** generated full working candidate after F07 repair  
**Status:** MATERIAL FINDING / WORKING / NON-CANON / UNVALIDATED

## Finding

The formal recursion budget is non-negative, but the executable operator enters recursive refinement only through:

```text
while depth_budget remains:
```

There is no explicit loop-entry path for an exhausted initial/recursive budget and no explicit rejection of an invalid negative remaining budget.

### Zero-budget case

```text
depth_budget = 0
```

The loop is skipped. The operator can continue to final output without recording that recursive differentiation did not run because its budget was exhausted. That can make a budget-truncated reading look like a reading that needed no further refinement.

### Negative-budget case

The formal rule declares remaining tracing budget non-negative. A negative input therefore lies outside the stated domain and must not be interpreted by an implementation-dependent truthiness rule as an ordinary remaining budget.

## Narrow diagnosis

This is a loop-entry propagation failure of the existing termination/budget discipline, not a new semantic root and not a new primitive.

Existing LIMIT, CLAIM, target-set aperture, coverage and termination machinery is sufficient.

Required distinctions:

```text
LOOP_NOT_ENTERED != RECURSION_COMPLETED
INITIAL_BUDGET_ZERO != NO_REFINEMENT_NEEDED
BUDGET_EXHAUSTED_AT_ENTRY != BOUNDED_SUFFICIENCY
NEGATIVE_TRACING_BUDGET != VALID_REMAINING_BUDGET
RECURSION_SKIPPED != COMPLETE_COVERAGE
```

## Repair contract

Before recursive target discovery:

1. enforce the declared non-negative domain of remaining tracing budget;
2. reject/preserve a negative budget as an invalid limit state rather than executing recursion;
3. when remaining budget is exactly zero, record budget-exhausted termination and preserve the resulting recursive coverage limit;
4. do not equate skipped recursion with bounded sufficiency or complete coverage;
5. enter target discovery only with positive remaining budget;
6. keep the minimum schema unchanged and add no canonical primitive.

## Claim boundary

This is a source-level coherence finding against the current full working candidate. It is not a world-validity result, release recommendation, new primitive, new semantic root, validation, or canon change.
