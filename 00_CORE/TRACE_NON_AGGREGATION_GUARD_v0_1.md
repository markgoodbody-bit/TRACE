# TRACE Non-Aggregation Guard v0.1

Status: core refinement / kernel patch surface.  
Parent: `00_CORE/TRACE_MATH_KERNEL_v0_1.md`.  
Reason: fresh-reader critique correctly found that raw total-harm minimisation can collapse into utilitarian sacrifice.

## 0. Purpose

The kernel currently includes:

```math
a^* = argmin_{a∈A} [\Delta H_{total}(a) + I_{total}(a) + HB(a)]
```

This is unsafe if read as simple aggregate utilitarian optimisation.

TRACE must not permit subject erasure through summation.

## 1. Problem

A total-harm rule can permit:

```math
\Delta H_{one} ↑↑
```

if:

```math
Σ\Delta H_{many} ↓
```

This violates TRACE's subject-preservation constraint.

## 2. Protected Individual Loss

For each entity:

```math
\Delta H_e(a)
```

Define maximum individual loss:

```math
MaxLoss(a) = max_e \Delta H_e(a)
```

Define irreversible individual loss:

```math
IrrLoss_e(a) = \Delta H_e(a) \cdot I_e(a)
```

High-risk condition:

```math
max_e IrrLoss_e(a) ≥ \theta_{severe}
```

## 3. Lexicographic Guard

System decision should not be pure sum-minimisation.

Use lexicographic ordering:

```text
1. Exclude actions that impose severe irreversible individual loss unless necessary to prevent greater severe irreversible loss.
2. Exclude actions with hidden bill above threshold.
3. Exclude actions where uncertainty display is below required level.
4. Among remaining actions, minimise total harm and irreversibility.
```

Formal sketch:

```math
A_{admissible} = \{a ∈ A : Guard(a)=pass\}
```

Then:

```math
a^* = argmin_{a∈A_{admissible}} [Σ_e \Delta H_e(a) + Σ_e I_e(a) + HB(a)]
```

Aggregation is allowed only after guard constraints.

## 4. Guard Function

```math
Guard(a)=pass
```

only if:

```math
max_e IrrLoss_e(a) < \theta_{severe}
```

or:

```math
Necessity(a)=true ∧ No_Less_Irreversible_Alternative(a)=true
```

and:

```math
HB(a) < \theta_{HB}
```

and:

```math
U_{displayed}(a) ≥ U_{required}(a)
```

and:

```math
RespRoute(a) exists
```

## 5. Pareto Check

A preferred action should be Pareto-improving where possible:

```math
∀e: \Delta H_e(a_1) ≤ \Delta H_e(a_2)
```

and:

```math
∃e: \Delta H_e(a_1) < \Delta H_e(a_2)
```

When no Pareto-improving action exists, record the collision explicitly.

## 6. Collision Register

If all available actions impose serious harm on some entity, create a collision register:

```math
Collision(a) = \{e : \Delta H_e(a) ≥ \theta_{harm}\}
```

A collision cannot be hidden inside total utility.

Mechanical Ethics translation:

A system must name who is being spent.

## 7. Mechanical Ethics Translation

TRACE:

```math
Σ\Delta H lowered by imposing severe irreversible loss on one entity
```

Mechanical Ethics:

Aggregate benefit does not automatically justify spending a subject.

TRACE:

```math
Collision(a) non-empty
```

Mechanical Ethics:

Collision must be named; affected subjects must not disappear into totals.

TRACE:

```math
Guard(a)=fail
```

Mechanical Ethics:

The action is not ethically admissible even if aggregate score is favourable.

## 8. Guardrail

Aggregation is a later-stage comparison tool.

It is not the root of ethics.

Subject-preservation, uncertainty visibility, hidden-bill control, and irreversibility constraints come first.
