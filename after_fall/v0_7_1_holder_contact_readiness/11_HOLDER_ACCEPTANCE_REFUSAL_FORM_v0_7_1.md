# Holder Acceptance / Refusal Form v0.7.1

Status: holder-contact readiness patch. Candidate only. Not legal advice, validation, proof, permission, clearance, compliance, field test result, or release.

## 1. Purpose

This form records whether a possible holder can receive, preserve, timestamp, review, advise on, or refuse a Witness Pack.

A refusal is not failure. A refusal with reasons is design data.

## 2. Holder identity

```yaml
holder_identity:
  holder_name_or_role:
  organisation_type: advice_worker | solicitor_or_legal_support | renters_group | union | journalist | archive | councillor_or_caseworker | trusted_intermediary | technical_holder | other
  named_or_anonymised: named | anonymised | role_only
  contact_date:
  permission_to_record_response: yes | no | anonymised_only
```

## 3. Response type

Choose one:

```yaml
response_type: HOLDER_ACCEPTS_WITH_CONDITIONS | HOLDER_REFUSES_WITH_REASONS | HOLDER_REQUIRES_DIFFERENT_FORMAT | HOLDER_CAN_HOLD_PUBLIC_SUMMARY_ONLY | HOLDER_CAN_HOLD_HASH_OR_INDEX_ONLY | HOLDER_UNREACHABLE_OR_NO_CAPACITY | SAFETY_RISK_TOO_HIGH | BETTER_HOLDER_SUGGESTED
```

## 4. What can be received?

```yaml
can_receive:
  public_summary: yes | no | maybe
  sealed_evidence: yes | no | maybe
  hashes_only: yes | no | maybe
  index_only: yes | no | maybe
  identity_escrow: yes | no | maybe
  retaliation_log: yes | no | maybe
```

## 5. Conditions for acceptance

```yaml
conditions_for_acceptance:
  required_format:
  required_redactions:
  required_consent:
  required_support_route:
  required_legal_or_policy_review:
  required_retention_terms:
  required_deletion_terms:
  required_identity_handling:
  required_metadata_handling:
```

## 6. Reasons for refusal or limits

```yaml
reasons_for_refusal_or_limits:
  - no_capacity
  - legal_risk
  - confidentiality_risk
  - unclear_role
  - unsafe_for_affected_person
  - unsafe_for_holder
  - wrong_format
  - no_mandate
  - cannot_hold_sealed_material
  - cannot_hold_sensitive_personal_data
  - cannot_receive_without_existing_client_relationship
  - other
notes:
```

## 7. Safety concerns

```yaml
safety_concerns:
  retaliation_risk:
  metadata_risk:
  identification_risk:
  compelled_disclosure_or_exposure_risk:
  publication_risk:
  data_retention_risk:
  small_N_aggregation_risk:
```

## 8. Better holder route

```yaml
better_holder_suggestion:
  suggested_holder_type:
  reason:
  contact_method_if_safe:
  limits_or_warnings:
```

## 9. Result label

If accepted:

```trace
HOLDER_ACCEPTS_WITH_CONDITIONS
not := validation | proof | safety | clearance
```

If refused:

```trace
HOLDER_REFUSES_WITH_REASONS
+ carrier_defect_or_context_limit_logged
```

If unreachable:

```trace
HOLDER_UNREACHABLE
+ CUSTODY_MASS_NOT_SHOWN
```

## 10. Follow-up

```yaml
follow_up:
  next_action:
  deadline:
  who_controls_next_clock:
  risk_before_follow_up:
```

End.
