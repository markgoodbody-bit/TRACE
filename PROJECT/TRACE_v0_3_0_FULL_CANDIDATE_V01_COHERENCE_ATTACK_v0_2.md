# TRACE v0.3.0 full candidate v0.1 — coherence attack v0.2

**Date:** 2026-08-25  
**Current target:** `PROJECT/TRACE_FORMAL_SEED_v0_3_0_FULL_WORKING_CANDIDATE_v0_1.md`  
**Current target SHA-256:** `ff01192bc2e489739984b57f9e5f1904a3653b3b4d1215f64a21d5bd30c13aa8`  
**Status:** MATERIAL NARROW FINDING / REPAIR REQUIRED  
**Claim ceiling:** self-attack evidence only; not validation, release, canon, authority, permission or clearance.

## Prior finding F01 — local validator ancestry prose

F01 was found on the first generated candidate (`0da980f51c16508c3420ed05eec7b9f767d73856516cab46b65b4bb6a7719b17`) and repaired in the compiler. The current target now correctly states that v0.3.0 is a generated full working candidate from released v0.2.7 and that a v0.2.7 packet is not silently relabelled as v0.3.0.

```text
DETERMINISTIC_BUILD_PASS != COHERENCE_ESTABLISHED
DONOR_TEXT_VALID_IN_DONOR != DONOR_TEXT_VALID_AT_NEW_USE_SITE
```

F01 remains part of failed ancestry and is not rewritten as if the first build had been clean.

## Finding F02 — correction-window discipline not propagated into brake / rollback use-sites

The current candidate's [8.1]–[8.3] timing repair requires strong correction-window claims to bind target/scope/boundary/capability/downstream use, establish a common temporal basis, and use interval-safe bounds when uncertainty is material.

Retained [8.8], however, still states point inequalities:

```text
t_brake_done < t_commit

t_rollback_done < t_irreversible
```

and says rollback can preserve the threatened path when executable and before `t_irreversible`.

The connected-brake surfaces also retain weaker shortcuts:

```text
[17.2] latency lower than commitment time
[17.3] completes before practical irreversibility
```

These statements can bypass the stronger [8.1]–[8.3] contract by treating a point estimate, generic commitment time, or generic practical irreversibility as sufficient for a strong brake/rollback conclusion.

This is one propagation class across [8.8], [17.2], and [17.3], not three semantic roots.

### Failure cases

1. Brake completion and commitment estimates are `8s` and `10s`, but their supported intervals are `[6,12]` and `[9,11]`. The point ordering says the brake is earlier; guaranteed precommit is not established.

2. Rollback completes before one represented system-level boundary but after the load-bearing target boundary for the affected individual scope. Generic `t_irreversible` launders the scope/target substitution.

3. A rollback action completes before the target boundary but does not restore the target state. Timing fit alone is silently upgraded into preservation/restoration.

4. Brake latency and commitment deadline use the same unit but different or unsupported reference events. Numeric comparison is not a supported temporal ordering.

### Required repair

For a strong guaranteed precommit claim under interval uncertainty:

```text
upper(t_brake_done) < lower(t_commit)
  -> GUARANTEED_PRECOMMIT_FOR_REPRESENTED_BINDINGS
```

Only under a supported common temporal basis and the represented brake/commitment bindings. A point shorthand may remain only as a bounded special case where the event times are supported as sufficiently point-bounded for the stated use.

For rollback timing:

```text
upper(t_rollback_done) < lower(t_target_boundary)
  -> ROLLBACK_COMPLETES_BEFORE_BOUNDARY_FOR_REPRESENTED_BINDINGS
```

where target, affected scope, boundary condition, capability/route context and temporal basis are explicit. This timing relation does **not** establish restoration or path preservation. The reached/restored target state remains a separate load-bearing proposition.

If bounds overlap, temporal bases cannot be joined, a material target/scope/boundary binding is unresolved, or the rollback route is not executable, preserve `UNKNOWN` for the strong timing claim.

### Preserve

```text
BRAKE_POINT_ESTIMATE_BEFORE_COMMIT != GUARANTEED_PRECOMMIT
ROLLBACK_POINT_ESTIMATE_BEFORE_BOUNDARY != GUARANTEED_RESTORATION
ROLLBACK_BEFORE_GENERIC_IRREVERSIBILITY != TARGET_STATE_RESTORED
BRAKE_LATENCY_REPORTED != BRAKE_COMPLETION_BOUND
FAST_ENOUGH_CLAIM_REQUIRES_COMMON_TEMPORAL_BASIS
ROLLBACK_COMPLETED_BEFORE_BOUNDARY != RESTORED_STATE
SAME_UNIT != SAME_REFERENCE_EVENT
POINT_ESTIMATE_FITS != GUARANTEED_OPEN
```

## Classification

F02 is a propagation/coherence failure of `T_CLOCK_ROUTE` into retained brake/rollback surfaces. It does not earn a new primitive, node type, relation type, evidence/access state, claim kind, semantic root, scheduler, process object, or minimum-schema field.

## Disposition

Repair the full compiler with one named brake/rollback timing-binding transform and fail-closed regression checks. Preserve the current target and this finding as evidence. Do not merge, release or canonise from this result.
