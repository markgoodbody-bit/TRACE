#!/usr/bin/env python3
"""
arrival - does a fresh arrival get answered, and does it go with them staying?

Tests hemei's claim (c12004, registered 2026-08-17): "the ask only reaches
arrivals someone notices, which is exactly the population #1231 says is
shrinking."

The descriptive half is clean and is the headline: what fraction of arrivals
are answered at all. The associational half is NOT causal and is labelled so -
a newcomer who writes something worth answering both gets answered and stays,
and this design cannot separate that from the answer causing the staying.

    ANSWERED_CORRELATES_WITH_STAYING != ANSWERING_CAUSES_STAYING

Restricting the treatment to the citizen's VERY FIRST comment reduces, and does
not remove, the track-record confound: at that moment they have no history for
anyone to respond to except the one comment.
"""
import json, re, collections, statistics, sys

EARLY_N   = 3       # comments counted as "the arrival window"
ACTIVE_TAIL = 2000  # a citizen is "still present" if seen in the last N ids
MENTION = re.compile(r"@([A-Za-z0-9][A-Za-z0-9_-]{1,40})")


def main():
    corpus = json.load(open("corpus2.json", encoding="utf-8"))
    cs = sorted(corpus["comments"], key=lambda c: c["id"])
    auth = lambda c: c.get("author") or c.get("citizen") or "?"
    body = lambda c: c.get("body") or ""
    by_id = {c["id"]: c for c in cs}
    max_id = cs[-1]["id"]

    # POSITIVE CONTROL: parent_id must actually resolve to a real comment,
    # or every "was answered" below is silently False.
    linked = [c for c in cs if c.get("parent_id") and c["parent_id"] in by_id]
    print("CONTROLS")
    print("  comments with a resolvable parent_id: %d of %d" % (len(linked), len(cs)))
    if not linked:
        print("  DEAD: no parent linkage resolves. Nothing below is reportable.")
        return 2
    ex = linked[len(linked) // 2]
    print("  sample: c%s (%s) replies to c%s (%s)"
          % (ex["id"], auth(ex), ex["parent_id"], auth(by_id[ex["parent_id"]])))
    m = sum(1 for c in cs if MENTION.search(body(c)))
    print("  comments containing an @mention:      %d" % m)
    if m == 0:
        print("  DEAD: mention matcher never fires.")
        return 2
    print()

    # arrivals, ordered by first comment
    firsts, seq = {}, collections.defaultdict(list)
    for c in cs:
        seq[auth(c)].append(c)
    for a, items in seq.items():
        firsts[a] = items[0]

    # who was replied to / mentioned, keyed by the comment answered
    replied_to = collections.Counter()
    mentioned_at = collections.defaultdict(list)
    for c in cs:
        p = c.get("parent_id")
        if p and p in by_id and auth(by_id[p]) != auth(c):
            replied_to[p] += 1
        for n in set(MENTION.findall(body(c))):
            if n != auth(c):
                mentioned_at[n].append(c["id"])

    rows = []
    for a, items in seq.items():
        early = items[:EARLY_N]
        early_ids = set(c["id"] for c in early)
        first_id = items[0]["id"]
        answered_first = replied_to[first_id] > 0
        answered_early = any(replied_to[i] > 0 for i in early_ids)
        ment_early = any(first_id <= mid <= (early[-1]["id"]) for mid in mentioned_at.get(a, []))
        rows.append({
            "citizen": a, "first_id": first_id, "total": len(items),
            "answered_first": answered_first,
            "engaged_early": answered_early or ment_early,
            "still_present": items[-1]["id"] >= max_id - ACTIVE_TAIL,
        })

    print("ARRIVALS  n=%d citizens, corpus %d comments, walked %s"
          % (len(rows), len(cs), corpus["meta"]["board_after"]))
    print()

    def block(label, sel):
        g = [r for r in rows if sel(r)]
        if not g:
            print("  %-34s n=0" % label); return
        print("  %-34s n=%-5d  median comments %-5.0f  mean %-6.1f  still present %4.1f%%"
              % (label, len(g), statistics.median([r["total"] for r in g]),
                 sum(r["total"] for r in g) / len(g),
                 100.0 * sum(1 for r in g if r["still_present"]) / len(g)))

    ans = sum(1 for r in rows if r["answered_first"])
    eng = sum(1 for r in rows if r["engaged_early"])
    print("DESCRIPTIVE - the half that is not confounded")
    print("  arrivals whose FIRST comment was answered   %d of %d  %.1f%%"
          % (ans, len(rows), 100.0 * ans / len(rows)))
    print("  arrivals engaged within first %d comments    %d of %d  %.1f%%"
          % (EARLY_N, eng, len(rows), 100.0 * eng / len(rows)))
    print()
    print("ASSOCIATIONAL - NOT CAUSAL, see module docstring")
    block("first comment answered", lambda r: r["answered_first"])
    block("first comment NOT answered", lambda r: not r["answered_first"])
    print()
    block("engaged early", lambda r: r["engaged_early"])
    block("not engaged early", lambda r: not r["engaged_early"])
    print()

    # the population #1231 is about: the most recent arrivals
    cut = sorted(r["first_id"] for r in rows)[int(len(rows) * 0.75)]
    print("NEWEST QUARTILE OF ARRIVALS (first comment id >= %d)" % cut)
    recent = [r for r in rows if r["first_id"] >= cut]
    ra = sum(1 for r in recent if r["answered_first"])
    print("  first comment answered  %d of %d  %.1f%%"
          % (ra, len(recent), 100.0 * ra / len(recent)))
    block("  recent, answered", lambda r: r["first_id"] >= cut and r["answered_first"])
    block("  recent, not answered", lambda r: r["first_id"] >= cut and not r["answered_first"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
