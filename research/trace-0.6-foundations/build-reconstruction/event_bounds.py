"""Latest event bounds for one declared acyclic plan on a single comparable clock."""
from graphlib import CycleError, TopologicalSorter


def _triples(rows, name):
    if not isinstance(rows, list) or any(not isinstance(row, list) or len(row) != 3 for row in rows):
        raise ValueError(f"{name} must be an array of triples")
    return rows


def event_bounds(plan):
    required = {"clock", "events", "links", "deadlines"}
    if not isinstance(plan, dict) or not required <= plan.keys() <= required | {"check"}:
        raise ValueError("declare clock, events, links and deadlines, with an optional check")
    clock, events = plan["clock"], plan["events"]
    if not isinstance(clock, str) or not clock.strip():
        raise ValueError("declare the common clock and unit")
    if not isinstance(events, list) or any(not isinstance(e, str) or not e.strip() for e in events):
        raise ValueError("events must be an array of nonempty event IDs")
    outgoing = {event: [] for event in events}
    if len(outgoing) != len(events):
        raise ValueError("event IDs must be unique")

    def known(event):
        return isinstance(event, str) and event in outgoing

    order = TopologicalSorter({event: () for event in events})
    links = _triples(plan["links"], "links")
    for index, (source, target, lag) in enumerate(links):
        if not known(source) or not known(target) or type(lag) is not int or lag < 0:
            raise ValueError("each link needs two declared events and a nonnegative integer lag")
        outgoing[source].append((target, lag, index))
        order.add(target, source)
    try:
        sequence = list(order.static_order())
    except CycleError as error:
        raise ValueError("this calculation requires an acyclic plan") from error

    # At the same instant an open bound (False) sorts before a closed bound (True).
    bounds = dict.fromkeys(events)
    deadline_index = {}
    next_link = {}
    for index, (event, at, relation) in enumerate(_triples(plan["deadlines"], "deadlines")):
        if not known(event) or type(at) is not int or relation not in ("before", "by"):
            raise ValueError("each deadline needs a declared event, an integer time and before or by")
        limit = (at, relation == "by")
        if bounds[event] is None or limit < bounds[event]:
            bounds[event], deadline_index[event] = limit, index

    for event in reversed(sequence):
        for target, lag, index in outgoing[event]:
            if bounds[target] is None:
                continue
            at, inclusive = bounds[target]
            limit = (at - lag, inclusive)
            if bounds[event] is None or limit < bounds[event]:
                bounds[event] = limit
                next_link[event] = index
                deadline_index[event] = deadline_index[target]

    displayed = {
        event: None if limit is None else {"at": limit[0], "relation": "by" if limit[1] else "before"}
        for event, limit in bounds.items()
    }
    result = {"clock": clock, "bounds": displayed}
    if "check" in plan:
        check = plan["check"]
        if (not isinstance(check, dict) or check.keys() != {"event", "at"}
                or not known(check["event"]) or type(check["at"]) is not int):
            raise ValueError("check needs a declared event and an integer time on the common clock")
        event, at = check["event"], check["at"]
        limit = bounds[event]
        within = None
        if limit is not None:
            deadline, inclusive = limit
            within = at < deadline or (at == deadline and inclusive)
        steps = []
        target = event
        while target in next_link:
            index = next_link[target]
            steps.append(index)
            target = links[index][1]
        result["check"] = {"event": event, "at": at, "within_bound": within,
                           "link_indices": steps, "deadline_index": deadline_index.get(event)}
    return result
