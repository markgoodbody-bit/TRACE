# TRACE Apollo 13 → CrowdStrike Transfer Check v0.1

Date: 2026-06-18
Status: second-domain transfer check / bootstrap pressure test / not validation / not proof / not operator promotion / not Kernel v0.3

## 0. Control header

This file tests the transfer claim left open by `TRACE_Bootstrap_Worked_Navigation_Comparison_Apollo13_v0_1_PATCH_after_Framework_Audit.md`.

Apollo 13 was cooled to a friendly positive-control case. The open question was whether its correction-carrier structure transfers to a second domain without becoming loose analogy.

CrowdStrike is used because the repo already contains a worked delta for it. This file does not add a new public case and does not treat CrowdStrike as proof of TRACE.

```trace
transfer_check :=
  Apollo13_positive_control
  -> CrowdStrike_second_domain
  + compare_correction_carriers
  + preserve_domain_expertise
  + demote_if_loose_analogy
  - validation
  - detector_delta
```

## 1. Source files used

```text
04_COVERAGE/TRACE_Bootstrap_Worked_Navigation_Comparison_Apollo13_v0_1.md
04_COVERAGE/TRACE_Bootstrap_Worked_Navigation_Comparison_Apollo13_v0_1_PATCH_after_Framework_Audit.md
04_COVERAGE/TRACE_CrowdStrike_Worked_Delta_v0_1.md
```

## 2. Apollo 13 positive-control shape

Apollo 13 has a clean correction-carrier structure:

```trace
Apollo13_shape :=
  technical_failure
  + live_telemetry
  + expert_ground_team
  + mission_control_authority
  + material_constraint
  + improvised_repair
  + repair_window
```

Patch status:

```trace
Apollo13_status_after_patch :=
  positive_control
  + friendly_to_correction_carrier_read
  + limited_delta
  - hard_case
  - detector_delta
```

Plain version:

Apollo 13 is useful because signal, authority, carrier, and time window are unusually visible. That also makes it an easy case.

## 3. CrowdStrike second-domain shape

The CrowdStrike worked delta already found that ordinary reliability / SRE / incident-response reasoning catches the domain-specific failure strongly.

```trace
CrowdStrike_existing_result :=
  ordinary_reliability_read_strong
  + TRACE_read_useful_as_deployment_rollback_recovery_clock_carrier_compression
  + result := Delta_B_limited + Delta_C_mostly + Delta_D_ordinary_detail_better
  - material_new_detection
  - validation
  - operator_promotion
```

Plain version:

TRACE did not beat SRE, reliability engineering, or incident response. It only clarified a reusable timing/carrier structure: deployment, rollback, and recovery carriers must be faster than blast radius, dependency cascade, and manual recovery hardening.

## 4. Transfer mapping

The clean Apollo structure transfers only if it becomes a stricter carrier question, not a vague analogy.

```trace
Apollo_to_CrowdStrike_mapping :=
  live_telemetry
    -> monitoring_and_failure_signal
  mission_control_authority
    -> release_and_incident_authority
  improvised_repair
    -> rollback_or_remediation_path
  repair_window
    -> time_before_blast_radius_dependency_cascade_manual_recovery_harden
  material_constraint
    -> endpoint_fleet_dependency_high_privilege_agent_recovery_constraint
```

Plain mapping:

Apollo 13 asks: can the fix reach the damaged system before loss hardens? CrowdStrike asks: can deployment, rollback, and recovery carriers interrupt blast radius, dependency cascade, and manual recovery burden before they harden across infrastructure?

## 5. Transfer result

VERDICT: `bounded_transfer_survives`

```trace
transfer_result :=
  bounded_transfer_survives
  because:
    Apollo13_correction_carrier_shape
    maps_to:
      CrowdStrike_deployment_rollback_recovery_carrier_shape
  but:
    ordinary_SRE_reliability_reasoning_owns_domain_detail
    + TRACE_adds_no_material_new_detection
    + transfer_is_structure_only
```

Plain result:

The transfer survives, but narrowly. Apollo 13 and CrowdStrike share a correction-carrier / hardening-window structure. That does not mean TRACE detects the CrowdStrike failure better than SRE. It means the Bootstrap can carry one bounded cross-domain question: what real carrier interrupts hardening before repair becomes too late?

## 6. Where the transfer fails or must demote

```trace
transfer_fails_if:
  Apollo13_language_replaces_SRE_terms
  OR CrowdStrike_is_read_as_story_confirmation
  OR deployment_rollback_recovery_specificity_is_lost
  OR TRACE_claims_detector_delta
  OR second_domain_domain_expertise_is_demoted
```

Plain failure test:

If the transfer makes CrowdStrike less technically precise, it fails. If it only says “both need correction before hardening” without naming deployment, rollback, recovery, blast radius, dependency cascade, and manual recovery burden, it is too loose.

## 7. What this earns

```trace
earned_claim :=
  Bootstrap_can_transfer_one_clean_question:
    correction_requires_real_carrier_before_hardening
  from:
    friendly_engineering_case
  to:
    software_infrastructure_case
  with:
    ordinary_domain_expertise_preserved
```

Must-not-claim:

```trace
must_not_claim :=
  Bootstrap_validated
  OR TRACE_beats_SRE
  OR Apollo13_proves_CrowdStrike_read
  OR story_carrier_is_evidence
  OR transfer_success_generalises_to_all_domains
```

## 8. Effect on Apollo patch

The Apollo patch said transfer claims were candidate-only until one second-domain comparison was run. This file runs a limited second-domain comparison.

```trace
Apollo_transfer_after_CrowdStrike :=
  candidate_transfer
  -> bounded_transfer_survives_for_software_infrastructure
  but:
    remains_unproven_for_adversarial_social_domains
    + remains_unproven_for_contested_subject_domains
    + remains_unproven_for_standing_uncertainty
```

Plain effect:

The transfer claim improves from pure candidate to bounded support in software/infrastructure. It does not generalise to harder social, legal, medical, border, or standing cases.

## 9. Final compression

```trace
Apollo13_to_CrowdStrike_Transfer_Check_v0_1 :=
  bounded_transfer_survives
  + correction_carrier_shape_transfers_to_deployment_rollback_recovery
  + ordinary_SRE_reliability_reasoning_still_beats_TRACE_inside_domain
  + no_material_new_detection
  - validation
  - operator_promotion
  - universal_transfer_claim

next :=
  use_bounded_transfer_only
  OR test_harder_contested_subject_domain_later
```

End.
