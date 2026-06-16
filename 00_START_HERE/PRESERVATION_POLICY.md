# TRACE Preservation Policy

Status: repository control policy. Not validation. Not proof.

## Principle

```trace
no_loss :=
  never_replace_payload_with_summary
```

Summaries, front doors, registries and one-sheets are navigation aids. They do not replace the source artifacts.

## File policy

- Full ZIPs and binary payloads should be preserved externally or in GitHub Releases / large-file storage when appropriate.
- Text source files, indexes, registries, policies, ledgers and prompts belong in the repo.
- Generated compression surfaces belong in the repo only as current reading aids, not authority.
- Older versions should be archived, not silently overwritten.

## Canonical memory unit

```trace
memory_unit := operator
not: case OR essay OR relay_pack
```

A case teaches an operator.

A claim statuses an operator.

A test pressures an operator.

A review attacks an operator.

An operator remembers.

## Expansion gate

Before adding a new bootstrap:

```trace
new_bootstrap_gate :=
  reveals_new_operator
  OR pressure_tests_existing_operator
  OR breaks_existing_operator
```

If none applies, do not add the bootstrap. Use the Case Atlas instead.

## Kernel gate

No candidate branch may enter the Diagnostic Kernel until it has:

```trace
kernel_gate :=
  clear_activation_condition
  + clear_deactivation_condition
  + at_least_one_success_case
  + at_least_one_failure_case
  + one_breaker_case
  + demotion_rule
  + comparator_check
```

## Demotion rule

```trace
if_TRACE_cannot_lose_claims:
  TRACE_becomes_belief_system
```

Every active operator and claim needs a falsifier, demoter, and removal or freeze condition.

## Relay rule

Relay packs are compatibility artifacts.

```trace
relay_pack :=
  latest_surface
  + <=10_files
  not:
    source_canon
```

## No silent edits

Any lowered threshold, softened claim, changed operator status, or removed warning must be explicit.

```trace
no_silent_edits :=
  every_material_change
  -> patch_note_or_lineage_record
```
