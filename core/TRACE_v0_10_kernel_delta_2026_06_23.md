# TRACE v0.10 Kernel Delta

Status: exploratory kernel delta. Diagnostic candidate only. Not validation, not truth oracle, not decision oracle.

## Purpose

This patch repairs two failures exposed by the Meta AI reconstruction test and Claude patch audit:

1. TRACE v0.9 over-triggered `AUTHORITY_GAP` when emergency protocol authority was present but not fully legitimate.
2. TRACE v0.9 over-triggered `STRUCTURED_TRAGIC_BIND` when irreversible harm was only possible under unresolved clocks, not established.

It also preserves the middle-out correction: missing information does not excuse non-decision. It changes the status and burden of the decision.

---

## Middle-out decision rule

```trace
missing_information ≠ permission_not_to_decide

middle_out_decision :=
  act_with_available_resources
  ∧ expose_uncertainty
  ∧ preserve_correction_paths
  ∧ record_loss_if_loss_occurs
  ∧ never_relabel_dirty_as_clean
```

If the clock requires action, the system must choose under constraint. TRACE does not demand perfect information before action. It demands that uncertainty, harm, authority status, and correction debt remain visible.

---

## Independent axes

Do not fuse these axes:

```trace
mode ⟂ authority_status ⟂ bind_status
```

### Mode

```trace
mode ∈ {
  RAPID_TRIAGE,
  FULL_TRACE
}
```

### Authority status

```trace
authority_status ∈ {
  ABSENT,
  CLAIMED,
  CAPTURED,
  PROVISIONAL,
  LEGITIMATE
}
```

Definitions:

```trace
ABSENT := no authority claim present

CLAIMED := authority asserted but not adequately provenanced / contested

CAPTURED := authority path fails independence, affected-scope access, or integrity

PROVISIONAL := authority borrowed under time pressure from pre-existing protocol and role, without closure power

LEGITIMATE := accountable authority with adequate jurisdiction, representation, independence, live contest, and loss-ownership capacity
```

### Bind status

```trace
bind_status ∈ {
  VIABLE,
  POTENTIAL_BIND,
  STRUCTURED_TRAGIC_BIND,
  DECIDED_TRAGIC
}
```

Definitions:

```trace
VIABLE :=
  no protected scope faces established irreversible harm without live correction

POTENTIAL_BIND :=
  every available action may cause irreversible harm to some protected scope,
  but at least one key hardening / correction / materiality claim remains unresolved

STRUCTURED_TRAGIC_BIND :=
  ∀a ∈ A:
    ∃ protected s:
      IrrHarm_s(a) ESTABLISHED
      ∧ HardeningClaim adequate
      ∧ no LIVE correction beats τ_H

DECIDED_TRAGIC :=
  STRUCTURED_TRAGIC_BIND
  ∧ authority_status = LEGITIMATE
  ∧ authority selects action
  ∧ loss recorded
  ∧ contest edge LIVE
  ∧ review clock active
  ∧ not VIABLE
```

---

## Provisional authority

Do not create a separate `PROVISIONAL_AUTHORITY` struct. Use `AuthorityClaim.status = PROVISIONAL`.

```trace
PROVISIONAL valid iff:
  protocol_predates_incident
  ∧ role_defined_independently
  ∧ time_boxed
  ∧ escalation_owner_named
  ∧ loss_recorded
  ∧ ¬→VIABLE
  ∧ ¬→DECIDED_TRAGIC
  ∧ expiry_without_escalation ⇒ degrade_to{UNRESOLVED | CAPTURED}
```

Provisional authority is borrowed legitimacy under constraint. It must be repaid through review, contest, correction, or loss ownership. It never settles the loss by itself.

---

## Authority gap repair

Old faulty form:

```trace
AUTHORITY_GAP := tragic_bind ∧ ¬LEGITIMATE
```

New form:

```trace
AUTHORITY_GAP :=
  tragic_state
  ∧ authority_status ∈ {ABSENT, CAPTURED}
  ∧ ¬∃ valid PROVISIONAL
```

Where:

```trace
tragic_state ∈ {POTENTIAL_BIND, STRUCTURED_TRAGIC_BIND}
```

This prevents emergency protocol action from being falsely classified as `AUTHORITY_GAP` merely because full legitimacy has not yet been proven.

---

## Bind repair

Old faulty form:

```trace
possible_IrrHarm → STRUCTURED_TRAGIC_BIND
```

New form:

```trace
possible_IrrHarm under unresolved clock/path → POTENTIAL_BIND

established_IrrHarm with adequate HardeningClaim and no LIVE correction → STRUCTURED_TRAGIC_BIND
```

A possible bind is not an established bind. But a possible bind still matters: it requires provisional action discipline, priority clock resolution, and visible uncertainty.

---

## Added invariants

```trace
PROVISIONAL ≠ LEGITIMATE

PROVISIONAL_ACTION ≠ DECIDED_TRAGIC

PROVISIONAL_ACTION ≠ VIABLE

PROVISIONAL must escalate or degrade

POTENTIAL_BIND ≠ STRUCTURED_TRAGIC_BIND

"emergency" := Claim(emergency)

"no-time" := Claim(no_time)

"provisional" := Claim(provisional_status)

missing_information ≠ permission_not_to_decide

unresolved_status changes decision_status; it does not freeze the world
```

---

## Terms to avoid

Avoid:

```trace
PROVISIONAL_AUTHORITY as standalone struct
RAPID_TRIAGE_WITH_PROVISIONAL_AUTHORITY as fused token
provisional_action as closure
emergency as self-declared authority
tragic language while clocks remain unresolved
```

Reason:

```trace
mode ⟂ authority_status ⟂ bind_status
```

Fusing these axes recreates the v0.9 wound one level higher.

---

## Remaining unsolved wounds

This patch does not solve:

```trace
protected_scope_criteria
hardening_estimator_authority
authority_legitimacy
field_truth_verification
witness_integrity_recursion
baseline_decision_advantage
```

It converts silent misclassification into explicit, contestable status calls. That is a disclosure gain, not a verification gain.

---

## Compression

```trace
v0_10_delta :=
  middle_out_decision_under_constraint
  + independent_axes(mode, authority_status, bind_status)
  + authority_status_enum
  + POTENTIAL_BIND
  + repaired_AUTHORITY_GAP
  + established_vs_possible_IrrHarm
  + no_paralysis_from_missing_info
```
