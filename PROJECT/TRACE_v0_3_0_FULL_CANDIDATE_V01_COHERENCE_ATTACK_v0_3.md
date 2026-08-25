# TRACE v0.3.0 full candidate v0.1 — coherence attack v0.3

**Date:** 2026-08-25  
**Current target:** `PROJECT/TRACE_FORMAL_SEED_v0_3_0_FULL_WORKING_CANDIDATE_v0_1.md`  
**Current target SHA-256:** `87037979556893b7e372389bd944aa1ff2d6fb294e6d59b09ac87596570c2af8`  
**Status:** MATERIAL NARROW FINDING / REPAIR REQUIRED  
**Claim ceiling:** self-attack evidence only; not validation, release, canon, authority, permission or clearance.

## Prior findings

F01 (local validator ancestry prose) and F02 (brake/rollback timing propagation) were found on prior generated candidates and repaired in the deterministic compiler. They remain failed ancestry rather than being rewritten as clean first-pass success.

## Finding F03 — recursive analytic target selection hides its own designation / measure

The current candidate correctly states in [10] that the choice of which structures TRACE makes visible is itself a designation, and that load-bearing comparative language must expose its comparison basis.

[11] then defines recursive differentiation as selecting an unresolved subobject:

```text
q_k = target(R_k, L_k)
```

and [13.2] operationalises this as:

```text
target <- highest_relevance_unresolved_node_or_edge(R)
```

The operator does not bind `highest_relevance` to a declared refinement target-set aperture, selection basis, designation, measure/materiality relation, or alternatives omitted because tracing budget is finite.

This matters because recursive tracing is budget-bounded. If only one further refinement can be afforded, selecting `q1` rather than `q2` changes what enters the later map. The attention-selection act can therefore affect downstream claims while presenting itself as neutral implementation detail.

### Counterexample

```text
unresolved candidates = {q1, q2}
remaining depth permits one refinement
hidden relevance rule chooses q1
q2 contains the dependency that would defeat a downstream completeness claim
```

A different legitimate relevance measure could choose q2. The map difference is caused partly by analytic target selection, not merely by world evidence.

### Classification

This is not world-action selection and does not grant TRACE operational authority. It is an internal analytic attention/coverage selection that belongs to existing:

```text
APERTURE
TARGET-SET APERTURE
DESIGNATION
MEASURE
SELECTOR / selection-basis representation where useful
LIMIT / omitted category handling
```

No new `ATTENTION`, `REFINEMENT`, `PRIORITY`, or `RELEVANCE` primitive is earned.

### Required repair

Retain targeted recursion, but expose the selection where it can change the reading:

```text
candidate unresolved refinement targets
refinement target-set aperture / known omissions
selection basis
relevance/materiality measure where comparative language is used
selected target
material alternatives not selected
budget-driven omissions
```

`highest relevance` may be used only when the ordering is actually declared and supported. Otherwise record the basis as unresolved rather than laundering an implementation heuristic into a neutral structural fact.

When unexplored candidates could materially alter a downstream load-bearing claim, finite budget must remain visible in limits/omissions.

### Preserve

```text
ANALYTIC_TARGET_SELECTION != WORLD_ACTION_SELECTION
ANALYTIC_TARGET_SELECTION != NEUTRAL
HIGHEST_RELEVANCE != MEASURE_FREE
TARGET_SELECTED_FOR_REFINEMENT != TARGET_MOST_IMPORTANT_IN_WORLD
TARGETED_REFINEMENT != COMPLETE_COVERAGE
OMITTED_BY_BUDGET != IRRELEVANT
FINITE_TRACING_BUDGET != COMPLETE_REPRESENTATION
REFINEMENT_TARGET_SET != WORLD_SCOPE
```

## Disposition

Repair the full compiler with a bounded recursion-target-selection transform over [11] and [13.2]. Use existing target-set, designation, measure, selector and limit machinery. Add fail-closed regression tokens. Do not expand minimum-schema vocabulary and do not merge/release/canon from this result.
