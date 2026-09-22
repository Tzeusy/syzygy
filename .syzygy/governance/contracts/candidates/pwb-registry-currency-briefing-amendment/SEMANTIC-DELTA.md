# Semantic delta — registry currency bounds and the briefing ceiling

> **Candidate — binds nothing.** Agents drafted these bytes under the
> owner's 2026-09-21 rulings in
> `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
> (P-69 question 2 arm (a), P-72 question 2, and the cross-cutting reading
> "One registry act, not two"), which authorize **drafting only**. Effect
> would come from one superseding `adopt-registry-entry` owner act over the
> subject named below, and from nothing else. Silence, a commit, a review, a
> merged pull request, a passing check or this manifest performs no act.
> Nothing here authorizes an implementation; the implementation that would
> read these fields additionally waits on a separate plain continuation
> direction, which this package does not contain and does not prepare.

**Artifact(s):**

- `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
  — the single subject. Its current bytes are the argument of the act
  recorded at
  `.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`
  (2026-09-05), which supersedes
  `.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-ACT.md` for the
  `adopt-registry-entry` role only. Those bytes are **not edited here**.
  The proposed bytes exist only as the unified diff
  `proposed/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json.patch`,
  and the single row of `PWB-EFFECT-AMENDMENT-MANIFEST.txt` hashes the
  result of applying that diff to the current bytes. Neither the superseded
  record, its digest, its tag, nor the bytes either record bound are
  touched by this package.

**Stable IDs affected:** `PWB-REQ-006` (the declared resource envelope and
its final-output ceilings) and `PWB-REQ-007` (the complete epistemic tuple,
including freshness) are the requirements whose inputs change. `RFC2-9`
(a currency bound is an authorization-bearing governance artifact) and
`RFC2-10` (the four closed freshness values) are the clauses the new block
answers to. **No requirement or clause is minted, retired, renumbered or
amended by this package** — every one of them is amended, if at all, by the
separate specification packages the ruling record routes elsewhere
(`syzygy-dov.22` for the derived read-only machine view category, and the
P-69 Q7a clarification scenario for the undeclared-class disclosure).
`CAP1-REQ-062` is the conformance identity of the judge this block feeds;
it is not amended either.

**Change class:** **Normative.** Three independent reasons, any one of
which is sufficient:

1. The block changes what an implementation is permitted and obliged to do.
   Before it, no bound is declared for any class; after it, thirteen classes
   carry an exact maximum age against which an evaluation's claims are
   judged, and a claim's rendered freshness can change as a result.
2. It mints a third declared response ceiling. `PWB-REQ-006` says the
   registry declares one evaluation-wide resource envelope and that the
   final encoded human HTML and machine JSON each have an explicit byte
   ceiling. A third ceiling is an addition to that envelope, not a
   restatement of it.
3. The subject is digest-bound. Any change at all to these bytes retires
   the digest the act in force names, so there is no editorial path
   through this artifact. "Editorial" would be a reviewable claim here and
   this package does not make it.

**Author:** agent draft, under the 2026-09-21 ruling record named above.

**Date:** 2026-09-21.

## Current meaning

Two things are true of the subject's current bytes, quoted in full rather
than summarized.

**One — the resource envelope declares seven limits and exactly two final
response ceilings.** `resourceLimits` reads:

```json
      "resourceLimits": {
        "maxSources": 512,
        "maxBytesPerSource": 1048576,
        "maxTotalBytes": 16777216,
        "maxIndexDepth": 4,
        "maxParsePassesPerSource": 16,
        "maxHumanResponseBytes": 2097152,
        "maxMachineResponseBytes": 8388608
      },
```

and the two ceiling sentences of `resourceLimitSemantics` read, in full:

```json
        "maxHumanResponseBytes": "the final encoded HTTP body for each Polaris HTML response",
        "maxMachineResponseBytes": "the final encoded HTTP body for each authenticated Polaris machine JSON response",
```

**Two — the entry declares no currency bound of any kind.** There is no
`currencyBounds` key and no `currencyBoundSemantics` key anywhere in the
file. [Observed] The sweep behind that absence claim, with its denominator,
is in `IMPACT-LEDGER.md` under "Discovery method"; the literal
`currencyBounds` occurs in four tracked files, none of them a governance
declaration.

The consequence is the defect P-69 exists to remove, and it is a fact
about the artifact rather than about any implementation: with no bound
declared, `RFC2-9` gives no class an authorized maximum age, so no claim
of any project-shape class can honestly render a freshness value derived
from evidence age.

## Proposed meaning

The diff makes exactly four changes; `--diff` prints it and the script's
`--check` proves it still applies to the bound bytes.

**1. `currencyBounds` — thirteen rows, one per project-shape claim class.**
A new array beside `resourceLimits`, each row exactly two keys,
`claimClass` and `maxAgeMs`. The thirteen classes are the nine extraction
classes plus `project-fact-declaration`, `project-account-statement`,
`source-coverage` and `project-shape`. Together they cover every claim
identity the shape model mints and nothing else. [Observed:
`packages/three-surface-poc-core/src/project-shape-manifest.ts` for the
nine; `packages/three-surface-poc-core/src/project-shape-model.ts` for the
six claim-id families.]

**The thirteen `maxAgeMs` values are the owner's numbers, not this
package's.** They are proposed, with one line of reasoning each, in
`OWNER-DECISION-PACKET.md` under "Every value here is the owner's", and
are carried in the diff only so that a single complete artifact can be
reviewed and acted on. Changing any of them regenerates the manifest row
and therefore the act argument; the packet says so at the point of
decision.

**2. `currencyBoundSemantics` — seven sentences, in the style of
`resourceLimitSemantics`.** `measuredFrom` and `measuredTo` answer the two
questions P-69 Q2 names: the bound is measured from the committer instant
of the exact Git object the declaration was extracted from, to the
evaluation's own as-of instant and to no other coordinate. `measuredTo`
states the consequence that makes the bound auditable — the judge reads no
wall clock, so two runs of one identified evaluation agree on every
freshness state. `claimClassAssignment` says which claims each row
governs, naming every population by its full claim id: the six keys behind
`claim:fact:project-account:<key>` and `claim:project-account:<key>` are
two different populations that differ only by an infix, and they take
different rows, so the sentence decides the assignment on its own words
without a reader holding the implementation open beside it. `undeclaredClass` says that a class with no row never leaves
Unknown and that no implementation constant, default or fallback repairs
that. `outOfBoundResult` says that age-exceeded, unreadable and
future-dated evidence all fail closed. `outsideTheseBounds` says the rows
cover project-shape claims only. `boundChange` states `RFC2-9` in the
entry's own voice: a value here is declared by an exact owner act over
this entry and by nothing else.

**3. `maxBriefingResponseBytes` — a third declared response ceiling.**
Added to `resourceLimits` with its own `resourceLimitSemantics` sentence,
placed after `maxMachineResponseBytes` and before `breachResult`, which is
unchanged. The sentence says the ceiling covers the final encoded HTTP body
of each authenticated derived read-only machine view response whose required
subject is one exact project-shape claim identified by its full claim id; any
remaining fields are same-evaluation joins independently derivable from the
machine answer already served under `maxMachineResponseBytes`. The ceiling is
separate and tighter, never a share of that one, and a view without its own
declared ceiling is not served. This is the proposed join to the now-present
`syzygy-dov.22` candidate; it remains an owner choice and binds nothing here.

**4. The version bump.** `registryVersion` and `observerVersion` both move
from `1.1.0-candidate.1` to `1.2.0-candidate.1`: a minor bump, matching
this entry's own convention, under which the 2026-09-05 amendment moved
both from `1.0.0-candidate.3` to `1.1.0-candidate.1` when it added
declared-home and precedence semantics. `discoveryVersion` is deliberately
**not** bumped: no discovery, manifest, classification, extraction or
coverage semantics change, and the discovery version is the identity the
manifest and its parse budget key off.

## What explicitly does NOT change

- **`status` and `adoptionStatus` keep their current bytes.** Both name
  the entry's governance lifecycle, and both still read as candidate
  strings under an act that has been performed. That is
  the known shape in which a bound file's own banner is permanently wrong;
  correcting it here would be an edit beyond what the ruling authorizes
  and would silently widen the act argument. The reader is routed to the
  act records instead. **This package neither repairs nor relies on those
  two strings.**
- **No existing limit value moves.** All seven current `resourceLimits`
  values and all seven existing `resourceLimitSemantics` sentences,
  `breachResult` included, are byte-identical after the diff.
- **`discoveryVersion`, `parsePassIdentities`, `failureStates`,
  `typedAuthority`, `observationGrammar`, the precedence input and every
  other block** are byte-identical after the diff.
- **No requirement, contract clause, policy or specification byte is
  touched.** This package contains no change to `openspec/**`, to
  `.syzygy/governance/contracts/**`, or to any decision record.
- **No act record is written, no phrase is performed, and no aggregate
  section is appended to `ACCEPTANCE-ACT-RECORD.md`.**
- **No implementation file is changed.** The implementation consequences
  are enumerated in `IMPACT-LEDGER.md`; they are work the adoption change
  must carry, not work this package does.

## Warrant

The authority for preparing this package, and its exact limit, is
`.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`.
Three parts of that record bear directly:

- **P-69 (M2), arm B**, rules Q1–Q6 "as the packet recommends", which
  includes Q2's arm (a): the currency bound is declared by amending this
  registry entry under a fresh `adopt-registry-entry` act, rather than by
  a new artifact with a new act type, phrase and recorder. The same row
  blocks the implementing slice on gate `syzygy-dov.18` — this package —
  and on three further gates, one of which is a continuation direction
  this package does not prepare.
- **P-72 (M5), arm A**, rules that `maxBriefingResponseBytes` is minted
  "under a superseding registry act", and that "No route is served before
  its ceiling is declared."
- **The cross-cutting reading "One registry act, not two"** requires that
  P-69 Q2(a) and P-72 Q2 travel as one superseding registry-entry
  amendment act, and states plainly that preparing the packet is agent
  work while performing it is the owner's.

The contract warrant for the currency block is `RFC2-9`, which makes a
currency bound an authorization-bearing governance artifact, and `RFC2-10`,
whose four closed freshness values are what a declared bound lets a claim
honestly carry. The `boundChange` sentence is `RFC2-9` restated in the
entry so that a reader of the entry alone cannot miss it. The warrant for
the third ceiling is `PWB-REQ-006`'s requirement that a final-output sink
have an explicit declared byte ceiling, together with P-72's ruling that
no route is served before its ceiling is declared.

The doctrine boundary is direct: `VIS-2` requires an undeclared or stale
class to remain Unknown; `VIS-4` reserves performance of the superseding act
to the owner; and `VIS-7` requires the as-of-bound result and its limit identity
to remain deterministic and faithfully rendered. `CC-REV-2` makes the later
adoption change indivisible with every authority byte this amendment
invalidates; this candidate package deliberately performs none of that change.

Method warrant: `NORMATIVE-CHANGE-WORKFLOW.md` and
`SEMANTIC-DELTA-TEMPLATE.md` under
`.syzygy/governance/contracts/candidates/policy-candidates/`. This delta
stops at step 2 of that workflow: it is drafted and its blast radius is
established. Two independent reviews were run in fresh context against
predecessor bytes; the `## Review` section below preserves their exact verdicts,
raw paths and dispositions. The later sibling-package reconciliation changed
the proposed semantics, so step 3 must run again after the owner fixes the
reserved values. No review file lives inside this package, and no self-review
was performed.

## Evidence or decision basis

- [Observed] The subject's current bytes, quoted above, and the diff's
  applicability to them: `scripts/build_pwb_registry_currency_briefing_amendment.py --check`
  re-derives both on every run and fails if either moves.
- [Observed] The blast radius: `IMPACT-LEDGER.md`, one sweep with a stated
  method and a denominator, confirmed by a second method.
- [Observed] The five return paths and three states of the judge,
  `assessCurrency` in `packages/cap1-core/src/staleness.ts`, and the
  `CurrencyBoundDeclaration` shape (`claimClass`, `maxAgeMs`) the rows
  match.
- [Observed] The two existing response ceilings and the closed
  `ResponseLimitIdentity` union in `apps/three-surface-poc/src/routes.ts`.
- [Inferred] That thirteen classes is the complete set. It rests on the
  two source files named above being the only places claim classes are
  minted; the sweep in `IMPACT-LEDGER.md` gives the denominator, and the
  builder's `--check` fails if the row set moves, but a class minted in
  future code would not be caught by either.
- [Unknown] Whether the thirteen `maxAgeMs` values and the 20,480-byte
  ceiling are the right values. No evidence in this repository fixes them;
  they are owner choices and are labelled as such wherever they appear.

## Terms introduced or retired

Introduced, in the subject's own bytes: `currencyBounds`,
`currencyBoundSemantics` and its seven keys (`measuredFrom`, `measuredTo`,
`claimClassAssignment`, `undeclaredClass`, `outOfBoundResult`,
`outsideTheseBounds`, `boundChange`), and `maxBriefingResponseBytes`.
Every one of these already occurs in this repository as a designed or
proposed name — none is coined here for the first time; see
`IMPACT-LEDGER.md` for where each occurs today.

Retired: none. No key is removed or renamed by the diff.

## Downstream impact

Enumerated with counts and a denominator in `IMPACT-LEDGER.md`. In one
line each, the four that a reviewer should not have to find:

1. **The registry-parity test is a hard gate.**
   `packages/three-surface-poc-core/src/project-shape-observation.test.ts`
   asserts the implementation's `PWB_OBSERVER_IDENTITY` and
   `PWB_RESOURCE_LIMITS` are byte-equal to this entry's. Adopting the diff
   without updating those two constants fails the suite — which is the
   check working, and is why adoption is one change.
2. **`resourceLimitsDigest` changes.** It is a SHA-256 over the canonical
   JSON of the limits object, and it is carried in every observation
   identity. Adding a field changes it for every evaluation.
3. **Two closed types widen by one.** `PwbResourceLimits` is a seven-field
   interface and `ResponseLimitIdentity` a two-literal union; a test in
   `packages/three-surface-poc-core/src/git-object-reader.test.ts` asserts
   the declared-limit name list has the same length as the constant's key
   count, so it fails until it is extended.
4. **Nothing renders differently on adoption alone.** No code reads
   `currencyBounds` today. The claims that would change are gated behind
   the implementing slice, which the ruling record blocks on further
   gates.

## Migration and supersession plan

**Supersession.** One superseding `adopt-registry-entry` act, in the shape
of the 2026-09-05 record, superseding
`PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md` for the
`adopt-registry-entry` role only. The superseded record, its digest, its
tag and the bytes it bound are preserved unedited; its recorder fails its
own `--check` by design after the successor lands, which is the recorded
convention for a superseded recorder.

**The adoption change is indivisible.** It carries, together:

1. `scripts/build_pwb_registry_currency_briefing_amendment.py --apply --at-adoption`,
   which writes the proposed bytes over the subject after re-verifying the
   whole package;
2. the new dedicated recorder script for the superseding act, which
   hard-codes the frozen subject and packet head, validates the owner's
   phrase against the bytes then present, writes the new dedicated record
   and appends exactly one aggregate section to `ACCEPTANCE-ACT-RECORD.md`;
3. the new `PWB_EFFECT_AMENDMENT_ACTS` row in
   `scripts/check_governance.py` — label, subject, predecessor record,
   the new amendment record and the act-time performed digest — plus the
   existence-gated registration of the new packet's copy files;
4. the implementation follow-ons in "Downstream impact" above, including
   the act-record path and act identity in
   `apps/three-surface-poc/src/governance-inputs.ts`, which the daemon
   verifies the artifact digest against at runtime.

Splitting any of these leaves the tree in a state where the daemon's
authority check, the parity test, or `check_governance.py` disagrees with
the act record. None of it is authorized by this package.

**Rollback.** Before the act: delete this directory and the builder
script; nothing else in the tree has changed. After the act: a further
superseding act, never an edit.

## Review

Two independent reviews have been run, each in fresh context, per CC-REV:
a first review of the drafted package and a confirmation review of the
repairs. No self-review was performed at any point.

### First review

**Raw output, stored verbatim and never edited:**
`docs/reviews/R-PWB-REGISTRY-CURRENCY-BRIEFING-DELTA-RAW.md`.

**Verdict, copied exactly: CONFIRM WITH EXCEPTIONS** (two revise, four
note).

**Rule 10 — what the raw is bound to.** The review names the commit
`3030668` and a manifest digest computed over the bytes at that commit.
The repairs below changed one line of the patch under `proposed/`, so the
proposed bytes and the manifest row both moved and the raw's confirmation
covers the reviewed bytes, not these. A reviewer wanting a confirmation of
the current bytes issues a second raw; this one is not overwritten.

### Disposition of each finding

| Finding | Class | Disposition |
|---|---|---|
| F1 — `--selftest` undercounts what `structure_findings` asserts | revise | **Repaired.** Nine predicates added, covering the three the reviewer mutation-tested by hand (top-level `registryVersion` bumped alone, a duplicated `claimClass`, a zeroed `maxBriefingResponseBytes`) and the six it identified by inspection (entry count, `resourceLimits` not an object, absent `currencyBounds`, a row with an extra key, `currencyBoundSemantics` not an object, an empty sentence). The printed count and both prose copies now read nineteen. |
| F2 — the ledger's itemized "+7" miscounts its Markdown component | note | **Repaired.** Four Markdown files, not five; the total of 7 was already correct and is unchanged. |
| F3 — `claimClassAssignment` names two populations with one shorthand | revise | **Repaired in the proposed bytes.** Every population is now named by its full claim id, and the sentence says in its own words that `claim:fact:project-account:<key>` and `claim:project-account:<key>` are different populations taking different rows. This changed the patch, so the manifest row was regenerated. |
| F4 — PWB-REQ-004 does not define a claim-class vocabulary | note | **No change.** The finding is against the review instructions this session was given, not the package: `SEMANTIC-DELTA.md` and `REVIEW-BRIEF.md` both cite PWB-REQ-006/007 and verify the thirteen classes against the two source files, which is the reading the reviewer independently confirmed with zero set difference. |
| F5 — the briefing-ceiling rationale mischaracterizes its measurement | note | **Repaired.** The packet row now states the measured figures (7,076 and 5,150 bytes) and that 20,480 is roughly 2.9x the larger — headroom, deliberately not a tight budget. The value itself is unchanged and remains the owner's. |
| F6 — "named subject" is undefined until the sibling package lands | note | **Historical disposition at the reviewed commit: open.** The reviewer correctly found no sibling package at `3030668`. The sibling candidate now exists, so the current packet reconciles against its proposed briefing member and defines the required subject as one exact project-shape claim identified by its full claim id. That semantic repair changes the proposed patch and manifest, retires both earlier reviews, and remains an explicit owner choice before fresh review. |

### Confirmation review

A second, independent confirmation review was run against the repairs.
Raw output, stored verbatim and never edited:
`docs/reviews/R-PWB-REGISTRY-CURRENCY-BRIEFING-DELTA-CONFIRMATION-RAW.md`.
**Verdict, copied exactly: CONFIRM**, with two notes.

**Rule 10 — what that confirmation is bound to.** It names the commit
`82cca27` and re-derived its figures there rather than carrying the first
review's forward. The N1 repair below changed `check()`'s decomposition,
`selftest()` and two prose sentences, so those bytes have moved again and
the confirmation covers the commit it names, not these bytes. The patch
under `proposed/` is byte-identical, so the manifest row did not move.

| Note | Disposition |
|---|---|
| N1 — the nineteen-predicate net covered `structure_findings` exactly, as claimed, but not `check()`'s own three assertions | **Repaired by fixture, not by narrowing the sentence.** `check()` is decomposed into `patch_population_findings`, `noop_findings` and `manifest_findings`, which it now calls, and three predicates mutate each in turn: a second patch under `proposed/`, a patch that changes nothing, and an absent manifest. Each fixture also asserts the good input returns clean, so none is a tautology, and each runs through the helper the caller uses, so a fixture cannot drift from `check()`. The count is now twenty-two and the packet sentence says the net covers both functions. |
| N2 — F6 is genuinely open at this commit, confirmed by a fresh sweep | **Historical confirmation at `82cca27`.** The sweep was correct for that commit. The sibling candidate has since landed; the 2026-09-22 reconciliation described below supersedes this no-change disposition for the current candidate bytes. |

**What neither review touched.** No finding reached the thirteen bound
values, the ceiling value, the class population, the act boundary or the
package's authority claims; the reviewer re-derived the manifest digest,
the key-level delta, the class vocabulary and the no-registration argument
independently and each survived.

### 2026-09-22 sibling-package reconciliation

The `syzygy-dov.22` candidate now exists at
`.syzygy/governance/contracts/candidates/pwb-machine-view-amendment/`. Its
proposed PWB-REQ-020 block names `/api/poc/briefing` as a closed derived
read-only machine-view member but does not define the granularity of that
member's required subject. This package now proposes one exact project-shape
claim identified by its full claim id, with same-evaluation joined fields as
derivable context rather than additional subjects. The builder checks that
exact sentence and a dedicated mutation widens it back to `one named subject`
to prove the check fails.

This is a semantic change to the proposed registry bytes. The manifest row was
regenerated mechanically. Both retained reviews remain valid evidence about
their named commits and are retired for these current candidate bytes. A new
fresh-context exact-byte review is required after the owner confirms or changes
the fourteen numeric values and this subject/category join.
