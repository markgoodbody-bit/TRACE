#!/usr/bin/env python3
"""Exact finite attacks on proposed compass/hope claims; invented probabilities.

Run: python3 countermodels.py [--output RESULTS.json]
No dependencies, random sampling, empirical estimates, or private case material.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


CHECKS = []
GROUPS = {}


def check(group, name, actual, expected):
    ok = actual == expected
    CHECKS.append({"group": group, "name": name, "pass": ok})
    if not ok:
        raise AssertionError(f"{group}/{name}: {actual!r} != {expected!r}")


def check_true(group, name, condition):
    check(group, name, bool(condition), True)


def bernoulli(p):
    return ((False, 1 - p), (True, p))


def independent(*variables):
    """Enumerate an expressly stipulated product distribution."""
    result = []
    for row in product(*variables):
        vals, probs = zip(*row)
        weight = F(1)
        for p in probs:
            weight *= p
        result.append((vals, weight))
    assert sum(p for _, p in result) == 1
    return result


def probability(dist, predicate):
    assert sum(p for _, p in dist) == 1
    return sum((p for v, p in dist if predicate(v)), F(0))


def bellman_trap():
    g = "bellman_trap"
    hidden = (("left", F(1, 2)), ("right", F(1, 2)))
    blind = probability(hidden, lambda world: world == "left")
    inspect_then_choose = probability(hidden, lambda world: world == world)
    q = {"blind_left": blind, "blind_right": blind,
         "inspect_then_choose": inspect_then_choose}
    optimum = max(q.values())
    check(g, "unrestricted_initial_optimum", optimum, F(1))
    check(g, "optimal_enabling_old_delta", inspect_then_choose - optimum, F(0))
    check(g, "paired_gain_over_blind_plan", inspect_then_choose - blind, F(1, 2))
    check_true(g, "all_old_deltas_nonpositive", all(v - optimum <= 0 for v in q.values()))
    GROUPS[g] = {"old_delta": inspect_then_choose - optimum,
                 "paired_plan_delta": inspect_then_choose - blind}


def filtering_and_capability_cost():
    g = "filtering_and_capability_cost"
    j = {"harmful_shortcut": F(9, 10), "permitted_route": F(3, 5)}
    all_policies = set(j)
    admissible = {"permitted_route"}
    before = max(j[p] for p in all_policies)
    after = max(j[p] for p in admissible)
    check(g, "filtering_can_lower_selected_goal_optimum", after - before, F(-3, 10))
    check_true(g, "admissibility_filter_is_subset", admissible <= all_policies)
    empty = all_policies & set()
    check(g, "incompatible_floor_can_leave_empty_menu", len(empty), 0)
    old = {"old_route": F(4, 5)}
    nested = {**old, "free_new_route": F(3, 5)}
    costly = {"new_route_after_spending_old_route_budget": F(3, 5)}
    check(g, "free_nested_menu_cannot_lower_max", max(nested.values()), F(4, 5))
    check(g, "construction_cost_can_lower_available_value", max(costly.values()) - max(old.values()), F(-1, 5))
    GROUPS[g] = {"filtering_delta": after - before,
                 "costly_capability_delta": max(costly.values()) - max(old.values()),
                 "meaning": "Normative permission and physical opportunity are separate inputs; neither is established by maximising a goal."}


def regard_not_weight():
    g = "regard_not_weight"
    # These stipulated comparable toy utilities are not measurements of persons.
    outcomes = {"exploit": (F(100), F(-10)), "cooperate": (F(5), F(5))}
    weights = (F(1), F(1, 1000))
    scores = {a: sum(w * v for w, v in zip(weights, vals)) for a, vals in outcomes.items()}
    selected = max(scores, key=scores.get)
    floor_menu = [a for a, vals in outcomes.items() if vals[1] >= 0]
    check_true(g, "both_weights_positive", all(w > 0 for w in weights))
    check(g, "positive_weight_still_selects_harm", selected, "exploit")
    check(g, "declared_floor_changes_menu", floor_menu, ["cooperate"])
    check(g, "exploit_weighted_score", scores["exploit"], F(9999, 100))
    GROUPS[g] = {"selected_with_positive_weights": selected,
                 "selected_with_declared_floor": floor_menu[0],
                 "meaning": "A positive weight does not establish adequate regard, legitimate floors, consent, or representation."}


def reliance_and_assurance():
    g = "reliance_and_assurance"
    # Support is observed before the fallback deadline. A certainty announcement
    # induces cancellation of the fallback; it does not improve support delivery.
    dist = independent(bernoulli(F(1, 4)), bernoulli(F(3, 4)))
    physical_delivery = probability(dist, lambda v: v[0])
    keep_fallback = probability(dist, lambda v: v[0] or v[1])
    cancel_fallback = probability(dist, lambda v: v[0])
    menus = {"conditional_disclosure": {"use_support", "use_fallback"},
             "certainty_then_cancellation": {"use_support"}}
    check(g, "support_probability_unchanged_by_words", physical_delivery, F(1, 4))
    check(g, "conditional_plan_success", keep_fallback, F(13, 16))
    check(g, "assurance_induced_plan_success", cancel_fallback, F(1, 4))
    check(g, "loss_due_to_reliance_policy", cancel_fallback - keep_fallback, F(-9, 16))
    check_true(g, "fallback_cancellation_strictly_shrinks_menu", menus["certainty_then_cancellation"] < menus["conditional_disclosure"])
    GROUPS[g] = {"physical_support": physical_delivery,
                 "keep_fallback": keep_fallback, "cancel_fallback": cancel_fallback,
                 "causal_loss_in_stipulated_model": cancel_fallback - keep_fallback,
                 "meaning": "The effect is mediated by a specified receiver policy and actual cancellation, not a theorem that every false statement worsens every outcome."}


def commitment_does_not_create_capacity():
    g = "commitment_does_not_create_capacity"
    physical = {False: F(2, 5), True: F(2, 5)}
    check(g, "recorded_commitment_does_not_change_fixed_transition", physical[True], physical[False])
    check(g, "promise_not_probability_one", physical[True], F(2, 5))
    check_true(g, "failure_remains_possible", physical[True] < 1)
    GROUPS[g] = {"delivery_without_promise": physical[False],
                 "delivery_with_promise_same_resources_and_policy": physical[True],
                 "meaning": "A commitment may motivate later actions in a fuller model; the statement alone is not delivered capacity or a guarantee."}


def causal_announcement_confounding():
    g = "causal_announcement_confounding"
    # C~Bernoulli(1/2); observational Z=C, Y=C. Intervention sets Z but
    # does not alter the C->Y structural equation.
    capacity = bernoulli(F(1, 2))
    observed = [((c, c), p) for c, p in capacity]
    obs_z1 = sum(p for (z, _), p in observed if z)
    obs_y1_z1 = sum(p for (z, y), p in observed if z and y) / obs_z1
    do_z1 = probability(capacity, lambda c: c)
    do_z0 = probability(capacity, lambda c: c)
    check(g, "observed_success_given_announcement", obs_y1_z1, F(1))
    check(g, "intervention_announcement_success", do_z1, F(1, 2))
    check(g, "causal_announcement_effect_zero", do_z1 - do_z0, F(0))
    check_true(g, "association_not_intervention", obs_y1_z1 != do_z1)
    GROUPS[g] = {"P_success_given_announcement": obs_y1_z1,
                 "P_success_do_announcement": do_z1,
                 "causal_effect": do_z1 - do_z0}


def complementary_support():
    g = "complementary_support"
    value = {(a, b): F(int(a and b)) for a, b in product((False, True), repeat=2)}
    marginal_a_without_b = value[True, False] - value[False, False]
    marginal_a_with_b = value[True, True] - value[False, True]
    interaction = value[True, True] - value[True, False] - value[False, True] + value[False, False]
    check(g, "first_support_alone", marginal_a_without_b, F(0))
    check(g, "first_support_with_complement", marginal_a_with_b, F(1))
    check(g, "nonadditive_interaction", interaction, F(1))
    check_true(g, "zero_standalone_gain_does_not_imply_useless", marginal_a_without_b == 0 and marginal_a_with_b > 0)
    GROUPS[g] = {"marginal_without_complement": marginal_a_without_b,
                 "marginal_with_complement": marginal_a_with_b,
                 "interaction": interaction}


def shared_budget():
    g = "shared_budget"
    demand_a, demand_b, budget = 1, 1, 1
    check_true(g, "first_commitment_individually_feasible", demand_a <= budget)
    check_true(g, "second_commitment_individually_feasible", demand_b <= budget)
    check(g, "combined_commitment_infeasible", demand_a + demand_b <= budget, False)
    feasible_allocations = [(a, b) for a, b in product((0, 1), repeat=2) if a + b <= budget]
    check(g, "no_joint_allocation", (1, 1) in feasible_allocations, False)
    check(g, "capacity_increase_restores_joint_feasibility", demand_a + demand_b <= 2, True)
    GROUPS[g] = {"feasible_allocations": feasible_allocations,
                 "meaning": "Individual promises must be checked against the joint allocation; a claimant's standing does not create resources."}


def correlated_support():
    g = "correlated_support"
    # Both devices depend on the same supply Z, available with probability 4/5.
    same_supply = [((z, z), p) for z, p in bernoulli(F(4, 5))]
    first = probability(same_supply, lambda v: v[0])
    second = probability(same_supply, lambda v: v[1])
    both = probability(same_supply, lambda v: v[0] and v[1])
    either = probability(same_supply, lambda v: v[0] or v[1])
    naive_both = first * second
    naive_either = 1 - (1 - first) * (1 - second)
    check(g, "actual_both", both, F(4, 5))
    check(g, "naive_both_wrong", naive_both, F(16, 25))
    check(g, "actual_either_no_redundancy", either, F(4, 5))
    check(g, "naive_redundancy_overclaims", naive_either, F(24, 25))
    GROUPS[g] = {"actual_both": both, "product_of_marginals": naive_both,
                 "actual_either": either, "independent_redundancy_claim": naive_either}


def finite_viability(initial_states, support_sequence):
    """Deterministic mandatory one-unit service each period; capacity must stay >=1.

    Support arrives before service. Capacity saturates at two; no hidden action
    or chance model is smuggled into this simple backward viability calculation.
    """
    safe = {1, 2}
    kernel = set(safe)
    kernels = [set(kernel)]
    for support in reversed(support_sequence):
        kernel = {x for x in safe if min(2, x + int(support)) - 1 in kernel}
        kernels.append(set(kernel))
    return set(initial_states) & kernel, list(reversed(kernels))


def attainment_vs_sustaining():
    g = "attainment_vs_sustaining"
    trajectories = [((1, 1, 0), F(1, 2)), ((1, 1, 1), F(1, 2))]
    attainment = probability(trajectories, lambda xs: any(x == 1 for x in xs))
    sustained = probability(trajectories, lambda xs: all(x == 1 for x in xs))
    k_no, sequence_no = finite_viability({1, 2}, [False, False])
    k_yes, sequence_yes = finite_viability({1, 2}, [True, True])
    k_one, _ = finite_viability({1, 2}, [False])
    check(g, "attainment_probability", attainment, F(1))
    check(g, "sustained_probability", sustained, F(1, 2))
    check(g, "one_period_viable_without_support", k_one, {2})
    check(g, "two_period_kernel_empty_without_support", k_no, set())
    check(g, "two_period_kernel_with_support", k_yes, {1, 2})
    GROUPS[g] = {"attainment": attainment, "sustained": sustained,
                 "unsupported_kernels_t0_t1_t2": sequence_no,
                 "supported_kernels_t0_t1_t2": sequence_yes}


def per_step_risk():
    g = "per_step_risk"
    dist = independent(bernoulli(F(9, 10)), bernoulli(F(9, 10)))
    first = probability(dist, lambda xs: xs[0])
    second = probability(dist, lambda xs: xs[1])
    horizon = probability(dist, all)
    union_lower_bound = 1 - ((1 - first) + (1 - second))
    check(g, "first_step_success", first, F(9, 10))
    check(g, "second_step_success", second, F(9, 10))
    check(g, "horizon_success", horizon, F(81, 100))
    check_true(g, "per_step_threshold_not_horizon_threshold", first >= F(9, 10) and second >= F(9, 10) and horizon < F(9, 10))
    check_true(g, "union_bound_is_valid_here", horizon >= union_lower_bound)
    GROUPS[g] = {"per_step": first, "whole_horizon": horizon,
                 "union_bound": union_lower_bound}


def nonanticipative_policy():
    g = "nonanticipative_policy"
    # No observation distinguishes two worlds. One response must be selected
    # using the same information; q is the chance of choosing left.
    def values(q):
        return (q, 1 - q)
    deterministic = max(min(values(q)) for q in (F(0), F(1)))
    grid = [F(i, 100) for i in range(101)]
    randomized = max(min(values(q)) for q in grid)
    clairvoyant = min(max(values(q)[m] for q in (F(0), F(1))) for m in (0, 1))
    check(g, "common_deterministic_robust_value", deterministic, F(0))
    check(g, "common_randomized_robust_value", randomized, F(1, 2))
    check(g, "model_specific_clairvoyant_value", clairvoyant, F(1))
    check_true(g, "universal_randomized_upper_bound_on_grid", all(min(values(q)) <= F(1, 2) for q in grid))
    check_true(g, "clairvoyant_swap_overstates_implementable_value", clairvoyant > randomized)
    GROUPS[g] = {"max_policy_min_model_deterministic": deterministic,
                 "max_policy_min_model_randomized": randomized,
                 "min_model_max_policy_clairvoyant": clairvoyant,
                 "analytic_upper_bound": "min(q,1-q) <= (q+1-q)/2 = 1/2 for every q in [0,1]; equality at q=1/2."}


def paired_model_difference():
    g = "paired_model_difference"
    js = {"m1": (F(2, 5), F(3, 10)), "m2": (F(9, 10), F(4, 5))}
    paired = [candidate - reference for candidate, reference in js.values()]
    paired_range = (min(paired), max(paired))
    unpaired = (min(c for c, _ in js.values()) - max(r for _, r in js.values()),
                max(c for c, _ in js.values()) - min(r for _, r in js.values()))
    check(g, "paired_range_preserves_same_model", paired_range, (F(1, 10), F(1, 10)))
    check(g, "unpaired_range_unnecessarily_wide", unpaired, (F(-2, 5), F(3, 5)))
    check_true(g, "all_models_agree_candidate_better", all(d > 0 for d in paired))
    GROUPS[g] = {"paired_difference_range": paired_range, "unpaired_envelope": unpaired}


def target_and_protection():
    g = "target_and_protection"
    # Recovered CC challenge: fixed target attainment hides severity of failure.
    reference = (("target", F(1, 10)), ("secure_below_target", F(9, 10)))
    candidate = (("target", F(3, 10)), ("ruin", F(7, 10)))
    reference_goal = probability(reference, lambda x: x == "target")
    candidate_goal = probability(candidate, lambda x: x == "target")
    reference_protection = probability(reference, lambda x: x != "ruin")
    candidate_protection = probability(candidate, lambda x: x != "ruin")
    paired = (candidate_goal - reference_goal,
              candidate_protection - reference_protection)
    check(g, "candidate_target_probability_gain", paired[0], F(1, 5))
    check(g, "candidate_protection_probability_loss", paired[1], F(-7, 10))
    check(g, "candidate_ruin_probability", 1 - candidate_protection, F(7, 10))
    check(g, "candidate_does_not_pareto_dominate", all(d >= 0 for d in paired), False)
    GROUPS[g] = {"source": "Recovered established Claude Code challenge, 16 November; recomputed here with exact finite distributions.",
                 "reference_goal_and_protection": (reference_goal, reference_protection),
                 "candidate_goal_and_protection": (candidate_goal, candidate_protection),
                 "paired_goal_and_protection_differences": paired,
                 "meaning": "A positive target-attainment difference does not establish that the policy is preferable. Preserve protective targets and failure severity separately."}


def model_boundary():
    g = "model_boundary"
    # A recorded route fails. Two observationally identical completions disagree
    # about an unexamined candidate; neither completion is evidence it exists.
    observed = {"known_route": False}
    completion_closed = {**observed, "unexamined_candidate": False}
    completion_open = {**observed, "unexamined_candidate": True}
    check(g, "recorded_model_has_no_success_route", any(observed.values()), False)
    check(g, "closed_completion_agrees_on_observed", {k: completion_closed[k] for k in observed}, observed)
    check(g, "open_completion_agrees_on_observed", {k: completion_open[k] for k in observed}, observed)
    check(g, "closed_completion_no_success", any(completion_closed.values()), False)
    check(g, "open_completion_has_success", any(completion_open.values()), True)
    GROUPS[g] = {"recorded_route_success": False,
                 "possible_completions_disagree": True,
                 "meaning": "The recorded failures do not identify what lies outside the model. No probability or hopeful real route follows from this logical underdetermination."}


def recursion_budget_not_termination():
    g = "recursion_budget_not_termination"
    budget = F(1)
    steps = 100
    costs = [F(1, 2 ** (k + 1)) for k in range(steps)]
    total = sum(costs, F(0))
    epsilon = F(1, 10)
    max_paid_steps = budget // epsilon
    check_true(g, "all_sampled_costs_strictly_positive", all(c > 0 for c in costs))
    check(g, "geometric_partial_sum", total, 1 - F(1, 2 ** steps))
    check_true(g, "finite_budget_not_exhausted_after_sampled_steps", total < budget)
    check(g, "uniform_lower_bound_caps_affordable_steps", max_paid_steps, 10)
    GROUPS[g] = {"sampled_steps": steps, "partial_cost": total,
                 "remaining_budget": budget - total,
                 "uniform_cost_lower_bound": epsilon, "affordable_step_bound": max_paid_steps,
                 "analytic_argument": "For every finite n, sum_{k=0}^{n-1} 2^{-(k+1)} = 1-2^{-n} < 1. Positive costs and finite budget alone do not imply a stopping time. A finite step cap or uniform positive cost lower bound supplies one.",
                 "scope": "This challenges an added implementation inference, not an attributed claim that the released text proves termination."}


def aggregation_loses_protection():
    g = "aggregation_loses_protection"
    # Burdens are deliberately toy quantities. A's declared individual floor is
    # burden_A <= 1; the sum alone cannot tell whether that floor is respected.
    balanced = (1, 1)
    concentrated = (2, 0)
    check(g, "same_aggregate_burden", sum(balanced), sum(concentrated))
    check(g, "balanced_respects_A_floor", balanced[0] <= 1, True)
    check(g, "concentrated_violates_A_floor", concentrated[0] <= 1, False)
    GROUPS[g] = {"balanced": balanced, "concentrated": concentrated,
                 "shared_aggregate": sum(balanced),
                 "meaning": "A compressed state or aggregate cannot support person-specific protective checks when it merges outcomes with different floor status."}


def worked_workshop_case():
    g = "worked_workshop_case"
    # Two groups seek separate workshop sessions. One facilitator, two possible
    # time slots. Both groups voluntarily accept different slots. Van and room
    # are independently available for the whole programme, common to both
    # sessions. Their joint state is observed before remote fallback cutoffs.
    # Each group's remote fallback succeeds independently with probability 1/2.
    dist = independent(bernoulli(F(9, 10)), bernoulli(F(4, 5)),
                       bernoulli(F(1, 2)), bernoulli(F(1, 2)))

    def direct(v):
        van, room, _, _ = v
        return van and room

    baseline_joint = probability(dist, lambda v: v[2] and v[3])
    rescheduled_direct_joint = probability(dist, direct)
    supported_with_fallback_joint = probability(dist, lambda v: direct(v) or (v[2] and v[3]))
    a_with_fallback = probability(dist, lambda v: direct(v) or v[2])
    b_with_fallback = probability(dist, lambda v: direct(v) or v[3])
    # Same-slot promises have only one facilitator. Cancellation of both remote
    # backups cannot turn the physically impossible joint session into success.
    simultaneous_joint = probability(dist, lambda v: direct(v) and 2 <= 1)
    rescheduled_joint_capacity_ok = 1 <= 1 and 1 <= 1
    check(g, "baseline_joint_remote", baseline_joint, F(1, 4))
    check(g, "simultaneous_promise_joint_failure", simultaneous_joint, F(0))
    check(g, "accepted_rescheduling_respects_capacity", rescheduled_joint_capacity_ok, True)
    check(g, "direct_joint_success_shared_dependencies", rescheduled_direct_joint, F(18, 25))
    check(g, "direct_joint_not_independent_sessions", rescheduled_direct_joint != rescheduled_direct_joint ** 2, True)
    check(g, "supported_joint_with_fallback", supported_with_fallback_joint, F(79, 100))
    check(g, "each_group_success_with_fallback_A", a_with_fallback, F(43, 50))
    check(g, "each_group_success_with_fallback_B", b_with_fallback, F(43, 50))
    check(g, "joint_plan_gain_over_named_baseline", supported_with_fallback_joint - baseline_joint, F(27, 50))
    check(g, "preserving_fallback_gain_over_direct_only", supported_with_fallback_joint - rescheduled_direct_joint, F(7, 100))
    check_true(g, "marginal_product_not_joint", a_with_fallback * b_with_fallback != supported_with_fallback_joint)
    GROUPS[g] = {"target": "Both groups receive their agreed session within the same declared programme window.",
                 "baseline_remote_joint": baseline_joint,
                 "same_slot_promises_and_cancelled_fallback_joint": simultaneous_joint,
                 "accepted_rescheduling_direct_joint": rescheduled_direct_joint,
                 "rescheduling_and_preserved_observable_fallback_joint": supported_with_fallback_joint,
                 "individual_success_each": a_with_fallback,
                 "paired_joint_gain": supported_with_fallback_joint - baseline_joint,
                 "important_assumptions": ["Voluntary accepted rescheduling; no consent is inferred from a numerical gain.",
                                           "Van and room are independent of each other but shared across sessions.",
                                           "Support status is observable before the fallback decision deadline.",
                                           "Fallbacks remain feasible and have no resource conflict with each other.",
                                           "All values are invented exact finite examples, not field estimates."]}


def serialise(value):
    if isinstance(value, F):
        return {"exact": f"{value.numerator}/{value.denominator}", "decimal": float(value)}
    if isinstance(value, dict):
        return {str(k): serialise(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [serialise(v) for v in value]
    if isinstance(value, set):
        return [serialise(v) for v in sorted(value)]
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="RESULTS.json")
    args = parser.parse_args()
    for fn in (bellman_trap, filtering_and_capability_cost, regard_not_weight,
               reliance_and_assurance, commitment_does_not_create_capacity,
               causal_announcement_confounding, complementary_support, shared_budget,
               correlated_support, attainment_vs_sustaining, per_step_risk,
               nonanticipative_policy, paired_model_difference, target_and_protection, model_boundary,
               recursion_budget_not_termination, aggregation_loses_protection,
               worked_workshop_case):
        fn()
    result = {"status": "PASS", "groups": len(GROUPS), "checks": len(CHECKS),
              "scope": "Exact invented finite examples; no empirical or normative validation.",
              "results": GROUPS, "check_log": CHECKS}
    Path(args.output).write_text(json.dumps(serialise(result), indent=2) + "\n", encoding="utf-8")
    print(f"PASS: {len(CHECKS)} exact checks across {len(GROUPS)} countermodel groups")
    print(f"Results: {Path(args.output).resolve()}")


if __name__ == "__main__":
    main()
