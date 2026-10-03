# R-M9-POC-IDENTITY-AMENDMENT-4 — fresh-context review, round 4, Three-Surface POC identity amendment
Reviewed commit: de81d25930429d926566162b19b16fe52807be1a
Manifest SHA-256: 1f925841de1de1142eafed9b02826c99ba3fd0164ac9205d5dcaf8ae539f900b
Verdict: REVISE

Reviewer: fresh-context agent. Scope: the brief at
`.syzygy/governance/contracts/candidates/three-surface-poc-identity-amendment/REVIEW-BRIEF.md`.
I read the four patches, the manifest, `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`,
`OWNER-DECISION-PACKET.md`, the builder, and only the governing references the
brief lists. I did not read any `ROUND-*-DISPOSITIONS.md` or anything under
`docs/reviews/`. I applied the patches in a scratch copy
(`.../scratchpad/review26d-apply`), never in the clone.

Line citations of the form "applied spec.md:N" or "applied CONTRACT-COVERAGE.md:N"
refer to the proposed bytes after `git apply` of the four patches in that scratch
copy. Those bytes hash to the manifest's rows (see Verification log).

## Verification log

- [Observed] The manifest file's SHA-256 at the reviewed commit, from
  `git show <commit>:<path>` piped to Python `hashlib`, is
  `1f925841de1de1142eafed9b02826c99ba3fd0164ac9205d5dcaf8ae539f900b`.
  `sha256sum` on the working file gives the same value.
- [Observed] All four patches apply cleanly with `git apply` in the scratch
  copy. The six resulting subjects hash byte-for-byte to the six manifest rows,
  checked with `sha256sum` (an independent method from the builder's).
- [Observed] `python3 scripts/build_three_surface_poc_identity_amendment.py --check`
  exits 0. Its output: "manifest matches 6 proposed subjects (4 patched, 2
  unchanged); 26 requirements, Part A 78 clauses over 134 rows; structure,
  regeneration and the preserved RFC1-26 row verify".
- [Observed] `--selftest` exits 0: "24 structure mutants, patch drift, manifest
  order and subject drift all fail closed on their own predicates". The harness
  (builder lines 659–665) requires every mutant to change bytes and to produce
  a finding that starts with that mutant's own expected predicate string.
- [Observed] `python3 scripts/check_governance.py` gives "31 OK, 21 WARN, 0 FAIL
  (52 checks)". None of the 890 output lines names this package's directory or
  its builder (checked with `grep`).
- [Observed] Running the brief's checks wrote a gitignored
  `scripts/__pycache__/` into the clone. `git status --short --ignored` shows
  only that directory, and no tracked file changed. My own extra probes ran in
  the scratch copy with `PYTHONDONTWRITEBYTECODE=1`.
- [Observed] I recomputed the coverage figures with my own Python over the
  applied matrix, without importing the builder:
  - Part A: 134 rows over 78 clauses, 102 covered and 32 Unknown, with no third
    disposition.
  - Part B1: 28 rows over 27 clauses. Part B2: 219 clauses.
  - Per family (A/B1/B2): RFC2 is 8/0/19 and RFC6 is 13/1/14. Every other
    family is unchanged from the signed table. The parts sum to 324.
  - The Part A clause set equals the `contracts[]` union over the applied spec
    (78 identifiers).
  - The applied spec has 26 requirement headings and 28 scenario headings. The
    signed spec has 24 and 24.
  - `scripts/build_three_surface_poc_spec_dependencies.py --check` passes in the
    scratch copy: "26 requirement(s), 90 distinct authorities".
- [Observed] The tree's six subjects hash to the last column of
  `THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md` lines 32–37, so no signed
  byte is edited in the tree.
- [Observed] Lines removed from the signed matrix by the patch, by line-set
  difference:
  - the four Part B2 rows for RFC2-25, RFC6-1, RFC6-3 and RFC6-12;
  - the family-table rows for RFC2, RFC6 and Total;
  - five computed-figure prose lines.

  The bound RFC1-26 row occurs exactly once before and after the patch. None of
  the 30 added row lines that start with `| RFC…-` lacks the words "Amendment
  row".
- [Observed] I checked these anchors at source:
  - RFC6-1 at RFC-0006 line 108, with its bullets at 112–115 and 116–118;
  - RFC6-3 at 135, RFC6-12 at 263 and RFC6-14 at 279;
  - RFC1-26 at RFC-0001 line 736, RFC1-9 at 300, and RFC1-25's table data rows
    at 596–621 (26 rows);
  - RFC2-24 and RFC2-25 at `RFC-0002/rendering-vocabularies.md` lines 103 and
    168;
  - `trust-and-evidence.md` lines 25, 84–85 and 115–116;
  - the lane-B direction at line 36.

  Each quoted fragment in `SEMANTIC-DELTA.md` matches its source.
- [Observed] `poc-seeds.ts` lines 194–260 hold nine relationships over eight
  kinds, and the `contains` relationship runs from `project:butlers` to
  `capability:…`. RFC1-25's `contains` row (line 596) assigns no
  Project→Capability pair.
- [Observed] I checked the residual claims at source:
  - `check_spec_reconciliation.py:214` reads `"POC": (24, 24)`;
  - `record_versioned_signoff.py:117–` lists only PWB packages;
  - the tracked population at `ab22492` is 1,924 paths (`git ls-tree -r -z`).
- [Observed] I ran extra rule-6 probes in the scratch copy. Each one mutated
  the proposed bytes, regenerated `GOVERNING-DEPENDENCIES.md` over the mutated
  spec (otherwise the spec digest inside it catches every spec edit by
  accident), and called `structure_findings`. Results:

  | Probe | Result |
  |---|---|
  | A signed reader-notes sentence ("Each requirement ends with a machine-readable") edited | survived |
  | The reader-notes group range (`054–055`) edited | survived |
  | POC-REQ-054's oracle-independence clause weakened | survived |
  | POC-REQ-055's "none is imported from the model" inverted | survived |
  | The proposal's "that needs its own owner act" sentence deleted | survived |
  | POC-REQ-060's fixture limb changed | caught ("lacks Inferred fixture limb") |
  | A Part A signed row edited | caught |
  | An amendment row's disposition flipped | caught (totals) |

## Findings

**Finding 26 — POC-REQ-054's oracle does not observe two limbs of its own required behavior, and the matrix marks them covered** (revise)

[Observed] The required behavior is that every subject carries one identity,
and "every surface and the machine answer SHALL name that subject by that
identity and by no other" (applied spec.md:948–950). The oracle covers less in
two ways.

(a) **Machine-answer identities are not enumerated.** [Observed] The sweep
enumerates "over the union of the served surfaces, every element carrying a
subject identity" (applied spec.md:967–968). The machine answer enters the
sweep only through "every three-state slot on the surfaces and in the machine
answer" (applied spec.md:970–971). The spec's reader notes keep "human
surface" and "machine answer" as two distinct observation points (applied
spec.md:24–27). So a machine-answer entity whose id differs from the one the
surfaces render is not in the identity population. [Inferred] "Served
surfaces" might be read to include `GET /api/poc`, but nothing defines it that
way. On the ordinary reading of this file the machine-answer limb has no
denominator.

(b) **Subjects no source authority owns are exempt, and the exempt population
is undefined.** [Observed] The oracle-independence bullet says: "A subject no
source authority owns has no independently derived identity; the
identity-equality limb makes no claim for it" (applied spec.md:993–995).
"Source authority" is given only by example ("a work item's tracker, a code
region's source adapter", applied spec.md:951–952). No procedure decides
which subjects fall outside, which is a judgment step that CC-SPEC-4's
oracle bar ("by a stated procedure … without judgment") excludes.

[Inferred] For an exempt subject, Polaris and Orrery can name the same
subject by two different values and pass, unless a link joins them. The
oracle already attributes each element to its subject by source record
(applied spec.md:991–992), so a value-free consistency check is available:
every element attributed to one subject carries one identity value. The
oracle does not state that check.

**The matrix and scenario claim both limbs.**

- [Observed] Applied CONTRACT-COVERAGE.md:136 marks "RFC6-1 | One identity per
  subject on every surface and in the machine answer … | covered".
- [Observed] Applied CONTRACT-COVERAGE.md:140 marks "RFC6-3 | One subject
  identity resolves to the same subject on all three surfaces | covered", and
  its justification is "all surfaces read one model instance". That is an
  implementation fact, not something the oracle observes.
- [Observed] The scenario "One subject, one identity on every surface" says
  THEN "all three name it by the same identity value" (applied
  spec.md:1004–1012), counting the machine answer as one of the three.
- [Observed] No Unknown row lists either limb.

Criterion 2 (sweep and falsifier cover the requirement's scope) and criterion
3 (no covered row claims what the oracle does not observe) are not met for
this requirement.

Repair options:
- Put the machine answer's identity-bearing records into the sweep
  population.
- Either add the value-free consistency check for unowned subjects, or define
  the owned/unowned partition by a stated procedure and add an Unknown row for
  the unowned limb.
- Narrow the RFC6-1 and RFC6-3 covered rows to what remains observed.

**Finding 27 — POC-REQ-060's record-shape sweep counts records, not the entities, relationships and claims that must carry them** (revise)

[Observed] The required behavior quantifies over objects: "Every entity,
relationship and claim the shared model holds SHALL carry its epistemic state
in one record shape" (applied spec.md:1103–1105). The sweep quantifies over
records: it "enumerates every epistemic record in the machine answer — the
denominator is that population" (applied spec.md:1120–1121). The Scope line
says the same: "every epistemic record in the shared model and the machine
answer".

[Observed] The falsifier list names "a record with no label, a tier outside
its parent label, a reason outside the twelve or an Unknown with no route". It
does not name an entity, relationship or claim that carries no epistemic
record at all.

[Inferred] Such an object is absent from the denominator, so the sweep passes
over exactly the omission RFC6-14 calls a violation. RFC6-14 says "A machine
answer never omits epistemic state: an answer listing entities without their
labels … is a violation" (RFC-0006, about 15 lines after line 279).

[Observed] The new covered row claims presence for every object: "RFC6-14 |
Every entity, relationship and claim in the machine answer carries its label,
tier where one applies and primary Unknown reason …" (applied
CONTRACT-COVERAGE.md:149). The oracle observes vocabulary membership only for
the records that exist.

[Inferred] The signed RFC6-14 row (POC-REQ-020/042/051) may already cover
"never silently omits", but it covers it for those requirements' populations,
not the record shape this row claims.

Criterion 2 (falsifier and denominator match the required behavior) and
criterion 3 are not met. Repair: enumerate every entity, relationship and
claim in the machine answer as the denominator, check that each carries
exactly one record, and add "an entity, relationship or claim with no
epistemic record" to the falsifier.

**Finding 28 — RFC2-25's `asserted-by-worker` row has an unlisted limb and a covered consequence not anchored to its text** (revise)

[Observed] RFC2-25's `asserted-by-worker` row reads, in its Authority column:
"Visible, never green, challengeable, never a status input"
(`rendering-vocabularies.md`, the tier table under line 168). The new rows
split it as follows:

- covered: "is Inferred, absent from every Observed total and never clears an
  Unknown" (applied CONTRACT-COVERAGE.md:111);
- Unknown: "challengeable and never a status input" (applied
  CONTRACT-COVERAGE.md:112).

**The "Visible" limb is in neither row.** [Inferred] POC-REQ-060 requires an
Inferred record to render "with the declared Inferred encoding on every
surface where it appears" (applied spec.md:1161–1163). It does not require
the record to appear. An implementation that hides every Inferred record
passes. Criterion 3 requires every uncovered limb of a newly mapped clause
(RFC2-25 moves from B2 to A) to be listed as Unknown, and this one is not.

**"Never green" is not anchored.** [Observed] The covered row's "never clears
an Unknown" is not RFC2-25 text; it is closer to the "never a status input"
limb, which the next row lists as Unknown. [Inferred] The covered row's "never
green" equivalent ("absent from every Observed total") is a paraphrase, not
the clause's own consequence. Rule 8 asks for the claim to be anchored to the
clause's words.

Repair: add a "Visible" Unknown row, or require and observe rendering. Then
restate the covered row against RFC2-25's own limbs ("never green", rendered
distinctly from Observed) and move "never clears an Unknown" onto the anchor
it belongs to.

**Finding 29 — "Every other signed row is unchanged" overstates; the family table and computed prose also move** (note)

[Observed] `SEMANTIC-DELTA.md:314–317` says four Part B2 beliefs move and that
"Every other signed row is unchanged". The line-set difference also removes
three signed family-table rows (`| RFC2 | 27 | 7 | 0 | 20 |`,
`| RFC6 | 28 | 10 | 1 | 17 |` and the Total row) and five computed-figure
prose lines.

[Inferred] These are computed figures. The builder recomputes and checks them
(`totals_findings`, builder lines 309–345; `COMPUTED_LINES`, 404–410), so
criterion 4 is met in substance. The sentence should still say "every other
signed consequence or belief row", or name the computed rows.

**Finding 30 — `--check` leaves some signed and load-bearing spec and proposal bytes unguarded** (note)

[Observed] `spec_findings` compares only the text before `## ADDED
Requirements` and each requirement block (builder lines 232–238). The reader
notes sit between those two (applied spec.md:18–). For them it checks only
that the `POC-DIR-2026-09-21` key and its file are present. Once the
dependency file is regenerated over the mutated spec, three mutations survive:

- an edit to a signed reader-notes sentence;
- weakening POC-REQ-054's or POC-REQ-055's oracle-independence text;
- deleting the proposal's "that needs its own owner act" sentence. This is
  the one place Q4's "no production constructor" is made binding.

`companion_findings` checks that no signed proposal line is lost, but not the
new section's content beyond its heading (lines 442–443). Separately, the
`--check` success line prints a literal "26 requirements" (line 749) rather
than a computed count. It cannot be wrong while `spec_findings` pins the
population, but the brief asks for printed totals to equal computation.

[Inferred] The manifest digest freezes the reviewed bytes, so this is
defence-in-depth, not a defect in these bytes. Criterion 5 is met: every
declared mutant fails on its own predicate. Adding a reader-notes signed-line
check like `_lost_lines` and a phrase guard for the proposal's Q4 sentence
would close the gap.

**Finding 31 — POC-REQ-060's Inferred limbs rest on two undefined or weaker observations** (note)

[Observed] The required behavior says Inferred "SHALL arise only from an
agent's assertion". The oracle checks only "that it names an agent assertion"
(applied spec.md:1132). Naming an assertion is not arising from one.
`SEMANTIC-DELTA.md:271–286` discloses the lighter provenance limb, but no
Unknown row says the source limb is unobserved.

[Observed] The oracle's "a comparison of each Unknown it addresses before and
after it is added" (applied spec.md:1133–1134) needs a procedure for
"addresses", and none is stated. [Inferred] Recounting every Unknown in the
answer before and after is judgment-free and strictly stronger. Criterion 2
is met in substance, because the fixture-only population makes both limbs
testable.

**Finding 32 — POC-REQ-055's role-pair extension and one row's identifier** (note)

[Observed] The adopted design's slice-3 item 3 reads "Every emitted kind is
either an RFC1-25 name or carries an explicit out-of-vocabulary flag"
(`POLARIS-M9-ONE-IDENTITY-FUNNEL.md` lines 804–807). P-75 Q3 speaks of "the
seven outside kinds". The package widens the check to role pairs, read
through a checked-in kind-to-class declaration, which also catches the eighth
relationship (`contains`).

[Inferred] This is lawful and better, because RFC1-26 forbids re-typing and
the design's slice 8 already treats direction as material (lines 973–977).
The owner packet tells the owner (lines 113–122). Criterion 1 is met. But the
delta labels the join key as a "Departure from the adopted design" and does
not label this widening the same way. A one-line departure note would make
"nothing more than P-75 ruled" checkable by the owner.

[Observed] Separately, applied CONTRACT-COVERAGE.md:94 files "A closed-name
relationship honours its row's semantic class and rule" under RFC1-26. The
semantic-class and rule columns are RFC1-25's table. Only "no relation is
re-typed" is RFC1-26's. Splitting the row, or listing it under both, would
anchor each limb to its own clause.

## Criteria summary

1. **Ruling content: met.** [Observed] The package carries:
   - POC-REQ-054;
   - the POC-REQ-060 amendment;
   - POC-REQ-055;
   - the ribbon scenario ("A three-state view with nothing joined");
   - Q3's repair as a new requirement plus a dated disclosure, with the bound
     row preserved once;
   - Q4's typed landing zone, made binding in the proposed `proposal.md` and
     exercised only by a fixture.

   The role-pair widening is within the contract (Finding 32, note).
2. **The specification bar: not met.** Finding 26: POC-REQ-054's identity
   population omits the machine answer and an undefined set of unowned
   subjects. Finding 27: POC-REQ-060's denominator is records, not the objects
   that must carry them. Each new requirement otherwise has one form, a scope,
   a sweep with a denominator, an observable, oracle independence, a
   falsifier, and scenarios its text carries.
3. **Contract claims: not met.** Every quoted anchor matches its clause
   [Observed]. But the RFC6-1, RFC6-3 and RFC6-14 covered rows claim limbs the
   oracles do not observe (Findings 26 and 27). RFC2-25's "Visible" limb of a
   newly mapped clause is not listed as Unknown (Finding 28).
4. **Signed bytes: met.** [Observed] The tree is untouched, the six subjects
   match the readability successor's rows, the RFC1-26 bound row survives byte
   for byte, and the only consequence or belief rows that move are the four
   Part B2 beliefs. The computed family and prose figures also move, as
   Finding 29 notes.
5. **Mechanics: met.** [Observed] `--check` and `--selftest` pass, each of
   the 24 mutants fails on its own predicate, the dependency file equals
   regeneration, and the printed totals equal my independent computation.
   Finding 30 notes guard gaps.
6. **Honest claims: met.** [Observed] The package claims no adoption and
   schedules no implementation. It names the sign-off route, the
   reconciliation checker and census, and the version-tag recorder
   registration as residuals, each verified at source.
7. **Plain language: met.** [Inferred] The delta's "What this does not do"
   section and the owner packet's "What you would be signing" let a fresh
   reader restate what changes and what does not.
