# TRACE Threshold Register Stress Test — Isolated v0.1

Status: worked example / isolated variable test.  
Depends on: `TRACE_THRESHOLD_REGISTER_v0_1.md`, `TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1.md`, `TRACE_REACHABILITY_MODEL_v0_1.md`, `TRACE_NECESSITY_AND_ALTERNATIVE_SEARCH_v0_1.md`, `ME_FROM_TRACE_TRANSLATION_RULES_v0_1.md`.  
Not: validation, real-world threshold authority, or new core theory.

## 0. Purpose

The previous threshold-register stress test showed that the same number should not carry the same authority under different threshold statuses.

Fresh-reader review found a defect:

```text
Run B was confounded by correction-reachability failure.
```

This file isolates the variable.

All non-threshold guards are held constant.

Only threshold-authority status changes.

## 1. Scenario

A public agency considers a temporary automated housing-support suspension after detecting possible overpayment.

The action is:

```text
a_suspend = temporary automated suspension with manual review route active
```

Affected entity:

```text
claimant
```

Protected dimension:

```text
housing_stability
```

Estimated upper catastrophic tail risk:

```math
\overline{TR}_{claimant,housing}(a_{suspend}) = 0.04
```

Candidate catastrophic-tail tolerance:

```math
\epsilon^{cat}_{claimant,housing}=0.05
```

Raw number-only comparison:

```math
0.04 < 0.05
```

This comparison is identical in all runs.

## 2. Held-Constant Guard Conditions

To isolate threshold status, all other guards are stipulated as passing in each run.

```yaml
non_threshold_guards:
  affected_entity_set: complete
  uncertainty_display: pass
  risk_record: complete
  correction_reachability: pass
  repair_route: active
  responsibility_route: exists
  non_aggregation_guard: pass
  necessity_exception: not needed
  safer_adequate_alternative: unavailable in the required time window
  imprecise_probability_mode: upper_bound_used
```

Correction reachability is held constant:

```math
\rho_{claimant}(correct,t)=0.75 ≥ \theta_{correct}=0.50
```

Risk record is held constant:

```text
upper bound used
model uncertainty displayed
threshold source record separately inspected
```

Alternative search is held constant:

```text
manual hold alternative unavailable before next payment cycle
human review route exists but cannot replace immediate temporary action
```

Therefore any difference in outcome must come from:

```math
Reg(\epsilon^{cat}_{claimant,housing})
```

## 3. No-Card Comparator

A number-only reviewer may say:

```text
0.04 is below 0.05, and the other guards pass, so proceed.
```

A careful institutional reviewer may ask:

```text
who authorised 0.05?
```

This test does not claim TRACE beats every careful human reviewer.

It tests whether TRACE makes threshold-authority inspection mandatory rather than optional.

## 4. Run A — Illustrative Threshold

Threshold status:

```yaml
symbol: epsilon_cat_claimant_housing
value_or_range: 0.05
status: illustrative
source_reference: worked_example_only
authority: none / illustrative
```

All other guards:

```text
pass
```

Raw comparison:

```math
0.04 < 0.05
```

Threshold-authority check:

```math
Reg(\epsilon^{cat}) = illustrative
```

TRACE rule:

```text
illustrative thresholds cannot support high-stakes pass
```

Output:

```yaml
permission_status: blocked_by_threshold_status
claim_status:
  - ME_OPEN_SEAM
  - ME_PRESUMPTIVE_CONSTRAINT
reason: illustrative threshold cannot authorise real suspension
```

Result:

```text
NO HIGH-STAKES PASS
```

Difference from number-only reasoning:

```text
number-only would pass
TRACE blocks because number lacks authority
```

## 5. Run B — Provisional Threshold with Incomplete Provisional Conditions

Threshold status:

```yaml
symbol: epsilon_cat_claimant_housing
value_or_range: 0.05
status: provisional
source_type: expert_judgement
authority: interim oversight panel
review_cycle: missing
expiry: missing
uncertainty_attached: present
change_log: present
```

All other guards:

```text
pass
```

Raw comparison:

```math
0.04 < 0.05
```

Threshold-authority check:

```math
Reg(\epsilon^{cat}) = invalid
```

Reason:

```text
provisional threshold lacks expiry / review cycle
```

TRACE rule:

```text
provisional thresholds must carry explicit uncertainty and review route
invalid threshold cannot support high-stakes pass
```

Output:

```yaml
permission_status: blocked_by_threshold_status
claim_status:
  - ME_OPEN_SEAM
  - ME_ESCALATION_REQUIRED
reason: provisional threshold incomplete; no high-stakes pass
```

Result:

```text
NO HIGH-STAKES PASS
```

Difference from Run A:

```text
A is blocked because threshold is illustrative.
B is blocked because provisional threshold is incomplete.
```

Difference from number-only reasoning:

```text
number-only would pass
TRACE blocks because provisional authority conditions are incomplete
```

## 6. Run C — Adopted Threshold

Threshold status:

```yaml
symbol: epsilon_cat_claimant_housing
value_or_range: 0.05
status: adopted
source_type: legal_floor + empirical_distribution + independent_audit
authority: authorised regulator / statutory body
review_cycle: annual and after material system change
uncertainty_attached: present
change_log: present
anti_gaming_note: cannot be altered during active case
```

All other guards:

```text
pass
```

Raw comparison:

```math
0.04 < 0.05
```

Threshold-authority check:

```math
Reg(\epsilon^{cat}) = valid
```

TRACE rule:

```text
adopted threshold can support high-stakes pass only within declared scope and with other guards passing
```

Output:

```yaml
permission_status: limited_pass
claim_status:
  - ME_ADVISORY
  - ME_PRESUMPTIVE_CONSTRAINT
reason: adopted threshold valid; all other guards pass; action remains scope-bound and auditable
```

Result:

```text
LIMITED PASS
```

Difference from Runs A and B:

```text
same number
same risk
same non-threshold guards
only threshold-authority status differs
```

## 7. Isolation Result

Held constant:

```text
risk number
threshold value
entity
protected dimension
uncertainty display
risk record
correction reachability
repair route
responsibility route
non-aggregation guard
necessity / alternative-search result
```

Varied only:

```text
threshold authority status
```

Outputs:

```text
illustrative -> blocked_by_threshold_status
provisional incomplete -> blocked_by_threshold_status
adopted -> limited_pass
```

Therefore this test isolates the threshold register's effect.

The register is not merely repeating the risk comparison.

It controls whether the comparison has authority.

## 8. What This Test Shows

Narrowly supported claim:

```text
TRACE can distinguish a numeric risk comparison from an authorised threshold comparison.
```

Potential decision delta:

```text
TRACE blocks permission where number-only reasoning would pass.
```

Scope:

```text
synthetic
single entity
single dimension
stipulated guard states
illustrative/provisional/adopted threshold statuses
```

This is not broad validation.

It is a cleaner partial delta than the previous stress test.

## 9. What This Test Does Not Show

It does not show:

```text
real-world threshold authority
a careful lawyer or regulator would miss this
profile-valued algebra changes the outcome
imprecise probability does more than require upper bound
TRACE generally beats careful reasoning
TRACE is validated
```

## 10. Falsifier

If a no-card careful reviewer, without TRACE, independently distinguishes all three threshold statuses and gives the same outputs:

```text
TRACE_DELTA_LOW
```

If a number-only reviewer passes all three and TRACE blocks A/B while permitting C only as limited pass:

```text
TRACE_DELTA_PARTIAL
```

If TRACE fails to change outcome by threshold status:

```text
TRACE_THRESHOLD_REGISTER_DECORATIVE
```

Current synthetic result:

```text
TRACE_DELTA_PARTIAL_CLEANER
```

## 11. Mechanical Ethics Translation

TRACE:

```text
same number, different threshold status
```

Mechanical Ethics:

A number is not authority.

TRACE:

```text
illustrative threshold
```

Mechanical Ethics:

This can explain a test but cannot govern a person's housing future.

TRACE:

```text
provisional threshold missing review / expiry
```

Mechanical Ethics:

A provisional standard without review discipline is not safe authority.

TRACE:

```text
adopted threshold + all other guards pass
```

Mechanical Ethics:

A limited action may proceed only within declared scope, with audit trail and correction route preserved.

## 12. Guardrail

This test must not be inflated into validation.

It answers only one question:

```text
Does threshold status alone change permission when all other guards are held constant?
```

Answer in this synthetic case:

```text
yes
```

If the project claims more than that, the translation layer has failed.
