# Round 2 dispositions — public-source screening scope, version 2

> **Candidate — binds nothing.** Record for
> `reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-2-RAW.md` (verdict REVISE;
> finding 1 blocking, 2 to 4 notes), written 2026-10-04. The raw is retained
> verbatim. Every repair changes bound bytes, so the round-2 review is retired
> and a round-3 review is needed. No digest is copied here.

## Machine-readable binding

Reviewed record: .syzygy/governance/contracts/candidates/public-source-screening-scope-v2/reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-2-RAW.md
Revise-severity findings: 1

## Dispositions

### 1 — Name-based withholding was root-only and exact-segment, and the claims said more (blocking)

Repaired by one closed token rule instead of exact directory segments. Under
the docs tree every directory name after the first, and the file name without
its extension, is split at the characters hyphen, underscore, full stop and
space after the ASCII fold; a path with any whole word from the denylist
(adr, decision, rfc, spec, specification, design, governance, policy,
security, conduct, with plural forms) is withheld. The opt-in words
MANIFESTO and ARCHITECTURE are in the denylist in every variant that does not
add them, so the variant governs them anywhere, not only at the root. The
reviewer's probe paths are fixtures, each token group and each token has its own
mutant, each separator has one, and a substring-matching mutant is caught.
Every sendable and withheld line in the packet and the delta is the generated
block, including the claim that a governance document whose path carries none of
the words is not withheld. `indeterminate` and `notMapped` agree. Packet Q1
and Q3 are rewritten to say what the rule does, including both costs.

### 2 — Stale cross references (note)

Repaired: the delta points to packet Q3, the builder docstring says four-row
manifest, and `--write` names the four patches.

### 3 — Exactly one variant act was prose only (note)

Each variant now has a distinct `policyVersion` suffix naming it. The delta
records that the recorder (written after the review) must refuse a second
variant act over this manifest unless it is a declared superseding version.

### 4 — The Kelvin-sign denylist bypass is literal by design (note)

Recorded in the delta as a literal-rule note for a TypeScript consumer, with the
other literal behaviours (ASCII digits, A-Z-only folding, whole-word splitting).
