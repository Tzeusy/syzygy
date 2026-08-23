# Capability 1 Runtime-Hardening Follow-ups Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Capability 1 evaluations snapshot-bound, fail closed on
uncorrelated consent, preserve exact consent and withdrawal provenance, harden
transport and parity checks, and serve evidence-backed discoverability through
one human/machine projection.

**Architecture:** The daemon first captures an immutable
`CapturedProjectInputs` value, derives the source-snapshot digest from canonical
bytes, and evaluates only that value. A verified consent record—not a bare
tree artifact—must authorize repository reads. Coverage and discoverability
then become required typed planes on `ProjectEvaluation`, and both HTTP channels
serialize those planes while independent wire oracles compare canonical
multisets.

**Tech Stack:** TypeScript, Node.js >=22.15, npm workspaces, Vitest 3,
`yaml@2.9.0`, exact runtime pins `marked@18.0.10` and `parse5@8.0.1`, SHA-256
from `node:crypto`, server-rendered HTML, JSON over the existing local daemon.
The dependency admission uses the current primary package records for
[`marked@18.0.10`](https://www.npmjs.com/package/marked?activeTab=versions) and
[`parse5@8.0.1`](https://www.npmjs.com/package/parse5?activeTab=versions): the
first supplies Markdown/GFM rendering with zero runtime dependencies, and the
second supplies a typed HTML parser with one runtime dependency. Their output
is never served; it exists only as an intermediate tree for hyperlink
classification.

## Global Constraints

- Behavioral authority is the adopted change at
  `openspec/changes/project-registration-and-honest-shape-visibility/`; its
  seven adopted artifacts are immutable.
- Implementation authority is
  `.syzygy/governance/decisions/CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md`.
- Implementation files stay in `apps/**`, `packages/**`, root tooling/config,
  and `docs/**`; never edit `openspec/**` or `.syzygy/**` in an implementation
  task.
- Node remains >=22.15 and hosted CI remains Node 24.
- Missing, inaccessible, stale, unverified, or unclassifiable inputs fail
  closed to named unavailable/`Unknown` states; never success, zero, or silent
  omission.
- No persistence, retry store, last-good history, retention policy, full
  authority-exposure source, proposal production, production deployment, or
  external-project onboarding is introduced.
- Every child records exact requirement limbs, risk classes, net test delta,
  controlled mutation evidence, exact-head gate artifacts, and a FROZEN-byte
  declaration before merge.
- Mandatory fresh-context exact-head review applies to security,
  deterministic-observation, identity, public-interface, write-containment,
  dependency-admission, and build/runtime-interface changes.

---

## Authorization and Execution Frontier

[Observed] RFC3-16(a) requires consent acts to correlate to an owner-attended
ceremony in an independently kept RFC5-25 trail. No such runtime source exists
in this repository. A Git commit, tree-resident record, fixture, or
caller-supplied `verified: true` cannot satisfy that gate.

Before Task 1 can run, the owner must select one of these outcomes:

1. **Authorize a local external audit trail and ceremony slice
   (recommended).** The trail is read-only to this daemon, outside the observed
   tree and untrusted worker write reach, and binds RFC3-16(b)'s nine fields.
   This requires a separate owner act if the selected storage, retention, or
   record encoding changes the current security/retention/normative-data
   posture.
2. **Identify an existing conforming RFC5-25 provider.** Supply its stable
   read/correlation interface and evidence that governed-tree workers cannot
   write it.
3. **Keep the status quo.** Tasks 1, 5, and 6 remain held; only Tasks 2–4 are
   runnable.

If unanswered, option 3 applies. The planning graph records this as one human
gate. It does not auto-enact an audit mechanism.

## File and Ownership Map

| Task | Primary owned surface | Serializes with |
|---|---|---|
| 1 | snapshot/capture pipeline, consent provenance and pre-observation authorization, entry capture | Depends on Task 4 and the owner gate; Tasks 5 and 6 consume it |
| 2 | credential transport tests, CLI realpath containment, state-dir system tests | Runs before Task 4 because both modify `main.ts` |
| 3 | `parity.ts` and requirement-keyed parity tests | Tasks 5 and 6 consume its canonical multiset helper |
| 4 | root Vitest config, package export maps, package lock, `main.ts` runtime import seam | Depends on Task 2; Task 1 and Task 6 follow it |
| 5 | coverage projection and both route coverage rows from Task 1 decisions | Depends on Tasks 1 and 3; serializes with Task 6 |
| 6 | README hyperlink adapter, discoverability model, required evaluated planes, both routes/system oracle | Tasks 1, 3, 4, and 5 |

The boundaries deliberately follow representation and dependency seams rather
than files or requirement numbers. Task 1 owns immutable input representation,
exact-reference authorization, and capture propagation because authorization
must precede repository I/O. Task 5 consumes that closed decision and owns only
coverage projection/serving. Task 6 owns the discoverability vertical outcome.

## Requirement, Risk, and Review Map

| Task | CAP1 requirement limbs | Risk classes | Required review |
|---|---|---|---|
| 1 | 011 consent provenance, 016 no unauthorized observation, 042 evaluation identity, 060 stable identity, 062 same-evaluation temporal behavior | security, deterministic observation, identity, public entry | Fresh-context exact-head security/determinism/identity/interface review |
| 2 | 015 credential-classed retrieval; 061 no unauthorized write/effect | authentication, write containment | Fresh-context exact-head security/write-boundary review |
| 3 | 041 same facts, 043 parity disagreements fail, 045 epistemic distinctions survive | deterministic parity, public interface | Fresh-context exact-head determinism/interface review |
| 4 | No behavioral completion claim; authorized developer tooling supporting all CAP1 verification | dependency admission, build/runtime interface | Fresh-context exact-head dependency/build review |
| 5 | 010–016 executable coverage and consent-rendering limbs; stale/observer-history limbs explicitly excluded | consent security, coverage, public interface | Fresh-context exact-head security/determinism/interface review |
| 6 | 040 explanations, 041 parity, 050–053 discoverability, 064 non-visual recovery | deterministic observation, untrusted parsing, public interface | Fresh-context exact-head dependency/security/determinism/interface review |

---

### Task 1: Bind Evaluations to Authorized Captured Snapshots

**Runnable:** No—blocked on Task 4 and the audit-correlation owner gate above.

**Files:**

- Create: `packages/cap1-core/src/snapshot.ts`
- Create: `packages/cap1-daemon/src/source-snapshot.ts`
- Create: `packages/cap1-daemon/src/source-snapshot.test.ts`
- Modify: `packages/cap1-core/src/consent.ts`
- Modify: `packages/cap1-core/src/index.ts`
- Modify: `packages/cap1-daemon/src/consent-loading.ts`
- Modify: `packages/cap1-daemon/src/observation.ts`
- Modify: `packages/cap1-daemon/src/pipeline.ts`
- Modify: `packages/cap1-daemon/src/routes-machine.ts`
- Modify: `packages/cap1-daemon/src/routes-human.ts`
- Modify: `packages/cap1-daemon/src/index.ts`
- Modify: `apps/syzygy/src/main.ts`
- Test: `packages/cap1-daemon/src/pipeline.test.ts`
- Test: `packages/cap1-daemon/src/routes-machine.test.ts`
- Test: `packages/cap1-daemon/src/routes-human.test.ts`
- Test: `packages/cap1-conformance/src/req-011.conformance.test.ts`
- Test: `packages/cap1-conformance/src/req-016.conformance.test.ts`
- Test: `packages/cap1-conformance/src/req-042.conformance.test.ts`
- Test: `packages/cap1-conformance/src/req-060.conformance.test.ts`
- Test: `packages/cap1-conformance/src/req-062.conformance.test.ts`
- Test: `packages/cap1-system/src/degradation.system.test.ts`
- Test: `packages/cap1-system/src/full-facts.system.test.ts`
- Test: `packages/cap1-system/src/harness.ts`

**Interfaces:**

- Consumes: `DeclarationObservation`, `ConsentReferenceLoad`,
  `ConsentRecord`, `RepositoryEntry`, `ObservationOutcome`, one injected
  `ConsentProvenanceVerifier`, and the composition root's explicit `asOf`.
- Produces: protocol-neutral snapshot/consent types in core;
  `CapturedProjectInputs`; canonical source-snapshot bytes and digest;
  `evaluateCapturedProject(captured, asOf)`; captured entry content; and one
  closed `PreObservationConsentDecision` per declaration entry consumed by
  Task 5.

```ts
export type Sha256Digest = `sha256:${string}`;
export type SnapshotSchema = 'cap1-source-snapshot/v1';

export const CONSENT_REFERENCE_FAILURE_KINDS = [
  'reference-unresolvable',
  'record-unreadable',
  'record-malformed',
  'record-identity-mismatch',
] as const;
export type ConsentReferenceFailureKind =
  (typeof CONSENT_REFERENCE_FAILURE_KINDS)[number];

export interface OwnerActBinding {
  readonly projectId: ProjectId;
  readonly artifactId: string;
  readonly artifactDigest: Sha256Digest;
  readonly actType: 'consent' | 'revoke';
  readonly ownerAttribution: string;
  readonly actInstant: string;
  readonly scope: string;
  readonly supersedes: string | undefined;
  readonly auditRecordId: string;
  readonly auditRecordDigest: Sha256Digest;
}

export type ConsentActVerification =
  | {
      readonly state: 'verified';
      readonly correlationId: string;
      readonly correlationDigest: Sha256Digest;
      readonly binding: OwnerActBinding;
    }
  | {
      readonly state: 'unverified';
      readonly reason:
        | 'audit-source-unavailable'
        | 'correlation-not-found'
        | 'artifact-digest-mismatch'
        | 'binding-mismatch';
    };

export interface ConsentProvenanceVerifier {
  verifyConsentAct(input: {
    readonly reference: string;
    readonly projectId: ProjectId;
    readonly artifactDigest: Sha256Digest;
    readonly record: ConsentRecord;
  }): Promise<ConsentActVerification>;
}

export interface UntrustedConsentRecordView {
  readonly recordId: string;
  readonly artifactDigest: Sha256Digest;
  readonly projectId: ProjectId;
  readonly repositoryId: RepositoryId;
  readonly scope: string;
  readonly attribution: string;
  readonly grantState: GrantState;
  readonly effectiveProvenance: 'Unknown';
  readonly contradiction: {
    readonly kind: 'owner-act-provenance-unverified';
    readonly route: 'owner-adjudication';
  };
}

export interface VerifiedConsentRecord {
  readonly reference: string;
  readonly artifactDigest: Sha256Digest;
  readonly record: ConsentRecord;
  readonly ownerAct: Extract<ConsentActVerification, { state: 'verified' }>;
}

export type ReferenceFailureBasis =
  | {
      readonly kind: 'reference-load-failure';
      readonly reference: string;
      readonly failure: ConsentReferenceFailureKind;
    }
  | {
      readonly kind: 'record-subject-mismatch';
      readonly reference: string;
      readonly actualProjectId: ProjectId;
      readonly actualRepositoryId: RepositoryId;
    }
  | {
      readonly kind: 'owner-act-unverified';
      readonly reference: string;
      readonly reason: Extract<ConsentActVerification, { state: 'unverified' }>['reason'];
    };

export type PreObservationConsentDecision =
  | {
      readonly authorized: true;
      readonly repositoryId: RepositoryId;
      readonly consent: VerifiedConsentRecord;
    }
  | {
      readonly authorized: false;
      readonly repositoryId: RepositoryId;
      readonly declaredReference: string;
      readonly basis: ReferenceFailureBasis | {
        readonly kind: 'withdrawn';
        readonly record: VerifiedConsentRecord;
      };
      readonly retainedUntrustedRecord: UntrustedConsentRecordView | undefined;
    };

export type CapturedText =
  | {
      readonly state: 'captured';
      readonly logicalPath: string;
      readonly text: string;
      readonly digest: Sha256Digest;
    }
  | {
      readonly state: 'missing' | 'unreadable';
      readonly logicalPath: string;
      readonly failureCode: string;
    };

export interface CapturedConsentInput {
  readonly reference: string;
  readonly source: CapturedText;
  readonly load: ConsentReferenceLoad;
  readonly provenance: ConsentActVerification;
  readonly decisionInput: ReferenceBoundConsentInput;
}

export type ReferenceBoundConsentInput =
  | {
      readonly reference: string;
      readonly state: 'loaded';
      readonly artifactDigest: Sha256Digest;
      readonly record: ConsentRecord;
      readonly provenance: ConsentActVerification;
    }
  | {
      readonly reference: string;
      readonly state: 'failed';
      readonly failure: ConsentReferenceFailureKind;
    };

export interface CaptureVersions {
  readonly manifestSchema: SnapshotSchema;
  readonly observer: string;
  readonly consentAdapter: string;
  readonly yamlParser: 'yaml@2.9.0';
  readonly markdownParser: string | 'not-produced';
  readonly kernel: string;
  readonly evaluationEngine: string;
}

export interface RepositoryLinkContext {
  readonly canonicalWebBase: string | undefined;
  readonly defaultBranch: string | undefined;
}

export interface SnapshotInputDescriptor {
  readonly kind: string;
  readonly subjectId: string;
  readonly ordinal: number | undefined;
  readonly logicalPath: string | undefined;
  readonly state: 'captured' | 'missing' | 'unreadable' | 'not-read';
  readonly digest: Sha256Digest | undefined;
  readonly failureCode: string | undefined;
}

export interface SourceSnapshotManifest {
  readonly schema: SnapshotSchema;
  readonly versions: CaptureVersions;
  readonly configuration: {
    readonly digestAlgorithm: 'sha256';
    readonly pathNormalization: 'relative-posix-v1';
  };
  readonly inputs: readonly SnapshotInputDescriptor[];
}

export interface CaptureDependencies {
  readonly repositoryRoots?: Readonly<Record<string, string>>;
  readonly linkContexts?: Readonly<Record<string, RepositoryLinkContext>>;
  readonly versions: CaptureVersions;
  readonly consentProvenance: ConsentProvenanceVerifier;
}

export interface CapturedProjectInputs {
  readonly manifest: SourceSnapshotManifest;
  readonly snapshot: Sha256Digest;
  readonly declaration: CapturedText;
  readonly declarationObservation: DeclarationObservation;
  readonly consents: readonly CapturedConsentInput[];
  readonly consentDecisions: readonly PreObservationConsentDecision[];
  readonly repositories: readonly CapturedRepositoryInput[];
  readonly entry: CapturedText | {
    readonly state: 'not-read';
    readonly reason: 'unconsented-governance-root';
  };
}

export interface CapturedRepositoryInput {
  readonly repositoryId: RepositoryId;
  readonly role: RepositoryRole;
  readonly linkContext: RepositoryLinkContext;
  readonly authorization: PreObservationConsentDecision;
  readonly root:
    | {
        readonly state: 'captured';
        readonly observation: ObservationOutcome;
        readonly inputDigest: Sha256Digest;
      }
    | {
        readonly state: 'not-read';
        readonly reason: 'unverified-consent' | 'unconsented' | 'no-root';
      };
  readonly readme:
    | CapturedText
    | {
        readonly state: 'not-read' | 'not-applicable';
        readonly reason: string;
      };
}

export function canonicalSnapshotBytes(
  manifest: SourceSnapshotManifest,
): Uint8Array;

export function snapshotDigest(
  manifest: SourceSnapshotManifest,
): Sha256Digest;

export async function captureProjectInputs(
  observedRootDir: string,
  deps: CaptureDependencies,
): Promise<CapturedProjectInputs>;

export function evaluateCapturedProject(
  captured: CapturedProjectInputs,
  asOf: string,
): ProjectEvaluation;

export function resolvePreObservationConsent(
  projectId: ProjectId,
  entry: RepositoryEntry,
  inputs: readonly ReferenceBoundConsentInput[],
): PreObservationConsentDecision;
```

Dependency direction is fixed: `Sha256Digest`, manifest descriptors,
`OwnerActBinding`, `ConsentActVerification`, `VerifiedConsentRecord`,
`ReferenceBoundConsentInput`, `ReferenceFailureBasis`,
`PreObservationConsentDecision`, canonical bytes, digest, and the pure resolver
live in `cap1-core/src/snapshot.ts` or `consent.ts`. Filesystem capture types,
`ConsentProvenanceVerifier`, `CapturedText`, `CapturedConsentInput`,
`CapturedRepositoryInput`, and `CapturedProjectInputs` live in
`cap1-daemon/src/source-snapshot.ts`. Core never imports a daemon loader type;
the daemon maps `ConsentReferenceLoad` into `ReferenceBoundConsentInput`.

Canonicalization is UTF-8 JSON without insignificant whitespace, with object
keys sorted lexicographically and input rows sorted by `(kind, stable subject
identity)`. Repository declaration order remains an explicit ordinal. Logical
paths are root-relative POSIX paths and reject absolute values, NUL, and `..`.
Failures carry stable named codes, never host paths or raw OS prose. Digests are
lowercase SHA-256 with the `sha256:` prefix. `asOf` is excluded from the
source manifest.

- [ ] **Step 1: Write the snapshot-forgery regression**

Add a pipeline test proving a caller can no longer inject
`snapshot: 'forged'`; the returned evaluation snapshot must be the digest of
canonical captured input bytes.

```ts
const CAPTURE_DEPS = {
  versions: {
    manifestSchema: 'cap1-source-snapshot/v1',
    observer: 'cap1-observer/v1',
    consentAdapter: 'cap1-consent-loader/v1',
    yamlParser: 'yaml@2.9.0',
    markdownParser: 'not-produced',
    kernel: 'cap1-core/v1',
    evaluationEngine: 'cap1-daemon/v1',
  },
  consentProvenance: {
    verifyConsentAct: async (): Promise<ConsentActVerification> => ({
      state: 'unverified',
      reason: 'audit-source-unavailable',
    }),
  },
} satisfies CaptureDependencies;

const captured = await captureProjectInputs(root, CAPTURE_DEPS);
const result = evaluateCapturedProject(captured, '2026-08-24T00:00:00Z');
expect(result.kind).toBe('project-evaluated');
if (result.kind === 'project-evaluated') {
  expect(result.model.evaluation.snapshot).toBe(captured.snapshot);
  expect(result.model.evaluation.snapshot).toMatch(/^sha256:[0-9a-f]{64}$/);
}
```

- [ ] **Step 2: Run the focused test and observe RED**

Run:

```bash
npx vitest run packages/cap1-daemon/src/pipeline.test.ts
```

Expected: FAIL because `captureProjectInputs` and
`evaluateCapturedProject` do not exist and the current pipeline accepts a
caller-supplied snapshot label.

- [ ] **Step 3: Implement canonical snapshot bytes and digest**

Implement recursive key sorting without a third-party canonical-JSON package:

```ts
function canonicalValue(value: unknown): unknown {
  if (Array.isArray(value)) return value.map(canonicalValue);
  if (value !== null && typeof value === 'object') {
    return Object.fromEntries(
      Object.entries(value as Record<string, unknown>)
        .sort(([a], [b]) => (a < b ? -1 : a > b ? 1 : 0))
        .map(([key, item]) => [key, canonicalValue(item)]),
    );
  }
  return value;
}

export function canonicalSnapshotBytes(manifest: SourceSnapshotManifest): Uint8Array {
  return new TextEncoder().encode(JSON.stringify(canonicalValue(manifest)));
}

export function snapshotDigest(manifest: SourceSnapshotManifest): Sha256Digest {
  const hex = createHash('sha256')
    .update(canonicalSnapshotBytes(manifest))
    .digest('hex');
  return `sha256:${hex}`;
}
```

- [ ] **Step 4: Prove every input class is identity-bearing**

Add table-driven tests that mutate exactly one of declaration bytes, consent
bytes, correlation, repository observation, README, entry, version, or parser
configuration. Each mutation must change canonical bytes and the digest. Same
inputs with a different `asOf` must retain the source digest.

- [ ] **Step 5: Implement fail-closed capture ordering**

The capture order is fixed:

```text
declaration
→ union of entry and top-level consent references
→ consent bytes and digests
→ external audit correlations
→ per-entry authorization
→ authorized repository/README/entry capture
→ input revalidation
→ canonical manifest and digest
→ evaluation
```

Use injected reader functions in tests so an unverified consent result can
assert zero calls to repository, README, and entry readers. Mid-capture change
returns `source-changed-during-capture`; it does not auto-retry.

- [ ] **Step 6: Implement the complete pre-observation consent decision**

Resolve the exact entry reference before any content read. Close precedence as
follows: invalid/unloadable/mismatched/unverified exact reference remains
primary; exact verified withdrawal refuses; exact verified in-force consent is
defeated by any verified same-pair withdrawal. Retain the winning record or
failure identity in `PreObservationConsentDecision`.

For a well-formed but unverified tree record, serve its record ID, scope,
attribution, and grant-state claim explicitly as untrusted content beside
`effectiveProvenance: 'Unknown'`. Include the machine-readable contradiction
`owner-act-provenance-unverified` and route `owner-adjudication`; never erase
the record and never honor it.

- [ ] **Step 7: Prove authorization visibility and no-read behavior**

Extend `req-011`, `req-016`, pipeline, and both route tests. The unverified
record must be visible with identical human/machine fields while repository,
README, and entry reader spies remain at zero calls. Add exact-reference,
wrong-subject, grant/withdrawal order, and invalid-plus-withdrawal cases here;
Task 5 must consume these decisions without re-resolving them.

```bash
npx vitest run \
  packages/cap1-conformance/src/req-011.conformance.test.ts \
  packages/cap1-conformance/src/req-016.conformance.test.ts \
  packages/cap1-daemon/src/pipeline.test.ts \
  packages/cap1-daemon/src/routes-machine.test.ts \
  packages/cap1-daemon/src/routes-human.test.ts
```

- [ ] **Step 8: Remove post-capture and request-time reads**

Change `humanRoutes` so `/entry` renders `evaluation.entry`. Remove
`readEntrySource` from `HumanRouteDependencies` and remove the dynamic
`readFile` closure in `apps/syzygy/src/main.ts`.

- [ ] **Step 9: Run snapshot, pipeline, and entry tests GREEN**

Run:

```bash
npx vitest run \
  packages/cap1-daemon/src/source-snapshot.test.ts \
  packages/cap1-daemon/src/pipeline.test.ts \
  packages/cap1-daemon/src/routes-machine.test.ts \
  packages/cap1-daemon/src/routes-human.test.ts \
  packages/cap1-conformance/src/req-011.conformance.test.ts \
  packages/cap1-conformance/src/req-016.conformance.test.ts \
  packages/cap1-conformance/src/req-042.conformance.test.ts \
  packages/cap1-conformance/src/req-060.conformance.test.ts \
  packages/cap1-conformance/src/req-062.conformance.test.ts
```

Expected: PASS, including same-snapshot repeat evaluation, changed-`asOf`,
mid-capture mutation, post-capture mutation, and unverified-consent no-read
tests.

- [ ] **Step 10: Perform controlled mutations**

Temporarily restore caller-supplied snapshot use, permit a post-capture entry
read, and skip consent verification in three separate mutations. The named
focused test must fail each time. Restore, rerun the focused set, and declare
the files FROZEN.

- [ ] **Step 11: Document implementation-only conventions**

The plan already records `cap1-source-snapshot/v1`, canonicalization, capture
failure codes, and `<decisionsDir>/<reference>.yaml`; do not edit the plan in
this task. Add only load-bearing module comments beside the implementation,
explicitly stating that these are implementation conventions, not new
conformance authority.

- [ ] **Step 12: Run full gates and commit**

```bash
npm run typecheck
npm test
npm run test:system
SYZYGY_FRESH_CLONE=1 npm run test:system
git add packages/cap1-core packages/cap1-daemon packages/cap1-conformance \
  packages/cap1-system apps/syzygy
git commit -m "feat: bind CAP1 evaluation to captured inputs"
```

Expected: all gates PASS; exact counts, skips, denominators, net test delta,
mutations, and commit SHA are retained by CI or the coordinator. Independent
security/determinism/identity/public-entry review must pass before merge.

---

### Task 2: Harden Daemon Admission and State-Directory Containment

**Runnable:** Yes after the planning commit reaches the execution base.

**Files:**

- Modify: `packages/cap1-daemon/src/server.test.ts`
- Modify: `packages/cap1-system/src/credentials.system.test.ts`
- Modify: `apps/syzygy/src/main.ts`
- Modify: `packages/cap1-system/src/state-dir.system.test.ts`

**Interfaces:**

- Consumes: existing `credentialFromAuthorizationHeader`, `verifyCredential`,
  `REFUSAL_BODY`, `governedPlaneViolation`, and the compiled CLI.
- Produces: transport-level regression coverage and link-aware containment for
  an existing or dangling state-dir symlink; no new credential vocabulary or
  public endpoint.

- [ ] **Step 1: Add the real-HTTP credential matrix**

Extend the component table with missing, `Bearer`, `Bearer `, `Basic x`,
`Bearer    `, malformed, wrong-length, wrong-token, and correct-token cases.
For every component refusal assert status 401, content type JSON, exact body
bytes `{"admitted":false,"served":"nothing"}`, and zero handler calls. In the
compiled system test assert status/content type/body and absence of served
facts; only the in-process component spy can prove zero handler calls. Keep the
correct-token request as a separate positive control.

```ts
it.each([
  [undefined, 401],
  ['Bearer', 401],
  ['Bearer ', 401],
  ['Basic x', 401],
  ['Bearer    ', 401],
  [`Bearer ${'f'.repeat(64)}`, 401],
])('refuses malformed credential %s', async (authorization, expectedStatus) => {
  const response = await requestMachineRoute(authorization);
  expect(response.status).toBe(expectedStatus);
  expect(response.body).toBe('{"admitted":false,"served":"nothing"}');
  expect(handlerInvocations()).toBe(0);
});
```

- [ ] **Step 2: Run baseline GREEN, mutate RED, restore GREEN**

```bash
npx vitest run packages/cap1-daemon/src/server.test.ts
npm run build
npx vitest run --config packages/cap1-system/vitest.config.ts \
  src/credentials.system.test.ts
```

Expected initial result: the added test-debt cases pass on current behavior.
Then weaken bearer parsing/admission in one controlled mutation and verify at
least one new case fails for the intended reason; restore and rerun GREEN. No
production credential change is required unless current behavior actually
admits or invokes the handler. Verify `timingSafeEqual` structurally for
syntactically presented tokens; a 401 alone never proves that function ran.

- [ ] **Step 3: Add dangling-symlink governed-plane falsifier**

Create a symlink outside the fixture whose link target is a nonexistent path
under `<fixture>/.syzygy/`. Spawn the compiled CLI and assert exit 1, stderr
contains `inside the governed plane`, stdout contains no listener, and the
governed-tree external snapshot has zero additions/deletions/modifications.

- [ ] **Step 4: Resolve symlink components without requiring target existence**

Use `lstatSync` and `readlinkSync` component-by-component. Resolve an absolute
link target directly and a relative target against the link's parent; append
the unbuilt suffix, normalize, and continue until no existing symlink component
remains. Reject loops with a named invalid diagnostic.

```ts
type PathIntentResolution =
  | {
      readonly resolved: true;
      readonly intendedRealPath: string;
      readonly dangling: boolean;
    }
  | {
      readonly resolved: false;
      readonly reason: 'symlink-loop' | 'path-unreadable';
      readonly detail: string;
    };

function resolvePathIntent(absolutePath: string): PathIntentResolution;
```

Map every failure arm to the CLI's named `invalid` outcome before any write or
listener creation.

- [ ] **Step 5: Pin the benign dangling outcome**

A dangling symlink to a nonexistent path outside the governed plane remains
`credential-unprovisionable`, exits 1, opens no listener, and writes nothing.
It must not be mislabeled as governed-plane refusal.

- [ ] **Step 6: Run state-dir component and system tests**

```bash
npm run build
npx vitest run --config packages/cap1-system/vitest.config.ts \
  src/state-dir.system.test.ts
```

Expected: existing target inside/outside and dangling target inside/outside
cases PASS.

- [ ] **Step 7: Mutate and restore both guards**

Temporarily revert to `existsSync`/nearest-existing-ancestor behavior and prove
the dangling in-plane test fails. Separately weaken bearer parsing and prove a
transport case fails. Restore and rerun focused tests.

- [ ] **Step 8: Run full gates and commit**

```bash
npm run typecheck
npm test
npm run test:system
git add apps/syzygy/src/main.ts packages/cap1-daemon/src/server.test.ts \
  packages/cap1-system/src/credentials.system.test.ts \
  packages/cap1-system/src/state-dir.system.test.ts
git commit -m "test: harden daemon security boundaries"
```

Independent security/write-containment exact-head review is mandatory.

---

### Task 3: Make the Parity Oracle Multiset-Safe

**Runnable:** Yes after the planning commit reaches the execution base.

**Files:**

- Modify: `packages/cap1-core/src/parity.ts`
- Modify: `packages/cap1-conformance/src/req-041.conformance.test.ts`
- Modify: `packages/cap1-conformance/src/req-043.conformance.test.ts`
- Modify: `packages/cap1-conformance/src/req-045.conformance.test.ts`

**Interfaces:**

- Consumes: `ChannelDisclosure`, `ServedFact`, `deterministicLayer`.
- Produces: reusable `canonicalTupleMultiset` and order-insensitive complete
  fact comparison consumed by Tasks 5 and 6. Existing `compareRenderings` and
  `ParityComparison` remain source-compatible.

```ts
export function canonicalTupleMultiset<T>(
  values: readonly T[],
  canonicalize: (value: T) => string,
): ReadonlyMap<string, number> {
  const counts = new Map<string, number>();
  for (const value of values) {
    const key = canonicalize(value);
    counts.set(key, (counts.get(key) ?? 0) + 1);
  }
  return counts;
}
```

- [ ] **Step 1: Add the equal-count Map-collapse falsifier**

Create two disclosures with duplicate fact names and equal total counts. Make
the final value for the duplicated name equal in both disclosures, but change
the earlier occurrence in only one channel. The current name-keyed maps must
incorrectly return parity.

- [ ] **Step 2: Add lawful permutation and multiplicity tests**

Pin three independent behaviors: same complete tuples in a different order
pass; one changed duplicate occurrence fails; one added identical duplicate
fails on multiplicity.

- [ ] **Step 3: Run parity tests and observe RED**

```bash
npx vitest run \
  packages/cap1-conformance/src/req-041.conformance.test.ts \
  packages/cap1-conformance/src/req-043.conformance.test.ts \
  packages/cap1-conformance/src/req-045.conformance.test.ts
```

- [ ] **Step 4: Replace name-keyed comparison**

Canonicalize every semantic fact field—name, value, epistemic label, primary
and secondary reasons, freshness, tier, and basis—while excluding only channel
formatting and presentation order. Compare tuple occurrence counts in both
directions. Do not use fact name as a uniqueness key.

Multiset equality alone decides the verdict. Preserve the current per-facet
diagnostics for unique-name differences. For duplicate mismatches, emit a
deterministic occurrence-count disagreement containing the canonical fact name,
tuple digest, and counts in each channel; never silently pick one occurrence.

- [ ] **Step 5: Run focused tests GREEN and perform mutations**

Reintroduce the old name-keyed map and prove the equal-count falsifier fails;
replace multiset comparison with positional comparison and prove the
permutation test fails. Restore and rerun.

- [ ] **Step 6: Run full gates and commit**

```bash
npm run typecheck
npm test
npm run test:system
git add packages/cap1-core/src/parity.ts \
  packages/cap1-conformance/src/req-041.conformance.test.ts \
  packages/cap1-conformance/src/req-043.conformance.test.ts \
  packages/cap1-conformance/src/req-045.conformance.test.ts
git commit -m "fix: preserve duplicate facts in parity checks"
```

Independent deterministic/public-interface review is mandatory.

---

### Task 4: Modernize Vitest and Workspace Runtime Resolution

**Runnable:** Yes after Task 2 reaches `main`; this serializes their shared
`apps/syzygy/src/main.ts` ownership.

**Files:**

- Delete: `vitest.workspace.ts`
- Create: `vitest.config.ts`
- Modify: `package.json`
- Modify: `package-lock.json`
- Modify: `packages/cap1-core/package.json`
- Modify: `packages/cap1-daemon/package.json`
- Modify: `apps/syzygy/package.json`
- Modify: `apps/syzygy/tsconfig.json`
- Modify: `apps/syzygy/src/main.ts`
- Modify: `packages/cap1-system/vitest.config.ts`
- Modify: `docs/CAPABILITY-1-IMPLEMENTATION-PLAN.md`
- Test: `packages/cap1-system/src/fresh-clone.system.test.ts`
- Test: `packages/cap1-daemon/src/package.test.ts`

**Interfaces:**

- Consumes: current npm workspace names and TypeScript project references.
- Produces: root `test.projects`, source aliases for no-prebuild tests,
  conditional package exports for built Node execution, and no
  composition-root `registerHooks` shim.

Use this configuration shape:

```ts
import { fileURLToPath } from 'node:url';
import { defineConfig } from 'vitest/config';

export default defineConfig({
  resolve: {
    alias: {
      '@syzygy/cap1-core': fileURLToPath(
        new URL('./packages/cap1-core/src/index.ts', import.meta.url),
      ),
      '@syzygy/cap1-daemon': fileURLToPath(
        new URL('./packages/cap1-daemon/src/index.ts', import.meta.url),
      ),
    },
  },
  test: {
    projects: [
      {
        extends: true,
        test: {
          name: '@syzygy/cap1-conformance',
          include: ['packages/cap1-conformance/src/**/*.test.ts'],
        },
      },
      {
        extends: true,
        test: {
          name: '@syzygy/cap1-daemon',
          include: ['packages/cap1-daemon/src/**/*.test.ts'],
        },
      },
    ],
  },
});
```

Use this package export shape for both runtime packages:

```json
{
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js",
      "default": "./dist/index.js"
    }
  }
}
```

Vitest's explicit source aliases are the only no-prebuild path. Node and
TypeScript consumers use built JavaScript/declarations.

- [ ] **Step 1: Pin the clean-checkout matrix before editing**

The matrix is: `npm ci`; `npm test` without prebuild; `npm run build`;
`npm run typecheck`; direct built app startup; full system tests; guarded fresh
clone. Record current warning/failure output.

- [ ] **Step 2: Add the root Vitest config and remove the workspace file**

Run:

```bash
npm test
```

Expected: 53 files / 408 baseline tests before later task additions, no
`workspace file is deprecated` warning, and no process/system tests in the
default gate.

- [ ] **Step 3: Add conditional exports and remove `registerHooks`**

Replace the dynamic post-hook import in `apps/syzygy/src/main.ts` with ordinary
static imports from `@syzygy/cap1-daemon`. Do not retain an alias, fallback, or
legacy loader. If no static app import references `@syzygy/cap1-core`, remove
that direct dependency from `apps/syzygy/package.json` and its project reference
from `apps/syzygy/tsconfig.json`.

Update the system-test config comment and
`docs/CAPABILITY-1-IMPLEMENTATION-PLAN.md` so neither still names
`vitest.workspace.ts` or `registerHooks` as current behavior.

- [ ] **Step 4: Regenerate the lock and verify the Node floor**

```bash
npm install --package-lock-only --ignore-scripts
npm ci
```

Expected: root lock metadata records Node >=22.15, workspace dependency links
remain local, and no unrelated version upgrade enters the lock.

- [ ] **Step 5: Run the full clean/build/runtime matrix**

```bash
npm test
npm run build
npm run typecheck
npm run test:system
SYZYGY_FRESH_CLONE=1 npm run test:system
```

Expected: all commands PASS; the default gate has no deprecation warning; the
built app resolves `dist` package entries; the fresh clone needs no generated
files before `npm run build`.

- [ ] **Step 6: Mutate and restore both seams**

Point a runtime package default export back to `src/index.ts` and prove direct
built execution fails. Remove one Vitest alias and prove no-prebuild tests fail.
Restore, rerun the focused matrix, and declare files FROZEN.

- [ ] **Step 7: Commit**

```bash
git add vitest.config.ts vitest.workspace.ts package.json package-lock.json \
  packages/cap1-core/package.json packages/cap1-daemon/package.json \
  apps/syzygy/package.json apps/syzygy/tsconfig.json apps/syzygy/src/main.ts \
  packages/cap1-system/vitest.config.ts \
  packages/cap1-system/src/fresh-clone.system.test.ts \
  packages/cap1-daemon/src/package.test.ts \
  docs/CAPABILITY-1-IMPLEMENTATION-PLAN.md
git commit -m "chore: align Vitest and workspace runtime resolution"
```

Independent dependency/build/runtime-interface review is mandatory.

---

### Task 5: Project and Serve Reference-Bound Consent Coverage

**Runnable:** No—depends on Task 1's reviewed exact head and Task 3's multiset
helper.

**Files:**

- Modify: `packages/cap1-core/src/coverage.ts`
- Modify: `packages/cap1-core/src/index.ts`
- Modify: `packages/cap1-daemon/src/pipeline.ts`
- Modify: `packages/cap1-daemon/src/routes-machine.ts`
- Modify: `packages/cap1-daemon/src/routes-human.ts`
- Test: `packages/cap1-conformance/src/req-010.conformance.test.ts`
- Test: `packages/cap1-conformance/src/req-011.conformance.test.ts`
- Test: `packages/cap1-conformance/src/req-012.conformance.test.ts`
- Test: `packages/cap1-conformance/src/req-013.conformance.test.ts`
- Test: `packages/cap1-conformance/src/req-014.conformance.test.ts`
- Test: `packages/cap1-conformance/src/req-015.conformance.test.ts`
- Test: `packages/cap1-conformance/src/req-016.conformance.test.ts`
- Test: `packages/cap1-conformance/src/req-integration.conformance.test.ts`
- Test: `packages/cap1-daemon/src/pipeline.test.ts`
- Test: `packages/cap1-daemon/src/routes-machine.test.ts`
- Test: `packages/cap1-daemon/src/routes-human.test.ts`
- Test: `packages/cap1-system/src/consent-coverage.system.test.ts`
- Test: `packages/cap1-system/src/harness.ts`

**Interfaces:**

- Consumes: Task 1's closed `PreObservationConsentDecision` values and
  `VerifiedConsentRecord`; Task 3's canonical multiset helper.
- Produces: exact provenance on every executable coverage row and canonical
  coverage DTOs in both channels. It must not reload records, reconsider
  owner-act provenance, or re-resolve withdrawal precedence.

```ts
export function computeCoverage(
  declaration: ProjectDeclaration,
  consentByEntry: readonly PreObservationConsentDecision[],
  observations: readonly ObservationOutcome[],
): CoverageResult;
```

- [ ] **Step 1: Add coverage-provenance regressions**

Construct already-resolved Task 1 decisions for: verified observed,
verified-but-unreadable, exact withdrawal, unresolved reference, and unverified
owner-act provenance. Assert every declared repository gets one coverage row;
observed/capture-failed rows cite the exact verified record; withdrawal cites
the defeating record; invalid and unverified rows preserve Task 1's primary
basis and visible contradiction.

- [ ] **Step 2: Run coverage requirements RED**

```bash
npx vitest run \
  packages/cap1-conformance/src/req-010.conformance.test.ts \
  packages/cap1-conformance/src/req-011.conformance.test.ts \
  packages/cap1-conformance/src/req-012.conformance.test.ts \
  packages/cap1-conformance/src/req-013.conformance.test.ts \
  packages/cap1-conformance/src/req-014.conformance.test.ts \
  packages/cap1-conformance/src/req-015.conformance.test.ts
```

Expected: current `computeCoverage` accepts raw record arrays and drops consent
provenance from `capture-failed`.

- [ ] **Step 3: Make coverage a pure projection of Task 1 decisions**

Replace raw-record resolution inside `computeCoverage` with an ordinal join to
the already-closed decision for each declaration entry. A decision-count or
repository-identity mismatch fails fast as a caller contract violation; it is
never repaired by pair lookup.

- [ ] **Step 4: Add the complete projection matrix**

Cover all Task 1 decision arms plus missing observation, unreachable source,
captured source, and the existing partial/stale type arms. The latter retain
provenance structurally but remain excluded from runtime completion claims.

- [ ] **Step 5: Change coverage to consume entry decisions**

```ts
export function computeCoverage(
  declaration: ProjectDeclaration,
  consentByEntry: readonly PreObservationConsentDecision[],
  observations: readonly ObservationOutcome[],
): CoverageResult;
```

Add the exact in-force citation to `observed` and `capture-failed`; keep the
held `stale` type citation but do not produce it at runtime. Add declared
reference and typed failure basis to `unconsented`; withdrawn rows include the
withdrawal citation.

- [ ] **Step 6: Preserve Task 1 authorization without re-resolution**

Add a pipeline test that supplies a closed unverified decision and proves the
coverage/route layer preserves its untrusted fields, effective `Unknown`, and
owner-adjudication contradiction exactly. Static import review must show no
coverage or route module importing the consent loader or provenance verifier.

- [ ] **Step 7: Serve canonical coverage rows in both channels**

Add `coverageBoundary` to `MachineProjectEvaluatedBody`. Render the same rows in
HTML with repository ID, state, reason, reference, record digest, scope,
attribution, and grant state as machine-readable attributes.

- [ ] **Step 8: Build the independent wire oracle**

Parse JSON and HTML separately into complete tuples, compare multiset counts in
both directions, and assert the denominator equals the declared repository
count. Mutations that omit, add, duplicate, or alter a row in either channel
must fail.

- [ ] **Step 9: Run focused tests and controlled mutations**

```bash
npx vitest run \
  packages/cap1-conformance/src/req-010.conformance.test.ts \
  packages/cap1-conformance/src/req-011.conformance.test.ts \
  packages/cap1-conformance/src/req-012.conformance.test.ts \
  packages/cap1-conformance/src/req-013.conformance.test.ts \
  packages/cap1-conformance/src/req-014.conformance.test.ts \
  packages/cap1-conformance/src/req-015.conformance.test.ts \
  packages/cap1-conformance/src/req-016.conformance.test.ts \
  packages/cap1-daemon/src/pipeline.test.ts \
  packages/cap1-daemon/src/routes-machine.test.ts \
  packages/cap1-daemon/src/routes-human.test.ts
npm run build
npx vitest run --config packages/cap1-system/vitest.config.ts \
  src/consent-coverage.system.test.ts
```

Mutate decision-to-row joining, capture-failed citation carriage, unverified
record visibility, and row parity separately; observe each intended failure
and restore.

- [ ] **Step 10: Run full gates and commit**

```bash
npm run typecheck
npm test
npm run test:system
SYZYGY_FRESH_CLONE=1 npm run test:system
git add packages/cap1-core packages/cap1-daemon packages/cap1-conformance \
  packages/cap1-system
git commit -m "feat: project reference-bound CAP1 coverage"
```

Independent security/determinism/public-interface review is mandatory.

---

### Task 6: Serve Evidence-Backed Repository Discoverability

**Runnable:** No—depends on Tasks 1, 3, 4, and 5 reaching `main`, including
captured repository locator context.

**Files:**

- Create: `packages/cap1-daemon/src/readme-links.ts`
- Create: `packages/cap1-daemon/src/readme-links.test.ts`
- Modify: `packages/cap1-daemon/package.json`
- Modify: `package-lock.json`
- Modify: `packages/cap1-core/src/discoverability.ts`
- Modify: `packages/cap1-daemon/src/observation.ts`
- Modify: `packages/cap1-daemon/src/pipeline.ts`
- Modify: `packages/cap1-daemon/src/routes-machine.ts`
- Modify: `packages/cap1-daemon/src/routes-human.ts`
- Modify: `packages/cap1-daemon/src/index.ts`
- Modify: `apps/syzygy/src/main.ts`
- Test: `packages/cap1-conformance/src/req-040.conformance.test.ts`
- Test: `packages/cap1-conformance/src/req-041.conformance.test.ts`
- Test: `packages/cap1-conformance/src/req-050.conformance.test.ts`
- Test: `packages/cap1-conformance/src/req-051.conformance.test.ts`
- Test: `packages/cap1-conformance/src/req-052.conformance.test.ts`
- Test: `packages/cap1-conformance/src/req-053.conformance.test.ts`
- Test: `packages/cap1-conformance/src/req-064.conformance.test.ts`
- Test: `packages/cap1-daemon/src/pipeline.test.ts`
- Test: `packages/cap1-daemon/src/routes-machine.test.ts`
- Test: `packages/cap1-daemon/src/routes-human.test.ts`
- Test: `packages/cap1-system/src/full-facts.system.test.ts`
- Test: `packages/cap1-system/src/fresh-clone.system.test.ts`
- Test: `packages/cap1-system/src/harness.ts`

**Interfaces:**

- Consumes: Task 1's captured README/entry/link context, versions, and closed
  consent decisions; Task 3's multiset helper; Task 5's canonical coverage
  projection.
- Produces: a deterministic semantic hyperlink adapter; identity-bearing
  discoverability evidence; required discoverability/authority/proposal plane
  arms; one explanation per finding; identical human/machine rows.

```ts
export const README_LINK_READER_VERSION =
  'marked@18.0.10+parse5@8.0.1;gfm=true' as const;

export interface ReadmeLinkContext {
  readonly canonicalWebBase: string | undefined;
  readonly defaultBranch: string | undefined;
}

export type ReadmeEntryLinkResult =
  | {
      readonly state: 'classified';
      readonly linksToEntry: boolean;
      readonly qualifyingHref: string | undefined;
    }
  | {
      readonly state: 'unclassifiable';
      readonly reason: 'repository-locator-unavailable' | 'ambiguous-target';
      readonly href: string;
    };

export function extractReadmeEntryLink(
  markdown: string,
  context: ReadmeLinkContext,
): ReadmeEntryLinkResult;

export type DiscoverabilityPlane =
  | { readonly state: 'available'; readonly rows: readonly EvaluatedDiscoverability[] }
  | {
      readonly state: 'unavailable';
      readonly reason: 'target-unclassifiable' | 'snapshot-input-unavailable';
    };

export type AuthorityPlane =
  | { readonly state: 'available'; readonly values: readonly AuthorityExposure[] }
  | { readonly state: 'unavailable'; readonly reason: 'authority-input-not-designed' };

export type ProposalPlane =
  | { readonly state: 'available'; readonly values: readonly ProposalRendering[] }
  | { readonly state: 'not-produced'; readonly reason: 'proposal-input-not-designed' };

export interface EvaluatedProjectPlanes {
  readonly discoverability: DiscoverabilityPlane;
  readonly authorityExposures: AuthorityPlane;
  readonly proposals: ProposalPlane;
  readonly entry: CapturedProjectInputs['entry'];
}
```

`EvaluatedProjectPlanes` and its daemon-owned `entry` reference live in
`packages/cap1-daemon/src/pipeline.ts`; putting them in core would invert the
dependency on `CapturedProjectInputs`. Pure discoverability evidence, finding,
and proposal row/value types remain in `cap1-core`.

Use `marked.parse(markdown, { gfm: true, async: false })`, pass its output only
to `parse5.parseFragment`, walk `<a href>` elements, and discard the HTML. Never
render that unsanitized intermediate. Exact pins pay rent by covering inline,
reference, autolink, GFM, and raw-HTML anchor semantics without an owned
Markdown/HTML parser.

- [ ] **Step 1: Add exact dependencies and parser matrix RED**

```bash
npm install --save-exact --workspace packages/cap1-daemon \
  marked@18.0.10 parse5@8.0.1
npx vitest run packages/cap1-daemon/src/readme-links.test.ts
```

Expected first test result: FAIL because the adapter is absent.

- [ ] **Step 2: Implement semantic hyperlink extraction**

Count inline, reference, autolink, GFM absolute, and raw `<a>` forms when their
resolved target is the fixed entry. Ignore plain text, code, comments, images,
and different targets. Relative paths resolve from the root README; normalize
`.`/`..`; ignore query/fragment for resource identity. Absolute links count only
through captured canonical repository locator context. Malformed percent
escapes, encoded separators, backslashes, or target-looking absolute links
without locator context return `unclassifiable`, never `no`.

- [ ] **Step 3: Perform the substring mutation check**

Temporarily replace extraction with `markdown.includes(HUMAN_ENTRY_PATH)`.
Plain-text, code, comment, image, and near-match tests must fail. Restore and
rerun parser tests GREEN.

- [ ] **Step 4: Extend pure discoverability evidence**

Replace boolean-only captured evidence with a typed captured README arm carrying
`relativePath: 'README.md'`, digest, and `linksToEntry`; retain unconsented,
uncaptured, and undeclared arms. Make the finding basis required and typed.

- [ ] **Step 5: Add required evaluated planes**

The evaluated arm must always contain discoverability, authority, proposals,
and captured entry fields. Authority uses
`unavailable: authority-input-not-designed`; proposals use
`not-produced: proposal-input-not-designed`. Remove optional human route
providers and machine `OPEN_PROPOSALS`.

During dependency review, verify and retain the exact resolved `entities`
version selected under `parse5@8.0.1`; no transitive version may drift as an
unreviewed side effect.

- [ ] **Step 6: Compute one row and explanation per declared repository**

Apply role before consent before README. Observed-source is
`not-applicable` without parsing; unconsented governance-root is Unknown #6
without parsing; missing/unreadable README is Unknown #10; classified captured
README yields `yes`/`no`; unclassifiable target makes the plane unavailable.
Attach README digest/reference/basis and a `Why this answer?` fact set.

- [ ] **Step 7: Serialize both public channels**

Machine JSON and human HTML expose complete row tuples: repository ID, value,
label, primary reason, typed basis, evidence identity, proposal state, and full
explanation. `/entry` continues to use captured input only.

- [ ] **Step 8: Add the independent system oracle**

Parse JSON and HTML separately, canonicalize complete rows, compare multiset
counts bidirectionally, and assert the denominator equals declared repository
count. Add/remove/duplicate/alter one row in each direction and prove failure.

- [ ] **Step 9: Run focused tests and mutations**

```bash
npx vitest run \
  packages/cap1-daemon/src/readme-links.test.ts \
  packages/cap1-daemon/src/pipeline.test.ts \
  packages/cap1-daemon/src/routes-machine.test.ts \
  packages/cap1-daemon/src/routes-human.test.ts \
  packages/cap1-conformance/src/req-040.conformance.test.ts \
  packages/cap1-conformance/src/req-041.conformance.test.ts \
  packages/cap1-conformance/src/req-050.conformance.test.ts \
  packages/cap1-conformance/src/req-051.conformance.test.ts \
  packages/cap1-conformance/src/req-052.conformance.test.ts \
  packages/cap1-conformance/src/req-053.conformance.test.ts \
  packages/cap1-conformance/src/req-064.conformance.test.ts
npm run build
npx vitest run --config packages/cap1-system/vitest.config.ts \
  src/full-facts.system.test.ts
```

- [ ] **Step 10: Run full/fresh-clone gates and commit**

```bash
npm run typecheck
npm test
npm run test:system
SYZYGY_FRESH_CLONE=1 npm run test:system
git add package-lock.json packages/cap1-core packages/cap1-daemon \
  packages/cap1-conformance packages/cap1-system apps/syzygy
git commit -m "feat: serve evidence-backed CAP1 discoverability"
```

Independent deterministic-observation, dependency, untrusted-content, and
human/machine public-interface review is mandatory.

---

## Epic-Level Reconciliation and Report

After Tasks 1–6 that are released by their dependencies reach `main`, run one
generation-1 reconciliation bead. It audits the codebase—not only sibling
diffs—against the approved design and CAP1 requirements, including universal
no-read-before-consent, no-post-capture-read, exact declared denominators,
parity multiplicity, and the held-work exclusions. Missing/partial behavior is
reported as cold-start-ready gap candidates; it is not silently accepted.

After reconciliation reports complete executable coverage, run one epic report
bead. It scaffolds `docs/reports/<epic-id>-cap1-runtime-hardening.md`, updates
`PROJECT-STATUS.md` and the hosted-workflow description from fresh exact-head
evidence, and lists the held CAP1-REQ-013 stale/observer-failure limbs,
CAP1-REQ-062 currency/staleness limb, CAP1-REQ-046 authority-input limb, and
proposal carriage. No held limb may be called implemented.

---

## Plan Self-Review

- **Spec coverage:** Tasks 1, 3, 5, and 6 map every executable design limb to
  CAP1 requirements and real-seam verification. Task 2 covers the authorized
  security debt; Task 4 covers bounded implementation tooling debt. Held rows
  are explicit and have no implementation step.
- **Placeholder scan:** The plan contains no unresolved implementation marker;
  the audit source is an explicit hard gate with a status-quo default, not a
  hidden implementation choice.
- **Type consistency:** Task 5 consumes Task 1's closed
  `PreObservationConsentDecision` and `VerifiedConsentRecord`; Task 6 consumes
  Task 1's captured inputs and link context, Task 3's multiset helper, and Task
  5's coverage projection. No later task re-resolves or renames Task 1's consent
  decision.
- **Cohesion:** Tasks sharing two or more ownership signals are bundled or
  serialized. Task 6 remains one vertical bead because parser, projection,
  routes, explanations, and system parity share the same interface, fixtures,
  review surface, and rollback.

---

## Execution Handoff

Use the Beads graph created with this plan. The coordinator may initially
dispatch only Task 2 (security boundary) and Task 3 (parity). Task 4 becomes
runnable after Task 2 reaches `main`. It must not dispatch snapshot, consent,
or discoverability until the human audit-source gate and their dependency edges
are satisfied. Reconciliation and report run last. No task in this plan
authorizes unattended execution by itself.
