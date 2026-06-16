# TRACE Memory Architecture v0.1

Date: 2026-06-16  
Status: control architecture for remembering and recording TRACE structures; not theory validation.

## Problem

```trace
discovery_rate > memory_structure
```

The project has generated bootstraps, front doors, claims, audits, review digests, handoffs, relay packs, and compression surfaces. The danger is not simple file count. The danger is **overlapping authority** and **loss of structural deltas**.

## Core Correction

```trace
memory_unit :=
  operator
  not:
    case
    essay
    relay_pack
```

A case teaches an operator.  
A claim statuses an operator.  
A test pressures an operator.  
A review attacks an operator.  
A handoff transmits a temporary surface.

## Folder / Artifact Roles

```trace
TRACE_memory_architecture :=
  00_SOURCE_CORE
  01_OPERATOR_REGISTRY
  02_BOOTSTRAP_CASES
  03_CLAIMS_LEDGER
  04_TESTS_AND_DEMOTIONS
  05_EXTERNAL_REVIEW_DIGEST
  06_CURRENT_FRONT_DOOR
  07_RELAY_PACK
  99_ARCHIVE
```

## Authority Order

```trace
authority_order :=
  1_OPERATOR_REGISTRY
  2_CLAIMS_LEDGER
  3_DEMOTION_PROTOCOL
  4_DIAGNOSTIC_KERNEL
  5_BOOTSTRAP_CASES
  6_CONCORDANCE
  7_EXTERNAL_REVIEWS
  8_HANDOFFS_AND_RELAY_PACKS
```

This does not mean the bootstraps are less important. It means they are **discovery and teaching surfaces**, not the canonical memory of the structure.

## No-Loss Rule

```trace
no_loss_rule :=
  every_new_bootstrap
  must:
    name_operator
    + add_or_update_registry_row
    + add_claim_status_if_needed
    + add_falsifier_or_demoter
    + record_lineage
```

## New Bootstrap Gate

```trace
no_new_bootstrap_unless :=
  reveals_new_operator
  OR pressure_tests_existing_operator
  OR breaks_existing_operator
```

If a case only repeats an existing operator, it belongs in the Case Atlas, not as a new bootstrap.

## Front Door Rule

There should be one current front door at a time.

```trace
front_door_rule :=
  latest_front_door
  points_to:
    operator_registry
    + top_20_claims
    + diagnostic_kernel
    + relay_pack
```

Older front doors become archive, not authority.

## Relay Rule

Relay packs are compatibility artifacts only.

```trace
relay_pack :=
  <=10_files
  + latest_surface
  not:
    source_canon
```

## Audit Rule

Every major expansion must produce either:

```trace
expansion_control :=
  operator_registry_update
  OR demotion_record
  OR explicit_no_operator_added_note
```

## Current State

The current operator registry has 28 seed operators. Some are core, some patterned, some candidates. Candidate branches are deliberately held out of Kernel v0.3.

End.
