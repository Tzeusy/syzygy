# Impact ledger — Messages API provider route registry entry

> **Candidate — binds nothing.** Drafted 2026-10-03. Each count below was
> produced by the stated command on a tree of 1,990 tracked files
> (`git ls-files | wc -l`), main at `b97b77ed`, before this package's files
> were added. Re-run before relying on a figure.

## Sweep 1 — who reads the installed adapter-registry directory

Commands: `git grep -l -F adapter-registry -- apps packages` (8 files) and
`git grep -l -F adapter-registry -- apps packages scripts` (22 files; 23 with
this package's builder).

[Observed] Readers name the Butlers file by its exact path; none enumerates the
directory. Adding one file at an act changes no existing reader; this
candidate, which sits in this package, changes none now.

## Sweep 2 — who would consume the entry

Commands: `git grep -n -F "@anthropic-ai/sdk" -- apps packages scripts` and
`git grep -n -F provider-messages-api -- apps packages scripts`, each over the
tree before this package, and `git grep -l -F provider-agent-sdk -- apps
packages scripts`: 0 lines, 0 lines, 0 files.

[Observed] No source imports the SDK or names either route's implementation
id on main; PR #264's adapter is unmerged. Consumers to come: that adapter and
the consent-backed ports. Each must refuse when the entry lacks an effective
act, which is why `implementationVersion` is `null`.

## Sweep 3 — the sibling entry

[Observed] PR #255's provider entry has observer id
`polaris-provider-route-anthropic-agent-sdk` and the same subject and
authority type. The builder cross-checks both while that file exists in the
tree, so a drift of either entry away from the shared authority fails
`--check`. If both were adopted RFC4-1 would be violated, which is why the
entry carries `routeSubstitution.onlyOneAdoptable`.

## Sweep 4 — governance tooling

| Tool | Effect |
|---|---|
| `scripts/check_governance.py` | Gains one candidate act label and a manifest copy registration, existence-gated, with no chain link (the AGENTS.md candidate-packet rule). A manifest-row mutation is caught by CG-7e |
| `scripts/build_provider_route_messages_api_entry.py` | New. `--check`, `--write`, `--digests`, `--manifest-digest`, `--selftest` |
| The Butlers recorders, PR #255's builder and registration | Unchanged |

## Sweep 5 — package prose carries no digest

Predicate: `[0-9a-f]{64}` over the package's Markdown files; the builder's
`--check` runs it. The act argument appears only in the manifest.
