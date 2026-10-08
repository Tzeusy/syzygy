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

Reviewed record: docs/reviews/R-DOSSIER-AGENT-PROVIDER-V2-2-RAW.md

*(Added 2026-10-08 at install: the line above and the numbered headings
below are the form `scripts/record_dossier_agent_provider_v2_act.py` reads,
through `record_versioned_signoff.validate_disposition`; no disposition
changed. Each heading kept its words after the number. The install outcome
of each note is in "Install notes" at the end.)*

## 1 — Note 1 — the `--tool` prerequisite has landed (taken)

The reviewer asked the delta to cite the fix commit and say the
precondition is met. The lead directed that change and it was made after
the review, in the delta only. `SEMANTIC-DELTA.md` now says the
prerequisite is met by #406, merged at `ff9a19b6` on 2026-10-08, and cites
`sessionStatementRefusal` (`session-handover.ts:225`, called at `:145`).
That is a prose edit to bytes round 2 read. It does not touch the record or
the manifest, and the builder's `--check` still reports both current.

## 2 — Note 2 — the aggregate record does not name version 2 (correction)

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

## 3 — Install requirement — version 2's own act prose and stems (note 3)

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

## Install notes

*(Added at install, in the commit that records the version-2 act. The
notes above are unchanged; this says what the install did with each.)*

- **Note 1, taken before the review closed.** No install change.
- **Note 2, read as stated.** The install exempts the two act records from
  each other:
  - version 2's form reads past version 1's act record at version 1's exact
    render;
  - version 1's statement form reads past version 2's act record at
    version 2's exact render.

  Both use `exemptRecords` in `gate-sources.ts`. A byte-identical copy of
  either record under any other file name is not exempt, and it names the
  other version. `gate-acts.test.ts` holds both directions and the copy
  case.
- **Note 3, taken.**
  - The version-2 recorder's template cites no other family's package path
    or class-act file name.
  - The version-2 stems are new: the file stem, identity stem, label and
    title. None of them appears in a decisions file before the act is
    recorded, and after it they appear only in the version-2 act record
    and its `ACCEPTANCE-ACT-RECORD.md` block. Row P-106 is resolved
    without them.
  - Because the stems were chosen clean, no `citedRows` pin is needed, and
    `sittingForm` still passes none.
  - `expectFollowsTree` in `gate-acts.test.ts` runs worlds holding version
    2's act, both with and without the rest of the sitting's acts.
  - The real tree passes `real-tree.test.ts`'s "refuse nothing" test with
    the act recorded.
