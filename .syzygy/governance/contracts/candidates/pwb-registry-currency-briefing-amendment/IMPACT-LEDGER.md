# Impact ledger — registry currency bounds and the briefing ceiling

> **Candidate review input — never authority.** Companion to
> `SEMANTIC-DELTA.md`. Binds nothing; only a superseding
> `adopt-registry-entry` owner act would give the proposed bytes effect.

Baseline: commit `a4a34510a5582edbd38c1df57a064ba3ac0a33f2`. The subject,
`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`,
is byte-identical at that commit and in the tree this package was drafted
in; `scripts/build_pwb_registry_currency_briefing_amendment.py --check`
fails if that stops being true, because the proposed diff would no longer
apply.

## Discovery method

Two independent sweeps, both run 2026-09-21 at the baseline commit
(verification rules 2 and 9). Nothing is sampled; every figure below is a
file count over a stated denominator.

1. **Python `re`** over the decoded UTF-8 text of every path returned by
   `git ls-files -z`, one pattern per identifier, counted per file.
   Non-UTF-8 and unreadable paths are skipped and are named in the
   remainder note below.
2. **`git grep -l -F`** over `HEAD` for each identifier as a literal,
   counted per file.

**Denominator: 1,334 tracked files.** `.beads/issues.jsonl` is untracked
and outside it; no bead is a consumer of these fields and none is read
here.

**The two methods return the same count for all fourteen identifiers.**
[Observed]

| Identifier | Method 1 | Method 2 |
|---|---|---|
| `currencyBounds` | 4 | 4 |
| `CurrencyBoundDeclaration` | 9 | 9 |
| `assessCurrency` | 18 | 18 |
| `no-currency-bound-declared` | 52 | 52 |
| `stale-beyond-currency-bound` | 38 | 38 |
| `resourceLimits` | 34 | 34 |
| `resourceLimitSemantics` | 19 | 19 |
| `maxMachineResponseBytes` | 23 | 23 |
| `maxHumanResponseBytes` | 33 | 33 |
| `maxBriefingResponseBytes` | 7 | 7 |
| `ResponseLimitIdentity` | 10 | 10 |
| `boundedResponse` | 28 | 28 |
| `registryVersion` | 2 | 2 |
| `observerVersion` | 31 | 31 |

A fifteenth sweep, over the subject's own basename stem
`POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE`, returns **43** files
by both methods. Those 43 are partitioned across the tables below, the
parts disjoint and the partition exhaustive: **10** in table 1, **3** in
table 2 (its fourth row, this package's own builder, is new and outside
the 43), **2** in table 3, **3** in table 5, and the remaining **25** in
table 6 — nine design funnels, six dated evidence records, three
2026-09-13 pursuit records and seven retained raw reviews.
10 + 3 + 2 + 3 + 25 = 43. [Observed]

**Remainders and the error term.** Three limits on these figures are
stated rather than hidden:

- A citation hard-wrapped across a line break inside a code span is
  invisible to a literal sweep. These identifiers are single tokens
  without path separators, so a wrap inside one is unlikely but not
  impossible; no wrapped-citation join pass was run for this package.
- Method 1 skips any path that does not decode as UTF-8. Method 2 does
  not decode, and returned the same counts, which is the second method
  doing its job: had a binary or non-UTF-8 file carried one of these
  identifiers, the two columns above would differ.
- The denominator excludes this package's own files, which were untracked
  when both sweeps ran. Adding them raises the denominator by **7** (five
  Markdown files, one manifest, one patch, one builder script — the patch
  and script counted as one each) and raises the `currencyBounds`,
  `currencyBoundSemantics`, `maxBriefingResponseBytes` and
  subject-basename counts accordingly. The tables below are the baseline
  tables and are not restated at the later commit; a reviewer wanting the
  later figures re-runs the two sweeps rather than reading them here.

## 1 — Governance authorities over the subject (10 of 43)

Every file in the 43 that is a governance record, packet or manifest
naming the subject. None is edited by this package.

| File | Relation | Disposition |
|---|---|---|
| `.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-ACT.md` | the original `adopt-registry-entry` act | Superseded for that role since 2026-09-05; preserved unedited, here and at adoption. |
| `.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md` | the act in force over the subject's current bytes | The act this package's proposal would supersede. Preserved unedited; its recorder is expected to fail its own `--check` after a successor lands, by design. |
| `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` | the aggregate transaction record | Gains exactly one aggregate section at adoption, written by the new act's dedicated recorder. Not touched here. |
| `.syzygy/governance/contracts/candidates/pwb-effect-acts/ACT-SEMANTICS.md` | the effect-acts packet's semantics | Frozen history of the 2026-09-02 transaction. No change. |
| `.syzygy/governance/contracts/candidates/pwb-effect-acts/PWB-EFFECT-ACTS-MANIFEST.txt` | that packet's manifest | Frozen. No change. |
| `.syzygy/governance/contracts/candidates/pwb-effect-acts/CANDIDATE-REPORT.md` | that packet's report | Frozen. No change. |
| `.syzygy/governance/contracts/candidates/pwb-effect-acts/OWNER-SIGNOFF-PACKET.md` | that packet's signoff | Frozen. No change. |
| `.syzygy/governance/contracts/candidates/pwb-truth-policy-amendment/PWB-EFFECT-AMENDMENT-MANIFEST.txt` | the 2026-09-05 amendment manifest | Frozen; it is the manifest whose registry row the act in force performed. No change. |
| `.syzygy/governance/contracts/candidates/pwb-truth-policy-amendment/IMPACT-LEDGER.md` | that amendment's ledger | Frozen. No change. |
| `.syzygy/governance/contracts/candidates/general-trusted-bootstrap-authorization/IMPACT-LEDGER.md` | classifies the subject among bootstrap-spent evidence | A row of its own package's transaction manifest, so its classification binds. No change. |

## 2 — Tooling that reads the subject or its act registry (4 of 43)

| File | Relation | Disposition at adoption |
|---|---|---|
| `scripts/check_governance.py` | holds the act label, subject path and amendment registries | **Changes at adoption, not here.** One new `PWB_EFFECT_AMENDMENT_ACTS` row (label, subject, predecessor record, new amendment record, act-time performed digest) and the existence-gated registration of the new packet's copy files. Why nothing is registered now is in `OWNER-DECISION-PACKET.md`. |
| `scripts/build_pwb_effect_acts_packet.py` | builds the frozen 2026-09-02 packet | No change; its subject bytes are immutable history. |
| `scripts/build_pwb_truth_policy_amendment.py` | builds the 2026-09-05 amendment manifest | **No change, and this is load-bearing.** Its manifest hashes the subject's *current* bytes. `--apply` in the adoption change moves those bytes, so that script's `--check` will disagree with the tree afterwards — expected, in the same way a superseded recorder's `--check` fails by design. A reviewer should confirm the owner accepts that, because it is a check that goes red without a defect behind it. |
| `scripts/build_pwb_registry_currency_briefing_amendment.py` | this package's builder | New in this package. Read-only; `--apply` refuses without `--at-adoption`. |

## 3 — Implementation that must change at adoption (6 files)

Derived from the `resourceLimits`, `resourceLimitSemantics`,
`maxMachineResponseBytes`, `ResponseLimitIdentity` and subject-basename
populations, restricted to `apps/**` and `packages/**`.

| File | Why it changes | Consequence if it does not |
|---|---|---|
| `packages/three-surface-poc-core/src/project-shape-observation.ts` | holds `PWB_OBSERVER_IDENTITY.observerVersion` and the seven-field `PWB_RESOURCE_LIMITS` as hard-coded copies of this entry | The parity test below fails. |
| `packages/three-surface-poc-core/src/project-shape-observation.test.ts` | asserts those two constants are byte-equal to the act-bound entry, reading the entry from disk | Suite red immediately after `--apply`. This is the hard gate that makes adoption one change. |
| `packages/three-surface-poc-core/src/git-object-reader.test.ts` | asserts the declared-limit name list has the same length as `Object.keys(PWB_RESOURCE_LIMITS)` | Suite red: the list is seven, the constant becomes eight. |
| `apps/three-surface-poc/src/routes.ts` | `ResponseLimitIdentity` is a closed two-literal union; `boundedResponse` is generic over it | The new ceiling has no identity to be enforced under. |
| `apps/three-surface-poc/src/response-limits.test.ts` | exercises the two current ceilings | The third ceiling is unexercised. |
| `apps/three-surface-poc/src/governance-inputs.ts` | hard-codes the registry act-record path and the act identity `PWB-OBSERVER-REGISTRY-ENTRY-ADOPTION-AMENDMENT-2026-09-05` | The daemon verifies the artifact digest against the named act record at runtime; leaving it pinned to the superseded record makes the authority read fail closed against bytes the owner has just adopted. |

`resourceLimitsDigest` in the first file is a SHA-256 over the canonical
JSON of the limits object and is carried in every observation identity, so
adding one field changes that digest for every evaluation. No test pins a
literal value of it at the baseline [Observed: the
`resourceLimitsDigest` population is the one file plus its own test, which
recomputes it].

## 4 — The judge and its conformance (4 files, no change at adoption)

| File | Relation | Disposition |
|---|---|---|
| `packages/cap1-core/src/staleness.ts` | defines `CurrencyBoundDeclaration` (`claimClass`, `maxAgeMs`) and `assessCurrency` | Unchanged. The proposed rows already match its declaration shape; adoption gives it an input it does not yet receive. |
| `packages/cap1-conformance/src/req-062.conformance.test.ts` | `CAP1-REQ-062` conformance over the judge | Unchanged; its expected values are hard-coded literals, not imports. |
| `packages/cap1-conformance/src/req-042.conformance.test.ts` | exercises `assessCurrency` | Unchanged. |
| `packages/three-surface-poc-core/src/project-shape-model.ts` | holds the constant that makes every claim render `fresh` today | **Unchanged at adoption.** Replacing it with a call to the judge is the implementing slice, which the ruling record blocks on further gates — including a plain continuation direction this package does not prepare. |

## 5 — Fixtures and versions that look like parity and are not (3 files)

Recorded because a reviewer will meet them and must not treat them as
either safe or broken.

| File | What it holds | Disposition |
|---|---|---|
| `packages/three-surface-poc-core/src/body-read-authority.test.ts` | a fixture carrying `registryVersion: '1.0.0-candidate.3'` | **Not a parity assertion.** It already differs from the entry's current `1.1.0-candidate.1`, so the version bump does not touch it. It is the only other tracked file carrying the `registryVersion` literal. |
| `packages/three-surface-poc-core/src/project-shape-manifest.test.ts` | reads the entry for `discoveryVersion` and `maxIndexDepth` | Unchanged: the diff moves neither. |
| `apps/three-surface-poc/src/walkthrough-inputs.ts` | lists the subject among the act-bound artifacts, by path only | Unchanged: it carries no digest, version or field name from the entry. |

## 6 — Design, evidence, review and pursuit material (25 of 43; no action)

The remaining 25 of the 43, and every file in the other fourteen
populations not already dispositioned above, are funnels under
`docs/design/`, dated evidence records under `docs/evidence/`, retained
raw reviews under `docs/reviews/`, and the 2026-09-13 pursuit records
under `docs/pursuits/`. **None is edited by this package or by adoption.**
Retained raw reviews are stored unchanged under CC-REV-6 in any case. The
funnels are where these fields were designed; the ruling record, not a
funnel, is this package's warrant, and where a funnel's recommendation and
the ruling differ the ruling governs — P-69 is exactly such a case, the
owner having taken arm B where the funnel recommended otherwise.

## 7 — Where each introduced term already occurs

No name in the diff is coined here. [Observed, from the table above]

| Introduced name | Tracked files carrying it at the baseline |
|---|---|
| `currencyBounds` | 4 — one funnel and three retained raw reviews |
| `currencyBoundSemantics` | within the `currencyBounds` population |
| `maxBriefingResponseBytes` | 7 — the ruling record, the decision history, one funnel and four retained raw reviews |
| `no-currency-bound-declared` | 52 |
| `stale-beyond-currency-bound` | 38 |

## Merge and effect boundary

Nothing in this package takes effect on merge. The subject keeps the bytes
the act in force bound; the manifest row is the digest of bytes that exist
nowhere in the tree; the builder is read-only unless given both `--apply`
and `--at-adoption`, and refuses even then if the package does not verify.
The adoption change is enumerated in `SEMANTIC-DELTA.md` under "Migration
and supersession plan" and is indivisible.
