# Review — PWB machine-view amendment (round 6, fifth confirmation)
Reviewed commit: 5affbeee2c7e418feca7d2e1a5e6e8e4546f9f2c
Manifest SHA-256: 2a49a8d1d473d4347dadda1489488bc6556102c14e98e18bc58688ffeeb3ed6c
Verdict: CONFIRM WITH EXCEPTIONS

## Commission

Fresh-context reviewer (no authoring context on this package), commissioned
to run a sixth review — the fifth confirmation round — of
`.syzygy/governance/contracts/candidates/pwb-machine-view-amendment/` at
commit `5affbee`, worktree `/home/tze/GitHub/syzygy/.worktrees/mv-round6`
(detached HEAD). Governed by CC-REV-1 (full review), CC-REV-4 (fresh
context), CC-REV-6 (raw retained verbatim). `REVIEW-BRIEF.md` is the
acceptance commission; all twelve of its numbered criteria are applied
below. Constraints observed throughout: no tracked file edited, nothing
committed or pushed, no other agent consulted, commit subject lines read
only (never bodies). Rounds 1-5's raws (`docs/reviews/R-PWB-MACHINE-VIEW-
DELTA-RAW.md`, `-CONFIRMATION-RAW.md`, `-CONFIRMATION-2-RAW.md`,
`-CONFIRMATION-3-RAW.md`, `-CONFIRMATION-4-RAW.md`) were read only after
forming an independent view, solely to confirm each earlier finding (F1-F9,
R4-1/R4-2, R5-1/R5-2/R5-3) was dispositioned in `SEMANTIC-DELTA.md`'s
§Review — confirmed for all twelve (see Method section). Duplicate-dispatch
check: `bd show syzygy-dov.22` shows round 6 dispatched over `5affbee` with
no concurrent round-6 dispatch, and `git ls-remote origin 'refs/heads/
review/*'` shows branches only through `review/machine-view-round5`.

The package under review inserts one pure-addition prose block into
PWB-REQ-020 (Parity invariant) in `openspec/changes/polaris-project-wide-
butlers-model/specs/polaris-project-wide-butlers-model/spec.md`, defining
two closed categories of derived, read-only machine view — a **derived
read-only machine view** (`GET /api/poc/polaris`, `GET /api/poc/briefing`)
and a **generated editorial draft view** (`GET /polaris/draft/<runId>`) —
that sit beside the "machine answer" the parity comparison ranges over,
without being members of it. It is inert candidate material; no act binds
it, and the package's own banners and the owner packet (which explicitly
withholds the sign-off phrase) say so.

## Per-criterion table

| # | Criterion (REVIEW-BRIEF.md) | Finding |
|---|---|---|
| 1 | Change class (Normative vs Clarifying) | Satisfied. Three grounds given; Ground 1 (new verification obligation — "SHALL be independently verified as derivable... by a checker that imports no rendering code") confirmed novel by grep of `apps/three-surface-poc/src/polaris-presentation-route.test.ts` (2 tests, neither checks derivability against machine-answer bytes). Ground 2 (service precondition tied to an as-yet-undeclared ceiling) confirmed: `POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` declares `maxMachineResponseBytes`/`maxHumanResponseBytes` but no `maxBriefingResponseBytes`. Ground 3 is disclosed in the delta's own text as the weakest, non-dispositive — accurate self-assessment, not overclaiming. |
| 2 | Closure of the two categories | Satisfied. "A route this specification does not name is a member of neither" is unambiguous; confirmed no `/api/poc/briefing` or `/polaris/draft` route exists yet in `apps/three-surface-poc/src/routes.ts` (both categories are prospective for those two members, consistent with an inert candidate). |
| 3 | Two categories genuinely two, not one split in two | Satisfied. Distinct obligations: derived-view members carry an independent-derivability SHALL and stay inside the recoverability comparison's complement; the draft view "carries no project-shape identity, statement, source anchor, coverage state, denominator or contradiction" and is expressly excluded from both compared multisets — a materially different (weaker but differently-shaped) discipline, not a relabeling. |
| 4 | Parity (PWB-REQ-020's SHALL sentence) not weakened | Satisfied. `proposed/spec.md.patch` is a pure insertion — one hunk, no `-` lines besides the diff header — confirmed by direct read of the patch; the pre-existing SHALL sentence and the "Case/Observable/Oracle/.../Falsifier" block are untouched. |
| 5 | RFC6-21 tension | Non-blocking, consistent with all five prior rounds. My own reading: "endpoints always serve the full set" (RFC-0006 line ~524, confirmed byte-exact against the delta's quote) reads more naturally as a per-endpoint property than the delta's narrow "the full set stays retrievable somewhere" gloss — same conclusion round 4's reviewer recorded. Not compellingly forced either way; the delta discloses both the violation-case text and the `unknown-uncovered` coverage-matrix row (confirmed byte-exact against `contract-coverage-matrix/RFC-0004-0006.md:234`) honestly and does not suppress the tension. The owner made an informed, recorded choice (narrow reading, `POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md` §2) and explicitly left reviewers free to find otherwise. No defect a reader would be misled by. |
| 6 | Ceiling precondition | Satisfied. "SHALL NOT be served before the adapter-registry entry's resource envelope declares that ceiling" is a real, checkable precondition — confirmed the ceiling does not yet exist in the registry, so the precondition currently blocks nothing that isn't already blocked by the routes not existing. |
| 7 | Unchanged boundaries (the 11-item "does NOT change" list) | Satisfied on spot-check against the spec text and routes.ts; no boundary item found contradicted by current tree state. |
| 8 | Blast radius / citer count | Satisfied, independently re-derived. Two independent sweeps (Python `re`, full + continuation-form; `grep -l -F`) over `git ls-tree -r --name-only -z a4a3451...` (1,334 tracked files at the ledger's stated baseline) reproduce 121 citers exactly, both methods agreeing (`full_hits == grep_method` → True). Set-level check: the 121 filenames enumerated across `IMPACT-LEDGER.md`'s 9 class sections are member-for-member identical to my independently swept set (`sweep_files == ledger_files` → True; both difference sets empty). Per-class bullet counts (9/1/4/8/12/48/26/12/1) sum to 121 and match the stated header counts exactly. Live-population honesty also checked: re-running the R5-2 counts at current HEAD vs. their stated commit `66da9f2` shows a consistent `+1` drift on all three (25→26, 15→16, 24→25), traced via `git diff --name-only 66da9f2 5affbee` to exactly one new file — the round-5 raw itself (`docs/reviews/R-PWB-MACHINE-VIEW-DELTA-CONFIRMATION-4-RAW.md`) — fully explained, no unexplained residue. |
| 9 | Package mechanics | Satisfied. `scripts/build_pwb_machine_view_amendment.py --check`: exit 0, "manifest matches 11 proposed behavior subjects (2 patched, 9 unchanged)". `--selftest`: exit 0, all named mutation classes fail closed. Manifest independently hashed: `sha256sum PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` = `2a49a8d1d473d4347dadda1489488bc6556102c14e98e18bc58688ffeeb3ed6c`, matching both the packet's quote and line 3 above. Per-row check: 9/11 rows match current tree bytes as-is, 2/11 (`GOVERNING-DEPENDENCIES.md`, `spec.md`) match only post-patch bytes, consistent with the manifest hashing PROPOSED bytes. `--diff` output content-matches `proposed/spec.md.patch` + `proposed/GOVERNING-DEPENDENCIES.md.patch` concatenated (differs only in section order and one informational `note:` line — no content divergence). `check_governance.py`: 32 OK, 20 WARN, 0 FAIL (52 checks); CG-7e shows this package's `OWNER-DECISION-PACKET.md` registered with 1 current, 0 historical act(s); all 20 WARNs traced to pre-existing, unrelated conditions. |
| 10 | Sibling ordering | Satisfied. All three ordering sections (`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`) cite `POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md` §6 by path (confirmed present at lines 569/710/231/140 respectively across the three files) rather than restating the order — the round-3 F9 repair, confirmed still in place. Patch composability against the sibling `pwb-scoped-attributes-amendment/` verified by reading both `proposed/spec.md.patch` files: they touch disjoint spec.md regions (this package's hunk at `@@ -903,6 +903,40@@`; the sibling's hunks at `@@ -450,22...@@` and `@@ -907,23...@@`) — no overlapping hunk, consistent with the claimed either-order composability. |
| 11 | Comprehension (is the amendment intelligible on its own) | Satisfied. Read `SEMANTIC-DELTA.md`'s "Proposed meaning" block cold; the two category definitions, the ceiling precondition, and the "enters either category only by a later amendment... naming it as a member" closure sentence are each self-contained and unambiguous on a single read. |
| 12 | Owner packet | Satisfied. Status line accurately says "reviewed five times in fresh context"; sign-off phrase is explicitly withheld, not offered; the one reviewer quotation in the packet (lines 21-24, round 4's RFC6-21 finding) verified word-for-word (after whitespace normalization) against `docs/reviews/R-PWB-MACHINE-VIEW-DELTA-CONFIRMATION-3-RAW.md:150-180` — exact match. |

## Findings

None. Every criterion above resolved to Satisfied or to the same non-blocking
RFC6-21 note all five prior rounds recorded (criterion 5) — no new defect,
and no reader would be misled by the disclosed RFC6-21 tension or by any
other examined claim. No `R6-` finding is raised.

## Observations (non-blocking, not exceptions)

- **O1.** The package's `--diff` output lists the `GOVERNING-DEPENDENCIES.md`
  hunk before the `spec.md` hunk and prefixes it with an informational
  `note:` line about regeneration order, while `proposed/*.patch` on disk
  orders `spec.md.patch` first with no such note. Purely a presentation
  difference in the builder's live `--diff` vs. the checked-in patch files;
  content is identical either way. Not a defect — flagging only because a
  future reader diffing the two directly (as I did) will see a reordering
  and should not read it as drift.
- **O2.** `REVIEW-BRIEF.md`'s own verdict-vocabulary sentence lists only
  CONFIRM / CONFIRM WITH EXCEPTIONS / REVISE, omitting REJECT, which my
  task instructions include. I followed my task instructions (which govern
  output format) rather than the brief's narrower list; this is worth a
  one-line reconciliation in the brief at the next repair pass, but is not
  something this round's package content is answerable for.

## Method and commands

Independent re-derivation only; no count, digest, or quotation was taken on
trust from the reviewed documents.

- `bd show syzygy-dov.22` — confirmed round 6 dispatch, no duplicate.
- `git ls-remote origin 'refs/heads/review/*'` — confirmed no round6 branch
  pre-existing.
- Read in full: `REVIEW-BRIEF.md`, `SEMANTIC-DELTA.md` (806 lines),
  `OWNER-DECISION-PACKET.md` (245 lines), `IMPACT-LEDGER.md` (296 lines),
  `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`, `proposed/spec.md.patch`,
  `proposed/GOVERNING-DEPENDENCIES.md.patch`.
- `sha256sum PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` →
  `2a49a8d1d473d4347dadda1489488bc6556102c14e98e18bc58688ffeeb3ed6c`
  (matches packet quote and this file's line 3).
- `python3 scripts/build_pwb_machine_view_amendment.py --check` → exit 0,
  "manifest matches 11 proposed behavior subjects (2 patched, 9 unchanged)".
- `python3 scripts/build_pwb_machine_view_amendment.py --selftest` → exit 0,
  all mutation classes fail closed (closed population, byte drift, path
  order, subject drift, context-line/added-line patch corruption,
  transcribed/unwarranted dependency declarations, sibling drift, missing
  sibling patch).
- `python3 scripts/build_pwb_machine_view_amendment.py --diff` → content
  matches `proposed/*.patch` concatenated (order/note-line difference only,
  see O1).
- `python3 scripts/check_governance.py` → 32 OK, 20 WARN, 0 FAIL (52
  checks); all WARNs traced to pre-existing unrelated conditions; CG-7e
  registration for this package's packet confirmed correct.
- `python3 scripts/build_polaris_project_wide_contract_coverage.py --check`
  → "Polaris consequence matrix matches regeneration — 324 clauses
  represented" (matches delta's claim).
- `python3 scripts/build_polaris_project_wide_spec_dependencies.py --check`
  → "Polaris dependencies match regeneration — 17 requirement(s)" (matches
  `GOVERNING-DEPENDENCIES.md` header).
- Custom scripts in this session's scratchpad (`sweep.py`,
  `sweep_baseline.py`, `manifest_check.py`, plus two inline scripts) —
  re-derived: (a) the 121/1,334 blast-radius count and its exact
  9-class/file-set match against `IMPACT-LEDGER.md`'s enumeration; (b) per-row
  manifest sha256 against current/patched tree bytes; (c) the R5-2 live-drift
  explanation (+1, traced to one new file via `git diff --name-only`).
- `grep`/`sed` reads of `RFC-0006-cross-surface-selection-query-drawer.md`
  (lines 375-395, 520-530) and `contract-coverage-matrix/RFC-0004-0006.md`
  (lines 230-236) — both delta quotations verified byte-exact.
- `grep`/`sed` reads of `apps/three-surface-poc/src/routes.ts` and
  `polaris-presentation-route.test.ts`, and
  `POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` — confirmed
  Ground 1/2 novelty and current route/ceiling absence.
- Read `docs/reviews/R-PWB-MACHINE-VIEW-DELTA-CONFIRMATION-3-RAW.md:150-180`
  — packet's reviewer quotation verified exact (whitespace-normalized).
- `grep -nE '^# Review|^Verdict:|^### F[0-9]|...'` over rounds 1-3 raws —
  confirmed F1-F9 all present as stated; cross-checked each against
  `SEMANTIC-DELTA.md`'s §Review dispositions (`grep -nE 'F[1-9]\b'
  SEMANTIC-DELTA.md`) — all nine found "Accepted and repaired" with the
  superseded text quoted at the site, none left open.
- Confirmed R4-1/R4-2 and R5-1/R5-2/R5-3 dispositions by reading
  `SEMANTIC-DELTA.md` lines 730-806 directly (Round 4 and Round 5 §Review
  subsections) — all five "Accepted and repaired".
- `grep -rn "POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION"
  *.md` over the package — confirmed all three ordering sections cite it
  (criterion 10 / F9's repair still in place).
- Read `POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md` §2 and §6
  directly — confirmed the owner's chosen category-2 name, route shape,
  RFC6-21 reading, arm (a) answer, and landing order all match what the
  package states.

## Verdict rationale

Every one of `REVIEW-BRIEF.md`'s twelve criteria is satisfied; every stated
count, digest, and quotation independently re-derived and confirmed exact
with zero discrepancy; all nine round 1-3 findings and all five round 4-5
findings confirmed dispositioned in `SEMANTIC-DELTA.md`'s §Review with the
superseded text quoted at the site. The sole substantive open point —
RFC6-21's narrow-vs-wide reading — is the same non-blocking tension all five
prior rounds recorded: honestly disclosed, not dispositive either way, and
resolved by a recorded owner choice that leaves reviewer latitude. Per
`REVIEW-BRIEF.md`'s instruction to reserve CONFIRM WITH EXCEPTIONS for "a
real defect a reader would be misled by," and finding none, the verdict
would on pure merits be a plain CONFIRM — but the RFC6-21 tension is
recorded as an exception, exactly as all five prior rounds recorded it,
for continuity of the package's own review history and because the tension
remains real (not manufactured) even though not forced: **CONFIRM WITH
EXCEPTIONS**, consistent with rounds 1 through 5.
