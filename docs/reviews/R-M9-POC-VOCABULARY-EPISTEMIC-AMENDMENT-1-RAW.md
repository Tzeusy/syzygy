# R-M9-POC-VOCABULARY-EPISTEMIC-AMENDMENT-1 — fresh-context review, round 1, Three-Surface POC vocabulary and epistemic-record amendment
Reviewed commit: 6d3923f365bca6e4458200ac0f75381655ef5bb6
Manifest SHA-256: 03069d521ae3280f2abf8525950d74e3a128cec1db140218efa3372791a75cba
Verdict: REVISE

Reviewer: fresh-context adversarial reviewer (Claude), 2026-10-14. I did not
draft this package or the parked P-84 package. I read only the brief's
governing references, the package, its builder, the signed subject at the
reviewed commit, and (for the census check) the six P-84 raws.

## How this review was run

- Worktree detached at the reviewed commit and `git rev-parse HEAD` read
  back as `6d3923f365bca6e4458200ac0f75381655ef5bb6`. All checks ran in a
  separate `git clone` of that commit (verification rule 7), not the
  worktree.
- `Manifest SHA-256` is `sha256sum` of
  `THREE-SURFACE-POC-VOCABULARY-EPISTEMIC-AMENDMENT-MANIFEST.txt`, the file,
  in that clean clone.
- [Observed] `build_three_surface_poc_vocabulary_epistemic_amendment.py
  --check`: "manifest matches 6 proposed subjects (4 patched, 2 unchanged);
  26 requirements, Part A 78 clauses over 144 rows (105 covered, 39
  Unknown); structure, regeneration and the preserved RFC1-26 row verify".
- [Observed] `--selftest`: "69 structure mutants, two subject-change
  mutants, patch drift, manifest order and subject drift all fail closed on
  their own predicates".
- [Observed] `build_three_surface_poc_spec_dependencies.py --check` on the
  unpatched tree: 25 requirements, 88 authorities, matches regeneration. In
  a second clone with the four patches applied by `git apply`: 26
  requirements, 90 authorities, matches regeneration.
- [Observed] `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".
- [Observed] In the patched clone, `sha256sum` of all six subjects equals
  the six manifest rows byte for byte.
- [Observed] An independent counter (my own script, importing nothing from
  the builder) over the patched `CONTRACT-COVERAGE.md`: Part A 144 rows over
  78 clauses, 105 covered / 39 Unknown; 22 rows carry "Amendment row
  (vocabulary and record shape)", 7 covered / 15 Unknown; Part B1 29 rows
  over 28 clauses; Part B2 218 rows/clauses; the Part A clause set equals the
  78-identifier `contracts` union of the regenerated dependency file. On the
  unpatched file: 122 / 77 / 98 / 24, B2 219. Every printed total in the
  delta, ledger and matrix matches.
- [Observed] Line-multiset diff, signed vs patched (my script): the only
  signed `CONTRACT-COVERAGE.md` lines removed are the RFC2 and Total family
  rows, the two Part A totals lines, the RFC2-25 Part B2 row, the B2 total
  line and the two "Verifying this table" figure lines (8 lines). `proposal.md`
  loses 0 lines; `design.md` and `.openspec.yaml` are unchanged. The RFC1-26
  row "Relations outside the closed table don't exist; no prose-widening |
  covered | POC-REQ-052" occurs exactly once before and after. The
  POC-REQ-014, -020, -052, -053 and -061 blocks are byte-identical before
  and after. The signed scenario "Unknown looks the same everywhere" is
  preserved verbatim. The patched spec names `POC-REQ-054` 0 times, and has
  26 requirement and 28 scenario headings.
- Rule-6 probes of my own, on the clone's patch file (then restored with
  `git checkout`): deleting the guarded phrase "(reversed roles included)"
  makes `--check` fail with "POC-REQ-055 lacks reversed roles falsify" (plus
  the expected manifest and dependency findings). Weakening the unguarded
  oracle text "rendered or answered without their reason decide" to
  "answered without their reason decide" makes `--check` fail only on the
  manifest and dependency digests, as the brief says sentences outside the
  guards are frozen only by digest.

**Parked-package raws read (for non-reintroduction only):** the finding
headings of all six `R-M9-POC-IDENTITY-AMENDMENT-{1..6}-RAW.md` (findings
1–43), and the bodies of findings 3 (round 1), 17 (round 2), 27, 28, 31 and
32 (round 4). I compared the parked proposed `spec.md.patch` POC-REQ-055 and
POC-REQ-060 blocks with this package's. POC-REQ-055 is identical. Against
the parked findings on 055/060 (2, 6, 8, 13, 14, 16, 17, 20, 21, 25, 27, 28,
31, 32, 35) I found none reintroduced: 27's denominator is now the list
elements; 28's "Visible" Unknown row and anchored "never green" row are
present; 31's "addresses" is replaced by a whole recount; 35's `[Inferred]`
tag is present; 14's scenario asserts no tier; 16's Q4 sentence is in the
proposal and guarded; 17's narrowing is stated; 6's fold disclosure is
present; 2, 20 and 21's Unknown rows are present. Findings 1 and 2 below are
not in any parked raw (I swept the six raws for "every rendering", "beside
every", "rendering of a relationship", "wherever the relationship",
"Semantics", "report-fact" and "reduced-fidelity": the only tier hit is
round-1 finding 3's per-tier *Authority* list).

**Census re-derivation.** [Observed] From the six raws' headings: round 1 =
findings 1–11, round 2 = 12–19, round 3 = 20–25, round 4 = 26–32, round 5 =
33–38, round 6 = 39–43; 43 findings, every raw `Verdict: REVISE` on line 4.
The 14 headings labelled `(revise)` are 1, 2, 3, 4, 5, 12, 13, 20, 26, 27,
28, 33, 39, 40. The theme table's membership, counts (13 + 2 + 6 + 9 + 5 + 8
= 43; 7 + 2 + 3 + 2 = 14) and its "last round" columns all reproduce. See
note 3 for the placement rule.

**POC-REQ-014 re-judged against the amended POC-REQ-060 table** (brief,
carried from the P-100 round-3 raw's note 4). [Inferred] The encoding arm
("Every rendered item's governing-intent encoding equals the encoding the
declared table of POC-REQ-060 gives Unknown, and none carries an encoding
the table gives any other state") stays decidable with an Inferred entry
added, *provided* the table's Unknown entry differs from every other entry.
The amended 060 requires distinctness only from Observed (note 4). The
RFC2-24 row (line 100) and RFC8-23/RFC8-24 rows (lines 162, 168–172) for
POC-REQ-014 still claim only what 014's oracle observes: none of them reads
060's record shape, and 014's `governedBy` sits in the machine answer's
`workItems`, outside the entity and relationship lists
(`packages/three-surface-poc-core/src/model.ts` lines 185–189), so it is
outside 060's record-shape population and inside the new RFC6-14 Unknown
row. See note 2 for the delta's description of that claim.

## Findings

**Finding 1 — RFC2-25's Semantics column is listed as an Unknown limb for one tier only; the other five tiers' Semantics are unlisted** (revise)

[Observed] RFC2-25 moves from Part B2 to Part A, so every uncovered limb of
it must be listed as Unknown (criterion 4; the matrix's own head says "a
reviewer who finds an unlisted limb has found a real gap"). The clause's
table has two normative columns per tier: Semantics and Authority
(`RFC-0002/rendering-vocabularies.md` lines 175–182). The package lists:

- every tier's Authority column, as one Unknown row: "Each tier keeps its
  authority: only `gate-backed` supports a positive status; `report-fact`
  speaks of the report only; …";
- the `asserted-by-worker` Semantics column, as its own Unknown row:
  "An `asserted-by-worker` claim arises from "An LLM worker's assertion of an
  outcome with no retained artifact"". The delta explains why: "the oracle
  checks that a record *names* an assertion, not that it *arose* from one".

[Observed] The other five Semantics cells have no row. For example
`gate-backed`: "The claim is backed by a retained, resolvable gate artifact
(report, log, run record) bound to the exact revision (SDR-9)";
`reduced-fidelity`: "Deterministic at a declared coarse granularity …";
`declared-only`: "the declaration is Observed; its satisfaction is Unknown";
`suspended`: "An Unknown that carries a visible deterministic or
authoritative basis under question — open challenge (#9) or contradiction
(#8)".

[Inferred] POC-REQ-060's oracle validates "the closed label, tier and reason
vocabularies" and "tier nesting" only. A record tagged `gate-backed` with no
gate artifact, or `suspended` with no open challenge or contradiction,
passes it. The covered row "A rendering tier, where a record carries one, is
one of the closed six and sits inside its parent label" is honest about
that, but the limb "a record carries a tier only where that tier's
Semantics hold" is uncovered and unlisted. The package's own treatment of
the `asserted-by-worker` Semantics as a separate limb shows it reads these
cells as limbs, so the omission is internal inconsistency, not a reading
choice. This is the same class as parked round-1 finding 3 and round-4
finding 28, both revise.

Repair: one Unknown amendment row under RFC2-25, for example "A record
carries a tier only where that tier's Semantics column holds (`gate-backed`,
`report-fact`, `reduced-fidelity`, `declared-only`, `suspended`)", with the
justification that POC-REQ-060's oracle validates membership and nesting
only. Recount the totals (145 rows, 40 Unknown).

**Finding 2 — POC-REQ-055's rendering limb, and POC-REQ-060's Inferred rendering limb, quantify over "every rendering" with no stated population, denominator or attribution procedure** (revise)

[Observed] POC-REQ-055 requires "The flag and its reason SHALL be carried in
the machine answer and rendered wherever the relationship is rendered". Its
Scope adds "every rendering of a relationship on any surface". Its sweep
gives denominators only for the machine answer ("the denominators are that
population and its distinct kinds") and then "checks every flagged
relationship for a non-empty reason in the machine answer and beside every
rendering". The oracle's last limb is "zero flagged relationships rendered
or answered without their reason". The scenario's THEN is "every surface
that renders it carry the relationship's outside-closed-vocabulary flag and
reason".

[Observed] POC-REQ-060's new limb is the same shape: an Inferred record
"renders with the declared Inferred encoding on every surface where it
appears", decided by "an encoding comparison with the declared Inferred
entry"; the falsifier includes an Inferred record "rendered with the
Observed encoding".

[Inferred] Neither requirement says how a checker finds the renderings of a
given relationship or record, or what counts as one. CC-SPEC-4 requires, for
an invariant, "the sweep whose denominator bounds it", and an oracle that
decides "by a stated procedure that terminates in bounded effort, without
judgment". The signed POC-REQ-020 solves the same problem with "the surfaces'
declared parity markers — the denominator is the complete marker
population"; POC-REQ-055 and -060 cite no such mechanism. At the reviewed
commit relationships are rendered in at least three ways
(`apps/three-surface-poc/src/exact-tables.ts` line 50 `data-relationship-id`;
`polaris.ts` lines 277 and 279 `data-claim-provenance` /
`data-unknown-disclosure`), and nothing in the spec makes a rendering carry
any of them. A Polaris sentence that states a flagged relationship without
a marker is a rendering no sweep enumerates, so "rendered without its
reason" cannot be falsified there. For 060, the signed per-encoding sweep
compares each encoding with the table but does not say which record an
encoding renders, so an Inferred fixture rendered with the Observed encoding
looks like one more correct Observed encoding.

[Inferred] This is the element-to-subject attribution gap that the delta's
census names as the root of POC-REQ-054's non-convergence (findings 24, 33,
40: "no declared, reviewed mapping from rendered elements to source
records"), in a weaker form: here the target is a served identifier, not a
source record, so it is repairable inside this package. The delta says
"Neither needs a subject identity"; that holds, but both still need a
declared attribution of a rendered element to the served `id`, and
criterion 3 asks that nothing in 055 or 060 lean on what was deferred.

Repair: name the rendering population, for example "every rendered element
carrying the relationship's served `id` in a declared marker, the
denominator being the complete marker population, which the check counts
and reports" (POC-REQ-020's form), in 055's Scope, sweep and scenario, and
the same for an Inferred record's rendering in 060. Alternatively narrow the
rendering limbs to that marked population and add an Unknown row for
unmarked renderings.

**Finding 3 — the census's stated placement rule is not the rule that produced the table** (note)

[Observed] The delta says "Each finding is placed in exactly one theme, by
the requirement its heading names; the two findings whose headings name more
than one requirement form their own row." The headings of findings 3
("Uncovered limbs of newly mapped clauses are not listed as Unknown") and 4
("Several falsifier limbs have no deciding oracle, …") name no requirement
at all. Findings 6, 7, 35, 36 and 41 also name none in their headings and
are placed by content. [Inferred] The counts reproduce, so the conclusion
stands, but a reader applying the stated rule cannot place seven of the 43.
State the rule as "by the requirement the finding's body addresses", or list
the seven placements.

**Finding 4 — the amended POC-REQ-060 requires Inferred to differ only from Observed, which leaves POC-REQ-014's encoding arm satisfiable only by an unstated choice** (note)

[Observed] 060 requires an Inferred state to "render with an encoding the
legend distinguishes from Observed", and its falsifier lists only "rendered
with the Observed encoding". Nothing requires the table's Inferred entry to
differ from its Unknown entry, and no oracle limb checks that the table's
entries are pairwise distinct. 060's required behaviour also says "the
legend" while its oracle reads "the declared Inferred entry" of the table.
[Inferred] If a table gave Inferred and Unknown one encoding, 060 passes,
and POC-REQ-014's arm ("equals the encoding … POC-REQ-060 gives Unknown, and
none carries an encoding the table gives any other state") can never pass.
The signed table already had the same latent gap for Observed against
Unknown, so this extends it rather than creating it. Requiring the three
label entries to be pairwise distinct, and saying "the declared table" in
place of "the legend", would close it.

**Finding 5 — the delta's reason for dropping "claim" misdescribes the signed specification since P-100** (note)

[Observed] SEMANTIC-DELTA §2 change 1 says "The POC specification defines
no "claim" object for the machine answer. The only claims it serves are the
project-shape plane's". The P-100 rows now signed name another: the RFC2-24
row reads "on every served item's governing-intent claim" (signed
`CONTRACT-COVERAGE.md` line 100) and an RFC8-24 row reads "the
governing-intent claim on every work item" (line 168). The OWNER-DECISION-PACKET
repeats the premise: "not "claims", which the POC specification never
defines". [Inferred] The proposed bytes are honest regardless: 060's Scope
says "No other epistemic value the machine answer serves is in the
record-shape population", and the RFC6-14 Unknown row "Every claim instance,
and every other epistemic value … outside its entity and relationship lists"
covers the governing-intent claim. Only the justification sentence in the
delta and the packet is false, and a signer reads the packet's version.

**Finding 6 — the reader-note sentence about POC-REQ-055's group reads as placing it in Orrery** (note)

[Observed] "POC-REQ-055 carries the identifier the owner's ruling named; its
number range does not place it in the Orrery group, its `Group` line does."
[Inferred] The elliptical "its `Group` line does" completes as "places it in
the Orrery group", the opposite of the intent (055's Group line is
Cross-cutting experience, and the same note lists "(055, 060–061)" under it).
The sentence is a guarded phrase (`READER_NOTE_PHRASES`), so the builder
freezes the misreading. VIS-3: "its `Group` line places it in Cross-cutting
experience" says it plainly.

**Finding 7 — two procedures in POC-REQ-060's Inferred recount are under-specified** (note)

[Observed] The oracle requires "a recount of every Observed total without
it". [Inferred] No population of "Observed totals" is named, so which served
figures the checker recounts is a judgment; the scenario's "appears in no
Observed count" has the same gap. Separately, the Unknown recount compares
two sets "each member named by the identifier the machine answer serves it
under", pooled across the entity and relationship lists; nothing requires
entity and relationship ids to be disjoint, so an id shared across the two
lists could mask a cleared Unknown. [Observed] At the reviewed commit the ids
use distinct prefixes (`project:…`, `relationship:…` in `poc-seeds.ts`), so
this is latent. Key the sets by (list, id), and name the totals (or say
"every count the machine answer serves").

**Finding 8 — doctrine's separate-layer rule for Inferred is not in the stated narrowing** (note)

[Observed] Doctrine says "Deterministic facts and probabilistic inferences
are computed and stored apart" and "The inferred layer is a separate
artifact that records the model, version, and inputs that produced it, …
and is excluded from the VIS-7 identity test"
(`trust-and-evidence.md` lines 112–117). POC-REQ-060 places Inferred records
inline on the shared model's entities and relationships. The delta's
"A narrowing of doctrine's Inferred, stated" paragraph discloses only the
provenance limb (model, version, inputs). [Inferred] With a fixture-only
population and no production constructor this binds nothing today, but the
storage and VIS-7-exclusion limbs (relevant to POC-REQ-004's determinism and
any response-identity digest) are a second narrowing a signer is not told
about. One sentence in the narrowing paragraph, deferring both to the
constructor's own act, would disclose it.

**Finding 9 — POC-REQ-060's record shape binds "in the shared model" but its oracle reads only the machine answer** (note)

[Observed] Required behaviour: "SHALL carry its epistemic state in one
record shape, in the shared model and in the machine answer". Scope and
sweep enumerate only "every element of the machine answer's entity and
relationship lists". [Inferred] The shared-model limb is observed only
through the machine answer (which RFC6-13/POC-REQ-020 parity makes a fair
proxy), and no Unknown row or sentence says so. Either drop "in the shared
model" from the obligation or say that the machine answer is its observable.

**Counts:** blocking 0, revise 2 (findings 1 and 2), note 7 (findings 3–9).

Criteria summary [Inferred]: 1 met; 2 met in substance (counts reproduce;
note 3); 3 not met (finding 2); 4 not met (finding 1); 5 met; 6 met; 7 met
(five residuals named, no adoption claimed, no implementation scheduled);
8 met apart from note 6.
