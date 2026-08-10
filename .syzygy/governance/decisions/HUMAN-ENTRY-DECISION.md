# Owner decision packet — human entry and discoverability (P-38; supersedes round-08d packet 8)

> **This file decides nothing.** Current form of the human-entry question
> (previously round-2026-08d packet 8). Queued as **P-38**. The
> launch-gate pilot's E3 trace found this question sitting directly on
> Capability 1's path (rows 3 and 4 of its trace table) — it must be
> ruled before the first spec is authored.

## Question

Fix the human entry point and the discoverability posture:

```text
fixed Syzygy-owned entry:
    .syzygy/intent/OVERVIEW.md
    (governed presentation, never authority; absence renders as a finding)

per-repository discoverability:
    a kernel finding per governed repository, answer domain CLOSED AT FOUR
    VALUES per RFC7-40: yes / no / not-applicable / Unknown
    (is the entry reachable from where that repository's readers start?
    not-applicable keeps a repository with no governance root from
    rendering a truthful-looking "no")

write posture:
    Syzygy may PROPOSE a root README link to the entry;
    Syzygy may never write it directly (VIS-5 two-root write boundary)

entry identity (added 2026-08-10, RD27-02(a)):
    the round-08e repair pass drafted into RFC7-39 the ruling that the
    fixed entry IS the project's primary narrative (RFC7-6) — "there are
    not two front doors". This is a substantive answer the pass made, not
    a derivation; the owner may prefer a thin index entry distinct from
    the narrative. Disclosed at the acceptance record's §7 item 15.
```

## Current authority

Candidate RFC7-39 (fixed entry) and RFC7-40 (discoverability finding,
propose-never-write), both added at round-2026-08d; VIS-5 (adopted) for
the write boundary. Wave B ratifies the drafted clauses.

## Options

- **(a)** As drafted: fixed entry **identified with the RFC7-6 primary
  narrative** (RFC7-39's drafted ruling), per-repo four-valued finding,
  propose-only.
- **(b)** Additionally allow a proposed root-README pointer via adapter —
  still propose-only under VIS-5; adds an adapter surface the current
  clauses do not contemplate. Available later as an OpenSpec-level
  proposal without contract change; choosing it now widens Wave B.
- **(c)** Leave entry unspecified — every clone renegotiates where to
  start; Capability 1's "honest shape visibility" has no fixed door;
  RFC7-39/40 revert out of Wave B.
- **(d)** Keep the fixed entry but sever the identity: the entry is a thin
  index distinct from the primary narrative (two documents, one door) —
  redraft RFC7-39's "there are not two front doors" sentence before the
  Wave B act.

## Consequences

- (a): undiscoverable repositories surface as `Unknown`/`no` findings,
  not silently; the spec's rows 1.3/1.6 cite RFC7-39/40 as drafted.
- (b): Wave B re-review of the widened surface before its act.
- (c): the launch-gate E3 reopen-list keeps this row forever; the first
  spec would fix the entry by implication.

## Recommendation

`[Inferred]` **(a)**; (b) remains reachable later as OpenSpec-level work.

## Earliest required gate

Wave B act; on Capability 1's E3 path, so before spec authoring
regardless.

## Independent work

Yes.
