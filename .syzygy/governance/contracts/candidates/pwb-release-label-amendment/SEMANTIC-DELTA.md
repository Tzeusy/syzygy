# Semantic delta — PWB release-label amendment

> **Candidate — binds nothing.** This package proposes one amendment to the
> signed PWB specification. Nothing here is signed, adopted or labelled
> accepted, and no implementation is authorized (VIS-4). Only the owner's
> version-tagged sign-off binds it.

**Drafted:** 2026-10-03, bead `syzygy-l362`, over `main` at `0a10977b`.

**Repaired:** 2026-10-14, over `main` at `8f1fbec7`, under the owner's
instruction of that day (relayed by the lead session; no decision record
carries it): one new version repairing all six round-2 findings, then one
fresh confirmation round. The repairs are mapped in `ROUND-2-DISPOSITIONS.md`.
**These bytes are unconfirmed:** no round has read them, and round 3 is
pending. The account below describes the repaired version.
*(Marked 2026-10-14: "no decision record carries it", "no round has read
them" and "round 3 is pending" are no longer true. The direction is
recorded in
`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md`, and
round 3 read these bytes and returned `REVISE`
(`docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-3-RAW.md` line 4). The bytes
stay unconfirmed; see `ROUND-3-DISPOSITIONS.md`.)*

**Repaired again:** 2026-10-14 (cycle 2), over `main` at `814fbcc1`, under
the owner's direction of that day to run one more cycle (relayed by the lead
session): every round-3 finding, notes included, repaired once, then one
fresh review under the same stopping rule. The repairs are mapped in
`ROUND-3-DISPOSITIONS.md` §"Repairs, 2026-10-14 (cycle 2)". **Round-3
findings repaired once on 2026-10-14, unconfirmed pending round 4.**
*(Marked 2026-10-14, round 4: "pending round 4" is no longer true. Round 4
returned `REVISE` (`docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-4-RAW.md`
line 4), one revise finding and seven notes, all open in
`ROUND-4-DISPOSITIONS.md`. The bytes stay unconfirmed.)* The
account below describes this version. The base moved because the
anchor-resolution amendment (P-96) was signed v1.0 at `7f43802f`, which
changed the signed PWB `spec.md`; the derived patches and the manifest were
regenerated over it with the builder's `--write`.
*(Marked 2026-10-14, cycle 3: "The account below describes this version"
is no longer true of the cycle-2 version; it describes the cycle-3 version
named next.)*

**Repaired a third time:** 2026-10-14 (cycle 3), over `main` at `7460aec8`,
under the owner's direction of that day, given in the lead session by
structured question: "One more cycle each" for P-85 and P-98, that is,
repair every round-4 finding, notes included, then one fresh review under
the same stopping rule. The repairs are mapped in `ROUND-4-DISPOSITIONS.md`
§"Repairs, 2026-10-14 (cycle 3)". **Round-4 findings repaired once on
2026-10-14, unconfirmed pending round 5.** The account below describes this
version. The base moved again: the class-granular extraction amendment
(P-86) was signed v1.0 at `235b71eb` under its Question 5 answer "First
ready lands first". It changed the signed `spec.md`, `design.md`,
`proposal.md` and `CAPABILITY-COVERAGE.md`, and took design decision 12 and
capability row 34. This package's capability patch no longer applied, so
the authored patches were rewritten over P-86's applied bytes, as design
decision 13 and capability row 35. The derived patches and the manifest
were regenerated with `--write`.
*(Marked 2026-10-15, round 5: "unconfirmed pending round 5" is no longer
true. Round 5 returned `REVISE`
(`docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-5-RAW.md` line 4): one revise
finding (the citation predicate leaves the cite's visible text free, so a
sentence naming the revision can be cast as a citation) and seven notes, all
open in `ROUND-5-DISPOSITIONS.md`. The cycle-3 direction is recorded in
`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-3-2026-10-14.md`.
After round 5 the owner answered "One more cycle": one more repair and a
round 6, made by a separate change. These bytes are not cleared and are not
offered for sign-off.)*

**Repaired a fourth time:** 2026-10-15 (cycle 4), under the owner's answer
"One more cycle" to round 5, recorded in
`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-3-2026-10-14.md`.
Every round-5 finding and note is repaired once; the repairs are mapped in
`ROUND-5-DISPOSITIONS.md` §"Repairs, 2026-10-15 (cycle 4)". **Round-5
findings repaired once on 2026-10-15, unconfirmed pending round 6.** The
account below describes this version. The base moved: the accessible-name
(P-99) and opening-index (P-98) amendments were signed v1.0, so this
package's derived `GOVERNING-DEPENDENCIES.md.patch` and manifest were
regenerated with `--write` over their applied bytes, and no PWB sibling is
pending beside it (§"Pending siblings").
*(Marked 2026-10-15, round 6: "unconfirmed pending round 6" is no longer
true. Round 6 returned `REVISE`
(`docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-6-RAW.md` line 4): one revise
finding (a citation embedded in a sentence passes every decide-line, and
the named limit below is contradicted by "therefore never a stamp" and the
new scenario) and three notes, all open in `ROUND-6-DISPOSITIONS.md`. These
bytes are not cleared and are not offered for sign-off.)*

The cycle-4 change to the requirement, in short:

- **A cite's text is decided by equality (round-5 Finding 1).** The cite's
  whole visible text, whitespace-normalized, must equal the served locator
  of the anchor it names or the path of the source record it names. That
  text holds no whitespace, or it is a path in the checker's own Git
  listing of the observed revision, and it holds no occurrence the text
  sweep finds. A decide-line, a falsifier limb, an Observable addition and
  the scenario "A sentence naming the revision is not a provenance stamp"
  carry it. The reviewer's page, a sentence cast as a citation whose cite
  is "Declared project shape of butlers at revision", now fails: its cite
  text holds whitespace, is no path, and equals no served locator.
- **Named limit.** A served locator is the system under test's own output
  (PWB-REQ-014's anchor shape requires a locator and does not fix its
  values). The text bounds it to one whitespace-free token or a real path,
  but does not fix the token set, so a one-token locator chosen to read as
  a phrase is not decided here. [Inferred] Closing it needs a closed locator
  vocabulary in PWB-REQ-014, which this package does not amend.
- **The identity exception is closed (round-5 Note 1).** It covers exactly
  two records: the evaluation identity, and the source identity of one
  source record the machine answer serves at that evaluation. "These two
  are the whole population."
- **Guards (round-5 Note 2).** The builder's `REQUIRED_ONCE` now holds the
  new wordings, the identity exception's "not a revision's id alone"
  clauses in the requirement, decide-line and falsifier, the Observable
  addition and the page exclusions as one whole sentence, each with a
  selftest mutant.

**Repaired a fifth time:** 2026-10-15 (cycle 5), over `main` with P-98 and
P-99 signed, under the owner's answer to round 6, "Weaker wording + review
(Rec.)" ("Drop 'never a stamp', state both gaps as limits, then one review;
it comes back to you to sign."), recorded verbatim in
`ROUND-6-DISPOSITIONS.md`. **Round-6 findings repaired once on 2026-10-15,
unconfirmed pending round 7.** The account below describes this version.
In short:

- **"Therefore never a stamp" is withdrawn (round-6 Finding 1).** The
  requirement now says: "Two limits stay. Where a citation sits is not
  decided by this requirement", and "Which tokens an anchor's served locator
  holds is not decided either". The fifth scenario is renamed "A citation's
  contents are decided, not its placement"; its THEN covers the sentence
  outside a citation, and an AND states the placement gap. Question 6's
  recommended row no longer promises that the label leads wherever the
  revision is named. The "Named limit" bullet above is now carried by the
  requirement itself.
- **Guards (round-6 Note 1).** The six wordings the reviewer deleted without
  a content finding are in `REQUIRED_ONCE`, each with a mutant.
- **Design and delta carried (round-6 Note 2).** Design decision 13 names
  the cite-text rule, the two gaps and the closed identity population;
  §"What changes" here does the same and says five scenarios.
- **Naming defined by the sweep (round-6 Note 3).** The prohibition says its
  three namings are what "names the observed revision" means, and that a
  shorter prefix is not decided; design decision 13 says the same.

*(Marked 2026-10-15, round 7: "unconfirmed pending round 7" is no longer
true. Round 7 returned `REVISE`
(`docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-7-RAW.md` line 4): two revise
findings (the withdrawal is incomplete in the packet summary and in cycle-3
choice 1 below; an excepted identity placed in a sentence passes, uncovered
by the stated limits) and three notes, all open in
`ROUND-7-DISPOSITIONS.md`. These bytes are not cleared.)*

## The warrant

[Observed — read with `bd show syzygy-l362` on 2026-10-03] The bead records
the owner's direction of 2026-10-02 in its description:

> Owner direction 2026-10-02: a Syzygy site over a repository reads better as
> 'Butlers v1.0.23' than a sha, even at some cost in determinism. Design
> stance: the human surface leads with the release label (nearest tag/version
> the observed commit carries or is described by); the exact object id stays
> beneath it as the evidence the claim binds to, so a moved tag is detected
> rather than trusted. A commit with no release tag shows a short sha,
> honestly labeled. Touches PWB identity/freshness display (PWB-REQ-007/020
> tuple, Polaris, Trajectory, Orrery) so it needs the same governed change
> path (spec delta or the new version-tagged sign-off once it lands); no read
> or egress change.

[Observed] The direction lives only in the bead tracker. The tracker export is
not a tracked file, and no record under `.syzygy/governance/decisions/` carries
it (`git grep -i "release label"` over `.syzygy/` at `0a10977b` returns
nothing). The roadmap names it as "owner direction of 2026-10-02 on the bead"
(`docs/plans/2026-10-03-smooth-example-roadmap.md` line 177). The bead's notes
say the direction authorizes drafting only.

**The trade-off the owner accepted, preserved.** The owner wrote "even at
some cost in determinism". This package pays that cost in one place only: the
label is computed from the repository's tags, which can change while the
revision does not. It keeps determinism everywhere else by making every input
the label reads an identified evaluation input: the captured tag set, the
captured ancestry, and the earlier evaluations a moved-tag comparison reads.
So one identified evaluation always shows one label with one set of moved-tag
disclosures, and two evaluations that differ only in their tags are two
evaluations.

## The sign-off route

[Observed] The 2026-10-02 Scope A direction covers "the PWB specification
deltas, the observer registry entry and the contract successors queued behind
them" (`decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`,
direction item 1). This package is a PWB specification delta, so it is signed
by version tag. It is not yet registered in `scripts/record_versioned_signoff.py`
`real_packages()`; the signing change adds it.

## What changes

One requirement, PWB-REQ-001, plus its companions. Every other requirement is
byte-identical, and the builder checks that.

**PWB-REQ-001 (amended).** Every signed line of the requirement stays as it
is, and so does its one scenario. The only signed lines that change are the
two warrant lists, which gain identifiers and lose none; the builder checks
both. Added:

- **Release label.** Wherever Polaris names the observed revision, it leads
  with the release label and shows the full Git object id beneath it, on the
  same surface. Every claim, evaluation identity, link and comparison binds to
  the object id, never to a tag name. The label is a presentation of the
  revision identity, not a project-shape claim.
  - The *Polaris pages* are a closed population: the human HTML responses to
    `GET /polaris` and to every request of PWB-REQ-011's exact-source route,
    served or refused, in every mount form. The machine answer, PWB-REQ-020's
    derived machine views and generation draft view (which "carries no
    project-shape identity"), and the response to a human re-observation
    request are not Polaris pages.
  - Polaris *names* the revision only in a *label unit*: one marked element
    of the page holding the label, its statement, the full object id
    beneath, the expansion of any tied names and any moved-tag disclosure.
    A checker finds each unit by its mark, without judgment. Every Polaris
    page presents at least one.
  - *The label leads*, and this is now decided: within each unit the label
    precedes the full object id, and on each page the first visible id of
    the revision, or project name followed by a tag name, that the text
    sweep finds outside the shared status line lies in a label unit.
  - Outside a label unit, visible text may not show the revision's full or
    twelve-digit id, or the project's name followed by a captured tag name.
    Four marked kinds of element are excepted. The mark only lets the
    checker find each one; what the checker reads decides whether it is of
    that kind:
    - a *provenance stamp* is only the revision element of a *citation*: an
      element holding a cite and its stamp and no other letter or digit. The
      cite names, by identity, one anchor the machine narrative serves or one
      source record the machine answer serves, and the stamp's whole text is
      that record's revision, in full or its first twelve digits. The cite's
      whole text equals that record's served locator or path, holds no
      whitespace unless it is a real path, and holds no swept occurrence.
      Stamps carry no label. Two limits are stated in the requirement and
      not decided: where the citation sits (one placed inside a sentence
      passes), and which tokens a served locator holds;
    - an *identity* shown whole, whose text equals the evaluation identity
      the machine answer serves or the source identity of one served source
      record, and no other record's, and is not a bare revision id. This
      covers the page footer's evaluation
      identity and the exact-source route's source identity, both of which
      contain the full revision;
    - Butlers-declared text that PWB-REQ-014 keeps verbatim, or that the
      exact-source route serves under PWB-REQ-011. It stays byte-identical,
      so PWB-REQ-014's verbatim rule is never in conflict with this one;
    - the shared operability status line. No requirement of either
      specification names it; this requirement excepts it on Polaris and
      governs nothing else in it (§"Scope: Polaris only"; Question 5).

    Attribute values and link targets are not visible text; the tag-name
    sweep covers them.
- **Two captured inputs.** Each is a deterministic evaluation input with its
  own identity:
  - the captured tag set: every ref under `refs/tags/`, each paired with the
    object it peels to. These are the *release tags* the label counts, so
    the term is defined by the tag set and follows whatever Question 4
    rules. If any one ref cannot be read or peeled, reading the tag set
    failed;
  - the captured ancestry: the parent ids of the revision's history, complete
    only when every commit in it was read.

  Only names and object ids are taken. No tag message, signature or commit
  message is read into the model or rendered, and a tag peeling to anything
  but a commit reaches nothing.
- **Four forms, decided by five ordered tests:**
  1. *not read* — the tag set was not captured. Statement: "release tags
     were not read";
  2. *tagged* — one or more tags peel to the revision itself: "Butlers
     v1.0.23";
  3. *not read* — the ancestry is incomplete (a shallow or grafted clone, an
     unreadable commit or an unadmitted read). Statement: "the history
     needed to judge release tags was not read";
  4. *described* — the nearest reaching tag is some commits behind: the tag's
     name and the count of later commits;
  5. *untagged* — no tag reaches the revision: the project name and the first
     twelve hexadecimal digits, with the statement "no release tag reaches
     this revision".

  Each not-read form shows the first twelve hexadecimal digits, its own
  statement, and the reason `source-uncaptured-or-unreachable` and its route.
  Test 3 is reached only after the tag set was read, so it does not say the
  tags were not read. Neither form ever says "untagged". Ties are broken by
  codepoint order of tag name, and every tied name is carried in the machine
  answer and in the label unit's expansion.
- **Moved tags.** An evaluation names, as inputs, the earlier evaluations it
  is compared with. A tag one of them bound to a different commit is
  disclosed as moved, naming both commits, wherever its name is carried: in
  a label, among the tied names in the machine answer, and in the surface's
  expansion of them. Nothing presents a tag as unmoved: no label unit, label
  record or *block* of visible text holding a tag name carries one of five
  closed stability terms (`unmoved`, `not moved`, `unchanged`, `stable`,
  `still points`), and a fifth sweep checks this. A block is the nearest
  enclosing paragraph, list item, table cell, heading, caption or summary,
  read whole, so a tag name and a term in different inline elements are
  read together. The requirement says the list is closed and that a
  paraphrase outside it is not decided, and the falsifier limb names the
  terms rather than any presentation of stability.
- **Machine answer.** Its label record carries the form, the test that
  applied, the statement, tag name, distance, tied names, moved-tag
  disclosures, the identities of the three inputs and the full object id.
- **Verification.** Fixture repositories cover every form, ties at the
  revision and at a distance, an annotated tag with a distinctive message, a
  tag peeling to a tree, a tag set with one ref that fails to peel, two
  shallow clones (one hiding the only reaching tag, one whose captured part
  holds a reaching tag), a complete clone observed three ways (ancestry read
  not admitted while the tag-set read is, one commit made unreadable, a
  graft boundary imposed), one revision under two tag sets, a moved tag,
  and a moved tag that is tied at the revision but not shown first. Each of
  test 3's three conditions therefore has a fixture.
  - The denominator is the naming sites: every marked label unit on every
    Polaris page, plus the machine answer's label record. The label-unit
    predicates apply to page sites only; the record is decided by equality
    alone.
  - A separate text sweep counts every visible short or full id of the
    revision, and every project name followed by a captured tag name, with
    its position in document order. It decides that none lies outside a
    label unit and the four excepted elements, and that the first one
    outside the status line lies in a label unit. For each stamp the
    checker reads the citation around it and the record its cite names; for
    each identity, the served identity it must equal; each excepted Butlers
    text must equal its source.
  - As it builds each fixture the checker records the conditions it imposes:
    whether the tag-set and ancestry reads are admitted, which ref fails to
    read or peel, which commit is unreadable, and any shallow or graft
    boundary. Tests 1 and 3 are decided from those construction records,
    and tests 2, 4 and 5 from its own Git listing and commit count. Neither
    is taken from the observer's inputs, and it decides on exact equality,
    the statement included.
  - Its sweeps cover five things: tag names in identities and links, the tag
    message in served bytes, distinct identities for differing tag sets,
    every moved-tag disclosure, tied names included, and the terms
    `unmoved`, `not moved`, `unchanged`, `stable` and `still points` beside a
    tag name.
- **Five new scenarios.** A tagged revision; a revision no tag reaches; unread
  tags never shown as untagged; a moved tag disclosed; a citation's contents
  decided, not its placement.
  *(Updated 2026-10-15, cycle 5, for round-6 Note 2: this section read "Four
  new scenarios", an identity equal to "a served record's own `identity`",
  and "A revision id in a sentence, a heading or other running text is
  therefore never a stamp"; the fifth scenario came in cycle 4, the closed
  identity population in cycle 4, and the claim was withdrawn in cycle 5.)*
- **Warrants.** VIS-2 joins the doctrine list, and RFC2-2 and RFC2-24 join the
  contracts.

**Companions.**

- `proposal.md` gains one "What Changes" bullet.
- `design.md` gains decision 13, "Name the revision by its release label",
  with a flowchart of the four forms. (Decision 12 is P-86's, signed first.)
- `CAPABILITY-COVERAGE.md` gains row 35, covered by PWB-REQ-001. The totals
  become 29 covered, 6 lawfully out of scope, 0 Unknown, 35 in all. (Row 34
  is P-86's, signed first.)
- `CONTRACT-COVERAGE-REPAIR-DELTA.md` supersedes one base row, `RFC4-11.c4`,
  with two repair rows. See §"Coverage matrix".
- `GOVERNING-DEPENDENCIES.md` and `CONTRACT-COVERAGE.md` are regenerated over
  the proposed bytes.

## Anchors

Each contract claim is anchored to the clause it rests on (rule 8).

- **RFC2-2 — Uncaptured means uninfluential.** The clause reads "A source not
  identified in the snapshot must not influence any deterministic claim of
  that snapshot's evaluations"
  (`RFC-0002/snapshot-and-evaluation-core.md` line 112). The tag set, the
  ancestry and the compared evaluations are therefore identified inputs, and
  what is not captured yields the not-read form rather than an inference.
- **RFC2-24 — Twelve reasons, closed.** The not-read form uses
  `source-uncaptured-or-unreachable` verbatim, whose condition reads "A
  deterministic input capable of affecting the claim was not captured in the
  snapshot (RFC2-2), including observer failure and unreachable sources".
- **RFC4-11 — Git/VCS adapter.** Its reads include "repository identity →
  revision map; ref → tip map" and "commit facts (SHA, parents, …)". So the
  contract allows a Git adapter to read tag refs and commit parents. Whether
  *this* observer may read them is a separate question; see below. RFC4-11 is
  already in PWB-REQ-001's warrants.
- **RFC6-15 — Every answer is evaluation-stamped.** "Same evaluation + same
  filters ⇒ same answer". Making the tag set an evaluation input keeps this
  true for the label. RFC6-15 is already in PWB-REQ-001's warrants.
- **VIS-2.** It reads "No evidence means Unknown, not success. Nothing turns
  green, and no project is declared aligned, converged, or genome-complete …
  without current evidence" (`doctrine/vision.md` lines 133–135). "Untagged"
  is a claim of absence that needs a complete look. This is why both not-read
  tests come before the untagged form, and why they never say "untagged".

[Inferred] RFC1-10, "Identifiers are opaque; names are labels", is the same
idea: a tag name is a label and the object id is the identifier. But its scope
is "every declared class (Capability, Topology entry, Declared region,
Repository, Project, Proposal)", and a release tag is none of those. It is
therefore cited as an analogy only and is not a warrant (rule 5).

**Coverage matrix.** One base row moves. Every other row stands.

- **The row.** `RFC4-11.c4`, "Squash/deletion loss becomes reduced-fidelity PR
  facts", was believed not applicable because "No commit/PR/change-accounting
  history is rendered by this capability"
  (`contract-coverage-matrix/RFC-0004-0006.md` line 65). A described label
  renders a count of later commits, so that basis no longer holds.
- **The repair.** `CONTRACT-COVERAGE-REPAIR-DELTA.md` supersedes it with two
  rows:
  - `RFC4-11.r1`, "A count over commit history is computed only from
    completely captured ancestry and is never reconstructed from history the
    adapter cannot reach", covered by PWB-REQ-001. It rests on RFC4-11's
    words "it never reconstructs commit history it cannot reach". Two
    fixtures observe it: the shallow clone whose missing history holds the
    only reaching tag (no untagged statement), and the shallow clone whose
    captured history holds a reaching tag, where a count over the partial
    history would give a described label and the expected form is not read.
    In both, the checker takes the not-read expectation from its own record
    of the shallow boundary it imposed, so the oracle can compute it. The
    falsifier names "a count of later commits computed from incomplete
    ancestry". Since the cycle-3 repair, the three complete-clone fixtures
    (ancestry read not admitted, an unreadable commit, a graft boundary)
    observe the same consequence for the other two ways history can be
    unreachable.
  - `RFC4-11.r2`, the PR-fact consequence, still believed not applicable.
    No PR fact is rendered.
- **Totals.** The repair delta declares 94 rows over 78 superseded base rows.
  The regenerated summary reads 629 effective rows: 137 covered, 247 Unknown
  uncovered and 245 believed not applicable. The generator's `--check` passes
  over the proposed bytes.
- **Rows that stand.** The two new warrants, RFC2-2 and RFC2-24, add no
  covered row. [Inferred] The existing rows for RFC2-2 (`.c1`
  unknown-uncovered, `.c2` covered by PWB-REQ-003) and RFC2-24 stand, and
  this amendment claims no new coverage for either. `RFC6-15.c2` ("no
  repeated-answer oracle exists") stays unknown-uncovered; the
  twice-observed fixture compares identities, not repeated answers.

## The read the owner's direction did not see

**[Observed] Deriving the label needs a read the observer is not admitted to
make.** The direction says "no read or egress change". There is in fact no
egress change. There is a read change.

- The observer's registry entry
  (`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`)
  bounds `typedAuthority.readAuthority` to: "phase A reads only the fixed root
  index, its declared pillar README indexes and Git tree metadata needed to
  derive the manifest; phase B reads only normalized repository-relative paths
  addressed as exact Git objects in that revision-bound manifest".
- Its `inputClasses` are `git-revision`, `repository-locator-mapping`,
  `git-object-database`, `governing-behavior-contract`, `git-tree-entry`,
  `git-blob`, `project-shape-source-manifest`, `observation-consent`,
  `secret-classification-policy`, `observer-registry-entry` and
  `resource-limits`. None of them is a tag ref or commit ancestry.
- [Observed] Today's implementation resolves only `rev-parse HEAD` in the
  observed repository (`apps/three-surface-poc/src/git-observation.ts` lines
  62 and 106 at `0a10977b`; re-measured 2026-10-14 at `814fbcc1`: lines 62,
  106 and 161, all `rev-parse HEAD`, and no `refs/tags` read).

Every form but not-read needs the tag set. The described and untagged forms
also need complete commit ancestry: the first to count commits back to a tag,
and the second to know that no tag lies anywhere behind. So:

- **If this package is signed alone,** every label takes the *not-read* form
  until a registry amendment admits those reads. That is lawful and honest,
  but it shows the owner no release label.
- **To see "Butlers v1.0.23",** the registry entry also needs an amendment
  admitting tag refs (names and peeled object ids) and commit ancestry
  (parent object ids). No tag message, signature or commit message is
  admitted. Scope A covers that amendment too. The packet puts this choice to
  the owner as Question 2. This package does not draft that amendment.

## Scope: Polaris only

The direction names Polaris, Trajectory and Orrery. **This package changes
Polaris and the machine answer only.**

[Observed] Trajectory and Orrery are governed by
`openspec/changes/three-surface-poc-experience/`, not by the PWB
specification. Their revision display is POC-REQ-001's. Today's renderers show
the first twelve hexadecimal digits in the shared page footer
(`apps/three-surface-poc/src/page-shell.ts` line 41) and in Orrery's eyebrow
(`apps/three-surface-poc/src/orrery.ts` line 187).
*(Marked 2026-10-14: those line numbers were measured at `0a10977b`, and
"footer" was wrong. Re-measured at `814fbcc1`: the prefix is in the shared
operability status line, `humanStatusLine` at `page-shell.ts` line 47,
rendered between the page header and the main content (line 127), and in
Orrery at `orrery.ts` lines 197 and 212. Trajectory's eyebrow carries it
too, at `trajectory.ts` line 236.)*

**One shared component reaches Polaris.** [Observed at `814fbcc1`] Polaris
renders the same status line through `pageShell({ …, status })`
(`apps/three-surface-poc/src/polaris.ts` lines 1870–1882), so on Polaris it
shows the observed revision's twelve-digit prefix. A single shared component
cannot owe a label unit on Polaris and a short id on Trajectory and Orrery
without a surface switch inside a POC-governed file. This version therefore
excepts the status line by name from PWB-REQ-001's visible-id prohibition,
leaves it to the POC specification, and changes nothing in `page-shell.ts`.
*(Marked 2026-10-14, cycle 3: "leaves it to the POC specification" claimed
more than either specification says. Round 4 swept `openspec/**` and found
no POC requirement naming the line (raw Note 3). [Observed at `7460aec8`]
The terms `operability`, `status line` and `page shell` return no hit in
the POC spec. The amended text now says so: no requirement of either
specification names the line, and PWB-REQ-001 excepts it on Polaris and
governs nothing else in it. So its revision display on Polaris is governed
by neither specification, which Question 5 now states. The mark: [Observed
at `7460aec8`] the line's element already carries the attribute
`data-human-status` (`page-shell.ts` line 55), which [Inferred] can serve as
its mark, so the exception needs no change to `page-shell.ts`. The
requirement names no attribute, as the signed spec names none.)*
Question 5 asks the owner whether the Polaris status line should carry the
label unit instead, which would touch that POC-governed component and so
interacts with Question 3.

The POC specification already has one open amendment package, the identity
amendment in register row P-84, and the owner was advised to answer it with
Revise. An OpenSpec change must overlap no other change, so a second POC
package now would collide with it. The packet asks the owner (Question 3)
whether the release label should join P-84's revision or wait for a
successor after P-84 is disposed of.

## Departures from the direction, named

1. **"No read change"** is not true of the label (above). The package says
   so, keeps the not-read form honest, and asks the owner how to proceed.
2. **Trajectory and Orrery** are out of this package (above).
3. **"Moved tag detected"** is detected only against earlier evaluations that
   an evaluation names as compared inputs. [Observed] No retained evaluation
   exists in the implementation: `git grep -i -E 'retained[- ]evaluation|retainedEvaluation'`
   over `apps` and `packages` at `0a10977b` returns nothing. Until one does,
   an evaluation can name none, and the moved-tag limb never fires. What
   still holds is that nothing binds to a tag and the full object id is
   always shown, so a reader can compare ids. The specification forbids
   stating that a tag is unmoved.
   *(Marked 2026-10-14: the reason above is stale. Re-measured at
   `814fbcc1`: the same grep still returns nothing, but
   `packages/three-surface-poc-core/src/reevaluation.ts` (last changed
   `c069f5f5`, 2026-10-03) records "the identity it supersedes" (line 5)
   and says "the prior one stays nameable beside it" (line 23), so an
   evaluation can already name an earlier one, the natural carrier for a
   compared evaluation. The conclusion stands for another reason: no
   evaluation captures a tag set — `git-observation.ts` reads no
   `refs/tags` at that commit — so a compared evaluation holds no tag
   binding to compare, and the moved-tag limb cannot fire until the read
   in Question 2 is admitted and implemented.)*
4. **Which tags count.** The package counts every ref under `refs/tags/`. A
   project whose non-release tags sit there would see them as labels.
   [Unknown] Butlers' tag population was not read, since reading it is the
   read this package is waiting on. Question 4 offers a declared tag pattern
   instead. The text calls the counted tags *release tags* and defines them
   as the captured tag set, so the label's statements stay true under either
   answer, and a pattern would change only the tag-set definition.
5. **The direction names "PWB-REQ-007/020 tuple"; this package amends
   PWB-REQ-001 only.**
   - PWB-REQ-007 governs "Every project entity and project-fact claim" and
     its epistemic tuple. The label is not such a claim: it is a
     presentation of PWB-REQ-001's revision identity, and the amended text
     says so ("not a project-shape claim or fact").
   - The not-read form uses an RFC2-24 reason and route as a disclosure
     beside the revision, the same way PWB-REQ-001 already discloses its
     inputs, without minting a tuple.
   - PWB-REQ-020's parity covers what Polaris presents. PWB-REQ-001 already
     requires that human and machine readers receive the same identities,
     and the amendment adds that the machine answer carries every label
     value.
   - [Inferred] So neither requirement needs new text. An owner who wants
     the label inside PWB-REQ-007's tuple, so that it is challengeable and
     carries a tier, can answer "Revise".

## Pending siblings

[Observed 2026-10-14 at `8f1fbec7` plus this repair] Four unsigned packages
also patch the PWB spec: the accessible-name (P-99), anchor-resolution
(P-96), class-granular extraction (P-86) and opening-index (P-98)
amendments. This builder's `--check` applies all five spec patches in every
order and requires one result, and each sibling builder's `--check` passes
over this repaired patch.
*(Marked 2026-10-14: no longer the population. P-96 was signed v1.0 at
`7f43802f` and is now a performed sibling. [Observed at `814fbcc1` plus the
cycle-2 repair] Three unsigned packages remain: accessible-name,
class-granular extraction and opening-index. This builder's `--check`
applies all four spec patches in every order and requires one result, and
passes. Each of the three sibling builders' `--check` fails at `814fbcc1`
before reaching the order check, on its own derived
`GOVERNING-DEPENDENCIES.md.patch`, which P-96's sign-off made stale; they
are being regenerated on their own branches.)*

Class-granular also adds design decision 12 and
capability row 34, so whichever of it and this package is signed second is
regenerated over the first's applied bytes and reviewed again (P-86's
Question 5).
*(Marked 2026-10-14, cycle 3: the population above is no longer current.
P-86 was signed v1.0 at `235b71eb`, first, so this package is the second
and was regenerated over P-86's applied bytes as decision 13 and row 35;
round 5 is its fresh review. [Observed at `7460aec8` plus the cycle-3
repair] Two unsigned packages remain over the PWB spec, accessible-name
and opening-index. Each patches only `spec.md` and the derived
`GOVERNING-DEPENDENCIES.md`. This builder's `--check` applies the three
spec patches in every order and requires one result, and passes. It now
runs the same search over every companion subject this package patches
(`design.md`, `CAPABILITY-COVERAGE.md`, `proposal.md`, the repair delta)
that a pending sibling also patches; today none does. It also requires the
design decisions and the capability rows to stay numbered 1..n, which is
what a silent duplicate number would break (round-4 Note 8). Both sibling
builders' `--check` fail at `7460aec8` before reaching their order check,
on their own derived `GOVERNING-DEPENDENCIES.md.patch`, which P-86's
sign-off made stale; they are regenerated on their own branches.)*
*(Marked 2026-10-15, cycle 4: the population above is no longer current.
The accessible-name amendment (P-99) and the opening-index amendment (P-98)
were both signed v1.0 on 2026-10-15 and are performed siblings, so no
unsigned package patches the PWB spec beside this one. This builder's
`--check` order search now runs over this package's patches alone, and its
`--selftest` adds a synthetic pending sibling so the order checks are still
exercised. Round-5 Note 7's three observations are therefore all
historical: the two sibling builders it measured are performed, and the
three `GOVERNING-DEPENDENCIES.md.patch` files it found not to compose are
derived and regenerated at each sign-off, so they never need to compose.)*

## Choices the round-2 repair made

The drafter made three choices while repairing round 2. None needs a ruling
before round 3, and each can be changed by answering Question 1 *Revise*.

1. **One ref that fails to peel makes the whole tag set unread.** The
   alternative, dropping that ref and judging the rest, could state
   "untagged" when the dropped tag was the one that reaches (VIS-2). The
   fixture "a tag set one of whose refs fails to peel while the others read"
   observes it.
2. **The three statements are worded exactly in the requirement**, so the
   oracle compares them by string equality and no reviewer has to judge
   whether a statement is true.
3. **A label unit is exposed as one element of the page.** This is a markup
   obligation on the implementation. It is what lets the naming-site sweep
   decide "inside a label unit" without judgment.

## Choices the cycle-2 repair made

The drafter made four more choices while repairing round 3. Each can be
changed by answering Question 1 *Revise*; the one that needs an owner
content choice is put as Question 5 instead.

1. **A naming site is a marked label unit, and every Polaris page has at
   least one.** The visible-id rule is then a separate prohibition with
   three marked exceptions, so the checker never judges which visible id
   "names" the revision. The floor of one unit per page is the drafter's
   reading of "the human surface leads with the release label".
2. **Provenance stamps carry no label.** A per-claim stamp is the identity
   that claim binds to, which the direction keeps "beneath" the label. A
   label unit per anchored claim would repeat the label once per claim and
   [Inferred] press on the `/polaris` response ceiling. Each stamp's whole
   text must be a revision id, so a stamp cannot hide a naming.
   *(Marked 2026-10-14, cycle 3: "so a stamp cannot hide a naming" did not
   hold and is withdrawn. A bare id is exactly what a naming looks like,
   and the kind was decided by the implementation's own mark (round-4
   Finding 1). Choice 1 of the cycle-3 repair replaces it.)*
3. **Butlers-declared verbatim text is excepted, and PWB-REQ-014 wins.**
   Butlers text that holds "Butlers" followed by a tag name stays verbatim
   and byte-identical; it is never a naming site. [Unknown] Whether any
   Butlers source holds such text was not read.
4. **Stability is swept by a closed term list** (`unmoved`, `not moved`,
   `unchanged`, `stable`, `still points`) over each label unit, the label
   record and every other visible text node holding a captured tag name.
   As with PWB-REQ-012's prohibited terms, the list is closed, so a
   paraphrase outside it is not caught.
   *(Marked 2026-10-14, cycle 3: "every other visible text node" is
   replaced by blocks read whole, and the gap is now stated in the
   requirement itself; see choice 5 of the cycle-3 repair.)*

## Choices the cycle-3 repair made

The drafter made five more choices while repairing round 4. Choice 1 has
an alternative the round-4 raw offered as the owner's, so it is put as
Question 6 with a recommendation; the others can be changed by answering
Question 1 *Revise*.

1. **A provenance stamp is structural.** It is only the revision element of
   a citation whose cite names a served anchor or source record, the
   citation holds no other letter or digit, and the stamp's text must be
   that record's revision. So a revision id in a sentence, a heading or the
   shape-identity line is never a stamp; it is a label unit, or it goes. The
   mark finds the element, and the citation and the record decide it. This
   is the raw's proposed repair (raw lines 124–129). The alternative it
   offered, bare stamps allowed in prose with the "cannot hide a naming"
   claim withdrawn, is Question 6.
2. **"The label leads" means first in document order.** On each page, the
   first id of the revision the text sweep finds lies in a label unit, and
   in each unit the label precedes the full id. The status line is the one
   element exempt from this order. On Polaris it sits above the main
   content, so a reader still meets its short id first, as Question 5
   discloses.
3. **Identities shown whole are excepted** (round-4 Note 2). The footer's
   evaluation identity begins with the full revision, and the exact-source
   route's source identity contains it. Excepting an identity whose whole
   text equals a served identity keeps RFC6-15's evaluation stamp and the
   signed Observable's "every deterministic input and per-emission
   identity" visible, rather than reformatting them. An identity that is a
   bare revision id is not excepted, and an identity holding a tag name
   already fails the tag-name sweep.
4. **The page population is closed** (round-4 Note 6): `/polaris` and every
   exact-source route response, served or refused, in every mount form.
   PWB-REQ-020's machine views and draft view are out, the draft view
   because it "carries no project-shape identity". The re-observation
   action's result page is out too. [Observed at `7460aec8`] It is a `POST`
   response that shows the new evaluation's identity
   (`reobserve-action.ts` line 25), not a reading page.
5. **Stability is read per block, and the closed list is stated as a gap**
   (round-4 Note 4). The sweep reads each block's whole text, so
   `<code>v1.0.23</code> unchanged` is found. The requirement says that a
   paraphrase outside the five terms is not decided, and the falsifier limb
   is now "a stability term in a label unit, the label record or a block
   holding a captured tag name", aligned with the list.

## Residuals the sign-off change must carry

Each is [Observed] at `0a10977b` unless it names another commit.

1. **The recorder.** Add the package to `scripts/record_versioned_signoff.py`
   `real_packages()`.
2. **The reconciliation census and successor chain.** Both live in
   `scripts/check_spec_reconciliation.py`, and the signing change edits both,
   as the tree-framing sign-off did (docstring lines 85–87).
   - **Census.** It hard-codes the PWB census at 17 requirements and 51
     scenarios, with PWB-REQ-001 at 1. After `--apply` they read 17, 55 and
     5. The signing change updates the literal census and `census.json`.
   - **Chain.** The PWB child's `successors` tuple (lines 164–176) holds
     only the tree-framing sign-off. Over the applied bytes, R2 reports a
     broken chain and stale digests until the signing change appends this
     package's sign-off to that tuple. `record_versioned_signoff.py` does
     not make this edit.
   - *(Marked 2026-10-14: the census, chain and line figures above are
     stale. Re-measured at `814fbcc1`, after the anchor-resolution
     sign-off: the literal census `EXPECTED_TOTALS` reads 17 requirements
     and 52 scenarios, with PWB-REQ-001 at 1; after `--apply` they read
     17, 56 and 5 (the builder's `--check` prints 56). The PWB child's
     `successors` tuple (lines 244–257) holds the tree-framing and
     anchor-resolution sign-offs, and this package's sign-off is appended
     after them. The docstring paragraph recording earlier re-derivations
     is at lines 141–146.)*
   - *(Marked 2026-10-14, cycle 3: re-measured at `7460aec8`, after the
     class-granular sign-off. `EXPECTED_TOTALS` reads 17 requirements and
     56 scenarios, with PWB-REQ-001 at 1; after `--apply` they read 17, 60
     and 5 (the builder's `--check` prints 60). The `successors` tuple
     (lines 255–274) holds the tree-framing, anchor-resolution and
     class-granular sign-offs, and this package's sign-off is appended
     after them.)*
3. **The battery.** Add the builder's `--check` line to `PROJECT-STATUS.md`
   at sign-off, under the CG-26 coupled-triple rule. A draft leaves the
   battery alone.
4. **Implementation consumers.** Eight implementation files cite
   PWB-REQ-001 at `8f1fbec7` (`IMPACT-LEDGER.md`, re-measured 2026-10-14;
   seven at `0a10977b`; still eight at `814fbcc1` and at `7460aec8`).
   Sign-off authorizes none of their changes; a separate implementation
   authorization does.

## What this does not do

- It authorizes no implementation and no read. In particular, it does not
  admit tag refs or commit ancestry to the observer.
- It changes no requirement but PWB-REQ-001, no base matrix row's bytes
  (one row, `RFC4-11.c4`, is superseded through the repair delta), no
  doctrine, contract, policy, registry entry or performed act.
  *(Reworded 2026-10-15, cycle 4, for round-5 Note 5: it read "no
  contract-coverage row", beside the superseded row.)*
- It changes nothing on Trajectory or Orrery, and nothing in the shared
  operability status line.
