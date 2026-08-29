# TRACE v0.3.0 — BLIND ADJUDICATION MIXED-ROUTE RESULT — 2026-08-29 v0.3

**Status:** STOPPED ON FIRST WEB PACKET — NO ASSISTANT RETURN — NO GEMINI SPEND — KEY STILL SEALED — NOT ADJUDICATION RESULT

## Earned result

The exact mixed-route successor began under authorization
`CODEX-THREAD-20260829-USD0_6149625-BLIND-ADJUDICATION-003`.

The first neutral packet, `PAIR-09F86168CA`, was transmitted to a fresh signed-out Grok guest chat
with the visible mode label `Fast`. The page accepted and displayed the complete user packet. After
at least 45 seconds, including reacquisition of the still-open page after a browser-control wait
timed out, the page still showed:

```text
visible articles = 1
user articles = 1
assistant articles = 0
visible alert text = empty
session-specific URL = unavailable
preservable assistant response bytes = 0
```

The in-app browser does not support exporting that page. The prompt itself was already frozen by
hash, and the observable failure boundary is preserved in `browser-failure-witness.json`. No retry
or substitution was attempted.

## Accounting boundary

```text
Grok web monetary exposure = USD 0.0000000
Gemini API calls = 0
Gemini API exposure = USD 0.0000000
unspent authorization = USD 0.6149625
```

## Frozen stopped-run identity

Directory:
`C:/Users/markg/Downloads/TRACE-v0.3.0-blind-adjudication-run-20260829-v0.3-mixed-route`

```text
files = 4
bytes = 4,059
run-summary.json SHA-256 = 78c2629027947dbf6ce4031225d78cb77b08fa66e25cf2bccb7d14e91b492402
browser-failure-witness.json SHA-256 = dd8205fa317459469010fafd4c32187945cff8b556d4ade134d6c7d8d3155e41
```

Download archive:
`C:/Users/markg/Downloads/TRACE-v0.3.0-blind-adjudication-run-STOPPED-20260829-v0.3.zip`

```text
archive bytes = 3,388
archive SHA-256 = cffdc488c184d5cd3869691cba30661981ec60fd4f9396c7ceb140a114371ba9
```

## What this does and does not establish

Established:

- the signed-out Grok guest `Fast` page accepted the first exact public packet;
- it did not produce a visible or preservable assistant return within the bounded observation;
- the fail-fast order prevented all Gemini spend and the remaining 31 calls;
- the sealed arm key remained unexposed.

Not established:

- whether Grok performed undisclosed backend work;
- whether a signed-in or different Grok mode would return;
- any substantive Grok adjudication;
- two-family confirmation of any candidate gain;
- any TRACE efficacy, validation, release or canon result.

## Narrow disposition

Do not retry this Grok guest route inside the stopped attempt. A different signed-out web family,
such as Meta AI, may be checked only as a newly frozen successor with the same web-first fail-closed
order. That would still carry a service-level rather than exact-backend-model identity limitation.
