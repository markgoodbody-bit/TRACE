"""Compute possible choices from observed usable menus under a fixed strict order."""
import argparse
import json
import sys
from graphlib import CycleError, TopologicalSorter
from itertools import permutations


BRAKES = "brake practice"
PUNCTURES = "puncture practice"
OPTIONS = (BRAKES, PUNCTURES)


def _read_menu(options):
    if not isinstance(options, (list, tuple)):
        raise ValueError("a usable menu must be an array of option IDs")
    if any(not isinstance(option, str) or not option.strip() for option in options):
        raise ValueError("option IDs must be nonempty strings")
    return tuple(dict.fromkeys(options))


def possible_choices(history, usable_next):
    """Return all possible next winners or a cycle refuting the fixed-order model.

    Each observation has a complete usable menu and one chosen member. All
    observations concern one chooser over a period with a fixed strict ranking.
    """
    if not isinstance(history, (list, tuple)):
        raise ValueError("history must be an array of observations")
    next_menu = _read_menu(usable_next)
    predecessors = {option: set() for option in next_menu}
    for observation in history:
        if not isinstance(observation, dict) or observation.keys() != {"usable", "chosen"}:
            raise ValueError("each observation must have usable and chosen fields")
        menu = _read_menu(observation["usable"])
        chosen = observation["chosen"]
        if not isinstance(chosen, str) or chosen not in menu:
            raise ValueError("the chosen option must belong to that observation's usable menu")
        predecessors.setdefault(chosen, set())
        for option in menu:
            if option != chosen:
                predecessors.setdefault(option, set()).add(chosen)

    offered = set(next_menu)
    has_offered_ancestor = set()
    try:
        for option in TopologicalSorter(predecessors).static_order():
            # A path may pass through options missing from the next menu.
            if any(parent in offered or parent in has_offered_ancestor
                   for parent in predecessors[option]):
                has_offered_ancestor.add(option)
    except CycleError as error:
        return {"status": "inconsistent", "cycle": error.args[1]}
    winners = [option for option in next_menu if option not in has_offered_ancestor]
    return {"status": "compatible", "possible_next_choices": winners}


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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stdin", action="store_true",
                        help="read a JSON request with history and usable_next")
    if parser.parse_args().stdin:
        try:
            request = json.load(sys.stdin)
            if not isinstance(request, dict) or request.keys() != {"history", "usable_next"}:
                raise ValueError("the request must have history and usable_next fields")
            result = possible_choices(request["history"], request["usable_next"])
        except ValueError as error:
            parser.error(str(error))
        print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
        return

    print(json.dumps({
        "basis": "stipulated strict rankings held fixed within each comparison",
        "both_usable_at_choice": compare(OPTIONS, PUNCTURES, OPTIONS),
        "route_withdrawn_and_then_restored": compare((PUNCTURES,), PUNCTURES, OPTIONS),
        "brake_session_listed_without_support": compare((PUNCTURES,), PUNCTURES, (PUNCTURES,)),
    }, indent=2))


if __name__ == "__main__":
    main()
