# Witness Pack Template v0.2.1 - Integrity Repair Layer

Status: CANDIDATE integrity repair over Witness Pack Template v0.2. Not legal advice, proof, certification, permission, closure, or safety guarantee.

## Purpose

v0.2 made the template materially stronger. v0.2.1 adds guardrails for real use: intake, compelled disclosure, small-N deanonymisation, trusted intermediary risk, non-monopoly, and explicit test status.

## 1. Human intake comes before schema

Do not give a frightened person a schema first. Use human questions, then convert to fields.

```text
1. What happened?
2. What are you afraid will happen if this is known?
3. Who already knows?
4. What proof exists, even if unsafe to share now?
5. What did you ask for?
6. Who did not answer, refused, delayed, or redirected you?
7. What is getting worse while you wait?
8. What details must stay sealed?
9. Who could safely hold a copy?
10. What would make this safer to file?
```

## 2. Compelled disclosure warning

Every holder must be checked for compelled disclosure risk.

```json
{
  "holder_compelled_disclosure": {
    "holder_id": "required",
    "jurisdiction": "required_or_unknown",
    "compulsion_route": "subpoena|court_order|employment_pressure|platform_request|police_power|unknown|other",
    "identity_at_risk": true,
    "content_at_risk": true,
    "mitigation": "split_custody|sealed_identity|legal_privilege|delayed_release|distributed_storage|other",
    "residual_risk": "low|medium|high|unknown"
  }
}
```

Legal custody may be unsafe when the legal system is part of the actor's pressure route.

## 3. Small-N deanonymisation

Aggregation can dox without names.

```json
{
  "small_N_risk": {
    "group_size_known_to_actor": "required_or_unknown",
    "distinctive_location_or_timing": true,
    "actor_can_infer_identity_from_pattern": true,
    "k_anonymity_floor": "required_or_reason_absent",
    "aggregation_allowed": "yes|no|only_sealed|affected_side_accepts_risk"
  }
}
```

Do not publish an aggregate if the aggregate itself identifies the witnesses.

## 4. Trusted intermediary record

```json
{
  "trusted_intermediary": {
    "intermediary_id": "required_or_null",
    "role": "intake|custody|aggregation|safe_contact|review|escalation|other",
    "independence_vector": {},
    "capacity_limit": "required",
    "succession_plan": "required_or_reason_absent",
    "burnout_or_overload_risk": "low|medium|high|unknown",
    "compelled_disclosure_risk": "low|medium|high|unknown"
  }
}
```

A trusted intermediary is not automatically safe. They are a concentration point.

## 5. Non-monopoly witness-pack rule

```trace
witness_pack_non_monopoly :=
  do_not_require_one_platform
  + do_not_require_one_custodian
  + do_not_require_one_registry
  + do_not_require_one_intermediary
```

If a pack only counts when filed through one service, the service becomes a subpoena target and kill switch.

## 6. Test status warning

A completed template is not proof. A simulated dry run is not a field test. A filed pack without a holder is a claim packet with missing custody mass.

```trace
pack_completed := not_proof
pack_deposited := custody_claim_not_justice
holder_refused := custody_mass_missing_but_useful_data
```
