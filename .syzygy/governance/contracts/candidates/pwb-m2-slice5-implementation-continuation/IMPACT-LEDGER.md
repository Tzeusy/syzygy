# Impact ledger — continue PWB implementation authorization for M2 slice 5

> **Candidate — binds nothing.** This ledger describes what the offered
> direction would reach if you gave it. It performs no act, edits no signed
> byte and authorizes no implementation.

**Baseline:** Syzygy `29e036f4` (`origin/main` when drafting began). The
round-1 repairs re-ran the sweeps at the same baseline; PR #489 was read at
its head `8c334f67`.

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
| `dov\.19\b\|(?<![\w.])\.19\b(?!\.\d)` (every `.19` form, the slash run `.17/.18/.19` included; added after review round 1) | 16 | 31 |

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

[Observed] The two narrower patterns miss the slash-run form. The broad
pattern in the table's last row finds those fourteen files and two more,
16 in all:

- `.syzygy/governance/contracts/candidates/pwb-missing-currency-disclosure-scenario/REVIEW-BRIEF.md`
  (`.17/.18/.19`, line 88)
- `docs/pursuits/2026-09-22-vision-pursuit-harvest.json` (seven)

None of these sixteen is edited by this package or by recording the
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

| File | What is there now | What B1–B11 ask |
|---|---|---|
| `packages/three-surface-poc-core/src/project-shape-model.ts` lines 205–238 | the `FRESH` constant and its comment; `observedClaim` and `unknownClaim` assign it to every claim, and `observedClaim` gives tier `report-fact` | remove both; freshness only from the judge; an Unknown never carries `report-fact`; the arm marker (B4) |
| `packages/three-surface-poc-core/src/project-shape-model.ts` lines 176–179 and 432–460 | `ReasonCounts { primary, secondary }`, the only aggregate counts; `countReasons` and `classAggregate` | the one per-freshness and arm count mechanism beside them (B5) |
| `packages/three-surface-poc-core/src/project-shape-model.ts` lines 379–390, 495–502 and 694–706 | the not-evaluated, observation-failed and not-admitted whole-shape claims | judged or not as B4 says for each |
| `packages/three-surface-poc-core/src/model.ts` lines 152–160 and 1235 | machine evidence block with `currencyBounds: readonly []`, commented "stays empty until the separately gated owner-act slice 5" | carry the effective rows (B6) |
| `apps/three-surface-poc/src/polaris.ts` lines 328–352 | `claimTuple` already renders a `freshness-absence` disclosure, which says the currency bound is not declared, whenever an Unknown has no freshness; no claim reaches it today | the scenario's human disclosure, reached for the first time and keyed to the arm marker rather than to an absent freshness value, so the not-evaluated claim does not reach it (B4) |
| `apps/three-surface-poc/src/polaris.ts` lines 371–386, 762 and 1107–1214 | `reasonCountsBlock`, rendered for each class aggregate and for the whole-shape claim over `countReasonsOf` | the freshness and arm counts rendered beside the reason counts (B5, B6) |
| `apps/three-surface-poc/src/polaris.ts` lines 400–432 | slice-1 legend markers drop when a value is used | unchanged mechanism; `stale` becomes reachable (B7) |
| `apps/three-surface-poc/src/governance-inputs.ts` lines 44–59 | the comment recording the field bar | the reader of the two fields, behind the existing gate (B1) |
| `apps/three-surface-poc/src/production-reobserve.ts` line 53; `production-reobserve.test.ts` line 43, `reobserve-session.test.ts` line 32 and the fixture module `test-model-fixture.ts` line 218 (all in that directory) | `currencyBounds: []` literals | the effective rows |
| `apps/three-surface-poc/src/polaris-parity-sweep.test.ts` line 627 | asserts `evidence.currencyBounds` equals `[]` | the effective rows; the disclosure and the counts as their own parity families (B6) |

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
`packages/three-surface-poc-core/src/`. [Observed] No relation claim is
minted yet: item depth would mint them, in the class
`governing-intent-relation`, which no `currencyBounds` row names (PWB
`spec.md`, PWB-REQ-015 "Relation claim").

## Effects to expect on a live evaluation

- [Inferred] Under reading (i), claims change only by the age of the
  evaluated revision against each class's bound: the 30-day classes
  (`roster-identity`, `project-shape`) go `stale` first when the observed
  revision is old. Under reading (ii) more claims would likely go `stale`,
  since a source's last change is usually older than the revision; not
  measured.
- [Inferred] Observed claims that go `stale` also lose their `report-fact`
  tier and render untiered (B4), so the tier column of the tuple changes
  with them.
- [Unknown] How many claims land in each judge arm at the next live
  evaluation, and the byte cost on `/polaris` and on the machine answer.
  Added Unknown reasons, routes and the per-freshness counts add bytes; B10
  measures both host forms against the 2,097,152-byte ceiling and the
  1,650,000-byte working target (from the 2026-10-02 lane B direction), and
  the machine answer against `maxMachineResponseBytes` (16,777,216).
- [Inferred] When slice 5 lands with the registry act effective, the arm
  has no live member (B2, B10). Item depth fills it: every relation claim,
  one per contract band, is in the arm until a bound for
  `governing-intent-relation` is declared, so its byte cost lands with that
  lane. An ineffective registry act puts every claim of that evaluation in
  the arm.

## Interactions

- **Shared-model WIP one.** Slice 5 changes `PocModel`, so it queues behind
  the 2026-10-15 direction's chain; ordering is the coordinator's. [Inferred]
  B11 needs slice 5 ahead of item depth and of the opening band's count
  arm, because both use its mechanism.
- **The dov.35 successor (`syzygy-sin5`, PR #489).** [Observed] At its head
  `8c334f67` it authorizes no part of the missing-currency scenario, routes
  M2 slice 5 to this gate, makes item depth (`syzygy-dov.14.4`) and the
  opening band's no-bound count (`syzygy-dov.4.2`) wait for this act, and
  lets each be built only as far as this act names. The packet's B11 and
  its section "Composition with the 2026-10-20 direction (PR #489)" say how
  the two compose.
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
  `REVIEW-BRIEF.md`, and after review round 1 the sibling
  `ROUND-1-DISPOSITIONS.md`;
- after review round 1, the retained raw
  `docs/reviews/R-PWB-M2-SLICE5-CONTINUATION-PACKET-RAW.md`, its campaign
  row in `docs/README.md` and its campaign pattern in
  `scripts/check_docs_review_campaign_partition.py`.

No `.beads/` file, signed byte, act or sign-off record, recorder,
governance check, implementation file, status page or hosted workflow is
changed; the partition helper's campaign table is the one script edit, as
every retained raw requires. No register row is added to
`PENDING-OWNER-DECISIONS.md`; whether and when to queue one is the
coordinator's integration step.
