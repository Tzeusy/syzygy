# Review — PWB exact-source render mode (round 2, confirmation)
Reviewed commit: abf6ddf1a7d4bd0450ce48a27622abf59175ff4e
Manifest SHA-256: 5796c1541a90a109c0259a079d2262883942d1f97ac36c733ecf2c0c28763433
Verdict: CONFIRM

Reviewer: fresh-context session. No authoring context; the package's own
prose was read only through `REVIEW-BRIEF.md` and `SEMANTIC-DELTA.md`
§Review, as this round's instructions direct. Read-only throughout; every
mutation (`--selftest` aside) ran in a `cp -r` scratch copy under the
session scratchpad, never in the reviewed worktree, and the reviewed
worktree's `.git` was never touched. Class: fresh-reader confirmation review
of a repaired normative delta (CC-REV-2, CC-REV-4, CC-REV-6).

This is round 2. Round 1 (`docs/reviews/R-PWB-EXACT-SOURCE-RENDER-MODE-DELTA-RAW.md`,
commit `08f980f746991b194d4d8dbfb5b6598087aa1e2d`) returned CONFIRM WITH
EXCEPTIONS: F1 revise, F2 revise, F3 note. `SEMANTIC-DELTA.md` §Review
dispositions all three as "Accepted and repaired." This review checks each
repair against the bytes at `abf6ddf`, checks for any new defect the repair
introduced, and re-reads the packet as the owner would.

---

## What I ran

1. `git fetch origin && git checkout -B review/req011-render-mode-confirmation
   abf6ddf1a7d4bd0450ce48a27622abf59175ff4e` → clean checkout;
   `git status --porcelain` empty throughout.
2. Read `AGENTS.md` in full, then the package's `REVIEW-BRIEF.md` (the
   round-1 instrument; unchanged this round — confirmed by
   `git diff 08f980f abf6ddf -- .../REVIEW-BRIEF.md`, no output). Read the
   round-1 raw in full and `SEMANTIC-DELTA.md` §Review's disposition table.
3. `sha256sum PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` →
   `5796c1541a90a109c0259a079d2262883942d1f97ac36c733ecf2c0c28763433`,
   matching both the round-1 raw's recorded digest and
   `OWNER-DECISION-PACKET.md:35` and `:173`. Unchanged, as §Review claims:
   no repair touched a manifest subject. `SEMANTIC-DELTA.md` §Review does
   not copy the digest anywhere in its own text (grepped the file for the
   64-hex string — zero hits) — consistent with rule 10 and with keeping
   exactly one registered copy of the act argument.
4. `python3 scripts/build_pwb_exact_source_render_mode_amendment.py --check`
   → exit 0: "...on a partial scoped-attributes tree the dependency digest
   is detectably inconsistent with the spec.md beside it" — the F3 addition
   is present and running.
5. `--selftest` → exit 0: "...and a self-consistent partial scoped-attributes
   tree fail closed" — nine named predicates (round 1 had eight).
6. `--diff`, saved to scratch; concatenated the four `proposed/*.patch`
   files in manifest-codepoint order (`CAPABILITY-COVERAGE.md`,
   `GOVERNING-DEPENDENCIES.md`, `design.md`, `spec.md`); diffed against
   `--diff`'s output. Byte-identical apart from `--diff`'s own leading
   informational note line (not patch content). No hand-transcription
   (rule 3). Confirmed via `git diff 08f980f abf6ddf -- .../proposed/`
   and the manifest itself: zero output — the four patches and the manifest
   are byte-identical to round 1, so round 1's substantive criteria 1–7 and
   9 (withholding, gates, content class, anchors, parity, vocabulary
   closure, coverage) rest on unmoved bytes and need no re-derivation.
7. **F1.** `grep -rn "269" .../pwb-exact-source-render-mode-scenario/` →
   four hits: `SEMANTIC-DELTA.md:366` (the repaired sentence, now inside an
   `[Inferred — 192 + 77, ...]` bracket that names both addends' sites and
   quotes P-81 Q4), `SEMANTIC-DELTA.md:585` (the disposition table, prose
   about the repair, not a use of the figure), `OWNER-DECISION-PACKET.md:113`
   (already-labeled, unchanged since round 1), `OWNER-DECISION-PACKET.md:197`
   (a forward reference to a future measurement step, not a fresh
   unlabeled assertion). Read `docs/evidence/polaris-m14-provenance-depth-funnel-2026-09-17.json`
   with Python `json.load`: `headline_measurement.post_trim.rule_tally["baseline-spec-tree"]`
   = `192`; `body_classification_for_s5_m2.nonbaseline_blob_classified.count`
   = `77`; `headline_measurement.post_trim.denominator_sources` = `278`. All
   three match what `SEMANTIC-DELTA.md:366-373` cites, exactly by key path.
   Read P-81 Q4 verbatim at
   `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:69`:
   "machine figures Observed, sums Inferred, the 417-minus-415 delta
   Unknown" — the citation is byte-accurate. F1 repaired correctly.
8. **F2.** `python3 scripts/check_governance.py --selftest` → 257 fixtures,
   0 failing (read the output, not the exit code). Reconstructed the
   round-1 baseline by extracting `scripts/check_governance.py` at
   `08f980f` with `git show 08f980f:scripts/check_governance.py` (read-only)
   into a `cp -r` scratch copy of the tree, in place of the current file,
   and re-ran `--selftest` there → 255 fixtures, 0 failing. 255→257
   confirmed independently, not transcribed.
   `git diff 08f980f abf6ddf -- scripts/check_governance.py` → 20 lines
   added, all inside `selftest()`: two new cases,
   `"CG-7e performed PWB render-mode act registers both record copies"` and
   `"...requires aggregate record copy"`, built from a `render_mode_link`
   tuple in the same shape as the existing `PWB_TRUTH_AMENDMENT_LABEL`
   cases. No change to `_act_subjects()`, `ACT_DIGEST_COPY_FILES`, or any
   `_activate_*` function — those were already present from round 1, so
   this round is additive only.
   Rule-6 mutation, in a `cp -r` scratch copy, one change at a time,
   restored between each:
   - Removed the line
     `ACT_DIGEST_COPY_FILES[PWB_RENDER_MODE_ACT] = (PWB_RENDER_MODE_LABEL,)`
     (the dedicated-record registration) → `--selftest`: **1 of 2 new
     fixtures FAIL** ("registers both record copies" fails; "requires
     aggregate record copy" still passes) — 257 fixtures, 1 failing.
   - Restored; removed the `if PWB_RENDER_MODE_LABEL not in labels:
     ACT_DIGEST_COPY_FILES[aggregate] = labels + (PWB_RENDER_MODE_LABEL,)`
     block (the aggregate registration) → **both new fixtures FAIL** — 257
     fixtures, 2 failing.
   - Restored; misspelled `PWB_RENDER_MODE_ACT`'s path string only
     (`AMENDMENT` → `AMENDMNET`) → **0 failing**, both new fixtures still
     pass. This exactly reproduces the disclosed limit in
     `SEMANTIC-DELTA.md:586`: "misspelling the act path constant fails
     neither, because the fixture creates the record at whatever path the
     constant names." Stated correctly and reproduced.
   F2 repaired correctly, with its own disclosed limit holding.
9. **F3.** Built the partial tree by hand, independent of the builder
   script's internal test: in a scratch directory, copied the four current
   (pre-patch) subject files, applied
   `pwb-scoped-attributes-amendment/proposed/spec.md.patch` alone (patches
   clean), then this package's four patches in manifest order (all four
   patch clean, `spec.md.patch`'s hunks land at a 42-line offset with no
   rejection — reproducing the round-1 raw's step-11 finding that no patch
   tool objects). `sha256sum` on the resulting `spec.md`: `5b2d451c...`,
   matching the round-1 raw's recorded composite digest exactly.
   `GOVERNING-DEPENDENCIES.md`'s Source line still names `30ce75f9...` —
   this package's own patched digest, stale against the actual on-disk
   `spec.md`. Independently confirms the exact inconsistency `--check` now
   reports.
   Mutated the detector directly, in a separate scratch copy: flipped
   `if match.group(1) == on_disk:` to `!=` inside `partial_lane_b_findings`
   → `--selftest` → "SELFTEST FAILED: the partial-lane detector fires on
   real bytes", exit 1. The inverse fixture (the no-op lane-B diff making
   the partial tree self-consistent) is genuinely exercised, not vacuous.
   F3 repaired correctly and closed by tooling as claimed.
10. `python3 scripts/check_governance.py` (full run, current commit) → 32
    OK, 20 WARN, 0 FAIL (52 checks); CG-1a 416 links 0 findings; CG-1b 6340
    code-span references 0 findings (the paths under
    `openspec/changes/polaris-project-wide-butlers-model/` that this
    package's own files backtick-cite are this repository's own change
    directory, not a body read from the observed Butlers repository — CG-1b
    resolves all of them); CG-7d 58 quotations, 0 findings; CG-7e 34 files,
    0 findings — same counts as the round-1 raw's step 12.
    Swept both `SEMANTIC-DELTA.md` (the file carrying the F1/F3 repair
    prose) for lines with an odd backtick count outside fences — zero, so
    no citation is broken across the 78-column wrap.
11. Package-deletion check (criterion 5), in a `cp -r` scratch copy with
    `.git` removed: deleted
    `.syzygy/governance/contracts/candidates/pwb-exact-source-render-mode-scenario/`
    entirely, ran `python3 scripts/check_governance.py` (plain) → 31 OK, 21
    WARN, **0 FAIL** (52 checks) — clean, matching the round-1 raw's step
    12 claim for this exact scenario.
    Went one step further than the round-1 raw and also ran `--selftest` on
    that same deleted-package scratch copy: it **crashes**,
    `FileNotFoundError` on `OWNER-DECISION-PACKET.md`, from the
    pre-existing `selftest()` case "CG-7e examines the real act-copy
    population without error" (line ~6169), which calls
    `cg7e_act_digest_copies` against the real `ROOT` and the real
    `ACT_DIGEST_COPY_FILES`, not a synthetic tempdir. Reproduced the same
    crash by deleting the *sibling* `pwb-scoped-attributes-amendment/`
    package instead, in an independent fresh copy — same traceback, same
    line. This is pre-existing, repo-wide `--selftest` behavior that
    predates this round's repairs and is not specific to this package: it
    would fire on the deletion of any currently-registered PWB candidate
    package. Not a new defect from F1/F2/F3; see Findings.
12. Re-read `OWNER-DECISION-PACKET.md` in full, slowly, as the owner would.
    The round-1 disposition, the F3 sequencing caveat, and the "not yet
    offered" sign-off phrase are consistent with each other and with what
    `check_governance.py` actually does today (the recorder is a no-op
    until `PWB-EXACT-SOURCE-RENDER-MODE-AMENDMENT-ACT.md` exists — confirmed
    absent on disk).

---

## Findings

### N1 — note. `--selftest`'s general "examines the real act-copy population without error" case is not robust to any registered PWB candidate package's directory being deleted from disk — not new to this round, and not specific to this package.

*Anchor:* `scripts/check_governance.py:6168-6170` (call site);
`scripts/check_governance.py:2527` (the `read()` call that raises).
*Rests on:* AGENTS.md verification rule 6 (mutate the input and confirm the
check fails **per predicate**) — this particular pre-existing case is not a
predicate with a pass/fail assertion at all; it is a bare "does not
exception" smoke check, so a missing file crashes the whole `--selftest`
run rather than reporting one failing case among 257.

Step 11: deleting this package's directory in a scratch copy leaves the
plain `check_governance.py` run clean (0 FAIL, matching the round-1 raw),
but crashes `--selftest` with `FileNotFoundError` reading
`OWNER-DECISION-PACKET.md`. The same crash reproduces, at the same line,
when the *sibling* `pwb-scoped-attributes-amendment/` package is deleted
instead in an independent copy — so this is a general property of
`--selftest`'s assumption that the live tree is intact, not something F1,
F2 or F3 introduced or could have prevented. Criterion 5 asked about
"check_governance still runs clean" on package deletion; the plain run is
clean (confirmed), and I read this as satisfying that criterion as the
round-1 raw scoped it. I raise it as a note because it is a real fragility
a future session could trip over (e.g. running `--selftest` in a worktree
mid-way through removing a superseded candidate package) and because
CC-REV-6 asks for concrete risks even on confirmation.

*Resolution:* none owed by this package. Worth a standalone repair to make
the "examines the real act-copy population without error" case tolerant of
a missing file (report it as a finding rather than raising), scoped to
`check_governance.py` generally rather than to any PWB package.

**Findings raised and rejected:** none.
**Findings this round confirms as correctly repaired:** F1, F2, F3 (all
independently reproduced above, not merely re-read).

---

## Why CONFIRM

Every repair the disposition table claims is independently reproduced,
not merely re-read. F1: the `269` figure's only bare occurrence
(`SEMANTIC-DELTA.md:366`, the one load-bearing for the change-class
argument) now carries `[Inferred]`, names both addends' exact JSON key
paths, and both addends verify against the cited evidence record by direct
read; the P-81 Q4 quote is byte-accurate. F2: the fixture count moves
255→257 (reconstructed the round-1 baseline independently via `git show`,
not trusted from prose), and three separate mutations reproduce exactly the
three behaviors the disposition claims — 1-of-2 failing, 2-of-2 failing,
and the disclosed limit (0 failing) — no more, no less. F3: hand-built the
exact partial tree byte-for-byte, reproduced the round-1 raw's recorded
`5b2d451c...` digest and the stale `GOVERNING-DEPENDENCIES.md` line, and a
direct mutation of the detector's equality check proves the new inverse
`--selftest` fixture is real rather than vacuous.

The manifest digest, the four proposed patches and `REVIEW-BRIEF.md` are
byte-identical to round 1 (confirmed by diff, not assumed), so round 1's
substantive judgment on criteria 1–7 and 9 — withholding is unconditional,
gates run on the complete body before any encoding, no content class
widens, anchors stay presentation-only, parity is per rendered tuple, the
mode vocabulary is closed in the text, coverage's population and totals
hold — rests on unmoved bytes and needs no re-derivation this round. Rule
10 is stated correctly in `SEMANTIC-DELTA.md` §Review: round 1 confirms
`08f980f`, not these bytes, and a second fresh reviewer was required before
the phrase could be offered — this review is that reviewer, and none of the
three repairs disturbed the manifest subjects. `check_governance.py` is 0
FAIL both on the reviewed commit and with the package directory deleted
(plain run); the only irregularity I found (N1) is pre-existing, general to
`--selftest`, and reproduces identically on the sibling package, so it is
not a defect this round introduced and does not weigh against CONFIRM. The
owner packet is internally consistent, correctly still withholds the
sign-off phrase, and its named risks (the page-size ceiling, the ordering
caveat) match what the tooling actually does today.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_016rwoqL9MW8v8nLyhQC7iY5
