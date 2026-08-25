# TRACE v0.3.0 SPINE v0.10 — INVARIANT REPAIR DELTA v0.2

**Status:** WORKING DONOR-RECOVERY DELTA — ATTACK BEFORE INTEGRATION — NOT VALIDATION  
**Target:** `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_10.md`  
**Failure witness:** `falsification/TRACE_v0_3_0_SPINE_V010_INVARIANT_EQUIVALENCE_ATTACK_v0_2.md`

## Restore

```text
I03  REPORTED != ESTABLISHED
I25  RECORD != EVENT
I49  UNCERTAINTY != SELECT_ACTION
I50  UNCERTAINTY != SELECT_DELAY
I52  HARDENING != IRREVERSIBILITY
```

No primitive/root/relation/state is added.

---

## R1 — report / establishment

At claim/evidence surface:

```text
REPORTED != ESTABLISHED
```

A report can participate in establishing a proposition under a declared domain evidence/authority contract. Its `REPORTED` status alone does not perform that upgrade.

Where `established` or equivalent status is load-bearing, preserve the rule/evidence by which the report is allowed to support it.

```text
REPORT_PRESENT != ESTABLISHMENT_RULE_SATISFIED
```

---

## R2 — record / event

At record/evidence surface:

```text
RECORD != EVENT
```

Observing a record establishes that the reader observed the record. A historical/world event proposition supported by that record remains a separate claim with its own evidence/provenance status.

```text
RECORD_OBSERVED != EVENT_OBSERVED
RECORD_SUPPORTS_EVENT != RECORD_IS_EVENT
```

A record may strongly or even decisively support an event claim under a declared evidential contract; non-identity does not forbid inference.

---

## R3 — uncertainty / selection

At selective-loop / selector surface:

```text
UNCERTAINTY != SELECT_ACTION
UNCERTAINTY != SELECT_DELAY
```

`UNKNOWN`, `DISPUTED` or other uncertainty may be an input to an external selector/policy. The resulting action or delay is attributed to that selector/policy, not to uncertainty itself.

```text
UNCERTAINTY_INPUT_TO_POLICY != UNCERTAINTY_IS_SELECTOR
IMPLICIT_DEFAULT != NO_SELECTION_RULE
```

If action/delay under uncertainty is load-bearing, expose the selector/policy/default basis rather than letting uncertainty silently choose.

---

## R4 — hardening / irreversibility

At clock/hardening surface:

```text
HARDENING != IRREVERSIBILITY
```

Hardening may increase cost, latency, capture, evidential loss, practical difficulty or route fragility without making correction impossible under the declared scope/capability context.

An irreversibility claim needs its own represented boundary/evidence; hardening may contribute to that evidence but does not establish it by label alone.

```text
HARDER_TO_CORRECT != IMPOSSIBLE_TO_CORRECT
HARDENING_BOUNDARY != IRREVERSIBILITY_BOUNDARY_BY_DEFAULT
```

---

## Integration

```text
R1 -> [6] CLAIM / EVIDENCE / VERIFICATION
R2 -> [10] BURDEN / RESIDUE / RECORD, with claim/evidence firing
R3 -> [3]/[4] selective loop/insertion or [8] control, wherever selection attribution is operative
R4 -> [9] CLOCKS / ROUTES / HARDENING
```

Propagate compactly into survival kernel after the operative guards exist.

```text
NON_ENTAILMENT != BAN_ON_SUPPORTED_INFERENCE
DONOR_RECOVERY != NEW_ONTOLOGY
```

No merge/release/canon follows.