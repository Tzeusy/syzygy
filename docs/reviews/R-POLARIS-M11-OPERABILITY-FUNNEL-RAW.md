# R-POLARIS-M11-OPERABILITY-FUNNEL-RAW — independent review 1

Reviewer: a fresh-context review session (Claude), read-only.
Date: 2026-09-15.

## What was reviewed, and at which bytes

Worktree `m11wt`, branch `agent/syzygy-dov.11`, HEAD **2c62d0b**.
`git diff --name-only a9f671e 2c62d0b` returns exactly the two files
below, so every source byte in the worktree is the `a9f671e` byte the
packet measures.

| File | `wc -c` | `sha256sum` |
|---|---:|---|
| `docs/design/POLARIS-M11-OPERABILITY-FUNNEL.md` | 102079 | 6f7e98bad81bb3f30a614bfe944d54b1d71091fb5608a6e7f4410827c6cf3eeb |
| `docs/evidence/polaris-m11-operability-funnel-2026-09-15.json` | 39956 | 3f6b239183a8939db797fbe8e5c0029d47d2d4d5f7baa299d262c859be0cb320 |

Both computed with `wc -c` and `sha256sum`, not transcribed.

Sibling worktrees read read-only at these heads, each recorded from
`git rev-parse --short HEAD` in that worktree this session: lane B
`4090f98`, M2 `f2f37dd`, M3 `6574600`, M4 `63b8e33`, M5 `ba9ca61`,
M6 `83c9f60`, M7 `f97baf4`, M8 `bce9039`, M9 `65de02b`, M10 `95f31cb`.
All ten match the packet's collision table.

Commands run in `m11wt`: `npm run build:poc` (exit 0), `npm test`
(**123 test files passed, 3 skipped; 1686 tests passed, 3 skipped, 0
failed**), `python3 scripts/check_governance.py` — tail line read, not
`grep -c`. That tail line reads, in full: 32 OK, 20 WARN, 0 FAIL
(52 checks) — counts derived, not asserted. It is byte-identical to
the `validation.tail_line` the evidence record carries. `git status --short` is empty at the end of
this session; nothing under a tracked path was added or modified.

**Two notes on the review prompt itself, stated so the record is
honest.** (1) The prompt says the packet "asks the owner six
questions" and asks for a Q1–Q5 table; the packet asks **five**
(Q1–Q5). The phrase the prompt echoes is the packet's own sentence
that it "adds no sixth question" for M5's route-existence question.
(2) The prompt's "in particular" list names measurements that are not
in this packet and are, by their content, M10's: the ETag /
Content-Encoding header sweep, the anchor-vocabulary census
(914 of 916, 99.7817%), `inputsDigest` excluding the project-shape
block, the 1,436-occurrence wall-clock figure, the schema subject
(769 structural paths, 241 field names, 57/48/273), the 19 top-level
keys, the gzip figures, the bytes-per-top-level-key costing, and the
S6-M1 / S6-M3 dossier corrections. Substring counts over this packet:
`ETag` 0, `Content-Encoding` 0, `gzip` 0, `769` 0, `914` 0,
"top-level key" 0. I verified the thirteen measurements this packet
actually makes (M1–M13 in its evidence record) instead, plus every
contract citation, the Gate 5 RFC2-26 test and both collision
predicates.

## Findings

### F1 — non-blocking — the stderr/stdout split is 7/3, not 6/4

`docs/design/POLARIS-M11-OPERABILITY-FUNNEL.md:337` ("Count: **10** —
6 stderr, 4 stdout") and `:355` ("**four** of the six stderr sites
drop an available cause"); same values in the evidence record's
`measurements.M7_failure_detail_census` (`stderr` 6, `stdout` 4).

Defect. Over the stated predicate and denominator — a
`process.stderr.write` or `process.stdout.write` call in the whole
253-line `apps/three-surface-poc/src/main.ts` — the sites are 56, 58,
65, 89, 207, 211, 229, 239, 241, 249. Total **10** (re-derives).
stderr = 58, 65, 89, 207, 239, 241, 249 = **7**; stdout = 56, 211,
229 = **3**. The packet's own table on the same page lists exactly
those seven stderr rows and three stdout rows, so the summary line
contradicts the table beneath it, and the derived sentence "four of
the six" understates the denominator of its own class.

Repair. "Count: **10** — 7 stderr, 3 stdout" and "**four** of the
seven stderr sites drop an available cause"; correct
`M7_failure_detail_census.stderr`/`.stdout` to 7 and 3. The four
dropping sites (65, the 89–93 pair, 207, 241) and the three that do
not (58, 239, 249) are each confirmed at source and are unchanged.

### F2 — non-blocking — the lifecycle sweep's published predicate
does not produce its figure, and the predicate that does drops the
one existing restart test

`docs/design/POLARIS-M11-OPERABILITY-FUNNEL.md:396-403`; evidence
record `measurements.M9_lifecycle_absence`.

Defect. The published predicate is "a line matching `restart`,
`systemd`, `upgrade`, `pidfile`, `pid file`, `service unit` or
`.service`, case-insensitively" over 558 in-scope tracked files. Run
exactly that, with Python `re` (verification rule 1), at `a9f671e`:
**29** files carry a hit, not 22. The denominators re-derive exactly
(1,216 tracked, 558 in scope — my run at `2c62d0b` gives 1,218 and
560, the difference being this packet's own two files). The figure 22
re-derives only under a **word-boundary** predicate
(`\brestart\b|\bsystemd\b|\bupgrade\b|\bpidfile\b`), which excludes
the plural and past forms. This is the AGENTS.md lesson about a word
set published as a predicate that cannot be re-derived from what the
page says.

The seven files the word-boundary predicate silently drops are
`apps/three-surface-poc/src/polaris.ts` (367),
`apps/three-surface-poc/src/polaris-first-reading.test.ts` (229),
`packages/cap1-daemon/src/server.test.ts` (159–160),
`packages/polaris-generation-core/README.md` (41),
`packages/three-surface-poc-core/src/test-artifact-verification.ts`
(228), `scripts/launch_gate_results.py` (80) and a fifth review
record (the partition says four; there are five). The packet's
**conclusion survives** — I read all seven and none is an operator
lifecycle instruction — but one of them is substantive to slice 4:
`packages/cap1-daemon/src/server.test.ts:159` opens a describe block
named RT3 — credential stability across daemon restarts, and `:160`
is the test "a restarted daemon reuses the same credential file and
token". That is the closest existing test to slice 4's own oracle,
and slice 4 cites `packages/cap1-system/src/degradation.system.test.ts`
instead without knowing it exists. A sweep whose predicate hides the
one relevant prior art is not only an arithmetic slip.

Repair. Publish the predicate actually run (word-bounded, with the
literal alternation written out and the case folding stated), or
publish the substring figure **29** with the corrected partition
(11 evidence/pursuit JSON + 3 pursuit/plan prose + 5 review records +
8 source/test files + `packages/polaris-generation-core/README.md` +
`scripts/launch_gate_results.py` = 29). Either way, cite
`server.test.ts` RT3 in slice 4's oracle paragraph.

### F3 — non-blocking — "the only three occurrences of the string
`log`" is false as a substring claim

`docs/design/POLARIS-M11-OPERABILITY-FUNNEL.md:31` (Q2's bracketed
label).

Defect. The claim is "[Observed, the only three occurrences of the
string `log` in that 1,153-line file are at 176, 407 and 665]". As a
substring, case-insensitively, `log` occurs on **43** lines of that
file — `catalog`, `catalog-count`, `topology`, `technology`-shaped
tokens. The figure three re-derives only under `\blogs?\b`. The
substantive point (all three word-form occurrences are sink
constraints) is correct and I confirmed each.

Repair. "the only three occurrences of the word `log` or `logs`
(predicate `\blogs?\b`, case-insensitive) are at 176, 407 and 665".

### F4 — non-blocking — `maxOutputBytes` occurs 38 times in the
repository, not twice, and the packet's own point is strengthened

`docs/design/POLARIS-M11-OPERABILITY-FUNNEL.md:314-318`, labeled
[Observed].

Defect. The packet writes that the literal `maxOutputBytes` occurs
twice in the repository, at
`apps/three-surface-poc/src/polaris-generation/pipeline-demo.ts`
lines 64 and 71. Swept over all 1,216 tracked
files at `a9f671e` with Python `re`: **38** occurrences in 14 files.
The two cited are real and exact, but the name's principal home is
`packages/polaris-generation-core/src/pipeline.ts` (**11**
occurrences) with two more in its test file, and it also appears once
in `openspec/changes/polaris-manifesto-generation/INTERFACES.md`.
A count of "twice in the repository" carries no predicate and no
denominator, which is what verification rule 2 and rule 9 are for.

Repair. State the sweep: "`maxOutputBytes` occurs 38 times over the
1,216 tracked files, 13 of them in the generator package's own
pipeline and its test and one in the generator's OpenSpec
`INTERFACES.md`; inside the three POC source trees it occurs only at
`pipeline-demo.ts` lines 64 and 71." The collision warning to the
implementing bead becomes stronger, not weaker: the name is taken by
an adopted generator interface, not only by a demo.

### F5 — non-blocking — P-72 and P-77 are not on the register at the
packet's own baseline

`docs/design/POLARIS-M11-OPERABILITY-FUNNEL.md:27` ("already on the
register as **P-72**"), `:94-97` ("already on the register as M10's
Q4 under **P-77**"), and the funnel summary's "the siblings' rows are
P-67/P-68 M1, P-69 M2, P-70 M3, P-71 M4, P-72 M5, P-73 M6, P-74 M8,
P-75 M9, P-76 M7, P-77 M10". None of these carries a label.

Defect. At `a9f671e`,
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` holds
**26** rows under the predicate `^| P-` (the 21 open plus 5 acted the
prompt names), and the highest number allocated anywhere in the file
is **P-67**, added and ruled 2026-09-13. P-68 through P-77 appear
nowhere in it. Each sibling worktree's copy of that file has 27 rows
— it adds exactly one, its own (m5wt has `| P-72`, m7wt `| P-76`,
m10wt `| P-77`) — so those rows exist only on unmerged branches. The
packet knows this elsewhere: Q1 says the M10 packet was "read
read-only in the M10 worktree and not present in this one". "Already
on the register" is nevertheless a claim about a file's current
bytes, and it is false against them. This is the AGENTS.md failure
mode of a page restating state it does not own.

Repair. "…is M5's Q1, proposed as **P-72** in the M5 packet on PR #39
and not yet on the register at `a9f671e` [Observed, the register's
highest allocated number there is P-67]", and the same shape for
P-77 and for the funnel summary's list. The sequencing conclusion is
unaffected: M5's Q1 exists and is the prior question either way, and
I confirmed its text at `m5wt` — "Does `GET /api/poc/briefing`, a new
machine-credentialed route, need a spec delta before it may be
built".

### F6 — non-blocking — two clauses are attributed to PWB-REQ-006
that belong to PWB-REQ-003 and PWB-REQ-011

`docs/design/POLARIS-M11-OPERABILITY-FUNNEL.md:529` ("**PWB-REQ-006
treats a log as a governed sink, twice.**" citing spec lines 407 and
665) and `:663` ("PWB-REQ-006's oracle scans 'every model, cache,
log, HTML, JSON and record sink for sentinels' (spec line 176)").
Gate 2 makes the same move at `:533-535`.

Defect. The quoted words and the line numbers are exact — I read all
three at source. The requirement identity is not. In the PWB
specification, requirement headings sit
at 160 (PWB-REQ-003), 202 (PWB-REQ-005), 340 (PWB-REQ-006), 439
(PWB-REQ-007), 632 (PWB-REQ-011) and 679 (PWB-REQ-012). Line **176**
is therefore PWB-REQ-003's Oracle bullet, not PWB-REQ-006's; line
**665** is inside PWB-REQ-011's "Consented baseline requirement
renders verbatim" scenario. PWB-REQ-006's own Oracle is at 394–396
and reads "injected Git/read/render spies, context-independent secret
scans, complete sink-byte scans, a separately accumulated resource
ledger and exact final encoded-byte counts decide" — it says
"complete sink-byte scans" but does not enumerate the sink list the
packet attributes to it. Rule 8: a claim is anchored to a defined
clause, and a clause in a neighbouring requirement is not that
clause. Only line 407 is PWB-REQ-006's (its "Active repository
content remains inert" scenario, 404–408, which the packet cites
correctly elsewhere).

Repair. Gate 2: "**The specification treats a log as a governed sink
three times**: PWB-REQ-003's Oracle (line 176), PWB-REQ-006's
scenario (line 407) and PWB-REQ-011's scenario (line 665)." Gate 4
slice 1: attribute the sentinel-scan oracle to PWB-REQ-003 and cite
PWB-REQ-006's own Oracle at 394–396 for the sink-byte scan. Nothing
downstream changes — all three requirements are in force and slice 1
is inside all three sink populations — but the packet should not be
the reason a later reader looks for that list under PWB-REQ-006.

### F7 — non-blocking — the continuation act's escalation paragraph
is cited at the wrong lines

`docs/design/POLARIS-M11-OPERABILITY-FUNNEL.md:35` — "The
continuation act reads, verbatim at
`.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`
lines 152–155: "Stop and return to the owner before proceeding if
implementation would need any of: …".

Defect. The quoted sentence begins on line **150** ("Stop and return
to the owner before proceeding if implementation would need") and
ends on line **156** ("…or any scope beyond the signed change."). The
words are verbatim; the span is not. The packet's two narrower cites
into the same paragraph are both right: line 151 for the spec-
amendment trigger (it begins there) and lines 154–155 for the
registry-envelope trigger.

Repair. "lines 150–156".

### F8 — editorial — three quoted spans end before the span cited,
with no ellipsis

- `:29` cites PWB-REQ-021 "lines 975–978" for a quotation whose words
  end on line **977** at "population"; lines 977–978 continue "a
  structurally lawful run can be not ready, and a valid owner act can
  lawfully retain a negative judgment about it."
- `:566` cites `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` "lines
  59–63" for a quotation whose words end mid-line **61** at
  "`.syzygy/**`"; the source continues ", under the in-force craft
  policies and the vendored `th-engineering` standards…".
- `:80-84` quotes S10-M3's slice plan as "optionally add a pidfile
  written at startup under `stateDir`"; the source sentence is
  "Optionally add a pidfile written at startup under stateDir and a
  tiny restart script that reads it."

Each is a fair paraphrase-free truncation, but the packet's own
standard is "no elision unmarked". Repair: narrow the cited span to
the quoted words, or mark the tail with "…".

### F9 — editorial — three published line-count denominators are one
higher than `wc -l`

The PWB spec is called a "1,153-line file" (`:31`, `:1193`) and is
**1152** by `wc -l`; the POC spec "1,009 lines" (`:100`) is **1008**;
`openspec/changes/polaris-project-wide-butlers-model/tasks.md` "a
139-line file" (`:630`) is **138**. All three are the split-on-
newline count. The packet already catches exactly this for
`docs/THREE-SURFACE-POC.md` and calls it "off by one, immaterial" —
but three of these are published denominators for absence claims
(Gate 6 item 3 lists 1,153 and 1,009 as rule-9 denominators), so the
convention should be stated once and applied, not caught once.

### F10 — editorial — the three over-width lines are mislocated

`:1223-1225` says the three remaining over-width non-fence lines are
"the two decision-record paths in Gate 0 and the impact-ledger path
in Gate 3". Re-derived: lines **93** (80 cols), **124** (79) and
**602** (85). Line 124 is in Gate 0; line **93** is in "Decided in
this packet, not put to the owner", which ends at line 100 (Gate 0
opens at 102). The count of three and the "unbreakable code-span
path" characterization are both correct.

### F11 — editorial — "undercounts the table by two" rests on an
unstated reading, and S10-F1's words are not in the file called the
dossier

`:216-222`. S10-F1's own sentence — confirmed verbatim in
`docs/pursuits/2026-09-13-vision-pursuit-data.json` and
`docs/pursuits/2026-09-13-vision-pursuit-harvest.json`, and **not**
in `docs/pursuits/2026-09-13-vision-pursuit.md`, which is the file
the packet's Gate 0 names as the dossier — enumerates "the five human
surfaces, /api/poc, /api/poc/polaris and their tailnet mirrors": 7
paths plus 7 mirrors = **14** distinct paths. The computed table is
17, so the literal undercount is **three** — the two POST materialize
routes and the `/butlers-syzygy/` trailing-slash mirror of `/`. "By
two" holds only if S10-F1 is read as describing `pocRoutes`' 15 GET
routes, which is a reasonable reading but is not the reading the
packet states. Repair: cite the file the sentence is in, and say
which reading the "by two" figure uses.

### F12 — editorial — `readinessPopulation` is cited at the wrong
lines

`:817-819` cites `packages/three-surface-poc-core/src/model.ts` lines
213–221 for the `readinessPopulation` builder; the function is
**211–220** (signature at 211, closing brace at 220; its doc comment
ends at 210). Q3's separate cite of "lines 217–219" for the
input-side snapshot is inside the function and acceptable.

### F13 — editorial — Q1's heading asks something the body then
declines to ask

`:27`. The question reads "**What credential class may a status
disclosure carry, and may a third machine-credentialed route be
minted at all?**" and the body then says the second limb "is not this
packet's", is M5's Q1, and that "this packet adds no sixth question
for it and rules it neither way". The disposition is correct and
consistent with the rest of the packet; the heading nevertheless
invites the owner to answer the P-72 question inside a P-number that
does not own it. Repair: move the second limb out of the heading into
the body's "the prior question is not this packet's" sentence.

## Q1–Q5

| # | Scope truthful? | Genuine hard human gate? | Recommendation follows from the evidence? | Every lawful arm named? |
|---|---|---|---|---|
| Q1 credential class of a status disclosure | Yes — the 17-route table, the `human-open` / `browserRequestAllowed` mechanism and the SEC-1 words all re-derive exactly | **Yes.** It turns on which reading SEC-1 lines 14–16 bear for a body carrying project metadata and no observed content; a delegate may not settle that. RFC5-3's "two classes are exhaustive" (lines 109–117) is quoted correctly and closes the third-class escape | Yes, and conservatively: it recommends the more restrictive class and states the counter-argument (a credentialed status route is useless when most needed) in the owner's own terms | Two arms named, both lawful, neither called unlawful. Default (machine route does not ship) is stated and lawful. F13 is the only defect and it is presentational |
| Q2 does "emit only" forbid a stderr breach line | Yes — the registry sentence at line 281 is byte-exact and the file's sha256 does equal the digest the amendment act records (compared this session; neither value reproduced, per CG-15) | **Yes.** It asks how far an act-bound word reaches, where the narrower reading costs operability and the wider one costs nothing | Yes. The recommended reading is grounded in PWB-REQ-006's own scenario (419–426, verified) and the counter-reading in the specification's log-sink sentences (see F6 for their true owners) | Two arms, both lawful. Notably the **default if unanswered is the second, narrower arm**, not the recommended one — a deliberate fail-closed choice, disclosed as such. Good practice |
| Q3 is the readiness widening conformance or amendment | Yes. Every quoted sentence (378, 384, 964–968) is exact, and the blindness is real: `recordBreach` has 12 non-test occurrences, all input-side, and 0 in `routes.ts` | **Yes — this is the packet's central question and it is a real one.** PWB-REQ-006's Oracle line does treat the ledger and the byte count as two deciders, which is the whole residue | Yes. The two quotations do carry the recommended reading, and the packet does not overclaim: it names the residue and refuses to resolve it | Two arms. The second arm's cost (CC-REV-2 plus a new act, re-opening act-bound bytes) is stated accurately. Default (slice 3 does not ship) is lawful and leaves the other three slices untouched |
| Q4 must a new registry limit be minted | Yes, and this is the packet's strongest measurement: `PwbResourceLimits` lines 65–73 (7 fields, two output-side), registry lines 270–271 and 279–280, `ResourceLimitBreach.limit` typed `keyof PwbResourceLimits` at line 205 — all four verified at source. The dossier's prerequisite second half really does rest on a false premise | **Partly.** The first half the packet answers itself and the answer is right; what remains for the owner is only "do you want a distinct limit anyway", plus the escalation-trigger consequence if so. That second half is a genuine act question | Yes. And the escalation-trigger quotation is verbatim, though cited at the wrong lines (F7) | Two arms. The minting arm is correctly called an escalation trigger rather than unlawful, and the packet is explicit that the registry bytes may not be edited on **either** arm. Default is lawful |
| Q5 may the status line ride `pageShell` | Yes — 5 footer call sites, no footer-fact function, and the 612,665 / 618,515 headroom both re-derive from the lane A record | **Yes**, because it spends a budget that is itself under open owner question (P-67 ruled, lane B open) | Yes, with the cost honestly priced at under 0.07% of headroom per page and the counter-argument ("a packet that charges that budget for a convenience is spending another move's savings") put at full strength | Two arms named; a third — render on the status route only and not on the home page — is lawful and unnamed. Default (second arm) is stated and lawful |

No owner trade-off is smoothed into consensus language anywhere in
the five rows. Every "counter-argument" paragraph states the opposing
case in its own strongest form, and three of the five defaults differ
from the recommendation, which is the opposite of a packet steering
its owner.

**"Decided in this packet, not put to the owner" — is each a
delegate's call?** Yes, on all five. The prerequisite falsification
and the P0-CEILING supersession are measurements (both verified: the
lane A record's `result.tailnetHeadroom.after` is 612,665 and the
retained 503 body's `observed` is 2,132,656 over a `declared` of
2,097,152). "No pidfile" is forced by an existing assertion —
`packages/cap1-system/src/state-dir.system.test.ts:294` reads
`expect(readdirSync(benignTarget)).toEqual(['machine-credential.token'])`,
exactly as quoted — and by `packages/cap1-daemon/src/server.ts`
lines 28–30. "No derived age, no green" declines a dossier request
(S10-M1's "how old") in the conservative direction while rendering
both instants, so the reader can still derive what the surface will
not assert; POC-REQ-032's falsifier at spec line 596 is quoted
exactly and `health` really does occur once in the POC spec and zero
times in the PWB spec. The improvement-cycle tracing item defers
rather than decides. **No owner question is hidden in the section.**

## Gate 5 — the RFC2-26 requirement-and-scenario test

RFC2-26 is quoted at
`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`
lines 196–221 under the `###` heading at line 194. I normalized
whitespace and emphasis and compared the packet's block quote to
those source lines programmatically: **identical, both paragraphs, no
elision**. The denominator is four slice rows and the test is run
over all four.

| Slice | Cited requirement and scenario | Verified at source? |
|---|---|---|
| 1 | PWB-REQ-006 at spec line 340; scenario "Active repository content remains inert" at 404–408, THEN at 407 | Heading, scenario heading and THEN limb all exact. The "none enumerated" judgment is sound: RFC2-26's enumerated consequence classes are the five phrases at lines 198–201 and a stderr line falls in none of them |
| 2 | POC-REQ-060 at POC spec 927 ("One design language, one epistemic encoding"); POC-REQ-032 at 574 with scenario "Unknown disclosed in the narrative" at 599; PWB-REQ-020 at 902 with "Complete model has wire parity" at 928–933 | All five headings exact at the cited lines. The "partial" verdict on the machine form is fair: the scenario's WHEN really does say "Polaris renders a project-wide evaluation" (line 930), and a status body is not one |
| 3 | PWB-REQ-006 at 340, scenario "Resource breach is bounded and explicit" at 419–426; PWB-REQ-021 at 946, scenario "Lawful run can remain not ready" at 1009–1015 | Exact, and the packet's verbatim rendering of the 419–426 scenario matches line for line. The WHEN limb does name "final-output ceiling" and the AND limb does say "cold-open readiness is false", so "closest possible match" is not overclaimed |
| 4 | None; argued from S10-F6 and the direction's recorded-finding limb at lines 55–56, with the "alter the runnable demonstration or falsify/repair a named product finding" bound at lines 23–24 | Both direction quotations exact at those lines. The absence claim holds against the clause's own enumerated list |

The packet's closing sentence — that the test establishes mapping and
not lawfulness, and that RFC2-26's scope sentence at lines 219–220 is
the owner's to read broadly or narrowly — is correct and properly
labeled.

## Collision and sequencing

Both predicates recomputed from scratch this session over the ten
sibling worktrees at the heads recorded above, using the packet's
stated extraction (code spans from every `.md` under each worktree's
`docs/design/`, kept if they begin `apps/`, `packages/`, `scripts/`
or `docs/` or equal `package.json`, kept if they resolve as a file in
`m11wt`, intersected with the 16-file surface; predicate B restricted
to each packet's `## Gate 3 — Topology` section).

**Every one of the twenty cells re-derives exactly**, and so does
every `The B files` list: lane B 1/0, M2 4/4, M3 3/1, M4 7/6, M5 6/4,
M6 2/1, M7 5/4, M8 14/9, M9 8/4, M10 7/5. "7 of 10 name `routes.ts`"
re-derives (7). `model.ts` in 6 re-derives; `polaris.ts` is also 6,
which the evidence record carries and the prose does not mention.
"M8 is the largest overlap at 9 of 16" re-derives. The four M11-only
files — `resource-ledger.ts`, `page-shell.ts`,
`docs/THREE-SURFACE-POC.md` and `materialize-action.ts` — appear in
no sibling's Gate 3 table.

Sequencing. The status route's existence really is sequenced behind
M5's Q1, whose text I read at `m5wt` and which is exactly that
question; the improvement-cycle tracing limb really is M10's Q4,
which I read at `m10wt` line 38, and the credential-class question at
`m10wt` line 37 is M10's Q3 as cited. Neither is re-asked. The only
defect is F5: both are described as being "already on the register"
when their rows exist only on the sibling branches. The M1 lane A/B
headroom, M6 (the generator's own stderr writes at
`apps/three-surface-poc/src/polaris-generation/pipeline-demo-main.ts`
lines 35–36, verified) and M4 (retention of last-request outcomes)
couplings are each stated fairly and none overstates the collision.

## Measurement table

| Claim | Re-derives? | My figure / the predicate difference |
|---|---|---|
| 17 routes; 13 `human-open`, 4 `machine-credentialed`; 0 matching the alternation status / health / live / ready case-insensitively | Yes | Built the worktree and enumerated `pocRoutes` (15) + `materializeRoutes` (2) against a stub model: 17, {human-open 13, machine-credentialed 4}, 0 status-like. The 17-row table is path-for-path identical |
| `minimalRootRoute` at `server.ts` 269–282, registered by nothing | Yes | Declared at 269; occurs only there, in `server.test.ts` (11, 196, 265, 288) and in docs |
| `boundedResponse` is 137–142, breach branch at 141, quoted verbatim | Yes | Exact, including the whole `return` line. Comment 98–106, constants 108–109, interface 113–124 with `readiness: false` at 123, `responseLimitFailure` 132–134 all confirmed |
| `routes.ts` is 240 lines; `recordBreach` 0 times in it; it imports no `ResourceLedger`; imports are lines 1–11 | Yes | 240 lines; both counts 0; imports end at 11 |
| `recordBreach` has 12 non-test occurrences, 5 in `resource-ledger.ts`, 7 input-side at the named lines | Yes | 12 exactly: ledger 96, 139, 148, 160, 171; `git-object-reader.ts` 307, 328, 351; `project-shape-observation.ts` 412, 427, 545, 548 |
| Logging sweep: 86/45, 53/27, 18/9 files; 37 hits in 7 files, all `*-main.ts`; 0 and 0 in core and daemon; 157 `.ts`, 81 non-test | Yes | Every number exact, and the seven file names are the seven listed |
| `handleRequest` is 169–224 with four outcome branches at 178, 196, 214, 218 and 0 logging calls | Yes | Exact; `createServer` is 165–167 as the "narrowed" row says |
| `ResourceLedgerSummary` 81–90 with 7 fields; `ResourceLedger` 92–121 with 14 members, 0 output-side; file 207 lines | Yes | Exact. (Field lines are 83–89; the cited 82–89 includes the comment at 82 — immaterial) |
| `PwbResourceLimits` 65–73, 7 fields, two output-side; block quoted verbatim | Yes | Exact, character for character |
| `ResourceLimitBreach` at 204–210, `limit` typed `keyof PwbResourceLimits` at 205 | Yes | Exact |
| Registry declares both ceilings at 270–271 with semantics at 279–280; `breachResult` at 281 quoted verbatim | Yes | The 281 quotation is byte-identical to the source line, whitespace aside |
| The registry file's sha256 equals the digest the amendment act records | Yes | Compared this session; match. Neither value is reproduced here or in the packet (CG-7e / CG-15 respected) |
| `maxHumanResponseBytes` 2097152 at `project-shape-observation.ts` line 81 | Yes | Exact |
| Determinism constraint: 630 snapshot, 635 digest, 636 `deepFreeze`, comment 288–289; `project-shape-model.ts` 640 | Yes | All five exact |
| `main.ts` stderr/stdout sites: 10 total | Yes for 10 | **No** for the split — 7 stderr / 3 stdout, not 6/4 (F1). All ten line numbers and all ten "detail dropped?" verdicts are correct |
| Evaluation identity composed at `main.ts` 101–105; `asOf` at 134; banner 211; "Credential value is never printed" 219; signal handlers 224–234 | Yes | All exact |
| 5 footer call sites under `^\s*footer:` over 45 non-test app files | Yes | Exactly `routes.ts` 92, `polaris.ts` 1630, `polaris-source.ts` 140, `trajectory.ts` 197, `orrery.ts` 162 |
| `pageShell` 44–74, one `footer` slot declared at 36 and rendered at 70 | Yes | Exact |
| Lifecycle sweep: 1,216 tracked, 558 in scope, 22 files with a hit | Denominators yes; **count no** | 29 under the published substring predicate; 22 only under a word-boundary one (F2) |
| `docs/THREE-SURFACE-POC.md` 89 lines, 0 hits, its four H2 headings | Yes | Exact, including all four heading strings |
| `package.json` declares 13 scripts at lines 12–24, 0 lifecycle; `scripts/` holds 20 `.py` and 0 shell files | Yes | Exact |
| `READINESS_ARMS` 47–58, exactly ten, doc comment 45–46 quoted verbatim; arm 9 `resource-breach` at 365–366; `ReadinessPopulation` 83–89 | Yes | All exact; `resource-breach` is the ninth entry |
| `readinessPopulation` builder in `model.ts` | Partly | Function is 211–220, cited as 213–221 (F12) |
| Act-binding sweep: 538 governance files + 24 manifests; 0 manifest rows; 4 hits, all in one CC-REV-2 inventory at lines 61, 66, 67, 69 | Yes | 538 and 24 exact; exactly four hits, exactly those four files, exactly those four lines; the ledger is a row of neither sibling manifest (0 hits for its basename in both); its lines 3–5 self-declaration is verbatim |
| The fifth consumer: `fresh-checkout-demo-main.ts` row at ledger line 71; `fresh-checkout-verdict.ts:130`; `fresh-checkout-demo-main.ts` 313 and 485 | Yes | All four exact. The blindness the packet describes is real |
| PWB `tasks.md`: 35 boxes, 32 checked, 3 open (4.6, 5.2, 5.3) | Yes | Exact under `^- \[[ xX]\] ` |
| Headroom 612,665 tailnet and 618,515 direct against a 2,097,152 ceiling at Butlers `2e3bac97` | Yes | `result.tailnetHeadroom.after` is 612,665; 2,097,152 − 1,478,637 = 618,515; shortfalls 78,637 / 84,487 confirmed |
| Capture: `run.sh` issued 7 requests, 2 of them the `/polaris` forms, both 503; `daemon.err` 0 bytes; 503 body 838 bytes with the nine named fields | Yes | 7 curls (the eighth is conditional and did not fire); both `/polaris` captures are the same 838-byte body; `daemon.err` is 0 bytes; `daemon.log` is 799 bytes of banner; the field list is exact |
| 17 requirements / 31 scenarios and 24 / 24, under `^### Requirement` and `^#### Scenario` | Yes | Exact |
| `health` occurs once across both specs, as POC-REQ-032's falsifier | Yes | POC line 596, PWB 0 |
| "only three occurrences of the string `log`" at 176, 407, 665 | Count yes, predicate no | 43 lines under the stated substring predicate (F3) |
| `maxOutputBytes` "occurs twice in the repository" | **No** | 38 occurrences in 14 tracked files (F4) |
| Both response ceilings already typed and declared, so no registry edit is needed — the dossier prerequisite's second half is falsified | Yes | This is the packet's key finding and it is correct at source on all four legs |
| Packet conventions: 1,257 non-fence lines, 0 odd-backtick lines, 326 distinct code spans, 34 slash-bearing non-resolving, partitioned 21+5+2+2+1+1+1+1 | Yes | 1,257; 0; 326; 87 slash-bearing of which exactly 34 do not resolve, and the 34 are exactly the enumerated set. No 16-or-longer hex run occurs anywhere in the packet |
| Over-width non-fence lines outside tables, headings and quotes: 3 | Count yes, location no | Lines 93, 124, 602 (F10) |
| `check_governance.py` ends `0 FAIL` | Yes | `32 OK, 20 WARN, 0 FAIL (52 checks)`, tail line read |
| All 15 file digests and byte counts in the evidence record | Yes | Recomputed all 15 with `hashlib`/`len`: 0 mismatches |
| Collision predicates A and B over ten siblings | Yes | All 20 cells and all ten B-file lists reproduce exactly |

## Invariants

No manifest row or truncated signed digest is reproduced in the
packet or in this review; the one digest comparison is reported as a
match with the record cited by path (CG-7e, CG-15). No
observed-repository path appears in a code span in either file
(CG-1b) — the Butlers commit identifiers that do appear are revision
strings, not paths. Every code span that is a path claim resolves in
this worktree; the 34 that contain `/` and do not resolve are
enumerated in the packet and each is a route, a glob, a placeholder,
a command, an out-of-repository capture path or a file a slice would
create. Every non-fence line has an even backtick count, so no code
span is broken across a line break. Substantive claims carry
[Observed] (39), [Inferred] (6) or [Unknown] (4); the four [Unknown]s
are honest and one of them — whether any `docs/evidence/*.json`
digest table binds the bytes slices 2 and 3 would edit — correctly
scopes a sweep the packet did not run and hands it to the
implementing bead as verification rule 10.

No digest-bound byte is proposed for edit. I checked the acceptance
record's manifests and the PERFORMED heads against the fourteen
implementation-plane files independently of the packet's own sweep
and reached the same result: zero manifest rows, and the only four
hits anywhere in the 546-file governance-plus-manifest population are
the CC-REV-2 inventory rows the packet already discloses. The
registry JSON, both specifications and every act record are read-only
throughout. Slice 3's design explicitly refuses to mutate the frozen
observation or its digest, and slice 3's mutant (e) asserts
PWB-REQ-022's 84+2 denominator is unchanged — the discipline
AGENTS.md's standing seam rule requires.

## Counts by severity

Blocking **0**. Non-blocking **7** (F1–F7). Editorial **6**
(F8–F13).

None of the seven non-blocking findings changes an owner's lawful
arms, a default, or a recommendation. Four of them (F1–F4) are
figures or predicates that do not re-derive as published; one (F5) is
a state claim about a governance file that is false at the packet's
own baseline; two (F6, F7) are citation-anchor errors where the words
quoted are exact. F2 is the one with a substantive tail: the
predicate that produces the published figure also hides the single
existing daemon-restart test, which slice 4's oracle should cite.

Verdict: CONFIRM WITH EXCEPTIONS
