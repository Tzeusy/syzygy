# Greenfield-parity audit — 2026-10-21

Audited commit: `dd520e8d` (main, 2026-10-20). Requested by the owner on
2026-10-20; the request and how this session read it are recorded in
`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-SIMPLIFICATION-2026-10-20.md`.
Method: th-engineering greenfield-parity (delta workflow and idempotent
audit), first run. This page is a plan and a measurement, never authority.
The beads it names are the work; `bd show <id>` owns their state.

## 1. Verdict

[Inferred from the measurements in sections 4 and 5.]

- **Product code is near parity in volume; its residue is structural.**
  - TypeScript source is 52.7k lines against an independent lean greenfield
    estimate of 30-47k (provider mode parked).
  - Remove the 9.2k lines of developer tooling compiled into the POC app and
    the 4.8k-line parked provider island, and the product runtime is about
    38k lines, inside the estimate.
  - The excess is shape, not bulk:
    - duplicated concepts: two owner-act validators whose non-human-principal
      rules have drifted; two bounded blob readers; 26 sha256 helpers; six
      epistemic carriers;
    - tooling living in the product package;
    - module-global render state and HTML that the renderer re-parses;
    - a CLI written as an if-chain.
- **Governance tooling is 12-20 times its greenfield size.**
  - It is 94,027 lines in 123 files against a data-driven estimate of
    4.5-7.5k source plus 3.5-6.5k tests.
  - 54% (50.4k lines) re-verifies frozen history.
  - Most of the rest is one patch-package lifecycle and one recorder template
    cloned once per act: 120 exact-duplicate function groups, 331 copies.
- **The artifact estates have no retention rule.**
  - docs/evidence holds 388 files (20.45 MB); 141 are cited by nothing.
  - About 56% of governed lines are spent rounds and history, performed
    packages, or a byte-identical RFC mirror.
  - AGENTS.md has grown back to 738 lines, 74% notes-to-self, and loads
    every session.
- **Three bugs were found and filed first:**
  - the sync-child-process guard is blind to two of seven test projects;
  - code-structure observation parses `git ls-tree` without `-z`, dropping
    or mis-recording quoted paths without an Unknown;
  - the two owner-act validators carry drifted copies of the
    non-human-principal rule, so the same principal is refused for
    different reasons. This is not a live fail-open: both validators then
    require the registered owner. It does weaken each validator's
    defense-in-depth check.

**The prior vision-pursuit runs did not reach these surfaces.** They
improved the product's honesty and the Polaris experience. Nothing in their
scope measured the code against a from-scratch build. So the duplication
and the tooling growth accumulated beside that work, not because of it.

**Rewrite surfaces.** The rewrite rule fired on six of them. On each,
residue outweighs parity, or removing it piece by piece would re-touch the
same files:

| Surface | Finding |
|---|---|
| frozen-history re-verification | GT-2 |
| per-act package builders | GT-5 |
| bespoke recorders | GT-6 |
| `check_governance.py` | GT-7 |
| six mutation frameworks | TB-6 |
| the two blob readers | DC-5 |

Each is filed `complexity:high` with an Opus-class tier noted in the bead.

## 2. Spec statement (step 0)

- **Goal [Observed: README.md, OVERVIEW.md, doctrine v1].** A local,
  specification-driven control plane. Humans define what should be true;
  evidence shows what is true; agents do bounded work to close the gap; the
  gap is always rendered honestly.
- **Hard requirements in force [Observed: openspec/changes/].** Eight
  changes are in scope:
  - CAP1: 42 requirements;
  - the trusted-bootstrap consent overlay: 2;
  - the Three-Surface POC: 26;
  - the PWB project-wide model: 17, 63 scenarios;
  - the generation base: 29, 154 scenarios;
  - the understanding amendment: 7 modified, 2 added;
  - dossier local-agent mode: 4, 54 scenarios;
  - the non-governed narrative profile: 1.

  Doctrine VIS-1…7 and SEC-1…5 and contracts RFC 0001-0009 bind them.
- **Constraints [Observed].**
  - It runs as a single operator's local daemon and CLI, on Node >=22.15.
  - It has no database; state lives in git files and JSON records.
  - Python governance tooling is stdlib-only. That constraint is unwritten;
    GT-1 writes it down.
  - It observes exactly one consented repository body, behind the P1
    authority gate.
- **Verified external consumers [Observed].** None. The HTTP endpoints and
  the CLI are consumed by the operator. The observed Butlers repository is a
  subject, not a consumer. No compatibility path applies to any finding;
  same-repo callers never count.

## 3. Greenfield sketch (recorded before implementation was read)

[Inferred.] A fresh-context agent wrote it from doctrine, the eight specs
and RFC clause leads, opening no file under `apps/`, `packages/` or
`scripts/`. It is reproduced from that agent's report, lightly abridged.
Ranges are about ±40%.

**Modules.**

- `kernel`:
  - a single Claim/EpistemicRecord type, created only by constructors that
    enforce the invariants (Unknown needs a reason, Observed needs a
    resolvable evidence link, an aggregate carries no label);
  - evaluation identity, the evidence record, closed vocabularies,
    aggregate-composition disclosure, canonical JSON and digest.
- `authority`: one owner-act predicate and one act-ledger interface,
  covering consent, classification policy, registry, currency bound,
  dismissal, walkthrough judgment and authorship.
- `git-read`: an exact-object reader with path containment, plus one
  resource ledger.
- `screen`: the classifier, secret detectors, the active-content scan, the
  inert-code mask and hash-not-body exclusions.
- `extract`: the profile-grammar engine, source discovery, and the coverage
  and conflict engine.
- `declared`: project.yaml and spec reading.
- `observers`: code structure, Dolt and Beads, README links.
- `model`: one project model that emits the machine answer, with parity
  markers generated at render time.
- `ui`: tokens, an encoding table that drives legends, components,
  accessibility helpers, the copy linter.
- `surfaces`: CAP1 pages, Polaris, Trajectory, Orrery.
- `server`: auth, ceilings, mounts, routes.
- `narrative-site`: the shared renderer.
- `dossier`: the operator-agent CLI.
- `generator`: parked.
- `cli`: one binary.
- `verify`: parity sweeps, the mutation harness and the browser harness.
- `govtools`: act descriptors as data, one recorder, one checker framework.

**Size [Inferred], thousands of lines.**

| Module | Source | Tests |
|---|---|---|
| kernel | 2.0-3.0 | 2.5-4.0 |
| authority (195- and 86-case matrices) | 1.0-1.6 | 2.5-4.0 |
| git-read plus resource ledger | 0.8-1.3 | 1.2-2.0 |
| screening | 1.0-1.7 | 1.5-2.5 |
| CAP1 domain | 2.2-3.2 | 2.5-4.0 |
| PWB extractor, profile, coverage, conflicts | 3.0-4.5 | 4.0-6.5 |
| observers | 0.9-1.5 | 1.2-2.0 |
| shared model, machine answer, claims, anchors | 2.0-3.0 | 2.5-4.0 |
| server, auth, ceilings, machine views | 1.8-2.8 | 2.5-4.0 |
| UI component layer | 1.5-2.5 | 2.0-3.5 |
| Polaris renderer | 3.5-5.5 | 4.5-7.5 |
| Trajectory | 0.9-1.5 | 1.2-2.0 |
| Orrery | 1.1-1.8 | 1.4-2.4 |
| walkthrough readiness and judgment | 0.7-1.2 | 1.2-2.2 |
| CLI | 0.6-1.0 | 0.5-0.9 |
| verification infrastructure | - | 3.0-5.0 |
| **Core subtotal** | **23-36** | **34-56** |
| narrative-site renderer | 3.0-4.5 | 3.5-5.5 |
| operator-agent dossier mode plus NGP | 4.0-6.5 | 5.0-8.0 |
| provider-mode generator core plus UND (parked) | 7.0-11.0 | 8.5-14.0 |
| effect host, recorder, audit (parked) | 3.0-4.5 | 3.5-6.0 |
| scheduler adapter, work state, joins (parked) | 2.5-4.0 | 3.0-5.0 |

- **Lean product** (provider mode parked): 30-47k source plus 42.5-70k tests.
- **Full product:** 42.5-66.5k source.
- **Governance tooling, data-driven:** 4.5-7.5k source plus 3.5-6.5k tests:
  - manifest and digest library: 0.25-0.4k;
  - one recorder: 0.7-1.1k;
  - a checker framework with 15-25 predicates: 2.0-3.5k;
  - one generic view generator: 0.8-1.4k;
  - launch-gate validator, quotation checker and partition checker:
    0.7-1.1k.

**Duplications a single abstraction removes.** The specs state each of
these concepts several times:

- the epistemic tuple;
- human/machine parity;
- the owner-act and consent gate;
- git read plus screening;
- evaluation determinism;
- "Unknown, never zero";
- walkthrough records;
- anchors;
- the fixed entry;
- the accessibility floor;
- proposals staying unadopted;
- work-item observation.

**Complexity the specs require.** These drivers are inherent, not residue:

- the PWB grammar interpreter (PWB-REQ-002/004);
- three owner acts with 195- and 84+2-case populations (PWB-REQ-005/022,
  CAP1-REQ-011/046);
- the read ledger and ceilings (PWB-REQ-006);
- the full epistemic tuple (PWB-REQ-007, POC-REQ-060);
- anchors and SVG (PWB-REQ-014);
- browser-computed offsets (PWB-REQ-010/016);
- multiplicity-preserving parity (PWB-REQ-020, CAP1-REQ-040-043,
  POC-REQ-020);
- the parked generator's durable dispatch;
- the dossier's pinned-clone and quote-verification rules (REQ-033-035);
- the strict interchange (REQ-019).

## 4. Inventory of the actual (dd520e8d)

[Observed by seven read-only sweeps, each scoped to one surface. Spot
checks re-ran the load-bearing claims, among them the three bugs, the two
regexes and the guard roots, with file:line in this session. Re-derive any
figure before relying on it (verification rule 2).]

| Surface | Source | Tests | Notes |
|---|---:|---:|---|
| apps/three-surface-poc | 16,909 | 20,253 | 7,713 reachable from main.ts; 9,196 not |
| three-surface-poc-core | 12,291 | 12,543 | owner-act validity 2.75k; PWB read pipeline 5.0k; seeded world 4.15k |
| cap1-core / -daemon / -conformance / -system | 3,761 / 2,915 / 0 / 600 | 0 / 3,113 / 6,814 / 1,401 | cap1-core's tests all live in cap1-conformance |
| polaris-dossier, generation core, consent, apps/syzygy, app polaris-generation | 9,781 / 4,425 / 1,277 / 371 / 3,145 | about 19,500 | 28% of declaration lines not reachable from the syzygy CLI |
| Python and mjs governance tooling | 94,027 (123 files) | embedded selftests 19,310 | 18 files over 1,000 lines; inventory in the appendix |
| docs/evidence | 388 files, 382,339 lines | - | 141 with no citer; 192 with no citer outside docs/evidence |
| Governed plane (.syzygy, openspec) | 1,326 files, 280,389 lines | - | rounds and history 86.4k; performed packages 57.1k; RFC mirror 14.5k |
| Cold start (README, AGENTS, PROJECT-STATUS) | 1,521 lines | - | AGENTS.md 738 lines / 6,845 words |

**Suite and CI [Observed, one run at load 28-33 on 12 cores].**

- The suite: 4,679 tests in 228 files, 3:40 wall clock.
  - 65 files spawn processes, run git, start servers or drive Chrome, and
    take 68% of test time.
  - 233 of about 451 emitted `dist/*.js` files are tests.
  - 15 of 22 root scripts force a rebuild first.
- The governance battery: 105 commands, 232 s sequential.
  - 40 `--selftest` commands take 83% of that.
  - 56 historical re-verifier commands take 47%.

## 5. Delta table

59 rows, one per component or per structural trait. Each row cites
the finding (section 6) or the constraint that justifies it.

| # | Actual | Greenfield counterpart | Verdict | Residue class | Finding or constraint |
|---:|---|---|---|---|---|
| 1 | cap1-core domain (3.8k source lines) | CAP1 domain 2.2-3.2k plus kernel share | parity | - | - |
| 2 | cap1-daemon Capability 1 app (about 1.9k) | CAP1 pages and machine routes | parity | - | - |
| 3 | Generic HTTP host inside cap1-daemon (about 1.0k) | server package 1.8-2.8k | residue | layer inflation | DC-8 |
| 4 | cap1-conformance (6.8k test lines) | independent black-box oracle | justified | - | oracle independence (AGENTS.md: expected values are literals) |
| 5 | cap1-system effect observer | external effect oracle | justified | - | CAP1-REQ-061 oracle must be independent |
| 6 | CAP1 unwired planes, test-only parity oracle, orphan modules | none | residue | speculative generality | DC-7 |
| 7 | Two owner-act validators (2.75k), drifted principal rule | one predicate and act ledger 1.0-1.6k | residue | duplicated concept | DC-2, DC-9 |
| 8 | PWB read pipeline (5.0k) | git-read, screening, extract 4.8-7.5k | parity | - | - |
| 9 | Two bounded blob readers; three ls-tree runs; one without -z | one reader, one listing | residue | duplicated concept | DC-1, DC-5 |
| 10 | Prose Unknown reasons; six epistemic carriers | kernel claim constructors | residue | duplicated concept | DC-4 |
| 11 | Helper copies (sha256 x26, deepFreeze x8, two canonicalJson) | kernel digest and canonical JSON | residue | duplicated concept | DC-3 |
| 12 | model.ts with a 347-line buildPocModel | model composing per-surface slices | residue | layer inflation | DC-6 |
| 13 | Walkthrough readiness and judgment (1.2k) | 0.7-1.2k | parity | - | - |
| 14 | POC app runtime closure (7.7k) | server, UI layer, three surfaces 8.8-14.1k | parity | - | - |
| 15 | Polaris module-global render state and HTML rescans | explicit render context and collected outline | residue | layer inflation | PA-2 |
| 16 | No HTML component layer (554 escapeHtml, 3 escapes, 5 decoders) | UI component layer | residue | duplicated concept | PA-3 |
| 17 | Path-prefixed tailnet route duplicates | Host-based mount detection only | residue | speculative generality | PA-4 |
| 18 | POC tooling compiled with the product (9.2k) | verify/tools workspace | residue | tooling sprawl | PA-1 |
| 19 | Top-level main.ts script, over-export, orphans | thin main, narrow surface | residue | interface sprawl | PA-5 |
| 20 | polaris-dossier live path (8.8k) | dossier and NGP 4.0-6.5k plus narrative site 3.0-4.5k | parity | - | - |
| 21 | Parked provider island (about 4.8k) | parked generator core | justified | - | owner direction: parked, not deleted (2026-10-05, 2026-10-15) |
| 22 | Live dossier path wired through provider modules | standalone source, draft and render inputs | residue | layer inflation | PD-1 |
| 23 | Dossier CLI if-chain and four argument parsers | one command table | residue | duplicated concept | PD-2 |
| 24 | Permanently true wait-mode sign-off gate | none | residue | history | PD-3 |
| 25 | Bespoke act-parser families in package-reader | one forms table | residue | duplicated concept | PD-4 |
| 26 | Two schema builders and helper copies | one schema module | residue | duplicated concept | PD-5 |
| 27 | 181-value barrel and mixed-concern files | narrow public surface | residue | interface sprawl | PD-6 |
| 28 | Execution-permitting arm built but switched off | REQ-033 permitting arm under D9 | gap | - | OG-5 |
| 29 | apps/syzygy (0.37k) | CLI 0.6-1.0k | parity | - | - |
| 30 | Two git object readers (cat-file and in-process) | none | justified | - | different trust boundaries; dossier reader is registry-bound |
| 31 | Literal-grammar Markdown parsers | none | justified | - | PWB literal line-based grammar |
| 32 | Orrery inline client script and JSON island | none | justified | - | POC-REQ-020-022, tasks.md 2.3 |
| 33 | TypeScript tests (about 60k) | 42.5-70k | parity | - | - |
| 34 | Unit run mixes process, git, server and Chrome tests | unit, integration and e2e tiers | residue | test bloat | TB-3 |
| 35 | Guard-test root list drifted from the workspace list | derived roots | residue | duplicated concept | TB-1 |
| 36 | Duplicated test helpers | one test kit | residue | test bloat | TB-4 |
| 37 | Wall-clock bounds and incidental byte pins | injected clocks and counts | residue | test bloat | TB-5 |
| 38 | dist as an executable input; tests emitted; --force; aliases | source condition; product-only build | residue | tooling sprawl | TB-2 |
| 39 | Six mutation frameworks (2.6k) | one runner (about 0.4k) | residue | duplicated concept | TB-6 |
| 40 | Live checkers 17.3k (check_governance.py 11.4k) | check framework 2.0-3.5k | residue | layer inflation | GT-7 |
| 41 | Selftests embedded in 98 files (19.3k) | one test suite | residue | test bloat | GT-8 |
| 42 | Historical re-verifiers and unrun history (50.4k) | frozen act ledger | residue | history | GT-2, GT-3 |
| 43 | Per-act package builders (34.1k) | one package engine | residue | duplicated concept | GT-5 |
| 44 | Bespoke recorders (17.7k) beside a generic one (2.4k) | one recorder 0.7-1.1k | residue | duplicated concept | GT-6 |
| 45 | Helper copies across 112 Python files | one core library | residue | duplicated concept | GT-1 |
| 46 | Battery spelled out twice, plus a parity check | one battery list | residue | tooling sprawl | GT-4 |
| 47 | Thirteen view generators (7.0k) | one generic generator 0.8-1.4k | residue | duplicated concept | not filed (see section 8) |
| 48 | Launch-gate validator and renderer (6.8k) | 0.7-1.1k | justified | - | frozen by docs/evidence/launch-gate-v2.5/APPROVAL-MANIFEST.json |
| 49 | Stdlib-only Python tooling | none | justified | - | unwritten constraint; GT-1 writes it down |
| 50 | Ten code files under .syzygy/** | scripts/ | residue | tooling sprawl | OG-3 |
| 51 | Consent gate re-renders the Python record template | structured record fields | residue | duplicated concept | OG-4 |
| 52 | Digest binding, retained raws, act records | none | justified | - | VIS-2, VIS-4, CC-REV-6 |
| 53 | AGENTS.md notes-to-self (550 of 738 lines) | an agent guide under 200 lines | residue | narration | DE-5 |
| 54 | PROJECT-STATUS.md as a ledger | a current-state page | residue | narration | DE-3 |
| 55 | Evidence with no index and no retention rule | indexed evidence, retained by rule | residue | history | DE-1, DE-2 |
| 56 | PENDING-OWNER-DECISIONS.md is 94% history | a register | residue | narration | DE-4 |
| 57 | Spent governed estate (rounds, history, performed packages) | a tag plus an index | residue | history | OG-2 |
| 58 | Installed/candidate RFC mirror (30 identical pairs) | one copy | residue | duplicated concept | OG-2 |
| 59 | Two largest generated reports committed | generated on demand | residue | tooling sprawl | OG-2 |

**Parity share by row:**

- 13.6% parity (8 rows)
- 15.3% justified (9 rows)
- 69.5% residue (41 rows)
- 1.7% gap (1 row)

Residue by class: duplicated concept 16, layer inflation 5, tooling sprawl 5, history 4, test bloat 4, narration 3, speculative generality 2, interface sprawl 2.

These are row counts, not lines. Several residue rows are structural traits
inside components whose volume is at parity, which is the verdict's point.

## 6. Findings and beads

The umbrella epic is `syzygy-bpyt`. Milestone epics:

| Milestone | Epic |
|---|---|
| M1a governance tooling: library, ledger, battery | `syzygy-bpyt.2` |
| M1b governance tooling: engines | `syzygy-bpyt.3` |
| M2 tests, build and CI | `syzygy-bpyt.4` |
| M3 POC app | `syzygy-bpyt.5` |
| M4a domain core: correctness and primitives | `syzygy-bpyt.6` |
| M4b domain core: model, CAP1, host, evaluators | `syzygy-bpyt.7` |
| M5 Polaris dossier and generation | `syzygy-bpyt.8` |
| M6 docs and evidence | `syzygy-bpyt.9` |
| M7 owner-gated simplifications | `syzygy-bpyt.1` |

The convergence bead is `syzygy-bpyt.10`. Each epic ends in a gen-1
reconciliation bead whose acceptance includes re-running this delta on its
surfaces.

Every bead carries several fixed parts:

- an `Audit-key: greenfield:<class>:<path>` line;
- a model-tier line (low, medium, high or epic);
- a cold-start paragraph pointing here;
- the guardrails that apply: byte identity, frozen scripts, WIP one,
  citer sweeps before moves, no Butlers body reads, and rule-6 evidence.

| Finding | Summary | Residue class | Exposure | Complexity | Bead |
|---|---|---|---|---|---|
| GT-1 | Shared stdlib library for the governance tooling | duplicated concept | internal | medium | `syzygy-bpyt.2.1` |
| GT-2 | Frozen act ledger replaces historical re-verifier battery lines | history | internal | high | `syzygy-bpyt.2.2` |
| GT-3 | Retire uncited historical, declined and one-off tooling | tooling sprawl | internal | medium | `syzygy-bpyt.2.3` |
| GT-4 | Battery defined once | tooling sprawl | internal | medium | `syzygy-bpyt.2.4` |
| GT-5 | One package engine for candidate builders | duplicated concept | internal | high | `syzygy-bpyt.3.1` |
| GT-6 | One descriptor-driven recorder | duplicated concept | internal | high | `syzygy-bpyt.3.2` |
| GT-7 | check_governance.py as a check registry | layer inflation | internal | high | `syzygy-bpyt.3.3` |
| GT-8 | Selftests into one unittest suite | test bloat | internal | medium | `syzygy-bpyt.3.4` |
| TB-1 | Bug: guard test skips two packages | duplicated concept | internal | low | `syzygy-bpyt.4.1` |
| TB-2 | Run tooling from source; product-only build | tooling sprawl | internal | high | `syzygy-bpyt.4.2` |
| TB-3 | Unit, integration and e2e tiers; check commands | test bloat | internal | medium | `syzygy-bpyt.4.3` |
| TB-4 | One test kit | test bloat | internal | medium | `syzygy-bpyt.4.4` |
| TB-5 | Wall-clock and byte pins | test bloat | internal | low | `syzygy-bpyt.4.5` |
| TB-6 | One mutation runner and evidence schema | duplicated concept | internal | high | `syzygy-bpyt.4.6` |
| PA-1 | POC tooling into a tools workspace | tooling sprawl | internal | high | `syzygy-bpyt.5.1` |
| PA-2 | Polaris render context and collected outline | layer inflation | internal | high | `syzygy-bpyt.5.2` |
| PA-3 | HTML component layer | duplicated concept | internal | high | `syzygy-bpyt.5.3` |
| PA-4 | Tailnet path-prefixed route duplicates | speculative generality | exported (machine links) | medium | `syzygy-bpyt.5.4` |
| PA-5 | POC hygiene: main, exports, orphans | interface sprawl | internal | low | `syzygy-bpyt.5.5` |
| DC-1 | Bug: code-structure ls-tree without -z | duplicated concept | internal | low | `syzygy-bpyt.6.1` |
| DC-2 | Bug: drifted non-human-principal rules | duplicated concept | internal (consent gate) | medium | `syzygy-bpyt.6.2` |
| DC-3 | One support module | duplicated concept | internal | medium | `syzygy-bpyt.6.3` |
| DC-4 | Typed Unknown reasons | duplicated concept | internal | high | `syzygy-bpyt.6.4` |
| DC-5 | One bounded blob reader and one tree listing | duplicated concept | internal | high | `syzygy-bpyt.6.5` |
| DC-6 | Model slice builders; walkthrough as a slice | layer inflation | internal | medium | `syzygy-bpyt.7.1` |
| DC-7 | CAP1 unwired planes and orphans; conformance fixtures | speculative generality | internal | medium | `syzygy-bpyt.7.2` |
| DC-8 | Generic HTTP host package | layer inflation | internal | medium | `syzygy-bpyt.7.3` |
| DC-9 | Owner-act gates as check tables | test bloat | internal (consent gate) | high | `syzygy-bpyt.7.4` |
| PD-1 | Decouple the live path from the parked island | layer inflation | internal | medium | `syzygy-bpyt.8.1` |
| PD-2 | CLI command table | duplicated concept | exported (CLI) | medium | `syzygy-bpyt.8.2` |
| PD-3 | Permanently true wait-mode gate | history | internal | low | `syzygy-bpyt.8.3` |
| PD-4 | package-reader forms table | duplicated concept | internal (consent gate) | high | `syzygy-bpyt.8.4` |
| PD-5 | One schema builder and util | duplicated concept | internal | medium | `syzygy-bpyt.8.5` |
| PD-6 | Narrow barrel; split mixed-concern files | interface sprawl | exported (package) | medium | `syzygy-bpyt.8.6` |
| DE-1 | Generated evidence index | narration | internal | medium | `syzygy-bpyt.9.1` |
| DE-2 | Evidence retention (owner-gated) | history | internal | medium | `syzygy-bpyt.9.2` |
| DE-3 | PROJECT-STATUS.md as current state | narration | internal | medium | `syzygy-bpyt.9.3` |
| DE-4 | Register split from history | narration | internal | medium | `syzygy-bpyt.9.4` |
| DE-5 | AGENTS.md regression (reopened syzygy-0kq) | narration | internal | medium | `syzygy-0kq (reopened)` |
| OG-1 | One owner packet, nine questions | - | - | medium | `syzygy-bpyt.1.1` |
| OG-2 | Retire spent estate, RFC mirror, two reports | history | internal | high | `syzygy-bpyt.1.3` |
| OG-3 | Code out of .syzygy/** | tooling sprawl | internal | medium | `syzygy-bpyt.1.4` |
| OG-4 | Structured act-record fields | duplicated concept | internal (consent gate) | high | `syzygy-bpyt.1.5` |
| OG-5 | Execution arm and provider island answers | speculative generality | internal | medium | `syzygy-bpyt.1.6` |

**Progressive order.** The bead dependencies encode it:

1. Bugs and leaves: TB-1, DC-1, DC-2, GT-1, PA-4, PA-5, PD-3, TB-5, DE-1,
   DE-4, DE-5, OG-1.
2. Boundary reshapes: GT-2, GT-3, GT-4, TB-2, TB-3, TB-4, DC-3, DC-7, DC-8,
   PD-1, PD-2, PD-4, PD-5, PD-6, DE-3.
3. Surface rewrites:
   - GT-5, GT-6, GT-7 and GT-8;
   - TB-6, PA-1, PA-2 and PA-3;
   - DC-4, DC-5, DC-6 and DC-9.
4. Owner-gated work, after the packet is answered:
   - OG-2, OG-3, OG-4 and OG-5;
   - DE-2.

**Cross-epic edges:**

- PA-1 waits for TB-2 and TB-6.
- PA-2 waits for `syzygy-dov.16.4`, and PA-3 for `syzygy-dov.16.2`.
- DC-9 waits for TB-6.
- DE-3 waits for GT-4.
- OG-3 waits for GT-1; OG-4 for GT-6; OG-5 for PD-1.

## 7. Reconciliation with existing beads

The ledger was checked first: no prior greenfield audit and no audit-keyed
bead existed. The dedupe sweep of 631 beads was re-run just before
creation and found 0 matches.

| Existing bead | State | Note |
|---|---|---|
| `syzygy-qkea.17` shared screening | attached (finding C2 of the generation sweep) | widened: `parseGithubUrl`, `resolvePathIntent`, `gitBlobObjectId` copies |
| `syzygy-qkea.19` renderer package | attached (finding C3 of the generation sweep) | widened to the whole app `polaris-generation/` tree, `isolated-git.ts` and the tokens dependency |
| `syzygy-0kq` condense AGENTS.md | reopened as a regression (DE-5) | 6,845 words against its 900-1,200 charter; reparented under `syzygy-bpyt.9` |
| `syzygy-dov.16.4` mechanical renderer split | coordination note | still accurate; its blocker `syzygy-dov.13.2` waited for lane B, which closed as declined on 2026-10-02 |
| `syzygy-dov.16.2` branded Html type | coordination note | PA-3 builds on it |
| `syzygy-r77h` docs README count | coordination note | DE-1 edits the same file |
| `syzygy-dov.9.2` epistemic unification question | coordination note | DC-4 answers it for internal typing only |
| `syzygy-u05.11` drift sweep and mutation gate | coordination note | TB-6 supplies the runner |

States, in the idempotent-audit sense:

- 43 findings filed as new beads;
- 2 attached (C2, C3);
- 1 reopened (DE-5);
- 0 superseded;
- 0 closed.

## 8. Not filed, with the reason

- **Thirteen view generators (7.0k lines) against one generic generator.**
  Their outputs are bound or CI-compared views. GT-1 (library) and OG-3
  (moving eight of them) change their surroundings first. Re-measure at
  convergence.
- **Compacting act-bound evidence matrices** (12 files, 85.7k lines, e.g.
  the 27.5k-line non7 bridge). Only a new owner act could do it, and the
  saving does not justify one now.
- **Compacting the sixteen funnel packets** (23.6k lines). The bound impact
  ledgers and retained raws cite them; compaction is owner-led, packet by
  packet, after each ruling.
- **Converging the four dossier session-start modes** (about 2.1k lines).
  The 2026-10-14 one-command direction keeps the older modes exactly; this
  belongs to the one-command change (`syzygy-fl2g`).
- **Renaming `cap1-*` packages.** It would break citations in bound files.
  DC-8 splits without renaming.
- **A browser automation library in place of `cdp-browser.ts`.** This is a
  CC-DEP-1 promotion decision. PA-1 moves the file and leaves the choice
  open.
- **The 47 act tags, digest binding, retained raws and the 195-case
  oracle.** Justified (section 5); they are what makes the honesty claim
  checkable.

## 9. Method and limits

- **Sketch first.** The sketch was recorded by an agent that read no
  implementation. The surface sweeps that followed formed their own
  post-hoc sketches; those are labelled [Inferred] where used.
- **Sweeps.** Seven read-only Sonnet sweeps per the owner's directive on
  fan-out models. The lead session spot-verified the load-bearing claims at
  file:line: the guard roots, the `ls-tree` call, both regexes, the
  `PERMITTING_ARM_ENABLED` flag, the tailnet comment and the battery shape.
- **Name-based counts are bounds.** Export and reachability counts
  (unused exports, CLI-unreachable declarations) are name- and regex-based:
  lower bounds for dead code in one case and upper bounds in the other.
  Each bead says to re-derive.
- **No Butlers or other observed-repository body was read.** Figures about
  Butlers come from committed evidence records.
- **Not retained.** The sweep scripts lived in the session scratchpad. The
  tooling inventory is reproduced below because beads GT-1 to GT-3 use its
  lifecycle classes.

## 10. Convergence record

```
Audited: dd520e8d on 2026-10-21
Findings: 46 - new 43 . attached 2 . superseded 0 . reopened 1 . closed 0
Parity share: 13.6% parity (8 rows) . 15.3% justified (9 rows) . 69.5% residue (41 rows) (+ 1.7% gap (1 row))
```

The next run (bead `syzygy-bpyt.10`) cites this commit and reports movement.
`new 0 . reopened 0` on the remediated head is the loop closing.

## Appendix A — governance tooling inventory at dd520e8d

[Observed by the tooling sweep.]

**Columns.**

- LOC: physical lines. SLOC: non-blank, non-comment lines.
- Bat: battery check/selftest lines.
- WF: hosted workflow.
- Reach: battery, via-import or none.
- Refs: other scripts naming the file.
- T: TypeScript files naming it.
- Digest: whether any tracked file cites a sha256 of the current or a
  historical version.
- StrL: lines inside string constants. Doc: docstring lines.

**Lifecycles.**

- L: live.
- H: historical re-verifier in the battery.
- HN: historical, not run.
- C: unperformed candidate tooling.
- O: one-off.

| LOC | SLOC | Role | Life | Bat chk/self | WF | Reach | Refs | T | Digest | StrL | Doc | File |
|---:|---:|---|---|---|---|---|---:|---:|---|---:|---:|---|
| 11424 | 8893 | checker | L | 1/1 | governance-docs | battery | 26 | 0 | hist-digest-cited | 1094 | 1032 | `scripts/check_governance.py` |
| 3721 | 2848 | validator | H | 0/1 | governance-docs | battery | 1 | 0 | hist-digest-cited | 960 | 297 | `scripts/launch_gate_results.py` |
| 3046 | 2386 | validator | L | 1/1 | governance-docs | battery | 1 | 0 | hist-digest-cited | 369 | 255 | `scripts/validate_launch_administration.py` |
| 2440 | 2085 | act recorder (generic) | L | 18/1 | governance-docs | battery | 24 | 5 | hist-digest-cited | 336 | 174 | `scripts/record_versioned_signoff.py` |
| 2322 | 2029 | builder (per-act package) | C | 0/0 | - | none | 1 | 0 | - | 217 | 87 | `scripts/build_pwb_registry_loaded_profile_amendment.py` |
| 2219 | 1900 | checker | L | 1/1 | governance-docs | battery | 9 | 0 | hist-digest-cited | 268 | 248 | `scripts/check_spec_reconciliation.py` |
| 1996 | 1806 | builder (per-act package) | H | 0/1 | governance-docs | battery | 1 | 0 | hist-digest-cited | 516 | 55 | `scripts/build_pwb_container_shape_profile_amendment.py` |
| 1914 | 1674 | act recorder | H | 3/0 | governance-docs | battery | 2 | 0 | - | 469 | 247 | `scripts/record_pwb_behavior_amendment_acts.py` |
| 1675 | 1447 | installer/simulator (sitting) | HN | 0/0 | - | none | 8 | 0 | hist-digest-cited | 270 | 88 | `scripts/install_redis_sitting.py` |
| 1661 | 1455 | act recorder | H | 1/1 | governance-docs | battery | 1 | 0 | cur-digest-cited | 46 | 58 | `scripts/record_polaris_understanding_adoption.py` |
| 1513 | 1358 | builder (per-act package) | H | 0/1 | governance-docs | battery | 1 | 0 | hist-digest-cited | 304 | 39 | `scripts/build_pwb_dismissal_expiry_amendment.py` |
| 1386 | 1159 | builder (per-act package) | C | 0/0 | - | none | 0 | 0 | hist-digest-cited | 24 | 79 | `scripts/build_pwb_release_label_amendment.py` |
| 1127 | 984 | builder (per-act package) | H | 0/1 | governance-docs | battery | 7 | 0 | hist-digest-cited | 18 | 54 | `scripts/build_pwb_tree_framing_amendment.py` |
| 1122 | 1005 | builder (per-act package) | H | 0/0 | - | via-import | 1 | 0 | - | 27 | 52 | `scripts/build_three_surface_poc_vocabulary_epistemic_amendment.py` |
| 1075 | 945 | builder (per-act package) | H | 0/0 | - | via-import | 1 | 0 | hist-digest-cited | 27 | 52 | `scripts/build_pwb_class_granular_extraction_amendment.py` |
| 1062 | 977 | checker | L | 0/0 | - | none | 2 | 0 | hist-digest-cited | 16 | 1 | `scripts/check_docs_review_campaign_partition.py` |
| 1038 | 860 | installer/simulator (sitting) | HN | 0/0 | - | none | 2 | 0 | hist-digest-cited | 61 | 115 | `scripts/install_redis_local_agent_sitting.py` |
| 1006 | 852 | builder (per-act package) | H | 0/0 | - | via-import | 2 | 0 | cur-digest-cited | 25 | 53 | `scripts/build_pwb_anchor_resolution_amendment.py` |
| 997 | 859 | builder (per-act package) | H | 0/1 | governance-docs | battery | 1 | 0 | hist-digest-cited | 28 | 49 | `scripts/build_pwb_readability_successor.py` |
| 996 | 806 | generator (live view) | L | 1/1 | governance-docs | battery | 1 | 0 | cur-digest-cited | 115 | 72 | `scripts/render_launch_administration.py` |
| 969 | 866 | builder (per-act package) | HN | 0/0 | - | none | 0 | 0 | - | 26 | 36 | `scripts/build_three_surface_poc_identity_amendment.py` |
| 951 | 821 | builder (per-act package) | HN | 0/0 | - | via-import | 3 | 0 | - | 87 | 61 | `scripts/build_public_source_screening_scope_v2.py` |
| 950 | 829 | act recorder | C | 0/0 | - | none | 0 | 0 | - | 146 | 69 | `scripts/record_public_source_screening_scope_v4_act.py` |
| 940 | 813 | act recorder | HN | 0/0 | - | via-import | 5 | 2 | - | 161 | 74 | `scripts/record_public_source_screening_scope_v2_act.py` |
| 911 | 722 | checker | L | 0/0 | - | none | 0 | 0 | - | 32 | 135 | `scripts/check_evidence_currency.py` |
| 907 | 748 | generator (live view) | L | 1/1 | governance-docs | battery | 1 | 0 | cur-digest-cited | 50 | 144 | `.syzygy/governance/contracts/candidates/scripts/build_capability_1_views.py` |
| 897 | 779 | installer/simulator (sitting) | HN | 0/0 | - | none | 2 | 0 | - | 38 | 80 | `scripts/simulate_redis_sitting.py` |
| 885 | 772 | builder (per-act package) | H | 0/1 | governance-docs | battery | 1 | 0 | hist-digest-cited | 12 | 41 | `scripts/build_pwb_item_depth_amendment.py` |
| 863 | 637 | one-off measurement | O | 0/0 | - | via-import | 2 | 0 | - | 112 | 82 | `scripts/count_polaris_effective_scenarios.py` |
| 851 | 706 | shared engine | L | 0/0 | - | via-import | 5 | 0 | hist-digest-cited | 28 | 52 | `scripts/pwb_requirement_amendment.py` |
| 806 | 696 | act recorder | H | 1/1 | governance-docs | battery | 3 | 2 | - | 148 | 61 | `scripts/record_public_source_screening_scope_v3_act.py` |
| 796 | 678 | builder (per-act package) | H | 0/1 | governance-docs | battery | 7 | 0 | hist-digest-cited | 84 | 74 | `scripts/build_pwb_behavior_contract_repin.py` |
| 785 | 658 | builder (per-act package) | H | 1/1 | governance-docs | battery | 4 | 0 | cur-digest-cited | 35 | 78 | `scripts/build_contract_readability_restyle.py` |
| 780 | 651 | act recorder | C | 0/0 | - | via-import | 2 | 3 | - | 135 | 58 | `scripts/record_public_egress_v2_act.py` |
| 765 | 662 | builder (per-act package) | C | 0/0 | - | none | 1 | 0 | cur-digest-cited | 64 | 55 | `scripts/build_public_source_screening_scope_v4.py` |
| 760 | 622 | generator (live view) | L | 1/1 | governance-docs | battery | 1 | 0 | cur-digest-cited | 145 | 24 | `.syzygy/governance/contracts/candidates/scripts/build_task_router.py` |
| 747 | 623 | act recorder | C | 0/0 | - | none | 1 | 0 | - | 136 | 52 | `scripts/record_messages_api_route_registry_act.py` |
| 743 | 634 | act recorder | H | 3/0 | governance-docs | battery | 3 | 3 | - | 152 | 63 | `scripts/record_dossier_local_agent_acts.py` |
| 739 | 612 | act recorder | HN | 0/0 | node-ci | battery | 3 | 3 | - | 135 | 42 | `scripts/record_public_repo_admission_acts.py` |
| 735 | 654 | builder (per-act package) | H | 1/1 | governance-docs | battery | 1 | 0 | hist-digest-cited | 40 | 29 | `scripts/build_three_surface_poc_readability_successor.py` |
| 731 | 620 | act recorder | H | 1/1 | governance-docs | battery | 4 | 0 | cur-digest-cited | 183 | 54 | `scripts/record_pwb_behavior_contract_repin_acts.py` |
| 726 | 609 | act recorder | H | 1/1 | governance-docs | battery | 0 | 3 | - | 123 | 65 | `scripts/record_dossier_agent_provider_v2_act.py` |
| 704 | 588 | act recorder | C | 0/0 | - | none | 1 | 2 | - | 138 | 41 | `scripts/record_public_admission_registry_entries_acts.py` |
| 687 | 585 | act recorder | HN | 0/0 | - | none | 3 | 3 | - | 140 | 50 | `scripts/record_public_source_screening_scope_act.py` |
| 683 | 639 | builder (per-act package) | C | 0/0 | - | none | 1 | 0 | - | 10 | 20 | `scripts/build_provider_route_messages_api_entry.py` |
| 668 | 581 | act recorder/builder (generic, performed acts) | H | 1/1 | governance-docs | battery | 6 | 0 | cur-digest-cited | 73 | 66 | `scripts/readability_successor.py` |
| 652 | 553 | builder (per-act package) | C | 0/0 | - | via-import | 1 | 0 | - | 56 | 71 | `scripts/build_pwb_behavior_contract_repin_tree_framing.py` |
| 637 | 576 | builder (per-act package) | H | 0/1 | governance-docs | battery | 1 | 0 | hist-digest-cited | 24 | 25 | `scripts/build_pwb_missing_currency_disclosure_scenario.py` |
| 631 | 507 | builder (per-act package) | H | 1/1 | governance-docs | battery | 1 | 0 | - | 48 | 30 | `scripts/build_pwb_registry_currency_briefing_amendment.py` |
| 618 | 518 | act recorder | H | 1/1 | governance-docs | battery | 2 | 3 | - | 131 | 64 | `scripts/record_rfc5_project_documentation_act.py` |
| 617 | 523 | act recorder | H | 1/1 | governance-docs | battery | 1 | 0 | - | 86 | 53 | `scripts/record_spec_policy_readability_restyle.py` |
| 614 | 539 | builder (per-act package) | HN | 0/0 | - | via-import | 3 | 0 | - | 6 | 60 | `scripts/build_public_source_screening_scope.py` |
| 611 | 514 | builder (per-act package) | H | 1/1 | governance-docs | battery | 3 | 0 | cur-digest-cited | 20 | 68 | `scripts/build_polaris_dossier_local_agent_mode_v1_1.py` |
| 606 | 558 | generator (live view) | L | 1/0 | governance-docs | battery | 10 | 0 | - | 18 | 7 | `scripts/build_polaris_project_wide_contract_coverage.py` |
| 602 | 539 | builder (per-act package) | H | 1/0 | governance-docs | battery | 0 | 0 | - | 94 | 10 | `scripts/build_general_trusted_bootstrap_transaction.py` |
| 602 | 518 | checker | L | 1/1 | governance-docs | battery | 0 | 0 | hist-digest-cited | 49 | 91 | `scripts/check_quotations.py` |
| 594 | 516 | checker | H | 1/1 | governance-docs | battery | 1 | 0 | - | 7 | 67 | `scripts/check_polaris_response_ceiling_reading.py` |
| 593 | 452 | generator (live view) | L | 1/0 | governance-docs | battery | 1 | 0 | cur-digest-cited | 34 | 67 | `.syzygy/governance/contracts/candidates/scripts/build_budget_report.py` |
| 587 | 479 | generator (live view) | L | 1/0 | governance-docs | battery | 0 | 0 | cur-digest-cited | 67 | 87 | `.syzygy/governance/contracts/candidates/scripts/build_active_manifest.py` |
| 585 | 497 | builder (per-act package) | H | 1/1 | governance-docs | battery | 1 | 0 | - | 114 | 46 | `scripts/build_cap1_trusted_bootstrap_consent_adoption.py` |
| 585 | 508 | builder (per-act package) | HN | 0/0 | - | none | 1 | 0 | - | 31 | 62 | `scripts/build_rfc7_scoped_values_successor.py` |
| 584 | 500 | builder (per-act package) | H | 1/1 | governance-docs | battery | 4 | 0 | - | 19 | 63 | `scripts/build_polaris_dossier_local_agent_mode.py` |
| 573 | 480 | act recorder | H | 1/1 | governance-docs | battery | 1 | 0 | - | 147 | 56 | `scripts/record_pwb_registry_currency_amendment.py` |
| 571 | 503 | builder (per-act package) | H | 0/0 | - | via-import | 2 | 0 | - | 44 | 49 | `scripts/build_pwb_exact_source_render_mode_amendment.py` |
| 568 | 431 | generator (live view) | L | 1/1 | governance-docs | battery | 2 | 0 | cur-digest-cited | 22 | 31 | `.syzygy/governance/contracts/candidates/scripts/build_contract_index.py` |
| 529 | 431 | builder (per-act package) | HN | 0/0 | - | none | 1 | 0 | cur-digest-cited | 175 | 20 | `scripts/build_pwb_state1_amendment_manifest.py` |
| 526 | 456 | generator (live view) | L | 1/0 | governance-docs | battery | 1 | 0 | cur-digest-cited | 15 | 91 | `.syzygy/governance/contracts/candidates/scripts/build_dependency_index.py` |
| 519 | 469 | builder (per-act package) | H | 1/0 | governance-docs | battery | 0 | 0 | - | 29 | 4 | `scripts/build_general_trusted_bootstrap_impact_ledger.py` |
| 516 | 443 | builder (per-act package) | HN | 0/0 | - | via-import | 2 | 2 | - | 48 | 48 | `scripts/build_public_source_screening_scope_v3.py` |
| 509 | 419 | builder (per-act package) | HN | 0/0 | - | none | 1 | 0 | cur-digest-cited | 147 | 30 | `scripts/build_pwb_effect_acts_packet.py` |
| 502 | 375 | checker | L | 1/0 | governance-docs | battery | 4 | 0 | cur-digest-cited | 39 | 20 | `.syzygy/governance/contracts/candidates/scripts/verify_final_prespec.py` |
| 500 | 423 | act recorder | HN | 0/0 | - | none | 1 | 0 | - | 74 | 51 | `scripts/record_rfc7_scoped_values_successor.py` |
| 494 | 418 | act recorder | H | 1/1 | governance-docs | battery | 1 | 0 | - | 70 | 48 | `scripts/record_contract_readability_restyle.py` |
| 490 | 399 | builder (per-act package) | C | 0/0 | - | none | 0 | 0 | - | 17 | 69 | `scripts/build_pwb_registry_machine_ceiling_amendment.py` |
| 481 | 380 | builder (per-act package) | C | 0/0 | - | none | 0 | 0 | cur-digest-cited | 15 | 51 | `scripts/build_polaris_edit_repair_deletion_scenario.py` |
| 480 | 439 | builder (per-act package) | C | 0/0 | - | none | 1 | 0 | - | 66 | 19 | `scripts/build_public_admission_registry_entries.py` |
| 453 | 408 | builder (per-act package) | H | 0/0 | - | via-import | 1 | 0 | - | 26 | 37 | `scripts/build_pwb_machine_view_amendment.py` |
| 452 | 383 | builder (per-act package) | H | 1/1 | governance-docs | battery | 2 | 0 | cur-digest-cited | 17 | 52 | `scripts/build_polaris_dossier_local_agent_mode_v1_2.py` |
| 452 | 372 | act recorder | HN | 0/0 | - | none | 0 | 0 | - | 148 | 19 | `scripts/record_pwb_effect_amendment_acts.py` |
| 449 | 402 | builder (per-act package) | H | 0/0 | - | via-import | 2 | 0 | - | 27 | 44 | `scripts/build_pwb_opening_band_scenario.py` |
| 442 | 370 | act recorder | H | 1/1 | governance-docs | battery | 0 | 0 | - | 62 | 38 | `scripts/record_three_surface_poc_readability_successor.py` |
| 435 | 373 | act recorder | HN | 0/0 | - | none | 0 | 0 | hist-digest-cited | 52 | 1 | `scripts/polaris_generator_approval.py` |
| 432 | 365 | generator (live view) | L | 1/1 | governance-docs | battery | 3 | 0 | - | 32 | 52 | `scripts/build_polaris_dependency_unions.py` |
| 425 | 363 | generator (live view) | L | 1/1 | governance-docs | battery | 1 | 0 | - | 44 | 43 | `scripts/build_directive_register.py` |
| 421 | 361 | builder (per-act package) | H | 1/1 | governance-docs | battery | 1 | 0 | - | 12 | 51 | `scripts/build_spec_policy_readability_restyle.py` |
| 414 | 366 | builder (per-act package) | C | 0/0 | node-ci | battery | 2 | 2 | - | 14 | 50 | `scripts/build_public_egress_v2.py` |
| 413 | 367 | builder (per-act package) | H | 0/0 | - | via-import | 1 | 0 | - | 2 | 46 | `scripts/build_public_git_source_acquisition_local_agent.py` |
| 410 | 363 | builder (per-act package) | H | 1/0 | governance-docs | battery | 3 | 0 | - | 18 | 14 | `scripts/build_pwb_truth_policy_amendment.py` |
| 406 | 334 | act recorder | HN | 0/0 | - | none | 0 | 0 | - | 136 | 11 | `scripts/record_pwb_effect_acts.py` |
| 386 | 335 | builder (per-act package) | H | 0/0 | - | via-import | 1 | 0 | - | 20 | 38 | `scripts/build_rfc5_project_documentation_class.py` |
| 373 | 337 | builder (per-act package) | HN | 0/0 | - | none | 0 | 0 | - | 19 | 25 | `scripts/build_pwb_scoped_attributes_amendment.py` |
| 364 | 309 | act recorder | H | 1/0 | governance-docs | battery | 3 | 0 | - | 46 | 34 | `scripts/record_narrative_profile_adoption.py` |
| 363 | 340 | builder (per-act package) | H | 0/0 | - | via-import | 1 | 0 | - | 0 | 32 | `scripts/build_pwb_opening_index_amendment.py` |
| 344 | 279 | act recorder | HN | 0/0 | - | none | 0 | 0 | - | 135 | 8 | `scripts/record_pwb_truth_amendment.py` |
| 343 | 290 | generator (live view) | L | 1/1 | governance-docs | battery | 12 | 0 | - | 53 | 25 | `scripts/build_capability_1_spec_dependencies.py` |
| 303 | 268 | installer/simulator (sitting) | HN | 0/0 | - | none | 0 | 0 | - | 13 | 31 | `scripts/simulate_redis_local_agent_sitting.py` |
| 301 | 268 | builder (per-act package) | HN | 0/0 | node-ci | battery | 4 | 0 | - | 17 | 31 | `scripts/build_public_repo_admission.py` |
| 287 | 229 | act recorder | HN | 0/0 | - | none | 1 | 0 | - | 116 | 1 | `scripts/record_pwb_state1_amendment.py` |
| 280 | 232 | builder (per-act package) | H | 0/0 | - | via-import | 1 | 0 | - | 7 | 34 | `scripts/build_dossier_agent_provider_v2.py` |
| 261 | 229 | builder (per-act package) | H | 0/0 | - | via-import | 1 | 0 | cur-digest-cited | 0 | 19 | `scripts/build_three_surface_poc_block_provenance_amendment.py` |
| 254 | 214 | builder (per-act package) | H | 0/0 | - | via-import | 1 | 1 | - | 12 | 27 | `scripts/build_dossier_local_agent_acts.py` |
| 241 | 232 | one-off measurement | O | 0/0 | - | none | 0 | 0 | cur-digest-cited | 0 | 0 | `scripts/dossier_scale_measure.mjs` |
| 229 | 221 | one-off measurement | O | 0/0 | node-ci | none | 2 | 0 | hist-digest-cited | 0 | 0 | `scripts/derive_generator_sent_text.mjs` |
| 198 | 188 | mutation runner | O | 0/0 | - | none | 0 | 0 | hist-digest-cited | 0 | 9 | `scripts/polaris_prompt_mutants.py` |
| 197 | 170 | one-off measurement | O | 0/0 | - | none | 0 | 0 | - | 0 | 30 | `scripts/measure_machine_channel_provenance.py` |
| 184 | 172 | builder (per-act package) | H | 0/0 | - | via-import | 1 | 0 | - | 0 | 20 | `scripts/build_pwb_accessible_name_amendment.py` |
| 181 | 152 | shared engine | L | 0/1 | governance-docs | battery | 6 | 0 | hist-digest-cited | 21 | 20 | `scripts/pwb_signed_selftest.py` |
| 177 | 158 | one-off measurement | HN | 0/0 | - | none | 0 | 0 | - | 0 | 28 | `scripts/estimate_pwb_scoped_attributes_saving.py` |
| 165 | 140 | installer/simulator (sitting) | HN | 0/0 | - | none | 0 | 0 | - | 0 | 26 | `scripts/simulate_public_source_screening_scope_act.py` |
| 155 | 131 | generator (live view) | L | 1/0 | governance-docs | battery | 14 | 0 | - | 16 | 6 | `scripts/build_polaris_project_wide_spec_dependencies.py` |
| 144 | 114 | generator (live view) | L | 1/0 | governance-docs | battery | 5 | 0 | - | 6 | 16 | `scripts/build_three_surface_poc_spec_dependencies.py` |
| 133 | 129 | mutation runner | O | 0/0 | - | none | 0 | 0 | - | 0 | 0 | `scripts/run_m13_literal_mutations.mjs` |
| 115 | 111 | mutation runner | O | 0/0 | - | none | 0 | 0 | - | 0 | 0 | `scripts/run_m9_literal_mutations.mjs` |
| 109 | 107 | mutation runner | O | 0/0 | - | none | 0 | 0 | - | 0 | 0 | `scripts/run_m10_conditional_mutations.mjs` |
| 106 | 96 | one-off measurement | O | 0/0 | - | none | 0 | 1 | cur-digest-cited | 0 | 0 | `scripts/dossier_run_evidence.mjs` |
| 105 | 85 | one-off sweep | HN | 0/0 | - | none | 0 | 0 | cur-digest-cited | 9 | 20 | `.syzygy/governance/contracts/candidates/round-2026-08j/sweep_c2_normative_population.py` |
| 103 | 99 | mutation runner | O | 0/0 | - | none | 0 | 0 | - | 0 | 0 | `scripts/run_m7_literal_mutations.mjs` |
| 101 | 83 | one-off sweep | HN | 0/0 | - | none | 0 | 0 | cur-digest-cited | 7 | 26 | `.syzygy/governance/contracts/candidates/round-2026-08j/sweep_d3_coined_terms.py` |
| 82 | 68 | helper CLI | O | 0/0 | - | none | 1 | 0 | cur-digest-cited | 0 | 15 | `.syzygy/governance/contracts/candidates/scripts/context_load.py` |
| 53 | 49 | helper CLI | O | 0/0 | - | none | 1 | 0 | - | 0 | 0 | `scripts/read_ts_exported_string_array.mjs` |
| 47 | 39 | one-off measurement | O | 0/0 | - | none | 0 | 0 | - | 0 | 7 | `scripts/compare_unknown_denominator_withheld.py` |
| 36 | 35 | mutation runner | L | 0/0 | - | none | 0 | 0 | cur-digest-cited | 0 | 4 | `scripts/rule6_mutation_runner.py` |
| 8 | 7 | checker | O | 0/0 | - | none | 0 | 0 | cur-digest-cited | 0 | 0 | `scripts/check_generator_install.mjs` |

#### Totals by role

| Role | Files | LOC | SLOC |
|---|---:|---:|---:|
| builder (per-act package) | 49 | 34123 | 29740 |
| act recorder | 25 | 17660 | 15017 |
| checker | 8 | 17322 | 13908 |
| generator (live view) | 13 | 7042 | 5815 |
| validator | 2 | 6767 | 5234 |
| installer/simulator (sitting) | 5 | 4078 | 3494 |
| act recorder (generic) | 1 | 2440 | 2085 |
| one-off measurement | 7 | 1860 | 1553 |
| shared engine | 2 | 1032 | 858 |
| mutation runner | 6 | 694 | 669 |
| act recorder/builder (generic, performed acts) | 1 | 668 | 581 |
| one-off sweep | 2 | 206 | 168 |
| helper CLI | 2 | 135 | 117 |
| **total** | 123 | 94027 | 79239 |

#### Totals by lifecycle

| Lifecycle | Files | LOC | in battery (cmds) |
|---|---:|---:|---:|
| L | 24 | 30316 | 49 |
| H | 46 | 35775 | 56 |
| HN | 26 | 14598 | 0 |
| C | 13 | 10854 | 0 |
| O | 14 | 2484 | 0 |

#### Role x lifecycle (LOC)

| Role | L | H | HN | C | O |
|---|---:|---:|---:|---:|---:|
| builder (per-act package) | 0 | 21103 | 5347 | 7673 | 0 |
| act recorder | 0 | 9689 | 4790 | 3181 | 0 |
| checker | 16720 | 594 | 0 | 0 | 8 |
| generator (live view) | 7042 | 0 | 0 | 0 | 0 |
| validator | 3046 | 3721 | 0 | 0 | 0 |
| installer/simulator (sitting) | 0 | 0 | 4078 | 0 | 0 |
| act recorder (generic) | 2440 | 0 | 0 | 0 | 0 |
| one-off measurement | 0 | 0 | 177 | 0 | 1683 |
| shared engine | 1032 | 0 | 0 | 0 | 0 |
| mutation runner | 36 | 0 | 0 | 0 | 658 |
| act recorder/builder (generic, performed acts) | 0 | 668 | 0 | 0 | 0 |
| one-off sweep | 0 | 0 | 206 | 0 | 0 |
| helper CLI | 0 | 0 | 0 | 0 | 135 |

