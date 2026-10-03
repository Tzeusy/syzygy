# Impact ledger — public-admission registry entries

> **Candidate — binds nothing.** Drafted 2026-10-03 for bead `syzygy-mea`.
> Each count below was produced by the stated command on a tree of 1,973
> tracked files (`git ls-files | wc -l`), main at `dbf8ed19`, before this
> package's files were added. Re-run before relying on a figure.

## Sweep 1 — who reads the installed adapter-registry directory

Commands: `git grep -l -F adapter-registry -- apps packages` (8 files) and
`git grep -l -F adapter-registry -- apps packages scripts` (22 files).

[Observed] Every code reader names the Butlers file by its exact path
(`governance-inputs.ts` constant `PWB_AUTHORITY_ARTIFACTS.registry`, the
`walkthrough-inputs.ts` path list, the tests that read the file, and the
amendment builders and recorders in `scripts/`). The only directory listing in
`governance-inputs.ts` (`list(decisionsDir)`) lists the decisions directory,
not the registry. So adding two files to the registry directory at an act
changes no existing reader, and these candidates, which sit in this package,
change none now.

| Class | Effect |
|---|---|
| Butlers read gate (`body-read-authority.ts`, `governance-inputs.ts`) | None. Its authority set is keyed by observed project and holds exactly one row; a new entry is not a row |
| `check_spec_reconciliation.py` R6 | Reads the Butlers file's pin only |
| The amendment builders and recorders | Read the Butlers file only |

## Sweep 2 — who would consume the new entries

[Observed] `git grep -n -F provider-agent-sdk -- apps packages scripts`
returns 0 lines and no file under `apps`, `packages` or `scripts` imports a
provider SDK; the pipeline's `generate` port has no registered implementation.
Consumers do not exist yet, which is why `implementationVersion` is `null`.
Consumers to come, in order: the Agent SDK adapter (gap G2), the any-repo
reader (G1) and the consent-backed ports that evaluate registry, consent and
policy acts (G3). Each must refuse when its entry lacks an effective act.

## Sweep 3 — governance tooling

| Tool | Effect |
|---|---|
| `scripts/check_governance.py` | Gains two candidate act labels and a manifest copy registration, existence-gated, with no chain link (the AGENTS.md candidate-packet rule). Mutating a manifest row is caught by CG-7e |
| `scripts/build_public_admission_registry_entries.py` | New. `--check`, `--write`, `--digests`, `--manifest-digest`, `--selftest` |
| The Butlers recorders | Unchanged; they read only the Butlers entry |
| The admission package manifest | Separate; this package's manifest carries only its two rows |

## Sweep 4 — package prose carries no digest

Predicate: `[0-9a-f]{64}` over the package's Markdown files; the builder's
`--check` runs it. A row appears only in the manifest.
