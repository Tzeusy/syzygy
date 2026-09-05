# Compaction charter — binding rules for every per-RFC compaction pass

> **Spent working charter. Binds nobody now, and is not authority.** It
> governed the rev9 → rev10 per-RFC compaction passes, which finished in
> August 2026; the corpus it produced has since been reviewed, amended and
> partly accepted by owner act. It is kept as the record of the rules that
> pass was run under. The word "binding" below means binding *on that pass*.
> Its input and output paths are under the git-excluded `_bootstrap/**` tree
> and do not resolve in a clone. For what binds today, read
> `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md`.

Authority: `REV9-FINAL-PRESPEC-DIRECTIVE.md` §3 and
`02-OWNER-DIRECTION-RECORD.md` OD-R10-3/OD-R10-6. The rev9 source corpus at
`_bootstrap/rfc-phase/rfcs/` is frozen input — never edit it. Outputs land in
`_bootstrap/rfc-phase/final-prespec/`.

## The optimization target (verbatim, owner)

> minimum complete governed context required for one decision or work item,
> not minimum document count.

The question is never "how can this be summarized?" It is: **what must a
human or agent read to act correctly, and what can remain linked historical
evidence?**

## Outputs per RFC

1. **Compacted active contract** → `final-prespec/rfcs/<same filename>`
   (RFC 0009: the `RFC-0009/` package per its specific charter).
2. **History file** → `final-prespec/history/RFC-000n-history.md`.
3. **Migration rows** → `final-prespec/matrix-rows/RFC-000n-rows.md`.
4. A short completion report (counts, anything ambiguous, anything you could
   not compact without judgment you lacked).

## Tier rules

**Tier 1 — stays in the active file:** scope + a short reader map;
definitions; every normative clause; closed vocabularies; state machines;
authority and lifecycle boundaries; integration obligations; failure,
Unknown, and degradation semantics; violation cases; explicit deferrals and
open defaults (open §8 questions, compactly). Keep `[Observed]`/`[Inferred]`/
`[Unknown]` labels on every retained substantive claim — the label survives
even when its essay is compressed to a sentence.

**Tier 2 — moves to the history file (with backlinks):** every
`*(History: …)*` parenthetical; amendment and review-origin narratives;
prior wording and why it changed; contradiction narratives; founder-interview
excerpts; extensive rejected alternatives (§6 "Alternatives considered" moves
wholesale unless an alternative is load-bearing for interpreting a live
clause — then one sentence stays with a pointer); **answered** §8 questions
with their answers/decision cites; long illustrative walkthroughs beyond one
canonical example.

**Tier 3 — generated later by the lead (not your job):** indexes, dependency
graph, routing, context manifests.

## Hard preservation rules (violating any of these fails the pass)

- **No obligation weakens.** Every MUST/never/only constraint survives at
  identical strength. Compress the prose around a rule, never the rule. When
  in doubt, keep the wording.
- **No owner decision disappears.** Any text carrying a decision identifier
  (A1–A9, B*, D1/D2, FD-*, SDR-*, CT-*, OQ-*, CC-TEST-*) or the phrase "the
  owner decided/ruled/declined" is retained in the active file or moved to
  history with an explicit backlink from the surviving clause. Never dropped.
- **No security premise thins.** The untrusted-tree premise, SEC-* readings,
  trust floors, and every "forgeable from inside the tree" argument keep
  their reasoning, not just their conclusion.
- **Preserved owner language stays verbatim** where the rev9 text marks a
  memorable owner phrase (quoted phrases, "stated honestly", named postures).
- **Closed vocabularies, enumerated lists, tables, and state machines are
  copied, not paraphrased.**

## Clause identity rules

- Retained clauses keep their exact `RFCn-m` (and letter) identifiers. No
  renumbering, ever. Retired numbers are never reused. Merges keep the
  **lowest** surviving number; the absorbed number is recorded in the matrix
  and listed in the active file's §0 as "merged into RFCn-k".
- New clauses (only where a specific charter orders one) take the next free
  integer after the rev9 end marker.
- The §0 structure line and end-of-contract marker state the final clause
  range **and** enumerate any gaps (retired/merged numbers) so the range
  stays deterministically checkable.

## Migration rows format

One row per rev9 numbered clause **and lettered sub-clause**, in order:

```
| RFCn-m | <outcome> | <target> | <reason, one line> |
```

Outcome is exactly one of: `retained unchanged` · `retained with wording
sharpened` · `merged into <clause>` · `moved to rationale/history` · `routed
to OpenSpec candidate` · `routed to craft-and-care` · `retired as
superseded/redundant`. ("moved"/"routed"/"retired" apply to whole clauses
only when their entire content leaves the active path; a clause whose
*narrative* moved but whose rule stays is `retained with wording sharpened`.)
Also add one row per §8 question (`q<n>` | `open — retained` or
`answered — moved to history`).

## History file format

```
# RFC-000n — rationale and amendment history (Tier 2, non-normative)
Extracted at the rev10 compaction. Nothing here binds; the active contract
is `../rfcs/<file>`. Full review corpus: `_bootstrap/rfc-phase/reviews/`.

## RFCn-m
*(History: …verbatim extracted text…)*  [plus any moved narrative, labeled]
```

Every entry keyed by clause ID; extracted `*(History: …)*` text is copied
**verbatim** — history is preserved, not rewritten to look cleaner.

## Metadata front matter (directive §5)

Every active RFC file (and each RFC-0009 module) begins with:

```yaml
---
id: RFC-000n
title: <title>
status_source: owner-act-record
module: <only for RFC-0009 package modules>
clauses: <exact range/list, e.g. "RFC4-1..RFC4-29 (RFC4-7 merged into RFC4-6)">
governs: [<closed set of entity/concern nouns>]
applies_to: [kernel|polaris|trajectory|orrery|mission-control|context|workspace|all-surfaces ...]
depends_on: [RFC-000x, ...]
provides_to: [RFC-000y, ...]
tags: [...]
---
```

Derivation rule for clause-level metadata (do not hand-maintain a second
store): `normative` = numbered clause text; `open-question` = §8 open items;
`informative` = sections marked non-normative; `history` = nothing in active
files (all in `history/`).

## Status header

Immediately after the front matter, keep the one-line status
self-declaration, updated to the two-state model:

> **Status:** Proposed foundational contract (self-declaration at authoring
> time). Effective status is established solely by an owner-act record
> binding this file's exact content digest — as an owner-adopted bootstrap
> act until the independent A1 correlation mechanism exists, and as a
> Syzygy-verified effective act only after correlation (RFC3-16). Absent
> such a record, this contract binds nothing.

## Citations

Every cross-RFC citation must resolve after compaction. Cite clause IDs, not
section numbers of other RFCs (IDs are stable; sections move). If you cite a
clause another pass might merge, cite it anyway — the lead reconciles merges
in the final citation sweep. Do not cite `_bootstrap/` paths in active
normative text; historical references belong in the history file.

## Word targets (acceptance targets, per RFC charter)

Stated in each work order. No module over ~7,000 words. Hitting the target
by deleting constraints or compressing into machine-only language is a
failed pass — if a target is unreachable without weakening, stop at the
smallest faithful size and say so in the report.

## Lead rulings (addendum, 2026-08-02 — uniform across all passes)

1. **Answered §8 questions** keep a one-line stub in the active §8 (question
   number + "answered — see history/<file> and <decision cite>") so question
   numbering never shifts; full text lives in history.
2. **`machine-clients`** is a lawful `applies_to` value (used by RFC-0006,
   0010, 0011).
3. **Document order** is front matter → H1 title → Status block; the H1 is
   not "intervening content."
4. **`provides_to` forward edges to RFC-0010/RFC-0011** are declared where
   real (both files exist in `final-prespec/rfcs/`).
5. **A word target is a target, not a license to weaken**: a pass that stops
   above target with an incompressibility accounting (à la RFC-0006's) is a
   conforming pass.
