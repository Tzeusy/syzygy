# Impact ledger — missing effective currency bound outside freshness

> **Candidate — binds nothing.** This ledger describes the effect of a possible
> PWB amendment under P-69 Q7a. It performs no act, edits no signed byte and
> authorizes no implementation.

**Baseline:** `9d741859dcee` (`origin/main` when drafting began).

**Subject:** the closed eleven-artifact PWB behavioral package. Proposed bytes
are six patches under `proposed/`; the manifest hashes their post-apply result.

## Discovery method and denominator

[Observed] Method 1 enumerated every NUL-separated path from `git ls-files -z`
at the baseline and scanned decoded bytes with Python `re`, counting files and
occurrences. Denominator: **1,376 tracked files**.

[Observed] Four files failed UTF-8 decoding and were skipped, all PNG evidence
captures:

- `docs/evidence/orrery-height-repaired-narrow-2026-09-09.png`
- `docs/evidence/orrery-height-repaired-wide-2026-09-09.png`
- `docs/evidence/polaris-existing-orrery-narrow-2026-09-09.png`
- `docs/evidence/polaris-existing-orrery-wide-2026-09-09.png`

[Observed] A separate NUL-byte method found six binaries: those four plus
`packages/three-surface-poc-core/src/owner-act-record.ts` and
`packages/three-surface-poc-core/src/project-shape-coverage.test.ts`. The latter
two decode and were swept. The skipped predicate is decode failure, not
"binary".

[Observed] Method 2 used fixed-string `git grep -F` against `HEAD` for the
literal forms and reproduced each literal file/occurrence pair. Continuation
forms were searched separately for `, 007`, `/007`, `..007` and `and 007`,
then restricted to lines containing `PWB-REQ-`, because this corpus writes both
full and abbreviated identifier runs.

| Pattern | Files | Occurrences |
|---|---:|---:|
| `PWB-REQ-007` | 90 | 443 |
| continuation forms ending in bare `007` after comma, slash, ASCII range or `and` | 7 | 8 |
| signed specification path | 65 | 142 |
| generated-dependencies path | 18 | 32 |
| `no-currency-bound-declared` | 54 | 78 |
| `RFC2-10` | 77 | 352 |

[Observed] The seven continuation-form files and eight occurrences are:

- the `.18` registry semantic delta and its retained raw review;
- the dated PWB P2-7 mutation record;
- `docs/design/POLARIS-M13-NAVIGATION-SCALE-FUNNEL.md:1065`;
- `docs/design/POLARIS-M14-PROVENANCE-DEPTH-FUNNEL.md:108`;
- `docs/reviews/2026-09-05-pwb-live-exact-head-packet.md:84`; and
- `docs/reviews/R-POLARIS-M13-NAVIGATION-SCALE-FUNNEL-RAW.md:415-416`,
  which carries two occurrences.

They were inspected rather than silently excluded. The retained raw reviews
are counted and classified as review evidence; they are never edited.

## The eleven subject rows

| Subject | Proposed disposition |
|---|---|
| `.openspec.yaml` | unchanged |
| `CAPABILITY-COVERAGE.md` | patched: row 16 names the outside-slot exception |
| `CONTRACT-COVERAGE-REPAIR-DELTA.md` | patched: five claims become `unknown-uncovered`; declared totals move |
| `CONTRACT-COVERAGE.md` | patched: exact regeneration over the repair delta |
| `GOVERNING-DEPENDENCIES.md` | patched: generated `spec.md` source digest only |
| `contract-coverage-matrix/RFC-0001-0003.md` | unchanged |
| `contract-coverage-matrix/RFC-0004-0006.md` | unchanged |
| `contract-coverage-matrix/RFC-0007-0009.md` | unchanged |
| `design.md` | unchanged |
| `proposal.md` | patched: project-level tuple obligation carries the same narrow exception |
| `specs/polaris-project-wide-butlers-model/spec.md` | patched: one scenario under PWB-REQ-007 |

[Observed] The manifest contains all eleven rows in codepoint order. A subset
manifest is rejected. The two generated outputs are checked against
regeneration, not accepted by transcribed digest.

## Contract and specification impact

[Observed] PWB-REQ-007's current universal freshness requirement is narrowed
for one condition. PWB-REQ-007, RFC2-9, RFC2-10 and CAP1-REQ-062 are quoted and
reconciled in `SEMANTIC-DELTA.md`.

[Observed] Five contract-coverage claims no longer have an honest PWB-REQ-007
coverage disposition: RFC6-14.r1/r3, RFC6-17.r1, RFC7-16.r1 and RFC7-33.r1.
Their authority bytes remain unchanged; the coverage layer marks them Unknown
uncovered. The generated totals move by exactly five, from 137/237 to 132/242
covered/Unknown, with the 622-row denominator fixed.

[Observed] `CAPABILITY-COVERAGE.md` remains 31 rows with 25 covered and six
lawfully out of scope. Row 16's wording changes; its disposition and totals do
not.

## Sibling composition

### Lane B (`syzygy-dov.17`)

[Observed] Lane B rewrites PWB-REQ-007's requirement, oracle, falsifier and
adds a scoped-field scenario. Applying lane B first and this minimal-context
scenario patch second succeeds. Applying this patch first makes lane B's wide
raw hunk stale. That is the declared order-sensitive case: if the owner
performs this package first, lane B must regenerate against the actual
predecessor before review/sign-off. No patch is force-applied.

### Opening band (`syzygy-dov.21`)

[Observed] The `.21` scenario lives under PWB-REQ-010 but cites
PWB-REQ-007's aggregate tuple. Its spec patch composes with this one in both
orders to identical bytes. Its own packet says its aggregate must expose
freshness counts; after this candidate, a member with no effective bound has
no freshness value to count. That is not silently resolved here: `.21` must
regenerate its impact reading against whichever predecessor is actually
performed, and implementation remains blocked.

### Other PWB candidates

[Observed] Machine-view and exact-source spec patches compose in both orders.
The exact-source capability-coverage patch also composes in both orders. All
four sibling generated-dependency patches collide with this package's patch,
as expected: each carries the digest of its own proposed `spec.md`. The later
package regenerates the file and its manifest against the actual predecessor.

## Parked registry checkpoint (`syzygy-dov.18`)

[Observed] `origin/agent/syzygy-dov.18` at `4d78776` was inspected without
merge. It is an unperformed candidate checkpoint: it proposes thirteen
currency-bound rows and a briefing ceiling in the registry entry. It is not
effective authority and cannot make a class current.

[Observed] This scenario remains reachable after that candidate only for a
claim class with no row or for a declaration whose owner-act provenance is
missing/invalid. The `.18` checkpoint and this package touch different signed
subjects, so no byte merge is required; their authority effects compose only
after separate owner acts. This package neither selects `.18`'s numeric values
nor repeats its proposed digest.

## Behavior-contract pins

[Observed] Two governed declarations pin the current signed PWB `spec.md`
digest in `governingBehaviorContract.version`:

- the Polaris Butlers project-shape observer registry candidate;
- the Polaris Butlers secret-classification policy candidate.

Any PWB successor stales both pins, including lane B, `.21` and this package.
Neither pin is edited here. The owner has already routed the registry
amendment through `.18`; no authority read this session authorizes changing
the policy candidate in this package. At adoption this remains an explicit
contradiction/gate, never an inferred repair.

## Generated dependencies and recorders

[Observed] `GOVERNING-DEPENDENCIES.md` changes only its source digest because
the new scenario has no warrants block. `CONTRACT-COVERAGE.md` changes only
the regenerated counts and repair-overlay digest. The builder imports the two
canonical generators and requires exact byte equality.

[Observed] No existing recorder can perform this act. Adoption needs a new
dedicated recorder that hard-codes the subject and reviewed packet head,
validates the exact phrase, writes
`PWB-MISSING-CURRENCY-DISCLOSURE-SCENARIO-ACT.md`, and appends one aggregate
record section. The recorder, record paths and successor-chain order are
adoption-time bytes; adding them now would assert an act not performed.

[Observed] Candidate-time registration is present in
`scripts/check_governance.py`: label, package subject, owner-packet digest
copy and existence-gated act-record copies. There is deliberately no
`PWB_SUCCESSOR_CHAIN` link before the owner chooses performance order.

## Documentation, status and hosted verification

[Observed] This branch does not edit `PROJECT-STATUS.md` or the hosted
workflow. CG-26 couples those two command lists and the stated total; all
parallel candidate builders are integrated there once, after branches are
combined. The integration change must add this builder's `--check` and
`--selftest` commands to both lists and recalculate the sentence.

[Observed] Default-path status remains unchanged: the candidate binds nothing,
the current signed PWB behavior remains effective, and M2 slice 5 remains
blocked. No narrative page may say the disclosure route renders before both
the spec act and separate implementation authorization.

## Implementation and consumer impact

[Observed] Direct implementation consumers are
`packages/three-surface-poc-core/src/project-shape-model.ts` and tests,
`apps/three-surface-poc/src/polaris.ts`, its copy and epistemic-tuple tests,
plus Capability 1's currency judge/conformance tests. None changes here.

[Observed] Current project-shape tuples still carry a constant freshness value;
the no-bound Capability 1 result still has no freshness. This candidate does
not wire the judge, alter HTML/data attributes, change machine JSON, or make
any route visible.

[Inferred] A later authorized implementation must model the outside-slot render
fact in both human and machine channels without inserting it into the claim's
freshness field, preserve exact reason/route/evaluation identity, and extend
aggregate/parity oracles so no favourable absorption is possible. Those are
implementation consequences, not authorization.

## Files changed by this preparation branch

- candidate package: semantic delta, impact ledger, owner packet, review brief,
  exact proposed patches and eleven-row manifest;
- read-only builder with `--check`, `--selftest`, `--diff`, guarded `--write`
  and adoption-gated `--apply`;
- candidate phrase/copy registration and its rule-6 selftest in
  `scripts/check_governance.py`;
- retained raw review only after an independent run.

No `.beads/` file, signed PWB byte, act record, recorder, implementation file,
status page or hosted workflow is changed.
