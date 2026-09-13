# R-PWB-M1-POLARIS-LANE-A — independent review, raw

- **Subject commit:** `2ef68f5b28307003e8fc38668986765ab0f884b5` (parent `8887cff7972eaac1221adb404dbc8cb098b92a88`), branch main.
- **Evidence file:** `docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`
  — sha256 `5146831e851ecb03553a5b7e4ba61284d111b3a61066649dd4d70e0a493de619`, 35,396 bytes
  (`sha256sum docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`).
- **Observed repository served:** the Butlers repository at /home/tze/GitHub/butlers,
  revision `2e3bac97790b4bd8906dcac63eadb5642a0bb1ac`, working tree clean
  (`git -C /home/tze/GitHub/butlers status --porcelain` empty;
  the model's `working-tree:sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
  is the sha256 of the empty string, recomputed).
- **Bead / ruling:** syzygy-dov.1; `.syzygy/governance/decisions/POLARIS-M1-PAGE-SIZE-OWNER-RULING-DECISION.md`.
- **Review date:** 2026-09-13. Read-only on the repository throughout: no edit, stage,
  commit, stash or checkout; the loopback daemon on port 7478 was never contacted; the
  machine credential file was never printed. All scratch output under
  `…/scratchpad/review/`; the reproduction captures were written to fresh labels
  `review-before` / `review-after`, so no retained capture was overwritten.
- **Method note (rule 1):** every load-bearing sweep in this report is Python `re` or
  `grep -F`; no `[^]]`-style class was used.

---

## Criterion 1 — reproduction

Copied the evidence file's `measurementScript` verbatim to the review directory, set
`SESSION_SCRATCHPAD` to the session scratchpad, and served one private daemon per
capture from each pre-built detached worktree (`--port 0 --state-dir <scratch>`):

```
./measure.sh $SESSION_SCRATCHPAD/m1/wt-after  review-after
./measure.sh $SESSION_SCRATCHPAD/m1/wt-before review-before
```

Worktree state confirmed first: `wt-after` at `2ef68f5…`, clean; `wt-before` at
`30b1535825948a09a8befb21ac5822eaa35f62c8`, clean, and
`git diff 8887cff..30b1535` is exactly one hunk — `maxHumanResponseBytes`
2097152 → 4194304 in `packages/three-surface-poc-core/src/project-shape-observation.ts`.
Nothing else differs, so the before capture is 8887cff's renderer bytes.

Sizes obtained (curl `size_download`, all status 200):

| capture | direct | tailnet | /api/poc/polaris | /api/poc |
|---|---|---|---|---|
| review-after (2ef68f5) | 1,478,637 | 1,484,487 | 640,592 | 5,520,314 |
| evidence after | 1,478,637 | 1,484,487 | 640,592 | 5,520,314 |
| review-before (30b1535) | 2,132,656 | 2,138,506 | 640,592 | 5,520,314 |
| evidence before | 2,132,656 | 2,138,506 | 640,592 | 5,520,314 |

All eight sizes reproduce exactly. `sha256sum` over the retained captures reproduces
every digest recorded in `captures` (before direct `bf9255d5f3a0d507a18e6ce46ed3f5d57f2fbced3167fa925ebf804b1d4c80a9`, before tailnet
`19cd0dbb3dec4f0b2d8108afe9650491287797459fa440928329c7854673bb54`, before envelope `614b6ba9b67e74eede3bf6a58f98bff5d552b70af87d5af523a399320b1d7dfc`; after direct `2fecdd01e1a2ff577567495796ea7e59ab89f1420be6033e23314d26442ea094`,
after tailnet `e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111`, after envelope `ab3b517be1e62a0a7f4cabe73d870f9aa6bea7d2bbbadf0d27a2f00c34eca22e`).

**Bytes are not identical between the retained capture and my re-run**, as the page
carries per-run instants. I characterised exactly which fields differ. After replacing
the run's `observationDigest` (one 12-hex occurrence on each HTML form, two 64-hex
occurrences in `/api/poc`) and ISO instants, the retained and re-run files are
**byte-identical** for all six page/model files:

```
before polaris-direct.html  equal_after_scrub True
before polaris-tailnet.html equal_after_scrub True
before api-poc.json         equal_after_scrub True
after  polaris-direct.html  equal_after_scrub True
after  polaris-tailnet.html equal_after_scrub True
after  api-poc.json         equal_after_scrub True
```

`api-polaris.json` needed only the ISO-instant scrub to become identical. The
`data-evaluation-id` value is stable across runs at the same inputs; only the
observation digest and the `asOf` instants move. **Criterion 1: met.**

---

## Criterion 2 — every [Observed] number recomputed from the retained captures

Independent recomputation, not a re-run of `invariantsScript`. For the attribute
multisets I wrote my own start-tag scanner (quote-aware character scan over the
document, then per-tag attribute parse) rather than the record's per-attribute
`\sname="…"` regex, so the two methods are genuinely independent (rule 2).

### Sizes and arithmetic

```
direct  2,132,656 → 1,478,637   saving 654,019
tailnet 2,138,506 → 1,484,487   saving 654,019
ceiling headroom (tailnet)  before −41,354   after +612,665
savingShareOfBefore (direct) 0.3067
Q3 shortfall  direct +78,637   tailnet +84,487
pageBytesPerMachineItem  before 5,153   after 3,577   (denominator 415)
machineModelBytes 5,520,314
```

Every figure in `result` and in `perItemCost.pageBytesPerMachineItem` reproduces.

### Attribute multisets (tailnet before vs after, independent tokenizer)

```
data-claim-id           713/713  distinct 703/703  equal=True
data-polaris-item       409/409  distinct 409/409  equal=True
data-polaris-source     278/278  distinct 278/278  equal=True
data-narrative-block    714/714  distinct 714/714  equal=True
data-claim-provenance   714/714  distinct 703/703  equal=True
data-unknown-disclosure   22/22  equal=True
data-polaris-gap            1/1  equal=True
data-anchor-id          935/935  distinct 916/916  equal=True
data-parity-field     1570/1570  distinct  23/23   equal=True
data-polaris-section      44/44  equal=True
data-polaris-class          9/9  equal=True
href                  1089/1089  distinct 444/444  equal=True
id                      351/350  equal=False — onlyBefore = ['polaris-narrative'], onlyAfter = []
data-evaluation-id      713/713  equal=False — one distinct value each side, the per-run instant
```

Every recorded count, distinct count and `equalMultiset` verdict reproduces, including
the record's stated `id` difference (the removed narrative script element is the single
dropped id; no duplicate id on either form).

Boolean markers, counted with a quote-stripping scan so an attribute *value* containing
the name cannot match:

```
data-presentation-artifact  2669 → 2653
data-non-citable            2669 → 2653
delta by tag: td −324, span +324, th −15, div −5, ul +5, script −1
```

This reproduces `presentationMarkersByTag` tag-for-tag on both sides (all 21 / 20 tags).
I cross-checked the header figure directly: the five trimmed classes each carried exactly
three `<th>` before (`Key`, `Declared`, `Epistemic state`) and none after; page-wide
`<th` goes 32 → 17, so the 15 removed headers are the trimmed classes' own, as recorded.

### Claim-tuple multiset

Extracted every `<span class="claim-tuple" …>` and parsed all its attributes (the record
compared a hand-listed seven-field projection; I compared the full attribute set, which
turned out to be eleven names). Result:

```
713 tuple spans before and after; 703 distinct claim ids each
the only attribute whose value-set differs before vs after is data-evaluation-id
tuple multiset over every attribute except data-evaluation-id: EQUAL
distinct evaluation ids: 1 before, 1 after
```

`equalMultisetModuloEvaluationId: true` confirmed on a strictly wider field set than the
record used.

### Unknown claim set

Unknown claim ids: 11 before, 11 after, and the two sets are equal. They are the
roster-identity class claim, the whole-project-shape claim, the source claim for the
frontend page under the lay-and-land directory, the source claims for the seven withheld
butler TOML files under the roster directory (chronicler, education, general, health,
lifestyle, relationship, travel), and the source claim for the QA manifesto page — all
plain-prose descriptions here, deliberately not written as code spans.


These are exactly the Butlers data quirks AGENTS.md already discloses (frontend and the
withheld TOML as active content, the roster-identity/whole-shape Unknowns). No Unknown
was removed or added.

### Visible-text accounting

My own tag-stripping + per-run-identity scrub (40-hex, 64-hex, 12-hex, ISO instants,
`pwb-eval-…`, `polaris@…`, working-tree strings):

```
visible words before 26,737   after 26,352
wordsOnlyBefore 385           wordsOnlyAfter 0
onlyBefore top: Key×5, Declared×5, state×5, Epistemic×5, 6:×5, Store×3, …
```

Decomposition, recomputed independently:

```
five trimmed classes, 324 before <tr> rows
sum of the Declared cell's reading-prose words: 365
table-header words: 4 per class × 5 classes = 20
365 + 20 = 385
Counter equality  onlyBefore == proseWords + headerWords : True   (both differences empty)
```

So the record's `385 = 20 + 365` is exact, not approximate. I also tested the *claim*
behind it rather than only the arithmetic: of the 324 removed Declared cells, **317**
have reading-prose text token-identical to the row's Key cell, and the remaining 7 differ
only because the key contains backticks that the markdown renderer turned into `<code>`
(e.g. key ``5:`/chronicles``` → prose `5: /chronicles`). And in the after page,
**0 of 324** list entries fail to carry their key in visible text. The vanished words are
a removed duplicate, and nothing a reader could read before is unreadable now.

### Narrative JSON, envelope, anchors

```
before in-page script payload 639,806 bytes; 714 blocks; 916 anchors
after envelope 640,592 bytes;               714 blocks; 916 anchors
before envelope narrative  == before in-page (scrubbed): True
after  envelope narrative  == before in-page (scrubbed): True
after page contains '<script type="application/json"' : False
after page contains '"kind":"polaris-narrative"'       : False
envelope anchor ids 916; page distinct data-anchor-id 916; uncited 0; page-only 0
```

### Per-item cost, item rows, fragments, mount prefix

```
afterCompactListEntry   count 324  mean 1486  max 1811
afterStatementTableRow  count  85  mean 1482
beforeTableRowAllClasses count 409 mean 1513
envelopeNarrativeBlock  count 714  mean  892
compactListClasses: topology-component 87, roster-identity 6, design-contract 32,
                    baseline-spec 192, craft-policy 7   (sum 324; 324 + 85 = 409)
machineItems 415; rendered exactly once 409 on BOTH captures;
   the 6 not-once are the project-account-section items, as recorded
fragment hrefs 699 both; dangling [] both; duplicate ids [] both;
   ids inside <details>: the same three on both
tailnet internal hrefs: 390 prefixed / 0 unprefixed, both captures
direct  internal hrefs:   0 prefixed / 390 unprefixed, both captures
```

Every `[Observed]` number in `result`, `captures`, `invariants` and `perItemCost`
reproduces. **Criterion 2: met**, with three arithmetic/labelling observations carried to
findings 2 and 3.

---

## Criterion 3 — the diff, and the two requirement properties

`git diff --name-status 8887cff..2ef68f5` (13 files):

```
M .syzygy/governance/decisions/DECISION-HISTORY.md
M .syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md
A .syzygy/governance/decisions/POLARIS-M1-PAGE-SIZE-OWNER-RULING-DECISION.md
M apps/three-surface-poc/src/polaris.ts
M apps/three-surface-poc/src/polaris-narrative.ts
M apps/three-surface-poc/src/polaris-{authority-sweep,capability-detail,first-reading,
    narrative,parity-sweep,presentation-route,reachability}.test.ts   (7 test files)
M docs/PWB-IMPLEMENTATION-PLAN.md
```

- `git diff --name-only 8887cff..2ef68f5 -- openspec/` → **0 files**. The signed PWB
  specification, and PWB-REQ-007/014/020 with it, are untouched.
- `docs/PWB-IMPLEMENTATION-PLAN.md`: one hunk, and it is the marked-in-place shape
  AGENTS.md asks for — the superseded sentence is kept verbatim and the marker names the
  date and the bead ("**Superseded 2026-09-13** … the sentence before this one describes
  the page as it was until that date"). No page-level banner substituted for it.
- **Three files under `.syzygy/` did change** — see finding 1. None is digest-bound
  (`check_governance.py` CG-7a/7b/7c/7e/15 all report 0 findings on the working tree), the
  new file is a plain owner-direction record that says of itself "Nothing here is an act:
  no digest is bound, no specification, policy or registry changes", and no implementation
  code was placed in a governed plane. I re-derived the register arithmetic the commit
  edits: the open section holds 21 `P-` rows counted with sub-lettered rows included
  (`P-25(c)` present) and the acceptance-act section holds 5, so the banner's "21 open …
  and 5 acceptance-act rows, 26 in all" is exact.

**PWB-REQ-014** — the envelope is the narrative of the same render: verified above
(714/916 identical to the before in-page registry after per-run scrub; every envelope
anchor cited on the page; no page copy). Additionally, `/api/poc` before vs after is
byte-identical once the per-run identities are scrubbed, with the *only* remaining
difference being `inputsDigest`, which folds in the observer revision (30b1535 vs
2ef68f5). Lane A changed the machine truth by nothing at all.

**PWB-REQ-020** — parity per tuple, not per id. I checked every rendered tuple against
its machine claim by id, and both id sets, on both captures:

```
after : 713 rendered tuples, 0 field mismatches against the machine claim
before: 713 rendered tuples, 0 field mismatches against the machine claim
rendered ids not present in the machine answer: 0
```

(The fields are `label`, `tier` — rendered `unstated` exactly where the machine omits it,
which is all 11 Unknown claims — `freshness`, `reasons.primary` rendered `none` where
absent, `reasons.secondary`, and `challenge`.) 713 tuples over 703 distinct ids confirms
the AGENTS.md caution: ids repeat, so per-id counting would be the false invariant here,
and the per-tuple check is the one that holds.

**Criterion 3: met for openspec and for both requirement properties; not met as written
for `.syzygy/` (finding 1).**

---

## Criterion 4 — the four rule-6 mutants

I did not re-run the mutants: reverting each one requires `git checkout --`, which this
review is barred from, and the recorded run mutated the main checkout. I verified them
structurally instead, which is sufficient to test the two things the criterion asks.

**(a) The old fragment exists at the named commit.** For each mutant,
`git show 2ef68f5:<file>` and count the literal:

```
list-container-renamed        old occurrences 1
list-container-dropped        old occurrences 1
script-re-embedded            old occurrences 1
route-serves-empty-narrative  old occurrences 1
```

All four are unique at the commit — the same precondition the generating script asserts.

**(b) The new fragment defeats the property the guard names.** Read the guards at 2ef68f5:

- `list-container-renamed` (`<ul class="item-list"` → `<ul class="items"`):
  `polaris-parity-sweep.test.ts:494` detects an item container by
  `section.inner.includes('<tbody>') || section.inner.includes('<ul class="item-list"')`
  — the literal opening, deliberately, "so a hoisted attribute cannot masquerade as one".
  Renaming the class drops all five classes out of `classes-with-item-tables`, whose
  expectation is derived from the machine answer at line 507. Killed, and the kill is in
  the right family.
- `list-container-dropped` (the whole `population('items', …)` branch → `''`):
  `itemExpected` is pushed at line 499-501 from `observed.items` for every class in
  `CLASSES_WITH_ITEM_TABLES`, explicitly **ungated** on container detection ("a class
  whose container vanished reports its items as missing instead of an empty-versus-empty
  pass"). This is precisely the guard the AGENTS.md lesson about dropping a family "to a
  human count of 0 rather than failing loudly" was paid for, and it holds.
- `script-re-embedded` (prepends `<script type="application/json" id="polaris-narrative">{}</script>`):
  `polaris-presentation-route.test.ts` asserts
  `expect(humanHtml).not.toContain('<script type="application/json"')`. Killed.
- `route-serves-empty-narrative` (`narrative` → `{ ...narrative, blocks: [] }` in the
  envelope): the same test asserts `expect(sameRender.blocks.length).toBeGreaterThan(0)`
  then `expect(envelope.narrative).toEqual(sameRender)`. Killed, and the emptied-blocks
  mutant cannot pass the `toBeGreaterThan(0)` sentinel either.

**(c) The recorded outcome.** The retained `mutants.json` in the session scratchpad is
**record-for-record identical** to the evidence file's `mutants` section (commit, `ranAt`
`2026-09-13T13:30:32+00:00`, and all four entries compare equal), and `mutants.log`
carries the matching per-mutant exit-1 lines naming the failing test files. Each entry
stores `old`, `new`, `testFiles` and the commit, so the run is re-runnable — the
re-runnability bar AGENTS.md sets for a rule-6 record. **Criterion 4: met.**

I also re-ran the repository's own battery on the working tree:
`python3 scripts/check_governance.py` → **32 OK, 20 WARN, 0 FAIL (52 checks)**, matching
`verification.governance` exactly.

---

## Criterion 5 — labelling honesty

- The `labels` line sets the default ("Every number below is [Observed] from the retained
  captures unless marked [Inferred]") and the two genuinely inferential statements —
  `trim.savingBreakdown.listFormBytes` and `followUp.laneB` — are the two carrying
  `[Inferred]`. I found no [Observed]-defaulted number that is not derivable from the
  captures.
- **The Q3 target is not claimed met.** `result.q3Target` records
  `directMet: false`, `tailnetMet: false`, and the shortfalls (+78,637 direct, +84,487
  tailnet), and `followUp` restates that the after page is 84,487 bytes over on the
  tailnet form with each statement-less item still ~1,486 bytes against the 1,000-byte
  target. This is VIS-2-shaped: the gap is rendered, not smoothed.
- **The scratch-ceiling before method is disclosed**, in `method.beforeCapture`, naming
  the scratch commit, the constant changed, the values, and that it is measurement-only.
  `syzygy.before.commit` repeats it, and `nonGoalsHonoured` records that the scratch
  commit lives only in the before worktree. The disclosure matches what I found in the
  worktree exactly.
- Two places where the record declines to round a `false` into a `true` rather than
  hiding it: `invariants.narrativeJson.afterEnvelopeEqualsBeforeInPageModuloObserverAndTimestamps: false`
  is retained beside the wider-scrub `…ModuloPerRunIdentities: true`, and
  `visibleText.equalModuloPerRunIdentities: false` is retained beside
  `wordsOnlyAfter: 0`. Both are honest; see note 6.

**Criterion 5: met.**

---

## Criterion 6 — backticked Butlers paths and truncated act digests

- `check_governance.py` on the working tree: **CG-1b** (code-span path references
  resolve) OK, 4,825 references examined, 0 findings; **CG-15** (truncated digest quotes
  still current) OK, 15 quotations, 0 findings; **CG-7e** (act-argument copies) OK, 32
  files, 0 findings. 0 FAIL overall.
- Independent sweep of the commit's Markdown plus the funnel packet and the ruling
  decision, matching every code span against the Butlers repository's tracked path set
  and against Butlers-only path shapes (about/…, roster/…, butler.toml, lay-and-land,
  MANIFESTO.md): the only code-span hits are names that exist in *both* repositories
  (AGENTS.md, README.md, LICENSE, .gitignore) or are Syzygy-relative
  (../policies/craft-and-care/…). No Butlers-only path is backticked in the new ruling
  record, in the funnel packet, or in the lines this commit added.
- Short-hex scan of the same files: every short-hex token is either a git short revision
  (the Butlers revision named by the funnel packet and the ruling) or a pre-existing
  identifier in `docs/PWB-IMPLEMENTATION-PLAN.md` and in `DECISION-HISTORY.md` that this
  commit did not add — in the latter case two truncated act arguments that CG-15 examines
  and reports current, and which are therefore not restated here. **No truncated act
  digest is introduced by any line this commit added**, and none appears in the evidence
  file, which is JSON and quotes only full 64-hex capture digests — the permitted form.

**Criterion 6: met.**

---

## Findings

1. **should-fix — the commit is not implementation-only, and the evidence does not say
   so.** Three files under `.syzygy/governance/decisions/` are in the same commit: the new
   P-67 ruling record, plus the `DECISION-HISTORY.md` and `PENDING-OWNER-DECISIONS.md`
   register maintenance that moves the row. Nothing is unlawful — the record binds no
   digest, no specification or policy changed, openspec is untouched, no implementation
   code entered a governed plane, and the register arithmetic it writes (21 open + 5 act
   rows = 26) re-derives exactly. But `trim.files` lists only the renderer, the seven test
   files and the plan sentence, and `nonGoalsHonoured` opens "no registry, spec or policy
   change" — a reader auditing the claim "implementation-only trim" against the commit
   will find three governance files the evidence never mentions, and "registry" is
   ambiguous between the PWB source registry and the decisions register. Add the ruling
   record to `trim.files` (or state that the commit also carries the ruling) and
   disambiguate the word "registry".

2. **should-fix — `invariants.tailnetMountPrefix.directFormUnprefixed` is mislabelled.**
   It records `{before: 0, after: 0}`, but the generating script assigns
   `mount(Bd)['prefixedInternalHrefs']` to that field. The direct form actually carries
   **390 unprefixed and 0 prefixed** internal hrefs on both captures (I measured both
   directions). The property the record means to assert — the direct form carries no
   mount prefix — holds, and the number 0 is correct for the prefixed count; the field
   *name* contradicts its own value, and a later reader re-deriving "0 unprefixed on the
   direct form" would get 390 and believe the record falsified.

3. **should-fix — the [Inferred] per-item figure understates the measured saving, and
   rests on two different denominators.** `savingBreakdown.listFormBytes` reads "the
   remainder of the direct saving, 14213 bytes, is the compact list form over 324 items
   (about 27 bytes per item, plus 5 table heads)". Recomputed directly:
   - the removed script **element** is 639,914 bytes (the recorded 639,806 is the payload
     without its opening and closing tags), so the remainder is 14,105, not 14,213;
   - the five trimmed class sections shrank by **14,218 bytes**, i.e. **43.9 bytes per
     item** including the removed table scaffolding;
   - over the *same* 324 items, the before `<tr>` mean is 1,521 bytes and the after `<li>`
     mean 1,486, i.e. **35.1 bytes per item** for the row itself, the remaining
     2,833 bytes being the five tables' scaffolding.

   The recorded "about 27" is the difference of `beforeTableRowAllClasses.meanBytes`
   (1,513, over **409** rows across all nine classes) and `afterCompactListEntry.meanBytes`
   (1,486, over **324** entries) — two means over different populations. Both underlying
   means are correct and reproduce; the subtraction of them is not a per-item delta. The
   figure is labelled `[Inferred]`, so this is a precision defect rather than a false
   `[Observed]`, and it errs *against* the change (the real saving is larger).

4. **note — `captures` omits the `/api/poc` digest though that capture is load-bearing.**
   The record digests three files per side but not `api-poc.json`, which supplies the 415
   machine-item denominator, the `itemRows` check and the PWB-REQ-020 parity comparison.
   For completeness: before `9208ce77403c077a12c651e1091fd4cf7da931cb7c6fb4967f1ab51f07df9977`,
   after `a89b0e059b5fdadc5f359c2bee58115cd50747399cfb00444703e0fafdfb466e`. Without them
   the evidence cannot be re-checked against the exact bytes its parity numbers came from.

5. **note — the before-method corroboration is sound, and can be stated with a
   denominator.** `method.beforeCapture` corroborates the scratch ceiling by observing
   that the captured 2,132,656 equals the `observed` field of the 503 the unmodified
   8887cff daemon served at Butlers 7c8743f63, which is a *different* Butlers revision
   (different tree) from the one measured here. I closed that gap: of the **61** files
   changed between Butlers 7c8743f63 and 2e3bac97, **none** is an observed source (278) or
   an exclusion (9), so the rendered page content is stable across the two revisions and
   the equality is a genuine corroboration rather than a coincidence. Worth adding, since
   as written the claim silently assumes it.

6. **note — the two retained `false` invariants read worse than they are.**
   `narrativeJson.afterEnvelopeEqualsBeforeInPageModuloObserverAndTimestamps: false` sits
   above `…ModuloPerRunIdentities: true`; the narrower scrub simply missed the 12-hex short
   digests and the `polaris@` surface version. My own wider scrub gives `True`, and I
   confirmed the after envelope narrative and the before in-page narrative are identical
   once per-run identities are removed. Keeping the `false` is honest; a one-line note
   saying *which* scrub produced it would stop a later reader inferring a real difference.

7. **note — the mutant run mutated the shared checkout.** `mutants.py` hard-codes
   `ROOT='/home/tze/GitHub/syzygy'` and reverts with `git checkout --` in a `finally`. It
   is rule-6-conformant and its own log records the tree clean afterwards apart from the
   co-lead's in-flight `AGENTS.md`, but AGENTS.md warns against editing the checkout while
   a mutation run is in flight, and this repository is run by two parallel lead sessions.
   A detached worktree (both already existed for the measurement) would remove the hazard
   at no cost.

8. **note — one invariant worth recording that the evidence does not claim.** The
   `/api/poc` truth endpoint is byte-identical before vs after once per-run identities are
   scrubbed; the single remaining difference is `inputsDigest`, which folds in the observer
   revision. That is stronger than `apiEnvelope`'s "unchanged size" and is the cleanest
   statement that lane A touched presentation only.

No blocker. The claimed saving, the retained invariants, the mutant kills and the
non-goals all hold on independent recomputation; every defect above is in how a figure is
labelled, scoped or disclosed, not in whether the trim preserved the page's truth.

Verdict: CONFIRMED WITH FINDINGS
