> # Record beside the package — not authority, binds nothing
>
> Dispositions of the third fresh-context review of the PWB class-granular
> extraction amendment package. This record is not a package artifact: the
> manifest does not hash it and no builder reads it. It offers nothing and
> performs no act (VIS-4).

# Round 3 dispositions — PWB class-granular extraction amendment

- **Reviewed commit (raw line 2):**
  `00e24fd2dd10e8ffa8ba9cbecf88f58443fe72df`, the head of
  `candidate/p86-round2-repairs` (draft PR #415).
- **Manifest file digest (raw line 3):**
  `4562e028fc56b8b87aead03080aa9c515ce0308806a693977b9fcb35d8750abb`.
  [Observed 2026-10-14] The manifest file hashes to the same value after the
  branch was rebased onto `main` and landed with this record, and the
  builder's `--check` passes there.
- **Verdict (raw line 4):** `REVISE`. One revise finding (1) and four notes
  (2–5), with no blocking finding (raw line 180).
- **Reading scope the reviewer disclosed.** The reviewer followed the
  brief's Round 3 section and did not read the earlier dispositions or raws,
  although the dispatcher asked for a repair check against them; it checked
  the round-2 repairs the package itself names (raw lines 8–14 and 85–93).
- **Stopping rule applied.** The owner's direction of 2026-10-14
  (`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md`):
  one repair and one review per packet; anything still `REVISE` goes to the
  owner with its findings, not into another loop. This is also the rule the
  brief's §"Round 3" set before the round ran. Round 2's findings were
  repaired once and round 3 is the one review. Round 3 is not notes-only.
  So:
  - **The package is not edited.** The brief's round-3 rule says so for
    any verdict but a notes-only one, so the stale status sentences inside
    the package are corrected here, not at the sentence (below).
    `REVIEW-BRIEF.md` is not edited.
  - **No round 4 is dispatched.**
  - **The bytes are not cleared.** This version is not offered for sign-off.
    It goes to the owner as register row P-86, with the five findings below
    open.
  - This record recommends nothing on Questions 1–7.

Reviewed record: docs/reviews/R-PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-3-RAW.md

## Corrections carried here instead of in the package

As of 2026-10-14 these sentences in the package are no longer true. Each is
left as the reviewer read it, and this record carries the correction:

- `OWNER-DECISION-PACKET.md`, Status: "These bytes are unconfirmed, pending
  round 3". Round 3 has run and returned `REVISE`; the bytes stay
  unconfirmed.
- `SEMANTIC-DELTA.md`, Date: "(relayed to the drafting session by the lead
  session; no decision record holds it yet)" and "no round has read them".
  The direction is recorded in
  `../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md`, and
  round 3 read them.
- `SEMANTIC-DELTA.md`, Review: "the repaired bytes are **unconfirmed**
  pending round 3". Round 3 has run.
- `REVIEW-BRIEF.md` line 156: "no round 3 is dispatched" (the round-2
  rule). Round 3 was dispatched on the 2026-10-14 direction.

`ROUND-2-DISPOSITIONS.md`, a record beside the package rather than package
bytes, carries dated marks at its own two stale sentences. Register row P-86
is updated outside the package.

## Dispositions

### 1 — rule provenance is undecidable for a source that two population rules admit (revise)

**Open.** Raw line 97. The reader definitions bind one rule name per rule,
but neither the signed source-path sentence nor any added line says which
name a source carries when two rules admit it. The code settles it by a
precedence the text does not state (`project-shape-manifest.ts` lines
471–478), and contradicts the text for a pillar-named roster `MANIFESTO.md`.
Whether Butlers' index actually links to a baseline spec at `32f38feb` is
[Unknown]. The raw's direction: state the precedence in the reader
definitions, cover the `MANIFESTO.md` and root-index cases, give it a
falsifier limb or scenario and a selftest mutant, and, being a reading, put
it to the owner.

### 2 — five selftest mutants assert only a generic prefix (note)

**Open.** Raw line 134. The reviewer's re-run shows each fails on its own
phrase; the selftest's assertion is weaker than its summary line, and two
round-3 phrases have no mutant.

### 3 — the registry and policy pin residual names a performed bead (note)

**Open.** Raw line 153. `syzygy-jloi` is closed (performed 2026-10-02);
the current staleness is attributed to `syzygy-2g0d` (P-95).

### 4 — the collision census names one pending sibling; the builder lists four (note)

**Open.** Raw line 159. The all-orders check passes over all five patches,
so this is not a semantic collision; the current-tense table row is false
at the reviewed commit.

### 5 — scenario 3 does not exercise the source-path population total's qualification (note)

**Open.** Raw line 176.
