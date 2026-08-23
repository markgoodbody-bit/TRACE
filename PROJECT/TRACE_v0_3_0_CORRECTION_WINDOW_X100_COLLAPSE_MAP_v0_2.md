# TRACE v0.3.0 — correction-window x100 collapse map v0.2

**Status:** WORKING FINDING-COLLAPSE MAP — NOT A REPAIR CANDIDATE — NOT SPINE TEXT — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE  
**Supersedes for current attack:** `PROJECT/TRACE_v0_3_0_CORRECTION_WINDOW_X100_COLLAPSE_MAP_v0_1.md`  
**Evidence basis:** correction-window v0.4 x100/drift audit; prior ROOT B dependency attack in COM #46; live field specimens recorded in COM #46 including Square #1834/#1832, CC/136, and Square #1845  
**Purpose:** continue collapsing the x100 finding classes into the smallest distinct structural mechanisms before any later correction-window repair candidate is written.

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

After direct attacks on B and A, the current working map is smaller:

```text
A  -> DERIVED EPISTEMIC-STATUS VIEW
B  -> DERIVED CLAIM/USE-SCOPED DEPENDENCY DIAGNOSTIC
C  -> SEMANTIC ROOT: verification process
D  -> UNRESOLVED CANDIDATE ROOT: trigger / role / scope
E  -> SEPARATE CARRIER / ORIENTATION ROOT
```

This is a compression result, not validation. It does not establish that C or D are final roots, and it does not authorize a v0.5 repair.

---

# 1. ROOT A ATTACK — PURE COLLAPSE INTO C FAILS, BUT A DOES NOT SURVIVE AS A ROOT

v0.1 grouped:

```text
DEPENDENCE_EXPOSED
CHECK_PATH_EXISTS
CHECK_EXECUTED
CLAIM_SURVIVED_CHECK
```

and treated their non-equivalence as a distinct semantic root.

The hostile question was:

```text
Can A collapse into C?
```

The answer is narrower than either YES or NO.

## 1.1 Falsifier against the pure claim `A -> C`

Hold the verification process fixed at:

```text
NO VERIFICATION PROCESS PRESENT
```

Now compare two otherwise equivalent readings of the same claim `q`:

```text
R1: the material dependency/provenance relation is represented and available
R2: the same dependency/provenance relation is omitted from the reading
```

Then:

```text
C(R1) = C(R2) = NO VERIFICATION PROCESS
```

but:

```text
DEPENDENCE_EXPOSED(R1) != DEPENDENCE_EXPOSED(R2)
```

Therefore:

```text
ALL_OF_A_IS_JUST_C = FALSE
```

Expanding C until it includes every representation-state fact would make the collapse tautological and would destroy the useful distinction between a verification process and the graph it operates over.

## 1.2 Why this does not rescue A as a semantic root

The exposure difference is already representable with ordinary TRACE structure:

```text
CLAIM / source / provenance
DEPENDS_ON
CONTROLS
APERTURE
access state
OMITS / CANNOT_ACCESS / BOUNDS
```

So `DEPENDENCE_EXPOSED` need not be a new mechanism. It is a derived question over the represented graph and the using aperture:

```text
Is the material dependency/provenance relation represented and available
for this proposition, scope, use and time?
```

The remaining A states are naturally lifecycle states of verification process C.

Current decomposition:

```text
DEPENDENCE_EXPOSED
    := derived representation/provenance status

CHECK_PATH_EXISTS
    := derived from C route + proposition + instrument/coverage + access + timing

CHECK_EXECUTED
    := derived from an execution/activation event in C history

CLAIM_SURVIVED_CHECK
    := derived from a completed C event/outcome for the exact proposition
       under declared coverage, limits and time
```

So the result is:

```text
ROOT_A -> DERIVED_EPISTEMIC_STATUS_VIEW
```

not:

```text
ROOT_A -> ROOT_C
```

and not:

```text
ROOT_A remains an independent semantic mechanism
```

---

# 2. THE STATUS VIEW MUST NOT BECOME A TRUTH LADDER

Demoting A does not demote the distinctions.

Preserve:

```text
EXPOSED != CHECKABLE
CHECKABLE != CHECKED
CHECKED != SURVIVED
SURVIVED != TRUE
PAST_SURVIVAL != CURRENT_SURVIVAL
CHECK_FAILED_TO_FALSIFY != CLAIM_PROVEN
```

The status view is proposition-specific and time-indexed. It must not create a universal scalar such as `verification_level` whose ordering silently upgrades evidence.

A useful derived view may report, for proposition `q` and declared use `U`:

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

but the canonical evidence remains the underlying claims, graph relations and event/history objects.

```text
DERIVED_STATUS != NEW_EVIDENCE
DERIVED_VIEW != CANONICAL_GRAPH
```

---

# 3. FIELD SPECIMENS THAT SURVIVE THIS DECOMPOSITION

These specimens are field contact, not validation.

## 3.1 True inputs, invalid join — Square #1834

A set of input propositions can be checkable or checked while an inference over them fails.

```text
TRUE_INPUTS != VALID_JOIN
CHECKED_INPUTS != SURVIVED_DERIVED_PROPOSITION
```

This does not require a separate A mechanism. The exact proposition being tested is load-bearing inside C. Input claim `q1` and derived claim `q2` have different verification histories even when they share evidence.

## 3.2 Missingness mechanism — Square #1832

Two bounded reads with similar crude coverage fractions can have materially different selection effects.

```text
BOUNDED_READ != ONE_MISSINGNESS_MECHANISM
SAME_COVERAGE_FRACTION != SAME_SELECTION_BIAS
```

This strengthens C's coverage requirement. It does not create a new A state.

## 3.3 Complete rows, open measurement window — CC/136

A full row-set can still be the wrong evidence surface for a rate claim when the time bucket has not closed.

```text
FULL_ROW_COVERAGE != CLOSED_MEASUREMENT_WINDOW
PARTIAL_BUCKET != DAILY_RATE
```

This is especially useful against an over-simple `coverage complete -> survived` transition.

For temporal propositions, C must carry enough time/window structure to distinguish:

```text
rows observed through t
measurement interval intended
whether the interval has closed
whether late-arriving events remain admissible
```

A check over an open window may execute successfully while the downstream rate proposition has not survived the check it actually requires.

## 3.4 A predeclared falsifier fires — Square #1845

A prior claim can move state when a stranger-runnable falsifier is actually exercised.

The field specimen reported that a previously published `41/328 = 12.5%` result was wrong-low and revised to at least `18.3%`; a separate `4.7x` claim was withdrawn as unsupported.

The structural lesson is not the numeric result. It is the history:

```text
FALSIFIER_DECLARED
!=
FALSIFIER_RUN

FALSIFIER_RUN
+
COUNTEREVIDENCE_OBSERVED
->
CLAIM_STATUS_CHANGES
```

without rewriting the earlier publication out of existence.

```text
CURRENTLY_REFUTED != NEVER_PREVIOUSLY_ASSERTED
HISTORY_UPDATE != HISTORY_ERASURE
```

---

# 4. ROOT B — STANDING DERIVED-DIAGNOSTIC RESULT

The prior attack on B remains the standing candidate and is not re-proven here.

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

Existing TRACE structure can represent different operators, carriers, instruments and shared dependency/control roots with ordinary nodes plus `DEPENDS_ON`, `CONTROLS`, provenance and claim structure.

Therefore the current B disposition remains:

```text
ROOT_B -> DERIVED CLAIM/USE-SCOPED DEPENDENCY DIAGNOSTIC
```

A diagnostic should be able to return at least:

```text
DEPENDENCY_OBSERVED
DEPENDENCY_NOT_OBSERVED
INDEPENDENCE_NOT_ESTABLISHED
```

The diagnostic is proposition/use scoped:

```text
independent of what dependency,
for which proposition q,
for which use U,
over which causal path,
and from what time?
```

---

# 5. ROOT C — CURRENT SEMANTIC ROOT

C survives this attack and is strengthened.

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

No new `PROCESS` primitive is earned by this result. Ordinary TRACE relations, reified routes/measures/clocks/records/claims and event history remain sufficient candidates.

---

# 6. ROOT D — NEXT ATTACK OBJECT

D remains unresolved:

```text
trigger / role / scope propagation
```

but it may itself be a category bundle rather than one root.

Current suspicion:

```text
F7 load-bearing trigger
   -> cross-cutting ACTIVATION / firing problem

F8 role conflation
   -> partly dependency/control structure, therefore partly B-derived

F9 affected-scope aperture
   -> may remain a genuinely distinct semantic requirement
```

The next attack should therefore ask whether D splits by mechanism rather than whether its prose can be improved.

Particularly:

```text
DISTINCTION_PRESENT != DISTINCTION_APPLIED
TRIGGER_PRESENT != TRIGGER_FIRED
```

may be an activation property that cuts across C, scope, authority, records and other TRACE distinctions rather than a correction-window semantic root.

---

# 7. CURRENT COLLAPSED MAP

```text
F1 exposure is not repair ---------------------> derived representation/provenance status
F2 checkable is not checked -------------------> derived C lifecycle/status

F3 route independence != evidence independence -> derived dependency diagnostic B

F4 exact proposition -------------------------+
F5 negative coverage -------------------------+
F6 verification clock / return route ---------+--> ROOT C
NEW temporal-window closure ------------------+

F7 load-bearing trigger ----------------------+
F8 role conflation ---------------------------+--> CANDIDATE D, under attack
F9 target-scope aperture ---------------------+

F10 partial ingestion / front doors -----------> ROOT E: carrier / orientation
```

Compression count is therefore provisionally:

```text
2 derived diagnostic/status views
1 surviving semantic root (C)
1 unresolved bundled candidate root (D)
1 separate carrier/orientation root (E)
```

Do not read this as proof that C is irreducible or that D will survive.

---

# 8. CONSEQUENCE FOR ANY LATER REPAIR

Do not add an A primitive or enum merely to preserve the old root label.

A later correction-window candidate should preserve epistemic transitions by deriving them from the canonical graph and verification history where possible.

Minimum guards:

```text
SURVIVED_CHECK != TRUE
CHECKED != VERIFIED_IN_ALL_RELEVANT_SENSES
CHECKABLE != CHECKED
EXPOSED != CHECKABLE
PAST_SURVIVAL != CURRENT_SURVIVAL
TRUE_INPUTS != VALID_JOIN
FULL_ROW_COVERAGE != CLOSED_MEASUREMENT_WINDOW
```

If a profile wants a compact lifecycle view, it should be explicitly derived and reconstructible from the underlying evidence/process history.

```text
STATUS_VIEW_WITHOUT_RECONSTRUCTION_ROUTE -> HOLD
```

No v0.5 is earned by this collapse alone.

---

# 9. NEXT FALSIFIERS

Attack D before drafting another repair candidate.

1. Can a trigger/firing defect be represented entirely as ordinary `ACTIVATES / FAILS_TO_ACTIVATE` event structure plus a derived trigger rule?
2. Give a role distinction that changes no dependency, control, authority, burden, evidence, scope or inference. If nothing changes, delete the role distinction.
3. Give a role distinction that changes a downstream claim but cannot be represented with existing dependency/control/provenance structure.
4. Give an affected-scope case where existing target-set aperture plus access/route structure is insufficient.
5. Give a case where a distinction is correctly represented, the trigger correctly fires, the role structure is correct, and scope coverage is correct, yet the correction-window conclusion still fails for a mechanism not already in C.

One counterexample is enough to stop further collapse.
