# Semantic delta — public Git source acquisition, local-agent version

> **Candidate — binds nothing.** One proposed adapter-registry entry,
> `proposed/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-CANDIDATE.json`,
> for the operator-agent mode of REQ-polaris-generation-033. It binds only if
> the owner extends Scope A to it and signs it off by version tag
> (`public-git-source-acquisition-local-agent-v1.0`). The owner packet is
> `../dossier-local-agent-acts/OWNER-SITTING-PACKET.md`, row 2.

## Predecessor and relation

The predecessor is version 1.0.0-candidate.1 of the same observer,
`../public-admission-registry-entries/proposed/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-CANDIDATE.json`,
parked with the provider mode and never acted on. This version neither edits
nor retires it; it is a second version for the other mode. The two may not
both be installed: the builder refuses this version's install while the
parked version sits in the installed home, so one authority never has two
adapters (REQ-polaris-generation-017).

## What changes, field by field

The key-level difference was computed by script over the two entries (a
recursive walk of both JSON objects): 44 keys are changed, added or removed,
and the last segment of every one of them appears literally on this page.

| Field | Parked version | This version | Why |
|---|---|---|---|
| `observerVersion`, `registryVersion` | 1.0.0-candidate.1 | 2.0.0-candidate.1 | a new version of the same observer |
| `implementationId`, `implementation`, `implementationVersion` | a generation-core module, unimplemented (null) | `polaris-dossier/git-object-reader`, the reader file of `syzygy-qkea.3`, 1.0.0 | the entry names a reader that exists once PR #367 merges |
| `implementationStatus`, `implementationCoverage` (added) | to be implemented | partly implemented: `implementationCoverage.reader` lists what the reader file does, `awaitingGate` what the unwritten dossier gate must do (the four source limits, screening, the fact records, the failure-state mapping, `failureStates.objectRefused` included); install refuses without the reader file; operator-agent mode only | round 1 Finding 2: the reader does not enforce the source limits or produce fact records; round 2 note 4: the reader throws a typed refusal and the mapping to `objectRefused` is the gate's |
| `typedAuthority.authorityType` | hosting and version control | version control | Syzygy reaches no hosting service |
| `typedAuthority.fetch` | one shallow fetch per consented commit | none; the operator prepares the clone, fetching the consented commit alone to stay within the consent's stated form | REQ-033: Syzygy reads the operator's clone |
| `typedAuthority.networkAccess` | the upstream host, for the fetch | none | no fetch |
| `typedAuthority.runDirectoryWrites` → `stateDirectoryWrites` | a local repository in the run directory | Syzygy's own state directory only, never a location derived from the clone's path | REQ-033's write rule |
| `typedAuthority.readAuthority` | object reads of the fetched commit | object reads at the pinned commit from the clone's loose objects and v2 packs; no ref, staging index (`.git/index`; the pack indexes under `objects/pack/` are read), working tree, configuration, hook, alternates, grafts, shallow file, replace ref or commit-graph; no process; algorithm from the identifier's length; every object on the path re-hashed at every step | REQ-033's read rule, as S2 implements it; round 2 note 4: "index" alone read as the pack index too |
| `typedAuthority.submodules`, `tags` | not fetched | a gitlink refuses as not-a-blob; a non-commit pinned identifier refuses | the reader's behaviour |
| `inputClasses` (`git-object-database`) | run-directory clone path | operator-declared clone `.git` directory | |
| `outputFactClasses` | acquisition capture record | pinned-object read record | no capture step exists |
| `determinismClass`, `determinismByOutputClass`, `determinismClassNote`, `determinism` | capture; `acquisition-capture-record` keyed | derivation-deterministic, the read record alone capture (it carries the step's instant); `pinned-object-read-record` keyed in its place | content-addressed reads |
| `failureStates` | `fetchFailed`, `revisionMissingAtUpstream`, `someSourcesUncapturedOrOverLimit` (all removed) | `objectRefused` (mismatch, missing, undecodable, wrong type, ambiguous tree entry, a link or special file under `objects/`, an unreadable store, an exceeded per-call bound: the refusals of the reader as repaired on PR #367) and `someSourcesOverLimit` (added); `revisionNotAdmitted.executionFact` now "refused before any object is read" (was "before any fetch"), its `note` reworded to match | no fetch can fail; a refused object refuses its step |
| `resourceLimits`, `resourceLimitSemantics` | `maxFetchBytesPerCommit` | `maxObjectBytes` (the reader's default, 1 GiB; a larger object refuses as corrupt-object) | values remain [Inferred] proposals |
| `screening` | screened before ingest | the same, and the agent's own reads are the operator's act, not this entry's | REQ-033 |
| `provenanceDisclosure` | owner-trusted records | the same, plus: the clone and every gate record lie within the agent sessions' write reach; only re-hashed bytes are used | R3-F8 |
| `authorizationModeDerivation` | entry, consent and screening scope in force | entry, the consent naming the pinned revision, and both the classification policy and the screening scope acts in force | REQ-033 lists the classification policy act among the run's gates |
| `inputClasses` (`classification-policy`, added), `snapshotInputMapping` | no classification policy input | the classification policy act is an input, mapped to RFC2-1 items 7 and 11 | as above |
| `admissionFailureMapping` | consent, screening scope, registry entry | the same, plus `missingClassificationPolicy` (`missing-declaration`) and `mismatchedStaleRevokedOrUnattributedClassificationPolicy` (`source-uncaptured-or-unreachable`), mirroring the screening scope | as above |
| `subject.observedRepositories` | each consented pair | each consented pair, at a revision its consent names | REQ-033 pins to a consented revision |
| `governingBehaviorContract` | base 017 and 025 with the amendments; `signedBy` "pending exact owner act over this entry" | the same plus 033 to 036 of the v1.0 sign-off; `signedBy` "pending the owner's version-tagged sign-off of this package" | |
| `supersession` | exact owner act | version tag under Scope A, if extended; does not supersede the parked version | |
| `snapshotInputMapping.outputs` | capture record | read record | |

Unchanged: `schemaVersion`, the top-level `status` key (its governance lifecycle word), `contractId`, `contractVersion` (the
installed Butlers entry's value, checked by the builder), `authorizationModes`,
the other input classes and their mapping,
`writeSurface`, `databaseAccess`, `executeObservedCode` and `workingTreeRead`
(still empty and false), `adoptionStatus`.

## Known gaps

- [Inferred] The dossier gate that would read this entry's sign-off, and that
  performs the declarations under `implementationCoverage.awaitingGate`, does
  not exist yet. The sign-off record (`record_versioned_signoff.py`, the
  `registry entry` package) names the installed entry with the SHA-256 of its
  bytes and carries the rest of RFC3-16(b)'s binding set (act type, instant,
  scope, supersession, state-(1) provenance, A1 explicitly absent), which
  RFC4-7 requires of a registry entry; the gate must still be written to read
  it.
- [Observed] Scope A names "the observer registry entry" of the PWB work and
  no public-source entry has been signed by tag; the owner's extension is
  part of the sign-off question.
- The resource limits are proposals; no Redis body has been read by this
  reader.
