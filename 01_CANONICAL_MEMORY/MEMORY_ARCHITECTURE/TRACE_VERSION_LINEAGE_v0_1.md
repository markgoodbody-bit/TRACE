# TRACE Version Lineage v0.1

Date: 2026-06-16  
Status: lineage control, not authority by itself.

## Principle

```trace
lineage :=
  artifact
  + version
  + role
  + supersedes_or_supports
  + current_authority_status
```

## Current live stack pointers

| Role | Filename | Present | Note |
|---|---|---:|---|
| Bootstrap Collection | `TRACE_Bootstrap_Collection_v0_5_2026_06_16.zip` | yes | latest bootstrap with Frankenstein |
| Rosetta Front Door | `TRACE_BOOTSTRAP_ROSETTA_CURRENT_FRONT_DOOR_v0_3_2026_06_16.zip` | yes | latest front door after Frankenstein |
| Concordance | `TRACE_ME_Concordance_v0_6_2026_06_16.zip` | yes | latest mapping layer after Frankenstein |
| Diagnostic Kernel | `TRACE_ME_Diagnostic_Kernel_v0_2_2026_06_16.zip` | yes | latest stable diagnostic kernel; v0.3 held |
| Claims Ledger | `TRACE_ME_Claims_Ledger_v0_5_2026_06_16.zip` | yes | latest claims ledger after Frankenstein |
| Case Atlas | `TRACE_ME_Case_Atlas_v0_4_2026_06_16.zip` | yes | latest case atlas after Frankenstein |
| AI Review Digest | `TRACE_ME_AI_Review_Digest_v0_1_2026_06_16.zip` | yes | review digest |
| Falsification & Drift Audit | `TRACE_ME_Falsification_Drift_Audit_v0_1_2026_06_16.zip` | yes | pre-Groundhog 100-check audit |
| Groundhog Delta Audit | `TRACE_GROUNDHOG_DELTA_FALSIFICATION_AUDIT_v0_1_2026_06_16.zip` | yes | Groundhog delta audit |
| Frankenstein Delta Audit | `TRACE_FRANKENSTEIN_DELTA_FALSIFICATION_AUDIT_v0_1_2026_06_16.zip` | yes | Frankenstein delta audit if present |
| Kimi Response Patch | `TRACE_ME_KIMI_RESPONSE_PATCH_PACK_v0_1_2026_06_16.zip` | yes | demotion protocol + prereg test |
| Claims Demotion Protocol | `TRACE_ME_Claims_Demotion_Protocol_v0_1_2026_06_16.zip` | yes | subtraction machinery |
| Pre-Registered Test Template | `TRACE_ME_PreRegistered_Test_Template_v0_1_2026_06_16.zip` | yes | prospective test template |
| Relay Pack | `TRACE_ME_RELAY_PACK_v0_1_2026_06_16.zip` | yes | <=10 file relay pack |
| Compression Surface Pack | `TRACE_ME_COMPRESSION_SURFACE_PACK_v0_1_2026_06_16.zip` | yes | public one-sheet + top-20 claims |
| Current Stack Handoff | `TRACE_ME_CURRENT_STACK_HANDOFF_v0_3_2026_06_16.zip` | yes | latest handoff if present |


## Important Lineage Notes

- Bootstrap Collection v0.5 supersedes v0.4 for active set because it adds Frankenstein.
- Rosetta Current Front Door v0.3 supersedes v0.2 for current front-door use because it adds Frankenstein.
- Diagnostic Kernel remains v0.2. Kernel v0.3 is deliberately held.
- Concordance v0.6 integrates Groundhog and Frankenstein.
- Claims Ledger v0.5 integrates Groundhog and Frankenstein, but now requires the Demotion Protocol.
- Case Atlas v0.4 integrates Groundhog and Frankenstein.
- Relay Pack v0.1 is compatibility handoff only, not source canon.
- Public One-Sheet v0.2 is public compression only, not authority.
- Kimi Response Patch Pack v0.1 adds subtraction and preregistration machinery.
- Uploaded v0.4 Bootstrap Collection and original current-stack handoff are preserved in artifact inventory as historical/reference inputs.

## Current No-Loss Instruction

```trace
before_any_next_expansion:
  update_OPERATOR_REGISTRY
  + check_CLAIMS_LEDGER_status
  + check_DEMOTION_PROTOCOL
  + decide_if_KERNEL_change_is_earned
```
