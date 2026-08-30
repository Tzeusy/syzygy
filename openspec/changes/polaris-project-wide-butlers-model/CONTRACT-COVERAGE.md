# Contract coverage — polaris-project-wide-butlers-model

> **GENERATED MANIFEST — do not edit.** The consequence judgments live in
> `contract-coverage-matrix/`; reviewed repairs live in
> `CONTRACT-COVERAGE-REPAIR-DELTA.md`. This file summarizes and verifies
> them. The generator makes no semantic applicability decision.

## Effective population

Accepted RFC 0001–0009 clauses: **324**.
Effective consequence rows: **615** — 140 covered, 230 Unknown uncovered, 245 believed not applicable.

Every accepted clause has at least one effective consequence row. A
`believed-not-applicable` row is an author/reviewer judgment, never an
owner-reviewed N/A. Every `unknown-uncovered` row remains a disclosed gap.

## Matrix parts

| Artifact | sha256 | Base consequences |
|---|---|---:|
| `contract-coverage-matrix/RFC-0001-0003.md` | `93d541cff0a36233c53f2e9b2957eefb02b0faf8a159b455951e633ce77de059` | 208 |
| `contract-coverage-matrix/RFC-0004-0006.md` | `e7e4eed310e9cc16888d3d097e68a9a64bd2d073e0018fd8bfc679dd50c73332` | 220 |
| `contract-coverage-matrix/RFC-0007-0009.md` | `fa272738b85c64b6e455c06da26c01d6f3b80aab504c68ad18f57918d1e953ea` | 183 |

## Repair overlay

`CONTRACT-COVERAGE-REPAIR-DELTA.md` sha256 `93366b05edd696ce76fce1bc9ce52a1457b91b8041ad7d12bf7bd3802cc8fcbb`
supersedes 62 base rows with 66 effective rows.

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
