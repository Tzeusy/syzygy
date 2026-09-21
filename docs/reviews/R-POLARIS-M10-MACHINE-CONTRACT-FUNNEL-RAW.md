# R-POLARIS-M10-MACHINE-CONTRACT-FUNNEL — review 1 (raw)

Independent fresh-context review, read-only. Review 1 of the M10 packet;
no prior review exists. This file is the raw output, retained verbatim.

## Header

- Reviewer: fresh-context session, 2026-09-15.
- Worktree: branch `agent/syzygy-dov.10`, HEAD `5c5ed0e`
  (parent `a9f671e`, the stated baseline). `npm ci` already run.
- `git status --short` in the worktree: empty at start and at finish;
  no tracked file was modified, no build artifact left outside
  `dist/`.
- The commit under review changes exactly two files (1,404 + 775
  inserted lines); the dossier and the register are untouched.

Reviewed bytes, computed this session (`wc -c`, `sha256sum`):

| File | Bytes | sha256 |
|---|---:|---|
| docs/design/POLARIS-M10-MACHINE-CONTRACT-FUNNEL.md | 106926 | f4c7f164e7089c38c78f42b7d918a460fca135cfea98aa992acaf70adf663b2f |
| docs/evidence/polaris-m10-machine-contract-funnel-2026-09-15.json | 33551 | 1b1a2a470d8346ce511adf13d609eda9d9ce2e02ceac9034dfa2935a0738fdf5 |

The evidence record's own `packet_bytes` (106926) and `packet_sha256`
match the committed packet exactly [Observed, recomputed].

Sibling heads read read-only this session, all in their own worktrees:
lane B `4090f98`, M2 `f2f37dd`, M3 `6574600`, M4 `63b8e33`,
M5 `ba9ca61`, M6 `83c9f60`, M7 `f97baf4`, M8 `bce9039`,
M9 `65de02b`. Every one matches the head the packet records.

Run in the worktree: the four cited test files (65 tests, all pass)
and `python3 scripts/check_governance.py`, whose last line reads
`32 OK, 20 WARN, 0 FAIL (52 checks)` — read as the tail line, not
counted with grep. No daemon was started, no provider called, no
observed repository read.

## Summary

The packet is unusually well measured. Of roughly sixty substantive
figures, every load-bearing one re-derives exactly from source or from
the named retained capture: 1,436 / 25 paths / 6 of 19 top-level keys;
914 of 916 anchors `evidence` on both captures; 0 caching or
negotiation headers over 104 files with 1 `.writeHead(`; 769 / 241 /
57 / 48 / 273; 5 of 19 and 0 of 7 documented fields; the gzip pair
851,986 and 105,850; the per-key byte table; all nine sibling heads
and all eighteen collision intersections. The contract quotations are
exact at the cited clauses, the two specifications' counts are right,
and no act-bound byte is proposed for edit.

One defect is blocking, and it is not a measurement: the packet rules
slice 3's new machine route as needing no specification delta while a
sibling packet already on the register puts exactly that question to
the owner over the same seam, citing a binding reader note the M10
evidence record itself anchors and the M10 prose never mentions.

## Findings

### F1 — blocking — slice 3's new machine route is ruled "no delta"
while P-72 (M5's Q1) has that question open, and the packet's own
evidence record anchors the clause the prose omits

`docs/design/POLARIS-M10-MACHINE-CONTRACT-FUNNEL.md:1009`
("**Slice 3 — no delta**"), `:1051` (the Gate 5 row), `:854` (Gate 3's
"one new route"), `:1229-1236` (collision 1, "No duplication").

Defect. The three-surface specification carries, under the heading
"Reader notes, binding on how this file is read", the sentence at
lines 25-26: "the \"machine answer\" is the authenticated `GET
/api/poc` response" — singular, definite article [Observed, read at
source this session]. M5's packet (PR #39, P-72, head `ba9ca61`) puts
its Q1 on exactly that sentence: "Does `GET /api/poc/briefing`, a new
machine-credentialed route, need a spec delta before it may be built,
and if so to which spec?", and it names the existing
`/api/poc/polaris` route as an unspec'd precedent. M10's slice 3 adds
a third machine route, and Q3's recommended answer serves it
`machine-credentialed` — the same class M5's Q1 governs.

The packet's evidence record carries the anchor
`"machine answer definition": "spec lines 25-26"` in
`measurements.M11_spec_sweeps.anchors_used`, so the clause was
located and then not carried into the prose. The literal phrase
"machine answer" occurs once in the whole packet, inside the
POC-REQ-020 quotation [Observed, 1 hit].

The consequence is not hypothetical. M10's collision section resolves
M5 as "complementary and the ordering is free… **No duplication.**",
and the recommended handoff tells the owner to "Budget it as
authoring". An owner reading M10 alone would see slice 3's only gate
as its credential class, answer Q3, and authorize a route whose right
to exist is the open subject of a sibling register row.

Repair. (a) Quote spec lines 25-26 in Gate 5's slice-3 paragraph and
say plainly that whether a third machine-credentialed route is inside
that definition is not settled here. (b) Replace collision 1's "the
ordering is free" with the real coupling: P-72's Q1 governs slice 3's
route, and slice 3 holds behind it as well as behind Q3. (c) Either
add the question as a seventh, or state in Q3 that its default —
slice 3 does not ship — also covers the unruled route question, and
name P-72 there.

### F2 — non-blocking — the `inputsDigest` preimage is five keys, not six

Packet `:35` (Q1, "its preimage is six named keys") and `:414`
("Its preimage is therefore exactly five named keys plus one derived
digest"). Source: `packages/three-surface-poc-core/src/model.ts`
lines 381-389.

Defect. The hashed object literal has exactly five keys: `repoRoot`,
`repositoryRevision`, `observerRevision`, `artifacts` and
`mappingDigest` [Observed, quoted whole at source]. Q1's "six named
keys" overstates by one; the measurements sentence reads as 5 + 1 = 6
and overstates by one on the same arithmetic. The accurate form is
four named inputs plus one derived digest, five keys in all. Nothing
in Q1's argument turns on it — the point is that `projectShape` is
absent — but it is a count in the packet's central question.

Repair. "four named inputs plus one derived digest (five keys)" in
both places.

### F3 — non-blocking — every governance-corpus figure is one short at
the commit the packet is published at

Packet `:110-112` (605), `:133` (640), `:148-152` (22 of 624), Gate 6
item 8 (22), and the per-file counts in the Gate 0 table
(`routes.ts` 4, `model.ts` 4, `polaris.ts` 19,
`polaris-narrative.ts` 3, `server.ts` 1).

Defect. Re-derived at `5c5ed0e` with the packet's own predicates:

- `.md`/`.txt`/`.json`/`.yaml` under `decisions/`, `contracts/` and
  `docs/evidence/`: **606**, not 605.
- all tracked under `docs/evidence/` and `.syzygy/governance/`:
  **641**, not 640.
- the four-extension corpus over those two trees: **625**, not 624.
- files naming at least one of the five implementation paths:
  **23**, not 22; per file **5, 5, 20, 4, 2**, not 4, 4, 19, 3, 1.

Every figure is short by exactly one, and the cause is the same in
each: the packet's own evidence record joined the population between
measurement and commit, and it names all five paths. This is the
lesson AGENTS.md records in terms — an absence figure over a
population the current pass is still editing has to be re-derived,
never read. The digest-citer result is unaffected: 0 citers for the
current sha256 of all nine candidate files [Observed, recomputed by
hashlib over 641 tracked files this session], and the packet's
handling of that zero — the records name paths, not bytes, so what
they oblige is a re-run — is correct.

Repair. Re-derive the five figures over the committed tree and state
the denominator's commit, or state the denominator as "the corpus as
it stood before this packet's own record landed" and give both.

### F4 — non-blocking — the POC-REQ-053 remainder is enumerated under a
predicate that returns nothing

Packet `:1002-1006`; evidence record
`measurements.M11_spec_sweeps.three_surface.literal_sweeps`, the entry
`"self-link|sibling route|endpoint list|endpoint map": 2`.

Defect. That alternation, run case-insensitively over the whole
1,008-line three-surface specification with Python `re`, returns
**0** lines, not 2 [Observed, denominator: every line of the file].
Neither cited line carries any of the four literals: line 904 reads
"dangling links over the exhausted population decides." and line 913
is the POC-REQ-053 scenario's THEN. The figure 2 is reproducible
under a different predicate — the literal `links`, whose only two
hits in the file are lines 904 and 913 — and a `route` predicate
gives lines 905 and 913, not 904. So the cited span is also off by
one under the nearest predicate that yields 2.

The conclusion is unharmed and in fact strengthened (0 ≤ 2), but the
sentence that carries it says "the remainder is enumerated rather
than waved at, per verification rule 9", and the enumerated remainder
belongs to another sweep.

Repair. State the predicate that was run (`links`), give its two
lines, and report the four-literal alternation separately as 0.

### F5 — non-blocking — "No file in this pursuit is uncontended" is a
zero/all claim with no predicate or denominator, and is false

Packet `:1216` and the funnel summary `:1344`.

Defect. Under predicate B, recomputed this session over all nine
sibling Gate 3 sections (every row and every named file re-derives
exactly, including 6 of 9 for `routes.ts`), two of M10's own nine
candidate files are named by **no** sibling packet:
`apps/three-surface-poc/src/polaris-narrative.ts` and
`packages/cap1-daemon/src/server.ts` — 0 sibling claims each.
`polaris-parity-sweep.test.ts` is claimed by one sibling (M4) and
`main.ts` by two (M2, M8). The sentence as written quantifies over
"this pursuit" and carries neither predicate nor denominator, which
is the discipline every other figure in the packet observes.

Repair. "Of M10's nine candidate files, seven are named by at least
one sibling Gate 3; `polaris-narrative.ts` and `server.ts` are named
by none" — with the denominator stated.

### F6 — non-blocking — slice 1's topology omits the consequence of
adding a top-level field to a body that is the model verbatim

Packet `:726-732` ("`/api/poc` gains one top-level object") against
Gate 3's slice-1 row `:852`, which names only
`apps/three-surface-poc/src/routes.ts` and a new sibling test.

Defect. `machineHandle` serves `JSON.stringify(model)`
(`routes.ts` lines 159-162, quoted correctly in the packet), so a new
top-level key in that body has exactly two implementations, and the
packet names neither consequence:

1. the field lands on `PocModel`
   (`packages/three-surface-poc-core/src/model.ts` lines 98-155), in
   which case Gate 3's slice-1 row should name `model.ts` as slice
   2's row conditionally does, and the change is a POC shared-model
   change — which the improvement-cycles direction puts at
   work-in-progress one (that direction, line 50, "WIP one for POC
   shared-model changes"); or
2. `machineHandle` serializes a wrapper, in which case `/api/poc` is
   no longer `JSON.stringify(model)` verbatim — the property the
   packet itself re-verifies at
   `apps/three-surface-poc/src/polaris-parity-sweep.test.ts` lines
   5-7 and that the sweep's oracle is built on.

The literal "WIP" does not occur in the packet [Observed, 0 hits],
and neither does any statement of which implementation is intended.
M8's Q7 puts the same shared-model ceremony question to the owner for
its own slice 7.

Repair. Say which of the two slice 1 takes; if (1), add `model.ts` to
Gate 3's slice-1 row and name the WIP-one constraint; if (2), say
that the parity sweep's production comment becomes false and owes an
edit in the same bead.

### F7 — non-blocking — Q5 understates the M9 coupling: M9's own
rule-6 mutant is designed to fail a path-derived key

Packet `:39` (Q5) and `:1239-1249` (collision 3). M9's packet, read
read-only at `65de02b`, slice 6(b) lines 920-925 and its rule-6
mutants at lines 927-931.

Defect. The packet's "not the same change" reading holds and is
labeled [Inferred] correctly: M9's key is cross-surface at one
evaluation and embeds the revision; M10's is cross-revision. But M9's
mutant (c) reads "Mint a join key from a path rather than the
artifact identity; the oracle … fails" — M9's design already carries
a guard aimed at exactly the derivation Q5's first arm proposes
(the dossier's "hash of source path + normalized statement"). Q5's
third arm — derive from the object id the source route already
carries — is M9's own answer, and the packet does not say so.

Repair. Name M9's mutant (c) in Q5, so the owner sees that arm three
is the arm M9 has already built a failing test for, and arm one would
require M9 to relax that mutant.

### F8 — editorial — two Q4 citations name one line of a two-line
quotation, against the packet's own stated convention

Packet `:38`. The direction's cycle definition, "a review/audit of
the runnable POC in fresh context producing evidence-cited findings",
spans lines 34-35 of
`.syzygy/governance/decisions/THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md`;
"the agent reports each completed cycle to the owner before starting
the next" spans lines 41-42. The packet cites 34 and 41. The quoted
words are exact; only the spans are short. The packet's own
line-count convention at `:20-24` says a quotation spanning two
source lines names both, "because a wrapped citation that names one
line of a two-line sentence is the error class this corpus records".
The third citation, line 36, is correct.

### F9 — editorial — PWB-REQ-020 is quoted through "in the machine
answer" while citing lines 906-910

Packet `:40` (Q6). The requirement sentence continues
", preserving multiplicity and exact provenance state." and ends on
line 910. Quoting to line 909 under a 906-910 citation is an unmarked
truncation. Nothing in Q6's argument turns on it — and the packet
does invoke the multiplicity discipline from AGENTS.md in the same
cell — but the elision should be marked.

### F10 — editorial — "eleven words" for a ten-word quotation

Packet `:36`, `:498`, `:544`. `"the final encoded HTTP body for each
Polaris HTML response"` is ten words. The machine twin at registry
line 280 is twelve.

### F11 — editorial — "two orders of magnitude inside the ceiling"
overstates by an order of magnitude

Packet `:539-541`. At the packet's own measured 7.2% ratio the
2,132,656-byte breach compresses to about 153,600 bytes against a
2,097,152 ceiling — roughly 13.7 times inside it, which is the same
factor of 14 Q2 states for the human page two hundred lines later.

### F12 — editorial — lane B's "changes only files under …"
enumeration is incomplete

Packet `:1209-1213`. Lane B's 22-file diff against `a9f671e` also
carries `PROJECT-STATUS.md` and
`.syzygy/governance/contracts/candidates/ACCEPTANCE-PHRASE-REGISTRY.yaml`
[Observed, the full diff read this session]. The claim that every
sibling branch is planning-only is true; the enumeration is not
exhaustive.

### F13 — editorial — the corrected dossier figures live in the
dossier's machine records, and the packet gives no path

Packet `:56-61` ("The dossier's \"18 top-level keys\" is 19") and
`:81-91` (the TSDoc premise). Neither "18 top-level keys" nor the
slice-plan sentence "Enumerate PocModel and PolarisPresentationEnvelope
field docs from existing TSDoc comments" occurs in
`docs/pursuits/2026-09-13-vision-pursuit.md`; both live in
`docs/pursuits/2026-09-13-vision-pursuit-data.json` and its harvest
twin [Observed, located this session]. The corrections are right and
the dossier is not edited; only the locator is missing, and a reader
checking the correction against the `.md` alone would find nothing.

### F14 — editorial — the non-fence line count is 1,327

Packet `:1298-1300`. Splitting the file and dropping the trailing
empty element gives 1,327 non-fence lines; 1,328 counts the trailing
boundary. Every other convention figure re-derives exactly: 0
odd-backtick lines, 2 lines over 78 columns (524 and 1033, each a
single unbreakable code-span path, as stated), 273 distinct code
spans, 57 slash-bearing, 13 non-resolving, and the enumerated
thirteen match the packet's list item for item.

## The six questions

| # | Scope truthful? | Genuine human gate? | Recommendation follows from the evidence? | Every lawful arm named? |
|---|---|---|---|---|
| Q1 equality key | Yes. Both candidate keys are shown false at source, in opposite directions, and the scope residue (POC-REQ-004 quantifies over code-structure facts, 27.05% of the body) is stated against the packet's own recommendation | Yes. Whether a code-structure determinism requirement warrants a whole-payload identity is a scope reading, and the continuation act's "any scope beyond the signed change" trigger is named | Yes, and the counter-argument is given more weight than the recommendation. Labeled [Inferred] where it is a reading | Three arms, and the third (scope the digest to the code-structure region) is the honest narrow one. None called unlawful. Default stated and lawful: slice 1 lands, 2/3/4a hold |
| Q2 compression | Yes. The quotation is exact at registry lines 279-280 and both readings are set out with the same words | Yes — the continuation act's registry-envelope trigger is quoted whole at lines 150-156 | Yes. The VIS-2 polarity argument is doctrine-anchored and the cheaper arm is named as cheaper and as leaving a false sentence standing | Two arms plus the do-nothing default. Neither called unlawful. Default lawful: 4b does not ship, 4a unaffected |
| Q3 schema credential class | Partly. The SEC-1 reading is truthful, but the route's *existence* question (F1) is not disclosed alongside it | Yes for the credential class — SEC-1's violation list names this exact case | Yes on the class. The dossier's own arm is stated fairly as "real" | Both arms named for the class; the arm that is missing is not a credential arm but the unruled prior question of F1. Default lawful: slice 3 does not ship |
| Q4 tracing | Yes. The direction is quoted at its own clause and the 24/24 and 17/31 sweeps re-derive | Borderline-but-fair: the second limb's reading is genuinely contestable, and the third arm (a one-sentence direction) is honestly labeled the cheapest affirmative one | Yes, and the counter-argument concedes that "slice 3 adds a document that has never existed" | Three arms. None called unlawful. Default lawful: filed, not landed |
| Q5 join key | Yes, with F7's omission | Yes. RFC1-9 reserves minting authority and PWB-REQ-014's sentence is quoted exactly | Yes, though arm three is M9's existing answer and is not identified as such | Three arms. None called unlawful. Default lawful: slice 5 does not ship |
| Q6 machine-only fields | Yes. Both parity requirements are quoted and both are shown one-directional; the sweep's silence is named as absence of coverage, not permission | Yes — it gates slices 1, 2 and 3 together, and the packet says so | Yes. The counter-argument is the stronger-sounding one and is not smoothed | Two arms, the second named "the honest version". Default lawful: 1, 2, 3 hold |

No sibling packet's question is re-asked. Q4 is the same shape as M9's
Q6 and M8's Q1, each scoped to its own slices, which is proper; the
owner may wish to answer the class once. No owner trade-off is
smoothed into consensus language anywhere in the six; the packet
consistently states the counter-argument at equal or greater length
than the recommendation, which is the bar this corpus sets.

"Decided in this packet, not put to the owner": five of the six
entries are a delegate's to make (two measurements, one cost class,
one scoping choice, one epistemic-label correction on the packet's
own claims), and the sixth — S6-M4 routes through CC-REV-2 — escalates
rather than absorbs. The one owner question hidden in the packet is
not in that section but in Gate 5: F1.

## Measurements

| Claim | Re-derived? | My figure / note |
|---|---|---|
| Capture sizes 5,508,208 / 640,592 / 5,520,314 / 640,592 / 1,478,637 / 1,484,487 | yes | identical; the two envelopes are equal-length and differ in sha256, as stated |
| Revisions per capture (7c8743f63 / f4589e26; 2e3bac977 / 2ef68f5b) | yes | read from each body's own fields |
| 19 top-level keys, identical sets, both captures | yes | 19; `materializedBeadId` is null, so the dossier's 18 is explicable and correctly marked [Unknown] |
| 65.8% / 7.6% / 70.5% / 70.8%; headroom 2,868,294 / 618,515 / 612,665 | yes | exact; the human pair also matches M9's independent figures at `65de02b` |
| `machineHandle` routes.ts 159-162, quoted whole | yes | byte-exact |
| presentation handler 163-176; envelope fields 167-173 | yes | the four named fields are 167-170; the span 167-173 covers all seven |
| route table 206-239; 15 routes over 15 paths; 4 machine-credentialed, 11 human-open | yes | 9 literal + 3 spreads × 2; 7 `human-open` credential literals, 2 inside the helper, emitted 3× each |
| header sweep: 104 files (54 non-test), all nine tokens 0, `.writeHead(` 1 at server.ts:122 | yes | exact, both methods; the `parseTagAttrs` false positive confirmed and correctly outside the denominator |
| server.ts 121-124 quoted whole | yes | byte-exact |
| discoverability: 0 of 19 keys, 0 at any depth, 0 occurrences of the five route literals, `openapi` exactly 1 per body | yes | exact on both captures; the envelope's six literals are 0 |
| anchor census: 714 blocks, 916 anchors, 914 / 1 / 1, 916 distinct ids, both captures | yes | exact. Both populations are the two *presentation* captures; the Method 1 table says "the served bodies", which is loose |
| 914/916 = 99.7817% | yes | exact |
| declared union at polaris-narrative.ts lines 21 and 25, spread at 185-186 | yes | byte-exact; the packet's correction away from model.ts is right |
| construction sites over 72 non-test modules: evidence 9, work 2, requirement 1, decision 1, doctrine 0, contract 0 | yes | every cited line confirmed, including the `ledger.block('contract', …)` exclusion at polaris.ts:1088 |
| `inputsDigest` declared 108-109, computed 381-389, emitted 688-693 | yes | byte-exact |
| preimage size | **no** | five keys, not six / five-plus-one — F2 |
| BuildButlersPocModelInput 179-206, 13 members, 3 in preimage, 10 not | yes | exact |
| model.test.ts comment 341-342 verbatim, assertion 343, kinds at 314 and 259; 8 tests pass | yes | byte-exact; 8 passed this session |
| wall clock: 1,436 occurrences, 25 paths, 6 of 19 keys; 439/415/278/278/6 and 20 singletons | yes | exact on both captures; main.ts 134, 148, 168 byte-exact |
| schema subject: 769 / 241, 57 / 48, 273 union | yes | exact |
| PocModel 19 fields, 5 documented / 14 not; envelope 7 / 0; the two name lists | yes | exact, including the nested-comment note at 101-104, 106, 108 |
| `boundedResponse` 137-142 quoted whole | yes | byte-exact |
| gzip -6: 851,986 (15.4%) and 105,850 (7.2%); saved 4,668,328 and 1,372,787 | yes | exact; factors 6.48 and 13.97 match Q2's 6.5 and 14 |
| "two orders of magnitude inside the ceiling" | **no** | ≈13.7× — F11 |
| bytes per key: 2,273,467 / 1,657,461 / 1,493,219 / 80,130 / 17,371; sum 5,521,648 = 100.02% | yes | exact; codeStructure 27.05% |
| 15 `compareMultisets` call sites over 568 lines; 43 tests pass | yes | 16 occurrences, 1 of them the definition at line 161 |
| dossier line-citation table (6 rows) | yes | every row confirmed, including the 5-7 and 17-20 span corrections |
| registry lines 264-272, 273-282, 279, 280 quoted | yes | byte-exact; ceilings 2,097,152 and 8,388,608 |
| "eleven words" | **no** | ten — F10 |
| spec counts 24/24/1,008 and 17/31/1,152 | yes | exact |
| POC-REQ-004 at 184, text 188-191, oracle 199-200, falsifier 202, scenario 204-208 | yes | byte-exact |
| POC-REQ-020 at 377, text 381-382 | yes | byte-exact |
| PWB-REQ-006 at 340, ceiling sentence 378-379, scenario 419-426 | yes | byte-exact |
| PWB-REQ-014 at 759, closed-class 774-776, one scenario at 799-803 | yes | byte-exact; exactly one scenario under that requirement |
| PWB-REQ-020 at 902, text 906-910 | yes, quotation truncated | F9 |
| RFC2-26 lines 196-221 under the 194 heading, quoted whole; scope sentence 219-220 | yes | byte-exact |
| RFC1-9 239-261, RFC1-10 263-267, RFC1-12 278-284, RFC1-33 750-755 | yes | byte-exact |
| VIS-1 82-87, VIS-2 96-106, VIS-3 108-110, VIS-5 141-165, VIS-7 183-193; SEC-1 10-23 / 14-16 / 22-23; SEC-2 25-37 | yes | byte-exact, elisions marked. VIS-4 is 122-139; the packet says 122-140 (line 140 is blank) |
| continuation act 150-156 whole, 154-155 for the trigger | yes | byte-exact |
| improvement-cycles direction 55-56 whole | yes | byte-exact; lines 34 and 41 are short spans — F8 |
| three-surface literal sweeps: json-schema / openapi / schema document = 0 | yes | 0 |
| the "2 lines, 904 and 913" remainder | **no** | 0 under the stated predicate — F4 |
| 0 of 41 requirements and 0 of 55 scenarios name a links map, schema document, cache validator or join key | yes | swept both files: `endpoint` 0, `etag` 0, `conditional` 0, `join key` 0, `cross-revision` 0, `gzip`/`compress` 0; the 4 PWB `links` and 3 PWB `cache` lines are unrelated |
| act line 46 is the act-relative form | yes | confirmed; no digest reproduced anywhere in the packet |
| 605 / 624 / 640 / 22 / 4,4,19,3,1 | **no** | 606 / 625 / 641 / 23 / 5,5,20,4,2 — F3 |
| 0 current-digest citers for the implementation files | yes | 0 for all nine, over 641 tracked files |
| predicate A: nine heads, 22/9/10/10/7/5/5/5/5 changed, intersection 0 everywhere | yes | exact, every head and count |
| predicate B: 0/4/1/5/3/1/2/5/3 and the named files | yes | exact, every row and every file |
| routes.ts claimed by 6 of 9; model.ts 5; polaris.ts 5; project-shape-model.ts 3 | yes | exact |
| "no file in this pursuit is uncontended" | **no** | two of M10's nine are — F5 |
| M6's head has advanced from `e318cbd` | yes | its packet records `e318cbd`; head today is `83c9f60` |
| M3 and M4 name polaris.ts but not lines 407-409 / 1078 | yes | M3 names 1307, 346-361, 1328-1329; M4 names no lines |
| M9 slice 6(b) at its lines 920-925 | yes | byte-exact; the "different axes" reading holds |
| P-77 is the next free number | yes | max allocated at `a9f671e` is P-67 (P-54..P-67 all ruled, 26 rows under `^\| P-`); siblings hold P-68..P-76, one each, matching the table |
| baseline 65 tests over 4 files | yes | 8 + 43 + 12 + 2 |
| `32 OK, 20 WARN, 0 FAIL (52 checks)` | yes | identical, read as the tail line |
| conventions: 0 odd backticks, 2 over-78, 273 spans, 57 slash-bearing, 13 non-resolving | yes | exact, including the enumerated thirteen |
| 1,328 non-fence lines | boundary | 1,327 — F14 |

Invariants checked on the packet itself: no manifest or truncated
signed digest is quoted; no observed-repository path appears in a code
span; every substantive claim carries a label; the two act-bound
specifications and the registry entry are named as uneditable and no
slice touches them; `check_governance.py` ends 0 FAIL. The dossier is
not edited and neither is any sibling worktree.

## Verdict

One blocking finding (F1), six non-blocking (F2-F7), seven editorial
(F8-F14). The measurement work is sound and, where it differs from the
packet, the differences are small, systematic and in the packet's own
favour more often than not. The blocking finding is a disclosure gap,
not a measurement error, and is repairable inside Gate 5 and the
collision section without touching a figure.

Verdict: REVISE
