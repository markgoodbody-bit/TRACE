#!/usr/bin/env python3
"""A finite, stipulated example of time to ask and time to act.

The learner has either 25 or 45 minutes, each with probability 1/2.
The learner consents to a question about available time and accepts the
offer that matches it. Demonstration takes 20 minutes. Practice takes 40,
including an agreed qualified check. No other session costs or outcomes
are modelled. The clock begins before the question and ends at departure.
"""

from fractions import Fraction


def outcome(available, inquiry_minutes, policy):
    """Return attendance and completed practice-with-check for one world."""
    remaining = available - inquiry_minutes
    if policy == "demonstration":
        duration = 20
    elif policy == "practice":
        duration = 40
    elif policy == "ask_then_offer":
        duration = 40 if remaining >= 40 else 20
    else:
        raise ValueError("Unknown policy")
    attendance = remaining >= duration
    return int(attendance), int(attendance and duration == 40)


def evaluate(inquiry_minutes, policy):
    worlds = (25, 45)
    results = [outcome(t, inquiry_minutes, policy) for t in worlds]
    return tuple(sum((Fraction(row[i], len(worlds)) for row in results), Fraction())
                 for i in range(2))


def main():
    cases = ((0, "demonstration"), (0, "practice"),
             (5, "ask_then_offer"), (10, "ask_then_offer"))
    expected = ((1, 0), (Fraction(1, 2), Fraction(1, 2)),
                (1, Fraction(1, 2)), (Fraction(1, 2), 0))
    for case, result in zip(cases, expected):
        observed = evaluate(*case)
        assert observed == result, (case, observed, result)
        print(f"inquiry={case[0]:2} policy={case[1]:15} attendance={observed[0]} "
              f"practice_with_check={observed[1]}")


if __name__ == "__main__":
    main()
