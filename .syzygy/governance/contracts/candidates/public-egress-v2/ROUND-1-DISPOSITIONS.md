> # Record beside the package — not authority, binds nothing
>
> Dispositions the findings of the round-1 fresh confirmation review of the
> second Anthropic egress version. It is not a package artifact: the manifest
> does not hash it and no builder reads it. Nothing here offers a phrase or
> performs an act (VIS-4).

# Round 1 dispositions — public egress version 2

- **Reviewed commit:** `860b0dea2d135fc032b61816540970315ebf012c`.
- **Raw:** `reviews/R-EGRESS-V2-1-RAW.md`, retained verbatim (CC-REV-6).
- **Verdict (raw line 4):** `REVISE`; two blocking findings (B-1, B-2) and nine
  notes (N-1 to N-9).
- **Effect:** every package byte the repair changes retires that review
  (rule 10); round 2 is dispatched over the repaired bytes.

## Machine-readable binding

Reviewed record: .syzygy/governance/contracts/candidates/public-egress-v2/reviews/R-EGRESS-V2-1-RAW.md
Revise-severity findings: 2

## Dispositions

### B-1 — "the same pinned parameters" was false for the Messages API route

Repaired. The template's route section now lists the parameters route by
route and says where they differ (tool list: an empty list against no field;
thinking: off against off or adaptive), and no longer says "the same". It also
adds the Agent SDK bytes the reviewer found missing (streaming, `cache_control`,
the `?beta=true` query, the empty account id), the Messages API endpoint, and
that the environment message is absent by construction on the Agent SDK route.
Each item was re-read against the two entries' `requestBytes` fields. The
brief gains criterion 13.

### B-2 — the packet did not say what signing lets leave the machine

Repaired. The packet opens with "What signing this record lets leave your
machine": file excerpts of the two named repositories for discovery ranking,
with the caps read from `discovery.ts` (1,500 characters, 40 files per call, 40
calls), the metadata that goes with them, the new sendability of README and
guide files, and that the route does not change. The brief gains criterion 12.

### N-1 — `project-documentation` is a widening outside the stages and the delegation

Accepted as declared. The packet, the brief (criterion 1) and the builder
docstring name it as a declared, intended widening that takes effect only after
sitting row 7.

### N-2 — route context became entry-overridable

Repaired. The first version's absolute ban on memory files, settings, MCP
servers, hooks and an environment summary is restored; the record says an
entry may narrow it and can never override it.

### N-3 — the Agent SDK summary omitted listed bytes

Repaired with B-1.

### N-4 — the target-metadata bullet was not extended

Repaired. The bullet names the discovery stages' subsystem names, blob counts,
blob ids and paths, and the target-content bullet names the bounded excerpts.

### N-5 — `all` in the Stages column was undefined

Repaired. The record defines `all` as the six pipeline stages and states, as
[Inferred], that discovery envelopes cross the same port once an adapter sends
them.

### N-6 — the derivation fails on current main

Repaired in this change. The derivation fixture used string reader questions;
it now uses the structured shape, and the script fails closed on any
`readerQuestions[]` leaf other than id, topics and text. The first version's
table bytes are unchanged by this (compared on main), so the confirmed first
version still describes the generator. Both builders' `--check` now run in the
node workflow, and the builder selftest has a mutant for the new leaf check.

### N-7 — stale or contradictory prose

Repaired. The stale readiness prose is gone, the class-list sentence is
reconciled, "rows 2 and 3" is now "rows 2a to 3b", the long line is wrapped,
criterion 7 now says retention and route context differ deliberately, and the
brief's head-line order now matches the four-line head the review used.

### N-8 — out-of-order signing

Repaired. The packet says signing the first version after this one is not an
offered order, and the first version's recorder now refuses it once this
version's act record exists (a selftest predicate covers it).

### N-9 — nothing pinned the template delta

Repaired. `v2.json` pins the template's delta against the first version's
(hunks, removed lines, added lines) and `--check` reports the template when the
counts differ; the selftest has a mutant for drift and for an unpinned delta.
