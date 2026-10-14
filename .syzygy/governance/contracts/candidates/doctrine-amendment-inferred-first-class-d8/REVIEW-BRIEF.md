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

## Round 3

*(Added 2026-10-14. Everything above is the round-1 brief, left as round 1
and round 2 read it; where this section and the text above differ, this
section governs round 3.)*

**Why a round 3.** Round 2 (`docs/reviews/R-DOCTRINE-AMENDMENT-D8-2-RAW.md`)
returned `REVISE`. The owner, in the lead session on 2026-10-14, directed
one more cycle for this packet: every round-2 finding, notes included,
repaired once, then one fresh review under the same stopping rule. The
repairs are mapped in `ROUND-2-DISPOSITIONS.md`, "Repairs, 2026-10-14
(cycle 2)". The repairing session dispatches no review.

**Stopping rule, set before the round.** One round, the same rule the
2026-10-14 confirmation cycle used
(`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md`):

- a verdict with no revise-level finding clears the exact bytes it read,
  under the owner's 2026-09-26 ruling; its notes go in a sibling record
  beside the package, and the package is not edited;
- a verdict still `REVISE` goes to the owner with its findings; the package
  is not repaired again and no round 4 is dispatched without a new owner
  direction;
- a verdict is never re-labelled.

**Subject.** Every tracked file of
`.syzygy/governance/contracts/candidates/doctrine-amendment-inferred-first-class-d8/`
at the reviewed commit (six files at the repair commit:
`IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`, `REVIEW-BRIEF.md`,
`ROUND-1-DISPOSITIONS.md`, `ROUND-2-DISPOSITIONS.md`, `SEMANTIC-DELTA.md`).

**Governing references.** Those above, plus: RFC7-20 and RFC7-21
(`contracts/rfcs/RFC-0007/narrative-contract.md` lines 414–440); the
generator specification's editorial-draft rules
(`openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`
lines 98 and 528); the PWB coverage part's RFC7-20 row
(`contract-coverage-parts/RFC-0007-0009.md` line 74);
`decisions/DOSSIER-LOCAL-AGENT-RFC7-20-READING-IN-FORCE-ACT.md`;
`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md` Q3; `architecture.md` lines
14–27 and 108–117; `DOCTRINE-AMENDMENT-LOG.md` (D9);
`openspec/changes/polaris-non-governed-narrative-profile/` (REQ-032); both
earlier raws and both dispositions records.

**What to test, at least.**

- Is each of the twelve round-2 findings repaired, as the cycle-2 mapping
  claims, in the bytes rather than only in the mapping?
- **Clause (e), moved and reworded.** Is its new position (after
  `trust-and-evidence.md` line 67, outside the trust floor) and its "adds
  no property to the trust floor" sentence coherent with lines 159–180 and
  VIS-7? Is "not release-blocking as drafted" an honest reading, and is the
  fifth-bullet arm stated fairly?
- **Clause (a) and RFC7-20.** Does "unless the surface admits generated
  prose only as a draft" defer to RFC7-20 without contradicting it, and is
  Q1's rechecked "decline" rationale sound? Is Q-C3 the right instrument
  question, and is the (a)/(f) manifesto overlap now honestly resolved?
- **Clause (d1), reworded and moved.** Is an observed-only project rightly
  a governed project; does "no act in force names a write into it" keep
  the registry field out of doctrine; does the new placement read?
- Are Q-C2's new arms and Q-D1 crisp, and does either pre-decide the owner?
- Do the re-derived figures (term sweep 1,883 / 151 / 438 and the static
  sweep 962 / 52, both at `09c7a61d`) and the application probe reproduce?

**Output.** Write the raw review to
docs/reviews/R-DOCTRINE-AMENDMENT-D8-3-RAW.md (a file this round
creates). Its first four non-blank lines must be exactly:

```text
# Review - D8 doctrine amendment packet (Inferred first-class, P-102) — round 3
Reviewed commit: <the full 40-hex commit you reviewed>
Package digest: <sha256 by the method below, at the reviewed commit>
Verdict: <CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE>
```

**Head contract.** `Package digest` is the package digest by this brief's
scripted method, computed at the reviewed commit and nothing else: at the
repo root of a clone checked out at the reviewed commit,
`sha256sum $(git ls-files .syzygy/governance/contracts/candidates/doctrine-amendment-inferred-first-class-d8 | LC_ALL=C sort) | sha256sum`,
first field. It is not a doctrine file's digest, not a single file's
digest and not a figure copied from this brief or the dispositions. Number
every finding, label each `[Observed]`, `[Inferred]` or `[Unknown]`, and
mark each as revise-level or a note.

## Round 4

*(Added 2026-10-14, before the round, by the cycle-3 repair lane.
Everything above is the brief rounds 1 to 3 read; where this section and
the text above differ, this section governs round 4.)*

**Why a round 4.** Round 3 (`docs/reviews/R-DOCTRINE-AMENDMENT-D8-3-RAW.md`)
returned `REVISE`. On 2026-10-14 the owner, in the lead session, ruled on
its finding and directed one more cycle for P-102: "Drop dismissal from
(d2)" — "Dismissals of an observed-only project's gaps can't live in the
observing project's tree, so VIS-6 stays intact. Then one more cycle."
[Observed: as relayed by the lead session to the repair lane; not yet
recorded under `decisions/`.] The repairs, notes included, are mapped in
`ROUND-3-DISPOSITIONS.md` §"Repairs, 2026-10-14 (cycle 3)". The repairing
session dispatches no review.

**Stopping rule, set before the round.** One round.

- A verdict with **no revise-level finding** (`CONFIRM`, or
  `CONFIRM WITH EXCEPTIONS` whose findings are all notes) clears the exact
  bytes it read, under the owner's 2026-09-26 ruling
  (`../../../decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1).
  Its notes go in a sibling `ROUND-4-DISPOSITIONS.md`, and the package's
  other files are not edited.
- A verdict of **`REVISE`** (any revise-level finding) goes back to the
  owner with its findings open: no further repair and no round 5 without a
  new owner direction.
- A clearance is not adoption; every question in packet §7 stays the
  owner's (VIS-4). A verdict is never re-labelled.

**Subject.** Every tracked file of
`.syzygy/governance/contracts/candidates/doctrine-amendment-inferred-first-class-d8/`
at the reviewed commit: `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`,
`REVIEW-BRIEF.md`, `ROUND-1-DISPOSITIONS.md`, `ROUND-2-DISPOSITIONS.md`,
`ROUND-3-DISPOSITIONS.md`, `SEMANTIC-DELTA.md`.

**Governing references.** Those listed above for rounds 1 and 3, plus:
`trust-and-evidence.md` lines 36–49 and 57–67; VIS-6 in `vision.md`
(lines 229–248), including its violation sentence (246–248);
`packages/polaris-dossier/src/gate-acts.test.ts` around line 298;
`scripts/record_polaris_understanding_adoption.py`; and candidate D7's
packet Q6 and ledger §4
(`../doctrine-amendment-held-derived-computation-d7/`). The reviewer
**SHOULD** read the earlier raws
(`docs/reviews/R-DOCTRINE-AMENDMENT-D8-1-RAW.md`,
`docs/reviews/R-DOCTRINE-AMENDMENT-D8-2-RAW.md` and
`docs/reviews/R-DOCTRINE-AMENDMENT-D8-3-RAW.md`) and
`ROUND-3-DISPOSITIONS.md`, and check each round-3 finding against the
current bytes, not against the dispositions' account of them.

**What to test, at least.**

- Is each of the five round-3 findings repaired as `ROUND-3-DISPOSITIONS.md`
  §"Repairs, 2026-10-14 (cycle 3)" says, and did any repair introduce a
  new inaccuracy?
- **Clause (d2), on the owner's ruling.** Is the dismissal gone from
  (d2)'s content, both as an example and from the general "content Syzygy
  authors" phrase? Does the new sentence state where such a dismissal can
  lawfully live without contradicting `trust-and-evidence.md` lines 42–43
  or VIS-6's violation sentence? Is "a promoted annotation" right where
  the old bytes said "a promoted note", and does "never suppresses a gap"
  overreach? Do §1 (d), §2's (d) row, Q-C2, Q-D1 and the delta now say the
  same thing?
- **Clause (e).** Is the heading no wider than the rule, is the Unknown
  sentence scoped to the denied claim, and is dropping the VIS-7 citation
  right? Is the new Q5 arm stated fairly?
- **Clause (a).** Does "is no claim while it stays one" carry the
  intended reading without licensing more than RFC7-20 and RFC7-21 allow?
- **Ledger §4.** Is the `gate-acts.test.ts` correction right, and does the
  re-run application probe over the repaired blocks reproduce?
- Are the dated status marks at the stale sentences, with the old text
  kept, and is any stale sentence left unmarked?

**Output.** Write the raw review to
docs/reviews/R-DOCTRINE-AMENDMENT-D8-4-RAW.md (a file this round
creates). **Head contract:** its first four non-blank lines must be
exactly these, with nothing appended to the title line:

```text
# Review - D8 doctrine amendment packet (Inferred first-class, P-102) — round 4
Reviewed commit: <the full 40-hex commit you reviewed>
Package digest: <sha256 by the method below, at the reviewed commit>
Verdict: <CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE>
```

`Package digest` is the package digest by this brief's scripted method,
computed **at the reviewed commit** and nothing else: at the repo root of
a clean clone or worktree whose `git rev-parse HEAD` is the reviewed
commit,
`sha256sum $(git ls-files .syzygy/governance/contracts/candidates/doctrine-amendment-inferred-first-class-d8 | LC_ALL=C sort) | sha256sum`,
first field, over the seven files above. It is not a doctrine file's
digest, not a single file's digest and not a figure copied from this brief
or the dispositions. Number every finding, label each `[Observed]`,
`[Inferred]` or `[Unknown]`, and mark each as revise-level or a note;
close with the count of each.
