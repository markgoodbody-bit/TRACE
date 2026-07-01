# TRACE Harm / Harmlessness Mathematical Note v0.1

Status: candidate primitive mathematical note. Not canon. Not validation. Not proof. Not permission. Not a moral oracle.

Purpose: define harm and harmlessness as future-space primitives under transition. This note formalises the current working claim that harm is not identical to pain, blame, bad feeling, or moral dirt. Harm is protected future-space reduction under transition, with correction and residue kept visible.

```trace
harm_note_v0_1 :=
  primitive_candidate
  + future_space_reduction
  + correction_clock
  + residue_guard
  + anti_laundering_boundary
  - validation
  - permission
  - canon
```

---

## 1. Transition

An action or inaction changes world-state.

```math
x_t --a--> x_{t+1}
```

Action includes omission where non-action changes future-space or permits harm to harden.

```trace
action_or_inaction := transition_channel
```

---

## 2. Future-space

For an entity or protected scope `e`, future-space is the set of reachable future trajectories available from state `x`.

```math
F_e(x) := { γ : γ is a reachable future trajectory for e from x }
```

Future-space is not raw option count. A future-space may be widened in a way that becomes unusable, disorienting, relationally destructive, or non-repairable.

```trace
raw_option_count != viable_future_space
```

Viable future-space is vectorial.

```math
Φ_e(F_e) := (V_e, A_e, W_e, R_e, C_e, I_e)
```

Where:

```text
V_e := viability
A_e := agency / option-space
W_e := welfare / pain / flourishing condition
R_e := repairability
C_e := continuity / identity / persistence
I_e := informational integrity / truth available for correction
```

A scalar measure may be used only as a compression, not as a moral permission score.

```math
μ_e(F_e) := measure_or_ordering_of_viable_future_space_for_e
```

Guard:

```trace
μ_e != moral_absolution_score
```

---

## 3. Harm

Core definition:

```trace
harm := protected_future_space_reduction_under_transition
```

Mathematical form:

```math
H(a,x,e) := [ μ_e(F_e(x)) - E_{x' ~ P(. | x,a)} μ_e(F_e(x')) ]_+
```

Where:

```math
[z]_+ := max(z,0)
```

So:

```math
H(a,x,e) > 0 iff expected protected future-space for e is reduced by transition a from x
```

Vector form:

```math
H_e(a,x) := [ Φ_e(F_e(x)) - E(Φ_e(F_e(x')) | x,a) ]_+
```

Compact TRACE form:

```trace
H_e := Δ⁻F_e
```

Harm is therefore not identical to sensory pain, culpability, illegality, offence, cost, preference-frustration, or visible suffering.

```trace
pain != harm
blame != harm
procedure != harm_repair
```

---

## 4. Harmlessness

Strong harmlessness:

```math
Harmless(a,x) iff ∀e ∈ P : H(a,x,e) = 0
```

Where `P` is the set of protected entities/scopes under the analysis.

Equivalent future-space form:

```math
∀e ∈ P : μ_e(F_e(x')) ≥ μ_e(F_e(x))
```

under the transition from `x` to `x'`.

Strong harmlessness is rare in living systems because action and inaction both alter future-space.

```trace
absolute_harmlessness ≈ no_transition
```

---

## 5. Operational harmlessness

Real-world harmlessness must usually be weaker than strict harmlessness.

```math
Harmless_ε(a,x) iff ∀e ∈ P : H(a,x,e) ≤ ε_e
```

But bounded loss is not enough. The loss must remain correctable before irreversibility.

```math
Harmless_ε(a,x) iff ∀e ∈ P : H(a,x,e) ≤ ε_e AND T_det + T_route + T_corr < T_irr
```

Expanded TRACE form:

```trace
operationally_harmless :=
  bounded_loss
  + reversible_or_correctable
  + correction_channel_live
  + residue_not_hidden
  + no_irreversibility_breach
```

Guard:

```trace
low_visible_harm != harmless
```

---

## 6. Reversible and irreversible harm

Correction set:

```math
Corr_e(x') := { c : c can restore, reopen, compensate, or materially repair lost future-space for e after x' }
```

Reversible harm:

```math
H_e^rev iff ∃c ∈ Corr_e : Φ_e(F_e(c(x'))) ⪰ Φ_e(F_e(x))
```

Irreversible harm:

```math
H_e^irr iff ∀c ∈ Corr_e : Φ_e(F_e(c(x'))) ≺ Φ_e(F_e(x))
```

Clock form:

```math
H_e^irr iff T_det + T_route + T_corr ≥ T_irr
```

Correction arriving after irreversibility may still create a record, compensation, apology, sanction, or institutional learning. It does not restore the original future-space.

```trace
repair != time_reversal
```

---

## 7. Ethical action is not harmless action

Strict harmlessness is often unavailable.

```trace
ethical_action != harmless_action
```

Candidate operational form:

```trace
ethical_action :=
  minimise_irreversible_harm
  + preserve_correction
  + do_not_hide_residue
  + keep_affected_futures_in_the_map
```

This preserves dirty conflict rather than pretending all legitimate action is clean.

```trace
clean_action != action_with_no_visible_harm
```

---

## 8. Non-cancellation

Benefit to one scope does not erase harm to another.

```math
Σ Benefit_e > Σ Harm_e  ↛  ∀e : H_e = 0
```

TRACE form:

```trace
aggregate_benefit != local_harm_erasure
```

A transition may be justified, necessary, or least-bad while still harming a protected scope.

```trace
justified_harm != harmlessness
```

---

## 9. Laundered harm

Laundered harm occurs when a future-space reduction is relabelled as no harm, repair, consent, efficiency, clearance, safety, progress, or inevitability without preserving affected scope, correction, and residue.

```trace
laundered_harm :=
  H(a,x,e) > 0
  + record_claims H(a,x,e) = 0
  + residue_hidden_or_erased
```

Common laundering forms:

```trace
procedure_called_repair
consent_called_cleanliness
net_benefit_called_erasure
uncertainty_called_permission
visibility_called_answerability
framework_use_called_clearance
```

---

## 10. Minimal kernel

```trace
harm = future_space_collapse
harmless = no_protected_future_space_collapse
real_world_harmless = bounded_reversible_nonhidden_loss
ethical_action = minimise_irreversible_harm + preserve_correction + do_not_hide_residue
```

End.