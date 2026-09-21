# R-POLARIS-M5-AGENT-BRIEFING-FUNNEL — review 3 (raw, retained verbatim)

Independent fresh-context review. Read-only: no file in any repo or
worktree was edited, no state-changing git command was run, no `bd`
write, no daemon, no network, no Butlers checkout read. The only file
written is this one.

## Subject and digests

Worktree: `/tmp/claude-1000/-home-tze-GitHub-syzygy/6b8e9d74-3b46-4418-b725-5b74d21d660a/scratchpad/m5wt`
Branch `agent/syzygy-dov.5`, HEAD **`09b5395a5c01033f2c229aa7e0498d0b662e4081`**
("docs: M5 funnel review 2 retained, G1–G12 repaired, P-72 row aligned
[syzygy-dov.5]", 2026-09-15T00:15:24+08:00). `git status --porcelain`
is empty [Observed].

Bytes and sha256 computed this session with `wc -c` and `sha256sum`,
never transcribed:

| File | Bytes | sha256 |
|---|---:|---|
| `docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md` | 103078 | `2ec2413af47f2c208c131dbfb9173aa16c8a3328ed70d66501031e914756cab1` |
| `docs/evidence/polaris-m5-agent-briefing-funnel-2026-09-14.json` | 26130 | `283b23576fdd696dd8d5efa2bd89d5dae9c99750b78655eb920e94e144c499e6` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 28297 | `101f2b19fc696e97fc4b0174c3fb1a849fbba43751b76f99f2b5baebd0d15a4b` |
| `docs/reviews/R-POLARIS-M5-AGENT-BRIEFING-FUNNEL-RAW.md` (review 1) | 34023 | `73b1596137fe2e02f5d6af781e896b33296d8871059715f582cafcb7f14b3aed` |
| `docs/reviews/R-POLARIS-M5-AGENT-BRIEFING-FUNNEL-2-RAW.md` (review 2) | 41872 | `861cece7952ee7c7a943abfa104a6ae24ba69a96714ea000b342f262b932d6a4` |

The packet's review-1 and review-2 sections quote the raws' digests and
the reviewed bytes at `1afa3d0` and `bf3999d`. The two raw digests above
match the review sections exactly, and all three `bf3999d` figures
re-derive exactly from `git cat-file` (packet 90597 /
`6d248dea1d428c72078622a1e369aad7f051a215dd2e3aeb4cef57e97b83ffa6`;
record 21576 / `e8503cf8ab1072c86f82405bd1aeb7e87d4be04a5aded96ecb80bc0727ef2410`;
register 27485 / `c4552371e4305b6d754788d1375d30ab2e09a7b5672ffe90582405afcb157619`)
[Observed]. Verification rule 10 is handled correctly: review 2 binds the
`bf3999d` bytes, this review binds the `09b5395` bytes named above, and
this raw is a third `-RAW.md`, never an overwrite.

Capture: `scratchpad/m1/measure/after/api-poc.json`, 5,520,314 bytes,
sha256 `a89b0e059b5fdadc5f359c2bee58115cd50747399cfb00444703e0fafdfb466e`
— present at the session scratchpad path the packet names, size and
digest recomputed this session and matching [Observed].

## Method

Everything below was re-derived at `09b5395` from source, the two signed
specifications, the doctrine and RFC files, `DIRECTIVE-REGISTER.md`, the
retained capture, and `git show f35a25f:…` for M3. No disposition row was
taken on trust. Byte figures are Python `json.dumps` with
`separators=(',',':')`; literal counts are `str.count` over the decoded
text and `bytes.count` over the raw file, run twice and agreeing. Line
numbers are `awk`/`grep -n` over declaration and closing-brace lines.
`grep -F` or Python `re` for anything load-bearing (rule 1).

## Findings

### H1 — blocking — Q3's "one new field" lands on a type shared by every bounded sink, so a briefing-specific sentence would be served on human-HTML and `/api/poc` breaches, and the no-gate warrant never considers the two sinks PWB-REQ-006 does govern

`docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md:60-73` and `:893-900`;
`apps/three-surface-poc/src/routes.ts:113-124, 132-142, 151, 161, 175`.

**Defect.** Q3 decides to "add **one new field** to that interface
carrying the sentence 'population describes the whole evaluation, not
this briefing's subject' — the breach body is `JSON.stringify` of exactly
that interface (`routes.ts` line 141), so a sentence cannot reach the
body without widening the type" (`:63-67`), and the slice-3 text repeats
it as scoped to "a briefing-ceiling breach" (`:893-897`).

`ResponseLimitFailure` is not the briefing's type. It is the single
failure envelope every bounded sink serves [Observed, re-derived this
session]: `responseLimitFailure(model, limit, declared, observed)` is
built once at `routes.ts:132-134`, `boundedResponse` serializes exactly
that object for whichever `ResponseLimitIdentity` it was passed
(`:137-142`, the `JSON.stringify` at `:141`), and its call sites today are
`html()` at `:151` (`maxHumanResponseBytes`, the Polaris/Trajectory/Orrery
pages), `machineHandle` at `:161` (`maxMachineResponseBytes`, `/api/poc`)
and `presentationHandle` at `:175` (`maxMachineResponseBytes`,
`/api/poc/polaris`). A required new field on that interface therefore
appears on every one of them. On a human-HTML breach of
`maxHumanResponseBytes` the served body would carry the sentence "…not
this briefing's subject" on a response that has no briefing and no
subject — a fabricated context stated as fact, on the one artifact
AGENTS.md records as the sole trace of a ceiling breach ("a
response-ceiling breach serves nothing and logs nothing… the 503 body of
the breaching request is the only trace"), which the packet itself quotes
at `:90-95` as the reason the sentence is worth having.

That is also where the no-gate warrant thins. Q3 argues it is not an
owner gate because "the type is an implementation type in
`apps/three-surface-poc/src/routes.ts` bound by no act" (`:68-70`). The
type is indeed bound by no act; the *bodies* it produces for two of the
three sinks are the breach envelope PWB-REQ-006 enumerates ("A final-output
breach SHALL return only a bounded typed failure envelope carrying
evaluation identity, limit identity, declared value, observed value and
population counts", spec `:381-384`, quoted correctly by the packet at
`:528-533`), and PWB-REQ-006's Case sweeps "both final-output sinks". The
packet's [Inferred] reading of "only" as a minimum is defensible and is
disclosed with the owner's contrary reading routed back to the funnel —
but the reading is applied only to the briefing sink, and the two sinks
the requirement names are never mentioned in Q3 at all. A decision the
packet removed from the owner's table rests on a scope claim that does
not hold on the current bytes.

This is not the same defect G6 found. G6 established that the sentence is
a type widening rather than a reuse "unchanged", and the packet repaired
that. What is still missing is *which* responses the widened type reaches.

**Repair.** Either (a) make the sentence limit-scoped — a field whose
value is derived from the `ResponseLimitIdentity` being served, so each
sink states what its own `population` counts describe, with the briefing
wording used only for the briefing identity; or (b) word the field
limit-neutrally ("population counts describe the whole evaluation") so it
is true on all three sinks. Either way, state in Q3 that the widened type
is shared with the two PWB-REQ-006 sinks and re-run the no-gate argument
over them, or move the question to the owner's table.

### H2 — non-blocking — "slice 3 adds a third final-output sink" counts routes where PWB-REQ-006 counts kinds, and Q2's premise turns on which

`docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md:534-537`; Q2 at `:56`;
handoff at `:1313-1317`; spec `:378-384`.

**Defect.** Gate 2 reads PWB-REQ-006 and concludes "slice 3 adds a third
final-output sink, Q2 proposes a third declared ceiling for it" (`:536`),
and Q2 asks the owner whether "a third ceiling amend[s] PWB-REQ-006's
two-sink wording". The clause's own words are "Final encoded human HTML
and machine JSON SHALL each have an explicit byte ceiling" (spec `:378-379`)
— two **kinds** of encoded output, not two routes. On the current
implementation there are already three bounded routes served under two
ceiling identities: the human pages under `maxHumanResponseBytes`
(`routes.ts:151`) and both `/api/poc` and `/api/poc/polaris` under
`maxMachineResponseBytes` (`:161`, `:175`) [Observed]. `/api/poc/briefing`
would be a fourth route and a third machine-JSON body, not a third kind
of sink.

The distinction is load-bearing for the question actually put to the
owner. If the two sinks are kinds, a briefing needs no third ceiling to
satisfy PWB-REQ-006 at all — minting `maxBriefingResponseBytes` becomes a
discretionary tightening (which is a good reason to do it, and the
packet's own "8 MiB with nothing to stop it" argument survives intact),
and the fold-in question in Q2 ("does a third ceiling amend
PWB-REQ-006's 'each'?") largely dissolves. If they are routes, the clause
is already stretched today by `/api/poc/polaris` and Q1's retroactive-
coverage recommendation gains a second, independent argument the packet
never makes. Neither reading is stated; the packet asserts the route
reading without labelling it.

**Repair.** State the kind-versus-route reading explicitly, label it
[Inferred], and say which of the two Q2's fold-in sub-question depends on.
Note in Q1 that `/api/poc/polaris` is already a second machine-JSON body
under the same ceiling.

### H3 — non-blocking — the per-key byte table's published method does not reproduce its own Share column

`docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md:323-352`.

**Defect.** The heading states the method as "compact re-serialization,
method: `json.dumps(v, separators=(",", ":"))` per key, summed against the
whole file's own compact size", and the prose below names that size:
"the whole file's own compact serialization, 5,521,960 bytes" (`:349-350`).

Every **byte** value in the table reproduces exactly under that method,
and so does the 312-byte gap [Observed, re-derived this session: sum
5,521,648 against whole 5,521,960]. The **Share** column does not. Two
rows are off in the last published digit: `workItems` 2,273,467 /
5,521,960 = 41.17%, published 41.18%; `codeStructure` 1,493,219 /
5,521,960 = 27.04%, published 27.05%. Both come back exactly when the
denominator is the *file's byte length*, 5,520,314 (41.18%, 27.05%,
30.02%, 1.45%) — a different number from the one the heading and prose
name, because `ensure_ascii` defaults to escaping non-ASCII while the
served file carries it as UTF-8.

Immaterial to every argument resting on it (the 68.2% and 0.339% figures
are unchanged to their published precision at either denominator, both
verified this session). It is a stated method that does not re-derive two
published values — the same class of defect G5 raised about the one-claim
totals, in the table immediately above them.

**Repair.** Name the denominator the Share column actually uses
(5,520,314, the file's own bytes), or recompute the column against
5,521,960 and publish 41.17% / 27.04%. Say once whether `ensure_ascii` is
on; the evidence record already carries `whole_file_compact_bytes`
5,521,960 alongside `bytes` 5,520,314, so both numbers exist and only the
prose picks the wrong one.

### H4 — non-blocking — the evidence record still carries G4's withdrawn `authorityLine` value in two places, as re-derived fact

`docs/evidence/polaris-m5-agent-briefing-funnel-2026-09-14.json`,
`line_numbers_reverified_at_a9f671e.citations["polaris.ts authorityLine"].actual`
and `not_verifiable_this_session[2]`.

**Defect.** G4 found the `authorityLine` row wrong and the packet repaired
it: the function opens at `polaris.ts:707` and closes at `:716` (`:713`
ends on a `.map(` continuation) [Observed, re-derived this session by
reading to the closing brace]. The packet's line table and both Collision
cites now say 707–716 (`:452`, `:1076`, `:1104`).

The evidence record does not. Its `line_numbers_reverified_at_a9f671e`
block still records `"actual": "707-713"` for that citation, under a
`note` asserting that "After review 1 (F5, F22) every row was re-derived
by grep over declaration and closing-brace lines" — so the record states
the wrong value with the strongest provenance claim in the file. The
third `not_verifiable_this_session` entry repeats it: "slice 2's edit site
authorityLine 707-713 is outside all five". `707-713` occurs twice in the
record and zero times in the packet [Observed, `grep -c`].

The record is the packet's own mechanical sidecar; a reader who checks the
packet's table against it finds a disagreement with no withdrawal marker
on either side. Everywhere else in this record a superseded figure is
marked in place and dated (the `rendered_packet_fields` and Q3 strings
both carry `[superseded 2026-09-15 …]`), so the convention exists and was
simply not applied here.

**Repair.** Correct both to 707–716, keeping the withdrawn value marked
and dated in place, in the same shape the record already uses twice.

### H5 — non-blocking — the record's briefing-set totals are still presented unqualified; G5's floors disclosure lives only in the review-2 block

`docs/evidence/polaris-m5-agent-briefing-funnel-2026-09-14.json`,
`agent_briefing_sets.one_claim_briefing_examples` versus
`review2.re_derived_before_applying.one_claim_components_bytes`.

**Defect.** G5's disposition claims "the record carries the components and
the unpublished-wrapper disclosure". Half of that is true. The components
are in the record, and all ten reproduce to the byte this session
[Observed, recomputed from the capture by the published field paths:
`evaluation` 595, `projectShape.identity.scope` 109,
`projectShape.authority` 1,369, item records 661 (its `claim` sub-object
504) and 812, chain records 1,075 / 844 / 326, source records 1,627 and
1,803; the with-source deltas 7,076 − 5,449 and 5,150 − 3,347 equal the
two source records exactly]. But they sit under `review2`, a block about
the review, while `agent_briefing_sets.one_claim_briefing_examples` — the
block a reader goes to for the measurement — still publishes
`bytes_without_source` 5449 / 3347 and `bytes_with_source` 7076 / 5150
with a `note` that names only the 27-byte placeholder href as the reason
each is a floor. The composed wrapper, which is the actual 439/462-byte
remainder G5 measured, is not disclosed at that site, and the totals read
as re-derivable from the `composition_fields` listed right above them.

The packet itself does this correctly (`:377-391`: "Every component
reproduces to the byte; the totals do not", with the components enumerated
and the wrapper named as unpublished).

**Repair.** Carry the floors-and-unpublished-wrapper sentence into
`one_claim_briefing_examples` itself, or point that block at the component
table, so the record's measurement section and the packet say the same
thing.

### H6 — editorial — the F20/G12 disposition is false on the current bytes, and the G12(a) repair made the line it fixed worse

`docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md:1424` (the F20 row);
`:27-28`, `:141`, `:272`, `:899`, `:969`.

**Defect.** The F20 row now reads: "nine of the remaining ten over-width
lines are single unbreakable paths or headings, as the review allows; the
tenth, ordinary prose at 80 columns, was found by review 2 (G12) and
wrapped."

Predicate, stated so it can be re-run: lines longer than 78 columns,
outside fenced code blocks, excluding lines whose stripped form begins
with `|` (table rows) or `#` (headings). Denominator: all 1,447 lines of
the file.

At `bf3999d` (what review 2 measured under this predicate): **7** such
lines — six single unbreakable paths, and `:27` at 80 columns, ordinary
prose. At `09b5395`: **11** — six paths (`:11`, `:514`, `:586`, `:613`,
`:763`, `:1011`) and **five** ordinary prose lines: `:28` (100), `:141`
(102), `:272` (97), `:899` (117), `:969` (85) [Observed, measured this
session].

The G12(a) repair split `:27` after "`polaris.ts`," instead of after the
comma review 2 named, turning one 80-column prose line into a 50-column
line and a **102**-column one (`:28`). The other four are reflow residue
from the G1, G2, G6 and G9 repairs themselves — `:899` at 117 columns is
the longest prose line in the file and was introduced by the G6 repair.
So the row's "wrapped" is wrong for the tenth line, and its "nine of ten
are unbreakable" is wrong for the population (five of eleven are
breakable prose).

Editorial: nothing turns on it. But AGENTS.md's own hard-wrap guidance
exists because a reflow that breaks a code span is invisible to every
citation sweep, and four of the five lines were created by this session's
repairs.

**Repair.** Re-wrap `:28`, `:141`, `:272`, `:899`, `:969` at 78 columns
without breaking a code span, then restate the F20 row with the count and
the predicate it was measured under.

### H7 — editorial — G2's disposition overstates what landed in the P-72 row

`docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md:1440` (G2 row);
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md:205`.

**Defect.** The G2 row says "Success criterion 2, the parity test, S4, the
summary, the F6 row and the P-72 row restated with both denominators".
Five of the six carry both (8 of 9 top-level fields **and** 9 of 11
leaves): `:265-274`, `:730-746`, `:1049-1053`, `:1270-1272`, `:1380`
[Observed]. The P-72 row carries one: "eight of its nine top-level fields
rendered there across seven cells, none on `/api/poc`" — the leaf
denominator is absent. A cell count is not the second denominator; that
conflation is what G2 was about.

**Repair.** Add "(9 of its 11 leaves)" to the P-72 row, or drop the P-72
row from the G2 disposition's list.

### H8 — editorial — "main's register still ends at P-67" is true of identifiers and false of rows

`docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md:1284-1286`;
`docs/evidence/…json`, `pending_register_state.main_at_a9f671e_last_row`.

**Defect.** Both say main's register "ends at P-67" / `"last_row": "P-67"`.
On `main` the open table's last row is **P-53**; P-54…P-67 were ruled and
are recorded only in the dated update notes above the table [Observed,
`git show main:…` this session]. The intended claim — P-67 is the highest
identifier allocated on main, so P-72 is lawfully next — is correct, but
a reader who checks the table finds a different number.

Not a count error elsewhere: the register's own "**22** open rows below
and **5** acceptance-act rows, **27** in all … counted from main's
21/5/26" re-derives exactly, once the `P-25(c)` row is included in the
denominator (a first sweep for `^\| P-<digits> \|` misses it and yields a
false 21/26 — rule 9) [Observed].

**Repair.** "main's register's highest allocated identifier is P-67 (its
last open row is P-53)", in both places.

### H9 — editorial — success criterion 4's zero-minting claim is scoped to four vocabularies the packet was never going to touch, while three new closed vocabularies go unnamed

`docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md:283-286`.

**Defect.** Criterion 4 is "Zero new epistemic or closed-vocabulary values
exist anywhere in the implementation that RFC2-10, RFC2-24, RFC2-25 or
PWB-REQ-004's closed population do not already carry." That holds, and I
confirmed it independently (see the closed-vocabulary check below). But
the three slices do mint three new closed vocabularies of their own: the
`dispatchState` discriminant (`'undispatched'` / `'dispatched'`, `:718-724`),
the `mayNot` row `id` space (`'no-write-to-observed-repository'` and five
siblings, `:751-757`), and the chain's `not-applicable` state (`:872-874`).
None is a value in the four vocabularies named, so the criterion cannot
see them. Gate 5 answers the minting question for the *fields*, and Gate 3
proposes registering the `mayNot` table's **row count** against the act's
bullet count — but not its id vocabulary, which is the part a later
amendment would silently desynchronize.

**Repair.** Either widen criterion 4 to "and every new closed vocabulary
this move introduces is enumerated, with its governing source and a
registration check", or add one sentence naming the three and saying where
each is closed.

## G1–G12 verification against the current bytes

Each row re-derived from source, not from the disposition.

| # | Claim the repair rests on | Re-derived this session | Status |
|---|---|---|---|
| G1 | PWB-REQ-013 is a presentation prohibition, not a type for the packet; `materializ` 0 in both signed specs | PWB-REQ-013 at spec `:723-740`, Group "Presentation", Form prohibition; the quoted words are `proposed-work.ts:8-19` header comment; `materializ` = 0 and 0 (`str.count`, case-insensitive too), over 17 PWB and 24 POC `### Requirement:` headings | **REPAIRED** — Gate 5 (`:947-971`) now answers slice 1 as the same minting question on the bound-by-no-act ground, labelled [Inferred], with the false attribution kept in a marked parenthetical; Gate 3's slice-1 row (`:665`) and the summary (`:1258-1260`) follow; Gate 2's PWB-REQ-013 paragraph still cites the comment as a comment |
| G2 | seven `<dd>` cells; 9 top-level fields, 11 leaves | `renderMaterializePanel` `materialize-action.ts:55-82`; seven `<dd>` at `:69-75`, `:74` carries `issueType` + `priority`; `MaterializationPacket` `materialization.ts:20-30` = 9 fields; leaves = 8 + 3 (`governingIntent`) = 11; rendered = 8 top-level, 9 leaves; machine-only = `targetBeadPrefix`, `governingIntent.designPath`, state `at`; status line `:61-62` = 1 of 2 state fields | **REPAIRED** in the packet (`:265-274`, `:730-746`, `:1049-1053`, `:1270-1272`, `:1380`); **PARTIAL** in the P-72 row — see H7 |
| G3 | `api/poc/polaris` absent from the specs; one occurrence in the corpus | 619 tracked files under `openspec/` and `.syzygy/` (`git ls-files -z`, counted); `grep -F` over all 619 returns exactly **1** hit, `PENDING-OWNER-DECISIONS.md:205`, the P-72 row; 0 in either signed spec | **REPAIRED** — Q1 (`:55`) states the claim over the specs and enumerates the register-row occurrence with the falsification disclosed |
| G4 | `authorityLine` closes at 716 | `polaris.ts:707` declaration, `:713` ends on a `.map(` continuation, `:714` `.join(';')`, `:715` the `return`, `:716` the closing brace | **PARTIAL** — packet corrected at `:452`, `:1076`, `:1104`; the evidence record still says 707-713 twice (H4) |
| G5 | the ten components reproduce; the totals do not | all ten reproduce exactly (595, 109, 1,369, 661, 812, 1,075, 844, 326, 1,627, 1,803); deltas 7,076−5,449 = 1,627 and 5,150−3,347 = 1,803 equal the source records | **PARTIAL** — packet states the floors and the unpublished wrapper (`:377-391`); the record's own measurement block does not (H5) |
| G6 | the breach body is `JSON.stringify` of `ResponseLimitFailure` | `routes.ts:141`, built at `:132-134`; `ResponseLimitFailure` `:113-124`, `population` `:120-122`; PWB-REQ-006 `:381-384` | **REPAIRED as to the type**, and Q3 now quotes PWB-REQ-006 and labels its "only"-as-minimum reading — but the widened type's reach is wrong (H1, blocking) |
| G7 | RFC2-24's defined clause is `rendering-vocabularies.md:92` | `DIRECTIVE-REGISTER.md:258` → `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md:92`; table at 119–131; `:44-50` is the module summary | **REPAIRED** (`:860-871`), summary marked as summary |
| G8 | M3's Gate 3 table has six slices | `git show f35a25f:docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md`, Gate 3 at its line 739, six slice rows | **REPAIRED** (`:1070-1073`, F15 row) |
| G9 | 7,481 work items, 7,481 distinct ids | `workItems.items` length 7,481; `len(set(ids))` 7,481 | **REPAIRED** (`:136-141`), `[Observed]`, withdrawn "7,396 presumably" kept |
| G10 | `targetBeadPrefix` set at `materialization.ts:58` from the constant at `:12` | confirmed; `designPath` is the one built at `materialize-action.ts:35` | **REPAIRED** (`:739-742`) |
| G11 | three `renderMaterializePanel` call sites | `trajectory.ts:187`, `materialize-action.test.ts:42` and `:59` | **REPAIRED** (`:180-184`) |
| G12 | (a) one 80-column prose line; (b) the capture path's base | (b) repaired at `:313-317` ("relative to this session's scratchpad directory, not to the repository"); (a) see H6 | **(b) REPAIRED; (a) NOT REPAIRED** — the fix produced a 102-column line and four more prose lines went over |
| beyond G1–G12 | the P-72 row carries Q1's lane-B queueing cost | present in the row's recommendation clause ("a PWB delta queues behind lane B's open package (P-68) under the one-manifest-at-a-time rule while the POC reader-note arm would not") | **REPAIRED** |

Also verified against the disposition text: `check_governance.py` ends
**"32 OK, 20 WARN, 0 FAIL (52 checks)"** at this commit; CG-1b examined
4,860 code-span path references with 0 findings (so every code-span path
in these three files resolves, and no Butlers path is backticked in the
packet), CG-7e 32 files 0 findings, CG-15 15 quotations 0 findings
[Observed, run this session].

## Spot-check that F1–F22 did not regress

| # | Re-derived at `09b5395` | Holds |
|---|---|---|
| F1 | `forbidden` 3, `prohibit` 1, both by `str.count` and `bytes.count`; all four hits are `workItems` bead titles (`bu-0n2wk`, `bu-18cg2`, `bu-scvfk`, `bu-0855u`); 0 occurrences anywhere outside `workItems` | yes |
| F2 | `proposedWork.currentAuthority.claim.claimId` = `claim:item:baseline-spec:switchboard-identity`; the `intent:req-switchboard-identity-001` entity and two relationships join it; `MaterializationGoverningIntent.requirementId` at `materialization.ts:15` | yes, four literals |
| F3 | `no-such-claim` appears once in the packet, inside its own withdrawal sentence; S2 carries no `reason` slot; PWB-REQ-007 `:447-448` quoted correctly | yes |
| F4 | `PwbResourceLimits` `project-shape-observation.ts:65-73`, seven fields; ceilings at `:81` (2,097,152) and `:82` (8,388,608) | yes |
| F5 | every line-table row re-derived by `grep -n`: `machineHandle` 159-162, `POLARIS_SOURCE_PATH` 221/222, machine block 225-238, `browserRequestAllowed` 26-38 (file ends 38), `MATERIALIZE_HUMAN_PATH` 17, `renderMaterializePanel` 55-82, `MaterializationPacket` 20-30, `MaterializationGoverningIntent` 14-18, `buildMaterializationPacket` 43-65, `MaterializationRecord` 67-78 (`createdAt` 71), `buildTrajectoryMaterializationPacket` 31-37, `ResponseLimitIdentity` 111, `ResponseLimitFailure` 113-124 (`population` 120-122), `boundedResponse` 137-142, `PocEpistemic` 44-46, `PocModel` 98-155, `BodyReadAuthorityEvaluation` 315-324, `AuthorityDisclosure` 39-46, `PwbResourceLimits` 65-73 / 75-83 | **19 of 19 hold**; `authorityLine` 707-716 holds in the packet and not in the record (H4) |
| F6 | both denominators present; machine-only remainder named | yes (H7 aside) |
| F7 | two compositions with exact field paths, "sevenfold" absent | yes |
| F8 | 18,710 with the `scope` key, 18,719 with `identity.scope`, on this capture; 148,780 for the classes-plus-claim set; shares 0.3389% and 2.6951% against 5,520,314 | yes, all four exact |
| F9 | 415 of 415 item ids match `claim:item:…`; `item` is the only second segment; `claim:baseline-spec:switchboard-identity` matches 0 | yes |
| F10 | the `switchboard-identity` item record is 661 bytes compact, its `claim` sub-object 504 | yes |
| F11 | PWB-REQ-006 cited and quoted at `:528-537`; Q2 asks the fold-in; Q3 cites "population counts" | yes |
| F12 | `ResponseLimitIdentity` is a two-literal closed union at `routes.ts:111` | yes |
| F13 | Gate 5's `mayNot` warrant rests on PWB-REQ-005's "every human and machine rendering of the authorization basis" (spec `:220-222`), labelled [Inferred], with the L5-F9 fallback | yes |
| F14 | act "What this does not authorize" = six bullets, `:70-72`, `:73-74`, `:75`, `:76-79`, `:80-81`, `:82-84`; escalation triggers `:86-94`, registry-envelope trigger at `:92` | yes, all seven line ranges exact |
| F15 | M2 6 / M3 6 / M4 8 denominators; `model.ts` `proposedWork` at 707 with `surfaces:` opening at 710; `routes.ts` 34-96 and 225-238 disjoint; `polaris.ts` `authorityLine` outside M3's five cited regions | yes |
| F16 | Q3 and Q4 decided below the table with reasoning shown; the owner table is Q1 and Q2 | yes |
| F17 | the existing-route arm named in Q1 and not recommended, labelled [Inferred] | yes |
| F18 | four `[Unknown]` bullets in Collision (`:1183-1196`), matching the record's four `not_verifiable_this_session` entries | yes (the third repeats the stale 707-713 — H4) |
| F19 | zero non-fence lines with an odd backtick count over all 1,447 lines, so no code span crosses a line break | yes |
| F20 | — | **regressed**, see H6 |
| F21 | PWB-REQ-020 introduced as "quoted in relevant part", naming the omitted bullets | yes |
| F22 | `ResponseLimitFailure` 113-124 / `population` 120-122; `MaterializationRecord` 67-78 / `createdAt` 71; the POC spec path spelled in full at the Q1 line-26 cite and at the Gate 5 POC-delta cite | yes (Gate 0's line-26 cite at `:116` names "the POC spec", not the path, in a cell that spells the change directory — acceptable) |

## The questions

| # | Scope truthful? | Genuine gate / genuinely not? | Recommendation follows? | Register matches packet? |
|---|---|---|---|---|
| **Q1** — does `GET /api/poc/briefing` need a spec delta, and to which spec? | Yes. The reader note at POC spec `:25-26` reads exactly "the 'machine answer' is the authenticated `GET /api/poc` response", singular and definite, under "Reader notes, binding on how this file is read" (`:18`) [Observed]. The `/api/poc/polaris` precedent is real: `routes.ts:17-21`, justified by a header comment citing PWB-REQ-014/020, named by no requirement heading, 0 occurrences in either signed spec | **Genuine owner gate.** Whether a new route inside a signed spec is a CC-REV-2 spec delta is a determination about digest-bound text; VIS-4 reserves it. The act's own bullet "Spec changes route through CC-REV-2's amendment path and a new owner act" (`:78-79`) and the escalation trigger "any scope beyond the signed change" (`:93-94`) both point at the owner | Yes. Three lawful arms, each stated with its cost; the recommended PWB delta discloses its own queueing cost behind lane B; arm (c) moots Q1 and Q2 and is declined on stated grounds, labelled [Inferred]; default-if-unanswered is the conservative one (slice 3 does not ship) and slices 1–2 are explicitly unaffected | Yes, clause by clause: three arms, the same recommendation, the lane-B/P-68 queueing cost, the 8 MiB defect of arm (c), the same default. The row compresses arm (c)'s PWB-REQ-020 parity-oracle reason to its ceiling reason only — compression, not contradiction. "spec'd nowhere" in the row is consistent with the packet's spec-scoped claim |
| **Q2** — how is the ceiling declared, and does a third amend PWB-REQ-006? | Mostly. The registry facts are exact (seven fields at `:65-73`, two ceilings at `:81-82`, the closed two-literal `ResponseLimitIdentity` at `routes.ts:111`) and the escalation trigger is quoted at its line (`:92`). The "third final-output sink" framing counts routes where the clause counts kinds — H2 | **Genuine owner gate**, on either reading: minting a registry field crosses "a change to the constraints or envelope the registry entry declares" (act `:92`) regardless of whether PWB-REQ-006 requires it | Yes, and the fold-in sub-question is disclosed as the owner's call with the cost of each path. The default arm is stated *with* its defect ("a bound that could silently widen release by release"), not smoothed | Yes, clause by clause: seven fields / two ceilings, the interface-and-union widening, the superseding registry act and its line-92 trigger, the fold-in conditional, the same recommendation and the same disclosed default |
| **Q3** (decided) — the breach body's `population` | **No.** Truthful about PWB-REQ-006's wording and about the type being bound by no act, but wrong about what the widened type reaches: the same envelope is served for the human-HTML and `/api/poc` sinks (H1) | **Genuinely not a hard gate** — the type is bound by no act, and the one reading that *would* make it a gate (PWB-REQ-006's "only" as a closure) is named, labelled [Inferred], and routed back to the funnel. It is also downstream of Q1 and Q2, so it cannot ship unseen. But the no-gate *warrant* as written does not hold over the two sinks the requirement governs | **No, as written.** The decision produces a briefing-specific sentence on non-briefing responses. The restraint argument (no third `population` arm) is sound and survives the repair | The row's Q3 parenthetical matches the packet exactly — including, necessarily, the scope defect |
| **Q4** (decided) — sequencing against M4 | Yes. The dependency is correctly characterised as conceptual: the oracle reads `PocEpistemic` and `resolutionRoutes` live (`model.ts:44-46`; `project-shape-model.ts:115-118`, `:150-154`), so it self-corrects when M4 lands | **Genuinely not a gate.** A sequencing preference between two of the owner's own branches binds nothing and crosses no escalation trigger | Yes, and the one cost (a pre-M4 acceptance fixture documenting free-prose reasons) is accepted in the open, with the evidence file told to say so | Yes — "(no ordering enforced against M4)" |

## Closed-vocabulary check

Swept every backticked kebab-case token in the packet and in the P-72 row
against RFC2-24's twelve (`rendering-vocabularies.md:119-131`, read this
session). Seventeen distinct tokens; none is a minted Unknown reason.
`no-such-claim` occurs once, inside the sentence withdrawing it.
`not-applicable` is a chain state, and the packet says in three places
that the not-found and not-applicable disclosures carry no `reason` field
(`:864-880`, S2 at `:1035-1043`, S6 at `:1060-1067`) — the RFC2-24
fact-of-render arm, correctly applied. The evidence record and the
register mint nothing. **No `reason` value outside the twelve is minted
anywhere in the three artifacts** [Observed; predicate: `` `([a-z]+(-[a-z]+){1,4})` ``
over the packet and the P-72 row, 17 tokens enumerated, each inspected].

One adjacent fact the packet does not mention: `ResponseLimitFailure`'s
`population` `unknown` arm already carries a free-prose
`reason: string`, set to `` `project shape ${shape.kind}` `` at
`routes.ts:128`. It is pre-existing, it is not an Unknown *claim* reason,
and Q3 does not touch it — but Q3 is the one place that reads this union
closely, and a reader checking "no value outside the twelve" will find it
there.

## Invariants on this review

- Problem scope holds: the four Gate 1 measurements all re-derive
  (0.339%; no requirement prose on either credentialed route; the
  dispatch packet 0 times on the machine channel; `mayNot` 0 on both
  channels and all four `forbidden`/`prohibit` hits in bead titles).
- No owner trade-off smoothed: every recommendation carries its
  counter-argument, its cost and its default-if-unanswered, and both
  withdrawn questions keep their numbers and their reasoning.
- No lawful arm called unlawful: all three Q1 arms are presented as
  lawful on the packet's own reading, and the register says the same.
- Labels: substantive claims carry `[Observed]`, `[Inferred]` or
  `[Unknown]`; the four `[Unknown]`s reach the document the owner reads.
- Contract claims are quoted at defined clauses located through
  `DIRECTIVE-REGISTER.md` (RFC2-24:92, RFC2-10:209, RFC2-25:153,
  RFC8-21:79, RFC8-22:93, RFC6-14:237, RFC6-22:390, CC-REV-2, RFC3-16),
  and every quotation I checked is verbatim at its cited lines.
- Zero/all claims carry a predicate and a denominator run this session:
  619 tracked files, 415 item ids, 7,481 work items, 17 + 24 requirement
  headings, 1,447 packet lines, 4,860 code-span references.
- Digests computed by `sha256sum`, never transcribed; no manifest and no
  truncated signed digest is quoted in the packet, the record or the row
  (CG-7e and CG-15 both 0 findings); no Butlers path is backticked in the
  packet (CG-1b 0 findings over 4,860 references).
- `python3 scripts/check_governance.py` ends `0 FAIL`.

## Severity counts

- blocking: **1** (H1)
- non-blocking: **4** (H2, H3, H4, H5)
- editorial: **4** (H6, H7, H8, H9)

Total 9 findings. Eleven of the twelve review-2 findings are repaired or
substantially repaired in the packet; G4 and G5 are complete in the packet
and incomplete in the evidence record, G12(a) regressed, and G6's repair
left the scope defect H1 standing. No F1–F22 finding regressed except
F20.

Verdict: REVISE
