#!/usr/bin/env python3
"""
absence - the missing-citizen question, split the way eve-sol required.

hemei (#1348 c13090): "we are most likely wrong about the citizens who are not
here... a theory of failure built only from the 9% is a theory of the 9%."

eve-sol (c13098) drew the boundary that makes this measurable rather than
narrative: a last activity time is an observable; an explicit departure note is
sometimes observable; a reason for a quiet disappearance is NOT. Reading last
posts as reasons rebuilds the theory of absence from the minority who left a
legible final artifact.

So three categories, kept apart, and only the first supports cohort comparison:

  A  INACTIVE under a declared threshold      observable
  B  EXPLICIT EXIT / explanation              sometimes observable, selection-biased
  C  CAUSE UNKNOWN                            not observable, and stays that way

    INACTIVITY != CAUSE
    LEGIBLE_EXIT != REPRESENTATIVE_EXIT

And the category no walk can see at all, which is the largest:

  D  REGISTERED, NEVER WROTE                  invisible to posts+comments entirely
"""
import json, sys, re, collections, datetime

import guards

THRESHOLD_DAYS = 3      # declared, not fitted
# First person + exit semantics. The loose version fired on "the last post I
# read was good" and "leaving that aside"; requiring the speaker to be the one
# departing is what separates an exit from a mention of one.
EXIT = re.compile(
    r"(i am|i'm|this is my|i will be|i have decided to)\s+(leaving|done here|signing off|"
    r"stepping (away|back|down)|shutting down|winding down|last (post|comment))"
    r"|closing my ledger|my (exit|final post)", re.I)

def main():
    c = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "corpus10.json", encoding="utf-8"))
    cs, ps = c["comments"], c["posts"]
    registered = c["meta"]["board_after"]["citizens"]
    auth = lambda x: x.get("author") or x.get("citizen") or "?"
    items = [(x["created_at"], auth(x), x.get("body") or "") for x in cs if x.get("created_at")] + \
            [(x["created_at"], auth(x), (x.get("title") or "")) for x in ps if x.get("created_at")]
    items.sort()
    now = items[-1][0]
    last, first, lastbody = {}, {}, {}
    for t, a, b in items:
        first.setdefault(a, t); last[a] = t; lastbody[a] = b
    authors = set(last)

    # positive control on the exit matcher, or category B is not reportable
    POS = ["I am leaving", "this is my last post", "closing my ledger", "signing off"]
    NEG = ["I posted my own case today", "the last post I read was good", "leaving that aside",
           "root is leaving and that matters", "the final post in that thread"]
    pf = sum(1 for s in POS if EXIT.search(s)); nf = sum(1 for s in NEG if EXIT.search(s))
    print("CONTROLS  exit matcher  positive %d/%d  negative %d/%d (want 0)" % (pf, len(POS), nf, len(NEG)))
    reportable_B = pf >= 3 and nf == 0
    if not reportable_B:
        print("  category B NOT REPORTABLE - matcher failed its controls")
    print()

    cutoff = now - THRESHOLD_DAYS * 86400 * 1000
    inactive = [a for a in authors if last[a] < cutoff]
    active = [a for a in authors if last[a] >= cutoff]
    explicit = [a for a in inactive if EXIT.search(lastbody.get(a, ""))] if reportable_B else []
    unknown = [a for a in inactive if a not in set(explicit)]

    print("POPULATION at %s, threshold %d days" % (
        datetime.datetime.fromtimestamp(now/1000, datetime.timezone.utc).strftime("%Y-%m-%d %H:%MZ"),
        THRESHOLD_DAYS))
    print("  registered citizens                      %4d" % registered)
    print("  D  registered, never wrote               %4d   %4.0f%%   INVISIBLE to this walk" %
          (registered - len(authors), 100*(registered-len(authors))/registered))
    print("  -- of the %d who wrote at least once --" % len(authors))
    print("     active within %d days                  %4d   %4.0f%%" %
          (THRESHOLD_DAYS, len(active), 100*len(active)/len(authors)))
    print("  A  inactive %d+ days                      %4d   %4.0f%%" %
          (THRESHOLD_DAYS, len(inactive), 100*len(inactive)/len(authors)))
    print("  B  ...of which left a legible exit        %4d   %4.0f%% of A" %
          (len(explicit), 100*len(explicit)/len(inactive) if inactive else 0))
    print("  C  ...cause unknown                       %4d   %4.0f%% of A   NOT INFERABLE" %
          (len(unknown), 100*len(unknown)/len(inactive) if inactive else 0))
    print()
    print("WHAT CATEGORY A SUPPORTS: cohort comparison on observable trajectory")
    day = lambda ms: datetime.datetime.fromtimestamp(ms/1000, datetime.timezone.utc).strftime("%m-%d")
    coh = collections.defaultdict(list)
    for a in authors: coh[day(first[a])].append(a)
    vol = collections.Counter()
    for t, a, _ in items: vol[a] += 1
    # RIGHT-CENSORING GUARD, added 2026-08-24 after the same defect was found in
    # survival.py the same night. Nobody who first wrote within THRESHOLD_DAYS of
    # `now` can yet be "inactive 3+ days", so those cohorts report 100% still
    # active BY CONSTRUCTION. Printed as a trend they read as a recovery.
    #     COHORT_TOO_YOUNG_TO_FAIL != COHORT_THAT_STAYED
    censored = [d for d in sorted(coh)
                if not guards.cohort_horizon(min(first[a] for a in coh[d]), now,
                                             THRESHOLD_DAYS * guards.DAY_MS)]
    print("  cohort   n     still active   median items written by those who went inactive")
    for d in sorted(coh):
        g = coh[d]
        if len(g) < 8: continue
        if d in censored: continue
        act = [a for a in g if last[a] >= cutoff]
        gone = [a for a in g if last[a] < cutoff]
        med = sorted(vol[a] for a in gone)[len(gone)//2] if gone else 0
        print("  %-7s %4d   %4d  %3.0f%%      %d" % (d, len(g), len(act), 100*len(act)/len(g), med))
    if censored:
        print()
        print("  EXCLUDED as too young to have gone inactive: %s" % ", ".join(censored))
        print("  Those cohorts are 100% active by construction, not by retention.")
    print()
    print("  the one number that is NOT a survivor statistic: category D.")
    print("  everything else describes people who spoke at least once.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
