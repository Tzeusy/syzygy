# PWB live exact-head review — finding traceability index

> **Navigation over existing records, never a disposition.** This page says
> *where each of the fifteen findings is named today*. It does **not** say
> whether any of them is repaired, open, or declined: that is the epic's and
> the reviewers' answer, not this page's, and where nothing names a finding
> this page renders **Unknown** rather than inferring an outcome (VIS-2).
> The findings themselves live in
> [`2026-09-05-pwb-live-exact-head-packet.md`](2026-09-05-pwb-live-exact-head-packet.md),
> which is retained review evidence and is not edited.

## Why this page exists

Epic `syzygy-1z3.24`'s first acceptance criterion is *"Every PWB-LIVE-01..15
finding is mapped to one child and dispositioned."* The mapping exists — every
one of the fifteen is claimed by exactly one repair child — but it is legible
only inside seven bead descriptions, in an abbreviated form (`PWB-LIVE-02, 03,
05 and 15`) that no search for a full identifier will find. This page is the
one place the whole mapping can be read at once, so that *nothing is dropped*
(CC-REV-6) is checkable rather than asserted.

## Where each finding is named

Every row's repair child is named by the child's own description. "Also named
in" lists the other records that carry the identifier; the epic
`syzygy-1z3.24`, the reconciliation bead `syzygy-1z3.24.7` and the bead
tracking this page (`syzygy-qzo`) each name the whole `01..15` range and are
omitted from that column, because naming a range is not traceability.

| ID | Severity | Repair child | Also named in |
|---|---|---|---|
| PWB-LIVE-01 | Blocker | `syzygy-1z3.24.1` | the plan |
| PWB-LIVE-02 | Blocker | `syzygy-1z3.24.2` | — |
| PWB-LIVE-03 | Blocker | `syzygy-1z3.24.2` | — |
| PWB-LIVE-04 | Blocker | `syzygy-1z3.24.3` | `syzygy-1z3.24.4`; the semantic delta |
| PWB-LIVE-05 | Blocker | `syzygy-1z3.24.2` | — |
| PWB-LIVE-06 | Blocker | `syzygy-1z3.24.5` | `syzygy-1z3.24.3` (gated portion only); the semantic delta; the plan |
| PWB-LIVE-07 | High | `syzygy-1z3.24.3` | `syzygy-1z3.24.4`; the semantic delta |
| PWB-LIVE-08 | High | `syzygy-1z3.24.1` | the plan |
| PWB-LIVE-09 | High | `syzygy-1z3.24.1` | the plan |
| PWB-LIVE-10 | High | `syzygy-1z3.24.4` | `syzygy-1z3.24.3` (gated portion only); the semantic delta |
| PWB-LIVE-11 | High | `syzygy-1z3.24.5` | the plan |
| PWB-LIVE-12 | Blocker | `syzygy-1z3.24.6` | `syzygy-1z3.24.3` (gated portion only); the semantic delta |
| PWB-LIVE-13 | High | `syzygy-1z3.24.5` | the plan |
| PWB-LIVE-14 | High | `syzygy-1z3.24.6` | — |
| PWB-LIVE-15 | Medium | `syzygy-1z3.24.2` | — |

"the semantic delta" is
`.syzygy/governance/contracts/candidates/pwb-truth-policy-amendment/SEMANTIC-DELTA.md`;
"the plan" is [`docs/PWB-IMPLEMENTATION-PLAN.md`](../PWB-IMPLEMENTATION-PLAN.md).

[Observed — swept 2026-09-06. Population: the fifteen rows of the packet's
"Confirmed findings" table, parsed from the table itself, not transcribed.
Sources: the full `bd show` text of `syzygy-1z3.24`, its seven children,
`syzygy-1z3.22`, `syzygy-1z3.25` and `syzygy-qzo`, plus the semantic delta and
the plan — thirteen sources. Matched with a pattern that expands the
abbreviated continuation forms this corpus actually uses (`PWB-LIVE-02, 03, 05
and 15`, `PWB-LIVE-02/03/05/15`, `PWB-LIVE-01..15`), not the bare identifier.
15 of 15 named; 0 named nowhere. Re-derive rather than trusting this table.]

*Superseded, dated:* as first written on 2026-09-05 this table reported **8 of
15 named nowhere**, including Blockers PWB-LIVE-03 and PWB-LIVE-05, and said
so under an `[Observed]` label. That was a false absence produced by a sweep
that searched for each full identifier and so could not see any finding named
in a continuation (`, 03,` after `PWB-LIVE-02`). All eight were named all
along, each in its repair child's description. The page's own method note
correctly warned that `bd search PWB-LIVE` does not reach bead descriptions —
and then the replacement method failed at the next step, on the same corpus.
The rule that would have caught it is verification rule 9: a claim of absence
needs a sweep with a denominator, and the denominator here had to include the
*forms* an identifier occurs in, not only the records searched.

## What this page still does not say

Not one disposition. `repaired` · `open` · `declined` is the register
vocabulary (`PROCESS-GLOSSARY.md`), never "acknowledged", and it is not this
page's to assign: an implementation child's owner knows what its commits
covered, and only an independent reviewer's confirmation closes a finding.
A reconciliation review under `syzygy-1z3.24.7` is deriving those dispositions
in fresh context; when its raw output is retained, the disposition question
belongs to that record, and this page should cite it rather than answer it.

Tracked as `syzygy-qzo`, a child of `syzygy-1z3.24`.
