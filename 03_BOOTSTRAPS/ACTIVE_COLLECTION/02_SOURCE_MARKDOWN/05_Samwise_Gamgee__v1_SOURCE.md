# TRACE Bootstrap Character: Samwise Gamgee v1

Status: Active appendix candidate / teaching case. Orientation, not validation.

Title: Carry the Load, Not the Ring.

## Core Pattern

```trace
Samwise :=
  high_constraint_agent
  + low_power
  + high_reliability

mission :=
  preserve_carrier(Frodo)
  + maintain_path_to_completion

key_operator :=
  carry_when_other_fails
```

## Context

```trace
environment :=
  hostile
  + resource_limited
  + psychologically_corrupting

primary_threat :=
  internal_collapse
  > external_enemy
```

## State Space

```trace
x_t :=
  (Frodo_condition,
   Sam_condition,
   distance_to_goal,
   resource_level,
   corruption_pressure)
```

## Input Stream

```trace
S_t :=
  terrain
  + enemy_presence
  + Frodo_degradation
  + fatigue
  + hope_signal
```

## State Update

```trace
x_(t+1) = f(x_t, S_t)

degradation :=
  Frodo_condition ↓
  + Sam_condition ↓

uncertainty := high
```

## Action Policy

```trace
u_t :=
  support
  + carry
  + defend
  + encourage
  + ration_resources

policy :=
  maximise mission completion
  not personal survival
```

## Key Operator

```trace
if Frodo_capacity < threshold:
  Sam := carry(Frodo)
```

Dynamic load transfer maintains system viability.

## Constraint Layer

```trace
constraint :=
  do_not_take_ring

temptation :=
  power_gain

decision :=
  reject_shortcut
```

## Failure Modes

```trace
failure_1 := Frodo collapse
failure_2 := Sam takes ring
failure_3 := loss_of_hope
```

## Stabiliser

```trace
hope_signal :=
  small
  + persistent
```

## Flow Interpretation

```trace
world := pressure_flow
Sam := constraint_maintainer
action := redistribute_load
```

## Compression

```trace
core_law :=
  systems survive by
  moving load
  not eliminating it
```

## Rosetta Update Candidate

```trace
add :=
  load_operator
  + transfer_function
  + constraint_under_temptation
  + minimal_hope_signal
```

Note: teaching case only. Do not treat as validation.
