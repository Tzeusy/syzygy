# Final foundational-contract acceptance record — rev10 (compacted package)

This record defines the owner gates over the rev10 final pre-specification
package and, on the owner's act, supersedes
`_bootstrap/rfc-phase/FOUNDATIONAL-RFC-ACCEPTANCE-RECORD.md` (rev9) as the
acceptance authority. **Nothing adopts implicitly**: each gate below is
independent, none implies another, and no artifact rides on another's
gate. Until an act is performed, every artifact here binds nothing
(RFC3-16).

## 1. The gates — exact scope, exact phrases

| # | Act (exact phrase) | Accepts exactly |
|---|---|---|
| 1 | `ACCEPT COMPACTED FOUNDATIONAL RFCS: ac07a06497cd72b8dd10a9a42776a6a41d7c45740ffec7905d4c27fbe7146b4f` | The 32 active contract modules (RFC 0001–0011) at the per-module sha256 digests in `ACTIVE-CONTRACT-MANIFEST.txt`, whose own digest is the act's argument. Nothing else — not history/, not fixtures/, not the reports. **Digest re-quoted twice on 2026-08-05b.** First: RFC-0010 gained six clauses (RFC10-17..22, the correction plane) and all 32 modules dropped the derived `provides_to` front-matter key. Then, after review RC-4 refuted four of the dependency edges added in that same pass, the edges were reverted, one wrong vocabulary ordinal was corrected, and the manifest was regenerated again (see `round-2026-08b/DEPENDENCY-CLOSURE-REPORT.md` §"Correction after RC-4"). The prior arguments `f2914fc5…` and `41195c81…` are both retired and satisfy nothing |
| 2 | `CONFIRM CRAFT AMENDMENT: CC-TEST-2@3858820f64768ef20e6514fe8adb28076263f071ac77e66a5520a612f3bcb26d` | The craft cluster is committed and owner-approved (D2); only this amendment needs confirming. **Digest re-quoted 2026-08-05** — the nine canonical files' banners were corrected (P-7/SD-3, rule text byte-unchanged), so the rev9 argument `aa2d6353…` is stale and satisfies nothing |
| 3 | `ACCEPT TOPOLOGY: 7a3b22494a08d888901c1f0cec76833dc926e89b6f510b5abf8963071fbaeb45` | The nine topology files at the per-member digests in `../../../map/topology-candidates/BUNDLE-MANIFEST.md`, whose own digest is the act's argument. **Digest re-quoted 2026-08-05** — topology `README.md` lost the retired acceptance phrase and its draft/proposed vocabulary (SD-2, SD-10); the other eight members are byte-unchanged from rev9, and the rev9 argument `0d34d1b5…` is stale and satisfies nothing |
| 4 | `ADOPT PROJECT OVERVIEW: 01d629515993188338f6a0e2d84d67543d8569003759a7c8f571a90b129c7cd1` | `.syzygy/intent/OVERVIEW.md` at that digest. **Digest re-quoted 2026-08-05** — the overview was refactored to four-layer progressive disclosure and its authoring-time status section removed (P-13/SD-9); the rev9 argument `42de2eb1…` is stale and satisfies nothing. **Re-quoted again 2026-08-05b** — the overview was rebuilt to a default layer plus two collapsed drawers, the frozen gate-state table was removed in favour of a pointer to `PROJECT-STATUS.md`, and the machine query plane was restored to the consumer list; the retired argument `ce7794fd…` satisfies nothing |
| 5 | Doctrine amendment **D3** (bounded mission) — VIS-4 owner adoption, no magic phrase | `DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` (**rev1**, 2026-08-05) and its two verbatim insertions. Rev1 supersedes `…-DRAFT.md`, whose `vision.md` insertion cannot be applied as written (SD-8). **Optional**: RFC-0010/0011 do not depend on it. Recommended ordering: perform act 1 before act 5 |

**Acceptance schedules no implementation.** Accepting these contracts
clears specification authoring only: the six phase-rule clauses (RFC6-28,
RFC7-38, RFC8-32, RFC9-52, RFC10-16, RFC11-12) bind, and every
user-observable behavior still routes through an owner-approved OpenSpec
requirement before any implementation work is scheduled.

Rework/rejection of the RFC package:

```text
REWORK COMPACTED FOUNDATIONAL RFCS: <reason>
REJECT COMPACTED FOUNDATIONAL RFCS: <reason>
```

The rev9 `ACCEPT FOUNDATIONAL RFCS` phrase is **retired unconditionally
at rev10 delivery** — a retirement notice is written into the rev9 record
itself, because supersession of an authority must not be conditional on
exercising the authority that supersedes it, and the rev9 phrase (which
carries no digest argument) cannot self-identify which corpus it would
bind. The rev9 corpus is preserved as history (`history/rev9-rfcs/`), not
offered for acceptance; acts 2–4 continue under this record's §1 rows at
unchanged digests.

## 1a. Revision of 2026-08-05 — read this before acting

This record was authored at rev10 (2026-08-03) and **re-quoted at the close
of the human-clarity refactor round (2026-08-05)**. Every one of the four
digest-bound arguments in §1 changed during that round, because the round
corrected defects inside three of the four digest sets:

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
python3 scripts/check_governance.py      # checks CG-7a/7b/7c cover all four acts
```

A CG-7 failure means the artifact moved after this record was written: **do
not perform that act** — regenerate, re-review, and re-offer. This is the
same rule §2 step 2 states; the round added the machine check because three
of the four acts had no check at all until 2026-08-05.

## 2. The acceptance transaction — honest under RFC3-16(c)

Each act is a chat-phrase ceremony executed in five steps:

1. **The phrase.** The owner writes the exact phrase from §1.
2. **Digest verification, by script.** The lead re-verifies the bound
   digest(s) against the working tree (`sha256sum -c
   ACTIVE-CONTRACT-MANIFEST.txt`; then the manifest's own digest). Any
   mismatch means no act: regenerate, re-review, re-offer.
3. **Installation, bytes unchanged.** Act 1 installs the 32 modules (with
   their package directory structure) to `.syzygy/governance/contracts/rfcs/`
   and `ACTIVE-CONTRACT-MANIFEST.txt` to `.syzygy/governance/contracts/` —
   one level above, so the manifest's `rfcs/…` entries resolve — the
   RFC3-15 `contracts/` home, created at this step. The copy is
   digest-verified by running `sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt`
   **from `.syzygy/governance/contracts/`**. Acts 2/4 bind content already
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
   **Companion material, installed but not accepted:** act 1's install
   also copies `history/` and `matrix-rows/` to
   `.syzygy/governance/contracts/history/` and `…/matrix-rows/` so the
   modules' 68 Tier-2 rationale backlinks and the RFC-0003 README's
   census link resolve from the governed tree. These directories are
   **non-normative** (their own README states "Nothing in this directory
   binds"), sit outside the act's accepted digest set, and carry no
   authority — the act binds exactly the 32 manifest entries, nothing
   else.
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

**Manifest digest (act 1's argument):** `ac07a06497cd72b8dd10a9a42776a6a4…`
— sha256 of `ACTIVE-CONTRACT-MANIFEST.txt`, which lists the sha256 of
each of the **32 active modules**. The manifest is regenerated by script
only; per-module digests are never hand-transcribed. (Regenerated after
the rev10 confirming review if any fix lands **in `rfcs/`** — only edits
to the 32 modules invalidate the digest; fixes to this record, the
reports, or the rev9 record do not churn it. The phrase in §1 always
carries the current manifest digest.)

**Clause inventory (script-verified, `scripts/verify_final_prespec.py`):**
**322 numbered clauses** — RFC1-1..32, RFC2-1..25, RFC3-1..32 (+5
lettered, incl. new **RFC3-16(c)**), RFC4-1..29 (+2), RFC5-1..26,
RFC6-1..28, RFC7-1..38 (+7), RFC8-1..32, RFC9-1..52 (+8),
**RFC10-1..16, RFC11-1..12** (new contracts). Zero rev9 clauses merged,
retired, renumbered, or routed out (04-CLAUSE-MIGRATION-MATRIX). Seven
contracts are packages (0002 ×4, 0003 ×2, 0004 ×4, 0005 ×3, 0007 ×2,
0008 ×3, 0009 ×3 modules + README each); RFC-0001 and RFC-0006 are single
files; RFC-0001 is the one justified-oversize module (8,353 words,
dictionary-shaped — justification in the 03 report and printed by the
verifier).

**Word accounting (03 report, honest form):** rev9 normative corpus
90,410 words, one mandatory reading path. Rev10: compacted normative text
73,685 (−18.5%) + package scaffolding 7,333 + READMEs 12,696 + new
contracts 5,353 = 99,067 on disk (post-review fix batch); Tier 2 history
27,521 extracted.
**The owner's 35–50k corpus band was not reached** — nine independent
passes each hit an incompressibility floor at −12…−22% (arithmetic in
`WORKER-REPORT-DIGEST.md`). The optimization target it served instead:
measured per-task mandatory load **10,854–18,302 words** (five fixtures;
median ≈ 13,900 ≈ 18.7k est. tokens ≈ 9–15% of the rev9 path), with one
disclosed risk-class exception (fixture 2).

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
  The manifest has been regenerated twice since (RFC-0010's correction plane;
  the dependency-direction change and its RC-4 correction). No confirming
  review is bound to the current argument
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
   unreserved directory is conforming").
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
9. **Single-source structure, disclosed** (safety review): RFC 0001–0009
   never cite RFC-0010/0011, so the no-self-widening rule has no
   redundant restatement inside the nine earlier contracts. Back-citations
   were deliberately not added (nine-contract churn for redundancy); the
   corpus relies on RFC10-15/RFC11-4 loading rules to carry the
   prohibition into every mission context.
10. **R1 — one stale navigation count inside the accepted digest set**
    (confirming review): `rfcs/RFC-0007/README.md` line 46 states its own
    size as 2,268 words and derives package-union figures 10,578 / 7,435
    / 5,411 from it; the actual post-fix-batch count is **2,326** (the
    58-word "Phase boundary" section postdates the figures; true unions
    10,636 / 7,493 / 5,469). No clause, obligation, or external artifact
    depends on the figure — the 06 map and index carry the correct
    2,326. Fixing it would churn the manifest digest and force another
    confirming cycle. The owner chooses knowingly: **accept as-is** (the
    correction rides the first genuine RFC-0007 amendment), or direct a
    fix + digest regeneration + one more digest-binding review.
