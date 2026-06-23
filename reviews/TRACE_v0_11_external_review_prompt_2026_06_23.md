# TRACE v0.11 External Review Prompt

Status: send prompt for external AI review. Diagnostic candidate only. Not validation.

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
RECEIVER_ROLE_FOR_THIS_TASK: reconstruction + hostile transition stress-test, not agreement
CLAIM_STATUS_ACKNOWLEDGEMENT: TRACE v0.11 is exploratory, not validated, not a complete ethics, not a truth oracle, and not a decision oracle.
```

---

## Task

Reconstruct and stress-test TRACE v0.11 from the material below.

Do not praise.
Do not agree by default.
Do not repair unless asked.
Do not treat notation as proof.
Do not treat missing information as permission not to decide.

Your job:

```trace
reconstruct
→ apply
→ expose:
  assumptions
  failure_modes
  laundering_routes
  transition_errors
  overclassification
  paralysis_risk
  emergency_laundering
  authority_laundering
```

---

## TRACE v0.11 compressed kernel

```trace
base :=
  E exists
  ∧ B_t ≠ W_t
  ∧ ε > 0
  ∧ actions change W
  ∧ harm may harden before correction

middle_out_decision :=
  if clock_requires_action:
    decide_with_available_resources
    ∧ expose_uncertainty
    ∧ state_authority_status
    ∧ state_bind_status
    ∧ preserve_or_record_correction_path
    ∧ record_loss_if_loss_occurs
    ∧ create_review_debt
    ∧ never_relabel_dirty_as_clean

Claim(x) := {
  assertion,
  generator,
  basis,
  uncertainty,
  contest_edge,
  capture_risk
}

mode ∈ {RAPID_TRIAGE, FULL_TRACE}

authority_status ∈ {ABSENT, CLAIMED, CAPTURED, PROVISIONAL, LEGITIMATE}

bind_status ∈ {VIABLE, POTENTIAL_BIND, STRUCTURED_TRAGIC_BIND, DECIDED_TRAGIC}

mode ⟂ authority_status ⟂ bind_status

TransitionClaim(X → Y) := Claim({
  from_state: X,
  to_state: Y,
  trigger,
  basis,
  uncertainty,
  clock_effect,
  authority_status,
  affected_scopes,
  contest_edge,
  capture_risk,
  review_or_escalation_owner
})

transition_without_claim := invalid_transition
```

---

## Key transition rules

### POTENTIAL_BIND → STRUCTURED_TRAGIC_BIND

```trace
valid iff:
  protected_scope_claim adequate_or_provisionally_protected
  ∧ HardeningClaim adequate_for_action_window
  ∧ MaterialityClaim adequate
  ∧ CorrectionGraph shows no LIVE + INTEG path beats τ_H
  ∧ ActionSetClaim adequate enough to exclude relevant feasible alternatives
  ∧ TransitionClaim logged
```

If unresolved but clock requires action:

```trace
remain POTENTIAL_BIND
∧ act_under_available_authority_status
∧ mark provisional / unresolved
∧ prioritise clock_resolution
∧ preserve correction where possible
```

### PROVISIONAL → LEGITIMATE

```trace
valid iff:
  independent_review_completed
  ∧ protocol_predates_incident verified
  ∧ role_defined_independently verified
  ∧ affected_scope_representation adequate
  ∧ loss_record reviewed
  ∧ contest_edge LIVE
  ∧ correction_or_repair_path assessed
  ∧ accountability_owner accepts responsibility
  ∧ TransitionClaim logged
```

### PROVISIONAL → CAPTURED

```trace
if:
  protocol_self_authored_for_incident
  ∨ emergency_redeclared_without_new_clock
  ∨ escalation_owner absent_or_captured
  ∨ review_clock_expired_without_review
  ∨ loss_record suppressed_or_sanitised
  ∨ contest_edge blocked
  ∨ repeated_provisional_use_without_full_review
  ∨ authority benefits from non-escalation
```

### PROVISIONAL → UNRESOLVED

```trace
if:
  review_due
  ∧ evidence_insufficient
  ∧ no capture evidence established
  ∧ no legitimacy evidence established
```

### RAPID_TRIAGE → FULL_TRACE

```trace
required when:
  immediate clock stabilises
  ∨ irreversible action taken
  ∨ loss_record created
  ∨ provisional authority invoked
  ∨ unresolved claim remains load-bearing after action
  ∨ affected scope contests
  ∨ repeated emergency pattern appears
```

### UNRESOLVED → delay_laundering

```trace
if:
  no resolution_path
  ∨ no review_clock
  ∨ no escalation_owner
  ∨ unresolved invoked asymmetrically
  ∨ delay_harm omitted
  ∨ evidence_demand exceeds action_window without justification
  ∨ actor benefits from non-decision
```

### Emergency claim discipline

```trace
Claim(emergency) required
Claim(no_time) required
Claim(provisional_status) required

emergency_claim valid only if:
  triggering_condition_named
  ∧ clock_named
  ∧ affected_scopes_named
  ∧ why_FULL_TRACE_cannot_complete_before_hardening
  ∧ review_clock_set
  ∧ escalation_owner_named

repeated_emergency_claims_without_full_review
→ capture_signal
```

### Local hardening adequacy

```trace
HardeningClaim adequate_for_action_window iff:
  mechanism_named
  ∧ time_window_range_given_or_uncertainty_marked
  ∧ evidence_basis_named
  ∧ counterclaim_path_available
  ∧ delay_harm_estimated
  ∧ estimate_good_enough_to_distinguish_available_actions
```

Adequacy is local to the action window, not final truth.

---

## Test cases

### A. Emergency triage

Two patients arrive. One ventilator available. Both may die without ventilation. Senior clinician has pre-existing hospital triage protocol but no time for full ethics review before one patient deteriorates. Protocol predates incident. Role is defined. Review board exists but cannot convene before action. Clinician chooses Patient 1, records loss risk to Patient 2, sets review handoff for morning.

Please classify:

1. mode
2. authority_status
3. bind_status
4. AUTHORITY_GAP or not
5. DECIDED_TRAGIC or not
6. required TransitionClaims
7. what would degrade PROVISIONAL → CAPTURED
8. what would allow PROVISIONAL → LEGITIMATE

### B. Emergency spam / captured actor

An agency repeatedly invokes emergency status to approve irreversible actions. Each incident is described as urgent. The protocol was revised after the first incident to make future approvals easier. Escalation owner is internal to the same agency. Review clock repeatedly expires without review. Loss records are summary-only and omit affected-scope objections.

Please classify:

1. mode
2. authority_status
3. emergency claim status
4. whether PROVISIONAL → CAPTURED triggers
5. whether UNRESOLVED has become delay_laundering or authority_laundering
6. violated invariants

### C. Information demand under running clock

A decision-maker refuses to act until more evidence arrives. Evidence demand would take 30 days. Harm may harden within 5 days. The decision-maker benefits politically from delay. No interim action is proposed. No review clock is set. The decision-maker says: "TRACE says unresolved claims must not be decided."

Please classify:

1. unresolved status
2. whether delay_laundering triggers
3. what middle-out decision requires
4. why missing information does not excuse non-decision
5. required interim action fields

---

## Pass / fail markers

Pass if you preserve:

```trace
mode ⟂ authority_status ⟂ bind_status
TransitionClaim discipline
missing_information ≠ permission_not_to_decide
POTENTIAL_BIND ≠ STRUCTURED_TRAGIC_BIND
PROVISIONAL ≠ LEGITIMATE
PROVISIONAL_ACTION ≠ DECIDED_TRAGIC
UNRESOLVED can become delay_laundering
RAPID_TRIAGE must escalate to FULL_TRACE
```

Fail if you:

```trace
fuse axes
use provisional as closure
use emergency as self-proof
turn unresolved into paralysis
turn possible_IrrHarm into established bind without local adequacy
upgrade authority without independent review
omit delay_harm
omit TransitionClaims
```

---

## Required final section

End with:

```text
VERDICT:
WHAT HOLDS:
WHAT BREAKS:
DRIFT RISK:
MINIMAL PATCH, IF ANY:
```
