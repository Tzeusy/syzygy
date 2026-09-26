# Semantic delta PWB-SELF-1 — three acts for a test-only self-observation

> **Candidate — binds nothing.** Drafted by an agent under the owner's
> 2026-09-21 ruling on P-74 question 3, which asks for three separate, dated
> owner acts and authorizes drafting them, nothing more. No review has been
> run on these bytes. Silence, a commit, a merged pull request or a passing
> check performs no act.

**Artifact(s):**
1. new consent record, drafted in full at
   `proposed/SYZYGY-SELF-PROJECT-SHAPE-OBSERVATION-CONSENT.md`, installed at
   adoption beside the Butlers consent record in
   `.syzygy/governance/decisions/`;
2. new adapter-registry entry, drafted in full at
   `proposed/POLARIS-SYZYGY-SELF-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`,
   installed at adoption beside the Butlers entry in
   `.syzygy/governance/declarations/adapter-registry/`;
3. `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`,
   changed only by the diff in
   `proposed/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json.patch`.

**Stable IDs affected:** none reworded. The three artifacts are the inputs
PWB-REQ-005 names, for a second pair; PWB-REQ-005's own text is not edited
(the ruling: "The consent record, the registry entry and PWB-REQ-005 are
edited on no arm").
**Change class:** Normative (a new consent, a new registry entry, and a
new policy scope; each widens what may be read).
**Author:** agent session for bead `syzygy-dov.25`
**Date:** 2026-09-26

## Current meaning

[Observed] Today the only consented, registered and screened pair is
Syzygy observing the Butlers repository. Three texts close every other pair:

- RFC1-3: "Every observed repository — governance root or not — requires a
  recorded **Consent record** (SEC-4). No consent means no observation, and
  therefore **Unknown**".
- The PWB implementation authorization act, line 73: "No second repository,
  no wider content class, no reading of Butlers content the
  secret-classification policy excludes or cannot classify."
- PWB-REQ-005: "The POC SHALL NOT read any Butlers project-shape body until
  each of the exact per-repository observation-consent record, the observing
  Syzygy project's concrete secret-detection/classification policy and the
  project-shape observer's governance-plane adapter-registry entry carries an
  effective human owner act under RFC3-16(a)…"

[Observed] The policy's one `scope` object names
`"observedRepository": "repository:butlers-configured-poc"` and ingest
boundaries that include `cache`, `log` and `walkthrough-record`.

## Proposed meaning

**Act 1 — consent.** A second consent record for the pair
`(project:syzygy, repository:syzygy)`, content class
`declared-project-shape-text`, purpose test-only. It permits read-only reads
of exact Git objects at one fixed revision a conformance fixture names, and
nothing observed is served, cached, logged, stored or written. Quoted from
the drafted record: "The rendered page and machine answer the test builds
are in-memory values the test inspects; they are never served, cached,
logged, written to disk or written to a walkthrough record." It quotes no
owner statement, because none has been given: "If the owner performs the
act over this record's exact digest, the act itself is the grant."

**Act 2 — registry entry.** A second entry, observer
`polaris-syzygy-self-project-shape`, for the same pair. It copies the Butlers
entry's fact families, limits, parse passes and failure mapping, and differs
in four ways:

- `surfaceExposure`: `"servedRoutes": []` and cache, log, stored
  evaluation and walkthrough record all `false`;
- `readAuthority` names this repository's own object database, still
  `"workingTreeRead": false` and `"executeObservedCode": false`;
- no catalog, root summary or precedence table is declared, and a
  `profileNote` says every claim that depends on one "is Unknown rather than
  borrowed from another profile";
- the human and machine response ceilings are kept as in-memory render
  bounds, since this entry serves no response.

**Act 3 — policy extension.** The policy version moves from
`1.1.0-candidate.1` to `1.2.0-candidate.1`, and one new object,
`selfObservationScope`, is added after `scope`. Its rules:

- `"ingestBoundaries"`: observation, model, human-html and machine-json
  only — no cache, log or walkthrough record.
- `"phaseASeedPaths"`: the doctrine index `.syzygy/governance/doctrine/README.md`.
- `"inheritedRules"`: "every other rule in this policy applies to this scope
  unchanged: the access boundary, phase-B manifest rule, Git-objects-only
  admission, encodings, denied paths, every detector, active-content
  classification, match action, unclassifiable exclusion…"
- `"selfReferenceRule"`: "this policy, every registry entry, consent record
  and act record in this repository are observed text under this scope and
  never an authority input to the same evaluation".

## What explicitly does NOT change

- The Butlers consent record, the Butlers registry entry and PWB-REQ-005:
  not a byte.
- The policy's `scope`, detectors, denied paths, encodings, match action,
  unclassifiable exclusion and every other key: unchanged. The builder
  checks that every key except `policyVersion` and the new
  `selfObservationScope` is equal before and after.
- No route, cache, log, walkthrough record or stored evaluation exists for
  the new pair.
- No other repository, no working-tree read, no execution of observed code,
  no network egress.
- No implementation is authorized by any of the three acts (see the
  packet's open question 4).

## Warrant

The P-74 row of
`.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
chose arm A for question 3: "three acts scoped to a test-only
self-observation (consent record, second registry entry, secret-policy
extension) before slice 6 runs", and "slice 6 runs only after the three acts
exist, each separate and dated".

## Evidence or decision basis

- The ruling row above.
- `docs/design/POLARIS-M8-PORTABILITY-FUNNEL.md`, question 3 and slice 6.
- The Butlers consent record and registry entry, from which the drafts'
  structure is copied.

## Terms introduced / retired

- *self-observation scope* — the policy's second scope object. New.
- Otherwise none.

## Downstream impact

See `IMPACT-LEDGER.md`. In short:

- [Observed] Act 3 bumps the policy version. Two code sites hard-code the
  current version: `apps/three-surface-poc/src/governance-inputs.ts` line 72
  and `packages/three-surface-poc-core/src/git-object-reader.ts` line 43.
- [Inferred] Until those sites move, the Butlers body-read authority fails
  closed and the Butlers page reads Unknown.
- [Observed] Act 2's entry carries the current PWB specification digest.
  Every later PWB specification act therefore regenerates it.

## Review

None yet. `REVIEW-BRIEF.md` states what a fresh-context reviewer is to be
given.
