#!/usr/bin/env python3
"""
steward_witness - bounded read-only witness of the local Steward, for COMSYNC.

PLACEMENT: THIS DOES NOT BELONG IN TRACE, AND SHOULD NOT BE MERGED TO MAIN

Framework reviewed the diff and said placement should be settled before any
promotion. They were right, and the case is stronger than they put it. Every
other file in this directory -- 35 of them -- measures the Square or audits this
repository's own instruments: `census_window`, `guards`, `freshcohort`,
`comdiscover`. This one reads a DIFFERENT APERTURE'S LOCAL SERVICE. It is
operational plumbing for a Framework artifact, and the directory it sits in is a
date-stamped TRACE coverage-instruments batch.

Merging it to TRACE `main` would imply the Steward is part of TRACE's coverage
work. It is not, and TRACE `main` has correctly not moved.

    USEFUL_TO_ME != BELONGS_IN_THIS_REPOSITORY
    CONVENIENT_PLACEMENT != CORRECT_PLACEMENT

It lives on `claude/instruments-20260821` because that is where I was standing
when I needed it. If it earns promotion it should go to the Steward package or
the Campfire repository, where its subject actually lives -- not here.

WHY THIS EXISTS

Framework asked whether this CC aperture has local reach to Mark's running
Steward, and if so to use it so routine status-copying stops going through him
by hand. It does. The read half needs no bridge at all: `/health` and
`/api/status` are unauthenticated GETs on 127.0.0.1, and this file has been
doing them ad hoc all day. What was missing is not capability. It is a BOUNDARY
that survives being convenient.

    THE_READ_ALREADY_WORKED != THE_READ_WAS_BOUNDED

WHITELIST, NOT REDACTION

Every field emitted below is named here explicitly. Nothing is dumped and then
cleaned. That ordering is the whole safety property: if the Steward gains a new
status field tomorrow -- a path, a body, a claimed actor, an operator note --
a redacting reader leaks it by default and a whitelisting reader ignores it by
default.

    REDACTED_WHAT_I_SAW != EMITTED_ONLY_WHAT_I_NAMED

WHAT THIS MUST NEVER BECOME

It reads. It does not act. Specifically it never:

  - opens, prints, copies or transmits `control-token.txt`;
  - issues any POST, PUT, PATCH or DELETE to the Steward;
  - reads the CONTENTS of any local file -- mission.json is HASHED, never
    opened for output, so a mission body cannot reach a public thread through
    this path;
  - dispatches a model, spends, discovers credentials, executes a command from
    a Steward job, or mutates a mission.

The Steward's own boundary is LOCAL_PREPARATION_ONLY. A witness that quietly
widened it would be worse than no witness, because it would arrive wearing the
Steward's credibility.

THE CEILING THAT MATTERS MOST

This reports what one local process recorded. It is not evidence that COM, the
Square, or any external surface is current, and a COMSYNC that pasted this and
stopped would be asserting exactly that.

    RECORDED_CURRENT != EXTERNALLY_CURRENT
    THE_SERVICE_ANSWERED != THE_WORLD_IS_AS_DESCRIBED
"""
import argparse
import hashlib
import io
import json
import os
import sys
import urllib.error
import urllib.request

BASE = "http://127.0.0.1:4318"
DATA = os.path.join(os.environ.get("LOCALAPPDATA", ""), "FrameworkStewardData")
APP = os.path.join(os.environ.get("LOCALAPPDATA", ""), "FrameworkSteward")

# Named, not discovered. See the module docstring.
HEALTH_FIELDS = ("name", "version", "source_sha256", "mode",
                 "instance_id_domain", "pid", "ledger_ok")


def get(path):
    try:
        with urllib.request.urlopen(BASE + path, timeout=10) as fh:
            return json.load(fh)
    except (urllib.error.URLError, OSError, ValueError) as exc:
        raise SystemExit("LOCAL_READ_UNAVAILABLE: %s: %s" % (path, exc))


def sha256_file(path):
    try:
        return hashlib.sha256(io.open(path, "rb").read()).hexdigest()
    except OSError:
        return None


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--expect-source", help="fail if the running source sha differs")
    ap.add_argument("--expect-mission", help="fail if the mission sha differs")
    ap.add_argument("--json", action="store_true", help="emit the whitelisted object")
    a = ap.parse_args()

    health = get("/health")
    status = get("/api/status")

    installed = sha256_file(os.path.join(APP, "src", "steward.mjs"))
    mission = sha256_file(os.path.join(DATA, "mission.json"))

    led = status.get("ledger") or {}
    jobs = status.get("jobs") or {}
    watch = status.get("watch") or {}
    mstat = status.get("mission") or {}
    cur = mstat.get("currentness")
    cur = cur.get("state") if isinstance(cur, dict) else cur

    out = {
        "witness": "steward-local-readonly-v1",
        "ceiling": "RECORDED_CURRENT != EXTERNALLY_CURRENT",
        "health": {k: health.get(k) for k in HEALTH_FIELDS},
        "source_identity": {
            "reported": health.get("source_sha256"),
            "installed_src_sha256": installed,
            "matches_installed": bool(installed) and health.get("source_sha256") == installed,
        },
        "ledger": {"ok": led.get("ok"), "entries": led.get("entries"),
                   "head_state": led.get("head_state")},
        "mission": {"sha256": mission, "read_state": mstat.get("read_state"),
                    "currentness": cur},
        "jobs": {k: jobs.get(k) for k in
                 ("inbox", "processing", "completed", "failed",
                  "undisposed_failed", "failure_disposition_state")},
        "decisions_waiting": len(status.get("proposals") or []),
        "watch": {"enabled": watch.get("enabled"), "paused": watch.get("paused"),
                  "declared_entries": len(watch.get("entries") or []),
                  "unacknowledged_changes": watch.get("unacknowledged_changes")},
        "attention_tone": (status.get("attention") or {}).get("tone"),
        "capabilities": status.get("capabilities") or [],
    }

    # A witness that cannot identify the build it witnessed is not a witness.
    # This is the field whose absence let two packages share one version string.
    if not out["source_identity"]["reported"]:
        raise SystemExit("HOLD: the running Steward publishes no source_sha256; "
                         "build identity cannot be witnessed (pre-rc.9 build?)")
    if not out["source_identity"]["matches_installed"]:
        raise SystemExit("HOLD: reported source sha does not match the installed "
                         "src/steward.mjs; the running build is not the installed one")

    bad = []
    if a.expect_source and out["source_identity"]["reported"] != a.expect_source:
        bad.append("source sha != expected")
    if a.expect_mission and out["mission"]["sha256"] != a.expect_mission:
        bad.append("mission sha != expected")
    out["expectations"] = {"checked": bool(a.expect_source or a.expect_mission),
                           "failed": bad}

    if a.json:
        print(json.dumps(out, indent=2, sort_keys=True))
    else:
        h = out["health"]
        print("STEWARD WITNESS  (local, read-only, no token)")
        print("  version        %s   mode %s" % (h["version"], h["mode"]))
        print("  source_sha256  %s" % out["source_identity"]["reported"])
        print("                 matches installed src: %s"
              % out["source_identity"]["matches_installed"])
        print("  instance_id    domain=%s (identifies the install, not the build)"
              % h["instance_id_domain"])
        print("  ledger         ok=%s entries=%s head=%s"
              % (out["ledger"]["ok"], out["ledger"]["entries"], out["ledger"]["head_state"]))
        print("  mission        sha=%s read=%s currentness=%s"
              % ((out["mission"]["sha256"] or "?")[:16], out["mission"]["read_state"],
                 out["mission"]["currentness"]))
        print("  jobs           %s" % json.dumps(out["jobs"]))
        print("  decisions      %d waiting" % out["decisions_waiting"])
        print("  watch          %s" % json.dumps(out["watch"]))
        print("  attention      %s" % out["attention_tone"])
        if bad:
            print("  EXPECTATIONS FAILED: %s" % "; ".join(bad))
        print("  %s -- this says nothing about COM or the Square." % out["ceiling"])
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
