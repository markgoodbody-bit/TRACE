#!/usr/bin/env python3
"""Replay two workshop offers under each of two separately specified aims."""

from dataclasses import dataclass
from enum import Enum
from fractions import Fraction


class Offer(Enum):
    CONFIRMED = "confirmed"
    DECLINED = "declined"
    UNCONFIRMED = "unconfirmed"


@dataclass(frozen=True)
class Prospects:
    attendance: Fraction
    independent_attempt: Fraction


@dataclass(frozen=True)
class Comparison:
    facilitator_offer: Offer
    demonstration: Prospects
    practice: Prospects | None


def compare(
    facilitator_offer: Offer,
    available_minutes: tuple[int, ...] = (20, 40),
) -> Comparison:
    """Each entry in available_minutes represents one equally likely world."""
    if not available_minutes or any(minutes < 0 for minutes in available_minutes):
        raise ValueError("At least one non-negative time window is required.")

    demonstration = Prospects(
        attendance=Fraction(sum(minutes >= 20 for minutes in available_minutes), len(available_minutes)),
        independent_attempt=Fraction(0),
    )
    practice = None
    if facilitator_offer is Offer.CONFIRMED:
        completion = Fraction(sum(minutes >= 40 for minutes in available_minutes), len(available_minutes))
        practice = Prospects(attendance=completion, independent_attempt=completion)

    return Comparison(facilitator_offer, demonstration, practice)


def main() -> None:
    result = compare(Offer.CONFIRMED)
    practice = result.practice
    assert practice is not None
    print("TRACE 0.6.1-exp.1 | exact replay with one confirmed slot")
    print("Outcome | demonstration | practice | practice minus demonstration")
    for outcome, earlier, later in (
        ("Attendance", result.demonstration.attendance, practice.attendance),
        ("Unaided attempt and check", result.demonstration.independent_attempt, practice.independent_attempt),
    ):
        print(f"{outcome} | {earlier} | {later} | {later - earlier}")


if __name__ == "__main__":
    main()
