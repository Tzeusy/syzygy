# Review — dossier-local-agent-acts and public-git-source-acquisition-local-agent, round 1
Reviewed commit: 8472acee69a1fcdb962e9f58b87ded463573b119
Manifest SHA-256: 8b3d89721825725c30276e4dc123b7e78d55a333b8ab6d3bc0d5f3082b524bd8
Verdict: REVISE

Reviewer: fresh-context subagent, 2026-10-06. Read-only, in a fresh
`git clone --no-local` checked out at the commit above. Packages reviewed:
`dossier-local-agent-acts` and `public-git-source-acquisition-local-agent`.
No owner act performed and no repository file changed. Nothing was read from
Redis or any other external repository; the only network use was
`git fetch` of this repository's own origin to read the reader of PR #367
(`origin/agent/dossier-s2-object-reader` at
`3a84d4a4c599197f1972c797a70e05ddd6e3546d`).

The manifest digest above was recomputed in the clone by
`python3 scripts/build_dossier_local_agent_acts.py --manifest-digest` and by
`sha256sum` over the manifest file; both print the same value.

## Checks run (final lines, verbatim)

```text
$ python3 scripts/check_governance.py | tail -1
32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted
$ python3 scripts/build_dossier_local_agent_acts.py --selftest | tail -1
selftest: 12 of 12 predicates held
$ python3 scripts/record_dossier_local_agent_acts.py --selftest | tail -1
selftest: 33 of 33 predicates held
$ python3 scripts/build_public_git_source_acquisition_local_agent.py --selftest | tail -1
selftest: 31 of 31 predicates held
$ python3 scripts/record_versioned_signoff.py --selftest | tail -1
81 fixtures, 0 failing
$ python3 scripts/build_dossier_local_agent_acts.py --check
dossier-local-agent-acts: records and manifest current
$ python3 scripts/build_public_git_source_acquisition_local_agent.py --check
public-git-source-acquisition-local-agent: unapplied, verifies
$ python3 scripts/build_dossier_local_agent_acts.py --manifest-digest
8b3d89721825725c30276e4dc123b7e78d55a333b8ab6d3bc0d5f3082b524bd8
```

All exited 0. I also ran `record_versioned_signoff.py --check <key> --version 1.0`
for all 8 keys in `real_packages()`. The 7 earlier ones each print
"regenerates exactly; applied tree verified", and
`public-git-source-acquisition-local-agent` prints "not performed" [Observed].

## Independent mechanics probes (criterion 6) [Observed]

- Live `--record d9-in-force <its row>` on the reviewed tree prints
  "FAILED (nothing written): no confirming review is recorded:
  FROZEN_SUBJECT is unset" and exits 1. `git status` is clean afterwards.
- In a scratch copy with `FROZEN_SUBJECT` and `FROZEN_FILE_DIGESTS` set from
  the live files and a synthetic raw, `validate()` gives these results:
  - it accepts the D9 row when the raw's head carries the manifest FILE digest;
  - it refuses when the head carries the D9 row instead ("does not bind the
    manifest file's SHA-256");
  - it refuses the registry-entry row and the OpenAI row offered as the D9
    argument ("is not the d9-in-force manifest row");
  - it refuses after a one-byte append to the RULINGS direction file (for
    the RFC7-20 act, and also for the drawer act) and after a one-byte
    append to `security.md` (for the D9 act), each as "builder reports stale
    records or manifest".
- `check_governance._act_subjects()` returns 50 labels, 50 of them distinct.
  All five new labels are present, and no new label is a prefix of any
  registered label, or the other way round.

## Findings

**Finding 1 — The version-tag sign-off record of the registry entry omits RFC3-16(b) items the contract makes mandatory** (revise)

Criterion 2 (each act is "bound to its artifact's exact digest under
RFC3-16(b)") and criterion 6 (the versioned record).

An adapter-registry entry is "honored **only under RFC3-16(a)**" (RFC4-7,
`.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md:189-191`).
RFC3-16(b) lists what "Every owner act, in either provenance state, binds at
minimum", including "6. the **act instant**" (RFC-0003
`governance-homes-and-owner-acts.md:287`) and "9. the **A1 audit-record
identity or its explicit absence** … Omitting the field is invalid"
(`:294-297`). Only "A state-(1) act satisfying items 1–8 and explicitly
recording item 9 absent is effective under RFC3-16(a)" (`:301-302`).

The record that `scripts/record_versioned_signoff.py` writes for this package
(`render_record`, lines 452-500, with `installed_lines` at 429-436) has these
gaps:

- It carries `Date:` only (line 457). There is no instant.
- It has no provenance-state line and no A1 line.
- It has no act type. `Kind: registry entry` (line 467) names an artifact
  class, not an act type.

The aggregate block (`render_aggregate`) adds none of these. The new code
added only item 3, the installed SHA-256.

By contrast, the dossier recorder's own records carry all nine items:
`record_dossier_local_agent_acts.py:296-322` has "Recorded at (UTC)", "Act
type", "Provenance state" and "A1 audit-record identity … **explicitly
absent**". Every earlier registry act (`PWB-OBSERVER-REGISTRY-ENTRY-ACT.md`
and its amendments) was a digest act.

The packet nevertheless presents the tag record as meeting RFC3-16 by naming
the SHA-256 (`OWNER-SITTING-PACKET.md:77-81`). The semantic delta repeats
this: "so the RFC3-16(a) cross-check can be exact-digest"
(`SEMANTIC-DELTA.md:56-59`). As drafted, a gate applying RFC3-16(a) to the
registry entry would find an act record that is invalid by RFC3-16(b)'s own
words. That is the case where the read is refused, or where RFC3-16 is read
more loosely than it is written.

Remedy:

- Option A: give the registry-entry package's record the missing items (a
  UTC instant, the act type, the explicit state-(1) provenance, and A1
  absent), with a selftest fixture.
- Option B: name in the packet that a Scope A tag sign-off of a
  registry entry is a reading of RFC3-16(b) that omits items 6 and 9, and
  leave that choice to the owner.

**Finding 2 — The entry calls the reader "implemented" for behaviour the reader does not perform** (revise)

Criterion 4 ("The registry entry matches what the reader does").

These match the reader of PR #367 [Observed, `git-object-reader.ts` at
`3a84d4a4`]:

- no fetch, no network and no write: no write call or child process exists
  in the file;
- no working-tree read;
- only `objects/` loose files and `objects/pack/*.idx`/`.pack` are read
  (lines 175-198); `objects/info/alternates` is only `lstat`-ed for an error
  message (line 196);
- the algorithm comes from the identifier's length (lines 46-50);
- re-hashing on every call (lines 84-87 and 206-212);
- a gitlink refuses as `not-a-blob` (line 130), and a non-commit pin refuses
  as `type-mismatch`.

`implementationStatus` says "implemented by syzygy-qkea.3 (S2) as
openPinnedObjectReader in the file named by implementation"
(`POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-CANDIDATE.json:14`).
`implementation` names only that file (line 178). Much of what the entry
declares is not in that file:

- `resourceLimits` `maxSources`, `maxBytesPerSource`, `maxTotalBytes` and
  `maxTreeEntries` (lines 116-119), with their semantics (lines 123-127),
  are not enforced. The reader takes only `maxObjectBytes` (lines 77-78).
  `listTree()` lists every entry with no cap (lines 96 and 136-144). That is
  the opposite of `maxTreeEntries`'s "an excess keeps the entries already
  listed, lists no more".
- `maxBytesPerSource`'s "a larger blob is excluded with a recorded reason …
  the run does not fail" is not reader behaviour. `readBlobs` returns whole
  blobs up to 1 GiB, and "One refusal refuses the whole call" (lines 65-67).
- Of the `outputFactClasses`, `pinned-object-read-record`,
  `content-exclusion` and `unknown` (lines 66-87), and the screening of
  line 113, are not produced by the reader. Its own header says
  "Classification and screening of what it returns … are the caller's"
  (line 17).
- No file under `packages/polaris-dossier/` on that branch mentions any of
  the four limits. `git grep` for `maxSources`, `maxTreeEntries`,
  `maxTotalBytes` and `maxBytesPerSource` over the package's 14 tracked
  files returns 0 hits [Observed].

Neither the entry nor the packet says which declared behaviours belong to
gate code that does not exist yet. The packet's "What else a real Redis run
still needs" (`OWNER-SITTING-PACKET.md:158-162`) names only the act
cross-check. An owner signing "implemented" would sign a claim that the
named file does not make true.

Remedy:

- Option A: restate `implementationStatus` (and the semantic delta's row for
  it, `SEMANTIC-DELTA.md:29`) to say which declarations the reader
  implements and which await the dossier gate, and name that gap in the
  packet.
- Option B: mark the four limits and the three output classes as
  unimplemented until that code lands.

**Finding 3 — An unrelated edit to any bound file blocks every act in the sitting, not only the one bound to it** (note)

Criterion 6. `validate()` refuses any act while `build.stale()` is non-empty
(`record_dossier_local_agent_acts.py:257-258`). `stale()` covers every
record in the package (`build_dossier_local_agent_acts.py:112-132`).
`FROZEN_FILE_DIGESTS` also covers every record (lines 93-95 and 264-267).

So a one-byte edit to the RULINGS direction refuses the drawer statement and
both provider statements, which bind nothing in that file. I observed this
refusal for the drawer act in the probe above, and the selftest's end-to-end
case asserts it for a `v1.md` edit (lines 648-651). After `--write`
regenerates the affected record, the sitting manifest changes. That retires
the frozen review for all five acts, and for the registry-entry sign-off,
whose `subject` is that manifest (`record_versioned_signoff.py:243`).

This is fail-closed and not wrong. But the packet says "declining one never
undoes another" (`OWNER-SITTING-PACKET.md:38`), and its cost paragraph
(lines 144-150) names only the edited file's own record. The cost is
broader: any edit to `security.md`, `v1.md` or the direction file before
every act is recorded needs a new review round for the whole sitting. Say so
in the cost paragraph, or scope the stale check to the act's own record.

**Finding 4 — The packet does not name the stretch in calling a digest-less adoption "enough to adopt" under RFC3-16** (note)

Criterion 2 ("any reading that stretches RFC3-16 is named").

RFC3-16 says "The **effective** lifecycle status of a normative or
authorization-bearing artifact is determined by an **owner-act record** …
binding the act to the artifact's **exact immutable content digest**"
(`governance-homes-and-owner-acts.md:134-139`). It also says "An artifact
with **no** owner-act record at all has effective status **unadopted**"
(`:155-156`).

The packet says D9 and the reading were "decided by your own words without a
digest … That was enough to adopt them, but not for the check Syzygy runs"
(`OWNER-SITTING-PACKET.md:126-129`). The D9 record says "this record does
not adopt it again" (`D9-IN-FORCE-RECORD.md:38-39`).

Under RFC3-16 read literally, the in-force act is the digest-bound act that
gives the doctrine bytes effective status. It binds them only through the
record: its `Exact digest` is the record's, and the doctrine digests sit
inside the record (`record_dossier_local_agent_acts.py:310-312`;
`D9-IN-FORCE-RECORD.md:26-29`).

"New usage" (`OWNER-SITTING-PACKET.md:148-150`) is disclosed. What is not
named is that this two-step binding, through a record rather than over the
doctrine file itself, and the "enough to adopt" premise are readings of
RFC3-16 that a reviewer may contest. [Inferred] The doctrine corpus has
followed this convention throughout: no doctrine digest act appears in
`ACCEPTANCE-ACT-RECORD.md`.

Suggested repair: one sentence naming both readings.

**Finding 5 — Row 5 adds the record the owner's RFC7-20 choice was described as not needing** (note)

Criterion 7 and the preservation of the owner's trade-off.

The owner chose "Rule it by interpretation", described as shown as "No extra
record, but it rests on an interpretation"
(`POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md:28`). Row 5 asks the owner
to sign an extra record so that the reading is in force
(`OWNER-SITTING-PACKET.md:36` and `:124-142`). Row 3's argument also cites
that choice as a reason to prefer the drawer record (lines 108-110).

R3-F8 is the source of the new requirement, and the packet cites it
(lines 20-22). But the packet does not tell the owner that the option chosen
was presented as needing no record, and that this row changes that. The
owner should see that before signing.

**Finding 6 — A miscount and two ambiguities in the packet** (note)

Criterion 7.

- `OWNER-SITTING-PACKET.md:21-24`: "a consent, a registry entry, a
  per-project statement, D9 and your RFC7-20 reading … Today four of those
  have no such act". All five have none. The Redis observation consent is
  unperformed [Observed: `redis-observation` appears 0 times in
  `ACCEPTANCE-ACT-RECORD.md`, and no Redis act record is in `decisions/`].
- Line 118: "the five that the prepared Anthropic egress record already
  names for Redis". Two prepared Anthropic egress records exist:
  - `public-repo-admission/instances/egress-anthropic/` has five classes;
  - `public-egress-v2/instances/egress-anthropic/` has six, adding
    `project-documentation`.

  Name which one is meant. The five chosen are the RFC5-14 vocabulary the
  statements cite, which is consistent.
- Line 64 calls the entry "version 2.0.0-candidate.1", and line 73 asks the
  owner to "sign version 1.0". The package's sign-off version and the
  entry's `observerVersion` are different numbers. One clause saying so
  would prevent confusion.
- Table row 3 (line 32) says signing lets Syzygy "treat Redis as an
  ungoverned project" without the tree condition. Lines 111-114 supply it,
  so the table cell overstates on its own.

**Finding 7 — The semantic delta leaves out three entry changes** (note)

Criterion 4 ("every changed field is in `SEMANTIC-DELTA.md`").

A key-level diff of the parked and proposed entries, which I computed by
script, finds three changes that no table row names:

- `governingBehaviorContract.signedBy`: "pending exact owner act over this
  entry" became "pending the owner's version-tagged sign-off of this
  package". The table's `governingBehaviorContract` row (line 44) describes
  only the version.
- `failureStates.revisionNotAdmitted.executionFact`: "refused before any
  fetch" became "refused before any object is read", and its `note` was also
  reworded. Row 39 describes only the removed and added failure states.
- `authorizationModeDerivation` now requires "the effective classification
  and public-source screening policy acts". Row 42 says "the same, plus" the
  write-reach sentence, which understates the change. Also,
  `admissionFailureMapping` has no key for a missing or stale classification
  policy act, although that act is now a stated precondition.

Every other changed, added and removed key is covered by a row.

## Criteria with no finding

- Criterion 1 holds:
  - The drawer statement decides only the drawer half
    (`NO-EVIDENCE-DRAWER-STATEMENT.md:32-38`).
  - Each provider statement is called SEC-2's per-project consent, "not an
    egress record", and says the classes "do not limit what the agent reads
    or sends" (`AGENT-PROVIDER-STATEMENT-*.md:39-58`).
  - The D9 and RFC7-20 records adopt nothing again and change no byte. The
    RFC7-20 record is scoped to item 1 only (`RFC7-20-READING-IN-FORCE-RECORD.md:18`
    and `:53-55`).
- Criterion 3 holds:
  - The recommendation follows REQ-033's non-governed scenario ("the
    admitted project input states that no kernel evidence drawer exists and
    the pinned tree holds no `openspec/**` path and no `.syzygy/` path").
  - A silent input is treated as needing a statement.
  - The fail-closed fallback is stated.
  - Redis-tree claims are labelled [Inferred] (lines 101-102 and 112-114).
- Criterion 5 holds: the packet offers the Scope A extension as the owner's
  choice (lines 73-77 and 175).
- Criterion 6 holds apart from Findings 1 and 3, as the probes above show.
