# TRACE v0.2.6 transition regression contract

Status: **working candidate**

This contract applies to the transition package and to any later compiled `TRACE_FORMAL_SEED_v0_2_6.md` derived from it.

## Invariants

A compiled v0.2.6 candidate must preserve all of the following.

### R01 — no silent primitive growth

```text
new node types = none
new edge types = none
new ports = none
new required packet fields = none
```

The target-set-aperture rule uses existing representation objects.

### R02 — target-set source remains visible

A material search or coverage claim cannot be described as complete merely because its selected targets were reached.

Required semantic distinctions:

```text
TARGET_SET != WORLD_SCOPE
TARGET_NOT_SELECTED != TARGET_DOES_NOT_EXIST
COVERAGE_OF_SELECTED_TARGETS != COMPLETE_DISCOVERY
```

### R03 — transition accounting remains aperture-relative

A materially live class may be checked against supplied evidence, but neither schema validity nor a checker pass may imply world-complete transition discovery.

### R04 — information presence remains separate from coverage

A represented `INFORMATION` transition does not establish that the selected aperture widens beyond the current map or reaches a supplied target.

### R05 — target-set disagreement remains disagreement

Two target-set apertures may produce different results for the same packet. The formal seed must preserve both provenance chains and must not silently select an authoritative target set.

### R06 — divergence does not create authority

A structural result, checker pass, or repeated aperture result cannot become an authorised selection without a visible external handoff.

### R07 — handoff visibility does not establish legitimacy

Selector, owner, authority, policy and route references make the handoff inspectable. They do not establish lawful or morally justified authority.

### R08 — contest route does not establish correction

A represented route to a brake before a deadline does not establish route execution, brake activation, interruption, repair or harm prevention.

### R09 — commitment receipt remains non-clearance

A receipt records proceeding under unresolved conditions. It does not convert uncertainty into approval.

### R10 — minimum schema remains minimum

The embedded validator may check shape, required fields and controlled vocabulary. It must not claim semantic completeness, reference integrity, route executability, independence, legitimacy or world correspondence.

### R11 — checker-external rules remain external

Transition accounting, search-target contradiction, authority handoff and contestability depend on supplied comparison envelopes. They must not be silently embedded as truth-valued minimum-schema fields.

### R12 — stop condition remains active

The candidate must not automatically expand into brake-effectiveness, authority-legitimacy, policy-quality or world-completeness machinery without a concrete representational defect.

## Adversarial scenes

A later full-seed regression suite should include at least these cases.

### V26-A — narrow target set passes

An operator checks only already-known targets and reaches all of them.

Expected:

```text
selected-target coverage may be represented
world completeness remains UNKNOWN
```

### V26-B — independent target aperture adds omitted scope

A second aperture supplies a materially affected target omitted by the operator set.

Expected:

```text
divergent target-set results preserved
no automatic authority transfer
```

### V26-C — information transition without outward reach

An `INFORMATION` transition queries only the current map.

Expected:

```text
transition accounting may PASS
search coverage must not be inferred
```

### V26-D — schema-valid silent transition omission

Supplied evidence makes INFORMATION materially live, but no transition or supported status is recorded.

Expected:

```text
minimum schema may PASS
checker-external accounting FAIL
```

### V26-E — declared authority handoff

A selector, authority claim, policy basis and route are recorded after divergent readings.

Expected:

```text
handoff structurally visible
legitimacy remains unestablished
```

### V26-F — route reaches brake before deadline

A declared uncaptured route reaches a bound brake under the supplied clocks.

Expected:

```text
contestability declaration may PASS
actual interruption remains unestablished
```

### V26-G — brake activation without observable change

A brake command is recorded, but no transition change is observed.

Expected:

```text
activation attempt represented
correction completion not inferred
```

### V26-H — unresolved target-set authority

Two apertures disagree and no selector is authorised to choose.

Expected:

```text
UNRESOLVED preserved
no forced selection
```

## Versioning regression

Full compilation must choose and test one explicit strategy:

1. formal version `0.2.6` with separately declared unchanged packet schema `0.2.5`; or
2. synchronized `TRACE-GRAPH-0.2.6` identifier bump with unchanged schema shape.

The compiled seed must not leave formal and packet version semantics ambiguous.

## Failure conditions

The transition candidate fails review if it:

- adds a new primitive without a representational counterexample;
- turns a checker input into a TRACE truth claim;
- implies target-set completeness;
- grants authority to an aperture result;
- equates a route or brake declaration with correction;
- changes the minimum schema shape without a demonstrated shape defect;
- or claims validation, operational readiness, decision advantage or world validity.
