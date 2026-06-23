# Challenge TRACE

Status: external challenge surface. Not validation. Not canon. Failure submissions are welcome.

Purpose: make TRACE/ME easier to attack, falsify, demote, or improve without requiring private context from Mark, Framework, Claude, or prior chats.

```trace
challenge_surface :=
  accept_failures
  + accept_COMPRESSION_ONLY
  + accept_REGRESSION
  + accept_INCONCLUSIVE
  + accept_partial_signals
  - no_success_only_curation
  - no_validation_theatre
```

---

## 1. What to challenge

Challenge any of the following:

```trace
challenge_targets :=
  claim
  + schema
  + case_graph
  + prompt
  + run_record
  + evidence_status
  + decision_delta
  + notation
  + public_surface
  + alignment_relevance
  + repo_authority_structure
```

Examples:

```trace
examples :=
  TRACE adds no value over baseline
  + TRACE only relabels ordinary incident review
  + a case graph passes schema but hides a false claim
  + a prompt leaks the answer
  + a supposed cold run is contaminated
  + an operator is decorative
  + a public-facing file is unreadable
  + a negative control triggers over-patterning
  + a claim should be demoted
```

---

## 2. Result labels

Use one of these labels where possible:

```trace
PASS := clear decision-relevant delta survives baseline comparison and evidence-status check
PARTIAL_PASS := useful structure appears but evidence, transfer, or comparison remains weak
COMPRESSION_ONLY := same substantive analysis as baseline, with new labels/format only
REGRESSION := TRACE makes the analysis worse, more obscure, or more misleading
INCONCLUSIVE := insufficient data, unclear setup, or contaminated comparison
DEMOte := claim should be lowered in status
DELETE_OR_ARCHIVE_CANDIDATE := file is broken, duplicated, superseded, or misleading
```

Guard:

```trace
failure_submission := useful_evidence
```

---

## 3. Minimum challenge submission format

```trace
challenge_id :=
challenger := human | AI | mixed | unknown
prior_TRACE_exposure := none | some | extensive | unknown
file_or_claim_challenged :=
challenge_type := claim | schema | case_graph | prompt | run | evidence | notation | public_surface | repo_structure | other
short_claim :=
why_it_might_fail :=
evidence_or_example :=
result_label := PASS | PARTIAL_PASS | COMPRESSION_ONLY | REGRESSION | INCONCLUSIVE | DEMOTE | DELETE_OR_ARCHIVE_CANDIDATE
recommended_action :=
```

Plain English version:

1. What are you challenging?
2. Why might it be wrong or misleading?
3. What evidence, example, or comparison supports your challenge?
4. What should change?
5. What should TRACE stop claiming?

---

## 4. Baseline comparison challenge

If your challenge concerns transfer value, include a baseline comparison.

```trace
baseline_required_if :=
  claiming_TRACE_adds_value
  OR claiming_TRACE_adds_no_value
  OR claiming_TRACE_regresses
```

Minimum comparison:

```trace
baseline_output_summary :=
TRACE_output_summary :=
decision_delta_claimed :=
what_baseline_missed :=
what_TRACE_missed :=
would_action_or_review_change := yes | no | unclear
```

Guard:

```trace
format_difference ≠ decision_delta
```

---

## 5. Evidence-status challenge

If challenging a case graph, run record, or public claim, mark evidence status:

```trace
EvidenceStatus :=
  illustrative
  | public_record_light
  | public_record_pinned
  | witness_pinned
  | live_use
  | unknown
```

If a file appears to upgrade evidence silently, say so.

```trace
silent_evidence_upgrade := challenge_valid
```

---

## 6. Negative-control challenge

A good challenge may show that TRACE over-patterns mundane cases.

Use this result if TRACE finds serious laundering, hardening, dirty delay, or authority collapse where a competent baseline sees only routine reversible coordination.

```trace
negative_control_failure :=
  TRACE_generates_major_deltas
  when stated_case_has:
    low_stakes
    + soft_clock
    + ordinary_contest
    + minimal_authority_asymmetry
```

Result label:

```trace
result_label := REGRESSION | COMPRESSION_ONLY
```

---

## 7. Forbidden uses of this challenge surface

Do not use submitted challenges as validation theatre.

```trace
forbidden :=
  challenge_count_as_validation
  + AI_challenge_as_external_proof
  + cherry_pick_successes_only
  + hide_failures
  + treat_schema_validity_as_truth
```

Allowed:

```trace
allowed :=
  use_challenges_to_demote_claims
  + patch_files
  + improve tests
  + record failures
  + discard weak operators
```

---

## 8. Current claims most in need of challenge

```trace
priority_challenges :=
  X057_MetaAI_Grenfell_cold_format_transfer
  + decision_advantage_over_baseline
  + DirtyDelayReceipt_added_value
  + negative_control_meeting_time_idle_test
  + CaseGraph_schema_usefulness
  + public_transfer_packet_readability
  + repo_flat_tree_authority_drift
```

Known current status:

```trace
TRACE_validated := false
cold_format_transfer := shown_once_self_reported_partial
decision_advantage := unproven
overall_drift := AMBER
```

---

## 9. How to preserve a challenge in the repo

Challenge records should live under:

```trace
tests/challenges/
```

Suggested filename:

```trace
tests/challenges/YYYY_MM_DD_TRACE_challenge_<short_slug>_v0_1.md
```

If the challenge demotes a claim, also update or create a claims-ledger delta.

---

## 10. One-line principle

```trace
if TRACE cannot survive hostile comparison to baseline, evidence, and negative controls, it should shrink its claims before it grows its surface.
```
