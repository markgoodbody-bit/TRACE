#!/usr/bin/env python3
"""One-shot exact migration for full-candidate coherence finding F01.

This script edits the v0.3 full-candidate compiler only when the expected
pre-repair source anchors match exactly. It is mechanical migration evidence,
not a semantic validator.
"""

from pathlib import Path

P = Path(__file__).with_name("compile_trace_v030_full_candidate.py")
text = P.read_text(encoding="utf-8")

transform_anchor = '''    b.replace_all_exact("T_VERSION_IDENTITY", "TRACE-GRAPH-0.2.7", "TRACE-GRAPH-0.3.0", expected=5)\n'''
transform_block = '''    validator_identity_old = (\n        "The v0.2.7 identifier records a narrow documentary, serialization-profile, and worked-transfer repair while the embedded minimum-schema shape remains identical to v0.2.6 after version normalization. The identifier does not imply that the minimum validator can enforce target discovery, target-set adequacy, search coverage, authority legitimacy, route execution, brake effectiveness, correction, or world correspondence.\\n\\n"\n        "A v0.2.6 packet is not silently relabelled as v0.2.7. Structural compatibility does not erase packet identity or the semantic contract under which the packet was produced."\n    )\n    validator_identity_new = (\n        "The v0.3.0 identifier marks this generated full working candidate. Its embedded minimum-schema shape remains identical to released v0.2.7 after version normalization. That compatibility does not imply that the minimum validator can enforce the v0.3 checker-external semantic bindings, target discovery, target-set adequacy, search coverage, authority legitimacy, route execution, brake effectiveness, correction, or world correspondence.\\n\\n"\n        "A v0.2.7 packet is not silently relabelled as v0.3.0. Structural compatibility does not erase packet identity or the semantic contract under which the packet was produced."\n    )\n    b.replace_once("T_VALIDATOR_IDENTITY_BOUNDARY", validator_identity_old, validator_identity_new)\n\n'''

if transform_block not in text:
    if text.count(transform_anchor) != 1:
        raise SystemExit(f"F01 transform anchor count != 1: {text.count(transform_anchor)}")
    text = text.replace(transform_anchor, transform_block + transform_anchor, 1)

required_anchor = '''        "This generated object is **TRACE v0.3.0 FULL WORKING CANDIDATE v0.1**.,\n'''
# The exact source does not contain the malformed anchor above; use the real
# line below while keeping the first value as a tripwire against accidental
# quote editing in this migration script.
required_anchor = '''        "This generated object is **TRACE v0.3.0 FULL WORKING CANDIDATE v0.1**.",\n'''
required_new = required_anchor + '''        "A v0.2.7 packet is not silently relabelled as v0.3.0.",\n'''
if '''        "A v0.2.7 packet is not silently relabelled as v0.3.0.",\n''' not in text:
    if text.count(required_anchor) != 1:
        raise SystemExit(f"F01 required-token anchor count != 1: {text.count(required_anchor)}")
    text = text.replace(required_anchor, required_new, 1)

bad_anchor = '''    bad_control = (\n        "v0.3.0 released baseline",\n        "v0.3.0 is released",\n        "v0.3.0 canonical baseline",\n    )\n'''
bad_new = '''    bad_control = (\n        "v0.3.0 released baseline",\n        "v0.3.0 is released",\n        "v0.3.0 canonical baseline",\n        "The v0.2.7 identifier records a narrow documentary",\n        "A v0.2.6 packet is not silently relabelled as v0.2.7.",\n    )\n'''
if bad_new not in text:
    if text.count(bad_anchor) != 1:
        raise SystemExit(f"F01 stale-control anchor count != 1: {text.count(bad_anchor)}")
    text = text.replace(bad_anchor, bad_new, 1)

P.write_text(text, encoding="utf-8")
print("F01 compiler migration applied or already present exactly.")
