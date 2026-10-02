# Impact ledger — missing effective currency bound outside freshness

> **Candidate — binds nothing.** This ledger describes the effect of a possible
> PWB amendment under P-69 Q7a. It performs no act, edits no signed byte and
> authorizes no implementation.

**Baseline:** `49ef8fd` (`origin/main` when this repair began; the first draft's figures were taken at `9d741859dcee` and are superseded).

**Subject:** the closed eleven-artifact PWB behavioral package. Proposed bytes
are six patches under `proposed/`; the manifest hashes their post-apply result.

## Discovery method and denominator

[Observed] Method 1 enumerated every NUL-separated path from `git ls-files -z`
at `49ef8fd` and scanned each file's bytes decoded as UTF-8 with Python `re`
(`re.findall` over the whole file), counting files and occurrences.
Denominator: **1,772 tracked files**, of which four failed UTF-8 decoding and
were skipped, all PNG evidence captures:

- `docs/evidence/orrery-height-repaired-narrow-2026-09-09.png`
- `docs/evidence/orrery-height-repaired-wide-2026-09-09.png`
- `docs/evidence/polaris-existing-orrery-narrow-2026-09-09.png`
- `docs/evidence/polaris-existing-orrery-wide-2026-09-09.png`

The skipped predicate is decode failure, not "binary". [Observed] Method 2,
`git ls-files | wc -l` and `git grep -F -l PWB-REQ-007`, gives 1,772 and 119
files, agreeing with method 1 on both. The figures count the whole tree at
that commit, including this package, other candidate packages and retained
raw reviews; they describe a population, not a consumer list, and are not
re-derived after the commit that retains this repair's own review raw.

| Pattern (Python `re`, exact) | Files | Occurrences |
|---|---:|---:|
| `PWB-REQ-007` | 119 | 530 |
| `PWB-REQ-[^\n]*(?:, \|/\|\.\.\| and )007\b` (continuation forms ending in bare `007`) | 7 | 8 |
| `specs/polaris-project-wide-butlers-model/spec\.md` | 97 | 199 |
| `polaris-project-wide-butlers-model/GOVERNING-DEPENDENCIES\.md` | 24 | 41 |
| `no-currency-bound-declared` | 65 | 98 |
| `RFC2-10` | 96 | 391 |

[Observed] The seven continuation-form files and eight occurrences are:

- the `.18` registry semantic delta and its retained raw review;
- the dated PWB P2-7 mutation record;
- `docs/design/POLARIS-M13-NAVIGATION-SCALE-FUNNEL.md:1065`;
- `docs/design/POLARIS-M14-PROVENANCE-DEPTH-FUNNEL.md:108`;
- `docs/reviews/2026-09-05-pwb-live-exact-head-packet.md:84`; and
- `docs/reviews/R-POLARIS-M13-NAVIGATION-SCALE-FUNNEL-RAW.md:415-416`,
  which carries two occurrences.

They were inspected rather than silently excluded (re-listed from the first
draft; the count 7 / 8 reproduces at `49ef8fd`). The retained raw reviews are
counted and classified as review evidence; they are never edited.

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

## Composition with performed acts

[Observed] The opening-band, render-mode and machine-view amendments are applied
to the specification; this package's spec patch applies over them. The opening
band's scenario (PWB-REQ-010) has the aggregate disclose its own label, tier,
freshness and separate primary and secondary reason counts. A member with no
effective bound has no freshness value of its own; those members are
presented only through the same outside-slot named disclosure, with their count
and the stated reason, never as a freshness value of the aggregate; per-freshness
counts plus the count of members under the condition equal the membership, and
no value is derived from the other members. Lane B is
declined.
The generated dependency patch carries the digest of the proposed `spec.md` and
regenerates against the actual predecessor.

## Registry act (`syzygy-dov.18`)

[Observed] The registry-entry amendment act was performed 2026-09-30
(`PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md`). The entry now
carries thirteen `currencyBounds` rows and `currencyBoundSemantics`, whose
`undeclaredClass` arm returns Unknown with the closed reason
`no-currency-bound-declared` for a class with no row.

[Observed] This scenario is reachable only for a claim class with no row or
for a declaration whose owner-act provenance is missing or invalid. The two
packages touch different signed subjects, so no byte merge is required. This
package neither selects the registry's numeric values nor repeats them.

## Behavior-contract pins

[Observed] Two governed declarations pin the current signed PWB `spec.md`
digest in `governingBehaviorContract.version`:

- the Polaris Butlers project-shape observer registry candidate;
- the Polaris Butlers secret-classification policy candidate.

Any PWB successor stales both pins, including this package.
Neither pin is edited here. The registry pin stays a later registry act;
no authority read authorizes changing the policy candidate in this package. At adoption this remains an explicit
contradiction/gate, never an inferred repair.

## Generated dependencies and recorders

[Observed] `GOVERNING-DEPENDENCIES.md` changes only its source digest because
the new scenario has no warrants block. `CONTRACT-COVERAGE.md` changes only
the regenerated counts and repair-overlay digest. The builder imports the two
canonical generators and requires exact byte equality.

[Observed] The act is performed by version under
`OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`:
`scripts/record_versioned_signoff.py` validates the review, applies the six
patches, writes the sign-off record and appends one aggregate block. No typed
phrase or digest argument is involved.

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
