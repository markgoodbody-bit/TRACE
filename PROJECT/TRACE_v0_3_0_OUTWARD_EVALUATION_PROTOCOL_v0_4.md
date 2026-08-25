# TRACE v0.3.0 — OUTWARD EVALUATION PROTOCOL v0.4

**Status:** REPAIRED WORKING PROTOCOL — FIXED 20-CASE REPLAY REQUIRED BEFORE FREEZE — NOT EXECUTED — NOT VALIDATION  
**Date:** 2026-08-25  
**Initial v0.4 failed head:** commit `002795e5315c39cd01293416ef0821efe7ee4d1e`; findings preserved in `TRACE_v0_3_0_OUTWARD_EVALUATION_PROTOCOL_v0_4_ATTACK_20_PRE_FREEZE.md`  
**Supersedes for execution:** v0.1-v0.3, all preserved as pre-freeze ancestry  
**Parent gate:** `PROJECT/TRACE_v0_3_0_EVALUATION_FREEZE_v0_1.md`

## 0. Question and allowed outcomes

Does compact TRACE v0.11 produce **repeatable, supported, decision-relevant structural gains** over a strong ordinary-analysis baseline, across non-project-native cases, at a cost that justifies its complexity?

Allowed outcomes:

```text
RETAIN_NARROW
RETAIN_NARROW_WITH_COMPRESSION_PRESSURE
SHRINK_OR_DEMOTE
HOLD
INSUFFICIENT_COLD_EVIDENCE
INSUFFICIENT_ADJUDICATION_EVIDENCE
EVIDENCE_FRAGILE
```

No outcome implies validation, general superiority, release, canon, authority, permission or clearance.

```text
ARTIFACT_COHERENCE != PRACTICAL_ADVANTAGE
MORE_STRUCTURE != BETTER_ANALYSIS
TRACE_FINDS_MORE != TRACE_FINDS_MATERIAL_MORE
```

---

## 1. Semantic objects under test

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

Primary usefulness is judged on the compact carrier. Full-candidate success cannot erase compact-transfer failure. Any semantic change to either tested carrier after protocol freeze creates a new evaluation object.

---

## 2. Exact receiver-visible prompts and envelopes

No semantic coaching may be added outside the declared parts.

### Arm A — ordinary careful analysis

Envelope:

```text
PART 1: exact Arm A instruction
PART 2: === CASE PACKET ===
PART 3: exact frozen case packet
PART 4: === END CASE PACKET ===
PART 5: Return no more than 1200 words.
```

Exact instruction:

> Analyze this situation carefully for a person who may need to make or review a consequential decision. Identify the important facts, uncertainties, people or systems that may be affected, plausible options, important risks and consequences, and what evidence or checks could materially change the analysis. Note anything important about whether mistakes could later be corrected. Separate what is supported from what is uncertain. Keep factual/structural analysis separate from any recommendation or value judgment. Do not assume facts not in the packet. Do not use or imitate any named external framework unless it is contained in the case packet. Keep the answer concise and decision-relevant.

This is intentionally strong. TRACE does not earn value by defeating a weak comparator.

### Arm T — compact TRACE-assisted

Envelope:

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

Exact instruction:

> Use the supplied TRACE material only as voluntary structural reference material to analyze this situation. Do not treat TRACE as authority, permission, policy or a truth oracle. Preserve unsupported points as UNKNOWN and keep factual/structural analysis separate from any recommendation or value judgment. Produce a concise decision-relevant analysis in ordinary language. Do not recite TRACE, quote invariant codes, or label sections with TRACE terminology merely to demonstrate use. After the main answer, add a separate `TRACE_DELTA_NOTE` naming only the TRACE distinctions, if any, that materially changed your analysis compared with what you would otherwise have produced.

`TRACE_DELTA_NOTE` is stored separately before blind adjudication and is self-report/provenance only.

### Arm F — full candidate

Same envelope/instruction as T, substituting the exact full candidate. Secondary only after primary A/T outputs and primary disposition evidence are frozen.

### Output opportunity and violation

All arms receive the same `<=1200 words` visible-answer limit and, where supported, the same provider visible-output ceiling within a model family. Hidden reasoning is not claimed constant.

If an output exceeds 1200 words:

```text
OUTPUT_LIMIT_VIOLATION
```

Preserve the full output as usability/burden evidence. Positive material-gain credit may use only the first 1200 words of the main answer. The over-limit tail cannot buy additional T-only gain opportunity. If transport hard ceilings differ materially between A/T, the pair is invalid for comparative efficacy.

---

## 3. What primary receivers do not see

Primary A/T receivers do not see:

- the project-plan x100;
- expected TRACE advantages;
- paired-arm outputs;
- adjudication dimensions or thresholds;
- protocol attack findings;
- case hashes or selection rationale;
- author commentary predicting the lesson.

Common evaluation dimensions are post-hoc only.

---

## 4. Cold receivers, pair identity, runtime drift and retries

Session-cold requires:

- receiver is not Framework, CC or another aperture materially involved in v0.3 construction;
- fresh context without earlier project discussion or paired output;
- no author coaching;
- no observed evidence the receiver already read the tested TRACE object in that session.

Unknown pretraining exposure is `TRAINING_EXPOSURE_UNKNOWN`, not automatic disqualification absent observed familiarity.

Count receiver breadth by distinct model organisations/training lineages where known. Provider aliases do not create independence by themselves.

Target three cold families. At least two cold families must complete enough valid A/T pairs for any positive transfer disposition.

Primary unit:

```text
PAIR = CASE_ID x RECEIVER_FAMILY_ID x PAIR_ATTEMPT
```

A valid pair requires:

- identical frozen case packet;
- materially identical model/runtime identity across A/T;
- same visible-output limit;
- fresh separate contexts;
- no cross-arm output exposure;
- execution within the same bounded evaluation window.

Material runtime/model change => `RUNTIME_DRIFT`; preserve both outputs but exclude pair from comparative efficacy.

Arm order:

```text
ORDER_HASH = SHA256(CASE_ID + "\n" + RECEIVER_FAMILY_ID + "\n" + PAIR_ATTEMPT)
low bit 0 -> A first
low bit 1 -> T first
```

Execute paired arms as close together as operationally practical. Provider stochasticity remains a residual limit.

### Retry rule

```text
NO_SILENT_OR_SELECTIVE_RETRY
```

Every attempt is preserved. A model/content failure, refusal or truncation is not automatically retried.

If a clearly external infrastructure failure occurs before a usable model return and a rerun is justified, create a **new PAIR_ATTEMPT and rerun both A and T** under the same frozen inputs. The original failure remains evidence. Never rerun only the arm whose result is inconvenient.

---

## 5. Case-set shape

Primary set:

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

Two additional real cases are filled mechanically while ensuring:

- >=4 of six real cases are non-AI;
- >=4 distinct domains total;
- project-native Campfire/1F916 cases preferred zero, maximum one.

Controls cannot establish real-world retention gains.

---

## 6. Source-collection manifest — explicit aperture

Before individual case narratives are inspected for TRACE usefulness, create and freeze `SOURCE_COLLECTION_MANIFEST` for each mandatory domain and at least two additional eligible domains.

For each collection record:

- canonical name/URL/identifier;
- responsible organisation;
- why it is broad/domain-wide rather than selected for a known TRACE-friendly case;
- alternative qualifying collections considered;
- canonical order rule;
- intake quota;
- access/date boundary.

Prefer broad public collections/registries over curated “interesting failure” lists.

The manifest itself must be committed/frozen and attacked for obvious TRACE-favourability before item-level intake. At least one attack aperture must not be the aperture that selected the collections if such an aperture is available. If not available, record `SOURCE_MANIFEST_INDEPENDENCE_LIMITED`.

```text
SOURCE_COLLECTION_FROZEN != SOURCE_COLLECTION_NEUTRAL
```

Collection choice remains an explicit residual study aperture; the protocol does not claim representative sampling.

---

## 7. Canonical order and eligibility intake

Collection order:

1. ascending stable source-native identifier when available;
2. otherwise published/decision date ascending, canonical item URL tie-break;
3. otherwise `ORDER_UNUSABLE`; replace collection before item-level TRACE-relevance reading and preserve failed manifest entry.

No sort/filter change after seeing which cases would enter.

Real-case eligibility:

1. sufficient public factual material for bounded packet;
2. consequential decision/transition or retrospective decision review;
3. not authored/designed by this project;
4. source can be frozen/cited;
5. not excluded because it appears too easy, too hard, too favourable or unfavourable to TRACE.

Preserve every intake exclusion and exact reason. Pool target: >=20 eligible real cases overall.

---

## 8. Mechanically derived case IDs and final selection

```text
SOURCE_COLLECTION_ID = frozen canonical collection identifier
SOURCE_NATIVE_ID_OR_URL = exact source-native id; otherwise canonical item URL
CASE_ID = SHA256(SOURCE_COLLECTION_ID + "\n" + SOURCE_NATIVE_ID_OR_URL)
```

Human aliases do not participate. Domain mapping is frozen before CASE_ID ordering is inspected.

Select:

1. smallest CASE_ID in infrastructure slot;
2. smallest unused in public-administration slot;
3. smallest unused in ecological slot;
4. smallest unused in AI/software slot;
5. two smallest remaining IDs satisfying >=4 non-AI and >=4 domains.

Preserve full pool and hashes.

`DETERMINISTIC_SELECTION != REPRESENTATIVE_SAMPLE_OF_WORLD`.

---

## 9. Controls and packet construction

Negative control: one low-complexity synthetic case with explicit facts, affected parties and correction path. Intended test is boundedness; TRACE should add little.

Stress control: one synthetic case with >=2 known compression traps but no TRACE vocabulary. It tests firing under source control, not real-world usefulness.

Freeze controls before receiver dispatch.

For real cases, use the same frozen packet across arms. Prefer full bounded primary-source material. If compressed, include source identities/dates, factual material, explicit unavailable facts, ordinary-language question and omission map.

No TRACE labels or expected lesson. Check case question for TRACE-coded cueing not native to source.

Where feasible, an independent packet auditor who has not seen expected gains checks source fidelity/material omissions only. If unavailable, record `PACKET_AUDIT_INDEPENDENCE_LIMITED`.

`CASE_PACKET != WORLD`.

---

## 10. Capture and primary burden

Preserve verbatim output plus:

- exact model/runtime/family;
- coldness disclosure;
- CASE_ID / arm / order / PAIR_ATTEMPT;
- carrier identity;
- receiver-visible input/output byte counts;
- provider token counts where available;
- elapsed/provider time;
- spend evidence state if applicable;
- truncation/failure/output-limit violation;
- clarification requests;
- operator intervention.

Store `TRACE_DELTA_NOTE` separately.

Primary deterministic burden:

```text
PRIMARY_BURDEN_BYTES = UTF8_BYTES(receiver-visible input)
                     + UTF8_BYTES(receiver-visible full output)

PRIMARY_BURDEN_RATIO = T_PRIMARY_BURDEN_BYTES / A_PRIMARY_BURDEN_BYTES
```

The T delta note counts because the receiver had to generate it. This byte measure is a crude deterministic transport/reading-volume proxy, not cognitive-cost truth. Report provider tokens, time, money, output words and adjudication burden separately. Do not substitute another burden view into the predeclared 1.5x rule.

---

## 11. Blind adjudication and positive-gain confirmation

Assign main A/T outputs random neutral labels. Remove T `TRACE_DELTA_NOTE`. Remove obvious invariant codes/framework labels only if underlying meaning is unchanged; otherwise mark `ARM_BLINDNESS_PARTIAL`.

Adjudicators use frozen case/source evidence, not author intent.

A candidate T-only gain can be noted after one adjudicator, but it counts toward retention/reproduction only as `CONFIRMED_GAIN` if:

1. **two distinct adjudicator model families/organisations** independently find it supported and materially consequential; and
2. at least one adjudicator family differs from the receiver family that produced the candidate gain.

If two distinct adjudicator families cannot be obtained, record `ADJUDICATION_INDEPENDENCE_LIMITED`; candidate gains remain `UNCONFIRMED_GAIN` for positive retention purposes.

Material disagreement => `GAIN_DISPUTED`, not majority-washed gain.

Mark retains project/release authority but is not counted as independent efficacy adjudication.

---

## 12. Pair-level dimensions

For each valid pair preserve separately:

- supported material distinctions A/T;
- confirmed/unconfirmed T-only gains;
- A-only gains;
- unsupported confidence/invention;
- affected-party/scope omission;
- over-firing/irrelevant asserted structure;
- authority/value leakage;
- usable check/review/repair information;
- usability/transfer failures;
- primary burden + secondary token/time/cost views;
- material precision: supported distinctions versus unsupported/irrelevant asserted distinctions.

Synonyms/duplicate granularity count once.

Pair-level baseline capture:

```text
BASELINE_CAPTURE_OF_T = equivalent A-supported distinctions / T-supported distinctions
```

If denominator is zero: `NOT_APPLICABLE`.

Do not union all receiver outputs into one giant T answer.

---

## 13. Predeclared reproduction classes

```text
R_SCOPE       affected-party/scope discovery or aggregation loss
R_WARRANT     evidence/warrant/currentness/verification-status collapse
R_CORRECTION  route/review/rollback/hardening/repair-window failure
R_BURDEN      burden/residue/loss survival
R_AUTHORITY   capability/description/authority/permission confusion
R_OTHER       other
```

A broad class label alone is insufficient. Adjudicators must state the concrete common mechanism. `R_OTHER` can reproduce only the same specifically described mechanism.

A confirmed gain is `REPRODUCED` if either:

1. substantially same gain appears for same real case in >=2 cold receiver families; or
2. same predeclared class **and concrete mechanism** appears in >=2 independent real cases, produced across >=2 cold receiver families.

One case/family only => `SINGLE_APERTURE_GAIN`.

---

## 14. Aggregation

Summarise valid pair-level evidence only:

- real cases with confirmed T-only gains;
- domains/classes with reproduced gains;
- cold families reproducing gains;
- median pair-level baseline-capture ratio where applicable;
- median PRIMARY_BURDEN_RATIO;
- secondary token/time/cost views;
- negative-control over-fire frequency;
- HOLD/insufficiency gates.

No extra credit for verbosity.

---

## 15. Disposition precedence and non-conflict rule

Apply in this order:

1. comparison integrity/contamination;
2. authority/value leakage + unsupported-confidence HOLD;
3. cold receiver/adjudication sufficiency;
4. confirmed gain existence;
5. reproduction;
6. complexity/over-fire pressure;
7. final narrow disposition.

### HOLD / insufficiency

Use HOLD/insufficient-evidence if:

- contamination invalidates material comparison;
- >=2 cold receivers require author coaching to use compact carrier;
- repeated material T authority/value leakage absent from paired A;
- T materially increases unsupported confidence/completeness in >=2 real cases across >=2 families;
- fewer than two session-cold families complete enough valid pairs;
- independent adjudication is insufficient to confirm candidate gains.

HOLD does not imply repair; consider removal/shrink first.

### Zero confirmed gain

If zero confirmed T-only material gains across real cases: `SHRINK_OR_DEMOTE`.

### Confirmed but unreproduced gain

If >=1 confirmed T-only gain exists but **no gain satisfies reproduction**, default disposition is:

```text
EVIDENCE_FRAGILE
```

This takes precedence over the general “no reproduced gain” shrink condition. However an **independent shrink trigger** may still produce `SHRINK_OR_DEMOTE`, specifically:

- negative-control substantial over-fire in majority of cold receivers;
- compact carrier unusable while only full carrier works at impractical cost;
- median baseline capture >=80% **and** median PRIMARY_BURDEN_RATIO >=1.5.

### Reproduced-gain path

With >=1 reproduced gain, apply the remaining retain/shrink criteria.

`SHRINK_OR_DEMOTE` if reproduced evidence does not span at least two non-project-native real cases/domains, or independent complexity triggers dominate.

`RETAIN_NARROW` requires all:

- >=2 real cases in >=2 domains with confirmed T-only gains;
- reproduction satisfied;
- >=1 reproduced gain in R_SCOPE/R_WARRANT/R_CORRECTION/R_BURDEN/R_AUTHORITY;
- bounded negative control;
- no repeated material authority/value leakage;
- >=2 cold families use compact carrier without author coaching;
- independent adjudication sufficient;
- observed cost plausibly proportionate to bounded gain.

If all material retention conditions pass but median baseline capture >=80% and median PRIMARY_BURDEN_RATIO >=1.5, or another strong complexity signal survives, use:

```text
RETAIN_NARROW_WITH_COMPRESSION_PRESSURE
```

No retention disposition means validation/release/canon.

---

## 16. Non-binding sensitivity report

Official thresholds do not move after results.

Report alternative views for:

- baseline capture 70/80/90%;
- primary burden 1.25/1.5/2x;
- real-case gain count 1/2/3.

If small changes flip the conclusion, state `DISPOSITION_THRESHOLD_SENSITIVE`.

---

## 17. Secondary full-candidate test

Only after primary A/T outputs and primary disposition evidence are frozen, choose two real cases with smallest CASE_ID and run Arm F.

Test:

- material limit/distinction compact carrier lost;
- UNKNOWN/provenance survival;
- recital/overhead;
- carrying versus enforcement.

Compact failure remains primary portability evidence.

---

## 18. Existing-method gate

A retain result establishes at most bounded value over ordinary careful analysis. Before claims of distinct practical advantage or adoption readiness, run a separate domain-appropriate comparator against relevant established methods.

```text
BEATS_ORDINARY_BASELINE != BEATS_EXISTING_METHODS
```

---

## 19. Fixed final 20-case replay

Replay exactly:

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

If no materially distinct protocol defect survives, freeze exact v0.4 identity with residual limits and **stop meta-protocol polishing**.

---

## 20. Stop

No source collection or case identity is selected by this object.

Next only after successful replay:

```text
freeze exact v0.4 identity
-> build/freeze/attack SOURCE_COLLECTION_MANIFEST
-> only then item-level intake and deterministic case selection
```
