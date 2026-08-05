#!/usr/bin/env python3
"""Build and verify the TRACE v0.2.7 rendered formal carrier.

The released Markdown seed remains the formal object. This script applies exactly
two presentation-only line-break repairs, prepends the carrier front matter, and
renders the resulting wrapper with Pandoc/XeLaTeX.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
FORMAL = ROOT / "TRACE_FORMAL_SEED_v0_2_7.md"
FRONT = ROOT / "carrier" / "trace_v027_carrier_front.md"
HEADER = ROOT / "carrier" / "trace_v027_carrier_header.tex"
WRAPPER = ROOT / "carrier" / "TRACE_v0_2_7_RENDERED_CARRIER_SOURCE.md"
MANIFEST = ROOT / "carrier" / "trace_v027_carrier_manifest.json"
COMMITTED_PDF = ROOT / "TRACE.pdf"

FORMAL_SHA256 = "de21182f42228a0104181fb24f245c652c3150853e14172c4174be4bb9ef03ab"
FORMAL_BLOB = "9238986ddc18c34709906b2fc4510d827c68d2b2"
EXPECTED_PAGES = 75
EXPECTED_NORMALIZED_TEXT_SHA256 = "2135547767b1e14963ad9c286aeb647ad5cedc0762f9a6aa9513849aacd77442"

TABLE_OLD = r"| \(\mathbf T\) | clocks | detection/routing/correction/hardening times | `CLOCKS` |"
TABLE_NEW = r"| \(\mathbf T\) | clocks | \makecell[l]{detection/routing/\\correction/hardening\\times} | `CLOCKS` |"

EQUATION_OLD = r"""&\operatorname{COST\_UP}_{\theta}(\gamma,\gamma')
\lor
\operatorname{RECOVERABILITY\_DOWN}_{\theta}(\gamma,\gamma')
\lor
\operatorname{CONTROL\_DOWN}_{\theta}(\gamma,\gamma')\\
&\lor
\operatorname{DEPENDENCY\_UP}_{\theta}(\gamma,\gamma')
\lor
\operatorname{INFORMATION\_BARRIER\_UP}_{\theta}(\gamma,\gamma')
\big)
\Rightarrow"""
EQUATION_NEW = r"""&\operatorname{COST\_UP}_{\theta}(\gamma,\gamma')
\lor
\operatorname{RECOVERABILITY\_DOWN}_{\theta}(\gamma,\gamma')\\
&\lor
\operatorname{CONTROL\_DOWN}_{\theta}(\gamma,\gamma')
\lor
\operatorname{DEPENDENCY\_UP}_{\theta}(\gamma,\gamma')\\
&\lor
\operatorname{INFORMATION\_BARRIER\_UP}_{\theta}(\gamma,\gamma')
\big)\\
&\Rightarrow"""

KEY_TOKENS = [
    *(f"I{i:02d}" for i in range(1, 61)),
    "TRACE-GRAPH-0.2.7",
    "TARGET_SET != WORLD_SCOPE",
    "PROFILE_CONFORMANCE != TARGET_DISCOVERY",
    "TRACE_OUTPUT != MAP_UPDATE",
    "COMMITMENT_RECEIPT != CLEARANCE",
    "That is the bid.",
    FORMAL_BLOB,
    FORMAL_SHA256,
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("−", "-").replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", text).strip()


def checked_replace(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one source match, found {count}")
    return text.replace(old, new, 1)


def generate_wrapper() -> str:
    formal_bytes = FORMAL.read_bytes()
    if sha256_bytes(formal_bytes) != FORMAL_SHA256:
        raise RuntimeError("formal source SHA-256 mismatch")
    if git_blob_sha1(formal_bytes) != FORMAL_BLOB:
        raise RuntimeError("formal source Git blob mismatch")
    body = formal_bytes.decode("utf-8")
    body = checked_replace(body, TABLE_OLD, TABLE_NEW, "core-glyph table line break")
    body = checked_replace(body, EQUATION_OLD, EQUATION_NEW, "hardening equation line break")
    return FRONT.read_text(encoding="utf-8").rstrip() + "\n" + body


def check_wrapper() -> None:
    expected = generate_wrapper()
    actual = WRAPPER.read_text(encoding="utf-8")
    if actual != expected:
        raise RuntimeError("committed carrier wrapper differs from deterministic generation")


def extract_pdf_text(pdf: Path) -> str:
    proc = subprocess.run(
        ["pdftotext", "-layout", str(pdf), "-"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return proc.stdout.decode("utf-8", errors="replace")


def verify_pdf(pdf: Path, require_exact_binary: bool) -> dict:
    try:
        import fitz  # type: ignore
        from PIL import Image  # type: ignore
    except ImportError as exc:
        raise RuntimeError("PyMuPDF and Pillow are required for carrier verification") from exc

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    raw = pdf.read_bytes()
    report: dict[str, object] = {
        "pdf": str(pdf),
        "sha256": sha256_bytes(raw),
        "git_blob": git_blob_sha1(raw),
        "size_bytes": len(raw),
    }
    if require_exact_binary and report["sha256"] != manifest["pdf_sha256"]:
        raise RuntimeError("committed PDF SHA-256 mismatch")

    doc = fitz.open(pdf)
    report["pages"] = doc.page_count
    if doc.page_count != EXPECTED_PAGES:
        raise RuntimeError(f"page count mismatch: {doc.page_count} != {EXPECTED_PAGES}")

    non_a4: list[int] = []
    blank_pages: list[int] = []
    tight_pages: list[dict[str, object]] = []
    minimum_margins = {"left": 10**9, "right": 10**9, "top": 10**9, "bottom": 10**9}
    scale = 100 / 72
    for i, page in enumerate(doc):
        rect = page.rect
        if abs(rect.width - 595.28) > 1 or abs(rect.height - 841.89) > 1:
            non_a4.append(i + 1)
        pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), colorspace=fitz.csGRAY, alpha=False)
        image = Image.frombytes("L", [pix.width, pix.height], pix.samples)
        mask = image.point(lambda x: 255 if x < 245 else 0)
        bbox = mask.getbbox()
        if bbox is None:
            blank_pages.append(i + 1)
            continue
        margins = {
            "left": bbox[0],
            "top": bbox[1],
            "right": image.width - bbox[2],
            "bottom": image.height - bbox[3],
        }
        for key, value in margins.items():
            minimum_margins[key] = min(minimum_margins[key], value)
        if min(margins.values()) < 12:
            tight_pages.append({"page": i + 1, "margins_px_at_100dpi": margins})
    doc.close()
    if non_a4:
        raise RuntimeError(f"non-A4 pages: {non_a4}")
    if blank_pages:
        raise RuntimeError(f"blank pages: {blank_pages}")
    if tight_pages:
        raise RuntimeError(f"page content too close to edge: {tight_pages}")
    report["all_pages_a4"] = True
    report["blank_pages"] = blank_pages
    report["minimum_ink_margins_px_at_100dpi"] = minimum_margins

    font_output = subprocess.run(
        ["pdffonts", str(pdf)], check=True, stdout=subprocess.PIPE, text=True
    ).stdout
    bad_fonts = []
    for line in font_output.splitlines()[2:]:
        parts = line.split()
        if len(parts) >= 9 and parts[-5].lower() != "yes":
            bad_fonts.append(line)
    if bad_fonts:
        raise RuntimeError(f"unembedded fonts: {bad_fonts}")
    report["fonts_embedded"] = True

    text = extract_pdf_text(pdf)
    normalized = normalize_text(text)
    text_hash = sha256_bytes(normalized.encode("utf-8"))
    report["normalized_text_sha256"] = text_hash
    report["replacement_character_count"] = text.count("\ufffd")
    if text_hash != EXPECTED_NORMALIZED_TEXT_SHA256:
        raise RuntimeError("normalized extracted-text hash mismatch")
    if text.count("\ufffd"):
        raise RuntimeError("replacement characters found in extracted PDF text")

    headings = []
    for line in FORMAL.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            headings.append(re.sub(r"\{#.*?\}\s*$", "", match.group(2)).strip())
    normalized_pdf_lower = normalized.lower()
    normalized_pdf_heading_search = normalize_text(re.sub(r"[`*_\\{}$]", "", normalized)).lower()
    missing_headings = [h for h in headings if normalize_text(re.sub(r"[`*_\\{}$]", "", h)).lower() not in normalized_pdf_heading_search]
    missing_tokens = [t for t in KEY_TOKENS if normalize_text(t).lower() not in normalized_pdf_lower]
    if missing_headings:
        raise RuntimeError(f"missing headings in PDF text: {missing_headings}")
    if missing_tokens:
        raise RuntimeError(f"missing key tokens in PDF text: {missing_tokens}")
    report["heading_count"] = len(headings)
    report["missing_headings"] = []
    report["key_token_count"] = len(KEY_TOKENS)
    report["missing_key_tokens"] = []
    return report


def build_pdf(output: Path) -> None:
    check_wrapper()
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="trace-v027-carrier-") as tmp_raw:
        tmp = Path(tmp_raw)
        shutil.copy2(WRAPPER, tmp / WRAPPER.name)
        shutil.copy2(HEADER, tmp / "header.tex")
        env = os.environ.copy()
        env.update({"SOURCE_DATE_EPOCH": "1785888000", "FORCE_SOURCE_DATE": "1", "TZ": "UTC"})
        cmd = [
            "pandoc",
            WRAPPER.name,
            "--from=markdown+tex_math_single_backslash+tex_math_dollars+raw_tex",
            "--pdf-engine=xelatex",
            "-o",
            str(output),
        ]
        subprocess.run(cmd, cwd=tmp, env=env, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-source", action="store_true")
    parser.add_argument("--build", type=Path)
    parser.add_argument("--verify", type=Path)
    parser.add_argument("--verify-committed", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    if not any((args.check_source, args.build, args.verify, args.verify_committed)):
        parser.error("select at least one action")

    report: dict[str, object] = {
        "formal_sha256": sha256_bytes(FORMAL.read_bytes()),
        "formal_git_blob": git_blob_sha1(FORMAL.read_bytes()),
        "wrapper_sha256": sha256_bytes(generate_wrapper().encode("utf-8")),
    }
    if args.check_source:
        check_wrapper()
        report["source_check"] = "PASS"
    if args.build:
        build_pdf(args.build)
        report["build"] = verify_pdf(args.build, require_exact_binary=False)
    if args.verify:
        report["verify"] = verify_pdf(args.verify, require_exact_binary=False)
    if args.verify_committed:
        report["committed"] = verify_pdf(COMMITTED_PDF, require_exact_binary=True)

    encoded = json.dumps(report, indent=2, sort_keys=True)
    print(encoded)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(encoded + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
