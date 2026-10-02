# Impact ledger — dismissal with a live expiry (PWB-REQ-007)

> **Candidate — binds nothing.** This ledger describes the effect of a
> possible PWB amendment under P-79 question 5. It performs no act, edits no
> signed byte and authorizes no implementation.

**Baseline:** `3ee61c7`. The branch has since been rebased onto `08d4d02`
and then `96ee305` (PR #130); the sweeps below were run at `3ee61c7` and were
not re-run on either later base, so whether their counts changed there is
[Unknown]. The builder figures (coverage totals, composition outcomes) are
re-derived by `--check` on every base. [Observed]

**Subject:** the closed eleven-artifact PWB behavioral package. Proposed bytes
are six patches under `proposed/`; the manifest hashes their post-apply
result.

## Discovery method and denominator

[Observed] Method 1 listed every blob from `git ls-tree -r -z 3ee61c7`, read
each through `git cat-file --batch`, decoded it as UTF-8 and counted, per
pattern, the files containing it and Python `str.count` occurrences.
Denominator: **1,537 tracked files**. Four failed UTF-8 decoding and were
skipped (none contains any pattern as bytes), all PNG captures:

- `docs/evidence/orrery-height-repaired-narrow-2026-09-09.png`
- `docs/evidence/orrery-height-repaired-wide-2026-09-09.png`
- `docs/evidence/polaris-existing-orrery-narrow-2026-09-09.png`
- `docs/evidence/polaris-existing-orrery-wide-2026-09-09.png`

[Observed] Method 2, run for every row: `git grep -F -l -e <pattern> 3ee61c7
| wc -l` for files and `git grep -F -o -e <pattern> 3ee61c7 | wc -l` for
occurrences (`-o` prints one line per match; `-c` counts matching *lines* and
gives 515 for the first row, which is not an occurrence count). Both methods
give every figure below.

| Pattern | Files | Occurrences |
|---|---:|---:|
| `PWB-REQ-007` | 113 | 540 |
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
Raw reviews are never edited. The predicate as run: Python `re`,
case-sensitive, pattern `(?:,|/|\.\.|\band)\s*007\b`, over each decoded line
that contains `PWB-REQ-` and does not contain `PWB-REQ-007`.

[Observed, round-2 note N8] One further form lies outside both predicates:
a hyphen suffix `-007` after another identifier's stem, in 3 lines of 3
files (`docs/design/POLARIS-M11-OPERABILITY-FUNNEL.md:1658`,
`docs/evidence/polaris-m11-operability-funnel-2026-09-15.json:1011`,
`docs/reviews/R-POLARIS-M11-OPERABILITY-FUNNEL-2-RAW.md:66`). The round-2
reviewer found and read them; none states dismissal behaviour.

[Observed] Range forms, which the continuation sweep above does not reach:
Python `re` pattern `PWB-REQ-(\d{3}) ?(?:\.\.|…|–) ?(?:PWB-REQ-)?(\d{3})`,
case-sensitive, over the same 1,533 decoded files, keeping each range whose
endpoints bracket 007. 13 lines in 9 files carry a range; 7 lines in 6 files
span 007: `docs/PWB-IMPLEMENTATION-PLAN.md:1402` (`001…007`), the dated P2-7
mutation record, line 2 (`001..007`, already in the continuation list),
`packages/three-surface-poc-core/src/project-shape-model.ts:2` (`001…007`,
a file comment), two lines of the 2026-09-13 pursuit data file and one of
its harvest file (`001..022`), and
`docs/reviews/R-PWB-LIVE-EXACT-HEAD-TRUTH-RAW.md:72` (`001…022`). All were
read; each names a scope of requirements, none states dismissal behaviour,
and none needs a change here.

## The eleven subject rows

| Row | Effect |
|---|---|
| `.openspec.yaml` | unchanged |
| `CAPABILITY-COVERAGE.md` | row 32 added; totals 26 covered, 6 out of scope, 32 |
| `CONTRACT-COVERAGE-REPAIR-DELTA.md` | one row changed, twelve added, totals line |
| `CONTRACT-COVERAGE.md` | regenerated: 628 rows, 141 covered, 242 Unknown, 245 believed not applicable (was 622, 137, 237, 248) |
| `GOVERNING-DEPENDENCIES.md` | regenerated: 100 distinct authorities (was 96) |
| three `contract-coverage-matrix/` files | unchanged |
| `design.md` | unchanged |
| `proposal.md` | one bullet added |
| `spec.md` | PWB-REQ-007 only: paragraph, Case, Oracle, Falsifier, three scenarios, warrants |

## Contract-coverage repair rows

Each new row splits a base row the audited matrix gave one disposition. The
repair delta's declared totals become 92 rows, 77 superseded base rows, 65
covered, 22 Unknown uncovered and 5 believed not applicable (was 80, 71, 61,
16, 3). [Observed: builder `--check` and the coverage generator]

| Row | Supersedes | Disposition | Why |
|---|---|---|---|
| RFC6-17.r7 | RFC6-17.c2 | covered (was Unknown) | dismissed members stay in every per-label, tier, freshness and reason count and are additionally counted and expandable |
| RFC1-12.r1 | RFC1-12.c1 | covered | a dismissal bound to a claim identity the evaluation records as retired is never transferred and is disclosed as bound to a retired identity [Inferred: PWB specifies no split, merge or retirement record, so the class is unreachable today and the credit is conditional] |
| RFC1-12.r3 | RFC1-12.c1 | Unknown, uncovered | "re-dismissal is an owner act": the paragraph requires a new attributed human record, and whether that must be the owner is packet question 3 (round-3 note N-C1) |
| RFC1-12.r2 | RFC1-12.c1 | believed not applicable | challenges and claims across split or merge; no split or merge behaviour is specified, as the base row said |
| RFC1-20.r1 | RFC1-20.c1 | Unknown, uncovered (was believed not applicable) | the clause is about a gap; the paragraph states the rule for claims |
| RFC1-25.r1 | RFC1-25.c14 | Unknown, uncovered (was believed not applicable) | `dismisses` is typed Decision to Gap; the record names a claim |
| RFC1-25.r2 | RFC1-25.c14 | believed not applicable | `challenges`/`adjudicates`: the POC has no challenge mechanism; base disposition kept |
| RFC2-1.r2 | RFC2-1.c12 | Unknown, uncovered | decisions affecting precedence are not made evaluation inputs by this change; left honest rather than claimed |
| RFC2-1.r3 | RFC2-1.c12 | covered | every dismissal record present at the evaluation's snapshot is an identified input |
| RFC2-15.r1 | RFC2-15.c2 | Unknown, uncovered (was believed not applicable) | the clause is about a gap; the paragraph states the rule for claims |
| RFC6-14.r4 | RFC6-14.c5 | covered | `dismissed-by-decision` travels beside the unchanged tuple in machine views |
| RFC6-14.r5 | RFC6-14.c5 | Unknown, uncovered (was believed not applicable) | `challenge-pending` and `editorial-draft` travel; RFC6-17.r5 and RFC6-17.r8 already hold challenge state and `editorial-draft` in aggregates Unknown, so their travel cannot be believed not applicable here (round-2 note N7) |
| RFC6-14.r6 | RFC6-14.c5 | Unknown, uncovered | `unadopted-draft` travel; RFC6-17.r2 already calls that state used, so it cannot be believed not applicable here |

[Inferred] RFC1-20.r1, RFC1-25.r1 and RFC2-15.r1 stay Unknown because the
contracts dismiss a *gap* (RFC1-18 gives Claim and Gap separate identities;
RFC1-5 lists Gap as "V0 surfaces absence; V1 computes gaps"), while the
drafted paragraph binds a record to a claim. Reading an Unknown PWB claim as
the gap it discloses is an inference, and until the owner answers packet
question 4 no row may rest on it. The paragraph still states the full rule
for claims; only the contract credit waits.

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
- **Sibling packages.** 15 declared composition outcomes, each checked in
  both orders, plus one sequential run applying every composing sibling in
  table order (`.21`, `.30`, `.22`, `.20`) before this package; see
  `SEMANTIC-DELTA.md`. [Observed]
- **Governance checks.** `check_governance.py` registers the phrase, the
  packet copy and an existence-gated act-record copy, with a selftest that
  the unperformed act registers no act-record copy. No `PWB_SUCCESSOR_CHAIN`
  link is added and CG-26's battery lists are untouched. [Observed]
- **Retention direction (2026-09-23).** Not settled by this package. A
  dismissal is not among the three retained per-claim fields, but the first
  scenario requires a retained evaluation, read again later, to render the
  same claim state, which includes the dismissal's reason, expiry, author and
  record identity. That needs the record's bytes to stay reachable, or a
  fourth retained field. Packet question 7 routes this to the owner as a
  possible retention change. [Inferred]
- **Status pages.** `PROJECT-STATUS.md` and the pending register are not
  edited by this candidate. [Observed]

## Composition and regeneration

The spec patch uses one line of context, so it composes with `.20`, `.21`,
`.22` and `.30` in both orders. It collides with lane B's spec patch, `.20`'s
repair-delta totals line and generated coverage file, and every sibling's
generated dependencies patch. Each collision means: regenerate this package
with `--write` against whatever tree an earlier act leaves, then re-review.
[Observed: builder `--check`]
