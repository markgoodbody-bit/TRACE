# Answerability Carrier v0.3 - Operational Carrier Candidate

Status: CANDIDATE. Not canon. Not final. Not validation. Not proof. Not permission. Not clearance.
Use: hostile testing, field-trial preparation, and witness-pack dry runs.
Boundary: TRACE/ME describes and constrains claims; it does not supply law, force, or moral settlement.

## 1. Purpose

The Answerability Carrier is the operational support object for TRACE/ME. It is activated when an actor uses TRACE/ME language near power, trust, safety, legitimacy, or public institutional action.

```text
carrier_purpose := convert_visibility_into_challenge_capacity
carrier_warning := every_carrier_can_be_captured
```

v0.3 adds missing masses, machine-readable field schemas, stronger witness protection, escalation discipline, and anti-branding rules.

## 2. Carrier state

```json
{
  "carrier_state": "uncarried|partially_carried|carried_limited|enforcement_absent_no_discharge|claim_packet_only",
  "carrier_state_reason": "required",
  "active_carrier_pointer": "required_or_null",
  "not_clearance": true,
  "not_compliance": true,
  "not_permission": true
}
```

`carried_limited` is never global. It must name scope, time, carrier masses present, masses missing, and independence limits.

## 3. Mass vector and proof discipline

```json
{
  "mass_vector": {
    "money": {},
    "time": {},
    "evidence_custody": {},
    "adjudication_custody": {},
    "succession": {},
    "price": {},
    "force_control": {},
    "attention_publicity": {},
    "technical_lockout": {}
  }
}
```

Each proof must state: holder, actor-control status, evidence id, expiry, contest route, and failure mode.

```text
actor_claimed_mass_without_non_actor_proof := CLAIM_PACKET_ONLY
private_mass_proof_for_public_claim := CLAIM_PACKET_ONLY
metadata_stripping := CONTAMINATED_SIGNAL
```

## 4. Minimum viable carrier: Witness Pack v0.2

The Witness Pack is the minimum carrier under enforcement absence. It preserves claims, records asks/refusals, protects identity where possible, and creates future challenge material.

It does not make justice happen. It must not pretend to.

v0.2 requires:

- evidence split into observation, claim, inference, document, testimony, and derived analysis.
- retaliation mitigation trigger.
- parallel retaliation log.
- minimum two decorrelated holder types where possible.
- holder independence vector.
- metadata redaction check.
- fake-pack countermeasure.
- stream id and correlation without doxxing.
- official route vs actual access comparator.
- publication or escalation trigger.
- legal aid bridge or ENFORCEMENT_ABSENT_NO_DISCHARGE.

## 5. Retaliation discipline

```json
{
  "retaliation_protocol": {
    "risk_level": "low|medium|high|unknown",
    "mitigation_trigger": "none|sealed_only|legal_aid_alert|union_alert|journalist_hold|automatic_public_release|other",
    "parallel_retaliation_log_required": true,
    "emergency_contact_or_bridge": "required_or_reason_absent",
    "identity_disclosure_conditions": "required",
    "safe_contact_route": "required_or_reason_absent"
  }
}
```

A high-retaliation pack without mitigation is `WITNESS_RISK_UNCARRIED`.

## 6. Holder and custody discipline

```json
{
  "holder_record": {
    "holder_id": "required",
    "holder_type": "public_archive|lawyer|journalist|union|regulator|trusted_person|distributed_storage|other",
    "holder_independence_vector": {},
    "correlation_cluster": "required",
    "actor_relationship": "none|direct|indirect|unknown",
    "access_conditions": "required",
    "retention_terms": "required",
    "tamper_evidence_method": "hash|timestamp|signature|append_only_log|other",
    "safety_assessment": "required"
  }
}
```

Minimum rule: two decorrelated holder types, unless unsafe or impossible. If not met, state why.

## 7. Evidence taxonomy

```json
{
  "evidence_item": {
    "item_id": "required",
    "item_type": "observation|claim|inference|document|testimony|derived_analysis",
    "quality_status": "primary_contested|primary_uncorroborated|primary_corroborated|secondary|hearsay|unknown",
    "description": "required",
    "source": "required_or_protected",
    "date_observed": "required_or_unknown",
    "hash": "required_or_null_reason",
    "storage_location": "required_or_protected",
    "sensitivity": "low|medium|high|extreme",
    "metadata_redaction_check": "passed|failed|not_checked|not_applicable",
    "chain_of_custody": "required_or_reason_absent"
  }
}
```

The template must never force a harmed party to expose metadata that increases retaliation risk.

## 8. Asks, refusals, and non-response

```json
{
  "ask_record": {
    "ask_id": "required",
    "date_sent": "required",
    "recipient": "required",
    "request_text_or_summary": "required",
    "official_route_required_by_actor": "required_or_unknown",
    "actual_route_available_to_affected_scope": "required_or_unknown",
    "response": "provided|refused|partial|no_response|redirected|retaliatory",
    "response_due_date": "required_or_unknown",
    "evidence_id": "required_or_null",
    "silence_after_due_date_counts_as": "non_response_not_consent"
  }
}
```

## 9. Witness pack aggregation without doxxing

```json
{
  "aggregation_record": {
    "stream_id": "required_or_null",
    "correlation_method": "shared_actor|shared_location|shared_mechanism|shared_time_window|trusted_intermediary|privacy_preserving_hash|other",
    "doxxing_risk": "low|medium|high|unknown",
    "aggregation_trigger": "N_packs|same_mechanism|retaliation_pattern|external_challenger_request|other",
    "public_aggregate_allowed": true,
    "individual_identity_release_allowed": false
  }
}
```

Actor fake-pack flooding is treated as its own stream:

```text
fake_pack_flood_suspected := unusual_volume + actor_benefit + weak_provenance
```

Suspicion does not invalidate real packs. It triggers provenance review.

## 10. Escrowed Challenge Trust v0.3

Escrow cannot be set by the actor alone.

```json
{
  "escrow_record": {
    "escrow_id": "required",
    "amount_or_formula": "required",
    "adequacy_basis": "class_default|custodian_formula|court_order|regulator_rule|other",
    "actor_set_amount": false,
    "independent_adequacy_review": "required",
    "effect_radius_claimed_by_actor": "required",
    "effect_radius_challenge_route": "required",
    "broader_radius_applies_until_resolved": true,
    "escrow_release_conditions": "required",
    "challenger_funding_route": "required"
  }
}
```

If the actor controls the amount, custodian, scope, and data, the trust is a claim packet.

## 11. Public register and breakout pool

```json
{
  "breakout_pool_record": {
    "pool_id": "required",
    "pool_precommitment_proof": "required",
    "pool_funding_source": "public|escrow|mixed|unknown",
    "infrastructure_funding_independence": "required",
    "actor_vendor_percentage_cap": "required",
    "affected_side_strike_rights": "required",
    "proxy_capture_disclosure": "required",
    "proxy_of_last_resort": "required_or_reason_absent"
  }
}
```

If all clean tiers collapse, output `ENFORCEMENT_ABSENT_NO_DISCHARGE` and trigger witness fallback.

## 12. Insurance-backed carrier v0.3

Insurance is useful only where it funds prevention or adversarial challenge. Insurance that merely prices harm is a laundering machine.

```text
insurance_is_risk_transfer_not_repair
insurance_is_not_prevention_by_default
insurance_payout_for_stream_harm := FORBIDDEN
pricing_stream_harm_as_risk := LAUNDERING
insurability != legitimate_answerability
premium_payment != good_faith
```

Required conditions:

- third_party_beneficiary_rights for affected scopes where possible.
- adversarial office funded by pooled insurer mechanism, not individual actor.
- prevention margin clause: if prevention cost is lower than recurrence cost prevented, prevention must be required or coverage narrows.
- public exclusion register for uncarried actions where safe.
- anti-collusion audit where market concentration is high.

Do not use this carrier for sovereign actors, monopoly actors indifferent to insurance, captive insurance markets, catastrophic irreversible harm framed as insurable, or affected scopes unable to trigger claims.

## 13. Technical lockout and operational control

```json
{
  "technical_lockout_record": {
    "system_or_process": "required",
    "who_holds_keys_or_access": "required_or_unknown",
    "pause_route": "required_or_absent",
    "rollback_route": "required_or_absent",
    "log_access_route": "required_or_absent",
    "data_deletion_or_retention_control": "required_or_unknown",
    "model_weight_or_code_custody": "required_or_not_applicable",
    "actor_can_unilaterally_continue": true
  }
}
```

If the actor can continue unilaterally after a carried reading says stop, the reading has no lockout mass.

## 14. Attention and publicity

```json
{
  "attention_publicity_record": {
    "public_route": "none|sealed_trigger|journalist|regulator|court|public_archive|community_register|other",
    "suppression_risk": "low|medium|high|unknown",
    "safe_public_version_exists": true,
    "publication_trigger": "required_or_reason_absent",
    "who_can_activate_publication": "required_or_unknown",
    "attention_capture_risk": "low|medium|high|unknown"
  }
}
```

A record without safe circulation remains succession-only. That may still matter. It is not public pressure.

## 15. Test integrity manifest

Every hostile test or field test must include:

```json
{
  "test_manifest": {
    "target_files": [],
    "target_hashes": [],
    "tester_independence_vector": {},
    "pre_registered_null": "required",
    "claims_under_test": [],
    "symbols_used": [],
    "extensions_introduced_by_tester": [],
    "test_verdict_scope": "required"
  }
}
```

If the test lacks manifest discipline, its result may still be informative, but its verdict is quarantined.
