# Fresh-context review (round 7) — PWB container-shape profile amendment (N8, syzygy-u05.8)
Reviewed commit: 18ad54dc271bf21409012ec1f69e0f24ccbaf4a8
Manifest SHA-256: afe181c82ed78bf1eeb5ac559f612ad21647b2e526a160092b0112786c512aae
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh context (CC-REV-1). Earlier raws and dispositions were not read. Only notes remain; no defect makes the normative text wrong or unsafe.

## What was run (detached worktree at the commit, then removed)

- [Observed] `--check` passes: 11 subjects (3 patched, 8 unchanged), whole-spec pin with 8 edits, 23 PWB-REQ-002 rules, 5 scenarios. `--selftest` prints "182 mutants killed", the figure the brief and packet state. `--diff` prints the three patches. `check_governance.py`: 31 OK, 21 WARN, 0 FAIL (52 checks); its `--selftest`: 357 fixtures, 0 failing.
- [Observed] Digests recomputed by script: the three patches applied in a `git archive` copy give spec.md 6aa52fe5..., CAPABILITY-COVERAGE.md b26c4dfd... and GOVERNING-DEPENDENCIES.md 8064c64a..., each equal to its manifest row. The other 8 rows equal the current files (`--check`).
- [Observed] Composition: the opening-band, render-mode, machine-view and dismissal-expiry spec patches reverse-apply on the current spec (already applied). The lane-B patch applies neither way, consistent with its recorded decline. This package's spec patch applies forward only. The missing-currency patch applies both ways (its scenario text is already present and the patch is not offered again). No unapplied sibling touches the lines this package edits.
- [Observed] The shared text was checked against `1d5966c` of `agent/tier4-dov24`, fetched read-only. With that builder temporarily placed in the archive tree, `SHAPES` is equal (9) and the 7 non-fixed key-form sentences are equal; `--check` then reports "match the loaded-profile amendment's builder". The temporary copy was removed.
- [Observed] Shape and key-form sentences were read against `project-shape-extraction.ts` lines 340-462 (heading-section, every-level-2-section, decimal and bulleted lists, leading-bold, leading-bold-or-code, duplicate-key). The sentences agree with the code on failure classes and the empty-bulleted-list case. The class-to-category sentence agrees with `CLASS_ROWS` (coverage.ts 85-95).
- [Observed] Independent mutants, made by editing the patch in the archive copy, each failed `--check` on the named predicate: refused profile "never returns" changed to "may return" (refused-profile-does-not-fall-back); "never substitutes" changed to "may substitute" (no built-in substitute once loaded); sources "fails" changed to "may fail" (sources fail); "never zero" dropped (project with no profile); oracle "must" changed to "may" (oracle: written Butlers grammar); the "reports a known item denominator" falsifier clause dropped (falsifier: project with no profile); category Unknown changed to known (class and category Unknown); craft-policy category changed (other categories); "at most two" changed to "three"; "never a heading" changed to "may be". Each also trips the whole-spec text pin first, so the named predicate is a second, redundant detector.

## VIS-2 / VIS-3 / PWB-REQ-020 attack

- [Inferred] A missing, bad or unreadable profile class yields an Unknown class and category item denominator with every source kept in the source-path population. A refused or declared-but-unread Butlers profile does not return to the written grammar. A non-Butlers project with no loaded profile gets Unknown, never zero. I found no path in the patched text where Unknown folds into a known count or zero, and no fallback to a built-in rule once a profile is loaded.
- [Inferred] Hidden or collapsed content: the patch adds no render rule. PWB-REQ-002's Observable clause (machine answer and Polaris) and PWB-REQ-020 are unchanged and not weakened.
- [Inferred] The window between a Butlers profile being declared and limb 5 reading it is disclosed in the packet (question 7), not hidden.

## Findings

**Finding 1 — "reproduces" in the oracle has no stated test, so the written-grammar comparison can be read as unfalsifiable** (note)
`proposed/spec.md.patch:209` says that for Butlers read through a loaded profile "that reproduces the grammar written in these reader definitions", both extractors also apply the written grammar. Nothing says whether "reproduces" is decided by the profile's rows, which is structural, or by equal output. If it is decided by output, a profile whose output differs from the written grammar is simply not one that "reproduces" it, and the comparison cannot fail. Scenario 1 (patch line 237) asserts equality but gives no way to decide the premise. Reading it as structural makes it falsifiable, so this is wording and not a safety defect. Suggest saying so at the next amendment.

**Finding 2 — no rule for a row whose shape and key form are each in the vocabulary but cannot be combined** (note)
`proposed/spec.md.patch:127` and `:143`: a row carries exactly one shape and one key form. Unreadability is defined by three conditions: a term outside the closed sets, a missing parameter, or too many headings. A pairing such as `tree-path` with `leading-bold`, or `heading-section` with `first-cell-link-text`, meets none of them. Several key-form sentences fail such a source on their own (for example `first-cell-link-text` fails as malformed-row), so most pairings land on a failing source and Unknown. The text still does not say that every incompatible pairing is unreadable, so a loader could read one. The falsifier "an item is read through a shape or key form its governing grammar does not declare" does not reach it, because both are declared. The text stays fail-closed through per-form failure rules, so this is a note. It belongs with the shared-sentence repairs routed to `syzygy-dov.32`.

**Finding 3 — the prose compares sentences against the sibling builder only when that file is present** (note)
`scripts/build_pwb_container_shape_profile_amendment.py:1900-1908`: on `main` the sibling builder is absent, so `--check` proves identity only by the pinned digest. I did the sentence-by-sentence comparison manually and it agrees (see above), so there is no discrepancy. It remains an on-main limitation until PR #123 lands, and the check output says so.

No finding is blocking or revise. By the owner's stopping rule, notes alone clear these bytes for a version-tagged sign-off offer; any edit retires this review.
