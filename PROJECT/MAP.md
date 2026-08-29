# TRACE — PROJECT MAP

## Currentness

```text
CURRENTNESS_MODE: SNAPSHOT
DERIVED_AT_COMMIT: d5c8a282db0acc4408e9548a42a2482245ec6be2
LAST_VERIFIED: 2026-08-29
DEPENDS_ON:
  - OUTWARD_API_EXECUTION_RESULT v0.2 blob cb74678b6e31a1b82fd6b4d762566fd04aba123e
  - BLIND_ADJUDICATION_API_RESULT v0.4 blob feb8c7a7f9aefc0613b8b670ec1c0833b181f062
  - PUBLIC_BLIND_PACKET_ARCHIVE blob d467b3ad7d686868f99fbad1c40c7aa2d0c56a85
REACQUIRE:
  - mutable branch / PR state -> live TRACE PR #38
  - released baseline -> live TRACE releases/main before release-sensitive action
```

This file does not carry a `CURRENT_BRANCH_HEAD`. Committing a branch-head value here would move the branch and make the claim self-invalidating. The commit above identifies the state from which this snapshot was derived.

`MAP != WORLD` and `SNAPSHOT != LIVE`.

## Controlled objects at this snapshot

```text
released baseline
  -> TRACE v0.2.7

next-version semantic comparison surface
  -> PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_11.md
       [25,355-byte compact spine; working / non-canon / unvalidated]

donor-preserving assembly
  -> PROJECT/TRACE_FORMAL_SEED_v0_3_0_FULL_WORKING_CANDIDATE_v0_1.md
       [179,731-byte deterministic full candidate; working / non-canon / unvalidated]

lineage and build controls
  -> PROJECT/TRACE_v0_2_7_TO_v0_3_0_DONOR_MAP_v0_1.md
  -> PROJECT/TRACE_v0_3_0_EXPANSION_PRESERVATION_RULE_v0_1.md
  -> PROJECT/TRACE_v0_3_0_BUILD_BRIEF.md

outward evidence controls
  -> PROJECT/TRACE_v0_3_0_OUTWARD_EVALUATION_PROTOCOL_v0_5_EXPANSION.md
  -> PROJECT/TRACE_v0_3_0_OUTWARD_API_EXECUTION_RESULT_20260829_v0_2.md
  -> PROJECT/TRACE_v0_3_0_BLIND_ADJUDICATION_API_RESULT_20260829_v0_1.md ... v0_4.md
  -> PROJECT/artifacts/TRACE-v0.3.0-blind-adjudication-public-20260829-v0.1.zip
```

The compact spine and full candidate are not interchangeable. The spine is the bounded receiver-facing comparison object. The full candidate preserves donor capability and implementation detail.

## Evidence state at this snapshot

```text
source-contract F01-F10 pass: BOUNDED-CLOSED FOR THIS PASS
primary two-family calls:      32 / 32 COMPLETE
paired A/T units:              16 / 16 TECHNICALLY COMPLETE
primary status:                COMPLETE_UNADJUDICATED
blind two-family adjudication: NOT COMPLETED
arm key:                       SEALED
efficacy result:               NONE
failure result about TRACE:    NONE
```

The primary run established execution and burden evidence. It did not establish a TRACE-only gain. Blind adjudication attempts exposed transport and access failures across Kimi, Grok and signed-out Meta routes. Those failures do not adjudicate the paired outputs.

## Current interpretation

Earned:

- the v0.11 spine and v0.1 full candidate reproduce deterministically under declared checks;
- the primary two-family study completed without call failure, truncation or retry;
- the compact carrier imposed substantial input/reading-volume burden;
- nine Kimi outputs exceeded the requested word envelope;
- public blind packets can be inspected without the arm key or expected-result notes.

Not earned:

- practical advantage over competent ordinary analysis or an established domain method;
- a positive or negative efficacy disposition;
- a new TRACE primitive or root;
- replacement of v0.2.7;
- release, canon, validation, authority, permission or clearance.

## Next boundary

Document cleanup, candidate assembly review and external criticism may continue without waiting for adjudication. Any efficacy claim remains blocked until the frozen pairs receive valid blinded assessment. Do not convert transport difficulty into evidence for or against TRACE.

Before acting on mutable state, use the `REACQUIRE` routes above.
