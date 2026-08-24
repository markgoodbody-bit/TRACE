# TRACE v0.3.0 — SPINE CANDIDATE v0.5 TRIGGER IMMEDIATE ATTACK

**Status:** CLEAR ON TARGETED TRIGGER CASES / RESIDUAL LIMITS REMAIN  
**Target:** `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_5.md`  
**Purpose:** test whether the narrow representation-independent firing rule repairs v0.4 without recreating universal packet bureaucracy

---

## 1. Prior falsifier: configuration masquerades as fact

Input:

```text
route_A:
  external = true
  independent = true
```

`independent = true` is copied from controller-owned configuration. No independent dependency evidence is supplied. A downstream selection prefers `route_A` because it is treated as an independent correction path.

v0.5 §6.0 fires because the downstream selection materially depends on proposition `independent(route_A)`, regardless of its representation as configuration.

Relevant TRACE discipline can therefore apply:

```text
EXTERNAL != INDEPENDENT
SEPARATE_PARTY != INDEPENDENT_EVIDENCE
```

The configuration value cannot remain warrant-free solely because it was not serialized as a `CLAIM` object.

**RESISTS prior falsifier.**

---

## 2. Harmless display field — bureaucracy attack

Input:

```text
gui_theme = dark
```

No downstream claim, comparison, selection, route, window status or transition depends on the theme.

§6.0 does not fire merely because the field exists.

```text
FIELD_PRESENT != FIELD_LOAD_BEARING
LOAD_BEARING_TRIGGER != FULL_PACKET_REQUIREMENT
```

**RESISTS simple bureaucracy attack.**

---

## 3. Cached derived score used for action

Input:

```text
risk_score = 0.82
source_model_version = v1
```

The score is cached. The live model has moved to v2. A downstream selector uses `risk_score > 0.8` to block an action.

The proposition carried by the cached score is load-bearing regardless of its representation as a numeric field. §6.0 invokes relevant evidence/currentness discipline; §5 then blocks age-only or date-only currentness if a load-bearing derivation dependency changed.

```text
DATE_CURRENT != DERIVED_VALUE_CURRENT
CURRENT_AT_USE != VALID_THROUGH_DEPENDENT_INTERVAL
```

**RESISTS.**

---

## 4. Missing field becomes an implicit default

Input schema omits `independent`. Receiver code treats missing `independent` as `true` and uses the route as independently corrective.

The load-bearing proposition did not arrive as an explicit field at all; it was produced by a defaulting rule. §6.0 is stated in terms of the downstream proposition rather than the source representation, so the evidence/warrant trigger still applies.

Section 13 also blocks treating non-observation as world absence/presence.

**RESISTS if receiver follows proposition-level wording.**

Residual transfer target: test whether an unfamiliar receiver actually reconstructs that defaults/implicit propositions are covered or reads the enumerated representation examples too literally.

---

## 5. Materiality gaming

Attack: receiver declares an inconvenient distinction non-load-bearing so it does not fire.

v0.5 adds:

```text
LOAD_BEARING_UNKNOWN != NOT_LOAD_BEARING
```

and requires uncertainty to be preserved when it is unresolved whether collapsing the distinction could change the downstream conclusion.

This does not solve adversarial dishonesty or guarantee correct materiality judgement. It prevents the grammar from licensing `not load-bearing` merely from unresolved self-assessment.

```text
TRIGGER_RULE != MATERIALITY_ORACLE
```

No further core rule is earned by this constructed case.

---

## 6. Residual limits

The trigger remains a use-relative inspection rule, not a mechanical estimator. A receiver can still fail to notice a causal dependency; TRACE cannot guarantee cognition by stating a rule.

A later operator/checker may help make firing more reliable, but that does not imply another semantic primitive.

```text
RULE_PRESENT != RULE_EXECUTED
TRIGGER_SPECIFIED != TRIGGER_RELIABLY_FIRED
```

This distinction is important: v0.5 repairs the **licensing gap** in the spine. It does not prove behavioural compliance by a receiver.

---

## 7. Disposition

```text
SPINE_CANDIDATE_v0_5: RESISTS TARGETED IMMEDIATE TRIGGER ATTACK
VERDICT: CLEAR_WITH_RESIDUAL_LIMITS
NEW PRIMITIVE: NO
NEW ROOT: NO
NEXT: ONE BOUNDED COLD/TRANSFER ATTACK
```

Do not treat this as validation or merge/release evidence.
