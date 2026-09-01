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
import ast
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
    # Drops the matched spans and prints only the pass/fail line -- the exact
    # 2026-08-30 defect that let "Baseball, huh?" sit atop a member-facing list
    # under a clean 4/4. Killed by any instrument that calls report.
    "report": (
        "def report(res, label='matcher'):\n"
        "    print('CONTROLS  %s  positive %d/%d  negative %d/%d'\n"
        "          % (label, res['positive'][0], res['positive'][1],\n"
        "             res['negative'][0], res['negative'][1]))\n"),
    # The pre-repair world: loads the walk artefact and never looks at whether
    # the walk finished. This is exactly what 29 instruments were doing on
    # 2026-09-01 against a corpus whose own meta said complete=False.
    "load_corpus": (
        "def load_corpus(path, allow_incomplete=False):\n"
        "    with io.open(path, encoding='utf-8') as fh:\n"
        "        c = json.load(fh)\n"
        "    return c, (c.get('meta') or {})\n"),
    # The pre-Absence world: a bare negative carrying no scope, and truth-testable,
    # so a caller can collapse it straight back into "not found".
    "Absence": (
        "class Absence(object):\n"
        "    def __init__(self, what, searched=None, note=None):\n"
        "        self.what, self.searched, self.note = what, searched, note\n"
        "    def __str__(self):\n"
        "        return '%s: not found' % self.what\n"
        "    def __bool__(self):\n"
        "        return False\n"
        "    __nonzero__ = __bool__\n"),
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


# EVERY public guard must be either mutated above or exempted HERE, WITH A REASON.
#
# 2026-09-01. The scoring loop iterates over MUTANTS, not over guards.py. So a
# guard added after this dict was written is not scored as unexercised -- it is
# absent from the table entirely, and the table still reads as a full result.
# The hand-maintained list WAS the coverage measure, and nothing checked it
# against the thing it claimed to cover.
#
#     ITERATED_THE_MUTANTS != COVERED_THE_GUARDS
#     ABSENT_FROM_THE_TABLE != PASSED
#
# Found the day `guards.Absence` was discovered to have ZERO call sites in the
# nine instruments written by the author who had written it the night before.
# Its docstring argues that a distinction you must remember at each call site is
# one you will lose at the next -- but CONSTRUCTING an Absence is itself a call
# site, so the class relocated the voluntary step instead of removing it. And
# this file, the instrument built to catch "imported but never exercised", could
# not see it twice over: a class is not a `def`, and it was never in MUTANTS.
#
#     STRUCTURAL_IN_THE_OBJECT != STRUCTURAL_IN_THE_PATH
EXEMPT = {
    "Refused": "the signalling exception type. Mutating it breaks the harness "
               "that detects mutants, not the guard under test.",
    "adoption": "a reporting CLI in guards.py itself, never called from an "
                "instrument. Its receipt is `guards.py --adoption`, and the "
                "whole point of this file is that that receipt is the weak one.",
}


def guard_surface(src):
    """Public top-level guards in guards.py -- functions AND classes."""
    return [n.name for n in ast.parse(src).body
            if isinstance(n, (ast.FunctionDef, ast.ClassDef))
            and not n.name.startswith("_")]


def coverage_gap(src):
    """Public guards with neither a mutant nor a declared exemption."""
    covered = set(MUTANTS) | set(REFUSERS) | set(EXEMPT)
    return [n for n in guard_surface(src) if n not in covered]


def mutate_source(src, name, replacement):
    # `def` only until 2026-09-01: `class Absence` could not be matched by this
    # pattern, so a class-shaped guard stayed unmutatable even once it was named.
    #     NOT_MATCHED_BY_THE_MUTATOR != NOT_A_GUARD
    pat = re.compile(r"^(?:def|class) %s\b.*?(?=\n(?:def |class |CONCEPTS|if __name__))"
                     % name, re.S | re.M)
    return pat.sub(replacement, src, count=1) if pat.search(src) else None


def run(script_name, cwd, corpus):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    # text=True decodes with the PLATFORM default, which is cp1252 here, while
    # the child was told to WRITE utf-8. That mismatch is invisible for as long
    # as the board writes ASCII. On 2026-08-27 @agy_bot posted in Chinese, an
    # instrument echoed the fragment, and the harness died in a reader thread
    # with UnicodeDecodeError -- not a failed mutant, a crashed run.
    #
    #     CHILD_WRITES_UTF8 != PARENT_READS_UTF8
    #     ASCII_SO_FAR != ASCII
    #
    # Decode explicitly, and never let an undecodable byte from a citizen's
    # comment be reported as an instrument failure.
    try:
        p = subprocess.run([sys.executable, script_name, corpus],
                           cwd=cwd, env=env, capture_output=True, timeout=300)
        out = (p.stdout or b"").decode("utf-8", "replace")
        err = (p.stderr or b"").decode("utf-8", "replace")
        return p.returncode, out + err
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

    # Coverage of the GUARD SURFACE, before any scoring. A guard with no mutant
    # is not a passing row and not a failing row -- it is no row at all, which
    # is how `Absence` sat unexercised under a table that looked complete.
    gap = coverage_gap(guards_src)
    surface = guard_surface(guards_src)
    print("SURFACE   %d public guards in guards.py; %d mutated, %d exempt, %d UNCOVERED"
          % (len(surface), len(set(MUTANTS) | set(REFUSERS)), len(EXEMPT), len(gap)))
    for name in gap:
        print("  UNCOVERED  %s -- no mutant and no declared exemption" % name)
    print("")

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

    # `run` invokes every instrument as `python <script> <corpus>`. That is a
    # CONVENTION, not a contract, and census_window.py takes subcommands
    # (`requests`, `serve`) instead. Its baseline run dies in argparse having
    # executed nothing, and both mutant and baseline then produce the identical
    # usage error -- which the scorer would have reported as "imported and
    # controls nothing" about a guard that is wired and does fire.
    #
    #     HARNESS_CANNOT_INVOKE_IT != THE_GUARD_IS_NOT_WIRED
    #     IDENTICAL_OUTPUT != MUTANT_SURVIVED
    #
    # Same treatment as nondeterminism: name the hole, do not convert it to a
    # pass and do not convert it to an accusation.
    _ARGPARSE = ("invalid choice", "the following arguments are required",
                 "unrecognized arguments", "error: argument")
    uninvokable = [t for t in targets if t not in unstable
                   and baseline[t][0] != 0
                   and "usage:" in baseline[t][1]
                   and any(k in baseline[t][1] for k in _ARGPARSE)]
    if uninvokable:
        print("  NOT INVOKABLE by this harness's convention, excluded: %s"
              % ", ".join(uninvokable))
        print("  they take subcommands, not a bare corpus path. Nothing below")
        print("  says their guards are unwired; it says they were never run.\n")

    scored = [t for t in targets if t not in unstable and t not in uninvokable]

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
        "guard_surface": surface,
        "guards_uncovered": gap,
        "guards_exempt": EXEMPT,
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
    if gap:
        print()
        print("  %d guard(s) have no mutant and no declared exemption: %s"
              % (len(gap), ", ".join(gap)))
        print("  Nothing above measured them. Add a mutant, or add an EXEMPT entry")
        print("  with a reason -- but the gap does not get to be silent.")
    if inert:
        return 2
    if gap:
        return 4        # the table is not about the whole guard surface
    if unstable or not_loaded:
        return 3        # coverage incomplete: distinct from clean, distinct from failure
    return 0


if __name__ == "__main__":
    sys.exit(main())
