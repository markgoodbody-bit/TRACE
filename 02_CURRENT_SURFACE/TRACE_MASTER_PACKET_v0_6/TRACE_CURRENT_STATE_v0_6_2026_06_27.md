# TRACE Current State v0.6 — 2026-06-27

Status: working TRACE artifact. Not validation.

This note freezes the current TRACE position before the separate Mechanical Ethics build begins.

## Split now in force

```trace
TRACE_artifact :=
  pre-prescriptive minimal-value grammar
  for transitions under uncertainty

Mechanical_Ethics_artifact :=
  later prescriptive layer:
  what should follow if TRACE's description is accepted
```

TRACE is the descriptive / field-inspection side. Mechanical Ethics is the later prescriptive side.

## Current packet shape

```trace
TRACE_Master_Packet_v0_6 :=
  motivation_layer
  + cold_test_card
  + decision_delta_battery
  + case_record_template
  + trust_audit_ledger
  + ME_boundary_stub
  + review_prompts
```

## Current operational spine

```trace
transition
-> affected scopes
-> future-space comparison
-> preference-gradient / local reward pull
-> loss clock
-> opportunity clock
-> correction channel usability
-> estimator authority
-> burden shift
-> residue
-> router/status label
```

Future-space is compared qualitatively:

```trace
F_x(t) := (O_x(t), R_x(t), I_x(t))

O := option topology
R := practical reachability
I := usable navigational information
```

Do not use fake scalar subtraction or undefined weights.

## Two clocks

```trace
loss_clock := T_det + T_route + T_corr < T_irr
opportunity_clock := T_access + T_uptake + T_integrate < T_opp
```

The likely decision-relevant contribution is forced dual-clock attention: checking both whether correction arrives before loss hardens and whether access arrives before opportunity expires.

## Estimator authority rule

Every clock-band estimate should record who set it.

```yaml
estimator_identity:
estimator_role:
estimator_incentive:
estimator_independence:
affected_scope_challenge_route:
contamination_flag:
```

```trace
if estimator_is_assessed_actor:
  estimate_status := CONTAMINATED_SIGNAL by default
```

The assessed actor may still be right. The point is that the estimate is not independent.

## Scope handling

Use unordered scope reasons, not a worth ladder.

```trace
scope_reasons :=
  affected
  continuing
  preference_bearing
  vulnerable_or_dependent
  domain_protected
  disputed_or_unknown
```

Uncertainty should be recorded, not silently demoted.

## Status labels

TRACE must be able to return:

```trace
UNKNOWN
COMPRESSION_ONLY
PARTIAL_SIGNAL
STRONG_SIGNAL
REGRESSION
CONTAMINATED_SIGNAL
```

## Current review signal

```trace
AI_reconstruction_signal := present
cross_language_reconstruction_candidate := present
low_fit_COMPRESSION_ONLY_cases := present
high_fit_PARTIAL_SIGNAL_candidate := present
STRONG_SIGNAL := none
validation := false
```

The project has passed the basic coherence gate. It has not passed the reliable decision-improvement gate.

## Current best description

```trace
TRACE_v0_6 :=
  structurally_coherent
  + transmissible
  + testable
  + not_validated
  + good_enough_to_pause_major_rewrites
```

Further TRACE work should mostly be testing, case records, and minor repairs. The next major build should be the separate Mechanical Ethics artifact.
