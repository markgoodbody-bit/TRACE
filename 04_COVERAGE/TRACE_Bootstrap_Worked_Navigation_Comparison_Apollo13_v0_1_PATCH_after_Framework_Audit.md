# TRACE Bootstrap Worked Navigation Comparison — Apollo 13 Patch after Framework Audit

Date: 2026-06-18
Status: patch note / support comparison cooling / not validation / not proof / not operator promotion / not Kernel v0.3

## 0. Control header

This patch cools `TRACE_Bootstrap_Worked_Navigation_Comparison_Apollo13_v0_1.md` after internal hostile audit.

It does not promote the Apollo 13 comparison.

It does not claim a detector delta.

It does not validate TRACE.

```trace
patch_after_audit :=
  positive_control_warning
  + expert_baseline_limitation
  + transfer_demotion_guard
  + scope_limitation
  - validation
  - detector_delta
```

## 1. Patch 1 — positive-control warning

Insert near Section 1 or Section 7:

```markdown
Positive-control warning: Apollo 13 is a friendly case for TRACE because the correction carrier, signal path, authority route, material constraints, and time window are already unusually visible. This comparison tests whether Bootstrap can explain a clean correction-carrier case without overclaiming. It does not test harder cases involving adversarial gates, hidden subjects, or contested standing.
```

Reason:

Apollo 13 is almost tailor-made for correction-before-hardening. That makes it useful as a positive control, not a hard test.

```trace
Apollo13_case_status :=
  positive_control
  + friendly_to_correction_carrier_read
  - hard_case
```

## 2. Patch 2 — expert baseline limitation

Insert near Section 2:

```markdown
Comparator limitation: this ordinary read is only a high-level summary. A real comparator run would require a stronger mission-operations, aerospace safety, or incident-response baseline. TRACE cannot claim a detector delta from this file.
```

Reason:

The ordinary expert side is not fully developed. TRACE should not gain apparent strength by comparing a structured TRACE read against a shallow ordinary read.

```trace
ordinary_baseline_status :=
  high_level_summary
  - full_comparator
```

## 3. Patch 3 — transfer-demotion guard

Insert near Section 4:

```markdown
Transfer-demotion guard: the listed cross-domain transfers remain candidate only until at least one second-domain comparison is run. Listing plausible transfer domains is not evidence that transfer succeeds.
```

Reason:

The file lists software incident response, administrative redress, AI deployment rollback, infrastructure maintenance, and medical supply/care path as plausible transfer domains. Listing is not testing.

```trace
transfer_claim_status :=
  candidate_only
  until:
    second_domain_comparison_run
```

## 4. Patch 4 — scope limitation

Insert near Section 8:

```markdown
Scope limitation: Apollo 13 mainly tests correction-carrier navigation. It does not strongly test contested subjects, adversarial power, hidden exclusion, burden routing, standing uncertainty, or captured review.
```

Reason:

Apollo 13 has a clear affected system and strong cooperative expert structure. It does not pressure the social/institutional edge cases where TRACE usually risks overclaim.

```trace
Apollo13_scope :=
  correction_carrier_navigation
  not:
    contested_subject
    + adversarial_power
    + hidden_exclusion
    + burden_routing
    + standing_uncertainty
    + captured_review
```

## 5. Status after patch

```trace
Apollo13_Worked_Navigation_after_patch :=
  retain_as_support_comparison
  + positive_control
  + limited_delta
  + transfer_candidate_only
  + ordinary_expert_priority_preserved
  - validation
  - detector_delta
  - hard_case_status
```

Plain result:

Apollo 13 remains useful, but only as a clean positive-control test of correction-carrier navigation. It should not be used as proof that Bootstrap V2 works in harder contested domains.

## 6. Final compression

```trace
Apollo13_patch_after_audit :=
  cool_case_status_to_positive_control
  + block_detector_delta
  + mark_transfer_candidate_only
  + preserve_expert_priority
  - validation
  - hard_case_claim

next :=
  either_apply_patch_to_source_file
  OR run_harder_second_domain_comparison
```

End.
