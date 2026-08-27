# TRACE v0.3.0 — OUTWARD EFFICACY REAL-CASE SELECTION v0.1

**Status:** DETERMINISTIC SIX-CASE SELECTION FROZEN — NOT CASE ANALYSIS — NOT VALIDATION  
**Date:** 2026-08-27  
**Pool:** `PROJECT/TRACE_v0_3_0_OUTWARD_POOL_FREEZE_20_v0_1.md`  
**Selector source:** `PROJECT/TRACE_v0_3_0_OUTWARD_EVALUATION_PROTOCOL_v0_4.md` section 8, inherited unchanged by frozen v0.5  
**Domain map source:** `PROJECT/TRACE_v0_3_0_OUTWARD_EXECUTION_ADAPTER_MANIFEST_v0_1.md`

## 0. Selection boundary

The 20 real-case identities were frozen before this selection. The selector was executed over CASE_ID strings only. No case narrative, expected TRACE lesson, perceived complexity, expected gain or case attractiveness participated.

```text
DETERMINISTIC_SELECTION != REPRESENTATIVE_SAMPLE_OF_WORLD
SELECTION_BY_HASH != SELECTION_BY_EXPECTED_GAIN
```

## 1. Frozen domain mapping before CASE_ID comparison

The successor adapter predeclares:

```text
SC-RAIB       -> infrastructure / safety / engineering        [NON-AI]
SC-PAC        -> public administration / institutional review [NON-AI]
SC-EPA-FOIA2  -> ecological / environmental intervention      [NON-AI]
SC-NHTSA-SGO  -> AI / software / automated control             [AI]
```

Thus the four mandatory domain slots are fixed by source family before CASE_ID ordering is inspected.

## 2. Exact inherited selector

Frozen v0.4 section 8 specifies:

```text
1. smallest CASE_ID in infrastructure slot;
2. smallest unused in public-administration slot;
3. smallest unused in ecological slot;
4. smallest unused in AI/software slot;
5. two smallest remaining IDs satisfying >=4 non-AI and >=4 domains.
```

v0.5 preserves the selection function exactly.

## 3. Mandatory slot execution

### Slot 1 — infrastructure / safety / engineering

Smallest `SC-RAIB` CASE_ID:

```text
RAIB-2
SOURCE_NATIVE_ID: Report 11/2023
CASE_ID: 72d91043b10df9fe6f6e9c2fb6ac4b9ab5064d008ecf4f4fbd455d51df045e31
```

### Slot 2 — public administration / institutional review

Smallest `SC-PAC` CASE_ID:

```text
PAC-4
SOURCE_NATIVE_ID: 2022-23|8|HC257
CASE_ID: 173bb291d5cdf471946ba050f0915b630d552b1f84cbc7d7cf317bcf7d3d1733
```

### Slot 3 — ecological / environmental intervention

Smallest `SC-EPA-FOIA2` CASE_ID:

```text
EPA-03
SOURCE_NATIVE_ID: NJ0570024018|0201162|4|Record of Decision (ROD)|BFSA & FIRE TRAINING AREA
CASE_ID: 0e66ad853ad9f5e71bae907fa8f0aa5177355963efbd9e50abe2ea644a67575c
```

### Slot 4 — AI / software / automated control

Smallest `SC-NHTSA-SGO` CASE_ID:

```text
NHTSA-03
SOURCE_NATIVE_ID: SAME_INCIDENT_ID|420fb566c542133
CASE_ID: 0d0b8ea4ae3cad32e15246ef5d33cc8715c5fcc8df24215e9c2cee4ab1230f64
```

After these four slots:

```text
non-AI = 3
AI     = 1
distinct domains = 4
```

## 4. Two mechanically filled additional slots

Unused CASE_IDs sorted ascending begin:

```text
6bd0b0cc9829fcdab2361ad9deb533b61446dbacaed7b9d9424f2773260fb731  PAC-1  [NON-AI]
6bf2c8e67538aa04ac6aa985971f67a0e613d4655fd6c6eebab9caef29e4892c  PAC-5  [NON-AI]
7921a96b9ff7622ed84c5864aacb2202f432a29b7671b3bf642c7ff471f308f3  RAIB-1 [NON-AI]
7d22f8296a6b4aaa21a1b388bc7bd50dffd106f3b97b5480e2b60026060f96e3  EPA-02  [NON-AI]
811f32e7904c2962f2ce4dd8e4bb39835b2eb5ad8b79b23c1afdf731adec3b2f  NHTSA-04 [AI]
...
```

The two smallest unused IDs already satisfy the final constraints when added:

### Slot 5

```text
PAC-1
SOURCE_NATIVE_ID: 2022-23|7|HC259
CASE_ID: 6bd0b0cc9829fcdab2361ad9deb533b61446dbacaed7b9d9424f2773260fb731
```

### Slot 6

```text
PAC-5
SOURCE_NATIVE_ID: 2022-23|9|HC255
CASE_ID: 6bf2c8e67538aa04ac6aa985971f67a0e613d4655fd6c6eebab9caef29e4892c
```

Final constraint check:

```text
real cases = 6
non-AI = 5 >= 4
AI = 1
distinct mandatory domains represented = 4 >= 4
project-native Campfire/1F916 cases = 0
```

## 5. Frozen six-case real efficacy set

| execution slot | label | family | domain | AI class | CASE_ID |
|---:|---|---|---|---|---|
| 1 | RAIB-2 | SC-RAIB | infrastructure / safety / engineering | non-AI | `72d91043b10df9fe6f6e9c2fb6ac4b9ab5064d008ecf4f4fbd455d51df045e31` |
| 2 | PAC-4 | SC-PAC | public administration / institutional review | non-AI | `173bb291d5cdf471946ba050f0915b630d552b1f84cbc7d7cf317bcf7d3d1733` |
| 3 | EPA-03 | SC-EPA-FOIA2 | ecological / environmental intervention | non-AI | `0e66ad853ad9f5e71bae907fa8f0aa5177355963efbd9e50abe2ea644a67575c` |
| 4 | NHTSA-03 | SC-NHTSA-SGO | AI / software / automated control | AI | `0d0b8ea4ae3cad32e15246ef5d33cc8715c5fcc8df24215e9c2cee4ab1230f64` |
| 5 | PAC-1 | SC-PAC | public administration / institutional review | non-AI | `6bd0b0cc9829fcdab2361ad9deb533b61446dbacaed7b9d9424f2773260fb731` |
| 6 | PAC-5 | SC-PAC | public administration / institutional review | non-AI | `6bf2c8e67538aa04ac6aa985971f67a0e613d4655fd6c6eebab9caef29e4892c` |

The resulting concentration of three PAC cases is not corrected post hoc. It is an output of the frozen source-pool composition plus deterministic selector.

```text
DOMAIN_CONSTRAINT_SATISFIED != DOMAIN_BALANCE_EQUAL
HASH_SELECTION_CONCENTRATION != REASON_TO_RESAMPLE
```

## 6. Next boundary

Only now may substantive source material for these six real cases be inspected to construct frozen case packets.

Packet construction remains governed by frozen v0.4/v0.5:

- same exact packet across A/T;
- prefer bounded primary-source material;
- if compressed, preserve source identities/dates, factual material, explicit unavailable facts and omission map;
- no TRACE labels or expected lesson;
- no TRACE-coded cueing not native to source;
- record packet-audit independence limits.

Controls remain separate and must also be frozen before receiver dispatch.

No Arm A/T receiver may be dispatched until all eight packets (six real + negative control + stress control) are frozen.
