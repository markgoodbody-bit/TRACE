# TRACE v0.2.7 carrier front-door probe update

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
