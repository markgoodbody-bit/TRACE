# TRACE Temporal Clock Index — Claude Review Prompt

Status: external review prompt. Diagnostic only. Not validation.

## Receiver identity header

Please complete before answering. If unknown, write UNKNOWN.

```text
MODEL_ID:
PROVIDER:
INTERFACE:
DATE_TIME:
MEMORY_STATUS:
PRIOR_TRACE_CONTEXT:
TOOLS_AVAILABLE:
SELF_DESCRIPTION_CONFIDENCE:
LIMITS_NOTICE:
RECEIVER_ROLE_FOR_THIS_TASK: hostile review of Temporal Clock Index candidate, not agreement
CLAIM_STATUS_ACKNOWLEDGEMENT: This is a support-layer candidate, not v0.12, not validation, not a full temporal algebra.
```

---

## Task

Hostile-review the following TRACE Temporal Clock Index candidate.

Do not praise.
Do not repair unless asked.
Focus on whether this adds real decision/reconstruction value or merely adds complexity.

Ask:

```trace
Does this improve v0.11?
Does it prevent clock laundering?
Does it create paperwork paralysis?
Does it belong in core, support layer, or case method only?
What breaks first?
```

---

## Candidate under review

```trace
TemporalClock(c) := Claim({
  clock_name,
  trigger,
  affected_scope,
  controller,
  start_time_or_event,
  action_window,
  hardening_effect,
  evidence_decay_effect,
  delay_harm,
  interim_action_required,
  review_clock,
  contest_edge,
  capture_risk
})
```

A clock is not just a deadline.

```trace
deadline ≠ clock
clock := deadline + hardening_effect + affected_scope + controller
```

Required clock families:

```trace
clock_families :=
  harm_hardening_clock
  + survivor_support_clock
  + evidence_decay_clock
  + contest_clock
  + review_clock
  + remediation_clock
  + accountability_clock
  + recurrence_risk_clock
  + communication_trust_clock
  + machine_speed_clock_if_applicable
```

Clock laundering patterns:

```trace
slow_clock_laundering :=
  slow_truth_or_justice_clock
  used_to_pause_fast_support_or_safety_clock

fast_clock_laundering :=
  emergency_clock
  used_to_bypass_review_forever
```

Clock conflict:

```trace
ClockConflict(c1,c2) :=
  action_required_by(c1)
  conflicts_with_integrity_required_by(c2)
```

RAPID minimum:

```trace
RAPID_clock_receipt := {
  trigger,
  named_clock,
  affected_scope,
  expected_hardening_effect,
  action_taken,
  review_clock,
  escalation_owner
}
```

Anti-laundering tests:

```trace
what_hardens_if_we_wait?
who_is_harmed_by_delay?
who_benefits_from_delay?
who_controls_the_clock?
what_evidence_decays?
what_interim_action_is_required?
when_must_review_occur?
who_can_contest_the_clock?
what_happens_if_review_clock_expires?
```

Limits admitted:

```trace
clock_priority_ordering
cross_scope_comparison
hardening_estimator_authority
field_truth_verification
machine_speed_enforcement
```

---

## Required output

```text
VERDICT:
WHAT IT ADDS:
WHAT IT BREAKS:
DRIFT RISK:
CORE / SUPPORT / CASE-ONLY:
MINIMAL PATCH, IF ANY:
SHOULD THIS BE TESTED ON GRENFELL-LIKE CASES BEFORE PROMOTION? yes/no
```

Also answer specifically:

```trace
Does TemporalClock(c) add decision advantage over v0.11 TransitionClaim.clock_effect?
Does RAPID_clock_receipt solve staged TransitionClaim pressure or create a loophole?
Does slow_clock_laundering / fast_clock_laundering capture real patterns?
What is the smallest safe version of this candidate?
```
