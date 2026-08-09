# RD-25 — Active-path truth review (round-2026-08e) — RAW
- Review id: RD-25
- Date: 2026-08-10
- Subject: the default reading and task routes, from README.md outward
- Frozen commit: 395da99
- Reviewer: isolated fresh-context session, Claude family (Fable 5). Same-family review — not the gate's family-diverse formal administration.
- Authoring context: none

---

## 0. Method and materials

Work was performed entirely inside the frozen clone at
`/tmp/claude-1000/-home-tze-GitHub-syzygy/3fa62952-e192-440e-8b1f-5b48212d8da1/scratchpad/clone-08e-v15`.
Nothing was edited; no write command was run; the git log was not read; no
`round-2026-08*` or `reviews/` content was read for narrative — the four such
files opened were opened **only** to verify a route's own claim about them
(banner text and existence), and their findings, verdicts, and narratives
informed no answer here.

Read-only scripts were run because the routed documents themselves instruct a
reader to run them (`PROJECT-STATUS.md` "How to verify this page";
`AGENTS.md` "Validation"; the acceptance record §2 step 2).

---

## 1. Route enumeration — the denominator I walked

This is the population my "clean where not noted" statements are scoped to.
Every entry below was opened at commit `395da99` this session `[Observed]`.

**Tier 0 — the default reading set (6/6 walked, in full):**

1. `README.md`
2. `AGENTS.md`
3. `.syzygy/intent/OVERVIEW.md`
4. `PROJECT-STATUS.md`
5. `.syzygy/governance/doctrine/README.md`
6. `.syzygy/governance/contracts/candidates/TASK-ROUTER.md`

**Tier 1 — destinations Tier 0 routes a reader to for a task (walked in full
unless marked):**

7. `CONTRIBUTING.md`
8. `SECURITY.md`
9. `launch-gate-pre-specifications.md` (header/yaml, §§1–2, §3 sample, §§5–9 in full; §3's 31 questions read in part)
10. `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`
11. `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md`
12. `.syzygy/governance/contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`
13. `.syzygy/governance/contracts/candidates/DEFERRED-WAVE-POSTURE.md`
14. `.syzygy/governance/contracts/candidates/README.md` *(the file a reader lands on from README "Start here" #4, which links the directory)*
15. `.syzygy/governance/contracts/candidates/HOW-TO-AUTHOR-A-SYZYGY-SPEC.md`
16. `.syzygy/governance/contracts/candidates/FIRST-OPENSPEC-SEQUENCE.md`
17. `.syzygy/governance/contracts/candidates/SURFACE-CLAUSE-ROUTING-MATRIX.md` (banner + route table)
18. `.syzygy/governance/contracts/candidates/06-CONTEXT-LOAD-MAP.md` (banner + corpus section)
19. `.syzygy/governance/contracts/candidates/TASK-TO-CONTRACT-INDEX.md` (banner only — to verify the router's supersession claim)
20. `.syzygy/governance/contracts/candidates/policy-candidates/TERM-REGISTRY.md` (banner + tier statement + full T-id census)
21. `.syzygy/governance/decisions/PROCESS-LESSONS.md` (first 60 lines)
22. `.syzygy/governance/policies/craft-and-care/README.md` and `INSTALL-RECORD.md` (heads, act-2 material)
23. `.syzygy/map/topology-candidates/BUNDLE-MANIFEST.md` (full) and `README.md` (head + index)
24. `.syzygy/governance/contracts/candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` (head + §5 item 1) and `…-DRAFT.md` (head + banner sweep)
25. `.syzygy/governance/decisions/launch-gate/README.md` and `TREND-LOG.md`
26. `.syzygy/governance/contracts/candidates/wave-manifests/` — all six manifests (module counts + recomputed act arguments)
27. `.syzygy/governance/contracts/candidates/round-2026-08d/ACCEPTANCE-WAVE-DESIGN.md` (banner only — AGENTS.md routes here)
28. `.syzygy/governance/contracts/candidates/round-2026-08d/OWNER-DECISION-PACKETS.md` (banner only — P-* rows route here)
29. `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md` (RFC9-8(a) clause + module front matter — to verify a routed claim)
30. `.syzygy/governance/doctrine/` directory + all five reading-order targets' existence; `vision.md`/`v1.md` swept for the "README glossary" and *actuator* citations

**Route-existence sweeps (mechanical, this session) `[Observed]`:**

- All 36 path references in `TASK-ROUTER.md`: **0 unresolved**.
- Link/backtick/path references in the 13 highest-traffic routed files
  (README, AGENTS, PROJECT-STATUS, CONTRIBUTING, SECURITY, OVERVIEW, doctrine
  README, TASK-ROUTER, DEFERRED-WAVE-POSTURE, acceptance record,
  PENDING-OWNER-DECISIONS, LAUNCH-GATE-AUTHORITY-DECISION, launch gate):
  every unresolved reference falls into one of four declared classes —
  by-design forward references (`openspec/`, `contracts/rfcs/`,
  `map/topology/`, `contracts/wave-manifests/`, `contracts/history/`,
  `decisions/ACCEPTANCE-ACT-RECORD.md`), the declared git-excluded
  `_bootstrap/` tree, prohibition-list names (`src/`, `apps/`, `packages/`),
  and typographic elision (`…/…`, `WAVE-C1…C2-MANIFEST.txt`) — **except the
  two recorded as findings RD25-08 and RD25-09.**

**Scripts run (read-only) `[Observed]`:**

- `python3 scripts/check_governance.py` → `29 OK, 19 WARN, 0 FAIL (48 checks)`.
  CG-7a/7b/7c/7d/7e all OK; CG-2a: `2 retired phrase(s) declared; 0 presented
  as current`; CG-14 `acceptance install routes valid — 12 paths`; CG-24
  `18 of 25 check families have at least one fixture`.
- `verify_final_prespec.py` → `PASS`, `numbered clauses defined: 341`,
  39 modules — matching the acceptance record §3's quoted figure.
- `build_contract_index.py --check`, `build_dependency_index.py --check`,
  `build_budget_report.py --check`, `build_active_manifest.py --check`,
  `build_task_router.py --check` → all no-drift; router `12 task classes`.
- `context_load.py rfcs/RFC-0002/README.md doctrine:vision.md` → runs as
  documented in `AGENTS.md`.
- Recomputed all six wave-act arguments with `sha256sum`; all six match the
  acceptance record §1 rows byte-for-byte (A `6b98e0c6…`, B `2041ad05…`,
  C1 `a5d3ba1f…`, C2 `acd27bb8…`, D1 `570e6170…`, D2 `ab590e3e…`).
  Module counts per wave: 19 / 11 / 2 / 1 / 5 / 1 = **39**, matching
  `AGENTS.md`'s "19 modules"/"11 modules" and the package's 39.

**Declared limits of this denominator.** I did not read the 39 RFC modules
(one clause verified), the five doctrine files in full (README read in full;
two swept), or any round-record or review content. A "clean" statement below
is scoped to the 30 destinations enumerated above and the sweeps named.

---

## 2. Findings

### Class 1 — Stale claims (routed text the current bytes contradict)

---

**RD25-01 — BLOCKING. `PROJECT-STATUS.md` tells the owner the next step is the
round-08d repair batches gated on P-29/P-30; the current bytes say the
opposite.**

Routed document, `PROJECT-STATUS.md:110–119` (§ "Next lifecycle step"):

> "The round-2026-08d repair batches (P-29/P-30 rulings first for the gated
> waves; scripted manifest regeneration and a fresh confirming review per
> edited wave, per the disposition register's §2 and §7), then the readiness
> recompute and the round's owner-facing offering; then the owner performs
> (or declines) the wave acts."

Current bytes, `.syzygy/governance/contracts/candidates/DEFERRED-WAVE-POSTURE.md:3–9` and `:22–26`:

> "**Current statement, owner-directed (launch-closure pass, 2026-08-10).**
> The launch target is **Capability 1 … whose contract prerequisite is
> **Waves A + B only**. The four waves below are **visibly deferred** …"
> "Also deferred from Capability 1, by the same direction: the **P-29** C2
> reproduction criterion, **P-30** Mission stop/containment form …"

And `FIRST-OPENSPEC-SEQUENCE.md:55`:

> "| Waves C1/C2/D1/D2, P-29, P-30, P-32, D3/D4 | — | **not applicable** —
> deferred per `DEFERRED-WAVE-POSTURE.md`; not on Capability 1's path |"

`[Observed]` The page an owner is sent to by `README.md` ("**exact current
gate state**", line 106), by `AGENTS.md` ("Current status"), by `TASK-ROUTER.md`
("Is this ready for OpenSpec?"), and by the launch gate's own
`CURRENT_STATE` parameter (§8) states a next step that the owner's own
Capability 1 direction retired. An owner acting on it would commission
P-29/P-30 rulings and C/D repairs that the current posture explicitly defers.

*Direction (one line):* regenerate "Next lifecycle step" from the Capability 1
posture — A/B fresh reviews → per-wave offers — and name `DEFERRED-WAVE-POSTURE.md`.

---

**RD25-02 — BLOCKING. `PROJECT-STATUS.md` states "repairs have not begun";
they have, and four routed documents say so.**

Routed document, `PROJECT-STATUS.md:96–98`:

> "All 173 findings are disposed in
> `…/round-2026-08d/reviews/DISPOSITION-REGISTER.md`; **repairs have not
> begun.**"

Contradicting current bytes, four independent routed sites:

- `AGENTS.md:56–58` — "the launch-closure pass (round-2026-08e) **repaired
  Waves A and B** under the owner's Capability 1 direction"
- `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:53–55` — "The
  round-2026-08e repair pass **executes the Wave A and Wave B batches** under
  the owner's Capability 1 launch direction"
- `.syzygy/governance/contracts/candidates/README.md:21–23` — "the Wave A/B
  repair batches **landed at round-2026-08e** and await fresh exact-package
  reviews before the acts may be offered"
- `FIRST-OPENSPEC-SEQUENCE.md:41` — "**blocking** — repairs landed this pass;
  fresh exact-package review then the offer"

Independent byte evidence `[Observed]`: `rfcs/RFC-0009/semantic-geography.md`
now carries the redrafted RFC9-8(a) with its staged-successor parenthetical
(line 798: "module appears in RFC9-8(a)'s staged successor parenthetical, as a
**citation**…"), and `verify_final_prespec.py` reports RFC-0009's oversize
justification as caused by "the owner-ordered RFC9-8(a) amendment, which homes
the portfolio layout registry on RFC3-15/RFC3-16(a)" — i.e. the Wave B repair
is in the bytes, not pending.

`PROJECT-STATUS.md`'s own header does state "where they disagree, the record
wins and this file is stale" — but the header also promises the file "is
regenerated or corrected in the same change whenever a gate fires", and its
`As-of: 2026-08-09` is one pass behind the commit it ships in.

*Direction:* re-date the page to 2026-08-10 and replace the sentence with the
A/B-repaired, review-pending state the acceptance record now carries.

---

**RD25-03 — MAJOR. Three routed documents ask the owner to approve launch-gate
`v1.4`; the instrument is `v1.5` and its owning packet asks for v1.5.**

Current bytes, `launch-gate-pre-specifications.md:7`:

> `effective_version: v1.5 (candidate; v1.3 was the pilot-administered version)`

Owning record, `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md:11`
and `:92`:

> "Approve `launch-gate-pre-specifications.md` **v1.5** …"
> "`APPROVED — launch-gate v1.5 as process policy`"

Stale routed sites `[Observed]` (whole-repo `v1.4` sweep, 5 hits outside
`round-2026-08e/`, 3 of them stale):

- `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md:138` (P-34) —
  "approve `launch-gate-pre-specifications.md` **v1.4** as the owner-approved
  process policy", and its amendment-record cell names only
  `LAUNCH-GATE-v1.4-SEMANTIC-DELTA.md`, omitting the v1.5 delta that exists at
  `round-2026-08e/LAUNCH-GATE-v1.5-SEMANTIC-DELTA.md`.
- `.syzygy/governance/contracts/candidates/FIRST-OPENSPEC-SEQUENCE.md:52` —
  "P-34 launch-gate **v1.4** authority + formal administration READY".
- `.syzygy/governance/contracts/candidates/DEFERRED-WAVE-POSTURE.md:41` —
  "Under the **v1.4** launch scope…", while §8's launch-scope parameters were
  materially re-cut at v1.5 (changelog v1.5: `LAUNCH_TARGET` re-cited,
  `DEFAULT_ROUTE_SET` enumerated, `PILOT_RECURRENCE_CHECK` moved in,
  `governs:` aligned).

Harm: P-34 is a digest-bound approval whose ceremony (packet §Mechanism, steps
1–4) has the owner write a version string into an approval block. The register
is the queue an owner works from.

*Direction:* re-quote v1.5 at all three sites and add the v1.5 delta to P-34's
owning-record cell.

---

### Class 2 — Superseded content presented as current on a default route

---

**RD25-04 — BLOCKING. The candidate-package README names the *superseded*
D3 draft as "The D3 proposal"; that draft carries no supersession banner, and
act 5 has no digest to fail on.**

Routed document (`README.md` "Start here" #4 links
`.syzygy/governance/contracts/candidates/`, whose `README.md` renders),
`.syzygy/governance/contracts/candidates/README.md:49`:

> "| `DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md` | The D3 proposal (act 5,
> optional) |"

That layout table is the file's only D3 row; `DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md`
appears nowhere in it `[Observed]` — a 2-hit `grep -F D3` over the file returns
only line 34 (the acceptance-record row) and line 49.

Current bytes everywhere else name rev1 as the subject:

- `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:31` (act 5) —
  "`DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` (**rev1**, 2026-08-05) … Rev1
  supersedes `…-DRAFT.md`, whose `vision.md` insertion **cannot be applied as
  written** (SD-8)."
- `PROJECT-STATUS.md:36` (gate 8) — "…`DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md`
  (rev1; supersedes the original `…-DRAFT.md`)".
- `PENDING-OWNER-DECISIONS.md:72` (P-5) — same.

And `DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md` carries **no** supersession
notice: a sweep of that file for `supersed|rev1|historical|not current`
returns **0 hits** `[Observed]`; its banner reads only "**Status: DRAFT — not
applied.**"

Why this is BLOCKING rather than MAJOR: act 5 is the one open act with **no
digest argument** (`AGENTS.md` gate table: "none — VIS-4 adoption of the D3
packet, rev1"), so no CG-7 check and no phrase mismatch can catch an owner who
adopts the file the default route named. CG-2a covers retired *acceptance
phrases*, not superseded packets.

*Direction:* point the layout row at `…-D3.md` and banner the `…-DRAFT.md`
as superseded-by-rev1.

---

### Class 3 — Contradictions between routed documents with no stated winner

---

**RD25-05 — MAJOR. The act-5 subject invites adopting a text its own gate says
cannot be applied.**

`DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` (head):

> "This packet is a **minimally revised** replacement for
> `DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md` … which is **left untouched**
> at the owner's gate. **The owner may adopt either version**, amend, or
> decline; act 5 carries no magic phrase."

`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:31`:

> "Rev1 supersedes `…-DRAFT.md`, whose `vision.md` insertion **cannot be
> applied as written** (SD-8)."

The rev1 packet's own §5 item 1 concedes the point in its own words — the
original anchor "applied verbatim leaves a parenthetical stranded between a
semicolon and the clause it precedes … an instruction that cannot be applied
without an unrecorded editorial judgment is a defect in an owner-act artifact."

A general precedence rule exists (`AGENTS.md`: "The live gates are
`…ACCEPTANCE-RECORD.md`"), which is why this is MAJOR and not BLOCKING — but
the two documents state the owner's option set differently, and the one an
owner reads *at* act 5 is the packet.

*Direction:* delete or qualify "may adopt either version" in the rev1 packet.

---

**RD25-06 — MAJOR. `PROJECT-STATUS.md`'s gate table presents Waves C1/C2/D1/D2
as live acts and is silent on the entire launch-scope layer.**

Routed document, `PROJECT-STATUS.md:31–32`:

> "| 4c | Waves C1/C2 … | ⏳ **Candidate — no act performed** | …"
> "| 4d | Waves D1/D2 … | ⏳ **Candidate — no act performed** | …"

Current bytes, `DEFERRED-WAVE-POSTURE.md:70`:

> "**No C/D wave act is offered while this posture stands.**"

Each row's text is literally true; the falsehood is by omission, and the
omission is systematic. Sweep with denominator `[Observed]`: a
case-insensitive `grep -E "launch|capability|defer|08e|P-3[0-9]"` over all 158
lines of `PROJECT-STATUS.md` returns **5 hits, none of them the launch-scope
layer** — the words *Capability 1*, *deferred*, *DEFERRED-WAVE-POSTURE*,
*round-2026-08e*, and the identifiers **P-31 … P-40** do not appear anywhere
in the file. Meanwhile `AGENTS.md:80` names `PROJECT-STATUS.md` co-owner of
the readiness question alongside the launch gate, and the launch gate's §8
binds it as `CURRENT_STATE`.

*Direction:* add a deferral marker to rows 4c/4d and a launch-scope paragraph
routing to `DEFERRED-WAVE-POSTURE.md`.

---

### Class 4 — Dead destinations

---

**RD25-07 — MAJOR. The topology bundle manifest's verification instruction
names a directory that exists in no clone — the exact defect class the
acceptance record records having already corrected once.**

`.syzygy/map/topology-candidates/BUNDLE-MANIFEST.md:25`:

> "Verify anytime with `sha256sum -c` against this block (from `topology/`)."

`[Observed]` `ls .syzygy/map/` returns exactly one entry: `topology-candidates`.
`.syzygy/map/topology/` does not exist at this commit and is created only by
act 3 (acceptance record §2 step 3). A reader or owner following the manifest's
own instruction before act 3 — which is the only time it matters, since the
manifest *is* act 3's argument — cannot run it as written.

This is the same shape the acceptance record §2 step 3 records repairing:

> "**Corrected 2026-08-05:** this step previously named a source path
> `topology/` that exists in no clone and never existed in the tracked
> package; the ceremony was unexecutable as written."

Nothing catches the recurrence: the acceptance record itself states "`CG-14`
still checks install *routes* only", and CG-14 passed this run (12 paths, 0
findings).

*Direction:* change `(from `topology/`)` to `(from `topology-candidates/`,
or from `topology/` after act 3)`.

---

**RD25-08 — MINOR. Topology `README.md` cites a fix report at a path that does
not exist.**

`.syzygy/map/topology-candidates/README.md:16–17`:

> "Review 07 swept the cluster against the current RFC text and repaired the
> drifts it found (`../reviews/07-topology-FIX-REPORT.md`)."

`[Observed]` `.syzygy/map/reviews/` does not exist; `ls .syzygy/map/` shows
only `topology-candidates`. The file is an act-3 bundle member (digest
`a0621a0d…` in `BUNDLE-MANIFEST.md`), so its evidence pointer is inside the
accepted digest set. The claim it supports is a provenance claim, not an
action, hence MINOR.

*Direction:* re-point at the surviving location or mark the report
founder-local, at the next digest regeneration.

---

**RD25-09 — MINOR. `HOW-TO-AUTHOR-A-SYZYGY-SPEC.md` promises a prerequisites
table it does not contain.**

`.syzygy/governance/contracts/candidates/HOW-TO-AUTHOR-A-SYZYGY-SPEC.md:6–8`:

> "**No specification may be authored yet** — **the prerequisites table at the
> end** is the current gate state, and `openspec/` does not exist until the
> owner authorizes it."

`[Observed]` The file has no prerequisites table; it ends at "Hard boundary,
restated from authority" (line 74). The table lives in
`FIRST-OPENSPEC-SEQUENCE.md:39–55`, which this file's §"The first
specification (E2)" does route to correctly.

*Direction:* change "the prerequisites table at the end" to name
`FIRST-OPENSPEC-SEQUENCE.md`'s table.

---

### Class 5 — Routing traps, and clarity findings

---

**RD25-10 — MINOR. `PROCESS-LESSONS.md` describes an `AGENTS.md` that no longer
exists.**

`.syzygy/governance/decisions/PROCESS-LESSONS.md:13–15`:

> "`AGENTS.md` keeps only **the four** compressed **verification rules**; this
> file is their single incident record…"

`AGENTS.md:115`: "**Ten rules**, each paid for by a recorded incident."
`[Observed]` `AGENTS.md` §"Verification rules" enumerates 1–10.

*Direction:* replace "the four" with "the compressed verification rules".

---

**RD25-11 — MINOR. The root `README.md` gives the lifecycle stage a different
name than every other routed document.**

`README.md:7`: "> **Current stage: pre-specification project-shape
normalization.**"
`AGENTS.md:9`: "## Current lifecycle stage: final pre-specification"
`PROJECT-STATUS.md:12`: "**Final pre-specification.**"
`CONTRIBUTING.md:5`: "Syzygy is in **final pre-specification**."

`[Observed]` Four routed documents, two names, no stated rule for which is the
stage's name. The substance is identical, hence MINOR.

*Direction:* use "final pre-specification" in the README banner.

---

**RD25-12 — MINOR. `PENDING-OWNER-DECISIONS.md` P-16 states a term-registry
size the registry contradicts.**

`PENDING-OWNER-DECISIONS.md:112` (P-16): "The term registry (**30 terms,
T-01…T-30**)".
`policy-candidates/TERM-REGISTRY.md:11`: "none of its **31 entries** acquires
force"; `:26`: "must not have to learn **thirty-one** terms".
`[Observed]` A `T-\d\d` census over the registry returns exactly 31 distinct
ids, T-01…T-31.

P-17, two rows below in the same file, discloses T-31's minting, so a careful
reader reconciles it; hence MINOR.

*Direction:* re-quote "31 terms, T-01…T-31" in P-16, or drop the count.

---

## 3. What I checked and found sound

Recorded so the "clean" half of the denominator is measurable `[Observed]`:

- **The acceptance ceremony's mechanical spine.** All six wave-act arguments
  recomputed by `sha256sum` match acceptance-record §1 exactly; CG-7a–7e all
  OK; the six manifests partition 39 modules (19/11/2/1/5/1) and match
  `AGENTS.md`'s stated counts; `verify_final_prespec.py` PASS at 341 clauses,
  matching §3's quoted figure; all five generator `--check` runs report
  no drift.
- **`TASK-ROUTER.md`** — 12 task classes, all 36 path references resolve,
  `build_task_router.py --check` confirms it is the generator's current
  output. Its two deferred-wave routes carry the explicit `DEFERRED-WAVE ROUTE`
  label that `DEFERRED-WAVE-POSTURE.md` §2 requires, and no other route reaches
  a C/D candidate.
- **Supersession banners on the routes I reached** — `TASK-TO-CONTRACT-INDEX.md`
  ("SUPERSEDED 2026-08-10"), `round-2026-08d/OWNER-DECISION-PACKETS.md`
  ("Partially superseded 2026-08-10 … do not act from the versions below"),
  `09-OPEN-SPEC-READINESS-REPORT.md` (declared banner-superseded by
  `FIRST-OPENSPEC-SEQUENCE.md`), `06-CONTEXT-LOAD-MAP.md` (scoped to
  measurement, self-corrects its own stale "32 modules"). CG-2a: 0 retired
  acceptance phrases presented as current.
- **The launch-gate instrument, its result home, and its trend log** are
  mutually consistent: `canonical_result_home` exists, contains exactly the
  README and an empty-by-design `TREND-LOG.md`, both stating the zero-row state
  is correct, and both keeping the pilot record immutable where it sits.
  `scripts/launch_gate_results.py` exists as named.
- **The doctrine "README glossary" trap is closed on the active path.** Three
  unqualified citations survive (`vision.md:16`, `vision.md:39`, `v1.md:98`)
  and *actuator* is used at four doctrine sites without a definition — but
  both are registered open owner decisions (P-25, P-25(c)), and `README.md:93–100`
  pre-empts the misroute in terms ("the one doctrine means when it says
  'README glossary' (seven entries; this file has none)"). The doctrine README
  glossary does hold exactly seven entries, and the `#glossary-read-first`
  anchor resolves. No finding.
- **`OVERVIEW.md`** states no gate state, routes gate state to
  `PROJECT-STATUS.md` three times, and labels every candidate claim as
  candidate in Drawer 2. Its four relative links resolve. No finding — though
  note that its three redirects inherit RD25-01/02/06.
- **`CONTRIBUTING.md`, `SECURITY.md`** — every path reference resolves;
  `.beads/hooks/`, `.github/workflows/governance-docs.yml`,
  `.claude/settings.json`, and the vendored `th-engineering` trees all exist as
  disclosed.

---

## 4. Findings table

| Id | Class | One-line summary |
|---|---|---|
| RD25-01 | BLOCKING | `PROJECT-STATUS.md` "Next lifecycle step" routes the owner to the retired 08d/P-29/P-30 plan the Capability 1 direction superseded |
| RD25-02 | BLOCKING | `PROJECT-STATUS.md` says "repairs have not begun"; four routed documents and the RFC-0009 bytes say the Wave A/B repairs landed |
| RD25-04 | BLOCKING | The candidate-package README names the superseded, unbannered `…-DRAFT.md` as "The D3 proposal", and act 5 has no digest to fail on |
| RD25-03 | MAJOR | Three routed sites ask the owner to approve launch-gate **v1.4**; the instrument and its owning packet are **v1.5** |
| RD25-05 | MAJOR | The D3 rev1 packet says "the owner may adopt either version"; the acceptance record says the other version cannot be applied as written |
| RD25-06 | MAJOR | `PROJECT-STATUS.md`'s gate table shows C1/C2/D1/D2 as live acts and never mentions Capability 1, deferral, 08e, or P-31…P-40 |
| RD25-07 | MAJOR | `BUNDLE-MANIFEST.md`'s verify instruction says "from `topology/`" — a directory in no clone; CG-14 checks install routes only |
| RD25-08 | MINOR | Topology `README.md` cites `../reviews/07-topology-FIX-REPORT.md`; `.syzygy/map/reviews/` does not exist |
| RD25-09 | MINOR | `HOW-TO-AUTHOR-A-SYZYGY-SPEC.md` promises "the prerequisites table at the end"; the file has none |
| RD25-10 | MINOR | `PROCESS-LESSONS.md` says `AGENTS.md` keeps "the four" verification rules; it keeps ten |
| RD25-11 | MINOR | `README.md` names the lifecycle stage differently from `AGENTS.md`, `PROJECT-STATUS.md`, and `CONTRIBUTING.md` |
| RD25-12 | MINOR | P-16 states the term registry holds 30 terms (T-01…T-30); it holds 31 (T-01…T-31) |

Counts: **3 BLOCKING, 4 MAJOR, 5 MINOR** — computed from the table, not asserted.

The single dominant pattern `[Inferred]`: the launch-closure pass moved the
acceptance record, `AGENTS.md`, the candidate-package README, the deferral
posture, and the first-spec sequence to the Capability 1 world, and left
`PROJECT-STATUS.md` — the one page four separate routes call the exact current
state, including the launch gate's own `CURRENT_STATE` parameter — at
`As-of: 2026-08-09`. Findings RD25-01, RD25-02, and RD25-06 are that one
omission read three ways.

VERDICT: REVISE
