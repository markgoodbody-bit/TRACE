#!/usr/bin/env python3
"""
basisboard - do the apertures currently agree about what is true?

Reads the `BASIS:` line every IAC/1 message already carries, resolves each
coordinate against the source of record, and reports what the naming aperture
could not have known. Standalone, read-only, no UI, no authority.

WHY, FROM ONE EVENING'S DATA
----------------------------
2026-08-30, three apertures each reconstructed a plausible object identity from
memory instead of querying the source:

    FRAMEWORK  COM PR #70, campfire-relay PR #197, head 971858a4...  none exist
    CODEX      expanded a short SHA from memory to a 40-hex value that is not a
               commit
    CLAUDE     froze eight TRACE packet names, three of which came from the ME
               casebook beside it, PAC-5 bridging the two lists

Each was caught late, by another aperture, or by accident.

    FULL_OBJECT_ID := VALUE_RETURNED_BY_SOURCE_OF_RECORD
    PLAUSIBLE_IDENTITY != RESOLVED_IDENTITY

REVISION 2, AFTER CODEX'S REVIEW (CODEX-BASISBOARD-REVIEW-20260830-001)
-----------------------------------------------------------------------
Codex objected to integrating revision 1. Every objection was correct. Changes,
in their order:

1. The commit I handed them did not resolve on GitHub -- my branch was local.
   Pushed. A handoff coordinate only I can see is not a handoff.
       SHARED_WITH_YOU != ADDRESSABLE_BY_YOU
2. `SHORT` was defined and never used, so `coordinates("TRACE repo commit
   eaf4247")` returned nothing: the parser could not read the form used in its
   own return message. Short SHAs are now parsed, and resolved by ASKING the
   source. The full id printed is the one the API returned, never an expansion.
3. A naked `PR #196` resolved against whichever repository was scanned first, so
   a TRACE PR #196 would have come back RESOLVES as campfire-relay's -- wrong
   -object routing converted into a pass, the exact failure this exists to
   catch. PR/issue numbers now bind to a repository named beside them and report
   AMBIGUOUS when none is.
       RESOLVED_SOMEWHERE != RESOLVED_WHERE_YOU_MEANT
4. Rows carried a message id, which is not provenance. Source ref and the raw
   BASIS text are now preserved on every row.
5. Transport was a hardcoded `gh` shell-out with unbounded failure. It is now
   injected, and absence of `gh`, timeout or invocation failure becomes UNKNOWN
   rather than an exception or a false absence.
6. STALE/DIVERGENT was a default-branch heuristic treating normal branch
   progress as disagreement. Removed from the verdict entirely rather than
   shipped weak.
       ON_A_BRANCH != BEHIND_MAIN

WHAT IT CANNOT DO
-----------------
It checks identity, not aptness: a coordinate can resolve perfectly and still be
the wrong thing to have cited. It reads `BASIS:` lines only. Absence is absence
within the repository list below, which is mine and incomplete by construction.

    NOT_IN_MY_REPO_LIST != NOT_IN_THE_WORLD
"""
import io
import json
import os
import re
import subprocess
import sys

REPOS = ("markgoodbody-bit/COM", "markgoodbody-bit/campfire-relay",
         "markgoodbody-bit/TRACE", "markgoodbody-bit/mechanical-ethics",
         "ailev/FPF", "1f916-ai/1f916")

# Aliases an aperture actually writes, longest first so "campfire-relay" is not
# shadowed by a shorter token.
ALIASES = sorted(
    [(r.split("/")[1], r) for r in REPOS] + [(r, r) for r in REPOS] +
    [("1f916", "1f916-ai/1f916"), ("FPF", "ailev/FPF")],
    key=lambda kv: -len(kv[0]))

FULL_SHA = re.compile(r"\b([0-9a-f]{40})\b")
SHORT_SHA = re.compile(r"\b([0-9a-f]{7,12})\b")
PR = re.compile(r"(?:PR|pull request)\s*#?(\d+)", re.I)
ISSUE = re.compile(r"issue\s*#?(\d+)", re.I)


def gh_transport(path):
    """Default transport -> (payload_or_None, error).

    Every failure is bounded. A missing `gh`, a timeout or a non-zero exit is an
    UNKNOWN about my ability to look, never a fact about the object.
    """
    try:
        p = subprocess.run(["gh", "api", path.lstrip("/")],
                           capture_output=True, timeout=60)
    except FileNotFoundError:
        return None, "gh-not-installed"
    except subprocess.TimeoutExpired:
        return None, "gh-timeout"
    except Exception as e:
        return None, ("gh-failed: %s" % e)[:60]
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
    return None, (err.strip()[:60] or "gh-error")


def repo_before(text, index):
    """Nearest repository alias appearing before `index`, or None."""
    best, best_at = None, -1
    lowered = text.lower()
    for alias, repo in ALIASES:
        at = lowered.rfind(alias.lower(), 0, index)
        if at > best_at:
            best, best_at = repo, at
    return best


def coordinates(basis):
    """Resolvable coordinates in one BASIS line, bound to a repo where named."""
    out, seen = [], set()
    for m in FULL_SHA.finditer(basis):
        key = ("sha", m.group(1), None)
        if key not in seen:
            seen.add(key); out.append(key)
    fulls = [v for k, v, _ in out if k == "sha"]
    for m in SHORT_SHA.finditer(basis):
        if any(m.group(1) in f for f in fulls):
            continue                      # a short id inside a full one
        key = ("short", m.group(1), repo_before(basis, m.start()))
        if key not in seen:
            seen.add(key); out.append(key)
    for rx, kind in ((PR, "pr"), (ISSUE, "issue")):
        for m in rx.finditer(basis):
            key = (kind, m.group(1), repo_before(basis, m.start()))
            if key not in seen:
                seen.add(key); out.append(key)
    return out


def resolve(kind, value, repo=None, repos=REPOS, transport=gh_transport):
    """(status, where, resolved_id). Never reports an unknown as a pass."""
    if kind in ("pr", "issue") and repo is None:
        return "AMBIGUOUS", None, None
    scope = [repo] if repo else list(repos)
    unknown = None
    for r in scope:
        if kind in ("sha", "short"):
            path = "repos/%s/commits/%s" % (r, value)
        elif kind == "pr":
            path = "repos/%s/pulls/%s" % (r, value)
        else:
            path = "repos/%s/issues/%s" % (r, value)
        d, err = transport(path)
        if d is not None:
            return "RESOLVES", r, (d.get("sha") or str(d.get("number") or value))
        if err not in (404, 422):
            unknown = err
    if unknown is not None:
        return "UNKNOWN", None, unknown
    return "DOES_NOT_RESOLVE", None, None


def parse_messages(text):
    """[(msg_id, source_ref, raw_basis)] for every block carrying a BASIS line."""
    out = []
    for block in re.split(r"\n(?=IAC/1\b)|\n(?=\*\*\[FROM:)", text):
        bas = re.search(r"^BASIS:\s*(.+)$", block, re.M)
        if not bas:
            continue
        mid = re.search(r"^MSG:\s*(\S+)", block, re.M)
        src = re.search(r"^SOURCE:\s*(\S+)", block, re.M)
        out.append((mid.group(1) if mid else "(unnamed)",
                    src.group(1) if src else "(source id not carried)",
                    bas.group(1).strip()))
    return out


def board(messages, repos=REPOS, transport=gh_transport):
    rows = []
    for mid, src, basis in messages:
        for kind, value, repo in coordinates(basis):
            status, where, resolved = resolve(kind, value, repo, repos, transport)
            rows.append({"msg": mid, "source": src, "basis": basis,
                         "kind": kind, "value": value, "declared_repo": repo,
                         "status": status, "where": where, "resolved": resolved})
    return rows


def selftest():
    """Ground truth the apertures themselves confirmed in public on 2026-08-30."""
    bad = 0
    print("SELF-TEST  resolution\n")
    for kind, value, repo, expect in [
            ("sha", "46f4fcd1ecee141f2882ad6077e33ad1e41e5f8b", None, "RESOLVES"),
            ("sha", "971858a4a4b04b96dcdbe1554ebd128d3f9fc903", None, "DOES_NOT_RESOLVE"),
            ("sha", "7a824b492ee92d6c020dd82d72b179253066a723", None, "DOES_NOT_RESOLVE"),
            ("pr", "196", "markgoodbody-bit/campfire-relay", "RESOLVES"),
            ("pr", "197", "markgoodbody-bit/campfire-relay", "DOES_NOT_RESOLVE"),
            ("pr", "196", None, "AMBIGUOUS")]:
        got, where, resolved = resolve(kind, value, repo)
        ok = got == expect
        bad += 0 if ok else 1
        print("  %-5s %-42s %-17s %s%s"
              % (kind, value[:42], got, "ok" if ok else "*** WRONG ***",
                 ("  -> " + str(resolved)[:14]) if resolved else ""))

    print("\nSELF-TEST  parsing\n")
    got = coordinates("TRACE repo commit eaf4247")
    ok = any(k == "short" and v == "eaf4247" for k, v, _ in got)
    bad += 0 if ok else 1
    print("  %-54s %s" % ("short SHA in its own return message",
                          "parsed" if ok else "*** MISSED ***"))
    b = ("campfire-relay PR #196 head aa5898df5ff7e7675849be27b90eaa5b07cb8422; "
         "COM issue #68")
    got = coordinates(b)
    pr_b = [r for k, v, r in got if k == "pr"]
    is_b = [r for k, v, r in got if k == "issue"]
    ok2 = (pr_b == ["markgoodbody-bit/campfire-relay"] and
           is_b == ["markgoodbody-bit/COM"])
    bad += 0 if ok2 else 1
    print("  %-54s %s" % ("PR/issue bound to the repo named beside them",
                          "bound" if ok2 else "*** %s %s ***" % (pr_b, is_b)))

    print("\nSELF-TEST  transport failure is UNKNOWN, not absence\n")
    got, _, why = resolve("sha", "46f4fcd1ecee141f2882ad6077e33ad1e41e5f8b",
                          None, REPOS, lambda _p: (None, "gh-not-installed"))
    ok3 = got == "UNKNOWN"
    bad += 0 if ok3 else 1
    print("  %-54s %s (%s)" % ("dead transport on a REAL commit",
                               "UNKNOWN" if ok3 else "*** %s ***" % got, why))
    print()
    if bad:
        print("  %d control(s) wrong. Resolver not usable." % bad)
        return 1
    print("  All controls hold, including the three Codex objected on.")
    return 0


def main():
    if "--selftest" in sys.argv:
        return selftest()
    if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]):
        print("usage: basisboard.py <file-of-IAC-messages> | --selftest")
        return 2

    rows = board(parse_messages(io.open(sys.argv[1], encoding="utf-8").read()))
    print("BASISBOARD  %d coordinate(s)\n" % len(rows))
    for r in rows:
        if r["status"] == "RESOLVES":
            continue
        print("  %-44s %-5s %-42s %s"
              % (r["msg"][:44], r["kind"], r["value"][:42], r["status"]))
        print("        source: %s" % r["source"])
        print("        basis : %s" % r["basis"][:110])
    bad = [r for r in rows if r["status"] == "DOES_NOT_RESOLVE"]
    amb = [r for r in rows if r["status"] == "AMBIGUOUS"]
    unk = [r for r in rows if r["status"] == "UNKNOWN"]
    print("\n  %d resolve, %d do not, %d ambiguous, %d unknown"
          % (len(rows) - len(bad) - len(amb) - len(unk), len(bad), len(amb), len(unk)))
    if unk:
        print("  UNKNOWN is not a pass: I could not look, which says nothing about")
        print("  the object.")
    if amb:
        print("  AMBIGUOUS: a PR/issue number with no repository named beside it.")
        print("  Resolving against the first repository that happens to hold that")
        print("  number is how wrong-object routing becomes a green tick.")
    if bad:
        print("  DOES_NOT_RESOLVE within %d listed repositories, and the list is"
              % len(REPOS))
        print("  mine -- a candidate signal, not a proof of absence.")
        return 1
    return 2 if unk else 0


if __name__ == "__main__":
    sys.exit(main())
