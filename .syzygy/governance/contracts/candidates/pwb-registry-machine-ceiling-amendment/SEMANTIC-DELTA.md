# Semantic delta P-114 — raise the Butlers machine-answer ceiling to 16 MiB

> **Candidate — binds nothing.** Drafted by an agent lane (`syzygy-59s5`)
> under the owner's 2026-10-15 direction
> (`decisions/OWNER-DIRECTION-MACHINE-CEILING-2026-10-15.md`). That direction
> asks for this draft. It does not sign it. Only the owner signs (VIS-4).
> No act argument is quoted here. The manifest row is read with the
> builder's `--digests`.

**Artifact(s):** `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
(the Polaris Butlers project-shape observer registry entry), as patched by
`proposed/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json.patch`.

**Stable IDs affected:** none renumbered. One declared value moves:
`entries[0].resourceLimits.maxMachineResponseBytes`. PWB-REQ-006 (its
ceilings are declared by the registry entry) and POC-REQ-014 / PWB-REQ-020
(served by the machine answer this ceiling bounds) read it. Their text does
not change.

**Change class:** Normative. A declared resource limit is widened. A
machine answer between 8,388,608 and 16,777,216 bytes is refused today and
would be served afterwards.

**Author:** agent lane `syzygy-59s5` (Claude Code, Opus 5.5).

**Date:** 2026-10-20.

## Current meaning

The entry's `resourceLimits` block reads, at line 271 of the installed file:

```json
        "maxMachineResponseBytes": 8388608,
```

Its semantics, at line 281, unchanged by this delta:

```json
        "maxMachineResponseBytes": "the final encoded HTTP body for each authenticated Polaris machine JSON response",
```

A final encoded machine JSON body larger than 8,388,608 bytes is never
served. Under `resourceLimitSemantics.breachResult` the daemon answers with
the bounded typed failure (HTTP 503, `served: 'nothing'`, readiness false).

## Proposed meaning

```json
        "maxMachineResponseBytes": 16777216,
```

A final encoded machine JSON body of up to 16,777,216 bytes (16 MiB) is
served. Larger bodies get exactly the same typed failure as today. The one
value bounds both machine routes the daemon sends through it, `/api/poc` and
the Polaris presentation envelope `/api/poc/polaris` (`routes.ts`, both
`boundedResponse(..., 'maxMachineResponseBytes', ...)` calls).

## What explicitly does NOT change

Every other byte of the entry. The builder checks this twice: once on bytes
(exactly one literal replaced, one line differs) and once on parsed JSON (one
leaf differs, at `entries[0].resourceLimits.maxMachineResponseBytes`).
Named, because a reader might assume they moved:

- `maxHumanResponseBytes` stays 2,097,152. Polaris HTML and Trajectory HTML
  keep their ceiling. Trajectory's growth is handled as implementation under
  signed POC-REQ-042 (bead `syzygy-blbu`), not by this delta.
- `maxBriefingResponseBytes` stays 20,480. It stays "a separate and tighter
  ceiling, never a share of" the machine ceiling.
- `maxTotalBytes` stays 16,777,216, and the per-source, source-count, depth
  and parse-pass limits stay as they are. Input budgets are unchanged; this
  delta bounds output only.
- `resourceLimitSemantics`, including `breachResult` and the meaning of
  "final encoded HTTP body", is unchanged. Compression stays governed by the
  P-77 Q2 reading (`decisions/POLARIS-RESPONSE-CEILING-READING-DIRECTION.md`),
  which this delta does not touch.
- `observerVersion`, `registryVersion` and `discoveryVersion` stay
  `1.2.0-candidate.1` / `pwb-discovery-v2-candidate.1`. This is a drafting
  choice that **departs from the entry's own convention**, offered to the
  owner as such (packet, "Not asked here").
  - *The precedents.* [Observed] The 2026-09-05 amendment moved both
    versions from `1.0.0-candidate.3` to `1.1.0-candidate.1`. The `.18`
    currency-and-briefing amendment (`f5da19ff`) moved them to
    `1.2.0-candidate.1`; its delta calls that "a minor bump, matching this
    entry's own convention", and it too was a `resourceLimits` change. Only
    the 2026-10-02 re-pin act B (`144fa5f7`) changed the entry's bytes under
    the same version, and it was a pin repair with no change in behaviour.
    The closest precedent, `.18`, points the other way.
  - *Why depart anyway.* `.18` added a key (`maxBriefingResponseBytes`), so
    the entry's schema grew. This delta changes one value under an existing
    key, and the entry's exact digest, which the superseding record names,
    already distinguishes the bytes. A version move would also add the gate's
    `1.2.0-candidate.1` scope anchor (`governance-inputs.ts:116`),
    `PWB_OBSERVER_IDENTITY.observerVersion` (`project-shape-observation.ts:50`)
    and their test literals to an urgent change. And it would collide with
    the `1.3.0-candidate.1` that P-112 already proposes for the same entry.
  - *What it costs.* [Inferred] A reader comparing two entry versions cannot
    tell the 8 MiB bytes from the 16 MiB bytes by version string alone, only
    by digest or by act record.
  - If the owner prefers the convention, the version move is a mechanical
    redraft (`1.2.1-candidate.1`) plus the three sites above, and needs a
    new review round.
- `governingBehaviorContract` is unchanged. Round 6 of P-112 found the pin
  behind the current PWB `spec.md`. This delta neither repairs nor worsens
  that. The P-95 re-pin owns it.
- The read authority, input classes, consent, policy and egress are
  unchanged. No new Butlers content class, body read or provider egress.

## Warrant

The owner's direction of 2026-10-15, quoted in full in
`decisions/OWNER-DIRECTION-MACHINE-CEILING-2026-10-15.md`. The owner chose
"Both, ceiling first (Rec.)":

> Now: a registry-entry amendment raising maxMachineResponseBytes to 16 MiB,
> signed by version tag after one review. Then a POC-REQ-014 amendment
> serving the identical governedBy Unknown once per observation, by
> reference (~2 MB saved). P-86 waits for the raise.

Scope A (`decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`,
item 1) names "the observer registry entry" among the artifacts signed by
version tag.

## Evidence or decision basis

[Observed] `docs/evidence/syzygy-59s5-live-size-2026-10-20.json`. On
2026-10-20 a private daemon served from origin/main `8340fa22`, against
Butlers git revision `36f0e0eb`, answered `/api/poc` with HTTP 503. Its
stderr reports `observed` 8,497,943 against `declared` 8,388,608. The live
machine answer is therefore already refused (101.3% of the ceiling).

[Observed] The same 8,497,943 bytes come back at `0ba72000`, against the
same Butlers git revision and the same evaluation identity. That commit was
measured at 7,927,433 bytes on 2026-10-15
(`docs/evidence/p100-governing-intent-implementation-2026-10-15.json`,
`liveSizeAdmitted`).

[Inferred] The 570,510-byte growth in five days is therefore neither Syzygy
code nor the Butlers git tree. This assumes the answer is a deterministic
function of those inputs plus the live ones. The answer also carries
capture and evaluation instants from the daemon's clock, but those are a
few bytes. [Inferred, by elimination, as the evidence record labels it] The
growth comes from the one large live input outside the git revision: the
Beads Dolt read in `packages/three-surface-poc-core/src/work-items.ts`.

**Why 16 MiB.**

- *Growth rate* [Inferred: linear extrapolation over five days]: about
  114 KB per day of machine bytes. At the P-100 synthetic marginal of
  1,447 machine bytes per item, that is about 79 item-equivalents per day.
  The figure is soft, though. The evidence record notes that the machine and
  Trajectory marginals give about 394 and 261 item-equivalents over the five
  days, and the two disagree. Changed rows and items the board does not
  render are likely part of the growth. Syzygy's own records carry no Butlers
  work-item count, so the count itself is [Unknown].
- *Headroom at 8,497,943* [Inferred]: 16 MiB leaves 8,279,273 bytes, about
  72 days at that rate. The serve-once amendment (P-115, about 2 MB on
  today's population) lengthens that. Re-landing P-100 without P-115 costs
  about 2.55 MB (its own record), and P-86 adds project-shape bytes. Either
  shortens it.
- *Why not more* [Inferred]: 16 MiB is the smallest power-of-two step that
  restores months of headroom, and it equals the input budget
  `maxTotalBytes`. Doubling again would let the answer grow unexamined. The
  structural fixes are serve-once and paging.
- *Memory* [Inferred, from `apps/three-surface-poc/src/routes.ts`: the
  answer is `JSON.stringify(model)`, then measured and written]: one
  request holds the string (16 MiB for one-byte text, up to twice that if
  V8 stores it two-byte) plus the encoded body, so peak is on the order of
  50 MB. The daemon serves one owner on one tailnet, and V8's maximum string
  length is far above this.
- *Latency* [Inferred]: 16 MiB over a tailnet path of 10 to 100 Mbit/s is
  about 1.3 to 13 seconds per uncached fetch. Repeat fetches stay small
  because `/api/poc` revalidates (a weak `etag` and a 304 in `routes.ts`
  `machineHandle`), though the 304 path still serializes the whole model. [Unknown]: serialization time at
  16 MiB was not measured, because the 503 path never times a successful
  body.

## Terms introduced / retired

None.

## Downstream impact

Swept 2026-10-20 with ugrep (`-F` where load-bearing) over every tracked
text file outside `node_modules` and `dist`, for the literals `8388608`,
`8,388,608`, `8 MiB`, `8 MB` and the key `maxMachineResponseBytes`, plus a
dry run that applied the patch in the working tree and ran the whole
PROJECT-STATUS battery and the gate's own tests. `IMPACT-LEDGER.md` lists
every hit and every resulting failure.

The load-bearing finding is [Observed, dry run]: once the entry's bytes
change, the PWB-REQ-005 body-read gate refuses every Butlers read. Its test
(`governance-inputs.test.ts`, the direction-C case) returns `admits: false`.
The gate follows the 2026-10-02 act B, whose argument no longer matches,
until its registry act pointers move to the new record. The daemon also
hard-codes the ceiling (`PWB_RESOURCE_LIMITS` in
`packages/three-surface-poc-core/src/project-shape-observation.ts`), so the
signed value takes effect only through a code change. A parity test already
holds the two in step: `project-shape-observation.test.ts` ("observer
identity, limits and failure states are byte-equal to the act-bound registry
entry") fails on either one alone. The sign-off and that code change
therefore have to land in one commit, under a separate implementation
authorization (packet, ask 2).

The walkthrough evaluation identity also changes. It digests the resource
limits and the registry act's identity
(`walkthrough-readiness.ts` `walkthroughEvaluationIdentity`), so a
walkthrough record bound to today's `pwb-eval-…` identity then reads as an
evaluation mismatch. This is expected [Inferred].

## Migration / supersession plan

On sign-off, in one change:

1. Apply the patch. The entry then hashes to the manifest row.
2. Write the superseding `adopt-registry-entry` record in the form the gate
   reads. It supersedes act B for the registry role only, and act B's
   record, tag and bytes stay immutable history. Append its acceptance-act
   block and create the version tag `pwb-registry-machine-ceiling-amendment-v1.0`.
   That tag is the record's recording tag.
3. Under ask 2 only: move the gate pointers and the constant, update the
   test literals, and teach the four builder and recorder checks that read
   this subject to accept a later performed act's row (`IMPACT-LEDGER.md`,
   part B).
4. Re-run the battery and measure `/api/poc` on a private daemon from the
   committed tree.

Siblings: P-112 (loaded-profile) and the P-95 tree-framing re-pin patch the
same subject. Neither is performed. Whichever lands after this one is
regenerated over these bytes and reviewed again. Neither package is edited
here.

## Review

**Required class:** CC-REV-1 full review, fresh context, one round
(`REVIEW-BRIEF.md`).

**Reviewer:** a fresh-context agent session that did not author this.

**Verdict:** recorded verbatim in the round's raw under `docs/reviews/`.
Not restated here.
