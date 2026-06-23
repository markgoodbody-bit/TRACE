# TRACE Case Graph Validation Status — 2026-06-23

Status: validation status record for JSON schema conformance only. Not validation of TRACE claims.

Purpose: preserve the first validator result after `tests/validate_case_graphs.py` was added, so schema drift is visible and not silently papered over.

```trace
record_type := schema_conformance_status
claim_truth := not_assessed
decision_value := not_assessed
validation_of_TRACE := false
```

---

## Validator source

```trace
validator := tests/validate_case_graphs.py
schema := schemas/CaseGraph.schema.json
graph_dir := cases/graphs
```

Repository source check shows:

```trace
exit_code_contract :=
  0 if all discovered case graphs validate
  1 if one_or_more_validation_failures OR no_graph_files_found
  2 if setup_dependency_schema_loading_failure
```

Guard:

```trace
schema_valid ≠ true
schema_valid ≠ justified
schema_valid ≠ complete
schema_valid ≠ decision_useful
```

---

## Reported run result

Read-only validator run reported by Claude:

```trace
validator_result := FAIL
pass_count := 2
fail_count := 2
```

Pass:

```trace
PASS :=
  cases/graphs/TRACE_amazon_case_graph_v0_1_2026_06_23.json
  + cases/graphs/TRACE_feral_hogs_case_graph_v0_1_1_2026_06_23.json
```

Fail:

```trace
FAIL :=
  cases/graphs/TRACE_feral_hogs_case_graph_v0_1_2026_06_23.json
  + cases/graphs/TRACE_rambo_first_blood_case_graph_v0_1_2026_06_23.json
```

---

## Failure triage

### Feral hogs v0.1

```trace
path := cases/graphs/TRACE_feral_hogs_case_graph_v0_1_2026_06_23.json
failure_type := broken_and_superseded
reported_errors :=
  band_enum
  + authority_status_enum
  + extra_metadata_properties
superseded_by := cases/graphs/TRACE_feral_hogs_case_graph_v0_1_1_2026_06_23.json
recommended_status := ARCHIVE_OR_DELETE_CANDIDATE_AFTER_REFERENCE_CHECK
requires_Mark_decision := true
```

### Rambo First Blood

```trace
path := cases/graphs/TRACE_rambo_first_blood_case_graph_v0_1_2026_06_23.json
failure_type := schema_vs_instance_vocabulary_drift
reported_errors := guard_values_not_in_Claim_schema_enum
examples :=
  authority_claim_not_legitimacy
  harm_carrier_not_culprit
recommended_status := LIVE_WORKING_NEEDS_SCHEMA_AUTHORITY_DECISION
requires_Mark_decision := true
```

Decision fork:

```trace
rambo_resolution :=
  expand_Claim_schema_guards
  OR rename_Rambo_graph_guards_to_existing_canonical_guards
```

Do not auto-resolve because this decides whether those guard labels are canonical.

---

## Immediate interpretation

```trace
control_status := working
```

Reason: the validator caught real drift. That is desirable.

```trace
not_failure_of_project := true
failure_of_current_graph_conformance := true
```

---

## Required next actions

```trace
next_actions :=
  1. verify references to feral_hogs_v0_1
  2. decide archive_or_delete for feral_hogs_v0_1
  3. decide Rambo guard enum authority
  4. rerun validator after patch
  5. record result in this file or successor
```

Do not claim schema coverage until validator result is PASS or known failures are explicitly exempted.
