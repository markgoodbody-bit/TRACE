"""Independent finite dependency checks for TRACE's initial 0.6 packet.

These models change explicit assumptions; they do not refute the original
worked example, implement TRACE, or validate a final simulator not yet pinned.
All cases are synthetic. Only the requested JSON output is written.
"""

import argparse
from fractions import Fraction as F
import itertools
import json
from pathlib import Path


def joint(p, q, both):
    """Two Bernoulli marginals with their explicitly supplied joint success."""
    cells = {(True, True): both, (True, False): p - both,
             (False, True): q - both, (False, False): 1 - p - q + both}
    if any(w < 0 for w in cells.values()) or sum(cells.values()) != 1:
        raise ValueError("Inconsistent probability law")
    return cells


def worlds(direct, fallback_both):
    """Direct delivery and the fallback pair are independent in this model."""
    return joint(direct, fallback_both, direct * fallback_both)


def best_exclusive_policy(law, reveal_before_choice, fallback_capacity=2):
    """Enumerate policies constant on each observable information cell.

    Choice of direct versus remote is exclusive at a common cutoff. Remote
    needs two simultaneous units. This differs from the initial packet's
    explicit no-conflict fallback assumption.
    """
    observations = (False, True) if reveal_before_choice else (None,)
    scores = []
    for choices in itertools.product(("direct", "fallback"), repeat=len(observations)):
        policy = dict(zip(observations, choices))
        value = F(0)
        for (d, fallback), weight in law.items():
            action = policy[d if reveal_before_choice else None]
            achieved = d if action == "direct" else fallback and fallback_capacity >= 2
            value += weight * achieved
        scores.append(value)
    # Randomisation cannot improve the maximum of this linear expected score.
    return max(scores)


def run():
    results = []

    def check(name, observed, expected, meaning):
        if observed != expected:
            raise AssertionError(f"{name}: {observed!r} != {expected!r}")
        results.append({"name": name, "observed": str(observed),
                        "expected": str(expected), "meaning": meaning})

    base = worlds(F(18, 25), F(1, 4))
    check("early_information_feasible_exclusive_policy",
          best_exclusive_policy(base, True), F(79, 100),
          "An early observation supports an executable direct-else-fallback policy.")
    check("late_information_best_precommitted_policy",
          best_exclusive_policy(base, False), F(18, 25),
          "With exclusive pre-cutoff choice, the pathwise union is not an available policy.")
    check("shared_fallback_resource",
          best_exclusive_policy(base, True, fallback_capacity=1), F(18, 25),
          "Two simultaneous fallback demands cannot both use a single available unit.")
    check("capacity_restores_constructive_route",
          best_exclusive_policy(base, True, fallback_capacity=2), F(79, 100),
          "Restoring the second resource restores the conditional cooperative route.")

    # A strict-before cutoff is an explicit contract here, not a universal rule.
    for reveal_time, expected in ((9, F(79, 100)), (10, F(18, 25)), (11, F(18, 25))):
        check(f"strict_before_cutoff_reveal_at_{reveal_time}",
              best_exclusive_policy(base, reveal_time < 10), expected,
              "At the cutoff is not before it under this declared event ordering.")
    check("inclusive_cutoff_alternative_contract",
          best_exclusive_policy(base, 10 <= 10), F(79, 100),
          "An inclusive choice contract has a different equality boundary; neither is implicit.")

    for x, expected in ((F(7, 10), F(31, 40)), (F(18, 25), F(79, 100)),
                        (F(4, 5), F(17, 20))):
        direct_law = joint(F(9, 10), F(4, 5), x)
        direct = sum(w for (van, room), w in direct_law.items() if van and room)
        check(f"van_room_joint_{x}", best_exclusive_policy(worlds(direct, F(1, 4)), True),
              expected, "Same component marginals allow different dependence and joint outcomes.")

    for x, expected in ((F(0), F(18, 25)), (F(1, 4), F(79, 100)), (F(1, 2), F(43, 50))):
        fallback_law = joint(F(1, 2), F(1, 2), x)
        fallback = sum(w for (a, b), w in fallback_law.items() if a and b)
        check(f"fallback_joint_{x}", best_exclusive_policy(worlds(F(18, 25), fallback), True),
              expected, "Independent versus shared or opposed fallbacks change the joint guarantee.")

    for overlap, expected in ((F(0), F(97, 100)), (F(9, 50), F(79, 100)),
                              (F(1, 4), F(18, 25))):
        law = joint(F(18, 25), F(1, 4), overlap)
        check(f"direct_fallback_overlap_{overlap}", best_exclusive_policy(law, True),
              expected, "Even direct and fallback marginals do not fix their union without a joint law.")

    for reveal, expected in ((F(0), F(1, 2)), (F(1, 2), F(3, 4)), (F(1), F(1))):
        # Two equally plausible target worlds; with no reveal, one common
        # randomised left/right policy has max-min value one half.
        values = []
        for q in (F(i, 20) for i in range(21)):
            values.append(min(reveal + (1 - reveal) * q,
                              reveal + (1 - reveal) * (1 - q)))
        check(f"partial_reveal_{reveal}", max(values), expected,
              "A common policy uses actual observations, not the hidden target-world identity.")

    def timely_delivery(ack_at, delivered_at, due):
        # Acknowledgement is deliberately unused: the target is delivery by due.
        return delivered_at is not None and delivered_at <= due

    for delivered, expected in ((9, True), (10, True), (11, False), (None, False)):
        check(f"delivery_by_due_{delivered}", timely_delivery(1, delivered, 10), expected,
              "An early acknowledgement cannot substitute for timely delivery.")
    def promised_route(delivery_at, backup_at, cancel_at, due):
        backup_available = cancel_at is None or cancel_at > backup_at
        return (timely_delivery(1, delivery_at, due)
                or backup_available and timely_delivery(1, backup_at, due))

    check("early_promise_no_replacement_and_cancelled_backup",
          promised_route(delivery_at=11, backup_at=8, cancel_at=2, due=10), False,
          "A late delivery and a previously cancelled fallback give no timely result.")
    check("retained_timely_backup_positive_control",
          promised_route(delivery_at=11, backup_at=8, cancel_at=None, due=10), True,
          "A retained backup can deliver before the same deadline.")

    rejected = 0
    for p, q, overlap in ((F(-1, 10), F(1, 2), F(0)),
                          (F(11, 10), F(1, 2), F(1, 2)),
                          (F(9, 10), F(4, 5), F(1, 2)),
                          (F(1, 2), F(1, 2), F(3, 4))):
        try:
            joint(p, q, overlap)
        except ValueError:
            rejected += 1
    check("inconsistent_probability_inputs_rejected", rejected, 4,
          "A future parameterised interface needs validation; this is not a failed initial fixture.")

    # Positive maintenance construction: support before each consumption is a
    # physical resource addition. A promise without delivery leaves it unchanged.
    def survives(initial, delivered_support):
        remaining = initial
        for support in delivered_support:
            remaining += support
            if remaining < 1:
                return False
            remaining -= 1
        return True

    check("maintenance_without_delivery", survives(1, (0, 0)), False,
          "The second required service cannot consume a missing resource.")
    check("maintenance_with_delivered_support", survives(1, (1, 1)), True,
          "Delivered recurring support makes an otherwise impossible maintenance plan feasible.")

    return {"status": "PASS", "checks": len(results),
            "scope": "Independent synthetic dependency checks on the initial packet's assumptions; not a final simulator test.",
            "initial_source": "09c07a4b20134c6fccec2b6eb26fa4daf612bc5e",
            "findings": results}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "checks": result["checks"], "output": str(args.output)}))
