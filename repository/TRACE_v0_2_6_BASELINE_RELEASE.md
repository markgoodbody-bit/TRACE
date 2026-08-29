# TRACE v0.2.6 baseline release

**Release ID:** `TRACE-v0.2.6-FORMAL-BASELINE`  
**Decision date:** 2026-08-05  
**Human release authority:** Mark  
**Status:** active released formal baseline  

```text
RELEASED
ACTIVE_FORMAL_BASELINE
NOT_CANON
NOT_VALIDATED
NOT_AUTHORITY
NOT_PERMISSION
NOT_CLEARANCE
```

## Released object

```text
TRACE_FORMAL_SEED_v0_2_6.md
```

Exact compiled source commit:

```text
e4df6e9bb7cc6e236395836e41edc6d7025985e6
```

Exact released object blob:

```text
5e50886f20bceef63be90456cae7f7f7f895bcd6
```

The released object is byte-identical to the compiled working candidate reviewed and merged through PR #18. Promotion changes its repository status and active-baseline role; it does not rewrite the reviewed formal object.

## Baseline succession

`TRACE_FORMAL_SEED_v0_2_6.md` supersedes `TRACE_FORMAL_SEED_v0_2_5.md` as the active formal baseline.

`TRACE_FORMAL_SEED_v0_2_5.md` remains preserved as the reviewed predecessor and last pre-v0.2.6 baseline. It is not silently relabelled or deleted.

## Admitted formal change

The release carries the bounded v0.2.6 repair:

```text
TARGET_SET_SELECTION_IS_APERTURE_BEARING
ACCOUNTING_AND_COVERAGE_ARE_APERTURE_RELATIVE
```

It also preserves these ceilings:

```text
TARGET_SET_RECORDED != TARGET_SET_COMPLETE
COVERAGE_CHECK_PASSED != DILIGENCE_ESTABLISHED
DIVERGENT_READINGS != AUTHORITY
AUTHORITY_HANDOFF_RECORDED != AUTHORITY_LEGITIMATED
CONTEST_ROUTE_RECORDED != CONTEST_SUCCEEDED
BRAKE_ACTIVATION_RECORDED != TRANSITION_INTERRUPTED
TRANSITION_INTERRUPTED != HARM_PREVENTED
```

No new primitive, node type, edge type, port, controlled-vocabulary member, required packet field, selector, value rule, or moral authority was introduced.

## Review and evidence boundary

Claude's original hostile review returned `NARROW`. The two evidenced findings were accepted and repaired before compilation:

1. package-integrity checks were hardened against gutted artefacts and whitespace-only false failures;
2. the F03/F04 target-set-aperture containment warrant was made explicit.

The requested additional repaired-head Claude re-review was not received before Mark instructed Framework to proceed. That is recorded as a human release decision, not Claude clearance, agreement, refusal, or validation.

At the final compiled head, both the full-seed compilation workflow and the transition-package integrity workflow passed. Those checks establish deterministic compilation and declared-contract integrity only. They do not establish semantic adequacy, operational effectiveness, world validity, moral correctness, or decision advantage.

## Release meaning

This release means that v0.2.6 is now the formal version to use, cite, test, and revise from unless an explicit later version supersedes it.

It does not make TRACE canon, a certification system, a policy authority, or a permission machine.
