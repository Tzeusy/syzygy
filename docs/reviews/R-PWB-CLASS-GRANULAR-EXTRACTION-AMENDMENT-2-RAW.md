# Review round 2 — PWB class-granular extraction amendment (M15)
Reviewed commit: 1701c88f31dcf74130f6f2b5c84b990ebc49de08
Manifest SHA-256: af996b0abff3b3ec1e804d760cb784692966c126b79f1b3d8bb189be43f85bd0
Verdict: REVISE

Reviewer: fresh-context agent; read only the brief and what it names (plus
the evidence record and code the package itself cites for its [Observed]
claims). `ROUND-1-DISPOSITIONS.md` and `docs/reviews/` were not read.
Manifest digest computed by `git show 1701c88f:<manifest path> | sha256sum`.

## Checks run (scratch clone at the reviewed commit)

- [Observed] `build_pwb_class_granular_extraction_amendment.py --check`:
  exit 0, "matches 11 proposed subjects (5 patched); 17 requirements, 54
  scenarios; structure, regeneration, contract coverage and sibling
  classification verify".
- [Observed] `--selftest`: exit 0, "34 structure mutants, patch drift and an
  unclassified sibling all fail closed on their own predicates".
- [Observed] `build_pwb_release_label_amendment.py --check`: exit 0.
- [Observed] `check_governance.py`: "31 OK, 21 WARN, 0 FAIL (52 checks)".
- [Observed] `check_spec_reconciliation.py --check`: "7 of 7 predicates
  without FAIL; PASS" (R6 reports the two already-stale pins the package
  names as residual 4).
- [Observed] Second clone with the five patches applied by `patch -p1`: all
  11 manifest rows equal the sha256 of the applied bytes;
  `build_polaris_project_wide_contract_coverage.py --check` passes (324
  clauses); `build_polaris_project_wide_spec_dependencies.py --check`
  passes; capability table recomputed by script: 34 rows, 28 covered, 6
  lawfully out of scope, matching the printed totals.
- [Observed] Removed spec lines (`git diff -U0 | grep '^-'`): exactly the 9
  signed lines the semantic delta quotes as Current in hunks 3–6, 8 and 9;
  every hunk lies in the reader definitions or PWB-REQ-002; spec scenarios
  51 → 54, PWB-REQ-002 6 → 9, requirements 17 → 17.
- [Observed] Own rule-6 mutations in a third clone: one character of the
  spec.md manifest row changed → `--check` reports "manifest differs from
  deterministic proposed-byte regeneration"; "class that fails never
  produces" changed to "may produce" inside `spec.md.patch` → `--check`
  reports the missing required phrase, the stale dependency digest and the
  stale manifest. Restored → passes.
- [Observed] Impact-ledger census re-derived at `ef5d5f03` with the
  ledger's own regex over `git ls-tree -r -z` (1,970 paths): 96 files, and
  the per-area split equals the ledger's table row for row.
- [Observed] Code claims at `ef5d5f03`: module comment lines 14–17,
  `CATALOG_HEADINGS` lines 56–66 (nine literals), `extractCatalogEntries`
  at 438, `extractSource` at 628 returning `kind: 'unknown'` on the first
  failed class, `ManifestSource.rule` present — all as the delta states.
- [Observed] `docs/evidence/smooth-example-live-run-2026-10-03.json`
  `unknownDenominatorWithheldComparison`: 9 = 9, `equal: true`; `b044a756`
  is an ancestor of the reviewed commit.

## Criteria summary

1. Ruling content — met. Q1–Q4 each carried; readings put to the owner as
   packet questions 2–6. Round-2 addition: question 6 states fairly that the
   PWB-REQ-002-only scope came from the recorder's gloss, not the owner's
   words, gives both arms with the consequence of deferral ("still skipped
   silently"), and names it residual 5 (see Finding 8 for a labelling note).
2. Specification bar — met except Finding 1. The source-level rule has its
   SHALL ("a source with a class whose item denominator is Unknown SHALL
   leave its own item denominator Unknown"), oracle ("each source with a
   class whose D is Unknown has its own D Unknown"), falsifier ("a source
   with a class whose item denominator is Unknown presents its own item
   denominator as known") and a scenario limb (the unenumerated-heading
   scenario's "the V1 index's own item denominator ... render Unknown"; see
   Finding 2). Unenumerated-heading count: oracle "the count per source and
   class equals the count the answer gives", falsifier "is miscounted".
   Rule provenance: oracle and falsifier limbs present, but see Finding 1.
3. Category rule — met: "A class's item denominator across its sources, and
   its category's, is Unknown whenever the class is Unknown in any of those
   sources", and a class is Unknown in a source for a failure, an
   unenumerated heading, or an unavailable/excluded/over-limit body; the
   aggregate is per class-in-source, so a sibling that read cannot mask a
   failed class. [Inferred] Today's coverage code already makes a class
   aggregate Unknown when any assigned source is Unknown
   (`project-shape-coverage.ts` lines 492–508), so the packet's "changes
   nothing visible on Butlers today" holds for the 9 withheld sources.
   Exactness reach — met: the narrowed rule sits under "For every grammar,
   loaded or built-in"; a resource breach stays whole-source; nothing that
   failed a whole source becomes silently partial, since every failed class
   is Unknown with a reason and makes its source's own denominator Unknown.
   See Finding 3 for an unstated change of meaning.
4. Signed bytes — met (checks above).
5. Honest claims — met except the [Observed] provenance claim in Finding 1.
   [Unknown] is used for Butlers' V1 index; no adoption, build or read is
   claimed; residuals 1–4 verified (`check_spec_reconciliation.py` line 214
   pins `"PWB": (17, 51)`; `real_packages()` lacks the package).
6. Mechanics — met (Finding 6 is a note).
7. Plain language — met: the packet's three-bullet summary and "what signing
   does not do" let a fresh reader restate the change.

## Findings

**Finding 1 — Rule provenance is made normative over rule names the spec never binds, and one admitted source has no rule** (revise)

[Observed] Hunk 1 adds "every source carries the name of the rule that
admitted it" and names "the pillar-root and pillar-index rules" and "the
baseline-spec and roster rules". The oracle requires "every source names the
rule that an independent derivation of the source-path population admits it
under", and the falsifier fires when "a source names no rule or a rule other
than the one that admitted it". But the signed population sentence (spec
lines 68–72 after apply) is "closed by four rules" that it never names; the
labels "pillar-root"/"pillar-index" appear nowhere else in the spec (grep
over `specs/` and `design.md` of the applied tree). [Observed] The code the
delta cites, `project-shape-manifest.ts` line 71 at the reviewed commit,
has five rules — `root-index`, `pillar-index`, `pillar-named-file`,
`baseline-spec-tree`, `roster-tree` — so its `pillar-index` names the
pillar's own README, while the spec's "pillar-index rule" can only be rule 2
(the files that index names), and the root index file itself is admitted as
a source by code under `root-index` but by none of the spec's four rules.
[Inferred] For the root index source (and arguably each pillar's index
file) the provenance oracle cannot be decided without judgment (CC-SPEC-4:
an oracle that "terminates in bounded effort, without judgment"): either
the independent derivation admits it under no rule, so the falsifier "names
no rule" fires on every Butlers observation, or the reader invents a fifth
rule the closure sentence denies. The delta's "[Observed at `ef5d5f03`]
`ManifestSource` ... already carries the rule that admitted a source" is
literally true but omits that the carried vocabulary does not match the
spec's. Repair: bind each label to its numbered rule in the reader
definitions, and say which rule (if any) admits the root index and the
pillar index files, or scope the provenance obligation to the four rules'
sources.

**Finding 2 — The failing-class scenario does not assert the source's own denominator or its partially extracted state** (note)

[Observed] "A failing class keeps its siblings" asserts the failed class's
in-source, class and category denominators Unknown and the siblings known,
but not the source's own item denominator Unknown, nor that the source is
shown as partially extracted. The source-level rule's scenario limb is
carried only through the unenumerated-heading arm. The oracle and falsifier
cover the failed-class arm, so this is a coverage gap in scenarios, not a
missing obligation.

**Finding 3 — Signed unreadable-class text changes meaning without the delta saying so** (note)

[Observed] The signed sentence "each source any of its rows names fails as a
source in which a class fails" and the signed scenario "Loaded profile names
a shape outside the vocabulary" are byte-unchanged, but under the old
exactness rule such a source lost every class, and under the new one its
other classes keep their items. [Inferred] That is the intended effect, but
the delta's "What explicitly does NOT change" says the six signed scenarios
"stay" and its "'Fails the source'" paragraph addresses only the shape and
key-form sentences. Name this reinterpretation in the Current/Proposed
meaning account.

**Finding 4 — "below" in the class-failure sentence excludes the shared heading rule directly above it** (note)

[Observed] Hunk 2 says "Wherever a shape or key form below fails the
source, it fails the class", but the shared rule "a declared heading that is
missing fails the source as missing-heading, and one that occurs more than
once fails it as duplicate-key" is in the preceding bullet. [Inferred] The
exactness bullet ("A missing heading ... unexpected duplicate key ... in any
of a class's rows fails that class") covers it in substance, so no
behaviour is left whole-source; the word is imprecise.

**Finding 5 — Packet question 4 understates the recommended arm's reach** (note)

[Observed] Question 4's recommended arm says "Rows that read a heading's
section are left out, so the V1 index's other level-2 headings are never
flagged." [Inferred] A loaded profile's list or table row naming two level-2
headings would enclose level 2 across the whole level-1 section or file and
flag every level-2 heading no row declares — the effect the delta cites to
exclude `heading-section`. Butlers' written grammar has no such row (its
only multi-heading list row is the level-3 catalog), so nothing changes for
Butlers; the option text should say the effect exists for such rows.

**Finding 6 — Selftest expectations are partly unpinned, and two predicates have no in-selftest mutant** (note)

[Observed] Mutants "whole-source discard restored", "partial class set
allowed", "unenumerated heading skipped" and "tree flag default flipped"
expect only the prefix "the reader definitions carries 0 copies of required
phrase", so they would pass if a different required phrase went missing. No
selftest mutant exercises the manifest or contract-coverage predicates.
[Observed] My own mutations of the manifest row and of `spec.md.patch` fail
`--check` on the right predicates, so the gap is in the fixture, not the
check.

**Finding 7 — "the root index was not read" is not defined against a read root index whose grammar fails** (note)

[Inferred] The qualification and the "mints no item" rule turn on whether
the root index "was read". Whether a root index whose body is read but whose
PWB-REQ-004 grammar fails counts as read is not stated; the pillar rules
name no source either way, but whether baseline-spec and roster counts carry
the qualification in that case is left to the implementer.

**Finding 8 — Residual 5 is an open owner question filed under an [Observed] list of signing-change tasks** (note)

[Observed] "Residuals the signing change must carry [Observed at
`ef5d5f03`]" lists item 5, the undesigned root-summary and precedence half
of Q3, which is neither an observation at a commit nor a task the signing
change performs. Packet question 6 handles it fairly; the label and the
heading are the only defect.
