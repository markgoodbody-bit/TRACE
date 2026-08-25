#!/usr/bin/env python3
"""One-shot exact migration for full-candidate coherence finding F03.

Edits only the deterministic v0.3 compiler and fails closed unless the expected
pre-repair compiler anchors are present exactly. This script is migration
evidence, not semantic validation.
"""

from pathlib import Path

P = Path(__file__).with_name("compile_trace_v030_full_candidate.py")
text = P.read_text(encoding="utf-8")

# 1. Supplemental and compression-critical guards.
supp_anchor = '''    "ROLLBACK_COMPLETED_BEFORE_BOUNDARY != RESTORED_STATE",\n)\n\nSURVIVAL_REQUIRED = (\n'''
supp_new = '''    "ROLLBACK_COMPLETED_BEFORE_BOUNDARY != RESTORED_STATE",\n    "ANALYTIC_TARGET_SELECTION != NEUTRAL",\n    "HIGHEST_RELEVANCE != MEASURE_FREE",\n    "TARGETED_REFINEMENT != COMPLETE_COVERAGE",\n    "OMITTED_BY_BUDGET != IRRELEVANT",\n)\n\nSURVIVAL_REQUIRED = (\n'''
if '    "ANALYTIC_TARGET_SELECTION != NEUTRAL",\n' not in text.split('SURVIVAL_REQUIRED = (', 1)[0]:
    if text.count(supp_anchor) != 1:
        raise SystemExit(f"F03 supplemental anchor count != 1: {text.count(supp_anchor)}")
    text = text.replace(supp_anchor, supp_new, 1)

survival_anchor = '''    "ROLLBACK_COMPLETED_BEFORE_BOUNDARY != RESTORED_STATE",\n)\n\n\ndef sha256_bytes'''
survival_new = '''    "ROLLBACK_COMPLETED_BEFORE_BOUNDARY != RESTORED_STATE",\n    "HIGHEST_RELEVANCE != MEASURE_FREE",\n    "OMITTED_BY_BUDGET != IRRELEVANT",\n)\n\n\ndef sha256_bytes'''
if text.count('    "HIGHEST_RELEVANCE != MEASURE_FREE",') < 2:
    if text.count(survival_anchor) != 1:
        raise SystemExit(f"F03 survival anchor count != 1: {text.count(survival_anchor)}")
    text = text.replace(survival_anchor, survival_new, 1)

# 2. Add a bounded formal use rule to retained [11].
insert_anchor = '''    record_guard = """\n'''
transform_marker = '    recursion_target_guard = r"""Refinement target-selection use rule:\n'
if transform_marker not in text:
    if text.count(insert_anchor) != 1:
        raise SystemExit(f"F03 transform insertion anchor count != 1: {text.count(insert_anchor)}")
    transform = r'''    recursion_target_guard = r"""Refinement target-selection use rule:

`target(R_k,L_k)` allocates analytic attention. Under a finite tracing budget,
that choice can change which unresolved structures enter the later map. Where
the choice can materially affect a downstream claim, comparison, coverage
statement, correction-window result or proposed transition, expose where
available:

```text
candidate_refinement_target_refs
refinement_target_set_aperture_ref
selection_basis_claim_refs
designation_ref
measure_ref
selected_refinement_target_ref
unselected_material_alternative_refs
budget_omission_refs
```

Comparative language such as `highest relevance` requires a declared comparison
basis. If no supported ordering is available, preserve the selection basis as
`UNKNOWN`; do not silently convert an implementation heuristic into a neutral
importance claim. Targets left unexplored because budget is exhausted remain
visible as omissions where they could still change a load-bearing result.

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

This uses existing APERTURE / target-set aperture / CLAIM / LIMIT /
designation / measure / selector machinery. It does not add an attention,
refinement, priority or relevance primitive and does not grant world-action
authority.

"""
    b.insert_before_once(
        "T_RECURSION_TARGET_SELECTION",
        "Let \\(d_k^{rem}\\ge0\\) be remaining tracing budget",
        recursion_target_guard,
    )

'''
    text = text.replace(insert_anchor, transform + insert_anchor, 1)

# 3. Replace the hidden highest-relevance pseudocode with exposed analytic selection.
ps_old = '''        target <- highest_relevance_unresolved_node_or_edge(R)\n        if stop_condition(target, R, L): break\n'''
ps_new = '''        candidates <- unresolved_refinement_targets(R)\n        record_refinement_target_set_aperture(R, candidates)\n        target, refinement_basis <- select_refinement_target(\n            candidates, declared_designation(R), declared_measure(R), depth_budget)\n        record_refinement_selection_basis_and_budget_omissions(\n            R, L, candidates, target, refinement_basis, depth_budget)\n        if refinement_basis is UNKNOWN and\n           unselected_candidate_could_materially_change_load_bearing_output(R, candidates, target):\n            preserve_refinement_selection_uncertainty(R, L)\n        if stop_condition(target, R, L): break\n'''
if ps_new not in text:
    if text.count(ps_old) != 1:
        raise SystemExit(f"F03 pseudocode anchor count != 1: {text.count(ps_old)}")
    text = text.replace(ps_old, ps_new, 1)

# 4. Required tokens and stale shortcut rejection.
required_anchor = '''        "ROLLBACK_COMPLETES_BEFORE_BOUNDARY_FOR_REPRESENTED_BINDINGS",\n'''
required_add = required_anchor + '''        "HIGHEST_RELEVANCE != MEASURE_FREE",\n        "OMITTED_BY_BUDGET != IRRELEVANT",\n        "record_refinement_target_set_aperture",\n        "record_refinement_selection_basis_and_budget_omissions",\n'''
if '        "record_refinement_target_set_aperture",\n' not in text:
    if text.count(required_anchor) != 1:
        raise SystemExit(f"F03 required-token anchor count != 1: {text.count(required_anchor)}")
    text = text.replace(required_anchor, required_add, 1)

bad_anchor = '''        "Rollback can preserve the threatened path only if it is executable, reaches the relevant state, and completes before practical irreversibility.",\n    )\n'''
bad_add = '''        "Rollback can preserve the threatened path only if it is executable, reaches the relevant state, and completes before practical irreversibility.",\n        "target <- highest_relevance_unresolved_node_or_edge(R)",\n    )\n'''
if '        "target <- highest_relevance_unresolved_node_or_edge(R)",\n' not in text:
    if text.count(bad_anchor) != 1:
        raise SystemExit(f"F03 stale-control anchor count != 1: {text.count(bad_anchor)}")
    text = text.replace(bad_anchor, bad_add, 1)

# 5. Document-control transform accounting.
doc_old = '''measure-bound advantage claims\noperator/checker discrimination\n'''
doc_new = '''measure-bound advantage claims\nrecursive analytic target-selection binding\noperator/checker discrimination\n'''
if doc_new not in text:
    if text.count(doc_old) != 1:
        raise SystemExit(f"F03 document-control anchor count != 1: {text.count(doc_old)}")
    text = text.replace(doc_old, doc_new, 1)

P.write_text(text, encoding="utf-8")
print("F03 compiler migration applied or already present exactly.")
