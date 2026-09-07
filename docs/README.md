# `docs/` — the implementation plane's working documents

> **Not authority.** Nothing here adopts, accepts, or approves anything, and
> nothing here may be cited as a rule. Authority lives in `.syzygy/**`
> (doctrine, decisions, policies, contracts) and `openspec/**`
> (specifications); current state lives in `PROJECT-STATUS.md`. Where a page
> here disagrees with one of those, **the owning record wins and this page is
> stale** — report the disagreement rather than resolving it here.

`.syzygy/**` says what must be true and `openspec/**` says what the software
must do. This directory holds the third thing: the **implementation plane's**
own working record — how the work was planned, what was reviewed, and what
evidence a run actually produced. It is written by and for the people and
agents doing the building.

## What is here

| Path | What it is | Reader, and the question it answers |
|---|---|---|
| `CAPABILITY-1-IMPLEMENTATION-PLAN.md` | The Capability 1 build plan | An implementer: "what is the next lawful implementation step, and under which act?" |
| `PWB-IMPLEMENTATION-PLAN.md` | The Polaris project-wide Butlers-model build plan | Same, for the PWB pipeline |
| `THREE-SURFACE-POC.md` | How to run the bounded POC | Anyone: "how do I start this thing and see it?" |
| `reviews/` | The review corpus — raw reviewer output and its dispositions | A reviewer or repairer: "what did an independent reader find, and what happened to each finding?" |
| `evidence/` | Machine-produced run records (mutation sweeps, browser and fresh-checkout runs), as JSON | Anyone checking a claim: "what did that run actually output?" |
| `plans/` | Dated design notes for a single bead, written before the work | An implementer picking up that bead: "what shape was already decided, and by whom?" |
| `superpowers/plans/`, `superpowers/specs/` | Spent plans and designs from an external-harness convention, kept as evidence | Someone auditing a past change: "what was the plan the work was actually done against?" |

Implementation *plans* live here. The **authorizing act** for any of that work
does not — it lives in `.syzygy/governance/decisions/`. A plan in this
directory is never permission; find the act first (`AGENTS.md`, "Where
authority lives").

## `reviews/` — the corpus, by campaign

Raw reviewer output is stored **verbatim and never edited** (CC-REV-6). Files
ending `-RAW.md` are that verbatim output; `-DISPOSITION.md` and `*-PACKET.md`
files are the synthesis over them. Correcting a RAW file is never the repair —
the repair is a new disposition that cites it.

| Campaign | Files | Recorded | What was under review | Last verdict of record, and where the findings landed |
|---|---|---|---|---|
| `R-S2` … `R-S7` | 4 | 2026-08-21 → 08-22 | Capability 1 domain slices S2, S5, S6, S7 | S2 `VERDICT: CONFIRM` (`R-S2-RISK-FLOOR-REVIEW.md:54`, the confirming pass over the `REVISE` at `:30`); S5/S6/S7 each `## Verdict: CONFIRM WITH EXCEPTIONS` at `:8`. S2's blocker was repaired in the slice; its four non-blocking findings and S5's parity exception went to bead `syzygy-ydr` (closed), whose successor `syzygy-e3e` is still open. S7's third exception is the `write-boundary.ts` `startsWith` containment item `AGENTS.md` still tracks as unfixed |
| `R-RT-*` | 2 | 2026-08-23 | The Capability 1 runtime vertical slice — daemon, app entry, system tests | `## Verdict: CONFIRMED` (`R-RT-CONFIRMATION-REVIEW.md:4`) over the `CONFIRM WITH EXCEPTIONS` first pass. RTF-1 (a symlinked `--state-dir` dodging the governed-plane guard) was repaired in the commit range the confirmation names, with a new system test. No bead: the disposition lives entirely in this file pair |
| `R-POC-*` | 8 | 2026-08-30 → 08-31 | The Three-Surface POC — one product review, four improvement cycles, and the owner's cold-open walkthrough | `## Verdict: CONFIRMED` (`R-POC-CYCLE-4-CONFIRMATION.md:15`) closes the cycle chain; each cycle's findings were repaired in the commit the next file names. The walkthrough is a different evidence class and did not close: `**FAIL — BLOCKER for presenting the current page as project-level Polaris.**` (`R-POC-OWNER-WALKTHROUGH-POLARIS.md:17`). It is what launched the `polaris-project-wide-butlers-model` spec work below |
| `POLARIS-*`, `R-POLARIS-*` | 15 | 2026-08-31 | Two threads: the read-boundary incident and the bootstrap-authorization exception; and the project-wide Polaris candidate's own six-pass review chain | The chain exhausted its six-pass convergence ceiling at `REVISE`; the owner authorized one bounded post-ceiling correction (`decisions/POLARIS-POST-CEILING-CORRECTION-AUTHORIZATION.md`), after which `Verdict: **CONFIRMED**` (`R-POLARIS-PROJECT-WIDE-SPEC-REVIEW-DISPOSITION.md:181`) closed the last finding. The binding disposition is the act, not a review file: `decisions/POLARIS-PROJECT-WIDE-SPEC-SIGNOFF-ACT.md:14`. Sign-off is not implementation authority — read the act |
| `R-GENERAL-TRUSTED-*` | 24 | 2026-08-31 → 09-01 | The general trusted-bootstrap authorization transaction, across four sub-rounds: semantic deltas, a full pre-act round, the owner packet, and a post-act round | Both final confirmations head `CONFIRM` (`…POST-ACT-CHECKER-FINAL-CONFIRMATION-RAW.md:1`, `…POST-ACT-READER-FINAL-CONFIRMATION-RAW.md:1`). Findings landed in the two `*-REVIEW-DISPOSITION.md` files, the candidate delta, RFC 0001–0009 and the CC-SPEC repairs, the act record, and three `check_governance.py` predicates. One item was deliberately deferred as non-blocking and is named there |
| `R-PWB-STATE1-*` | 14 | 2026-09-02 | The PWB state-(1) amendment — a second lawful provenance state for PWB-REQ-005/022, over an eleven-artifact manifest | Three post-act reviews each `**EXACT VERDICT: CONFIRM**`. Three lanes (security, transaction, oracles) each ran to `REVISE` and back twice before the owner packet; the act is `decisions/PWB-STATE1-AMENDMENT-ACT.md` |
| `R-PWB-EFFECT-*` | 3 | 2026-09-02 | The three PWB effect acts — the consent, secret-policy and registry authority that PWB-REQ-005 gates on | `**EXACT VERDICT: CONFIRM**` (`R-PWB-EFFECT-ACTS-OWNER-PACKET-RAW.md:353`). One security finding on policy vocabulary was repaired and confirmed; the rest were readability notes. Three separate acts in `decisions/`, one per authority |
| `R-PWB-TRUTH-*` | 11 | 2026-09-05 | The PWB truth-and-readiness amendment — precedence grammar, code-context and secret-scan grammar, the resource-limit ledger, PWB-REQ-021 readiness — plus two dependent effect amendments | `**EXACT VERDICT: CONFIRM**` (`R-PWB-TRUTH-POLICY-OWNER-PACKET-FINAL-RAW.md:19`), zero findings, after three frozen subjects and two full repair cycles across security, contract-oracle and comprehension lanes. Three acts followed: `PWB-TRUTH-READINESS-AMENDMENT-ACT.md` and the two `*-AMENDMENT-ACT.md` effect decisions |
| `R-PWB-LIVE-*`, `*-pwb-live-*` | 5 | 2026-09-05 | The live implementation at its exact head — truth, denominator, secret-exposure, parity, copy and comprehension | Fifteen findings PWB-LIVE-01…15 across three raw reviews, plus the traceability index over them. Their dispositions are not in this campaign; they are in the row below |
| `R-PWB-RECOVERY-*`, `*-pwb-recovery-*` | 5 | 2026-09-06 | The recovery of those fifteen findings: a gen-1 reconciliation packet with its raw review, then a gen-2 reconciliation of the repairs it required, with its raw review | Gen-1 `**CONFIRM WITH EXCEPTIONS.**` (`2026-09-06-pwb-recovery-reconciliation-packet.md:21`) — all fifteen `repaired`, nine residues PWB-RECON-01…09. Gen-2 `**CONFIRM WITH EXCEPTIONS.**` (`2026-09-06-pwb-recovery-reconciliation-gen2-packet.md:24`) — the three required repairs confirmed, gen-3 not needed, four Low/Info residues PWB-RECON-10…13 as ordinary beads. This closes the PWB-LIVE cycle's repair half; §5.3 of the spec's task list (report the cycle to the owner) is still open |

| `R-PWB-P63-*` | 1 | 2026-09-07 | The P-63 arm-A trim of the Polaris human page (bead `syzygy-1z3.27`): 434,960 bytes off both forms, measured before the P-60/P-61 Butlers repairs merge | `CONFIRMED WITH FINDINGS` (`R-PWB-P63-POLARIS-TRIM-RAW.md:16`), no blocker; the reviewer reproduced the measurement byte-for-byte. Both should-fix findings were repaired in the same branch (the apostrophe-bearing identity reader, and the evidence retention); dispositions live in `docs/evidence/pwb-p63-polaris-trim-measurement-2026-09-07.json` under `review.dispositions` |
The eleven rows partition the directory: 92 files on disk, 92 assigned, no
remainder [Observed — swept by a script that asserts each basename matches at
most one campaign pattern and prints the unmatched remainder; re-run
2026-09-07 after the P-63 row was added (92), and 2026-09-06 when it read 91;
this figure read 88 the morning of the 6th. All three arrivals
landed in the last row: the gen-2 reconciliation added two, and the gen-2 raw
was then re-issued with its crosswalk addendum as a fifth file rather than
overwriting the first (verification rule 10). Dates are
`git log --diff-filter=A`]. These are navigation figures, not measurement,
and they go stale the moment a review lands — re-derive rather than trusting
the row.

Three things the table cannot show. The PWB rows are a dependency chain, not
four independent campaigns: the state-(1) amendment made a behavioral change,
the effect acts then granted the authority that change could satisfy, and the
truth-and-readiness amendment later replaced the state-(1) artifacts outright
while amending the two instruments the effect acts had put in force — the act
records say so, and only they say it. A `CONFIRM` verdict is a reviewer's
finding about frozen bytes, never an adoption: what binds is always the act in
`.syzygy/governance/decisions/`. And a campaign with nothing open in its own
files may still have left something open elsewhere — the S-slice row's
`syzygy-e3e`, the POC row's walkthrough blocker, the recovery row's §5.3.

## `plans/` and `superpowers/` — two homes, one role

Both hold plan-and-design notes; they are split by which harness wrote them,
not by what they are. Prefer `plans/` for anything new.

`superpowers/` is **path-pinned and must not be moved or renamed.** The
general trusted-bootstrap authorization's impact ledger classifies every path
under that prefix as spent historical evidence, and
`scripts/build_general_trusted_bootstrap_impact_ledger.py` hard-codes the
prefix string to do it. Relocating a file out of that directory would silently
re-classify it on the next regeneration.

**One of the four is not spent.** The ledger's classification is about where a
file sits, not about whether the work it plans is finished, and those two
answers have come apart. Read the table before treating any of these as
history — and read the `bd` issue, never the "REQUIRED SUB-SKILL" line at a
file's head, which addressed the worker of the day.

| File | Issue | State |
|---|---|---|
| `superpowers/plans/2026-08-24-cap1-runtime-hardening-followups.md` | epic `syzygy-u2a` | **Live.** The epic names it as its *approved implementation guidance* at commit `d11c07e`, and shapes its six implementation children on that file's Tasks 1–6. The epic is open (P1) and its human gate `syzygy-u2a.1` is blocked |
| `superpowers/specs/2026-08-23-cap1-runtime-hardening-followups-design.md` | `syzygy-ydr`, `syzygy-e84`, `syzygy-h84` | Spent. The design the plan above was written from |
| `superpowers/plans/2026-08-27-syzygy-vky-validator-hardening.md` | `syzygy-vky` (closed) | Spent |
| `plans/2026-08-26-syzygy-vky-validator-hardening-design.md` | `syzygy-vky` (closed) | Spent. The design for the same work as the row above — two files, one bead, split only by which harness wrote them. Neither is cited by anything |

[Observed — swept 2026-09-06: four files across the three directories; each
searched for `syzygy-*` identifiers in its own text, and each filename searched
across every tracked `.md` and `.py`. Two are cited, both by the general
trusted-bootstrap impact ledger; two are cited by nothing.]

## `evidence/` — run records

Each file is one run's machine output at a named commit, kept because a claim
elsewhere cites it. A mutation-run record is valid **only for the commit it
names** (`AGENTS.md` verification rule 7). Reading the file's own contents is
the check; the filename is not the evidence.

**This directory has no index of its own, and does not need one:
`PWB-IMPLEMENTATION-PLAN.md` is the index.** Every file here is cited, and 25
of the 28 are cited by that plan, at the task whose evidence they are — so the
route in is the plan's task, never a listing of this directory. The three the
plan does not name are the three a *reviewer* produced rather than a task
(`…-gen2-reviewer.json`, `pwb-recon-gen1-reviewer-…`,
`pwb-recon-gen2-reviewer-…`); the reconciliation packets in `reviews/` cite
those, which is the correct home for a reviewer's own run. [Observed — swept
2026-09-06: 28 files, each basename and stem searched across every tracked
`.md`, `.py`, `.ts`, `.json`, `.yml`, `.txt` and `.sh` outside this directory;
28 cited, 0 uncited, 25 cited by the plan, remainder enumerated above.]

A JSON here does not say whether the work it evidences is finished — a run
that passed at a commit says nothing about the finding a later review raised
against the same seam. `bd show` and `PROJECT-STATUS.md` own that.

## The maintenance contract

This directory is governed by the adopted craft policy
`.syzygy/governance/policies/craft-and-care/review-and-documentation.md`. The
clauses that bind what you write here — cited, not restated:

- **CC-REV-2** — a change that moves a responsibility updates its
  documentation *in the same change*; it does not merge with the
  contradiction open.
- **CC-REV-3** — documentation **cites** authoritative artifacts, it never
  restates them normatively. A restated rule drifts and becomes a shadow
  authority. If you find the same question answered in two homes, surface the
  contradiction; do not silently pick a winner.
- **CC-REV-5** — substantive claims carry `[Observed]` (with a resolvable
  source), `[Inferred]`, or `[Unknown]`. Missing evidence renders Unknown,
  never Inferred.
- **CC-REV-6** — raw reviewer output is stored unchanged before synthesis, and
  every revise-severity finding is fixed or explicitly overruled with recorded
  rationale. Nothing is dropped.
- **CC-REV-7** — identifiers are stable: amend in place, retire rather than
  renumber.

In practice, for this directory: a page that no longer has a nameable reader
and a question it answers should be merged or removed, not left to rot; a page
that has gone stale is marked stale **with evidence at the stale sentence**,
never left silently standing behind a general "this page may be stale" banner.

## What does not belong here

- Implementation code (it belongs in `apps/**`, `packages/**`, `scripts/`).
- Anything normative — rules, acceptance, adoption, approval. Those are owner
  acts under `.syzygy/governance/` (VIS-4).
- A second copy of state `PROJECT-STATUS.md` already owns.
- Per-tool scratch conventions from an external harness. If a tool wants a
  directory of its own, it gets one outside `docs/`.
