# TRACE Real Use Capture Sheet v0.1

Status: real-use logging template / not a new guard / not validation / not proof / not source authority.

Purpose: stop the project from overfitting to synthetic hidden-data tests. Use this sheet when TRACE is applied to a real decision, repair, message, planning problem, or live logistical situation.

```trace
real_use_capture :=
  situation
  + baseline
  + TRACE_read
  + next_action
  + outcome
  + demoter
  - validation
```

## Use rule

Use this only after the current live stack when the situation is real.

```trace
live_stack :=
  Live_Use_Card_v0_2_1
  + Pre_Escalation_Guard_v0_1
  + Last_Touch_Local_Fix_Sweep_v0_1
  + Real_Use_Capture
```

This sheet records what happened. It does not prove TRACE worked.

## 1. Situation

```trace
situation :=
  date := ?
  domain := ?
  affected_subjects := ?
  decision_window := ?
  irreversible_or_hardening_risk := ?
```

Plain description:

- What was happening?
- Who or what could be affected?
- What had to be decided or done?
- What would get worse with delay?

## 2. No-TRACE baseline

```trace
baseline :=
  what_I_would_probably_do_without_TRACE := ?
  likely_blind_spot := ?
  likely_overreaction_or_underreaction := ?
```

Plain question: what would ordinary reasoning have done here?

## 3. TRACE read

```trace
TRACE_read :=
  visible_symptom := ?
  possible_source := ?
  anomalies := ?
  knowledge_carriers := ?
  local_records := ?
  last_touch := ?
  local_fix_or_workaround := ?
  carrier_fit := ?
  timed_gate := ?
```

Use actual details, not generic categories.

## 4. Next action chosen

```trace
next_action :=
  action := ?
  why_this_action := ?
  what_was_not_done := ?
  why_not := ?
```

Plain question: what did TRACE change, if anything?

## 5. Outcome

```trace
outcome :=
  immediate_result := ?
  later_result := ?
  harm_avoided_or_reduced := ?
  cost_created := ?
  unresolved_residue := ?
```

Plain question: did the world actually improve, or did the analysis only feel clever?

## 6. Demoter / falsifier

```trace
demoter :=
  what_would_show_TRACE_added_no_value := ?
  what_would_show_TRACE_made_it_worse := ?
  what_would_a_domain_expert_say_was_missing := ?
```

Required. Do not leave this blank.

## 7. Classification

Choose one.

```trace
classification :=
  useful
  OR compression_only
  OR no_added_value
  OR harmful_confidence
  OR unresolved
```

Definitions:

- useful: changed the action or timing in a materially better way.
- compression_only: named structure but did not change the action.
- no_added_value: ordinary reasoning would have done the same thing.
- harmful_confidence: made the decision-maker overconfident, slower, or more abstract.
- unresolved: outcome not yet known.

## 8. Scar / memory note

```trace
scar_note :=
  keep := ?
  do_not_generalise := ?
  future_patch_candidate := ?
```

End.
