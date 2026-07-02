# Answerability Carrier v0.3.1 - Integrity Repair Layer

Status: CANDIDATE integrity repair over Answerability Carrier v0.3. Not canon, validation, certification, proof, permission, compliance, or clearance.

## Purpose

v0.3 gave carrier readings more material mass. v0.3.1 repairs integrity defects found after review: instantiation path, trusted intermediary risk, compelled disclosure, carrier latency, small-N deanonymisation, non-discharge accumulation, mass-vector closure risk, counter-streams, binding-route discipline, intake gap, and carrier monoculture.

## 1. Deployment readiness gradient

Every carrier component must declare deployment status.

```trace
deployment_readiness :=
  executable_today
  | requires_counterparty
  | requires_institution_building
  | unavailable_under_current_conditions
```

Minimum examples:

```trace
witness_pack_basic := executable_today
trusted_holder_acceptance := requires_counterparty
public_register := requires_institution_building
escrowed_challenge_trust := requires_counterparty + legal_contract
insurance_backed_carrier := requires_institution_building
technical_lockout := requires_precommitment
sovereign_route := unavailable_unless_law_or_countervailing_power_exists
```

If a component is not executable today, the packet must not imply that it currently carries the reading.

## 2. Trusted intermediary risk

The trusted intermediary is load-bearing and cannot remain a magic box.

```json
{
  "trusted_intermediary_record": {
    "intermediary_id": "required_or_null",
    "role": "intake|custody|aggregation|safe_contact|review|escalation|other",
    "selected_by": "required",
    "paid_by": "required_or_none",
    "independence_vector": {},
    "capacity_limit": "required",
    "burnout_or_overload_risk": "low|medium|high|unknown",
    "succession_plan": "required_or_reason_absent",
    "compelled_disclosure_risk": "low|medium|high|unknown",
    "capture_risk": "required"
  }
}
```

One captured or exhausted intermediary can collapse many packs. A carrier depending on one intermediary must output `INTERMEDIARY_SINGLE_POINT_OF_FAILURE`.

## 3. Compelled disclosure risk

Safe custody is jurisdictional. Lawyers, courts, regulators, journalists, unions, and platforms can be compelled or pressured.

```json
{
  "compelled_disclosure_risk": {
    "holder_id": "required",
    "jurisdiction": "required_or_unknown",
    "likely_compulsion_route": "subpoena|court_order|employment_pressure|platform_request|police_power|unknown|other",
    "identity_material_at_risk": true,
    "content_material_at_risk": true,
    "mitigation": "sealed_identity|split_custody|legal_privilege|distributed_storage|delayed_release|other",
    "residual_risk": "low|medium|high|unknown"
  }
}
```

If the ordinary legal route is part of the actor's pressure route, ordinary legal custody may be unsafe.

## 4. Carrier latency vs harm velocity

The correction inequality applies to the carrier itself.

```trace
if harm_velocity > carrier_latency:
  only_prepositioned_masses_count
  carrier_state := CARRIER_TOO_SLOW_FOR_CLASS unless technical_lockout_or_tripwire_precommitted
```

Human-institutional carriers cannot honestly claim to control machine-speed harm after deployment. For high-velocity classes, technical lockout, logging, tripwires, and revocation must be pre-positioned.

## 5. Small-N deanonymisation

Aggregation can identify people even when names are withheld.

```trace
small_N_deanonymisation_risk :=
  actor_side_knowledge
  + small_group_size
  + distinctive_timing_or_location
  + aggregation_trigger_visibility
```

```trace
aggregate_only_if :=
  k_anonymity_floor_met
  OR affected_side_explicitly_accepts_risk
  OR safety_override_recorded_with_reason
```

`N_packs >= 3` is not automatically safe. N must reflect what the actor already knows.

## 6. NO_DISCHARGE accumulation location

`ENFORCEMENT_ABSENT_NO_DISCHARGE` only accumulates if a ledger survives.

```json
{
  "non_discharge_ledger": {
    "ledger_location": "public_register|escrowed_archive|trusted_intermediary|private_pack_only|none",
    "holder_independence_vector": {},
    "stream_id": "required_or_null",
    "cross_case_index_available": true,
    "access_conditions": "required",
    "if_private_only": "private_annotation_not_stream_evidence_yet"
  }
}
```

If no cross-case location exists, stream logic remains latent.

## 7. Open mass vector

Nine masses must not be read as complete.

```trace
mass_vector_is_open := true
new_mass_claim := challenger_may_assert_missing_mass
```

Candidate masses already identified:

```trace
candidate_masses := legitimacy_capital + jurisdictional_exit
```

## 8. Counter-streams

The witness pack can be used symmetrically by power.

```trace
counter_stream_risk :=
  actor_files_parallel_packs_against_affected_scope
  + actor_has_better_records
  + actor_has_faster_attestation
  + actor_can_frame_affected_party_as_source_of_harm
```

Counter-streams are not automatically false. They require power-differential analysis:

```trace
whose_packs_get_attested_faster?
whose_records_are_presumed_official?
who_pays_to_answer?
who_is_punished_by_the_existence_of_the_record?
```

## 9. Binding-route discipline

Rules written in binding voice must say what binds them.

```json
{
  "binding_route": {
    "rule_id": "required",
    "binding_language": "must|forbidden|required|blocked|invalid|other",
    "binds_via": "law|contract|escrow|technical_lockout|public_register|custodian_policy|institutional_adoption|none",
    "if_none": "aspirational_until_adopted_by:<actor_or_institution>",
    "claim_ceiling": "no_current_force_without_bind_route"
  }
}
```

Without `binds_via`, the rule is a design claim, not an operational constraint.

## 10. Intake gap

A frightened person on a phone cannot be expected to fill JSON.

```trace
intake_instrument_required := true
```

Human intake order:

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

The schema is for conversion after intake, not for first contact.

## 11. Non-monopoly clause

Carrier infrastructure must not become one convenient chokepoint.

```trace
carrier_non_monopoly_clause :=
  no_single_required_custodian
  + no_single_required_register
  + no_single_required_template_service
  + no_single_required_intermediary
  + plural_decorrelated_paths_preferred
```

```trace
carrier_monoculture_risk :=
  subpoena_target
  + correlation_cluster
  + kill_switch
  + capture_multiplier
```

If one witness-pack service, custodian, registry, or intermediary becomes necessary for recognition, the carrier has recreated the problem it was built to resist.

## 12. Next real test

```trace
next_real_test :=
  one_real_witness_pack
  + one_real_case
  + one_real_holder_or_refusal
  + test_manifest
```

A refusal by a holder is data. It means custody mass is missing.
