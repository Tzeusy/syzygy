# Round-2 dispositions — agent-provider statement, version 2

> **Candidate — binds nothing.** This record dispositions review notes. It
> performs no act, approves nothing and changes no reviewed byte.

Review: `docs/reviews/R-DOSSIER-AGENT-PROVIDER-V2-2-RAW.md`, verdict
`CONFIRM WITH EXCEPTIONS` (raw line 4), over commit `5db1dd72`. The raw's
head names the manifest file it read; cite it from there. It confirms the
record bytes at the manifest row, the same bytes round 1 confirmed. All six
round-1 findings are repaired. Round 2 has three findings, each marked
`note`, and none marked revise. Under the owner's notes-only rule
(`decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1), that round
clears the package at its manifest. The record and manifest are unchanged.

## Note 1 — the `--tool` prerequisite has landed (taken)

The reviewer asked the delta to cite the fix commit and say the
precondition is met. The lead directed that change and it was made after
the review, in the delta only. `SEMANTIC-DELTA.md` now says the
prerequisite is met by #406, merged at `ff9a19b6` on 2026-10-08, and cites
`sessionStatementRefusal` (`session-handover.ts:225`, called at `:145`).
That is a prose edit to bytes round 2 read. It does not touch the record or
the manifest, and the builder's `--check` still reports both current.

## Note 2 — the aggregate record does not name version 2 (correction)

`SEMANTIC-DELTA.md` lines 103–104 say a version-2 form built in version 1's
pattern "would read version 1's act record, and its `ACCEPTANCE-ACT-RECORD.md`
block, as naming version 2". The first half holds. The second does not
[Observed by the reviewer, probe C]:

- `namesDigestBoundAct` exempts `ACCEPTANCE-ACT-RECORD.md` from its text
  check (`package-reader.ts:572`).
- Version 1's block carries the basename only in table rows, which the
  field-line pattern (`:574`) does not match.

**Read as:** "would read version 1's act record as naming version 2". The
installer must still exempt version 1's act record in both directions, as
the bullet says.

## Install requirement — version 2's own act prose and stems (note 3)

**This adds to the delta's install list, and the owner should read it beside
the act.** Every reader sweeps every decisions file, so the version-2 act
record's own wording can close gates [Observed by the reviewer, probes D and
E]:

- **No other family's stems in the version-2 recorder's template.** An act
  record citing the egress precedent's package path refuses the whole
  admission read (`invalid-records`). That closes observation consent for
  every repository. One citing the project-documentation class act's file
  name refuses that class act, which also refuses the admission read. The
  delta's own Why cites both, so the act record must not copy it.
- **Version 2's new stems checked against the decisions tree.** That means
  the file stem, identity stem, label and title. A title that already
  appears in a decisions file refuses version 2 itself. Row P-106 in
  `decisions/PENDING-OWNER-DECISIONS.md` and the blockers packet both
  carry version-2 title wording today. Either choose stems that appear in
  neither, or pin those lines with `citedRows`, as the P-104 precedent does
  (`package-reader.ts:550`). `sittingForm` passes no `citedRows` today
  (`gate-sources.ts:175-185`). Any line-level exemption, including the
  both-directions exemption the delta asks for, needs that parameter
  threaded through.
- **`expectFollowsTree` covers both versions in the install commit.** The
  real-tree pin in `gate-acts.test.ts` lists version-1 keys only today. The
  title collision fails only once that pin learns version 2's record. The
  first two hazards already fail `real-tree.test.ts`'s "refuse nothing" test
  in CI.
