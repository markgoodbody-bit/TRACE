# TRACE / ME Diagnostic Kernel v0.2

Status: exploratory diagnostic kernel. Not validation. Not governance certification.

## Kernel purpose

The Diagnostic Kernel is the smallest usable TRACE checklist.

It should diagnose whether a system has live correction, exit, or repair capacity before harm hardens.

## Core K-gate

```trace
K := Witness * Record * Authority * Time * Enforcement * Repair
```

If any factor is functionally zero, correction capacity collapses at that gate.

## Rating vocabulary

Use only:

- `PASS`
- `PASS_LIMITED`
- `PARTIAL`
- `FAIL`
- `UNKNOWN`

Do not invent numeric scores without measurement rules.

## Branch 1: internal correction

```trace
if system_corrigible:
  test_internal_correction_before_hardening
```

Ask:

| Gate | Question |
|---|---|
| Witness | Can the affected subject and harm path be seen? |
| Record | Is the record preserved, contestable, and non-captured? |
| Authority | Can anyone actually change the path? |
| Time | Can correction arrive before hardening? |
| Enforcement | Will correction bind the system? |
| Repair | Can repair matter to the affected subject? |

## Branch 2: exit route under predatory system

```trace
else_if official_system_is_harm_carrier:
  test_exit_route_before_capture
```

Use only when the official route itself increases capture, exposure, retaliation, or harm.

Ask:

| Field | Question |
|---|---|
| Capture risk | Does internal review expose the subject to the harm carrier? |
| Exit route | Is there a viable protected path out? |
| Trust | Who verifies the route? |
| Timing | Can exit beat capture? |
| Protection | Is secrecy protective or self-serving? |
| Aftercare | What happens after exit? |

## Held candidate branches

These are not Kernel v0.3 yet:

```trace
held :=
  recursive_agency_training_loop
  + creator_responsibility
  + contested_legitimacy
```

They may become Kernel branches only after pressure testing.

## Candidate branch gate

```trace
candidate_branch_gate :=
  clear_activation_condition
  + clear_deactivation_condition
  + one_success_case
  + one_failure_case
  + one_breaker_case
  + demotion_rule
  + comparator_check
```

## Must-not-claim

```trace
Diagnostic_Kernel != validation
Diagnostic_Kernel != certification
K_gate != numeric_score
exit_route != opacity_permission
candidate_branch != operational_kernel
```
