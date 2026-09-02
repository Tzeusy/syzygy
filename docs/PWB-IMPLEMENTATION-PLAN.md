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
  body-read-authority.ts       PWB-REQ-005: evaluate consent / policy / registry
                               triples; closed 195-case invalid vocabulary; 8 valid
                               triples; failed state-(2) never downgrades
  project-shape-manifest.ts    PWB-REQ-001 phase A discovery: root index → pillar
                               indexes → Git-tree baseline specs + roster; emits the
                               revision-bound manifest (paths, extraction classes,
                               discovery version, sha256)
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
                               (fail closed; unreadable ≠ absent)
  polaris.ts                   project-level entry: Overview, Boundaries, Architecture,
                               V1, Project catalog, Capability detail, Evidence and gaps
  polaris-copy.ts              the closed copy roles and the owner-visible string table
  capability-detail.ts         argument / contract / reality bands; WhatsApp slice moves here
  authority-disclosure.ts      the one renderer for per-authority state text and the
                               exact state-(1) disclosure, shared by every surface
```

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
   `--governance-dir` override exists for hermetic tests only.
2. **The act record is parsed, never trusted.** `owner-act-record.ts`
   extracts the labelled fields the 2026-09-02 records carry: act identity,
   act type, project identity, artifact identity, exact digest, provenance
   state, supersession/revocation, A1 identity or explicit absence, owner,
   date, ceremony phrase, recording tag. Each field is `present | missing |
   malformed`; the parser owns no notion of validity.
3. **Evaluation is a pure function.** `evaluateBodyReadAuthority(inputs) →
   { admits: boolean; consent: AuthorityState; policy: AuthorityState;
   registry: AuthorityState; contradiction?: … }` where `AuthorityState` is
   `valid-state-1 | valid-state-2 | invalid(caseId)`. Per authority it
   checks, in order: the nine RFC3-16(b) items (item 3 by recomputing the
   artifact's SHA-256 from the bytes just read and comparing to the act
   argument, so an edited artifact is "wrong but present digest"); the
   association (act record names this artifact); the provenance-state input;
   false substitutes (a record that is only a tag, commit, sign-off, machine
   submission or agent assertion); lifecycle (stale, expired, superseded,
   revoked); state mechanics (state (1) explicitly selected; A1 explicitly
   absent for state (1); claimed state (2) needs successful correlation);
   state-(1) record semantics (phrase and recording tag present, well-formed
   and matching); then the authority-specific fields (consent subject pair
   and content class; policy-owning project and version; registry home,
   project, repository, read-only authority and empty write surface). The
   first failing predicate names the case; every predicate is independently
   reachable so the 195 cases are 195 predicates, not a bucket.
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
carries a `// mutation-point: <case-id>` comment. A small tool in
`apps/three-surface-poc/src/mutation-runner.ts` (tooling, not shipped
behavior) rewrites one predicate to `return ok` at a time, runs the matching
Vitest case, asserts it fails, restores the bytes, verifies the restore by
digest, and appends `{caseId, mutatedDigest, restoredDigest, failed:
true|false}` to `docs/evidence/pwb-mutation-run-<date>.json`. A run is valid
only at a named commit and is retained as review evidence; it is never run
against a dirty tree.

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
