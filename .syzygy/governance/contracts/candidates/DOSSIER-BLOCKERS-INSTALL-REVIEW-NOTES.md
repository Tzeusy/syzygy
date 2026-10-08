# P-105 and P-106 record and install — review notes

> **Candidate — binds nothing.** This is the sibling record for the notes of
> the fresh-context review of PR #409, which recorded the owner's acts P-105
> (screening scope version 3, variant `all`) and P-106 (agent-provider
> statement version 2) and installed both. Under the owner's notes-only rule
> (`../../decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1), a round
> with no revise-level finding clears the exact bytes it read, and its notes
> go in a sibling record, never into the reviewed bytes. The two act records
> and the aggregate block in `ACCEPTANCE-ACT-RECORD.md` are bound by the acts
> they record, so this file edits none of them. It signs nothing off, adopts
> nothing and performs no act: only the owner's own acts do that (VIS-4). It
> quotes no act digest, so nothing here is registered in
> `check_governance.py`.

Reviewed record: docs/reviews/R-PR409-DOSSIER-BLOCKERS-INSTALL-1-RAW.md

## What was confirmed

- **Subject:** PR #409, commits `4cd1ded7`, `557e7074`, `53b10a82` and
  `c4a5921d` over base `c88bbf9e`.
- **Reviewed commit:** `c4a5921d3d3fec1ff25c86083321de5a0f7db123`.
- **Verdict:** `CONFIRM WITH EXCEPTIONS`, on line 2 of the raw named on the
  `Reviewed record:` line above, with six findings, each a note. #409 merged
  at `f7d1ea7f`.

## The notes and what happens to each

### N1 — "Recorded at" is the act instant

The two act records carry the owner's answer instant, rounded up to the
whole second, under the label `Recorded at (UTC)`; the records were written
about an hour later. The gate reads the value as the act's effective
instant, which is correct. The bound records keep their label.

**For future recorders:** label the field "Act instant (UTC)" and, where a
recorder's docstring says it writes "the UTC instant of recording", say
instead that it writes the act instant given by `--instant`. If the writing
time matters, record it as a separate field. Two acts answered in one
question may share one instant; a template need not refuse that.

### N2 — version 2's act record understates its difference from version 1

The provider record says version 2 differs from version 1 "in nothing else
but its draft date, version and supersession line" beyond the added
`project-documentation` class. A word-diff also shows two banner lines: the
template path (the version-1 template to its `-V2` successor) and the
builder path (`build_dossier_local_agent_acts.py` to
`build_dossier_agent_provider_v2.py`). Neither has consent effect.

**For future recorders:** derive the "differs in nothing else" sentence
from a script's word-diff of the two statements, and list every differing
line class, presentation lines included: banner template path, banner
builder path, draft date, record version, content classes, supersession
line.

### N3 — the aggregate block says the gates are re-pointed "by a separate change"

The sentence is template text inherited from the earlier provider and
screening blocks. For P-105 and P-106 the read gates were re-pointed by the
installer in the same commit as the records, as the decision packet's
decision 1 requires.

**For future recorders:** say "the read gates are re-pointed by the
installer in the same change" when the installer runs in the recording
commit, and name the separate change only when one exists.

### N4 — the extension shape belongs to the exemption reader

Taken in the follow-up PR. `readCodeContentExemption` in
`packages/polaris-generation-core/src/public-source-classification.ts` now
refuses any `exemptExtensions` entry that is not a dot followed by no `/`
and no whitespace, so it no longer relies on its callers' own check. A test
in `public-source-exemption.test.ts` covers an extension carrying `/`, and a
rule-6 mutant removing the check is killed; the record is under
`docs/evidence/`.

### N5 — no retained fresh-clone battery transcript

Taken in the follow-up PR: a fresh-clone battery transcript for the merged
head `f7d1ea7f` is retained under `docs/evidence/`, run on disk with
`TMPDIR` on disk so the shared `/tmp`'s inode exhaustion cannot affect it.

### N6 — the register note does not record the owner's P-107 answer

Not taken here. P-107 belongs to another lane (PR #408), which records it.
