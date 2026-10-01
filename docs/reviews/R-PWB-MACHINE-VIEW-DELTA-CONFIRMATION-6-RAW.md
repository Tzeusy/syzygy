# Review — PWB machine-view amendment (round 7, fresh confirmation of regenerated package)
Reviewed commit: e58fd1cd1021734a6a617e87424ad3b531c3a61c
Manifest SHA-256: acabc7915e4461186b5878ce40cc0c62ed7cf91eadd7eead1cb179c80f672e72
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh context, CC-REV-1. Detached worktree at e58fd1c; mutations and composition in a `git archive` copy in the scratchpad. No other reviewer raw and no ROUND-*-DISPOSITIONS.md was read. Package: `.syzygy/governance/contracts/candidates/pwb-machine-view-amendment/`.

## Checks run this session

1. `git diff 5affbee..e58fd1c -- <package> scripts/build_pwb_machine_view_amendment.py` shows exactly three files changed, 8 insertions and 8 deletions. [Observed]
   - `proposed/GOVERNING-DEPENDENCIES.md.patch`: the `Source: spec.md sha256` line only, 14e01af3... to fe9afdb5... on the base side and 42d073cd... to f57c37a8... on the proposed side.
   - `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`: four rows (CAPABILITY-COVERAGE.md, GOVERNING-DEPENDENCIES.md, design.md, spec.md).
   - `OWNER-DECISION-PACKET.md`: two digest copies (line 40 and line 180) 2a49a8d1... to acabc791...
   - The builder script has no diff. No other file in the package changed.
2. Builder checks, output read:
   - `--check`: "matches 11 proposed behavior subjects (2 patched, 9 unchanged); the dependency declaration is regenerated from the proposed spec and the spec patch composes with the sibling candidate in either order".
   - `--selftest`: all fail-closed cases listed, no failure.
   - `--diff`: 59 lines, touching only GOVERNING-DEPENDENCIES.md (one Source line) and spec.md (one hunk, 34 added lines in PWB-REQ-020).
   - `sha256sum` of the manifest file is acabc791...72e, equal to the packet's quoted digest at lines 40 and 180.
3. Independent composition: the `--diff` output applied with `patch -p1` to a clean archive of e58fd1c. The patch succeeded (spec hunk at offset +80, see Finding 1). A shell loop (`sha256sum` per manifest path, sorted, `diff` against the manifest rows) printed DIGESTS_EQUAL over all 11 rows. [Observed]
4. Collision check of the composed PWB-REQ-020 against the applied PWB-REQ-010 (opening-band, spec.md lines 596-646) and PWB-REQ-011 (render-mode, lines 648ff). [Observed, then Inferred]
   - REQ-010's third scenario states the machine answer carries the opening aggregate "under PWB-REQ-020". The composed REQ-020 keeps the machine answer as the comparison baseline and adds no obligation that this contradicts.
   - REQ-011 requires the mode, source identity and refusal reason to be "recoverable, per rendered tuple, from the same evaluation in the machine answer". That is the existing parity direction. The new derived-view clause ("composes only values already reachable from the machine answer", "subtracts nothing") is consistent with it, and it does not move render modes or scroll anchors out of the compared multisets.
   - REQ-011 says a scroll anchor is presentation only and does not enter any anchor identity. That sits cleanly beside REQ-020's "source anchor" multiset.
   - The unchanged REQ-020 body (parity sentence, Case, Observable, Oracle, Oracle independence, Mutation proof, Falsifier, Scenario, warrants) appears byte-identical in the composed text. The patch adds lines only, before the parity sentence.
   - Two small tensions are recorded as Findings 2 and 3.
5. Brief criteria read against the composed spec (lines 982-1019):
   - Closed categories: both are enumerated, with one named member each for the draft view and two for the derived view. "A route enters either category only by a later amendment ... naming it as a member" is unambiguous.
   - Disjointness: the draft view composes only recorded generation-run bytes, and the derived view composes only values reachable from the machine answer. The two definitions do not overlap.
   - Read-only: both say "writes nothing".
   - Machine-credentialed: both say so "in every mount form".
   - Non-authoritative: not stated as an explicit sentence in REQ-020. It follows from "mints no project fact" and "is neither the machine answer". I treat this as sufficient, and I raise it only as a possible wording point in Finding 3.
   - Unnamed routes: "a route this specification does not name is a member of neither" and "neither admitted nor forbidden by this requirement". This does not license a route, because other requirements and acts still gate it.
   - Ceiling: "SHALL NOT be served before the adapter-registry entry's resource envelope declares that ceiling". The existing Polaris member uses the registry's existing machine-JSON ceiling and is not newly constrained.
   - Drafts never write or egress: "writes nothing, sends no source or draft byte outside the observing project".
6. `python3 scripts/check_governance.py` at e58fd1c: "31 OK, 21 WARN, 0 FAIL (52 checks)". [Observed]

Not re-derived this session: the ledger's 121-over-1,334 blast-radius figure (criterion 8) and the full "does NOT change" list beyond what the 9-unchanged-rows check and the diff cover. The patches touch only spec.md and GOVERNING-DEPENDENCIES.md, so criterion 7's claim holds at the byte level. [Observed]

## Findings

**Finding 1 — Patch hunk header and index line are stale against the current base** (note) `proposed/spec.md.patch:1-6` carries `index 543469d..8110290` and `@@ -903,6 +903,40 @@`. The pre-amendment base for the spec now sits at line 983 (patch applied with offset +80 after the opening-band and render-mode acts). The post-apply bytes and manifest digests are correct. Only the context coordinates are stale. The patch is not regenerated at the line level and `git apply` strictness would depend on fuzz. The builder tolerates the offset. A `--write` that rebuilt the patch headers would remove the discrepancy.

**Finding 2 — SEMANTIC-DELTA.md Baseline paragraph is now false** (note) `SEMANTIC-DELTA.md:51-55` says "None of the eleven behavior subjects changes between that commit [a4a34510...] and the commit carrying this draft". Since then the opening-band and render-mode acts changed spec.md and (via regeneration) the dependency declaration, as the `5affbee..e58fd1c` and spec-blob history show (3209098, eb6c66f). The sentence was true at drafting. It is stale-by-design in the same way as §Review, and it is not marked at the sentence (see AGENTS.md guidance on marking staleness at the stale sentence). Same for the §Ordering count of sibling packages "re-derived at 76b4beb" (`SEMANTIC-DELTA.md:552-557`), where two of the five listed siblings have since been performed and now sit in the base rather than beside it.

**Finding 3 — The draft-view definition is silent on two points a derived draft view would meet in the now-applied REQ-011** (note) `spec.md` (composed) lines 1002-1009 say the draft view "carries no ... source anchor" and is composed of recorded run bytes "over sources that run was already admitted to read".
   - A real generation draft normally cites sources, and REQ-011 now defines scroll anchors and revision-bound source identities for exact-source routes. A literal reading of "carries no source anchor" would forbid such a citation, while the intent seems to be "no parity-compared anchor identity". The wording does not say which.
   - REQ-011 also requires that an excluded source's body bytes be carried by no route. The draft view says only "already admitted to read" and does not restate that excluded-source bodies, or bodies that failed the secret and inert-content gates, cannot appear in a recorded draft. Compliance with REQ-011 is probably implied by "already admitted", but admission by a run is not the same as the evaluation's current classified-blob outcome.
   Neither point blocks the closure or disjointness arguments. I recommend an owner choice between leaving the ambiguity for the later route amendment (which would name the member and its fields) and stating the restriction now.

## Verdict basis

Digest, composition, builder checks and the governance battery all reproduce at e58fd1c. The only package changes since 5affbee are the intended digest lines. I found no blocking or revise-level defect. Three notes remain, so CONFIRM is not available under the stated rule.
