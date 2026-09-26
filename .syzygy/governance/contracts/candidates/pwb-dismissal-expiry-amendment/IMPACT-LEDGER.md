# Impact ledger — dismissal with a live expiry (PWB-REQ-007)

> **Candidate — binds nothing.** This ledger describes the effect of a
> possible PWB amendment under P-79 question 5. It performs no act, edits no
> signed byte and authorizes no implementation.

**Baseline:** `3ee61c7`.

**Subject:** the closed eleven-artifact PWB behavioral package. Proposed bytes
are six patches under `proposed/`; the manifest hashes their post-apply
result.

## Discovery method and denominator

[Observed] Method 1 listed every path from `git ls-files -z` at the baseline
and scanned each file's decoded text with Python, counting files and
occurrences. Denominator: **1,537 tracked files**. Four failed UTF-8 decoding
and were skipped, all PNG captures:

- `docs/evidence/orrery-height-repaired-narrow-2026-09-09.png`
- `docs/evidence/orrery-height-repaired-wide-2026-09-09.png`
- `docs/evidence/polaris-existing-orrery-narrow-2026-09-09.png`
- `docs/evidence/polaris-existing-orrery-wide-2026-09-09.png`

[Observed] Method 2, fixed-string `git grep -F`, reproduced the file and
occurrence counts for the first three rows and `RFC2-15`.

| Pattern | Files | Occurrences |
|---|---:|---:|
| `PWB-REQ-007` | 114 | 541 |
| `dismissed-by-decision` | 39 | 48 |
| `CHALLENGE_STATES` | 8 | 33 |
| `RFC2-15` | 45 | 150 |
| signed specification path | 72 | 163 |
| generated-dependencies path | 20 | 37 |

[Observed] Continuation forms (a bare `007` after a comma, slash, `..` or
`and`, on a line naming `PWB-REQ-` but not `PWB-REQ-007`): seven lines in six
files — the `.18` registry semantic delta and its retained raw review, the
M14 funnel, the dated P2-7 mutation record, the 2026-09-05 live exact-head
packet, and two lines of the retained M13 funnel raw review. All were read;
none states PWB-REQ-007's dismissal behaviour, so none needs a change here.
Raw reviews are never edited.

## The eleven subject rows

| Row | Effect |
|---|---|
| `.openspec.yaml` | unchanged |
| `CAPABILITY-COVERAGE.md` | row 32 added; totals 26 covered, 6 out of scope, 32 |
| `CONTRACT-COVERAGE-REPAIR-DELTA.md` | one row changed, eight added, totals line |
| `CONTRACT-COVERAGE.md` | regenerated: 625 rows, 143 covered, 236 Unknown, 246 believed not applicable |
| `GOVERNING-DEPENDENCIES.md` | regenerated: 99 distinct authorities (was 96) |
| three `contract-coverage-matrix/` files | unchanged |
| `design.md` | unchanged |
| `proposal.md` | one bullet added |
| `spec.md` | PWB-REQ-007 only: paragraph, Case, Oracle, Falsifier, two scenarios, warrants |

## Contract-coverage repair rows

Each new row splits a base row the audited matrix gave one disposition.

| Row | Supersedes | Disposition | Why |
|---|---|---|---|
| RFC6-17.r7 | RFC6-17.c2 | covered (was Unknown) | aggregates now count dismissed members separately and expand to them |
| RFC1-20.r1 | RFC1-20.c1 | covered | the paragraph and first scenario state the as-of-instant rule |
| RFC1-25.r1 | RFC1-25.c14 | covered | `dismisses`: reason and expiry mandatory, never green |
| RFC1-25.r2 | RFC1-25.c14 | believed not applicable | `challenges`/`adjudicates`: the POC has no challenge mechanism; base disposition kept |
| RFC2-1.r2 | RFC2-1.c12 | Unknown, uncovered | decisions affecting precedence are not made evaluation inputs by this change; left honest rather than claimed |
| RFC2-1.r3 | RFC2-1.c12 | covered | dismissal records are identified evaluation inputs |
| RFC2-15.r1 | RFC2-15.c2 | covered | the two exits, and facts staying visible beside the dismissal |
| RFC6-14.r4 | RFC6-14.c5 | covered | `dismissed-by-decision` travels beside the unchanged tuple in machine views |
| RFC6-14.r5 | RFC6-14.c5 | believed not applicable | the other sibling states and `challenge-pending`; base disposition kept |

[Inferred — a review point] RFC6-14.r5 keeps the base disposition, while the
existing RFC6-17.r2 says `unadopted-draft` is "used". A reviewer may find r5
should be Unknown instead. It is packet question 10.

## Consumers outside the subject

- **Implementation.** `dismissed-by-decision` occurs in no file under
  `apps/`, `packages/` or `scripts/`; `CHALLENGE_STATES` is unchanged. No code
  changes with this act. The M12 funnel names the files slice 4 would touch;
  none is edited. [Observed]
- **Pins of the current `spec.md` digest.** 19 tracked files carry it
  (full-digest and 12-character sweeps agree): the generated dependencies
  file, five sibling dependencies patches, the truth-policy manifest and its
  act, seven generator evidence records, the observer-registry candidate, the
  secret-classification policy candidate, and two retained raw reviews.
  Performed records and raws keep their history. The two candidates' pins
  would go stale on adoption; this package does not repair them. [Observed]
- **Sibling packages.** 15 declared composition outcomes, checked by the
  builder; see `SEMANTIC-DELTA.md`. [Observed]
- **Governance checks.** `check_governance.py` registers the phrase, the
  packet copy and an existence-gated act-record copy, with a selftest that
  the unperformed act registers no act-record copy. No `PWB_SUCCESSOR_CHAIN`
  link is added and CG-26's battery lists are untouched. [Observed]
- **Retention direction (2026-09-23).** Unchanged. Under the drafted arm a
  dismissal is not among the three retained per-claim fields. [Inferred]
- **Status pages.** `PROJECT-STATUS.md` and the pending register are not
  edited by this candidate. [Observed]

## Composition and regeneration

The spec patch uses one line of context, so it composes with `.20`, `.21`,
`.22` and `.30` in both orders. It collides with lane B's spec patch, `.20`'s
repair-delta totals line and generated coverage file, and every sibling's
generated dependencies patch. Each collision means: regenerate this package
with `--write` against whatever tree an earlier act leaves, then re-review.
[Observed: builder `--check`]
