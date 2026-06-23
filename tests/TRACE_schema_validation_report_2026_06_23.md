# TRACE Schema Validation Report — 2026-06-23

Status: validation pass over current schema/graph build. Not validation of TRACE. Not factual adjudication. Not policy advice.

Scope:

```trace
schemas_checked :=
  schemas/Claim.schema.json
  + schemas/CaseGraph.schema.json

case_graphs_checked :=
  cases/graphs/TRACE_feral_hogs_case_graph_v0_1_2026_06_23.json
  + cases/graphs/TRACE_amazon_case_graph_v0_1_2026_06_23.json
```

This is a structural validation report, not a live domain-evidence assessment.

---

## Result summary

```trace
Claim.schema.json := parse_pass / structure_pass
CaseGraph.schema.json := parse_pass / structure_pass
Amazon_graph_v0_1 := intended_schema_pass_with_open_design_warnings
Feral_hogs_graph_v0_1 := schema_conflict_found
```

The first useful result is not success. It is that the schema caught mismatch in the first graph.

---

## Blocking defects found

### 1. Feral hogs graph metadata conflict

`CaseGraph.schema.json` declares `metadata.additionalProperties := false` and permits:

```trace
metadata_allowed := title + status + created + purpose + guards + schema_version
```

But `TRACE_feral_hogs_case_graph_v0_1_2026_06_23.json` included:

```trace
primary_schema_available
case_graph_schema_status
```

These are useful notes, but they violate the schema. They should be removed or moved into `status` / `purpose` / `notes` after schema support exists.

Patch path:

```trace
create feral_hogs_case_graph_v0_1_1
remove extra metadata keys
add schema_version
```

### 2. Feral hogs evaluator authority enum conflict

`CaseGraph.schema.json` allows evaluator authority statuses:

```trace
ABSENT | CLAIMED | CAPTURED | PROVISIONAL | LEGITIMATE | UNKNOWN
```

But the hogs graph used:

```trace
ABSENT_IN_THIS_GRAPH
```

This is semantically useful but structurally wrong. The schema already has `ABSENT`; use that, and preserve the nuance in the evaluator role or notes.

Patch path:

```trace
ABSENT_IN_THIS_GRAPH → ABSENT
```

---

## Non-blocking design warnings

### A. `$ref` portability

`CaseGraph.schema.json` references:

```trace
Claim.schema.json
```

This is acceptable as a relative schema reference if the validator resolves from the `/schemas` directory. Some tools may require explicit resolver configuration.

Potential later patch:

```trace
use $defs or absolute $id resolver guidance
```

No immediate patch required.

### B. DirtyActionReceipt is under-specified

Current schema says:

```trace
dirty_action_receipt_candidate := object
```

This allows graph transfer to start, but it is too loose for serious validation.

Later schema required:

```trace
schemas/DirtyActionReceipt.schema.json
```

### C. CorrectionPath and Evaluator are under-tight

`correction_paths` and `evaluator_stack` allow additional properties. This was deliberate to avoid overfitting too early, but it should not remain loose indefinitely.

Later schemas required:

```trace
schemas/CorrectionPath.schema.json
schemas/Evaluator.schema.json
```

### D. Amazon graph passes current shape but is evidence-light

The Amazon graph is a transfer structure, not a factual case. It is correctly marked:

```trace
not_validation
not_factual_adjudication
```

Its main live wound is evidence capture and site-specific fact absence, not schema failure.

---

## Immediate patches accepted

```trace
patches :=
  create feral_hogs_case_graph_v0_1_1
  + remove invalid metadata keys
  + replace ABSENT_IN_THIS_GRAPH with ABSENT
```

No schema widening is needed for these two defects.

---

## What this proves and does not prove

```trace
proves :=
  schemas_are_now_capable_of_catching_real_mismatch
```

```trace
does_not_prove :=
  TRACE_is_true
  ∨ graphs_are_factually_complete
  ∨ Amazon_graph_transfers_successfully
  ∨ dirty_action_receipt_is_sufficient
```

---

## Next build sequence

```trace
next :=
  1. create patched feral_hogs graph v0_1_1
  2. build EntityRoleVector.schema.json
  3. build LaunderingCandidate.schema.json or DirtyActionReceipt.schema.json
  4. build Grenfell graph as public-institution transfer test
  5. only then hostile review again
```

Do not return to review-loop before the schema/graph path has one more build cycle.
