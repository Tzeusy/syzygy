# History review 1 — reconciliation recorder

Verdict: REVISE
Reviewed commit: f5fdde79da4c08f5d6a47fee2cb9ff3199b90f90
Reviewer: independent fresh-context agent, 2026-09-28

Recorder bytes reviewed (sha256 computed by script from the reviewed commit):

- `scripts/record_polaris_understanding_adoption.py`: `6df073ed8b89710d288c02afa1a33d20cf3c63a3ace39e1b146a9fdc069fc85b`

## Scope

Subject: `git diff a9a0830 f5fdde7` — `scripts/record_polaris_understanding_adoption.py`
(+53/−6), new `docs/evidence/polaris-understanding-reconciliation-2026-09-28/HISTORY-READING.md`
and `history-reading-rule6.json`. Governing references read: owner ruling
"R1: read as history" (`OWNER-ADOPTION-2026-09-28-TREE-STYLE-RESTYLES.md:27-30`),
the reconciliation `README.md`, `REVIEW-RAW.md`, and the
`CONFIRM CRAFT AMENDMENT: CC-SPEC@` lines of `ACCEPTANCE-ACT-RECORD.md`.
All experiments ran in a scratch clone at the reviewed commit
(`histrev/clone`); the reviewed worktree was not modified by this review.

## Facts established

- [Observed] C1 is `9322656dcfcc00b436868e93f2754f812dfa9db9` (`REVIEW-RAW.md:4`);
  the raw carries 13 path/digest bindings (12 `FROZEN_PATHS` + `review-inputs.json`),
  matching HISTORY-READING.md:3 "thirteen inputs".
- [Observed] CC-SPEC at C1 hashes (sha256sum over `git show`) to the digest
  bound at `REVIEW-RAW.md:22`, and the current file hashes to the same digest.
  The recorder at C1 and at `a9a0830` hashes to the digest bound at
  `REVIEW-RAW.md:32`; at the reviewed commit it hashes to the digest in the
  binding line of this raw's head, which differs from the C1 one.
- [Observed] `ACCEPTANCE-ACT-RECORD.md` has exactly two lines matching the
  anchored `POLICY_ACT` regex: line 66 (act 6, performed 2026-08-17, the
  pre-amendment CC-SPEC digest) and line 95 (under "Performed nested row-5 act argument, bound by
  the outer transaction ceremony", general trusted-bootstrap transaction
  performed 2026-09-01, the digest
  equal to the C1 CC-SPEC blob). Both are performed; the C1 digest is
  satisfied by line 95.
- [Observed] `--selftest` exits 0: "3 valid states …; 41 trust-boundary
  mutations refused". `--check` exits 1 with "no history review binds the
  current recorder", as expected before this raw is retained.
- [Observed] End-to-end in the scratch clone: an untracked
  `HISTORY-REVIEW-1-RAW.md` is refused ("history review not retained"); once
  committed with `CONFIRM` and the current digest, `--check` exits 0; a
  committed `HISTORY-REVIEW-2-RAW.md` with `REVISE` makes `--check` fail
  ("latest history review not confirming").
- [Observed] Code path: `reviewed_template` (script lines 447-482) still checks
  every C1 binding against its C1 blob, still compares every non-`HISTORY_PATHS`
  input (evidence `README.md`, `proof.json`, template, patch, images JSON,
  `vision.md`, `review-inputs.json`) against current bytes, and `candidate_check`
  runs over the `Frozen` view whose only change is that POLICY and SCRIPT now
  resolve to C1 blobs. `check_evidence` (lines 502-522) is unchanged: C3
  record, C3 checker equality and documentation before/after images are checked
  as before. The only guard removed is "review retired by changed input" for
  POLICY and SCRIPT; POLICY is compensated by the performed-digest check (line
  469-470), SCRIPT by `history_review` (lines 485-499).

## Criterion 1 — CC-SPEC read at C1, performed digest required

Met in substance. [Observed] Line 227 adds POLICY to `HISTORY_PATHS`, so line
467-468 no longer compares current CC-SPEC to the C1 digest; lines 469-470
require `digest(blob(c1, POLICY))` to be among the digests captured by
`^CONFIRM CRAFT AMENDMENT: CC-SPEC@([0-9a-f]{64})$` over the current
acceptance record. This matches R1's wording ("read the CC-SPEC bytes it froze
as history and to require that digest be a performed CC-SPEC digest").

On non-performed lines: the regex does not distinguish a performed phrase from
a quoted or proposed one anywhere in the acceptance record (see Note N1). It
does not matter today [Observed: both matching lines are performed] and is
unlikely to matter later [Inferred], because the digest tested is fixed by the
C1 blob and `REVIEW-RAW.md:22`, and that digest is already performed; a stray
quoted line could only ever "satisfy" a digest that is in fact performed.

## Criterion 2 — self-binding relaxed and compensated

Partly met; one fail-open path (M1).

- Ordering: numeric sort on the captured integer (line 271), leading zero
  excluded by `[1-9][0-9]*` (line 228). [Observed by inspection] correct; not
  exercised by the selftest (N2).
- Missing directory: `iterdir` raises `FileNotFoundError`, an `OSError` caught
  by `main` as FAIL — fail-closed [Observed by inspection].
- Verdict parsing: exactly one `^Verdict:` line with exact value; trailing
  space or CR fails closed [Observed by inspection].
- Duplicate binding lines: `bindings == [digest]` refuses two lines, even
  identical ones [Observed by inspection]; untested (N2).
- Retention: checked only for raws **present in the working tree** — see M1.

## Findings

### M1 — Material: a committed history raw can be deleted and the check re-opens on an earlier CONFIRM

[Observed] `Evidence.history_reviews` (script lines 269-271) enumerates
`HISTORY-REVIEW-<n>-RAW.md` from the filesystem only; `history_review` (lines
485-492; retention loop 489-492) checks retention (introduced once, bytes unchanged) only for the files
it was handed. Reproduced in the scratch clone at the reviewed commit:

1. commit `HISTORY-REVIEW-1-RAW.md` (`CONFIRM`, current recorder digest) → `--check` exit 0;
2. commit `HISTORY-REVIEW-2-RAW.md` (`REVISE`, same digest) → `--check` exit 1, "latest history review not confirming";
3. `git rm` raw 2 and commit → `--check` exit 0.

So a later non-confirming review over the same bytes — the duplicate-dispatch
case AGENTS.md records for 2026-09-23 — is defeated by deleting it, and the
compensating control for the relaxed self-binding fails open. The original
guard it replaces (`REVIEW-RAW.md` at a fixed path, "missing evidence" on
deletion) had no such gap. HISTORY-READING.md:24-26 ("Every history review is
retained … earlier raws stay unchanged") states the stronger property the code
does not enforce.

Proposed fix: derive the population from Git as well as the tree — e.g.
`git log --format= --name-only --diff-filter=AD HEAD -- <EVIDENCE>` filtered by
`HISTORY_REVIEW`, and require (a) no history raw was ever deleted, (b) the set
ever introduced equals the set present, and optionally (c) numbers are
contiguous `1..n`. Add a selftest mutant that drops a lower-numbered or the
highest-numbered raw from the enumerated population while its introduction
stays recorded, expecting a named refusal.

### M2 — Material: rule-6 coverage misses four of the new predicates, and HISTORY-READING.md claims every guard is covered

[Observed] All eight mutants in `history-reading-rule6.json` reproduce
(re-run in the scratch clone, each fragment unique, each makes `--selftest`
exit non-zero with the recorded refusal; script bytes at `c4a7ef4` and
`f5fdde7` are identical). But the following mutants of new predicates
**survive** (`--selftest` exits 0 with its PASS line):

| Mutant (script line) | Predicate left untested |
|---|---|
| `reviews[-1]` → `reviews[0]` (493) | latest raw is the one judged |
| `sorted(names, key=int…)` → `sorted(names)` (271) | numeric, not lexicographic, order (`10` after `9`) |
| verdict check → `any(v.strip().startswith('CONFIRM') …)` (494-496) | exactly one `Verdict:` line; `REVISE`+`CONFIRM` pair refused |
| `bindings == [d]` → `d in bindings` (497-499) | exactly one binding line; a stale second line refused |
| `POLICY_ACT` → unanchored `CC-SPEC@(…)` (229) | only line-start phrase lines count (N1) |
| `HISTORY_REVIEW` `[1-9][0-9]*` → `[0-9]+` (228) | leading-zero / `0` numbering excluded |

The root cause is the fixture: `Fixture.history_reviews` (lines 604-605)
overrides the enumeration with at most one hard-coded raw, so neither ordering
nor the real `Evidence.history_reviews` is ever exercised. HISTORY-READING.md:27-29
says the JSON "records each guard's mutant … each one fails the selftest"; that
over-claims (AGENTS.md verification rule 6: per predicate).

Proposed fix: let the fixture hold a list of history raws (e.g. 1 = CONFIRM
over an old digest, 2 = REVISE, 10 = CONFIRM current), add mutants for
two-verdict, two-binding, `9`-vs-`10` ordering and a quoted-but-unanchored
`CC-SPEC@` digest; re-run and extend `history-reading-rule6.json`; reword
HISTORY-READING.md:27-29 to state the population the JSON covers.

### N1 — Note: "performed" is inferred from line shape over the whole acceptance record

[Observed] Line 469 scans every line of `ACCEPTANCE-ACT-RECORD.md` that starts
with the phrase; it cannot tell a performed phrase from one quoted in a future
offering or supersession note. [Inferred] Harmless for the fixed C1 digest
(already performed at line 95), and the aggregate is the performed-acts record.
Proposed fix (optional): additionally hard-code the reviewed performed digest
(the line-95 argument) and require it equal the C1 digest, so the check does not depend on
future record shapes; or document the dependency in HISTORY-READING.md.

### N2 — Note: pre-existing untested input — `vision.md` drift

[Observed] Adding `VISION` to `HISTORY_PATHS` survives the selftest: no mutant
exercises `vision.md` (nor the evidence `README.md`, `final-documentation.patch`
or `documentation-images.json` through the "review retired" arm). Code still
checks them [Observed by inspection, lines 467-468 and `candidate_check`], so
nothing is weakened by this diff; the gap predates it. Proposed fix: add one
"review retired by changed input" mutant per remaining non-history input.

### N3 — Note: the frozen README's retirement sentence is now false and nothing routes from it

[Observed] `README.md:52` of the package says "The checker remains subject to
review retirement"; after this change the recorder is no longer retired by
changing (it is bound by the latest history review). The README is a C1 frozen
input and cannot be edited. HISTORY-READING.md does not quote or name that
sentence, and [Observed] nothing but a code comment (script line 226) cites
HISTORY-READING.md. Proposed fix: have HISTORY-READING.md quote README.md:52 as
superseded, dated, per the CG-27 lesson (mark the stale sentence, not a page).

### N4 — Note: "latest wins" lets a later CONFIRM overrule a REVISE over the same bytes

[Observed] Only `reviews[-1]` is judged. A REVISE raw n followed by a CONFIRM
raw n+1 over the same recorder digest passes with no repair in between. That
may be intended (the owner's 2026-09-26 stopping rule), but HISTORY-READING.md
says only "A later change to the recorder needs a new, higher-numbered raw".
Proposed fix: state explicitly that a later raw over unchanged bytes supersedes
an earlier verdict, or require that a non-confirming raw's bound digest never
equals the current one.

### N5 — Note: two recorded "killed" mutants are killed by a crash, not a guard

[Observed] `history-reading-rule6.json` mutants 6 and 7 fail by `IndexError`
and `TypeError` ("expected string or bytes-like object"), not the named
refusal. They are still fail-closed [Observed: `main` catches `TypeError`; the
`IndexError` path escapes `main` uncaught but still exits non-zero]. Accurate
as recorded; worth one sentence in HISTORY-READING.md that those two guards are
belt-and-braces.

### N6 — Note: history raws live where check_governance does not treat them as raw review

[Observed] The recorder requires history raws in
`docs/evidence/polaris-understanding-reconciliation-2026-09-28/` (script line
270), but `_is_raw_review` in `scripts/check_governance.py` (lines 537-542)
exempts only the candidate `reviews/` lane and `docs/reviews/*-RAW.md`. A draft
of this very raw, committed in the scratch clone, failed CG-15 (three truncated
digest prefixes that no current act argument carries) and CG-1b (a code-span
path not in the tree). This raw was worded to avoid both, but a future
reviewer's verbatim output (CC-REV-6: stored unchanged) can fail the battery
and then cannot be repaired. Proposed fix: extend `_is_raw_review` to the
`HISTORY-REVIEW-<n>-RAW.md` population in this package (with a rule-6 mutant),
or state the CG-15/CG-1b constraints in the history-review brief and in
HISTORY-READING.md.

## Criterion 3 and 4 summary

- Every other frozen input is checked as before [Observed]; `--selftest` passes
  [Observed]; the eight recorded mutants are accurate [Observed].
- HISTORY-READING.md is present-tense and matches the code except
  lines 24-26 (M1) and 27-29 (M2).

## Housekeeping

[Observed] During this review the reviewed worktree gained paths this review
did not create: a spec-policy readability restyle candidate package directory
and two restyle builder/recorder scripts, first untracked and then staged as
additions. They presumably come from a parallel session [Inferred]. This
review edited nothing there; its scratch work ran in a separate clone. The
reviewed bytes are pinned by commit and digest above, so the staged additions
do not affect this review's subject.
