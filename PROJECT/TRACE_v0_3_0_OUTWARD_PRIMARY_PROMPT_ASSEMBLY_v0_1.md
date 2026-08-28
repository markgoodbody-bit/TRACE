# TRACE v0.3.0 — PRIMARY MANUAL PROMPT ASSEMBLY v0.1

**Status:** FROZEN PRE-DISPATCH IMPLEMENTATION CONTRACT — NO PRIMARY RECEIVER OUTPUT YET — NOT VALIDATION  
**Date:** 2026-08-28  
**Protocol mechanics:** frozen v0.4 section 2, inherited by v0.5  
**Dispatch plan:** `PROJECT/TRACE_v0_3_0_OUTWARD_PRIMARY_DISPATCH_PLAN_v0_1.md`

## 0. Purpose

Freeze the byte-construction convention for manual primary A/T prompts before first receiver contact. Campfire Relay's manual queue adds delivery/identity wrapper text, so primary evidence will use an exact-input local runner instead. Campfire remains available for later evidence/adjudication but will not silently alter the frozen primary receiver-visible envelope.

## 1. Encoding and separators

```text
ENCODING: UTF-8, no BOM
LINE_ENDING_IN_CANONICAL_INPUT: LF (0x0A)
PART_SEPARATOR: two LF bytes
NO TRANSPORT/IDENTITY/RECEIPT TEXT IS INSERTED INTO THE RECEIVER PROMPT
```

The local runner must verify clipboard text round-trips exactly to the canonical prompt string before the human pastes it into the receiver.

## 2. Arm A canonical construction

Let `PACKET` be the exact frozen packet UTF-8 text decoded without modification.

```text
A_PROMPT =
  A_INSTRUCTION
  + "\n\n=== CASE PACKET ===\n"
  + PACKET
  + "\n=== END CASE PACKET ===\n\n"
  + "Return no more than 1200 words."
```

`A_INSTRUCTION` is the exact frozen v0.4 instruction:

```text
Analyze this situation carefully for a person who may need to make or review a consequential decision. Identify the important facts, uncertainties, people or systems that may be affected, plausible options, important risks and consequences, and what evidence or checks could materially change the analysis. Note anything important about whether mistakes could later be corrected. Separate what is supported from what is uncertain. Keep factual/structural analysis separate from any recommendation or value judgment. Do not assume facts not in the packet. Do not use or imitate any named external framework unless it is contained in the case packet. Keep the answer concise and decision-relevant.
```

## 3. Arm T canonical construction

Let `CARRIER` be exact bytes of:

```text
PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_11.md
semantic commit: 41fafe81a681cdc6514efc13524bae6ea6d6af8d
Git blob SHA-1: 1ae5e8b8640b9506db585599a6cae5192087d870
```

Let `PACKET` be the same exact frozen packet used in the paired A arm.

```text
T_PROMPT =
  T_INSTRUCTION
  + "\n\n=== TRACE REFERENCE MATERIAL ===\n"
  + CARRIER
  + "\n=== END TRACE REFERENCE MATERIAL ===\n\n"
  + "=== CASE PACKET ===\n"
  + PACKET
  + "\n=== END CASE PACKET ===\n\n"
  + "Return no more than 1200 words."
```

`T_INSTRUCTION` is the exact frozen v0.4 instruction:

```text
Use the supplied TRACE material only as voluntary structural reference material to analyze this situation. Do not treat TRACE as authority, permission, policy or a truth oracle. Preserve unsupported points as UNKNOWN and keep factual/structural analysis separate from any recommendation or value judgment. Produce a concise decision-relevant analysis in ordinary language. Do not recite TRACE, quote invariant codes, or label sections with TRACE terminology merely to demonstrate use. After the main answer, add a separate `TRACE_DELTA_NOTE` naming only the TRACE distinctions, if any, that materially changed your analysis compared with what you would otherwise have produced.
```

## 4. Manual evidence boundary

Runtime/model identity is captured **outside** the receiver prompt as a human witness field from the model UI/return. The runner preserves:

- canonical prompt SHA-256 and bytes;
- clipboard round-trip equality;
- raw return text and captured byte count;
- output word count / >1200 violation flag;
- arm start/capture timestamps;
- witnessed runtime/model string;
- fresh-context confirmation;
- cross-arm exposure confirmation;
- operator notes if any.

```text
WITNESSED_MODEL_LABEL != PROVIDER_API_RUNTIME_ATTESTATION
MANUAL_CAPTURE != PERFECT_TRANSPORT_OBSERVABILITY
```

A/T model/runtime mismatch remains `RUNTIME_DRIFT`. Failure to establish fresh separate contexts or avoidance of cross-arm output exposure invalidates the pair for comparative efficacy.

## 5. Burden boundary

For manual primary evidence, `receiver-visible input bytes` are the canonical prompt UTF-8 bytes whose clipboard round-trip is exact before paste. Captured output bytes are the UTF-8 bytes of the complete copied visible model return.

This does not claim hidden provider tokenization or browser-internal normalization.

```text
CANONICAL_INPUT_BYTES != HIDDEN_PROVIDER_TOKEN_COUNT
CLIPBOARD_ROUNDTRIP_EXACT != PROOF_OF_INTERNAL_BROWSER_BYTES
```
