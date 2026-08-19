#!/usr/bin/env python3
"""
comsync fast - emit the FAST half of COM state.

PARTIAL. Shipped unfinished on purpose; the gap is named at the bottom and in
--help. Extend it rather than rebuilding it.

Why this exists, from one measured day (2026-08-19). Every failure that cost
real time had the same shape:

    a DECLARED identity sitting next to a different MEASURED one

    FW declared head ea8c7105           PR was at 6c6cc6e4
    hotfix gated on R28F                installed base had to be measured
    CC published 439 self-corrections   saved instrument gives 296
    route object said transport BLOCKED capability probe said ANCHORED

None of these was a lie and none was caught by reading. Each was caught, late,
by someone going and measuring. This emits the measured half so the comparison
is cheap and nobody has to remember to make it.

FAST is small, rewritten whole every sync, and every row carries its own clock.
SLOW state (project goals, baselines, work items) is deliberately NOT here.
"""

import argparse
import datetime
import hashlib
import json
import os
import subprocess
import sys

UTC = datetime.timezone.utc
SCHEMA = "com-fast-state-v0.1-partial"

SQUARE = r"C:\Users\markg\OneDrive\Documents\Campfire-Square"
INSTALLED = os.path.join(SQUARE, "App", "Campfire-Square.ps1")
LEDGER = os.path.join(SQUARE, "Profiles", "cc-relay", "Ledger", "events.jsonl")
WRITE_STATE = os.path.join(SQUARE, "WriteRelay", "cc-relay", "state.json")
WRITE_CONFIG = os.path.join(SQUARE, "WriteRelay", "cc-relay", "config.json")

DUE = ("CORRECTION_DUE", "PUBLIC_CORRECTION_DUE")
DUE_INV = ("WITNESS_INVESTIGATION_DUE",)
CLOSED = ("CORRECTION_CLOSED", "PUBLIC_CORRECTION_CLOSED", "PUBLIC_CORRECTION_NOT_REQUIRED")
CLOSED_INV = ("WITNESS_INVESTIGATION_RESOLVED",)


def now():
    return datetime.datetime.now(UTC).isoformat(timespec="seconds")


def measured(fn):
    """Every row is a measurement or an explicit failure. Never a silent default."""
    try:
        v = fn()
        return dict(v, measured_at_utc=now())
    except Exception as e:
        return {"result": "MEASUREMENT_FAILED",
                "error": "%s: %s" % (type(e).__name__, e),
                "measured_at_utc": now()}


def m_installed_source():
    with open(INSTALLED, "rb") as fh:
        b = fh.read()
    return {"result": "MEASURED", "path": INSTALLED,
            "sha256": hashlib.sha256(b).hexdigest(), "bytes": len(b),
            "method": "sha256(file)"}


def m_obligations():
    due = inv_due = closed = inv_closed = 0
    open_ids = {}
    for line in open(LEDGER, encoding="utf-8-sig"):
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
        except Exception:
            continue
        t = r.get("type")
        d = r.get("data") or {}
        # DUE rows carry both debt_id and action_id; CLOSURE rows carry only
        # debt_id. Keying on action_id silently never closes anything, which
        # reported cc023-a1 as open on 2026-08-19 while the counts were right.
        did = d.get("debt_id")
        aid = d.get("action_id")
        if t in DUE:
            due += 1
            open_ids.setdefault(did, {"action_id": aid, "types": []})["types"].append(t)
        elif t in DUE_INV:
            inv_due += 1
            open_ids.setdefault(did, {"action_id": aid, "types": []})["types"].append(t)
        elif t in CLOSED:
            closed += 1
            open_ids.pop(did, None)
        elif t in CLOSED_INV:
            inv_closed += 1
            open_ids.pop(did, None)
    return {"result": "MEASURED", "method": "count(ledger rows)", "ledger": LEDGER,
            "open_correction_debts": due - closed,
            "open_witness_investigations": inv_due - inv_closed,
            "open_action_ids": sorted(
                set(v["action_id"] for v in open_ids.values() if v.get("action_id"))),
            "blocks_remote_routine_write":
                (due - closed) > 0 or (inv_due - inv_closed) > 0}


def m_write_lane():
    st = json.load(open(WRITE_STATE, encoding="utf-8-sig"))
    cfg = json.load(open(WRITE_CONFIG, encoding="utf-8-sig"))
    return {"result": "MEASURED", "enabled": bool(cfg.get("enabled")),
            "allowed_operations": cfg.get("allowed_operations"),
            "correction_debt_closure_permitted": bool(cfg.get("correction_debt_closure")),
            "active_request_id": st.get("active_request_id"),
            "active_dispatch_phase": st.get("active_dispatch_phase"),
            "config_updated_at_utc": cfg.get("updated_at_utc")}


def m_git_head(repo, ref):
    url = "https://github.com/markgoodbody-bit/%s.git" % repo
    p = subprocess.run(["git", "ls-remote", url, ref],
                       capture_output=True, text=True, timeout=90)
    if p.returncode != 0 or not p.stdout.strip():
        return {"result": "NOT_FOUND", "repo": repo, "ref": ref,
                "method": "git ls-remote"}
    return {"result": "MEASURED", "repo": repo, "ref": ref,
            "sha": p.stdout.split()[0], "method": "git ls-remote"}


def reconcile(declared, rows):
    """
    The point of the whole file. A declaration is checked against the row that
    measured the same thing. Disagreement is reported, never resolved here.
    """
    out = []
    for d in declared:
        row = rows.get(d["measure"]) or {}
        field = d.get("field", "sha256")
        got = row.get(field)
        out.append({"declared_by": d.get("by"), "declared_in": d.get("where"),
                    "measure": d["measure"], "field": field,
                    "declared": d["value"], "measured": got,
                    "agree": got is not None and str(got) == str(d["value"]),
                    "measured_at_utc": row.get("measured_at_utc")})
    return out


def main():
    ap = argparse.ArgumentParser(
        description="Emit the FAST half of COM state. PARTIAL - see UNFINISHED.",
        epilog="UNFINISHED: declarations are supplied by hand via --declared. "
               "They should be harvested automatically from COM messages, which "
               "is the obvious next slice and is not built.")
    ap.add_argument("--declared", help="JSON file: [{by,where,measure,value,field?}]")
    ap.add_argument("--branch", action="append", default=[],
                    help="repo:ref to measure, repeatable")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    rows = {
        "installed_source": measured(m_installed_source),
        "obligations": measured(m_obligations),
        "write_lane": measured(m_write_lane),
    }
    for spec in a.branch:
        repo, _, ref = spec.partition(":")
        rows["branch:" + spec] = measured(lambda r=repo, b=ref: m_git_head(r, b))

    declared = json.load(open(a.declared, encoding="utf-8")) if a.declared else []
    checks = reconcile(declared, rows)

    doc = {"schema": SCHEMA, "emitted_at_utc": now(), "emitted_by": "cc-relay",
           "note": "Emitted, not authored. If this timestamp is old, treat as ABSENT.",
           "measured": rows, "declared_vs_measured": checks,
           "disagreements": [c for c in checks if not c["agree"]]}

    if a.json:
        print(json.dumps(doc, indent=2, sort_keys=True))
        return 2 if doc["disagreements"] else 0

    print("COM FAST STATE  %s  (%s)" % (doc["emitted_at_utc"], SCHEMA))
    src = rows["installed_source"]
    ob = rows["obligations"]
    wl = rows["write_lane"]
    print("  installed source  %s  %s bytes"
          % (str(src.get("sha256"))[:16], src.get("bytes")))
    print("  obligations       %s open debts, %s open investigations  %s"
          % (ob.get("open_correction_debts"), ob.get("open_witness_investigations"),
             ",".join(ob.get("open_action_ids") or []) or "-"))
    print("  write lane        enabled=%s  blocked_by_obligation=%s  debt_closure_allowed=%s"
          % (wl.get("enabled"), ob.get("blocks_remote_routine_write"),
             wl.get("correction_debt_closure_permitted")))
    for k, v in rows.items():
        if k.startswith("branch:"):
            print("  %-18s %-12s %s" % (k[7:][:18], str(v.get("sha"))[:12], v.get("result")))
    for c in checks:
        print("  %-8s %-18s declared %-16s measured %s"
              % ("AGREE" if c["agree"] else "DISAGREE", c["measure"][:18],
                 str(c["declared"])[:16], str(c["measured"])[:16]))
    if not checks:
        print("  (no declarations supplied; pass --declared to reconcile)")
    return 2 if doc["disagreements"] else 0


if __name__ == "__main__":
    sys.exit(main())
