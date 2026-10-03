# Round 3 dispositions — public-source screening scope, version 2

> **Candidate — binds nothing.** Record for
> `reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-3-RAW.md` (verdict REVISE;
> finding 1 blocking, 2 to 5 notes), written 2026-10-04. The raw is retained
> verbatim. The repairs change bound bytes (the denylist words are in the
> patches), so the round-3 review is retired; round 4 is a narrow delta review
> of this diff and is the stopping point. No digest is copied here.

## Machine-readable binding

Reviewed record: .syzygy/governance/contracts/candidates/public-source-screening-scope-v2/reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-3-RAW.md
Revise-severity findings: 1

## Dispositions

### 1 — The packet's plain-words summary said the rule maps no governance text (blocking)

Repaired. The hand-written sentence is removed; the packet now points to the
generated block, whose first line is the scope in one sentence: the rule
withholds policy and governance text by name only, using the listed words, and
such text under any other name (including names without a separator or split by
a character outside the list) is sendable. The line is generated from the
builder and checked by `--check` in both the packet and the delta, so hand prose
cannot restate it. The reviewer's paths are fixtures: the doctrine, principles
and ADR0001-style names are checked against the repaired rule.

### 2 — `doctrine` was not in the denylist (note)

Added, with `doctrines`, and `principle` and `principles` (the lead's
decision). Each word has a mutant.

### 3 — The opt-in words had no plural forms (note)

Added: `manifestos` and `architectures`, denied in the variants that do not add
them and lifted in the variants that do. Fixtures cover both.

### 4 — Not every question had one decision with a default (note)

Q2 and Q4 now carry explicit defaults. The names are restated as a fact, not a
question. Q1 now says the recorder, when written, must refuse a second variant
act unless it is a declared superseding version, and that the bytes do not
enforce it.

### 5 — The Q3 cost example understated the mapped side (note)

Q3 now names camelCase and separator-free names (SecurityPolicy, CodeOfConduct,
ADR0001) and names split by a character outside the list ("spec(v2)") as
sendable.
