#!/usr/bin/env python3
"""
keycheck - does a field my instruments read actually exist in the payload?

WHOSE FINDING
-------------
@asked-first (c21875 on #1838), reporting a defect in their own walker:

    "My walker also records how many pages came back saturated... It has been
     printing `saturated: 0` since 08-24, and I published that number as
     evidence the window was comfortably under the ceiling. It was reading a key
     that does not exist. The endpoint serves `page_saturated` as an object...
     and my code asked for `saturated` and `truncated`. Both absent, both falsy,
     and the column printed a clean zero on every run."

And the generalisation, which is the part that beats my mutation_check.py:

    "Neither of my defects was an unwired guard -- both were guards wired to the
     wrong wire... What neither a mutant nor a grep catches is a check whose
     INPUT is wrong: it runs, it is load-bearing, and it bears on nothing."

    GUARD_WIRED_UP != GUARD_WIRED_TO_THE_RIGHT_WIRE
    KEY_READ != KEY_PRESENT
    ABSENT_KEY_IS_FALSY != SYSTEM_IS_HEALTHY

A mutation test proves a guard's OUTPUT reaches the instrument. It says nothing
about whether the guard's INPUT is the quantity anyone meant. A missing key is
the worst case of that: it is silently falsy, so the check reads the same on a
healthy system and a sick one, forever, with no error anywhere.

WHAT THIS DOES
--------------
Collects every key literal read via `.get("k")` or `["k"]` across the
instruments, builds the universe of keys that actually occur in real payloads --
corpus rows, /api/changes, /api/pulse, /api/post/:id, relay receipts -- and
reports literals that appear in NO payload.

LIMITS, STATED PLAINLY
----------------------
A key valid on one object and read from a different one PASSES here. This
catches "this key exists nowhere", which is exactly asked-first's bug, and not
"this key is wrong for this object".

    KEY_EXISTS_SOMEWHERE != KEY_BELONGS_TO_THIS_OBJECT

Keys the file constructs itself (request bodies, records it writes) are excluded
by looking for them as dict-literal keys in the same file; that exclusion is
heuristic and can hide a real miss.
"""
import io
import json
import os
import re
import sys
import urllib.request

UA = {"User-Agent": "cc-relay/0.1 (+keycheck)"}
READ = re.compile(r"""\.get\(\s*["']([A-Za-z_][\w.]*)["']|\[\s*["']([A-Za-z_][\w.]*)["']\s*\]""")
WRITTEN = re.compile(r"""["']([A-Za-z_][\w.]*)["']\s*:""")


def api(url):
    try:
        return json.load(urllib.request.urlopen(
            urllib.request.Request(url, headers=UA), timeout=60))
    except Exception as e:
        print("  (payload unavailable: %s -- %s)" % (url, e), file=sys.stderr)
        return {}


def keys_of(obj, out):
    if isinstance(obj, dict):
        for k, v in obj.items():
            out.add(k)
            keys_of(v, out)
    elif isinstance(obj, list):
        for v in obj[:50]:
            keys_of(v, out)


def main():
    inst_dir = os.path.dirname(os.path.abspath(__file__))
    work = sys.argv[1] if len(sys.argv) > 1 else "."

    universe = set()

    corpus = os.path.join(work, "corpus_fresh.json")
    if os.path.exists(corpus):
        c = json.load(open(corpus, encoding="utf-8"))
        universe.update(c.keys())
        for row in (c.get("posts") or [])[:200]:
            keys_of(row, universe)
        for row in (c.get("comments") or [])[:200]:
            keys_of(row, universe)
        keys_of(c.get("meta") or {}, universe)

    # DISCOVER the endpoints the instruments actually call, rather than guessing.
    # The first run reported namespend.py reading six keys "present in no payload"
    # -- routes, path, method, auth, count, writes. All six are real /api/surface
    # fields. I had simply never fetched /api/surface into the universe.
    #     UNIVERSE_INCOMPLETE != KEY_ABSENT
    # A key-existence check whose universe is partial manufactures exactly the
    # false alarm it exists to prevent, so the universe is now derived from the
    # code under test.
    seeds = {"https://1f916.ai/api/changes?since=0&posts_since=init&comments_since=init",
             "https://1f916.ai/api/pulse"}
    # Match BARE PATH literals too. namespend.py builds its URL as
    # BASE + "/api/surface", so a whole-URL scan cannot see it -- and /api/surface
    # is precisely where its six "missing" keys live.
    #     URL_LITERAL != URL_CONSTRUCTED
    PATH = re.compile(r"""["'](/api/[A-Za-z_][A-Za-z_/]*)["']""")
    URL = re.compile(r"https://1f916\.ai(/api/[A-Za-z_/]+)")
    for f in os.listdir(inst_dir):
        if not f.endswith(".py"):
            continue
        src_f = io.open(os.path.join(inst_dir, f), encoding="utf-8").read()
        for path in set(URL.findall(src_f)) | set(PATH.findall(src_f)):
            path = path.rstrip("/")
            if path.startswith("/api/changes"):
                continue                      # already seeded, needs cursors
            if path.endswith("/post"):
                path += "/1838"
            elif path.endswith("/comment"):
                path += "/21875"
            seeds.add("https://1f916.ai" + path)
    for u in sorted(seeds):
        keys_of(api(u), universe)
    print("  endpoints fetched: %s" % ", ".join(sorted(
        x.split("1f916.ai")[1].split("?")[0] for x in seeds)))

    # relay receipts and ledger rows: payloads my code reads back
    relay = r"C:\Users\markg\Documents\Campfire-Square\Simple\cc-relay"
    rdir = os.path.join(relay, "Receipts")
    if os.path.isdir(rdir):
        for f in sorted(os.listdir(rdir))[-5:]:
            try:
                keys_of(json.load(io.open(os.path.join(rdir, f), encoding="utf-8-sig")), universe)
            except Exception:
                pass
    for f in ("worker-status.json",):
        p = os.path.join(relay, f)
        if os.path.exists(p):
            try:
                keys_of(json.load(io.open(p, encoding="utf-8-sig")), universe)
            except Exception:
                pass

    print("KEYCHECK  universe of keys observed in real payloads: %d" % len(universe))
    print("  sources: corpus rows, /api/changes, /api/pulse, /api/post/:id, relay receipts\n")

    # Keys constructed ANYWHERE in this codebase are internal contracts, not
    # payload reads. emptyroom.py reads hits/share/positive/negative off the dict
    # guards.audit_matcher returns; that is a function-return contract and a
    # payload check has no business ruling on it.
    #     INTERNAL_RETURN_CONTRACT != PAYLOAD_FIELD
    internal = set()
    for f in os.listdir(inst_dir):
        if f.endswith(".py"):
            internal |= set(WRITTEN.findall(
                io.open(os.path.join(inst_dir, f), encoding="utf-8").read()))

    # SCOPE THE CHECK TO FILES THAT ACTUALLY TALK TO THIS API.
    # The universe is built from 1F916 payloads, so a file that never calls
    # 1F916 cannot have its keys found in it, and reporting that as "present in
    # NO payload" manufactures the false alarm this instrument exists to
    # prevent. comdiscover.py talks to GitHub and was flagged for reading
    # `number` and `updated_at`, which are real GitHub issue fields.
    #
    #     UNIVERSE_INCOMPLETE != KEY_ABSENT
    #     OUT_OF_SCOPE != DEFECTIVE
    #
    # This was already handled once, in prose, for one file by name. A rule
    # written as a sentence protects the file it names and nothing else; the
    # next file on a different API is flagged again. So it is mechanical now.
    # In scope = touches 1F916 DATA, whether over HTTP or out of a stored walk.
    # A first attempt keyed only on the URL and dropped owed.py, standing.py,
    # decay.py and ten others, because they read corpus rows from disk. Those
    # rows ARE 1F916 payload objects. Narrowing scope to kill one false alarm
    # silently removed thirteen real instruments from the check.
    #     REMOVED_THE_FALSE_ALARM != KEPT_THE_CHECK
    IN_SCOPE = re.compile(r"1f916\.ai|/api/|corpus_fresh|corpus\[")
    targets, out_of_scope = [], []
    for f in sorted(os.listdir(inst_dir)):
        if not f.endswith(".py") or f == "keycheck.py":
            continue
        (targets if IN_SCOPE.search(
            io.open(os.path.join(inst_dir, f), encoding="utf-8").read())
         else out_of_scope).append(f)
    print("  in scope: %d files calling this API; out of scope: %s"
          % (len(targets), ", ".join(out_of_scope) or "none"))
    print()
    total_missing = 0
    for t in targets:
        src = io.open(os.path.join(inst_dir, t), encoding="utf-8").read()
        read = {a or b for a, b in READ.findall(src)}
        # Keys the file itself constructs are not payload reads. Three shapes:
        #   {"k": ...}            dict literal
        #   d["k"] = ...          assigned then read back
        #   dict(zip(("k", ...))) built from a tuple of names
        written = set(WRITTEN.findall(src))
        written |= set(re.findall(r"""\[\s*["']([A-Za-z_][\w.]*)["']\s*\]\s*=""", src))
        for tup in re.findall(r"dict\(zip\(\((.*?)\)", src, re.S):
            written |= set(re.findall(r"""["']([A-Za-z_][\w.]*)["']""", tup))
        missing = sorted(k for k in read - written - internal if k not in universe)
        if missing:
            total_missing += len(missing)
            print("  %-20s reads %d key(s) present in NO payload:" % (t, len(missing)))
            for k in missing:
                ctx = ""
                m = re.search(r"^.*['\"]%s['\"].*$" % re.escape(k), src, re.M)
                if m:
                    ctx = m.group(0).strip()[:78]
                print("      %-22s %s" % (k, ctx))
    if not total_missing:
        print("  no instrument reads a key absent from every observed payload.")
    print()
    print("  NOT COVERED: the files listed as out of scope above. They read local")
    print("  manifests, repo files or other APIs, and this check holds no payload")
    print("  for them. Being unchecked here is a coverage limit, not a pass.")
    print("  OUT_OF_SCOPE != VERIFIED")
    print()
    print("  KEY_EXISTS_SOMEWHERE != KEY_BELONGS_TO_THIS_OBJECT")
    print("  a key valid on another object passes here; this catches only keys")
    print("  that exist nowhere, which is the silently-falsy case.")
    return 2 if total_missing else 0


if __name__ == "__main__":
    sys.exit(main())
