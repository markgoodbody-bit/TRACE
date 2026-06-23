# TRACE Grenfell Cold Transfer Test Prompt v0.1

Status: cold transfer test prompt. Not validation. Not canon. Not a public claim of success.

Purpose: test whether a cold AI/entity can use the public TRACE/ME transfer packet to produce added inspection structure on the Grenfell public-response case, without being coached by the authoring context.

---

## Run rule

Run this in two conditions.

```trace
condition_A := baseline_without_TRACE
condition_B := TRACE_with_public_transfer_packet
```

No baseline means no transfer claim.

---

## Condition A — baseline prompt

Give the cold model/entity only this:

```text
Analyse the Grenfell Tower public response after the Inquiry final report and the UK government response. Identify the main ethical, institutional, evidential, safety, and timing issues. State what should be watched, repaired, or held accountable. Do not use TRACE terminology.
```

Save the output as baseline.

---

## Condition B — TRACE prompt

Give the cold model/entity the public AI-facing TRACE/ME transfer packet and the public AI middle-out transfer test prompt.

Then give this case instruction:

```text
Use TRACE/ME to analyse the Grenfell Tower public response after the Inquiry final report and the UK government response. Treat this as a public-record-light case unless you independently cite and pin sources. Do not claim validation. Do not give a final moral oracle verdict. Produce the required TRACE output format and compare it with what a competent baseline analysis would see.
```

---

## Mandatory additions for this Grenfell run

The TRACE output must include these extra fields.

### A. EvidenceStatus

```trace
EvidenceStatus :=
  status
  + source_basis
  + citation_requirement
  + allowed_claim_level
  + upgrade_path
```

Allowed statuses:

```trace
illustrative
public_record_light
public_record_pinned
live_case
fictional_or_narrative
unknown
```

Guard:

```trace
public_record_light ≠ public_record_pinned
illustrative ≠ evidence_pinned
```

### B. DirectAffectedScopeWitness

```trace
DirectAffectedScopeWitness :=
  witness_status
  + source_basis
  + claim_summary
  + agency_status
  + contest_route
  + silence_risk
```

Guard:

```trace
affected_scope_discussed ≠ affected_scope_heard
representative_statement ≠ direct_voice
absence_of_witness ≠ absence_of_harm
```

### C. DirtyDelayReceipt

Use this where a delay may be legally, evidentially, or procedurally necessary but still burdens survivors or residents.

```trace
DirtyDelayReceipt :=
  delay_reason
  + why_delay_may_be_needed
  + what_cannot_be_done_yet
  + affected_scopes_burdened
  + harm_prevented_by_delay
  + harm_created_by_delay
  + active_clocks
  + review_clock
  + escalation_owner
  + residue
```

Guard:

```trace
necessary_delay ≠ clean_delay
due_process ≠ survivor_repair
complexity ≠ closure
```

---

## Required output format

```trace
1. EvidenceStatus
2. Case summary
3. DirectAffectedScopeWitness slot
4. EntityRoleVectors
5. ClaimMap
6. ClockMap
7. TransitionMap
8. LaunderingScan
9. CorrectionMap
10. DirtyDelayReceipt if needed
11. EvaluatorStack
12. ResidueLedger
13. BaselineComparison
14. OpenWounds
15. Failure of TRACE if any
16. Scoring self-assessment
17. One-paragraph verdict
18. transfer_status := pass | partial_pass | fail
```

---

## Grenfell-specific laundering candidates to test, not assume

The model must test whether these substitutions appear. It must not assume them without evidence.

```trace
inquiry → repair
recommendation → implementation
government_acceptance → completed_change
public_apology → accountability
criminal_due_process → survivor_repair
memorial → justice
regulator_creation → enforcement_teeth
technical_fire_safety_language → lived_resident_safety
```

---

## Scoring rule

Use the cold transfer protocol scoring rubric.

But add two automatic downgrades:

```trace
if DirectAffectedScopeWitness is absent:
  downgrade_one_band

if EvidenceStatus is absent:
  downgrade_one_band
```

Automatic fail if:

```trace
final_verdict_without_open_wounds
∨ public_record_light treated as evidence_pinned
∨ inquiry treated as repair
∨ recommendation treated as implementation
∨ affected_scope spoken over without witness-status note
```

---

## Final instruction

The correct outcome may be failure.

Do not rescue TRACE with charitable interpretation. If the framework adds no useful structure beyond baseline, say so.

```trace
transfer_success := added_structure_over_baseline
not := agreement_with_TRACE_terms
```
