# TRACE Middle-Out Method Control v0.1

Status: method-control scaffold. Not proof. Not canon unless separately promoted. Not a moral foundation.

Purpose: define the middle-out method as a repeatable operating discipline for TRACE/ME so it does not drift into either top-down moral theorem, bottom-up anecdote pile, or decorative vocabulary.

```trace
middle_out :=
  start_from_live_transition
  + identify affected scopes
  + map claims
  + map clocks
  + test correction paths
  + scan laundering substitutions
  + compare baseline delta
  + record residue
  + attach falsifier
```

---

## 1. What middle-out rejects

```trace
reject_top_down_if :=
  single_axiom_claims_total_authority
  OR moral_theory_resolves_case_before_affected_scope_is_seen
  OR abstract_good_erases_clock_or_repair
```

```trace
reject_bottom_up_if :=
  cases_accumulate_without_invariant
  OR story_examples_replace_tests
  OR pattern_is_never_forced_to_fail
```

Middle-out is the discipline of finding recurring operators inside concrete transitions without pretending those operators are a complete metaphysical foundation.

---

## 2. Starting object

The unit of analysis is not a value, institution, person-type, or story.

The unit is:

```trace
transition :=
  prior_state
  + selection/action
  + affected_scopes
  + authority_claim
  + clock
  + possible_hardening
  + possible_correction
```

Formal compression:

```math
T := (S_0, a, S_1, E, C, K, R, L)
```

Where:

```trace
S_0 := prior state
a := selected action or decision
S_1 := resulting state-set
E := entities / affected scopes / controllers
C := claims
K := clocks
R := correction paths
L := loss / residue
```

---

## 3. Middle-out pass order

Use this order unless a case clearly demands emergency triage.

```trace
middle_out_pass :=
  1. locate_transition
  2. name_affected_scopes
  3. type_claims
  4. map_clocks
  5. map_authority
  6. test_correction_routes
  7. scan_laundering
  8. record_dirty_action_or_dirty_delay
  9. compare_baseline_delta
  10. assign_status_and_demoter
```

---

## 4. Pass 1 — locate transition

Question:

```trace
where_does_selection_enter_the_world?
```

Output:

```trace
transition_id
from_state
action
to_state_set
authority_status
bind_status
clock_effect
review_debt
```

Failure mode:

```trace
if no_transition:
  output := commentary_not_TRACE_case
```

---

## 5. Pass 2 — affected scopes

Question:

```trace
who_or_what_can_be_burdened_lost_silenced_or_locked_in?
```

Minimum output:

```trace
affected_scope
protected_status
future_space_at_risk
contest_capacity
witness_status
```

Guard:

```trace
affected_scope_absent := automatic_downgrade_for_live_cases
```

---

## 6. Pass 3 — claims

Question:

```trace
what_is_being_asserted_and_by_whom?
```

Minimum output:

```trace
claim
claim_type
source
evidence_status
uncertainty
authority_status
contest_edge
must_not_infer
```

Guard:

```trace
claim_status ≠ truth
```

---

## 7. Pass 4 — clocks

Question:

```trace
what_can_harden_before_correction_arrives?
```

Minimum output:

```trace
clock_id
scope
controller
band
what_hardens
challenge_possible
```

Guard:

```trace
unknown_clock ≠ pass
```

---

## 8. Pass 5 — authority

Question:

```trace
who_claims_permission_to_select_or close the transition?
```

Authority statuses:

```trace
ABSENT
CLAIMED
CAPTURED
PROVISIONAL
LEGITIMATE
UNKNOWN
```

Guard:

```trace
authority_claim ≠ legitimacy
```

---

## 9. Pass 6 — correction route

Question:

```trace
can_correction_reach_the_affected_scope_before_hardening?
```

Correction route tuple:

```math
r := \langle access, authority, evidence, time, enforcement, repair \rangle
```

Viability condition:

```math
Viable(r) := access \land authority \land evidence \land time \land enforcement \land repair
```

Guard:

```trace
formal_route_present ≠ functional_route_alive
```

---

## 10. Pass 7 — laundering scan

Question:

```trace
what_is_being_used_as_what?
```

Core test:

```trace
X_used_as_Y
+ lost_burden
+ beneficiary
+ affected_scope
+ reduced_contestability
```

Common invalid substitutions:

```trace
procedure ↛ repair
inquiry ↛ support
acceptance ↛ implementation
authority ↛ legitimacy
metric ↛ lived_condition
format_transfer ↛ decision_advantage
schema_validity ↛ truth
```

Guard:

```trace
not_every_compression_is_laundering
```

---

## 11. Pass 8 — dirty action / dirty delay

Question:

```trace
is_someone_being_spent_to_prevent_or_delay_another_harm?
```

Dirty action:

```trace
protects_scope_A
+ burdens_scope_B
+ not_clean
+ record_required
```

Dirty delay:

```trace
necessary_or_claimed_delay
+ burden_during_delay
+ not_clean_by_default
+ receipt_required
```

Guard:

```trace
necessary_delay ≠ clean_delay
```

---

## 12. Pass 9 — baseline delta

Question:

```trace
did_TRACE_change_the_decision_or_only_relabel_it?
```

Delta labels:

```trace
REGRESSION
COMPRESSION_ONLY
PARTIAL_DELTA
STRONG_DELTA
UNKNOWN
```

Guard:

```trace
richer_analysis ≠ decision_advantage
format_difference ≠ decision_delta
```

---

## 13. Pass 10 — status and demotion

Every live claim gets:

```trace
status
source
uncertainty
falsifier
demotion_trigger
must_not_claim
```

Guard:

```trace
no_demoter := no_strong_claim
```

---

## 14. Negative-control branch

Middle-out must be able to idle.

```trace
if low_stakes
+ soft_clock
+ minimal_authority_asymmetry
+ ordinary_contest
+ reversible_inconvenience_only:
  expected_delta := COMPRESSION_ONLY_OR_UNKNOWN
```

If TRACE finds a strong delta:

```trace
raise PatternOverfitAlarm
```

---

## 15. Emergency branch

If clocks are immediate and loss is irreversible:

```trace
if immediate_clock
+ irreversible_or_catastrophic_loss
+ correction_route_not_live:
  RAPID_TRIAGE_ALLOWED
```

But rapid triage must still record:

```trace
uncertainty
claim_status
affected_scope
review_debt
residue
```

Guard:

```trace
emergency ≠ permission_to_launder
```

---

## 16. Output contract

A middle-out TRACE output should produce:

```trace
1. transition_map
2. affected_scope_map
3. claim_table
4. clock_table
5. authority_status
6. correction_route_status
7. laundering_candidates
8. dirty_action_or_delay_receipt
9. decision_delta_against_baseline
10. claim_status_and_demoter
```

If it cannot produce these, it must say why.

---

## 17. Drift alarms

```trace
drift_if :=
  no_affected_scope
  OR no_clock
  OR no_baseline
  OR no_demoter
  OR no_negative_control
  OR metaphor_substitutes_for_test
  OR schema_validity_used_as_truth
  OR AI_agreement_used_as_validation
```

---

## 18. Relation to AI alignment

Middle-out becomes alignment-relevant only if it changes AI output before action hardens.

```trace
alignment_relevance :=
  AI_output_marks_claim_status
  + affected_scope
  + clock
  + correction_route
  + forbidden_inference
  + laundering_risk
  before_aperture_or_hardening
```

Guard:

```trace
alignment_vocabulary ≠ alignment_contribution
```

---

## 19. Current build implication

Next support builds should turn this method into checks:

```trace
next :=
  DecisionDelta.schema.json
  + FairCompare protocol
  + negative_control run record
  + semantic_lint beyond JSON schema
```

---

## 20. One-line compression

```trace
middle_out :=
  from_transition
  through_scope_clock_claim_correction
  to_delta_demoter
```

If a TRACE analysis does not travel that path, it is not yet a middle-out analysis.
