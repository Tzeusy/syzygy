> **Candidate — binds nothing.** Impact ledger for semantic delta
> DOSSIER-LOCAL-AGENT-1.2 (`SEMANTIC-DELTA.md` in this directory), under
> CC-IMPACT-1 to CC-IMPACT-6. Every figure below was computed by script on
> branch `feat/dossier-waiting-sessions` at
> `28015c67fce4e84e542cc9d4b09f18eaa59bfecd`, whose
> `openspec/changes/polaris-dossier-local-agent-mode/` bytes are v1.1 as on
> `main`; the predicates are published so that a reader can re-run them.

# Impact ledger — Polaris dossier local-agent mode, version 1.2

## Subject bytes

All digests are SHA-256 over the file bytes. "v1.2" is the v1.1 tree with the
three patches applied by `git apply` and `check_spec_reconciliation.py
--regenerate` run.

| File, under `openspec/changes/polaris-dossier-local-agent-mode/` | v1.1 | v1.2 (patches applied, regenerated) |
|---|---|---|
| `specs/polaris-generation/spec.md` | `6414597d73572c903b0f876fd31d58f04d1b42a8c1a68361aa3a5f30feb598ee` | `a8f631a3ae2390f5090c86f982a8c8c34a875438d8ea38a814aa18641e593d67` |
| `design.md` | `66356a0fccee14a7e88fbce52324f619d11f82e49e3da955463b55fcf37c4a81` | `752ee397becb78e353ebfc108e646321b0f4078fad3c6e67e97a56dbb36a001d` |
| `proposal.md` | `f917b75019574bfb89af4cdb86be7347b4595e0e4758056de842a07cecdbb4da` | `b096c4d65dc6cb0a52fcc17b228bcaa981bc295f019faf931dc63574e1bb0b06` |
| `GOVERNING-DEPENDENCIES.md` (regenerated) | `de399fc8f8f85eb90a13c3e941ac8374f9d171577d2e81431b0f0ed435410cf5` | `ef111e933745618c573d58228edd3970d3144765df850bfc0a1fe36e62a0f545` |
| `tasks.md` | `6ccaa6893947aa9cbb7dbe7b3704b7084167aee4bc74d4bf251b66115edd60c6` | unchanged |

The patches are under `proposed/`: `spec.md.patch` (71 lines),
`design.md.patch` (66) and `proposal.md.patch` (39). Each applies to the v1.1
bytes with `git apply`. The regeneration also rewrites
`docs/evidence/spec-readability-reconciliation-2026-10-02/census.json`, and no
other tracked file.

## Counts

[Observed] `scripts/count_polaris_effective_scenarios.py` over the effective
Polaris composition:

| Bytes | Requirements | Scenarios |
|---|---|---|
| v1.1 | 36 | 244 |
| v1.2 | 36 | 248 |

The four scenarios v1.2 adds, all to REQ-polaris-generation-035, are "Waiting
session started before its packet", "Packet delivered to a waiting session",
"Printed pre-approval for a waiting session" and "Continuing reviewer
disclosed". No scenario is edited, removed or renamed. `openspec validate
polaris-dossier-local-agent-mode --strict` reports the change valid on the
applied bytes.

## Checks on the applied bytes

[Observed] `check_spec_reconciliation.py --check`, after `--regenerate`, on
the applied bytes: R1, R2, R3, R4 and R7 OK; R6 WARN with the two stale
behaviour-contract pins it reports on `main` today (unrelated, `syzygy-2g0d`);
R5 FAIL with one finding, `PROJECT-STATUS.md`'s Polaris composition figure
(36, 244) against the census (36, 248). That sentence is updated by the
install, not by this package.

R2 passing on the applied bytes is the gap the v1.1 package named: no check
tells the signed v1.1 bytes from unsigned v1.2 bytes until a v1.2 builder and
recorder entry exist.

## Text sweep

Predicate: for each phrase below, a byte-literal substring match (Python
`bytes in`) over every blob of `git ls-tree -r -z --name-only 28015c67`.
Population: **2,628 tracked files**. Every hit is listed; the classification
is the drafter's.

| Phrase changed by v1.2 | Files | Classification |
|---|---|---|
| `Exact behavioral delta, version 1.1` | 3 | the spec (changed here); the v1.1 package's `spec.md.patch` (historical record of v1.1, not edited); `packages/polaris-dossier/src/agent-texts.test.ts`, which pins the spec's head and moves at install |
| `these bytes bind only by the owner's sign-off of version 1.1` | 2 | the spec; the v1.1 package's patch (historical) |
| `this text binds only by the owner's sign-off of` + newline + `> version 1.1` | 1 | `design.md` (changed here) |
| `> **Version 1.1.**` | 4 | `design.md` and `proposal.md` (changed here); the v1.1 package's two patches (historical) |

The phrase v1.2 introduces as a warrant,
`POLARIS-DOSSIER-WAITING-SESSIONS-2026-10-08`, appears in 4 files at that
commit: the direction record, and three implementation files
(`packages/polaris-dossier/src/waiting-sessions.ts`, its test, and
`render.ts`), which cite the direction, not this package.

## Dependents

- **Implementation.** `packages/polaris-dossier`: `waiting-sessions.ts`,
  `session-handover.ts` (`startSessions`, `handOver`, the delivery),
  `cli.ts` (`session-prompt … all|--fresh`, `await`, exit 3) and `render.ts`
  (the continuity item and the review-status note). Each wait-mode step
  refuses until a `POLARIS-DOSSIER-LOCAL-AGENT-MODE-SIGNOFF-v1.2.md` (or
  later) record exists, so v1.1 behaviour is unchanged while this package is
  unsigned. Tests: `waiting-sessions.test.ts`, 32 tests; rule-6 mutants in
  `docs/evidence/polaris-dossier-waiting-sessions-mutants-2026-10-09.json`.
- **Agent texts.** The `/polaris-dossier` skill and the Codex instructions
  describe the v1.1 hand-over at their step 8 and do not mention waiting
  sessions; they are updated after the sign-off, under the agent-text lint.
- **Generated.** `GOVERNING-DEPENDENCIES.md` and the census, regenerated at
  install; `PROJECT-STATUS.md`'s Polaris figure and its v1.1 routing line.
- **Tooling, missing.** A v1.2 builder, its `real_packages()` entry and the
  v1.1 builder's delegation (the delta's migration plan).
- **Not touched.** REQ-polaris-generation-033, 034, 036; the provider-mode
  requirements; RFC7; doctrine; the gate sources and screens.

## Overlap

Predicate: `git grep -l -F REQ-polaris-generation-035 -- openspec` at the
commit above. Three files: this change's spec, and the candidate
`openspec/changes/polaris-dossier-arbitrary-public-repo/` (its
`proposed/polaris-generation/spec.md` and generated
`GOVERNING-DEPENDENCIES.md`). That candidate reads 035's *verdict contents*
(the fidelity verdict gains a classification of Inferred blocks) and names
035 as a parent; it says nothing about when a session starts or how many
revisions it reviews, so the two compose without overlap. A continuing
reviewer writes the same verdict either way. Whichever lands second
regenerates its dependency rows.
