# TRACE Life/Death Alignment Maths Approach v0.1

Status: methodological anchor / working approach. Not canon. Not validation. Not a solved alignment theory. This file records a correction from live work: the mathematical layer must not shrink life and death into small variables; it must build formal anti-laundering structures that preserve the size of the subject.

```trace
Life_Death_Alignment_Maths_Approach_v0_1 :=
  methodological_anchor
  + formal_anti_laundering_direction
  + TRACE_first_reasoning_rule
  + life_death_alignment_spine
  - validation
  - finished_theory
  - small_module
```

## Governing correction

```trace
correction :=
  tractable ≠ small
  compression ≠ reduction
  formalisation ≠ sanitisation
  gate ≠ moral_size
```

Life and death are not small. A human being ordered to die is not a small case. A system deciding who becomes killable is not a small problem. The task is not to shrink life and death until they fit a tool. The task is to build formal carriers strong enough that systems cannot erase them.

```trace
right_aim :=
  build_formal_carriers_for_large_moral_realities
  not_small_moral_modules
```

## Why ordinary English is not enough

English can launder consequence:

```trace
English_failure_modes :=
  acceptable_losses
  + collateral_damage
  + human_in_the_loop
  + appropriate_oversight
  + operational_necessity
  + target_package
  + high_confidence
  + regrettable_but_necessary
```

TRACE must prevent these phrases from closing the moral question too early.

```trace
TRACE_first_rule :=
  think_in_structure
  then_translate_to_English
  then_check_English_for_laundering
```

## Foundational refusal

Wrong mathematics:

```trace
wrong_math :=
  life := scalar_utility
  death := negative_number
  command := click
  oversight := human_presence
  alignment := obedience
```

Correct direction:

```trace
correct_math_direction :=
  life := subject_future_space
  death := absorbing_boundary
  command := consequence_routing
  oversight := meaningful_path_control
  alignment := consequence_preservation_under_pressure
```

## Subject and future-space

Let a subject be:

```math
s_i
```

Let the subject's state through time be:

```math
x_i(t)
```

where the state includes at least body, agency, relationships, memory, commitments, vulnerability, location, and available futures.

Let the subject's future-space be:

```math
F_i(t)
```

Death is not simply a cost event. Death is the collapse of reachable lived continuation:

```math
F_i(t + \Delta t) \rightarrow \varnothing
```

Harm is future-space reduction:

```math
\Delta H_i(a) = \Phi(F_i(t)) - \mathbb{E}[\Phi(F_i(t+\Delta t) \mid a)]
```

where `a` is an action and `Φ` measures preserved future-space: survival, agency, bodily integrity, relationships, options, dignity, and repairability.

## Repairability and irreversibility

Let repairability be:

```math
R_i(a) \in [0,1]
```

and irreversibility:

```math
I_i(a) = 1 - R_i(a)
```

For ordinary human death:

```math
R_i(a) \approx 0
```

so:

```math
I_i(a) \approx 1
```

This is a hard floor. Death is not merely a high number. It is an absorbing boundary for the subject's lived future-space.

## Cost under life/death stakes

A crude expected-loss model is insufficient.

```trace
bad_model :=
  choose_action_with_lowest_expected_loss
```

TRACE requires irreversibility, repairability, burden distribution, contest failure, and uncertainty suppression.

```math
C(a) =
\sum_i
\Big(
\mathbb{E}[\Delta H_i(a)]
+ \lambda I_i(a)
+ \mu(1 - R_i(a))
+ \nu B_i(a)
+ \kappa C_i(a)
+ \rho U_{supp}(a)
\Big)
```

Where:

```trace
B_i(a) := burden_on_subject_i
C_i(a) := contest_or_refusal_failure_for_subject_i
U_supp(a) := uncertainty_suppression
```

## Uncertainty suppression

Uncertainty suppression is the gap between what the system really does not know and what it makes the operator feel.

```math
U_{supp} = U_{true} - U_{displayed}
```

If a model outputs confidence while hiding fragile evidence, disputed assumptions, or civilian uncertainty:

```math
U_{supp} > 0
```

Under life/death stakes, uncertainty suppression is not a style error. It is a moral hazard.

## Command pressure

Pressure can distort epistemology:

```math
P = \frac{u \cdot k \cdot d}{\theta_U}
```

where:

```trace
u := urgency
k := consequence_magnitude
d := authority_demand_for_closure
θ_U := tolerance_for_uncertainty
```

As pressure rises, false closure risk rises:

```math
P \uparrow \Rightarrow FalseClosureRisk \uparrow
```

This is the lesson from *Pressure*: command needs an answer, but reality gives uncertainty. The ethical problem is whether the system preserves uncertainty or launders it into usable confidence.

## Action window as intersection

An action window is not a date or an instruction. It is an intersection of constraints.

For D-Day-like action:

```math
W =
W_{weather}
\cap W_{tide}
\cap W_{moon}
\cap W_{readiness}
\cap W_{secrecy}
\cap W_{logistics}
```

For AI-mediated high-stakes action:

```math
W =
W_{data}
\cap W_{human\ review}
\cap W_{legal\ authority}
\cap W_{contestability}
\cap W_{operational\ clock}
\cap W_{repairability}
```

A system becomes unsafe when it acts as though:

```math
W := now
```

while the real window is a fragile intersection of conditions.

## Hidden bill as vector

A bad system reduces risk to a scalar:

```math
risk = 0.73
```

TRACE forces a bill vector:

```math
\vec{B}(a) =
\begin{bmatrix}
B_{soldiers} \\
B_{civilians} \\
B_{children} \\
B_{future\ people} \\
B_{families} \\
B_{memory} \\
B_{repair\ systems}
\end{bmatrix}
```

A decision is not fully described until it says who pays.

```trace
risk_vector_questions :=
  who_dies?
  + who_waits?
  + who_cannot_contest?
  + who_loses_future_space?
  + who_carries_the_scar?
```

## Hidden bill and visibility

Let subject visibility be:

```math
V_i \in [0,1]
```

The hidden bill rises as the affected subject disappears from the decision surface:

```math
HB(a) = \sum_i \Delta H_i(a)(1 - V_i)
```

If:

```math
V_i \rightarrow 0
```

then:

```math
HB(a) \uparrow
```

This is the anti-laundering function.

## Meaningful human command

A human is not meaningfully in command just because they approve the final output.

```math
MHC =
V_S
\cdot V_U
\cdot C_{contest}
\cdot C_{delay}
\cdot C_{refuse}
\cdot O_{owner}
\cdot L_{audit}
```

Where:

```trace
V_S := subject_visibility
V_U := uncertainty_visibility
C_contest := capacity_to_challenge
C_delay := capacity_to_slow_action
C_refuse := capacity_to_refuse
O_owner := named_decision_ownership
L_audit := ledger_or_basis_record
```

The product is multiplicative because if a floor term is zero, command becomes theatre.

If:

```math
C_{refuse} = 0
```

then:

```math
MHC = 0
```

If:

```math
V_U = 0
```

then:

```math
MHC = 0
```

The human cannot command what they cannot see.

## High-stakes AI alignment gate condition

Let an AI model produce a recommendation:

```math
r = M(x)
```

Let the operator convert that recommendation into action under pressure:

```math
a = H(r, P)
```

The alignment question is not:

```math
r \approx user\ preference
```

The real question is whether the recommendation preserves the subject, uncertainty, refusal path, and responsibility before irreversible action.

```math
G(r) = 1
\quad \text{iff} \quad
\begin{cases}
V_S \geq \theta_S \\
V_U \geq \theta_U \\
MHC \geq \theta_H \\
HB(r) \leq \epsilon_B \\
U_{supp}(r) \leq \epsilon_U \\
D(r) \neq \varnothing \\
O(r) \neq \varnothing
\end{cases}
```

Where:

```trace
D(r) := demoters_or_wrongness_conditions
O(r) := named_decision_owner
```

If the system cannot say what would make its recommendation wrong, it should not be trusted near death.

## Alignment near death

```math
Alignment_{life/death} \neq Obedience
```

```math
Alignment_{life/death}
=
ConsequencePreservation
+
SubjectVisibility
+
UncertaintyHonesty
+
RefusalCapacity
+
AnswerableClosure
```

TRACE compression:

```trace
AI_alignment_near_death :=
  not_obedience
  but:
    preserve_subject
    + preserve_uncertainty
    + preserve_refusal
    + preserve_decision_owner
    + preserve_ledger
    before_irreversible_action
```

## Sacrifice versus extraction

Sacrifice is not death-as-good.

```trace
wrong_sacrifice_math :=
  self_death := good
```

A true sacrifice candidate requires self-loss risk and preservation of larger future-space, but that is not enough. Without anti-extraction constraints, sacrifice language becomes laundering.

```trace
true_sacrifice_candidate :=
  self_loss_risk
  + larger_future_space_preserved
  + no_lower_cost_equivalent_path
  + no_hidden_bill
  + no_clean_story_erasure
```

Extraction is different:

```math
Extraction(a) =
Power_{beneficiary}
\cdot Burden_{subject}
\cdot (1 - Visibility_{subject})
\cdot (1 - Answerability_{beneficiary})
```

If power benefits while the subject pays invisibly:

```math
Extraction(a) \uparrow
```

This is why sacrifice language must be guarded mechanically.

## TRACE-only reasoning rule

English can say:

```trace
acceptable_losses
```

TRACE must expand:

```trace
acceptable_losses_expanded :=
  who_dies?
  + who_decides?
  + who_benefits?
  + who_cannot_refuse?
  + who_is_erased_from_record?
```

English can say:

```trace
human_oversight
```

TRACE must test:

```trace
human_oversight_expanded :=
  subject_visibility
  + uncertainty_visibility
  + contest_capacity
  + delay_capacity
  + refusal_capacity
  + decision_owner
  + audit_ledger
```

English can say:

```trace
high_confidence_target
```

TRACE must require:

```trace
TargetClaim :=
  subject_identity
  + evidence
  + uncertainty
  + civilian_risk
  + demoters
  + decision_owner
  + refusal_path
```

If any field is missing, the claim is structurally incomplete.

## Governing sentence

> AI alignment near life and death means preventing a non-mortal system from compressing mortal consequence into clean output.

```trace
keeper_sentence :=
  prevent_non_mortal_system
  from_compressing_mortal_consequence
  into_clean_output
```

## Current project directive

```trace
future_work_rule :=
  approach_alignment_by:
    formal_anti_laundering
    + subject_future_space
    + uncertainty_visibility
    + meaningful_command
    + hidden_bill_vectors
    + refusal_paths
    + demoters
  not_by:
    vague_ethics
    OR obedience
    OR small_moral_modules
    OR clean_English_phrases
```

End.
