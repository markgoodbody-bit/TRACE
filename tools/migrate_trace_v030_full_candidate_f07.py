#!/usr/bin/env python3
"""One-shot exact migration for full-candidate coherence finding F07.

Edits only the deterministic v0.3 compiler and fails closed unless the expected
post-F06 compiler anchors are present exactly. This script is migration
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


# 1. Propagate the narrow F07 empty-target distinctions.
supp_anchor = '''    "COST_RECORDED != COST_DOMAIN_VALID",\n)\n\nSURVIVAL_REQUIRED = (\n'''
supp_new = '''    "COST_RECORDED != COST_DOMAIN_VALID",\n    "EMPTY_REFINEMENT_TARGET_SET != SELECTABLE_TARGET",\n    "NO_UNRESOLVED_TARGET_IN_DECLARED_SET != COMPLETE_WORLD_COVERAGE",\n    "LOCAL_REFINEMENT_EXHAUSTED != REPRESENTATION_COMPLETE",\n    "NO_TARGET_SELECTED != SELECTOR_FAILURE",\n    "EMPTY_TARGET_SET != BOUNDED_SUFFICIENCY_WITHOUT_BASIS",\n)\n\nSURVIVAL_REQUIRED = (\n'''
replace_once(supp_anchor, supp_new, "F07 supplemental propagation")

survival_anchor = '''    "NEGATIVE_REFINEMENT_COST != BUDGET_CREDIT",\n    "COST_RECORDED != COST_DOMAIN_VALID",\n)\n\n\ndef sha256_bytes'''
survival_new = '''    "NEGATIVE_REFINEMENT_COST != BUDGET_CREDIT",\n    "COST_RECORDED != COST_DOMAIN_VALID",\n    "EMPTY_REFINEMENT_TARGET_SET != SELECTABLE_TARGET",\n    "NO_UNRESOLVED_TARGET_IN_DECLARED_SET != COMPLETE_WORLD_COVERAGE",\n    "LOCAL_REFINEMENT_EXHAUSTED != REPRESENTATION_COMPLETE",\n)\n\n\ndef sha256_bytes'''
replace_once(survival_anchor, survival_new, "F07 survival propagation")

# 2. State the empty-target executable rule after target-selection discipline.
insert_anchor = '''    recursion_budget_guard = r"""Refinement-budget use rule:\n'''
transform = r'''    recursion_empty_target_guard = r"""Empty refinement-target use rule:

After constructing and recording the unresolved refinement target set, handle an
empty set before calling the target selector. Empty discovery means only that no
unresolved target is present inside the represented target-set aperture under
the current construction. It does not establish complete world coverage,
representation completeness, or bounded sufficiency without the required basis.

```text
EMPTY_REFINEMENT_TARGET_SET != SELECTABLE_TARGET
NO_UNRESOLVED_TARGET_IN_DECLARED_SET != COMPLETE_WORLD_COVERAGE
LOCAL_REFINEMENT_EXHAUSTED != REPRESENTATION_COMPLETE
NO_TARGET_SELECTED != SELECTOR_FAILURE
EMPTY_TARGET_SET != BOUNDED_SUFFICIENCY_WITHOUT_BASIS
```

Record local target-set exhaustion as a termination state relative to the
represented refinement target-set aperture and preserve material aperture /
representation limits. No target, completion or coverage primitive is added.

"""
    b.insert_before_once(
        "T_RECURSION_EMPTY_TARGET_SET",
        "Let \\(d_k^{rem}\\ge0\\) be remaining tracing budget",
        recursion_empty_target_guard,
    )

'''
replace_once(insert_anchor, transform + insert_anchor, "F07 empty-target rule insertion")

# 3. Handle empty candidates before selector invocation.
ps_old = '''        candidates <- unresolved_refinement_targets(R)\n        record_refinement_target_set_aperture(R, candidates)\n        target, refinement_basis <- select_refinement_target(\n            candidates, declared_designation(R), declared_measure(R), depth_budget)\n'''
ps_new = '''        candidates <- unresolved_refinement_targets(R)\n        record_refinement_target_set_aperture(R, candidates)\n        if candidates is empty:\n            record_empty_refinement_target_set_termination(R, L, candidates)\n            preserve_coverage_relative_to_refinement_target_set_aperture(R, L, candidates)\n            break\n        target, refinement_basis <- select_refinement_target(\n            candidates, declared_designation(R), declared_measure(R), depth_budget)\n'''
replace_once(ps_old, ps_new, "F07 operator empty-target handling")

# 4. Require repaired semantics in deterministic output.
required_anchor = '''        "preserve_material_unresolved_after_invalid_refinement_cost",\n    )\n'''
required_new = '''        "preserve_material_unresolved_after_invalid_refinement_cost",\n        "EMPTY_REFINEMENT_TARGET_SET != SELECTABLE_TARGET",\n        "NO_UNRESOLVED_TARGET_IN_DECLARED_SET != COMPLETE_WORLD_COVERAGE",\n        "record_empty_refinement_target_set_termination",\n        "preserve_coverage_relative_to_refinement_target_set_aperture",\n    )\n'''
replace_once(required_anchor, required_new, "F07 required tokens")

# 5. Account for the repair in generated document control.
doc_anchor = '''recursive positive-cost domain enforcement\noperator/checker discrimination\n'''
doc_new = '''recursive positive-cost domain enforcement\nrecursive empty-target termination / coverage binding\noperator/checker discrimination\n'''
replace_once(doc_anchor, doc_new, "F07 document-control accounting")

P.write_text(text, encoding="utf-8")
print("F07 compiler migration applied exactly.")
