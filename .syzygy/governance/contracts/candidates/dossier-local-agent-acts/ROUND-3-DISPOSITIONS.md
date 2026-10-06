# Round 3 dispositions — local-agent dossier sitting

Reviewed record: .syzygy/governance/contracts/candidates/dossier-local-agent-acts/reviews/R-DOSSIER-LOCAL-AGENT-SITTING-3-RAW.md

Verdict of record (the raw's own `Verdict:` line): CONFIRM WITH EXCEPTIONS.
Round 3 was the last round allowed. It has four findings, every one a note.
Under the owner's 2026-09-26 ruling, a notes-only round clears the bytes it
read, here the package at `d19ec98b`. The package bytes are not edited after
this round. Each note is carried below and in the bead `syzygy-qkea.15`. Any
repair would change reviewed bytes and need a successor package.

The phrases the five acts take, each the record's label, a colon and its row
of the sitting manifest at the reviewed bytes (the owner selects; nobody
types these):

```text
STATE NO KERNEL EVIDENCE DRAWER FOR REDIS-REDIS: e2dc0e2398cd9094001fc57c892d7090d445efc829c06588eb6ccf7475979f50
CONSENT TO AGENT PROVIDER ANTHROPIC FOR REDIS-REDIS: fbbcd3c0e3d49aab3384a4ab18bf35816dbd8fb952e658d1edbac3d1c50e48a7
CONSENT TO AGENT PROVIDER OPENAI FOR REDIS-REDIS: 07006f9333ca9db0ff8a1ab8a4c37ce58db66780406d78ac79df6894668cd583
BIND D9 TO EXACT BYTES FOR OPERATOR-AGENT RUNS: 41fdfaea8cbde4cd8220910113fb5b376c7834a470d8c2d9badd9ab0fec9ac66
BIND RFC7-20 READING TO EXACT BYTES FOR OPERATOR-AGENT RUNS: f0725a204b6e6ccbccb211441e26e139502ef42a6447d0f4a40df2d09062f3d9
```

The source-acquisition entry takes no phrase. It is signed by version tag:

```text
record_versioned_signoff.py --record public-git-source-acquisition-local-agent
  --version 1.0 --review <the raw above> --disposition <this record>
  --owner-selection-quote "<the selected option label>"
```

The selected option label must contain "Extend Scope A", or the recorder
refuses.

### 1 — note: the packet's "an edit affects only the record it touches" is true of the gate, not of `--check`

Carried, as round 2 note 1 was. This is fail-closed [Inferred, the
reviewer's and ours]. When the owner is offered rows 4 and 5, say aloud that
after any act is recorded, an edit to a bound file turns every recorder
`--check` red until a successor package is drafted. Never run `--write`
after any act in this package is recorded. Bead item (1).

### 2 — note: `objectRefused.note` names per-call bounds the entry does not declare, and lists the reader's refusals incompletely

Carried to the entry's next version (bead item 4). The reader on PR #367 has
three per-call bounds that refuse `budget-exceeded`:

- `maxDeltaChainDepth`;
- `maxInflatedBytesPerCall`;
- `maxObjectsPerCall`.

The next version should declare all three in `resourceLimits` with their
values. It should also either list every `GitObjectReadRefusalReason` or
drop the delta row's "the refusals of the reader as repaired" claim.

Every listed outcome refuses, so nothing is widened.

### 3 — note: recorder residues

- **The frozen-constant comment.** Repaired in this freeze commit. The
  comment now reads "re-frozen only by a later confirming round", which is
  what this commit does.
- **The stale post-record instruction.** The recorder still prints "add the
  performed-act registration". Carried. Registration has been existence-gated
  since `11d01c25`, so after a record, ignore that line and run
  `check_governance.py`.
- **The substring Scope A check.** Carried. The lead passes the selected
  option label verbatim, so a negated quote cannot arise in practice
  [Inferred].

Bead item (3).

### 4 — note: `implementationVersion` is bound to no reader bytes, and the reader changed under it before merge

Carried, bead item (4). The entry defines 1.0.0 as the file "as merged". The
packet's sign-after-merge alternative stands, and the lead should prefer it:
offer row 2 only after PR #367 merges.

### Round 2 note 5, still carried

The semantic delta's key count does not re-derive, and three value changes
are undescribed. This is carried to the entry's next version (bead item 5).
