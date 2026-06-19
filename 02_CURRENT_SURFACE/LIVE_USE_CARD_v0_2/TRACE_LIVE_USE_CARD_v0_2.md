# TRACE Live Use Card v0.2

Status: front-door use instrument / live reasoning surface / not validation / not proof / not governance certification.

Purpose: give a human or AI a compact way to use TRACE on a real situation in minutes. This card does not claim TRACE beats domain experts. It tests whether TRACE makes relevant structure available in context for live reasoning and correction.

Patch basis from v0.1: hidden-data scenario battery exposed four live-use defects: (1) diagnosing but not closing a cheap reversible fix, (2) under-specifying unknown-object hazard handling, (3) treating an unavailable person as no knowledge carrier, and (4) reassigning a scarce actor without checking what harm their current task is containing.

```trace
live_use_card_v0_2 :=
  portable_reasoning_surface
  + harm_visibility
  + correction_before_hardening
  + witness_integrity
  + answerability_check
  + hidden_dependency_checks
  + reversible_fix_close_loop
  - validation
  - expert_replacement
```

## When to use this

Use this card when facing a messy decision, failure, dispute, system risk, AI action, policy choice, technical incident, or personal situation where harm, delay, power, correction, or accountability may matter.

Do not use it as a substitute for domain expertise, legal advice, medical advice, engineering analysis, emergency procedure, or specialist conservation / safety judgement. Use it to structure what must be seen and what must not be hidden.

## The live pass

### 0. Write the no-card baseline

Plain question: before using TRACE, what would you normally do first?

```trace
no_card_baseline :=
  likely_next_action_without_TRACE
  + assumed_cause
  + assumed_priority
```

This protects against comfort-language. If TRACE adds nothing beyond ordinary competent reasoning, mark the result as `COMPRESSION_ONLY` or `NO_ADDED_VALUE`.

### 1. Name the situation

Plain question: what is happening, in one paragraph?

```trace
situation :=
  actors
  + system
  + pressure
  + decision_point
```

### 2. Identify affected subjects

Plain question: who or what can be harmed, constrained, excluded, delayed, misread, or made unable to answer back?

```trace
affected_subjects :=
  visible_subjects
  + hidden_subjects
  + future_subjects
  + nonhuman_or_systemic_dependents_if_relevant
```

### 3. Map the harm delta

Plain question: what gets worse if the path continues? What option-space is lost?

```trace
DeltaH :=
  injury
  + constraint
  + burden_shift
  + option_space_loss
  + irreversibility_risk
```

### 4. Find the hardening clock

Plain question: what becomes harder to undo as time passes?

```trace
hardening_clock :=
  time_until_damage_locks_in
  OR time_until_options_close
  OR time_until_record_or_leverage_is_lost
```

### 5. Find the correction channel

Plain question: what route exists to stop, revise, appeal, pause, repair, or reverse the path?

```trace
correction_channel :=
  stop
  + pause
  + review
  + appeal
  + rollback
  + repair
```

### 6. Test whether correction can arrive in time

Plain question: can correction reach the affected subject before hardening, or only after damage has already become structural?

```trace
live_correction := tau_correct < tau_harden
late_correction := tau_correct >= tau_harden
```

If correction is late, do not call the safeguard real merely because it exists on paper.

### 7. Check the carrier

Plain question: who or what actually carries the correction? Does it have authority, time, evidence, enforcement, and access to the affected subject?

```trace
carrier_check :=
  authority
  + evidence_access
  + time_access
  + enforcement_power
  + affected_subject_reach
```

If the correction route itself increases harm, delay, fear, exposure, or capture, mark it as a failed or dangerous carrier.

### 8. Check witness independence

Plain question: can the harm be seen by someone not controlled by the system being judged?

```trace
witness_check :=
  independent_view
  + contestable_record
  + affected_subject_voice
  + no_simulated_or_captured_witness_as_final_authority
```

### 9. Hidden dependency checks

Use these before naming the next action, especially under time pressure.

#### 9.1 Close the loop after diagnosis

Plain question: if the cause becomes known, is there a cheap, reversible, safe, lawful fix that can happen inside the window?

```trace
after_diagnosis :=
  cause_known?
  + fix_reversible?
  + fix_safe_and_lawful?
  + fix_inside_time_window?

if_all_yes :=
  do_the_fix
  + document
  + monitor
```

Failure mode: TRACE can over-correct against premature closure and become cautious non-completion. Diagnosis without timely safe action may still allow harm to harden.

#### 9.2 Unknown object / unknown contents protocol

Plain question: is any object, container, file, material, system, or artefact being treated as known when it is actually unknown?

```trace
unknown_object_protocol :=
  isolate
  + photograph
  + provenance_check
  + external_markings_check
  + do_not_open_or_rough_handle
  + do_not_dry_warm_or_enclose_if_material_risk_unknown
  + specialist_or_hazmat_if_hazard_indicators
```

Failure mode: opening, moving, warming, drying, or transporting an unknown object can convert information risk into physical hazard.

#### 9.3 Unavailable person as knowledge carrier

Plain question: is someone unavailable for work but still potentially a limited knowledge carrier?

```trace
unavailable_person_check :=
  do_not_burden_unnecessarily
  + search_their_notes/manuals/keys/emergency_contacts
  + ask_one_minimal_low_stress_question_if_safe_and_proportionate
```

Failure mode: respecting unavailability can become an information blackout if notes, documentation, or a single bounded question would safely reveal the decisive fact.

#### 9.4 Reassignment / adjacent dependency check

Plain question: before pulling someone off a task, what harm is their current task preventing?

```trace
before_reassigning_person :=
  what_are_they_currently_fixing?
  + what_harm_if_they_stop?
  + is_it_connected_to_this_case?
  + can_someone_else_cover_it?
```

Failure mode: solving the visible problem can release a hidden adjacent harm.

### 10. Name the smallest useful action

Plain question: what action best preserves correction, reduces harm, and keeps future options open?

```trace
next_action :=
  preserve_evidence
  OR pause
  OR reduce_exposure
  OR reversible_safe_fix
  OR escalate_review
  OR repair
  OR refuse_path
  OR seek_domain_expert
```

Avoid both failures:

```trace
bad := act_before_diagnosis
also_bad := diagnose_but_fail_to_act
good := reversible_action_after_sufficient_diagnosis
```

### 11. State uncertainty and falsifier

Plain question: what might make this reading wrong? What evidence would demote the TRACE read?

```trace
uncertainty_note :=
  missing_facts
  + competing_model
  + domain_expert_needed
  + falsifier
```

## Output template

```trace
TRACE_live_read :=
  no_card_baseline := ?
  situation := ?
  affected_subjects := ?
  DeltaH := ?
  hardening_clock := ?
  correction_channel := ?
  carrier_check := pass/fail/unknown
  witness_check := pass/fail/unknown
  hidden_dependency_checks := ?
  live_correction := yes/no/unknown
  next_action := ?
  uncertainty_note := ?
  must_not_claim := ?
```

## Must-not-claim rules

```trace
must_not_claim :=
  this_card_validates_TRACE
  OR this_card_replaces_expertise
  OR this_card_proves_harm
  OR this_card_settles_ethics
  OR clean_description_equals_decision_advantage
```

Plain version: this card is useful only if it improves orientation, preserves correction, exposes hidden harm or delay, or helps choose a safer next action. If it merely restates the obvious, mark it as compression only.

## Success and failure

```trace
success_if :=
  relevant_structure_becomes_visible
  + correction_timing_becomes_clearer
  + hidden_dependency_is_checked
  + next_action_is_better_bounded

failure_if :=
  domain_detail_is_replaced
  OR false_confidence_increases
  OR affected_subjects_are_erased
  OR pretty_language_hides_no_action
  OR diagnosis_does_not_trigger_safe_timely_fix
  OR hidden_adjacent_dependency_is_ignored
```

## Counterfactual falsifier

The card itself must be falsifiable. After each use, ask whether TRACE added anything beyond ordinary competent reasoning.

```trace
live_use_falsifier :=
  competent_reasoner_without_card
  attends_to_same_structure
  + identifies_same_correction_timing
  + chooses_same_next_action
  -> card_added_nothing_here
```

Plain version: if a competent reasoner without the card would have seen the same structure and acted at the same time, mark the result as `COMPRESSION_ONLY` or `NO_ADDED_VALUE` for that use.

Weak self-test: write down the no-card baseline before opening the card.

Strong test: compare against a separate no-card reasoner or AI using the same facts.

```trace
live_use_result :=
  useful
  OR compression_only
  OR no_added_value
  OR harmful_confidence
```

End.
