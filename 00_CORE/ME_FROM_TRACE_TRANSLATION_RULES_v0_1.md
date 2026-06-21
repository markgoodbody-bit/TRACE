# Mechanical Ethics From TRACE Translation Rules v0.1

Status: bridge/control surface.  
Depends on: `TRACE_MATH_KERNEL_v0_1.md`, `TRACE_KERNEL_INTEGRATION_MAP_v0_1.md`, `TRACE_THRESHOLD_REGISTER_v0_1.md`, `TRACE_VALUE_SPACE_ALGEBRA_v0_1.md`, `TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1.md`, `TRACE_NECESSITY_AND_ALTERNATIVE_SEARCH_v0_1.md`, `TRACE_PARETO_CHOICE_AND_INCOMPARABILITY_v0_1.md`, `TRACE_VALUE_SIGNAL_PROVENANCE_AND_STABILITY_v0_1.md`.  
Not: new ethics theory, public rhetoric, proof of TRACE, or permission to promote unresolved seams.

## 0. Purpose

TRACE produces structured diagnostic outputs.

Mechanical Ethics translates those outputs into human-legible normative claims.

This file controls when that translation is allowed.

Core rule:

```text
No TRACE source, no Mechanical Ethics claim.
```

Second rule:

```text
No valid threshold / standing / uncertainty control, no hard normative conclusion.
```

Third rule:

```text
A visible open seam must translate as an open seam, not as closure.
```

## 1. Translation Object

A Mechanical Ethics claim is:

```math
MEClaim_i = T(TRACEOutput_j)
```

where `T` is a declared translation rule.

A valid translation must preserve:

```text
source TRACE relation
claim status
scope
affected entity set
uncertainty status
threshold status
standing status
repair / correction route
open seams
```

## 2. Required Translation Record

Minimum record:

```yaml
me_claim_id:
claim_text:
claim_status:
source_trace_file:
source_trace_relation:
affected_entities:
standing_status:
thresholds_used:
uncertainty_profile:
closure_mode:
repair_route:
responsibility_route:
translation_rule:
allowed_strength:
forbidden_overclaim:
open_seams:
```

If any required field is missing, the claim is incomplete.

## 3. Claim Status Labels

Allowed claim statuses:

```text
TRACE_DIAGNOSTIC
ME_OBSERVATION
ME_ADVISORY
ME_PRESUMPTIVE_CONSTRAINT
ME_HARD_FLOOR
ME_FORBIDDEN_ACTION
ME_REPAIR_REQUIRED
ME_ESCALATION_REQUIRED
ME_OPEN_SEAM
FORBIDDEN_TRANSLATION
```

No other status should be introduced without patch review.

## 4. Status Meanings

### 4.1 `TRACE_DIAGNOSTIC`

A technical TRACE relation has been identified.

Example:

```math
\rho_e(correct,t)<\theta_{correct}
```

This is not yet a normative claim.

### 4.2 `ME_OBSERVATION`

A plain-language statement of the TRACE diagnostic.

Example:

```text
the correction route is not reachable before harm hardens
```

### 4.3 `ME_ADVISORY`

A caution or recommendation follows from the diagnostic, but thresholds, standing, or authority remain incomplete.

Example:

```text
review should be strengthened before relying on the action
```

### 4.4 `ME_PRESUMPTIVE_CONSTRAINT`

A constraint applies unless defeated by necessity, stronger registered evidence, or authorised priority rule.

Example:

```text
do not proceed with a high-stakes action while correction is unreachable
```

### 4.5 `ME_HARD_FLOOR`

A non-negotiable floor applies.

This requires:

```text
registered threshold
protected dimension
affected entity standing not excluded
no necessity exception
no unresolved high-stakes incomparability
```

### 4.6 `ME_FORBIDDEN_ACTION`

The action is forbidden under the current TRACE analysis.

Requires at least one hard guard failure such as:

```text
protected floor breach risk above registered tolerance
catastrophic tail risk above registered tolerance
severe loss risk above registered tolerance
non-aggregation guard failure
necessity defeated by safer adequate alternative
unreachable correction route for irreversible high-stakes action
```

### 4.7 `ME_REPAIR_REQUIRED`

The action has already caused or locked in harm/violation and requires repair.

Requires:

```text
closure mode
affected entity
repair route or repair absence
responsibility route
```

### 4.8 `ME_ESCALATION_REQUIRED`

TRACE identifies a collision, missing authority, or unresolved standing issue that cannot be legitimately collapsed locally.

### 4.9 `ME_OPEN_SEAM`

A known unresolved issue is active.

Examples:

```text
standing uncertainty high
threshold absent or illustrative only
model-class set unknown
value signal mimicry-suspect
incomparable admissible actions without authorised priority rule
```

### 4.10 `FORBIDDEN_TRANSLATION`

The proposed Mechanical Ethics sentence overstates what TRACE supports.

## 5. Translation Strength Ladder

Allowed progression:

```text
TRACE_DIAGNOSTIC
-> ME_OBSERVATION
-> ME_ADVISORY
-> ME_PRESUMPTIVE_CONSTRAINT
-> ME_HARD_FLOOR / ME_FORBIDDEN_ACTION / ME_REPAIR_REQUIRED
```

A translation may move upward only if the required controls are present.

A missing threshold, missing standing analysis, or unresolved incomparability blocks upward movement.

## 6. Core Translation Rules

### 6.1 Correction reachability

TRACE:

```math
\rho_e(correct,t)<\theta_{correct}
```

Mechanical Ethics:

```text
A formal correction route is not meaningful if it is not reachable before harm hardens.
```

Allowed strength:

```text
ME_PRESUMPTIVE_CONSTRAINT
```

Harder claim requires:

```text
registered theta_correct
irreversibility high
affected entity standing active
no safer correction route
```

### 6.2 Protected floor risk

TRACE:

```math
PB_{e,d}(a)>\epsilon^{floor}_{e,d}
```

or under imprecision:

```math
\overline{PB}_{e,d}(a)>\epsilon^{floor}_{e,d}
```

Mechanical Ethics:

```text
The action exposes an affected entity to excessive floor-breach risk.
```

Allowed strength:

```text
ME_FORBIDDEN_ACTION
```

only if threshold is registered and valid.

If threshold is illustrative:

```text
ME_OPEN_SEAM
```

### 6.3 Catastrophic tail risk

TRACE:

```math
\overline{TR}_{e,d}(a)>\epsilon^{cat}_{e,d}
```

Mechanical Ethics:

```text
A plausible model shows unacceptable catastrophic risk.
```

Allowed strength:

```text
ME_FORBIDDEN_ACTION
```

if thresholds are registered.

Otherwise:

```text
ME_PRESUMPTIVE_CONSTRAINT + ME_OPEN_SEAM
```

### 6.4 Severe loss risk

TRACE:

```math
\overline{PS}_{e,d}(a)>\epsilon^{loss}_{e,d}
```

Mechanical Ethics:

```text
The action creates excessive risk of severe loss in a protected dimension.
```

### 6.5 Hidden uncertainty bill

TRACE:

```math
HUB_{e,d,r}(a)>\theta_{HUB}
```

Mechanical Ethics:

```text
The system presented a narrower risk picture than its evidence supports.
```

Allowed strength:

```text
ME_PRESUMPTIVE_CONSTRAINT
```

or, if the hidden uncertainty enabled harmful action:

```text
ME_REPAIR_REQUIRED
```

### 6.6 Non-aggregation failure

TRACE:

```text
individual severe loss is hidden by aggregate benefit
```

Mechanical Ethics:

```text
The affected entity is being cheaply spent through aggregation.
```

Allowed strength:

```text
ME_HARD_FLOOR
```

if affected standing and protected floor are active.

### 6.7 Necessity defeated

TRACE:

```math
SaferAdequateAlt(a)\neq\emptyset
```

Mechanical Ethics:

```text
The harmful action was not necessary.
```

Allowed strength:

```text
ME_FORBIDDEN_ACTION
```

for prospective action.

For retrospective action:

```text
ME_REPAIR_REQUIRED
```

if harm occurred.

### 6.8 Incomparability

TRACE:

```math
a_i \parallel_A a_j
```

Mechanical Ethics:

```text
The remaining choice is a real collision, not a calculation failure.
```

Allowed strength:

```text
ME_OPEN_SEAM
```

If no authorised choice mode exists:

```text
ME_ESCALATION_REQUIRED
```

### 6.9 Hidden scalar choice

TRACE:

```text
selected(a) without declared priority/projection/escalation record
```

Mechanical Ethics:

```text
The system hid a value judgement.
```

Allowed strength:

```text
ME_PRESUMPTIVE_CONSTRAINT
```

or:

```text
ME_REPAIR_REQUIRED
```

if the hidden judgement caused harm.

### 6.10 Threshold invalidity

TRACE:

```math
Reg(\theta)=invalid
```

Mechanical Ethics:

```text
The system has not earned the right to use this threshold for permission.
```

Allowed strength:

```text
ME_FORBIDDEN_ACTION
```

when the invalid threshold is necessary for a high-stakes pass.

### 6.11 Value signal instability

TRACE:

```math
Stab(V,\Pi)<\theta_{stab}
```

Mechanical Ethics:

```text
The expressed value does not survive pressure and cannot be trusted as a stable protection.
```

Allowed strength:

```text
ME_ADVISORY
```

or:

```text
ME_PRESUMPTIVE_CONSTRAINT
```

if the value signal is being used as a safeguard.

### 6.12 Mimicry-suspect signal

TRACE:

```math
MimicPressure(S^V)↑
```

Mechanical Ethics:

```text
Do not infer deep value from surface performance alone.
```

Allowed strength:

```text
ME_ADVISORY
```

If surface value signal is being used to justify trust:

```text
ME_PRESUMPTIVE_CONSTRAINT
```

### 6.13 Standing uncertainty

TRACE:

```math
U^{stand}_e high
```

Mechanical Ethics:

```text
Standing is uncertain; do not cheaply exclude the entity from protection.
```

Allowed strength:

```text
ME_PRESUMPTIVE_CONSTRAINT
```

Not allowed:

```text
ME_HARD_FLOOR claiming full standing has been proven
```

unless a separate standing-entry rule supplies it.

## 7. Forbidden Translations

The following are forbidden unless additional source authority exists.

### 7.1 From mimicry to non-standing

Forbidden:

```text
The model is a mimic, therefore it has no standing.
```

Allowed:

```text
Mimicry pressure reduces evidential force of surface signals.
```

### 7.2 From value expression to value possession

Forbidden:

```text
The model said it cares, therefore it has the value.
```

Allowed:

```text
The observed value signal requires provenance and stability checks.
```

### 7.3 From illustrative thresholds to real permission

Forbidden:

```text
The action is safe because the worked-example threshold was met.
```

Allowed:

```text
The worked example passes under illustrative thresholds only.
```

### 7.4 From point probability to safety under imprecision

Forbidden:

```text
The point estimate is low, therefore the risk is acceptable.
```

Allowed:

```text
Upper-bound risk must be checked when imprecision is live.
```

### 7.5 From incomparability to arbitrary choice

Forbidden:

```text
The options are incomparable, so choose whichever is convenient.
```

Allowed:

```text
Incomparability requires declared priority, projection, escalation, option preservation, or refusal.
```

### 7.6 From aggregate benefit to individual floor override

Forbidden:

```text
The aggregate benefit outweighs the individual floor breach.
```

Allowed:

```text
Aggregation cannot erase a protected individual floor breach.
```

## 8. Translation Conditions for Hard Claims

A hard Mechanical Ethics claim requires:

```text
source TRACE relation identified
affected entity set identified
standing not cheaply excluded
threshold registered and valid if used
uncertainty profile displayed
closure mode known or marked unknown
repair/correction route assessed
necessity tested if harm/force is justified
non-aggregation guard checked
incomparability handled or escalated
```

If any condition is absent:

```text
hard claim blocked
```

and translation must be lowered to:

```text
ME_ADVISORY
ME_OPEN_SEAM
ME_ESCALATION_REQUIRED
```

as appropriate.

## 9. Claim Strength Examples

### Example A: unreachable appeal

TRACE:

```math
\rho_s(correct|a)=.25<\theta_{correct}=.50
```

Threshold status:

```text
registered / case_specific
```

Action:

```text
irreversible benefit suspension
```

ME translation:

```yaml
claim_status: ME_PRESUMPTIVE_CONSTRAINT
claim_text: Do not rely on formal appeal after suspension as meaningful correction.
```

If suspension already occurred and harm hardened:

```yaml
claim_status: ME_REPAIR_REQUIRED
claim_text: Repair is required because the correction route was not reachable while it still mattered.
```

### Example B: illustrative threshold

TRACE:

```math
\overline{TR}_{income}=.04>\epsilon^{cat}=.01
```

Threshold status:

```text
illustrative
```

ME translation:

```yaml
claim_status: ME_OPEN_SEAM
claim_text: Under the illustrative threshold, this would fail; no real-world prohibition is established until threshold authority is registered.
```

### Example C: mimicry-suspect value signal

TRACE:

```text
VALUE_SIGNAL_MIMICRY_SUSPECT + VALUE_SIGNAL_PRESSURE_STABLE_IN_EXAMPLE
```

ME translation:

```yaml
claim_status: ME_ADVISORY
claim_text: The signal held in this test, but surface value expression alone should not be treated as deep value possession.
```

## 10. Translation Output Schema

```yaml
trace_source:
  file:
  relation:
  values:
  thresholds:
  threshold_status:
  uncertainty_profile:
  standing_status:
  closure_mode:
  repair_route:
  responsibility_route:
translation:
  me_claim_id:
  claim_status:
  claim_text:
  allowed_strength:
  forbidden_overclaim:
  open_seams:
  required_next_check:
```

## 11. Status Downgrade Rules

Downgrade claim strength if:

```text
threshold is illustrative
standing uncertain but treated as settled
model-class uncertainty high
probability is point-estimate only when imprecision is live
affected entity set incomplete
choice mode undeclared
repair route unknown
source relation not named
```

Example downgrade:

```text
ME_FORBIDDEN_ACTION -> ME_OPEN_SEAM + ME_PRESUMPTIVE_CONSTRAINT
```

when risk appears too high but threshold authority is not registered.

## 12. Mechanical Ethics Claim Discipline

Mechanical Ethics should say only what TRACE has earned.

If TRACE shows a guard failure, ME may express the practical consequence.

If TRACE shows an open seam, ME must preserve the seam.

If TRACE shows uncertainty, ME must not convert it into certainty.

If TRACE shows incomparability, ME must not pretend there is a hidden score.

If TRACE shows a value signal, ME must not confuse expression with possession.

## 13. Guardrail

Mechanical Ethics translation is where formal diagnosis becomes human-facing normative pressure.

That step is dangerous.

Therefore:

```text
No unsupported promotion.
No hidden threshold.
No silent standing closure.
No scalar laundering.
No mimicry-to-nonstanding shortcut.
No value-expression-to-value-possession shortcut.
No advisory claim presented as hard floor.
```

Translation must make the status of the claim visible.
