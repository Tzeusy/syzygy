# History review 5 — reconciliation recorder
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 0f9144bf23bb8346aa2d733591ae447c163b392c
- `scripts/record_polaris_understanding_adoption.py`: `c83f2f27416235849e013164e00dfb855d11728351a4533e77f748f6cca964c9`

Reviewer: independent fresh-context agent (syzygy-5gv6), 2026-09-29.
Digest computed by `sha256sum` on the file checked out at the reviewed commit.

## Head contract, quoted before writing

From `HISTORY-READING.md` ("What binds the recorder now"):

- "That raw carries exactly one `Verdict:` header, `CONFIRM` or `CONFIRM WITH EXCEPTIONS`."
- "It carries exactly one line `` - `scripts/record_polaris_understanding_adoption.py`: `<sha256>` ``."
- "'Latest' is the highest `<n>`, compared as a number; the raws are numbered 1 to n with no gap."
- Every raw must be the file's own introduction, unchanged.

The dispatch adds: both lines within the first four non-blank lines. This
raw's four non-blank lines are the title, the one Verdict line, the reviewed
commit and the one digest line. The recorder itself scans the whole text
(`history_review()`: `re.findall(r'^Verdict:…', text, re.M)` and the same for
the digest line), so this body contains no other line that starts with
`Verdict:` and no other line of the digest form.

## Scope

Subject: `git diff main...0f9144b` (two commits: `ca3bed0` recorder,
`0f9144b` docs and rule-6 rows), three files: the recorder,
`HISTORY-READING.md`, `history-reading-rule6.json`. Findings re-derived:
N1, N2, N3, N4 of round 4. All experiments ran in scratch clones of
`0f9144b` (and `ca3bed0`); the reviewed tree was not modified.

## Facts established

- [Observed] The recorder hashes to the digest above. `git diff ca3bed0
  0f9144b -- scripts` is empty, so the rule-6 rows recorded at `ca3bed0` ran
  against the same recorder bytes.
- [Observed] `--selftest` exits 0: "54 trust-boundary mutations refused",
  "PASS history population selftest: 16 real-Git cases".
- [Observed] `--check` fails only with "latest history review does not bind
  the current recorder: …HISTORY-REVIEW-4-RAW.md" (round 4 bound different
  bytes). This is the designed state until this raw is retained. Hosted
  `checks` on the PR fails on that same line; `node` passes.
- [Observed] `check_governance.py` before this raw: 31 OK, 21 WARN, 0 FAIL;
  `--selftest`: 341 fixtures, 0 failing.

### N1 — `-z` NUL split (re-derived, mutated)

- [Observed] The code at `0f9144b` passes `-z` and splits the decoded output on
  NUL, dropping empty items. `HISTORY-READING.md` says the same.
- [Observed] Mutant: revert both edits (drop `-z`, restore `.decode().splitlines()`).
  `--selftest` exits 1 with "history population selftest: non-ASCII name
  deleted refused". The on-disk non-ASCII case still passes, as the page's
  "refused only while on disk" describes. The `-z` guard is pinned.
- [Observed] Mutant: drop only `-z` and keep `split('\0')`, or keep `-z` and use
  `splitlines()`: both fail, but on the first fixture (the blob is one item),
  so they say nothing about non-ASCII names. Not counted as evidence.
- [Observed] Survivors, both exit 0: removing `log = [p for p in log if p]`,
  and decoding with `'ascii', 'ignore'` instead of `'utf-8', 'replace'`.
  [Inferred] Neither can change a verdict: an empty item never starts with the
  evidence prefix, and a name with a dropped byte still matches the near-miss
  pattern. Notes only.
- [Observed] The newline-in-name case is refused even with the `-z` guard
  reverted, because git quotes the name and the first half still matches the
  near-miss pattern. [Inferred] The "not split" claim for newline names is not
  pinned separately from the non-ASCII case.

### N2 — near-miss predicate (re-derived, mutated)

- [Observed] Code: `re.compile(r'history[^a-z0-9]*review', re.IGNORECASE)`,
  applied with `.search` to the basename, over the disk and Git populations.
  `HISTORY-READING.md` publishes the same regex, its flags, its separator class
  (including none) and `search`. Published and coded forms agree.
- [Observed] Killed: the old `'history-review' in name.lower()` predicate;
  dropping `re.IGNORECASE`; `*` to `+` (run-together name).
- [Observed] Survivors, both exit 0: narrowing the separator class to
  `[-_ ]*`, and `.search` to `.match`. The fixtures use only hyphen,
  underscore, space, none, and names that begin with the word, so a name
  such as `history.review-5-RAW.md` or `old-history-review.md` is refused by
  the code but by no fixture. [Inferred] The published predicate is correct and
  the tests under-pin its width. Note, not a defect.
- [Observed] A separator outside the class definition (a digit, an ASCII
  letter, a misspelling such as `hist0ry`) is not a near miss by the
  published predicate and is not refused; that is stated on the page.

### N3 — 28 rule-6 rows re-run at `ca3bed0`

- [Observed] `history-reading-rule6.json` at `0f9144b` holds 28 mutants, every
  one recorded at `ca3bed0` (its own `commit` field). I applied each `old` to
  `new` in a clone at `ca3bed0` (each `old` occurs exactly once), ran the
  row's command (the recorder selftest, or the governance selftest for the
  last row) and checked the row's `refusal` string against the output.
- [Observed] 28 of 28 exit non-zero; 28 of 28 contain the row's recorded
  `refusal` string. (A first pass that read the JSON from `ca3bed0` saw 23
  rows and one stale `old` text; the 28-row file is the one at `0f9144b`.)
  The clone was restored after each row.

### N4 — documentation only

- [Observed] The page states that a committed malformed or twice-added raw
  keeps `--check` failing and that no clearing mechanism exists. The
  "deleted" fixtures show a committed near-miss name is refused after
  `git rm`. No code was changed for N4, as the page says.
- [Observed] The page's round-5 sentence ("required, because the recorder
  changed after round 4… `--check` fails by design") matches the state above.

## Notes (do not block; owner ruling 2026-09-26 clears these bytes)

1. Add fixtures for a `.`-separated near miss and a prefixed near miss, so the
   separator class and `search` are pinned (N2 survivors).
2. Add a newline-name case that only the NUL split distinguishes (N1).
3. The two benign N1 survivors need a rule-6 row or an explicit no-effect
   statement.
4. Both the reviewer brief's "first four non-blank lines" and the page's
   whole-text contract are satisfied by this head; only the second is
   enforced by the recorder.

## Verdict basis

No blocking finding. The recorder, the page and the 28 rows agree at
`0f9144b`; the pattern and the NUL split each fail closed under mutation.
Notes are cosmetic test-width gaps in the direction of over-refusal.
