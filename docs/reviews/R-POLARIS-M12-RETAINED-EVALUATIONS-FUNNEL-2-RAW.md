# Review 2 — Polaris M12 retained-evaluations funnel packet

Independent fresh-context review. Read-only: no tracked file, worktree or
`node_modules` was modified; `git status --short` was empty in the M12
worktree before and after, and in every sibling worktree opened. No daemon
was started, no provider was called, no repository body was read. The
retained captures were read with Python only, and no observed-repository
path or content is reproduced here.

## Subject

Worktree `…/scratchpad/m12wt`, branch `agent/syzygy-dov.12`, HEAD
`4d61b73cdd8d750fb9bea72b3de5282874181d30`.

| File reviewed at `4d61b73` | Bytes | sha256 |
|---|---:|---|
| `docs/design/POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL.md` | 166846 | `528f8eb8fa1cc90e504a689e2f91f0925fd7beda55b694713ca096cf58468ba0` |
| `docs/evidence/polaris-m12-retained-evaluations-funnel-2026-09-15.json` | 50409 | `70a1c880dd1af410d744ffd6b6d04fedf74134dac7197646ae7b7c07ecb0de8a` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 34027 | `8dc39326a8d39f7e5cb8f0167126163a4ddeca18b2839ee74ae6e8ba36e90c34` |
| `docs/reviews/R-POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL-RAW.md` | 34220 | `549b38f1654b0bc33fc6329aae8b9747fb91260e63405ac6c393cf9ca84e2605` |

Predecessor bytes, recomputed by `git show a55fe3a:<path>` piped to `wc -c`
and `sha256sum` — both match the packet's own table exactly [Observed]:

| File at `a55fe3a` | Bytes | sha256 |
|---|---:|---|
| the packet | 136105 | `d65c7860608bf8f1520c27ff71501bd9e8861c840aeec0177e2a70e0f58ab924` |
| the evidence record | 31585 | `9765554e546c159b676df90b702984211cd9e7c2ac5c1361c52222cb3b28485f` |

Sibling worktree heads read read-only this session, each matching the head
the packet names [Observed]: `laneb` **4090f98**, `m2wt` **f2f37dd**,
`m3wt` **6574600**, `m4wt` **63b8e33**, `m5wt` **ba9ca61**,
`m6wt` **83c9f60**, `m7wt` **f97baf4**, `m8wt` **bce9039**,
`m9wt` **65de02b**, `m10wt` **95f31cb**, `m11wt` **bbd6837**. Eleven of
eleven as expected.

`python3 scripts/check_governance.py` was run in the worktree and its tail
line read, not grepped:
`32 OK, 20 WARN, 0 FAIL (52 checks) — counts derived, not asserted`
[Observed]. `npm run build:poc` and `npm test` were
not run: the packet proposes no code change and makes no claim about test
outcomes, so neither would test anything the artifact asserts. Stated
rather than left implicit.

## Review-1 repair verification, F1–F12

Every figure below was re-derived from source or from the retained
captures this session, not read from the packet or the record.

| # | Sev | Verdict | Evidence |
|---|---|---|---|
| F1 | blocking | **REPAIRED** (one residual, G1) | `docs/pursuits/2026-09-13-vision-pursuit.md` 415–416 read at `a9f671e` carry `(retention posture)`. The packet block-quotes the full line at `:106-107` and carries the parenthetical in the re-split paragraph at `:74-75`; the literal `retention posture` now occurs **7** times in the packet and **4** in the record (dossier **1**) [Observed, `grep -F`]. The record keeps `dossier.prerequisiteLine` unedited at `:62` and adds the dated sibling `prerequisiteLine_note_2026-09-15` at `:63` naming the elision; `prerequisiteVerdict` likewise gains `prerequisiteVerdict_note_2026-09-15` at `:66`. The "reached without the trigger list being read" ruling survives only inside dated superseded-wording markers — packet `:128` (inside `[Until 2026-09-15 …]`, followed by "**The ruling is withdrawn.**"), `:1947` and `:1965` (both marked), the F1 disposition row `:1865`, record `:942`, register `:130`; **0** live sites [Observed, `grep -F` over all four files]. Q1's row: the recommendation cell is **byte-identical** to `a55fe3a`, as are Q2, Q3, Q4, Q5 and Q6's; only Q1's and Q3's *question* cells differ, and a word-level diff shows the interrogative sentence, the continuation-act quotation, the three arms and the default are untouched — the changes are the F2/F3/F4 and F6 figures plus their superseded-wording markers [Observed, `git show a55fe3a:<packet>` diffed cell by cell] |
| F2 | non-blocking | **REPAIRED** | Recursive walk over `…/scratchpad/capture/api-poc.json` for every object carrying both `claimId` and `epistemic`: **1,149** objects, **1,148** distinct identities, **1** identity twice. Distinct identities by prefix 278 / **415** / 439 / 9 / 6 / 1 = **1,148**; claim objects 278 / **416** / 439 / 9 / 6 / 1 = **1,149**. `claim:fact:` decomposes 415 `item:` + 9 `count:` + 9 `catalog-count:` + 6 `project-account:` = 439. Distinct (epistemic, challenge) tuples **2**, at **1,137** and **12**. Both rows are published in the packet at `:575-583` and in the record as `byIdentityPrefix_distinctIdentities_2026-09-15` and `byIdentityPrefix_tupleInstances_2026-09-15`, with the original `byIdentityPrefix` kept unedited beside a dated note [Observed] |
| F3 | non-blocking | **REPAIRED, and the repair worker is right against the raw** | `grep -F 'claimId:'` over `packages/three-surface-poc-core/src/project-shape-model.ts` returns **13** lines: six interpolating (367, 375, 383, 403, 430, **447**), **4** fixed literal `'claim:project-shape'` (345, 457, 611, 659), **2** interface declarations (123, 157) and **1** pass-through (173); 6+4+2+1 = 13 [Observed, every line read]. Review 1's raw at `:128-134` states "twelve `claimId:` lines … the remaining six are the fixed literal"; **that half is wrong** and the packet records it as not confirmed at `:170-174` and in the record's `claimIdConstructionSites_note_2026-09-15` rather than copying it. Line 447 is the Unknown arm of `projectAccountOf` and interpolates the same closed-vocabulary account key as 430, so the conclusion is unchanged |
| F4 | non-blocking | **REPAIRED, and the partition re-derives to the identity** | The 1,148 split **1,117** / **30** / **1**. 1,117 = 278 source paths + 415 item class-and-key pairs + their 415 `claim:fact:item:` twins (the twin key set is set-equal to the item key set) + 9 catalog headings. 30 = 9 `claim:class:` + 9 `claim:fact:count:` (every suffix a member of `EXTRACTION_CLASSES`, nine values at `project-shape-manifest.ts` 58–68) + 6 `claim:project-account:` + 6 `claim:fact:project-account:` (every suffix a member of `PROJECT_ACCOUNT_KEYS`, six values at `project-shape-extraction.ts` line 46). Both constants read at source; both membership tests are total [Observed]. The canonical `claimId → {epistemic, challenge}` map is **177,031** bytes and with `resolutionRoutes` **203,379**, difference **26,348** — all three reproduce to the byte under key-sorted, separator-compact JSON [Observed] |
| F5 | non-blocking | **REPAIRED, all five predicates reproduce** | Over the **246** `.ts` files under `apps/` and `packages/` excluding `dist/` and `node_modules` (denominator reproduced exactly), with the packet's stated exclusion — a line dropped only when its single occurrence of the word is `challenge-suspended`: `\bchallenge\b` case-sensitive **35**, case-insensitive **36**, case-sensitive without the exclusion **43**, case-insensitive without it **44**; the accepted case-insensitive substring predicate **50**, splitting **25** test / **25** non-test. The 50-minus-35 difference is **15**, splitting **7 non-test / 8 test**: `drawer.ts` 59, 60, 114, 138, 174 and `project-shape-model.ts` **83**, **84** against `polaris-epistemic-tuples.test.ts` 42, `polaris-first-reading.test.ts` 88, `req-040.conformance.test.ts` 163, 196, 225, 227 and `project-shape-model.test.ts` 19, 351 — the packet's enumeration line for line [Observed]. The hinge is `project-shape-model.ts` line 98, whose two occurrences keep it out of the exclusion; the packet's figures are self-consistent under that one reading and I found no other reading that reproduces all five |
| F6 | non-blocking | **REPAIRED, on both host forms** | Span predicate `<span class="claim-tuple".*?</span>` with DOTALL: the pre-trim retained page (2,090,025 bytes) carries **699** spans totalling **409,829**, mean **586.3**, min 559, max 661; each lane A after-capture (1,478,637 direct and 1,484,487 tailnet) carries **713** totalling **418,122**, mean **586.4**, min 559, max 661 — identical on both host forms and on the `review-after` pair as well. Headrooms recomputed: 2,097,152 − 1,484,487 = **612,665**; − 1,478,637 = **618,515**; 8,388,608 − 5,520,314 = **2,868,294**. 612,665 / (2 × 586.4) = **522.395…**, floor **522** [Observed]. The record keeps the pre-trim values and the withdrawn "upper bound" gloss unedited and adds dated post-trim siblings |
| F7 | non-blocking | **REPAIRED, and the enumeration is exact** | All **15** enumerated surface files resolve as files in this worktree, and the list is **element-for-element equal in order** to the record's `collision.m12_surface` [Observed]. Gate 3's four topology data rows carry **25** code spans, of which **12** resolve as files; **2** of those 12 are off the surface (`polaris-parity-sweep.test.ts`, `walkthrough-preflight.ts`) and **5** of the 15 are not among the 12 — `project-shape-observation.ts` and `walkthrough-readiness.ts` (named only in the "Not touched by any slice" prose), `body-read-authority.ts` (present in the slice-1 row as a bare basename only, confirmed), `walkthrough-judgment.ts` and `write-guard.ts` (absent from Gate 3 entirely). Every figure as published |
| F8 | non-blocking | **REPAIRED** | `git diff --name-only f4589e2 a9f671e` prints **146** paths; **0** of the twelve named files appear, tested by exact whole-line match, and `apps/three-surface-poc/src/polaris.ts` **does** appear and is not one of the twelve [Observed]. All twelve resolve as files. The superseded "nine implementation files and three governance files" wording survives only inside dated markers in the packet (`:64-69`) and the record (`:69`) |
| F9 | editorial | **REPAIRED** | `grep -F 'canonicalJson' packages/three-surface-poc-core/src/project-shape-observation.ts` returns **36** (the import member), **337** and **635**. Over `apps/` and `packages/` the identifier has **7** occurrences: 333 (definition), 338 (`canonicalManifestJson`), 22 and 126 in `walkthrough-readiness.ts`, and the three above — the packet's census exactly. Line 336 is inside `resourceLimitsDigest`, as the packet now says |
| F10 | editorial | **REPAIRED** | Read read-only at `95f31cb`: the M10 packet's line **35** is its Q1 and carries `model.test.ts`, `inputsDigest` (×4) and the word `insensitive`; line **36** is its Q2, on `Content-Encoding: gzip` and the response ceiling. The packet's corrected clause matches both [Observed] |
| F11 | editorial | **PARTIAL** — see G4 | `MATERIALIZE_ATTRIBUTION` is declared at `apps/three-surface-poc/src/materialize-action.ts` lines **28-29**, as the packet says. But the quoted comment sentence spans lines **26-27**: line 26 is "Fixed, never user-supplied —" and line 27 is "this action is human-triggered but not human-identified." The packet moved the anchor from 28-29 to 27 and is still one line short at the head [Observed, lines 24–29 read] |
| F12 | editorial | **REPAIRED** (one consequence missed, G3) | `vision.md`: VIS-6 runs **167–181** and 182 is blank; the expiry parenthetical spans **175–177**; exception (a) ends on **177**; 178–179 are exception (b)'s first two lines. So L2-M6's 176–179 and L2-M8's 170–179 each overrun by two lines, exactly as the repaired verdict cell now states [Observed] |

## Independent re-measurement of the load-bearing figures

Every one of the following was recomputed this session from source or from
the retained captures. Unless a row says otherwise it reproduces the
packet's published figure exactly.

- `main.ts`: 134 `const asOf = new Date().toISOString();`; 113 the
  `buildModel` declaration; 148 and 168 the two per-run evaluation
  identities; 171 the builder call; 175 `evaluation: { snapshot, asOf }`;
  187 and 201 the two call sites; 101–105 the `snapshot` composition;
  **253** lines by `wc -l`. All exact. **But see G2** on the stated
  occurrence predicate.
- `buildButlersPocModel(`: **36** occurrences across `apps/`, `packages/`
  and `scripts/`, **33** in `*.test.ts`; the three others are the
  definition at `model.ts` 369, the production call at `main.ts` 171 and
  `test-model-fixture.ts` 133. As published.
- State-directory write sweep: **157** `.ts` files across the three named
  trees, **81** non-test, **56** matching lines under the word-boundary
  alternation. Partition re-derived and exhaustive: **11** imports, **31**
  in the eight command-line and fixture files the packet names, **2**
  clear/delete helpers (`materialization.ts` 139 and
  `test-artifact-verification.ts` 84), **3** comment lines
  (`write-guard.ts` 13 and 16,
  `consent-loading.ts` 143), **2** the governed-plane write at
  `write-guard.ts` 187–188, **1** the `authorizeWrite` call at 152, and
  **6** the three state-directory sites two lines each (`credentials.ts`
  223–224, `materialization.ts` 129–130, `test-artifact-verification.ts`
  74–75). 11+31+2+3+2+1+6 = 56. **0** writes an evaluation, an
  observation, a claim state or a judgment [Observed, all 56 read].
- The retained capture's state directory: **one** entry, 64 bytes, mode
  `0600`, directory mode `0700`. Contents not read.
- The two appenders: quoted whole in the packet and **byte-identical** to
  source at `body-read-authority.ts` 754–767 and `walkthrough-judgment.ts`
  810–824, including the `// mutation-point: history-append-only` line at
  818. Census **5** + **6** = 11 sites, **2** definitions, **9** in
  `*.test.ts`, **0** in `packages/three-surface-poc-core/src/index.ts`.
  Neither reads or writes a file. As published.
- `canonicalJson` at `project-shape-manifest.ts` 333 with its three digest
  users at `project-shape-observation.ts` 337 and 635 and
  `walkthrough-readiness.ts` 126. Exact.
- Footer: filled at **3** sites — `routes.ts` 92, `polaris.ts` 1630,
  `polaris-source.ts` 140 — each interpolating `model.evaluation.snapshot`
  and `model.evaluation.asOf`; `routes.ts` adds the machine-endpoint
  sentence. In the retained page the rendered snapshot is **262**
  characters in one `<code>` element and the instant **24**, and the
  snapshot is a four-field `|`-joined composite. **No digest, truncated or
  whole, is reproduced in the packet, the record or the register row**
  [Observed; the field values were measured by length only].
- PWB-REQ-007: heading at spec 439, requirement text 443–446, Case line
  453–456 (naming "two evaluations of the same semantic subjects" at
  453–454 and "challenge" at 455), Oracle line 459–463 with the stable
  semantic identity clause at 460–461, the trend-and-count-wall sentence at
  450–451. All exact. The six interpolating `claimId` sites carry no
  revision — each builds a path, an item class-and-key, a fact name, a
  class name or an account key [Observed, all six read].
- `CHALLENGE_STATES` at `project-shape-model.ts` 83 under the comment at
  81–82, `ChallengeState` at 84, `readonly challenge` at 129, the single
  producer at 177. Exact.
- `.syzygy/local/` and `.syzygy/cache/`: **0** of **556** files tracked
  under `.syzygy/` at `a9f671e`, and `.syzygy/` holds three directories.
  Over the **278** distinct source paths of the retained observation, **0**
  begin `.syzygy` and **0** carry a segment `local`; the population has
  **3** top-level segments. Repository total **1,216** tracked files at
  `a9f671e` — the packet's baseline convention, confirmed (the worktree
  head carries 1,219, the difference being this pass's four files).
- PWB-REQ-022 at spec 1032–1035 names a retained walkthrough execution
  record in a Syzygy governance path; that path is **not** among
  `.syzygy/governance/`'s five directories and **0** files are tracked
  under it. Observable line at 985. Exact.
- Continuation act: the trigger paragraph is lines **150–156** under the
  `## Escalation triggers` heading at 148, and the packet's Q1 quotation is
  word-for-word (bold emphasis added by the packet, which its "verbatim"
  framing does not flag; not material).
  `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`
  70–72 is quoted exactly, and 59–61's elision is correctly
  described as the sentence's continuation running to line 63.
- VIS-6 at vision.md 167–181 (182 blank), with the expiry sentence at
  175–177; VIS-2 at 96–106; VIS-1 at 82–94. All quotations check at the
  clause. architecture.md 56–57 are the `cache/` and `local/` rows,
  217–219 the not-captured-source sentence, 221–229 the temporal rule and
  231–235 the observation-record definition. SEC-4 at security.md 47–52 and
  SEC-5 at 54–60. RFC2-26 at RFC-0002 `rendering-vocabularies.md` 196–221
  under the heading at 194, quoted whole with no elision and with the
  source's own emphasis. RFC5-11 at RFC-0005 `admission-and-boundary.md`
  244–252 under the heading at 242. Every one exact (rule 8) [Observed].
- M2's line 47 at `f2f37dd` is its Q3, recommending "A second identified
  evaluation, never a freshness value"; M10's Gate 3 row at 722 and slice 5
  at 1004ff at `95f31cb` are the `logicalId` anchor sibling. Both read
  read-only; both as cited.
- Gate 5 retention sweep: all twelve per-term counts over the two `spec.md`
  files (1,008 + 1,152 = **2,160** lines) reproduce exactly, including the
  15 `retain` hits in the PWB spec and the 0/0 rows. Requirement and
  scenario counts 17/31 and 24/24 reproduce. `tasks.md`: **138** lines,
  **35** boxes, **32** checked, **3** unchecked (4.6, 5.2, 5.3).
- Act-corpus sweep: **538** governance `.md`/`.txt` + **24** `MANIFEST`
  files + **7** `docs/evidence/` manifest files, union **553** distinct.
  Result over the 15-file surface: the only governance hit is
  `.syzygy/governance/contracts/candidates/pwb-truth-policy-amendment/IMPACT-LEDGER.md`
  (8 of the 15), whose lines 3–5 read exactly as quoted
  and whose basename returns **0** hits in both sibling manifests, plus one
  `docs/evidence/` rule-6 mutation record for `polaris.ts` whose key set is
  exactly the seven the packet lists. **0** act records and **0** manifest
  rows [Observed].
- Collision table: predicates A, B-full and B-basename recomputed from
  scratch over the eleven sibling worktrees at the heads above. **All 33
  cells reproduce exactly**, as do the file lists in the last column, the
  "moves on 7 of 11 rows" claim (M1 lane B 0→1, M2 4→5, M5 3→4, M6 0→1, M7
  1→2, M8 7→9, M9 2→6; M3, M4, M10, M11 static), every per-file frequency
  (`polaris.ts` 11/11, `model.ts` 7/11, and so on), and the three files at
  0/11. Basename non-uniqueness confirmed: `main.ts` 2 and `index.ts` 4 over
  1,216 tracked files, the other thirteen unique [Observed].
- Self-referential conventions: **166,846** bytes, **2,019** lines by
  `wc -l`, **1,931** non-fence lines, **8** over-78 non-pipe non-fence
  lines, **0** odd-backtick non-fence lines, **401** distinct code spans of
  which **108** carry a `/` and **32** do not resolve. The 32 partition
  exactly as published — 4 declared absences, 3 proposed modules, 6 tree
  globs, 2 `<name>` placeholders, 2 route paths, 4 bare directory
  fragments, 4 command lines, 1 gitignored build artifact, 1 generation-kit
  path and 5 prose-or-code spans, summing to 32 [Observed, enumerated].
  **But see G5** on the accompanying "unbreakable code span" claim.

## The register

- **Fidelity.** The P-79 row's Q1–Q6 renderings match the repaired Q-table:
  every recommended answer, every lawful arm (Q1 three, Q2 four, Q4 four
  lettered, Q3/Q5/Q6 three each) and every default-if-unanswered is carried,
  and each matches the packet's wording in substance. The row's evidence
  figures — 3 write sites over 157 files, 0 evaluations written, 1 file of
  64 bytes, 0 of 2,160 lines, 1,149 / 1,148 / 1,117 / 30 / 1, 2 tuples,
  177,031 bytes, 0 of 278, 0 acts and 0 manifest rows over 15 files and 553
  — every one re-derived above [Observed].
- **Verdict word and counts.** The blockquote copies **REVISE** and
  **blocking 1, non-blocking 7, editorial 4, F1–F12**; the raw's own final
  two lines are `blocking 1 · non-blocking 7 · editorial 4` and
  `Verdict: REVISE`, and it carries exactly 12 `### F` headings with those
  severities. Exact match [Observed].
- **Recount.** Predicate `^| P-` over the current file, partitioned by the
  `##` section each row falls under: **22** under "Open, and only the owner
  can dispose", **5** under "The acceptance acts", **27** in all. Over
  `git show a9f671e:` of the same file: **21** + **5** = **26**, the
  highest `P-` number anywhere is **67**, and `P-7[0-9]` returns **0** hits
  [Observed, Python `re`]. Reproducible by the stated predicate.
- **Sibling branches.** Each of the eleven sibling worktrees' registers
  carries **27** rows, **none** carries a `P-79` row, and each carries
  exactly one row in P-68…P-78 — its own, matching the PR mapping the
  packet publishes (laneb P-68, m2 P-69, m3 P-70, m4 P-71, m5 P-72, m6
  P-73, m7 P-76, m8 P-74, m9 P-75, m10 P-77, m11 P-78) [Observed]. The
  blockquote's claim is correct.
- **Digests and paths.** The row quotes no act digest and no truncated
  signed digest; the only hashes are commit short-names. No Butlers path is
  backticked anywhere in the three artifacts, and no observed-repository
  content appears in any of them [Observed, sweep for the capture's own
  declaration labels and file names returns 0 in all three].

## New findings

### G1 — non-blocking — a ruling on Q1 survives in "Decided in this packet"

`docs/design/POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL.md:102` and
`:109-116`; also the funnel summary at `:1947`.

**Defect.** The section is headed "Decided in this packet, not put to the
owner". Its first item still opens "**The dossier's prerequisite line does
not survive as written, and the half that fails is the first half**" and
argues at `:109-116` that "The **first clause does not** [hold]: retention
is the one part of this move that touches a *named* escalation trigger by
its own noun … and slice 1 is a proposal to retain something the daemon has
never retained." The dossier's first clause is "None for retention and
delta" — whether a prerequisite is required for retention is exactly Q1,
whose second and third lawful arms rule the record inside the existing
authorization. On either of those arms the first clause survives. So the
packet's own recommended answer to Q1 is asserted as decided, in the
section that says it is not put to the owner.

The next paragraph (`:118-123`) does retract it — "Whether that trigger also
reaches slice 1's derived claim-state record is Q1, and this packet does not
rule it" — and the F1 disposition and the handoff at `:1960-1963` are clean.
But the qualification is two paragraphs below the sentence it qualifies, and
AGENTS.md's own recorded lesson is that staleness or withdrawal must be
marked **at the sentence**, not at the section. The funnel summary repeats
the unqualified form first ("the prerequisite's 'none for retention and
delta' does NOT survive") and qualifies it only in the same line's tail.

This is materially weaker than review 1's F1 — the full line is quoted
immediately above, the withdrawal is explicit, and Q1's three arms and
fail-closed default are on the page — so it is not blocking. But it is the
same residue F1 was raised about and a fresh reader meets the ruling before
the retraction.

**Repair.** Re-cast the lead sentence and `:109-116` as what Q1 asks rather
than what the packet concludes — for example "the dossier's first clause
cannot be asserted without ruling Q1, because retention is the one part of
this move that touches a named escalation trigger by its own noun" — and
make the same change in the funnel summary's opening clause.

### G2 — non-blocking — the `buildModel()` count does not
reproduce under its own published predicate

`…FUNNEL.md:361-363` and `:437-439`.

**Defect.** The packet writes "[Observed, the only two occurrences of the
literal `buildModel()` in the file …]" and then states the count again under
an explicit predicate: "under the predicate 'the literal `buildModel()`
occurring in `apps/three-surface-poc/src/main.ts`', denominator that file's
**253** lines". Run this session, that literal occurs at **three** lines —
113, 187 and 201 — because the declaration
`function buildModel(): ReturnType<typeof buildButlersPocModel> {`
contains it. The packet names
line 113 as the declaration in the same sentence, so the substantive claim
(two call sites) is correct and unaffected; the published predicate is not
the one that yields 2. This is the class of defect the packet makes a
virtue of catching elsewhere (Gate 6 item 1) and review 1 raised as F5.

**Repair.** State the predicate as the literal `buildModel()` excluding the
declaration at line 113, and publish 3 as the raw count beside the 2.

### G3 — editorial — the re-verification tally was not updated by F12

`…FUNNEL.md:1938` (funnel summary).

**Defect.** The summary reads "Of the 14 rows in the re-verification table,
10 re-locate exactly, 2 are narrowed by one line at the tail, 1 is
approximate, and 1 names the wrong construct" — 10+2+1+1 = 14. Reading the
verdict column of the table at `:767-780` this session: **9** rows are
wholly exact, 2 narrowed, 1 approximate (`materialization.ts`), 1 wrong
referent, and **1 mixed** — the `vision.md` row at `:775`, whose verdict F12
changed from "exact, all three" to "**exact for 167-181; approximate for the
other two**". The tally still counts that row among the 10 exact.

**Repair.** Publish 9 exact, 2 narrowed, 1 approximate, 1 wrong referent and
1 mixed, or fold the mixed row into the approximate count and say so.

### G4 — editorial — F11's own line anchor is one line short,
and was applied rather than re-derived

`…FUNNEL.md:1875` (the F11 disposition), `:1249` (the quoting site) and
`:888`.

**Defect.** The disposition states "The words 'Fixed, never user-supplied —
this action is human-triggered but not human-identified' are at
`apps/three-surface-poc/src/materialize-action.ts` line **27**". Read at
source: line **26** is "// still records separately as `owner`). Fixed,
never user-supplied —" and line **27** is "// this action is human-triggered
but not human-identified." The quoted sentence spans **26-27**. Review 1's
raw says "They are at line **27**" in the same words, so the finding was
applied as the raw stated it. That qualifies, in one small instance, the
packet's claim at `:1848-1851` that "Every one of the twelve findings was
re-derived against source before being applied" and that eleven "re-derived
exactly" — a re-derivation of F11 would have produced 26-27.

The declaration's own citation (lines 28-29) is correct at both sites.

**Repair.** Cite lines 26-27 for the comment at `:1249` and `:888`, correct
the F11 row, and amend the "eleven re-derived exactly" sentence to name F11
as a second partial.

### G5 — editorial — the "unbreakable code span" explanation of
the 8 over-78 lines does not hold for 4 of them

`…FUNNEL.md:1926-1927`.

**Defect.** Of the 8 over-78 lines, four carry a code span longer than the
budget and are genuinely forced: `:57` (span 102 columns with its
delimiters), `:236` (148), `:342` (79) and `:1009` (85). The other four are
not: `:430` (79 columns, longest span 64), `:547` (92, the double-backtick
span 64), `:1350` (88, longest span 29) and `:1794` (79, longest span 32).
Each of those four would fit inside 78 columns if the line were wrapped
before the span, without breaking it. The count of 8 is exact; the
explanation attached to it is an "every" claim that fails on half the
population.

**Repair.** Say that 4 of the 8 are forced by a span wider than 78 columns
and name them, and state the other 4 as wrapping choices, or reflow them.

## Q1–Q6 assessment

| Q | Scope truthful? | Genuine hard human gate? | Recommendation follows? | All lawful arms named? |
|---|---|---|---|---|
| Q1 retention posture as escalation trigger | **Yes on the act text** — the continuation act's trigger paragraph is quoted whole and exact at 150–156, the policy's `rawBodyHandling` block reads five `"never"` members at 178–184, and the 1,117/30/1 partition now re-derives to the identity. The dossier-comparison half is repaired; **G1** is the residual, and it sits outside the question cell | **Yes.** The act's own noun is "retention"; whether "beyond" reaches derived state is a reading only the owner may fix | **Yes**, and fail-closed. The counter-argument is named "strong" and the two narrower arms are offered without being argued down | **Yes** — trigger it; the same-posture reading; the disclosure-limited reading; plus the stated default that slice 1 and slice 2 do not ship. No arm is called unlawful |
| Q2 what a record may hold, how long | **Yes.** VIS-6(b)'s five words are exact at 177–179 and the 177,031 / 203,379 / 26,348 figures reproduce to the byte | **Yes.** "Immutable" against a discard policy is a doctrine tension the packet refuses to resolve, in terms | **Yes**, with the recommendation (unbounded) and the default (one prior) deliberately divergent and the divergence disclosed | **Yes** — unbounded; cap by count with the discard counted and rendered; keep exactly one prior; cap by bytes. Four arms, default named |
| Q3 may the band spend M1's headroom | **Yes**, and now measured rather than bounded: 713 / 418,122 / 586.4 post-trim on both host forms, 699 / 409,829 / 586.3 pre-trim, all four headrooms re-derived. F6 is fully discharged | **Partly**, as review 1 said — the allocation is the owner's; the honesty constraint inside it is settled and the packet treats it as settled, correctly | **Yes.** The recommended default is the cheapest honest arm and M1's objection is stated as the counter-argument, including that lane B is still open over the same budget | **Yes** — capped band with a disclosed remainder; machine channel only, explicitly held behind M10's Q6; counts-only with a route. Default named |
| Q4 may a note be promoted by writing out | **Yes.** The act's prohibition at 70–72 is exact, the registry's `"writeSurface": []` is at line 125 and its status banner at line 4, and the 0-of-278 and 0-of-556 measurements both reproduce | **Yes.** An act in force forbids the write in terms and the registry bytes are digest-bound; only the owner can move either | **Yes**, and the packet explicitly declines to rule whether a future act could authorize it | **Yes** — (a) new act plus CC-REV-2 over `writeSurface` plus a new registry act; (b) unpromoted stage 1 only; (c) promote into Syzygy's own `.syzygy/local/`, with its own objection stated; (d) do not build. The counter-argument to (b) is given |
| Q5 dismissal: implementation or amendment | **Yes.** PWB-REQ-007 at 443–446, its Case line at 454–456 and `CHALLENGE_STATES` at 83 under the comment at 81–82 are all exact | **Yes.** Widening a closed vocabulary a signed requirement quantifies over is a CC-REV-2 matter by construction | **Yes**, and the packet calls the dismissal neither lawful nor unlawful — only that the path is not conformance | **Yes** — amendment plus act; a sibling claim beside the tuple, with its VIS-6(a) objection named; do not build. The doctrinal bound on every arm is quoted, not argued |
| Q6 which evaluation owns a delta claim | **Yes.** architecture.md 221–229 is quoted whole and exact, 217–219 supports the counter-argument, and M2's line 47 is quoted correctly and read read-only at `f2f37dd` | **Yes.** A doctrinal question about what a claim may assert; M2 ruled its own and this packet flags the coupling without re-asking it | **Yes.** The recommended arm mints no identity and keeps the pinned tuples byte-identical, and the strongest counter-argument is stated and labelled a construction | **Yes** — a claim of the current evaluation about two; a third identified evaluation; a non-normative rendering artifact under PWB-REQ-014. Default named |

**Defaults.** All six are stated and all six fail closed. No lawful arm is
called unlawful anywhere in the six rows, and I found no place where a
trade-off is smoothed into consensus language; the counter-arguments remain
the strongest part of the packet.

**Hidden owner questions.** One: G1, the residue of F1. Every other item
under "Decided in this packet" is a measurement-backed correction a delegate
may properly make, and each is re-derived above.

**The dossier's prerequisite line, tested on the full line.** The packet's
repaired reading — that the dossier attached the retention-posture trigger to
the note's owner act and gave "none" for retention and delta, and that
whether the trigger reaches slice 1 is Q1 — is what the full line at
`docs/pursuits/2026-09-13-vision-pursuit.md` 415–416 supports and what the
act text at continuation-act 150–156 leaves open [Observed for both texts].
It holds, subject to G1.

## Invariants

No manifest row and no truncated signed digest is quoted anywhere in the
three artifacts; no Butlers path is backticked; every code-span path in the
packet either resolves or is one of the 32 enumerated non-paths; every
substantive claim I checked carries a label; every zero/all claim I checked
carries a predicate and a denominator, and each was run this session; every
digest in this review was computed by `wc -c` and `sha256sum` and none was
transcribed. `check_governance.py` ends `0 FAIL`. This review is bound to
the bytes tabled at the head of it and to no later edit (rule 10).

blocking 0 · non-blocking 2 · editorial 3

Verdict: CONFIRM WITH EXCEPTIONS
