# Round 3 dispositions — D8 doctrine amendment packet

> **Candidate — binds nothing.** The record of how each round-3 finding is
> classified. Nothing in the package is repaired here: every finding is
> open for the owner. A disposition is not a confirmation.
> *(Marked 2026-10-14, cycle 3: "Nothing in the package is repaired here:
> every finding is open" is no longer true. The owner ruled on finding 1
> and directed one more cycle; every finding was repaired once; see
> §"Repairs, 2026-10-14 (cycle 3)" below. **Round-3 findings repaired once
> on 2026-10-14, unconfirmed pending round 4.**)*

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

*(Marked 2026-10-14, cycle 3: the first two bullets are no longer true.
The owner then answered finding 1 and directed one more cycle for P-102
in the lead session: "Drop dismissal from (d2)" — "Dismissals of an
observed-only project's gaps can't live in the observing project's tree,
so VIS-6 stays intact. Then one more cycle." [Observed: as relayed by the
lead session to this repair lane; not yet recorded under `decisions/`.]
The package was repaired once (below), and a round 4 is briefed in
`REVIEW-BRIEF.md` §"Round 4". The bytes are still not confirmed.)*

**What the round confirmed.** All twelve round-2 findings are repaired in
the bytes; the term sweep (1,883 / 151 / 438), the static sweep (962 / 52
at `09c7a61d`, 686 / 39 at `59fbf787`) and the partial application probe
reproduce; every anchor, digest and quotation checked is exact (raw lines
312–316).

| # | Level | Finding (short) | Raw line | Disposition |
|---|---|---|---|---|
| 1 | revise | Under the packet's own reading that "the governed plane" stays the observed project's own plane (lines 300–304), a dismissal (d2) places in the observing project's `.syzygy/**` either never takes effect, or takes effect and is the violation VIS-6 names ("a dismissal taking effect without living in the governed plane"); the packet, which recommends adopting (d), does not say which | 193 | **Open for the owner.** Raw's repair, one of: say in (d2), or in §1 (d) with an owner arm, whether such a dismissal takes effect and, if it does, reconcile it with VIS-6 and `trust-and-evidence.md` lines 42–43; drop "a dismissal" from (d2)'s examples and leave P-71-Q5's route; or ask the owner in a Q-D2 beside Q-D1. *Repaired 2026-10-14 (cycle 3), below.* |
| 2 | note | Repaired (e) keeps residues of its trust-floor placement: the "(vision.md VIS-7)" citation, an unscoped "a claim resting only on such records", and a heading wider than the rule | 247 | **Open.** Cite the line-60 trigger's section or no rule; write "such a claim"; say in §1 (e) whether the other triggers may rest on self-observation. *Repaired 2026-10-14 (cycle 3), below.* |
| 3 | note | (a)'s "never a claim" is unscoped in time, while Q-C3's rationale relies on RFC7-21's adoption path | 270 | **Open.** "While it is that draft" would carry the intended reading. *Repaired 2026-10-14 (cycle 3), below.* |
| 4 | note | Ledger §4 says none of the 13 new readers is a D8 reader, but `gate-acts.test.ts` line 298 reads the doctrine `README.md` whose glossary packet §9 step 3 edits; the probe does not exercise that edit | 283 | **Open.** Correct the sentence and say beside the probe that the glossary edit is unprobed. *Repaired 2026-10-14 (cycle 3), below.* |
| 5 | note | Register row P-102 still states Q1's pre-repair rationale | 297 | **Dispositioned outside the package.** The register is not a package file. Row P-102's Q1 sentence is marked at the sentence there, dated, with the old text kept: the packet's Q1 reason is now that RFC7-20 already decides the rendering on Polaris, as an `editorial-draft`. *Re-read 2026-10-14 (cycle 3), below.* |

**Stale sentences outside the package.** Register row P-102 and
`docs/README.md`'s D8 row are updated directly.

## Repairs, 2026-10-14 (cycle 3)

On the owner's cycle-3 direction of 2026-10-14 (quoted above), each
finding was repaired once, notes included. Every clause text and line
number below was re-read from the file at `origin/main` `7460aec8` (this
branch's base), not copied from the raw. At that commit the three
doctrine files still hash to the sha256 values in packet §1. "Packet" is
`OWNER-DECISION-PACKET.md`.

| # | Repair |
|---|---|
| 1 | **The owner's ruling applied: the dismissal is dropped from (d2).** The (d2) bytes now read "content Syzygy authors about such a project — a promoted annotation, an attributed answer — is committed out to the `.syzygy/**` of the observing project … is never cited as the project's text, and never suppresses a gap of the project. A dismissal of such a project's gap is not committed there: it takes effect only in the project's own governed plane, so it waits for an act that names that write." Beyond dropping the example, two changes are disclosed in the packet's dated note under the block: "a promoted note" became "a promoted annotation", because VIS-6(a) promotes a note "as an annotation or a dismissal"; and the general phrase "content Syzygy authors" would still have covered a dismissal, so the last sentence excludes it in words and states **where such a dismissal can lawfully live: only in the observed project's own governed plane**, as `trust-and-evidence.md` lines 42–43 and VIS-6's violation sentence already require, reachable by an act naming that write (today P-71-Q5's route). "Never suppresses a gap" stops a record not called a dismissal from doing a dismissal's work. Restated to match: packet §1 (d)'s "It is a governed project" paragraph (the second destination takes no dismissal), the SDR-30 caution (one example, the annotation, names an entity), the offboarding sentence, the P-71 trade-off paragraph (a drafted act that would dismiss an observed project's gap is not made describable in the observing tree), the no-change arm, §2's (d) row (no (d2) record renders `dismissed-by-decision`), Q-C2's premise and Q-D1's premise; the delta's (d) meaning and its VIS-6 "does not change" bullet. No owner question was needed beyond the ruling. |
| 2 | Clause (e)'s bytes: the "(vision.md VIS-7)" citation is dropped (the denial qualifies line 60's trigger in its own section); "a claim resting only on such records has no evidence, and renders Unknown" became "such a claim, resting only on such records, has no evidence and renders Unknown", scoped to the denied kind; and the heading "Self-observation never self-certifies" became "Self-observation never certifies Syzygy's own alignment". The section heading of §1 (e) follows. §1 (e) now says the other triggers — a green badge about Syzygy (line 59) or a Syzygy gap "factually resolved or absent" (line 63) — may still rest on self-observation records, as the drafter intends [Inferred], and **Q5 gains an arm**: widen the denial to every status-claim trigger about Syzygy (not drafted). The delta's (e) meaning and its "cites VIS-4, VIS-6 and VIS-7" sentence are repaired and marked. |
| 3 | Clause (a)'s bytes: "where it is that draft and never a claim" became "where it is that draft and is no claim while it stays one", so RFC7-21's adoption act may later make the draft curated narrative with Inferred claims (RFC7-2(c)), which Q-C3's rationale relies on. A dated note under the block says the freshness and withdrawal sentences bind the draft as a rendered object on such a surface. The delta's (a) meaning follows. |
| 4 | Ledger §4: the sentence "every doctrine file they name is `security.md` or `v1.md`" and "none of them is a D8 reader" is marked at the sentence: `packages/polaris-dossier/src/gate-acts.test.ts` line 298 reads the doctrine `README.md` live (re-read at `7460aec8`; a fixed-string `git grep` for `doctrine/README` over the 13 files returns that one line), packet §9 step 3 edits that README's glossary, the test should stay green because it hashes live bytes [Inferred: not run], and the glossary edit's battery effect is **unprobed**. Packet §9 step 3 says the same. **The application probe was also re-run over the cycle-3 bytes** at `7460aec8`, because (a), (d2) and (e) changed: baseline 100 commands, 0 nonzero; applied 100 commands, 6 nonzero, the same six commands and messages as before; VIS-7 now moves from line 250 to 260 (ledger §4, dated mark). |
| 5 | Register row P-102's Q1 sentence was marked at the sentence on 2026-10-14 after round 3 (row cell, "marked 2026-10-14, round 3"); re-read at `7460aec8` and left as marked. The row's later cycle-3 mark adds this repair's outcome and the renamed clause (e). |

**Also repaired: the D7 ledger disagreement this ledger routed.** Ledger
§5 item 4 is marked at the sentence: D7's cycle-3 repair, landing with
this one, corrects its recorder row and adds D7 Q6 beside Q-A1. Packet
§8's "Shared gate" bullet and Q-A1's cell name D7's Q6.

**What was not changed.** Clauses (b), (c), (d1) and (f), the change
classes, the recommendations on Q1–Q6, and every owner question other
than Q5's added arm. The round-1, round-2 and round-3 raws are not
edited.
