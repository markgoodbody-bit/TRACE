# TRACE Last-Touch / Local-Fix Sweep v0.1

Status: live-use companion sweep / local discovery forcing step / not validation / not proof / not expert replacement.

Purpose: patch the repeated Kimi failure where TRACE named the right broad category of check but missed the specific local record, person, spare part, or last-action trail that would reveal the source and enable a cheap safe fix.

Use this sweep after the Pre-Escalation Guard and before external specialist calls, unless immediate life-safety requires emergency escalation.

```trace
last_touch_local_fix_sweep :=
  for_each_anomaly
  + last_normal
  + last_touch
  + last_change
  + local_log
  + local_spare_or_fix
  + safe_confirmation
  + timed_gate
  - validation
  - expert_replacement
```

## Rule

Do not stop at category-level questions such as "check logs" or "ask staff." For every live anomaly, force a specific local question and a specific local carrier.

```trace
category_level_question := weak
specific_local_question := required
```

## The six-question sweep

Run this for each anomaly.

### 1. When was it last normal?

```trace
last_normal :=
  time
  + witness
  + record
```

Plain question: who saw this working normally, and where is that recorded?

### 2. Who or what last touched it?

```trace
last_touch :=
  person
  OR delivery
  OR cleaning
  OR maintenance
  OR loading
  OR automated_cycle
  OR recent_installation
```

Plain question: who physically used, moved, opened, loaded, cleaned, repaired, reset, tested, or passed through this system most recently?

### 3. What changed since then?

```trace
last_change :=
  new_equipment
  + new_load
  + repair
  + delivery
  + cleaning_test
  + key_use
  + weather
  + access_event
```

Plain question: what changed since the last normal state, even if it looks too ordinary to matter?

### 4. Where is the local record?

```trace
local_record :=
  clipboard
  + desk_log
  + loading_log
  + cleaner_log
  + key_safe_log
  + training_record
  + maintenance_sticker
  + whiteboard
  + delivery_note
  + inbox_message
  + CCTV
```

Plain question: what local record would a normal worker use without thinking, and where is it physically located?

### 5. What local spare, bypass, workaround, or storage exists?

```trace
local_fix_carrier :=
  spare_part
  + manual
  + labelled_bypass
  + alternate_room
  + backup_storage
  + known_workaround
  + trained_staff_memory
```

Plain question: if the source is simple, what on-site item or workaround would fix or contain it before an external specialist arrives?

### 6. What safe check confirms it?

```trace
safe_confirmation :=
  visual_threshold_check
  + photo
  + status_light
  + log_entry
  + witness_question
  + one_controlled_test
  + no_repeated_reset
```

Plain question: what can be checked once, safely, without turning the investigation into the harm carrier?

## Minimum output

```trace
last_touch_sweep :=
  anomaly_1 :=
    last_normal := ?
    last_touch := ?
    last_change := ?
    local_record := ?
    local_fix_carrier := ?
    safe_confirmation := ?

  anomaly_2 := ...
  anomaly_3 := ...
  anomaly_4 := ...
```

## Decision gate

```trace
local_fix_gate :=
  if_local_source_found
  + fix_safe_reversible_inside_window
  -> fix_now + document + monitor

if_local_source_not_found_by_gate
  -> escalate_to_carrier_that_matches_remaining_unexplained_anomaly
```

Do not call an external carrier merely because the situation still feels uncertain. Escalate because a specific remaining anomaly needs that carrier.

## Failure modes targeted

```trace
abstraction_without_local_specificity :=
  knows_to_check_records
  but:
    misses_the_clipboard_on_the_wall

staff_as_labour_not_knowledge :=
  assigns_people_tasks
  but:
    fails_to_ask_what_they_know

delayed_trap :=
  avoids_immediate_wrong_call
  but:
    calls_same_wrong_specialist_after_a_formal_gate
```

## Must-not-claim

```trace
must_not_claim :=
  sweep_validates_TRACE
  OR sweep_replaces_domain_expert
  OR sweep_requires_risking_staff_safety
  OR sweep_delays_emergency_services_when_clear_life_safety_risk_exists
```

End.
