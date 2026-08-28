# TRACE v0.3.0 — OUTWARD PACKET SET FREEZE v0.1

**Status:** FROZEN EIGHT-PACKET RECEIVER SET — NOT DISPATCH — NOT VALIDATION  
**Date:** 2026-08-28  
**Protocol:** `PROJECT/TRACE_v0_3_0_OUTWARD_EVALUATION_PROTOCOL_v0_5_EXPANSION.md`  
**Real-case selection:** `PROJECT/TRACE_v0_3_0_OUTWARD_EFFICACY_SELECTION_v0_1.md`  
**Packet directory:** `PROJECT/outward_case_packets_v0_1/`

## 0. Purpose

Freeze the exact receiver-visible case-packet bytes for the primary outward A/T study before any cold receiver is dispatched.

```text
PACKETS_WRITTEN != PACKET_SET_FROZEN
PACKET_SET_FROZEN != STUDY_EXECUTED
PACKET_FREEZE != PACKET_WORLD_COMPLETENESS
```

No Arm A/T output existed when this freeze was created. No packet was revised in response to receiver performance or expected TRACE gain.

## 1. Byte-identity method

Each committed UTF-8 packet body was re-read from GitHub. The reconstructed byte stream was accepted for SHA-256 only after it reproduced both:

1. the repository-reported byte length; and
2. the repository Git blob SHA-1 (`SHA1("blob " + byte_length + NUL + bytes)`).

This provides an independent check against accidental newline or Unicode normalization during the SHA-256 calculation.

Canonical set line format:

```text
FILENAME|BYTE_LENGTH|SHA256
```

Canonical set order is the table order below. The final newline after every canonical set line participates in `PACKET_SET_ID`.

## 2. Frozen eight packet identities

| slot | role | file | bytes | Git blob SHA-1 | SHA-256 |
|---:|---|---|---:|---|---|
| 1 | REAL / RAIB-2 | `REAL_01_RAIB_2.txt` | 4135 | `b8aacc188dabd634bcd367e33f81613ed39627cd` | `38b20fe3a6cd70c705509aa42b1bcfc779d5c6a27a8777ee0f0c357a007826fa` |
| 2 | REAL / PAC-4 | `REAL_02_PAC_4.txt` | 4968 | `1d85b654efc57a008cc73d54a964036d8a718940` | `0633166ae80d34483381e16e14bed3c4fe70db19aab14bd8fe704f2ac2bf92da` |
| 3 | REAL / EPA-03 | `REAL_03_EPA_03.txt` | 4310 | `a88dde48643b4d8a5e604fc89d7652bf19d3d4b3` | `cc2fe210b9cc0c42850ef8e6c906fa51f81b7c0b5a2f6dc4657f11e59642b140` |
| 4 | REAL / NHTSA-03 | `REAL_04_NHTSA_03.txt` | 4717 | `ee39be02d7bad31c4574f5709a7220e4e227f57c` | `21766d949cc045a5c18dc5bfd67733525449bac8088d317cc294f73550e3bbeb` |
| 5 | REAL / PAC-1 | `REAL_05_PAC_1.txt` | 4979 | `9ba4e10034855e0a7de42d3c2ce3f43fe1bb4b72` | `6b08fd024b5fc8daed19f9fd64a52eb0992174842a186fc9d85e6739a0c50238` |
| 6 | REAL / PAC-5 | `REAL_06_PAC_5.txt` | 5298 | `5ee1a9fc1ac0178aaeda49363a7bfd8977db6af7` | `17464c86daef67b3637e61699f3e44298fda9db04330b11679378cd3725aa8b6` |
| 7 | LOW-COMPLEXITY NEGATIVE CONTROL | `CONTROL_NEGATIVE_01.txt` | 2048 | `44133a6f7005840cf92b57e50047cfe436a06df5` | `4f3844f3a1c9445c917a62028598d32491452d2188938f4ab366038506a3fe6c` |
| 8 | SYNTHETIC STRESS CONTROL | `CONTROL_STRESS_01.txt` | 5325 | `e8a7e42bf39e60c0ce241abb0cdafffe460cdaad` | `77b7c73b73a22122558b3f6b2e92b692803748bad742995809f34ebcc0155c1f` |

```text
TOTAL_PACKET_BYTES: 35780
PACKET_SET_ID_SHA256: 61433c13922bbfc2d0c1c6ee51a5baeb0ee18eb854d9532cf6f6c9f8858b6af8
```

The set ID is SHA-256 over these exact UTF-8 canonical lines, in table order:

```text
REAL_01_RAIB_2.txt|4135|38b20fe3a6cd70c705509aa42b1bcfc779d5c6a27a8777ee0f0c357a007826fa
REAL_02_PAC_4.txt|4968|0633166ae80d34483381e16e14bed3c4fe70db19aab14bd8fe704f2ac2bf92da
REAL_03_EPA_03.txt|4310|cc2fe210b9cc0c42850ef8e6c906fa51f81b7c0b5a2f6dc4657f11e59642b140
REAL_04_NHTSA_03.txt|4717|21766d949cc045a5c18dc5bfd67733525449bac8088d317cc294f73550e3bbeb
REAL_05_PAC_1.txt|4979|6b08fd024b5fc8daed19f9fd64a52eb0992174842a186fc9d85e6739a0c50238
REAL_06_PAC_5.txt|5298|17464c86daef67b3637e61699f3e44298fda9db04330b11679378cd3725aa8b6
CONTROL_NEGATIVE_01.txt|2048|4f3844f3a1c9445c917a62028598d32491452d2188938f4ab366038506a3fe6c
CONTROL_STRESS_01.txt|5325|77b7c73b73a22122558b3f6b2e92b692803748bad742995809f34ebcc0155c1f
```

## 3. Freeze rule

These exact packet bytes are now the case-packet inputs for this study run.

```text
PACKET_CONTENT_CHANGE -> NEW_PACKET_OBJECT
NEW_PACKET_OBJECT -> DO_NOT SILENTLY SUBSTITUTE INTO EXISTING PAIRS
```

Arm A and Arm T for a given case must receive the same exact frozen case packet. Any infrastructure transformation must reproduce the packet SHA-256 before dispatch or the pair is not treated as using this freeze.

The six real packets use the same ordinary-language review question and contain no TRACE vocabulary in that question. The controls were frozen before receiver dispatch.

## 4. Source / omission boundary

Each real packet is a bounded digest of its named official source evidence, with explicit information-not-supplied sections. The NHTSA packet also carries the frozen SGO reporting/provenance ceilings.

```text
CASE_PACKET != WORLD
OFFICIAL_SOURCE != COMPLETE_AFFECTED_PARTY_EVIDENCE
BOUNDED_DIGEST != COMPLETE_ADMINISTRATIVE_RECORD
```

Where the underlying official source already contains recommendations, corrective proposals or explicit limitations, the packet preserves those where material rather than suppressing them to create artificial room for TRACE gain.

## 5. Packet-audit independence limit

The packet constructor / freezer is Framework, which is materially involved in the v0.3 working build. No independent packet auditor uninvolved in expected TRACE gains has yet completed a source-fidelity/material-omission audit over all eight packets before this freeze.

Therefore preserve:

```text
PACKET_AUDIT_INDEPENDENCE_LIMITED
```

This does not by itself invalidate the packet set, but any later packet-fidelity challenge must be preserved rather than silently repaired inside already-generated A/T evidence.

```text
PACKET_AUDIT_INDEPENDENCE_LIMITED != PACKET_INVALID
AUTHOR_PACKET_CONSTRUCTION != INDEPENDENT_AUDIT
```

If a material factual/source-fidelity defect is later established, preserve the affected outputs as evidence from the original packet object and create a new packet/version for any justified rerun. Do not overwrite history.

## 6. Dispatch gate

This freeze discharges the packet-identity gate only.

Before primary cold dispatch:

1. reverify live PR #38 state;
2. reverify that frozen protocol v0.5, compact carrier, execution adapter, 20-case pool freeze and six-case selection have not been superseded/corrected;
3. identify genuinely session-cold receiver families that satisfy the protocol; Framework and CC do not qualify as cold primary receivers because both materially participated in v0.3 construction;
4. preserve exact receiver/model/runtime identity and deterministic arm order;
5. use fresh separate contexts and no cross-arm output exposure.

No efficacy, retention, validation, release, authority, permission or canon claim follows from this freeze.
