# Witness Pack Template v0.2

Status: CANDIDATE. Not canon. Not final. Not validation. Not proof. Not permission. Not clearance.
Use: hostile testing, field-trial preparation, and witness-pack dry runs.
Boundary: TRACE/ME describes and constrains claims; it does not supply law, force, or moral settlement.

Purpose: preserve evidence, protect witnesses where possible, log asks/refusals, resist outlasting, and create future challenge material when no immediate enforcer exists.

Warning: this template is not legal advice, not justice, not proof, and not safe in every context. If filling the pack increases danger, use a safer intermediary or do not fill personally.

## 1. Pack identity

```json
{
  "pack_id": "WP-YYYYMMDD-shortcode",
  "created_at": "ISO-8601",
  "pack_status": "draft|sealed|deposited|public_summary|reviewed|abandoned_unknown",
  "identity_mode": "named|pseudonymous|identity_escrowed|anonymous",
  "deanonymization_risk": "low|medium|high|unknown",
  "safe_contact_route": "required_or_reason_absent",
  "retaliation_risk": "low|medium|high|unknown",
  "legal_or_support_bridge": "required_or_reason_absent"
}
```

## 2. Core claim

```json
{
  "core_claim": {
    "summary": "plain-language claim",
    "affected_scope": "who or what is affected",
    "responsible_actor_or_system": "actor name or unknown",
    "location_or_context": "where this happens",
    "what_changed": "transition being recorded",
    "future_space_lost_or_threatened": "what options, health, safety, relation, or repair path narrowed",
    "uncertainty_notes": "what is unknown",
    "D_plain_language": "who/what was counted or not counted",
    "mu_plain_language": "how loss or burden was measured or ignored"
  }
}
```

Use plain English. No TRACE training is required. D means who/what counts. mu means how loss is measured.

## 3. Retaliation protocol

```json
{
  "retaliation_protocol": {
    "risk_level": "low|medium|high|unknown",
    "mitigation_trigger": "sealed_only|legal_aid_alert|union_alert|journalist_hold|trusted_intermediary|automatic_public_release|none|other",
    "parallel_retaliation_log_required": true,
    "emergency_contact_or_bridge": "required_or_reason_absent",
    "identity_release_conditions": "required",
    "safe_public_summary_allowed": true,
    "unsafe_details_to_keep_sealed": []
  }
}
```

High risk with no mitigation means: `WITNESS_RISK_UNCARRIED`.

## 4. Evidence items

```json
{
  "evidence_items": [
    {
      "item_id": "E1",
      "item_type": "observation|claim|inference|document|testimony|derived_analysis",
      "quality_status": "primary_contested|primary_uncorroborated|primary_corroborated|secondary|hearsay|unknown",
      "description": "what it is, not what it proves",
      "source": "protected_or_named",
      "date_observed": "date_or_unknown",
      "hash": "sha256_or_null_reason",
      "storage_location": "protected_or_named",
      "sensitivity": "low|medium|high|extreme",
      "metadata_redaction_check": "passed|failed|not_checked|not_applicable",
      "chain_of_custody": "required_or_reason_absent"
    }
  ]
}
```

Separate observation, inference, and claim. A photo of mould is an observation. "The mould caused illness" is an inference unless supported by medical or expert evidence.

## 5. Asks, refusals, and silence

```json
{
  "asks_and_refusals": [
    {
      "ask_id": "A1",
      "date_sent": "date",
      "recipient": "actor or office",
      "request_summary": "what was asked",
      "official_route_required_by_actor": "required_or_unknown",
      "actual_route_available_to_affected_scope": "required_or_unknown",
      "response": "provided|refused|partial|no_response|redirected|retaliatory",
      "response_due_date": "date_or_unknown",
      "evidence_id": "linked evidence or null",
      "silence_after_due_date_counts_as": "non_response_not_consent"
    }
  ]
}
```

## 6. Parallel retaliation log

```json
{
  "parallel_retaliation_log": [
    {
      "event_id": "R1",
      "date": "date",
      "event_summary": "rent increase, eviction notice, repair refusal, threat, access denial, etc.",
      "actor_or_agent": "required_or_unknown",
      "connection_to_claim": "known|suspected|unknown",
      "evidence_id": "required_or_null",
      "safety_action_taken": "required_or_none"
    }
  ]
}
```

Retaliation may be indirect. Pattern change after complaint matters.

## 7. Custody and holders

```json
{
  "custody_plan": {
    "minimum_holder_types_required": 2,
    "holders": [
      {
        "holder_id": "H1",
        "holder_type": "public_archive|lawyer|journalist|union|regulator|trusted_person|distributed_storage|other",
        "holder_independence_vector": {
          "selected_by": "affected_scope|trusted_intermediary|unknown",
          "paid_by": "none|affected_scope|escrow|unknown",
          "actor_relationship": "none|direct|indirect|unknown",
          "publicity_control": "holder|affected_scope|sealed_trigger|unknown"
        },
        "correlation_cluster": "required",
        "access_conditions": "required",
        "retention_terms": "required",
        "tamper_evidence_method": "hash|timestamp|signature|append_only_log|other",
        "safety_assessment": "required"
      }
    ]
  }
}
```

## 8. Aggregation without doxxing

```json
{
  "aggregation_record": {
    "stream_id": "required_or_null",
    "correlation_method": "shared_actor|shared_location|shared_mechanism|shared_time_window|trusted_intermediary|privacy_preserving_hash|other",
    "doxxing_risk": "low|medium|high|unknown",
    "aggregation_trigger": "N_packs|same_mechanism|retaliation_pattern|external_challenger_request|other",
    "public_aggregate_allowed": true,
    "individual_identity_release_allowed": false,
    "fake_pack_flood_countermeasure": "provenance_review|trusted_intermediary_attestation|timestamp_gap_check|other"
  }
}
```

## 9. Clocks

```json
{
  "clocks": {
    "first_detected": "date_or_unknown",
    "actor_notified": "date_or_unknown",
    "response_due": "date_or_unknown",
    "time_to_challenge": "date_or_unknown",
    "opportunity_clock": "what closes if delayed",
    "irreversibility_clock": "what may become impossible to repair",
    "who_controls_each_clock": "required",
    "slow_hardening_risk": "low|medium|high|unknown"
  }
}
```

## 10. Residue and burden

```json
{
  "residue_and_burden": {
    "current_burden_bearer": "affected_scope|other|unknown",
    "burden_types": ["money", "time", "health", "fear", "care", "legal_work", "adaptation", "proof_labour", "other"],
    "what_would_burden_return_require": "plain language",
    "affected_side_confirmation_required": true,
    "review_clock": "date_or_trigger"
  }
}
```

## 11. Enforcement and escalation

```json
{
  "enforcement_state": {
    "current_route": "none|landlord_process|regulator|court|union|journalist|public_archive|other",
    "enforcer_identity": "required_or_null",
    "enforcement_status": "present|absent|pending|captured|unknown",
    "if_no_enforcer": "ENFORCEMENT_ABSENT_NO_DISCHARGE",
    "automatic_escalation": {
      "trigger_condition": "date|non_response|retaliation_event|N_packs|health_risk|other",
      "action": "deposit_more_holders|legal_aid_alert|trusted_intermediary_review|public_summary_release|regulator_submission|other",
      "safe_public_version_required": true
    }
  }
}
```

## 12. Completion status

```json
{
  "completion_status": {
    "filled_by": "named_or_protected",
    "reviewed_by": "none|trusted_intermediary|lawyer|advocate|other",
    "next_review_date": "date_or_unknown",
    "known_gaps": [],
    "risk_of_using_this_pack": "low|medium|high|unknown",
    "plain_warning": "A witness pack is a record. It is not justice or safety by itself."
  }
}
```
