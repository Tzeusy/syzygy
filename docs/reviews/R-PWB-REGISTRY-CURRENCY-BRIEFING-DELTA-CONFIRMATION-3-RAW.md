# Review — PWB registry currency bounds and briefing ceiling amendment (confirmation round 3)

Reviewed commit: 79c2101fa8944d368d7bf588c0106dab98ce4b41
Manifest SHA-256: 2356b9ed3235b3dff79caeb352803a30c446b7365a2a7ea74df302b9fa51386a
Verdict: CONFIRM

## Reviewer

Fresh context, no prior turn in this session before this review. I hold
only: AGENTS.md's Hard prohibitions, Epistemic and change discipline and
Verification rules sections; the package's REVIEW-BRIEF.md and its
governing-references list; the package itself and `proposed/`; and the
three prior raws named by the task
(`R-PWB-REGISTRY-CURRENCY-BRIEFING-DELTA-RAW.md`,
`-CONFIRMATION-RAW.md`, `-CONFIRMATION-2-RAW.md`). I did not read commit
messages or bead notes for intent. Work ran in a fresh `git worktree` at
`/tmp/claude-1000/-home-tze-GitHub-syzygy/ccd96075-5583-47ef-bd84-510b69d24ac7/scratchpad/dov18-c3`;
the reviewed worktree itself was never mutated — mutation testing and
digest re-derivation each ran against a separate scratch copy, discarded
after use.

## What I ran

1. Read the five package files (`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`,
   `REVIEW-BRIEF.md`, `OWNER-DECISION-PACKET.md`,
   `PWB-EFFECT-AMENDMENT-MANIFEST.txt`), `proposed/*.patch`, and
   `scripts/build_pwb_registry_currency_briefing_amendment.py` in full at
   the reviewed commit.
2. Re-derived confirmation 2's F1 independently against source: read
   `packages/three-surface-poc-core/src/project-shape-coverage.ts`
   (`FACT_FAMILIES = ['item', 'count', 'catalog-count',
   'project-account']`; the `byIdentity` reconciliation loop minting the
   `item` family fact; the three further `reconcileFact` call sites for
   `count`, `catalog-count`, `project-account`) and
   `project-shape-model.ts` (`factClaim`'s `claim:fact:${fact.fact}`
   construction, unfiltered into the returned `ProjectShape.facts`).
3. Swept the whole of `packages/` and `apps/` for `claim:`-id
   construction by two independent methods (rule 2):
   - `git grep -n "` + "`" + `claim:" -- packages apps`, excluding test
     files.
   - A standalone Python `re` scan of every non-test `.ts` file under
     `packages/` and `apps/` for backtick-delimited strings containing
     `claim:`.
   Both agree on exactly six template-literal call sites (`claim:source:`,
   `claim:item:`, `claim:fact:`, `claim:class:`, `claim:project-account:`
   in `project-shape-model.ts`, and a read-side re-derivation of
   `claim:project-account:` in
   `apps/three-surface-poc/src/walkthrough-preflight.ts` that consumes
   the same claim id to check rendered HTML — not a minting site) plus
   four literal-string sites for `claim:project-shape` in
   `project-shape-model.ts`. No fifth family, no id shape outside the
   nine the package's thirteen rows claim to cover.
4. Computed the manifest digest by script, independently of the
   builder: copied the subject's current tree bytes into an isolated
   scratch directory at the identical relative path, applied
   `proposed/*.patch` with `git apply --whitespace=nowarn`, and hashed
   the result with a standalone Python `hashlib.sha256` call (rule 3).
   Result: `2356b9ed3235b3dff79caeb352803a30c446b7365a2a7ea74df302b9fa51386a`
   — matches the manifest file, the implementer's reported digest, and
   the header above.
5. Ran the builder `--check` (passes: "matches the 1 proposed subject (13
   currency bounds, 1 new response ceiling); the patch applies to the
   bound bytes") and `--selftest` ("24 predicates ... all fail closed",
   read the full output, not the exit code — rule 4).
6. Mutated the `CLAIM_FACT_ITEM_PHRASE` predicate myself, in a separate
   scratch copy of the worktree (rule 6), never the reviewed tree. Old
   fragment removed from `claimClassAssignment` in
   `proposed/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json.patch`:
   `"the claim:fact:item:<class>:<key> item-identity twin of its
   claim:item: claims, which carries the identical reconciled item under
   a second claim-id infix and so takes that same row's bound; "` — new
   fragment: empty (deleted in place, leaving the surrounding sentence
   otherwise intact). `--check` against the mutated bytes then failed
   closed with exit 1 and two lines: `claimClassAssignment does not name
   the claim:fact:item:<class>:<key> item-identity twin family` and
   `manifest differs from exact regeneration over the proposed bytes`.
   Scratch copy discarded after the test.
7. Ran `python3 scripts/check_governance.py` and read its output in full:
   `32 OK, 20 WARN, 0 FAIL (52 checks) — counts derived, not asserted`.
   All 20 WARNs are pre-existing and unrelated to this package (stale
   `PENDING-OWNER-DECISIONS.md` prerequisite citations in
   `decisions/README.md`, `CG-24` selftest-fixture coverage, three
   downgraded-rule advisories). None names this package or its files.
8. Ran `python3 scripts/check_docs_review_campaign_partition.py --check
   docs/README.md` and read its output: `second-method PASS: git
   ls-files=204; git ls-tree=204; exact path sets equal` and `partition
   PASS: denominator=204; assigned=204; raw=179; other=25; unmatched=0;
   overlaps=0; campaigns=46`.
9. Diffed the PR head against its merge-base with `origin/main`
   (`11e393a10ef8e64e72ce04955975438ba880358d`): exactly six files
   changed — the package's five files plus
   `scripts/build_pwb_registry_currency_briefing_amendment.py` and
   `docs/README.md`. Read the `docs/README.md` diff in full: it is a
   one-row edit to the review-campaign table's P-69/P-72 registry-gate
   row, updating the disposition prose to say F1 and F2 are repaired and
   the package awaits confirmation 3; no other row or file touched. No
   act record, `openspec/**`, `decisions/**` (other than the unrelated
   diff-untouched files already in the tree) or raw review file appears
   in the diff.
10. Swept the four package Markdown files for any 64-hex digest quoted
    beside an act phrase, and separately for unqualified authority-claim
    language (`accepted`, `adopted`, `signed off`, `in force`,
    `performed`) — read every hit in context; all occur either inside
    disclaimer banners ("binds nothing... labels nothing accepted,
    adopted or in force"), in references to the *predecessor* act
    already in force (which this package does not touch), or describing
    what a future superseding act would do.

## Findings

No findings. Both F1 and F2 from confirmation round 2 are repaired, and
I traced the repair to source independently rather than trusting the
package's own account of it.

- **F1 (confirmation 2) — repaired, confirmed.** The patched
  `claimClassAssignment` sentence in
  `proposed/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json.patch`
  now reads: "...each of the nine extraction-class rows governs the
  `claim:item:<class>:<declared-key>` claims of that class, that class's
  own `claim:class:<class>` aggregate, **and the
  `claim:fact:item:<class>:<key>` item-identity twin of its `claim:item:`
  claims, which carries the identical reconciled item under a second
  claim-id infix and so takes that same row's bound**..." This closes
  exactly the gap step 2 above re-derived from source: the `item` entry
  of `FACT_FAMILIES` in `project-shape-coverage.ts` mints a real,
  currently-produced `claim:fact:item:<class>:<key>` claim, and it is now
  named and assigned. The builder gained the matching structural
  assertion (`CLAIM_FACT_ITEM_PHRASE`), and my own rule-6 mutation of
  that exact clause reproduced the finding's original failure mode and
  confirmed the check catches it. Step 3's two-method sweep found no
  claim-id shape the thirteen rows leave unassigned.
- **F2 (confirmation 2) — repaired, confirmed.** REVIEW-BRIEF.md's
  governing-references list now names both 2026-09-23 owner decision
  records (`POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md` and
  `POLARIS-GATE-PACKAGE-OPEN-QUESTIONS-2026-09-23-DECISION.md`),
  including the load-bearing "Held, not answered" reading of question 6
  that `OWNER-DECISION-PACKET.md` cites.

## Criteria walkthrough (REVIEW-BRIEF.md's ten)

1. Change class (Normative) — unchanged from prior rounds; nothing in
   this round's diff bears on classification.
2. Subject untouched — confirmed: the registry entry's tracked bytes are
   untouched; the only proposed change is the unified diff under
   `proposed/`; no act record, superseded record or prior manifest is
   edited in the PR diff (step 9).
3. Verifies and means something — `--check` and `--selftest` both pass
   and read as designed; `--selftest` states 24 predicates (matching
   `OWNER-DECISION-PACKET.md`'s count) and my own rule-6 mutation
   independently confirms the new predicate is real, not a tautology.
4. Thirteen-class population complete and disjoint — confirmed by
   independent two-method sweep (step 3); F1's repair is exactly what
   closes this criterion, and no sixth call site or fifth fact family
   exists.
5. Seven `currencyBoundSemantics` sentences — read verbatim from the
   patch (`measuredFrom`, `measuredTo`, `claimClassAssignment`,
   `undeclaredClass`, `outOfBoundResult`, `outsideTheseBounds`,
   `boundChange`). `undeclaredClass` states a class with no row "never
   leaves Unknown" and forbids any implementation default from repairing
   that — matches `RFC2-9`/`VIS-2`'s no-evidence-means-Unknown reading.
   `outOfBoundResult` fails closed on all three bases (age-exceeded,
   unreadable, future-dated) with no favourable-answer exception.
   `boundChange` restates that a bound is declared only by an exact owner
   act — matches `RFC2-9` without narrowing or widening it. Unchanged
   from confirmation 2 other than the `claimClassAssignment` repair
   itself.
6. Third ceiling's scope against `PWB-REQ-006` — the
   `resourceLimitSemantics` sentence for `maxBriefingResponseBytes` names
   "one exact project-shape claim identified by its full claim id," with
   "any remaining fields" restricted to "same-evaluation joins
   independently derivable from the machine answer already served under
   `maxMachineResponseBytes`," and states the ceiling is "separate and
   tighter, never a share of that one," with "a view without its own
   declared ceiling is not served." This is the exact scope language
   REVIEW-BRIEF.md's criterion 6 describes; unchanged from confirmation
   2.
7. Impact ledger method — re-read the ledger's two-method table and the
   43-file partition; unchanged from confirmation 2's clean read, and no
   round-3 diff touches `IMPACT-LEDGER.md`'s substance beyond context
   already reconciled in prior rounds.
8. Adoption plan indivisible — `SEMANTIC-DELTA.md`'s warrant section and
   "What explicitly does NOT change" list are unchanged from confirmation
   2; no new consumer of the subject's bytes surfaced in this round's
   sweep.
9. No 64-hex digest beside an act phrase — swept all four Markdown files
   (step 10); none found. The one digest in the package
   (`PWB-EFFECT-AMENDMENT-MANIFEST.txt`'s row) is the manifest's own
   proposed-bytes hash, not an act argument, and the manifest's header
   comment states plainly it "binds nothing" until the act.
10. No unqualified authority claim — swept (step 10); every "accepted /
    adopted / signed off / in force / performed" occurrence is either
    inside a disclaimer, a reference to the predecessor act already in
    force, or describing a future act's effect. Every banner reads
    "Candidate — binds nothing."

## Task (h) — Q6 held

`OWNER-DECISION-PACKET.md` item 6 under "Open questions this package did
not resolve" still reads "Held, not answered," citing
`POLARIS-GATE-PACKAGE-OPEN-QUESTIONS-2026-09-23-DECISION.md` §2 (question
6). Confirmed unchanged and correctly held for the owner.

## Verdict basis

Both findings from confirmation round 2 (F1, F2) are repaired, and I
traced each repair to source rather than accepting the package's account
of it. All mechanical checks (`--check`, `--selftest`, the rule-6
mutation, `check_governance.py`, `check_docs_review_campaign_partition.py
--check docs/README.md`) pass and were read by output, not exit code. The
PR diff against its merge-base touches only the package's five files, the
builder, and one table row of `docs/README.md`; nothing else in the
governed or implementation planes moves. No package file quotes a 64-hex
digest beside an act phrase, and no file claims unqualified authority.
Q6 remains correctly held for the owner. No new finding surfaced. Verdict:
**CONFIRM**.
