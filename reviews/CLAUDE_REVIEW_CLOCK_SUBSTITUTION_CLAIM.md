# Claude Review Target: Clock Substitution Claim

Status: review target only. Not v0.12. Not validation.

Claude: please hostile-review this file. Do not praise. Do not agree by default. Do not expand the framework unless the need is forced.

## Context

TRACE v0.11 already has:

```trace
TransitionClaim.clock_effect
review_clock
delay_laundering
hardening_clock
RAPID_TRIAGE → FULL_TRACE
missing_information ≠ permission_not_to_decide
```

A proposed Temporal Clock Index was too heavy. Z.ai pressure suggested shrinking it.

This file tests the smaller idea: **Clock Substitution Claim**.

---

## Candidate

```trace
ClockSubstitutionClaim :=
  required only when one clock is used to pause, delay, override, or justify another clock
```

Examples:

```trace
public_inquiry_clock pauses survivor_support_clock
criminal_justice_clock pauses remediation_clock
emergency_clock pauses review_clock
budget_clock pauses safety_clock
```

Minimum form:

```trace
ClockSubstitutionMinimum := {
  paused_clock,
  pausing_clock,
  pausing_clock_controller,
  hardening_effect_of_pause,
  review_clock_for_pause,
  contest_edge
}
```

Full form, if needed later:

```trace
ClockSubstitutionClaim := Claim({
  paused_clock,
  pausing_clock,
  pausing_clock_controller,
  justification_for_pause,
  affected_scope,
  hardening_effect_of_pause,
  evidence_decay_effect_if_any,
  interim_action_required,
  review_clock_for_pause,
  contest_edge,
  capture_risk
})
```

---

## Guardrail

Do not index every clock.

```trace
multiple_clocks ≠ ClockSubstitutionClaim_required
clock_A_pauses_clock_B ⇒ ClockSubstitutionClaim_required
```

The point is not temporal bureaucracy. The point is to expose clock substitution.

---

## Review questions

Please answer:

1. Does this add real value beyond v0.11's existing `TransitionClaim.clock_effect`?
2. Is this smaller candidate better than the full Temporal Clock Index?
3. Does it catch real laundering patterns, especially Grenfell-style inquiry/support/safety clock substitution?
4. What loophole does it create?
5. Should it be support-layer only, case-method only, core, or rejected?

Use this final format:

```text
VERDICT:
KEEP / MODIFY / REJECT:
WHAT IT ADDS:
WHAT IT BREAKS:
SMALLEST SAFE FORM:
BIGGEST DRIFT RISK:
CORE / SUPPORT / CASE-ONLY:
```
