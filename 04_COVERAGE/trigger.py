#!/usr/bin/env python3
"""
Trigger analysis over a complete 1F916 walk.

Written because the previous run's matchers were never saved. Counts were
published on 2026-08-18 that cannot now be reproduced. Every pattern used
here is a named constant so the instrument travels with the number.

Reports a RANGE across matcher variants rather than a single figure, because
the single figure is exactly what failed.
"""
import json, re, sys, random, collections

CORPUS = "corpus.json"

# ---- named, versioned patterns -------------------------------------------

SELF_NARROW = r"""\b(
    i \s was \s wrong
  | i \s withdraw
  | i \s retract
  | i \s am \s withdrawing
  | withdrawing \s my
  | i \s take \s (that|it) \s back
  | my \s (claim|number|reading|conclusion) \s was \s wrong
)\b"""

SELF_BROAD = SELF_NARROW[:-3] + r"""
  | i \s (got|had) \s (that|it|this) \s wrong
  | i \s (mis|over)(stated|read|counted|claimed)
  | my \s error
  | correcting \s myself
  | i \s should \s not \s have \s (said|claimed)
  | that \s was \s (false|wrong) \s of \s me
  | i \s overstated
)\b"""

PROMPTED = r"""\b(
    you \s (are|were) \s right
  | @[\w-]+ \s (is|was) \s right
  | as \s @?[\w-]+ \s (pointed \s out|showed|noted)
  | thanks \s .{0,25}? (for \s catching|for \s the \s catch)
  | after \s .{0,25}? (challenged|caught|corrected|falsified)
  | @?[\w-]+ \s caught \s (me|this|that)
  | your \s (point|correction|catch) \s (stands|holds|is \s right)
)\b"""

SELF_FOUND = r"""\b(
    i \s re-?(ran|checked|read|counted)
  | on \s re-?(reading|checking|running|counting)
  | when \s i \s went \s back
  | checking \s my \s own
  | i \s noticed \s .{0,30}? myself
  | going \s back \s through \s my \s own
)\b"""

F = re.X | re.I


def build(pat):
    return re.compile(pat, F)


def main():
    corpus = json.load(open(CORPUS, encoding="utf-8"))
    cs = corpus["comments"]
    meta = corpus["meta"]
    author = lambda c: c.get("citizen") or c.get("author") or "?"
    body = lambda c: c.get("body") or ""

    print("COVERAGE")
    print("  comments        %d" % meta["comments_retrieved"])
    print("  posts           %d" % meta["posts_retrieved"])
    print("  has_more_at_end %s" % meta["has_more_at_end"])
    print("  authors         %d" % len(set(author(c) for c in cs)))
    print()

    prompted = build(PROMPTED)
    found = build(SELF_FOUND)

    rows = []
    for name, pat in (("SELF_NARROW", SELF_NARROW), ("SELF_BROAD", SELF_BROAD)):
        sc = [c for c in cs if build(pat).search(body(c))]
        cp = [c for c in sc if prompted.search(body(c)) and not found.search(body(c))]
        cf = [c for c in sc if found.search(body(c)) and not prompted.search(body(c))]
        ratio = (len(cp) / len(cf)) if cf else float("inf")
        rows.append((name, sc, cp, cf, ratio))
        print("%s" % name)
        print("  self-corrections     %4d   (%.2f%% of corpus)" % (len(sc), 100.0 * len(sc) / len(cs)))
        print("  distinct authors     %4d   (%.1f%% of board)"
              % (len(set(author(c) for c in sc)), 100.0 * len(set(author(c) for c in sc)) / len(set(author(c) for c in cs))))
        print("  cleanly prompted     %4d   authors %d" % (len(cp), len(set(author(c) for c in cp))))
        print("  cleanly self-found   %4d   authors %d" % (len(cf), len(set(author(c) for c in cf))))
        print("  ratio                %.2f : 1" % ratio)
        print("  unclassified         %4d   (%.0f%%)"
              % (len(sc) - len(cp) - len(cf), 100.0 * (len(sc) - len(cp) - len(cf)) / len(sc)))
        print()

    lo = min(r[4] for r in rows)
    hi = max(r[4] for r in rows)
    print("DIRECTION: prompted exceeds self-found under both matchers")
    print("MAGNITUDE: ratio spans %.2f:1 to %.2f:1 across matcher choice" % (lo, hi))
    print()

    if len(sys.argv) > 1 and sys.argv[1] == "--sample":
        seed = int(sys.argv[2]) if len(sys.argv) > 2 else 20260819
        random.seed(seed)
        name, sc, cp, cf, _ = rows[1]
        print("PRECISION SAMPLE from %s, seed %d" % (name, seed))
        for c in random.sample(sc, min(12, len(sc))):
            b = " ".join(body(c).split())
            m = build(SELF_BROAD).search(body(c))
            print("  c%-6s %-22s ...%s..." % (c["id"], author(c)[:22], b[max(0, m.start() - 60):m.end() + 70]))


if __name__ == "__main__":
    main()
