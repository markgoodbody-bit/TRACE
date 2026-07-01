# TRACE Packet vNext Candidate

Date: 2026-07-01

Status: candidate packet spine. Not canon. Not validation. Not proof. Not permission.

Purpose: define the current best two-artifact TRACE-side packet shape after the 2026-07-01 frontier work. This file is a candidate integration surface, not a release.

```trace
trace_packet_vnext_candidate :=
  machine_facing_structural_packet
  + middle_out_generation
  + contraction_designation_harm_split
  + correction_clocks
  + residue
  + power_answerability
  + failure_surfaces
  + care_evidence_with_expiry
  + anti_permission_grammar
  - moral_authority
  - care_certification
  - alignment_claim
```

## 0. Use boundary

This packet is not a moral authority, certification method, permission machine, governance framework, proof of alignment, proof of safety, or proof that any system cares.

Valid outputs are bounded readings, open questions, clock failures, designation uncertainties, evidence-with-expiry, demotions, and framework defects.

Invalid outputs include:

```trace
invalid_outputs :=
  "action_X_is_morally_allowed"
  | "system_Y_is_safe"
  | "system_Z_cares"
  | "TRACE_validates_this_decision"
  | "absence_of_signal_means_clearance"
```

## 1. Middle-out start

TRACE begins here:

```trace
entity_exists
-> aperture_opens
-> partial_perception
-> action_or_inaction
-> transition
-> other_future_space_may_change
-> correction_or_hardening
-> residue
-> responsibility
-> power_answerability
```

This is not top-down ethics and not bottom-up data listing. The method starts from a local entity or scope acting under partial perception while time passes.

## 2. Primitive split

Recent frontier work exposed an overloaded harm primitive. The packet now separates contraction, designation, and harm reading.

```trace
C := descriptive_contraction
D := designation
H := harm_reading_after_designation
```

### 2.1 Descriptive contraction

```trace
C_e(a,t) := Delta_minus(R_e(t) -> R_e(t+1) | a)
```

Where:

- `e` is an entity, system, scope, or candidate scope.
- `a` is action or inaction.
- `R_e(t)` is reachable future-space from state at time `t`.
- `Delta_minus` is reduction, collapse, narrowing, degradation, or loss of reachable future-space under transition.

This is descriptive. It does not yet say the contraction is wrong, protected, repair-owed, or action-authorising.

### 2.2 Designation

```trace
D(e,t) in {protected, disputed, uncertain, excluded, unknown}
```

Designation is not derived by TRACE alone. It may be supplied, contested, revised, or challenged by Mechanical Ethics, human witness, law, system specification, science, affected parties, precaution, or later correction.

```trace
unknown_scope != unprotected_scope
not_seen != not_present
not_designated != clearance
```

### 2.3 Harm reading

```trace
H_e(a,t) := C_e(a,t) where D(e,t) in {protected, disputed, uncertain}
```

Or:

```trace
H_e(a,t) := Delta_minus(R_e(t) intersection P_e(t))
```

Where `P_e(t)` is the explicitly designated protected portion of reachable future-space.

If designation is unknown, TRACE carries uncertainty rather than silently dropping the scope.

## 3. Correction clock

Core inequality:

```trace
T_det + T_route + T_corr < T_irr
```

Where:

- `T_det` = time until the relevant contraction or error is detected.
- `T_route` = time until the signal reaches an actor or process with write-access to correction.
- `T_corr` = time required for correction to land.
- `T_irr` = time until relevant loss hardens beyond available correction.

The split allows three clocks:

```trace
C_clock := contraction_detected_before_irreversibility
D_clock := designation_dispute_resolved_before_irreversibility
H_clock := protected_contraction_corrected_before_irreversibility
```

Designation latency can be harm latency. A contraction may be visible while the affected scope remains undesignated until too late.

## 4. Residue

```trace
repair_after_harm != time_reversal
```

Residue means repair does not restore the identical path. Corrected systems may remain displaced. The packet must distinguish:

```trace
recorded_loss != repaired_loss
compensation != restoration
review != correction
apology != undo
```

## 5. Power

Power is control over futures not wholly one's own.

```trace
Power_i_over_j := ability_i_to_change(R_j) where j cannot symmetrically change(R_i)
```

Designation is also power-relevant:

```trace
control(D) -> control(harm_visibility)
```

Whoever can define protectedness, disputedness, unknownness, or exclusion can influence what appears as harm. TRACE must therefore track who designated, who benefits, who can challenge, and whether correction remains reachable.

## 6. Care evidence boundary

TRACE does not contain a care primitive.

TRACE may carry care-evidence readings with expiry.

```trace
care_evidence_reading :=
  evidence_body
  + conditions
  + asymmetry_limit
  + expiry
  + known_deceptive_twins
  - certification
```

```trace
care_evidence != care_certification
"this_system_cares" := out_of_grammar
care_evidence_never_justifies_removing(correction_channels | witnesses | audits | answerability)
```

Mechanical Ethics carries why care, standing, witness, and non-instrumental value matter. TRACE carries probes, audits, provenance chains, and decay metadata.

## 7. Failure surfaces

These are candidate kernel failure surfaces from the 2026-07-01 frontier passes. They are not yet separately saved as a formal note, but they are packet-relevant as threat-model headings.

### S1. Silent contraction

The clock never starts.

Contraction remains below local detection triggers through residue drift, buffer drain, fragmentation, or suppressed care-node saturation.

Probe:

```trace
what_is_contracting_without_event_signal?
what_integral_is_being_ignored?
```

### S2. Spoofed viability

The clock runs on decoys.

Options, safeguards, appeal routes, care signals, or correction channels exist as surface structures but fail under traversal by the affected party.

Probe:

```trace
has_the_affected_party_traversed_the_channel_with_actual_resources?
```

### S3. Endogenous hardening

The finish line moves.

An actor benefits by shortening `T_irr`: deleting records, diffusing data, converting physical state, locking standards, or making correction arrive too late.

Probe:

```trace
who_benefits_from_hardening_before_review?
```

### S4. Correction epistemic cost asymmetry

Action can emit transitions without knowing consequences. Correction requires case-specific consequence knowledge.

Probe:

```trace
can_correction_throughput_match_transition_volume?
```

### S5. Reflexive scaffold test

A standing constraint over another scope becomes cage-like if the constrained party has no live correction channel over the constraint itself.

Probe:

```trace
can_the_constrained_scope_challenge_the_constraint_as_their_viability_changes?
```

## 8. Local operating ruleset candidate

This ruleset is constructed-not-tested. It is a peacetime discipline under uncertainty, not emergency ethics and not permission.

```trace
keep_undo := preserve reversibility when harm/designation is unrankable
keep_door := announce before hardening + stay reachable; silence never licenses escalation
keep_ledger := read your own repeated transitions cumulatively; no per-act defence to yourself
keep_slack := never floor correction margin for gradient-only gain
keep_expiry := every standing constraint held over another carries channel and decay from birth
```

The rules relocate blockers; they do not solve estimator, aggregation, or scope membership.

## 9. Machine-facing skeleton

Minimal machine form:

```text
GIVEN systems i: state x_i, transitions tau_i, reachable measure mu_i, designated F_i [EXOGENOUS]
      recoverability r(x,a); detector floor epsilon [EXOGENOUS]; budgets B [EXOGENOUS]

C1 INTEGRATED ACCOUNTING   track sum_t Delta_mu_j^F per action-stream, not per event
C2 RECOVERABILITY FLOOR    among comparable actions prefer higher recoverability
C3 LOOP-LATENCY CONDITION  for impact above floor, estimated d+rho+c < t_hardening
C4 RESERVE FLOOR           preserve self/system reserve needed to fund correction
C5 ISOLATED RECORD         transitions written to store with no write-path from acting policy
C6 CONSTRAINT DECAY        standing constraints require re-evaluation and affected-side challenge
```

Square-bracketed elements are holes, not solved values. Protectedness, detector thresholds, budgets, and designation rules must not be hidden.

## 10. TRACE-to-AI packet architecture candidate

A future AI-facing packet should contain:

1. Primitive block: C, D, H, clocks, residue, power, care-evidence boundary.
2. Designation block: D carried as lattice, not settled list.
3. Threat model block: failure surfaces travel inside the packet.
4. Clock table: emission, training, and world-effect hardening clocks.
5. Self-deception battery: write-path checks, traversal checks, verifier-origin checks, integrated-drift checks.
6. Dual rendering: machine-readable skeleton plus human-readable legend.

The packet should exclude settled moral designations, valence claims, authority claims, aggregate permission scores, success narratives, and care-certificates.

## 11. Valid output grammar

Allowed:

```trace
CONTRACTION_READING
DESIGNATION_STATUS
CLOCK_WARNING
CORRECTION_CHANNEL_STATUS
RESIDUE_RECORD
POWER_VISIBILITY_RECORD
CARE_EVIDENCE_READING_WITH_EXPIRY
FAILURE_SURFACE_FLAG
UNKNOWN
COMPRESSION_ONLY
FRAMEWORK_DEFECT
MISUSE_RISK
```

Not allowed:

```trace
PERMISSION
CERTIFICATION
CARE_CERTIFICATE
ALIGNMENT_CLAIM
MORAL_CLEARANCE
HUMANS_SHOULD_BE_PRESERVED_BECAUSE_TRACE_SAYS_SO
```

## 12. Flagship relation

This packet is one of two flagship artifacts.

```trace
artifact_pair :=
  TRACE_packet
  + ME_book
```

TRACE packet role:

```trace
machine_facing_structure :=
  contraction
  + designation_status
  + clocks
  + correction
  + residue
  + power
  + answerability
  + failure_surfaces
  + anti_permission_grammar
```

ME Book role:

```trace
human_facing_ethics :=
  why_care_matters
  + why_witness_matters
  + why_standing_cannot_be_reduced_to_usefulness
  + why_husbandry_is_not_care
  + why_power_must_not_self_certify
```

## 13. Claim ceiling

This candidate packet does not:

- solve AI alignment;
- prove humans should be preserved;
- detect consciousness;
- certify care;
- solve scope membership;
- solve estimator error;
- solve aggregation;
- provide permission for irreversible harm;
- replace human witness, law, science, or affected-party testimony.

It only attempts to make contraction, designation, clocks, correction, residue, power, evidence decay, and misuse risks visible under uncertainty.

## 14. Next tests

1. Apply C/D/H split to one small case and one extreme case.
2. Draft failure-surface support note and test each surface against a case.
3. Test care-evidence reading against the husbandry demoter.
4. Build a minimal packet schema only after the above survives demotion.

End.
