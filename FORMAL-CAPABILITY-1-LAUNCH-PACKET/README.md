# Formal Capability 1 launch administration — sealed packet

> **⛔ RETIRED — ADMINISTERED 2026-08-18. Purpose discharged.** One full
> formal administration was run under this packet on 2026-08-18
> (out-of-family, instrument v2.4, against commit `71e5986`); the record
> is `.syzygy/governance/decisions/launch-gate/ADMINISTRATION-2026-08-18-CAPABILITY-1.json`
> and its verdict was `NOT READY`. The banner below this one — "Prepared,
> not administered … No administration has been run under it" — was true
> when sealed and is **false since 2026-08-18**; it is retained unedited
> as the sealed text. This retirement is the governance-reduction plan's
> §4 row, executed 2026-08-19 under the owner's P-47 ruling
> (`.syzygy/governance/decisions/F2-GOVERNANCE-REDUCTION-DECISION.md`).
> A future administration takes its commission from
> `PROJECT-STATUS.md` §"Next lawful step" and the instrument itself,
> never from this packet.

> **Prepared, not administered.** This packet is everything a reviewer
> needs to run **one full, formal administration** of the launch gate
> against the launch target below. **No administration has been run under
> it**, and this repository's authoring sessions may not run one: an
> administration by the corpus's own authors is not the evidence a launch
> decision needs (instrument §2 — *"A repair session may not administer the
> gate over its own repaired bytes"*).
>
> Nothing in this packet is an owner act. A `READY` verdict authorizes
> nothing; the owner's launch decision is separate and comes after.

## 1. What is being asked

Administer `launch-gate-pre-specifications.md` **v2.4**, in full, against
the target below. **v2.4 is owner-approved process policy** — ruled
2026-08-16 (P-34, arm (a); the recorded decision with verified digests is
`.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md`) — with
**two disclosed BLOCKING residuals** in the validator's guarding
(RD-67 f1, RD-68 f1; §3 below states the mitigation this packet requires
of you) and **F5 not promoted** to a formula conjunct. The instrument's
own header still reads "owner approval pending": the approval binds the
instrument's exact digest, so the header could not be updated without
retiring the approved bytes — the authority record above, not the banner,
states the instrument's force.

```text
LAUNCH TARGET
    Capability 1 — Project registration and honest shape visibility

REQUIRED WAVES
    A, B

DEFERRED WAVES
    C1, C2, D1, D2
    candidate; not accepted; not used by the launch target; excluded from
    default task routing. Posture and per-wave reasons:
    .syzygy/governance/contracts/candidates/DEFERRED-WAVE-POSTURE.md
```

## 2. What is bound — verify every digest before you begin

```text
repository commit    (recorded by you, in full — see the note below)

launch-gate-pre-specifications.md (v2.4 — the digest the P-34 approval itself binds)
    1852c2c3d31eff3afa0924b6b72e855481ab2516ba8fde5eda7b2ae8772f01e8
§8 parameter block (as bound for this administration)
    01209c0f052971f794e1f35827a002aa8d80420aad471d10fde000abb6366ff6
launch-gate-administration.schema.json
    e0167fb8af6a903c527d402d56c4fb85ebdfed9608de1a485f4f1563aa6a69fb
scripts/validate_launch_administration.py
    047098326af2f415558f0ca748a98a5889d91e9cfecaa67d700ef1ba883ba497
scripts/render_launch_administration.py
    44d568e397271ff897dc13fd4cc46a9d1a9404d0d32db19b5b22dad69fa351c5
```

**Fourth re-seal, 2026-08-17, at instrument v2.4.** The v2.2 seal's
instrument, validator and renderer digests —
`ac8751236ec7434c20606b404d41c885d29f67dd5f3dab8c9d0cbb90de670977`,
`dbb8b69097df15a4bf60cc6fc0cef1043b838a22d30920f1914da31a91322977`,
`4ffa3c9ec83aad7951884be159eec81dde8374387fc45c4d7a6ba9b323a08e61`,
each written in full because a truncated stale digest is a promise
`CG-15` refuses — are superseded and **satisfy nothing**: the instrument
was repaired through v2.3 and v2.4 (each pair of reviews returned
`REVISE`; §9 has the sequence) and the owner then approved v2.4 with the
residuals disclosed. **Two of the five digests did not move across all
five seals**: the **§8 parameter block** (full value in the block above —
every fixed input you are judged against is unchanged since v2.0) and
the **schema**. The instrument digest above is the same digest the P-34
approval record binds; if it does not verify, you are not holding the
approved instrument.

Verify, in a fresh clone:

```sh
git log --oneline -1
git status --porcelain                       # must print nothing
sha256sum launch-gate-pre-specifications.md launch-gate-administration.schema.json \
          scripts/validate_launch_administration.py scripts/render_launch_administration.py
```

**If any of the four sha256 digests differs, stop.** The packet is stale and
the administration would bind bytes nobody offered. Report the mismatch
rather than proceeding.

**No commit is bound, deliberately** *(changed 2026-08-13; the v2.0 seal
named one, and RD-50 f11 had already had to explain that its advancing was
not a mismatch)*. **The five sha256 digests are the whole of the binding.**
Verify them at whatever commit you clone, record the commit you actually
used in `repository_commit`, and note nothing about divergence — there is
nothing to diverge from. A digest mismatch is the only mismatch, and it means
this packet is stale: report it rather than proceeding.

**`repository_commit` must be the full 40-hex commit — this is residual
mitigation, not house style.** Disclosed residual **RD-67 f1**: an
abbreviated commit (7–39 hex) validates against the schema's pattern but
routes the validator's schema read to `HEAD` instead of the record's
commit, which is a demonstrated false-`READY` path. Write all 40
characters (`git rev-parse HEAD`), and the schema the validator reads is
then the one at your commit.

## 3. How the record is produced

**The record is JSON, not prose.** Author a file conforming to
`launch-gate-administration.schema.json`, then:

```sh
python3 scripts/validate_launch_administration.py <record>.json --trend-row
python3 scripts/render_launch_administration.py  <record>.json
```

The validator computes the verdict from your rows. **There is no field in
which to write a verdict** — the schema rejects one. The Markdown report is
generated and is never read back as authority.

Set `"formal": true` and `"administration_kind": "full"`. A delta
administration cannot support a gate decision, and the validator refuses
the combination.

**Before submitting the record, run the two residual checks yourself** —
the validator's guarding has two disclosed holes an adversarial record
could walk through, and a formal record must be shown clean of both:

1. **Full 40-hex `repository_commit`** (RD-67 f1 — §2 above).
2. **No category-`So`/invisible padding** (RD-68 f1): the placeholder
   strip misses `So`-category characters (`U+2800` Braille blank,
   `U+FFFC`), so a padded, unfalsified record can validate. Verify the
   record contains none:

   ```sh
   python3 -c "import sys,unicodedata as u; d=open(sys.argv[1],encoding='utf-8').read(); bad=[(i,hex(ord(c))) for i,c in enumerate(d) if u.category(c)=='So' or ord(c)==0x2800]; print(bad or 'clean'); sys.exit(1 if bad else 0)" <record>.json
   ```

   `clean` is the required output; anything else is a finding against the
   record itself.

## 4. Who may administer this

- **Fresh context.** No prior contact with this repository's review
  history, no summaries of "how it's going", no prior administrations
  (except the trend log, and only when answering F1).
- **A different model family from the corpus's authors, or a human —
  required for THIS administration.** This corpus was authored by Claude
  models, every administration and review to date has been by that
  family, and the owner's convergence direction treats a same-family
  formal administration as repair-grade evidence only — it cannot be the
  formal administration this packet exists to obtain. (The instrument's
  F5 is not a formula conjunct — the owner declined to promote it at
  P-34 — so this requirement is the *packet's*, stated here because the
  packet is what commissions the run.) If the owner nonetheless accepts a
  same-family run, the record must say so —
  `reviewer.same_family_as_corpus_authors: true` — and the disclosure
  travels into the trend row; hiding it would fail the question the
  record is answering.
- **Not an authoring session of this repository**, under any circumstance.

## 5. The materials you are given

```text
1. launch-gate-pre-specifications.md              the instrument, in full
2. .syzygy/governance/doctrine/                   the adopted goal statement
3. .syzygy/intent/OVERVIEW.md                     the public entry document
4. read access to the repository at the named commit
5. §8 of the instrument                           the parameter block
6. .syzygy/governance/decisions/launch-gate/TREND-LOG.md   for F1 only
```

**Withheld — do not read for content:** authoring history, prior review
results, prior administrations, and any summary of the project's progress.
Trees holding reviews and administrations are in scope as *objects* of the
F2/F4/C3 sweeps — they are files, and a stale claim in one is a finding —
but their findings and narratives must not inform any other question's
answer. If you read them for content, record it as a materials deviation.

**The materials list is fixed by this packet and the instrument. It is not
curated per administration.** Anything added, missing, or unreadable goes
in `materials.deviations`.

## 6. Fixed inputs you must use as given

**The D2 routing tasks** (parameter block; chosen before the
administration, never by you mid-run):

```text
routine    "add an evidence adapter for a new CI system"
authority  "change what counts as a completed Mission"
seam       "trace a merged change from its work record to its reconciled
            status"                    — crosses the work/evidence seam
```

**The E4 fixed cases** are the six statements in §8's `E4_CASES` list.
Classify each from its text alone (shape side or spec side — two-valued),
then compare against the routing authority named in §8. The validator
checks your `case_text` against the instrument's own bytes: a paraphrased
case carries no verdict.

**The A3 near-misses** and **A5's closed `MAJOR_SHAPE_COMMITMENTS` list**
are likewise fixed in §8. Do not invent softer near-misses, and do not build
A5's population yourself.

## 7. What the owner has and has not decided

**Four owner acts have been performed, all 2026-08-17** *(corrected
2026-08-18; this section previously said no act had been performed and the
act record did not exist — true at the fourth re-seal, false from the acts
onward, and Administration 1 correctly flagged the staleness as its F3
counterexample)*: Wave A, Wave B, and craft acts 6 + 7 (CC-SPEC,
CC-IMPACT). `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` exists
since the first act and owns them. The five seal digests above are
unchanged by this correction — none of the sealed artifacts moved.

The open decisions are owned by
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` (open rows) and
`.syzygy/governance/decisions/DECISION-HISTORY.md` (what was ruled and
when). *(The round-08g owner-decision index this section previously
routed to is superseded and banner-marked — eight of its decisions were
ruled 2026-08-16; read the queue.)*

**No count is stated here on purpose.** *(Corrected 2026-08-13.)* This
section previously said "ten owner decisions are open" and routed to the
round-08f combined packet — a page review `RD-52` returned `REVISE` on, whose
blocking finding was that its one-sitting premise was false by its own
contents. It is now banner-marked superseded. Routing an administrator to a
superseded offering, with a hand-maintained count beside it, is the defect
this repository has already paid for twice; read the queue.

This matters for your verdicts in a specific way: **an unruled decision is
not a defect of the corpus** — it is a recorded open question, which is
what VIS-4 requires. What *would* be a defect is a document presenting an
unruled decision as settled. Judge that, not the existence of the queue.

## 8. Spot-review requirements

D2, E3 and E4 are exercises, not document judgments. Their results are to
be **human spot-reviewed** before the record is treated as gate evidence:

- **D2** — did the route actually answer the task, or did it require
  reading the corpus?
- **E3** — is the reopen-list empty because nothing must reopen, or because
  the reading was shallow? The trace table exists to make that visible, and
  the validator refuses `E3 | Met` without it.
- **E4** — do your classifications and the routing authority's actually
  disagree where you say they do?

## 9. What this packet does not contain, deliberately

- **Prior verdicts and repair summaries.** Withheld by §5. If you have seen
  them, say so in `materials.deviations`.
- **A recommended verdict.** There is none, and any document that offered
  one would be inviting the failure the gate exists to catch.
- **The ten reviews' findings.** *(Updated 2026-08-17. This section has
  said several different things; the sequence matters more than any one of
  them, and it is the honest answer to "how settled is this instrument?")*

  | Round | Reviews | Verdicts |
  |---|---|---|
  | v2.0 | RD-47 machinery, RD-48 policy | both `REVISE` |
  | v2.1 | RD-56 machinery, RD-55 policy | both `REVISE` |
  | v2.2 | RD-62 machinery, RD-61 policy | both `REVISE` |
  | v2.3 | RD-66 machinery, RD-65 policy | both `REVISE` |
  | v2.4 | RD-68 machinery, RD-67 policy | both `REVISE` |

  **The instrument you are administering is v2.4, and it is
  owner-approved with that record in front of the owner.** After the
  fifth consecutive `REVISE` pair, the owner ruled **P-34 arm (a)**
  (2026-08-16): approve v2.4 as process policy rather than spend a sixth
  repair cycle — the one structural repair (the mechanical forgery sweep)
  held, no live forgery exists in v2.4's bytes, and the two recurring
  class defects (**RD-67 f1**, **RD-68 f1**) are **disclosed blocking
  residuals** this administration runs with; §3's residual checks are
  their mitigation. **F5 was not promoted** to a formula conjunct. The
  full reasoning and the digests the approval binds are in
  `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md`.

  Read that as a fact about *this instrument's* maturity, and do not let
  it colour your verdicts on the corpus — F6 is where the process's own
  health is recorded. The raw reviews live in `round-2026-08f/`,
  `round-2026-08g/` and `round-2026-08h/` `reviews/` trees.
  **Their content is withheld from you under §5 for every other
  purpose.** Do not read them to inform an answer; this section exists so
  that you know what state the instrument is in, not so that you inherit
  its reviewers' judgments. If you do read them, record it in
  `materials.deviations`.

## 10. Deliverable

```text
<record>.json    the source record — the deliverable
<record>.md      its generated report
one trend row    printed by --trend-row, appended to TREND-LOG.md
```

Store both verbatim in `.syzygy/governance/decisions/launch-gate/`. Never
edit a past administration; supersede it.
