# R-DOV27 — response-ceiling reading packet (PR #117), fresh-context review

- Reviewed commit: `2bb75cf63d133d8c0501490b4fad9ec6539de2af` (`origin/agent/tier4-dov27`)
- Merge base with main: `3ee61c70e8cebf97f41c14af2dcbf98b2d016c25`; also re-checked as merged onto `origin/main` at `23b486c`
- Files reviewed: `.syzygy/governance/decisions/POLARIS-RESPONSE-CEILING-READING-DECISION-PACKET.md` (426 lines), `scripts/check_polaris_response_ceiling_reading.py` (352 lines)
- Reviewer: independent, fresh context, read-only. Date: 2026-09-27

## Commands run and what they returned (read, not exit codes)

- `check_polaris_response_ceiling_reading.py --check` at head: C1 15 quotes checked; C2 3 ceilings (`maxBriefingResponseBytes`, `maxHumanResponseBytes`, `maxMachineResponseBytes`); C3 137 non-test source files scanned; C4 5 questions with a default; C5 6 patches applied alone, 0 not applicable; `OK`. The same result on a merge onto `origin/main` `23b486c`.
- `--selftest`: 12/12 PASS. The C1 packet-side mutation uses `re.subn` over every wrapped occurrence, so the single-copy trap noted in AGENTS.md does not apply.
- C3 denominator checked a second way: `git ls-files 'apps/*/src/**' 'packages/*/src/**'`, filtered to `.ts`/`.mts` with tests and `test-fixtures` removed, gives **137**, which matches. A case-insensitive grep for `zlib|gzip|content-encoding|brotli|CompressionStream|deflate` over every tracked file under `apps/`, `packages/` and `scripts/` hits only the new checker, so the claim that no compression code exists holds.
- `check_governance.py` at head: `32 OK, 20 WARN, 0 FAIL (52 checks)`. At the merge base I got the same totals and the same verdict on every line. A line-by-line diff of the verdict lines shows only four denominators changing (CG-1b 6905→6909, CG-2a 1015→1017, CG-3 973→974, CG-22 536→537). No finding names the new files (0 matches for `RESPONSE-CEILING` or `check_polaris_response_ceiling`). The PR body's "same as origin/main" holds against the merge base.
- The 6 patches C5 applies: `.18` registry patch, and the `spec.md.patch` files of `pwb-exact-source-render-mode-scenario`, `pwb-machine-view-amendment`, `pwb-missing-currency-disclosure-scenario`, `pwb-opening-band-scenario` and `pwb-scoped-attributes-amendment`. Each is applied alone to the current tree. No composed order was tested (see F7).

## What holds

- **The ruling is implemented faithfully.** P-77 row, arm A: "Q2 compression needs a dated owner act on the ceiling reading before it ships". Consequences: "compression lands nowhere before its act … The registry entry is edited on no arm." The packet asks only for the reading, edits no registry byte, and its default leaves slice 4b blocked. The plain-direction instrument follows a real precedent: P-79 also says "owner act", and `POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DIRECTION.md` was issued as a plain direction ("binds no artifact digest, needs no manifest or recorder script").
- **Every quote I checked is byte-true.** The continuation trigger is at `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md:154-155`. The registry sentences and `breachResult` are at registry lines 279-281. `boundedResponse` is at `routes.ts:168`. PWB-REQ-006 is at spec lines 378-379, 400 and 424-425. The VIS-2 heading is at `vision.md:96`. The evidence figures (838-byte 503 body, observed 2132656 against declared 2097152) match `docs/evidence/polaris-m9-one-identity-funnel-2026-09-15.json:38`. The gzip figures match the funnel's table at lines 563-564.
- **The breach description is current.** `routes.ts:172` records the breach through `ServedResponseRecorder`, and `withServedReadiness` (`routes.ts:183-191`) makes readiness false. The packet's "records the breach so the status strip can show it" is accurate. It correctly departs from the funnel's older "logs nothing" wording (funnel line 225).
- **VIS-4 holds.** The banner (lines 3-11) performs nothing, and the packet offers no phrase and labels nothing accepted. The direction text is marked as a proposal. The note about where it would be recorded (line 343) says it would hold "your words verbatim".
- **The registration decision is sound.** With no subject digest there is nothing for CG-7d or CG-7e to police, and leaving the battery, the workflow and the CG-26 triple untouched is correct for a draft package.
- **The questions are genuine owner gates.** Q1 and Q4 are clearly the owner's. Q2, Q3 and Q5 are real choices inside the gate. The drafter's own choices are separated out at lines 271-281.

## Findings

### F1 — revise — The packet credits the owner with a landing order the owner did not set

Evidence, packet lines 359-362:

> This packet changes no file that any other candidate package patches, and it binds no digest, so it is **outside** the landing order you set on 2026-09-23 (`.21` → `.30` → `.22` → lane B, then `.20` and `.18`).

The owner's record, `POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md` §6 (lines 110-127), sets only ".21 → .30 → .22 → lane B" ("Readiness order, lane B last (Recommended)"). It says nothing about where `.20` or `.18` land. `.20`'s own packet says the opposite of an owner ordering: `pwb-missing-currency-disclosure-scenario/OWNER-DECISION-PACKET.md:70` reads "It would not decide the performance order of lane B, `.21`, or another PWB …". I searched the decisions directory and PROJECT-STATUS.md and found no owner record that places `.20` and `.18` after lane B.

This is an owner-facing packet stating something about the owner's own ruling that the ruling does not say. The packet's conclusion (it is outside the order) does not depend on the error, but the wrong sentence would stand in a record the owner reads.

Suggested fix: "outside the landing order you set on 2026-09-23 (`.21` → `.30` → `.22` → lane B). It is equally independent of `.20` and `.18`, whose order that ruling does not fix."

### F2 — note — The fairness argument leaves out the registry's own contrast between "UTF-8" and "HTTP body"

Acceptance criterion 2 asks for both readings to be stated fairly. Packet line 153 defines Reading 1 as "the response in its final character encoding (UTF-8)". The same `resourceLimitSemantics` object says "UTF-8" explicitly when it means the character encoding. At registry line 275, `maxBytesPerSource` reads "the exact UTF-8 blob before classification or parsing". By contrast, lines 279-280 say "the final encoded HTTP body". A reader could take that contrast as evidence that the author meant the body as sent, which is Reading 2.

The packet admits the HTTP-vocabulary lean at lines 166-170 and "at least as well" at line 183, but it never gives the owner this in-document evidence.

Suggested fix: add one `[Observed]` bullet under Reading 1's "Cost" quoting line 275 beside lines 279-280, with no conclusion drawn.

### F3 — note — The SEC-3 warrant claim is not quoted (rule 8)

Packet lines 188-189 say that loosening the ceiling "loosens a safety limit that PWB-REQ-006 names SEC-3 as its warrant for". This is true: the spec's `warrants:` block at lines 429-431 reads `primary: SEC-3`, and `GOVERNING-DEPENDENCIES.md:18` maps `SEC-3` to PWB-REQ-006. But the packet neither quotes nor cites the clause, and the checker's QUOTES list does not cover it.

Suggested fix: quote `primary: SEC-3` with its spec path and add it to QUOTES.

### F4 — note — "14 times inside" is applied to the wrong page

Packet lines 176-178: "the funnel's largest human page is about 14 times inside it once compressed". The funnel's measured human page, 1,478,637 bytes, compresses to 105,850, which is about 19.8 times inside the 2,097,152 ceiling. The 14× figure (13.66) belongs to the refused 2026-09-13 page (2,132,656 bytes), and it is an extrapolation at the 7.2% ratio rather than a measurement (funnel lines 566-573). The packet's own line 126 gets this right.

Suggested fix: "the refused 2026-09-13 page would be about 14 times inside it at the funnel's measured ratio; the measured page is about 20 times inside".

### F5 — withdrawn — "`syzygy-dov.24` … in drafting" is accurate

Packet line 82 says "another in drafting (`syzygy-dov.24`, the loaded profile)". The bead shows `OPEN` with no start date, which first read to me as undrafted. However, the local branch `agent/tier4-dov24` exists: at `5483ba9`, "draft the loaded-profile registry amendment candidate [syzygy-dov.24]", committed 2026-09-27. So the claim holds. The only gap is that it has no path the owner can follow.

Optional: cite the branch or PR once one exists.

### F6 — note — The slice-4b test list leaves out conditional GET, and the packet never addresses security posture

- **Conditional GET.** Weak conditional GET (slice 4a, `a971361`) is already on main. The packet's "Tests that must exist" (lines 384-389) says nothing about how 304 and ETag behave once content coding is in play. Specifically: whether one weak ETag is shared across codings, and whether a 304 carries `Vary: Accept-Encoding` whenever its 200 would.
- **Security posture.** The continuation act's escalation triggers include "a change to security, privacy, or retention posture". The packet never says whether any response body carries a secret, which is what compression side channels (BREACH class) would reach. I found that the served body carries only a `credentialProvision` label (`'minted' | 'reused'`, `routes.ts:199,214`) and no credential. So the risk looks absent `[Inferred]`, but the packet should say so and label it.

Suggested fix: add both cases to the test list, and add one labelled bullet under "What is true today" stating that no response body carries a credential, with its sweep.

### F7 — note — Gaps in the checker

- **C3 turns off on the file's existence, not its content.** It stays off after a withdrawal, and after a direction that answered Q1 (c) or picked a narrower arm. The direction's paragraph 7 ("on withdrawal no response is compressed") then has no mechanical guard. Suggestion: key the gate on a parsed `[Q1]` answer, or turn the sweep back on when a withdrawal record exists.
- **C3's pattern misses some forms.** It does not match `CompressionStream('deflate')` or `createBrotliCompress` unless a `zlib` or `gzip` token also appears nearby. Suggestion: add `CompressionStream` and `brotli` without the leading `\b`.
- **C5 applies each sibling patch alone to the current tree.** The packet's claim that it can be issued "before, between or after any of those acts" (line 377) rests on that alone-application plus C1 being re-run after each act. That is stated, but the packet should say plainly that composed application was not tested.

### F8 — note — Some of the fail-closed defaults are actually affirmative

- Q3's and Q5's defaults equal their recommended arms, and Q5 (a) is affirmative (gzip may ship). This is only harmless because Q1's default blocks everything. Acceptance criterion 4 says "every default is the fail-closed one".
- The drafter's argument for a plain direction over a digest-bound act (lines 61-95) is sound. But P-77's word is "act", and the packet offers the alternative only as "say so" rather than as a question with a default.

Suggested fix:
- Add one sentence stating that the Q2-Q5 defaults take effect only once Q1 is answered (a) or (b).
- Make the choice of instrument an explicit item in the issue option, the way the retention direction recorded "Issue now, with these answers".

### Out of scope, for the lead

AGENTS.md "Notes to self" ("A response-ceiling breach serves nothing and logs nothing … no ledger, stderr line or status record sees it") is stale against `routes.ts:172` and `served-response-recorder.ts`. The funnel inherited the same wording at line 225. This packet is correct and they are not.

## Rule 1-10 sweep

- Rule 1: the checker uses Python `re`, not grep classes.
- Rules 2 and 9: the 137-file absence claim was confirmed by a second method (above).
- Rule 3: the packet carries no digest, and C4 enforces this.
- Rule 4: C5's denominator (6) was checked against the enumerated patch population (7 `.patch` files under `*/proposed/` targeting quoted-file families; the one excluded, `polaris-edit-repair-deletion-scenario`, targets a different spec).
- Rule 5: the P-79 precedent is used as an argument, not as authority.
- Rule 6: all 12 selftest mutations fail as expected.
- Rule 7: I did not run the full PROJECT-STATUS battery in a clone. I ran only `check_governance.py` and the packet checker in detached worktrees.
- Rule 8: F3.
- Rule 10: this review is bound to `2bb75cf`.

The only revise-severity finding is F1.

Verdict: REVISE
