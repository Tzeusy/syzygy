# R-M9-POC-VOCABULARY-EPISTEMIC-AMENDMENT-2 — fresh-context review, round 2, Three-Surface POC vocabulary and epistemic-record amendment
Reviewed commit: a4a864e657d586e783fb3f5febc1ad9a990a34bd
Manifest SHA-256: 559a5ea12f109f1e00e155420f19d1b46cc02c294691b713e720ae9482c6feb3
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context reviewer (Claude), 2026-10-15. I did not draft or
repair this package or the parked P-84 package. I read the package's files,
its builder, the governing references the brief lists, the round-1 raw, the
package's `ROUND-1-DISPOSITIONS.md`, and the parked package's six raws for
the census. I did not read PROJECT-STATUS, the pending register or bead
history. I read no observed-repository content.

## How this review was run

- [Observed] The clone at
  `/tmp/.../scratchpad/p108-r2-clone` has `git rev-parse HEAD` =
  `a4a864e657d586e783fb3f5febc1ad9a990a34bd`, and `git status --short` is
  empty. Every check below ran in that clone, or in byte copies of it
  (`cp -a`) where I applied patches or mutated files. Nothing in the clone
  was edited.
- [Observed] `Manifest SHA-256` above is `sha256sum` of
  `THREE-SURFACE-POC-VOCABULARY-EPISTEMIC-AMENDMENT-MANIFEST.txt`, the file,
  in the clone. I computed it myself; it differs from round 1's
  `03069d52…`, as the dispositions say it must after the regeneration.
- [Observed] `build_three_surface_poc_vocabulary_epistemic_amendment.py
  --check`: "manifest matches 6 proposed subjects (4 patched, 2 unchanged);
  26 requirements, Part A 78 clauses over 147 rows (105 covered, 42
  Unknown); structure, regeneration and the preserved RFC1-26 row verify".
- [Observed] `--selftest`: "82 structure mutants, two subject-change
  mutants, patch drift, manifest order and subject drift all fail closed on
  their own predicates".
- [Observed] `build_three_surface_poc_spec_dependencies.py --check` in the
  clone (unpatched): 25 requirements, 88 distinct authorities, matches
  regeneration. In a copy with the four patches applied by `patch -p1`: 26
  requirements, 90 distinct authorities, matches regeneration.
- [Observed] `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".
- [Observed] In the patched copy, `sha256` of all six subjects equals the
  six manifest rows (6 of 6 match, my own script).
- [Observed] Independent counter (my own script; it imports nothing from the
  builder and parses the `| RFC` rows per `##` Part section). Patched
  `CONTRACT-COVERAGE.md`: Part A 147 rows over 78 clauses, 105 covered and
  42 Unknown; 25 rows carry "Amendment row (vocabulary and record shape)",
  18 of them Unknown (so 7 covered); Part B1 29 rows over 28 clauses; Part
  B2 218 rows and clauses; 78 + 28 + 218 = 324; no clause in two parts; the
  Part A clause set equals the `contracts:` union of the patched spec's
  warrant blocks (78). Signed file: 122 / 77 / 98 / 24, B1 29 / 28, B2 219.
  The printed totals in the matrix, delta, ledger and dispositions match.
  The patched spec has 26 requirement and 28 scenario headings.
- [Observed] Line-multiset diff, signed against patched. `CONTRACT-COVERAGE.md`
  loses exactly 8 lines: the RFC2 and Total family rows, the two Part A
  totals lines, the RFC2-25 Part B2 row, the Part B2 total line and the two
  "Verifying this table" figure lines. `proposal.md` loses 0 lines;
  `design.md` and `.openspec.yaml` are unchanged. The RFC1-26 closure row
  occurs once before and once after. The POC-REQ-014, -020, -051, -052,
  -053 and -061 blocks are byte-identical. The patched spec and matrix name
  `POC-REQ-054` 0 times. The spec loses only the reader-notes lines the
  builder lists and lines of the old POC-REQ-060 block; the signed scenario
  "Unknown looks the same everywhere" survives (builder predicate, and my
  reading of the diff).
- [Observed] Round-1 against round-2 patch diff (`git show 6d3923f3:` of the
  two patches, compared with the reviewed ones): the changes are exactly the
  repairs the dispositions table lists; no other proposed line moved.
- **Rule-6 probes of my own**, on a byte copy's patch files, each restored
  after its run:
  - [Observed] New guard: "three pairwise distinct entries" → "three distinct
    entries" fails with "POC-REQ-060 lacks label entries pairwise distinct"
    (plus the expected dependency and manifest findings).
  - [Observed] New guard: the tier-Semantics Unknown row flipped to
    `covered` fails with "RFC2-25 Unknown row missing or not Unknown: A
    record carries a tier only where that tier's Semantics column holds"
    (plus totals and manifest).
  - [Observed] New guard: "every count the machine answer serves" → "every
    count the machine answer marks Observed" fails with "POC-REQ-060 lacks
    Observed totals named".
  - [Observed] Outside the guards: deleting "zero equal label entries," from
    060's oracle, and deleting the 055 oracle's "or marked by a rendered
    element that carries no reason" limb, each fail only on the dependency
    file's spec digest and the manifest. Flipping the unguarded "Visible"
    Unknown row to `covered` fails only on the Part A totals and the
    manifest. So those sentences are frozen by digest only, as the brief
    says. [Inferred] 11 of the 18 amendment Unknown rows are outside
    `UNKNOWN_ROWS`; that is the declared design, not a finding.
  - (One probe of mine, deleting a whole patch line, produced a corrupt
    patch rather than a test of a predicate; I discarded it.)

**Census re-derivation.** [Observed] From the six raws' `**Finding N — …**
(level)` headings (my script, Python `re`): round 1 = 1–11, round 2 = 12–19,
round 3 = 20–25, round 4 = 26–32, round 5 = 33–38, round 6 = 39–43; 43
findings, ids 1–43 with no gap; line 4 of each raw is `Verdict: REVISE`;
the 14 `(revise)` headings are 1, 2, 3, 4, 5, 12, 13, 20, 26, 27, 28, 33,
39, 40; no `(blocking)`. The theme table partitions 1–43 exactly once; each
row's count, revise count and members, "last round with a finding" and
"last revise" reproduce (054: 13 / 7, 6, 6; 054+060: 2 / 2, 1, 1; 055:
6 / 3, 4, 3; 060: 9 / 2, 5, 4; guards 5 / 0, 6; prose 8 / 0, 6). See
finding 10 for the new placement sentence.

**Marker populations (round-1 finding 2).** [Inferred] Both rendering limbs
are now quantified over a stated population: POC-REQ-055 over "every
rendered element that marks the relationship", an element marking it when
it carries the served `id` in a declared relationship marker, with the
complete marker population as the counted, reported denominator; POC-REQ-060's
Inferred limb the same way through declared record markers. Required
behaviour, Scope, sweep, observable, oracle, falsifier and scenario all say
it. Every rendering outside the population has an Unknown row: RFC1-26 "A
flagged relationship rendered in an element that carries no declared
relationship marker shows its flag and reason there" and RFC2-25 "An
`asserted-by-worker` claim renders unlike Observed in a rendering that
carries no declared record marker". The two covered rows are narrowed to
the marked elements. See finding 13 for the empty-population case.

**POC-REQ-014 re-judged against the amended POC-REQ-060.** [Inferred]
014's encoding arm ("Every rendered item's governing-intent encoding equals
the encoding the declared table of POC-REQ-060 gives Unknown, and none
carries an encoding the table gives any other state") is now decidable over
the three labels: 060 requires "three pairwise distinct entries" and its
oracle and falsifier check that, so the Unknown entry differs from the
Observed and Inferred entries. 014's RFC2-24 row (governing-intent reason
and route), and its RFC8-23/RFC8-24 rows, still claim only what 014's
oracle observes; none of them reads 060's record shape, and 060's Scope puts
every epistemic value outside the entity and relationship lists outside its
record-shape population, with an RFC6-14 Unknown row for them. One residual
is finding 14.

**"An Observed total" (round-1 finding 7).** See finding 12.

## Findings

**Finding 10 — the census's new "seven headings" sentence copies round 1's population instead of re-deriving it** (note)

[Observed] `SEMANTIC-DELTA.md` lines 74–77 now read: "Seven headings name no
requirement, so a reader applying a heading-only rule cannot place them;
their placements are listed here: 3 and 4 …, 6 and 35 …, and 7, 36 and 41".
The tag says "the seven headings re-read". [Observed] A sweep of all 43
headings for a requirement identifier (`POC-REQ-\d{3}`, or a bare `054`,
`055` or `060`) finds 26 headings with none. Twelve of those are in the guard
and prose themes, which need no requirement. The other 14 are in requirement
themes: 3, 4, 5, 6, 7, 14, 15, 16, 20, 28, 35, 36, 39 and 41. Seven of them
(5 "join key", 14 "The Inferred scenario", 15 "a code region's [identity
owned]", 16 "Q4's 'no production constructor' limb", 20 "The RFC1-26
disclosure row", 28 "RFC2-25's `asserted-by-worker` row", 39 "the identifier
field") point at a requirement by subject matter, not by identifier. Heading
6 ("the new tier row") and heading 35 ("'never green'") do the same, yet they
are in the delta's seven. [Inferred] The seven is round 1's list (its
finding 3), and the predicate that separates it from the other seven is not
stated. A reader cannot apply "name no requirement" and get seven. The
table and its counts are unaffected, because placement is now by body. Fix:
list all 14 heading placements, or state the predicate (for example "by
identifier") and its count of 14.

**Finding 11 — sentences saying the owner's directions are "not recorded under `decisions/`" are stale and unmarked in the delta and packet** (note)

[Observed] `.syzygy/governance/decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-3-2026-10-14.md`
records both directions: line 27 quotes P-84's "Park, redraft narrower"
answer, and line 108 records "P-108: 'One cycle'". `ROUND-1-DISPOSITIONS.md`
lines 35–38 mark its own copy of the claim as no longer true. The package's
other copies stand unmarked:

- `SEMANTIC-DELTA.md` lines 14–16: "One cycle" "[Observed: as relayed by the lead
  session; not recorded under `decisions/`]";
- `SEMANTIC-DELTA.md` lines 58–59, for the park direction: "not recorded under
  `decisions/`";
- `OWNER-DECISION-PACKET.md` line 179, under D4: "[Observed: as relayed; no
  decision record holds it yet.]".

`REVIEW-BRIEF.md` lines 166–167 repeat the claim, but briefs are not edited.
[Inferred] The cycle-3 record says the packet, delta and brief "belong to
that lane", so the records lane left them alone on purpose. They are still
false present-tense sentences that a signer reads, and the D4 one carries
an `[Observed]` label. They are the stale-sentence class of parked findings
38 and 43. D4's recommended "Record it" arm may still have content, since
the record may not state the narrowing of P-75 Q1 in those words; I did not
judge that. Fix: mark each at the sentence, dated, keeping the old text.

**Finding 12 — "Observed total" now has a population, but "count" and the recount procedure still need judgment, and the population takes in label-agnostic totals** (note)

[Observed] POC-REQ-060's Scope (patched spec lines 1201–1203) reads "An
Observed total is every count the machine answer serves, except a count the
machine answer declares to be of Inferred records". The oracle reads "a
recount of every Observed total without it, each of which must equal the
count served with it". The scenario reads "changes no Observed total the
machine answer serves".

[Inferred] This closes round 1's "no population named" in form, but three
gaps remain.

- **"Count" is not defined.** A checker must still decide which served
  numbers are counts.
- **The recount procedure is not stated.** To "recount" a served count
  without the injected record, a checker needs that count's membership
  rule, and the specification gives none. The judgment-free procedure the
  wording suggests is a differential: serve once with the fixture and once
  without, then compare each count. That is not what the text says.
- **The population is wider than doctrine's "Observed total".** A
  label-agnostic total that includes the injected entity or relationship,
  such as "N relationships, one of them Inferred", is a served count not
  "declared to be of Inferred records". The falsifier "an Inferred record
  counted in an Observed total" then fires on a total that RFC6-17-style
  composition disclosure would allow.

The covered RFC2-25 "never a status input" row repeats the same
definition, so it claims no more than the oracle reads. That is why this is
a note and not a revise. Fix: name the procedure (a with/without
differential of every served count), or make the declared counts an
enumerated list; and say whether a label-agnostic total must leave Inferred
members out.

**Finding 13 — an empty or implementation-chosen marker population passes both rendering limbs at a reported zero** (note)

[Observed] Both requirements define the rendering population through "the
surfaces' declared relationship markers" and "declared record markers".
Neither says where the declaration lives or who writes it, and neither
requires it to be non-empty. Both oracles decide by "zero … decide" counts.
For POC-REQ-060 the "Visible" Unknown row says "no requirement requires one
to appear", so the fixture's marker population may be empty by design.
[Inferred] An implementation that declares no relationship marker, or marks
only some renderings, passes the rendering limb of 055 and the encoding limb
of 060 with whatever denominator it chooses, possibly 0. The check reports
that number, but nothing in the text says that a zero marker population
decides nothing (VIS-2: no evidence is never zero). This is POC-REQ-020's
signed form, and the two unmarked-rendering Unknown rows carry every
unmarked rendering. So the covered rows overclaim nothing; with zero
markers, every rendering falls under those Unknown rows. A signer reading
the covered RFC1-26 disclosure row is not told that its rendering limb can
be covered on an empty population. Packet Question 2 is the right place for
the trade-off. One sentence there, or in the Unknown rows, would make it
visible.

**Finding 14 — POC-REQ-014's "any other state" also reaches reason or tier entries, which the pairwise rule does not separate from the Unknown entry** (note)

[Observed] The amended POC-REQ-060 encodes "epistemic states (Observed,
Inferred, Unknown, and their reasons)". Its new distinctness rule covers
"Observed, Inferred and Unknown three pairwise distinct entries" only.
[Inferred] If the declared table gives a reason, or a tier such as
`suspended` or `declared-only` (both under Unknown), an entry of its own,
POC-REQ-014's arm becomes ambiguous. It reads "none carries an encoding the
table gives any other state". A reader cannot tell whether a reason-specific
Unknown entry counts as an "other state", and nothing requires such an
entry to differ from the bare Unknown entry. The ambiguity predates this
package in the signed "and their reasons", and the package narrows it. It
is not closed for reason and tier entries. The delta's "so it is decidable"
(§2 "POC-REQ-014") holds over the three labels only. Say so there, or extend
the rule to every entry the table declares.

**Finding 15 — the tier-Semantics Unknown row is a paraphrase that the dispositions call a quotation, and it leaves out one Semantics limb** (note)

[Observed] `ROUND-1-DISPOSITIONS.md` row 1 says the new row names "each of
the five other tiers' Semantics cell (quoted from
`RFC-0002/rendering-vocabularies.md`'s RFC2-25 table)". The row paraphrases
instead ("`report-fact` only for a fact about a report", "`declared-only`
only for a declaration whose satisfaction is unverified"). It leaves out
the `suspended` cell's limb "The basis and, where inferred, the challenger's
provenance render alongside" (RFC2-25 table, line 182). Neither this row nor
the Authority Unknown row ("`suspended` never erases its basis") lists that
limb. [Inferred] The row's head clause, "A record carries a tier only where
that tier's Semantics column holds", reaches the whole column. So the
missing limb is Unknown in substance, and round-1 finding 1 is closed (see
below). The paraphrase still reads as the full content, and rule 8 asks
that a contract claim be quoted. Fix: quote the cells, or add "among other
limbs".

**Finding 16 — the finding-9 repair cites POC-REQ-020 for a property that POC-REQ-020 does not decide** (note)

[Observed] The new Scope sentence reads "The shared model's records are
observed through the machine answer, which serves the shared model's fact
set (POC-REQ-020); no check reads the shared model directly". POC-REQ-020
decides that "Every fact a client-rendered surface presents SHALL be present,
with equal value, in the machine answer". That is the rendered set inside the
machine answer, not the machine answer equal to the shared model.
[Inferred] An entity the shared model holds but the machine answer does not
serve is outside 060's sweep. That is honest: the sentence says no check
reads the model. But it rests on a citation that is not a reliance (rule 5).
RFC6-13 ("Machine endpoint answers from the same fact set surfaces render"),
already in Part A, is the closer anchor. No covered row claims the
shared-model limb, so this is a note.

**Round-1 findings, closed or not, at the reviewed bytes** [Inferred unless
marked]

1. *RFC2-25 Semantics listed for one tier only* — **closed.** [Observed] A
   new Unknown row names the other five tiers' Semantics, with the
   justification "validates tier membership and nesting only". It is
   guarded, and my mutant fails on it. Note 15 is a residual on its
   wording.
2. *"every rendering" with no population* — **closed.** The reviewer's
   second option was taken: marked population, counted denominator, two
   Unknown rows, and owner Question 2. Note 13 is a residual.
3. *census placement rule* — **closed as to the rule.** "By the requirement
   its body addresses" produces the table. The added sentence is
   new repair text with its own defect (note 10).
4. *060 distinct from Observed only; "the legend"* — **closed.** Pairwise
   distinctness is required, compared and falsified, and "the legend" is
   gone from the spec and the RFC2-25 row. Note 14 is a residual over reason
   and tier entries.
5. *"claim" justification false since P-100* — **closed.** [Observed] The
   delta §2 change 1 names both claim kinds and quotes the signed RFC2-24
   and RFC8-24 rows. The packet line 46–50 corrects its sentence with a
   dated mark.
6. *reader-note "its `Group` line does"* — **closed.** [Observed] The
   sentence now reads "its `Group` line places it in *Cross-cutting
   experience*", and the guard checks it.
7. *Observed totals unnamed; Unknown sets pooled* — **pooling closed**
   ([Observed] keyed "by the list it is served in and the identifier");
   **population partly closed** (note 12).
8. *doctrine's separate-layer and VIS-7 limbs* — **closed.** [Observed] The
   delta quotes `trust-and-evidence.md` and defers both limbs to the
   constructor's act; the packet says so in one sentence.
9. *"in the shared model" with a machine-answer-only oracle* — **closed**,
   by a Scope sentence. Note 16 is a residual on its citation.

**Criteria summary** [Inferred]: 1 met; 2 met (counts reproduce; note 10);
3 met (notes 12–14); 4 met (notes 15–16); 5 met; 6 met; 7 met (five
residuals named; no adoption claimed; no implementation scheduled; note 11
on stale sentences); 8 met.

**Counts:** blocking 0, revise 0, note 7 (findings 10–16).
