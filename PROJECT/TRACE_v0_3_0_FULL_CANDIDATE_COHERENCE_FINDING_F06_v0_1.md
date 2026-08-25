# TRACE v0.3.0 full-candidate coherence finding F06

**Date:** 2026-08-25  
**Object attacked:** generated full working candidate after F05 repair  
**Status:** MATERIAL FINDING / WORKING / NON-CANON / UNVALIDATED  

## Finding

F05 repaired the hidden unit-cost assumption by reading a declared refinement cost and subtracting it from remaining tracing budget. The repair did not enforce the pre-existing formal requirement:

```text
cost_d(q_k) > 0
```

The operator currently distinguishes `UNKNOWN` and over-budget cost, but a declared zero or negative cost can pass those checks.

## Counterexamples

### Zero cost

```text
remaining budget = 2
refinement_cost = 0
```

The recursive call receives the same remaining budget. Repeated zero-cost refinements can therefore bypass the intended finite tracing budget.

### Negative cost

```text
remaining budget = 2
refinement_cost = -1
```

The computed next budget becomes 3. The act of refinement creates tracing budget, contradicting the formal budget semantics.

## Narrow diagnosis

This is a failed repair edge on F05, not a new semantic root and not a new primitive.

Existing `CLAIM` and `LIMIT` machinery is sufficient.

Required distinctions:

```text
DECLARED_COST != VALID_POSITIVE_COST
ZERO_REFINEMENT_COST != FREE_UNBOUNDED_RECURSION
NEGATIVE_REFINEMENT_COST != BUDGET_CREDIT
COST_RECORDED != COST_DOMAIN_VALID
```

## Repair contract

Before budget subtraction:

1. require the load-bearing refinement cost to satisfy the declared positive-cost domain;
2. preserve an invalid/nonpositive cost as a limit rather than treating it as affordable;
3. do not recurse on a zero or negative cost;
4. preserve the selected material target as unresolved when recursion is blocked for this reason;
5. keep the minimum schema unchanged and add no canonical primitive.

## Claim boundary

This is a source-level coherence finding against the current full working candidate. It is not a world-validity result, release recommendation, new primitive, new semantic root, validation, or canon change.
