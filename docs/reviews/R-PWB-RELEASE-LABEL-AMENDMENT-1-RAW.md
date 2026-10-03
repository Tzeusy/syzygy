# R-PWB-RELEASE-LABEL-AMENDMENT-1 — fresh-context review, round 1, PWB release-label amendment
Reviewed commit: b7eb7f59d0fcd2c3456dfaea789fcec064da784e
Manifest SHA-256: f451f3beea61a36215d0f49e4ae493bfc13f2d19a3693c6e729cc24135f3e57b
Verdict: REVISE

Scope: the package under
`.syzygy/governance/contracts/candidates/pwb-release-label-amendment/` (five
patches, manifest, SEMANTIC-DELTA.md, IMPACT-LEDGER.md,
OWNER-DECISION-PACKET.md) and `scripts/build_pwb_release_label_amendment.py`,
judged against the seven acceptance criteria in REVIEW-BRIEF.md:44-77, reading
only the governing references at REVIEW-BRIEF.md:21-42. Line numbers for the
spec patch are lines of `proposed/spec.md.patch`.

## Checks run

All in the clone at the reviewed commit, `PYTHONDONTWRITEBYTECODE=1`; the
working tree stayed clean (`git status --short` empty before and after).

- [Observed] Manifest digest: `sha256sum` of the file and of
  `git show HEAD:<path>` both give `f451f3be…3e57b` (full value in the head).
- [Observed] `build_pwb_release_label_amendment.py --check`: exit 0, "release-label
  candidate matches 11 proposed subjects (5 patched); 17 requirements, 55
  scenarios; structure, regeneration, contract coverage and sibling
  classification verify".
- [Observed] `--selftest`: exit 0, "16 structure mutants, patch drift and an
  unclassified sibling all fail closed on their own predicates". Each mutant
  is matched against its own expected finding prefix
  (build_pwb_release_label_amendment.py:543-552), so a mutant passing on a
  different predicate would be reported.
- [Observed] Two extra mutants of my own in the scratch copy: a one-character
  change to the spec row of the manifest fails `--check` with "manifest
  differs from deterministic proposed-byte regeneration"; adding `RFC2-3` to
  the proposed warrant line fails with the warrant, GOVERNING-DEPENDENCIES
  digest and manifest findings. Both restored.
- [Observed] `check_governance.py`: exit 0, "31 OK, 21 WARN, 0 FAIL (52
  checks)".
- [Observed] Patches applied with `git apply` in a scratch copy
  (`review-l362-apply`, built by `git archive` of the reviewed commit): all
  five apply; exactly the five declared subjects change (149 insertions, 11
  deletions); all 11 manifest rows equal the sha256 of the applied bytes (11
  rows, 0 mismatches).
- [Observed] Over the applied bytes:
  `build_polaris_project_wide_contract_coverage.py --check` passes ("Polaris
  consequence matrix matches regeneration — 324 clauses represented");
  `build_polaris_project_wide_spec_dependencies.py` regenerates
  GOVERNING-DEPENDENCIES.md to sha256 `76319cb4…`, equal to the manifest row,
  and its `--check` passes.
- [Observed] Capability totals recomputed by Python `re` over the applied
  table: 34 rows numbered 1…34 contiguously, 28 covered, 6 lawfully out of
  scope, 0 other — equal to the printed "Totals: 28 covered, 6 lawfully out of
  scope, 0 Unknown/unresolved; 34 total." and to "Population: 34".
- [Observed] Spec block comparison (Python, independent of the builder):
  preamble identical; requirement id list identical (17); only PWB-REQ-001
  differs; the signed PWB-REQ-001 paragraph ("WHEN the POC observes Butlers …
  observer identity/version.") and the signed scenario occur verbatim in the
  amended block. The only removed spec lines are three Verification line
  endings and the two warrant lines, each re-added extended.
- [Observed] Impact-ledger census re-run at `0a10977b` with the ledger's own
  regex over `git ls-files -z`: 1,947 files, 74 hits, and the per-area split
  19 / 16 / 15 / 11 / 5 (scripts) / 5 / 2 / 1 matches IMPACT-LEDGER.md:14-21.
- [Observed] `check_spec_reconciliation.py --check`: PASS (7 of 7) on the
  clone; over the applied bytes FAIL — R2 with 10 findings and R3 with 3 (see
  Finding 5).

## Findings

**Finding 1 — The four-form rule does not decide a captured tag set with uncaptured or incomplete ancestry, and can then state "untagged" from an absence nobody could look for** (revise)

[Observed] The not-read form's only condition is "when the tag set was not
captured, because its input is not admitted or reading it failed"
(spec.md.patch:29-30). "Reaches" and "distance" are defined over the
revision's history (spec.md.patch:24-26), and the untagged form applies
"otherwise" (spec.md.patch:39). No form covers a tag set that was captured
while commit ancestry was not captured, or was captured incompletely (a
shallow or grafted object database, or history that RFC4-11's fidelity limb
says may be unreachable: "it never reconstructs commit history it cannot
reach", RFC-0004/named-adapters.md:120-124).

[Inferred] In those states the rule as written yields *untagged* for a
revision whose reaching tag lies beyond the missing history — exactly the
"absence nobody looked for" the package itself says must never read as
untagged (SEMANTIC-DELTA.md "Anchors", VIS-2 bullet). The packet's Question 2
option "Admit tag refs only" says "The described form becomes 'not read' for
a revision that sits after a tag" (OWNER-DECISION-PACKET.md, Question 2
table), but the specification text carries no such rule: with tags captured
and no ancestry, the not-read condition is false. The owner would be offered
an option whose stated behaviour the bytes do not specify. Criterion 2's "the
four-form rule decides every revision without judgment" is therefore not met.
A repair would make the not-read (or a further Unknown) form's condition
"the tag set or the ancestry needed to decide reach was not completely
captured", add that case to the fixture list and falsifier, and align the
packet's option text.

**Finding 2 — Two falsifier limbs, the naming-site population and the tag-set identity rule have no oracle procedure or denominator** (revise)

[Observed] The falsifier lists "a claim or link bound to a tag name" and "a
tag message rendered" (spec.md.patch:89-92). The oracle that "decides" names
"Exact equality of form, tag name, distance, tied names and moved-tag
disclosure …, the full object id on the same surface as each label, and zero
labels stating untagged for an uncaptured tag set" (spec.md.patch:75-81). No
oracle step sweeps claims and links for a tag-name binding, and none sweeps
rendered output for tag-message bytes (the annotated-tag fixture,
spec.md.patch:62-63, is not said to carry a distinctive message to search
for). Per CC-SPEC-4 (SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md:200-203) a
prohibition is "satisfied by an exhausted population, never by an absence of
complaints"; these two prohibitions name no population.

[Observed] The obligation is scoped "Wherever Polaris names the observed
revision" (spec.md.patch:9), but neither the case nor the oracle says how the
checker enumerates those naming sites, so a site that names the revision by a
bare short id with no label is outside both the oracle ("each label") and the
falsifier. [Observed] "two evaluations of one revision whose captured tag
sets differ are two evaluations" (spec.md.patch:19-21) and "the captured tag
set's identity" in the machine answer (spec.md.patch:51-53) have no oracle
step and no falsifier limb. [Inferred] For the moved-tag limb, the expected
disclosure depends on what an earlier held evaluation bound; the oracle says
expected labels come "from the checker's own Git listing of each fixture"
(spec.md.patch:84-85) but does not say the checker records its own earlier
listing before moving the tag, so independence for that limb is asserted
rather than specified. Criterion 2 ("a sweep oracle with a denominator",
"oracle independence", "a falsifier") is not met for these limbs.

**Finding 3 — The moved-tag disclosure is influenced by an input the snapshot does not identify, and the package's determinism claim does not address it** (revise)

[Observed] The moved-tag rule keys on "an earlier identified evaluation of
the same repository, held by the observer" (spec.md.patch:45-48), and the
machine answer carries "moved-tag disclosures" (spec.md.patch:51-52). RFC2-2
reads "A source not identified in the snapshot must not influence any
deterministic claim of that snapshot's evaluations"
(RFC-0002/snapshot-and-evaluation-core.md:112-114); RFC6-15 reads "**Same
evaluation + same filters ⇒ same answer** in the deterministic layer"
(RFC-0006-cross-surface-selection-query-drawer.md:314-315); and RFC2-3
identifies an evaluation by "(source snapshot, as-of instant) — and nothing
else" (snapshot-and-evaluation-core.md:122-123). The set of earlier
evaluations the observer *holds* is not declared a captured input, and it can
change (retention, loss) while the snapshot does not. [Inferred] So two
answers at one evaluation can differ in their moved-tag disclosures, and
SEMANTIC-DELTA.md's claim that "one identified evaluation always shows one
label" and that RFC6-15 "keeps this true for the label" (§"The warrant", §
"Anchors") is true only of the label's form and values, not of the machine
answer the requirement defines. Criterion 3 requires each contract claim to
be anchored to a defined clause; this one is contradicted by the clauses the
package cites. A repair either makes the held prior-evaluation set (or the
compared evaluation) an identified input, or states the disclosure as
outside the deterministic layer and says how RFC2-2/RFC6-15 are then met.

**Finding 4 — A believed-not-applicable coverage row's stated basis is falsified by the described form, and the package does not name it** (revise)

[Observed] RFC4-11.c4 is `believed-not-applicable` with the rationale "No
commit/PR/change-accounting history is rendered by this capability"
(openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0004-0006.md:65).
The described form renders "that distance stated as a count of later
commits" (spec.md.patch:36-38), a count over commit history. SEMANTIC-DELTA.md
§"Anchors" says "No contract-coverage row moves" and discusses only RFC2-2 and
RFC2-24. [Observed] The literal claim is true: CONTRACT-COVERAGE.md and the
matrix parts are unpatched and the generator's `--check` passes over the
applied bytes. [Inferred] But the row's own justification becomes false the
moment the amendment is signed, and the clause it rests on (the fidelity
limb quoted in Finding 1) is directly engaged by distance counting. Criterion
3 asks that no coverage row claim something it does not; the package neither
re-examines this row nor names it as a residual for the sign-off change. The
RFC6-15.c2 row ("no repeated-answer oracle exists", RFC-0004-0006.md:220)
stays `unknown-uncovered`, consistent with Finding 3.

**Finding 5 — The reconciliation residual omits the successor-chain entry the sign-off change must also add** (revise)

[Observed] Residual 2 says the signing change "updates the literal census and
`census.json`, as the tree-framing sign-off did" (SEMANTIC-DELTA.md §"Residuals
the sign-off change must carry", item 2). Over the applied bytes,
`check_spec_reconciliation.py --check` fails R3 as predicted ("PWB: 17
requirements / 55 scenarios, expected 17 / 51"; the per-requirement 001
census; census.json) **and** fails R2 with 10 findings: five "broken chain —
reversing `…pwb-tree-framing-amendment/proposed/<file>.patch` over the
successor row … does not yield the row the chain reached" and five "stale
digest — … no longer hashes to its signed row". [Observed] The PWB child's
successors are a hard-coded tuple holding only the tree-framing sign-off
(scripts/check_spec_reconciliation.py:164-176), and the docstring says the
tree-framing re-derivation "added the tree-framing sign-off v1.0 to the PWB
child and re-derived the PWB census" (lines 84-87) — two edits, of which the
residual names one. Criterion 6 ("names the residuals the sign-off change
must carry") is not met for this item. [Unknown] Whether
`record_versioned_signoff.py` performs the chain edit itself; I did not read
the recorder beyond `real_packages()`, and the residual does not say so.

**Finding 6 — The direction's PWB-REQ-007/020 tuple is narrowed to PWB-REQ-001 without being named as a departure** (revise)

[Observed] The quoted direction says the change "Touches PWB
identity/freshness display (PWB-REQ-007/020 tuple, Polaris, Trajectory,
Orrery)" (SEMANTIC-DELTA.md:21-22). The package amends PWB-REQ-001 only; the
strings "007" and "020" occur in the package only inside that quotation
(grep over the four `.md` files, one hit). The §"Departures from the
direction, named" list has four items (read, Trajectory/Orrery, moved-tag
limits, tag population) and none covers this. [Inferred] It matters: the
not-read form carries an RFC2-24 reason and route (spec.md.patch:29-33),
which makes it an Unknown claim of the kind PWB-REQ-007 governs ("Every
project entity and project-fact claim SHALL … carry the closed label, tier,
exactly one primary reason …", spec.md:752-756), and PWB-REQ-020 governs
human/machine parity of project-wide facts (spec.md:1826). The package should
say whether the label is such a claim/fact and why 007 and 020 need no change,
or name the narrowing as a departure and put it to the owner. Criterion 1's
"Every departure from the direction is named" is not met for this item; the
four departures the criterion lists are all present and put to the owner
(SEMANTIC-DELTA.md §"Departures"; packet Questions 2-4).

**Finding 7 — Edge cases of the label rule are left to judgment** (note)

[Observed] The captured tag set pairs each ref "with the commit it peels to"
(spec.md.patch:16-18); a tag that peels to a tree or blob has no such commit
and the rule does not say whether it is excluded or makes the set unread.
"that tag's name" (spec.md.patch:35) does not say whether the `refs/tags/`
prefix is stripped, while "Only ref names … are taken" (spec.md.patch:22)
suggests the full ref name. Several tags peeling to the revision itself is
decided by the tie rule (distance zero is a least distance), which is
correct but only by inference; a sentence would remove the doubt.

**Finding 8 — "without further disclosure" collides with the requirement's own use of "disclosed"** (note)

[Observed] "show the revision's full Git object id beneath the label, on the
same surface and without further disclosure" (spec.md.patch:10-12) uses
"disclosure" for a progressive-disclosure control, while the same block uses
"disclosed as moved" and "moved-tag disclosures" (spec.md.patch:45-52) for
stating a fact. [Inferred] A fresh reader can still restate the change
(criterion 7 met), but "without expanding anything" would read unambiguously
(VIS-3).

**Finding 9 — The packet points to a disposition file that does not exist at the reviewed commit** (note)

[Observed] OWNER-DECISION-PACKET.md's status line says the review verdict and
dispositions "are in `ROUND-1-DISPOSITIONS.md` beside this file, which also
says whether this version is ready to offer"; `ls` of that path at
`b7eb7f59` returns "No such file or directory". [Inferred] Expected for a
pre-review draft, but the packet must not be offered until the file exists.

**Finding 10 — Two anchors paraphrase rather than quote** (note)

[Observed] The VIS-2 anchor reads "An absence nobody looked for is Unknown,
never zero" (SEMANTIC-DELTA.md §"Anchors"); VIS-2's defined text is "No
evidence means Unknown, not success. Nothing turns green, and no project is
declared aligned, converged, or genome-complete … without current evidence"
(doctrine/vision.md:133-135). The RFC2-2 anchor quotes only the heading. The
RFC2-24, RFC4-11 and RFC6-15 quotes match their clauses verbatim
(rendering-vocabularies.md:139; named-adapters.md:108-111;
RFC-0006…:314-315). The RFC1-10 analogy is correctly kept out of the warrants
(rule 5). Quote the clause text for VIS-2 and RFC2-2 (rule 8).

**Finding 11 — Builder diagnostics and sibling pinning are weaker than they read** (note)

[Observed] The warrant predicate is an exact-string test
(build_pwb_release_label_amendment.py:141-144, 286-287), so adding any further
warrant reports "PWB-REQ-001 warrants do not carry RFC2-2 and RFC2-24" — it
fails closed, but with a misleading message (my mutant above). Performed
siblings are classified by record existence only, which the builder itself
discloses (lines 89-94). Neither affects the current verdict of `--check`.

## Criteria summary

1. Direction content — **not met** (Finding 6). The four direction elements
   and the four listed departures are present and put to the owner.
2. The specification bar — **not met** (Findings 1, 2). One form (state
   projection/query) is kept, scope and scenarios are present and carried by
   the text; the four-form rule does not decide every case, and several
   prohibition limbs lack an oracle with a denominator.
3. Contract claims — **not met** (Findings 3, 4). The "no coverage row moves"
   claim is literally true and verified; the determinism claim is not
   supported by RFC2-2/RFC6-15 for moved-tag disclosures, and RFC4-11.c4's
   N/A basis is falsified unnamed.
4. Signed bytes — **met**. Only the five declared subjects change; every
   requirement but PWB-REQ-001 and the preamble are byte-identical; the
   signed paragraph and scenario survive verbatim.
5. Mechanics — **met**. `--check`, `--selftest` (each mutant on its own
   predicate), dependency regeneration, contract-coverage `--check` over the
   proposed bytes and the capability totals all verified by independent run.
6. Honest claims — **not met** (Finding 5). No adoption, read or
   implementation is claimed; one sign-off residual is incomplete.
7. Plain language — **met**, with Finding 8 as a note.
