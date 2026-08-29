# TRACE v0.3.0 fixed-value discipline test record v0.1

**Status:** BOUNDED TEST EXECUTED — NOT RELEASE — NOT CANON — NOT VALIDATION
**Date:** 2026-08-29
**Target:** `PROJECT/TRACE_v0_3_0_MINIMUM_SCHEMA_CANDIDATE_v0_1.json`
**Runner:** `tools/test_trace_v030_fixed_value_discipline.py`

## Review trigger

A warm technical review correctly identified five required discipline fields constrained to `false` and argued that they imposed burden without discriminating understanding.

The strong form of that claim is not yet established. A `const: false` field can mechanically reject omission and `true`. It cannot establish that an author understood or applied the non-entailment in the represented world.

## Bounded test

The runner:

1. validates the schema as Draft 2020-12;
2. constructs a mechanically minimal positive instance from required schema structure;
3. verifies that the positive control passes;
4. counts required discipline group objects and required fields;
5. removes each fixed declaration and requires rejection;
6. flips each fixed declaration to `true` and requires rejection;
7. verifies whether the positive control can pass with all discipline reference arrays empty.

The target fields are:

```text
transition_set.uncertainty_selects_transition
clock_typing.deadline_entails_irreversibility
clock_typing.hardening_entails_irreversibility
scope_granularity.aggregate_recovery_repairs_individual_loss
evidence_custody.control_alone_establishes_deception
```

## Decision rule

- If omission or `true` is accepted, the corresponding declaration does not discriminate its declared packet-level target and the schema needs repair.
- If both are rejected, describe the declaration as shape/value-discriminating, not as proof of understanding.
- If an otherwise minimal packet with empty discipline reference arrays passes, preserve that as the semantic ceiling: declaration acceptance does not establish a basis or real application.
- Do not drop or replace fields on this test alone. Their comparative activation/population burden remains an empirical question for outward evidence.

```text
CONST_FIELD_REJECTS_TRUE != AUTHOR_UNDERSTOOD_DISTINCTION
REQUIRED_DECLARATION != WORLD_APPLICATION
SCHEMA_DISCRIMINATION != SEMANTIC_DISCRIMINATION
```

## Execution result

Executed from repository root:

```text
python tools\test_trace_v030_fixed_value_discipline.py --json
```

Observed validator library: `jsonschema 4.25.1`.

Observed result:

```text
status: PASS
Draft 2020-12 schema check: PASS
mechanically minimal positive control: PASS
required discipline group objects: 5
required fields inside discipline groups: 31
total required discipline elements counting group objects: 36
fixed false declarations: 5
missing declaration rejected: 5 / 5
true value rejected: 5 / 5
minimal packet with every discipline reference array empty: ACCEPTED
```

## Bounded disposition

The fields are not checks that can never fail. They discriminate presence and the prohibited Boolean value at packet shape/value level.

They also do not establish comprehension, basis, or world application. A template can populate them, and the schema accepts them with empty discipline reference arrays.

Keep the fields unchanged pending comparative burden evidence. Count their population cost in the outward study where they actually fire. Do not describe schema acceptance as semantic application, and do not remove the declarations merely because all conforming packets carry the same permitted value.
