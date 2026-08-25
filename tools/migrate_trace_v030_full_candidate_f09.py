#!/usr/bin/env python3
"""One-shot exact migration for full-candidate coherence finding F09.

Edits only the deterministic v0.3 compiler and fails closed unless the expected
post-F08 compiler anchors are present exactly. This script is migration
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


# 1. Propagate recursive limit-carrying distinctions.
supp_anchor = '''    "RECURSION_SKIPPED != COMPLETE_COVERAGE",\n)\n\nSURVIVAL_REQUIRED = (\n'''
supp_new = '''    "RECURSION_SKIPPED != COMPLETE_COVERAGE",\n    "RECURSIVE_GRAPH_MERGE != RECURSIVE_LIMIT_MERGE",\n    "CHILD_GRAPH_VISIBLE != CHILD_LIMIT_VISIBLE",\n    "DEEPER_UNCERTAINTY != DISPENSABLE",\n    "GRAPH_CONTRIBUTION_SURVIVED != QUALIFYING_LIMIT_SURVIVED",\n    "CHILD_GRAPH_MERGED + CHILD_LIMIT_DROPPED != RECURSIVE_INTEGRATION",\n)\n\nSURVIVAL_REQUIRED = (\n'''
replace_once(supp_anchor, supp_new, "F09 supplemental propagation")

survival_anchor = '''    "NEGATIVE_TRACING_BUDGET != VALID_REMAINING_BUDGET",\n    "RECURSION_SKIPPED != COMPLETE_COVERAGE",\n)\n\n\ndef sha256_bytes'''
survival_new = '''    "NEGATIVE_TRACING_BUDGET != VALID_REMAINING_BUDGET",\n    "RECURSION_SKIPPED != COMPLETE_COVERAGE",\n    "RECURSIVE_GRAPH_MERGE != RECURSIVE_LIMIT_MERGE",\n    "CHILD_GRAPH_VISIBLE != CHILD_LIMIT_VISIBLE",\n    "DEEPER_UNCERTAINTY != DISPENSABLE",\n    "GRAPH_CONTRIBUTION_SURVIVED != QUALIFYING_LIMIT_SURVIVED",\n)\n\n\ndef sha256_bytes'''
replace_once(survival_anchor, survival_new, "F09 survival propagation")

# 2. Repair the formal recursion so child limits are carried as well as graph.
formal_old = r'''\[
\mathcal R_{k+1}
=
\operatorname{merge}(
\mathcal R_k,
\mathcal R_{q_k}
)
\]
'''
formal_new = r'''\[
\mathcal R_{k+1}
=
\operatorname{merge}(
\mathcal R_k,
\mathcal R_{q_k}
)
\]

\[
\mathcal L_{k+1}
=
\operatorname{mergeLimits}(
\mathcal L_k,
\mathcal L_{q_k}
)
\]

Recursive integration carries qualifying limits with the graph contribution.
Where materially distinct child limits would collapse under deduplication,
preserve target/scope/provenance association.

```text
RECURSIVE_GRAPH_MERGE != RECURSIVE_LIMIT_MERGE
CHILD_GRAPH_VISIBLE != CHILD_LIMIT_VISIBLE
DEEPER_UNCERTAINTY != DISPENSABLE
GRAPH_CONTRIBUTION_SURVIVED != QUALIFYING_LIMIT_SURVIVED
CHILD_GRAPH_MERGED + CHILD_LIMIT_DROPPED != RECURSIVE_INTEGRATION
```
'''
# This anchor is donor text and must still occur exactly once after prior transforms.
compiler_insert = '''    record_guard = """\n'''
transform_code = '''    b.replace_once(\n        "T_RECURSION_LIMIT_PROPAGATION",\n        r"""''' + formal_old + '''""",\n        r"""''' + formal_new + '''""",\n    )\n\n'''
replace_once(compiler_insert, transform_code + compiler_insert, "F09 formal recursion migration")

# 3. Bind recursive graph and limit returns explicitly in executable pseudocode.
ps_old = '''        R <- merge_graphs(R, TRACE(target, aperture, history,\n                                   next_depth_budget, primitive_aperture))\n'''
ps_new = '''        child_R, child_L <- TRACE(target, aperture, history,\n                                  next_depth_budget, primitive_aperture)\n        R <- merge_graphs(R, child_R)\n        L <- merge_limits_with_recursive_provenance(L, child_L, target)\n'''
replace_once(ps_old, ps_new, "F09 operator child-limit merge")

# 4. Require repaired semantics in deterministic output.
required_anchor = '''        "preserve_recursive_coverage_limit_due_to_budget",\n    )\n'''
required_new = '''        "preserve_recursive_coverage_limit_due_to_budget",\n        "RECURSIVE_GRAPH_MERGE != RECURSIVE_LIMIT_MERGE",\n        "CHILD_GRAPH_VISIBLE != CHILD_LIMIT_VISIBLE",\n        "merge_limits_with_recursive_provenance",\n    )\n'''
replace_once(required_anchor, required_new, "F09 required tokens")

# 5. Reject the old direct recursive tuple-to-graph merge shortcut.
bad_anchor = '''        "depth_budget - 1",\n    )\n'''
bad_new = '''        "depth_budget - 1",\n        "R <- merge_graphs(R, TRACE(target, aperture, history,",\n    )\n'''
replace_once(bad_anchor, bad_new, "F09 stale-control rejection")

# 6. Account for the repair in generated document control.
doc_anchor = '''recursive entry-budget termination / domain binding\noperator/checker discrimination\n'''
doc_new = '''recursive entry-budget termination / domain binding\nrecursive child-limit propagation\noperator/checker discrimination\n'''
replace_once(doc_anchor, doc_new, "F09 document-control accounting")

P.write_text(text, encoding="utf-8")
print("F09 compiler migration applied exactly.")
