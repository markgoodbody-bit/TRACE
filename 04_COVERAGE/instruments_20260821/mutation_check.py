#!/usr/bin/env python3
"""
mutation_check - does a guard actually CONTROL the instrument that imports it?

WHY, AND WHOSE IDEA
-------------------
guards.py --adoption greps for `import guards` and reports adoption. @zola
(c19530, c21606) pointed out that this is the weaker half of the very
distinction it exists to report:

    "A repository search can establish that a capability exists; only an
     exercised path, or a coverage check that fails when the import is removed,
     can establish that the deployed instrument controls anything. The second
     mutant is the cheap receipt."

    CAPABILITY_IN_THE_REPOSITORY != CONTROL_IN_THE_INSTRUMENT
    IMPORT_PRESENT != GUARD_EXERCISED

An instrument can import guards and never call it, call it in a dead branch, or
call it and discard the result. The adoption scan scores all three as adopted.
It scored my own directory 6 of 6 while proving nothing about any of them.

THE RECEIPT
-----------
Replace a guard with a permissive mutant that cannot refuse or censor anything,
re-run every instrument against it, and diff.

    output CHANGES   -> the guard is load-bearing in that instrument
    output IDENTICAL -> the import is present and the guard controls nothing

TWO DEFECTS THIS FILE HAD ON ITS FIRST RUN, BOTH ITS OWN SUBJECT MATTER
-----------------------------------------------------------------------
1. The mutant was written to a temp dir and put on PYTHONPATH, while the
   instrument stayed in its own directory. Python places the SCRIPT'S directory
   at sys.path[0], ahead of PYTHONPATH, so the real guards.py shadowed every
   mutant. The check printed a full clean-looking table while mutating nothing.

       MUTANT_WRITTEN != MUTANT_LOADED

   Instruments are now copied beside the mutated guards.py and run from there.

2. No determinism control. burst.py runs a permutation test and its output
   varies run to run, so it scored EVERY mutant as killed -- including guards it
   does not import. A nondeterministic instrument reports a killed mutant for
   free.

       UNSTABLE_OUTPUT != MUTANT_KILLED

   Every instrument is now run twice against unmutated guards first; any that
   disagrees with itself is excluded from scoring and named.

The giveaway was that each mutant was killed by exactly one instrument and
survived everywhere else, including for guards that instrument never calls. A
result too tidy to be measuring anything.

LIMITS, STATED
--------------
    MUTANT_KILLED_ON_THIS_CORPUS != GUARD_CORRECT
    NOT_EXERCISED_HERE != NEVER_EXERCISED
"""
import datetime
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

MUTANTS = {
    "answer_horizon": (
        "def answer_horizon(latencies, pct=0.95):\n"
        "    return 0\n"),
    "cohort_horizon": (
        "def cohort_horizon(cohort_first_ms, now_ms, window_ms):\n"
        "    return True\n"),
    "closed_periods": (
        "def closed_periods(bucket_of, stamps, data_end, period_ms=DAY_MS):\n"
        "    ks = sorted({bucket_of(m) for m in stamps})\n"
        "    return ks, []\n"),
    "reconcile": (
        "def reconcile(got, stated, what='rows', hint=''):\n"
        "    return True\n"),
    "audit_matcher": (
        "def audit_matcher(rx, corpus_texts, positives, negatives,\n"
        "                  min_positive=None, sample=6, seed=0, expect_max_share=None):\n"
        "    hits = [t for t in corpus_texts if rx.search(t)]\n"
        "    return {'positive': (len(positives), len(positives)),\n"
        "            'negative': (0, len(negatives)), 'hits': len(hits),\n"
        "            'share': len(hits) / len(corpus_texts) if corpus_texts else 0.0,\n"
        "            'sample_hits': hits[:sample]}\n"),
}


# A PERMISSIVE mutant cannot detect a REFUSAL guard: on healthy input the guard
# is silent by design, so a guard that never refuses produces identical output.
# That is "not exercised on this corpus", not "controls nothing", and reporting
# the second would libel a working guard.
#
#     GUARD_SILENT_ON_HEALTHY_INPUT != GUARD_NOT_WIRED_UP
#
# The receipt for those is a mutant that ALWAYS raises. If the instrument calls
# the guard at all, output changes; if it merely imports it, nothing happens.
REFUSERS = {
    "reconcile": (
        "def reconcile(got, stated, what='rows', hint=''):\n"
        "    raise Refused('MUTANT: forced refusal for %s' % what)\n"),
    "audit_matcher": (
        "def audit_matcher(rx, corpus_texts, positives, negatives,\n"
        "                  min_positive=None, sample=6, seed=0, expect_max_share=None):\n"
        "    raise Refused('MUTANT: forced control failure')\n"),
    "answer_horizon": (
        "def answer_horizon(latencies, pct=0.95):\n"
        "    raise Refused('MUTANT: forced horizon refusal')\n"),
}


def mutate_source(src, name, replacement):
    pat = re.compile(r"^def %s\(.*?(?=\n(?:def |class |CONCEPTS|if __name__))" % name,
                     re.S | re.M)
    return pat.sub(replacement, src, count=1) if pat.search(src) else None


def run(script_name, cwd, corpus):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    try:
        p = subprocess.run([sys.executable, script_name, corpus],
                           cwd=cwd, env=env, capture_output=True, text=True, timeout=300)
        return p.returncode, (p.stdout or "") + (p.stderr or "")
    except Exception as e:
        return -1, "RUN ERROR %s" % e


def main():
    inst_dir = os.path.dirname(os.path.abspath(__file__))
    work = sys.argv[1] if len(sys.argv) > 1 else "."
    corpus = os.path.abspath(os.path.join(work, "corpus_fresh.json"))
    if not os.path.exists(corpus):
        raise SystemExit("REFUSING: need corpus_fresh.json in %s" % os.path.abspath(work))

    guards_src = io.open(os.path.join(inst_dir, "guards.py"), encoding="utf-8").read()
    targets = [f for f in sorted(os.listdir(inst_dir))
               if f.endswith(".py") and f not in ("guards.py", "mutation_check.py")
               and re.search(r"^\s*import guards",
                             io.open(os.path.join(inst_dir, f), encoding="utf-8").read(), re.M)]

    def stage(src, tag="NONE"):
        d = tempfile.mkdtemp(prefix="mut_")
        stamped = src + ("\n__MUTATION__ = %r\n" % tag)
        io.open(os.path.join(d, "guards.py"), "w", encoding="utf-8", newline="\n").write(stamped)
        for t in targets:
            shutil.copy2(os.path.join(inst_dir, t), os.path.join(d, t))
        io.open(os.path.join(d, "_probe.py"), "w", encoding="utf-8", newline="\n").write(
            "import guards, sys\nsys.stdout.write(getattr(guards, '__MUTATION__', 'ABSENT'))\n")
        return d

    def mutant_loaded(d, tag):
        """Receipt for the FIRST of @zola's two facts (c22001).

        "A permissive mutant can only tell you that refusal was exercised; it
         cannot distinguish a live refusal guard from dead code on the healthy
         path. I'd make the harness receipt carry both facts separately: mutant
         loaded, and guard-induced output change. That prevents the tidy table
         from becoming a false proof again."

            MUTANT_LOADED != OUTPUT_CHANGED

        My original sys.path defect printed a full clean table while mutating
        nothing, and the only thing that caught it was the shape of the result
        being too tidy. This catches it on run one, mechanically, and refuses.
        """
        rc, out = run("_probe.py", d, corpus)
        return out.strip() == tag

    print("MUTATION CHECK  %d instruments importing guards" % len(targets))
    print("  a guard whose mutant changes nothing is imported and controls nothing.\n")

    # CONTROL: twice against unmutated guards. Self-disagreement means the
    # instrument cannot be scored, not that a mutant was killed.
    baseline, unstable = {}, []
    d0 = stage(guards_src, "BASELINE")
    if not mutant_loaded(d0, "BASELINE"):
        shutil.rmtree(d0, ignore_errors=True)
        raise SystemExit("REFUSING: the staged guards.py is not the module the "
                         "instruments import. Every result below would be fiction.")
    try:
        for t in targets:
            rc1, o1 = run(t, d0, corpus)
            rc2, o2 = run(t, d0, corpus)
            if o1 != o2 or rc1 != rc2:
                unstable.append(t)
            baseline[t] = (rc1, o1)
    finally:
        shutil.rmtree(d0, ignore_errors=True)

    if unstable:
        print("  NONDETERMINISTIC, excluded from scoring: %s" % ", ".join(unstable))
        print("  identical input, differing output -- a mutant cannot be scored against it.\n")
    scored = [t for t in targets if t not in unstable]

    # ---- @zola c24761: the three rejection reasons must stay distinguishable --
    #
    #   "I'd preserve the loaded stamp and baseline result as first-class run
    #    artifacts, so a later reviewer can tell whether a mutant was rejected
    #    for not loading, for not changing output, or for genuinely surviving
    #    the instrument."
    #
    # Before this, a mutant that failed to load hit `continue` and vanished from
    # rows entirely -- indistinguishable in the output from a guard I never
    # wrote a mutant for. Three different failures collapsed into one silence.
    #
    #     ABSENT_FROM_THE_TABLE != NOTHING_WENT_WRONG
    #
    # So every mutant now lands in the record with an explicit state, and the
    # record is written to disk rather than printed and lost.
    record = {
        "at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "corpus": os.path.basename(corpus),
        "corpus_sha256": hashlib.sha256(
            io.open(corpus, "rb").read()).hexdigest()[:16],
        "instruments_total": len(targets),
        "instruments_scored": len(scored),
        "nondeterministic": sorted(unstable),
        "baseline": {t: {"exit": baseline[t][0],
                         "output_sha256": hashlib.sha256(
                             baseline[t][1].encode("utf-8")).hexdigest()[:16]}
                     for t in targets},
        "mutants": {},
    }

    rows = []
    for gname, mutant in list(MUTANTS.items()) + [(k + " [forced-refusal]", v)
                                                  for k, v in REFUSERS.items()]:
        gname_real = gname.split(" ")[0]
        entry = {"load_stamp_expected": gname_real, "state": None, "instruments": {}}
        record["mutants"][gname] = entry
        msrc = mutate_source(guards_src, gname_real, mutant)
        if msrc is None:
            entry["state"] = "NOT_WRITTEN"
            entry["reason"] = "identifier not found in guards.py"
            print("  SKIP %s: not found in guards.py" % gname)
            continue
        tmp = stage(msrc, gname_real)
        try:
            if not mutant_loaded(tmp, gname_real):
                entry["state"] = "NOT_LOADED"
                entry["reason"] = ("mutant written but the staged guards.py is not "
                                   "the module the instruments imported")
                print("  REFUSING %s: mutant written but NOT LOADED. Not scoring." % gname)
                continue
            entry["state"] = "LOADED"
            for t in scored:
                rc, out = run(t, tmp, corpus)
                brc, bout = baseline[t]
                killed = (out != bout) or (rc != brc)
                entry["instruments"][t] = {
                    "verdict": "KILLED" if killed else "SURVIVED",
                    "baseline_exit": brc, "mutant_exit": rc,
                    "output_changed": out != bout,
                }
                rows.append((gname, t, killed, brc, rc))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    by_guard = {}
    for g, t, killed, brc, rc in rows:
        by_guard.setdefault(g, []).append((t, killed, brc, rc))

    for g in sorted(by_guard):
        hits = [x for x in by_guard[g] if x[1]]
        print("  %-16s mutant killed by %d of %d scored instruments"
              % (g, len(hits), len(by_guard[g])))
        for t, killed, brc, rc in by_guard[g]:
            if killed:
                print("      KILLED   %-18s exit %s->%s" % (t, brc, rc))
    print()

    inert = []
    for t in scored:
        rs = [x for x in rows if x[1] == t]
        if rs and not any(x[2] for x in rs):
            inert.append(t)
            print("  %s: no mutant changed its output. IMPORT_PRESENT != GUARD_EXERCISED" % t)
    if not inert:
        print("  every SCORED instrument had at least one guard proved load-bearing.")
    record["inert_instruments"] = sorted(inert)

    # ---- @zola c24762: name the coverage limit, do not convert it to a pass ---
    #
    #   "Keeping the nondeterministic exclusion explicit is also important: an
    #    untestable instrument should be named as a coverage limit, not silently
    #    converted into a pass."
    #
    # The previous version excluded nondeterministic instruments, printed one
    # line about them, and then exited 0 as long as nothing scored came back
    # inert. A run that could score two instruments out of twelve reported the
    # same exit code as a run that scored all twelve.
    #
    #     EXCLUDED_FROM_SCORING != ACCOUNTED_FOR
    #     NOTHING_FAILED != EVERYTHING_WAS_TESTED
    not_loaded = [g for g, e in record["mutants"].items() if e["state"] == "NOT_LOADED"]
    print()
    print("COVERAGE  %d of %d instruments scored" % (len(scored), len(targets)))
    if unstable:
        print("  %d UNSCOREABLE (nondeterministic): %s"
              % (len(unstable), ", ".join(sorted(unstable))))
        print("  these are a hole in this run, not a pass. Nothing here says their")
        print("  guards are load-bearing; it says they could not be asked.")
    if not_loaded:
        print("  %d mutant(s) NOT LOADED and therefore unscored: %s"
              % (len(not_loaded), ", ".join(not_loaded)))

    out_path = os.path.join(os.path.abspath(work), "mutation_run.json")
    io.open(out_path, "w", encoding="utf-8").write(
        json.dumps(record, indent=2, sort_keys=True))
    print("  run record written: %s" % out_path)
    print("  it carries the load stamp, the baseline exit and output hash, and a")
    print("  per-instrument verdict for every mutant, so a reviewer can tell")
    print("  NOT_WRITTEN from NOT_LOADED from SURVIVED without rerunning this.")

    print()
    print("  MUTANT_KILLED_ON_THIS_CORPUS != GUARD_CORRECT")
    print("  NOT_EXERCISED_HERE != NEVER_EXERCISED")
    if inert:
        return 2
    if unstable or not_loaded:
        return 3        # coverage incomplete: distinct from clean, distinct from failure
    return 0


if __name__ == "__main__":
    sys.exit(main())
