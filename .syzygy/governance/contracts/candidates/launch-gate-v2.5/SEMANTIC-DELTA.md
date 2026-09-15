# Semantic delta — launch-gate v2.5 / schema 2.1

> Candidate, non-effective. Owner work authorization covers drafting, necessary
> supporting code and independent review; exact-version approval is still required.

**Artifacts:** successor launch-gate-pre-specifications.md and
launch-gate-administration.schema.json in this directory; validator support in
scripts/validate_launch_administration.py. The renderer changes only if needed.
**Stable IDs affected:** LA-1 schema binding/conformance, LA-2 instrument binding
(as preserved constraint), SPEC_MEDIUM; findings RD-56 f11 and P-53.
**Change class:** Normative (schema admission), Clarifying (SPEC_MEDIUM).
**Author:** Codex, owner-directed.
**Date:** 2026-09-14.
**CC-REV-1 review classes:** 3 (deterministic observation: historical schema
selection and local drift), 6 (public interface: machine-record schema and CLI
eligibility). Class 5 migration is not claimed: no stored record is converted or
rewritten. No new execution/write authority, graph identity, credentials/egress
boundary or certificate logic is introduced. These classifications are proposed
for independent review, not an exemption from review.

P-34's required policy-semantics review covers preservation of the readiness
questions/formula and this declared scope; its structured-record review covers
the schema, validator, renderer and version/replay behavior under classes 3/6.

## Current meaning

The approved v2.4 instrument and schema 2.0 are rooted at the repository top
level. They remain byte-unchanged while this candidate is prepared. Exact current
and proposed changed lines are in successor.diff; BASELINE.json binds the source
files. The question-digest definition currently states:

```json
{
  "description": "sha256 of the question's verbatim text as administered, or the literal `instrument-bound` when the record binds identity through the instrument digest instead. A verdict rendered against a paraphrased question is void (instrument section 2).",
  "type": "string",
  "pattern": "^([0-9a-f]{64}|instrument-bound)$"
}
```

No check recomputes or compares that arbitrary per-question hash (RD-56 f11).
LA-2 checks the full instrument identity. The current parameter row is:

```text
| `SPEC_MEDIUM` | OpenSpec (`openspec/` — does not exist yet; its absence is correct pre-gate) |
```

That existence claim is stale; a process parameter need only identify the medium.

## Proposed meaning

```json
{
  "description": "The literal `instrument-bound`: question identity is bound through the instrument digest and checked under LA-2. An unchecked per-question hash is not accepted. A verdict rendered against a paraphrased question is void (instrument section 2).",
  "type": "string",
  "const": "instrument-bound"
}
```

```text
| `SPEC_MEDIUM` | OpenSpec (`openspec/`) |
```

Schema version changes from 2.0 to 2.1, instrument version v2.4 to v2.5, and a
new §9 entry records this bounded delta. Existing changelog entries remain intact.
A new full-commit schema-2.1 record with an arbitrary 64-hex question value fails
LA-1 and cannot support an eligible formal result. Its question identity must be
instrument-bound and is checked by LA-2. No per-question hashing protocol is added.

The validator judges a record using the schema committed at that record's full
repository_commit. Separately, it compares the current schema file with HEAD to
detect uncommitted local drift. A committed successor is not uncommitted drift
from a historical record. Missing committed schemas, unsupported record versions,
uncommitted drift and arbitrary alternate --schema inputs remain invalid.

## What explicitly does NOT change

Sections 1–7, including questions, roster, verdict vocabulary and formula, are
byte-identical. Section 8 differs only in the SPEC_MEDIUM row above. F5 remains
unpromoted. JSON remains canonical; Markdown remains generated. The two historical
fixtures and their generated reports are immutable; there is no data migration.
RD-67 abbreviated-commit selection and RD-68 invisible-character handling remain
outside this amendment, with no assertion that the policy is free of false-READY
paths. Approval would knowingly retain those disclosed residuals.

## Warrant

[Observed] In interactive chat on 2026-09-14 the owner answered “Agreed, please
proceed” to LAUNCH-DIGEST option A: combine RD-56 f11 and P-53 in one non-effective
successor, including necessary validator/renderer support and independent review.
The bounded direction is recorded in syzygy-s9q. P-34's owning decision record
requires fresh work authorization for v2.5 and separately final owner approval.
This direction satisfies the authoring gate, not the adoption gate.

## Evidence or decision basis

- .syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md: P-34, current
  approval and disclosed residuals; no act phrase or signed digest is reoffered.
- .syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md: P-53.
- syzygy-s9q: exact authorized scope, including bounded historical replay.
- BASELINE.json and SCOPE-PROOF.json: scripted predecessor protection and scope.
- The interactive direction is retained in local Beads; it is not a public signed
  adoption record. The candidate remains non-effective until the later owner act.

## Terms introduced / retired

No domain term introduced. The unchecked question-hash alternative is retired
from schema 2.1 only; schema 2.0 semantics remain historical. New version labels
identify the breaking schema and the associated instrument successor.

## Downstream impact and verification

Validation/replay support and selftests move with the successor. Named historical
replay population is Administration 1 and the committed round-2026-08f dry run,
both using full commit identities. No guarantee is made for schema-2.0 records
with abbreviated identities. Stop if the named population requires the excluded
RD-67 repair; do not smuggle it into version-support work.

The two normative source diffs are enumerated in successor.diff and checked
independently in SCOPE-PROOF.json. Before approval, retain policy-semantics and
structured-record reviews against the same frozen successor version. Use the
existing validator/renderer selftests plus positive v2.1 admission, hash rejection
through the CLI, and historical replay after a committed successor. A controlled
mutation restores the alternative and must make the responsible rejection test
fail. The canonical PROJECT-STATUS battery is required in a fresh clone of the
reviewed supporting-code commit, with its output and limits retained.

## Rollback

Before approval, discard only this candidate worktree/package if declined; the
approved root files and historical artifacts remain untouched. After approval,
reversal needs a superseding owner-approved amendment. A code revert alone does
not revoke a policy act. Never rewrite the earlier P-34 approval or its evidence.

## Adoption and regeneration cycle

OWNER-PACKET.md names the exact offered subjects and remaining approval gate.
Only a separately approved transaction may install successor bytes, record the
new owner decision, update current-state routes, and regenerate affected derived
views in one logical change. This candidate does none of those. Performed
manifests, prior reviews and historical administration records remain unchanged.
