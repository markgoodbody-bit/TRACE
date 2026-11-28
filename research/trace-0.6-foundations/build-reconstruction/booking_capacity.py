"""Check if all held offers can use distinct, already-timed confirmation slots."""

import argparse
import json
import sys
from collections import deque


def _ids(values, label):
    if not isinstance(values, list) or any(
        not isinstance(value, str) or not value.strip() for value in values
    ):
        raise ValueError(f"{label} must be an array of nonempty IDs")
    if len(set(values)) != len(values):
        raise ValueError(f"{label} must contain distinct IDs")
    return values


def _routes(slots, offers):
    inventory = set(_ids(slots, "slots"))
    if not isinstance(offers, list):
        raise ValueError("offers must be an array")
    confirmed = {}
    possible = {}
    for offer in offers:
        if not isinstance(offer, dict) or offer.keys() not in (
            {"person", "confirmed"}, {"person", "confirmed", "unconfirmed"}
        ):
            raise ValueError("each offer needs person and confirmed, with optional unconfirmed")
        person = offer["person"]
        if not isinstance(person, str) or not person.strip() or person in confirmed:
            raise ValueError("each offer needs a distinct nonempty person ID")
        known = _ids(offer["confirmed"], "confirmed routes")
        pending = _ids(offer.get("unconfirmed", []), "unconfirmed routes")
        if set(known).intersection(pending):
            raise ValueError("a route cannot be both confirmed and unconfirmed")
        candidates = known + pending
        if not inventory.issuperset(candidates):
            raise ValueError("each route must name a declared slot")
        confirmed[person] = known
        possible[person] = candidates
    return confirmed, possible


def _find_free_slot(start, routes, holders):
    """Find a free slot by following routes and the people currently holding them."""
    pending = deque([start])
    seen = {start}
    previous = {}
    while pending:
        person = pending.popleft()
        for slot in routes[person]:
            if slot in previous:
                continue
            previous[slot] = person
            holder = holders.get(slot)
            if holder is None:
                return slot, previous
            if holder not in seen:
                seen.add(holder)
                pending.append(holder)
    return None, previous


def _allocate(routes):
    assigned = {}
    holders = {}
    for person in routes:
        free, previous = _find_free_slot(person, routes, holders)
        if free is None:
            # Every reachable slot is occupied by a reached person. The
            # starting person is the extra one, so this group cannot all fit.
            group = {holders[slot] for slot in previous}
            group.add(person)
            return {"shortfall": {
                "people": [candidate for candidate in routes if candidate in group],
                "slots": list(previous),
            }}
        while free is not None:
            recipient = previous[free]
            old_slot = assigned.get(recipient)
            assigned[recipient] = free
            holders[free] = recipient
            free = old_slot
    return {"allocation": assigned}


def check_capacity(slots, offers):
    """Return a supported allocation, a conditional one, or a certified shortfall."""
    confirmed, possible = _routes(slots, offers)
    known_result = _allocate(confirmed)
    if "allocation" in known_result:
        return {"status": "confirmed", **known_result}

    possible_result = _allocate(possible) if possible != confirmed else known_result
    if "shortfall" in possible_result:
        return {"status": "insufficient", **possible_result}

    allocation = possible_result["allocation"]
    return {
        "status": "unconfirmed",
        "confirmed_shortfall": known_result["shortfall"],
        "possible_allocation": allocation,
        "routes_to_confirm": [
            {"person": person, "slot": slot}
            for person, slot in allocation.items() if slot not in confirmed[person]
        ],
    }


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON field: {key}")
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    try:
        request = json.load(sys.stdin, object_pairs_hook=_unique_object)
        if not isinstance(request, dict) or request.keys() != {"slots", "offers"}:
            raise ValueError("the request needs slots and offers")
        result = check_capacity(request["slots"], request["offers"])
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))


if __name__ == "__main__":
    main()
