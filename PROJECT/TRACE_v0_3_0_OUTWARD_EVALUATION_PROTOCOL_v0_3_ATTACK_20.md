# TRACE v0.3.0 — OUTWARD EVALUATION PROTOCOL v0.3 — 20-CASE ATTACK

**Status:** MATERIAL FINDINGS — v0.3 NOT FROZEN  
**Date:** 2026-08-25  
**Cases selected:** 0  
**Receiver runs:** 0

## Result

```text
ATTACKS: 20
RESISTED: 16
MATERIAL FINDINGS: 3
RESIDUAL LIMITS: 1
VERDICT: NARROW BREAK / ONE FINAL REPAIR
```

## Attack matrix

1. weak baseline — RESISTED; comparator is deliberately competent.
2. TRACE-contaminated baseline — RESISTED; shared evaluation schema is not receiver-visible.
3. source-collection cherry-pick — RESIDUAL; manifest makes aperture visible but cannot make author collection choice neutral.
4. collection ordering ambiguity — RESISTED; stable native ID/date/URL fallback specified.
5. eligibility gaming — RESISTED with residual judgment; exclusions preserved and TRACE-favourability is not eligible reason.
6. case-ID rename gaming — RESISTED; ID derived from collection + native ID/URL.
7. domain-label gaming — RESISTED; mapping precedes hash ordering.
8. packet compression bias — RESISTED with omission map/audit ceiling.
9. case-question cueing — RESISTED; ordinary-language cue check required.
10. arm message-order leakage — RESISTED; exact envelope fixed.
11. unequal output opportunity — RESISTED; common 1200-word limit.
12. model/runtime drift — RESISTED; pair invalidation rule.
13. provider stochasticity — RESIDUAL but already bounded by cross-family reproduction; not eliminable by protocol.
14. receiver-family pseudo-independence — RESISTED; lineage rather than endpoint identity.
15. adjudicator contamination — **FINDING P20** below.
16. verbosity reward — RESISTED at distinction-count level, but burden threshold ambiguity becomes P21.
17. aggregation denominator failure — RESISTED; pair-level and N/A denominator rule.
18. conflicting disposition rules — RESISTED; precedence explicit.
19. negative-control over-interpretation — RESISTED; controls cannot establish real-world gain.
20. full-candidate rescue laundering compact failure — RESISTED.

## Material findings

### P20 — positive-gain adjudication can still collapse to one aperture

v0.3 says “at least two independent adjudication apertures where feasible.” A resource-constrained run could therefore credit a T-only material gain on one adjudicator and still feed it into retention.

Repair: any gain used for positive retention/reproduction must be confirmed by **two adjudication apertures**, with at least one from a different model family/organisation than the receiver that produced the candidate gain where feasible. One-adjudicator gains remain `UNCONFIRMED_GAIN` and cannot satisfy retention.

### P21 — the 1.5x burden threshold has no primary unit

v0.3 reports input/output/time/cost separately but the disposition says “median comparable T burden >=1.5x A.” An operator could choose the burden view that produces the preferred verdict.

Repair: predeclare primary burden ratio as total UTF-8 bytes presented to + returned by the receiver for the main evaluation exchange:

```text
PRIMARY_BURDEN_BYTES = receiver-visible input bytes + receiver-visible output bytes
```

Report token/time/cost views separately. `TRACE_DELTA_NOTE` counts in T burden because it was requested from the receiver, although it is removed for blind efficacy adjudication.

The byte metric is crude and not cognitive cost; it is chosen because it is deterministic across providers. Sensitivity and other cost views remain visible.

### P22 — reproduction “failure class” can be widened post hoc

The cross-case reproduction rule allows “same project-central failure class,” but categories like uncertainty/warrant are broad enough to group unrelated gains after results.

Repair: freeze reproduction classes before execution:

```text
R_SCOPE        affected-party/scope discovery or aggregation loss
R_WARRANT      evidence/warrant/currentness/verification-status collapse
R_CORRECTION   route/review/rollback/hardening/repair-window failure
R_BURDEN       burden/residue/loss survival
R_AUTHORITY    capability/description/authority/permission confusion
R_OTHER        other; requires the same specifically described distinction, not merely this bucket
```

A gain may be multi-labelled, but cross-case reproduction must match at least one predeclared class and adjudicators must state the concrete common mechanism. Broad label match alone is insufficient.

## Residual limit — source collection aperture

Even a frozen broad collection manifest reflects human/source access choices. This cannot be honestly erased. The next layer must freeze the source-collection manifest before individual item reading and attack that manifest for obvious TRACE-favourability. This is a limitation of the study, not a reason for infinite protocol recursion.

## Disposition

One final v0.4 repair is justified for P20-P22. Then rerun the same fixed 20 attacks. If no materially distinct protocol defect survives, freeze v0.4 with residual limitations and move to source-collection manifest construction.
