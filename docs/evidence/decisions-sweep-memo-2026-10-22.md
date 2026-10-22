# The decisions sweep, folded once per file (syzygy-bpyt.8.20, syzygy-bpyt.8.22)

Evidence report, not authority. It records why the consent gate's
decisions-directory sweep now folds each swept file's text at most three
times per sweep instead of up to nineteen, why the admission sweep no longer
tests its four paths in a file's text, why neither change can alter an
answer, and what was run to check that. CC-REV-1 class 4 (availability of
the consent gate), with the three further checks GP-Q0 sets for class 4 in
`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`:
an old-versus-new differential over a mutated-record corpus that includes
records with altered prose, a rule-6 mutant for each predicate, and an owner
notice in the cycle report.

Old is `68c553b8ca643fcec1558768b6cad4c0af911f28`, the merge of PR #505 on
`main`, which also carries PR #508. New is
`7deb8dfd8f161b9de8471061053fd0b86a33fa6c`, the commit every record below
names. No file under `.syzygy/**` or `openspec/**` changes, and no observed
repository is read: every world is the Syzygy checkout's own decisions
directory with in-memory overlays.

The branch then merges `main` at `4b31531c0f7c687bac01d15d0d54eb8bfda80f00`
(PR #510) and adds this report, the records and
`scripts/rule6_timeout_rerun.py`. [Observed] `git diff 7deb8dfd HEAD`
touches nothing under `packages/polaris-generation-consent/`, the decisions
directory, `packages/polaris-dossier/src/gate-sources.ts` or the three
scripts the records name, and after rebuilding the merged tree its
`package-reader.ts`, `package-reader.js`, `gate-sources.ts`,
`gate-sources.js` and `testing.js` have the digests the differential records
for the new tree. `gate-sources.ts` imports only the consent package and a
type.

## Where the time went

`findActRecords` (`packages/polaris-generation-consent/src/package-reader.ts`)
walks `.syzygy/governance/decisions/` once per read and asks of each file
that is none of the family's records, pins or exempt records whether it
names the act. For the text test the sweep tried each of its stems and
needles in turn, and for each one refolded the whole file:
`carries(text, needle)` computed `stemFolds(text)`, and a loose sweep's
`carriesLoosely` computed `stemFolds(loose(text))` too when the first missed.
The field-line test then computed `fold(text)` once more.

A digest-bound form, such as each provider statement the dossier reads, has
eight stems and its artifact path: nine needles, all of which miss in a file
that does not name the act, so the sweep folded each such file
2 × 9 + 1 = 19 times. A whole `providerStatements.statementsFor` call makes
three such sweeps over the 184 files of the decisions directory (the
version 1 Anthropic statement, the version 2 successor, the OpenAI
statement).

[Observed] A CPU profile of one `statementsFor('redis-redis')` call in a
fresh process on each tree (`node --cpu-prof`, 2026-10-22, at a one-minute
load of about 37 on this 12-CPU host), by inclusive sampled time:

| | old | new |
|---|---|---|
| sampled time | 8,781 ms | 1,899 ms |
| `findActRecords` (the sweep) | 84.2 % | 71.4 % |
| `stemFolds` | 59.2 % | 29.9 % |
| reading files | 2.1 % | 17.4 % |
| the directory walk | 0.3 % | 1.4 % |

No git process runs in the call. The profiles are scratch measurements, not
retained; the timing record below is the evidence for criterion 1.

## The change (syzygy-bpyt.8.20)

`findActRecords` builds a `TextForms` for each swept file, inside its loop:
the file's `plain` spellings (`stemFolds(text)`), its `slack` spellings
(`stemFolds(loose(text))`) and its `folded` text (`fold(text)`), each
computed on first use and kept for the rest of that file's tests.
`formsCarry(forms, needle, loosely)` is `carries(text, needle)`, or with
`loosely` `carriesLoosely(text, needle)`, over those kept values. `namesAct`
takes the forms in place of the text; the field-line test splits
`forms.folded()`. Nothing else in the reader changes: the walk, its order,
the record, pin and exempt tests, the file-name tests, the field-value tests
(which fold one short field value, as before) and every refusal string.

The scope is one file in one call. The forms object is created for one
swept file and is unreachable once the loop moves on, so nothing is shared
between files, between the sweeps of one call or between calls, and nothing
is held at module level. A process-lifetime cache keyed across sweeps (the
design called D2) was rejected as a runtime-posture change and is not part
of this bead.

## Why no answer can change (syzygy-bpyt.8.20)

- **The same values.** `stemFolds`, `loose` and `fold` are pure functions of
  their argument: a kept value is the value a fresh call on the same text
  would return. The text is the file's swept text for this one read, so a
  kept value is never compared against another file's needles or another
  read's bytes.
- **The same tests.** For each needle, `formsCarry` computes the needle's
  folded spelling and asks whether a plain spelling of the text contains it;
  on a miss, and only for a loose sweep, it computes the needle's loose
  spelling and asks the same of the slack spellings. That is
  `carries(text, needle) || carries(loose(text), loose(needle))` with the
  text's folds taken from the memo, in the same order.
- **The same short-circuit.** `namesAct` still returns at the first needle
  that names the act, and `findActRecords` still returns at the first file
  that names it, so the refusal names the same file.
- **The same exceptions.** Each kept value is first computed at the needle
  where the per-needle code first computed it (`plain` at the first needle,
  `slack` at the first plain miss of a loose sweep, `folded` at the field
  test). A fold that throws (a `RangeError` past the longest string, from
  NFKC expansion) therefore throws at the same point, and the read refuses
  the same way.

## The admission paths (syzygy-bpyt.8.22)

The admission family's sweep tested its five stems and four paths in a
file's text, and the stems and paths on every swept field line. Its text
needles are now its stems alone; the field needles are unchanged
(`everyField(ADMISSION_NEEDLES)`, stems and paths).

Each of the four paths contains an admission stem in its folded spelling:

| Path | Admission stems it contains |
|---|---|
| `.syzygy/governance/contracts/candidates/public-repo-admission/instances` | `public-repo-admission` |
| `.syzygy/governance/contracts/candidates/public-egress-v2/instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md` | `public-egress-v2` (and `public-egress-`) |
| `.syzygy/governance/contracts/candidates/public-repo-admission/` | `public-repo-admission` |
| `.syzygy/governance/contracts/candidates/public-egress-v2/` | `public-egress-v2` (and `public-egress-`) |

The admission sweep is not loose, so its text test is
`carries(text, needle)`: whether some spelling of the text (`stemFolds`)
contains `stemFolds(needle)[0]`. Every path and stem is ASCII with no
underscore, whitespace, default-ignorable code point or repeated dash, so
`stemFolds(needle)[0]` is the needle in lower case: the stems are already
lower case, and each path in lower case still contains its stem as written.
So any spelling of a text that contains a path's needle spelling contains
its stem's, and the stem is tested in the same `some` over
`[...stems, ...needles]`, before the paths. A path could never name the
admission act that its stem had not already named. Removing the paths from
the text needles therefore changes no answer, and skips four tests per swept
file.

The same containment holds on field values, so the paths on field lines are
redundant as well (mutant M22c below survives). Removing them is outside
this bead, whose first criterion keeps the field needles; it is recorded
here so the redundancy is known.

## What was run

### Tests

`packages/polaris-generation-consent/src/decisions-sweep.test.ts` (new):

- **Each swept file is read in its own spellings.** With a file that does
  not name the act walked first (`AA-NOTES.md`), a file walked after it that
  names the registry git-source act refuses the read, naming that file:
  the stem in prose, the stem split by backticks (found only by the loose
  reading), and the stem on a field line of the aggregate acceptance record
  (found only by the field-line test). One file edited between three reads
  of the same tree is read in its bytes each time: ok, refused, ok. Every
  expected answer is a literal.
- **The cost contract (a cost test).** Six files of about 20,000
  characters of prose with dashes, no-break spaces and accents, swept by a
  digest-bound form with eight stems and its artifact (nine needles), none
  of which the prose names. The test spies on `String.prototype.normalize`
  (restored after each test), counts its calls on strings longer than
  10,000 characters during one read, and asserts at least 6 and at most
  18, three per file. Each fold of a text normalizes it once. The old code
  makes 19 per file; the test times nothing.
- **An admission path in a decisions file's text.** Each of the four paths,
  as written, in upper case with underscores, and with a soft hyphen before
  each dash, in a decisions file's prose, still makes the admission read
  refuse (`invalid-records`); a world naming another package's path reads
  no admission record and refuses nothing.

### Rule 6

`docs/evidence/decisions-sweep-mutants-2026-10-22.json`, written by
`scripts/rule6_mutation_runner.py` at commit
`7deb8dfd8f161b9de8471061053fd0b86a33fa6c`: each mutant's `old` and `new`
fragment of `packages/polaris-generation-consent/src/package-reader.ts`,
the command it ran (the six consent test files other than
`recorder-template.test.ts`, 489 tests), and each failed test with its
first error line. Each mutant is one textual replacement, restored after
its run. M0 replaces a fragment by itself: the suite on the subject as
committed, which must pass for any other outcome to mean anything.

| Mutant | What it breaks | Failed tests | Outcome |
|---|---|---|---|
| M0 unmutated control | nothing | 0 | passes |
| M1 slack from plain | the loose spellings, read from the text as written | 2 | killed |
| M2 forms reused across files | per-file scope: the first file's forms kept for the rest of one call | 23 | killed |
| M2b forms keyed by name, process-wide | per-file scope: a module-level memo by file name, reused across sweeps and calls (D2's reuse) | 116 | killed |
| M3 folded from plain | the field lines, read from the stem spelling | 18 | killed |
| M4 memo removed | the cost: every needle refolds the text | 1 (the cost test: 114 folds, 6 files × 19, against at most 18) | killed |
| M5 slack eager | where the loose spelling is first computed | 1 (timeout, see below) | equivalent |
| M6 loosely inverted | the loose arm, run for the sweeps that are not loose | 6 | killed |
| M7 plain arm dropped | the plain arm | 220 | killed |
| M22a admission stem removed | 8.22: the stem a path relies on | 28 | killed |
| M22b admission paths restored | 8.22 undone | 1 (timeout, see below) | equivalent |
| M22c admission field paths dropped | the same containment on field values, outside 8.22's scope | 0 | survives, equivalent |

M4 is the mutant only a cost test can kill: it gives every answer the old
code gave, at the old cost. Its one failure is the cost test's count.

**M5 and M22b give the same answers and are slower.** Each failed one test,
"the policy port and the strict policy chain agree on every world in the
fixture set, at every instant" (`package-reader.test.ts`), which compares
the admission records port with the strict policy chain over every policy
world the file builds, at eight instants, under vitest's default 5,000 ms
per-test timeout. Both mutants add work to the sweeps that are not loose
(the admission, policy and class sweeps): M5 computes the loose spellings of every
swept file whether or not a loose test will read them, and M22b tests the
four admission paths in every file's text again. Neither changes an answer.
`docs/evidence/decisions-sweep-mutants-timeout-2026-10-22.json`
(`scripts/rule6_timeout_rerun.py`, the same tree, the same fragments and
tests, the timeout raised to 120,000 ms) records it:

| Run | Tests | Failed | The policy-chain test | Load1 |
|---|---|---|---|---|
| M0 unmutated control | 489 | 0 | 4,347 ms | 38.65 |
| M5 slack eager | 489 | 0 | 6,895 ms | 40.24 |
| M22b admission paths restored | 489 | 0 | 7,012 ms | 38.44 |

So M5 is recorded as equivalent, as its note in the record says before the
run: the loose spelling is the same pure function of the text wherever it is
first computed, and only the point where a fold that throws would throw
moves, which no natural input reaches. No test was built to kill it. M22b
is the 8.22 change undone and is equivalent by the containment above. M22c
is equivalent by the same containment on field values.

**A void first run.** The first run of the same mutants, at a one-minute
load of about 50, had no control. The policy-chain test failed by its
timeout under every mutant, and an unmutated run of the same file then also
timed out (old and new trees alike), so that run's kills of M5, M22b and
M22c carry no information. It is retained, marked by its name, as
`docs/evidence/decisions-sweep-mutants-void-high-load-2026-10-22.json`; the
record of reference is the second run, which adds M0.

### Criterion 2 (8.20) and criterion 2 (8.22): the differential

`scripts/differential_consent_act_families.mjs`, the syzygy-bpyt.8.4 script
extended in place, runs every reader the gate composes over owner-act
records from both trees' compiled packages over the same worlds and
instants, and compares the two answers as text (the answer's JSON, or the
error the read throws). This bead adds the dossier's package gate sources
as readers (D9, the RFC7-20 ruling, the registry entry, each drawer and
each repository's provider statements), so `statementsFor` itself is
compared, and adds the world kinds and placements marked below. The
syzygy-bpyt.8.4 record (`docs/evidence/consent-act-family-differential-2026-10-22.json`)
names that script's earlier digest and is left as it is; the new record
names the script's current digest and the commit it ran at.

`docs/evidence/decisions-sweep-differential-2026-10-22.json` (6 worker
threads, 3,709 s):

- **Trees.** Old `68c553b8ca643fcec1558768b6cad4c0af911f28`, new
  `7deb8dfd8f161b9de8471061053fd0b86a33fa6c`, both clean. For each, the
  record gives the sha256 of `package-reader.ts` and `gate-sources.ts` and of their compiled
  `.js` files and of the compiled test support module, and confirms that
  the tree's dossier package resolves the consent package inside the same
  tree, so neither tree reads the other's code.
- **The altered-prose corpus is imported, not copied.** The
  `PROSE_ALTERATIONS` and `HEAD_FIELD_ALTERATION` of syzygy-bpyt.8.10 (PR
  #500), five alterations, are read from the new tree's built
  `packages/polaris-generation-consent/dist/testing.js`, beside the
  script's own 41 head alterations: 46 named alterations in all. Each
  field-parsed record takes every one; each byte-exact record takes the two
  title alterations and the date alteration, since the template refuses
  every other one in the same unchanged call on both trees (the script's
  comment at that line says why).
- **Instants.** 2026-10-08T09:30:00Z and 2026-10-22T12:00:00Z. At the
  earlier instant the policy chain reads ok in 1 world, the one whose policy
  file carries the bytes the version 2 screening-scope act binds (found in
  the checkout's history at commit
  `3409ef5ae9f7dcbadbb248d4df1c295dc43a5b0b`; the version 1 act's bytes are
  in no commit, so that act has no such world).
- **The corpus**, 4,643 worlds, digest
  `1d5d50dbc270cff3fab1cd0e23fb41b612a2adfb9288da173b7f11459315834a`:

| Kind | Worlds | What it is |
|---|---|---|
| `base` | 4 | the four bases (the checkout as it is; with the three admission acts it lacks; with the registry git-source act; with all of them), over the whole tree |
| `base-reduced` | 4 | the same four over the reduced tree (the decisions files some reader names) |
| `line` | 2,400 | each non-blank line of each field-parsed act record appended to, deleted, duplicated or fenced |
| `named` | 449 | named alterations of each act record's head and prose, the PR #500 corpus among them |
| `record` | 15 | each act record deleted |
| `artifact` | 24 | each act's artifact with a byte appended, or deleted |
| `pin` | 8 | each pinned file with a byte appended, or deleted |
| `probe` | 1,541 | one added decisions file per needle and placement: 67 needles × 23 placements |
| `real-file` | 184 | each of the 184 decisions files with one needle appended, the needles in turn |
| `edited-between-reads` | 11 | one probe file read three times in one world: not naming, naming, not naming |
| `policy-bytes` | 3 | the policy file overlaid with the bytes a screening-scope act binds, from git history |

The 23 placements are: in prose; on each of the four swept field lines; on
three of them behind a `>`; on a bulleted bold field line; spelled loosely;
in upper case with underscores; with soft hyphens; with zero-width spaces;
with other dash code points; with spaces; in fullwidth forms; walked after
a file that does not name it; on a field line of the aggregate record
walked after such a file; in a subdirectory; in the file's name; in the
name with a withdrawal word; in the aggregate record's prose; and on the
aggregate record's field line. The last kinds of the table, the
walked-second placements, `real-file`, `edited-between-reads` and
`policy-bytes`, are new in this bead.

[Observed] 36,515 answers compared, **0 differ**. The old answers form
1,648 distinct answer vectors (by answer digest; 1,582 of them seen in one
world only) and 256 distinct label vectors (by what each answer says,
digests and texts dropped). Each reader's distinct labels are in
`totals.distinctLabelsPerReader`, and each distinct answer, with its label
and the number of worlds that gave it, in `answersPerReader`.

**What 8.22 is held to here.** The four admission paths are among the 67
needles, so each is placed in a decisions file's text in all 23 ways (92
probe worlds) and appended to three of the real decisions files each (12
`real-file` worlds); the admission reader, the port and the gate sources
read every world. The old tree tests the paths in text, the new one does
not, and no answer differs.

**The syzygy-bpyt.8.4 review's notes carried to this bead**
(`docs/evidence/consent-act-families-round-1-dispositions-2026-10-22.md`):

- N5, record what ran: each tree's compiled `package-reader.js`,
  `gate-sources.js` and `testing.js` digests are recorded beside the
  sources', with the check that each tree's dossier resolves its own
  consent package.
- N6, labels beside vectors and a mid-instant `ok`: the label vectors and
  each reader's distinct labels are counted beside the answer vectors, and
  the `policy-bytes` world above reads `ok` at the mid instant. The records
  port is still compared on 11 worlds only (the 8 base worlds and the 3
  `policy-bytes` worlds); see the residuals.
- N7, import the corpus: done, as above.

### The negative controls

A differential that cannot report a mismatch proves nothing, so each bead's
change has a control run: the same script with `--expect-mismatches`, its
`--new` tree a checkout of the new commit with one mutant's fragment from
the rule-6 record applied and the packages rebuilt. The record names the
mutant in `controlNote`, gives the mutated tree's compiled digests (its
`clean` is `false`), and the script succeeds only when some answer differs.

- **8.20, M2 applied** (the first swept file's forms kept for the rest of
  one call): `docs/evidence/decisions-sweep-negative-control-2026-10-22.json`,
  the `edited-between-reads` and `base-reduced` kinds (15 worlds,
  corpus digest `29d7919313eff87dc1847316b787e4371b383a93a16817efedf91fb6a1ec7d11`):
  [Observed] 697 answers compared, **570 differ**. Under M2 the
  aggregate acceptance record, whose text the sweep never tests, lends its
  spellings to every file walked after it, so reads that answered `ok`
  refuse on a file that does not name the act, and a read that refused
  names another file [Inferred: from the refusals, which name the first
  file walked after the aggregate record]. A run of the same control over
  the `probe` kind (1,541 worlds) reported 19,456 differing answers of
  26,197 [Observed]; its record is not retained (12.9 MB), and the two
  kinds above stand for it.
- **8.22, M22a applied** (the stem `public-repo-admission` removed, which
  two of the paths contain, now that the paths are not text needles):
  `docs/evidence/decisions-sweep-negative-control-8-22-2026-10-22.json`, the
  `probe` kind (1,541 worlds, corpus digest
  `45c534e776dcc81a37a1d5a581d39efaa3e488e2c9d72da0d0b8fb8bc6ddbc0c`):
  [Observed] 26,197 answers compared, **152 differ**, in 76 worlds, each in
  the admission reader and the in-force egress read: where the old tree
  refused (`invalid-records`), the mutated one reads the admission records
  and the egress act. Among them are the two paths that contain the stem,
  each in its 12 text placements (prose, the loose, upper-case,
  soft-hyphen, zero-width, dash, spaced and fullwidth spellings, walked
  second, in a subdirectory, in the name, in the name with a withdrawal
  word); on field lines the paths are still field needles and the read
  still refuses. So the corpus does exercise the paths in text, and a
  change to what names the admission act there is reported.

### Criterion 1: whole `statementsFor` calls

`scripts/measure_decisions_sweep.mjs` times one
`createPackageGateSources(...).providerStatements.statementsFor('redis-redis')`
call per fresh `node` process, from just before the call to just after it,
over the old tree's checkout (both trees read the same decisions directory),
at instant 2026-10-22T12:00:00.000Z. The rounds alternate which tree goes
first, and each sample records the one-minute load average just before and
just after it. The bound the lead set: every new sample at most 5,000 ms at a
one-minute load of at most 30, and the median of the paired new/old ratios
at most 0.4. The script computes it and does not assert it.

`docs/evidence/decisions-sweep-timing-2026-10-22.json` (12-CPU host,
node v24.6.0; both trees' compiled `package-reader.js` and
`gate-sources.js` digests are in the record):

| Round | First | Old (load1 before) | New (load1 before) | New/old |
|---|---|---|---|---|
| 0 | old | 7,493 ms (27.39) | 1,904 ms (26.32) | 0.254 |
| 1 | new | 7,793 ms (26.62) | 2,071 ms (26.32) | 0.266 |
| 2 | old | 8,597 ms (26.41) | 1,406 ms (25.86) | 0.164 |
| 3 | new | 8,782 ms (26.2) | 2,023 ms (25.86) | 0.230 |
| 4 | old | 7,995 ms (26.25) | 3,048 ms (25.91) | 0.381 |
| 5 | new | 9,710 ms (26.48) | 2,918 ms (26.48) | 0.301 |
| 6 | old | 7,944 ms (26.01) | 2,000 ms (25.77) | 0.252 |
| 7 | new | 7,395 ms (25.39) | 1,359 ms (25.39) | 0.184 |

[Observed] Old 7,395–9,710 ms, new 1,359–3,048 ms, one-minute load
25.27–27.39 over every sample, median paired ratio 0.253; the record's
`bound.holds` is `true`. Every sample's answer has the same sha256, old and
new. The differential above was running on six worker threads of the same
host throughout, and the load figures include it [Inferred: it weighed on
both trees' samples alike, since they were interleaved].

An earlier run of the same script at a one-minute load of 35.68–50.36,
outside the bound's condition, is retained as
`docs/evidence/decisions-sweep-timing-high-load-2026-10-22.json`: old
14,314–22,991 ms, new 2,397–5,254 ms, median ratio 0.207, and its
`bound.holds` is `false` because its load exceeded 30; its one new sample
over 5,000 ms (5,254 ms) started at a load of 43.9.

## Acceptance criteria

The two beads' criteria, each with the evidence that answers it. The
review criteria are the lead's to discharge; this report does not.

### syzygy-bpyt.8.20

1. **A whole `statementsFor` call within a stated bound, old against new,
   with the load beside each sample.** [Observed] Met:
   `docs/evidence/decisions-sweep-timing-2026-10-22.json`, every new sample
   at most 3,048 ms (bound 5,000 ms) at a one-minute load of at most 27.39
   (condition: at most 30), median paired new/old ratio 0.253 (bound 0.4),
   8 interleaved rounds in fresh processes, `bound.holds` true.
2. **An old-versus-new differential over every recorded act and the PR #500
   altered-prose corpus changes 0 answers, with its distinct answer
   vectors.** [Observed] Met:
   `docs/evidence/decisions-sweep-differential-2026-10-22.json`, 15 act
   records (10 field-parsed, 5 byte-exact) altered by line, by name and by
   the imported PR #500 corpus, 4,643 worlds, 36,515 answers, 0 differ;
   1,648 distinct answer vectors and 256 distinct label vectors. The
   negative control (`docs/evidence/decisions-sweep-negative-control-2026-10-22.json`,
   M2 applied) reports 570 differing answers of 697.
3. **A rule-6 mutant per new predicate is killed.** [Observed] Met:
   `docs/evidence/decisions-sweep-mutants-2026-10-22.json`, with its
   control passing: the plain arm (M7), the loose arm (M1, M6), the field
   fold (M3), the per-file scope (M2, M2b) and the memo itself (M4, by the
   cost test) are each killed. M5 (where the loose fold is first computed)
   is equivalent and recorded as such.
4. **An independent review raw retained; an owner notice if the review
   rules class 1, 3 or 4.** Open: the lead dispatches the fresh-context
   review. This pull request claims class 4.

### syzygy-bpyt.8.22

1. **`ADMISSION_PATHS` removed from the admission family's text needles
   only; its field needles unchanged.** [Observed] Met: the commit changes
   the admission sweep's `needles` from `ADMISSION_PATHS` to `[]` and leaves
   `fields: everyField(ADMISSION_NEEDLES)`, where `ADMISSION_NEEDLES` is
   still the stems and the paths.
2. **An old-versus-new differential over every decisions record and the
   altered-prose corpus: 0 answers changed, with a recorded negative-control
   run.** [Observed] Met by the same differential: the old tree tests the
   paths in text and the new one does not, every one of the 184 decisions
   files is swept with a needle appended, and the four paths are placed in
   92 probe worlds and 12 `real-file` worlds; 0 answers differ. Its negative
   control (`docs/evidence/decisions-sweep-negative-control-8-22-2026-10-22.json`,
   M22a applied) reports 152 differing answers of 26,197.
3. **A rule-6 run retained.** [Observed] Met: the same mutant record; M22a
   (the stem two paths rely on, removed) is killed by 28 tests, M22b (the
   change undone) is equivalent, and M22c (the field paths dropped,
   outside this bead) is equivalent.
4. **A fresh-context class-4 review raw retained.** Open: the lead
   dispatches it.

## Residuals

- **A pre-existing test that times out under load.** [Observed] The
  policy-chain agreement test in `package-reader.test.ts` took 4,347 ms
  unmutated at a one-minute load of 38.65 and failed vitest's default
  5,000 ms timeout on both trees at a load of about 50 (7,302 ms new,
  9,688 ms old; on the old tree a second test of that file timed out too).
  It decides nothing about this change; it is reported as a follow-up and
  not changed here.
- **M5's cost on the sweeps that are not loose has no test.** The cost test
  reads a loose sweep; an eager loose fold on the admission, policy or class
  sweep adds one fold per file there, at most three still, which the test's bound
  allows. The lead's design ruling was to record it as equivalent and build
  no test for it.
- **The admission field paths are redundant (M22c).** They stay, since
  syzygy-bpyt.8.22's first criterion keeps the field needles.
- **What the cost test bounds.** It counts `normalize` calls on strings over
  10,000 characters, so it bounds the folds of a swept file's text; the
  folds of needles and field values (short strings) are not counted, and are
  not changed by this bead.
- **What is still spent.** A `statementsFor` call still walks and reads the
  decisions directory once per sweep, three times; reading files is now
  17.4 % of the profiled call. A process-lifetime cache across sweeps (D2)
  was rejected and is not filed, since the bound is met.
- **The records port's coverage.** The port, which composes the admission
  and policy reads, is compared in 11 worlds; the reads it composes are
  compared in every world they take part in (the admission reader in
  3,016). The port's own composition is not changed by this bead.
- **The recorded commands omit the reporter flags.** The rule-6 runner's
  recorded `command` omits the reporter flags it passes (syzygy-bpyt.8.4
  review N8, filed under `syzygy-bpyt.11`), and the timeout re-run records
  its command the same way: both also pass vitest's JSON reporter and an
  output file, which change no outcome.
- **One host.** [Unknown] The bound was measured on one 12-CPU host that was
  never idle (one-minute load 25–27 with this lane's own differential
  running); other hosts are not measured.

## Re-running

Each tool is read-only over the trees it is given and writes only its
`--out` file (the rule-6 runners rewrite one source file in place and
restore it from git after each run). Build each tree first:

```sh
npm ci && npx tsc -b packages/polaris-generation-consent packages/polaris-dossier
```

Then, from a checkout of the new tree, with `OLD` a clean checkout of
`68c553b8ca643fcec1558768b6cad4c0af911f28`, `CTL` and `CTL22` checkouts of
the new tree with M2's and M22a's fragments applied to `package-reader.ts`
and rebuilt, and `MUT` a clean checkout of the new tree:

```sh
node scripts/differential_consent_act_families.mjs --old OLD --new . --bead syzygy-bpyt.8.20 --workers 6 --out diff.json
node scripts/differential_consent_act_families.mjs --old OLD --new CTL --bead syzygy-bpyt.8.20 --kinds edited-between-reads,base-reduced \
  --workers 3 --expect-mismatches --control-note '<M2 applied>' --out control.json
node scripts/differential_consent_act_families.mjs --old OLD --new CTL22 --bead syzygy-bpyt.8.22 --kinds probe --workers 4 \
  --expect-mismatches --control-note '<M22a applied>' --out control-8-22.json
node scripts/measure_decisions_sweep.mjs --old OLD --new . --rounds 8 --out timing.json
python3 scripts/rule6_mutation_runner.py --tree MUT spec.json mutants.json
python3 scripts/rule6_timeout_rerun.py MUT mutants.json timeout.json 120000 'strict policy chain agree' M5-slack-eager M22b-admission-paths-restored
```

`spec.json` may be the retained mutant record itself, which the runner
accepts as a spec. Each record's `controlNote` gives the note it was run
with in full.
`node scripts/differential_consent_act_families.mjs --old OLD --new . --bead syzygy-bpyt.8.20 --count`
prints the corpus's world counts and digest without running a reader.
