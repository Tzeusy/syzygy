# R-M9-ONE-IDENTITY-FUNNEL-2-RAW

Independent fresh-context review 2 of the M9 one-identity funnel packet,
of the repairs applied to review 1's findings F1-F21, and of the P-75
register row. Review 1 is retained verbatim at
`docs/reviews/R-POLARIS-M9-ONE-IDENTITY-FUNNEL-RAW.md`, verdict REVISE.

## Subject and digests

Worktree `scratchpad/m9wt`, branch `agent/syzygy-dov.9`, HEAD
`3e764d8840c98f1251a88e01c295f8ffc014df93` (subject: "docs: M9 funnel
review 1 retained, F1-F21 applied, P-75 registered [syzygy-dov.9]").
Baseline of the packet's own source measurements: Syzygy `a9f671e` on
main.

Computed this session with `wc -c` and `sha256sum`, never transcribed:

| File | bytes | sha256 |
|---|---:|---|
| `docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md` | 132428 | `1b5e98a60623bee98a888a12e88fbe90e9241f158b36f6bca516ef9bd29de3b4` |
| `docs/evidence/polaris-m9-one-identity-funnel-2026-09-15.json` | 48632 | `aa3e68a8370e0840097d4dcfc03fb1ca3616254a4ff9aec4611adf3845281d84` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 33712 | `3845d85c3ceec6f9f2a0c7877e06498169e256d93c897e02dc5cad9f67309333` |
| `docs/reviews/R-POLARIS-M9-ONE-IDENTITY-FUNNEL-RAW.md` | 42309 | `fa280ab0544e8211ed9c8a38982ad073735590e3d61750398e65a795dd67b82e` |

The raw's byte count and digest are exactly what the packet's review-1
section cites for it, so that citation is correct against current bytes.
[Observed]

Sibling worktrees read read-only at these heads: `laneb` `4090f98`,
`m2wt` `f2f37dd`, `m3wt` `6574600`, `m4wt` `63b8e33`, `m5wt` `ba9ca61`,
`m6wt` `83c9f60`, `m7wt` **`1803608`** (past the `0c4b4a9` the packet
names), `m8wt` `4b2e8cb`. M8 was also read at `8035c8f` by `git show`.

`python3 scripts/check_governance.py` run in `m9wt` this session with all
three written files present; its last line, read rather than grepped,
reads: 32 OK, 20 WARN, 0 FAIL over 52 checks, counts derived rather than
asserted. `git status --short` in `m9wt` was empty before and after this
review; no tracked file and no `node_modules` entry was modified. No
daemon was started, no provider was called, no Butlers checkout and no
`.worktrees/` directory was read, and `machine-credential.token` was
never opened. `npm run build:poc` and `npm test` were not run: no claim
in this packet rests on a test result, and every test-file citation was
verified by reading the file at its cited line instead.

Scope: (a) each of F1-F21 verified against current bytes and against
source; (b) every load-bearing measurement review 1 reproduced re-run
independently this session; (c) the P-75 row and its blockquote; (d) the
six questions; (e) a fresh read for defects neither review has named.
New findings are numbered G1...

## Review-1 repair verification

"Re-derived" below means recomputed this session from source or from the
retained captures under the packet's own stated predicate.

| # | Sev | Verdict | Evidence |
|---|---|---|---|
| F1 | blocking | **REPAIRED** | The href-census section now carries a five-row provenance table naming each file's daemon, evaluation and as-of. I read the five captures' embedded evaluation blocks myself: `polaris-7478.html` carries `butlers:66ed58f`, `observer:a121591`, as-of `2026-09-10T01:50:48.470Z`; `home.html` and `api-poc.json` carry `butlers:7c8743f`, `observer:f4589e2`, as-of `2026-09-13T02:03:33.040Z`; `trajectory-7478.html` and `orrery-7478.html` embed **no** snapshot label, observer id or timestamp at all, and the packet labels both [Unknown] from the bytes and [Inferred] from the log. The retained run script and daemon log show `--port 0 --state-dir`, `http://127.0.0.1:41215/`, observed revision `7c8743f6…`, and the same run's Polaris output is an 838-byte body with `"served":"nothing"`, `"failure":"response-limit-breached"`, `observed` 2132656 against `declared` 2097152, `readiness` false. The packet's "Which figures depend on which" paragraph names the four-page figures, the `api-poc.json`-only figures and the lane-A figures separately. **The census recomputes to the cell over both retained `api-poc.json` files** (`capture/` and `m1/measure/after/`), walking every object whose `label` is one of the three doctrine labels: 1,167 total; key signatures `{freshness,label,tier}` 1,137, `{freshness,label,reasons}` 12, `{basis,label}` 9, `{label,reason}` 9; 30 without a tier of which 18 are the nine entities and nine relationships; Observed 1,146 / Unknown 21 / **Inferred 0**; tier `report-fact` 1,137 and 0 of the other five; freshness `fresh` 1,149 and 0 of the other three; challenge `unchallenged` 1,149; Unknown primary reason `excluded-content` 12 and 0 of the other eleven. Identical in both files. The record marks the false `provenance` value **in place** (`-- FALSE`) and appends `provenance_corrected_2026_09_15`; nothing was deleted. Gate 6 bullet 1 is narrowed to "each named to the evaluation it was actually served from" |
| F2 | blocking | **REPAIRED** | The disjointness sentence is replaced by measured rows with the superseded wording kept and dated. Recomputed under the packet's own predicate B (code spans naming an implementation-plane path inside the sibling's "Gate 3 — Topology" section, fences stripped, resolving in that sibling's worktree) against the eleven-file surface: **M7 11 spans / 1 shared** (`routes.ts`) — identical at `0c4b4a9` and at today's `1803608`; **M8 at `4b2e8cb` 20 / 7** (`orrery.ts`, `polaris-copy.ts`, `polaris.ts`, `routes.ts`, `trajectory.ts`, `model.ts`, `project-shape-model.ts`); **M8 at `8035c8f` 19 / 6**, without `project-shape-model.ts` — exactly as the packet states, including the direction of the change. M8 is added to collision item 2's shared-model queue. A question-level collision table discloses M8 Q7 by identifier and subject; I read M8 Q7 at source in `m8wt` and the packet's rendering of it is faithful. **M8's question is not re-asked**: M9 Q6 asks whether the pursuit is a continuation or a new cycle owing a report, M8 Q7 whether one shared-model rewrite triggers the ceremony; the packet proposes an ordering and labels it [Inferred] |
| F3 | non-blocking | **REPAIRED** | The ceiling table gains a "Daemon and evaluation" column on all eight rows and both pre-lane-A Polaris observations. Re-derived: `polaris-7478.html` 2,090,025 bytes, 2,097,152 − 2,090,025 = **7,127**; the breach body records 2,132,656 against 2,097,152, over by **35,504**. Every other row re-derives: trajectory 254,168 (headroom 1,842,984), orrery 37,048 (2,060,104), home 38,706 (2,058,446), `/api/poc` 5,520,314 against 8,388,608 (2,868,294). The two 7478-daemon rows are now labelled as such. See G7 on the sentence that frames them |
| F4 | non-blocking | **REPAIRED** | Recomputed over the four captures with the nine `model.entities` ids as denominator and "an attribute whose value is exactly one of the nine" as predicate: home 3 (`id`, `data-entity-id`, `data-surface-entity`), Polaris 8 (`data-argument-ref`, `data-capability-deep-dive`, `data-claim-provenance`, `data-depth-dive`, `data-depth-source`, `data-polaris-section`, `data-proposal-capability`, `data-unknown-disclosure`), Orrery 2, Trajectory 0; **union 11**, the names exactly as the packet's table lists them. Corrected in Gate 1, the funnel summary and the record's `distinct_names_union` (with the superseded 10 kept) |
| F5 | non-blocking | **REPAIRED** | Gate 3 names **eleven** distinct implementation files (`polaris.ts`, `trajectory.ts`, `orrery.ts`, `materialize-action.ts`, `page-shell.ts`, `routes.ts`, `polaris-copy.ts`, `exact-tables.ts`, `model.ts`, `project-shape-model.ts`, `epistemic.ts`) and four test files, the four deliberately out of the surface. On the eleven-file surface every collision row re-derives exactly at the heads named: M1 1/1/0/0, M2 11/4/7/4, M3 13/4/9/2, **M4 22/9/13/8**, M5 9/3/5/3, M6 13/0/9/0, lane B 1/0/n-a/0. M4's eight are exactly the eight the packet names, and the residue (`page-shell.ts`, `materialize-action.ts`, `epistemic.ts`) is right |
| F6 | non-blocking | **REPAIRED** (see G5, G6) | The pursuit *record set* is defined once at the head; each of the four quotations is now cited to `docs/pursuits/2026-09-13-vision-pursuit-data.json` by line with the `-harvest.json` twin named. Verified at source: the tier parenthetical at data line 4296 / harvest 3889, the enumeration at data 4360 / harvest 3953, and 14,804 and the P-63 percentage in both JSON files. `grep -c -F` over `docs/pursuits/2026-09-13-vision-pursuit.md`: **0** hits for each of the four strings. The dossier `.md` is not edited |
| F7 | non-blocking | **REPAIRED** | Set difference recomputed: RFC1-25's table header at line 494, separator 495, data rows **496-521 = 26**, carrying **30** backticked first-column tokens; the enumeration at data line 4360 lists 25 comma-separated entries covering 26 tokens once `contains/part_of` is split; the four omitted are `calls`, `exposes`, `accesses(mode)`, `succeeds`. The packet now states the set difference as its predicate with the denominator 30. The load-bearing intersection re-derives: **{`contains`}, 1 of 8** |
| F8 | non-blocking | **REPAIRED** to the byte | One predicate now governs all four part rows ("delete the element, its own tags included"). Re-measured on **both** Polaris captures by depth-matched tag walk, identical on each: band **14,820**; 11 headings **2,130**; 9 `data-claim-provenance` spans **1,534** with tags (905 inner text); 9 `class="citation"` spans **4,309**; the whole `<section class="relationships">` **5,680** (inner `<ul>` 5,077), and its stated decomposition h3 189 + lede 243 + wrapper 171 + 5,077 = 5,680. Recoveries **5,843** and **11,523**; against the P-63 trim's 434,960 that is 1.34% and 2.65%, rendered 1.3% and 2.6%. Nine tuples at the measured mean 586.4 = **5,278**, so the net is +565 to +6,245, exactly as restated. Superseded 5,214 / 10,291 and the superseded −64/+5,013 net are kept and dated |
| F9 | non-blocking | **REPAIRED** | `class="wi-card"` counted this session: **310** in `trajectory-7478.html`, 299 in `trajectory.html`. The packet uses 310 and names why |
| F10 | non-blocking | **REPAIRED** | Gate 3's slice 6 row now carries `packages/three-surface-poc-core/src/model.ts` with the reason (slice 6b's canonical identity and its alias list live on the model), the superseded omission marked, and the four-slice work-in-progress queue intact and consistent with line 100-101 and collision item 2 |
| F11 | non-blocking | **REPAIRED** | Read at source: spec lines 903-904 are "**Oracle**: HTTP/anchor resolution per enumerated element; zero dangling links over the exhausted population decides." The packet quotes exactly that, at those lines, with the superseded paraphrase kept and marked |
| F12 | non-blocking | **REPAIRED** | The Gate 5 conclusion is qualified to "on Q2's recommended arm", "squarely" is dropped from the [Observed] clause, and the sentence now says plainly that on Q2's second arm slice 4a *does* map. Mirrored in the funnel summary's G5 line |
| F13 | non-blocking | **REPAIRED** | Q4 is recast as "If and when an agent asserts something, may the POC construct `Inferred`?" with the superseded wording kept; the cell now states that on the recommended arm no trigger is reached and that what is put is the constructible limb, consistent with Gate 3's act row for slice 4b. The recommended answer did not change |
| F14 | non-blocking | **REPAIRED** (see G2) | A third lawful arm — RFC2-26's reviewed N/A judgment package — is added to Q1 and to Q3, with per-slice reachability stated as this packet's reading and labelled [Inferred]: slice 6a reachable, slice 8 arguable and put rather than assumed, the other seven not reachable. The clause is cited at its own lines (route 201, home and gate 206), both verified at source |
| F15 | non-blocking | **REPAIRED**, all five | (1) `.syzygy/governance/doctrine/trust-and-evidence.md` line 16 reads "An LLM assertion is **Inferred, never Observed**" and is now quoted verbatim in Q4. (2) The improvement-cycles direction's report sentence begins at line **41** and "derived only from recorded findings" at line **36**; both cited correctly. (3) The PWB implementation act's "and a new owner act" begins at line **79**, its sentence at **78**; stated exactly that way. (4) RFC2-26's scope sentence begins at line **219**. (5) "the clause text is the authority, and nothing here restates a clause normatively" is `CONTRACT-COVERAGE.md` lines **7-8**, its own head banner, and is now attributed as such; CC-SPEC-8 is at `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` line **229** per `DIRECTIVE-REGISTER.md` line 129, carrying the per-consequence row unit — all four verified at source |
| F16 | non-blocking | **REPAIRED** (see G3) | `P-7[4-9]` swept over the packet and the record: **P-75** everywhere, no live P-74 claim for M9, and the superseded forecast kept and dated. Recounted with the predicate `^\| P-` over all nine registers this session: `laneb` P-68, `m2wt` P-69, `m3wt` P-70, `m4wt` P-71, `m5wt` P-72, `m6wt` P-73, `m8wt` P-74, `m9wt` **P-75**, and `m7wt` now **P-76** at `1803608`. M9's assignment is safe; the *sentence about M7* is not (G3) |
| F17 | non-blocking | **REPAIRED** | `apps/three-surface-poc/src/routes.ts` line 80 is quoted whole, all four sentences, matching the file byte for byte |
| F18 | non-blocking | **REPAIRED** | A four-row question-level collision table names M3 Q1, M2 Q1, M2 Q6 and M8 Q7 with the M9 question that presupposes each. I read all four at source in their own worktrees at the heads named; each rendering is faithful to the sibling's own wording, each is given by identifier and subject only, none is re-asked, and none is ruled |
| F19 | editorial | **REPAIRED** | Read at source: VIS-3 runs 108-120 and VIS-4 122-139; both corrected, and VIS-1 82-94, VIS-2 96-106, VIS-7 183-193 remain exact. The line convention is stated once and the denominator is re-derived for the current bytes rather than carried forward — and it is **true of those bytes**: 1,580 lines, 1,552 non-fence, 0 odd-backtick lines, 8 over 78 columns (see "conventions" below) |
| F20 | editorial | **REPAIRED** | All nine relationships read from the machine capture: the chain holds four edges (`materializes-as`, `changes`, `verified-by`, `satisfies-at-runtime`); the fifth Unknown relationship is `coverage-unknown`, capability → `region:unmapped-code`, off the chain. Corrected at both sites. The load-bearing part re-derives: entity signatures 5 `{basis,label}` + 4 `{label,reason}`, relationship signatures 4 + 5 |
| F21 | editorial | **REPAIRED** | `openspec/changes/` holds six directories; `archive/` holds only `README.md`; the exclusion is now stated and the conclusion holds |

Twenty-one of twenty-one repaired. No repair introduced an arithmetic
error, and no superseded wording was deleted rather than marked: every
stale phrase review 1 named (`disjoint from M9`, `Ten attribute`,
`ten-file`, `5,214`, `10,291`, `299 rendered`, the P-74 forecast, "no
independent review", "five edges", "seven of M9's ten", "provenance
2026-09-10 loopback daemon") occurs **only** inside a dated,
quotation-marked supersession note. [Observed, `grep -n -F` for each
string over the packet and the record; denominator both files whole]

## New findings

### G1 — non-blocking

`docs/evidence/polaris-m9-one-identity-funnel-2026-09-15.json`, keys
`file_bytes`, `file_digests_sha256`, `file_digests_note`.

**Defect.** Those three keys still carry the **first draft's** figures —
`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md` 93626 bytes, sha256
`ae0ec92c…` — and `file_digests_note` asserts of them, live and
unqualified, "These are this packet's OWN bytes". The packet at this
commit is **132428** bytes, sha256 `1b5e98a6…` (computed this session).
[Observed] Every other superseded value in this record carries a dated
marker: `captures_used.provenance` is marked `-- FALSE`,
`conventions_checked` carries a `superseded_2026_09_15` key,
`independent_review.note` and `not_verifiable_this_session` both mark
their predecessors. These three do not. The correct values are recorded
in the same file, in `review1.reviewed_packet_bytes` and
`reviewed_packet_sha256`, correctly labelled as review 1's subject at
commit `206d775` — so the record contains both the right answer and an
unmarked wrong one, and only the wrong one is presented as current.

This is the shape `AGENTS.md` records as its own lesson: a page-level
staleness notice does not discharge a specific false sentence, and
verification rule 10 turns on exactly which bytes a digest names.

**Repair.** Mark the two values as the first draft's, dated, and add the
current byte count and digest beside them — or say at the key that the
record cannot carry its own subject's post-repair digest and route the
reader to the `review1` block.

### G2 — non-blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:41` (Q1's third arm;
reached again by reference at `:43`, Q3's third arm).

**Defect.** An unmarked elision inside quotation marks, in the clause the
newly added arm rests on. The packet writes: *its home and gate are at
line 206: "A reviewed N/A judgment is a recorded owner judgment homed in
`decisions/` (RFC3-15), and the judgment is honored only through an
effective owner act under RFC3-16(a)".* Read at source, RFC2-26's
sentence continues: ", in state (1) or state (2), with that state
rendered; absent or invalid acts map nothing and leave the consequence
unmapped and Unknown, never covered (RFC3-16(a)'s effect rule; VIS-2)."
[Observed, `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`
lines 206-210]

This is exactly the class review 1 raised twice (F11, F17), reintroduced
by the F14 repair, and the dropped half is the cautionary half: it says
what happens when the act is absent or invalid, which is the risk an
owner weighing "a materially cheaper owner act" most needs in front of
them. The packet is not hiding it — the whole clause, both paragraphs, is
quoted verbatim in Gate 5 and I compared it word for word against the
source with no difference — but a reader of the question table alone sees
a truncated clause presented as complete.

**Repair.** Close the quotation with an ellipsis, or quote the sentence
whole, or cite Gate 5's blockquote at the site.

### G3 — non-blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:1240` and `:1489`; the
register blockquote; the record's
`review1.re_derived_before_applying.register_recount`.

**Defect.** Three places state, live and undated, that `m7wt` carries no
register row: "`m8wt` P-74, `m7wt` none beyond P-53" (1240), "M7 carries
no row yet" (1489), "and M7 carries no register row yet" (blockquote),
"m7wt none beyond P-53" (record). All four are false today: `m7wt` at
`1803608` — subject "docs: M7 funnel review 1 retained, F1-F12
dispositioned, P-76 registered" — carries **P-76**, its register holding
27 rows ending at P-76. [Observed, `^\| P-` over each of the nine
registers this session; denominator all nine worktrees]

The collision tables in the same packet each name the head they were read
at, which is what makes them re-derivable; the register recount names
none, so it cannot be dated by a reader and quietly went stale. This is
review 1's F16 finding one level up: F16 was about forecasting a literal
number, and the repair correctly stopped forecasting — but then made an
undated present-tense claim about a moving sibling instead.

M9's own assignment is **unaffected and correct**: M7 took P-76, not
P-75, so P-75 remains M9's and is consistent in all nine places the sweep
`P-7[4-9]` finds it. No recommendation moves.

**Repair.** Name the head each register was counted at, as the collision
tables already do, and say that a sibling row may land at any time.

### G4 — non-blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:46` (Q6).

**Defect.** Q6's own affirmative limb has no arm. The question is "**Do
slices 1 and 2 need an owner direction naming them?**" Its recommended
answer is "No — they trace to recorded review findings". Its second
lawful arm is "treat the pursuit as cycle *n*'s review, report it, and
land slices 1 and 2 as cycle *n*'s repairs after that report" — which
answers a different question (is the pursuit a continuation or a new
cycle?) and still lands the slices under the existing direction. The
lawful arm that answers the question as asked — the owner writes a
direction naming slices 1 and 2, which moots the trace-to-findings
reading entirely and is cheaper than a cycle report — is named nowhere.

The packet says at line 35-37 that Q6 "is the only one that could stop
slices 1 and 2"; on the unnamed arm a "yes" does not stop them at all, it
authorizes them directly. The owner is therefore shown a binary where
the cheapest affirmative route is absent.

Review 1 read this the other way ("Yes. Two arms plus a default"). I
record the disagreement rather than resolve it: the arm is lawful, the
owner may always issue a direction, and naming it costs one sentence.

**Repair.** Add "the owner issues a direction naming slices 1 and 2" as a
third arm of Q6, and say what it moots.

### G5 — editorial

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:3-15` (the head banner).

**Defect.** The F6 repair leaves a sentence fragment. At `206d775` the
banner read "...move M9 of the 2026-09-13 vision pursuit
(`docs/pursuits/2026-09-13-vision-pursuit.md`), **written in the shape
of** `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md` and its siblings."
[Observed, `git show 206d775:<path>`] The repair replaced the
parenthetical with four sentences ending in a bracketed correction note
and a full stop, so line 11 now begins "written in the shape of..." as an
orphaned lower-case clause with no subject or verb before it.

The substance of the F6 repair is right and I confirm it; only the
sentence it was spliced into is broken. Worth fixing because VIS-3's bar
is a fresh reader's comprehension and this is the packet's first
paragraph.

**Repair.** Re-join the clause, e.g. "This packet is written in the shape
of `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md` and its siblings."

### G6 — editorial

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:533-534`.

**Defect.** A quotation inside quotation marks that is not verbatim. The
packet writes: **The machine records' 14,804 is 16 bytes low and their
"~12 KB recovered, 2.8% of the P-63 trim" overstates the saving**. The
bytes at `docs/pursuits/2026-09-13-vision-pursuit-data.json` line 4956
(and the `-harvest.json` twin at 4548) read: "Be honest about the size:
**this recovers ~12 KB, 2.8% of the P-63 trim**, so it is a coherence
move that happens to help, not the ceiling answer." [Observed] The verb
is changed and the phrase reordered, with no elision mark. The substance
is untouched and the 14,804/14,820 arithmetic is exact (16 bytes).

F6 corrected this string's *attribution* and did not touch its *wording*,
so the slip survived the repair pass.

**Repair.** Quote the record's own words, or paraphrase outside
quotation marks.

### G7 — editorial

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:497-498`.

**Defect.** The headline sentence names no anchor for its interval:
"**The 618,515-byte headroom is one evaluation's figure, and the same
page breached the ceiling on a different Butlers revision three days
later.**" Three days later than the 2026-09-10 loopback observation in
the row above — that reading is correct. But the sentence's own first
clause is about the lane-A evaluation that produced 618,515, and relative
to *that* the breach was about eleven hours **earlier**, on the same
calendar day: the breach body is as-of `2026-09-13T02:03:33.040Z`, the
lane-A capture is as-of `2026-09-13T13:33:24.295Z` at Butlers `2e3bac9`,
and the lane-A trim commit `2ef68f5` is dated 2026-09-13 21:29 +0800.
[Observed, all four read this session]

Read naturally the sentence suggests the page breached *after* the trim
bought the headroom. The next sentence repairs the impression ("The
lane-A trim is what bought the 618,515"), so nothing downstream is
wrong — but the framing sentence is the one a skimming owner reads.

**Repair.** "...breached the ceiling three days after that 2026-09-10
observation, on the revision the lane-A trim then superseded."

### G8 — editorial

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:1515` (funnel summary).

**Defect.** An off-by-one against the packet's own stated convention. The
summary cites the improvement-cycles direction's second limb as
"(\"or to a recorded review finding\", line 56)". Read at source, line 55
is "Improvement-cycle work must trace to POC-REQ-001..061 or to a
recorded" and line 56 is "review finding." — so the quoted text *begins*
at line 55. [Observed] The packet's convention, stated once at lines
27-30, is "the line on which the cited text *begins*"; Gate 3's act table
cites the same clause correctly as "lines 55-56". This is the F15 class
in the one section review 1 did not line-check.

**Repair.** "lines 55-56", as Gate 3 already has it.

### G9 — editorial

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:1518` and `:1529-1530`.

**Defect.** An aggregate that does not follow from the packet's own
stated bounds. Both the funnel summary's handoff line and the Recommended
handoff section say slices 1, 2 and 6a "cost under 15 KB". The packet's
own per-slice upper bounds are: slice 1 "Under 2 KB on the largest page"
(line 739); slice 2 "Roughly 500 bytes across four pages" (748); slice 6a
"about 12 KB" on Trajectory plus "under 1 KB" on Orrery (895-896). Those
sum to about **15.4 KB**, above 15 KB; the claim holds only on central
values (13 links at 60-75 bytes plus mount prefix ≈ 1.1 KB, 310 cards at
40 bytes = 12,400, nine Orrery rows ≈ 360 bytes, ≈ 14.4 KB). Gate 6
bullet 1 asserts that every count in the packet carries its predicate, so
an aggregate should say which of the two it is.

**Repair.** "about 15 KB", or state that the figure is the central
estimate and the stated upper bounds sum to 15.4 KB. Nothing downstream
changes: either figure is under 3% of the measured headroom.

### G10 — editorial

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:1408-1410` (Gate 6 bullet
12) and the record's `governance_check`.

**Defect.** "`scripts/check_governance.py` was run in this worktree
**after both files were written**" — this pass wrote three tracked files,
the packet, the evidence record and the P-75 register row. The
superseded forecast at line 1234 ("this packet writes two files and no
register row") is correctly marked; bullet 12's "both" was not updated
with it.

No substantive risk: I ran the check myself with all three files present
and the last line reads `32 OK, 20 WARN, 0 FAIL (52 checks)`, matching
the recorded line exactly.

**Repair.** "after all three files were written".

### G11 — editorial

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:1170-1172`.

**Defect.** "M6's sibling intersections were zero across the board; M9's
are not." — a substantive claim about another packet's own measurements,
carrying no epistemic label and no citation, in a packet whose
neighbouring sentences are all labelled and head-cited. I checked it and
it is **true**: M6's collision table in `m6wt` at `83c9f60` shows **0**
in the intersection column of all five sibling rows. [Observed]

**Repair.** Label it [Observed] and cite the sibling packet and head, as
the question-level collision table beneath it already does.

## Measurements re-derived this session

Independently recomputed, not read from the packet. "exact" means every
digit matched.

| Claim | Re-derived? | My figure |
|---|---|---|
| Epistemic census over **both** `api-poc.json` files | yes | 1,167 / 1,137 / 30 / 18; sigs 1,137 + 12 + 9 + 9; Observed 1,146, Unknown 21, Inferred 0; tier `report-fact` 1,137 and 0 of five; fresh 1,149 and 0 of three; unchallenged 1,149; `excluded-content` 12 and 0 of eleven — identical in both files |
| Capture provenance, five files | yes | `polaris-7478.html` 66ed58f / a121591 / 2026-09-10T01:50:48.470Z; `home.html` and `api-poc.json` 7c8743f / f4589e2 / 2026-09-13T02:03:33.040Z; `trajectory-7478.html` and `orrery-7478.html` carry no snapshot label, observer or timestamp at all |
| Private daemon, run script and log | yes | `--port 0 --state-dir`, `127.0.0.1:41215`, observed revision `7c8743f6…`; the run wrote `home.html`, `api-poc.json`, un-suffixed `trajectory.html`/`orrery.html`, and an 838-byte breach body for Polaris |
| Attribute-name union | yes | **11**; per page 3 / 8 / 2 / 0; names exactly as tabled |
| RFC1-25: 26 data rows, 30 tokens; intersection | yes | header 494, separator 495, rows 496-521 = 26; 30 tokens; **{`contains`}**, 1 of 8 |
| Set difference against the enumeration | yes | 25 entries / 26 tokens at data line 4360; omitted `calls`, `exposes`, `accesses(mode)`, `succeeds` |
| Href census over the four captures | yes | 40 / 1,061 / 315 / 23 = **1,439**; fragments 1,051; source routes 372; surface roots **16** (one `site-nav` per page, 4 hrefs in each); claim-level cross-surface **0**; post-lane-A Polaris 1,089 and still 0 |
| `data-claim-id` | yes | 699/689 and 713/703 on the two Polaris captures, 0 on the other three, 0 values naming an entity id; both excesses exactly 10 |
| Three-state word sweep | yes | desired 1, observed state 1, execution state 0, three-state 0 |
| Headroom arithmetic | yes | 2,097,152 − 1,478,637 = **618,515**; − 1,484,487 = **612,665**; registry `maxHumanResponseBytes` 2097152 at line 270 |
| Claim-tuple spans | yes | **713** spans, **418,122** bytes, mean **586.4**, min 559, max 661, **28.28%** of the page |
| Ribbon arithmetic | yes | 618,515 / 415 = 1,490; 3 × 586 = 1,758 → 1,758 × 415 = **729,570 > 618,515**, does not fit; 300 × 415 = 124,500, does |
| Reality band, four parts, both captures | yes | 14,820 / 2,130 / 1,534 (905 inner) / 4,309 / 5,680 (5,077 inner ul); recoveries **5,843** and **11,523**; 9 × 586.4 = 5,278; net +565 to +6,245 |
| Ceiling rows | yes | 2,090,025 (7,127 under); breach 2,132,656 vs 2,097,152 (over by 35,504); 254,168; 37,048; 38,706; 5,520,314 vs 8,388,608 |
| `wi-card` on the named capture | yes | **310** (299 on the unnamed one) |
| Collision rows, eight siblings, predicate A and B | yes | M1 1/1/0/0, M2 11/4/7/4, M3 13/4/9/2, M4 22/9/13/8, M5 9/3/5/3, M6 13/0/9/0, lane B 1/0/—/0; M7 11/1 at both `0c4b4a9` and `1803608`; M8 20/7 at `4b2e8cb`, 19/6 at `8035c8f` |
| M2 names `polaris.ts` | yes | **0** occurrences |
| Lane B manifest | yes | 11 rows naming the PWB change, **0** three-surface paths, and "All rows take effect together or none do" verbatim; no row and no digest reproduced here |
| Mutation-record digests | yes | both `subjects` rows of the 2026-09-04 record differ from their files' current bytes (computed, neither value reproduced); the two 2026-09-05 records name `model.ts` and carry no `subjects` block |
| `Inferred` sweep | yes | 0 of 27, 2 of 45, 2 of 21 non-test modules (recursive `.ts`, `.test.ts` excluded); sites `polaris-copy.ts` 35 and 41, `epistemic.ts` 36, `vocabulary.ts` 65 |
| Spec population | yes | 24 `^### Requirement:`, 24 `^#### Scenario:`, ids POC-REQ-001…061; `Inferred` occurs **0** times in the spec |
| `openspec/changes/` | yes | six directories; `archive/` holds only `README.md` |
| Register partition | yes | `m9wt` 22 open + 5 acceptance-act = **27**; `a9f671e` 21 + 5 = 26; predicate `^\| P-` partitioned by the `##` section each row falls under |
| Register rows across nine worktrees | **no** | P-68…P-75 as stated, but `m7wt` now carries **P-76** (G3) |
| `check_governance.py` | yes | `32 OK, 20 WARN, 0 FAIL (52 checks)` |
| Packet conventions on current bytes | yes | 1,580 lines; 1,552 non-fence; 0 odd-backtick; **8** over 78 columns (the title, four `###` slice headings, three code-span paths at 436, 800, 977); **295** distinct spans, **68** slash-bearing, **22** non-resolving, and the 22 are exactly the 22 enumerated |

## Clause quotations checked at source (rule 8)

Every clause the packet quotes was opened at its cited path and line. All
exact except G2's truncation and G6's paraphrase: VIS-1 (82-94), VIS-2
(96-106), VIS-3 (108-120), VIS-4 (122-139), VIS-7 (183-193);
`trust-and-evidence.md` 16; RFC1-25 (RFC-0001:463) and its table;
RFC1-26 (636-642); RFC2-26 — the whole clause, both paragraphs, compared
word for word against lines 196-221 with **no difference**, its heading
at 194, route at 201, home and gate at 206, scope sentence at 219;
POC-REQ-031 (537), POC-REQ-052 (851, text 855, scenario 872-877),
POC-REQ-053 (890, text 894, **oracle 903-904**, scenario 910-914),
POC-REQ-060 (927, text 931-934, scenario 948-953), POC-REQ-061 (972-973);
PWB Purpose (5), the nine declared-item classes (15-26), PWB-REQ-007
(439, text 443, scenario 470-474 including its AND limb);
`CONTRACT-COVERAGE.md` 3, 7-8, 89, Part B2 heading 232, preamble 238-241,
RFC6-1 358, RFC6-3 360, **RFC6-12 369**, RFC6-24 371; the sign-off act
32-34, 39, table 42-49, `tasks.md` exclusion 51-53; the project-wide act
31 and table 34-46; the PWB implementation act 76, 78-79, triggers 88-94,
93; the continuation act 110 and 112-113; the improvement-cycles
direction 34, 36, 41, 46-54, 50, 55-56; CC-SPEC-8 at
`SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` 229 per
`DIRECTIVE-REGISTER.md` 129; `PROJECT-STATUS.md` 147. Source lines also
confirmed: `model.ts` 44-46, 64-73, 76, 82, 86, 90-96;
`project-shape-model.ts` 120-131, 142-148, 184, 188; `epistemic.ts` 36
and 50-67 with the Inferred label at 52; `vocabulary.ts` 65 with its
comment at 63-64; `polaris-copy.ts` 35 and 41; `page-shell.ts` 20 and 23;
`exact-tables.ts` 28 and 41; `routes.ts` 80; `polaris.ts` 255, 276, 1173;
`trajectory.ts` 136 and 192; `orrery.ts` 157;
`polaris-reachability.test.ts` 101 and 189; `surface-routes.test.ts` 38
and 123; `cross-cutting.test.ts` 4-9. [Observed]

## The register

| Question | Finding |
|---|---|
| Is the P-75 row a faithful one-line rendering of Q1-Q6 **after** the repairs? | **Yes.** Each of the six carries its recommendation, its second arm and its default verbatim in substance; Q1 and Q3 both carry the **third** arm added by the F14 repair, with Q1's per-slice reachability reading labelled [Inferred] and Q3's stated as arguable; Q4 appears in its **recast** form ("if and when an agent asserts something") with the no-act-on-the-recommended-arm point; Q5's order is the packet's order; Q6 carries the M8 Q7 overlap and says the packet re-asks nothing. The evidence preamble's figures (eleven attribute names, 0 of 1,439, 1,167/1,137/30/18, 1 of 8 against 30 tokens) all match the repaired packet and re-derive above |
| Does the blockquote's verdict word and counts match the raw exactly? | **Yes.** "verdict copied exactly: **REVISE**" — the raw's last line is `Verdict: REVISE`. "2 blocking, 16 non-blocking, 3 editorial, F1–F21": counted over the raw's own severity headings, F1-F2 blocking (2), F3-F18 non-blocking (16), F19-F21 editorial (3), total 21 [Observed] |
| Is the recount reproducible by a stated predicate? | **Yes.** The stated predicate is "`^\| P-` partitioned by the `##` section each row falls under, run against both trees". Run this session: `m9wt` gives 22 under "Open, and only the owner can dispose" and 5 under "The acceptance acts", 27 in all; `a9f671e` gives 21 and 5, 26 in all. Exact |
| Does it correctly state that P-68…P-74 live only on their own branches? | **Partly.** P-68…P-74 are each on exactly one branch and nowhere else, confirmed across nine registers. The trailing clause "and M7 carries no register row yet" is false today — `m7wt` at `1803608` carries **P-76** (G3) |
| Does the row quote a digest or backtick an observed-repository path? | **No** to both. No sha256, no truncated digest, no manifest row, no act argument; the three digest-bearing records it depends on are cited by path. No observed-repository path appears in a code span anywhere in the row, the packet or the record — `check_governance.py` ends `0 FAIL`, CG-1b included |

## The six questions

| # | Scope truthful? | Genuine human gate? | Recommendation follows? | All lawful arms named? |
|---|---|---|---|---|
| Q1 | **Yes.** The two specifications are separately signed and separately digest-bound and both limiting sentences are verbatim at their lines; lane B's manifest does occupy the PWB side, with 11 PWB rows, 0 three-surface rows and its all-or-none sentence, read read-only | **Yes.** Only the owner may sign a CC-REV-2 delta (VIS-4); which specification it binds is not an engineering choice | **Yes**, and unchanged by the repair. The counter-argument is still stated as real and still argues against the recommendation | **Yes now** — the RFC2-26 reviewed-N/A arm is added with per-slice reachability, closing review 1's gap; subject to G2, which truncates the clause it rests on |
| Q2 | **Yes.** The nine declared-item classes really do exclude every kind the POC's nine entities carry; the 18-of-1,167 breach figure re-derives over both machine captures | **Yes.** A requirement's scope is the owner's to read, and the answer moves slice 4 between enhancement and repair owed | **Yes.** And the uncomfortable end is still followed: "the served payload is in breach today… a disclosure owed" | **Yes.** Two arms plus a stated default |
| Q3 | **Yes.** Line 89's mapping is verbatim as quoted and POC-REQ-052's text really is anti-fabrication, not vocabulary closure; the 1-of-8 intersection against 30 tokens re-derives | **Yes.** Whether RFC1-26 reaches a bounded POC's local rendering vocabulary is a contract reading | **Yes**, including the part that cannot be repaired: the signed row stands and the successor reading goes in the amendment's own coverage | **Yes now** — the N/A arm is added for slice 8 and honestly marked arguable rather than asserted, because the kinds are rendered |
| Q4 | **Yes now.** The recast question matches what the packet's own act table says is gated; the measurement was always exact and re-derives | **Yes, on the constructible limb** — and the packet now says so in the cell rather than leaving the reader to find it in Gate 3 | **Yes.** The recommendation is unchanged and the counter-argument ("dead code with a test suite") still carries full weight | **Yes.** Two arms plus a default |
| Q5 | **Yes now.** Every ceiling row names its daemon and evaluation, both omitted pre-lane-A observations are present, and the headroom is called one evaluation's figure; subject to G7's anchor | **Borderline**, as review 1 read it: allocation order is engineering, but the trade-off against a margin the Butlers repairs are counting on is genuinely the owner's | **Yes.** VIS-1's ordering is applied correctly and the "does not fit" arithmetic re-derives to the byte | **Yes.** Two arms plus a default |
| Q6 | **Yes.** The 24/24 sweep is exact, both limbs of the direction are now cited to their own lines, and the M8 Q7 overlap is disclosed without re-asking it | **Yes.** Whether the pursuit is a continuation or a new cycle is the owner's reading of their own direction | **Yes** for the two arms it names | **No** — the question's own affirmative limb, an owner direction naming slices 1 and 2, is not offered as an arm (G4) |

**Defaults.** All six still state a default-if-unanswered; all six are
conservative (hold the slice, draft no delta, land nothing byte-adding);
none authorizes anything, and none moved in this pass. No lawful arm is
called unlawful anywhere. **No owner trade-off is smoothed**: the two
counter-arguments that cut against the packet's own recommendations —
Q2's breach disclosure and Q5's earmarked margin — survive the repair
pass intact and are if anything sharper, because the ceiling table now
shows the same page both fitting with 7,127 bytes to spare and serving
nothing at all on two different Butlers revisions.

## What I checked and found sound

- **Marked, never deleted.** Every superseded figure, quotation and
  sentence review 1 named is kept in place, dated, inside quotation
  marks, with the finding number that retired it. I swept for all eleven
  stale phrases the brief lists and found no live occurrence of any.
  The one class of exception is G1, in the record, where two superseded
  values carry no marker at all.
- **The record's corrections are appended, not substituted.**
  `captures_used.four_page_capture.provenance` still carries the false
  sentence with `-- FALSE` appended and the corrected per-file keys sit
  beside it; `conventions_checked` keeps the first draft's 1,206 / 2 /
  233 / 58 / 19 under an explicit "true of the FIRST DRAFT at commit
  206d775" note.
- **Nothing digest-bound is proposed for edit.** Gate 3's eleven
  implementation files and four test files intersect neither the six
  signed three-surface artifacts nor the eleven signed PWB artifacts;
  the intersection is empty by construction (all seventeen live under
  `openspec/`). Slice 3 is an amendment package by construction. No
  manifest row and no truncated signed digest is reproduced in the
  packet, the record, the register row, or this review.
- **The self-referential convention figures are true of the bytes that
  carry them** — the point where a claim of this shape usually fails.
  1,580 lines, 1,552 non-fence, 0 odd-backtick lines, 8 over 78 columns,
  and the packet's identification of those 8 (title, four `###` slice
  headings, three unbreakable code-span paths) is exactly right;
  295 / 68 / 22 code spans, and the 22 non-resolving spans I enumerate
  independently are precisely the 22 the packet lists, none of them a
  path to a file that should exist in this worktree.
- **The question-level collision table is honest in both directions.** I
  read M3 Q1, M2 Q1, M2 Q6 and M8 Q7 at source. Each rendering is
  faithful; none is re-asked; none is ruled; and the M8 Q7 / M9 Q6
  sequencing proposal is labelled [Inferred] and explicitly says M8's
  question stands as its own row on its own branch.
- **The disjointness repair went further than the finding.** Review 1
  measured M8 at 6 shared files; the packet measured 7 at M8's newer head
  and disclosed that the collision **grew**. Both figures re-derive, and
  reporting the worse one is the right instinct.
- **The census mitigation is real, not rhetorical.** The whole epistemic
  census agrees cell for cell over two captures three days and two
  Butlers revisions apart. The packet says so and says which figures
  still mix evaluations.

## Closing note

The repair pass is unusually complete: twenty-one of twenty-one findings
repaired, every one of them re-derivable at source, no arithmetic moved
except where a finding required it, and both recommendations the review
pressed hardest (Q1's and Q4's) held their ground while gaining the arm
and the framing they were missing. The eleven findings above are all
second-order: one stale digest pair in the record (G1), one truncated
clause introduced by a repair (G2), one undated claim about a sibling
that moved under it (G3), one unnamed arm (G4), and seven smaller things.
None changes a recommendation, a default, or a figure an owner would act
on.

Verification rule 10 applies: this review is bound to the four files at
the digests above. Any edit retires it.

Verdict: CONFIRM WITH EXCEPTIONS
