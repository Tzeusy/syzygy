> **Candidate — binds nothing.** Impact ledger for semantic delta
> DOSSIER-LOCAL-AGENT-1.1 (`SEMANTIC-DELTA.md` in this directory), under
> CC-IMPACT-1 to CC-IMPACT-6. Every figure below was computed by script at
> `55daf6ceafe9e3622653beb4110284729e82d911` (`main`, after the v1.0
> sign-off); the predicates are published so that a reader can re-run them.

# Impact ledger — Polaris dossier local-agent mode, version 1.1

## Subject bytes

All digests are SHA-256 over the file bytes, computed by `sha256sum`.

| File, under `openspec/changes/polaris-dossier-local-agent-mode/` | v1.0 at `55daf6ce` | v1.1 (main patches applied) |
|---|---|---|
| `specs/polaris-generation/spec.md` | `b39d103263d6667e8ab5e10abec70fc0a53ed9a22fad00e4bc7532f1ce18c40e` | `b5564fe4f52b98716349c72307e123090952986cfd45dd7e2aab3fbf68765204` |
| `design.md` | `400e4e7c011566516df1e835ce4be5b1437828f3d8f92f5a269a0afd6c7658ce` | `66356a0fccee14a7e88fbce52324f619d11f82e49e3da955463b55fcf37c4a81` |
| `proposal.md` | `abdb8ba1fe1155fbe161e516b70fa20d743aa452ab73fc99b699bbe791f2e46d` | `f917b75019574bfb89af4cdb86be7347b4595e0e4758056de842a07cecdbb4da` |
| `GOVERNING-DEPENDENCIES.md` (regenerated) | `ae3008b3641ab6d88d09c7572fa481ae62f3ec3e3daa1deb3c2fa43e9b78f7c5` | `de399fc8f8f85eb90a13c3e941ac8374f9d171577d2e81431b0f0ed435410cf5` |
| `tasks.md` | `6ccaa6893947aa9cbb7dbe7b3704b7084167aee4bc74d4bf251b66115edd60c6` | unchanged |

With the optional N6 hunk applied on top, `spec.md` hashes to
`6414597d73572c903b0f876fd31d58f04d1b42a8c1a68361aa3a5f30feb598ee`. The
patches themselves are under `proposed/`: `spec.md.patch` (141 lines),
`design.md.patch` (94), `proposal.md.patch` (83) and
`spec.md.n6-optional.patch` (35). Each applies to the v1.0 bytes with
`git apply`; the N6 patch applies only after `spec.md.patch`.

## Counts

[Observed] `scripts/count_polaris_effective_scenarios.py` over the effective
Polaris composition:

| Bytes | Requirements | Scenarios |
|---|---|---|
| v1.0 | 35 | 227 |
| v1.1 | 35 | 231 |
| v1.1 with N6 | 35 | 232 |

The four scenarios v1.1 adds to 033 are "Permitting brief without the host
and attendance declaration", "Consent or policy record without its owner
act", "D9 record without its owner act" and "RFC7-20 reading record without
its owner act". Five 033 scenarios change their text: "Governed subject
without a per-project provider statement", "Execution rule follows SEC-3",
"Execution permission stays with the authoring session", "Adapter
credential readable" and "Execution permitted under the amendment". N6 adds
"Reported command outside the named scope". No scenario is removed or
renamed. `openspec validate polaris-dossier-local-agent-mode --strict`
(OpenSpec 1.9.0) passes on both applied forms.

## Text sweep

Predicate: for each phrase below, a byte-literal substring match (Python
`bytes in`) over every blob of `git ls-tree -r -z --name-only 55daf6ce`.
Population: **2,379 tracked files**. Every hit is listed; the classification
is the drafter's.

| Phrase changed or removed by v1.1 | Files | Classification |
|---|---|---|
| `SEC-3's rule` | 4 | the spec (changed here); the v1.0 delta, the v1.0 notes record and the round-3 raw (historical record of v1.0, not edited) |
| `every later check and at close` | 3 | the spec; the v1.0 delta and the round-3 raw (historical) |
| `configuration holds for its typed adapters` | 3 | the spec; the v1.0 delta and the round-3 raw (historical) |
| `an adopted capability declaration` | 4 | the spec (changed here); the round-3 raw (historical); `openspec/changes/polaris-non-governed-narrative-profile/proposed/polaris-generation/spec.md` and that package's `reviews/ROUND-2-DISPOSITIONS.md` — a separate change, describing its own predicate; **not touched** |
| `for a public repository` | 2 | `design.md` (changed here); the round-3 raw |
| `allow-execution` | 5 | `design.md` (changed here); `tasks.md`, the v1.0 packet and the v1.0 notes record (the command's name is unchanged, so these stay true); the round-3 raw |
| `REQ-polaris-generation-033` | 8 | spec, design, tasks, `GOVERNING-DEPENDENCIES.md`, the v1.0 delta, the v1.0 route-edits file, the reconciliation evidence `README.md` and `census.json` — the identifier is unchanged, so only the census entry's scenario list moves (below) |
| `drafted as D9` | 5 | spec, design, proposal (all changed here); the v1.0 delta and v1.0 packet (historical) |
| `the identifier it carries when adopted` | 2 | the spec (changed here); the v1.0 delta (historical) |
| `The candidate delta is held in` | 2 | this change's proposal (changed here); `openspec/changes/polaris-non-governed-narrative-profile/proposal.md`, a separate candidate whose sentence is still true; **not touched** |
| `Execution follows SEC-3 until it is amended` | 1 | the proposal (changed here) |
| `REQ-polaris-generation-034` | 4 | spec, `GOVERNING-DEPENDENCIES.md`, the v1.0 delta, `census.json`; 034's scenario names are unchanged |

[Observed] No file under `apps/`, `packages/` or `scripts/` contains
`REQ-polaris-generation-033`, `REQ-polaris-generation-034` or
`allow-execution` at `55daf6ce`. The `dossier` hits under `apps/` and
`packages/` belong to the provider-mode dossier (REQ 017–032), which v1.1
does not touch. No implementation code cites the changed text yet.

## Generated and coupled files

[Observed] In a scratch worktree at `55daf6ce` with the three main patches
applied:

- `scripts/check_spec_reconciliation.py --check` failed on three
  predicates, all expected ("4 of 7 predicates without FAIL"): R3, the
  census differs from regeneration; R4, `GOVERNING-DEPENDENCIES.md` differs
  from its spec's warrants (the new RFC5-12); R5, `PROJECT-STATUS.md`'s
  Polaris figure (35, 227) differs from the census (35, 231).
- `--regenerate` rewrote `GOVERNING-DEPENDENCIES.md` (contracts line gains
  `RFC5-12`, nothing else) and
  `docs/evidence/spec-readability-reconciliation-2026-10-02/census.json`
  (Polaris scenarios 227 → 231; four names added to 033's list).
- With `PROJECT-STATUS.md` line 51 edited to "35 requirements and 231
  scenarios", `check_spec_reconciliation.py --check` passed 7 of 7,
  `build_polaris_dossier_local_agent_mode.py --check` reported "the package
  verifies (applied)", `build_polaris_dependency_unions.py --check` passed,
  `check_governance.py` reported 0 FAIL of 53, and
  `record_versioned_signoff.py --check polaris-dossier-local-agent-mode
  --version 1.0` reported the v1.0 record "regenerates exactly; applied tree
  verified". The v1.0 record therefore survives the v1.1 bytes.

So the install must also edit:

| File | Edit |
|---|---|
| `PROJECT-STATUS.md` line 51 | 227 → 231 (232 with N6), and name the v1.1 sign-off record beside v1.0's |
| `GOVERNING-DEPENDENCIES.md` | regenerated |
| `census.json` | regenerated |
| `openspec/README.md` | the change's row names its current version (route edit, the v1.0 recording's block 2 form) |

The figure is also a coupling with the narrative profile's install
(`scripts/install_redis_sitting.py`, `refigure()`): whichever of the two
lands second recomputes both figures. `POLARIS-DOSSIER-LOCAL-AGENT-MODE-SIGNOFF-ROUTE-EDITS.txt`
quotes "227" as the v1.0 recording's input; it is a record of that
recording and is not edited.

## Tooling prerequisite (not in this package)

[Observed] `scripts/record_versioned_signoff.py`'s `real_packages()` knows
one package for this change, keyed `polaris-dossier-local-agent-mode`, whose
builder (`build_polaris_dossier_local_agent_mode.py`) installs v1.0 by moving
`proposed/` to `specs/`. Nothing applies a patch to an installed Polaris
addition. Recording v1.1 needs, in a separate implementation change:

- a builder for this package that checks the unapplied state (each patch
  applies to the v1.0 bytes; the N6 hunk, if the owner takes it, applies
  after), applies the patches, regenerates, and refigures `PROJECT-STATUS.md`;
- a `real_packages()` entry for this package, its subject being the applied
  `specs/polaris-generation/spec.md` and the review head digest being the
  v1.1 digest above (or the N6 digest);
- a selftest fixture per predicate, as the v1.0 builder has.

The reconciliation needs no change (the scratch run above). The same run
shows a gap: no check tells the signed v1.0 bytes from unsigned v1.1 bytes,
so until the builder exists the version-tagged sign-off is the only guard on
them. The PWB successor chain is the nearest precedent for a patch-carried
successor. The v1.0 record and recorder entry stay as they are.

## Downstream obligations

- The implementation slices written against v1.0 already carry R3-F1, F2,
  F3, F5, F7, F8 and N5 as implementation obligations (v1.0 notes record,
  "The other round-3 notes"). After the v1.1 sign-off their tests are
  conformance tests of normative text; no slice needs to wait.
- The N6 flag, if accepted, is new work: the run record gains a working
  directory and an in-scope statement per command, and the render a
  finding.
- The skill and Codex texts the design describes defer to the brief (N5);
  when they are written, they say nothing that grants execution.

## Out of scope, by finding

- R3-F6, dropped: the owner kept D9's Q3 (b).
- D9 notes N1 and N2 are the owner's. v1.1 reads N1 as the dossier already
  does (the choice is "a record for one run that names what the instruction
  covers: the run, its pinned revision, and building and running the observed
  project in the clone from that run's authoring session") and writes
  F1's keeping obligation in N2's recommended form; the packet says so.
