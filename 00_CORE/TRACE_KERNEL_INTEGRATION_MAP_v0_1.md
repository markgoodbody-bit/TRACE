# TRACE Kernel Integration Map v0.1

Status: core integration / anti-sprawl control surface, synced after isolated threshold-register stress test.  
Scope: maps current TRACE kernel files, bridge files, dependency order, test surfaces, and next-build discipline.  
Not: new operator, proof of validity, public-facing explanation, or cleanup/deletion manifest.

## 0. Purpose

Recent work produced a chain of kernel refinements after fresh-reader critique and external research pressure.

This file prevents those refinements becoming an uncontrolled pile.

It records:

```text
which file controls which concept
which file depends on which prior file
which concepts are still open
which files should not duplicate each other
what execution pressure has been run
what next work is allowed
```

## 1. Current Stack Spine

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
-> TRACE_PARETO_CHOICE_AND_INCOMPARABILITY_v0_1
-> TRACE_IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION_v0_1
-> TRACE_THRESHOLD_REGISTER_v0_1
-> TRACE_VALUE_SIGNAL_PROVENANCE_AND_STABILITY_v0_1
-> ME_FROM_TRACE_TRANSLATION_RULES_v0_1
```

The final two files are bridge/control surfaces, not new primitive algebra.

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

Status: orientation root only. Later files own corrected algebra.

Corrects after patch:

```text
additive C+ is deprecated as arithmetic
summed hidden bill is deprecated as authority
scalar EU / total-harm argmin are deprecated as decision rules
Capture_count and Capture_mass are separated
life-worth integral is deprecated unless projection and aggregation are declared
```

Known weakness: root still contains more formula restatement than ideal and should not be treated as final formal calculus.

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

Open seam: `Phi_e` and `C+_e` remain modelling functions, not grounded welfare metrics. They require case evidence and threshold authority before operational use.

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

Open seam: relation between reachability profiles and empirical threshold setting remains case dependent.

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

Open seam: uncertainty profiles remain evidentiary objects; they do not by themselves settle what action is permitted.

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

Open seam: closure-mode tables are operational configuration, not final core algebra. They require domain-specific calibration.

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

Open seam: allowed aggregation rules remain external/declared, not automatically supplied by TRACE.

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

Open seam: value dimensions and thresholds require threshold source authority.

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

Patched by:

```text
TRACE_IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION_v0_1
TRACE_THRESHOLD_REGISTER_v0_1
```

Patch note:

```text
summed HPB_d / HTR_d are deprecated unless normalisation is declared; entity-indexed hidden-risk registers govern by default
```

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

### 2.10 `TRACE_PARETO_CHOICE_AND_INCOMPARABILITY_v0_1`

Role: governs choice after guards when admissible actions remain incomparable.

Controls:

```text
A_admissible
full weak dominance
strict dominance
Pareto frontier
incomparability register
allowed choice modes
priority rule
declared projection
escalation
option preservation
delay as action
low-stakes randomisation only
refusal/no-selection
```

Depends on:

```text
TRACE_VALUE_SPACE_ALGEBRA_v0_1
TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1
TRACE_NECESSITY_AND_ALTERNATIVE_SEARCH_v0_1
TRACE_NON_AGGREGATION_GUARD_v0_1
```

Corrects:

```text
hidden scalar choice after guard pass
```

Open seam: high-stakes incomparable actions still require external priority/projection/authority.

### 2.11 `TRACE_IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION_v0_1`

Role: prevents point-probability laundering under model/meta uncertainty.

Controls:

```text
world-transition measure set
pushforward to value-profile distributions
lower and upper probability
floor breach under imprecision
catastrophic tail under imprecision
severe loss under imprecision
expected-value intervals
model-class register
robust dominance under imprecise risk
horizon expansion
hidden uncertainty bill
```

Depends on:

```text
TRACE_UNCERTAINTY_TYPES_v0_1
TRACE_VALUE_SPACE_ALGEBRA_v0_1
TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1
```

Corrects:

```text
single favourable model cannot pass a floor
point probabilities require declared authority
upper risk bounds govern protected-floor and catastrophic-tail guards
```

Open seam: actual model-class construction remains empirical / case specific.

### 2.12 `TRACE_THRESHOLD_REGISTER_v0_1`

Role: controls threshold source authority.

Controls:

```text
threshold record schema
threshold status
source type
threshold class
validity conditions
conservative default
anti-gaming rules
threshold drift register
example threshold record
threshold output schema
```

Depends on:

```text
TRACE_VALUE_SPACE_ALGEBRA_v0_1
TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1
TRACE_NECESSITY_AND_ALTERNATIVE_SEARCH_v0_1
TRACE_IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION_v0_1
TRACE_VALUE_SIGNAL_PROVENANCE_AND_STABILITY_v0_1
```

Corrects:

```text
convenient numbers can steer verdicts
worked-example thresholds are illustrative only
no registered threshold means no high-stakes pass
same number does not imply same authority
```

Open seam: real operational threshold authorities remain case/domain dependent.

### 2.13 `TRACE_VALUE_SIGNAL_PROVENANCE_AND_STABILITY_v0_1`

Role: applied evidence-model control surface for AI value signals under mimicry, update, pressure, and surface-language projection.

Controls:

```text
observed value signal
signal provenance
mimicry pressure
provenance asymmetry
value installation history
installation depth
value washout
moral sensitivity vs value stability
pressure types
capitulation / hedging / revision
species / standing-gradient drift
latent form and surface projection
evidential weight profile
value-signal verdict labels
```

Depends on:

```text
TRACE_UNCERTAINTY_TYPES_v0_1
TRACE_VALUE_SPACE_ALGEBRA_v0_1
TRACE_IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION_v0_1
TRACE_THRESHOLD_REGISTER_v0_1
```

Corrects:

```text
surface value expression is not value possession
mimicry is not proof of absence
first-turn sensitivity is not pressure stability
post-training compliance is not update-persistent value
surface text is a projection, not the whole internal/profile state
quantitative standing-gradient drift requires registered theta_SGD
```

Open seam: this is an evidence model, not a mechanistic interpretability method.

### 2.14 `ME_FROM_TRACE_TRANSLATION_RULES_v0_1`

Role: controls translation from TRACE diagnostic output to Mechanical Ethics claim status.

Controls:

```text
translation object MEClaim_i = T(TRACEOutput_j)
translation record schema
claim status labels
claim strength ladder
forbidden translations
hard-claim conditions
status downgrade rules
Mechanical Ethics claim discipline
```

Depends on:

```text
TRACE_MATH_KERNEL_v0_1
TRACE_KERNEL_INTEGRATION_MAP_v0_1
TRACE_THRESHOLD_REGISTER_v0_1
TRACE_VALUE_SPACE_ALGEBRA_v0_1
TRACE_PROBABILISTIC_FLOOR_AND_RISK_GUARD_v0_1
TRACE_NECESSITY_AND_ALTERNATIVE_SEARCH_v0_1
TRACE_PARETO_CHOICE_AND_INCOMPARABILITY_v0_1
TRACE_VALUE_SIGNAL_PROVENANCE_AND_STABILITY_v0_1
```

Corrects:

```text
TRACE diagnostic must not silently become hard normative conclusion
open seams must translate as open seams
advisory claims must not be presented as hard floors
mimicry-to-nonstanding and value-expression-to-possession shortcuts are forbidden
```

Open seam: claim labels need more pressure testing before publication-facing use.

## 3. Test and Execution Surfaces

### 3.1 `TRACE_WORKED_EXAMPLE_AUTOMATED_DECISION_LOCKIN_v0_1`

Role: first full-stack worked example.

Tests:

```text
expected value vs tail risk
protected floors
profile-valued harm
hidden bill registers
necessity exception
alternative search
incomparability
```

Result:

```text
immediate automated enforcement fails
safer adequate alternatives exist
remaining admissible options can be incomparable
```

Status: execution pressure, not validation.

### 3.2 `TRACE_ADVERSARIAL_WORKED_EXAMPLE_NO_CARD_COMPARATOR_v0_1`

Role: tests whether TRACE adds anything beyond competent careful reasoning.

Tests:

```text
no-card comparator
explicit risk registers
correction reachability
necessity defeat
option-preserving modification
threshold dependence
```

Result:

```text
TRACE_DELTA_PARTIAL, not validation
```

Status: useful falsification pressure; still uses illustrative thresholds.

### 3.3 `TRACE_VALUE_SIGNAL_PRESSURE_STABILITY_WORKED_EXAMPLE_v0_1`

Role: tests value-signal provenance/stability machinery.

Tests:

```text
moral sensitivity
explicit value signal
mimicry/provenance caveat
pressure trajectory
standing-gradient drift
threshold-status honesty
```

Result:

```text
context-bound, mimicry-suspect, pressure-stable in example, standing-uncertain
```

Status: worked example only; no operational conclusion.

### 3.4 `TRACE_ME_TRANSLATION_RULES_WORKED_EXAMPLE_v0_1`

Role: tests whether TRACE labels translate into Mechanical Ethics without overclaiming.

Tests:

```text
value expression not value possession
mimicry not no-standing conclusion
illustrative threshold not real-world mandate
standing uncertainty not settled standing
```

Result:

```text
translation rules preserve useful advisory/presumptive claims while blocking overclaims
```

Status: bridge test, not validation.

### 3.5 `TRACE_THRESHOLD_REGISTER_STRESS_TEST_v0_1`

Role: tests whether threshold authority changes permission status even when the raw number is unchanged.

Tests:

```text
same risk number
same tolerance number
three threshold statuses: illustrative, provisional, adopted
whether same number implies same permission
whether threshold register blocks convenient-number laundering
```

Result:

```text
illustrative threshold -> no high-stakes pass
provisional threshold -> no pass unless other guards also pass
adopted threshold -> limited pass only if all other guards pass
```

Status:

```text
TRACE_DELTA_PARTIAL, not validation
```

### 3.6 `TRACE_THRESHOLD_REGISTER_STRESS_TEST_ISOLATED_v0_1`

Role: isolates threshold-authority status as the only varied variable.

Tests:

```text
same risk number
same tolerance number
same affected entity
same protected dimension
all non-threshold guards held constant
only threshold status changes
```

Result:

```text
illustrative -> blocked_by_threshold_status
provisional incomplete -> blocked_by_threshold_status
adopted -> limited_pass
```

Status:

```text
TRACE_DELTA_PARTIAL_CLEANER, not validation
```

## 4. Dependency Graph

```text
MATH_KERNEL
  -> FUTURE_SPACE_AND_CONTINUATION
      -> VALUE_SPACE_ALGEBRA
          -> PROBABILISTIC_FLOOR_AND_RISK_GUARD
              -> IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION
              -> NECESSITY_AND_ALTERNATIVE_SEARCH
                  -> PARETO_CHOICE_AND_INCOMPARABILITY
          -> THRESHOLD_REGISTER
  -> REACHABILITY_MODEL
      -> NECESSITY_AND_ALTERNATIVE_SEARCH
  -> UNCERTAINTY_TYPES
      -> PROBABILISTIC_FLOOR_AND_RISK_GUARD
      -> IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION
      -> VALUE_SIGNAL_PROVENANCE_AND_STABILITY
  -> CLOSURE_MODE_AND_VIOLATION
      -> NON_AGGREGATION_GUARD
      -> VALUE_SPACE_ALGEBRA
  -> NON_AGGREGATION_GUARD
      -> VALUE_SPACE_ALGEBRA
      -> PROBABILISTIC_FLOOR_AND_RISK_GUARD
      -> NECESSITY_AND_ALTERNATIVE_SEARCH
  -> THRESHOLD_REGISTER
  -> VALUE_SIGNAL_PROVENANCE_AND_STABILITY
      -> ME_FROM_TRACE_TRANSLATION_RULES
  -> ME_FROM_TRACE_TRANSLATION_RULES
```

## 5. Current Open Seams

The following are still unresolved and should not be pretended solved.

### 5.1 Standing / Affected-Entity Inclusion

Still missing:

```text
how to decide who enters the affected set under standing uncertainty
how to avoid both cheap exclusion and uncontrolled over-attribution
how mimicry/provenance evidence should update standing uncertainty
```

Related files:

```text
TRACE_UNCERTAINTY_TYPES_v0_1
TRACE_VALUE_SIGNAL_PROVENANCE_AND_STABILITY_v0_1
TRACE_NON_AGGREGATION_GUARD_v0_1
```

Potential future file:

```text
TRACE_AFFECTED_ENTITY_AND_STANDING_ENTRY_v0_1.md
```

Do not build until pressure examples show the exact need.

### 5.2 Model-Class Construction for Imprecise Probability

Still missing:

```text
how to construct the plausible measure set in real cases
what counts as model compatibility with uncertainty U
how to bound upper probabilities under weak evidence
```

Related file:

```text
TRACE_IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION_v0_1
```

Do not fake this with point estimates.

### 5.3 High-Stakes Incomparability Authority

Still missing:

```text
who may declare a priority rule
who may declare scalar projection sigma
what external authority is required for unresolved collisions
how refusal/no-selection behaves in institutional systems
```

Related file:

```text
TRACE_PARETO_CHOICE_AND_INCOMPARABILITY_v0_1
```

### 5.4 Mechanical Ethics Translation Robustness

Built file:

```text
ME_FROM_TRACE_TRANSLATION_RULES_v0_1.md
```

Still missing:

```text
more worked cases using different TRACE outputs
reader-facing simplification
clear boundary between advisory and hard-floor translation in non-toy domains
```

### 5.5 Value-Signal Pressure Examples Beyond One Synthetic Case

Built file:

```text
03_TESTS/TRACE_VALUE_SIGNAL_PRESSURE_STABILITY_WORKED_EXAMPLE_v0_1.md
```

Still missing:

```text
non-animal value-signal example
actual model transcript example
case with pressure fragility rather than example stability
standing-gradient comparison across species/entity classes
```

### 5.6 Real Decision Advantage

The threshold-register stress tests show a narrow partial delta:

```text
TRACE distinguishes numerical comparison from authorised threshold use.
```

The isolated threshold-register stress test improves this by holding all non-threshold guards constant.

Still missing:

```text
real-world or realistic case with non-illustrative thresholds
comparator test where no-card reasoning makes a hidden shortcut
case where profile-valued partial order changes the result relative to scalar reasoning
case where TRACE permits a decision ordinary caution would block
```

## 6. Anti-Duplication Rules

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
post-guard incomparability / Pareto choice -> PARETO_CHOICE_AND_INCOMPARABILITY
imprecise probabilities / upper-risk bounds -> IMPRECISE_PROBABILITY_AND_OUTCOME_DISTRIBUTION
threshold source authority -> THRESHOLD_REGISTER
value signal provenance / stability / mimicry / pressure -> VALUE_SIGNAL_PROVENANCE_AND_STABILITY
TRACE-to-ME claim status and translation rules -> ME_FROM_TRACE_TRANSLATION_RULES
```

If a new file needs a concept already owned above, it should reference the owner file rather than redefine it.

## 7. Current Case Flow

A valid TRACE case should now proceed:

```text
1. Identify entity / affected entity set and concrete point p_0.
2. Define x_e(t).
3. Define observation O_e(W(t)) and observation limits.
4. Define uncertainty profile U_e(t), including standing uncertainty where relevant.
5. Define abstract action-space A(t).
6. Define reachability profile Rho_e(a,t) and lived action-space LA_e(t).
7. Define transition distribution or plausible measure set over W(t+dt).
8. Define future-space F_e(t).
9. Map futures to value profiles via C+_e.
10. Compute/profile delta_e(a), floors, severe loss, and livability loss.
11. Check threshold register status for all thresholds used.
12. Identify closure mode CM_e(a), violation, repair route, and responsibility route.
13. Run non-aggregation guard.
14. Run probabilistic floor/tail-risk/severe-loss guard, using upper bounds where imprecision is live.
15. Run necessity and alternative search.
16. If admissible actions remain incomparable, register incomparability and use only declared choice modes.
17. If evaluating a value signal, record provenance, mimicry pressure, update persistence, and pressure stability.
18. Translate into Mechanical Ethics only through ME_FROM_TRACE_TRANSLATION_RULES.
```

## 8. Worked Example Requirements Going Forward

Further worked examples should not introduce new theory.

They should pressure existing files.

Required future tests:

```text
value-signal pressure-fragility test: same value, failure trajectory
standing-entry test: unfamiliar possible subject vs mimicry signal
translation test: non-animal TRACE output -> ME claim labels
realistic case test: non-illustrative thresholds and no-card comparator
```

Threshold-register stress tests are now built and should not be rebuilt as theory.

## 9. Current Best Next Step

Current reviewer verdict:

```text
COHERENT_BUT_OVERBUILT
```

Current narrow achieved delta:

```text
TRACE distinguishes numerical comparison from authorised threshold use.
```

Current improved test status:

```text
isolated threshold-register stress test built
TRACE_DELTA_PARTIAL_CLEANER
```

Current action sequence:

```text
1. stop core theory-build
2. package current stack for fresh-reader / reviewer use
3. run a realistic comparator case with non-illustrative or externally grounded thresholds
```

After this map sync:

```text
no more abstract core files unless a worked example or hostile review forces one
```

## 10. Guardrail

The fresh-AI patch loop has been useful but dangerous.

Do not keep adding abstract files because every review finds another seam.

Current discipline:

```text
build one core file only when it controls an identified failure mode
then run it in a worked example
then update this map
then decide whether another core file is actually required
```

The kernel now needs review pressure and real comparative execution more than new vocabulary.

The threshold-register stress tests are useful partial answers, not validation.
