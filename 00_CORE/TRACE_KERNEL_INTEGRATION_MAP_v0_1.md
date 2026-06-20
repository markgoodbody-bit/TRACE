# TRACE Kernel Integration Map v0.1

Status: core integration / anti-sprawl control surface.  
Scope: maps the current TRACE mathematical kernel files and their dependency order.  
Not: new operator, proof of validity, public-facing explanation, or cleanup/deletion manifest.

## 0. Purpose

Recent work produced a chain of kernel refinements after fresh-reader critique.

This file stops those refinements becoming a new pile.

It records:

```text
which file controls which concept
which file depends on which prior file
which concepts are still open
which files should not duplicate each other
what the next worked example must exercise
```

## 1. Current Kernel Spine

Current intended order:

```text
TRACE_MATH_KERNEL_v0_1
-> TRACE_FUTURE_SPACE_AND_CONTINUATION_v0_1
-> TRACE_REACHABILITY_MODEL_v0_1
-> TRACE_UNCERTAINTY_TYPES_v0_1
-> TRACE_CLOSURE_MODE_AND_VIOLATION_v0_1
-> TRACE_NON_AGGREGATION_GUARD_v0_1
-> TRACE_VALUE_SPACE_ALGEBRA_v0_1
-> TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1
-> TRACE_NECESSITY_AND_ALTERNATIVE_SEARCH_v0_1
```

This is the current core stack.

No later file should silently redefine an earlier primitive.

If a later file modifies an earlier primitive, it must mark itself as a patch surface and name the modified relation.

## 2. File Roles

### 2.1 `TRACE_MATH_KERNEL_v0_1`

Role: root vocabulary and minimal TRACE sequence.

Controls:

```text
entity
state
observation
belief/model
uncertainty
action-space
reachability
transition
future-space
harm
repairability
irreversibility
positive continuation
empathy as modelling
middle-out procedure
Mechanical Ethics translation examples
```

Dependency: none.

Status: foundation, not final formalism.

Known weakness: introduced several variables before their algebra was fully specified.

### 2.2 `TRACE_FUTURE_SPACE_AND_CONTINUATION_v0_1`

Role: separates reachable futures from livable/value-weighted futures.

Controls:

```text
F_e(t) as reachable future-space
Phi_e as weighting over future-space
C+_e as profile-valued viability field over future-space
LF_e(t) as livable future-space
DeltaF, DeltaH, DeltaL distinction
```

Depends on:

```text
TRACE_MATH_KERNEL_v0_1
```

Corrects:

```text
C+ is not raw future-space
C+ is not valid as a simple additive equation
```

Open seam: `Phi_e` and `C+_e` require value-space algebra.

### 2.3 `TRACE_REACHABILITY_MODEL_v0_1`

Role: replaces loose scalar reachability with profile-first reachability.

Controls:

```text
Rho_e(a,t) profile
rho_e(a,t) scalar compression only when aggregation rule declared
lived action-space LA_e(t)
capture condition
correction reachability
formal appeal vs real correction route
```

Depends on:

```text
TRACE_MATH_KERNEL_v0_1
```

Corrects:

```text
abstract action availability must not be treated as meaningful access
```

Open seam: relation between reachability profiles and probability distributions remains to be worked in examples.

### 2.4 `TRACE_UNCERTAINTY_TYPES_v0_1`

Role: separates uncertainty kinds.

Controls:

```text
epistemic uncertainty
aleatoric uncertainty
model uncertainty
normative uncertainty
standing uncertainty
translation uncertainty
meta-uncertainty
uncertainty display rule
```

Depends on:

```text
TRACE_MATH_KERNEL_v0_1
```

Corrects:

```text
U_actual cannot be assumed perfectly known
uncertainty itself may be uncertain
```

Open seam: imprecise probability / set-of-measures treatment is not yet fully formalised.

### 2.5 `TRACE_CLOSURE_MODE_AND_VIOLATION_v0_1`

Role: distinguishes magnitude of future-space loss from how future-space was closed.

Controls:

```text
closure mode CM_e(a)
closure vector K_e(a)
violation indicator Vio_e(a)
repair dependence on closure mode
responsibility route relevance
```

Depends on:

```text
TRACE_MATH_KERNEL_v0_1
TRACE_FUTURE_SPACE_AND_CONTINUATION_v0_1
```

Corrects:

```text
harm magnitude alone does not capture violation
accident, coercion, deception, predation, and bureaucratic error require different repair routes
```

Open seam: closure-mode tables are operational configuration, not core algebra.

### 2.6 `TRACE_NON_AGGREGATION_GUARD_v0_1`

Role: prevents total-harm minimisation from erasing individual subjects.

Controls:

```text
subject-preservation before aggregation
severe individual loss guard
Pareto check
collision register
aggregation as later-stage comparison only
```

Depends on:

```text
TRACE_MATH_KERNEL_v0_1
TRACE_CLOSURE_MODE_AND_VIOLATION_v0_1
```

Corrects:

```text
raw sum-minimisation can become utilitarian sacrifice
```

Open seam: scalar/profile mismatch required value-space algebra.

### 2.7 `TRACE_VALUE_SPACE_ALGEBRA_v0_1`

Role: defines profile-valued continuation and harm comparison.

Controls:

```text
value dimensions D_e
profile space V_e
componentwise partial order
incomparability
profile loss delta_e(a)
declared scalar projection sigma_e
protected floors
severe loss by dimension
hidden bill by dimension
interval/distribution value profiles
```

Depends on:

```text
TRACE_FUTURE_SPACE_AND_CONTINUATION_v0_1
TRACE_NON_AGGREGATION_GUARD_v0_1
```

Corrects:

```text
C+ profile-valued cannot feed scalar max/sum without declared projection
scalar harm is a projection, not source authority
```

Open seam: floor checks by expected value exposed tail-risk problem.

### 2.8 `TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1`

Role: prevents expected-value floor checks from hiding catastrophic tail risk.

Controls:

```text
outcome distributions over value profiles
floor breach probability PB
catastrophic tail risk TR
severe loss probability PS
lower-bound guard
probabilistic guard Guard_P
risk profiles indexed by entity and protected dimension
hidden probabilistic risk registers
cross-entity normalisation requirement
horizon-indexed risk
```

Depends on:

```text
TRACE_VALUE_SPACE_ALGEBRA_v0_1
TRACE_UNCERTAINTY_TYPES_v0_1
TRACE_NON_AGGREGATION_GUARD_v0_1
```

Corrects:

```text
E[v] can pass while a catastrophic tail remains
protected floors are not expectation checks
```

Open seam: probability measure over future profiles and imprecise probability need more formal handling.

### 2.9 `TRACE_NECESSITY_AND_ALTERNATIVE_SEARCH_v0_1`

Role: prevents necessity from becoming a loophole.

Controls:

```text
alternative search set Alt_s(a,t)
reachable alternatives RAlt_s(a,t)
control profile Ctrl(a)
risk dominance without scalar aggregation
SaferAdequateAlt(a)
necessity as earned status
incomparable alternative register
alternative search record
hidden probabilistic bill registers replacing unsafe sums
risk horizon tau_breach(a)
```

Depends on:

```text
TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1
TRACE_VALUE_SPACE_ALGEBRA_v0_1
TRACE_NON_AGGREGATION_GUARD_v0_1
TRACE_REACHABILITY_MODEL_v0_1
```

Corrects:

```text
necessity cannot be asserted in prose
a safer adequate alternative defeats necessity
risk incomparability must be named
urgency adds delay as an action; it does not erase alternatives
```

Open seam: action-choice after admissible but incomparable alternatives remains unresolved.

## 3. Dependency Graph

```text
MATH_KERNEL
  -> FUTURE_SPACE_AND_CONTINUATION
      -> VALUE_SPACE_ALGEBRA
          -> PROBABILISTIC_FLOOR_AND_RISK_GUARD
              -> NECESSITY_AND_ALTERNATIVE_SEARCH
  -> REACHABILITY_MODEL
      -> NECESSITY_AND_ALTERNATIVE_SEARCH
  -> UNCERTAINTY_TYPES
      -> PROBABILISTIC_FLOOR_AND_RISK_GUARD
  -> CLOSURE_MODE_AND_VIOLATION
      -> NON_AGGREGATION_GUARD
      -> VALUE_SPACE_ALGEBRA
  -> NON_AGGREGATION_GUARD
      -> VALUE_SPACE_ALGEBRA
      -> PROBABILISTIC_FLOOR_AND_RISK_GUARD
      -> NECESSITY_AND_ALTERNATIVE_SEARCH
```

## 4. Current Open Seams

The following are still unresolved and should not be pretended solved.

### 4.1 Probability Measure Over Futures

`TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1` says outcome distributions are induced by world transition and value-profile maps.

Still missing:

```text
formal construction of P_e(v_e(t+dt)|x,a,M,U)
handling of imprecise probability / set of measures
how model uncertainty changes distribution bounds
```

Potential next file:

```text
TRACE_IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION_v0_1.md
```

### 4.2 Choice Among Incomparable Admissible Actions

`VALUE_SPACE_ALGEBRA` names incomparability.

`NECESSITY_AND_ALTERNATIVE_SEARCH` records incomparable adequate alternatives.

Still missing:

```text
selection procedure when multiple actions pass guards but remain incomparable
rules for projection declaration
when to escalate
when to defer
when to randomise, rotate, or preserve option-space
```

Potential next file:

```text
TRACE_PARETO_CHOICE_AND_INCOMPARABILITY_v0_1.md
```

### 4.3 Threshold Register

Many files use thresholds:

```text
theta_live
theta_floor
theta_cat
epsilon_floor
epsilon_cat
epsilon_loss
theta_visi
theta_control
theta_rho
```

Still missing:

```text
how thresholds are declared
who sets them
how they are audited
what defaults exist
what happens when thresholds are absent
```

Potential next file:

```text
TRACE_THRESHOLD_REGISTER_v0_1.md
```

### 4.4 Mechanical Ethics Translation Rules

The kernel gives examples of translation.

Still missing:

```text
strict rule for deriving a Mechanical Ethics claim from TRACE output
claim status labels
when a translation is forbidden
when a translation is advisory
when a translation becomes a hard floor
```

Potential next file:

```text
ME_FROM_TRACE_TRANSLATION_RULES_v0_1.md
```

### 4.5 Worked Example

The kernel has been patched enough to require a test.

Still missing:

```text
one fully worked example using all current kernel layers
no new theory inside the example
explicit entity, state, observation, uncertainty, action-space, reachability, future-space, value profile, floor breach probability, closure mode, non-aggregation guard, necessity test
```

Potential next file:

```text
03_TESTS/TRACE_WORKED_EXAMPLE_AUTOMATED_DECISION_LOCKIN_v0_1.md
```

## 5. Anti-Duplication Rules

Do not duplicate definitions across files.

Use this allocation:

```text
future-space and livability -> FUTURE_SPACE_AND_CONTINUATION
reachability profile -> REACHABILITY_MODEL
uncertainty taxonomy -> UNCERTAINTY_TYPES
closure mode / violation -> CLOSURE_MODE_AND_VIOLATION
subject-preservation before aggregation -> NON_AGGREGATION_GUARD
profile algebra / scalar projection / floors -> VALUE_SPACE_ALGEBRA
probabilistic floor / tail risk -> PROBABILISTIC_FLOOR_AND_RISK_GUARD
necessity / alternatives / control profile -> NECESSITY_AND_ALTERNATIVE_SEARCH
```

If a new file needs one of these concepts, it should import or reference it, not redefine it.

## 6. Current Kernel Flow for a Case

A valid TRACE case should now proceed:

```text
1. Identify entity e and concrete point p_0.
2. Define x_e(t).
3. Define observation O_e(W(t)) and observation limits.
4. Define uncertainty profile U_e(t).
5. Define abstract action-space A_e(t).
6. Define reachability profile Rho_e(a,t) and lived action-space LA_e(t).
7. Define transition distribution over W(t+dt).
8. Define future-space F_e(t).
9. Map futures to value profiles V_e via C+_e.
10. Compute/profile delta_e(a), floors, severe loss, and livability loss.
11. Identify closure mode CM_e(a), violation, repair and responsibility route.
12. Run non-aggregation guard.
13. Run probabilistic floor/tail-risk guard.
14. Run necessity and alternative search.
15. If admissible actions remain incomparable, register incomparability.
16. Translate into Mechanical Ethics only after TRACE structure is explicit.
```

## 7. Worked Example Requirements

The first worked example must include at least two actions:

```text
A: fast system action with low expected harm but catastrophic tail risk
B: slower or more constrained action with lower tail risk but weaker control
```

It must test:

```text
expected value vs tail risk
protected floors
profile-valued harm
hidden bill registers
necessity exception
alternative search
incomparability
```

It must not introduce new theory.

If the example requires new theory, that is evidence the kernel is still incomplete.

## 8. Current Best Next Step

The next build should be a worked example or a Pareto-choice file.

Decision:

```text
If we want to test current machinery: build worked example next.
If we want to complete action selection logic: build Pareto choice next.
```

Recommended sequence:

```text
1. TRACE_WORKED_EXAMPLE_AUTOMATED_DECISION_LOCKIN_v0_1
2. TRACE_PARETO_CHOICE_AND_INCOMPARABILITY_v0_1
3. TRACE_IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION_v0_1
4. TRACE_THRESHOLD_REGISTER_v0_1
5. ME_FROM_TRACE_TRANSLATION_RULES_v0_1
```

## 9. Guardrail

Stop the fresh-AI patch loop until at least one worked example runs through the stack.

Further critique without a worked example will keep finding valid seams but may produce patch sprawl.

The kernel now needs execution pressure.
