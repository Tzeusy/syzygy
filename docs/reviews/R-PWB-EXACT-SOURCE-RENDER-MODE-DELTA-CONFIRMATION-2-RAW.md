# Review — PWB exact-source render mode (round 3, confirmation of regenerated package)
Reviewed commit: 41dac2b8a7b8501a1e693fe31d81aae2fa5be707
Manifest SHA-256: 527be5ac3732619608355ae9658c92cee45341e831521bc526398481dd915785
Verdict: CONFIRM WITH EXCEPTIONS

Fresh-context reviewer (CC-REV-1), no authoring context. Worktree detached at
41dac2b; all mutation-class work (patch application) done in a `git archive`
copy under the session scratchpad. Worktree removed afterwards.

Digest note: `sha256sum` of the package's
`PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` file is
`527be5ac3732619608355ae9658c92cee45341e831521bc526398481dd915785`, which is
also the act argument the packet phrase names
(`OWNER-DECISION-PACKET.md` lines 35 and 173). The two are the same value; there
is no separate act-argument digest to state. The prior round (CONFIRM, over
`5796c154…`) is retired as to these bytes by rule 10 because the manifest
moved; this round stands in its place.

## Checks run this session (outputs read)

1. **Diff 0b6c583..41dac2b over the package.** `git diff` shows exactly three
   files, 6 insertions and 6 deletions, and nothing else:
   - `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`: two rows only (the
     GOVERNING-DEPENDENCIES.md row `787d983e…` -> `de3f7b8f…`, the spec.md row
     `30ce75f9…` -> `14e01af3…`). Nine other rows unchanged.
   - `proposed/GOVERNING-DEPENDENCIES.md.patch`: the one `Source: spec.md
     sha256` line, `9a44bdb6…` -> `14e01af3…`. `9a44bdb6…` is the sha256 of
     the current tree's `spec.md` (confirmed with `sha256sum`) and the
     opening-band base's spec digest; `14e01af3…` is the post-patch digest.
   - `OWNER-DECISION-PACKET.md`: the two digest copies (lines 35 and 173)
     only.
   The patches `CAPABILITY-COVERAGE.md.patch`, `design.md.patch` and
   `spec.md.patch` are byte-identical to the previously reviewed ones. The
   delta's prose (`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `REVIEW-BRIEF.md`)
   is unchanged.
2. **Builder.** `python3 scripts/build_pwb_exact_source_render_mode_amendment.py
   --check` printed: manifest matches 11 proposed behavior subjects (4
   patched, 7 unchanged); the generated dependency file carries the proposed
   spec.md digest; the 3 semantic patches apply and the generated one collides
   as declared on the scoped-attributes tree; the partial-tree dependency
   digest is detectably inconsistent. `--selftest` printed that closed
   population, byte drift, path order, subject drift, patch corruption,
   transcribed generated digest, wide-context lane collision, absent
   regeneration collision and the self-consistent partial tree all fail
   closed.
3. **Independent composition.** In a `git archive 41dac2b` copy I ran
   `git apply --check -p1` then `git apply -p1` for all four patches (no
   errors), then recomputed sha256 of each of the 11 post-apply files in
   Python and compared with the 11 manifest rows: 11 rows, 0 mismatches. The
   check used no builder code and no transcribed digest.
4. **Opening-band collision.** The opening-band act (commit eb6c66f) added one
   scenario ("One opening Unknown aggregate, reconciled with members",
   `spec.md` lines 621-634 post-apply) inside the PWB-REQ-010 region, plus a
   GOVERNING-DEPENDENCIES digest line. The spec patch hunks are at old lines
   637/664 and `git diff --no-index -U0` of current vs composed spec shows
   changes only at old lines 655-683 (inside PWB-REQ-011, header at 648), 5
   deleted lines, all in PWB-REQ-011. Every line mentioning "opening" is
   identical before and after; the opening-band scenario is present in the
   composed spec. No collision, no silent drop. The five deleted lines
   (patch file) are the old PWB-REQ-011 Oracle/Observable/Falsifier wording
   and the old coverage row 10 and the one generated digest line, i.e. the
   intended replacements.
5. **Criteria 1-2 spot check against the composed `spec.md` 648-757.**
   - Withholding: "A source whose record outcome is excluded SHALL NOT be
     served in any mode", "no route or sink SHALL carry any of its body
     bytes", the scenario "Withheld source stays digest-only", and the
     falsifier "an excluded source is served in any mode". I tried: the
     anchor route (anchors apply only to "a source the route serves"), the
     whole-body mode (restricted to sources "admitted by this evaluation as
     a classified blob"), the requirement-sections mode (restricted to
     baseline specs already selected), and the closed-set clause (a third
     mode is outside the set). I could construct no reading serving any of
     the nine.
   - Gates: "Every mode SHALL apply the same authority, exact-object,
     secret-detection and inert-content gates to the complete transient body
     before encoding any part of it; a failed gate SHALL leave that body
     Unknown with its reason". "Complete transient body" ahead of "any part"
     blocks the per-section reading; the whole-body scenario repeats "its
     complete transient body". The baseline scenario still says "only that
     requirement and its scenarios" is encoded, but it is governed by the
     requirement paragraph's complete-body gate sentence (see note N2).
   - No wider class: both modes and scenarios keep "already selected by the
     signed source population" and "grants no wider content-class access".
6. **Governance.** `python3 scripts/check_governance.py` in the worktree:
   "31 OK, 21 WARN, 0 FAIL (52 checks)". The only line matching FAIL in the
   output is that summary. `check_docs_review_campaign_partition.py` in the
   main checkout reported `unmatched=0` before this raw was written (see
   note N3).

## Findings

No blocking findings. No revise findings.

- **N1 (note)** `REVIEW-BRIEF.md:16`: "This is the **first round**. There is
  no prior raw review of this delta" is false for the bytes now at HEAD: two
  retained raws exist
  (`docs/reviews/R-PWB-EXACT-SOURCE-RENDER-MODE-DELTA-RAW.md` and
  `docs/reviews/R-PWB-EXACT-SOURCE-RENDER-MODE-DELTA-CONFIRMATION-RAW.md`,
  the latter line 1-4 CONFIRM over `5796c154…`). The brief was unchanged by
  the regeneration, and editing it retires this review, so it should be
  disclosed in a sibling record rather than edited. This does not mislead the
  owner decision; it is a stale sentence in a reviewer instruction.
- **N2 (note)** `spec.md` composed line 710-714 (scenario "Consented baseline
  requirement renders verbatim"): "Polaris may transiently encode only that
  requirement and its scenarios verbatim" sits beside the requirement-level
  sentence that gates the complete transient body. They are consistent
  (gate on the complete body, then encode one section), and the package's
  criterion 2 reading holds, but the two sentences are not cross-referenced in
  the scenario itself. No change requested; a reader could stop at the
  scenario.
- **N3 (note)** `SEMANTIC-DELTA.md:562-590`: the §Review section records only
  round 1 (commit 08f980f) and says a second fresh reviewer is required; it
  does not record the CONFIRM round 2 (over `5796c154…`) or this round 3 over
  the regenerated manifest. Editing the file retires the review, so the round
  history belongs in the sibling disposition record the owner's stopping rule
  provides, not in the delta. Also: this raw's basename must match a campaign
  pattern in `scripts/check_docs_review_campaign_partition.py` (the
  `-CONFIRMATION-2-RAW.md` form) and a `docs/README.md` row/count must be
  added in the same commit that lands it; I did not run the partition check
  after writing this file.
- **N4 (note, scope of this round)** The regeneration changes neither the
  semantics nor any non-generated byte. Criteria 3-12 of the brief were not
  re-derived from scratch beyond the spot checks above; they rest on the
  unchanged round-2 CONFIRM for the unchanged patches and prose, and on
  byte-identity of those files shown in check 1. That reliance is `[Inferred]`
  from the unchanged-bytes diff, not `[Observed]` by a fresh read of each
  criterion.

## Limitations

The earlier round's CONFIRM does not carry over by itself; the confirmation
here is bound to manifest `527be5ac…` at 41dac2b. Any later edit to a
manifest subject, the packet, or the package prose retires it (rule 10).
