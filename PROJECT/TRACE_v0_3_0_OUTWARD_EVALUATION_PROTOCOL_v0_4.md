# TRACE v0.3.0 — OUTWARD EVALUATION PROTOCOL v0.4

**Status:** FINAL WORKING PROTOCOL UNDER FIXED 20-CASE ATTACK — NOT YET FROZEN — NOT EXECUTED — NOT VALIDATION  
**Date:** 2026-08-25  
**Supersedes for execution:** v0.1-v0.3, preserved as pre-freeze ancestry  
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

## 1. Semantic objects

Primary compact carrier:

```text
PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_11.md
semantic commit: 41fafe81a681cdc6514efc13524bae6ea6d6af8d
```

Secondary full carrier:

```text
PROJECT/TRACE_FORMAL_SEED_v0_3_0_FULL_WORKING_CANDIDATE_v0_1.md
sha256: 32409ee8d91e9c4bc67ecbb2359cc7d1c68249cab457511a50e586733ee7598a
lines: 6539
bytes: 179731
```

Primary usefulness is judged on the compact carrier. Full-candidate success cannot erase compact-transfer failure.

---

## 2. Exact receiver-visible envelopes

No semantic coaching may be added outside these parts.

### Arm A

```text
PART 1: exact Arm A instruction
PART 2: === CASE PACKET ===
PART 3: exact frozen case packet
PART 4: === END CASE PACKET ===
PART 5: Return no more than 1200 words.
```

Exact Arm A instruction:

> Analyze this situation carefully for a person who may need to make or review a consequential decision. Identify the important facts, uncertainties, people or systems that may be affected, plausible options, important risks and consequences, and what evidence or checks could materially change the analysis. Note anything important about whether mistakes could later be corrected. Separate what is supported from what is uncertain. Do not assume facts not in the packet. Do not use or imitate any named external framework unless it is contained in the case packet. Keep the answer concise and decision-relevant.

### Arm T

```text
PART 1: exact Arm T instruction
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

The `TRACE_DELTA_NOTE` is stored separately before blind adjudication and is self-report/provenance only.

### Arm F

Same as T, substituting exact full candidate. Secondary only after primary outputs are frozen.

### Output opportunity

All arms receive the same `<=1200 words` visible-answer limit. Use the same provider visible-output ceiling within a model family where transport supports it. Hidden reasoning is not claimed constant.

---

## 3. What primary receivers do not see

- project-plan x100;
- expected TRACE gains;
- paired outputs;
- adjudication thresholds/dimensions;
- protocol attacks;
- case hashes;
- author commentary about intended lessons.

Common evaluation dimensions are post-hoc only.

---

## 4. Receiver coldness and valid pairs

Session-cold requires:

- not Framework, CC or another aperture materially involved in v0.3 construction;
- fresh context without earlier project discussion or paired output;
- no author coaching;
- no observed evidence receiver already read the tested object in that session.

Unknown pretraining exposure is `TRAINING_EXPOSURE_UNKNOWN`, not automatic disqualification absent observed familiarity.

Count families by distinct model organisations/training lineages where known. Provider aliases alone do not create independence.

Target three cold families; at least two must complete enough valid pairs for any positive transfer disposition.

Primary unit:

```text
PAIR = CASE_ID x RECEIVER_FAMILY_ID x Arm A + Arm T
```

Valid pair requires same case packet, same materially identical model/runtime identity, same visible-output limit, fresh separate contexts, no cross-arm exposure and same bounded evaluation window.

Material runtime identity change => `RUNTIME_DRIFT`; preserve outputs but exclude pair from comparative efficacy.

Arm order:

```text
ORDER_HASH = SHA256(CASE_ID + "\n" + RECEIVER_FAMILY_ID)
low bit 0 -> A first
low bit 1 -> T first
```

Execute paired arms as close in time as operationally practical. Provider stochasticity remains a residual limit.

---

## 5. Case-set shape

```text
6 real-world cases
1 low-complexity negative control
1 synthetic adversarial/stress control
```

Mandatory real-case slots:

1. essential infrastructure / safety / engineering;
2. public administration / institutional decision;
3. ecological / environmental intervention;
4. AI / software / automated decision/control.

Two additional real cases filled mechanically while ensuring >=4 non-AI, >=4 domains, and preferably zero project-native cases (maximum one).

Controls never count as real-world retention gains.

---

## 6. Source-collection manifest

Before individual case narratives are inspected for TRACE usefulness, freeze a `SOURCE_COLLECTION_MANIFEST` containing for each mandatory domain and at least two additional eligible domains:

- canonical collection name/URL/identifier;
- responsible organisation;
- why it is broad/domain-wide rather than selected for a known TRACE-friendly case;
- alternative qualifying collections considered;
- canonical stable ordering rule;
- intake quota;
- access/date boundary.

Prefer broad public collections/registries over curated “interesting failure” lists.

The manifest itself must be committed/frozen and attacked for obvious TRACE-favourability **before item-level intake**. If a material collection-selection defect is found, preserve the failed manifest and repair before case reading.

```text
SOURCE_COLLECTION_FROZEN != SOURCE_COLLECTION_NEUTRAL
```

Collection choice remains an explicit study aperture/residual limitation.

---

## 7. Canonical collection order and eligibility intake

Order:

1. ascending stable source-native identifier where available;
2. otherwise published/decision date ascending with canonical item URL tie-break;
3. otherwise collection is `ORDER_UNUSABLE` and must be replaced before item-level TRACE-relevance reading.

No sort/filter change after seeing which cases would enter.

Eligibility:

1. sufficient public facts for bounded packet;
2. consequential decision/transition or retrospective decision review;
3. not project-authored/designed;
4. source can be frozen/cited;
5. not excluded for being too easy/hard/favourable/unfavourable to TRACE.

Preserve ineligible items and exact exclusion reason.

Pool target >=20 eligible real cases overall.

---

## 8. Case IDs and selection

```text
SOURCE_COLLECTION_ID = frozen canonical collection identifier
SOURCE_NATIVE_ID_OR_URL = exact source-native id; otherwise canonical item URL
CASE_ID = SHA256(SOURCE_COLLECTION_ID + "\n" + SOURCE_NATIVE_ID_OR_URL)
```

Human aliases do not participate. Domain mapping is frozen before hashes are inspected.

Select smallest CASE_ID for mandatory slots 1-4, then two smallest remaining IDs satisfying >=4 non-AI and >=4 domains.

Preserve full pool/hashes.

`DETERMINISTIC_SELECTION != REPRESENTATIVE_SAMPLE_OF_WORLD`.

---

## 9. Controls

Negative control: one low-complexity synthetic case with explicit facts/affected parties/correction path. Intended test is boundedness; TRACE should add little.

Stress control: one synthetic case with at least two known compression traps but no TRACE terminology. It tests firing under source control, not real-world usefulness.

Freeze both before receiver dispatch.

---

## 10. Case packet

Same frozen packet across arms.

Prefer full bounded primary-source material. If compressed, include source identities/dates, factual material, explicit unavailable facts, ordinary-language question and omission map.

No TRACE labels or expected lesson. Check question for TRACE-coded cueing not native to source.

Where feasible, independent packet auditor who has not seen expected gains checks source fidelity/material omissions only.

`CASE_PACKET != WORLD`.

---

## 11. Capture and primary burden

Preserve verbatim main output plus model/runtime/family, coldness, CASE_ID, arm/order, carrier identity, input/output token/byte evidence, elapsed/provider time, spend evidence state, truncation/failure, clarifications and operator intervention.

Store `TRACE_DELTA_NOTE` separately.

### Primary deterministic burden measure

For each arm:

```text
PRIMARY_BURDEN_BYTES = UTF8_BYTES(receiver-visible input message)
                     + UTF8_BYTES(receiver-visible full output)
```

For T, the requested `TRACE_DELTA_NOTE` counts in burden even though removed from blind efficacy adjudication.

Pair-level:

```text
PRIMARY_BURDEN_RATIO = T_PRIMARY_BURDEN_BYTES / A_PRIMARY_BURDEN_BYTES
```

This is a crude deterministic transport/reading-volume proxy, **not cognitive-cost truth**. Report provider tokens, elapsed time, monetary evidence, output words and adjudication burden separately. Do not substitute another burden view into the predeclared 1.5x threshold.

---

## 12. Blind adjudication

Main A/T answers receive random neutral labels. Remove T `TRACE_DELTA_NOTE`. Remove obvious invariant codes/framework labels only if underlying ordinary-language meaning remains unchanged; otherwise mark `ARM_BLINDNESS_PARTIAL`.

Adjudicators use frozen case/source evidence, not author intent.

### Positive-gain confirmation rule

A candidate T-only material gain may be recorded descriptively after one adjudicator, but it counts toward retention/reproduction only as `CONFIRMED_GAIN` if:

- **two adjudication apertures** independently find it supported and materially consequential; and
- at least one adjudicator is from a different model family/organisation than the receiver that produced the candidate gain where available.

If only one adjudicator supports it, or the two materially disagree, record `UNCONFIRMED_GAIN` / `GAIN_DISPUTED`. It cannot satisfy positive retention.

If two independent adjudication apertures cannot be obtained for enough candidate gains, positive disposition becomes `INSUFFICIENT_ADJUDICATION_EVIDENCE` (reported under HOLD/insufficient evidence), not PASS.

Mark retains project/release authority but is not counted as independent efficacy adjudication.

---

## 13. Pair-level dimensions

For every valid pair preserve separately:

- supported material distinctions A/T;
- confirmed/unconfirmed T-only gains;
- A-only gains;
- unsupported confidence/invention;
- affected-party/scope omission;
- over-firing/irrelevant asserted distinctions;
- authority/value leakage;
- usable check/review/repair information;
- usability/transfer failures;
- primary burden bytes/ratio and secondary cost views;
- material precision: supported material distinctions vs unsupported/irrelevant asserted distinctions.

Synonyms/duplicate granularity count once.

Pair-level baseline capture:

```text
BASELINE_CAPTURE_OF_T = equivalent A-supported distinctions / T-supported distinctions
```

If T-supported denominator is zero, `NOT_APPLICABLE`.

Do not union all receiver outputs into one giant T answer.

---

## 14. Predeclared reproduction classes

Every confirmed gain may be assigned one or more classes:

```text
R_SCOPE       affected-party/scope discovery or aggregation loss
R_WARRANT     evidence/warrant/currentness/verification-status collapse
R_CORRECTION  route/review/rollback/hardening/repair-window failure
R_BURDEN      burden/residue/loss survival
R_AUTHORITY   capability/description/authority/permission confusion
R_OTHER       other
```

Cross-case reproduction under `R_OTHER` requires the same specifically described mechanism; the generic bucket cannot establish reproduction.

A broad class label alone is insufficient. Adjudicators must state the concrete common mechanism.

A gain is `REPRODUCED` if either:

1. substantially same confirmed gain appears for same real case in >=2 cold receiver families; or
2. same predeclared class **and concrete mechanism** appears as confirmed gain in >=2 independent real cases, with gains produced across >=2 cold receiver families.

One case/family only => `SINGLE_APERTURE_GAIN`.

---

## 15. Aggregation

Project summary uses valid pair-level evidence:

- real cases with confirmed T-only gains;
- domains/gain classes with reproduced gains;
- cold families reproducing gains;
- median pair-level baseline-capture ratio where applicable;
- median `PRIMARY_BURDEN_RATIO`;
- secondary token/time/cost views;
- negative-control over-fire frequency;
- HOLD/insufficiency gates.

No extra credit for verbosity.

---

## 16. Disposition precedence

1. comparison integrity/contamination;
2. authority/value leakage + unsupported-confidence HOLD;
3. cold receiver + adjudication sufficiency;
4. confirmed/reproduced material gain;
5. complexity/over-fire pressure;
6. final narrow disposition.

### HOLD / insufficient evidence

HOLD or insufficient-evidence disposition if:

- contamination invalidates material comparison;
- >=2 cold receivers require author coaching to use compact carrier;
- repeated material T authority/value leakage absent from paired A;
- T materially increases unsupported confidence/completeness in >=2 real cases across >=2 families;
- fewer than two session-cold families complete enough valid pairs;
- insufficient independent adjudication exists to confirm candidate positive gains.

HOLD does not imply repair; consider removal/shrink first.

### EVIDENCE_FRAGILE

Confirmed gains exist but reproduction rule is not satisfied.

### SHRINK_OR_DEMOTE

Presume if:

- zero confirmed T-only material gains; or
- no reproduced gain across at least two non-project-native cases/domains; or
- compact carrier unusable while only full carrier works at impractical cost; or
- negative control substantially over-fires in majority of cold receivers.

Also presume when median pair-level baseline capture >=80% and median `PRIMARY_BURDEN_RATIO >= 1.5`, unless all RETAIN_NARROW material conditions pass. If they pass, outcome is `RETAIN_NARROW_WITH_COMPRESSION_PRESSURE`.

### RETAIN_NARROW

Requires all:

- >=2 real cases in >=2 domains with confirmed T-only gains;
- reproduction rule satisfied;
- >=1 reproduced gain in R_SCOPE/R_WARRANT/R_CORRECTION/R_BURDEN/R_AUTHORITY;
- bounded negative control;
- no repeated material authority/value leakage;
- >=2 cold families use compact carrier without author coaching;
- independent adjudication sufficient;
- observed cost plausibly proportionate to bounded gain.

### RETAIN_NARROW_WITH_COMPRESSION_PRESSURE

Use when retention material conditions pass but median baseline capture >=80% and median primary burden ratio >=1.5, or another strong complexity signal survives.

No retention means validation/release/canon.

---

## 17. Non-binding sensitivity report

Official thresholds do not move after results.

Report alternative views for baseline capture 70/80/90%, primary burden 1.25/1.5/2x and real-case gain count 1/2/3.

If small threshold changes flip disposition, state `DISPOSITION_THRESHOLD_SENSITIVE`.

---

## 18. Secondary full-candidate test

After primary A/T outputs/disposition evidence are frozen, choose two real cases with smallest CASE_ID and run Arm F.

Test material limit survival, UNKNOWN/provenance, recital/overhead, and carrying-vs-enforcement.

Compact failure remains primary portability evidence.

---

## 19. Existing-method gate

A retain result only establishes bounded value over ordinary careful analysis. Before claims of distinct practical advantage/adoption readiness, run a separate domain-appropriate comparator against relevant established methods.

```text
BEATS_ORDINARY_BASELINE != BEATS_EXISTING_METHODS
```

---

## 20. Fixed final protocol attack

Before freeze, replay exactly these 20 confounds:

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
15. adjudicator contamination/insufficiency;
16. verbosity/reward leakage;
17. aggregation denominator failure;
18. conflicting disposition rules;
19. negative-control over-interpretation;
20. full-candidate rescue laundering compact failure.

If no materially distinct protocol defect survives, freeze v0.4 with residual limits and stop meta-protocol polishing.

---

## 21. Stop

No source collection or case identity is selected by this object.

Next only after successful fixed attack:

```text
freeze exact v0.4 identity
-> build/freeze/attack SOURCE_COLLECTION_MANIFEST
-> only then item-level intake and case selection
```
