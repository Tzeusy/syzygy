# Polaris project-wide Butlers model — implementation plan

> **Implementation guidance, never behavioral authority.** Required behavior
> is owned by the signed change
> `openspec/changes/polaris-project-wide-butlers-model/` (eleven artifacts
> bound by `decisions/PWB-STATE1-AMENDMENT-ACT.md`). Implementation is
> authorized by `decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`
> (2026-09-02). The three effect acts of 2026-09-02 are warrants only; the
> implementation must evaluate them itself before the first body read
> (PWB-REQ-005). Scope: one configured Butlers repository, content class
> `declared-project-shape-text`, read-only, local demonstration; no
> write, egress, execution, deployment, release, recovery or mission effect.
> Bead epic `syzygy-1z3`; plan bead `syzygy-1z3.1`.

Every substantive statement below is `[Inferred]` planning unless marked
`[Observed]`; the spec's own oracles decide, never this plan.

## 1. Stack and packaging

**No new language, package, runtime dependency or route.** `[Observed]` The
adopted registry entry names the implementation module as
`packages/three-surface-poc-core/src/project-shape-observer.ts` inside the
existing `three-surface-poc-core` package, so no `tsc -b` project list or
Vitest project entry changes. TypeScript on Node ≥22.15, Vitest, `tsc -b
--force` for `build:poc`, exactly as today.

- **Markdown and TOML are parsed by small, inert, purpose-built line
  parsers** in this repository rather than a third-party Markdown library.
  The extraction grammar (spec "Reader definitions") is literal: H2/H3
  headings, top-level list items, table body rows, a leading bold or code
  span, one `[butler].name` key. A general Markdown parser would both widen
  the attack surface (raw HTML, link resolution) and make the grammar harder
  to falsify. The parser never produces HTML; it produces typed items and
  NFC-normalized strings.
- **Git objects only.** Bodies are read through `git cat-file --batch` /
  `git ls-tree -r -l <revision>` against the configured repository's
  resolved Git common directory, never through the working tree, and only for
  paths admitted by the read guard (§4). `[Observed]` `code-structure.ts`
  already uses `ls-tree` metadata this way with an injectable `runGit`.
- **One shared model, parity by construction.** `PocModel` gains additive
  fields (§5); `GET /api/poc` stays `JSON.stringify(model)`; all Polaris
  HTML renders from that object.

## 2. Module layout

```text
packages/three-surface-poc-core/src/
  owner-act-record.ts          parse a decisions/ act record into the nine RFC3-16(b)
                               items (+ state, phrase, recording tag, A1 absence);
                               parse failures are typed, never coerced to "absent"
  authority-artifact-fields.ts extract the authority-specific fields from the
                               consent record (Markdown) and the policy / registry
                               JSON as present | missing; no validity
  body-read-authority.ts       PWB-REQ-005: evaluate consent / policy / registry
                               triples; closed 195-case invalid vocabulary; 8 valid
                               triples; failed state-(2) never downgrades; append-only
                               evaluation history
  authority-disclosure.ts      the one renderer for per-authority state text and the
                               exact state-(1) sentence (in core, not the app, so
                               `/api/poc`'s verbatim model JSON carries the same strings)
  git-tree.ts                  `ls-tree -r -z` parser, tree index, POSIX path
                               normalization; shared by the manifest and the reader
  project-shape-manifest.ts    PWB-REQ-001 phase A discovery: root index → pillar
                               indexes → Git-tree baseline specs + roster; emits the
                               revision-bound manifest (paths, extraction classes,
                               discovery version, sha256)
  project-shape-observation.ts PWB-REQ-001 phase A observer: injectable Git runner,
                               exact commit, committer instant as source-claimed time,
                               admitted + ledgered seed reads, observer identity /
                               versions / capture-instant stamps, capture-independent
                               observation digest, registry failure states
  git-object-reader.ts         PWB-REQ-006 read guard + exact-object reader with
                               declared resource limits; injectable runGit/read spy
  content-classification.ts    PWB-REQ-003: the adopted secret policy's six-step
                               classificationOrder over transient bytes; emits
                               hash-not-body exclusions only
  project-shape-extraction.ts  PWB-REQ-002: the nine item classes' literal grammar;
                               malformed source → whole-source Unknown, never partial
  project-shape-coverage.ts    PWB-REQ-002/004: per-class denominators, modeled /
                               Unknown / contradicted states, documented precedence
  project-shape-observer.ts    the registry-named adapter: composes the above in the
                               design.md data-flow order; zero body reads unless the
                               authority evaluation admits
  walkthrough-judgment.ts      PWB-REQ-022: run record + owner judgment act evaluation
                               (84 present-invalid + 2 absent cases)
  model.ts                     additive PocModel fields; buildButlersPocModel wires
                               the observer and the two authority evaluations
apps/three-surface-poc/src/
  governance-inputs.ts         locate and load the act-bound artifacts and act records
                               from the observing checkout's .syzygy/governance tree
                               (fail closed; unreadable ≠ absent); hard-codes the
                               controlled expectations; classifies a missing record as
                               git-ref-only / tree-attribution-only / absent
  pwb-mutation.ts              the PWB-REQ-005 mutation plan (pure): marked predicate
  pwb-mutation-run-main.ts     sites + literal mutations; runner writes docs/evidence
  polaris.ts                   project-level entry: Overview, Boundaries, Architecture,
                               V1, Project catalog, Capability detail, Evidence and gaps
  polaris-copy.ts              the closed copy roles and the owner-visible string table
  capability-detail.ts         argument / contract / reality bands; WhatsApp slice moves here
```

P1 deviation, recorded 2026-09-03: `authority-disclosure.ts` landed in
`packages/three-surface-poc-core/` rather than the app so the machine channel
inherits the strings by construction, and the field extraction split out into
`authority-artifact-fields.ts`.

P2.1 note, recorded 2026-09-03: `git-tree.ts` was split out because the
manifest (2.1) and the exact-object reader (2.3) share tree metadata. The
manifest's index-link grammar is a closed rule under
`pwb-discovery-v1-candidate.3`: inline links and reference definitions
outside fenced blocks and code spans; a pillar root is a root-index link
whose directory basename is one of the five pillar keys; a pillar index
names only files under its own root; images, external, escaping, directory
and self links are recorded as ignored. Extraction classes are assigned by
(rule, pillar, path within root). `[Unknown]` whether the real Butlers
indexes fit this grammar — §9 already routes that to the first P4 live run.

P2.2 note, recorded 2026-09-03: the phase A observer landed as its own
module, `project-shape-observation.ts`, rather than inside the registry-named
`project-shape-observer.ts`, so the P1 gate file (and its 86-site mutation
denominator) stays byte-stable; the gate composes it through `read`, and the
test proves a non-admitting authority issues zero Git calls. The observer
resolves the revision to an exact commit, takes the committer instant from
Git metadata as the source-claimed instant PWB-REQ-001 wants kept distinct
from capture, and admits every seed read against the tree before it happens
(root index or pillar `README.md` only, tree-matching object id, regular blob
mode; symlinks and submodules are refused, over-limit seeds are not opened).
Returned bytes are verified against Git's own blob identity before use. The
production `gitRunnerFor` binding exists but nothing in `main.ts` calls it:
no Butlers read happens before P4.

P2.3 note, recorded 2026-09-04: `git-object-reader.ts` is the phase B
read guard and reader. It never reuses phase A's `readSeed` (the phase A
seed allowlist is narrower and already act-tested), but both share
`git-tree.ts` metadata and the P2.2 `GitRunner`, `gitBlobObjectId` and
`ResourceLimitBreach` shapes. Decisions: (a) the caller's path must already
be normalized — a traversal-shaped path that would resolve inside the tree
is refused as `path-not-normalized`, never silently rewritten; (b) the only
Git command the reader issues is `cat-file blob <object-id>` taken from the
tree entry, never a path-addressed read; (c) the policy's denied
basename/prefix/suffix rules are compared case-insensitively on the final
segment (strictly more refusals); (d) active content is scanned over the
whole body, code fences and code spans included, and one finding excludes
the whole source with a body-free finding (form, line, column) — a
technical README quoting HTML stays counted and Unknown rather than being
partially admitted; (e) `evaluateLimit` is the one comparison for all six
registry limits, so index depth (observer), parse time (2.5) and rendered
bytes (2.7/3.x) breach in the same shape as source count and bytes; (f)
`readManifestSources` returns one result per manifest source in manifest
order and hands each body only to the caller's `consume` callback, so no
record this module returns can carry a body. Still no Butlers read: the
reader is constructed by nothing before P4.

P2.4 note, recorded 2026-09-04: `content-classification.ts` is the policy's
six-step `classificationOrder` executed over the P2.3 reader's transient
body. Decisions: (a) the policy is a parameter — `PWB_SECRET_POLICY` is the
hard-coded copy proven byte-equal to the act-bound JSON, detectors are
compiled from the policy document's own strings (an uncompilable policy
throws rather than screening nothing), and every exclusion names the
policy version it ran under; (b) every detector runs over each body and the
first match in policy order is the one named, so a later detector's failure
cannot hide behind an earlier match; (c) three outcomes, all body-free:
`classified` (text handed to the extractor's callback only),
`excluded` (an RFC5-17 hash-not-body record in one of the two emitted
redaction classes) and `unavailable` (missing, non-blob, unreadable — the
policy never saw a body, so it is not an exclusion but stays counted with the
registry's `source-uncaptured-or-unreachable`); (d) a denied path is an
`excluded-artifact` exclusion with reason `denied-path` and no content digest,
because the body was never read; (e) a resource-limit breach is the policy's
`unclassifiable-excluded` exclusion, but its Unknown reason follows the
registry's `someSourcesUncapturedOrOverLimit` mapping (`Partial snapshot`,
`source-uncaptured-or-unreachable`) rather than the policy's blanket
`excluded-content` — the two act-bound artifacts differ here and the
registry is the adapter's declared error mapping (RFC4-2 item 6), so it wins
for the reason while the policy wins for the exclusion record; (f) parse
failure (step 5) is exposed as `parseFailureExclusion` for the extractor to
call, since only 2.5 knows when a parse failed. Still no Butlers read.

P2.5 note, recorded 2026-09-04: `project-shape-extraction.ts` implements the
spec's "Reader definitions" literally, one function per item class, over the
classified text 2.4 hands to its consumer. Decisions: (a) the parsers are
inert line parsers of the plan's own making — ATX headings, column-0 list
items, pipe tables with a required delimiter row, a leading bold or code
span, a Markdown link, and one `[butler].name` key — fenced code blocks are
masked, CRLF is tolerated, and nothing is rendered or resolved; (b) identity
is `(class, key)` with the path and 1-based line as anchor state, keys and
statements are NFC-normalized and nothing else (heading text, levels,
top-level depth, column counts and label positions are matched exactly);
(c) the six `project-account-section` keys are `purpose`, `promises`,
`refusals` (vision.md), `architecture` (every H2 of architecture.md
concatenated) and `v1-scope`, `v1-success` (v1.md); success criteria are
keyed `vision:<n>` / `v1:<n>`; topology components `<H2 ordinal>:<label>`;
catalog entries by their leading bold/code label, which must be followed by
a dash; craft policies by the File-column link target's basename; baseline
specs and roster identities by their tree directory; (d) any grammar
failure — closed vocabulary `unsupported-source`, `missing-heading`,
`malformed-list`, `malformed-row`, `malformed-toml`, `duplicate-key`,
`ambiguous-leading-label` — makes the whole source Unknown (no items, no
denominators), and a duplicate key within one source is such a failure
while cross-source duplicates are left for 2.6's contradiction handling;
(e) a source whose classes all succeed carries per-class item counts as its
denominators, which 2.6/2.7 sum into the per-class D. The REQ-002 oracle is
a regex-only second extractor inside the test file; 35 rule-6 mutations
killed with digest-verified restore
(`docs/evidence/pwb-p2-5-extraction-mutation-run-2026-09-04.json`). Still no
Butlers read: extraction is called by nothing before P4.

P2.6 note, recorded 2026-09-04: `project-shape-coverage.ts` is coverage as
data over the classified-and-extracted population. Decisions: (a) the
source population is the input list unchanged and in order; each source
carries a known item denominator or an Unknown one with the classifier's
fixed reason, and a grammar failure becomes the policy's `parse-failure`
exclusion (hash kept, failure named, `excluded-content`); (b) facts are
reconciled from declarations — `item:<class>:<key>` for identities (a
second declaration of one identity is a conflict whatever its statement
says, per the spec's duplicate-key rule), `count:<class>` derived from the
admitted items, and stated declarations supplied from outside the grammar
(fixtures now; empty in production until Butlers is observed to declare a
summary that the model may read); (c) a conflict is resolved only by a
`PrecedenceRule` whose anchor path is in the admitted population and whose
two selectors each match exactly one declaration; rules with disagreeing
winners, out-of-scope facts or unmatched sides decide nothing and the fact
is Unknown with RFC2-24's `contradicted-pending-adjudication`, every
declaration retained and every considered rule's outcome recorded; (d) a
count over a class with any Unknown-denominator source is itself Unknown
with that source's reason, whatever a summary states; (e) item states are
modeled or contradicted, `unknown` is reachable only through count facts,
and per class modeled + unknown + contradicted equals the declared count
while D is known only when every source of the class was readable.
`[Unknown]` still whether Butlers declares any precedence rule — the first
live run (P4's second half) answers it; the eight-versus-nine domain-butler
conflict is the first fixture either way. 27 rule-6 mutations killed
(`docs/evidence/pwb-p2-6-coverage-mutation-run-2026-09-04.json`). Still no
Butlers read.

P2.7 note, recorded 2026-09-04: `project-shape-model.ts` composes P1–P2.6
into the one `ProjectShape` value that `model.ts` places on `PocModel`;
`GET /api/poc` is still `JSON.stringify(model)`, so the machine answer is
extended by construction. Decisions: (a) the gate runs first — a
non-admitting evaluation issues zero Git commands and the shape is
`not-admitted` with the gate's reasons; no evaluation at all is
`not-evaluated` with the loader's failure text, Unknown as
`unconsented-source-or-provider`; (b) every claim is a full PWB-REQ-007
tuple — stable claim id, the PWB-REQ-005 evaluation id, cap1-core's
`EpistemicState` (label, tier, one primary and deduplicated secondary
reasons, freshness), a resolution route per reason from a twelve-entry
table keyed by RFC2-24's vocabulary, challenge `unchallenged` (no challenge
channel exists yet), and support anchors (path, line, content digest,
source identity); (c) Observed claims are `report-fact` ("the source
declares X") and `fresh` (bound to the evaluated revision); contradictions
are `suspended`; an excluded, uncaptured or absent source is Unknown with
the classifier's reason; (d) the whole-shape claim derives from its members
(sources and reconciled facts): the first Unknown member's reason is
primary, the rest secondary, and observer degradation is disclosed beside
it as data because the population never shrinks; (e) class aggregates
carry label, tier, freshness and primary/secondary reason counts over
members and declaring sources, never a headline; (f) phase B re-lists the
tree at the resolved commit rather than reusing phase A's listing, so the
reader is bound to the same object ids the manifest recorded; (g) the
daemon evaluates the authority from its own working directory's governance
tree at every model build and fails closed to `not-evaluated` if the
inputs cannot be loaded; (h) `walkthroughJudgment` is deferred to 4.6 and
no live Butlers observation was run — the model is exercised only through
an in-memory Git runner over a Butlers-shaped fixture. Item-level
contradiction and item-level `unknown` are unreachable through the P2.5
grammar (each identity has one declaring source; a duplicate key inside a
source is a grammar failure), so those branches are tested at the exported
`itemClaim` seam. 38 rule-6 mutations killed
(`docs/evidence/pwb-p2-7-model-mutation-run-2026-09-04.json`). Still no
Butlers read.

P3.1 note, recorded 2026-09-04: `apps/three-surface-poc/src/polaris.ts`
now opens with the seven project-level groups in the task's order —
Overview, Boundaries, Architecture, V1, Project catalog, Capability detail,
Evidence and gaps — rendered exactly once each from `PocModel.projectShape`
(PWB-REQ-010; RFC7-1, RFC7-13). Decisions: (a) the movement scaffolding and
the "three movements" tally are gone; the WhatsApp slice renders unchanged
under "Capability detail" behind a scope instruction naming it one
capability within the complete catalog; (b) group membership is fixed:
Overview = purpose and promises plus the project-account class aggregate;
Boundaries = refusals plus principles; Architecture = the architecture
statement plus topology components; V1 = V1 scope, V1 success and success
criteria; Project catalog = declared projects, roster identities, design
contracts, baseline specs and craft policies, each class as its own block
with declared/modeled/Unknown/contradicted counts and a denominator that
is Unknown when a source was unreadable; (c) an unobserved shape
(`not-evaluated`, `not-admitted`, `observation-failed`) renders every
project group as Unknown in place with the shape claim's reason, its route
and the kind-specific detail — never an empty group (RFC7-15); (d) every
rendered project-shape claim carries a `claim-tuple` span with claim id,
label, tier, freshness and evaluation id, and Observed leaves cite
path:line plus the exact content digest, linked to a source row in
"Evidence and gaps" that carries the source digest, rule, outcome and
denominator (PWB-REQ-011; RFC7-16); reconciled facts that agree are not
rendered as separate claims (their counts are the class blocks),
contradicted facts are, with every declaration kept; (e) exclusions render
as hash-not-body (path, redaction class, detector or reason, digest,
policy) and an Unknown-by-reason list closes the group with
`missing-declaration` and `unconsented-source-or-provider` foremost; (f)
the copy for the new groups already meets PWB-REQ-012's bounds (headings
≤ 6 words, ledes ≤ 20, no prohibited vocabulary), tested for the group
headings, ledes, notice and shell lede only — the exhaustive `polaris-copy.ts`
role table and independent extractor remain task 3.3; (g) surface tests
reach an `observed` shape through `test-project-shape-fixture.ts`, an
in-memory Butlers-shaped Git runner plus admitting/rejecting authority
evaluations (a copy of the core fixture texts, kept in the app so the
core's test module stays private). Five hand rule-6 mutations: four killed
(group reorder, excluded-body leak, empty unobserved groups, omitted
route); the fifth (hard-coding freshness to `fresh`) is equivalent because
the model stamps every claim `fresh` — a freshness-varying claim does not
exist yet, so no test can distinguish it. Still no Butlers read.

Nothing lands in `openspec/**` or `.syzygy/**`. The walkthrough execution
record (PWB-REQ-022) is a governance record written by the recording
session, not by the daemon; the owner judgment is an owner act prepared as a
packet, the same way task 1.7 was.

## 3. The body-read gate

This is the risk-floor of the change. Design so the spec's falsifier "any
body is read before all three acts are effective" is structurally hard to
violate:

1. **Inputs are files, not flags.** `governance-inputs.ts` resolves the
   observing checkout root (the same root `pocObserverInputsAreClean`
   already inspects), then reads exactly: the three act-bound artifacts
   (consent record, policy JSON, registry entry) and their three dedicated
   act records under `decisions/`. Each read yields `{kind:'present', bytes,
   sha256}` or a typed failure (`missing`, `unreadable`, `malformed`). A
   `repoRoot` option plus injectable `readFile` / `listDirectory` / `runGit`
   serve hermetic tests (replacing the planned `--governance-dir` flag).
2. **The act record is parsed, never trusted.** `owner-act-record.ts`
   extracts the labelled fields the 2026-09-02 records carry: act identity,
   act type, project identity, artifact identity, exact digest, provenance
   state, supersession/revocation, A1 identity or explicit absence, owner,
   date, ceremony phrase, recording tag. Each field is `present | missing |
   malformed`; the parser owns no notion of validity.
3. **Evaluation is a pure function.** `evaluateBodyReadAuthority(inputs) →
   { admits: boolean; consent: AuthorityState; policy: AuthorityState;
   registry: AuthorityState; contradiction?: … }` where `AuthorityState` is
   `valid(state-1 | state-2) | invalid(caseId) | absent(artifact-missing |
   artifact-unreadable | act-record-absent)`; `absent` is a non-admitting
   outcome outside the 195 present-invalid cases. Per authority it checks,
   in order: false substitutes first (a record that is only a tag, commit,
   sign-off, machine submission or agent assertion has no fields to judge),
   then the nine RFC3-16(b) items (item 3 by recomputing the
   artifact's SHA-256 from the bytes just read and comparing to the act
   argument, so an edited artifact is "wrong but present digest"); the
   association (act record names this artifact); the provenance-state input;
   lifecycle (stale, expired, superseded,
   revoked); state mechanics (state (1) explicitly selected; A1 explicitly
   absent for state (1); claimed state (2) needs successful correlation);
   state-(1) record semantics (phrase and recording tag present, well-formed
   and matching); then the authority-specific fields (consent subject pair
   and content class; policy-owning project and version; registry home,
   project, repository, read-only authority and empty write surface). The
   first failing predicate names the case; every predicate is independently
   reachable. `[Observed]` 2026-09-03: 85 predicate sites — 55 common ones
   shared by the three authorities (× 3 = 165 instances) plus 30
   authority-specific — carry the 195 case instances; there is no bucket.
4. **State (2) is unavailable in this repository.** `[Observed]` No RFC5-25
   audit trail exists. Correlation is an injected function whose production
   value returns `unavailable`; any record claiming state (2) is therefore
   invalid today and never falls back to state (1). Tests inject a
   `succeeded` correlator to exercise the four state-(2)-bearing valid
   triples and a `failed` one for the no-fallback scenarios.
5. **Zero reads unless admitted.** `project-shape-observer.ts` receives the
   authority result and the reader; its first statement returns a
   project-shape Unknown (reason from the registry's
   `admissionFailureMapping`, the RFC3-16(a) contradiction attached) when
   `admits` is false. The reader is an injected spy in every test; the read
   count is asserted zero in each of the 195 cases.
6. **Exact state everywhere.** `authority-disclosure.ts` is the only place
   the per-authority state text and the exact state-(1) sentence are
   rendered; Polaris, the home page and `/api/poc` carry the same strings.
   State (1) renders exactly the sentence PWB-REQ-005 quotes; nothing may
   say "verified" for it. Evaluation history is append-only per
   evaluation: a later correlation produces a new evaluation and never
   rewrites an earlier one's recorded state.

## 4. Containment, classification and extraction

- **Read guard** (`git-object-reader.ts`): a path is admitted only if it is
  relative, NUL-free, contains no `.`/`..` segments after POSIX
  normalization, resolves to a `blob` entry (mode `100644`/`100755`) in the
  exact revision's tree — so symlinks (`120000`) and submodules (`160000`)
  are rejected by mode, without touching the working tree — and its
  normalized final segment passes the policy's denied basename, prefix and
  suffix rules. The registry's `resourceLimits` block is an evaluation input:
  source count, per-source and total bytes, index depth, parse time and
  rendered bytes; a breach leaves the source counted and Unknown with reason
  `source-uncaptured-or-unreachable`.
- **Classification** (`content-classification.ts`) follows the policy's
  `classificationOrder` literally over transient bytes: membership in phase
  A seed or phase B manifest → denied path / strict UTF-8 / NUL → every
  detector (the detectors are executed from the policy document's own
  strings, so the policy version is the input) → extraction class assigned
  by the manifest → whole-artifact exclusion on any failure → admit parsed
  facts only. Exclusions carry `{contentDigest, repositoryRelativePath,
  policyId, policyVersion, detectorId | exclusionReason}` with redaction
  class `excluded-artifact` or `unclassifiable-excluded`; `redacted-span` is
  never emitted. Raw bodies are never stored, logged, rendered or served.
- **Extraction** (`project-shape-extraction.ts`): one function per item
  class implementing the spec grammar exactly; keys are literal after NFC;
  any missing heading, malformed row/list/TOML, duplicate key or ambiguous
  leading label makes that source's item denominator Unknown (no partial
  set). Identity is `(item class, declared key)`; path and digest are
  anchor state.
- **Coverage and precedence** (`project-shape-coverage.ts`): the source-path
  denominator comes from Git and phase A and never shrinks; the item
  denominator per admitted source; states modeled / Unknown / contradicted
  summing to D per class. A conflict between two admitted declarations is
  resolved only by a precedence rule that Butlers itself declares and the
  model can cite by source anchor; otherwise both anchors are retained and
  the fact is Unknown with reason `contradicted-pending-adjudication`.
  `[Unknown]` Whether Butlers declares any such rule; the first live run
  answers this and the design's known eight-versus-nine domain-butlers
  conflict is the first fixture either way.

## 5. Model and surfaces

- `PocModel` gains `projectShape` (authority evaluation with per-authority
  state and disclosure, manifest identity, source coverage, items,
  contradictions, exclusions, per-class counts, project-account statements
  with their epistemic tuples) and `walkthroughJudgment`. Epistemic tuples
  reuse cap1-core's `EpistemicState` and six rendering tiers rather than a
  new vocabulary; Unknown reasons are RFC2-24 strings verbatim.
- New provenance kinds: `project-shape-source` (path at revision, blob
  digest) and `owner-act` (record identity, artifact digest, state).
- Polaris renders the seven project-level groups in RFC7 order, then
  capability detail with the existing WhatsApp slice under it (argument /
  contract / reality bands, verbatim requirement text loaded from the
  owning artifact at render, never stored). Every owner-visible string is a
  row in `polaris-copy.ts` with exactly one role; headings ≤ 6 words, ledes
  ≤ 20, prohibited words rejected at test time by an independent extractor.
  The existing "movement" scaffolding is removed from Polaris entirely.
- Every project-shape fact, authority state, judgment state and disclosure
  carries a `data-parity-field` marker so the sweep in §6 can count both
  channels.

## 6. Verification design and denominators

| Denominator | Where | How it is made independent |
|---|---|---|
| 8 valid authority triples | `body-read-authority.test.ts` | hard-coded expected table; fixtures are hand-written act records; the test never imports the validator's case vocabulary |
| 195 invalid admission cases | same file, one `it` per case id | fixture generator mutates one field of a valid triple per case; expected outcome and read-spy count 0 hard-coded; case ids are the spec table rows, not implementation names |
| 84 present-invalid + 2 absent judgment cases | `walkthrough-judgment.test.ts` | same pattern; `verdict-unlawful` literal hard-coded |
| Source denominator and two-extractor agreement (REQ-001/002) | `project-shape-extraction.test.ts` (fixtures) and `project-shape-observer.live.test.ts` (real Butlers, `SYZYGY_POC_BUTLERS_REPO`-gated) | the second extractor is a regex-based implementation written inside the test; Git tree listing is obtained by the test's own `git` call |
| Fault sweep (REQ-003/006) | `content-classification.test.ts`, `git-object-reader.test.ts` | injected faults, sentinel strings, sink scans over model JSON, HTML, logs and state dir |
| Copy oracle (REQ-012) | `polaris-copy.test.ts` | plain text extraction from rendered HTML with an independent word counter and prohibited-term set |
| Parity sweep (REQ-020) | extend `routes.test.ts` into a multiplicity-preserving comparator over every marker class, reporting both channel counts | comparator imports no production vocabulary |
| Anchor covering and non-citability (REQ-014) | `polaris.test.ts` + a static-source sweep for downstream citations of Polaris | expected spans from captured artifacts |

**Mutation proofs** (rule 6; REQ-005/020/022 demand one per case). Each
predicate in the two authority evaluators and each parity marker class
carries a `// mutation-point: <case-id>` comment. For REQ-005 the tool is
`apps/three-surface-poc/src/pwb-mutation.ts` (pure plan) plus
`pwb-mutation-run-main.ts` (`npm run poc:pwb-mutation-run`; tooling, not
shipped behavior). Per mutation it rewrites one predicate's condition to
`false && (…)` (or applies one hand-listed literal mutation: exact-state
collapse/inflation, failed-correlation downgrade, admits-always,
contradiction suppression, history rewrite, duplicate append, forced
"independently verified", altered state-(1) sentence), runs the two
independent test files, requires every named case-instance test to fail,
restores the bytes, verifies the restore by digest, and writes one record
`{id, mustFail, observed, mustFailMissing, killed, restored}` per mutation
with source digests before/after and the commit to
`docs/evidence/pwb-mutation-run-<date>.json`. A run is valid only at a named
commit and is retained as review evidence; it is never run against a dirty
tree.

**Retained evidence** per slice: commit, `vitest run` transcript summary,
the three denominators reported separately, mutation-run file. Claims
without a resolvable record are not made.

## 7. Slices, order and bead mapping

| Slice | Content | Beads | Requirements |
|---|---|---|---|
| P1 | act-record parser, body-read authority evaluator, governance-inputs loader, authority disclosure; 8 + 195 cases with mutation runner | syzygy-1z3.26 (gate every later slice depends on) | PWB-REQ-005 |
| P2 | read guard, exact-object reader, resource limits; phase A manifest | 1z3.2, 1z3.3, 1z3.4 | PWB-REQ-001, 006 |
| P3 | content classification and exclusions | 1z3.5 | PWB-REQ-003 |
| P4 | extraction grammar, coverage, precedence; live Butlers run (the first lawful body read) | 1z3.6, 1z3.7 | PWB-REQ-002, 004 |
| P5 | model extension, `/api/poc`, epistemic tuples | 1z3.8 | PWB-REQ-001…007, 020 |
| P6 | Polaris project account, copy table, capability detail bands, proposal subordination, anchors, keyboard reachability | 1z3.9…1z3.16 | PWB-REQ-010…016 |
| P7 | verification sweep: parity comparator, mutation runs, contrast/keyboard checks, fresh-checkout demo; walkthrough judgment evaluator | 1z3.17…1z3.21 | PWB-REQ-020, 022 |
| P8 | owner cold-open walkthrough (record + judgment packet), independent review, repair, confirmation, owner report | 1z3.22…1z3.25 | PWB-REQ-021, 022 |

Order P1 → P2 → P3 → P4 → P5 → P6 → P7 → P8. **The first real Butlers body
read happens in P4 and only after P1's evaluator, run against the real
governance tree, reports an all-valid triple.** Until then every live test
runs with the read spy and asserts zero reads. Shared-model changes keep WIP
one; each slice lands with its tests, its mutation evidence where the spec
demands it, and a review at the classes below.

## 8. Risk classes and review bar

| Class | What falls in it | Review bar |
|---|---|---|
| Risk-floor | body-read authority evaluator and loader (REQ-005), read guard and reader (REQ-006), content classification (REQ-003), judgment evaluator (REQ-022), parity comparator (REQ-020) | independent fresh-context review on frozen bytes before merge; mutation evidence attached |
| Ordinary | extraction grammar, coverage, Polaris rendering, copy table | standard review; fixtures pin each grammar class |
| Trivial | tooling, tokens, non-semantic refactors | author-verified |

## 9. Known gaps and assumptions, stated now

- `[Unknown]` Automated keyboard traversal and WCAG AA contrast (task 4.4)
  need a browser driver; none is a dependency today and adding one pulls a
  browser binary over the network. The plan keeps structural accessibility
  checks in-process and records the keyboard-only cold-open walkthrough as
  the manual evidence, exactly as the previous POC cycle disclosed. A driver
  is an ordinary tooling choice if the owner wants it; it is not assumed.
- `[Unknown]` Whether the real Butlers indexes match the literal grammar at
  the observed revision. A mismatch renders that source's item denominator
  Unknown; it does not license grammar changes (those are spec amendments).
- `[Observed]` `.syzygy/governance/records/` does not exist yet; it is
  created by the recording session when the first walkthrough record is
  written, per RFC3-15's records category.
- `[Inferred]` The registry entry's `implementationVersion` is `1.0.0`; the
  observer reports that string and the entry's `discoveryVersion` as its
  identities so PWB-REQ-001's deterministic-input stamps match the adopted
  entry byte-for-byte.

## 10. Escalation back to the owner (from the act, restated)

Stop and return to the owner before: any doctrine or contract change; any
amendment to the signed PWB artifacts (including the extraction grammar or
the case tables); any change to security, privacy or retention posture beyond
the adopted policy; any change to the registry entry's constraints or limits;
any read outside the consented repository or content class; any scope beyond
the signed change. Everything else in stack and layout is settled by this
plan and its ordinary revisions.
