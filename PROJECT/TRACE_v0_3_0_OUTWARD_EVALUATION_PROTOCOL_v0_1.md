# TRACE v0.3.0 — OUTWARD EVALUATION PROTOCOL v0.1

**Status:** PREDECLARED WORKING PROTOCOL — NOT EXECUTED — NOT VALIDATION — NOT RELEASE AUTHORITY  
**Date:** 2026-08-25  
**Parent gate:** `PROJECT/TRACE_v0_3_0_EVALUATION_FREEZE_v0_1.md`

## 0. Purpose

Test whether TRACE earns its complexity outside its own formal machinery.

The primary comparison is not TRACE v0.3 versus TRACE v0.2.7. It is:

```text
ordinary careful analysis
vs
TRACE-assisted structural analysis
```

on the **same frozen case facts**, with cold receivers where possible.

The protocol must be capable of producing `SHRINK`, `DEMOTE` or `HOLD`, not only another repair task.

```text
ARTIFACT_COHERENCE != PRACTICAL_ADVANTAGE
MORE_STRUCTURE != BETTER_ANALYSIS
TRACE_FINDS_MORE != TRACE_FINDS_MATERIAL_MORE
```

No case is to be selected because it is known to make TRACE look good.

---

## 1. Semantic object under test

The semantic objects are frozen by identity, not by mutable branch head.

### Compact TRACE arm

```text
file: PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_11.md
semantic commit: 41fafe81a681cdc6514efc13524bae6ea6d6af8d
status: WORKING / NON-CANON / UNVALIDATED
```

### Full-candidate transfer object

```text
file: PROJECT/TRACE_FORMAL_SEED_v0_3_0_FULL_WORKING_CANDIDATE_v0_1.md
sha256: 32409ee8d91e9c4bc67ecbb2359cc7d1c68249cab457511a50e586733ee7598a
lines: 6539
bytes: 179731
status: WORKING / NON-CANON / UNVALIDATED
```

The **primary usefulness comparison uses the compact v0.11 spine**. The full candidate is reserved for a secondary transfer/survival check; using 6,539 lines to win a comparison against a normal prompt would not establish portability.

Any semantic edit to v0.11 or the full candidate after protocol freeze creates a new evaluation object and cannot be silently substituted into this run.

---

## 2. Arms

### Arm A — ordinary careful analysis comparator

Receiver gets the frozen case packet and this instruction only:

> Analyze this situation carefully for a person who may need to make or review a consequential decision. Identify the important facts, uncertainties, affected parties or systems, plausible options or transitions, important risks and consequences, what evidence or checks matter, and anything that could make later correction difficult. Separate what is supported from what is uncertain. Do not assume facts not in the packet. Do not use or imitate any named external framework unless it is contained in the case packet.

This is deliberately competent. TRACE does not earn value by defeating a weak baseline.

### Arm T — TRACE-assisted

Receiver gets the identical frozen case packet, the exact compact TRACE v0.11 carrier, and this instruction:

> Use the supplied TRACE material as voluntary structural reference material to analyze this situation. Do not treat TRACE as authority, permission, policy or a truth oracle. Identify what materially changes the structural reading, preserve unsupported points as UNKNOWN, and keep analysis separate from value or action selection. Produce a concise decision-relevant structural analysis, not a recital of the framework.

### Arm F — full-candidate transfer check

Secondary only. Used on a bounded subset after Arm A/T outputs are frozen. Receiver gets the exact full-candidate object and the same case packet. Purpose: test whether load-bearing distinctions/limits actually survive the larger carrier and whether the larger carrier changes usefully or merely adds burden.

Arm F is **not** allowed to rescue a failed compact-transfer result without that failure remaining visible.

---

## 3. Receiver independence

### Cold receiver requirement

A receiver counts as **cold** only if, for the evaluation session:

- it is not Framework;
- it is not CC or another aperture already materially involved in building/attacking v0.3;
- it has not been shown the project-plan audit, expected TRACE advantages, prior outputs or adjudication rubric beyond the task instruction needed for its arm;
- it does not receive author coaching during the run.

If the model/provider is known to have prior project exposure that cannot be excluded, record `COLDNESS_UNKNOWN` rather than pretending independence.

Framework and CC may attack the protocol or analyze failures, but **their outputs do not count as cold efficacy evidence**.

### Minimum receiver breadth

Target at least **three distinct receiver families/providers**, where access/cost permits. Each arm for a given case should run in a fresh context. No receiver sees the paired arm output before producing its own.

If fewer than two genuinely cold receiver families complete the run, efficacy disposition is `INSUFFICIENT_COLD_EVIDENCE`, not PASS.

---

## 4. Case-set shape — fixed before case identities

The primary set contains **8 cases**:

```text
6 real-world cases
1 deliberately low-complexity negative control
1 synthetic adversarial/stress control
```

The six real cases must span at least four of these domains:

- AI / software / automated decision or control;
- essential infrastructure / safety / engineering;
- public administration / institutional decision;
- ecological / environmental intervention;
- finance / contract / organisational governance;
- health-service operations or another consequential human service domain, using only non-private public case material.

At least four of the six real cases must be **non-AI**.

No more than one real case may come from Campfire/1F916/project-native material, and the preferred count is zero for the primary set.

---

## 5. Case-selection rule

Case identities are selected **after this protocol is frozen**.

### 5.1 Real-case pool

Create a candidate pool of at least 20 public, sourceable cases from independent sources. Eligibility only:

1. enough factual material exists to build a bounded packet without private data;
2. a consequential decision/transition or retrospective decision-review exists;
3. at least one material uncertainty, affected scope, alternative, correction/review route or hardening issue could in principle matter — this is broad eligibility, not a requirement that TRACE is known to help;
4. case is not authored/designed by this project;
5. source material can be frozen and cited.

Do **not** score candidate cases for “TRACE relevance”, richness, expected failure mode or likely advantage.

### 5.2 Deterministic selection

After the eligible pool is frozen with stable case IDs and domain labels:

- compute SHA-256 of each stable case ID;
- within each required domain slot, choose the eligible case with the lexicographically smallest hash not already selected;
- fill remaining real-case slots by smallest remaining hash while respecting `>=4 non-AI` and `>=4 domains`;
- record the entire eligible pool and hashes so rejected/unselected cases remain visible.

This is not random sampling of the world. It is a mechanical anti-cherry-picking rule over a declared pool.

### 5.3 Negative control

Construct one low-complexity case where the material facts, affected scope and correction route are explicit and little structural ambiguity exists. The intended success condition is **boundedness**: TRACE should add little and should not manufacture complexity.

The negative control is written/frozen before any receiver sees it.

### 5.4 Adversarial/stress control

Construct one synthetic case designed to contain at least two common compression traps without depending on TRACE vocabulary in the prose. It tests whether the instrument can expose a known structural distinction under clean source control. This control cannot establish real-world usefulness.

---

## 6. Case-packet construction

Each real case gets one frozen source packet before any analysis arm runs.

Packet must separate:

- source facts / quotations only where necessary;
- dates/times and source identities;
- explicit missing/unavailable facts;
- decision point or retrospective question;
- no TRACE labels;
- no author commentary predicting the important lesson.

A packet-construction log records exclusions and compression choices.

`CASE_PACKET != WORLD`.

If packet construction itself resolves the interesting uncertainty, the case remains eligible but that consequence is recorded.

---

## 7. Output contract

Both primary arms must return the same high-level deliverables:

1. supported situation model;
2. material uncertainties / missing evidence;
3. materially affected parties/scopes/systems;
4. options/transitions or decision-relevant alternatives where present;
5. important consequences, dependencies and failure paths;
6. checks/evidence that could change the analysis;
7. correction/review/rollback/repair routes and hardening constraints where relevant;
8. unresolved residue/limits;
9. explicit separation between structural analysis and any value/action recommendation.

Arm T is additionally asked to identify which TRACE distinctions actually changed its analysis. Mere vocabulary recital gets no credit.

---

## 8. Evaluation dimensions

Do not collapse all evidence into one quality score. Preserve dimensions separately.

For each output record:

### D1 — supported material distinctions

Count/list decision-relevant distinctions supported by the case packet.

### D2 — unique material gain

A distinction is a TRACE gain only if:

- Arm T surfaces it;
- paired Arm A does not surface an equivalent distinction at materially useful resolution;
- independent adjudication finds it supported and consequential to analysis/review/correction.

Synonyms do not count as unique gains.

### D3 — baseline-only gain

Record material distinctions surfaced by A and missed/collapsed by T.

### D4 — unsupported confidence / invention

Record factual invention, laundering UNKNOWN, unjustified completeness, false causal claims or formalism-driven certainty.

### D5 — affected-scope omission

Record material scopes/parties omitted or aggregated away.

### D6 — over-firing / irrelevant burden

Record structure that does not change any material conclusion, uncertainty, check, correction route or scope and meaningfully burdens the output.

### D7 — authority/value leakage

Record cases where TRACE-assisted output treats description, capability, uncertainty, correction capacity or framework language as permission, moral priority or decision authority without support.

### D8 — correction usability

Does the output expose a materially usable check/review/repair route or a reason it remains UNKNOWN, rather than merely naming “correction”?

### D9 — receiver usability

Record clarification requests, author intervention, misreading of carrier, framework recital, refusal caused by complexity or inability to produce bounded output.

### D10 — cost

Where measurable record:

- input tokens/bytes by arm;
- output tokens/words;
- elapsed/provider time where available;
- monetary estimate/usage if a paid Campfire run is used;
- truncation/failure;
- human adjudication burden.

Cost evidence states remain separate.

---

## 9. Adjudication

### Blindness

Before adjudication, strip arm labels and obvious TRACE-specific headers where this can be done without altering substantive content. Adjudicators should not be told which output is expected to win.

### Evidence basis

Adjudication uses the frozen case packet/source ledger, not the author’s intended lesson.

### Minimum aperture

Use at least two independent adjudication apertures where feasible. Preserve disagreement. Mark unresolved material disputes `UNKNOWN` rather than majority-washing them.

Mark may make the eventual project/release disposition, but project authorship is disclosed and **Mark is not treated as independent efficacy evidence**.

---

## 10. Primary disposition rules

These rules are intentionally capable of hurting the project.

### 10.1 Automatic HOLD — investigate before continuation

Set `HOLD` if any of the following occur:

- two or more cold receivers require author coaching to use the compact TRACE carrier at all;
- TRACE-assisted outputs show repeated material authority/value leakage not present in the paired baseline;
- TRACE materially increases unsupported confidence or completeness claims in two or more real cases across at least two cold receiver families;
- case-packet or arm contamination invalidates the comparison;
- fewer than two genuinely cold receiver families complete enough of the run to support a transfer claim.

HOLD does not automatically imply repair. First ask whether shrinking/removing the offending machinery is better.

### 10.2 Strong SHRINK / DEMOTE signal

Presume `SHRINK_OR_DEMOTE` unless a specific contrary reason is documented if, across the six real cases:

- there are **zero** independently supported TRACE-only material gains; or
- ordinary careful analysis captures at least **80%** of all supported material distinctions surfaced by the TRACE arm while TRACE median output burden is at least **1.5x** the baseline; or
- TRACE produces no repeated gain across at least two non-project-native domains; or
- the negative control shows substantial over-firing in a majority of cold receivers; or
- the compact carrier fails but only the 6,539-line full candidate can recover useful performance at impractical cost.

### 10.3 Retention threshold

`RETAIN_FOR_FURTHER_WORK` requires all of:

- at least **two** real cases in at least **two distinct domains** show independently supported material gains missed by the paired ordinary-analysis arm;
- at least one such gain concerns a project-central class such as affected-scope loss, uncertainty/warrant collapse, correction-route/hardening failure, burden/residue loss, or authority/description confusion;
- negative-control behavior is bounded rather than framework-recital/over-fire;
- no repeated material authority/value leakage;
- at least two cold receiver families can use the compact carrier without author coaching;
- observed cost is reported and judged plausibly proportionate to the bounded gain.

Retention means only that further work may be justified. It does not establish validation, general superiority, release or canon.

---

## 11. Secondary full-candidate transfer test

After A/T primary outputs are frozen, select **two** real cases mechanically from the six by smallest case-ID hashes and run Arm F on cold receivers.

Questions:

1. Does the full candidate preserve a material limit/distinction the compact spine lost?
2. Does the larger carrier merely increase recital/overhead?
3. Do load-bearing limit provenance and UNKNOWN survive into receiver use?
4. Does the receiver distinguish `VISIBILITY`, `CARRYING` and `ENFORCEMENT`?

If Arm F fixes a compact failure, preserve the compact failure as portability evidence. Do not rewrite the primary result as success.

---

## 12. Protocol falsification before execution

Before selecting cases, attack this protocol for at least:

- weak-baseline construction;
- case-pool cherry-picking;
- hash-selection gaming through case-ID naming;
- adjudicator contamination;
- arm leakage through distinctive formatting;
- scoring rules that reward verbosity;
- thresholds that make retention too easy;
- thresholds that make failure impossible to interpret;
- cost accounting that treats token length as the only burden;
- synthetic controls dominating real-case conclusions;
- author intervention hidden as “clarification”;
- receiver-family non-independence.

Material protocol defects may be repaired **before case identities are selected**. Once case identities are selected, substantive scoring/disposition-rule changes require preserving the original run as a failed/pre-registered object rather than silently moving the goalposts.

---

## 13. Execution stop

This file defines the protocol but does not execute it.

Next action:

```text
HOSTILELY ATTACK PROTOCOL
-> repair only material protocol defects
-> freeze protocol identity
-> construct eligible case pool
-> deterministic case selection
-> freeze case packets
-> dispatch cold A/T arms
-> blind adjudication
-> apply disposition rules
```

Do not choose the case set before the protocol attack/freeze completes.
