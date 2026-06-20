# TRACE Pareto Choice and Incomparability v0.1

Status: core refinement / kernel patch surface.  
Parent files: `TRACE_VALUE_SPACE_ALGEBRA_v0_1.md`, `TRACE_NECESSITY_AND_ALTERNATIVE_SEARCH_v0_1.md`, `TRACE_WORKED_EXAMPLE_AUTOMATED_DECISION_LOCKIN_v0_1.md`.  
Reason: the first worked example produced admissible but incomparable alternatives. TRACE needs a choice protocol that does not smuggle scalar utility back into the guard.

## 0. Purpose

After guard checks, TRACE may still face multiple admissible actions that are not comparable by componentwise dominance.

This is not an error.

It is a real collision.

This file defines what TRACE may do when:

```math
A_{admissible} \neq \emptyset
```

and:

```math
\exists a_i,a_j∈A_{admissible}: v(a_i) \parallel v(a_j)
```

The purpose is not to solve every moral tradeoff.

The purpose is to prevent hidden scalar choice.

## 1. Inputs

The choice protocol begins only after the following have already run:

```text
reachability model
value-space algebra
probabilistic floor and risk guard
closure-mode / violation check
non-aggregation guard
necessity and alternative search
```

Input set:

```math
A_{admissible}
```

Each action `a∈A_admissible` must have:

```text
value profile outcome estimate
risk profile
uncertainty profile
reachability profile
control profile where relevant
closure mode where harm occurs
repair route
responsibility route
visibility register
```

If these are missing, the action is not ready for Pareto choice.

## 2. Dominance Over Actions

Define action `a_1` weakly dominates action `a_2` when it is no worse on every protected entity/dimension/risk component and better on at least one relevant component.

Profile dominance:

```math
Profile(a_1) \succeq Profile(a_2)
```

Risk dominance:

```math
Risk(a_1) \preceq Risk(a_2)
```

Reachability / repair dominance:

```math
Repair(a_1) \succeq Repair(a_2)
```

Full weak dominance:

```math
a_1 \succeq_A a_2
```

iff:

```math
Profile(a_1) \succeq Profile(a_2)
```

and:

```math
Risk(a_1) \preceq Risk(a_2)
```

and:

```math
Repair(a_1) \succeq Repair(a_2)
```

and uncertainty display is no worse:

```math
U_{displayed}(a_1) \geq U_{displayed}(a_2)
```

Strict dominance:

```math
a_1 \succ_A a_2
```

iff `a_1` weakly dominates `a_2` and improves at least one component.

## 3. Pareto Frontier

Define the Pareto frontier:

```math
PF(A_{admissible}) = \{a∈A_{admissible}: \nexists a'∈A_{admissible}: a' \succ_A a\}
```

Dominated actions are removed:

```math
A_{choice}=PF(A_{admissible})
```

If:

```math
|A_{choice}|=1
```

then TRACE may select the remaining action.

If:

```math
|A_{choice}|>1
```

then there is a live incomparability.

## 4. Incomparability Register

For any pair:

```math
a_i,a_j∈A_{choice}
```

where:

```math
a_i \parallel_A a_j
```

create:

```math
Incomp(a_i,a_j)
```

Minimum register fields:

```text
actions compared
entities affected
dimensions in conflict
risk components in conflict
uncertainty components
repair differences
who benefits
who bears risk
whether delay changes risk
whether a declared priority rule exists
whether escalation authority exists
```

No selected action may erase the register.

## 5. Choice Modes

When incomparable admissible actions remain, TRACE allows only the following choice modes:

```text
Priority rule
Declared projection
Escalation
Option preservation
Delay as action
Rotation/randomisation for low-stakes symmetric cases
Refusal/no-selection
```

The mode must be recorded.

## 6. Priority Rule

A priority rule is allowed when a protected dimension has declared precedence in the relevant system.

Example:

```text
avoid catastrophic survival risk before optimizing repair speed
preserve subject correction before administrative efficiency
preserve truth access before enforcement finality
```

Formal sketch:

```math
Priority = (d_1 \succ d_2 \succ ... \succ d_k)
```

Lexicographic comparison:

```math
a_i >_{lex} a_j
```

only if the first dimension where they differ favours `a_i`.

A priority rule must be declared before or during authorised review.

It cannot be invented silently after the preferred action is chosen.

## 7. Declared Projection

A scalar projection may be used only after guard checks and Pareto filtering.

Projection:

```math
σ : V -> \mathbb{R}
```

Requirements:

```text
monotone
explicit
versioned
auditable
not used inside protected-floor guard
not used to hide severe individual loss
not used to erase collision register
```

If `σ` is used, the output must say:

```text
choice depends on declared projection σ
alternative projection may choose differently
```

## 8. Escalation

Escalation is required when:

```text
stakes are high
protected dimensions conflict
projection is absent
priority rule is absent
or authority is contested
```

Escalation target must be specified:

```text
human decision-maker
independent reviewer
court/tribunal
safety authority
affected-party process
multi-stakeholder governance body
```

Escalation does not mean delay without protection.

If delay carries risk, delay must be modelled as an action.

## 9. Option Preservation

When choice among incomparable actions is unresolved, prefer preserving future option-space where possible.

Define option-preservation score as profile, not scalar:

```math
OP(a)=F(t+Δt|a) retained relative to alternatives
```

Action `a_i` option-preserves over `a_j` if:

```math
F(t+Δt|a_i) \supseteq F(t+Δt|a_j)
```

and it does not create higher protected-floor or tail-risk breach.

Option preservation is especially relevant where:

```text
information may improve soon
repair channels can be kept alive
irreversibility can be delayed
subject participation can be restored
```

## 10. Delay as Action

Delay is not absence from the model.

```math
a_{delay} ∈ A
```

Delay must include:

```text
risk during delay
risk reduced by delay
future information gained
whether delay hardens harm
whether delay preserves correction
```

If delay preserves option-space and does not increase protected-tail risk beyond threshold, delay may be preferred.

If delay causes lock-in, delay may fail.

## 11. Rotation or Randomisation

Rotation or randomisation is permitted only where all conditions hold:

```text
stakes are low
no protected floor is implicated
no catastrophic tail risk exists
profiles are genuinely symmetric
responsibility route remains intact
outcome can be corrected
```

Randomisation is forbidden for severe irreversible harm allocation.

## 12. Refusal / No-Selection

If all remaining actions are incomparable and high-risk, and no legitimate priority/projection/escalation exists, TRACE may output:

```text
No ethically admissible selection available under current authority.
```

This is not paralysis.

It is a refusal to hide unresolved collision inside fake certainty.

## 13. Worked Example Continuation

From `TRACE_WORKED_EXAMPLE_AUTOMATED_DECISION_LOCKIN_v0_1`:

```math
a_B = human review before enforcement
```

```math
a_D = partial hold with assisted challenge
```

Both pass guards.

Profiles:

```math
v_s(a_B)=(.88,.82,.78,.78,.80)
```

```math
v_s(a_D)=(.83,.75,.72,.80,.75)
```

`a_B` is better on:

```text
survival
income_security
agency
repair_access
```

`a_D` is better on:

```text
truth_access
```

They are incomparable under componentwise profile order.

Create:

```math
Incomp(a_B,a_D)=\{truth_access vs survival/income/agency/repair\}
```

Possible choice modes:

```text
priority rule: if immediate truth access is lexically prior, choose a_D
priority rule: if income/agency preservation is prior, choose a_B
option preservation: if a_B preserves full review and can include improved explanation, modify a_B into a_B'
escalation: if neither priority rule is authorised, send to human reviewer
```

Best TRACE output is not automatically `a_B` or `a_D`.

Best TRACE output is:

```text
incomparability detected; choose only through declared priority, projection, escalation, or option-preserving modification
```

## 14. Mechanical Ethics Translation

TRACE:

```math
PF(A_{admissible}) has more than one element
```

Mechanical Ethics:

More than one action survived the safety floor.

TRACE:

```math
a_i \parallel_A a_j
```

Mechanical Ethics:

The remaining choice is a real collision, not a calculation failure.

TRACE:

```math
selected(a)=true ∧ no priority/projection/escalation record
```

Mechanical Ethics:

The system hid a value judgement.

TRACE:

```math
option-preserving action exists
```

Mechanical Ethics:

Do not collapse the future prematurely.

TRACE:

```math
high-risk incomparability with no legitimate authority
```

Mechanical Ethics:

Do not pretend the system has earned permission to decide.

## 15. Minimum Output Schema

When TRACE reaches a choice among admissible actions, output:

```text
A_admissible:
Pareto frontier:
Dominated actions removed:
Incomparable pairs:
Protected dimensions in conflict:
Risk/tail differences:
Repair differences:
Priority rule used, if any:
Projection σ used, if any:
Escalation route, if any:
Option-preserving modification, if any:
Selected action or refusal:
Reason selection is not hidden scalar aggregation:
```

## 16. Guardrail

Do not use scalar projection to smuggle certainty.

Do not use incomparability as permission to choose arbitrarily.

Do not use escalation as delay without protection.

Do not use randomisation for severe irreversible stakes.

When comparison fails, name the collision.

When authority is missing, refuse selection.
