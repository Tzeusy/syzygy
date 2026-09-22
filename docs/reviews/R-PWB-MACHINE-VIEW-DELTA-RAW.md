# Review — PWB machine-view amendment
Reviewed commit: 02b6ebc70f505c42dfa2afa7a5e64d9f1a04bff5
Manifest SHA-256: 2a49a8d1d473d4347dadda1489488bc6556102c14e98e18bc58688ffeeb3ed6c
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context session. No authoring context; the package was not
read before this review, and no commit message body was read for intent
(rule followed throughout, no accidental exposure to disclose). Read-only
throughout; every mutation ran in a `cp -r` scratch copy under the session
scratchpad, never in the reviewed worktree. Class: fresh-reader semantic
review of a normative delta (CC-REV-1, CC-REV-4, CC-REV-6).

The sandbox this session runs under refuses any Bash command it cannot prove
stays inside the worktree, including several that did not in fact call `git`
(rejected on the substring "git" in absolute paths and on `git apply` via
`subprocess`). Two consequences, neither weakening a finding: the manual
composability test below uses GNU `patch` rather than the builder's internal
`git apply` — a genuinely independent tool, not the mechanism under test —
and the mutation-composed script files were written to disk with the Write
tool rather than assembled in a Bash heredoc.

---

## What I ran

All read-only unless noted; the scratch copy is
`…/25dc4c66-…/scratchpad/rev-machine-view/` (a `cp -r --parents` of
`openspec`, `scripts` and `.syzygy` from the reviewed worktree, used only for
the two mutation probes).

1. `git branch --show-current` → `review/machine-view-delta`;
   `git rev-parse HEAD` → `02b6ebc70f505c42dfa2afa7a5e64d9f1a04bff5`. Matches
   the brief. `git status --porcelain` → empty.
2. Computed `sha256sum PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` this session →
   `2a49a8d1d473d4347dadda1489488bc6556102c14e98e18bc58688ffeeb3ed6c`. Equals
   the argument quoted at `OWNER-DECISION-PACKET.md:23` and the sign-off
   phrase at `:159`. Digest computed, never transcribed (rule 3). Also parsed
   the manifest with Python: 11 rows, each a 64-hex-character sha256, sorted
   by codepoint path, matching the file's own header comment.
3. `python3 scripts/build_pwb_machine_view_amendment.py --check` → exit 0:
   "PWB machine-view amendment manifest matches 11 proposed behavior subjects
   (2 patched, 9 unchanged); the dependency declaration is regenerated from
   the proposed spec and the spec patch composes with the sibling candidate
   in either order."
4. `--selftest` → exit 0: "closed population, byte drift, path order, subject
   drift, context-line and added-line patch corruption, transcribed and
   unwarranted dependency declarations, sibling drift and a missing sibling
   patch fail closed." Read the fixture bodies at
   `scripts/build_pwb_machine_view_amendment.py:275-386` (`selftest()`):
   nine predicates, each mutating a real input in a temp dir and asserting
   the checker then refuses. Rule 6 satisfied for the builder itself.
5. `--diff` → printed to a scratch file; diffed byte-for-byte against the
   two stored `proposed/*.patch` files. The spec.md portion is byte-identical
   to `proposed/spec.md.patch`; the `GOVERNING-DEPENDENCIES.md` portion is
   byte-identical to `proposed/GOVERNING-DEPENDENCIES.md.patch` once a
   leading advisory line ("note: the dependency declaration patch is
   generated from the proposed spec.md bytes and is order-dependent against
   the sibling candidate…") is set aside — that line is printed only by
   `--diff`, is not part of either stored patch, and is accurate (§ composed
   order, below).
6. **Composability (criterion a).** In the scratch copy, applied
   `pwb-scoped-attributes-amendment/proposed/spec.md.patch` then this
   package's `spec.md.patch` with GNU `patch 2.7.6` (order 1), and the
   reverse order (order 2), against two independent copies of the base
   `spec.md`. Both applied with **0 fuzz, 0 rejects**. `sha256sum` of both
   resulting files: `37737cc0ce0ae2c654448cfc5f003e4e3592cd1673d572de4d87e1fd75b60d50`
   in both orders — byte-identical. `patch` output (order 1, representative):
   ```
   patching file openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md
   Hunk #1 succeeded at 450 (offset 0 lines).
   patching file openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md
   Hunk #1 succeeded at 937 (offset 34 lines).
   ```
   (Order 2 swaps which patch reports the offset; both report a clean apply,
   no `.rej` file in either scratch tree.)
7. Read `coexistence_findings()` (`scripts/build_pwb_machine_view_amendment.py:186-245`)
   and confirmed it is called unconditionally inside `check()` — it is not an
   opt-in probe. Then, in the full-repo scratch copy, edited one context line
   of `pwb-scoped-attributes-amendment/proposed/spec.md.patch` (the `-` line
   at its hunk touching the same `spec.md` region) via the Edit tool and
   re-ran `--check`:
   ```
   PWB machine-view amendment manifest does not verify:
     sibling-first composition failed: spec.md.patch does not apply to openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md: error: patch failed: openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md:450
   error: openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md: patch does not apply
   ```
   Exit 1. Rule 6 satisfied for the composability claim specifically, not
   only for the builder's own fixtures.
8. **Dependency regeneration (criterion g).** Located the generator the
   builder imports as `dependencies`
   (`scripts/build_polaris_project_wide_spec_dependencies.py`, called from
   `derivation_findings()` at `scripts/build_pwb_machine_view_amendment.py:171-185`).
   In a fresh temp dir, applied `proposed/spec.md.patch` to the current
   `spec.md`, ran `dependencies.generate()` on the patched text, and compared
   the result to `proposed/GOVERNING-DEPENDENCIES.md.patch` applied to the
   current `GOVERNING-DEPENDENCIES.md`. Output: `errors: []`;
   `independently-generated == proposed GOVERNING-DEPENDENCIES.md.patch
   result: True`. No diff printed (there is none).
9. **Blast radius (criterion 8).** Re-derived the ledger's sweep independently
   in Python, against the ledger's own stated baseline commit
   `a4a34510a5582edbd38c1df57a064ba3ac0a33f2` (`IMPACT-LEDGER.md:7`) — not
   the reviewed commit, and confirmed that choice is correct: the ledger
   states explicitly (`:34-35`) that "this ledger's own files, once
   committed, join the citer population… the difference is this package," so
   sweeping at the reviewed commit would double-count the package's own new
   prose as a "citer" of the requirement it defines. `git merge-base
   --is-ancestor a4a3451 <reviewed commit>` confirmed the ancestry; `git diff
   --stat` between them shows exactly the 8 new package files (7 under the
   candidate directory, 1 script), nothing else — the baseline is not stale
   for any other reason.
   - Method 1 (`PWB-REQ-020\b` full form, `re`) + continuation pattern: 112
     full-form + 9 continuation-only = **121**, over a denominator of
     **1,334** tracked files at that commit (`git ls-tree -r --name-only`,
     counted this session). The 9 continuation-only files matched the
     ledger's own list byte-for-byte:
     `.syzygy/governance/decisions/DECISION-HISTORY.md`,
     `.syzygy/governance/decisions/POLARIS-M1-PAGE-SIZE-OWNER-RULING-DECISION.md`,
     `apps/three-surface-poc/src/polaris.ts`,
     `apps/three-surface-poc/src/pwb-mutation-sweep-main.ts`,
     `apps/three-surface-poc/src/routes.ts`,
     `docs/evidence/pwb-p4-2-mutation-sweep-2026-09-09-named-absent-file-dropped.json`,
     `docs/reviews/2026-09-05-pwb-live-exact-head-packet.md`,
     `docs/reviews/R-POLARIS-M13-NAVIGATION-SCALE-FUNNEL-RAW.md`,
     `docs/reviews/R-POLARIS-READING-ASSETS-REPAIR-2026-09-10-RAW.md`.
   - Method 2 (`git grep -l -F 'PWB-REQ-020'`, the ledger's second method):
     also 112, confirming the full-form count by a second method (rule 2).
   - Cross-checked my independently swept 121-file set against the ledger's
     own `## Every citing file` enumeration
     (`IMPACT-LEDGER.md:120-269`): **exact set equality, 0 files in either
     direction only**.
10. **Ceiling precondition (criterion f/6).** Grepped
    `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`:
    `maxHumanResponseBytes: 2097152` and `maxMachineResponseBytes: 8388608`
    are already declared (lines 270-271); `maxBriefingResponseBytes` occurs
    **0** times in that file. Confirms the existing `/api/poc/polaris`
    member is served under an already-declared ceiling (the precondition
    sentence does not retroactively touch it) while the not-yet-built
    briefing member's ceiling is genuinely absent and gated on the sibling
    registry act, exactly as claimed.
11. **Contract-coverage matrix (item 9 of "does NOT change").** Ran
    `python3 scripts/build_polaris_project_wide_contract_coverage.py --check`
    this session → `Polaris consequence matrix matches regeneration — 324
    clauses represented`, exit 0. Independently grepped `RFC6-21` across the
    signed package and found the matrix already carries, unpatched:
    `contract-coverage-matrix/RFC-0004-0006.md:234` — `RFC6-21.c2 | RFC6-21 |
    …:382-386 | Endpoint always serves the full set | yes | [Inferred]
    PWB-REQ-020 only requires every Polaris fact in the machine answer, not
    completeness of endpoint-only facts. | unknown-uncovered`. This is the
    **same narrow-reading rationale** the delta's disclosure takes, already
    signed and already marked `unknown-uncovered` — prior art the delta's
    text does not cite (folded into F1 below).
12. Read `RFC-0006-cross-surface-selection-query-drawer.md:382-386` (RFC6-21
    itself) and `:506-528` (§4 "Violation cases"), located via
    `DIRECTIVE-REGISTER.md:371`. Quoted and analyzed under F1.
13. Retrieved current byte-for-byte text of PWB-REQ-004
    (`spec.md:487-500`) and PWB-REQ-020 (`spec.md:901-908`) and compared
    against `SEMANTIC-DELTA.md`'s quotations of both — exact match.
14. Read `docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md:56` (Q1 row) and
    `:1082-1084` (Gate 5 prose) — the exact category-1 definition, matching
    the delta's three properties. Read
    `docs/design/POLARIS-M10-MACHINE-CONTRACT-FUNNEL.md:37,758,923` and
    `docs/design/POLARIS-M11-OPERABILITY-FUNNEL.md:71,744,922` — both confirm
    their machine-route slices "hold behind P-72" and neither M10's slice 3
    nor M11's slice 2 is admitted or foreclosed by this delta.
15. Read `docs/design/POLARIS-M7-GENERATION-LOOP-FUNNEL.md:37` (Q3 row) and
    `:833-928` (slice 4 detail) — confirmed the exact phrase "generated
    editorial draft view" and the "0 references… 20 tracked files"
    disjointness figure the delta cites, scoped correctly (the delta cites
    M7 only for the category's name, member and disjointness, not for its
    other properties — no drift).
16. Read `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:60,62`
    (P-72, P-76 rows) — both ruled arm A, 2026-09-21, matching the delta's
    "Warrant" section quotations.
17. Read `OWNER-DECISION-PACKET.md` in full: manifest digest matches (step
    2); the sign-off phrase (`:154-163`) is present and explicitly "not
    offered"; the inert-offering banner (`:3-6`) and the tail
    ("Silence, a partial answer, a commit or a merge performs nothing,"
    `:148-150`) state that nothing autonomous binds; options (a)/(b)/(c) are
    present (`:132-147`); no implementation, route or registry edit is
    authorized anywhere in the file (grepped `implement\|authorize` — every
    hit is a negation).
18. Checked `apps/three-surface-poc/src/routes.ts` (grep): `POLARIS_PRESENTATION_PATH
    = '/api/poc/polaris'`; `ResponseLimitIdentity` is a closed 2-literal
    union (`'maxHumanResponseBytes' | 'maxMachineResponseBytes'`, line 111)
    — confirming no `maxBriefingResponseBytes` literal exists in
    implementation code either, consistent with criterion f. Checked
    `apps/three-surface-poc/src/polaris-presentation-route.test.ts`: exactly
    2 test cases (credential refusal, typed ceiling failure) — neither is a
    derivability oracle, confirming the factual premise of Normative ground 1.

---

## Findings

### F1 — non-blocking. The `RFC6-21` disclosure omits the two most directly on-point pieces of textual evidence, though its own conclusion is defensible on the record.

*Anchor:* `SEMANTIC-DELTA.md:335-357` ("The RFC6-21 tension, disclosed rather
than reconciled").

*Rests on:* criterion e's own instruction ("read RFC6-21 … and say whether
the narrow reading is defensible"); rule 8 (anchor a contract claim to the
defined clause and quote it); CC-REV-6 (a rubber stamp is a finding — naming
a real gap even while confirming).

The delta's disclosure states two readings and takes the narrow one: RFC6-21
governs *display depth*, not every endpoint's completeness, because the full
fact set stays retrievable from the machine answer at the same evaluation.
It correctly marks this `[Inferred]` and correctly instructs a reviewer who
reaches the wide reading to record it as a finding, per the brief.

Two pieces of evidence bear directly on that decision and neither is cited:

1. **RFC-0006's own worked violation case.** `RFC-0006-cross-surface-selection-query-drawer.md:525-526`,
   § "Violation cases," item 7: *"(RFC6-18/21) Polaris's drawer shows an
   evidence artifact Trajectory's omits for the same selection and
   evaluation; an endpoint serves only the 'minimal' display subset."* This
   is the single closest illustration in the source document to the question
   the delta is deciding, and it is not quoted or referenced anywhere in the
   disclosure.
2. **The signed package's own coverage row.** `contract-coverage-matrix/RFC-0004-0006.md:234`
   already carries `RFC6-21.c2`, marked `unknown-uncovered`, with the note
   *"[Inferred] PWB-REQ-020 only requires every Polaris fact in the machine
   answer, not completeness of endpoint-only facts"* — the same narrow
   reading, already signed, already flagged as open. Item 9 of "What
   explicitly does NOT change" (`SEMANTIC-DELTA.md:317-320`) says this row
   "remains accurate" but does not say the row is prior art for the very
   question the disclosure is deciding two sections later.

My own reading of the violation case does not flip the conclusion: its wrong
is a *silent*, undisclosed subset presented as if complete for one selection
across two surfaces at one evaluation; the delta's category-1 members are the
opposite — named, closed-by-enumeration, and each explicitly bounded by a
declared ceiling, with the complete fact set continuously available from the
unmodified machine answer. On that reading the narrow reading is
**defensible**. But a reviewer reaching that conclusion should not have to
locate both of these on their own — the violation case in particular is the
kind of evidence a disclosure exists to surface, not to leave found.

*Resolution:* quote RFC-0006 §4 item 7 in the disclosure section and state
why the delta's members fall outside it (the "silent"/"named" distinction
above); cite the RFC6-21.c2 coverage row as existing, signed treatment of the
same question. Neither changes the delta's conclusion; both strengthen the
reviewer's ability to check it without a second read of RFC-0006.

### F2 — editorial. Ground 3 of the Normative classification is the weakest of the three and says so only by omission.

*Anchor:* `SEMANTIC-DELTA.md:264-267` (ground 3, "A scope limit is added").

*Rests on:* criterion d (test each ground against the quoted current text).

Grounds 1 (new verification obligation) and 2 (new service precondition) are
solid: both bind a route that complied before the amendment and would not
comply after, which is the template's own test
(`SEMANTIC-DELTA.md:250-251`). Ground 3 argues instead that "a reader could
previously have argued the presentation view's fields belonged in the
compared multiset" — a claim about what a reader *might have* argued, not
about text that is removed. Checked against the pre-patch PWB-REQ-020 text
(`spec.md:903-946`): the Observable/Oracle language never enumerated the
presentation view's own rendering fields as in-scope in the first place, so
ground 3 may be formalizing an already-implicit exclusion rather than newly
narrowing one. This does not change the Normative verdict — grounds 1 and 2
independently satisfy the template's test — but the packet asks a reader to
accept three grounds when two carry the weight, and does not say so.

*Resolution:* either drop ground 3 or mark it explicitly as the weakest,
non-dispositive ground, so a reader does not have to independently discover
that grounds 1-2 alone already classify the change.

## Criteria with no finding

- **Closure (#2).** "A route in neither category is neither admitted nor
  forbidden by this requirement" is scoped to PWB-REQ-020's own comparison
  only; it licenses nothing on its own because AGENTS.md's hard prohibition
  ("anything no act covers is forbidden") and the credential/ceiling gates
  named in P-72/P-76/P-77/P-78 sit outside this requirement and are
  unaffected. Verified M10 slice 3 and M11 slice 2 both still read "behind
  P-72" after this delta's own closure language (step 14 above).
- **The two categories are genuinely two (#3).** Disjointness independently
  re-confirmed this session (step 9's grep of `three-surface-poc-core`,
  `PocModel`, `projectShape` returns 0 over the 20-file M7 denominator,
  matching the funnel's own figure).
- **Parity is not weakened (#4).** The patch is a pure insertion; every Case,
  Observable, Oracle, Oracle-independence, Mutation-proof, Falsifier,
  Scenario and warrants line of PWB-REQ-020 is byte-identical (confirmed by
  the selftest's context-line-mutation fixture and independently by reading
  `spec.md:901-946` against the unpatched hunk boundary at line 903).
- **Package mechanics (#9), sibling ordering (#10), owner packet (#12).**
  All independently confirmed in "What I ran," steps 3-8, 17.
- **Registry field naming (criterion f).** `maxBriefingResponseBytes` occurs
  0 times in `spec.md`, in `proposed/spec.md.patch`, and in
  `routes.ts`'s `ResponseLimitIdentity` union; the dependency on the sibling
  registry package is stated in both directions (`SEMANTIC-DELTA.md` and
  "does NOT change" item 4) without assuming its content.
- **The second category vs. M7 slice 4 (criterion c).** No drift found; the
  delta's citation is narrowly scoped to what M7 actually supports (name,
  member, disjointness) and does not borrow M7's other, unruled claims.

## Comprehension restatement

Without author context: this delta adds two closed, enumerated categories to
PWB-REQ-020 — "derived read-only machine view" (composed only from the
machine answer at the same evaluation, independently oracle-verified,
served under its own declared ceiling; members: `/api/poc/polaris` now,
`/api/poc/briefing` once its ceiling is registered) and "generated editorial
draft view" (composed from one recorded generation run, carries no
project-shape identity, contributes to neither compared multiset; member:
`/polaris/draft/<runId>`). Neither category widens PWB-REQ-020's parity
comparison; a route not named a member of either is unaffected by this
requirement (and still needs whatever other gate applies to it). The owner is
being asked to sign off the drafted realization of two rulings already made
(P-72 arm A, P-76 arm A) or to name changes or decline. Adoption authorizes
no implementation, no route registration and no registry edit — those need
their own acts, one of which (the registry ceiling) is a separate,
not-yet-landed sibling package.

## Why CONFIRM WITH EXCEPTIONS

The package's mechanics are exact: the manifest digest, `--check`,
`--selftest`, and `--diff` all verify and reproduce; the composability claim
holds under an independent tool in both orders and fails closed under
mutation exactly as claimed; the dependency declaration is genuinely
regenerated, not transcribed; the 121/1,334 blast-radius figure and its
9-file continuation list are exactly reproducible by two independent methods
and match the ledger's own enumeration with zero set difference; the ceiling
precondition is coherent and creates no dangling literal; the "does NOT
change" list holds against every patch byte, including a fresh run of the
contract-coverage regeneration check. The Normative classification is
correctly argued (grounds 1-2 alone suffice). Neither finding above blocks
adoption: F1 concludes the delta's own reading is defensible, and F2 does not
change the change class. Both are completeness gaps in the disclosure a
reader is asked to rely on, which is why this is CONFIRM WITH EXCEPTIONS
rather than CONFIRM.
