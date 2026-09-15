# Feature request M11 — Operability: the daemon can say what it is serving, and a breach that serves nothing leaves a trace

> **Candidate — binds nothing.** Bead `syzygy-dov.11`, move M11 of the
> 2026-09-13 vision pursuit (`docs/pursuits/2026-09-13-vision-pursuit.md`),
> written in the shape of `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md` and
> its nine siblings. Planning only: nothing here authorizes implementation.
> Each question below names the arms the owner may take; naming a lawful arm
> is not a ruling that a slice is authorized. The owner disposes.

Date: 2026-09-15. Author: a funnel session (Claude), for the owner.

Size: **small** (slices 1 and 4) / **medium** (slices 2 and 3).

Baseline: Syzygy `a9f671e` (main). The subject is the daemon the POC runs
in — its request outcomes, its startup failures, its lifecycle and the
ceiling that makes it serve nothing — not the Polaris page's content.

**Line-number convention, stated once.** Every line number is 1-based over
the file's bytes at `a9f671e` unless another commit or worktree is named;
`sed -n 'Np' <file>` selects line N. The dossier's spans were taken at
`f4589e2` and every one is re-located below.

**Line-count convention, stated once** (added 2026-09-15 per review 1, F9).
Every published line count in this packet is the `wc -l` figure — physical
newline-terminated lines — never the split-on-newline count, which is one
higher on every newline-terminated file cited here. Three counts published in
the first draft used the other convention and are corrected in place below.

## The five questions for the owner

Batched, each with the recommended answer first. Everything below is the
evidence behind them. Q3 is the packet's central question; Q4 is downstream
of it and is the only registry question. Q1 and Q5 are disclosure questions
and gate only the surfaces, not the logging.

| # | Question | Recommended |
|---|---|---|
| Q1 | **What credential class may a status disclosure carry?** Today the daemon dispatches **17** routes: **13** `human-open` and **4** `machine-credentialed`, and **0** whose path matches the literal alternation `status|health|live|ready` under a case-insensitive test [Observed, computed this session by importing the built `pocRoutes` and `materializeRoutes` and enumerating the returned array — the full table is in Measurements]. In this daemon `human-open` is not unauthenticated: it passes `browserRequestAllowed` (`apps/three-surface-poc/src/browser-origin.ts` lines 26–38), which requires a loopback or tailnet `Host` and an `Origin` that is absent or matches. An absent `Origin` is admitted and a non-browser agent sends none, so a `human-open` status route admits an agent on host alone. SEC-1 reads, verbatim at `.syzygy/governance/doctrine/security.md` lines 14–16: "**non-browser agent and CLI clients are admitted only through an explicit machine-client authentication mechanism**"; its violation list, lines 21–23, names "a machine client admitted on loopback location alone". A status body discloses the observer commit, the Butlers commit, the state-directory provision kind and the last breach — project metadata, not project content. | **Serve the machine form `machine-credentialed`, like the four machine routes it would sit beside; serve the human form on the existing `human-open` pages, which already disclose the evaluation identity in their footer.** This is the same answer M10 reached for its schema document and for the same clause (the M10 packet, docs/design/POLARIS-M10-MACHINE-CONTRACT-FUNNEL.md line 37, its Q3 row, read read-only in the M10 worktree and not present in this one). **The counter-argument is real:** a status route an operator must hold a credential to read is useless at the moment it is most needed — when the daemon is misbehaving and the operator is looking for a reason — and a status body names commits and a credential *provision kind*, never a credential value, so SEC-2's egress rule is not engaged. **Second lawful arm:** serve it `human-open` and record the SEC-1 reading that makes that lawful, namely that the origin check is the explicit mechanism for a body carrying no observed content. This packet does not rule which reading SEC-1 bears [Inferred]. **And the prior question is not this packet's:** whether a *third* machine-credentialed route may be minted at all is M5's Q1. That limb stood in this question's heading until 2026-09-15 and was moved here per review 1, F13 [superseded heading wording: "What credential class may a status disclosure carry, and may a third machine-credentialed route be minted at all?" — the heading invited the owner to answer M5's question inside a P-number that does not own it]. It is proposed as **P-72** in the M5 packet on PR #39 and is **not yet on the register at `a9f671e`** [Observed, re-derived this session: `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` at `a9f671e` carries **26** rows under the predicate `^| P-` (21 open plus 5 acceptance-act), its highest allocated number anywhere in the file is **P-67**, and the predicate `P-7[0-9]` returns **0** hits over it; superseded wording: "already on the register as **P-72**"]. The question rests on the three-surface specification's reader note — "the 'machine answer' is the authenticated `GET /api/poc` response" (`openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md` line 26, singular and definite) [Observed, read at source this session]. Slice 2's machine form holds behind P-72 exactly as M10's slice 3 does; this packet adds no sixth question for it and rules it neither way. **Default if unanswered: slice 2's machine route does not ship**; slice 2's human disclosure is ruled by Q5. |
| Q2 | **Does the act-bound registry's `breachResult` sentence forbid a stderr line naming a response-ceiling breach?** The registry entry declares, verbatim at `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` line 281: `"breachResult": "source and input breaches retain the complete population and make dependent facts Unknown; final-output breaches emit only a bounded typed failure carrying evaluation identity, limit identity, declared value, observed value and population counts; no truncated or success-shaped model is emitted; PWB-REQ-021 readiness is false"`. Those bytes are bound: the file's current sha256 equals the digest recorded in `.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md` [Observed, `sha256sum` compared this session; neither value is reproduced here, per CG-15 — the record is cited by path]. The word is **emit only**. The signed specification's own sentence is narrower — "SHALL return only a bounded typed failure envelope" (`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md` lines 381–382) — and *return* plainly governs the HTTP response. | **No: a stderr line is not an emission to the requester, and slice 1 may log the breach.** Two readings of the registry sentence exist and the specification settles the one that matters: PWB-REQ-006's own scenario "Resource breach is bounded and explicit" says "**THEN** the evaluation names the exact limit and counts the affected population as Unknown without emitting a partial success-shaped answer" (spec lines 419–424) — the prohibition is on *success-shaped* output, not on a diagnostic. **The counter-argument, and it is why this is a question:** the registry is act-bound and says "emit only", a phrase with no *to the requester* qualifier, and the same specification treats logs as a governed sink twice over — line 407, "**THEN** no active content reaches Polaris, JSON, **logs**, caches or records", and line 665, "**AND** it stores, **logs**, caches and returns no unselected body bytes" [Observed, the only three occurrences of the word `log` or `logs` — predicate `\blogs?\b`, case-insensitive, Python `re` — in that **1,152**-line file are at 176, 407 and 665, and all three are sink constraints. Corrected 2026-09-15 per review 1, F3 and F9; superseded wording: "the only three occurrences of the string `log` in that 1,153-line file". As a case-insensitive **substring**, `log` occurs on **43** of that file's lines — `catalog`, `topology`, `technology`-shaped tokens — so the substring reading of the claim is false, and 1,153 was the split-on-newline count. The three are owned by three different requirements: 176 is PWB-REQ-003's Oracle, 407 is PWB-REQ-006's scenario and 665 is PWB-REQ-011's scenario, per review 1, F6]. An owner who reads "emit" as covering every sink may want the breach line to carry less than the 503 body does. **Second lawful arm:** log the breach with its status, method and limit identity only, omitting the population counts and the evaluation identity that the 503 body already carries. **Default if unanswered: the second arm** — the line lands without the population counts, which is the smaller claim and loses no operability. |
| Q3 | **Is making a final-output breach reach PWB-REQ-021 readiness an implementation of PWB-REQ-006, or an amendment to it?** Two sentences of the signed specification already require it. PWB-REQ-006, line 384: "Every breach SHALL make PWB-REQ-021 readiness false." PWB-REQ-021, lines 964–968: "Readiness SHALL be false for a missing, empty, duplicate or unrecognized answer identity; an unresolved source anchor; a surface/evaluation mismatch; any path outside Polaris or its same-evaluation exact-source route; **any PWB-REQ-006 resource breach**; or an answer whose cited current Butlers authority cannot be resolved." And PWB-REQ-006 line 378 puts the response ceilings inside that population: "Final encoded human HTML and machine JSON SHALL each have an explicit byte ceiling." Today the readiness evaluator's breach arm reads one number — `population.limitBreaches` (`packages/three-surface-poc-core/src/walkthrough-readiness.ts` lines 365–366) — sourced from the observation's phase-A/phase-B input ledger snapshot (`packages/three-surface-poc-core/src/model.ts` lines 217–219). A response-ceiling breach never enters that number: `boundedResponse` (`apps/three-surface-poc/src/routes.ts` lines 137–142) constructs a `ResponseLimitFailure` and returns it, and the string `recordBreach` occurs **0** times in `routes.ts` over its 240 lines [Observed, swept this session; all 7 non-ledger `recordBreach` call sites are input-side, in `git-object-reader.ts` and `project-shape-observation.ts`]. | **It is an implementation of two quoted sentences, not an amendment; no CC-REV-2 delta is needed for the readiness consequence itself.** The specification names the consequence, names the population and names the ceilings as members of it; wiring the evaluator to see a member it already declares is conforming code to bound text. **The counter-argument, which this packet does not resolve:** PWB-REQ-006's own oracle line separates the two — "a separately accumulated resource ledger **and** exact final encoded-byte counts decide" (line 395) — so the specification's picture may be two independent oracles rather than one ledger, and an owner may read "every breach" as every breach *the evaluation-wide ledger holds*, which is an input-side object by construction. **Second lawful arm:** rule it an amendment and route the readiness widening through CC-REV-2 (`.syzygy/governance/policies/craft-and-care/review-and-documentation.md` line 52) with a new owner act — slower, and it re-opens bytes an act bound. **Default if unanswered: slice 3 does not ship**; slices 1, 2 and 4 are unaffected. |
| Q4 | **Must a new registry limit be minted for the output side — and does minting one cross an escalation trigger?** The dossier's S7-M3 slice plan opens "Add `maxOutputBytes` to the registry's `resourceLimits` schema and `PwbResourceLimits` type". **That step is unnecessary and this packet does not recommend it.** `PwbResourceLimits` already carries both output-side ceilings — `maxHumanResponseBytes` and `maxMachineResponseBytes` (`packages/three-surface-poc-core/src/project-shape-observation.ts` lines 71–72), declared in the registry at lines 270–271 and given their semantics at lines 279–280 — and `ResourceLimitBreach.limit` is typed `keyof PwbResourceLimits` (line 205), so a breach record naming `maxHumanResponseBytes` is **already expressible with no type, schema or registry change at all** [Observed, all four read at source this session]. | **Do not mint a new limit: record the breach against the ceiling the registry already declares.** Then slice 3 needs no registry edit, and Q4's second half does not arise. **If the owner prefers a distinct limit anyway**, that arm crosses a named escalation trigger. The continuation act reads, verbatim at `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` lines 150–156 [span corrected 2026-09-15 per review 1, F7; superseded citation: "lines 152–155". The quoted sentence begins on line 150 at "Stop" and ends on line 156 at "the signed change."; the packet's two narrower cites into the same paragraph, line 151 for the specification-amendment trigger and lines 154–155 for the registry-envelope trigger, are both exact and unchanged]: "Stop and return to the owner before proceeding if implementation would need any of: a change to doctrine or an accepted contract; a further amendment to the signed PWB specification beyond the 2026-09-05 package; a change to security, privacy, or retention posture beyond the 2026-09-05 approved secret-classification policy; **a change to the constraints or envelope the 2026-09-05 registry entry declares**; any observation outside the consented content class or repository; or any scope beyond the signed change." A new `resourceLimits` key is a change to the envelope that entry declares, so that arm needs a new owner act and a CC-REV-2 delta over the registry and the specification together; the registry bytes are digest-bound and **may not be edited under this packet on either arm**. **Counter-argument for minting one:** a served-response budget and an input-read budget measure different things, and overloading the two existing ceilings makes a single `ResourceLimitBreach` ambiguous about which side of the pipeline it came from unless a discriminator is added. **Default if unanswered: the recommended arm** — no new limit; slice 3, if Q3 allows it, uses the declared ceilings. |
| Q5 | **May the human status disclosure ride `pageShell`, appearing once on every human page, or must it live only on its own route?** `pageShell` (`apps/three-surface-poc/src/page-shell.ts` lines 44–74) renders **one** footer slot, filled by **5** call sites that each build their own string inline: `apps/three-surface-poc/src/routes.ts` line 92, `apps/three-surface-poc/src/polaris.ts` line 1630, `apps/three-surface-poc/src/polaris-source.ts` line 140, `apps/three-surface-poc/src/trajectory.ts` lines 197–200 and `apps/three-surface-poc/src/orrery.ts` lines 162–165. **There is no function that computes the footer's facts** [Observed, swept this session; the denominator is the 45 non-test `.ts` files under the app's `src`, over which `^\s*footer:` matches exactly those 5 lines]. Three of the five are the same two evaluation fields; two are surface-specific one-liners. Adding a status line to `pageShell` therefore costs its bytes **on every human response**, including the one under the ceiling. After M1 lane A the tailnet `/polaris` headroom is **612,665** bytes and the direct headroom **618,515** (ceiling 2,097,152 against 1,484,487 and 1,478,637 served bytes at Butlers `2e3bac97`) [Observed, from `docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`, whose `result.tailnetHeadroom.after` is that figure; the direct headroom is the subtraction, computed this session]. | **Put it in `pageShell`, above the fold, and keep it under 400 bytes.** VIS-1 ranks comprehension of the truth's presentation second only to truth itself, and a status an operator must navigate to is a status they will not read; the cost is under 0.07% of the current headroom. **The counter-argument, and it is M1's:** the headroom is not free — it is the whole subject of P-67 and P-68, lane A spent a 654,019-byte trim to buy it, and the restated Q3 target of 1.4 MB is **not yet met** on either host form (short by 78,637 direct and 84,487 tailnet, per the same record). A packet that charges that budget for a convenience is spending another move's savings. **Second lawful arm:** the status line renders only on the home page and its own route, and the other four pages keep today's footer — zero cost on `/polaris`, one more place the operator must go. **Default if unanswered: the second arm.** |

### Decided in this packet, not put to the owner

**The dossier's prerequisite line does not survive as written.** The dossier
gives M11 a `prerequisite` value of "none; owner act for the registry
resourceLimits change". The first half holds for slices 1, 2 and 4. The
second half rests on a premise this packet falsified: there is no
`resourceLimits` change to make, because both output-side ceilings are
already declared in the registry
and already typed into `PwbResourceLimits`, and `ResourceLimitBreach.limit`
already admits them (Q4, measured above). An owner act is needed only on the
arm that mints a *new* limit key, which this packet does not recommend and
which S7-M3 assumed without checking the type it proposed to extend
[Observed for the four source facts; Inferred for the consequence that the
prerequisite therefore does not bind the recommended arm].

**P0-CEILING is superseded on main and this packet does not re-report it.**
The dossier's P0-CEILING records `/polaris` serving nothing at Butlers
`7c8743f63`, and the retained 503 body is at the session capture path
`scratchpad/capture/polaris.html` (838 bytes; its `observed` field is
2,132,656 against a `declared` of 2,097,152). The M1 lane A trim landed on
main at `2ef68f5` and the page now fits with the headroom quoted in Q5
[Observed]. What does **not** change is the finding M11 exists for: the
breach left no trace anywhere but that 838-byte body, and nothing in the
code prevents the next one.

**No pidfile, and this is not a preference.** S10-M3's slice plan offers
"Optionally add a pidfile written at startup under stateDir…" — the
elision is the sentence's second half, "and a tiny restart script that reads
it", and the source writes stateDir without a code span [quotation marked
2026-09-15 per review 1, F8; superseded rendering: "optionally add a pidfile
written at startup under `stateDir`", which stopped mid-sentence with no
ellipsis]. An existing
system test asserts the state directory's contents *exactly*:
`packages/cap1-system/src/state-dir.system.test.ts` line 294 reads
`expect(readdirSync(benignTarget)).toEqual(['machine-credential.token'])`
[Observed, read at source this session]. A pidfile would fail it. The daemon
module states the same invariant in prose — "Startup writes: exactly the
credential/state files inside the explicit state directory (via
`ensureCredential`, whose writes are routed through the state-write
boundary). Nothing else is written." (`packages/cap1-daemon/src/server.ts`
lines 28–30). Slice 4's script therefore resolves the running daemon from
its port, never from a file it wrote.

**No derived "age", and no green.** The dossier's S10-M1 asks the status
route to answer "how old". VIS-2 reads, at
`.syzygy/governance/doctrine/vision.md` lines 101–103: "Currency is judged at
a status evaluation's identified as-of instant (architecture.md) — the wall
clock never silently
changes a displayed status." A rendered age is a wall-clock function that
changes on every request; two identified instants (the evaluation's `asOf`
and the request's own) are not. The status surface renders both and derives
nothing. It also renders no word meaning *healthy*: the single occurrence of
`health` across both signed specifications is a **falsifier** —
`three-surface-poc-experience` spec line 596, "**Falsifier**: prose asserting
verification, health, or completion for a relationship the model holds as
Unknown" [Observed; 1 occurrence in the POC specification's **1,008**
lines, 0 in the PWB specification's **1,152**, both `wc -l` under the
line-count convention stated at the head of this packet. Corrected 2026-09-15
per review 1, F9; superseded figures: "1,009 lines" and "1,153 lines", the
split-on-newline counts of the same two newline-terminated files].

**The improvement-cycle tracing question is M10's, not a sixth question
here.** The authorizing direction reads, verbatim at
`.syzygy/governance/decisions/THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md`
lines 55–56: "Improvement-cycle work must trace to POC-REQ-001..061 or to a
recorded review finding." Whether a *vision-pursuit dossier* is a recorded
review finding within that limb is M10's Q4, proposed as **P-77** in the
M10 packet on PR #44 and **not yet on the register at `a9f671e`** [Observed,
the same count as Q1's: 26 rows under `^| P-`, highest allocated number P-67,
0 hits for the predicate `P-7[0-9]`. Corrected 2026-09-15 per review 1, F5;
superseded wording: "already on the register as M10's Q4 under **P-77**"]
(the M10 packet, docs/design/POLARIS-M10-MACHINE-CONTRACT-FUNNEL.md
line 38, in the M10 worktree).
M11's answer follows whatever the owner rules there; asking it again would
duplicate a register row.

## Gate 0 — Baseline

| Pillar | Present | Constrains this request |
|---|---|---|
| Doctrine | `.syzygy/governance/doctrine/vision.md`, `.syzygy/governance/doctrine/security.md` | VIS-1, VIS-2, VIS-4, VIS-5; SEC-1, SEC-5 (SEC-2, SEC-3 and SEC-4 are not engaged — Gate 2 says why, with the sweep) |
| Decisions | `.syzygy/governance/decisions/THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md`, `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`, `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`, `.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md` | the first two authorize; the third continues and names the registry-envelope escalation trigger; the fourth binds the registry bytes Q2 and Q4 quote |
| Specification | `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md` (17 requirements, 31 scenarios) and `openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md` (24 requirements, 24 scenarios) | PWB-REQ-006 and PWB-REQ-021 are the load-bearing pair; POC-REQ-032's falsifier and POC-REQ-060/061 bound the human surface |
| Registry | `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` | digest-bound; declares both response ceilings and the `breachResult` semantics; **no slice edits it** |
| Contracts | `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md` (RFC2-26), `.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md` (RFC5-3) | RFC2-26's phase rule is run over all four slices in Gate 5; RFC5-3 fixes the two client classes a status route must fall into |
| Policies | `.syzygy/governance/policies/craft-and-care/review-and-documentation.md` (CC-REV-2) | the amendment path Q3's second arm and Q4's minting arm would need |

**Which statuses these acts are in.** `PROJECT-STATUS.md` is the page that
says which acts are in force and this packet does not restate its rows; the
four decision records above were each read at source this session and each
is a dated owner act or direction with no supersession notice naming it
[Observed]. The registry JSON's own head says
`"status": "candidate-amendment-no-effect-until-owner-act"` (line 4), which
is a **pre-act banner over bytes an act bound** on 2026-09-05 — the same
shape AGENTS.md records for both adopted specifications. Read the act
record, never the package banner.

**One name that is not what it looks like.**
`.syzygy/governance/decisions/POLARIS-POST-CEILING-CORRECTION-AUTHORIZATION.md`
concerns the six-pass *reconciliation review* ceiling of 2026-08-31 and
authorizes exactly one edit to a design document's data-flow item (its lines
19–22). It has nothing to do with the response-byte ceiling this move is
about, and no slice rides it [Observed, the whole 30-line file read this
session].

## Gate 1 — Motif

**A daemon that cannot say it failed renders a false green to the one reader
who could fix it.** VIS-2's whole subject is a surface that shows success
where there is no evidence. Applied inward, to the process itself, the POC
has three such surfaces and all three are silent.

**The specific shape, in four measurements.** (1) A response-ceiling breach
serves nothing and **leaves no trace but the body of the request that
breached**: across both the app's and the core's source trees and the
daemon package's, **0** of the **81** non-test TypeScript files contains a
call to `process.stderr`, `process.stdout`, `console.` or any logger inside
a request-handling path; every one of the **37** such call sites in the app
lives in a `*-main.ts` command-line entry point, and the core and daemon
packages have **0** between them. (2) The retained capture proves it end to
end: `run.sh` issued **7** requests, **2** of which were the two `/polaris`
forms and both answered 503; the captured `daemon.err` is **0 bytes** and
the captured `daemon.log` is the startup banner alone [Observed, both files
read this session at the session capture path]. (3) The daemon's own
readiness answer is unmoved by that breach: PWB-REQ-006 says "Every breach
SHALL make PWB-REQ-021 readiness false" (spec line 384) and PWB-REQ-021
lists "any PWB-REQ-006 resource breach" among its false arms (spec line
967), but the arm that implements it reads a count of *input-side* breaches
only, and `routes.ts` records none — so a `/polaris` breach at instant T
leaves `/api/poc`'s readiness answer at instant T+1 exactly as it was. (4)
There is **no route** by which an operator could ask: 17 routes, 0 of them
status, health, liveness or readiness.

**And the startup failure that stops the daemon prints a single word.**
`DaemonStart`'s three failure arms each carry a `.detail`
(`packages/cap1-daemon/src/server.ts` lines 112–114), the `bind-failed` one
carrying Node's own listen-error message (line 231); `main.ts` line 207
interpolates `start.failure.kind` and nothing else. An operator who starts a
second daemon on an occupied port is told `bind-failed` and not which port.

**Success criteria, per slice.** Slice 1: every non-2xx outcome the daemon
produces is one structured stderr line, and a failed start names its cause.
Slice 2: one route and one page line answer "what am I serving, from which
commits, and did the last render fit", from the same values the footer
already prints. Slice 3: a final-output breach is a recorded breach, so the
readiness arm the specification already declares can see it. Slice 4: an
operator who needs a new Butlers commit or a new observer build has a
written answer and a script, and knows the credential survives.

**What M11 is not.** It is not a change to what Polaris says about Butlers,
not a new observation, not a provider call, not a second repository, and not
a deployment story. Every slice writes into `apps/**`, `packages/**`,
`docs/**` or `scripts/`.

## Measurements at `a9f671e`

Every figure below was taken this session in the worktree at `a9f671e`.
Method, predicate, denominator and raw output for each are in the evidence
record beside this packet.

### The complete route table, computed not transcribed

Method: `npm run build:poc`, then import `pocRoutes` and `materializeRoutes`
from the built JavaScript and enumerate the returned arrays against a stub
model. Denominator: every route the app registers.

| # | Method and path | Credential class |
|---:|---|---|
| 1 | `GET /` | human-open |
| 2 | `GET /butlers-syzygy` | human-open |
| 3 | `GET /butlers-syzygy/` | human-open |
| 4 | `GET /polaris` | human-open |
| 5 | `GET /butlers-syzygy/polaris` | human-open |
| 6 | `GET /polaris/source` | human-open |
| 7 | `GET /butlers-syzygy/polaris/source` | human-open |
| 8 | `GET /trajectory` | human-open |
| 9 | `GET /butlers-syzygy/trajectory` | human-open |
| 10 | `GET /orrery` | human-open |
| 11 | `GET /butlers-syzygy/orrery` | human-open |
| 12 | `GET /api/poc` | machine-credentialed |
| 13 | `GET /butlers-syzygy/api/poc` | machine-credentialed |
| 14 | `GET /api/poc/polaris` | machine-credentialed |
| 15 | `GET /butlers-syzygy/api/poc/polaris` | machine-credentialed |
| 16 | `POST /trajectory/materialize` | human-open |
| 17 | `POST /butlers-syzygy/trajectory/materialize` | human-open |

**17 routes: 13 human-open, 4 machine-credentialed, 0 matching
`status|health|live|ready` case-insensitively** [Observed, computed].
`minimalRootRoute` exists in the daemon package (`server.ts` lines 269–282)
and is registered by nothing: the literal `minimalRootRoute` occurs in that
file and in its tests and in no route list [Observed]. **Two figures differ
from the dossier here.** S10-F1's sentence — "the only routes are the
five human surfaces, `/api/poc`, `/api/poc/polaris` and their tailnet
mirrors" — lives in `docs/pursuits/2026-09-13-vision-pursuit-harvest.json`
at the jq path `.agents["S10-operability"].findings[0].summary`, and verbatim
in `docs/pursuits/2026-09-13-vision-pursuit-data.json` at
`.agents[9].findings[0].summary`. It is **not** in
`docs/pursuits/2026-09-13-vision-pursuit.md`, which is the file Gate 0 names
as the dossier [Observed, `grep -F` of the sentence over all three this
session: 1 hit, 1 hit, 0 hits. Citation added 2026-09-15 per review 1, F11].
**Two readings, and this packet publishes both.** Read literally the sentence
enumerates 7 paths plus their 7 tailnet mirrors = **14**, against which the
computed table of 17 undercounts by **three**: the two `POST` materialize
routes and the `/butlers-syzygy/` trailing-slash mirror of `/`. Read as
describing `pocRoutes`' **15** `GET` routes — the reading the figure below
uses — it undercounts by **two**, the two `POST` materialize routes
[Observed both ways this session; superseded wording: "omits the two `POST`
materialize routes and undercounts the table by two", which stated the second
reading without naming it as a reading]. It also cites the complete route
list at `routes.ts` lines 206–239, which is still exactly the `return`
array at `a9f671e` [Observed, re-located]. The
finding's **conclusion** — no status route exists anywhere — holds under a
sweep with a stated denominator.

### `boundedResponse`, re-located and quoted

The dossier cites `apps/three-surface-poc/src/routes.ts` lines 99–151 at
`f4589e2`. At `a9f671e` that span is the whole final-output-ceiling block:
the explanatory comment runs 98–106, the two constants are 108–109, the
`ResponseLimitFailure` interface is 113–124, `responseLimitFailure` is
132–134, and `boundedResponse` itself is **137–142**, its one-line comment
at 136. The breach branch, quoted verbatim at line 141:

```ts
  return { status: RESPONSE_LIMIT_STATUS, contentType: 'application/json', body: JSON.stringify(responseLimitFailure(model, limit, declared, observed)) };
```

The served body is the whole trace. The retained 503 at the session capture
path is 838 bytes and its fields are `served`, `failure`, `evaluation`
(itself `snapshot`, `snapshotLabel`, `inputsDigest`, `asOf`), `limit`,
`declared`, `observed`, `population` and `readiness` [Observed, parsed this
session]. Note `readiness: false` — a literal of the type (line 123), true
of *that response* and of nothing else in the evaluation.

**The absence claim, with its predicate and denominator.** Predicate: a
source line in a non-test `.ts` file under `apps/three-surface-poc/src`,
`packages/three-surface-poc-core/src` or `packages/cap1-daemon/src` that
mentions the breach to any sink other than the HTTP response — that is, any
of `process.stderr`, `process.stdout`, `console.`, `logger`, `log(`, or the
ledger's `recordBreach`. Denominator: **81** non-test `.ts` files (45, 27
and 9 respectively) out of 157 `.ts` files in the three trees. Result: the
breach reaches **no** ledger, **no** stderr or stdout, and **no** status
record. Corroborated two ways, per verification rule 2: (a) `recordBreach`
has **12** non-test occurrences, all in `resource-ledger.ts` (5, its own
declaration and closure) and in the two input-side readers
(`git-object-reader.ts` lines 307, 328, 351; `project-shape-observation.ts`
lines 412, 427, 545, 548) — **0** in `routes.ts`; (b) `routes.ts` does not
import `ResourceLedger` at all, so no ledger is in scope there (its import
list is lines 1–11).

### The resource ledger, quoted field by field

`packages/three-surface-poc-core/src/resource-ledger.ts` is 207 lines. The
dossier cites lines 81–121 and that span is exact at `a9f671e`: it is
`ResourceLedgerSummary` (81–90) followed by `ResourceLedger` (92–121).

`ResourceLedgerSummary`'s complete field list, lines 82–89:
`bodiesCounted`, `totalBytes`, `parsePasses`, `passesByIdentity`,
`sourcesTraversed`, `maxPassesOnOneSource`, `breaches` — **7 fields, 0 of
them output-side**. `ResourceLedger`'s complete member list, lines 93–120:
`limits`, `breaches`, `recordBreach`, `projectBody`, `chargeBody`,
`counted`, `totalBytes`, `chargePass`, `passesFor`, `chargeFor`, `remember`,
`recall`, `release`, `summary` — **14 members, 0 of them output-side**
[Observed, both counted this session from the source; S7-F3's claim is
confirmed at these exact lines].

`PwbResourceLimits`, in
`packages/three-surface-poc-core/src/project-shape-observation.ts` at lines
65–73, has **7** fields and **two of them are output-side**:

```ts
export interface PwbResourceLimits {
  readonly maxSources: number;
  readonly maxBytesPerSource: number;
  readonly maxTotalBytes: number;
  readonly maxIndexDepth: number;
  readonly maxParsePassesPerSource: number;
  readonly maxHumanResponseBytes: number;
  readonly maxMachineResponseBytes: number;
}
```

This is the measurement that changes M11's shape. S7-F3 says the *ledger* is
structurally input-side only, and that is true. S7-M3 then proposes adding
`maxOutputBytes` to "the registry's `resourceLimits` schema and
`PwbResourceLimits` type" — but the type already holds both ceilings, the
registry already declares them (lines 270–271, with semantics at 279–280),
and `ResourceLimitBreach` is declared

```ts
export interface ResourceLimitBreach {
  readonly limit: keyof PwbResourceLimits;
  readonly declared: number;
  readonly observed: number;
  // The source the breach left counted-and-Unknown, when it is one source.
  readonly path?: string;
}
```

at lines 204–210 — so `{ limit: 'maxHumanResponseBytes', declared, observed }`
is already a well-typed breach record that nothing constructs [Observed, all
three read at source]. **The gap is a recording site, not a schema.** The
literal `maxOutputBytes` occurs **31** times in **12** of the **1,216**
files tracked at `a9f671e` — swept this session with Python `re` over every
blob named by `git ls-tree -r -z --name-only a9f671e`. Its principal home is
an adopted generator interface, not a demo: **11** occurrences in
`packages/polaris-generation-core/src/pipeline.ts`, **2** in
`packages/polaris-generation-core/src/pipeline.test.ts` and **1** in
`openspec/changes/polaris-manifesto-generation/INTERFACES.md`. Inside the
three POC source trees it occurs **twice**, both at
`apps/three-surface-poc/src/polaris-generation/pipeline-demo.ts` lines 64 and
71 — an unrelated provider-call budget in the generator demo. **The
collision warning to the implementing bead is therefore stronger, not
weaker:** a slice that minted `maxOutputBytes` would take a name an adopted
generator interface and its OpenSpec `INTERFACES.md` already hold [Observed.
Corrected 2026-09-15 per review 1, F4; superseded wording: "does occur twice
in the repository", which carried neither predicate nor denominator. One
correction to the finding itself: review 1 publishes **38** occurrences in
**14** files against a stated denominator of 1,216 at `a9f671e`, but that
figure is over the **1,218** files tracked at `2c62d0b`, which include this
packet and its own evidence record — 7 of the 38 occurrences, in those 2
files. Both sweeps were run this session].

### Where a served-side breach cannot go

The evaluation ledger cannot hold it, and the reason is determinism rather
than taste. `project-shape-observation.ts` line 630 snapshots
`limitBreaches: [...ledger.breaches]` into the observation body; line 635
computes `observationDigest` over that body; line 636 `deepFreeze`s the
result. `project-shape-model.ts` line 640 takes the second, phase-B-inclusive
snapshot the model carries. A breach recorded after the response is
serialized would therefore either mutate a frozen object — it cannot — or
be invisible to the digest that is supposed to mean "same exact inputs, same
digest" (the comment at lines 288–289). Slice 3's design below takes the
consequence seriously: the served-side breach is a **separate, per-process
record**, not a late write into the evaluation's ledger.

### Every stderr and stdout site, and exactly which drop detail

Predicate: a `process.stderr.write` or `process.stdout.write` call in
`apps/three-surface-poc/src/main.ts`. Denominator: the whole 253-line file.
Count: **10** — **7** stderr, at 58, 65, 89, 207, 239, 241 and 249, and
**3** stdout, at 56, 211 and 229, which is exactly the split the table below
lists [corrected 2026-09-15 per review 1, F1; superseded figures: "6 stderr,
4 stdout", which contradicted the packet's own table].

| Line | Sink | What it prints | Detail available and dropped? |
|---:|---|---|---|
| 56 | stdout | the usage text | n/a |
| 58 | stderr | `syzygy POC: ${parsed.detail}` plus usage | **No** — this is the CLI parse union, and its `detail` *is* printed |
| 65 | stderr | `configured repository is not readable` | **Yes** — the caught `realpathSync` error is discarded whole |
| 89–93 | stderr | one of two fixed sentences | **Yes** — `cause.message` is compared against `'observer-checkout-dirty'` and otherwise never printed, so the git error text is lost |
| 207 | stderr | `daemon did not start (${start.failure.kind})` | **Yes** — all three `DaemonStart` arms carry `.detail` |
| 211 | stdout | the startup banner | n/a |
| 229 | stdout | the shutdown line | n/a |
| 239 | stderr | `observation failed (${cause.kind})` plus `artifactPath` | **No** — `PocObservationError`'s message is exactly `kind: artifactPath` (`packages/three-surface-poc-core/src/model.ts` lines 222–232) |
| 241 | stderr | `observation failed (unexpected-failure)` | **Yes** — `cause` is discarded entirely, stack included |
| 249 | stderr | `configured repository authority rejected (${launch.reason})` | **No** — the rejected arm carries only `reason` (`apps/three-surface-poc/src/launcher.ts` line 4) |

**The dossier's S10-F3 is correct and narrower than the class.** It names
line 207 and the three `DaemonStart` arms, and that is exactly right at
`a9f671e`. What it does not say is that **four** of the **seven** stderr
sites drop an available cause, not one: 65, the 89–93 pair, 207 and 241.
Line 58 — which writes a `.detail` — belongs to `parsePocCli`'s union and
is neither evidence for nor against the finding [Observed, every site read at
source; superseded wording: "four of the six stderr sites", corrected
2026-09-15 per review 1, F1 — that class's denominator is seven].

### Every logging site in the three source trees

Predicate: a line matching `process.stderr`, `process.stdout`, `console.`,
`logger` or `log(` in a non-test `.ts` file. Denominators: 86 `.ts` files (45
non-test) under `apps/three-surface-poc/src`; 53 (27) under
`packages/three-surface-poc-core/src`; 18 (9) under
`packages/cap1-daemon/src`.

| Tree | Non-test files | Hits | Files with a hit | All in a `*-main.ts` entry point? |
|---|---:|---:|---:|---|
| `apps/three-surface-poc/src` | 45 | 37 | 7 | yes — `main.ts`, `capture-test-artifact-main.ts`, `fresh-checkout-demo-main.ts`, `polaris-accessibility-main.ts`, `pwb-mutation-run-main.ts`, `pwb-mutation-sweep-main.ts` and `polaris-generation/pipeline-demo-main.ts` |
| `packages/three-surface-poc-core/src` | 27 | **0** | 0 | n/a |
| `packages/cap1-daemon/src` | 9 | **0** | 0 | n/a |

So `handleRequest` (`packages/cap1-daemon/src/server.ts` lines 169–224) has
**0** logging calls on any of its four outcome branches: unknown route (178),
refused credential (196), handler success (214) and handler throw (218). The
dossier's S10-F2 cites lines 165–224 for that and the span holds at
`a9f671e`; the precise handler body is 169–224 [Observed, re-located].

### The footer facts, and the function that does not exist

The dossier's S10-M1 asks the status route to reuse "the same footer facts".
There is no such function. `pageShell` takes a `footer` string
(`apps/three-surface-poc/src/page-shell.ts` line 36) and renders it at line
70; the string is built inline at **5** call sites, listed in Q5 above, three
of which are near-identical restatements of `model.evaluation.snapshot` and
`model.evaluation.asOf`. The evaluation identity itself is composed once, in
`apps/three-surface-poc/src/main.ts` lines 101–105, as
`butlers:<revision>|working-tree:<digest>|observer:<revision>`; `asOf` is
`new Date().toISOString()` at line 134, recomputed on every model build. The
observer revision an operator would want is therefore *already* inside the
snapshot string but is never labelled as such on any surface [Observed, the
five call sites and the two composition sites read at source]. Slice 2's
first act is to give those facts one home.

### Lifecycle: what exists, and an absence with a denominator

**Two predicates, both published**, because they give different figures
and the first draft published one of them and ran the other [corrected
2026-09-15 per review 1, F2; superseded wording: the first draft published
the substring predicate below with the figure **22**, which that predicate
does not produce, and partitioned it 11 + 3 + 4 + 4 = 22 with four review
records where the substring predicate finds five].

**Predicate A — substring.** A line matching the alternation
`restart|systemd|upgrade|pidfile|pid file|service unit|\.service` as a
case-insensitive substring, Python `re`, in a tracked file under `docs/`,
`scripts/`, `apps/`, `packages/`, or `README.md`. Denominator: **558** such
files out of **1,216** tracked at `a9f671e`. Result: **29** files carry a
hit, partitioned 11 evidence or pursuit JSON + 3 pursuit or plan prose + **5**
review records + 8 source or test files +
`packages/polaris-generation-core/README.md` +
`scripts/launch_gate_results.py` = 29.

**Predicate B — word-bounded.** The same denominator, with the alternation
`\brestart\b|\bsystemd\b|\bupgrade\b|\bpidfile\b`, case-insensitive,
Python `re`. Result: **22** files. This is the predicate that produced the
first draft's figure, and the seven files it silently drops are plural and
past forms: `apps/three-surface-poc/src/polaris.ts` (line 367),
`apps/three-surface-poc/src/polaris-first-reading.test.ts` (229),
`docs/reviews/R-POC-CYCLE-3-REVIEW.md` (347),
`packages/cap1-daemon/src/server.test.ts` (159–160),
`packages/polaris-generation-core/README.md` (41),
`packages/three-surface-poc-core/src/test-artifact-verification.ts` (228) and
`scripts/launch_gate_results.py` (80).

**The conclusion is unchanged and now carries the wider denominator: 0 of
the 29 files is an operator lifecycle instruction** [Observed — all 29 read
this session, the 22 of predicate B for the first draft and the seven
predicate A adds for this pass; none of the seven is an instruction either].
The two source comments are unchanged:
`packages/cap1-daemon/src/credentials.ts` line 175, "Restart: reads and
reuses the [credential]", and
`packages/three-surface-poc-core/src/walkthrough-readiness.ts` line 113, the
identity being "the same after a daemon restart", each with its own test
file. **One of the seven is substantive to slice 4**:
`packages/cap1-daemon/src/server.test.ts` line 159 opens a describe block
named "RT3 — credential stability across daemon restarts" and line 160 is
its test, "a restarted daemon reuses the same credential file and token".
That is the closest existing prior art to slice 4's own oracle, and the first
draft did not cite it because predicate B hid the file. It is cited in slice
4 below. `docs/THREE-SURFACE-POC.md`
carries **0** hits over its 89 lines; its entire lifecycle content is one
foreground `npm ci && npm run poc` command in a fenced block, and its four
second-level headings are "Start from a fresh Syzygy checkout", "First-slice
walkthrough", "Capturing test-run evidence" and "Deliberately absent in this
slice"
[Observed; S10-F6 confirmed, and its "repo-wide grep … none found" is
reproduced here with the denominator it lacked]. `package.json` declares 13
scripts (lines 12–24) and **0** of them stops, restarts or upgrades a running
daemon; `scripts/` holds 20 Python files and **0** shell scripts [Observed,
both counted this session].

### Line numbers re-verified at `a9f671e`

| Dossier citation | At `f4589e2` | At `a9f671e` | Verdict |
|---|---|---|---|
| `resource-ledger.ts` lines 81–121 | ledger interfaces | **81–121**, `ResourceLedgerSummary` 81–90 and `ResourceLedger` 92–121 | exact |
| `routes.ts` lines 99–151 (`boundedResponse`) | the ceiling block | the block is 98–142; `boundedResponse` is **137–142**, exported at 137 | narrowed |
| `routes.ts` lines 206–239 (complete route list) | the `return` array | **206–239**, unchanged | exact |
| `routes.ts` lines 137–142 (503 path, no logging) | the breach branch | **141** is the branch; 137–142 is the function | exact |
| `main.ts` lines 206–208 (`.detail` dropped) | the startup-failure branch | **206–208**, the write at **207** | exact |
| `main.ts` lines 224–234 (signal handlers) | SIGINT/SIGTERM | **224–234** | exact |
| `server.ts` lines 107–115 (`DaemonStart` union) | the failure arms | **107–115**, details at 112–114 | exact |
| `server.ts` lines 165–224 (`handleRequest`) | no logging | handler body **169–224**; 165–167 is `createServer` | narrowed |
| `server.ts` lines 230–231 (bind-failed detail) | the raw listen error | **230–231** | exact |
| `server.ts` lines 269–282 (`minimalRootRoute`) | unwired | **269–282** | exact |
| `project-shape-observation.ts` line 81 (`maxHumanResponseBytes` 2097152) | the constant | **81** | exact |
| `docs/THREE-SURFACE-POC.md` lines 1–90 | the whole file | the file is **89** lines | off by one, immaterial |

## Gate 2 — Doctrine

**VIS-2 — No evidence means Unknown, not success.** Quoted at the clause,
`.syzygy/governance/doctrine/vision.md` lines 96–106: "No surface may declare
a project aligned, converged, or genome-complete — nor turn anything green
— without current evidence… Currency is judged at a status evaluation's
identified as-of instant (architecture.md) — the wall clock never silently
changes a displayed status. Until a claim class declares its currency bound,
its evidence is not current and the claim renders Unknown. *Violation:*
'spec-aligned ✓' computed from a stale index; a stale view silently green; a
status flipping with no new identified evaluation."

The dossier reads this rule **applied to the operator**, and this packet
adopts that reading and states it as a reading: the doctrine's subject is
"a project" and its surfaces, and the daemon serving those surfaces is not
itself a governed project [Inferred — VIS-2's literal subject is the
project's status, and extending it to the process is a construction this
packet makes rather than a quotation it relies on]. What the quotation
*does* give directly is two hard constraints on slice 2, and both are
obeyed: the status surface renders no derived age (the wall clock may not
change a displayed status) and no word meaning healthy (nothing turns
green). Slice 3 is the one slice VIS-2 reaches without construction, because
there the false-success surface is a *project* surface: PWB-REQ-021 readiness
is a rendered project claim, and today a breach that made the page unservable
leaves it unchanged.

**VIS-1's ordering is what ranks the four slices.** Lines 82–94: "(1) truth
and observation determinism; (2) comprehension of the truth's presentation;
(3) momentum (delivery speed); (4) breadth of scope and fidelity of
presentation… Lower ranks are spent before higher ones; rank 1 is never
spent." Slice 3 is a rank-1 change: it makes a declared truth reachable.
Slices 1 and 2 are rank-2: the truth exists in the 503 body and in the
footer, and neither is where an operator looks. Slice 4 is rank-3. That is
the order the handoff recommends, and it is the reverse of the dossier's
build-cost order.

**VIS-4 and VIS-5.** This packet drafts and adopts nothing; the two
questions that could need an amendment (Q3's second arm, Q4's minting arm)
name CC-REV-2 and a new owner act precisely because normative data contracts
are human-gated. Every slice writes into `apps/**`, `packages/**`, `docs/**`
or `scripts/` — the implementation plane — and none writes into
`openspec/**` or `.syzygy/**`.

**SEC-1 — Authenticated by default.** At
`.syzygy/governance/doctrine/security.md` lines 10–23, quoted at the two
sentences Q1 turns on: "**non-browser agent and
CLI clients are admitted only through an explicit machine-client
authentication mechanism**; loopback location alone is never proof of client
identity; and an absent browser Origin header is neither automatically trusted
nor treated as a browser-origin violation… *Violation:* … a machine client
admitted on loopback location alone." This is the clause Q1 puts to the owner
and this packet does not rule.

**SEC-5 — Secrets are never indexed.** Lines 54–60: "A secret reproduced in
any Syzygy surface, store, or endpoint is a trust-floor violation". Slice 1
creates a **new sink**, which is the reason it is not the cheap slice the
dossier calls it. Two constraints follow and both are designed in below: the
structured line never carries the `Authorization` header, any credential
value, or a request body; and it never echoes `url.pathname` raw, because the
path is caller-supplied and reaches the line from outside. The startup banner
already models the discipline — "Credential value is never printed"
(`main.ts` line 219) and `RunningDaemon.credentialPath` is documented "the
PATH, never the value" (`server.ts` line 101).

**SEC-2, SEC-3 and SEC-4 are not engaged, and here is the sweep.** SEC-2
governs governed-project content leaving owner-controlled infrastructure; no
slice transmits anything anywhere — the daemon binds `127.0.0.1` only
(`server.ts` line 34) and no slice adds a client. SEC-3 governs executing
observed code; no slice executes anything from the observed repository, and
slice 4's script re-executes Syzygy's own `npm run poc`. SEC-4 governs writes
into a governed repository; no slice writes into the observed repository, and
the "no pidfile" decision keeps the state directory's write set unchanged
[Observed for the three mechanisms; the judgment that this exhausts the three
rules is [Inferred]].

**RFC5-3 — admission by credential.** Quoted at its defined clause, found
through `DIRECTIVE-REGISTER.md`, which places it at
`.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md` line
101, under the `###` heading "3.2 Client classes" at line 99 — lines
101–107, whole:

> **RFC5-3.** Every request is classified as exactly one of two client
> classes, **by credential presented, never by network location or header
> heuristics**: a request bearing a valid machine credential is a machine
> client; every other request is browser-class. Loopback location alone never
> proves client identity (SEC-1), and an absent browser `Origin` header is
> neither automatically trusted nor treated as a browser-origin violation
> (SEC-1): absence of a header classifies nothing — the request must satisfy
> its class's full discipline.

Lines 109–117 add that the two classes are **exhaustive** and that "no later
contract may introduce one". A status route is therefore not a third thing:
it is browser-class or machine-class, which is exactly Q1, and the second
paragraph's "any client that is not a browser holding a session under RFC5-4
is machine-class" is the sentence that makes Q1's recommended arm the
conservative one.

**The specification treats a log as a governed sink three times, and the
three belong to three different requirements.** This is not doctrine but it
belongs beside SEC-5. **PWB-REQ-003's Oracle** (line 176) says "scan every
model, cache, log, HTML, JSON and record sink for sentinels";
**PWB-REQ-006's** scenario "Active repository content remains inert" (line
407) says "no active content reaches Polaris, JSON, **logs**, caches or
records"; **PWB-REQ-011's** scenario (line 665) says "it stores, **logs**,
caches and returns no unselected body bytes". Requirement headings sit at 160
(PWB-REQ-003), 340 (PWB-REQ-006) and 632 (PWB-REQ-011), so 176 falls under
the first and 665 under the third [Observed, all read at source this session;
corrected 2026-09-15 per review 1, F6. Superseded wording: "**PWB-REQ-006
treats a log as a governed sink, twice**", which credited PWB-REQ-006 with
lines 176 and 665. Nothing downstream moves — all three requirements are in
force and slice 1's new sink is inside all three sink populations — but the
packet should not be the reason a later reader looks for that list under
PWB-REQ-006]. PWB-REQ-006's **own** Oracle is at lines 394–396 and reads
"injected Git/read/render spies, context-independent secret scans, complete
sink-byte scans, a separately accumulated resource ledger and exact final
encoded-byte counts decide" — "complete sink-byte scans", without
enumerating the sinks. Slice 1's test obligations below are written to those
oracles rather than to a convenience.

## Gate 3 — Topology

| Slice | Lives in | Governed artifact touched |
|---|---|---|
| 1 Structured non-2xx line and startup detail | `packages/cap1-daemon/src/server.ts` (a private `logOutcome` called from the four non-2xx branches at 178, 196 and 218, and from a 2xx/non-2xx discriminator around 214); `packages/cap1-daemon/src/server.test.ts`; `apps/three-surface-poc/src/main.ts` lines 65, 89–93, 207 and 241 | none |
| 2 Status route and status line | a new `apps/three-surface-poc/src/status.ts` (the fact builder and both renderers); `apps/three-surface-poc/src/routes.ts` (register the route; call the builder from `html`); `apps/three-surface-poc/src/page-shell.ts` (one optional `pocStatus` slot) and the five footer call sites listed in Q5, which become callers of the one builder | none |
| 3 A served-side breach record that readiness can see | `apps/three-surface-poc/src/routes.ts` (record the breach beside the 503); a new served-side record module beside it; `packages/three-surface-poc-core/src/walkthrough-readiness.ts` (arm 9 gains a second input); `packages/three-surface-poc-core/src/model.ts` (`readinessPopulation`) | **none edited.** The limit identities and the breach shape are read from the registry and from `PwbResourceLimits`; Q4 keeps both unchanged |
| 4 Restart and upgrade | `docs/THREE-SURFACE-POC.md` (a new section); a new shell script under `scripts/`; `package.json` (one script entry) | none |

Boundaries crossed: none. Every file above is in the implementation plane.
The `openspec/**` and `.syzygy/**` trees are read for authority and written
by no slice. The registry JSON is quoted and not edited.

Not touched by any slice: the observation pipeline
(`packages/three-surface-poc-core/src/project-shape-observation.ts` apart
from reading its types), the extraction and coverage stages, the Polaris
renderer's content, and the `PwbResourceLimits` constant itself.

### The authorizing act, per slice

There is **no amendment overlay** for either specification this move rests
on: `openspec/changes/` holds five change directories and neither
`polaris-project-wide-butlers-model` nor `three-surface-poc-experience` has a
sibling amendment package (the two overlays that exist,
`polaris-manifesto-understanding-amendment` and the archive, belong to the
generator) [Observed, listed this session]. The 2026-09-05 PWB amendment was
performed **in place**, against the same files, which is why the predecessor
/ overlay column M6 and M4 carry has no analogue here and is replaced by the
column below.

| Slice | Owner act needed | Named clause, and where it is | Named act and the trigger test |
|---|---|---|---|
| 1 Structured line | **No** | PWB-REQ-006 lines 386–398, the Case/Observable/Oracle block that already names every sink; SEC-5 for the sink's content | Rides `.syzygy/governance/decisions/THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md` lines 55–56 through the recorded-finding limb (S10-F2, S10-F3), and the implementation plane of `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` lines 59–61: "Code in the ordinary implementation plane only — `apps/**`, `packages/**`, tooling, root manifests — never inside `openspec/**` or `.syzygy/**`…" [span narrowed and the elision marked 2026-09-15 per review 1, F8; superseded citation: "lines 59–63". The quoted words end mid-line 61, which continues ", under the in-force craft policies and the vendored `th-engineering` standards" and runs to line 63]. No trigger crossed: no doctrine or contract change, no spec amendment, no registry-envelope change, no observation outside the consented class. **Q2 is the disclosure question, not an act question** |
| 2 Status surfaces | **No for the human line; the machine route is behind P-72, and its credential class is Q1** | POC-REQ-060 (spec line 927) and POC-REQ-061 (line 966) bound the human rendering; the reader note at spec line 26 is what P-72 turns on | Same direction and act. The machine route does not ride them until P-72 is ruled: minting a third machine-credentialed route is the question M5 put and this packet does not answer |
| 3 Served-side breach reaching readiness | **No on the recommended reading of Q3; yes on its second arm** | PWB-REQ-006 line 384, "Every breach SHALL make PWB-REQ-021 readiness false"; PWB-REQ-006 line 378, the two response ceilings; PWB-REQ-021 line 967, "any PWB-REQ-006 resource breach" | Same direction and act on Q3's first arm. On Q3's second arm the trigger is "a further amendment to the signed PWB specification beyond the 2026-09-05 package" (`.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` line 151), which needs CC-REV-2 and a new act. On **Q4's minting arm** the trigger is the registry-envelope clause at lines 154–155 of the same file, quoted in Q4 |
| 4 Restart and upgrade | **No** | none named — argued from S10-F6 and from the direction's recorded-finding limb, not from a requirement clause | Same direction and act. "Tooling" is named in the implementation-plane sentence quoted for slice 1, so a script under `scripts/` is inside it. The direction's own bound applies: each improvement item "must still alter the runnable demonstration or falsify/repair a named product finding" (`.syzygy/governance/decisions/THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md` lines 23–24) — the doc section repairs S10-F6 and the script alters the demonstration |

**The one open bound on every slice, stated not asked.** The PWB change's
`tasks.md` carries **35** checkbox lines under the predicate `^- \[[ xX]\] `,
of which **32** are checked and **3** are not: 4.6 (the owner cold-open
walkthrough), 5.2 (repair recorded findings and confirm) and 5.3 ("Report the
completed improvement cycle to the owner before any next cycle begins")
[Observed, counted this session over a **138**-line file, `wc -l`;
corrected 2026-09-15 per review 1, F9 — superseded figure: "a 139-line
file", the split-on-newline count]. **No M11 slice
duplicates an unchecked task** — unlike M6, whose slices each filed against
one — so M11 is new improvement-cycle scope rather than unfinished signed
work. And 5.3 being unchecked means the *current* cycle has not been reported
to the owner; that constraint is shared by all ten sibling packets and is a
sequencing fact for whoever schedules them, not a question for this one
[Inferred].

**What landing these slices retires.** No act binds any file in the Gate 3
table. Predicate: the file's repository-relative path, or its basename where
that is distinctive, occurring in any tracked `.md` or `.txt` file under
`.syzygy/` or in any tracked file whose basename contains `MANIFEST`.
Denominator: **538** such governance files plus **24** manifests. Result:
**0** manifest rows and **0** act records name any of the fourteen
implementation-plane files; four of them —
`apps/three-surface-poc/src/main.ts`, `apps/three-surface-poc/src/routes.ts`,
`apps/three-surface-poc/src/polaris.ts` and
`packages/three-surface-poc-core/src/model.ts` — occur in exactly one place,
`.syzygy/governance/contracts/candidates/pwb-truth-policy-amendment/IMPACT-LEDGER.md`
lines 61, 66, 67 and 69, which is the CC-REV-2 affected-consumer inventory and
says of itself, at its own lines 3–5: "**Candidate review input — never
authority.** This is the CC-REV-2 affected-consumer inventory. It performs no
act and authorizes no implementation." It is **not** a row of either manifest
in its own directory [Observed, both `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` and
`PWB-EFFECT-AMENDMENT-MANIFEST.txt` searched this session for its basename: 0
hits] — so unlike the general-trusted-bootstrap case AGENTS.md records, this
ledger's classifications bind nothing.

**But that ledger names a fifth consumer this packet had not looked at, and
it matters.** Its row for the file
`apps/three-surface-poc/src/fresh-checkout-demo-main.ts` (line 71) reads
"make every limit/readiness breach affect exit polarity". The
demo's verdict does exactly one limit check —
`check('limit-breaches', inputs.limitBreaches === 0)`
(`apps/three-surface-poc/src/fresh-checkout-verdict.ts` line 130) — over a
number taken from `shape.limitBreaches.length`
(`apps/three-surface-poc/src/fresh-checkout-demo-main.ts` lines 313 and 485),
which is the same input-side count slice 3 is about. **So the fresh-checkout
demo's "every limit breach" gate is blind to a response-ceiling breach in the
same way readiness is** [Observed, all three read at source this session]. It
is not in this packet's Gate 3 table because slice 3 as designed fixes it for
free — the demo reads the same model — but the implementing bead should add
the assertion rather than assume it.

Whether any `docs/evidence/*.json` record binds these bytes by digest is
**[Unknown]** to this packet: the sweep above covered the act corpus, not
every evidence digest table. The implementing bead must run that sweep and
re-record anything it retires, which is verification rule 10 applied to an
evidence record.

All four slices run under `syzygy-dov.11`, the pursuit bead; no new bead is
filed by this packet.

## Gate 4 — Design sketch, per slice

### Slice 1 — Every non-2xx outcome is one line, and a failed start says why (small; no act; Q2 rules the line's content)

**Where.** One private function in `packages/cap1-daemon/src/server.ts`,
called from `handleRequest`'s outcome branches. It is not exported: nothing
outside the daemon decides what a request outcome is, and an exported logger
would become a second vocabulary to keep honest.

**The line.** One JSON object per line on stderr, with a fixed closed key
set and no free text:

```json
{"kind":"request-outcome","method":"GET","route":"/polaris","status":503,"reason":"response-limit-breached","at":"2026-09-15T00:00:00.000Z"}
```

`route` is the **registered route path**, taken from the matched `Route`
value, never `url.pathname` — so a caller cannot write into the log. On the
unknown-route branch there is no matched route, so `route` is omitted
entirely and a separate `pathLength` integer records how long the unmatched
path was; the path itself is never echoed. `reason` draws from a closed
list: `unknown-route`, `credential-refused` (the daemon's own
`REFUSAL_BODY`'s meaning, never the presented credential),
`browser-origin-refused`, `handler-failure` and `response-limit-breached`.
No header, no body, no query string, no credential, ever.

**Why that shape.** **PWB-REQ-003's** Oracle scans "every model, cache,
log, HTML, JSON and record sink for sentinels" (spec line 176), and
**PWB-REQ-006's** own Oracle, at lines 394–396, requires "complete
sink-byte scans"; PWB-REQ-006's scenario at line 407 requires that "no active
content reaches Polaris, JSON, logs, caches or records" [attributions
corrected 2026-09-15 per review 1, F6; superseded wording credited line 176's
sentinel-scan oracle to PWB-REQ-006, which owns line 407 and not 176]. A log
line built only from closed vocabulary and
integers satisfies that by construction rather than by filtering, which is
the difference between a guard and a hope.

**The 503's own line.** `boundedResponse` does not log: it returns a
`RouteResponse` and the daemon's outcome logger sees the 503 like any other
non-2xx. That keeps one logging site rather than two and keeps `routes.ts`
free of a sink.

**Startup detail.** Four sites in `main.ts` gain their dropped cause:
line 207 appends the failure's own `detail` string after its `kind`; line 65
appends the caught error's message; the
89–93 pair appends it on the non-`observer-checkout-dirty` arm; line 241
appends `cause instanceof Error ? cause.message : String(cause)`. Lines 58,
239 and 249 are unchanged, because their unions carry nothing more.

**Oracle.** An injected `process.stderr.write` spy in the daemon's own tests,
independent of the logger: the test asserts the parsed JSON's key set and
values against literals written in the test file, never imported from
`server.ts` (AGENTS.md's conformance rule). A second, independent oracle for
the sentinel property: request a path containing an active-content sentinel
and a credential-shaped sentinel and assert neither string occurs anywhere in
the captured stderr bytes.

**Rule-6 mutants.** (a) Change `route` to use `url.pathname` instead of the
matched route path and confirm the sentinel test fails. (b) Delete the log
call from the handler-throw branch (server.ts line 218) and confirm the
outcome test for 500 fails — one mutant per branch, four branches. (c) Make
the reason string free text and confirm the closed-vocabulary assertion
fails. (d) Revert `main.ts` line 207 to `.kind` alone and confirm the
startup-failure test fails naming the missing detail. (e) Add a header value
to the line and confirm the "no header ever" assertion fails.

**Cost, honestly.** The dossier calls S10-M2 "the cheapest fix in the audit".
It is cheap in lines and not cheap in obligations: it creates a sink the
signed specification already regulates in two places, so its test set is a
sentinel sweep and not an assertion that a string appeared.

### Slice 2 — One place that answers "what am I serving" (medium; human line ruled by Q5; machine route behind P-72 and Q1)

**Where.** A new `apps/three-surface-poc/src/status.ts` exporting one pure
builder and two renderers, so the two channels cannot drift:

```ts
export interface PocStatusFacts {
  readonly startedAt: string;          // process start, ISO-8601
  readonly requestAt: string;          // this request's instant
  readonly evaluation: PocModel['evaluation'];  // snapshot + asOf, verbatim
  readonly observerRevision: string;   // parsed out of the snapshot
  readonly projectRevision: string;
  readonly credentialProvision: 'minted' | 'reused';
  readonly lastResponseLimitFailure: ResponseLimitFailure | undefined;
}
```

**Two identified instants, never an age.** `startedAt` and `requestAt` are
both recorded instants; nothing subtracts them. The reader may; the surface
may not (VIS-2, Gate 2). The same rule kills the word *healthy*: the body
carries facts and, where a fact is unavailable, the string `Unknown` with a
reason — never a verdict (POC-REQ-032's falsifier, spec line 596).

**The human form** is one line rendered by `pageShell`, in a new optional
`pocStatus` slot rendered directly under the existing `header` block so it is
above the fold rather than in the footer; Q5 decides whether every page gets
it or only the home page and the status route. The five footer call sites
listed in Q5 become callers of the one builder, which is the smallest change
that stops a sixth restatement from appearing.

**The machine form** is the same `PocStatusFacts` as JSON at
`GET /api/poc/status` with a `kind` and a `version`, in the shape
`PolarisPresentationEnvelope` already models (`routes.ts` lines 24–32). It
does not ship until P-72 rules that a third machine-credentialed route may be
minted, and Q1 rules its credential class.

**`lastResponseLimitFailure`.** A module-level reference in `routes.ts` set
on the 503 branch and read by the builder. It is deliberately *not* a
history: one slot, last-writer-wins, cleared by nothing. That is the honest
minimum — "the last render that did not fit, and what it was" — and it
avoids inventing a retention posture the acts do not cover.

**Oracle.** A copy oracle over the rendered line and the JSON body: every
field of `PocStatusFacts` appears in both channels with equal value, compared
by an extractor that imports no rendering code. Per AGENTS.md's copy-oracle
caution, no label may be a short word another part of the page reaches by
coincidence, so each field carries a distinctive `data-poc-status-*`
attribute and the oracle matches on those, not on the visible text.

**Rule-6 mutants.** (a) Drop one field from the human renderer and confirm
the parity oracle fails naming that field. (b) Render a derived age instead
of `requestAt` and confirm the "no derived value" assertion fails. (c) Render
the literal `healthy` and confirm the forbidden-word assertion fails. (d)
Return a stale `lastResponseLimitFailure` after a successful render and
confirm the last-writer assertion fails. (e) Give two fields the same
`data-poc-status-*` attribute and confirm the oracle's denominator check
fails rather than passing on a coincidence.

**Byte cost, measured against the budget it charges.** Q5 quotes the
headroom: 612,665 bytes on the tailnet form. A status line held under 400
bytes is under 0.07% of that on every page. The bead must re-measure rather
than trust this figure, because M1 lane B (P-68) is still open over the same
budget.

### Slice 3 — A final-output breach becomes a breach the readiness arm can see (medium; Q3 rules it; Q4 keeps the registry unchanged)

**The constraint that shapes it.** The evaluation's ledger cannot take the
record: its breaches are snapshotted into a frozen, digest-covered
observation before any response exists (Measurements, "Where a served-side
breach cannot go"). So slice 3 does **not** add `chargeOutput` to
`ResourceLedger`, which is where S7-M3 and S7-F3 point.

**What it adds instead.** A served-side record beside `boundedResponse`, in
the same module, holding zero or more `ResourceLimitBreach` values — the
existing type, with `limit` set to the ceiling that was breached, which
`keyof PwbResourceLimits` already admits (Measurements). It is per process,
not per evaluation, and it is reset when the model is rebuilt, because a new
evaluation is a new question.

**How readiness sees it, and the trap in doing it the obvious way.** The
obvious design — a new, distinctly named readiness finding for the served
side — is wrong, and the source says why. `READINESS_ARMS`
(`packages/three-surface-poc-core/src/walkthrough-readiness.ts` lines 47–58)
is a **closed list of exactly ten**, and its own doc comment at lines 45–46
reads: "The ten readiness arms, one per clause of the requirement's readiness
sentence. Each makes readiness false; none is an act-validity case." An
eleventh arm would break that one-per-clause correspondence with PWB-REQ-021
lines 964–968 and would itself be a specification claim [Observed for the
list and the comment; Inferred for the consequence].

So slice 3 adds **no arm**. It feeds the existing ninth one, `resource-breach`
— the arm whose clause is literally "any PWB-REQ-006 resource breach" — and
distinguishes the side in the finding's *message*, which is free text today
(`walkthrough-readiness.ts` lines 365–366). `ReadinessPopulation`
(lines 83–89) gains one more number beside `limitBreaches`, supplied by
`readinessPopulation` (`packages/three-surface-poc-core/src/model.ts` lines
**211–220** — signature at 211, closing brace at 220, its doc comment
ending at 210) [corrected 2026-09-15 per review 1, F12; superseded citation:
"lines 213–221". Q3's separate cite of lines 217–219 for the input-side
snapshot is inside the function and is unchanged]; arm 9's condition becomes
the sum. The evaluator stays pure and
injectable and the core package gains no import from the app. **This is also
the strongest form of Q3's recommended answer:** the arm already exists and
its clause already names the whole of PWB-REQ-006, of which the two response
ceilings are members by line 378; what is missing is a number, not a
concept.

**What it must not do.** It must not touch the PWB-REQ-022 evaluator
(AGENTS.md's standing seam rule and PWB-REQ-021's own lines 975–977:
"These readiness cases belong only to PWB-REQ-021. They SHALL NOT be added
to, substituted for or treated as invalid arms in PWB-REQ-022's owner-act and
record-validity population…") [span narrowed and the elision marked
2026-09-15 per review 1, F8; superseded citation: "lines 975–978". The
quoted words end mid-line 977, which continues "; a structurally lawful run
can be not ready, and a valid owner act can lawfully retain a negative
judgment about it" and ends on 978]. It must not change `observationDigest`
or any
field under it. And it must not make the breach retroactive: a breach at
instant T makes readiness false from T, and the record says when.

**Oracle.** Two independent ones, because the claim is a conformance claim.
(a) A behavior test that serves a body one byte over a fixture ceiling and
asserts both that the 503 is unchanged byte-for-byte and that the readiness
evaluation for the same model now carries the served-side finding. (b) A
counterexample at `limit - 1`, `limit` and `limit + 1`, which is the sweep
PWB-REQ-006's own Case line already demands ("every limit at `limit - 1`,
`limit`, and `limit + 1` … and both final-output sinks", spec lines 386–391)
— the existing suite exercises the input limits at those three points and
this extends the same discipline to the output sinks.

**Rule-6 mutants.** (a) Record the breach but do not thread it into
`ReadinessPopulation`, and confirm the readiness test fails. (b) Set the
breach's `limit` to `maxTotalBytes` instead of the response ceiling and
confirm the which-side test fails. (c) Make the served record survive a model
rebuild and confirm the new-evaluation test fails. (d) Mutate the boundary
from `observed <= declared` to `observed < declared` (`routes.ts` line 140)
and confirm the `limit`-exactly test fails — a mutant that also proves the
existing 503 guard is real. (e) Add an eleventh entry to `READINESS_ARMS` and
confirm the closed-ten assertion fails; and separately add the served finding
to PWB-REQ-022's population and confirm its closed-denominator assertion
fails (PWB-REQ-021's oracle fixes that denominator at "84 present-invalid
plus 2 absent cases", spec lines 992–993).

### Slice 4 — The operator has a written answer and one command (small; no act)

**The doc.** A new section in `docs/THREE-SURFACE-POC.md` stating three
facts, each of which is true today and written down nowhere:

1. The daemon observes Git **once, at process start** — `main.ts` lines
   80–87 run inside the launch callback, before `createDaemon` — so a new
   Butlers commit or a new Syzygy build reaches a surface only after a
   restart.
2. The state directory survives a restart untouched: the credential is
   reused rather than reminted (`packages/cap1-daemon/src/credentials.ts`
   line 175), and `credentialProvision` on the startup banner says which
   happened (`main.ts` line 218).
3. Shutdown is `SIGINT` or `SIGTERM` and is idempotent (`main.ts` lines
   224–234); there is no other stop mechanism, and the process writes
   nothing on the way out.

**The script**, a new shell file under `scripts/` plus one `package.json`
entry. It takes the port, finds the listening process, sends `SIGTERM`,
waits for the socket to close, and re-executes the same `npm run poc`
invocation with the same arguments. **No pidfile** — the system test quoted
in "Decided in this packet" asserts the state directory holds exactly one
entry, and a pidfile would fail it. The script never touches the observed
repository.

**Oracle.** The closest existing prior art is
`packages/cap1-daemon/src/server.test.ts` lines 159–174: a describe block
named "RT3 — credential stability across daemon restarts" whose single test,
"a restarted daemon reuses the same credential file and token", starts a
daemon, closes it, starts a second against the same state directory and
asserts `credentialProvision` is `reused`, that the credential path is
identical and that the token bytes are unchanged [Observed, read at source
this session; cited 2026-09-15 per review 1, F2 — the first draft's
word-bounded lifecycle predicate hid that file, so the packet did not know
the test existed]. Slice 4's own oracle is a system-level test in the shape of
`packages/cap1-system/src/degradation.system.test.ts`, which already starts a
daemon twice against one state directory (its lines 74–96): assert the second
start reports `reused`, that the state directory still holds exactly one
entry after both, and that the second daemon serves the new revision. The doc
claims are asserted against the source, not restated: a check reads the three
line references above and fails if the construct moved.

**Rule-6 mutants.** (a) Make the script write a pidfile and confirm the
state-directory test fails. (b) Make the script `SIGKILL` and confirm the
clean-shutdown assertion fails (the shutdown line is not written). (c) Move
the `observeGitRepository` calls after `createDaemon` and confirm the
once-at-start assertion fails. (d) Change `credentials.ts`'s reuse branch and
confirm the `reused` assertion fails.

### Design bar for the human surface

The status line is one row, not a panel: label, value, label, value, in the
page's existing type scale and epistemic encoding (POC-REQ-060, spec line
927). It carries no color that is not already in the token set, no icon, and
no state that is not one of the three epistemic labels the legend defines.
Keyboard and non-visual reading are unchanged because the line adds no
interactive element and no fragment target — AGENTS.md's rule that a
fragment target must never sit inside a `<details>` is not engaged, because
the line has neither.

## Gate 5 — Specification

Two signed specifications are in force over this surface and neither has an
amendment overlay: `polaris-project-wide-butlers-model` (17 requirements, 31
scenarios) and `three-surface-poc-experience` (24 requirements, 24 scenarios)
[Observed, counted this session with the predicates `^### Requirement` and
`^#### Scenario`]. The 2026-09-05 PWB amendment was performed against these
same bytes, so every citation below is to the effective text.

### Does the readiness widening need a delta? (Q3)

**No, on the recommended arm, and the argument is two quotations rather than
a reading.** PWB-REQ-006's requirement text ends, at spec lines 378–384:

> Final encoded human HTML and machine JSON SHALL each have an explicit byte
> ceiling. A source or input breach SHALL keep the complete source population
> counted and every dependent fact Unknown. A final-output breach SHALL
> return only a bounded typed failure envelope carrying evaluation identity,
> limit identity, declared value, observed value and population counts; it
> SHALL NOT truncate or emit a success-shaped model. Every breach SHALL make
> PWB-REQ-021 readiness false.

And PWB-REQ-021's readiness sentence, spec lines 964–968:

> Readiness SHALL be false for a missing, empty, duplicate or unrecognized
> answer identity; an unresolved source anchor; a surface/evaluation
> mismatch; any path outside Polaris or its same-evaluation exact-source
> route; any PWB-REQ-006 resource breach; or an answer whose cited current
> Butlers authority cannot be resolved.

The response ceilings are declared **inside PWB-REQ-006** by the first
sentence; "every breach" in the last sentence has no qualifier narrowing it
to input-side breaches; and "any PWB-REQ-006 resource breach" in PWB-REQ-021
is the clause the existing closed arm `resource-breach` implements. Feeding
that arm a number it does not yet receive changes no requirement text.

**The residue, and it is a genuine owner question.** PWB-REQ-006's Oracle
line reads "injected Git/read/render spies, context-independent secret scans,
complete sink-byte scans, **a separately accumulated resource ledger and
exact final encoded-byte counts** decide" (spec line 395). That sentence
treats the ledger and the final byte count as two oracles, which is a reading
under which "every breach" might mean every breach *the ledger holds*. This
packet records the divergence and does not choose: Q3 is the question.

### Does a status route need a delta?

**The route's existence is P-72's question and this packet does not answer
it.** What this packet adds to it is one measurement P-72 did not have: the
`/api/poc/polaris` precedent M5's Q1 names is a route serving a body that is
*not* derived from the model alone but from a render of it
(`renderPolarisPresentation`, `routes.ts` lines 163–176), whereas a status
body is assembled entirely from fields the model and the daemon already hold
and would fall inside M5's proposed "derived read-only machine view" category
without straining it [Inferred — a judgment about how a proposed category
would classify a body neither M5 nor this packet has built].

**The human status line needs no delta.** It renders no project claim: every
field is an identity or an instant the footer already carries, plus the
credential *provision kind* and the last breach. POC-REQ-060 (spec line 927)
and POC-REQ-061 (line 966) bound how it renders, not whether.

### The RFC2-26 test, run over all four slice rows

RFC-0002 is an accepted design contract in force. Its phase rule is quoted
verbatim at the defined clause, located through `DIRECTIVE-REGISTER.md` at
`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md` line
196, under the `###` heading "Authority boundary at the OpenSpec seam
(binding phase rule)" at line 194 — lines 196–221, **the whole clause, both
paragraphs, with no elision**:

> **RFC2-26.** This contract schedules nothing: **it is not a specification of
> record from which implementation work may be scheduled**. No implementation
> work for user-observable consequences of this contract — evaluation and
> snapshot displays, claim and challenge rendering, Unknown-reason and
> rendering-tier presentation, reconciliation-chain and gap surfaces, API
> answers over epistemic state — may be scheduled solely from this RFC.
> Before implementation, every observable consequence either maps to an
> approved OpenSpec requirement and scenario in the governance root's
> `openspec/**` plane, or carries a reviewed N/A judgment proving it purely
> structural with no independently testable behavior. **The reviewed N/A
> judgment's home and gate.** A reviewed N/A judgment is a recorded owner
> judgment homed in `decisions/` (RFC3-15), and the judgment is honored only
> through an effective owner act under RFC3-16(a), in state (1) or state (2),
> with that state rendered; absent or invalid acts map nothing and leave the
> consequence unmapped and Unknown, never covered (RFC3-16(a)'s effect rule;
> VIS-2).
>
> **Rows are per observable consequence, not per clause.** A clause with five
> observable consequences and one mapped requirement is not covered; the
> matrix discloses the consequences it enumerates for each clause, so a
> complete-looking matrix over under-enumerated consequences is a defect of
> the matrix. At surface specification a clause-to-requirement coverage
> matrix over RFC2-1..RFC2-26 is produced — **that matrix is review material,
> never authority**. This clause creates no OpenSpec content now (none may
> exist during bootstrap). This clause binds the whole RFC 0002 package, not
> this module alone. (Shape-parallel with RFC6-28, RFC7-38, RFC8-32, RFC9-52,
> RFC10-16, RFC11-12.)

**The denominator is four**: the four slice rows of Gate 3's authorizing-act
table [Observed, counted this session over that table]. The test is run over
all four. Every requirement and scenario cited below was read at source this
session.

| Slice | RFC2-26 consequence class | Approved requirement **and** scenario | Limb 1 |
|---|---|---|---|
| 1 Structured line | **None enumerated.** A stderr line is not a rendering, not a claim, not an Unknown-reason presentation and not an API answer; no class in the clause's list fits. The line is nevertheless inside PWB-REQ-006's sink population, which is a different requirement's obligation and is discharged in Gate 4 | n/a for RFC2-26. The governing obligation is **PWB-REQ-006** (spec line 340) via scenario **"Active repository content remains inert"** at spec lines 404–408, whose THEN reads "no active content reaches Polaris, JSON, logs, caches or records" | n/a. The clause is not engaged; slice 1 is scheduled from a recorded finding under the improvement-cycles direction |
| 2 Status surfaces | "evaluation and snapshot displays" (the human line renders the evaluation identity and two instants); "API answers over epistemic state" (the machine form, if minted, answers with `Unknown` where a fact is unavailable) | **POC-REQ-060** — "One design language, one epistemic encoding" (spec line 927) — and **POC-REQ-032** (spec line 574), scenario **"Unknown disclosed in the narrative"** at spec line 599, for the rule that an unavailable fact renders as a disclosed Unknown rather than as nothing. For the **evaluation-identity display** specifically, **PWB-REQ-020** (spec line 902), scenario **"Complete model has wire parity"** at spec lines 928–933, is the requirement a two-channel status must satisfy | **Available for the human line** on POC-REQ-060 plus POC-REQ-032's scenario. **Partial for the machine form**: PWB-REQ-020's scenario speaks of "a project-wide evaluation" Polaris renders, and a status body is not a project-wide evaluation, so the parity obligation applies by analogy rather than by its own scenario's terms. This packet does not call the machine form lawful or unlawful on that: it is behind P-72 and Q1, and if the owner reads RFC2-26's bar strictly the route needs a scenario through CC-REV-2 or the reviewed N/A route the clause itself names — which this packet judges unreachable here, because a status answer is independently testable and the N/A route admits only a consequence "purely structural with no independently testable behavior" [Inferred] |
| 3 Readiness widening | "API answers over epistemic state" (readiness is machine-readable by PWB-REQ-021's own line 969); arguably "Unknown-reason … presentation", since the readiness finding carries a reason string rendered on Polaris | **PWB-REQ-006**, spec line 340, scenario **"Resource breach is bounded and explicit"** at spec lines 419–426, quoted verbatim: "**WHEN** any evaluation-wide input, deterministic parse-work or final-output ceiling is exceeded / **THEN** the evaluation names the exact limit and counts the affected population as Unknown without emitting a partial success-shaped answer / **AND** human and machine responses stay within their own declared encoded-byte ceilings and cold-open readiness is false". Also **PWB-REQ-021**, spec line 946, scenario **"Lawful run can remain not ready"** at spec lines 1009–1015 | **Available**, and the scenario is the closest possible match: its WHEN names the final-output ceiling explicitly and its AND limb names cold-open readiness false. This is the row that makes slice 3 a conformance repair rather than a feature |
| 4 Restart and upgrade | **None enumerated.** A documentation section and a shell script render nothing, claim nothing and answer no query over epistemic state | n/a | n/a. Argued from S10-F6 and the improvement-cycles direction's recorded-finding limb; the direction's "must still alter the runnable demonstration or falsify/repair a named product finding" bound is met by both halves |

**What the test establishes and what it does not.** It establishes
[Observed] that slice 3 maps to a requirement-and-scenario pair whose WHEN
limb names its exact trigger, that slice 2's human line maps to two POC
requirements and its machine form's parity scenario is a partial match, and
that slices 1 and 4 enumerate no consequence of RFC-0002 at all. It does not
establish that any slice is lawful: that is the owner's, and RFC2-26's own
scope sentence — "This clause binds the whole RFC 0002 package, not this
module alone" (lines 219–220) — is a reading the owner may take more or less
broadly than this packet has.

### New WHEN/THEN scenarios, for the beads' acceptance contract, not the spec

These are acceptance criteria for the implementing beads. They are **not**
proposed spec text and nothing here amends a requirement.

**S1 (slice 1).** WHEN the daemon answers any request with a status outside
200–299, THEN exactly one JSON line is written to stderr naming the method,
the matched route path, the status and a reason drawn from the closed list,
AND a 2xx response writes no line.

**S2 (slice 1).** WHEN a request arrives for an unregistered path containing
an active-content sentinel, THEN the stderr bytes contain the sentinel zero
times, AND the line carries the unmatched path's length rather than the path.

**S3 (slice 1).** WHEN a request presents an invalid credential, THEN the
stderr bytes contain the presented credential zero times, AND the line's
reason is the closed value for a refused admission.

**S4 (slice 1).** WHEN the daemon cannot bind its port, THEN the startup
failure line names both the failure kind and the `.detail` string, AND a line
naming only the kind is not an acceptable failure message.

**S5 (slice 2).** WHEN the status facts are rendered on both channels for one
evaluation, THEN every field appears in both with equal value, AND the oracle
reports both denominators.

**S6 (slice 2).** WHEN a fact the status surface names is unavailable, THEN
it renders as `Unknown` with its reason, AND no field renders as absent,
blank, or as a word meaning healthy.

**S7 (slice 2).** WHEN a render breaches a response ceiling and a later
render does not, THEN the status surface names the last breach with its limit
identity and its instant, AND it does not report a breach after the record is
reset by a model rebuild.

**S8 (slice 3).** WHEN a human response is one byte over
`maxHumanResponseBytes`, THEN the 503 body is unchanged byte-for-byte from
today, AND the same evaluation's readiness is false through the ninth arm,
AND `READINESS_ARMS` still has exactly ten entries.

**S9 (slice 3).** WHEN a response is exactly `maxHumanResponseBytes` bytes,
THEN it is served and no breach is recorded; and WHEN it is one byte more,
THEN it is not served and one breach is recorded — the `limit - 1` / `limit`
/ `limit + 1` sweep PWB-REQ-006's Case line already requires, extended to
both final-output sinks.

**S10 (slice 3).** WHEN a served-side breach is recorded, THEN PWB-REQ-022's
act-validity denominator is unchanged at 84 present-invalid plus 2 absent
cases, AND no readiness case has been added to it.

**S11 (slice 4).** WHEN the restart script runs against a daemon started with
an explicit state directory, THEN the old process receives `SIGTERM` and
writes its shutdown line, the new process reports `reused` provision, and the
state directory holds exactly one entry throughout.

**S12 (slice 4).** WHEN the observed repository advances by one commit and
the script runs, THEN the served revision is the new one, AND a daemon that
was not restarted still serves the old one — the fact the doc section states.

## Collision and sequencing

**Unlike M6, the file-set intersection here is not zero, and the reason is
that M11's subject is the daemon every other move renders through.** Two
predicates are reported, both computed this session.

**Predicate A — citation.** Extract every code span from every Markdown file
under each sibling worktree's `docs/design/`; keep those beginning `apps/`,
`packages/`, `scripts/` or `docs/`, or equal to `package.json`; keep those
that resolve as a **file** in this worktree; intersect with M11's 16-file
candidate surface (the fourteen of Gate 3 plus
`apps/three-surface-poc/src/materialize-action.ts` and
`packages/three-surface-poc-core/src/project-shape-model.ts`, both reachable
from slice 1's route population and slice 3's model path).

**Predicate B — proposal.** The same extraction restricted to each packet's
`## Gate 3 — Topology` section, which is where a packet says what it would
*touch*. A citation is not a proposal (verification rule 5), and the two
columns differ by a factor of two on several rows.

| Sibling | Head read this session | A: citation ∩ M11's 16 | B: Gate 3 ∩ M11's 16 | The B files |
|---|---|---:|---:|---|
| M1 lane B, PR #35, P-68 | `4090f98` | 1 | **0** | — (its Gate 3 names no file on M11's surface) |
| M2, PR #36, P-69 | `f2f37dd` | 4 | **4** | `main.ts`, `routes.ts`, `model.ts`, `project-shape-model.ts` |
| M3, PR #37, P-70 | `6574600` | 3 | **1** | `polaris.ts` |
| M4, PR #38, P-71 | `63b8e33` | 7 | **6** | `orrery.ts`, `polaris.ts`, `routes.ts`, `trajectory.ts`, `model.ts`, `project-shape-model.ts` |
| M5, PR #39, P-72 | `ba9ca61` | 6 | **4** | `polaris.ts`, `routes.ts`, `model.ts`, `project-shape-observation.ts` |
| M6, PR #40, P-73 | `83c9f60` | 2 | **1** | `package.json` |
| M7, PR #42, P-76 | `f97baf4` | 5 | **4** | `polaris-source.ts`, `routes.ts`, `package.json`, `project-shape-observation.ts` |
| M8, PR #43, P-74 | `bce9039` | 14 | **9** | `main.ts`, `orrery.ts`, `polaris-source.ts`, `polaris.ts`, `routes.ts`, `trajectory.ts`, `model.ts`, `project-shape-model.ts`, `walkthrough-readiness.ts` |
| M9, PR #41, P-75 | `65de02b` | 8 | **4** | `polaris.ts`, `routes.ts`, `trajectory.ts`, `model.ts` |
| M10, PR #44, P-77 | `95f31cb` | 7 | **5** | `polaris.ts`, `routes.ts`, `package.json`, `server.ts`, `model.ts` |

(Paths in the last column are basenames of files already named in full in
Gate 3; the full paths are `apps/three-surface-poc/src/<name>` for the app
files, `packages/three-surface-poc-core/src/<name>` for `model.ts`,
`project-shape-model.ts`, `project-shape-observation.ts` and
`walkthrough-readiness.ts`, and `packages/cap1-daemon/src/server.ts`.)

**The load-bearing facts.** `apps/three-surface-poc/src/routes.ts` appears in
**7** of the ten siblings' Gate 3 tables and
`packages/three-surface-poc-core/src/model.ts` in **6**; M11 is the only
packet naming `packages/three-surface-poc-core/src/resource-ledger.ts`,
`apps/three-surface-poc/src/page-shell.ts` or `docs/THREE-SURFACE-POC.md` in
its Gate 3 at all [Observed, both predicates computed this session over the
ten worktrees at the heads named]. **M8 is the largest overlap** at 9 of 16
and the two packets touch `walkthrough-readiness.ts` from opposite ends: M8's
subject is the profile as a registry input, M11's is arm 9's population.

**Named collisions, per the prompt's list.**

- **M10 (P-77, PR #44) owns the machine contract.** Slice 2's machine form
  would be a new machine route with its own body, response headers and
  identity — all three of which are M10's subject. M11 mints nothing on that
  channel until M10 lands, and the status route's response identity is M10's
  `inputsDigest` question, not a second answer to it.
- **M5 (P-72, PR #39) owns route existence on the machine channel.** Slice
  2's machine form holds behind P-72, as M10's slice 3 does. This packet asks
  no route-existence question and sequences identically.
- **M1 lane A (main, P-67) and lane B (PR #35, P-68) own the ceiling
  headroom.** Slice 2's human line spends it; Q5 is where the owner rules
  that, and lane B is still open over the same budget, so the implementing
  bead must re-measure rather than reuse Q5's figure.
- **M6 (P-73, PR #40) owns generator honesty and any stderr line the
  generator emits.** Slice 1's logger is registered in the daemon and sees
  only HTTP request outcomes; the generator's demo writes its own lines from
  `apps/three-surface-poc/src/polaris-generation/pipeline-demo-main.ts` lines
  35–36, which slice 1 does not touch [Observed]. The two do not overlap.
- **M4 (P-71, PR #38) owns the owner loop's evidence records.** Slice 2's
  `lastResponseLimitFailure` is deliberately **not retained**: one in-memory
  slot, no file, no record. If the owner wants last-request outcomes kept
  across a restart, that is M4's retention question and not this packet's.

**Sequencing inside M11.** Slice 1 is independent of everything and should
land first. Slice 3 is independent of slices 1 and 2 and is the rank-1
change. Slice 4 is independent of all three. Slice 2's human line depends on
Q5 and on lane B's budget; its machine form depends on P-72, Q1 and M10.

**Not verifiable this session.** [Unknown] Whether the sibling branches'
actual diffs stay inside the paths their Gate 3 tables name, until they land
— predicate B measures what each packet *says*. [Unknown] Which arm the
owner takes on Q3, and therefore whether slice 3 is conformance or an
amendment. [Unknown] Whether any `docs/evidence/*.json` digest table binds
the bytes slices 2 and 3 would edit.

## Gate 6 — Engineering bar

1. **Every count carries its predicate and its denominator**, and every one
   was taken this session in the worktree at `a9f671e`. Route counts are
   computed by importing the built route builders, not read off the source
   (verification rule 3). Sweeps that matter were run with Python `re` rather
   than shell `grep`, per verification rule 1.
2. **Two methods for the load-bearing zero.** "The breach reaches no ledger,
   stderr or status record" is established both by the 81-file sink sweep and
   by the independent fact that `routes.ts` imports no `ResourceLedger` at
   all — and corroborated a third way by the retained capture, whose
   `daemon.err` is 0 bytes after two 503s (rule 2).
3. **The absence claims name their denominators.** 81 non-test files for the
   logging sweep; 558 of 1,216 tracked files for the lifecycle sweep, whose
   result is now published under both a substring and a word-bounded
   predicate over that one denominator (29 files and 22); 538 governance
   files plus 24 manifests for the act-binding sweep; 17 routes for the
   status-route sweep; **1,152** and **1,008** spec lines, both `wc -l`, for
   the operability vocabulary sweep (rule 9) [corrected 2026-09-15 per review
   1, F9 and F2; superseded wording: "558 of 1,216 tracked files for the
   lifecycle sweep" without its two predicates, and "1,153 and 1,009 spec
   lines"].
4. **Rule-6 mutants are specified per slice and per guard branch**, above;
   each names the predicate to mutate and the fixture that must then fail.
   Slice 1's are one per outcome branch, because a single mutant over a
   four-branch logger proves one branch.
5. **Conformance expected values are literals in the tests**, never imported
   from the module under test (AGENTS.md).
6. **The copy-oracle caution is applied**: slice 2's parity oracle matches
   distinctive `data-poc-status-*` attributes, not short visible words, and
   one mutant checks that two fields sharing an attribute fails rather than
   passes.
7. **A closed list was checked before a slice proposed to extend it.**
   `READINESS_ARMS` is ten by construction and one per clause; slice 3 was
   redesigned to feed the ninth arm rather than mint an eleventh.
8. **No act-bound byte is proposed for edit.** The registry JSON is quoted
   and not touched, and both specifications are read only. The fourteen
   implementation-plane files were swept against the act corpus with the
   predicate and denominator stated in Gate 3; the four hits are in a
   self-declared non-authoritative CC-REV-2 inventory that is not a row of
   either manifest in its own directory.
9. **Independent review.** This packet has had **one**, retained verbatim
   and disclosed in the review-1 section below; its `independent_review`
   count in the evidence record beside it is 1 [superseded wording,
   2026-09-15: "This packet has had **none**. It is a first draft and its
   `independent_review` count in the evidence record beside it is 0."].
   Verification rule 10: review 1 is bound to the bytes at `2c62d0b` and not
   to these, so the thirteen exception repairs are uncovered until a second
   review; superseded wording is marked and dated in place throughout this
   pass, never deleted.
10. **Conventions this packet was checked against, this session.** Every
    non-fence line has an even backtick count, so no code span is broken
    across a line break (0 of **1,553** non-fence lines; superseded figure,
    exact over the first draft at `2c62d0b`: **1,257**). Every code span
    matching CG-1b's extension set — `.md`, `.py`, `.sh`, `.yaml`, `.json`,
    `.txt` — resolves in this worktree: **0** unresolved. Spans that name a
    file this worktree does not hold are written **without** backticks for
    exactly that reason: the M10 packet, and slice 4's not-yet-written
    script. Of **374** distinct code spans, **36** contain a `/` and
    do not resolve as a path; each is enumerated and none is a path claim,
    and they partition as 22 + 5 + 2 + 2 + 1 + 1 + 1 + 1 + 1 = 36
    [re-derived 2026-09-15 over the final bytes of the review-1 pass and
    iterated to a fixed point, since this file states the figures;
    superseded figures, exact over the first draft at `2c62d0b`: **326**
    distinct spans, **34** non-resolving, partitioned 21 + 5 + 2 + 2 + 1 + 1
    + 1 + 1 = 34. The two the review-1 repairs added are the bare
    `/butlers-syzygy/` route, which F11 names, and this packet's own branch
    name]. **22 are HTTP routes**: the 17 method-and-path spans of the route
    table, the proposed `GET /api/poc/status`, the three bare forms
    `/polaris`, `/api/poc` and `/api/poc/polaris`, and the bare
    `/butlers-syzygy/`. **5 are write-root globs**: `.syzygy/**`,
    `openspec/**`, `apps/**`, `packages/**`, `docs/**`. **2 are the RFC2-26
    quotation's own bare `decisions/` and the glob `docs/evidence/*.json`.**
    **2 are placeholder forms** used in the collision table's note:
    `apps/three-surface-poc/src/<name>` and
    `packages/three-surface-poc-core/src/<name>`. **1 is a command**,
    `python3 scripts/check_governance.py`. **1 is the session capture path**
    `scratchpad/capture/polaris.html`, outside the repository. **1 is the
    file slice 2 would create**, `apps/three-surface-poc/src/status.ts`.
    **1 is a repository-relative source path written without its `apps/`
    prefix**, `polaris-generation/pipeline-demo-main.ts`. **1 is a Git
    branch name**, `agent/syzygy-dov.11`. (`/` itself is not in this
    population: it resolves, as the filesystem root.) **Three**
    over-width lines remain outside fences, tables, headings and block
    quotes, and each is a single unbreakable code-span path: line 107
    (80 columns) in "Decided in this packet, not put to the owner",
    which ends at line 118; line 142 (79) in Gate 0, which opens at line
    120; and line 704 (85) in Gate 3
    [locations corrected 2026-09-15 per review 1, F10; superseded wording:
    "the two decision-record paths in Gate 0 and the impact-ledger path in
    Gate 3" — only one of the two decision-record paths is in Gate 0. The
    count of three and the unbreakable-code-span characterization both
    survive; the line numbers are re-derived over the final bytes of this
    pass, after every edit of it, and the broader figure over every non-fence
    non-table line is restated in the review-1 section below].
    No observed-repository path is backticked anywhere in this file. No act
    argument, manifest digest or truncated signed digest is reproduced: the
    one digest comparison this packet made is reported as a match and the
    record is cited by path, per CG-7e and CG-15.

11. **Validation.** `python3 scripts/check_governance.py` was run in this
    worktree at the end of the drafting pass and again at the end of the
    review-1 pass, tail line read rather than an exit code or a grep count
    (verification rule 4); both runs are recorded in the evidence record
    beside this packet and both end `0 FAIL`.

## Review 1 and repairs (2026-09-15)

An independent fresh-context review of this packet (read-only; only the
artifact, its governing references and the acceptance criteria) is retained
verbatim at `docs/reviews/R-POLARIS-M11-OPERABILITY-FUNNEL-RAW.md` (36182
bytes, sha256
`943d567120272ac97e05b6de0b61f14800d5ed973df6f353e9b052e60d3ac049`, both
computed this session with `wc -c` and `sha256sum`, never transcribed). It
reviewed commit `2c62d0b`, at which the two reviewed files hashed as follows,
recomputed this session with `git show 2c62d0b:<path>` piped to `wc -c` and
`sha256sum`:

| File reviewed | Bytes | sha256 |
|---|---:|---|
| `docs/design/POLARIS-M11-OPERABILITY-FUNNEL.md` | 102079 | `6f7e98bad81bb3f30a614bfe944d54b1d71091fb5608a6e7f4410827c6cf3eeb` |
| `docs/evidence/polaris-m11-operability-funnel-2026-09-15.json` | 39956 | `3f6b239183a8939db797fbe8e5c0029d47d2d4d5f7baa299d262c859be0cb320` |

Both match the raw's own table exactly.

Its verdict word, copied exactly: **CONFIRM WITH EXCEPTIONS**. Its counts, as
the raw states them: **blocking 0, non-blocking 7 (F1–F7), editorial 6
(F8–F13)** — thirteen findings in all.

**Its Q1–Q5 table, in one line:** all five scopes truthful, all five genuine
hard human gates with **Q4 "Partly"** (its first half the packet answers
itself and answers right; what remains for the owner is "do you want a
distinct limit anyway" plus the escalation-trigger consequence if so), every
recommendation following from its evidence and conservatively stated, every
lawful arm named and none called unlawful, every default lawful — with one
arm the raw says is lawful and unnamed, Q5's third: render the status line on
the status route only and not on the home page. The raw records that three of
the five defaults differ from their recommendation and that no owner
trade-off is smoothed into consensus language [Observed, read from the
retained raw].

**Its Gate 5 verdict, in one line:** the packet's RFC2-26 block quote is
**identical** to the source at
`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md` lines
196–221, both paragraphs and no elision, compared programmatically after
normalizing whitespace and emphasis; the test is run over all four slice rows
(denominator four) and every cited requirement heading, scenario heading and
THEN limb is exact at the line cited.

**Its collision verdict, in one line:** both predicates were recomputed from
scratch over the ten sibling worktrees at the heads the packet records, and
**every one of the twenty cells re-derives exactly**, as does every "The B
files" list, "7 of 10 name `routes.ts`", "`model.ts` in 6", "M8 is the
largest overlap at 9 of 16" and the four M11-only files — with the note that
`polaris.ts` is also 6, a figure the evidence record carries and the prose
does not mention; the only defect in the section is F5.

**Every exception was re-derived against source before being applied; none
was applied on the review's say-so.** Twelve of the thirteen confirmed
exactly. **F4 carries a defect of its own, corrected rather than copied:** it
publishes 38 occurrences in 14 files against a stated denominator of 1,216
tracked files at `a9f671e`, but 38/14 is the figure over the **1,218** files
tracked at `2c62d0b`, which include this packet and its own evidence record —
7 of those 38 occurrences, in those 2 files. At the `a9f671e` baseline the
packet measures, the sweep gives **31** occurrences in **12** files. The
defect F4 reports is real and is applied in full, with the corrected figure.
Superseded wording is marked in place and dated throughout, never deleted.

One note on the raw's own citations: several of its `:NNN` references into
this packet do not resolve at `2c62d0b` — `:337` is line 336, `:355` is 353,
`:31` is 33, `:817-819` is 799–800, `:29` is 808 and `:566` is 574 — while
others (`:396-403`, `:35`, `:27`) are exact. Each finding was located by its
quoted content, not by its line number, and every quotation the raw reproduces
was found where it says [Observed]. The raw also records **two notes on its
own review prompt**: that the prompt said "six questions" where this packet
asks five, and that the prompt's "in particular" list named measurements
belonging to M10 and not to this packet, which the reviewer swept for and
found at zero occurrences before reviewing the thirteen measurements this
packet actually makes.

**Where review 1 records an [Unknown].** It records none of its own against
any finding. The only [Unknown]s it records are this packet's four, which it
labels honest, and it singles one out as correctly scoped: whether any
`docs/evidence/*.json` digest table binds the bytes slices 2 and 3 would edit
is a sweep this packet did not run and hands to the implementing bead under
verification rule 10. That remains [Unknown] and is unchanged by this pass.

| Finding | Severity | Disposition |
|---|---|---|
| F1 the stderr/stdout split is 7/3, not 6/4 | non-blocking | **CONFIRMED.** Swept `apps/three-surface-poc/src/main.ts` whole with Python `re` over its 253 `wc -l` lines: 10 sites, stderr at 58, 65, 89, 207, 239, 241, 249 (**7**) and stdout at 56, 211, 229 (**3**), exactly the split the packet's own table lists. Applied at the census summary, at the derived "four of the **seven**" sentence, in the funnel summary's dossier line and in the record's `M7_failure_detail_census` by same-line edit with a dated sibling note; superseded figures marked in place |
| F2 the published lifecycle predicate does not produce its figure, and the predicate that does drops the one existing restart test | non-blocking | **CONFIRMED**, both limbs, both predicates run this session with Python `re` over the 558 in-scope files of the 1,216 tracked at `a9f671e` (`git ls-tree -r -z --name-only a9f671e` through the packet's own in-scope filter): the published substring predicate gives **29**, the word-bounded one **22**, and the difference is exactly the seven files the raw names — the fifth review record it could not name is `docs/reviews/R-POC-CYCLE-3-REVIEW.md` (line 347). All 29 were read; **0** is an operator lifecycle instruction, so the conclusion survives on the wider denominator. Both predicates are now published with their literal alternations and case folding, and the 29 are partitioned by class. `packages/cap1-daemon/src/server.test.ts` line 159's RT3 describe block and line 160's test are cited in slice 4's oracle paragraph beside the existing `packages/cap1-system/src/degradation.system.test.ts` cite |
| F3 "the only three occurrences of the string `log`" is false as a substring claim | non-blocking | **CONFIRMED.** Over the PWB specification in full: `log` case-insensitively as a substring matches **43** lines; `\blogs?\b` matches **3**, at 176, 407 and 665. Q2's bracket now names the word predicate, keeps the three lines, states the substring figure and marks the superseded wording |
| F4 `maxOutputBytes` occurs far more than twice, and the packet's own point is strengthened | non-blocking | **CONFIRMED in substance, with the finding's own figure corrected.** At `a9f671e`, over all 1,216 tracked files: **31** occurrences in **12** files — 11 in `packages/polaris-generation-core/src/pipeline.ts`, 2 in its test, 1 in `openspec/changes/polaris-manifesto-generation/INTERFACES.md` and 2 at `apps/three-surface-poc/src/polaris-generation/pipeline-demo.ts` lines 64 and 71, which are the only two inside the three POC source trees. The raw's 38/14 is the figure at `2c62d0b`. Applied with the whole-repository count, its denominator and the POC-tree count stated separately, and the collision warning strengthened: the name is held by an adopted generator interface. Mirrored in the record under a dated key |
| F5 P-72 and P-77 are not on the register at the packet's own baseline | non-blocking | **CONFIRMED.** At `a9f671e`, `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` carries **26** rows under the predicate `^| P-` — 21 open plus 5 acceptance-act — its highest allocated number anywhere in the file is **P-67**, and the predicate `P-7[0-9]` returns **0** hits. Q1, the improvement-cycle paragraph and the funnel summary's sibling list now describe each row as a branch-only proposal with its PR number, labelled [Observed]. The sequencing conclusion is unchanged: M5's Q1 is still the prior question either way |
| F6 two clauses are attributed to PWB-REQ-006 that belong to PWB-REQ-003 and PWB-REQ-011 | non-blocking | **CONFIRMED.** Requirement headings read at source: 160 (PWB-REQ-003), 202 (-005), 340 (-006), 439 (-007), 632 (-011), 679 (-012). Line 176 is PWB-REQ-003's Oracle bullet, 407 is PWB-REQ-006's "Active repository content remains inert" scenario and 665 is inside PWB-REQ-011's scenario; PWB-REQ-006's own Oracle sits at 394–396 and reads "injected Git/read/render spies, context-independent secret scans, complete sink-byte scans, a separately accumulated resource ledger and exact final encoded-byte counts decide". Gate 2 now says "three times" with each attributed correctly, Gate 4's slice 1 attributes the sentinel-scan oracle to PWB-REQ-003 and cites 394–396 for the sink-byte scan, and the record's dossier-correction entry carries a dated sibling note. Nothing downstream moves |
| F7 the continuation act's escalation paragraph is cited at the wrong lines | non-blocking | **CONFIRMED.** Read at source: the sentence begins on line **150** and ends on line **156**. Q4's citation is now "lines 150–156"; the two narrower cites, line 151 and lines 154–155, are exact and unchanged. The record's `acts.continuation` block already carried 150–156 and needed no repair |
| F8 three quoted spans end before the span cited, with no ellipsis | editorial | **CONFIRMED**, all three, each source opened first. PWB-REQ-021's quoted words end mid-line **977** (978 continues "a structurally lawful run can be not ready…"), so the span is narrowed to 975–977 and the tail marked; `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`'s end mid-line **61** (which continues ", under the in-force craft policies…" to 63), so the span is narrowed to 59–61 and the tail marked; S10-M3's sentence is "Optionally add a pidfile written at startup under stateDir and a tiny restart script that reads it", so the elision is marked and the source's unbackticked `stateDir` disclosed |
| F9 three published line-count denominators are one higher than `wc -l` | editorial | **CONFIRMED.** `wc -l` this session: PWB specification **1152**, three-surface specification **1008**, PWB `tasks.md` **138**. The packet stated a line-*number* convention and no line-*count* one, so a **line-count convention is now stated once** at the head — every published line count is the `wc -l` figure — and all four published denominators (Q2's bracket, the `health` sentence, the `tasks.md` count and Gate 6 item 3) follow it, with the superseded split-on-newline figures marked in place |
| F10 the three over-width lines are mislocated | editorial | **CONFIRMED.** Re-derived at `2c62d0b`: lines **93** (80 columns), **124** (79) and **602** (85). Line 124 is in Gate 0, which opens at line 102; line 93 is in "Decided in this packet, not put to the owner", which ends at line 100; line 602 is the impact-ledger path in Gate 3. Gate 6 item 10 now names the three by line, column and section, re-derived **last** over the final bytes of this pass, since every edit above moved them |
| F11 "undercounts the table by two" rests on an unstated reading, and S10-F1's words are not in the file called the dossier | editorial | **CONFIRMED.** `grep -F` of S10-F1's sentence over all three pursuit files: 1 hit in `docs/pursuits/2026-09-13-vision-pursuit-data.json`, 1 in `docs/pursuits/2026-09-13-vision-pursuit-harvest.json`, **0** in `docs/pursuits/2026-09-13-vision-pursuit.md`, which Gate 0 names as the dossier. The packet now cites the harvest file with its jq path and publishes both readings: literally the sentence names 7 paths plus 7 mirrors = 14, an undercount of **three** (the two POST materialize routes and the `/butlers-syzygy/` trailing-slash mirror of `/`); read as `pocRoutes`' 15 GET routes, which is the reading the figure uses, an undercount of **two** |
| F12 `readinessPopulation` is cited at the wrong lines | editorial | **CONFIRMED.** In `packages/three-surface-poc-core/src/model.ts` the signature is at line **211** and the closing brace at **220**, its doc comment ending at 210. Corrected in the slice 3 design and in the record under a dated key; Q3's separate cite of 217–219 is inside the function and is unchanged |
| F13 Q1's heading asks something the body then declines to ask | editorial | **CONFIRMED.** The second limb is removed from Q1's heading and the superseded heading is quoted and dated in the body's "the prior question is not this packet's" sentence, which already carried the disposition. The Q-table row's question text and the record's `owner_questions` Q1 entry carry the same note under a dated sibling key, the original value unedited. Q1's recommendation, its two lawful arms and its default if unanswered are unchanged |

**No recommended answer changed.** Confirmed against the raw's own Q1–Q5
table, whose "Recommendation follows from the evidence?" column answers
**Yes** for all five, and against the thirteen findings one by one: none
moves an arm, a recommendation or a default. **Q1** keeps
`machine-credentialed` for the machine form and the human form on the
existing `human-open` pages, keeps its second `human-open` arm, and keeps its
default that slice 2's machine route does not ship — F13 moved a limb out of
its heading and F5 relabelled P-72 as a branch-only proposal, and neither
touches the answer. **Q3** keeps "an implementation of two quoted sentences,
not an amendment", keeps its CC-REV-2 second arm and keeps its default that
slice 3 does not ship; F6 corrected which requirement owns a log-sink
sentence and left the readiness argument, which rests on PWB-REQ-006 lines
378 and 384 and PWB-REQ-021 lines 964–968, untouched. **Q4** keeps "do not
mint a new limit", keeps the minting arm as a named escalation trigger rather
than as unlawful, and keeps its default; F7 moved the citation span of the
escalation sentence it quotes and F4 strengthened its collision warning
without changing either arm. Q2 and Q5 are untouched by any finding except
F3's predicate correction inside Q2's bracket [Observed, both sides read this
session].

**Registered as P-78.** The five questions are registered in
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` on branch
`agent/syzygy-dov.11`, as the row the first draft said would land with review
1. P-68 through P-77 each live only on their own branch and none of them is
on the register at `a9f671e` [Observed, counted this session: 26 rows under
`^| P-`, highest allocated number P-67, `P-7[0-9]` 0 hits. All ten sibling
registers were recounted at their own heads and each carries 27 rows].

By verification rule 10, review 1 binds the bytes it names — the two digests
in the table above, at commit `2c62d0b` — and not these. Every edit in this
section and above was made after it, so **the thirteen exception repairs are
uncovered until a second independent fresh-context review confirms them**;
that raw will be a second `-RAW.md` file, never an overwrite of the retained
one. Subject to that, and on review 1's confirmation of the `2c62d0b` bytes —
CONFIRM WITH EXCEPTIONS, no blocking finding, no recommended answer moved,
all five questions found to be genuine hard gates with Q4 partly, and no
lawful arm called unlawful — **this packet stands at the owner gate**: P-78
is ready to be ruled.

Over-width lines after these edits, under the predicate "lines outside fenced
code blocks whose first non-space character is not a pipe, longer than 78
columns", denominator every line of this file: **8** [Observed,
measured last of all in this pass, after every edit including this section,
and iterated to a fixed point because this file states the figure. The
narrower Gate 6 item 10 population — the same lines, excluding headings and
block quotes as well — is **3**, unchanged].

## Funnel summary

```
## Feature Request: M11 - Operability: a status surface, structured non-2xx logging, and a breach that reaches readiness
Size: small (slices 1, 4) / medium (slices 2, 3)
Baseline: Syzygy a9f671e; the dossier audited at f4589e2 and every one of its twelve line citations is re-located above (10 exact, 2 narrowed)
- G1 Motif: a daemon that cannot say it failed renders a false green to the one reader who could fix it - 17 routes and 0 of them status/health; 0 logging calls in any request-handling path over 81 non-test source files in three trees; the retained capture's daemon.err is 0 bytes after 7 requests of which 2 were 503s; PWB-REQ-006 says "Every breach SHALL make PWB-REQ-021 readiness false" and a response-ceiling breach reaches that arm through no path that exists [Observed, every figure measured this session with predicate and denominator stated]
- G2 Doctrine: VIS-2 directly for slice 3 (readiness is a project claim) and by construction for slices 1-2 (stated as a construction, not quoted); VIS-1's ordering ranking slice 3 above slices 1-2 above slice 4; SEC-1 for the status route's client class (Q1); SEC-5 plus PWB-REQ-006's two log-sink sentences for slice 1's new sink; SEC-2/3/4 swept and not engaged; RFC5-3's exhaustive two client classes quoted at its defined clause
- G3 Topology: apps/three-surface-poc/src + packages/cap1-daemon/src + packages/three-surface-poc-core/src + docs/ + scripts/ + package.json; no boundary crossed; no governed artifact touched; 0 of the 14 files in any act manifest over 538 governance files and 24 manifests; no M11 slice duplicates an unchecked PWB task (35 boxes, 32 checked, the 3 open ones being 4.6, 5.2 and 5.3)
- G4 Design: one closed-vocabulary stderr line per non-2xx outcome built from the matched route, never the requested path; one status fact builder feeding both channels with two identified instants and no derived age; a per-process served-side breach record feeding the existing ninth readiness arm, NOT an eleventh arm and NOT the frozen evaluation ledger; a restart section and script with no pidfile
- G5 Spec: no delta needed for the readiness widening on the recommended arm - PWB-REQ-006 line 378 puts the response ceilings inside PWB-REQ-006 and line 384 says every breach makes readiness false, and PWB-REQ-021's ninth arm is that clause - but PWB-REQ-006's own oracle line separates ledger from byte count, which is Q3. RFC2-26 run over all four slice rows (denominator 4): slice 3 maps to PWB-REQ-006 scenario "Resource breach is bounded and explicit" whose WHEN names the final-output ceiling; slice 2's human line maps to POC-REQ-060 and POC-REQ-032; slice 2's machine form's parity scenario is a partial match and holds behind P-72; slices 1 and 4 enumerate no RFC-0002 consequence
- G6 Bar: computed route enumeration rather than transcription; three independent methods for the load-bearing zero; every absence claim with its denominator; rule-6 mutants per slice and per branch; a closed ten-entry list checked before a slice proposed to extend it; no act-bound byte proposed for edit; review 1 read these two files at 2c62d0b and returned CONFIRM WITH EXCEPTIONS (0 blocking, 7 non-blocking, 6 editorial, F1-F13), retained verbatim at docs/reviews/R-POLARIS-M11-OPERABILITY-FUNNEL-RAW.md; all thirteen exceptions were re-derived against source before being applied, and by verification rule 10 the thirteen repairs are uncovered until a second review confirms them [superseded wording, 2026-09-15: "NO independent review yet - this is a first draft"]
Acts: slices 1, 3 and 4 ride THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md lines 55-56 (the recorded-finding limb) inside PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md lines 59-63's implementation plane, continued by PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md; slice 2's machine route additionally holds behind P-72; Q3's second arm and Q4's minting arm each cross a named escalation trigger of the continuation act and need CC-REV-2 plus a new act
Open questions: Q1-Q5 above, registered as P-78 in PENDING-OWNER-DECISIONS.md on branch agent/syzygy-dov.11, 2026-09-15 with review 1 [superseded wording: "NOT yet registered in PENDING-OWNER-DECISIONS.md - this packet writes two files and no register row, by instruction, and the row lands with review 1"]; the sibling rows are proposals that each live only on their own branch and none of them is on the register at a9f671e, whose highest allocated number is P-67 - P-67 (M1 lane A, ruled 2026-09-13 and moved to DECISION-HISTORY.md), P-68 (M1 lane B, PR #35), P-69 (M2, PR #36), P-70 (M3, PR #37), P-71 (M4, PR #38), P-72 (M5, PR #39), P-73 (M6, PR #40), P-76 (M7, PR #42), P-74 (M8, PR #43), P-75 (M9, PR #41), P-77 (M10, PR #44) [Observed, counted this session; superseded wording: "the siblings' rows are P-67/P-68 M1, ... P-77 M10", which did not say the rows are branch-only]
Dossier corrections: the prerequisite's "owner act for the registry resourceLimits change" does not bind the recommended arm, because both response ceilings are ALREADY declared in the registry and typed into PwbResourceLimits and ResourceLimitBreach.limit already admits them - the gap is a recording site, not a schema; P0-CEILING is superseded on main by the M1 lane A trim (612,665 bytes of tailnet headroom); S10-F1's route enumeration undercounts the computed table by two read against pocRoutes' 15 GET routes and by three read literally as 14 paths (17 routes in all); S10-F3 is exact at line 207 but four of the seven stderr sites drop an available cause, not one [both corrected 2026-09-15 per review 1, F11 and F1; superseded wording: "undercounts by two (17 routes, not 15)" and "four of six stderr sites"]; boundedResponse is at routes.ts 137-142 at this baseline, not 99-151
Sign-off: pending - the owner's
Recommended handoff: land slice 1 now (no gate, no ceiling cost); then slice 3 once Q3 is ruled, because it is the only rank-1 change here; then slice 4; slice 2's human line after Q5 and lane B, its machine form after P-72, Q1 and M10
```

## Recommended handoff

**Land slice 1 first, whatever else happens.** It needs no gate, spends no
ceiling headroom, collides with no sibling's Gate 3 table except through
`server.ts`, which only M10 names, and it is the difference between an
operability incident that is invisible and one that has a line. Q2 rules only
how much the breach line carries; on the default arm it carries the status,
the method, the route and the limit identity, which is already enough for the
class of failure the dossier found.

**Then slice 3, if Q3 is answered as recommended.** It is the only rank-1
change in M11: it makes a readiness claim the specification already requires
reachable by the mechanism the specification already names. The bead must
land it as a feed into the existing ninth arm — `READINESS_ARMS` is closed at
ten and one per clause — and must not touch the PWB-REQ-022 evaluator or the
observation digest. It also closes the same blindness in
`apps/three-surface-poc/src/fresh-checkout-verdict.ts`, whose one limit check
reads the same input-side count, and the bead should add that assertion
rather than assume it follows.

**If Q3 is answered the other way** — that the readiness widening is an
amendment — then slice 3 holds behind a CC-REV-2 delta and a new owner act,
and slices 1, 2 and 4 proceed regardless. That is a coherent outcome and
should be written down as one: the reason it is coherent is PWB-REQ-006's own
oracle sentence, which names "a separately accumulated resource ledger **and**
exact final encoded-byte counts" as two deciders, and an owner may reasonably
read the requirement's ledger as an input-side object by construction. Record
in the bead's close reason, if that arm is taken, that a `/polaris` breach
leaves `/api/poc`'s readiness answer unchanged — so the next person to open
this does not mistake an unchanged `ready` for a run that fit.

**If Q4 is answered as recommended:** no registry change is made, no
escalation trigger is crossed, and the breach record names
`maxHumanResponseBytes` or `maxMachineResponseBytes` — the ceilings the
registry already declares. If the owner prefers a distinct output limit
instead, that arm needs a CC-REV-2 delta over the registry and the
specification together plus a new owner act, and the implementing bead should
not start it until that act exists. The implementation should also avoid the
literal `maxOutputBytes` on either arm: the name is already taken by an
unrelated provider budget in the generator demo.

**If Q5 is answered as recommended:** the status line goes in `pageShell` and
the bead re-measures `/polaris` on both host forms before and after, in the
shape `docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`
records, and records the delta — because lane B is still open over the same
budget and a figure taken today is a figure about today. If the owner takes
the second arm, the line renders on the home page and its own route only, and
the bead records that four of the five human surfaces still answer "what am I
serving" only through a footer that does not name the observer.

**If Q1 is answered as recommended and P-72 clears:** the machine status
route is `machine-credentialed` and its body is the same `PocStatusFacts` the
page renders. If the owner takes the `human-open` arm instead, the bead must
record the SEC-1 reading that makes it lawful — that the origin check is the
explicit mechanism for a body carrying no observed content — because that
reading is the owner's to make and not the implementation's to assume.

**Slice 4 can be done by anyone, at any point, and should not wait.** Three
sentences of true documentation and one script close the only lifecycle gap
in the audit, and the three facts they state are already true; nobody has
written them down.
