# Impact ledger — non-governed narrative profile

> **Candidate — binds nothing.** Review material for
> `SEMANTIC-DELTA.md`. Not an authority or an adopted applicability judgment.

## Method

[Observed] Sweeps ran by script over `git ls-tree -r -z` at commit
`9a6e8e31cfa842e83fa0970765f581579b40de3b`, excluding this change's own two
directories (neither exists at that commit). Denominator (rule 9): 1,988
tracked paths, of which 4 do not decode as UTF-8 and were skipped, so 1,984
were searched. Round 1 swept `dbf8ed1911aa193b0db7cfebdf8d4338c7500ba0`
(1,973 paths, 4 skipped, 1,969 searched); re-run in round 2 at both commits,
every count below is identical. Python `re`, never `grep` (verification rule
1). The regexes are published in full, with run form and case:

| Sweep | Regex (Python, flags as stated) | Files |
|---|---|---|
| A: the identifier | `REQ-polaris-generation-004`, case-sensitive | 47 |
| B: the continuation form | `REQ-polaris-generation-(?:\d{3}\s*(?:/\|,\|, and\| and\|\.\.\|–)\s*)+004`, case-sensitive | 11 |
| C: the RFC7 clauses | `RFC7-1[479]\b` or `RFC7-1[3-9]\s*(?:…\|\.\.\.?\|to\|–)\s*\d+`, case-sensitive | 70 |
| D: the phrases | `declared capabilit`, `verbatim (?:specification )?leaf` or `honest absence line`, case-insensitive | 92 |
| E: the prose short form | `\b[Rr]equirements? (?:\d{3}(?:,\| and\|,? and\| to)\s*)*004\b`, case-sensitive | 7 |
| F: the title form | `Understandable reading depths`, case-sensitive | 15 |

Citers of requirement 004 by identifier or continuation are A together with B:
A and B overlap in 6 files, B has 5 files not in A, so A or B is 52 files
(47 + 5). Round 1's claim that B's files were in A or continuation-only hits
outside A was false in the second half and is withdrawn: 5 of B's 11 files
are not in A (the understanding-specification adoption act,
`openspec/changes/polaris-manifesto-generation/ASSET-CONTRACT.md`,
`docs/design/POLARIS-M7-GENERATION-LOOP-FUNNEL.md` and the two M7 funnel
raws). The short-form and title-form sweeps (E, F) add 8 files outside A or B
(E: 4, F: 4; no file is in both lists outside A or B), for 60 files
citing 004 in any of the four forms. The eight are
`docs/reviews/R-POLARIS-GENERATOR-FRESH-PRODUCT-2026-09-12-RAW.md`,
`docs/reviews/R-POLARIS-GENERATOR-PRODUCT-READINESS-2026-09-12-RAW.md`,
`openspec/README.md`,
`openspec/changes/polaris-manifesto-generation/APPLICABILITY-DECISIONS.md`,
three selftest-witness evidence files and `scripts/check_spec_reconciliation.py`.
None changes the disposition below; the last, a checker that names the
requirement by title, is the one tooling file the sweeps add, and this
package does not edit it.

Second method (rule 2): `git grep -l -F` for sweep A's literal returns 47
files, equal to sweep A. For D, `git grep -l -F -i "declared capabilit"` alone
returns 73, a different predicate that is a subset of D's three alternations,
so it confirms D's first alternative only. C and D carry no second method and
are reported as sweeps, not as a proof of completeness. A citation of a
requirement by a name other than these six forms is not covered [Unknown].

## The sets (CC-IMPACT-3)

| Set | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| Act records and decision records | 6 | 2 | 1 | 0 | 0 | 0 |
| Evidence records (`docs/evidence`) | 19 | 3 | 10 | 14 | 2 | 10 |
| Retained raw reviews | 4 | 2 | 12 | 14 | 2 | 1 |
| Other governed files under `.syzygy` | 5 | 0 | 26 | 38 | 0 | 0 |
| OpenSpec files | 5 | 1 | 13 | 13 | 2 | 2 |
| Code and tooling (`apps`, `packages`, `scripts`) | 3 | 1 | 4 | 4 | 0 | 1 |
| Docs and top-level pages | 5 | 2 | 4 | 9 | 1 | 1 |

Row classes are by the first matching path rule, in this order: a raw review
is a path ending `-RAW.md` or containing `/reviews/`; then `docs/evidence/`;
then `.syzygy/governance/decisions/`; then the rest of `.syzygy/`; then
`openspec/`; then `apps/`, `packages/` and `scripts/`; then the rest. A raw
review under `decisions/` is therefore a raw. A file counts once per sweep.
Totals per sweep are 47, 11, 70, 92, 7 and 15, summing the column.

## Disposition by class

- **Historical or digest-bound: not edited.** Act records, evidence records,
  retained raws and the adopted change directories cite requirement 004 or
  the RFC7 clauses as they stood. This candidate edits none of them. The
  additive requirement is the reason: no MODIFIED block means no bound byte
  moves (AGENTS.md, "Never edit an artifact after an act has bound its
  digest").
- **Code and tooling that cite 004.** `packages/polaris-generation-core/src/rendered-design.ts`
  and its test cite the requirement for the rendered-design review record
  [Observed: the file names the requirement in its header comment]; neither
  checks bands, a catalog or a terminus. `scripts/record_polaris_understanding_adoption.py`
  is a performed recorder. None needs editing for this candidate.
- **Code that uses the phrases in D.** `apps/three-surface-poc/src/orrery.ts`,
  `polaris-copy.ts` and `polaris-first-reading.test.ts` use "declared
  capability" for the governed Butlers surfaces, and
  `scripts/build_pwb_item_depth_amendment.py` for a PWB amendment. These are
  governed subjects and keep the governed reading [Inferred: from the phrase
  context, not a full read of each].
- **Implementation of the profile.** Nothing implements a frozen declaration
  form, a contract-class band or the terminus yet. The generator code
  (`packages/polaris-generation-core/src/prompts.ts`) names no band or leaf
  [Observed: no match for the phrases in D in that file]. The work is in the
  task list, behind the owner's act.

## Edits required (CC-IMPACT-5, 6)

Each is named with its actor. The first row happens with this candidate's
existence; the rest happen in the adopting change.

| Artifact | Why it moves | Actor |
|---|---|---|
| `openspec/README.md` | `scripts/check_spec_reconciliation.py --check` predicate R5 requires one row per tracked change directory, so the candidate directory needs a row; round 1 found the commit failing R5 without it. The row says the change is a candidate that no act binds and not one of the five in force [Observed: R5 passes with the row] | This candidate (existence-time) |
| The candidate spec in `proposed/` | Moves to `specs/polaris-generation/spec.md` | Adopting change |
| `scripts/count_polaris_effective_scenarios.py` and the R-check that classifies base and overlay | Both refuse a third `polaris-generation` spec file: "expected exactly one base" [Observed: run at the base commit with the file placed in `specs/`] | Adopting change |
| `PROJECT-STATUS.md` | States 31 requirements and 182 scenarios; 32 and 194 with the twelve added [Inferred: the count of 12 is this file's scenario headings] | Adopting change |
| `DIRECTIVE-REGISTER.md` | Generated; gains REQ-polaris-generation-032 | Adopting change |
| `scripts/build_polaris_dependency_unions.py` | Knows two changes; a third union needs its own entry and a signed successor if the existing unions change | Adopting change |
| `docs/polaris-generation/AUTHORING.md` | Candidate guidance; may need a line on the profile | Optional |

## Undecidable impact (CC-IMPACT-4)

[Unknown] Whether the owner wants the maintainer span to be the verbatim
specification leaf itself. As drafted in round 2, (c) does not need that: the
leaf altitude is one honest line and the span is the anchor (RFC7-2 (a)), so
no RFC7-13 or RFC7-14 clarification is required [Inferred]. If the owner
rules the other way (packet O1), RFC7-13 and RFC7-14 get a semantic delta of
their own through the RFC-0007 amendment path, and (c) is redrafted after it.
