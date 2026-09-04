# PWB live exact-head engineering, security, and test review — raw

Review date: 2026-09-05
Reviewer: independent fresh-context engineering/security/test reviewer
Syzygy subject: `cd6c95250772d98c199020c08e25476fbe34bb5b`
Observed Butlers subject: `a3dd1fe08a1d9a11b5e899e0ecf33f03d8eefc96`
Runtime: `127.0.0.1:7478`, with the same daemon mounted at tailnet path
`/butlers-syzygy`
Standing review prompts applied: Craft and Care; Security, Authority, and
Untrusted Inputs
Risk floors touched: truth, evidence, deterministic observation, public
interface, and security/consent

## Verdict

**REVISE**

[Observed] The exact-head suite is green and several important controls work,
but the live product fails its central project-comprehension outcome. The
production observer omits the Heart and Soul and Spec and Spine roots, presents
four resulting empty classes as Observed zero, cannot observe the signed
change's known eight-versus-nine contradiction, and offers no route to a
verbatim requirement. The supplied baseline records that the owner aborted the
walkthrough as unusable and performed no judgment act. These are not minor copy
exceptions; they are truth and acceptance failures under VIS-1, VIS-2,
PWB-REQ-001/002/004/010/011/015/021, CC-BAR-3, and CC-TEST-6.

[Observed] There are also security-boundary defects that a clean current tree
does not trigger: the consented repository identity is not bound to the CLI
locator; phase-A index bodies are parsed before the adopted classifier runs;
and governance lifecycle/tag checks can accept incomplete ambient state. These
must be repaired without weakening the fail-closed policy.

## Trust-boundary model reviewed

1. Syzygy's governance plane supplies three authorization-bearing artifacts
   and three owner-act records. Their effective state is supposed to decide
   whether any Butlers project-shape body may be read.
2. A CLI locator selects one local Git repository. That concrete locator must
   be bound to the consented opaque identity
   `repository:butlers-configured-poc`; a flag is not consent.
3. Phase A reads the root and pillar indexes and derives a revision-bound
   manifest. Phase B reads exact Git blobs, applies the secret policy, extracts
   declarations, reconciles coverage/contradictions, and builds one immutable
   model.
4. Polaris and authenticated `GET /api/poc` project that same model. Tailnet
   ingress adds TLS and device restriction outside the daemon; browser Origin
   admission and machine bearer admission remain daemon controls.
5. The walkthrough execution record is a kernel record. The separate owner
   judgment is authorization-bearing and may be carried only through a lawful
   owner act. Neither is empirical proof that comprehension succeeded.

Butlers Markdown, Git metadata, paths, filenames, and work state were treated
as untrusted inputs throughout this review.

## Confirmed controls and contrary evidence

- [Observed] `git rev-parse HEAD` in the review worktree returned the exact
  subject. The running process is
  `node apps/three-surface-poc/dist/main.js --repo /home/tze/GitHub/butlers`,
  and that repository's local HEAD is the exact supplied Butlers subject.
- [Observed] Exact-head Vitest completed with **100 passed files, 2 skipped;
  1219 passed tests, 2 skipped**. The six Polaris browser variants ran in a
  real browser; they were not among the skipped tests. This is useful
  development feedback, not a retained CC-TEST-2 gate artifact.
- [Observed] The focused six-file risk suite completed **95/95**. It includes
  manifest, model, authority-loader, judgment-loader, Polaris shape, and parity
  tests. Its green result is important contradictory evidence for the findings
  below: the defects are oracle/population gaps, not ordinary failing tests.
- [Observed] Loopback and tailnet Polaris each returned 200. The loopback
  listener is bound only to `127.0.0.1:7478`; an untrusted browser Origin
  returned 403; unauthenticated `GET /api/poc` returned 401. No bearer value was
  read or printed.
- [Observed] The current three state-(1) act-record bytes are byte-identical to
  their recording-tag trees; all 54 current decision Markdown files are
  readable; a fixed-string sweep found no later decision naming any of the
  three effect-act identities. Thus the current live admission is not shown to
  be unauthorized by the latent loader defects below.
- [Observed] The live page truthfully carries the walkthrough as `absent`,
  `no-run-record`, criterion `unknown-never-met`. It does not fabricate the
  owner's verdict.
- [Observed] The phase-B reader uses exact object IDs, refuses path
  normalization differences/symlink and submodule modes, hashes returned blob
  bytes, uses strict UTF-8, and escapes rendered content. Its focused tests and
  mutation evidence cover many meaningful failure arms.
- [Observed] The parity test is strong for the population the model already
  contains: it is multiplicity-preserving and exercises authority/judgment
  states. Parity does not prove that the producer selected the complete or
  correct source population.
- [Observed] The supplied generic spec-trace scan reports 86 errors/83 warnings
  because it expects the newer ID/Source/Scope layout, while these signed POC
  specs use the earlier format. Per the review baseline, that incompatibility
  is not treated as a defect and does not authorize editing digest-bound specs.

## Findings

### BLOCKER 1 — The consented repository identity is not bound to the CLI locator

**Supporting evidence checked**

- The act-bound consent records the current locator
  `/home/tze/GitHub/butlers`
  (`.syzygy/governance/decisions/BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md:13-18`),
  and the adopted registry declares a `repository-locator-mapping`
  deterministic input
  (`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json:41-47`).
- The CLI accepts any non-empty `--repo` value and calls that “exactly one
  explicit repository” (`apps/three-surface-poc/src/cli.ts:14-59`). `main.ts`
  merely resolves that path, observes its HEAD, and passes it to the model
  (`apps/three-surface-poc/src/main.ts:45-65,153-164`).
- The PWB builder defaults every such repository to the constant identity
  `repository:butlers-configured-poc` and constructs its Git runner from the
  caller's locator
  (`packages/three-surface-poc-core/src/project-shape-model.ts:70-72,438-450`;
  `packages/three-surface-poc-core/src/model.ts:595-605`). No comparison binds
  locator, Git common directory, remote identity, or another approved mapping
  to the consented repository.
- `buildButlersPocModel` also opens the five legacy intent/code/test artifact
  paths from that caller-selected working tree before it builds the gated PWB
  shape (`packages/three-surface-poc-core/src/model.ts:334-345`). A wrong
  locator therefore crosses the older bounded observation seam as well as the
  PWB Git-object seam.
- The CLI test considers an arbitrary `/work/butlers` string sufficient
  (`apps/three-surface-poc/src/cli.test.ts:5-36`). Model/surface tests routinely
  pass an arbitrary temporary Git repository with an admitting authority and
  receive the constant Butlers identity.

**Contradictory/mitigating evidence checked**

- The currently running daemon was in fact invoked with the intended local
  Butlers path, and that path resolved to the supplied exact commit.
- The 195-case evaluator correctly compares the opaque repository identity in
  the consent and registry artifacts. The missing link is from that opaque
  identity to the concrete repo selected by the CLI.

**Why this blocks confirmation**

An owner or script can point the daemon at a different repository carrying the
five legacy POC fixture paths; the three Butlers acts still admit and the model
labels the other repository as Butlers. A CLI argument cannot widen recorded
per-repository consent. This crosses SEC-2/SEC-5 and PWB-REQ-005's subject
boundary even though the current invocation is correct.

**Minimum fix**

Bind the resolved locator and resolved Git common directory to the approved
repository-locator mapping before any observed-repository body read, and include
that mapping identity in the evaluation inputs. The existing act-bound consent
locator is one possible bounded source if that is the intended contract
reading. Add an end-to-end counterexample in which an otherwise Butlers-shaped
second repository is supplied and the read spy remains zero.

**Authority route:** implementation fix if it consumes the already act-bound
mapping/locator semantics. Any new mapping authority, portable identity scheme,
or widening beyond the one recorded locator returns to the signed-spec/owner
gate.

### BLOCKER 2 — Real source discovery omits two pillars, then converts the omitted population into Observed zero

**Supporting evidence checked**

- The signed population begins with the five roots “named in Butlers' root
  project-shape index”
  (`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md:8-14`),
  and PWB-REQ-001's oracle requires independent comparison to the real Butlers
  indexes (`spec.md:81-96`).
- At exact Butlers head, `about/README.md:15-21` names Heart and Soul with
  directory ``about/heart-and-soul/`` but links its start file as
  `heart-and-soul/vision.md`; it names Spec and Spine with directory
  ``openspec/`` and no Markdown link. The implementation removes code spans,
  considers only Markdown link targets, and recognizes a root only when the
  target itself is a pillar directory or ends in `README.md`
  (`packages/three-surface-poc-core/src/project-shape-manifest.ts:165-201,
  321-343`). The Heart link therefore produces key `vision.md`, and the Spec
  directory is never considered.
- Live exact-head output contains zero occurrences of
  `about/heart-and-soul/README.md`, `vision.md`, `architecture.md`, or `v1.md`.
  It shows purpose, promises, refusals, architecture, V1 scope, and V1 success
  as `missing-declaration` even though those exact declarations exist at the
  reviewed Butlers commit.
- Unknown pillar state is retained only in the phase-A manifest. Coverage is
  built from the sources that made it into `manifest.sources`; the model does
  not project `manifest.pillars` into coverage
  (`packages/three-surface-poc-core/src/project-shape-model.ts:489-526`). With
  zero class sources, coverage declares a known denominator of zero
  (`packages/three-surface-poc-core/src/project-shape-coverage.ts:341-358`),
  and `classAggregate` labels it Observed
  (`packages/three-surface-poc-core/src/project-shape-model.ts:382-397`).
  `projectAccountOf` then maps an empty source set to `missing-declaration`
  (`project-shape-model.ts:400-425`).
- The live page consequently says “No admitted source declares this class” and
  `Observed · report-fact · fresh` with `0 declared` for four classes:
  project-account-section, principle, success-criterion, and catalog-entry.
  That is confident absence produced by observer failure.

**Contradictory/mitigating evidence checked**

- `project-shape-manifest.test.ts` passes 18/18, but its fabricated root creates
  an `about/spec-and-spine/README.md` tree that real Butlers does not have and
  uses direct directory/README links for all five roots
  (`project-shape-manifest.test.ts:39-104`). The app fixture repeats that shape
  (`apps/three-surface-poc/src/test-project-shape-fixture.ts:83-105`).
- Per-source missing/excluded cases that are already in the manifest do render
  Unknown correctly. The missed case is an unknown discovery root whose
  dependent source population never enters the downstream denominator.
- The retained older fresh run records the same four classes as Observed zero
  (`docs/evidence/pwb-p4-5-fresh-checkout-demo-2026-09-04.json:190-234`), but
  treats that output as data rather than failing the independent population
  oracle.

**Why this blocks confirmation**

This is the exact self-selected-model failure PWB was created to stop. It makes
the first four reading groups unable to explain Butlers and gives the owner the
wrong resolution route (“draft it”) for facts that are already declared. It
violates VIS-1/VIS-2, PWB-REQ-001/002/003/010, CC-BAR-3, and CC-TEST-6.

**Minimum fix**

Parse the actual five-row root table (including the Directory column and the
`Spec and Spine` -> `openspec/` mapping) or otherwise implement an equivalent
literal rule that recognizes any declared start file within its named root.
Carry each pillar-discovery outcome into downstream class coverage: an unknown
root or index must make every dependent denominator and the whole-shape claim
Unknown, never known zero or `missing-declaration`. Add a real-layout regression
fixture independently transcribed from exact Butlers `about/README.md`, then a
live exact-revision sweep that requires 5/5 roots, all three owning account
files, and all six account statements.

**Authority route:** implementation and test repair; no policy relaxation and
no signed artifact edit is needed for the five roots already named by the
signed grammar.

### BLOCKER 3 — The known real contradiction and precedence rules have no production ingestion path

**Supporting evidence checked**

- The signed design explicitly names the real conflict: `about/README.md` says
  eight domain butlers while `about/heart-and-soul/v1.md` declares nine, and
  requires Polaris to expose it
  (`openspec/changes/polaris-project-wide-butlers-model/design.md:8-13`). Exact
  Butlers head still has “3 staffers + 8 domain butlers” at
  `about/README.md:103-106` and nine top-level domain entries at
  `about/heart-and-soul/v1.md:35-69`.
- The root index has no extraction class
  (`packages/three-surface-poc-core/src/project-shape-manifest.ts:224-243`).
  The only way coverage receives summary declarations or precedence rules is
  through injectable `rules` and `statedDeclarations`; comments admit
  production passes none
  (`packages/three-surface-poc-core/src/project-shape-model.ts:304-315`;
  `packages/three-surface-poc-core/src/model.ts:153-165`). `main.ts` supplies
  neither.
- Live exact-head Polaris reports “No two admitted declarations disagree.” It
  exposes no contradiction for the design's named eight-versus-nine case.

**Contradictory/mitigating evidence checked**

- Coverage and rendering tests exercise contradictions and explicit precedence
  correctly when tests inject synthetic declarations/rules
  (`packages/three-surface-poc-core/src/project-shape-model.test.ts:647-705`;
  `apps/three-surface-poc/src/polaris-reachability.test.ts:47-59,272-319`).
  That proves the downstream reconciler, not production observation.
- Once Heart and Soul is fixed, the V1 catalog can supply the nine-item side.
  The eight-item root summary and Butlers' actual precedence table still have
  no extractor or production wiring.

**Why this blocks confirmation**

PWB-REQ-004's named real counterexample is unreachable in production, while a
fixture-only seam makes the suite look complete. The surface silently reports
absence of contradiction instead of preserving both authorities.

**Minimum fix**

Add a deterministic, revision-bound production extractor for the exact root
summary fact and the documented Butlers precedence table, then wire those
declarations/rules into `buildProjectShape`. The real-source regression must
assert that both 8 and 9, both source anchors, and the applicable precedence
outcome (or Unknown pending adjudication) are present.

**Authority route:** if the signed reader grammar already authorizes these as
project facts under PWB-REQ-004, this is implementation repair. If a new
statement/rule grammar or identity must be invented, stop and use CC-REV-2's
signed-spec amendment path; do not hard-code a winner in Syzygy.

### BLOCKER 4 — “Exact source” stops at a metadata row; no verbatim requirement is reachable

**Supporting evidence checked**

- PWB-REQ-011 requires progressive reach to exact authoritative artifacts and
  exact requirement text (`spec.md:502-530`); PWB-REQ-015 requires a verbatim
  current requirement/scenario (`spec.md:675-710`); PWB-REQ-021 requires the
  owner to reach exact intent from Polaris alone (`spec.md:805-837`).
- `supportCitations` links only to an in-page `#polaris-source-*` fragment
  (`apps/three-surface-poc/src/polaris.ts:329-343`). The target row contains
  path, identity, rule, outcome, digest, and count metadata, but no artifact
  body (`polaris.ts:531-548`). `pocRoutes` defines no source/artifact route
  (`apps/three-surface-poc/src/routes.ts:81-152`). Probes of `/source`,
  `/sources`, `/artifact`, and `/api/source` all returned 404.
- The test named “reaches the exact source” considers a fragment resolving to
  that metadata row sufficient
  (`apps/three-surface-poc/src/polaris-project-shape.test.ts:177-226`). It never
  compares reached bytes to the authoritative artifact.
- Production passes no `VerbatimLeafReader`; the resolver explicitly returns
  `unconsented-source-or-provider` when absent
  (`apps/three-surface-poc/src/capability-detail.ts:165-193`;
  `apps/three-surface-poc/src/polaris.ts:922-934`). On the exact live page there
  are **0** `data-verbatim="rendered"` regions, **1** not-rendered region, and
  **119** source-fragment links. The sole deep dive says its current authority
  and requirement text are Unknown.
- The supplied owner baseline records the walkthrough as aborted and the page
  unusable (`/tmp/syzygy-pwb-recovery.2fCvej/baseline.md:13-14`).

**Contradictory/mitigating evidence checked**

- All fragment links resolve and are keyboard-operable; the exact-head browser
  suite verifies focus, accessible names, and contrast. This is good navigation
  to evidence metadata, not reachability of the artifact or requirement.
- `resolveVerbatim` correctly refuses forged, binary, or digest-mismatched
  bytes in tests. The secure seam exists, but production never supplies it.
- The live judgment remains absent/Unknown, so the implementation does not
  falsely claim that the failed walkthrough passed.

**Why this blocks confirmation**

The mandatory owner prompt “Where does exactness live? Reach one verbatim
requirement” is impossible on the current surface. Internal link integrity
cannot substitute for source reachability. This independently explains why
mechanical accessibility/parity can pass while the owner cannot complete the
cold open.

**Minimum fix**

Provide a contained, authenticated source-resolution route or render-time
reader that serves only exact, revision-bound, policy-admitted bytes and keeps
excluded bodies withheld. Ensure at least one adopted capability deep dive can
reach a current verbatim requirement and scenario; compare the reached bytes
to the captured Git object in a browser/system test. Keep proposal bytes
visibly proposed and non-authoritative.

**Authority route:** implementation may expose already consented,
policy-admitted baseline-spec content only if the existing content class truly
covers that body use. The selected active WhatsApp proposal lies outside the
current baseline source population; reading it or widening the content class
requires the applicable signed-spec/consent/policy owner acts. Do not bypass the
Unknown while that gate is unresolved.

### HIGH 1 — Governance authority loading is ambient, incompletely tag-bound, and fails open on lifecycle read errors

**Supporting evidence checked**

- The loader reads authority artifacts and act records from current working-tree
  paths (`apps/three-surface-poc/src/governance-inputs.ts:117-130,220-243`).
  The runtime dirty-input guard protects app/core source and root manifests, but
  deliberately does not protect `.syzygy/**`
  (`apps/three-surface-poc/src/git-observation.ts:47-61`).
- `resolveRecordingTag` proves only that the tag commit contains the record
  **path**; it does not compare the tag's act-record blob to the bytes being
  parsed (`governance-inputs.ts:143-160`). Therefore a coordinated current-tree
  edit to an authority artifact and its act record can satisfy their mutual
  digest while the old tag merely supplies path existence.
- `lifecycleFor` returns an empty lifecycle when directory enumeration fails and
  silently skips any decision file it cannot decode/read
  (`governance-inputs.ts:181-212`). The evaluator treats absence of
  `supersededBy`/`revokedBy` as current and may admit
  (`packages/three-surface-poc-core/src/body-read-authority.ts:508-516,
  709-733`). The walkthrough judgment loader reuses the same function
  (`apps/three-surface-poc/src/walkthrough-inputs.ts:91-119`).

**Contradictory/mitigating evidence checked**

- At this exact head, all three current act records match their recording-tag
  blobs byte-for-byte; all 54 decision files are readable; no later decision
  names the three effect-act identities. No current unauthorized read was
  demonstrated.
- Tests catch a present synthetic revocation/supersession and an unresolved
  tag. They do not make `listDirectory` throw, make one later decision
  unreadable, or pair a modified artifact with a correspondingly modified
  current act record while the tag still points to old bytes
  (`apps/three-surface-poc/src/governance-inputs.test.ts:88-165`).
- State (1) openly accepts same-tree forgeability and never claims independent
  verification. It still requires the exact owner phrase, act record, and
  recording commit/tag (`RFC3-16(c)`); path-only tag resolution is weaker than
  that disclosed record semantics.

**Why it matters**

An unreadable revocation source can widen authority by omission, and an ambient
act record can drift independently of its claimed recording context. Both are
the wrong polarity for an authorization-bearing ingest gate.

**Minimum fix**

Read the authority artifacts, act records, and lifecycle population from one
identified Git tree (or prove every working byte equal to that tree); bind the
exact act-record blob to its recording tag; sort and identity-stamp the complete
lifecycle population; and turn any inability to enumerate/read it into a
non-admitting/not-evaluated result. Add the three counterexamples above to the
loader and end-to-end zero-read tests.

**Authority route:** implementation/security repair within the current
fail-closed contract. No weakening or new provenance state is proposed.

### HIGH 2 — Phase A parses unclassified index bodies

**Supporting evidence checked**

- The adopted policy applies its six-step classification order to phase-A or
  phase-B membership and requires every detector before parsing
  (`.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json:128-136`;
  CC-SEC-5).
- Phase A checks tree membership, size, object identity, NUL, and UTF-8, then
  hands raw text directly to manifest derivation
  (`packages/three-surface-poc-core/src/project-shape-observation.ts:391-443`).
  Manifest derivation parses root/pillar links immediately
  (`packages/three-surface-poc-core/src/project-shape-manifest.ts:321-407`).
  Secret detectors and active-content handling run only later, when phase B
  rereads the completed manifest population
  (`packages/three-surface-poc-core/src/project-shape-model.ts:468-498`).
- A secret-shaped internal link destination in a seed can therefore become a
  manifest/source path and reach model/HTML/JSON before the body is excluded in
  phase B. Path rules do not apply the body detector regex to that derived path.

**Contradictory/mitigating evidence checked**

- Phase-B classification tests pass 18/18 and scan returned records for
  controlled sentinels. They plant secrets in phase-B sources, not in the
  phase-A root/pillar indexes that define the manifest
  (`packages/three-surface-poc-core/src/content-classification.test.ts:44-70,
  270-313`).
- A content-blind live HTML check found zero private-key markers, known-token
  markers, or credential-bearing URL markers. This lowers evidence of a current
  leak; it does not close the phase-A path.

**Minimum fix**

Apply the act-bound policy to each phase-A seed before `indexLinkTargets` sees
it. On a match, parse failure, or classifier failure, keep the index/pillar
visible as Unknown and derive no child paths from its bytes. Add phase-A
sentinels in prose, link text, and internal link destinations and scan every
returned sink.

**Authority route:** implementation repair that strengthens the approved
policy; do not whitelist active or secret-bearing seed content.

### HIGH 3 — Parse-time and rendered-output limits are declarations, not controls

**Supporting evidence checked**

- PWB-REQ-006 requires source-count, byte, depth, parse-time, and
  rendered-output limits, with a counterexample for each
  (`spec.md:340-362`). The registry declares 250 ms per source and 2,097,152
  rendered bytes
  (`POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json:123-130`).
- A complete production-source search found `maxParseMillisecondsPerSource`
  and `maxRenderedBytes` only in the limit type/default declaration. No parser,
  model builder, route, HTML renderer, or JSON renderer measures or enforces
  either. The only other references are a unit test that loops over all keys of
  the generic `evaluateLimit` helper
  (`packages/three-surface-poc-core/src/git-object-reader.test.ts:371-380`).
- The retained prior live evidence records authenticated `/api/poc` at
  **4,644,380 bytes**, already above the registry's rendered-byte value
  (`docs/evidence/pwb-p4-5-fresh-checkout-demo-2026-09-04.json:95-102`). The
  exact current Polaris HTML is 1,069,549 bytes, below that particular value
  but large enough to show the budget is material.
- Phase-A and phase-B byte counters also start independently, so
  `maxTotalBytes` is not a single total over every body read in one evaluation
  (`project-shape-observation.ts:391-420`; `git-object-reader.ts:255-317`).

**Contradictory/mitigating evidence checked**

- Source count, per-source bytes, phase-local total bytes, and index depth have
  real checks and focused boundary tests. The missing controls are not the
  entire resource envelope.
- The 4.64 MB machine artifact is from Syzygy `7de2f68` and Butlers `59e5caa`,
  not the exact reviewed heads; exact current authenticated JSON size was not
  probed because this review did not read the bearer credential.

**Minimum fix**

Measure parse work with a deterministic bounded mechanism or an explicit
resource counter, enforce rendered bytes before either response is served,
carry phase-B reader breaches into `shape.limitBreaches`, and use one
evaluation-wide source/byte budget across both phases. Every breach must keep
the affected population visible as Unknown. Add integration mutations for each
named limit; testing the generic comparator alone is tautological.

**Authority route:** implementation repair under the existing registry limits.
Changing a limit or its consequence requires the registry/spec owner gate.

### HIGH 4 — The fresh-checkout command can return success while its recorded parity and subject checks fail

**Supporting evidence checked**

- The command computes clone-head equality, observed/model revisions, shape
  state, authority, parity differences, limit breaches, daemon exit, and
  walkthrough state
  (`apps/three-surface-poc/src/fresh-checkout-demo-main.ts:226-310`). Its final
  `healthy` predicate checks only install/build/test exit codes, four human
  200s, and machine 401/200 (`fresh-checkout-demo-main.ts:316-317`). It does
  **not** gate clone head,
  observed/model revision equality, body-read admission, project-shape kind,
  either parity difference, duplicate claim IDs, resource breaches, or daemon
  exit.
- No test imports or exercises the fresh-checkout command. A repository search
  finds only the command itself and its package script.
- The sole retained fresh-checkout record is not exact-head evidence: it binds
  Syzygy `7de2f681...` and Butlers `59e5caaf...`, while this review is bound to
  `cd6c9525...` and `a3dd1fe0...`
  (`docs/evidence/pwb-p4-5-fresh-checkout-demo-2026-09-04.json:6-12,41-50`).
  Relevant runtime/loader files changed after `7de2f68`.

**Contradictory/mitigating evidence checked**

- That retained run happened to record zero parity differences, matching
  clone/source heads, 1212 test passes, correct HTTP statuses, and an admitted
  observed shape (`pwb-p4-5-fresh-checkout-demo-2026-09-04.json:21-39,
  105-142`). It is useful historical evidence for that pair of commits.
- The exact-head full suite passed 1219 tests in this review, and the live
  exact-head routes respond. Neither substitutes for a fresh clone at the
  exact two reviewed revisions or for the owner comprehension oracle.

**Minimum fix**

Make every recorded invariant that can falsify the demonstration part of its
exit predicate, including exact source/clone head, exact Butlers/model revision,
admitted expected shape, zero parity differences with multiplicity, unique IDs,
zero unexpected limit breaches, and clean daemon shutdown. Add a test around
the predicate with one counterexample per field, then retain a new exact-head
fresh-checkout run. Keep PWB-REQ-021 as a separate owner judgment; do not turn
HTTP 200 or parity into comprehension.

**Authority route:** implementation/test repair.

### HIGH 5 — Metadata-only baseline-spec identities are unnecessarily body-gated

**Supporting evidence checked**

- The signed grammar defines each `baseline-spec` identity solely from a Git
  tree path (`spec.md:47-48`), and phase A already enumerates those paths from
  exact tree metadata (`project-shape-manifest.ts:410-425`).
- Phase B nevertheless reads and classifies every baseline spec body before
  calling an extractor whose identity depends only on the path
  (`project-shape-model.ts:489-498`; `project-shape-extraction.ts:425-434`).
- Exact Butlers tree metadata contains 183 matching baseline spec paths. Live
  Polaris says `denominator Unknown (excluded-content); 76 modeled; 107
  source(s) unreadable`. The retained prior evidence records the same 76/107
  split (`pwb-p4-5-fresh-checkout-demo-2026-09-04.json:246-257`).

**Contradictory/mitigating evidence checked**

- The conservative current behavior never presents excluded body content and
  does not overclaim the 107 bodies as safe. That fail-closed behavior must be
  preserved for any claim that actually depends on body text.
- Roster identity is different: the signed grammar requires a non-empty
  `[butler].name`, so excluded `butler.toml` bodies cannot be repaired from path
  metadata alone.

**Why it matters**

The implementation performs 183 unnecessary body reads, expands attack and
resource surface, and turns a fully known Git-metadata catalog into a huge
Unknown denominator. This is a correctness and least-authority defect, not a
reason to weaken whole-artifact secret exclusion.

**Minimum fix**

Derive baseline-spec identities and denominator directly from the exact tree
manifest without opening their bodies. Keep source-body state separate: a body
may remain excluded while the path-defined baseline identity remains Observed.
Add a test where every baseline body contains an exclusion sentinel but the
tree-defined identity denominator is still exact and no body read occurs.

**Authority route:** implementation repair; no policy exception.

### MEDIUM 1 — Multiline list items are truncated, and real-corpus copy is not tested for comprehension

- `topLevelListItems` stores only the marker line and ignores indented
  continuations
  (`packages/three-surface-poc-core/src/project-shape-extraction.ts:175-200`).
  Principle, success, and catalog statements use that first line
  (`project-shape-extraction.ts:342-393`). Exact
  Butlers entries are routinely wrapped; for example the first V1 item spans
  two lines and Chronicler spans many (`about/heart-and-soul/v1.md:40-69` at
  the reviewed Butlers commit). Once Blocker 2 is fixed, Polaris will present
  sentence fragments as declarations.
- The fixtures put material statements on one line, so the two-extractor tests
  agree on the same reduced grammar. The copy oracle enforces roles and word
  bans but intentionally delegates comprehension to PWB-REQ-021. The live page
  is 1,069,549 bytes, carries 256 source rows and 389 claim tuples, and the
  owner aborted the cold open.

Fix by preserving the complete inert list-item text (including continuation
lines) and moving exhaustive catalogs/evidence behind genuine progressive
disclosure so the first read remains a concise project account. Add real-shaped
multiline fixtures and re-run the owner cold open after the blockers are fixed.
This is implementation work within existing presentation behavior; do not
summarize normative text where the spec requires verbatim bytes.

## Signed-spec / owner-act gate discovered during review

### GATE 1 — The judgment evaluator does not validate the retained nine-answer record

[Observed] PWB-REQ-021 requires the retained answer population and independent
owner comparison (`spec.md:805-837`). `parseRunRecord` parses only identity,
surface version, evaluation identity, mode, and traversed paths; it ignores the
`## Answers` section
(`packages/three-surface-poc-core/src/walkthrough-judgment.ts:273-389`). The
loader's “lawful” fixture contains one
placeholder answer and one `/polaris` path yet is accepted
(`apps/three-surface-poc/src/walkthrough-inputs.test.ts:25-47,178-191`). Path
validation requires only that every supplied path belongs to the allowlist, not
that a mandatory path population was traversed
(`walkthrough-judgment.ts:574-580`).

[Observed] Current behavior remains safe because no run record or judgment act
exists; the live criterion is Unknown-never-met. No implementation or test
result may substitute for the missing owner judgment.

Adding missing/malformed/wrong answer cases appears to expand PWB-REQ-022's
closed 84 present-invalid denominator (`spec.md:850-885`). Therefore the
implementation should not silently invent those cases. Route the mismatch
through CC-REV-2 and the owner if exact answer/path completeness is intended to
be mechanically admissibility-bearing. Independently, the owner may record the
already aborted experience as `not-met` through the existing ceremony; this
review does not fabricate that act.

### GATE 2 — Current exclusions remain binding

[Observed] The prior live record found 132 whole-artifact active-content
exclusions and one token-detector exclusion, and current Polaris still carries
large excluded populations. This review does **not** recommend relaxing active
content, secret detection, whole-artifact exclusion, or the content class.
Where comprehension needs a body the current acts do not cover, the lawful
result remains Unknown until a signed-spec/consent/policy/registry act changes
the boundary. Metadata-only derivations and safer progressive rendering should
be exhausted first.

## Test-rigor assessment

- [Observed] Net exact-head suite result in this review: 1219 passed, 2 live
  tests skipped. The skips are the pre-existing live work-item and live focused
  pytest tests, not the browser accessibility suite.
- [Observed] The strongest tests are the closed owner-act/judgment tables,
  exact-object read guard, independent parity extraction, and browser-driven
  focus/contrast checks. Their failure names are generally defect-localizing.
- [Observed] The principal weakness is fixture closure around production's own
  assumptions: fake five-pillar roots, injected-only contradictions, metadata
  rows treated as exact artifacts, and generic limit comparisons treated as
  enforcement. These are test-rigor rule 4/5 failures: the oracle repeats the
  implementation boundary instead of challenging it with the actual source
  contract.
- [Observed] There is no live project-shape test analogous to
  `work-items.live.test.ts`; the only real-source exercise is the manually run
  fresh-checkout command, whose success predicate omits its most important
  recorded results.
- [Inferred] A repair is not complete until each blocker has a regression that
  fails on `cd6c952`, the security cases have fail-then-restore mutation proof,
  and a fresh exact-head run against the supplied Butlers revision produces a
  usable project account before the owner is asked to judge it again.

## Required disposition before confirmation

1. Repair Blockers 1-4 and Highs 1-5 in the implementation plane only, except
   where the findings explicitly route to a signed-spec/owner gate.
2. Add real-source-shaped, independent counterexamples for locator binding,
   five-root discovery, unknown-pillar denominators, the eight-versus-nine
   contradiction, exact requirement reachability, phase-A secrets, lifecycle
   unreadability/tag-byte mismatch, every resource limit, and fresh-demo exit
   polarity.
3. Retain exact-head test, mutation, browser, fresh-checkout, loopback, and
   tailnet evidence. A passing response code remains transport evidence only.
4. Keep the walkthrough judgment Unknown until a lawful owner act exists. Ask
   for a new owner cold open only after the implementation is independently
   confirmed usable; do not reinterpret the aborted walkthrough as sign-off.

**VERDICT: REVISE**
