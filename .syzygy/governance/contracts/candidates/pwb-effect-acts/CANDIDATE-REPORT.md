# Candidate report — PWB effect acts (consent, secret policy, observer registry)

> **GENERATED CANDIDATE REPORT — never authority.** The three artifacts bind
> nothing until the human owner performs the exact phrases in
> `OWNER-SIGNOFF-PACKET.md`; each phrase acts on one artifact only.

Frozen candidate commit: `48e0f5db645d1fb08e5e3a65c5e50dbcece40412`

Three-artifact manifest SHA-256: `d259c3798b2961489d31c55af09e86c9711c0cfd4e5ec626211fdc2447a54150`

## Result

The three effect-specific authorities PWB-REQ-005 requires before any Butlers
project-shape body read are drafted at their final bytes, cite only the
currently signed PWB package (the act recorded at
`.syzygy/governance/decisions/PWB-STATE1-AMENDMENT-ACT.md`) and the
currently accepted RFC-0004 general contract (the 2026-09-01 amendment
manifest), and carry the
PWB-REQ-005 authority-specific fields. Each is offered for a separate state-(1)
human owner act bound to its own SHA-256.

| Act type | Artifact | sha256 |
|---|---|---|
| `consent-observation` | `.syzygy/governance/decisions/BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md` | `5d705d75f993059d5ae5561b1a6f99d143462d9d2e5bcea8ecc9b0c258777841` |
| `approve-policy` | `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json` | `513a3be75bbd417a06d475c46bb423393ac59013e307157357083f29781a2a61` |
| `adopt-registry-entry` | `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` | `d71eadb612cf657983d96ad44415b832054dc37e51ea674e569d9b8f655d05d7` |

## Independent confirmation

| Raw review | Bound subject | Exact verdict | sha256 |
|---|---|---|---|
| `docs/reviews/R-PWB-EFFECT-ACTS-SECURITY-RAW.md` | `2fda7c440d996a5c58e6cf8577361520a0f1dca0` (manifest `b9af93fdd25dc57b99cffd7585c8222c763a56fc142d1aa6f30f58819394c849`) | `CONFIRM`, two non-blocking findings | `ef3010fce6eb0c55004f8cde1f09d92fe9a1cd068db70bec57fd5bde2b293d94` |
| `docs/reviews/R-PWB-EFFECT-ACTS-SECURITY-CONFIRMATION-RAW.md` | `48e0f5db645d1fb08e5e3a65c5e50dbcece40412` (manifest `d259c3798b2961489d31c55af09e86c9711c0cfd4e5ec626211fdc2447a54150`) | `CONFIRM` | `98bd5131c3f15b70e9d5172ad0aa92d094f6a67dc144e21a2d9f913c6d1e9549` |

The confirmation review covers the one repair made between the two subjects
(the secret policy now names RFC5-17's `unclassifiable-excluded` class); the
consent and registry bytes are identical at both subjects.

## Authority boundary

This report performs no owner act. Even after all three acts, no body read
occurs until separate PWB implementation authorization (task 1.8) exists and
an implementation evaluates the acts under PWB-REQ-005.
