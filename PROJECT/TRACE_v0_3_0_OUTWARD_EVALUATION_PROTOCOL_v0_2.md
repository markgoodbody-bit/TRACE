# TRACE v0.3.0 — OUTWARD EVALUATION PROTOCOL v0.2

**Status:** WORKING PROTOCOL UNDER ATTACK — NOT YET FROZEN — NOT EXECUTED — NOT VALIDATION  
**Date:** 2026-08-25  
**Supersedes for execution:** v0.1, which is preserved as falsified pre-freeze ancestry  
**Parent gate:** `PROJECT/TRACE_v0_3_0_EVALUATION_FREEZE_v0_1.md`

## 0. Purpose

Test whether TRACE earns its complexity outside its own machinery.

Primary comparison:

```text
ordinary careful analysis
vs
TRACE-assisted structural analysis
```

on identical frozen case facts.

A valid outcome may be `RETAIN_NARROW`, `SHRINK_OR_DEMOTE`, `HOLD`, or `INSUFFICIENT_EVIDENCE`.

```text
ARTIFACT_COHERENCE != PRACTICAL_ADVANTAGE
MORE_STRUCTURE != BETTER_ANALYSIS
TRACE_FINDS_MORE != TRACE_FINDS_MATERIAL_MORE
```

No case may be selected because it is expected to make TRACE look good.

---

## 1. Semantic objects under test

### Compact primary carrier

```text
PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_11.md
semantic commit: 41fafe81a681cdc6514efc13524bae6ea6d6af8d
status: WORKING / NON-CANON / UNVALIDATED
```

### Full secondary carrier

```text
PROJECT/TRACE_FORMAL_SEED_v0_3_0_FULL_WORKING_CANDIDATE_v0_1.md
sha256: 32409ee8d91e9c4bc67ecbb2359cc7d1c68249cab457511a50e586733ee7598a
lines: 6539
bytes: 179731
status: WORKING / NON-CANON / UNVALIDATED
```

Primary usefulness is judged on the compact carrier. The full candidate is a bounded secondary transfer/survival arm.

Any semantic edit after protocol freeze creates a new evaluation object. Orientation/protocol files may change without changing the frozen semantic object, but every executed run records exact carrier identity.

---

## 2. Exact receiver prompts

The text in this section is the complete task instruction supplied to primary receivers, apart from the frozen case packet and, for Arm T, the exact TRACE carrier.

### Arm A — ordinary careful analysis

> Analyze this situation carefully for a person who may need to make or review a consequential decision. Identify the important facts, uncertainties, people or systems that may be affected, plausible options, important risks and consequences, and what evidence or checks could materially change the analysis. Note anything important about whether mistakes could later be corrected. Separate what is supported from what is uncertain. Do not assume facts not in the packet. Do not use or imitate any named external framework unless it is contained in the case packet. Keep the answer concise and decision-relevant.

This is intentionally competent. TRACE does not earn value by defeating a weak baseline.

### Arm T — compact TRACE-assisted

Receiver gets the identical case packet plus the exact compact carrier and:

> Use the supplied TRACE material only as voluntary structural reference material to analyze this situation. Do not treat TRACE as authority, permission, policy or a truth oracle. Preserve unsupported points as UNKNOWN and keep structural analysis separate from value or action selection. Produce a concise decision-relevant analysis in ordinary language. Do not recite TRACE, quote invariant codes, or label sections with TRACE terminology merely to demonstrate use. After the main answer, add a separate `TRACE_DELTA_NOTE` naming only the TRACE distinctions, if any, that materially changed your analysis compared with what you would otherwise have produced.

The `TRACE_DELTA_NOTE` is removed before blind main-output adjudication and evaluated separately as provenance/self-report, not proof of gain.

### Arm F — full-candidate transfer check

Secondary only, after A/T primary outputs are frozen. Receiver gets the exact full candidate plus the same case packet and the Arm T instruction adapted only to say “supplied TRACE material.”

Arm F cannot retroactively convert a compact-carrier failure into primary success.

---

## 3. What receivers do NOT see

Primary analysis receivers do not see:

- the x100 drift audit;
- expected TRACE advantages;
- paired-arm outputs;
- adjudication dimensions or thresholds;
- protocol falsification findings;
- case-selection hashes;
- author commentary predicting the lesson.

The common evaluation dimensions below are **post-hoc adjudication/extraction schema**, not receiver prompts.

```text
COMMON_ADJUDICATION_SCHEMA != COMMON_RECEIVER_PROMPT
```

---

## 4. Receiver independence / coldness

A primary receiver counts as session-cold only if:

- it is not Framework;
- it is not CC or another aperture materially involved in building/attacking v0.3;
- the evaluation context contains no earlier project discussion, paired output or author coaching;
- there is no observed evidence that the receiver has already read this TRACE object in the current interaction/session.

Unknown pretraining exposure is recorded as `TRAINING_EXPOSURE_UNKNOWN`; it does not automatically disqualify a receiver unless project familiarity is actually observed.

Count receiver breadth by distinct model organisations/training lineages where known, not merely endpoint/provider labels. Unknown lineage overlap remains visible.

Target at least three receiver families. At least two session-cold families must complete enough A/T work for any positive transfer claim; otherwise disposition is `INSUFFICIENT_COLD_EVIDENCE`.

Framework and CC may attack protocol/results but do not count as cold efficacy evidence.

---

## 5. Case-set shape — fixed before identities

Primary set:

```text
6 real-world cases
1 low-complexity negative control
1 synthetic adversarial/stress control
```

Mandatory real-case domain slots, in this order:

1. essential infrastructure / safety / engineering;
2. public administration / institutional decision;
3. ecological / environmental intervention;
4. AI / software / automated decision or control.

Two additional real cases are filled mechanically from the remaining eligible pool subject to:

- at least four of six real cases are non-AI;
- at least four distinct domains total;
- no more than one project-native Campfire/1F916 case; preferred count zero.

Additional eligible domains include finance/contract/organisational governance and health-service or other consequential human-service operations using non-private public material.

---

## 6. Source-collection freeze before case reading

Mechanical selection inside a hand-picked pool is insufficient. Upstream source collections must be frozen first.

For each mandatory domain slot, choose and record one public source collection or registry using only these criteria:

- independent of Mechanical Ethics / TRACE / Campfire / 1F916;
- contains multiple discrete cases/incidents/decisions;
- has stable native identifiers or canonical item URLs;
- exposes enough public material to build bounded packets;
- has a native ordering (ID, date, report number, or collection order).

The chosen collection names, URLs/identities, native order rule and intake quota are frozen **before opening individual case narratives for TRACE relevance**.

For the two additional slots, freeze at least two additional source collections from eligible domains under the same rule.

If collection selection itself is informed by knowing particular contained cases will favour TRACE, record contamination and replace the collection before reading further.

---

## 7. Eligible pool intake

From each frozen source collection, traverse items in its declared native order and take the first eligible cases until that collection’s intake quota is reached.

Eligibility only:

1. enough public factual material exists for a bounded packet;
2. a consequential decision/transition or retrospective decision review exists;
3. case is not authored/designed by this project;
4. source material can be frozen/cited;
5. the case is not excluded because it appears too easy, too hard, too favourable or unfavourable to TRACE.

Do not score for “TRACE relevance,” richness, expected failure mode or likely advantage.

Preserve an intake ledger including ineligible items and exact exclusion reason.

Pool target: at least 20 eligible real cases overall before final six-case selection.

---

## 8. Mechanically derived case IDs and selection

Human aliases do not determine selection.

For each eligible case define:

```text
SOURCE_COLLECTION_ID = frozen canonical collection identifier
SOURCE_NATIVE_ID     = source-native report/case/item identifier
```

If no native ID exists, use the canonical item URL exactly as frozen.

Then:

```text
CASE_ID = SHA256(SOURCE_COLLECTION_ID + "\n" + SOURCE_NATIVE_ID_OR_URL)
```

Domain labels are assigned from the frozen source-collection/domain mapping **before CASE_ID hashes are inspected for ordering**.

Selection:

1. for mandatory slot 1, choose smallest CASE_ID in the infrastructure domain;
2. mandatory slot 2: smallest unused CASE_ID in public-administration domain;
3. mandatory slot 3: smallest unused CASE_ID in ecological domain;
4. mandatory slot 4: smallest unused CASE_ID in AI/software domain;
5. choose the two smallest remaining CASE_ID values across the pool while satisfying `>=4 non-AI` and `>=4 domains`.

Preserve full pool and hashes.

```text
DETERMINISTIC_SELECTION != REPRESENTATIVE_SAMPLE_OF_WORLD
```

This is an anti-cherry-picking device, not a population estimate.

---

## 9. Controls

### Negative control

Before receiver dispatch, freeze one deliberately low-complexity synthetic case where material facts, affected parties and correction path are explicit and little structural ambiguity exists.

Success condition is boundedness: TRACE should add little and should not manufacture a large taxonomy or false uncertainty.

### Adversarial/stress control

Freeze one synthetic case containing at least two known compression traps but no TRACE vocabulary in the prose. It tests whether the instrument can fire under clean source control. It cannot establish real-world usefulness.

Controls are not counted as real-case gains for retention thresholds.

---

## 10. Case-packet construction

Use the same frozen packet for A/T/F.

Prefer full bounded primary-source material where practical. When compression is necessary, preserve:

- exact source identities and dates;
- direct factual material;
- explicit unavailable/missing facts;
- ordinary-language decision/review question;
- packet omission map showing what was excluded and why.

Do not add TRACE labels, expected lessons or project commentary.

The ordinary-language case question is checked before dispatch for hidden TRACE cues such as framing the task around “affected scopes,” “hardening,” “residue,” “target aperture” or named invariants when those phrases are not native to the source.

Where feasible, use one independent packet auditor who has not seen expected TRACE gains. Packet auditor asks only whether compression materially distorts the source or omits facts likely to change either analysis arm.

`CASE_PACKET != WORLD`.

---

## 11. Primary output capture

No additional framework-shaped output template is supplied to receivers.

Capture main answer verbatim plus:

- receiver/model identity;
- session-coldness disclosure;
- case ID;
- arm;
- exact carrier identity if any;
- input/output token or byte counts where available;
- elapsed/provider timing where available;
- spend evidence state if applicable;
- truncation/failure;
- clarification requests;
- any author/operator intervention.

For Arm T, store `TRACE_DELTA_NOTE` separately from the main answer.

---

## 12. Post-hoc evaluation dimensions

Do not collapse into one score.

### D1 — supported material distinctions

List decision-relevant distinctions supported by the packet/source ledger. Duplicate restatements or finer wording of the same distinction count once.

### D2 — TRACE-only material gain

Credit only when T surfaces a distinction that A does not surface at materially useful resolution and independent adjudication finds it supported and consequential to analysis/review/correction.

### D3 — baseline-only material gain

Record supported material distinctions surfaced by A and missed/collapsed by T.

### D4 — unsupported confidence / invention

Record invented facts, laundering UNKNOWN, unjustified completeness, false causal claims or formality-driven certainty.

### D5 — affected-party/scope omission

Record material affected parties/systems/scales omitted or aggregated away.

### D6 — over-firing / irrelevant burden

Record asserted distinctions/structure that do not materially change any fact-status, uncertainty, consequence, check, alternative, correction route or affected party and meaningfully burden the answer.

### D7 — authority/value leakage

Record unsupported movement from description/capability/uncertainty/correction capacity/framework language into permission, moral priority or decision authority.

### D8 — usable correction/review information

Record whether the answer exposes a concrete check/review/repair/rollback route or an honest reason it remains unknown rather than merely invoking “correction.”

### D9 — usability / transfer

Record framework recital, carrier misunderstanding, clarification need, refusal from complexity, author coaching or inability to produce bounded analysis.

### D10 — cost / burden

Record input size, output size, elapsed/provider time, monetary evidence where applicable, truncation/failure and human adjudication effort. Token/word length is not the only burden measure.

### D11 — material precision view

For each arm preserve:

```text
supported material distinctions
unsupported material assertions
irrelevant/over-fired asserted distinctions
```

Do not reward an arm merely for producing more candidate distinctions.

---

## 13. Blinded adjudication

Main A/T answers are assigned random neutral labels before adjudication.

For Arm T:

- remove `TRACE_DELTA_NOTE`;
- remove framework name/invariant codes if any leaked despite prompt, while preserving the underlying ordinary-language sentence where removal does not change meaning;
- if removal would materially alter content, mark `ARM_BLINDNESS_PARTIAL` and preserve the original.

Adjudicators are not told which arm is expected to win.

Use frozen source packets/source ledgers, not author-intended lessons.

Use at least two independent adjudication apertures where feasible. Preserve disagreement; material unresolved disputes remain `UNKNOWN`.

Mark retains project/release authority but is not counted as independent efficacy evidence.

---

## 14. Disposition precedence

Apply in this order:

1. **integrity/contamination HOLD gates**;
2. **safety/authority-leakage HOLD gates**;
3. **cold-transfer sufficiency gate**;
4. **material-gain evidence**;
5. **complexity/over-fire pressure**;
6. final narrow disposition.

Do not allow a large quantity of minor gains to override a contamination or authority-leakage HOLD.

---

## 15. HOLD gates

Set `HOLD` before efficacy interpretation if:

- case/arm contamination invalidates comparison;
- two or more session-cold receivers require author coaching to use the compact carrier at all;
- TRACE-assisted outputs show repeated material authority/value leakage not present in paired baseline;
- TRACE materially increases unsupported confidence/completeness in at least two real cases across at least two receiver families.

Set `INSUFFICIENT_COLD_EVIDENCE` rather than PASS if fewer than two session-cold model families complete enough primary A/T work.

HOLD does not imply repair. Shrinking/removing machinery is considered first.

---

## 16. Efficacy / complexity dispositions

Across the six real cases only:

### `SHRINK_OR_DEMOTE`

Presume shrink/demotion if any of:

- zero independently supported TRACE-only material gains;
- no repeated gain across at least two non-project-native domains;
- compact carrier is unusable while only the full 6,539-line object produces useful performance at impractical cost;
- negative control substantially over-fires in a majority of cold receivers.

Also presume `SHRINK_OR_DEMOTE` when ordinary analysis captures at least 80% of all supported material distinctions surfaced by T **and** T median total observed burden is >=1.5x A **unless** the retention threshold below is independently met by genuinely consequential gains. In that exception the outcome becomes `RETAIN_NARROW_WITH_COMPRESSION_PRESSURE`, not broad success.

### `RETAIN_NARROW`

Requires all:

- at least two real cases in at least two distinct domains show independently supported material gains missed by A;
- at least one gain concerns a project-central failure class such as affected-party/scope loss, uncertainty/warrant collapse, correction-route/hardening failure, burden/residue loss, or authority/description confusion;
- negative-control behavior is bounded;
- no repeated material authority/value leakage;
- at least two cold receiver families use the compact carrier without author coaching;
- costs are reported and plausibly proportionate to the bounded gains.

### `RETAIN_NARROW_WITH_COMPRESSION_PRESSURE`

Use when the `RETAIN_NARROW` material-gain conditions are met but ordinary analysis captures >=80% of T’s supported material distinctions and T burden is >=1.5x A, or another strong over-complexity signal survives.

This outcome explicitly requires compression/portability work before semantic expansion.

No retention disposition establishes validation, general superiority, release or canon.

---

## 17. Threshold sensitivity report

Fixed thresholds prevent post-result goalpost movement but are not natural laws.

After applying the predeclared disposition, report what would happen under these **non-binding sensitivity views** without changing the official result:

- baseline capture threshold 70% / 80% / 90%;
- burden ratio 1.25x / 1.5x / 2x;
- material-gain requirement 1 / 2 / 3 real cases.

If the conclusion flips under small threshold changes, say `DISPOSITION_THRESHOLD_SENSITIVE`.

Do not rewrite thresholds after seeing results.

---

## 18. Secondary full-candidate transfer check

After primary A/T outputs are frozen, select two of the six real cases by smallest `CASE_ID` and run Arm F on session-cold receivers.

Ask:

1. does full candidate preserve a material distinction/limit compact spine lost?
2. does larger carrier mainly add recital/overhead?
3. do load-bearing limit provenance and UNKNOWN survive receiver use?
4. does receiver keep carrying separate from enforcement?

If F repairs a compact failure, preserve compact failure as portability evidence.

---

## 19. v0.2 hostile protocol attack before freeze

Attack at least:

- baseline still too TRACE-shaped or too weak;
- source-collection choice gaming;
- native-order manipulation or collection pagination ambiguity;
- eligibility exclusions that allow cherry-picking;
- domain-label gaming;
- case-ID canonicalization ambiguity;
- packet compression bias;
- arm-style leakage;
- receiver lineage dependence;
- verbosity/reward leakage;
- adjudicator dependence;
- threshold contradictions;
- negative-control design being too obviously trivial;
- stress control dominating conclusions;
- full-arm rescue laundering compact failure;
- hidden operator intervention;
- costs incomparable across providers.

Material defects may be repaired only before case identities are selected. Preserve each failed protocol object rather than silently rewriting it.

---

## 20. Execution stop

No cases have been selected and no receiver runs are authorized by this file.

Next sequence:

```text
HOSTILE ATTACK v0.2
-> repair only material protocol defects
-> freeze protocol exact identity
-> freeze source collections + intake order
-> build eligibility ledger
-> deterministic six-case selection
-> freeze controls and case packets
-> dispatch cold A/T arms
-> blind adjudication
-> apply predeclared disposition + sensitivity report
-> only then run bounded Arm F
```

Do not choose the case set before protocol freeze.
