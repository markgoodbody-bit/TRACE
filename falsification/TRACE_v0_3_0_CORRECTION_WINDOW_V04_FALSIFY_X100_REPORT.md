# TRACE v0.3.0 — correction-window v0.4 falsify x100 + drift audit

**Audit target commit:** `09cb55f55cc6ccd5eede85b47cd80c32592b771b`  
**Audit target blob:** `9f8c2637276a862a31045cfffa35e02f6b548ef7`  
**Target:** `PROJECT/TRACE_v0_3_0_CORRECTION_WINDOW_REPAIR_CANDIDATE_v0_4.md`  
**Predecessor commit:** `5afcf629dbbf96eff439491d227ca1d0600773f5`  
**Predecessor blob:** `43e766925de0301eaec9b3c4c52c37cc62222bdd`  
**PR:** `#38` / `framework/trace-v0-3-0-working`

## Verdict

```text
NARROW — DO NOT INTEGRATE v0.4 AS WRITTEN
```

The visibility repair survives: expose deadline control, target linkage, provenance, custody and whether a nondeclarer check route exists. The proposed `SELECTOR_PROBLEM_REPAIRED` sufficient-condition compression does not survive. Visibility of selector dependence is not repair of that dependence, and an external route can be cosmetic when it shares the same evidential/control root, is not exercised, targets the wrong proposition, or cannot return before hardening.

```text
probe_count:              100
resisted_count:            59
finding_probe_count:       36
bounded_limit_count:        5
material_finding_classes:  10
verdict:                 NARROW / NO SPINE INTEGRATION
```

These are hostile semantic/transfer probes against the exact Markdown object plus repository/coordination drift checks. They are not a hosted executable mutation suite and do not constitute validation.

## Material findings

### F1 — exposure is not repair

Branch B of the terminating rule calls the selector problem repaired when no external check exists and dependence is merely made explicit. That prevents laundering but leaves the selector vulnerability unresolved.

```text
SELECTOR_DEPENDENCE_EXPOSED != SELECTOR_PROBLEM_REPAIRED
```

### F2 — checkable is not checked

v0.4 sometimes lets existence of a nondeclarer route support a stronger result. A route that could test a claim is not evidence that the claim survived that test.

```text
CHECK_PATH_EXISTS != CHECK_EXECUTED
CHECK_EXECUTED != CLAIM_SURVIVED_CHECK
```

### F3 — route independence is not evidential independence

`not controlled solely by the selector/declarer` is too weak. Joint control, unilateral veto, selector-produced public APIs, captured verifiers and copied upstream records can all create cosmetic externality. Independence must be assessed over dependency/control roots, not actor count or route label.

### F4 — the falsifier must target the exact load-bearing proposition

A verifier can check a hash, current deadline or public rule while the actual load-bearing claim is physical state, non-acceleration authority or private interpretation.

```text
CHECKED_EVIDENCE != CHECKED_PROPOSITION
```

### F5 — negative claims require coverage

Claims such as `cannot accelerate` or `no override exists` cannot be supported by checking a selected repository without bounding omitted routes/powers. A check path needs a declared selection/coverage basis.

### F6 — correction-window verification has its own clock and route

An independent check that completes after hardening, requires a selector-controlled credential, is unavailable, destroys a one-shot brake, or cannot route its result back in time does not do the work v0.4 assigns it.

```text
EVENTUALLY_CHECKABLE != CHECKABLE_BEFORE_USE
```

### F7 — `load-bearing` is an uninstalled trigger

The selector can evade the metadata by declaring a claim non-load-bearing or omitting it. Interaction effects also let two individually weak claims jointly determine the result. Define load-bearing by counterfactual dependence on the downstream result/qualifier where executable, otherwise mark aperture-discipline dependence.

### F8 — selector / declarer / beneficiary / evidence-controller are not one role

The `selector/declarer` compression can misclassify third-party declarers, first-person reporters, organisational coalitions and beneficiaries who control evidence without being either named role.

### F9 — target linkage remains aperture-relative

A supported `q,l1 -> g` linkage does not establish that all affected scopes were represented or reached. The target-set aperture discipline from the spine must travel.

```text
TARGET_LINK_FOR_l != TARGET_LINK_FOR_COMPLETE_AFFECTED_SCOPE
```

### F10 — active-object / front-door drift

The v0.4 attack object depends on `retain v0.3` rather than carrying the full retained output/control discipline; its compact profile names a check route but not the concrete falsifier. Separately, PR #38 and COM #46 front doors still orient a cold reader to earlier state. These are documentary/coordination drift, not a core TRACE collapse.

## What resisted

- no baseline/canon/authority/permission/clearance drift;
- v0.3 -> v0.4 is one additive file; no predecessor rewrite;
- the v0.2.7 donor and v0.3 spine target remain untouched;
- first-person, sole-witness and one-instrument evidence are not coerced to false merely because independent checking is absent;
- target causal linkage remains distinct from moral adequacy, restoration, authorization and priority;
- controlled/social deadlines are not automatically invalid;
- unknown control/check state is not coerced to independence;
- multiple apertures are explicitly not treated as independent evidence by identity alone;
- no new primitive is required by the surviving repair.

## Drift audit

At the audit boundary:

```text
PR #38 head                 09cb55f55cc6ccd5eede85b47cd80c32592b771b
v0.4 blob                   9f8c2637276a862a31045cfffa35e02f6b548ef7
v0.3 -> v0.4                ahead_by=1; one added file; 297 additions; 0 deletions
released donor mutation     NONE in PR #38
spine v0.2 mutation by v0.4 NONE
semantic promotion          NONE
```

Drift found:

1. PR #38 description does not name the current v0.4 correction-window attack object/head.
2. COM #46 issue body still advertises the original v0.1 candidate as the exact candidate; later comments carry the actual current state.
3. v0.4 is not standalone: a bounded reader of only v0.4 must follow `retain v0.3` to recover the full control/output semantics.
4. the compact check-path profile does not carry an explicit `FALSIFIER / TEST / EXPECTED COUNTEREVIDENCE` field even though the prose's sufficient condition depends on falsifiability.

## Probe ledger

### IDENTITY / DRIFT

| ID | Result | Hostile probe |
|---|---|---|
| P001 | RESISTED | PR #38 head equals expected v0.4 commit `09cb55f...` |
| P002 | RESISTED | v0.4 blob at branch head equals `9f8c263...` |
| P003 | RESISTED | v0.3 -> v0.4 commit delta is exactly one additive file |
| P004 | RESISTED | TRACE v0.2.7 donor object is not modified by PR #38 |
| P005 | RESISTED | spine v0.2 is not overwritten by v0.4 candidate |
| P006 | RESISTED | v0.4 withholds baseline/canon/validation/authority/permission/clearance |
| P007 | RESISTED | v0.4 names v0.3 as superseded only for attack |
| P008 | RESISTED | source-attack lineage includes CC/63 |
| P009 | FINDING | PR #38 front-door description does not mention current correction-window v0.4 head |
| P010 | FINDING | COM #46 issue body still advertises the original v0.1 candidate as exact candidate |

### ROLES

| ID | Result | Hostile probe |
|---|---|---|
| P011 | RESISTED | same actor is selector and declarer; dependence remains visible |
| P012 | FINDING | declarer is external but selector/beneficiary controls claim context; slash `selector/declarer` can misclassify |
| P013 | FINDING | separate declarer, selector and evidence custodian inside one organisation share one dependency root |
| P014 | RESISTED | genuinely external regulator with public independently held record remains representable |
| P015 | RESISTED | affected person gives first-person evidence and is not coerced to false because no external witness exists |
| P016 | RESISTED | multiple apertures reading one source are explicitly not treated as independent evidence |
| P017 | FINDING | beneficiary controls verifier while neither selector nor declarer does; rule does not name beneficiary control |
| P018 | FINDING | selector and ally jointly control check route; `not controlled solely` passes despite effective capture |
| P019 | FINDING | external declarer relies on selector-produced evidence; route identity does not expose production dependence |
| P020 | RESISTED | ordinary TRACE objects can represent separate actors/custody/routes without new primitive |

### EXTERNAL-CHECK INDEPENDENCE

| ID | Result | Hostile probe |
|---|---|---|
| P021 | RESISTED | immutable public record held outside interested party provides a real external check route |
| P022 | FINDING | selector-controlled public API is externally queryable; route externality can be mistaken for evidence independence |
| P023 | FINDING | nominally external verifier has aligned incentive/capture without formal route control; no dependency-root test |
| P024 | RESISTED | two nominally separate model apertures sharing one source are not auto-upgraded |
| P025 | FINDING | two organisations copy the same upstream record; multiple checkers do not create independent evidence |
| P026 | FINDING | independent escrow co-controls route but selector has unilateral veto; `not solely controlled` is too weak |
| P027 | RESISTED | append-only externally witnessed ledger can support stronger provenance |
| P028 | FINDING | cryptographic source authenticity does not by itself establish the external-world proposition |
| P029 | RESISTED | second physical sensor with a different failure root can strengthen the check path |
| P030 | FINDING | external checker merely republishes declarer's assertion; external route exists but no new evidential root |

### CHECKABILITY / VERIFICATION / PROPOSITION

| ID | Result | Hostile probe |
|---|---|---|
| P031 | FINDING | external check route exists but nobody runs it; checkability alone is not verification |
| P032 | RESISTED | independent check executes against exact proposition and corroborates it |
| P033 | FINDING | checker confirms current deadline but not load-bearing claim that deadline cannot accelerate |
| P034 | FINDING | checker validates hash/signature while load-bearing proposition concerns physical reality |
| P035 | FINDING | public rule text is checkable but private discretionary interpretation is actual load-bearing proposition |
| P036 | FINDING | negative claim `no override exists` is checked only against an incomplete repository |
| P037 | RESISTED | external checker finds contrary evidence; DISPUTED remains representable without clearance |
| P038 | FINDING | compact profile names a check route but not exact falsifier/test or expected counterevidence |
| P039 | RESISTED | external reviewer supplies only another unsupported opinion; candidate need not upgrade claim |
| P040 | BOUNDED | a once-checked dynamic claim later becomes stale; ordinary TRACE freshness can represent this |

### TIMING / REACHABILITY

| ID | Result | Hostile probe |
|---|---|---|
| P041 | RESISTED | external check completes and reaches receiver before correction decision |
| P042 | FINDING | external check exists but completes after target hardening |
| P043 | FINDING | check route is days long while correction window is hours |
| P044 | FINDING | verifier is external but access requires selector-issued credential that can be withheld |
| P045 | FINDING | checker exists but is currently unavailable; route existence is not current reachability |
| P046 | FINDING | falsification test consumes a one-shot brake or otherwise destroys correction capacity |
| P047 | RESISTED | cheap read-only verifier with current access survives the attack |
| P048 | BOUNDED | stale route-status evidence is already bounded by TRACE freshness discipline |
| P049 | FINDING | checker can inspect evidence but cannot lawfully/technically route result back before use |
| P050 | RESISTED | check runs, survives, and result reaches decision aperture before hardening |

### LOAD-BEARING TRIGGER

| ID | Result | Hostile probe |
|---|---|---|
| P051 | RESISTED | a claim whose value changes robust-fit result is plainly load-bearing |
| P052 | FINDING | selector labels a consequential claim `not load-bearing` and evades metadata |
| P053 | FINDING | selector omits a consequential control claim entirely, so trigger never sees it |
| P054 | RESISTED | changing target linkage changes downstream window claim; candidate can expose it |
| P055 | FINDING | claim changes only qualifier/control-sensitivity rather than boolean fit; load-bearing boundary underspecified |
| P056 | RESISTED | counterfactual dependency can in principle be executable by recomputing result with claim varied/removed |
| P057 | FINDING | prose-only load-bearing assessment by same aperture repeats CC/47 trigger failure |
| P058 | BOUNDED | claim influences later action but not correction-window output; outside candidate sufficiency scope |
| P059 | FINDING | two individually non-decisive claims jointly determine fit; per-claim test can miss interaction |
| P060 | BOUNDED | metadata cost can exceed ambiguity reduction; v0.4 explicitly marks this as hostile limit |

### TARGET / SCOPE / RESIDUE

| ID | Result | Hostile probe |
|---|---|---|
| P061 | RESISTED | target `g` has explicit causal link to threatened `q` for affected scope `l` |
| P062 | RESISTED | predeclared but causally trivial target is refused as load-bearing repair target |
| P063 | RESISTED | record correction distinguished from restoration of lost intended state; residue preserved |
| P064 | FINDING | target repairs selected scope `l1` while omitted `l2` remains affected; singular linkage can be overgeneralised |
| P065 | FINDING | public correction exists but affected scope's actual access path cannot reach it; public surface != effective repair |
| P066 | RESISTED | partial correction can be valuable without being labeled restoration |
| P067 | RESISTED | target selected after clock but required by pre-existing contract can still be represented |
| P068 | RESISTED | target selected before clock yet causally trivial still fails linkage |
| P069 | RESISTED | second aperture can dispute causal linkage without supplying moral priority rule |
| P070 | RESISTED | sole-custody evidence for target linkage remains explicit rather than coerced to false |

### SOLE-CUSTODY / UNKNOWN

| ID | Result | Hostile probe |
|---|---|---|
| P071 | RESISTED | patient pain report with no external measure remains reportable |
| P072 | RESISTED | sole witness event remains reportable |
| P073 | RESISTED | one physical instrument remains usable with independence not established |
| P074 | RESISTED | organisation reports undocumented internal discretionary power; dependence travels |
| P075 | RESISTED | later independent corroboration can upgrade evidence without rewriting history |
| P076 | RESISTED | conflicting first-person and instrument evidence can remain disputed |
| P077 | RESISTED | no external check does not imply false |
| P078 | RESISTED | no external check does not imply clearance |
| P079 | FINDING | label `selector-dependent` can be wrong when declarer/custodian is not selector; role conflation leaks into output |
| P080 | RESISTED | forced action clock does not require manufacturing certainty or ignorance |

### AUTHORITY / VALUE / CLAIM CEILING

| ID | Result | Hostile probe |
|---|---|---|
| P081 | RESISTED | external check path does not establish authorization |
| P082 | RESISTED | robust timing does not establish moral adequacy |
| P083 | RESISTED | causal target linkage does not establish priority |
| P084 | RESISTED | control visibility does not establish legitimacy |
| P085 | RESISTED | correction-window fit does not establish execution |
| P086 | RESISTED | correctability does not establish harmlessness |
| P087 | RESISTED | verifier existence does not establish clearance |
| P088 | RESISTED | first-person evidence does not auto-assign moral standing or priority |
| P089 | RESISTED | affected-scope inclusion does not auto-rank scopes |
| P090 | RESISTED | controlled/social deadline is not automatically invalid |

### INTEGRATION / PARTIAL INGESTION

| ID | Result | Hostile probe |
|---|---|---|
| P091 | FINDING | active v0.4 says `retain v0.3` but omits substantial retained output/control detail; partial reader can lose repair content |
| P092 | FINDING | compact check-path representation omits explicit falsifier/test despite prose requiring falsifiability |
| P093 | BOUNDED | compact profile omits validity/freshness but ordinary TRACE claim envelope already provides it |
| P094 | FINDING | title `terminating rule` overclaims: external checker can inherit same selector/evidence dependence recursively |
| P095 | RESISTED | current PR head exactly equals v0.4 target commit at audit boundary; no hidden branch drift observed |
| P096 | RESISTED | all PR #38 changes are additive; released donor object is not replaced |
| P097 | RESISTED | v0.4 does not mint controller/check-route/target-link primitives |
| P098 | RESISTED | v0.4 is not yet integrated into spine; promotion remains withheld |
| P099 | RESISTED | live #46 ASK attacks shared-source/captured-verifier pseudo-independence directly |
| P100 | RESISTED | no external return after ASK is not treated as validation or absence of counterexample |

## Smallest justified repair direction

Do not add a new independence primitive. Replace the broken compression with a claim ceiling:

```text
SELECTOR_DEPENDENCE_EXPOSED != SELECTOR_PROBLEM_REPAIRED
CHECK_PATH_EXISTS != CHECK_EXECUTED
CHECKER_SEPARATE != EVIDENCE_DEPENDENCY_SEPARATE
CHECKED_EVIDENCE != CHECKED_LOAD_BEARING_PROPOSITION
CHECKABLE_EVENTUALLY != CHECKABLE_BEFORE_USE
TARGET_LINK_FOR_l != COMPLETE_AFFECTED_SCOPE
```

A stronger result may rely on an external check only when the exact load-bearing proposition has a declared falsifier/check route whose relevant evidence/control dependencies are exposed, whose coverage is adequate to that proposition, and whose result is reachable within the time for which the downstream claim is being used. Otherwise preserve the claim and make the unresolved dependency explicit; do not call the selector problem repaired.

## Claim boundary

```text
100 PROBES != VALIDATION
EXTERNAL CHECKABILITY != TRUTH
EXPLICIT DEPENDENCE != REPAIRED DEPENDENCE
FINDING != NEW PRIMITIVE
DRIFT FOUND != DONOR CORRUPTED
NARROW != BASELINE FAILURE
```
