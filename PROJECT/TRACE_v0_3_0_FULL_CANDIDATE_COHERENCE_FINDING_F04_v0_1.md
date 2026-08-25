# TRACE v0.3.0 full-candidate coherence finding F04

**Date:** 2026-08-25  
**Object attacked:** generated full working candidate after F03 repair  
**Status:** MATERIAL FINDING / WORKING / NON-CANON / UNVALIDATED  

## Finding

F03 exposes which unresolved refinement target receives analytic attention under a finite tracing budget. The generated operator still terminates recursion with:

```text
if stop_condition(target, R, L): break
```

without requiring the stopping ground, its evidence/basis, or its downstream consequence to be recorded.

That collapses materially different histories into the same apparent terminal output. For example, a reading may stop because:

- further differentiation is no longer materially relevant under a declared measure;
- uncertainty cannot be reduced with available access;
- tracing budget is exhausted;
- further tracing costs exceed expected informational value under a declared measure;
- a reversible transition can preserve time;
- an irreversible clock requires handoff to a connected brake or authority;
- available authority has been reached.

Those are not interchangeable. In particular, stopping for bounded sufficiency is not the same warrant state as stopping because budget, access, authority, or time prevented further work.

## Counterexample pair

Hold the current graph, candidate target set, selected target, designation, measure, and represented world evidence fixed.

### Case A — bounded sufficiency

A supported declared measure establishes that further refinement of the selected target is not materially relevant to the load-bearing downstream claim. Recursion stops.

### Case B — forced truncation

The same selected target remains materially unresolved, but available access or tracing budget is exhausted. Recursion stops.

Under the current operator both can execute the same visible `break`. Nothing in that line requires the final packet to distinguish why tracing ended.

The difference is material: Case A may support a bounded sufficiency claim; Case B must preserve unresolved truncation and must not inherit the same epistemic posture.

## Narrow diagnosis

This is not a new semantic root and does not earn a `STOP`, `TERMINATION`, or `SUFFICIENCY` primitive.

Existing `CLAIM`, `LIMIT`, `APERTURE`, `CLOCK`, `ROUTE`, designation, measure, evidence-state and handoff machinery is sufficient if the firing event is explicitly carried into the result.

Required distinctions:

```text
STOPPED != COMPLETED
STOP_REASON_DECLARED != STOP_REASON_SUPPORTED
STOP_FOR_BOUNDED_SUFFICIENCY != STOP_FOR_RESOURCE_EXHAUSTION
STOP_FOR_HANDOFF != STOP_FOR_SUFFICIENCY
TERMINATION != COMPLETE_COVERAGE
BUDGET_EXHAUSTED != NO_MATERIAL_UNRESOLVED_TARGET
ACCESS_EXHAUSTED != QUESTION_RESOLVED
AUTHORITY_REACHED != ANALYSIS_COMPLETE
```

## Repair contract

At the recursion use-site:

1. evaluate the stop condition into an explicit result rather than a bare boolean;
2. record the stop basis / supporting claim refs and relevant measure, limit, clock, route or authority refs;
3. distinguish bounded-sufficiency termination from truncation / handoff / resource exhaustion;
4. preserve unresolved material alternatives when termination is not supported as bounded sufficiency;
5. ensure final confidence / coverage language remains relative to the recorded termination state;
6. do not add a canonical primitive or expand the minimum schema.

## Claim boundary

This finding establishes a source-level coherence defect in the current working candidate. It does not establish a world failure, validation result, release recommendation, new primitive, new semantic root, or canon change.
