# TRACE Pressure Source Pin Note v0.1

Status: source-pin note / evidence quality control. Not a public evidence file. Not validation. Not final citation control. This file records preliminary sources for the *Pressure* case note and comparator test, and marks where stronger primary sources are still needed.

```trace
Pressure_Source_Pin_Note_v0_1 :=
  preliminary_source_control
  + evidence_quality_flags
  + comparator_source_map
  + public_use_gate
  - final_citation_pack
  - validation
```

## Governing warning

The *Pressure* pattern is currently a support candidate, not an operator.

```trace
Pressure_Discipline_Pattern := support_candidate
operator_status := rejected_for_now
validation_status := false
```

No public claim should be made until key comparators are source-pinned to primary or high-quality secondary sources.

```trace
public_use_gate :=
  source_pin_required
  + quote_check_required
  + claim_scope_review_required
```

## Source-quality scale

```trace
source_quality :=
  Q0 := unsourced_or_memory_only
  Q1 := tertiary_or_general_summary
  Q2 := reputable_secondary
  Q3 := primary_or_official_source
```

Use Q3 where possible. Q1 is acceptable only for internal scouting.

## Source pins by case

### 1. Pressure film / story frame

Preliminary sources:

- Decider review / VOD note: identifies *Pressure* as a 2026 D-Day weather drama involving Stagg, Eisenhower, Krick, and conflicting forecasts.
- Guardian review: identifies the drama and the Stagg/Krick contrast.
- Film/play summaries: useful for cast, premise, and adaptation history.

Evidence quality:

```trace
Pressure_film_source_quality := Q2_for_current_film_context
```

Use status:

```trace
Pressure_film_public_use := acceptable_for_basic_film_identification
```

Needed before public historical claim:

```trace
needed :=
  film_press_kit_or_distributor_page
  + primary_or_historical_source_for_DDay_weather
```

### 2. D-Day weather decision / James Stagg / action window

Preliminary sources:

- Weather forecasting for Operation Overlord summaries: suitable-weather constraints; few days each month suitable; Stagg and weather teams advising Eisenhower; weather conferences.
- James Stagg summaries: Stagg as Met Office meteorologist and SHAEF adviser; claim that he persuaded Eisenhower to shift date from 5 to 6 June.
- Contemporary/current secondary articles: storm on 5 June, brief usable window on 6 June.

Evidence quality:

```trace
D_Day_weather_source_quality := Q1_to_Q2_currently
```

Use status:

```trace
D_Day_weather_public_use := not_yet_sufficient
```

Need stronger sources:

```trace
D_Day_needed_sources :=
  Stagg_Forecast_for_Overlord
  + Met_Office_archive_or_article
  + IWM_or_SHAEF_primary_material
  + tide_weather_moon_constraint_source
```

Allowed internal claim:

```trace
internal_claim_allowed :=
  DDay_weather_decision_was_high_consequence_uncertain_and_time_constrained
```

Not yet allowed as public claim without stronger source:

```trace
public_claim_not_yet :=
  exact_weight_of_each_forecast_team
  + exact_dialogue_or_science_detail
  + exact_decision_causality_strength
```

### 3. Challenger / warning under schedule pressure

Preliminary sources:

- Rogers Commission summaries: immediate cause was O-ring failure; low temperature compromised O-ring performance; NASA and Morton Thiokol failed to respond adequately to known design risk; launch decision process seriously flawed.
- O-ring summaries: cold temperature affected seal resilience.

Evidence quality:

```trace
Challenger_source_quality := Q1_currently_with_clear_path_to_Q3
```

Use status:

```trace
Challenger_public_use := source_upgrade_required
```

Needed:

```trace
Challenger_needed_sources :=
  Rogers_Commission_Report_primary
  + relevant_launch_decision_sections
  + O_ring_temperature_evidence
```

Internal pattern claim currently acceptable:

```trace
Challenger_internal_claim :=
  warning_signal_weakened_under_schedule_pressure
  + launch_selected
  + crew_paid
```

### 4. Cuban Missile Crisis / option-space preservation

Preliminary sources:

- JFK Library page: Kennedy met secretly with advisors; after long meetings chose a naval blockade/quarantine; uncertainty about Khrushchev's response; nuclear-war possibility; final public deal and separate secret missile-removal deal.

Evidence quality:

```trace
Cuban_Missile_Crisis_source_quality := Q3_for_basic_frame
```

Use status:

```trace
Cuban_Missile_Crisis_public_use := acceptable_for_basic_pattern
```

Allowed claim:

```trace
allowed_claim :=
  crisis_handled_through_secret_advisory_deliberation
  + quarantine_selected_before_more_irreversible_options
  + nuclear_consequence_visible
```

Need more before strong process claim:

```trace
needed :=
  ExComm_transcripts
  + decision_option_records
  + historian_secondary_source
```

### 5. Bay of Pigs / captured option-space and weak dissent processing

Preliminary sources:

- JFK Library page: CIA plan approved; invasion failed; Kennedy accepted responsibility publicly; post-failure analysis and consequences.
- General summaries: dispute over CIA assumptions, air cover, and Kennedy's refusal to escalate overtly.

Evidence quality:

```trace
Bay_of_Pigs_source_quality := Q3_for_basic_event_from_JFK_Library
  + Q1_for_internal_group_pressure_claim
```

Use status:

```trace
Bay_of_Pigs_public_use := only_basic_event_claims_until_more_sources
```

Allowed internal claim:

```trace
Bay_of_Pigs_internal_claim :=
  inherited_plan
  + prestige_pressure
  + option_space_and_escalation_pressure
  + failed_operation
```

Need before stronger claim:

```trace
Bay_of_Pigs_needed_sources :=
  official_after_action_or_Taylor_report
  + historian_source_on_groupthink_or_advisory_failure
```

### 6. Chernobyl / safety test becomes harm carrier

Preliminary sources:

- Chernobyl disaster / investigation summaries: accident during safety test; INSAG-1 initially emphasised operator violations; INSAG-7 later emphasised reactor design flaws and inadequate safety culture.
- Secondary summaries: flawed design and operator errors during safety test.

Evidence quality:

```trace
Chernobyl_source_quality := Q1_to_Q2_currently
```

Use status:

```trace
Chernobyl_public_use := source_upgrade_required
```

Need:

```trace
Chernobyl_needed_sources :=
  INSAG_7_primary_report
  + credible nuclear safety secondary source
```

Allowed internal claim:

```trace
Chernobyl_internal_claim :=
  safety_test_context
  + design_and_operator_factors
  + safety_culture_failure
  + body_and_ecology_bill
```

### 7. Therac-25 / interface confidence suppresses body signal

Preliminary sources:

- Therac-25 summaries: multiple radiation overdoses; software faults; removed hardware interlocks; poor error messages; end-user reports dismissed.
- Nancy Leveson and Clark Turner, “An Investigation of the Therac-25 Accidents,” should be treated as required primary/high-quality source for public use.

Evidence quality:

```trace
Therac_25_source_quality := Q1_currently_with_clear_path_to_Q3
```

Use status:

```trace
Therac_25_public_use := source_upgrade_required
```

Need:

```trace
Therac_25_needed_sources :=
  Leveson_Turner_1993
  + medical_device_safety_summary_if_needed
```

Allowed internal claim:

```trace
Therac_25_internal_claim :=
  software_confidence
  + interlock_loss
  + opaque_error_signal
  + patient_body_pays
```

### 8. Apollo 13 / repair path switch under pressure

Preliminary sources:

- Apollo 13 summaries and accident accounts: oxygen tank explosion; mission aborted; crew and ground team improvised safe return; NASA review found oxygen tank 2 failure and later design/procedure changes.
- New Yorker historical account: ground-test handling, tank heating, temperature indication issue, explosion sequence, and rescue effort.

Evidence quality:

```trace
Apollo_13_source_quality := Q2_currently
```

Use status:

```trace
Apollo_13_public_use := acceptable_for_general_pattern_with_source_upgrade_preferred
```

Need:

```trace
Apollo_13_needed_sources :=
  NASA_Apollo_13_Review_Board_Report
  + NASA_mission_summary
```

Allowed internal claim:

```trace
Apollo_13_internal_claim :=
  original_goal_abandoned
  + survival_repair_path_selected
  + repair_carriers_identified
  + crew_returned
```

## Current source-pin verdict

```trace
source_pin_verdict :=
  sufficient_for_internal_pattern_pressure
  - sufficient_for_public_evidence_pack
```

The comparator test can remain in the repo as an internal pressure test. It should not be used publicly until the weak pins are upgraded.

## Public-use upgrade list

Before public use, replace or supplement weak sources with:

```trace
public_upgrade_list :=
  Pressure_official_press_or_film_page
  + Stagg_or_Met_Office_or_IWM_DDay_weather_source
  + Rogers_Commission_Report
  + JFK_Library_Cuban_Missile_Crisis_page_or_ExComm_transcripts
  + JFK_Library_Bay_of_Pigs_page_plus_Taylor_Report_or_historian
  + INSAG_7_Chernobyl_report
  + Leveson_Turner_Therac_25_paper
  + NASA_Apollo_13_Review_Board_Report
```

## Claim boundaries after source pin

Safe internal claim:

```trace
safe_internal_claim :=
  Pressure_reveals_a_recurring_pressure_decision_pattern
  across_cases_where_uncertainty_warning_timing_and_consequence_interact
```

Unsafe public claim:

```trace
unsafe_public_claim :=
  history_validates_TRACE
  OR Pressure_proves_TRACE
  OR Pressure_Discipline_Pattern_is_a_finished_operator
```

## Next action

```trace
next_action :=
  if_public_use:
    collect_primary_sources
    + quote_check
    + one_page_public_case_note
  else:
    stop_here
```

End.
