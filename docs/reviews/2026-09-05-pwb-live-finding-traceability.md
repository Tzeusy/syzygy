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

## The reviewer identifiers the packet renumbered

One of the three raw reviews numbered its own findings. `PWB-UX-1` … `PWB-UX-4`
are the UX reviewer's identifiers, assigned in
[`R-PWB-LIVE-EXACT-HEAD-UX-RAW.md`](R-PWB-LIVE-EXACT-HEAD-UX-RAW.md), and the
packet re-numbered them into the `PWB-LIVE-*` series without recording which
became which. A reader asking "was `PWB-UX-4` repaired?" therefore found the
identifier in exactly one file — the raw review that raised it — and nowhere
else in the repository [Observed — 2026-09-06: all four searched as literals
across every tracked `.md`, `.py`, `.ts` and `.jsonl`, and again in the
continuation forms this corpus uses; the only hits are inside that raw review].
CC-REV-7 amends identifiers in place and retires rather than renumbers, so the
crosswalk belongs somewhere, and this page is the somewhere.

| Reviewer ID | Severity as raised | Packet ID | The overlap the mapping rests on |
|---|---|---|---|
| `PWB-UX-1` | BLOCKER | `PWB-LIVE-02` | "No `heart-and-soul` path appears anywhere in the rendered source population" (`:153-154`, line-wrapped) against the packet's "the source delta is seven omitted Heart and Soul paths" |
| `PWB-UX-2` | BLOCKER | `PWB-LIVE-06` | Both titles state the same defect — the reviewer's is "never reaches exact requirement text" (`:202`), the packet's "links stop at metadata and production cannot render a verbatim current requirement", each about the `Exact source` link |
| `PWB-UX-3` | HIGH | `PWB-LIVE-13` | "the useful story is buried under its index" (`:248`) against "Page hierarchy exposes exhaustive inventories by default" |
| `PWB-UX-4` | HIGH | `PWB-LIVE-13` | "Resolution copy sends the owner to the wrong gate" (`:297`), whose two limbs — `missing-declaration` routed to owner drafting, and one generic policy route for 141 exclusion claims — are the packet row's second and third clauses verbatim |

Two of the four landed in one packet row, so the series is not a relabelling
and cannot be read as one. The mapping above is `[Inferred]` — it is read off
the overlapping text, because no record states it — and it is navigation, not
a disposition: `PWB-LIVE-13`'s repair child is `syzygy-1z3.24.5`, and whether
either UX finding is closed is still the reconciliation review's answer.

The gen-2 reconciliation reviewer checked the four rows on 2026-09-06
(`R-PWB-RECOVERY-RECONCILIATION-GEN2-UX-ADDENDUM-RAW.md`, Section F) and
agrees with all four primaries; its answer wins where it adds. Two additions:
`PWB-UX-1` (the six `missing-declaration` statements, raw `:148-152`) and
`PWB-UX-4` (the project-account fallback, raw `:299-307`) also land partly in
`PWB-LIVE-03`, which the table above omits `[Inferred]`; and `PWB-UX-3`'s
self-referential-lede sub-observation (raw `:259-266`) matches no packet
clause by text and reaches `PWB-LIVE-13` only through the gen-1 register
`[Inferred]`. No disposition moves: `PWB-LIVE-02`, `-03`, `-06` and `-13` are
all `repaired` in the gen-1 register.

The other two raw reviews numbered nothing. `R-PWB-LIVE-EXACT-HEAD-TRUTH-RAW.md`
and `R-PWB-LIVE-EXACT-HEAD-ENGINEERING-RAW.md` head their findings with bare
severity words (`### BLOCKER`, `### HIGH`), so for those the packet's numbering
is the first numbering and nothing was renumbered.

## The dispositions now exist, and they are not here

The section above this one says a reconciliation review under `syzygy-1z3.24.7`
was deriving the dispositions and that this page should cite that record rather
than answer for it. That record landed on 2026-09-06:
[`2026-09-06-pwb-recovery-reconciliation-packet.md`](2026-09-06-pwb-recovery-reconciliation-packet.md),
over `R-PWB-RECOVERY-RECONCILIATION-GEN1-RAW.md`. Its verdict line reads
**`CONFIRM WITH EXCEPTIONS.`** (`:21`) and its own register (`:40-62`) gives
all fifteen the disposition `repaired`, two of them with a stated residue —
`PWB-LIVE-04`'s live eight-versus-nine scenario stays unobservable until the
Butlers V1 page parses, and `PWB-LIVE-15`'s comprehension half is the owner's
under PWB-REQ-021 by spec design. That packet is the disposition of record;
this page still assigns none, and a reader wanting outcomes should go there.

**Two rows attribute differently, and the packet's column is the later one.**
For `PWB-LIVE-04` and `PWB-LIVE-07` the table above names `syzygy-1z3.24.3`,
read from the bead descriptions; the packet names `syzygy-1z3.24.4 (act via
.24.3)`. Both are true of different things — `.24.3` owns the owner-gated act
and `.24.4` the code — and the packet's is the finer statement. Neither record
is edited to match the other (CC-REV-6); the disagreement is recorded here,
which is what this page is for.

Tracked as `syzygy-qzo`, a child of `syzygy-1z3.24`. A gen-2 cycle
(`syzygy-1z3.24.8`, `.24.9`) is in flight as this is written, so the packet
above is the gen-1 record and not necessarily the last one.
