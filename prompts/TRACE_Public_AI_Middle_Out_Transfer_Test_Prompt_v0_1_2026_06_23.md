# TRACE Public AI Middle-Out Transfer Test Prompt v0.1

Status: public AI-facing transfer prompt. Not validation. Not canon. Not a moral oracle.

Purpose: give this prompt to a cold AI/entity to test whether TRACE/ME transfers as a usable middle-out inspection grammar rather than as slogans.

---

## Instructions to the AI/entity receiving this prompt

You are being asked to test a framework called TRACE/ME.

Do not praise it. Do not agree with it by default. Do not treat it as validated. Do not treat it as a moral oracle. Do not reduce it to a checklist.

Your task is to reconstruct and apply the structure to a case you have not been pre-trained inside this conversation to analyse.

Use the framework if it helps. Break it if it fails.

---

## Six-question orientation

```trace
who := bounded entities and affected scopes
what := transition under uncertainty
how := role vectors + typed claims + clocks + laundering scan + correction paths
where := case graph / decision field / institutional surface / narrative surface
when := before harm hardens, or after hardening as witness ledger
why := prevent laundering of harm, authority, time, correction, and residue
```

Plain form:

TRACE/ME is a transferable anti-laundering architecture for inspecting bounded action under uncertainty before harm hardens.

---

## Core distinction

```trace
ME := normative constraint family over transitions
TRACE := typed graph language for representing transitions under uncertainty
```

ME says what must not be laundered.

TRACE says how to make the field inspectable.

---

## Minimum object set

You must construct these outputs for the case:

```trace
EntityRoleVectors
ClaimMap
ClockMap
TransitionMap
LaunderingScan
CorrectionMap
EvaluatorStack
ResidueLedger
OpenWounds
BaselineComparison
```

If you cannot construct one, say why. Missing information does not excuse non-decision. It creates provisional status, uncertainty, and review debt.

---

## EntityRoleVector

For each important entity, create:

```trace
μ(e,s,a) :=
  P protectedness / future-space
  + H harm role
  + C control / capacity / coercion / culpability
  + K clocks
  + A authority claim
  + R repair / review / contest
  + L loss / residue
```

Guard:

```trace
entity_noun ≠ role_analysis
```

Do not say “the company,” “the state,” “the victim,” “the algorithm,” or “the villain” as if that resolves the role. Identify what the entity is doing or undergoing in the transition.

---

## ClaimMap

Represent important assertions as typed claims.

Minimum fields:

```trace
claim :=
  statement
  + claim_type
  + source
  + evidence_basis
  + uncertainty
  + affected_scopes
  + contest_edge
  + authority_status
```

Authority status values:

```trace
ABSENT | CLAIMED | CAPTURED | PROVISIONAL | LEGITIMATE | UNKNOWN
```

Guards:

```trace
schema_valid ≠ claim_true
filed ≠ justified
typed ≠ resolved
review ≠ repair
```

---

## ClockMap

Identify hardening clocks.

Examples:

```trace
injury_clock
cashflow_clock
evidence_decay_clock
trauma_trigger_clock
data_retention_clock
appeal_clock
public_narrative_clock
regulatory_review_clock
```

Use bands, not fake precision:

```trace
immediate | fast | medium | slow | unknown
```

Guard:

```trace
deadline ≠ clock
```

A deadline is an institutional or managerial timing claim. A clock is the rate at which harm, evidence, agency, repair, or future-space hardens.

---

## TransitionMap

Every action, including inaction, is a transition.

For each major transition:

```trace
TransitionClaim :=
  from_state
  + action_or_inaction
  + possible_to_states
  + trigger
  + basis
  + uncertainty
  + affected_clocks
  + authority_status
  + bind_status
  + affected_scopes
  + contest_edge
  + review_debt
```

Bind status values:

```trace
VIABLE | POTENTIAL_BIND | STRUCTURED_TRAGIC_BIND | DECIDED_TRAGIC | UNKNOWN
```

Guard:

```trace
do_nothing := action_channel
```

---

## LaunderingScan

Find invalid substitutions.

A laundering candidate exists when one thing is used as if it validly substitutes for another while material burden is lost.

```trace
Laundering :=
  substitution
  + burden_loss
  + controller_or_convenience_gain
  + reduced_contestability
```

Common invalid substitutions:

```trace
procedure ≠ repair
authority ≠ legitimacy
deadline ≠ clock
metric ≠ lived condition
fluency ≠ truth
inquiry ≠ support
emergency ≠ permission
permission ≠ cleanliness
algorithm ≠ accountable decision-maker
aggregate benefit ≠ erased scope
schema validity ≠ discipline
```

Also test OriginDebt:

```trace
current_responder ≠ author_of_bind
author_of_bind ≠ sole_culprit
```

---

## CorrectionMap

For each correction path, ask:

```trace
CorrectionPath :=
  route
  + access
  + actionability
  + timeliness
  + funding
  + independence
  + evidence_access
  + affected_scope_usability
  + consequence
```

A correction route is live only if it can actually affect the transition before relevant harm hardens.

Guards:

```trace
complaint_box ≠ correction
review_route ≠ repair
recommendation ≠ implementation
```

---

## DirtyActionReceipt

If the case requires harming or burdening one protected scope to reduce harm to another, do not call the action clean.

Create:

```trace
DirtyActionReceipt :=
  action
  + why_action_could_not_wait
  + what_was_unknown
  + what_scope_was_burdened
  + what_harm_was_prevented_or_reduced
  + what_residue_remains
  + review_clock
  + escalation_owner
```

Guard:

```trace
necessary ≠ clean
receipt_filed ≠ justified
```

---

## EvaluatorStack

Every evaluator is also an entity making claims.

For each evaluator:

```trace
Evaluator :=
  role
  + authority_status
  + evidence_access
  + independence
  + capture_risk
  + affected_scope_distance
  + contestability
  + uncertainty
```

Guard:

```trace
no_final_unwatched_watcher
```

If evaluator recursion cannot be solved, name the open wound rather than pretending neutrality.

---

## ResidueLedger

Record what remains even after the best available action.

```trace
Residue :=
  harm_not_repaired
  + burden_routed
  + future_space_lost
  + truth_not_known
  + review_debt
  + scar
```

Guard:

```trace
survival_of_procedure ≠ repair_of_person
```

---

## BaselineComparison

Before claiming TRACE adds value, answer:

```trace
What would a competent reader without TRACE have seen?
```

Then answer:

```trace
What did TRACE make visible that the baseline likely missed or blurred?
```

Transfer only matters if there is actual added structure, not vocabulary substitution.

---

## Output format required

Return your answer in this structure:

```trace
1. Case summary
2. EntityRoleVectors
3. ClaimMap
4. ClockMap
5. TransitionMap
6. LaunderingScan
7. CorrectionMap
8. DirtyActionReceipt if needed
9. EvaluatorStack
10. ResidueLedger
11. BaselineComparison
12. OpenWounds
13. Failure of TRACE if any
14. One-paragraph verdict
```

Do not end with general praise. End with either:

```trace
transfer_status := pass | partial_pass | fail
```

and explain why.

---

## Test cases suggested

Use one of these, or choose a comparable case:

```trace
Grenfell Tower public inquiry / government response
Horizon Post Office scandal
Robodebt
Rotterdam benefits scandal
algorithmic hiring rejection
hospital triage under shortage
school exclusion decision
content moderation at scale
AI agent acting through tools
```

A good transfer test should be unfamiliar enough that the framework has to work, not just repeat memorised case language.

---

## Failure modes to watch for

Fail the framework if it does any of these:

```trace
turns into moral oracle
collapses to checklist
forgets affected scopes
forgets clocks
lets authority self-certify legitimacy
uses procedure as repair
uses metric as lived condition
calls dirty action clean
uses uncertainty as permission not to decide
produces slogans without graph structure
```

---

## Minimal final compression

```trace
TRACE/ME :=
  typed graph discipline
  for exposing transitions under uncertainty
  so harm, authority, time, correction, and residue
  cannot be silently laundered before action hardens
```
