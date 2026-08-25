#!/usr/bin/env python3
"""One-shot exact migration for full-candidate coherence finding F08.

Edits only the deterministic v0.3 compiler and fails closed unless the expected
post-F07 compiler anchors are present exactly. This script is migration
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


# 1. Propagate the narrow loop-entry budget distinctions.
supp_anchor = '''    "EMPTY_TARGET_SET != BOUNDED_SUFFICIENCY_WITHOUT_BASIS",\n)\n\nSURVIVAL_REQUIRED = (\n'''
supp_new = '''    "EMPTY_TARGET_SET != BOUNDED_SUFFICIENCY_WITHOUT_BASIS",\n    "LOOP_NOT_ENTERED != RECURSION_COMPLETED",\n    "INITIAL_BUDGET_ZERO != NO_REFINEMENT_NEEDED",\n    "BUDGET_EXHAUSTED_AT_ENTRY != BOUNDED_SUFFICIENCY",\n    "NEGATIVE_TRACING_BUDGET != VALID_REMAINING_BUDGET",\n    "RECURSION_SKIPPED != COMPLETE_COVERAGE",\n)\n\nSURVIVAL_REQUIRED = (\n'''
replace_once(supp_anchor, supp_new, "F08 supplemental propagation")

survival_anchor = '''    "EMPTY_REFINEMENT_TARGET_SET != SELECTABLE_TARGET",\n    "NO_UNRESOLVED_TARGET_IN_DECLARED_SET != COMPLETE_WORLD_COVERAGE",\n    "LOCAL_REFINEMENT_EXHAUSTED != REPRESENTATION_COMPLETE",\n)\n\n\ndef sha256_bytes'''
survival_new = '''    "EMPTY_REFINEMENT_TARGET_SET != SELECTABLE_TARGET",\n    "NO_UNRESOLVED_TARGET_IN_DECLARED_SET != COMPLETE_WORLD_COVERAGE",\n    "LOCAL_REFINEMENT_EXHAUSTED != REPRESENTATION_COMPLETE",\n    "LOOP_NOT_ENTERED != RECURSION_COMPLETED",\n    "INITIAL_BUDGET_ZERO != NO_REFINEMENT_NEEDED",\n    "NEGATIVE_TRACING_BUDGET != VALID_REMAINING_BUDGET",\n    "RECURSION_SKIPPED != COMPLETE_COVERAGE",\n)\n\n\ndef sha256_bytes'''
replace_once(survival_anchor, survival_new, "F08 survival propagation")

# 2. Bind loop-entry budget state to the existing termination/limit discipline.
insert_anchor = '''    recursion_budget_guard = r"""Refinement-budget use rule:\n'''
transform = r'''    recursion_entry_budget_guard = r"""Recursion-entry budget use rule:

The declared recursion budget is non-negative. Before target discovery, expose
whether recursive refinement is prevented at entry by exhausted budget or by an
invalid negative budget. Skipping the loop is not evidence that no refinement
was needed.

```text
LOOP_NOT_ENTERED != RECURSION_COMPLETED
INITIAL_BUDGET_ZERO != NO_REFINEMENT_NEEDED
BUDGET_EXHAUSTED_AT_ENTRY != BOUNDED_SUFFICIENCY
NEGATIVE_TRACING_BUDGET != VALID_REMAINING_BUDGET
RECURSION_SKIPPED != COMPLETE_COVERAGE
```

A zero remaining budget records budget-exhausted termination and the resulting
recursive coverage limit. A negative remaining budget is outside the declared
domain and is preserved as an invalid limit state rather than treated as usable
budget. No new budget or termination primitive is added.

"""
    b.insert_before_once(
        "T_RECURSION_ENTRY_BUDGET",
        "Let \\(d_k^{rem}\\ge0\\) be remaining tracing budget",
        recursion_entry_budget_guard,
    )

'''
replace_once(insert_anchor, transform + insert_anchor, "F08 entry-budget rule insertion")

# 3. Expose zero/negative entry state before the loop can silently be skipped.
ps_old = '''    record_reader_limits(L)\n\n    while depth_budget remains:\n'''
ps_new = '''    record_reader_limits(L)\n\n    if depth_budget < 0:\n        record_invalid_negative_tracing_budget(R, L, depth_budget)\n        preserve_recursive_coverage_limit_due_to_invalid_budget(R, L)\n        depth_budget <- 0\n    elif depth_budget == 0:\n        record_budget_exhausted_at_recursion_entry(R, L, depth_budget)\n        preserve_recursive_coverage_limit_due_to_budget(R, L)\n\n    while depth_budget remains:\n'''
replace_once(ps_old, ps_new, "F08 operator entry-budget handling")

# 4. Require repaired semantics in deterministic output.
required_anchor = '''        "preserve_coverage_relative_to_refinement_target_set_aperture",\n    )\n'''
required_new = '''        "preserve_coverage_relative_to_refinement_target_set_aperture",\n        "LOOP_NOT_ENTERED != RECURSION_COMPLETED",\n        "NEGATIVE_TRACING_BUDGET != VALID_REMAINING_BUDGET",\n        "record_budget_exhausted_at_recursion_entry",\n        "record_invalid_negative_tracing_budget",\n        "preserve_recursive_coverage_limit_due_to_budget",\n    )\n'''
replace_once(required_anchor, required_new, "F08 required tokens")

# 5. Account for the repair in generated document control.
doc_anchor = '''recursive empty-target termination / coverage binding\noperator/checker discrimination\n'''
doc_new = '''recursive empty-target termination / coverage binding\nrecursive entry-budget termination / domain binding\noperator/checker discrimination\n'''
replace_once(doc_anchor, doc_new, "F08 document-control accounting")

P.write_text(text, encoding="utf-8")
print("F08 compiler migration applied exactly.")
