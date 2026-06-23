# TRACE Temporal Clock Index Candidate v0.1

Status: support-layer candidate. Not v0.12. Not validation. Not a full temporal algebra.

## Purpose

v0.11 has time as pressure: hardening clocks, review clocks, delay harm, action windows, and RAPID_TRIAGE expiry.

This note tests whether TRACE needs a compact **Temporal Clock Index** to stop time from remaining implicit inside cases.

```trace
problem :=
  clocks_exist
  ∧ clocks_conflict
  ∧ slow_clock_can_launder_fast_clock
  ∧ fast_clock_can_launder_review
```

Core rule retained:

```trace
missing_information ≠ permission_not_to_decide
```

New compression:

```trace
clock_without_owner_or_hardening_effect := weak_clock_claim
```

---

## Temporal Clock Index

For any live decision route, list active clocks explicitly.

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

A clock is not just a deadline. It is a claim about what changes if time passes.

```trace
deadline ≠ clock
clock := deadline + hardening_effect + affected_scope + controller
```

---

## Required clock families

A TRACE route should ask whether these clocks are active:

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

Definitions:

```trace
harm_hardening_clock := time_until harm becomes irreversible_or_harder_to_repair

support_clock := time_until lack_of_support creates secondary harm

evidence_decay_clock := time_until truth becomes less replayable

contest_clock := time_until affected_scope loses practical ability to challenge

review_clock := time_until provisional action must be reviewed / escalated / degraded

remediation_clock := time_until repair delay becomes new harm

accountability_clock := time_until accountability becomes impossible_or_performative

recurrence_risk_clock := time_until similar harm may recur elsewhere

communication_trust_clock := time_until silence / opacity becomes institutional injury

machine_speed_clock := time_until automated action hardens faster than human review
```

---

## Clock interaction rules

### Slow-clock laundering

```trace
slow_clock_laundering :=
  slow_truth_or_justice_clock
  used_to_pause_fast_support_or_safety_clock
```

Examples:

```trace
inquiry_pending ≠ support_pause
criminal_investigation_pending ≠ housing_pause
culpability_unresolved ≠ safety_triage_pause
```

### Fast-clock laundering

```trace
fast_clock_laundering :=
  emergency_clock
  used_to_bypass_review_forever
```

Guard:

```trace
fast_action_now
→ review_clock_required
→ escalation_or_degradation_required
```

### Clock ownership

```trace
controller(c) must_be_named
```

If the actor benefiting from delay controls the clock:

```trace
capture_risk ↑
```

### Clock conflict

```trace
ClockConflict(c1,c2) :=
  action_required_by(c1)
  conflicts_with_integrity_required_by(c2)
```

A conflict is not solved by hiding either clock.

```trace
visible_conflict ≠ failure
hidden_clock := laundering_risk
```

---

## Relationship to v0.11

The Temporal Clock Index does not add new states.

It strengthens existing v0.11 mechanisms:

```trace
TransitionClaim.clock_effect
UNRESOLVED_to_delay_laundering
RAPID_TRIAGE_review_clock
HardeningClaim_adequate_for_action_window
staged_TransitionClaim_candidate
```

It makes one field explicit:

```trace
clock_effect := TemporalClock(c).hardening_effect
```

---

## Grenfell pressure example

Active clocks after Grenfell:

```trace
Grenfell_clocks :=
  survivor_support_clock
  + housing_clock
  + evidence_preservation_clock
  + building_safety_clock
  + public_truth_clock
  + criminal_justice_clock
  + institutional_reform_clock
```

Risk:

```trace
public_inquiry_clock
used_to_pause:
  survivor_support_clock
  ∨ building_safety_clock
  ∨ remediation_clock
→ slow_clock_laundering
```

Middle-out response:

```trace
act_fast_on_support_and_safety
while_truth_process_runs
and_keep_actions_reviewable
```

---

## Dirty action receipt integration

For RAPID_TRIAGE, a full TemporalClock record may be too heavy.

Minimum clock receipt:

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

Full TemporalClock(c) must be completed during FULL_TRACE.

```trace
RAPID_clock_receipt now
FULL_clock_index later
```

---

## Anti-laundering tests

Ask these of any clock claim:

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

If these cannot be answered:

```trace
clock_claim := weak_or_unresolved
```

If the actor benefits from non-answer:

```trace
weak_clock_claim + actor_benefits_from_delay
→ delay_laundering_signal
```

---

## Limits

This note does not solve:

```trace
clock_priority_ordering
cross_scope_comparison
hardening_estimator_authority
field_truth_verification
machine_speed_enforcement
```

It only makes time explicit enough to prevent hidden clock substitution.

---

## Compression

```trace
TemporalClockIndex_v0_1 :=
  list_active_clocks
  + name_controller
  + name_hardening_effect
  + name_delay_harm
  + name_interim_action
  + name_review_clock
  + expose_clock_laundering
```

Current status:

```trace
candidate_support_layer
not_v0_12
use_in_cases_before_kernel_promotion
```
