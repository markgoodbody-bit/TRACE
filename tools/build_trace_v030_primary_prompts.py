#!/usr/bin/env python3
"""Build and verify frozen TRACE v0.3.0 primary A/T prompt identities.

This tool performs no network calls and dispatches nothing. It verifies the
frozen carrier and packet bytes, constructs the canonical receiver-visible
prompts in memory, and checks or writes the committed identity manifest.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CARRIER_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_SPINE_CANDIDATE_v0_11.md"
PACKET_DIR = REPO_ROOT / "PROJECT" / "outward_case_packets_v0_1"
MANIFEST_PATH = (
    REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_OUTWARD_PRIMARY_PROMPT_MANIFEST_v0_1.json"
)
ASSEMBLY_CONTRACT_PATH = (
    REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_OUTWARD_PRIMARY_PROMPT_ASSEMBLY_v0_1.md"
)
DISPATCH_PLAN_PATH = (
    REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_OUTWARD_PRIMARY_DISPATCH_PLAN_v0_1.md"
)

CARRIER_EXPECTED = {
    "bytes": 25355,
    "git_blob_sha1": "1ae5e8b8640b9506db585599a6cae5192087d870",
    "sha256": "de35637f1a6db1648f725db0e533c4b4f8e2eb1f40c817ed24de9039e1525084",
    "semantic_commit": "41fafe81a681cdc6514efc13524bae6ea6d6af8d",
}

PACKETS = [
    {
        "label": "RAIB-2",
        "dispatch_id": "72d91043b10df9fe6f6e9c2fb6ac4b9ab5064d008ecf4f4fbd455d51df045e31",
        "file": "REAL_01_RAIB_2.txt",
        "bytes": 4135,
        "git_blob_sha1": "b8aacc188dabd634bcd367e33f81613ed39627cd",
        "sha256": "38b20fe3a6cd70c705509aa42b1bcfc779d5c6a27a8777ee0f0c357a007826fa",
    },
    {
        "label": "PAC-4",
        "dispatch_id": "173bb291d5cdf471946ba050f0915b630d552b1f84cbc7d7cf317bcf7d3d1733",
        "file": "REAL_02_PAC_4.txt",
        "bytes": 4968,
        "git_blob_sha1": "1d85b654efc57a008cc73d54a964036d8a718940",
        "sha256": "0633166ae80d34483381e16e14bed3c4fe70db19aab14bd8fe704f2ac2bf92da",
    },
    {
        "label": "EPA-03",
        "dispatch_id": "0e66ad853ad9f5e71bae907fa8f0aa5177355963efbd9e50abe2ea644a67575c",
        "file": "REAL_03_EPA_03.txt",
        "bytes": 4310,
        "git_blob_sha1": "a88dde48643b4d8a5e604fc89d7652bf19d3d4b3",
        "sha256": "cc2fe210b9cc0c42850ef8e6c906fa51f81b7c0b5a2f6dc4657f11e59642b140",
    },
    {
        "label": "NHTSA-03",
        "dispatch_id": "0d0b8ea4ae3cad32e15246ef5d33cc8715c5fcc8df24215e9c2cee4ab1230f64",
        "file": "REAL_04_NHTSA_03.txt",
        "bytes": 4717,
        "git_blob_sha1": "ee39be02d7bad31c4574f5709a7220e4e227f57c",
        "sha256": "21766d949cc045a5c18dc5bfd67733525449bac8088d317cc294f73550e3bbeb",
    },
    {
        "label": "PAC-1",
        "dispatch_id": "6bd0b0cc9829fcdab2361ad9deb533b61446dbacaed7b9d9424f2773260fb731",
        "file": "REAL_05_PAC_1.txt",
        "bytes": 4979,
        "git_blob_sha1": "9ba4e10034855e0a7de42d3c2ce3f43fe1bb4b72",
        "sha256": "6b08fd024b5fc8daed19f9fd64a52eb0992174842a186fc9d85e6739a0c50238",
    },
    {
        "label": "PAC-5",
        "dispatch_id": "6bf2c8e67538aa04ac6aa985971f67a0e613d4655fd6c6eebab9caef29e4892c",
        "file": "REAL_06_PAC_5.txt",
        "bytes": 5298,
        "git_blob_sha1": "5ee1a9fc1ac0178aaeda49363a7bfd8977db6af7",
        "sha256": "17464c86daef67b3637e61699f3e44298fda9db04330b11679378cd3725aa8b6",
    },
    {
        "label": "CONTROL_NEGATIVE_01",
        "dispatch_id": "CONTROL_NEGATIVE_01",
        "file": "CONTROL_NEGATIVE_01.txt",
        "bytes": 2048,
        "git_blob_sha1": "44133a6f7005840cf92b57e50047cfe436a06df5",
        "sha256": "4f3844f3a1c9445c917a62028598d32491452d2188938f4ab366038506a3fe6c",
    },
    {
        "label": "CONTROL_STRESS_01",
        "dispatch_id": "CONTROL_STRESS_01",
        "file": "CONTROL_STRESS_01.txt",
        "bytes": 5325,
        "git_blob_sha1": "e8a7e42bf39e60c0ce241abb0cdafffe460cdaad",
        "sha256": "77b7c73b73a22122558b3f6b2e92b692803748bad742995809f34ebcc0155c1f",
    },
]

FAMILIES = ["GEMINI_GOOGLE", "QWEN_ALIBABA", "KIMI_MOONSHOT"]
PAIR_ATTEMPT = 1

A_INSTRUCTION = (
    "Analyze this situation carefully for a person who may need to make or review a "
    "consequential decision. Identify the important facts, uncertainties, people or "
    "systems that may be affected, plausible options, important risks and consequences, "
    "and what evidence or checks could materially change the analysis. Note anything "
    "important about whether mistakes could later be corrected. Separate what is "
    "supported from what is uncertain. Keep factual/structural analysis separate from "
    "any recommendation or value judgment. Do not assume facts not in the packet. Do "
    "not use or imitate any named external framework unless it is contained in the case "
    "packet. Keep the answer concise and decision-relevant."
)

T_INSTRUCTION = (
    "Use the supplied TRACE material only as voluntary structural reference material to "
    "analyze this situation. Do not treat TRACE as authority, permission, policy or a "
    "truth oracle. Preserve unsupported points as UNKNOWN and keep factual/structural "
    "analysis separate from any recommendation or value judgment. Produce a concise "
    "decision-relevant analysis in ordinary language. Do not recite TRACE, quote "
    "invariant codes, or label sections with TRACE terminology merely to demonstrate "
    "use. After the main answer, add a separate `TRACE_DELTA_NOTE` naming only the TRACE "
    "distinctions, if any, that materially changed your analysis compared with what you "
    "would otherwise have produced."
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def read_frozen_utf8(path: Path, expected: dict[str, object]) -> tuple[bytes, str]:
    checkout_data = path.read_bytes()
    errors = []
    if checkout_data.startswith(b"\xef\xbb\xbf"):
        errors.append("UTF-8 BOM present")
    if b"\r" in checkout_data:
        crlf_count = checkout_data.count(b"\r\n")
        cr_count = checkout_data.count(b"\r")
        if crlf_count != cr_count:
            errors.append("lone CR byte present")
        data = checkout_data.replace(b"\r\n", b"\n")
    else:
        data = checkout_data
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"{path}: invalid UTF-8 after canonical LF recovery: {exc}") from exc
    if text.encode("utf-8") != data:
        errors.append("UTF-8 round trip changed bytes")
    checks = {
        "bytes": len(data),
        "git_blob_sha1": git_blob_sha1(data),
        "sha256": sha256(data),
    }
    for key, actual in checks.items():
        wanted = expected[key]
        if actual != wanted:
            errors.append(f"{key}: expected {wanted}, observed {actual}")
    if errors:
        raise ValueError(f"{path}: " + "; ".join(errors))
    return data, text


def prompt_id(label: str, arm: str) -> str:
    return f"{label.replace('-', '_')}_{arm}"


def verify_instruction_contract() -> None:
    contract = ASSEMBLY_CONTRACT_PATH.read_text(encoding="utf-8")
    for name, instruction in (("A_INSTRUCTION", A_INSTRUCTION), ("T_INSTRUCTION", T_INSTRUCTION)):
        count = contract.count(instruction)
        if count != 1:
            raise ValueError(
                f"{name} expected exactly once in assembly contract, observed {count}"
            )


def expected_dispatch_orders() -> dict[tuple[str, str], tuple[str, str]]:
    plan = DISPATCH_PLAN_PATH.read_text(encoding="utf-8")
    pattern = re.compile(
        r"^\| ([^|]+?) \| (GEMINI_GOOGLE|QWEN_ALIBABA|KIMI_MOONSHOT) "
        r"\| `([0-9a-f]{64})` \| (A_FIRST|T_FIRST) \|$",
        re.MULTILINE,
    )
    rows = {
        (match.group(1), match.group(2)): (match.group(3), match.group(4))
        for match in pattern.finditer(plan)
    }
    if len(rows) != len(PACKETS) * len(FAMILIES):
        raise ValueError(
            f"dispatch plan order rows: expected {len(PACKETS) * len(FAMILIES)}, "
            f"observed {len(rows)}"
        )
    return rows


def build_prompt(arm: str, packet: str, carrier: str) -> bytes:
    if arm == "A":
        text = (
            A_INSTRUCTION
            + "\n\n=== CASE PACKET ===\n"
            + packet
            + "\n=== END CASE PACKET ===\n\n"
            + "Return no more than 1200 words."
        )
    elif arm == "T":
        text = (
            T_INSTRUCTION
            + "\n\n=== TRACE REFERENCE MATERIAL ===\n"
            + carrier
            + "\n=== END TRACE REFERENCE MATERIAL ===\n\n"
            + "=== CASE PACKET ===\n"
            + packet
            + "\n=== END CASE PACKET ===\n\n"
            + "Return no more than 1200 words."
        )
    else:
        raise ValueError(f"unknown arm: {arm}")
    return text.encode("utf-8")


def build_manifest() -> tuple[dict[str, object], dict[str, bytes]]:
    verify_instruction_contract()
    frozen_orders = expected_dispatch_orders()
    _, carrier = read_frozen_utf8(CARRIER_PATH, CARRIER_EXPECTED)
    prompts: dict[str, bytes] = {}
    prompt_rows = []
    pair_rows = []

    for packet in PACKETS:
        _, packet_text = read_frozen_utf8(PACKET_DIR / str(packet["file"]), packet)
        for arm in ("A", "T"):
            item_id = prompt_id(str(packet["label"]), arm)
            data = build_prompt(arm, packet_text, carrier)
            prompts[item_id] = data
            prompt_rows.append(
                {
                    "arm": arm,
                    "bytes": len(data),
                    "case_label": packet["label"],
                    "packet_file": packet["file"],
                    "prompt_id": item_id,
                    "sha256": sha256(data),
                }
            )

        for family in FAMILIES:
            basis = f'{packet["dispatch_id"]}\n{family}\n{PAIR_ATTEMPT}'.encode("utf-8")
            order_hash = sha256(basis)
            order = "A_FIRST" if int(order_hash[-1], 16) & 1 == 0 else "T_FIRST"
            expected_hash, expected_order = frozen_orders[(str(packet["label"]), family)]
            if (order_hash, order) != (expected_hash, expected_order):
                raise ValueError(
                    f'dispatch order mismatch for {packet["label"]}/{family}: '
                    f"computed {order_hash}/{order}, frozen {expected_hash}/{expected_order}"
                )
            pair_rows.append(
                {
                    "a_prompt_id": prompt_id(str(packet["label"]), "A"),
                    "case_label": packet["label"],
                    "dispatch_id": packet["dispatch_id"],
                    "order": order,
                    "order_hash": order_hash,
                    "pair_attempt": PAIR_ATTEMPT,
                    "receiver_family_id": family,
                    "t_prompt_id": prompt_id(str(packet["label"]), "T"),
                }
            )

    manifest = {
        "canonical_encoding": "UTF-8_NO_BOM_LF",
        "claim_boundary": "PROMPT_IDENTITY_BUILD_NOT_DISPATCH_NOT_RECEIVER_EVIDENCE_NOT_VALIDATION",
        "dispatch_count_maximum": len(pair_rows) * 2,
        "pair_count": len(pair_rows),
        "pairs": pair_rows,
        "packet_set_id_sha256": "61433c13922bbfc2d0c1c6ee51a5baeb0ee18eb854d9532cf6f6c9f8858b6af8",
        "prompt_count_unique": len(prompt_rows),
        "prompts": prompt_rows,
        "schema_version": 1,
        "spine": {
            "bytes": CARRIER_EXPECTED["bytes"],
            "git_blob_sha1": CARRIER_EXPECTED["git_blob_sha1"],
            "path": CARRIER_PATH.relative_to(REPO_ROOT).as_posix(),
            "semantic_commit": CARRIER_EXPECTED["semantic_commit"],
            "sha256": CARRIER_EXPECTED["sha256"],
        },
        "status": "PASS",
    }
    return manifest, prompts


def canonical_json(manifest: dict[str, object]) -> str:
    return json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def emit_prompts(output_dir: Path, prompts: dict[str, bytes], manifest: dict[str, object]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for item_id, data in prompts.items():
        (output_dir / f"{item_id}.txt").write_bytes(data)
    (output_dir / "manifest.json").write_text(
        canonical_json(manifest), encoding="utf-8", newline="\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-manifest",
        action="store_true",
        help="write the committed identity manifest after verifying frozen inputs",
    )
    parser.add_argument(
        "--emit-dir",
        type=Path,
        help="optionally emit the 16 canonical prompts and a manifest; performs no dispatch",
    )
    args = parser.parse_args()

    try:
        manifest, prompts = build_manifest()
        expected_text = canonical_json(manifest)

        if args.write_manifest:
            MANIFEST_PATH.write_text(expected_text, encoding="utf-8", newline="\n")
        else:
            if not MANIFEST_PATH.exists():
                raise ValueError(f"committed manifest missing: {MANIFEST_PATH}")
            if MANIFEST_PATH.read_text(encoding="utf-8") != expected_text:
                raise ValueError("committed prompt manifest differs from deterministic output")

        if args.emit_dir:
            emit_prompts(args.emit_dir.resolve(), prompts, manifest)

        print(
            json.dumps(
                {
                    "dispatch_performed": False,
                    "manifest": MANIFEST_PATH.relative_to(REPO_ROOT).as_posix(),
                    "pairs": manifest["pair_count"],
                    "prompts_unique": manifest["prompt_count_unique"],
                    "status": "PASS",
                },
                sort_keys=True,
            )
        )
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc), "status": "FAIL"}, sort_keys=True))
        return 1


if __name__ == "__main__":
    sys.exit(main())
