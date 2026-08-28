# TRACE v0.3.0 — PRIMARY COLD RECEIVER DISPATCH PLAN v0.1

**Status:** FROZEN PRE-DISPATCH PLAN — NO PRIMARY RECEIVER OUTPUT YET — NOT VALIDATION  
**Date:** 2026-08-28  
**Protocol:** `PROJECT/TRACE_v0_3_0_OUTWARD_EVALUATION_PROTOCOL_v0_5_EXPANSION.md` + frozen v0.4 mechanics  
**Packet set:** `PROJECT/TRACE_v0_3_0_OUTWARD_PACKET_SET_FREEZE_v0_1.md`  
**Pair attempt:** `1`

## 0. Receiver boundary

Framework and CC are excluded from primary cold receiver evidence because both materially participated in v0.3 construction.

The zero-spend Campfire preflight on 2026-08-28 reported all candidate external connectors as MANUAL ONLY. Before any primary model call, freeze these three distinct provider/training lineages:

| RECEIVER_FAMILY_ID | Campfire connector | organisation | configured model snapshot | primary transport |
|---|---|---|---|---|
| `GEMINI_GOOGLE` | `gemini` | Google | `gemini-3.5-flash` | manual |
| `QWEN_ALIBABA` | `qwen` | Alibaba Cloud | `qwen3.7-plus` | manual |
| `KIMI_MOONSHOT` | `kimi` | Moonshot AI | `kimi-k3` | manual |

Configured model names are routing snapshots, not runtime proof. Every return must preserve actual model/runtime identity. Material model/runtime change between A and T => `RUNTIME_DRIFT`; preserve outputs but exclude that pair from comparative efficacy.

Unknown pretraining exposure remains `TRAINING_EXPOSURE_UNKNOWN` absent observed familiarity.

## 1. Coldness / manual transport rules

For every arm:

- use a fresh model conversation/context;
- do not expose paired output or project discussion from another arm;
- do not coach beyond the exact frozen envelope;
- do not ask the receiver to compare A and T;
- preserve the raw return verbatim;
- if a manual model reports/uses a materially different runtime from its paired arm, mark `RUNTIME_DRIFT`;
- no silent/selective retry;
- clear external infrastructure failure before usable return may justify `PAIR_ATTEMPT=2`, but rerun **both** A and T and preserve attempt 1.

## 2. Control IDs for arm ordering

Real cases retain their frozen SHA-256 CASE_IDs. The two synthetic controls have no source-derived CASE_ID, so before dispatch freeze these exact dispatch-only identifiers for the v0.4 arm-order function:

```text
CONTROL_NEGATIVE_01
CONTROL_STRESS_01
```

This assigns transport order only and does not convert synthetic controls into real-world CASE_IDs.

## 3. Exact deterministic order

Formula inherited from frozen v0.4:

```text
ORDER_HASH = SHA256(CASE_ID_OR_CONTROL_ID + "\n" + RECEIVER_FAMILY_ID + "\n" + PAIR_ATTEMPT)
low bit 0 -> A first
low bit 1 -> T first
```

| case | family | ORDER_HASH | order |
|---|---|---|---|
| RAIB-2 | GEMINI_GOOGLE | `9382952926394880907679aac72778c10d7312cb1737b361397248cb9287389a` | A_FIRST |
| RAIB-2 | QWEN_ALIBABA | `4857787bef9b65d3b79f494348e16f420719d9f70aba287cec307725ae0a07ae` | A_FIRST |
| RAIB-2 | KIMI_MOONSHOT | `a1c65e134a5d6960c9e867f611f8c69b4f10b2c8b6622276d0ed6bfe2b22a2d1` | T_FIRST |
| PAC-4 | GEMINI_GOOGLE | `6b1518c989d5342dc0bcb78dcb577f3f0d234f3e3403f361274e96f675eefd85` | T_FIRST |
| PAC-4 | QWEN_ALIBABA | `66678a0e49d22b0cf06a01a991bea523a0ab5d021c750a8d9950eb2c77279a1a` | A_FIRST |
| PAC-4 | KIMI_MOONSHOT | `ceace685e63fced618c1af61470bd645ed5fe70c9fe0600fa5ceb2bc16f555b9` | T_FIRST |
| EPA-03 | GEMINI_GOOGLE | `c3f4569d0327365e0a690f4273b04d567a3d1c3328d4119bee4a313cfc4c914e` | A_FIRST |
| EPA-03 | QWEN_ALIBABA | `87aca64b4e6eb7382c3e302d9cdeae9083205d92eb712cacd48a4bd0833e2795` | T_FIRST |
| EPA-03 | KIMI_MOONSHOT | `17a9467541c8064a39170372b03f9762251e3f6efda9f63a756d9321b3bc189d` | T_FIRST |
| NHTSA-03 | GEMINI_GOOGLE | `568415bd9f733b82406f77c24088f6357426464563915b9072b3d47cacf05ffd` | T_FIRST |
| NHTSA-03 | QWEN_ALIBABA | `a32756a9f4d30bb163e979c345a84e6eef2cbe56506ee2bad6a874a448547941` | T_FIRST |
| NHTSA-03 | KIMI_MOONSHOT | `e3db45386b5640f5f1c4ea266516e2c0057173dd5e339563d294de11ca063653` | T_FIRST |
| PAC-1 | GEMINI_GOOGLE | `751f249e3f2ef56aa7a8edefcc8037b991a758a222f1e603ff151f0316b5c96e` | A_FIRST |
| PAC-1 | QWEN_ALIBABA | `b16444ab578ea0eb103177e2e7e8e2e05384f96504e6bd628114838b2c406b02` | A_FIRST |
| PAC-1 | KIMI_MOONSHOT | `c7e10d03fb91ac3b24682fb7a817eaee9ac6e7c8b7ac81f5696dfbe7dc34828e` | A_FIRST |
| PAC-5 | GEMINI_GOOGLE | `d87792b038c0b0a91c7c0ef28e8b531db21e419422bfc27a114de8cfc8d0d882` | A_FIRST |
| PAC-5 | QWEN_ALIBABA | `1915ce8c610021b4f106588939dc57e67552b071981d448cb9805c8c2a21ff2b` | T_FIRST |
| PAC-5 | KIMI_MOONSHOT | `d6dc038890616fcab38bdad1eace99cb994a2ca4126d850bf239c125fbdfb73d` | T_FIRST |
| CONTROL_NEGATIVE_01 | GEMINI_GOOGLE | `bb0e88e0bf0bab3cf8aedb72ffcd914931ed4d9e7af5b8891e258e18dc80b23c` | A_FIRST |
| CONTROL_NEGATIVE_01 | QWEN_ALIBABA | `0aaef6400815cd29f2ad9845493b09a90645e3d205c8a58a2f4767dc9f16cb3f` | T_FIRST |
| CONTROL_NEGATIVE_01 | KIMI_MOONSHOT | `cafc4bb18bdcf1365f6255a7e92ea4c20a2b63c3c52cc91007cf5d3c3734c276` | A_FIRST |
| CONTROL_STRESS_01 | GEMINI_GOOGLE | `b4b3b443509cc4d25abb0f79d286a28d0dc64da17cd82c2f55251d9d4f5ba6d2` | A_FIRST |
| CONTROL_STRESS_01 | QWEN_ALIBABA | `eb56c457cba6be5aa759c290fcb5a6156a8746251093657a6289049e998c40a6` | A_FIRST |
| CONTROL_STRESS_01 | KIMI_MOONSHOT | `3d53038db5511c2d12ea5638a840d19d34a0e8d9a6613b5d5f7ca1aee003f00c` | A_FIRST |

## 4. Execution shape

Primary planned evidence object:

```text
8 packets x 3 cold families x 2 arms = 48 manual model returns maximum for PAIR_ATTEMPT=1
24 A/T pairs
```

Execute each pair as close together as operationally practical, while still using fresh separate contexts. Pair identity and order are more important than global case ordering. Controls remain evidence about boundedness/firing, not real-world retention gains.

No dispatch has occurred merely because this plan exists.

```text
DISPATCH_PLAN_FROZEN != RECEIVER_CONTACT
RECEIVER_CONTACT != VALID_PAIR
VALID_PAIR != CONFIRMED_GAIN
```
