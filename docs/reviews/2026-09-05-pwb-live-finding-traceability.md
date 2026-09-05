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
finding is mapped to one child and dispositioned."* Five of its seven children
were closed before anything checked that mapping against the fifteen, and the
mapping turned out to be partial. Eight findings — two of them Blockers — are
named by no bead, no amendment record and no plan section. That is not a claim
that eight defects are unfixed; several plausibly fall inside a closed child's
wording without carrying its identifier. It is a claim that the traceability
the criterion asks for cannot currently be read off anything, which is exactly
the shape CC-REV-6 exists to prevent: *nothing is dropped* is only checkable
if every finding can be followed somewhere.

## Where each finding is named

| ID | Severity | Named in | Follow-up |
|---|---|---|---|
| PWB-LIVE-01 | Blocker | beads `syzygy-1z3.24.1`, `syzygy-1z3.24.7`, epic `syzygy-1z3.24`; `docs/PWB-IMPLEMENTATION-PLAN.md` | Read those |
| PWB-LIVE-02 | Blocker | bead `syzygy-1z3.24.2` | Read that |
| PWB-LIVE-03 | Blocker | — | **Unknown** — no record names it |
| PWB-LIVE-04 | Blocker | beads `syzygy-1z3.24.3`, `syzygy-1z3.24.4`; the truth-policy amendment's semantic delta | Read those |
| PWB-LIVE-05 | Blocker | — | **Unknown** — no record names it |
| PWB-LIVE-06 | Blocker | bead `syzygy-1z3.24.5`; the semantic delta; the plan | Read those |
| PWB-LIVE-07 | High | the semantic delta | Read that; the route needs an approved policy amendment and a new act |
| PWB-LIVE-08 | High | — | **Unknown** — no record names it |
| PWB-LIVE-09 | High | — | **Unknown** — no record names it |
| PWB-LIVE-10 | High | the semantic delta | Read that |
| PWB-LIVE-11 | High | — | **Unknown** — no record names it |
| PWB-LIVE-12 | Blocker | bead `syzygy-1z3.24.6`; the semantic delta | Read those |
| PWB-LIVE-13 | High | — | **Unknown** — no record names it |
| PWB-LIVE-14 | High | — | **Unknown** — no record names it |
| PWB-LIVE-15 | Medium | — | **Unknown** — no record names it |

[Observed — swept 2026-09-05. Population: the fifteen rows of the packet's
"Confirmed findings" table, parsed from the table itself, not transcribed.
Searched for each identifier in the full `bd show` text of `syzygy-1z3.24`,
its seven children, `syzygy-1z3.22` and `syzygy-1z3.25`; in
`.syzygy/governance/contracts/candidates/pwb-truth-policy-amendment/SEMANTIC-DELTA.md`;
and in `docs/PWB-IMPLEMENTATION-PLAN.md`. 7 of 15 named, 8 named nowhere.
`bd search PWB-LIVE` returns "No issues found" and is not a valid method here —
it does not reach bead descriptions, which is where every one of the seven
matches actually lives. Re-derive rather than trusting this table.]

## What would close the gap

Naming the identifier in whichever record already covers the work, or
recording a disposition for it — `repaired` · `open` · `declined`, the
register vocabulary, never "acknowledged" (`PROCESS-GLOSSARY.md`). Both are
someone else's call: an implementation child's owner knows what its commits
covered, and only an independent reviewer's confirmation closes a finding.
This page is deliberately not that record, and must not be cited as one.

Tracked as `syzygy-qzo`, a child of `syzygy-1z3.24`, so the epic's criterion 1 is not read as satisfied by the
five closed children alone.
