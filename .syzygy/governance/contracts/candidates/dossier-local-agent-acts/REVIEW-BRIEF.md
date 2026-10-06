# Review brief — local-agent dossier sitting (G5)

> **Candidate — binds nothing.** Brief for a fresh-context review of the
> sitting's records, its registry entry and its owner packet. A review
> performs no act.

## What to review

Two candidate packages and the scripts that would record them:

- `.syzygy/governance/contracts/candidates/dossier-local-agent-acts/`: the
  owner packet `OWNER-SITTING-PACKET.md`, four templates, two `params.json`
  files, five generated records and `DOSSIER-LOCAL-AGENT-SITTING-MANIFEST.txt`;
- `.syzygy/governance/contracts/candidates/public-git-source-acquisition-local-agent/`:
  the proposed entry and `SEMANTIC-DELTA.md`;
- `scripts/build_dossier_local_agent_acts.py`,
  `scripts/record_dossier_local_agent_acts.py`,
  `scripts/build_public_git_source_acquisition_local_agent.py`, the new
  package row and record wording in `scripts/record_versioned_signoff.py`, and
  the registration in `scripts/check_governance.py`
  (`DOSSIER_LOCAL_AGENT_*`).

## Round 3 — what changed since round 2

Round 2 (`reviews/R-DOSSIER-LOCAL-AGENT-SITTING-2-RAW.md`) returned `CONFIRM
WITH EXCEPTIONS` with six notes. The lead had the following repaired before
this round, the last one allowed:

- **Note 2.** The act types are now verbs: `state-project-input` for the drawer
  statement, `bind-exact-bytes` for the D9 and RFC7-20 records, and
  `consent-agent-provider` unchanged.
- **Note 3.**
  - For a package that installs a registry entry, `record_versioned_signoff.py`
    requires the owner's selection quote to contain `Extend Scope A`, both
    when recording and at `--check`.
  - The dedicated record carries a `Scope A extension` line.
  - The aggregate block's closing sentence for such a package says the
    sign-off is one of the acts a read needs, no longer that it widens no
    read.
- **Note 4, in part.**
  - `failureStates.objectRefused` moved to `implementationCoverage.awaitingGate`,
    since the mapping is the gate's.
  - `readAuthority` says "staging index (`.git/index`)" and that pack indexes
    are read.
  - `objectRefused.note` lists the refusals of the reader as repaired on PR
    #367.
  - `SEMANTIC-DELTA.md` rows changed to match.
  - Not repaired: `implementationVersion` is still bound to no reader bytes
    (as with the installed Butlers entry), and the two limits the gate
    enforces after the reader's work.
- **Note 5** is left as a disposition note.
- **Note 6.**
  - The drawer statement's basis no longer assumes the observation consent is
    in force.
  - The packet's recommendation says the same.
  - The packet says the rows are asked in table order, the observation
    consent (row 1) before the drawer statement (row 3).
- Also changed:
  - `ROUND-2-DISPOSITIONS.md` marks its "not edited after this round"
    sentence as no longer holding, and retires its drawer phrase.
  - `check_governance.py` registers each round's dispositions file per label.
  - `PENDING-OWNER-DECISIONS.md` gains row P-104 and a dated note.

The reader on PR #367 has itself been repaired since round 2 (review
R-POLARIS-DOSSIER-S2-READER-1). Read it at that branch's current head.

## Governing references

- `openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md`,
  REQ-polaris-generation-033 (signed off v1.0), and its review note R3-F8 in
  `.syzygy/governance/contracts/candidates/POLARIS-DOSSIER-LOCAL-AGENT-MODE-REVIEW-NOTES.md`;
- RFC3-16, RFC3-16(a) and RFC3-16(b) in
  `.syzygy/governance/contracts/rfcs/RFC-0003/governance-homes-and-owner-acts.md`;
- SEC-2 and SEC-3 in `.syzygy/governance/doctrine/security.md`; D9 in
  `.syzygy/governance/decisions/DOCTRINE-AMENDMENT-LOG.md`;
- the direction `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md`;
- Scope A, `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`;
- the parked predecessor entry
  `.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-CANDIDATE.json`,
  the installed Butlers entry under `.syzygy/governance/declarations/adapter-registry/`,
  and the Redis observation consent under
  `.syzygy/governance/contracts/candidates/public-repo-admission/instances/redis/`;
- the reader the entry names, `packages/polaris-dossier/src/git-object-reader.ts`,
  on the branch of PR #367 (absent from main until it merges; read it with
  `git show origin/agent/dossier-s2-object-reader:<path>` after `git fetch`).

## Acceptance criteria

1. **Each record does exactly what its packet row says** and no more: the
   drawer statement decides only the drawer half of REQ-033's governed
   predicate; each provider statement is the SEC-2 per-project consent REQ-033
   describes, is not an egress record, and says the classes do not bind the
   agent; the D9 record and the RFC7-20 record adopt nothing again, change no
   doctrine or direction byte, and are scoped as stated (item 1 only for the
   reading).
2. **RFC3-16(a) fit.** Each act would be current, attributable, scope-matched
   and bound to its artifact's exact digest under RFC3-16(b); the whole-file
   binding of `security.md`, `v1.md` and the direction file is stated with its
   cost; any reading that stretches RFC3-16 is named.
3. **The recommendation in row 3** follows from REQ-033 as signed: the drawer
   statement plus the tree check makes Redis non-governed, a silent input
   does not, and the fallback is honest. Claims about Redis's tree are
   labelled [Inferred] and nothing was read from Redis.
4. **The registry entry** matches what the reader does (no fetch, no network,
   no write outside Syzygy's state directory, no working tree, no execution,
   the clone files it ignores, re-hashing), every changed field is in
   `SEMANTIC-DELTA.md`, and nothing in it is copied from the provider mode
   that the local-agent mode no longer does.
5. **Scope A.** The packet does not treat this entry as already covered by
   Scope A; the extension is the owner's.
6. **Mechanics.** Each recorder refuses while unfrozen, binds the review by the
   manifest FILE's SHA-256 in the raw's first four non-blank lines, rejects
   any argument other than its own row (the registry-entry row included), and
   refuses when a bound doctrine or direction file changes; the versioned
   sign-off record for the entry names the installed bytes' SHA-256 and every
   earlier sign-off record still regenerates exactly. The registered labels
   are distinct and no label is a prefix of another.
7. **The packet is readable by the owner**: plain words, what each signature
   unlocks, what declining costs, no digest, nothing presented as decided.
8. **Round 2's notes** are repaired as listed above, or carried to a later
   version where the list says so, and each repair introduces no new
   mismatch with criteria 1–7.

## Output

Write the raw to `reviews/R-DOSSIER-LOCAL-AGENT-SITTING-<n>-RAW.md`. Its first
four non-blank lines must be, in this order:

```text
# Review — dossier-local-agent-acts and public-git-source-acquisition-local-agent, round <n>
Reviewed commit: <40-hex commit you read>
Manifest SHA-256: <SHA-256 of DOSSIER-LOCAL-AGENT-SITTING-MANIFEST.txt, the FILE>
Verdict: <CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE>
```

The manifest line carries the SHA-256 of the manifest file itself
(`python3 scripts/build_dossier_local_agent_acts.py --manifest-digest`), never
one of its rows. Then a `## Findings` section, each finding headed
`**Finding N — title** (blocking|revise|note)`, numbered from 1, with the
evidence (file and line) and the criterion it fails. CONFIRM WITH EXCEPTIONS
means notes only. Run `python3 scripts/check_governance.py`, the three new
scripts' `--selftest` and `record_versioned_signoff.py --selftest`, and report
their final lines.
