# Capability 1 runtime-hardening follow-ups — design

**Status:** Approved by the user for detailed implementation planning and
packet-complete Bead shaping on 2026-08-24. This approval does not release held
rows or replace any owner act required by the escalation conditions below.

**Baseline:** `main` at `0cbb8f9e0eabf7e89d023c2fe7f559465f77b2b0`; the
baseline default suite passed 53 files / 408 tests in an isolated worktree.

## Purpose and authority

[Observed] The owner’s 2026-08-21 authorization permits Capability 1
implementation, tests, developer tooling, and a bounded Beads backlog. The
adopted Capability 1 specification remains the behavioral authority. This
design is implementation guidance only; it neither amends the adopted
specification nor changes accepted contracts.

No further owner act is needed while the work remains within that authorization.
Any spec/contract amendment, security or retention posture change, normative
data-contract change, resource-envelope breach, or scope expansion returns to
the act's escalation path.

The work dispositions every item in `syzygy-ydr` and `syzygy-h84` after the
completed runtime epic. A disposition is not a claim that the item is
executable: only the packet-complete outcomes explicitly marked executable
below may become child Beads.

In this document, **executable** means eligible for implementation planning and
child-Bead shaping after this revised design is approved; it does not mean
currently dispatchable. Until approval, a detailed plan, and packet-complete
child Beads exist, no implementation child may be claimed or dispatched.

## Governing design decisions

1. **Snapshot before status.** Every deterministic input used by these phases
   is bound into the source-snapshot identity before it may affect a served
   claim. A caller-supplied timestamp-shaped label is not sufficient.
2. **Reference-bound consent.** De-duplicating record reads is an I/O
   optimization only. A repository is consented only through the exact consent
   reference on its declaration entry; another same-pair record may not
   substitute for a dangling, mismatched, or withdrawn entry reference.
3. **Multiset parity.** Equivalent channels compare order-insensitively over
   complete canonical facts while preserving multiplicity. Positional
   comparison is forbidden because presentation order may differ lawfully.
4. **One required evaluated projection.** Coverage, discoverability, authority,
   proposals, and ordinary facts are never optional route-local additions.
   Every plane is a required `ProjectEvaluation` field, carrying either its
   value or a named `unavailable` / `not-produced` arm, and both served channels
   consume only that projection.
5. **Executable rows and held rows are different states.** A synthetic core
   fixture does not make a runtime condition executable. Stale and
   observer-failed behavior remain required by the adopted specification, but
   no child is shaped until the runtime has an authorized currency/prior-record
   input that can produce them.
6. **Gate evidence is externally captured.** Worker-written transcripts are
   report facts, not merge-gate evidence. Exact-head CI or coordinator-captured
   artifacts own pass/fail claims.

## Scope and non-goals

The executable sequence has four phases:

0. Identified source snapshot and evaluation input.
1. Runtime admission, parity-oracle, state-directory, and tooling hardening.
2. Reference-bound consent and conditionally executable coverage truth.
3. Served discoverability facts.

The following remain explicitly held or out of scope:

- Any edit under `openspec/**` or `.syzygy/**`, including generated governance
  views and accepted contract artifacts.
- Rendering an unresolvable consent reference as reason #11. Accepted RFC3-6
  assigns that condition to reason #6; changing it needs the governed amendment
  path.
- Inventing persistence, retry, retention, or a last-good observation store to
  make the observer-failed row executable.
- Claiming CAP1-REQ-046 runtime completion until a separate authority-input
  design identifies the exact artifact and owner-act inputs the runtime may
  consume. Disclosed absence remains honest but does not satisfy the
  requirement. This does not waive the smaller RFC3-16(a) owner-act
  verification needed before a consent record may authorize observation.
- Inventing an authority-exposure source, proposal source, project-wide
  Markdown dialect, retention model, or persistent observation contract.
- Updating status pages to declare completion before the corresponding
  behavior and retained evidence exist.
- The governance-only portions of the remaining open queue.

## Source-Bead disposition ledger

| Source item | Disposition in this design |
|---|---|
| `syzygy-ydr` 1 — per-entry consent reference | Eligible in Phase 2 after Phase 0's consent-provenance gate, through reference-bound resolution and masking falsifiers. |
| `syzygy-ydr` 2 — whitespace admissibility | Executable in Phase 1 as transport test debt; the core stub is not widened. |
| `syzygy-ydr` 3 — consent/withdrawal provenance | Eligible in Phase 2 after Phase 0's consent-provenance gate, across coverage and both channels. |
| `syzygy-ydr` 4 — observer failure vs source unreachable | Required but held in Phase 2B until an authorized last-good input exists. |
| `syzygy-h84` 1 — discoverability and authority exposure | Discoverability is executable in Phase 3. Authority exposure remains held and is a prerequisite only to claiming CAP1-REQ-046 complete; it does not block the discoverability child. |
| `syzygy-h84` 2 — dangling state-directory symlink | Executable in Phase 1. The existing-target case is fixed; the dangling-target named-arm gap remains real. |
| `syzygy-h84` 3 — reason #11 for consent reference | Rejected as contract-incompatible; reason #6 is preserved. |
| `syzygy-h84` 4 — loader path convention | Executable as implementation documentation in Phase 2; never promoted to a normative conformance rule. |
| `syzygy-h84` 5 — substring entry-link detection | Executable in Phase 3 after parser/dependency admission is recorded. |
| `syzygy-h84` 6 — deprecated Vitest workspace | Executable as a focused Phase 1 tooling child. |
| `syzygy-h84` 7 — runtime module-resolution seam | Executable as a focused Phase 1 tooling child after its clean-test/build/runtime matrix is pinned. |
| `syzygy-h84` 8 — stale status/workflow text | Final truthful-status packet only, after the behavior packets and evidence land. |
| `syzygy-h84` 9 — proposal carriage | Held until evaluation produces real proposals; no empty implementation is claimed. |
| `syzygy-h84` 10 — parity Map collapse | Executable in Phase 1 as order-insensitive, multiplicity-preserving comparison. |

## Delivery topology

`syzygy-h84` remains the provenance record for the runtime follow-ups and
`syzygy-ydr` remains the provenance record for consent findings. Before code
starts, the coordinator shapes focused child Beads with complete dispatch
packets, explicit dependencies, requirement traces, and exact acceptance
tests; no worker receives either aggregate record unchanged.

The envelope permits two to three workstreams, but the phases are serialized
where they share `coverage.ts`, `pipeline.ts`, evaluation facts, channel DTOs,
or exact-head review surfaces. Each child has one accountable implementation
worker and an independent fresh-context exact-head reviewer. The tooling child
may run in parallel only while it touches no manifest or configuration file
owned by another active child.

Held outcomes remain on their aggregate provenance Bead. They are not marked
dependency-ready, not dispatched, and not counted as implemented.

Phase 3 depends on reviewed exact heads for Phase 0 and the Phase 1
parity-oracle child, and on executable Phase 2A reaching `main`. Other Phase 1
children block Phase 3 only when their packet owns an overlapping Phase 3 surface.
README hyperlink-extractor admission is an additional Phase 3 pre-dispatch
gate.

## Phase 0 — identified source snapshot and evaluation input

### Outcome

Every deterministic input capable of affecting the Phase 1–3 outputs is
captured once in an immutable `CapturedProjectInputs` value and named in one
canonical source-snapshot manifest. `EvaluationIdentity.snapshot` is the digest
of that captured manifest; `EvaluationIdentity.asOf` remains the separately
injected time coordinate. Evaluation and `/entry` consume only the captured
value, never a second filesystem read.

### Design

The manifest uses deterministic ordering and content/version identities for:

- every observed repository and its declared working-tree state;
- the declaration and every consent record or consent-load failure consumed;
- each consent artifact's exact digest and independently captured owner-act or
  audit correlation used to establish RFC3-16(a) provenance;
- root-README evidence consumed by discoverability;
- every governance artifact and owner-act record consumed by authority
  exposure, once that prerequisite is designed;
- observer, adapter, parser, kernel, and evaluation-engine versions;
- deterministic parsing/classification configuration; and
- any prior observation record admitted in a future authorized phase.

A source absent from the manifest cannot influence the evaluation. Missing
capture renders unavailable or `Unknown`; it is never read opportunistically
after the identity is minted. Computing the manifest is read-only and adds no
persistent store.

Capture order is explicit: capture the declaration; capture its referenced
consent artifacts and independently kept act/audit correlations; verify the
effective consent state; only then capture content from each admitted
repository. A well-formed but unverified consent record grants no repository
read. The entry document and README evidence are captured in the same immutable
input value rather than read when a route is requested.

The capture boundary detects a source changing during capture. It either
retries the whole capture as a new source snapshot or fails closed with a named
unavailable/`Unknown` result; it never hashes one set of bytes and evaluates or
serves another. A falsifier mutates or deletes a source after capture and before
evaluation and proves the captured evaluation remains internally consistent
and no post-capture read influences it.

Before Phase 0 is dispatchable, its packet names the versioned manifest schema,
canonical byte serialization, digest algorithm, path-normalization rules, and
representation of missing or failed-load inputs. Equivalent manifests produce
identical bytes before hashing; any semantic input change changes those bytes.

### Surface and evidence

Likely surfaces are the composition root, pipeline dependencies, evaluation
identity helpers, entry route dependency, and fixture builders. Required
falsifiers mutate each input class one at a time and prove the snapshot identity
changes; two runs over the same captured manifest and as-of instant must
produce byte-equivalent deterministic layers, including freshness. A separate
observation spy proves unverified or mismatched consent invokes no repository
capture. This phase traces to `CAP1-REQ-011`, `016`, `042`, `060`, and `062`,
and requires independent exact-head review as security,
deterministic-observation, and identity-floor work.

## Phase 1 — runtime admission, parity, state-directory, and tooling hardening

### Outcome

The real HTTP admission path has complete negative transport coverage; the
parity oracle preserves duplicate occurrences without coupling correctness to
presentation order; dangling and existing state-directory symlink targets are
classified before any write; and the test/runtime module seams no longer rely
on deprecated or implicit behavior.

### Focused child outcomes

1. **Credential transport regression proof.** Through a real HTTP route, prove
   that missing, empty-Bearer, non-Bearer, whitespace-token, malformed, and
   wrong-token requests all return status 401, JSON content, and the exact bytes
   `{"admitted":false,"served":"nothing"}`; they do not invoke the handler
   and serve no facts. A correct token is the positive control.
   Malformed headers may be rejected before equality comparison; only a
   syntactically presented token exercises the constant-time equality path.
   Constant-time use is a structural review property, not something inferred
   from a 401 response.
2. **Parity oracle hardening.** Replace name-keyed comparison with an
   order-insensitive multiset comparison over the complete canonical fact
   tuple, preserving duplicate multiplicity. A lawful permutation passes; an
   equal-count duplicate-name fixture with one differing occurrence fails; a
   multiplicity difference fails. The oracle canonical-encodes every semantic
   field, excluding only presentation order and channel formatting, counts each
   encoded tuple, and compares occurrence counts bidirectionally. Fact name and
   repository identity are compared fields, never uniqueness keys that can
   overwrite an occurrence.
3. **Dangling state-directory symlink classification.** Resolve every existing
   symlink component, including a final dangling link whose target path does
   not yet exist, before directory creation. A target under `openspec/**` or
   `.syzygy/**` returns the existing governed-plane `invalid` arm, exits
   nonzero, opens no listener, and writes nothing. A dangling link to a benign
   nonexistent path outside the governed plane remains
   `credential-unprovisionable`, exits 1, opens no listener, and writes
   nothing; it is not misreported as an in-plane target.
4. **Vitest configuration migration.** Replace `vitest.workspace.ts` with the
   supported root `test.projects` configuration without changing which tests
   belong to the default versus process/system gates. The deprecation warning
   must disappear from a clean run.
5. **Workspace package runtime seam.** Replace or justify the composition-root
   `registerHooks` mapping only after a matrix proves: TypeScript source tests
   run from a clean checkout without a prebuild; built Node execution resolves
   compiled package entries; declarations resolve for typecheck; and the
   fresh-clone system test still runs the compiled app. Conditional exports are
   preferred only if that full matrix passes; no manifest is changed merely to
   remove unusual-looking code.

### Surface and evidence

Likely surfaces include `credentials.*`, `server.*`,
`packages/cap1-system/src/credentials.system.test.ts`, `parity.*`, the CLI
composition root and state-directory system test, root Vitest configuration,
workspace package manifests, and the fresh-clone test. Credential test debt
uses a controlled mutation to prove the added transport cases detect weakened
admission; it does not require a needless production change merely to make the
already-correct baseline red.

The admission child owns the transport limb of `CAP1-REQ-015`; parity owns
`CAP1-REQ-041`, `043`, and `045`; snapshot identity remains Phase 0's. Every
child receives the applicable mandatory review class in its packet: security,
public interface, deterministic observation, or build/runtime interface.

## Phase 2 — reference-bound consent and coverage truth

### Outcome

Every declared repository is resolved through its exact consent reference;
coverage results preserve the consent or withdrawal provenance needed to
explain every executable result; and the human and machine channels expose the
same canonical coverage rows.

### Phase 2A — executable design

Phase 2A becomes executable only after Phase 0 provides independently verified
consent-artifact provenance and a pre-observation authorization result. If that
correlation input cannot be identified without inventing a new normative data
contract, Phase 2A remains held and returns to the authorization act's
escalation path.

1. Form the de-duplicated read set from both the declaration’s top-level
   consent references and each repository entry’s consent reference. Preserve
   a reference-keyed load result; de-duplication changes I/O count only.
2. For entry reference `R`, the load result stored under `R` must contain a
   record whose internal record ID equals `R`, whose subject equals the declared
   project/repository pair, and whose exact digest has independently verified
   RFC3-16(a) owner-act provenance. No grant loaded under another reference and
   no self-declared but unverified record may substitute.
3. Consent precedence is closed:
   - an unloadable, identity-mismatched, subject-mismatched, or unverified exact
     entry reference remains the primary unconsented basis; other records may
     neither replace nor reclassify it;
   - a verified exact withdrawn entry is unconsented with that withdrawal as
     its visible basis; and
   - a verified exact in-force entry is defeated by any verified applicable
     withdrawal in the reference-keyed union read set, whose identity becomes
     the visible withdrawal basis, regardless of record order.
4. Repository capture occurs only after that consent decision. No
   `observeRepositorySnapshot`, README read, or other repository-content I/O is
   invoked for an unconsented result. The declaration/governance inputs needed
   to make the authorization decision are the only earlier reads.
5. Carry the resolved consent or withdrawal record identity through every
   consented or withdrawn coverage result rather than retaining only an
   abstract basis. Executable `observed` and `capture-failed` results cite the
   exact in-force record; withdrawn results cite the defeating withdrawal. The
   held `stale` result must retain that citation when later made executable. No
   runtime partial result is introduced by this design; any such result needs
   an explicit input condition and matrix row in a later design. A missing or
   mismatched reference carries the declared reference and named load or
   subject-mismatch fact, never a fabricated record citation.
6. Serialize one canonical per-repository coverage row from the evaluated
   projection. Both channels consume it. The independent wire oracle parses
   JSON and HTML separately and compares repository-keyed multisets
   bidirectionally; an omitted, extra, or duplicate row is a defect.
7. Document the current `<decisionsDir>/<reference>.yaml` loader convention as
   implementation documentation only; it does not become a normative
   conformance rule.

The executable matrix is:

| Input condition | Coverage result | Required provenance and rendered outcome |
|---|---|---|
| Exact in-force entry reference and captured repository | `observed` | Exact record ID, scope, attribution, and `in-force` state appear in the coverage row and both channels. |
| Missing, malformed, mismatched, or unresolvable entry reference | `unconsented`, reason #6 | Repository and declared reference remain visible; no alternative same-pair record can mask the failure; never reason #11. |
| Withdrawal applicable to the declared pair | `unconsented`, reason #6 | Withdrawal defeats grants in either record order; the withdrawal record is visible as the consent basis in both channels. |
| Exact in-force consent and source unreadable at the snapshot | `capture-failed`, reason #10 | The coverage row preserves the in-force consent citation while rendering source-unreachable as `Unknown`. |

Required masking fixtures include:

- an entry-only in-force reference absent from top-level `consents[]`;
- the same reference present in both locations, loaded once but producing one
  coverage row per declared repository;
- a dangling entry reference plus another in-force same-pair top-level record,
  which must remain unconsented;
- an exact reference whose record names the wrong pair, also unconsented;
- an unverified exact record that invokes no repository observation;
- invalid exact entry plus a verified same-pair withdrawal, which retains the
  invalid-entry primary basis;
- verified exact in-force entry plus withdrawal in both record orders, which
  renders the withdrawal basis; and
- verified exact withdrawn entry plus an alternate grant, which remains
  withdrawn.

### Phase 2B — required but held runtime rows

Two accepted behaviors have no executable runtime input on the baseline:

| Required condition | Missing prerequisite | Disposition |
|---|---|---|
| Evidence stale at the evaluation as-of instant | An authorized currency-bound and evidence-age input at the observation boundary | No child Bead; a core-only `stale` fixture is not runtime evidence. |
| Observer/adapter failure with degrade-to-last-good | A typed observer-failure outcome plus an identified prior observation record already admitted to the source snapshot | No child Bead; do not invent persistence, retry, storage, or retention semantics. |

Planning must not hide these rows inside Phase 2A. If an existing authorized
input is later identified, a separate design records the adapter classification
table, last-good selection rule, snapshot membership, and runtime/system
falsifiers. If that design changes retention or a normative data contract, it
returns to the owner-act escalation path.

### Surface and evidence

Phase 2A is serialized across declaration, consent, coverage, loader, pipeline,
evaluation projection, and both routes. It has requirement tests for
`CAP1-REQ-010`–`016`, targeted daemon tests, independent dual-channel row
parsers, and a real-filesystem/system fixture. It owns the executable coverage
limbs of `CAP1-REQ-015`; Phase 1 owns credential admission. It requires
independent exact-head review for security, deterministic-observation, and
public-interface classes.

## Phase 3 — served discoverability facts

### Outcome

One discoverability finding per declared repository becomes a required part of
the same evaluated projection that supplies the shape answers. Machine and
human channels expose identical repository-keyed findings with evidence,
epistemic state, basis, and proposal state intact when one exists; the absence
of proposals remains an explicit empty plane, never an omitted field.

### Design

1. Apply conditions in this order: applicability from declared repository role;
   consent; repository-root availability; then README capture and link parsing.
   A repository with no governance root is `not-applicable` before any README
   read. A governance-root repository without consent is `Unknown` reason #6
   and is not read. Missing or unreadable README evidence is `Unknown` reason
   #10.
2. A raw substring never establishes a link. The adapter asks the semantic
   question the specification owns: does the rendered README contain a
   navigable hyperlink whose resolved target is the fixed entry? It is not
   defined by one AST node type or URL spelling. Inline, reference-style, and
   autolink Markdown forms and raw-HTML anchors supported by the selected
   deterministic reader count when they resolve to the fixed entry. Plain text,
   inline/fenced code, comments, image destinations, and genuinely different
   targets do not.
3. Relative destinations resolve against the root README's repository context.
   Query and fragment components do not disqualify a hyperlink whose resolved
   repository path is the fixed entry. Absolute destinations count only when
   captured repository-locator inputs resolve them deterministically to the
   same repository and entry path. If a rendered hyperlink's target cannot be
   classified from lawful snapshot inputs, Phase 3 remains held rather than
   serving an evidence-backed `no` from an arbitrary syntax subset.
4. The selected deterministic README hyperlink extractor is local to the
   discoverability observation adapter; it does not establish a project-wide
   canonical Markdown dialect. Before the Phase 3 child is dispatchable, its
   packet records the exact parser/renderer behavior, dependency rent decision,
   exact pins, transitive/security review, options, snapshot version identity,
   and a normalization table. The table covers relative and absolute forms,
   raw HTML, percent encoding, slash and backslash handling, repeated
   separators, case, `.`/`..`, queries, and fragments. Every row states
   count/ignore/hold and has a falsifier. No generic parser abstraction is added
   without a second real consumer.
5. Add discoverability as a required typed field on the evaluated-project arm.
   Add required authority and proposal fields at the same boundary, using named
   `unavailable` / `not-produced` arms until lawful values exist. Remove the
   optional human-only injection paths and the machine route's local empty
   proposal constant. Both routes serialize the same source projection, and the
   disclosure oracle compares a canonical repository-keyed multiset including
   value, epistemic label/reason, basis, evidence identity, and proposal state.
   It counts canonical row tuples; it never stores one row keyed only by
   repository ID.
6. Serve one `Why this answer?` explanation fact set for every discoverability
   finding, including its evidence or Unknown reason, consent boundary,
   evaluation identity, and applicable authority classes already supported by
   the evaluated projection.
7. Preserve current explicit absence for authority exposure and proposals as
   the projection's named arms, but do not claim CAP1-REQ-046 or proposal
   carriage satisfied. Full authority exposure needs its own input design;
   proposal carriage becomes executable only after evaluation produces real
   proposals.

The behavior matrix includes:

| Declared condition | Result |
|---|---|
| Governance root, consented, captured README with a qualifying link | `yes` with captured evidence |
| Governance root, consented, captured README without a qualifying link | `no` with captured evidence |
| Governance root, consented, missing/unreadable README | `Unknown`, reason #10 |
| Governance root, unconsented | `Unknown`, reason #6; README not read |
| Repository with no governance root | `not-applicable` with declared basis; README not read |

Extractor falsifiers cover inline, reference-style, autolink, and raw-HTML
hyperlinks; reordered reference definitions; plain-text mentions;
inline/fenced code; HTML comments; images; relative and absolute destinations;
path normalization; query/fragment variants; and near-match targets. They must
not encode a closed syntax subset the adopted specification never names.
Route/system falsifiers remove or add one repository row in one channel and
require the bidirectional oracle to fail.

### Surface and evidence

Likely surfaces are observation, pipeline, evaluated projection, fact model,
human route, machine route, distinction extraction, and parity/conformance
tests for `CAP1-REQ-040`, `041`, `050`–`053`, and `064`. Phase 3 no longer
claims `CAP1-REQ-046`. It requires independent exact-head review because it
changes deterministic observation and both public serving contracts, regardless
of whether implementation introduces a new trust boundary.

## Review, verification, and closeout

Every executable child packet names:

- the exact requirement limbs and review classes it owns;
- the focused test files and exact test names used during iteration;
- each new test's tier (`unit`, `component`, or `system`), unique regression,
  nearest existing test extended, and net suite delta;
- the controlled mutation that proves each new falsifier catches its target;
- the full gates: `npm run typecheck`, `npm test`, and
  `npm run test:system`; package/manifest changes additionally run the gated
  fresh-clone system test with `SYZYGY_FRESH_CLONE=1`;
- the denominator for every parity, repository, write, or absence sweep; and
- the exact-head evidence artifact: commit SHA, commands, counts, skipped tests,
  denominators, and full output captured by hosted CI or the coordinator.

The default `npm test` gate currently contains pure conformance tests and
real-socket daemon component tests; packets label those tiers honestly rather
than calling the whole gate “unit.” Focused iteration uses explicit test-file
paths until the Vitest `test.projects` migration establishes supported named
project commands. The system gate remains process/filesystem/HTTP reality.

All executable phases require independent fresh-context exact-head review:
Phase 0 touches deterministic identity; Phase 1 touches authentication, parity,
write containment, and build/runtime interfaces; Phase 2 touches consent and
public coverage; Phase 3 touches deterministic observation and both public
channels. Reviewer prompts receive the artifact, governing references, and
acceptance criteria, never the author's desired verdict. Workers declare tested
bytes FROZEN; the coordinator re-verifies staged bytes before commit or merge.
A Bead closes only after its reviewed exact head reaches `main`.

After all executable behavior packets land, a final truthful-status packet may
update `PROJECT-STATUS.md` and the hosted-workflow description using fresh
evidence. Its held-work list is cross-checked against the disposition ledger
and includes the CAP1-REQ-013 stale/observer-failure limbs, CAP1-REQ-062
currency/staleness limb, CAP1-REQ-046 authority-input limb, and proposal
carriage. It may not convert disclosed absence into completion. Root-only
selftest-fixture hygiene from `syzygy-e84` remains a separate maintenance
design, and its governed-plane portion remains held.

## Approval checkpoint

The conversation approved the original direction; this revised written record
requires the user's review. After approval, the next step is a detailed
implementation plan and packet-complete Bead shaping for executable outcomes
only under the existing 2026-08-21 authorization. Held rows remain open on
their provenance records and receive no lifecycle mutation.

No implementation or Beads lifecycle mutation is authorized by this document
alone.
