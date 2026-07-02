# After-Fall v0.6.1 Integrity Repair - Revision History

Status: CANDIDATE. Not canon. Not final. Not validation. Not proof. Not permission. Not clearance.

## Source rule

This repair was made after committing v0.6 source into the TRACE repo under:

```text
after_fall/v0_6_operational_carrier/
```

v0.6.1 does not replace that source. It repairs three integrity defects found after the post-carrier review.

## Trigger

Fable's post-carrier review found that the deepest remaining defects were not more carrier machinery. They were:

```trace
missing_answer_type := instantiation + latency + naming_integrity
```

The sharpest structural warning was:

```trace
if TRACE_document_contains_carrier_interface_but_not_TRACE_grammar:
  object_name_does_not_match_object
```

The package also violated its own test discipline because the tenant/mould dry run had no test manifest, no tester independence vector, no pre-registered null, and no verdict scope.

## v0.6.1 repair set

```trace
v0_6_1_integrity_repair :=
  grammar_kernel_reanchor
  + dry_run_test_manifest_retrofit
  + non_monopoly_clause
```

Additional notes added because they are tightly coupled to the three repairs:

```trace
added_notes :=
  instantiation_readiness_gradient
  + trusted_intermediary_single_point_of_failure
  + compelled_disclosure_risk
  + carrier_latency_vs_harm_velocity
  + small_N_deanonymisation
  + NO_DISCHARGE_accumulation_location
  + mass_vector_openness
  + counter_streams
  + binding_route_discipline
  + intake_gap
```

## What this does not do

v0.6.1 does not claim that the carrier is solved. It does not supply enforcement, custodians, public registers, lawyers, tenants' unions, journalists, attention, or law.

It marks which parts are executable today and which require counterparty or institution building.

## Current next test

```trace
next_real_test :=
  one_real_witness_pack
  + one_real_case
  + one_real_holder_or_refusal
  + test_manifest
```

A holder refusal counts as data. It shows missing custody mass.
