# Review — PWB registry currency bounds and briefing ceiling amendment (confirmation round)
Reviewed commit: 82cca275273eea0c34bb7e48fcf42269ee4223bb
Manifest SHA-256: 69c5bde8fcbfe81793abec92766ff31a4e1d36779e8e83b52f4ddda9c11e7ecb
Verdict: CONFIRM

Reviewer: fresh-context session. No authoring context; the package, its
prior raw review and the `## Review` disposition table were all read for
the first time this session, in the order `AGENTS.md`, `REVIEW-BRIEF.md`,
the prior raw (`docs/reviews/R-PWB-REGISTRY-CURRENCY-BRIEFING-DELTA-RAW.md`,
named in the task as already confirmed against commit `3030668`), then the
package's own files at the current commit. Commit message bodies were not
read for intent; `git log -1 --format='%H %s'` was used only to identify
the two candidate commits by subject line before checkout. Read-only
throughout the worktree; every mutation ran either through the package's
own `structure_findings`/`selftest` functions invoked directly (no tree
write) or in a scratch copy under the session scratchpad
(`/tmp/claude-1000/-home-tze-GitHub-syzygy/25dc4c66-2fc9-4594-82e1-b88a40232dcc/scratchpad/registry-review-scratch/`),
never in the reviewed worktree. Class: fresh-reader confirmation review of
a normative delta's repairs (CC-REV-4, CC-REV-6), against the five
confirmation criteria supplied by the requesting session, read alongside
`REVIEW-BRIEF.md`'s own ten acceptance criteria.

This is a **confirmation round**: the prior raw (CONFIRM WITH EXCEPTIONS at
commit `3030668`, F1 and F3 revise, F2/F4/F5/F6 note) is bound to bytes the
repairs have since moved (rule 10, stated correctly in `SEMANTIC-DELTA.md`'s
`## Review` section at the current commit). This review checks each
disposition against the repaired bytes rather than re-deriving the whole
package from zero.

---

## What I ran

1. `git fetch origin && git checkout -B review/registry-currency-briefing-confirmation 82cca275273eea0c34bb7e48fcf42269ee4223bb`.
   `git rev-parse HEAD` → `82cca275273eea0c34bb7e48fcf42269ee4223bb`, matching
   the head of `origin/agent/gate-registry-currency-briefing`. `git status
   --porcelain` → empty, before and after every step below.
2. Read `AGENTS.md` in full, then
   `.syzygy/governance/contracts/candidates/pwb-registry-currency-briefing-amendment/REVIEW-BRIEF.md`
   in full, then the prior raw
   (`docs/reviews/R-PWB-REGISTRY-CURRENCY-BRIEFING-DELTA-RAW.md`) in full,
   then `SEMANTIC-DELTA.md`'s `## Review` section (its disposition table
   for F1–F6).
3. `python3 scripts/build_pwb_registry_currency_briefing_amendment.py
   --check` → exit 0: "PWB registry currency-and-briefing amendment
   manifest matches the 1 proposed subject (13 currency bounds, 1 new
   response ceiling); the patch applies to the bound bytes".
4. `--selftest` → exit 0, printed: "selftest: 19 predicates — subject
   drift, patch corruption, manifest digest and path mutation, both
   version bumps, limit semantics, the briefing ceiling's value,
   claim-class population, duplication, row shape and bound value, the
   semantics block's type, keys and empty sentences, entry count and JSON
   validity all fail closed". Matches `OWNER-DECISION-PACKET.md`'s claim
   ("mutates nineteen predicates … the count is the one the command
   prints") exactly.
5. **F1 check (criterion 1).** Read `structure_findings()` (script lines
   131–196) and enumerated every `findings.append(...)`/early-`return`
   call site: 15 distinct assertions (JSON validity; `registryVersion`;
   entry count/shape; `observerVersion`; `resourceLimits`/
   `resourceLimitSemantics` typing; `maxBriefingResponseBytes` positivity;
   a limit missing its semantics sentence; `currencyBounds`
   missing/empty; a duplicated `claimClass`; population/order mismatch; a
   row with unexpected keys; non-positive `maxAgeMs`; `currencyBoundSemantics`
   typing; its key population/order; an empty sentence). Read `selftest()`
   (lines 247–421) end to end and mapped each of its 19 predicates:
   predicates 1–4 exercise `proposed_bytes()`/`verify_manifest()` (subject
   drift, patch corruption, manifest digest mutation, manifest path
   mutation — none of these is a `structure_findings` assertion);
   predicates 5–19 map one-to-one onto all 15 `structure_findings` sites
   (5→observerVersion, 6→limit-without-semantics, 7→population/order via
   a renamed claim class, 8→maxAgeMs positivity, 9→semantics key
   population/order via a renamed key, 10→JSON validity, 11→top-level
   registryVersion, 12→duplicated claimClass, 13→BRIEFING_LIMIT_KEY
   positivity, 14→entry count/shape, 15→resourceLimits typing,
   16→currencyBounds missing/empty, 17→row unexpected keys, 18→
   currencyBoundSemantics typing, 19→empty sentence). Every one of the 15
   assertion sites has a mutating fixture; no predicate is a tautology —
   each asserts `mutant != proposed`/`drifted != current`/`corrupted !=
   original` before checking the mutation is caught, and each fixture
   mutates a real byte sequence or a real parsed-document field, not a
   value that was already going to fail. This matches
   `SEMANTIC-DELTA.md`'s disposition of F1 ("Nine predicates added,
   covering the three the reviewer mutation-tested by hand … and the six
   it identified by inspection … The printed count and both prose copies
   now read nineteen") exactly: 19 − 10 (the prior count) = 9 added, and
   `git diff 3030668 82cca27 -- scripts/build_pwb_registry_currency_briefing_amendment.py`
   shows exactly predicates 11–19 as new code, nothing else touched in the
   function.
6. `--diff` → captured to a scratch file, byte-diffed against
   `proposed/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json.patch`
   on disk → identical.
7. Manifest digest, computed not transcribed (rule 3): built a scratch tree,
   copied the subject's current bytes in, ran `git apply --whitespace=nowarn`
   with the on-disk patch (exit 0), parsed the result as JSON (succeeded),
   then `sha256sum` → `5fbef79751f52f2e6cfbbbaa6e2d33993926627461346246e00a6cace7ac8ae2`.
   Equals the manifest row exactly. `git diff 3030668 82cca27 --
   .../PWB-EFFECT-AMENDMENT-MANIFEST.txt` confirms this is the only line
   that moved, from `dd2773c0…` (the prior raw's cited manifest row) to
   `5fbef797…` — the digest moved with the patch, as `SEMANTIC-DELTA.md`
   claims for F3 ("This changed the patch, so the manifest row was
   regenerated").
8. Swept the package's four Markdown files (`IMPACT-LEDGER.md`,
   `OWNER-DECISION-PACKET.md`, `REVIEW-BRIEF.md`, `SEMANTIC-DELTA.md`) for
   a 64-hex token: `re.findall(r'[0-9a-f]{64}', text)` per file → **0 hits
   in all four** (criterion 2's third clause). `--check` passes (criterion
   2's second clause, "What I ran" #3).
9. **F3 check (criterion 1).** Read the patched `claimClassAssignment`
   sentence in a scratch tree with the current patch applied (same tree as
   #7): "every claim is named by its full claim id, because two
   populations differ only by an infix: … project-fact-declaration
   governs the closed fact families `claim:fact:count:<class>`,
   `claim:fact:catalog-count:<catalog-key>` and
   `claim:fact:project-account:<key>`; project-account-statement governs
   the six statement claims `claim:project-account:<key>`, which carry no
   `fact:` infix and are a different population from the
   `claim:fact:project-account:<key>` family above; …". Names both
   populations by their full claim id, as `SEMANTIC-DELTA.md` claims.
   Cross-checked against `packages/three-surface-poc-core/src/project-shape-model.ts`:
   `factClaim` builds `claim:fact:${fact.fact}` (line 383); `projectAccountOf`
   builds `claim:project-account:${key}` with no `fact:` infix (lines
   430/447). Cross-checked `fact.fact`'s own values against
   `project-shape-coverage.ts:358-360`: `countFact` → `count:<class>`,
   `catalogCountFact` → `catalog-count:<catalog-key>`, `projectAccountFact`
   → `project-account:<key>` — so `factClaim` produces exactly
   `claim:fact:count:<class>`, `claim:fact:catalog-count:<catalog-key>`,
   `claim:fact:project-account:<key>`. All three shapes and the bare
   `claim:project-account:<key>` statement shape match the patched
   sentence's own spelling, word for word. The nine extraction-class rows'
   `claim:item:<class>:<key>` and `claim:class:<class>` shapes
   (`itemClaim` line 375, `classAggregate` line 403) and the
   `claim:source:<path>`/`claim:project-shape` shapes (lines 367, 345/611/658)
   likewise match the sentence's remaining clauses.
10. Confirmed `EXTRACTION_CLASSES` in
    `packages/three-surface-poc-core/src/project-shape-manifest.ts:58-67`
    is the same nine-entry, same-order list as the first nine of the
    script's `CURRENCY_CLASSES` tuple (script lines 67-80).
11. `python3 scripts/check_governance.py` — full output read: **32 OK, 20
    WARN, 0 FAIL (52 checks)**; `grep -c "pwb-registry-currency-briefing"`
    over the output → 0. No WARN or FAIL names this package (criterion 4).
12. Swept the package's four Markdown files for lines over 79 columns
    outside fenced code blocks, then read every hit in context: all are
    Markdown table rows (owner-value tables, the finding-disposition
    table, the governance-authorities table) or single unbreakable
    governed paths inside blockquote banners — none is a reflowed prose
    paragraph, so none exhibits the wrapped-citation defect AGENTS.md
    warns of. Swept for backticked Butlers paths (`grep '`' | grep
    "Butlers"`) → 0 hits. Swept for "in force"/"adopted"/"accepted"/
    "performed"/"signed off" outside references to the predecessor act →
    every hit either disclaims authority explicitly or describes a
    different, already-performed act; no file claims this package's own
    bytes are accepted, adopted, signed off or in force (criterion 4).
13. `git diff 303066819e8f267136425d0de67e48eeac34e731 82cca275273eea0c34bb7e48fcf42269ee4223bb`
    over the package directory, the builder script and `docs/reviews/`:
    read in full. Confirms the repair's blast radius is exactly the six
    files `SEMANTIC-DELTA.md` names, plus the new raw file; no act record,
    no superseded record, no other package's file, and no `openspec/**` or
    implementation file is touched (criterion 4's implicit "no new
    defect" check extended to scope).
14. **F6 check (criterion 3).** Read `OWNER-DECISION-PACKET.md`'s "Open
    questions" item 6 (added since the prior raw): states the risk,
    attributes it to F6, and names the sibling package as its closure
    ("The category belongs to the sibling specification package, which is
    not in the tree; until it lands this stays open"). Re-ran the sweep at
    the current commit: `git grep -n -F -e "derived read-only machine
    view" -e "syzygy-dov.22"` over the whole tree returns hits only in
    `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`, three
    `docs/design/*.md` funnels, one evidence JSON, and this package's own
    files and the prior raw — no directory under
    `.syzygy/governance/contracts/candidates/` names the category. F6 is
    genuinely still open, not merely declared so.
15. Read `SEMANTIC-DELTA.md`'s `## Review` `## Rule 10` paragraph: it
    names commit `3030668` and states the repairs moved the proposed bytes
    and the manifest row, so "the raw's confirmation covers the reviewed
    bytes, not these." Correct: the prior raw's own header names
    `3030668` and a manifest digest (`277a50db…`, the manifest *file's*
    hash at that commit) that no longer matches the current manifest file
    (`69c5bde8…`, computed this session — see header above). The two
    digests differ because the file's payload row changed
    (`dd2773c0…` → `5fbef797…`, "What I ran" #7), which is exactly what
    rule 10 says retires the confirmation.
16. **F5 spot-check.** Read the repaired `OWNER-DECISION-PACKET.md` row for
    `maxBriefingResponseBytes`: "measured the two one-claim briefing
    compositions at 7,076 and 5,150 bytes and recommended 20,480 as
    roughly 2.9x the larger — deliberate headroom, not a tight budget and
    not the measured cost." Cross-checked against
    `docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md:410-436`: the two
    measured totals are 7,076 and 5,150 bytes exactly, and the funnel's
    own text computes "20,480 / 7,076" ≈ 2.9×. The repaired sentence no
    longer conflates the measured cost with the ceiling.
17. Read `IMPACT-LEDGER.md`'s repaired remainder note (F2): "raises the
    denominator by 7 — four Markdown files, one manifest, one patch and
    one builder script." `git diff 3030668 82cca27 --
    .../IMPACT-LEDGER.md` shows this is the only change in the file (the
    43-file partition, the two-method identifier table and the baseline
    commit are all byte-identical to the confirmed version, so they did
    not need re-derivation this round).

---

## Findings

### N1 — note. `--selftest`'s 19-predicate net covers every `structure_findings` assertion exactly, as claimed, but does not extend to `check()`'s three other assertions.

*Anchor:* `scripts/build_pwb_registry_currency_briefing_amendment.py:223-241`
(`check()`) versus `:247-421` (`selftest()`);
`OWNER-DECISION-PACKET.md:232-234` ("`--selftest` mutates nineteen
predicates in turn and requires each to fail closed … it covers every
assertion `structure_findings` makes").

`check()` makes three assertions `structure_findings()` does not:
"proposed/*.patch population is not the single declared subject patch"
(line 227-231), "the proposed patch changes nothing" (line 237), and
"manifest missing" (line 241). None of these has a mutating fixture in
`selftest()`. This is **not** a defect in the repaired claim — the packet's
sentence is scoped to `structure_findings` specifically, and every one of
that function's 15 assertion sites does now have a fixture (see "What I
ran" #5) — but a reader could come away thinking `--selftest`'s coverage is
total over `check()`. *Repair (non-blocking, for a future pass):* either
extend `selftest()` to cover the three `check()`-only assertions, or add
one clause to the packet's sentence naming the boundary explicitly (e.g.
"…covers every assertion `structure_findings` makes; three further
`check()`-only assertions — patch population, no-op patch, missing
manifest — are proven correct by inspection but have no selftest fixture").

### N2 — note. F6 is still genuinely open at this commit, not merely declared so — confirmed by a fresh sweep, not carried forward from the prior review.

*Anchor:* `OWNER-DECISION-PACKET.md`, open question 6; `SEMANTIC-DELTA.md`
`## Review` disposition of F6 ("Open, and stays open… Recorded as a sixth
open question").

Re-running the sibling-package sweep at `82cca27` (rather than trusting the
prior raw's `3030668`-commit result) still finds no directory under
`.syzygy/governance/contracts/candidates/` declaring the "derived
read-only machine view" category; `syzygy-dov.22` and the phrase occur
only in the ruling record, three design funnels, one evidence file, and
this package's own text. `REVIEW-BRIEF.md` criterion 6's answer therefore
still depends entirely on a package that does not exist in the tree. This
is exactly what the disposition claims — recorded here as confirmation
that the claim was re-derived this round, not copied, per rule 9 (an
absence claim needs its own sweep).

---

## Verdict basis

Both revise-class findings from the prior round are repaired at the bytes
named: F1's `--selftest` now has a mutating fixture for all 15
`structure_findings` assertion sites (9 new predicates, exactly as
claimed, mapped one-to-one in "What I ran" #5), and F3's
`claimClassAssignment` sentence now names every population by its full
claim id and states the fact/statement distinction in its own words,
verified word-for-word against `project-shape-model.ts` and
`project-shape-coverage.ts`'s actual `claimId` construction. The two
note-class findings (F2, F5) are repaired as described. F4 is correctly
left unchanged (it was a finding against the review instructions, not the
package). F6 is correctly left open and is still open at this commit,
confirmed by an independent re-sweep rather than trusted from the prior
round.

The manifest digest moved with the patch and re-derives independently to
the exact row on disk; `--check` and `--selftest` both pass and print the
claimed counts; `check_governance.py` runs 0 FAIL with the package
untouched by any finding; no 64-hex token appears in any of the package's
four Markdown files; no repair introduced a banner, label, wrap, Butlers-
path or act-digest defect, and the repair's blast radius is exactly the
six files `SEMANTIC-DELTA.md`'s disposition table names. Rule 10 is stated
correctly: the prior raw's manifest-file digest (`277a50db…`) no longer
matches the current manifest file (`69c5bde8…`), which is the mechanical
signature of "the raw's confirmation covers the reviewed bytes, not
these." Neither finding here (N1, N2) is blocking; N1 names a documentation
boundary worth tightening in a future pass, and N2 confirms a genuinely
open risk stays open rather than closing it silently. **CONFIRM.**
