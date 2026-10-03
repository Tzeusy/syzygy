> # Record beside the package — not authority, binds nothing
>
> Dispositions of the one fresh-context review of the PWB release-label
> amendment package. This record is not a package artifact: the manifest does
> not hash it and no builder reads it. It offers nothing and performs no act
> (VIS-4).

# Round 1 dispositions — PWB release-label amendment

- **Reviewed commit:** `b7eb7f59d0fcd2c3456dfaea789fcec064da784e`.
- **Verdict (raw line 4):** `REVISE`. The review has six revise findings (1–6)
  and five notes (7–11), with no blocking finding.
- **Stopping rule, set by the coordinator before the round ran.** The bead
  allows one round. A REVISE is repaired, no further round is dispatched,
  and the package goes to the owner.
- **Applied here:**
  - Every finding below is repaired in the package.
  - The repair retires the round-1 review (rule 10), so **the repaired bytes
    have not been reviewed.**
  - No second round is dispatched.
- **Status: not cleared.** This version is not "ready for owner sign-off" in
  the sense Scope A item 3 requires: "a package is offered only after a round
  that returns CONFIRM, or CONFIRM WITH EXCEPTIONS with notes only". It goes
  to the owner as a pending row with this disposition. The owner may direct
  one fresh round over the repaired bytes before the sign-off question is
  asked. That is the drafter's recommendation.
- **Re-derived figures.** Every figure below was re-derived from the repaired
  bytes by `scripts/build_pwb_release_label_amendment.py --check` and by the
  contract-coverage generator's `--check`:
  - 7 patched subjects;
  - 17 requirements and 55 scenarios;
  - 629 effective consequence rows: 137 covered, 247 Unknown uncovered and
    245 believed not applicable.

Reviewed record: docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-1-RAW.md

## Dispositions

### 1 — the four-form rule did not decide incomplete ancestry (revise)

**Accepted.**

- PWB-REQ-001 now defines a second captured input, the **captured
  ancestry**. It is complete only when every commit in the revision's
  history was read; a shallow or grafted database, an unreadable commit or an
  unadmitted read leaves it incomplete.
- The rule is now five ordered tests over four forms. *Not read* applies
  when the tag set is uncaptured, and again when the ancestry is incomplete
  and no tag peels to the revision itself. So neither *described* nor
  *untagged* can be reached from history nobody read.
- The case now has a shallow-clone fixture. The falsifier names "an uncaptured
  tag set or incomplete ancestry stated as untagged".
- The packet's "Admit tag refs only" option now says that only the tagged form
  works.

### 2 — falsifier limbs, naming sites and the tag-set identity lacked an oracle (revise)

**Accepted.** The oracle now:

- enumerates every naming site (each element carrying the full object id,
  its first twelve hexadecimal digits, or a label) and uses that count as the
  denominator;
- searches every claim identity, evaluation identity and link target for each
  captured tag name;
- searches every served byte for the annotated fixture's distinctive message
  string;
- compares the tag-set and evaluation identities of one revision observed
  under two tag sets;
- records its own listing of each fixture before any tag moves.

The falsifier gains these limbs: "a naming site without a label" and "one
evaluation identity for two different tag sets".

### 3 — moved-tag disclosures read an unidentified input (revise)

**Accepted.**

- An evaluation now names its **compared evaluations** in its inputs, by
  evaluation identity, and the moved-tag comparison reads only those. That
  makes the disclosure a function of identified inputs, which is what RFC2-2
  and RFC6-15 require.
- The machine answer carries the compared evaluations' identities.
- The delta's determinism paragraph now names all three inputs.

### 4 — RFC4-11.c4's not-applicable basis was falsified (revise)

**Accepted.**

- The package now also patches `CONTRACT-COVERAGE-REPAIR-DELTA.md`. It
  supersedes `RFC4-11.c4` with two rows:
  - `RFC4-11.r1`, a commit count computed only from completely captured
    ancestry and never reconstructed, covered by PWB-REQ-001;
  - `RFC4-11.r2`, PR facts, still not applicable.
- The repair delta explains why. `CONTRACT-COVERAGE.md` is regenerated, and
  the builder now regenerates it as a derived patch.
- The delta's §"Coverage matrix" replaces the claim that no row moves.

### 5 — the reconciliation residual omitted the successor chain (revise)

**Accepted.** Residual 2 now names both edits the signing change makes in
`scripts/check_spec_reconciliation.py`: the literal census, and appending
this package's sign-off to the PWB child's `successors` tuple. It also says
`record_versioned_signoff.py` does not make the chain edit. That was checked
with `grep -n -i -E 'successor|chain'` over the recorder, which shows only
package names.

### 6 — the PWB-REQ-007/020 narrowing was not named (revise)

**Accepted.**

- The amended text now says the label is a presentation of PWB-REQ-001's
  revision identity, "not a project-shape claim or fact", and carries no
  epistemic tuple.
- The delta names this as departure 5 and says why PWB-REQ-007 and
  PWB-REQ-020 need no new text.
- The packet tells the owner that answering "Revise" makes the label a
  challengeable claim instead.

### 7 — edge cases (note)

**Accepted.**

- A tag peeling to anything but a commit reaches no revision.
- A tag's name is its ref name without `refs/tags/`.
- Ties at the revision itself are stated explicitly.

### 8 — "without further disclosure" (note)

**Accepted.** It now reads "without expanding anything".

### 9 — the packet cited a disposition file not yet present (note)

**Accepted.** This file now exists.

### 10 — two anchors paraphrased (note)

**Accepted.** The delta now quotes VIS-2 (`doctrine/vision.md` lines
133–135) and RFC2-2's clause text (`snapshot-and-evaluation-core.md` line
112).

### 11 — builder diagnostics (note)

**Accepted in part.**

- The warrant predicate now parses the contracts list and names the missing
  identifier, so adding a further warrant no longer trips it.
- Classifying siblings by the existence of their record is unchanged. It is
  already disclosed in the builder's comment.
- The selftest now runs 19 structure mutants, including the ancestry limb,
  the repair rows and a signed repair-delta line.
