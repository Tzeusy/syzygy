# Contract coverage — polaris-project-wide-butlers-model

> **GENERATED MANIFEST — do not edit.** The consequence judgments live in
> `contract-coverage-matrix/`; reviewed repairs live in
> `CONTRACT-COVERAGE-REPAIR-DELTA.md`. This file summarizes and verifies
> them. The generator makes no semantic applicability decision.

## Effective population

Accepted RFC 0001–0009 clauses: **324**.
Effective consequence rows: **622** — 142 covered, 232 Unknown uncovered, 248 believed not applicable.

Every accepted clause has at least one effective consequence row. A
`believed-not-applicable` row is an author/reviewer judgment, never an
owner-reviewed N/A. Every `unknown-uncovered` row remains a disclosed gap.

## Matrix parts

| Artifact | sha256 | Base consequences |
|---|---|---:|
| `contract-coverage-matrix/RFC-0001-0003.md` | `e15f2a974f9063dfb73e7a5132b59cc6b9401292c0a05547fa274664b7dfed93` | 210 |
| `contract-coverage-matrix/RFC-0004-0006.md` | `d5cd15470bc721b449543a18a84110df749c02f33984b9c3eedf55772fab29b7` | 220 |
| `contract-coverage-matrix/RFC-0007-0009.md` | `fa272738b85c64b6e455c06da26c01d6f3b80aab504c68ad18f57918d1e953ea` | 183 |

## Repair overlay

`CONTRACT-COVERAGE-REPAIR-DELTA.md` sha256 `c2b8e2f56b2d3ff004a7ac10523f945fc92dbbedcff027783101d2307f7b42d7`
supersedes 62 base rows with 71 effective rows.

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
