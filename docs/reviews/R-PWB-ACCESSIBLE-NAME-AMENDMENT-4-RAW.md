# R-PWB-ACCESSIBLE-NAME-AMENDMENT-4 — regeneration-confirmation review, PWB accessible-name amendment (PWB-REQ-016, P-99), round 4
Reviewed commit: 83b29c96775d9c2215292fa41e1599080f0b802c
Manifest SHA-256: f794d73536f55b916fa09bff8504cecf7b9b67d225c0cc0916211184cbb95490
Verdict: CONFIRM WITH EXCEPTIONS

Package: `.syzygy/governance/contracts/candidates/pwb-accessible-name-amendment/`
(manifest `PWB-ACCESSIBLE-NAME-AMENDMENT-MANIFEST.txt`). Brief:
`pwb-opening-index-amendment/REVIEW-BRIEF.md`, §"Round 4" governing. Under
its "Subject, C", this round confirms the regeneration over the P-86
sign-off. It does not re-judge the prose or requirement text that round 3
cleared (`docs/reviews/R-PWB-ACCESSIBLE-NAME-AMENDMENT-3-RAW.md`, `CONFIRM
WITH EXCEPTIONS`, at `d6b3784f`). Round 3's ten notes are recorded in
`ROUND-3-DISPOSITIONS.md` and are not re-raised here. Finding 3 applies to
both packages and is repeated from the A raw.

The head digest is the sha256 of the manifest file's bytes at the reviewed
commit. I computed it twice: `git show 83b29c96…:<path> | sha256sum`, and a
Python `hashlib` pass over the file in a clean clone. Both gave the same
value.

## Mechanics run (fresh clone at the reviewed commit)

[Observed] Everything below ran in a fresh `git clone`, checked out
detached at `83b29c96775d9c2215292fa41e1599080f0b802c`. I read each check's
output, not only its exit code. `git status --short` in the clone was empty
after the runs.

- `build_pwb_accessible_name_amendment.py --check`: passes. Output: "11
  proposed subjects (2 patched); 17 requirements, 58 scenarios; structure,
  regeneration, contract coverage, sibling classification and
  pending-sibling composition (pairwise, and one result in every order)
  verify".
- `build_pwb_accessible_name_amendment.py --selftest`: passes. Output: "27
  structure mutants, … all fail closed on their own predicates".
- `build_pwb_opening_index_amendment.py --check` and `--selftest`: both
  pass. Output: 61 scenarios, 4 position fixtures and 50 structure mutants.
- `build_pwb_release_label_amendment.py --check`: passes. Output: "11
  proposed subjects (7 patched); 17 requirements, 60 scenarios".
- `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".
- `check_spec_reconciliation.py --check`: "7 of 7 predicates without FAIL;
  PASS". R6 warns on the two behaviour-contract pins, as before. The
  current PWB `spec.md` is sha256 `107125b2ca05…`.
- All 15 `scripts/build_pwb_*amendment*.py --check`. The three pending
  builders pass. So do registry-currency-briefing and truth-policy. The ten
  that fail are signed, performed or declined packages. See the A raw for
  the list.

**Spec patch identity.** `proposed/spec.md.patch` at round 3's reviewed
commit (`d6b3784f`) and at this commit has the same sha256
(`6ba8075c8a76…`). `git diff --stat d6b3784f..83b29c96` does not list
it. It is byte-identical, as the dispositions claim.

**What else changed.** `git diff --stat d6b3784f..83b29c96` over the
package directory and `scripts/build_pwb_accessible_name_amendment.py`
lists exactly 3 files:
- the manifest (10 lines);
- `proposed/GOVERNING-DEPENDENCIES.md.patch` (4 lines);
- `ROUND-3-DISPOSITIONS.md`. It is new in the range: it was written after
  round 3, and its §"Regenerated over the P-86 sign-off, 2026-10-14" is
  part of it.

The builder, `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`,
`OWNER-DECISION-PACKET.md`, this package's `REVIEW-BRIEF.md` and
`ROUND-1`/`ROUND-2-DISPOSITIONS.md` are unchanged.

Outside the package, the shared engine changed by 3 lines in `235b71eb`.
The change moved class-granular from pending to performed (finding 3).

**The dependency patch.** Its diff changes exactly one `-` line and one
`+` line, the two `Source:` digest lines:
- base: `48c33c53…` → `107125b2…`;
- proposed: `f6f6bc7d…` → `c3ea81d9…`.

`--check` confirms that the file equals regeneration.

**Manifest rows.** I compared the round-3 manifest with this one row by
row, and the current tree at the two commits file by file:
- exactly 5 rows moved: `CAPABILITY-COVERAGE.md`,
  `GOVERNING-DEPENDENCIES.md`, `design.md`, `proposal.md` and `spec.md`;
- exactly the same 5 PWB files changed in the tree over the range;
- the other 6 rows and the other 6 files are unchanged;
- `git log d6b3784f..83b29c96 -- openspec/changes/polaris-project-wide-butlers-model/`
  lists one commit, `235b71eb` (the P-86 and P-100 sign-off). P-100's
  changes are in the POC change directory only.

**The base change is P-86 alone.** Every one of the 11 rows of the
class-granular manifest at `235b71eb^` hashes the PWB tree at `235b71eb`.
No PWB file changes after that commit.

**Every row hashes the proposed bytes.** By my own script, not the engine,
I copied the PWB change directory at this commit and applied both patches
with plain `git apply`:
- all 11 of the 11 rows hash to the proposed bytes;
- only `GOVERNING-DEPENDENCIES.md` and `spec.md` differ from the tree, so
  the 3 other moved rows equal the signed tree bytes as P-86 left them;
- the text before the requirements and the requirement order are
  identical;
- PWB-REQ-016 is the only changed block;
- `difflib` finds exactly 3 signed lines replaced, the builder's 3;
- the `warrants:` block is identical;
- PWB-REQ-016 goes from 1 scenario to 3, and the proposed spec has 58.

**Composition.** All 6 orders of the three pending spec patches apply
and give 1 result (`4b95e7d4bd64…`).

**Round-3 head.** Round 3's manifest digest `8dfd6d83…` re-derives from the
manifest at `d6b3784f`. The file no longer hashes to it at this commit.
That is the expected consequence the dispositions record.

The regeneration is what the dispositions describe:
- the spec patch is unchanged;
- the dependency patch moves only its digest lines;
- every moved row is explained by the P-86 base change;
- every row hashes the proposed bytes over the signed tree at this commit.

Every finding below is a note.

## Findings

**Finding 1 — The P-86 sign-off made the package's "P-86 pending" sentences false, and the dispositions do not carry that correction** (note)

[Observed] The package prose is unchanged since round 3 and still treats
the class-granular package as pending:
- `SEMANTIC-DELTA.md:205` and `:218` ("stay pending: this one, P-98, P-86
  and P-85");
- `IMPACT-LEDGER.md:21` ("the pending class-granular package"), `:69` and
  `:85` ("composes this package with the three still pending: P-98, P-86
  and P-85");
- `OWNER-DECISION-PACKET.md:132`.

At this commit the builder composes with two pending siblings, not three.
The regeneration did not make these sentences false; the sign-off that
caused it did. So under the brief they are not grounds for `REVISE`.

The cleared-bytes rule keeps the prose unedited. But
`ROUND-3-DISPOSITIONS.md` §"Corrections carried here instead of in the
package" lists only round-state sentences, not these. The same record's
§"Composition at the integration branch" says "all four pending PWB
builders' `--check` pass … class-granular". At this commit class-granular
is not pending and its builder fails post-sign-off.

The correction belongs in the round-4 dispositions record.

**Finding 2 — The byte-identical spec patch now applies by offset** (note)

[Observed] The spec patch's hunk headers are still those of the round-3
base: `@@ -1857,17 …` and `@@ -1876,4 …`. PWB-REQ-016 now begins at line
2008 of the signed `spec.md`, against 1850 at `d6b3784f`, because P-86
added lines above it.

`git apply` places both hunks by context. My independent apply shows the
result is exactly the intended change, and the builder checks
regeneration. So this is cosmetic. Package A's spec patch was rebuilt over
the current `spec.md`; C's was kept byte-identical by design, so that
round 3's reading of it carries.

A sign-off tool that rejects offset hunks would refuse it. [Unknown]
Whether `record_versioned_signoff.py`'s apply path tolerates offsets; I did
not read it. [Inferred] If it applies through the engine's `git apply`
call, as this builder's `--check` does, the patch applies.

**Finding 3 — Composition and sibling state at this commit (applies to both packages)** (note)

[Observed] At `83b29c96` the engine's `PENDING_SIBLINGS` is exactly
accessible-name, opening-index and release-label. All three builders'
`--check` pass, and all 6 application orders of the three spec patches
give one result.

The class-granular builder's `--check` now fails on its own
`CAPABILITY-COVERAGE.md.patch`. That is consistent with P-86 being signed
and applied in `235b71eb`: the other signed siblings' builders fail the
same way. It is not in the round-4 battery.

The engine changed by 3 lines in that sign-off commit. The change moves
class-granular from pending to performed and is no repair.

Re-run each pending builder's `--check` after the next sibling sign-off.
If P-98 or P-85 is signed first, this package is regenerated again, and
its manifest rows for `spec.md` and `GOVERNING-DEPENDENCIES.md`, at
least, move again.
