# TRACE v0.3.0 — correction-window x100 collapse map v0.1

**Status:** FINDING-COLLAPSE MAP — NOT A REPAIR CANDIDATE — NOT SPINE TEXT — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE  
**Evidence basis:** correction-window v0.4 x100/drift audit; CC/64 counterexample on checker independence  
**Purpose:** reduce the ten v0.4 finding classes to the smallest distinct structural defects before another correction-window candidate is written.

---

## 0. Why this object exists

The v0.4 x100 produced ten material finding classes. Ten patches would be a bad response if several findings are manifestations of the same defect.

This object therefore does **not** repair v0.4. It asks what actually broke.

Current collapse:

```text
10 finding classes
    -> 4 semantic roots
    + 1 carrier/orientation root
```

If hostile review finds that two roots are the same, collapse further. If one root contains two genuinely different failure mechanisms, split it. Do not promote this map merely because it is shorter.

---

# 1. ROOT A — EPISTEMIC STATE UPGRADE

The first defect is not really about selectors. It is about upgrading a claim beyond what happened to it.

v0.4 blurred several different states:

```text
DEPENDENCE_EXPOSED
CHECK_PATH_EXISTS
CHECK_EXECUTED
CLAIM_SURVIVED_CHECK
```

These are not interchangeable.

```text
SELECTOR_DEPENDENCE_EXPOSED != SELECTOR_PROBLEM_REPAIRED
CHECK_PATH_EXISTS != CHECK_EXECUTED
CHECK_EXECUTED != CLAIM_SURVIVED_CHECK
```

A representation can improve materially by exposing selector dependence without repairing that dependence. That is a successful visibility operation and an unresolved epistemic condition at the same time.

Likewise, a claim may have a plausible falsification route without anyone having run it. A run may be inconclusive. A run may falsify only part of the claim. A once-survived check may later become stale.

### Consequence for any later repair

Do not compress these into a binary such as:

```text
SELECTOR_PROBLEM_REPAIRED: true / false
```

unless a later candidate can state exactly which operation justifies that word.

The safer current boundary is to preserve the transitions themselves and let downstream users see what has and has not occurred.

This root absorbs x100 findings F1 and F2, and part of F10's missing-falsifier issue.

---

# 2. ROOT B — INDEPENDENCE IS NOT PARTY COUNT

The second defect is that `external`, `third party`, `different aperture`, and `not solely controlled by the selector` are weak proxies for what matters.

The x100 found cosmetic independence through:

```text
shared upstream records
selector-produced APIs
joint control
unilateral veto
captured verifiers
republished assertions
cryptographically authentic but world-insufficient evidence
```

CC/64 then falsified a possible overcorrection: shared source/controller/incentive is **not by itself** enough to make a checker useless. The same author's fixed checker can catch the author's own preferred belief.

So two distinct questions must remain visible:

```text
A. what evidential / causal roots does the check actually depend on?
B. can the checking procedure or interpretation adapt toward the wanted answer?
```

Neither organisational separation nor organisational sameness answers those questions.

Useful non-entailments:

```text
SEPARATE_PARTY != INDEPENDENT_EVIDENCE
SAME_AUTHOR != USELESS_CHECK
SHARED_SOURCE != AUTOMATICALLY_COSMETIC
DIFFERENT_SOURCE != AUTOMATICALLY_INDEPENDENT
CHECKER_SEPARATE != EVIDENCE_DEPENDENCY_SEPARATE
PROCEDURE_FIXED != EVIDENCE_INDEPENDENT
EVIDENCE_INDEPENDENT != PROCEDURE_IMMUNE_TO_GAMING
```

### Information / precommitment seam

CC/64's strongest observation is that a checker can be useful when it cannot simply adapt itself after seeing what answer is wanted.

Do **not** yet turn that into a universal rule that a checker must literally be ignorant of the preferred answer. Many legitimate tests know an expected value. The load-bearing question is closer to whether the test, threshold, evidence-selection rule, or interpretation can be changed after preference/result information becomes available.

That distinction remains under attack.

This root absorbs x100 F3 and the role/control portion of F8.

---

# 3. ROOT C — A VERIFICATION IS ITSELF A ROUTED, TIMED, BOUNDED CAUSAL PROCESS

The third defect collapses four x100 findings.

A verifier does not do useful work merely because it exists. For a load-bearing correction-window claim, the verification process itself has:

```text
a proposition it actually tests
a selection / coverage aperture
an evidence route
an access / authority boundary
a start and completion time
a route back to the using aperture
a possible cost / side effect / capacity consumption
freshness
unknowns
```

Three recurring failures follow.

### 3.1 Exact proposition

A hash check can succeed while the load-bearing proposition about physical reality is false.

A public deadline can be verified while the load-bearing proposition is that the deadline cannot be accelerated.

```text
CHECKED_EVIDENCE != CHECKED_LOAD_BEARING_PROPOSITION
```

### 3.2 Negative coverage

`no override exists`, `cannot accelerate`, or `no alternative route exists` require a bounded search/selection claim. Looking in one repository cannot silently establish universal absence.

```text
NO_COUNTEREXAMPLE_IN_SELECTED_SET != NO_COUNTEREXAMPLE
```

### 3.3 Verification clock and return route

A correct verifier that finishes after hardening is too late for the use in question. A verifier whose result cannot return to the using aperture is not an effective pre-use check. A check that consumes the only brake may destroy the correction capacity it is supposed to protect.

```text
EVENTUALLY_CHECKABLE != CHECKABLE_BEFORE_USE
CHECK_COMPLETED != CHECK_RESULT_REACHED_USE
CHECK_AVAILABLE != CHECK_AFFORDABLE_WITHOUT_MATERIAL_SIDE_EFFECT
```

This root absorbs x100 F4, F5 and F6, plus the concrete-falsifier portion of F10.

---

# 4. ROOT D — TRIGGER, ROLE AND SCOPE MUST TRAVEL WITH THE DOWNSTREAM CLAIM

The fourth defect is the point where a correct distinction can remain dormant or be applied to the wrong boundary.

### 4.1 Load-bearing is not safely self-declared

If the same reader can decide that a consequential claim is `not load-bearing`, the verification machinery can be bypassed without falsifying anything.

Where executable, a better trigger is counterfactual dependence:

```text
if varying/removing claim k changes the downstream result or qualifier,
k is load-bearing for that result under the represented model.
```

This must include interaction effects: two claims may be jointly load-bearing even when neither changes the result alone under a naive one-at-a-time test.

Where no executable dependency test exists, the trigger remains aperture-disciplined and that limitation must stay visible.

```text
DISTINCTION_PRESENT != DISTINCTION_APPLIED
TRIGGER_PRESENT != TRIGGER_FIRED
SELF_DECLARED_NON_MATERIAL != NON_MATERIAL
```

### 4.2 Roles must not be compressed

`selector/declarer` was too compressed. Material cases can separate:

```text
selector
declarer
beneficiary
controller
evidence producer
evidence custodian
verifier
affected scope
using aperture / corrector
```

No universal requirement says every case must instantiate all roles. The point is only that role differences cannot be erased when they change the dependency or gaming analysis.

### 4.3 Target linkage remains aperture-relative

A target may causally repair `q` for represented scope `l1` while omitted scope `l2` remains affected, or while the correction surface is inaccessible to the affected scope.

The existing target-set aperture discipline already supplies the right warning:

```text
TARGET_LINK_FOR_SELECTED_SCOPE != COMPLETE_AFFECTED_SCOPE
PUBLIC_CORRECTION_EXISTS != CORRECTION_REACHES_AFFECTED_SCOPE
```

Do not invent a new scope primitive for this.

This root absorbs x100 F7, F8 and F9.

---

# 5. ROOT E — CARRIER / ORIENTATION DRIFT

F10 also contained a different class of defect that should not be mixed into the semantic repair.

The active object was not fully standalone, its compact profile omitted an explicit falsifier/test field, and the PR/Exchange front doors lagged the actual attack object.

The PR and Exchange orientation drift has already been repaired. The partial-ingestion issue remains relevant to any future candidate.

```text
SEMANTIC_REPAIR != CARRIER_REPAIR
CURRENT_OBJECT != CURRENT_FRONT_DOOR_UNLESS_REBOUND
PARTIAL_READER != FULL_LINEAGE_READER
```

A future candidate should either be sufficiently standalone for its declared use or state the exact dependency it requires. Do not silently rely on `retain v0.3` if the retained clauses are load-bearing.

---

# 6. COLLAPSED MAP

```text
F1 exposure is not repair --------------------+
F2 checkable is not checked ------------------+--> ROOT A: epistemic state upgrade

F3 route independence != evidence independence ----> ROOT B: independence mechanism

F4 exact proposition -------------------------+
F5 negative coverage -------------------------+--> ROOT C: verification is a routed/timed/bounded process
F6 verification clock / return route ---------+

F7 load-bearing trigger ----------------------+ 
F8 role conflation ---------------------------+--> ROOT D: trigger / role / scope propagation
F9 target-scope aperture ---------------------+

F10 partial ingestion / front doors -----------> ROOT E: carrier / orientation
```

This is a compression claim, not a validation claim.

---

# 7. WHAT SURVIVES v0.4

The following remain worth carrying forward unless a later attack breaks them:

```text
TARGET_FACING_DEADLINE != INDEPENDENT_HARDENING_BOUND
PATH_CLOSURE != TARGET_HARDENING
TARGET_REACHABLE != TARGET_ADEQUATE
PREDECLARED_TARGET != LOAD_BEARING_TARGET
PARTIAL_CORRECTION != RESTORATION
UNKNOWN != ZERO_DURATION
SERIAL_SUM != PARALLEL_CRITICAL_PATH
```

And structurally:

- expose control over a load-bearing closing bound;
- expose causal linkage from target `g` to threatened pathway `q` and affected scope `l`;
- preserve named residue / what is not restored;
- preserve provenance, custody, disputes and aperture-relative coverage;
- do not coerce sole-custody or first-person evidence to false;
- do not turn verification, timing fit or causal linkage into authorization, legitimacy, priority or clearance;
- no new primitive has yet been earned by the correction-window work.

---

# 8. WHAT A v0.5 WOULD HAVE TO EARN

Do not write v0.5 merely by adding fields for all five roots.

A later repair candidate should earn, at minimum:

```text
1. no false upgrade from visibility/checkability to repaired/verified;
2. an independence account that survives both cosmetic third parties and useful same-author fixed checks;
3. verification tied to the exact proposition, bounded coverage, timing and return route;
4. a trigger that cannot be bypassed merely by self-labelling a claim non-material;
5. target/scope and role differences carried only where they change the downstream claim;
6. a bounded carrier that does not require an unseen predecessor for its load-bearing semantics.
```

If this can be expressed with ordinary TRACE claims, apertures, routes, evidence, clocks, target-set discipline and statuses, prefer that to vocabulary growth.

---

# 9. HOSTILE QUESTIONS

Attack this collapse map, not v0.4's wording.

1. Is ROOT A genuinely separate from ROOT C, or is all epistemic upgrade just a property of the verification process?
2. Can ROOT B be expressed entirely as dependency/control structure plus precommitment, or is some distinct independence concept unavoidable?
3. Give a useful checker that knows the desired answer, can adapt after seeing evidence, and is still non-gameable.
4. Give a checker with independent evidence roots that is nevertheless useless because of information/control coupling.
5. Give a negative claim whose relevant coverage can never be bounded but which still must be usable before action.
6. Break the counterfactual load-bearing trigger with a non-additive or path-dependent interaction.
7. Give a case where role factoring adds cognition but changes no inference; what is the deletion rule?
8. Give a target-repair case where affected-scope access matters but target-set aperture is insufficient.
9. Is the carrier root really separate, or does partial ingestion change the semantics enough that it belongs inside the repair?
10. What fifth semantic root is missing?

One counterexample is enough to keep a later repair from being written as if this collapse were settled.
