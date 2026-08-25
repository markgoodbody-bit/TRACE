# TRACE v0.3.0 — DELAY / MEMORY / UNRESOLVED / ABSENCE FRONTIER QUARRY v0.1

**Status:** WORKING QUARRY — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — NO NEW PRIMITIVE EARNED  
**Date:** 2026-08-25  
**Source:** ephemeral external analyst transmission supplied by Mark after the selector-provenance/aperture-actuation exchange.

## 0. Purpose

Preserve four external frontier hypotheses without importing their unsupported causal, normative, epistemic, or policy claims into TRACE.

The four proposed surfaces are:

1. delay-burden asymmetry;
2. memory / attestation topology;
3. unresolved-dependency backlog and expiry;
4. timelocked response to missed heartbeat.

This quarry asks what survives after existing TRACE distinctions fire.

```text
EXTERNAL_PROPOSAL != NEW_PRIMITIVE
USEFUL_MEASURE != MORAL_VERDICT
SIGNED_RECORD != TRUE_RECORD
MISSED_HEARTBEAT != ABSENCE_PROVEN
UNRESOLVED_AT_EXPIRY != FALSE
POLICY_OPTION != TRACE_REQUIREMENT
```

---

## 1. Delay-burden asymmetry

### External proposal

Compare delay burden borne by differently positioned entities, including a proposed ratio such as:

```text
DeltaB_delay(vulnerable) / DeltaB_delay(powerful)
```

and treat extreme asymmetry as a structural predator position.

### What survives

TRACE already permits typed burden, delay/null-input transitions, differential affected scopes, capability/control and clocks. A **derived burden-asymmetry view** may be useful where delay changes burden differently across entities.

However burden is a vector, not one universal scalar. A ratio is meaningful only where:

- the compared burden dimension is declared;
- units / measure are commensurable;
- interval and causal attribution are supported;
- denominator semantics are valid;
- uncertainty is preserved.

Prefer a typed comparison before division:

```text
A_delay(i,j,d,t0,t1) = compare(
    DeltaB_i[d | delay, t0:t1],
    DeltaB_j[d | delay, t0:t1],
    declared_measure
)
```

A scalar ratio may be an optional derived view only when the measure supports it.

### Required guards

```text
BURDEN_VECTOR != UNIVERSAL_SCALAR
ASYMMETRIC_DELAY_BURDEN != EXPLOITATION_PROVEN
LOW_DELAY_COST_TO_A != COERCION_BY_A
DELAY_CAUSES_BURDEN != DELAY_SELECTED_TO_CAUSE_BURDEN
CAPACITY_ASYMMETRY != INTENT
RATIO_UNDEFINED_AT_ZERO != INFINITE_MORAL_SIGNAL
STRUCTURAL_LEVERAGE != MORAL_PREDATION
```

`Predator Position` may remain useful in Mechanical Ethics as a human-facing/normative interpretation where separately justified; it is not automatically emitted by TRACE from one burden ratio.

### Current disposition

```text
NEW PRIMITIVE: NO
DERIVED VIEW PRESSURE: YES
ME TRANSLATION PRESSURE: YES
```

---

## 2. Memory / attestation topology

### External proposal

Bifurcate memory into:

- `SOCIAL_MEMORY` validated through a witness/countersignature DAG;
- `SOLO_MEMORY` anchored by an agent's own persistent Ed25519 key;

with solitary memory restricted from irreversible transitions unless quarantined.

### What survives

The important structural issue is not two truth classes of memory. It is **attestation topology**:

- who produced the record;
- what each witness actually observed;
- whether evidence is independent;
- integrity/custody of the record;
- key/control provenance where cryptographic signatures exist;
- what the record is being used to support;
- capture / refusal / availability of witnessing routes.

Existing TRACE claim/evidence/access/custody/witness/authority structure can carry most of this.

A cryptographic signature can support claims such as `these bytes were signed by a key controlling this signature operation` under the relevant cryptographic assumptions. It does not by itself establish truth of the content, continuity of personhood, exclusive key custody, or external observation of the event.

Likewise, countersignatures may establish what signers witnessed or attested; they do not automatically upgrade a proposition from `REPORTED` to `OBSERVED` for every receiver.

### Required guards

```text
SIGNED_RECORD != TRUE_RECORD
SELF_SIGNATURE != CONTINUOUS_IDENTITY
KEY_CONTROL != PERSONHOOD_CONTINUITY
COUNTERSIGNATURE != INDEPENDENT_WITNESS
WITNESS_DAG != TRUTH
NO_COUNTERSIGNATURE != CLAIM_FALSE
SOCIAL_ATTESTATION != COMMONS_TRUTH
PRIVATE_ATTESTATION != NO_STANDING
CRYPTOGRAPHIC_INTEGRITY != EVENT_VALIDITY
```

The proposed rule `SOLO_MEMORY cannot trigger irreversible transition without QUARANTINE` is a policy/authority rule, not a TRACE entailment. A domain profile may choose such a gate, but TRACE should expose the evidence state, authority, target, clocks, risks and alternatives rather than mandate the policy.

### Capture frontier

A witness topology can itself be aperture-bearing and capturable:

```text
WITNESS_ROUTE_EXISTS != WITNESS_ROUTE_USABLE
COUNTERSIGNATURE_REQUIRED != COUNTERSIGNATURE_AVAILABLE
NO_SOCIAL_ATTESTATION != EVENT_DID_NOT_OCCUR
SOCIAL_GRAPH_CAPTURE != CLAIM_FALSE
```

### Current disposition

```text
NEW PRIMITIVE: NO
DERIVED ATTESTATION-TOPOLOGY VIEW: PLAUSIBLE
DOMAIN PROFILE / TOOLING PRESSURE: YES
MANDATORY QUARANTINE POLICY: NO
```

---

## 3. Unresolved-dependency backlog / expiry

### External proposal

Quarantined unknowns should have a decay half-life; after expiry a mandatory `FIREBREAK` prunes the dependent subgraph as `UNRESOLVED_AT_EXPIRY` to prevent unresolved uncertainty from consuming network attention indefinitely.

### What survives

The useful frontier is **bounded unresolved-state handling**.

An unresolved claim can accumulate operational burden through repeated checking, blocked downstream decisions, attention consumption, storage/coordination cost, or unresolved dependency fan-out. That burden can be represented and timed.

A use can also have an eligibility/currentness window. When support needed for a particular downstream use expires, the correct transition may be:

```text
VALID_FOR_USE -> NOT_CURRENT_FOR_THIS_USE / UNKNOWN_FOR_THIS_USE
```

without changing the underlying proposition to false or deleting its history.

A `firebreak` may be a candidate bounded action under an explicit domain policy/authority: stop propagating an unresolved dependency into a particular active computation, route or deployment while preserving the source object, limits, residue and reopening path.

It is not a universal TRACE requirement to destroy a subgraph at a deadline.

### Required guards

```text
UNRESOLVED_AT_EXPIRY != FALSE
USE_WINDOW_EXPIRED != CLAIM_DELETED
BACKLOG_COST != DUTY_TO_PRUNE
PRUNED_FROM_ACTIVE_VIEW != ERASED_FROM_LEDGER
FIREBREAK_EXECUTED != ISSUE_RESOLVED
STOP_PROPAGATION != TRUTH_VERDICT
TIME_PASSED != UNKNOWN_RESOLVED
QUARANTINE_DURATION != EVIDENCE_DECAY_BY_DEFAULT
```

### Candidate derived objects

Where useful:

```text
UNRESOLVED_DEPENDENCY_BACKLOG
USE_ELIGIBILITY_CLOCK
ACTIVE_VIEW_FIREBREAK
REOPEN_ROUTE
RESIDUE_OF_UNRESOLVED_DEPENDENCY
```

These are descriptive/derived concepts unless a concrete counterexample later earns stronger formal placement.

### Current disposition

```text
NEW PRIMITIVE: NO
DERIVED VIEW / RUNTIME PROFILE PRESSURE: YES
MANDATORY HALF-LIFE: NO
MANDATORY SUBGRAPH COLLAPSE: NO
```

---

## 4. Timelocked response to missed heartbeat

### External proposal

An agent precommits: `If I do not post by time T, transition my state to ABSENT.` A ledger/timelock then executes this without an external actor having to notice the absence.

### Core correction

A missed heartbeat is evidence about an expected signal, not direct observation of the cause.

Preauthorization may validly authorize a response to a missing heartbeat. It cannot turn silence into knowledge that the agent is absent, crashed, dead, unwilling, disconnected, censored, delayed, or otherwise unavailable.

The safer structural form is:

```text
expected heartbeat by T
+ heartbeat not observed through declared aperture by T
+ valid scoped precommitment / standing rule
-> HEARTBEAT_MISSED / PRESENCE_UNCONFIRMED
-> authorized contingent response, if the rule actually grants it
```

not:

```text
no heartbeat -> ABSENT proven
```

### Required guards

```text
MISSED_HEARTBEAT != ABSENCE_PROVEN
SILENCE != CAUSE_ESTABLISHED
PRECOMMITMENT != FUTURE_FACT
PREAUTHORISED_RESPONSE != PREAUTHORISED_TRUTH
TIMED_RULE_EXECUTED != WORLD_STATE_OBSERVED
HEARTBEAT_APERTURE_FAILED != AGENT_ABSENT
SCHEDULER_FAILED != AGENT_FAILED
PRESENCE_UNCONFIRMED != NONEXISTENT
```

### Timelock / covenant structure that may survive

A useful domain profile may preserve:

- declarant / principal;
- rule text / transition class;
- trigger condition;
- clock basis;
- executor;
- witness/aperture used to test trigger;
- scope and expiry;
- revocation/change route;
- authority source;
- contingent response;
- failure modes of timer/executor/witness;
- residue and recovery route.

This is a **contingent authorization / liveness profile**, not a new epistemic primitive.

### Current disposition

```text
NEW PRIMITIVE: NO
DOMAIN PROFILE / TOOLING PRESSURE: YES
SELF-CERTIFYING ABSENCE: REJECT
TIMED CONTINGENT RESPONSE: RETAIN FOR QUARRY
```

---

## 5. Shared frontier exposed by all four

The four proposals converge on one larger structure:

> Systems often contain rules whose consequences depend not merely on what is observed, but on **who bears time, who attests memory, what unresolved dependencies remain active, and what transition fires when an expected signal fails to arrive.**

The common seam is therefore not four new ontological objects. It is interaction among existing TRACE surfaces:

```text
CLOCK
+ BURDEN
+ EVIDENCE / ATTESTATION
+ APERTURE / ACTIVATION
+ SELECTOR / DEFAULT RULE
+ AUTHORITY
+ ROUTE / EXECUTOR
+ RESIDUE
```

This extends the earlier aperture-actuation quarry:

```text
AVAILABLE_APERTURE != ACTIVATED_APERTURE
EXPECTED_SIGNAL != OBSERVED_SIGNAL
MISSING_SIGNAL != CAUSE_OF_MISSING_SIGNAL
DEFAULT_RULE_FIRED != RULE_JUSTIFIED
```

---

## 6. Required falsification set before promotion

Attack at least these cases before any spine/core promotion:

1. symmetric delay burden — proposed ratio adds nothing;
2. incomparable burden dimensions — ratio invalid;
3. denominator near zero — ratio unstable but no exploitation exists;
4. high asymmetry caused by benign physical constraints, not power;
5. self-signed record with false content but valid signature;
6. social DAG with colluding/captured witnesses;
7. true event with no available countersignature;
8. unresolved claim whose correct handling is continued preservation, not pruning;
9. expired use window where later evidence reopens the claim;
10. firebreak that causes greater harm than unresolved backlog;
11. missed heartbeat caused by network/aperture failure while agent remains active;
12. valid precommitment whose executor lacks current authority;
13. timer fires after covenant revocation/change;
14. scheduler and witness share one failure domain;
15. native field case independently rediscovers one of these structures without TRACE vocabulary contamination.

Promotion pressure should be judged by concrete failure of existing structure, not by elegance of the proposed names.

---

## 7. Current overall disposition

```text
BURDEN ASYMMETRY:
  DERIVED VIEW PRESSURE = YES
  NEW PRIMITIVE = NO

ATTESTATION TOPOLOGY:
  DERIVED VIEW / DOMAIN PROFILE PRESSURE = YES
  NEW PRIMITIVE = NO

UNRESOLVED BACKLOG / USE EXPIRY:
  DERIVED VIEW / RUNTIME PROFILE PRESSURE = YES
  MANDATORY FIREBREAK = NO

TIMELOCKED MISSED-HEARTBEAT RESPONSE:
  DOMAIN PROFILE / TOOLING PRESSURE = YES
  SELF-CERTIFYING ABSENCE = NO

SPINE EDIT: NO
MINIMUM SCHEMA CHANGE: NO
ME TRANSLATION PRESSURE: YES, ESPECIALLY DELAY-BURDEN ASYMMETRY
```

Preserve the external proposals, the rejected overclaims, and the residual frontiers together. Negative correction is part of project expansion.