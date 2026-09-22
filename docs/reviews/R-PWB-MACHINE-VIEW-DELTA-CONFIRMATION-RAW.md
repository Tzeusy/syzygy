# Review — PWB machine-view amendment (round 2, confirmation)
Reviewed commit: 9d741859dceee935f256b99ebb68e095545b868b
Manifest SHA-256: 2a49a8d1d473d4347dadda1489488bc6556102c14e98e18bc58688ffeeb3ed6c
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context session, round 2 (confirmation) under CC-REV-1,
CC-REV-4 and CC-REV-6. No authoring context; no commit message body was read
for intent; nothing under `.syzygy/local/` was opened; no other agent was
consulted. Read, in order: `AGENTS.md` in full; the package's
`REVIEW-BRIEF.md`; the round-1 raw
`docs/reviews/R-PWB-MACHINE-VIEW-DELTA-RAW.md`; `SEMANTIC-DELTA.md` §Review;
then the whole package (`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`,
`OWNER-DECISION-PACKET.md`, `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`,
`proposed/spec.md.patch`, `proposed/GOVERNING-DEPENDENCIES.md.patch`) and the
builder `scripts/build_pwb_machine_view_amendment.py`; and, as each criterion
needed it, `RFC-0006` §3 and §4, the signed package's
`contract-coverage-matrix/RFC-0004-0006.md`, the P-68…P-83 ruling record and
the three sibling candidates that patch the same `spec.md`. The detached
checkout at `9d74185` was treated as read-only throughout: no checkout,
commit, add, apply or edit was made inside it. Every mutation ran in a
`cp -r` copy under `scratchpad/review-mv-scratch/base`, restored with
`git checkout --` in that copy after each probe. `git status --porcelain` in
the reviewed checkout was empty before the review began (0 lines) and empty
again before this verdict was written (0 lines; recorded in the final
section).

The instrument for this round is the brief's twelve criteria. The brief's
own sentence "This is the first round" (`REVIEW-BRIEF.md:9-10`) is false at
this commit and is recorded under F3; it does not change the criteria.

---

## What I ran

All commands from the checkout root unless the scratch copy is named. Output
is what I read, not the exit code.

1. `git status --porcelain | wc -l` → `0`. `git rev-parse HEAD` →
   `9d741859dceee935f256b99ebb68e095545b868b`.
2. `sha256sum .syzygy/governance/contracts/candidates/pwb-machine-view-amendment/PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`
   → `2a49a8d1d473d4347dadda1489488bc6556102c14e98e18bc58688ffeeb3ed6c`.
   Computed, not transcribed (rule 3). `grep -n -F` of that value over the
   four package `.md` files: exactly two hits, both in
   `OWNER-DECISION-PACKET.md` (`:23`, the quoted manifest digest, and `:159`,
   the not-offered sign-off phrase). Equal to the round-1 raw's line 3.
3. `python3 scripts/build_pwb_machine_view_amendment.py --check` → exit 0,
   output: "PWB machine-view amendment manifest matches 11 proposed behavior
   subjects (2 patched, 9 unchanged); the dependency declaration is
   regenerated from the proposed spec and the spec patch composes with the
   sibling candidate in either order".
4. `--selftest` → exit 0, output: "selftest: closed population, byte drift,
   path order, subject drift, context-line and added-line patch corruption,
   transcribed and unwarranted dependency declarations, sibling drift and a
   missing sibling patch fail closed".
5. `--diff` → exit 0; stdout captured to a scratch file. Python containment
   test: `proposed/spec.md.patch` bytes are contained in the output (`True`);
   `proposed/GOVERNING-DEPENDENCIES.md.patch` bytes are contained (`True`);
   after removing both, the remainder is empty. The one advisory line ("note:
   the dependency declaration patch is generated from the proposed spec.md
   bytes and is order-dependent against the sibling candidate; regenerate
   with --write after either package lands") is printed on stderr, not in
   either stored patch.
6. **Byte identity between `02b6ebc` and `9d74185`** (`git rev-parse
   <commit>:<path>` blob ids, compared):
   - `proposed/spec.md.patch` — `d492e23087e84694f26e0c7e3d7f7321a9ba463a`
     at both: IDENTICAL.
   - `proposed/GOVERNING-DEPENDENCIES.md.patch` —
     `156b285074040e8eb4c372cc9247a2853cf0c22d` at both: IDENTICAL.
   - `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` —
     `c76599ab25854dbbe82a1c2d1b9624ac0538159a` at both: IDENTICAL.
   - `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`, `REVIEW-BRIEF.md` and
     `scripts/build_pwb_machine_view_amendment.py`: IDENTICAL (each blob
     id equal at both commits; only `SEMANTIC-DELTA.md` differs).
   - `git diff --stat 02b6ebc 9d74185 -- <package dir>
     scripts/build_pwb_machine_view_amendment.py` → exactly one file,
     `SEMANTIC-DELTA.md`, `84 insertions(+), 6 deletions(-)`.
   [Observed] The repair moved prose only; the dispositions' sentence "no
   patch byte moved" (`SEMANTIC-DELTA.md:578-579`) and "byte-identical to the
   reviewed commit" (`:586-590`) are true.
7. **The whole-tree diff** `git diff --stat 02b6ebc 9d74185` → 39 files.
   Besides this package's `SEMANTIC-DELTA.md`, the interval added three new
   sibling candidates under `contracts/candidates/`
   (`pwb-exact-source-render-mode-scenario/`, `pwb-opening-band-scenario/`,
   `pwb-registry-currency-briefing-amendment/`), their three builders, +139
   lines in `scripts/check_governance.py`, +24 lines in
   `.github/workflows/governance-docs.yml`, `PROJECT-STATUS.md`, `AGENTS.md`,
   a retention-posture decision packet and seven retained raws (including
   round 1 of this package). `git diff --stat a4a3451 9d74185 --
   openspec/changes/polaris-project-wide-butlers-model/` → empty: none of the
   eleven subjects moved since the ledger's baseline. `git diff --stat
   02b6ebc 9d74185 -- …/pwb-scoped-attributes-amendment/` → empty.
8. **Repair quotations, byte-for-byte** (rule 8). Python equality of the
   delta's fenced quotation at `SEMANTIC-DELTA.md:361-363` against
   `RFC-0006-cross-surface-selection-query-drawer.md` lines 524-526 →
   `True`; of the delta's fenced row at `:383` against
   `contract-coverage-matrix/RFC-0004-0006.md` line 234 → `True`. The delta's
   line range "524-526" is exact (item 7 begins at line 524; the round-1 raw
   had cited 525-526, which starts one line late — the repair corrected the
   anchor rather than copying it).
9. `python3 scripts/check_governance.py` → last line "32 OK, 20 WARN, 0 FAIL
   (52 checks) — counts derived, not asserted". The only lines naming this
   package are informational: "[subject] SIGN OFF PWB MACHINE-VIEW AMENDMENT
   — 1 quotation(s), 0 finding(s), 0 performed digest(s)" and "[registered]
   …/pwb-machine-view-amendment/OWNER-DECISION-PACKET.md — declares 1 current
   and 0 performed-history act(s); 1 current, 0 historical valid". The 20
   WARNs are unrelated to this package (CG-27 `decisions/README.md` rows,
   CG-24 fixture coverage, CG-25 downgrades). `--selftest` → "261 fixtures,
   0 failing — a check that cannot fail is not a check".
10. `python3 scripts/build_polaris_project_wide_contract_coverage.py --check`
    → "Polaris consequence matrix matches regeneration — 324 clauses
    represented", exit 0 (the "does NOT change" item 9 figure).
11. **Dependency regeneration, independently** (criterion 9). In a temp
    dir: GNU `patch` applied `proposed/spec.md.patch` to the current
    `spec.md` and `proposed/GOVERNING-DEPENDENCIES.md.patch` to the current
    `GOVERNING-DEPENDENCIES.md`; then
    `build_polaris_project_wide_spec_dependencies.generate()` over the patched
    spec text. Output: `errors: []`; `independently-generated == proposed
    GOVERNING-DEPENDENCIES.md.patch result: True`; patched spec sha256
    `f57c37a8ae8fd287b9b3a807a6d641be327dbbffc13ec370de950bde2d23e2f8`, equal
    to the manifest's `spec.md` row (`PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt:18`)
    and to the `Source:` line the dependency patch writes
    (`proposed/GOVERNING-DEPENDENCIES.md.patch:10`); generated counts
    `('17', '96')`, matching `SEMANTIC-DELTA.md:32-33`.
12. **Blast radius re-derived** (criterion 8) at the ledger's stated baseline
    `a4a34510a5582edbd38c1df57a064ba3ac0a33f2`, via `git ls-tree -r -z
    --name-only` (denominator **1334**) and `git show <base>:<path>` per
    file: full form `PWB-REQ-020\b` → **112** files; the ledger's own
    continuation regex plus a `..` range form → **9** continuation-only files,
    listed and equal to `IMPACT-LEDGER.md:30-38` one for one; total **121**.
    Method 2, `git grep -l -F PWB-REQ-020 a4a3451` → 112, set-equal to method
    1's full-form set. My 121-file set is set-equal to the ledger's "Every
    citing file" enumeration (121 entries, symmetric difference `[]`).
13. **Composition, independent tool** (criterion 10). GNU patch 2.7.6 in the
    scratch copy over the current `spec.md` (sha256
    `42d073cdeaf7fa7940c5e822b05213267ec1d0064faaaad092f21d264b76a2b1`):
    - scoped-attributes then machine-view, and the reverse: both apply with
      0 rejects; both yield
      `37737cc0ce0ae2c654448cfc5f003e4e3592cd1673d572de4d87e1fd75b60d50`
      (the round-1 figure, reproduced).
    - all 24 orders of the four candidate `spec.md.patch` files now in the
      tree (scoped-attributes, machine-view, exact-source-render-mode,
      opening-band): every order applies with 0 rejects and every order
      yields the single digest
      `4334e7dca5f394ad5b1fef560be7b13e8176a6e52c7768b9746f3d57eb0ed0a8`.
      See F5.
14. **Rule-6 mutations**, each in the scratch copy, restored after
    (`git status --porcelain | wc -l` → `0` after each restore):
    - **A — corrupt one added line of `proposed/spec.md.patch`** (line 30,
      `sends no source or draft byte outside` → `sends one source or draft
      byte outside`; `git diff --stat` in the scratch: 1 file, 1 insertion,
      1 deletion). `--check` → exit 1:
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
      (`sed s///g`, last hex digit `c` → `d`; 2 occurrences rewritten).
      `check_governance.py` → "31 OK, 19 WARN, 2 FAIL (52 checks)". CG-7d
      fired on `OWNER-DECISION-PACKET.md:159` ("…but
      …/PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt hashes to [the current digest]
      and …/ACCEPTANCE-ACT-RECORD.md records no performance of that argument
      — this copy is stale"); CG-7e fired on the same file ("declared to
      carry act `SIGN OFF PWB MACHINE-VIEW AMENDMENT` and does not contain its
      current argument … The copy in this file is stale, and this file is one
      the owner is sent to"). The registration the delta's migration step 3
      describes as future is therefore already live — see F4.
15. Read-only checks behind criteria 6 and 12: `maxBriefingResponseBytes`
    occurs **0** times in
    `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
    and 0 tracked files under `.syzygy/governance/declarations/` name it; the
    sibling `pwb-registry-currency-briefing-amendment/proposed/*.json.patch`
    adds it (`+ "maxBriefingResponseBytes": 20480`, patch line 27), so the
    delta's `:25-27` sentence about that sibling is now true of a file in the
    tree. No recorder for this act exists (`grep -rl MACHINE-VIEW scripts/`
    → only the builder and `check_governance.py`); no
    `decisions/PWB-MACHINE-VIEW-AMENDMENT-ACT.md`; `ACCEPTANCE-ACT-RECORD.md`
    contains the phrase 0 times. P-72 and P-76 rows read at
    `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:60,62`, both arm A,
    matching `SEMANTIC-DELTA.md:409-414`.
16. Stale-sentence sweep, `grep -n -i -E "first round|first draft|no review
    has been run|no reviewer|not yet assigned|no verdict|has run no
    review|no fresh-context review"` over the four package `.md` files → 8
    hits, all enumerated under F3.
17. Registration and CI timing: `git show 02b6ebc:scripts/check_governance.py
    | grep -c PWB_MACHINE_VIEW` → 0; at `9d74185` → 12
    (`check_governance.py:1542-1547`, `:2054`, `:2269`). `git show
    02b6ebc:.github/workflows/governance-docs.yml | grep -c
    build_pwb_machine_view_amendment` → 0; at `9d74185` →
    `governance-docs.yml:118-122` and `PROJECT-STATUS.md:254-255` run
    `--check` and `--selftest`. Neither the packet nor the delta was updated
    for this — see F4.

---

## F1 — DISCHARGED. The `RFC6-21` disclosure now carries both pieces of evidence.

*Round-1 anchor:* `SEMANTIC-DELTA.md:335-357` at `02b6ebc`. *Repair:*
`SEMANTIC-DELTA.md:354-392` at `9d74185`.

- **Item 7 quoted.** `:354-364` quotes `RFC-0006` § "Violation cases" item 7
  in full inside a fence, anchored to lines 524-526. Byte-equal to the source
  (run 8). [Observed]
- **Distinction stated.** `:366-374` gives the silent-versus-named
  distinction the round-1 finding asked for, marks the conclusion
  `[Inferred]`, and tells a reviewer who reads item 7 wide where the wide
  reading is stated (`:394-401`). This is the resolution round 1 named,
  neither more nor less. [Observed]
- **Coverage row quoted.** `:376-392` quotes the `RFC6-21.c2` row inside a
  fence, anchored to `RFC-0004-0006.md` line 234; byte-equal to the source
  (run 8); names it "prior art for this disclosure, not a new position"; and
  ties it to "does NOT change" item 9 (`:326-331`) with a stated reason the
  delta does not reconcile ("marking a signed `unknown-uncovered` row covered
  … is an owner's act over the contract, not a drafter's"). [Observed]
- **Conclusion unchanged.** The narrow reading is still taken and still
  disclosed rather than resolved; the act count is unchanged; no patch byte
  moved (run 6). I re-read `RFC6-21` (`RFC-0006…md:382-386`) and item 7 this
  round and reach the same place round 1 did: item 7's wrong is an
  undisclosed subset presented as the answer at one selection across two
  surfaces; a category-1 member is named, closed, ceilinged and leaves the
  complete set on the unmodified machine answer. The narrow reading is
  defensible. [Inferred] No `RFC-0006` amendment and no second act follow
  from this package (criterion 5).
- **Disposition text truthful.** `:572-579` says item 7 "is now quoted in
  full with the silent-versus-named distinction stated" and the row "is now
  quoted as existing treatment of the same question" — both true of the
  bytes; "no patch byte moved" — true (run 6). [Observed]

Criteria 5 and 11.

## F2 — DISCHARGED. Ground 3 is marked, not dropped, and says what it is.

*Round-1 anchor:* `SEMANTIC-DELTA.md:264-267` at `02b6ebc`. *Repair:*
`SEMANTIC-DELTA.md:266-274` at `9d74185`.

Ground 3's heading now reads "the weakest of the three, and not
dispositive"; the body says the reading it narrows against "was always
strained", that the current Observable and Oracle "never enumerate those
fields as in-scope", that the ground "may formalize an already-implicit
exclusion rather than newly narrow one [Inferred]", and that "Grounds 1 and 2
each satisfy the template's test on their own, and the classification does
not rest on this one". That is the marking arm of round 1's either/or
resolution. The class stays Normative (`:39-42`, `:279-280`); grounds 1 and 2
are unchanged and I re-tested them against the quoted current text
(`:83-126`): the derivability obligation (`:159-161` of the proposed text)
binds the one served member, whose route test has no such oracle (packet
`:42-44`, ledger `:85`, both [Observed] and unchanged since round 1 — no
`apps/` file moved in the interval, run 7); the ceiling precondition
(`:176-177`) binds a route that does not yet exist. Both satisfy "someone who
complied before may not comply now". [Inferred] The disposition text
(`:580-584`) — "marking, not dropping … grounds 1 and 2 independently carry
the classification. The class stays Normative" — is true of the bytes.

Criteria 1 and 11.

---

## New findings

### F3 — revise (non-blocking). Five sentences in the package say no review has happened; the same package records the round-1 verdict.

*Criteria 11 and 12; AGENTS.md "Mark staleness at the stale sentence".*

At `9d74185` the package carries, unedited from `02b6ebc`:

- `OWNER-DECISION-PACKET.md:8-9` — "Date: 2026-09-21 (first draft; no review
  has been run against these bytes, and no verdict exists for them)." The
  packet's bytes are blob-identical to `02b6ebc` (run 6), which the round-1
  raw read in full (its run 17) and returned `CONFIRM WITH EXCEPTIONS` over.
  False at this commit. [Observed]
- `OWNER-DECISION-PACKET.md:163` — "no fresh-context review has confirmed
  these bytes". A fresh-context review has confirmed them with exceptions;
  the reason the phrase is not offered is now rule 10 over the *repaired*
  delta bytes (which `SEMANTIC-DELTA.md:563-568` states correctly) and the
  absence of a recorder (the second half of `:163-164`, still true, run 15).
  The stated reason is the wrong one. [Observed]
- `OWNER-DECISION-PACKET.md:137-139` — arm (a) "Yes — send it to
  fresh-context review as drafted … only then is a sign-off phrase offered".
  The owner is asked to authorize a step the tree shows already taken; a
  reader of arm (a) alone cannot tell that round 1 ran, was dispositioned,
  and that the repairs are what this round confirms. [Observed]
- `SEMANTIC-DELTA.md:44-45` — "**Author:** … No reviewer has seen these
  bytes." and `:555-557` — "**Reviewer:** not yet assigned. … this draft's
  author has run no review of it and has written none." The second sits four
  lines above "**Verdict of record:** `CONFIRM WITH EXCEPTIONS`, copied
  exactly from `docs/reviews/R-PWB-MACHINE-VIEW-DELTA-RAW.md`" (`:559-561`).
  A reviewer was assigned and did produce that raw. Internally
  contradictory. [Observed]
- `REVIEW-BRIEF.md:9-10` — "This is the first round. No review has been run
  against these bytes and no verdict of any kind exists for them." False at
  this commit (already acknowledged by the dispatch; recorded here so the
  sweep is complete). [Observed]

None of these authorizes anything, and each errs on the side of understating
progress, which is why this is revise and not blocking: criterion 12's own
tests hold (phrase present at `:159`, stated "not offered" at `:163`; `:3-6`
and `:150-152` say a commit, merge, review, manifest or silence performs
nothing; no sentence authorizes an implementation, a route or a registry
edit — `grep -n -i "authoriz\|implement"` over the packet returns only
negations). But the packet is the page the owner reads, and its two stale
sentences give the owner a false account of where the package stands.
*Resolution:* mark each sentence at the sentence, keeping the superseded text
quoted and dated (the repository's own CG-27 lesson), or reword `:8-9`,
`:137-139` and `:163` to state the round-1 verdict and this round's status.
Note that `OWNER-DECISION-PACKET.md:25-27` says changing the packet after
the review retires the review; the packet is not a manifest row, so the
manifest digest does not move, but the packet edit will need this round's
successor to re-read it.

### F4 — revise (non-blocking). Migration step 3 points at a list the packet does not contain, and steps 3 and 6 describe as future what the tree at this commit has already done.

*Criterion 11 (a fresh reader restating what adoption does) and criterion
9 (package mechanics); rule 5 / rule 9 on citations.*

- `SEMANTIC-DELTA.md:518-520` — "**Registration** of the act phrase and its
  packet digest copies in `scripts/check_governance.py` before the act
  exists, so CG-7d can see a stale copy. The three edits are listed in
  `OWNER-DECISION-PACKET.md`." `grep -n -i -E
  "check_governance|three edits|CG-7"` over `OWNER-DECISION-PACKET.md` → no
  hits. The packet lists no such edits. This sentence was already false at
  `02b6ebc` (packet identical, run 6); round 1 did not catch it. [Observed]
- The registration itself is done: `check_governance.py:1542-1547` define
  `PWB_MACHINE_VIEW_LABEL/DIR/SUBJECT/ACT`, `:2054` enters the subject,
  `:2269` registers the packet as a digest copy (0 hits at `02b6ebc`, 12 at
  `9d74185`, run 17) — and mutation C (run 14) shows CG-7d and CG-7e both
  fire on a stale copy today. Step 3 is not a future step. [Observed]
- `SEMANTIC-DELTA.md:528-532` — step 6, "At adoption … `check_governance.py`
  and the CI workflow gain this package's `--check` and `--selftest`." The
  hosted workflow already runs both (`governance-docs.yml:118-122`) and the
  PROJECT-STATUS battery already lists both (`PROJECT-STATUS.md:254-255`),
  since the interval between the two commits. `check_governance.py` does not
  run the builder and is not described as doing so elsewhere, so the
  step-6 sentence is half stale (the workflow) and half unclear (what
  `check_governance.py` would "gain"). [Observed]

Nothing here affects the manifest, the patches or the change class; it is a
plan section whose ground moved under it and a cross-reference that never
resolved. *Resolution:* delete or correct the "three edits are listed"
sentence; mark steps 3 and 6 as performed at the sentence, with the commit
that performed them, or restate them as "already in place".

### F5 — note. The sibling population is three, not one, and the ordering advice is written for two.

*Criterion 10.*

`SEMANTIC-DELTA.md:536-546`, `IMPACT-LEDGER.md:103-118` and
`OWNER-DECISION-PACKET.md:185-195` each say *the* sibling candidate
(`pwb-scoped-attributes-amendment/`) is pending against the same eleven
subjects and that "whichever package the owner signs second must be
regenerated". At `9d74185` three candidates besides this one carry a
`proposed/spec.md.patch` and a `proposed/GOVERNING-DEPENDENCIES.md.patch`
over the same subjects (scoped-attributes, exact-source-render-mode-scenario,
opening-band-scenario; run 7), and the builder's `--check` composes against
scoped-attributes only (`build_pwb_machine_view_amendment.py:59,188-192`).
What is written is true of the two it names — the two-way composition
reproduces to the round-1 digest in both orders (run 13) — and the
generalization holds empirically: all 24 four-way orders apply with 0
rejects to one digest (run 13). But no builder verifies that four-way claim,
and the advice an owner needs is "every package signed after the first must
be regenerated with `--write` against the tree the previous one left", not
"whichever you sign second". Not false; incomplete for the reader it is
addressed to. [Observed for the composition; Inferred for the reading]
*Resolution (optional):* one sentence in the packet's "One more ordering"
naming the sibling count as of a date and generalizing "second" to "each
later one".

## Criteria with no finding

- **Change class (1), closure (2), two categories (3), parity (4):** the
  proposed text is byte-identical to round 1 (run 6); round 1's readings
  were re-tested against the quoted current and proposed text and hold. The
  patch is a pure insertion (`spec.md.patch` has no `-` line other than its
  `---` header; run 6's blob identity plus a read of `:5-45`).
- **`RFC6-21` (5):** decided under F1 — narrow reading defensible, no second
  act.
- **Ceiling precondition (6):** no dangling literal (run 15: 0 occurrences of
  the field name in `spec.md`, in the patch and under `declarations/`); the
  existing member's ceiling is declared already (`routes.ts` unchanged since
  round 1, run 7).
- **Unchanged boundaries (7):** the eleven subjects are unchanged since the
  baseline (run 7); the coverage matrix regenerates at 324 clauses (run 10);
  no RFC patch in the package.
- **Blast radius (8):** 121 over 1,334 re-derived by two methods with the
  nine continuation files and the full enumeration set-equal (run 12). The
  dated table at `SEMANTIC-DELTA.md:62-69` ("What is true today,
  2026-09-21") has drifted at `9d74185` — `/api/poc/briefing` 12 → 17
  tracked files, `/polaris/draft` 4 → 9, `maxBriefingResponseBytes` 7 → 18,
  the growth being the new candidates and raws — but it carries its as-of
  date and its load-bearing cell ("No registry file") is still true (0 under
  `declarations/`). Not a finding.
- **Package mechanics (9):** runs 3, 4, 5, 11 and 14. The manifest hashes
  the post-apply bytes; the declaration is regenerated, not transcribed;
  `--check` fails closed on added-line corruption and on a transcribed
  digest; CG-7d/7e fail closed on a stale packet copy; nothing binds by merge
  (no act record, no recorder, phrase absent from the acceptance record; run
  15).
- **Owner packet (12):** criterion's own tests hold (see F3 for the stale
  sentences around them). The digest quoted at `:23` and `:159` equals the
  file the builder writes (run 2).

## Comprehension restatement

Without author context: PWB-REQ-020 gains one inserted block naming two
closed categories of derived, read-only machine view beside the machine
answer. A *derived read-only machine view* is composed only from the machine
answer at the same evaluation, mints and writes nothing, is
machine-credentialed in every mount form, subtracts nothing, and every value
it serves must be verified derivable by a checker that imports no rendering
code; members are `GET /api/poc/polaris` (under the ceiling the registry
already declares) and `GET /api/poc/briefing` (under a ceiling of its own,
which may not be served before the registry declares it). A *generated
editorial draft view* is composed from one recorded generation run, carries
no project-shape field and so is outside the parity comparison; member
`GET /polaris/draft/<runId>`. A route joins either category only by a later
amendment naming it; an unnamed route is in neither and this requirement says
nothing about it. Parity itself — every limb, scenario and warrant — is
unchanged. The owner is being asked whether this drafted realization of P-72
arm A and P-76 arm A is what they ruled; adoption authorizes no route, no
implementation and no registry edit, and the briefing ceiling is a separate
act on a separate subject.

## Verdict

**CONFIRM WITH EXCEPTIONS.**

F1 and F2 are discharged by the bytes at `9d74185`, and the dispositions
describe the repairs truthfully. The repair diff introduced no new false
sentence, no quotation drift (both quotations byte-equal to their sources),
no label error, and no transcribed digest; the patches, manifest and quoted
digest are byte-identical to the round-1 commit and every machine check
reproduces. The exceptions are the package's own stale self-description (F3),
a cross-reference that never resolved and two plan steps the tree has already
performed (F4), and an ordering section written for one sibling where there
are now three (F5). None changes the change class, the act count, the
proposed bytes or the manifest; none reads as authorizing anything; all three
are sentences the owner or a fresh reader would be misled by, which is why
this is CONFIRM WITH EXCEPTIONS and not CONFIRM. Repairing F3 and F4 touches
`OWNER-DECISION-PACKET.md` and `SEMANTIC-DELTA.md` only, so the manifest
digest above does not move; per rule 10 and `OWNER-DECISION-PACKET.md:25-27`
those repaired bytes carry no confirmation until a reviewer who did not
author them reads them.

`git status --porcelain` in the reviewed checkout: empty (0 lines) before
the review began, and empty (0 lines) again immediately after this file was
written outside it.
