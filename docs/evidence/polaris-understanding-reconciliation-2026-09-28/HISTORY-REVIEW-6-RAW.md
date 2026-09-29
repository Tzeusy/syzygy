# History review 6 — reconciliation recorder
Verdict: CONFIRM
Reviewed commit: 32bc2bf24ca71727d30ac1085c7cadd5ca1d6031
- `scripts/record_polaris_understanding_adoption.py`: `97ee4b74e8497d25550e1a13752d3f2861dadddea4e7706652370890f81e2448`

Reviewer: independent fresh-context agent (syzygy-zbwb), 2026-09-29.
Digest computed by `sha256sum` on the file checked out at the reviewed commit.

## Head contract, quoted before writing

From `HISTORY-READING.md` ("What binds the recorder now"):

- "That raw carries exactly one `Verdict:` header, `CONFIRM` or `CONFIRM WITH EXCEPTIONS`."
- "It carries exactly one line `` - `scripts/record_polaris_understanding_adoption.py`: `<sha256>` ``."
- "'Latest' is the highest `<n>`, compared as a number; the raws are numbered 1 to n with no gap."

The dispatch adds: both lines within the first four non-blank lines. This raw's
four non-blank lines are the title, the one Verdict line, the reviewed commit
and the one digest line. The body below has no other line that starts with the
Verdict header and none of the digest-line form.

## Scope

Subject: `git diff main...32bc2bf` (two commits: `082a331` recorder selftest
fixtures, `32bc2bf` docs, rule-6 rows and sibling notes). Four files: the
recorder (+3 lines), `HISTORY-READING.md`, `history-reading-rule6.json`
(+3 rows, now 31), `RECORDER-REVIEW-NOTES.md` (new). Round 5's notes 1 to 3
were re-derived. All mutation experiments ran in scratch clones; the reviewed
tree was not modified.

## Facts established

- [Observed] The recorder hashes to the digest above.
  `git diff 082a331 32bc2bf -- scripts` is empty, so the rows recorded at
  `082a331` ran against the same recorder bytes.
- [Observed] Baseline `--selftest` exits 0: "54 trust-boundary mutations
  refused", "PASS history population selftest: 22 real-Git cases" (was 16;
  the page and the notes say 22).
- [Observed] The recorder digest appears in 0 tracked files at the head
  (`git grep -F`); round 5's bound digest appears in 1
  (`HISTORY-REVIEW-5-RAW.md`). So `--check` binds round 5's bytes and fails by
  design until this raw lands.

### Note 1 — separator class and `search` (mutated)

- [Observed] Mutant `history[^a-z0-9]*review` to `history[-_ ]*review`:
  `--selftest` exits 1, "history population selftest: dot-separated near-miss
  on disk refused".
- [Observed] Mutant `.search` to `.match` on the near-miss test: exits 1,
  "history population selftest: prefixed near-miss on disk refused".
- [Observed] Each `old` fragment occurs exactly once in the recorder.

### Note 2 — NUL split (mutated)

- [Observed] Mutant `.split('\0')` to `.replace('\0', '\n').splitlines()`
  (git's `-z` kept): exits 1, "history population selftest: newline-joined
  near-miss deleted refused".
- [Observed] Isolation: with the fixture `history\nreview.md` deleted from the
  tuple and the same mutant applied, `--selftest` exits 0 ("20 real-Git
  cases"). So the join-only fixture is the only one that refuses a
  NUL-to-newline mutant; it is refused only with the NUL split.
- [Observed] The halves are innocent to the published pattern
  (`history`, `review.md`: no match); the join matches. The predicate run on
  the names is False, False, True.

### Note 3 — the two benign no-effect claims

- [Observed] Removing `log = [p for p in log if p]` (one occurrence): exit 0.
  Decoding `'ascii', 'ignore'` for `'utf-8', 'replace'` (one occurrence): exit
  0. Both re-ran at `082a331`, as the notes say.
- [Inferred] Neither can change a verdict, for the reasons the notes give (an
  empty item never starts with the evidence prefix; a name with a dropped byte
  still matches the near-miss pattern). The reason is an argument, not a
  proof; the claim is stated as inferred there and here.

### Rule-6 rows

- [Observed] `history-reading-rule6.json` at `32bc2bf` holds 31 mutants: 28
  recorded at `ca3bed0`, 3 at `082a331`. I applied each of the 3 new rows'
  `old` to `new` from the JSON in a clone at `082a331` (each `old` occurs
  once), ran the row's command, and checked the row's `refusal` string
  against the output: 3 of 3 exit 1, 3 of 3 contain the recorded string. I did
  not re-run the 28 older rows (round 5 did, at `ca3bed0`; the recorder bytes
  are unchanged apart from the +3 fixture lines).

### Notes record's name

- [Observed] `RECORDER-REVIEW-NOTES.md` does not match
  `history[^a-z0-9]*review` case-insensitively (predicate False). Over the
  directory listing, the pattern matches exactly the five
  `HISTORY-REVIEW-<n>-RAW.md` files, which are strictly named.
- [Observed] The notes file quotes no digest; the recorder digest is in no
  tracked file, so the notes add no citer and need no registration.
- [Observed] Denominators the notes state: 1,669 tracked files at `082a331`
  (recounted with `git ls-tree -r`: 1,669).

### Prose

- [Observed] The page's round 5 and round 6 bullets match the state: round 6
  raw required, `--check` failing by design until retained; "three selftest
  fixtures; 22 real-Git cases, was 16" matches the selftest.

## Notes (do not block; owner ruling 2026-09-26 clears these bytes)

1. The 28 older rule-6 rows were not re-run this round (round 5's re-run
   stands for the unchanged behavior).
2. The two benign survivors remain inferred no-effect; no row.

## Verdict basis

No blocking finding. Each new fixture kills its mutant, the join-only fixture
is unique to the NUL split, the three new rows reproduce, and the notes
record's name evades the near-miss pattern.
