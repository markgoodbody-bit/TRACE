# TRACE v0.3.0 — SPINE v0.8 I11 / I48 REPAIR DELTA v0.1

**Status:** WORKING REPAIR DELTA — NOT INTEGRATED SPINE — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED  
**Parent:** spine v0.8  
**Failure witness:** `falsification/TRACE_v0_3_0_INVARIANT_SEMANTIC_DISPOSITION_V01_HOSTILE_ATTACK.md`

---

## 1. I11 — route existence does not establish usability

Restore:

```text
ROUTE_EXISTS != ROUTE_USABLE
```

A downstream proposition that a route is **usable for correction** is scope/target relative. Where load-bearing, its support may depend on:

```text
practical access
ability to reach/alter the stated target effect
capability and authority
relevant timing/window
material burden, danger or retaliation exposure
material execution constraints
```

This is a firing rule, not a universal usability checklist. Do not demand every field when the distinction cannot change the downstream claim.

```text
ROUTE_LISTED != ROUTE_EXECUTABLE
ROUTE_EXECUTABLE != ROUTE_USABLE
BURDEN_PRESENT != ROUTE_UNUSABLE
COURAGE_REQUIRED != ROUTE_USABLE   # retained full-candidate regression guard
```

TRACE does not define one universal usability threshold. A domain, policy, value layer or declared comparison may supply the threshold/basis; TRACE exposes it when the usability conclusion depends on it.

If no such basis is available and the unresolved condition could change usability, preserve uncertainty.

---

## 2. I48 — advantage claim requires an exposed measure

Restore in compressed form:

```text
ADVANTAGE_CLAIM_REQUIRES_DECLARED_MEASURE
```

An `advantage` comparison is not free-standing. Expose the comparison basis/measure that makes one scope/state/path advantaged relative to another.

The measure may be:

```text
numeric
ordinal
qualitative
relational
partial / multi-dimensional
```

No scalar is required.

Example:

```text
A can override queue outcome; B cannot.
measure = control over queue outcome
-> A may be advantaged over B under that measure
```

Without a declared measure/basis, preserve the underlying supported control asymmetry but do not upgrade it to an unqualified advantage claim.

```text
STRUCTURAL_DIFFERENCE != ADVANTAGE_WITHOUT_MEASURE
ADVANTAGE_UNDER_MEASURE != MORAL_ENTITLEMENT
DIFFERENT_MEASURE != SAME_ADVANTAGE_ORDERING
```

---

## 3. Immediate attack set

### Route usability

1. route exists and is technically executable but public use creates material retaliation risk;
2. route executes but cannot alter the claimed target effect;
3. route has non-zero burden but remains usable under a declared domain threshold;
4. route usability is unknown because safe access evidence is unavailable;
5. route is usable but not authorised for this actor;
6. route is authorised and usable but cannot complete before target boundary;
7. route is usable for one scope and unusable for another.

### Advantage / measure

8. control asymmetry with no declared comparison measure;
9. same facts with a declared qualitative control measure;
10. two supported measures rank the same pair in opposite directions;
11. a measured advantage is treated as moral entitlement;
12. a structural difference that is not designated as an advantage comparison.

One false `usable`, false unqualified advantage, or hidden moral upgrade is enough to hold the delta.

---

## 4. Disposition

```text
NEW PRIMITIVE: NO
NEW NODE/RELATION: NO
I11: DONOR GUARD RESTORED
I48: DONOR MEASURE BINDING RESTORED
USABILITY SCALAR: NONE
ADVANTAGE SCALAR: NONE REQUIRED
THIS DELTA: ATTACK OBJECT
```
