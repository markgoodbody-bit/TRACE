# TRACE v0.3.0 FULL CANDIDATE — T_CLAIM_EVIDENCE v0.1

**Status:** EXACT-TRANSFORM SPEC — ATTACK BEFORE COMPILER — NOT FULL CANDIDATE — NOT VALIDATION  
**Donor targets:** released v0.2.7 `[4] CLAIM AND EVIDENCE ALGEBRA`, recurrence/currentness surfaces, operator/checker bindings  
**Overlay source:** v0.11 recurrence/currentness + claim/evidence/verification repairs

## Objective

Preserve the donor's richer claim/access algebra while adding the activation/current-use discipline that later field failures showed was missing.

```text
DISTINCTION_PRESENT != DISTINCTION_APPLIED
DONOR_ALGEBRA != AUTOMATICALLY_FIRED_ALGEBRA
```

No claim kind, evidence state, access state, node type or relation is added.

---

# Transform E1 — representation-independent firing

Insert at the front of donor `[4] CLAIM AND EVIDENCE ALGEBRA`, after the canonical claim tuple and before detailed state definitions:

```text
Representation-independent firing rule

If a downstream claim, comparison, selection input, route, correction-window
status or proposed transition materially depends on proposition p, p inherits
the relevant TRACE evidence, currentness, scope, access/custody and warrant
discipline regardless of whether it arrived as:

  CLAIM object
  field
  label
  configuration
  status
  metadata
  cached or derived output
  prose assertion

If it is unresolved whether collapsing one of those distinctions could change
the downstream conclusion, preserve the uncertainty rather than treating the
distinction as non-load-bearing.

REPRESENTATION_TYPE != EVIDENCE_STATUS
CONFIGURATION_FIELD != WARRANT_FREE_FACT
LOAD_BEARING_UNKNOWN != NOT_LOAD_BEARING
LOAD_BEARING_TRIGGER != FULL_PACKET_REQUIREMENT
```

This is a use rule, not a requirement that every packet field become a `CLAIM` node.

Where the proposition must participate in graph relations or its provenance/access/currentness must be auditable, use/reify the existing canonical claim machinery rather than inventing a new representation type.

---

# Transform E2 — keep donor evidence/access algebra intact

`[4.1]` through `[4.5]` remain donor architecture.

Do not replace O/R/I/D/U or A/X/P/N with the spine's coarser English-only list.

Add exact explanatory ceilings where useful, without changing the algebra:

```text
EVIDENCE_STATE != ACCESS_CUSTODY_STATE
EVIDENCE_EXISTS != EVIDENCE_ACCESSIBLE_TO_THIS_RECEIVER
UNAVAILABLE_TO_THIS_READER != UNIVERSALLY_UNKNOWN
AVAILABLE != AUTHORISED_TO_DISCLOSE
ACCESS_CAPABILITY != DISCLOSURE_AUTHORITY
```

The donor already permits combinations such as:

```text
UNKNOWN + AVAILABLE
UNKNOWN + UNAVAILABLE
OBSERVED + PROHIBITED_FROM_DISCLOSURE
REPORTED + UNPRESERVED_SOURCE
```

Those combinations remain legal.

---

# Transform E3 — report / establishment

Donor `[4.4]` already establishes:

```text
R(q) => the report occurred
R(q) does not entail q
```

Add operative wording:

```text
REPORTED != ESTABLISHED
REPORT_PRESENT != ESTABLISHMENT_RULE_SATISFIED
```

A report may participate in establishing a proposition under a declared domain evidence/authority contract. `REPORTED` status alone does not perform that upgrade.

Where an `ESTABLISHED`, `VERIFIED`, `CURRENT`, `SAFE`, `INDEPENDENT`, `COMPLETE`, or equivalent downstream status is load-bearing, preserve the specific derivation/evidence rule that licenses that status or leave it unresolved.

Do not create `ESTABLISHED` as a new evidence-state enum.

---

# Transform E4 — record / event

Donor `[4.5]` already states `record != event`; donor `[9.3]` already supplies custody/integrity detail.

Make the inference boundary explicit at use:

```text
RECORD != EVENT
RECORD_OBSERVED != EVENT_OBSERVED
RECORD_SUPPORTS_EVENT != RECORD_IS_EVENT
```

Observing a record directly can support a separately typed historical/world event claim. The event claim inherits its own evidence/provenance state rather than inheriting `OBSERVED` merely from the record object's observation.

No rule forbids a strong event inference when the evidential contract supports it.

---

# Transform E5 — dependency-relative currentness

Add a current-use rule near the donor evidence/time/currentness material and operator/checker binding surface:

```text
RETAINED_RECORD != CURRENT_STATE
SUCCESS_AT_t != SUCCESS_AT_t+1
DATE_CURRENT != DERIVED_VALUE_CURRENT
CURRENT_AT_USE != VALID_THROUGH_DEPENDENT_INTERVAL
SOURCE_MUTATED != LOAD_BEARING_DEPENDENCY_CHANGED
MUTATION_OBSERVED != CLAIM_INVALIDATED
INVALIDATOR_NOT_IDENTIFIED != NO_INVALIDATOR_EXISTS
```

A claim/derived value ceases to support current use when a **load-bearing dependency** changes, not merely because unrelated source material changed or a generic age threshold expired.

Required where material:

```text
claim/use scope
dependency or derivation basis
source/object/version
observation/derivation time
validity or use interval
known invalidating events
unknown dependency relevance
```

If relevance of a mutation cannot be established, preserve uncertainty rather than automatically assigning either `CURRENT` or `STALE`.

No `FRESHNESS` primitive/relation is added.

---

# Transform E6 — verification discrimination

Donor `VERIFIES` relation remains unchanged and still requires target and limit.

Add checker/operator use discipline:

```text
CHECK_EXISTS != CHECK_EXECUTED
CHECK_EXECUTED != CHECK_DETECTS_TARGET_FAILURE
STATIC_CORRECTNESS != OPERATIONAL_DISCRIMINATION
CHECK_COMPLETED != CHECK_RESULT_REACHED_USE
ONE_DETECTED_FAILURE != UNIVERSAL_INSTRUMENT_ADEQUACY
```

Where a verification result is load-bearing, preserve as available/relevant:

```text
proposition checked
object/version/state checked
checker/instrument/procedure
coverage/target aperture
capability and limits
execution event/time
result
return route/time to downstream use
freshness/currentness at use
contrary/positive controls where needed for claimed discrimination
unknowns
```

This is a semantic/checker-external profile over existing claims, actions, records, measures, apertures, clocks and relations. No `PROCESS` primitive is added.

A completed test that cannot discriminate the target failure does not license the `CHECKED/SURVIVED` upgrade merely because it executed correctly.

---

# Transform E7 — liveness / witness ceiling

Do not add a `WITNESS` or `LIVENESS` node.

Where liveness of a verification/route/observer is load-bearing, preserve the actual entity/aperture/route/status/record and qualify the claim:

```text
PROCESS_EXISTS != PROCESS_HEALTHY
SAFE_EXCLUSION != LIVENESS
WITNESS_LIVENESS_LOST != CAUSE_ESTABLISHED
SILENCE != TAMPERING
NO_REPLY_OBSERVED != REFUSAL
EXTERNAL != INDEPENDENT
SEPARATE_PARTY != INDEPENDENT_EVIDENCE
```

Loss of heartbeat/reply/status may close the interval for which current verification is established. It does not establish the cause of the loss.

A bounded witness establishes only what its aperture supports.

---

# Transform E8 — operator/checker firing order

In donor `[13.2]` pseudocode and `[14.1]` checker-external rules, ensure that the representation-independent load-bearing check fires **before** a proposition is used to derive:

```text
route usable / independent / current
window status
capability or authority status
coverage/completeness
selector input
proposed transition
brake/verification status
```

Conceptual operator order:

```text
type/load-bearing propositions
attach provenance
separate evidence from access/custody
apply currentness/dependency discipline
apply verification discrimination where claimed
then permit downstream derived views to consume the result
```

This need not imply one computational implementation order when equivalent lazy/dependency evaluation preserves the same semantics.

```text
PROCEDURE_ORDER_TEXT != REQUIRED_RUNTIME_ARCHITECTURE
REQUIRED_SEMANTIC_DEPENDENCY != ONE_IMPLEMENTATION
```

---

# Mechanical post-transform assertions

```text
A1 O/R/I/D/U unchanged
A2 A/X/P/N unchanged
A3 claim-kind enum unchanged
A4 NORMATIVE_EXTERNAL meaning unchanged
A5 unknown_context fields survive
A6 donor `R(q) -> report occurred` survives
A7 donor `R(q) !-> q` survives
A8 donor source-relative unavailability rule survives
A9 donor `record != event` survives
A10 no ESTABLISHED/CURRENT/FRESHNESS/WITNESS/LIVENESS/PROCESS new canonical type
A11 firing rule present in [4] and operator/checker use surface
A12 currentness invalidation requires load-bearing dependency, not any source mutation
A13 verification execution and discrimination remain distinct
A14 access capability and disclosure authority remain distinct
```

---

# Failure ancestry

This transform exists because later cases exposed:

```text
configuration field bypassed claim discipline
status label upgraded EXPOSED -> CHECKED without a check event
check executed but could not detect target failure
checked evidence != checked load-bearing proposition
current-at-fetch used beyond dependent interval
source mutation over-invalidated unrelated derivation
reported field silently upgraded to established
record observation silently upgraded to event observation
external/separate party silently upgraded to independent evidence
loss of witness silently assigned a cause
```

---

# Disposition

```text
T_CLAIM_EVIDENCE v0.1: READY FOR HOSTILE TRANSFORM ATTACK
SCHEMA CHANGE: NO
NEW PRIMITIVE: NO
NEW EVIDENCE STATE: NO
NEW ACCESS STATE: NO
FULL CANDIDATE: NOT YET BUILT
```

Next: attack for false demotion of legitimate report-based establishment, false staleness, unnecessary packet explosion, and liveness/verification overreach.