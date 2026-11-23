#!/usr/bin/env python3
"""Two possible futures consistent with the same workshop observations.

Two equally likely learner windows are 20 and 40 minutes. A demonstration
fits either. A practice session with a qualified check fits only 40 minutes.
The home result concerns a later, separately specified goal. The following
home outcomes are invented, not forecasts or a claim about brake safety.
"""

from fractions import Fraction

WINDOWS = (20, 40)
WORKSHOP = {
    "demonstration": ((True, False), (True, False)),
    "practice": ((False, False), (True, True)),
}

# Each row corresponds to the same 20- and 40-minute worlds. A home success
# requires attendance in this example. Outcomes under alternative offers are
# stipulated counterfactuals, not jointly observed participant outcomes.
HOME = {
    "demonstration_favours_home": {
        "demonstration": (True, True),
        "practice": (False, False),
    },
    "practice_favours_home": {
        "demonstration": (False, False),
        "practice": (False, True),
    },
}


def probability(outcomes):
    return Fraction(sum(outcomes), len(outcomes))


def main():
    for offer, observations in WORKSHOP.items():
        attendance = probability([row[0] for row in observations])
        checked_attempt = probability([row[1] for row in observations])
        print(f"{offer}: attendance={attendance}, checked_attempt={checked_attempt}")

    expected = {
        "demonstration_favours_home": Fraction(-1),
        "practice_favours_home": Fraction(1, 2),
    }
    for name, outcomes in HOME.items():
        for offer in WORKSHOP:
            assert all(not success or attended[0]
                       for success, attended in zip(outcomes[offer], WORKSHOP[offer]))
        difference = probability(outcomes["practice"]) - probability(outcomes["demonstration"])
        assert difference == expected[name]
        print(f"{name}: practice minus demonstration at home={difference}")


if __name__ == "__main__":
    main()
