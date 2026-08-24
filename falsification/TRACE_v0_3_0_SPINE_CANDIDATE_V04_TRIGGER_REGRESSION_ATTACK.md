# TRACE v0.3.0 — SPINE CANDIDATE v0.4 TRIGGER-REGRESSION ATTACK

**Status:** MATERIAL FINDING — HOLD v0.4 AS WRITTEN  
**Target:** `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_4.md`  
**Prior quarry:** `PROJECT/TRACE_v0_3_0_TRIGGER_SURFACE_CANDIDATE_v0_1.md` and CC/47 on COM #46

---

## 1. Failure

Compression retained many distinctions but dropped the generic firing rule that makes a load-bearing proposition pass through the relevant evidence/warrant surface regardless of how it is syntactically presented.

v0.4 says:

```text
A load-bearing claim should expose enough ... to bound its use.
```

But a load-bearing proposition may enter a downstream conclusion as configuration, metadata, a route attribute, status field, policy row, cached value, derived score, or ordinary prose rather than as an explicit `CLAIM` object.

The distinction can therefore remain present in the grammar and still fail to fire.

```text
DISTINCTION_PRESENT != DISTINCTION_APPLIED
CONFIGURATION_FIELD != WARRANT_FREE_FACT
REPRESENTATION_TYPE != EVIDENCE_STATUS
```

---

## 2. Worked counterexample

Input contains a correction-route object:

```text
route_A:
  endpoint = reviewer@example
  external = true
  independent = true
  reachable = true
```

The `independent = true` field is copied from configuration maintained by the same controller whose decision the route is meant to challenge. No separate dependency evidence is supplied.

A downstream comparison uses `route_A` to support:

```text
INDEPENDENT_CORRECTION_ROUTE_PRESENT
```

and therefore prefers a design on the ground that correction is independently reachable.

v0.4 contains relevant distinctions elsewhere:

```text
EXTERNAL != INDEPENDENT
SEPARATE_PARTY != INDEPENDENT_EVIDENCE
ROUTE_LISTED != ROUTE_EXECUTABLE
```

But if `independent = true` is treated as configuration rather than as a proposition requiring support, those distinctions need never fire at the use point.

The receiver can therefore preserve the vocabulary while still licensing the stronger downstream conclusion.

This is the same structural failure shape previously identified by CC/47: a capability row can look like configuration and bypass claim typing.

---

## 3. Smallest repair direction

Do **not** restore the full trigger-surface candidate or create a MATERIALITY/TRIGGER primitive.

Add one representation-independent firing rule near claim/evidence use:

```text
If a downstream claim, comparison, selection input, route, window status,
or proposed transition materially depends on proposition p,
then p must inherit the relevant TRACE evidence/currentness/scope/warrant discipline
regardless of whether p arrived as a CLAIM, field, label, configuration, status,
metadata, cached value, derived output, or prose assertion.
```

Where it is unresolved whether collapsing the distinction could change the downstream conclusion, preserve that uncertainty rather than treating the distinction as non-load-bearing.

```text
LOAD_BEARING_UNKNOWN != NOT_LOAD_BEARING
```

This is a firing rule over existing structure, not new ontology.

---

## 4. Bureaucracy ceiling

The rule must not mean “convert every field into a full claim packet.”

It fires only when the proposition is actually carrying a downstream conclusion whose support could change if the relevant distinction were applied.

```text
FIELD_PRESENT != FIELD_LOAD_BEARING
LOAD_BEARING_TRIGGER != FULL_PACKET_REQUIREMENT
```

A harmless display label with no downstream use does not need evidence machinery merely because it exists.

---

## 5. Classification

```text
COMPRESSION REGRESSION
DONOR / PRIOR-QUARRY RECOVERY
NEW PRIMITIVE: NO
NEW ROOT: NO
```

The repair is smaller than the prior trigger-surface candidate and should be tested for whether it actually changes the worked case without recreating checklist bureaucracy.

---

## 6. Disposition

```text
SPINE_CANDIDATE_v0_4: HELD AS WRITTEN
NEXT: v0.5 NARROW TRIGGER REPAIR
```

Do not erase v0.4. It remains useful evidence that a shorter object can preserve vocabulary while silently dropping activation.
