# Round 2 dispositions — local-agent dossier sitting

Reviewed record: .syzygy/governance/contracts/candidates/dossier-local-agent-acts/reviews/R-DOSSIER-LOCAL-AGENT-SITTING-2-RAW.md

Verdict of record (the raw's own `Verdict:` line): CONFIRM WITH EXCEPTIONS.
It has six findings, every one a note. Under the owner's 2026-09-26 ruling, a
notes-only round clears the bytes it read. The package bytes are therefore
not edited after this round. Each note is carried here and in the bead
`syzygy-qkea.15`, for a later version or for a round 3 if the lead asks for
one. Every repair below would change reviewed bytes and so retire this
review.

[Marked 2026-10-07: the sentence "The package bytes are therefore not edited
after this round" no longer holds. The lead directed a round 3 (the last
allowed), with notes 2, 3, 4 (in part) and 6 repaired first and note 5 left
as a disposition. Those repairs retire this round's confirmation of the
bytes they change, and `ROUND-3-DISPOSITIONS.md` will carry round 3's
disposition.]

The phrases the five acts take, each the record's label, a colon and its row
of the sitting manifest at the reviewed bytes (the owner selects; nobody
types these):

```text
STATE NO KERNEL EVIDENCE DRAWER FOR REDIS-REDIS: [retired 2026-10-07 — the note 6 repair changed this record; its current row is in the sitting manifest]
CONSENT TO AGENT PROVIDER ANTHROPIC FOR REDIS-REDIS: fbbcd3c0e3d49aab3384a4ab18bf35816dbd8fb952e658d1edbac3d1c50e48a7
CONSENT TO AGENT PROVIDER OPENAI FOR REDIS-REDIS: 07006f9333ca9db0ff8a1ab8a4c37ce58db66780406d78ac79df6894668cd583
BIND D9 TO EXACT BYTES FOR OPERATOR-AGENT RUNS: 41fdfaea8cbde4cd8220910113fb5b376c7834a470d8c2d9badd9ab0fec9ac66
BIND RFC7-20 READING TO EXACT BYTES FOR OPERATOR-AGENT RUNS: f0725a204b6e6ccbccb211441e26e139502ef42a6447d0f4a40df2d09062f3d9
```

The source-acquisition entry takes no phrase. It is signed by version tag
(`record_versioned_signoff.py --record public-git-source-acquisition-local-agent
--version 1.0 --review <the raw above> --disposition <this record>`).

### 1 — note: after an act, an unrelated edit to a bound file fails every recorded act's check; "a new version" has no tooling

Carried. This is fail-closed and not unsafe [Inferred, the reviewer's and
ours]. Before the sitting, nothing changes. After it, the packet's sentence
"an edit affects only the record it touches" is true of the gate's authority
but not of `--check`. A re-act needs a successor package with versioned
record paths, not `--write`, which would overwrite act-bound bytes. Until
that successor is drafted, never run `--write` after any act in this package
is recorded. Bead item (1).

### 2 — note: three act types are record-class nouns

Carried. The act types are rendered by the recorder, not by package bytes,
but changing them changes what the owner's records will say, so this goes to
the bead (item 2: `state-project-input`, `bind-in-force`). It must be done
before any act is recorded or not at all.

### 3 — note: the tag sign-off does not capture the Scope A extension, and its aggregate block says it widens no read

Carried, bead item (3). Before row 2 is offered, the recorder should require
the owner's selection quote for a registry-entry package to name the
extension. Its aggregate sentence should also be tailored the way `does_not`
is. Until then, the lead quotes the option label "Extend Scope A to this
entry and sign v1.0" verbatim as `--owner-selection-quote`, which puts the
extension in the record's `Owner selection:` line.

### 4 — note: residual entry–reader mismatches

Carried, bead item (4):

- `objectRefused` belongs under `awaitingGate`.
- "index" should read "the staging index (`.git/index`)".
- Bounding the work of `listTree` and `readBlobs`, not only their output,
  needs a reader change, which by the entry's own rule is a new entry
  version. This strengthens the packet's sign-after-the-gate alternative.
- `implementationVersion` is bound to no bytes, as in the installed Butlers
  entry.

### 5 — note: the delta's count does not re-derive; three value changes undescribed

Carried, bead item (5). The figure 44 came from a walk that compared lists
whole and treated the `entries` array as a single entry. The reviewer's 45
and 46 come from two other walk rules. A later version states the rule beside
the figure and describes the three value changes:
`outputFactClasses[0].identityScheme`, `resourceLimits.status`, and
`screening`.

### 6 — note: the drawer statement calls Redis "admitted for observation" while that consent is unperformed

Carried, bead item (6). The operative sentence (no drawer exists) stays true.
The basis sentence is exact only once row 1 is signed. Until a later
version, offer row 3 only together with or after row 1, so the basis holds
when the act is recorded.
