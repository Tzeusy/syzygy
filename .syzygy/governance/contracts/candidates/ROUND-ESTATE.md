# The round estate — what eleven work rounds settled, and where it lives now

> **Navigation, never authority.** This page adopts nothing, accepts nothing
> and may not be cited as a rule. It routes a reader through
> `round-2026-08` … `round-2026-08k` — the tracked files that no index
> covered; "How many files are in here" below derives the count and
> reconciles the four different figures other pages quote. Where this page and an owning record disagree, **the owning record
> wins and this page is stale.** Current state is `PROJECT-STATUS.md`; what is
> accepted is `decisions/ACCEPTANCE-ACT-RECORD.md`.
>
> Written 2026-09-06. Before it, ten of the eleven round directories had no
> index of any kind — only `round-2026-08/` carried a `README.md` [Observed —
> `ls` over all eleven, 2026-09-06; `round-2026-08g/CAPABILITY-1-OWNER-DECISION-INDEX.md`
> indexes a decision set, not the directory]. A reader asking "what did round
> 08e settle, and does any of it still bind?" had to open 53 files. Later the
> same day all eleven directories gained a `README.md`; this page is the route
> across them, each round's own README the route within it.

## How to read a round

A round is one work pass with its own reviews and reports. **A round directory
is never authority and never on a default reading path.** Three facts about
them are easy to get wrong:

- **The directory's index date is its first-commit date and does not bound its
  contents.** `round-2026-08g` took two files seventeen days after it closed.
- **"Historical" never means "safe to relocate."** Two round files are live
  inputs to running software; both are named below.
- **96 of the 235 Markdown round files carry no status word at their head**
  (the denominator is derived under "How many files are in here"). Every round
  directory now has a `README.md` saying the round is closed, but those 96
  file heads are unchanged and an agent may not change them — some are bound
  by a performed act's manifest (`syzygy-3zi` states the lawful shapes). Read
  the `round-*` path itself as the banner.

## The eleven rounds

| Round | Span | Files | What it settled | Where that settlement lives now |
|---|---|---|---|---|
| `round-2026-08` | 08-05 → 08-07 | 26 | The first human-clarity refactor: the original five-act owner offering, the SD-1…12 semantic-delta classification, term migration | **Nowhere current.** Its acceptance record opens `SUPERSEDED`; acts 1 and 4 were retired. Its one durable export is this repository's process-lessons file, moved out to `decisions/PROCESS-LESSONS.md` |
| `round-2026-08b` | 08-05 → 08-10 | 28 | A repair pass over stale derived word-counts; CG-21 gained its "pass B" | The CG-21 logic is now native to `scripts/check_governance.py` — the script, not this directory, is the home. The round's own acceptance record is superseded twice over |
| `round-2026-08c` | 08-07 → 08-10 | 31 | The `depends_on` / `constrains` / `cites` contract-relation model, and twelve pre-specification criteria | **Still open as P-21.** The Wave A and B acts of 2026-08-17 ratified the relation's *presence*; sub-question (a) is unruled, and `decisions/PENDING-OWNER-DECISIONS.md` row P-21 cites this round's `CONTRACT-RELATION-CLOSURE-REPORT.md` as its evidence |
| `round-2026-08d` | 08-09 → 08-10 | 26 | The six-wave acceptance structure (A, B, C1, C2, D1, D2) that replaced one all-in-one act. Fifteen reviews — nine by dimension, six by wave — and **fifteen `REVISE` verdicts, zero `CONFIRM`** (`reviews/DELIVERY-AND-VERDICT-REGISTER.md`) | `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` and `wave-manifests/` — the wave partition is the live shape. Waves A and B are accepted; C1/C2/D1/D2 remain deferred and unauthorized |
| `round-2026-08e` | 08-10 → 08-13 | 53 | Waves A and B confirmed (`VERDICT: CONFIRM`) but withheld from offer by the P-33 ruling; the launch-gate instrument versioned v1.4 → v1.18 | The Wave A and B acts, performed 2026-08-17. The instrument's v1.x content is folded cumulatively into `launch-gate-pre-specifications.md` (now v2.4) — the versioned file, not the per-version raw reviews |
| `round-2026-08f` | 08-11 → 08-17 | 20 | Launch gate v2.0; the first Capability 1 owner decision packet; a dry-run administration fixture | **Carries a live CI input** (below). The decision packet was superseded 2026-08-13 by 08g's index; the P-33 analysis likewise |
| `round-2026-08g` | 08-13 → **08-30** | 20 | P-33 re-derived and ruled; CC-SPEC and CC-IMPACT repaired as one model | `decisions/WAVE-A-INSTALL-SHAPE-DECISION.md`, and the two craft policies in `policy-candidates/` that are **in force** despite their directory's name. **Carries a live fixture** (below) |
| `round-2026-08h` | 08-16 | 11 | A pure review round: eight raw reviews (RD-61…RD-68) over launch-gate v2.2, v2.3 and v2.4 and the P-41/P-42 owner packets, plus the v2.3 and v2.4 deltas | The two deltas fold into `launch-gate-pre-specifications.md`; **the round produced no artifact of its own that anything outside it now depends on** — its eight RAW reviews and disposition register stay here as the evidence behind that fold |
| `round-2026-08i` | 08-17 | 9 | The convergence pass: Wave A and B acts performed, CC-SPEC/CC-IMPACT consolidated and adversarially reviewed, craft acts 6 and 7 minted | Craft acts 6 and 7 — the in-force craft-policy acceptance. `SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA-2.md` is the change record behind them |
| `round-2026-08j` | 08-18 | 6 | The repair pass after launch-gate Administration 1 returned `NOT READY`; three Unknown verdicts (B5, C2, D3) settled by dedicated measurement rather than prose | The three reports and their two sweep scripts are the settlements of record, tied together by `ADMINISTRATION-1-DISPOSITION-REGISTER.md` over `decisions/launch-gate/ADMINISTRATION-2026-08-18-CAPABILITY-1.json` |
| `round-2026-08k` | 08-20 → 08-21 | 8 | The Capability 1 specification adoption and implementation-authorization acts, prepared and bound; five fresh-context reviews | `decisions/CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md` and `decisions/CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md`, both in force. The two `*-PREPARED.md` files here are literally the packets those acts performed from |

## One finding that outlived the packet it was routed to

Round `2026-08c` recorded its own sharpest unrepaired finding — facets permit
**intra**-facet rollup and forbid **inter**-facet rollup, with no stated
principle distinguishing them (B-4/B-6, `HUMAN-CLARITY-CLOSURE-REPORT.md:154`
over `reviews/RD-2-human-clarity-RAW.md:346`) — and routed it to owner
**packet 6**. Packet 6 was later struck as stale
(`round-2026-08d/OWNER-DECISION-PACKETS.md:21`, "Do not act from packet 6
below"), and no row in `decisions/PENDING-OWNER-DECISIONS.md` inherited the
question [Observed — 2026-09-06, `intra-facet` and `rollup` swept as literals
across `.syzygy/`, `openspec/`, `docs/` and the root pages; the only hits for
the finding are the two round files above].

The adopted Capability 1 specification now speaks to both halves:
**CAP1-REQ-030** defines each facet as a question plus its constituent facts,
and **CAP1-REQ-031** prohibits any composite over the answers. `[Inferred]`
that is the distinction the finding asked for — a facet's own aggregation is
definitional, a cross-facet one is derived — but neither clause states it as a
principle, and no record says B-6 was answered. Read the two clauses before
concluding either way; do not treat this paragraph as the disposition.

## The two round files that running software reads

Neither may be moved, renamed or deleted without breaking something.

- **`round-2026-08f/fixtures/DRY-RUN-ADMINISTRATION.json`** — a live CI input.
  `.github/workflows/governance-docs.yml` invokes
  `validate_launch_administration.py` against it at line 127 and
  `render_launch_administration.py --check` against it at line 130, both by
  full path [Observed — read from the workflow, 2026-09-06].
- **`round-2026-08g/SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2.md`** and its
  answer key — named **by path and by SHA-256** inside CC-IMPACT-7, an
  in-force craft clause
  (`policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md`, the fenced
  block under the clause head). Note the trap: fixture **3** exists in the same
  directory and supersedes fixture 2 on the merits — fixture 2 left
  `topology[]` unexercised — but the clause names fixture 2, and neither the
  clause nor the fixture may be edited to say otherwise.

Rounds `h` through `k` are additionally cited as evidence by acts in force.
Before treating any round file as inert, sweep for citers by filename across
`git ls-files` — not by directory name, and not by the word "historical".

## How many files are in here

Four figures for this one population are in circulation, and all four are
right about different things. The derivation, so no page has to guess:

| Figure | What it counts |
|---|---|
| **249** | Every file ever added under a `round-*` path |
| **248** | Present on disk now. The one that left was the first round's own PROCESS-LESSONS.md — no code span, because a path that no longer resolves may not carry one (CG-1b) — moved out to [`decisions/PROCESS-LESSONS.md`](../../decisions/PROCESS-LESSONS.md) as the rounds' one durable export |
| **239** | Present before 2026-09-06, plus that departed file — the population `HISTORICAL-INDEX.md` swept with `git log --diff-filter=A` |
| **238** | Present before 2026-09-06: the 248 less the ten directory `README.md` files added that day (`round-2026-08/` already had one) |
| **235** | Of those 238, the Markdown ones. The three that are not: `round-2026-08f/fixtures/DRY-RUN-ADMINISTRATION.json` and `round-2026-08j/`'s two `sweep_*.py` |
| **237** | On disk now, less all eleven directory READMEs — the round *work*, which is what a citation sweep should measure |

[Observed — 2026-09-06: `git ls-files` for what is present, `git log
--diff-filter=A --name-only` for what was ever added, both over all eleven
directories; the two lists differ by exactly the one file named above.]

A figure quoted anywhere else is a copy and may have gone stale — including
the two in the next section, which were re-derived here today and were already
wrong by four when first published, for the reason that section gives.

## What no longer has a reader

**84 of the 237 round work files are named by no other tracked file**
[Observed — re-swept 2026-09-06: every non-README round file's basename
searched as a literal substring across the decoded bytes of all 751 tracked
non-round files; `git ls-files` is the denominator for both populations]. By
round: 08→9, 08b→8, 08c→13, 08d→8, 08e→19, 08f→9, 08g→5, 08h→4,
08i→2, 08j→4, 08k→3.

*This figure read 88 of 238 when the page was first written, hours earlier.*
Four of those 88 have a citer now, and the citer is **this page**: writing the
round table named `round-2026-08c/HUMAN-CLARITY-CLOSURE-REPORT.md`,
`round-2026-08c/reviews/RD-2-human-clarity-RAW.md`,
`round-2026-08g/CAPABILITY-1-OWNER-DECISION-INDEX.md` and
`round-2026-08j/ADMINISTRATION-1-DISPOSITION-REGISTER.md`, and no other
tracked file names any of them. An index that names files changes the absence
figure it reports, so the sweep has to run *after* the prose is written, not
before — measure last, or the number is stale on publication.

Two cautions on that figure, in both directions. It counts **filename**
citation only, so a file whose findings were absorbed into a successor's prose
counts as uncited while its content lives on — which is what happened to most
of 08e's nineteen, the per-instrument-version raw reviews that the closure
reports summarise without ever naming. And it says nothing about whether a
file *should* have a reader: a raw reviewer file is stored verbatim precisely
so that nobody has to cite it for it to remain evidence (CC-REV-6).

**Nothing here may be deleted or relocated by an agent.** These files sit in
the governed plane; disposing of them is an owner decision, and the open
question is queued in `decisions/DOCUMENTATION-ESTATE-DECISION-PACKET.md`.

## Where the durable lessons went

Rounds discover rules; rules outlive rounds. Every round's transferable
lesson — the thing that changes how the *next* piece of work is done — belongs
in `decisions/PROCESS-LESSONS.md`, which now carries a section for every one
of the eleven — the first round's under `## Added at the round close`, since
that file *was* round `2026-08`'s lessons file before it was moved to its
durable home [Observed — 2026-09-06; the sections for 08d, 08e, 08f, 08j and
08k were written that day from the rounds' own registers, closing a gap of
113 files whose lessons had never been promoted anywhere]. `AGENTS.md` keeps the ten
compressed verification rules and points there for the incidents behind them.

If you are reading a round directory to learn a rule, you are in the wrong
file. Read the lesson; open the round only to check what paid for it.
