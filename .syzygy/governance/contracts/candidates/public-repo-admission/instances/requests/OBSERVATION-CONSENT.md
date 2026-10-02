# requests observation consent (public repository)

> Instance for target T1, filled from `../../templates/OBSERVATION-CONSENT-TEMPLATE.md`. Candidate —
> binds nothing until the owner acts on this record's exact bytes. Fields
> marked "pending Q…" follow the packet's open questions and change if the
> owner answers differently.

Date: 2026-10-03 (drafted); the act, if performed, records its own instant

Owner: Tzeusy

Record ID: `PUBLIC-OBS-REQUESTS-2026-10-03`

Record version: `0.1.0-candidate.1`

Consent class: observation (RFC5-12)

Subject: `(project:oss-requests, repository:psf-requests)`

Upstream: https://github.com/psf/requests (public; configuration, not repository identity)

Admitted revisions (each a full Git object id; a tag name is a label only):

| Label | Git object id |
|---|---|
| `v2.34.2` | `6e83187b8feb273ed4c6cdab5efd8d54901dfab3` |

Proposed revocation state: active; supersedes no earlier consent

## Scope

Read-only reads of exact Git objects reachable from the admitted revisions,
from a scratch clone the operator creates for the run and deletes after it.
Reads are selected by the registered source-acquisition observer for this
project and screened under the observing project's public-source screening
scope before any ingest (RFC5-16).

The scope excludes:

- any revision not listed above, and any working tree other than the scratch
  clone;
- executing any code in the repository, including build, install and test
  scripts (SEC-3);
- any write to the repository, its forks or its issue tracker;
- the repository's issues, pull requests, CI logs and release assets;
- any other repository, including submodules not vendored at the admitted
  revisions; and
- network egress, which is a separate egress consent.

## Effect

Without an effective owner act over this record's exact bytes, nothing above
may be read and every claim depending on this repository is Unknown
(`unconsented-source-or-provider`). Revocation is prospective (RFC5-13): it
stops future reads; records made under the consent remain, shown as
withdrawn.
