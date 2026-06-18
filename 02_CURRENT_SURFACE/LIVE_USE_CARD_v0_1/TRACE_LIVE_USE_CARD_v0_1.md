# TRACE Live Use Card v0.1

Status: front-door use instrument / live reasoning surface / not validation / not proof / not governance certification.

Purpose: give a human or AI a compact way to use TRACE on a real situation in minutes. This card does not claim TRACE beats domain experts. It tests whether TRACE makes relevant structure available in context for live reasoning and correction.

```trace
live_use_card :=
  portable_reasoning_surface
  + harm_visibility
  + correction_before_hardening
  + witness_integrity
  + answerability_check
  - validation
  - expert_replacement
```

## When to use this

Use this card when facing a messy decision, failure, dispute, system risk, AI action, policy choice, technical incident, or personal situation where harm, delay, power, correction, or accountability may matter.

Do not use it as a substitute for domain expertise, legal advice, medical advice, engineering analysis, or emergency procedure. Use it to structure what must be seen and what must not be hidden.

## The live pass

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

Plain question: can correction reach the affected subject before hardening, or only after the damage has already become structural?

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

### 9. Name the smallest useful action

Plain question: what action best preserves correction, reduces harm, and keeps future options open?

```trace
next_action :=
  preserve_evidence
  OR pause
  OR reduce_exposure
  OR escalate_review
  OR repair
  OR refuse_path
  OR seek_domain_expert
```

### 10. State uncertainty and falsifier

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
  situation := ?
  affected_subjects := ?
  DeltaH := ?
  hardening_clock := ?
  correction_channel := ?
  carrier_check := pass/fail/unknown
  witness_check := pass/fail/unknown
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
  + next_action_is_better_bounded

failure_if :=
  domain_detail_is_replaced
  OR false_confidence_increases
  OR affected_subjects_are_erased
  OR pretty_language_hides_no_action
```

End.
