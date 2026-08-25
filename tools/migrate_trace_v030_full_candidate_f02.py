#!/usr/bin/env python3
"""One-shot exact migration for full-candidate coherence finding F02.

Edits only the deterministic v0.3 compiler and fails closed unless the expected
pre-repair compiler anchors are present exactly. This script is migration
evidence, not semantic validation.
"""

from pathlib import Path

P = Path(__file__).with_name("compile_trace_v030_full_candidate.py")
text = P.read_text(encoding="utf-8")

# 1. Propagate the two compression-critical F02 guards.
supp_anchor = '''    "SAME_PATH_LABEL != SAME_TRAJECTORY",\n)\n\nSURVIVAL_REQUIRED = (\n'''
supp_new = '''    "SAME_PATH_LABEL != SAME_TRAJECTORY",\n    "BRAKE_POINT_ESTIMATE_BEFORE_COMMIT != GUARANTEED_PRECOMMIT",\n    "ROLLBACK_POINT_ESTIMATE_BEFORE_BOUNDARY != GUARANTEED_RESTORATION",\n    "FAST_ENOUGH_CLAIM_REQUIRES_COMMON_TEMPORAL_BASIS",\n    "ROLLBACK_COMPLETED_BEFORE_BOUNDARY != RESTORED_STATE",\n)\n\nSURVIVAL_REQUIRED = (\n'''
if '    "BRAKE_POINT_ESTIMATE_BEFORE_COMMIT != GUARANTEED_PRECOMMIT",\n    "ROLLBACK_POINT_ESTIMATE_BEFORE_BOUNDARY != GUARANTEED_RESTORATION",\n' not in text.split('SURVIVAL_REQUIRED = (', 1)[0]:
    if text.count(supp_anchor) != 1:
        raise SystemExit(f"F02 supplemental anchor count != 1: {text.count(supp_anchor)}")
    text = text.replace(supp_anchor, supp_new, 1)

survival_anchor = '''    "LOCAL_CORRECTION + STREAM_PERSISTENCE != MECHANISM_CHANGE",\n)\n\n\ndef sha256_bytes'''
survival_new = '''    "LOCAL_CORRECTION + STREAM_PERSISTENCE != MECHANISM_CHANGE",\n    "BRAKE_POINT_ESTIMATE_BEFORE_COMMIT != GUARANTEED_PRECOMMIT",\n    "ROLLBACK_COMPLETED_BEFORE_BOUNDARY != RESTORED_STATE",\n)\n\n\ndef sha256_bytes'''
if text.count('    "BRAKE_POINT_ESTIMATE_BEFORE_COMMIT != GUARANTEED_PRECOMMIT",') < 2:
    if text.count(survival_anchor) != 1:
        raise SystemExit(f"F02 survival anchor count != 1: {text.count(survival_anchor)}")
    text = text.replace(survival_anchor, survival_new, 1)

# 2. Insert one named transform after T_CLOCK_ROUTE and before record/residue.
insert_anchor = '''    record_guard = """\n'''
transform_marker = '    brake_rollback_old = r"""## [8.8] Pre-commit brake and post-commit rollback\n'
if transform_marker not in text:
    if text.count(insert_anchor) != 1:
        raise SystemExit(f"F02 transform insertion anchor count != 1: {text.count(insert_anchor)}")
    transform = r'''    brake_rollback_old = r"""## [8.8] Pre-commit brake and post-commit rollback

A pre-commit brake succeeds only if detection, decision, and actuation complete before commitment:

\[
t_{brake}^{done}<t_{commit}
\]

A post-commit rollback is distinct. It can preserve the threatened path only where rollback is executable and:

\[
t_{rollback}^{done}<t_{irreversible}
\]

```text
REVIEW_AFTER_COMMITMENT != PRECOMMIT_BRAKE
ROLLBACK_LISTED != ROLLBACK_EXECUTABLE
ROLLBACK_AFTER_IRREVERSIBILITY != RESTORATION
```

"""
    brake_rollback_new = r"""## [8.8] Pre-commit brake and post-commit rollback

A pre-commit brake supports a strong timing claim only when detection, decision,
and actuation completion are compared with commitment on a supported common
temporal basis and under the represented brake/commitment bindings.

Under material interval uncertainty, guaranteed precommit requires:

\[
\overline t_{brake}^{done}<\underline t_{commit}
\]

```text
upper(t_brake_done) < lower(t_commit)
  -> GUARANTEED_PRECOMMIT_FOR_REPRESENTED_BINDINGS
```

The point shorthand

\[
t_{brake}^{done}<t_{commit}
\]

is only a bounded special case when both event times are supported as
sufficiently point-bounded for the stated use. A pair of point estimates is not
such a guarantee. If the supported intervals overlap or the temporal basis is
unresolved, preserve the strong precommit status as `UNKNOWN`.

A post-commit rollback is distinct. A strong timing claim that rollback
completes before a load-bearing target boundary requires an executable rollback
route plus explicit target, affected-scope, boundary-condition,
route/capability and common-temporal-basis bindings. Under material interval
uncertainty:

\[
\overline t_{rollback}^{done}<\underline t_{target\_boundary}
\]

```text
upper(t_rollback_done) < lower(t_target_boundary)
  -> ROLLBACK_COMPLETES_BEFORE_BOUNDARY_FOR_REPRESENTED_BINDINGS
```

That timing relation does not establish restoration or preservation of the
threatened path. Reaching/restoring the represented target state is a separate
load-bearing proposition.

```text
REVIEW_AFTER_COMMITMENT != PRECOMMIT_BRAKE
ROLLBACK_LISTED != ROLLBACK_EXECUTABLE
ROLLBACK_AFTER_TARGET_BOUNDARY != RESTORATION
BRAKE_POINT_ESTIMATE_BEFORE_COMMIT != GUARANTEED_PRECOMMIT
ROLLBACK_POINT_ESTIMATE_BEFORE_BOUNDARY != GUARANTEED_RESTORATION
FAST_ENOUGH_CLAIM_REQUIRES_COMMON_TEMPORAL_BASIS
ROLLBACK_COMPLETED_BEFORE_BOUNDARY != RESTORED_STATE
```

"""
    b.replace_once("T_BRAKE_ROLLBACK_TIMING_BINDING", brake_rollback_old, brake_rollback_new)

    connected_brake_old = """A connected pre-commit brake requires:

```text
authenticated authority
independence appropriate to the challenged selector
latency lower than commitment time
known trigger and action-resolution path
testability
resistance to actor capture
activation and failure records
```

A brake controlled only by the actor it may need to stop is not independent."""
    connected_brake_new = """A connected pre-commit brake requires:

```text
authenticated authority
independence appropriate to the challenged selector
supported completion bound before commitment under a common temporal basis
known trigger and action-resolution path
testability
resistance to actor capture
activation and failure records
```

Where timing uncertainty is material, `BRAKE_FAST_ENOUGH` inherits [8.8]: a
point latency/deadline comparison is not a guaranteed precommit result. The
brake-completion and commitment bounds must be comparable under the same
represented timing basis and bindings.

A brake controlled only by the actor it may need to stop is not independent."""
    b.replace_once("T_BRAKE_ROLLBACK_TIMING_BINDING", connected_brake_old, connected_brake_new)

    rollback_old = "Rollback can preserve the threatened path only if it is executable, reaches the relevant state, and completes before practical irreversibility."
    rollback_new = """Rollback timing inherits [8.8]. A strong claim that rollback completes in time requires an executable route and completion before the represented target boundary under the same target, affected-scope, boundary-condition, capability and temporal-basis bindings. Completing before that boundary does not by itself establish restoration or preservation; the reached/restored target state remains a separate load-bearing claim."""
    b.replace_once("T_BRAKE_ROLLBACK_TIMING_BINDING", rollback_old, rollback_new)

'''
    text = text.replace(insert_anchor, transform + insert_anchor, 1)

# 3. Require the repaired semantics and reject the stale shortcuts.
required_anchor = '''        "A v0.2.7 packet is not silently relabelled as v0.3.0.",\n'''
required_add = required_anchor + '''        "BRAKE_POINT_ESTIMATE_BEFORE_COMMIT != GUARANTEED_PRECOMMIT",\n        "ROLLBACK_COMPLETED_BEFORE_BOUNDARY != RESTORED_STATE",\n        "GUARANTEED_PRECOMMIT_FOR_REPRESENTED_BINDINGS",\n        "ROLLBACK_COMPLETES_BEFORE_BOUNDARY_FOR_REPRESENTED_BINDINGS",\n'''
if '        "GUARANTEED_PRECOMMIT_FOR_REPRESENTED_BINDINGS",\n' not in text:
    if text.count(required_anchor) != 1:
        raise SystemExit(f"F02 required-token anchor count != 1: {text.count(required_anchor)}")
    text = text.replace(required_anchor, required_add, 1)

bad_anchor = '''        "A v0.2.6 packet is not silently relabelled as v0.2.7.",\n    )\n'''
bad_add = '''        "A v0.2.6 packet is not silently relabelled as v0.2.7.",\n        "A pre-commit brake succeeds only if detection, decision, and actuation complete before commitment:",\n        "A post-commit rollback is distinct. It can preserve the threatened path only where rollback is executable and:",\n        "latency lower than commitment time",\n        "Rollback can preserve the threatened path only if it is executable, reaches the relevant state, and completes before practical irreversibility.",\n    )\n'''
if '        "latency lower than commitment time",\n' not in text:
    if text.count(bad_anchor) != 1:
        raise SystemExit(f"F02 stale-control anchor count != 1: {text.count(bad_anchor)}")
    text = text.replace(bad_anchor, bad_add, 1)

# 4. Make document-control transform accounting explicitly include F02.
doc_old = '''carrier/enforcement/brake ceilings\nsupplemental misuse/invariant guards\n'''
doc_new = '''carrier/enforcement/brake ceilings and brake/rollback timing propagation\nsupplemental misuse/invariant guards\n'''
if doc_new not in text:
    if text.count(doc_old) != 1:
        raise SystemExit(f"F02 document-control anchor count != 1: {text.count(doc_old)}")
    text = text.replace(doc_old, doc_new, 1)

P.write_text(text, encoding="utf-8")
print("F02 compiler migration applied or already present exactly.")
