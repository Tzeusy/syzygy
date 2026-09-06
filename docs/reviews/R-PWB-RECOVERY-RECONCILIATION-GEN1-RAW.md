# PWB recovery gen-1 reconciliation review — raw

Review date: 2026-09-06
Reviewer: independent fresh-context gen-1 reconciliation reviewer (bead syzygy-1z3.24.7)
Syzygy subject: worktree `/home/tze/GitHub/syzygy/.worktrees/parallel-agents/syzygy-1z3.24.3`,
branch `agent/syzygy-1z3.24.7`, HEAD `d92910c8a8f423414e82a25653b2857e92ebce32` (= `origin/main`),
`git status --short` empty
Observed Butlers subject: `/home/tze/GitHub/butlers` at HEAD
`2891522f339df3a82e309d194fc41a5f7a63f8a3` (the last retained run observed
`ff52900a341dfcc3d1018d6e5970a72526c085e3`; 19 Butlers commits lie between them,
touching `about/lay-and-land/frontend-copy-inventory.md`, two RFCs, three baseline specs
and several `roster/*/butler.toml`)
Runtime: my own daemon from a fresh clone of the worktree (`<scratch>/clone`, HEAD `d92910c`),
loopback `127.0.0.1:46825`, ephemeral port, started and stopped by this review; the
fresh-checkout demo's own daemon at `127.0.0.1:43693`. The pre-existing daemon (pid 2851269)
was neither used nor signalled.
Mode: read-only in the worktree; clone-based battery (rule 7); every guard relied on is either
cited to retained mutation evidence by predicate or mutated in my clone (rule 6); every
universal claim carries its sweep and denominator (rules 2, 9); requirement claims anchor to
clause text (rule 8). Butlers bodies were read only through Syzygy's daemon or `git show` of
paths in the model's admitted population (root index, four pillar indexes, `about/heart-and-soul/v1.md`
lines 88–100); no implementation file body, no working-tree read, no Butlers write.

## Verdict

**CONFIRM WITH EXCEPTIONS.**

[Observed] All fifteen retained findings PWB-LIVE-01..15 map to exactly one repair child,
to code, and to a gate I re-ran or mutated myself; fourteen are `repaired` and one
(PWB-LIVE-04) is `repaired` in code with its live scenario unobservable until a Butlers-data
owner decision. The eleven amended artifacts, the amended policy and registry hash to their
2026-09-05 acts; no digest-bound artifact changed after its act; `openspec/**` changed only in
the three amendment commits that precede the sign-off. A fresh clone builds, runs 1,498 passed
/ 3 skipped tests, and the fresh-checkout demo exits 1 on exactly the one invariant the retained
record failed (`preflight-ready`), with the same three limbs on the current Butlers head.

The exceptions are not in the fifteen. [Observed] The human Polaris page on both mounts does
not render the exact state-(1) sentence PWB-REQ-005 makes mandatory for "both surfaces"
(the machine answer carries it three times); this predates the recovery (`cd6c952` renders the
same `authorityLine`) and was not caught by the baseline reviews. [Observed] The whole-shape
claim is Unknown because the root index names Spec and Spine's home as `openspec/` with no
README, and neither that cause nor the degradation state reaches the human page. [Observed]
The walkthrough evaluation identity does not change with a core code change that bumps no
declared version. These need one gen-2 implementation pass before the owner walkthrough; the
readiness failure itself needs the owner first (Section I).

## Section A — finding disposition register

Sibling and commit columns are from `bd show` and `git log`; code and gate columns are what I
opened. "Mine" = mutation I applied in my clone this review (Section D lists all fourteen).

| ID | Sibling / commits | Code evidence | The one gate | Disposition | Evidence I checked |
|---|---|---|---|---|---|
| PWB-LIVE-01 | 1z3.24.1 / PR #15 → `4e28852` | `apps/three-surface-poc/src/git-observation.ts:33-54` (`resolvePwbRepositoryBinding`: realpath locator = `PWB_APPROVED_REPOSITORY_LOCATOR`, then `--git-common-dir` = `<locator>/.git`); `launcher.ts:9-17`; `main.ts:71-73` (binding before any observation) | `git-observation.test.ts` "rejects a second Butlers-shaped repository before any repository observation" (7 cases) + `launcher.test.ts` | **repaired** | Mine: `locator-mismatch-accepted` KILLED (1 failed), `git-common-dir-mismatch-accepted` KILLED (1 failed). Live daemon accepted the consented locator only. |
| PWB-LIVE-02 | 1z3.24.2 / PR #16 → `8bdb501` | `packages/three-surface-poc-core/src/project-shape-manifest.ts:283-310` (`rootIndexPillarRoots`: Pillar/Directory table columns), `:387-399` (link fallback) | `project-shape-manifest.test.ts` (20 cases; real-shaped root fixture) | **repaired** | Mine: `root-directory-column-ignored` KILLED. Live: independent enumeration of rules 1–4 at `2891522f` = 270 paths; model = 270; symmetric difference ∅; Heart and Soul carries 7 sources (README + 6 named). |
| PWB-LIVE-03 | 1z3.24.2 / `8bdb501` | `project-shape-model.ts:535-560` (`uncoveredDiscovery` → `discoveryUncertainties`), `:416-446` (`projectAccountOf` reason precedence: source Unknown → class Unknown → only then `missing-declaration`) | `project-shape-model.test.ts` + `polaris-project-shape.test.ts` "does not claim a complete or absent catalog when root discovery is Unknown" | **repaired** | Mine: `unknown-pillar-not-propagated` KILLED (2 failed). Live: no account statement is `missing-declaration`; `v1-scope`/`v1-success` are `excluded-content`; four classes carry Unknown denominators, none "Observed zero"; `complete catalog` 0 hits on the page. |
| PWB-LIVE-04 | 1z3.24.3 (act `2a3310a`) + 1z3.24.4 `88efbd1` | `project-shape-extraction.ts` (root cardinal + 7-row table grammar), `project-shape-coverage.ts:265-300` (family map, exactly-one-under-home, row 7 inert) | `project-shape-model.test.ts:746` "with the root precedence table, row 1 makes the derived count effective…"; retained `pwb-c4-…json` 23/23 killed | **repaired** (live scenario unobservable — Section I) | Spec `PWB-REQ-004` scenario "Eight versus nine follows the declared layer rule". Live: `precedence.kind=admitted` (7 rules, root lines 44–50), `rootSummary.kind=emitted` (3 / 8 at root line 105), `catalog-count:Butlers` state `unknown` reason `excluded-content`, `rulesConsidered=[]`, contradictions 0 — because `v1.md` is whole-source Unknown. |
| PWB-LIVE-05 | 1z3.24.2 / `8bdb501` | `project-shape-model.ts:523-530` (baseline path-only derivation), `content-classification.ts:529-549` (`not-read`, `basis:'path-only'`), `project-shape-model.ts:589-591` (final records → exclusions/counts) | `project-shape-model.test.ts` (path-only zero reads; final partitions) | **repaired** | Mine: `baseline-specs-read-bodies` KILLED (7 failed), `final-exclusions-stale` KILLED (2). Live: 185 baseline specs `classified/path-only`; 270 = 259 classified + 11 excluded + 0 unavailable; items 246 = 246 modeled + 0 + 0; `exclusions` list length 11 = `counts.exclusions`. |
| PWB-LIVE-06 | 1z3.24.4 `7c5d40d` + 1z3.24.5 / PR #18 → `2d15336` | `apps/…/verbatim-route.ts:62-131` (ten ordered gates), `capability-detail.ts` `resolveVerbatim`/`selectRequirementSections`, `polaris-source.ts`, `routes.ts:179-186,221-222` | `verbatim-route.test.ts` (13) + `polaris-source-route.test.ts` (5, incl. HTTP); retained C5 12 route + C6 8 source-route mutations killed | **repaired** | Live: 185 identities linked, 175 rendered (1,670 blocks), 10 `not-rendered excluded-content`; page renders 1 verbatim block with 6 requirements. My probes: empty, unknown, forged-oid, non-baseline (`v1.md`, `vision.md`), detector-excluded (`roster/qa/MANIFESTO.md`) → each `data-verbatim="not-rendered"` with a typed reason and no bytes; Origin off-list → 403. |
| PWB-LIVE-07 | 1z3.24.3 (act `156b689`) + 1z3.24.4 `c69e6f2` | `markdown-code-context.ts` (profile), `git-object-reader.ts:191-219` (`scanActiveContent` over the mask; detectors on raw) | `markdown-code-context.test.ts`, `git-object-reader.test.ts` "every sentinel inside a closed code fence or inline span is inert" | **repaired** | Policy artifact hashes to the act. Live exclusions fell from 133 (`a3dd1fe`) to 11 (`2891522f`); `about/lay-and-land/README.md` is now classified. Residual policy fact: 7 of 13 `butler.toml` are still `active-content` (TOML has no inert context) — Section I. |
| PWB-LIVE-08 | 1z3.24.1 / `4e28852` | `governance-inputs.ts:176-212` (one Git tree), `:225-243` (tag resolves only when the act-record blob is byte-equal), `:266-296` (enumeration/read failure throws → `not-evaluated`) | `governance-inputs.test.ts` (13 cases) | **repaired** | Mine: `tag-path-only-resolves` KILLED (2), `lifecycle-enumeration-failure-empty` KILLED (1); `lifecycle-unreadable-record-skipped` SURVIVED — equivalent in the production git-tree path (ENOENT cannot occur for a listed name; a `cat-file` failure re-throws at `readText`), so a test-rigor gap only (PWB-RECON-06). |
| PWB-LIVE-09 | 1z3.24.1 / `4e28852` | `project-shape-observation.ts:449-489` (`classifyPhaseA` before `phase-a-link-discovery`; excluded seed → `unavailable`, derives nothing) | `project-shape-observation.test.ts` "screens a secret-bearing root seed before it can derive any child path" (30 cases in file) | **repaired** | Mine: `phase-a-excluded-seed-parsed` KILLED (2). |
| PWB-LIVE-10 | 1z3.24.3 (acts `2a3310a`,`382798a`) + 1z3.24.4 `0a108aa` | `resource-ledger.ts` (one cumulative counter, closed 12-pass list), `routes.ts:136-142` (`boundedResponse` on every human/machine body, 503 typed failure) | `resource-ledger.test.ts`, `response-limits.test.ts` "limit − 1 breaches, limit and limit + 1 serve, for each ceiling" | **repaired** | Mine: `human-ceiling-unenforced` KILLED (9). Live: `limitBreaches=[]`; `resourceUse` 85 bodies, 1,095,529 bytes, 688 passes, max 14 passes on one source (limit 16); human 2,045,086 B direct / 2,050,726 B tailnet vs 2,097,152; machine 4,975,401 B vs 8,388,608. |
| PWB-LIVE-11 | 1z3.24.5 / `2d15336` | `routes.ts:163-176,237-238` (`GET /api/poc/polaris`, machine-credentialed, `citable:false`) | `polaris-presentation-route.test.ts` (2) + retained C6 `presentation-*` 4 mutations | **repaired** | Mine: `narrative-envelope-detached` KILLED. Live: 401 without bearer; 497,011 B with; envelope `narrative` byte-equal (sorted JSON) to the page's `polaris-narrative` script: 3 roles, 6 anchor classes, 521 blocks, 1 deep dive; identical on the tailnet mount. |
| PWB-LIVE-12 | 1z3.24.6 / PR #19 → `2cfee1a` (+ 1z3.24.4 `7c5d40d`) | `walkthrough-inputs.ts:56-68` (no placeholder; Polaris + `/polaris/source` on both mounts), `:81-89` (`polaris@<tree oid>`), `:190-217` (traversal predicate), `walkthrough-readiness.ts:119-128` (identity), `:208-250` (nine answers parsed) | retained C7 46/46 + C5 38/38 killed; `walkthrough-readiness.test.ts` (32), `walkthrough-inputs.test.ts` (17) | **repaired** | Mine: `evaluation-identity-drops-manifest` KILLED. Live: daemon prints and page renders `polaris@dea2b82f3ef5` / `pwb-eval-db00655d0b8535a2e590e149`; readiness `no-run-record`. Residual: identity is blind to core code (PWB-RECON-03). |
| PWB-LIVE-13 | 1z3.24.5 / `2d15336` | `polaris.ts:440` (`causeRoutes`), `:342` (one claim-state glossary), `:355` (population `<details>`) | `polaris-first-reading.test.ts` (7) + retained C6 `cause-route-*`, `population-*`, `tuple-not-described` killed | **repaired** | Live page: 47 headings ≤ 6 words, 6 ledes ≤ 20, 0 prohibited terms, exactly 1 `poc-bound` scope instruction; 7 `population` disclosures; `By cause:` ×7; `as it declares itself` 0; glossary once and 529/529 tuples `aria-describedby` it; 0 fragment targets inside a closed `<details>` other than the glossary element itself. Residual: the shape-level Unknown's discovery cause is not on the page (PWB-RECON-02). |
| PWB-LIVE-14 | 1z3.24.6 / `2cfee1a` + `d92910c` | `fresh-checkout-verdict.ts:15-32,81-112` (16 named invariants, each moves the exit) | `fresh-checkout-verdict.test.ts` + retained C7 15 `verdict-*` mutations killed | **repaired** | My clone run: `DEMO_EXIT=1`, `unhealthy: preflight-ready`, 15/16 hold; identical failed set to the retained record. |
| PWB-LIVE-15 | 1z3.24.2 / `8bdb501` | `project-shape-extraction.ts:221-260` (`topLevelListItems` keeps indented continuations) | `project-shape-extraction.test.ts` (87 cases) | **repaired** (extraction); the comprehension half is the owner's under PWB-REQ-021 by spec design | Mine: `multiline-continuation-dropped` KILLED (6 failed). Live: `about/README.md:105` two-line "11 daemons" item is extracted as one summary declaration. |

[Observed] The prior traceability sweep's "eight unnamed findings" was a false absence
(abbreviated identifiers); `bd show` of the seven children names 15/15 exactly once each, and
`SEMANTIC-DELTA.md` names 04, 06, 07, 10, 12. Code comments name 02, 06, 11, 12, 13, 14.

## Section B — requirement-to-code checklist

Amended scenarios are those the 2026-09-05 act added or rewrote (PWB-REQ-004 all three,
PWB-REQ-006 "Markup examples in code remain inert" and "Resource breach is bounded and
explicit", PWB-REQ-011 "Consented baseline requirement renders verbatim", PWB-REQ-021 "Lawful
run can remain not ready"). Status vocabulary: `conforms` (code + gate + live observation
agree), `conforms-fixture-only` (gate exists, live state cannot exercise it), `gap`.

| Requirement / scenario | Implementing module(s) | Gate(s) | Status |
|---|---|---|---|
| PWB-REQ-001 "Source population is complete at one revision" | `project-shape-manifest.ts`, `project-shape-observation.ts:387-405,561-572` | `project-shape-observation.test.ts` "exposes the complete population with a per-source identity and stamp", "records every deterministic input identity"; live-gated `project-shape-discovery.live.test.ts` (pinned to `a3dd1fe`, skipped in the battery) | `conforms` — my independent oracle: 270 = 270 at `2891522f`; every source resolves at R (0 non-blob anchors); human and machine expose the same 270 paths (parity sweep). Note the only live gate at the *current* head is the fresh demo. |
| PWB-REQ-002 "Declared shape reconciles" | `project-shape-extraction.ts`, `project-shape-coverage.ts`, `project-shape-model.ts:579-591` | `project-shape-extraction.test.ts` (87), `project-shape-coverage.test.ts`, preflight `population-unreconciled` limb | `conforms` for known denominators (principle 7=7, design-contract 32=32, baseline-spec 185=185, craft-policy 7=7); Unknown denominators for five classes are honest, not partial. |
| PWB-REQ-003 "Excluded source fails closed" | `content-classification.ts`, `git-object-reader.ts` | `content-classification.test.ts` "the three spec faults…", "no secret, active or body byte reaches the returned model…" | `conforms` — 11 live exclusions carry digest/path/reason/detector only; sink sweep over 24 retained files found 0 secret-shaped strings and 0 credential bytes. |
| PWB-REQ-005 "Missing observation consent blocks content reads" / "Failed state-(2)…" / "Later correlation…" / "Mixed valid…" | `body-read-authority.ts`, `governance-inputs.ts` | `body-read-authority.test.ts` (195-case table, eight valid triples, no-fallback, history), retained `pwb-mutation-run-2026-09-03.json` | `conforms` |
| PWB-REQ-005 "State-(1) authorities permit reads with the trust gap visible" — "both surfaces expose every state as owner-adopted **and the exact same-tree-forgeability disclosure**" | `authority-disclosure.ts` (machine); `polaris.ts:592-599` `authorityLine` (human) | machine: `body-read-authority.test.ts:657`; human: **none** (parity families cover `authority-state`, not the disclosure) | **gap** — human page carries "consent — owner-adopted (bootstrap, uncorrelated)" ×3 and 0 occurrences of the sentence (PWB-RECON-01). |
| PWB-REQ-006 "Active repository content remains inert" | `git-object-reader.ts:191-219` | `git-object-reader.test.ts` "scanActiveContent: forms, positions, obfuscation and case" | `conforms` |
| PWB-REQ-006 "Markup examples in code remain inert" (amended) | `markdown-code-context.ts` | `markdown-code-context.test.ts`, `verbatim-route.test.ts:148` | `conforms` |
| PWB-REQ-006 "Resource breach is bounded and explicit" (amended) | `resource-ledger.ts`, `routes.ts:108-142` | `resource-ledger.test.ts`, `response-limits.test.ts`, `walkthrough-readiness.ts:365` (breach → not ready) | `conforms` — the live evaluation is 0 breaches; the human ceiling is 97.5 % (direct) / 97.8 % (tailnet) consumed. |
| PWB-REQ-007 "Missing current evidence remains explicit Unknown" | `project-shape-model.ts:380-414` | `polaris-epistemic-tuples.test.ts`, `project-shape-model.test.ts` "every claim is a complete tuple…" | `conforms` — 19 visible Unknowns = 19 machine Unknowns, each with a primary reason and a route. |
| PWB-REQ-004 "Stale summary does not silently replace V1 scope" / "Eight versus nine…" / "Conflict remains Unknown…" (all amended) | `project-shape-extraction.ts`, `project-shape-coverage.ts:265-300`, `polaris.ts:797` (`shape:root-index`) | `project-shape-coverage.test.ts`, `project-shape-model.test.ts:746`, retained C4 23/23 | `conforms-fixture-only` — live: both stated counts retained and anchored, no rule applied, `catalog-count:Butlers` Unknown; the disagreement cannot appear until `v1.md` parses. |
| PWB-REQ-010 "WhatsApp is a drill-down, not the project account" | `polaris.ts` (group order), `polaris-copy.ts:85` | `polaris-first-reading.test.ts:60`, `polaris.test.ts` | `conforms` — h1 `Butlers`, h2 order What Butlers is / is not / How built / What V1 ships, capability detail later; scope sentence now conditions completeness on the disclosed denominator. |
| PWB-REQ-011 "Capability reaches exact requirements" | `polaris.ts:1250` (`exactSourceIdentities`), `polaris-source.ts` | `polaris-reachability.test.ts`, `polaris-source-route.test.ts:192` | `conforms` — 372 `Exact text` links on the page, 498 fragments, 0 dangling. |
| PWB-REQ-011 "Consented baseline requirement renders verbatim" (amended) | `verbatim-route.ts`, `capability-detail.ts:227-262` | `verbatim-route.test.ts`, `polaris-source-route.test.ts:101` | `conforms` — only `### Requirement:` blocks and their scenarios are encoded; machine form carries titles only. |
| PWB-REQ-012 "Section headings name project concepts" | `polaris-copy.ts` | `polaris-copy.test.ts` (roles, ≤6/≤20, prohibited terms, `poc-bound` ≤ 1) | `conforms` — my live sweep matches the fixture oracle (Section C). |
| PWB-REQ-013 "Proposal is shown only in affected capability detail" | `capability-detail.ts`, `proposed-work.ts` | `polaris-proposed-work.test.ts`, `proposed-work.test.ts` | `conforms` |
| PWB-REQ-014 "A project claim is supported without making Polaris authority" | `polaris-narrative.ts`, `routes.ts:163-176` | `polaris-narrative.test.ts`, `polaris-authority-sweep.test.ts`, `polaris-presentation-route.test.ts` | `conforms` — 521 blocks, every one `presentation-artifact`/`non-citable`; envelope = page registry. |
| PWB-REQ-015 "Proposed work stays beside exact current intent" | `capability-detail.ts` (`DeepDiveLedger`, bands) | `polaris-capability-detail.test.ts` "renders exactly the three bands in order…" | `conforms` |
| PWB-REQ-016 "Keyboard-only owner reaches exact intent" | `polaris-accessibility.ts`, `cdp-browser.ts` | `polaris-accessibility.browser.test.ts` (6 variants), fresh demo browser check | `conforms` (mechanical) — 0 violations at `d92910c`; the walkthrough record's mode flag is `nonvisual-keyboard-only` by schedule. |
| PWB-REQ-020 "Complete model has wire parity" | `fresh-checkout-demo-main.ts:177-197`, `polaris-parity-sweep.test.ts` | parity sweep (fixture, all authority/judgment states) + demo parity (live) | `conforms` — live 529 tuples / 528 ids, 0 mismatch, 0 absent either way, direct and tailnet tuple lists equal; but the body-read authority *disclosure* is not a parity family (PWB-RECON-01). |
| PWB-REQ-021 "Whole-project walkthrough passes" | `walkthrough-readiness.ts`, `walkthrough-preflight.ts` | `walkthrough-readiness.test.ts` (32), `walkthrough-preflight.test.ts`, retained C5/C7 | `gap-by-data` — readiness `no-run-record`; preflight fails on Butlers data (Section F). |
| PWB-REQ-021 "Lawful run can remain not ready" (amended) | `walkthrough-readiness.ts:260-379`; `walkthrough-judgment.ts:335` (`section()` never reads `## Answers`) | `walkthrough-readiness.test.ts` "answer-missing…", "path-outside-polaris…"; judgment test denominator `84 + 2` asserted at `walkthrough-judgment.test.ts:398-399` | `conforms` |
| PWB-REQ-022 all five scenarios | `walkthrough-judgment.ts`, `walkthrough-inputs.ts` | `walkthrough-judgment.test.ts` (84 present-invalid, 2 absent, both valid states, history), `polaris-parity-sweep.test.ts:517-527` (human `judgment-disclosure` field) | `conforms` — live: `absent` / `no-run-record` / `unknown-never-met`. |

## Section C — universal / negative-claim audit

| Claim (where made) | Sweep I ran | Denominator | Remainders |
|---|---|---|---|
| "No Butlers body is read before the authority admits" (plan §3, `main.ts`) | Enumerated every `cat-file`/`readFileSync`/`execFileSync`/`spawnSync` call site in `apps/three-surface-poc/src` + `packages/three-surface-poc-core/src`, non-test | 41 call sites; 5 read Butlers objects: `project-shape-observation.ts:430` (phase A, after `authority` admits inside `observeProjectShape`), `git-object-reader.ts:338` (phase B, same gate), `verbatim-route.ts:46` (render, only for a source of the admitted population), `model.ts:273` (legacy five-file POC observer — pre-PWB Three-Surface POC scope, working tree, after the locator binding), `git-observation.ts:26` (metadata only) | The legacy `model.ts:273` read is not PWB-gated and is not a PWB source; it is the older POC slice and lies outside this recovery — recorded, not charged. Others are tooling/governance reads of Syzygy's own tree. |
| "Working-tree bytes are never consulted" (`polaris-source.ts`, C5 note) | same enumeration | 5 Butlers reads | Only `model.ts:273` (legacy slice) reads a working tree; every PWB read is by exact object id. |
| "Raw bodies are never stored, logged, rendered or sent" (policy act) | `console.*`, `process.std*`, `writeFileSync` in core non-test | 4 write sites, all state records (`materialization.ts:130`, `test-artifact-verification.ts:75`) | 0 body writes. Live sink sweep: 0 secret-shaped strings, 0 credential bytes, 0 act digests in the evidence record; the three effect-artifact digests appear in `/api/poc` by PWB-REQ-005 design ("digest … SHALL be an evaluation input"). |
| "No fragment target inside a `<details>`" (AGENTS.md; C6) | ids inside every `<details>…</details>` ∩ `href="#…"` targets on the live page | 18 details, 498 fragment hrefs | 1: `polaris-claim-states` — the `<details>` element's own id, named by the entry notice link; not a child target. 0 dangling fragments. |
| "Every tailnet link carries the mount prefix" | root-absolute hrefs on the Host-mounted render | 874 hrefs | 0 without `/butlers-syzygy`. |
| "Direct and tailnet render the same facts" | tuple lists, both mounts | 529 tuples each | equal lists; size differs by 5,640 B (prefixes). |
| "Every owner-visible string has one role; headings ≤ 6 words; ledes ≤ 20; no prohibited term; ≤ 1 POC-bound scope instruction" (PWB-REQ-012) | live-page sweep | 47 headings, 6 ledes, 1 notice, 2,393 role attributes (1,077 disclosure / 904 fact / 396 action / 16 scope) | 0 violations; 12 distinct scope-instruction strings from the copy table, exactly 1 `poc-bound`. |
| "Every visible Unknown has a primary reason and a route; count equals the machine" | preflight `unknown-invisible` limb re-computed | 19 | 0 |
| "`openspec/**` and act-bound artifacts unchanged after their acts" | `git log 2a3310a..d92910c -- openspec/ …policies …adapter-registry` and per-file commit counts | 9 act-bound files | 0 commits after the act for each; `openspec/**` last changed at `4daea08` (frozen subject). |
| "PWB-REQ-022 denominator unchanged (84 + 2)"; "PWB-REQ-005 = 195" | test assertions | `walkthrough-judgment.test.ts:398-399`, `body-read-authority.test.ts:449-451` | asserted literals; readiness arms live in a separate module and `section()` never sees `## Answers`. |
| "The eight-versus-nine conflict is exposed" (design.md:8-13) | live facts | 268 facts, 254 modeled, 14 unknown | Unobservable live: `catalog-count:Butlers` Unknown; not "agreement", not "disappeared" — honest but the spec's own named scenario has no live instance. |
| "Source population never shrinks on failure" | 270 model vs 270 independent; 11 excluded still counted | 270 | 0 missing. |

## Section D — instrument blind-spot audit

Rule-6 evidence relied on: retained `pwb-c4` (23/23), `pwb-c5` (38/38), `pwb-c6` (26/26),
`pwb-c7` (46/46), `pwb-mutation-run-2026-09-03` (P1); plus fourteen mutations I applied in my
clone (`<scratch>/mutations.json`; every file restored byte-for-byte, `git status` clean):
13 killed, 1 survived (`lifecycle-unreadable-record-skipped`, equivalent mutant on the
production path).

| Instrument | What it cannot see | Gate doubles / gaps |
|---|---|---|
| Preflight (8 limbs) | Runs only on the direct mount (never the tailnet Host render, never `/api/poc/polaris`, never an Origin refusal); checks one verbatim leaf (the capability's current authority); does not run the PWB-REQ-012 copy oracle over the live page; ignores `degradation` | Each limb has one pre-fix-failing counterexample (C7 17 preflight mutations). No double. |
| Fresh-checkout verdict (16 invariants) | `human-routes-served` is four direct paths; `source-route-served` only linked identities; parity is project-shape claims only (528 ids), not entity/relationship tuples or the narrative registry (those are fixture-gated in `polaris-parity-sweep.test.ts` and `polaris-presentation-route.test.ts`; I compared the live registry myself: equal) | one counterexample per invariant (C7). |
| Parity oracle (demo + sweep) | The body-read **authority disclosure sentence** is not a parity family; only `authority-state`, `authority-mode`, `authority-evaluation-id` | gap → PWB-RECON-01. |
| Readiness evaluator (10 arms) | Anchors resolve by path only (any line number ≥ 1 passes); the identity it binds to excludes the Syzygy observer revision and the core tree (`implementationVersion` literal `'1.0.0'` at `project-shape-observation.ts:53`, unchanged since `e1617a4`) | → PWB-RECON-03. |
| Authority gate + loader | Working-tree `.syzygy/**` is not consulted (one Git tree at the observed observer revision); the only ambient input left is the tag ref itself, bound to the record blob bytes | survivor: unreadable-record-skip is unreachable via the git-tree reader. |
| Resource envelope | Ceilings are per response; the busiest source spends 14 of 16 passes; the tailnet render is 5,640 B larger than what the demo measures | headroom, not a gap (Section I). |
| Classifier | Applies the Markdown code-context mask to TOML/any text; TOML strings containing `<…>` exclude the whole `butler.toml` (7 of 13 live) | policy-bound; owner item. |
| Verbatim route | Baseline specs only (by amended PWB-REQ-011); pillar bodies are never verbatim even when admitted | by design; the `exact-requirement` prompt has exactly one live route (`switchboard-identity`). |
| Discovery (manifest) | A declared pillar whose home has no `README.md` is `index-missing-at-revision` → whole-shape Unknown ("Partial snapshot") with an observer-repair route; the page shows neither the pillar state nor the cause | → PWB-RECON-02. |
| Live regression | `project-shape-discovery.live.test.ts` pins Butlers `a3dd1fe` and is skipped without `SYZYGY_POC_BUTLERS_REPO`; nothing in the battery observes the current Butlers head except the manual fresh demo | note only. |

Scenario-to-gate: every scenario in Section B has exactly one behavior gate except PWB-REQ-005
"State-(1)… trust gap visible", whose human half has none (the machine half has
`body-read-authority.test.ts:657`). No scenario has two competing gates; the PWB-REQ-020 parity
is gated twice by design (fixture sweep + live demo), on different populations.

## Section E — surfaces reconciliation

| Channel | Observed (my daemon, `2891522f`) |
|---|---|
| Human direct `/polaris` | 200, 2,045,086 B; 529 tuples / 528 ids; 19 Unknowns; 874 hrefs (498 fragments, 372 `Exact text`, 4 surface routes) |
| Human tailnet (`Host: tzeusy.parrot-hen.ts.net`) | 200, 2,050,726 B; tuple list identical; 0 unprefixed root-absolute hrefs |
| Prefixed path `/butlers-syzygy/polaris` direct | 200 (route exists for a path-preserving proxy; unreachable through real `tailscale serve`, per `tailnet.ts`) |
| Bad `Origin` / bad `Host` | 403 `browser-origin-refused` on `/polaris` and `/polaris/source` |
| Machine `/api/poc` | 401 without / wrong bearer; 200 with, 4,975,401 B, identical size on the tailnet mount; carries the state-(1) sentence ×3, the three effect-artifact digests, `degradation`, `precedence`, `rootSummary`, `resourceUse` |
| Machine `/api/poc/polaris` | 401 without; 200 with, 497,011 B, `citable:false`, `narrative` byte-equal to the page's `polaris-narrative` script (521 blocks) |
| Exact-source `/polaris/source` | 200 always; rendered only for admitted baseline identities (6 requirement blocks for `switchboard-identity`, same on tailnet with prefixed back-link); typed Unknown for empty, unknown, forged-oid, non-baseline and excluded identities |
| Human − machine | human lacks the state-(1) disclosure sentence and the degradation state/cause (PWB-RECON-01/02); human never carries requirement text in the machine form (by design) |

## Section F — live readiness and fresh-checkout verification

My run (`<scratch>/clone/docs/evidence/pwb-p4-5-fresh-checkout-demo-2026-09-06.json`, artifacts
in `<scratch>/retain`) versus retained `docs/evidence/pwb-p4-5-fresh-checkout-demo-2026-09-05.json`:

| Field | Retained (2026-09-05) | Mine (2026-09-06) |
|---|---|---|
| Syzygy clone head | `28ff68d` (tree = `2cfee1a`: `git diff --stat 28ff68d 2cfee1a` empty — confirmed) | `d92910c` = source |
| Butlers observed = model | `ff52900a` | `2891522f` |
| Tests in clone | 1501 / 0 failures | 1501 / 0 failures (my separate `npx vitest run`: 112 files passed, 3 skipped; 1498 passed, 3 skipped) |
| Surface version / evaluation identity | `polaris@dea2b82f3ef5` / `pwb-eval-0c3baa9fb21e88afce06602f` | `polaris@dea2b82f3ef5` / `pwb-eval-db00655d0b8535a2e590e149` (Butlers revision and manifest digest changed; surface tree unchanged — expected drift) |
| Parity | 529 / 528 / 0 / 0 / 0 | identical |
| Source routes | 185 linked, 175 rendered, 1,669 blocks, 10 excluded | 185, 175, 1,670, 10 |
| Browser check | 6 variants, 0 violations at the serving commit | same at `d92910c` |
| Human / machine bytes | 2,045,086 / 4,946,161 | 2,045,086 / 4,975,905 |
| Limit breaches / daemon | 0 / exit 0, stderr empty | 0 / exit 0, stderr empty |
| Preflight | not ready: `account-statement-unbacked` (v1-scope, v1-success), `population-empty` (catalog-entry, topology-component), `population-unreconciled` (success-criterion, catalog-entry, topology-component: denominator Unknown `excluded-content`) | identical limbs and identical detail |
| Exit | 1 (`preflight-ready`) | 1 (`preflight-ready`) |

[Observed] Causes at `2891522f`, from the machine answer (no excluded body read):
`about/heart-and-soul/v1.md` `parse-failure` (root of v1-scope, v1-success, success-criterion,
catalog-entry and both catalog counts — the Modules list item `**Steam**:` at v1.md:95 uses a
colon where the signed grammar requires the leading label before a dash);
`about/lay-and-land/components.md` `parse-failure` (topology-component 0);
`about/lay-and-land/frontend.md` `active-content`; 7 of 13 `roster/*/butler.toml`
`active-content` (1–3 markers each; roster-identity denominator Unknown, 6 modeled);
`roster/qa/MANIFESTO.md` `credential-assignment` detector. [Observed] `about/lay-and-land/README.md`
is now classified (the AGENTS.md "Lay and Land's index is excluded" note is stale at this head).
[Inferred] No Syzygy implementation change can make the preflight ready without crossing the
grammar or policy act boundary — the coordinator's claim holds.

Nine-prompt surface reading (mine, not an owner judgment): from the first reading level the page
now answers why (purpose, 1,536 chars, anchored), promises, refusals and architecture from
source; `capabilities-and-fit`, `architecture-and-groups` (V1 groups) and `v1-success` remain
Unknown with `excluded-content`; `exact-requirement` is reachable (6 blocks); `unknown-or-
contradiction` is answerable (19 visible Unknowns with causes); `claim-strength` is explained
once and every tuple points at it. Four of nine prompts are therefore blocked by Butlers data,
not by Syzygy.

## Section G — amendment digests and scope check

[Observed] `python3 scripts/check_governance.py`: 33 OK, 19 WARN, 0 FAIL (52 checks); CG-7d/7e
report 0 findings. Recomputed SHA-256: all eleven `PWB-TRUTH-READINESS-AMENDMENT-ACT.md` rows
match (11/11); `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` = `97e3d8f8…d578a` (the act's argument);
policy = `d148f036…8e75`; registry = `0765f4d5…643f`; consent record = `5d705d75…7841` per its act.
Tags: `pwb-truth-readiness-amendment-signed-2026-09-05` → `2a3310a`, `pwb-approve-policy-signed-2026-09-05`
→ `156b689`, `pwb-adopt-registry-entry-signed-2026-09-05` → `382798a`. `npx openspec validate
--all --strict`: 3 passed, 0 failed.

[Observed] `git diff --name-status 6823b07..d92910c`: 132 paths. Classification: implementation
71 (`apps/three-surface-poc/src` 40 incl. 14 new; `packages/three-surface-poc-core/src` 27 incl.
6 new; `scripts/` 4), tests included above (every new module has a sibling test);
docs/evidence 5 JSON + `docs/PWB-IMPLEMENTATION-PLAN.md` + `docs/README.md` + 11 retained
reviews; governance records 21 (`decisions/` 7 incl. the four 2026-09-05 acts/direction,
`contracts/candidates/` 9, `ACCEPTANCE-ACT-RECORD.md`, `PENDING-OWNER-DECISIONS.md`, README);
`openspec/**` 6 files changed only in `305500d`, `9bac13f`, `4daea08` (all before the act at
`2a3310a`; 0 changes after); policy and registry JSON changed before their acts and never after;
root/docs 5 (`AGENTS.md`, `CONTRIBUTING.md`, `README.md`, `PROCESS-GLOSSARY.md`, `PROJECT-STATUS.md`,
`.gitignore`); deletions 11 (`.claude/commands/opsx/*`). No digest-bound artifact changed after
its act (per-file commit counts: 1 each for the eight act records; the consent artifact's last
commit predates its act).

## Section H — findings and gen-2 need

| ID | Severity | Finding | Route / duplicate |
|---|---|---|---|
| PWB-RECON-01 | High | The human Polaris page (both mounts) renders no state-(1) disclosure sentence for the three body-read authorities although PWB-REQ-005 says "State (1) SHALL render exactly: `Owner-trusted only; same-tree forgeable…`" and its scenario requires "both surfaces expose … the exact same-tree-forgeability disclosure"; `authorityLine` (`polaris.ts:592-599`) emits state labels only; the machine answer carries the sentence ×3; no parity family or test covers the human side. Pre-existing at `cd6c952` (same function), missed by the baseline reviews. | Implementation (gen-2): render `entry.disclosure` per authority as a `data-parity-field="authority-disclosure"` and add the family to the sweep and the preflight. Duplicate of: none. |
| PWB-RECON-02 | Medium | Spec and Spine's declared home `openspec/` has no `README.md`, so the pillar is `index-missing-at-revision`, the whole-shape claim is Unknown (`source-uncaptured-or-unreachable`, route "Repair the observer or source; new snapshot") and `degradation = Partial snapshot: pillar spec-and-spine unknown` — none of which reaches the human page (0 hits for `spec-and-spine`, `degradation`, `Partial snapshot`). The observer is behaving as designed, so the route is cause-incorrect (PWB-LIVE-13 family) and the top-level Unknown is permanent under current Butlers. | Owner wording/decision (Section I item 3) plus implementation (gen-2): surface each pillar's discovery state and reason on the page with a cause-correct route. Duplicate of: none (P-57 concerns Syzygy's own `openspec/`, not Butlers'). |
| PWB-RECON-03 | Medium | `walkthroughEvaluationIdentity` digests deterministic inputs whose only code-version stamps are the registry literals (`observerVersion 1.1.0-candidate.1`, `implementationVersion 1.0.0`, unchanged since `e1617a4`); the surface version covers `apps/three-surface-poc/src` only. A core-only change (extraction, coverage, classification) leaves both binding values unchanged, so a run record stays "ready" against a surface whose facts changed. | Implementation (gen-2): fold the observer revision or the core tree oid into the surface version. Confirms the coordinator's fourth known item. |
| PWB-RECON-04 | Medium (owner) | Readiness is blocked by Butlers data, and the list is wider than recorded: `v1.md:95` colon row (v1-scope, v1-success, success-criterion, catalog-entry, `catalog-count:*` — the spec's own eight-versus-nine scenario is unobservable live), `components.md` parse-failure (topology 0), `frontend.md` active-content, 7/13 `butler.toml` active-content (TOML has no inert context under the approved policy), `roster/qa/MANIFESTO.md` detector hit. | Owner (Section I items 1–2). Confirms and widens the coordinator's first item. |
| PWB-RECON-05 | Low | Human ceiling headroom is 52,066 B direct and 46,426 B on the tailnet mount (the demo measures direct only); the busiest source spends 14 of 16 parse passes. A real run record's readiness section or one more Butlers source can trip a 503 on the tailnet mount first. | Owner (Section I item 4). Sharpens the coordinator's second item. |
| PWB-RECON-06 | Low | Mutant survived: skipping an unreadable decision record inside `lifecycleFor` (`governance-inputs.ts:288`) fails no test; equivalent on the git-tree path, reachable only through the injected `readFile` fallback. | Test-rigor (gen-2, optional): one counterexample. Duplicate of: none. |
| PWB-RECON-07 | Low | The fresh demo and preflight never exercise the tailnet Host mount, `/api/poc/polaris`, or an Origin refusal; only fixture tests and this review did. | Implementation (gen-2, optional): add the three probes to the demo. Duplicate of: none. |
| PWB-RECON-08 | Low (docs) | AGENTS.md "Known gaps" states "Lay and Land's index is excluded" (as of `a3dd1fe`); at `2891522f` the index is classified and `components.md`/`frontend.md` are the exclusions. The only live discovery regression pins `a3dd1fe` and is skipped in the battery. | Docs note; re-pin or parameterize the live test. Duplicate of: none. |
| PWB-RECON-09 | Info | `/polaris/source` bare and `?identity=<population source>` are lawful PWB-REQ-021 traversals (`walkthrough-inputs.ts:190-217`) and the schedule's `surfaceRoutes` names the route on both mounts; the remaining question is record-guidance wording. | Owner wording (Section I item 5). Confirms the coordinator's third item. |

**Gen-2 needed: yes.** It must cover PWB-RECON-01 (human disclosure + parity family),
PWB-RECON-02's implementation half (pillar discovery state and cause on the page), and
PWB-RECON-03 (binding covers the core), each with a pre-fix-failing test and rule-6 evidence,
then a re-run of the fresh demo. PWB-RECON-04/05 cannot be closed by gen-2; they wait on the
owner. Epic closure should wait for gen-2 or an explicit owner acceptance of RECON-01..03 as
tracked debt; the owner walkthrough remains not ready in either case until Section I item 1 or 2
lands.

## Section I — owner-decision candidates (plain language)

1. **The Butlers V1 page does not parse.** One line in `about/heart-and-soul/v1.md` (line 95, the
   Steam module) uses a colon instead of the dash the signed grammar requires, so Polaris cannot
   show V1 scope, V1 success, the success criteria, the catalog, or the eight-versus-nine domain-
   butler disagreement. Choose one: fix that line in Butlers (a Butlers edit, not Syzygy's), or
   amend the signed grammar by a new act, or leave it Unknown. Until one of these, the owner
   walkthrough stays correctly not ready.
2. **Roster and topology files are withheld as active content.** Seven of thirteen `butler.toml`
   files and `about/lay-and-land/frontend.md` contain `<…>`-shaped text, and TOML has no code-span
   protection under the approved policy; `components.md` fails the table grammar. Choose: repair
   the Butlers files, extend the policy's inert-context profile to TOML by a new policy act, or
   accept a roster denominator that stays Unknown.
3. **Spec and Spine has no index file.** Butlers' root index says that pillar lives at `openspec/`
   and points at a directory, not a README. Syzygy treats "no index" as Unknown and therefore marks
   the whole project shape Unknown with an observer-repair route, even though every baseline spec
   is already counted from the Git tree. Choose: declare that a pillar whose start cell is a
   directory is "declared without an index" (a wording amendment), or add an index in Butlers, or
   keep the permanent Unknown. In every case Syzygy should say on the page why the top claim is
   Unknown (PWB-RECON-02).
4. **The human page is within 2.2 % of its byte ceiling on the tailnet mount.** Any growth fails
   closed with a 503. Choose: raise `maxHumanResponseBytes` by a registry amendment act, or direct
   a presentation trim.
5. **Record guidance for the exact-source route.** The code already treats `/polaris/source` (bare
   or with a population identity) as a lawful walkthrough path; the packet that instructs the
   recording session should say so in the owner's words.
6. **State-(1) sentence on the human page** (PWB-RECON-01) needs no decision — it is a
   conformance repair — but the owner should know that, today, the trust-gap sentence is visible
   only to machine readers.

No implementation, signed artifact, policy, registry, Butlers artifact, Beads state or owner
state was changed by this review. The worktree is clean; my daemon is stopped.

VERDICT: CONFIRM WITH EXCEPTIONS
