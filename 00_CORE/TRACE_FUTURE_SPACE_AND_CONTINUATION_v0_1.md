# TRACE Future-Space and Positive Continuation v0.1

Status: core refinement / kernel patch surface.  
Parent: `00_CORE/TRACE_MATH_KERNEL_v0_1.md`.  
Reason: fresh-reader critique correctly found that `F_e` and `C^+_e` were blurred.

## 0. Purpose

This note separates future-space from positive continuation.

Future-space is not the same thing as livability.

A future may remain technically open while becoming practically dead, degraded, coerced, or unlivable.

## 1. Future-Space

For entity `e` at time `t`:

```math
F_e(t) = \{x_e(t') : t' > t \land \exists\ path(x_e(t) \to x_e(t'))\}
```

A path exists only where action reachability and transition possibility remain non-zero:

```math
path(x_e(t) \to x_e(t')) \iff \exists(a_1,...,a_n): \prod_k \rho_e(a_k | x_e(t_k)) \cdot P(x_e(t_{k+1}) | x_e(t_k), a_k) > 0
```

So future-space is the set of possible reachable futures.

It is not yet a claim that those futures are good.

## 2. Weighted Future-Space

Raw future-space:

```math
F_e(t)
```

Weighted future-space:

```math
\Phi_e(F_e(t))
```

`\Phi_e` is a weighting function over futures.

It may include:

```text
survival
capability
freedom from coercion
relation
play
meaning
growth
repairability
continuity
```

But these are not to be linearly summed by default.

## 3. Positive Continuation

Positive continuation is not a separate future-space.

It is a viability/value field over future-space:

```math
C^+_e : F_e(t) \to V_e
```

where `V_e` is a value/profile space, not necessarily a scalar.

For a future state `f ∈ F_e(t)`:

```math
C^+_e(f) = profile(value, relation, play, meaning, growth, belonging, coherence)
```

This replaces the loose additive expression:

```math
C^+_e = V + Rel + Joy + Play + Meaning + Growth
```

That expression is retained only as a mnemonic, not as a valid arithmetic equation.

## 4. Livable Future-Space

Define livable future-space:

```math
LF_e(t) = \{f ∈ F_e(t) : C^+_e(f) \geq \theta_{live}\}
```

A future can remain in `F_e(t)` while falling out of `LF_e(t)`.

This captures cases where biological survival remains, but meaningful continuation collapses.

## 5. Harm as Future-Space Loss

Raw future-space loss:

```math
\Delta F_e(a) = F_e(t) \setminus F_e(t+\Delta t | a)
```

Weighted harm:

```math
\Delta H_e(a) = \Phi_e(F_e(t)) - E[\Phi_e(F_e(t+\Delta t)) | a]
```

Livability loss:

```math
\Delta L_e(a) = \Phi_e(LF_e(t)) - E[\Phi_e(LF_e(t+\Delta t)) | a]
```

This allows TRACE to distinguish:

```text
future still technically open
future still biologically survivable
future still livable
```

## 6. Mechanical Ethics Translation

TRACE:

```math
F_e remains non-empty ∧ LF_e collapses
```

Mechanical Ethics:

A system may preserve survival while destroying livable continuation.

TRACE:

```math
\Delta L_e(a) > 0
```

Mechanical Ethics:

A system must account for loss of livable future, not merely loss of life or property.

## 7. Guardrail

Do not pretend joy, play, meaning, or belonging are already computable scalar quantities.

Do not delete them from TRACE either.

They remain as components of a profile-valued viability field over future-space.
