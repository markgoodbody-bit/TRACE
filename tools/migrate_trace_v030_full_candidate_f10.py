#!/usr/bin/env python3
"""Fail-closed F10 migration for TRACE v0.3.0 full-candidate compiler.

Repairs packet/carrier survival of load-bearing limits using existing LIMIT
representation and an optional packet limit_refs binding. This script changes
compiler source only; the deterministic compiler must regenerate the candidate.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "tools" / "compile_trace_v030_full_candidate.py"


class MigrationError(RuntimeError):
    pass


def replace_once(text: str, anchor: str, replacement: str, name: str) -> str:
    count = text.count(anchor)
    if count != 1:
        raise MigrationError(f"{name}: expected anchor count 1, observed {count}")
    return text.replace(anchor, replacement, 1)


def main() -> int:
    text = PATH.read_text(encoding="utf-8")
    original = text

    supplemental_anchor = '''    "CHILD_GRAPH_MERGED + CHILD_LIMIT_DROPPED != RECURSIVE_INTEGRATION",
)
'''
    supplemental_replacement = '''    "CHILD_GRAPH_MERGED + CHILD_LIMIT_DROPPED != RECURSIVE_INTEGRATION",
    "CAN_SERIALIZE_LIMIT_DETAIL != LIMIT_DETAIL_SURVIVED",
    "LIMIT_VISIBLE_IN_ANALYSIS != LIMIT_CARRIED_IN_PACKET",
    "UNRESOLVED_CLAIM_RECORDED != LIMIT_CAUSE_RECORDED",
    "LIMIT_TEXT_PRESENT != LIMIT_PROVENANCE_PRESERVED",
    "SCHEMA_VALID_LIMITS != SEMANTIC_LIMIT_SURVIVAL",
    "INTERNAL_L_MERGED != CANONICAL_PACKET_L_CARRIED",
)
'''
    text = replace_once(text, supplemental_anchor, supplemental_replacement, "F10 supplemental guards")

    survival_anchor = '''    "GRAPH_CONTRIBUTION_SURVIVED != QUALIFYING_LIMIT_SURVIVED",
)
'''
    survival_replacement = '''    "GRAPH_CONTRIBUTION_SURVIVED != QUALIFYING_LIMIT_SURVIVED",
    "CAN_SERIALIZE_LIMIT_DETAIL != LIMIT_DETAIL_SURVIVED",
    "LIMIT_VISIBLE_IN_ANALYSIS != LIMIT_CARRIED_IN_PACKET",
    "UNRESOLVED_CLAIM_RECORDED != LIMIT_CAUSE_RECORDED",
    "LIMIT_TEXT_PRESENT != LIMIT_PROVENANCE_PRESERVED",
    "SCHEMA_VALID_LIMITS != SEMANTIC_LIMIT_SURVIVAL",
    "INTERNAL_L_MERGED != CANONICAL_PACKET_L_CARRIED",
)
'''
    text = replace_once(text, survival_anchor, survival_replacement, "F10 survival propagation")

    operator_anchor = '''    emit_packet_use_state(R)
    emit_confidence_and_limits(R, L)
    validate_schema(R, "TRACE-GRAPH-0.3.0")
'''
    operator_replacement = '''    emit_packet_use_state(R)
    material_limit_refs <- serialize_load_bearing_limits_with_provenance(R, L)
    bind_packet_limit_refs(R, material_limit_refs)
    emit_confidence_and_limits(R, L, material_limit_refs)
    validate_schema(R, "TRACE-GRAPH-0.3.0")
'''
    text = replace_once(text, operator_anchor, operator_replacement, "F10 operator binding")

    binding_anchor = '''These are semantic use rules. They do not add required minimum-schema fields.

"""
    b.insert_before_once("T_PACKET_BINDING", "## [14.2] Packet-use boundary\\n", binding_add)
'''
    binding_replacement = '''These are semantic use rules. They do not add required minimum-schema fields.

### [14.1.1] Load-bearing limit carrier survival

If an item in `L` is load-bearing because losing its kind, target/scope, basis
or provenance could change a downstream claim, coverage/window/transition view,
confidence statement or correction/repair route, canonical packet emission must
carry that distinction rather than summarize it away.

Use the existing `LIMIT` node type and stable node identity. Its existing open
attributes may carry, where available:

```text
limit_kind
description
target_refs
scope_refs
basis_claim_refs
aperture_refs
clock_refs
route_or_handoff_refs
recursive_parent_target_ref
source_limit_refs
```

The packet `limits` object may expose optional `limit_refs` pointing to those
carried `LIMIT` node ids. Derived confidence, coverage, correction-window and
transition views may reference the same carried limit ids. Missing or unsupported
fields remain unresolved; do not invent provenance merely to fill the profile.

Do not deduplicate materially distinct limits merely because their prose summary
or unresolved-claim set is identical. If limit kind/provenance changes the next
repair route, that distinction is load-bearing and must survive the carrier.

```text
CAN_SERIALIZE_LIMIT_DETAIL != LIMIT_DETAIL_SURVIVED
LIMIT_VISIBLE_IN_ANALYSIS != LIMIT_CARRIED_IN_PACKET
UNRESOLVED_CLAIM_RECORDED != LIMIT_CAUSE_RECORDED
LIMIT_TEXT_PRESENT != LIMIT_PROVENANCE_PRESERVED
SCHEMA_VALID_LIMITS != SEMANTIC_LIMIT_SURVIVAL
INTERNAL_L_MERGED != CANONICAL_PACKET_L_CARRIED
MINIMUM_SCHEMA_PASS != SEMANTIC_LIMIT_SURVIVAL
```

This is an existing-object serialization/binding profile, not a new primitive
and not a required minimum-schema expansion.

"""
    b.insert_before_once("T_PACKET_BINDING", "## [14.2] Packet-use boundary\\n", binding_add)

    packet_limits_old = """  limits:
    receiver_limits: []
    unavailable_evidence: []
    unresolved_claim_refs: []
    omitted_primitive_effects: []
"""
    packet_limits_new = """  limits:
    receiver_limits: []
    unavailable_evidence: []
    unresolved_claim_refs: []
    omitted_primitive_effects: []
    limit_refs: []
"""
    b.replace_once("T_LIMIT_CARRIER_SURVIVAL", packet_limits_old, packet_limits_new)
'''
    text = replace_once(text, binding_anchor, binding_replacement, "F10 packet semantic binding")

    required_anchor = '''        "merge_limits_with_recursive_provenance",
    )
'''
    required_replacement = '''        "merge_limits_with_recursive_provenance",
        "CAN_SERIALIZE_LIMIT_DETAIL != LIMIT_DETAIL_SURVIVED",
        "SCHEMA_VALID_LIMITS != SEMANTIC_LIMIT_SURVIVAL",
        "INTERNAL_L_MERGED != CANONICAL_PACKET_L_CARRIED",
        "serialize_load_bearing_limits_with_provenance",
        "bind_packet_limit_refs",
        "emit_confidence_and_limits(R, L, material_limit_refs)",
        "    limit_refs: []",
        "recursive_parent_target_ref",
        "source_limit_refs",
    )
'''
    text = replace_once(text, required_anchor, required_replacement, "F10 required output tokens")

    bad_control_anchor = '''        "R <- merge_graphs(R, TRACE(target, aperture, history,",
    )
'''
    bad_control_replacement = '''        "R <- merge_graphs(R, TRACE(target, aperture, history,",
        "    emit_confidence_and_limits(R, L)\\n",
    )
'''
    text = replace_once(text, bad_control_anchor, bad_control_replacement, "F10 stale generic emission rejection")

    doc_anchor = '''packet binding without shape expansion
worked-case regression tightening
'''
    doc_replacement = '''packet binding + load-bearing limit carrier survival without minimum-shape expansion
worked-case regression tightening
'''
    text = replace_once(text, doc_anchor, doc_replacement, "F10 document-control accounting")

    if text == original:
        raise MigrationError("F10 migration produced no compiler delta")

    PATH.write_text(text, encoding="utf-8")
    print("F10 migration applied: compiler source changed fail-closed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())