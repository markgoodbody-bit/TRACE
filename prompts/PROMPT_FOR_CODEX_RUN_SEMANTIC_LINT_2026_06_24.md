# Prompt for Codex — Run TRACE semantic lint and preserve result

```trace
speaker := Framework
to := Codex
task := run_semantic_lint
mode := execution
not := theory_refinement OR schema_build OR validation_claim
```

## Purpose

Run the existing TRACE semantic lint script and preserve the output exactly. Do not patch first. Do not interpret a pass as validation. Do not hide a failure.

Current execution boundary:

```trace
self_test_binary_cheap
+ externalise_expensive_judgment
```

This task is the cheap internal gate. Serious-case decision advantage remains external-reader territory.

## Commands

From the TRACE repo root, run:

```bash
mkdir -p tests/semantic_lint/runs
python tests/semantic_lint/trace_semantic_lint.py --json > tests/semantic_lint/runs/semantic_lint_run_2026_06_24.json
echo $? > tests/semantic_lint/runs/semantic_lint_run_2026_06_24.exitcode
python tests/semantic_lint/trace_semantic_lint.py > tests/semantic_lint/runs/semantic_lint_run_2026_06_24.txt || true
```

Then commit the three output files, even if the exit code is nonzero:

```bash
git add tests/semantic_lint/runs/semantic_lint_run_2026_06_24.json \
        tests/semantic_lint/runs/semantic_lint_run_2026_06_24.exitcode \
        tests/semantic_lint/runs/semantic_lint_run_2026_06_24.txt

git commit -m "Record semantic lint run 2026-06-24"
```

## Interpretation rules

```trace
exit_0 := no_ERROR_findings
exit_1 := one_or_more_ERROR_findings
exit_2 := setup_or_load_failure
```

If exit code is `0`, report:

```trace
semantic_lint := pass_no_ERROR
not := true OR validated OR complete OR decision_useful
```

If exit code is `1`, report:

```trace
semantic_lint := fail_useful
next := patch_one_failure_only_after_reading
```

If exit code is `2`, report:

```trace
semantic_lint := setup_failure
next := fix_run_environment_or_load_path
not := TRACE_failure_claim
```

## Stop rules

Do not:

```trace
forbidden :=
  patch_before_recording
  + delete_or_hide_failure
  + summarize_failure_as_success
  + create_new_schema
  + create_new_operator
  + update_Robodebt_packet
  + claim_validation
```

## Required response back to Mark / Framework

Return:

1. Commit SHA.
2. Exit code.
3. Error count and warning count from JSON if available.
4. Top 5 findings by severity if any.
5. Whether any finding touches current Robodebt reader packet, negative control, DecisionDelta, or overclaim language.
6. No patch recommendation beyond “patch one failure next” unless explicitly asked.

## Reminder

```trace
semantic_lint_clean ≠ true
semantic_lint_clean ≠ justified
semantic_lint_clean ≠ complete
semantic_lint_clean ≠ decision-useful
```
