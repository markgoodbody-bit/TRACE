#!/usr/bin/env python3
"""Apply the bounded TRACE v0.2.7 carrier/falsification cross-lane repair."""
from __future__ import annotations

from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 match, found {count}")
    return text.replace(old, new, 1)


def main() -> int:
    runner_path = Path("falsification/run_trace_v027_falsify_x100.py")
    runner = runner_path.read_text(encoding="utf-8")

    old_front = '''    seed_pos = readme.find("TRACE_FORMAL_SEED_v0_2_6.md")
    pdf_pos = readme.find("TRACE.pdf")
    if seed_pos < 0 or pdf_pos < 0 or seed_pos > pdf_pos:
        errors.append("front-door-order")
    if "TRACE.pdf` — older v0.5 human-facing carrier candidate; not the active formal baseline" not in readme:
        errors.append("pdf-label")
'''
    new_front = '''    seed_pos = readme.find("TRACE_FORMAL_SEED_v0_2_7.md")
    pdf_pos = readme.find("TRACE.pdf")
    if seed_pos < 0 or pdf_pos < 0 or seed_pos > pdf_pos:
        errors.append("front-door-order")
    if "TRACE.pdf` — current v0.2.7 rendered formal carrier; the Markdown seed remains the formal source" not in readme:
        errors.append("pdf-label")
'''
    runner = replace_once(runner, old_front, new_front, "required-surface front door")
    runner = replace_once(
        runner,
        '        Probe("D19", "front-door", "active released baseline precedes TRACE.pdf", lambda: 0 <= readme.find("TRACE_FORMAL_SEED_v0_2_6.md") < readme.find("TRACE.pdf")),\n',
        '        Probe("D19", "front-door", "active released v0.2.7 baseline precedes TRACE.pdf", lambda: 0 <= readme.find("TRACE_FORMAL_SEED_v0_2_7.md") < readme.find("TRACE.pdf")),\n',
        "D19",
    )
    runner = replace_once(
        runner,
        '        token_probe("D20", "front-door", "TRACE.pdf is labelled as older carrier", readme, "older v0.5 human-facing carrier candidate; not the active formal baseline"),\n',
        '        token_probe("D20", "front-door", "TRACE.pdf is labelled as current rendered carrier with Markdown authority preserved", readme, "current v0.2.7 rendered formal carrier; the Markdown seed remains the formal source"),\n',
        "D20",
    )
    runner = replace_once(
        runner,
        '            if line.startswith("- `TRACE_FORMAL_SEED_v0_2_6.md`")\n',
        '            if line.startswith("- `TRACE_FORMAL_SEED_v0_2_7.md`")\n',
        "README mutation seed line",
    )
    runner = replace_once(
        runner,
        '        ("M19", "removing stale-PDF label is detected", lambda: bool(required_surface_errors(candidate, readme.replace(" — older v0.5 human-facing carrier candidate; not the active formal baseline", ""), manifest))),\n',
        '        ("M19", "removing current-PDF authority label is detected", lambda: bool(required_surface_errors(candidate, readme.replace(" — current v0.2.7 rendered formal carrier; the Markdown seed remains the formal source", ""), manifest))),\n',
        "M19",
    )
    runner = replace_once(
        runner,
        '            "TRACE_PDF_REMAINS_OLDER_CARRIER_BUT_IS_NOW_LABELLED",\n',
        '            "TRACE_PDF_IS_RENDERED_CARRIER_NOT_FORMAL_SOURCE",\n',
        "runner residual",
    )
    runner_path.write_text(runner, encoding="utf-8")

    release_path = Path("TRACE_v0_2_7_BASELINE_RELEASE.md")
    release = release_path.read_text(encoding="utf-8")
    release = replace_once(
        release,
        "TRACE_PDF_REMAINS_OLDER_CARRIER_BUT_IS_NOW_LABELLED",
        "TRACE_PDF_IS_RENDERED_CARRIER_NOT_FORMAL_SOURCE",
        "release residual",
    )
    release_path.write_text(release, encoding="utf-8")

    report_path = Path("TRACE_v0_2_7_RENDERED_CARRIER_REPORT.md")
    report = report_path.read_text(encoding="utf-8")
    report = replace_once(
        report,
        "**Status:** exact binary visually reviewed; bounded Windows-checkout repair applied; post-repair exact-head recheck pending  ",
        "**Status:** exact binary visually reviewed; independent NARROW findings integrated; final bounded re-anchor pending  ",
        "report status",
    )
    addition = '''

## Windows checkout compatibility

Fresh clones now receive LF bytes for Markdown through:

```text
.gitattributes
*.md text eol=lf
```

This prevents a correct default Git for Windows checkout (`core.autocrlf=true`) from producing a false formal-source hash mismatch. Existing working trees created before the attribute was added may retain CRLF bytes until they are freshly cloned or explicitly renormalised with:

```text
git add --renormalize .
```

That operational caveat is about checkout state, not a change to the released source object.

## Falsification-instrument synchronization

The carrier replacement changes the repository front-door fact previously tested by probes `D19` and `D20`. Those probes were re-pointed rather than retired:

```text
D19: active released v0.2.7 baseline precedes TRACE.pdf
D20: TRACE.pdf is labelled as the current rendered carrier while Markdown remains the formal source
```

`A15` continues to require the complete declared surface to pass. Mutation probe `M19` continues to fail closed if the current-carrier authority label is removed. The original pre-carrier audit report and summary remain historical evidence of the earlier repository state; the executable instrument now tests the post-carrier state.
'''
    if "## Windows checkout compatibility" not in report:
        report += addition
    report_path.write_text(report, encoding="utf-8")

    workflow_path = Path(".github/workflows/trace-v027-pdf-carrier.yml")
    workflow = workflow_path.read_text(encoding="utf-8")
    path_anchor = "      - .gitattributes\n      - TRACE_FORMAL_SEED_v0_2_7.md\n"
    path_replacement = (
        "      - .gitattributes\n"
        "      - README.md\n"
        "      - TRACE_v0_2_7_BASELINE_RELEASE.md\n"
        "      - falsification/**\n"
        "      - TRACE_FORMAL_SEED_v0_2_7.md\n"
    )
    if workflow.count(path_anchor) != 2:
        raise SystemExit(f"workflow paths: expected 2 matches, found {workflow.count(path_anchor)}")
    workflow = workflow.replace(path_anchor, path_replacement, 2)
    step_anchor = '''          python tools/build_trace_v027_carrier.py --check-source

      - name: Rebuild and compare semantic render surface
'''
    step_replacement = '''          python tools/build_trace_v027_carrier.py --check-source

      - name: Run current v0.2.7 falsification instrument
        run: |
          python falsification/run_trace_v027_falsify_x100.py \\
            --strict \\
            --json-out /tmp/trace-v027-falsify-x100-current.json

      - name: Rebuild and compare semantic render surface
'''
    workflow = replace_once(workflow, step_anchor, step_replacement, "persistent x100 step")
    artifact_anchor = '''            /tmp/trace-v027-carrier-rebuild.json
          if-no-files-found: error
'''
    artifact_replacement = '''            /tmp/trace-v027-carrier-rebuild.json
            /tmp/trace-v027-falsify-x100-current.json
          if-no-files-found: error
'''
    workflow = replace_once(workflow, artifact_anchor, artifact_replacement, "artifact x100 output")
    workflow_path.write_text(workflow, encoding="utf-8")

    note = Path("falsification/TRACE_v0_2_7_CARRIER_FRONT_DOOR_PROBE_UPDATE.md")
    note.write_text(
        '''# TRACE v0.2.7 carrier front-door probe update

**Date:** 2026-08-05  
**Trigger:** independent CC NARROW return on TRACE PR #26  
**Scope:** executable front-door drift probes only  

The original `D19` and `D20` assertions described the pre-carrier repository state: the active released formal seed preceded an older v0.5 `TRACE.pdf`, and that PDF was labelled as older. PR #26 intentionally replaces that artifact with a current v0.2.7 rendered carrier.

The probes are therefore re-pointed, not deleted:

```text
D19  active released v0.2.7 baseline precedes TRACE.pdf
D20  TRACE.pdf is labelled as current rendered carrier and Markdown remains formal source
A15  complete required surface remains error-free
M19  removing the current-carrier authority label is detected
```

The formal seed and PDF binary are unchanged by this repair. Historical audit reports remain historical evidence of the state they tested. The executable v0.2.7 instrument now targets the post-carrier repository state.

```text
PROBE_UPDATE != PROBE_RETIREMENT
RENDERED_CARRIER != FORMAL_SOURCE
GREEN_X100 != VALIDATION
```
''',
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
