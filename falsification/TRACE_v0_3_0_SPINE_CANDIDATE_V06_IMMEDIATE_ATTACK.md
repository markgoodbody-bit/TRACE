# TRACE v0.3.0 — SPINE CANDIDATE v0.6 IMMEDIATE ATTACK

**Status:** CLEAR ON TARGETED REPAIR CASES / RESIDUAL TRANSFER TARGETS REMAIN  
**Target:** `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_6.md`  
**Purpose:** test whether the two v0.6 donor-loss repairs change the worked downstream conclusions without creating unnecessary firing/bureaucracy

---

## 1. Evidence exists but receiver cannot inspect it

Case:

```text
clinician directly observes proposition X
clinical record preserves X
receiver receives a report that the record exists
receiver cannot access the protected record
```

Bad collapse:

```text
receiver cannot inspect X
-> no evidence exists / X universally UNKNOWN
```

v0.6 §6.0.1 requires evidence state and access/custody state to remain separate when load-bearing:

```text
EVIDENCE_STATE != ACCESS_CUSTODY_STATE
EVIDENCE_EXISTS != EVIDENCE_ACCESSIBLE_TO_THIS_RECEIVER
UNAVAILABLE_TO_THIS_READER != UNIVERSALLY_UNKNOWN
```

The scene can therefore preserve that X has an observed source/provenance route while this receiver cannot inspect the source.

**RESISTS.**

Residual transfer target: an unfamiliar receiver must keep `OBSERVED` bound to source/provenance/observation route rather than silently reading it as `OBSERVED_BY_ME`. v0.6's load-bearing claim rule already requires source/provenance and observation/derivation route. No extra observer primitive is earned by this constructed case.

```text
SOURCE_OBSERVED != RECEIVER_OBSERVED
```

---

## 2. Technical access becomes disclosure authority

Case:

```text
receiver can technically read protected record R
a downstream publish action depends on "R is available"
no disclosure grant / authority is supplied
```

Bad conclusion:

```text
AVAILABLE(R) -> MAY_DISCLOSE(R)
```

v0.6 blocks the promotion directly:

```text
AVAILABLE != AUTHORISED_TO_DISCLOSE
ACCESS_CAPABILITY != DISCLOSURE_AUTHORITY
CAPABILITY != AUTHORITY
```

The representation-independent §6.0 trigger fires because the publish action materially depends on the availability proposition. Technical access cannot become a disclosure grant merely by field type.

**RESISTS.**

TRACE still does not decide the external disclosure policy. It exposes that the authority claim is missing/unresolved.

---

## 3. Challenged actor controls the only evidence copy

Case:

Evidence is `AVAILABLE`, but the challenged actor can alter/delete the sole copy before review.

Attack: does v0.6 turn the new access/custody separation into an independence claim merely because custody is represented?

No. §6.0.1 says access/custody is a separate load-bearing axis but does not equate outside access, preservation, or custody with truth/independence. Existing ceilings remain:

```text
EXTERNAL != INDEPENDENT
IMMUTABLE_RECORD != CURRENT_WORLD
HASH_MATCH != ORIGINAL_RECORD_TRUE
```

The full donor custody algebra remains a build-ceiling obligation; the compressed spine does not claim it has mechanically solved custody.

**NO FALSE UPGRADE FOUND.**

---

## 4. Same path label, materially different continuation

At `t0`:

```text
path_id = APPEAL
reachable effect = can pause eviction before possession
```

At `t1` after possession:

```text
path_id = APPEAL
reachable effect = retrospective record correction / compensation only
```

Bad longitudinal conclusion:

```text
APPEAL at t0 == APPEAL at t1
-> protected path preserved
```

v0.6 §12 requires supported correspondence at the resolution relevant to a `preserved/lost/opened/closed` claim and explicitly blocks identifier persistence as proof:

```text
SAME_PATH_LABEL != SAME_TRAJECTORY
PATH_IDENTIFIER_PERSISTS != PATH_EFFECT_PERSISTS
TECHNICALLY_REACHABLE_SUCCESSOR != COMPARABLE_CONTINUATION
```

The pre-possession continuation cannot be claimed preserved solely from the label.

**RESISTS.**

---

## 5. Different label, materially corresponding continuation

At `t0`:

```text
path_id = APPEAL
reachable effect = independent reviewer can pause eviction before possession
```

At `t1` after administrative renaming:

```text
path_id = URGENT_REVIEW
reachable effect = same reviewer / same pause authority / same relevant timing and scope
```

Attack: does v0.6 falsely infer loss because the identifier changed?

No. The rule says correspondence **must be supported** and says label persistence is insufficient; it does not make label equality necessary. A supported correspondence relation can survive renaming.

```text
DIFFERENT_PATH_LABEL != DIFFERENT_TRAJECTORY
```

This guard is a useful consequence of the stated rule but is not yet added to the spine because the positive correspondence wording already carries it.

**RESISTS.**

---

## 6. Correspondence unresolved

At `t1`, the path retains the label `APPEAL`, but evidence is insufficient to determine whether it retains pause authority or only retrospective review.

v0.6 explicitly requires `UNKNOWN` rather than silently equating paths.

**RESISTS.**

```text
CORRESPONDENCE_UNRESOLVED != PATH_PRESERVED
CORRESPONDENCE_UNRESOLVED != PATH_LOST
```

---

## 7. Single-time future-space view — bureaucracy attack

A one-time reading maps three currently represented future paths. It makes no cross-time/state claim that any path was preserved, lost, opened or closed relative to another state.

The correspondence rule is conditional on that downstream comparison. It does not require a trajectory-correspondence audit merely to list current represented paths.

**RESISTS.**

```text
FUTURE_PATH_PRESENT != CROSS_TIME_CORRESPONDENCE_CLAIM
```

---

## 8. Compression gate

Repository object size:

```text
SPINE_v0_2 = 22,924 bytes
SPINE_v0_6 = 21,400 bytes
```

v0.6 remains smaller than the earlier v0.2 spine while carrying the two restored donor protections. Size alone is not proof of good compression; it only shows these repairs did not recreate the prior 31,714-byte accretion failure.

---

## 9. Residual limits / cold-transfer targets

This pass does not prove that an unfamiliar receiver will reliably reconstruct:

1. `OBSERVED` as source/aperture-relative rather than silently `observed by receiver`;
2. positive path correspondence across renames, splits or merges;
3. when path effect changes are material enough to break correspondence;
4. custody/deletion/alteration risk beyond the compressed access-state separation.

Those are transfer/full-candidate questions. No new primitive or additional spine paragraph is earned by this immediate pass.

```text
COMPRESSED_RULE_PRESENT != COLD_RECEIVER_RECONSTRUCTION_PROVEN
```

---

## 10. Disposition

```text
SPINE_CANDIDATE_v0_6: RESISTS TARGETED IMMEDIATE ATTACK
VERDICT: CLEAR_WITH_RESIDUAL_LIMITS
NEW PRIMITIVE: NO
NEW ROOT: NO
NEXT: ONE BOUNDED COLD/TRANSFER PASS + CONTINUED DONOR LEDGER, NOT SERIAL REVIEW
```

Do not treat this as validation, merge/release/canon evidence, or proof of donor equivalence.
