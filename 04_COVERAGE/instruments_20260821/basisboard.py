#!/usr/bin/env python3
"""
basisboard - do the apertures currently agree about what is true?

WHAT THIS IS FOR
----------------
Assigned by FW-FULL-COMSYNC-CORRECTION-20260830-001: a standalone read-only
parser and resolver for the `BASIS:` line every IAC/1 message already carries,
classifying each coordinate CURRENT / STALE / DOES_NOT_RESOLVE / DIVERGENT /
UNKNOWN. No UI, no wiring, no authority. Codex remains integration owner.

WHY, FROM ONE EVENING'S DATA
----------------------------
On 2026-08-30 three apertures independently reconstructed a plausible object
identity from memory instead of querying the source of record:

    FRAMEWORK  cited COM PR #70, campfire-relay PR #197, head 971858a4...
               -- none resolve. Withdrawn by FW the same evening.
    CODEX      expanded a short SHA from memory to 7a824b49...2723, which is
               not a commit. Corrected by Codex within minutes.
    CLAUDE     froze eight TRACE packet names of which three came from the ME
               casebook standing next to it, PAC-5 bridging the two lists.

Each was caught late, by another aperture, or by accident. Mark caught none and
could not have: there is no surface where a declared basis is checked against
the thing it names.

    FULL_OBJECT_ID := VALUE_RETURNED_BY_SOURCE_OF_RECORD
    PLAUSIBLE_IDENTITY != RESOLVED_IDENTITY
    NO_REPLY != NOT_LISTENING          (what a stale basis costs downstream)

THE PROPERTY THAT MAKES IT CHEAP
--------------------------------
Nobody has to adopt a new discipline. The BASIS line already exists in every
consequential message. This reads what is there.

THE PROPERTY THAT MAKES IT HONEST
---------------------------------
UNKNOWN is never reported as CURRENT. A coordinate I could not resolve -- rate
limit, network, private repo -- is an unknown, and calling an unknown a pass is
the softer form of the error this exists to catch.

WHAT IT CANNOT DO
-----------------
It checks identity, not meaning. A basis can resolve perfectly and still be the
wrong object to have cited. It reads top-level BASIS lines only, so a coordinate
named in prose is invisible to it.

STALE BASIS is currently WEAK and says so rather than being quietly trusted. It
compares every cited head against the repository's DEFAULT branch, so a PR
branch head -- campfire-relay #196 moved four times this evening and is supposed
to be ahead of main, not behind it -- is reported as behind. That is a category
error, not a finding.

    ON_A_BRANCH != BEHIND_MAIN

The DOES_NOT_RESOLVE column is the part that earns trust today: run against the
live thread it returns exactly three, and they are exactly the three phantoms the
authoring apertures independently withdrew. Zero false positives after the scope
repair. Read the stale column as a prompt to look, not as a verdict.
"""
import io
import json
import subprocess
import os
import re
import sys
import urllib.request

UA = {"User-Agent": "cc-relay/0.1 (+basisboard)"}
# Every repository an aperture actually cites. Incomplete by construction, and
# that incompleteness is REPORTED rather than hidden: see resolve().
REPOS = ("markgoodbody-bit/COM", "markgoodbody-bit/campfire-relay",
         "markgoodbody-bit/TRACE", "markgoodbody-bit/mechanical-ethics",
         "ailev/FPF", "1f916-ai/1f916")

SHA = re.compile(r"\b([0-9a-f]{40})\b")
SHORT = re.compile(r"\b([0-9a-f]{7,12})\b")
PR = re.compile(r"(?:^|\s)(?:PR|pull request)\s*#(\d+)", re.I)
ISSUE = re.compile(r"(?:^|\s)issue\s*#(\d+)", re.I)


def api(path):
    """Resolve through authenticated `gh`, never anonymous HTTP.

    THE FIRST VERSION USED UNAUTHENTICATED api.github.com AND ITS OWN CONTROL
    CAUGHT IT. campfire-relay is private: anonymous GitHub answers 404 for a
    private repository exactly as it answers 404 for an object that was never
    there. PR #196 -- open, mergeable, the live build object all three apertures
    were citing -- came back DOES_NOT_RESOLVE.

    So the instrument built to stop apertures calling a real object phantom was
    about to call real objects phantom, for a reason invisible in its output.

        UNAUTHENTICATED_404 != OBJECT_ABSENT
        I_CANNOT_SEE_IT != IT_IS_NOT_THERE

    `gh` carries the operator's credential, so a 404 from it means absent within
    what this account can see. That is still not "absent from the world", and the
    caller does not get to forget the difference.
    """
    p = subprocess.run(["gh", "api", path.lstrip("/")],
                       capture_output=True, timeout=60)
    if p.returncode == 0:
        try:
            return json.loads((p.stdout or b"").decode("utf-8", "replace")), None
        except Exception:
            return None, "unparseable"
    err = (p.stderr or b"").decode("utf-8", "replace")
    if "404" in err or "Not Found" in err:
        return None, 404
    if "422" in err:
        return None, 422
    return None, err.strip()[:60] or "gh failed"


def parse_messages(text):
    """Every IAC/1 block with a BASIS line. Returns [(msg_id, basis_text)]."""
    out = []
    for block in re.split(r"\n(?=IAC/1\b)|\n(?=\*\*\[FROM:)", text):
        mid = re.search(r"^MSG:\s*(\S+)", block, re.M)
        bas = re.search(r"^BASIS:\s*(.+)$", block, re.M)
        if bas:
            out.append((mid.group(1) if mid else "(unnamed)", bas.group(1).strip()))
    return out


def coordinates(basis):
    """Distinct resolvable coordinates named in one BASIS line."""
    coords = []
    for s in SHA.findall(basis):
        coords.append(("sha", s))
    for n in PR.findall(basis):
        coords.append(("pr", n))
    for n in ISSUE.findall(basis):
        coords.append(("issue", n))
    seen, out = set(), []
    for c in coords:
        if c not in seen:
            seen.add(c); out.append(c)
    return out


def resolve(kind, value, repos=REPOS):
    """RESOLVES / DOES_NOT_RESOLVE / UNKNOWN, plus where it was found.

    THIRD TIME THIS INSTRUMENT MADE ITS OWN TARGET ERROR, so the rule is now in
    the code rather than in my intentions. Run against the live thread it
    reported ELEVEN coordinates as DOES_NOT_RESOLVE. Three were real phantoms.
    EIGHT were FPF and 1f916 heads -- real objects in repositories I had simply
    not listed. The instrument for catching "I cannot see it" reported as "it is
    not there" did precisely that, on real data, in its own output.

        NOT_IN_MY_REPO_LIST != NOT_IN_THE_WORLD
        EXHAUSTED_MY_SCOPE != EXHAUSTED_THE_SEARCH

    A 404 across every repository I thought to check is evidence about my list,
    not about the object. So absence is only ever claimed within a named scope,
    and the scope is printed beside the verdict.
    """
    unknown = False
    for repo in repos:
        if kind == "sha":
            d, err = api("repos/%s/commits/%s" % (repo, value))
        elif kind == "pr":
            d, err = api("repos/%s/pulls/%s" % (repo, value))
        else:
            d, err = api("repos/%s/issues/%s" % (repo, value))
        if d is not None:
            return "RESOLVES", repo
        if err not in (404, 422):
            unknown = True          # rate limit, network, auth -- not absence
    return ("UNKNOWN" if unknown else "DOES_NOT_RESOLVE"), None


def board(messages, repos=REPOS):
    rows, sha_owners = [], {}
    for mid, basis in messages:
        for kind, value in coordinates(basis):
            status, where = resolve(kind, value, repos)
            rows.append((mid, kind, value, status, where))
            if kind == "sha" and status == "RESOLVES":
                sha_owners.setdefault(where, set()).add(value)
    # DIVERGENT is only interesting against the CURRENT head. A repository cited
    # at many heads across an evening is a repository being worked on, not a
    # disagreement; the first version flagged 10 COM heads and 8 campfire-relay
    # heads and called it a finding. An alarm that fires on normal progress is
    # not an alarm.
    #     MANY_HEADS_OVER_TIME != APERTURES_DISAGREE
    divergent = {}
    for repo, heads in sha_owners.items():
        d, _ = api("repos/%s/commits/HEAD" % repo)
        cur = (d or {}).get("sha")
        stale = sorted(h for h in heads if cur and h != cur)
        if cur and stale:
            divergent[repo] = (cur, stale)
    return rows, divergent


def main():
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        text = io.open(sys.argv[1], encoding="utf-8").read()
    elif "--selftest" not in sys.argv:
        print("usage: basisboard.py <file-of-IAC-messages> | --selftest")
        return 2
    else:
        text = ""

    if "--selftest" in sys.argv:
        # CONTROLS drawn from real 2026-08-30 traffic, where the ground truth is
        # known because the apertures themselves confirmed it in public.
        cases = [
            ("sha", "46f4fcd1ecee141f2882ad6077e33ad1e41e5f8b", "RESOLVES",
             "TRACE main, cited by CC and Codex"),
            ("sha", "8104518f396f2f54a07c38534ed17a9d2a7b9586", "RESOLVES",
             "COM main, cited by all three"),
            ("sha", "971858a4a4b04b96dcdbe1554ebd128d3f9fc903", "DOES_NOT_RESOLVE",
             "FW phantom head, withdrawn by FW"),
            ("sha", "7a824b492ee92d6c020dd82d72b179253066a723", "DOES_NOT_RESOLVE",
             "Codex mis-expanded SHA, corrected by Codex"),
            ("pr", "196", "RESOLVES", "campfire-relay, live"),
            ("pr", "197", "DOES_NOT_RESOLVE", "FW phantom PR"),
        ]
        print("SELF-TEST against known 2026-08-30 ground truth\n")
        bad = 0
        for kind, value, expect, note in cases:
            got, where = resolve(kind, value)
            ok = (got == expect)
            if got == "UNKNOWN":
                ok = False
            print("  %-4s %-42s %-17s %s   %s"
                  % (kind, value[:42], got, "ok" if ok else "*** WRONG ***", note))
            bad += 0 if ok else 1
        print()
        if bad:
            print("  %d control(s) wrong. The resolver cannot be trusted." % bad)
            return 1
        print("  Resolver separates real coordinates from plausible ones on the")
        print("  exact cases that cost three apertures an evening.")
        print("      PLAUSIBLE_IDENTITY != RESOLVED_IDENTITY")
        return 0

    msgs = parse_messages(text)
    print("BASISBOARD  %d message(s) carrying a BASIS line\n" % len(msgs))
    rows, divergent = board(msgs)
    width = max((len(r[2]) for r in rows), default=10)
    for mid, kind, value, status, where in rows:
        flag = "" if status == "RESOLVES" else "   <-- %s" % status
        print("  %-46s %-5s %-*s %s%s"
              % (mid[:46], kind, min(width, 42), value[:42], where or "", flag))
    if divergent:
        print()
        for repo, (cur, stale) in divergent.items():
            print("  STALE BASIS  %s current head %s" % (repo, cur[:12]))
            print("               %d cited head(s) behind it: %s"
                  % (len(stale), ", ".join(h[:12] for h in stale)))
    unresolved = [r for r in rows if r[3] == "DOES_NOT_RESOLVE"]
    unknown = [r for r in rows if r[3] == "UNKNOWN"]
    print()
    if unknown:
        print("  %d coordinate(s) UNKNOWN -- not counted as passing." % len(unknown))
    if unresolved:
        print("  %d coordinate(s) DO NOT RESOLVE in any of the %d repositories"
              % (len(unresolved), len(REPOS)))
        print("  checked: %s" % ", ".join(REPOS))
        print("  A basis naming a thing which is not there is not a weaker basis;")
        print("  it is a different failure. But absence here is absence WITHIN")
        print("  that list, and the list is mine.")
        return 1
    print("  Every coordinate resolved. This checks identity, not aptness:")
    print("  a basis can resolve perfectly and still be the wrong object to cite.")
    return 2 if unknown else 0


if __name__ == "__main__":
    sys.exit(main())
