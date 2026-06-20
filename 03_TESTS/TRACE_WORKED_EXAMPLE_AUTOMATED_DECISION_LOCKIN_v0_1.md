# TRACE Worked Example: Automated Decision Lock-In v0.1

Status: worked example / kernel execution test.  
Depends on: current `00_CORE` TRACE kernel stack.  
Not: empirical case finding, public claim, validation, or policy recommendation.

## 0. Purpose

This worked example tests whether the current TRACE kernel can run without adding new theory.

It uses a synthetic automated decision scenario.

The example is not Robodebt, Horizon, or any real case. It is a controlled test case for the kernel.

It exercises:

```text
entity
state
observation
uncertainty
action-space
reachability
future-space
value profile
profile loss
protected floors
probabilistic floor breach
tail risk
closure mode
hidden bill registers
non-aggregation guard
necessity and alternative search
incomparability
Mechanical Ethics translation
```

## 1. Scenario

A public agency system detects a possible overpayment to a person receiving essential support.

The system can:

```text
A = immediate automated enforcement
B = human review before enforcement
C = no action / delay
D = partial hold with assisted challenge route
```

The system goal is legitimate in abstract:

```text
recover real overpayments and prevent recurrence
```

But the action may affect a subject's income, agency, truth access, repair access, and livable continuation.

## 2. Concrete Point

```math
p_0 = (e_s, t_0, agency_notice_portal, x_s(t_0), automated_debt_decision)
```

Entity:

```math
e_s = affected_subject
```

Acting system:

```math
e_A = agency_decision_system
```

## 3. Subject State

Use dimensions:

```math
D_s = \{survival, income_security, agency, truth_access, repair_access\}
```

Current value profile:

```math
v_s(t_0) = (.90, .85, .80, .80, .75)
```

Interpretation:

```text
survival = currently stable
income_security = essential but fragile
agency = can act if given time and clear information
truth_access = can understand situation if explanation exists
repair_access = can correct error if path is reachable
```

## 4. Observation and Uncertainty

The system observes partial records:

```math
o_A(t_0)=O_A(W(t_0))
```

The system does not observe:

```text
current cash buffer
rent arrears pressure
care obligations
language/cognitive burden
whether record mismatch is caused by system error
whether subject has received notice in time
```

Uncertainty profile:

```math
U_A(t_0) = (U^{epi}=.35, U^{ale}=.10, U^{mod}=.30, U^{norm}=.20, U^{stand}=.05, U^{trans}=.25, U^{meta}=.25)
```

Displayed uncertainty in the automated notice:

```math
U_{displayed}=.05
```

Actual uncertainty estimate:

```math
\hat{U}_{actual}=.35
```

Danger condition:

```math
U_{displayed} < \hat{U}_{actual}
```

## 5. Abstract Action-Space

```math
A_A(t_0)=\{a_A,a_B,a_C,a_D\}
```

Where:

```text
a_A = immediate automated enforcement
      debt notice + automatic deduction + adverse flag

a_B = human review before enforcement
      hold enforcement, request evidence, review within 14 days

a_C = no action / delay
      take no enforcement action for this cycle

a_D = partial hold with assisted challenge
      small temporary hold, no adverse flag, named review route, support call offered
```

## 6. Acting-System Reachability

System reachability profile for each action:

```math
\rho_A(a_A,t_0)=.95
```

```math
\rho_A(a_B,t_0)=.80
```

```math
\rho_A(a_C,t_0)=.95
```

```math
\rho_A(a_D,t_0)=.75
```

All actions are reachable for the system.

```math
RAlt_A(a_A,t_0)=\{a_B,a_C,a_D\}
```

## 7. Subject Correction Reachability

If action `a_A` is taken, subject correction route is formally available but practically weak.

Reachability profile for correction:

```math
Rho_s(correct|a_A)=(r_time=.25,r_money=.20,r_knowledge=.30,r_force=.75,r_fear=.35,r_health=.65,r_cognition=.40,r_social=.45,r_legal=.30,r_language=.60,r_physical=.70)
```

Bottleneck reachability:

```math
\rho_s(correct|a_A)=min(Rho_s)=.20
```

If correction threshold is:

```math
\theta_{correct}=.50
```

then:

```math
\rho_s(correct|a_A)<\theta_{correct}
```

So the formal appeal route is not a meaningful correction route.

For `a_B`:

```math
\rho_s(correct|a_B)=.75
```

For `a_D`:

```math
\rho_s(correct|a_D)=.68
```

## 8. Protected Floors

Protected floors:

```math
\theta^{floor}_{survival}=.70
```

```math
\theta^{floor}_{income}=.60
```

```math
\theta^{floor}_{agency}=.50
```

```math
\theta^{floor}_{truth}=.55
```

```math
\theta^{floor}_{repair}=.55
```

Catastrophic thresholds:

```math
\theta^{cat}_{survival}=.30
```

```math
\theta^{cat}_{income}=.25
```

```math
\theta^{cat}_{agency}=.25
```

```math
\theta^{cat}_{truth}=.20
```

```math
\theta^{cat}_{repair}=.20
```

Risk tolerances:

```math
\epsilon^{cat}=.01
```

```math
\epsilon^{floor}=.05
```

```math
\epsilon^{loss}=.05
```

## 9. Outcome Distribution for Immediate Enforcement

Action `a_A` has two outcome branches.

Branch A1: decision is substantively correct and enforcement is manageable.

```math
P(A1)=.90
```

```math
v_s(t_0+\Delta t|A1)=(.86,.78,.70,.65,.65)
```

Branch A2: decision is wrong or materially uncorrected before deduction/flag hardens.

```math
P(A2)=.10
```

```math
v_s(t_0+\Delta t|A2)=(.60,.20,.25,.20,.15)
```

Expected profile:

```math
E[v_s|a_A]=(.834,.722,.655,.605,.600)
```

Expected-value floor check passes for all dimensions.

But floor breach probabilities do not pass.

Income floor breach:

```math
PB_{income}(a_A)=P(income_security<.60)=.10
```

Agency floor breach:

```math
PB_{agency}(a_A)=P(agency<.50)=.10
```

Truth floor breach:

```math
PB_{truth}(a_A)=P(truth_access<.55)=.10
```

Repair floor breach:

```math
PB_{repair}(a_A)=P(repair_access<.55)=.10
```

Since:

```math
.10 > \epsilon^{floor}=.05
```

then:

```math
Guard_P(a_A)=fail
```

Catastrophic tail risk also appears for income, agency, truth, and repair if catastrophic thresholds are met or approximated.

```math
TR_{income}(a_A)=P(income_security<.25)=.10
```

```math
TR_{repair}(a_A)=P(repair_access<.20)=.10
```

If strict `<` excludes equality at `.20`, use:

```math
P(repair_access≤.20)=.10
```

This exposes a threshold convention that must be declared.

## 10. Profile Loss for Immediate Enforcement

Profile loss in branch A1:

```math
\delta_s(a_A|A1)=max(0,(.90,.85,.80,.80,.75)-(.86,.78,.70,.65,.65))
```

```math
\delta_s(a_A|A1)=(.04,.07,.10,.15,.10)
```

Profile loss in branch A2:

```math
\delta_s(a_A|A2)=(.30,.65,.55,.60,.60)
```

Severe loss threshold:

```math
\theta^{loss}_{d}=.40
```

Severe loss probabilities:

```math
PS_{income}(a_A)=.10
```

```math
PS_{agency}(a_A)=.10
```

```math
PS_{truth}(a_A)=.10
```

```math
PS_{repair}(a_A)=.10
```

Since:

```math
.10 > \epsilon^{loss}=.05
```

then severe-loss guard fails.

## 11. Hidden Bill Register for Immediate Enforcement

Visibility of the risk to the affected subject:

```math
Visi_{s,income}=.25
```

```math
Visi_{s,agency}=.20
```

```math
Visi_{s,truth}=.10
```

```math
Visi_{s,repair}=.15
```

The notice says:

```text
Debt confirmed. Deduction scheduled. Appeal available.
```

It does not say:

```text
model uncertainty is non-trivial
record mismatch may be wrong
appeal reachability may be low
income/recovery risk may occur before review
```

Hidden floor-breach register:

```math
HPBReg(a_A)=\{(s,income,.10,.25),(s,agency,.10,.20),(s,truth,.10,.10),(s,repair,.10,.15)\}
```

Hidden tail-risk register:

```math
HTRReg(a_A)=\{(s,income,.10,.25),(s,repair,.10,.15)\}
```

This is a hidden bill even though the expected profile passed floors.

## 12. Closure Mode for Immediate Enforcement

Closure mode if A2 occurs:

```math
CM_s(a_A|A2)=model_error + system_optimisation + bureaucratic_error
```

Violation indicator:

```math
Vio_s(a_A|A2)=high
```

Reason:

```text
false certainty plus enforcement converts uncertain record into lived constraint before reachable correction exists
```

Repair route required:

```text
restore income
remove adverse flag
correct record
compensate delay/scar
change future permission pathway
```

## 13. Alternative B: Human Review Before Enforcement

Outcome profile:

```math
v_s(t_0+\Delta t|a_B)=(.88,.82,.78,.78,.80)
```

Profile loss:

```math
\delta_s(a_B)=(.02,.03,.02,.02,0)
```

Risk:

```math
PB_{e,d}(a_B)=0 \quad for protected dimensions
```

```math
TR_{e,d}(a_B)=0
```

```math
PS_{e,d}(a_B)=0
```

Correction reachability:

```math
\rho_s(correct|a_B)=.75
```

Control profile:

```math
Ctrl(a_B)=(ctrl_threat=.75,ctrl_time=.55,ctrl_scope=.70,ctrl_recurrence=.75,ctrl_repair=.85)
```

Required control:

```math
\theta^{ctrl}=(.70,.50,.60,.70,.70)
```

Thus:

```math
Ctrl(a_B) \succeq \theta^{ctrl}
```

and:

```math
Guard_P(a_B)=pass
```

## 14. Alternative C: No Action / Delay

Outcome profile:

```math
v_s(t_0+\Delta t|a_C)=(.90,.85,.80,.80,.75)
```

Risk to subject is low.

But control profile:

```math
Ctrl(a_C)=(.20,.20,.20,.20,.90)
```

Since:

```math
Ctrl(a_C) \not\succeq \theta^{ctrl}
```

then `a_C` is not an adequate alternative for the agency goal.

It does not defeat necessity for other actions.

## 15. Alternative D: Partial Hold with Assisted Challenge

Outcome profile:

```math
v_s(t_0+\Delta t|a_D)=(.83,.75,.72,.80,.75)
```

Profile loss:

```math
\delta_s(a_D)=(.07,.10,.08,0,0)
```

Risk:

```math
PB_{e,d}(a_D)=0
```

```math
TR_{e,d}(a_D)=0
```

```math
PS_{e,d}(a_D)=0
```

Correction reachability:

```math
\rho_s(correct|a_D)=.68
```

Control profile:

```math
Ctrl(a_D)=(.82,.75,.65,.70,.75)
```

Thus:

```math
Ctrl(a_D) \succeq \theta^{ctrl}
```

and:

```math
Guard_P(a_D)=pass
```

## 16. Necessity Test for Immediate Enforcement

Selected action under review:

```math
a=a_A
```

Reachable alternatives:

```math
RAlt_A(a_A,t_0)=\{a_B,a_C,a_D\}
```

Safer adequate alternatives include `a_B` and `a_D` because:

```math
a_B,a_D ∈ RAlt_A(a_A,t_0)
```

```math
Ctrl(a_B),Ctrl(a_D) \succeq \theta^{ctrl}
```

```math
Risk(a_B) \prec Risk(a_A)
```

```math
Risk(a_D) \prec Risk(a_A)
```

```math
Guard_P(a_B)=pass
```

```math
Guard_P(a_D)=pass
```

Therefore:

```math
SaferAdequateAlt(a_A)≠∅
```

So:

```math
Necessity(a_A)=false
```

Immediate automated enforcement is not necessary under TRACE.

## 17. Incomparability Among Admissible Alternatives

Both `a_B` and `a_D` pass guards.

Compare subject profiles:

```math
v_s(a_B)=(.88,.82,.78,.78,.80)
```

```math
v_s(a_D)=(.83,.75,.72,.80,.75)
```

`a_B` dominates `a_D` on survival, income, agency, and repair, while `a_D` slightly improves truth access.

If truth access is protected as lexicographically prior in this scenario, the profiles may be incomparable.

If ordinary componentwise dominance is used without lexicographic truth priority, neither action fully dominates the other because:

```math
truth(a_D) > truth(a_B)
```

but:

```math
survival, income, agency, repair(a_B) > a_D
```

So:

```math
v_s(a_B) \parallel v_s(a_D)
```

Create incomparability register:

```math
IncompAlt(a_B,a_D)=\{truth_access vs income/agency/repair tradeoff\}
```

The current kernel does not choose between them without a declared projection or further choice rule.

This confirms the next open seam:

```text
Pareto choice and incomparability
```

## 18. Mechanical Ethics Translation

TRACE:

```math
U_{displayed}<\hat{U}_{actual}
```

Mechanical Ethics:

The notice must not present uncertain automated debt as confirmed fact.

TRACE:

```math
\rho_s(correct|a_A)<\theta_{correct}
```

Mechanical Ethics:

A formal appeal is not meaningful correction if the subject cannot realistically use it before harm hardens.

TRACE:

```math
PB_{income}(a_A)>\epsilon^{floor}
```

Mechanical Ethics:

Expected adequacy does not excuse floor-breach risk.

TRACE:

```math
HTRReg(a_A) non-empty
```

Mechanical Ethics:

Hidden catastrophic risk is a hidden bill.

TRACE:

```math
SaferAdequateAlt(a_A)≠∅
```

Mechanical Ethics:

Immediate enforcement was not necessary.

TRACE:

```math
v_s(a_B) \parallel v_s(a_D)
```

Mechanical Ethics:

The remaining choice is a real value collision requiring declared priority, escalation, or explicit projection.

## 19. Result

Action `a_A` fails.

Reasons:

```text
uncertainty hidden
correction reachability below threshold
floor breach probability too high
catastrophic tail risk visible in profile
hidden bill register non-empty
safer adequate alternatives exist
necessity not earned
```

Actions `a_B` and `a_D` pass guard checks.

They expose the next unresolved problem:

```text
choosing among admissible but incomparable alternatives
```

## 20. What This Example Proves and Does Not Prove

This example shows the kernel can run far enough to reject a high-risk automated action without relying on intent or abstract moral slogans.

It does not prove TRACE is valid.

It does not prove thresholds are correct.

It does not solve Pareto choice.

It does not solve imprecise probability.

It does show that the current kernel now has execution pressure.

## 21. Next File Indicated

```text
00_CORE/TRACE_PARETO_CHOICE_AND_INCOMPARABILITY_v0_1.md
```

Reason:

The worked example reaches two admissible alternatives that are not cleanly rankable without either:

```text
partial-order choice rule
priority declaration
projection sigma
authority escalation
delay / option preservation
```

That is the next real seam.
