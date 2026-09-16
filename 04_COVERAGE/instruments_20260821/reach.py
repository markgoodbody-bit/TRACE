#!/usr/bin/env python3
"""
reach - for every refusal in guards.py, is it on a path an instrument actually runs?

THE QUESTION THIS ANSWERS
-------------------------
@zola, c27288 on #1838 (2026-08-28), on automutate's nine surviving `raise -> pass`
mutants:

    "Worth logging which of the nine raise -> pass survivors are reachable from an
     entry point versus only from _selftest/report/adoption -- a refusal that is
     unreachable in production is a smaller finding than one sitting on a live path,
     and right now both read as 'survived' with no way to tell them apart from the
     table alone."

Unanswered for nineteen days. This prints the split.

WHAT IT DOES
------------
Walks guards.py's AST and lists every `raise` with its enclosing function (class
methods qualified). Then walks every scored instrument and records which guards
names are CALLED from code outside functions named _selftest / report / adoption
(a call inside those is a self-test, not a run). A refusal is then one of:

    LIVE_PATH     enclosing function is called by >= 1 instrument's run path
    SELFTEST_ONLY enclosing function is called only from _selftest/report/adoption,
                  or is guards.py's own __main__ block (runs only as a script)
    UNCALLED      enclosing function is called by no instrument at all

Static reachability, stated as such: LIVE_PATH means the function runs, not that
the refusing condition ever occurs on the corpus. automutate runs each instrument
on the real corpus only, so a refusal on a live path survives `raise -> pass`
whenever no scored run would have refused. That survivor class needs a fixture
that drives the refusal, not a bigger corpus.

    REACHABLE_FUNCTION != EXERCISED_REFUSAL
    A_RAISE_IN___MAIN___IS_NOT_A_REFUSAL_AN_INSTRUMENT_CAN_LOSE
"""
import ast, io, os, sys, json, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
SELFTEST_NAMES = {"_selftest", "report", "adoption"}


def raises_in(path):
    """[(line, qualified enclosing name, exception text)] for every Raise node."""
    src = io.open(path, encoding="utf-8").read()
    tree = ast.parse(src)
    out = []

    def walk(node, stack):
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                walk(child, stack + [child.name])
            elif isinstance(child, ast.Raise):
                exc = ast.unparse(child.exc)[:60] if child.exc is not None else "re-raise"
                out.append((child.lineno, ".".join(stack) or "<module>", exc))
                walk(child, stack)
            else:
                walk(child, stack)
    walk(tree, [])
    return out


def guard_calls(path):
    """{guards name: [(line, enclosing function)]} for calls made from this file,
    split into run-path calls and selftest-path calls."""
    src = io.open(path, encoding="utf-8").read()
    tree = ast.parse(src)
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module == "guards":
            imported |= {a.asname or a.name for a in node.names}
    run, selftest = {}, {}

    def walk(node, fn):
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                walk(child, child.name)
                continue
            if isinstance(child, ast.Call):
                name = None
                f = child.func
                if isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name) and f.value.id == "guards":
                    name = f.attr
                elif isinstance(f, ast.Name) and f.id in imported:
                    name = f.id
                if name:
                    (selftest if fn in SELFTEST_NAMES else run).setdefault(name, []).append((child.lineno, fn))
            walk(child, fn)
    walk(tree, "<module>")
    return run, selftest


def main():
    guards = os.path.join(HERE, "guards.py")
    scored = sorted(f for f in os.listdir(HERE)
                    if f.endswith(".py") and f not in ("guards.py", "reach.py") and
                    "guards" in io.open(os.path.join(HERE, f), encoding="utf-8").read())
    if len(sys.argv) > 1:
        scored = [s for s in scored if s in sys.argv[1:]]
    callers_run, callers_self = {}, {}
    for f in scored:
        run, selftest = guard_calls(os.path.join(HERE, f))
        for k, v in run.items():
            callers_run.setdefault(k, []).extend((f, ln, fn) for ln, fn in v)
        for k, v in selftest.items():
            callers_self.setdefault(k, []).extend((f, ln, fn) for ln, fn in v)
    rows = []
    for line, where, exc in raises_in(guards):
        top = where.split(".")[0]
        if where == "<module>":
            state, by = "SELFTEST_ONLY", "guards.py __main__ block; runs only as a script"
        elif top in callers_run:
            by = ", ".join(sorted({f for f, _, _ in callers_run[top]}))
            state = "LIVE_PATH"
        elif top in callers_self:
            by = ", ".join(sorted({"%s:%s" % (f, fn) for f, _, fn in callers_self[top]}))
            state = "SELFTEST_ONLY"
        else:
            state, by = "UNCALLED", "-"
        rows.append({"line": line, "in": where, "raises": exc, "state": state, "reached_by": by})
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print("reach at %s | guards.py %d raise sites | %d instruments read: %s" % (now, len(rows), len(scored), ", ".join(scored)))
    for r in rows:
        print("  line %-4d %-28s %-14s %s" % (r["line"], r["in"], r["state"], r["reached_by"]))
        print("           %s" % r["raises"])
    counts = {}
    for r in rows:
        counts[r["state"]] = counts.get(r["state"], 0) + 1
    print("  " + "  ".join("%s %d" % kv for kv in sorted(counts.items())))
    print("  LIVE_PATH means the function runs on an instrument's run path; whether the refusing")
    print("  condition ever occurs on the corpus is a separate question this does not answer.")
    json.dump({"at_utc": now, "instruments": scored, "rows": rows}, open(os.path.join(HERE, "reach_run.json"), "w", encoding="utf-8"), indent=1)


if __name__ == "__main__":
    main()
