# Review R-PR493-BEAD-TITLE-WITHHOLDING
Reviewed commit: 0b29573a0d760dfe2af4422a7db97321466f6a22
Verdict: CONFIRM WITH EXCEPTIONS

rev-pr493-k7q2vx

Review of PR #493 at head `0b29573a0d760dfe2af4422a7db97321466f6a22` (code subject `fdb71f71`, base `29e036f4`). I made no edits, git writes, gh writes or bd writes. Everything I ran was in scratch clones under `/tmp/claude-1000/-home-tze-GitHub-syzygy/49123ca9-8529-48cf-8e46-2ac45afbd82a/scratchpad/`.

**What I ran at the PR head** [Observed]
- Full vitest with every `dist/` removed: 4,783 passed, 5 skipped, 0 failed, of 4,788. The POC core and app suites alone: 2,042 passed, 4 skipped.
- `npm run typecheck`: exit 0.
- `check_governance.py`: 32 OK, 21 WARN, 0 FAIL over 53 checks.
- All four results match the PR's claims.

---

**1. The premise holds: no signed clause obliges serving or using a title.** [Observed] Severity: Note.
- POC-REQ-040 (`openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md:792-793`): "with every rendered item placed by its observed status and carrying its identifier".
- POC-REQ-010 (`spec.md:282-283`): "a sampled item's served status and timestamps match the database".
- POC-REQ-014 (`spec.md:454-455`): "No served item's `governedBy` SHALL name an identifier taken from its title". This is a prohibition. Its scope (`spec.md:463-464`) says "This requirement admits no work-item column and no other input".
- The POC-REQ-014 Case (`spec.md:476-478`) still applies: "an injected work-item read holding one item whose title names a requirement identifier". The test injects that row and the observer ignores the title.
- The P-97 and P-100 sign-off records add no title obligation. A sweep of `proposal.md`, `design.md` and `CONTRACT-COVERAGE.md` finds title only at `CONTRACT-COVERAGE.md:140` and `:185` and `proposal.md:90`. None of those obliges anything.
- Residual: the Scenario at `spec.md:529` ("WHEN a served item's title reads 'Implement POC-REQ-010'") now describes a state the POC cannot reach. It is satisfied only through the Case's injected-read form. Its wording should ride the next POC amendment.

**2. Fail closed: the title is never read.** [Observed] Severity: Note.
- The SELECT at `packages/three-surface-poc-core/src/work-items.ts:177-178` names exactly eight columns, with no title and no `*`. `RawRow` (lines 152-161) has no title field. The item literal (lines 256-265) copies only named fields.
- Every non-test `bd` call in `packages/` and `apps/` was swept (4 found):
  - `work-items.ts:142`
  - `materialization.ts:217`: its query at `:281` is `SELECT id … AND external_ref = …`.
  - `materialization.ts:230`: `bd create` writes Syzygy's own packet title. Its stdout is parsed for `id` only (`:396`).
  - `materialization.ts:456`: `bd close`, whose output is discarded.
- There is no other `FROM issues` query. Nothing reads `.beads` or the JSONL export. Persisted state (the materialization and test-artifact records) holds no title.
- No retained rendered title exists among the 2,940 tracked files (checked in raw and JSON-escaped form). The one hit is this PR's own record, which holds fixture titles only.
- The tests' fake `runQuery` returns a title whatever the SQL asks for, so "read but never copied" is exercised too.

**3. The VIS-2 disclosure is never blank or silent, and parity holds per tuple.** [Observed] Severity: Note.
- The machine channel carries `titles` on both the observed path and the observed-empty path (`work-items.ts:231`, `:275`). Its twin subject is pushed at `model.ts:592`.
- The card mark (`apps/three-surface-poc/src/trajectory.ts:166-169`) and the board notice (`:172-179`) both resolve through `unknownSubject`. That helper throws when the twin is missing (`unknown-marker.ts:37`), so a dropped twin fails loudly (mutant M08).
- On the 250-card synthetic I reproduced, there are 251 rendered tuples under `region:work-item-titles`. All carry `excluded-content`, all 250 card spans match the literal exactly, and they map to one machine subject. Parity holds per tuple, not by counting ids.
- The route is RFC2-24 row 7 (`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md:136`): "`excluded-content` | Secret-detection policy excluded the content, or it was unclassifiable (fails closed, SEC-5) | Policy change by the owner, or accept the exclusion".
- That satisfies SEC-5 (`.syzygy/governance/doctrine/security.md:125-127`): "a matching exclusion is rendered".
- When the work-item region is Unknown, it covers the titles too. That is correct.

**4. Tests and mutants: independent literals, an honest count, 11 of 11 replayed.** [Observed] Severity: Note.
- Expected values are typed literals and are not imported from the module under test:
  - the `WITHHELD` object and the column list in `work-items.test.ts:166-212`;
  - the basis sentence and route in `trajectory.test.ts:98-118`;
  - the checker-owned `FIXTURE_TITLES` in `governing-intent-sweep.test.ts:34`.
- The count +5 ~9 is honest:
  - New (5): three `work-items` cases, one Trajectory case and the "a served title" falsifier.
  - Changed (9): two block-provenance cases; three governing-intent cases (the counterexample and two falsifiers); three unknown-sweep denominator cases and the reach list.
  - The changed assertions are stronger, not weaker. The page-wide `not.toContain('POC-REQ-010')` replaces the old `.title` path exemption.
  - The trajectory-projection fixture also changed, but that is an input, not a case.
- Mutant replay used the record's own `old`/`new` fragments and command:
  - All 11 killed and the baseline survives (99 of 99).
  - Each mutated sha256 equals the record, the per-mutant fail counts match exactly, and the tree was clean afterwards.
  - M04 (30 TypeErrors) and M08 (16 "no machine Unknown" errors) die mostly by crash, but each also has a real assertion kill.
- Rule 11 holds:
  - The record names the commit, tree, `patchSha256` and 10 files with gitBlob and sha256.
  - I re-derived all of them at the head. The patch digest equals `git diff 29e036f4 fdb71f71`.
- Gaps: the differential harness and the battery log are not retained; the record gives only the log's digest. The differential cannot be re-run from the record alone. I re-implemented it and got identical bytes.

**5. Output change: Polaris and Orrery are identical, and the Trajectory growth is far under the ceiling.** [Observed] for the fixtures, [Inferred] for live. Severity: Note.
- I independently re-rendered the plain and synthetic-252 models at base and head. All 8 byte sizes match the record (for example Trajectory 435,827 → 510,627, and `/api/poc` 400,508 → 382,288).
- Polaris and Orrery are identical after normalization. The 2 hex tokens that differ per page also differ between two renders of the base, so they are run-to-run noise.
- The synthetic's 250 cards is the maximum selection (`NON_CLOSED_LIMIT` 200 + `RECENT_CLOSED_WINDOW` 50, `model.ts:49-50`).
- The human ceiling is 2,097,152 (`project-shape-observation.ts:81`).
- The last live `/trajectory` measurement was 443,755 bytes via tailnet (`docs/evidence/p100-governing-intent-restoration-2026-10-21.json`). Adding 74,800 bounds the live page at about 518.6 KB, roughly 25% of the ceiling. [Inferred] Live titles are longer than the fixture titles, so the live delta should be smaller still. No live run was made.
- Design note: the same ~300-byte sentence repeats on every card. That is 250 identical screen-reader announcements beside a board notice that already says it once. Also, `data-parity-field="work-item-title"` now labels a disclosure rather than a title. Both are optional follow-ups.

**6. The shared-model change is bounded, but it collides with the P-115 candidate fixtures.** [Observed] Severity: Important (coordination; not a defect in this PR).
- The change itself is bounded:
  - removes `WorkItemFact.title` and `TrajectoryLaneItem.title`;
  - adds `WorkItemsObserved.titles`;
  - adds one Unknown subject.
- No other open PR changes POC core code: #487 is candidate-only, #489 and #492 are docs, #491 is evidence. On code, WIP-one is not breached.
- The conflict: #487 (P-115, head `be5dfbde`) has literal fixtures that encode served titles and the old card.
  - `compatibility/literal-fixtures/expected-effective-facts.json:3,16` holds `"item:fixture-a/title": "Alpha work"`.
  - `human-body-A.html:12` holds `<a data-parity-field="work-item-title" …>Alpha work</a><code data-parity-field="work-item-id">`.
  - `LITERAL-FACTS.json` counts `"work-item-title": 2`.
  - Its `OWNER-DECISION-PACKET.md` says human text "remain[s] as adopted".
- Once #493 merges, that literal proof describes a wire and card the code no longer produces. If it is offered as-is, it puts a served title back into signed material. Route this to the `syzygy-318o` lane before the P-115 offer.
- Separately, main has moved to `fdc866af`, which touches `apps/three-surface-poc/src/sync-child-process-guard.test.ts`. Under rule 7 the battery is valid only at the PR's commits, so rebase and re-run before merging.

**7a. The stale RFC4-15 row is correctly left unedited, but nothing tracks it.** [Observed] Severity: Note.
- `openspec/changes/three-surface-poc-experience/CONTRACT-COVERAGE.md:140` says "the work-item title, the only free text the POC reads". It is now false.
- The file's current sha256 is a row of `three-surface-poc-vocabulary-epistemic-amendment/THREE-SURFACE-POC-VOCABULARY-EPISTEMIC-AMENDMENT-MANIFEST.txt`, so it is bound and must not be edited. Leaving it was correct.
- A sweep of all 711 beads finds 0 for "RFC4-15" or "only free text". File a bead so this row and the Scenario wording from finding 1 ride the next POC amendment.

**7b. `issue_type` (and `id`) are correctly out of scope, but need a tracked follow-up.** [Observed] Severity: Note.
- `issue_type` is checked only as a string (`work-items.ts:242`) and served raw (`:259`). [Inferred] Beads allows custom types, so it is a possible free-text carrier.
- `id`, now the card's display name, is checked only by its prefix (`:249`).
- The ruling's boundary excludes these fields: "Explicit exclusions: other free-text bead fields, other Butlers tables" (`.syzygy/local/owner-questionnaire-2026-10-20.md:276`). So leaving them out of this PR is correct.
- But the bead's acceptance criterion asks to "check that no other work-item free-text column is read". That is now answered by an open question, not "none", and no bead tracks it.

**7c. The ruling is recorded only locally: fine for merge, not for closing the bead.** [Observed] Severity: Important (blocks closing `syzygy-jytt`, not merging).
- `.syzygy/local/` is gitignored (`.gitignore:11`).
- At its own item, the local questionnaire still reads "Adversarial review: Pending" and "Status: Pending owner response" (line 288). Only its summary table (line 369) says Agreed / A.
- The only shared record is the 2026-10-20 bead comment.
- The code is lawful on SEC-5 alone. The packet itself says "the interim fail-closed handling needs no owner act" (line 255). So keeping the ruling out of the PR's diff is acceptable.
- However, the code comments and the evidence record's `authority.ownerAnswer` cite an owner answer whose durable home is untracked. The bead's acceptance criterion, "Owner ruling recorded (register row or act)", is unmet, and no follow-up bead exists. `syzygy-jytt` must not close until a register row lands.

Verdict: CONFIRM WITH EXCEPTIONS