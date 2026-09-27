# R-DOV27-2 — confirmation review of PR #117
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 36f0aa85a27acfc0ac3fc7ad30f074e60d6026b5
Packet sha256: 22f5e35c47dd387750931fbcf8c813c8ff325315c7428d7d8dddc14290988b49

- Branch: `origin/agent/tier4-dov27`. Base: `origin/main` `23b486c`.
- Subject: `.syzygy/governance/decisions/POLARIS-RESPONSE-CEILING-READING-DECISION-PACKET.md` (504 lines), `scripts/check_polaris_response_ceiling_reading.py` (470 lines), the retained round-1 raw `docs/reviews/R-DOV27-RESPONSE-CEILING-PACKET-RAW.md`, and its partition row.
- Reviewer: fresh context, read-only, working in a detached worktree. Date: 2026-09-27.
- The packet sha256 above was computed by `sha256sum` on the file at `36f0aa8`.

## Commands run and what their output says

- `check_polaris_response_ceiling_reading.py --check` at `36f0aa8` [Observed]:
  - C1: 17 quotes checked.
  - C2: 3 ceilings.
  - C3: 137 non-test source files scanned.
  - C4: 6 questions, each with a default.
  - C5 alone: 6 applied, 0 not applicable.
  - **C5 composed: 5 applied; not applicable on top: 1.** The one that does not apply is `pwb-scoped-attributes-amendment/proposed/spec.md.patch`, which is lane B.
  - Result: `OK`. See N1.
- `--selftest` [Observed]: 19/19 PASS.
- `check_governance.py` [Observed]: `32 OK, 20 WARN, 0 FAIL (52 checks)` at head, and the same at base `23b486c`. I diffed the two outputs with digits stripped. The only difference is the repo-root line. There are 0 lines matching `RESPONSE-CEILING|check_polaris_response_ceiling|R-DOV27`.
- `check_governance.py --selftest` [Observed]: `265 fixtures, 0 failing`.
- `check_docs_review_campaign_partition.py --check docs/README.md` [Observed]:
  - Second-method pass: `git ls-files=242; git ls-tree=242`.
  - Partition pass: `denominator=242; assigned=242; unmatched=0; overlaps=0; campaigns=54`.
  - The new row cites `R-DOV27-RESPONSE-CEILING-PACKET-RAW.md:105`. That line is `Verdict: REVISE`, so the citation is correct.
- The retained round-1 raw [Observed]:
  - It is byte-identical to the reviewer's original file (the sha256 prefixes match).
  - It cites commit `2bb75cf`, which is not on the branch. The branch has `7b6de7c`. I checked with `git rev-parse`: `2bb75cf` and `7b6de7c` carry identical blobs for both the packet (`2013e40e…`) and the checker (`371009dd…`), so this is a rebase. The citation is provenance only and is correct in substance.

## F1–F8 resolution

| Finding | Round-1 severity | Resolved? | Evidence |
|---|---|---|---|
| F1 landing order | revise | **Yes** [Observed] | Packet :410-413 now reads "`.21` → `.30` → `.22` → lane B", with `.20` and `.18` stated as unordered. The source is `POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md:114-118`: the owner's verbatim answer is "Readiness order, lane B last (Recommended)", and the option as presented was ".21 → .30 → .22 → lane B". The packet no longer attributes anything more to the owner. |
| F2 UTF-8 contrast | note | Yes [Observed] | Packet :204-210. `maxBytesPerSource` is quoted, and the quote is in QUOTES (the per-source UTF-8 sentence) and present in the registry. No conclusion is drawn. It sits under Reading 2 rather than Reading 1's Cost, which is fine. |
| F3 SEC-3 warrant | note | Yes [Observed] | Packet :216-217. The spec's `primary: SEC-3` at line 430 lies inside PWB-REQ-006 (the heading is at :340, and it is the only `primary: SEC-3` in the file). The quote is in QUOTES. |
| F4 14× / 20× | note | Yes [Observed] | Packet :195-199. My arithmetic: 2,097,152 / 105,850 = 19.8. And 2,132,656 × 0.072 = 153,551, which gives 13.66×. The packet labels the second figure an extrapolation. |
| F5 | withdrawn | n/a | No change was made. |
| F6 conditional GET + security | note | Yes, with N4 [Observed] | The tests are at :442-447 (304 `Vary`, a shared weak ETag with cross-form `If-None-Match`, an empty uncompressed 304). The credential sweep is at :138-154; I re-derived it below. |
| F7 checker gaps | note | Partly; see N1–N3 [Observed] | C3 now gates on direction content and reopens on withdrawal. The regex is widened. Composed mode exists. The disposition overclaims on three points: "every patch … composed" (lane B is not composed), "each has a new selftest" (the `brotli` term alone has none), and "permits a coding" (substring matching accepts negated text). |
| F8 defaults / instrument | note | Yes [Observed] | Packet :224-227 says the Q2–Q5 defaults are inert unless Q1 is (a) or (b). Q6 at :304-316 defaults to "no instrument", which blocks compression whatever Q1 says. Acceptance criterion 4 holds: Q1 unanswered blocks, and Q6 unanswered blocks. |

## Re-derivations (rules 2, 8, 9)

- **F6 credential sweep, second method** [Observed]:
  - I built the population with `git ls-files -z 'apps/*/src/*' 'packages/*/src/*'`, filtered to `.ts`/`.mts`, and excluded `.test.`, `test-fixtures`, `dist` and `node_modules`. That gives **137** files. The only other suffix tracked under those trees is one `.mjs`, which the packet correctly excludes from "TypeScript".
  - Python `re` over that population finds 9 lines.
  - `grep -nF -e expectedToken -e provision.token -e .token` over the same file list also finds **9**.
  - The 9 lines:
    - `design-tokens.ts:42`
    - `restart.ts:85`
    - `admission.ts:34`
    - `credentials.ts:31`, `:174`, `:283` and `:290`
    - `server.ts:207` and `:255`
  - `verifyCredential` returns an `AdmissionResult`: `{admitted:true, clientClass:'machine'}` or `{admitted:false, served:'nothing'}` (`admission.ts:13-15`). No token is returned.
  - `credentialProvision` is at `routes.ts:199,214`.
  - The packet's description of the 9 lines leaves out the two `verifyCredential` internals (`credentials.ts:283,290`) and the second file-name occurrence (`restart.ts:85`). None of these changes the conclusion.
- **Compression absence** [Observed]: the widened pattern `zlib|gzip|content-encoding|brotli|deflate|CompressionStream` (case-insensitive), run by `grep -niE` over the same 137 files, finds 0 lines.
- **Rule 8 quotes at source** [Observed]:
  - "Q2 compression needs a dated owner act on the ceiling reading before it ships" is on rulings line 65, which is the P-77 row.
  - "The registry entry is edited on no arm." is on lines 65 and 66. Line 65 is P-77's own row.
  - "a retention-posture change needing an owner act before slice 1" is on line 67, the P-79 row.
  - "dated owner act" is also on line 65.
  - The continuation trigger is at `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md:150-157`.
  - The VIS-2 heading is at `vision.md:96`.
  - `Buffer.byteLength(body, 'utf8')` is at `routes.ts:168`.
  - C1 confirms all 17 quotes are present in their sources and in the packet.
  - Note that C1 searches whole files, not rows. I confirmed row placement by hand for the three rulings quotes.
- **VIS-4** [Observed]:
  - The banner at :3-11 is intact.
  - There is no act phrase and no digest (C4).
  - The direction text is a template (`Date: <date issued>`).
  - The record note (:394-398) says "your words verbatim".
  - Nothing claims adoption.

## Rule-6 mutations run by this reviewer (throwaway copies only)

**Behavioural mutations on fixtures** (built with `_fixture_root`, then `check()`):

| Id | Mutation | Findings | Wanted | Result |
|---|---|---|---|---|
| M0 | The packet's own fenced direction text is issued verbatim and gzip code lands | 0 | 0 | ok |
| M0b | The Q1(b) variant ("as sent, after any HTTP content coding") is issued (replacement confirmed to occur) | 0 | 0 | ok |
| M1 | The direction reads "WHAT MAY SHIP. Nothing. gzip is not permitted." | **0** | C3 | **fail-open** |
| M2 | A Q1(c) decline that quotes "before any HTTP content coding is applied", with "No gzip, no brotli." | **0** | C3 | **fail-open** |
| M3 | A withdrawal record in `decisions/sub/W.md` | **0** | C3 | missed |
| M4 | A later record narrows the direction to "no coding may ship" | **0** | C3 | missed |
| M5 | A gzip-only direction, with `createBrotliCompress` landing | **0** | C3 | missed (coding scope not enforced) |
| M6 | A decisions file names the direction and says "withdrawal defeats grant" elsewhere | 1 | 0 | spurious close (fail-closed) |
| M7 | `import compression from 'compression'` | 0 | C3 | missed |
| M8 | `const enc = 'br'` | 0 | C3 | missed |
| M9 | `.js` under `src/` requiring `zlib` | 0 | C3 | missed (out of population) |
| M10 | "gzip" appears only under paragraph 3 | 1 | C3 | ok (paragraph scoping works) |

**Code mutations on the checker, then `--selftest`:**

| Id | Mutation | Selftest result |
|---|---|---|
| K1 | Drop the withdrawal reopen | killed |
| K2 | Drop the Q1-reading requirement | killed |
| K3 | Drop the coding requirement | killed |
| K4 | Drop the MAY_SHIP requirement | crash (killed) |
| K5 | Revert the regex to its round-1 form | killed |
| K7 | Disable the composed-quote check | killed |
| K8 | Compose only the first patch | killed |
| K9 | A missing direction permits | killed |
| K6 | Drop `CompressionStream` alone | **survived** |
| K11 | Drop `brotli` and `deflate` | **survived** |
| K12 | Drop `brotli` and `CompressionStream` | **survived** |
| K13 | Drop `deflate` alone | **survived** |
| K10 | Search the coding over the whole direction instead of paragraph 2 | **survived** |

K6, K11, K12 and K13 survive because the one selftest line, `CompressionStream('deflate')`, is caught by either of two terms, so no single new term is pinned. The `brotli` term has no selftest at all.

**Owner-order composition, run by hand** [Observed]: I applied `.21` (opening band), then `.30` (exact source), then `.22` (machine view), then lane B (scoped attributes) to the spec in a scratch copy. All four applied. All five PWB-REQ-006 quotes survive, checked under the checker's own `normalize`. I also paired the patches: `.20` (missing-currency) followed by lane B does **not** apply (`git apply` rc=1), while each of `.21`, `.30` and `.22` followed by lane B does.

## New findings

### N1 — note — The "composed" claim is labelled [Observed], but the check never composed lane B

Packet :425-428 says:

> `[Observed]` None of their current proposed patches touches those sentences, applied alone or composed in sequence (the check does both).

The disposition at :487 says "C5 also applies every patch to a quoted file composed in sequence".

The check's own output says lane B was **not applicable composed**. The cause is that C5 composes in path order (`scripts/check_polaris_response_ceiling_reading.py:292-295`, sorted by package name). That order puts `.20` before lane B, and those two conflict.

The substantive claim is true: my owner-order run above composes all four and keeps every quote. But it is not what the check shows. Rule 4 says to read the output, not the exit code, and `OK` hides the skip.

Suggested fix, either of:
- Compose in the owner's ruled order (`.21` → `.30` → `.22` → lane B).
- Reword the packet to say that the check composes in path order and that lane B does not apply on top of `.20`.

### N2 — note — The C3 gate is a substring test, so negated or declining text opens it

This is M1 and M2 (`direction_permits`, :173-192):
- `READING_ANSWERS` matches anywhere in the direction, so a decline that quotes the reading opens the gate.
- `CODING` matches any mention of `gzip` in paragraph 2, including "not permitted".

The gate also does not see:
- a withdrawal filed in a subdirectory (M3), since the scan uses `os.listdir` and is not recursive;
- a narrowing record (M4); the packet's own paragraph 7 names "narrow or withdraw", but `WITHDRAW` has no narrow form;
- the coding scope (M5): once a gzip-only direction exists, Brotli code passes.

In the other direction, M6 closes the gate spuriously. `PENDING-OWNER-DECISIONS.md` already contains `withdr` (9 of the 75 top-level decisions `.md` files do), so the gate will close if the register ever names the direction file. That failure is fail-closed.

The disposition's "permits a coding" is true only for well-formed directions. None of this is exploitable without an owner-authored record, and the owner direction and slice-4b review remain the real gate. That is why this is a note.

Suggested fix, any of:
- Key the gate on a fixed marker the direction text carries, for example the literal paragraph-2 first clause.
- State the limits in the docstring.

### N3 — note — The widened regex terms are not individually pinned

Three terms have no single-term selftest:
- `brotli` has no selftest line.
- `deflate` and `CompressionStream` share one line, so K6, K11, K12 and K13 survive. That line is `_land_compression(r, "const cs = new CompressionStream('deflate');")`, at checker :432.

K10 also survives: M10 shows that paragraph-2 scoping works, but no selftest pins it.

Separately, M7 to M9 show that a third-party `compression` import, a `'br'` literal and `.js`/`.mjs` sources lie outside the sweep. [Inferred] That is acceptable if the packet's words ("mentions `zlib`, `gzip` or a `Content-Encoding` header", :108-110) are what the check claims. The disposition's "in any form" (:487) overstates it.

Suggested fix:
- Add one selftest line per term.
- Either soften "in any form" or extend the sweep.

### N4 — note — The credential bullet does not connect to the security-posture trigger

The continuation act's triggers (:150-157) include "a change to security, privacy, or retention posture". The packet now explains BREACH-class risk and says "no secret in any body" is not claimed (:150-154). But "Why an owner act is needed" (:50-59) and direction paragraph 1 ("answers … and does not widen") address only the registry-envelope trigger.

[Inferred] Whether compressing Butlers-derived text that the detectors did not flag is a security-posture change is an owner question the packet leaves implicit. Criterion 3 asks the instrument argument to hold "against the continuation act's triggers", which is plural.

Suggested fix:
- Add one sentence saying whether the drafter holds that the security-posture trigger is crossed, and why.
- Or add it as a question with a fail-closed default.

The 9-line enumeration at :144-146 also leaves out the `credentials.ts:283,290` and `restart.ts:85` hits. This is cosmetic.

### N5 — note — A cross-reference points the wrong way

Packet :446-447: "The shared weak ETag is the drafter's choice, listed below." The list is **above**, in "What is the drafter's and not yours", item 4 at :329. This is an editorial slip.

## Rules 1–10

- **Rule 1:** the checker and my sweeps use Python `re` or `grep -F`. The one `grep -E` sweep has no bracket classes.
- **Rules 2 and 9:** 137 files and 9 lines are confirmed by two methods, and 0 compression lines by two methods.
- **Rule 3:** the only digest here is scripted.
- **Rule 4:** read the C5 skip line (N1).
- **Rule 5:** the P-79 precedent is argued, not cited as authority.
- **Rule 6:** see the M and K tables above.
- **Rule 7:** I did not run the full PROJECT-STATUS battery. I ran the four named checks in detached worktrees at `36f0aa8` and `23b486c` only.
- **Rule 8:** quotes were verified at source and row.
- **Rule 10:** this review is bound to packet sha256 `22f5e35c…` at `36f0aa8`. Any repair of N1–N5 retires it.

There are no revise-severity findings. F1 is resolved, and F2–F8 are resolved with the exceptions noted in N1–N3.

Verdict: CONFIRM WITH EXCEPTIONS
