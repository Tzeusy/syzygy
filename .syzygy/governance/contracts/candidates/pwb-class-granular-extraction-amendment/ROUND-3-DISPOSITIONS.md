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
    `REVIEW-BRIEF.md` is not edited. *(Marked 2026-10-14: superseded the
    same day. The owner directed one more cycle; the package, its builder
    and `REVIEW-BRIEF.md` were edited to repair all five findings, and the
    stale sentences listed below are now also marked at the sentence. See
    §"Repairs, 2026-10-14 (cycle 2)".)*
  - **No round 4 is dispatched.** *(Marked 2026-10-14: a round 4 is now
    prepared in `REVIEW-BRIEF.md` §"Round 4"; this record dispatches
    nothing.)*
  - **The bytes are not cleared.** This version is not offered for sign-off.
    It goes to the owner as register row P-86, with the five findings below
    open. *(Marked 2026-10-14: the five findings are repaired once,
    unconfirmed pending round 4; nothing is cleared or offered.)*
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

**Open.** *(Marked 2026-10-14: repaired once, unconfirmed; repair R1
below.)* Raw line 97. The reader definitions bind one rule name per rule,
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

**Open.** *(Marked 2026-10-14: repaired once, unconfirmed; repair R2
below.)* Raw line 134. The reviewer's re-run shows each fails on its own
phrase; the selftest's assertion is weaker than its summary line, and two
round-3 phrases have no mutant.

### 3 — the registry and policy pin residual names a performed bead (note)

**Open.** *(Marked 2026-10-14: repaired once, unconfirmed; repair R3
below.)* Raw line 153. `syzygy-jloi` is closed (performed 2026-10-02);
the current staleness is attributed to `syzygy-2g0d` (P-95).

### 4 — the collision census names one pending sibling; the builder lists four (note)

**Open.** *(Marked 2026-10-14: repaired once, unconfirmed; repair R4
below.)* Raw line 159. The all-orders check passes over all five patches,
so this is not a semantic collision; the current-tense table row is false
at the reviewed commit.

### 5 — scenario 3 does not exercise the source-path population total's qualification (note)

**Open.** *(Marked 2026-10-14: repaired once, unconfirmed; repair R5
below.)* Raw line 176.

## Repairs, 2026-10-14 (cycle 2)

**Status: round-3 findings repaired once on 2026-10-14, unconfirmed pending
round 4.** On 2026-10-14 the owner directed one more repair-and-review cycle
for this package; that direction supersedes this record's "the package is
not edited" and "no round 4 is dispatched" (marked above) and the same
words in `REVIEW-BRIEF.md` §"Round 3" (marked there). Every finding, notes
included, was repaired once over `main` at `814fbcc1`, on branch
`candidate/p86-round3-repairs`. Nothing was reviewed, signed or recorded.

The anchor-resolution sign-off (P-96, `7f43802f`) had moved the signed PWB
`spec.md` and `GOVERNING-DEPENDENCIES.md`, so the builder's `--check` failed
on arrival (the dependency patch no longer applied). The derived patch and
the manifest were regenerated with `--write`; the authored patches were
re-rendered over the current signed bytes with only the edits below.
Line numbers are in the files as repaired.

| Finding | Repair |
|---|---|
| R1 — rule provenance undecidable for a source two rules admit (revise) | `proposed/spec.md.patch` line 15: a new reader-definition bullet states the order (root index always `root-index`; a pillar's index file always `pillar-index`; a baseline spec, roster `butler.toml` or loaded-profile tree source admitted by its tree population alone; any other pillar-named file, a roster `MANIFESTO.md` included, `pillar-named-file`; two tree populations of one profile: the first declared). Oracle limb line 164 ("by the stated order …"), falsifier limb line 179, Case line 144, and a fourth new scenario line 225, "A source two rules admit carries one rule name". `proposed/design.md.patch` line 11 carries the order in the discovery-rule note. `SEMANTIC-DELTA.md` §3 cites the code order ([Observed] `project-shape-manifest.ts` 393, 403–405, 470–478) and names the one case the code differs (a pillar index an earlier pillar's index names) as [Inferred]. That case and the loaded-profile clauses are an owner content choice: **packet question 8** (new). Builder: six reader and six PWB-REQ-002 required phrases, one scenario heading and two design phrases added; mutants "rule precedence dropped" (line 802) through "scenario population total dropped" and "design precedence dropped" (line 866). |
| R2 — five mutants assert a generic prefix; two round-3 phrases unguarded (note) | Builder `_once` and `_lacks` (lines 655, 660) build each mutant's exact finding; the five mutants now expect it ("falsifier limb dropped" line 726, "per-class oracle dropped", "signed scenario dropped", "new scenario dropped", "design catalog-count sentence dropped" line 862). New mutants "third and fourth rule qualified by a grammar failure" (line 794) and "second rule's root need dropped" (line 798) guard the two phrases. [Observed] `--selftest` reports 51 structure mutants (39 before), all failing on their own predicates. `ORDER_POPULATION` (line 952) drops the now-signed anchor-resolution amendment, without which `--selftest` failed. |
| R3 — residual names performed `syzygy-jloi` (note) | Marked at the sentence, with the superseded text kept: `SEMANTIC-DELTA.md` residual 4 and `IMPACT-LEDGER.md` §"Registry entry and policy" now say R6 attributes both stale pins to `syzygy-2g0d` (P-95), [Observed at `814fbcc1`]. |
| R4 — collision census names one pending sibling; builder lists four (note) | Marked at the sentence: `IMPACT-LEDGER.md` sibling-packages row and §"Packages and fields this collides with", and `SEMANTIC-DELTA.md` §"Downstream impact", now list the three pending siblings (P-85, P-98, P-99) with "compose, all orders checked", and record that anchor-resolution (P-96) was signed v1.0 on 2026-10-14. Builder `PENDING_SIBLINGS` comment (line 128 area) updated to match. |
| R5 — scenario 3 misses the source-path population total (note) | `proposed/spec.md.patch` line 217: scenario 3's THEN now reads "every class and category count, and the source-path population total, that includes them states …"; required phrase and mutant "scenario population total dropped" added. |

Stale status sentences, also repaired at the sentence (dated marks, old text
kept): the packet's Status and question 1, `SEMANTIC-DELTA.md` Date, residual
2 (census now 17 requirements and 56 proposed scenarios, PWB-REQ-002 at 10,
from the builder's `--check`) and Review, and `REVIEW-BRIEF.md`'s round-2
and round-3 stopping-rule sentences. `REVIEW-BRIEF.md` gains §"Round 4",
with the head contract, the stopping rule and an explicit instruction that
the reviewer should read the round-3 raw and this record to verify the
repairs.

**Owner question added:** packet question 8 (the order for a source two
rules admit: the drafted order with the code changed at build for nested
pillar roots, or the code's registration order written into the text).
