# Semantic delta PWB-SELF-1 — three acts for a test-only self-observation

> **Candidate — binds nothing.** Drafted by an agent under the owner's
> 2026-09-21 ruling on P-74 question 3, which asks for three separate, dated
> owner acts and authorizes drafting them, nothing more. Round 1 of review
> returned REVISE; these bytes are the repair and are not yet reviewed (see
> "Review"). Silence, a commit, a merged pull request or a passing
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

**Stable IDs affected:** none reworded. No approved requirement names the
self pair: PWB-REQ-005 says "The consent subject SHALL be exactly
`(observing Syzygy project, configured Butlers repository)`", and the M8
portability funnel says of slice 6 "No approved requirement names a
self-observation". Slice 6 would apply PWB-REQ-005's gate to the self pair
by analogy [Inferred]; whether it may is the packet's open question 10.
PWB-REQ-005's own text is not edited. The record's reading of the P-74
row, in its "What it means" column and not the owner's answer, says "The
consent record, the registry entry and PWB-REQ-005 are edited on no arm".
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
nothing observed is served, cached, logged, stored or written. The
population is closed: the doctrine index and at most the five doctrine
files it links to, "No other file is read, even if the index links to it".
The scope is pinned to observer version `1.0.0-candidate.1` and policy
version `1.2.0-candidate.1`: "A later version of either, or any wider
population, needs a new consent act". Test output is bounded: "Test
assertions compare only digests, counts, identities and closed reasons. No
assertion message, snapshot, reporter output or test log carries an
observed body or rendered text." It quotes no
owner statement, because none has been given: "If the owner performs the
act over this record's exact digest, the act itself is the grant."

**Act 2 — registry entry.** A second entry, observer
`polaris-syzygy-self-project-shape`, for the same pair. It copies the Butlers
entry's fact families, limits, parse passes and failure mapping, and differs
in these ways:

- `surfaceExposure`: `"servedRoutes": []` and cache, log, stored
  evaluation and walkthrough record all `false`;
- `readAuthority` names this repository's own object database, still
  `"workingTreeRead": false` and `"executeObservedCode": false`;
- no catalog, root summary or precedence table is declared, and a
  `profileNote` says every claim that depends on one "is Unknown rather than
  borrowed from another profile";
- the human and machine response ceilings are kept as in-memory render
  bounds, since this entry serves no response;
- its own `discoveryVersion`, `pwb-self-discovery-v1-candidate.1`, because
  the self discovery has a different seed and population, and no
  `implementationId` or `implementationVersion` until slice 6 names one;
- `observationGrammar.sourcePopulation` names the same closed six-file
  population as the consent; and
- a `selfReferenceRule` mirroring the policy's.

**Act 3 — policy extension.** The policy version moves from
`1.1.0-candidate.1` to `1.2.0-candidate.1`, and one new object,
`selfObservationScope`, is added after `scope`. Its rules:

- `"ingestBoundaries"`: observation, model, human-html and machine-json
  only — no cache, log or walkthrough record.
- `"phaseASeedPaths"`: the doctrine index `.syzygy/governance/doctrine/README.md`;
  `"phaseBPaths"`: the five doctrine files it links to, and no others.
- `"inheritedRules"`: "every other rule in this policy applies to this scope
  unchanged…", and then says how the rules that name the signed PWB grammar
  read here: "the PWB grammar's extraction classes and fixed literals apply
  unchanged; a phase-B manifest validates only when every entry is a
  phaseBPaths member the seed links to; and a source that matches no signed
  literal is excluded as an unknown extraction class, never admitted under a
  looser or unsigned grammar."
- `"selfReferenceRule"`: "no object read as an observed Git blob under this
  scope, including any policy, registry entry, consent record, act record,
  manifest, owner packet or the acceptance-act record, is an authority input
  to any evaluation; … authority for this pair is evaluated only for the pair
  (project:syzygy, repository:syzygy) and is never inherited from another
  pair, including through expectations keyed only by the observing project".

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
records the owner's answer, arm A, which for question 3 reads "three acts
scoped to a test-only self-observation (consent record, second registry
entry, secret-policy extension) before slice 6 runs". The row's "What it
means" column, which is the record's reading and not the owner's answer,
adds "slice 6 runs only after the three acts exist, each separate and
dated".

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

- [Observed] Act 3 bumps the policy version, which 10 lines in 4 files
  hard-code, and supersedes the policy act that
  `apps/three-surface-poc/src/governance-inputs.ts` names by act identity,
  recording tag, act-record path and supersession target (ledger sweep 2).
- [Inferred] Until all of those move, the Butlers body-read authority fails
  closed and the Butlers page reads Unknown.
- [Observed] Act 2's entry carries the current PWB specification digest.
  Every later PWB specification act therefore regenerates it.

## Review

Round 1: REVISE, over commit `5323721`, retained verbatim at
`docs/reviews/R-DOV25-SELF-OBSERVATION-ACTS-RAW.md`. Every finding is
dispositioned in the packet's "Review record". The repair has not been
reviewed. `REVIEW-BRIEF.md` states what a fresh-context reviewer is to be
given.
