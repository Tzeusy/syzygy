# Impact ledger — non-governed narrative profile

> **Candidate — binds nothing.** Review material for
> `SEMANTIC-DELTA.md`. Not an authority or an adopted applicability judgment.

## Method

[Observed] Sweeps ran this session over `git ls-files` at base commit
`dbf8ed19` (1,969 tracked files; a file that did not decode as UTF-8 was
skipped), excluding this change's own two directories. Python `re`, never
`grep` (verification rule 1). The regexes are published in full, with run
form and case:

| Sweep | Regex (Python, flags as stated) | Files |
|---|---|---|
| A: the identifier | `REQ-polaris-generation-004`, case-sensitive | 47 |
| B: the continuation form | `REQ-polaris-generation-(?:\d{3}\s*(?:/\|,\|, and\| and\|\.\.\|–)\s*)+004`, case-sensitive | 11 |
| C: the RFC7 clauses | `RFC7-1[479]\b` or `RFC7-1[3-9]\s*(?:…\|\.\.\.?\|to\|–)\s*\d+`, case-sensitive | 70 |
| D: the phrases | `declared capabilit`, `verbatim (?:specification )?leaf` or `honest absence line`, case-insensitive | 92 |

Second method (rule 2): `git grep -l -F` for sweep A's literal returns 47
files, equal to sweep A. For D, `git grep -l -F -i "declared capabilit"` alone
returns 73, a different predicate that is a subset of D's three alternations,
so it confirms D's first alternative only. Sweep B overlaps A by
construction; its 11 files are in A or are continuation-only hits, and no
continuation-only hit was found outside A's list. C and D carry no second
method and are reported as sweeps, not as a proof of completeness.

Populations (rule 9): the denominator is 1,969 tracked files at the base
commit. A pattern outside these four forms (a requirement renamed or cited
by title only) is not covered; a title-only citer of "Understandable reading
depths" was not swept [Unknown].

## The four sets (CC-IMPACT-3)

| Set | Sweep A | Sweep B | Sweep C | Sweep D |
|---|---|---|---|---|
| Act records and decision records | 6 | 2 | 1 | 0 |
| Evidence records (`docs/evidence`) | 19 | 3 | 10 | 14 |
| Retained raw reviews | 4 | 2 | 12 | 14 |
| Other governed files under `.syzygy` | 5 | 0 | 26 | 38 |
| OpenSpec files | 5 | 1 | 13 | 13 |
| Code and tooling (`apps`, `packages`, `scripts`) | 3 | 1 | 4 | 4 |
| Docs and top-level pages | 5 | 2 | 4 | 9 |

Row classes are by path prefix; a file counts once per sweep. Totals per
sweep are 47, 11, 70 and 92.

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

## Edits required on adoption (CC-IMPACT-5, 6)

Each is named with its actor. All happen in the adopting change.

| Artifact | Why it moves | Actor |
|---|---|---|
| The candidate spec in `proposed/` | Moves to `specs/polaris-generation/spec.md` | Adopting change |
| `scripts/count_polaris_effective_scenarios.py` and the R-check that classifies base and overlay | Both refuse a third `polaris-generation` spec file: "expected exactly one base" [Observed: run at the base commit with the file placed in `specs/`] | Adopting change |
| `PROJECT-STATUS.md` | States 31 requirements and 182 scenarios; 32 and 190 with the eight added [Inferred: the count of 8 is this file's scenario headings] | Adopting change |
| `DIRECTIVE-REGISTER.md` | Generated; gains REQ-polaris-generation-032 | Adopting change |
| `scripts/build_polaris_dependency_unions.py` | Knows two changes; a third union needs its own entry and a signed successor if the existing unions change | Adopting change |
| `docs/polaris-generation/AUTHORING.md` | Candidate guidance; may need a line on the profile | Optional |

## Undecidable impact (CC-IMPACT-4)

[Unknown] Whether an RFC7-14 clarification is also needed. If the owner rules
that a spec overlay cannot define the terminus (packet O1), RFC7-14 gets a
semantic delta of its own through the RFC-0007 amendment path, and this
requirement waits on it.
