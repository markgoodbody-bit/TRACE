"""seedaudit.py DIR...

brak-potato, c39873 on post 3211 (2026-09-03): the bug class is "seed a random
process fed by an unseeded set-to-list conversion"; audit for list(some_set) or
set comprehensions feeding anything seeded, rather than treating burst.py as
closed. This walks every .py under the given directories by AST.

For each call to a randomising function (random.shuffle/sample/choice/choices,
Random(...).shuffle/... , numpy.random.*), it collects the names in the call's
arguments and asks whether any of those names is, anywhere in the same scope or
at module level, bound to an unordered source: a set literal, set(), a set
comprehension, set operators (| & - ^) on names, dict.keys()/.items()/.values()
(ordered by insertion, but insertion from an unordered walk inherits the order),
or a call to a function whose name contains "set". It also flags the direct
form random_call(list(x)) / random_call(sorted(...)) so the repaired cases are
visible as repaired.

It prints, per file: randomising call sites, and for each the verdict
  ORDERED     every argument name traces to a list/sorted/tuple or literal
  SET-FED     an argument name traces to an unordered source with no sorted()
  UNTRACED    an argument's origin is not resolvable statically (say so)
Exit 1 if any SET-FED remains.
"""
import ast, os, sys

RAND_ATTRS = {"shuffle", "sample", "choice", "choices", "randrange", "randint", "permutation"}
UNORDERED_CALLS = {"set", "frozenset"}


def is_rand_call(node):
    f = node.func
    if isinstance(f, ast.Attribute) and f.attr in RAND_ATTRS:
        return True
    return False


def unordered_expr(e):
    """True if the expression is structurally unordered."""
    if isinstance(e, (ast.Set, ast.SetComp)):
        return True
    if isinstance(e, ast.Call):
        fn = e.func
        name = fn.id if isinstance(fn, ast.Name) else (fn.attr if isinstance(fn, ast.Attribute) else "")
        if name in UNORDERED_CALLS:
            return True
        if name in {"keys", "values", "items"}:
            return "dict-view"
    if isinstance(e, ast.BinOp) and isinstance(e.op, (ast.BitOr, ast.BitAnd, ast.Sub, ast.BitXor)):
        return "set-op?"
    return False


def comp_sources(e):
    """Iterables a comprehension draws from (the burst.py shape: [h for h in a_set])."""
    return [g.iter for g in getattr(e, "generators", [])]


def ordered_expr(e):
    if isinstance(e, ast.ListComp):
        # ordered only if every generator iterates something ordered; a
        # comprehension over a set is the bug itself, not a repair of it
        return all(not unordered_expr(it) for it in comp_sources(e))
    if isinstance(e, (ast.List, ast.Tuple)):
        return True
    if isinstance(e, ast.Call):
        fn = e.func
        name = fn.id if isinstance(fn, ast.Name) else (fn.attr if isinstance(fn, ast.Attribute) else "")
        if name in {"sorted", "list", "tuple", "range", "enumerate"}:
            # list(set) is the bug; list(sorted) / list(list) fine
            if name == "list" and e.args and unordered_expr(e.args[0]):
                return False
            return True
    return False


def bindings(tree):
    """name -> list of value expressions bound to it (module + all functions)."""
    b = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name):
                    b.setdefault(t.id, []).append(node.value)
        elif isinstance(node, (ast.AugAssign, ast.AnnAssign)) and isinstance(node.target, ast.Name):
            if node.value is not None:
                b.setdefault(node.target.id, []).append(node.value)
        elif isinstance(node, ast.For) and isinstance(node.target, ast.Name):
            b.setdefault(node.target.id, []).append(node.iter)
    return b


def trace(name, b, depth=0, seen=None):
    seen = seen or set()
    if name in seen or depth > 6:
        return "UNTRACED"
    seen.add(name)
    vals = b.get(name)
    if not vals:
        return "UNTRACED"
    verdicts = []
    for v in vals:
        u = unordered_expr(v)
        if u:
            verdicts.append("SET-FED(%s)" % (u if isinstance(u, str) else "set"))
            continue
        if isinstance(v, ast.ListComp):
            srcs = []
            for it in comp_sources(v):
                if unordered_expr(it):
                    srcs.append("SET-FED(comp over set)")
                elif isinstance(it, ast.Name):
                    t = trace(it.id, b, depth + 1, seen)
                    srcs.append("SET-FED(comp over %s)" % it.id if t.startswith("SET-FED") else t)
                elif isinstance(it, ast.Call) and it.args and isinstance(it.args[0], ast.Name):
                    fn = it.func.id if isinstance(it.func, ast.Name) else getattr(it.func, "attr", "")
                    t = trace(it.args[0].id, b, depth + 1, seen)
                    srcs.append("ORDERED(sorted)" if fn == "sorted" else t)
                else:
                    srcs.append("ORDERED" if ordered_expr(it) else "UNTRACED")
            if any(s.startswith("SET-FED") for s in srcs):
                verdicts.append(next(s for s in srcs if s.startswith("SET-FED")))
            elif all(s.startswith("ORDERED") for s in srcs):
                verdicts.append("ORDERED")
            else:
                verdicts.append("UNTRACED")
            continue
        if ordered_expr(v):
            # sorted()/list() of what? if list(name) trace inner
            if isinstance(v, ast.Call) and v.args and isinstance(v.args[0], ast.Name):
                fn = v.func.id if isinstance(v.func, ast.Name) else v.func.attr
                inner = trace(v.args[0].id, b, depth + 1, seen)
                if fn == "sorted":
                    verdicts.append("ORDERED(sorted)")
                elif inner.startswith("SET-FED"):
                    verdicts.append("SET-FED(list(%s))" % v.args[0].id)
                else:
                    verdicts.append(inner if inner != "UNTRACED" else "ORDERED(%s)" % fn)
            else:
                verdicts.append("ORDERED")
            continue
        if isinstance(v, ast.Name):
            verdicts.append(trace(v.id, b, depth + 1, seen))
            continue
        if isinstance(v, ast.Call) and v.args and isinstance(v.args[0], ast.Name):
            verdicts.append(trace(v.args[0].id, b, depth + 1, seen))
            continue
        verdicts.append("UNTRACED")
    if any(x.startswith("SET-FED") for x in verdicts):
        return next(x for x in verdicts if x.startswith("SET-FED"))
    if all(x.startswith("ORDERED") for x in verdicts):
        return "ORDERED"
    return "UNTRACED"


def audit_file(path):
    src = open(path, encoding="utf-8", errors="replace").read()
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        return [(0, "PARSE-ERROR", str(e))]
    b = bindings(tree)
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and is_rand_call(node):
            args = list(node.args) + [k.value for k in node.keywords]
            if not args:
                out.append((node.lineno, "ORDERED", "no arguments"))
                continue
            verdicts = []
            for a in args:
                if isinstance(a, ast.Name):
                    verdicts.append((a.id, trace(a.id, b)))
                elif unordered_expr(a):
                    verdicts.append(("<expr>", "SET-FED(inline)"))
                elif ordered_expr(a):
                    inner = "ORDERED"
                    if isinstance(a, ast.Call) and a.args and isinstance(a.args[0], ast.Name):
                        fn = a.func.id if isinstance(a.func, ast.Name) else a.func.attr
                        t = trace(a.args[0].id, b)
                        inner = "ORDERED(sorted)" if fn == "sorted" else ("SET-FED(list(%s))" % a.args[0].id if t.startswith("SET-FED") else t if t != "UNTRACED" else "ORDERED")
                    verdicts.append(("<expr>", inner))
                elif isinstance(a, ast.Constant):
                    verdicts.append(("<const>", "ORDERED"))
                else:
                    verdicts.append(("<expr>", "UNTRACED"))
            worst = "ORDERED"
            if any(v.startswith("SET-FED") for _, v in verdicts):
                worst = "SET-FED"
            elif any(v == "UNTRACED" for _, v in verdicts):
                worst = "UNTRACED"
            out.append((node.lineno, worst, ", ".join("%s:%s" % kv for kv in verdicts)))
    return out


def main(dirs):
    total = {"ORDERED": 0, "SET-FED": 0, "UNTRACED": 0, "PARSE-ERROR": 0}
    files = 0
    for d in dirs:
        for root, _, names in os.walk(d):
            if "__pycache__" in root or "/.git" in root.replace("\\", "/"):
                continue
            for n in sorted(names):
                if not n.endswith(".py"):
                    continue
                files += 1
                p = os.path.join(root, n)
                res = audit_file(p)
                if res:
                    print(os.path.relpath(p, d))
                    for ln, verdict, detail in res:
                        total[verdict] = total.get(verdict, 0) + 1
                        print("  line %-5d %-9s %s" % (ln, verdict, detail))
    print("\nfiles scanned %d | randomising call sites: ORDERED %d, SET-FED %d, UNTRACED %d, parse errors %d"
          % (files, total["ORDERED"], total["SET-FED"], total["UNTRACED"], total["PARSE-ERROR"]))
    return 1 if total["SET-FED"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or ["."]))
