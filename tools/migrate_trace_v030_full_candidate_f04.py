#!/usr/bin/env python3
"""One-shot exact migration for full-candidate coherence finding F04.

Edits only the deterministic v0.3 compiler and fails closed unless the expected
post-F03 compiler anchors are present exactly. This script is migration
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


# 1. Propagate the narrow F04 distinctions into supplemental/survival guards.
supp_anchor = '''    "OMITTED_BY_BUDGET != IRRELEVANT",\n)\n\nSURVIVAL_REQUIRED = (\n'''
supp_new = '''    "OMITTED_BY_BUDGET != IRRELEVANT",\n    "STOPPED != COMPLETED",\n    "TERMINATION != COMPLETE_COVERAGE",\n    "BUDGET_EXHAUSTED != NO_MATERIAL_UNRESOLVED_TARGET",\n    "AUTHORITY_REACHED != ANALYSIS_COMPLETE",\n)\n\nSURVIVAL_REQUIRED = (\n'''
replace_once(supp_anchor, supp_new, "F04 supplemental propagation")

survival_anchor = '''    "HIGHEST_RELEVANCE != MEASURE_FREE",\n    "OMITTED_BY_BUDGET != IRRELEVANT",\n)\n\n\ndef sha256_bytes'''
survival_new = '''    "HIGHEST_RELEVANCE != MEASURE_FREE",\n    "OMITTED_BY_BUDGET != IRRELEVANT",\n    "STOPPED != COMPLETED",\n    "TERMINATION != COMPLETE_COVERAGE",\n    "BUDGET_EXHAUSTED != NO_MATERIAL_UNRESOLVED_TARGET",\n    "AUTHORITY_REACHED != ANALYSIS_COMPLETE",\n)\n\n\ndef sha256_bytes'''
replace_once(survival_anchor, survival_new, "F04 survival propagation")

# 2. Add the bounded termination rule to retained [11] without a new primitive.
insert_anchor = '''    record_guard = """\n'''
transform = r'''    recursion_stop_guard = r"""Recursion termination use rule:

Stopping recursive differentiation is itself load-bearing when the termination
basis can change a downstream claim, coverage statement, correction-window
status, proposed transition or confidence/limits statement. A stop event must
therefore preserve, where available:

```text
refinement_stop_basis_claim_refs
refinement_stop_kind
refinement_stop_measure_ref
refinement_stop_limit_refs
refinement_stop_clock_refs
refinement_stop_route_or_handoff_refs
material_unresolved_at_stop_refs
```

Distinguish bounded sufficiency from truncation, exhaustion and handoff. If the
stopping basis is unsupported or the stop occurs because budget, access,
authority or time prevents further material refinement, preserve the remaining
material uncertainty/omissions rather than presenting termination as analytic
completion.

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

This uses existing CLAIM / LIMIT / APERTURE / CLOCK / ROUTE / designation /
measure machinery. No stop, termination or sufficiency primitive is added.

"""
    b.insert_before_once(
        "T_RECURSION_STOP_PROVENANCE",
        "## [11.3] Recursion stop\n",
        recursion_stop_guard,
    )

'''
replace_once(insert_anchor, transform + insert_anchor, "F04 stop-rule insertion")

# 3. Replace bare boolean termination in the generated operator.
ps_old = '''        if stop_condition(target, R, L): break\n'''
ps_new = '''        stop, stop_basis <- evaluate_refinement_stop_condition(\n            target, R, L, declared_designation(R), declared_measure(R))\n        if stop:\n            record_refinement_stop_basis_and_limits(R, L, target, stop_basis)\n            if not supported_bounded_sufficiency(stop_basis):\n                preserve_material_unresolved_after_truncation_or_handoff(\n                    R, L, candidates, target, stop_basis)\n            break\n'''
replace_once(ps_old, ps_new, "F04 operator termination")

# 4. Require the repaired semantics in deterministic output.
required_anchor = '''        "record_refinement_selection_basis_and_budget_omissions",\n    )\n'''
required_new = '''        "record_refinement_selection_basis_and_budget_omissions",\n        "STOPPED != COMPLETED",\n        "TERMINATION != COMPLETE_COVERAGE",\n        "record_refinement_stop_basis_and_limits",\n        "preserve_material_unresolved_after_truncation_or_handoff",\n    )\n'''
replace_once(required_anchor, required_new, "F04 required tokens")

# 5. Reject reintroduction of the bare stop shortcut.
bad_anchor = '''        "target <- highest_relevance_unresolved_node_or_edge(R)",\n    )\n'''
bad_new = '''        "target <- highest_relevance_unresolved_node_or_edge(R)",\n        "if stop_condition(target, R, L): break",\n    )\n'''
replace_once(bad_anchor, bad_new, "F04 stale-control rejection")

# 6. Account for the repair in generated document control.
doc_anchor = '''recursive analytic target-selection binding\noperator/checker discrimination\n'''
doc_new = '''recursive analytic target-selection binding\nrecursive termination provenance / truncation binding\noperator/checker discrimination\n'''
replace_once(doc_anchor, doc_new, "F04 document-control accounting")

P.write_text(text, encoding="utf-8")
print("F04 compiler migration applied exactly.")
