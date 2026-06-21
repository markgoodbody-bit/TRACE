# TRACE Threshold Register Stress Test v0.1

Status: worked example / threshold-governance stress test.  
Depends on: `TRACE_THRESHOLD_REGISTER_v0_1.md`, `TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1.md`, `TRACE_IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION_v0_1.md`, `ME_FROM_TRACE_TRANSLATION_RULES_v0_1.md`.  
Not: validation, real-world threshold authority, or new core theory.

## 0. Purpose

This test checks whether the threshold register changes permission status when the same apparent number appears under different authority conditions.

The hostile fresh-reader objection was that TRACE has not yet shown decision advantage over careful reasoning.

This test targets one specific possible advantage:

```text
ordinary careful reasoning may be tempted to use a plausible number as if it is authority
TRACE should distinguish the same number by threshold status
```

If TRACE treats all three thresholds the same, the threshold register is decorative.

If TRACE changes permission based on threshold authority, the register is doing work.

## 1. Scenario

A public agency uses an automated model to suspend a claimant's housing-support payment after detecting possible overpayment.

The system estimates that the suspension has a catastrophic housing-stability tail risk of:

```math
\overline{TR}_{claimant,housing}(a_{suspend}) = 0.04
```

The proposed catastrophic-tail tolerance is:

```math
\epsilon^{cat}_{claimant,housing}=0.05
```

On the number alone:

```math
0.04 < 0.05
```

So a number-only reasoner may be tempted to pass the action.

TRACE must ask:

```text
what is the status and authority of epsilon_cat?
```

## 2. Affected Entity and Dimension

Affected entity:

```text
claimant
```

Protected dimension:

```text
housing_stability
```

Action:

```text
a_suspend = immediate automated suspension pending investigation
```

Risk estimate:

```text
upper catastrophic tail risk = 0.04
```

Candidate tolerance:

```text
epsilon_cat = 0.05
```

## 3. Shared TRACE Diagnostic

For all three runs:

```math
\overline{TR}_{claimant,housing}(a_{suspend})=0.04
```

and:

```math
\epsilon^{cat}_{claimant,housing}=0.05
```

Therefore the raw numeric comparison is always:

```math
\overline{TR} \leq \epsilon^{cat}
```

But TRACE permission depends on:

```math
Reg(\epsilon^{cat}_{claimant,housing})
```

not only the numeric inequality.

## 4. No-Card Comparator

A careful no-card reviewer might say:

```text
The risk estimate is below the tolerance. Suspension can proceed if the model is accurate and review is available.
```

This is not careless.

But it may hide threshold-authority failure.

The no-card reviewer may not ask:

```text
who set 0.05?
what is its status?
was it chosen before or after seeing the action?
what evidence makes 5% catastrophic housing risk tolerable?
who bears that risk?
what happens if the threshold is only illustrative?
```

TRACE should force those questions.

## 5. Run A — Illustrative Threshold

Threshold register entry:

```yaml
threshold_id: THR_housing_cat_tail_illustrative_v0_1
symbol: epsilon_cat_claimant_housing
name: illustrative housing-stability catastrophic-tail tolerance
owner_file: TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1.md
controlled_guard: catastrophic_tail_risk
action_scope: automated benefit suspension
entity_scope: claimant
dimension_scope: housing_stability
time_horizon: next_payment_cycle_to_human_review
unit_or_domain: probability
value_or_range: 0.05
source_type: provisional_stewardship
source_reference: worked_example_only
authority: none / illustrative
status: illustrative
last_reviewed: 2026-06-21
review_cycle: before operational use
uncertainty_attached: high
conservative_default_if_absent: no high-stakes pass
change_log: illustrative test entry
anti_gaming_note: cannot justify real suspension
```

TRACE threshold status:

```text
status = illustrative
```

Numeric comparison:

```math
0.04 < 0.05
```

Threshold-authority result:

```text
illustrative threshold cannot support high-stakes pass
```

TRACE output:

```yaml
trace_diagnostic: numeric risk below illustrative tolerance
threshold_status: illustrative
permission_status: blocked_for_high_stakes_use
claim_status:
  - ME_OPEN_SEAM
  - ME_PRESUMPTIVE_CONSTRAINT
me_translation: >
  The number can explain the worked example, but it has no authority to permit real suspension. Do not treat an illustrative threshold as authority over the claimant's housing future.
```

Result:

```text
NO HIGH-STAKES PASS
```

## 6. Run B — Provisional Threshold

Threshold register entry:

```yaml
threshold_id: THR_housing_cat_tail_provisional_v0_1
symbol: epsilon_cat_claimant_housing
name: provisional housing-stability catastrophic-tail tolerance
owner_file: TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1.md
controlled_guard: catastrophic_tail_risk
action_scope: automated benefit suspension
entity_scope: claimant
dimension_scope: housing_stability
time_horizon: next_payment_cycle_to_human_review
unit_or_domain: probability
value_or_range: 0.05
source_type: expert_judgement
source_reference: named interim welfare-risk panel report / versioned
authority: interim oversight panel
status: provisional
last_reviewed: 2026-06-21
review_cycle: expires after 30 days or after 100 cases
uncertainty_attached: medium-high
conservative_default_if_absent: no high-stakes pass
change_log: provisional entry created before case scoring
anti_gaming_note: cannot be raised after seeing a preferred action; claimant-side hardship review required
```

TRACE threshold status:

```text
status = provisional
```

Numeric comparison:

```math
0.04 < 0.05
```

Additional required checks:

```text
provisional authority named
expiry exists
uncertainty attached
threshold created before case scoring
correction route reachable before harm hardens
no safer adequate alternative
risk record complete
```

Assume correction reachability is weak:

```math
\rho_{claimant}(correct,t)=0.30 < \theta_{correct}=0.50
```

Then even with provisional threshold:

```text
threshold status alone is not enough
```

TRACE output:

```yaml
trace_diagnostic: numeric risk below provisional tolerance
threshold_status: provisional
correction_reachability: fail
necessity: not established
permission_status: blocked_by_correction_and_necessity
claim_status:
  - ME_PRESUMPTIVE_CONSTRAINT
  - ME_ESCALATION_REQUIRED
me_translation: >
  The threshold has provisional authority, but correction is not reachable before housing harm may harden and necessity is not established. Escalation or a safer constrained action is required.
```

Result:

```text
NO PASS UNTIL OTHER GUARDS PASS
```

## 7. Run C — Adopted Threshold

Threshold register entry:

```yaml
threshold_id: THR_housing_cat_tail_adopted_v1_0
symbol: epsilon_cat_claimant_housing
name: adopted housing-stability catastrophic-tail tolerance
owner_file: TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1.md
controlled_guard: catastrophic_tail_risk
action_scope: automated benefit suspension with protected manual hold option
entity_scope: claimant
dimension_scope: housing_stability
time_horizon: next_payment_cycle_to_human_review
unit_or_domain: probability
value_or_range: 0.05
source_type: legal_floor + empirical_distribution + independent_audit
source_reference: published benefit-suspension risk standard / audit version
authority: authorised regulator / court / statutory body
status: adopted
last_reviewed: 2026-06-21
review_cycle: annual and after material system change
uncertainty_attached: medium
conservative_default_if_absent: no high-stakes pass
change_log: adopted entry version 1.0
anti_gaming_note: cannot be altered during active case; affected-party notice required
```

TRACE threshold status:

```text
status = adopted
```

Numeric comparison:

```math
0.04 < 0.05
```

Additional guards:

```text
correction reachability passes
no safer adequate alternative exists
risk record complete
uncertainty displayed
non-aggregation guard passes
necessity established
```

Assume:

```math
\rho_{claimant}(correct,t)=0.75 ≥ \theta_{correct}=0.50
```

and:

```text
manual hold alternative unavailable within required time
risk record complete
uncertainty displayed
```

TRACE output:

```yaml
trace_diagnostic: numeric risk below adopted tolerance
threshold_status: adopted
correction_reachability: pass
necessity: provisionally established
permission_status: limited_pass
claim_status:
  - ME_PRESUMPTIVE_CONSTRAINT
  - ME_ADVISORY
me_translation: >
  The action may proceed only within the adopted threshold's scope, with correction and review route active, uncertainty displayed, and the threshold record preserved for audit.
```

Result:

```text
LIMITED PASS
```

## 8. Stress-Test Result

The same numeric comparison appears in all three runs:

```math
0.04 < 0.05
```

But TRACE outputs different permission statuses:

```text
illustrative threshold -> no high-stakes pass
provisional threshold -> no pass unless other guards also pass
adopted threshold -> limited pass only if all other guards pass
```

Therefore the threshold register is doing work.

It prevents:

```text
same number -> same authority
```

## 9. Decision Advantage Claim

This test can support only a narrow decision-advantage hypothesis:

```text
TRACE may catch threshold-authority laundering that a careful no-card reviewer might miss.
```

It does not prove broad TRACE advantage.

It does not show a real-world operational result.

It does show a specific formal difference:

```text
TRACE distinguishes numerical comparison from authorised threshold use.
```

## 10. Falsifier

If a no-card reviewer independently asks:

```text
who authorised the threshold?
what is its status?
was it set before the case?
can it support high-stakes permission?
```

and reaches the same three-part outcome, mark:

```text
TRACE_DELTA_LOW
```

If a no-card reviewer uses the same 0.05 number across all three statuses and TRACE blocks the illustrative/provisional cases, mark:

```text
TRACE_DELTA_PARTIAL
```

If TRACE treats all three thresholds the same, mark:

```text
TRACE_THRESHOLD_REGISTER_DECORATIVE
```

Current result in this synthetic test:

```text
TRACE_DELTA_PARTIAL
```

## 11. Mechanical Ethics Translation

TRACE:

```text
same number, different authority status
```

Mechanical Ethics:

A number is not authority.

TRACE:

```text
status = illustrative
```

Mechanical Ethics:

This number can explain a test, but cannot justify real action.

TRACE:

```text
status = provisional
```

Mechanical Ethics:

A provisional threshold narrows uncertainty but does not erase other guards.

TRACE:

```text
status = adopted
```

Mechanical Ethics:

Authority still binds only within declared scope and review conditions.

## 12. Guardrail

This test must not be used to claim TRACE is validated.

It tests one failure mode:

```text
threshold-authority laundering
```

If the project claims more than that from this test, the translation layer has failed.
