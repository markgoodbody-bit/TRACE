# TRACE Primitive Transition Grammar v0.1

Status: candidate primitive formalisation layer. Not canon. Not validation. Not proof. Not permission. Not a public front door.

Purpose: formalise the middle-out origin sequence underneath TRACE and Mechanical Ethics: an entity exists, opens its eyes, perceives partially, acts or does not act, changes the world, affects other future-spaces, and thereby makes harm, care, correction, residue, power, responsibility, and answerability possible.

```trace
primitive_transition_grammar_v0_1 :=
  existence
  + aperture
  + partial_information
  + action_or_inaction
  + transition
  + other_entities
  + affected_future_space
  + harm
  + care
  + correction
  + residue
  + power
  + answerability
  - moral_oracle
  - permission_machine
  - validation
```

---

## 0. Method guard

Do not begin with morality, law, rights, utility, virtue, compliance, or authority.

Begin with a transition field.

```trace
middle_out_start :=
  something_is_here
  + it_perceives_partially
  + it_can_change_something
  + it_does_not_know_everything
  + time_passes
  + other_things_continue
  + actions_interfere
```

Ethics appears only after action under uncertainty can alter futures not wholly owned by the actor.

---

## 1. Entity

An entity exists.

```math
e ∈ E
```

This does not yet settle personhood, moral patienthood, responsibility, sentience, or rights.

```trace
entity_exists != moral_status_resolved
```

---

## 2. Aperture / partial perception

The entity has an aperture onto the world. It receives only partial information.

```math
I_e(t) ⊂ Ω
```

Where `Ω` is the relevant condition-space.

No entity is assumed omniscient.

```trace
partial_information := default_condition
```

Guard:

```trace
unknown != permission
```

---

## 3. Action and inaction

The entity has an available action field.

```math
a_e(t) ∈ A_e(t)
```

Inaction is included where delay, omission, refusal, non-response, or non-routing changes future-space.

```trace
inaction := transition_channel
```

---

## 4. Transition

An action or inaction changes world-state.

```math
x_t --a_e--> x_{t+1}
```

Under uncertainty, the transition usually maps to a set or distribution of possible future states.

```math
δ : S × A -> P(S)
```

or:

```math
x' ~ P(. | x,a)
```

---

## 5. Other

Ethics begins when another entity or protected scope exists and can be affected.

```math
∃o ∈ E : o ≠ e
```

The first moral discovery is not a rule. It is another future entering the map.

```trace
first_moral_discovery := another_future_exists
```

---

## 6. Future-space

For an entity or protected scope `o`, future-space is the set of reachable future trajectories from a state.

```math
F_o(x) := { γ : γ is a reachable future trajectory for o from x }
```

Future-space is not raw option count. It must be read as viable future-space.

```trace
viable_future_space :=
  orientation
  + relation
  + usable_capacity
  + repairability
  + meaningful_constraint
```

Guard:

```trace
more_options != better_future
fewer_options != automatic_harm
```

---

## 7. Interference

The actor's transition may alter another scope's future-space.

```math
a_e(t) ⇒ ΔF_o(t)
```

or:

```math
F_o(x_{t+1}) ≠ F_o(x_t)
```

Ethics emerges because affected futures are not always compatible.

```trace
ethics_emerges := unavoidable_interference_under_uncertainty
```

---

## 8. Harm

Harm is protected future-space reduction under transition.

```math
H(a,x,o) := [ μ_o(F_o(x)) - E_{x' ~ P(. | x,a)} μ_o(F_o(x')) ]_+
```

Compact form:

```trace
H_o := Δ⁻F_o
```

Harm is not identical to pain, blame, illegality, offence, or visible suffering.

```trace
harm != pain
harm != culpability
harm != procedural_defect_only
```

---

## 9. Harmlessness

Strong harmlessness means no protected future-space reduction for any protected scope.

```math
Harmless(a,x) iff ∀o ∈ P : H(a,x,o) = 0
```

Operational harmlessness under real-world conditions is weaker:

```trace
operationally_harmless :=
  bounded_loss
  + reversible_or_correctable
  + correction_channel_live
  + residue_not_hidden
  + no_irreversibility_breach
```

---

## 10. Care

Empathy models another future. Care constrains action by that future.

```math
Empathy(e,o,t) := Model_e(S_o(t), F_o(t), H_o(t))
```

```math
Care(e,o,t) iff F_o(t) ↪ Decision_e(t)
```

Care is not sentiment. Care is chosen loss of permission because another future has entered the map.

```trace
care := another_future_becomes_constraint
```

---

## 11. Correction

Correction matters because time can close paths.

```math
T_det + T_route + T_corr < T_irr
```

If correction arrives after irreversibility, it may still matter, but it does not restore the original future-space.

```trace
late_correction != time_reversal
```

---

## 12. Residue

Residue is what remains because repair is not an inverse operation.

```math
Repair ∘ Harm ≠ Identity
```

TRACE form:

```trace
residue := failed_inverse + path_dependence + time_hardening + unrecovered_future_space
```

Guard:

```trace
recorded_residue != addressed_residue
case_closed != harm_repaired
```

---

## 13. Power

Power is the capacity to alter future-space one does not own.

```math
Power(e,o,t) := Capacity_e(ΔF_o(t)) where e ≠ o
```

Power increases the burden of answerability.

```trace
more_power -> less_self_trust_credit
```

---

## 14. Responsibility

Responsibility is not identical to causation. It depends on role in transition.

```math
Resp_i := Control_i × Foreseeability_i × Authority_i × CorrectionCapacity_i
```

Expanded candidate vector:

```trace
responsibility_factors :=
  causal_role
  + control
  + foreseeability
  + authority
  + benefit
  + correction_capacity
  + concealment_or_disclosure
```

Guard:

```trace
causal_contact != full_responsibility
no_intent != no_responsibility
```

---

## 15. Answerability

Answerability becomes necessary when power changes futures it does not own, especially when an actor uses a record, framework, process, or moral language as trust material.

```trace
if_power_uses_TRACE_ME_as_credit:
  actor_self_application := claim_packet
  not_clearance
  not_good_faith_evidence
  not_answerability
```

A live challenge channel requires more than a process existing.

```trace
valid_challenge_channel :=
  reachable
  + affordable
  + safe_to_use
  + evidence_access
  + time_before_hardening
  + non_actor_scope_setting
  + enforcement_or_delay_power
```

---

## 16. Full sequence

```trace
entity_exists
-> aperture_opens
-> partial_world_model
-> action_or_inaction
-> transition
-> other_futures_affected
-> future_space_change
-> harm_or_preservation
-> care_or_indifference
-> correction_or_hardening
-> residue
-> responsibility
-> power_answerability
```

The first moral sentence:

```trace
another_future_has_entered_the_map
```

The second:

```trace
my_action_can_reduce_it
```

The third:

```trace
if_I_reduce_it_I_must_not_call_that_clean
```

---

## 17. Minimal kernel

```trace
TRACE := seeing_transition_fields
ME := holding human constraints under uncertainty
harm := future_space_reduction
care := another_future_as_constraint
correction := repair_before_irreversibility
residue := repair_not_time_reversal
power := capacity_to_change_futures_not_owned
answerability := material challenge to power's record
```

End.