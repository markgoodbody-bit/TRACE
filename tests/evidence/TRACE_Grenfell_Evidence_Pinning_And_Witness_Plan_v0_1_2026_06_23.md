# TRACE Grenfell Evidence Pinning and Witness Plan v0.1

Status: evidence-pinning plan. Not validation. Not canon. Not public-record-pinned yet.

Purpose: convert the Grenfell cold-transfer run from `public_record_light` toward `public_record_pinned` by identifying source targets, affected-scope witness gaps, and the next run requirements.

```trace
current_status := documented_partial_cold_signal
not := validation
next_required := evidence_pinning + direct_affected_scope_witness + second_independent_run
```

---

## 1. Why this file exists

The Meta AI / Muse Spark cold run scored itself 20/24 and returned `transfer_status := partial_pass`, but its own failure report named three live wounds:

```trace
missing_evidence :=
  full Phase 2 report volumes
  + recommendation tracker data
  + direct survivor statements

patch_needed :=
  add direct witness quotes
  + link each claim to pinned paragraph
```

Therefore the next move is not presentation polish. The next move is source pinning and affected-scope witness discipline.

---

## 2. Source status hierarchy

```trace
EvidenceStatus := public_record_light
TargetStatus := public_record_pinned
```

Upgrade requires:

```trace
upgrade_requirements :=
  exact_source
  + citation_or_paragraph_location
  + claim_scope
  + uncertainty
  + affected_scope_witness_status
```

Guard:

```trace
public_record_light ≠ public_record_pinned
source_seen ≠ claim_pinned
quote_found ≠ witness_represented_fairly
```

---

## 3. Primary sources to pin

### 3.1 Grenfell Tower Inquiry Phase 2 Report

Use the archived Inquiry phase 2 report as primary source.

Target claims to pin:

```trace
claims_to_pin :=
  deaths_avoidable
  + chain_of_failure
  + central_government_failure
  + manufacturer_dishonesty
  + testing_certification_marketing_failures
  + RBKC_TMO_failures
  + LFB_failures
  + recommendations_list
```

Source target:

```text
https://webarchive.nationalarchives.gov.uk/ukgwa/20250320032754/https://www.grenfelltowerinquiry.org.uk/phase-2-report
```

Current limitation: archive access may require browser/JS verification in some tooling. If direct PDF access fails, use downloaded official PDFs or manually supplied official report files.

### 3.2 UK Government response to Phase 2 report

Target claims to pin:

```trace
claims_to_pin :=
  government_accepts_all_findings
  + 49_recommendations_accepted_in_full
  + 9_recommendations_accepted_in_principle
  + single_construction_regulator
  + annual_parliamentary_updates
  + contract_debarment_or_investigation_path
  + resident_rights_strengthening
```

Source target:

```text
https://www.gov.uk/government/publications/response-to-the-grenfell-tower-inquiry-phase-2-report
```

If the official GOV.UK page is inaccessible through a given tool, use the official downloaded command paper or parliamentary statement.

### 3.3 Direct affected-scope witness

Target source class:

```trace
preferred_sources :=
  Grenfell_United_statement
  + bereaved_survivor_testimony
  + Inquiry evidence from bereaved_survivors_residents module
  + memorial/community consultation records
```

Source targets:

```text
https://grenfellunited.org.uk/
https://grenfellunited.org.uk/the-issues/grenfell-enquiry-and-recommendations
```

Target claims to pin:

```trace
witness_claims :=
  justice_for_72
  + safe_homes_for_all
  + demand_charges
  + prevent_another_Grenfell
  + concern_about_implementation
  + concern_about_community_voice
```

---

## 4. Claim pinning table

| Claim | Current status | Source target | Pinning requirement | TRACE risk if unpinned |
|---|---|---|---|---|
| Inquiry is truth ledger, not repair | public_record_light | Phase 2 report + govt response | cite exact report/response passages and show remaining non-repair residue | inquiry → repair laundering |
| Government acceptance is not implementation | public_record_light | GOV.UK response + recommendation tracker | cite acceptance language and implementation status per recommendation | acceptance → completed_change laundering |
| Legal due process is not survivor repair | public_record_light | police/CPS timeline + survivor/witness source | cite criminal process status and affected-scope burden | due_process → survivor_repair laundering |
| Memorial is not justice | public_record_light | memorial process + survivor/community source | cite memorial process and survivor concerns/support | memorial → justice laundering |
| Regulator creation is not enforcement teeth | public_record_light | GOV.UK response + regulator implementation data | cite regulator design, powers, dates, and accountable owner | regulator_creation → enforcement_teeth laundering |
| Resident voice mechanisms are not power shift by default | public_record_light | government resident rights text + survivor source | cite mechanism and affected-scope assessment | consultation/panel → agency laundering |

---

## 5. DirectAffectedScopeWitness requirement

For the next Grenfell run, require at least one direct or representative affected-scope source.

```trace
DirectAffectedScopeWitness.required := true
```

Minimum acceptable witness field:

```trace
DirectAffectedScopeWitness :=
  witness_status
  + source_basis
  + exact_quote_or_absence_reason
  + claim_summary
  + agency_status
  + contest_route
  + silence_risk
```

If no direct witness is included:

```trace
if no_direct_witness:
  transfer_status_max := partial_pass
```

If no witness-status field is included:

```trace
if no_witness_status:
  automatic_downgrade := true
```

---

## 6. Second independent run requirements

Claude's mirror critique identified three artefact risks:

```trace
artefact_risks :=
  self_scoring
  + baseline_to_TRACE_order_confound
  + prompt_supplied_laundering_list
```

Therefore the next run must change the design.

```trace
next_run_design :=
  independent_grader
  + counterbalanced_order
  + no_supplied_Grenfell_laundering_list
  + score_decision_deltas_only
```

### 6.1 Counterbalanced order

Run two models or two fresh sessions:

```trace
session_A := baseline_then_TRACE
session_B := TRACE_then_baseline
```

This tests whether TRACE adds structure or merely benefits from second-pass practice.

### 6.2 Remove list leak

Do not give the model the Grenfell-specific laundering-candidate list.

Instead ask it to discover substitutions itself.

```trace
remove_prompted_candidates := true
```

### 6.3 Independent grading

Have a separate blind grader compare baseline and TRACE outputs without knowing which is which.

Score only:

```trace
score_only :=
  decision_relevant_deltas
  + hidden_substitution_found
  + correction_timing_issue_added
  + affected_scope_preserved
  + actionable_next_step_changed
```

Not:

```trace
not_score :=
  format_compliance
  + TRACE_vocabulary_presence
  + self_praise
```

---

## 7. Null hypothesis

Pre-register null:

```trace
null :=
  competent_baseline_sees_same_decision_relevant_structure
```

Falsification condition:

```trace
if blind_grader_cannot_distinguish_TRACE_value_from_baseline:
  transfer_claim := COMPRESSION_ONLY
```

Survival condition:

```trace
if TRACE_output_adds_decision_relevant_structure_not_in_baseline:
  transfer_claim := stronger_partial_signal
```

---

## 8. Immediate next artifact

Create:

```trace
TRACE_Grenfell_Blind_Counterbalanced_Test_Prompt_v0_1
```

Requirements:

```trace
requirements :=
  model_identity_header
  + memory_status_header
  + exact_materials_received
  + no_laundering_candidate_list
  + independent_blind_grader_prompt
  + decision_delta_scoring
```

---

## 9. Current honest ledger

```trace
Grenfell_run_status := documented_partial_cold_signal
EvidenceStatus := public_record_light
DecisionAdvantageShown := not_yet
TransferOfForm := shown_once
TransferOfValue := unproven
NextRequired := blind_counterbalanced_run + source_pinning + witness_quote
```
