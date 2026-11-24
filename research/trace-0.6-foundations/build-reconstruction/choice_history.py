"""Compute possible choices from observed usable menus under a fixed strict order."""
import argparse
import json
import sys
from collections import deque
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


def _observed_steps(path, predecessors):
    return [{"history_index": predecessors[other][winner], "chosen": winner, "over": other}
            for winner, other in zip(path, path[1:])]


def _choice_witness(target, offered, predecessors, order):
    # Search backwards for the nearest rival in the next menu.
    pending = deque([target])
    towards_target = {target: None}
    while pending:
        option = pending.popleft()
        if option != target and option in offered:
            path = [option]
            while path[-1] != target:
                path.append(towards_target[path[-1]])
            return {"kind": "excluded", "option": target,
                    "steps": _observed_steps(path, predecessors)}
        for winner in predecessors[option]:
            if winner not in towards_target:
                towards_target[winner] = option
                pending.append(winner)

    # Every strict ancestor was visited. They can all precede the target
    # without placing any other offered option first.
    ancestors = [node for node in order if node != target and node in towards_target]
    remaining = [node for node in order if node not in towards_target]
    return {"kind": "possible", "option": target,
            "example_ranking": [*ancestors, target, *remaining]}


def possible_choices(history, usable_next, *, explain=None):
    """Return all possible next winners or a cycle refuting the fixed-order model.

    Each observation has a complete usable menu and one chosen member. All
    observations concern one chooser over a period with a fixed strict ranking.
    Request a witness by naming a member of the next menu with explain.
    """
    if not isinstance(history, (list, tuple)):
        raise ValueError("history must be an array of observations")
    next_menu = _read_menu(usable_next)
    offered = set(next_menu)
    if explain is not None and (not isinstance(explain, str) or explain not in offered):
        raise ValueError("explain must name an option in usable_next")
    predecessors = {option: {} for option in next_menu}
    for index, observation in enumerate(history):
        if not isinstance(observation, dict) or observation.keys() != {"usable", "chosen"}:
            raise ValueError("each observation must have usable and chosen fields")
        menu = _read_menu(observation["usable"])
        chosen = observation["chosen"]
        if not isinstance(chosen, str) or chosen not in menu:
            raise ValueError("the chosen option must belong to that observation's usable menu")
        predecessors.setdefault(chosen, {})
        for option in menu:
            if option != chosen:
                # Keep one source row for a comparison even when it recurs.
                predecessors.setdefault(option, {}).setdefault(chosen, index)

    try:
        order = list(TopologicalSorter(predecessors).static_order())
    except CycleError as error:
        cycle = error.args[1]
        result = {"status": "inconsistent", "cycle": cycle}
        if explain is not None:
            result["witness"] = {"kind": "inconsistent_history",
                                 "steps": _observed_steps(cycle, predecessors)}
        return result

    has_offered_ancestor = set()
    for option in order:
        # A path may pass through options missing from the next menu.
        if any(parent in offered or parent in has_offered_ancestor
               for parent in predecessors[option]):
            has_offered_ancestor.add(option)
    winners = [option for option in next_menu if option not in has_offered_ancestor]
    result = {"status": "compatible", "possible_next_choices": winners}
    if explain is not None:
        result["witness"] = _choice_witness(explain, offered, predecessors, order)
    return result


def compare_availability(history, usable_next, disputed, *, explain=None):
    """Compare two answers about one recorded rival in a past choice."""
    if not isinstance(disputed, dict) or disputed.keys() != {"history_index", "option"}:
        raise ValueError("check_availability needs history_index and option")

    if_usable = possible_choices(history, usable_next, explain=explain)
    index = disputed["history_index"]
    if type(index) is not int or not 0 <= index < len(history):
        raise ValueError("history_index must identify an observation in history")
    option = disputed["option"]
    row = history[index]
    if not isinstance(option, str) or option not in row["usable"] or option == row["chosen"]:
        raise ValueError("the disputed option must be an unchosen member of that usable menu")

    without_option = list(history)
    without_option[index] = {
        "usable": [member for member in row["usable"] if member != option],
        "chosen": row["chosen"],
    }
    return {
        "check_availability": {"history_index": index, "option": option},
        "if_usable": if_usable,
        "if_unusable": possible_choices(without_option, usable_next, explain=explain),
    }


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
                        help="read JSON history and next menu, with optional witness and availability check")
    if parser.parse_args().stdin:
        try:
            request = json.load(sys.stdin)
            required = {"history", "usable_next"}
            allowed = required | {"explain", "check_availability"}
            if not isinstance(request, dict) or not required <= request.keys() <= allowed:
                raise ValueError("the request needs history and usable_next, "
                                 "with optional explain and check_availability")
            history, usable_next = request["history"], request["usable_next"]
            explain = request.get("explain")
            if "check_availability" in request:
                result = compare_availability(history, usable_next, request["check_availability"],
                                              explain=explain)
            else:
                result = possible_choices(history, usable_next, explain=explain)
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
