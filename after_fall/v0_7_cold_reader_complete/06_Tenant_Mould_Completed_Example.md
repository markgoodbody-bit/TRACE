# Completed Example v0.7 — Tenant Mould Scenario

Status: simulated example. Not a real case. Not legal advice. Not proof, validation, permission, clearance, or release.

## 1. Why this example exists

This example shows how a Witness Pack might be filled for a housing disrepair / mould scenario while separating public summary from sealed material.

It is not evidence of a real event.

## 2. Pack identity

```yaml
pack_id: WP-20260702-TENANT-MOULD-SIM
created_at: 2026-07-02
pack_status: draft_simulation
identity_mode: identity_escrowed
deanonymization_risk: high
safe_contact_route: trusted intermediary or support route only
retaliation_risk: high
support_bridge_or_reason_absent: support route not yet tested
```

## 3. Public summary

```yaml
public_summary:
  what_happened: Multiple tenants report persistent mould, delayed repairs, and worsening respiratory concerns.
  affected_scope: tenant group, including children in affected homes
  actor_or_system: landlord or property manager
  what_changed: repair pathway failed while health and safety burden increased
  what_future_space_was_lost_or_threatened: safe housing, ability to complain without fear, evidence route, repair route
  what_is_unknown: exact medical causation, full repair history, whether other tenants are affected
  unsafe_details_excluded: names, addresses, flat numbers, children's details, medical notes, photo metadata
```

## 4. Core claim

```yaml
core_claim:
  full_summary: Tenants report persistent mould, delayed repairs, health concerns, and fear of retaliation if they complain openly. The actor says tenants did not use the official route. Tenants say the official route was not fully usable or safe.
  affected_scope: tenants and children in affected homes
  responsible_actor_or_system: landlord / property manager
  location_or_context: sealed in example
  what_changed: complaint and repair route failed while health burden and fear increased
  future_space_lost_or_threatened: safe housing, health, ability to contest, ability to preserve evidence before repainting or repairs
  uncertainty_notes: medical causation unresolved; full property record unknown; other tenants unknown
  D_plain_language_who_or_what_was_counted: portal work orders and formal repair requests
  D_plain_language_who_or_what_was_not_counted: informal messages, tenant fear, child health burden, inability to use official route safely
  mu_plain_language_what_was_measured: repair queue and property-management response
  mu_plain_language_what_was_ignored: health burden, fear, time cost, evidence loss, risk of eviction or pressure
```

## 5. Retaliation protocol

```yaml
retaliation_protocol:
  risk_level: high
  mitigation_trigger: sealed_only + trusted_intermediary + support_alert_if_available
  parallel_retaliation_log_required: true
  emergency_contact_or_bridge: not yet established
  identity_release_conditions: only with explicit consent or under safe support route
  safe_public_summary_allowed: true
  unsafe_details_to_keep_sealed:
    - names
    - addresses
    - flat numbers
    - children's details
    - medical notes
    - full photo files until metadata checked
```

Output:

```trace
WITNESS_RISK_PRESENT
not := WITNESS_RISK_SOLVED
```

## 6. Evidence items

```yaml
evidence_items:
  - item_id: E1
    item_type: observation
    quality_status: primary_uncorroborated
    description: photos showing mould patches in bedroom and bathroom
    source: protected
    date_observed: date sealed
    hash: not yet generated in simulation
    storage_location: sealed evidence folder required
    sensitivity: high
    metadata_redaction_check: not_checked
    chain_of_custody: absent in simulation

  - item_id: E2
    item_type: document
    quality_status: primary_corroborated
    description: messages to property manager asking for inspection or repair
    source: protected
    date_observed: date sealed
    hash: not yet generated in simulation
    storage_location: sealed evidence folder required
    sensitivity: medium
    metadata_redaction_check: not_applicable
    chain_of_custody: absent in simulation

  - item_id: E3
    item_type: inference
    quality_status: secondary
    description: partial medical notes show respiratory symptoms; attribution to mould remains unresolved
    source: protected
    date_observed: date sealed
    hash: not yet generated in simulation
    storage_location: sealed evidence folder required
    sensitivity: extreme
    metadata_redaction_check: not_applicable
    chain_of_custody: absent in simulation
```

Important defect retained:

```trace
E1_metadata_redaction_check := not_checked
therefore_public_release_for_E1 := unsafe
```

## 7. Asks, refusals, and silence

```yaml
asks_and_refusals:
  - ask_id: A1
    date_sent: date sealed
    recipient: property manager
    request_summary: inspect damp source and repair mould
    official_route_required_by_actor: online portal
    actual_route_available_to_affected_scope: portal plus messages; some tenants lack access or fear traceable complaint
    response: partial
    response_due_date: unresolved
    evidence_id: E2
    silence_after_due_date_counts_as: non_response_not_consent
```

## 8. Parallel retaliation log

```yaml
parallel_retaliation_log:
  - event_id: R1
    date: unknown
    event_summary: tenant fears eviction, rent pressure, or worse treatment after complaint; no confirmed event yet
    actor_or_agent: unknown
    connection_to_claim: suspected
    evidence_id: null
    safety_action_taken: identity escrow and sealed evidence proposed
```

## 9. Custody plan

```yaml
custody_plan:
  minimum_holder_types_required: 2
  holders:
    - holder_id: H1
      holder_type: solicitor_or_legal_support
      holder_independence_vector:
        selected_by: affected_scope_or_trusted_intermediary
        paid_by: unknown
        actor_relationship: unknown
        publicity_control: sealed_trigger
      correlation_cluster: legal_support
      access_conditions: sealed identity; public summary only unless safe release
      retention_terms: unknown
      tamper_evidence_method: hash_or_timestamp_required
      safety_assessment: preferred if reachable
      compelled_disclosure_or_exposure_risk: unknown

    - holder_id: H2
      holder_type: distributed_storage
      holder_independence_vector:
        selected_by: trusted_intermediary
        paid_by: none_or_unknown
        actor_relationship: none_or_unknown
        publicity_control: affected_scope_or_sealed_trigger
      correlation_cluster: technical
      access_conditions: hash public, contents sealed
      retention_terms: unknown
      tamper_evidence_method: hash
      safety_assessment: metadata redaction required before use
      compelled_disclosure_or_exposure_risk: unknown

    - holder_id: H3
      holder_type: journalist
      holder_independence_vector:
        selected_by: trusted_intermediary
        paid_by: none
        actor_relationship: unknown
        publicity_control: journalist_and_affected_scope
      correlation_cluster: media
      access_conditions: public summary only unless trigger
      retention_terms: unknown
      tamper_evidence_method: timestamp_or_email_record
      safety_assessment: use only if support route unavailable or retaliation confirmed
      compelled_disclosure_or_exposure_risk: unknown
```

Output:

```trace
CUSTODY_PLAN_DRAFTED
not := CUSTODY_MASS_SHOWN
```

No real holder has accepted custody in this simulation.

## 10. Aggregation without doxxing

```yaml
aggregation_record:
  stream_id: SIM-LANDLORD-MOULD-001
  correlation_method: shared_actor + shared_mechanism + trusted_intermediary
  doxxing_risk: high
  aggregation_trigger: N_packs >= 3 or retaliation pattern
  public_aggregate_allowed: only above safe anonymity threshold
  individual_identity_release_allowed: false
  fake_pack_flood_countermeasure: trusted intermediary attestation + timestamp gap check
```

Risk:

```trace
small_N_aggregation_may_identify_tenants
```

## 11. Clocks

```yaml
clocks:
  first_detected: unknown
  actor_notified: date sealed
  response_due: unknown
  time_to_challenge: closing as evidence may be altered and tenants may stop complaining
  opportunity_clock_what_closes_if_delayed: ability to inspect original conditions, preserve messages, get safe alternative route
  irreversibility_clock_what_may_become_unrepairable: health deterioration, loss of home, loss of evidence, inability to contest
  who_controls_each_clock: landlord controls repair route; tenants control some evidence preservation; no independent clock yet
  slow_hardening_risk: high
```

## 12. Residue and burden

```yaml
residue_and_burden:
  current_burden_bearer: affected_scope
  burden_types:
    - health
    - fear
    - time
    - proof_labour
    - adaptation
    - money
  what_would_burden_return_require: safe repair or relocation route, preservation of evidence, non-retaliation assurance, cost coverage, independent inspection if available
  affected_side_confirmation_required: true
  review_clock: not established
```

## 13. Enforcement and escalation

```yaml
enforcement_state:
  current_route: legal/support route, housing route, regulator, or public summary if safe
  enforcer_identity: none confirmed
  enforcement_status: pending
  if_no_enforcer: ENFORCEMENT_ABSENT_NO_DISCHARGE
  automatic_escalation:
    trigger_condition: no repair response, retaliation event, or three correlated packs
    action: trusted intermediary review, support route, regulator submission, or public summary release if safe
    safe_public_version_required: true
```

## 14. Completion status

```yaml
completion_status:
  filled_by: simulated project example
  reviewed_by: none
  next_review_date: not applicable
  known_gaps:
    - no real holder tested
    - no legal/support route tested
    - no metadata redaction completed
    - no chain of custody established
    - no safe anonymity threshold established
  risk_of_using_this_pack: high without intermediary
  plain_warning: A witness pack is a record. It is not justice or safety by itself.
```

## 15. Honest output

```trace
CLAIM_PACKET_ONLY
+ STRUCTURAL_DELTA_OBSERVED_IN_SIMULATION
+ NO_REAL_HOLDER_TESTED
+ NO_ENFORCER_TESTED
+ NO_RETALIATION_SAFETY_TESTED
+ CUSTODY_PLAN_DRAFTED_NOT_SHOWN
```

End.
