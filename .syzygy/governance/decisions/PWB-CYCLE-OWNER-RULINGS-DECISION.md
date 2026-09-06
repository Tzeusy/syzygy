# PWB improvement cycle — the owner's rulings on P-60…P-65 (2026-09-07)

> **Status: ruled and being applied.** The six questions the PWB cycle
> report gathered ([`PWB-CYCLE-REPORT-DECISION-PACKET.md`](PWB-CYCLE-REPORT-DECISION-PACKET.md),
> register rows P-60…P-65) were answered by the owner in one reply on
> 2026-09-07, after every item had passed independent adversarial review in
> a local questionnaire packet (git-ignored, `.syzygy/local/`; its six raw
> reviews are retained beside it). This record owns the rulings; the
> packet remains the question each was ruled on. Where this file and the
> owner's own words differ, the words win, and they are quoted in full
> below. Nothing here is an act: no digest is bound, no specification,
> policy or registry changes, and no acceptance-record row is added.

## The owner's reply, verbatim

Claude Code chat, 2026-09-07, about 01:20 +08:00:

> Follow your recommendations for all of the above. For the butler page
> change, dispatch a subagent to do that

Evidence snapshot the items were reviewed and answered at: syzygy
`a396f0e` (main, clean), Butlers `13d269b` (main, clean).

## The six rulings

Each row is its own decision; agreement to one is not approval of another.
"A" is the recommended arm in every case, as presented.

| Row | Ruled | What it means | Applied by |
|---|---|---|---|
| **P-63** (byte ceiling) | **A** — implementation-only trim of the Polaris human page, built and measured **before** the P-60/P-61 repairs merge into Butlers main; target about 420 KB (the repairs add 418–443 KB against 44 KB of headroom on the tailnet form). If the measured saving falls short, a registry act packet (arm B: raise the ceiling, or narrow the declared population) is drafted at once and the repairs wait. | Direction only; the owner did not rule the trim's design. P-52 (whether new POC beads may be filed) was not ruled by this reply: the bead was filed on the item's own boundary, which named that as the path unless P-52 is ruled the other way. | Bead `syzygy-1z3.27` filed as a child of `syzygy-1z3` (POC improvement cycle); `syzygy-1z3.22` (the walkthrough) now depends on it. |
| **P-60** (Butlers V1 page) | **A** — repair the page in Butlers: nine edits over eight lines (five colon-for-dash forms, four duplicated labels disambiguated). No Syzygy act. | **Boundary edited by the owner:** the item said the commit is the owner's and no agent edits Butlers; the owner directed that an agent be dispatched to make the change. Recorded as an owner edit; the edited boundary took a fresh scope and recommendation pass before routing. The agent works on a branch, never Butlers main; push, pull request and merge stay the owner's, and the merge follows the P-63 measurement. | A dispatched agent, on a Butlers branch (see "Routing" below). |
| **P-61** (two topology tables) | **A** — bold the seven first cells (two rows of the Frontend routes table, five of the identity table); 87 topology items. Not B (relocating the tables drops seven documented rows from the model with no Unknown raised), not C (the seven withheld roster files are untouched; the roster stays a disclosed Unknown and gates no readiness limb), not D (no grammar act). | Same owner edit as P-60, same branch, its own commit. | Same dispatched agent. |
| **P-65** (repair epic) | **A** — close `syzygy-1z3.24` now. Criterion 4 (a retained exact-head run passing readiness) is unmet at close and is carried by `syzygy-1z3.22`'s own readiness gate and by the trim bead. | The walkthrough is not offered, scheduled or performed; it stays gated on P-60, P-61, P-63 and a green preflight. | `bd close syzygy-1z3.24`, 2026-09-07, with the per-child evidence in the close reason. |
| **P-64** (walkthrough guidance) | **A** — one sentence in the owner's words that following an *Exact source* link is a permitted walkthrough step, inserted below line 79 of the candidate walkthrough packet (in "What is already in place", where it shifts no retained review's line citation). | **The sentence has not been supplied.** The reply chose the arm and gave no wording; no agent drafts it on the owner's behalf (VIS-4). Nothing is inserted until it arrives. | Waits on the owner's sentence. |
| **P-62** (Spec and Spine index) | **A** — add an index page at openspec/README.md in Butlers, in the shape of the other four pillar indexes, so the pillar is discovered and the whole-shape claim can become Observed. | The owner's "butler page change" is read as covering this page too; it is written by the same dispatched agent as its own commit on the same branch, so the owner can drop that one commit if the reading was wider than meant. The index links only to directories or to nothing: a file link inside openspec/ would be read by the discovery rule as a named source. **This item delegates drafting, not just application:** the post-answer review named that as a VIS-4-shaped trade-off the other two do not carry, so the commit is a proposal — its full text goes before the owner verbatim, it is final only when the owner has read and approved it or merged it knowingly, and the agent writes no descriptive claim beyond directory names, counts and the question each answers. | Same dispatched agent, separate commit. |

## Sequencing, in one sentence

The trim (`syzygy-1z3.27`) is built and measured first; the Butlers branch
exists but merges only after that measurement, or after the owner
knowingly accepts an interval in which the page serves nothing; the
walkthrough is re-offered only when the fresh-checkout demo reports ready.

## Sentences in the canonical records that were wrong

The review found six wrong claims and one misleading default standing in
seven places in the two records the owner would otherwise have acted from.
Each is marked in place, quoted and dated, by the same pass that recorded
these rulings:

- Register row P-61 and cycle-report §P-61 attributed the empty catalog and
  topology populations to the roster withholding and said readiness
  reports "two limbs". The roster withholding gates no limb; the empty
  populations come from the two failing pages (the V1 page's catalog
  grammar and the components page's table grammar), and readiness reports
  three limbs.
- Register row P-63's default, "the page serves until it crosses the
  ceiling, then reports the breach", misleads by omission: at the ceiling
  the page serves nothing (HTTP 503, readiness false) and the walkthrough
  is unreachable. Its arm (c), "let the limit ledger report the breach", is
  false: no ledger sees a response-ceiling breach; the 503 body of the
  breaching request is the only trace, and nothing is logged. The resource
  ledger is the input-side reader budget and never sees a response
  ceiling.
- Cycle-report §P-63's "the limit ledger records a breach and the page
  degrades honestly" and its arm (c) are false for the same reasons.
- The cycle-report packet's "None depends on another" is wrong for one
  pair: P-63 is a prerequisite of any P-60/P-61 arm that lands items.

The register rows themselves moved to
[`DECISION-HISTORY.md`](DECISION-HISTORY.md) §"Resolved on 2026-09-07",
where the wrong sentences are quoted beside the correction.

## Routing

- **Syzygy** — this record; the six register rows moved to
  `DECISION-HISTORY.md`; the cycle-report packet banner-marked answered
  with its stale sentences marked in place; bead `syzygy-1z3.27` filed;
  `syzygy-1z3.24` closed. All in one commit on 2026-09-07 (its hash is in
  `git log`, not here).
- **Butlers** — a dispatched agent applied P-60 and P-61 as two commits
  and P-62 as a third on one branch in the Butlers repository, from
  `13d269b`, without pushing, opening a pull request, or touching main.
  Branch pwb/p60-p61-p62-doc-repairs (worktree under ~/.butlers-worktrees):
  f3948af88 (P-60, the V1 page), 6cbc9e785 (P-61, the components page),
  952ee4083 (P-62, the new index, a proposal awaiting the owner's read).
  The built extractor over that worktree yields 65 catalog entries and 87
  topology items; the owner merges.

## External actions intentionally not taken

No push to any remote, no pull request, no merge into Butlers main, no
change to the POC daemon on loopback port 7478, no Syzygy act, no
registry, policy, specification or grammar change, no walkthrough offered,
no reading of any withheld roster file or manifesto body.
