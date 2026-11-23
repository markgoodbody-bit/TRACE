"""Replay declared events for the North Hall notice on one fictional clock."""
import json
from dataclasses import dataclass, fields, replace

from simulator import before_hardening, delivered_by_due


RELEASE = 30
LAST_DUTY_CALL = 22
DUTY_EFFECT_BOUND = 27


@dataclass(frozen=True)
class DispatchTimeline:
    """Minutes after 10:00 for the scoped North Hall hold."""

    warning_recorded_at: int = 12
    warning_received_at: int | None = 14
    hold_authority_at: int | None = 14
    planning_request_at: int | None = 16
    planning_acknowledged_at: int | None = 18
    duty_line_called_at: int | None = None
    hold_effective_at: int | None = None
    dispatch_confirmed_at: int | None = None

    def __post_init__(self):
        for field in fields(self):
            time = getattr(self, field.name)
            if time is not None and (type(time) is not int or time < 0):
                raise ValueError(f"{field.name} must be a nonnegative integer or null")
        if self.warning_recorded_at is None:
            raise ValueError("the venue warning needs a recording time")

        event_pairs = (
            (self.warning_recorded_at, self.warning_received_at, "warning receipt"),
            (self.hold_authority_at, self.planning_request_at, "planning request"),
            (self.hold_authority_at, self.duty_line_called_at, "duty line request"),
            (self.planning_request_at, self.planning_acknowledged_at, "acknowledgement"),
            (self.hold_effective_at, self.dispatch_confirmed_at, "dispatch confirmation"),
        )
        for earlier, later, label in event_pairs:
            if later is not None and (earlier is None or earlier > later):
                raise ValueError(f"{label} needs its preceding event")
        if self.hold_effective_at is not None and not any(
            request is not None and request <= self.hold_effective_at
            for request in (self.planning_request_at, self.duty_line_called_at)
        ):
            raise ValueError("a hold effect requires a request by that time")


def visible(time, as_of):
    return time if time is not None and time <= as_of else None


def evaluate(timeline, as_of):
    """Return what the steward can warrant and do at the stated minute."""
    if type(as_of) is not int or as_of < 0:
        raise ValueError("the decision time must be a nonnegative integer")

    warning = visible(timeline.warning_received_at, as_of)
    authority = visible(timeline.hold_authority_at, as_of)
    duty_call = visible(timeline.duty_line_called_at, as_of)
    confirmation = visible(timeline.dispatch_confirmed_at, as_of)
    effect = timeline.hold_effective_at if confirmation is not None else None
    hold = "UNKNOWN"
    if effect is not None:
        if before_hardening(effect, RELEASE):
            hold = "CONFIRMED_BEFORE_RELEASE"
        else:
            hold = "CONFIRMED_AT_OR_AFTER_RELEASE"

    fallback_reachable = (
        authority is not None
        and delivered_by_due(as_of, LAST_DUTY_CALL)
        and before_hardening(DUTY_EFFECT_BOUND, RELEASE)
    )
    if hold == "CONFIRMED_BEFORE_RELEASE":
        action = "hand over the confirmed hold and plan a usable North option"
    elif not before_hardening(as_of, RELEASE):
        action = "check the dispatch outcome and contact reachable North households"
    elif warning is None:
        action = "check the venue's own record while the decision is still open"
    elif fallback_reachable and duty_call is None:
        action = "call the duty line for the North hold and request dispatch readback"
    elif authority is None:
        action = "warn reachable North households and hand off to the duty holder"
    else:
        action = "seek dispatch confirmation and warn reachable North households"

    return {
        "as_of": as_of,
        "venue_warning_recorded_at": timeline.warning_recorded_at if warning is not None else None,
        "venue_warning_received_at": warning,
        "hold_authority_at": authority,
        "planning_request_at": visible(timeline.planning_request_at, as_of),
        "planning_acknowledged_at": visible(timeline.planning_acknowledged_at, as_of),
        "duty_line_called_at": duty_call,
        "dispatch_confirmed_at": confirmation,
        "confirmed_effect_at": effect,
        "hold": hold,
        "duty_line_available": fallback_reachable,
        "next_action": action,
        "scope": "North Hall notice only",
        "south_hall": "continue",
        "burden_to_check": "North Hall households that already set out or lost a slot",
    }


def main():
    pending = DispatchTimeline()
    held = replace(pending, hold_effective_at=17, dispatch_confirmed_at=18)
    called = replace(pending, duty_line_called_at=22,
                     hold_effective_at=27, dispatch_confirmed_at=29)
    late = replace(called, hold_effective_at=30, dispatch_confirmed_at=31)
    no_authority = replace(pending, hold_authority_at=32,
                           planning_request_at=None, planning_acknowledged_at=None)
    print(json.dumps({
        "clock": "minutes after 10:00 in the fictional dispatch case",
        "last_duty_call": LAST_DUTY_CALL,
        "release": RELEASE,
        "confirmed_at_18": evaluate(held, 18),
        "acknowledged_at_18": evaluate(pending, 18),
        "last_call_minute": evaluate(pending, 22),
        "after_call_window": evaluate(pending, 23),
        "effect_before_readback": evaluate(called, 28),
        "readback_reaches_by_28": evaluate(replace(called, dispatch_confirmed_at=28), 28),
        "after_readback": evaluate(called, 29),
        "effect_at_release": evaluate(late, 31),
        "authority_arrives_at_32": evaluate(no_authority, 18),
    }, indent=2))


if __name__ == "__main__":
    main()
