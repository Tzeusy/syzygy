# Review brief — PWB opening-index and accessible-name amendments

> **Candidate — binds nothing.** This brief tells a fresh-context reviewer
> what to read and what to decide. It is not itself under review.

## What you are reviewing

Two amendment packages against the signed PWB specification,
`openspec/changes/polaris-project-wide-butlers-model/`, reviewed in one
round:

- **A, opening index** (PWB-REQ-010), in
  `.syzygy/governance/contracts/candidates/pwb-opening-index-amendment/`;
- **C, accessible names** (PWB-REQ-016), in
  `.syzygy/governance/contracts/candidates/pwb-accessible-name-amendment/`.

Each package has two patches under `proposed/` (the spec patch, authored,
and the `GOVERNING-DEPENDENCIES.md` patch, regenerated), a manifest,
`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md` and `OWNER-DECISION-PACKET.md`. The
tooling under review is:

- the shared engine `scripts/pwb_requirement_amendment.py`;
- the builders `scripts/build_pwb_opening_index_amendment.py` and
  `scripts/build_pwb_accessible_name_amendment.py`;
- the pending-sibling entries added to
  `scripts/build_pwb_class_granular_extraction_amendment.py` and
  `scripts/build_pwb_release_label_amendment.py`.

To read the proposed bytes, run each builder with `--diff`, or apply the
patches in a scratch copy. Never apply them in the tree.

## Governing references (read only these)

- **The bead and its narrowing.** `bd show syzygy-u05.12` (read-only): its
  description, and the 2026-10-03 coordinator note that narrowed it to
  slices A and C and set B and D aside.
- **The pursuit finding.** `docs/pursuits/2026-09-22-vision-pursuit.md`,
  section "N12".
- **The signed subject.** The eleven artifacts each manifest names, at the
  reviewed commit. The requirements amended are PWB-REQ-010 and PWB-REQ-016;
  read PWB-REQ-012 (copy rules), PWB-REQ-020 (parity) and PWB-REQ-021 (the
  walkthrough record) for what the amendments must not cross.
- **The contract.** RFC7-30, RFC7-31 and RFC7-34 in
  `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`.
- **The parent requirement.** POC-REQ-061 in
  `openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md`.
- **The sign-off scope.**
  `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`.
- **The specification bar.** CC-SPEC-1…11 in
  `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`.
  It is in force despite the path, because craft acts 6 and 7 bound it.
- **The delta form.**
  `.syzygy/governance/contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`
  and `SEMANTIC-DELTA-TEMPLATE.md` beside it.
- **The checker C describes.** `apps/three-surface-poc/src/polaris-accessibility.ts`,
  for checking the delta's claims about today's behaviour.
- **Doctrine.** VIS-1, VIS-3 and VIS-7 in `.syzygy/governance/doctrine/vision.md`.

## Acceptance criteria

1. **No verdict, no score.** Nothing in A lets a machine decide, score or
   imply that a cold-open prompt is answered (RFC7-31; PWB-REQ-021's
   "never a verdict or proof of comprehension"). Each index target is
   declared by the specification, not chosen by a run. The offsets enter no
   epistemic tuple, parity family, walkthrough record or readiness arm.
2. **Scope.** A changes only PWB-REQ-010 and C only PWB-REQ-016. Neither
   crosses into the Three-Surface POC specification. Slices B and D are not
   drafted, and each packet puts them to the owner with clause reasoning.
3. **The specification bar.** Each amended requirement still meets CC-SPEC:
   one obligation form, scope, a sweep oracle with a denominator, an
   observable, oracle independence, a falsifier, and scenarios its text
   carries. Each new obligation has an oracle limb, a falsifier limb and a
   scenario. A's index rows obey PWB-REQ-012, and their identities match
   PWB-REQ-021's nine in order.
4. **Signed bytes.** No signed byte outside the patches changes. Every other
   requirement is byte-identical, and every signed line of the amended
   requirement survives except those each builder lists as `replaced`.
5. **Honest claims.** Each [Observed] claim is checkable at the commit it
   names. No figure is quoted from an untracked capture; current figures
   are [Unknown]. The packages claim no adoption, authorize no build or
   read, and name the packages they collide with.
6. **Mechanics.**
   - Each builder's `--check` and `--selftest` pass, and each selftest
     mutant fails on its own predicate (rule 6).
   - The dependency file equals regeneration, and contract coverage
     regenerates byte-identical over the proposed bytes.
   - The four pending PWB packages' spec patches compose in either order.
   - The class-granular and release-label builders' `--check` still pass.
7. **Plain language.** A fresh reader can restate what changes and what
   does not (VIS-3).

Run the checks in a clone, not this worktree (verification rule 7):

- `python3 scripts/build_pwb_opening_index_amendment.py --check`
- `python3 scripts/build_pwb_opening_index_amendment.py --selftest`
- `python3 scripts/build_pwb_accessible_name_amendment.py --check`
- `python3 scripts/build_pwb_accessible_name_amendment.py --selftest`
- `python3 scripts/build_pwb_class_granular_extraction_amendment.py --check`
- `python3 scripts/build_pwb_release_label_amendment.py --check`
- `python3 scripts/check_governance.py`
- `python3 scripts/check_spec_reconciliation.py --check`

## Output contract

One review, two raw files, one per package, because each sign-off binds one
package's review head. Write each verbatim to the path the dispatcher names;
each filename ends in `-RAW.md`. Over the first four non-blank lines of each:

- line 1 is `# ` followed by a title;
- line 2 is `Reviewed commit: ` followed by the 40-hex commit you read;
- line 3 is `Manifest SHA-256: ` followed by the lowercase 64-hex sha256 of
  the bytes of that package's manifest file
  (`PWB-OPENING-INDEX-AMENDMENT-MANIFEST.txt` or
  `PWB-ACCESSIBLE-NAME-AMENDMENT-MANIFEST.txt`) at that commit, computed by
  script (`git show <commit>:<path> | sha256sum`). It is never a row inside
  the manifest;
- line 4 is `Verdict: ` followed by exactly one of `CONFIRM`,
  `CONFIRM WITH EXCEPTIONS` or `REVISE`.

Then add a `## Findings` section, numbering findings as
`**Finding N — title** (blocking|revise|note)`. CONFIRM WITH EXCEPTIONS means
every finding is a `note`. A finding about the shared engine, or about both
packages, goes in both raws.

**Stopping rule, set before this round.** One round only. For each package,
a notes-only verdict, meaning `CONFIRM` or `CONFIRM WITH EXCEPTIONS` with
every finding a note, clears the bytes it read; its notes are dispositioned
in a sibling `ROUND-1-DISPOSITIONS.md` and the package is not edited. Any
other verdict leaves that package unedited: no second round is dispatched,
and its findings go to the owner.

**Applied after the round (2026-10-03).** Both packages returned `REVISE`.
The coordinator then directed that a first-round `REVISE` on a new draft
is repaired once, with each finding and its repair recorded, and no round
2 is run; the rule above, which said the packages stay unedited, was
written for a confirmation round and was not applied. Each package's
`ROUND-1-DISPOSITIONS.md` records the repairs. The repaired bytes are
unconfirmed.

## Round 3

*(Added 2026-10-14. Everything above is the round-1 brief, left as rounds
1 and 2 read it. Where this section and the text above differ, this
section governs round 3.)*

**Why a round 3.** Round 2 returned `REVISE` on both packages
(`docs/reviews/R-PWB-OPENING-INDEX-AMENDMENT-2-RAW.md` and
`docs/reviews/R-PWB-ACCESSIBLE-NAME-AMENDMENT-2-RAW.md`, line 4 of each).
The owner, in the lead session on 2026-10-14, directed one more cycle:
every round-2 finding, notes included, repaired once, then one fresh
review under the same stopping rule. The repairs are mapped in each
package's `ROUND-2-DISPOSITIONS.md`, §"Repairs, 2026-10-14 (cycle 2)". The
repairing session dispatches no review.

**Stopping rule, set before the round.** One round, the same rule the
2026-10-14 confirmation cycle used
(`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md`).
Each package is judged on its own:

- a verdict with no revise-level or blocking finding (`CONFIRM`, or
  `CONFIRM WITH EXCEPTIONS` with every finding a note) clears the exact
  bytes it read, under the owner's 2026-09-26 ruling. Its notes go in a
  sibling `ROUND-3-DISPOSITIONS.md` beside the package, and the package is
  not edited;
- a verdict still `REVISE` goes to the owner with its findings. The
  package is not repaired again, and no round 4 is dispatched without a
  new owner direction;
- a verdict is never re-labelled.

**Subject.** For each package, the manifest at the reviewed commit and
the proposed bytes it hashes, the package's prose (`SEMANTIC-DELTA.md`,
`IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`), its builder, and the
shared engine `scripts/pwb_requirement_amendment.py`. The engine is not
changed in this cycle; each builder now adds its own positional check for
replaced lines.

**Governing references.** Those above, plus:

- both earlier raws for each package;
- each package's `ROUND-1-DISPOSITIONS.md` and `ROUND-2-DISPOSITIONS.md`;
- `.syzygy/governance/decisions/PWB-ANCHOR-RESOLUTION-AMENDMENT-SIGNOFF-v1.0.md`,
  the sign-off that moved PWB `spec.md`, so that both packages were
  regenerated over it;
- PWB-REQ-011's machine-recovery limb and PWB-REQ-020, for C's page list
  and expected paths;
- for checking C's claims about today's code,
  `apps/three-surface-poc/src/polaris-source.ts`,
  `apps/three-surface-poc/src/polaris-markdown.ts` and
  `apps/three-surface-poc/src/polaris-accessibility.ts`.

You SHOULD read the prior raws and dispositions, and check each claimed
repair against the bytes, not only against the mapping.

**What to test, at least.**

- Is each round-2 finding repaired in the bytes as each cycle-2 mapping
  claims? That is nine for A and seven for C.
- **A.** Does the first scenario now place the stopping line where the
  requirement does? Is "each row shows its declared row name" a checkable
  replacement for the dropped accessible-name sentence, and is dropping
  that sentence stated fairly to the owner (packet Question 8)? Do the
  offset base, the tie, closed-`details` and no-target rules, the declared
  viewport and the per-text-node visibility rule leave any offset or line
  position undecidable? Do the recognizer's permitted keys keep it
  independent of the renderer's markers? Is Question 9 fair?
- **C.** Is the shared-label rule scoped, decidable and independent: its
  visible-label definition, its label prefix, and its path taken from the
  machine answer? Is the [Unknown] about whether the machine answer
  carries paths honest, and is Question 7 fair? Does the interactive
  population now mirror the heading population? Is dropping the verbatim
  exemption right on the code facts the delta cites, and is Question 8
  fair? Is the page list's source outside the renderer?
- **Both.** Does each builder's positional check fail closed (rule 6), and
  are the phrases the round-2 probes moved now pinned? Do all pending PWB
  builders' `--check` pass at the reviewed commit, or does the raw name
  which fail and why?

**Mechanics.** Run in a clone at the reviewed commit (verification rule
7):

- `python3 scripts/build_pwb_opening_index_amendment.py --check` and `--selftest`
- `python3 scripts/build_pwb_accessible_name_amendment.py --check` and `--selftest`
- `python3 scripts/build_pwb_class_granular_extraction_amendment.py --check`
- `python3 scripts/build_pwb_release_label_amendment.py --check`
- `python3 scripts/check_governance.py`
- `python3 scripts/check_spec_reconciliation.py --check`

**Output.** One raw per package, written verbatim to the paths the
dispatcher names, each filename ending in `-RAW.md`
(docs/reviews/R-PWB-OPENING-INDEX-AMENDMENT-3-RAW.md and
docs/reviews/R-PWB-ACCESSIBLE-NAME-AMENDMENT-3-RAW.md, files this round
creates, unless the dispatcher names others). A finding about the shared engine, or about both
packages, goes in both raws.

**Head contract.** Over the first four non-blank lines of each raw:

- line 1 is `# ` followed by a title;
- line 2 is `Reviewed commit: ` followed by the full 40-hex commit you read;
- line 3 is `Manifest SHA-256: ` followed by the lowercase 64-hex sha256 of
  the bytes of **that package's manifest file**
  (`PWB-OPENING-INDEX-AMENDMENT-MANIFEST.txt` or
  `PWB-ACCESSIBLE-NAME-AMENDMENT-MANIFEST.txt`) at the reviewed commit,
  computed by script
  (`git show <commit>:.syzygy/governance/contracts/candidates/<package>/<manifest> | sha256sum`).
  It is never a row inside the manifest, never the proposed spec's digest
  and never a figure copied from this brief or the dispositions;
- line 4 is `Verdict: ` followed by exactly one of `CONFIRM`,
  `CONFIRM WITH EXCEPTIONS` or `REVISE`.

Then a `## Findings` section, numbering findings as
`**Finding N — title** (blocking|revise|note)`, each labelled
`[Observed]`, `[Inferred]` or `[Unknown]`.
