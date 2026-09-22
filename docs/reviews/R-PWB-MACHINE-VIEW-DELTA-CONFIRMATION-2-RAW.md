# Review — PWB machine-view amendment (round 3, second confirmation)
Reviewed commit: 76b4bebcbf7819bda36b9b049ada109b1c6e3db8
Manifest SHA-256: 2a49a8d1d473d4347dadda1489488bc6556102c14e98e18bc58688ffeeb3ed6c
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context session, round 3 (second confirmation) under
CC-REV-1, CC-REV-4 and CC-REV-6. No authoring context; no commit message
body was read for intent (only `%s` subject lines, parent ids and commit
dates were read, as metadata); nothing under `.syzygy/local/` was opened; no
other agent was consulted. Read, in order: `AGENTS.md` in full (the
checkout's copy, diffed against the working copy — the differences are
later lessons and do not touch this review); the package's
`REVIEW-BRIEF.md`; the round-1 raw `docs/reviews/R-PWB-MACHINE-VIEW-DELTA-RAW.md`
and the round-2 raw `docs/reviews/R-PWB-MACHINE-VIEW-DELTA-CONFIRMATION-RAW.md`
in full; `SEMANTIC-DELTA.md` §Review; then the whole package
(`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`,
`PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`, `proposed/spec.md.patch`,
`proposed/GOVERNING-DEPENDENCIES.md.patch`) and the builder
`scripts/build_pwb_machine_view_amendment.py` in full; and, as each check
needed it, the registration blocks of `scripts/check_governance.py`, the
`ACTS` table and docstring of `scripts/record_pwb_behavior_amendment_acts.py`,
`PROJECT-STATUS.md` and `.github/workflows/governance-docs.yml` at three
commits, the two 2026-09-23 owner decision records the dispatch named, the
P-72/P-76 rows of the ruling record, and the four sibling candidates'
`proposed/spec.md.patch` files. The detached checkout at `76b4beb` was
treated as read-only throughout: no checkout, commit, add, apply or edit was
made inside it. Every mutation ran in a `cp -r` copy (every top-level entry
except `node_modules`) under `scratchpad/review3-mv-scratch/base`, restored
with `git checkout --` after each probe. `git status --porcelain` in the
reviewed checkout was empty before the review began (0 lines) and empty
again before this verdict was written (0 lines; final section).

The instrument for this round is the brief's twelve criteria, applied to
the repair diff `git diff 9d74185 76b4beb -- <package dir>` (four files,
prose only) and to the whole package as it stands.

---

## What I ran

All commands from the checkout root unless the scratch copy is named.
Output is what I read, not the exit code.

1. `git status --porcelain | wc -l` → `0`; `git rev-parse HEAD` →
   `76b4bebcbf7819bda36b9b049ada109b1c6e3db8`.
2. `sha256sum …/PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` →
   `2a49a8d1d473d4347dadda1489488bc6556102c14e98e18bc58688ffeeb3ed6c`
   (computed, rule 3). `grep -n -F` of that value over the four package
   `.md` files → exactly two hits, both in `OWNER-DECISION-PACKET.md`
   (`:30` the quoted manifest digest, `:170` the not-offered phrase). Equal
   to line 3 of both earlier raws.
3. **Byte identity across three commits** (`git rev-parse <commit>:<path>`):
   `proposed/spec.md.patch` → `d492e23…` at `02b6ebc`, `9d74185`, `76b4beb`;
   `proposed/GOVERNING-DEPENDENCIES.md.patch` → `156b285…` at all three;
   `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` → `c76599a…` at all three. All
   IDENTICAL. `scripts/build_pwb_machine_view_amendment.py` → same blob at
   `9d74185` and `76b4beb`. `git diff --stat 9d74185 76b4beb -- <package>`
   → exactly four files: `IMPACT-LEDGER.md` (+5/−1),
   `OWNER-DECISION-PACKET.md` (+26/−10), `REVIEW-BRIEF.md` (+9/−2),
   `SEMANTIC-DELTA.md` (+65/−6). [Observed] The repair moved prose only;
   the packet's "the patches and manifest never moved" (`:147`) and the
   delta's "no patch or manifest byte moved" (`:625`) are true.
4. `git diff --stat a4a3451 76b4beb -- openspec/changes/polaris-project-wide-butlers-model/`
   → empty: none of the eleven subjects moved since the ledger's baseline.
5. `python3 scripts/build_pwb_machine_view_amendment.py --check` → exit 0:
   "PWB machine-view amendment manifest matches 11 proposed behavior
   subjects (2 patched, 9 unchanged); the dependency declaration is
   regenerated from the proposed spec and the spec patch composes with the
   sibling candidate in either order".
6. `--selftest` → exit 0: "selftest: closed population, byte drift, path
   order, subject drift, context-line and added-line patch corruption,
   transcribed and unwarranted dependency declarations, sibling drift and a
   missing sibling patch fail closed".
7. `--diff` → exit 0; stdout to a scratch file. Python containment:
   `spec.md.patch` bytes contained → `True`; `GOVERNING-DEPENDENCIES.md.patch`
   bytes contained → `True`; remainder after removing both → 0 bytes. The
   advisory "note: … regenerate with --write after either package lands" is
   on stderr only.
8. `python3 scripts/build_polaris_project_wide_contract_coverage.py --check`
   → "Polaris consequence matrix matches regeneration — 324 clauses
   represented", exit 0 ("does NOT change" item 9, `SEMANTIC-DELTA.md:328-333`).
9. `python3 scripts/check_governance.py` → last line "32 OK, 20 WARN, 0 FAIL
   (52 checks) — counts derived, not asserted". Lines naming this package:
   CG-1c "[declared forward reference]
   `docs/reviews/R-PWB-MACHINE-VIEW-DELTA-CONFIRMATION-RAW.md ->
   decisions/PWB-MACHINE-VIEW-AMENDMENT-ACT.md`" (the round-2 raw names the
   act record that does not yet exist; skipped by design); CG-7d
   "[subject] SIGN OFF PWB MACHINE-VIEW AMENDMENT — 1 quotation(s), 0
   finding(s), 0 performed digest(s)"; CG-7e "[registered]
   …/pwb-machine-view-amendment/OWNER-DECISION-PACKET.md — declares 1
   current and 0 performed-history act(s); 1 current, 0 historical valid".
   None of CG-27's 17 findings names a path under
   `contracts/candidates/pwb-`. The 20 WARNs are the report-only families
   (CG-1c…CG-27) and are outside this package. `--selftest` → "263
   fixtures, 0 failing".
10. **F4, step 3, against `scripts/check_governance.py` itself** (file and
    line, at `76b4beb`): `PWB_MACHINE_VIEW_LABEL` `:1542`,
    `PWB_MACHINE_VIEW_DIR` `:1543`, `PWB_MACHINE_VIEW_SUBJECT` `:1544-1545`,
    `PWB_MACHINE_VIEW_ACT` `:1546-1547`; `def _act_subjects()` at `:2022`
    (next `def` at `:2131`) with the machine-view entry at `:2066-2072`;
    `ACT_DIGEST_COPY_FILES` row for the packet at `:2283-2284`;
    existence-gated activation `_activate_pwb_machine_view_act_copy_registry`
    at `:2422-2424` over `_activate_pwb_candidate_act_copy_registry`
    `:2407-2419`; `PWB_SUCCESSOR_CHAIN` at `:1631-1638` carries exactly three
    links (state1, truth-and-readiness, scoped-attributes) and no machine-view
    link. The comment at `:1537-1541` says the link is withheld "until an act
    fixes the performance order". [Observed]
11. **F4, step 6.** `grep -n build_pwb_machine_view_amendment` →
    `PROJECT-STATUS.md:254-255` and `governance-docs.yml:118-122` at
    `76b4beb`; the same lines present at `9d74185`; 0 hits in either file at
    `02b6ebc`. `grep -n record_pwb` over both files → 0 hits: no recorder's
    `--check` is in the battery yet. `9d74185` has one parent (`a4a3451`),
    subject ends "(#52)", committed 2026-09-22 08:00 +0800 — a squash merge
    of PR #52, so "Performed at the merge of PR #52 (`9d74185`, 2026-09-22)"
    and "since `9d74185`" are exact. [Observed]
12. **The recorder the packet now names** (`OWNER-DECISION-PACKET.md:176`).
    `scripts/record_pwb_behavior_amendment_acts.py` first appears at
    `e49fecf`, 2026-09-23 01:40:28 +0800 ("added 2026-09-23": true).
    Imported its `ACTS` table: `len(ACTS) == 1`, the one key `render-mode`
    with label `SIGN OFF PWB EXACT-SOURCE RENDER-MODE AMENDMENT`;
    `grep -n -i machine` over the script → one hit, inside the render-mode
    entry's effect prose ("machine answer"). "carries no entry for this
    package yet": true. [Observed] Its docstring `:31-33`: "The
    successor-chain link and the existence-gated copy registrations in
    `check_governance.py` are the performing change's to add; this script
    prints what it knows and edits no check." (See F8.)
13. **Rule 8, the repair's quotations of superseded text.** Python
    substring test of each quoted first-draft sentence against the
    whitespace-normalized `9d74185` blob of the file that carried it:
    packet "no review has been run against these bytes, and no verdict
    exists for them" → True; "send it to fresh-context review as drafted"
    → True; "the manifest is regenerated" → True; "no fresh-context review
    has confirmed these bytes, and no recorder exists" → True (a prefix of
    the original, which continues "that would accept it"); delta "No
    reviewer has seen these bytes." → True; "not yet assigned" → True; "The
    three edits are listed in `OWNER-DECISION-PACKET.md`" → True; brief
    "This is the first round. No review has been run against these bytes"
    → True (a prefix). No quotation drift.
14. **F3 stale-sentence sweep**, the round-2 regex
    (`first round|first draft|no review has been run|no reviewer|not yet
    assigned|no verdict|has run no review|no fresh-context review`,
    case-insensitive) over the four package `.md` files → 15 hits, every one
    either inside a quotation of the superseded text, the phrase "first
    draft" used as a dated label, or the still-true "this draft's author has
    run no review of it" (`SEMANTIC-DELTA.md:570`). Zero current-state
    claims of "no review" remain.
15. **Owner-packet tests (criterion 12).** `grep -c -F` of the full phrase
    `SIGN OFF PWB MACHINE-VIEW AMENDMENT: 2a49…ed6c` → 1 (`:170`), inside
    the section headed "Not yet offered" and followed at `:173-174` by "it
    is **not offered**". `grep -n -i "authoriz\|implement"` → three lines,
    all negations (`:4` "authorizes no implementation, no route and no
    registry edit"; `:197-198` "Nothing is implemented after either act; an
    implementation bead is opened separately, under its own
    authorization"). `:161-163` "Silence, a partial answer, a commit or a
    merge performs nothing"; `:3-6` the inert-offering banner. Options
    (a)/(b)/(c) at `:144-159`.
16. **Rule-6 mutations**, each in the scratch copy, `git status --porcelain
    | wc -l` → `0` after each restore:
    - **A — corrupt one added line of `proposed/spec.md.patch`**
      (`sed` on the line `+mints no project fact, writes nothing, sends no
      source or draft byte outside` → `… sends one source …`; `git diff
      --stat`: 1 file, 1 insertion, 1 deletion). `--check` → exit 1:
      ```
      PWB machine-view amendment manifest does not verify:
        proposed GOVERNING-DEPENDENCIES.md bytes are not the generator's output over the proposed spec.md bytes
        manifest differs from exact regeneration over the proposed bytes
      ```
    - **B — transcribe a wrong digest into the manifest** (row 18, the
      `spec.md` row, last hex digit `8` → `9`). `--check` → exit 1:
      ```
      PWB machine-view amendment manifest does not verify:
        manifest differs from exact regeneration over the proposed bytes
      ```
    - **C — go stale on both digest copies in `OWNER-DECISION-PACKET.md`**
      (`sed s///g`, last hex digit `c` → `d`; `grep -c` of the mutant → 2).
      `check_governance.py` → exit 1, "31 OK, 19 WARN, 2 FAIL (52 checks)".
      CG-7d: "…/OWNER-DECISION-PACKET.md:170 — quotes `SIGN OFF PWB
      MACHINE-VIEW AMENDMENT: 2a49a8d1d473…` but
      …/PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt hashes to 2a49a8d1d473… and
      …/ACCEPTANCE-ACT-RECORD.md records no performance of that argument".
      CG-7e: "…/OWNER-DECISION-PACKET.md — declared to carry act `SIGN OFF
      PWB MACHINE-VIEW AMENDMENT` and does not contain its current argument
      … The copy in this file is stale, and this file is one the owner is
      sent to". (The check truncates the digest in its own output; I copy
      its line, and the full current value is in run 2.)
    - **D — corrupt one context line of the sibling scoped-attributes
      patch** (` …available on demand.` → ` …available on request.`, the
      fixture the builder's own selftest uses, applied to the real sibling
      file). `--check` → exit 1: "sibling-first composition failed:
      spec.md.patch does not apply to
      openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md:
      error: patch failed: …spec.md:450 / error: …spec.md: patch does not
      apply".
17. **Sibling population and composition (criterion 10, F5).** At `76b4beb`,
    `ls .syzygy/governance/contracts/candidates/*/proposed/spec.md.patch` →
    **five** files, every one with `+++ b/openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`:
    `pwb-machine-view-amendment`, `pwb-scoped-attributes-amendment`,
    `pwb-exact-source-render-mode-scenario`, `pwb-opening-band-scenario`,
    **`pwb-missing-currency-disclosure-scenario`**. Five
    `proposed/GOVERNING-DEPENDENCIES.md.patch` files, same directories. The
    fifth package's manifest has 11 rows whose paths equal this package's
    eleven (`diff` of the path columns → identical); it is registered in
    `check_governance.py:1557-1562` and its `spec.md.patch` first appears at
    `807cecf`, 2026-09-23 01:37:44 +0800, an ancestor of `76b4beb`
    (`git merge-base --is-ancestor` → true), 2 min 44 s before the repair
    commit. [Observed] See F6.
    Composition, `git apply` in a temp tree over the current `spec.md`
    (sha256 `42d073cd…`):
    - this package's patch with each of the four siblings, both orders: 8
      of 8 apply; each pair yields one digest in both orders
      (scoped-attributes `37737cc0…`, the round-1/round-2 figure;
      exact-source `1cc36a17…`; opening-band `55faf032…`; missing-currency
      `9459f638…`).
    - all 120 five-way orders: 60 apply, every one to the single digest
      `32277aa713e7416c08e8e95fff4d50eff5d72276bc71d22209cf5db228012994`;
      60 fail, and the failing set is exactly the set in which
      `pwb-missing-currency-disclosure-scenario` precedes
      `pwb-scoped-attributes-amendment` (60 of 60), failing at the
      scoped-attributes hunk at `spec.md:450`. Pairwise: 19 of 20 ordered
      pairs apply; the one failure is missing-currency then
      scoped-attributes. That pair is two other packages; this package's
      patch is not the failing member in any order. [Observed]
18. **Ceiling precondition (criterion 6), unchanged since round 2.**
    `maxBriefingResponseBytes` occurs 0 times in the package's patches; the
    sibling `pwb-registry-currency-briefing-amendment/proposed/*.json.patch`
    adds it (`+ "maxBriefingResponseBytes": 20480`, patch line 27) with a
    description at patch line 35 that bounds "each authenticated derived
    read-only machine view response that serves one named subject composed
    from an evaluation already served under maxMachineResponseBytes". See
    the note under "Open question 6".
19. Owner records the dispatch named:
    `POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md` §2 (`:54-70`):
    three verbatim answers, every drafted value stands, read as arm (a);
    "Review status at presentation: none run" is that record's own as-of
    statement. §6 (`:110-129`): landing order "Readiness order, lane B
    last", read as `.21 → .30 → .22 → lane B`, "fixes order only". First
    committed at `39bc2dc`, 2026-09-23 01:24:56 +0800 — in the tree at
    `76b4beb`. `POLARIS-GATE-PACKAGE-OPEN-QUESTIONS-2026-09-23-DECISION.md`
    `:77` question 6 "Hold for .22 review (Recommended)"; `:96-98` "The
    drafter's leaning, one claim id, goes to the `.22` reviewer as input
    only. The owner decides when that review returns." P-72 and P-76 rows
    at `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:60,62`, both arm A,
    matching `SEMANTIC-DELTA.md:411-416`.
20. Line-length sweep of the repair's added lines: four exceed 79 columns
    (`IMPACT-LEDGER.md:121` at 134, `OWNER-DECISION-PACKET.md:209` at 106,
    `SEMANTIC-DELTA.md:45` and `:551` at 80). No code span is broken across
    a line (AGENTS.md's wrapped-citation lesson does not bite). Cosmetic;
    folded into F6's repair.

---

## F3 — DISCHARGED. Every sentence round 2 listed is reworded or marked at the sentence, with the superseded text quoted.

*Round-2 anchors at `9d74185`:* `OWNER-DECISION-PACKET.md:8-9`, `:137-139`,
`:163`; `SEMANTIC-DELTA.md:44-45`, `:555-557`; `REVIEW-BRIEF.md:9-10`.
*Repairs at `76b4beb`:*

- `OWNER-DECISION-PACKET.md:8-16` — date line now states both rounds and
  their verdicts with the raw paths, the rule-10 status of the current
  bytes, and quotes the superseded sentence "true on 2026-09-21, superseded
  since". Quoted text byte-equal to the `9d74185` sentence (run 13). [Observed]
- `OWNER-DECISION-PACKET.md:144-150` — arm (a) is now "Yes — as drafted",
  says when a phrase is offered (a confirming round *and* a recorder entry),
  records "Two rounds have run as of 2026-09-23", and quotes the
  first-draft wording with an ellipsis; both quoted fragments byte-equal
  (run 13). [Observed]
- `OWNER-DECISION-PACKET.md:173-180` — the not-offered reason is now the
  rule-10 form plus the absence of a recorder *entry*, naming the recorder
  file; the first-draft reason is quoted. Both halves verified against the
  tree (runs 3, 12). [Observed]
- `SEMANTIC-DELTA.md:44-47` — "Two fresh-context rounds have read earlier
  bytes of this file (§Review); no reviewer has seen these repaired ones",
  first draft quoted and dated. True at this commit by construction (round 2
  reviewed `9d74185`; these bytes post-date it). [Observed]
- `SEMANTIC-DELTA.md:568-571` — reviewer line now "a fresh-context session
  … per round (two so far, 2026-09-21 and 2026-09-23)", first draft quoted.
  The 2026-09-23 date matches the round-2 raw's commission sentence
  (`R-…-CONFIRMATION-RAW.md:… "commissioned 2026-09-23"` per
  `SEMANTIC-DELTA.md:613`, and the raw's first commit `76b4beb`,
  2026-09-23). The **2026-09-21** date for round 1 is [Unknown] from the
  bytes: the round-1 raw carries no date of its own and first landed at
  `9d74185` (2026-09-22 08:00 +0800). Not a finding — nothing contradicts
  it — but it is a date the package asserts and no retained artifact
  states.
- `REVIEW-BRIEF.md:9-17` — "Two rounds have been run against this brief",
  the first-draft sentence quoted, both verdicts and raw paths named, and
  the rule-10 caveat stated. The brief carries no date line of its own, so
  "the first draft said here" is dated only by reference to the packet and
  delta. [Observed]

The disposition text (`SEMANTIC-DELTA.md:630-635`) — "repaired at each
sentence, superseded text quoted and dated: the packet's date line, arm (a)
and the not-offered reason; this file's author and reviewer lines; the
brief's 'first round' paragraph" — is true of the bytes. Criteria 11, 12.

## F4 — DISCHARGED. Step 3's registration claim is verified line by line; the chain link is absent as the sentence says; step 6 is truthful about what is already in the battery.

*Round-2 anchors at `9d74185`:* `SEMANTIC-DELTA.md:518-520`, `:528-532`.
*Repairs at `76b4beb`:* `SEMANTIC-DELTA.md:520-527`, `:535-542`.

- Step 3 now says the registration was "**Performed** at the merge of PR
  #52 (`9d74185`, 2026-09-22): the label, directory, subject, act-record
  path, `_act_subjects()` entry and the packet's digest-copy row are
  registered; the successor-chain link is withheld until the act fixes the
  order", and quotes the superseded "three edits" sentence with "the packet
  never listed them — round 2 finding F4". Each of the six registered items
  exists at the lines in run 10; the chain at `:1631-1638` has no
  machine-view link; the commit is a single-parent squash of PR #52 dated
  2026-09-22 (run 11). Every clause true. [Observed]
- Step 6 now says adoption adds the successor-chain link and puts "the
  recorder's `--check`" in the battery, and that the builder's `--check` and
  `--selftest` "are already in the PROJECT-STATUS battery and the hosted
  workflow since `9d74185` (2026-09-22), not gained at adoption as the
  first draft said". Battery lines present at `9d74185` and `76b4beb`,
  absent at `02b6ebc`; no `record_pwb` line in either battery file today
  (run 11). Consistent with the recorder's docstring (run 12). [Observed]
- Disposition text (`SEMANTIC-DELTA.md:636-641`): "step 3 is marked
  performed at `9d74185` with what was registered and what was withheld;
  step 6 now says what adoption still adds and that the builder's checks are
  already in the battery" — true of the bytes, except that it locates the
  repair in a section called "How this would be adopted", which does not
  exist (F7).

Criteria 9 and 11.

## F5 — DISCHARGED AS WRITTEN, BUT THE REPAIR IS FALSE ON ARRIVAL (see F6).

*Round-2 anchors at `9d74185`:* `SEMANTIC-DELTA.md:536-546`,
`IMPACT-LEDGER.md:103-118`, `OWNER-DECISION-PACKET.md:185-195`. *Repairs at
`76b4beb`:* `SEMANTIC-DELTA.md:546-551`, `IMPACT-LEDGER.md:118-121`,
`OWNER-DECISION-PACKET.md:206-209`.

Each of the three places now carries a dated sentence generalizing
"second" to "each one signed after the first" and stating that the builder
composes against scoped-attributes only (true: `SIBLING_SPEC_PATCH` at
`build_pwb_machine_view_amendment.py:60-63` and `coexistence_findings`
`:186-217` name that one file). The disposition (`SEMANTIC-DELTA.md:642-646`)
describes exactly that. What round 2 asked for is present. But each of the
three sentences states a sibling *count* — "three", "two more candidates",
"so are X and Y" — that was already wrong when the repair commit was made
(run 17). That is a new false sentence introduced by the repair and is
recorded as F6, not folded into F5, because it is the class of defect the
round-2 finding was about and it recurred in the fix.

---

## New findings

### F6 — revise (non-blocking). The F5 repair counts three siblings; the tree at `76b4beb` holds four, and the fourth landed 2 min 44 s before the repair.

*Criterion 10 (sibling ordering) and 11 (comprehension); AGENTS.md
"Measuring last is not enough" and rule 2.*

- `IMPACT-LEDGER.md:118-121` — "As of 2026-09-23 the sibling population is
  three (`pwb-exact-source-render-mode-scenario/` and
  `pwb-opening-band-scenario/` patch the same subjects; …)".
- `OWNER-DECISION-PACKET.md:206-209` — "As of 2026-09-23 two more candidates
  patch the same subjects (`pwb-exact-source-render-mode-scenario/`,
  `pwb-opening-band-scenario/`), …".
- `SEMANTIC-DELTA.md:546-551` — "… and as of 2026-09-23 so are
  `pwb-exact-source-render-mode-scenario/` and `pwb-opening-band-scenario/`".

At `76b4beb` a fourth sibling, `pwb-missing-currency-disclosure-scenario/`,
carries a `proposed/spec.md.patch` and a
`proposed/GOVERNING-DEPENDENCIES.md.patch` against the same file, a manifest
over the same eleven paths, and a `check_governance.py` registration
(`:1557-1562`); its patch first appears at `807cecf` (2026-09-23 01:37:44
+0800), which is an ancestor of the repair commit `76b4beb` (01:40:28)
(run 17). All three sentences carry an as-of date on which they were
already false. [Observed] The generalization they introduce ("each one
signed after the first") still holds and is the load-bearing part; the
count is not load-bearing for this package's mechanics, which is why this
is revise and not blocking.

Two things the repair should say when it is redone, because the owner reads
"each one signed after the first must be regenerated" as a complete
procedure and it is not:

1. Regeneration with `--write` repairs the generated `Source:` line only.
   It does not make a sibling's *specification* patch apply. This package's
   patch composes with every one of the four siblings in both orders (run
   17), so nothing here is at risk; but among the siblings, the
   missing-currency patch applied before the scoped-attributes patch makes
   the latter fail at `spec.md:450` in all 60 such five-way orders, and the
   other 60 orders compose to one digest. Under the owner's 2026-09-23
   landing order (`.21 → .30 → .22 → lane B`,
   `POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md:110-129`) lane B
   (scoped-attributes) is last, so whichever package that fifth candidate
   is, it is the one that would need its spec patch re-based, not this one.
   [Observed for the compositions; Inferred for the consequence]
2. That landing order was in the tree at `76b4beb` (`39bc2dc`, 01:24:56)
   and fixes this package's position as third. The packet's "whichever
   package you sign second" (`:210-211`) and the delta's "compose in either
   order" (`:551-552`) are still true as mechanics but now read as though
   the order were open (see F9).

*Resolution:* restate the count as a re-derived figure with its predicate
("candidates under `contracts/candidates/` whose `proposed/spec.md.patch`
targets the PWB `spec.md`: five including this one, at commit X"), or drop
the count and keep only the generalization; wrap the two over-long lines
(`IMPACT-LEDGER.md:121`, `OWNER-DECISION-PACKET.md:209`) at 78 columns.

### F7 — note. The round-2 disposition of F4 points at a section heading that does not exist.

*Criterion 11; rule 5/rule 9 (the same class as F4 itself).*

`SEMANTIC-DELTA.md:638` — "**Accepted and repaired** in 'How this would be
adopted'". `grep -n "^## \|^### "` over the file lists no such heading; the
repaired steps sit under `## Migration / supersession plan` (`:510`). The
string "How this would be adopted" occurs once in the package, at that
line. [Observed] A reader following the disposition to check the repair
finds no section. *Resolution:* name the section that exists.

### F8 — note. The packet says the recorder "registers the chain link"; the recorder it now names says the chain link is not its to add.

*Criterion 12 (what the owner is told an act does); criterion 9.*

`OWNER-DECISION-PACKET.md:187-192` — "a dedicated recorder in the
2026-09-05 shape verifies the phrase against the manifest bytes, applies the
two patches with the builder's `--apply --at-adoption`, confirms every row
now hashes the tree, writes the dedicated record and the aggregate section
of `ACCEPTANCE-ACT-RECORD.md`, and registers the chain link, in one change."
The grammatical subject of "registers" is the recorder. The recorder the
packet names sixteen lines earlier (`:176`,
`scripts/record_pwb_behavior_amendment_acts.py`) says at its docstring
`:31-33` that the successor-chain link and the copy registrations "are the
performing change's to add; this script prints what it knows and edits no
check" (run 12), and the delta's step 6 (`:538-539`) correctly attributes
the link to `check_governance.py` gaining it at adoption. The sentence
predates the repair unchanged; what the repair changed is that it now has a
concrete referent that contradicts it. Nothing in it authorizes anything
and the builder's `--apply` flags exist as named
(`build_pwb_machine_view_amendment.py:408-409`). [Observed] *Resolution:*
"…writes the dedicated record and the aggregate section; the same change
registers the chain link in `check_governance.py`".

### F9 — note. The three ordering sections do not cite the owner's 2026-09-23 landing-order answer, which fixes this package's position.

*Criterion 10; AGENTS.md "A page that restates state it does not own goes
stale silently."*

`OWNER-DECISION-PACKET.md:200-213`, `SEMANTIC-DELTA.md:546-559` and
`IMPACT-LEDGER.md:103-122` present ordering as arithmetic the owner is free
over ("whichever package you sign second"). At `76b4beb` the owner has
answered "Readiness order, lane B last", read as `.21 → .30 → .22 → lane B`
("This fixes order only"), in
`POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md:110-129`, which
also says each later package "is regenerated with its builder's `--write`
against the tree its predecessor's act left, and its packet's quoted digest
updated, before its phrase is offered" — the same rule the package states.
Not false; the package is now silent about a ruled fact the owner will
expect it to acknowledge, and a reader of the packet alone believes the
order is theirs to choose. [Observed for the record; Inferred for the
reading] *Resolution:* one sentence citing that record by path in the
packet's "One more ordering" section; do not restate the order (the record
owns it).

## Criteria with no finding

- **Change class (1), closure (2), two categories (3), parity (4):** the
  proposed text is byte-identical to rounds 1 and 2 (run 3); the patch is a
  pure insertion (`spec.md.patch` has no `-` line other than its `---`
  header). Nothing in the repair diff touches the argument for the class or
  the categories; I re-read the proposed block (`SEMANTIC-DELTA.md:150-182`)
  and the three grounds (`:257-276`) and reach the same reading rounds 1 and
  2 did. Normative stands.
- **`RFC6-21` (5):** the owner has since answered "Narrow (Recommended)"
  (`…OWNER-VALUES…:63`), with the record itself noting the reviewer stays
  free to find otherwise. I re-read item 7 as quoted (`:362-366`, byte-equal
  per round 2) and the `RFC6-21.c2` row (`:385`) and take the narrow
  reading for the reasons rounds 1 and 2 gave: the wrong item 7 names is a
  silent subset; a named, closed, ceilinged member beside an unmodified
  complete machine answer is not that. No `RFC-0006` amendment, no second
  act. [Inferred]
- **Ceiling precondition (6):** no dangling literal (run 18); the existing
  member's ceiling is the registry's `maxMachineResponseBytes`, unchanged.
- **Unchanged boundaries (7):** the eleven subjects are unchanged since the
  baseline (run 4); the coverage matrix regenerates at 324 clauses (run 8);
  no RFC patch in the package.
- **Blast radius (8):** the ledger's baseline table is unchanged since round
  2 re-derived it (121 over 1,334, nine continuation files, set-equal); the
  repair added no citer claim. Not re-run: the figure is stated as the
  baseline table and says so (`IMPACT-LEDGER.md:44-47`).
- **Package mechanics (9):** runs 5, 6, 7, 16. `--check` fails closed on an
  added-line corruption, a transcribed digest and a sibling context
  corruption; CG-7d/7e fail closed on a stale packet copy; nothing binds by
  merge (no act record, no recorder entry, phrase absent from the
  acceptance record: run 9's "0 performed digest(s)").
- **Owner packet (12):** run 15. Nothing reads as authorizing an
  implementation, a route or a registry edit; the phrase is present exactly
  once and stated as not offered; the quoted digest equals `sha256sum` of
  the manifest.

## Open question 6, as a note (not a decision)

The `.18` record holds "what is the 'one named subject' the briefing ceiling
bounds?" for this review, with the drafter's leaning "one claim id" as input
only. What this package's bytes say: the briefing ceiling bounds exactly one
member, the agent briefing view `GET /api/poc/briefing`
(`proposed/spec.md.patch:25-26`), defined only by composition — "values
already reachable from the machine answer at the same evaluation" — and
"served under a byte ceiling of its own". The inserted text gives that route
no parameter, names no claim, no task and no subject, and the package's
prose calls the briefing "task-scoped" in four places
(`SEMANTIC-DELTA.md:136,346,398`; `OWNER-DECISION-PACKET.md:127`) without
saying what a task is. So the package identifies the subject at the level of
*route and evaluation* ("the briefing view's response for one evaluation")
and is silent below that. Whether one response is scoped to one claim id is
not decidable from these bytes; adopting them neither admits nor forecloses
it. [Observed for what the bytes say; the rest is the owner's.]

## Comprehension restatement

Without author context: PWB-REQ-020 gains one inserted block naming two
closed categories of derived, read-only machine view beside the machine
answer. A *derived read-only machine view* composes only from the machine
answer at the same evaluation, mints and writes nothing, is
machine-credentialed in every mount form, subtracts nothing, and every value
it serves must be verified derivable by a checker that imports no rendering
code; members `GET /api/poc/polaris` (under the ceiling the registry already
declares) and `GET /api/poc/briefing` (under a ceiling of its own, not
servable before the registry declares it). A *generated editorial draft
view* composes from one recorded generation run, carries no project-shape
field and is outside the parity comparison; member
`GET /polaris/draft/<runId>`. A route joins either category only by a later
amendment naming it; an unnamed route is in neither and this requirement
says nothing about it. Parity's every limb, scenario and warrant is
unchanged. The owner has already said the drafted values stand (arm (a));
what remains before a phrase is offered is a round that confirms the
repaired prose and a recorder entry, neither of which exists at this
commit. Adoption authorizes no route, no implementation and no registry
edit; the briefing ceiling is a separate act on a separate subject; this
package lands third in the owner's ruled order.

## Verdict

**CONFIRM WITH EXCEPTIONS.**

F3 and F4 are discharged by the bytes at `76b4beb` and their dispositions
are truthful, with every quoted superseded sentence byte-equal to its
`9d74185` source. F5's requested generalization is present in all three
places. The repair diff introduced no quotation drift, no label error and no
transcribed digest; the patches, manifest and quoted digest are
byte-identical to rounds 1 and 2 and every machine check reproduces, with
four mutations caught. The exceptions: the F5 repair states a sibling
count that was false 2 min 44 s before it was committed (F6, revise), a
disposition that cites a heading that does not exist (F7, note), a packet
sentence whose newly named referent disclaims the edit it is credited with
(F8, note), and ordering sections that do not cite the owner's same-day
landing-order answer (F9, note). None changes the change class, the act
count, the proposed bytes or the manifest; none reads as authorizing
anything; F6 is a false sentence on the page the owner reads, which is why
this is CONFIRM WITH EXCEPTIONS and not CONFIRM. Repairing F6–F9 touches
prose only, so the manifest digest above does not move; per rule 10 and
`OWNER-DECISION-PACKET.md:32-34` the repaired bytes carry no confirmation
until a reviewer who did not author them reads them.

`git status --porcelain` in the reviewed checkout: empty (0 lines) before
the review began, and empty (0 lines) again immediately before this file
was written outside it.
