# TRACE Kernel Integration Map Delta After Realistic Comparator v0.1

Status: temporary integration-map delta / anti-staleness note.  
Parent file: `TRACE_KERNEL_INTEGRATION_MAP_v0_1.md`.  
Reason: the realistic comparator test landed after the last full integration-map sync. This file records the narrow delta without reopening the full map.

## 0. Current Head Note

New test file added:

```text
03_TESTS/TRACE_REALISTIC_COMPARATOR_CASE_SAR_ACTION_WINDOW_v0_1.md
```

Commit:

```text
e3c2bd84d62647cb84a388df813b4705d15ac348
```

## 1. Role of the New Test

Role: realistic comparator test with externally grounded threshold.

It tests:

```text
valid information-access threshold
separate practical action window
formal compliance versus functional correction reachability
valid threshold used for the wrong function
```

## 2. Result

The test shows a narrow partial delta:

```text
valid threshold, wrong function
```

Expanded:

```text
a threshold can be valid inside its own domain but insufficient for preserving the action window needed for meaningful correction
```

Status:

```text
TRACE_DELTA_PARTIAL_REALISTIC
not validation
```

## 3. Map Implication

The main integration map should next include this file under test surfaces.

It should update current achieved deltas to include:

```text
TRACE distinguishes numerical comparison from authorised threshold use.
TRACE distinguishes valid threshold compliance from functional correction reachability.
```

## 4. Next Discipline

No new core files.

Next useful work:

```text
documented case test
actual timeline
actual documents
explicit no-card comparator
```

## 5. Guardrail

This delta file is not a substitute for a full map sync.

It exists to avoid losing the state if the full map is not edited immediately.
