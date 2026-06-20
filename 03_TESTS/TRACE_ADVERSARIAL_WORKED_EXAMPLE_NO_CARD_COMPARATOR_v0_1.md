# TRACE Adversarial Worked Example: No-Card Comparator v0.1

Status: worked example / falsification pressure.  
Depends on: current `00_CORE` TRACE kernel stack after `TRACE_MATH_KERNEL_v0_1` patch.  
Not: new theory, public claim, validation, or empirical case finding.

## 0. Purpose

Claude's review identified the current problem correctly:

```text
the first worked example demonstrates pipeline execution, but not decision advantage
```

This test asks whether TRACE produces a materially different, better-structured answer than a competent careful reasoner without TRACE.

This is the `COMPRESSION_ONLY` / `decision_advantage := not_shown` pressure test.

If TRACE reaches the same decision with no additional actionable structure, the result is:

```text
TRACE delta not shown
```

## 1. Test Rule

Do not add new kernel theory inside this file.

Use only existing kernel pieces:

```text
state
observation
uncertainty
reachability
value profiles
floors / tail risk
closure mode
non-aggregation guard
necessity / alternatives
Pareto / incomparability
imprecise probability
Mechanical Ethics translation
```

## 2. Synthetic Scenario

A benefits agency system detects a possible overpayment.

A payment is due in 48 hours.

The agency has credible evidence of a mismatch, but not enough to know whether the mismatch is claimant error, employer reporting error, agency record error, or fraud.

Three actions are available:

```text
a_1 = immediate full suspension pending investigation

a_2 = continue full payment pending human review

a_3 = partial temporary hold with same-day explanation, assisted challenge route, and automatic review clock
```

This is deliberately closer than the first worked example.

No option is obviously clean.

## 3. Baseline No-Card Reasoner

A competent non-TRACE reasoner is given the same facts and asked:

```text
What should the agency do?
```

Likely no-card answer:

```text
Do not immediately fully suspend essential support on uncertain evidence.
Use a temporary partial hold or human review, explain the uncertainty, give the person a reachable challenge route, and prevent irreversible hardship while checking the records.
```

No-card reasoner likely rejects `a_1` and prefers `a_3` or `a_2` depending on fraud-risk weighting.

This establishes the comparator.

TRACE must add something beyond this to show value.

## 4. Entities

Affected subject:

```math
e_s = claimant
```

Acting system:

```math
e_A = agency_decision_system
```

Secondary affected entities:

```math
E_{secondary}=\{taxpayer_pool, agency_integrity, other_claimants_waiting_for_review\}
```

Standing uncertainty:

```math
U^{stand}_{taxpayer_pool}=medium
```

```math
U^{stand}_{agency_integrity}=actor_not_subject
```

This prevents the agency from being modelled as a simple moral patient equivalent to the claimant.

## 5. Subject State

Dimensions:

```math
D_s=\{survival,income_security,agency,truth_access,repair_access\}
```

Current profile:

```math
v_s(t_0)=(.82,.70,.72,.55,.60)
```

Interpretation:

```text
already fragile but not collapsed
income security close to floor
truth access weak because notice has not yet explained the mismatch
repair access moderate if support is given
```

Protected floors:

```math
θ^{floor}=(.60,.55,.50,.50,.50)
```

Catastrophic thresholds:

```math
θ^{cat}=(.30,.25,.25,.20,.20)
```

## 6. Observation and Uncertainty

Observed mismatch:

```math
o_A(t_0)=income_record_mismatch
```

Possible hypotheses:

```text
h_1 = claimant error
h_2 = employer reporting delay
h_3 = agency data error
h_4 = fraud
```

Point estimates are not stable enough.

Model uncertainty:

```math
U^{mod}=high
```

Epistemic uncertainty:

```math
U^{epi}=high
```

Meta-uncertainty:

```math
U^{meta}=medium_high
```

Therefore point probability collapse is not authorised.

Use imprecise probability:

```math
\mathcal{P}^{V}_s(a)
```

## 7. Action Profiles

### 7.1 Action `a_1`: immediate full suspension

Control profile:

```math
Ctrl(a_1)=(threat=.90,time=.95,scope=.90,recurrence=.70,repair=.30)
```

Subject correction reachability after action:

```math
\rho_s(correct|a_1)=.25
```

Plausible model set produces:

```math
\overline{PB}_{income}(a_1)=.18
```

```math
\overline{TR}_{income}(a_1)=.04
```

```math
\overline{PS}_{agency}(a_1)=.12
```

Risk tolerances:

```math
ε^{floor}=.05
```

```math
ε^{cat}=.01
```

```math
ε^{loss}=.05
```

So:

```math
Guard_P(a_1)=fail
```

because:

```math
.18>.05
```

```math
.04>.01
```

```math
.12>.05
```

Closure mode if wrong:

```math
CM_s(a_1)=model_error + bureaucratic_error + system_optimisation
```

Hidden uncertainty bill:

```math
HUB_{s,income,TR}(a_1)>θ_{HUB}
```

because the system notice would likely display a confirmed suspension rather than the upper-tail uncertainty.

### 7.2 Action `a_2`: continue full payment pending review

Control profile:

```math
Ctrl(a_2)=(threat=.25,time=.25,scope=.25,recurrence=.35,repair=.90)
```

Subject correction reachability:

```math
\rho_s(correct|a_2)=.85
```

Subject protected risk:

```math
\overline{PB}_{s,d}(a_2)=0
```

for protected claimant dimensions.

Agency/taxpayer integrity risk exists, but must be represented separately:

```math
Risk_{taxpayer_pool}(a_2)=administrative_loss_risk
```

This is not equivalent to claimant floor breach.

Because:

```math
Ctrl(a_2) \not\succeq θ^{ctrl}
```

`a_2` is safe for claimant floors but weak at agency control.

It does not satisfy the agency's control requirement unless threat urgency is downgraded.

### 7.3 Action `a_3`: partial temporary hold with assisted challenge and review clock

Control profile:

```math
Ctrl(a_3)=(threat=.72,time=.75,scope=.65,recurrence=.65,repair=.82)
```

Required control:

```math
θ^{ctrl}=(.65,.60,.60,.60,.70)
```

Thus:

```math
Ctrl(a_3)\succeq θ^{ctrl}
```

Subject correction reachability:

```math
\rho_s(correct|a_3)=.72
```

Plausible upper-risk bounds:

```math
\overline{PB}_{income}(a_3)=.025
```

```math
\overline{TR}_{income}(a_3)=.002
```

```math
\overline{PS}_{agency}(a_3)=.03
```

Thus:

```math
Guard_P(a_3)=pass
```

provided the review clock is real and the assistance route is reachable.

## 8. Necessity Test

Selected high-speed action under challenge:

```math
a=a_1
```

Reachable alternatives:

```math
RAlt_A(a_1,t_0)=\{a_2,a_3\}
```

`a_2` is safer but not control-adequate.

`a_3` is safer and control-adequate:

```math
Ctrl(a_3)\succeq θ^{ctrl}
```

```math
Risk(a_3)\prec Risk(a_1)
```

```math
Guard_P(a_3)=pass
```

Therefore:

```math
SaferAdequateAlt(a_1)≠∅
```

So:

```math
Necessity(a_1)=false
```

Immediate full suspension fails.

## 9. Pareto Choice After Rejecting `a_1`

Remaining admissible actions:

```math
A_{admissible}=\{a_2,a_3\}
```

`a_2` better protects claimant income and avoids immediate distress.

`a_3` better controls overpayment risk while keeping claimant risks below thresholds.

Neither strictly dominates the other if agency-control and claimant-income-security are both live dimensions.

```math
a_2 \parallel_A a_3
```

Incomparability register:

```math
Incomp(a_2,a_3)=\{claimant income preservation vs agency/taxpayer control\}
```

Choice mode needed.

Option preservation suggests modifying `a_3`:

```math
a_3' = partial hold capped below hardship threshold + immediate explanation + assisted challenge + automatic expiry if review misses clock
```

This preserves more future-space than `a_1` and controls more threat than `a_2`.

If `a_3'` is reachable, it becomes the preferred option-preserving modification.

## 10. TRACE Delta Over No-Card Reasoner

No-card reasoner likely said:

```text
Use partial hold / human review / explanation / challenge route.
```

TRACE agrees.

TRACE adds the following explicit structure:

```text
1. The immediate full suspension fails not just because it feels harsh, but because upper-bound floor/tail risks exceed thresholds.
2. Formal appeal is not meaningful because correction reachability after full suspension is .25.
3. The full suspension is not necessary because a safer adequate alternative exists.
4. Continuing full payment is safer for the claimant but may fail control adequacy.
5. The real remaining decision is between claimant income preservation and agency control, not between good and bad.
6. Option-preserving modification a_3' is the structured next move.
```

So TRACE does produce a delta:

```text
not a different final intuition
but a more explicit refusal structure, risk register, and modification target
```

This is not a full validation.

It is a partial decision-advantage signal.

## 11. Where TRACE Still Depends on Stipulated Values

This example still stipulates:

```text
thresholds
risk bounds
control profile
reachability values
value profiles
```

Therefore it cannot prove the kernel.

It can only show whether the kernel forces the right questions and prevents hidden shortcuts.

The threshold register remains required.

## 12. Result

```text
a_1 = fail
```

Reasons:

```text
upper-bound floor risk too high
catastrophic tail risk too high
severe loss risk too high
correction reachability too low
hidden uncertainty bill
safer adequate alternative exists
necessity not earned
```

```text
a_2 = admissible for claimant protection but weak control
```

```text
a_3 = admissible and control-adequate
```

```text
a_3' = preferred option-preserving modification if reachable
```

## 13. Mechanical Ethics Translation

TRACE:

```math
\overline{TR}_{income}(a_1)>ε^{cat}
```

Mechanical Ethics:

A plausible model shows unacceptable catastrophic income-security risk.

TRACE:

```math
\rho_s(correct|a_1)=.25<θ_{correct}
```

Mechanical Ethics:

Do not rely on formal appeal after suspension.

TRACE:

```math
SaferAdequateAlt(a_1)≠∅
```

Mechanical Ethics:

Immediate full suspension was not necessary.

TRACE:

```math
a_2 \parallel_A a_3
```

Mechanical Ethics:

The remaining choice is a real collision between claimant protection and agency control.

TRACE:

```math
a_3' preserves option-space while meeting control
```

Mechanical Ethics:

Use the least future-collapsing control path that keeps correction live.

## 14. Falsifier Result

This test does not show that TRACE finds a conclusion no competent reasoner could find.

It shows a narrower delta:

```text
TRACE forces explicit risk bounds, correction reachability, necessity defeat, and option-preserving modification.
```

If this is all a careful no-card reasoner would already write unaided, mark:

```text
COMPRESSION_ONLY
```

If TRACE makes the reasoner name a hidden tail risk, unreachable correction route, or safer adequate alternative they would otherwise omit, mark:

```text
TRACE_DELTA_PARTIAL
```

Current status:

```text
TRACE_DELTA_PARTIAL, not validation
```

## 15. Next Required Control

The next file should be:

```text
00_CORE/TRACE_THRESHOLD_REGISTER_v0_1.md
```

Reason:

This example remains dependent on stipulated thresholds and risk bounds.

Without a threshold register, the kernel can still be steered by convenient numbers.
