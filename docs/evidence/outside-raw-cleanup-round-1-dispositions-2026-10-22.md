# Outside-raw cleanup: review dispositions, round 1

[Observed] This record dispositions the CC-REV-1 review of `syzygy-bpyt.4.12`
(pull request #513). In `packages/polaris-dossier/src/waiting-sessions.test.ts`,
the row "the record names a review outside the records root" now builds the
raw's path once. It registers its removal before it writes the raw, so the
file-level `afterEach` deletes the `dossier-signoff-*-outside-RAW.md` file the
row writes beside its temp root. The change also adds the evidence record
`docs/evidence/waiting-sessions-outside-raw-cleanup-2026-10-22.json`. No
production file changes.

| Round | Raw | Verdict (line 2) | Reviewed commit (line 3) | Subject (line 4) |
|---|---|---|---|---|
| 1 | `docs/reviews/R-GP-IMPL-OUTSIDE-RAW-CLEANUP-1-RAW.md` | `CONFIRM WITH EXCEPTIONS` | `a670f988` | `r1-review.diff` sha256 `5430edc6184be10f9305ce856d7519d6294a00112d5d3266b5c456158cc03130` |

The subject equals `git diff a0406967 a670f988`. Main had not moved at
landing, so the branch took no merge. `git diff origin/main HEAD | sha256sum`
printed the same digest before the landing commit.

The reviewer found "No F (blocking) findings." (section 4), with four notes.
Under the owner's notes-only stopping rule
(`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
section 1), the round clears the exact bytes it read, and those bytes are not
edited. This record sits beside them. It is an implementation record and binds
nothing.

Revise-severity findings open: 0

## Retained review evidence

The reviewer's tools and results are kept under
`docs/evidence/outside-raw-cleanup-review-2026-10-22/`. Each file's sha256
equals the one the raw gives for it (section 3, items 3, 5, 9, and section 5):
- `tools/rev513.py` and `rev513-results.json`: ten runs of
  `waiting-sessions.test.ts` alone, each in a fresh TMPDIR listed before and
  after. They cover the unmutated base and fix, R1 at both, R2, T-eager,
  T-drop, and the throw, retry and timeout probes.
- `tools/proposal.py` and `proposal-results.json`: N2's proposed row, checked
  in scratch.
- `tools/identity.py`, which gives the per-path blob comparison behind
  section 5's "None", and `tools/names.py`, which gives the 116 test names at
  base and fix.

The per-run Vitest JSON reports, the typecheck log and the two
`check_governance` logs are not kept. The raw quotes their result lines.

## N1: class and owner notice

[Observed by the reviewer] The PR declared "class none declared; class 1
possible by the #506 N3 precedent". The reviewer rules **class 1** (authority
boundaries). The changed row is the rule-6 kill evidence for the review-path
predicate of `appliedSubjectHolds` (`waiting-sessions.ts:110`). That predicate
is one leg of `waitModeSignedIn`, the v1.2 owner sign-off gate. The reviewer
considered class 4 and does not rule it. GP-Q0's three extras:
- The differential is degenerate. `waiting-sessions.ts` is byte-identical at
  every commit in question, so any old-versus-new differential is identical
  by construction.
- The per-predicate mutant is met: R1, which drops the review-path check, is
  killed at base and at fix.
- The owner notice was pending.

**Disposition:** the declared class is superseded by the reviewer's ruling.
The PR's evidence record is not edited. The owner notice for #513 is posted on
`syzygy-bpyt.10` at landing.

## N2: the review-path row covers only a leading `..`

[Observed by the reviewer] The reader refuses any `..` segment. The row
exercises only `Review: ../<root>-outside-RAW.md`, so mutant R2, which checks
only the first segment, survives the whole file at 116/116. The gap was there
before this change; the change neither causes it nor widens it. The reviewer's
T-eager probe also shows that the kill depends on the raw existing until the
gate is asked a second time. Removing it right after the write silently loses
R1's kill.

**Disposition:** filed as `syzygy-bpyt.4.16` (P3, test-only, class 1). It adds
one row whose record names `docs/../../<root>-outside-RAW.md`, records R1 and
R2 against it, and extends the reviewed row's comment to say that the raw must
exist until the gate is asked. It cannot ride in this PR, because AC2 fixes the
assertions and AC3 fixes the count.

## N3: AC3's wording

[Observed by the reviewer] The bead's AC3 reads "Tests +0 ~0 -0; class none".
In this campaign, `~n` counts the expanded tests whose bodies changed while
their titles stayed the same. Exactly one row's callback changed, and the 116
names are the same at base and fix.

**Disposition:** AC3: `Tests: +0 ~1 -0` is correct (one row's callback
changed, titles unchanged), and the class is 1 by the reviewer's ruling (N1).
AC3's intent, no test added or removed, holds. The bead closes with this
wording. The PR is not edited.

## N4: no mechanical guard against a recurrence

[Observed by the reviewer] No test or CI step fails if a test writes outside
its temp root again. With the cleanup line removed (T-drop), the suite stays
116/116 green, and only the listing shows the stray. Three leaks of this class,
`syzygy-bpyt.4.10`, `4.11` and `4.12`, were each found by a person listing a
TMPDIR.

**Disposition:** filed as `syzygy-bpyt.4.17` (P3). It adds a check that runs
the unit tier once under a fresh private TMPDIR and fails on any leftover other
than `node-compile-cache`, with a rule-6 run against this file's base bytes
(`waiting-sessions.test.ts` at `a0406967`). It depends on `syzygy-bpyt.4.10` and `syzygy-bpyt.4.11`. If
`syzygy-bpyt.4.4`'s `tempDir()` lands first, it is the natural owner.

## Acceptance criteria (raw section 6)

- AC1 met: at the fix, seven fresh-TMPDIR runs leave no `dossier-*` entry
  (unmutated, R1, R2, throw, retry, timeout and T-eager). The base reproduces
  exactly one.
- AC2 met: no assertion line changed, and R1 is killed by the row at the fix
  with the same first line as at base.
- AC3 met in substance, with the wording corrected above (N3).
