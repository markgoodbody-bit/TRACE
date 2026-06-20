# TRACE Reachability Model v0.1

Status: core refinement / kernel patch surface.  
Parent: `00_CORE/TRACE_MATH_KERNEL_v0_1.md`.  
Reason: fresh-reader critique correctly found that reachability cannot remain a loose scalar.

## 0. Purpose

TRACE distinguishes abstract action-space from lived reachable action-space.

This file defines reachability as a profile first and a scalar only second.

## 1. Abstract Action-Space

For entity `e`:

```math
A_e(t) = \{a_1, a_2, ..., a_n\}
```

This means action `a` is abstractly describable.

It does not mean action `a` is live for entity `e`.

## 2. Reachability Profile

Define reachability profile:

```math
Rho_e(a,t) = (r_time, r_money, r_knowledge, r_force, r_fear, r_health, r_cognition, r_social, r_legal, r_language, r_physical)
```

Each component lies in:

```math
r_i ∈ [0,1]
```

Where:

```text
r_time      = enough time to perform action
r_money     = enough economic capacity
r_knowledge = knowledge that action exists and how to use it
r_force     = absence of coercive force blocking action
r_fear      = fear level compatible with action
r_health    = bodily/medical capacity
r_cognition = cognitive load / comprehension / executive capacity
r_social    = social support / safe witness / relational backing
r_legal     = legal access / procedural access
r_language  = language and communication access
r_physical  = physical/geographic/digital access
```

## 3. Bottleneck Reachability

For actions requiring all components, use bottleneck reachability:

```math
\rho_e(a,t) = min_i Rho_{e,i}(a,t)
```

If one required component is zero, action reachability is zero.

This fits appeals, escape routes, medical access, legal challenge, and safety-seeking actions.

## 4. Weighted Reachability

Some actions do not require every component equally.

Define weights:

```math
w_a = (w_1, ..., w_k)
```

Then:

```math
\rho_e(a,t) = \prod_i Rho_{e,i}(a,t)^{w_i}
```

This preserves bottleneck pressure while allowing action-specific profiles.

## 5. Action Is Live

An action is live when:

```math
a ∈ A_e(t) ∧ \rho_e(a,t) ≥ \theta_a
```

Define lived action-space:

```math
LA_e(t) = \{a ∈ A_e(t) : \rho_e(a,t) ≥ \theta_a\}
```

## 6. Capture

Capture is the loss of lived action-space relative to abstract action-space:

```math
Capture_e(t) = 1 - |LA_e(t)| / |A_e(t)|
```

For weighted action-space:

```math
Capture_e(t) = 1 - \frac{Σ_{a∈A_e(t)} \rho_e(a,t)}{|A_e(t)|}
```

High capture:

```math
Capture_e(t) -> 1
```

This means most abstract actions are not live.

## 7. Appeal / Correction Reachability

For institutional and AI systems, define correction reachability:

```math
\rho_e(correct,t)
```

A formal appeal route exists only abstractly unless:

```math
\rho_e(correct,t) ≥ \theta_{correct}
```

If:

```math
\rho_e(correct,t) < \theta_{correct}
```

then the system must not claim meaningful contestability.

## 8. Mechanical Ethics Translation

TRACE:

```math
a ∈ A_e ∧ \rho_e(a,t) ≈ 0
```

Mechanical Ethics:

A system must not treat abstract availability as meaningful access.

TRACE:

```math
\rho_e(correct,t) < \theta_{correct}
```

Mechanical Ethics:

A formal appeal route is not a real correction route.

TRACE:

```math
Capture_e(t) -> 1
```

Mechanical Ethics:

Responsibility must be assessed with collapsed reachable exits visible.

## 9. Guardrail

Do not reduce reachability to one scalar too early.

Use the profile for diagnosis.

Use scalar compression only when the aggregation rule is explicit.
