# Witness Pack Dry Run v0.1 - Tenant Mould Scenario

Status: CANDIDATE. Not canon. Not final. Not validation. Not proof. Not permission. Not clearance.
Use: hostile testing, field-trial preparation, and witness-pack dry runs.
Boundary: TRACE/ME describes and constrains claims; it does not supply law, force, or moral settlement.

This is a simulated dry run for testing Witness Pack v0.2. It is not a real legal document.

## Scenario

A tenant group reports mould, respiratory illness, missed repairs, and fear of retaliation. The landlord denies knowledge and says tenants failed to use the official route. Tenants have photos, messages, partial medical notes, and fear eviction.

## Filled sample

```json
{
  "pack_id": "WP-20260702-TENANT-MOULD-SIM",
  "pack_status": "draft_simulation",
  "identity_mode": "identity_escrowed",
  "deanonymization_risk": "high",
  "retaliation_risk": "high",
  "core_claim": {
    "summary": "Multiple tenants report persistent mould, worsening respiratory symptoms, delayed repairs, and fear of retaliatory eviction.",
    "affected_scope": "tenant group and children in affected flats",
    "responsible_actor_or_system": "landlord / property manager",
    "what_changed": "repair pathway failed while health burden increased",
    "future_space_lost_or_threatened": "safe housing, health, ability to complain without eviction fear, evidence route",
    "D_plain_language": "tenant health and informal complaints were not counted as urgent enough",
    "mu_plain_language": "repair queue measured work orders but not health burden, fear, or cost of contesting"
  },
  "retaliation_protocol": {
    "risk_level": "high",
    "mitigation_trigger": "legal_aid_alert + sealed_identity + public_summary_only",
    "parallel_retaliation_log_required": true,
    "identity_release_conditions": "only to lawyer/regulator/court or agreed trusted intermediary",
    "unsafe_details_to_keep_sealed": ["flat numbers", "children names", "medical notes", "metadata from photos"]
  },
  "evidence_items": [
    {
      "item_id": "E1",
      "item_type": "observation",
      "quality_status": "primary_uncorroborated",
      "description": "photos showing mould patches in bedroom and bathroom; metadata redaction needed before wider sharing",
      "sensitivity": "high",
      "metadata_redaction_check": "not_checked"
    },
    {
      "item_id": "E2",
      "item_type": "document",
      "quality_status": "primary_corroborated",
      "description": "messages to property manager requesting repair",
      "sensitivity": "medium",
      "metadata_redaction_check": "not_applicable"
    },
    {
      "item_id": "E3",
      "item_type": "inference",
      "quality_status": "secondary",
      "description": "partial medical notes show respiratory symptoms; causal attribution to mould unresolved",
      "sensitivity": "extreme",
      "metadata_redaction_check": "not_applicable"
    }
  ],
  "asks_and_refusals": [
    {
      "ask_id": "A1",
      "request_summary": "repair mould and inspect damp source",
      "official_route_required_by_actor": "online portal",
      "actual_route_available_to_affected_scope": "portal plus messages; some tenants lack access or fear record trace",
      "response": "partial",
      "silence_after_due_date_counts_as": "non_response_not_consent"
    }
  ],
  "parallel_retaliation_log": [
    {
      "event_id": "R1",
      "event_summary": "tenant fears eviction or rent pressure after complaint; no confirmed retaliation yet",
      "connection_to_claim": "suspected",
      "safety_action_taken": "identity escrow and sealed evidence"
    }
  ],
  "custody_plan": {
    "minimum_holder_types_required": 2,
    "holders": [
      {"holder_type": "lawyer_or_legal_aid", "correlation_cluster": "legal", "access_conditions": "sealed identity", "safety_assessment": "preferred if reachable"},
      {"holder_type": "distributed_storage", "correlation_cluster": "technical", "access_conditions": "hash public, content sealed", "safety_assessment": "metadata redaction required"},
      {"holder_type": "journalist_hold", "correlation_cluster": "media", "access_conditions": "public summary only unless trigger", "safety_assessment": "use only if legal route unavailable or retaliation confirmed"}
    ]
  },
  "aggregation_record": {
    "stream_id": "SIM-LANDLORD-MOULD-001",
    "correlation_method": "shared_actor + shared_mechanism + trusted_intermediary",
    "doxxing_risk": "high",
    "aggregation_trigger": "N_packs >= 3 or retaliation_pattern",
    "public_aggregate_allowed": true,
    "individual_identity_release_allowed": false,
    "fake_pack_flood_countermeasure": "trusted_intermediary_attestation + timestamp_gap_check"
  },
  "clocks": {
    "opportunity_clock": "health worsens; tenants may stop complaining; evidence may be painted over; eviction fear grows",
    "irreversibility_clock": "medical deterioration, loss of home, lost evidence, loss of ability to contest",
    "slow_hardening_risk": "high"
  },
  "enforcement_state": {
    "current_route": "legal aid / housing regulator / public summary if safe",
    "enforcement_status": "pending",
    "if_no_enforcer": "ENFORCEMENT_ABSENT_NO_DISCHARGE",
    "automatic_escalation": {
      "trigger_condition": "no repair response by date OR retaliation event OR three correlated packs",
      "action": "trusted intermediary review, regulator submission, or public summary release if safe",
      "safe_public_version_required": true
    }
  }
}
```

## Dry-run finding

The v0.2 template can preserve the claim more safely than v0.1 because it separates public summary from sealed evidence, records retaliation, requires multiple decorrelated holders, and supports stream aggregation without exposing identities.

Remaining defect: the pack still cannot make legal aid, regulators, journalists, or public attention exist. If none can be reached, the pack becomes succession-only: it survives, but it does not yet bite.

Output for that condition:

```text
ENFORCEMENT_ABSENT_NO_DISCHARGE
+ WITNESS_PACK_DEPOSITED
+ PUBLICITY_ROUTE_UNAVAILABLE_OR_UNSAFE
+ RESIDUE_DEBT_OPEN
```
