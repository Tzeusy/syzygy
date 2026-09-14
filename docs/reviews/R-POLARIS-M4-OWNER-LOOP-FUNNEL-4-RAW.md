# R-POLARIS-M4-OWNER-LOOP-FUNNEL — review 4 (raw, retained verbatim)

Independent fresh-context review. Read-only throughout: no file in any repo
or worktree was edited, no state-changing git command was run, no `bd`
write, no daemon, no network, no read of the observed repository's
checkout. The single file written is this one.

## What was reviewed

Worktree `…/scratchpad/m4wt`, branch `agent/syzygy-dov.4`, HEAD
`181797a4390e6b3f9afbd618efb5009db6bf1d89` (2026-09-15), working tree clean
(`git status --porcelain` empty), so all three artifacts are tracked at that
commit.

Byte sizes and digests computed this session with `wc -c` and `sha256sum`,
never transcribed:

| File | Bytes | sha256 |
|---|---|---|
| `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md` | 162860 | `267278fae7af380383eeeec2adc73c44c025c3963f1829ee8d1fdf8aee567411` |
| `docs/evidence/polaris-m4-owner-loop-funnel-2026-09-14.json` | 49243 | `d2ebbeae3e3cdaf493ae95abbb902329b4b73d44b1f680e7a0e1401a6e842a61` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 35850 | `a2f7d338a8728e859fb8e11728b885bbbf77d47a3414c24a7c76c217805d5916` |

The three retained raws re-hashed this session, each matching the figure the
packet cites for it: review 1 47636 bytes
`6983034196c706c213e2a939e0ca7dfe4c3f75f958378403fbd115112c2966ec`; review 2
39050 bytes
`a7b3782882e41cf954e1dda326f502e20eceea4acd05732625de9f9ee2654649`;
review 3 31656 bytes
`ebce963f86f302940cc78f98dbe91325ae5c7b0ffa88e423b1fe05669035ccfe`
[Observed]. The three digests the packet publishes for commit `f911a45`
reproduce exactly under `git show f911a45:<path> | sha256sum` [Observed].

All eight rows of the packet's own capture-provenance table re-hashed this
session; byte count and digest match on every row, including the lane A
tailnet capture at 1,484,487 bytes /
`e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111`
[Observed].

Invariant checks run this session in the worktree:
`python3 scripts/check_governance.py` ends **32 OK, 20 WARN, 0 FAIL (52
checks)** [Observed]. Every code span in the packet containing a `/`
resolves as a path except seven, each of which is not a path: three git
branch refs, one HTML literal, one shell command, and two more branch refs
[Observed: an existence sweep over every backticked span outside fences].
No wrapped code span: every non-fence line has an even backtick count
[Observed]. No Butlers path appears in backticks in either governed file
[Observed: a sweep for backticked spans containing `butler.toml`, `v1.md`,
`lay-and-land`, `MANIFESTO` or `components.md`; the only two hits are a
plain-prose `v1.md` and an RFC string quoted as `"(v1.md)"`, neither a
backticked path]. No manifest row and no truncated signed digest is quoted.

## Findings

### J1 — blocking — the H1 repair never reaches the acceptance contract; S1, Gate 6 item 3 and Gate 1's Success 1 still encode the two-literal population

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1106-1115` (scenario S1),
`:1375-1384` (Gate 6 item 3) and `:171-180` (Gate 1, Success 1).

**Defect.** H1 was blocking because a slice built and accepted to this
packet's published denominators would pass its sweep and leave
POC-REQ-060's falsifier standing. The repair reached eight sites — Q1
(`:91`), Gate 3's slice-5 row (`:589`), slice 1's Tests (`:698-719`), Gate 5
(`:1009-1018`), Gate 6 item 1 (`:1363-1365`), the review-3 section, the
funnel summary and the evidence record's `provenance_none_census` block. It
did not reach the three places that state what a slice-1 implementation is
*accepted against* [Observed: the literal `provenance-none` occurs at packet
lines 91, 589, 698, 701, 712, 717, 1009, 1363, 1557, 1569 and 1591 — eleven
occurrences over the whole file, and none inside `:117-185`, `:1104-1146` or
`:1375-1384`].

- **S1**, under the heading "New WHEN/THEN scenarios (for the beads'
  acceptance contract, not the spec)", reads "WHEN any of the three surfaces
  renders an Unknown **disclosure**, THEN that disclosure carries a reason
  from RFC2-24's closed twelve and either its route or the declared 'No
  route declared' copy". The `provenance-none` span is not a disclosure and
  carries no reason; the scenario cannot see it. Its parenthetical still
  gives "22, 0 and 0" as the surfaces' disclosure population.
- **Gate 6 item 3** enumerates the rule-6 mutants an implementation must
  produce: "each of slice 1's nine route rows …; a thirteenth reason value;
  slice 2's empty-array-on-Unknown prohibition; slice 3's
  band-equals-gaps invariant …; slice 4's declared-equals-rendered
  assertion; slice 5's no-prior-evaluation counterexample; slice 7's
  drafted-packet banner check". The `provenance-none` re-emit mutant that
  slice 1's Tests added at `:717-719` is absent from that list.
- **Gate 1, Success 1** is the packet's falsifiable success statement. Its
  parenthetical names only the `epistemic-unknown` family — "299 and 9
  rendered … and 0 disclosure elements, a population the original
  single-denominator sweep could not see" — the same sentence shape H1
  falsified one level up.

Review 3's H1 named `:171-180` (Success 1) and `:154-158` among the sites
carrying the figures, and the packet's own H1 disposition cell does not
claim to have repaired them; so this is not a false disposition, it is an
incomplete repair of the blocking finding at the three sites that matter
most for acceptance. The packet now carries two mutually inconsistent
statements of slice 1's acceptance condition: the four-family one at slice
1's Tests and Gate 6 item 1, and the two-family one at S1, Gate 6 item 3 and
Success 1. An implementation built and accepted against the latter pair
passes while POC-REQ-060's falsifier stands — which is H1's failure mode,
relocated rather than closed.

Re-derived independently this session, so the finding rests on measurement
and not on review 3's say-so [predicate: literal occurrences of the string
`provenance-none`; denominator: the whole served page of each of the five
retained captures the evidence record names; each occurrence then assigned
to its enclosing tag]: Polaris lane A tailnet **0**, Polaris lane A direct
**0**, Trajectory **0**, Orrery **9** (all nine `<span class="provenance-none">`,
**0** inside `<style>`), home **10** = 1 stylesheet rule + 9 spans. The nine
Orrery spans' enclosing `<tr>` ids, in document order:
`work:whatsapp-single-event-normalization`, `evidence:focused-pytest`,
`runtime:live-satisfaction`, `region:unmapped-code`,
`relationship:intent-to-work`, `relationship:work-to-code`,
`relationship:code-to-evidence`, `relationship:code-to-runtime`,
`relationship:capability-to-unmapped-region` — exactly the nine the
packet publishes, and exactly the nine rows the disclosure table at
`:290-298` marks **none**/**no** [Observed]. Source sites re-read at HEAD:
`apps/three-surface-poc/src/exact-tables.ts` line 10 emits the span on an
empty `provenance` array; `apps/three-surface-poc/src/design-tokens.ts` line
25 declares `className: 'epistemic-unknown'` and the file names
`provenance-none` nowhere; its only style rule is
`apps/three-surface-poc/src/routes.ts` line 73, inside `HOME_STYLE` declared
at line 57 and passed as `extraStyle` at line 90 only;
`apps/three-surface-poc/src/orrery.ts` imports `exactTablesSection` at line 4
and calls it at lines 125 and 151 without it [Observed; a repository-wide
`grep -rn 'provenance-none'` over `apps`, `packages` and `scripts` returns
exactly those two lines]. POC-REQ-060's falsifier, read at
`openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md`
lines 945–946: "- **Falsifier**: one surface encoding Unknown (or Observed)
differently / from the declared table, or a surface styling epistemic state
ad hoc." Both limbs hold.

**Repair.** Extend S1 to the marker the sweep is actually re-specified over
(not "an Unknown disclosure"), or add an S1b scenario naming the
`provenance-none` rendering with its own oracle; add the re-emit mutant to
Gate 6 item 3; and restate Success 1's parenthetical with the four
per-surface denominators. State in the review-4 disposition which acceptance
text now carries the fourth family and which does not.

### J2 — blocking — RFC2-26 is never reached, and the packet's thrice-repeated "lawful because nothing specifies it" inverts it for slices 4 and 5

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1091-1093` (Gate 5), `:80-82`
(the Q6 preamble repaired under review 2's G4), `:617-618` (the Gate 3
authorizing-act rows for slices 4 and 5) and Q7's recommended answer at
`:97`. The packet contains **0** occurrences of the identifier `RFC2-26`
[Observed: a literal sweep over the whole file; RFC-0002 clauses cited are
RFC2-9 ×1, RFC2-10 ×2, RFC2-13 ×1, RFC2-23 ×1, RFC2-24 ×18, RFC2-25 ×2].

**Defect.** Gate 5 concludes: "**Slices 4 and 5 have no spec delta because
no requirement reaches them — and that is itself a finding**", and draws the
consequence at `:1091-1093`: "changing the home page freely is lawful today
precisely because nothing specifies it, and the same silence means no oracle
but `routes.test.ts` protects it." The same sentence is quoted approvingly
inside the Q6 preamble at `:80-82` as the ground for calling both Q6 arms
lawful, and Gate 3's rows 4 and 5 record "Owner act needed: **No**".

RFC-0002 is an accepted design contract in force. `PROJECT-STATUS.md` line
147 records Wave A (RFC 0001–0006, 19 modules) as **ACCEPTED**, act
performed 2026-08-17, with the installed modules' current bytes bound by the
2026-09-01 thirty-module contract-amendment manifest [Observed]. Quoting the
clause at
`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md` lines
196–206, verbatim and at the defined clause (verification rule 8):

> **RFC2-26.** This contract schedules nothing: **it is not a specification
> of record from which implementation work may be scheduled**. No
> implementation work for user-observable consequences of this contract —
> evaluation and snapshot displays, claim and challenge rendering,
> Unknown-reason and rendering-tier presentation, reconciliation-chain and
> gap surfaces, API answers over epistemic state — may be scheduled solely
> from this RFC. Before implementation, every observable consequence either
> maps to an approved OpenSpec requirement and scenario in the governance
> root's `openspec/**` plane, or carries a reviewed N/A judgment proving it
> purely structural with no independently testable behavior. **The reviewed
> N/A judgment's home and gate.** A reviewed N/A judgment is a recorded
> owner judgment homed in `decisions/` (RFC3-15), and the judgment is
> honored only through an effective owner act under RFC3-16(a) … absent or
> invalid acts map nothing and leave the consequence unmapped and Unknown,
> never covered (RFC3-16(a)'s effect rule; VIS-2).

Slice 5 (`:819-850`) rewrites the home route to answer four questions:
"which evaluation is current and as of when" (an evaluation and snapshot
display); "what needs the owner (slice 3's band, same projection, third
rendering, same total)" (Unknown-reason presentation and a gap surface);
the materialize status; and "when a previous evaluation exists, what changed
since it" (a reconciliation-chain surface), whose counterexample "renders a
named Unknown with its reason and route". Slice 4 (`:803-814`) makes each
surface declare "the count and denominator it renders" and asserts it
against the rendered population. Every one of those is in RFC2-26's own
enumerated list, on a page the packet has itself established no OpenSpec
requirement reaches [Observed, re-run this session: `grep -c '^### Requirement'`
returns **24** on the POC spec and **17** on the PWB spec; a case-insensitive
whole-word `home` returns **0** and **6**; the backticked literal `surfaces`
and the string `model.surfaces` return **0** in both].

So RFC2-26 turns "no requirement reaches it" into an affirmative bar, not a
freedom: absent a mapping or a reviewed N/A judgment homed in `decisions/`
and honored through an effective owner act, the consequence is "unmapped and
Unknown, never covered." Neither alternative is available to slices 4 and 5
as designed — the N/A route requires "purely structural with no
independently testable behavior", and both slices are specified with their
own oracles and, for slice 5, a rule-6 counterexample. The packet never
names the clause, so Q7's recommended answer ("rule the audit-finding
reading acceptable for slices 4 and 5") is offered to the owner without the
one contract clause that bears directly on it, and Q6's repaired preamble
replaced one wrong lawfulness framing with a second one.

This is not a claim that slices 4 and 5 are unlawful. It is that the packet
asserts their lawfulness on a ground RFC2-26 contradicts, and never tests
the clause. Which way the clause falls is the owner's to rule; the packet
must put it to them.

**Repair.** Add an RFC2-26 subsection to Gate 5 quoting the clause at its
lines, state for each of slices 4 and 5 which limb is being relied on, and
either (a) withdraw the "lawful because nothing specifies it" sentence at
`:1091-1093` and at `:80-82` (quoted and dated in place, as this packet does
elsewhere) and widen Q7's authorization limb to name the RFC2-26 bar and the
reviewed-N/A-judgment route as an owner gate, or (b) show the mapping to an
approved requirement and scenario. Record in the register row that Q7's
slices-4-and-5 limb now carries a contract test it did not.

### J3 — non-blocking — the repaired PWB-REQ-020 blockquote introduces a second, unmarked elision at the site H4 was about

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1021-1041`.

**Defect.** The quotation is introduced "quoted verbatim from … lines
902–926, with **one** elision marked (per review 3, H4)". The blockquote
runs: requirement text → `- **Observable**` → the marked ellipsis (Oracle,
Oracle independence, Mutation proof) → `- **Falsifier**`. The **Case
(sweep)** bullet, source lines 912–914, is gone with no ellipsis and no
mention [Observed: source read this session at
`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`
lines 898–930; Case (sweep) is 912–914, Observable 915, Oracle 916–917,
Oracle independence 918–919, Mutation proof 920–923, Falsifier 924–926].
There are two elisions; one is marked. Review 3 described the pre-repair
quote as running "Case (partial) → Observable → Falsifier", so the repair
dropped the partial Case entirely rather than completing it.

The bullet is load-bearing for the argument the quotation supports. It
defines the sweep's population: "enumerate every project-shape parity marker
on Polaris and every corresponding machine-answer fact at one evaluation,
including every PWB-REQ-005 authority state and PWB-REQ-022 judgment state
and disclosure." Slice 2 adds a new disclosure marker class, and `:749-758`
argues its parity obligation from "PWB-REQ-020's enumerated population
includes 'disclosure Polaris presents'" — the very bullet the reader cannot
see. The evidence record repeats the claim: `review3.disposition_summary.H4`
says "Both elisions marked".

The rest of H4's repair holds: the POC-REQ-060 quotation at `:980-998` is
complete with one marked ellipsis, source order intact, and the range
extended to 946 ✓; PWB-REQ-004 at `:1055-1062` is verbatim against source
lines 491–498, and line 490 is blank ✓; slice 2 at `:760-771` quotes the
Mutation proof bullet verbatim against source lines 920–923 and names it as
the source of the obligation ✓ [all Observed, read at source this session].

**Repair.** Restore the Case (sweep) bullet or mark its elision, and change
"one elision marked" to the true count; correct the record's H4 field.

### J4 — non-blocking — H6's repair states a universal that is false over the population it names

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:279-283`, and the same claim in
the evidence record's `review3.disposition_summary.H6`.

**Defect.** The sentence added above the disclosure table says the two
conventions differ by "32 characters", "so the same first and last
disclosures read 378,599 and 1,462,590 here and 378,631 and 1,462,622
there [Observed: both conventions re-derived this session on the lane A
tailnet capture; **the delta is 32 at both ends, over all 22 elements**]".
The first four figures are exact. The universal is not.

Re-derived this session on
`…/scratchpad/m1/measure/after/polaris-tailnet.html` [predicate: for each of
the 22 occurrences of the literal `data-unknown-disclosure`, the distance
back to the nearest preceding `<`; denominator 22]: the delta is **30** for
the 6 elements opening `<p class="unknown-disclosure" `, **31** for the 5
opening `<li class="unknown-disclosure" `, and **32** for the 11 opening
`<div class="unknown-disclosure" `. 6 + 5 + 11 = 22, so the partition
accounts for every element [Observed]. The first and last happen to be
`<div>`s, which is why both ends read 32. All 22 offsets in the table's
Offset column match my derivation value for value [Observed].

The defect is exactly the class the packet exists to prevent: a figure
correct for two members offered as holding over a stated denominator of 22,
inside the sentence whose whole purpose is to make the two conventions
legible. Verification rules 2 and 4.

**Repair.** "…a delta of 32 at both ends; over all 22 the delta is the
opening tag's own length — 30 for the six `<p>` disclosures, 31 for the five
`<li>`, 32 for the eleven `<div>`" — or drop the universal and keep the two
endpoint figures. Correct the record's H6 field.

### J5 — non-blocking — the register states a closed count of four encodings where the packet states a floor, and no sweep has ever enumerated POC-REQ-060's own population

`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md:247` (the P-71
row): "— **four** encodings for one label [Observed, each against its own
denominator]", against the packet's Q1 recommendation at `:91`: "Across the
three surfaces there are **at least four** encodings today".

**Defect.** The packet's hedge is the honest form and it is earned: three
consecutive reviews each found the census's population wrong in a different
way — F5 found it was one surface instead of three, G3 found a stylesheet
rule and a legend item inside it, H1 found a whole family outside both
literals. Each family was discovered by someone noticing a new literal, not
by a sweep whose denominator is POC-REQ-060's own "every epistemic encoding
across the three surfaces". The register drops "at least" and attaches
`[Observed, each against its own denominator]`, which is true of each
family's count and is not a denominator for the count *of families*. A
reader of the register — the artifact the owner rules from — meets a closed
figure the packet does not assert.

For the avoidance of a false alarm: I looked for a fifth family and did not
find one that survives inspection [predicate: every `class` token on the
four retained captures matching `unknown|epistem|proven|defer|no-route|gap`,
and every rendered-text occurrence of the whole word `Unknown` outside
`<style>` and `<script>` assigned to its innermost class-bearing ancestor].
The candidates are `unknown-source-details` (11 on Polaris) and
`class-provenance` (8), both nested inside the counted disclosure wrapper at
`apps/three-surface-poc/src/polaris.ts` lines 488 and 612, so neither is a
separate encoding; the remaining Polaris hits are declared copy
(`data-copy-role`), machine-parity tuple attributes and `<pre class="verbatim">`
source quotations. So the figure four is, on this evidence, right — and it
is still a count published without the predicate that could establish it
[Inferred: the census method is literal-matching per family, which cannot
enumerate a family nobody has named].

**Repair.** Restore "at least four" in the register row, or state the
predicate under which four is exhaustive and run it. The honest version is
one sentence: four families are known, each measured against its own
denominator, and no sweep has yet enumerated the requirement's own
population — which is itself part of what Q1 asks the owner to rule.

### J6 — editorial — a superseded machine field in the evidence record carries no supersession note, while its sibling in the same block does

`docs/evidence/polaris-m4-owner-loop-funnel-2026-09-14.json`,
`review1.re_derived_before_applying.file_intersections.M4_and_M2_shared_files`.

**Defect.** That array still holds **four** file paths. Review 2's G1
established the intersection is five, and the packet, the register row and
`review2.re_derived_before_applying.G1_shared_file_intersection` all carry
five. The sibling field in the same block,
`three_surface_disclosure_counts`, carries an explicit
`note_2026_09_15` explaining that its figures are raw and superseded by G3
and pointing at the current block — so the record already knows how to mark
a historical field, and did not mark this one. A machine reader taking
`M4_and_M2_shared_files` at face value gets the superseded set.

**Repair.** Add the same style of note to `file_intersections`, naming the
fifth file and the corrected field.

### J7 — editorial — the record's G6 summary says 88–102 where the source, the packet and the register say 89–102

`docs/evidence/polaris-m4-owner-loop-funnel-2026-09-14.json`,
`review2.disposition_summary.G6`: "UNKNOWN_REASON_ROUTES is at
project-shape-model.ts 88-102". Its own sibling field
`re_derived_before_applying.G6_reason_route_table_location` says "declared at
project-shape-model.ts line 89 and closing at 102", the packet says 89–102
at `:264` and `:402`, and the register row says 89–102. At source,
`packages/three-surface-poc-core/src/project-shape-model.ts` line 88 is the
third line of the preceding comment and line 89 is
`export const UNKNOWN_REASON_ROUTES…`; the closing `};` is line 102
[Observed]. One field out of five is off by one against the other four and
against the bytes.

**Repair.** Correct the record's G6 summary to 89–102.

### J8 — editorial — the register note's count is dated a day before the note it closes

`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md:165-168`: "Now
**22** open rows below (sub-lettered rows counted) and **5** acceptance-act
rows, **27** in all [Observed — recounted **2026-09-14** by the corrected
method above]", closing a block whose preceding eight paragraphs are dated
2026-09-15 and describe review 3.

The figures themselves are right, re-derived this session by the register's
own stated method [predicate: split the file on `## ` headings, then match at
line start a table row whose first cell is `P-` followed by anything but a
cell break]: acceptance-act section **5** (P-1…P-5), reading aid **0**, open
section **22** — P-10, P-12, P-15, P-17, P-18, P-19, P-20, P-21, P-23,
P-25, **P-25(c)**, P-27, P-29, P-30, P-32, P-43, P-49, P-50, P-51, P-52,
P-53, P-71 — **27** in all, with the sub-lettered row counted as the
corrected predicate requires [Observed]. The defect is only the as-of date:
this register file was edited on 2026-09-15 and the figure is presented as
having been recounted the day before, which is the shape of the stale-count
lesson the register's own corrected-predicate paragraph records.

**Repair.** Re-derive and date the count to the session that last edited the
file, or say the population is unchanged since 2026-09-14 and why.

### J9 — editorial — two dated short-head mentions remain, and "not rewritable" overstates the constraint

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1436` and `:1504`.

The H3 repair is real: the live Collision-section mention is gone and the
sentence at `:1255-1262` now routes M3 by register row P-70 and by the two
files, naming the removal. Counted this session [predicate: literal
occurrences of the seven-character short M3 head; denominator: the whole
file]: **3** over **2** lines of the packet, both inside historical
disposition tables, and **1** in the evidence record — exactly the "3 over 2
lines" the disposition claims, and the record is down from two to one
[Observed]. The bar this pass was set is at most one dated head mention, and
there are two lines.

The disposition calls the remainders "historical record[s] of what a named
repair session read and not rewritable". That overstates: this packet is not
digest-bound and the same pass rewrote the surrounding G7 disposition prose
under H3. What is worth preserving is what each session read, not the head
literal; one of the two could route by register row while keeping the fact.

**Repair.** Keep one, route the other by row, or restate "not rewritable" as
"preserved deliberately, because it records what that session read".

## H1–H9 verification

Every load-bearing finding re-derived independently this session from source,
the five retained captures and the two spec files — not read from the
disposition table.

| # | Verdict | Evidence |
|---|---|---|
| H1 fourth Unknown encoding | **PARTIAL** | The census is right and the repair is real at eight sites: Q1 carries `provenance-none` as a fourth family with the predicate, the denominator and the Orrery-versus-home asymmetry; "every Unknown" is superseded in place at Q1 and slice 1's Tests; "at least three" became "at least four"; Q1's recommendation and slice 1's Tests require the shared marker to cover it and add the re-emit mutant; Gate 3's slice-5 row records where the encoding lives; Gate 5 and Gate 6 item 1 carry it; the record gained a `provenance_none_census` block whose five per-surface figures and nine `<tr>` ids I reproduced exactly. **But** S1, Gate 6 item 3 and Gate 1's Success 1 — the packet's own acceptance contract, mutant list and falsifiable success statement — still encode the two-literal population. See J1 |
| H2 "largest of the three" | **REPAIRED** | The ranking is quoted, dated and superseded at Q1 and in the review-2 G3 disposition row, restated as "each surface's Unknowns are encoded by a marker the other two do not share", per family and unranked; the record's `cross_surface_unknown_disclosure_populations` G3 field carries the same supersession. No cross-family ranking survives in the current bytes [Observed: a sweep for "largest" and for "orders of magnitude" finds only the quoted-and-superseded instances] |
| H3 M3 head count | **REPAIRED** | Re-counted: 3 occurrences over 2 packet lines (1436, 1504), none in the Collision section, 1 in the record. Review 2's G7 disposition is restated to the true count and names which mentions are historical; the record's G7 field carries the correction. The substance re-derived: `b34fca7` is cited only inside dated disposition prose, and Q7 and the Collision section route M3 by register row P-70 and by `apps/three-surface-poc/src/polaris-copy.ts` and `apps/three-surface-poc/src/polaris.ts`. Editorial residue at J9 |
| H4 two elided spec quotations | **PARTIAL** | POC-REQ-060 at `:980-998`: complete, one marked ellipsis naming Oracle 941–942 and Oracle independence 943–944, range extended to 946, verbatim against source ✓. PWB-REQ-004 at `:1055-1062`: verbatim against source 491–498, and line 490 is blank ✓. Slice 2 at `:760-771`: PWB-REQ-020's Mutation proof bullet quoted in full against source 920–923 and named as the source of the per-class obligation ✓. **But** the PWB-REQ-020 blockquote at `:1026-1041` now drops the Case (sweep) bullet (source 912–914) with no ellipsis, under an introduction saying "one elision marked". See J3 |
| H5 over-78-column count | **REPAIRED** | Re-derived independently [predicate: lines outside fenced blocks whose first non-space character is not a pipe, length > 78; denominator 1,657 lines]: **7** — lines 1, 10, 493, 568, 764, 975, 1023. The F21 disposition at `:1454` publishes exactly those seven line numbers with the predicate and denominator stated, and supersedes "five lines" / "the four path-span lines" in place. Six of the seven are single unbreakable path code spans; line 1 is the disclosed H1 at 126 characters |
| H6 two offset conventions | **PARTIAL** | The sentence is added above the table, names both conventions and says which is which, and its four endpoint figures reproduce exactly (attributes 378,631 / 1,462,622; enclosing tags 378,599 / 1,462,590). All 22 Offset-column values match my derivation. **But** "the delta is 32 at both ends, over all 22 elements" is false over that denominator: 30 ×6, 31 ×5, 32 ×11. See J4 |
| H7 "merge-conflict site" | **REPAIRED** | Renamed to the shared copy-oracle reconciliation site in the packet (3 occurrences), the record and the register note, with the superseded name quoted and dated at `:1233-1242`. Re-derived at source: M2 slice 1's cited region is `apps/three-surface-poc/src/polaris-copy.ts` lines 45–49; `label.deferred` is line 192 and `label.no-route` line 193; 192 − 49 = 143, matching the packet's figure; `UNREACHED_IN_FIXTURES` is declared at `apps/three-surface-poc/src/polaris-copy.test.ts` line 296, with `label.deferred` and `label.no-route` among its entries. The sequencing conclusion is unchanged |
| H8 Q6's question cell | **REPAIRED** | `:96` now opens "Both arms are lawful; deletion has a cost the move does not name, stated here so the choice is made knowing it", with "Disclosed for confirmation…" quoted, dated and superseded in the same cell |
| H9 three unlabelled claims | **REPAIRED** | `:574` (conflict check), `:594` (boundaries crossed) and `:602` (not touched by any slice) each carry `[Inferred, labelled per review 3, H9: checked … against all eight slice rows above; denominator 8]` |

## F1–F22 and G1–G11 regression spot-check

**G7, PARTIAL at review 3, is now complete.** The head is out of the
Collision section, that sentence carries its meaning without it, and the
removal is noted in place at `:1260-1262`.

No regression found in the rest. Independently re-derived this session:

- **G3 / F5.** Raw `epistemic-unknown`: Polaris tailnet **2**, Polaris
  direct **2**, Trajectory **301**, Orrery **11**, home **18**; rendered =
  raw − 2 on every page, so 0 / 299 / 9 / 16, exactly as published
  [Observed].
- **G1 / F3.** Q7 and the Collision section carry the five-file M2 set with
  both denominators (9 and 13), and `polaris-copy.ts` is no longer in the
  "M4 does not touch" list. The record's review-1 block still carries the
  superseded four — J6.
- **G6.** `UNKNOWN_REASON_ROUTES` is declared at line 89 of
  `packages/three-surface-poc-core/src/project-shape-model.ts` and closes at
  102; `routesFor` is lines 150–154 with the two-branch guard at 151.
  Neither M2 slice 5's cited 162–193 nor M4 slice 2's 115–118 / 150–154
  touches 89–102 [Observed]. Record field off by one — J7.
- **G10 / N5.** `awk` count of the literal `model.` per line of
  `apps/three-surface-poc/src/routes.ts`: 35:1, 78:1, 87:1, **89:4**, 92:2,
  127:1, 133:1, 171:1, 172:1 = **13** over nine lines; `renderPocPage` opens
  at line 77, so five lines lie outside it [Observed].
- **G8.** VIS-5 at `.syzygy/governance/doctrine/vision.md` line 141 names no
  number of adapters; the superseded "two typed, explicitly authorized
  adapters" sentence is quoted and dated at `:482-489`. The registry entry's
  five `typedAuthority` values re-read at source: `writeSurface: []`,
  `databaseAccess: []`, `networkAccess: []`, `executeObservedCode: false`,
  `workingTreeRead: false`, with top-level `status`
  `candidate-amendment-no-effect-until-owner-act` and
  `authorityType: "version-control"` — every value the packet quotes
  [Observed].
- **F2 / Q2 machine figures.** Recomputed by a recursive walk over both
  machine captures: **1,149** objects carry `resolutionRoutes`, **1,137**
  empty (all `Observed`), **12** non-empty (all `Unknown`), **1** distinct
  non-empty row (`excluded-content` → "Policy change by the owner, or accept
  the exclusion"), **9** relationships of which **5** are Unknown and **0**
  carry the field. Identical, value for value, on the pre-lane-A capture
  [Observed].
- **Gate 1 censuses.** href sweep: home 40 (36 fragments + 4 nav),
  Trajectory 304 (300 + 4), Orrery 23 (19 + 4), Polaris 1,089 (699 + 386
  `/polaris/source` + 4 nav) [Observed]. `data-claim-id="` occurs **713**
  times on the lane A tailnet capture [Observed]. `model.surfaces` declares
  Polaris 4 entities / 3 relationships, Trajectory 4 / 3, Orrery 9 / 9 — so
  Q6's "declares Polaris presents 4 entities" holds and Orrery's are the
  derived pair [Observed].
- **Disclosure table.** All 22 offsets, the 13/9 split and the nine
  neither-reason-nor-route keys reproduce exactly, and those nine keys are
  identical to the nine `provenance-none` enclosing `<tr>` ids [Observed].
- **Anchors.** Every doctrine and RFC line the packet cites resolves at the
  line given: vision.md 61–64, 82, 96, 122, 141, 234–236; RFC2-23 at line
  70, RFC2-24 at 92, RFC2-25 at 153 of `rendering-vocabularies.md`; RFC2-9
  at 187 and RFC2-10 at 209 of `snapshot-and-evaluation-core.md`. Both spec
  requirement counts hold (24 POC, 17 PWB) [Observed].
- **F19/N13** could not be checked: its source is in the observed
  repository, which this review may not read [Unknown].

## Q1–Q7

| Q | Scope truthful? | Genuine gate? | Recommendation follows? | Register matches packet? |
|---|---|---|---|---|
| Q1 | **Nearly.** The four per-surface censuses are exact and I reproduced every figure. The cell is hedged correctly ("at least four"). What is still short is the acceptance text the cell points at (J1) | Yes — a conformance ruling only the owner can make, both arms written out with the consequence of the second stated at the handoff | Yes on the arm; the arm's zero-denominator ground re-derived and holding. The remedy's *coverage* is stated at Q1 but not carried into S1 or Gate 6 item 3 | Mostly — the register hardens "at least four" into "four" (J5); otherwise clause by clause identical, including the marker-coverage caveat and the "arm unchanged" sentence |
| Q2 | Yes. Both return-`[]` branches at line 151, the third `EpistemicState` arm, the two declared copy rows at 192–193 and their `UNREACHED_IN_FIXTURES` entries, and the 0-of-1,137 / 12-of-12 split all re-derived at source and on both machine captures | Yes — a real choice, with the mint-and-retire arm named as available | Yes. The narrowing to "Unknown carrying `reasons`" follows from the deferred arm being modelled | Yes |
| Q3 | Yes. The empty write surface and the act's own prohibition are quoted accurately | Yes — three arms, (b) correctly identified as needing no act | Yes, and the handoff's "build the pure drafter anyway" is consistent with (b) | Yes |
| Q4 | Yes. One gap reason over 12 claims and the `foremost` ordering at `polaris.ts` 933–948 | Yes — both arms lawful, stated as such | Yes, with the filter arm's cost named | Yes |
| Q5 | Yes. The unconditional literals at `model.ts` 588 and 597, the conditional at 570, the seam comments and both readings' quotations verified at source | Yes — and still the packet's most honest passage: two readings quoted, the recommendation labelled `[Inferred]`, the counter-argument left standing | Yes | Yes |
| Q6 | Yes on the figures (4 declared, 415 items, 713 tuples, the five fields, the 13-over-nine-lines arithmetic) | Yes — but the preamble's ground for calling both arms lawful is the sentence RFC2-26 contradicts (J2) | Yes on the arm; deletion's cost is stated without denying deletion is available | Yes |
| Q7 | Yes on the file sets, the three-way band and the intersections | Yes — sequencing, the collision set and the slices 4–5 authorization arm each named as the owner's call | **Not fully.** The slices-4-and-5 limb recommends accepting the recorded-finding reading without testing RFC2-26, which bears directly on it (J2) | Yes, clause by clause, including the five-file correction, the three-way reconciliation, the changed-after-review-2 marker and the corrected G6 collision sentence |

**Register note counts.** 22 open / 5 acceptance / 27 in all — **correct for
this branch's copy**, counted this session by the register's own stated
method and enumerated in J8. The as-of date is a day stale (J8).

**Sibling-packet references.** All by register row and by file: M2
`syzygy-dov.2` / P-69 / PR #36 and by the shared files; M3 `syzygy-dov.3` /
P-70 and by `apps/three-surface-poc/src/polaris-copy.ts` and
`apps/three-surface-poc/src/polaris.ts`; lane B `syzygy-dov.17` / P-68 / PR
#35. Head mentions: two lines, both historical disposition prose — see J9.

**Owner trade-offs.** None found smoothed into consensus. Q5's two readings,
Q2's mint-and-retire arm, Q3's three arms, Q4's filter arm, Q6's deletion
arm and Q1's "accepted shape" arm are each written out with their
consequence, and every changed recommended answer is disclosed in the
packet, the record, the register note and the register row. **One lawful-arm
claim is unsupported rather than wrong:** Q6's preamble and Gate 5 call both
Q6 arms and slices 4–5 lawful on a ground RFC2-26 contradicts (J2) — that is
a missing test, not an arm called unlawful. No lawful arm is called unlawful
anywhere in the current bytes.

**Epistemic labelling.** Substantive claims carry `[Observed]`, `[Inferred]`
or `[Unknown]` throughout, including the three H9 sites. The one label I
would question is the register's
`[Observed, each against its own denominator]`, attached to a family count
no denominator reaches (J5).

## Counts

blocking 2, non-blocking 3, editorial 4 — nine findings, J1–J9.

Verdict: REVISE
