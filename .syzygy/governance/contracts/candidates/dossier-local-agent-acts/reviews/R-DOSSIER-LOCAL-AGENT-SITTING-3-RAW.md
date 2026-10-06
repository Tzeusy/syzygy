# Review — dossier-local-agent-acts and public-git-source-acquisition-local-agent, round 3
Reviewed commit: d19ec98bb3bfb9c83f48919715cb5b8c7710ede8
Manifest SHA-256: ecf916c4f67c2ba8c8a33739653eef75a36874b925bd28e08852219243f1fb56
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context subagent, 2026-10-07. I worked read-only in a fresh
`git clone --no-local -b governance/dossier-g5-sitting`, at the commit above.
I performed no owner act and changed no file in the repository or its
worktrees. I ran the probes in one further scratch clone, which I discarded.
I read nothing from Redis or any other external repository. My only network
use was `git fetch origin agent/dossier-s2-object-reader`. FETCH_HEAD is
`f3743f51fc76e21f67a5162089d067c5441614d1`, and I read
`packages/polaris-dossier/src/git-object-reader.ts` (490 lines) at that head
with `git show FETCH_HEAD:<path>`.

Manifest digest [Observed]: both
`python3 scripts/build_dossier_local_agent_acts.py --manifest-digest` and
`sha256sum` over `DOSSIER-LOCAL-AGENT-SITTING-MANIFEST.txt` print the value
in the head above. It equals the expected value.

## Checks run (final lines, verbatim)

```text
$ python3 scripts/check_governance.py
32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted
$ python3 scripts/build_dossier_local_agent_acts.py --selftest
selftest: 12 of 12 predicates held
$ python3 scripts/record_dossier_local_agent_acts.py --selftest
selftest: 34 of 34 predicates held
$ python3 scripts/build_public_git_source_acquisition_local_agent.py --selftest
selftest: 36 of 36 predicates held
$ python3 scripts/record_versioned_signoff.py --selftest
86 fixtures, 0 failing
$ python3 scripts/build_dossier_local_agent_acts.py --check
dossier-local-agent-acts: records and manifest current
$ python3 scripts/build_public_git_source_acquisition_local_agent.py --check
public-git-source-acquisition-local-agent: unapplied, verifies
```

All of these exited 0. I also ran
`record_versioned_signoff.py --check <key> --version 1.0` for all 8 keys of
`real_packages()`:

- The 7 earlier keys each print `recorded <key> v1.0 sign-off regenerates
  exactly; applied tree verified`.
- `public-git-source-acquisition-local-agent` prints `v1.0: not performed`.

Of the 8 packages, only `public-git-source-acquisition-local-agent` has
`installed` set. So the new Scope A quote check (`validate_inputs(..., pkg)`,
which also runs at `--check`) cannot fail any earlier record [Observed].

## Mechanics probes (criterion 6) [Observed]

**On the reviewed tree.** `record_dossier_local_agent_acts.py --record` was
run with the current manifest rows and a full option set.

- `d9-in-force` and `redis-no-evidence-drawer` each refuse with "frozen
  subject does not carry the presented bytes of
  …/DOSSIER-LOCAL-AGENT-SITTING-MANIFEST.txt" and exit 1.
  - The recorder is still frozen to round 2: `FROZEN_SUBJECT = "c26aaf34…"`
    at `scripts/record_dossier_local_agent_acts.py:92`, with round-2 file
    digests.
  - So it fails closed until it is re-frozen.
- `d9-in-force` given the registry-entry row is refused: "owner argument
  917aecc7… is not the d9-in-force manifest row 41fdfaea…".
- Nothing was written.

**Simulated round-3 freeze.** In a scratch clone I made these changes and
committed them:

- set `FROZEN_SUBJECT` to the reviewed commit;
- hashed `FROZEN_FILE_DIGESTS` live from `frozen_rels()` (14 files);
- pointed `CONFIRMATION_REVIEW_REL` at a synthetic CONFIRM raw whose head
  carries the manifest FILE digest.

Results:

- All five acts record (exit 0). The dedicated records render
  ``Act type: `state-project-input` ``, `consent-agent-provider` (twice) and
  `bind-exact-bytes` (twice).
- `check_governance.py` then still reports 0 FAIL.
- Each `--check` passes.
- After a one-line append to `security.md`, `--check` fails for `d9-in-force`.
  It also fails for `redis-no-evidence-drawer`, which binds nothing in
  `security.md` ("builder reports stale records or manifest:
  …/D9-IN-FORCE-RECORD.md: differs from its regeneration"). See Finding 1.

**Same clone, with the PR #367 reader file committed.**

- `record_versioned_signoff.py --record public-git-source-acquisition-local-agent --version 1.0 …`
  with `--owner-selection-quote "Sign it"` is refused: "owner selection
  quote must name the Scope A extension ('Extend Scope A') …".
- With "Extend Scope A to this entry and sign v1.0" it records. The record
  carries these lines:
  - ``Act type: `adopt-registry-entry` ``
  - `Installed entry SHA-256: 917aecc766f01133d5a29c1ee8b3e575332ad48d04308a1b62c68217e48d254b`
    (equal to `sha256sum` of the installed file and to the manifest row)
  - `Scope A extension: the owner's selection quoted above names it ("Extend Scope A") …`
- The aggregate block closes "This sign-off approves the registry entry its
  dedicated record names … That is one of the separate acts a read needs.
  It gives no observation consent …".
- Its `--check` prints "regenerates exactly; applied tree verified".

**Labels.** `check_governance._act_subjects()` gives 50 labels, 50 distinct.
The only prefix pair is the older, unrelated `CONSENT TO PUBLIC TARGET
EGRESS TO ANTHROPIC` / `… VERSION 2`, as in round 2.

**Register.** The P-104 note's counts re-derive: 31 rows under "Open, and
only the owner can dispose", 5 acceptance-act rows, 36 in all. That is
`^\| P-[0-9]+[^ |]*` per `##` section, via Python `re`. The file had 35 at
`c26aaf34`.

## Round-2 notes: repair status (criterion 8)

- **Note 2 — repaired.** `ACTS` uses `state-project-input` and
  `bind-exact-bytes` (`record_dossier_local_agent_acts.py:159, 190, 199`),
  and the dedicated records render them (probe above).
- **Note 3 — repaired.**
  - `SCOPE_A_EXTENSION` is required at record and at `--check`
    (`record_versioned_signoff.py:280-296, 650`).
  - The record carries the `Scope A extension` line (`:461-463`).
  - `aggregate_scope` tailors the closing sentence (`:531-540`).
  - The packet's row-2 option label "Extend Scope A to this entry and sign
    v1.0" (`OWNER-SITTING-PACKET.md:216`) satisfies the check.
- **Note 4 — repaired in part, as the brief lists.**
  - `failureStates.objectRefused` is now under `awaitingGate` (entry line
    38). The coverage status names `GitObjectReadRefusal` (line 46).
  - `readAuthority` says "staging index (`.git/index`; the pack indexes under
    `objects/pack/` are read)" (line 139).
  - `objectRefused.note` was widened (line 171).
  - The matching `SEMANTIC-DELTA.md` rows changed (lines 30, 36, 40).
  - The unrepaired residues are as the brief says. Finding 2 covers a new
    mismatch the widened note introduces.
- **Note 5 — left as a disposition note, as stated.** `SEMANTIC-DELTA.md`
  line 23 still reads "44 keys" with no walk rule. The round-3 edits touched
  only keys that already differed, so the stated figure is no more or less
  derivable than before [Inferred].
- **Note 6 — repaired.**
  - The drawer statement's basis now reads "offered for observation only, and
    observed only while the observation consent … is in force … This
    statement stays true whether or not that consent is signed"
    (`NO-EVIDENCE-DRAWER-STATEMENT.md:23`; `params.json:5`).
  - The packet's recommendation matches (lines 116-119).
  - The packet states table order, with row 1 before row 3 (lines 210-211).
- **Note 1 — not on the brief's round-3 list.** It is carried in
  `ROUND-2-DISPOSITIONS.md:36-44`, but the packet sentence it named is
  unchanged. See Finding 1.

## Findings

**Finding 1 — The packet still says a post-act edit "affects only the record it touches"; `--check` behaves otherwise** (note)

Criteria 2 (whole-file binding "stated with its cost") and 8.

`OWNER-SITTING-PACKET.md:185` still reads "After an act is recorded, an edit
affects only the record it touches."

[Observed] My probe above reproduces round-2 Finding 1: an unrelated append
to `security.md` turns the drawer act's `--check` red. Two causes:

- `validate()` refuses while `build.stale()` is non-empty;
- `validate()` compares every frozen package file
  (`record_dossier_local_agent_acts.py:280-293`).

`ROUND-2-DISPOSITIONS.md:39-44` concedes the sentence holds of the gate's
authority but not of `--check`. It also says that a re-act needs a successor
package and that `--write` must never run after any act. None of this
reaches the owner: the packet sentence is unqualified, and the brief's
round-3 list does not mention note 1 at all.

[Inferred] It stays fail-closed: the gate would honour each act by its own
record's digest. So this is a note.

Before the sitting, a short qualifier would make the cost exact, for example
"…for the gate; the recorders' own checks for every act go red until a
successor package is drafted".

**Finding 2 — The widened `objectRefused.note` cites per-call bounds the entry never declares, and its list of reader refusals is not complete** (note)

Criteria 4 and 8 (a repair introducing a new mismatch).

Entry line 171 now lists "… unreadable store or exceeded per-call bound".
`SEMANTIC-DELTA.md:40` calls the list "the refusals of the reader as repaired
on PR #367".

[Observed] At `f3743f51` the reader has three per-call bounds beyond
`maxObjectBytes`, each refusing `budget-exceeded` (reader lines 98-103,
110-111, 275, 280, 328):

- `maxDeltaChainDepth` (default 1,000);
- `maxInflatedBytesPerCall` (default 4 GiB);
- `maxObjectsPerCall` (default 1,000,000).

None of the three appears anywhere in the entry or the delta: a search for
`PerCall`, `DeltaChain` and `budget` hits only `deferred-by-budget`.
Consequences:

- `resourceLimits` (lines 151-158) and `implementationCoverage.reader`
  (lines 16-26) name only `maxObjectBytes` among the reader's limits.
- So the `resource-limits` input class (`canonical-json-sha256`, line 100)
  does not identify bounds that can refuse a step.
- [Inferred] The entry also does not say whether the gate may set them.

The list also omits several reader refusals, unless "undecodable" is read
broadly:

- `path-not-found`;
- `malformed-path`;
- `malformed-identifier`;
- `not-a-git-directory` (a `.git` that is a link or file, reader line 252);
- `invalid-pack-index`.

The note also calls `malformed-tree` "ambiguous tree entry". But the reader
also refuses truncated entries and modes git does not write under that
reason (reader lines 208-215).

All of these refuse, so nothing is widened. This is a note. A later version
should do two things:

- declare the three bounds, with their values, in `resourceLimits`;
- either list every `GitObjectReadRefusalReason` or drop the completeness
  claim in the delta row.

**Finding 3 — Recorder residues: the frozen-constant comment, a stale post-record instruction, and a substring Scope A check** (note)

Criterion 6.

- **The frozen-constant comment.** `record_dossier_local_agent_acts.py:88-91`
  says `FROZEN_SUBJECT` and the two paths are "never hand-edited again" once
  a round returns. They were set to round 2 in `7c69781b`. A confirming
  round 3 now requires editing them again: `FROZEN_SUBJECT`, the 14 file
  digests, `CONFIRMATION_REVIEW_REL` and `DISPOSITION_REL`. The edit is
  necessary and fails closed until made (probe above). The comment should
  say "re-frozen per confirming round" rather than forbid what the process
  needs.
- **The stale post-record instruction.** After a successful record, the
  recorder prints "scripts/check_governance.py: add the performed-act
  registration for this label (the candidate registration stays until
  then)" (`:468-470`). Since `11d01c25`, `check_governance.py` registers
  each dedicated record and the aggregate by existence
  (`DOSSIER_LOCAL_AGENT_ACT_RECORDS`,
  `_activate_dossier_local_agent_manifest_copy_registry`). With all five
  records written it reported 0 FAIL, with no edit. The instruction invites
  a redundant registration edit.
- **The substring check.** The Scope A check is a substring test
  (`SCOPE_A_EXTENSION not in quote`, `record_versioned_signoff.py:293`). A
  quote such as "Not now — do not Extend Scope A" would pass. [Inferred]
  This is harmless in practice, because the lead quotes the selected
  option's label verbatim. An exact match against the packet's option label
  would be tighter.

**Finding 4 — `implementationVersion` stays bound to no reader bytes, and the reader has already changed under it** (note)

Criterion 4. Carried by the brief; recorded so the residue is visible.

[Observed] `git diff --stat 3a84d4a4 f3743f51 -- …/git-object-reader.ts`
shows 1 file changed, with 173 insertions and 51 deletions, between the
reader round 2 read and the head read here. The entry still says
`implementationVersion` "1.0.0" and that "any change to it is a new
implementation version" (line 14).

The entry defines 1.0.0 as the file "as merged", so a pre-merge change
breaks no stated fact [Inferred]. But nothing ties the signed entry to the
merged bytes:

- `apply()` checks only that the file exists;
- the package version stays `0.0.0`.

The same convention holds for the installed Butlers entry. A note; it
strengthens the packet's sign-after-the-gate (and after-merge) alternative
(`OWNER-SITTING-PACKET.md:94-100`).

## Criteria with no finding

- **Criterion 1 holds.**
  - The drawer statement decides only the drawer half. It leaves the tree
    half to Syzygy's check at the pinned revision (`NO-EVIDENCE-DRAWER-STATEMENT.md:32-38`),
    and its corrected basis no longer depends on row 1.
  - The provider statements, the D9 record and the RFC7-20 record are
    byte-unchanged since round 2 (manifest rows identical [Observed]).
    Round 2's criterion-1 analysis of them therefore still applies.
- **Criterion 2 holds** apart from Finding 1. The act types are now verbs
  (RFC3-16(b) item 4). The two contestable readings are named at packet lines
  153-161.
- **Criterion 3 holds.**
  - The recommendation (packet lines 114-130) follows REQ-033's non-governed
    predicate, and a silent input is treated as governed (line 112).
  - The fallback fails closed.
  - Redis-tree claims are labelled [Inferred] (lines 116 and 129).
  - Nothing was read from Redis, by the package or by me.
- **Criterion 4 holds** apart from Findings 2 and 4.
  - The entry declares `networkAccess` `[]`, `writeSurface` `[]`,
    `workingTreeRead` false, `executeObservedCode` false and `fetch` "none".
  - [Observed] The reader imports only `node:crypto`, `node:fs/promises`
    (`lstat`, `open`, `readdir`), `node:path` and `node:zlib`. It has no
    write, spawn or network call.
  - It opens files `O_RDONLY | O_NOFOLLOW | O_NONBLOCK` and re-hashes each
    object (`identifier-mismatch`, reader line 287).
  - It only `lstat`s `objects/info/alternates`, which is consistent with "no
    alternates file … is read".
- **Criterion 5 holds.**
  - The packet offers the extension as the owner's choice (lines 76-79 and
    216).
  - The recorder now refuses a sign-off whose quote does not name it, and
    records the extension.
- **Criterion 6 holds**, per the probes above, apart from Finding 3.
- **Criterion 7 holds.**
  - The packet has 0 64-hex tokens (Python `re`).
  - Each row states what it unlocks and what declining costs.
  - Nothing pending is presented as decided.
  - The new table-order sentence is plain.
- **Criterion 8 holds** for notes 2, 3, 4 (in part), 5 and 6 as listed, with
  one exception. The note 4 repair introduced Finding 2's undeclared-bound
  mismatch, a note-level issue.
