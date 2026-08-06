> # SUPERSEDED — 2026-08-05b
>
> **Do not act from this file.** The current owner-facing offering is
> [`../round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md`](../round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md).
> A second round of work changed the act-1 and act-4 arguments (RFC-0010
> gained six clauses; every module's `provides_to` front matter was removed
> as derived; the overview was rebuilt). The two act phrases quoted below are
> **retired** and satisfy nothing. Acts 2, 3 and 5 are unchanged, but read
> them from the current offering so that all five come from one place.
>
> This file is kept because its §4 residual and its per-act "what is
> knowingly imperfect" sections are the honest record of what the previous
> round offered and why.

# Final owner acceptance record — human-clarity refactor round, 2026-08-05

> **This record offers. It does not accept.** Nothing below has been
> performed, and no agent may perform it. Every act is the owner's, written
> by the owner, in the owner's own words, one act at a time.

**What this file is.** The round's single owner-facing offering: the exact
files each act covers, the exact argument each act takes, what is knowingly
imperfect inside each, and what happens after. It is a *presentation* of the
gates, not their definition — the defining record is
[`../FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`](../FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md)
(§1 phrases, §2 ceremony, §7 knowing-acceptance items). Where the two
disagree, that record wins and this one is stale.

**Why a digest quoted here is safe to trust.** It is not trusted — it is
checked. `scripts/check_governance.py` check **CG-7d** compares every act
digest quoted *anywhere* in the repository against the artifact it names, so
a stale copy here fails the build rather than misleading a reader. That check
exists because this round's headline defect was the opposite: four act
arguments that were correct in their manifests and stale in the document that
offered them, found independently by six of eight reviewers.

---

## 1. The five acts

Each act is independent. **None implies another. None may be bundled.**
Performing act 1 does not adopt the overview; adopting the overview does not
accept the topology; nothing accepts the knowledge-hygiene policy, the term
registry, or a license.

### Act 1 — accept the compacted foundational contracts

The following argument is **retired** and satisfies nothing:

```text
RETIRED — ACCEPT COMPACTED FOUNDATIONAL RFCS: f2914fc56cd2aa069b952747b9c78b00dc41d908830887ecd2f1addd37e61fc4
```

- **Covers exactly:** the 32 active contract modules of RFC 0001–0011 at the
  per-module sha256 digests listed in
  `../ACTIVE-CONTRACT-MANIFEST.txt`, whose own sha256 is the argument above.
- **Does not cover:** `history/`, `fixtures/`, `matrix-rows/`, `reviews/`,
  the numbered reports, this round's records, or anything under
  `policy-candidates/`.
- **Verify before acting:** `python3 scripts/check_governance.py` — checks
  CG-7a (32 module digests), CG-7b (this argument), CG-7d (every copy of it).
  Or by hand: `cd .syzygy/governance/contracts/candidates && sha256sum -c
  ACTIVE-CONTRACT-MANIFEST.txt && sha256sum ACTIVE-CONTRACT-MANIFEST.txt`.
- **Knowingly imperfect inside this set:** the eight §7 owner-attention items
  of the defining record, plus this round's carried items F and G in
  [`ROUND-DISPOSITIONS.md`](ROUND-DISPOSITIONS.md) §4 — recomputable
  measurement figures sit inside digest-bound module text, RFC-0007's
  "twelve edges" enumeration is not exhaustive, and 20 `depends_on` /
  `provides_to` edges are asymmetric. None changes an obligation; each was
  left unedited rather than reopening a frozen manifest on a lead's judgment.
- **What acceptance schedules:** specification authoring only. The six
  phase-rule clauses (RFC6-28, RFC7-38, RFC8-32, RFC9-52, RFC10-16, RFC11-12)
  begin to bind; every user-observable behavior still routes through an
  owner-approved OpenSpec requirement before any implementation is scheduled.
- **Alternatives:** `REWORK COMPACTED FOUNDATIONAL RFCS: <reason>` or
  `REJECT COMPACTED FOUNDATIONAL RFCS: <reason>`.

### Act 2 — confirm the craft amendment CC-TEST-2

```text
CONFIRM CRAFT AMENDMENT: CC-TEST-2@7a716090bc827121b3f70c4f7e252fc5680cd8a56d7b4121b70f3673489690a0
```

- **Covers exactly:** `.syzygy/governance/policies/craft-and-care/testing-and-verification.md`
  at that digest. The craft cluster itself is already owner-approved (D2);
  only this one amendment is unconfirmed.
- **Digest re-quoted 2026-08-06** (superseding the retired, `aa2d6353…`-then-
  `3858820f…` arguments below): the owner directed `th-engineering` be
  vendored in-tree and re-pinned to close P-26, so `testing-and-verification.md`
  gained CC-TEST-7 recording the re-check against test-rigor's two new bars
  (no conflicts found) — `INSTALL-RECORD.md`'s 2026-08-06 correction.
- **Why the argument changed on 2026-08-05:** the nine canonical craft files
  carried an opening banner calling the canonical home "the bootstrap-phase
  record" — false, and inverted the authority relation. The banners were
  corrected; **no rule text changed** (SD-3). The rev9 argument `aa2d6353…`
  is retired and satisfies nothing.
- **No longer imperfect (resolved 2026-08-06):** the cluster's engineering
  bar was adopted *by reference* to a machine-local skill tree that a clone
  could not read (dispositions §4 C, register P-20). It is now vendored
  in-tree at `.claude/skills/th-engineering/` and `.codex/skills/th-engineering/`
  and pinned in `../../policies/GOVERNANCE-SUBSTRATE-LOCK.yaml` — owner
  override, P-26 executed.

### Act 3 — accept the topology bundle

```text
ACCEPT TOPOLOGY: 7a3b22494a08d888901c1f0cec76833dc926e89b6f510b5abf8963071fbaeb45
```

- **Covers exactly:** the nine files in `.syzygy/map/topology-candidates/` at
  the per-member digests in that directory's `BUNDLE-MANIFEST.md`, whose own
  sha256 is the argument above.
- **Why the argument changed this round:** topology `README.md` cited the
  retired rev9 acceptance phrase and called the contracts "proposed" rather
  than *candidate* (SD-2, SD-10). The other eight members are byte-unchanged
  from rev9. The rev9 argument `0d34d1b5…` is retired.
- **Verify:** `cd .syzygy/map/topology-candidates && sha256sum -c` against
  the manifest's fenced block, then `sha256sum BUNDLE-MANIFEST.md`.

### Act 4 — adopt the project overview

The following argument is **retired** and satisfies nothing:

```text
RETIRED — ADOPT PROJECT OVERVIEW: ce7794fd8c0e528ae50434f5c63ce27df998441cdd07b20a903627ecaf885b06
```

- **Covers exactly:** `.syzygy/intent/OVERVIEW.md` at that digest.
- **Why the argument changed this round:** the overview was rewritten into
  four-layer progressive disclosure, and its hand-maintained "Where this
  stands" section — which froze a status claim into a digest — was removed
  entirely; status now lives in `PROJECT-STATUS.md` (SD-9). Two review
  corrections followed: the VIS-4 sentence no longer asserts D3 as *the*
  licensing mechanism, and the north star and fleet-observability mandate are
  now stated rather than only disclaimed.
- **Note on what adoption means here:** the overview is explanatory. Adopting
  it fixes *how the project explains itself*, not what binds; it creates no
  obligation that doctrine or contracts do not already carry.

### Act 5 — optional: doctrine amendment D3 (bounded mission)

VIS-4 owner adoption in the owner's own words — **adopt**, **amend**, or
**decline** — is sufficient and is what the D3 packet itself specifies. The
round charter also offers a digest-bound phrase form; it is available, not
required, and is machine-checked (CG-7d) if used:

```text
RETIRED — ADOPT DOCTRINE AMENDMENT: D3@0328cb379cab1ffa462cc5bf2205241b96dec21b0917d485b0906d4fe7dcd96c
```

- **Covers exactly:** `../DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` (**rev1**,
  2026-08-05) and its two verbatim doctrine insertions. Rev1 supersedes
  `…-DRAFT.md`, whose `vision.md` insertion cannot be applied as written
  (SD-8).
- **Optional:** RFC-0010 and RFC-0011 do not depend on it.
- **Knowingly imperfect:** rev1's own change table is incomplete — the
  doctrine floor was recomposed and slightly widened. Every unlisted delta is
  meaning-preserving or stricter and none licenses anything, but the table
  understates the rewrite (dispositions §4 I, RB-6 F3).

### Recommended ordering

**Act 1 before act 5.** Adopting D3 first would leave *bounded mission* and
*autonomy envelope* as adopted doctrine terms whose binding definitions live
only in an unaccepted contract. Acts 2, 3 and 4 are order-independent.

---

**One deviation from the charter's suggested phrasing, disclosed.** The
charter writes act 2 as `CONFIRM CRAFT AMENDMENT: <policy IDs>@<bundle
digest>`. The form offered above binds the amended **file's** digest rather
than a cluster-bundle digest, because that is what the pre-existing acceptance
record and `INSTALL-RECORD.md` already define and what CC-TEST-2 actually
amends. Substituting a bundle digest now would retire a third act argument
mid-round. If you prefer the charter's form, say so and it will be regenerated
before any act.

## 2. The ceremony — five steps, per act, unchanged

Defined in `../FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §2 and
summarized here so the owner need not hold two documents open:

1. **The phrase.** The owner writes the exact phrase, including the digest.
2. **Scripted digest verification.** `python3 scripts/check_governance.py`
   must pass CG-7a/7b/7c/7d. A failure means the artifact moved after this
   offering was written: **do not perform that act** — regenerate, re-review,
   re-offer.
3. **Install at the act, bytes unchanged.** The accepted bytes move to their
   accepted home with no edit of any kind. An artifact edited after its act
   is, for the record, an artifact with no act.
4. **A dated entry** in `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md`
   naming the act, the argument, the files, and the date.
5. **One commit and one annotated tag** per act, the SHA mirrored afterwards
   into the founder decision log.

---

## 3. What is *not* offered here, and stays open

| Register item | What it is | Why it is not an act today |
|---|---|---|
| P-12 | Knowledge-hygiene craft policy (CC-KNOW-1…18, CC-BUDGET-1…4) | A candidate needing its own `CONFIRM CRAFT AMENDMENT` act; six sub-questions still open at the policy's foot |
| P-14 | License choice | Four candidates, three `[Unknown]`s including copyleft reach into governed repositories. Wants qualified legal review; never chosen autonomously |
| P-16 / P-17 / P-18 | Term registry, its eight undefined public terms, and three doctrine/contract vocabulary seams | The registry is a working vocabulary proposal, not doctrine; the seams want an owner ruling before OpenSpec multiplies them |
| P-10 | RFC-0006 clause-level routing classification | The artifact does not exist. Defer to RFC6-28 at surface specification, or commission it now |
| P-19 / P-20 | Mission-envelope residuals and this round's carried findings | Amendment candidates against a digest-frozen contract; none blocks an act |

Full text: [`../../decisions/PENDING-OWNER-DECISIONS.md`](../../decisions/PENDING-OWNER-DECISIONS.md).

---

## 4. The round's principal residual — read before act 1

**No fresh-context confirming review has been run over the current digests.**

The round commissioned eight independent verticals (`reviews/`), and their
findings drove a fix batch — but that batch is *why* the digests changed, so
every review predates the bytes now offered. Three reviewer sessions hit the
account's session limit during the battery, and the planned ninth review over
the exact final manifest was never run.

What partly substitutes for it, and what does not:

- **Substitutes mechanically.** All four digests reproduce from a
  `_bootstrap`-free clone simulation (§5); the 32 module digests and 9
  topology member digests verify; both index builders report no drift; the
  packet verifier passes; `check_governance.py` reports 15 OK / 7 WARN /
  0 FAIL over 22 checks, now including CG-7d.
- **Does not substitute.** No independent human-or-agent reader has judged
  the *content* of the post-batch bytes. The fix batch was small, cited, and
  recorded as SD-10 — but "small and recorded" is the author's claim about
  the author's own edits, which is precisely the claim review exists to test.

**The owner's choice:** commission one fresh-context digest-binding review
before act 1, or perform act 1 as a knowing acceptance with this paragraph as
the disclosure. Recorded as the round's principal residual in
[`ROUND-DISPOSITIONS.md`](ROUND-DISPOSITIONS.md) §5.

---

## 5. Evidence that a clone reproduces this offering

Run 2026-08-05 against a simulated clone — every tracked and to-be-tracked
file, **no `_bootstrap/`**, 190 files:

| Check | Result |
|---|---|
| Act 1 argument recomputed from clone bytes | `f2914fc5…` — matches |
| Act 2 argument recomputed | `3858820f…` — matches |
| Act 3 argument recomputed | `7a3b2249…` — matches |
| Act 4 argument recomputed | `ce7794fd…` — matches |
| `sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt` | 32/32 OK |
| Topology member digests vs `BUNDLE-MANIFEST.md` | 9/9 OK |
| `build_contract_index.py --check` | no drift |
| `build_dependency_index.py --check` | no drift |
| `verify_final_prespec.py` | PASS |
| `check_governance.py` | 14 OK, 8 WARN, 0 FAIL over 22 checks — the extra WARN versus the repository run is CG-11, correctly Unknown where git is unavailable |

---

## 6. After the acts

Only when the front door is clear, the active knowledge is compact, the
vocabulary is canonical, the candidate contracts are clone-visible, the
Context Compiler contract is fixture-tested, bounded-Mission policy is
owner-resolved, the knowledge-hygiene policy is adopted, and the
project-shape artifacts are accepted, the next phase is:

```text
/th-projects project-feature-request
```

for the first coherent V0 specification. Four of those eight conditions are
owner acts that have not happened. **Until they do, this repository stays in
pre-specification: no OpenSpec feature changeset, no implementation backlog,
no stack choice, no product code.**
