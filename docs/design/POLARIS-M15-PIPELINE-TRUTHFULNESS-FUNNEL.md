# Feature request M15 — Pipeline truthfulness at class granularity: a class's grammar defect that no longer wipes its healthy siblings, an added category that is flagged not invisible, and a tree fact that cannot stand alone beneath an unread root

> **Candidate — binds nothing.** Bead `syzygy-dov.15`, move M15 of the
> 2026-09-13 vision pursuit (`docs/pursuits/2026-09-13-vision-pursuit.md`,
> section "### M15"), written in the shape of
> the M14 provenance-depth funnel packet and its siblings.
> Planning only: nothing here authorizes implementation. This packet names
> lawful arms for the owner to take; it rules no slice authorized or
> unauthorized, and the owner disposes.
>
> **One fresh-context review landed 2026-09-17 — CONFIRM WITH EXCEPTIONS
> (0 blocking, 2 non-blocking, 1 editorial).** The two non-blocking and one
> editorial line-pointer repairs (F1–F3) were applied at this close-out; the
> reviewed bytes stay quoted-and-dated in place. By verification rule 10 those
> repairs are themselves uncovered until a second independent review, bound to
> the post-repair bytes, confirms them; none is queued. The retained raw is at
> `docs/reviews/R-POLARIS-M15-PIPELINE-TRUTHFULNESS-FUNNEL-1-RAW.md`. The
> load-bearing figures were reproduced this session by two independent methods
> (verification rule 2) and no repair moved any of them.
>
> **The whole move is spec-amendment-gated.** Every slice is downstream of a
> change to PWB-REQ-002's tested contract, which trips the continuation act's
> spec-amendment escalation trigger (Gate 3). So the strongest lawful arm this
> packet ever recommends is *drafting* a CC-REV-2 semantic delta and designing
> against it; nothing here may be built until the owner signs the amendment
> and authorizes implementation afresh. Drafting binds nothing (VIS-4).

Date: 2026-09-17. Author: a funnel session (Claude), for the owner.

Size: **small** (slice 3) / **medium** (slices 2 and 4) / **large** (slice 1,
the semantic delta, and only its drafting question is asked here).

Baseline: Syzygy `a9f671e` (main). The subject is the pure project-shape
extraction and manifest pipeline in `packages/three-surface-poc-core/` — the
grammar that turns a classified source body into modeled items, and the
manifest that populates the source set. No renderer change is proposed.

**Line-count convention, stated once.** A "line N" below is the one-based
index into the split-on-newline segments of the file at `a9f671e` — the
number `sed -n 'Np'` prints. A byte count is the UTF-8 length.

**Capture convention, stated once.** One machine capture is read for
magnitudes: the retained lane A "after" capture `api-poc.json` (5,520,314
bytes), the machine answer served at Syzygy `2ef68f5` against Butlers revision
`2e3bac97790b4bd8906dcac63eadb5642a0bb1ac` and recorded in
`docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`. The
defect this move addresses is structural, read at the source at `a9f671e`; the
capture supplies only how much data each defect stands to affect. Butlers'
revision matters: the AGENTS.md known-gap note records the Butlers v1 index as
whole-source Unknown at revision `13d269b`, an earlier revision than the
capture's, where its three extraction classes' facts were all discarded by one
grammar defect. On the capture's revision the same index reads cleanly. Both
states are `[Observed]` on their named revisions and neither is smoothed into
the other. No daemon was started this session and no Butlers body was read.

## The four questions for the owner

Batched, recommended answer first. Everything below is the evidence behind
them. Q1 is the packet's central question: it is the spec amendment on which
the other three slices depend, and it is the reason the move exists — a single
class's grammar defect discarding the classes that already succeeded in the
same source is a partial truth rendered as none, which VIS-2 and VIS-1 both
rank as a failure. Because the amendment trips the continuation act's
escalation trigger, every question below recommends *drafting and designing*,
never building.

| # | Question | Recommended |
|---|---|---|
| Q1 | **[S7-M1] May a CC-REV-2 semantic delta to PWB-REQ-002 be *drafted* — via the normative-change workflow — narrowing the "a source never yields a partial item set" contract from whole-source to whole-class granularity, so one class's grammar failure no longer discards the classes that already succeeded in the same source?** Measured at `a9f671e`: `extractSource` (`packages/three-surface-poc-core/src/project-shape-extraction.ts` lines 628–662) loops the source's classes and, on the first failing class, returns `{ kind: 'unknown' }` at line 646, discarding the `all` array it has already filled with the succeeded classes' items. The test at lines 779–786 [line ref corrected 2026-09-17 from 778–786; 778 is the blank line before the it( block] pins this exactly — its own name is "a failing class withholds the items of the classes that succeeded," and it asserts the whole source is `unknown` even though two of three classes "would succeed alone." The contract is not an accident: the module comment at lines 14–17 states "A source never yields a partial item set," and PWB-REQ-002's own **Falsifier** (`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`, the requirement at line 115, its Falsifier at lines 137–138) lists "a malformed source emits a partial population" as a falsifier — a partial set is currently a *bug*, not a feature. On the retained capture the two multi-class item-bearing sources are the Butlers v1 index (75 items: catalog 65, project-account 2, success-criterion 8) and the Butlers vision file (15 items: principle 7, project-account 3, success-criterion 5); under today's contract each of those bundles stands or falls whole, and at Butlers `13d269b` the v1 index's bundle fell whole on one catalog-grammar defect. | **Authorize the *drafting* only — a CC-REV-2 semantic delta binds nothing (VIS-4), and implementation waits on the signed amendment and a fresh implementation authorization.** Drafting lets the owner see the exact contract change, its blast radius and a fresh-context review before deciding anything. **This is the slice that gates the move:** the continuation act (Gate 3) stops work for "a further amendment to the signed PWB specification beyond the 2026-09-05 package," so even the recommended arm is drafting, never building. **Every lawful arm:** (a) *no change* — whole-source Unknown stands and one defect keeps wiping a source's healthy classes; (b) *the recommended arm* — draft the delta down the normative-change workflow, owner disposes; (c) *draft the full package* — the delta plus the CC-IMPACT blast-radius statement and the fresh-context review, so the owner rules on the whole amendment at once. **Counter-argument, and it is real:** class-granular Unknown makes each source's answer more truthful but also more intricate — a reader must now read a per-class state where one source-level state stood, and the coverage consumer (`project-shape-coverage.ts`) must treat a partially-extracted source's failed classes as class-scoped Unknown without letting a succeeded class mask a failed sibling. **Default if unanswered: no delta is drafted; the whole-source-Unknown contract stands and slices 2–4 stay blocked behind it.** |
| Q2 | **[S7-M1] Given a signed Q1 delta, may a `partially-extracted` `SourceExtraction` outcome be designed — carrying items and denominators for the classes that succeeded and a per-class failure record, drawn from the same failure vocabulary, for those that failed?** `extractSource` already computes each class independently before discarding (the `extractClass` call at line 645 precedes the discard at line 646), and the failure vocabulary `EXTRACTION_FAILURES` (lines 33–41, seven reasons today) is already class-scoped. The mechanism is a new result kind that retains what the loop already built instead of throwing it away. | **Endorse the direction and *design* it inside the drafted delta package — do not build it until Q1's delta is signed and implementation is authorized afresh.** A `partially-extracted` source *is* a partial item set, which the current tested contract and PWB-REQ-002's falsifier forbid, so it cannot ship ahead of the amendment. **Every lawful arm:** (a) *no partial outcome* — even after the delta, keep whole-source Unknown, which would make the amendment pointless; (b) *the recommended arm* — a per-class outcome with class-scoped failure records, the succeeded classes modeled and the failed ones Unknown-with-reason; (c) *a coarser split* — a source is either fully extracted or wholly Unknown, blessed by the delta but still discarding, strictly less truthful than (b). **Counter-argument:** (b) moves work into the coverage consumer, whose oracle (PWB-REQ-002's two-independent-extractor check) must now reconcile per class, not per source. **Default if unanswered: no `partially-extracted` outcome is designed or built; extraction stays all-or-nothing per source regardless of how Q1 falls.** |
| Q3 | **[S7-M2] May an `unenumerated-heading` failure reason be added — with a tenth-category fixture — so a level-3 catalog heading outside the closed vocabulary, or an unenumerated root-summary or precedence heading, is *flagged* rather than silently skipped?** Measured at `a9f671e`, two methods: `CATALOG_HEADINGS` (`packages/three-surface-poc-core/src/project-shape-extraction.ts` lines 56–66) is **nine** string literals, and `extractCatalogEntries` (lines 438–460) iterates only `for (const headingText of CATALOG_HEADINGS)` and never scans the document's own headings for a tenth level-3 heading. So a tenth Butlers catalog category — or any heading a project adds outside the closed nine — yields neither a count nor an Unknown: it is invisible, the one outcome VIS-2 forbids ("no evidence means Unknown" also forbids "never counted at all"). | **Design it in the same drafted delta and rule which arm.** **Every lawful arm:** (a) *fail the catalog class on an unenumerated heading* — this works under today's whole-source-Unknown semantics and is arguably already within PWB-REQ-002's intent (flagging is more truthful than silence), but it still changes a bound, tested pipeline's observable behavior, so it should ride in the drafted delta rather than ship alone; (b) *surface the extra heading as a distinct flagged declaration alongside the modeled catalog* — strictly more informative, but it depends on Q1/Q2's class-scoped mechanism to carry the flag without failing the healthy items; (c) *no change* — the tenth category stays invisible. **Counter-argument:** arm (a) turns a silent under-count into a whole-class Unknown, which for a project that legitimately extends the catalog is itself a partial truth unless paired with (b)'s surfaced flag. **Default if unanswered: no `unenumerated-heading` detection ships; a tenth category stays invisible.** |
| Q4 | **[L1-M4] May the tree-population rules declare their root-independence — each carrying an explicit `rootIndexRequired` flag and its rule provenance — so that when the root index did not read, a root-dependent rule's sources stay counted-and-Unknown rather than admitted, while a genuinely root-independent population is stamped and the page states, at the class aggregate, that it was derived without a read root index?** Measured at `a9f671e`: Rule 2 (`packages/three-surface-poc-core/src/project-shape-manifest.ts` line 419) gates every pillar on `rootIndex.state`, returning `unknown` when the root is missing or unavailable; Rules 3 and 4 (lines 491–506) loop over `input.tree` unconditionally and reference `rootIndex` **nowhere** — the `BASELINE_SPEC` and `ROSTER_BUTLER` regexes (lines 354–355) mint sources over the whole tree regardless of root state. On the retained capture Rule 3 mints 192 baseline-spec sources this way. Butlers is not exposed, because its root index reads; a second repository using OpenSpec's conventional `openspec/specs/<dir>/spec.md` layout with an unread root index would show real, modeled baseline-spec counts beneath five pillars all reporting root-index-missing — the silent-partial-truth class VIS-1 ranks worst. | **Design it and route it through the same drafted CC-REV-2 delta, because it changes admission semantics when the root is unread — a spec-bound behavior — even though the flags themselves are additive metadata.** Butlers' manifest digest must be **unchanged** by the additive flags; if the digest moves, the profile field ordering is wrong (that check is the slice's own falsifier). **Every lawful arm:** (a) *no change* — Rules 3 and 4 stay root-blind and a second project can emit modeled facts beneath a wholly-Unknown shape; (b) *the recommended arm* — declare `rootIndexRequired` per rule, keep root-dependent sources counted-and-Unknown when the root is unread, stamp the root-independent population and render the aggregate qualification; (c) *qualify only* — render the aggregate note "derived without a read root index" without changing admission, so the facts still stand alone but are labelled, half the fix. **Counter-argument:** whether Butlers' baseline specs are *genuinely* root-independent is the spec's own reader-definition question, and mis-stamping a root-dependent rule as independent would re-admit exactly the silent facts the slice exists to stop. **Default if unanswered: no change; Rules 3 and 4 stay root-blind.** |

### Decided in this packet, not put to the owner

**The move is entirely spec-amendment-gated, and the packet recommends
drafting, never building — this is stated once and governs every question.**
Unlike the M14 packet, where one of five slices tripped the escalation
trigger, here all four slices are downstream of the PWB-REQ-002 contract
change. There is no slice that may proceed under the acts in force. The
strongest lawful arm is a CC-REV-2 semantic delta the owner disposes, plus
design work bound to that unsigned delta.

**The S7-F1 defect is structural, read at the source, and its magnitude is
measured — not asserted — on a capture where the defect did not fire.** The
discard at line 646 is `[Observed]` from the code and pinned by the test at
779–786 [corrected 2026-09-17 from 778–786]. Its magnitude is `[Observed]`
on the retained capture: the two multi-class item-bearing sources carry 75
and 15 items, each bundle discarded whole if any one of its classes fails.
The *bite* — a whole bundle actually lost — is `[Observed]` at Butlers
`13d269b`, a different revision, where the v1 index was whole-source
Unknown. Naming both revisions is the honest form; collapsing them would
either overclaim the current capture or hide the live example the known-gap
note records.

**The tenth-category and second-project exposures are `[Inferred]`
counterfactuals, not present in Butlers today.** The packet does not claim the
Butlers catalog has a tenth heading, nor that any observed repository has an
unread root index minting orphan facts. What is `[Observed]` is the code path
that would make each invisible; the harm is `[Inferred]` for the project that
first hits it. VIS-2 forbids the silence regardless of whether a project has
tripped it yet.

## Gate 0 — Baseline

| Pillar | Present | Constrains this request |
|---|---|---|
| Doctrine | `.syzygy/governance/doctrine/vision.md` | VIS-2 (no-evidence → Unknown, never silence, never zero); VIS-1 (a partial truth presented without its qualification is the worst failure mode) |
| Decisions | `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` (2026-09-02), `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` (2026-09-05), `THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md` | the first two are the implementation grant and its continuation, whose spec-amendment escalation trigger every slice is tested against in Gate 3 |
| Specification | `openspec/changes/polaris-project-wide-butlers-model/…/spec.md` | PWB-REQ-002 (the coverage invariant and its "a malformed source emits a partial population" falsifier), the byte Q1 asks to amend; PWB-REQ-004 as amended (the root index and precedence grammar) |
| Amendment overlay | **None as a separate directory.** The PWB 2026-09-05 amendment was performed **in place**; PWB-REQ-002's bytes are bound, which is why Q1 asks to draft a semantic delta rather than edit them | Q1 and slices 2–4 all depend on that bound byte changing, so none may ship without the amendment |
| Contracts | RFC-0002 (RFC2-26 phase rule) | RFC2-26 run in Gate 5; each slice is scheduled from an approved OpenSpec requirement, not from RFC-0002 alone |
| Policies | `policy-candidates/` (CC-SPEC, CC-IMPACT, in force despite the directory name); the normative-change workflow at `.syzygy/governance/contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`; CC-REV-2 | CC-REV-2 is the propagate-in-the-same-change rule (a spec change syncs its dependents in one delta, never "later"); the workflow is the path Q1 asks to *draft* down |

**One bound-byte constraint this packet obeys.** PWB-REQ-002's requirement
text and its falsifier are bound by the 2026-09-05 amendment performed in
place, so **no slice edits them**; Q1 asks only to draft a CC-REV-2 delta
against that requirement, which the owner then disposes. No slice reads a
Butlers body or changes any consent or read boundary — the whole move is
pipeline-internal to a body already lawfully admitted.

## Gate 1 — Motif

The move is one sentence of doctrine made mechanical: **a fact the pipeline
holds must not vanish because a different fact next to it could not be read.**
Today three independent things are lost to one defect, in three shapes. A
class's grammar failure discards the healthy classes of the same source
(slice 1's mechanism, slice 2's outcome). A catalog category outside the
closed nine headings is neither counted nor Unknown — it is unread and
unnamed (slice 3). And a tree rule mints modeled facts even when the root
index that should frame them never read, so a second project's page can show
real counts beneath a shape that was never read (slice 4).

The motif is VIS-2 and VIS-1, not a new idea: no evidence yields Unknown,
never silence; and a partial truth shown without the qualification that makes
it true is worse than an honest gap. Each slice replaces a silence with a
named Unknown at the finest granularity the evidence supports — per class, per
heading, per rule — without ever inventing a fact it does not have.

## Measurements

Each figure names its source and its method. Method is Python `re` and a JSON
walk over the retained capture (verification rule 1); every load-bearing
figure is confirmed by a second method (verification rule 2). No "zero / all /
every" claim rests on a single sweep.

### 1. The whole-source discard, and what it stands to cost

`extractSource` returns `{ kind: 'unknown' }` at
`packages/three-surface-poc-core/src/project-shape-extraction.ts` line 646 on
the first class whose extraction fails, after the loop has already pushed the
succeeded classes' items into `all`. **Second method:** the test at lines
779–786 [corrected 2026-09-17 from 778–786] constructs a source where
"project-account-section and success-criterion would succeed alone," fails
the principle class, and asserts the whole `extractSource` result is
`unknown` — the behavior read from the code, asserted by the suite.

Magnitude, from `projectShape.items` in the retained capture (415 items
total): the only two sources that mint items in more than one class are the
Butlers v1 index — catalog-entry 65, project-account-section 2,
success-criterion 8, **75** items — and the Butlers vision file —
principle 7, project-account-section 3, success-criterion 5, **15** items.
Under the current contract each bundle is discarded whole if any one of its
classes fails. **Second method:** grouping every item by its first anchor's
path and by class yields the same two multi-class sources and the same 75 and
15, and the manifest's class assignment (`project-shape-manifest.ts` lines
248 and 250 [corrected 2026-09-17 from line 250; vision file at 248, v1
index at 250; 249 is architecture.md, single-class]) independently shows
both the v1 index and the vision file declaring exactly three extraction
classes each. At Butlers `13d269b` the v1 index's whole bundle was in fact
lost — the AGENTS.md known-gap note records it whole-source Unknown there
(its catalog grammar carried colon forms and duplicate labels outside the
signed dash grammar).

### 2. The closed catalog vocabulary and the invisible tenth

`CATALOG_HEADINGS` is **nine** literals (`project-shape-extraction.ts` lines
56–66), counted two ways this session: parsing the array body for
single-quote literals, and counting the per-line literal rows — both nine.
`extractCatalogEntries` (lines 438–460) iterates only over those nine and
performs no scan of the document's own level-3 headings, so a tenth level-3
heading is read by nothing and produces no item and no Unknown. The current
`EXTRACTION_FAILURES` vocabulary is seven reasons (lines 33–41); slice 3 adds
an eighth, `unenumerated-heading`.

### 3. Rules 3 and 4 run without the root index

Rule 2, the pillar discovery at `project-shape-manifest.ts` lines 419–420 (419
was cited alone until 2026-09-21; the branch is at 420), branches
on `rootIndex.state` and returns an `unknown` pillar when the root is missing
or unavailable. Rules 3 and 4, the tree-population block at lines 491–506,
contain no reference to `rootIndex` at all — measured this session by reading
the region between the "Rules 3 and 4" comment and the manifest body
assembly and finding zero occurrences of the token, against Rule 2's region
which contains it. The `BASELINE_SPEC` regex at line 354 therefore mints a
baseline-spec source for every matching path in the tree irrespective of root
state; on the retained capture that is 192 baseline-spec sources. Butlers is
unexposed because its root index reads; the exposure is `[Inferred]` for a
second repository whose root index does not.

## Gate 2 — Doctrine

- **VIS-2 (no-evidence → Unknown, never silence, never zero).** Every slice
  replaces a silence with a named Unknown: a failed class becomes class-scoped
  Unknown instead of erasing its siblings (1, 2); a tenth heading becomes a
  flagged Unknown instead of nothing (3); a tree fact under an unread root
  becomes counted-and-Unknown instead of silently admitted (4).
- **VIS-1 (a partial truth without its qualification is the worst failure).**
  Slice 4 is this rule almost verbatim — modeled baseline-spec counts beneath
  a shape that was never read are a partial truth shown as whole; the slice
  attaches the qualification that makes it honest.
- **Fail-closed polarity.** Each slice's default is the more-Unknown reading:
  a failed class stays Unknown, an unenumerated heading is flagged not
  guessed, a root-dependent fact under an unread root stays Unknown. No slice
  admits a fact it cannot ground.
- **No new read or egress.** The whole move is internal to a body already
  lawfully admitted; no slice reads a Butlers content class the PWB-REQ-005
  evaluation excludes, and none changes any consent boundary.

## Gate 3 — Topology and the acts

The authorizing acts are the implementation grant
(`PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`, 2026-09-02) and its continuation
(`PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`, 2026-09-05). The
continuation's own record states, as `[Observed]`, that the 2026-09-02
authorization names escalation triggers stopping implementation before, among
other things, an amendment to the signed PWB specification, and that further
spec changes route through CC-REV-2's amendment path and a new owner act. Each
slice against that sentence:

| Slice | Trigger test | Reading |
|---|---|---|
| Q1 / S7-M1 delta | amends PWB-REQ-002's tested "a source never yields a partial item set" contract and its falsifier | **trips "a further amendment to the signed PWB specification"** — Q1 authorizes drafting only, which binds nothing (VIS-4) |
| Q2 / S7-M1 outcome | builds a partial item set the current contract forbids | inherits Q1's trigger — designed here, built only after the signed delta and a fresh authorization |
| Q3 / S7-M2 | changes a bound, tested pipeline's observable behavior (a new failure reason and heading scan) | rides the drafted delta; ruled with Q1, not shipped ahead of it |
| Q4 / L1-M4 | changes admission semantics when the root is unread | rides the drafted delta; the additive flags must leave Butlers' manifest digest unchanged |

There is no PWB overlay change directory; the 2026-09-05 amendment replaced
the spec bytes in place and they are bound. That is why every slice's lawful
path is the same CC-REV-2 semantic delta the owner disposes, never an in-place
edit and never a build ahead of the signature.

## Gate 4 — Design sketch, per slice

**Slice 1 (S7-M1, the delta).** A CC-REV-2 semantic delta against PWB-REQ-002,
authored down the normative-change workflow: classify the change (a normative
narrowing of a coverage invariant), draft the delta form stating the change
class, compute the blast radius CC-IMPACT requires (the coverage consumer, the
two-extractor oracle, the fixtures), and obtain a fresh-context review. The
delta's substance: replace "a source never yields a partial item set" with a
per-class contract — each `(source, class)` pair is independently modeled,
Unknown or contradicted — and rescope the falsifier "a malformed source emits
a partial population" to "a malformed *class* emits a partial population."
Nothing is implemented on the delta; it is the object the owner disposes.

**Slice 2 (S7-M1, the outcome).** Add a `partially-extracted`
`SourceExtraction` kind carrying `items` and `denominators` for the succeeded
classes and a per-class failure list (the existing `EXTRACTION_FAILURES`
vocabulary) for the failed ones; `extractSource` retains what the loop already
built at line 645 instead of discarding it at line 646. Update the coverage
consumer to treat a partially-extracted source's succeeded classes as normal
declarations and its failed classes as class-scoped Unknown, and rewrite the
multi-class fixtures (the vision and v1 index fixtures) to assert per-class
outcomes rather than a whole-source `unknown`. Built only after the signed
delta.

**Slice 3 (S7-M2).** Add `unenumerated-heading` to `EXTRACTION_FAILURES`;
after the `CATALOG_HEADINGS` loop in `extractCatalogEntries`, collect any
level-3 heading in the catalog's section range that is not among the nine, and
either fail the class with the new reason (arm a) or, on Q1/Q2's mechanism,
surface it as a flagged extra declaration beside the modeled catalog (arm b).
A fixture with a tenth level-3 category asserts it is surfaced, not dropped.
The same treatment applies to an unenumerated root-summary or precedence
heading in the root grammar.

**Slice 4 (L1-M4).** Move Rules 3 and 4 into the loaded profile as declared
tree rules, each with a `rootIndexRequired` flag and its rule provenance. When
`rootIndex.state` is not `read` and a rule is root-dependent, its sources stay
in the population as counted-and-Unknown rather than admitted; a genuinely
root-independent rule stamps each source with its provenance and the class
aggregate states it was derived without a read root index (extend the
aggregate's existing denominator reason; do not add a banner). A
counterexample fixture — a tree with a baseline spec and no root index — must
not present an unqualified modeled baseline-spec count, and Butlers' current
manifest digest must be unchanged by the additive metadata.

## Gate 5 — Specification and the RFC2-26 test

RFC2-26 bars scheduling implementation work for user-observable consequences
**of RFC-0002** from that RFC alone. Each slice is scheduled from PWB-REQ-002,
an approved OpenSpec requirement with a scenario, not from RFC-0002:

- Slices 1 and 2 from PWB-REQ-002 directly — its coverage invariant and its
  falsifier are the subject, which is why they are an amendment and not a
  plain implementation.
- Slice 3 from PWB-REQ-002's "every declared item is accounted for" and VIS-2:
  an unenumerated heading is a declared category the invariant currently fails
  to account for.
- Slice 4 from PWB-REQ-002's "a source whose item population cannot be read
  retains its identity while its denominator renders Unknown," read together
  with PWB-REQ-004's root-index grammar — the qualification the slice renders.

Each slice's oracle is a hand-typed sweep or a fixture, not a generator that
quotes prose (the rule-1-and-8 discipline). The load-bearing one is slice 2's:
the two independent extractors of PWB-REQ-002's own oracle must now reconcile
per class, and a mutation that fails one class of a multi-class fixture must
leave that class Unknown while the siblings stay modeled — mutation-tested per
class (verification rule 6) before the slice is called green.

## Collision and sequencing

| Slice | Touches | Collides with |
|---|---|---|
| 1 S7-M1 delta | PWB-REQ-002 (drafting only) | gates 2, 3 and 4 — none may build before it |
| 2 S7-M1 outcome | `extractSource`, the coverage consumer, fixtures | 3 (same extractor), 4 (shares the outcome type) |
| 3 S7-M2 | `extractCatalogEntries`, `EXTRACTION_FAILURES`, fixtures | 2 (same extractor) |
| 4 L1-M4 | `project-shape-manifest.ts` Rules 3–4, the profile | 2 (class-scoped Unknown it reuses) |

Slice 1 is the prerequisite; nothing is scheduled until the owner signs the
delta and authorizes implementation afresh. Slices 2, 3 and 4 all consume the
same class-scoped Unknown outcome and should be designed against one delta,
not three. Slice 3 and slice 2 both change the catalog extractor and should
land together or in order (2 then 3). Slice 4 reuses slice 2's outcome type
for its counted-and-Unknown sources, so it follows 2.

## Gate 6 — Engineering bar and the review posture

- **Self-referential figures, computed at a fixed point.** This file is
  **481** lines, **454** of them outside fenced code blocks. Over the
  non-fenced prose lines whose first non-space character is not `|`, `>` or
  `#`, **0** exceed 78 columns — every code span and long identifier was
  wrapped at a space between spans, never broken across a line. The
  odd-backtick-non-fence-line count is **0** — no code span is
  broken across a line break. These numbers are the same ones the evidence
  record carries, computed against the bytes this file ends in.
- **No self-referential figure was transcribed.** Each was scripted over the
  finished bytes and iterated to convergence after the last edit
  (verification rule 3).
- **One review landed; repairs uncovered until a second.** One fresh-context
  review landed 2026-09-17 — **CONFIRM WITH EXCEPTIONS** (0 blocking, 2
  non-blocking, 1 editorial); the register row P-82 says so. The two
  non-blocking and one editorial line-pointer repairs (F1–F3) were applied
  at this close-out, and by verification rule 10 those repairs are
  themselves uncovered until a second independent review, bound to the
  post-repair bytes, confirms them; none is queued. The load-bearing
  figures — the 75 and 15 multi-class bundles, the nine-literal catalog
  vocabulary, the 192 root-blind baseline-spec sources, and the discard at
  line 646 — were reproduced this session by a second method each
  (verification rule 2) and no repair moved any of them.
- **What a review must re-derive.** The discard mechanism at line 646 and its
  pinning test at 779–786 [corrected 2026-09-17 from 778–786]; the two
  multi-class sources and their 75 / 15 bundles against `projectShape.items`;
  the nine `CATALOG_HEADINGS` literals and the absence of a document-heading
  scan; that Rule 2 branches on `rootIndex.state` while Rules 3 and 4 do
  not; and that PWB-REQ-002's falsifier is the bound byte Q1 would amend, so
  every slice is drafting-gated.

## Review 1 and repairs (2026-09-17)

An independent fresh-context review of this packet (read-only; only the
artifact, its governing references and the acceptance criteria) is retained
verbatim at
`docs/reviews/R-POLARIS-M15-PIPELINE-TRUTHFULNESS-FUNNEL-1-RAW.md`
(**12919** bytes, sha256
`f7c9171a5708f5464c51d6adb205db5191513556a8425d373a5891c8d44cbbe3`, both
computed this session with `wc -c` and `sha256sum`, never transcribed). It
reviewed commit `bdc2fda`, at which the three files it measured hashed as
follows — file-content sha256 (not truncated signed digests), recomputed this
session with `git show bdc2fda:<path>` piped to `wc -c` and `sha256sum`:

| File reviewed at `bdc2fda` | Bytes | sha256 |
|---|---:|---|
| `docs/design/POLARIS-M15-PIPELINE-TRUTHFULNESS-FUNNEL.md` | 33748 | `0733d7271a707ebaf04d969275e0c5811c7fb5f479b2017d4f6bb1b52f2e18d4` |
| `docs/evidence/polaris-m15-pipeline-truthfulness-funnel-2026-09-17.json` | 14709 | `e50cc378717b999b868ff4dc5f8e9445afc106d9e0c3d102b3f25c42eeb17e79` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 25667 | `ea6248edaa38cc652f2c02e4d97d705407da6484994d3fb0ac71c5117bc4bdad` |

Its verdict word, copied exactly: **CONFIRM WITH EXCEPTIONS**. Its counts:
**0 blocking, 2 non-blocking (F1, F2), 1 editorial (F3)** — no blocking
finding. Each exception was re-derived against the source bytes at `bdc2fda`
before being applied, and the reviewed bytes stay quoted-and-dated in place.

**F1 — non-blocking. A pinning-test line range was off by one at four sites.**
The packet cited the pinning test in
`project-shape-extraction.test.ts` — the `it(` block named "a failing class
withholds the items of the classes that succeeded" — as lines **778–786** at
four sites: the Q1 cell, the S7-F1 structural note, Measurement 1, and the
Gate 6 re-derivation list. Re-derived against `bdc2fda`: line 778 is the blank
separator before the `it(`, and line 779 is the `it(` line, so the block is
**779–786**. Repaired at all four sites, the old 778–786 kept in a dated
bracket at the first site and compactly at the repeats.

**F2 — non-blocking. A multi-class assignment citation named one of two
lines.** Measurement 1 cited `project-shape-manifest.ts` **line 250** as the
class assignment for both multi-class sources, but line 250 is only the v1
index's three-class declaration; the vision file's three-class declaration is
line **248** (line 249, between them, is `architecture.md`, a single-class
assignment). Repaired to **lines 248 and 250**, the old `line 250` kept in a
dated bracket. **This applied fix diverges from the reviewer's suggested
`249–250`:** line 249 is the single-class `architecture.md` assignment and
must not be included, so the two multi-class lines are 248 and 250, never a
249–250 range.

**F3 — editorial. PWB-REQ-002's Falsifier had no line pointer of its own.**
The Q1 cell cited the requirement at spec line 115, which is the requirement
**header**; the Falsifier bullet "a malformed source emits a partial
population" is at spec lines **137–138**. The Falsifier's own pointer was
appended (", its Falsifier at lines 137–138"); nothing was replaced, only made
precise.

**Rule 2 — the load-bearing magnitudes were re-derived and no repair moved
any.** The 415 items across 9 classes, the two multi-class sources' 75 and 15
bundles, the nine `CATALOG_HEADINGS` literals, the seven `EXTRACTION_FAILURES`
reasons, and the 192 root-blind baseline-spec sources are unchanged by F1–F3,
which corrected only line pointers, not magnitudes.

**Rule 10 — these close-out edits are themselves uncovered.** Review 1 binds
the three digests recorded above at commit `bdc2fda`, not the bytes this
close-out then wrote. The F1–F3 repairs, this section, the re-tensed posture
in the banner, Gate 6, the funnel summary and the register, and the evidence
record's `review1` block all post-date `bdc2fda`, so by verification rule 10
they are themselves uncovered until a second independent fresh-context review,
bound to the post-repair bytes, confirms them; none is queued. No
recommendation, arm or default moved.

**Figures re-derived last of all, after every edit in this pass**, over the
bytes this paragraph is part of and iterated to a fixed point. Over-width
lines under the predicate "lines outside fenced code blocks whose first
non-space character is not `|`, `>` or `#`, longer than 78 columns",
denominator every line of this file: **0**. Non-fence lines with an odd
backtick count: **0**. Total lines **481**, non-fence lines **454**. These are
the same numbers the evidence record's `packet_measured_after_review1` block
carries.

## Funnel summary

```
Move M15 — Pipeline truthfulness at class granularity   reviewed 2026-09-17
------------------------------------------------------------------------------
Motif    a fact the pipeline holds must not vanish because a neighbour could
         not be read (VIS-2, VIS-1)
Defect   one class's grammar failure discards the source's succeeded classes
Cost     the two multi-class sources carry 75 and 15 items, each bundle whole
Live     Butlers 13d269b: the v1 index's whole bundle lost to one defect
Blind    catalog vocab is 9 literals, a 10th heading is invisible; Rules 3-4
         mint 192 baseline-spec sources with no dependence on rootIndex.state

Q1 S7-M1   DRAFT a CC-REV-2 delta: whole-source -> whole-class Unknown   large
           default: no delta drafted, the whole-source contract stands
Q2 S7-M1   design a partially-extracted outcome, build after signoff     medium
           default: extraction stays all-or-nothing per source
Q3 S7-M2   an unenumerated-heading flag + a tenth-category fixture        small
           default: a tenth category stays invisible
Q4 L1-M4   root-independence per tree rule, digest unchanged             medium
           default: Rules 3-4 stay root-blind

Acts     every slice trips the continuation act's spec-amendment trigger;
         the packet recommends drafting and design only (binds nothing, VIS-4)
Review   1 landed 2026-09-17: CONFIRM WITH EXCEPTIONS (0 blk/2 non-blk/1 ed);
         F1-F3 repaired at close-out; uncovered until a 2nd review (rule 10).
Register P-82 in PENDING-OWNER-DECISIONS.md: 1 review, repairs uncovered
         until a second independent review (rule 10)
```

## Recommended handoff

1. **Commission the second fresh-context review.** One review landed
   2026-09-17 (CONFIRM WITH EXCEPTIONS, 0/2/1) and its F1–F3 repairs were
   applied at this close-out; by rule 10 those repairs are uncovered until a
   second independent review confirms them. Give the reviewer only this
   packet, its evidence record, the named source files at `a9f671e`,
   PWB-REQ-002 and its falsifier, and the acceptance criteria.
2. **Put Q1–Q4 to the owner as one batch.** Each carries a recommended answer,
   its lawful arms and a stated default of "nothing happens." Every one is
   drafting-and-design only; none may be built under the acts in force.
3. **Do not build any slice on this packet.** Q1 authorizes drafting a
   CC-REV-2 delta and nothing more; slices 2–4 wait on the owner's signature
   and a fresh implementation authorization.
4. **Keep the additive-metadata discipline on slice 4.** The
   `rootIndexRequired` flags must leave Butlers' manifest digest unchanged; a
   moved digest means the profile field ordering is wrong, and that check is
   the slice's own falsifier.
