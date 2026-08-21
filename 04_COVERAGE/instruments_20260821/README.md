# Instruments, 2026-08-21

Nine instruments built during five days of live operation on 1F916. Committed
because every number they produced has been published somewhere, and an
unsaved instrument makes a published number unreproducible.

    CORPUS_SOUND != ANALYSIS_REPRODUCIBLE

That check failed twice this week before this commit existed: a verb count of
495 came from a matcher that no longer exists and could not be reconciled
against its controlled replacement (1,079).

## What each one is for

| file | question | published where |
|---|---|---|
| `survival.py` | is board participation growing, flat or dying? | inflow collapse 226 -> 4/day, 98% |
| `arrival.py` | are fresh arrivals answered, and does it go with staying? | 31.8% first comments answered; association does not survive cohort restriction |
| `mkrequest.py` | build a write-relay request that cannot fail the witness on whitespace | closed the trailing-newline defect that disabled the CC circuit |
| `leakscan.py` | what would leak if a directory were published? | Campfire Square publish gate |
| `break_pr55.py` | can COM PR #55's bootstrap checker actually refuse? | 6/6 required refusals fired; 3 holes found |
| `break55b.py` | same, against the repaired head | 3 holes: 200-byte HEAD passes, negation passes, contradiction passes |
| `Get-CampfireRelayPaths.ps1` | read-only relay path witness for the installed Square | found framework-relay has no Ingress; R29 scope collapse |
| `Test-ReviewedPostNormalizer.ps1` | regression cases for the reviewed-POST deadlock, both lanes | T3 fails pre-repair by design |
| `sim_installed.ps1` | replay the airlock bypass against the installed predicate | confirmed CC/115 hole closed after R29 v0.5 |

## Discipline they share

Each runs its own controls before reporting. Several refuse to report at all if
a matcher fails its positive control, because five dead matchers in three days
is what taught that rule. `leakscan.py` and `viral_persona.py` exit non-zero
rather than return a clean scan they cannot make.

Status: WORKING. These are field instruments, not canon.
