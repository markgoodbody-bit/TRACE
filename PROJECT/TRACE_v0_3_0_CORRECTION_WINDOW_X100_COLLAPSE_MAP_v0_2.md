# TRACE v0.3.0 — correction-window x100 collapse map v0.2

**Status:** WORKING FINDING-COLLAPSE MAP — NOT A REPAIR CANDIDATE — NOT SPINE TEXT — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE  
**Supersedes for current attack:** `PROJECT/TRACE_v0_3_0_CORRECTION_WINDOW_X100_COLLAPSE_MAP_v0_1.md`  
**Evidence basis:** correction-window v0.4 x100/drift audit; COM #46 ROOT B attack; CC/74 and later A-vs-C attack; live field specimens in COM #46 including Square #1834/#1832, CC/136/137, and Square #1845  
**Purpose:** reduce the x100 finding classes to the smallest distinct failure surfaces before any later correction-window repair candidate is written.

---

# 0. Current result

v0.1 proposed four semantic roots plus carrier/orientation drift:

```text
A  epistemic state upgrade
B  independence mechanism
C  verification as routed/timed/bounded causal process
D  trigger / role / scope propagation
E  carrier / orientation drift
```

After direct attacks on B and A, the current working map is:

```text
A  -> DISTINCT EPISTEMIC-TRANSITION / WARRANT ROOT
      implementation may be derived; no new primitive earned

B  -> DERIVED CLAIM/USE-SCOPED DEPENDENCY DIAGNOSTIC

C  -> DISTINCT VERIFICATION-PROCESS ROOT

D  -> UNRESOLVED BUNDLED CANDIDATE ROOT

E  -> SEPARATE CARRIER / ORIENTATION ROOT
```

Two distinctions are essential:

```text
ROOT != PRIMITIVE
DERIVED_STATUS != NON_ROOT
```

A failure surface can be reconstructed from existing graph/history without requiring a new canonical type and still remain distinct from C.

This is a compression result, not validation. No v0.5 is earned.

---

# 1. ROOT A ATTACK — A DOES NOT COLLAPSE INTO C

v0.1 grouped:

```text
DEPENDENCE_EXPOSED
CHECK_PATH_EXISTS
CHECK_EXECUTED
CLAIM_SURVIVED_CHECK
```

The attack asked whether these are merely lifecycle states of verification process C.

That collapse fails.

## 1.1 Counterexample: false upgrade when no verification exists

Hold C fixed at:

```text
NO CHECKER
NO CHECK PATH
NO VERIFICATION PROCESS
NO CHECK EVENT
```

Now let a representation expose or publish a claim and then label it as checked/validated anyway:

```text
EXPOSED -> CHECKED
```

Nothing about C is inadequate. C does not exist.

Yet the transition is invalid.

```text
NO_VERIFICATION_PROCESS
+
STATUS_UPGRADED_TO_CHECKED
=
EPISTEMIC_TRANSITION_FAILURE
```

This is the CC/74 break and it survives the present attack.

Therefore:

```text
ROOT_A != ROOT_C
```

## 1.2 Counterexample: legitimate exposure transition without verification

Inspection of ordinary provenance may reveal that a selector authored or controlled the only evidence:

```text
DEPENDENCE_UNSEEN -> DEPENDENCE_EXPOSED
```

No falsifier need run and the proposition need not become more verified.

This shows that C can cause some epistemic transitions but does not define the whole transition algebra.

## 1.3 What A actually is

A is not a new world object. It is the distinct failure surface governing whether a claimed epistemic transition is warranted by the represented history.

For proposition `q`, scope/use `U`, and time `t`, a derived status view may include:

```text
exposure_status
checkability_status
execution_status
outcome_status
coverage_basis
observation/completion time
freshness
remaining unknowns
```

Those statuses should be reconstructed from ordinary claims, provenance, apertures, routes and event history where possible.

But reconstruction does not make the transition rule disappear.

The repair obligation is:

```text
DO_NOT_EMIT_A_STRONGER_STATUS_THAN_THE_REPRESENTED_HISTORY_WARRANTS
```

Useful guards:

```text
EXPOSED != CHECKABLE
CHECKABLE != CHECKED
CHECKED != SURVIVED
SURVIVED != TRUE
PAST_SURVIVAL != CURRENT_SURVIVAL
CHECK_FAILED_TO_FALSIFY != CLAIM_PROVEN
```

So the current disposition is:

```text
ROOT A SURVIVES
A is a status/transition-warrant root, not a new primitive
```

---

# 2. HOW A AND C INTERLOCK WITHOUT COLLAPSING

C supplies much of the history from which A statuses are derived.

```text
CHECK_PATH_EXISTS
    <- C route + proposition + instrument/coverage + access + timing

CHECK_EXECUTED
    <- C execution/activation event

CLAIM_SURVIVED_CHECK
    <- completed C event/outcome for exact proposition under declared limits/time
```

But A constrains the inference from those facts to epistemic status.

```text
C = what verification process existed / happened
A = what status transition that history licenses
```

Neither substitutes for the other.

A clean process with a falsely upgraded label is an A failure.
A correctly conservative label attached to an inadequate process remains a C failure.

```text
PROCESS_CORRECT != STATUS_LABEL_CORRECT
STATUS_LABEL_CONSERVATIVE != PROCESS_ADEQUATE
```

---

# 3. FIELD SPECIMENS

These are field contact, not validation.

## 3.1 True inputs, invalid join — Square #1834

```text
TRUE_INPUTS != VALID_JOIN
CHECKED_INPUTS != SURVIVED_DERIVED_PROPOSITION
```

This strengthens both roots:
- C must bind verification to the exact proposition;
- A must not transfer the checked/survived status of premises to a derived join without warrant.

## 3.2 Missingness mechanism — Square #1832

```text
BOUNDED_READ != ONE_MISSINGNESS_MECHANISM
SAME_COVERAGE_FRACTION != SAME_SELECTION_BIAS
```

This primarily strengthens C's coverage representation.

## 3.3 Complete rows, open measurement window — CC/136/137

```text
FULL_ROW_COVERAGE != CLOSED_MEASUREMENT_WINDOW
PARTIAL_BUCKET != DAILY_RATE
CHECKED_AT_t != SURVIVED_FOR_CLOSED_INTERVAL
```

C must carry the proposition's temporal aggregation/closure condition.
A must refuse the stronger `SURVIVED_FOR_CLOSED_INTERVAL` status until that condition is met.

Existing CLOCK/history structure may be sufficient; no new primitive is earned.

## 3.4 A predeclared falsifier fires — Square #1845

A prior claim can move state after a falsifier is actually exercised and counterevidence is observed.

```text
FALSIFIER_DECLARED != FALSIFIER_RUN
FALSIFIER_RUN + COUNTEREVIDENCE_OBSERVED -> STATUS_CHANGE
CURRENTLY_REFUTED != NEVER_PREVIOUSLY_ASSERTED
HISTORY_UPDATE != HISTORY_ERASURE
```

Again:
- C records the test and its conditions;
- A governs the licensed state transition.

---

# 4. ROOT B — STANDING DERIVED-DIAGNOSTIC RESULT

Party count and organisational separation are weak proxies for evidential independence.

Preserve:

```text
SEPARATE_PARTY != INDEPENDENT_EVIDENCE
PREFERENCE_BLIND_CHECK != INDEPENDENT_EVIDENCE_SOURCE
PRECOMMITTED != EXTERNALLY_SOURCED
DIFFERENT_OBSERVATION_TIME != DIFFERENT_CONTROL_ROOT
NO_KNOWN_DEPENDENCY_PATH != INDEPENDENT
NO_OBSERVED_DEPENDENCY != INDEPENDENCE_ESTABLISHED
```

Existing TRACE structure can represent operators, carriers, instruments and shared dependency/control roots with ordinary nodes plus `DEPENDS_ON`, `CONTROLS`, provenance and claim structure.

Current disposition:

```text
ROOT_B -> DERIVED CLAIM/USE-SCOPED DEPENDENCY DIAGNOSTIC
```

A diagnostic should be able to return at least:

```text
DEPENDENCY_OBSERVED
DEPENDENCY_NOT_OBSERVED
INDEPENDENCE_NOT_ESTABLISHED
```

Question form:

```text
independent of what dependency,
for which proposition q,
for which use U,
over which causal path,
and from what time?
```

No separate universal `independence` primitive is earned.

---

# 5. ROOT C — DISTINCT VERIFICATION-PROCESS ROOT

C survives and is strengthened.

A verification capable of doing load-bearing work needs, as applicable:

```text
exact proposition q
evidence source and provenance
selection / coverage mechanism
instrument capability / resolution / limits
access and authority boundary
start time
measurement window and closure condition
completion time
freshness
return route to the using aperture
cost / side effect / consumed capacity
actor/control/dependency structure
event history and outcome
remaining unknowns
```

Useful non-entailments:

```text
CHECKED_EVIDENCE != CHECKED_LOAD_BEARING_PROPOSITION
NO_COUNTEREXAMPLE_IN_SELECTED_SET != NO_COUNTEREXAMPLE
EVENTUALLY_CHECKABLE != CHECKABLE_BEFORE_USE
CHECK_COMPLETED != CHECK_RESULT_REACHED_USE
CHECK_AVAILABLE != CHECK_AFFORDABLE_WITHOUT_MATERIAL_SIDE_EFFECT
FULL_ROW_COVERAGE != CLOSED_MEASUREMENT_WINDOW
```

No new `PROCESS` primitive is earned by this result.

---

# 6. ROOT D — NEXT ATTACK OBJECT

D remains unresolved:

```text
trigger / role / scope propagation
```

but may be a category bundle.

Current suspicion:

```text
F7 load-bearing trigger
   -> cross-cutting ACTIVATION / firing problem

F8 role conflation
   -> mostly dependency/control/provenance structure

F9 affected-scope aperture
   -> mostly C + existing target-set/aperture discipline, unless a counterexample survives
```

The next attack should test mechanism separation rather than improve the wording.

Two known hazards already constrain any simple trigger:

```text
DISTINCTION_PRESENT != DISTINCTION_APPLIED
TRIGGER_PRESENT != TRIGGER_FIRED
```

and adaptive/path-dependent systems can preserve the same endpoint while changing the causal route:

```text
SAME_ENDPOINT != SAME_CAUSAL_DEPENDENCE
COMPENSATED_COUNTERFACTUAL != NON_LOAD_BEARING
```

So a one-output perturbation test is not enough.

---

# 7. CURRENT COLLAPSED MAP

```text
F1 exposure is not repair --------------------+
F2 checkable is not checked ------------------+--> ROOT A: epistemic transition / warrant

F3 route independence != evidence independence ----> derived dependency diagnostic B

F4 exact proposition -------------------------+
F5 negative coverage -------------------------+
F6 verification clock / return route ---------+--> ROOT C: verification process
TEMPORAL window closure ----------------------+ 

F7 load-bearing trigger ----------------------+
F8 role conflation ---------------------------+--> CANDIDATE D, under attack
F9 target-scope aperture ---------------------+

F10 partial ingestion / front doors -----------> ROOT E: carrier / orientation
```

Current compression count:

```text
2 distinct semantic failure surfaces: A, C
1 derived dependency diagnostic: B
1 unresolved bundled candidate root: D
1 separate carrier/orientation root: E
```

This count is provisional.

---

# 8. CONSEQUENCE FOR ANY LATER REPAIR

Do not add an A primitive merely because A survives as a root.

A later candidate should derive compact status views from canonical graph/process history where possible and make unsupported upgrades fail visibly.

```text
ROOT != PRIMITIVE
DERIVED_STATUS != NEW_EVIDENCE
STATUS_VIEW_WITHOUT_RECONSTRUCTION_ROUTE -> HOLD
```

Minimum guards:

```text
SURVIVED_CHECK != TRUE
CHECKABLE != CHECKED
EXPOSED != CHECKABLE
PAST_SURVIVAL != CURRENT_SURVIVAL
TRUE_INPUTS != VALID_JOIN
FULL_ROW_COVERAGE != CLOSED_MEASUREMENT_WINDOW
```

No v0.5 is earned by this attack.

---

# 9. NEXT FALSIFIERS — ATTACK D

1. Can F7 be represented as generic activation/firing structure without a correction-window-specific semantic root?
2. Give a role distinction that changes no dependency, control, authority, burden, evidence, scope or inference. If nothing changes, delete it.
3. Give a role distinction that changes a downstream claim but cannot be represented with existing dependency/control/provenance structure.
4. Give an affected-scope case where target-set aperture plus access/route structure is insufficient.
5. Break any simple counterfactual load-bearing trigger with compensated adaptation or path dependence.
6. Give a case where A and C are both correct, trigger fires correctly, role structure is correct and scope coverage is correct, yet the correction-window conclusion fails for a mechanism not already represented.

One counterexample is enough to stop further collapse.
