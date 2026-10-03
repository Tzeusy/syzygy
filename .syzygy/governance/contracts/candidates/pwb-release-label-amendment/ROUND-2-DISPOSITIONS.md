> # Record beside the package — not authority, binds nothing
>
> Dispositions of the second fresh-context review of the PWB release-label
> amendment package. This record is not a package artifact: the manifest does
> not hash it and no builder reads it. It offers nothing and performs no act
> (VIS-4).

# Round 2 dispositions — PWB release-label amendment

- **Reviewed commit:** `f0ad565e488432e42019c27d1e348419e5d4a892`. The
  package bytes there are those merged at `4c5c22a1`; the only later change
  is the round-2 section of `REVIEW-BRIEF.md`.
- **Verdict (raw line 4):** `REVISE`. The review has three revise findings
  (1–3) and three notes (4–6). Criteria 1, 2 and 3 are not met; criteria 4–7
  are met.
- **Stopping rule.** The owner's ruling of 2026-09-26
  (`decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`): a round clears
  the exact bytes it read when it returns `CONFIRM`, or
  `CONFIRM WITH EXCEPTIONS` with notes only, and its notes are dispositioned
  beside the package, never by editing those bytes. The coordinator's
  instruction for this bead adds: any other verdict sends the package to the
  owner with its findings open, and no third round is dispatched.
- **Applied here:**
  - The verdict is not notes-only, so **the bytes at the reviewed commit are
    not cleared.** This version is not offered for sign-off under Scope A
    item 3: "a package is offered only after a round that returns CONFIRM,
    or CONFIRM WITH EXCEPTIONS with notes only".
  - **Nothing in the package is edited.** Repairing a revise finding would
    produce new bytes that no round has read (rule 10), and repairing only
    the notes would leave the revise findings standing. The owner reads
    the bytes the reviewer read.
  - No round 3 is dispatched.
  - Every finding below is **open**, with the drafter's proposed repair. It
    goes to the owner as register row P-85.
- **The two carried wording notes.** The round-2 brief carried two notes from
  the PR 241 comments. The reviewer confirmed both: note 1 became Finding 1
  (revise) and note 2 became Finding 4 (note).
- **Drafter's recommendation.** Rule Q1 *Revise*: direct one new version that
  repairs Findings 1–6, and one fresh round over it. Q2–Q4 can be ruled now;
  Q4's answer settles the wording in Finding 4.

Reviewed record: docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-2-RAW.md

## Dispositions

### 1 — the not-read form mandates a false statement under test 3 (revise; carried note 1)

**Open.** Raw line 68. Test 3 is reached only after the tag set was captured,
yet every not-read form must state "release tags were not read". The packet
says the opposite ("the tags, or the history needed to judge them"), so the
owner would be shown one rule and sign another.

Proposed repair: state "release tags, or the history needed to judge them,
were not read" (or one statement per not-read test) in the proposed spec, its
scenario, `SEMANTIC-DELTA.md` and any design node that repeats it. Add a
decide-line that checks the statement's text.

### 2 — `RFC4-11.r1` claims coverage the fixture set cannot exercise (revise)

**Open.** Raw line 91. The only incomplete-ancestry fixture has no visible
reaching tag, so no implementation could produce a count from it. A
`git describe`-style count over a shallow history passes every listed
fixture.

Proposed repair: add the fixture "a shallow clone whose captured history
holds a reaching tag" (expected form: not read), or narrow r1 to the
never-say-untagged limb that the existing fixture observes.

### 3 — the naming-site denominator counts sites the requirement makes label-free (revise)

**Open.** Raw line 110. The denominator counts every element carrying the
full object id, but link targets, identities and per-fact revision stamps
lawfully carry it without a label. A conforming implementation would then
fail the oracle, or the checker would have to judge which elements "name"
the revision (CC-SPEC-4).

Proposed repair: define a naming site as the human-visible text presenting
the revision, plus the machine answer's label record. Leave identities and
link targets to the separate tag-name sweep.

### 4 — "release tag" is undefined while the rule counts every tag (note; carried note 2)

**Open.** Raw line 132. The reviewer found nothing renders false under either
Q4 answer and the oracle is unaffected, but the term is undefined in the
requirement text.

Proposed repair: say "no tag reaches", or define "release tag" as a tag in
the captured tag set, so the wording neither pre-empts nor contradicts the Q4
ruling.

### 5 — signed PWB-REQ-001 sentences are extended and the builder does not guard them (note)

**Open.** Raw line 145. Criterion 4 is met: every signed word survives as a
prefix. But `KEPT_IN_001` in the builder pins only the opening WHEN-sentence
and the signed scenario title.

Proposed repair: apply the lost-line guard already used for the companions
inside PWB-REQ-001, with a selftest mutant that deletes one signed
Observable, Oracle or Falsifier clause.

### 6 — moved-tag disclosure on tied, unnamed tags is unstated (note)

**Open.** Raw line 160. The text does not say whether a moved tag that is
tied but not shown first must be disclosed, and no fixture combines a tie
with a move. A tag ref whose peel fails while the rest of `refs/tags/` reads
is not plainly "reading it failed".

Proposed repair: state that a moved tag is disclosed wherever its name is
carried (the machine answer and the expansion included), add a tie-plus-move
fixture, and say which form a single failed peel yields.
