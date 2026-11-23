#!/usr/bin/env python3
"""Finite, declared-law support/observation laboratory, not an ethical solver."""
import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path


ROUTES = ("direct", "fallback")


def law(rows):
    result = []
    seen = set()
    for row in rows:
        if set(row) != {"direct", "f1", "f2", "prob"}:
            raise ValueError("each world needs direct, f1, f2 and prob")
        key = (row["direct"], row["f1"], row["f2"])
        if any(type(x) is not bool for x in key) or key in seen:
            raise ValueError("worlds must be distinct boolean triples")
        seen.add(key)
        p = Fraction(str(row["prob"]))
        if p < 0 or p > 1:
            raise ValueError("probability out of range")
        result.append((key, p))
    if sum((p for _, p in result), Fraction(0)) != 1:
        raise ValueError("joint law must sum to one")
    return result


def fallback_fits(capacity, fallback_units):
    if type(capacity) is not int or type(fallback_units) is not int or capacity < 0 or fallback_units < 1:
        raise ValueError("capacity and demand must be integer and nonnegative")
    return capacity >= fallback_units


def route_succeeds(world, route, enough_fallback_capacity):
    direct, first, second = world
    return direct if route == "direct" else first and second and enough_fallback_capacity


def support(rows, timing, capacity, fallback_units=2):
    """direct or fallback, never both; observation of direct may be early or late."""
    worlds = law(rows)
    if timing not in ("early", "late"):
        raise ValueError("observation timing must be early or late")
    enough_fallback_capacity = fallback_fits(capacity, fallback_units)
    policies = list(itertools.product(ROUTES, repeat=2 if timing == "early" else 1))
    scored = []
    for policy in policies:
        chance = sum((p for key, p in worlds
                      if route_succeeds(key, policy[int(key[0])] if timing == "early" else policy[0],
                                        enough_fallback_capacity)), Fraction())
        scored.append((chance, policy))
    best = max(x[0] for x in scored)
    return {"success": str(best), "policies": [list(p) for v, p in scored if v == best],
            "basis": "stipulated joint law; support is not consent, authority or delivery proof"}


def before_hardening(effect_time, hardening_time):
    return effect_time < hardening_time


def inquiry(rows, *, positive_likelihoods, observation_time, booking_minutes, booking_lock,
            allowed_routes=ROUTES, capacity=2, fallback_units=2):
    """Compare one check with booking on the evidence already available.

    The likelihoods give the chance of a positive answer when direct fails
    and when direct succeeds, respectively, conditional on the existing evidence.
    """
    worlds = law(rows)
    likelihoods = tuple(Fraction(str(p)) for p in positive_likelihoods)
    if len(likelihoods) != 2 or any(not 0 <= p <= 1 for p in likelihoods):
        raise ValueError("supply two conditional probabilities between zero and one")
    if any(type(t) is not int for t in (observation_time, booking_minutes, booking_lock)) or booking_minutes < 0:
        raise ValueError("use integer clock times and a nonnegative time to book")
    enough_fallback_capacity = fallback_fits(capacity, fallback_units)
    permitted = set(allowed_routes)
    if permitted.difference(ROUTES):
        raise ValueError("allowed routes must come from the declared route set")
    routes = [r for r in ROUTES if r in permitted and (r == "direct" or enough_fallback_capacity)]
    if not routes:
        raise ValueError("the comparison needs a permitted and feasible booking route")

    def best_route(weighted_worlds):
        chance_by_route = {
            route: sum((mass for world, mass in weighted_worlds
                        if route_succeeds(world, route, enough_fallback_capacity)), Fraction())
            for route in routes
        }
        best = max(chance_by_route.values())
        return best, [route for route, chance in chance_by_route.items() if chance == best]

    baseline, baseline_routes = best_route(worlds)
    booking_time = observation_time + booking_minutes
    in_time = before_hardening(booking_time, booking_lock)
    answers = {}
    best_with_answer = Fraction()
    for answer in (False, True):
        weighted = []
        for world, mass in worlds:
            positive = likelihoods[int(world[0])]
            weighted.append((world, mass * (positive if answer else 1 - positive)))
        answer_probability = sum((mass for _, mass in weighted), Fraction())
        if answer_probability == 0:
            continue
        best, best_routes = best_route(weighted)
        best_with_answer += best
        direct_mass = sum((mass for world, mass in weighted if world[0]), Fraction())
        answers["positive" if answer else "negative"] = {
            "probability": str(answer_probability),
            "probability_direct_works": str(direct_mass / answer_probability),
            "best_routes_if_in_time": best_routes,
        }

    at_lock = best_with_answer if in_time else baseline
    return {
        "baseline_success": str(baseline),
        "baseline_routes": baseline_routes,
        "answers": answers,
        "booking_effect_time": booking_time,
        "usable_before_lock": in_time,
        "success_by_acting_on_available_evidence": str(at_lock),
        "gain_in_success_probability": str(at_lock - baseline),
    }


def workshop_inquiry(rows):
    """Run the stipulated checks on the workshop's two alternative kit routes."""
    checks = (
        ("copy_of_the_listing", (1, 1), 1, ROUTES),
        ("fresh_partial_check", ("1/3", "2/3"), 4, ROUTES),
        ("fresh_full_check_before_lock", (0, 1), 7, ROUTES),
        ("fresh_full_check_at_lock", (0, 1), 8, ROUTES),
        ("full_check_with_only_direct_authority", (0, 1), 7, ("direct",)),
    )
    return {
        name: inquiry(rows, positive_likelihoods=likelihoods, observation_time=time,
                      booking_minutes=2, booking_lock=10, allowed_routes=routes)
        for name, likelihoods, time, routes in checks
    }


def delivered_by_due(delivery_time, due_time):
    return delivery_time <= due_time


def unknown_conditions(agreement, delivery):
    if agreement not in ("yes", "no", "unknown") or delivery not in ("yes", "no", "unknown"):
        raise ValueError("unsupported tri-state input")
    return {"agreement": agreement, "delivery": delivery,
            "authorization": "UNASSESSED", "claim": "neither promise nor agreement proves delivery"}


def delivery_route(*, acknowledgement_time, delivery_time, backup_available, backup_cancelled_before_delivery,
                   backup_time, due_time, hardening_time):
    """Stipulated events: cancellation flag applies strictly before backup delivery."""
    for value in (acknowledgement_time, delivery_time, backup_time, due_time, hardening_time):
        if value is not None and type(value) is not int:
            raise ValueError("times must be integers or null")
    if type(backup_available) is not bool or type(backup_cancelled_before_delivery) is not bool:
        raise ValueError("backup states must be explicit booleans")
    if due_time is None or hardening_time is None:
        return {"status": "UNKNOWN", "reason": "due or hardening time unavailable"}
    available_times = [delivery_time]
    if backup_available and not backup_cancelled_before_delivery:
        available_times.append(backup_time)
    known_success = any(t is not None and delivered_by_due(t, due_time) and
                        before_hardening(t, hardening_time) for t in available_times)
    if known_success:
        status = "SUPPORTED_IN_MODEL"
    elif any(t is None for t in available_times):
        status = "UNKNOWN"
    else:
        status = "NOT_SUPPORTED_IN_MODEL"
    return {"status": status, "acknowledgement": acknowledgement_time,
            "basis": "single stipulated comparable clock; cancellation flag is before backup delivery; not authorisation or observed delivery"}


def simulate_scenario(scenario):
    expected = {"worlds", "observation_time", "action_deadline", "capacity", "fallback_units"}
    if not isinstance(scenario, dict) or set(scenario) != expected:
        raise ValueError("scenario needs exact declared fields")
    observation_time = scenario["observation_time"]
    action_deadline = scenario["action_deadline"]
    if type(observation_time) is not int or type(action_deadline) is not int:
        raise ValueError("observation and action deadline must be integer clocks")
    # Convention: observation at the deadline is available before the action.
    timing = "early" if observation_time <= action_deadline else "late"
    return {"observation_timing": timing,
            "boundary": "observation at deadline available before choice",
            "result": support(scenario["worlds"], timing, scenario["capacity"],
                              scenario["fallback_units"])}


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--input", help="local JSON scenario with explicit joint law")
    mode.add_argument("--inquiry", action="store_true", help="compare the workshop checks")
    args = parser.parse_args()
    if args.inquiry:
        scenario = json.loads(Path(__file__).with_name("scenario.example.json").read_text(encoding="utf-8"))
        print(json.dumps(workshop_inquiry(scenario["worlds"]), indent=2))
        return
    if args.input:
        with open(args.input, encoding="utf-8") as stream:
            scenario = json.load(stream)
        print(json.dumps(simulate_scenario(scenario), indent=2))
        return
    rows = [{"direct": d, "f1": a, "f2": b,
             "prob": str((Fraction(18,25) if d else Fraction(7,25)) * Fraction(1,4))}
            for d, a, b in itertools.product((False, True), repeat=3)]
    print(json.dumps({"early": support(rows, "early", 2), "late": support(rows, "late", 2),
                      "insufficient_capacity": support(rows, "early", 1),
                      "commitment": unknown_conditions("yes", "unknown")}, indent=2))


if __name__ == "__main__":
    main()
