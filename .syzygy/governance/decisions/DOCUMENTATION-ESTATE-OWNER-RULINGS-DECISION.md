# The written estate — the owner's rulings on P-54…P-59 and P-66 (2026-09-07)

> **Status: ruled, and applied except where the arm itself defers.** The
> seven questions gathered by the documentation-estate packet
> ([`DOCUMENTATION-ESTATE-DECISION-PACKET.md`](DOCUMENTATION-ESTATE-DECISION-PACKET.md),
> register rows P-54…P-59 and P-66) were answered by the owner in one reply
> on 2026-09-07. This record owns the rulings; the packet remains the
> question each was ruled on and is not the state of any of them. Where this
> file and the owner's own words differ, the words win, and they are quoted
> in full below. **Nothing here is an act**: no digest is bound, no
> specification, policy or registry changes, and no acceptance-record row is
> added.

## The owner's reply, verbatim

Claude Code chat, 2026-09-07:

> Agreed with your  recommendstions in DOCUMENTATION-ESTATE-DECISION-PACKET.md

Evidence snapshot the items were ruled at: syzygy `4aa60ee` (main, clean).

The reply agrees with the packet's recommendations, so each row's ruling is
that row's recommended arm as the packet stated it — nothing wider. Three of
the seven recommendations are themselves conditional or deferred, and this
record keeps those conditions rather than resolving them in the owner's
favour.

## The seven rulings

| Row | Ruled | What it means | Applied by |
|---|---|---|---|
| **P-54** (OpenSpec config) | **(b)** — delete the vendor example, keep `schema: spec-driven`, and rule that this project's agent-facing context travels through `AGENTS.md` and the governed plane, not tool config | No `context:` block is ever written here; a future one would be a second home for an answer `AGENTS.md` owns, invisible to anyone not reading tool config (CC-REV-3) | `openspec/config.yaml` trimmed 2026-09-07; a comment in the file states the ruling so the block is not reintroduced |
| **P-55** (two empty directories) | **(b)** — rule that this project does not use the archive and spec-materialization steps, and give each empty directory a one-line README saying so | `changes/` is the permanent home; "what is specified today" is answered by `PROJECT-STATUS.md` and the governed plane. Neither directory was tracked by git before this (git stores no empty directory), so the READMEs also make them exist in a clone for the first time | `openspec/specs/README.md` and `openspec/changes/archive/README.md`, added 2026-09-07 |
| **P-56** (spent prompt at the root) | **(b)** — leave the file at the repository root and mark its head: what it opened, that the stage is finished, and why it stays | Not (a): the packet's own argument is that (a) edits a decision record to buy a tidier root listing, and the trade runs the wrong way. The citation that pins it here is wrapped across a line break in the citing record, which is why a basename sweep does not find it | A head note on `syzygy_begin_specification_stage_capability1_prompt.md`, added 2026-09-07 |
| **P-57** (`openspec/` has no door) | **(a)** — authorize an agent to write a top-level README under `openspec/` as navigation only, banner-marked never authority, **with the owner's review of its text reserved** | The reservation is part of the arm, not a formality. The page is committed so it is reviewable in place, and it says on its face that it awaits that review. It is the governed plane's only agent-authored page; it names which change is bound and by which act, and quotes no requirement, digest or verdict | `openspec/README.md`, added 2026-09-07. **Awaits the owner's review** |
| **P-58** (two front doors, two founding pairs) | **(a)**, *folded into act 4 whenever the owner next takes it up* — make the overview name VIS-1 and VIS-2 by identifier and keep the activity-is-not-proof sentence as prose | The arm defers by its own terms: an agent may prepare the delta, only the owner performs the act. `.syzygy/intent/OVERVIEW.md` is byte-unchanged and was not opened for editing. The ruling does not schedule act 4 | Prepared delta OVW-1 (with P-59), not applied |
| **P-59** (the overview says nothing is implemented) | **(a)**, *folded into act 4 alongside P-58* — replace the false sentence with the route to `PROJECT-STATUS.md` the next paragraph already takes | Same deferral, same one act argument, deliberately one delta: a second edit later would retire whatever confirmation the first earned | Same delta OVW-1, not applied |
| **P-66** (CC-SPEC's amendment banner) | **(b)**, with **(a)** riding along if a CC-SPEC amendment ever comes — rule it a permanent, disclosed blemish | The operative clause at lines 245-248 is the authority and names all nine phase rules; the banner is history, and history that under-counts is recorded rather than repaired. The bytes are frozen — the file's sha256 is row 7 of the general trusted-bootstrap transaction manifest — so no correction is possible without a standalone act, which arm (c) offered and the owner did not take. **This record and the history row are the disclosure**; the next audit should not re-raise it | Nothing edited, by design. Disclosure only |

## The prepared delta, and what performing it would cost

P-58 and P-59 travel as one drafted delta,
[`PROJECT-OVERVIEW-ACT-4-SEMANTIC-DELTA.md`](../contracts/candidates/PROJECT-OVERVIEW-ACT-4-SEMANTIC-DELTA.md)
(OVW-1), in the candidate tree where the other deltas live. It quotes the
current and proposed text of both passages exactly, states its class claim so
a reviewer can contradict it, and carries a six-step migration plan whose
first step is the owner's. Two things about it are worth reading before
taking act 4 up:

- **Applying the edits and performing the act are separable.** Steps 1-5 of
  the plan leave the page correct and act 4 still open and unperformed. The
  ruling authorizes the repair, not the act.
- **The digest check will fail between step 1 and step 3.**
  `scripts/check_governance.py` recomputes the overview's sha256 against the
  digest quoted in the acceptance record, so the act-4 row must be re-minted
  in the same logical change — that row's own house form, which has carried
  four such re-quotes already.

No review has been run against the delta, and no reviewer is assigned.

## What this pass did not do

- **It did not touch `.syzygy/intent/OVERVIEW.md`.** Not one byte. Its
  current hash still equals act 4's argument as recorded.
- **It did not edit `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`,** whose
  banner P-66 is about. Those bytes are a performed act's argument.
- **It did not perform, offer, schedule or prepare any act**, and added no
  row to `ACCEPTANCE-ACT-RECORD.md`.
- **It did not archive or materialize any change** under `openspec/`, which
  P-55 arm (b) is precisely the ruling not to do.

## One thing the packet said that this record corrects

The packet's head says the seven questions are answerable "in one reply, or
any subset; none depends on another." That is true of the questions but not
of the applications: **P-55 and P-57 are coupled.** The `openspec/` index
written under P-57 has to say what the two empty directories mean, and what
they mean was only settled by P-55. Ruled the other way — P-55 (a), the
lifecycle adopted — the index would have described a tree that was about to
be restructured. The two were ruled together, so nothing went wrong; the
coupling is recorded because the packet denied it.

## Where the rows live now

The seven register rows moved out of
[`PENDING-OWNER-DECISIONS.md`](PENDING-OWNER-DECISIONS.md) into
[`DECISION-HISTORY.md`](DECISION-HISTORY.md) on 2026-09-07, under a dated
resolved-on section. The open register is smaller by seven; its head note
carries the recount.
