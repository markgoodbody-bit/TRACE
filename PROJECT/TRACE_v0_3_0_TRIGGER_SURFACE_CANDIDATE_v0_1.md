# TRACE v0.3.0 — TRIGGER-SURFACE CANDIDATE v0.1

Status: WORKING OPERATOR CANDIDATE — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — NO NEW PRIMITIVE CLAIM

## Problem

A distinction can exist in the grammar and still fail at the moment it matters.

```text
DISTINCTION_PRESENT != DISTINCTION_APPLIED
SOURCE_ANCHORED != PROPOSITION_SUPPORTED
HISTORICALLY_SUPPORTED != CURRENTLY_SUPPORTED
```

A status legend nobody applies, a claim-status algebra nothing invokes, or a clock/record distinction a reader walks past does not reliably change the reading.

The repair should not be `populate every TRACE field` and should not create a universal MATERIALITY or TRIGGER primitive.

## Candidate rule: load-bearing distinction

Let `q` be a downstream claim, comparison, selection input, or proposed transition whose support depends on a reading.

Let `D` be a distinction already representable by TRACE.

[SCHEMATIC_MODEL]

Treat `D` as load-bearing for `q` when collapsing `D` could make two represented states appear equivalent even though they support materially different statuses for `q`.

Informally:

```text
IF collapsing distinction D could change whether q is supported,
current, scoped, reachable, independent, authorised, complete,
or otherwise valid under the declared comparison,
THEN D must fire before q is used.
```

This is an inspection rule, not a universal estimator. A receiver may be unable to determine whether a distinction is load-bearing. Where the unresolved distinction itself could change the claim, preserve that uncertainty rather than silently collapsing it.

```text
LOAD_BEARING_UNKNOWN != NOT_LOAD_BEARING
```

## Minimum conditional surface

When a downstream claim materially relies on a **capability** claim, expose enough to distinguish:

```text
source / assertion
world evidence or derivation route
observation time / freshness
current applicability
cannot_access / cannot_verify / cannot_act where relevant
```

When it relies on **authority / grant**, distinguish:

```text
existence
source
scope
target / action class
time / current applicability
revocation or supersession where represented
```

When it relies on a **clock / hardening / irreversibility** claim, type what the clock actually times and its evidence. Do not promote urgency or a deadline into irreversibility merely because the downstream decision is urgent.

When it relies on a **route / brake / correction path**, distinguish where material:

```text
listed
reachable
usable
independent
within authority
actuated
witnessed
completed before hardening
```

When it relies on **coverage / target-set completeness**, expose target-set source, selection basis, known omissions, alternative target-set apertures, and the comparison basis.

When it relies on a **record as current world state**, test freshness / world correspondence rather than provenance alone.

When it relies on **burden, future-space, control, benefit or structural comparison**, expose the designation, measure, dependency roots, affected scopes and unresolved alternatives required by the comparison.

## Decayed versus never-supported

Two false current claims can have very different histories.

### Previously supported, now decayed

A claim may have had adequate evidence for a declared earlier time/scope and later lose current applicability because of:

```text
world change
evidence expiry
changed aperture
changed target set
changed capability / authority / control
changed scope or boundary
superseding evidence
```

Possible repair: re-observation, re-derivation, or explicit narrowing to the historical claim.

### Never adequately supported

A claim may be perfectly anchored to an immutable source which proves only that an assertion, configuration, plan, policy, or report existed. The source may never have established the world proposition later attributed to it.

```text
IMMUTABLE_ASSERTION != WORLD_VALID_PROPOSITION
CONFIGURED != OPERATIONAL
DECLARED_CAPABILITY != OBSERVED_CAPABILITY
```

Re-deriving from the same source cannot create the missing evidence. Repair requires a different evidential route or a narrower proposition.

## Observer-to-world transfer

A faulty observer path can create real downstream state.

Example:

```text
source object intact
-> observer decodes incorrectly
-> observer believes source is damaged
-> corrective act publishes observer artifact
-> artifact is now world state
```

TRACE already has the required structure:

```text
OBSERVED_RENDERING != SOURCE_OBJECT
TRACE_OUTPUT != MAP_UPDATE
MAP_UPDATE / OBSERVATION_ERROR can condition ACTION
ACTION can change WORLD
```

No new primitive is proposed for this case.

## Falsification targets

Break this candidate with cases where:

1. the relevant distinction is not triggered even though collapse changes the downstream claim;
2. the trigger fires on almost everything and recreates full-packet bureaucracy;
3. a reader can game `load-bearing` to suppress an inconvenient distinction;
4. historical support and current support cannot be separated;
5. a perfectly anchored but never-supported claim is mistaken for decay;
6. the rule silently imports a value or priority selector;
7. the rule requires unavailable evidence and therefore converts `UNKNOWN` into an automatic stop;
8. the trigger surface becomes more cognitively expensive than the errors it prevents.

## Retain / reject rule

RETAIN only if this conditional surface makes existing TRACE distinctions fire in hostile cases without requiring every field in every reading.

DEMOTE if the same effect can be obtained by a smaller operator/checker rule.

REJECT if it becomes a disguised universal checklist, materiality oracle, compliance gate, or value selector.
