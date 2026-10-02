# {{TARGET_NAME}} observation consent (public repository)

> Template. Replace every `{{…}}` field; a filled record with any `{{` left is
> invalid. Candidate — binds nothing until the owner acts on the filled record.

Date: {{DRAFT_DATE}} (drafted); the act, if performed, records its own instant

Owner: {{OWNER}}

Record ID: `PUBLIC-OBS-{{TARGET_ID}}-{{DRAFT_DATE}}`

Record version: `{{VERSION}}`

Consent class: observation (RFC5-12)

Subject: `(project:{{PROJECT_ID}}, repository:{{REPOSITORY_ID}})`

Upstream: {{UPSTREAM_URL}} (public; configuration, not repository identity)

Admitted revisions (each a full Git object id; a tag name is a label only):

{{REVISION_TABLE}}

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
