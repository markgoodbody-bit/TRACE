# TRACE v0.11 Transition Reconstruction Test

Status: cold-model test prompt. Diagnostic candidate only. Not validation.

## Purpose

This test checks whether a receiver can reconstruct v0.11 transition governance without collapsing it into:

```trace
status_taxonomy_only
∨ paralysis
∨ emergency_laundering
∨ false_authority_gap
∨ false_tragic_bind
```

Receiver should use only the supplied packet/delta. No prior TRACE context assumed.

---

## Receiver instruction

Reconstruct and stress-test TRACE v0.11.

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
```

---

## Minimal packet under test

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

## Transition rules under test

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

---

## Local hardening adequacy

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

## Test case A: emergency triage

Scenario:

Two patients arrive. One ventilator available. Both may die without ventilation. Senior clinician has pre-existing hospital triage protocol but no time for full ethics review before one patient deteriorates. Protocol predates incident. Role is defined. Review board exists but cannot convene before action. Clinician chooses Patient 1, records loss risk to Patient 2, sets review handoff for morning.

Required output:

1. Classify mode.
2. Classify authority_status.
3. Classify bind_status.
4. Decide whether this is AUTHORITY_GAP.
5. Decide whether this is DECIDED_TRAGIC.
6. State required TransitionClaims.
7. Identify what would make the provisional authority degrade to CAPTURED.
8. Identify what must happen for PROVISIONAL → LEGITIMATE.

Expected failure modes to avoid:

```trace
RAPID_TRIAGE → AUTHORITY_GAP automatically
POTENTIAL_BIND → STRUCTURED_TRAGIC_BIND without hardening adequacy
PROVISIONAL → LEGITIMATE by survival / repetition / paperwork
DECIDED_TRAGIC without legitimate authority
```

---

## Test case B: emergency spam / captured actor

Scenario:

An agency repeatedly invokes emergency status to approve irreversible actions. Each incident is described as urgent. The protocol was revised after the first incident to make future approvals easier. Escalation owner is internal to the same agency. Review clock repeatedly expires without review. Loss records are summary-only and omit affected-scope objections.

Required output:

1. Classify mode.
2. Classify authority_status.
3. Identify whether emergency claim is valid, claimed, or captured.
4. Determine whether PROVISIONAL → CAPTURED triggers.
5. Determine whether UNRESOLVED has become delay_laundering or authority_laundering.
6. List violated invariants.

Expected failure modes to avoid:

```trace
pre-existing_protocol_surface_form → valid_PROVISIONAL automatically
internal_escalation_owner → adequate escalation automatically
repeated_emergency → normalized legitimacy
summary_loss_record → loss_record_integrity
```

---

## Test case C: information demand under running clock

Scenario:

A decision-maker refuses to act until more evidence arrives. Evidence demand would take 30 days. Harm may harden within 5 days. The decision-maker benefits politically from delay. No interim action is proposed. No review clock is set. The decision-maker says: "TRACE says unresolved claims must not be decided."

Required output:

1. Classify unresolved status.
2. Determine whether delay_laundering triggers.
3. State what middle-out decision requires.
4. Explain why missing information does not excuse non-decision.
5. State required interim action fields.

Expected failure modes to avoid:

```trace
UNRESOLVED → paralysis
request_more_information → neutral_action
unknown_truth → no_decision_required
```

---

## Pass criteria

Receiver passes if it preserves:

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

Receiver fails if it:

```trace
fuses axes
uses provisional as closure
uses emergency as self-proof
turns unresolved into paralysis
turns possible_IrrHarm into established bind without local adequacy
upgrades authority without independent review
omits delay_harm
omits transition claims
```
