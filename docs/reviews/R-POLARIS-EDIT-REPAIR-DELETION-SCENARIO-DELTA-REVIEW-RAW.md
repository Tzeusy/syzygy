# R-POLARIS-EDIT-REPAIR-DELETION-SCENARIO-DELTA review — PR #98 at e349ddb

Verdict: CONFIRM WITH EXCEPTIONS

## Scope and method

Fresh-context review per CC-REV-6: reviewed the package with only itself,
`SEMANTIC-DELTA.md`'s cited baseline files, and the acceptance criteria in
`REVIEW-BRIEF.md`, without the authoring conversation. Worktree:
`/tmp/claude-1000/-home-tze-GitHub-syzygy/ccd96075-5583-47ef-bd84-510b69d24ac7/scratchpad/rev98`
at `e349ddb87148a613d402bbcc7f649a437a43deea`.

## Findings

### 1. [PASS] Patch scope (REVIEW-BRIEF criterion 1)

`git apply --check` on both patches against the worktree HEAD succeeds:

```
$ git apply --check .../proposed/spec.md.patch && echo "SPEC PATCH APPLIES CLEANLY"
SPEC PATCH APPLIES CLEANLY
$ git apply --check .../proposed/PROJECT-STATUS.md.patch && echo "STATUS PATCH APPLIES CLEANLY"
STATUS PATCH APPLIES CLEANLY
```

Reading `proposed/spec.md.patch`'s two hunks: hunk 1 appends one sentence to
the end of REQ-006's requirement paragraph (`@@ -177,7 +177,7 @@`, single
line replaced, sentence appended at its end); hunk 2 inserts exactly one new
`#### Scenario: Edit or repair drops a prior block without account` block
immediately before `Form: lifecycle transition.` (`@@ -219,6 +219,17 @@`).
Nothing else is touched. This matches SEMANTIC-DELTA.md's claim exactly.

### 2. [PASS] No other requirement touched (criterion 2)

```
$ grep -n "### Requirement:\|ID: REQ-polaris-generation-" .../proposed/spec.md.patch
5: ### Requirement: Independent review and repair
10: ID: REQ-polaris-generation-006
```

Both hits are unmodified context lines (leading space, not `+`/`-`); neither
appears inside a `+` line. Confirmed: no other requirement is touched.

### 3. [PASS] Scenario is falsifiable and distinguishable (criterion 3)

The new scenario's THEN clause ("the output is invalid unless its change
account names each omitted block's id with a removed action and a reason")
states an actual, checkable failure condition, not aspirational prose: it is
directly checkable against a stage's output structure (block-id diff against
the account). The AND clause makes a repair that leaves every finding
unrepairable — returning input unchanged, each finding disposed
"unrepairable" — explicitly valid and distinguishable in the record from a
repair that changed content. Combined with the THEN clause (an *undisclosed*
drop is invalid), the three clauses together correctly separate three
distinct outcomes: valid change-with-account, invalid silent drop, and valid
no-op-with-recorded-dispositions. This satisfies the intent of not
conflating "nothing needed fixing" with "something was silently dropped."

### 4. [PASS] PROJECT-STATUS.md patch is the only change to that file (criterion 4)

`proposed/PROJECT-STATUS.md.patch` has one hunk, one line changed, only the
digit `177` → `178`; confirmed by direct read of the patch file.

### 5. [PASS] Manifest is honest (criterion 5)

```
$ python3 scripts/build_polaris_edit_repair_deletion_scenario.py --check
PASS: 6 behavior subjects, 2 patched, 0 manifest mismatches, scenario delta +1 confirmed by two methods, 0 sibling patch collisions.
```
Exit 0, and the printed stdout (not just exit code) reports 0 mismatches, +1
delta confirmed by two methods, 0 collisions — matching the claim.

**Independent digest recomputation (verification rule 3 — never transcribed, always
scripted; here also cross-checked by a second, non-builder method):**

- `python3 .../build_polaris_edit_repair_deletion_scenario.py --write` regenerated
  the manifest; `git diff` against the committed manifest file was empty —
  byte-identical.
- Independently, outside the builder script entirely, applied both patches
  with plain `git apply` into a scratch checkout of the two PATCHED files and
  hashed with plain `sha256sum`:
  - `openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`
    (post-patch) → `abea545df981ef1d4838146f57816135d06bdf01f8ef0fabca238bbcbcfe54ad` —
    matches the manifest's PATCHED row exactly.
  - `PROJECT-STATUS.md` (post-patch) → `fe2b88ee81ecd8fc91349c4607b9318896780d60ed712c6ff5f7be3ed50bef94` —
    matches the manifest's PATCHED row exactly.
  - Plain `sha256sum` on the four REFERENCE-row source files
    (`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`,
    `POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md`,
    `review-and-documentation.md`, the predecessor `spec.md`) matches all
    four REFERENCE digests in the manifest exactly.
  - All 6 manifest rows are now independently confirmed by a method that
    does not reuse the builder's own hashing code path.
- `PROJECT-STATUS.md`'s and the amendment `spec.md`'s **current** (pre-patch)
  sha256, as cited in `SEMANTIC-DELTA.md` (`b7c95f57ca5f67...`) and
  `IMPACT-LEDGER.md` (`e7b35f8da778938d...` / `b7c95f57ca5f67...`), both
  match plain `sha256sum` on the worktree's current files.

### 6. [PASS] Selftest fails closed, and fixture 1 hand-verified genuine (criterion 6)

```
$ python3 scripts/build_polaris_edit_repair_deletion_scenario.py --selftest
Running rule-6 mutation fixtures (each must make check() fail closed)...
  [ok] manifest digest tampered: check failed closed as expected
  [ok] proposed patch corrupted (context mismatch): check failed closed as expected
  [ok] base file drifted under the patch's context: check failed closed as expected
  [ok] PROJECT-STATUS.md patch states a scenario total inconsistent with the spec patch: check failed closed as expected
  [ok] undocumented sibling package patches the same behavior subject: check failed closed as expected
  [ok] a referenced behavior subject is missing: check failed closed as expected
selftest: all 6 fixtures failed closed as expected.
```

Hand-verified fixture 1 (manifest-digest-tamper) independently by importing
the builder module and reproducing its exact mutation logic in a standalone
script: it flips the first hex character of the first data row
(`a59294d4...` → `059294d4...`, the OWNER_RULINGS reference row), and
`check()` raises with the specific finding `manifest digest mismatch for
.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:
recorded 059294d4..., actual a59294d4...` — i.e., the fixture genuinely
exercises `verify_manifest()`'s digest-comparison path on the exact byte it
claims to tamper, not a no-op that fails for an unrelated reason.

### 7. [PASS] No governed byte edited in place (criterion 7)

```
$ git diff --stat origin/main...HEAD
 .../IMPACT-LEDGER.md                               | 135 ++++++
 .../OWNER-DECISION-PACKET.md                       | 119 +++++
 .../POLARIS-EDIT-REPAIR-DELETION-SCENARIO-MANIFEST.txt |  16 +
 .../REVIEW-BRIEF.md                                | 102 +++++
 .../SEMANTIC-DELTA.md                              | 304 +++++++++++++
 .../proposed/PROJECT-STATUS.md.patch               |  11 +
 .../proposed/spec.md.patch                         |  29 ++
 .../build_polaris_edit_repair_deletion_scenario.py | 481 +++++++++++++++++++++
 scripts/check_governance.py                        |  42 +-
 9 files changed, 1238 insertions(+), 1 deletion(-)
```

Only new files under the package directory, the new builder script, and the
`check_governance.py` registration diff appear. `PROJECT-STATUS.md` and
`openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`
themselves do not appear in the diff — confirmed unchanged in place. Also
mutated one patch byte (`178 scenarios` → `179 scenarios` in
`proposed/PROJECT-STATUS.md.patch`) and confirmed `--check` fails closed
(digest mismatch **and** the delta-consistency check both fire), then
reverted with `git checkout --` and confirmed `git status --short` is clean
and `--check` passes again (rule 6, applied a second time at the review's
own initiative beyond fixture 1).

### 8. [PASS] CG-7d/CG-7h registration, no chain link (criterion 8)

`git diff origin/main...e349ddb -- scripts/check_governance.py` shows:
- `POLARIS_EDIT_REPAIR_LABEL`/`_DIR`/`_SUBJECT`/`_ACT` constants added and
  the label registered in `_act_subjects()`'s tuple alongside the sibling
  PWB labels.
- `ACT_DIGEST_COPY_FILES[f"{POLARIS_EDIT_REPAIR_DIR}/OWNER-DECISION-PACKET.md"]`
  registered.
- `_activate_polaris_edit_repair_act_copy_registry()` is existence-gated:
  `if not os.path.isfile(os.path.join(ROOT, POLARIS_EDIT_REPAIR_ACT)): return`
  — a no-op today since `POLARIS-EDIT-REPAIR-DELETION-SCENARIO-ACT.md` does
  not exist, matching AGENTS.md's "registered from an existence-gated
  activation function" rule.
- No `PWB_SUCCESSOR_CHAIN`-equivalent entry was added; the docstring on the
  constant block explicitly states this: "Deliberately not a
  PWB_SUCCESSOR_CHAIN entry: it amends the Polaris generation specification,
  not the PWB behavior population, and asserts no adoption order beyond its
  own single act." Matches AGENTS.md "register a phrase and a copy, never a
  chain link."

Confirmed live in `check_governance.py`'s own output:
```
WARN  CG-7d  act digests quoted anywhere are current or performed — 61 quotations examined, 0 findings
        [subject] SIGN OFF POLARIS EDIT/REPAIR DELETION-ACCOUNT SCENARIO — 1 quotation(s), 0 finding(s), 0 performed digest(s)
OK    CG-7e  act-argument copies enumerated and current — 38 files examined, 0 findings
OK    CG-7h  performed bootstrap transaction subjects remain exact — 102 predicates examined, 0 findings
```

### 9. [PASS] CG-26 untouched (criterion 9)

The `check_governance.py` diff touches only `_act_subjects()` and
`ACT_DIGEST_COPY_FILES`/the new existence-gated activation function; no line
was added to the PROJECT-STATUS battery, the hosted CI workflow, or the
battery count sentence. Confirmed live:
```
OK    CG-26  published battery and hosted battery are one list — 36 checks examined, 0 findings — 36 published, 36 hosted, 36 shared
```

### 10. [PASS] `check_governance.py` is 0 FAIL (criterion 10)

Full run's printed summary line (not exit code alone):
```
32 OK, 20 WARN, 0 FAIL (52 checks) — counts derived, not asserted
```

### 11. [PASS] Owner questions genuinely open (criterion 11)

`SEMANTIC-DELTA.md`'s three open questions (sign-off scope; PROJECT-STATUS.md
coupling; full composition re-derivation) and `OWNER-DECISION-PACKET.md`'s
mirrored three questions are phrased as questions throughout, with no
default answer embedded in the proposed patch text — the patch text itself
contains only the new requirement sentence and scenario, none of which
answers any of the three questions. `OWNER-DECISION-PACKET.md`'s Options
(a)/(b)/(c) genuinely leave the choice to the owner, including "(c) Hold."
as a real no-op option. The act phrase is explicitly marked "Not offered"
with a stated reason (no review confirmed yet, no recorder script exists).

### 12. [PASS] Landing-order note computed live, re-swept and matches (criterion 12)

Re-ran the ledger's own sweep at review time:
```
$ for d in .syzygy/governance/contracts/candidates/*/; do [ -d "${d}proposed" ] && echo "$d"; done
.syzygy/governance/contracts/candidates/polaris-edit-repair-deletion-scenario/
.syzygy/governance/contracts/candidates/pwb-exact-source-render-mode-scenario/
.syzygy/governance/contracts/candidates/pwb-machine-view-amendment/
.syzygy/governance/contracts/candidates/pwb-missing-currency-disclosure-scenario/
.syzygy/governance/contracts/candidates/pwb-opening-band-scenario/
.syzygy/governance/contracts/candidates/pwb-registry-currency-briefing-amendment/
.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/
```
7 total including this package itself; 6 siblings excluding it, matching
`IMPACT-LEDGER.md`'s claimed "6 siblings" exactly (same six names). `--check`
(criterion 5's run) reports "0 sibling patch collisions," consistent with
`composition_findings()` finding nothing.

### 13. [PASS] Code-level evidence in SEMANTIC-DELTA.md verified independently against current code

Every code citation was independently re-read against the actual worktree
files, not trusted from the package's prose:

- `packages/polaris-generation-core/src/provider-draft.ts` line 45: exact
  literal `const schemas: Record<GenerationStage, Schema> = { inventory,
  plan, author: draft, edit: draft, repair: draft, fidelity };` confirmed.
- `validateStage`'s `else` branch is at lines 143-156 exactly (confirmed via
  `awk 'NR==143,NR==156'` — the branch opens `} else {` at line 143 and
  closes `}` at line 156); it never reads `context.draft` (only the earlier
  `fidelity` branch at lines 136 and 138 does — exactly 2 hits for
  `context.draft` in the file, both inside that branch, confirmed by grep).
- `packages/polaris-generation-core/src/pipeline.ts` lines 314-320: the
  three unconditional `context.draft = await stage(...)` reassignments
  (`author`, `edit`, `repair`) confirmed at those exact lines, no diffing
  against the prior value.
- `apps/three-surface-poc/src/polaris-generation/pipeline-demo.ts` line 66:
  exact literal confirmed. A word-boundary grep
  (`grep -rnw "edit" apps/three-surface-poc/src/polaris-generation/*.ts`,
  excluding `.test.ts`) confirms exactly one hit outside test files — the
  package's "exactly 1 hit" claim holds under a word-boundary search (a
  plain substring search also matches "editorial" in `draft-preview.ts`,
  but the package's phrasing ["the one hit for 'edit' ... outside test
  files"] is best read as the stage-name token, which is correct).

### 14. [PASS] Structural parity with sibling packages

`pwb-opening-band-scenario/` and `pwb-exact-source-render-mode-scenario/`
both carry the same file set (`IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`,
`proposed/`, a `*-MANIFEST.txt`, `REVIEW-BRIEF.md`, `SEMANTIC-DELTA.md`) as
this package. Structural parity confirmed.

### 15. [PASS] CC-REV-2 clause quoted correctly, from the correct location

`DIRECTIVE-REGISTER.md:89` names `CC-REV-2` ("The same-logical-change rule")
at `.syzygy/governance/policies/craft-and-care/review-and-documentation.md:52`.
Read directly:

> ## CC-REV-2 — The same-logical-change rule
>
> A change that invalidates any authoritative artifact updates **every**
> invalidated authoritative artifact in the same logical change: behavioral
> specs (`openspec/`), declared topology, accepted contracts, and the
> policies in this cluster. … The rule is a **merge invariant, not a
> property of how work is packaged**: no merge may leave mainline with an
> invalidated authoritative artifact still asserting the old truth.

This matches `SEMANTIC-DELTA.md`'s quotation (which elides one sentence with
an honest `…`). The package's own analysis — that `PROJECT-STATUS.md` is not
one of CC-REV-2's four named authoritative classes, and that bundling its
digit fix into this package is therefore a reasoned choice under a
*different*, AGENTS.md-sourced guardrail rather than a literal CC-REV-2
requirement — is accurate and is correctly surfaced as open question 2
rather than asserted as settled.

### 16. [EXCEPTION] The P-73 quotation is not byte-for-byte verbatim; it silently drops the table row's outer pipe delimiters

`SEMANTIC-DELTA.md` states: "Owner warrant, quoted verbatim" and then
block-quotes the P-73 row from
`.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
line 61. Diffed by Python (join the wrapped `>`-quote lines with spaces,
normalize whitespace runs, compare against the source table row with the
same whitespace normalization):

```
ORIG (source line 61, whitespace-normalized):
'| **P-73** (M6) | **A** — Q1 implementation; ... | Ready `.6.1`, `.6.2`; blocked `.6.3` on gate `.23`. |'

JOINED QUOTE (SEMANTIC-DELTA.md lines 17-28, dewrapped):
'**P-73** (M6) | **A** — Q1 implementation; ... | Ready `.6.1`, `.6.2`; blocked `.6.3` on gate `.23`.'

MATCH: False (first diff at position 0)
MATCH after stripping the source's leading '| ' and trailing ' |' table-row
delimiters: True
```

Every cell's content — bold markers, em-dash, backtick-quoted identifiers,
semicolons, the ellipsis-elided middle text is not elided here, this is the
full row — is byte-identical once the outer markdown-table pipe syntax is
stripped. This is very likely a deliberate, reasonable choice (rendering a
table cell's content as blockquote prose rather than reproducing raw
`| ... |` table syntax inside a blockquote), and it does not change the
row's substance in any way that affects this package's claims. But the
package's own label — "quoted verbatim" — is not literally true of the
bytes as quoted, and `REVIEW-BRIEF.md`'s own instruction to reviewers
elsewhere emphasizes exact, scripted verification over paraphrase-by-eye.
Given this repo's verification rule 8 ("Anchor a contract claim to a
defined clause and quote it; nearby prose is not the clause") and the task's
explicit instruction to diff this exact quotation with Python, I flag this
as a should-fix wording issue: either quote the row including its table
pipes, or change "quoted verbatim" to something accurate like "quoted
verbatim (table-cell content; outer pipe delimiters omitted)." This does
not affect the substance of the P-73 warrant as presented and does not
change my assessment of any other criterion.

### 17. [Observed] Bead cross-check

`bd show syzygy-dov.23` confirms the package's own framing: title "Gate:
CC-REV-2 scenario for the generator edit-stage deletion (P-73 slice 4) —
draft, sign-off", description matches the P-73/Q6 direction quoted in this
package, and it BLOCKS `syzygy-dov.6.3` ("M6 slice 4: edit-stage deletion —
blocked on its CC-REV-2 scenario sign-off"). The bead's own 2026-09-23
comment restates this package's contents, check results, and all three open
questions consistently with `SEMANTIC-DELTA.md`/`OWNER-DECISION-PACKET.md`.

### 18. OWNER-DECISION-PACKET.md plain-language check

Read in full. No jargon requiring governance-fluency: it explains the
generator's stages in plain terms ("it writes a first version, then an
'edit' stage can revise it..."), states the problem, the two file changes in
plain language, what does not change, buys/costs, and explicit
options (a)/(b)/(c) with (c) "Hold. ... nothing changes" as a genuine no-op.
The three open questions are phrased as questions, not statements, and no
default is asserted. The act phrase is explicitly marked "Not offered" with
a stated reason. No owner question is decided in this file or elsewhere in
the package.

## Summary

All twelve `REVIEW-BRIEF.md` criteria, the mechanical checks (builder
`--check`/`--selftest`, `check_governance.py` at 0 FAIL, independent digest
recomputation, a live rule-6 mutation-and-revert, and hand-verification of
selftest fixture 1), the code-evidence citations against
`packages/polaris-generation-core` and
`apps/three-surface-poc/src/polaris-generation`, the CC-REV-2 clause quote,
and structural parity with the two sibling PWB scenario packages all pass.
The one exception (finding 16) is a wording precision issue in a "quoted
verbatim" label that does not misrepresent the P-73 ruling's substance and
does not require re-drafting the package's technical content — only a
one-line label fix (or extending the quoted text to include the table
pipes) before this label can honestly be called verbatim.
