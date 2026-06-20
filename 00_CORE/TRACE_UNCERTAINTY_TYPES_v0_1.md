# TRACE Uncertainty Types v0.1

Status: core refinement / kernel patch surface.  
Parent: `00_CORE/TRACE_MATH_KERNEL_v0_1.md`.  
Reason: fresh-reader critique correctly found that `U_actual` cannot be treated as simple omniscient entropy.

## 0. Purpose

TRACE requires visible uncertainty.

But uncertainty is not one thing.

This file separates uncertainty types so the kernel does not pretend that all uncertainty can be computed from a single model entropy.

## 1. Uncertainty Vector

Define uncertainty profile:

```math
U_e(t) = (U^{epi}, U^{ale}, U^{mod}, U^{norm}, U^{stand}, U^{trans}, U^{meta})
```

Where:

```text
U^epi   = epistemic uncertainty / missing knowledge or data
U^ale   = aleatoric uncertainty / stochastic world variation
U^mod   = model uncertainty / model-form uncertainty
U^norm  = normative uncertainty / uncertainty about value, priority, or duty
U^stand = standing uncertainty / uncertainty about moral/legal/patient status
U^trans = translation uncertainty / uncertainty moving from TRACE to human rule
U^meta  = uncertainty about the uncertainty estimate itself
```

## 2. Epistemic Uncertainty

Epistemic uncertainty is reducible in principle by better evidence.

```math
U^{epi} = uncertainty_due_to_missing_information
```

Failure mode:

```math
U^{epi}_{displayed} < U^{epi}_{actual}
```

Mechanical Ethics:

Do not hide ignorance.

## 3. Aleatoric Uncertainty

Aleatoric uncertainty is variation in the world or process.

```math
U^{ale} = uncertainty_due_to_stochastic_variation
```

This may not be removable by more data.

Mechanical Ethics:

Do not present stochastic outcomes as deterministic guarantees.

## 4. Model Uncertainty

Model uncertainty concerns whether the model form is adequate.

```math
U^{mod} = uncertainty_over_model_class
```

Example:

```math
P(M_i | data)
```

where multiple models remain live.

Mechanical Ethics:

Do not act as if one model has captured the world when rival models remain plausible.

## 5. Normative Uncertainty

Normative uncertainty concerns what matters, how much, and under what priority.

```math
U^{norm} = uncertainty_about_value_or_priority
```

This cannot be solved merely by more factual data.

Mechanical Ethics:

High normative uncertainty should lower permission for irreversible imposition.

## 6. Standing Uncertainty

Standing uncertainty concerns the status of the entity being modelled.

```math
U^{stand} = uncertainty_about_subjecthood_or_protected_status
```

Mechanical Ethics:

When standing uncertainty is high and irreversible harm is possible, use conservative treatment.

## 7. Translation Uncertainty

Translation uncertainty concerns converting TRACE diagnosis into human-facing rule.

```math
U^{trans} = uncertainty_about_ME_translation
```

Example:

TRACE may show:

```math
Capture_e ↑
```

But the correct institutional rule may still be uncertain.

Mechanical Ethics:

Do not confuse a detected structure with a fully specified policy.

## 8. Meta-Uncertainty

The fresh-reader critique is correct: `U_actual` may not be objectively knowable.

Define:

```math
U^{meta} = uncertainty_about_U
```

So instead of assuming perfect access to `U_actual`, TRACE tracks:

```math
\hat{U}_{actual} ± U^{meta}
```

Danger condition:

```math
U_{displayed} < \hat{U}_{actual} - margin
```

Severe danger condition:

```math
U^{meta} ↑ ∧ I(a) ↑ ∧ U_{displayed} ↓
```

## 9. Display Rule

For high-stakes systems, uncertainty display should show at least:

```text
knowns
unknowns
model limits
confidence range
appeal/correction route
irreversibility warning
```

## 10. Mechanical Ethics Translation

TRACE:

```math
U^{epi}_{displayed} < U^{epi}_{actual}
```

Mechanical Ethics:

Do not hide ignorance.

TRACE:

```math
U^{mod} high
```

Mechanical Ethics:

Do not act as if the model is settled.

TRACE:

```math
U^{norm} high ∧ I(a) high
```

Mechanical Ethics:

Do not impose irreversible outcomes under unresolved value conflict.

TRACE:

```math
U^{meta} high
```

Mechanical Ethics:

Do not pretend uncertainty itself is precisely known.

## 11. Guardrail

TRACE does not require omniscience.

It requires visible limits.
