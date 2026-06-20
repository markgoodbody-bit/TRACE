# TRACE Threshold Register v0.1

Status: core control surface / threshold governance.  
Parent files: `TRACE_MATH_KERNEL_v0_1.md`, `TRACE_KERNEL_INTEGRATION_MAP_v0_1.md`, `TRACE_VALUE_SPACE_ALGEBRA_v0_1.md`, `TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1.md`, `TRACE_NECESSITY_AND_ALTERNATIVE_SEARCH_v0_1.md`, `TRACE_PARETO_CHOICE_AND_INCOMPARABILITY_v0_1.md`, `TRACE_IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION_v0_1.md`.  
Reason: current kernel uses many thresholds. Without a register, verdicts can be steered by convenient numbers.

## 0. Purpose

TRACE thresholds must not be magic numbers.

A TRACE guard may use a threshold only if the threshold has a declared source, scope, status, and review rule.

This file defines the threshold control surface.

It does not set final canonical thresholds.

It defines how thresholds must be declared before they can be trusted.

## 1. Basic Rule

For any threshold:

```math
\theta
```

or tolerance:

```math
\epsilon
```

TRACE requires a register entry:

```math
Reg(\theta) or Reg(\epsilon)
```

If no valid register entry exists, the threshold is not authorised for high-stakes permission.

Default rule:

```text
No registered threshold, no high-stakes pass.
```

## 2. Threshold Record Schema

Minimum threshold record:

```text
threshold_id:
symbol:
name:
owner_file:
controlled_guard:
entity_scope:
dimension_scope:
action_scope:
time_horizon:
unit_or_domain:
value_or_range:
source_type:
source_reference:
authority:
status:
last_reviewed:
review_cycle:
uncertainty_attached:
conservative_default_if_absent:
change_log:
anti_gaming_note:
```

Threshold records are part of the evidentiary surface.

They must be inspectable.

## 3. Threshold Status

Allowed status values:

```text
draft
illustrative
case_specific
provisional
adopted
under_review
deprecated
invalid
```

Only the following can support a high-stakes pass:

```text
case_specific
provisional
adopted
```

But `case_specific` and `provisional` must carry explicit uncertainty and review route.

Illustrative thresholds may be used in examples only.

They must not be treated as canonical.

## 4. Source Types

Allowed source types:

```text
legal_floor
medical_or_safety_standard
empirical_distribution
historical_error_rate
system_SLA
contractual_rule
independent_audit
affected_party_requirement
expert_judgement
provisional_stewardship
unknown
```

`unknown` cannot support a high-stakes pass.

`expert_judgement` requires named expertise, conflict status, and uncertainty interval.

`provisional_stewardship` requires explicit expiry.

## 5. Threshold Classes

### 5.1 Livability / continuation threshold

```math
\theta_{live}
```

Controls:

```text
livable future-space LF_e(t)
positive continuation floor
```

Owner files:

```text
TRACE_FUTURE_SPACE_AND_CONTINUATION_v0_1.md
TRACE_VALUE_SPACE_ALGEBRA_v0_1.md
```

### 5.2 Protected floor threshold

```math
\theta^{floor}_{e,d}
```

Controls:

```text
protected dimension breach
minimum acceptable value profile component
```

Owner file:

```text
TRACE_VALUE_SPACE_ALGEBRA_v0_1.md
```

Register must state:

```text
entity type
protected dimension
why this is a floor
what evidence supports it
whether floor is hard or provisional
```

### 5.3 Catastrophic threshold

```math
\theta^{cat}_{e,d}
```

Controls:

```text
catastrophic tail event
```

Owner files:

```text
TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1.md
TRACE_IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION_v0_1.md
```

Catastrophic threshold must be stricter than protected floor:

```math
\theta^{cat}_{e,d} < \theta^{floor}_{e,d}
```

unless the dimension uses a binary floor.

### 5.4 Severe loss threshold

```math
\theta^{loss}_{e,d}
```

Controls:

```text
severe profile loss event
```

Owner file:

```text
TRACE_VALUE_SPACE_ALGEBRA_v0_1.md
```

### 5.5 Floor-breach tolerance

```math
\epsilon^{floor}_{e,d}
```

Controls:

```text
maximum tolerated probability of protected floor breach
```

This is not the same as the floor itself.

Register must state why this probability is tolerable.

### 5.6 Catastrophic-tail tolerance

```math
\epsilon^{cat}_{e,d}
```

Controls:

```text
maximum tolerated probability of catastrophic event
```

Catastrophic-tail tolerance must be lower than ordinary floor-breach tolerance:

```math
\epsilon^{cat}_{e,d} < \epsilon^{floor}_{e,d}
```

unless explicitly justified.

### 5.7 Severe-loss tolerance

```math
\epsilon^{loss}_{e,d}
```

Controls:

```text
maximum tolerated probability of severe loss
```

### 5.8 Reachability threshold

```math
\theta_{\rho}
```

Controls:

```text
when an abstract action is considered live
```

Owner file:

```text
TRACE_REACHABILITY_MODEL_v0_1.md
```

### 5.9 Correction reachability threshold

```math
\theta_{correct}
```

Controls:

```text
whether a formal correction route is meaningfully reachable
```

This threshold is more demanding than ordinary action availability.

Reason:

```text
correction must bite before harm hardens
```

### 5.10 Control threshold

```math
\theta^{ctrl}
```

Controls:

```text
whether an alternative adequately controls the relevant threat or need
```

Owner file:

```text
TRACE_NECESSITY_AND_ALTERNATIVE_SEARCH_v0_1.md
```

Control thresholds are profile-valued:

```math
\theta^{ctrl}=(\theta_{threat},\theta_{time},\theta_{scope},\theta_{recurrence},\theta_{repair})
```

No scalar control threshold should replace this without declaration.

### 5.11 Visibility threshold

```math
\theta_{visi}
```

Controls:

```text
hidden bill / hidden risk register trigger
```

Owner files:

```text
TRACE_VALUE_SPACE_ALGEBRA_v0_1.md
TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1.md
TRACE_IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION_v0_1.md
```

### 5.12 Point-probability threshold

```math
\theta^{pointP}
```

Controls:

```text
whether a point probability is authorised instead of imprecise probability
```

Owner file:

```text
TRACE_IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION_v0_1.md
```

If model/meta uncertainty exceeds this threshold, use:

```math
\mathcal{P}^{V}_e(a)
```

not a single `P`.

### 5.13 Hidden uncertainty bill threshold

```math
\theta_{HUB}
```

Controls:

```text
when hidden uncertainty display failure is material
```

Owner file:

```text
TRACE_IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION_v0_1.md
```

### 5.14 Time / correction horizon threshold

```math
T_{correction}
```

and:

```math
\tau_{breach}
```

Controls:

```text
whether harm or floor breach occurs before correction can bite
```

Owner files:

```text
TRACE_REACHABILITY_MODEL_v0_1.md
TRACE_NECESSITY_AND_ALTERNATIVE_SEARCH_v0_1.md
TRACE_IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION_v0_1.md
```

## 6. Register Validity Conditions

A threshold register entry is valid only if:

```text
symbol matches owner file
scope is explicit
status is not invalid/deprecated/illustrative for high-stakes use
source type is declared
authority is named or marked absent
time horizon is declared where relevant
uncertainty is visible
change log exists
```

If any required field is absent:

```math
Reg(\theta)=invalid
```

## 7. Conservative Default

For high-stakes actions:

```math
Reg(\theta)=invalid
```

forces:

```text
no permission grant from that threshold
```

If an action requires a threshold to pass and the threshold is missing, output:

```text
threshold_absent -> guard unresolved -> high-stakes pass forbidden
```

For low-stakes illustrative examples, missing thresholds may be marked:

```text
illustrative only
```

## 8. Anti-Gaming Rules

A system must not:

```text
choose thresholds after seeing desired outcome
lower a floor to pass an action
raise risk tolerance to permit a preferred action
narrow time horizon to hide future breach
switch from upper probability to point probability without authorisation
aggregate across entities to dilute an individual floor breach
rename a catastrophic threshold as ordinary loss
```

Threshold change after case exposure creates:

```math
Threshold_Drift_Flag=1
```

## 9. Threshold Drift Register

When a threshold changes, record:

```text
old value
new value
reason
who changed it
who benefits
who bears added risk
whether prior decisions would change
whether affected parties are notified
```

If a threshold change would alter prior verdicts:

```math
Retroactive_Instability=1
```

This triggers review.

## 10. Worked Example Status

The following files use illustrative thresholds:

```text
TRACE_WORKED_EXAMPLE_AUTOMATED_DECISION_LOCKIN_v0_1.md
TRACE_ADVERSARIAL_WORKED_EXAMPLE_NO_CARD_COMPARATOR_v0_1.md
```

Their numeric thresholds are not canonical.

They are test scaffolding.

A worked example can show pipeline execution using illustrative thresholds.

It cannot validate TRACE unless threshold sources are independently grounded.

## 11. Example Register Entry

```yaml
threshold_id: THR_income_floor_claimant_v0_1
symbol: theta_floor_s_income
name: claimant income-security protected floor
owner_file: TRACE_VALUE_SPACE_ALGEBRA_v0_1.md
controlled_guard: protected_floor_breach
action_scope: automated_benefit_debt_action
entity_scope: affected_claimant
dimension_scope: income_security
time_horizon: next_payment_cycle_to_review_completion
unit_or_domain: normalized value profile [0,1]
value_or_range: illustrative .55-.60
source_type: provisional_stewardship
source_reference: worked_example_only
authority: none / illustrative
status: illustrative
last_reviewed: 2026-06-21
review_cycle: before operational use
uncertainty_attached: high
conservative_default_if_absent: no high-stakes pass
change_log: initial illustrative entry
anti_gaming_note: cannot be used outside examples
```

## 12. Output Schema

When a TRACE run uses thresholds, output:

```text
thresholds_used:
  - threshold_id
  - symbol
  - status
  - value_or_range
  - source_type
  - authority
  - time_horizon
  - uncertainty_attached
invalid_or_missing_thresholds:
  - symbol
  - affected_guard
  - consequence
threshold_drift_flags:
  - threshold_id
  - drift_type
  - prior_verdict_effect
```

## 13. Mechanical Ethics Translation

TRACE:

```math
Reg(\theta)=invalid
```

Mechanical Ethics:

The system has not earned the right to use this threshold for permission.

TRACE:

```math
Threshold_Drift_Flag=1
```

Mechanical Ethics:

The system may be moving the standard to fit the desired action.

TRACE:

```math
threshold_absent -> high-stakes pass forbidden
```

Mechanical Ethics:

Do not treat an unstated standard as authority over a person's future.

TRACE:

```math
status=illustrative
```

Mechanical Ethics:

This number can explain a test, but cannot justify real action.

## 14. Guardrail

Thresholds are not neutral.

Thresholds are where judgement enters the machine.

TRACE must expose them.

No hidden thresholds.

No retrospective thresholds.

No high-stakes pass from illustrative numbers.

No aggregation that makes a floor breach disappear.
