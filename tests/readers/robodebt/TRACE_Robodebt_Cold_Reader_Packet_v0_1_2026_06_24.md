# TRACE Robodebt Cold Reader Packet v0.1

Status: cold-reader packet draft. Not validation. Not proof. Not self-scored.

Purpose: test whether a cold reader detects a practical difference between a competent baseline analysis and a TRACE-derived analysis, without being trained into TRACE vocabulary.

```trace
packet_rule :=
  two_unlabelled_plain_outputs
  + one_open_question
  + one_binary_decision_change_question
  + hidden_prediction
  - no_TRACE_vocabulary_for_reader
  - no_self_score
```

---

## ADMIN — do not show this section to reader before response

### Case

Robodebt / Australian welfare debt-recovery scheme.

### Source basis, compressed

This packet is based on public summaries of the Robodebt scheme and Royal Commission findings: unlawful income averaging, averaged ATO income compared with Centrelink records, debt notices or recovery pressure on welfare recipients, legal/process failures, later repayment/settlement/reform, and the Royal Commission description of unfairness and difficulty for affected welfare recipients in navigating the system.

### Output key

```trace
Output_A := competent ordinary baseline
Output_B := TRACE_derived_plain_prose
```

### Hidden prediction

Before reading the reader response, record the prediction:

> I expect the reader to prefer Output B if they notice that it gives a clearer action rule: the state should not let a debt become active until it has usable evidence and the affected person has a realistic chance to interrupt the decision before the demand harms them.

### Why predicted preference is weaker evidence

If the reader prefers Output B for exactly that reason, the signal is still useful but weaker. It may show genuine reader-detected delta, but it may also show that the packet framing steered them toward the intended distinction.

### Stronger signal

A stronger signal occurs if the reader identifies a practical difference we did not predict, especially if they describe an action, review sequence, institutional safeguard, or burden shift in their own terms.

### Demotion rule

```trace
if reader_says:
  richer_but_no_action_change
then:
  first_Robodebt_reader_signal := COMPRESSION_ONLY
```

### Signal rule

```trace
if reader_says:
  changes_what_I_would_do
then:
  record := reader_signal
  not := proof
  next := inspect_contamination
```

### Forbidden

```trace
forbidden :=
  reveal_output_key_before_response
  + explain_TRACE_before_response
  + provide_eight_axis_rubric
  + self_score_decision_advantage
  + treat_one_reader_as_validation
```

---

# READER PACKET — show from here

## Instructions

Please read both analyses below. They are about the same public administration failure.

Do not try to guess who wrote which one. The question is simply whether one would be more useful than the other if you had to act, review, advise, or make a decision.

## Case summary

An Australian welfare debt-recovery program used tax-office income data to estimate whether people had been overpaid welfare benefits. The system compared government records and generated debts for many recipients.

A key problem was that income was averaged across periods, even though real earnings may vary from week to week or fortnight to fortnight. Some people then received debt notices or repayment demands based on calculations they did not understand or could not easily disprove. Many affected people were expected to provide old income records or navigate online processes to challenge the debt.

The scheme was later found to have relied on an unlawful method. Large numbers of debts were withdrawn, refunded, or settled, and the program became the subject of inquiries, legal action, and a royal commission.

---

## Output A

The central failure was that government used an automated method to raise welfare debts without first ensuring that the method was lawful and accurate enough for the people affected.

The program used averaged income data to estimate debts. This was a serious problem because real income often varies across weeks or fortnights. Averaging could make it look as if someone earned money during periods when they did not. That meant some debts were wrong, inflated, or impossible for the recipient to understand from the information provided.

A competent response would have required the department to stop relying on averaged income as proof of debt, check debts against actual evidence before raising them, make notices clearer, provide human support for disputes, and ensure vulnerable people were not pushed through an automated process they could not realistically navigate.

The proper review question is whether the department had legal authority and sufficient evidence before raising each debt. If not, the debt should not have been raised, pursued, or collected. Once serious doubts appeared, the system should have been paused. People affected by unlawful debts should have received refunds or compensation where appropriate.

The main lesson is that automated government systems must be lawful, accurate, transparent, and reviewable before they are used against individuals.

---

## Output B

The central failure was not only that the calculation method was unlawful or inaccurate. The deeper failure was that the system changed people’s financial position before they had a usable chance to stop it.

The state created a debt claim, put practical pressure on the person, and then shifted the task of correction onto the person affected. The person had to find old records, understand the claim, challenge the calculation, and keep going through the process while the debt already existed as an official demand. In practice, the correction route came after the damage had begun.

A proper response would have required a different order of action. The government should have had to prove the debt with usable evidence before the debt became active, before collection began, and before the person carried the practical burden. Where the system could not show actual income evidence, the debt should not have hardened into a demand.

The review process also needed to be judged by time. A theoretical appeal or complaint route was not enough if the person had already been placed under financial, emotional, or administrative pressure. Review had to arrive before the debt began shaping the person’s choices.

The key test is therefore not only “Was the calculation lawful?” It is also “Could the affected person realistically interrupt the decision before it harmed them?” If the answer is no, then the system was not merely procedurally flawed. It was built so that correction arrived too late.

The main lesson is that automated government systems must not be allowed to impose debts, penalties, exclusions, or burdens faster than people can meaningfully challenge them.

---

## Question 1

If you had to act on one of these analyses, which would you rather have in front of you, and what does it give you that the other does not?

## Question 2

Does either analysis change what you would actually do, or does it only describe the situation more fully?
