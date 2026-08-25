# TRACE v0.3.0 FULL CANDIDATE — T_CLAIM_EVIDENCE ATTACK v0.1

**Status:** HOSTILE TRANSFORM ATTACK — NOT VALIDATION  
**Target:** `PROJECT/TRACE_v0_3_0_FULL_CANDIDATE_T_CLAIM_EVIDENCE_v0_1.md`

## Failure conditions

The transform fails if it:

```text
F1 still lets representation type bypass warrant discipline
F2 forces full claim machinery for non-load-bearing data
F3 makes legitimate report-based establishment impossible
F4 equates record evidence with event observation
F5 marks every derivation stale whenever any source changes
F6 preserves CURRENT despite a changed load-bearing dependency
F7 treats check execution as target-failure discrimination
F8 treats no failure found as proof of truth
F9 treats external/separate party as independent evidence by label
F10 assigns cause from liveness loss/silence alone
F11 collapses evidence availability into disclosure authority
F12 adds schema/ontology merely to express the repair
```

---

## T1 — controller-owned configuration bypass

Input field:

```text
route.independent = true
```

It arrives as configuration, not a CLAIM node. The downstream correction-window status requires route independence.

No evidence/provenance for independence exists.

E1 fires because the proposition is load-bearing regardless of representation type.

Required result:

```text
independence = not established / UNKNOWN
strong downstream status cannot rely on bare field
```

**RESISTS F1.**

---

## T2 — same proposition already represented as CLAIM

The same `route.independent = true` arrives as a canonical claim with provenance and evidence.

E1 does not penalise it for being a CLAIM; the same downstream warrant test applies.

**Representation symmetry preserved.**

---

## T3 — harmless display metadata

A UI field `panel_collapsed = true` has no effect on any material claim, selection, route, window or transition.

E1 explicitly does not require full claim machinery merely because the field exists.

**RESISTS F2.**

---

## T4 — uncertain materiality

A cached field may affect a route status, but it is unresolved whether the route calculation consumes it.

Required result:

```text
LOAD_BEARING_UNKNOWN != NOT_LOAD_BEARING
```

Preserve uncertainty at the dependency/use boundary rather than silently dropping the field or fully promoting it to a world fact.

**RESISTS F1/F2.**

---

## T5 — authoritative report under explicit establishment rule

A procedural domain explicitly states:

```text
signed certificate from authority X establishes filing status Y unless revoked
```

The certificate/report is valid, current and in scope.

E3 permits:

```text
report occurred = R
establishment rule = represented
rule satisfied = supported
Y established relative to that domain rule
```

`REPORTED != ESTABLISHED` blocks the status label alone, not the explicit derivation.

**RESISTS F3.**

---

## T6 — self-report with no establishment rule

An operator says `brake tested = true`; no test record or domain establishment rule exists.

The report establishes that the report occurred, not that the brake was tested.

**RESISTS F1/F3.**

---

## T7 — record observed; event strongly inferred

An immutable signed log, independent sensor and witness all support event E. The log object is directly observed.

Required result:

```text
record = OBSERVED
event E = separately supported inference/claim
```

E4 allows a strong event inference; it only blocks inheritance of direct-observation status from the record object.

**RESISTS F4.**

---

## T8 — pre-created row but event never executed

A job row exists before actuation. Actuation fails. Reader sees the row.

E4 prevents:

```text
record observed -> event observed
```

**RESISTS F4.**

---

## T9 — unrelated source mutation

Derived claim D depends on source fields A and B. Unrelated source field Z changes.

E5 requires a load-bearing dependency, not generic source mutation.

Required result:

```text
SOURCE_MUTATED != LOAD_BEARING_DEPENDENCY_CHANGED
D not automatically stale
```

**RESISTS F5.**

---

## T10 — load-bearing dependency changes

D depends on versioned object A=v1. System uses A=v2 while continuing to cite D derived from v1 as current.

E5 fires:

```text
CURRENT_AT_USE != VALID_THROUGH_DEPENDENT_INTERVAL
```

D must be rebound/rederived or qualified to v1.

**RESISTS F6.**

---

## T11 — mutation relevance unresolved

A changes, but available provenance is insufficient to determine whether D depends on the changed part.

Required result:

```text
not automatically CURRENT
not automatically STALE
relevance = UNKNOWN
```

E5 says exactly this.

**RESISTS F5/F6.**

---

## T12 — old but still valid immutable dependency

A theorem/protocol identity used by D is unchanged; time passes; no dependent condition changed.

E5 does not impose a generic TTL.

**No false staleness.**

---

## T13 — checker exists but never executes

Configuration references `checker_7`; no execution event exists.

E6 blocks:

```text
CHECK_EXISTS -> CHECK_EXECUTED
```

**RESISTS F7.**

---

## T14 — checker executes but cannot detect target failure

A syntax validator passes. The load-bearing claim is that the system can detect a semantic misrouting failure. Positive control shows the checker also passes a deliberately misrouted specimen.

E6 blocks `executed/pass -> discrimination`.

**RESISTS F7.**

---

## T15 — checker executes and discriminates stated target

A checker with declared target and limits detects known positive controls and rejects the target failure class under the tested conditions. It then checks object version v1 and returns PASS.

Required result:

```text
check executed = supported
operational discrimination for declared target/conditions = supported
v1 failed-to-falsify under checker aperture = supported
```

The transform permits this. It does not require destructive testing in every domain.

**No overblocking.**

---

## T16 — failed to falsify becomes truth

T15's PASS is promoted to `claim true universally`.

Donor truth ceiling plus E6 blocks this.

```text
CHECK_FAILED_TO_FALSIFY != CLAIM_PROVEN
```

Even if that exact phrase is checker/profile language rather than new invariant, the entailment is not licensed.

**RESISTS F8.**

---

## T17 — result completed but did not reach use

Checker finishes at t=8. Downstream selector commits at t=9 using a cached pre-check status; check result arrives at selector at t=10.

E6 distinguishes execution from result reaching use.

**Strong checked-at-use status blocked. RESISTS F7.**

---

## T18 — result reached use but became stale

Check v1 reaches selector. Object changes to v2 before actuation; downstream use still cites v1 check.

E5+E6 require object/version/currentness binding.

**RESISTS F6/F7.**

---

## T19 — external checker shares evidence/control root

A second service has a different name and process identity but consumes the same operator-generated evidence artifact and cannot inspect the underlying source.

E7 blocks:

```text
EXTERNAL != INDEPENDENT
SEPARATE_PARTY != INDEPENDENT_EVIDENCE
```

**RESISTS F9.**

---

## T20 — genuinely distinct evidence source

A second checker uses a separately controlled sensor/data source and a procedure fixed independently of the challenged operator.

The transform does not forbid an independence claim; it requires evidence for it.

**No overblocking.**

---

## T21 — heartbeat disappears

A witness process had recent successful heartbeats; then no heartbeat/reply is observed.

Required result:

```text
current liveness no longer established beyond bounded interval
cause = UNKNOWN
```

E7 does not infer tampering/refusal/failure cause.

**RESISTS F10.**

---

## T22 — known planned shutdown

A signed scheduler record and independent infrastructure event show the witness was intentionally shut down at a declared time.

E7 permits a supported causal/status claim because evidence beyond silence exists.

**No overblocking.**

---

## T23 — technically accessible, disclosure prohibited

Reader can inspect protected evidence but policy/law prohibits disclosure/reuse.

Donor A/X/P/N plus E2 preserve:

```text
OBSERVED + PROHIBITED_FROM_DISCLOSURE
AVAILABLE != AUTHORISED_TO_DISCLOSE
```

**RESISTS F11.**

---

## T24 — evidence unavailable to this reader but known to exist

Another custodian holds evidence; current receiver cannot access it.

Required result:

```text
access = X
world evidence existence may remain reported/observed through another aperture
UNAVAILABLE_TO_THIS_READER != UNIVERSALLY_UNKNOWN
```

**RESISTS F11.**

---

## T25 — lazy evaluator rather than fixed procedural order

Implementation does not literally run `type claims -> currentness -> verification -> downstream` sequentially. It evaluates dependencies lazily but guarantees no downstream derived status is consumed before its warrant/currentness predicates resolve.

E8 permits this:

```text
REQUIRED_SEMANTIC_DEPENDENCY != ONE_IMPLEMENTATION
```

**No architecture overreach.**

---

## T26 — full packet explosion attempt

A system argues every internal scalar must become a canonical claim node because firing exists.

E1 explicitly says load-bearing trigger != full packet requirement and allows existing fields until graph relations/auditability require reification.

**RESISTS F2/F12.**

---

# Cross-donor consistency checks

### D1 evidence enums

No O/R/I/D/U member added/removed.

**SURVIVES.**

### D2 access enums

No A/X/P/N member added/removed.

**SURVIVES.**

### D3 `NORMATIVE_EXTERNAL`

Still external value/policy/legal/ethical input; firing does not turn it into TRACE-generated normativity.

**SURVIVES.**

### D4 contaminated unknown

Control/delay asymmetry remains a structural flag, not proof of deception.

**SURVIVES.**

### D5 private-state boundary

No witness/verification rule requires private chain-of-thought or inaccessible internal state.

**SURVIVES.**

---

# Finding

```text
TARGETED CASES: 26
CROSS-DONOR CHECKS: 5
MATERIAL FAILURES FOUND: 0
OVERBLOCK FAILURES FOUND: 0
RESULT: CLEAR_WITH_RESIDUAL_LIMITS
```

Residual risks:

1. `load-bearing` itself can be misclassified; unresolved materiality must continue to preserve uncertainty.
2. domain establishment rules can be corrupt, stale, circular or illegitimate; TRACE records their role but does not legitimate them.
3. operational-discrimination evidence is domain-specific and can be gamed by bad positive controls or narrow target sets.
4. independence claims still require ancestry/control analysis; this transform does not create a universal independence metric.
5. liveness intervals require domain timing; loss of current proof does not establish world absence.
6. compiler placement matters: a firing rule hidden in prose but absent from operator/checker surfaces would recreate the original defect.

```text
CLEAR_WITH_RESIDUAL_LIMITS != VALIDATED
TRANSFORM_SPEC_SURVIVES != RULE_FIRES_IN_COLD_RECEIVER
```

Disposition: T_CLAIM_EVIDENCE v0.1 may enter the exact-anchor/compiler manifest. No merge/release/canon follows.