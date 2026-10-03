# redis observation consent (public repository)

> Instance filled from `../../templates/OBSERVATION-CONSENT-TEMPLATE.md` by
> `scripts/build_public_repo_admission.py`. Candidate — binds nothing
> until the owner acts on this record's exact bytes.

Date: 2026-10-03 (drafted); the act, if performed, records its own instant

Owner: Tzeusy

Record ID: `PUBLIC-OBS-REDIS-2026-10-03`

Record version: `0.1.0-candidate.7`

Consent class: observation (RFC5-12)

Subject: `(project:syzygy, repository:redis-redis)`

Upstream: https://github.com/redis/redis (public; configuration, not repository identity)

Admitted revisions (each a full commit object id; a tag name is a label only):

| Label | Commit object id |
|---|---|
| `8.10.2` | `498ecd0d6d007db11ddb3aea9428552598a78622` |
| `7.2.4` | `d2c8a4b91e8c0e6aefd1f5bc0bf582cddbe046b7` |
| `7.4.0` | `c9d29f6a918c335bc1778d9f68e521c1bbb36a0f` |
| `8.0.0` | `e91a340e241cf0abe3c6a0c254214fbe4aa1d95f` |

Proposed provenance state: `owner-adopted (bootstrap, uncorrelated)` —
state (1), RFC3-16; A1 audit-record identity explicitly absent

Proposed revocation state: active; supersedes no earlier consent

## Scope

The grant covers read-only reads of exactly these Git objects: each admitted
revision's commit object, and the tree and blob objects reachable from that
commit's root tree. It does not cover any other commit, including ancestors
of an admitted revision, or the trees of other commits except where an
object is shared with an admitted snapshot.

The operator fetches each admitted commit alone into a local repository used
only for the run (`git fetch --depth=1 <upstream> <commit>`), so no ancestor
commit is transferred; reads go through Git object access, never a
checked-out working tree. Reads are selected by the registered source
acquisition entry that serves this repository (its shape is settled when it
is drafted) and screened under
`project:syzygy`'s effective public-source screening scope before any ingest
(RFC5-16, RFC3-30).

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
