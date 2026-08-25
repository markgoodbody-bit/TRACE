#!/usr/bin/env python3
"""Build a deterministic heading/section manifest for released TRACE v0.2.7.

The manifest is a mechanical address map for full-candidate assembly. It does
not classify semantic importance or establish donor equivalence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = REPO_ROOT / "TRACE_FORMAL_SEED_v0_2_7.md"
OUTPUT_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_2_7_SECTION_MANIFEST_v0_1.json"
EXPECTED_SOURCE_SHA256 = "de21182f42228a0104181fb24f245c652c3150853e14172c4174be4bb9ef03ab"

HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.+?)\s*$")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def section_slug(title: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "-", title).strip("-").lower()
    return value or "section"


def parse_headings(text: str) -> list[dict[str, object]]:
    lines = text.splitlines(keepends=True)
    headings: list[dict[str, object]] = []
    in_fence = False
    fence_char = ""
    fence_len = 0

    for index, raw_line in enumerate(lines):
        line_no = index + 1
        stripped = raw_line.rstrip("\r\n")
        fence = FENCE_RE.match(stripped)
        if fence:
            marker = fence.group(1)
            char = marker[0]
            if not in_fence:
                in_fence = True
                fence_char = char
                fence_len = len(marker)
            elif char == fence_char and len(marker) >= fence_len:
                in_fence = False
                fence_char = ""
                fence_len = 0
            continue
        if in_fence:
            continue

        match = HEADING_RE.match(stripped)
        if match:
            headings.append(
                {
                    "level": len(match.group("marks")),
                    "title": match.group("title"),
                    "start_line": line_no,
                }
            )

    # A section ends immediately before the next heading of the same or higher
    # level. This produces nested, stable spans useful for exact donor carry.
    for i, heading in enumerate(headings):
        level = int(heading["level"])
        end_line = len(lines)
        for later in headings[i + 1 :]:
            if int(later["level"]) <= level:
                end_line = int(later["start_line"]) - 1
                break
        heading["end_line"] = end_line

        start = int(heading["start_line"]) - 1
        end = end_line
        body = "".join(lines[start:end])
        body_bytes = body.encode("utf-8")
        heading["bytes"] = len(body_bytes)
        heading["sha256"] = sha256_bytes(body_bytes)
        heading["slug"] = section_slug(str(heading["title"]))

    return headings


def make_report(text: str) -> dict[str, object]:
    source_bytes = text.encode("utf-8")
    source_sha = sha256_bytes(source_bytes)
    errors: list[str] = []
    if source_sha != EXPECTED_SOURCE_SHA256:
        errors.append(
            f"donor SHA-256 mismatch: expected {EXPECTED_SOURCE_SHA256}, observed {source_sha}"
        )

    headings = parse_headings(text)
    if not headings:
        errors.append("no headings parsed")

    # Require the major numbered donor surfaces expected by the assembly plan.
    required_titles = {
        "[0] HANDSHAKE / CLAIM CEILING",
        "[1] MIDDLE-OUT SEED",
        "[3] CANONICAL OBJECT / TYPED GRAPH",
        "[14] CANONICAL TRACE GRAPH PACKET",
        "[15] WORKED TRANSFORMATIONS",
        "[17] LIVE INTERPRETER / VALUE LAYER / SELECTOR / CONNECTED BRAKE",
        "[19] INVARIANTS / MISUSE GUARDS",
        "[20] COMPRESSION / SURVIVAL KERNEL",
    }
    observed_titles = {str(row["title"]) for row in headings}
    missing = sorted(required_titles - observed_titles)
    if missing:
        errors.append(f"required donor headings missing: {missing}")

    level_counts: dict[str, int] = {}
    for row in headings:
        key = str(row["level"])
        level_counts[key] = level_counts.get(key, 0) + 1

    return {
        "status": "PASS" if not errors else "FAIL",
        "source_path": str(SOURCE_PATH.relative_to(REPO_ROOT)),
        "source_sha256": source_sha,
        "source_bytes": len(source_bytes),
        "source_lines": len(text.splitlines()),
        "heading_count": len(headings),
        "heading_level_counts": level_counts,
        "sections": headings,
        "errors": errors,
        "claim_boundary": (
            "MECHANICAL_SECTION_ADDRESS_MAP_NOT_SEMANTIC_IMPORTANCE_"
            "NOT_EQUIVALENCE_NOT_VALIDATION"
        ),
    }


def render(report: dict[str, object]) -> str:
    return json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args(argv)

    text = SOURCE_PATH.read_text(encoding="utf-8")
    report = make_report(text)
    expected = render(report)

    if args.write:
        OUTPUT_PATH.write_text(expected, encoding="utf-8")

    if args.check:
        if not OUTPUT_PATH.exists():
            report["status"] = "FAIL"
            report.setdefault("errors", []).append("committed section manifest missing")
        elif OUTPUT_PATH.read_text(encoding="utf-8") != expected:
            report["status"] = "FAIL"
            report.setdefault("errors", []).append(
                "committed section manifest differs from deterministic output"
            )

    final = render(report)
    if args.report:
        args.report.write_text(final, encoding="utf-8")
    print(final, end="")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
