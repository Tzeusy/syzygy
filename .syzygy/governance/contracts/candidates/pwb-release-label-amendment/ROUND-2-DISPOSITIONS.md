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
    *(Marked 2026-10-14: no longer true. The owner's direction of
    2026-10-14 ordered round 3, which read the repaired bytes and returned
    `REVISE`. See `ROUND-3-DISPOSITIONS.md`.)*
  - Every finding below is **open**, with the drafter's proposed repair. It
    goes to the owner as register row P-85.
- **The two carried wording notes.** The round-2 brief carried two notes from
  the PR 241 comments. The reviewer confirmed both: note 1 became Finding 1
  (revise) and note 2 became Finding 4 (note).
- **Drafter's recommendation.** Rule Q1 *Revise*: direct one new version that
  repairs Findings 1–6, and one fresh round over it. Q2–Q4 can be ruled now;
  Q4's answer settles the wording in Finding 4.

- **Repaired 2026-10-14 (owner-instructed).** The owner instructed one new
  version repairing Findings 1–6, then one fresh confirmation round — the
  drafter's recommendation above. Every finding is mapped to its repair
  under "Repairs, 2026-10-14" at the end of this record. The dispositions
  between here and there are kept as written on 2026-10-03; their **Open**
  marks describe the round-2 bytes. The repaired bytes are **unconfirmed**:
  no round has read them, and round 3 is pending. This record dispatches
  nothing.
  *(Marked 2026-10-14: "no round has read them" and "round 3 is pending"
  are no longer true; round 3 returned `REVISE`
  (`docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-3-RAW.md` line 4). The
  repaired bytes stay unconfirmed. See `ROUND-3-DISPOSITIONS.md`.)*

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

## Repairs, 2026-10-14

Made under the owner's instruction of 2026-10-14, over `main` at
`8f1fbec7`. Every repair is in the proposed bytes the builder applies, and
the generated patches and manifest were regenerated with `--write`, never
hand-edited. **Unconfirmed:** these repairs are what round 3 reviews; none is
"accepted" until it does.

| # | Finding | Repair |
|---|---|---|
| 1 | Not-read statement false under test 3 (revise) | Each not-read test now names its own statement: test 1 "release tags were not read", test 3 "the history needed to judge release tags was not read". The scenario, `SEMANTIC-DELTA.md`, the packet and design decision 12 (its form list and two flowchart nodes) say the same. A decide-line now checks "exact equality of form, statement, …", the machine answer's label record carries the test that applied and its statement, and the falsifier gains "a not-read or untagged label whose statement is not its test's". |
| 2 | `RFC4-11.r1` claims more than the fixtures observe (revise) | The fixture "a shallow clone whose captured history holds a reaching tag" is added (expected form: not read, since test 3 precedes test 4), and so is the falsifier limb "a count of later commits computed from incomplete ancestry". The r1 row is unchanged; the delta now names both shallow-clone fixtures as what observes it. |
| 3 | Naming-site denominator counts label-free sites (revise) | Polaris *names* the revision where its owner-visible text shows the full id, the twelve-digit prefix, or the project name followed by a captured tag name. Attribute values, link targets and identities are not owner-visible text and are left to the tag-name sweep. Each naming is one *label unit* (label, statement, full id, moved-tag disclosures), exposed as one element of the page. Sites are those occurrences plus the machine answer's label record, and the decide-line is "zero sites outside a label unit". |
| 4 | "Release tag" undefined (note) | The tag-set definition now says "These are the release tags the label counts", so the term follows the tag set and whatever Question 4 rules. The untagged statement is fixed as "no release tag reaches this revision". |
| 5 | Signed PWB-REQ-001 sentences extended and unguarded (note) | The spec patch now leaves every signed line of PWB-REQ-001 byte-identical: the Observable, Oracle-independence and Falsifier additions start on new lines. Only the doctrine and contracts warrant lines change. The builder applies the lost-line guard to the whole signed PWB-REQ-001 block, exempting only those two warrant lines, and checks that each list keeps every signed identifier. New selftest mutants delete a signed Oracle clause, edit a signed Falsifier clause and a signed Observable clause, and drop the signed SEC-3 warrant; each fails on its own predicate. |
| 6 | Moved tags on tied, unnamed tags; a single failed peel (note) | A moved tag is disclosed "wherever its name is carried": in a label, among the tied names in the machine answer, and in the surface's expansion of them. A fixture now has two tags tied at the revision, the later in codepoint order moved. "When any ref under `refs/tags/` cannot be read or peeled, reading the tag set failed", so test 1 applies, with the fixture "a tag set one of whose refs fails to peel while the others read". This fail-closed reading is a drafter's choice named in `SEMANTIC-DELTA.md` §"Choices the round-2 repair made". |

**Builder.** `REQUIRED_ONCE` gains one or more pinned phrases per finding.
The selftest now runs 30 structure mutants (19 before): 11 are new, and the
existing mutants were re-pointed at the repaired wording. `--check` and
`--selftest` pass. Requirement, scenario and contract-coverage figures are
unchanged: 17 requirements and 55 scenarios, and the regenerated
`CONTRACT-COVERAGE.md.patch` is byte-identical to round 2's.

**Left for the owner.** No finding needed an owner choice. The three
drafter choices named under Finding 6 and in the delta can be changed by answering Question 1 *Revise*.
