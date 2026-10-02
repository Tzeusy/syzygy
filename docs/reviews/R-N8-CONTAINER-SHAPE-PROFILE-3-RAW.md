# R-N8-3 — confirmation review of PR #124
Verdict: REVISE
Reviewed commit: 81315da91eeaa1f5f31456a64c5f68a6e918aa31
Manifest sha256: e297d800c262173b707c54476fbd7a879ce9467e748c7f4e3c2e6ea6c08b07e5

Reviewer: independent round-3 confirmation reviewer, fresh detached worktree
at the reviewed commit (removed after review). No commit, push or branch edit.
Package: `.syzygy/governance/contracts/candidates/pwb-container-shape-profile-amendment/`.
Builder: `scripts/build_pwb_container_shape_profile_amendment.py`.
Line numbers for the patched spec refer to
`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`
after applying all three `proposed/` patches to a scratch copy.

## Commands run and output (at 81315da)

| Command | Result |
|---|---|
| `python3 scripts/build_pwb_container_shape_profile_amendment.py --check` | exit 0; "matches 11 proposed subjects … 7 vocabulary, 2 key-form, 8 profile, 11 loaded-profile and 4 declared-item rules … 20 PWB-REQ-002 rules, 4 scenarios word for word"; also "shape and key-form sentences are a copy: … not in this tree" (dov.24 builder absent at this commit) |
| same, with `git show 929100f:<dov24 builder>` copied in temporarily | "shape and key-form sentences match the loaded-profile amendment's builder"; `shared_text_findings` = [] ; copy removed after |
| `… --selftest` | "146 mutants killed", exit 0 |
| `python3 scripts/check_governance.py` | "32 OK, 20 WARN, 0 FAIL (52 checks)", exit 0; CG-7d "SIGN OFF PWB CONTAINER-SHAPE PROFILE AMENDMENT — 1 quotation(s), 0 finding(s)" |
| `python3 scripts/check_governance.py --selftest` | "285 fixtures, 0 failing" |
| `python3 scripts/check_docs_review_campaign_partition.py` | "total=250 assigned=250 raw=225 other=25 unmatched=0 overlaps=0"; row "N8 container-shape profile gate 2"; `ls docs/reviews \| wc -l` = 250 |
| manifest digest, `sha256sum` and Python `hashlib` | both `e297d800c262173b707c54476fbd7a879ce9467e748c7f4e3c2e6ea6c08b07e5`; equals OWNER-DECISION-PACKET.md:25 and :195 |
| `openspec validate polaris-project-wide-butlers-model --strict`, three patches applied to a scratch copy | "is valid" |

Worktree `git status --short` was empty after every mutation run.

## Round-2 resolution

| Finding | Status | Evidence |
|---|---|---|
| R-A — refused Butlers profile fell back; no rule for a project with no profile | Resolved for refusal; residual note N-a; see new R-C | spec:132-135 "Until the observer reads a profile for Butlers … A Butlers profile the loader refuses never returns Butlers to the built-in default. A project other than Butlers with no loaded profile has no extraction rules …"; scenario "Refused Butlers profile does not fall back" (spec:308 WHEN) |
| R-B — owner attribution | Resolved | Ruled cells checked against `PENDING-OWNER-DECISIONS.md` P-74 (line 64) and P-82 (line 70), sitting §6 (line 135) and owner-values §6 (line 110). Package now attributes "What it means"/"Reading" text to the recorder: packet :13-16, :88-91, :101-106, :138-145, :171-181; SEMANTIC-DELTA :186-196, :277-282; IMPACT-LEDGER :143, :148. Sweep `ruling|rulings|ruled|chose|decided|answer|you|your` over the five package files: no remaining owner-voiced recorder text found |
| N-1 — shared text with dov.24 | Resolved | `SHAPES` equal; `ITEM_KEY_SENTENCES` keys fixed, leading-bold, leading-bold-or-code, first-cell-link-text, tree-key, ordinal-and-label, link-target-basename equal to 929100f's builder. #123 round-3 gaps inherited: see N-c |
| N-2 — multiple headings | Resolved with residual note N-g | list/table rows under more than one heading now defined |
| N-3 — shared rules | Resolved | spec:44-48 states the shared rules; claim narrowed |
| N-4 — M15/P-82 overlap disclosure | Resolved | SEMANTIC-DELTA :283-293, packet Q8, IMPACT-LEDGER :148 |
| N-5 — citer counts | Resolved | at 08d4d02, 1,545 tracked paths (4 undecodable): literal 49, run/range 14, total 63, by Python `re` and by `git grep -P`; the 14 run/range files equal the ledger list, including `project-shape-model.ts` (U+2026 range) |
| N-6 — review status | Resolved | packet :197-199 says both rounds REVISE and these bytes are unreviewed |
| N-7 — seven surviving builder mutants | Resolved | all seven now killed; B5 (scenario word-for-word) confirmed load-bearing |
| N-8 — "one extraction rule"; no class-to-category map | Resolved in text; evidence miscited, N-d | declared-item bullet and category map added |

## New findings

### R-C (revise) — falsifier fires on the conforming interim default

Patched spec.md:271-272 (PWB-REQ-002 falsifier): "… a refused Butlers
profile returns Butlers to the built-in grammar, or a project with no
profile reports a known item denominator."

"A project with no profile" is not scoped to projects other than Butlers.
Butlers today has no profile and, by spec:132-133 ("Until the observer reads
a profile for Butlers, it reads Butlers by the … built-in default"), lawfully
reports known item denominators. As written the falsifier is satisfied by the
conforming interim state, contradicting REVIEW-BRIEF.md:67-68 criterion 5
("today's code, with no profile loaded, must conform") and the body's own
scoping at spec:134-135 ("A project other than Butlers with no loaded
profile …"). The same unscoped clause is quoted in SEMANTIC-DELTA.md:149-151
and REVIEW-BRIEF.md:69-70.

The builder pins the defect: `REQUIREMENT_RULES["falsifier: project with no
profile"]` at builder:379-380 requires the literal "or a project with no
profile reports a known item denominator." A repair-form mutant ("or a
project other than Butlers with no profile reports a known item
denominator.") was KILLED by `--check`, so the repair must change the pinned
rule, the patch and the two quoting package files together.

Repair: scope the clause to "a project other than Butlers with no loaded
profile", matching spec:134, in the patch, builder:379-380,
SEMANTIC-DELTA.md:149-151 and REVIEW-BRIEF.md:69-70.

### Notes

N-a (note) — "reads" leaves a gap between declared and refused. spec:132
"Until the observer reads a profile for Butlers" falls back for any Butlers
profile not read, including one declared but unreadable (for example an
unreadable registry) which the loader never reaches to refuse. The scenario
WHEN at spec:308 says "declared for Butlers"; "reads" is undefined. Tie the
trigger to "declares" or state that a declared, unread profile is treated as
refused. Stale wording remains in live text at IMPACT-LEDGER.md:119 ("until a
profile is loaded"); packet:249 is a round-1 disposition and may stay.

N-b (note) — no case or scenario for a non-Butlers project with no profile.
The body (spec:134-135) and falsifier (spec:272) name it, but the Case list
(spec:~250-253) adds only three cases and none of the four scenarios covers it.
Class/category Unknown for a refused Butlers profile is stated only in the
fourth scenario; the body gives only per-source Unknown.

N-c (note) — two of #123 round 3's shared-sentence gaps recur here.
spec:106 "optionally with a quoted title" versus `LINK =
/^\[([^\]]*)\]\(([^)\s]*)(?:[ \t]+"[^"]*")?\)$/` in
`packages/three-surface-poc-core/src/project-shape-extraction.ts`, which accepts
double quotes only (probed with node: `'t'` false, `(t)` false). spec:88 "the field
inside any other table, is not read" versus `TOML_TABLE =
/^\[([^\]]+)\][ \t]*(?:#.*)?$/`, which does not match `[[other]]` (probed
false), so a `name` line after `[[other]]` is still read as `[butler]`'s.
spec:48 ("recognized is shared by every project and left to the observer")
arguably covers recognition, but the affirmative clauses are false of the
code. The headings[0]-only probe gap does not apply: this builder runs no
code probes, and code conformance is [Inferred] and delegated to dov.24
(SEMANTIC-DELTA.md:235-238). Since the sentences are shared text with dov.24,
any repair lands in both packages.

N-d (note) — class-to-category evidence miscited. SEMANTIC-DELTA.md:164-166
([Observed]), IMPACT-LEDGER.md:121 and packet:278 name `classesForPillar`
(`project-shape-model.ts:544-552`) as the mapping, but it has
`'spec-and-spine': []` (baseline-spec identity owned by the exact-tree rule)
and no roster entry. The complete mapping that agrees with the new bullet is
`CLASS_ROWS` in `packages/three-surface-poc-core/src/project-shape-coverage.ts:85-95`
(layers 1-6). The text is right; the citation is not the source that shows it.

N-e (note) — builder selftest overclaims on manifest verification. Mutant B6
(disable `if text != expected` in `verify_manifest`, builder:881) and B7
(disable the undeclared-subject-change append, builder:898) both survive
`--selftest` (still "146 mutants killed"). Under B6, `--check` passed a
manifest with a corrupted row digest (rc 0) that the real builder fails
(rc 1). The selftest's "stale manifest" fixture (reported at builder:1310)
only tests that `render()` changes. The live `--check` works; the selftest's
claim to cover a stale manifest does not.

N-f (note) — unchanged-text claims are guarded by the frozen digest, not the
builder. These spec mutants survive `requirement_findings`, and survive
`structure_findings` once dependents are regenerated as `--write` would:
PWB-REQ-002's unchanged oracle "malformed/unreadable", "modeled + Unknown +
contradicted", "revision-bound", oracle-independence "not from", observable
"Polaris", Form invariant, title, case "one revision", case "unreadable source
case", falsifier partial-population and unavailable-body clauses, the body
category list; a swap of scenario order; PWB-REQ-003 SHALL NOT → MAY; the
source-population "do not recurse". So "No other requirement changes"
(SEMANTIC-DELTA.md:29) and "source population rules unchanged"
(SEMANTIC-DELTA.md:173-177) are true of the current patch [Observed] but
enforced only by digest and review. Either narrow SEMANTIC-DELTA.md:25
("the builder checks this") or add those pins.

N-g (note, minor) — unstated details. The ordinal-and-label key form does not
say whether the label is trimmed; precedence among several first failures in
one source is unstated; heading-section with three or more headings is
undefined, and whether prefixed-ordinal numbering restarts per heading is
ambiguous.

## Behaviour checks against `project-shape-extraction.ts` (D5)

`sectionOf` ends at `h.level <= heading.level`; `oneHeading` gives
missing-heading / duplicate-key; `headedTable` matches by text at any level,
with missing-heading / duplicate-key / malformed-row; v1-scope statement is
ships + body + defers + body joined by blank lines, trimmed; architecture joins
the h2s; `ORDINAL_H2 = /^(\d+[a-z]?)(?![\w])/` matches the spec; the catalog
extractor's dash set (hyphen, en dash, em dash) matches. Except N-c, the
written grammar agrees with the code [Observed].

## Rule-6 mutants (my own)

Builder mutants B1-B5, B8-B15: killed. B6, B7: survived (N-e). The repair-form
falsifier mutant was killed (R-C). The "NFC-normalized" and "as it reads one
section" spec mutants were killed. Spec mutants in N-f survived.

## Confirmations

- VIS-4: no adoption or acceptance claim; the act phrase is not offered
  (packet :191-202); the landing order is attributed only as the four ruled
  packages.
- VIS-2: loaded-profile and refused-profile paths yield Unknown, never zero
  (spec:134-145), apart from R-C's unscoped falsifier.
- Open questions 4, 6, 7 and 8 are genuine owner questions.
- The oracle's second leg ("must produce the same identities and D") is
  falsifiable together with scenario 1's AND clause; alone it could be read
  as the two extractors agreeing with each other.
