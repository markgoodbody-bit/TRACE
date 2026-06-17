# TRACE Source-Backed Comparator Run — Prediction Authority v0.1

Date: 2026-06-17
Status: first source-backed comparator run / provisional / not validation

## Purpose

This file runs the first comparator pass against the prediction-authority worked-delta protocol.

The question is whether TRACE adds navigational value beyond existing due-process, administrative-law, contestability, reviewability, and algorithmic-accountability work.

```trace
source_backed_comparator_run :=
  worked_delta_protocol
  + comparator_sources
  + delta_test
  + demotion_test
  + residual_if_any
  - validation_claim
```

## Claim being tested

Claimed TRACE delta:

```trace
TRACE_delta_candidate :=
  prediction_authority_gate
  + contestability_clock
  + future_space_confiscation
  + technical_opacity_as_route_block
```

Demotion condition:

```trace
TRACE_delta_falsified_if:
  due_process_or_administrative_law
  + open_future_or_anticipatory_harm_analysis
  + algorithmic_accountability_analysis
  already_captures:
    prediction_as_authority_gate
    + contestability_clock
    + future_space_confiscation
    + changed_conduct_as_relevant
    + technical_opacity_as_route_block
  with_equal_clarity
  and_less_vocabulary
```

## Comparator sources used in this first pass

This is a first pass from accessible source summaries and paper abstracts. It is not a full literature review.

Comparator families:

1. Reviewable automated decision-making — reviewability, record keeping, socio-technical process, administrative-law framing.
2. Contestability work — contesting algorithmic decisions as a safeguard, with administrative-law design insights.
3. Process-centric explanations — explanations must cover process and development/deployment rationale, not only outcomes.
4. Algorithmic tools in public decision systems — transparency, evaluation, monitoring, and governance problems.
5. Scored-society / automated prediction work — scoring opacity, public review, and education about score variables.
6. Open-future / anticipatory-harm family — relevant but not fully run in this pass.

```trace
comparator_set :=
  reviewability
  + contestability
  + process_explanation
  + public_algorithm_governance
  + scored_society
  + open_future_pending
```

## Comparator pass

### 1. Prediction as authority gate

Comparator result:

The comparator literature strongly covers the problem that automated outputs become part of consequential decision-making. Reviewability frames automated decision-making as a socio-technical process extending before and beyond the decision, not a single model output. Contestability work treats challenge as an important safeguard for affected people. Public-sector algorithm governance work highlights that deployed tools may lack sufficient information about purpose, use, evaluation, and monitoring.

TRACE result:

```trace
forecast_gate :=
  predicted_path
  -> authorised_intervention
  -> present_constraint
```

Assessment:

```trace
prediction_as_authority_gate :=
  mostly_captured_by_comparator
  but:
    TRACE_names_gate_transition_more_compactly
```

Residual delta: small but real as diagnostic compression. Existing work captures the issue; TRACE gives a portable gate test.

### 2. Contestability clock

Comparator result:

Contestability literature clearly recognises that affected people need meaningful ability to challenge decisions. Administrative-law based contestability and reviewability both emphasise process, record keeping, and institutional arrangements that make review possible. Process-centric explanation work also pushes beyond outcome explanation toward the rationale and process behind system development and deployment.

What is less foregrounded in the comparator summaries is the hard timing claim: contestability must reach the relevant gate before the life path hardens, otherwise it becomes theatre.

TRACE result:

```trace
contestability_real_if:
  challenge_reaches_gate
  before:
    future_space_closes
```

Assessment:

```trace
contestability_clock :=
  partially_captured_by_comparator
  but:
    TRACE_sharpens_timing_axis
```

Residual delta: strongest surviving contribution in this run.

### 3. Technical opacity as route block

Comparator result:

The comparator literature strongly covers opacity. Reviewability emphasises record keeping across technical and organisational elements. Process-centric explanation argues that explanation should cover rationales behind development and deployment, not only the outcome. Public algorithm governance work highlights the lack of sufficient information to evaluate deployed systems. Scored-society work highlights opacity and the need for public review and education about scoring variables.

TRACE result:

```trace
opacity_harmful_if:
  subject_cannot_replay_basis
  + decision_changes_life_path
```

Assessment:

```trace
technical_opacity_as_route_block :=
  strongly_captured_by_comparator
  TRACE_delta := weak
```

Residual delta: weak. Existing algorithmic-accountability and reviewability work already handles this better and with richer institutional detail.

### 4. Future-space confiscation

Comparator result:

Due-process and contestability work protect procedural fairness and challenge routes. Scored-society work recognises social consequences of automated scores and restrictions on participation. The open-future and anticipatory-harm family appears relevant but has not yet been fully run in this pass.

TRACE result:

```trace
future_space_confiscation :=
  possible_future
  treated_as:
    fixed_identity
  -> present_closure
```

Assessment:

```trace
future_space_confiscation :=
  partially_captured_by_comparator
  + open_future_comparator_pending
  TRACE_delta := plausible_but_unproven
```

Residual delta: plausible, but cannot be claimed as surviving until the open-future / anticipatory-harm comparator is actually read and tested.

### 5. Changed conduct as relevant

Comparator result:

Due-process, risk-assessment, and contestability traditions can recognise inaccurate predictions and review needs. The specific idea that a person's future remains alterable until institutional action hardens it is not clearly established from this first-pass source set.

TRACE result:

```trace
agency_erased_if:
  predicted_future
  treated_as:
    unchangeable_identity
```

Assessment:

```trace
changed_conduct_as_relevant :=
  partly_captured_by_due_process_and_risk_error_frames
  but:
    TRACE_links_it_to_future_space_and_timing
```

Residual delta: plausible but tied to the future-space claim.

## Delta table

| Claimed TRACE component | Comparator coverage | TRACE residual | Result |
|---|---:|---:|---|
| prediction as authority gate | high | low-medium | survives as compression only |
| contestability clock | medium | medium-high | strongest residual |
| technical opacity as route block | high | low | mostly demoted |
| future-space confiscation | medium / incomplete | medium | plausible, comparator pending |
| changed conduct as relevant | medium / incomplete | medium | plausible, comparator pending |

## Provisional verdict

```trace
verdict :=
  TRACE_delta_not_fully_falsified
  but:
    large_parts_captured_by_existing_work

surviving_residual :=
  contestability_clock
  + future_space_confiscation_pending
  + gate_compression

mostly_demoted :=
  technical_opacity_as_route_block
```

Plain version:

TRACE does not beat the comparator literature wholesale. Reviewability, contestability, process explanation, and algorithmic-accountability work already capture much of the issue, especially opacity, record keeping, and challenge routes.

The surviving TRACE contribution is narrower: timing and future-space as a diagnostic movement.

```trace
surviving_question :=
  can_contestability_reach_the_gate
  before_future_space_hardens?
```

## Demotion result

The original demoter is only partly met.

```trace
demoter_status :=
  technical_opacity_component_demoted
  + prediction_gate_component_demoted_to_compression
  + contestability_clock_survives
  + future_space_component_pending_open_future_comparator
```

Therefore:

```trace
Prediction_Authority_status :=
  keep_as_worked_delta_candidate
  but:
    narrow_claim
    + no_validation
    + run_open_future_comparator_next_if_continuing
```

## Patch implication

Later, the worked-delta case should be narrowed:

```trace
patch_case_later :=
  narrow_TRACE_delta_to:
    contestability_clock
    + future_space_confiscation
    + prediction_gate_as_compression
  demote:
    technical_opacity_as_route_block
  mark:
    open_future_comparator_pending
```

## What this run does not settle

```trace
not_settled :=
  validation
  + full_literature_review
  + real_world_case_application
  + open_future_comparator
```

## Recommendation

```trace
recommendation :=
  keep_candidate_alive
  + narrow_claim
  + no_more_cases
  + patch_index_or_case_later
```

Plain version:

This comparator run gives TRACE a limited survival: not a new field, not a replacement for due process or algorithmic accountability, but a compact timing-and-future-space diagnostic. That is enough to keep the candidate alive, not enough to promote it.
