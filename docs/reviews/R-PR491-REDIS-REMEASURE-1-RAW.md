Reviewer: rev-pr491-666b43

Bound to: PR #491 head `8f0a558d7e632fed4a15b1b1e5f69b1949b48b1f`. Script sha256 `6a52c982702ff4bb252ec762907fd2ffb902d387ae1830ebcb58e21ad4a807d7`, the same bytes at `1bb9b24e` and `8f0a558d`.

**What I ran (read-only)**
- `--selftest`: all cases pass.
- `--mutants`: all 7 mutants killed, exit 1 each.
- Measured the run twice at clean `8f0a558d`: once with the default headline, once with `--headline-revision 2`.
- `check_governance.py`: 32 OK, 21 WARN, 0 FAIL.
- `check_evidence_currency.py`: the new record is current, 1/1 in-tree digest.

**Second methods**
- Before and after the measurement I took a metadata snapshot (size, mtime, ctime, mode) of all 52 entries in the run directory and of the clone's `.git`. Both diffs are empty.
- In Python I re-summed each `byPath` table against `withheld`, `admitted + withheld` against `total`, the by-design split, and the non-passing rows (taken from the verdict's row counts under the `derivedBlocking` rule). Every figure agrees.
- I hashed `run.json`, the v3 policy at `d3a9b753` and the v4 policy on disk. All three match the record.
- I read no Redis bytes outside the script.

**Findings**

1. [Observed] Important. The script bypasses the expired-deadline refusal.
   - It calls `openRun`, gets `stage: 'deadline'`, and records it (`scripts/redis_screening_remeasure.mjs:270-272`).
   - It then builds an `OpenedRun`-shaped object by hand, without `declared`, `deadlineEnds` or `revision`, and calls `buildFidelityPacket` with it, which reads Redis bodies (`:309-311`).
   - `review-packet` would stop at that point (`packages/polaris-dossier/src/review.ts:314-315`).
   - The spec says: "Syzygy SHALL enforce the limits that bind its own steps: it SHALL refuse … any step after the deadline" (`openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md:23`).
   - The script's header (`:13-14`) and the PR body disclose this. They argue the script is "no dossier step". [Inferred] Whether a screening-only re-measure counts as a "step" is a scope question. No act or direction is cited for it. The bead only says "Runs only through the existing public-target read gate".
   - So "the same code path as `review-packet`" holds only from `buildFidelityPacket` onward.
   - The record's method line (`docs/evidence/redis-screening-v4-remeasure-2026-10-21.json:57`) says the outcome "is recorded beside it". It does not say the refusal was overridden.
   - What is clean: the read gate `reverifyPinnedRevision` passed. There is no model, provider or process spawn on the call path (grep of review, reverify, gate-sources, screen, inventory, session-statement and git-object-reader). Nothing was written to the run directory.

2. [Observed] Important. The rebuilt packet digests cannot be reproduced (rules 3 and 11).
   - `rebuiltV3.packetSha256` and `rebuiltV4.packetSha256` change on every run (JSON `:197, :258, :491, :552, :776, :840`). My re-run produced six different values.
   - Cause: `fidelityCriteria(runDir)` puts the run path into the packet bytes (`review.ts:98`), and the script points it at a fresh `mkdtemp` view each time (`script:198, :301`).
   - Fix: drop these fields, or label them as tied to a temporary path. Today they look like digests a reader can re-check.

3. [Observed] Note. All four headline numbers reproduce exactly. My re-run differs from the committed record only in `measuredAt`, the commit, `treeClean` and the item-2 digests (diff with jq).
   - 140 → 100 withheld of 233 cited spans.
   - README 40 of 41 admitted. The one still withheld is `span-48`, line 1. Withheld lines are 1–2, detector `credential-assignment`.
   - 96 of the 100 are in the 7 by-design files. Those 7 files match the v4 packet's "What stays withheld" section (`OWNER-DECISION-PACKET.md:88-103`).
   - 30 of the 101 non-passing rows now cite only admitted spans, and 71 still cite a withheld span.
   - The v3 rebuild equals the retained packet `613695de…` span by span, comparing whole JSON objects including text.
   - [Unknown] The v4 figures have no method independent of `buildFidelityPacket` and the script. The v3 oracle checks only the baseline.

4. [Observed] Note. The committed record was measured on a dirty tree at a commit other than the head: `treeClean: false` at `1bb9b24e` (JSON `:6-7`).
   - [Inferred] The cause is the `> docs/evidence/…json` redirect, which truncates the tracked file before the script checks status.
   - It is harmless here: same script bytes, and the clean re-run matches. But the record does not explain it.

5. [Observed] Note. The invocation is not recorded.
   - The committed headline is revision 2. A default run headlines revision 3 (244 cited spans, 145 → 105 withheld, 73 still / 28 freed rows), because the script defaults to the latest revision (`script:419`).
   - `headline.latestDraftRevision: 3` discloses that the headline is not the latest, but the `--headline-revision 2` argument and the `SYZYGY_REMEASURE_ROOT` override (`:36`) are not recorded.

6. [Observed] Important. Mutant coverage is incomplete (rule 6).
   - The 7 named predicates each have a mutant that fails `--selftest`.
   - The logic behind the "30 of 101" claim has no selftest or mutant: the row join, the non-passing row rule, `stillOnlyOutsideByDesign`, and the `blockCites`/`entryCites` lookups (`script:336-370`).
   - `cited()` silently drops any citation whose path and line range is not among the packet's spans (`:338`). Such a row could be counted as "every cited span admitted".
   - [Unknown] Whether any such citation exists in this run.
   - My independent re-count confirms the 101 total but not the 30/71 split.

7. [Observed] Note. The record contains no Redis text or secret.
   - I enumerated all 105 string values: 25 are 40- or 64-hex digests or object ids, and the other 80 are Redis paths, enums, policy and consent identifiers, Syzygy method prose, and the script's own mutant fragments.
   - No key is anything but an identifier.
   - The README entry carries line numbers, the object id and the content digest only.
   - The `bodyLeak` guard catches only exact admitted span texts of 12 or more characters. Substrings are not checked. It is backstop-only.

8. [Observed] Note. Two wording issues:
   - The header says "the only Git reads are the pinned reader's, after the gate" (`:26`). The script also runs `git rev-parse`/`status` before the gate and `git log`/`show` of Syzygy's own history (`:252, :284-285`).
   - The method line says redacted spans are split by `spanTouchesWithheld`'s reading (JSON `:60`). The script uses its own copy, `redactedCause` (`:58-60`). It is semantically identical to `secret-redaction.ts:263-265`, but it is not the same code.

9. [Inferred] Note. The readiness statement (JSON `:1081`) is mostly well hedged.
   - "Readiness is not reached by the screening change alone" is a prediction. A fresh reviewer could judge mixed rows from their admitted spans.
   - "would still lack bytes for them" overstates for the rows among the 71 that also cite admitted spans. The record does not count those mixed rows.
   - Suggested wording: "cannot be shown reached", and count the mixed rows.
   - The statement does label itself Inferred, defers to a new review session for the 30, and proposes no relaxation.

Verdict: REVISE