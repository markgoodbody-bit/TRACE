# TRACE v0.3.0 full-candidate coherence finding F09

**Date:** 2026-08-25  
**Object attacked:** generated full working candidate after F08 repair  
**Status:** MATERIAL FINDING / WORKING / NON-CANON / UNVALIDATED

## Finding

Recursive TRACE returns both a graph and limits:

```text
(R_qk, L_qk) = tau(...)
```

but the formal recursion only specifies graph merge:

```text
R_(k+1) = merge(R_k, R_qk)
```

and the executable operator similarly performs:

```text
R <- merge_graphs(R, TRACE(...))
```

without explicitly merging the recursively returned limits into parent `L`.

A deeper-scale graph contribution can therefore survive while the deeper-scale uncertainty, omitted categories, unavailable capabilities, truncation reasons or other limits that qualify it fail to propagate to the parent output.

## Counterexample

At parent scale, target `q` is selected and affordable.

The recursive child returns:

```text
R_q: a dependency relation that materially changes the parent map
L_q: source access unavailable; causal attribution unresolved
```

If `R_q` is merged while `L_q` is not, the parent can expose the dependency without carrying the very limit that prevents a stronger causal claim.

That is not merely missing metadata. It changes the warrant available at the parent scale.

## Narrow diagnosis

This is an inherited recursive-integration / limit-propagation defect. It does not earn a new primitive or semantic root.

`L` already exists precisely for limits, unresolved questions, omitted categories and unavailable capabilities.

Required distinctions:

```text
RECURSIVE_GRAPH_MERGE != RECURSIVE_LIMIT_MERGE
CHILD_GRAPH_VISIBLE != CHILD_LIMIT_VISIBLE
DEEPER_UNCERTAINTY != DISPENSABLE
GRAPH_CONTRIBUTION_SURVIVED != QUALIFYING_LIMIT_SURVIVED
CHILD_GRAPH_MERGED + CHILD_LIMIT_DROPPED != RECURSIVE_INTEGRATION
```

## Repair contract

1. bind the recursive return explicitly as `child_R, child_L`;
2. merge `child_R` into parent `R`;
3. merge/carry `child_L` into parent `L` with enough scope/provenance to retain which recursive target produced it;
4. do not let duplicate suppression erase materially distinct limit provenance;
5. preserve the same rule in the formal recursion, executable pseudocode and survival guards;
6. keep the minimum schema unchanged and add no canonical primitive.

## Claim boundary

This is a source-level coherence finding against the current full working candidate and may reflect inherited donor ancestry. It is not a world-validity result, release recommendation, new primitive, new semantic root, validation, or canon change. Released v0.2.7 remains untouched.
