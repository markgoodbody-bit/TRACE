# TRACE v0.3.0 — SOURCE COLLECTION MANIFEST ATTACK v0.1

**Status:** PRE-FREEZE ATTACK — WORKING — NOT VALIDATION  
**Target:** `PROJECT/TRACE_v0_3_0_SOURCE_COLLECTION_MANIFEST_v0_1.md`  
**Date:** 2026-08-25

## Verdict

```text
ATTACKS: 15
MATERIAL FINDINGS: 3
NARROW / RESIDUAL LIMITS: 8
RESISTED: 4
VERDICT: REPAIR_BEFORE_FREEZE
```

## Material findings

### M1 — chronological `first 5` creates avoidable edge-of-year bias

The v0.1 intake rule takes the first five eligible items in canonical chronological order from every collection. That mechanically over-samples the beginning of the year and can cluster dense collections into a very narrow temporal slice.

This does not look like TRACE cherry-picking, but it is an unnecessary aperture distortion and is easy to remove before item reading.

Repair: derive a collection-specific deterministic start day from the already-frozen collection ID and year, then scan canonical order forward from that day with year-end wraparound until five eligible items are collected.

```text
START_HASH = SHA256(SOURCE_COLLECTION_ID + "\n2022")
START_DAY  = 1 + (uint32(first_8_hex(START_HASH)) mod 365)
```

This keeps selection mechanical without requiring case-content scoring.

### M2 — source persistence differs materially across collections

LGSCO states that ordinary decision statements are kept for five years, while public-interest reports are kept for ten. A 2022 source packet may therefore disappear from the live collection on a different schedule from FOS/EPA/RAIB/HSSIB material.

Repair: once selected, preserve exact source identity, retrieval date and a bounded frozen source packet/evidence pointer promptly. Do not treat later live disappearance as proof the source never existed.

```text
LIVE_COLLECTION_PERSISTENCE != SOURCE_EVENT_PERSISTENCE
LATER_UNAVAILABLE != NEVER_PUBLISHED
```

### M3 — NHTSA SGO inclusion is a reporting aperture, not a crash-population frame

NHTSA explicitly warns that reporting depends on telemetry, manufacturer awareness, incomplete/unverified reports, duplicate reports and non-normalized exposure. Treating SGO rows as a representative crash sample would be invalid.

Repair: the NHTSA arm is explicitly a **reported-incident structural sample**, not an incidence/risk-rate sample. Case packets must carry those reporting limitations and must not infer system causation from inclusion.

## Narrow / residual limits retained

### R1 — date semantics differ across source families

RAIB uses occurrence date; EPA document date; LGSCO/FOS/HSSIB decision/publication date; NHTSA crash occurrence month/year. This prevents naïve cross-collection temporal-rate comparison but does not block case-level structural analysis. Preserve source-native date semantics.

### R2 — RAIB full-investigation filter creates severity/completion bias

Full reports are selected because they provide a completed evidence/analysis record. They are not representative of all rail events. Keep this as a declared aperture, not a hidden assumption.

### R3 — HSSIB is already a selected subset of healthcare safety reality

HSSIB chooses which systemic issues to investigate under its own criteria. The collection therefore samples HSSIB-selected safety issues, not all NHS harm. Preserve that institutional selector.

### R4 — EPA mixes decision-document types

RODs, amendments and ESDs are not identical decision objects. Preserve document type in the case record; do not aggregate as one homogeneous intervention class.

### R5 — official-source bias

All six primary apertures are official/institutional sources. This improves provenance but can underrepresent affected-party accounts. Selected case packets should record that limitation and, after case identity is frozen, may add secondary public evidence under a separately frozen packet-construction rule. Official record is not the world.

### R6 — UK-heavy institutional mix

Four collections are UK and two US. This is a bounded cross-domain contact set, not a globally representative institutional sample. Do not generalise geographic prevalence.

### R7 — 2022 is a common aperture, not a representative year

The rationale survives the attack: 2022 is the earliest complete calendar year after the latest-starting source family (NHTSA SGO began in 2021) and avoids current-headline selection. But no representativeness claim follows.

### R8 — Framework has partial item exposure

Framework saw incidental item titles/summaries while verifying collection mechanics. v0.1 already records this. Framework therefore cannot count as a cold receiver or independent efficacy adjudicator.

## Resisted attacks

### A1 — known favourable 2022 case drove year choice

No evidence found. The year was chosen from source-family availability, before selected case identities.

### A2 — collection IDs can be renamed after seeing start positions

Repair must freeze the exact IDs before the start-date hashes are used. Once v0.2 is committed, IDs/start dates are immutable for this run.

### A3 — deterministic selection equals representative sampling

The manifest explicitly denies this. Keep the ceiling.

### A4 — six domains all require universal TRACE expansion

No. The expansion protocol already permits `NO_NEW_STRUCTURE_EARNED_ON_THIS_CASE`, derived/profile/tooling placement and over-fire containment. Cross-domain contact does not imply core accretion.

## Required repair before freeze

1. replace chronological first-five rule with deterministic collection-specific start day + forward/wrap scan;
2. add source-persistence/frozen-packet requirement;
3. strengthen NHTSA reported-incident ceiling;
4. carry residual aperture limitations explicitly;
5. do not change source families merely because the attack found limitations inherent to them.
