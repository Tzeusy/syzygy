# R-EGRESS-V2-3 — egress record v2 confirmation, round 3 (delta)
Reviewed commit: 905899957a056a4c64cd24b575be07f70540fada
Manifest SHA-256: 15c3c304de06bc5d9e9af10f872bfe481cded3c1c16605bf8b4b6ace8d9f1881
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context governance reviewer. No provider was called and no external repository body was read. Nothing was pushed, commented or edited in tracked files.
Worktree: detached at 90589995 in a scratch directory, `npm ci` first (rc 0). Every mutant was restored with `git checkout`, and `--check` reported current again after each. The worktree was removed at the end.
Paths are relative to `.syzygy/governance/contracts/candidates/` unless they start with `scripts/` or `packages/`. PKT = `public-egress-v2/OWNER-DECISION-PACKET.md`; REC = `public-egress-v2/instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md`; TPL2 = `public-egress-v2/templates/EGRESS-CONSENT-TEMPLATE-V2.md`; TPL1 = `public-repo-admission/templates/EGRESS-CONSENT-TEMPLATE.md`.

## Delta scope

- [Observed] d2f9ab90 is an ancestor of the head. `git diff --stat d2f9ab90..HEAD` lists 10 files: PKT, the manifest, REVIEW-BRIEF.md, ROUND-2-DISPOSITIONS.md (new), REC, the round-2 raw (new), TPL2, v2.json, `scripts/build_public_egress_v2.py` and `scripts/record_public_repo_admission_acts.py`.
- [Observed] There is no diff to `scripts/derive_generator_sent_text.mjs` or under `public-repo-admission/`. The v1 bytes are unchanged.
- [Observed] Only one of the two named recorders exists at the head: `record_public_repo_admission_acts.py`. The row-8 recorder is still absent. ROUND-2-DISPOSITIONS.md:55-56 defers the coupling test to it.

## Digests and runs (rule 3, scripted; rule 4, output read)

- `sha256sum public-egress-v2/PUBLIC-EGRESS-V2-MANIFEST.txt` = 15c3c304de06bc5d9e9af10f872bfe481cded3c1c16605bf8b4b6ace8d9f1881. This equals `--manifest-digest` (rc 0) and the expected value.
- Python `hashlib.sha256` over REC = 2a97b98f0e707b39ee06bdc8f9e0d1f8cd351bddd2a09312c9c4a7302b2bbf3e. This equals the manifest row and `--digests` (rc 0).
- `build_public_egress_v2.py --check` → "public egress v2: current" (rc 0). `--ready` → "public egress v2: ready" (rc 0). `--selftest` → "selftest: 23 checks held" (rc 0; it was 22 at round 2). The "unknown mode --bogus" line is the selftest's own expected refusal.
- `record_public_repo_admission_acts.py --selftest` → "36 of 36 predicates held" (rc 0).
- `build_public_repo_admission.py --check` → "public-repo admission instances: current" (rc 0).
- `python3 scripts/check_governance.py` → "32 OK, 21 WARN, 0 FAIL (53 checks)".

## Round-2 notes against the bytes

- **N-1, volume: repaired as to the defaults. The new sentence about bounds is unsupported; see N-1 below.**
  - [Observed] PKT:21-27 now says "This record caps no volume" and names the numbers as code defaults.
  - Against `packages/polaris-generation-core/src/discovery.ts:36-37` `DEFAULT_DISCOVERY_BUDGET`, each default holds:
    - excerpt 1,500 = `maxExcerptChars` (applied at :235);
    - 40 files per map call = `maxGroupBlobs`, sliced at :150-152;
    - 40 map calls = `maxMapCalls` (:231);
    - 400 claims of 400 characters = `maxReduceClaims` and `maxClaimChars` (:247, :263).
  - [Inferred, code read] Under the defaults the reduce input holds at most 400 claims. `perGroup` is at most floor(400 / groups) when there are 400 groups or fewer, and when there are more than 400 groups only the 40 or fewer mapped groups carry claims, one each.
  - [Observed] "A larger discovery budget stays inside it" matches the validation at :180-182, which sets lower bounds only.
  - "Short claims" is gone.
- **N-2: repaired.** [Observed] REVIEW-BRIEF.md:30-33 names both digests by the command that prints each. This head carries the `--manifest-digest` value.
- **N-3: repaired.**
  - [Observed] The pin is now the 4-tuple of counts plus `diffSha256` (v2.json:18-22). `stale()` compares all four (`scripts/build_public_egress_v2.py:195-197`). An independent `diff -U0` TPL1→TPL2 gives 8 hunks, 13 removed and 60 added, equal to the pin.
  - Round 2's M3 re-run: TPL2 "no route byte is permitted" → "any route byte is permitted", with the line count unchanged (157 → 157).
    - `--check` before `--write`: STALE on REC, TPL2 and the manifest (rc 1).
    - `--write` (rc 0). It leaves v2.json untouched, so it cannot launder the pin.
    - `--check` after `--write`: "STALE …TEMPLATE-V2.md" (rc 1).
    - `--digests`: "refusing: stale" (rc 1).
    - `--ready` still says "ready", because it checks only the stage list. That is unchanged since round 2.
  - The new selftest check is itself guarded. Reducing the `stale()` comparison to the first three fields makes `--selftest` raise "same-count template edit not caught".
- **N-4: repaired.**
  - [Observed] The selftest now calls `do_record` (`scripts/record_public_repo_admission_acts.py:645-654`). It asserts rc 1, the reason text and no record written.
  - Mutant: `:438` `if superseded_by_later_version(...)` → `if False and …`. The selftest gives "FAIL do_record refuses the first version's egress act at the call site, writing nothing" and "35 of 36" (rc 1).
  - The docstring is restored. `import tempfile` now follows it (:495-496).
- **N-5: repaired.**
  - [Observed] REC:152-153 and TPL2 (same hunk) read "`cache_control` on the fixed system prefix and on the generator's system prompt and input".
  - This matches the #255 entry's `requestBytes`: `runtimeFixed[0]` "system[0]: … (cache_control ephemeral)", and `generatorBuilt[0]` and `[1]` "with cache_control ephemeral attached".
  - The edit sits inside an added hunk. The counts are unchanged, and only the diff digest moved.
- **N-6: repaired.** [Observed] PKT:134-142 states the by-kind delegation, its bound and the need for a separate owner act for any successor entry. This agrees with REC:131-132 (fields outside the table are refused) and REC:188-191 (the absolute ban).

## Nothing weakened

[Observed] The only REC change is the N-5 widening of the description, which brings it into line with the entry. The entries govern (REC:146). Everything else in the diff is:

- an added pin and an added selftest check (22 → 23);
- an added recorder predicate (35 → 36);
- packet narrowing: "sendable" became "egress-eligible", with the read gated on a later screening scope.

No round-2-confirmed predicate or wording was removed.

## README wording (criterion 4)

[Observed] PKT:28-34 matches #266's SEMANTIC-DELTA.md:47-49 and :68. SEMANTIC-DELTA:47-49 says "defines no class … prose stays indeterminate until a later policy version maps it". SEMANTIC-DELTA:68 says "indeterminate (excluded from reading and egress)".

It also matches RFC5-14 as patched by #257 (`rfc5-project-documentation-class/SEMANTIC-DELTA.md:61-62`: "A consent record that does not list `project-documentation` does not permit its egress").

The row numbers match the sitting packet's table: row 1 is the screening scope and row 7 is the RFC5-14 class. One exception is listed as N-2.

## Findings

**N-1 — The repaired volume paragraph states as fact a bound that no code enforces on discovery egress.** (note; fix before the packet is offered)

PKT:25-27: "How much leaves is bounded by the run budget the trigger supplies, which the owner sets and which this act does not (the `dossier-units-v1` proposal under "Proposed run budget" in the sitting packet)."

- [Observed] At the head and at origin/main 7fa64394, `git grep discoverAndSelect` finds no caller outside `discovery.ts`, its test and `index.ts`.
- [Observed] The only wired caller is on unmerged origin/agent/dossier-engine-6 (c9d61c5e), in `apps/three-surface-poc/src/polaris-generation/dossier-trigger.ts`:
  - :124 passes `DEFAULT_DISCOVERY_BUDGET`;
  - :122-123 gives a `permitted` port that checks only the egress record;
  - the `GenerationBudget` at :95 goes to the reader and pipeline config, not to discovery.
- [Observed] The cited source is unmerged too: origin/governance/admission-sitting-packet b9ef900a, OWNER-SITTING-PACKET.md:203-219. It is not on main or this branch. It labels those values "[Inferred] … unmeasured … They will live in code under syzygy-bc0g", and bead syzygy-bc0g is OPEN.

Today the effective bound is the code defaults, which this packet now correctly says the record does not carry. The intended run-budget bound is [Inferred] and not yet in code.

Suggested repair: label the sentence and say it is not yet in code. For example: "[Inferred] intended to be bounded by the run budget …, which is not yet in code (syzygy-bc0g); until it is, the discovery defaults are the only limit."

**N-2 — "design documents" is not a member that RFC5-14's `project-documentation` row names, and #266 groups design documents with the governance-text question.** (note)

- PKT:28 lists "README files, guides, tutorials and design documents".
- The class row (`rfc5-project-documentation-class/SEMANTIC-DELTA.md:47`) lists:
  - README;
  - user and developer guides;
  - tutorials;
  - how-to and overview documents;
  - changelogs and release notes;
  - contribution guides;
  - licence and notice files.

  It adds "the declared policy decides each file". Its bullet (:53-55) makes spec-like text `governance-text`.
- #266 SEMANTIC-DELTA:63-69 speaks of "specification and design documents" as unmapped governance-text candidates, which stay indeterminate.
- The phrase was present at round 2 as well. It now sits under the reworded bullet.

Suggested repair: name the class's own members ("README, guides, tutorials, overview documents, changelogs, contribution guides and licence files, as the declared policy places each file"). The sitting packet's own row-7 consequence names LICENSE.
