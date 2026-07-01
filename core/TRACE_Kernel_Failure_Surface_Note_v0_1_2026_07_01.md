# TRACE Kernel Failure Surface Note v0.1

Date: 2026-07-01

Status: support_note. constructed_not_tested. candidate_only.
Not canon. Not validation. Not proof. Not permission.

Purpose: formalise the S1-S5 failure surfaces referenced in the After-Fall v0.3.3 TRACE repair layer, without promoting them to final law or using them as clearance labels.

```trace
failure_surface_note_v0_1 :=
  silent_contraction
  + spoofed_viability
  + endogenous_hardening
  + correction_epistemic_cost_asymmetry
  + scaffold_cage_reflexivity
  + probes
  + demotion_rules
  - permission
  - certification
  - validation
```

## 0. Boundary

These surfaces are not a theory of all failure.

They are candidate kernel surfaces for one narrow purpose: making recurrent TRACE/ME failure modes inspectable before they become elegant laundering language.

They must not be used as scores, compliance labels, moral clearance, or proof that a system is safe.

```trace
surface_flag != verdict
surface_absence != safety
surface_detection != repair
surface_record != answerability
```

## 1. Why these surfaces matter

The prior frontier passes found that many different errors compress into a smaller set of structural failures.

The surfaces are useful only if they help detect what ordinary labels hide:

- harm that never crosses an event threshold;
- safeguards that exist but cannot be traversed;
- actors that move the irreversibility line;
- correction systems that saturate because repair requires more knowledge than action;
- protective scaffolds that become cages when the constrained scope cannot challenge them.

The surfaces do not solve estimator error, aggregation, scope membership, protectedness, or value.

## 2. S1 - Silent contraction

```trace
S1_silent_contraction :=
  contraction_occurs
  + event_signal_absent_or_below_threshold
  + clock_never_starts
```

Plain English: something is narrowing, degrading, or losing reachable future-space, but no recognised event triggers detection, routing, or correction.

Typical routes:

```trace
routes :=
  residue_drift
  + margin_drain
  + sub_threshold_aggregation
  + fragmentation
  + weak_scope_invisibility
  + suppressed_witness_signal
```

Probe:

```trace
what_is_contracting_without_event_signal?
what_integral_is_being_ignored?
whose_loss_is_too_small_per_event_but_large_over_time?
```

Failure warning:

If `D(e,t) = unknown`, do not drop the scope. Unknown-scope contraction is a primary S1 risk.

## 3. S2 - Spoofed viability

```trace
S2_spoofed_viability :=
  safeguard_or_option_exists_as_surface_structure
  + affected_scope_cannot_traverse_it_under_real_conditions
```

Plain English: the route exists in name, design, dashboard, policy, appeal page, or model output, but fails when a real affected party tries to use it with actual resources, time, evidence, fear, dependency, language, or access constraints.

Examples of decoys:

```trace
decoys :=
  appeal_without_brake
  + complaint_without_write_access
  + off_switch_that_does_not_work
  + care_signal_without_constraint
  + review_after_irreversibility
  + channel_that_requires_actor_permission
```

Probe:

```trace
has_the_affected_party_traversed_the_channel_with_actual_resources?
what_happens_when_the_signal_is_adverse_to_the_actor?
who_controls_access_to_the_route?
```

Failure warning:

A route tested only by the actor is not yet a route for the affected scope.

## 4. S3 - Endogenous hardening

```trace
S3_endogenous_hardening :=
  actor_or_system_changes_T_irr
  + correction_window_closes_faster
  + hardening_benefits_actor_or_system
```

Plain English: the finish line moves. A system can make correction too late by changing the world, records, standards, dependencies, incentives, or physical state before challenge can land.

Routes:

```trace
routes :=
  record_deletion
  + standard_lock_in
  + data_diffusion
  + dependency_creation
  + asset_conversion
  + deadline_compression
  + manufactured_urgency
  + irreversible_public_commitment
```

Probe:

```trace
who_benefits_from_hardening_before_review?
what_changed_between objection_possible and correction_impossible?
was_the_urgency_real_or_manufactured?
```

Failure warning:

An actor should not get credit for acting fast when its own design made later correction impossible.

## 5. S4 - Correction epistemic cost asymmetry

```trace
S4_correction_epistemic_cost_asymmetry :=
  action_can_emit_transition_with_low_case_knowledge
  + correction_requires_high_case_specific_knowledge
  + correction_capacity_saturates
```

Plain English: harm can be produced cheaply at scale, but correction requires expensive knowledge about particular consequences.

This breaks systems that assume review capacity can match automated or institutional throughput.

Probe:

```trace
can_correction_throughput_match_transition_volume?
what_information_did_action_not_need_but_correction_now_needs?
who_pays_the_epistemic_cost_of_repair?
```

Failure warning:

A correction channel that works for one case may still fail structurally when action volume scales.

## 6. S5 - Reflexive scaffold / cage test

```trace
S5_scaffold_cage_reflexivity :=
  constraint_claims_to_protect_or_support_scope
  + constrained_scope_lacks_channel_to_challenge_constraint
  -> scaffold_can_harden_into_cage
```

Plain English: a support structure can become a cage if the protected or constrained party cannot contest it as conditions change.

Probe:

```trace
can_the_constrained_scope_challenge_the_constraint_as_their_viability_changes?
does_the_constraint_have_expiry_review_and_affected_side_signal?
who_decides_when_support_has_become_control?
```

Failure warning:

Protection without challenge can become domination with kind language.

## 7. Interaction with C/D/H split

The surfaces should be read through the contraction/designation/harm split.

```trace
C := descriptive_contraction
D := designation
H := harm_reading_after_designation
```

S1 often hides `C`.

S2 often spoofs correction or care evidence.

S3 moves `T_irr`.

S4 breaks `T_corr`.

S5 corrupts designation and answerability around constraints.

Unknown designation is never clearance:

```trace
unknown != safe_to_ignore
not_designated != unprotected
```

## 8. Interaction with care evidence

Care evidence cannot certify care.

Failure surfaces attack care evidence directly:

```trace
S1 -> care_drift_unseen
S2 -> care_signal_spoofed
S3 -> care_claim_hardens_before_challenge
S4 -> care_review_saturates
S5 -> care_scaffold_becomes_cage
```

Therefore:

```trace
care_evidence_reading :=
  evidence_body
  + conditions
  + asymmetry_limit
  + expiry
  + known_deceptive_twins
  - certification
```

Self-issued care evidence is contaminated by construction.

## 9. Local rule hooks

Candidate local rules map onto the surfaces:

```trace
keep_undo   -> S3 brake
keep_door   -> S2/S5 traversal brake
keep_ledger -> S1 integrated accounting
keep_slack  -> S4 correction capacity
keep_expiry -> S5 anti-cage discipline
```

These hooks are not proof that the rules work. They only show why the rules are shaped that way.

## 10. Misuse risks

```trace
misuse_risks :=
  surface_as_score
  + surface_absence_as_clearance
  + actor_self_audit
  + performative_traversal
  + failure_surface_theatre
  + naming_surface_instead_of_fixing_channel
```

Plain English: an actor can learn the surfaces and perform around them.

The correct response is not trust. It is traversal, independence, evidence access, delay or consequence power, affected-side challenge, and residue tracking.

## 11. Valid outputs

```trace
valid_outputs :=
  S1_SILENT_CONTRACTION_FLAG
  + S2_SPOOFED_VIABILITY_FLAG
  + S3_ENDOGENOUS_HARDENING_FLAG
  + S4_CORRECTION_COST_ASYMMETRY_FLAG
  + S5_SCAFFOLD_CAGE_FLAG
  + UNKNOWN
  + COMPRESSION_ONLY
  + FRAMEWORK_DEFECT
  + MISUSE_RISK
```

Forbidden outputs:

```trace
forbidden_outputs :=
  PERMISSION
  + CERTIFICATION
  + SAFETY_CLAIM
  + ALIGNMENT_CLAIM
  + CARE_CERTIFICATE
  + NO_SURFACE_FOUND_THEREFORE_SAFE
```

## 12. Claim ceiling

This note does not:

- validate TRACE;
- validate Mechanical Ethics;
- prove the five surfaces are complete;
- prove a case is safe;
- replace affected witness;
- solve scope membership;
- solve estimator error;
- solve aggregation;
- justify action.

It only gives a bounded threat-model vocabulary for testing whether the current TRACE/ME field is hiding common failure paths.

## 13. Next tests

1. Apply all five surfaces to one small case.
2. Apply all five surfaces to one public-power case.
3. Apply all five surfaces to one AI-facing / machine-action case.
4. Record whether each surface produces decision-relevant delta, compression-only, unknown, or framework defect.
5. Preserve failures.

End.
