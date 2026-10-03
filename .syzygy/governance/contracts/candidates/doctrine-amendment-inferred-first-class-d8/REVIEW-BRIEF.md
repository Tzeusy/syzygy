# Review brief — D8 doctrine amendment packet, round 1

> **Candidate — binds nothing.** The brief for one fresh-context review of
> this package (CC-REV-1). A review is evidence for the owner; it adopts
> nothing and its verdict is not an owner act (VIS-4).

## Stopping rule, set before the round

One round. Whatever the verdict, the drafter repairs each finding once and
records each finding and its repair in `ROUND-1-DISPOSITIONS.md`; no round
2 is dispatched. Repaired bytes go to the owner marked as repaired and
unconfirmed. A verdict is never re-labelled.

## Subject

The tracked files of
`.syzygy/governance/contracts/candidates/doctrine-amendment-inferred-first-class-d8/`
at the reviewed commit: `OWNER-DECISION-PACKET.md`, `SEMANTIC-DELTA.md`,
`IMPACT-LEDGER.md`, `REVIEW-BRIEF.md`.

## Governing references

- `.syzygy/governance/doctrine/trust-and-evidence.md` (whole file),
  `vision.md` (VIS-4, VIS-6, VIS-7), `architecture.md` ("Governed
  projects" and Definitions), `README.md` (glossary).
- Accepted contracts: RFC1-14 and RFC1-16 and the deferrals list
  (`contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`),
  RFC2-10, RFC2-24, RFC2-25 (`contracts/rfcs/RFC-0002/`), RFC4-26
  (`contracts/rfcs/RFC-0004/fidelity-joins-and-mappings.md`), RFC7-2,
  RFC7-3, RFC7-4 (`contracts/rfcs/RFC-0007/narrative-contract.md`).
- Specifications: PWB-REQ-012
  (`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`)
  and its coverage part `contract-coverage-parts/RFC-0007-0009.md`;
  REQ-polaris-generation-031
  (`openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`);
  the POC specification's `CONTRACT-COVERAGE.md` RFC4-26 row.
- Decisions: `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md` (P-71,
  P-74, P-75, P-76); `A6-RESOURCE-ENVELOPE-DECISION.md`;
  `DOCTRINE-AMENDMENT-LOG.md`; `launch-gate/` (for clause (e)'s scope);
  `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md` (Q3).
- `contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md` and
  `SEMANTIC-DELTA-TEMPLATE.md`.
- The pursuit's move N15 and findings L2-F5, L6-F2, L9-F3, S4-F3 and moves
  L3-M7, S3-M4 in `docs/pursuits/2026-09-22-vision-pursuit-data.json`.

## Acceptance criteria (from bead `syzygy-u05.15`)

1. Six drafted clauses, (a) synthesis copy role, (b) AttributedAnswer, (c)
   typed Inferred correspondence claim, (d) observed-only project under
   VIS-6, (e) reflexive observation, (f) generator figures stage, each with
   citations and blast radius.
2. Each shown representable in the current tuple vocabulary.
3. An owner decision packet batched with packet A (D7, P-101), each clause
   with its no-change arm.
4. Nothing adopted by agents; no doctrine byte edited; no code; any
   contract or specification amendment implied is an owner question, not a
   draft.

## What to test, at least

- **The premise check (packet §0).** Is it right that (a), (c) and (f) need
  no doctrine change and that (b), (d) and (e) do? Is any blocker
  mis-located (doctrine vs contract vs specification)?
- Does any quoted text differ from its source? Are the anchors, line
  numbers and sha256 values right at the reviewed commit?
- **Representability (packet §2).** Does each clause really fit the
  closed label, tier, reason, freshness and surface-state sets? Is (e)'s
  "restricted below `gate-backed`" a lawful use of RFC2-25's restriction
  rule, or an unstated new tier?
- **Clause (b) vs `trust-and-evidence.md` line 14.** Does a third named
  class contradict the two-warrant enumeration?
- **Clause (d) and VIS-5/VIS-6.** Does committing content about an
  observed-only project to the running governance root's `.syzygy/**`
  stay inside VIS-6 and add no write root? Does the packet state P-71 Q3's
  ruling correctly?
- **Clause (e)'s scope.** Could it be read to deny the trust floor to the
  canonical battery or a launch-gate administration?
- **Clause (a)'s scope.** Is "prose a surface composes" distinguishable
  from the generator specification's "synthesis" (ledger §3.3)?
- Is the departure from N15's wording of (b) (packet §0) honest and
  necessary?
- Re-run the ledger's term sweep and derived-artifact sweep; do the
  figures and set-equality hold?
- Does the composition with D7 and D3 (packet §8) hold?

## Output

Write the raw review to docs/reviews/R-DOCTRINE-AMENDMENT-D8-1-RAW.md (a
file this round creates).
Its first four non-blank lines must be exactly:

```text
# Review - D8 doctrine amendment packet (Inferred first-class, P-102)
Reviewed commit: <the full 40-hex commit you reviewed>
Package digest: <sha256 by the method below>
Verdict: <CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE>
```

Package digest method: at the repo root of a clone at the reviewed commit,
`sha256sum $(git ls-files .syzygy/governance/contracts/candidates/doctrine-amendment-inferred-first-class-d8 | LC_ALL=C sort) | sha256sum`.
Number every finding, label each `[Observed]`, `[Inferred]` or
`[Unknown]`, and mark each as revise-level or a note.
