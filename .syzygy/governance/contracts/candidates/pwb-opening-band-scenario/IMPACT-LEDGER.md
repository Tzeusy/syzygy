# Impact ledger — the Polaris opening-band aggregate scenario

> **Candidate — binds nothing.** An agent drafted these bytes under the
> owner's 2026-09-21 direction recorded in
> `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
> (row P-71, arm A, question 7). That direction authorizes drafting only.
> This ledger records what an adoption **would** touch; it authorizes no
> edit, and only a dedicated owner act naming this package's manifest digest
> could give the proposed bytes effect.

**Baseline commit:** `a4a3451` (2026-09-21), the branch point of
`agent/gate-opening-band-scenario`. Every figure below was produced over the
tracked files of that commit, this session, except where a paragraph names
another population.

**Subject:** one scenario added under PWB-REQ-010 in the signed PWB
behavioral change. The delta is in `SEMANTIC-DELTA.md`; the proposed bytes
are the two unified diffs under `proposed/`.

---

## Discovery method

Stated so every figure can be re-derived rather than re-read (verification
rules 2, 4 and 9). A claim of absence with no denominator is not a finding.

**Population.** Every path returned by `ls-files -z` in this worktree,
decoded as UTF-8; paths that fail to decode are skipped.
**Denominator: 1,334 tracked files** at the baseline commit.

**Skipped paths, enumerated** (this paragraph replaces an earlier
unenumerated "none did", which was false — the review of 2026-09-21 found
it, and it is recorded in §Review finding 1). Re-derived by script,
2026-09-21, over the branch population of 1,343 tracked files — the baseline
1,334 plus this package's own eight files and the retained raw review.
**Four** paths fail UTF-8 decode and are skipped, all binary images under
`docs/evidence/`: `orrery-height-repaired-narrow-2026-09-09.png`,
`orrery-height-repaired-wide-2026-09-09.png`,
`polaris-existing-orrery-narrow-2026-09-09.png` and
`polaris-existing-orrery-wide-2026-09-09.png` [Observed]. None can carry any
of the five patterns below, so no reported figure moves.

**The remainder, stated** (rule 2's second method, which does *not* return
the same set). A NUL-byte scan over the same 1,343 files returns **six**
files: the four above plus `packages/three-surface-poc-core/src/owner-act-record.ts`
and `packages/three-surface-poc-core/src/project-shape-coverage.test.ts`,
which carry a literal NUL byte yet decode as UTF-8 and were therefore swept,
not skipped [Observed]. The decode-failure set is a strict subset of the
binary set; "binary" and "undecodable" are different predicates here, and
naming which one a skip figure uses is the difference between a number a
reader can check and one they cannot.

**Sweep 1 — Python `re`.** Five patterns, counted per file and per
occurrence:

1. the literal identifier `PWB-REQ-010`;
2. a continuation-form pattern for it: a requirement identifier
   `PWB-REQ-NNN` followed by a run of bare three-digit members, each
   introduced by a slash, a comma and a space, or a space, with `010` as any
   member — Python `re`, case-sensitive, no `DOTALL`, exactly
   `PWB-REQ-\d{3}(?:(?:/|,\s|\s)\d{3})*?(?:/|,\s|\s)010\b` — because the
   corpus writes identifier runs as `PWB-REQ-009, 010` and as
   `PWB-REQ-001/002/003/004/005/010`, and a full-identifier sweep alone
   produces a false absence. An earlier draft stated this pattern in words
   only ("a neighbouring requirement identifier followed by a bare `010`")
   and ran it over one member, which returns 0 files; the review of
   2026-09-23 found that the run form the corpus actually uses returns six
   (§Review finding 4). Re-run this session, 2026-09-23, at the baseline
   commit, with a second method (`-l -F` for the literal, and the same
   regex over `git ls-tree -r -z` blobs) agreeing on every figure;
3. the patched specification path;
4. the patched `GOVERNING-DEPENDENCIES.md` path;
5. the specification's current source digest, as a 64-hex literal. The
   digest is **not** reproduced anywhere in this package's prose: it is an
   argument component of a performed amendment act, and CG-7e and CG-15
   forbid copying it into a new artifact. Act records are cited by path.

**Sweep 2 — second method.** The repository's own fixed-string search
(`-l -F`) over the same literals; `grep` here is ugrep, so only `-F` is
trusted. The file sets agree with sweep 1 exactly, over the same 1,334-file
denominator [Observed, both run this session].

**What the method does not measure.** A citation hard-wrapped across a line
break inside a code span is invisible to a literal sweep. The identifiers
swept here are short and none of the patched paths appears in this package's
own prose in wrapped form, but the residual error term is real and is
declared rather than assumed away [Inferred].

---

## Results

| Pattern | Files | Occurrences |
|---|---|---|
| `PWB-REQ-010` | 36 | 110 |
| continuation forms of `PWB-REQ-010` (the regex above) | 6 | 7 |
| the patched specification path | 51 | 113 |
| the patched `GOVERNING-DEPENDENCIES.md` path | 9 | 13 |
| the specification's current source digest | 13 | 13 |

The continuation sweep adds **five** files the literal sweep misses; the
sixth run-form file, `docs/evidence/pwb-p4-2-mutation-sweep-2026-09-04.json`,
carries both forms. The five, every occurrence the literal
`PWB-REQ-001/002/003/004/005/010` or a shorter run ending the same way:
`apps/three-surface-poc/src/pwb-mutation-sweep-main.ts`,
`docs/evidence/pwb-p4-2-mutation-sweep-2026-09-04-parity-markers.json`,
`docs/evidence/pwb-p4-2-mutation-sweep-2026-09-06-parity-markers.json`,
`docs/evidence/pwb-p4-2-mutation-sweep-2026-09-09-named-absent-file-dropped.json`
and `docs/reviews/R-PWB-LIVE-EXACT-HEAD-ENGINEERING-RAW.md` (two
occurrences). **The citer population is therefore 41 files, not 36**
[Observed, 2026-09-23, both methods]. An earlier draft of this section
reported 0 / 0 and "adds no file"; both were false for the run form, and the
class 5 figures below moved with the recount. That the same section had to
be repaired twice — once for an unenumerated skip set, once for a
false absence — is why the predicate is now given as a regex a reader can
run rather than as a sentence.

---

## What changes, and what does not

### Class 1 — changed by this package (2 files)

Both as diffs under `proposed/`, never in place. CG-7h binds the current
openspec bytes to the latest performed act, so an in-tree edit would read as
drift on every run of the governance battery.

| Path | Change |
|---|---|
| the signed specification `spec.md` | one scenario inserted under PWB-REQ-010, after the existing scenario and before its `warrants` block |
| the generated `GOVERNING-DEPENDENCIES.md` | its source-digest line only |

The generated declaration's totals — 17 requirements, 96 distinct
authorities — do not move, because the new scenario adds no `warrants`
block and changes none. `scripts/build_pwb_opening_band_scenario.py --check`
regenerates the declaration from the proposed specification bytes and fails
if the proposed declaration differs, so a hand-edited generated file cannot
ride along.

### Class 2 — unchanged but inside the same bound subject (9 files)

The other nine artifacts of the eleven-artifact PWB behavioral package. They
are rows of `PWB-OPENING-BAND-SCENARIO-MANIFEST.txt` at their **current**
bytes, because a manifest over a subset would let a silent edit to a sibling
pass unnoticed. The builder's selftest asserts the population is closed in one sense only:
`BEHAVIOR_SUBJECTS` is a hard-coded tuple of eleven distinct paths, the
manifest hashes exactly those, and a change to any unpatched one fails
`--check` (the selftest's byte-drift fixture). The builder never lists the
change directory: a twelfth file appearing there is outside the bound
subject and is not hashed, so it neither fails `--check` nor enters the
manifest. An earlier draft claimed the opposite ("a new artifact appearing
in the change directory fails `--check`"); the review of 2026-09-23
falsified it with a one-line mutation (§Review finding 5) [Observed].

### Class 3 — digest-pinned elsewhere, staled by any amendment (2 files)

A finding of this sweep, recorded here because no other live ledger carries
it:

- `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
- `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`

Both pin the specification's current source digest in a
`governingBehaviorContract.version` field, each beside a `signedBy` value
that names a pending exact owner act over the PWB truth-and-readiness
amendment manifest. **Any** amendment to this specification stales both
pins — this package's, lane B's, and the P-69 Q7a clarification alike
[Observed].

This package does not edit either file, for two reasons. First, the owner
ruled on 2026-09-21, in the P-74 and P-78 rows, that the adapter-registry
entry is edited on no arm of those moves — P-78's row closes "The registry
entry is edited on no arm." and P-74's closes "The consent record, the
registry entry and PWB-REQ-005 are edited on no arm." (each quoted from
its own row; an earlier draft attributed P-78's sentence to both, §Review
finding 9). Each sentence closes its row's "What it means" cell as a summary
of the whole row, which answers several sub-questions; neither is scoped to
a numbered sub-question,
and an earlier draft of this ledger tagged it "Q4" in both rows. The
substance is the owner's; the per-question tag was this package's inference
and has been withdrawn (§Review finding 3). Second, P-69 Q2(a) and P-72 Q2 travel
together as one superseding registry-entry amendment act at gate bead
`syzygy-dov.18`, which is where a registry repair belongs [Observed for the
ruling rows; **[Inferred]** that the repair is that act's, since no record
read this session says so in those words]. **This is an owner-visible
consequence, not a resolved one.**

### Class 4 — history, never edited (4 files)

The performed PWB amendment act records, their manifests and the candidate
package that produced them quote the digests they bound at their own moment.
They are correct about that moment and are never rewritten. This package
cites them by path and quotes no act argument.

### Class 5 — citers carrying no obligation this scenario changes (39 files)

The remainder of the 41 `PWB-REQ-010` citers (36 literal plus the five the
continuation sweep adds): 41 less the two class-1 files, `spec.md` and
`GOVERNING-DEPENDENCIES.md`, is **39**. Two class-2 files carry the
identifier at `a4a3451` — `CAPABILITY-COVERAGE.md` once and
`contract-coverage-matrix/RFC-0007-0009.md` four times — and both are
counted below; neither class-3 file and no class-4 file carries it
[Observed — the eleven manifest rows, both JSONs and the four history
files each swept at `a4a3451`, round 4]. Re-derived 2026-09-23 by
re-running sweep 1 over the baseline tree and placing every hit in exactly
one kind; an earlier heading said 37 and left two citers in no kind
(§Review round 3, finding 13), and the round-3 repair then said only
`CAPABILITY-COVERAGE.md` was a class-2 citer (§Review round 4, finding
20). By kind, summing to 39:

- **Implementation and tests (6):** `apps/three-surface-poc/src/polaris.ts`,
  `polaris-first-reading.test.ts`, `polaris-project-shape.test.ts`,
  `polaris.test.ts`, `pwb-mutation-sweep.ts` and
  `pwb-mutation-sweep-main.ts` (the last lists identifiers in run form and
  carries no literal). Today's rendering satisfies
  the existing scenario and continues to satisfy it; the new scenario's
  antecedent is false of a page with no opening aggregate, so nothing here
  becomes non-conforming on adoption [Inferred — the mutation sweep was not
  run this session]. These sites change only when the owner separately
  authorizes slice 3, which this package does not do.
- **Generated coverage views inside the change (4):**
  `CAPABILITY-COVERAGE.md`, `contract-coverage-matrix/RFC-0007-0009.md`,
  `contract-coverage-parts/RFC-0007-0009.md`, `tasks.md`. Their PWB-REQ-010
  rows key off the requirement, not its scenario count, so no row moves. The
  first two are manifest rows (class 2); the other two are outside the bound
  eleven. An earlier sentence said the first alone was a row (§Review
  round 4, finding 20).
- **Design packets (2):** the M3 and M4 funnels. They are the drafting
  inputs, are read-only to this package, and are not edited by it.
- **Retained raw reviews (11)** and **dated evidence records (12)** — the
  ten `docs/evidence/*.json` hits and the two
  `docs/pursuits/2026-09-13-*.json` harvest records: never edited, under
  CC-REV-6 and the evidence-record convention. One raw and three evidence
  records reach this class only through the continuation sweep. An adoption
  does not make them wrong; they are true of their own commits.
- **The implementation plan and one dated review record (2):**
  `docs/PWB-IMPLEMENTATION-PLAN.md` and
  `docs/reviews/2026-09-09-polaris-editorial-repair.md`. The plan names the
  requirement in its first-reading slice and moves only as owner-authorized
  work advances; the dated record is true of its own commit and is not
  edited. Both were swept from the first draft and placed in no kind until
  2026-09-23 (§Review round 3, finding 13).
- **The pending-decision register (1):**
  `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`. Registering
  this package's sign-off as a queue row is the coordinator's merge-time
  edit, not this package's; the branch does not touch the register.
- **One other specification's design note (1):**
  `openspec/changes/polaris-manifesto-generation/design.md`, a cross
  reference with no obligation.

---

## Registration this package deliberately does not perform

**As of 2026-09-23 this section describes the branch as drafted, not the
tree.** The three edits below landed at the merge of PR #52 (`9d74185`,
2026-09-22), with one deliberate exception: the successor-chain link is
withheld until an act fixes the performance order (the note beside the
opening-band constants in `scripts/check_governance.py` says so). The owners
of that fact are `scripts/check_governance.py`, `PROJECT-STATUS.md` and
`.github/workflows/governance-docs.yml`, not this page.

Three edits are required before the governance battery can see this package
go stale, and all three are left to merge time because two of them are
coupled by CG-26 to a check-count sentence that every parallel package would
collide on:

1. `scripts/check_governance.py` — the act label, package directory,
   manifest subject, act-record path, a successor-chain link, an
   `_act_subjects()` entry, an `ACT_DIGEST_COPY_FILES` row for
   `OWNER-DECISION-PACKET.md` and an existence-gated activation function,
   all mirroring the lane B pattern.
2. `PROJECT-STATUS.md` §"How to verify this page" — two battery lines for
   the builder's `--check` and `--selftest`, plus the coupled check-count
   sentence.
3. `.github/workflows/governance-docs.yml` — the same two commands as CI
   steps.

Exact insertion sites are listed in `OWNER-DECISION-PACKET.md`. Until they
land, the builder's two commands were run by hand beside the canonical
battery this session and both pass [Observed]. (Landed 2026-09-22, chain
link excepted, per the dated note at the head of this section.)

---

## Composition with the other live offerings

`pwb-scoped-attributes-amendment` (gate bead `syzygy-dov.17`) proposes its
own diffs against the same eleven subjects. The two packages are independent
offerings and either may be adopted first, so the builder proves composition
rather than asserting it: `--check` applies lane B's specification patch and
this one in **both orders** in a scratch tree and fails if either order does
not compose. It composes at this commit [Observed].

The two `GOVERNING-DEPENDENCIES.md` patches do **not** compose, and that is
correct: both rewrite the one generated digest line, and a generated file is
regenerated after the second specification patch lands rather than patched
twice. `--selftest` asserts that collision, so the claim fails loudly if lane
B changes shape rather than going quietly stale.

The P-69 Q7a clarification scenario to PWB-REQ-007 (gate bead
`syzygy-dov.20`) and the P-75 Q1 three-surface package (gate bead
`syzygy-dov.26`) are not drafted at the baseline commit `a4a3451`. As of
2026-09-23 the first is drafted, as the sibling candidate
`pwb-missing-currency-disclosure-scenario/`, whose specification patch
inserts under PWB-REQ-007 (`spec.md` line 469) and composes with this
package's patch in both orders to one digest [Observed this session, by
`git apply` in a scratch tree; the builder asserts lane B composition
only]; the second is not. Both are named in `SEMANTIC-DELTA.md` as regions
this package must not enter, which is why the scenario is hosted under
PWB-REQ-010 and not under PWB-REQ-007 [Observed: the two gate rows; the
non-overlap is a drafting choice, and open question OQ-2 put the placement
back to the owner, who answered placement (A) on 2026-09-23].
