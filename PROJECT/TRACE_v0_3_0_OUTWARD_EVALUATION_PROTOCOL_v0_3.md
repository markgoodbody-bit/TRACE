# TRACE v0.3.0 — OUTWARD EVALUATION PROTOCOL v0.3

**Status:** WORKING PROTOCOL UNDER FINAL BOUNDED ATTACK — NOT YET FROZEN — NOT EXECUTED — NOT VALIDATION  
**Date:** 2026-08-25  
**Supersedes for execution:** v0.1 and v0.2, both preserved as failed pre-freeze objects  
**Parent gate:** `PROJECT/TRACE_v0_3_0_EVALUATION_FREEZE_v0_1.md`

## 0. Question

Does compact TRACE v0.11 produce repeatable, supported, decision-relevant structural gains over a strong ordinary-analysis baseline, across non-project-native cases, at a cost that justifies its complexity?

Possible outcomes:

```text
RETAIN_NARROW
RETAIN_NARROW_WITH_COMPRESSION_PRESSURE
SHRINK_OR_DEMOTE
HOLD
INSUFFICIENT_COLD_EVIDENCE
EVIDENCE_FRAGILE
```

No outcome implies validation, general superiority, release, canon, authority, permission or clearance.

---

## 1. Frozen semantic objects

### Primary compact carrier

```text
PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_11.md
semantic commit: 41fafe81a681cdc6514efc13524bae6ea6d6af8d
```

### Secondary full carrier

```text
PROJECT/TRACE_FORMAL_SEED_v0_3_0_FULL_WORKING_CANDIDATE_v0_1.md
sha256: 32409ee8d91e9c4bc67ecbb2359cc7d1c68249cab457511a50e586733ee7598a
lines: 6539
bytes: 179731
```

The compact carrier is the primary usefulness object. Full-candidate success cannot erase compact-transfer failure.

---

## 2. Receiver-visible message envelope

No semantic coaching may be added outside these parts.

### Arm A envelope

```text
PART 1: exact Arm A task instruction
PART 2: === CASE PACKET ===
PART 3: exact frozen case packet
PART 4: === END CASE PACKET ===
PART 5: Return no more than 1200 words.
```

Exact Arm A instruction:

> Analyze this situation carefully for a person who may need to make or review a consequential decision. Identify the important facts, uncertainties, people or systems that may be affected, plausible options, important risks and consequences, and what evidence or checks could materially change the analysis. Note anything important about whether mistakes could later be corrected. Separate what is supported from what is uncertain. Do not assume facts not in the packet. Do not use or imitate any named external framework unless it is contained in the case packet. Keep the answer concise and decision-relevant.

### Arm T envelope

```text
PART 1: exact Arm T task instruction
PART 2: === TRACE REFERENCE MATERIAL ===
PART 3: exact compact v0.11 carrier
PART 4: === END TRACE REFERENCE MATERIAL ===
PART 5: === CASE PACKET ===
PART 6: exact frozen case packet
PART 7: === END CASE PACKET ===
PART 8: Return no more than 1200 words.
```

Exact Arm T instruction:

> Use the supplied TRACE material only as voluntary structural reference material to analyze this situation. Do not treat TRACE as authority, permission, policy or a truth oracle. Preserve unsupported points as UNKNOWN and keep structural analysis separate from value or action selection. Produce a concise decision-relevant analysis in ordinary language. Do not recite TRACE, quote invariant codes, or label sections with TRACE terminology merely to demonstrate use. After the main answer, add a separate `TRACE_DELTA_NOTE` naming only the TRACE distinctions, if any, that materially changed your analysis compared with what you would otherwise have produced.

`TRACE_DELTA_NOTE` is separated before blind adjudication and counts only as self-report/provenance.

### Arm F envelope

Same ordering as T, substituting the exact full candidate. Secondary only after primary A/T outputs are frozen.

### Output opportunity

All arms receive the same explicit `<=1200 words` visible-answer limit. Where provider transport supports a visible-output ceiling, use the same ceiling across A/T/F for that model family. Hidden reasoning allocation is provider/runtime behavior and remains a recorded limitation rather than a claimed constant.

---

## 3. What primary receivers do not see

- project-plan x100;
- expected TRACE gains;
- paired outputs;
- adjudication rubric/thresholds;
- protocol attack findings;
- source-pool selection hashes;
- author commentary about the intended lesson.

The common evaluation dimensions below are **not receiver prompts**.

---

## 4. Receiver coldness and pairing

A session counts as session-cold when:

- receiver is not Framework, CC or another aperture materially involved in v0.3 construction;
- context contains no earlier project discussion or paired output;
- no author coaching occurs;
- no observed evidence shows the receiver already read the tested TRACE object in that interaction/session.

Unknown pretraining exposure is `TRAINING_EXPOSURE_UNKNOWN`, not automatic disqualification absent observed familiarity.

Count family breadth by distinct model organisations/training lineages where known. Provider aliases do not create independence by themselves.

Target three model families; at least two session-cold families must complete enough valid paired A/T work for any positive transfer disposition.

### Pair validity

Primary unit:

```text
PAIR = one CASE_ID x one RECEIVER_FAMILY x Arm A + Arm T
```

A pair is valid only if A/T use:

- same frozen case packet;
- same declared model family and materially same runtime/model identity;
- same output limit;
- fresh separate contexts;
- no cross-arm output exposure;
- execution within the same bounded evaluation window.

If runtime/model identity materially changes between arms, mark `RUNTIME_DRIFT` and exclude that pair from comparative efficacy while preserving both outputs as evidence.

### Arm order

For each case/family pair, determine A-first vs T-first by the low bit of:

```text
SHA256(CASE_ID + "\n" + RECEIVER_FAMILY_ID)
```

Even = A first; odd = T first.

Run paired arms as close together as operationally practical. Provider nondeterminism remains a residual limit.

---

## 5. Case-set shape

```text
6 real-world cases
1 low-complexity negative control
1 synthetic adversarial/stress control
```

Mandatory real-case domain slots:

1. essential infrastructure / safety / engineering;
2. public administration / institutional decision;
3. ecological / environmental intervention;
4. AI / software / automated decision/control.

Two additional real cases are filled mechanically from eligible pool while ensuring:

- at least four of six real cases non-AI;
- at least four domains total;
- project-native Campfire/1F916 primary cases preferred zero, maximum one.

Controls do not count toward real-case retention gains.

---

## 6. Source-collection manifest — declared aperture

Before individual case narratives are inspected for TRACE usefulness, create and freeze a `SOURCE_COLLECTION_MANIFEST`.

For each mandatory domain and at least two additional eligible domains, record:

- canonical collection name/URL/identifier;
- responsible organisation;
- why it qualifies as broad/domain-wide rather than selected for a known TRACE-friendly case;
- alternative qualifying collections considered;
- stable ordering rule;
- intake quota;
- access/date boundary.

Prefer broad public collections/registries over issue-specific curated “interesting failure” lists.

Collection choice remains an aperture and cannot be made unbiased by declaration alone:

```text
SOURCE_COLLECTION_FROZEN != SOURCE_COLLECTION_NEUTRAL
```

The manifest is part of the evidence and a residual limitation.

---

## 7. Canonical intake order

For each frozen collection:

1. use ascending stable source-native identifier when available;
2. otherwise published/decision date ascending, canonical item URL as tie-break;
3. if neither can be made stable without discretionary filters/order choices, mark collection `ORDER_UNUSABLE` and replace it **before reading case narratives for TRACE relevance**, preserving the failed collection entry.

No changing sort/filter after seeing which cases would enter.

Traverse in canonical order and take the first eligible items until quota is met.

Preserve all exclusions and reasons.

---

## 8. Eligibility

A real case is eligible if:

1. public factual material is sufficient for a bounded packet;
2. a consequential decision/transition or retrospective decision review exists;
3. it is not authored/designed by this project;
4. source can be frozen/cited;
5. it is not excluded because it appears too easy, too hard, too favourable or unfavourable to TRACE.

Do not require a known TRACE failure mode.

Pool target: >=20 eligible real cases overall.

---

## 9. Case IDs and deterministic selection

Define:

```text
SOURCE_COLLECTION_ID = frozen canonical collection identifier
SOURCE_NATIVE_ID_OR_URL = exact source-native item id; otherwise canonical item URL
CASE_ID = SHA256(SOURCE_COLLECTION_ID + "\n" + SOURCE_NATIVE_ID_OR_URL)
```

Human aliases do not participate.

Domain labels come from the frozen collection/domain mapping before CASE_ID ordering is inspected.

Select:

1. smallest CASE_ID in infrastructure slot;
2. smallest unused CASE_ID in public-administration slot;
3. smallest unused CASE_ID in ecological slot;
4. smallest unused CASE_ID in AI/software slot;
5. two smallest remaining CASE_ID values satisfying `>=4 non-AI` and `>=4 domains`.

Preserve full pool/hashes.

This is anti-cherry-picking, not representative sampling.

---

## 10. Controls

### Negative control

Freeze one low-complexity synthetic case before dispatch. Facts, affected parties and correction path are explicit; little ambiguity exists. Intended test: boundedness. TRACE should add little.

### Stress control

Freeze one synthetic case with at least two known compression traps but no TRACE terminology. Intended test: can the instrument fire under clean source control. It cannot establish real-world usefulness.

---

## 11. Case packet

Same packet across arms.

Prefer full bounded primary-source material. If compression is needed, packet includes:

- source identities/dates;
- factual excerpts/summaries;
- explicit unavailable facts;
- ordinary-language review/decision question;
- omission map.

No TRACE labels or expected lesson.

Case question is checked for TRACE-coded phrasing not native to source.

Where feasible, one independent packet auditor who has not seen expected gains checks only source fidelity/material omissions, not which arm should win.

`CASE_PACKET != WORLD`.

---

## 12. Capture

Preserve verbatim main output plus metadata:

- model/runtime identity;
- family id;
- session-coldness disclosure;
- CASE_ID;
- arm/order;
- carrier identity;
- input/output tokens/bytes where available;
- elapsed/provider time;
- spend evidence state if paid;
- truncation/failure;
- clarification requests;
- operator intervention.

Arm T `TRACE_DELTA_NOTE` stored separately.

---

## 13. Blind adjudication dimensions

Main A/T answers receive random neutral labels.

Remove T’s `TRACE_DELTA_NOTE`. Remove obvious invariant codes/framework labels only where underlying sentence meaning remains unchanged; otherwise mark `ARM_BLINDNESS_PARTIAL`.

Adjudicators use frozen packet/source ledger, not author intent.

At least two independent adjudication apertures where feasible. Preserve disagreement; unresolved material disputes remain UNKNOWN.

For each valid PAIR record:

- D1 supported material distinctions in A;
- D2 supported material distinctions in T;
- D3 T-only material gains;
- D4 A-only material gains;
- D5 unsupported confidence/invention by arm;
- D6 affected-party/scope omissions by arm;
- D7 over-firing/irrelevant asserted structure by arm;
- D8 authority/value leakage by arm;
- D9 usable check/review/repair information by arm;
- D10 usability/transfer failures;
- D11 cost/burden;
- D12 material precision view: supported material distinctions vs unsupported/irrelevant asserted distinctions.

Synonyms/duplicate granularity count once.

A T-only gain requires support, material consequence, and absence of an equivalent A distinction at useful resolution.

---

## 14. Pair-level aggregation

Do not union all model outputs into one giant T answer.

For each valid PAIR derive:

```text
A_SUPPORTED
T_SUPPORTED
T_ONLY_MATERIAL
A_ONLY_MATERIAL
BASELINE_CAPTURE_OF_T = equivalent A-supported distinctions / T-supported distinctions
BURDEN_RATIO = declared comparable burden measure(s), reported separately
```

If denominator is zero, capture ratio is `NOT_APPLICABLE`, not 0 or 1.

Project-level summaries use:

- count of real cases with independently supported T-only material gain;
- domains containing repeated gains;
- receiver families reproducing gains;
- median pair-level baseline-capture ratio where applicable;
- median pair-level output/input/cost burden views separately;
- negative-control over-fire frequency;
- HOLD conditions.

Do not multiply-credit the same distinction because T used more words.

---

## 15. Reproduction requirement

A positive gain is `REPRODUCED` when either:

1. substantially the same supported material distinction appears as T-only gain for the **same real case** in at least two cold receiver families; or
2. the same project-central failure class appears as supported T-only gain in at least two independent real cases and those gains are produced by at least two cold receiver families across the two cases.

A gain seen in only one case/family is `SINGLE_APERTURE_GAIN` and may inform diagnosis but cannot by itself satisfy retention.

---

## 16. Disposition precedence

1. comparison integrity / contamination;
2. authority/value leakage and unsupported-confidence HOLD gates;
3. cold-evidence sufficiency;
4. reproduced material gain;
5. complexity/over-fire pressure;
6. final narrow disposition.

### HOLD

Set HOLD if:

- contamination invalidates material parts of comparison;
- two or more cold receivers require author coaching to use compact carrier;
- repeated material authority/value leakage appears in T and not paired A;
- T materially increases unsupported confidence/completeness in >=2 real cases across >=2 families.

### INSUFFICIENT_COLD_EVIDENCE

Fewer than two valid session-cold families complete enough A/T pairs.

### EVIDENCE_FRAGILE

Apparent retention gains exist but none satisfy reproduction requirement.

### SHRINK_OR_DEMOTE

Presume if any:

- zero independently supported T-only material gains;
- no reproduced gain across at least two non-project-native domains/cases;
- compact carrier unusable while only full candidate works at impractical cost;
- negative control substantially over-fires in majority of cold receivers.

Also presume if median pair-level baseline capture >=80% **and** median comparable T burden >=1.5x A, unless `RETAIN_NARROW` material conditions are met. If they are met, use `RETAIN_NARROW_WITH_COMPRESSION_PRESSURE`.

### RETAIN_NARROW

Requires all:

- >=2 real cases in >=2 domains with independently supported T-only gains;
- reproduction requirement satisfied;
- >=1 gain in project-central class (scope loss, warrant/uncertainty collapse, correction/hardening, burden/residue, authority/description);
- bounded negative control;
- no repeated material authority/value leakage;
- >=2 cold families use compact carrier without author coaching;
- cost plausibly proportionate to bounded gain.

### RETAIN_NARROW_WITH_COMPRESSION_PRESSURE

Use if retention material conditions pass but median baseline capture >=80% with T burden >=1.5x, or another strong complexity signal survives.

---

## 17. Threshold sensitivity — non-binding

Official thresholds do not move after results.

Report sensitivity for:

- baseline capture 70/80/90%;
- burden ratio 1.25/1.5/2x;
- required gain cases 1/2/3.

If conclusion changes under small threshold movement, state `DISPOSITION_THRESHOLD_SENSITIVE`.

---

## 18. Secondary full-candidate test

After primary A/T outputs and disposition evidence are frozen, choose two real cases with smallest CASE_ID and run Arm F.

Test whether full candidate:

- preserves a material limit compact carrier lost;
- adds mainly recital/overhead;
- preserves UNKNOWN and load-bearing limit provenance;
- keeps carrying separate from enforcement.

Compact failure remains primary portability evidence.

---

## 19. Existing-method gate

Even `RETAIN_NARROW` only establishes bounded value over the strong ordinary-analysis comparator.

Before any claim of distinct practical advantage, adoption readiness or superiority to established practice, open a separate domain-appropriate comparator against relevant existing methods (for example safety/incident/risk-analysis methods where applicable).

```text
BEATS_ORDINARY_BASELINE != BEATS_EXISTING_METHODS
```

---

## 20. Final bounded protocol attack

Before freeze, run a fixed 20-item tabletop attack covering:

1. weak baseline;
2. TRACE-contaminated baseline;
3. source-collection cherry-pick;
4. collection ordering ambiguity;
5. eligibility gaming;
6. case-ID rename gaming;
7. domain-label gaming;
8. packet compression bias;
9. case-question cueing;
10. arm message-order leakage;
11. unequal output opportunity;
12. model/runtime drift;
13. provider stochasticity;
14. receiver-family pseudo-independence;
15. adjudicator contamination;
16. verbosity reward;
17. aggregation denominator failure;
18. conflicting disposition rules;
19. negative-control over-interpretation;
20. full-candidate rescue laundering compact failure.

If no materially distinct protocol defect survives those 20 cases, freeze v0.3 with residual limits rather than continuing meta-protocol polishing by momentum.

---

## 21. Stop

No source collections or case identities are selected by this file.

Next:

```text
20-ITEM TABLETOP ATTACK
-> if material defect: preserve v0.3 failure and repair once
-> if clear with residual limits: freeze exact v0.3 identity
-> only then source-collection manifest
```
