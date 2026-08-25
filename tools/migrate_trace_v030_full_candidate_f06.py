#!/usr/bin/env python3
"""One-shot exact migration for full-candidate coherence finding F06.

Edits only the deterministic v0.3 compiler and fails closed unless the expected
post-F05 compiler anchors are present exactly. This script is migration
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


# 1. Propagate the narrow F06 domain-validity distinctions.
supp_anchor = '''    "REFINEMENT_SELECTED != REFINEMENT_BUDGET_FEASIBLE",\n)\n\nSURVIVAL_REQUIRED = (\n'''
supp_new = '''    "REFINEMENT_SELECTED != REFINEMENT_BUDGET_FEASIBLE",\n    "DECLARED_COST != VALID_POSITIVE_COST",\n    "ZERO_REFINEMENT_COST != FREE_UNBOUNDED_RECURSION",\n    "NEGATIVE_REFINEMENT_COST != BUDGET_CREDIT",\n    "COST_RECORDED != COST_DOMAIN_VALID",\n)\n\nSURVIVAL_REQUIRED = (\n'''
replace_once(supp_anchor, supp_new, "F06 supplemental propagation")

survival_anchor = '''    "COST_UNKNOWN != COST_ONE",\n    "REFINEMENT_SELECTED != REFINEMENT_BUDGET_FEASIBLE",\n)\n\n\ndef sha256_bytes'''
survival_new = '''    "COST_UNKNOWN != COST_ONE",\n    "REFINEMENT_SELECTED != REFINEMENT_BUDGET_FEASIBLE",\n    "DECLARED_COST != VALID_POSITIVE_COST",\n    "ZERO_REFINEMENT_COST != FREE_UNBOUNDED_RECURSION",\n    "NEGATIVE_REFINEMENT_COST != BUDGET_CREDIT",\n    "COST_RECORDED != COST_DOMAIN_VALID",\n)\n\n\ndef sha256_bytes'''
replace_once(survival_anchor, survival_new, "F06 survival propagation")

# 2. Make the existing formal cost domain explicit at the use-site.
insert_anchor = '''    recursion_stop_guard = r"""Recursion termination use rule:\n'''
transform = r'''    recursion_cost_domain_guard = r"""Refinement-cost domain use rule:

The formal recursion contract requires `cost_d(q_k) > 0`. Recording a cost does
not establish that it belongs to that domain. Before budget subtraction, reject
zero or negative refinement costs as invalid for this recursion budget.

```text
DECLARED_COST != VALID_POSITIVE_COST
ZERO_REFINEMENT_COST != FREE_UNBOUNDED_RECURSION
NEGATIVE_REFINEMENT_COST != BUDGET_CREDIT
COST_RECORDED != COST_DOMAIN_VALID
```

An invalid/nonpositive cost blocks this refinement path and remains visible as a
limit; it does not create free recursion or increase remaining budget. No new
primitive is added.

"""
    b.insert_before_once(
        "T_RECURSION_COST_DOMAIN",
        "When \\(d_{k+1}^{rem}\\ge0\\):",
        recursion_cost_domain_guard,
    )

'''
replace_once(insert_anchor, transform + insert_anchor, "F06 cost-domain insertion")

# 3. Enforce positivity before subtraction in the generated operator.
ps_old = '''        if refinement_cost is UNKNOWN:\n            preserve_unknown_refinement_cost_and_budget_feasibility(R, L, target)\n            break\n        next_depth_budget <- depth_budget - refinement_cost\n'''
ps_new = '''        if refinement_cost is UNKNOWN:\n            preserve_unknown_refinement_cost_and_budget_feasibility(R, L, target)\n            break\n        if refinement_cost <= 0:\n            record_invalid_nonpositive_refinement_cost(R, L, target, refinement_cost)\n            preserve_material_unresolved_after_invalid_refinement_cost(R, L, target)\n            break\n        next_depth_budget <- depth_budget - refinement_cost\n'''
replace_once(ps_old, ps_new, "F06 operator positive-cost check")

# 4. Require the repaired semantics in deterministic output.
required_anchor = '''        "preserve_unknown_refinement_cost_and_budget_feasibility",\n    )\n'''
required_new = '''        "preserve_unknown_refinement_cost_and_budget_feasibility",\n        "DECLARED_COST != VALID_POSITIVE_COST",\n        "record_invalid_nonpositive_refinement_cost",\n        "preserve_material_unresolved_after_invalid_refinement_cost",\n    )\n'''
replace_once(required_anchor, required_new, "F06 required tokens")

# 5. Account for the repair in generated document control.
doc_anchor = '''recursive declared-cost / budget-consumption binding\noperator/checker discrimination\n'''
doc_new = '''recursive declared-cost / budget-consumption binding\nrecursive positive-cost domain enforcement\noperator/checker discrimination\n'''
replace_once(doc_anchor, doc_new, "F06 document-control accounting")

P.write_text(text, encoding="utf-8")
print("F06 compiler migration applied exactly.")
