# Witness Pack Dry Run v0.1.1 - Tenant Mould Scenario with Test Manifest

Status: CANDIDATE test-manifest retrofit over the v0.1 simulated dry run. Not validation, proof, permission, clearance, legal advice, or field evidence.

## 1. Test manifest

```json
{
  "test_packet_manifest": {
    "target_artifact": "after_fall/v0_6_operational_carrier/04_Witness_Pack_Template_v0_2.md",
    "target_hash_from_manifest": "c8e480c012ecafeb7d67aca42c0503fc4fa97203d1fd9906cad7947969e3eab4",
    "test_artifact": "Witness Pack Dry Run Tenant Mould v0.1.1",
    "tester_identity": "internal_AI_generated_simulation",
    "tester_independence_vector": {
      "selected_by": "same_build_loop",
      "paid_by": "none",
      "data_control": "simulated_by_builder",
      "scope_control": "same_build_loop",
      "witness_access": "none_real",
      "time_control": "same_build_loop",
      "publicity_control": "none",
      "origin_correlation_cluster": "TRACE_ME_build_context",
      "contamination_flags": ["self_test", "no_real_holder", "no_real_witness", "no_external_counterparty"]
    },
    "pre_registered_null": "pack_completed_but_no_holder_accepts_or_no_safe_publication_route",
    "verdict_scope": "template_usability_simulation_only",
    "allowed_verdict": "CLAIM_PACKET_ONLY_WITH_USEFUL_DEFECTS",
    "not_allowed": "validation|field_success|proof_of_safety|proof_of_bite"
  }
}
```

## 2. Retrofitted verdict

The original dry-run sentence - that v0.2 preserves the claim more safely than v0.1 - is a design claim by the builder, not an independent test result.

Correct status:

```trace
dry_run_status := CLAIM_PACKET_ONLY_WITH_USEFUL_DEFECTS
```

The useful surviving finding is the defect admission:

```trace
pack_survives_but_does_not_yet_bite
```

## 3. Simulated scenario retained

Tenant group reports mould, respiratory illness, missed repairs, and fear of retaliation. Landlord denies knowledge and says tenants failed to use the official route. Tenants have photos, messages, partial medical notes, and fear eviction.

## 4. Added defects from manifest review

```trace
defects_added :=
  metadata_redaction_not_checked_on_high_sensitivity_item
  + no_real_holder_acceptance
  + no_real_legal_aid_bridge
  + no_compelled_disclosure_assessment
  + small_N_deanonymisation_not_resolved
```

## 5. Next valid dry run

```trace
next_valid_test :=
  real_or_external_holder_contacted
  + holder_accepts_or_refuses
  + refusal_logged
  + manifest_completed_before_verdict
```

A refusal is not failure. It is evidence that custody mass is missing.
