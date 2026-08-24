# TRACE v0.3.0 — SPINE CANDIDATE v0.5 TARGETED DONOR-LOSS PASS

**Status:** TWO MATERIAL DONOR-LOSS FINDINGS / TWO NON-PROMOTIONS  
**Target:** `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_5.md`  
**Donor ledger:** `PROJECT/TRACE_v0_2_7_TO_v0_3_0_DONOR_MAP_v0_1.md`

Purpose: do not compare v0.5 against the donor by bulk. Probe donor capabilities whose loss can still license a materially stronger or wrong downstream conclusion in the compressed spine.

---

## 1. ACCESS / CUSTODY STATE — MATERIAL DONOR LOSS

v0.5 claim/evidence text asks for an `aperture/access boundary`, but it does not explicitly preserve the donor separation between evidence state and access/custody state.

### Counterexample A — inaccessible to this receiver becomes universally unknown

A clinician directly observes result `X` and records it. A downstream model receives a report that the record exists but does not have permission or technical access to inspect the clinical record itself.

World/evidence state:

```text
X was OBSERVED by clinician
record exists
receiver cannot access record
```

Collapsed reading:

```text
receiver cannot inspect X
-> X = UNKNOWN / no evidence exists
```

That destroys a material distinction. The correct bounded representation can preserve both that evidence exists and that this receiver cannot inspect it.

```text
UNAVAILABLE_TO_THIS_READER != UNIVERSALLY_UNKNOWN
EVIDENCE_EXISTS != EVIDENCE_ACCESSIBLE_TO_THIS_RECEIVER
```

### Counterexample B — access becomes disclosure authority

A receiver is technically able to read a protected record. A downstream action publishes it because `available` is treated as sufficient for disclosure.

```text
AVAILABLE != AUTHORISED_TO_DISCLOSE
ACCESS_CAPABILITY != DISCLOSURE_AUTHORITY
```

The handshake blocks requests for protected/inaccessible internal state, but it does not carry this general evidence/access/custody distinction for ordinary external records.

### Disposition

**REPAIR IN SPINE, NARROWLY.**

Do not restore the full donor access/custody algebra. Add the separation and decisive ceilings near claim/evidence use:

```text
EVIDENCE_STATE != ACCESS_CUSTODY_STATE
UNAVAILABLE_TO_THIS_READER != UNIVERSALLY_UNKNOWN
AVAILABLE != AUTHORISED_TO_DISCLOSE
```

The generic §6.0 trigger then makes the distinction fire when access/custody is load-bearing.

No new primitive is earned.

---

## 2. FUTURE-PATH CORRESPONDENCE — MATERIAL DONOR LOSS

v0.5 preserves represented future-space but no longer states how a path represented at two times is shown to be the same continuation.

### Counterexample

At `t0`:

```text
path_id = APPEAL
meaning = appeal can pause eviction before possession
status = reachable
```

At `t1` after the possession event:

```text
path_id = APPEAL
meaning = retrospective appeal can correct record / compensation only
status = reachable
```

A longitudinal summary compares identifiers and concludes:

```text
APPEAL existed at t0
APPEAL exists at t1
-> protected path was preserved
```

The label persisted; the reachable continuation did not.

```text
SAME_PATH_LABEL != SAME_TRAJECTORY
PATH_IDENTIFIER_PERSISTS != PATH_EFFECT_PERSISTS
TECHNICALLY_REACHABLE_SUCCESSOR != COMPARABLE_CONTINUATION
```

This matters directly to TRACE's future-space / hardening claim. Without correspondence discipline, nominal path persistence can hide foreclosure.

### Disposition

**REPAIR IN SPINE, NARROWLY.**

Do not add a trajectory-matching primitive or universal path metric. Add one rule in future-space:

When a downstream comparison claims that a future path was preserved, lost, opened or closed across states/times, path correspondence must be supported at the resolution relevant to that claim; label/identifier persistence is insufficient.

Unknown correspondence remains `UNKNOWN`.

---

## 3. CLOCK AUTHORSHIP — NO NEW REPAIR EARNED IN THIS PASS

Donor map marks clock authorship as partial. v0.5 no longer carries the older explicit sentence that a deadline may be physical, contractual, political, manufactured or mixed.

Attack case: an actor creates a 24-hour internal deadline and presents it as an irreversible boundary.

v0.5 already requires:

```text
URGENCY != IRREVERSIBILITY
```

and, for strong correction-window claims, §9.2 requires explicit target-boundary condition plus selector/source/basis and material disputes/alternatives. §8 separately preserves control scope/time.

The constructed false boundary is therefore already challengeable without restoring a separate clock-authorship paragraph.

**NO ADDITION EARNED by this pass.**

Retain as cold-transfer/donor-loss target: if unfamiliar receivers fail to reconstruct authorship from source/basis + control, reconsider.

---

## 4. CONCRETE COMPRESSED-INPUT SEED — NO SEMANTIC REPAIR EARNED YET

The donor map says the concrete compressed -> differentiated demonstration is KEEP or must be shown unnecessary. v0.5 currently has no worked front-door seed.

This may be a reception/reconstruction cost rather than a semantic licensing defect. PR #41 already explores a cold-entry/profile surface.

No constructed case here shows that omission of the example licenses a false world claim that the spine otherwise permits.

**DO NOT RE-EXPAND CORE YET.**

Let the bounded cold-transfer pass test whether an unfamiliar reader can reconstruct the object without a worked seed. If not, restore the smallest worked example or attach the cold-entry profile rather than assuming all donor front-door prose belongs in core.

---

## 5. Other donor capabilities sampled

Current v0.5 already carries in compressed form:

```text
primitive-set aperture / self-application
absence / stream / pattern
nested-boundary refinement warning
refusability / exit / override
parallel correction process
interval-safe timing
explicit target boundary
value/designation/measure boundary
mechanistic-interpretability interface
validator/world ceiling
```

Full controlled vocabulary, serialization, packet schema, operator/checker implementation, worked transfers, recursive merge detail and invariant-by-invariant coverage remain full-candidate obligations under the build ceiling. Their omission from this spine is not silently recoded as deletion.

---

## 6. Current result

```text
MATERIAL DONOR LOSS 1: EVIDENCE_STATE != ACCESS_CUSTODY_STATE
MATERIAL DONOR LOSS 2: PATH LABEL != TRAJECTORY CORRESPONDENCE
CLOCK AUTHORSHIP:     NO NEW SPINE TEXT EARNED YET
WORKED SEED:          DEFER TO COLD-TRANSFER / PROFILE TEST
NEW PRIMITIVE:        NO
NEW ROOT:             NO
```

Next candidate should add only the two material repairs, then re-run the cheap compression and worked counterexamples before any broader donor restoration.
