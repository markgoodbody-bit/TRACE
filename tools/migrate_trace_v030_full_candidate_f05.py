#!/usr/bin/env python3
"""One-shot exact migration for full-candidate coherence finding F05.

Edits only the deterministic v0.3 compiler and fails closed unless the expected
post-F04 compiler anchors are present exactly. This script is migration
evidence, not semantic validation.
"""

from pathlib import Path

P = Path(__file__).with_name("compile_trace_v030_full_candidate.py")
text = P.read_text(encoding="utf-8")


def replace_once(anchor: str, replacement: str, label: str) -> None:
    global text
    count = text.count(anchor)
    if count != 1:
        raise SystemExit(f"{label}: expected anchor count 1, observed {count}")
    text = text.replace(anchor, replacement, 1)


# 1. Propagate the narrow F05 budget/cost distinctions.
supp_anchor = '''    "AUTHORITY_REACHED != ANALYSIS_COMPLETE",\n)\n\nSURVIVAL_REQUIRED = (\n'''
supp_new = '''    "AUTHORITY_REACHED != ANALYSIS_COMPLETE",\n    "DECLARED_REFINEMENT_COST != UNIT_COST",\n    "BUDGET_REMAINS != NEXT_REFINEMENT_AFFORDABLE",\n    "COST_UNKNOWN != COST_ONE",\n    "REFINEMENT_SELECTED != REFINEMENT_BUDGET_FEASIBLE",\n)\n\nSURVIVAL_REQUIRED = (\n'''
replace_once(supp_anchor, supp_new, "F05 supplemental propagation")

survival_anchor = '''    "BUDGET_EXHAUSTED != NO_MATERIAL_UNRESOLVED_TARGET",\n    "AUTHORITY_REACHED != ANALYSIS_COMPLETE",\n)\n\n\ndef sha256_bytes'''
survival_new = '''    "BUDGET_EXHAUSTED != NO_MATERIAL_UNRESOLVED_TARGET",\n    "AUTHORITY_REACHED != ANALYSIS_COMPLETE",\n    "DECLARED_REFINEMENT_COST != UNIT_COST",\n    "BUDGET_REMAINS != NEXT_REFINEMENT_AFFORDABLE",\n    "COST_UNKNOWN != COST_ONE",\n    "REFINEMENT_SELECTED != REFINEMENT_BUDGET_FEASIBLE",\n)\n\n\ndef sha256_bytes'''
replace_once(survival_anchor, survival_new, "F05 survival propagation")

# 2. Bind the declared formal refinement cost to executable budget use.
insert_anchor = '''    recursion_stop_guard = r"""Recursion termination use rule:\n'''
transform = r'''    recursion_budget_guard = r"""Refinement-budget use rule:

The declared tracing cost of a selected refinement is load-bearing. The
operator must not silently replace `cost_d(q_k)` with a unit decrement.
Before recursion, bind the selected target to a supported refinement-cost claim,
compute the next remaining budget on the same declared budget basis, and recurse
only if the next budget is non-negative.

```text
DECLARED_REFINEMENT_COST != UNIT_COST
BUDGET_REMAINS != NEXT_REFINEMENT_AFFORDABLE
BUDGET_DECREMENT != RECURSION_DEPTH_DECREMENT
COST_UNKNOWN != COST_ONE
REFINEMENT_SELECTED != REFINEMENT_BUDGET_FEASIBLE
```

If the load-bearing refinement cost is `UNKNOWN`, do not default it to one.
Preserve budget feasibility as unresolved. If the declared cost exceeds the
remaining budget, record exhaustion/insufficiency and preserve the selected
material target as unresolved rather than executing an unaffordable refinement.
No budget, resource or cost primitive is added.

"""
    b.insert_before_once(
        "T_RECURSION_BUDGET_COST",
        "When \\(d_{k+1}^{rem}\\ge0\\):",
        recursion_budget_guard,
    )

'''
replace_once(insert_anchor, transform + insert_anchor, "F05 budget-rule insertion")

# 3. Make the operator consume the declared cost rather than an implicit unit.
ps_old = '''        if stop:\n            record_refinement_stop_basis_and_limits(R, L, target, stop_basis)\n            if not supported_bounded_sufficiency(stop_basis):\n                preserve_material_unresolved_after_truncation_or_handoff(\n                    R, L, candidates, target, stop_basis)\n            break\n        R <- merge_graphs(R, TRACE(target, aperture, history,\n                                   depth_budget - 1, primitive_aperture))\n'''
ps_new = '''        if stop:\n            record_refinement_stop_basis_and_limits(R, L, target, stop_basis)\n            if not supported_bounded_sufficiency(stop_basis):\n                preserve_material_unresolved_after_truncation_or_handoff(\n                    R, L, candidates, target, stop_basis)\n            break\n        refinement_cost <- declared_refinement_cost(target, R, L)\n        if refinement_cost is UNKNOWN:\n            preserve_unknown_refinement_cost_and_budget_feasibility(R, L, target)\n            break\n        next_depth_budget <- depth_budget - refinement_cost\n        if next_depth_budget < 0:\n            record_budget_exhaustion_before_refinement(\n                R, L, target, depth_budget, refinement_cost)\n            preserve_material_unresolved_after_budget_exhaustion(R, L, target)\n            break\n        R <- merge_graphs(R, TRACE(target, aperture, history,\n                                   next_depth_budget, primitive_aperture))\n'''
replace_once(ps_old, ps_new, "F05 operator budget-cost binding")

# 4. Require the repaired semantics in deterministic output.
required_anchor = '''        "preserve_material_unresolved_after_truncation_or_handoff",\n    )\n'''
required_new = '''        "preserve_material_unresolved_after_truncation_or_handoff",\n        "DECLARED_REFINEMENT_COST != UNIT_COST",\n        "BUDGET_REMAINS != NEXT_REFINEMENT_AFFORDABLE",\n        "declared_refinement_cost",\n        "record_budget_exhaustion_before_refinement",\n        "preserve_unknown_refinement_cost_and_budget_feasibility",\n    )\n'''
replace_once(required_anchor, required_new, "F05 required tokens")

# 5. Reject the old hidden unit-cost decrement if it reappears.
bad_anchor = '''        "if stop_condition(target, R, L): break",\n    )\n'''
bad_new = '''        "if stop_condition(target, R, L): break",\n        "depth_budget - 1",\n    )\n'''
replace_once(bad_anchor, bad_new, "F05 stale-control rejection")

# 6. Account for the repair in generated document control.
doc_anchor = '''recursive analytic target-selection binding\nrecursive termination provenance / truncation binding\noperator/checker discrimination\n'''
doc_new = '''recursive analytic target-selection binding\nrecursive termination provenance / truncation binding\nrecursive declared-cost / budget-consumption binding\noperator/checker discrimination\n'''
replace_once(doc_anchor, doc_new, "F05 document-control accounting")

P.write_text(text, encoding="utf-8")
print("F05 compiler migration applied exactly.")
