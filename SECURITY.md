# Security

## Scope

**Syzygy has no running software, no deployed service, and no released
artifact.** There is no product attack surface today. This repository's
contents are governance documents plus a small amount of executable tooling,
disclosed here in full:

- tracked git hooks under `.beads/hooks/` (Beads issue-tracker integration).
  **Cloning never activates them** — `git clone` does not install hooks;
- `.github/workflows/governance-docs.yml`, which runs the documentation
  checks below on push and pull request to `main`;
- `.claude/settings.json`, which runs `bd prime` on session start for anyone
  opening the repository in Claude Code;
- Python validation scripts under `scripts/` and
  `.syzygy/governance/contracts/candidates/scripts/`. `check_governance.py`,
  `verify_final_prespec.py` and `context_load.py` are read-only.
  `build_contract_index.py` and `build_dependency_index.py` **write their
  derived index files** in default mode (`--check` mode is read-only).

Nothing else in this repository executes.

## Committed posture

The security rules the project has already adopted are doctrine
**SEC-1…SEC-5** in
[`.syzygy/governance/doctrine/security.md`](.syzygy/governance/doctrine/security.md).
**That file is the authority; this table is a faithful summary, and where
they differ, doctrine wins.**

| Rule | Summary |
|---|---|
| **SEC-1 — Authenticated by default** | Endpoints reachable unauthenticated only on loopback, and client classes distinguished even there: browser requests pass origin/CSRF checks including on loopback; non-browser clients are admitted only through an explicit machine-client mechanism; location never proves identity. Any exposure beyond localhost requires authenticated, TLS-protected access limited to the owner's devices |
| **SEC-2 — Egress through consent** | Governed-project content — including anything derived from it, prompts included — leaves owner-controlled infrastructure only under explicit, recorded, per-project consent naming the permitted providers and the content classes that may be sent. Model providers are such services; providers not named require fresh consent, and remote backing dependencies are permitted under the same consent rule. Absent consent, the inferred layer renders Unknown rather than being computed |
| **SEC-3 — Observed code is untrusted, everywhere** | Observed-project code executes only inside an explicit opt-in execution profile — default-deny, isolated credentials, declared network access, resource limits, and destructive-operation gates — untrusted regardless of who owns the project. No observed code executes at all until the profile contract is accepted |
| **SEC-4 — Writes consented, attributed, revertable** | Syzygy writes into a governed repository only after recorded per-repository consent; every write is attributed, atomic, and individually revertable; existing governance artifacts it did not author are never overwritten without surfacing the conflict |
| **SEC-5 — Secrets never indexed** | Observation applies a declared secret-detection policy; matching content is excluded and the exclusion rendered; unclassifiable content fails closed — excluded, not indexed. A secret in any surface, store, or endpoint is a trust-floor violation |

These are floors an implementation may strengthen and may never weaken,
waive, or temporarily bypass; changing them is an owner doctrine amendment.

## Reporting

There is nothing deployed to attack. If you find a **governance-level**
security defect — a rule that would permit an unsafe implementation, a
contradiction between security rules, or a gap a first implementation could
fall through — please open a GitHub issue describing both readings.
Governance defects are cheapest to fix before they become code. A dedicated
security contact address arrives with the first deployable artifact.

## What this project does not claim

- It does not claim to be secure — nothing exists to be secure.
- It does not claim its governance records are independently verified:
  records in this tree sit within the write reach of the actors they govern.
  The project states that gap (see the acceptance record's two-state
  provenance model) rather than hiding it.
