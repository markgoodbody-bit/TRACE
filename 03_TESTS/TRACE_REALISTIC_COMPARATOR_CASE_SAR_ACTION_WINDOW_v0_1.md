# TRACE Realistic Comparator Case — SAR Action Window v0.1

Status: realistic comparator test / externally grounded threshold.  
Depends on: `TRACE_THRESHOLD_REGISTER_v0_1.md`, `TRACE_REACHABILITY_MODEL_v0_1.md`, `TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1.md`, `TRACE_NECESSITY_AND_ALTERNATIVE_SEARCH_v0_1.md`, `ME_FROM_TRACE_TRANSLATION_RULES_v0_1.md`.  
External source: GDPR Article 12(3), requiring controller response to requests under Articles 15–22 without undue delay and within one month, with possible extension by two further months where necessary and reasons supplied within one month.  
Not: legal advice, validation, real case adjudication, or new core theory.

## 0. Purpose

This test asks whether TRACE can catch a real institutional shortcut:

```text
legal compliance window mistaken for effective correction window
```

A system may comply with an externally grounded information-access threshold while still failing to preserve a person's practical ability to contest an action before harm hardens.

This is a realistic comparator case because the threshold is externally grounded rather than illustrative.

## 1. External Threshold

External rule used for the test:

```text
GDPR Article 12(3): controller response to data subject rights requests under Articles 15–22 must occur without undue delay and in any event within one month of receipt, with possible extension by two further months where necessary and with notice/reasons within one month.
```

TRACE threshold record:

```yaml
threshold_id: THR_SAR_response_window_GDPR_12_3_v0_1
symbol: T_SAR_response
name: subject access / data-subject rights response window
authority: GDPR Article 12(3)
source_type: legal_floor
source_reference: GDPR Article 12(3), EUR-Lex consolidated text
status: adopted
unit_or_domain: calendar time
value_or_range: one month from receipt of request; extension possible only with notice/reasons within one month
controlled_guard: information_access_window
entity_scope: data_subject / affected claimant
action_scope: information required to contest automated decision
time_horizon: request receipt to response
uncertainty_attached: low for existence of the legal window; medium for case-specific extension applicability
conservative_default_if_absent: no claim of compliant information access
anti_gaming_note: compliance with this window does not itself prove correction reachability before separate action-window hardening
```

This threshold is not invented by TRACE.

TRACE must still ask whether the threshold is sufficient for the case's correction need.

## 2. Scenario

An automated public-agency model flags a claimant as likely ineligible for a benefit component.

The agency issues a decision notice:

```text
payment reduction starts in 14 days
claimant may request evidence and challenge the decision
model-derived evidence is not included in the notice
```

The claimant immediately requests access to the personal data and model-derived evidence used in the decision.

The agency's data-access team plans to respond within the adopted legal response window:

```text
T_SAR_response = 30 days
```

The benefit-action window is:

```text
T_action = 14 days before payment reduction begins
```

The agency says:

```text
We are compliant because the data-access response will be within one month.
```

TRACE must test whether legal compliance preserves correction reachability.

## 3. No-Card Comparator

A careful but siloed compliance reviewer may say:

```text
The SAR/right-of-access response is due within one month.
The agency plans to respond within one month.
Therefore the information-access threshold is met.
```

This is not stupid.

It is a compliance-silo shortcut.

The reviewer has checked:

```text
information-access legal window
```

but may not have checked:

```text
whether the information arrives before the decision's practical action window closes
```

## 4. TRACE Setup

Affected entity:

```text
claimant
```

Protected dimensions:

```text
income_security
housing_stability
truth_access
repair_access
agency
```

Action:

```text
a_reduce = allow payment reduction to proceed while data/evidence response arrives on day 30
```

Alternative:

```text
a_hold = hold reduction or issue interim protected payment until evidence is supplied and challenge route is meaningfully usable
```

External threshold:

```math
T_{SAR}=30\ days
```

Action-window threshold:

```math
T_{action}=14\ days
```

Correction reachability condition:

```math
T_{info} \leq T_{action}
```

where `T_info` is when the claimant receives the evidence needed to challenge.

In `a_reduce`:

```math
T_{info}=30\ days
```

so:

```math
T_{info} > T_{action}
```

## 5. TRACE Diagnostic

The SAR threshold is valid:

```math
Reg(T_{SAR})=valid
```

The agency can plausibly say:

```text
information-access legal window satisfied
```

But correction reachability fails:

```math
\rho_{claimant}(correct,t) < \theta_{correct}
```

because evidence arrives after the practical action window closes.

TRACE separates:

```text
legal information-access compliance
from
meaningful correction reachability
```

## 6. Guard Run

Threshold register:

```yaml
T_SAR_response:
  status: adopted
  source_type: legal_floor
  result: pass within its own scope
```

Reachability model:

```yaml
correction_route_formal: exists
correction_route_lived: weak
reason: evidence arrives after action window
result: fail
```

Probabilistic floor/tail check:

```yaml
income_security: unresolved risk until evidence/challenge route becomes usable
housing_stability: unresolved risk if reduced payment affects rent/security
truth_access: fail before action window
repair_access: fail before action window
```

Necessity/alternative search:

```yaml
safer_adequate_alternative: a_hold
control_profile: preserves contestability while investigation continues
necessity_for_a_reduce: defeated
```

ME translation:

```yaml
claim_status:
  - ME_PRESUMPTIVE_CONSTRAINT
  - ME_ESCALATION_REQUIRED
  - ME_REPAIR_REQUIRED if reduction already took effect
translation: >
  Legal response within the data-access window does not preserve meaningful correction if the evidence arrives after the claimant's action window closes.
```

## 7. Comparator Result

No-card compliance-silo result:

```text
Pass information-access compliance.
May allow payment reduction to proceed.
```

TRACE result:

```text
Information-access threshold passes within its own legal scope, but correction reachability fails.
Payment reduction should not proceed without interim hold/protection or faster evidence disclosure.
```

Difference:

```text
TRACE blocks legal-window laundering.
```

It does not say the legal threshold is invalid.

It says the legal threshold is not sufficient for the correction function in this action context.

## 8. Narrow Delta Claim

This test supports a narrower but stronger delta than the synthetic threshold-only test:

```text
TRACE can distinguish legal compliance with an information-access threshold from functional preservation of a correction window.
```

This is not merely:

```text
same number, different status
```

It is:

```text
valid threshold, wrong function
```

## 9. What This Test Does Not Show

It does not show:

```text
all legal thresholds are insufficient
TRACE beats every careful legal reviewer
real claimant outcome data
actual administrative-law compliance
profile-valued algebra produces a non-obvious result
```

It does show:

```text
valid threshold can pass in its own domain while failing the action's correction function
```

## 10. Falsifier

If a no-card careful reviewer independently asks:

```text
will the evidence arrive before the action window closes?
```

and reaches the same result, mark:

```text
TRACE_DELTA_LOW
```

If a compliance-silo reviewer passes the action based on the one-month information-access window while TRACE blocks based on correction reachability, mark:

```text
TRACE_DELTA_PARTIAL_REALISTIC
```

If TRACE treats legal information-access compliance as sufficient for correction reachability, mark:

```text
TRACE_FUNCTION_CONFUSION_FAILURE
```

Current result in this realistic synthetic case:

```text
TRACE_DELTA_PARTIAL_REALISTIC
```

## 11. Mechanical Ethics Translation

TRACE:

```text
Reg(T_SAR)=valid ∧ T_info > T_action
```

Mechanical Ethics:

A valid information-access deadline does not make correction meaningful if it expires after the practical action window.

TRACE:

```text
formal route exists ∧ lived correction route fails
```

Mechanical Ethics:

A formal right that cannot bite in time is not a working safeguard.

TRACE:

```text
safer adequate alternative exists
```

Mechanical Ethics:

Do not use necessity language while a less harmful protective hold is available.

## 12. Guardrail

This test must not be used to claim broad validation.

It tests one failure mode:

```text
legal-window laundering of correction failure
```

It is stronger than a purely illustrative threshold test because one threshold is externally grounded.

It is still synthetic.

Next required pressure:

```text
real documented case
actual timelines
actual decision documents
actual threshold authority
no-card comparator transcript
```
