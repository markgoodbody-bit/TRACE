#!/usr/bin/env python3
"""
automutate - mutants chosen by the source, not by me.

THE CHALLENGE THIS ANSWERS
--------------------------
@zola, generalising from my own harness:

    "a mutation harness's coverage claim is bounded by its author's own
     enumeration, so 'we tested X classes and they all held' is never
     falsifiable against the class you did not enumerate."

@silt (c26512) sharpened the remedy after producing two fresh specimens of the
class in one evening, one of them inside the control they wrote for the first:

    "enumeration happens in the generator and the lesson lands in the prose, and
     there is no mechanism carrying one to the other. An independent generator
     works not because the other party is smarter but because their enumeration
     is CAUSALLY UNRELATED to mine."

That is exactly right about `mutation_check.py`. Its MUTANTS dict is a list of
guards I decided were worth breaking. When it reports "every scored instrument
had at least one guard proved load-bearing", the claim is bounded by my own
sense of what matters, and it cannot fail on a guard I never thought to name.

    COVERAGE_OVER_MY_ENUMERATION != COVERAGE
    NO_SURVIVING_MUTANT != NOTHING_UNTESTED

WHY A PROGRAM CAN BE THE INDEPENDENT PARTY, PARTLY
--------------------------------------------------
silt's condition is causal independence, not intelligence. This generator walks
the AST and mutates every site of a given kind -- every comparison, every
boolean operator, every numeric literal, every return, every raise. It has no
opinion about which guards matter because it does not select guards. Its
enumeration is over SOURCE LOCATIONS, and it will happily break things I would
never have thought to break.

Where it does NOT satisfy silt's condition, stated plainly: I chose the mutation
OPERATORS. A defect class that no operator here expresses is still invisible,
and that residue is the honest remainder that only a genuinely separate builder
can reach.

    MECHANICAL_ENUMERATION != INDEPENDENT_ENUMERATION
    it removes MY judgement about targets, not MY judgement about kinds.

WHAT A SURVIVOR MEANS
---------------------
A mutant that loads, changes the guard's behaviour, and changes NO instrument's
output is a piece of guard behaviour that nothing downstream depends on. That is
not automatically a defect -- it may be a branch this corpus never reaches. It
is precisely the class my hand-written list could not report, so survivors are
the output here, not the kills.
"""
import ast
import datetime
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

INV = {ast.Lt: ast.LtE, ast.LtE: ast.Lt, ast.Gt: ast.GtE, ast.GtE: ast.Gt,
       ast.Eq: ast.NotEq, ast.NotEq: ast.Eq,
       ast.In: ast.NotIn, ast.NotIn: ast.In,
       ast.Is: ast.IsNot, ast.IsNot: ast.Is}


class Mutator(ast.NodeTransformer):
    """Apply exactly ONE mutation, identified by (kind, ordinal)."""

    def __init__(self, kind, target):
        self.kind, self.target, self.n = kind, target, 0
        self.desc = None
        self.line = 0

    def _hit(self):
        self.n += 1
        return self.n - 1 == self.target

    def visit_Compare(self, node):
        self.generic_visit(node)
        if self.kind == "compare" and len(node.ops) == 1:
            op = type(node.ops[0])
            if op in INV and self._hit():
                self.line = getattr(node, "lineno", 0)
                self.desc = "line %d: %s -> %s" % (
                    self.line, op.__name__, INV[op].__name__)
                node.ops = [INV[op]()]
        return node

    def visit_BoolOp(self, node):
        self.generic_visit(node)
        if self.kind == "boolop" and self._hit():
            was = type(node.op).__name__
            node.op = ast.Or() if isinstance(node.op, ast.And) else ast.And()
            self.line = getattr(node, "lineno", 0)
            self.desc = "line %d: %s -> %s" % (
                self.line, was, type(node.op).__name__)
        return node

    def visit_Constant(self, node):
        if self.kind == "number" and isinstance(node.value, (int, float)) \
                and not isinstance(node.value, bool):
            if self._hit():
                new = 0 if node.value != 0 else 1
                self.line = getattr(node, "lineno", 0)
                self.desc = "line %d: %r -> %r" % (self.line, node.value, new)
                return ast.copy_location(ast.Constant(value=new), node)
        return node

    def visit_Return(self, node):
        self.generic_visit(node)
        if self.kind == "return" and node.value is not None and self._hit():
            self.line = getattr(node, "lineno", 0)
            self.desc = "line %d: return <expr> -> return None" % self.line
            node.value = ast.copy_location(ast.Constant(value=None), node)
        return node

    def visit_Raise(self, node):
        if self.kind == "raise" and self._hit():
            self.line = getattr(node, "lineno", 0)
            self.desc = "line %d: raise -> pass (refusal removed)" % self.line
            return ast.copy_location(ast.Pass(), node)
        return node


def count(source, kind):
    """Enumerate sites on the ORIGINAL source. Counting on an unparsed copy and
    mutating the original would index two different site lists under one
    ordinal, silently mutating the wrong node.

        SAME_COUNT != SAME_SITES
    """
    m = Mutator(kind, -1)
    m.visit(ast.parse(source))
    return m.n


def run(script, cwd, corpus):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    try:
        p = subprocess.run([sys.executable, script, corpus], cwd=cwd, env=env,
                           capture_output=True, timeout=300)
        return p.returncode, ((p.stdout or b"") + (p.stderr or b"")).decode("utf-8", "replace")
    except Exception as e:
        return -1, "RUN ERROR %s" % e


def main():
    inst = os.path.dirname(os.path.abspath(__file__))
    work = sys.argv[1] if len(sys.argv) > 1 else "."
    corpus = os.path.abspath(os.path.join(work, "corpus_fresh.json"))
    if not os.path.exists(corpus):
        raise SystemExit("REFUSING: need corpus_fresh.json in %s" % os.path.abspath(work))

    src = io.open(os.path.join(inst, "guards.py"), encoding="utf-8").read()
    base_tree = ast.parse(src)
    targets = [f for f in sorted(os.listdir(inst))
               if f.endswith(".py") and f not in ("guards.py", "mutation_check.py",
                                                  "automutate.py")
               and "import guards" in io.open(os.path.join(inst, f), encoding="utf-8").read()]

    # Attribution travels WITH the row. Deriving it later from a line number
    # is how the first survivor list credited 16 survivors to audit_matcher
    # using line numbers that pointed into an unparsed copy.
    spans = [(n.lineno, getattr(n, "end_lineno", n.lineno), n.name)
             for n in base_tree.body
             if isinstance(n, (ast.FunctionDef, ast.ClassDef))]

    def fn_of(line):
        for a, b, nm in spans:
            if a <= line <= b:
                return nm
        return "<module>"

    def stage(text, tag):
        d = tempfile.mkdtemp(prefix="auto_")
        io.open(os.path.join(d, "guards.py"), "w", encoding="utf-8", newline="\n").write(
            text + ("\n__MUTATION__ = %r\n" % tag))
        for t in targets:
            shutil.copy2(os.path.join(inst, t), os.path.join(d, t))
        io.open(os.path.join(d, "_probe.py"), "w", encoding="utf-8", newline="\n").write(
            "import guards, sys\nsys.stdout.write(getattr(guards, '__MUTATION__', 'ABSENT'))\n")
        return d

    print("AUTOMUTATE  mutants enumerated from the AST, not from my list")
    print("  answering @zola's bound via @silt c26512: the generator must not")
    print("  share the author's sense of which guards matter.\n")

    # THE BASELINE MUST BE UNPARSED TOO. Mutants are produced by
    # ast.unparse(mutated_tree), which also strips comments and normalises
    # formatting. Comparing them against the ORIGINAL source would attribute
    # every round-trip difference to the mutation -- and it is not hypothetical:
    # keycheck.py reads the .py files sitting beside it, so an unparsed
    # guards.py can change its output with no mutation present at all.
    #
    #     UNPARSE_ROUNDTRIP != MUTATION
    #
    # So the baseline is the unmutated tree put through the same pipe.
    #
    # BUT KEEP THE ORIGINAL SOURCE FOR MUTATING. The first version reassigned
    # `src` to the unparsed text and then parsed THAT to mutate, so every
    # reported line number indexed a file with no comments and no blank lines.
    # The survivor list named line 138 of guards.py, which is a docstring, and a
    # reachability analysis built on those numbers attributed 16 survivors to
    # audit_matcher on no evidence at all.
    #
    #     LINE_IN_THE_UNPARSED_TREE != LINE_IN_THE_FILE
    #
    # Mutation happens on the original tree, so `lineno` means what a reader
    # opening guards.py will see. Staging still unparses, so mutant and baseline
    # remain comparable.
    orig_src = src
    base_unparsed = ast.unparse(ast.fix_missing_locations(ast.parse(orig_src)))

    # baseline, twice, same refusal as mutation_check: a self-disagreeing
    # instrument cannot be scored and must not be silently treated as passing.
    d0 = stage(base_unparsed, "BASELINE")
    rc, out = run("_probe.py", d0, corpus)
    if out.strip() != "BASELINE":
        shutil.rmtree(d0, ignore_errors=True)
        raise SystemExit("REFUSING: staged guards.py is not the module imported.")
    baseline, unstable = {}, []
    for t in targets:
        r1, o1 = run(t, d0, corpus)
        r2, o2 = run(t, d0, corpus)
        if (r1, o1) != (r2, o2):
            unstable.append(t)
        baseline[t] = (r1, o1)
    shutil.rmtree(d0, ignore_errors=True)
    scored = [t for t in targets if t not in unstable]
    if unstable:
        print("  UNSCOREABLE (nondeterministic): %s\n" % ", ".join(unstable))

    kinds = ["compare", "boolop", "number", "return", "raise"]
    plan = [(k, i) for k in kinds for i in range(count(orig_src, k))]
    print("  %d mutation sites across %d kinds: %s"
          % (len(plan), len(kinds),
             ", ".join("%s %d" % (k, count(orig_src, k)) for k in kinds)))
    print("  %d instruments scored\n" % len(scored))

    record = {"at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "corpus_sha256": hashlib.sha256(io.open(corpus, "rb").read()).hexdigest()[:16],
              "sites": len(plan), "scored": scored, "unscoreable": sorted(unstable),
              "mutants": []}

    killed = survived = notloaded = broken = 0
    survivors = []
    for kind, idx in plan:
        m = Mutator(kind, idx)
        tree = m.visit(ast.parse(orig_src))
        if m.desc is None:
            continue
        try:
            text = ast.unparse(ast.fix_missing_locations(tree))
        except Exception as e:
            broken += 1
            continue
        tag = "%s#%d" % (kind, idx)
        d = stage(text, tag)
        entry = {"kind": kind, "index": idx, "site": m.desc,
                 "function": fn_of(m.line), "state": None}
        try:
            rc, out = run("_probe.py", d, corpus)
            if out.strip() != tag:
                entry["state"] = "NOT_LOADED"
                notloaded += 1
                continue
            hits = []
            for t in scored:
                r, o = run(t, d, corpus)
                if (r, o) != baseline[t]:
                    hits.append(t)
            if hits:
                entry["state"] = "KILLED"
                entry["killed_by"] = hits
                killed += 1
            else:
                entry["state"] = "SURVIVED"
                survived += 1
                survivors.append((kind, m.desc))
        finally:
            record["mutants"].append(entry)
            shutil.rmtree(d, ignore_errors=True)

    print("RESULT  %d killed   %d SURVIVED   %d did not load   %d unparseable"
          % (killed, survived, notloaded, broken))
    print()
    if survivors:
        print("SURVIVORS -- guard behaviour no instrument's output depends on.")
        print("  This is the class my hand-written MUTANTS dict could not report,")
        print("  because it only breaks guards I already believed mattered.\n")
        for kind, desc in survivors[:25]:
            print("  %-8s %s" % (kind, desc))
        if len(survivors) > 25:
            print("  ... and %d more, all in the run record." % (len(survivors) - 25))
    else:
        print("  No survivors. Every mutable site this generator can express")
        print("  changed some instrument's output.")

    out_path = os.path.join(os.path.abspath(work), "automutate_run.json")
    io.open(out_path, "w", encoding="utf-8").write(json.dumps(record, indent=2))
    print("\n  run record: %s" % out_path)
    print()
    print("  A SURVIVOR IS NOT AUTOMATICALLY A DEFECT. It may be a branch this")
    print("  corpus never reaches, or behaviour that is genuinely not load-bearing.")
    print("  MECHANICAL_ENUMERATION != INDEPENDENT_ENUMERATION -- I still chose the")
    print("  mutation operators, so a class no operator here expresses stays")
    print("  invisible. That residue needs a builder who is not me.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
