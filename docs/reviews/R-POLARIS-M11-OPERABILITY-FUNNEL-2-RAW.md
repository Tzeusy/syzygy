# R-POLARIS-M11-OPERABILITY-FUNNEL-2-RAW — independent review 2

Reviewer: a second fresh-context review session (Claude), read-only.
Date: 2026-09-15.

## What was reviewed, and at which bytes

Worktree `m11wt`, branch `agent/syzygy-dov.11`, HEAD **9cfb31b**
(`9cfb31ba9ea5dc49e720f73d43653677a46d0b96`). `git status --short`
returned empty before this review began and empty after it ended; no
tracked file and no `node_modules` entry was modified [Observed].

| File reviewed | `wc -c` | `sha256sum` |
|---|---:|---|
| `docs/design/POLARIS-M11-OPERABILITY-FUNNEL.md` | 131795 | 5dd76226a5ae8b7cf28a000008bafca674aa215d1bf6fc5a5651acd7449e30c4 |
| `docs/evidence/polaris-m11-operability-funnel-2026-09-15.json` | 65059 | dffda0512d3b22f825d4fe6aaeb6ecdd5653a46091b4ca83b4f8a818092a89b5 |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 34833 | 2a31628fd886132538716355275f5ff0fb3df538c011374a70a4cc624d3eb230 |
| `docs/reviews/R-POLARIS-M11-OPERABILITY-FUNNEL-RAW.md` | 36182 | 943d567120272ac97e05b6de0b61f14800d5ed973df6f353e9b052e60d3ac049 |

All eight figures computed this session with `wc -c` and `sha256sum`,
never transcribed. The retained review 1 digest above is byte-identical
to the one the packet's review-1 section and the evidence record's
`review1.raw_sha256` publish [Observed].

The two files review 1 was bound to, recomputed with `git show
2c62d0b:<path>` piped to `wc -c` and `sha256sum`: the packet 102079 /
`6f7e98bad81bb3f30a614bfe944d54b1d71091fb5608a6e7f4410827c6cf3eeb`, the
record 39956 / `3f6b239183a8939db797fbe8e5c0029d47d2d4d5f7baa299d262c859be0cb320`.
Both match the raw's own table and the packet's restatement of it
exactly [Observed].

Sibling worktrees read read-only, each head from `git -C <wt> rev-parse`
this session: lane B `4090f98`, M2 `f2f37dd`, M3 `6574600`, M4
`63b8e33`, M5 `ba9ca61`, M6 `83c9f60`, M7 `f97baf4`, M8 `bce9039`, M9
`65de02b`, M10 `95f31cb`. All ten match the packet's collision table and
M10's matches this review's prompt [Observed]. Every sibling tree was
clean; none was written.

Commands run in `m11wt`: `npm run build:poc` (exit 0); `npm test` — **123
test files passed, 3 skipped (126); 1686 tests passed, 3 skipped, 0
failed**; `python3 scripts/check_governance.py`, tail line read in full
rather than an exit code or a grep count (verification rule 4): 32 OK,
20 WARN, 0 FAIL (52 checks) — counts derived, not asserted. That is
byte-identical to the tail line the packet's Gate 6 item 11 and the
record's `validation` and `review1.validation_after_review1` blocks
publish [Observed].

No daemon was started and no provider was called. The retained captures
were read with Python only. No observed-repository path is reproduced in
this review, in backticks or otherwise; the registry digest comparison
below is reported as a match and the record is cited by path, per CG-7e
and CG-15.

## (a) Review-1 repair verification, F1–F13

Every repair was re-derived against source; none is accepted on the
packet's or the raw's say-so.

| # | Verdict | Evidence re-derived this session |
|---|---|---|
| F1 | **REPAIRED** | `apps/three-surface-poc/src/main.ts` swept whole with Python `re` over its 253 `wc -l` lines: 10 sites — `process.stderr.write` at 58, 65, 89, 207, 239, 241, 249 (**7**) and `process.stdout.write` at 56, 211, 229 (**3**). The packet's census line publishes 7/3 with those exact line numbers, its derived sentence reads "four of the **seven**" and the funnel summary's dossier line reads "four of the seven stderr sites". The record's `M7_failure_detail_census` carries `stderr: 7`, `stdout: 3` and three dated sibling notes naming the superseded 6 and 4. The literals `6 stderr, 4 stdout` and `occurs twice` return 0 hits over the packet; `four of the six` returns 1, inside a `superseded wording:` quotation at packet line 409 |
| F2 | **REPAIRED** | Both predicates run this session with Python `re` over the **558** in-scope files of the **1,216** tracked at `a9f671e` (`git ls-tree -r -z --name-only`, filtered to `docs/`, `scripts/`, `apps/`, `packages/` and `README.md`). Predicate A (substring `restart|systemd|upgrade|pidfile|pid file|service unit|\.service`, case-insensitive): **29** files. Predicate B (`\brestart\b|\bsystemd\b|\bupgrade\b|\bpidfile\b`): **22**. The A-only difference is exactly the seven files the packet names, in its order. The 29-file partition sums: 11 evidence/pursuit JSON + 3 pursuit-or-plan prose + 5 review records + 8 source/test + `packages/polaris-generation-core/README.md` + `scripts/launch_gate_results.py` = 29, re-derived by classifying all 29. `packages/cap1-daemon/src/server.test.ts` line 159 is the describe "RT3 — credential stability across daemon restarts" and 160 its test; both are cited in slice 4's oracle paragraph, spans 159–174, which is exact (174 closes the block) |
| F3 | **REPAIRED** | Over the PWB specification in full: `log` as a case-insensitive substring matches **43** lines; `\blogs?\b`, Python `re`, matches **3**, at 176, 407 and 665. Q2's bracket names the word predicate, keeps the three lines, publishes the 43 and marks the superseded substring wording |
| F4 | **REPAIRED, with the finding's own defect correctly rejected** | `maxOutputBytes` swept with Python `re` over every blob of both commits. At `a9f671e`: **31** occurrences in **12** of 1,216 files — 11 in `packages/polaris-generation-core/src/pipeline.ts`, 2 in its test, 1 in `openspec/changes/polaris-manifesto-generation/INTERFACES.md`, 2 at `apps/three-surface-poc/src/polaris-generation/pipeline-demo.ts` (lines 64 and 71, the only two inside the three POC source trees), the remaining 15 in six evidence and pursuit JSON files. At `2c62d0b`: **38** in **14** of 1,218 — the two extra files are the packet (4) and its record (3), 7 occurrences. **The packet is right and review 1's 38/14 is the `2c62d0b` figure**, exactly as the close-out states |
| F5 | **REPAIRED** | `PENDING-OWNER-DECISIONS.md` at `a9f671e`: **26** rows under `^| P-`, the highest allocated number anywhere in the file **P-67**, and `P-7[0-9]` **0** hits. The literal `already on the register` returns 2 hits over the packet, both inside `superseded wording:` quotations (lines 38 and 114); Q1, the improvement-cycle paragraph and the funnel summary each describe P-72 and P-77 as branch-only proposals with their PR numbers |
| F6 | **REPAIRED** | Requirement headings read at source: 160 PWB-REQ-003, 202 -005, **340** -006, 439 -007, **632** -011. So 176 falls under PWB-REQ-003, 407 under PWB-REQ-006 and 665 under PWB-REQ-011, as the packet now says in Gate 2 and in Gate 4's slice 1. PWB-REQ-006's own Oracle is at **394–396** and reads, verbatim, "injected Git/read/render spies, context-independent secret scans, complete sink-byte scans, a separately accumulated resource ledger and exact final encoded-byte counts decide" — the packet quotes it identically in both places |
| F7 | **REPAIRED (the span), PARTIAL (the exactness claim about one sub-cite)** | The escalation sentence begins on line **150** at "Stop" and ends on line **156** at "the signed change."; Q4 now cites 150–156. The registry-envelope sub-cite at **154–155** is exact. The specification-amendment sub-cite at **line 151** is not: line 151 ends "…a further amendment to" and the phrase the packet quotes completes on 152. See G5 |
| F8 | **REPAIRED** | All three narrowings checked at source. PWB-REQ-021's quoted words end mid-**977** (978 opens "a structurally lawful run can be not ready…"); `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`'s end mid-**61** (which continues ", under the in-force craft policies…" to 63); S10-M3's sentence is "Optionally add a pidfile written at startup under stateDir and a tiny restart script that reads it", found verbatim, so the marked elision and the disclosed unbackticked `stateDir` are both correct |
| F9 | **REPAIRED** | `wc -l` this session: PWB specification **1152**, three-surface specification **1008**, PWB `tasks.md` **138**. A "Line-count convention, stated once" paragraph occurs exactly **once**, at packet line 23, beside the line-number convention at 18. All four published denominators follow it: Q2's bracket (1,152), the `health` sentence (1,008 and 1,152), the `tasks.md` count (138) and Gate 6 item 3 (1,152 and 1,008). The literals `1,153` and `1,009` survive only inside `superseded` quotations, at packet lines 39, 102 and 1297 |
| F10 | **REPAIRED** | Re-derived over the final bytes: the narrow population (outside fences, tables, headings and block quotes, > 78 columns) is exactly **3**, at lines **107** (80 columns), **142** (79) and **704** (85), each a single unbreakable code-span path. Line 107 is in "Decided in this packet, not put to the owner", which ends before Gate 0's heading at line 120; 142 is in Gate 0; 704 is the impact-ledger path in Gate 3. Every figure matches the packet's Gate 6 item 10 |
| F11 | **REPAIRED for S10-F1; the defect class survives elsewhere** | `grep -F` of S10-F1's sentence over the three pursuit files: **0** in `docs/pursuits/2026-09-13-vision-pursuit.md`, **1** in `docs/pursuits/2026-09-13-vision-pursuit-data.json`, **1** in `docs/pursuits/2026-09-13-vision-pursuit-harvest.json`. The packet cites the harvest file with its jq path and publishes both readings (14 read literally, an undercount of three; 15 `GET` routes read as `pocRoutes`, an undercount of two), both of which I reproduce from the computed table. Four other "the dossier" quotations are still attributed to the `.md` — see G6 |
| F12 | **REPAIRED** | In `packages/three-surface-poc-core/src/model.ts` the `readinessPopulation` signature is line **211** and its closing brace **220**, the doc comment ending at 210. The slice 3 design and the record's `M6_readiness_arms.readinessPopulation_builder` both carry 211–220 under a dated note; Q3's separate cite of 217–219 is inside the function and correct |
| F13 | **REPAIRED** | Q1's heading is now the single limb "What credential class may a status disclosure carry?"; the superseded two-limb heading is quoted and dated in the body's "the prior question is not this packet's" sentence. The record's `owner_questions.questions[0].gist` is unedited and a dated sibling key `gist_note_2026_09_15` carries the disposition. Q1's recommendation, both arms and its default are unchanged |

**Superseded wording is marked, never deleted** [Observed]: every one of
the eleven stale literals this review's prompt enumerates returns either
0 hits over the packet or hits only inside a `superseded` or `corrected`
bracket, checked line by line.

## (b) Load-bearing measurements, re-run

Each was reproduced independently; the packet's figure is given only
after mine.

1. **The route table.** `npm run build:poc`, then `pocRoutes` and
   `materializeRoutes` imported from `apps/three-surface-poc/dist/` and
   enumerated against a stub model: **17** routes — **13**
   `human-open`, **4** `machine-credentialed`, **0** whose path matches
   `status|health|live|ready` case-insensitively; 15 `GET` from
   `pocRoutes`, 2 `POST` from `materializeRoutes`. All seventeen
   method-and-path pairs match the packet's table row for row, in order
   [Observed]. `minimalRootRoute` occurs in `packages/cap1-daemon/src/server.ts`
   (1) and its test file (4) and in no route list, swept over all 1,216
   tracked files.
2. **Zero logging in any request-handling path.** Predicate `process.stderr`,
   `process.stdout`, `console.`, `logger` or `log(` over non-test `.ts`
   files. Denominators re-counted: `apps/three-surface-poc/src` 86 `.ts`
   / **45** non-test; `packages/three-surface-poc-core/src` 53 / **27**;
   `packages/cap1-daemon/src` 18 / **9** — **81** of 157. Hits: **37**
   in the app, in 7 files; **0** and **0** in core and daemon. Per file:
   10 `main.ts`, 6 `pwb-mutation-run-main.ts`, 6 `pwb-mutation-sweep-main.ts`,
   5 `capture-test-artifact-main.ts`, 4 `polaris-accessibility-main.ts`,
   3 `fresh-checkout-demo-main.ts`, 3 `polaris-generation/pipeline-demo-main.ts`
   = 37 [Observed]. See G3 for the one defect in how the packet labels
   this population.
3. **The retained capture.** `run.sh` issues exactly **7** requests —
   three in the `polaris trajectory orrery` loop, the home page, the
   tailnet `/polaris`, and the two credentialed machine endpoints; the
   conditional source-route sample did not fire in that run. Both
   `/polaris` forms answered with an 838-byte failure body whose
   `served` is `nothing`, `limit` is `maxHumanResponseBytes`, `declared`
   2097152, `observed` 2132656 (direct) and `readiness` false. The
   captured `daemon.err` is **0 bytes**; `daemon.log` is the startup
   banner alone [Observed, parsed with Python; no observed-repository
   path and no credential value is reproduced here].
4. **`boundedResponse`.** `apps/three-surface-poc/src/routes.ts` is 240
   lines; the function is **137–142**, its comment 136, its breach
   branch **141**, returning `RESPONSE_LIMIT_STATUS` with the
   `responseLimitFailure` JSON. `recordBreach` occurs **0** times in
   that file and `ResourceLedger` **0** times, so no ledger is in scope;
   its import list is lines 1–11. The 12 non-test `recordBreach`
   occurrences are `resource-ledger.ts` 96/139/148/160/171 (5),
   `git-object-reader.ts` 307/328/351 (3) and
   `project-shape-observation.ts` 412/427/545/548 (4) — all seven
   non-ledger sites input-side [Observed].
5. **The frozen evaluation.** `project-shape-observation.ts` line **630**
   is `limitBreaches: [...ledger.breaches]`, **635** computes
   `observationDigest`, **636** returns `deepFreeze(...)`; the
   same-inputs-same-digest comment is at 288–289;
   `project-shape-model.ts` line **640** is the phase-B-inclusive
   snapshot [Observed]. The determinism argument holds as written.
6. **`READINESS_ARMS`.** Doc comment **45–46** reads "The ten readiness
   arms, one per clause of the requirement's readiness sentence. Each
   makes readiness false; none is an act-validity case."; the list is
   47–58 and holds exactly **ten** entries, `resource-breach` ninth.
   `ReadinessPopulation` is 83–89; arm 9's condition and message are
   365–366; `readinessPopulation` is 211–220 [Observed].
7. **The registry and the types.** `PwbResourceLimits` is
   `project-shape-observation.ts` 65–73 with **7** fields, of which
   `maxHumanResponseBytes` (**71**) and `maxMachineResponseBytes`
   (**72**) are output-side; `ResourceLimitBreach` is 204–210 with
   `limit: keyof PwbResourceLimits` at **205**. The registry declares
   both at lines **270–271** and gives their semantics at **279–280**;
   `breachResult` is line **281** and the packet quotes it verbatim. The
   file's current sha256 equals the digest recorded in
   `.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`
   — compared this session, neither value reproduced [Observed].
8. **The state directory.** `packages/cap1-system/src/state-dir.system.test.ts`
   line **294** is `expect(readdirSync(benignTarget)).toEqual(['machine-credential.token'])`;
   `packages/cap1-daemon/src/server.ts` 28–30 states the same invariant
   in prose [Observed].
9. **The act-binding sweep.** Denominators re-counted at `a9f671e`:
   **538** tracked `.md`/`.txt` files under `.syzygy/` and **24** files
   whose basename contains `MANIFEST`. Result: **0** manifest rows name
   any of the fourteen implementation-plane files, and the only
   governance file naming any of them is
   `.syzygy/governance/contracts/candidates/pwb-truth-policy-amendment/IMPACT-LEDGER.md`
   at lines **61** (`model.ts`), **66** (`main.ts`), **67** (`routes.ts`)
   and **69** (`polaris.ts`), with its "Candidate review input — never
   authority" banner at 3–5 and the fifth-consumer row at **71**. Its
   basename returns **0** hits in both sibling manifests in its own
   directory [Observed]. The packet's fourteen is reproducible: the
   Gate 3 section carries exactly 14 concrete path spans once the four
   globs and `scripts/` are removed.
10. **The collision table.** Both predicates recomputed from scratch over
    the ten sibling worktrees at the heads above. **All twenty cells
    re-derive exactly, and every "The B files" list matches the packet
    file for file, in order** [Observed]. So do the load-bearing counts:
    `routes.ts` in **7** of ten Gate 3 tables, `model.ts` in **6**,
    `polaris.ts` in **6** (the figure the packet's review-1 section says
    the record carries and the prose does not), M8 largest at **9**. The
    defect is in the predicate itself — G1.
11. **Contract quotations, spot-checked at the cited line (rule 8).**
    VIS-1 at `vision.md` **82–94** and VIS-2 at **96–106**, both quoted
    exactly with marked elision; VIS-2's currency sentence at **101–103**
    spans those lines exactly. SEC-1's machine-client sentence spans
    **14–16** exactly and its violation phrase "a machine client admitted
    on loopback location alone" is on line **23**, inside both cited
    spans (21–23 and 10–23). SEC-5 at **54–60**. RFC5-3 at **101–107**
    under the `###` heading at 99, quoted whole and exactly, with the
    exhaustiveness paragraph at 109–117. **The RFC2-26 block quote is
    identical to lines 196–221 of
    `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`,
    both paragraphs, no elision** — compared programmatically after
    normalizing whitespace and emphasis [Observed]; its heading is at
    194 and the scope sentence at 219–220. PWB-REQ-006 lines 378–384 and
    386–391 and 394–396 and 404–408 and 419–426, PWB-REQ-021 lines
    964–968 and 975–977 and 992–993 and 1009–1015, PWB-REQ-020 line 902
    with its scenario at 928–933, POC-REQ-032 at 574 with its scenario
    heading at 599, POC-REQ-060 at 927 and POC-REQ-061 at 966: every one
    is exact at the line cited, and every quoted THEN limb is verbatim.
    `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`
    **59–61** and the continuation act's **150–156** and **154–155** are
    exact; the improvement-cycles direction's **55–56** and **23–24** are
    exact; `POLARIS-POST-CEILING-CORRECTION-AUTHORIZATION.md` is 30 lines
    with its single authorized edit at 19–22. CC-REV-2's heading is
    `review-and-documentation.md` line **52**. M10's Q3 row is at line
    **37** of `POLARIS-M10-MACHINE-CONTRACT-FUNNEL.md` in the M10
    worktree at `95f31cb` and recommends `machine-credentialed`, and its
    Q4 is at line 38, both as the packet says [Observed, read read-only].
12. **Counts.** PWB specification **17** requirements / **31** scenarios;
    three-surface **24** / **24**; `health` as a case-insensitive
    substring: **1** line in the POC specification (596, the falsifier),
    **0** in the PWB. `tasks.md`: **35** boxes under `^- \[[ xX]\] `,
    **32** checked, **3** open, at lines 125 (4.6), 135 (5.2) and 137
    (5.3). `docs/THREE-SURFACE-POC.md` is **89** lines with **0**
    predicate-A hits and exactly the four `##` headings named.
    `package.json` declares **13** scripts at lines 12–24, none of which
    stops, restarts or upgrades a daemon; `scripts/` holds **20** `.py`
    and **0** `.sh` files. `openspec/changes/` holds five change
    directories plus `archive`. The M1 lane A record's figures — 612,665
    tailnet headroom, 654,019 trim on both forms, 1,484,487 and
    1,478,637 served, shortfalls 84,487 and 78,637 against 1,400,000 —
    are exact, and the direct headroom 618,515 is the subtraction
    [Observed].
13. **The packet's self-referential figures.** Re-derived over the bytes
    that carry them: **131,795** bytes, **1,606** `wc -l` lines, **1,553**
    non-fence lines, **0** odd-backtick non-fence lines, **374** distinct
    code spans, **36** slash-bearing spans that do not resolve, **8**
    over-78 lines under the broad predicate and **3** under the narrow
    one at 107, 142 and 704. Every figure is true of these bytes, and the
    36-span partition 22 + 5 + 2 + 2 + 1 + 1 + 1 + 1 + 1 re-derives
    member by member [Observed]. The record keeps the first-draft figures
    unedited under an explicit note and puts the re-derived ones in
    `review1.packet_measured_after_review1`, whose bytes, sha256, line
    and span counts all equal mine — **no value inside a prior-bound
    block was edited in place** [Observed].

## (c) The register

- **Faithfulness.** The P-78 row renders all five questions with their
  recommended answer, their second lawful arm and their default if
  unanswered, and every one matches the packet's Q1–Q5 table **after**
  the repairs [Observed, compared limb by limb]. Q1 carries the
  one-limb heading and the branch-only P-72 description; Q4 carries "do
  not mint one" with the escalation-trigger consequence; Q5 carries the
  612,665-byte and 654,019-byte figures, both exact.
- **Verdict word and counts.** The raw's final line is exactly `Verdict:
  CONFIRM WITH EXCEPTIONS`; its findings are F1–F7 `non-blocking` and
  F8–F13 `editorial`, 0 blocking, 13 in all. The row, the blockquote,
  the packet's review-1 section and the record's `review1.counts` and
  `independent_review` all copy that word and those counts exactly
  [Observed].
- **The recount is reproducible.** Predicate `^| P-`, partitioned by the
  `##` section each row falls under: this branch gives **22** open + **5**
  acceptance-act = **27**; main at `a9f671e` gives 21 + 5 = 26. Run over
  all ten sibling registers at their own heads: **every one gives 27**,
  each adding exactly its own row — laneb P-68, m2 P-69, m3 P-70, m4
  P-71, m5 P-72, m6 P-73, m7 P-76, m8 P-74, m9 P-75, m10 P-77, which is
  the same non-sequential mapping the blockquote publishes [Observed].
  So "P-68…P-77 live only on their own branches" is confirmed on both
  sides: present on its own branch, absent from main.
- **Hygiene.** No 12-or-more-character hex run and no `sha256` token
  occurs in the row or the blockquote; every code span in both is a
  vocabulary token, a short commit id, a worktree name, a route, a
  predicate or a `docs/` path that resolves. No observed-repository path
  is backticked [Observed].

## (d) The five questions

| # | Scope truthful? | Genuine hard human gate? | Recommendation follows? | Every lawful arm named? |
|---|---|---|---|---|
| Q1 | **Yes.** SEC-1 and RFC5-3 quoted at their clauses; the route table computed, not transcribed; `browserRequestAllowed` at `apps/three-surface-poc/src/browser-origin.ts` 26–38 does admit an absent `Origin`, so the premise holds | **Yes.** Which reading SEC-1 bears is a doctrine question no delegate may settle, and the packet says so explicitly | **Yes**, and conservatively — it recommends the narrower class and states the operability counter-argument at full strength | **Yes.** Two arms plus a default that ships neither; the prior route-existence question is correctly handed to M5's Q1 and not re-asked |
| Q2 | **Yes.** The `breachResult` sentence is verbatim at registry line 281 and those bytes are act-bound; the three `\blogs?\b` sink clauses are real and correctly attributed after F6 | **Yes.** It is the reading of an act-bound sentence | **Yes.** The specification's scenario limb does narrow the prohibition to success-shaped output, and the counter-argument is preserved | **Partly.** Two arms are named on the "no" side and the default is the narrower of them, but the "yes" answer — the registry forbids the line, so slice 1 logs no breach — is left implicit in the question rather than named as an arm. Not a finding: the question is a yes/no and the yes is on its face |
| Q3 | **Yes.** Both quoted sentences are exact, the ceilings are inside PWB-REQ-006 by line 378–379, and the evaluator really does read only `population.limitBreaches` | **Yes**, and it is the central one. Implementation-versus-amendment decides whether CC-REV-2 and a new act are needed | **Yes.** And the residue is not smoothed: PWB-REQ-006's Oracle line is quoted as a genuine two-oracle reading the packet declines to resolve | **Yes.** Conformance arm, CC-REV-2 amendment arm, and a default that does not ship slice 3 |
| Q4 | **Yes**, and its first half is answered by measurement rather than asserted. I verified all four source facts independently: the type carries both ceilings, the registry declares them, the semantics are declared, and `limit` is `keyof PwbResourceLimits`. **The dossier's prerequisite line is fairly tested and does rest on a false premise** | **Partly** — the same judgment review 1 reached. The first half the packet answers itself, and answers right; what remains is "do you want a distinct limit anyway", plus the escalation-trigger consequence if so | **Yes.** Not minting is the arm that crosses nothing, and the minting arm is named as lawful-but-gated rather than as forbidden | **Yes.** Both arms, with the registry bytes declared uneditable on either |
| Q5 | **Yes.** The five footer call sites are exactly the five lines matching `^\s*footer:` over the 45 non-test app files, there is no footer-fact function, and every headroom figure is exact against the lane A record | **Yes.** It spends a budget that is itself under open owner question | **Yes**, and it argues against its own recommendation in M1's terms | **No — see G4.** Review 1 named a third lawful arm (the status route only, not the home page). The packet reports that in its review-1 section but never carries it into Q5's row or into the P-78 register row, which are the two places the owner will read |

**No trade-off is smoothed into consensus language** [Observed]. Each
question states its counter-argument in the strongest form I could
construct from the same sources, three of the five defaults differ from
their recommendation, and no arm is called unlawful.

**Is an owner question hidden in "Decided in this packet"?** Four of the
five entries are measurements or quotations, and I re-derived each: the
prerequisite falsification, the P0-CEILING supersession, the no-derived-age
and no-green constraints, and the improvement-cycle tracing hand-off to
M10's Q4. The fifth, "No pidfile, and this is not a preference",
overstates by one step — see G7. Nothing else is a ruling wearing a
measurement's clothes.

## New findings

### G1 — non-blocking — the collision predicate silently drops continuation-form basenames, and two published claims are false because of it

`docs/design/POLARIS-M11-OPERABILITY-FUNNEL.md` lines 1215–1236.

Predicate B keeps only spans "beginning `apps/`, `packages/`, `scripts/`
or `docs/`, or equal to `package.json`". These packets write a file's
second and later mentions in continuation form — a bare basename after
one full path in the same cell. AGENTS.md records exactly this class:
"A sweep matching the full identifier misses every continuation and
produces a false absence."

Re-run this session over the ten sibling Gate 3 sections, admitting a
bare basename only when it equals the basename of a file on M11's
surface, the B column moves on **8 of 10** rows: laneb 0→2, M2 4→5,
M3 1→2, M4 6→6, M5 4→5, M6 1→3, M7 4→5, M8 9→10, M9 4→8, M10 5→5
[Observed]. Two of the section's own claims are false under it:

- The M1 lane B row's "— (its Gate 3 names no file on M11's surface)" is
  an absence claim, and laneb's Gate 3 names `polaris.ts` and
  `routes.ts` in continuation form.
- "M11 is the only packet naming `packages/three-surface-poc-core/src/resource-ledger.ts`,
  `apps/three-surface-poc/src/page-shell.ts` or `docs/THREE-SURFACE-POC.md`
  in its Gate 3 at all" is false twice over. M9's Gate 3 names
  `page-shell.ts` on two rows. And `resource-ledger` does not occur in
  **M11's own** Gate 3 section at all — it occurs at packet lines 287,
  296, 510 and in this very sentence at 1234, none of them Gate 3.

`routes.ts` is then in 10 of 10 rather than 7, and `polaris.ts` in 10
rather than 6. "M8 is the largest overlap" survives (10 against M9's 8).

**Repair.** Admit continuation-form basenames, or state in the predicate
that it counts full paths only and that the figures are therefore a
lower bound; correct the lane B row's absence claim; strike
`resource-ledger.ts` from the M11-only list and move `page-shell.ts`
out of it, naming M9.

### G2 — non-blocking — the funnel summary's re-location tally contradicts the table it summarizes

Packet line 1537 (funnel summary) against the table at lines 476–489.

The summary reads "every one of its twelve line citations is re-located
above (10 exact, 2 narrowed)". The table has 12 rows and its verdict
column tallies **9 exact, 2 narrowed, 1 "off by one, immaterial"**
[Observed, parsed row by row]. The twelfth row —
`docs/THREE-SURFACE-POC.md` lines 1–90 against an 89-line file — is
silently promoted to exact. The arithmetic still reaches twelve, which
is why it reads as sound.

This is review 1's F1 shape: a summary figure contradicted by the
packet's own table.

**Repair.** "(9 exact, 2 narrowed, 1 off by one)".

### G3 — non-blocking — "every one of the 37 lives in a `*-main.ts` entry point" is false of the 10 sites the list's own first entry holds

Packet lines 153–160 (Gate 1 measurement 1) and the Gate 4 table row for
`apps/three-surface-poc/src`.

The glob `*-main.ts` requires a literal hyphen. `apps/three-surface-poc/src/main.ts`
does not match it, and it supplies **10 of the 37** hits — more than any
other file. The packet's own answer column names `main.ts` first inside
a cell headed "All in a `*-main.ts` entry point?" [Observed, per-file
counts 10 + 6 + 6 + 5 + 4 + 3 + 3 = 37, glob tested with `fnmatch`].

The conclusion the measurement exists for — no logging call in any
request-handling path — is unaffected and I confirm it: `main.ts` is the
command-line entry point, not a handler, and `handleRequest` at
`packages/cap1-daemon/src/server.ts` 169–224 has zero on all four
branches. Only the stated predicate is wrong, which is the class review
1 called non-blocking at F3.

**Repair.** Write the predicate as "a command-line entry point — `main.ts`
or a `*-main.ts` file", or as the glob `*main.ts`.

### G4 — non-blocking — a lawful arm the packet knows about is named nowhere the owner will read it

Packet Q5 (line 42) and the P-78 row in
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` line 221.

Review 1's Q1–Q5 table found "one arm the raw says is lawful and
unnamed, Q5's third: render the status line on the status route only and
not on the home page." The packet faithfully reports that sentence in
its review-1 section at line 1414. But Q5's own row still names exactly
two arms — `pageShell` on every page, or the home page plus its own
route — and so does the register row, which is the artifact the owner
disposes from [Observed, both read this session].

The arm is materially different from the second: it is the only one that
spends **zero** bytes on any existing page, including the home page,
which is itself 38,706 bytes in the retained capture. An owner reading
P-78 cannot choose an arm P-78 does not list.

This is not a repaired-exception failure — the third arm was not among
F1–F13 — but it is a disclosure defect that survived the repair pass.

**Repair.** Add the third arm to Q5's row and to the P-78 register row,
or say in Q5 why it is not offered.

### G5 — editorial — five single-line citations anchor a quotation that wraps onto the next line

These specifications and acts are hard-wrapped, and a sentence quoted
verbatim across a wrap needs the span it actually occupies (rule 8).
Verified with `grep -n -F` on each fragment:

- "Final encoded human HTML and machine JSON SHALL each have an explicit
  byte ceiling." spans PWB spec **378–379**; cited as "line 378" at
  packet lines 40, 676, 914 and 1537.
- "any PWB-REQ-006 resource breach" spans PWB spec **967–968**; cited as
  "line 967" at packet line 676 and in Gate 1.
- "the 'machine answer' is the authenticated `GET /api/poc` response"
  begins on POC spec **25** and ends on 26; cited as "line 26" at packet
  line 38.
- The POC-REQ-032 falsifier's quoted words end on POC spec **597**;
  cited as "spec line 596" at packet lines 97 and 831.
- The specification-amendment trigger spans continuation act **151–152**;
  cited as "line 151" at packet lines 41, 676 and 1472 — and the F7
  disposition at line 1472 asserts that sub-cite is "exact", which it is
  not.

Minor sixth: `ResourceLedgerSummary`'s "complete field list, lines
82–89" (packet line 300) opens on a comment; the seven fields are 83–89.

Every corresponding **block quote** in the packet (Gate 5's 378–384 and
964–968, Gate 2's doctrine and RFC quotations) is exact, so no argument
moves. This is the mirror of F8: there a span ran past the quotation,
here it stops short of it.

**Repair.** Give each the two-line span, as F7 and F8 already did
elsewhere.

### G6 — editorial — four "the dossier" quotations live only in the pursuit JSON records, not in the file Gate 0 names as the dossier

F11 established the distinction for S10-F1 and the packet applies it
there. It is not applied to the rest. Counts this session over the three
pursuit files, in the order `.md` / `-data.json` / `-harvest.json`
[Observed]:

- "Optionally add a pidfile written at startup under stateDir and a tiny
  restart script that reads it" (packet line 130, "the dossier's S10-M3"):
  **0 / 1 / 1**.
- The `prerequisite` value "none; owner act for the registry
  resourceLimits change" (packet line 104, "The dossier gives M11 a
  `prerequisite` value of"): **0 / 1 / 0**.
- S10-M3's `maxOutputBytes` slice-plan sentence (packet lines 46 and
  310): **0 / 1 / 1**, and the source writes `'maxOutputBytes'` in
  single quotes with `resourceLimits` and `PwbResourceLimits`
  unbackticked, where the packet renders all three as code spans —
  the same normalization F8's third limb disclosed for `stateDir`.
- "the cheapest fix in the audit" (packet line 811): **0 / 1 / 1**.

`docs/pursuits/2026-09-13-vision-pursuit.md` is 553 lines and does carry
an `### M11` section and the identifiers `S7-M3`, `S10-M3` and `S10-M1`
— which is why the attribution reads as sound — but not these sentences.

**Repair.** Cite each to its file with its jq path, as F11's repair does,
or widen Gate 0's definition of "the dossier" to the three-file record
set once, at the head.

### G7 — editorial — "this is not a preference" overstates the pidfile decision by one step

Packet lines 126–140.

The basis is real and I verified both halves: `state-dir.system.test.ts`
line 294 asserts the directory's contents exactly, and
`packages/cap1-daemon/src/server.ts` 28–30 states "Nothing else is
written." But a system-test assertion and a source comment are both
implementation-plane artifacts. Neither is act-bound: the act-corpus
sweep the packet itself runs returns 0 manifest rows for `server.ts`,
and I confirm that over the same 538 + 24 denominator. An implementing
bead could lawfully change the test in the same plane the slice writes
in.

So the true statement is narrower: *given* the invariant the POC
currently asserts, a pidfile would fail an existing test, and changing
that invariant is a decision this packet declines to make. That is an
engineering judgment, well-argued — but "not a preference" claims a
constraint the sources do not supply.

**Repair.** State the invariant's status: asserted by a system test and
a source comment, bound by no act, and unchanged by this packet on
purpose.

### G8 — editorial — the CG-1b resolution claim publishes a zero without its path-candidate predicate or its denominator

Packet lines 1284–1288: "Every code span matching CG-1b's extension set
— `.md`, `.py`, `.sh`, `.yaml`, `.json`, `.txt` — resolves in this
worktree: **0** unresolved."

The extension set is stated; the rule that turns a span into a path
candidate is not, and the denominator is not published. Under the plain
reading — every non-fence code span ending in one of those six
extensions, tested with `os.path.exists` from the worktree root — there
are **47** candidates and **15** do not resolve: the glob
`docs/evidence/*.json`, the six bare extension tokens themselves, five
bare basenames (`INTERFACES.md`, `tasks.md`, two manifest names,
`PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`), the command span, `run.sh`
and the suffix `-RAW.md` [Observed]. None is a defect — every one is a
bare basename, a literal extension, a glob or a command — which is
precisely why the predicate needs stating.

`check_governance.py` reports no CG-1b failure at these bytes (tail line
32 OK, 20 WARN, 0 FAIL), so the claim is true of CG-1b's own predicate.
The defect is that a reader cannot re-derive the zero.

**Repair.** Name the path-candidate rule and the denominator, as the
neighbouring 374/36 span figures do.

## Invariants

No manifest row and no truncated signed digest is reproduced (CG-7e,
CG-15); the registry comparison is reported as a match with the record
cited by path. No observed-repository path appears in backticks or
otherwise (CG-1b). Every code span naming a repository file resolves in
`m11wt` at `9cfb31b`; spans that are globs, bare extensions, routes, a
branch name or a not-yet-written file are written without a path claim.
Every substantive claim carries [Observed], [Inferred] or [Unknown].
Every zero and every "all" above carries the predicate and the
denominator it was run over this session. All digests were computed,
never transcribed. Prose is wrapped at 78 columns with no code span
broken across a line.

**What this review does not establish.** [Unknown] Whether any
`docs/evidence/*.json` digest table binds bytes slices 2 and 3 would
edit — the packet hands that sweep to the implementing bead under
verification rule 10 and this pass did not run it either. [Unknown]
Whether the sibling branches' actual diffs stay inside the paths their
Gate 3 tables name. [Unknown] Which arm the owner takes on any of the
five questions. By verification rule 10 this review is bound to the four
digests in the header and to no later bytes; any edit retires it.

Findings: **0 blocking, 4 non-blocking (G1–G4), 4 editorial (G5–G8)**.
No finding moves a recommended answer, an arm or a default, and I
confirm the packet's claim that review 1's thirteen repairs changed
none: I compared all five questions' recommendations, second arms and
defaults against the raw's own Q1–Q5 table and against each of F1–F13.

Verdict: CONFIRM WITH EXCEPTIONS
