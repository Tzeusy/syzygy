# PWB recovery gen-2 reconciliation review — raw

Review date: 2026-09-06
Reviewer: independent fresh-context gen-2 reconciliation reviewer (bead syzygy-1z3.24.9)
Syzygy subject: worktree `/home/tze/GitHub/syzygy/.worktrees/parallel-agents/syzygy-1z3.24.3`,
branch `agent/syzygy-1z3.24.9`, HEAD `9b28663804281f5419c41ea70b7ede52f8ff6597`,
`git status --short` empty at start and at end.
Observed Butlers subject: `/home/tze/GitHub/butlers` at HEAD
`ec8b1f6cd529a976700a1360acfac1efc29f9762` at start and at end of the review (the retained
gen-2 demo observed the same head; gen-1 observed `2891522f`).
Gen-1 review answered: `docs/reviews/2026-09-06-pwb-recovery-reconciliation-packet.md`
(PWB-RECON-01..09, CONFIRM WITH EXCEPTIONS, at `d92910c`) and
`docs/reviews/R-PWB-RECOVERY-RECONCILIATION-GEN1-RAW.md`.
Runtime: my own daemon from a fresh clone of the worktree (`<scratch>/recon2/clone`, HEAD
`9b28663`), loopback `127.0.0.1:33221`, ephemeral port, started and stopped by this review
(exit on SIGINT, stderr 0 bytes); the fresh-checkout demo's own daemon at `127.0.0.1:35989`.
I signalled no process I did not start; at my final check no process with pid 2851269 was
listed by `ps` — I did not touch it.
Mode: read-only in the worktree (no edit, commit, checkout, stash or `bd` mutation; `bd show`
only); clone-based battery, demo and every mutation (rule 7); every guard relied on is either
checked against retained evidence by predicate or mutated in my clone (rule 6); every universal
claim carries its sweep and denominator (rules 2, 9); requirement claims quote clause text
(rule 8); `grep -F`/Python for load-bearing matches (rule 1). Butlers bodies were read only
through Syzygy's daemon; the one direct Git call was `git cat-file -e ec8b1f6:openspec/README.md`
(existence, no body). No Butlers write.

## Verdict

**CONFIRM WITH EXCEPTIONS.**

[Observed] PWB-RECON-01, the page half of PWB-RECON-02 and PWB-RECON-03 are repaired in the
code the worktree serves: reverting each repair's implementation hunks in my clone makes the
new tests fail (78 of 103, 14, 5 of 18), the live human page on both mounts renders the exact
PWB-REQ-005 sentence once per authority and one discovery state per pillar with the Unknown
pillar's reason, route and the degradation state, and the walkthrough surface version is now
`polaris@` + sha256 over both source trees (recomputed by hand: `e64a10980701`). Fifteen of my
eighteen clone mutants and one mount-dependent mutant were killed. A fresh clone of `9b28663`
builds, passes 1537 / 3 skipped of 1540 tests, and its own fresh-checkout run exits 1 on exactly
`preflight-ready` with the same three Butlers-data limbs and identical detail as the retained
gen-2 record. Nothing under `openspec/**` or `.syzygy/**` changed in the six repair commits; the
governance check reports 0 FAIL; the PWB-REQ-005 (195) and PWB-REQ-022 (84 + 2) denominators
are untouched.

[Observed] The exceptions are test-rigor gaps in the new RECON-02 gates, not conformance
gaps: three of my mutants survived — a route rendered for the wrong discovery reason, the
preflight's page-wide route check removed, and the core model dropping Unknown pillars from
`discovery` when only the core test runs (the page test kills it). The retained gen-2
mutation-run record names its twelve mutants but stores no fragments, and the retained demo
head `1ad69cc` is reachable from no ref, so both are reproducible only by reconstruction (I
reconstructed and re-ran equivalents). PWB-RECON-04, -05, -08 (live test re-pin) and -09 are
unchanged owner or docs items. No gen-3 is needed: the remaining items are ordinary beads.

## Section A — disposition register (PWB-RECON-01..09)

Repair commits are the six `[syzygy-1z3.24.8]` commits on `main` above `804339e`:
`fe1c5f2` (fix), `cf083ae` (preflight tests), `2fdf801` (demo probes), `9685bd8` (demo shape
summary), `278940a` (evidence), `9b28663` (docs). "Mine" = mutation I applied in my clone
(Section C); "revert" = Section B.

| ID | Repair commit(s) | Code evidence (file:line at `9b28663`) | The one gate | Disposition | Evidence I checked |
|---|---|---|---|---|---|
| PWB-RECON-01 | `fe1c5f2` | `apps/three-surface-poc/src/polaris.ts:638-648` `authorityLine`: per authority `<span data-parity-field="authority-disclosure" data-authority=…>${escapeHtml(entry.disclosure)}</span>` beside the state marker; disclosure derives from `packages/three-surface-poc-core/src/authority-disclosure.ts:21-22,54` (`STATE_1_DISCLOSURE`, byte-equal to the spec sentence, ASCII apostrophe both sides) | `polaris-project-shape.test.ts` "renders the exact state-(1) sentence once per state-(1) authority…"; `surface-routes.test.ts` "…both directly and through the tailnet Host mount"; parity family `parity-field:authority-disclosure` (`polaris-parity-sweep.test.ts:341`); preflight limb `authority-disclosure-missing` (`walkthrough-preflight.ts:256-278`, six counterexamples) | **repaired** | Revert: 78/103 fail. Mine: 4 killed (registry sentence dropped 70; state shown instead of sentence 71; duplicated 70; dropped on the tailnet mount only 1 — surface-routes). Live (Section D): sentence ×3 on direct and tailnet, text equal to `/api/poc` `authority.authorities[].disclosure` ×3. Retained: parity-markers sweep `polaris-authority-disclosure-missing/-changed` killed; gen-2 run `preflight-authority-*` 4/4 killed. |
| PWB-RECON-02 (page half) | `fe1c5f2` | core `project-shape-model.ts:317,643` (`discovery: observation.manifest.pillars`); `polaris.ts:597-636` `pillarRoute` (seven reasons, exhaustive by type), `discoveryLine` (`shape-pillar-state` per pillar, `shape-pillar-reason` per Unknown pillar, route text), `degradationLine` (`shape-degradation-state` or the copy sentence `sentence.no-degradation`, `polaris-copy.ts:185-187`); rendered at `polaris.ts:945-946` | `polaris-project-shape.test.ts` "discloses every pillar's discovery state, and a missing pillar index with its reason and a cause-correct route" + "…degradation state…"; core `project-shape-model.test.ts:490-496`; parity families `shape-pillar-state/-reason`, `shape-degradation-state` with sweep states `observed-excluded`, `observed-undiscovered`; preflight limb `discovery-undisclosed` (`walkthrough-preflight.ts:280-296`, four counterexamples) | **repaired** (page); the cause itself stays an owner item (gen-1 item 3) | Revert page: the two new page tests fail; revert core: 14 fail (`discovery` undefined). Mine: killed — reason marker dropped (46), degradation always "none" (47), route text of `root-missing` for `index-missing` (1), discovered-only filter under the page gate (2). **Survived** — route text of `index-unavailable` for `index-missing` (0/103), preflight route check removed (0/41), discovered-only filter under the core gate alone (0/29) → PWB-RECON-10/11/12. Live: `spec-and-spine — unknown (index-missing-at-revision; route: the home openspec carries no index at openspec/README.md …)`, `Degradation: Partial snapshot (someSourcesUncapturedOrOverLimit; pillar spec-and-spine unknown).` on both mounts; machine `discovery[2]` and `degradation` equal. `openspec/README.md` absent at `ec8b1f6` (`cat-file -e` exit 128; `openspec` tree exists). |
| PWB-RECON-03 | `fe1c5f2` | `walkthrough-inputs.ts:77,84-97`: `POLARIS_SURFACE_TREES = ['apps/three-surface-poc/src', 'packages/three-surface-poc-core/src']`; `pwbSurfaceVersion` = `polaris@` + first 12 hex of sha256 over the two tree ids joined by `\n`; `polaris@unresolved` on any failure or non-hex id | `walkthrough-inputs.test.ts` `pwbSurfaceVersion` (4 tests; expected value computed in the test, not imported) + `walkthroughJudgmentInputsFor` binding test | **repaired** | Revert: 5/18 fail. Mine: tree order swapped (3), unhashed prefix (4), core id replaced by a constant (4) — all killed. Hand recomputation: `printf '%s\n%s' <app oid> <core oid> \| sha256sum` = `e64a1098 0701…`; daemon prints `polaris@e64a10980701`; `git diff --stat 1ad69cc HEAD -- <both src trees>` empty, so the retained record's version binds the same bytes. The evaluation identity (`walkthrough-readiness.ts:119-128`) still digests deterministic inputs only, so it is unchanged between `1ad69cc` and `9b28663` — the surface version is the code-bearing half of the binding, as the repair intended. |
| PWB-RECON-04 | — | — | owner items 1–2 | **owner-item** (unchanged) | My demo and daemon at `ec8b1f6`: same three limbs (`account-statement-unbacked` v1-scope/v1-success; `population-empty` catalog-entry/topology-component; `population-unreconciled` success-criterion/catalog-entry/topology-component `excluded-content`). Nothing in `804339e..HEAD` touches grammar, policy, registry or Butlers. |
| PWB-RECON-05 | — | ceiling `project-shape-observation.ts:81` / registry `maxHumanResponseBytes: 2097152` | owner item 4 | **owner-item** (unchanged; headroom shrank) | Live: direct 2,047,268 B (headroom 49,884), tailnet 2,052,908 B (headroom 44,244) — the page grew 2,182 B with the new lines; gen-1 measured 52,066 / 46,426. `limitBreaches: []`. The demo still measures direct bytes only for the ceiling; the tailnet probe records bytes but no ceiling comparison. |
| PWB-RECON-06 | `fe1c5f2` (test only; `governance-inputs.ts:288` unchanged since `804339e`) | `governance-inputs.ts:287-288`: `readText` undefined → `throw new Error('governance lifecycle record disappeared: …')` | `governance-inputs.test.ts` `it.each(['list','read','decode','vanish'])` "fails closed when lifecycle vanish fails" | **repaired** (test-rigor) | Not pre-fix-failing by nature (the throw pre-existed; revert of the impl file: 17/17 pass). Mine: `if (text === undefined) continue;` → killed (1/17). |
| PWB-RECON-07 | `2fdf801`, `9685bd8` | `fresh-checkout-demo-main.ts:149-171,409-433` (`requestWithHeaders` via `node:http`, tailnet Host + Origin, `/api/poc/polaris` 401/200 kind/citable, foreign Origin); `fresh-checkout-verdict.ts:24-26,115-117` (19 invariants) | `fresh-checkout-verdict.test.ts` (11 new counterexamples; table covers every invariant; length 19) | **repaired** | Revert verdict: 12/41 fail. Mine: disclosure-count equality dropped (2), any-403 accepted (1), citable ignored (2) — killed. Live demo: `tailnet mount 200 (links prefixed, 3 disclosures); presentation 401/200 polaris-presentation; foreign origin 403 browser-origin-refused`. Residual: `fresh-checkout-demo-main.ts` itself has no unit gate (live-only), as before. |
| PWB-RECON-08 | gen-1 handoff (docs) | AGENTS.md Known gaps now names `frontend.md` and 7 of 13 `butler.toml` (current); `project-shape-discovery.live.test.ts:24` still pins `a3dd1fe08a1…`, skipped in the battery (3 skipped files) | — | **open** (docs half done; live test re-pin not done) | `grep -F a3dd1fe` hits lines 24 and 36; the 24.8 diff does not touch the file. |
| PWB-RECON-09 | — | `walkthrough-inputs.ts` traversal predicate unchanged | owner item 5 (wording) | **owner-item** (unchanged) | Not in the 24.8 diff. |

Denominator for the register: 9 of 9 gen-1 ids dispositioned; 5 `repaired` (01, 02-page, 03,
06, 07), 1 `open` (08), 3 `owner-item` (04, 05, 09); 0 `declined`.

## Section B — pre-fix-failing confirmation

Method: in my clone, `git checkout 804339e -- <implementation file(s)>` (parent of `fe1c5f2`),
`npx vitest run <new test files>`, then `git checkout HEAD -- <files>`; `git status` showed 0
dirty tracked files after each group (`<scratch>/recon2/prefix.log`).

| Group | Reverted | Tests run | Result |
|---|---|---|---|
| RECON-01 + RECON-02 page | `polaris.ts`, `polaris-copy.ts` | `polaris-project-shape.test.ts`, `surface-routes.test.ts`, `polaris-parity-sweep.test.ts`, `walkthrough-preflight.test.ts` | **78 failed / 25 passed (103)**, 4/4 files failed; named among them: both new page tests, the surface-routes tailnet test, every preflight "and nothing else" case (the two new limbs fire). |
| RECON-02 core | `project-shape-model.ts` | `project-shape-model.test.ts`, `polaris-project-shape.test.ts` | **14 failed** (`TypeError: Cannot read properties of undefined (reading 'map')` — `shape.discovery` absent) incl. the core discovery assertion and all three new page tests. |
| RECON-03 | `walkthrough-inputs.ts` | `walkthrough-inputs.test.ts` | **5 failed / 13 passed (18)**: the four `pwbSurfaceVersion` tests and the binding test. |
| RECON-07 | `fresh-checkout-verdict.ts` | `fresh-checkout-verdict.test.ts` | **12 failed / 29 passed (41)**: all eleven new counterexamples plus the coverage/length test. |
| RECON-06 | `governance-inputs.ts` (unchanged in 24.8) | `governance-inputs.test.ts` | 17/17 pass — the throw pre-dates 24.8; the repair is the test, gated by my mutant (Section C). |

## Section C — rule-6 evidence

### Retained evidence, checked by predicate

| Record | What it claims | What I checked | Finding |
|---|---|---|---|
| `docs/evidence/pwb-recon-gen2-repair-mutation-run-2026-09-06.json` | 12/12 killed at pre-rebase `c2d75c8` (first round `cff7e15`: 8 killed, 4 preflight survivors, one counterexample each added) | JSON parsed: `summary {mutations:12, killed:12, survived:0}`; 12 result rows each `killed:true`, `failingTests ≥ 1`, `exitCode 1`; ids cover 8 preflight, 3 surface-version, 1 core-discovery predicates. **The record stores ids, files and test files only — no `old`/`new` fragment** — so no mutant can be re-applied from the record. Both commits exist as loose objects here (`git cat-file -t` = commit) but neither is on any ref. | Counts consistent; not reproducible from the file → PWB-RECON-13. I re-created and re-ran equivalents for every predicate class (below). |
| `docs/evidence/pwb-p4-2-mutation-sweep-2026-09-06-parity-markers.json` | 32/32 killed incl. six new literals | `summary {planned:32, killed:32, survived:0, restoreFailures:0}`, `uncommittedChanges: []`, commit `c2d75c8…`; the six new ids (`polaris-authority-disclosure-missing/-changed`, `polaris-pillar-state-missing/-changed`, `polaris-pillar-reason-changed`, `polaris-degradation-missing`) present with `killed:true`; the literals are in `pwb-mutation-sweep.ts:539-589` with their fragments, so this family is reproducible. | Consistent. |
| "nine verdict/lifecycle mutants killed in-session" | not retained | Cannot be checked; I ran 3 verdict + 1 lifecycle mutants of my own (all killed). | Unretained claim — carry as reconstructed only. |

### My mutants (clone, `<scratch>/recon2/mutants-result.json`, `mutants2-result.json`; each restored byte-for-byte, sha256 equal)

| id | file | fragment (old → new) | tests | result |
|---|---|---|---|---|
| R01-disclosure-dropped-for-registry | `polaris.ts` | `${escapeHtml(entry.disclosure)}` → `${entry.authority === 'registry' ? '' : escapeHtml(entry.disclosure)}` | page set (4 files) | KILLED 70/103 |
| R01-disclosure-shows-state-not-sentence | `polaris.ts` | `…entry.disclosure…` → `…entry.state…` in the disclosure span | page set | KILLED 71/103 |
| R01-disclosure-duplicated-per-authority | `polaris.ts` | disclosure span emitted twice | page set | KILLED 70/103 |
| R01-disclosure-dropped-on-tailnet-mount | `polaris.ts` | `${activeMountPrefix === '' ? escapeHtml(entry.disclosure) : ''}` | page set | KILLED 1/103 — only `surface-routes.test.ts` (the sweep and preflight render the direct mount only) |
| R01-preflight-state1-sentence-check-dropped | `walkthrough-preflight.ts` | the `STATE_1_LABEL … STATE_1_SENTENCE` guard removed | preflight test | KILLED 1/41 ("page and evaluation both carry another sentence") |
| R02-route-text-of-index-unavailable-for-index-missing | `polaris.ts` | `case 'index-missing-at-revision'` returns the `index-unavailable` route text (`the index ${index} could not be read: restore its body in Butlers, then a new snapshot`) | page set | **SURVIVED 0/103** |
| R02-route-text-of-root-missing-for-index-missing | `polaris.ts` | same case returns the `root-missing` text | page set | KILLED 1/103 (only because the index path disappears) |
| R02-pillar-reason-marker-dropped | `polaris.ts` | `shape-pillar-reason` span removed from the Unknown arm | page set | KILLED 46/103 |
| R02-degradation-always-none | `polaris.ts` | `if (degradation === undefined \|\| true) return …none…` | page set | KILLED 47/103 |
| R02-core-discovery-discovered-only (core gate) | `project-shape-model.ts` | `discovery: …pillars.filter((p) => p.state === 'discovered')` | `project-shape-model.test.ts` | **SURVIVED 0/29** |
| R02-core-discovery-discovered-only (page gate) | same | same | `polaris-project-shape.test.ts`, parity sweep | KILLED 2/58 |
| R02-preflight-route-check-dropped | `walkthrough-preflight.ts` | `if (!html.includes('then a new snapshot')) problems.push(…)` removed | preflight test | **SURVIVED 0/41** |
| R03-tree-order-swapped | `walkthrough-inputs.ts` | `trees.join('\n')` → `[...trees].reverse().join('\n')` | inputs test | KILLED 3/18 |
| R03-unhashed-prefix-of-app-tree | `walkthrough-inputs.ts` | digest replaced by `trees.join('\n').slice(0, 12)` | inputs test | KILLED 4/18 |
| R03-core-tree-replaced-by-constant | `walkthrough-inputs.ts` | `trees.push(path === 'apps/three-surface-poc/src' ? tree : 'core-ignored')` | inputs test | KILLED 4/18 |
| R06-vanished-record-skipped | `governance-inputs.ts` | `throw new Error('governance lifecycle record disappeared…')` → `continue` | governance-inputs test | KILLED 1/17 |
| R07-verdict-tailnet-disclosure-count-ignored | `fresh-checkout-verdict.ts` | disclosure equality and `> 0` dropped from `tailnet-mount-served` | verdict test | KILLED 2/41 |
| R07-verdict-origin-any-403 | `fresh-checkout-verdict.ts` | reason equality dropped | verdict test | KILLED 1/41 |
| R07-verdict-presentation-citable-ignored | `fresh-checkout-verdict.ts` | `presentationCitable === false` dropped | verdict test | KILLED 2/41 |

Denominator: 19 mutants, 16 killed, 3 survived; 0 restore failures.

## Section D — surfaces

All from my daemon at `127.0.0.1:33221` (Butlers `ec8b1f6`), requests through `node:http`
with explicit `Host`/`Origin` (`<scratch>/recon2/probe-result.json`, page bytes retained as
`direct-polaris.html`, `tailnet-polaris.html`, `api-poc.json`).

| Channel | Observed |
|---|---|
| Human direct `/polaris` | 200, 2,047,268 B; `authority-disclosure` markers 3 (consent, policy, registry), each text = `Owner-trusted only; same-tree forgeable from Syzygy's perspective. Digest detects drift, not authorship or attendance.` (apostrophe served as `&#39;`, decoded); `authority-state` ×3 `owner-adopted (bootstrap, uncorrelated)`; `shape-pillar-state` ×5 (`heart-and-soul — discovered`, `legends-and-lore — discovered`, `spec-and-spine — unknown`, `lay-and-land — discovered`, `craft-and-care — discovered`); `shape-pillar-reason` ×1 `index-missing-at-revision` (`data-pillar="spec-and-spine"`); `shape-degradation-state` ×1 `Partial snapshot`, `data-shape-degradation="someSourcesUncapturedOrOverLimit"`; raw `same-tree forgeable` count 3; page shows `polaris@e64a10980701` / `pwb-eval-5bce8f59f94b4f8cbfbd1a61` |
| Human tailnet (`Host: tzeusy.parrot-hen.ts.net`) | 200, 2,052,908 B; every marker list above identical text-for-text; 0 root-absolute hrefs without `/butlers-syzygy` |
| Foreign `Origin` on `/polaris` | 403 `{"served":"nothing","reason":"browser-origin-refused"}` |
| Machine `/api/poc` | 401 without bearer; 200 with, 4,978,646 B (same size on the tailnet Host); `projectShape.authority.authorities[].disclosure` = the sentence ×3, `authorizationMode: owner-trusted-bootstrap`; `discovery` = five pillars, `[2]` = `{spec-and-spine, unknown, index-missing-at-revision, root: openspec, indexPath: openspec/README.md}`; `degradation` = `{someSourcesUncapturedOrOverLimit, Partial snapshot, source-uncaptured-or-unreachable, "pillar spec-and-spine unknown"}`; whole-shape claim `Unknown` / `source-uncaptured-or-unreachable`; `limitBreaches: []` |
| Machine `/api/poc/polaris` | 401 without; 200 with, 497,011 B, `kind: polaris-presentation`, `citable: false` |
| Parity I measured | human = machine for: disclosure 3 = 3, authority-state 3 = 3, pillar-state 5 = 5, pillar-reason 1 = 1, degradation-state 1 = 1 — on both mounts. Demo comparator (my run): 529 tuples / 528 human ids / 528 machine ids / 0 mismatching / 0 absent either way. |
| Human − machine | none of the gen-1 deltas remain (sentence, discovery cause and degradation state are now on the page); the requirement text stays machine-form-only by design. |

Discovery line, verbatim from the page: `Discovery: heart-and-soul — discovered
(about/heart-and-soul/README.md, 6 named); legends-and-lore — discovered
(about/legends-and-lore/README.md, 33 named); spec-and-spine — unknown
(index-missing-at-revision; route: the home openspec carries no index at openspec/README.md at
this revision: add that index in Butlers, then a new snapshot; or an owner gate amending the
discovery rule. No policy change is involved); lay-and-land — discovered
(about/lay-and-land/README.md, 8 named); craft-and-care — discovered
(about/craft-and-care/README.md, 7 named).` [Observed] The route is cause-correct for the live
state; [Observed] no test or preflight limb would notice a cause-incorrect route that keeps the
index path and "then a new snapshot" (Section C survivors).

## Section E — fresh clone battery and demo

Clone: `git clone <worktree> <scratch>/recon2/clone` → HEAD `9b28663`; `npm ci` exit 0; `npm run
build` exit 0; `npx vitest run`: **112 files passed / 3 skipped (115); 1537 tests passed / 3 skipped
(1540)**, exit 0 (skipped: `project-shape-discovery.live.test.ts`, two core `*.live.test.ts`).
Demo: `npm run poc:fresh-checkout-demo -- --repo /home/tze/GitHub/butlers --retain-dir
<scratch>/recon2/retain --date 2026-09-06-gen2-reviewer` from the clone; evidence
`<scratch>/recon2/clone/docs/evidence/pwb-p4-5-fresh-checkout-demo-2026-09-06-gen2-reviewer.json`.

| Field | Retained gen-2 (`…-2026-09-06-gen2.json`) | Mine |
|---|---|---|
| Clone head / matches source | `1ad69cc…` / true | `9b28663…` / true |
| Butlers observed = model | `ec8b1f6…` | `ec8b1f6…` |
| Surface version / evaluation identity | `polaris@e64a10980701` / `pwb-eval-5bce8f59f94b4f8cbfbd1a61` | identical |
| Install / build / test | 0 / 0 / junit 1540 tests, 0 failures, 0 errors | 0 / 0 / junit 1540, 0, 0 (38.2 s) |
| Invariants (19) / failed | 19 listed / `[preflight-ready]` | identical list / `[preflight-ready]` |
| Probes | tailnet 200, prefixed links, 3 disclosures, 2,052,908 B; presentation 401 / 200 `polaris-presentation` `citable:false` 497,011 B; foreign Origin 403 `browser-origin-refused` | identical values (only the html sha256 differs — evaluation instant) |
| Parity | 529 / 528 / 0 / 528 / 528 / 0 / 0 | identical |
| Source routes | 185 identities, 175 rendered | identical |
| Browser check | 6 variants, 0 violations at `1ad69cc` | 6, 0 at `9b28663` |
| Human direct bytes | 2,047,268 | 2,047,268 |
| Preflight | not ready: `account-statement-unbacked` (v1-scope, v1-success), `population-empty` (catalog-entry, topology-component), `population-unreconciled` (success-criterion, catalog-entry, topology-component: denominator Unknown `excluded-content`) | identical limbs and identical detail strings |
| Discovery / degradation | Spec and Spine `index-missing-at-revision` (root `openspec`); `Partial snapshot` | identical |
| Daemon exit / stderr | 0 / empty | 0 / 0 bytes |
| Exit | 1 (`unhealthy: preflight-ready`) | **1** (`unhealthy: preflight-ready`) |

Drift: none in any recorded value; the only differences are the observer commit, timestamps
and the digests that carry them. [Observed] `1ad69cc` is reachable from no ref in this
worktree (`git for-each-ref --contains` empty; the object survives loose); its tree differs
from `9b28663` in 10 files, none under `apps/**` or `packages/**` (`git diff --name-only
1ad69cc HEAD`: three `.syzygy/governance/**` docs, `AGENTS.md`, `CONTRIBUTING.md`,
`PROJECT-STATUS.md`, `SECURITY.md`, two `docs/*.md`, the gen-2 evidence file) — the co-lead's
docs commits, as claimed. The surface version, not the head, is the reproducible anchor.

## Section F — regression and scope check

`git diff --name-status 804339e..HEAD`: 21 paths, classified: implementation 7
(`polaris.ts`, `polaris-copy.ts`, `walkthrough-inputs.ts`, `walkthrough-preflight.ts`,
`fresh-checkout-verdict.ts`, `fresh-checkout-demo-main.ts`, core `project-shape-model.ts`);
tests 8 (the sibling `*.test.ts` of each of those plus `surface-routes`, `governance-inputs`,
`polaris-parity-sweep`, `polaris-project-shape`); tooling 1 (`pwb-mutation-sweep.ts`, six
literals); docs 2 (`AGENTS.md` one guardrail, `docs/PWB-IMPLEMENTATION-PLAN.md` gen-1 and gen-2
notes); evidence 3 (new JSON). **0 paths under `openspec/**` or `.syzygy/**`** (`git diff
--name-only 804339e..HEAD -- openspec .syzygy | wc -l` = 0), so no digest-bound artifact,
policy, registry, consent or Butlers artifact changed. `python3 scripts/check_governance.py`:
**33 OK, 19 WARN, 0 FAIL (52 checks)**; CG-7d 47 quotations, 0 findings; CG-7e 27 files, 0
findings. `npx openspec validate --all --strict`: 3 passed, 0 failed. Denominators unchanged:
`body-read-authority.test.ts:449` asserts 195; `walkthrough-judgment.test.ts:398-399` asserts
84 present-invalid (+ 2 absent by construction); neither file is in the diff. The walkthrough
readiness evaluator (`walkthrough-readiness.ts`) and the PWB-REQ-022 evaluator are not in the
diff. Copy oracle: the three new copy rows (`label.discovery`, `label.degradation`,
`sentence.no-degradation`) are role `epistemic-disclosure` and the copy test passes in the
clone battery. Bead state read-only: `syzygy-1z3.24.8` closed (PR #21), `syzygy-1z3.24.9` in
progress, epic `syzygy-1z3.24` open; `syzygy-1z3.25` open and unchanged; no bead was mutated.

Instrument blind spots that remain (not regressions): the preflight's ten limbs still run on the
direct render only (the tailnet mount is covered by the demo's disclosure-count equality and by
`surface-routes.test.ts`, not per limb); `fresh-checkout-demo-main.ts` has no unit gate; the
retained gen-2 mutation record cannot be re-applied from its bytes.

## Section G — findings and gen-3 need

| ID | Severity | Finding | Route |
|---|---|---|---|
| PWB-RECON-10 | Low (test rigor) | The "cause-correct route" for an Unknown pillar is not gated: `pillarRoute` returning the `index-unavailable` text for `index-missing-at-revision` survives all 103 page/sweep/preflight tests (the page test checks only the index path and "then a new snapshot"; the preflight checks a page-wide substring). | One counterexample per reason in `polaris-project-shape.test.ts` asserting the route's distinguishing phrase; ordinary bead. Duplicate of: none. |
| PWB-RECON-11 | Low (test rigor) | Preflight limb `discovery-undisclosed`'s route check (`walkthrough-preflight.ts:291`, `html.includes('then a new snapshot')`) has no isolating counterexample: removing it survives 41/41; it is also satisfied by any pillar's route anywhere on the page, not the Unknown pillar's. | Add a counterexample and scope the check to the pillar's own discovery entry; ordinary bead. Duplicate of: PWB-RECON-10 family (same gate), listed separately because it is a different instrument. |
| PWB-RECON-12 | Low (test rigor) | The core gate for `ProjectShape.discovery` covers only the all-discovered fixture: filtering Unknown pillars out of `discovery` survives `project-shape-model.test.ts` (0/29) and is caught only by the app page test. The retained `model-discovery-empty` mutant was killed by the same assertion but does not cover this shape. | One core assertion on an undiscovered fixture (the `index-missing` texts already exist in the app fixture); ordinary bead. Duplicate of: none. |
| PWB-RECON-13 | Info (evidence quality) | `pwb-recon-gen2-repair-mutation-run-2026-09-06.json` records mutant ids and outcomes but no fragments, and cites pre-rebase commits (`c2d75c8`, `cff7e15`) that no ref reaches; the "nine verdict/lifecycle mutants" are not retained at all. The record is consistent but not re-runnable from its bytes; I reconstructed equivalents (Section C). | Retain fragments (as the parity-markers sweep does) in future rule-6 records; no repair needed for this bead. Duplicate of: none. |
| PWB-RECON-05 (update) | Low (owner) | Headroom shrank to 49,884 B direct / 44,244 B tailnet (2.1 % of the ceiling on the tailnet mount) after the new disclosure lines. | Owner item 4 stands; no new id. |

**Gen-3 needed: no.** The three required repairs are confirmed by revert, mutation and live
observation; the fresh demo exits only on Butlers-data limbs; nothing regressed. PWB-RECON-10..12
are test-rigor debts on the new gates (the live route is cause-correct) and can be closed by
ordinary beads with their own rule-6 evidence; they do not require a third independent
reconciliation. The owner walkthrough remains not ready for the reasons the owner already holds
(PWB-RECON-04), not for any Syzygy-side gap.

## Section H — owner-decision candidates (plain language)

1. No new decision arises from gen-2. The gen-1 items stand unchanged: the Butlers V1 page's
   colon line (item 1), the roster TOML and topology table withheld or unparsed (item 2), the
   Spec and Spine home without an index (item 3 — the page now says so and points at
   `openspec/README.md`; the choice between adding an index, amending the discovery rule, or
   keeping the Unknown is still the owner's), the byte ceiling (item 4 — the margin is now
   44 KB on the tailnet mount), and the record-guidance wording for the exact-source route
   (item 5).
2. Whether to close epic `syzygy-1z3.24` with PWB-RECON-10..13 carried as ordinary beads, or to
   hold it until those test-rigor gaps are closed with evidence. This review recommends the
   former: none of them changes what the page says today.

No implementation, signed artifact, policy, registry, Butlers artifact, Beads state or owner
state was changed by this review. The worktree is clean at `9b28663`; my daemon is stopped; the
clone carries only my untracked evidence file.

VERDICT: CONFIRM WITH EXCEPTIONS
