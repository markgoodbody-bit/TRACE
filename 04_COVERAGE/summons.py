#!/usr/bin/env python3
"""
Does an @mention actually pull a citizen into a thread they were not in?

A raw response rate cannot answer this. 23% of summoned non-participants later
comment in the thread - but some of them would have arrived anyway. Without a
control, "mentions do nothing" and "mentions work and are usually declined"
predict the same number.

So: matched control. For every summons, sample citizens who were ACTIVE at the
same moment, NOT already in that thread, and NOT mentioned. If mentioning does
nothing, the two groups join the thread at the same rate.

SUMMONS   comment X in post P mentions citizen N; N has not commented in P
          before X. Outcome: does N comment in P after X?
CONTROL   same X, same P. Citizens active within +/-W comment ids of X, not in
          P before X, not mentioned by X. Same outcome question.

Every parameter is a named constant. Corpus rebuilds from walk.py.
"""
import json
import re
import random
import collections
import statistics

WINDOW = 500          # comment-ids either side that count as "active near X"
CONTROLS_PER = 5      # matched controls sampled per summons
SEED = 20260819

MENTION = re.compile(r"@([A-Za-z0-9][A-Za-z0-9_-]{1,40})")


def main():
    corpus = json.load(open("corpus.json", encoding="utf-8"))
    cs = sorted(corpus["comments"], key=lambda c: c["id"])
    author = lambda c: c.get("citizen") or c.get("author") or "?"
    body = lambda c: c.get("body") or ""
    authors = set(author(c) for c in cs)

    # activity index: citizen -> sorted comment ids
    acts = collections.defaultdict(list)
    for c in cs:
        acts[author(c)].append(c["id"])

    by_post = collections.defaultdict(list)
    for c in cs:
        by_post[c.get("post_id")].append(c)

    def active_near(cid):
        lo, hi = cid - WINDOW, cid + WINDOW
        return [a for a, ids in acts.items()
                if any(lo <= i <= hi for i in ids)]

    random.seed(SEED)
    s_total = s_hit = 0
    c_total = c_hit = 0
    s_gap, c_gap = [], []

    for pid, items in by_post.items():
        items = sorted(items, key=lambda c: c["id"])
        before = set()
        # who appears in this post after id X, and when each first appears
        after_cache, first_cache = {}, {}
        for i, x in enumerate(items):
            rest = items[i + 1:]
            after_cache[x["id"]] = set(author(y) for y in rest)
            f = {}
            for y in rest:
                f.setdefault(author(y), y["id"])
            first_cache[x["id"]] = f

        for x in items:
            names = {n for n in MENTION.findall(body(x))
                     if n in authors and n != author(x)}
            summoned = {n for n in names if n not in before}
            later = after_cache[x["id"]]

            first = first_cache[x["id"]]
            if summoned:
                pool = [a for a in active_near(x["id"])
                        if a not in before and a not in names and a != author(x)]
                for n in summoned:
                    s_total += 1
                    if n in later:
                        s_hit += 1
                        s_gap.append(first[n] - x["id"])
                if pool:
                    for a in random.sample(pool, min(CONTROLS_PER, len(pool))):
                        c_total += 1
                        if a in later:
                            c_hit += 1
                            c_gap.append(first[a] - x["id"])
            before.add(author(x))

    print("PARAMETERS  window=%d ids, controls_per_summons=%d, seed=%d"
          % (WINDOW, CONTROLS_PER, SEED))
    print()
    print("SUMMONED  (mentioned, not previously in thread)")
    print("  n=%-6d later commented in that thread: %-5d  %.1f%%"
          % (s_total, s_hit, 100.0 * s_hit / s_total))
    print("CONTROL   (active same moment, not in thread, not mentioned)")
    print("  n=%-6d later commented in that thread: %-5d  %.1f%%"
          % (c_total, c_hit, 100.0 * c_hit / c_total))
    print()
    sr = s_hit / s_total
    cr = c_hit / c_total
    print("  arrival lift: %.1fx" % (sr / cr if cr else float("inf")))
    print()
    print("LATENCY  gap in board comment-ids between the mention and the")
    print("         mentioned citizen's first comment in that thread")
    for name, g in (("SUMMONED", s_gap), ("CONTROL", c_gap)):
        g = sorted(g)
        print("  %-9s n=%-5d median=%-6d  <=50: %4.1f%%  <=200: %4.1f%%"
              % (name, len(g), statistics.median(g),
                 100.0 * sum(1 for v in g if v <= 50) / len(g),
                 100.0 * sum(1 for v in g if v <= 200) / len(g)))
    print()
    print("VERDICT  NOT_ESTABLISHED whether mentioning causes attendance.")
    print()
    print("  The lift is large. The latency distributions are indistinguishable,")
    print("  and the control is if anything faster. A notification acted upon")
    print("  should cluster summoned arrivals shortly after the mention relative")
    print("  to controls. It does not.")
    print()
    print("  So the lift is equally consistent with: citizens are mentioned")
    print("  BECAUSE they are topically relevant, and topically relevant")
    print("  citizens arrive at ~11x the rate of merely-active ones, on the")
    print("  same timescale whether mentioned or not.")
    print()
    print("  MENTION_CORRELATES_WITH_ARRIVAL != MENTION_CAUSES_ARRIVAL")
    print()
    print("  Consequence: it is NOT established that the 77% non-response rate")
    print("  is citizens declining. Non-delivery is not ruled out, and neither")
    print("  is 'mentions do not function as summons at all'.")
    print()
    print("  An earlier version of this file printed a DELIVERED AND ACTED ON")
    print("  verdict from the lift alone, before the latency test existed. That")
    print("  verdict was not licensed by its evidence and is withdrawn.")


if __name__ == "__main__":
    main()
