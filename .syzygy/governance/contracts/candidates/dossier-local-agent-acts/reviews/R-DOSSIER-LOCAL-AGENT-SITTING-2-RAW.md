# Review — dossier-local-agent-acts and public-git-source-acquisition-local-agent, round 2
Reviewed commit: c26aaf34ef932db717abbe3c48065e9f2da9e3c4
Manifest SHA-256: 83424ac57dbd82d330ad4dff869f2b5da50df697357f7963746c73a37a490f4f
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context subagent, 2026-10-06. I worked read-only in a fresh
`git clone --no-local` checked out at the commit above. I performed no owner
act and changed no repository file. Probes ran in two further scratch clones,
which I discarded. I read nothing from Redis or from any other external
repository. My only network use was `git fetch` of this repository's own
origin, to read the reader of PR #367:
`origin/agent/dossier-s2-object-reader` at
`3a84d4a4c599197f1972c797a70e05ddd6e3546d`, `packages/polaris-dossier/`
(14 tracked files). The PR is open and not merged [Observed: `gh pr view 367`
gives `state OPEN`, `mergedAt null`].

I recomputed the manifest digest in the clone with
`python3 scripts/build_dossier_local_agent_acts.py --manifest-digest` and with
`sha256sum` over the manifest file. Both print the value above, which is also
the expected value.

## Checks run (final lines, verbatim)

```text
$ python3 scripts/check_governance.py | tail -1
32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted
$ python3 scripts/build_dossier_local_agent_acts.py --selftest | tail -1
selftest: 12 of 12 predicates held
$ python3 scripts/record_dossier_local_agent_acts.py --selftest | tail -1
selftest: 33 of 33 predicates held
$ python3 scripts/build_public_git_source_acquisition_local_agent.py --selftest | tail -1
selftest: 36 of 36 predicates held
$ python3 scripts/record_versioned_signoff.py --selftest | tail -1
83 fixtures, 0 failing
$ python3 scripts/build_dossier_local_agent_acts.py --check
dossier-local-agent-acts: records and manifest current
$ python3 scripts/build_public_git_source_acquisition_local_agent.py --check
public-git-source-acquisition-local-agent: unapplied, verifies
$ python3 scripts/build_dossier_local_agent_acts.py --manifest-digest
83424ac57dbd82d330ad4dff869f2b5da50df697357f7963746c73a37a490f4f
```

All of these exited 0. I also ran
`python3 scripts/record_versioned_signoff.py --check <key> --version 1.0` for
all 8 keys in `real_packages()`:

- The 7 earlier keys (`pwb-missing-currency-disclosure-scenario`,
  `pwb-dismissal-expiry-amendment`, `pwb-container-shape-profile-amendment`,
  `pwb-item-depth-amendment`, `pwb-readability-successor`,
  `pwb-tree-framing-amendment`, `polaris-dossier-local-agent-mode`) each print
  `recorded <key> v1.0 sign-off regenerates exactly; applied tree verified`.
- `public-git-source-acquisition-local-agent` prints
  `public-git-source-acquisition-local-agent v1.0: not performed`.

## Independent mechanics probes (criterion 6) [Observed]

- On the reviewed tree, a live
  `record_dossier_local_agent_acts.py --record d9-in-force <its row> …`
  prints `FAILED (nothing written): no confirming review is recorded:
  FROZEN_SUBJECT is unset, so nothing may be recorded` and exits 1.
  `git status` is clean afterwards.
- I set up a scratch clone as follows: `FROZEN_SUBJECT` set,
  `FROZEN_FILE_DIGESTS` hashed from the live `frozen_rels()`, and a
  synthetic raw whose head carries the manifest FILE digest. In it,
  `validate()` behaves as follows:
  - It accepts each of the five acts with its own row.
  - It refuses the registry-entry row offered as the argument of each of the
    five acts ("is not the <key> manifest row").
  - It refuses the OpenAI row offered as the D9 argument.
  - It refuses a head that carries the D9 row instead of the file digest
    ("does not bind the manifest file's SHA-256").
  - It refuses a `REVISE` head.
  - After a one-byte append to `security.md`, to `v1.md`, to the RULINGS
    direction or to the proposed entry, it refuses all five acts ("builder
    reports stale records or manifest").
- In a scratch clone with the PR #367 reader file present, I committed a
  synthetic CONFIRM raw bound to the manifest FILE digest. Then
  `record_versioned_signoff.py --record public-git-source-acquisition-local-agent
  --version 1.0 --instant 2026-10-06T10:00:00Z …` wrote a record with these
  lines:
  - `Recorded at (UTC): 2026-10-06T10:00:00Z`
  - ``Act type: `adopt-registry-entry` ``
  - `Installed entry SHA-256: d1736a69c0e36f53f3614c30d5be37a3b31f2de449bee37f6aba87575f4aa143`

  That digest equals the entry's manifest row. Its `--check`, the builder's
  `--check` ("applied, verifies") and the
  `polaris-dossier-local-agent-mode` `--check` all passed afterwards.
- `check_governance._act_subjects()` returns 50 labels, 50 of them distinct.
  All five `DOSSIER_LOCAL_AGENT_ACTS` labels are present. No new label is a
  prefix of any other label, nor any other label of a new one. The one prefix
  pair in the registry is older and unrelated: `CONSENT TO PUBLIC TARGET
  EGRESS TO ANTHROPIC` / `… VERSION 2`.

## Round-1 repairs checked

- Finding 1 holds. `installed_lines` (`scripts/record_versioned_signoff.py`,
  lines 434-455) now renders RFC3-16(b) items 3, 4, 6, 7, 8 and 9, and
  `--check` reads the instant back. My end-to-end probe confirms both.
- Finding 2 holds:
  - `implementationStatus` reads "partly implemented".
  - `implementationCoverage` splits the reader's declarations from the
    gate's.
  - The builder requires all 8 `AWAITING_GATE` names.
  - The packet's "What is built and what is not" (`OWNER-SITTING-PACKET.md`,
    lines 89-96) gives the owner the sign-after-the-gate alternative.
- Findings 3–7 hold as dispositioned. Residues are in Findings 1, 5 and 6
  below.

## Findings

**Finding 1 — After an act is recorded, an unrelated edit to a bound file fails every recorded act's check, and the "new version" remedy has no tooling** (note)

Criteria 2 ("the whole-file binding … is stated with its cost") and 6.

The packet says (`OWNER-SITTING-PACKET.md`, lines 177-183): "until a new
version of the record is generated and you sign it … After an act is
recorded, an edit affects only the record it touches." The D9 record's Cost
section (`D9-IN-FORCE-RECORD.md`, lines 61-64) and the RFC7-20 record's Cost
section (`RFC7-20-READING-IN-FORCE-RECORD.md`, lines 61-63) both say "until a
new version of this record is generated … and acted on".

The tooling behaves otherwise:

- **Every recorded act's check fails, not only D9's.** `do_check` re-runs
  `validate()`, which refuses while `build.stale()` is non-empty
  (`record_dossier_local_agent_acts.py:257`). It also compares every package
  file to `FROZEN_FILE_DIGESTS` (`:264`). Both checks cover the whole package.
  [Observed] In a scratch clone I recorded the drawer act; its `do_check`
  returned 0. I then appended one line to `security.md`. The drawer act's
  `do_check` returned 1 with "builder reports stale records or manifest:
  …/D9-IN-FORCE-RECORD.md: differs from its regeneration", although the
  drawer record binds nothing in `security.md`.
- **The only regeneration tool overwrites act-bound bytes.**
  `build_dossier_local_agent_acts.py --write` writes each record back to its
  fixed path (`:135-137`). After the D9 act, that path is the act's artifact.
  So the only tool that "generates a new version" edits bytes an act has
  bound. RFC3-16 says "Acceptance and adoption do not edit the artifact"
  (`governance-homes-and-owner-acts.md`, around line 141).
- **A second act over the same record cannot be recorded.** The dedicated
  record path is fixed per act key, with no version or date
  (`record_dossier_local_agent_acts.py:123-124`), and `do_record` refuses
  "dedicated act already exists" (`:435`).

[Inferred] The authority claim (a gate honours each act by its own record's
digest) probably still holds, so this is fail-closed and not unsafe. What is
missing is the cost the owner would actually pay:

- after any doctrine or direction edit, all five recorded acts' checks go red;
- re-establishing D9 or the reading needs a successor package (a new record
  path and recorder), not a regeneration.

Say so in the cost paragraph, or scope `do_check` to the act's own record and
version the record path.

**Finding 2 — Three of the five act types are record-class nouns, not act types** (note)

Criterion 2 (RFC3-16(b) item 4: "the **act type** (adopt, accept, approve,
consent, dismiss, revoke, …) from the acting surface's own vocabulary").

`ACTS` gives `project-input-statement` (`record_dossier_local_agent_acts.py:129`)
and `in-force-record` (`:160`, `:169`) as the `Act type` that the dedicated
record renders. Each names the class of the record acted on, not what the
owner did to it. This is the same objection round 1 raised against
`Kind: registry entry` for the tag record (round-1 raw, Finding 1); there the
repair chose `adopt-registry-entry`. `consent-agent-provider` is a verb form
and fits.

A form like `state-project-input` / `bind-in-force` (or `approve`) would keep
the vocabulary consistent. The surface's own vocabulary is the drafter's to
set, so this is a note.

**Finding 3 — The tag sign-off does not capture the Scope A extension, and its aggregate block says it widens no read** (note)

Criteria 5 and 7.

The packet correctly offers the extension as the owner's choice
(`OWNER-SITTING-PACKET.md`, lines 73-79 and 211-212). That part holds. The
recorder side does not carry it:

- **Any quote is accepted.** `validate_inputs` checks only that the quote is
  one non-empty line with no digest (`record_versioned_signoff.py`, lines
  277-287). A quote of "Sign it" is accepted for this package.
- **The record asserts Scope A cover regardless.** The record renders
  `DIRECTION_NOTE` ("Signed under `…SCOPE-A-2026-10-02.md`: the owner's
  selection … is the sign-off", lines 424-427) whatever the owner selected.
  So a record could assert Scope A cover for an entry the direction does not
  name ("the PWB specification deltas, the observer registry entry and the
  contract successors queued behind them", Scope A item 1) with no recorded
  extension. The extension is itself a plain owner direction, and no record
  is planned for it.
- **The aggregate block contradicts the dedicated record.**
  `render_aggregate` ends "This sign-off authorizes no implementation, widens
  no consent, read, write or egress" (line 538). For this package the
  dedicated record says the entry "is one of the separate acts a read needs"
  (`does_not`, lines 461-466). The packet says signing "lets Syzygy use its
  in-process reader as the one registered way to read the clone" (line 31).

Suggested repairs:

- require, for a package that installs an entry, that the quote names the
  extension, or render a line stating it;
- tailor the aggregate sentence as `does_not` is tailored.

**Finding 4 — Residual mismatches between the entry and the reader of PR #367** (note)

Criterion 4 ("The registry entry matches what the reader does").

[Observed] Against `git-object-reader.ts` at `3a84d4a4`, the entry's read
rules match the reader:

- object store only;
- algorithm from the identifier's length (lines 46-50);
- re-hash on every call (lines 84-87 and 206-212);
- gitlink refuses as `not-a-blob` (line 130);
- non-commit pin refuses as `type-mismatch` (line 210);
- an over-size object refuses as `corrupt-object` (lines 228, 245 and 347),
  with a default of 2^30 = `maxObjectBytes` 1073741824;
- no write call and no child process.

Four residues remain:

- **`failureStates.objectRefused` is listed as the reader's.** It sits under
  `implementationCoverage.reader` (entry line 26). But the reader only throws
  `GitObjectReadRefusal`. The mapping to `Observer failed` /
  `source-uncaptured-or-unreachable` is the caller's, and the entry's own
  coverage status says so: "the fact records, limits, screening and
  failure-state mapping are the dossier gate's" (line 46).
- **"no … index … is read" is ambiguous.** `readAuthority` says this
  (line 139), and the builder requires the word (`NOT_HONOURED`). The reader
  does read every `objects/pack/*.idx` pack index (reader lines 192-194 and
  311-322). The Git staging index is clearly what is meant; "the staging
  index (`.git/index`)" would remove the ambiguity.
- **Two limits can only filter after the reader has done the work.**
  `maxTreeEntries` says "lists no more" (line 164). `maxBytesPerSource` says
  "the exact blob size before classification" (line 161). With this reader
  API the gate can only enforce them after the reader has done the work:
  - `listTree()` returns every entry with no cap (reader lines 96 and
    136-144);
  - `readBlobs()` inflates whole blobs up to 1 GiB before any size is known
    (lines 91-95).

  [Inferred] Bounding the work, not only the output, needs a reader change,
  which by the entry's own rule is a new implementation version and so a new
  entry version. That strengthens the packet's sign-after-the-gate
  alternative.
- **`implementationVersion` "1.0.0" is bound to no bytes.** The entry says it
  "names that file as merged, and any change to it is a new implementation
  version" (line 14). But:
  - the package declares `"version": "0.0.0"`;
  - the entry carries no commit or digest of the reader;
  - `apply()` checks only that the file exists
    (`build_public_git_source_acquisition_local_agent.py:243`).

  So a reader edit between signing and install, or after it, changes no
  version. The installed Butlers entry has the same convention (`1.0.0`, a
  path), so this is inherited.

**Finding 5 — The semantic delta's stated count does not re-derive, and three value changes are not described** (note)

Criterion 4 ("every changed field is in `SEMANTIC-DELTA.md`").

The delta says "44 keys are changed, added or removed"
(`SEMANTIC-DELTA.md`, line 23) but does not say how lists are walked. I
re-derived the count by script over the parked and proposed files:

- Recursing into `entries[0]` with lists compared whole gives **45**. Every
  last segment is on the page.
- Recursing into equal-length lists element by element gives **46**. One of
  them, `outputFactClasses.0.identityScheme`, has a last segment that is not
  on the page.

Neither walk gives 44. Value changes that no row describes:

- `outputFactClasses[0].identityScheme`:
  `repository-id-plus-commit-object-id-plus-capture-instant` became
  `repository-id-plus-pinned-commit-object-id-plus-step-instant`. Row 38
  names only the class rename.
- `resourceLimits.status` gained "by this reader". Row 41 names only
  `maxFetchBytesPerCommit` → `maxObjectBytes`.
- `screening` changed in three ways:
  - it now adds the classification policy;
  - "before ingest" became "before its content is used in a check or
    rendered";
  - it now cites REQ-polaris-generation-025.

  Row 42 says "the same, and the agent's own reads …", which understates the
  change. Rows 44-46 cover the classification policy elsewhere.

The predicate "the last segment … appears literally on this page" is weak:
`status` and `note` are satisfied by unrelated words (line 52, "the top-level
`status` key"). State the walk and the list rule beside the figure.

**Finding 6 — The drawer statement's basis, and the packet's recommendation, call Redis "admitted for observation" while that consent is unperformed** (note)

Criteria 1 and 3.

The packet and the drawer statement call Redis observed or admitted:

- `NO-EVIDENCE-DRAWER-STATEMENT.md`, line 23 (from `params.json`, line 5):
  "it is a public repository admitted for observation only (the observation
  consent `PUBLIC-OBS-REDIS-2026-10-03`)".
- The packet, lines 116-117: "Syzygy has never onboarded Redis; it only
  observes it".

[Observed] Neither `redis-observation` nor `PUBLIC-OBS-REDIS` appears in
`ACCEPTANCE-ACT-RECORD.md` (0 hits). The packet itself says none of the five
inputs has an act (lines 20-23). Rows are independent ("declining one never
undoes another", line 39). So if the owner signs row 3 and declines row 1, the
signed record states as its basis a consent that is not in force.

The statement's operative sentence (no drawer exists) stays true, which is
why this is a note. "Offered for observation" or "observed only if the
observation consent is in force" would be exact.

## Criteria with no finding

- **Criterion 1 holds** apart from Finding 6:
  - The drawer statement decides only the drawer half and leaves the tree half
    to Syzygy's check at the pinned revision (lines 32-38).
  - Each provider statement calls itself SEC-2's "explicit, recorded,
    per-project consent", "not an egress record", and says the classes "do
    not limit what the agent reads or sends" (lines 39-58).
  - Both provider statements differ only in tool, provider and identity
    lines [Observed, `diff`].
  - The D9 record "does not adopt it again and changes no doctrine byte"
    (lines 38-39).
  - The RFC7-20 record is scoped to "item 1 … and only item 1" and excludes
    item 2 (lines 18 and 53-54).
  - The bound digests equal the live `sha256sum` of `security.md`, `v1.md` and
    the direction [Observed]. Neither file changed after the D9 adoption
    commit `cf2a894b` or the direction commit `a0b13dc1`.
- **Criterion 2 holds** apart from Findings 1 and 2:
  - The dossier acts' records carry RFC3-16(b) items 1–9
    (`render_act`, lines 296-322).
  - The two contestable readings are named (packet, lines 151-159).
  - The whole-file cost is stated (lines 175-186), subject to Finding 1.
- **Criterion 3 holds:**
  - The recommendation follows the REQ-033 scenario "Non-governed subject
    needs no statement" ("the admitted project input states that no kernel
    evidence drawer exists and the pinned tree holds no `openspec/**` path
    and no `.syzygy/` path").
  - A silent input is treated as governed (packet, lines 110-112; spec,
    line 97).
  - The fail-closed fallback matches the governed-subject scenario.
  - Every Redis-tree claim is labelled [Inferred] (lines 116 and 127-128).
- **Criterion 4 holds** apart from Findings 4 and 5:
  - The entry declares `networkAccess` `[]`, `writeSurface` `[]`,
    `workingTreeRead` and `executeObservedCode` false, and `fetch` "none".
  - It names every clone file the reader ignores.
  - It carries no provider-mode behaviour that I could find. The removed
    `fetchFailed`, `revisionMissingAtUpstream`, `maxFetchBytesPerCommit` and
    `runDirectoryWrites` are all gone.
- **Criterion 5 holds:** the packet never treats the entry as already
  covered (lines 76-79). On the recorder side, see Finding 3.
- **Criterion 6 holds**, as the probes above show, apart from Finding 1's
  post-act behaviour.
- **Criterion 7 holds:**
  - No 64-hex token appears in the packet (the builder check confirms it).
  - Each row states what it unlocks and what declining costs.
  - Past acts (the v1.0 sign-off, D9) are stated as past and verified
    [Observed: the `--check` above; `DOCTRINE-AMENDMENT-LOG.md` row D9].
  - Nothing pending is presented as decided.
