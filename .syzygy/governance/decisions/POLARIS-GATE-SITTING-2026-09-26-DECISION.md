# Polaris gate sitting — the owner's answers on the review bar, the `.21`, `.18`/`.22` and `.23` open questions, and N8's container-shape draft (2026-09-26)

> **Plain owner direction. Performs no act.** This record answers six
> questions: when a confirmation review clears a candidate package's bytes;
> the PWB-REQ-020 reading `syzygy-dov.21` rests on; `.18` open question 6,
> which the 2026-09-23 open-questions record held for the `.22` review;
> `syzygy-dov.23` open questions 1–3; and whether N8's container-shape
> change may be drafted. It binds no digest. It amends no specification,
> policy or registry byte, adds no row to `ACCEPTANCE-ACT-RECORD.md`, and
> registers nothing. It offers no phrase. Each package still takes effect
> only through its own owner act, after the review it owes.

## How the answers were given

Date: 2026-09-26. Owner: Tzeusy. Channel: the Claude Code CLI. The owner
answered structured questions in two batches, drawn from a git-ignored
local questionnaire under `.syzygy/local/` (the gate-sitting packet dated
2026-09-23). Each answer below is the option label the owner
selected, quoted byte-for-byte. The owner added no notes. Every selection
was the option presented as recommended.

Before presentation, independent fresh-context reviewers passed every item's
problem scope and recommendation. Items 2, 4 and 5 came back Revise and
were repaired: a doctrine citation, a mischaracterized reason the question
was open, and a CC-REV-2 scope overstatement. A second fresh reviewer then
passed all three. The raws are retained beside the questionnaire.

Evidence snapshot: `origin/main` at `3cc2d5c`. Recorded at `9162d62`. Of the
paths these answers rest on, one changed in between. `fe71755` (#107)
regenerated the `.23` manifest to carry a status-page sentence authorized
separately, and the package's packet was updated to match; the digest to
cite is the one that package's `--check` reports now. No answer below depends on that
digest.

## 1. When a confirmation review clears a package's bytes

| Question | Owner's answer (verbatim) |
|---|---|
| When does a review clear a package for sign-off? | "Notes-only clears (Recommended)" |

As presented, the option read: "A round clears the exact text it read if
nothing asks for a change. Its notes are answered in a record beside the
package, not by editing it. .22 is ready now; .21 needs one final round.
The recording script gets changed and reviewed."

Reading:

- **When a round clears its bytes.** A confirmation round clears the exact
  bytes it read when it raises no revise-severity finding, that is, nothing
  that asks for a change. Such a round returns either `CONFIRM` or
  `CONFIRM WITH EXCEPTIONS` with notes only.
- **Where its notes go.** Its notes are dispositioned in a record beside the
  package, never by editing the reviewed bytes. Editing them would retire
  the clearance.
- **Exceptions already ruled on.** An exception the owner has already ruled
  on counts as dispositioned by that ruling.

This is CC-REV-6's bar: every revise-severity finding is fixed or overruled
by the owner. No written policy requires a bare `CONFIRM`.

- **`.22`.** Round 6 (`docs/reviews/R-PWB-MACHINE-VIEW-DELTA-CONFIRMATION-5-RAW.md`,
  over `5affbee`) clears the machine-view package's current bytes.
  - Its one exception is the RFC6-21 reading the owner chose on 2026-09-23,
    which is dispositioned by that ruling.
  - The package's bytes are unchanged since `5affbee`.
  - Its landing position is 3 of 4, so its act still waits for the
    regeneration the 2026-09-23 landing order requires. A regenerated
    manifest is new bytes and needs its own round under this rule.
- **`.21`.** The opening-band package's current bytes (`3369410`) carry no
  review. One further round over them is next. If that round raises no
  revise finding, its notes are dispositioned beside the package, on the
  bead or in a sibling file. `SEMANTIC-DELTA.md` §Review stays the record
  for rounds 1–10 and says nothing about that round.
- **The recorder.** `scripts/record_pwb_behavior_amendment_acts.py` accepts
  only an exact `Verdict: CONFIRM` line (line 244). It may be changed to
  accept a notes-only `CONFIRM WITH EXCEPTIONS` bound to a disposition
  record. The change needs its own mutation fixtures and independent review
  before any ceremony relies on it.

## 2. The PWB-REQ-020 reading `.21` rests on

| Question | Owner's answer (verbatim) |
|---|---|
| Which reading of PWB-REQ-020's "and disclosure"? | "Wider reading (Recommended)" |

Reading: "disclosure" in PWB-REQ-020's parity case reaches any disclosure
Polaris presents, not only the PWB-REQ-022 judgment state. The case reads
"every PWB-REQ-005 authority state and PWB-REQ-022 judgment state and
disclosure". The opening band's aggregate is therefore inside the parity
population as the `.21` package already assumes, and no PWB-REQ-020
amendment is needed. This settles round-5 finding 27 of the `.21` review.

## 3. The briefing's "one named subject" — `.18` question 6, `.22`

| Question | Owner's answer (verbatim) |
|---|---|
| What counts as one subject? | "One claim (Recommended)" |

Reading: the briefing ceiling's one required subject is one exact
project-shape claim, identified by its full claim id. Fields from the same
evaluation that are joined in stay derivable context; they are not extra
subjects.

This confirms the reading the `.18` package's proposed registry bytes
already carry. The `.22` package's bytes are silent below route and
evaluation, so they admit it without edit. Neither package's bytes move.
This answers `.18` question 6, which
`POLARIS-GATE-PACKAGE-OPEN-QUESTIONS-2026-09-23-DECISION.md` §2 held. That
record is not edited.

## 4. Slice 4 of M6 — `.23` question 1

| Question | Owner's answer (verbatim) |
|---|---|
| Does sign-off alone release slice 4? | "Sign-off is enough (Recommended)" |

Reading: once the edit/repair deletion-account scenario is signed off,
M6 slice 4 (`syzygy-dov.6.3`) is implemented under the existing
`POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md`, as P-73 Q6 in
`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md` reads. No further
implementation act is needed.

## 5. The status-page count — `.23` questions 2 and 3

| Question | Owner's answer (verbatim) |
|---|---|
| How should the 177 → 178 digit be handled? | "Bundle + full recount (Recommended)" |

Reading: the `PROJECT-STATUS.md` digit stays in the `.23` package. Before
sign-off, a small script, with its own test, recounts the effective
composition's full scenario total from scratch, so the number the page
asserts is checked rather than carried forward. The package's packet says
the selected arm needs its own review; that review covers the recount.

## 6. N8's container-shape change

| Question | Owner's answer (verbatim) |
|---|---|
| Draft the spec change that lets each project declare its own formats? | "Draft it now (Recommended)" |

Reading: agents may draft a candidate package now. It would let a project's
profile declare its own container shapes, instead of the shapes written
into PWB-REQ-002's reader definitions.

- **What it contains:** a CC-REV-2 amendment to PWB-REQ-002, plus any
  registry or policy act it needs.
- **Butlers:** its profile declares today's shapes as they are.
- **Afterwards:** it is independently reviewed and brought back to the
  owner.

Drafting binds nothing. This record admits no shape, reads no new source,
and performs no act.

## What this does not do

It performs no act, offers no phrase, and waives no review a package names.
It edits no earlier record. It does not change the 2026-09-23 landing order
(`.21` → `.30` → `.22` → lane B).
