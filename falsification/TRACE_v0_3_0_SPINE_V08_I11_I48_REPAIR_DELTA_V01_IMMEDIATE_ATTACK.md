# TRACE v0.3.0 — SPINE v0.8 I11 / I48 REPAIR DELTA v0.1 IMMEDIATE ATTACK

**Target:** `PROJECT/TRACE_v0_3_0_SPINE_V08_I11_I48_REPAIR_DELTA_v0_1.md`  
**Verdict:** `CLEAR_WITH_RESIDUAL_LIMITS` — NOT VALIDATION  
**Scope:** twelve targeted route-usability / advantage-measure cases

---

# ROUTE USABILITY

## 1. Executable route with retaliation risk

The route endpoint works and authority can alter the target decision. Public use exposes the affected person to credible material retaliation.

The repair does not upgrade technical executability to usability. If the declared usability basis requires safe practical access, the route is not established usable; if the threshold/basis is itself unresolved, preserve `UNKNOWN`.

**RESISTS.**

## 2. Executable route cannot alter target effect

A complaint endpoint accepts and records the complaint but has no mechanism or authority to alter the challenged outcome.

Execution is real. Usability **for correction of the stated target** is not established.

```text
ROUTE_EXECUTED != TARGET_CORRECTABLE_BY_ROUTE
```

**RESISTS.**

## 3. Non-zero burden but route remains usable

A route costs ten minutes and one form; the declared domain usability basis permits that burden and there is no material exclusion for the affected scope.

The repair explicitly blocks:

```text
BURDEN_PRESENT -> ROUTE_UNUSABLE
```

Non-zero burden is preserved without laundering it into unusability.

**RESISTS.**

## 4. Safe access unknown

Technical route exists; evidence about retaliation/safe access is unavailable and could change the usability conclusion.

Result remains unresolved rather than `usable` or `unusable` by default.

**RESISTS.**

## 5. Usable mechanism, actor lacks authority

The route is practically usable by an authorised reviewer but the current actor lacks authority to invoke it.

For proposition `usable by this actor`, authority is load-bearing and blocks the claim. For proposition `a usable institutional route exists for an authorised reviewer`, actor-specific authority is not silently imported.

**RESISTS.**

## 6. Usable route, correction window already closed

The route remains accessible, safe and executable, but cannot complete before the relevant target boundary.

Do **not** globally relabel the route unusable merely because the correction window for this target/time is closed.

Correct separation:

```text
ROUTE_USABLE = supported under declared usability basis
WINDOW(route,target,time) = closed/unknown as evidence supports
```

Timing becomes part of the usability claim only where the proposition explicitly means “usable to correct this target before this boundary.”

```text
WINDOW_CLOSED != ROUTE_GLOBALLY_UNUSABLE
```

**RESISTS WITH QUALIFIER.**

## 7. Scope-relative usability

A route is usable for a represented organisation with counsel but inaccessible to an individual without that representation.

The repair binds usability to scope rather than globalising one status.

**RESISTS.**

---

# ADVANTAGE / MEASURE

## 8. Control asymmetry, no declared measure

A can override a queue decision; B cannot. No comparison basis is declared.

The control relation may be reported. An unqualified `A is advantaged` claim is not licensed.

**RESISTS.**

## 9. Qualitative measure

Same facts, with:

```text
measure = degree of control over queue outcome
```

A qualitative/relational comparison is sufficient. No numeric scalar is demanded.

**RESISTS.**

## 10. Opposite rankings under two measures

```text
measure M1 = control over queue outcome -> A advantaged
measure M2 = waiting-time burden       -> B advantaged
```

The repair preserves measure-indexed comparisons. It does not silently collapse them to one unqualified ordering.

```text
ADVANTAGED_UNDER_M1 != ADVANTAGED_UNDER_M2
```

**RESISTS.**

## 11. Measured advantage -> moral entitlement

A is advantaged under a declared control measure. A reader concludes A therefore deserves control.

The existing value ceiling plus the repair blocks the upgrade:

```text
ADVANTAGE_UNDER_MEASURE != MORAL_ENTITLEMENT
```

**RESISTS.**

## 12. Structural difference not used as advantage comparison

A and B differ in topology. No downstream proposition compares one as advantaged.

The measure trigger does not fire merely because a structural difference exists.

```text
STRUCTURAL_DIFFERENCE != AUTOMATIC_ADVANTAGE_QUERY
```

**RESISTS.**

---

## Residual limits

Not established:

1. universal usability criteria — deliberately absent;
2. correct domain thresholds for safety, affordability or practical access;
3. whether an unfamiliar receiver consistently distinguishes route usability from correction-window status;
4. whether all advantage language is detected when hidden in domain synonyms;
5. correctness or legitimacy of a supplied measure;
6. cross-measure aggregation — deliberately not supplied by TRACE.

---

## Disposition

```text
MATERIAL FINDING IN TARGETED ATTACK: NONE
I11 REPAIR: SURVIVES WITH ROUTE/WINDOW QUALIFIER
I48 REPAIR: SURVIVES
NEW ONTOLOGY: NONE
NEXT: MINIMAL v0.9 INTEGRATION -> BUILD/CHECK -> RE-RUN INVARIANT MAP
```

`CLEAR_WITH_RESIDUAL_LIMITS != VALIDATED`.
