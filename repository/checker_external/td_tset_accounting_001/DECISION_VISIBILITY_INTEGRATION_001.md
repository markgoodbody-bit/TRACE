# TRACE decision-visibility integration 001

Status: **bounded integration note**

TRACE change: **none**

Minimum-schema change: **none**

Checker change: **none**

Version change: **none**

## Purpose

This note integrates the transition-accounting, search-coverage, aperture-differential, authority-handoff and authority-contestability sequence into one bounded result.

It is not another checker. It does not promote any working candidate into canon or validation. Its purpose is to state what the sequence has established, what remains outside the instrument, and where expansion should stop unless a new real-work defect appears.

## Frozen basis

This integration reads the following existing artifacts together:

- `TRACE-GRAPH-0.2.5` and its embedded minimum validator;
- `TD-TSET-ACCOUNTING-001`;
- schema-valid applied witnesses K–N;
- `TD-TSET-SEARCH-COVERAGE-001`;
- target-set aperture differential Z1/Z2;
- `TD-AUTHORITY-HANDOFF-001`;
- `TD-AUTHORITY-CONTESTABILITY-001`.

No result below is stronger than those artifacts and their declared epistemic ceilings.

## Integrated chain

```text
supplied scene evidence
→ transition-class accounting
→ represented INFORMATION transition
→ declared search target and reachability path
→ target-set aperture comparison
→ divergent aperture results
→ explicit selector / authority / policy handoff
→ challenge route to a bound brake
→ contest clock comparison before commitment
```

Each arrow preserves a boundary. No later stage retroactively proves the earlier stage complete or true.

## What the sequence establishes

### 1. Supplied evidence can be silently omitted from a structurally valid packet

The embedded minimum schema checks packet shape and controlled vocabulary. It does not enforce semantic completeness.

A checker-external comparison can detect when supplied evidence makes a transition class materially live but the packet neither represents it nor records a supported unavailable, unresolved or not-assessable status.

```text
schema-valid
!=
transition-set complete relative to supplied evidence
```

### 2. Representing an information transition does not establish meaningful outward search

The schema-valid ritual-search witness represents an `INFORMATION` transition while restricting the selected aperture to categories already present in the working map.

Transition accounting accepts that packet because the transition exists and is internally represented.

```text
INFORMATION transition represented
!=
search capable of exposing the omitted target
```

### 3. Search coverage is assessable only against a supplied target and comparison basis

When a discovery target, selected aperture and declared path are supplied, the search-coverage checker can detect:

- an explicit target/aperture contradiction;
- a missing or non-contiguous declared reachability path;
- unresolved target, claim or path references;
- a weak comparison envelope whose support is absent or internally unbound.

It cannot establish that the target set is complete or that the declared path works in the world.

### 4. Target selection is itself an aperture

The target-set differential freezes one schema-valid TRACE packet and changes only the external target comparison:

```text
operator target set: hog population
→ PASS / declared reachability chain

external-record target set: field team
→ FAIL / explicit aperture contradiction
```

The checker has not changed its interpretation of one target. It has received a different target set.

```text
search-coverage result
is conditional on
supplied target-set aperture
```

### 5. Divergence does not create authority

Conflicting aperture results can remain unresolved without structural failure.

When a later process selects a result or transition, the handoff can be checked for an explicit:

- selector and selector owner;
- authority claim;
- policy or value basis;
- route from results to selector;
- selected transition;
- brake and brake authority where represented;
- commitment receipt when commitment proceeds under unresolved conflict.

This exposes silent authority inheritance. It does not establish legitimate authority or good policy.

### 6. Visible authority does not establish contestable authority

A declared selector, policy and brake can coexist with no usable route for a conflicting aperture to alter the trajectory.

The contestability candidate can check whether the packet represents:

- a challenging aperture result;
- a route from that result to a bound brake;
- external contest authority;
- explicit capture status;
- route and deadline clocks;
- strict arrival before the declared contest boundary.

```text
route_seconds < contest_deadline_seconds
```

Equality is not before.

The result remains a declaration about represented topology and clocks. It is not proof that the route or brake works.

## What the sequence does not establish

The integrated chain does not establish:

- complete discovery of affected entities or scopes;
- complete or correct target selection;
- truth of packet claims;
- good faith;
- genuine aperture independence;
- actual route executability;
- legitimate authority;
- correct policy or value selection;
- brake independence, connection or effectiveness;
- interruption of the selected transition;
- prevention or repair of harm;
- decision advantage in live operation;
- world validity.

These are not small omissions hidden by successful tests. They are the declared boundary of the instrument.

## Layer boundary

| Layer | What it may establish | What it must not claim |
|---|---|---|
| TRACE representation | objects, claims, routes, clocks, apertures, transitions, authority and correction structure are representable | truth, permission, legitimacy or successful actuation |
| Minimum schema | required packet shape and controlled vocabulary are present | semantic completeness or correspondence with the world |
| Checker-external accounting | supplied evidence is accounted for or explicitly bounded | unseen evidence or world completeness |
| Search-coverage comparison | a supplied target is supported, unsupported or contradicted by a declared aperture/path | complete target selection or actual reachability |
| Authority handoff | selection and commitment basis are visible | legitimate authority or good policy |
| Contestability comparison | a declared challenge route reaches a declared brake before a declared deadline | actual interruption or effective correction |
| Selector / policy / value layer | chooses among represented options under declared authority | attribution of its choice to TRACE |
| Actuation and world observation | records what was attempted and what observably changed | retroactive conversion of an attempt into success |

## Current integrated claim

The strongest supported compression is:

> TRACE and its checker-external candidates can keep supplied affected scopes, uncertainty, materially live alternatives, conflicting apertures, authority handoff and a declared contest route visible through a consequential decision. They cannot by themselves discover every affected scope, choose the governing values, legitimate authority, or prove that correction occurred.

That is enough to give the structure practical teeth without turning it into a hidden selector or moral sovereign.

## Stop condition

Do not continue automatically into an expanding sequence of brake-effectiveness, brake-independence, policy-quality or authority-legitimacy checkers merely because those distinctions can be named.

Reopen checker construction only when one of the following occurs:

1. a real or independently supplied scene passes the current chain while producing a concrete false-complete result inside a boundary the existing candidates claim to check;
2. an existing candidate cannot express a required comparison using its declared inputs without silently strengthening its authority;
3. repeated applied use shows a material false-positive, false-negative or ritual-compliance pattern not already preserved by the current epistemic ceilings;
4. implementation requires a machine-testable assertion whose evidence and failure semantics can be stated without pretending to know the unseen world.

Absent one of those triggers, the next work belongs to application, interpretation or human-facing translation rather than another checker.

## Reader path

A compact review path is:

1. `APPLIED_SCENE_001.md` — schema-valid transition accounting and ritual search;
2. `SEARCH_COVERAGE_001.md` — target-relative contradiction checking;
3. `COVERAGE_APERTURE_DIFFERENTIAL_001.md` — target selection as aperture;
4. `AUTHORITY_HANDOFF_001.md` — visible selection and commitment basis;
5. `AUTHORITY_CONTESTABILITY_001.md` — declared route to correction before commitment;
6. this note — integrated boundary and stop condition.

## Final boundary

```text
what the structure can expose
what supplied evidence can falsify
what authority must openly decide
what remains genuinely unknown
```

Keeping those four regions separate is the result.
