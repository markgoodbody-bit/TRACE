#!/usr/bin/env python3
"""
leakscan - what would leak if this directory were published.

Reports COUNTS and PATHS only. Never prints a matched value: the whole point is
to describe an exposure without reproducing it.

Every pattern is positive-controlled against planted text before any real result
is reported. Five matchers were written for this scan on 2026-08-19 and one of
them (local_user_path) was DEAD - a non-raw Python string turned C:\\+Users\\+
into the regex C:\+Users\+, an escaped literal plus. It reported a clean result
for a directory it could not see into. The controls below exist because of it.
"""
import os, re, sys, collections

PATTERNS = {
 "api_key_or_token": re.compile(r'"(?:api_?key|apikey|token|secret|password|authorization|bearer)"\s*:\s*"[^"]{8,}"', re.I),
 "bearer_header":    re.compile(r'Bearer\s+[A-Za-z0-9._\-]{20,}'),
 # separator class built from chr(92): a literal backslash here is eaten by
 # the shell heredoc that writes this file, which is how this matcher died
 # the first time. It reported a clean scan it could not have made.
 "local_user_path":  re.compile("C:_SEP_Users_SEP_[A-Za-z0-9_.-]+"
                                .replace("_SEP_", "[" + chr(92)*2 + "/]{1,2}"), re.I),
 "email":            re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'),
 "personal_name":    re.compile(r'\bMark\s+[A-Z][a-z]{3,}\b'),
}

CONTROLS = {
 "api_key_or_token": '{"api_key":"sk-abcdef1234567890abcdef"}',
 "bearer_header":    'Authorization: Bearer abcdefghijklmnopqrstuvwxyz123456',
 "local_user_path":  'path = "C:' + chr(92) + 'Users' + chr(92) + 'someone' + chr(92) + 'Docs"',
 "email":            'contact a.person@example.com now',
 "personal_name":    'signed by Mark Exampleton today',
}

TEXT_EXT = {'.json','.jsonl','.ps1','.txt','.md','.py','.psm1','.psd1','.xml','.yml','.yaml'}
MAXBYTES = 25_000_000


def controls_pass():
    dead = [n for n, rx in PATTERNS.items() if not rx.search(CONTROLS[n])]
    print("POSITIVE CONTROLS  %d/%d matchers fire" % (len(PATTERNS) - len(dead), len(PATTERNS)))
    if dead:
        print("  DEAD: %s" % ", ".join(dead))
        print("  No result is reportable. A dead matcher returns a clean scan.")
    return not dead


def scan(root, areas):
    tally = collections.Counter(); per_file = collections.Counter(); scanned = 0
    for area in areas:
        base = os.path.join(root, area) if area != "." else root
        if area == ".":
            it = [(root, [], [f for f in os.listdir(root)
                              if os.path.isfile(os.path.join(root, f))])]
        else:
            it = os.walk(base)
        for dp, _, fns in it:
            for fn in fns:
                p = os.path.join(dp, fn)
                if not os.path.isfile(p): continue
                if os.path.splitext(fn)[1].lower() not in TEXT_EXT: continue
                try:
                    if os.path.getsize(p) > MAXBYTES: continue
                    t = open(p, encoding="utf-8", errors="replace").read()
                except Exception:
                    continue
                scanned += 1
                for name, rx in PATTERNS.items():
                    n = len(rx.findall(t))
                    if n:
                        tally[(name, area)] += n
                        per_file[(name, os.path.relpath(p, root))] += n
    return tally, per_file, scanned


def main():
    root = sys.argv[1]
    areas = sys.argv[2:] or ["."]
    if not controls_pass():
        return 2
    tally, per_file, scanned = scan(root, areas)
    print("\nSCANNED  %d text files across: %s\n" % (scanned, ", ".join(areas)))
    if not tally:
        print("  no pattern matched in any scanned area")
    else:
        print("  %-18s %-14s %s" % ("PATTERN", "AREA", "OCCURRENCES"))
        for (name, area), n in sorted(tally.items(), key=lambda kv: -kv[1]):
            print("  %-18s %-14s %d" % (name, area, n))
        print("\n  FILES (values never printed)")
        for (name, p), n in per_file.most_common(20):
            print("    %-18s %-56s %d" % (name, p[:56], n))
    print("\nKNOWN HOLE: pattern-based. A secret in a shape not listed here is")
    print("not detected. Clean is 'nothing matched', never 'nothing is there'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
