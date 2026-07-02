# Tenant Mould Witness Pack Dry Run — Test Manifest v0.6.1

Status: retrofit test manifest for `05_Witness_Pack_Dry_Run_Tenant_Mould_v0_1.md`. Candidate only. Not validation, proof, permission, clearance, legal advice, or real-world evidence.

## 0. Why this exists

The v0.6 dry run was useful but violated the package's own test-integrity rule because it lacked:

```trace
test_manifest
+ tester_independence_vector
+ pre_registered_null
+ verdict_scope
```

This file retrofits the manifest and downgrades the dry-run finding to its honest status.

## 1. Target artifact

```json
{
  "target_artifact": "05_Witness_Pack_Dry_Run_Tenant_Mould_v0_1.md",
  "target_package": "After-Fall v0.6 Operational Carrier Candidate",
  "target_repo_path": "after_fall/v0_6_operational_carrier/05_Witness_Pack_Dry_Run_Tenant_Mould_v0_1.md",
  "target_status": "simulated_dry_run"
}
```

## 2. Claims under test

The dry run tested whether Witness Pack v0.2 could represent a tenant/mould scenario better than v0.1 by adding:

```trace
public_summary_separated_from_sealed_evidence
+ retaliation_protocol
+ evidence_typing
+ asks_and_refusals
+ decorrelated_holder_plan
+ aggregation_without_identity_release
+ enforcement_absent_no_discharge
```

The dry run did **not** test whether:

```trace
legal_aid_exists
regulator_responds
journalist_accepts_pack
publicity_route_is_safe
holder_accepts_custody
landlord_is_forced_to_answer
```

## 3. Pre-registered null

```trace
pre_registered_null :=
  pack_completed_but_no_holder_accepts
  OR pack_completed_but_publication_unsafe
  OR pack_completed_but_no_enforcer_available
  OR pack_completed_but_no_actor_response
```

The null is not failure of the witness pack as succession carrier. It is evidence that the pack has not yet found enough carrier mass to bite.

## 4. Tester independence vector

```json
{
  "tester_independence_vector": {
    "selected_by": "project_internal",
    "paid_by": "none",
    "data_control": "project_internal_simulation",
    "scope_control": "project_internal",
    "enforcement_power": "none",
    "witness_access": "none_real_case_simulated_only",
    "time_control": "project_internal",
    "publicity_control": "none",
    "origin_correlation_cluster": "same_loop_as_template_builder",
    "contamination_flags": [
      "self_test",
      "same_loop_as_template_builder",
      "no_real_holder",
      "no_real_affected_party",
      "no_external_custodian"
    ]
  }
}
```

## 5. Verdict scope

Allowed finding:

```trace
DRY_RUN_STRUCTURAL_REPRESENTATION_CHECK
```

Forbidden finding:

```trace
field_test_passed
witness_pack_validated
carrier_works
justice_route_created
holder_acceptance_shown
```

## 6. Revised dry-run finding

Original claim:

```text
The v0.2 template can preserve the claim more safely than v0.1.
```

Reissued status:

```trace
CLAIM_PACKET_ONLY
+ STRUCTURAL_DELTA_OBSERVED_IN_SIMULATION
+ NO_REAL_HOLDER_TESTED
+ NO_ENFORCER_TESTED
+ NO_RETALIATION_SAFETY_TESTED
```

The useful defect admission survives:

```trace
pack_survives_but_does_not_bite
```

## 7. Manifest result

```trace
dry_run_verdict := quarantined_as_claim_packet_only
useful_defects := retained
next_test := real_holder_acceptance_or_refusal
```

## 8. Next valid field test

Minimum next test:

```trace
one_real_case_or_realistic_counterparty_case
+ one_real_holder_contacted
+ holder_acceptance_or_refusal_recorded
+ safety_review_before_publication
+ pre_registered_null
+ tester_independence_vector
```

If no holder accepts, output:

```trace
CUSTODY_MASS_ABSENT
+ WITNESS_PACK_NOT_YET_CARRIED
+ SUCCESSION_ROUTE_UNPROVEN
```

End.
