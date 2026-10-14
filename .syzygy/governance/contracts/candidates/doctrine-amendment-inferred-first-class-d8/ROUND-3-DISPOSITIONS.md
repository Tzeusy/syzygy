# Round 3 dispositions — D8 doctrine amendment packet

> **Candidate — binds nothing.** The record of how each round-3 finding is
> classified. Nothing in the package is repaired here: every finding is
> open for the owner. A disposition is not a confirmation.

**Round:** 3, fresh context. **Raw:**
`docs/reviews/R-DOCTRINE-AMENDMENT-D8-3-RAW.md`, retained verbatim.
**Reviewed commit (raw line 2):** `b913d1ef37b8e6fc5dffe65b113285f00eb8ab8c`.
**Package digest reviewed (raw line 3):**
`801ad3c05edb70f87784e8129ea2da6414518fe48a6f4c2cb5a096dfde35eaad`
(re-derived 2026-10-14 by the brief's method over the six tracked files at
that commit; it matches).
**Verdict, copied from the raw (line 4):** `Verdict: REVISE`.
**Findings:** 5 — one revise-level (1) and four notes (2–5), per the raw's
summary (lines 310–311).

Reviewed record: docs/reviews/R-DOCTRINE-AMENDMENT-D8-3-RAW.md

**Why round 3 ran.** The owner's direction of 2026-10-14 for a second
cycle, now recorded in
`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md`:
repair every finding, notes included, then one fresh review under the same
stopping rule. The brief's §"Round 3" set that rule before the round.

**Process note the raw records.** The brief names the raw's output path
in the repository; the dispatcher had the reviewer write to a session
scratchpad instead, and the raw was copied into `docs/reviews/`
byte-for-byte afterwards (raw lines 52–55). The head is the brief's
four-line contract.

**Stopping rule applied.** A verdict still `REVISE` goes to the owner with
its findings; the package is not repaired again and no round 4 is
dispatched without a new owner direction (brief §"Round 3"; raw lines
321–322). So:

- **The package is not repaired again.** The only edits after the round
  are dated status marks at the "unconfirmed pending round 3" sentences in
  the packet, the delta, the ledger and `ROUND-2-DISPOSITIONS.md`, with the
  old text kept.
- **No round 4 is dispatched.**
- **The bytes are not confirmed.** This record and the marks move the
  package's directory digest away from the value above; the reviewed bytes
  stay retrievable at the reviewed commit. This record recommends nothing
  on any of the packet's questions.

**What the round confirmed.** All twelve round-2 findings are repaired in
the bytes; the term sweep (1,883 / 151 / 438), the static sweep (962 / 52
at `09c7a61d`, 686 / 39 at `59fbf787`) and the partial application probe
reproduce; every anchor, digest and quotation checked is exact (raw lines
312–316).

| # | Level | Finding (short) | Raw line | Disposition |
|---|---|---|---|---|
| 1 | revise | Under the packet's own reading that "the governed plane" stays the observed project's own plane (lines 300–304), a dismissal (d2) places in the observing project's `.syzygy/**` either never takes effect, or takes effect and is the violation VIS-6 names ("a dismissal taking effect without living in the governed plane"); the packet, which recommends adopting (d), does not say which | 193 | **Open for the owner.** Raw's repair, one of: say in (d2), or in §1 (d) with an owner arm, whether such a dismissal takes effect and, if it does, reconcile it with VIS-6 and `trust-and-evidence.md` lines 42–43; drop "a dismissal" from (d2)'s examples and leave P-71-Q5's route; or ask the owner in a Q-D2 beside Q-D1. |
| 2 | note | Repaired (e) keeps residues of its trust-floor placement: the "(vision.md VIS-7)" citation, an unscoped "a claim resting only on such records", and a heading wider than the rule | 247 | **Open.** Cite the line-60 trigger's section or no rule; write "such a claim"; say in §1 (e) whether the other triggers may rest on self-observation. |
| 3 | note | (a)'s "never a claim" is unscoped in time, while Q-C3's rationale relies on RFC7-21's adoption path | 270 | **Open.** "While it is that draft" would carry the intended reading. |
| 4 | note | Ledger §4 says none of the 13 new readers is a D8 reader, but `gate-acts.test.ts` line 298 reads the doctrine `README.md` whose glossary packet §9 step 3 edits; the probe does not exercise that edit | 283 | **Open.** Correct the sentence and say beside the probe that the glossary edit is unprobed. |
| 5 | note | Register row P-102 still states Q1's pre-repair rationale | 297 | **Dispositioned outside the package.** The register is not a package file. Row P-102's Q1 sentence is marked at the sentence there, dated, with the old text kept: the packet's Q1 reason is now that RFC7-20 already decides the rendering on Polaris, as an `editorial-draft`. |

**Stale sentences outside the package.** Register row P-102 and
`docs/README.md`'s D8 row are updated directly.
