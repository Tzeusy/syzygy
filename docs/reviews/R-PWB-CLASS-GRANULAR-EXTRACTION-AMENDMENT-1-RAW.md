# R-PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-1 — fresh-context review of the PWB class-granular extraction amendment (M15)
Reviewed commit: 14db1a988e08b24e83bbc931eb66680d36a425f6
Manifest SHA-256: 317417646914577a73a1a0d62c2c059cd92d008351bfd4e16b0a394719b61f0b
Verdict: REVISE

Reviewer: a fresh-context agent that did not draft the package. I worked in my
own clone at the commit above, plus a second scratch clone where the five
patches were applied. I read only the brief's governing references, the
package, the two builders and the two code modules it names. I read nothing
under `docs/reviews/`, no `ROUND-*-DISPOSITIONS.md` file and no Butlers
content. The manifest digest above comes from
`git show <commit>:<manifest path> | sha256sum`.

## Checks run

All were run in my clone at `14db1a98`. I read each check's output as well as
its exit code.

| Check | Result |
|---|---|
| `build_pwb_class_granular_extraction_amendment.py --check` | exit 0; "11 proposed subjects (5 patched); 17 requirements, 54 scenarios; structure, regeneration, contract coverage and sibling classification verify" [Observed] |
| `… --selftest` | exit 0; "22 structure mutants, patch drift and an unclassified sibling all fail closed on their own predicates" [Observed]. Each mutant is matched with `finding.startswith(expected)`, so it is checked against its own predicate [Observed, read in `selftest()`]. |
| `build_pwb_release_label_amendment.py --check` | exit 0; "17 requirements, 55 scenarios … sibling classification verify" [Observed] |
| `check_governance.py` | exit 0; "31 OK, 21 WARN, 0 FAIL (52 checks)" [Observed] |
| `check_spec_reconciliation.py --check` | exit 0; "7 of 7 predicates without FAIL; PASS". R6 has two WARN rows for the stale registry and policy pins (`syzygy-jloi`), which the package discloses [Observed]. |
| Patches applied in a scratch clone (`patch -p1`) | All five apply. All 11 manifest rows equal `sha256sum` of the applied files [Observed]. |
| `build_polaris_project_wide_contract_coverage.py --check` over the applied bytes | exit 0; "matches regeneration — 324 clauses represented" [Observed] |
| `build_polaris_project_wide_spec_dependencies.py --check` over the applied bytes | "Polaris dependencies match regeneration — 17 requirement(s)". The applied file hashes to the manifest row `b14013a8…` [Observed]. |
| `check_spec_reconciliation.py --check` over the applied bytes | FAIL R2 (tree-framing successor chain) and R3 (census 51→54, PWB-REQ-002 6→9, `census.json`) [Observed]. These are exactly residual 2 of the semantic delta, which says the signing change must update them. |
| Own byte-preservation script (Python, `difflib` over requirement blocks) | The text before "Reader definitions:" is identical. The 17 requirement IDs are equal. Only PWB-REQ-002 differs. The only signed lines lost are the 5 reader-definition lines and 5 PWB-REQ-002 lines that the delta quotes as "Current" (one of them, "a known source disappears, an admitted item appears twice or", is only re-wrapped) [Observed]. |
| Census | Scenario headings are 51 before and 54 after, with 17 requirements in both [Observed]. |
| Capability totals | 34 rows: 28 `covered` and 6 `lawfully out of scope`. This matches the printed "28 covered, 6 lawfully out of scope, 0 Unknown/unresolved; 34 total" [Observed, computed]. |
| Impact-ledger sweep | I re-ran the published regex over `git ls-tree -r -z ef5d5f03`. Population 1,970 paths, 96 citing files, and the per-area split 23/22/23/5/10/4/5/3/1 is exact. The fixed-string second method gives 21 of 22 under openspec/packages/apps/scripts, and the one it misses is `apps/three-surface-poc/src/pwb-mutation-sweep-main.ts`, as the ledger says [Observed]. |
| Code claims at `ef5d5f03` | Module comment lines 14–17 match. `EXTRACTION_FAILURES` has seven reasons. `CATALOG_HEADINGS` (lines 56–66) has nine literals. `extractCatalogEntries` (from 438) loops only those nine. `extractSource` (from 628) returns `{ kind: 'unknown' }` on the first failed class and drops `all` [Observed]. |
| Sibling classification | The new builder lists `pwb-release-label-amendment` as pending. The release-label builder's one-entry change lists this package as pending [Observed]. |

## Acceptance criteria

1. **Ruling content.** Partly met. Q1 is met: the package is a delta only,
   in the workflow's form. Q2 is met: `partially-extracted` is designed in
   the reader definitions and design decision 12, and nothing is built. Q4 is
   met: root-independence is in the same delta. Q3 is met for the catalog
   only. See Finding 1: one narrowing of the ruled scope is not put to the
   owner. The other readings the drafter chose (what "counted" means, whether
   baseline specs and roster directories are root-independent, which rows can
   enclose a level, the sibling order) are put to the owner as packet
   questions 2–5 [Observed].
2. **Specification bar.** Partly met. The form stays invariant. The case
   sweep, observable, oracle, oracle independence and falsifier each gain
   limbs, and there are three new scenarios. The new SHALL sentence's scope
   does not match the defined term (Finding 2). The rule-provenance
   obligation has no oracle limb, falsifier limb or scenario (Finding 5).
3. **The container-shape packet's two questions.**
   - *Category rule:* met for class and category totals. "A class's item
     denominator across its sources, and its category's, is Unknown whenever
     the class is Unknown in any of those sources." An unenumerated heading
     makes the class Unknown in that source, so the rule reaches it. The
     falsifier covers both cases ("a class or category item denominator that
     counts a failed class or an unenumerated heading is presented as known"),
     and the falsifier limb "a failed class withholds the items of a sibling
     class" stops a class that reads from masking a failed one
     [Observed, text].
   - *Exactness reach:* the narrowed sentence still sits under "For every
     grammar, loaded or built-in". A source that failed whole before is now
     either partially extracted (its own denominator Unknown) or fails in
     every class (Unknown through the retained oracle limb "malformed/
     unreadable sources … carry an Unknown item denominator"). Breach and
     unavailable bodies still leave every class Unknown. One gap: a source
     whose only defect is an unenumerated heading has no stated source-level
     denominator rule (Finding 3).
4. **Signed bytes.** Met. My independent script and the builder agree (see
   the checks above).
5. **Honest claims.** Mostly met. The Butlers V1 index question is labelled
   [Unknown] in the delta and the packet. The package claims no adoption and
   names four residuals and three collisions. One unlabelled claim about
   Butlers is in Finding 8.
6. **Mechanics.** Met as specified: every listed check passes and the
   dependency file and totals equal regeneration. The selftest's guard
   coverage is narrower than the semantics under review (Finding 6).
7. **Plain language.** Met. The packet's "What you would be signing" can be
   restated: one bad class no longer hides its neighbours, an extra heading is
   shown and makes its count Unknown, and counts made without the root index
   say so. The delta separates what changes from what does not.

## Findings

**Finding 1 — Root-summary and precedence headings were dropped from the ruled Q3 scope without being put to the owner** (revise)

[Observed] The question the owner ruled on is funnel Q3, which asks whether
`unenumerated-heading` may be added "so a level-3 catalog heading outside the
closed vocabulary, **or an unenumerated root-summary or precedence heading**,
is *flagged*". The design sketch for slice 3 adds: "The same treatment applies
to an unenumerated root-summary or precedence heading in the root grammar."
P-82's Ruled column takes Q3 without narrowing it ("Q3 design the
`unenumerated-heading` reason as surface-flag").

[Observed] `SEMANTIC-DELTA.md` §2 sets those headings aside in one sentence:
"Out of scope: the funnel also named root-summary and precedence headings.
Those grammars belong to PWB-REQ-004, not PWB-REQ-002, so this delta leaves
them alone." `OWNER-DECISION-PACKET.md` asks five questions and none of them
is this one.

[Inferred] The drafter followed the recorder's gloss ("One CC-REV-2 semantic
delta to PWB-REQ-002") over the ruled question's scope. That may be the right
reading, but the gloss is not the owner's words, and the brief's criterion 1
requires every reading the drafter chose to be "named and put to the owner".
This one changes how much of the ruled Q3 is delivered.

*Failure scenario:* the owner signs v1.0 believing Q3 is fully designed. A
project with a tenth precedence or root-summary heading still has it skipped
silently, and no package anywhere carries that half of the ruling.

*Repair:* add a packet question with two options: (a) defer the root grammars
to a separate PWB-REQ-004 delta, or (b) widen this package to PWB-REQ-004.
Name the open half as a residual in the delta.

**Finding 2 — The new SHALL sentence obliges more than the defined term** (revise)

[Observed] The PWB-REQ-002 sentence reads: "a heading that a class's grammar
does not enumerate SHALL be surfaced, never skipped". The reader definitions
use a narrow defined term instead. An *unenumerated heading* exists only at a
level that a list or table row with two or more headings encloses, and only
within the sections one level up that hold those headings.

[Inferred] Read literally, the SHALL clause reaches every heading in every
admitted source that no class's grammar names. That includes the V1 index's
other level-2 headings, which the delta excludes on purpose ("enclosing that
level would flag every undeclared level-2 heading in that file") and which
packet question 4 recommends leaving unflagged. A normative sentence that is
broader than its reader definition makes the falsifier and the requirement
disagree. An implementation that follows the definitions would break the
literal SHALL, and one that follows the SHALL would break the owner's
question-4 answer. This is a CC-SPEC-4 scope defect, and under CC-SPEC-6 it
quietly re-opens question 4.

*Failure scenario:* a reviewer or the owner reads the SHALL clause alone and
expects every unnamed heading in v1.md and vision.md to be surfaced.
Alternatively, an implementer surfaces them all and makes the catalog-entry
count read Unknown on headings that are not catalog categories.

*Repair:* use the defined term, for example "an unenumerated heading SHALL be
surfaced, never skipped".

**Finding 3 — No rule for a source's own denominator when its only defect is an unenumerated heading** (revise)

[Observed] The reader definitions make a source's own item denominator Unknown
only when it is *partially extracted*: "A source in which some classes fail
and others read is partially extracted: its own item denominator is Unknown".
They also say "an unenumerated heading is not a failure". So a source in which
every class reads but one class carries an unenumerated heading is neither
failed nor partially extracted. Its own item denominator is not stated. The
retained oracle limb covers only "malformed/unreadable sources", and no
falsifier limb names a source-level denominator. The new limb names only "a
class or category item denominator".

[Inferred] An implementation could therefore show v1.md as a source with a
known item total while its catalog-entry count is Unknown. That known total
would be wrong, because the items under the extra heading are not read (the
delta gives this same reason for making the class Unknown). VIS-1 forbids "a
confident state in place of an Unknown one". This is the source-level form of
the brief's criterion-3 question, "is anything … now silently partial?".

*Failure scenario:* a tenth level-3 heading appears in the V1 index. The
catalog-entry and Heart and Soul counts render Unknown, but the source row
for v1.md reports its 75 items as its known within-source denominator.

*Repair:* state that a source whose classes include one with an Unknown
denominator, for any reason, has an Unknown item denominator. Add the matching
falsifier limb. Optionally say which outcome kind such a source has.

**Finding 4 — When the root index is unread, the counted-and-Unknown sentence covers no source of the two rules that need the root index** (note)

[Observed] The bullet says "a rule that needs it mints no item: each source
its tree path pattern matches stays counted in the source-path population with
an Unknown item denominator". The rules it names as needing the root index
are pillar-root and pillar-index, which the source-path population defines
by the root index and pillar indexes, not by a tree path pattern. Only a
loaded profile's tree population has a `pathPattern`.

[Inferred] For Butlers' built-in grammar, the "stays counted" half applies to
no source, and only "mints no item" has effect. The text also never says how
a loaded profile's tree population (`rootIndexRequired`) relates to the four
population "rules". The intended reading is probably "a rule-level flag, which
a profile sets per tree population". Saying that in one clause would remove
the ambiguity.

**Finding 5 — The rule-provenance obligation has no oracle limb, falsifier limb or scenario** (note)

[Observed] The reader definitions add "every source carries the name of the
rule that admitted it". No PWB-REQ-002 oracle, falsifier, observable or
scenario mentions rule provenance. The brief's criterion 2 asks that "each new
obligation has an oracle limb, a falsifier limb and a scenario". The
loaded-profile default ("a tree population that does not declare it needs the
root index") has a falsifier limb but no scenario.

[Observed] Mitigation: `ManifestSource` already carries `rule`
(`project-shape-manifest.ts` lines 79–81, set at lines 405–503 at `14db1a98`).
So the obligation probably costs nothing and does not threaten the funnel's
Butlers-manifest-digest falsifier.

**Finding 6 — The builder's structural guards do not cover several of the semantics under review** (note)

[Observed, rule 6] I applied the mutants to the proposed spec, regenerated
`GOVERNING-DEPENDENCIES.md` so that the digest check did not mask the result,
and ran `structure_findings`. Six of seven **survived**:

- "and its category's" dropped from the category rule (the criterion-3 rule);
- "a rule that does not need it still admits its sources" inverted to "mints
  no item";
- the falsifier limb "a class or category item denominator that counts a
  failed class or an unenumerated heading is presented as known" removed;
- the falsifier limb "a count derived without a read root index is shown
  without that qualification" removed;
- the three additions to the Observable removed;
- the THEN line of "A failing class keeps its siblings" weakened so it no
  longer names the category.

Only the removal of the root SHALL clause was killed by a phrase guard.

These bytes are still pinned by the manifest digest and by this review. The
predecessor container-shape package, however, pinned the whole proposed spec
byte for byte. A repair that regenerates the manifest would weaken any of
these limbs without the builder noticing.

*Suggested repair:* add these phrases to `READER_REQUIRED_ONCE` and
`REQ_REQUIRED_ONCE`, with matching selftest mutants, or pin the whole
proposed spec as the sibling package does.

**Finding 7 — The oracle checks that unenumerated headings are found, not how many; source-path totals are not qualified** (note)

[Observed] The reader definition requires "the count of such headings". The
oracle requires only that "an independent scan … finds every unenumerated
heading, and each one is surfaced", and no limb compares the count.

The root qualification applies to "every class and category item denominator
that counts one of them". The SHALL clause says "a count derived without a
read root index SHALL say so wherever it is shown". [Inferred] That covers the
source-path population total too, but the reader definitions do not say so.

**Finding 8 — Unlabelled factual claim about Butlers in the packet** (note)

[Observed] `OWNER-DECISION-PACKET.md` says, without an epistemic label or a
record path: "Butlers' root index reads, and the latest recorded run had no
grammar failure." [Unknown to this reviewer] I did not verify it, because
checking it needs an evidence record outside the brief's reference set. Label
it and cite the run record.

**Finding 9 — Hunk 8's "Current" block joins two separate replaced lines** (note)

[Observed] In `SEMANTIC-DELTA.md`, Hunk 8 quotes "loaded profile." and "the
machine answer and reachable from Polaris." as one block, and quotes the
proposed text for each straight after the other. A reader takes them as
adjacent lines, but they belong to the Case and Observable limbs. Split them
or mark the boundary. This is editorial.

**Finding 10 — Residual risks I am naming even though I would accept the rest** (note)

- [Unknown] Whether Butlers' V1 index has an extra level-3 heading in a
  section that holds the catalog. The package states this honestly. If it
  does, building this amendment turns two Butlers denominators Unknown on the
  first run.
- [Inferred] The release-label sibling (P-85) also takes design decision 12
  and capability row 34. Whichever lands second must be regenerated and
  re-reviewed. Both builders tolerate each other only through
  `PENDING_SIBLINGS`, so if either package is declined, its entry must be
  moved by hand.
- [Inferred] The packet and the delta refer to a `ROUND-1-DISPOSITIONS.md`
  that does not exist at this commit. That is expected for a forward
  reference, but until it exists the packet's "says whether this version is
  ready to offer" points at nothing.
- [Observed] Applying the patches makes `check_spec_reconciliation.py` fail on
  R2 and R3 until the signing change adds the successor link and the census.
  The delta names this as residual 2. It must not be read as "the package
  breaks the battery".
