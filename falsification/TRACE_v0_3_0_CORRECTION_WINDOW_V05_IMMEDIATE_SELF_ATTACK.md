# TRACE v0.3.0 — correction-window v0.5 immediate self-attack

**Status:** FALSIFICATION NOTE — NOT VALIDATION — NOT SPINE TEXT — NOT CANON  
**Object attacked:** initial v0.5 commit `567b6731785267fdc28a468b878d8d98ff45d264`  
**Corrected v0.5 commit:** `d862a021b0d1f614c44062e12fb7cb84badbdd71`

## Break

Initial v0.5 made load-bearing verification semantically explicit but retained a completion-time shorthand containing only:

```text
signal + diagnosis + route + correction
```

That allows an internally inconsistent reading:

```text
required pre-use verification exists
verification consumes material time
window equation prices verification time as zero
```

Counterexample:

```text
target closes in 15 min
raw correction mechanics take 5 min
required check takes 20 min and must return before the route may honestly proceed
```

The initial timing form could print a fit even though the required checking path cannot finish before target closure.

```text
REQUIRED_CHECK_TIME != ZERO_DURATION
```

## Repair

Corrected v0.5 makes a declared event/precedence graph `G_window` primary.

Where load-bearing, it includes:

```text
signal
diagnosis
required verification
required result return
required activation / decision conditioning
routing
correction execution
target reached
use / commitment boundary
```

`T_complete` is the critical-path duration for the declared abstraction.

A sequential shorthand may include `T_required_verify`, but only for check/review work actually on the critical path and not already counted elsewhere.

```text
LOAD_BEARING_CHECK != FREE_CHECK
CHECK_IN_PARALLEL != SERIAL_DELAY
NOT_REQUIRED != UNKNOWN_DURATION
```

## Disposition

This is a ROOT C / timing integration defect, not evidence for a new semantic root.

The initial v0.5 commit remains in Git history as the failed object. The corrected candidate is `d862a021...`.

```text
SELF_ATTACK_FOUND_BREAK != CANDIDATE_INVALID_FOREVER
REPAIRED_BREAK != VALIDATION
```
