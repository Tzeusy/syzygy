> **Candidate — binds nothing.** This file proposes exact contract and PWB
> semantics. It does not edit accepted RFCs, alter signed PWB bytes, approve
> the three gate artifacts, authorize implementation or permit a Butlers body
> read.

# Semantic delta PWB-TRUST-1 — trust owner bootstrap acts for read-only observation

**Artifacts:** `.syzygy/governance/contracts/rfcs/RFC-0003/governance-homes-and-owner-acts.md`; `.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md`; `.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md`; `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`

**Stable IDs affected:** `RFC3-16(a)`, `RFC3-16(c)`, `RFC4-7`, `RFC5-16`, `PWB-REQ-001`, `PWB-REQ-005`, `PWB-REQ-006`; no ID is added, retired or renumbered

**Change class:** Normative — uncorrelated state-(1) acts become sufficient for one read-only effect class

**Author:** OpenAI Codex, drafting only

**Date:** 2026-08-31

**Baseline:** commit `3f5853004dad849815ea7a76909b24fddaef9632`

## Current meaning

### RFC3-16(a) and RFC3-16(c)

RFC3-16(a) currently states:

> **The predicate.** Such an artifact is honored **only when its owner-act
> provenance is independently verifiable to Syzygy by a mechanism the governed
> tree cannot forge**. Being present, well-formed, and correctly attributed *in
> the tree* is not sufficient.

Its failure rule currently states:

> **Effect when the predicate fails.** An authorization present in the tree
> without verifiable owner-act provenance is **never silently honored and never
> silently deleted**. Its **dependent effect is blocked** — the egress is
> refused, the run does not launch, the adapter write does not proceed, the
> adoption does not bind, the policy does not widen anything — the
> **authorization itself renders Unknown**, and the condition **mints a
> contradiction routed to owner adjudication**.

RFC3-16(c)'s final consequence currently states:

> - Nothing here weakens RFC3-16(a): an authorization-bearing artifact resting
>   on a state-(1) record has not satisfied the predicate, and RFC3-16(a)'s
>   *Effect when the predicate fails* governs its dependent effects.

Therefore every authorization-for-effect blocks when its act is state (1),
including read-only observation consent, its secret policy and its registry
entry.

### RFC4-7

RFC4-7 currently ends:

> An entry whose owner-act provenance does not verify admits nothing: outputs
> attributed to it render Unknown exactly as if the adapter were unregistered.

Therefore an owner-adopted but uncorrelated read-only observer emits no
admissible deterministic fact.

### RFC5-16

RFC5-16 currently ends:

> An unverifiable policy does not fail open: the ingest is blocked on
> RFC3-16(a)'s effect rule, never performed under the unverified policy.

Therefore an owner-adopted but uncorrelated secret policy blocks all ingest.

### PWB-REQ-005

PWB-REQ-005 currently requires all three acts to have verifiable provenance,
tests absent/mismatched/stale/unverifiable/valid triples, says only the
all-valid triple permits reads, and falsifies any read before all three
provenances verify.

## Proposed meaning

### RFC3-16(a) — independent verification is preferred, with one closed trust mode

Replace the first sentence of **The predicate** with:

> Except for the trusted-bootstrap read-only repository-observation rule
> defined in RFC3-16(c), such an artifact is honored only when its owner-act
> provenance is independently verifiable to Syzygy by a mechanism the governed
> tree cannot forge.

Replace the authorization half of **Bootstrap correlation** with:

> Rendering is the only effect this paragraph adds; what a state-(1) record
> suffices for splits by role (RFC3-16(c)): an artifact consumed as a constraint
> binds at full strength — refusing to apply a constraint over uncorrelated
> provenance would widen, not narrow — while an artifact consumed as an
> authorization for an effect has not satisfied the RFC3-16(a) predicate on a
> state-(1) record alone. The sole exception is RFC3-16(c)'s trusted-bootstrap
> read-only repository-observation rule. That rule may unblock only its exact
> observation effect; every other dependent effect remains governed by
> *Effect when the predicate fails* until correlation.

Replace **Effect when the predicate fails** with:

> **Effect when the predicate fails.** Except where RFC3-16(c)'s
> trusted-bootstrap read-only repository-observation rule applies, an
> authorization present in the tree without verifiable owner-act provenance is
> never silently honored and never silently deleted. Its dependent effect is
> blocked — the egress is refused, the run does not launch, the adapter write
> does not proceed, the adoption does not bind, the policy does not widen
> anything — the authorization itself renders Unknown, and the condition mints
> a contradiction routed to owner adjudication. Under the trusted-bootstrap
> rule, absence of independent correlation alone does not block the exact
> read-only observation effect, render its authorization Unknown, or mint that
> contradiction: the authorization instead renders as
> `owner-adopted (bootstrap, uncorrelated)` with the trusted basis disclosed.
> Absence, digest or scope mismatch, revocation, expiry where declared, or any
> requested effect outside that rule follows the normal
> blocked/Unknown/contradiction posture. Blocking is not deletion: the artifact
> and its provenance state remain rendered.

The non-exhaustive gate list remains, with a note that RFC4-7 and RFC5-16 use
this closed observation mode only where their amended clauses say so.

### RFC3-16(c) — preserve two states and allow one state-(1) effect class

After state (2), before **Consequences that bind**, insert:

> **Trusted-bootstrap read-only repository observation.** State (1) remains
> uncorrelated and does not satisfy independent verification. It may
> nevertheless be trusted for one dependent effect only: read-only observation
> of repository content within the exact project, repository, content-class and
> adapter scope bound by the owner act.
>
> Eligibility requires every authorization-bearing input consumed by the
> observation — including observation consent, secret-detection policy and
> adapter-registry entry — to have a current state-(1) or state-(2) owner act
> over its exact content digest. Each state-(1) act binds RFC3-16(b) items 1–8;
> item 9 is absent and that absence is disclosed. A mixed set selects the
> trusted-bootstrap mode whenever at least one required act remains state (1).
> Missing, mismatched, stale, superseded or revoked authority selects neither
> mode.
>
> This is an authorization mode, not a third provenance state. Human and
> machine views disclose, at project-account and per-claim provenance level,
> `owner-adopted (bootstrap, uncorrelated); trusted for read-only repository
> observation; not independently verified`. They never call the act, artifact,
> observation or resulting fact independently verified.
>
> The allowance authorizes no write to an observed repository or external
> authority; no RFC5-15 egress or model-provider disclosure; no observed-code
> execution or execution consent; no credential, credential-API or
> process-environment access; no deployment, release, certificate, conformance
> or positive security claim; and no autonomous owner act, mission effect or
> multi-user authority. Those effects remain subject to the ordinary
> RFC3-16(a) failure rule until A1 correlation exists. SEC-5 remains
> outcome-binding under either provenance state.

Replace RFC3-16(c)'s final non-derogation bullet with:

> - Nothing here otherwise weakens RFC3-16(a): outside the trusted-bootstrap
>   read-only repository-observation rule, an authorization-bearing artifact
>   resting on a state-(1) record has not satisfied the predicate and
>   RFC3-16(a)'s *Effect when the predicate fails* governs every dependent
>   effect. The constraint half of the split remains unchanged.

### RFC4-7 — admit only exact read-only entries under trust mode

Replace RFC4-7's final two sentences with:

> An entry is honored only under RFC3-16(a). Ordinarily, an entry whose
> owner-act provenance does not independently verify admits nothing and its
> outputs render Unknown exactly as if the adapter were unregistered. Under
> RFC3-16(c)'s trusted-bootstrap rule only, an exact digest-bound state-(1)
> entry may admit deterministic facts solely within its recorded read-only
> repository-observation scope. The entry must declare an empty
> observed-repository and external-authority write surface, no egress, no
> credential or process-environment access, and no observed-code execution.
> Every admitted fact and evaluation carries the entry identity, digest,
> provenance state and selected authorization mode.
>
> Where the complete source manifest is itself derived through observation,
> the entry declares one deterministic transaction at one exact repository
> revision: phase A may read only the fixed bootstrap seed set and Git-tree
> metadata declared by the governing behavior contract, under the same secret
> policy; it produces a revision-bound manifest and digest. Phase B may read
> only exact Git objects selected by that manifest from the same object database
> and revision. No alternate locator, working tree, symlink, submodule,
> traversal, environment value, remote fetch or runtime default may widen
> either phase. Missing, changed, revoked or out-of-scope entry state follows
> the ordinary no-admission rule.

### RFC5-16 — apply an exact state-(1) policy without weakening SEC-5

Replace RFC5-16's provenance ending with:

> The policy version and content digest are snapshot inputs, so what was
> screened is part of every evaluation's identity, and the policy is honored
> only under RFC3-16(a). Ordinarily, an uncorrelated policy blocks ingest. Under
> RFC3-16(c)'s trusted-bootstrap rule only, an exact digest-bound state-(1)
> policy may govern its exact read-only repository-observation scope. It screens
> transient bytes before parsing in both bootstrap-discovery and
> manifest-capture phases; matching or unclassifiable content is excluded and
> never enters a model, cache, log, surface, endpoint or record. Missing,
> changed, revoked or out-of-scope policy state blocks ingest.
>
> Trusting the policy's state-(1) owner act changes only the provenance gate. It
> weakens none of this clause's matching, classification, exclusion,
> hash-not-body provenance or all-sink obligations. A secret appearing in any
> Syzygy sink remains an SEC-5 trust-floor violation.

RFC5-17 remains unchanged.

### PWB-REQ-005 — replace the complete requirement block

Keep the title, group, form and stable ID. Replace the normative body, test
contract, scenarios and warrants with:

> The POC SHALL perform zero Butlers project-shape body reads until it resolves
> an exact observation-consent record, secret-classification policy and
> registered project-shape adapter entry for the same
> `(project:syzygy, repository:butlers-configured-poc)` subject.
>
> Each artifact SHALL have a current, attributable owner act bound to its exact
> digest. The authorization mode SHALL be `independently-verified` when all
> three acts correlate through A1. Otherwise it SHALL be
> `owner-trusted-bootstrap` only when every artifact has an exact digest-bound
> owner act, at least one act remains uncorrelated, and the amended PWB behavior
> signed under `TRUSTED-BOOTSTRAP-OBSERVATION-DIR-2026-08-31` permits that
> mode. No other combination authorizes a read. Lack of independent correlation
> alone SHALL NOT block the trusted mode and SHALL NOT be represented as
> independent verification.
>
> The consent record SHALL live in Syzygy's decisions plane and name the
> observation class, exact subject, declared-project-shape content scope,
> principal, grant instant and revocation state. The governing policy SHALL be
> the observing Syzygy project's exact policy and SHALL apply before every
> ingest, parse, store, log, surface, endpoint and record boundary. The registry
> entry SHALL live in Syzygy's governance plane, name the same subject and
> declare read-only Git authority with empty write, database, network,
> credential, process-environment and observed-code-execution surfaces. The
> observer SHALL NOT write, migrate or repair the observed repository or its
> governance plane.
>
> Every artifact identity, version and digest; owner-act identity and provenance
> state; A1 correlation identity or its explicit absence; authorization mode;
> accepted RFC3/RFC4/RFC5 trust-rule module digests and their superseding owner
> act identities; signed PWB source-grammar digest and superseding sign-off act;
> source-discovery algorithm and version;
> opaque repository identity; approved locator mapping; exact Git revision; and
> permitted Git object database SHALL be deterministic evaluation inputs.
> Missing, mismatched, stale, revoked, unattributed, wrong-subject, wrong-scope
> or effect-widening authority SHALL produce zero body reads and a project-model
> Unknown.
>
> When `owner-trusted-bootstrap` is active, Polaris SHALL show the persistent
> project-account notice “Observation uses owner-trusted records; independent
> audit is not configured.” Each affected claim SHALL expose the same basis on
> demand, and `/api/poc` SHALL carry the authorization mode, act identities,
> artifact digests and uncorrelated provenance state on every admitted
> project-shape fact. Neither channel may label that basis verified or infer a
> positive security, conformance, release or certification claim from it.
>
> After authority admission, discovery SHALL run within one identified
> evaluation at one exact Git revision in two phases. Phase A SHALL read only
> the exact Git object for the Butlers path “about/README.md”, then only the
> README index under each of the five normalized pillar roots that index
> declares, plus Git-tree metadata needed to enumerate baseline
> `openspec/specs/*/spec.md` paths and top-level `roster/*/butler.toml` and
> corresponding `MANIFESTO.md` candidates. Narrative links SHALL NOT recurse.
> The secret policy SHALL screen each transient body before parsing; raw bodies
> SHALL never be stored, logged, rendered or returned.
>
> Phase A SHALL emit a revision-bound manifest containing normalized
> repository-relative paths, Git object identities, extraction classes, the
> source-discovery version and a manifest digest. The manifest is derived
> evaluation data, not a separate authorization artifact: the owner acts bind
> the signed grammar and discovery algorithm, while the manifest digest becomes
> an evaluation input after derivation. Phase B SHALL begin only after an
> independent validator confirms that the manifest exactly satisfies the signed
> PWB grammar at the same repository identity, revision and object database.
> Phase B SHALL read only exact Git objects named by that manifest. A Phase-A
> parse, containment, limit or manifest-validation failure SHALL produce zero
> Phase-B body reads and a project-model Unknown; it does not erase already
> admitted Phase-A read calls. PWB-REQ-006 applies to both phases.
>
> Revocation or supersession SHALL stop new reads at the next evaluation. Prior
> observation records remain immutable and visibly withdrawn or stale. No later
> act retroactively authorizes an earlier read.
>
> - **Case (counterexample sweep)**: for each artifact and act, exercise absent,
>   mismatched, stale, revoked, unattributed, wrong-subject, wrong-scope and
>   digest-mismatch cases; exercise valid all-A1, all-uncorrelated and mixed
>   A1/uncorrelated tuples; exercise every non-empty authority surface; then,
>   for each valid mode, exercise Phase-A seed widening, recursive-link
>   widening, malformed discovery output, manifest/revision/object-database
>   mismatch and Phase-B path widening with separate injected phase read spies.
> - **Observable**: every invalid authority tuple yields zero Phase-A and Phase-B
>   body calls and a fixed Unknown reason; both valid modes permit only the
>   exact Phase-A seed set and validated Phase-B manifest; a Phase-A or manifest
>   failure yields zero Phase-B calls; trusted mode is identical across human
>   and machine views and is never rendered as verified.
> - **Oracle**: independently compare artifact bytes and digests, act fields,
>   subjects, scopes, lifecycle states, A1 correlations, adapter authority and
>   mode derivation. Derive the expected Phase-A set from the literal signed
>   grammar and controlled Git tree, derive the expected manifest with an
>   independent extractor, and compare both phase spies, evaluation inputs and
>   every human/machine provenance marker. Exact equality, zero out-of-set reads
>   and the phase-specific zero-read rules decide.
> - **Oracle independence**: authority fixtures, literal authorization-mode
>   vocabulary, expected discovery algorithm, independent manifest extractor,
>   controlled Git tree and both read spies live outside the observer,
>   production parser and renderers.
> - **Falsifier**: any body read under invalid authority; incorrect mode
>   selection; a missing deterministic input; a trusted basis hidden or called
>   verified; a Phase-A read outside the closed seed algorithm; a Phase-B read
>   before manifest validation or outside the manifest; cross-revision,
>   alternate-locator or alternate-object-database substitution; raw-body
>   persistence; or admission of any non-read authority.
>
> #### Scenario: Owner-trusted bootstrap acts permit read-only observation
>
> - **WHEN** every matching consent, policy and empty-authority registry artifact
>   has a current exact digest-bound owner act and at least one act remains
>   uncorrelated
> - **THEN** the two-phase observation may run in `owner-trusted-bootstrap` mode
>   at one exact Git revision
> - **AND** Polaris and `/api/poc` disclose the owner-trusted, uncorrelated basis
>   without calling it verified
>
> #### Scenario: A1-correlated acts render independently verified
>
> - **WHEN** all three matching owner acts correlate through A1
> - **THEN** the same bounded observation may run in independently-verified mode
> - **AND** the trusted-bootstrap notice is absent
>
> #### Scenario: Invalid authority blocks before discovery
>
> - **WHEN** any required artifact or act is absent, mismatched, stale, revoked,
>   unattributed, wrong-subject, wrong-scope or effect-widening
> - **THEN** both discovery phases perform zero body reads
> - **AND** the project model reports Unknown with the exact failed gate and
>   resolution route
>
> #### Scenario: Discovery failure blocks manifest reads
>
> - **WHEN** valid authority admits Phase A but its seed parsing or derived
>   manifest fails the signed grammar, containment, revision or limit checks
> - **THEN** Phase B performs zero body reads
> - **AND** the project model reports Unknown without claiming a complete source
>   population
>
> ```yaml
> warrants:
>   primary: SEC-5
>   doctrine: [VIS-1, VIS-2, VIS-4, VIS-7, SEC-2, SEC-3, SEC-5]
>   contracts: [RFC1-3, RFC2-1, RFC2-23, RFC3-7, RFC3-8, RFC3-16, "RFC3-16(a)", "RFC3-16(c)", RFC3-30, RFC4-3, RFC4-7, RFC4-11, RFC5-12, RFC5-13, RFC5-16, RFC5-17, RFC5-19, RFC6-13, RFC6-22, RFC7-33]
>   policies: [CC-BAR-5, CC-SEC-5, CC-SEC-6, CC-TEST-6]
>   decisions: [POLARIS-DIR-2026-08-31, TRUSTED-BOOTSTRAP-OBSERVATION-DIR-2026-08-31]
>   topology: []
>   parent_requirements: []
> ```

### PWB-REQ-001 — replace the complete requirement block

Keep its title, group, form and stable ID. Replace the body, test contract and
scenario with:

> WHEN the POC observes Butlers, it SHALL bind the complete source-path
> population to one opaque repository identity, approved locator mapping,
> resolved Git object database and exact Git revision. It SHALL bind the signed
> PWB source-grammar digest and superseding sign-off act; accepted RFC3/RFC4/
> RFC5 trust-rule module digests and superseding owner-act identities;
> authorization mode; consent, policy and registry
> artifact/act identities, versions, digests and provenance states;
> source-discovery algorithm/version; resource limits; observer/parser version;
> and the Phase-A-derived manifest digest as deterministic evaluation inputs.
>
> Human and machine readers SHALL receive those identities, the capture instant
> and the same source population. Every emitted project-shape fact SHALL carry
> its source identity, scope, capture instant, observer identity/version,
> authorization mode and act basis. The manifest digest becomes an evaluation
> input only after Phase A derives and independently validates it; no ambient or
> prior manifest may substitute.
>
> - **Case**: observe a controlled repository at one known revision through
>   both authorization modes, including an alternate locator/object database,
>   a source-claimed instant distinct from capture, and a mutated Phase-A
>   manifest.
> - **Observable**: Polaris and `/api/poc` expose identical repository,
>   revision, source paths/count, capture instant, authorization inputs,
>   discovery identity and validated manifest digest; substitutions and invalid
>   manifests never enter Phase B.
> - **Oracle**: compare repository identity, approved locator, object database,
>   revision and Phase-A/Phase-B paths to an independent controlled Git tree;
>   independently derive and digest the manifest from the literal signed
>   grammar; exhaust every emitted fact's source, scope, capture, observer and
>   authorization stamps. Exact set, digest, stamp and input equality decides.
> - **Oracle independence**: the Git tree, source population, manifest
>   extractor, digester and expected input tuple live outside the POC model,
>   observer, parser and renderers.
> - **Falsifier**: one source is absent or arbitrary, one deterministic input is
>   missing, the two channels differ, Phase B uses an unvalidated manifest, or
>   any source crosses locator, object-database or revision boundaries.
>
> #### Scenario: Source population is complete at one revision
>
> - **WHEN** Butlers is observed at revision R through a valid authorization
>   mode and validated Phase-A manifest
> - **THEN** every admitted project-shape source resolves from the approved
>   object database at R
> - **AND** human and machine views expose the same complete source set,
>   manifest digest and authorization basis

Keep the existing warrant block and add
`TRUSTED-BOOTSTRAP-OBSERVATION-DIR-2026-08-31` to `decisions`.

### PWB-REQ-006 — replace the complete requirement block

Keep its title, group, form and stable ID. Replace the body, test contract and
scenarios with:

> Both discovery phases SHALL read only exact Git objects addressed by
> normalized repository-relative paths within the consented opaque repository,
> approved locator, resolved object database and one exact revision. Phase A
> SHALL stay inside PWB-REQ-005's closed seed algorithm; Phase B SHALL start only
> after independent manifest validation and stay inside that manifest.
>
> Neither phase SHALL follow absolute paths, traversal, NUL-bearing paths,
> working-tree files, symlinks, submodules, filters, credential helpers,
> environment-selected locators, alternate object databases or remote fetches;
> execute observed content; or emit active Markdown, HTML, SVG, scripts, event
> handlers or unsafe URL schemes. The secret policy SHALL screen transient
> bytes before parsing in both phases. Declared source-count, byte, depth,
> parse-time and rendered-output limits SHALL be evaluation inputs; breaches
> SHALL keep the affected source visible and Unknown.
>
> - **Case (counterexample sweep)**: exercise every prohibited path, object
>   database, revision, Git helper/filter/fetch and active-content form plus
>   each limit; include valid authority followed by malformed Phase-A output and
>   manifest validation failure.
> - **Observable**: no request escapes the phase-specific Git object reader; no
>   prohibited helper, fetch, execution or active sentinel runs or reaches a
>   sink; rejected/limited sources remain visible; invalid authority yields zero
>   Phase-A/Phase-B calls, while Phase-A/manifest failure yields zero Phase-B
>   calls.
> - **Oracle**: separate injected Phase-A and Phase-B read spies, Git helper/
>   fetch/execute spies, independent manifest validator, complete sink-byte
>   scans and every limit boundary decide.
> - **Oracle independence**: malicious paths, repositories, object databases,
>   manifests, content, limits and spies are supplied outside production
>   discovery, parsing and rendering code.
> - **Falsifier**: host working-tree access, alternate locator/object database,
>   cross-revision read, submodule/symlink/traversal, Git helper/filter/fetch,
>   observed execution, unsafe output, an unbounded operation, a vanished
>   rejected source or any Phase-B call after failed manifest validation.
>
> #### Scenario: Active repository content remains inert
>
> - **WHEN** either phase encounters raw active HTML, an unsafe URL or secret
>   sentinel in an otherwise admitted Markdown source
> - **THEN** no active or secret content reaches Polaris, JSON, logs, caches or
>   records
> - **AND** the affected source remains counted with its exclusion or Unknown
>   reason
>
> #### Scenario: Invalid manifest blocks Phase B
>
> - **WHEN** valid authority admits Phase A but the derived manifest changes
>   locator, object database, revision, path scope or signed grammar
> - **THEN** Phase B performs zero body reads
> - **AND** the project model remains Unknown with the failed validation route

Keep the existing warrant block and add
`TRUSTED-BOOTSTRAP-OBSERVATION-DIR-2026-08-31` to `decisions`.

## What explicitly does NOT change

- A1 remains the only basis for the `Syzygy-verified` provenance state.
- RFC3-16(b)'s nine-item A1 binding model and RFC5-25's independently kept
  audit trail remain unchanged.
- The trusted mode applies only to read-only repository observation. It cannot
  authorize writes, egress, execution, credentials, environment access,
  deployment, release, certification, autonomy or another authority type.
- SEC-5 remains an outcome rule. Matching or unclassifiable content is excluded
  before parsing; no raw body is stored, logged, rendered or returned.
- PWB's closed source grammar, exact Git revision, item denominator,
  contradiction, Unknown, containment, resource-limit and parity rules remain.
- The two provenance states, their names and their upgrade path remain.
- No earlier body read becomes authorized or admissible evidence.
- The current consent, policy and registry candidates remain non-effective
  until the owner signs their exact final digests.

## Warrant

The owner explicitly directed:

> “let's relax this requirement for now. I'm OK with this being a general
> principle that isn't strictly enforced, rely on trust rather than systemic
> blockage here”

The normalized boundary is recorded in
`.syzygy/governance/decisions/POLARIS-TRUSTED-BOOTSTRAP-OBSERVATION-DIRECTION.md`.
It accepts same-tree forgery risk for read-only observation while preserving
all non-observation gates.

## Evidence or decision basis

- `docs/reviews/R-POLARIS-POC-EXCEPTION-SECURITY-RAW.md` identifies the exact
  risk now accepted rather than silently claimed absent.
- `docs/reviews/R-POLARIS-A1-LOCAL-AUDIT-BOUNDARY.md` shows why the prior hard
  gate cannot be satisfied locally on this host.
- `docs/reviews/R-POLARIS-OBSERVATION-GATE-CONFIRMATION-RAW.md` confirms the
  earlier three-artifact shape; their revised bytes require fresh review.
- `docs/reviews/R-POC-OWNER-WALKTHROUGH-POLARIS.md` records the product failure
  this observation must unblock.

## Terms introduced / retired

- `owner-trusted-bootstrap`: authorization mode for exact state-(1) acts used
  by read-only repository observation.
- Owner-visible notice: “Observation uses owner-trusted records; independent
  audit is not configured.”
- No provenance state, epistemic label, tier, Unknown reason or degradation
  state is introduced or retired.

## Downstream impact

Method: fixed-string sweeps with both `rg -F` and `git grep -F` at baseline
`3f58530`, once through `git grep` and independently through `rg` over a
`git archive` extraction of that exact commit. Both methods returned the same
starting denominator: 191 files cite `RFC3-16(a)`, 45 cite `RFC3-16(c)`, 35
cite `RFC4-7`, 40 cite `RFC5-16`, and 24 cite `PWB-REQ-005`. The
same-logical-change pass must
classify every member as edit, re-review or no impact.

Known direct propagation:

1. RFC 0003/0004/0005 installed clause modules and candidate mirrors. RFC 0003
   and RFC 0004 package READMEs receive explicit no-impact dispositions; their
   two-state and mandatory-registration summaries remain true. RFC 0005's
   installed and candidate README summaries must distinguish the narrow
   trusted read-only mode from A1-gated egress/execution/effects.
2. Wave-A and active manifests; contract/dependency indexes, budget and
   context/router projections; exact-byte review and a superseding owner
   acceptance act.
3. Every signed PWB artifact whose behavior, warrant, coverage or digest moves:
   proposal, design, specification, tasks, capability coverage, contract
   coverage, repair delta, dependency union and affected matrices; fresh review
   and one superseding eleven-digest sign-off act.
4. Capability 1's requirement bodies and coverage remain unchanged because its
   RFC3-16(a) consequences apply to Capability 1, not this PWB observation.
   The signed `three-surface-poc-experience/CONTRACT-COVERAGE.md` requires a
   digest-bound scope amendment because its whole-POC statements that consent,
   runtime provenance evaluation, a registry and secret policy do not exist
   become false once this child change binds.
5. Final consent, policy and registry candidate digests and review records;
   their exact acts occur only after the amended contract/PWB bytes bind.
6. `AGENTS.md`, `PROJECT-STATUS.md`, Beads and task 1.5 update only after the
   full transaction; their current A1-only statements remain true until then.

Historical decisions, reviews, incidents and prior acts remain append-only.
The rejected `PWB-EX-1` candidate stays marked not offered.

## Migration / supersession plan

No accepted or signed byte changes before owner sign-off. If this delta passes
review, prepare complete amended candidate copies and every invalidated derived
artifact, freeze their bytes, and present their exact digests together. The
ordered owner transaction is: accept amended Wave-A contract bytes; sign the
amended PWB suite; then consent/approve/adopt the final three gate artifacts.
Only that complete transaction makes implementation dispatchable.

Rollback before adoption is deletion of this candidate. After adoption, a
later owner amendment restores the A1-only observation gate; prior observation
records remain immutable and disclose their original authorization mode.

## Review

**Required class:** CC-REV-1 authority boundary, deterministic observation,
security and public interface; CC-REV-4 material normative amendment

**Reviewer:** pending fresh-context review

**Verdict:** pending
