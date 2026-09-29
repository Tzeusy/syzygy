# Recorder review notes, round 5 to round 6

Sibling record for `HISTORY-REVIEW-5-RAW.md`'s four notes (owner ruling
2026-09-26: a notes-only round clears its bytes; notes go here, not into the
raw). The basename deliberately avoids the recorder's near-miss pattern
`history[^a-z0-9]*review`, which refuses any other such name in this
directory. It quotes no act digest, so it needs no `ACT_DIGEST_COPY_FILES`
row (see Registration).

Recorder change (bead syzygy-ehgz, commit `082a331`): three fixtures in
`history_population_selftest()`. Real-Git cases 16 to 22 (each fixture runs
on disk and committed-then-deleted, so 3 fixtures add 6). The predicate
published in `HISTORY-READING.md` is unchanged.

## Dispositions

1. **Separator class and `search` unpinned.** Fixed.
   - `history.review-2-RAW.md` (dot separator): with the class narrowed to
     `[-_ ]*` the selftest exits 1 at "dot-separated near-miss on disk
     refused".
   - `old-history-review-2.md` (prefixed): with `.search` changed to `.match`
     the selftest exits 1 at "prefixed near-miss on disk refused".
2. **NUL split unpinned for newline names.** Fixed, by search.
   - [Observed] Review 5's premise held for `history-review-2\nx.md`: with
     only the NUL split replaced by a newline split it is still refused,
     because its first half is itself a near miss.
   - [Observed] Its deleted variant is not refused when both `-z` and the NUL
     split are reverted (git quotes the name), which the pre-existing
     non-ASCII fixture also shows.
   - Search log (probe over on-disk and deleted variants): `x\nhistory-review-2.md`,
     `history\nreview-2.md` and `history-review-2.md\n` all have a half that
     is a near miss, so a NUL-to-newline mutant refuses them. `a\nb.md`
     is innocent whole and in halves.
   - `history\nreview.md` is the fixture: each half is innocent, the join
     matches (`\n` is in `[^a-z0-9]*`). With `.replace('\\0', '\n').splitlines()`
     in place of `.split('\\0')` (git's `-z` kept) the on-disk variant is still
     refused and the deleted variant is accepted; the selftest exits 1 at
     "newline-joined near-miss deleted refused", and the non-ASCII fixtures
     pass. It fails on that fixture only.
3. **Two benign survivors.** No rule-6 row; [Inferred] no-effect, as review 5
   inferred.
   - Removing `log = [p for p in log if p]`: an empty item never starts with
     the evidence prefix.
   - Decoding `'ascii', 'ignore'` for `'utf-8', 'replace'`: a name with a
     dropped byte still matches the near-miss pattern. Both re-ran at
     `082a331` and still exit 0.
4. **Head contract enforced only by the brief.** Unchanged by design; the
   round 6 brief quotes it (both lines within the first four non-blank
   lines). The recorder scans the whole text.

## Registration

`git grep -n -F REVIEW-NOTES.md -- scripts` returns nothing: the precedent
sibling (`spec-policy-readability-restyle/REVIEW-NOTES.md`) is not registered
in `ACT_DIGEST_COPY_FILES` or `_act_subjects`, and this record quotes no
digest, so it is not registered either.

## Digest sweeps (`git grep -F`, at `082a331`)

This record quotes no digest, so it does not add a citer. The digest of the
recorder after `082a331` is computed with `sha256sum` and quoted in the
round 6 brief, not here.

- Recorder digest after `082a331` in tracked files: 0 (expected 0 until
  `HISTORY-REVIEW-6-RAW.md` lands, then 1).
- Round 5's bound recorder digest in tracked files: 1,
  `HISTORY-REVIEW-5-RAW.md`. Denominator: all 1,669 tracked files at
  `082a331`.

## State

`record_polaris_understanding_adoption.py --check` fails by design with
"latest history review does not bind the current recorder: ...HISTORY-REVIEW-5-RAW.md"
until a fresh-context `HISTORY-REVIEW-6-RAW.md` is retained.
