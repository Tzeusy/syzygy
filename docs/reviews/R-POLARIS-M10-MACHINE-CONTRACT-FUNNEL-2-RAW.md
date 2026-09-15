# R-POLARIS-M10-MACHINE-CONTRACT-FUNNEL — review 2 (raw)

Independent fresh-context review, read-only. Review **2** of the M10
packet. Review 1 is retained verbatim at
`docs/reviews/R-POLARIS-M10-MACHINE-CONTRACT-FUNNEL-RAW.md` (verdict
REVISE, F1–F14) and binds the bytes at commit `5c5ed0e`; this review
is bound to the repaired bytes below. This file is the raw output,
retained verbatim, and is a second `-RAW.md`, never an overwrite of
the first.

## Header

- Reviewer: fresh-context session, 2026-09-15.
- Worktree: branch `agent/syzygy-dov.10`, HEAD
  `2b5622009348b231fe66f60cf7886e18818a8860` (short `2b56220`), the
  head the brief names.
- `git status --short` in that worktree: **empty at start and at
  finish**; no tracked file was modified and nothing was written into
  it. No daemon was started, no provider called, no observed
  repository read, no `bd` write, no state-changing git command.
- Sibling worktrees were opened read-only for their packets and
  registers only.

Reviewed bytes, computed this session (`wc -c`, `wc -l`,
`sha256sum` — never transcribed):

| File | Bytes | Lines | sha256 |
|---|---:|---:|---|
| docs/design/POLARIS-M10-MACHINE-CONTRACT-FUNNEL.md | 135823 | 1682 | c609b08666bb6907953637a3587f3294a34586ec15b69085677f646b65c6953b |
| docs/evidence/polaris-m10-machine-contract-funnel-2026-09-15.json | 48446 | 856 | 1e4e31d96a8ef9df80305d1d2c6ddccc6476eb4eb0400aac9ca193b9aa1ec0d1 |
| .syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md | 33684 | 226 | 8b34705e86969438f107bd4d400b4ac38355107076148172d7bf62325f6573ba |
| docs/reviews/R-POLARIS-M10-MACHINE-CONTRACT-FUNNEL-RAW.md | 27447 | 432 | 2cb4d80cbd86cbb2c30ec6008104452c4ef79eea9fd62da3f21c38fc80a062f6 |

The raw's bytes and sha256 as the packet states them (27,447 and
`2cb4d80…` written in full there) match exactly [Observed,
recomputed]. The record's `review1.packet_measured_after_review1`
(135823 bytes, sha256 `c609b08…`, 1682 total lines, 1605 non-fence,
11 over-78) matches the packet's final bytes exactly [Observed,
recomputed four ways]. The record keeps the first draft's
`packet_bytes`/`packet_sha256` (106926 / `f4c7f16…`) unedited beside a
dated sibling note, which is the right shape.

Sibling heads read read-only this session, each in its own worktree:
lane B `4090f98`, M2 `f2f37dd`, M3 `6574600`, M4 `63b8e33`,
M5 `ba9ca61`, M6 `83c9f60`, M7 `f97baf4`, M8 `bce9039`,
M9 `65de02b`. Every one matches the head the packet's collision table
records [Observed].

Conventions of this file, re-derived over its own final bytes last of
all: **8** lines exceed 78 columns outside fenced blocks and table
rows — **7** of them finding headings that name their severity, and
**1** prose line carrying a single unbreakable code-span path; **0**
non-fence lines carry an odd backtick count. Every line number written
`:N` is 1-based as `cat -n` gives it, and a quotation spanning two
source lines names both.

Run in the worktree: the four cited test files — 8 + 43 + 12 + 2 =
**65** tests, all passing — and `python3 scripts/check_governance.py`,
whose last line reads `32 OK, 20 WARN, 0 FAIL (52 checks)`, read as
the tail line [Observed]. `npm run build:poc` was not needed and was
not run; nothing was written to `dist/`.

## Summary

Thirteen of the fourteen review-1 findings are repaired exactly, at
every site the disposition claims, with the superseded wording marked
in place and dated rather than deleted. The blocking finding F1 is
fully repaired in all four places and in the record: slice 3 now holds
behind P-72's Q1 in Gate 5, in Gate 3's act row, in Gate 4's slice 3,
in Q3, in the collision section, in the sequencing paragraph, in the
funnel summary and in the handoff; M5's question is not re-asked; no
seventh question was added; and Q3's recommended answer and default did
not move. F14 is repaired in the one place review 1 named but the same
class of self-referential figure went stale one Gate above it, which
is G1 — the only finding of consequence here.

No recommended answer and no default-if-unanswered moved between
`5c5ed0e` and `2b56220` [Observed, both drafts diffed]. The register
row is a faithful one-line rendering of the repaired Q1–Q6 table,
its recount is reproducible, and its claim about P-68…P-76 is true of
all ten worktrees.

## Review-1 repair verification, F1–F14

Each was checked against the current bytes **and** against source, not
against the disposition's own words.

| # | Verdict | Evidence |
|---|---|---|
| F1 | **REPAIRED** | Spec reader notes read at source: lines 25–26 of `openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md` carry, under the heading "Reader notes, binding on how this file is read", the sentence defining the machine answer as the authenticated GET /api/poc response — singular, definite [Observed]. M5's packet read read-only at `ba9ca61`: its Q1 line asks, verbatim, whether a new machine-credentialed route "need[s] a spec delta before it may be built, and if so to which spec?", register row P-72 [Observed]. Slice 3 is shown as holding behind P-72's Q1 at **six** sites, not the four claimed: Gate 5 (`:1078`–`:1108`), Gate 3's act row (`:752`), Gate 4's slice 3 (`:901`–`:909`), Q3 (`:37`), collision 1 (`:1320`–`:1329`) and the sequencing paragraph (`:1345`), plus the funnel summary (`:1617`) and the handoff (`:1668`). The superseded wording is marked in place at both sites review 1 named — collision 1 keeps "The two are complementary and the ordering is free. **No duplication.**" quoted inside its dated supersession bracket, and Gate 5's old heading is bracketed rather than dropped (but see G5). M5's question is **not** re-asked: the packet routes to P-72 and adds no seventh question [Observed, the six-row question table counted]. Q3's recommendation is still `machine-credentialed` and its default is still "slice 3 does not ship", now stated to cover the route question too — both unchanged from the first draft [Observed, the two drafts' Q3 cells diffed] |
| F2 | **REPAIRED** | `packages/three-surface-poc-core/src/model.ts` lines 381–389 quoted whole in the packet and read at source: the hashed literal has exactly five keys — `repoRoot`, `repositoryRevision`, `observerRevision`, `artifacts`, `mappingDigest` [Observed]. Both sites (`:35` in Q1, `:454`–`:456`) now read "four named inputs plus one derived digest (five keys)" with the superseded count quoted in a dated bracket |
| F3 | **REPAIRED, and the denominators still hold at `2b56220`** | Re-derived this session at the current commit with the packet's own predicates over `git ls-files`: **606** four-extension files under the three trees; **641** tracked under `docs/evidence/` and `.syzygy/governance/`; **625** four-extension over those two trees; **23** naming at least one of the five implementation paths, per file **5, 5, 20, 4, 2** [Observed]. These are identical to the packet's stated `5c5ed0e` figures: the raw review joined `docs/reviews/`, which is outside all three trees, and the register edit names no implementation path, so nothing moved. The 0-citer result also stands at `2b56220`: **0** citers for the current sha256 of each of the nine candidate files over the 641-file denominator [Observed, hashlib this session; no digest reproduced here]. Both denominators are stated with their commits at every site (`:139`–`:152`, `:161`–`:165`, `:171`–`:176`, `:766`, `:1441`) |
| F4 | **REPAIRED** | Python `re` over all **1,008** lines of the three-surface specification: the alternation `self-link|sibling route|endpoint list|endpoint map`, case-insensitive, returns **0** lines; the literal `links` returns exactly **2**, lines **904** and **913** [Observed, denominator every line of the file]. The packet now states both sweeps with their predicates (`:1045`–`:1063`) and marks the superseded attribution. The record keeps the original `…: 2` key unedited and adds two dated sibling keys plus a note — the shape the F4 disposition claims |
| F5 | **REPAIRED, exactly** | Predicate B recomputed this session over all nine sibling Gate 3 sections in their own worktrees: **0/4/1/5/3/1/2/5/3**, with `routes.ts` 6, `polaris.ts` 5, `model.ts` 5, `project-shape-model.ts` 3 — every row and every named file reproduces [Observed]. **7 of M10's 9** candidate files are named by at least one sibling; `polaris-narrative.ts` and `server.ts` by none. The basename-admitting variant gives **8 and 1**, lane B's Gate 3 being the one that names `polaris-narrative.ts` (with `polaris.ts` and `polaris-parity-sweep.test.ts`) [Observed]. Both are stated with denominators at `:1300`–`:1315` and in the funnel summary `:1618`; the zero/all sentence is quoted inside a dated supersession bracket at both sites |
| F6 | **REPAIRED for slice 1; see G2** | Implementation (1) is stated: Gate 3's slice-1 row (`:711`) now names `packages/three-surface-poc-core/src/model.ts` (the `PocModel` interface, lines 98–155 — confirmed at source) with a dated completion note; Gate 4's slice 1 (`:787`–`:806`) states the choice, quotes the improvement-cycles direction line 50 verbatim ("WIP one for POC shared-model changes" — read at source, line 50 exactly) and puts slice 1 in the shared-model queue; the sequencing paragraph (`:1339`–`:1347`) carries it. M8's Q7 (P-74, read at `bce9039`: the shared-`PocModel`-rewrite ceremony question) and M9's Q6 (P-75, read at `65de02b`: the direction/cycle-report question) are both named and **neither is re-asked** [Observed, both packets' question tables read]. The parity sweep's production comment at `apps/three-surface-poc/src/polaris-parity-sweep.test.ts` lines 5–7 is quoted byte-exactly and stays true under implementation (1). What the repair did **not** do is close the identical conditional one row above it — G2 |
| F7 | **REPAIRED, with the span corrected** | M9's packet read read-only at `65de02b`: slice 6(b) at its lines 920–925, the rule-6 mutant block opening at 927 and mutant (c) at lines **929–932**, whose words the packet quotes byte-exactly [Observed]. Named in Q5's cell (`:39`) and in collision 3 (`:1331`–`:1337`), with arm three identified as M9's own answer and arm one as requiring M9 to relax that mutant. Q5's recommendation and default are unchanged [Observed, drafts diffed] |
| F8 | **REPAIRED** | The direction's cycle definition spans lines **34–35** and the report sentence lines **41–42**; line 36 carries "derived only from recorded findings" whole [Observed, read at source]. Q4's cell now cites 34–35 and 41–42 and marks both corrections |
| F9 | **REPAIRED** | PWB spec lines 906–910 read at source; the sentence continues ", preserving multiplicity and exact provenance state." and ends on line 910 [Observed]. Q6's cell marks the elision and gives the continuation |
| F10 | **REPAIRED** | "the final encoded HTTP body for each Polaris HTML response" at registry line 279 is **ten** words; its twin at line 280 is **twelve** [Observed, counted; both quoted byte-exactly]. Corrected at all three sites (`:36`, `:236`–`:237`, `:578`) |
| F11 | **REPAIRED** | 2,132,656 × 0.072 = 153,551.2; 2,097,152 ÷ 153,551.2 = 13.66 [Observed, recomputed]. `:568`–`:575` now reads "roughly **14 times inside**" with the arithmetic shown and the superseded phrase quoted in a dated bracket |
| F12 | **REPAIRED** | `git diff --name-only a9f671e 4090f98` lists **22** paths this session, including PROJECT-STATUS.md and the phrase-registry YAML under contracts/candidates/ [Observed]. Both are added at `:1290`–`:1296`; the planning-only claim is re-verified — no sibling branch touches any of M10's nine candidate files, so predicate A is **0** everywhere [Observed, all nine diffs read] |
| F13 | **REPAIRED** | Both locators added, as file plus jq path, for the `-data.json` and the `-harvest.json`, with the **0** occurrences in the `.md` stated (`:80`–`:90`, `:113`–`:121`). The dossier is not edited [Observed, `git diff` against `5c5ed0e` lists only the packet, the record and the register] |
| F14 | **REPAIRED at the site named** | The first draft splits into 1,405 segments, 1,404 lines, **1,327** non-fence [Observed, recomputed on `git show 5c5ed0e:` bytes]. Gate 6 item 11 now says 1,327 with the trailing-boundary convention stated and 1,328 marked. The same item's *other* convention figures were not re-derived — G1 |

Two claims in the repairs section cannot be verified from bytes and
are recorded as such. "Every one of the fourteen findings was
re-derived against source before being applied" asserts an ordering
inside the repairing session; each finding is correct *now*, which is
all these bytes can show [Unknown for the ordering, Observed for the
results]. The same holds for "computed last of all in this pass".

One repair improves on the review it answers: review 1 reported the
literal "machine answer" as occurring "once in the whole packet"; the
repair reports **1 line and 3 occurrences on it**, all inside Q6's
row, and states why a per-line count alone understates. Recomputed on
the first draft's bytes: 1 line, 3 occurrences, line 40 [Observed].

## New findings

### G1 — non-blocking — Gate 6 item 11's convention figures are stale at the repaired bytes, while the item asserts they were re-derived over exactly those bytes

`docs/design/POLARIS-M10-MACHINE-CONTRACT-FUNNEL.md:1475-1504`.

Defect. Item 11 states, unqualified: "**Two** lines exceed 78 columns
outside fences, tables, headings and block quotes, and each is a
single unbreakable code-span path: the observer registry entry and the
RFC-0001 filename"; and "Of **273** distinct code spans, **57**
contain a `/` and **13** of those do not resolve as a path in this
worktree; each is enumerated here". It closes: "Every figure here was
re-derived over these bytes rather than carried forward from an
earlier draft."

Re-derived over the committed bytes at `2b56220` this session
[Observed; predicates stated, denominator all 1,682 lines and all
non-fence code spans]:

- over-78 under item 11's own predicate (outside fences, tables,
  headings and block quotes): **three**, not two — lines 575 and 1150
  as named, plus line **801**, the improvement-cycles direction's path
  as a single code span, which the F6 repair added to Gate 4's slice 1.
- distinct code spans: **301**, not 273.
- slash-bearing: **65**, not 57.
- non-resolving: **15**, not 13. The two the enumeration does not
  carry were both introduced by the repair pass: the quoted route form
  at lines 904 and 1094 (from the F1 repair's reader-note quotation),
  and the bare `contracts/` inside the F3 disposition row at line
  1555.

Only the non-fence-line figure in that item was corrected and dated;
the bracket at `:1473`–`:1475` says "That denominator is the first
draft's" and refers to the 1,327/1,328 pair alone, so the four figures
above stand as live, unmarked claims about the current bytes, and the
item's own closing sentence makes them false rather than stale. The
review-1 section's own conventions paragraph (`:1591`–`:1602`) does
re-derive the over-78 count correctly (11 under the wider predicate),
which is what makes item 11's "Two" a contradiction inside one file
rather than merely an omission.

This is the F3/F14 class exactly: a self-referential figure over a
population the current pass is still editing, read rather than
re-derived. AGENTS.md records both the lesson and the rule that
staleness is marked at the stale sentence, never covered by a note
elsewhere on the page.

Repair. Re-derive item 11's four figures over the final bytes, state
the two added non-resolving spans in the enumeration, and mark the
superseded values in place with their date, as every other corrected
figure in this packet is.

### G2 — non-blocking — the F6 decision closes slice 1's landing question and leaves the identical one open for slice 2, while Gate 4 and the sequencing paragraph already rely on it being closed

`docs/design/POLARIS-M10-MACHINE-CONTRACT-FUNNEL.md:712` against
`:711`, `:802`–`:804` and `:1339`–`:1344`.

Defect. F6's argument is general, not slice-specific: `machineHandle`
serves `JSON.stringify(model)` (`apps/three-surface-poc/src/routes.ts`
lines 159–162, quoted correctly and confirmed at source), so **any**
new top-level key in that body is either a member of `PocModel` or a
wrapper, and the wrapper falsifies the parity sweep's production
comment. Slice 2's `responseIdentity` is a new top-level key in that
same body. The packet applies the argument to slice 1 and decides it,
but Gate 3's slice-2 row still reads "`packages/three-surface-poc-core/src/model.ts`
**if** the field lands on `PocModel` rather than on the response
envelope", and Gate 4's slice 2 (`:846`–`:855`) does not say either.

The packet meanwhile relies on the answer: Gate 4's slice 1 says
"Slice 1 therefore joins slice 2 (on Q1's recommended arm) in that
one-at-a-time queue", and the sequencing paragraph says "it and slice
2 are both POC shared-model changes". Both sentences presuppose that
slice 2's field lands on `PocModel` — the proposition the row above
leaves conditional [Observed for the three sites; Inferred that the
F6 argument settles slice 2, since the disjunction and the falsified
comment are the same].

Nothing an owner must rule turns on it — the credential class, the
act, the recommendation and the default for slice 2 are all
unaffected — but it leaves the packet asserting a WIP-one ceremony
consequence for a slice whose topology row still names two possible
implementations.

Repair. Either state in Gate 3's slice-2 row that the F6 argument
decides it the same way, or say in Gate 4's slice 2 why the wrapper
remains open there and withdraw "both POC shared-model changes" to
the conditional form.

### G3 — editorial — the conventions paragraph's arithmetic contradicts its own enumeration

`docs/design/POLARIS-M10-MACHINE-CONTRACT-FUNNEL.md:1597-1602`. The
paragraph states **11** over-78 lines, then enumerates them as the
title, **2** slice headings, **3** single-code-span lines and **5**
block-quoted RFC2-26 lines, and closes "[Observed, enumerated this
session over the final bytes; 1 + 2 + 4 + 5 = 12.]" The enumeration is
right (1 + 2 + 3 + 5 = 11, and the eleven lines are 2, 778, 839, 575,
801, 1150, 1131, 1132, 1137, 1139, 1143 [Observed, enumerated this
session]); the arithmetic line is wrong twice, in the addend and in
the sum, and is the one part of the sentence a reader would use to
check it.

### G4 — editorial — VIS-4 is cited as vision.md lines 122–140; the clause ends at 139

`docs/design/POLARIS-M10-MACHINE-CONTRACT-FUNNEL.md:653`, and the
record's `measurements.M11_spec_sweeps.anchors_used`. Line 139 ends
"…treating RFC acceptance alone as opening the gate."; line 140 is
blank [Observed, read at source]. Review 1 recorded this in its
measurement table but filed no numbered finding, so it survived a
pass that corrected four other spans against the packet's own stated
line-count convention.

### G5 — editorial — the Gate 5 supersession note misquotes the heading it supersedes

`docs/design/POLARIS-M10-MACHINE-CONTRACT-FUNNEL.md:1079-1082` reads:
[The heading read "**Slice 3 — no delta**" without qualification until
2026-09-15]. At `5c5ed0e` that heading read "**Slice 3 — no delta;
the disclosure it carries is the thing PWB-REQ-014 already closes.**"
[Observed, `git show 5c5ed0e:` this session]. It did carry a
qualification — just not the one about the route — so the note both
shortens the superseded words inside quotation marks and mischaracterises
them. The packet's own rule is that superseded wording is marked in
place, and marking it accurately is the point of the rule.

### G6 — editorial — RFC5-3 is named in Gate 4 with no path, no quotation and no Gate 0 entry

`docs/design/POLARIS-M10-MACHINE-CONTRACT-FUNNEL.md:952` calls the
daemon's credential-first admission "the RFC5-3 posture". RFC-0005's
rev10 modules live under `.syzygy/governance/contracts/candidates/`,
the clause is not in Gate 0's Contracts row, and the sentence carries
no quotation and no line number — against this packet's convention of
quoting every clause at its defined location, and against verification
rule 8. The design point does not rest on it; the citation should
either be anchored and quoted or dropped to a description of what
`packages/cap1-daemon/src/server.ts` lines 188–200 do.

### G7 — editorial — the funnel summary's G6 Bar line was rewritten without a supersession marker, unlike its two neighbours

`docs/design/POLARIS-M10-MACHINE-CONTRACT-FUNNEL.md:1615`. At
`5c5ed0e` the line ended "NO independent review yet - this is a first
draft"; it now reads "ONE independent review (2026-09-15, verdict
REVISE …)" with no bracket [Observed, drafts diffed]. The two lines
immediately below it in the same fenced block — Open questions and
Collisions — both carry "[this line read …]" brackets, so the omission
reads as an oversight rather than a policy.

### G8 — editorial — Gate 6 item 7's working-tree sentence is stale

`docs/design/POLARIS-M10-MACHINE-CONTRACT-FUNNEL.md:1436-1437`: "A
short git status in the worktree names only this packet's two files."
At `2b56220` the tree is clean and the branch's diff against
`a9f671e` carries three files — the packet, the record and
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`, which the
same pass added the P-77 row to [Observed].

## The six questions, after the repairs

| # | Scope truthful? | Genuine human gate? | Recommendation follows from the evidence? | Every lawful arm named? |
|---|---|---|---|---|
| Q1 equality key | Yes. Both candidate keys are shown false at source in opposite directions, the preimage count is now right, and the scope residue (POC-REQ-004 quantifies over code-structure facts, 27.05% of the body) is stated against the packet's own recommendation | Yes. Whether a code-structure determinism requirement warrants a whole-payload identity is a scope reading, and the continuation act's "any scope beyond the signed change" trigger is quoted | Yes, and the counter-argument is given at least equal weight. Labeled [Inferred] where it is a reading | Three arms; the third is the honest narrow one. None called unlawful. Default stated and lawful: slice 1 lands, 2/3/4a hold |
| Q2 compression | Yes. The registry sentence is quoted byte-exactly at lines 279–280, the word count is now ten, the 14× factor is now consistent with the rest of the packet, and both readings are set out in the same words | Yes — the continuation act's registry-envelope trigger is quoted whole at lines 150–156 and the trigger sentence spans 154–155, both confirmed at source | Yes. The VIS-2 polarity argument is doctrine-anchored and the cheaper arm is named as cheaper and as leaving a false sentence standing in a file that may not be edited | Two arms plus the do-nothing default. Neither called unlawful. Default lawful: 4b does not ship, 4a unaffected |
| Q3 schema credential class | **Yes now.** The route's existence question is disclosed beside the credential-class question, in the cell itself, with P-72 named and the spec's reader-note definition cited at lines 25–26 | Yes for the credential class — SEC-1's violation list names this exact case, quoted byte-exactly at security.md lines 14–16 and 22–23 — and the second gate is disclosed rather than absorbed | Yes on the class, and it did not move. The dossier's own arm is still stated as "real" | Both credential arms named; the prior unruled question is routed to P-72 rather than re-asked, which is the disposition review 1 offered. Default lawful and now explicitly two-fold: slice 3 does not ship |
| Q4 tracing | Yes. The direction is quoted at its own clause with both two-line spans corrected, and the 24/24 and 17/31 sweeps re-derive exactly | Borderline-but-fair, unchanged: the second limb's reading is genuinely contestable and the third arm is honestly labeled the cheapest affirmative one | Yes, and the counter-argument concedes that "slice 3 adds a document that has never existed" | Three arms. None called unlawful. Default lawful: filed, not landed |
| Q5 join key | **Yes now.** F7's omission is closed: arm three is identified as M9's existing answer and arm one as requiring M9 to relax a designed failing mutant, with the mutant quoted and its span corrected | Yes. RFC1-9 reserves minting authority by class and PWB-REQ-014's sentence is quoted exactly at PWB spec lines 774–776 | Yes, and the recommendation did not move | Three arms. None called unlawful. Default lawful: slice 5 does not ship |
| Q6 machine-only fields | Yes. Both parity requirements are quoted and both shown one-directional; PWB-REQ-020's elision is now marked and its continuation given; the sweep's silence is named as absence of coverage, not permission | Yes — it gates slices 1, 2 and 3 together and the packet says so | Yes. The counter-argument is the stronger-sounding one and is not smoothed | Two arms, the second named "the honest version". Default lawful: 1, 2, 3 hold |

No sibling packet's question is re-asked [Observed, all nine sibling
question tables read this session]. No owner trade-off is smoothed
into consensus language; the packet still states each
counter-argument at equal or greater length than its recommendation.

"Decided in this packet, not put to the owner" now carries six
entries. Five are a delegate's to make (two measurements, one cost
class, one scoping choice, one epistemic-label correction on the
packet's own claims) and the sixth — S6-M4 routes through CC-REV-2 —
escalates rather than absorbs. The new sixth entry, the F6 decision
that slice 1's `links` field lands on `PocModel`, is a design choice a
delegate may make: it names its own ceremony consequence, quotes the
constraint, and routes the ceremony question to M8's Q7 and M9's Q6
without re-asking either. **No owner question is hidden in that
section.** The one incompleteness it leaves is G2, which is a topology
row, not a question.

## Measurements re-derived this session

| Claim | Re-derived? | Note |
|---|---|---|
| 1,436 occurrences / 25 distinct paths / 6 of 19 top-level keys | yes | exact on **both** retained machine bodies; per-path 439/415/278/278/6 and 20 singletons all exact |
| 19 top-level keys, identical sets, both captures | yes | 19; `materializedBeadId` present and null |
| 914 of 916 anchors `evidence`; 714 blocks; 916 distinct ids | yes | byte-for-byte identical on both presentation envelopes; 914/916 = 99.7817% |
| the two envelopes are 640,592 bytes each with different sha256 | yes | confirmed |
| header sweep: 104 `.ts` files (54 non-test), all nine tokens 0, `.writeHead(` 1 at server.ts line 122 | yes | exact, word-bounded Python `re` |
| schema subject 769 / 241, 57 / 48, 273 union | yes | exact under the record's key-path predicate (825 and 69 under an all-paths variant, which is not the stated predicate) |
| `PocModel` 19 fields, 5 documented / 14 not; envelope 7 / 0 | yes | exact, and the five and fourteen name-lists are right |
| gzip level 6: 851,986 (15.4%) and 105,850 (7.2%); saved 4,668,328 and 1,372,787 | yes | exact |
| bytes per key 2,273,467 / 1,657,461 / 1,493,219 / 80,130 / 17,371; sum 5,521,648 = 100.02% | yes | exact under the record's stated `json.dumps` method; `codeStructure` 27.05% |
| `inputsDigest` five keys at model.ts 381–389; exclusion asserted at model.test.ts 343 with kinds at 314 and 259 | yes | byte-exact; the file's 8 tests pass |
| `BuildButlersPocModelInput` 179–206, 13 members | yes | exact |
| route table 206–239, 15 routes over 15 paths, 4 machine-credentialed / 11 human-open | yes | exact |
| `machineHandle` 159–162, `boundedResponse` 137–142, `respond` 121–124 quoted whole | yes | byte-exact |
| 15 `compareMultisets` call sites over 568 lines | yes | 16 occurrences, 1 the definition at line 161 |
| the four-literal alternation 0; the literal `links` 2 at 904 and 913 | yes | exact, over all 1,008 lines |
| 24/24/1,008 and 17/31/1,152; PWB-REQ-014 has exactly one scenario, at 799–803 | yes | exact |
| POC-REQ-004 at 184, text 188–191, oracle 199–200, falsifier 202, scenario 204–208; POC-REQ-020 at 377, text 381–382 | yes | byte-exact |
| PWB-REQ-006 at 340, ceiling sentence 378–379, scenario 419–426; PWB-REQ-014 774–776; PWB-REQ-020 906–910 | yes | byte-exact; the scenario's "encoded-byte" is hyphen-wrapped in the source and joined in the quotation |
| registry lines 264–272, 273–282, 279, 280; ten and twelve words | yes | byte-exact |
| continuation act 150–156 whole; trigger 154–155 | yes | byte-exact |
| improvement-cycles direction 34–35, 36, 41–42, 50, 55–56 | yes | byte-exact, every span |
| VIS-1 82–87, VIS-2 96–106, VIS-3 108–110, VIS-5 141–165, VIS-7 183–193; SEC-1 10–23 / 14–16 / 22–23; SEC-2 25–37 | yes | byte-exact, elisions marked. VIS-4 is 122–139 — G4 |
| RFC2-26 196–221 under the 194 heading, quoted whole; scope sentence 219–220 | yes | byte-exact |
| RFC1-9 239–261, RFC1-10 263–267, RFC1-12 278–284, RFC1-33 750–755 | yes | byte-exact; RFC1-13 is 286–289 and is not cited in the prose |
| collision table: nine heads, 22/9/10/10/7/5/5/5/5 changed, predicate A intersection 0 everywhere | yes | exact, every head and count |
| predicate B 0/4/1/5/3/1/2/5/3; 7 of 9 strict, 8 of 9 basename-admitting | yes | exact, every row and every file |
| 606 / 641 / 625 / 23 and 5,5,20,4,2 at `5c5ed0e` | yes | identical at `2b56220` — the raw landed outside all three trees |
| 0 current-digest citers for all nine candidate files over 641 files | yes | 0 for every one |
| 65 tests over 4 files; `32 OK, 20 WARN, 0 FAIL (52 checks)` | yes | identical, read as the tail line |
| packet self-figures 135,823 bytes / 1,682 lines / 1,605 non-fence / 11 over-78 / 0 odd-backtick | yes | all exact of the bytes that carry them |
| Gate 6 item 11's "Two" over-78, 273 spans, 57 slash-bearing, 13 non-resolving | **no** | 3 / 301 / 65 / 15 — G1 |
| register recount 22 open / 5 act / 27, from main's 21/5/26 | yes | reproducible by the stated predicate `^| P-` partitioned by `##` section |
| P-68…P-76 each live only on their own branch | yes | each sibling register carries exactly one of them; main carries none of P-68…P-77 |

Invariants checked on the packet, the record and the register: no
manifest and no truncated signed digest is quoted; no observed-repository
path appears in a code span (`check_governance.py` CG-1b and CG-15 both
pass); the two act-bound specifications and the registry entry are named
as uneditable and no slice touches them; the P-77 row quotes no digest
and backticks no observed-repository path; substantive claims carry
[Observed]/[Inferred]/[Unknown] labels; superseded wording is marked in
place and dated rather than deleted, with the exceptions at G5 and G7.
The dossier is not edited and no sibling worktree was written to.

## Verdict

No blocking finding. Two non-blocking (G1, G2) and six editorial
(G3–G8). All fourteen review-1 findings are repaired — thirteen
without qualification, F6 for the slice it names — and the blocking
one is repaired more thoroughly than its disposition claims. The two
non-blocking findings are of the same family as F3/F14 and F6: a
self-referential figure left un-re-derived after the edits that moved
it, and a general argument applied to one row and not the row above.
Neither moves a recommendation, a default or an owner question.

Verdict: CONFIRM WITH EXCEPTIONS
