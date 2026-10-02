# {{TARGET_NAME}} observation consent (public repository)

> Template. Replace every `{{…}}` field; a filled record with any `{{` left is
> invalid. Candidate — binds nothing until the owner acts on the filled record.

Date: {{DRAFT_DATE}} (drafted); the act, if performed, records its own instant

Owner: {{OWNER}}

Record ID: `PUBLIC-OBS-{{TARGET_ID}}-{{DRAFT_DATE}}`

Record version: `{{VERSION}}`

Consent class: observation (RFC5-12)

Subject: `(project:syzygy, repository:{{REPOSITORY_ID}})`

Upstream: {{UPSTREAM_URL}} (public; configuration, not repository identity)

Admitted revisions (each a full commit object id; a tag name is a label only):

{{REVISION_TABLE}}

Proposed provenance state: `owner-adopted (bootstrap, uncorrelated)` —
state (1), RFC3-16; A1 audit-record identity explicitly absent

Proposed revocation state: active; supersedes no earlier consent

## Scope

The grant covers read-only reads of exactly these Git objects: each admitted
revision's commit object, and the tree and blob objects reachable from that
commit's root tree. It does not cover any other commit, including ancestors
of an admitted revision, or the trees of other commits except where an
object is shared with an admitted snapshot.

The operator fetches those objects into a local clone used only for the run;
reads go through Git object access, never a checked-out working tree. Reads
are selected by the registered source-acquisition observer for this pair and
screened under `project:syzygy`'s public-source screening scope before any
ingest (RFC5-16, RFC3-30).

The scope excludes:

- every commit not listed above, and every working tree;
- executing any code in the repository, including build, install and test
  scripts (SEC-3);
- any write to the repository, its forks or its issue tracker;
- the repository's issues, pull requests, CI logs and release assets;
- any other repository, including submodules not vendored at the admitted
  revisions; and
- network egress, which only the separate egress consent can permit.

## Effect

Without an effective owner act over this record's exact bytes, nothing above
may be read and every claim depending on this repository is Unknown
(`unconsented-source-or-provider`). Revocation is prospective (RFC5-13): it
stops future reads and renders dependent claims Unknown at the next
evaluation; records made under the consent remain, shown as withdrawn.
