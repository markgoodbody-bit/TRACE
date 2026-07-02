# Witness Pack Fillable Template v0.7

Status: cold-reader pre-field candidate. Not canon, validation, proof, permission, clearance, compliance, or release.

Use plain English. Leave unknown fields as UNKNOWN. Do not invent certainty.

## 1. Pack identity

```yaml
pack_id:
created_at:
pack_status: draft | sealed | deposited | public_summary | reviewed | abandoned_unknown | unsafe_to_use
identity_mode: named | pseudonymous | identity_escrowed | anonymous
deanonymization_risk: low | medium | high | unknown
safe_contact_route:
retaliation_risk: low | medium | high | unknown
support_bridge_or_reason_absent:
```

## 2. Public summary

Use only details safe enough to share.

```yaml
public_summary:
  what_happened:
  affected_scope:
  actor_or_system:
  what_changed:
  what_future_space_was_lost_or_threatened:
  what_is_unknown:
  unsafe_details_excluded:
```

## 3. Core claim, sealed if needed

```yaml
core_claim:
  full_summary:
  affected_scope:
  responsible_actor_or_system:
  location_or_context:
  what_changed:
  future_space_lost_or_threatened:
  uncertainty_notes:
  D_plain_language_who_or_what_was_counted:
  D_plain_language_who_or_what_was_not_counted:
  mu_plain_language_what_was_measured:
  mu_plain_language_what_was_ignored:
```

## 4. Retaliation protocol

```yaml
retaliation_protocol:
  risk_level: low | medium | high | unknown
  mitigation_trigger: sealed_only | legal_or_support_alert | union_alert | journalist_hold | trusted_intermediary | delayed_public_release | none | other
  parallel_retaliation_log_required: true | false
  emergency_contact_or_bridge:
  identity_release_conditions:
  safe_public_summary_allowed: true | false | unknown
  unsafe_details_to_keep_sealed:
    -
```

If high risk and no mitigation exists:

```trace
WITNESS_RISK_UNCARRIED
```

## 5. Evidence items

Do not say what the item proves. Say what it is.

```yaml
evidence_items:
  - item_id:
    item_type: observation | claim | inference | document | testimony | derived_analysis
    quality_status: primary_contested | primary_uncorroborated | primary_corroborated | secondary | hearsay | unknown
    description:
    source: protected_or_named
    date_observed: date_or_unknown
    hash: sha256_or_null_reason
    storage_location: protected_or_named
    sensitivity: low | medium | high | extreme
    metadata_redaction_check: passed | failed | not_checked | not_applicable
    chain_of_custody: required_or_reason_absent
```

## 6. Asks, refusals, and silence

```yaml
asks_and_refusals:
  - ask_id:
    date_sent:
    recipient:
    request_summary:
    official_route_required_by_actor:
    actual_route_available_to_affected_scope:
    response: provided | refused | partial | no_response | redirected | retaliatory
    response_due_date:
    evidence_id:
    silence_after_due_date_counts_as: non_response_not_consent
```

## 7. Parallel retaliation log

```yaml
parallel_retaliation_log:
  - event_id:
    date:
    event_summary:
    actor_or_agent:
    connection_to_claim: known | suspected | unknown
    evidence_id:
    safety_action_taken:
```

## 8. Custody plan

```yaml
custody_plan:
  minimum_holder_types_required: 2
  holders:
    - holder_id:
      holder_type: public_archive | advice_worker | solicitor_or_legal_support | journalist | union_or_renters_group | regulator | trusted_person | distributed_storage | other
      holder_independence_vector:
        selected_by: affected_scope | trusted_intermediary | unknown
        paid_by: none | affected_scope | escrow | unknown
        actor_relationship: none | direct | indirect | unknown
        publicity_control: holder | affected_scope | sealed_trigger | unknown
      correlation_cluster:
      access_conditions:
      retention_terms:
      tamper_evidence_method: hash | timestamp | signature | append_only_log | other
      safety_assessment:
      compelled_disclosure_or_exposure_risk: low | medium | high | unknown
```

If one holder or one provider is the only route:

```trace
CARRIER_MONOCULTURE_RISK
```

## 9. Aggregation without doxxing

```yaml
aggregation_record:
  stream_id:
  correlation_method: shared_actor | shared_location | shared_mechanism | shared_time_window | trusted_intermediary | privacy_preserving_hash | other
  doxxing_risk: low | medium | high | unknown
  aggregation_trigger: N_packs | same_mechanism | retaliation_pattern | external_challenger_request | other
  public_aggregate_allowed: true | false | unknown
  individual_identity_release_allowed: false
  fake_pack_flood_countermeasure: provenance_review | trusted_intermediary_attestation | timestamp_gap_check | other
```

## 10. Clocks

```yaml
clocks:
  first_detected:
  actor_notified:
  response_due:
  time_to_challenge:
  opportunity_clock_what_closes_if_delayed:
  irreversibility_clock_what_may_become_unrepairable:
  who_controls_each_clock:
  slow_hardening_risk: low | medium | high | unknown
```

## 11. Residue and burden

```yaml
residue_and_burden:
  current_burden_bearer: affected_scope | other | unknown
  burden_types:
    - money
    - time
    - health
    - fear
    - care
    - legal_work
    - adaptation
    - proof_labour
    - other
  what_would_burden_return_require:
  affected_side_confirmation_required: true
  review_clock:
```

## 12. Enforcement and escalation

```yaml
enforcement_state:
  current_route: none | actor_process | regulator | court | union | journalist | public_archive | other
  enforcer_identity:
  enforcement_status: present | absent | pending | captured | unknown
  if_no_enforcer: ENFORCEMENT_ABSENT_NO_DISCHARGE
  automatic_escalation:
    trigger_condition: date | non_response | retaliation_event | N_packs | health_risk | other
    action: deposit_more_holders | support_alert | trusted_intermediary_review | public_summary_release | regulator_submission | other
    safe_public_version_required: true
```

## 13. Completion status

```yaml
completion_status:
  filled_by: named_or_protected
  reviewed_by: none | trusted_intermediary | advocate | other
  next_review_date:
  known_gaps:
    -
  risk_of_using_this_pack: low | medium | high | unknown
  plain_warning: A witness pack is a record. It is not justice or safety by itself.
```

End.
