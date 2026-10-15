# Candidate consent contract-coverage overlay

Non-effective CC-SPEC-8 consequence matrix, read with the unchanged predecessor
CONTRACT-COVERAGE.md. The accepted clause text remains authority; row labels are
navigation/mapping, not new contract prose. Candidate requirement coverage is not
implementation evidence. No new N/A judgment is asserted by this artifact.

## Exact predecessor row affected

| RFC3-16(a) | valid state (1) or state (2) acts are effective and disclosed; other invalid acts fail closed | **Unknown** — CAP1-REQ-046 exercises only the missing-record case; no adopted requirement covers valid-state admission or the other invalid-act cases | — |

## Proposed scoped replacement and additional consequences

Only the consent consequences are mapped to the proposed 011/046 replacements.
Non-consent consequences of the same clause remain Unknown in the last row. Every
other predecessor mapping and unmapped/N/A-pending disposition is carried forward
unchanged; no historical clause count is restated as freshly measured. The rows
below expand the affected owner-act/consent consequences, not the whole contract
estate. The generated composition union is GOVERNING-DEPENDENCIES.json.

| Clause | Observable consequence | Requirement/basis | Candidate disposition |
|---|---|---|---|
| RFC3-7 / RFC3-30 | Exact project/repository observation scope and withdrawal polarity | CAP1-REQ-011/016 | covered by proposed 011 plus preserved 016 |
| RFC3-16(a) | Explicit valid bootstrap act can admit consent without A1 | CAP1-REQ-011 | covered |
| RFC3-16(a) | Successful independent correlation admits state (2) | CAP1-REQ-011 | covered |
| RFC3-16(a) | Each named invalid act state refuses effect, yields authorization Unknown and owner route | CAP1-REQ-011/046 | covered |
| RFC3-16(a) | Missing owner record or declared non-human actor does not establish an owner act | CAP1-REQ-011 | covered with controlled oracle |
| RFC3-16(a) | Undetectable same-tree forgery remains unauthorized, not independently detected | CAP1-REQ-011 Bootstrap oracle boundary | specified trust limitation; actual attendance unverified |
| RFC3-16(b) | Binding 1: project identity | CAP1-REQ-011 | covered |
| RFC3-16(b) | Binding 2: stable artifact identity | CAP1-REQ-011 | covered |
| RFC3-16(b) | Binding 3: exact artifact digest | CAP1-REQ-011 | covered |
| RFC3-16(b) | Binding 4: act type | CAP1-REQ-011 | covered |
| RFC3-16(b) | Binding 5: owner attribution | CAP1-REQ-011 | covered |
| RFC3-16(b) | Binding 6: act instant | CAP1-REQ-011 | covered |
| RFC3-16(b) | Binding 7: scope | CAP1-REQ-011 | covered |
| RFC3-16(b) | Binding 8: supersession/revocation relationship | CAP1-REQ-011 | covered |
| RFC3-16(b) | Binding 9: audit identity or explicit absence, distinguished from omission | CAP1-REQ-011 | covered |
| RFC3-16(b) | Failed/unavailable state-(2) correlation never creates state (1) | CAP1-REQ-011 | covered |
| RFC3-16(b/c) | Later correlation updates a new evaluation without rewriting prior effect/provenance | CAP1-REQ-046 | covered |
| RFC3-16(c) | Exact bootstrap/correlated provenance and act basis readable in both channels | CAP1-REQ-046 | covered |
| RFC3-16(c) | Act permission, provenance and execution success remain distinct | CAP1-REQ-046 | covered |
| RFC6-13 / RFC6-14 / RFC7-33 | Consent fact provenance and distinctions survive both renderings and nonvisual access | CAP1-REQ-046 plus preserved 040/041/045/064 | covered |
| RFC3-16(a) | General non-consent valid/invalid owner-act admission | predecessor CONTRACT-COVERAGE.md Unknown row | Unknown; no general authority-input implementation/specification supplied |

[Inferred] This clause/consequence applicability is proposed for independent
review and owner judgment with the amendment. No pending N/A is promoted to covered.
State-(1) human attendance is deliberately not a runtime-verification claim. A
reviewer finding another used contract consequence must add a scoped row or
retain an explicit Unknown; absence from this table is not N/A authority.
