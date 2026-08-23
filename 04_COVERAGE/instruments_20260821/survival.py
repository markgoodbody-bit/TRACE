#!/usr/bin/env python3
"""
survival - is 1F916's participation growing, flat, or dying?

Measures what a posts+comments walk can see, and states plainly what it cannot.

    SURVIVOR_BIAS: a citizen who registered and never wrote is invisible here.
    190 of 730 registered citizens have never authored anything (hemei, #1348).
    Every rate below is therefore a rate among people who spoke at least once.

Four questions, because "participation" is not one number:
  1. volume      comments + posts per day
  2. breadth     distinct authors active per day
  3. inflow      authors appearing for the first time per day
  4. concentration  share of daily volume from that day's top 10 authors
  5. retention   of authors first seen on day D, what share are still active 3+ days on
"""
import json, sys, collections, datetime, statistics

def day(ms): return datetime.datetime.fromtimestamp(ms/1000, datetime.timezone.utc).strftime("%m-%d")

def main():
    c = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "corpus10.json", encoding="utf-8"))
    cs, ps = c["comments"], c["posts"]
    auth = lambda x: x.get("author") or x.get("citizen") or "?"
    items = [(day(x["created_at"]), auth(x), "c") for x in cs if x.get("created_at")] + \
            [(day(x["created_at"]), auth(x), "p") for x in ps if x.get("created_at")]
    items.sort()
    days = sorted(set(d for d, _, _ in items))

    # RIGHT-CENSORING GUARD, added 2026-08-23 after this instrument published its
    # own partial trailing bucket as a completed day. A walk ends mid-day; the last
    # bucket is a fraction of a day read as a whole one. PARTIAL_BUCKET != DAILY_RATE.
    end_ms = max(x["created_at"] for x in cs + ps if x.get("created_at"))
    end_dt = datetime.datetime.fromtimestamp(end_ms / 1000, datetime.timezone.utc)
    def complete(d):
        dt = datetime.datetime.strptime("%d-%s" % (end_dt.year, d), "%Y-%m-%d")
        return end_dt >= dt.replace(tzinfo=datetime.timezone.utc) + datetime.timedelta(days=1)
    partial = [d for d in days if not complete(d)]

    vol   = collections.Counter(d for d, _, _ in items)
    posts = collections.Counter(d for d, _, k in items if k == "p")
    byday = collections.defaultdict(collections.Counter)
    for d, a, _ in items: byday[d][a] += 1
    first = {}
    for d, a, _ in items: first.setdefault(a, d)
    newby = collections.Counter(first.values())
    lastseen = {}
    for d, a, _ in items: lastseen[a] = d

    print("BOARD LIFE  %s -> %s   %d days   %d items   %d authors"
          % (days[0], days[-1], len(days), len(items), len(first)))
    print("SURVIVOR BIAS: citizens who never wrote are invisible to this instrument.")
    print()
    print("  day     items   posts   active   new     top10 share   new/active")
    for d in days:
        act = len(byday[d])
        top10 = sum(n for _, n in byday[d].most_common(10))
        share = 100.0 * top10 / vol[d] if vol[d] else 0
        print("  %-7s %5d   %5d   %5d   %4d      %4.0f%%        %4.0f%%%s"
              % (d, vol[d], posts[d], act, newby.get(d, 0), share,
                 100.0*newby.get(d,0)/act if act else 0,
                 "   <-- PARTIAL, NOT A RATE" if d in partial else ""))

    if partial:
        print()
        print("PARTIAL DAY: corpus ends %s, so %s is a fraction of a day."
              % (end_dt.strftime("%m-%d %H:%MZ"), ", ".join(partial)))
        print("  Do not read the last row as a daily rate or as the endpoint of a trend.")
        print("  On 2026-08-21 this instrument reported 4 new authors and 37% concentration")
        print("  from a bucket holding 18 of 24 hours. The completed day was 71 and 24%.")

    print()
    print("RETENTION  of authors first seen on day D, share still writing 3+ days later")
    idx = {d: i for i, d in enumerate(days)}
    horizon = max(idx[d] for d in days if complete(d))
    for d in days:
        if idx[d] + 3 > horizon: continue   # cohort not yet observable for 3 full days
        cohort = [a for a, f in first.items() if f == d]
        if len(cohort) < 5: continue
        alive = [a for a in cohort if idx[lastseen[a]] - idx[d] >= 3]
        print("  %-7s cohort %4d   still active 3d+ %4d   %4.0f%%"
              % (d, len(cohort), len(alive), 100.0*len(alive)/len(cohort)))
    return 0

if __name__ == "__main__":
    sys.exit(main())
