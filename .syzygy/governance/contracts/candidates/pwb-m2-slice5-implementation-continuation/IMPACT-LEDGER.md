# Impact ledger — continue PWB implementation authorization for M2 slice 5

> **Candidate — binds nothing.** This ledger describes what the offered
> direction would reach if you gave it. It performs no act, edits no signed
> byte and authorizes no implementation.

**Baseline:** Syzygy `29e036f4` (`origin/main` when drafting began).

**Subject:** a plain owner direction (`OWNER-DECISION-PACKET.md`). It
changes no governed artifact, so there is no manifest and no subject
digest; its effect is on which implementation work becomes lawful.

## Discovery method and denominator

[Observed] Every NUL-separated path from `git ls-files -z` at the baseline,
read as bytes, decoded as UTF-8 and scanned with Python `re.findall` over
the whole file. Denominator: **2,939 tracked files**, of which four failed
UTF-8 decoding and were skipped, all PNG captures:

- `docs/evidence/orrery-height-repaired-narrow-2026-09-09.png`
- `docs/evidence/orrery-height-repaired-wide-2026-09-09.png`
- `docs/evidence/polaris-existing-orrery-narrow-2026-09-09.png`
- `docs/evidence/polaris-existing-orrery-wide-2026-09-09.png`

The figures count the whole tree at the baseline, including candidate
packages and retained raw reviews; they are a population, not a consumer
list, and they do not count this package.

| Pattern (Python `re`, exact) | Files | Occurrences |
|---|---:|---:|
| `dov\.19\b` | 8 | 12 |
| `` `\.19`\|\b\.19\b \(continuation `` (continuation forms; the `\|` is the table's escaped alternation bar) | 6 | 6 |
| `currencyBounds` | 22 | 55 |
| `assessCurrency` | 26 | 133 |
| `no-currency-bound-declared` | 97 | 177 |
| `(?i)\bM2 slice 5\b` | 13 | 20 |

[Observed] The eight files carrying `dov.19`:

- `.syzygy/governance/contracts/candidates/pwb-registry-currency-briefing-amendment/OWNER-DECISION-PACKET.md`
- `.syzygy/governance/contracts/candidates/pwb-registry-loaded-profile-amendment/OWNER-DECISION-PACKET.md`
- `.syzygy/governance/decisions/OWNER-INSTRUCTIONS-2026-09-29-30-READABILITY-AND-REGISTRY.md` (two)
- `docs/evidence/spec-readability-reconciliation-2026-10-02/README.md`
- `docs/plans/2026-10-03-smooth-example-roadmap.md`
- `docs/pursuits/2026-09-22-vision-pursuit-data.json` (two)
- `docs/pursuits/2026-09-22-vision-pursuit.md` (two)
- `docs/reviews/R-DOV24-LOADED-PROFILE-AMENDMENT-6-RAW.md` (two)

[Observed] The six files carrying the bare `.19` continuation form:

- `.syzygy/governance/contracts/candidates/pwb-missing-currency-disclosure-scenario/OWNER-DECISION-PACKET.md`
- `.syzygy/governance/contracts/candidates/pwb-missing-currency-disclosure-scenario/SEMANTIC-DELTA.md`
- `.syzygy/governance/decisions/POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md`
- `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
- `docs/reviews/R-PWB-MISSING-CURRENCY-DISCLOSURE-SCENARIO-DELTA-CONFIRMATION-4-RAW.md`
- `docs/reviews/R-PWB-MISSING-CURRENCY-DISCLOSURE-SCENARIO-DELTA-CONFIRMATION-RAW.md`

None of these fourteen is edited by this package or by recording the
direction. Each says the gate is open, which stays true of its own date;
after recording, documentation cites the new record rather than editing
them. Several are bound (the registry and missing-currency packages, under
their acts and tags) or raw review output (CC-REV-6).

## Readback of the predecessor gates

[Observed] Method, re-runnable at the baseline:

1. `git show <tag>:<registry entry path>` at each of the three recording
   tags `pwb-adopt-registry-entry-signed-2026-09-30`,
   `pwb-adopt-registry-entry-signed-2026-10-02` and
   `pwb-registry-machine-ceiling-amendment-v1.0`; parse each as JSON and
   compare `entries[0].currencyBounds` and
   `entries[0].currencyBoundSemantics` with the tree's, serialized with
   sorted keys. All three are equal to the tree's. The tree has 13 rows and
   7 semantics keys (`boundChange`, `claimClassAssignment`, `measuredFrom`,
   `measuredTo`, `outOfBoundResult`, `outsideTheseBounds`,
   `undeclaredClass`).
2. SHA-256 of the registry entry at each tag and in the tree, compared with
   the argument each act record names. Each tag's bytes hash to its own
   act's argument, and the tree's to the 2026-10-20 machine-ceiling act's,
   which `apps/three-surface-poc/src/governance-inputs.ts` lines 60–64 name
   as the current registry act. The digests are not copied here; the act
   records carry them.
3. In the PWB `spec.md`, the scenario heading (level four, titled "No
   effective currency bound is disclosed outside freshness") occurs once at
   the tag `pwb-missing-currency-disclosure-scenario-v1.0` and once in the
   tree, and the block from that heading to the next level-four heading is
   byte-identical between them.

## The registry trigger and the field bar

[Observed] The 2026-09-30 read-gate direction bars "reading, evaluating or
rendering" the currency bounds, the semantics block and
`maxBriefingResponseBytes`, gated on `syzygy-dov.19`. The 2026-10-02
re-pin direction keeps that bar ("Unchanged: … the 2026-09-30 direction's
bar on reading the currency and briefing fields"), and the 2026-10-20
machine-ceiling act changed only `maxMachineResponseBytes`. The offered
direction lifts the bar for the bounds and the semantics block only;
`maxBriefingResponseBytes` stays barred.

[Inferred] If the loaded-profile registry act (row P-112, unperformed) is
performed later, it supersedes the registry role again. Its packet adds
`observationGrammar` fields and leaves the currency fields alone, so under
B1 no further continuation would be needed; B1's test of that is byte
identity of the two fields, not the packet's description.

## Behavior-contract pins

[Observed] The registry entry's `governingBehaviorContract.version` names
the PWB `spec.md` the readability-successor sign-off bound, and the
`spec.md` in the tree hashes differently: later sign-offs, the
missing-currency one among them, moved it. Row P-95 owns that re-pin.
[Observed] `governance-inputs.ts` lines 53–55 say "Nothing here reads
`governingBehaviorContract`", and B9 keeps it unread. [Inferred] The stale
pin therefore does not block slice 5, as it did not block the 2026-10-15
direction's amendments; it is disclosed, not repaired.

## Implementation consumers

[Observed] Files the slice-5 lane would change, read at the baseline:

| File | What is there now | What B1–B10 ask |
|---|---|---|
| `packages/three-surface-poc-core/src/project-shape-model.ts` lines 205–238 | the `FRESH` constant and its comment; `observedClaim` and `unknownClaim` assign it to every claim | remove both; freshness only from the judge (B4) |
| `packages/three-surface-poc-core/src/model.ts` lines 152–160 and 1235 | machine evidence block with `currencyBounds: readonly []`, commented "stays empty until the separately gated owner-act slice 5" | carry the effective rows (B6) |
| `apps/three-surface-poc/src/polaris.ts` lines 328–352 | `claimTuple` already renders a `freshness-absence` disclosure when freshness is absent; no claim reaches it today | the scenario's human disclosure, reached for the first time (B4) |
| `apps/three-surface-poc/src/polaris.ts` lines 400–432 | slice-1 legend markers drop when a value is used | unchanged mechanism; `stale` becomes reachable (B7) |
| `apps/three-surface-poc/src/governance-inputs.ts` lines 44–59 | the comment recording the field bar | the reader of the two fields, behind the existing gate (B1) |
| `apps/three-surface-poc/src/production-reobserve.ts` line 53 and four test files | `currencyBounds: []` literals | the effective rows |

[Observed] `packages/cap1-core/src/staleness.ts` lines 87–155 define
`assessCurrency`, with five returns over three states; its
`no-bound-declared` return carries no freshness field (lines 98–103). B4
imports it unchanged. The Capability 1 conformance tests that exercise it
(`req-062`, `req-042`) are not touched.

[Observed] The core package mints the claim-id families `claim:source:`,
`claim:item:`, `claim:fact:`, `claim:class:`, `claim:project-account:`
and `claim:project-shape`, which `claimClassAssignment` assigns, and
`claim:currency-probe`, which `outsideTheseBounds` leaves outside (B2).
Method: every `claim:` prefix literal in non-test TypeScript under
`packages/three-surface-poc-core/src/`.

## Effects to expect on a live evaluation

- [Inferred] Under reading (i), claims change only by the age of the
  evaluated revision against each class's bound: the 30-day classes
  (`roster-identity`, `project-shape`) go `stale` first when the observed
  revision is old. Under reading (ii) many more claims would go Unknown.
- [Unknown] How many claims land in each judge arm at the next live
  evaluation, and the byte cost on `/polaris`. Added Unknown reasons and
  routes add bytes; B10 measures both host forms. The 1,650,000-byte
  working target comes from the 2026-10-02 lane B direction.
- [Inferred] The scenario's arm should have no live members (B2, B10).

## Interactions

- **Shared-model WIP one.** Slice 5 changes `PocModel`, so it queues behind
  the 2026-10-15 direction's chain; ordering is the coordinator's.
- **The dov.35 successor (`syzygy-sin5`).** It would name missing-currency
  among the signed amendments it authorizes. The packet's "Overlap with the
  dov.35 successor direction" section says how the two compose.
- **Lane B.** Declined 2026-10-02. Its freshness-hoist estimate assumed
  uniform freshness, which slice 5 ends; nothing depends on it now.
- **Machine-view package (`syzygy-dov.22`).** The briefing route and its
  ceiling stay behind it; B9.

## Governance registration

[Observed] None, by design. `scripts/check_governance.py` `_act_subjects()`
registers only entries whose argument is a SHA-256 over a named subject,
and `ACT_DIGEST_COPY_FILES` watches copies of such digests. This direction
has neither, as the 2026-09-05 continuation had neither. Adding one would
invent a digest ceremony, which bead `syzygy-dov.19`'s acceptance criterion
5 forbids. No `PWB_SUCCESSOR_CHAIN` link, no recorder script, no
`PROJECT-STATUS.md` battery line and no hosted-workflow step are added, so
the CG-26 lists and count are untouched.

## Files changed by this preparation branch

- this package: `OWNER-DECISION-PACKET.md`, this ledger and
  `REVIEW-BRIEF.md`.

No `.beads/` file, signed byte, act or sign-off record, recorder,
governance check, implementation file, status page or hosted workflow is
changed. No register row is added to `PENDING-OWNER-DECISIONS.md`; whether
and when to queue one is the coordinator's integration step.
