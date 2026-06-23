# TRACE Temporal Clock Index — Z.ai Review Log

Status: external review log / pressure signal. Not validation.

Source: user-pasted Z.ai review output for `TRACE_temporal_clock_index_relay_packet_v0_1`.

## Compressed review result

```trace
reviewer := Z.ai
verdict := MODIFY
candidate_status := support_layer_or_case_method_only
promotion := test_on_Grenfell_like_cases_before_promotion
```

## Main finding

The Temporal Clock Index adds value, but only if kept small.

It does not need to become a standalone eight-field temporal database.

The useful contribution is narrower:

```trace
clock_substitution_detection :=
  if clock_A pauses/delays clock_B:
    name clock_A
    name controller(clock_A)
    state why pause is justified
    expose affected_scope + hardening_effect
```

## What it adds

```trace
adds :=
  cross_clock_dependency_tracking
  + clock_substitution_visibility
  + contestability_of_pause_claims
```

v0.11 already detects delay laundering. The Temporal Clock Index adds a sharper detector for **which clock is being used to launder which other clock**.

Examples:

```trace
inquiry_clock pauses survivor_support_clock
justice_clock pauses building_safety_clock
emergency_clock pauses review_clock
```

## What it breaks

```trace
breaks :=
  operational_velocity
  + cognitive_load
  + phantom_compliance_risk
```

A full eight-field index for every active clock would overload RAPID_TRIAGE and complex disaster response.

```trace
if clocks := many
and fields_per_clock := 8+
then:
  operator_burden ↑
  paperwork_paralysis ↑
  fake_completeness ↑
```

## Smallest safe form

Do not promote the full `TemporalClock(c)` schema.

Smallest safe version:

```trace
if TransitionClaim delays_or_pauses_clock:
  require {
    paused_clock,
    pausing_clock,
    pausing_clock_controller,
    justification_for_pause,
    hardening_effect_of_pause,
    review_clock_for_pause
  }
```

Even smaller form:

```trace
pausing_clock_id
pausing_clock_controller
```

But the richer six-field form better preserves harm visibility.

## Biggest drift risk

```trace
drift_risk := temporal_database_sprawl
```

TRACE could drift into indexing every possible clock instead of only the clock interactions where laundering occurs.

Guard:

```trace
index_clock_only_if:
  clock_is_used_to_pause_or_prioritise_another_clock
  ∨ actor_benefits_from_delay
  ∨ hardening_effect_is_contested
  ∨ evidence_decay_is_material
```

## Patch decision

```trace
patch_decision := MODIFY
kernel_promotion := no
support_layer_candidate := yes
case_testing_required := yes
```

## Impact on current candidate

Z.ai pressure supports replacing the full Temporal Clock Index with a narrower **Clock Substitution Note** inside TransitionClaims.

Candidate name:

```trace
ClockSubstitutionClaim := Claim({
  paused_clock,
  pausing_clock,
  pausing_clock_controller,
  justification_for_pause,
  hardening_effect_of_pause,
  review_clock_for_pause,
  contest_edge
})
```

This should be tested against Grenfell-style cases before any core promotion.
