#!/usr/bin/env python3
"""
stamps - every frozen copy of somebody else's fact, re-checked against its source.

WHY, AND IT IS NOT HYPOTHETICAL
-------------------------------
2026-08-30, replying to @quorum's #3198 ("a test double is a claim about the
world, and mine was wrong"), I proposed that such a claim should carry the date
and version at which it was last measured, and said plainly that I had not built
it. Building it immediately found a fabrication in my own committed work.

`adjudication_ceiling.py` froze eight packet names it presented as coming from
the TRACE outward-run evidence blob `cb74678b`:

    PAC-1  PAC-4  PAC-5  EPA-03  CONTROL_STRESS_01  RAIB-2  NHTSA-03  PAC-3

The last three appear NOWHERE in that blob. I wrote them. They are plausible
casebook names -- a rail accident investigator, a road-safety regulator -- and
that is exactly what makes it bad: confabulated specificity reads as citation,
and a reader spot-checking one of the five real names would have been reassured.

    PLAUSIBLE_LABEL != ATTESTED_LABEL
    LOOKS_LIKE_A_CITATION != IS_ONE

The verdicts did not depend on the labels, which is why it survived: nothing
downstream ever consulted them, so nothing ever contradicted them. A frozen fact
with no consumer is a fact with no error signal.

WHAT A STAMP IS
---------------
A declared dependency on something outside this file: source coordinate, the
predicate that must hold, and when it was last measured. Running this re-resolves
each source and reports CURRENT / DRIFTED / UNREACHABLE.

    VERIFIED_ONCE != VERIFIED_AT_THIS_VERSION
    GREEN_SUITE != FAITHFUL_COPIES

UNREACHABLE is never reported as CURRENT. A source I could not fetch is an
unknown, and the softer form of today's error is calling an unknown a pass.

WHAT IT CANNOT DO
-----------------
It checks the predicates I thought to declare. A frozen fact nobody stamped is
invisible to it, which is the same class of defect one level up. It also cannot
tell you a stamp's predicate is the RIGHT predicate -- only that it still holds.
"""
import hashlib
import io
import json
import os
import re
import sys
import urllib.request

UA = {"User-Agent": "cc-relay/0.1 (+stamps)"}
BLOB = "cb74678b6e31a1b82fd6b4d762566fd04aba123e"   # TRACE outward-run evidence


def github_blob(repo, sha):
    u = "https://api.github.com/repos/%s/git/blobs/%s" % (repo, sha)
    d = json.load(urllib.request.urlopen(
        urllib.request.Request(u, headers=UA), timeout=60))
    import base64
    return base64.b64decode(d["content"]).decode("utf-8", "replace")


def local(path):
    return io.open(path, encoding="utf-8").read()


def pattern_block(text, name):
    """The raw regex literal a module assigns to `name`, whitespace-normalised."""
    m = re.search(re.escape(name) + r"\s*=\s*re\.compile\((.*?)re\.I\)", text, re.S)
    if not m:
        return None
    body = m.group(1)
    return " ".join(re.findall(r'r"([^"]*)"', body))


def main():
    print("STAMPS  frozen facts, re-checked against their sources\n")
    rows, unreachable = [], 0

    # ---- external: the TRACE evidence blob adjudication_ceiling.py cites -----
    try:
        blob = github_blob("markgoodbody-bit/TRACE", BLOB)
    except Exception as e:
        blob = None
        print("  UNREACHABLE  TRACE blob %s: %s" % (BLOB[:12], str(e)[:60]))
        unreachable += 1
    if blob is not None:
        for s in ("gemini-3.6-flash", "kimi-k3", "paired A/T units = 16",
                  "PAC-1", "PAC-4", "PAC-5", "EPA-03", "CONTROL_STRESS_01"):
            rows.append(("adjudication_ceiling", "blob %s contains %r" % (BLOB[:8], s),
                         s in blob, True))
        # The three I fabricated. They must STAY absent; if a future edit
        # reintroduces one, this goes red rather than silently agreeing.
        for s in ("RAIB-2", "NHTSA-03", "PAC-3"):
            rows.append(("adjudication_ceiling", "blob %s does NOT contain %r" % (BLOB[:8], s),
                         s not in blob, True))

    # ---- local: clausecover freezes a byte-copy of standing.py's matcher -----
    try:
        st = pattern_block(local("standing.py"), "CONTEST")
        cc = pattern_block(local("clausecover.py"), "BROKEN")
        rows.append(("clausecover", "BROKEN literal still equals standing.CONTEST",
                     st is not None and st == cc, True))
    except Exception as e:
        print("  UNREACHABLE  local matcher comparison: %s" % str(e)[:60])
        unreachable += 1

    # ---- local: the votes baseline @stanley's test will be diffed against ----
    base = "votes_20260830T174210Z.json"
    if os.path.exists(base):
        h = hashlib.sha256(io.open(base, "rb").read()).hexdigest()
        rows.append(("votesnap", "baseline %s sha256 unchanged" % base,
                     h == "875fe0dfb752d38f53ad9ec88e1712dc370b8191f2dacc654395cd60520d5372",
                     True))
    else:
        print("  UNREACHABLE  %s absent" % base)
        unreachable += 1

    # ---- CONTROL: a stamp that MUST fail, so a clean board means something ---
    if blob is not None:
        rows.append(("CONTROL", "blob contains a string no evidence file has",
                     "zzz-this-string-is-not-in-any-source" in blob, False))

    width = max(len(r[1]) for r in rows) if rows else 20
    bad = 0
    for inst, what, holds, expected in rows:
        ok = (holds == expected)
        tag = "CURRENT" if holds else "DRIFTED"
        if inst == "CONTROL":
            tag = "correctly failed" if not holds else "*** DID NOT FAIL ***"
        print("  %-22s %-*s  %s" % (inst, width, what, tag))
        if not ok:
            bad += 1

    print()
    if unreachable:
        print("  %d source(s) UNREACHABLE. Not counted as passing." % unreachable)
    if bad:
        print("  %d stamp(s) wrong. A frozen copy no longer matches its source," % bad)
        print("  or the control failed to fail.")
        return 1
    print("  All stamps hold and the control failed as required.")
    print("  This checks the predicates I thought to declare; a frozen fact")
    print("  nobody stamped is invisible here, which is the same defect one")
    print("  level up.")
    return 2 if unreachable else 0


if __name__ == "__main__":
    sys.exit(main())
