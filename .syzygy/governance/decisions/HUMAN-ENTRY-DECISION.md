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
    a kernel finding per governed repository: yes / no / Unknown
    (is the entry reachable from where that repository's readers start?)

write posture:
    Syzygy may PROPOSE a root README link to the entry;
    Syzygy may never write it directly (VIS-5 two-root write boundary)
```

## Current authority

Candidate RFC7-39 (fixed entry) and RFC7-40 (discoverability finding,
propose-never-write), both added at round-2026-08d; VIS-5 (adopted) for
the write boundary. Wave B ratifies the drafted clauses.

## Options

- **(a)** As drafted: fixed entry, per-repo finding, propose-only.
- **(b)** Additionally allow a proposed root-README pointer via adapter —
  still propose-only under VIS-5; adds an adapter surface the current
  clauses do not contemplate. Available later as an OpenSpec-level
  proposal without contract change; choosing it now widens Wave B.
- **(c)** Leave entry unspecified — every clone renegotiates where to
  start; Capability 1's "honest shape visibility" has no fixed door;
  RFC7-39/40 revert out of Wave B.

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
