# TRACE Loss Prevention Checklist v0.1

Use this before every new build.

## Before Adding a Case

```trace
case_gate :=
  does_it_reveal_new_operator?
  OR does_it_pressure_test_existing_operator?
  OR does_it_break_existing_operator?
```

If no, do not add as bootstrap.

## Before Adding an Operator

Required fields:
- name
- compression
- definition
- source case
- activation condition
- deactivation condition
- comparator
- distinct remainder
- falsifier
- demoter
- status
- must-not-claim

## Before Updating the Kernel

```trace
kernel_gate :=
  clear_activation_condition
  + clear_deactivation_condition
  + one_success_case
  + one_failure_case
  + one_breaker_case
  + demotion_rule
  + comparator_check
```

If incomplete, do not update Kernel.

## Before Publishing / Relaying

Use:
1. Public One-Sheet
2. Current Front Door
3. Top-20 Claims
4. Diagnostic Kernel
5. Operator Registry
6. External Review Prompt

## Before Declaring Progress

Ask:
- What became more falsifiable?
- What could now be demoted?
- What did we subtract?
- What existing framework covers this better?
- What branch is being held back?

End.
