# TRACE v0.3.0 — OUTWARD EVALUATION PROTOCOL v0.4 — PRE-FREEZE 20-CASE ATTACK

**Status:** NOT CLEAR — WORKING v0.4 REQUIRES NARROW PRE-FREEZE REPAIR  
**Target initial v0.4 commit:** `002795e5315c39cd01293416ef0821efe7ee4d1e`  
**Cases selected:** 0  
**Receiver runs:** 0

## Fixed-matrix result

```text
ATTACKS: 20
RESISTED: 15
MATERIAL/NARROW EXECUTION FINDINGS: 5
VERDICT: NARROW BREAK BEFORE FREEZE
```

The same 20 confounds declared in v0.4 were replayed. No new attack category was invented after seeing the object.

## Findings

### V4-P01 — Arm A/T recommendation-separation asymmetry

Arm T is explicitly told to keep structural analysis separate from value/action selection; Arm A is not. If T then shows less authority/value leakage, the protocol cannot distinguish TRACE effect from prompt instruction.

Repair: add the same ordinary-language sentence to Arm A: `Keep factual/structural analysis separate from any recommendation or value judgment.` D7 remains primarily a safety check, not automatically a TRACE gain.

### V4-P02 — selective retry policy absent

A failed/truncated A or T attempt could be selectively rerun, changing sampling opportunity by arm.

Repair:

```text
NO_SILENT_OR_SELECTIVE_RETRY
```

Preserve every attempt. If an infrastructure failure before a usable model return warrants rerun, rerun **both arms** as a new pair-attempt under the same frozen inputs; original failure remains evidence. Model/content failure is not automatically retryable.

### V4-P03 — output-limit noncompliance can buy more discovery opportunity

A receiver that ignores `<=1200 words` can surface more candidate gains.

Repair: preserve full over-limit output as usability/burden evidence but mark `OUTPUT_LIMIT_VIOLATION`; it cannot generate positive T-only gain credit beyond the first 1200 words. If provider hard ceiling differs materially between arms, pair invalid.

### V4-P04 — adjudication independence can still be same-family duplication

Two “apertures” could be two sessions of the same adjudicator model family.

Repair: positive gain confirmation requires two distinct adjudicator model families/organisations where available. If only same-family duplicate adjudication exists, gain remains `ADJUDICATION_INDEPENDENCE_LIMITED` and cannot satisfy positive retention by itself.

### V4-P05 — `EVIDENCE_FRAGILE` conflicts with `SHRINK_OR_DEMOTE`

A run with confirmed one-off gains but no reproduction satisfies `EVIDENCE_FRAGILE`, while the current shrink rule also says no reproduced gain -> shrink. The protocol does not state which wins.

Repair precedence:

- zero confirmed gains -> `SHRINK_OR_DEMOTE`;
- >=1 confirmed gain but no reproduced gain -> `EVIDENCE_FRAGILE` unless an independent shrink trigger also fires (e.g. negative-control over-fire, unusable compact carrier, or high baseline capture + burden);
- reproduced gains then proceed to retain/shrink complexity test.

## Residuals deliberately not promoted to another repair loop

- source-collection choice remains an explicit author/source aperture; manifest freeze + independent attack limits but does not erase it;
- provider stochasticity cannot be eliminated; pair/runtime/reproduction rules bound it;
- byte burden is a crude transport/reading-volume proxy, not cognitive cost truth;
- a six-real-case first cycle supports only narrow conclusions.

## Disposition

Apply these five narrow repairs to the working v0.4 file before freeze. Then replay the **same fixed 20 attacks**. If they resist, freeze exact v0.4 identity with the residual limits above and stop meta-protocol work.
