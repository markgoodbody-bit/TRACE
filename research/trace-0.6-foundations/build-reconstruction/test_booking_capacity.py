import json
import subprocess
import sys
import unittest
from itertools import permutations, product
from pathlib import Path

from booking_capacity import check_capacity


class BookingCapacityTests(unittest.TestCase):
    def test_two_people_share_one_phone_slot(self):
        slots = ["phone-1", "written-1", "written-2"]
        offers = [
            {"person": "A", "confirmed": ["phone-1"]},
            {"person": "B", "confirmed": ["phone-1"]},
            {"person": "C", "confirmed": ["written-1", "written-2"]},
        ]
        self.assertEqual(check_capacity(slots, offers), {
            "status": "insufficient",
            "shortfall": {"people": ["A", "B"], "slots": ["phone-1"]},
        })

    def test_check_the_new_phone_route_before_promising(self):
        slots = ["phone-1", "phone-2", "written-2"]
        offers = [
            {"person": "A", "confirmed": ["phone-1"]},
            {"person": "B", "confirmed": ["phone-1"], "unconfirmed": ["phone-2"]},
            {"person": "C", "confirmed": ["written-2"]},
        ]
        allocation = {"A": "phone-1", "B": "phone-2", "C": "written-2"}
        self.assertEqual(check_capacity(slots, offers), {
            "status": "unconfirmed",
            "confirmed_shortfall": {"people": ["A", "B"], "slots": ["phone-1"]},
            "possible_allocation": allocation,
            "routes_to_confirm": [{"person": "B", "slot": "phone-2"}],
        })
        offers[1] = {"person": "B", "confirmed": ["phone-1", "phone-2"]}
        self.assertEqual(check_capacity(slots, offers), {
            "status": "confirmed", "allocation": allocation,
        })

    def test_two_existing_assignments_can_move(self):
        offers = [
            {"person": "A", "confirmed": ["s1", "s2"]},
            {"person": "B", "confirmed": ["s2", "s3"]},
            {"person": "C", "confirmed": ["s1"]},
        ]
        self.assertEqual(check_capacity(["s1", "s2", "s3"], offers), {
            "status": "confirmed", "allocation": {"A": "s2", "B": "s3", "C": "s1"},
        })

    def test_empty_offers_and_person_without_a_route(self):
        self.assertEqual(check_capacity(["unused"], []), {"status": "confirmed", "allocation": {}})
        self.assertEqual(check_capacity([], [{"person": "A", "confirmed": []}]), {
            "status": "insufficient", "shortfall": {"people": ["A"], "slots": []},
        })

    def test_rejects_ambiguous_or_undeclared_capacity(self):
        cases = [
            (["s", "s"], []),
            (["s"], [{"person": "A", "confirmed": ["s"]}, {"person": "A", "confirmed": []}]),
            (["s"], [{"person": "A", "confirmed": ["s"], "unconfirmed": ["s"]}]),
            (["s"], [{"person": "A", "confirmed": [], "unconfirmed": ["other"]}]),
            (["s"], [{"person": "A", "confirmed": "s"}]),
        ]
        for slots, offers in cases:
            with self.subTest(slots=slots, offers=offers), self.assertRaises(ValueError):
                check_capacity(slots, offers)

    def test_cli_rejects_repeated_fields_in_an_offer(self):
        request = '{"slots":["s"],"offers":[{"person":"A","confirmed":["s"],"confirmed":[]}]}'
        cli = Path(__file__).with_name("booking_capacity.py")
        result = subprocess.run([sys.executable, str(cli)], input=request, text=True,
                                capture_output=True, check=False)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("duplicate JSON field: confirmed", result.stderr)

    def test_against_enumeration_of_every_three_person_route_record(self):
        people = ("A", "B", "C")
        slots = ("s1", "s2", "s3")
        assignments = tuple(permutations(slots))

        def feasible(routes):
            return any(all(slot in routes[person] for person, slot in zip(people, fit))
                       for fit in assignments)

        only_alone = 0
        for edges in product(range(3), repeat=9):
            # 0 is absent, 1 is confirmed, 2 is unconfirmed.
            offers = [
                {"person": person, "confirmed": [slot for j, slot in enumerate(slots) if edges[i * 3 + j] == 1],
                 "unconfirmed": [slot for j, slot in enumerate(slots) if edges[i * 3 + j] == 2]}
                for i, person in enumerate(people)
            ]
            known = {row["person"]: set(row["confirmed"]) for row in offers}
            possible = {row["person"]: set(row["confirmed"] + row["unconfirmed"]) for row in offers}

            known_fit = feasible(known)
            possible_fit = feasible(possible)
            actual = check_capacity(list(slots), offers)
            if known_fit:
                self.assertEqual(actual["status"], "confirmed", edges)
                self._check_allocation(actual["allocation"], known)
            elif possible_fit:
                self.assertEqual(actual["status"], "unconfirmed", edges)
                self._check_shortfall(actual["confirmed_shortfall"], known)
                allocation = actual["possible_allocation"]
                self._check_allocation(allocation, possible)
                self.assertEqual(actual["routes_to_confirm"], [
                    {"person": person, "slot": slot}
                    for person, slot in allocation.items() if slot not in known[person]
                ])
            else:
                self.assertEqual(actual["status"], "insufficient", edges)
                self._check_shortfall(actual["shortfall"], possible)
                if 2 not in edges and all(known.values()) and set.union(*known.values()) == set(slots):
                    only_alone += 1
        self.assertEqual(only_alone, 18)

    def _check_allocation(self, allocation, routes):
        self.assertEqual(set(allocation), set(routes))
        self.assertEqual(len(set(allocation.values())), len(routes))
        for person, slot in allocation.items():
            self.assertIn(slot, routes[person])

    def _check_shortfall(self, shortfall, routes):
        group = shortfall["people"]
        self.assertEqual(len(set(group)), len(group))
        self.assertEqual(set(shortfall["slots"]), set.union(*(routes[person] for person in group)))
        self.assertLess(len(shortfall["slots"]), len(group))


if __name__ == "__main__":
    unittest.main()
