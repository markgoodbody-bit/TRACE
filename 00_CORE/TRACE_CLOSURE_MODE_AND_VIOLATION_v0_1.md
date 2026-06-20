# TRACE Closure Mode and Violation v0.1

Status: core refinement / kernel patch surface.  
Parent: `00_CORE/TRACE_MATH_KERNEL_v0_1.md`.  
Reason: fresh-reader critique correctly found that future-space volume loss alone does not capture violation.

## 0. Purpose

Two actions can close similar amounts of future-space while differing morally, legally, and structurally.

Example:

```text
accident closes future-space
coercion closes future-space
fraud closes future-space
predation closes future-space
neglect closes future-space
```

TRACE therefore needs a variable for how future-space is closed.

## 1. Raw Future-Space Closure

Raw closure:

```math
\Delta F_e(a) = F_e(t) \setminus F_e(t+\Delta t | a)
```

Weighted harm:

```math
\Delta H_e(a) = \Phi_e(F_e(t)) - E[\Phi_e(F_e(t+\Delta t)) | a]
```

But this only tells us loss magnitude/profile.

It does not tell us mode.

## 2. Closure Mode

Define closure mode:

```math
CM_e(a) ∈ \mathcal{C}
```

where:

```text
accident
coercion
deception
neglect
predation
bureaucratic_error
model_error
system_optimisation
self_action
mutual_risk
care_tradeoff
emergency_force
unknown
```

## 3. Closure Vector

A closure event should be represented as:

```math
K_e(a) = (\Delta F_e(a), \Delta H_e(a), CM_e(a), I_e(a), R_e(a), RespRoute(a))
```

Where:

```text
DeltaF = raw futures closed
DeltaH = weighted future-space loss
CM = mode of closure
I = irreversibility
R = repairability
RespRoute = route through which responsibility can be traced
```

## 4. Violation

Violation is not merely loss.

Violation occurs where closure mode includes wrongful agency, boundary breach, coercion, deception, predation, or illegitimate authority.

Define violation indicator:

```math
Vio_e(a) ∈ [0,1]
```

High violation modes include:

```text
coercion
deception
predation
abuse_of_authority
non-consensual_boundary_breach
```

Low or different violation modes include:

```text
accident
mutual_risk
care_tradeoff
natural_constraint
```

This does not mean accidents are harmless.

It means repair and responsibility differ by closure mode.

## 5. Repair Depends on Closure Mode

Repair function:

```math
Repair_e = f(\Delta H_e, I_e, CM_e, Vio_e, RespRoute)
```

For accident:

```text
restore capacity, compensate loss, reduce recurrence
```

For deception:

```text
restore truth, undo induced action, sanction deceiver, prevent recurrence
```

For coercion:

```text
restore agency, remove coercive structure, repair loss, constrain coercer
```

For predation:

```text
protect subject, stop predator, repair scar where possible, impose durable constraint
```

For bureaucratic/model error:

```text
correct record, restore lost future-space, compensate delay, change system permission
```

## 6. Mechanical Ethics Translation

TRACE:

```math
\Delta H_1 ≈ \Delta H_2 ∧ CM_1 ≠ CM_2
```

Mechanical Ethics:

Similar loss magnitude does not imply identical moral or institutional response.

TRACE:

```math
CM = deception
```

Mechanical Ethics:

Truth repair is required, not only material compensation.

TRACE:

```math
CM = coercion
```

Mechanical Ethics:

Agency restoration is required, not only outcome correction.

TRACE:

```math
CM = bureaucratic_error ∧ I ↑
```

Mechanical Ethics:

Record correction must occur before administrative error hardens into lived reality.

## 7. Guardrail

Do not collapse all harm into scalar future-space loss.

Track:

```text
how much future was closed
which future was closed
how it was closed
who closed it
whether it can be repaired
what responsibility route remains
```
