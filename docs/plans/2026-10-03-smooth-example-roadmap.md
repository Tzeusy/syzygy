# Smooth-example roadmap — 2026-10-03

**Status:** Research and plan, requested by the owner on 2026-10-03 ("please
proceed with doing research on all necessary work left to optimize a smooth
functional example based on our goals, and draft implementation plans for all
necessary steps"). This page is a plan. It is never authority, adopts
nothing and authorizes nothing; each step below names the act that covers
it, and `PROJECT-STATUS.md` says which acts are in force.

The example is the bounded Three-Surface POC (Polaris, Trajectory, Orrery)
over the one configured Butlers repository, plus the Capability 1 daemon.
"Smooth" is measured here as: a fresh checkout builds, the fresh-checkout
demo exits 0, every route answers within its ceiling, a keyboard reader can
traverse Polaris, nothing on a surface offers an action an act forecloses,
and the owner can be invited to the cold-open walkthrough at one frozen
head.

## Outcome

- **Ranked work:** 27 beads carry the `self-drivable` label (4 created
  today, 23 refreshed), each naming its authority, owned files, design and
  acceptance. 8 were ready when this page was written.
- **Owner sitting:** eight owner decisions are batched below (D1–D8).
- **External blocks:** five items, C1–C5.
- **What the live run found broken** [Observed, all in the evidence record]:
  1. The fresh-checkout demo exits 1 on every run since PR #106, by
     construction.
  2. The Polaris keyboard sweep reports 218 violations.
  3. Trajectory still offers a write that an owner ruling forecloses.
  4. Three tests time out under host load.
  5. A reused credential is trusted without checking its file mode.

Evidence:

- `docs/evidence/smooth-example-live-run-2026-10-03.json` — computed by
  script from the retained captures (rule 3). The capture bytes themselves
  stay outside the repository.
- `docs/evidence/pwb-p4-5-fresh-checkout-demo-2026-10-03-roadmap.json` — the
  demo's own record.

## 1. Current end-to-end status

### Measured on 2026-10-03

Run at Syzygy `b5c2bcd`, against the Butlers revision the evidence record
names. A private daemon was started with `--port 0 --state-dir <scratch>`.
Never the loopback daemon on 7478.

| Check | Result | Label |
|---|---|---|
| `npm ci`, `npm run build:poc`, `npm run build` | all exit 0 | [Observed] |
| `/` · `/orrery` | 200 · 200 | [Observed] |
| `/polaris` direct · tailnet `Host` | 200, 1,467,147 B · 200, 1,473,252 B | [Observed] |
| `/polaris` against target · ceiling | under 1,650,000 · under 2,097,152 | [Observed] |
| `/trajectory` | 200, 316,266 B | [Observed] |
| `/api/poc` without · with credential | 401 · 200, 5,719,916 B of 8,388,608 | [Observed] |
| `/api/poc/polaris` · unknown path | 200, 633,283 B · 404 JSON | [Observed] |
| `POST /polaris/reobserve` | 200 in 2.8 s, new evaluation | [Observed] |
| foreign-origin `POST /trajectory/materialize` | 403 | [Observed] |
| Fresh-checkout demo | **exit 1** — invariants `test`, `daemon-exit-clean` | [Observed] |
| Demo tests | 3 timeouts of 2,000 | [Observed] |
| Human/machine parity | 699 tuples over 687 ids, 0 mismatches | [Observed] |
| Browser check | 6 variants, 0 violations | [Observed] |
| Walkthrough preflight | ready | [Observed] |
| Walkthrough readiness | `no-run-record`; owner judgment absent | [Observed] |
| Keyboard sweep (live HTTP) | 1,187 of 1,187 reached; **218 violations** over 709 activations | [Observed] |
| Trajectory | still renders "Materialize this work item" | [Observed] |
| CAP1 daemon on this repo | home says `missing-declaration` | [Observed] |
| `check_governance` | 31 OK, 21 WARN, 0 FAIL | [Observed] |
| Docs partition | 332 of 332 assigned | [Observed] |

Further detail on the keyboard sweep, the project shape and the demo
tests:

- **Keyboard sweep.** The 218 split 109 activation-did-not-reach-target and
  109 focus-did-not-continue-from-target. Every activation from 600 to 708
  fails, with the hash stuck on one source anchor. Activation 599 was the
  *second* link to that same anchor; 404 was the first.
- **Project shape.** 285 sources, 392 items, 416 facts, 0 contradicted. The
  whole-shape claim is Unknown with reason `excluded-content`: 9 sources are
  withheld (8 active content, 1 excluded artifact). The worst source used 14
  of 16 parse passes. 7 precedence rules are declared and 0 applied.
- **Demo tests.** The load average was about 20 on 12 cores. The three
  timeouts were two tests in `production-reobserve.test.ts` and the
  copy-table test in `polaris-copy.test.ts`.

### Why the demo fails by construction

[Observed] `apps/three-surface-poc/src/fresh-checkout-verdict.ts` line 132
requires the daemon's stderr to be empty:

```ts
check('daemon-exit-clean', inputs.daemonExitCode === 0 && inputs.daemonStderr.trim() === '');
```

Since PR #106 (`syzygy-dov.11.1`) the daemon writes one
`daemon-http-outcome` line for each non-2xx response. The demo itself sends
three refusal probes: two unauthenticated machine reads (401) and one
foreign-origin request (403). So stderr is never empty, and the demo has
not exited 0 since its 2026-09-10 record [Inferred from the record dates
and the commit order]. The verdict should accept exactly the demo's own
probe lines and nothing else. That repair is `syzygy-1z3.31`.

A smaller rough edge, recorded here and not scheduled: the 403's logged
reason is `route-non-success`, not a reason that names the browser-origin
refusal.

### Already smooth

- Build and every route.
- Ceilings with headroom: about 183 KB under the working target.
- Parity, the browser check, re-observation and the readiness preflight.
- [Observed] The Butlers repairs ruled at P-60/P-61/P-62 are merged
  upstream. No grammar Unknown remains; the only whole-shape Unknown is the
  nine withheld sources, which is policy working as written.

## 2. Ranked steps

Classes:

- **A** — self-drivable under acts in force, run under the 2026-10-03
  overnight direction (PR #219, merged).
- **B** — needs an owner act, sign-off or ruling.
- **C** — blocked externally.

Every A bead's notes carry its authority path and owned files. Its design
and acceptance carry the plan. Common acceptance for every A step:

- PR merged by rebase with CI green;
- app suite, build, typecheck, `check_governance` 0 FAIL and the partition
  check all pass;
- rule-6 mutants recorded with their fragments and commit;
- no act-bound byte edited.

The `PWB act` and `continuation` named below are
`decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` and
`decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`. The
`rulings` are `decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`.
The `cycles` direction is
`decisions/THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md`.

### Lane P — POC app and core (serial where files or the shared model meet)

| # | Bead | Step | Owns | Authority | After |
|---|---|---|---|---|---|
| 1 | `syzygy-1z3.31` | Demo verdict accepts exactly its own probe diagnostics | `fresh-checkout-verdict.ts` (+test), `fresh-checkout-demo-main.ts` | PWB act task 4.5; continuation; cycles | — |
| 2 | `syzygy-4d15` | Timeouts: cheaper fixtures, or justified per-test timeouts | `production-reobserve.test.ts`, `polaris-copy.test.ts` | cycles | — |
| 3 | `syzygy-1z3.30` | Commit the keyboard sweep tool; diagnose 599/600; repair | new sweep main, `polaris-accessibility.ts`, the renderer file the diagnosis names | PWB act task 4.6 prerequisite | — |
| 4 | `syzygy-c46a` | Rail/drawer browser test timeout | `polaris-accessibility.browser.test.ts` | cycles | — |
| 5 | `syzygy-u05.6` (slices 1–2) | Typed effect authority; the materialize write rendered and refused as foreclosed | core `effect-authority.ts`, `materialization.ts`, `materialize-action.ts` | rulings P-71-Q5, P-75 Q6; cycles | — |
| 6 | `syzygy-u05.4` (slices 1–2) | Legend before the first claim; jargon glossed | `page-shell.ts`, `polaris.ts`, `polaris-copy.ts` | rulings P-75 Q6; cycles | 2, 3 |
| 7 | `syzygy-dov.3.2` | M3 slices 5–6 | Polaris renderer | rulings; continuation | 6 |
| 8 | `syzygy-dov.14.1` | M14 slices 3–4 | `polaris-copy.ts`, `polaris.ts` | rulings P-81 | 7 |
| 9 | `syzygy-dov.4.1` | M4 slices 1, 2, 7: reason and route on every Unknown; pure drafter | `project-shape-model.ts`, three renderers | rulings P-71 | 5, 8 |
| 10 | `syzygy-1z3.32` | Walkthrough-invitation readiness at one frozen head | docs/evidence; a comment on `syzygy-1z3.22` | PWB act task 4.6 preparation | 1–9 |
| 11 | `syzygy-u05.2` | Re-observe: three clocks, superseded identity, `--watch` | core re-evaluation, `main.ts` | rulings P-69, P-75 Q6 | 9 |
| 12 | `syzygy-u05.3` (slice 3) | Ledger headroom on the status line | status line, machine family | rulings P-75 Q6 | 11 |
| 13 | `syzygy-dov.12.1` | M12 slices 1–2: retained record, what-changed band | core record writer, band renderer | rulings P-79; retention direction | 12 |
| 14 | `syzygy-dov.13.2` | M13 slice 5: a population you can get through | `polaris.ts`, parity fixtures | rulings P-80 | 13 |
| 15 | `syzygy-dov.16.4` → `.2` → `.6` → `.3` → `.1` | M16 renderer chain | renderer split, Html type, tokens, AT marker, sweep record | rulings P-82 | 14 |
| 16 | `syzygy-dov.10.4` | gzip only when smaller, ceilings measured before compression | `routes.ts` | `decisions/POLARIS-RESPONSE-CEILING-READING-DIRECTION.md` | 9, 18 |

Step 10 is the capstone of the example. It freezes one head, runs the demo
(exit 0) and the keyboard sweep (0 violations on both mounts), and writes
the readiness record that `syzygy-1z3.22`'s acceptance asks for. It invites
nobody: the walkthrough itself is the owner's (D4).

### Lane G — governance scripts, CAP1 daemon, docs (parallel to lane P)

| # | Bead | Step | Owns | Authority | After |
|---|---|---|---|---|---|
| 17 | `syzygy-u05.6.1` | Credential reuse verifies file and directory owner and mode (N6 slice 4) | `packages/cap1-daemon/src/credentials.ts` (+test) | `decisions/CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md`; rulings P-75 Q6; cycles | — |
| 18 | `syzygy-dov.31` | Ceiling-checker N2/N3 selftests | `check_polaris_response_ceiling_reading.py` | cycles (recorded review notes) | — |
| 19 | `syzygy-wh1` | CG-7e structural check | `check_governance.py` | operating procedure | — |
| 20 | `syzygy-vxlv` | Docs currency: known gaps, rule 11, materialize walkthrough text | `AGENTS.md`, `docs/THREE-SURFACE-POC.md` | operating procedure | 1, 5, 19 |
| 21 | `syzygy-dov.26` | Draft the M9 CC-REV-2 package; stop at "ready for sign-off" | a new candidate package | rulings P-75 (drafting binds nothing) | 19 |
| 22 | `syzygy-l362` | Draft the release-label delta; stop at "ready for sign-off" | a new candidate delta | owner direction of 2026-10-02 on the bead | 21 |
| 23 | `syzygy-t69g` | Recorder CONTESTED rows; one history review, then stop | `record_polaris_understanding_adoption.py` | operating procedure; recorded finding | 22 |

Notes on lane G:

- `syzygy-wh1` touches `check_governance.py`; branch it from a main that
  already carries PR #220 (merged).
- `syzygy-u05.6.1` only narrows: it adds a fail-closed refusal and widens
  nothing. A 0700 state directory was not required, because a 0755
  directory holding a 0600 file exposes no token.

**Ready now (no open blocker):** 1, 2, 3, 4, 5, 17, 18 and 19. Two lanes can
run them in parallel without sharing a file. Lane P's serial order exists
because the shared `PocModel` is WIP-one under the cycles direction, and
because steps 6–9 and 14–16 edit the same renderer files.

### Not scheduled (A-eligible, off the example path)

- `syzygy-u05.6` slice 3 (the boundary register);
- `syzygy-u05.11`'s remainder, apart from rule 11, which step 20 takes;
- `syzygy-u05.18`, `syzygy-dov.34`, `syzygy-dov.15.1`;
- `syzygy-u05.5`, and the `syzygy-u05.14`/`syzygy-u05.15` drafts;
- the N9, N10, N12 and N13 deltas;
- `syzygy-e3e`, CAP1 runtime hardening, which only bites once a real project
  is declared (D5).

These stay off the loop so that it finishes the example first.

## 3. Owner decisions, batched for one sitting

None of these is drafted here as an act. Each names what would be asked.

| # | Decision | Unblocks | Bead |
|---|---|---|---|
| D1 | One implementation authorization covering the amendments signed 2026-10-01/02 (machine-view, opening-band, render-mode, item-depth, dismissal-expiry, missing-currency, container-shape profile) and tree-framing v1.0 (PR #220) | tree-form openings, the amendments' code, M8 re-shape | `syzygy-dov.35`, `syzygy-73e.20`, `syzygy-dov.8.2`, `syzygy-dov.8.3` |
| D2 | The continuation phrase for M2 slice 5 | currency and briefing fields | `syzygy-dov.19` |
| D3 | Whether the P-71-Q5 return path (the write into Butlers' tracker) should ever be demonstrated. If yes: three ordered acts — a dated act naming the write, a registry `writeSurface` amendment, a fresh implementation authorization | M4 slice 6 | — |
| D4 | The owner's cold-open walkthrough at the head step 10 names, then the judgment, then the cycle report | PWB 4.6, 5.3 | `syzygy-1z3.22`, `syzygy-1z3.25` |
| D5 | Capability 1 on a real project: adopt the trusted-bootstrap consent candidate, a bounded implementation authorization, one project declaration and consent | CAP1 beyond `missing-declaration` | `syzygy-u2a` and children |
| D6 | The nine withheld sources: accept the honest Unknown, amend the active-content policy, or change Butlers | the whole-shape claim | — |
| D7 | Later sitting: sign the drafts from steps 21 and 22; optional `syzygy-dov.24` and `syzygy-dov.25` acts; `syzygy-dov.23` scenario; `syzygy-hfp7`; `syzygy-8de`; release the owner-gated `syzygy-1z3.28` | M9 slices 4–8; release labels | as named |
| D8 | Where an owner's note may be stored (the retention direction §7 excludes it today) | M12 slice 3 | `syzygy-dov.12.2` |

D1 and D4 matter most for the example. D3's default — never demonstrated —
costs the example nothing once step 5 renders the write as foreclosed.

## 4. Externally blocked

| # | Block | What unblocks it |
|---|---|---|
| C1 | Nine Butlers sources withheld as active content or an excluded artifact | D6, or a change in Butlers |
| C2 | Host load (load average 7–28 on 12 cores) causes test timeouts | Step 2 removes the dependence; otherwise run on a quieter host |
| C3 | The overnight loop's own authority, and the tree-framing sign-off | **Resolved**: PR #219 and PR #220 merged |
| C4 | Butlers PR #4066 | **Resolved**: merged 2026-09-07 |
| C5 | Generalizing the generator needs a second real project | A second consented repository (an owner act; outside the one-repository bound) |

## Retention

[Observed] The capture bytes are retained outside the repository. The
evidence record carries each capture's sha256 digest and no Butlers text.
