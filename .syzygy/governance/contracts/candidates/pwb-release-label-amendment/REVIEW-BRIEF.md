# Review brief — PWB release-label amendment

> **Candidate — binds nothing.** This brief tells a fresh-context reviewer
> what to read and what to decide. It is not itself under review.

## What you are reviewing

One amendment package against the signed PWB specification,
`openspec/changes/polaris-project-wide-butlers-model/`. It consists of:

- the seven patches under `proposed/` (five authored, two regenerated);
- the manifest `PWB-RELEASE-LABEL-AMENDMENT-MANIFEST.txt`;
- `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md` and `OWNER-DECISION-PACKET.md` in
  this directory;
- the builder `scripts/build_pwb_release_label_amendment.py`.

To read the proposed bytes, run `python3
scripts/build_pwb_release_label_amendment.py --diff`, or apply the patches in
a scratch copy. Never apply them in the tree.

## Governing references (read only these)

- **The direction.** It is quoted in full in `SEMANTIC-DELTA.md` §"The
  warrant". It lives on bead `syzygy-l362` and is not a tracked file.
- **The signed subject.** The eleven artifacts the manifest names. Their
  current bytes are those signed at
  `.syzygy/governance/decisions/PWB-TREE-FRAMING-AMENDMENT-SIGNOFF-v1.0.md`.
  *(Marked 2026-10-14: since the anchor-resolution sign-off at `7f43802f`,
  the current bytes are those signed at
  `.syzygy/governance/decisions/PWB-ANCHOR-RESOLUTION-AMENDMENT-SIGNOFF-v1.0.md`.)*
  *(Marked again 2026-10-14, cycle 3: since the class-granular sign-off at
  `235b71eb`, the current bytes are those signed at
  `.syzygy/governance/decisions/PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-SIGNOFF-v1.0.md`.)*
- **The sign-off scope.**
  `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`.
- **The specification bar.** CC-SPEC-1…11 in
  `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`.
  It is in force despite the path, because craft acts 6 and 7 bound it.
- **The clauses relied on:**
  - RFC2-2 in `.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`;
  - RFC2-24 in `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`;
  - RFC4-11 in `.syzygy/governance/contracts/rfcs/RFC-0004/named-adapters.md`;
  - RFC6-15 in `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`;
  - RFC1-10 in `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`,
    as an analogy only.
- **The observer's read authority.**
  `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`.
- **Doctrine.** VIS-2, VIS-3 and VIS-7 in `.syzygy/governance/doctrine/vision.md`.

## Acceptance criteria

1. **Direction content.** The package carries what the direction asks for
   Polaris:
   - the release label leads;
   - the object id sits beneath it as the identity;
   - a moved tag is detected, not trusted;
   - an untagged commit shows a short id, honestly labelled.

   Every departure from the direction is named and put to the owner: the read
   change, Trajectory and Orrery, the limits of moved-tag detection, and the
   tag population.
2. **The specification bar.** The amended requirement meets CC-SPEC: one
   obligation form, scope, a sweep oracle with a denominator, an observable,
   oracle independence, a falsifier, and scenarios its text carries. The
   four-form rule decides every revision without judgment.
3. **Contract claims.** Each claim is anchored to a defined clause and quoted
   (rule 8). No contract-coverage row claims something the oracle does not
   observe, and the coverage rows the delta says move are the only ones that
   do.
4. **Signed bytes.** No signed byte outside the patches changes. Every
   requirement but PWB-REQ-001 is byte-identical, and PWB-REQ-001's signed
   text and scenario survive.
5. **Mechanics.**
   - `--check` and `--selftest` pass, and each selftest mutant fails on its
     own predicate (rule 6).
   - The dependency file equals regeneration.
   - `scripts/build_polaris_project_wide_contract_coverage.py --check` passes
     over the proposed bytes.
   - The capability totals equal computation.
6. **Honest claims.** The package claims no adoption, authorizes no read,
   schedules no implementation, and names the residuals the sign-off change
   must carry.
7. **Plain language.** A fresh reader can restate what changes and what does
   not (VIS-3).

Run the checks in a clone, not this worktree (verification rule 7):

- `python3 scripts/build_pwb_release_label_amendment.py --check`
- `python3 scripts/build_pwb_release_label_amendment.py --selftest`
- `python3 scripts/check_governance.py`

## Output contract

Write your raw output verbatim to the path the dispatcher names; the
filename ends in `-RAW.md`. The first four non-blank lines must be exactly
these:

```text
# <title>
Reviewed commit: <40-hex commit you read>
Manifest SHA-256: <sha256 of PWB-RELEASE-LABEL-AMENDMENT-MANIFEST.txt, the file>
Verdict: CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE
```

`Manifest SHA-256` is the digest of the manifest **file** at the reviewed
commit, computed by script. It is not any row inside the manifest.

Then add a `## Findings` section, numbering findings as
`**Finding N — title** (blocking|revise|note)`. CONFIRM WITH EXCEPTIONS means
every finding is a `note`.

## Round 2 (added 2026-10-03, bead `syzygy-zeaf`)

Round 1 returned `REVISE`, and its findings were repaired with no review
round over the repaired bytes. Round 2 reviews those bytes against the same
seven criteria, on their own merits. Do not read `ROUND-1-DISPOSITIONS.md`
or anything under `docs/reviews/`.

**Raw-head digest predicate.** The version-tag sign-off binds a review by the
manifest digest in the raw's head. Over the first four non-blank lines of
your raw:

- line 2 is `Reviewed commit: ` followed by the 40-hex commit you read;
- line 3 is `Manifest SHA-256: ` followed by the lowercase 64-hex sha256 of
  the bytes of `PWB-RELEASE-LABEL-AMENDMENT-MANIFEST.txt` at that commit,
  computed by script (`git show <commit>:<path> | sha256sum`). It is never a
  row inside the manifest;
- line 4 is `Verdict: ` followed by exactly one of `CONFIRM`,
  `CONFIRM WITH EXCEPTIONS` or `REVISE`.

**Two notes carried from the merge review of PR 241.** Judge each one and
give it a finding of whatever severity you find:

1. In the proposed `spec.md`, the not-read form requires the statement
   "release tags were not read". Under test 3 (tag set captured, ancestry
   incomplete), that statement is false: the tags were read and the history
   was not. The packet already says "the tags, or the history needed to judge
   them"; the specification text should match.
2. Test 5 and its scenario say "no release tag reaches", while the
   recommended answer to the packet's Question 4 counts every tag under
   `refs/tags/`. "Release tag" is undefined until Question 4 is ruled.

**Stopping rule, set before this round.** A notes-only round, meaning
`CONFIRM` or `CONFIRM WITH EXCEPTIONS` with every finding a note, clears the
bytes it read. Any other verdict sends the package to the owner with its
findings open. No round 3 is dispatched.

## Round 3 (added 2026-10-14; not yet dispatched)

Round 2 returned `REVISE`. On 2026-10-14 the owner instructed one new
version repairing all six round-2 findings, then one fresh confirmation
round. Round 3 reviews the repaired bytes against the same seven criteria,
on their own merits. Do not read `ROUND-1-DISPOSITIONS.md`,
`ROUND-2-DISPOSITIONS.md` or anything under `docs/reviews/`.

**Raw-head digest predicate.** Unchanged from round 2: over the first four
non-blank lines, line 3 is `Manifest SHA-256: ` followed by the lowercase
64-hex sha256 of the bytes of the **file**
`PWB-RELEASE-LABEL-AMENDMENT-MANIFEST.txt` at the reviewed commit, computed
by `git show <commit>:<path> | sha256sum`. It is never a row inside the
manifest, and never the proposed spec's digest.

**Stopping rule, set before this round.** A notes-only round (`CONFIRM`, or
`CONFIRM WITH EXCEPTIONS` with every finding a note) clears the bytes it
read; its notes are dispositioned beside the package, never by editing
those bytes. Any other verdict sends the package to the owner with its
findings open. No round 4 is dispatched without a new owner instruction.

*(Marked 2026-10-14: "not yet dispatched" in the heading above is no longer
true. Round 3 ran under this section and returned `REVISE`
(`docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-3-RAW.md` line 4). The new
owner instruction this sentence anticipates was given the same day; see
Round 4 below.)*

## Round 4 (added 2026-10-14, cycle 2; not yet dispatched)

Round 3 returned `REVISE`: two revise findings and five notes. On
2026-10-14 the owner directed one more cycle: repair every round-3 finding,
notes included, then one fresh review under the same stopping rule. The
repair was made over `main` at `814fbcc1`, after the anchor-resolution
sign-off moved the signed `spec.md`, so the derived patches and the
manifest were regenerated. It also adds Question 5 to the packet. Round 4
reviews these bytes against the same seven criteria, on their own merits.

**Read the prior round.** Unlike rounds 2 and 3, you SHOULD read
`docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-3-RAW.md` and
`ROUND-3-DISPOSITIONS.md` (its §"Repairs, 2026-10-14 (cycle 2)" maps each
finding to its repair) and verify, finding by finding, that each repair
closes what the raw found. Judge the repair against the raw, never against
the mapping's own account of it. You may also read the implementation
files the round-3 raw cites (`apps/three-surface-poc/src/polaris.ts`,
`page-shell.ts`, `verbatim-route.ts`, `capability-detail.ts`, `orrery.ts`,
`git-observation.ts`, and
`packages/three-surface-poc-core/src/reevaluation.ts`), and PWB-REQ-011
and PWB-REQ-014 in the signed spec, to check the delta's re-measured
`[Observed]` claims. Do not read `ROUND-1-DISPOSITIONS.md`,
`ROUND-2-DISPOSITIONS.md` or any other raw.

**Raw-head digest predicate.** Over the first four non-blank lines of your
raw:

- line 1 is the title;
- line 2 is `Reviewed commit: ` followed by the 40-hex commit you read;
- line 3 is `Manifest SHA-256: ` followed by the lowercase 64-hex sha256 of
  the bytes of the manifest **file**
  `PWB-RELEASE-LABEL-AMENDMENT-MANIFEST.txt` at the reviewed commit,
  computed by script (`git show <commit>:<path> | sha256sum`). It is never a
  row inside the manifest, and never the proposed spec's digest;
- line 4 is `Verdict: ` followed by exactly one of `CONFIRM`,
  `CONFIRM WITH EXCEPTIONS` or `REVISE`.

**Sibling note.** At `814fbcc1` the three pending sibling builders
(accessible-name, class-granular extraction, opening-index) fail their own
`--check` on their stale derived dependency patches, before their order
check runs; they are being repaired on their own branches. This builder's
`--check` composes all four pending spec patches in every order itself.
Report what you observe at the reviewed commit.

**Stopping rule, set before this round.** A notes-only round (`CONFIRM`, or
`CONFIRM WITH EXCEPTIONS` with every finding a note) clears the bytes it
read; its notes are dispositioned beside the package, never by editing
those bytes. Any other verdict sends the package to the owner with its
findings open. No round 5 is dispatched without a new owner instruction.

*(Marked 2026-10-14, cycle 3: "not yet dispatched" in the heading above
is no longer true. Round 4 ran under this section and returned `REVISE`
(`docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-4-RAW.md` line 4). The new
owner instruction this sentence anticipates was given the same day; see
Round 5 below.)*

## Round 5 (added 2026-10-14, cycle 3; not yet dispatched)

Round 4 returned `REVISE`: one revise finding and seven notes. On
2026-10-14 the owner directed "One more cycle each" for this package and
P-98: repair every round-4 finding, notes included, then one fresh review
under the same stopping rule. The repair was made over `main` at
`7460aec8`. The class-granular amendment (P-86) had been signed first, so
this package was regenerated over P-86's applied bytes, as design decision
13 and capability row 35. The repair also adds Question 6 to the packet.
Round 5 reviews these bytes against the same seven criteria, on their own
merits.

**Read the prior round.** You SHOULD read
`docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-4-RAW.md` and
`ROUND-4-DISPOSITIONS.md`, whose §"Repairs, 2026-10-14 (cycle 3)" maps
each finding to its repair. Verify, finding by finding, that each repair
closes what the raw found. Judge the repair against the raw, never against
the mapping's own account of it.

You may also read these, to check the delta's and the ledger's re-measured
`[Observed]` claims:

- the implementation files the round-4 raw and the ledger cite:
  `apps/three-surface-poc/src/polaris.ts`, `polaris-source.ts`,
  `page-shell.ts`, `verbatim-route.ts`, `capability-detail.ts`,
  `production-reobserve.ts`, `reobserve-action.ts` and `main.ts`;
- PWB-REQ-011, PWB-REQ-014 and PWB-REQ-020 in the signed spec, and a term
  sweep of the POC spec;
- `PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-SIGNOFF-v1.0.md`, for the
  renumbering.

Do not read `ROUND-1-DISPOSITIONS.md` to `ROUND-3-DISPOSITIONS.md` or any
other raw.

**Raw-head digest predicate.** Over the first four non-blank lines of your
raw:

- line 1 is the title;
- line 2 is `Reviewed commit: ` followed by the 40-hex commit you read;
- line 3 is `Manifest SHA-256: ` followed by the lowercase 64-hex sha256 of
  the bytes of the manifest **file**
  `PWB-RELEASE-LABEL-AMENDMENT-MANIFEST.txt` at the reviewed commit,
  computed by script (`git show <commit>:<path> | sha256sum`). It is never a
  row inside the manifest, and never the proposed spec's digest;
- line 4 is `Verdict: ` followed by exactly one of `CONFIRM`,
  `CONFIRM WITH EXCEPTIONS` or `REVISE`.

**Sibling note.** At `7460aec8` the two pending sibling builders
(accessible-name, opening-index) fail their own `--check`, before their
order check runs, on derived dependency patches made stale by P-86's
sign-off; they are regenerated on their own branches. This builder's
`--check` composes the three pending spec patches in every order itself,
and runs the same search over any companion subject a pending sibling also
patches. Report what you observe at the reviewed commit.

**Stopping rule, set before this round.** A notes-only round (`CONFIRM`, or
`CONFIRM WITH EXCEPTIONS` with every finding a note) clears the bytes it
read; its notes are dispositioned beside the package, never by editing
those bytes. Any other verdict sends the package to the owner with its
findings open. No round 6 is dispatched without a new owner instruction.

## Round 6 (added 2026-10-15, cycle 4)

Round 5 returned `REVISE`: one revise finding (the cite's visible text was
free, so a sentence naming the revision could be cast as a citation) and
seven notes. The owner answered "One more cycle": repair every round-5
finding, notes included, once, then one fresh review under the same
stopping rule. The accessible-name (P-99) and opening-index (P-98)
amendments were signed v1.0 on 2026-10-15, so this package was regenerated
over their applied bytes and no PWB sibling is pending beside it. Round 6
reviews these bytes against the same seven criteria, on their own merits.

**Read the prior round.** You SHOULD read
`docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-5-RAW.md` and
`ROUND-5-DISPOSITIONS.md`, whose §"Repairs, 2026-10-15 (cycle 4)" maps
each finding to its repair. Verify, finding by finding, that each repair
closes what the raw found; in particular, build the round-5 raw's
falsifier page against the new text and say whether it now fails. Judge
the repair against the raw, never against the mapping's own account of it.
The delta names one residual as a limit (a served locator's token set is
not fixed); judge whether that disclosure is honest and sufficient.

You may also read these, to check the delta's and the ledger's
`[Observed]` claims:

- the implementation files the round-5 raw cites:
  `apps/three-surface-poc/src/polaris.ts`, `polaris-source.ts`,
  `page-shell.ts`, `verbatim-route.ts`, `capability-detail.ts`,
  `production-reobserve.ts`, `reobserve-action.ts` and `main.ts`;
- PWB-REQ-011, PWB-REQ-014 and PWB-REQ-020 in the signed spec;
- `PWB-ACCESSIBLE-NAME-AMENDMENT-SIGNOFF-v1.0.md` and
  `PWB-OPENING-INDEX-AMENDMENT-SIGNOFF-v1.0.md` in
  `.syzygy/governance/decisions/`, for the new base.

Do not read `ROUND-1-DISPOSITIONS.md` to `ROUND-4-DISPOSITIONS.md` or any
other raw. Never read any Butlers repository or other observed target's
content: everything you need is in this repository.

**Raw-head digest predicate.** Over the first four non-blank lines of your
raw:

- line 1 is the title;
- line 2 is `Reviewed commit: ` followed by the 40-hex commit you read;
- line 3 is `Manifest SHA-256: ` followed by the lowercase 64-hex sha256 of
  the bytes of the manifest **file**
  `PWB-RELEASE-LABEL-AMENDMENT-MANIFEST.txt` at the reviewed commit,
  computed by script (`git show <commit>:<path> | sha256sum`). It is never a
  row inside the manifest, and never the proposed spec's digest;
- line 4 is `Verdict: ` followed by exactly one of `CONFIRM`,
  `CONFIRM WITH EXCEPTIONS` or `REVISE`.

Number findings as `**Finding N — title** (blocking|revise|note)`, and end
with one line counting them by severity.

**Stopping rule, set before this round.** A notes-only round (`CONFIRM`, or
`CONFIRM WITH EXCEPTIONS` with every finding a note) clears the bytes it
read; its notes are dispositioned beside the package, never by editing
those bytes. Clearing is not signing: this package has no carry-over
answer, so it then goes to the owner for Question 1. Any other verdict
sends the package to the owner with its findings open. No round 7 is
dispatched without a new owner instruction.

## Round 7 (added 2026-10-15, cycle 5)

Round 6 returned `REVISE`: one revise finding (a citation placed inside a
sentence still passes every decide-line, so "therefore never a stamp", the
fifth scenario and Question 6's recommended row promised more than the
checks decide) and three notes. The owner answered "Weaker wording + review
(Rec.)": "Drop 'never a stamp', state both gaps as limits, then one review;
it comes back to you to sign." This version does that, and repairs the three
notes. Round 7 reviews these bytes against the same seven criteria, on their
own merits.

In particular, judge:

- whether the withdrawal is complete, so that no requirement text, scenario,
  design line or packet option still claims that a sentence, heading or
  identity line never names the revision through a citation;
- whether the two stated limits are honest and stated in the requirement
  itself;
- whether what remains decided is still a sweep with a denominator and a
  falsifier the oracle catches (CC-SPEC).

A disclosed, owner-chosen limit is not by itself a revise finding. Raise a
revise finding only where the text still claims more than its oracle
decides, or where a stated limit is false.

**Read the prior round.** You SHOULD read
`docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-6-RAW.md` and
`ROUND-6-DISPOSITIONS.md`, whose §"Repairs, 2026-10-15 (cycle 5)" maps each
finding to its repair. Judge each repair against the raw, never against the
mapping's own account of it. You may read the implementation and decision
files §"Round 6" lists. Do not read `ROUND-1-DISPOSITIONS.md` to
`ROUND-5-DISPOSITIONS.md` or any other raw. Never read any Butlers repository
or other observed target's content.

**Raw-head digest predicate.** This is the same as round 6. Over the first
four non-blank lines of your raw:

1. the title;
2. `Reviewed commit: ` followed by the 40-hex commit you read;
3. `Manifest SHA-256: ` followed by the lowercase 64-hex sha256 of the bytes
   of the manifest **file** `PWB-RELEASE-LABEL-AMENDMENT-MANIFEST.txt` at the
   reviewed commit, computed by script. It is never a row inside the
   manifest;
4. `Verdict: ` followed by exactly one of `CONFIRM`,
   `CONFIRM WITH EXCEPTIONS` or `REVISE`.

Number findings as `**Finding N — title** (blocking|revise|note)`, and end
with one line counting them by severity.

**Stopping rule, set before this round.** A notes-only round clears the bytes
it read, and its notes are dispositioned beside the package. The package
then goes to the owner for Question 1; clearing signs nothing. Any other
verdict is classified and stops, and no round 8 is dispatched without a new
owner instruction.
