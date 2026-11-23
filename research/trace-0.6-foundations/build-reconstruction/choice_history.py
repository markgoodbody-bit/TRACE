"""Two-option example of how a usable menu changes what a choice can show."""
import json
from itertools import permutations


BRAKES = "brake practice"
PUNCTURES = "puncture practice"
OPTIONS = (BRAKES, PUNCTURES)


def choose(ranking, usable):
    return next((option for option in ranking if option in usable), None)


def compare(usable_now, observed_choice, usable_next):
    """Examine both strict rankings, keeping each fixed across this comparison."""
    usable_now = frozenset(usable_now)
    usable_next = frozenset(usable_next)
    if (usable_now | usable_next) - set(OPTIONS):
        raise ValueError("explain availability using the two declared practice options")
    if observed_choice not in usable_now:
        raise ValueError("the observed choice needs to be usable in this fixture")

    rankings = [ranking for ranking in permutations(OPTIONS)
                if choose(ranking, usable_now) == observed_choice]
    next_choices = list(dict.fromkeys(choose(ranking, usable_next) for ranking in rankings))
    return {
        "usable_now": [option for option in OPTIONS if option in usable_now],
        "observed_choice": observed_choice,
        "compatible_rankings": [list(ranking) for ranking in rankings],
        "usable_next": [option for option in OPTIONS if option in usable_next],
        "possible_next_choices": next_choices,
    }


def main():
    print(json.dumps({
        "basis": "stipulated strict rankings held fixed within each comparison",
        "both_usable_at_choice": compare(OPTIONS, PUNCTURES, OPTIONS),
        "route_withdrawn_and_then_restored": compare((PUNCTURES,), PUNCTURES, OPTIONS),
        "brake_session_listed_without_support": compare((PUNCTURES,), PUNCTURES, (PUNCTURES,)),
    }, indent=2))


if __name__ == "__main__":
    main()
