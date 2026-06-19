# Use TRACE on One Problem v0.1

Status: cold-reader use sheet. Not canon. Not validation. Not advice that replaces domain expertise. Use this to try TRACE once on a real or fictional problem.

```trace
Use_TRACE_On_One_Problem_v0_1 :=
  one_problem
  + one_pass
  + visible_next_action
  + demoter
  - full_theory
  - validation
```

## Rule

Do not begin by understanding all of TRACE.

Begin with one problem.

```trace
start :=
  one_problem
  + one_pass
  + one_next_action
```

## Step 1 — Name the situation

Write the situation in one sentence.

```trace
situation :=
  what_is_happening_now?
```

Plain prompt:

> What is happening, in ordinary language?

Avoid diagnosis at this stage.

## Step 2 — Name the affected subject

```trace
affected_subject :=
  person
  OR group
  OR animal
  OR ecology
  OR future_subject
  OR system_dependant_on_repair
```

Plain prompt:

> Who or what might be carrying the harm, cost, risk, or loss?

If the answer is “nobody”, check again.

## Step 3 — Name the possible harm or loss

```trace
harm_or_loss :=
  bodily_harm
  OR agency_loss
  OR time_loss
  OR repair_loss
  OR dignity_loss
  OR future_space_loss
  OR ecological_cost
```

Plain prompt:

> What could get worse if this continues?

## Step 4 — Find the clock

```trace
clock :=
  what_gets_harder_with_time?
```

Plain prompt:

> What becomes harder, more expensive, more irreversible, or less correctable if delayed?

Examples:

```trace
clock_examples :=
  health_deteriorates
  + appeal_window_closes
  + evidence_disappears
  + debt_accumulates
  + trust_breaks
  + ecology_degrades
  + subject_loses_energy
```

## Step 5 — Find the hidden bill

```trace
hidden_bill :=
  benefit_here
  + cost_elsewhere
  + time_gap
  + responsibility_gap
```

Plain prompt:

> Is the visible benefit being bought by hidden cost somewhere else?

Ask:

```trace
hidden_bill_questions :=
  who_benefits_now?
  + who_pays_later?
  + what_work_is_unseen?
  + what_repair_is_unfunded?
  + what_body_or ecology_absorbs_cost?
```

## Step 6 — Find the option-space

```trace
option_space :=
  available_paths
  - impossible_paths
  - blocked_paths
  - unseen_paths
```

Plain prompt:

> What choices does the affected subject actually have?

Then ask:

```trace
option_shaping :=
  who_controls_options?
  + who_controls_defaults?
  + who_controls_information?
  + who_controls_exit?
```

## Step 7 — Find the carrier

A repair path needs a carrier: a person, process, institution, tool, record, rule, or practical route that can actually carry correction.

```trace
repair_carrier :=
  person_or_process_that_can_change_the_path
```

Plain prompt:

> Who or what can actually make this better in time?

If no carrier exists, do not pretend the safeguard is real.

```trace
false_safeguard :=
  protection_claim
  + no_carrier
```

## Step 8 — Check local facts before escalation

```trace
local_check :=
  last_touch
  + local_record
  + local_spare_or_workaround
  + safe_confirmation
```

Plain prompt:

> What can be checked locally before escalating or theorising?

This protects against respectable wrongness: sounding careful while missing the obvious nearby carrier.

## Step 9 — Decide the next action

```trace
next_action :=
  preserve_evidence
  OR ask_specific_person
  OR check_local_record
  OR restore_safe_state
  OR escalate_to_correct_carrier
  OR pause_because_information_missing
```

Plain prompt:

> What is the smallest action that improves truth, safety, repair, or timing?

## Step 10 — Demote your own read

```trace
demoter :=
  what_would_show_this_read_is_wrong?
```

Plain prompt:

> What fact would make this interpretation fail?

If there is no possible demoter, the analysis is probably too self-protective.

## One-page template

Copy this:

```trace
TRACE_one_problem :=
  situation:
  affected_subject:
  possible_harm_or_loss:
  clock:
  hidden_bill:
  option_space:
  repair_carrier:
  local_check:
  next_action:
  demoter:
```

Plain version:

1. What is happening?
2. Who or what is affected?
3. What could be harmed or lost?
4. What gets worse with time?
5. Where might the hidden bill be?
6. What choices really exist?
7. Who or what can carry repair?
8. What can be checked locally?
9. What should happen next?
10. What would prove this reading wrong?

## Success test

```trace
success :=
  structure_clearer
  + next_action_better
  + false_confidence_lower
```

TRACE helped if it made the situation more answerable.

TRACE failed if it only made the description sound clever.

```trace
failure :=
  elegant_language
  + no_better_action
```

End.
