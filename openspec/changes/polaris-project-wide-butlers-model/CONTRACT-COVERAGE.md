# Contract coverage — polaris-project-wide-butlers-model

> **GENERATED MANIFEST — do not edit.** The consequence judgments live in
> `contract-coverage-matrix/`; reviewed repairs live in
> `CONTRACT-COVERAGE-REPAIR-DELTA.md`. This file summarizes and verifies
> them. The generator makes no semantic applicability decision.

## Effective population

Accepted RFC 0001–0009 clauses: **324**.
Effective consequence rows: **620** — 132 covered, 240 Unknown uncovered, 248 believed not applicable.

Every accepted clause has at least one effective consequence row. A
`believed-not-applicable` row is an author/reviewer judgment, never an
owner-reviewed N/A. Every `unknown-uncovered` row remains a disclosed gap.

## Matrix parts

| Artifact | sha256 | Base consequences |
|---|---|---:|
| `contract-coverage-matrix/RFC-0001-0003.md` | `31174ca2d6a5e9c2bcb7e2973f3f53c978496dad32a22ea49bf69d8107039b68` | 210 |
| `contract-coverage-matrix/RFC-0004-0006.md` | `e7e4eed310e9cc16888d3d097e68a9a64bd2d073e0018fd8bfc679dd50c73332` | 220 |
| `contract-coverage-matrix/RFC-0007-0009.md` | `fa272738b85c64b6e455c06da26c01d6f3b80aab504c68ad18f57918d1e953ea` | 183 |

## Repair overlay

`CONTRACT-COVERAGE-REPAIR-DELTA.md` sha256 `cf1239e8c201d6d40cc3e4b7b195cce7f326bbd523fb9000a4065f87a2393c94`
supersedes 62 base rows with 69 effective rows.

## Verification

```sh
python3 scripts/build_polaris_project_wide_spec_dependencies.py --check
python3 scripts/build_polaris_project_wide_contract_coverage.py --check
python3 scripts/build_polaris_project_wide_contract_coverage.py --selftest
```

The checks enforce accepted-clause representation, unique consequence
identities, valid repair supersession, closed dispositions and exact
requirement-warrant agreement. They do not confirm semantic judgments;
fresh review does.
