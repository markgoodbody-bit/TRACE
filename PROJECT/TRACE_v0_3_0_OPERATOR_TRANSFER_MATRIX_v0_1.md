# TRACE v0.3.0 — OPERATOR TRANSFER MATRIX v0.1

**Status:** HOSTILE TRANSFER OBJECT — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE  
**Target:** `TRACE_v0_3_0_OPERATOR_INTERFACES_CANDIDATE_v0_1.md`  
**Purpose:** try to falsify the I/X/C decomposition by asking whether it locates a demonstrated failure closely enough to imply a different repair. If two labels merely rename the same repair, collapse them.

---

## 0. Test rule

Current candidate distinguishes:

```text
I  INGRESS / CONSTITUTION
   relevant material or its relation does not enter standing representation in the needed form

X  ACTIVATION
   the needed distinction is represented but remains dormant at a downstream use

C  CHECK / ACTUATION
   the distinction fires but the executable evidential/corrective process is absent, inadequate,
   too late, wrongly dependent, under-resolved, or fails to return to use
```

The labels earn their place only if they change what repair should be attempted.

```text
DIFFERENT_LABEL != DIFFERENT_FAILURE
DIFFERENT_FAILURE != DIFFERENT_REPAIR_UNLESS_ROUTE_CHANGES
```

The transfer cases below deliberately reuse existing TRACE machinery. No case may earn a new primitive merely by fitting a column.

---

# 1. MEDICINE — HANDOVER FRAMING

## M-I — supplied relation collapses at ingress

Handover says:

```text
Patient 14 is anxious, medically stable, frequent caller.
```

Assume every statement was supportable when written. The current clinician receives it as undifferentiated standing context: prior-team report, current observation and current assessment are not practically distinguished.

**First visible failure:** I.

Existing TRACE carriers:

```text
CLAIM / EVIDENCE
REPORTED / OBSERVED / INFERRED
PROVENANCE
RETAINED HISTORY
MAP
SOURCE / ROUTE
```

**Repair implied by classification:** preserve the ingress relation and current-assessment status. Do not require rejection or re-derivation of the handover.

**Why X alone is insufficient:** there may be no later represented distinction to activate if the report/current-assessment relation disappeared during map formation.

## M-X — distinction present, not used

The handover is explicitly marked `previous-team working interpretation; not independently reassessed`. Twenty minutes later a new symptom is reported, but the downstream assessment continues to treat `medically stable` as current without firing the historical/current distinction.

**First visible failure:** X.

**Repair:** activate freshness/source-status distinctions on the dependency path feeding the current assessment. The representation itself need not be rebuilt.

## M-C — distinction fires, check cannot discriminate

The clinician notices the inherited/current distinction and requests a current test, but the chosen test or observation is incapable of discriminating the relevant alternative at the needed resolution.

**First visible failure:** C.

**Repair:** change the evidential route/instrument, not the handover representation or activation rule.

**Transfer verdict:** the three locations imply different repairs in this domain. I/X/C survives this case provisionally.

---

# 2. LAW — DISCOVERY AND EVIDENTIARY RECORD

## L-I — selected record omits a consequential class

A discovery export is internally faithful but excludes a class of messages because the collection query did not target an alias used by one custodian. The resulting record contains no marker that this class was outside the target aperture.

**First visible failure:** I.

Existing TRACE carriers:

```text
APERTURE
TARGET-SET source / selection basis
BOUNDS / OMITS / DISPUTES
CLAIM / EVIDENCE
```

**Repair:** expose/perturb the target-set aperture; reacquire through a changed selection route where warranted.

## L-X — limitation represented, completeness claim ignores it

The record states that the alias was not searched, but a later argument relies on `the produced record contains no contrary message` as if it established `no contrary message exists`.

**First visible failure:** X.

**Repair:** fire the negative-coverage distinction at the downstream completeness claim.

## L-C — completeness challenge uses the same blind query

The limitation fires and a verification is ordered, but the verifier reruns the same collection matcher against the same target definition.

**First visible failure:** C.

**Repair:** alter matcher/coverage/evidence dependency; a second process is not an independent check if it shares the failing selection mechanism.

**Transfer verdict:** I/X/C again changes repair without adding a legal primitive.

---

# 3. SCIENCE — LITERATURE SELECTION AND NULL RESULT

## S-I — publication/search aperture narrows the represented evidence base

A review faithfully summarizes every study in its selected corpus, but the search strategy systematically misses a relevant terminology family.

**First visible failure:** I.

**Repair:** perturb the literature target aperture / terminology selector. More careful inference over the same corpus cannot recover the omitted studies.

## S-X — corpus limitation present, conclusion suppresses it

The search limitation is documented, but the downstream statement `the literature shows no effect` is used without activating corpus-coverage and negative-claim distinctions.

**First visible failure:** X.

**Repair:** narrow/qualify the downstream claim or activate the omitted-coverage fork.

## S-C — null test is under-resolved

The coverage distinction fires and the exact experiment is checked, but the test has insufficient resolution to distinguish the effect size relevant to the claim.

**First visible failure:** C.

**Repair:** expose instrument/test resolution; `TEST_RAN != RELEVANT_ALTERNATIVE_DETECTABLE`.

**Transfer verdict:** strong support for keeping C separate from representation/activation.

---

# 4. ORGANISATION — KPI / BOARD REPORT

## O-I — dashboard target set filters a failure class

A reliability dashboard counts only outages longer than five minutes. Short repeated outages disappear from the represented incident set even though they materially affect a customer population.

**First visible failure:** I if the threshold/omission relation is absent from the standing report.

**Repair:** expose target-set source, threshold and omitted class; compare through an alternate aperture if the downstream use depends on total interruption burden.

## O-X — threshold visible, headline ignores it

The report clearly states `outages >5 min`, but the headline `reliability improved` is consumed as a general reliability claim.

**First visible failure:** X.

**Repair:** fire scope/measure/target distinctions at the headline's downstream use.

## O-C — audit reproduces the dashboard, not the world proposition

An independent team reproduces the dashboard perfectly from the supplied logs but never tests whether the logs themselves contain the short-outage class or whether the threshold matches the operative claim.

**First visible failure:** C.

**Repair:** bind verification to the load-bearing proposition and evidence root, not merely the artifact computation.

**Transfer verdict:** `REPRODUCED_ARTIFACT != VERIFIED_WORLD_PROPOSITION` remains a C-class repair once the representation and activation issues are already visible.

---

# 5. EDUCATION — TRUE CURRICULUM, SELECTIVE WORLD

A curriculum contains no false statements about a historical event but selects only material from one institutional perspective.

## E-I — selection relation absent

Students receive the material without any representation of the selection basis or known omitted perspectives.

**First visible failure:** I.

**Repair:** preserve that the supplied corpus is selected/bounded and provide source routes where the declared educational use requires comparison. TRACE does not choose the morally preferred curriculum.

## E-X — selection relation present, later claim ignores it

The curriculum explicitly identifies its source boundary, but a later assessment treats mastery of that corpus as mastery of the complete historical dispute.

**First visible failure:** X.

**Repair:** activate scope/coverage at the later claim.

## E-C — alternate-source exercise is nominal only

A checking exercise supplies several `different` sources that all reproduce one upstream institutional summary.

**First visible failure:** C.

**Repair:** expose evidence dependency rather than count nominal sources.

**Transfer verdict:** the operator can remain structural if it exposes selection and dependency without selecting which historical interpretation should win.

---

# 6. ARCHIVE — OBSERVER ERROR HARDENS INTO RECORD

## A-I — rendering is mistaken for source object

An intact UTF-8 source is decoded through a legacy code page; the mangled rendering is stored without preserving that it is an observer-path artifact.

**First visible failure:** I.

**Repair:** preserve source-object / observed-rendering relation; reacquire source through a different path.

## A-X — relation present, correction ignores it

The archive record preserves both raw bytes and a warning that the display may be decoding-corrupted, but an archivist still treats the rendering as the source and publishes a correction.

**First visible failure:** X.

**Repair:** activate `OBSERVED_RENDERING != SOURCE_OBJECT` before the corrective act.

## A-C — comparison check uses the same decoder

The distinction fires and a second read is requested, but both reads use the same broken decoding path.

**First visible failure:** C.

**Repair:** alter the observation/instrument path; nominal repetition is not an independent check.

**Transfer verdict:** this is the cleanest recurrence case because a C failure can create new world state which becomes fresh I for the next reader.

---

# 7. IMPORTANT BREAK: I/X/C ARE NOT A ONE-WAY PIPELINE

The archive case breaks a naive sequential interpretation.

A failed C operation may publish a new artifact. That artifact becomes supplied world material for another receiver. The next failure is again I or X.

Likewise:

```text
CHECK RESULT -> NEW RECORD -> NEW INGRESS
ACTION -> WORLD CHANGE -> NEW APERTURE -> NEW MAP
CORRECTION -> RESIDUE -> LATER DOWNSTREAM USE
```

Therefore the operator interfaces must not be represented as an irreversible phase progression.

```text
I_THEN_X_THEN_C != UNIVERSAL_EXECUTION_ORDER
FAILURE_AT_C_CAN_CREATE_NEW_I
INTERFACE_LOCATION != UNIQUE_CAUSE
FIRST_VISIBLE_FAILURE != ONLY_FAILURE
```

They are **diagnostic interfaces in a recursive causal loop**.

This is a material self-correction to the rhetoric of `INGRESS -> ACTIVATION -> CHECK/ACTUATION` if that arrow is read as a one-way architecture rather than a local inspection order.

---

# 8. SECOND BREAK: `INGRESS` CURRENTLY HIDES TWO DIFFERENT REPAIRS

The matrix also exposes a compression inside I:

```text
R  representation-route failure
   relevant material/relation is omitted, retyped, target-filtered or corrupted before receipt

J  receiver-integration failure
   supplied material arrives with adequate relations but is incorporated into standing map in a way that erases them
```

Examples:

```text
L-I missing alias search     -> R failure
A-I mojibaked observation    -> R failure
M-I handover relation erased -> J failure (if relation existed in supplied object)
```

These repairs differ:

```text
R -> change/reacquire representation route
J -> change/preserve integration relation
```

**But no new primitive is earned.** The spine already has both sides:

```text
Pi / APERTURE / target-set / source-object path
J_receiver / MAP / RETAINED HISTORY / claim-evidence relation
```

Current disposition:

- keep `I` only as a coarse operator family if it helps orientation;
- do not let `INGRESS` hide whether the defect is upstream representation or receiver integration;
- if hostile review shows this distinction is routinely needed, derive `R/J` as sublocations from existing spine machinery rather than promote them to roots.

---

# 9. THIRD BREAK: FIRST FAILURE LOCATION IS APERTURE-RELATIVE

A downstream analyst may first observe an X failure even though an upstream R failure created the conditions for it. Another aperture with access to the source-selection process may locate R directly.

```text
OBSERVED_FAILURE_LOCATION != UNIQUE_CAUSAL_ORIGIN
DIAGNOSTIC_INTERFACE != BLAME_ASSIGNMENT
```

Therefore I/X/C must not be used as causal-responsibility labels without an actual dependency account.

This is especially important for organisations and institutions where the actor consuming a report differs from the actor who selected the report contents.

---

# 10. CURRENT RESULT

The transfer matrix does **not** falsify the usefulness of separating representation/integration, activation, and checking. Across six non-AI domains, the location changes the next repair.

But it narrows the candidate in three ways:

1. I/X/C are recursive diagnostic interfaces, not a universal one-way pipeline.
2. coarse `I` must expose whether the actionable defect lies in representation route (`R`) or receiver integration (`J`) when that difference changes repair.
3. observed interface location is aperture-relative and does not by itself assign causal responsibility.

No new semantic primitive is earned.

Preferred integrated shape remains derived:

```text
existing TRACE grammar
  + bounded interface diagnosis
  + repair route appropriate to the located failure
```

The next hostile question is now sharper:

> Can an ordinary TRACE reading derive R/J/X/C failure location and the corresponding repair route cheaply enough from existing APERTURE / MAP / CLAIM / EVIDENCE / ROUTE / HISTORY / TARGET-SET structure that even the named interface family becomes unnecessary?

If yes, delete I/X/C as named machinery and keep only the operator sentence.