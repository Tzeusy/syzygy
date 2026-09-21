# Review 2 (independent, fresh context) — POLARIS M5 agent-briefing funnel

Read-only review. Only the artifact, the governing references named in the
brief, and what the packet cites by path were opened. No file in any repo or
worktree was modified; no state-changing git command, no `bd` write, no
daemon, no network, no observed-repository checkout read.

## Subject and digests

Worktree `scratchpad/m5wt`, branch `agent/syzygy-dov.5`, HEAD
`bf3999d1debfdb93e4830957b7bdb2d8f25dcd24`, working tree clean
(`git status --porcelain` empty) [Observed, this session].

All sizes by `wc -c` and all digests by `sha256sum`, computed this session,
never transcribed (rule 3):

| File | Bytes | sha256 |
|---|---:|---|
| `docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md` | 90597 | `6d248dea1d428c72078622a1e369aad7f051a215dd2e3aeb4cef57e97b83ffa6` |
| `docs/evidence/polaris-m5-agent-briefing-funnel-2026-09-14.json` | 21576 | `e8503cf8ab1072c86f82405bd1aeb7e87d4be04a5aded96ecb80bc0727ef2410` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 27485 | `c4552371e4305b6d754788d1375d30ab2e09a7b5672ffe90582405afcb157619` |
| `docs/reviews/R-POLARIS-M5-AGENT-BRIEFING-FUNNEL-RAW.md` (review 1) | 34023 | `73b1596137fe2e02f5d6af781e896b33296d8871059715f582cafcb7f14b3aed` |

Review 1's digest as recomputed here matches the value the packet's
"Review 1 and repairs" section prints, so that section cites review 1's
current bytes [Observed].

The retained capture the evidence file names, re-verified before use:
`scratchpad/m1/measure/after/api-poc.json`, 5,520,314 bytes, sha256
`a89b0e059b5fdadc5f359c2bee58115cd50747399cfb00444703e0fafdfb466e` —
matching the packet's stated value exactly [Observed]. The dossier's
pre-lane-A capture was also opened (5,508,208 bytes), matching the
denominator the packet gives for it.

`python3 scripts/check_governance.py` on this worktree ends
**`32 OK, 20 WARN, 0 FAIL (52 checks)`** [Observed, run this session].

## What I re-derived, and what held

Every figure below was recomputed from the capture or from source at this
commit; nothing was accepted from the packet, the evidence file or review 1.

**Reproduced exactly.** The nineteen-row per-key byte table and both of its
control totals (sum of per-key compact sizes 5,521,648 against the whole
file's own compact serialization 5,521,960, gap 312 — which I independently
confirm is exactly the 19 key names, their quotes and colons, 18 commas and
2 braces, so the packet's explanation of the gap is right); the 14-field
orientation set at **18,710** bytes with the dossier's `scope` key spelling
and **18,719** with `identity.scope`; the classes-plus-claim set at
**148,780**; `counts.sources`/`.items`/`.facts`/`.exclusions` = 278 / 415 /
439 / 9; all three authority act identities, their state string and
`independentlyVerified: false`; `identity.scope`'s three fields;
`proposedWork.changeId`, `.specKey`, `.currentAuthority.kind`/`.key` and
`.currentAuthority.claim.claimId`; every literal-substring row of the
counts table on **both** captures; the item record at 661 bytes with its
`claim` sub-object at 504; the three chain records at 1,075 / 844 / 326
bytes with their `Observed` and `Unknown` labels; the two matching source
records at 1,627 and 1,803 bytes; the `topology-component` item at 812
bytes in state `modeled`.

Method note, verified rather than assumed: the per-key table and its two
control totals reproduce only under `json.dumps(..., separators=(',',':'))`
with `ensure_ascii` left at its default (escaping), which is the method the
evidence file states for that table; the briefing-set figures reproduce
only under `ensure_ascii=False`, which is the method the evidence file
states for *those*. Both stated methods are correct for the figures they
govern, so the artifacts are internally consistent [Observed].

**Line citations re-derived by reading the declaration and closing-brace
lines at this commit**, not by hand: `routes.ts` `ResponseLimitIdentity`
111 (a closed union of two string literals), `ResponseLimitFailure` 113–124
with `population` at 120–122, `boundedResponse` 137–142, `machineHandle`
159–162, `POLARIS_SOURCE_PATH` 221 with its tailnet variant at 222 and the
Trajectory spread at 223, the machine-credentialed block 225–238 with 239
outside the returned array; `materialization.ts`
`MATERIALIZATION_EXTERNAL_REF` 9, `MATERIALIZATION_TARGET_BEAD_PREFIX` 12,
`MaterializationGoverningIntent` 14–18 with its `requirementId` literal at
15, `MaterializationPacket` 20–30
(nine fields), `buildMaterializationPacket` 43–65, `MaterializationRecord`
67–78 with `createdAt` at 71; `materialize-action.ts`
`MATERIALIZE_HUMAN_PATH` 17, `buildTrajectoryMaterializationPacket` 31–37,
`renderMaterializePanel`
55–82 with the status line at 61–62 and the seven `<dd>` parity cells at
69–75; `model.ts` `WORKER_CHANGE_INTENT_ID` 42, `PocEpistemic` 44–46,
`PocModel` 98–155 with `proposedWork` at 140, `buildModel`'s returned
`proposedWork:` at 707 and `surfaces:` at 710; `authority-disclosure.ts`
`AuthorityDisclosure` 39–46; `body-read-authority.ts`
`BodyReadAuthorityEvaluation` 315–324 and the write-surface and
execute-observed-code guards at 677–684; `project-shape-observation.ts`
`PwbResourceLimits` 65–73 (seven fields) and `PWB_RESOURCE_LIMITS` 75–83
with the two ceilings at 81 and 82; `project-shape-model.ts`
`UNKNOWN_REASON_ROUTES` 89–102 (exactly the twelve RFC2-24 keys);
`polaris-source.ts` `SOURCE_IDENTITY_PARAM` 33 and `sourceRouteHref` 41–42;
`polaris-narrative.ts` 193–198; the observer registry entry's
`writeSurface` at 125 and `executeObservedCode` at 128. All hold. One row
does not —
see **G4**.

**Clause anchors checked against the generated register**
(`DIRECTIVE-REGISTER.md`, used only to locate, never to learn what a clause
says): VIS-1 at `vision.md`:82, VIS-4 at :122, VIS-5 at :141, SEC-1 at
`security.md`:10,
SEC-3 at :39 — every one matching the packet's cited range. RFC6-14 at
:237, RFC6-22 at :390, RFC8-21 at :79 — all matching. RFC2-24 is defined at
`rendering-vocabularies.md`:92; the packet cites :44–50 — see **G7**.
The two unnumbered `vision.md` passages the packet quotes (lines 39–41,
61–64) are verbatim, and the packet correctly says the first is not an
authority.

**Spec clauses opened and compared word by word**: PWB-REQ-005 at spec 202,
PWB-REQ-006 at 340 (with its Case, Observable, Oracle, Falsifier and the
resource-breach scenario), PWB-REQ-007 at 439 with the quoted sentences at
443–446 and 447–448, PWB-REQ-013 at 723, PWB-REQ-020 at 902 with the
SHALL, Observable and Falsifier the packet quotes. The PWB spec carries 17
`### Requirement:` headings and the POC spec 24, exactly the denominator
the packet states. The POC reader note's defining sentence is on line 26
of the file the packet now names at each cite.

**Sweeps run this session, with their denominators.** 619 tracked files
under `openspec/` and `.syzygy/` swept for the literal `api/poc/polaris`
(see **G3**); the same 619 for `api/poc/briefing`; the literal `materializ`
over both signed specs (0 and 0); all 415 `projectShape.items` claim ids
parsed for their second segment; every occurrence of `no-such-claim` in
the packet and the evidence file read in context; 1,318 non-fence lines of
the packet tested for odd backtick parity and for column width; every
path-shaped code span in the packet resolved against the worktree.

## Findings

### G1 — blocking — PWB-REQ-013 does not type the dispatch packet, and it is the stated spec warrant for shipping slice 1 with no delta

`docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md:896-899` (Gate 5),
`:629` (the authorizing-act table, slice 1), `:1193` (funnel summary).

**Defect.** Gate 5 opens the "no spec delta" argument with: "PWB-REQ-013
already types the dispatch packet's subject matter as 'described here as a
distinct machine type'". Two things are wrong with that sentence, and both
are checkable:

1. **The quoted string is not PWB-REQ-013's.** It is from the file header
   comment of `packages/three-surface-poc-core/src/proposed-work.ts`, lines
   11–12, which reads "The one OpenSpec change this POC follows is described
   here as a distinct machine type, never as a project-account statement or
   a catalog item" [Observed]. PWB-REQ-013's own clause (spec lines 723–740)
   contains no such words.
2. **PWB-REQ-013 does not reach the dispatch packet at all.** Its clause is
   a prohibition about presentation: "Polaris SHALL NOT present active or
   proposed OpenSpec changes as the current project account. Proposed work
   SHALL appear only in the affected capability's detail, with its lifecycle
   state and current authoritative requirement adjacent." Its Case,
   Observable, Oracle and Falsifier are all about current-versus-proposed
   requirement sets. The literal `materializ` occurs **0 times** in the
   digest-bound PWB specification and **0 times** in the signed POC
   specification [Observed, swept this session over both files]. No
   requirement in either signed spec names the materialization packet.

Gate 3's act table carries the same claim in compressed form — slice 1
needs no act because there is "no PWB spec amendment (PWB-REQ-013 already
types this exact artifact)" — and the funnel summary repeats it as
"slices 1-2 no delta (PWB-REQ-013/020 already reach them)".

This is the precise defect review 1's F13 identified for slice 2 and the
packet repaired there. Gate 5 now asks the right question for `mayNot` —
"may the implementation add a disclosure no requirement names?" — answers it
on PWB-REQ-005's "every human and machine rendering of the authorization
basis" ground, and labels the reading [Inferred]. For slice 1's `dispatch`
field the same question is never asked; a false attribution to a
digest-bound requirement stands in its place. Since nothing in either spec
types the artifact, slice 1 is in fact the *cleaner* instance of the
minting question, not the exempt one.

The packet also contradicts itself on this point. Gate 2's own PWB-REQ-013
paragraph (`:504-514`) is honest: it states plainly that it is citing the
file header comment, says the requirement's heading "was located by sweep",
and draws only the defensible conclusion that PWB-REQ-013's subordination
property is "undisturbed". Gate 5 and Gate 3 then convert that into a
positive warrant the clause does not supply.

**Why this is blocking rather than a citation defect.** It is the sentence
on which an owner reading Gate 5 concludes that slice 1 may be built under
the existing continuation with no specification question attached, and
AGENTS.md's rule is "before implementing, find the act" — a warrant that
names the wrong clause is not a found act. Note that the *outcome* may well
survive: if no requirement reaches the artifact, there is nothing to amend,
and the packet's other grounds (zero new observation, no registry-envelope
change, no route added, a payload field set bound by no act) are
independently stated and, as far as I checked them, sound. What does not
survive is the stated reason, and rule 8 is explicit that nearby prose is
not the clause.

**Repair.** Delete the PWB-REQ-013 attribution from Gate 5, Gate 3's slice-1
row and the summary. In its place, ask for `dispatch` the same minting
question Gate 5 already asks for `mayNot`, record the swept absence (the
literal `materializ` occurs 0 times across both signed specs, with that
denominator stated), and say on which ground the packet concludes the
implementation may add it — the "payload field set is bound by no act"
ground it already uses elsewhere — labelling that reading [Inferred].
Keep Gate 2's PWB-REQ-013 paragraph as it stands; it is correct.

### G2 — non-blocking — "7 of 9 packet fields" is the wrong denominator, and Gate 6 would encode it in a test

`:240-253` (success criterion 2), `:683-690` (slice 1's parity test),
`:979-982` (S4), `:1186` (summary), `:1296` (F6's disposition row), and the
P-72 register row at `PENDING-OWNER-DECISIONS.md:201`.

**Defect.** `MaterializationPacket` has nine top-level fields.
`renderMaterializePanel` renders seven `<dd>` cells (lines 69–75). Those
seven cells do not carry seven packet fields — they carry **eight**, because
line 74 renders `issueType` and `priority` in one cell ("Type / priority").
Enumerated against the nine [Observed, this session]:

| Packet field | Panel counterpart |
|---|---|
| `title` | line 71 |
| `description` | line 72 |
| `labels` | line 73 |
| `issueType` | line 74 |
| `priority` | line 74 |
| `externalRef` | line 75 |
| `targetRepoRoot` | line 69 |
| `governingIntent` | line 70, partially — `requirementId` and `proposalPath` only |
| `targetBeadPrefix` | **none** |

So of the nine top-level fields, eight have a panel counterpart and exactly
one does not. The packet's "7 of 9" counts *cells* on one side of the ratio
and *fields* on the other. The same sentence then names "the two packet
fields the panel never renders (`targetBeadPrefix`,
`governingIntent.designPath`)" — but `designPath` is not a top-level packet
field, it is a leaf of `governingIntent`, so that pair is only a correct
remainder under an eleven-leaf denominator (nine of eleven leaves rendered),
not under nine.

Both honest denominators are available and neither is 7 of 9: **8 of 9
top-level fields** (remainder `targetBeadPrefix`), or **9 of 11 leaves**
(remainder `targetBeadPrefix`, `governingIntent.designPath`). The
*remainder enumeration* the packet gives — `targetBeadPrefix`,
`designPath`, and the state's `at` — is correct and is the part the
PWB-REQ-020 reading depends on, which is why this is non-blocking rather
than blocking.

It is not cosmetic either. Gate 6 item 4 requires the new parity test to
report "both denominators", success criterion 2 fixes them as "7 of 9
packet fields; 1 of 2 state fields", and the P-72 row tells the owner
"seven of its nine fields rendered there". A test asserting 7 would have to
be written against a fact that is 8, and AGENTS.md's own recorded lesson is
that PWB-REQ-020 parity is checked per tuple, by id, with both id sets.

**Repair.** Pick one level and state it: "8 of the packet's 9 top-level
fields have a panel counterpart (`targetBeadPrefix` has none), and 9 of its
11 leaves (`targetBeadPrefix` and `governingIntent.designPath` have none)",
plus "1 of the state's 2 fields". Note that `issueType` and `priority`
share one cell, since the parity test must map a cell to two fields there.
Correct the same figure in S4, the summary, the F6 disposition row and the
P-72 register row.

### G3 — non-blocking — Q1's `api/poc/polaris` absence claim is falsified by the packet's own register row

`:55` (Q1), against `PENDING-OWNER-DECISIONS.md:201`.

**Defect.** Q1 states, labelled [Observed, swept this session]: "the literal
`api/poc/polaris` occurs 0 times across every tracked file under `openspec/`
and `.syzygy/`, over 17 PWB and 24 POC `### Requirement:` headings". Swept
this session over the 619 tracked files under those two trees, the literal
occurs in **1** file:
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` line 201 — the
P-72 row this same packet added on this same branch
[Observed, with denominator]. The heading counts (17 and 24) are exact.

This is AGENTS.md's recorded lesson landing again: an absence figure over a
population the current pass is still editing has to be re-derived, never
read, because the page writing the figure can become the missing citer. The
premise Q1 actually needs survives intact — no requirement heading and no
specification text names the route, which is what makes it "spec'd nowhere"
— so this is a restatement, not a change of argument.

**Repair.** Restate the population as specification text: "the literal
`api/poc/polaris` occurs 0 times in either signed specification, over 17 PWB
and 24 POC `### Requirement:` headings; its only occurrence anywhere under
`openspec/` or `.syzygy/` is this packet's own register row." Give the
sweep's denominator either way.

### G4 — non-blocking — one row of the mechanically re-derived line table is still wrong, and it is slice 2's own edit site

`:414` (the line-number table), repeated at `:1006` and `:1032`
(Collision).

**Defect.** The table's preamble says "Every row below was re-derived
mechanically after review 1 (F5) with `grep -n` over the declaration and
closing-brace lines, never by hand". The row for `polaris.ts` `authorityLine`
reads 707–713. Read at this commit: the declaration is at 707, the doc
comment runs 708–711, the body 712–715, and the function's closing brace is
**716** [Observed]. Line 713 is a `.map(` continuation, not a closing brace
— the same class of error F5 was raised to fix, in the table built to fix
it. Review 1 printed the same range, so it was carried over rather than
re-derived.

The conclusion it supports survives: 707–716 is still outside all five
`polaris.ts` regions M3's packet cites (306–307, 346–361, 506–510, 1307,
1328–1329), which I confirmed by reading those regions.

**Repair.** 707–716 in the table and at both Collision cites.

### G5 — non-blocking — the two one-claim totals are not reproducible from the field paths the packet publishes

`:336-339` (the two-denominator table), `:346-350`, `:838-840`, and
`agent_briefing_sets.one_claim_briefing_examples` in the evidence file.

**Defect.** The packet's answer to F7 is that it "publishes its own two
compositions with their field paths rather than the reviewer's number".
Every *component* those paths name reproduces to the byte: `evaluation` 595,
`projectShape.identity.scope` 109, `projectShape.authority` 1,369, the two
item records 661 and 812, the three chain records 1,075 / 844 / 326, the two
matching source records 1,627 and 1,803 — and the with-source deltas
(7,076 − 5,449 = 1,627; 5,150 − 3,347 = 1,803) are exactly those source
records, so the arithmetic is internally consistent [Observed].

The **totals** are not reachable. Composing the nine named fields under the
stated method I get 5,340 and 3,271 against the published 5,449 and 3,347 —
remainders of 439 and 462 bytes, which is 8% and 14% of the figures. Those
remainders are the object's own wrapper: the nine key names, the
not-applicable disclosure's wording, and the fields of the one
`exactSourceRoutes` entry beyond its 27-byte placeholder href. None of the
three is published, so an independent reader cannot re-derive either
number; the two runs differ by 23 bytes in a direction the subject strings
alone do not explain (the second subject is 6 characters *shorter*), which
is consistent with the not-applicable disclosure being the larger carrier.

This is non-blocking because the packet calls each figure a floor and
because the argument resting on them — 2.9x headroom under a 20,480-byte
ceiling — survives with a very wide margin at either value.

**Repair.** Publish the composed object's key names and the
not-applicable disclosure's exact text and the route entry's fields, or
state the totals as approximate and give the component table (which does
reproduce) as the re-derivable part.

### G6 — non-blocking — Q3's "the type is unchanged" contradicts Q3's own proposal, and PWB-REQ-006's "only" is never read

`:60-78` ("Decided in this packet", Q3), `:844-850` (slice 3's breach body),
against PWB-REQ-006 at spec lines 381–384.

**Defect, first half.** Q3 decides to "reuse `ResponseLimitFailure` ...
**unchanged**, and add one sentence to the body", and justifies withholding
the question from the owner partly on the ground that "both arms leave the
type unchanged, so there is no trade-off for the owner to hold". The breach
body is a `JSON.stringify` of `responseLimitFailure(...)` (`routes.ts`
line 141), a serialization of exactly that interface [Observed]. A
sentence cannot be added to the body without adding
a field to `ResponseLimitFailure` or changing its constructor. "Reuse it
unchanged" and "add one sentence to the body" cannot both hold, and the
alternative arm — minting a third `population` arm — obviously changes the
type too, so "both arms leave the type unchanged" is false under any
reading of "both arms".

**Defect, second half.** PWB-REQ-006's breach sentence reads: "A
final-output breach SHALL return **only** a bounded typed failure envelope
carrying evaluation identity, limit identity, declared value, observed
value and population counts; it SHALL NOT truncate or emit a
success-shaped model." Q3 quotes the clause for "population counts" and
says it "says nothing about their scope" — true — but never addresses
whether "only ... carrying [five items]" closes the envelope's contents
against a sixth. A reader who takes "only" as closing the field set reaches
a spec question, not an engineering decision.

**My reading, stated as mine** [Inferred]: the enumeration is a minimum,
not a closure — the clause's own contrast is with truncation and
success-shaped models, the Falsifier fires on "an oversized or truncated
success response" and not on an extra field, and neither the Observable nor
the resource-breach scenario constrains the envelope's field set. So I
agree with the packet's *outcome*: Q3 is genuinely engineering judgment and
not a hard gate in disguise. What is missing is that the packet reached
that outcome without reading the word that could have made it a gate.

**Repair.** State that the disclosure sentence is a new field on
`ResponseLimitFailure` (a widening of an implementation type bound by no
act) rather than "unchanged", drop "both arms leave the type unchanged",
and add one sentence saying why "only ... carrying" is read as a minimum
rather than a closure, labelled [Inferred].

### G7 — non-blocking — RFC2-24 is quoted from the module summary, not from the defined clause

`:810-816` (slice 3's unresolvable-selector design), `:1293` (F3's
disposition row).

**Defect.** The packet anchors its F3 repair to
`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`
lines 44–50 and quotes them accurately. Those lines are the module's
opening "Three rules carry most of the weight" summary. RFC2-24 is
*defined* at line 92 of the same file, per `DIRECTIVE-REGISTER.md`
[Observed], and the clause and its twelve-row table run 92–131. Review 1
read the clause; the packet's repair reads the summary. Rule 8 is exact on
this: anchor a contract claim to a defined clause and quote it, because
nearby prose is not the clause.

The substance is unaffected — the summary states the same rule in nearly
the same words, and the remedy sentence ("a fact of the render, never
dressed as a reason") appears in both — and the packet's own evidence file
already cites 119–131 alongside 44–50, so the author had the table. This is
an anchoring defect at the one site where the packet is discharging a
blocking vocabulary finding, which is why it is worth fixing rather than
waiving.

**Repair.** Cite lines 92–115 with the table at 119–131 and quote from
there; keep 44–50 as the summary restatement if useful.

### G8 — non-blocking — the Collision denominator undercounts M3 by two slices

`:1001-1009`.

**Defect.** The denominator sentence F15 asked for reads: "every slice row
of each sibling's own Gate 3 table was read — M2's 6 slices, M3's 4 slices
plus the five `polaris.ts` regions its packet cites ..., M4's 8 slices".
Counted this session from each sibling worktree's own Gate 3 table: M2 has
**6** slice rows, M4 has **8**, and M3 has **6**, not 4 [Observed]. The
sentence also does not date the M3 read, while the following sentence dates
only the M4 and M2 reads to 2026-09-14, so a reader cannot tell whether "4"
was ever right.

The conclusion survives: the operative population for M3 is its five cited
`polaris.ts` regions, which I read, and `authorityLine` lies outside all
five. But a stated denominator is the whole point of the repair, and this
one is wrong at these bytes (rule 9).

**Repair.** "M3's 6 slices", with the date the M3 worktree was read.

### G9 — non-blocking — "7,396 beads presumably" matches neither capture, and "presumably" is not a label

`:124-125`.

**Defect.** Gate 1's first headline measurement reads "`workItems`
(2,273,467 bytes, 7,396 beads presumably, 41.18%)", inside a sentence
labelled [Observed, computed this session]. `workItems.items` on this
capture holds **7,481** entries, 7,481 of them with distinct ids; on the
dossier's pre-lane-A capture it holds **7,456** [Observed, both counted this
session]. 7,396 is neither. The byte figure and the share in the same
parenthesis are exact, so only the count is wrong.

"presumably" is also an unlabelled hedge sitting inside an [Observed]
claim. The project's discipline has three labels and this is not one of
them; a figure the author is unsure of is [Inferred] or [Unknown], and
this one is simply countable.

**Repair.** "7,481 work items [Observed]", or drop the count — the byte
share is what the argument uses.

### G10 — editorial — `targetBeadPrefix` is not built at `materialize-action.ts` line 35

`:684-687`.

**Defect.** "(`targetBeadPrefix`, `materialization.ts` line 12, and
`governingIntent.designPath`, line 17, are built at `materialize-action.ts`
line 35 and rendered nowhere)". Line 35 is
`designPath: ARTIFACT_PATHS.design,` and carries `designPath` alone;
`targetBeadPrefix` does not occur anywhere
under `apps/three-surface-poc/src/` — it is set inside
`buildMaterializationPacket` at `materialization.ts` line 58 from the
constant at line 12 [Observed, grep over the app's source tree]. Review 1's
sentence — that a grep for both names across two app files returns one hit
— was about the pair jointly; the packet reads it as both.

**Repair.** "`designPath` is built at `materialize-action.ts` line 35;
`targetBeadPrefix` at `materialization.ts` line 58 from the constant at
line 12. Neither is rendered."

### G11 — editorial — "which only `trajectory.ts` line 187 calls" omits two call sites

`:165-167`.

**Defect.** `renderMaterializePanel` is also called at
`materialize-action.test.ts` lines 42 and 59 [Observed]. The claim is true
of production callers and the point it makes (the packet reaches only the
Trajectory page) is unaffected, but "only" with no qualifier is an
exactly-one claim over an unstated population.

**Repair.** "which only `trajectory.ts` line 187 calls outside tests".

### G12 — editorial — two small residues of the F20 and capture-path dispositions

`:1310` against `:27`; `:294` and the evidence file's `capture.path`.

**Defect.** (a) F20's disposition says "the remaining over-width lines are
single unbreakable paths or headings, as the review allows". Ten lines
exceed 78 columns outside tables and fences; nine are headings or single
unbreakable paths, but line 27 — "all under
`apps/three-surface-poc/src/polaris.ts`, `polaris-narrative.ts`, their" —
is ordinary prose at 80 columns and could
wrap after the comma [Observed, measured this session]. Off by one.
(b) The capture is cited as `scratchpad/m1/measure/after/`, which resolves
from neither the repository root nor the worktree root; it is relative to
the session scratchpad. Of the packet's path-shaped code spans this is the
only one that resolves nowhere (the others that do not resolve are globs,
branch names, or the literal under sweep).

**Repair.** (a) Wrap line 27, or say "nine of ten". (b) Say what the
capture path is relative to, once, where the capture is introduced.

## F1–F22 verification against the current bytes

Every row re-derived from the capture or from source at `bf3999d`; no
disposition was accepted as stated.

| # | Sev (rev 1) | Status | Evidence at these bytes |
|---|---|---|---|
| F1 | blocking | **REPAIRED** | `forbidden` = 3 and `prohibit` = 1 on **both** captures (`str.count` and `bytes.count` agreeing). All four hits are `title` values inside `workItems.items` at offsets 1541039, 1585658, 3312753, 1518492. `:169-184` and the table row at `:366` state 3 / 3; the "moved with the catalog" story is gone; the claim is restated as zero prohibitions *of Syzygy's own authority* |
| F2 | blocking | **REPAIRED** | Four literals at `:186-207`; `proposedWork.currentAuthority.claim.claimId` equals `claim:item:baseline-spec:switchboard-identity` exactly; the intent entity and its two relationships join it; `MaterializationGoverningIntent.requirementId` named as the fourth. `claim:item:topology-component:1:Spawner` is the not-applicable illustration and is present in the population. S6 (`:989-997`) and the RFC8-21 reading follow |
| F3 | blocking | **REPAIRED** | No `reason` slot anywhere in the unresolvable-selector design; `no-such-claim` occurs 3 times in the packet and once in the evidence file, every one a withdrawal or disposition statement, never a mint. PWB-REQ-007 spec 447–448 quoted verbatim. See **G7** on the anchor |
| F4 | blocking | **REPAIRED** | `PwbResourceLimits` 65–73 carries seven fields; `maxHumanResponseBytes` 2097152 at line 81 and `maxMachineResponseBytes` 8388608 at 82. Q2 and the table both say "seven fields, of which exactly two are response ceilings" |
| F5 | blocking | **PARTIAL** | All four named corrections verified exact: `boundedResponse` 137–142, `buildTrajectoryMaterializationPacket` 31–37, `MaterializationPacket` 20–30, `buildMaterializationPacket` 43–65. Every other row I re-derived holds — except `authorityLine` 707–713, actually 707–716 (**G4**) |
| F6 | blocking | **PARTIAL** | The *shape* is repaired: by value after unescaping, the machine-only remainder recorded explicitly, the PWB-REQ-020 non-reach reading labelled [Inferred]. The remainder enumeration (`targetBeadPrefix`, `designPath`, `at`) is correct. The denominator "7 of 9" is not (**G2**) |
| F7 | non-blk | **PARTIAL** | "Sevenfold" withdrawn; headroom restated as 20,480 / 7,076 = 2.9x; two compositions published. Every component reproduces to the byte and the with-source deltas are exact; the two totals are not reachable from the published paths (**G5**) |
| F8 | non-blk | **REPAIRED** | 18,710 (short keys), 18,719 (`identity.scope`) and 148,780 all reproduce exactly on this capture. The table compares shares only and says so at `:341-345` |
| F9 | non-blk | **REPAIRED** | 415 of 415 item claim ids have the form `claim:item:<class>:<key>`, with `item` the only second segment present; the old spelling matches 0. Both worked subjects exist in the population. The selector paragraph at `:776-781` states the form with its denominator |
| F10 | non-blk | **REPAIRED** | 661 bytes compact, `claim` sub-object 504. Withdrawn 511 kept at `:157-158` |
| F11 | non-blk | **REPAIRED** | PWB-REQ-006 quoted in relevant part at `:490-502` from spec 340–386, accurately; Q2 carries the fold-in question; Q3 cites "population counts". The clause's "only" is not read (**G6**) |
| F12 | non-blk | **REPAIRED** | Q2 states the closed-type widening plainly (`ResponseLimitIdentity` a closed two-literal union at line 111, `PwbResourceLimits` seven fields, both grow by one) and defends the asymmetry against Q3 on the owner-act ground |
| F13 | non-blk | **PARTIAL** | Repaired for slice 2: the minting question is asked, answered on PWB-REQ-005's ground, labelled [Inferred], with the recorded-finding fallback naming L5-F9; Gate 2's PWB-REQ-020 scope reading labelled [Inferred]. Not asked for slice 1, where a false PWB-REQ-013 attribution replaces it (**G1**) |
| F14 | non-blk | **REPAIRED** | Six bullets under the heading at act line 68: 70–72, 73–74, 75, 76–79, 80–81, 82–84 — verified against the act. The table is "exactly six rows" and the registration fixture asserts six |
| F15 | non-blk | **PARTIAL** | M4 slice 8 (`materialization.ts` 9–65), slice 4 (`model.ts` 710–750) and slice 5 (`routes.ts` 34–96) all confirmed against the M4 worktree's own Gate 3 table; M2's 6 slices confirmed; M3's five `polaris.ts` regions confirmed and the conclusion holds; M3's diff marked [Unknown]. "M3's 4 slices" is wrong — 6 (**G8**) |
| F16 | non-blk | **REPAIRED** (disposition) | Q3 and Q4 decided in the packet at `:58-94` with reasoning shown and numbers kept; the owner table is Q1 and Q2; AGENTS.md's serves-nothing/logs-nothing fact cited in Q3. Q3's warrant has a defect (**G6**) but its outcome is right |
| F17 | non-blk | **REPAIRED** | Arm (c) named inside Q1 with its two defects (the parity oracle's reference form; no ceiling of its own), marked not recommended and labelled [Inferred]; carried into the order (`:1105`), the handoff and the P-72 row |
| F18 | non-blk | **REPAIRED** | 19 `[Observed`, 13 `[Inferred`, 8 `[Unknown` in the packet, counted this session; the evidence file's four `not_verifiable_this_session` entries appear as four labelled Unknown bullets at `:1114-1124` |
| F19 | non-blk (editorial) | **REPAIRED** | Zero lines with an odd backtick count outside fences, over 1,318 lines tested this session |
| F20 | editorial | **PARTIAL** | Line 795 reflowed. Ten lines still exceed 78 columns; nine are headings or single unbreakable paths as the disposition claims, but line 27 is ordinary prose at 80 (**G12a**) |
| F21 | editorial | **REPAIRED** | "quoted in relevant part", naming the Case, Oracle, Oracle-independence and Mutation-proof bullets as omitted. The leading em dashes the source does not carry are still there — immaterial, recorded |
| F22 | editorial | **REPAIRED** | `ResponseLimitFailure` 113–124 with `population` 120–122 ✓; `MaterializationRecord` 67–78 with `createdAt` 71 ✓; the POC spec file named at all three line-26 cites ✓; the `browserRequestAllowed` row recorded as 26–38 with the doc comment from 24 ✓ |

Summary: 15 REPAIRED, 6 PARTIAL (F5, F6, F7, F13, F15, F20), 1 repaired as
a disposition (F16), **0 NOT REPAIRED** — 22 of 22 accounted for. Of the
six blocking findings, four are fully repaired and two are partial; the
partial residue of F13 is this review's one blocking finding.

## The questions

| # | Scope truthful? | Genuine gate / genuinely not? | Recommendation follows? | Register matches the packet? |
|---|---|---|---|---|
| Q1 — spec delta for a new machine-credentialed route | **Mostly.** The reader note at POC spec line 26 is definitional and binding, and the file is now named at every cite. The heading denominators (17 PWB, 24 POC) are exact. The `api/poc/polaris` zero is falsified by the packet's own P-72 row (**G3**), and F5's four bad citations are fixed | **Yes.** Two literal escalation triggers: "any scope beyond the signed change" (act lines 93–94) and "No edit to any act-bound artifact ... Spec changes route through CC-REV-2's amendment path and a new owner act" (act lines 76–79). Both read at the act this session | **Yes.** Three arms, each with its cost; the recommendation's own lane-B queueing penalty is surfaced against itself, and the cheapest arm is named and argued down rather than omitted. No arm is called unlawful | **Mostly.** The question, the three arms, the recommendation and the default match clause by clause, and the row correctly scopes the block to slice 3 while letting slices 1–2 proceed. **One omission:** the register row never mentions that the recommended arm must queue behind lane B (P-68), a cost the packet calls "worth the owner weighing alongside" its own recommendation. The row should carry it |
| Q2 — how the briefing's ceiling is declared | **Yes.** "seven digest-bound fields, two of them response ceilings" is exact at `project-shape-observation.ts` 65–73 and 81–82; the closed-union widening is stated plainly; PWB-REQ-006 is quoted accurately | **Yes.** "a change to the constraints or envelope the registry entry declares", act line 92, read this session | **Yes.** The direction is right and the fold-in possibility is surfaced as the owner's call, correctly labelled [Inferred]. The default arm is stated with its defect disclosed | **Yes.** Question, the seven/two figures, the widening, the act-line-92 trigger, the fold-in, the recommendation and the default all match clause by clause |
| Q3 — the breach body's `population` (decided, not asked) | **Partly.** "reuse it unchanged" contradicts "add one sentence to the body", and PWB-REQ-006's "only ... carrying [five items]" is never read (**G6**) | **Genuinely not a gate** — I agree with the outcome. `ResponseLimitFailure` is an implementation type in `apps/three-surface-poc/src/routes.ts` bound by no act; PWB-REQ-006's Falsifier fires on truncation and success-shaped responses, not on an added field; the Observable and the resource-breach scenario do not close the envelope's field set [Inferred]. But the packet reaches that outcome without reading the word that could have made it a gate | **Yes** on the merits: declining to mint a third `population` arm is the right restraint, the added sentence is lawful, and the counter-argument is stated and accepted rather than smoothed | **Yes.** "reuse `ResponseLimitFailure` unchanged, one sentence added ... decided in the packet with reasoning shown, not put to the owner" matches, and carries the same "unchanged" wording, so **G6**'s repair must reach the row too |
| Q4 — sequencing against M4 (decided, not asked) | **Yes.** M4 slice 1's routed-Unknown work and M5 slice 3's read of `PocEpistemic`/`resolutionRoutes` are correctly described, and the three additional M4 slices are now named with their ranges | **Genuinely not a gate.** An ordering preference between two of the owner's own branches, resolved as "no ordering is enforced". No act, no trigger, no artifact bound either way | **Yes.** The oracle-self-corrects argument holds — slice 3 reads the model's live shape, not a copied list — and the one cost (a pre-M4 fixture documenting free-prose reasons) is named and accepted rather than hidden | **Yes.** "no ordering enforced against M4 ... decided in the packet" matches |

**Are Q3 and Q4 hard gates in disguise?** No. Both are genuinely engineering
and planning judgment, and withdrawing them from the owner table is the
right call — it is the scarcest resource the funnel exists to protect. Q3's
*stated reasoning* needs the repair in G6; its conclusion does not.

**Is any lawful arm called unlawful?** No. Q1's three arms are all presented
as lawful, with arm (c) argued down on stated trade-offs rather than
forbidden. Q2's default arm is disclosed with its defect rather than barred.
The packet's own rule — a new route in a signed spec is a spec delta — is
consistently attributed to the packet's reading, never to an authority.

**Is any owner trade-off smoothed into consensus?** One, and it is
structural rather than rhetorical: G1. Gate 5 asks the minting question for
`mayNot` and answers it honestly, then supplies slice 1 a warrant from a
requirement that does not reach it, so the owner never sees that the
dispatch packet is governed by no requirement in either signed spec. G3's
self-falsified zero and G2's denominator are errors, not smoothing.

## Closed-vocabulary check

No `reason` value outside RFC2-24's twelve is minted anywhere in the packet,
the evidence file or the P-72 row [Observed, swept this session]. Every
`reason`-assignment pattern in all three files returns empty; the three
occurrences of `no-such-claim` in the packet and the one in the evidence file
are withdrawal or disposition statements naming the first draft's mint.
`UNKNOWN_REASON_ROUTES` (`project-shape-model.ts` 89–102) carries exactly the
twelve and nothing more, unchanged by this packet. The unresolvable-selector
design carries no `reason` slot, and success criterion 4 ("Zero new epistemic
or closed-vocabulary values") survives with one qualification the packet
itself states: Q2's `maxBriefingResponseBytes` widens `ResponseLimitIdentity`,
which is a closed type but not an RFC2-10/2-24/2-25 or PWB-REQ-004
vocabulary, so criterion 4 is not breached and the packet says so.

## Invariants on this review

No manifest row, act argument or truncated signed digest is quoted; the
implementation-authorization act is cited by path and line only. No observed
repository path appears in a code span. Every digest above is a full sha256
of an unbound working file, computed this session by `sha256sum`, never
transcribed. Every zero, all, only and exactly claim above carries its
predicate and the denominator swept this session; the sweeps are named
where they run. Every substantive claim is labelled or is a directly quoted
source, and my one contested reading (PWB-REQ-006's "only") is labelled
[Inferred] and given as mine. `python3 scripts/check_governance.py` ends
`0 FAIL` at this commit. Prose is wrapped at 78 columns with no code span
broken across a line.

By rule 10 this review binds only the bytes named at the top; any later
edit retires it.

## Severity counts

- blocking: **1** (G1)
- non-blocking: **8** (G2, G3, G4, G5, G6, G7, G8, G9)
- editorial: **3** (G10, G11, G12)
- total: **12**

The repair pass is substantially honest work. Twenty-two findings were each
re-derived rather than assumed, the withdrawn figures are kept visible beside
their corrections, one reviewer figure was declined with a stated reason
rather than absorbed, and the two questions that were not real gates were
withdrawn from the owner instead of padding the table. The measurement
table, the literal counts, the act's six bullets, the 415-id sweep, the
key-spelling pair and the collision ranges all reproduce exactly. The one
blocking finding is not a measurement error but a warrant: the packet
learned, from F13, to ask whether an implementation may mint a disclosure no
requirement names — and then exempted the other new field from that question
by attributing it to a clause that does not mention it.

Verdict: REVISE
