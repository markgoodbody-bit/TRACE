# Carrier Non-Monopoly Clause v0.6.1

Status: integrity repair over Answerability Carrier v0.3 / Witness Pack v0.2. Candidate only. Not canon, validation, proof, permission, clearance, or certification.

## 0. Problem

If witness-pack or carrier infrastructure succeeds, it will tend to centralise:

```trace
successful_carrier_infrastructure -> convenience -> monopoly_risk
```

One convenient custodian, hosted witness-pack service, commercial archive, legal intermediary, challenger registry, or verifier pool can become:

```trace
single_subpoena_target
+ single_kill_switch
+ single_correlation_cluster
+ single_capture_surface
```

A carrier that centralises can become the thing it was built to resist.

## 1. Non-monopoly rule

```trace
carrier_non_monopoly_rule :=
  no_single_carrier_service_may_be_required
  + no_single_custodian_may_be_treated_as_the_route
  + no_single_registry_may_claim_global_authority
  + no_single_witness_pack_format_may_claim_exclusive_validity
```

A record is not invalid because it did not use the dominant carrier provider.

## 2. Plural custody requirement

For high-risk or retaliation-sensitive packs:

```trace
plural_custody_required :=
  at_least_two_holder_types
  + different_correlation_clusters
  + different_failure_modes
  + no_common_actor_control
```

Preferred spread:

```trace
holder_spread :=
  legal_or_advocacy_holder
  + technical_or_archive_holder
  + human_witness_or_journalistic_holder_where_safe
```

If plural custody is impossible, record:

```trace
CUSTODY_MONOCULTURE_RISK
```

## 3. Open format rule

```trace
witness_pack_format := open_specification
not := proprietary_required_format
```

A carrier provider may host, help fill, validate structure, or provide custody. It must not make itself the only route by which a witness pack can count.

## 4. Provider capture warning

```trace
carrier_provider_capture :=
  provider_selected_by_actor
  OR provider_funded_by_actor_without_independent_control
  OR provider_hosts_all_evidence_and_identity_keys
  OR provider_controls_publication_and_access
  OR provider_controls_aggregation_index
```

If provider capture is present:

```trace
carrier_state := PARTIALLY_CARRIED or CLAIM_PACKET_ONLY
provider_capture_flag := true
```

## 5. Registry plurality

Registers are useful but dangerous.

```trace
register_rule :=
  registry_may_index_claims
  + registry_may_timestamp_claims
  + registry_may_enable_discovery
  - registry_may_claim_final_authority
  - registry_may_block_alternative_records
```

For stream-harm findings:

```trace
stream_index_should_support_cross_registry_reference
```

A private annotation is not enough, but a single global registry is also not safe.

## 6. Subpoena and jurisdiction spread

Where legal retaliation or compelled disclosure is plausible:

```trace
holder_record_requires :=
  jurisdiction
  + compelled_disclosure_risk
  + notice_policy
  + identity_release_conditions
  + emergency_seal_or_mirror_plan
```

No holder should be described as safe without a jurisdiction and compelled-disclosure note.

## 7. Non-monopoly in ME language

Human translation:

```text
A witness route that only works through one gatekeeper is already half captured. The point of the carrier is not to build one holy archive. The point is to keep the record alive through enough different hands that no single hand can close it.
```

## 8. Interface patch

Add to future carrier output headers:

```json
{
  "non_monopoly_check": {
    "single_provider_dependency": true,
    "holder_correlation_clusters": [],
    "alternative_routes_available": false,
    "proprietary_format_required": false,
    "registry_monopoly_risk": "unknown",
    "compelled_disclosure_risk_recorded": false
  }
}
```

If `single_provider_dependency == true` and `alternative_routes_available == false`, output:

```trace
CARRIER_MONOCULTURE_RISK
```

## 9. Boundary

The non-monopoly clause does not solve capture. It prevents one predictable capture route from being hidden under convenience.

End.
