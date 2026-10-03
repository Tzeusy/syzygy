# R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-6 — screening scope v2 review, round 6 (narrow delta)
Reviewed commit: 8a0bb2a187ecab562d4672e3e115439e26d392e5
Manifest SHA-256: 7757e70c4d0e8e65c19c77f4970853967456cdd7f225077feac1f91e16200e1e
Verdict: REVISE

Reviewer method: I am a fresh-context governance reviewer (Claude Opus 5.5). I ran `git fetch origin`, then worked only in a detached worktree of 8a0bb2a1 under my scratchpad. I reviewed the repair diff `git diff fd4e2509 39d83718` over the package (without `reviews/`) and the builder, and then the 39d83718..8a0bb2a1 commit. To check the rule against the patches, I took the version-1 bytes from the builder's `v1_bytes`, applied each committed `proposed/*.patch` with `git apply` in a scratch repository, compared the result with `propose()` and with the manifest row, and took the `project-documentation` rule out of each patched JSON. I then ran probe paths through the builder's reference reader (`classify_documentation`) under each variant's rule. I applied five source mutants to the builder and restored each with `git checkout -- .`; `git status --porcelain` was empty at the end. I called no model provider, read no external repository body, and made no network calls other than git fetch and ls-remote. I edited no tracked file in the main checkout. The manifest digest above was computed by `sha256sum` and printed identically by `--manifest-digest --pending-prerequisite`.

## Checks run (this session, at the reviewed commit)

- [Observed] `--check` printed "public-source screening scope v2: current" and exited 0.
- [Observed] `--selftest` printed "selftest: 116 of 116 predicates held" and exited 0.
- [Observed] `--ready --pending-prerequisite` printed "current" and exited 0. It also printed two NOTE lines: the class is not in the installed RFC-0005 text, and the version-1 act is not recorded.
- [Observed] `--manifest-digest --pending-prerequisite` printed 7757e70c4d0e8e65c19c77f4970853967456cdd7f225077feac1f91e16200e1e. `sha256sum` of the manifest file gives the same value.
- [Observed] `python3 scripts/check_governance.py` printed "32 OK, 21 WARN, 0 FAIL (53 checks)".
- [Observed] For all 4 variants, the committed patch applied to the v1 bytes equals `propose(v1, variant)`, and its SHA-256 equals that variant's manifest row (4 of 4).
- [Observed] With the variant words masked, the 39d83718 hunks of the four patches hash identically. Each patch moves 6 lines (`notMapped` and `indeterminate`). The rule text, `docExcludedTokens`, the separators, the license roots and the suffixes are unchanged.
- [Observed] Criterion 8: a 64-hex sweep over the 9 package Markdown files outside `reviews/` found 0 tokens. The words accepted, approved and adopted appear only in REVIEW-BRIEF.md:57, the criterion that prohibits them.
- [Observed] The stated diff holds. `git diff --shortstat fd4e2509 39d83718 -- <package minus reviews> <builder>` reports "9 files changed, 77 insertions(+), 37 deletions(-)", and the commit-only diff `39d83718~1..39d83718` reports the same. The 9 files are the packet, the delta, the brief, the manifest, the four patches and the builder, exactly as packet:9-11 lists them. The intermediate commits 3004939c, 5c7aba3d, 65c77a0e and a358200a touch only the recorder, the installer, the simulator and check_governance.py, all outside the reviewed paths. 8a0bb2a1 changes exactly three files: the round-5 raw (new), ROUND-5-DISPOSITIONS.md (new), and packet lines 7-14, which hold the review-state statement and nothing else. The retained round-5 raw is byte-identical (`cmp`) to the scratch copy written by the round-5 reviewer.
- [Observed] RFC5-12 to RFC5-17 are at `contracts/rfcs/RFC-0005/consent-egress-secrets.md` lines 95, 115, 134, 182, 232 and 283 (DIRECTIVE-REGISTER.md:336-341). The PR #257 class text is at `rfc5-project-documentation-class/SEMANTIC-DELTA.md`:47. The round-5 diff does not change the rule, so its RFC5-14 conformance is as round 5 found it.

## Round-5 findings against the bytes

**R5-1: repaired on the withheld side, but the new clause introduces R6-1.** [Observed] The reader maps licenses/README.md, LICENSE.txt, CHANGELOG.md, NEWS.md, 00-README.md and AUTHORS.md in all four variants. It withholds src/README.md, src/NEWS.md, vendor/x/README.md, licenses/sub/README.md and licenses/sub/LICENSE.txt. The first clause of packet:44 / delta line ("outside docs, doc and licenses") agrees with these results. In all four patches, `notMapped` now says "outside docs-tree and licenses-tree" and `indeterminate` gives "src/README.md" as its example. Both agree with the reader, and Q4 (packet:115-118) no longer contradicts the list. The second clause, new in 39d83718, is false for some files: see R6-1.

**R5-2: repaired.** [Observed] Packet:37 and the delta now say "from the docs and licenses withholding". `notMapped` says "docs-tree and licenses-tree paths whose directory or file name has a word". The reader agrees: licenses/MANIFESTO.md is mapped only under manifesto and both, and licenses/ARCHITECTURE.txt only under architecture and both.

**R5-3: repaired, with one weak guard (R6-2).** [Observed] `SENTENCE_EXAMPLES` (builder:124) feeds both `scope_sentence()` and `examples_hold()`. I ran the claimed mutants:
- M1, `["Security", "ADR0001"]`: fails `--selftest` (115 of 116) and `--check`.
- M3, `["SecurityPolicy", "sub/ADR0001"]`, a genuine "mapped in docs, withheld in licenses" example: fails `--selftest` (115 of 116).
- M2, `["SecurityPolicy", "licenses-policy"]`: also fails.

The sentence now says "inside the mapped paths is sendable". The reader withholds src/policy-notes.md and notes.md, and maps docs/SecurityPolicy.md, docs/ADR0001.md, licenses/SecurityPolicy.md and licenses/ADR0001.md in all four variants.

**R5-4: repaired.** [Observed] REVIEW-BRIEF.md is the round-6 brief. Criterion 12 covers the round-5 diff. Criterion 1 now names the `docExcludedTokens` opt-in words and the `policyVersion` suffix. The recording section names the round-6 raw. ROUND-5-DISPOSITIONS.md:8-17 records that the lead asked for round 5 and that it supersedes the round-4 "no round 5" sentence.

**Review-state statement (packet:7-14): true at these bytes.** [Observed] The round-4 raw has verdict REVISE. 33b15a65 is the round-4 repair. The round-5 raw at fd4e2509 has verdict REVISE. The counts and the file list are correct (see above). [Inferred] The statement "are unreviewed until round 6 reads them" becomes true when this raw is written.

## Findings

**Finding R6-1 — the clause the R5-1 repair added says a file directly inside licenses is mapped "whatever its stem unless a word above withholds it". The rule withholds such a file when its suffix is not .md or .txt, so the generated list now overstates what is sendable and contradicts its own lines 36 and 45.** (revise)

Evidence:
- [Observed] OWNER-DECISION-PACKET.md:44 and the matching generated line in SEMANTIC-DELTA.md (builder:595-598, new in 39d83718) read: "a file directly inside a top-level licenses folder is mapped whatever its stem unless a word above withholds it."
- [Observed] Under the rule taken from each variant's patched bytes, the reference reader **withholds** licenses/LICENSE, licenses/COPYING, licenses/README and licenses/README.rst in all four variants. None of these names contains a denylist word, so the clause's only stated exception does not apply. The licenses-tree rule in the policy bytes (none.patch:27) requires a name that "ends with one of licenseTreeSuffixes" (.md, .txt).
- [Observed] Within the same generated block, packet:36 ("Files ending .md, .txt directly inside a top-level licenses folder") and packet:45 ("Any other path … indeterminate and withheld") place these files as withheld, and packet:44 places them as mapped. SEMANTIC-DELTA.md:56-58 calls these lists "the only statement of what is sendable and what is withheld".
- [Observed] The selftest predicate added for R5-1 (builder:803-810) uses only .md and .txt fixtures, so it cannot see this.
- [Inferred] The error runs toward overstating sendability, not toward making text sendable. The policy bytes are correct and fail closed, `notMapped` and `indeterminate` are accurate, and no governance-shaped or unscreened text becomes sendable. It is still a false packet claim in the list the owner signs against, the same shape as R5-1, which round 5 graded revise. Extensionless licence files (licenses/LICENSE, licenses/COPYING) are a common layout, so the gap is not hypothetical.

Proposed repair: generate the clause from the constant, for example "a file directly inside a top-level licenses folder whose name ends {' or '.join(LICENSE_TREE_SUFFIXES)} is mapped whatever its stem unless a word above withholds it". Add licenses/LICENSE and licenses/README.rst as withheld fixtures to the builder:803-810 predicate. Only the packet and delta generated blocks change; the patches and the manifest rows do not.

**Finding R6-2 — the predicate "an example that is mapped in docs but withheld in licenses is caught" uses an example that is withheld in docs too, so the licenses half of `examples_hold` is unguarded.** (note)

Evidence:
- [Observed] Builder:801-802 tests `not examples_hold(["Guide", "licenses-policy"], rule)`. The reader withholds docs/licenses-policy.md (the word policy), so the docs half alone fails the predicate.
- [Observed] Mutant M4 removes `LICENSE_TREE_ROOTS[0]` from `examples_hold` (builder:556). It **survives**: `--selftest` holds 116 of 116 and `--check` reports current.
- [Inferred] The disposition's two mutants (M1, M3) do fail, so the R5-3 claim holds. Only this one guard predicate's label is false.

Proposed repair: use a name that is mapped in docs and withheld in licenses, for example `"sub/Guide"`.

**Finding R6-3 — the R5-1 predicate checks tree names by substring.** (note)

Evidence:
- [Observed] Builder:805 requires `all(r_ in wl[0] for r_ in DOC_TREE_ROOTS + LICENSE_TREE_ROOTS)`, and "doc" is a substring of "docs".
- [Observed] Mutant M5 rewrites the line to "outside docs and licenses". It survives `--selftest` (116 of 116). Only `--check` catches it, through file drift.

Proposed repair: match whole words, for example `re.search(rf"\b{r_}\b", wl[0])`.

**Finding R6-4 — the packet still describes the recorder as not yet written.** (note)

Evidence:
- [Observed] Packet:57-58 says "A recorder is written after the review and takes the chosen row". Packet:90-93 says "the recorder, when written, must refuse a second variant act". At this commit, `scripts/record_public_source_screening_scope_v2_act.py` exists, added in 3004939c. It keeps `FROZEN_SUBJECT = None` (line 97) and refuses to record until a confirming review. It already refuses a second variant (lines 22-26 and 246-247).
- [Inferred] These are pre-existing forward-looking sentences outside the round-5 diff. They misstate no authority. They now read as stale, not false in effect: the recorder is not usable until frozen.

Proposed repair: in the next regeneration, write "A recorder, frozen only after a confirming review, takes the chosen row" and "the recorder refuses a second variant act over this manifest".

## No new weakening

[Observed] The round-5 repair changes only prose fields in the policy bytes (`notMapped`, `indeterminate`), identically across the four variants. The rule, the token lists and the reader logic are unchanged, and every probe agrees with the round-5 table for paths that both rounds ran. [Observed] Licences-tree build files (licenses/requirements.txt, robots.txt, CMakeLists.txt) are mapped. The packet claims that the build-file exclusion covers docs and doc only (packet:43, Q3 line 111), so this is consistent, and it is not new.
