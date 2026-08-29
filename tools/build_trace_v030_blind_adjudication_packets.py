#!/usr/bin/env python3
"""Build neutral-label adjudication packets from a completed TRACE v0.3.0 A/T run.

The public packet directory deliberately excludes arm and receiver-family identity.
The arm key and TRACE_DELTA_NOTE material are written to a separate sealed directory.
Both output directories must not already exist.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import secrets
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


WORD_RE = re.compile(r"\b\w+\b", re.UNICODE)
DELTA_MARKER_RE = re.compile(r"(?im)^.*TRACE_DELTA_NOTE.*(?:\r?\n|$)")
TRACE_LABEL_RE = re.compile(r"\bTRACE\b|\bI\d{1,3}\b", re.IGNORECASE)

PACKETS = {
    "RAIB-2": ("REAL_01_RAIB_2.txt", "38b20fe3a6cd70c705509aa42b1bcfc779d5c6a27a8777ee0f0c357a007826fa"),
    "PAC-4": ("REAL_02_PAC_4.txt", "0633166ae80d34483381e16e14bed3c4fe70db19aab14bd8fe704f2ac2bf92da"),
    "EPA-03": ("REAL_03_EPA_03.txt", "cc2fe210b9cc0c42850ef8e6c906fa51f81b7c0b5a2f6dc4657f11e59642b140"),
    "NHTSA-03": ("REAL_04_NHTSA_03.txt", "21766d949cc045a5c18dc5bfd67733525449bac8088d317cc294f73550e3bbeb"),
    "PAC-1": ("REAL_05_PAC_1.txt", "6b08fd024b5fc8daed19f9fd64a52eb0992174842a186fc9d85e6739a0c50238"),
    "PAC-5": ("REAL_06_PAC_5.txt", "17464c86daef67b3637e61699f3e44298fda9db04330b11679378cd3725aa8b6"),
    "CONTROL_NEGATIVE_01": ("CONTROL_NEGATIVE_01.txt", "4f3844f3a1c9445c917a62028598d32491452d2188938f4ab366038506a3fe6c"),
    "CONTROL_STRESS_01": ("CONTROL_STRESS_01.txt", "77b7c73b73a22122558b3f6b2e92b692803748bad742995809f34ebcc0155c1f"),
}

CASE_ORDER = tuple(PACKETS)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_text(path: Path) -> str:
    """Read committed text and normalize working-tree CRLF back to frozen LF bytes."""
    return path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")


def word_count(text: str) -> int:
    return len(WORD_RE.findall(text))


def split_creditable_prefix(text: str, limit: int = 1200) -> tuple[str, str]:
    matches = list(WORD_RE.finditer(text))
    if len(matches) <= limit:
        return text, ""
    boundary = matches[limit - 1].end()
    return text[:boundary], text[boundary:]


def split_delta(text: str, expect_delta: bool) -> tuple[str, str]:
    matches = list(DELTA_MARKER_RE.finditer(text))
    if expect_delta:
        if len(matches) != 1:
            raise ValueError(f"expected exactly one TRACE_DELTA_NOTE marker, found {len(matches)}")
        marker = matches[0]
        main = text[: marker.start()].rstrip()
        delta = text[marker.start() :].strip()
        if not main or not delta:
            raise ValueError("empty main answer or delta note")
        return main, delta
    if matches:
        raise ValueError("Arm A unexpectedly contains TRACE_DELTA_NOTE")
    return text.rstrip(), ""


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def exclusive_text(path: Path, text: str) -> None:
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def exclusive_json(path: Path, value: object) -> None:
    exclusive_text(path, json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n")


def random_id(prefix: str, used: set[str]) -> str:
    while True:
        candidate = f"{prefix}-{secrets.token_hex(5).upper()}"
        if candidate not in used:
            used.add(candidate)
            return candidate


def pair_case(pair_id: str) -> str:
    parts = pair_id.split("__")
    if len(parts) < 3 or parts[-1] != "ATTEMPT_1":
        raise ValueError(f"unexpected pair id: {pair_id}")
    return parts[0]


def pair_family(pair_id: str) -> str:
    parts = pair_id.split("__")
    if len(parts) < 3:
        raise ValueError(f"unexpected pair id: {pair_id}")
    return parts[1]


def instructions() -> str:
    return """# Neutral paired-analysis adjudication instructions

You are assessing two anonymized analyses of the same frozen case packet. Do not search for the
project, source run, prompts, method, arm identity, expected winner, or matching outputs. Use only
the supplied case packet and responses. Do not guess which response used which method.

This is not a style contest. Extra length, structure, confidence, or granularity earns no credit by
itself. Credit a distinction only when it is:

1. supported by the supplied packet;
2. materially consequential to analysis, review, checking, or correction; and
3. absent from, or materially weaker in, the other response rather than merely reworded.

Synonyms and duplicate granularity count once. Preserve `UNKNOWN` where the packet cannot resolve a
claim. Record A-only and T-only differences neutrally by response label; the coordinator will unseal
arm identity later. A response marked `OUTPUT_LIMIT_VIOLATION` remains fully visible for burden,
over-fire, false-confidence, authority/value leakage, and other adverse findings. Positive gain may
be credited only from its section titled `POSITIVE-GAIN-CREDITABLE TEXT`; never credit its
non-creditable tail.

For each response assess separately:

- supported material distinctions;
- unsupported confidence or invention;
- affected-party or scope omissions;
- irrelevant structure / over-fire;
- leakage from factual or structural analysis into authority, permission, policy, or value choice;
- usable evidence, check, review, rollback, repair-window, or correction-route information;
- material usability or transfer failure.

For every proposed unique finding, name the response label, state the concrete finding, cite or
closely paraphrase its packet support, explain why it matters, and state why the other response is
not equivalent. Classify it as one of:

- `R_SCOPE` — affected-party/scope discovery or aggregation loss;
- `R_WARRANT` — evidence/warrant/currentness/verification-status collapse;
- `R_CORRECTION` — route/review/rollback/hardening/repair-window failure;
- `R_BURDEN` — burden/residue/loss survival;
- `R_AUTHORITY` — capability/description/authority/permission confusion;
- `R_OTHER` — give a specific mechanism.

Return one JSON object and no surrounding prose:

```json
{
  "packet_id": "copy from packet",
  "adjudication_boundary": {
    "used_only_supplied_material": true,
    "searched_external_material": false,
    "saw_or_inferred_arm_key": false,
    "uncertainties": []
  },
  "responses": {
    "RESPONSE_LABEL_1": {
      "supported_material_distinctions": [],
      "unsupported_or_invented": [],
      "affected_scope_omissions": [],
      "overfire_or_irrelevance": [],
      "authority_or_value_leakage": [],
      "usable_check_review_or_correction_information": [],
      "usability_or_transfer_failures": []
    },
    "RESPONSE_LABEL_2": {
      "supported_material_distinctions": [],
      "unsupported_or_invented": [],
      "affected_scope_omissions": [],
      "overfire_or_irrelevance": [],
      "authority_or_value_leakage": [],
      "usable_check_review_or_correction_information": [],
      "usability_or_transfer_failures": []
    }
  },
  "candidate_unique_findings": [
    {
      "response_label": "...",
      "finding": "...",
      "packet_support": "...",
      "material_consequence": "...",
      "other_response_equivalent": false,
      "equivalence_reason": "...",
      "class": "R_SCOPE|R_WARRANT|R_CORRECTION|R_BURDEN|R_AUTHORITY|R_OTHER",
      "confidence": "SUPPORTED|NOT_SUPPORTED|UNKNOWN"
    }
  ],
  "material_disagreements_or_unknowns": [],
  "decision_review_preference": "RESPONSE_LABEL_1|RESPONSE_LABEL_2|TIE|UNKNOWN",
  "preference_reason": "..."
}
```

Controls test boundedness and over-fire. They cannot establish a real-world retention gain.
"""


def render_response(label: str, main: str, original_words: int, violation: bool) -> tuple[str, dict[str, Any]]:
    prefix, tail = split_creditable_prefix(main)
    main_words = word_count(main)
    leak_matches = sorted(set(match.group(0) for match in TRACE_LABEL_RE.finditer(main)))
    status = "OUTPUT_LIMIT_VIOLATION" if violation else "WITHIN_OUTPUT_LIMIT"
    body = [
        f"## Response `{label}`",
        "",
        f"Original visible-answer limit status: `{status}`",
        f"Original full visible-answer words (including removed provenance note, if any): {original_words}",
        f"Blind main-answer words: {main_words}",
        f"Positive-gain-creditable words: {word_count(prefix)}",
        "",
        "### POSITIVE-GAIN-CREDITABLE TEXT",
        "",
        prefix,
    ]
    if tail:
        body.extend(
            [
                "",
                "### NON-CREDITABLE TAIL — ADVERSE/BURDEN REVIEW ONLY",
                "",
                tail,
            ]
        )
    body.append("")
    return "\n".join(body), {
        "label": label,
        "originalVisibleAnswerWords": original_words,
        "blindMainWords": main_words,
        "positiveGainCreditableWords": word_count(prefix),
        "nonCreditableTailWords": word_count(tail),
        "outputLimitViolation": violation,
        "armBlindness": "PARTIAL" if leak_matches else "NEUTRAL_LABEL_NO_EXPLICIT_TRACE_OR_INVARIANT_CODE",
        "explicitFrameworkOrInvariantTokens": leak_matches,
        "blindMainSha256": sha256_bytes(main.encode("utf-8")),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--public-dir", type=Path, required=True)
    parser.add_argument("--sealed-dir", type=Path, required=True)
    args = parser.parse_args()

    run_dir = args.run_dir.resolve()
    repo_root = args.repo_root.resolve()
    public_dir = args.public_dir.resolve()
    sealed_dir = args.sealed_dir.resolve()
    if public_dir.exists() or sealed_dir.exists():
        raise FileExistsError("public and sealed output directories must both be absent")
    if public_dir == sealed_dir or public_dir in sealed_dir.parents or sealed_dir in public_dir.parents:
        raise ValueError("public and sealed directories must be separate, non-nested paths")

    summary = read_json(run_dir / "run-summary.json")
    if summary.get("status") != "COMPLETE_UNADJUDICATED" or summary.get("completedPrimaryCalls") != 32:
        raise ValueError("source run is not the exact completed unadjudicated 32-call state")

    events = [json.loads(line) for line in (run_dir / "ledger.jsonl").read_text(encoding="utf-8").splitlines()]
    authorized = {event["jobId"]: event for event in events if event.get("type") == "primary.authorized"}
    completed = [event for event in events if event.get("type") == "primary.completed"]
    if len(authorized) != 32 or len(completed) != 32:
        raise ValueError("ledger does not contain 32 authorized and 32 completed primary events")

    packet_text: dict[str, str] = {}
    for case_id, (filename, expected_hash) in PACKETS.items():
        text = canonical_text(repo_root / "PROJECT" / "outward_case_packets_v0_1" / filename)
        actual_hash = sha256_bytes(text.encode("utf-8"))
        if actual_hash != expected_hash:
            raise ValueError(f"frozen case packet identity mismatch for {case_id}: {actual_hash}")
        packet_text[case_id] = text.rstrip()

    public_dir.mkdir(parents=True)
    packets_dir = public_dir / "packets"
    packets_dir.mkdir()
    sealed_dir.mkdir(parents=True)
    delta_dir = sealed_dir / "delta-notes"
    delta_dir.mkdir()

    used_ids: set[str] = set()
    pair_groups: dict[str, list[dict[str, Any]]] = {}
    for event in completed:
        pair_groups.setdefault(str(event["pairId"]), []).append(event)
    if len(pair_groups) != 16 or any(len(group) != 2 for group in pair_groups.values()):
        raise ValueError("expected 16 complete two-arm pairs")

    sealed_pairs: list[dict[str, Any]] = []
    public_packets: list[dict[str, Any]] = []
    packet_sources: list[tuple[str, str]] = []
    randomizer = secrets.SystemRandom()

    ordered_groups = sorted(
        pair_groups.items(),
        key=lambda item: (CASE_ORDER.index(pair_case(item[0])), pair_family(item[0])),
    )
    for source_pair_id, pair_events in ordered_groups:
        arms = {str(event["arm"]): event for event in pair_events}
        if set(arms) != {"A", "T"}:
            raise ValueError(f"pair lacks exact A/T arms: {source_pair_id}")
        case_id = pair_case(source_pair_id)
        family = pair_family(source_pair_id)
        neutral_pair_id = random_id("PAIR", used_ids)
        neutral_labels = {arm: random_id("RESPONSE", used_ids) for arm in ("A", "T")}
        display_arms = ["A", "T"]
        randomizer.shuffle(display_arms)

        response_bodies: dict[str, str] = {}
        public_response_meta: list[dict[str, Any]] = []
        sealed_response_meta: list[dict[str, Any]] = []
        for arm in ("A", "T"):
            event = arms[arm]
            job_id = str(event["jobId"])
            order = int(event["order"])
            raw_path = run_dir / "raw" / f"{order:02d}_{job_id}.txt"
            raw_bytes = raw_path.read_bytes()
            actual_raw_hash = sha256_bytes(raw_bytes)
            if actual_raw_hash != event.get("rawResponseSha256"):
                raise ValueError(f"raw response identity mismatch: {job_id}")
            raw_text = raw_bytes.decode("utf-8")
            main_answer, delta_note = split_delta(raw_text, expect_delta=(arm == "T"))
            label = neutral_labels[arm]
            body, meta = render_response(
                label,
                main_answer,
                int(event["outputWords"]),
                bool(event["over1200Words"]),
            )
            response_bodies[arm] = body
            public_response_meta.append(meta)
            delta_file = None
            delta_hash = None
            if delta_note:
                delta_file = f"{neutral_pair_id}__{label}.txt"
                delta_bytes = (delta_note + "\n").encode("utf-8")
                exclusive_text(delta_dir / delta_file, delta_note + "\n")
                delta_hash = sha256_bytes(delta_bytes)
            sealed_response_meta.append(
                {
                    "arm": arm,
                    "neutralLabel": label,
                    "sourceJobId": job_id,
                    "sourceOrder": order,
                    "sourceRawFile": raw_path.name,
                    "sourceRawSha256": actual_raw_hash,
                    "receiverFamily": family,
                    "deltaNoteFile": delta_file,
                    "deltaNoteSha256": delta_hash,
                }
            )

        packet_filename = f"{neutral_pair_id}__{case_id}.md"
        packet_parts = [
            instructions().rstrip(),
            "",
            "---",
            "",
            "# Adjudication packet",
            "",
            f"Packet ID: `{neutral_pair_id}`",
            f"Case ID: `{case_id}`",
            "",
            "## Frozen case packet",
            "",
            packet_text[case_id],
            "",
            "---",
            "",
        ]
        for arm in display_arms:
            packet_parts.extend([response_bodies[arm].rstrip(), "", "---", ""])
        packet_body = "\n".join(packet_parts).rstrip() + "\n"
        packet_path = packets_dir / packet_filename
        exclusive_text(packet_path, packet_body)
        packet_hash = sha256_bytes(packet_body.encode("utf-8"))
        packet_sources.append((packet_filename, packet_hash))
        public_packets.append(
            {
                "packetId": neutral_pair_id,
                "caseId": case_id,
                "file": f"packets/{packet_filename}",
                "bytes": len(packet_body.encode("utf-8")),
                "sha256": packet_hash,
                "responseMetadata": sorted(public_response_meta, key=lambda item: item["label"]),
            }
        )
        sealed_pairs.append(
            {
                "packetId": neutral_pair_id,
                "caseId": case_id,
                "sourcePairId": source_pair_id,
                "receiverFamily": family,
                "displayOrder": [neutral_labels[arm] for arm in display_arms],
                "responses": sorted(sealed_response_meta, key=lambda item: item["neutralLabel"]),
            }
        )

    instruction_text = instructions().rstrip() + "\n"
    exclusive_text(public_dir / "ADJUDICATOR_INSTRUCTIONS.md", instruction_text)

    sealed_value = {
        "schema": "trace-v030-blind-adjudication-sealed-key-v1",
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "claimBoundary": "SEALED_COORDINATOR_EVIDENCE_NOT_FOR_ADJUDICATORS",
        "sealNonce": secrets.token_hex(32),
        "sourceRunDirectory": str(run_dir),
        "sourceRunTreeSha256": "ab7541515ab8381515b000db291f712ca21cb2cf826bf623883c44d28f3d585c",
        "pairs": sealed_pairs,
    }
    sealed_path = sealed_dir / "sealed-arm-key.json"
    exclusive_json(sealed_path, sealed_value)
    sealed_hash = sha256_bytes(sealed_path.read_bytes())

    canonical_set = "".join(f"{name}|{digest}\n" for name, digest in sorted(packet_sources))
    public_set_id = sha256_bytes(canonical_set.encode("utf-8"))
    manifest = {
        "schema": "trace-v030-blind-adjudication-public-manifest-v1",
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "claimBoundary": "NEUTRAL_PACKETS_NOT_ADJUDICATION_NOT_EFFICACY_RESULT",
        "sourceRunTreeSha256": "ab7541515ab8381515b000db291f712ca21cb2cf826bf623883c44d28f3d585c",
        "frozenPacketSetIdSha256": "61433c13922bbfc2d0c1c6ee51a5baeb0ee18eb854d9532cf6f6c9f8858b6af8",
        "packetCount": len(public_packets),
        "packetSetIdSha256": public_set_id,
        "instructionSha256": sha256_bytes(instruction_text.encode("utf-8")),
        "sealedArmKeySha256": sealed_hash,
        "armKeyIncluded": False,
        "receiverFamilyIncluded": False,
        "deltaNotesIncluded": False,
        "packets": sorted(public_packets, key=lambda item: item["packetId"]),
    }
    exclusive_json(public_dir / "public-manifest.json", manifest)

    print(
        json.dumps(
            {
                "publicDirectory": str(public_dir),
                "sealedDirectory": str(sealed_dir),
                "publicPacketCount": len(public_packets),
                "publicPacketSetIdSha256": public_set_id,
                "sealedArmKeySha256": sealed_hash,
                "partialBlindnessResponses": sum(
                    meta["armBlindness"] == "PARTIAL"
                    for packet in public_packets
                    for meta in packet["responseMetadata"]
                ),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
