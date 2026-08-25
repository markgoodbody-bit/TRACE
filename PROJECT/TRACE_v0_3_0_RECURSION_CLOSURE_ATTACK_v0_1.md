# TRACE v0.3.0 recursion closure attack v0.1

**Date:** 2026-08-25  
**Object:** full working candidate after F09 repair  
**Scope:** recursive refinement control-flow and propagation only  
**Verdict:** CLEAR_WITH_RESIDUAL_LIMITS  
**Status:** WORKING / NON-CANON / UNVALIDATED

## Purpose

This is a bounded closure attack after findings F03–F09. It asks whether the repaired recursive refinement path still contains a materially distinct source-level failure across its main entry, selection, stopping, budget, recursion and merge states.

It is not a general TRACE validation, runtime implementation test, release gate, or proof that no other defect exists.

## Cases

| # | Counterexample / state | Required behaviour | Current source-level disposition |
|---|---|---|---|
| 1 | negative entry budget | reject as outside declared non-negative domain; preserve limit; do not recurse | RESISTS — explicit invalid-negative entry path |
| 2 | zero entry budget | record budget-exhausted termination/coverage limit; do not imply no refinement needed | RESISTS — explicit zero-entry path |
| 3 | positive budget, empty unresolved target set | do not invoke selector; record local target-set exhaustion relative to aperture | RESISTS — empty set handled before selection |
| 4 | multiple candidates, unsupported ordering, unselected material alternative | preserve selection basis as UNKNOWN and material selection uncertainty | RESISTS — basis/aperture/omission path explicit |
| 5 | supported bounded-sufficiency stop | record stop basis; permit bounded termination without claiming world completeness | RESISTS — stop basis carried |
| 6 | stop caused by access/time/authority/truncation rather than sufficiency | preserve unresolved material alternatives and limit/handoff state | RESISTS — non-sufficiency stop path explicit |
| 7 | refinement cost UNKNOWN | do not default to unit cost; preserve budget feasibility as unresolved | RESISTS — explicit UNKNOWN-cost branch |
| 8 | zero or negative refinement cost | reject as invalid cost domain; do not create free recursion or budget credit | RESISTS — explicit nonpositive-cost branch |
| 9 | positive refinement cost exceeds remaining budget | do not recurse; record exhaustion and preserve selected unresolved target | RESISTS — explicit unaffordable-cost branch |
| 10 | positive refinement cost exactly equals remaining budget | recurse with zero child budget; child records entry-budget exhaustion rather than silently appearing complete | RESISTS — computed remaining budget is passed recursively and zero-entry path exists |
| 11 | positive affordable refinement cost | recurse using declared cost rather than unit decrement | RESISTS — `next_depth_budget` is computed from declared cost |
| 12 | child returns graph contribution plus qualifying limits | merge both graph and child limits; retain recursive target/scope provenance | RESISTS — formal `R` and `L` merge plus executable child-limit merge |

## Findings encountered during closure

The pass did not begin clean. It exposed and preserved four additional recursion defects after F03:

```text
F04  stop reason / termination provenance
F05  declared refinement cost != hidden unit decrement
F06  recorded cost != valid positive cost
F07  empty unresolved target set != selectable target
F08  loop not entered != recursion completed
F09  recursive graph merge != recursive limit merge
```

Each failed object remains preserved. None earned a new canonical primitive or semantic root.

## Closure verdict

No further materially distinct recursion failure survived the bounded 12-case pass after F09 repair.

```text
CLEAR_WITH_RESIDUAL_LIMITS
```

This means only:

- the tested source-level recursion seams now have an explicit handling path;
- the donor/minimum-schema boundary remains unchanged;
- the current deterministic full working candidate can move on to a different coherence surface.

It does **not** mean:

```text
SOURCE_LEVEL_CLOSURE != RUNTIME_VALIDATION
BOUNDED_CASE_CLEAR != COMPLETE_CORRECTNESS
PSEUDOCODE_PATH_PRESENT != IMPLEMENTATION_EXISTS
RECursion_CLUSTER_CLEAR != TRACE_VALIDATED
NO_NEW_FINDING_IN_12_CASES != NO_OTHER_DEFECT
```

## Residual limits

1. Operator functions remain abstract semantic operations rather than a complete executable implementation.
2. Materiality, designation, measure, access, evidence quality and target-set construction remain declared/contextual rather than universally solved.
3. This pass did not reopen unrelated full-candidate surfaces such as packet/checker behaviour, brake independence, carrier behaviour, worked-transfer fidelity, or all cross-section interactions.
4. Generated/build success proves deterministic assembly against the current compiler contract, not world validity or semantic completeness.

## Next boundary

Stop attacking recursion for now. Preserve F03–F09 as ancestry and move to a different full-candidate coherence surface only if it is materially motivated.

No merge, release, canon, validation, new primitive or new semantic root follows from this closure result.
