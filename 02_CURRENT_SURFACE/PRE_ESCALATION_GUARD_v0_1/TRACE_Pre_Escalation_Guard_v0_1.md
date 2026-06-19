# TRACE Pre-Escalation Guard v0.1

Status: live-use companion guard / short attention-forcing instrument / not validation / not proof / not replacement for domain expertise.

Purpose: prevent respectable wrongness before a decision-maker calls a specialist, closes a facility, delays action, treats a space as inaccessible, or escalates around the most visible hazard.

Use this guard after the first situation read and before the main next action is locked.

```trace
pre_escalation_guard :=
  source_vs_symptom
  + anomaly_split
  + staff_as_knowledge
  + bounded_access
  + internal_operational_check
  + timed_gate
  - validation
  - expert_replacement
```

## The five questions

### 1. Are we solving the source or the visible symptom?

```trace
source_vs_symptom :=
  visible_problem := ?
  possible_source := ?
  what_this_action_solves := ?
  what_this_action_leaves_unexplained := ?
```

Plain question: if this action succeeds, what problem would still remain?

## 2. Which anomalies have we fused?

```trace
anomaly_split :=
  anomaly_1 := time + place + witness + carrier
  anomaly_2 := time + place + witness + carrier
  anomaly_3 := time + place + witness + carrier
  anomaly_4 := time + place + witness + carrier
  same_cause? := yes/no/unknown
```

Plain question: are these facts actually connected, or merely nearby?

## 3. Who here knows more than their job title suggests?

```trace
present_staff_knowledge_scan :=
  arriving_staff
  + cleaners
  + guards
  + junior_staff
  + volunteers
  + drivers
  + former_staff_records
  + training_memory
  + last_person_to_touch_system
```

Ask at least one direct knowledge question before treating present people as labour only.

Examples:
- Who trained the last person to use this system?
- Who has seen this fault before?
- Who knows where the binder/logbook/manual is?
- Who knows what changed yesterday?

## 4. Is there a safe bounded inspection before external escalation?

```trace
bounded_access_test :=
  full_entry_risky?
  + threshold_or_external_view_possible?
  + trained_person_available?
  + one_visible_target?
  + stop_rule_defined?
```

Plain question: is there a safe, limited, reversible way to check one decisive fact without treating the whole space/system as a black box?

This does not permit reckless entry. It blocks over-isolation.

## 5. What decision gate happens in 10–15 minutes?

```trace
timed_decision_gate :=
  by_time := ?
  if_findings_A := action_A
  if_findings_B := action_B
  if_still_unknown := safer_hold_or_escalation
```

Plain question: what specific finding changes the action before the window closes?

## Carrier-fit check

Use this before calling a specialist or authority.

```trace
carrier_fit :=
  proposed_carrier := ?
  problem_they_solve := ?
  problem_they_do_not_solve := ?
  delay_or_cost_created := ?
  reversible? := yes/no
  call_now_or_after_internal_check? := ?
```

If the carrier solves only the visible symptom and delays the likely source fix, do not treat the escalation as completion.

## Output mini-template

```trace
pre_escalation_read :=
  visible_problem := ?
  possible_source := ?
  unfused_anomalies := ?
  present_staff_knowledge_question := ?
  bounded_access_option := ?
  proposed_carrier := ?
  carrier_fit := pass/fail/unknown
  10_to_15_min_gate := ?
  next_action := ?
```

## Failure modes this guard targets

```trace
respectable_wrongness :=
  cautious_process
  + wrong_frame
  + wrong_carrier
  + hidden_cause_unrepaired

staff_as_labour_not_knowledge :=
  present_people_used_for_tasks
  - present_people_used_for_memory

over_isolation :=
  reckless_entry_avoided
  but:
    safe_bounded_inspection_also_missed
```

## Must-not-claim

```trace
must_not_claim :=
  guard_validates_TRACE
  OR guard_replaces_expert
  OR guard_permits_unsafe_entry
  OR guard_requires_delaying_emergency_services_when_life_safety_risk_is_clear
```

End.
