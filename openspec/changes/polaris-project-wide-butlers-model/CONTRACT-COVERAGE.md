# Contract coverage — polaris-project-wide-butlers-model

> **GENERATED MANIFEST — do not edit.** The consequence judgments live in
> `contract-coverage-matrix/`; reviewed repairs live in
> `CONTRACT-COVERAGE-REPAIR-DELTA.md`. This file summarizes and verifies
> them. The generator makes no semantic applicability decision.

## Effective population

Accepted RFC 0001–0009 clauses: **324**.
Effective consequence rows: **622** — 137 covered, 237 Unknown uncovered, 248 believed not applicable.

Every accepted clause has at least one effective consequence row. A
`believed-not-applicable` row is an author/reviewer judgment, never an
owner-reviewed N/A. Every `unknown-uncovered` row remains a disclosed gap.

## Matrix parts

| Artifact | sha256 | Base consequences |
|---|---|---:|
| `contract-coverage-matrix/RFC-0001-0003.md` | `f28404be66a4241503f2214757d640361751934b2ab308dafeada5c6d2152e50` | 210 |
| `contract-coverage-matrix/RFC-0004-0006.md` | `ec091e743cb95070b30980021f2b5bdf054128161a86f6f8a8bbdf7678ffbc29` | 220 |
| `contract-coverage-matrix/RFC-0007-0009.md` | `6e480d6b94734abd41b15fbdcab1e6d7df9d60f68f0f3f5b0d66f98462728cd0` | 183 |

## Repair overlay

`CONTRACT-COVERAGE-REPAIR-DELTA.md` sha256 `77f6b685f7a92eff39d874b92ed36b99e832ded16d1970f1242b6750641b5349`
supersedes 71 base rows with 80 effective rows.

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
