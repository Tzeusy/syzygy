# Contract coverage — polaris-project-wide-butlers-model

> **GENERATED MANIFEST — do not edit.** The consequence judgments live in
> `contract-coverage-matrix/`; reviewed repairs live in
> `CONTRACT-COVERAGE-REPAIR-DELTA.md`. This file summarizes and verifies
> them. The generator makes no semantic applicability decision.

## Effective population

Accepted RFC 0001–0009 clauses: **324**.
Effective consequence rows: **622** — 132 covered, 242 Unknown uncovered, 248 believed not applicable.

Every accepted clause has at least one effective consequence row. A
`believed-not-applicable` row is an author/reviewer judgment, never an
owner-reviewed N/A. Every `unknown-uncovered` row remains a disclosed gap.

## Matrix parts

| Artifact | sha256 | Base consequences |
|---|---|---:|
| `contract-coverage-matrix/RFC-0001-0003.md` | `d03eebe142d9cc8b9046243d33bcd498debc6235ec9f8700b114834987aeb88e` | 210 |
| `contract-coverage-matrix/RFC-0004-0006.md` | `bccadc7d5218eb5fa5b2a008747a9f90a2d62cac08f7dd604f6c90872d5a347d` | 220 |
| `contract-coverage-matrix/RFC-0007-0009.md` | `b09abdb8aaf8d54f378139d1e4f93e053d5fa7d721c9e4dbd1f750f5a7987d9c` | 183 |

## Repair overlay

`CONTRACT-COVERAGE-REPAIR-DELTA.md` sha256 `732053ce53814f65a65d940c3ea65e0117b837fc375004d57d08c25ed3bd7a87`
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
