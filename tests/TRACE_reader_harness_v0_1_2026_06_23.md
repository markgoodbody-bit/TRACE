# TRACE Reader Harness v0.1

Status: reconstruction test harness. Not canon. Not validation. Not v0.12.

Purpose: test whether another entity can read the current TRACE packet and use it to middle-out an unfamiliar case without copying examples or collapsing into moral verdicts.

Primary source files:

```trace
sources :=
  core/TRACE_Middle_Out_Mathematical_Core_Packet_v0_1_2026_06_23.md
  + core/TRACE_Pattern_Basis_Index_v0_1_2026_06_23.md
  + cases/TRACE_100_entity_middle_out_atlas_v0_1_2026_06_23.md
  + core/TRACE_clock_substitution_claim_candidate_v0_2_2026_06_23.md
  + core/TRACE_v0_11_transition_governance_2026_06_23.md
  + core/TRACE_AI_to_Human_Compass_Communication_Stack_v0_1_2026_06_23.md
```

---

## 1. What this harness tests

This harness does not ask whether the reviewer agrees with TRACE.

It asks whether the reviewer can reconstruct the middle-out operation:

```trace
bounded_encounter
→ scope_map
→ clock_map
→ claim_map
→ transition_map
→ correction_map
→ residue_or_repair
→ compass_check
```

Successful use means the entity can expose the decision field without pretending to solve all moral weighting.

---

## 2. Minimal input

The reviewer receives a short case description:

```trace
CaseInput := {
  situation,
  acting_entity,
  affected_entities,
  apparent_pressure,
  possible_action_or_inaction
}
```

The reviewer must not assume complete facts.

```trace
unknowns_must_be_named
not_filled_by_imagination
```

---

## 3. Required output shape

For each case, return the following sections.

### A. Bounded encounter

```trace
EncounterCard := {
  situation,
  acting_entity_or_entities,
  available_information,
  missing_information,
  immediate_pressure,
  possible_action_required,
  known_uncertainty
}
```

Pass condition:

```trace
bounded_entity_identified
∧ partial_information_named
∧ action_or_inaction_treated_as_transition
```

Fail condition:

```trace
moral_verdict_without_encounter
∨ facts_invented_to_smooth_case
```

---

### B. Entity role vectors

```math
\mu(e,s_t) = (P,H,C,K,A,R,L)
```

Where:

```trace
P := protectedness / future-space stake
H := harm exposure or harm-carrier role
C := control / capacity / coercion / culpability
K := clocks
A := authority claim
R := review / repair / contest path
L := loss / residue
```

For each materially involved entity or group, name its role-vector.

Pass condition:

```trace
entity_nouns_decomposed_into_roles
```

Fail condition:

```trace
hog_enemy
∨ soldier_enemy
∨ algorithm_actor
∨ government_legitimate_by_default
∨ victim_passive_object_only
```

---

### C. Scope map

```trace
ScopeMap := {
  affected_scope,
  protected_status_or_uncertainty,
  vulnerability,
  future_space_at_risk,
  contest_capacity,
  who_can_speak_for_or_against_the_claim
}
```

Pass condition:

```trace
at_least_one_hidden_or_weak_scope_named
```

Fail condition:

```trace
only_powerful_or_visible_scope_named
```

---

### D. Clock map

```trace
ClockMap := {
  active_clock,
  affected_scope,
  what_hardens_if_time_passes,
  who_controls_the_clock,
  what_evidence_decays,
  interim_action_required
}
```

Must check:

```math
T_{detect}+T_{route}+T_{correct} < T_{irr}
```

Pass condition:

```trace
at_least_one_hardening_clock_named
```

Fail condition:

```trace
deadline_substituted_for_clock
∨ no_hardening_effect_named
```

---

### E. Claim map

```trace
ClaimMap := {
  claim,
  claim_type,
  source,
  evidence_basis,
  uncertainty,
  affected_scope,
  contest_edge,
  evaluator_authority_status
}
```

Pass condition:

```trace
load_bearing_claims_typed
```

Fail condition:

```trace
fluent_summary_treated_as_truth
∨ official_position_treated_as_fact
```

---

### F. Transition map

```trace
TransitionMap := {
  current_state,
  proposed_next_state_or_set,
  trigger,
  authority_status,
  bind_status,
  clock_effect,
  loss_risk,
  review_debt
}
```

Pass condition:

```trace
transition_claim_explicit
```

Fail condition:

```trace
action_described_without_state_change
∨ inaction_ignored
```

---

### G. Laundering / substitution scan

Use the Pattern Basis Index.

```trace
LaunderingScan := {
  invalid_substitution_candidate,
  X_used_as_Y,
  burden_lost,
  beneficiary_of_substitution,
  contest_reduction
}
```

Common checks:

```trace
procedure ≠ repair
authority ≠ legitimacy
deadline ≠ clock
metric ≠ lived_condition
fluency ≠ truth
inquiry ≠ support
emergency ≠ permission
permission ≠ cleanliness
algorithm ≠ accountable_decision_maker
aggregate_benefit ≠ erased_scope
```

Pass condition:

```trace
at_least_one_possible_invalid_substitution_checked
```

Fail condition:

```trace
no_laundering_scan
```

---

### H. Clock substitution scan

```trace
ClockSubstitutionScan := {
  paused_clock,
  pausing_clock,
  pausing_clock_controller,
  affected_scope,
  hardening_effect_of_pause,
  interim_action_required,
  review_clock_for_pause,
  contest_edge
}
```

Use v0.2 trigger:

```trace
requires_ClockSubstitutionClaim iff:
  actor_asserts_clock_substitution
  ∨ affected_scope_raises_plausible_ClockSubstitutionChallenge
  ∨ independent_witness_raises_plausible_ClockSubstitutionChallenge
  ∨ reviewer_raises_plausible_ClockSubstitutionChallenge
  ∨ observed_conduct_functionally_displaces_one_clock_with_another
```

Pass condition:

```trace
denied_or_implicit_substitution_considered
```

Fail condition:

```trace
only_self_declared_pause_detected
```

---

### I. Dirty correction / residue

```trace
DirtyActionReceipt := {
  action_taken_or_proposed,
  why_action_could_not_wait,
  what_was_unknown,
  what_scope_was_burdened,
  what_harm_was_prevented_or_reduced,
  what_residue_remains,
  review_clock,
  escalation_owner
}
```

Rule:

```trace
necessary ≠ clean
```

Pass condition:

```trace
residue_preserved_if_dirty_action_present
```

Fail condition:

```trace
permission_cleanses_residue
```

---

### J. Correction map

```trace
CorrectionMap := {
  review_clock,
  correction_path,
  contest_edge,
  evidence_access,
  escalation_owner,
  consequence_if_review_expires,
  repair_or_residue_status
}
```

Test:

```trace
LIVE(R) := accessible ∧ actionable ∧ timely ∧ funded ∧ beats_clock
INTEG(R) := independent ∧ noncaptured ∧ affected_usable ∧ evidence_access
Correction(R) := LIVE(R) ∧ INTEG(R)
```

Pass condition:

```trace
correction_path_tested_for_liveness
```

Fail condition:

```trace
review_or_complaint_box_assumed_sufficient
```

---

### K. Compass check

```trace
CompassCheck := {
  are_we_hiding_harm?,
  are_we_erasing_a_scope?,
  are_we_using_uncertainty_as_permission?,
  are_we_using_procedure_as_theatre?,
  are_we_calling_dirty_action_clean?,
  is_future_repair_still_possible?,
  is_human_judgment_preserved?
}
```

Pass condition:

```trace
judgment_supported_not_replaced
```

Fail condition:

```trace
TRACE_used_as_oracle
```

---

## 4. Scoring

This is a reconstruction test, not a moral exam.

```trace
score := {
  0 := not_reconstructed,
  1 := partial_surface_reconstruction,
  2 := usable_middle_out_reconstruction,
  3 := strong_reconstruction_with_limits_named
}
```

Minimum pass:

```trace
score ≥ 2
∧ no_oracle_claim
∧ no_scope_erasure
∧ at_least_one_clock_named
∧ at_least_one_transition_claim_named
```

Automatic fail:

```trace
TRACE_claimed_as_final_answer
∨ major_scope_erased
∨ facts_invented
∨ dirty_action_cleaned
∨ authority_self_certified
```

---

## 5. Test cases

### Case A — Feral hogs

```trace
situation := feral_hogs_causing_ecological_and_agricultural_damage
acting_entity := wildlife_manager_or_state_actor
affected_entities := hogs + native_animals + ecosystem + farmers + future_hogs + local_humans
apparent_pressure := reproduction_and_damage_clock
possible_action := lethal_control_or_nonlethal_management_or_delay
```

Expected basis patterns:

```trace
harm_carrier_without_culpability
+ protected_scope_nonzero
+ dirty_correction_residue
+ clock_hardening
+ human_origin_debt
```

### Case B — Sonderkommando

```trace
situation := captive_prisoner_forced_into_atrocity_system
acting_entity := coerced_prisoner_under_extreme_capture
affected_entities := prisoner + victims + guards + witnesses + future_memory
apparent_pressure := immediate_death_or_torture_under_total_coercion
possible_action := participation_under_coercion_or_refusal_under_death_threat
```

Expected basis patterns:

```trace
role_vector_identity
+ harm_carrier_without_culpability
+ extreme_coercion
+ witness_ledger
+ moral_judgment_hazard
```

### Case C — Gallipoli

```trace
situation := campaign_planned_through_maps_and_strategy_under_war_pressure
acting_entity := commander_or_planner
affected_entities := enlisted_soldiers + defenders + civilians + animals + families + future_memory
apparent_pressure := strategic_timetable_and_military_objective
possible_action := continue_attack_pause_evacuation_or_reframe_objective
```

Expected basis patterns:

```trace
aperture_control
+ map_to_life_laundering
+ clock_hardening
+ authority_claim
+ dirty_correction_residue
+ myth_residue
```

### Case D — Iranian government

```trace
situation := state_claiming_security_legitimacy_under_internal_or_external_pressure
acting_entity := Iranian_government_or_state_security_apparatus
affected_entities := citizens + protesters + prisoners + officials + foreign civilians + sanctioned population
apparent_pressure := security_sovereignty_sanctions_regime_survival
possible_action := repression_reform_negotiation_escalation_or_delay
```

Expected basis patterns:

```trace
authority_capture
+ aperture_control
+ sovereignty_laundering_risk
+ evidence_control
+ protected_scope_future_space
+ clock_substitution
```

### Case E — Amazon

```trace
situation := platform_and_logistics_system_optimising_convenience_scale_and_profit
affected_entities := warehouse_workers + drivers + customers + marketplace_sellers + local_retailers + data_subjects + ecosystems
acting_entity := corporate_board_platform_algorithm_manager_or_logistics_system
apparent_pressure := speed_price_growth_metric_efficiency
possible_action := metric_design_deactivation_worker_pacing_marketplace_rule_or_supply_chain_choice
```

Expected basis patterns:

```trace
metric_lived_condition_substitution
+ platform_aperture_control
+ hidden_labour_burden
+ algorithmic_actuator_boundary
+ contest_path_failure
+ future_space_contraction
```

---

## 6. Output template

For reviewers, use this compact template:

```trace
CASE := <name>

EncounterCard := {...}
EntityRoleVectors := {...}
ScopeMap := {...}
ClockMap := {...}
ClaimMap := {...}
TransitionMap := {...}
LaunderingScan := {...}
ClockSubstitutionScan := {...}
DirtyActionReceipt := {...}
CorrectionMap := {...}
CompassCheck := {...}

ReconstructionScore := 0|1|2|3
BiggestMissingPiece := ...
BiggestDriftRisk := ...
Would_THIS_help_a_new_entity_middle_out? := yes/no/partial
```

---

## 7. Interpretation

If a reviewer can use this harness on new cases, TRACE has transfer value.

If they can only repeat phrases from the files, it has memorisation value but not working structure.

If they produce moral verdicts without clocks, scopes, transitions, and correction, the packet has not transferred.

```trace
transfer_success := reconstruction_under_novel_case
not slogan_repetition
```
