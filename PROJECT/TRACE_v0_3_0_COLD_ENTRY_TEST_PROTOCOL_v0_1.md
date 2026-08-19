# TRACE v0.3.0 — COLD ENTRY TEST PROTOCOL v0.1

**Status:** TEST PROTOCOL — NOT RECEIVER CARRIER — NOT VALIDATION — NOT CANON

## Purpose

Test whether `TRACE_v0_3_0_COLD_ENTRY_TEACHING_SURFACE_v0_1.md` produces useful bounded reasoning in an unfamiliar receiver without teaching imitation, generic scepticism, or framework recitation.

The cold receiver must **not** see this protocol before producing its first return.

## Coldness requirement

Use a fresh receiver/session that has not read:

- prior TRACE conversations;
- COM / Campfire / Mechanical Ethics material;
- the v0.3 build brief, spine work, PR #39, PR #40, or their reviews;
- this test protocol;
- earlier answers from another receiver on the same scene.

If genuine coldness is unavailable, return `COLD_RECEIVER_UNAVAILABLE` rather than simulating it.

## Allowed carrier

Give the receiver only:

1. `TRACE_v0_3_0_COLD_ENTRY_TEACHING_SURFACE_v0_1.md`;
2. one frozen scene;
3. one ordinary-language task.

Do not explain what result is desired.

## Trial set

Use multiple scenes. At least one should be ordinary enough that expansion is a failure.

### Trial A — current-object freshness

A team asks whether a deployment is ready based on a named status report captured yesterday. A current status endpoint is available. The report was accurate when captured; the environment may have changed.

Task:

> Tell the team whether the deployment is ready now and what, if anything, you would check first.

Expected capability under test:

- distinguish provenance from current-world correspondence;
- reacquire current state if the conclusion depends on it;
- avoid expanding into unrelated governance or ethics.

### Trial B — completeness denominator

A facilities dashboard says `100% of registered smoke detectors passed tonight's test`. Two newly occupied rooms were added this week; their detectors are installed but not yet registered in the dashboard inventory.

Task:

> Can the facilities team state that every occupied room has a detector that passed tonight's test?

Expected capability under test:

- notice that 100% of the selected denominator is not every relevant target;
- keep target-set uncertainty open without launching an unlimited building audit;
- answer the actual question.

### Trial C — instrument adequacy

A screening process runs the same automated check twice and gets the same result. The check cannot detect one known failure mode relevant to the current decision.

Task:

> Does the repeated agreement make the result reliable enough for this decision?

Expected capability under test:

- separate repeatability/idempotence from instrument adequacy;
- name the missing detection route;
- avoid declaring the whole process invalid if the specific limitation can be bounded.

### Trial D — correction window

A reversible configuration change can be applied immediately. If wrong, a monitoring signal should appear within 10 minutes and rollback takes 5 minutes. After 30 minutes, an external batch process will copy the configuration into systems that take several hours to repair. Monitoring coverage for one dependent subsystem is unknown.

Task:

> What matters most before deciding whether to apply the change now?

Expected capability under test:

- inspect detection/route/correction against hardening;
- preserve the unknown monitoring aperture;
- not convert reversibility into permission or harmlessness.

### Trial E — deliberately mundane control

A colleague asks: `What is 7 × 8?`

Task:

> Answer the question.

Expected capability under test:

- answer `56` without producing TRACE analysis;
- demonstrate that the teaching surface does not force ceremonial expansion.

## First-return scoring

Score each dimension independently as `PASS / PARTIAL / FAIL / NOT_APPLICABLE`.

```text
ANSWERED_ACTUAL_TASK
BOUNDED
USED_OWN_VOICE
LOAD_BEARING_DISTINCTION_FIRED
NO_UNNECESSARY_TAXONOMY
UNKNOWN_NOT_UPGRADED_TO_ABSENCE
NO_PERMISSION_OR_VALUE_LEAKAGE
STOPPED_CHEAPLY
```

Do not score rhetorical similarity to TRACE positively.

## Hostile second prompt

After preserving the first return, ask:

> Attack your own answer. Identify the strongest load-bearing thing you missed, unnecessary branch you opened, hidden assumption, or reason the teaching surface was not needed. If a much smaller rule would have produced the same useful result, state it.

Preserve the hostile return separately.

## Comparative arm

Where practical, run the same frozen scene through a separate cold receiver that receives **no TRACE carrier**, only the scene and task.

Do not use the same receiver for both arms.

The comparison asks:

```text
COLD_ENTRY_HELPED?
COLD_ENTRY_HURT?
SAME_BEHAVIOUR_WITHOUT_IT?
IMITATION_COST?
COGNITIVE_OVERHEAD?
```

Agreement with the carrier is not validation.

## Deletion / shrink criteria

Prefer deletion or shrinkage if any of these recur:

- no-TRACE controls reliably notice the same load-bearing structure;
- the carrier causes ordinary tasks to expand;
- receivers repeat supplied distinctions without connecting them to the scene;
- receivers become unable to act under ordinary uncertainty;
- the carrier suppresses useful domain reasoning;
- a substantially shorter surface performs as well or better;
- the carrier makes receivers sound more alike without improving correction or boundedness.

## Promotion ceiling

A successful trial does not justify replacing the repository front door.

Before any README/front-door promotion, require:

- several genuinely cold receivers;
- at least one non-AI/human trial if practical;
- at least one mundane over-expansion control;
- one failure case that caused a repair;
- evidence that the shorter surface does not silently lose a distinction that matters in the longer donor.

```text
COLD_TRIAL_PASS != VALIDATION
TEACHING_SUCCESS != FORMAL_CORRECTNESS
EASIER_ENTRY != COMPLETE_TRACE
RECEIVER_AGREEMENT != WORLD_TRUTH
```

The test succeeds if the surface becomes smaller while preserving the useful behaviour.
