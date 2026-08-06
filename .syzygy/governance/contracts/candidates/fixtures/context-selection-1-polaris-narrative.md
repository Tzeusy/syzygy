# Context-selection fixture 1 — Polaris narrative/requirement change

**Objective.** A governed work item: revise an adopted Polaris narrative
section whose claim block cites a requirement whose target anchor changed;
re-anchor and resubmit for adoption. Risk class: content change on the
intent surface; no code, no security surface.

**Selection rule trace (RFC11-4).** Warrant names the narrative entity →
`applies_to: polaris` selects RFC-0007; the affected clause set is the
narrative model and adoption workflow → module `narrative-contract` +
package README (lookup + spanning invariants). The claim block renders
against evaluation vocabularies → RFC-0002 `rendering-vocabularies` +
package README. Shape-defining adoption gates are doctrine → `vision.md`
(VIS-3/VIS-4).

## Required context (mandatory, deterministic)

```
scripts/context_load.py rfcs/RFC-0007/README.md \
  rfcs/RFC-0007/narrative-contract.md rfcs/RFC-0002/README.md \
  rfcs/RFC-0002/rendering-vocabularies.md doctrine:vision.md
```

Measured: **13,892 words ≈ 18,754 estimated tokens** — inside the
15–20k working target. (Rev9 equivalent: whole corpus, ~121k words.)

## Omitted applicable candidates, with reasons

- RFC-0007 `rendering-and-surface` — the task edits content, not surface
  rendering; its obligations bind the surface implementer, not the author.
- RFC-0002 core/challenge/reconciliation modules — the claim's evaluation
  is pinned by the packet's as-of; authoring consumes the rendering
  vocabulary only.
- RFC-0001, RFC-0006 — anchor and selection semantics are restated at
  authoring strength inside RFC7-11/11(a)/16; the deeper contracts bind
  the kernel, not this edit (moved to suggested, below).
- RFC-0003/0004/0005/0008/0009/0010/0011, `security.md`, all craft
  policies — no governed home change, no evidence capture, no client or
  execution surface touched.

## Why no applicable constraint was lost

Every clause the warrant's entities cite in the index
(`05-CONTRACT-INDEX.yaml`) resolves into the selected set or into the
suggested set below; the adoption gate (VIS-4, RFC7-23/24/25) and the
anchor obligations (RFC7-11(a)) are in the mandatory set. The governing
phase rule travels with the packet (RFC11-4's mandatory-inclusion rule):
the selected RFC-0007 README carries the **RFC7-38 restatement** in its
"Phase boundary" section, and the index marks the clause
`kind: phase-rule` so a selector can force the full clause text when the
module carrying it is not otherwise selected. The packet
would render **incomplete/Unknown** (RFC11-6) if the narrative's pinned
evaluation were stale — disclosed, not silently proceeded past.

## Suggested inferred additions (provenance: index adjacency)

RFC-0006 (selection-reference semantics behind RFC7-16); RFC-0001
clauses RFC1-19/RFC1-25 (anchor identity classes). Suggested because the
authoring-strength restatements suffice for this edit; loading them adds
~4,900 words.

## Packet digest

sha256 over the mandatory files concatenated in listed order:
`8c0d75e6e2ce3e53…` (recompute: `cat <mandatory files> | sha256sum`).

**Selection: hand-authored golden selection. Measurement: mechanical.
Compiler implementation: absent.** `scripts/context_load.py` resolves a
path list it is handed and counts words; it has no notion of a task, a
warrant, a risk class, an `applies_to` value, or a dependency edge. The
selection above was made by a human and the trace is the reasoning that
produced it, written down — not a machine's output narrated afterwards.
The `Compiler: context_load.py, selection rules rev10-fixtures` line this
fixture used to carry was removed 2026-08-06: there is no compiler, and
`rev10-fixtures` resolved to nothing anywhere in the repository.

*Re-measured 2026-08-05 (refactor round): packet digest refreshed after the recorded RFC-0007 README correction (cross-module edge count, word-neutral); word/token figures unchanged; selection unchanged.*

*Re-measured 2026-08-05b by `scripts/check_governance.py` CG-18, which recomputes the digest and the word count from the declared mandatory set rather than trusting the recorded figures. Previous: 13,864 words, digest `4544d4b27646e905…`. Selection unchanged; the movement is contract edits landing under a fixture that had no mechanical freshness check until now.*
