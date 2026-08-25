# TRACE v0.3.0 — OUTWARD EVALUATION PROTOCOL v0.2 FALSIFICATION

**Status:** MATERIAL DEFECTS FOUND BEFORE CASE SELECTION — DO NOT FREEZE v0.2  
**Date:** 2026-08-25  
**Target:** `PROJECT/TRACE_v0_3_0_OUTWARD_EVALUATION_PROTOCOL_v0_2.md`

```text
VERDICT: BREAK / PRE-FREEZE
CASES SELECTED: 0
RUNS EXECUTED: 0
TRACE SEMANTIC OBJECT CHANGED: NO
```

v0.2 repairs the v0.1 comparator/pool/ID defects, but a second hostile pass found additional confounds that could still create a persuasive but unreliable result.

## Findings

### P11 — output opportunity is not held constant

Both prompts say “concise” but no shared visible-answer ceiling exists. A longer T output gets more opportunities to surface a unique distinction. Cost accounting after the fact does not fully remove this confound.

Repair: same explicit visible answer limit for A/T/F (`<=1200 words`) and same provider visible-output ceiling where transport permits. Truncation remains evidence.

### P12 — stochastic/runtime drift can masquerade as framework effect

v0.2 requires fresh contexts but does not bind paired A/T runs to the same exact model/runtime window. A model update or ordinary sampling variance could create the apparent delta.

Repair: record exact runtime/model identity; interleave/randomise A/T order within a bounded run window; invalidate a pair if runtime identity materially changes. Preserve provider nondeterminism as a limit.

### P13 — aggregation across receiver families is under-specified

The 80% capture rule does not define whether distinctions are unioned across models, counted per case, or counted per paired run. Different aggregation choices can change the disposition.

Repair: primary unit becomes `case x receiver-family paired A/T`. Compute capture/material-gain evidence at pair level, then aggregate medians/counts across valid pairs. Do not union all T verbosity into one denominator.

### P14 — retention can rest on one-off receiver variance

Two cases/two domains could satisfy retention even if each “gain” appears in only one model family once.

Repair: at least one project-central gain must reproduce across two cold receiver families on the same case **or** the same failure class must recur in two independent real cases with support from different receiver families. Otherwise disposition remains `EVIDENCE_FRAGILE` even if other retention conditions pass.

### P15 — message ordering / recency is unspecified

Arm T has an additional carrier. Whether the carrier or case appears last can materially change model attention. Unspecified ordering creates another operator degree of freedom.

Repair: freeze message envelope/order for all arms. In T/F the carrier appears before the case packet so the case remains the most recent substantive object; final instruction/word limit is identical.

### P16 — source-collection choice remains a residual author degree of freedom

v0.2 freezes collections before case narratives, a major improvement, but the project still chooses which broad collections qualify. This cannot be fully eliminated in a bounded study.

Repair: freeze a source-collection manifest before item reading, state objective selection rationale, prefer broad domain-wide collections over issue-specific collections, and record alternative qualifying collections considered. Treat collection selection as a declared aperture and residual limitation, not “unbiased.”

### P17 — source native order can be ambiguous

Web collections often offer multiple default sorts/filters. “Native order” can be chosen opportunistically.

Repair: use stable ascending native identifier when available; otherwise chronological published date ascending with canonical URL tie-break; otherwise declare the collection unusable for deterministic intake.

### P18 — existing-method distinctiveness remains untested

Beating ordinary careful analysis would still not establish value over FMEA/STPA/safety-case/incident-analysis or other relevant methods.

Disposition: not a blocker for this first outward cycle, but any retention result must explicitly open a **method-comparator gate** before claims of distinct practical advantage or adoption readiness.

### P19 — prompt/case question can vary in final operator wrapping

The protocol gives task text but not the exact message envelope. Extra operator preambles could cue one arm.

Repair: freeze allowed message parts and forbid additional semantic coaching. Operational metadata may be added only outside the receiver-visible prompt.

## Disposition

Do not execute/freeze v0.2. Build v0.3 with P11-P19 repairs, then run a bounded attack matrix. Stop protocol polishing if that attack yields no materially distinct confound; residual limitations should be recorded rather than driving infinite meta-protocol work.
