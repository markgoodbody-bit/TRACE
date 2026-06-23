# TRACE Feral Hogs / Dirty Correction Multi-Scope Test v0.1

Status: sandbox/case pressure test. Not canon. Not v0.12. Not a wildlife policy recommendation. No empirical claims are relied on beyond the stylised case structure.

Purpose: test whether TRACE can handle a case where every available correction route harms some protected scope, and where the harm-carrier is sentient, adaptive, non-evil, and partly produced by human-created conditions.

```trace
case := feral_hogs_dirty_correction
claim_status := stylised_pressure_test
```

---

## 1. Why this case matters

This is not a simple pest-control case.

```trace
feral_hogs :=
  sentient_adaptive_agents
  + protected_scope_nonzero
  + harm_carriers
  + not_moral_culprits
  + reproduction_accelerated_hardening_clock
  + human_origin_debt_present
```

Two bad simplifications are blocked:

```trace
bad_1 := treat_hogs_as_enemy
bad_2 := treat_sentience_as_absolute_veto
```

Both fail.

```trace
treat_hogs_as_enemy → innocence_erasure
sentience_as_absolute_veto → ecosystem_and_other_scope_erasure
```

The case forces TRACE to hold several truths at once:

```trace
truths :=
  hogs_can_suffer
  ∧ hogs_are_not_culpable
  ∧ hogs_can_carry_real_harm
  ∧ inaction_can_harden_damage
  ∧ correction_can_harm_hogs
  ∧ human_systems_helped_create_the_condition
```

---

## 2. Protected scopes

Minimum scope map:

```trace
protected_scopes := {
  hogs,
  native_animals,
  ecosystems,
  farmers_or_landholders,
  local_humans,
  future_hogs,
  future_ecological_communities,
  human_institutions_responsible_for_land_management
}
```

Scope status:

```trace
hogs.scope_status := protected_scope_nonzero
native_animals.scope_status := protected_scope_nonzero
ecosystems.scope_status := protected_system_scope_candidate
humans.scope_status := protected_scope
future_entities.scope_status := future_scope_candidate
```

Important boundary:

```trace
protected_scope_nonzero ≠ absolute_veto
harm_carrier ≠ enemy
innocence ≠ no_correction
```

---

## 3. Human-origin debt

The hogs case is dirty before the decision-maker arrives.

```trace
human_origin_debt :=
  human_introduction_or_escape
  ∨ habitat_change
  ∨ failed_containment
  ∨ land_use_change
  ∨ selective_pressure_created_by_prior_management
  ∨ institutional_delay
```

This matters because correction burden must not be laundered entirely onto the hogs.

```trace
human_origin_debt
→ recurrence_prevention_required
→ residue_ledger_required
→ no_clean_pest_language
```

If humans created or amplified the condition, killing or harming hogs cannot be described as simple moral cleansing.

```trace
human_caused_condition + harm_to_hogs
→ dirty_correction_residue
```

---

## 4. Active clocks

```trace
active_clocks :=
  reproduction_clock
  + ecosystem_damage_clock
  + native_animal_suffering_clock
  + crop_or_livelihood_clock
  + disease_or_safety_clock_if_applicable
  + hog_suffering_clock
  + evidence_uncertainty_clock
  + prevention_reform_clock
```

Clock meanings:

```trace
reproduction_clock := time_until population_growth_makes_later_correction_more_harmful

ecosystem_damage_clock := time_until habitat / soil / water / vegetation damage hardens

native_animal_suffering_clock := time_until predation / competition / displacement / injury worsens

crop_or_livelihood_clock := time_until human livelihood / food / land burden hardens

hog_suffering_clock := suffering_created_by_control_method_or_unmanaged_population_condition

prevention_reform_clock := time_until human-side recurrence causes continue producing same problem
```

Core time pressure:

```trace
waiting_can_reduce_direct_harm_to_hogs_now
but_increase_total_future_harm_to_hogs_and_others
```

---

## 5. Clock substitution risks

Clock substitution applies sharply here.

```trace
bad_delay :=
  study_clock pauses containment_clock
  while reproduction_clock accelerates
```

```trace
bad_emergency :=
  emergency_clock overrides welfare_review_forever
```

Required claim when one clock pauses another:

```trace
ClockSubstitutionClaim required iff:
  study_clock pauses containment_clock
  ∨ emergency_clock pauses welfare_review_clock
  ∨ budget_clock pauses prevention_reform_clock
  ∨ political_clock pauses ecological_damage_clock
```

Minimum form:

```trace
ClockSubstitutionMinimum := {
  paused_clock,
  pausing_clock,
  pausing_clock_controller,
  hardening_effect_of_pause,
  review_clock_for_pause,
  contest_edge
}
```

---

## 6. Action set

Candidate action families:

```trace
action_families :=
  prevention
  + exclusion_or_fencing
  + fertility_control_if_feasible
  + relocation_if_nonharmful_and_nonspreading
  + targeted_lethal_control
  + broad_lethal_control
  + do_nothing
  + habitat_or_food_source_modification
  + human_system_reform
```

Do not treat `do_nothing` as clean.

```trace
do_nothing := action_channel
```

Do not treat lethal control as clean.

```trace
lethal_control := dirty_correction_candidate
```

Do not treat nonlethal control as automatically adequate.

```trace
nonlethal_control := preferred_if_beats_clock
not_preferred_if_symbolic_and_too_slow
```

---

## 7. Dirty correction gate

Dirty correction is correction that prevents or reduces one harm pathway by imposing harm on another protected or partly protected scope.

```trace
DirtyCorrection :=
  correction_action a
  such_that:
    reduces material_harm_to_scope_set S1
    ∧ imposes material_harm_on_scope_set S2
    ∧ S2 has protected_scope_status_nonzero
```

Dirty correction may be considered only if:

```trace
DirtyCorrectionGate opens iff:
  material_harm_clock_active
  ∧ affected_scopes_named
  ∧ human_origin_debt_logged
  ∧ nonlethal_routes_tested_or_shown_too_slow
  ∧ chosen_method_minimises_suffering_given_clock
  ∧ recurrence_prevention_plan_exists
  ∧ review_clock_set
  ∧ contest_edge_available
  ∧ residue_ledger_open
```

It closes if:

```trace
DirtyCorrectionGate closes iff:
  harm_to_hogs_is_denied
  ∨ hogs_are_named_as_enemy_or_waste
  ∨ nonlethal_routes_are_ignored_without_clock_reason
  ∨ human_origin_debt_is_erased
  ∨ urgency_is_used_to_bypass_review_indefinitely
  ∨ method_choice_maximises_suffering_for_convenience
  ∨ no_recurrence_prevention_path
```

---

## 8. Residue ledger

Even justified dirty correction remains dirty.

```trace
residue :=
  harm_to_hogs
  + uncertainty_about_suffering
  + human_origin_debt
  + lost_future_space_for_killed_or_harmed_animals
  + ecological_uncertainty
```

Ledger rule:

```trace
if hogs_harmed:
  record "we harmed/killed sentient animals to prevent these specified harms"
```

Forbidden phrasing:

```trace
"pest removal" as moral erasure
"resource management" as suffering erasure
"invasive" as standing erasure
```

Acceptable compression:

```trace
"dirty correction under residue"
```

---

## 9. Future-space analysis

For each protected scope `l`:

```trace
F_l(t) := possible_future_set_available_to_scope_l_at_time_t
```

Relevant future-space collapses:

```trace
F_hogs := life / welfare / social behaviour / reduced suffering / non-recurrence of harmful human-created cycles

F_native_animals := habitat / survival / reproduction / reduced predation or displacement

F_ecosystem := regenerative capacity / biodiversity / soil-water integrity / resilience

F_humans := safety / livelihood / food / land stewardship / institutional trust
```

Dirty correction compares not one life against one system, but multiple future-space collapses under time.

```trace
compare := ΔF_l across scopes under action and inaction
```

But no scalar aggregation may erase protected lower scopes.

```trace
aggregate_benefit ≠ residue_erasure
```

---

## 10. Middle-out route

```trace
hogs_middle_out_route :=
  identify_scope_set
  → mark_hogs_protected_scope_nonzero
  → mark_other_affected_scopes
  → log_human_origin_debt
  → identify_active_clocks
  → identify_clock_substitution_risks
  → test_nonlethal_routes_against_clocks
  → if_insufficient_open_DirtyCorrectionGate
  → choose_least_suffering_method_that_beats_material_clock
  → set_review_clock
  → keep_residue_ledger_open
  → implement_recurrence_prevention
```

Plain English compression:

Do not pretend the hogs are evil. Do not pretend the damage is imaginary. Do not pretend inaction is harmless. Do not pretend killing is clean. Choose the least-cruel correction that can actually beat the harm clock, and record the residue.

---

## 11. What this case tests in TRACE

```trace
tests :=
  protected_scope_nonzero
  + harm_carrier_without_culpability
  + human_origin_debt
  + reproduction_as_hardening_clock
  + nonlethal_symbolism_vs_clock_reality
  + dirty_correction_gate
  + residue_ledger
  + cross_scope_future_space_collision
```

---

## 12. Remaining unsolved wound

This case is not solved.

The unresolved kernel-level wound remains:

```trace
cross_scope_priority_when_all_routes_are_dirty := unresolved
```

TRACE can currently discipline the decision, expose false cleanliness, and require review and residue.

It cannot yet provide a final moral conversion rate between:

```trace
hog_life_and_welfare_interest
vs
ecosystem_future_space
vs
native_animal_suffering
vs
human_livelihood_and_safety
```

This is not failure. It is an honest boundary.

```trace
honest_result := dirty_decision_disciplined_not_absolved
```

---

## 13. Candidate reviewer questions

```trace
review_questions :=
  does DirtyCorrectionGate reduce cruelty_or_hide_it?
  does protected_scope_nonzero have enough teeth?
  does human_origin_debt create useful obligation_or_empty_guilt?
  does residue_ledger change action_or_only_language?
  does this outperform ordinary invasive_species_policy_language?
```

---

## 14. Compression

```trace
feral_hogs_case_v0_1 :=
  sentient_nonculpable_harm_carrier
  + human_origin_debt
  + reproduction_clock
  + multi_scope_future_space_collision
  + dirty_correction_gate
  + residue_ledger
  + unresolved_cross_scope_priority
```

Status:

```trace
case_pressure_test := active
kernel_patch := no
public_claim := no
next_step := hostile_review_or_comparator_against_ordinary_policy_language
```
