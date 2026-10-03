# Semantic delta — PWB release-label amendment

> **Candidate — binds nothing.** This package proposes one amendment to the
> signed PWB specification. Nothing here is signed, adopted or labelled
> accepted, and no implementation is authorized (VIS-4). Only the owner's
> version-tagged sign-off binds it.

**Drafted:** 2026-10-03, bead `syzygy-l362`, over `main` at `0a10977b`.

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
revision does not. It keeps determinism everywhere else by making the captured
tag set an evaluation input, so one identified evaluation always shows one
label, and two evaluations that differ only in their tags are two evaluations.

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

**PWB-REQ-001 (amended).** The signed paragraph and its one scenario stay as
they are. Added:

- **Release label.** Wherever Polaris names the observed revision, it leads
  with the release label and shows the full Git object id beneath it, on the
  same surface. Every claim, evaluation identity, link and comparison binds to
  the object id, never to a tag name.
- **Captured tag set.** Every ref under `refs/tags/`, each paired with the
  commit it peels to, is a deterministic evaluation input with its own
  identity. Only names and object ids are taken; no tag message or signature
  is read into the model or rendered.
- **Four forms, tested in order:**
  1. *not read* — the tag set was not captured. Polaris shows the first
     twelve hexadecimal digits, says release tags were not read, and gives
     the reason `source-uncaptured-or-unreachable` and its route. It never
     says "untagged".
  2. *tagged* — a tag peels to the revision: "Butlers v1.0.23".
  3. *described* — the nearest reaching tag is some commits behind: the tag's
     name and the count of later commits.
  4. *untagged* — no tag reaches the revision: the project name and the first
     twelve hexadecimal digits, with a statement that no release tag reaches
     it.

  Ties at the least distance are broken by codepoint order of tag name, and
  every tied name is carried in the machine answer.
- **Moved tags.** A tag name that an earlier held evaluation bound to a
  different commit is disclosed as moved, naming both commits. Nothing
  presents a tag as unmoved.
- **Machine answer.** It carries the form, tag name, distance, tied names,
  moved-tag disclosures, the tag set's identity and the full object id.
- **Verification.** Fixture repositories cover every form, a tie, an
  annotated tag and a moved tag. The checker computes the expected label from
  its own Git listing, never from the observer's captured set.
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
- `GOVERNING-DEPENDENCIES.md` is regenerated over the proposed spec.

## Anchors

Each contract claim is anchored to the clause it rests on (rule 8).

- **RFC2-2 — Uncaptured means uninfluential.** The tag set must be a captured
  input before it can influence the label. The not-read form is what an
  uncaptured tag set yields.
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
- **VIS-2.** An absence nobody looked for is Unknown, never zero, and the same
  goes for "untagged". This is why the not-read form comes first and never
  says "untagged".

[Inferred] RFC1-10, "Identifiers are opaque; names are labels", is the same
idea: a tag name is a label and the object id is the identifier. But its scope
is "every declared class (Capability, Topology entry, Declared region,
Repository, Project, Proposal)", and a release tag is none of those. It is
therefore cited as an analogy only and is not a warrant (rule 5).

**Coverage matrix.** No contract-coverage row moves. The two new warrants add
no covered row, so the generator's warrant-agreement check (covered rows must
cite a warranted clause) is unaffected, and `CONTRACT-COVERAGE.md` regenerates
to the same bytes. [Inferred] The matrix's existing rows for RFC2-2 (`.c1`
unknown-uncovered, `.c2` covered by PWB-REQ-003) and RFC2-24 stand as they are.
This amendment does not claim new coverage for either clause.

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

The tagged, described and untagged forms all need the tag set. The described
form also needs commit ancestry to count commits back to a tag. So:

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
3. **"Moved tag detected"** is detected only against an earlier evaluation
   the observer holds. [Observed] No retained evaluation exists in the
   implementation: `git grep -i -E 'retained[- ]evaluation|retainedEvaluation'`
   over `apps` and `packages` at `0a10977b` returns nothing. Until one does,
   the moved-tag limb never fires. What still holds is that nothing binds to a
   tag and the full object id is always shown, so a reader can compare ids.
   The specification forbids stating that a tag is unmoved.
4. **Which tags count.** The package counts every ref under `refs/tags/`. A
   project whose non-release tags sit there would see them as labels.
   [Unknown] Butlers' tag population was not read, since reading it is the
   read this package is waiting on. Question 4 offers a declared tag pattern
   instead.

## Residuals the sign-off change must carry

Each is [Observed] at `0a10977b`.

1. **The recorder.** Add the package to `scripts/record_versioned_signoff.py`
   `real_packages()`.
2. **The reconciliation census.** `scripts/check_spec_reconciliation.py`
   hard-codes the PWB census at 17 requirements and 51 scenarios, with
   PWB-REQ-001 at 1. After `--apply` they read 17, 55 and 5. The signing
   change updates the literal census and `census.json`, as the tree-framing
   sign-off did.
3. **The battery.** Add the builder's `--check` line to `PROJECT-STATUS.md`
   at sign-off, under the CG-26 coupled-triple rule. A draft leaves the
   battery alone.
4. **Implementation consumers.** Seven implementation files cite
   PWB-REQ-001 (`IMPACT-LEDGER.md`). Sign-off authorizes none of their
   changes; a separate implementation authorization does.

## What this does not do

- It authorizes no implementation and no read. In particular, it does not
  admit tag refs or commit ancestry to the observer.
- It changes no requirement but PWB-REQ-001, no contract-coverage row, no
  doctrine, contract, policy, registry entry or performed act.
- It changes nothing on Trajectory or Orrery.
