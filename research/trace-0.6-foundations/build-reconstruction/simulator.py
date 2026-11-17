#!/usr/bin/env python3
"""Finite, declared-law support/observation laboratory, not an ethical solver."""
import argparse
import itertools
import json
from fractions import Fraction


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


def support(rows, timing, capacity, fallback_units=2):
    """direct or fallback, never both; observation of direct may be early or late."""
    worlds = law(rows)
    if timing not in ("early", "late"):
        raise ValueError("observation timing must be early or late")
    if type(capacity) is not int or type(fallback_units) is not int or capacity < 0 or fallback_units < 1:
        raise ValueError("capacity and demand must be integer and nonnegative")
    def succeeds(key, action):
        d, f1, f2 = key
        return d if action == "direct" else bool(f1 and f2 and capacity >= fallback_units)
    policies = list(itertools.product(("direct", "fallback"), repeat=2 if timing == "early" else 1))
    scored = []
    for policy in policies:
        chance = sum((p for key, p in worlds
                      if succeeds(key, policy[int(key[0])] if timing == "early" else policy[0])), Fraction())
        scored.append((chance, policy))
    best = max(x[0] for x in scored)
    return {"success": str(best), "policies": [list(p) for v, p in scored if v == best],
            "basis": "stipulated joint law; support is not consent, authority or delivery proof"}


def before_hardening(effect_time, hardening_time):
    return effect_time < hardening_time


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
    parser.add_argument("--input", help="local JSON scenario with explicit joint law")
    args = parser.parse_args()
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
