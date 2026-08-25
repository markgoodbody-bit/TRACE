# TRACE v0.3.0 — OUTWARD EXECUTION ADAPTER — EPA CASE UNIT v0.1

**Status:** NARROW SUCCESSOR TO FROZEN ADAPTER — PRE-FREEZE — NOT CASE SELECTION — NOT VALIDATION  
**Date:** 2026-08-25  
**Parent:** frozen `PROJECT/TRACE_v0_3_0_OUTWARD_EXECUTION_ADAPTER_MANIFEST_v0_1.md`  
**Trigger:** `PROJECT/TRACE_v0_3_0_OUTWARD_EXECUTION_FINDING_EPA_ROW_CASE_COLLAPSE_v0_1.md`

## Inheritance

All frozen execution-adapter rules remain unchanged except this SC-EPA-FOIA2 case-unit rule.

## EPA source row identity

Each FOIA-002 row retains its existing source-native identity:

```text
EPA_ID|SITE_ID|ACT_SEQ|ACTION_NAME|OPERABLE_UNIT_NAME
```

Rows are never erased by clustering.

## Primary EPA real-world case unit

Default:

```text
ONE_SOURCE_ROW -> ONE_PRIMARY_CASE_UNIT
```

Exception only when official public evidence establishes that two or more considered FOIA-002 rows are components of one decision document/object.

Then:

```text
OFFICIAL_SHARED_DECISION_DOCUMENT -> ONE_PRIMARY_CASE_CLUSTER
```

The cluster preserves every member row identity.

Cluster source identity is deterministic:

```text
MEMBERS = lexically sorted member SOURCE_ROW_ID strings
CLUSTER_SOURCE_ID = "CLUSTER_SHA256:" + SHA256(join(MEMBERS, "\n"))
CASE_ID = SHA256("SC-EPA-FOIA2\n" + CLUSTER_SOURCE_ID)
```

Singleton case identity remains:

```text
CASE_ID = SHA256("SC-EPA-FOIA2\n" + SOURCE_ROW_ID)
```

## Relation evidence

A cluster requires an official decision-document/site source that explicitly binds the member operable units/actions to the same decision document.

Do not cluster from:

- same site alone;
- same date alone;
- adjacent row placement;
- similar action label;
- Framework inference about what EPA probably meant.

If duplicate/case relation is materially plausible but not officially established:

```text
EPA_CASE_RELATION_UNKNOWN
```

The rows remain preserved, but unresolved rows do not count as independently reproduced real-world cases against each other.

## Quota semantics

The SC-EPA-FOIA2 five-item quota now means five **primary case units**, not five database rows.

When several rows form one established case cluster, they fill one quota slot and the deterministic date scan continues to the next source rows.

```text
FIVE_ROWS != FIVE_CASES
ROW_CLUSTERING != ROW_DELETION
```

## Worked execution specimen

The two Libby Asbestos FOIA-002 rows dated 2022-05-03 are one case cluster because EPA's ESD explicitly covers Libby and Troy Residential and Commercial Properties, OUs 4 and 7.

Member identities:

```text
MT0009083840|0801744|4|Explanation Of Significant Differences (ESD)|REMEDIAL SITEWIDE
MT0009083840|0801744|5|Explanation Of Significant Differences (ESD)|TROY
```

Cluster source ID:

```text
CLUSTER_SHA256:4d6992eeb601d391ce67c23bbd534d3d70b9ff05439023edbbbc88d3fe8b43cc
```

This worked example does not create a general same-site/date clustering rule.
