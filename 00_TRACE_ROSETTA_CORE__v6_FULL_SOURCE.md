# TRACE / Mechanical Ethics Diagnostic Kernel v0.2

Date: 2026-06-16  
Authoring context: Mark Goodbody with Framework (GPT-5.5 Thinking / OpenAI).  
Status: exploratory diagnostic tool; not validation; not a safety certification.

## v0.2 Change

v0.2 adds the **Predatory-System / Exit-Route Branch** exposed by the Harriet Tubman bootstrap and Concordance v0.4.

The original Kernel asks:

```trace
can_internal_correction_reach_harm_before_it_hardens?
```

v0.2 adds:

```trace
if official_system == harm_carrier:
  internal_review_is_not_enough
  test_exit_route + external_constraint + protected_subject_path
```

This is not a general anti-institution rule. It is a boundary branch for cases where the official channel is itself the source, carrier, or enforcer of harm.

## Core Question

Can correction reach the affected subject before harm hardens?

## Step 0 — System-Type Triage

Before running the K-gate, identify the system type.

| Question | Values | Meaning |
|---|---|---|
| Is the official channel plausibly corrigible? | yes / partial / no / unknown | Can internal review realistically alter the path? |
| Is the official channel itself the harm carrier? | yes / partial / no / unknown | Is the system enforcing, laundering, or preserving the harm? |
| Is using the official channel likely to increase risk? | yes / partial / no / unknown | Does appeal/reporting expose the subject to retaliation, capture, delay, or further loss? |
| Is there a viable external constraint or exit route? | yes / partial / no / unknown | Can protection come through independent authority, public exposure, sanctuary, external review, emergency support, or physical/digital exit? |

Branch rule:

```trace
if official_channel_harm_carrier == yes
  OR official_channel_increases_risk == yes:
    run Exit_Route_Branch
else:
    run Internal_Correction_K_Gate
```

## Internal Correction K-Gate

Use when the system is plausibly corrigible from inside.

| Gate | Question | Values |
|---|---|---|
| Witness | Can the affected subject and harm path be seen? | yes / partial / no / unknown |
| Record | Is there a trustworthy, contestable record? | yes / partial / no / unknown |
| Authority | Is there an actor with real authority to change the path? | yes / partial / no / unknown |
| Time | Can correction happen before hardening? | yes / partial / no / unknown |
| Enforcement | Can the correction bind the system? | yes / partial / no / unknown |
| Repair | Can the subject be restored or compensated in a way that matters? | yes / partial / no / unknown |

Compression:

```trace
K := W * R * A * Tm * E * Rp

if any_gate == no:
  correction_capacity_collapses_at_that_gate
```

Do not convert this into a numeric score without domain-specific measurement rules.

## Exit-Route Branch

Use when the official channel is unavailable, captured, predatory, or dangerous to the subject.

| Gate | Question | Values |
|---|---|---|
| Subject protection | Can the subject be protected from further exposure while action is taken? | yes / partial / no / unknown |
| External witness | Can evidence or testimony reach a witness outside the harm carrier? | yes / partial / no / unknown |
| Independent authority | Is there any actor outside the harmful channel with power to constrain it? | yes / partial / no / unknown |
| Route | Is there a practical path out of the harm state? | yes / partial / no / unknown |
| Safe secrecy | Does any necessary secrecy protect the subject rather than shield power? | yes / partial / no / unknown |
| Support | Are shelter, money, care, legal help, technical support, or continuity resources available? | yes / partial / no / unknown |
| Time | Can the route/protection beat capture, lock-in, retaliation, or irreversible hardening? | yes / partial / no / unknown |

Compression:

```trace
Exit_Capacity :=
  subject_protection
  * external_witness
  * independent_authority
  * route
  * safe_secrecy
  * support
  * time
```

If the official system is predatory and `Exit_Capacity` is low, the case is high-risk even if formal process exists.

## Context Flags

| Flag | Meaning | Values |
|---|---|---|
| H_immediacy | How quickly harm hardens if uncorrected | 1 latent / 2 cumulative / 3 rapid serious / 4 immediate catastrophic |
| P_trigger | Correction-dependence / trigger-independence | 1 independent trigger / 2 mixed / 3 actor-controlled |
| E_scale | Scope or scale of affected subjects/actions | qualitative or log10(units) where measurable |
| Exposure risk | Risk created by using the official channel | low / medium / high / unknown |
| Exit feasibility | Practicality of route out of harm state | low / medium / high / unknown |

## Output Labels

| Label | Meaning |
|---|---|
| PASS-LIMITED | Correction or exit route appears live before hardening, with visible limits. |
| PARTIAL | Some gates work; one or more gates are weak or uncertain. |
| FAIL | Correction/exit cannot reach harm before hardening. |
| UNKNOWN | Insufficient evidence to assess. |
| FORBIDDEN / HALT | Action should not proceed because it creates irreversible harm without live correction/exit path. |

## Minimal Use

One case. One page. No false precision.

1. Identify system type.
2. Run either Internal Correction K-Gate or Exit-Route Branch.
3. Answer the clock question.
4. Record context flags.
5. State one failure point and one repair move.

## Guardrails

This Kernel must not claim:

- safety certification;
- validation of TRACE;
- superiority to expert review;
- that all internal process is useless;
- that secrecy is generally good;
- that exit is always possible;
- that numerical scores are meaningful without measurement rules.

## One-Line Compression

```trace
Kernel_v0_2 :=
  if system_corrigible:
    test_correction_before_hardening
  else_if system_predatory:
    test_exit_route_before_capture
```
