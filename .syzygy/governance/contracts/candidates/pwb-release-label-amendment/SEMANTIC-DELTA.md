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
  - Polaris *names* the revision wherever its owner-visible text shows the
    full object id, its first twelve hexadecimal digits, or the project's
    name followed by a captured tag's name. Attribute values, link targets
    and identities are not owner-visible text.
  - Each such place shows one *label unit*: the label, its statement, the
    full object id beneath and any moved-tag disclosure, exposed as one
    element of the page so that a checker finds it without judgment.
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
  answer.
- **Moved tags.** An evaluation names, as inputs, the earlier evaluations it
  is compared with. A tag one of them bound to a different commit is
  disclosed as moved, naming both commits, wherever its name is carried: in
  a label, among the tied names in the machine answer, and in the surface's
  expansion of them. Nothing presents a tag as unmoved.
- **Machine answer.** Its label record carries the form, the test that
  applied, the statement, tag name, distance, tied names, moved-tag
  disclosures, the identities of the three inputs and the full object id.
- **Verification.** Fixture repositories cover every form, ties at the
  revision and at a distance, an annotated tag with a distinctive message, a
  tag peeling to a tree, a tag set with one ref that fails to peel, two
  shallow clones (one hiding the only reaching tag, one whose captured part
  holds a reaching tag), one revision under two tag sets, a moved tag, and a
  moved tag that is tied at the revision but not shown first.
  - The denominator is the naming sites: every occurrence, in owner-visible
    text, of the short or full id or of the project name followed by a
    captured tag name, plus the machine answer's label record. Each must
    lie in a label unit. Link targets and identities are not sites; the
    tag-name sweep covers them.
  - It computes each expected form, statement and value from its own
    recorded Git listing, never from the observer's inputs, and decides on
    exact equality, the statement included.
  - Its sweeps cover four things: tag names in identities and links, the tag
    message in served bytes, distinct identities for differing tag sets, and
    every moved-tag disclosure, tied names included.
- **Four new scenarios.** A tagged revision; a revision no tag reaches; unread
  tags never shown as untagged; a moved tag disclosed.
- **Warrants.** VIS-2 joins the doctrine list, and RFC2-2 and RFC2-24 join the
  contracts.

**Companions.**

- `proposal.md` gains one "What Changes" bullet.
- `design.md` gains decision 12, "Name the revision by its release label",
  with a flowchart of the four forms.
- `CAPABILITY-COVERAGE.md` gains row 34, covered by PWB-REQ-001. The totals
  become 28 covered, 6 lawfully out of scope, 0 Unknown, 34 in all.
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
    The falsifier names "a count of later commits computed from incomplete
    ancestry".
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
  62 and 106).

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
over this repaired patch. Class-granular also adds design decision 12 and
capability row 34, so whichever of it and this package is signed second is
regenerated over the first's applied bytes and reviewed again (P-86's
Question 5).

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
3. **The battery.** Add the builder's `--check` line to `PROJECT-STATUS.md`
   at sign-off, under the CG-26 coupled-triple rule. A draft leaves the
   battery alone.
4. **Implementation consumers.** Eight implementation files cite
   PWB-REQ-001 at `8f1fbec7` (`IMPACT-LEDGER.md`, re-measured 2026-10-14;
   seven at `0a10977b`). Sign-off authorizes none of their
   changes; a separate implementation authorization does.

## What this does not do

- It authorizes no implementation and no read. In particular, it does not
  admit tag refs or commit ancestry to the observer.
- It changes no requirement but PWB-REQ-001, no contract-coverage row, no
  doctrine, contract, policy, registry entry or performed act.
- It changes nothing on Trajectory or Orrery.
