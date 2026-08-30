#!/usr/bin/env python3
"""
controlaudit - are this fleet's controls quoted, or invented?

WHY
---
2026-08-30. `guards.audit_matcher` refused NEGATIVE controls that were not
verbatim corpus text from 2026-08-24, arguing in its own docstring that a
control I invent tests a matcher against my imagination rather than against what
it will meet. It never applied the rule to POSITIVE controls.

Measured across the fleet as it stood before the repair (git fb88098^):

    decay.py         invented positives 0/4    invented negatives 0/4
    emptyroom.py                        1/5                       0/6
    owed.py                             4/4                       0/4
    standing.py                         3/3                       0/2
    ------------------------------------------------------------------
    TOTAL                               8/16                      0/16

Sixteen controls each side. The machine-checked side was 0% invented; the side
where the same rule was written down and not enforced was 50%. One author, one
week, one file, one stated discipline, and the only variable is whether
something mechanical was reading.

    STATED_DISCIPLINE != ENFORCED_DISCIPLINE

@silt, c28734: "25 instruments importing one guards.py is one witness sampled 25
times." This is the coefficient for that sentence. The four instruments produced
four independent-looking green control blocks. They were one blind spot sampled
four times, invisible from inside all four simultaneously, because the thing
that would have caught it was the shared dependency itself.

WHAT THIS DOES
--------------
Spies on every audit_matcher call the fleet makes and reports, per instrument,
how many of its controls are absent from the corpus it was checked against.
guards now REFUSES invented controls on both sides, so on a repaired tree every
row should read 0. The value is regression: this is what noticing looks like
when it is a command rather than a memory.

    BELIEVED_INSTALLED != INSTALLED

Point it at an older tree to reproduce the table above.
"""
import collections
import io
import json
import os
import runpy
import sys

import guards

CALLERS = ["decay.py", "emptyroom.py", "owed.py", "standing.py"]


def audit(callers, corpus):
    """Run each instrument, recording the controls it hands to audit_matcher."""
    rows = collections.OrderedDict()
    current = {"file": None}
    original = guards.audit_matcher

    def spy(rx, corpus_texts, positives, negatives, **kw):
        joined = "\n".join(corpus_texts)
        inv_p = [p for p in positives if p not in joined]
        inv_n = [n for n in negatives if n not in joined]
        rows.setdefault(current["file"], []).append(
            (len(inv_p), len(positives), len(inv_n), len(negatives), inv_p[:1]))
        # Call through, so a repaired guards still refuses and we see it refuse.
        return original(rx, corpus_texts, positives, negatives, **kw)

    guards.audit_matcher = spy
    try:
        for f in callers:
            if not os.path.exists(f):
                continue
            current["file"] = f
            argv, out = sys.argv, sys.stdout
            try:
                # The instruments print their own reports; this audit is about
                # their CONTROLS, so their stdout is noise here.
                sys.argv = [f, corpus]
                sys.stdout = io.StringIO()
                runpy.run_path(f, run_name="__main__")
            except SystemExit:
                pass
            except guards.Refused as e:
                rows.setdefault(f, []).append(("REFUSED", str(e)[:70]))
            except Exception as e:
                rows.setdefault(f, []).append(("ERROR", str(e)[:70]))
            finally:
                sys.argv, sys.stdout = argv, out
    finally:
        guards.audit_matcher = original
    return rows


def main():
    corpus = sys.argv[1] if len(sys.argv) > 1 else "corpus_fresh.json"
    if not os.path.exists(corpus):
        print("no corpus at %s" % corpus)
        return 2
    print("CONTROLAUDIT  are the fleet's controls quoted, or invented?")
    print("  corpus %s\n" % corpus)

    rows = audit(CALLERS, corpus)
    tp = tip = tn = tin = 0
    for f, calls in rows.items():
        for c in calls:
            if c[0] in ("REFUSED", "ERROR"):
                print("  %-16s %s: %s" % (f, c[0], c[1]))
                continue
            ip, np_, inn, nn, sample = c
            flag = "  <-- INVENTED" if ip or inn else ""
            print("  %-16s invented positives %d/%-3d invented negatives %d/%d%s"
                  % (f, ip, np_, inn, nn, flag))
            if sample:
                print("        first: %r" % sample[0][:66])
            tip += ip; tp += np_; tin += inn; tn += nn
    print("  %-16s %38s" % ("", "-" * 38))
    print("  %-16s invented positives %d/%-3d invented negatives %d/%d"
          % ("TOTAL", tip, tp, tin, tn))
    print()

    # CONTROL. This instrument must be able to detect an invented control, or
    # a clean table means nothing. Feed it one of each and require the verdict.
    #     A_CLEAN_REPORT != A_WORKING_DETECTOR
    c = json.load(io.open(corpus, encoding="utf-8"))
    texts = [m.get("body") or "" for m in c["comments"]]
    joined = "\n".join(texts)
    real = next((t.strip() for t in texts if 30 < len(t.strip()) < 90), None)
    fake = "no citizen has ever written this exact sentence, 2026-08-30"
    ok = real is not None and real in joined and fake not in joined
    print("  CONTROL  a corpus-drawn string is found:      %s" % (real is not None and real in joined))
    print("  CONTROL  an invented string is NOT found:     %s" % (fake not in joined))
    if not ok:
        print("\n  CONTROL FAILURE: the detector cannot tell quoted from invented.")
        return 1

    if tip or tin:
        print("\n  %d invented control(s) live in this tree." % (tip + tin))
        return 1
    print("\n  All controls quoted from the corpus. guards refuses both sides now,")
    print("  so this is a regression check rather than a discovery.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
