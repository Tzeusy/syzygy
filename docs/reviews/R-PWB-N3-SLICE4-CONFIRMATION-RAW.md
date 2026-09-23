# R-PWB-N3-SLICE4 confirmation — PR #96 at ecd6623

Verdict: CONFIRM WITH EXCEPTIONS

## Scope

PR #96, head `ecd66239934d859f5f2b005b22c5579c13a831f2` (starts `ecd6623`, as
expected), reviewed in worktree
`/tmp/claude-1000/-home-tze-GitHub-syzygy/ccd96075-5583-47ef-bd84-510b69d24ac7/scratchpad/conf96`.
Repair commits under review: `25874a4390dfa2c15b18f3b3b0b2be14c189fab7..ecd6623`
(one commit, `ecd6623 fix(pwb): repair N3 slice 4 review findings (REVISE)`),
responding to `docs/reviews/R-PWB-N3-SLICE4-REVIEW-RAW.md` (verdict REVISE,
read verbatim from `origin/main` — not present on the local `main` I started
from; `git fetch origin` picked it up at `d86d587`). Repair diff:
```
docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md                     |  14 ++
docs/evidence/pwb-polaris-population-backfill-2026-09-23.json  | 139 ++
packages/three-surface-poc-core/src/evidence-population.test.ts|  17 ++
3 files changed, 170 insertions(+)
```

## Finding 1 (blocking): population backfill for the 10 pre-existing records

**Sweep re-run, this session, at the pre-repair base `25874a4`:**
`git ls-tree -r --name-only 25874a4 -- docs/evidence` piped through a
per-file `grep -qF '"polaris-direct.html"'` on the blob content →
**11 matches**, 10 after excluding `pwb-m1-polaris-lane-a-population-2026-09-23.json`
(this PR's own already-populated record). Matches the record's `sweep` block
exactly, including the file list.

**No `population` key in any of the 10:** `python3`, `'population' in
json.load(open(f))` → `False` for all 10, matching the record's
`confirmedNoPopulationKey` claim.

**`butlersRevision` traced to each record's own bytes:** for every one of
the 10 entries I independently confirmed the stated value (7 full 40-char
hashes, 1 twelve-char prefix `2e3bac97790b`, and 2 explicit Unknowns) is
either literally present in that record's bytes or, for the two Unknowns
(`polaris-m16-renderer-visual-system-funnel-2026-09-17.json`,
`pwb-laneb-strict-scope-estimate-2026-09-14.json`), that no Butlers revision
appears anywhere in the record — the only `butler`-matching substrings in
those two files are "no Butlers body was read" and "plusButlersRepairsMax"
respectively, exactly as the backfill record states. All three 40-hex hashes
are valid-length git revisions.

**Every Unknown carries a reason, nothing is zero or guessed:** verified
programmatically over all 10 records × 3 fields — every dict-valued field
has `state: "unknown"` and a non-empty `reason`; every non-dict value is a
non-empty string. No zero stands in for "not measured" (VIS-2).

**No retained capture bytes — independent sha256 sweep:** collected all
64-hex digests named across the 10 records (97 distinct, matching the
record), sha256'd every `git ls-files -z`-tracked file (1,464 in this
worktree — 1 more than the record's stated 1,463, because that count was
taken before the backfill record itself existed as a tracked file; the
delta is exactly the one new file the repair adds) and cross-checked.
**24 matches, all outside capture bytes** — independently re-derived by
category: 19 `docs/reviews/*-RAW.md`, **3** `docs/design/*.md`
(`POLARIS-M9-ONE-IDENTITY-FUNNEL.md`, `POLARIS-M13-NAVIGATION-SCALE-FUNNEL.md`,
`POLARIS-M14-PROVENANCE-DEPTH-FUNNEL.md`), 2 `.ts` sources
(`page-shell.ts`, `polaris-narrative.ts`). **Minor inaccuracy in the record**:
its own `itemClaimIdSweep.matchesAreNote` says "two docs/design/*.md files";
it is three. The total (24), the conclusion (no capture bytes retained,
Unknown is correct per VIS-2) and the substance are unaffected — this is a
cosmetic miscount in descriptive prose, not a wrong result. Non-blocking but
worth a follow-up correction.

**No pre-existing record edited:** `git diff 25874a4 ecd6623 --stat` lists
only the 3 files above; none of the 10 `docs/evidence/*.json` paths appear.

**Digest-binding disclosure (rule 10), independently re-run:** for each of
the 10 records I sha256'd current bytes and searched every
`docs/reviews/*-RAW.md` for a 64-hex digest within two lines of the record's
basename. Result: **6 of 10** (`polaris-m10-machine-contract-funnel`,
`polaris-m13-navigation-scale-funnel`, `polaris-m4-owner-loop-funnel`,
`polaris-m5-agent-briefing-funnel`, `polaris-m9-one-identity-funnel`,
`pwb-m1-polaris-lane-a-measurement`) have one or more nearby digest
quotations in raws, **none of which match current bytes** (all retired by
later edits); the other 4 have none. This matches the record's
`priorReviewDigestConfirmations` claim exactly.

**Truncated digest check:** the only truncated (non-64-hex) digest-shaped
string quoted in the new record is the 12-char `2e3bac97790b` in the
`polaris-m5-agent-briefing-funnel` entry, quoted verbatim as a Butlers git
revision prefix from that record's own `capture.provenance` field — not a
signed act digest. `check_governance.py`'s CG-15 ("truncated digest quotes
still prefix a current argument") scans specifically for truncation markers
against `ACT_DIGEST_COPY_FILES`-registered act digests; it is unrelated to
git-commit prefixes and passed clean (15 quotations examined, 0 findings).
Confirmed fine per AGENTS.md's own distinction between a Butlers revision
prefix and a signed act digest.

**Verdict on finding 1: fixed**, modulo the one cosmetic miscount noted
above.

## Finding 2 (disclosure): note on POLARIS-M1-PAGE-SIZE-FUNNEL.md

Pre-edit bytes at `25874a4`: `git show 25874a4:docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md
| sha256sum` → `d38df844f0f27d14d29475c59486e59f7cd66b0bf9de62eb2d885941939b36af`
— matches the digest the backfill record itself quotes for this file's
pre-edit state.

- Grepped that exact digest across `.syzygy/`, `docs/`, `scripts/` and
  `openspec/` (broader than the record's own claimed scope of "docs, .syzygy
  and scripts"): **0 citers** anywhere except the new backfill record's own
  self-disclosure sentence.
- Grepped `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` and
  `ACCEPTANCE-ACT-RECORD.md` for the bare path: **not present in either.**
- Grepped every `*MANIFEST*` file under `.syzygy/` for the path: **0 hits.**
- Grepped every `docs/reviews/*-RAW.md` for the path: found citations in
  `R-PWB-SCOPED-ATTRIBUTES-DELTA-{,2,3,4}-RAW.md`, `R-POLARIS-M7-GENERATION-LOOP-FUNNEL{,-2}-RAW.md`,
  `R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL-2-RAW.md`, `R-POLARIS-M9-ONE-IDENTITY-FUNNEL-2-RAW.md` —
  mostly line-number/content citations, but
  `R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL-2-RAW.md` quotes a **full sha256
  digest** for this exact path: "`docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md`
  — 20579 bytes, sha256 89e0e7af90c979ef497422acd75527bb33131f0736ad9669ada11cb54d78eb01".
  This digest does **not** match the pre-repair-of-this-PR state
  (`d38df844...`) either — it is an even older byte-state (the file has
  clearly been edited many times across its life; the other raws quote
  different line ranges for the same headings). Per rule 10 and its own
  worked example in AGENTS.md (the `GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-SEMANTIC-DELTA.md`
  case), a stale review confirmation of a long-superseded byte-state does
  not lock a candidate, non-act-bound file against further edits — it
  confirms history, and the current bytes carry no confirmation. Since this
  confirmation was already retired well before `25874a4` (i.e. before this
  PR existed), the repair did not retire a live review; nothing this PR did
  newly voided an active confirmation.
- The file is corroborated as non-act-bound by its own governing decision,
  `.syzygy/governance/decisions/POLARIS-M1-PAGE-SIZE-OWNER-RULING-DECISION.md`,
  which states explicitly: "Nothing here is an act: no digest is bound... It
  is a plain owner direction."
- The edit itself is strictly additive (append-only, a new dated section at
  end of file per `git diff 25874a4 ecd6623 -- docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md`);
  no existing sentence is touched, and the new note self-labels "candidate
  design material like the rest of this document and binds nothing by
  itself."

**Verdict on finding 2: fixed, not a bound or live-review-confirmed file;
editing it is not a REVISE.** (The one stale, already-long-retired
confirmation found above is disclosed here for completeness, not as a
defect — it predates this repair and this PR did not touch the sentences
that digest was ever confirmed against.)

## Finding 3 (test gap): decodeHtmlAttr `&amp;` mutant

Reviewed the new test (`decodes an entity-escaped and a plain rendering of
the same id to one distinct value`, asserting `renderedClaimIdCount(...) === 1`
over a two-occurrence fixture, one `&amp;`-escaped and one plain) — this is
exactly the fixture shape the prior review asked for.

Applied the same mutant myself: replaced
`.replace(/&amp;/g, '&');` with `.replace(/&gt;/g, '>');` (dropping the
`&amp;` decode) in `packages/three-surface-poc-core/src/evidence-population.ts`.
`npx vitest run packages/three-surface-poc-core/src/evidence-population.test.ts`
→ **8 passed, 1 failed** — exactly the new test:
`AssertionError: expected 2 to be 1`. All other 8 tests still passed
(confirming the mutant is narrowly targeted). Reverted with
`git checkout --`; re-ran → **9/9 passed**, `git status --short` on the file
clean (byte-identical restore).

Expected values in the test file are hand-typed literals throughout
(`toBe(1)`, `toBe(2)`, `toBe(0)`, `.toEqual({...})` with literal fields),
never imported from the module under test — matches the repo's rule.

**Verdict on finding 3: fixed.**

## Cross-cutting checks

- **model.ts, polaris.ts, routes.ts untouched:** `git diff origin/main...ecd6623 --stat`
  over the whole PR lists 6 files total (the 3 from the original PR plus the
  3 repair files); none of the three named files appear.
- **PR body and bead comment tallies match the record:** `gh pr view 96`
  body and `bd show syzygy-u05.3`'s 2026-09-23 00:58 comment both state
  "Ten pre-existing... butlersRevision stated for 8/10... Unknown for 2/10...
  itemCount/claimIdCount: Unknown for 10/10... 24 matches, none the measured
  capture bytes... 6/10 were digest-confirmed by an earlier review... a later
  edit retired." Every one of these numbers matches my independent
  re-derivation above.
- **PWB-REQ-014 authority sweep:** `npx vitest run apps/three-surface-poc/src/polaris-authority-sweep.test.ts`
  → 4/4 passed. Read the actual test predicate
  (`apps/three-surface-poc/src/polaris-authority-sweep.test.ts:117-137`): it
  flags a line matching `^\s*["']?(source|authority|warrants?|primary|evidence|provenance|cites?|anchor)["']?\s*[:=]`
  *and* mentioning the Polaris surface on the same line, exempting retained
  `-RAW.md` reviews. This is narrower than a naive substring match (e.g.
  `"sources"` or `"evidenceCurrency"` keys, which appear in the sibling
  `pwb-m1-polaris-lane-a-population-2026-09-23.json` record from the
  original PR, do **not** trip it) — confirmed by direct reading, not
  inference, so the green result is trustworthy.
- **`npx tsc -b packages/three-surface-poc-core packages/polaris-generation-core`**
  → clean (exit 0).
- **`npx tsc --noEmit -p apps/three-surface-poc`** → clean (exit 0), but
  only *after* first running `npx tsc -b --force packages/cap1-core
  packages/cap1-daemon packages/three-surface-poc-core apps/three-surface-poc`
  (i.e. `npm run build:poc`) — a fresh worktree's app typecheck otherwise
  reports 24 phantom `Cannot find module '@syzygy/cap1-daemon'`/implicit-any
  errors, exactly the known AGENTS.md gotcha ("App typecheck... resolves
  core through `dist` declarations: run `tsc -b` first... or the app reports
  phantom errors"). Once built, both requested commands are clean.
- **Full `npm test`:** 135 passed | 1 failed | 3 skipped (139 files);
  1813 passed | 1 failed | 3 skipped (1817 tests). The one failure is
  `production-reobserve.test.ts`'s "keeps served bytes and asOf stable..."
  timing out at 5000ms under full-suite load. Re-run in isolation
  (`npx vitest run apps/three-surface-poc/src/production-reobserve.test.ts`)
  → **4/4 passed**, confirming the known non-reproducing load-timeout
  artifact, not a regression.
- **`python3 scripts/check_governance.py`** → **32 OK, 20 WARN, 0 FAIL (52
  checks)**, matching the PR's claim exactly; all WARNs pre-existing/advisory
  (CG-19b, CG-22b, CG-23, CG-24, CG-27 items, none touching this diff's
  files).
- **`python3 scripts/check_evidence_currency.py`** → exit 0. Read-only
  report over 114 tracked `docs/evidence/*.json` files (113 before this PR's
  first commit added one, 114 after the repair's backfill record adds a
  second); neither new record (`pwb-m1-polaris-lane-a-population-2026-09-23.json`,
  `pwb-polaris-population-backfill-2026-09-23.json`) appears in the
  drift/actionable listing, consistent with both classifying `unknown`
  (scratch-file capture subjects, never committed) as claimed.

## Overall assessment

All three review findings are genuinely repaired: the population gap is now
disclosed record-by-record with honest, reason-bearing Unknowns and a
correctly-scoped, independently reproducible sha256 sweep (VIS-2 respected
throughout, no zeros standing in for "not measured"); the measurement-script
gap is disclosed in a non-bound, append-only note on a confirmed-unbound
candidate design document; and the rule-6 mutant the prior review found now
fails as expected and reverts cleanly. None of the ten pre-existing evidence
records, and none of `model.ts`/`polaris.ts`/`routes.ts`, were touched. Every
requested validation command is clean or matches its known, previously
disclosed flake.

The **CONFIRM WITH EXCEPTIONS** verdict, rather than a clean CONFIRM, is for
one thing only, non-blocking: the new backfill record's own
`itemClaimIdSweep.matchesAreNote` miscounts its digest-match categories
("two docs/design/*.md files" where the independently re-run sweep finds
three) — the total (24), the conclusion (no capture bytes retained), and
every other figure in the record are correct; only this one descriptive
sub-count is off by one. Recommend a follow-up one-line correction to that
sentence; it does not warrant blocking the PR.
