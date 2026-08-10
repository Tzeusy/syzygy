# Final foundational-contract acceptance record — final pre-specification package

This record defines the owner gates over the final pre-specification
package and, on the owner's act, supersedes
`_bootstrap/rfc-phase/FOUNDATIONAL-RFC-ACCEPTANCE-RECORD.md` (rev9) as the
acceptance authority. **Nothing adopts implicitly**: each gate below is
independent, none implies another, and no artifact rides on another's
gate. Until an act is performed, every artifact here binds nothing
(RFC3-16).

**Restructured at round-2026-08d (owner work order §4):** the single act 1
over the whole contract package is replaced by **six wave acts**, each
independently acceptable, each binding exactly the modules in its
generated wave manifest (`wave-manifests/`, written and partition-checked
by `scripts/build_active_manifest.py`). Design rationale:
`round-2026-08d/ACCEPTANCE-WAVE-DESIGN.md`. Acts 2–5 are unchanged.

## 1. The gates — exact scope, exact phrases

| # | Act (exact phrase) | Accepts exactly |
|---|---|---|
| A | `ACCEPT FOUNDATIONAL WAVE A: 8972d9630b95f5d4266432dbb1b3602114576bbd6c0f29d6f9bd6f905b1f884a` | The 19 modules of RFC 0001–0006 (kernel, evidence, storage, admission, cross-surface selection) at the per-module sha256 digests in `wave-manifests/WAVE-A-MANIFEST.txt`, whose own digest is the act's argument. Every `depends_on` edge of these contracts stays inside the wave. **Argument regenerated three times in round-2026-08e, by script each time** — for the RD-26 repair batch (seven modules; delta: `round-2026-08e/WAVE-A-SEMANTIC-DELTA.md` §13), retiring `6b98e0c6…`; for the RD-30 batch (RFC2-19(a) minted; delta §14), retiring `8af6805f…`; and for the RD-31 batch (RFC3-2/RFC3-15 two-trigger alignment and provenance safeguard, the RFC-0002 index's sub-clause declaration, RFC1-7's P-28 marker, the RFC-0004 dependency correction; delta §15), retiring `c649143b…`. **All three earlier arguments are stale and satisfy nothing.** RD-31 reviewed `c649143b…` and returned `VERDICT: REVISE`; **RD-31b reviewed the current argument `8972d963…` exactly and returned `VERDICT: CONFIRM` (2026-08-10; raw at `round-2026-08e/reviews/RD-31b-wave-a-RAW.md`)** — the offer is now withheld solely by §7 item 11, until P-33 is ruled *(review-state corrected 2026-08-10, RD32b-N5 — the row still said "awaits RD-31b" after RD-31b had delivered)* |
| B | `ACCEPT FOUNDATIONAL WAVE B: 193e3c1e15e4b1375f938d62c9e8c1a442984313e0794ada5965d2cdf9d7e3ed` | The 11 modules of RFC 0007–0009 (Polaris, Trajectory, Orrery) per `wave-manifests/WAVE-B-MANIFEST.txt`. Depends on Wave A. **Argument regenerated four times in round-2026-08e, by script each time** — for the wave-wide repair batch (all eleven modules; delta: `round-2026-08e/WAVE-B-SEMANTIC-DELTA.md`), retiring the round-08d argument `daa6a5dd…`; for the RD-27 batch (seven modules — delta §11's own "Modules touched (7 of 11)"; this row said "four" until 2026-08-10, RD32b-N3), retiring `2041ad05…`; for the RD-32 batch (RFC9-43's enumeration restored to the full RFC6-17 set, the P-38/P-22 in-place markers; delta §12), retiring `c0fd0e27…`; and for the RD-32b batch (the aggregation-attribution entry routed into RFC9-47's release-gate list per RFC9-47(a) part 1, RFC7-37's drift-prone gloss deleted; delta §13), retiring `052acfb8…`. **All four earlier arguments are stale and satisfy nothing.** RD-32 reviewed `c0fd0e27…` and RD-32b reviewed `052acfb8…` — both returned `VERDICT: REVISE`; the current argument awaits its fresh exact-package review (RD-32c) before any offer. The pre-repair row's reliance caveat is retired with them: after the RFC9-8(a) re-grounding, every normative reliance lands inside Waves A+B (RD-27 §4, confirmed by sweep) — lawful stated at the act. **Performed alone — before act 1 — this act binds eleven surface contracts whose operative predicates (11 of 11 modules' `depends_on`; 763 RFC 0001–0006 clause citation tokens — `RFC[1-6]-\d+` swept over the 11 manifest modules at the RD-32b rebind, 2026-08-10, replacing an unreproducible "1,067" per RD32b-N4 and rule 3) resolve into unaccepted Wave A candidate text: lawful only stated at the act, and the offer path is A → B** (RD32-M2; the register's P-1 row states the same ordering) |
| C1 | `ACCEPT FOUNDATIONAL WAVE C1: a5d3ba1f22ad0ff5ff66485b1829e5b2f652a8c7678dcc96699eaca4ac5b2b4d` | RFC-0011 module 1 (packet identity, provenance, memory — RFC11-1..3, 5..10, 12) plus the package index, per `wave-manifests/WAVE-C1-MANIFEST.txt`. Declares `depends_on` RFC-0010 (waves D1/D2): recommended after them. Module 1 uses *mandatory context* as a primitive whose defining clause is RFC11-4 in Wave C2; performed alone, the packet contract binds identity, immutability, execution-record binding, the fail-closed Unknown rule, governed memory and profiles, while the criterion separating a packet's mandatory core from its suggested additions is not yet fixed — lawful only stated at the act. Performing C2 in the same sitting removes the condition |
| C2 | `ACCEPT FOUNDATIONAL WAVE C2: acd27bb8f9b7be76725057b4280e2dc9fe23f3e9fac17c448542b9cb250d8b1a` | RFC-0011 module 2 (deterministic selection and budget posture — RFC11-4, 11, 13..16), per `wave-manifests/WAVE-C2-MANIFEST.txt`. Depends on C1 (the module consumes module 1's packet primitives throughout) and declares `depends_on` RFC-0010 (waves D1/D2) in its front matter — performed before them, it binds text whose reliances point at candidate material, lawful only stated at the act. Carries its own external criterion: acceptable only when its selection rules reproduce the blind golden fixtures (`fixtures/`), a derivation the fixtures' task/answer boundary exists to allow — and that criterion's pass/fail standard is itself an open owner question (**P-29**): until it is ruled and the standard exists, this row's condition cannot be discharged |
| D1 | `ACCEPT FOUNDATIONAL WAVE D1: 570e617091bb41d8b34ca17b09e12f41d22e4d592a23249c8a737a698f8c0dff` | RFC-0010 modules 1, 2, 3, 5 (mission identity/approval/lifecycle; envelope/attention; budget reservation; portfolio/consent) plus the package index, per `wave-manifests/WAVE-D1-MANIFEST.txt`. Even accepted, RFC10-24 holds every mission in `awaiting-approval` until the D3 question (act 5) is ruled — this act is never an operating license |
| D2 | `ACCEPT FOUNDATIONAL WAVE D2: ab590e3e553a2f1f2db92d1c676a0fd5c05d2283548163e5c3663df5a31382d8` | RFC-0010 module 4 (effects, recovery, stop — the correction plane), per `wave-manifests/WAVE-D2-MANIFEST.txt`. The plane both 2026-08-07 `REVISE` reviews concentrated on; the round-2026-08d rewrite repairs their findings and awaits its own fresh confirming review — see the wave-history note below |
| 2 | `CONFIRM CRAFT AMENDMENT: CC-TEST-2@7a716090bc827121b3f70c4f7e252fc5680cd8a56d7b4121b70f3673489690a0` | The craft cluster is committed and owner-approved (D2); only this amendment needs confirming. **Digest re-quoted 2026-08-06** — `th-engineering` was vendored in-tree and re-pinned (owner override, closing P-26), and `testing-and-verification.md` gained CC-TEST-7 recording the resulting re-check (no conflicts found); the retired, `aa2d6353…`-then-`3858820f…` arguments satisfy nothing. Earlier: **re-quoted 2026-08-05** — the nine canonical files' banners were corrected (P-7/SD-3, rule text byte-unchanged), so the rev9 argument `aa2d6353…` was stale and satisfied nothing |
| 3 | `ACCEPT TOPOLOGY: 568a6f17659af770a5f052922b10299fceb564cc4601b65d5c5a3c13d9dba096` | The nine topology files at the per-member digests in `../../../map/topology-candidates/BUNDLE-MANIFEST.md`, whose own digest is the act's argument. **Digest re-quoted 2026-08-10** — topology `README.md` presented the retired rev10 phrase as the current acceptance gate (launch-gate pilot C1; the same defect class P-6 repaired for the rev9 phrase in this same file); the sentence is now phrase-free so a future retirement cannot recur here. **Re-quoted again 2026-08-10 (RD-25)** — the manifest's verify instruction named `topology/`, a directory that exists in no clone before act 3 (RD25-07 — the recurrence of the defect class this step corrected on 2026-08-05), and the topology README cited a founder-local fix report that never travelled (RD25-08); both sentences repaired, seven members byte-unchanged. The `3d8f75da…`, `7a3b2249…` and rev9 `0d34d1b5…` arguments are stale and satisfy nothing. Earlier: **re-quoted 2026-08-05** — the rev9 retired phrase and draft/proposed vocabulary corrected (SD-2, SD-10) |
| 4 | `ADOPT PROJECT OVERVIEW: a975fb96159042b43b4ddc147301aff44e839e618bc5a815261aa882e136f9c0` | `.syzygy/intent/OVERVIEW.md` at that digest. **Digest re-quoted 2026-08-10b (RD29-08)** — the header now states the act is unperformed and the page a draft until it is (the cold reader previously had no candidate marking on the designated human entry); the prior `e5d6910a…` argument is stale and satisfies nothing. Earlier same day: **re-quoted 2026-08-10** — the round-2026-08e vocabulary repair (R-OVW batch: the OVERVIEW's advanced-vocabulary findings from RD-16, verified to zero CG-23 hits over all 20 registry terms) moved the overview's bytes; the retired `01d62951…` argument satisfies nothing. Earlier: **re-quoted 2026-08-05** — the overview was refactored to four-layer progressive disclosure and its authoring-time status section removed (P-13/SD-9); the rev9 argument `42de2eb1…` is stale and satisfies nothing. **Re-quoted again 2026-08-05b** — the overview was rebuilt to a default layer plus two collapsed drawers, the frozen gate-state table was removed in favour of a pointer to `PROJECT-STATUS.md`, and the machine query plane was restored to the consumer list; the retired argument `ce7794fd…` satisfies nothing |
| 5 | Doctrine amendment **D3** (bounded mission) — VIS-4 owner adoption, no magic phrase | `DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` (**rev1**, 2026-08-05) and its two verbatim insertions. Rev1 supersedes `…-DRAFT.md`, whose `vision.md` insertion cannot be applied as written (SD-8). **Optional**: RFC-0010/0011 do not depend on it. Recommended ordering: perform Waves A, B, D1 and D2 before act 5 — Wave A binds the mission extension profile (RFC1-7) and the D waves bind the mission vocabulary D3's terms would otherwise leave defined only in unaccepted contracts *(this guidance previously said "perform act 1 before act 5", naming the retired all-in-one gate — RD-20 M5)* |

**Wave-history note — read before any wave act.** The retired all-in-one
offer closed with the 2026-08-07 review pass — **eight independent
reviews, every verdict `REVISE`** — two of which concentrated on one
shared structural defect (RFC10-17's budget invariant stated over the
ledger while RFC10-10 demands prevention over consumption), left
unrepaired then so the reviews stayed bound to their bytes. **Round
2026-08d performed the repairs**: RFC-0010 was split into the five-module
package waves D1/D2 now bind, its budget module rewritten (six-quantity
accounting, enforced-limit admission at the RFC5-21 launch gate and the
RFC5-15 transmission predicate), the effects/recovery/stop module rebuilt
against reviews RD-1/RD-1b's blocking findings, and RFC-0011 split and
amended (RFC11-13..16). **The round-2026-08d fresh-context review pass
then ran over those bytes (commit `771965c`): fifteen reviews — nine
dimension, six wave exact-package — and all fifteen returned `REVISE`,
zero `CONFIRM`** (verdicts:
`round-2026-08d/reviews/DELIVERY-AND-VERDICT-REGISTER.md`; dispositions:
`…/DISPOSITION-REGISTER.md`). A `REVISE` review is a verdict against
binding, not for it: **no wave act may be offered or performed until that
wave's repairs land, its manifest is regenerated by script, and a fresh
confirming review is bound to the new argument** — or the owner knowingly
binds the findings at the act. The round-2026-08e repair pass executes
the Wave A and Wave B batches under the owner's Capability 1 launch
direction; Waves C1/C2/D1/D2 are visibly deferred
(`DEFERRED-WAVE-POSTURE.md`). Semantic deltas:
`round-2026-08d/` and `round-2026-08e/` (work orders, wave design, and
the rounds' delta records).

**Acceptance schedules no implementation.** Accepting these contracts
clears specification authoring only: every active contract carries a
binding phase-rule clause (RFC1-33, RFC2-26, RFC3-33, RFC4-30, RFC5-27,
RFC6-28, RFC7-38, RFC8-32, RFC9-52, RFC10-16, RFC11-12), and every
user-observable behavior still routes through an owner-approved OpenSpec
requirement before any implementation work is scheduled.

Rework/rejection, per wave:

```text
REWORK FOUNDATIONAL WAVE <A|B|C1|C2|D1|D2>: <reason>
REJECT FOUNDATIONAL WAVE <A|B|C1|C2|D1|D2>: <reason>
```

**Two phrases are retired and satisfy nothing.** The rev9
`ACCEPT FOUNDATIONAL RFCS` phrase was retired unconditionally at rev10
delivery — a retirement notice is written into the rev9 record itself,
because supersession of an authority must not be conditional on exercising
the authority that supersedes it, and the rev9 phrase (which carries no
digest argument) cannot self-identify which corpus it would bind. The
rev10 phrase `ACCEPT COMPACTED FOUNDATIONAL RFCS` (last argument
`2862b2f5…`, with the six earlier retired arguments its row recorded) is
**retired at round-2026-08d delivery on the same rule**: the wave acts
supersede it, and an offer superseded must not remain performable beside
its successor. The rev9 corpus is preserved as history
(`history/rev9-rfcs/`), not offered for acceptance; acts 2–4 continue
under this record's §1 rows at unchanged digests.

## 1a. Revision of 2026-08-05 — retained as history of the retired offer

*This section describes the retired all-in-one act 1 and its 2026-08-05
re-quote; it is retained because a reader of an earlier revision needs to
find what happened, and its digests are all retired values.* This record
was authored at rev10 (2026-08-03) and **re-quoted at the close
of the human-clarity refactor round (2026-08-05)**. Every one of the four
digest-bound arguments then in §1 changed during that round, because the
round corrected defects inside three of the four digest sets:

| Act | Prior argument (retired) | Cause of change |
|---|---|---|
| 1 | `08793ddf…` | retired acceptance phrase removed from `rfcs/RFC-0003/governance-homes-and-owner-acts.md`; RFC-0007 README self-counts and edge count corrected; RFC-0010/0011 §6 headings no longer promise absent history files (SD-1, SD-10) |
| 2 | `aa2d6353…` | the nine canonical craft files' false "bootstrap-phase record" banners corrected; **no rule text changed** (SD-3) |
| 3 | `0d34d1b5…` | retired acceptance phrase and draft/proposed vocabulary corrected in topology `README.md` (SD-2, SD-10) |
| 4 | `42de2eb1…` | the overview was refactored to four-layer progressive disclosure and its authoring-time status section removed (SD-9) |

Each change is recorded as a semantic delta in
`round-2026-08/SEMANTIC-DELTAS-THIS-ROUND.md`; all four manifests were
regenerated **by script**, never hand-transcribed. The round's eight
independent reviews are stored verbatim in `round-2026-08/reviews/`, and its
dispositions — including what was knowingly *not* fixed — in
`round-2026-08/ROUND-DISPOSITIONS.md`.

**Before performing any act, verify its argument mechanically:**

```sh
python3 scripts/check_governance.py      # CG-7a..7e cover every wave and act
```

A CG-7 failure means the artifact moved after this record was written: **do
not perform that act** — regenerate, re-review, and re-offer. This is the
same rule §2 step 2 states; the round added the machine check because three
of the four acts had no check at all until 2026-08-05.

## 2. The acceptance transaction — honest under RFC3-16(c)

Each act is a chat-phrase ceremony executed in five steps — preceded by
one reading obligation:

0. **Read §7 first** *(step added 2026-08-10, RD30-05)*. §7 is titled
   "items requiring explicit owner attention at the gate" and lists what
   each act ratifies beyond its digest — drafted arms, disclosed rulings,
   open questions riding in. An act performed without §7 read is the
   surprised act this record exists to prevent; no phrase before it.

1. **The phrase.** The owner writes the exact phrase from §1.
2. **Digest verification, by script.** The lead re-verifies the bound
   digest(s) against the working tree: for a wave act, `sha256sum -c
   wave-manifests/WAVE-<X>-MANIFEST.txt` run from the candidates root,
   then the wave manifest's own digest against the phrase; additionally
   `python3 scripts/build_active_manifest.py --check` proves the wave
   manifests are the generator's current output and still partition the
   package. Any mismatch means no act: regenerate, re-review, re-offer.
3. **Installation, bytes unchanged.** A wave act installs its manifest's
   modules (with their package directory structure) to
   `.syzygy/governance/contracts/rfcs/` and its wave manifest to
   `.syzygy/governance/contracts/wave-manifests/` — the RFC3-15
   `contracts/` home, created at the first wave act; the first wave act
   also installs `ACTIVE-CONTRACT-MANIFEST.txt` beside it as the package
   identity record (updated in place by later regenerations only through
   re-offer, never silently). The copy is digest-verified by running
   `sha256sum -c wave-manifests/WAVE-<X>-MANIFEST.txt` **from
   `.syzygy/governance/contracts/`**. Acts 2/4 bind content already
   committed at canonical homes; act 3 copies the nine bundle members from
   **`.syzygy/map/topology-candidates/`** — their tracked home, present in
   every clone — to `.syzygy/map/topology/`, verified by the bundle
   manifest's own `sha256sum -c` block run from the installed directory.
   (`.syzygy/map/` already exists as the candidates' parent; act 3 creates
   the `.syzygy/map/topology/` home inside it, and does **not** delete
   `topology-candidates/` — retirement of the candidate home is a separate,
   later cleanup, so a failed act leaves the source intact.) Installation is
   a copy, never an edit. **Corrected 2026-08-05:** this step previously
   named a source path `topology/` that exists in no clone and never
   existed in the tracked package; the ceremony was unexecutable as
   written. `check_governance.py` CG-14 now resolves every act's install
   source and destination so this class of defect fails a check rather than
   waiting for a reader.
   **Companion material, installed but not accepted:** the first wave
   act's install also copies `history/` and `matrix-rows/` to
   `.syzygy/governance/contracts/history/` and `…/matrix-rows/` so the
   modules' Tier-2 rationale backlinks and the RFC-0003 README's
   census link resolve from the governed tree. These directories are
   **non-normative** (their own README states "Nothing in this directory
   binds"), sit outside every act's accepted digest set, and carry no
   authority — each wave act binds exactly its manifest entries, nothing
   else.

   **The RD-7 pointer finding, and its repair.** Review **RD-7** simulated
   the rev10 install exactly as documented and swept the installed
   modules: **81 relative backlinks examined, 12 unresolved, of which 8
   broke as a direct consequence of the act** — six package READMEs point
   two levels up at the context budget report, and one points two levels
   up at the 03 compaction report, targets the install did not copy.
   **Repaired at round-2026-08d in the ceremony, not the modules**: the
   first wave act's install additionally copies
   `CONTEXT-BUDGET-REPORT.md` and
   `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md` to
   `.syzygy/governance/contracts/` — both non-normative generated
   reports, outside every digest set, carrying no authority — so the
   backlinks resolve where they land. The repair is verified by
   simulation, not asserted:
   `round-2026-08d/POST-INSTALL-LINK-REPORT.md` re-runs RD-7's sweep
   against the current bytes with the copy in place and records the
   remaining unresolved population with its denominator. `CG-14` still
   checks install *routes* only.
4. **The owner-act record.** A dated entry quoting the exact phrase and
   digest is appended to
   `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` (created at
   the first act) — committed and clone-visible.
5. **One commit and an annotated tag** containing the installed content
   and the act record. This is the last *required* step: after it, the act
   is complete and fully recorded in the tracked tree.

   On the founder machine only, the SHA is then mirrored to
   `_bootstrap/state/FOUNDER_DECISION_LOG.md` (process mirror only —
   CT-027's rule). **That mirror is not part of the ceremony.**
   `_bootstrap/` is git-excluded and absent from every clone, so a step
   that required it would make the ceremony unexecutable by anyone but the
   founder — which is the defect this round exists to remove. Skipping it
   loses nothing an act depends on.

**What that record is, and is not (RFC3-16(c) — the two-state model).**
The committed act record establishes an **owner-adopted bootstrap act**: a
human/social governance fact preserved as phrase + exact digest +
commit/tag, from which effective status *for human governance* is read.
The owner and the humans working with them lawfully govern development by
it. The license has a machine-side complement, stated here so the
acceptance is knowing: until the correlation act, a state-(1) record
satisfies no machine-enforced authorization gate. Artifacts consumed as
**constraints** (contract clauses, doctrine rules) bind at full strength —
refusing to apply a constraint over uncorrelated provenance would widen,
not narrow — but anything consumed as an **authorization for an effect**
(a consent, an autonomy envelope, a write-expanding policy) has not
satisfied the RFC3-16(a) predicate on a state-(1) record alone and
resolves under its effect rule, exactly as RFC10-9 leaves an uncorrelated
mission in `awaiting-approval`. It is **not** independent verification: every tree-resident record —
including this committed act record — lies within the untrusted actor
class's write reach, so Syzygy never claims the act is independently
verified. When the A1 correlation mechanism first exists, the owner
performs the **one-time recorded correlation act** (RFC3-16(b)) binding
each accepted artifact's exact digest to its historical act — upgrading it
to a **Syzygy-verified effective act** without editing anything. Until
then, every Syzygy-visible provenance render states the gap honestly:
**"owner-adopted (bootstrap, uncorrelated)" — never "verified"** (the A9
posture). **A git commit or tag alone is never sufficient for either
state** — it is evidence within a record, never the mechanism. Artifacts
are never edited after an act; an artifact edited after its act is, for
the record, an artifact with no act (RFC3-16(b) item 3).

**Retention before the act, stated honestly.** The package is **tracked**
and present in every clone, at `.syzygy/governance/contracts/candidates/`
(contracts, manifest, scripts, fixtures, reviews) and
`.syzygy/map/topology-candidates/` (the bundle). Nothing the ceremony needs
lives outside the clone: a collaborator with only `git clone` can recompute
every act digest and run every validation. Step 2 makes tampering
detectable, not recoverable, from this repository alone. From step 5 onward
the accepted content additionally sits at its governed home, tagged.

**Corrected 2026-08-05.** This paragraph previously stated that the package
"lives in the deliberately git-excluded `_bootstrap/` working tree plus the
delivered review packet". That was true when it was written and became
false when the package was tracked; it survived because nothing checked it.
The claim is retired rather than deleted, because a reader who saw the old
text needs to know it was wrong, not merely that it is gone.

## 3. Package identity

**Package identity.** `ACTIVE-CONTRACT-MANIFEST.txt` lists the sha256 of
each of the **39 active modules** and is the package's identity record; it
is **no act's argument** under the wave structure — the six wave manifests
it partitions into carry the arguments, and their current digests are
quoted only in §1. All seven manifests are written by
`scripts/build_active_manifest.py` (partition asserted on every run,
selftested); per-module digests are never hand-transcribed. Only edits
under `rfcs/` churn digests; fixes to this record or the reports do not.
§1 always carries the current wave arguments — `check_governance.py`
CG-7a/7b fail on any divergence.

**Clause inventory — read it from the verifier, never from here.**
`python3 scripts/verify_final_prespec.py` prints the count and every
per-module figure; **as of 2026-08-09 it reports 341 numbered clauses**, and
that line is the authority, not this one. The ranges are RFC1-1..33,
RFC2-1..26 (+1 lettered: RFC2-19(a)), RFC3-1..33 (+5 lettered, incl. **RFC3-16(c)**), RFC4-1..30 (+2),
RFC5-1..27, RFC6-1..28, RFC7-1..40 (+7), RFC8-1..32, RFC9-1..52 (+8),
**RFC10-1..24** (+3 lettered: RFC10-17(a), RFC10-18(a), RFC10-19(a)),
**RFC11-1..16**. Zero rev9 clauses merged, retired, renumbered, or routed out
(04-CLAUSE-MIGRATION-MATRIX). Nine contracts are packages (0002 ×4, 0003 ×2,
0004 ×4, 0005 ×3, 0007 ×2, 0008 ×3, 0009 ×3, **0010 ×5, 0011 ×2** modules +
README each); RFC-0001 and RFC-0006 are single files; RFC-0001 and (at
round-2026-08d, by the margin its owner-ordered RFC9-8(a) amendment added)
`RFC-0009/semantic-geography.md` are the justified-oversize modules
(justifications in the 03 report and the verifier's own table; current word
counts in `CONTEXT-BUDGET-REPORT.md`, both printed by the verifier).

> **Correction, 2026-08-07 (review RD-8, finding S2).** This paragraph said
> **322 numbered clauses** and **RFC10-1..16**, under the label
> *script-verified* — while the script reported **328** and RFC10 ran to
> **22**. The gap was exactly the six correction-plane clauses RFC10-17..22.
> §1's act-1 row narrated their addition; §3 — *the section a reader consults
> to learn what the package is* — was never swept. Two derived figures in the
> same section were stale the same way, and both are now replaced by pointers
> rather than refreshed: **a figure quoted outside its owning artifact goes
> stale silently**, which is this repository's third verification rule, broken
> here in the record that governs its own acceptance. *(Label correction,
> 2026-08-10 — RD-20 m6: this note called RFC10-17..22 "the six
> correction-plane clauses"; by the package's own clause map RFC10-17 is
> module 3, RFC10-18..20 module 4, RFC10-21 module 5, RFC10-22 module 2 —
> only module 4 is the correction plane. They are the six clauses the
> correction pass added, not six correction-plane clauses.)*

**Word accounting (03 report, honest form):** rev9 normative corpus
90,410 words, one mandatory reading path — a historical baseline, fixed.
**Every current figure lives in `CONTEXT-BUDGET-REPORT.md` and in
`verify_final_prespec.py`'s output; none is restated here.** The shape of the
rev10 change is: compacted normative text, plus package scaffolding, plus
READMEs, plus two new contracts, with Tier 2 history extracted. *(The "99,067
on disk" total this paragraph used to carry was stale against the verifier's
own figure — RD-8 finding S2, same class as the clause count above.)*
**The owner's 35–50k corpus band was not reached** — nine independent
passes each hit an incompressibility floor at −12…−22% (arithmetic in
`WORKER-REPORT-DIGEST.md`). The optimization target it served instead:
measured per-task mandatory loads across the golden fixtures — **every
current figure lives in `CONTEXT-BUDGET-REPORT.md`, regenerated by its
script; none is restated here** *(the "10,854–18,302 words across five
fixtures" range this sentence used to carry was stale by roughly 2×
against the generated report's ten-fixture figures — RD-23 M3, the same
transcribed-derived-value class the §3 corrections above record)* — with
one disclosed risk-class exception (fixture 2).

## 4. Decisions and directions in force

- The **34 owner-decision identifiers** of the rev9 record §4 remain in
  force unchanged; the compaction preserved every decision text or moved
  it to history with a backlink (per-pass decision censuses in
  `matrix-rows/`). The three standing non-identifier rulings likewise.
- **New owner direction (this run):** OD-R10-1..7
  (`02-OWNER-DIRECTION-RECORD.md`) — Mission Control as platform
  capability; bounded-mission autonomy; compaction before acceptance; the
  Context Compiler; the two-state acceptance repair; the RFC 0009 split
  reversal; this gate. These are recorded directions, not doctrine; D3 is
  the only doctrine change proposed and it awaits act 5.
- One deliberate semantic resolution rode the compaction: RFC8-25's
  pre-B13 fallback retired as superseded (strictly stricter; history
  record carries the retired text). Confirmed by the semantic-equivalence
  review (§6).

## 5. Open questions at this gate

**27 open §8 questions** (21 carried from rev9 + 6 new in RFC-0010/0011)
plus the RFC9-9 follow-on item, each individually classified with a
stated reason in `08-OPEN-QUESTION-TRIAGE.md`: **1 to close at this
gate** (RFC 0003 §8 q4, `declarations/` — §7 item 1 below), 6 may remain
open before OpenSpec, 13 close before V0 implementation (incl. the
follow-on), 7 before Mission Control V1, 1 post-V1. RFC 0005 q1 (machine-client mechanism) is scoped in the contract
itself: it selects among RFC5-6-conforming mechanisms and blocks V0
implementation, not specification — accepting with it open is a
**knowing** deferral.

## 6. Verification and review state

- Mechanical: `scripts/verify_final_prespec.py` **PASS** (clause
  continuity incl. package disjointness/completeness, citation
  resolution, closed matrix vocabulary, phase-rule presence, fixture
  completeness, module ceilings); `scripts/build_contract_index.py
  --check` — no drift. All scripts derive their root from their own
  location and run from the delivered packet on any machine (directive
  §11).
- Fresh-context reviews (directive §13) over the compacted package — six
  independent reviews run 2026-08-02/03, raw reports stored verbatim in
  `reviews/` before synthesis, all findings dispositioned in
  `reviews/DISPOSITIONS.md`:
  1. **Transaction** (§13.5) — EXCEPTIONS, 5 findings: all fixed
     (record steps 2/3 repaired, topology bundle shipped in-packet, rev9
     phrase retired, RFC3-16(b) reconciling sentence).
  2. **Digestibility** (§13.2) — EXCEPTIONS, 4 + 4 nits: all fixed
     (install-at-act companion material, packet-reference rewording,
     `governance_sources` index section, scripted count refresh).
  3. **Boundary** (§13.4) — EXCEPTIONS, 9: all fixed (phase-rule
     forced into packets and READMEs, four rev9 limbs restored in
     RFC10-16/RFC11-12, routing-matrix tallies machine-recounted).
  4. **Portability** (§13.6) — EXCEPTIONS, 8 (2 blocking, both
     reproduction failures of stated mechanical claims): all fixed or
     disclosed (source-resolution logging, shell assumptions stated).
  5. **Safety** (§13.3) — EXCEPTIONS, 14 (6 blocking): all fixed in the
     conservative direction (RFC10-8/9 approval and decomposition
     semantics, RFC11-6 fail-closed default, RFC11-10 gate fields,
     RFC10-10 scoped MUST); owner consequences pinned in §7 items 6–9.
  6. **Equivalence** (§13.1) — 7 exceptions over 294+21 clause rows: all
     fixed (the RFC3-16 relaxation now stated plainly in the migration
     matrix; constraint/authorization split carried into RFC3-16(b)/(c)).
  After the consolidated fix batch, the §1 act-1 digest was regenerated
  to the now-retired `f2914fc5…`.
- **Final confirming review (2026-08-03): CONFIRM at the then-current,
  now retired manifest digest
  `f2914fc56cd2aa069b952747b9c78b00dc41d908830887ecd2f1addd37e61fc4`**
  — **this CONFIRM does not reach the corpus the owner would accept today.**
  **The manifest has been re-quoted six times since; §1's act-1 row is the
  count of record.** *(This sentence said "twice", and `PROJECT-STATUS.md`
  said "three times" — three incompatible counts across two files, one of
  them the acceptance authority. RD-8 finding S2. A count of one's own
  history is a derived value like any other, and it now has one home.)*
  **Review state per wave (2026-08-10): Wave A's current argument
  `8972d963…` carries RD-31b's `VERDICT: CONFIRM` — the one confirming
  review bound to a current argument; Wave B's current argument awaits
  RD-32c after RD-32b returned `VERDICT: REVISE`; no C/D argument
  carries any round-2026-08e review (deferred posture).** *(This
  sentence said "No CONFIRM verdict is bound to the current argument"
  until RD-31b delivered — corrected the same day, 2026-08-10,
  RD32b-N5. Review state first extended 2026-08-10, RD30-14 — the
  section previously narrated only the 2026-08-07 reviews.)* Three
  review passes have run since the rev10 offering: eight independent
  reviews on 2026-08-07 (every verdict `REVISE`); the round-2026-08d
  pass of fifteen fresh-context reviews on 2026-08-09 (nine dimension,
  six wave exact-package — every verdict `REVISE`, register at
  `round-2026-08d/reviews/`); and the round-2026-08e launch-closure
  fleet (RD-24 onward, register at
  `round-2026-08e/reviews/DELIVERY-AND-VERDICT-REGISTER.md`), whose
  per-wave exact-package chains — RD-31 → RD-31b for Wave A, RD-32 →
  RD-32b → RD-32c for Wave B — are the offer gates for the current
  wave arguments. The 2026-08-07 detail: every verdict was `REVISE`
  (raw report verbatim at `reviews/rev10-confirming-review.md`). It
  re-ran every mechanical check (all 32 manifest lines OK; verifier
  PASS; index no-drift), verified every spot-checked disposition in the
  final bytes, reproduced every numeric claim exactly (all five fixture
  loads and two packet digests byte-exact; §3 arithmetic; 322 clauses;
  all sibling-gate digests), and probed the fix batch for new
  contradictions (none found). Three residuals named, none blocking:
  **R1** — one stale self-count inside the digest set (§7 item 10, a
  knowing-acceptance item); **R2** — two §6 verdict labels softened a
  reviewer's verdict (corrected in this section, digest-stable, per its
  recommendation); **R3** — two malformed register rows (fixed,
  digest-stable). This record's §6 was corrected after the confirming
  review per its R2; the corpus bytes it bound are unchanged.

## 7. Items requiring explicit owner attention at the gate

1. **RFC 0003 §8 q4 — the `declarations/` category**: rule it (or
   knowingly ride the drafted default into the accepted digest). The
   default is load-bearing, not passive: RFC3-15's drafted text is a
   **six-name closed validator** ("accepts exactly these six names and
   rejects a seventh; neither rejecting `declarations/` nor admitting an
   unreserved directory is conforming"). The same act ratifies the P-18(a)
   seam: doctrine's architecture.md calls its four `governance/` categories
   "constitutional minimums", and a validator that rejects a seventh name
   is a closure, not obviously a narrowing — accepting RFC3-15 knowingly
   closes what doctrine floors (RD26-13).
2. **The [Inferred] SEC-3 extension** (workers' commits are untrusted) —
   ratify or amend into doctrine; carried unchanged from rev9.
3. **RFC 0005 §8 q1** — knowing deferral to V0 implementation (§5).
4. **D3** (bounded-mission doctrine clarification) — adopt, amend, or
   decline; RFC-0010 §2 states the consequence of declining.
5. **The corpus-size outcome** (§3): the 35–50k band was refused in favor
   of preservation; the acceptance of this record accepts that trade as
   presented in the 03 report.
6. **Mission approval is a runtime act — V0 consequence** (safety review
   S1, resolved conservatively in RFC10-9): a mission-approval act must be
   an A1-mechanism act (owner-attended, Syzygy-mediated, correlated to an
   audit trail outside `.syzygy/**`); a state-(1) bootstrap-shaped record
   never launches a mission. Consequence the owner accepts with the
   package: **Mission Control V0 must ship the approval ceremony and
   external audit trail as a hard precondition** — no interim
   tree-record-approved missions exist.
7. **Mission decomposition is off by default** (safety review S3, resolved
   in RFC10-8): agents mint child missions only under an explicit
   owner-approved decomposition grant in the parent envelope; the child's
   provenance is the parent's act plus a recorded derivation, its budget a
   reservation debited at grant time. If the owner wants freer
   decomposition, that is an envelope-design decision to make knowingly.
8. **D4 — the VIS-4 self-licensing question** (safety review): whether a
   bounded-autonomy doctrine amendment adopted through Syzygy's own
   ceremony is doctrine amending doctrine. The amendment draft states the
   position (it is an owner act like any other, VIS-4-gated) with the
   owner's overrule path; the ruling itself is the owner's.
9. **Single-source structure, disclosed** (safety review; rewritten
   2026-08-10, round-2026-08e — the X3 single rewrite; the previous text's
   "never cite" was false as worded). The measured position, swept this
   session over all **30 modules** of RFC 0001–0009 (Python `re`, tokens
   `RFC10-n`/`RFC11-n` plus the package names): **no clause of
   RFC 0001–0009 relies on RFC-0010 or RFC-0011.** Twelve citation hits
   exist, every one a non-reliance under verification rule 5: five phase
   clauses carry the `(Shape-parallel with …)` sibling list naming
   RFC10-16 and RFC11-12; RFC 0003's correlation text names RFC10-9 as
   *"the worked example"*; and RFC9-8(a) names RFC10-15 in a
   staged-successor parenthetical stating in-clause that it is *"a
   citation, not a reliance"* — after the round-2026-08e Wave B repair,
   the portfolio layout registry's home and gate are RFC3-15/RFC3-16(a),
   fully inside Waves A+B, and the fail-closed bar (no portfolio re-lay
   while no workspace-scope governance home exists) derives from
   RFC 0003's own silence plus RFC3-15(a)'s recorded-widening
   requirement, not from RFC-0010. (RFC-0005's front matter lists
   RFC-0010/0011 under `constrains:` — an outbound constraint edge, not a
   reliance.) The no-self-widening rule therefore has no restatement by
   reliance inside the nine earlier contracts; its reach into mission
   contexts is carried by RFC10-15/RFC11-4's loading rules when and only
   when those waves are accepted — until then the earlier contracts stand
   complete on their own text.
10. **R1 — CLOSED, and the item outlived its defect.** This item asked the
    owner to rule on a stale navigation count in `rfcs/RFC-0007/README.md`
    line 46, offering "accept as-is, or direct a fix + digest regeneration +
    one more digest-binding review." **The figure no longer exists.** The
    fourth re-quote removed every volatile measurement from six package
    READMEs; that line now says module sizes are deliberately not stated and
    points at `CONTEXT-BUDGET-REPORT.md`, and `2,268` and `10,578` each have
    **zero hits** across `rfcs/`. Review **RD-8** (finding S4) found the item
    still standing and named the shape of the harm precisely: an owner who
    chose the second branch **would have commissioned a review cycle over a
    string that is not in the corpus.** Retained, struck through, rather than
    deleted — an owner-attention item that was live and is not is part of this
    record's history, and silently removing it would leave a reader of an
    earlier revision unable to find out what happened to it.
11. **P-33 — the Wave A install shape** *(added 2026-08-10; RD26-01/RD26-02).*
    The ceremony's step 3 installs companion material and the act's own
    manifests into `governance/contracts/`, and RFC3-15 — bound by the same
    act — says that category holds accepted load-bearing contracts
    **exclusively**. P-33's packet
    (`decisions/WAVE-A-INSTALL-SHAPE-DECISION.md`) states it must be ruled
    **before Wave A is re-offered** and its own recommendation is the
    RFC3-15(a) recorded-widening route. **Until P-33 is ruled, this record
    offers no Wave A act** — performing act 1 over the current step 3 would
    freeze an install that breaches a clause the act binds.
12. **P-31 — the drafted RFC2-19(a) exemption arm** *(added 2026-08-10;
    RD26-02/RD26-06; re-keyed 2026-08-10, RD31-08 — the arm is the minted
    sub-clause RFC2-19(a)).* RFC2-19(a) is a drafted-awaiting-ruling
    sub-clause that
    exempts the `reconciliation-pending` rendering from RFC2-24's
    twelve-reason closure — candidate text the act would ratify. Rule P-31,
    or perform the act knowing it ratifies the drafted arm.
13. **P-37 — the shape-facet vocabulary** *(added 2026-08-10; RD26-02;
    corrected 2026-08-10, RD30-01).* P-37's packet names the Wave A act
    as its earliest required gate because RFC-0006 is in this wave — but
    **the seven-facet vocabulary itself is in no Wave A byte** (RD-30's
    sweep over all 30 A+B modules found the facet names in zero contract
    modules). What the act ratifies is the anti-rollup ground the facets
    ride on (RFC6-18/19 as amended). The vocabulary needs P-37's ruling
    **plus a drafting site** — an RFC-0006 amendment before this act, or
    the Capability 1 spec — and an earlier form of this item wrongly said
    the act settles it. Rule P-37 before the act so the site is chosen
    knowingly.
14. **Two drafted repairs ratified by this act** *(added 2026-08-10;
    RD26-04/RD26-05).* (a) RFC3-15's `records/` cell now admits the
    pre-declared deterministic challenge-sweep's expiry-resolution record —
    the widening that makes RFC2-13's owner-decision-B1 resolution act
    recordable at all (as repaired after RD-31: RFC3-2's transition rule
    states the same two triggers, and the record's authority is the
    resolving policy's RFC3-16(a) provenance, never the record's own
    say-so); (b) RFC4-19's `terminal outcome` row now carries §8
    q2's proposed answer (`unknown-terminal` as a legal Syzygy-side value,
    keeping vanished-worker runs admissible). Both are candidate drafts in
    the bytes the act binds; the act ratifies or the owner reverts them.

15. **RFC7-39's entry-identity ruling** *(added 2026-08-10; RD27-02(a)).*
    The round-2026-08e repair pass drafted a substantive answer inside
    RFC7-39: the fixed entry **is** the project's primary narrative
    (RFC7-6) — "there are not two front doors". The pass's own delta
    (`round-2026-08e/WAVE-B-SEMANTIC-DELTA.md` §10.3) concedes the owner
    may prefer the other design (a thin index entry distinct from the
    narrative). The Wave B act ratifies this identity or the owner reverts
    it; the question is carried on P-38's packet
    (`decisions/HUMAN-ENTRY-DECISION.md`), which is the gate path.

16. **P-28 — the drafted mission extension profile** *(added 2026-08-10;
    RD30-03).* RFC1-7 carries a drafted `mission` extension profile
    (option (b) of P-28, drafted at round-08d per the owner work order)
    and RFC10-4 grounds Mission identity in it. RFC-0001 is a Wave A
    module: **accepting Wave A ratifies the profile.** Rule P-28, or
    perform the act knowing the profile rides in; packet 5 of
    `round-2026-08d/OWNER-DECISION-PACKETS.md` carries the alternatives.

17. **P-22 — the RFC9-8(a) registry placement** *(added 2026-08-10;
    RD30-03).* RFC9-8(a) as repaired places the portfolio layout registry
    in a typed, owner-gated governance store grounded entirely on Wave A
    (RFC3-15/RFC3-16(a)/RFC3-15(a)); **accepting Wave B ratifies that
    placement.** The revert option (workspace manifest) restores the RC-4
    contradiction; P-22's register row is the current statement (packet 6
    of the round-08d file is stale and banner-marked).

18. **P-21(a) — the `constrains:` relation, frozen first by this act**
    *(added 2026-08-10; RD31-05).* RFC-0005's front matter declares the
    `constrains:` relation (`constrains_source: RFC5-3`) — installed while
    P-21's sub-question (a), whether `constrains:` is the right relation
    at all, is still open (RD-4 F-17). The wave that was to ratify it
    (C2, via RFC11-16's consumption clause) is deferred, so **the Wave A
    act is now the first act that freezes the declaration into
    owner-bound bytes** — and the only clause defining what a consumer
    does with the relation sits in a deferred wave. Nothing in Wave A
    evaluates the field (an outbound edge, not a reliance — item 9), but
    the act ratifies its presence. The same open ruling covers a
    declared-nowhere instance inside Wave B: RFC8-12 and RFC9-32 restrict
    each other in-clause with no `depends_on` or `constrains` edge either
    way (RD32-m2; intra-wave, no containment escape, and no new front
    matter is minted while (a) is open). Rule P-21(a), or perform the
    acts knowing the relation rides in unruled.
