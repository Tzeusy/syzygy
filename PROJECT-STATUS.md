# Project status

> **As-of: 2026-08-05b** (the commit introducing this revision of this file —
> `git log -1 --format=%h PROJECT-STATUS.md`). This file is a hand-authored
> pointer page with an as-of revision: it **must not be the sole source** for
> any fact it states — each row cites the owning record, and where they
> disagree, the record wins and this file is stale. It is regenerated or
> corrected in the same change whenever a gate fires.

## Lifecycle stage

**Final pre-specification.** No application code exists; none may be added
until the foundational contracts are accepted and behavioral specifications
are authored and approved.

## Gates

| # | Gate | Status | Owning record |
|---|---|---|---|
| 1 | Doctrine adoption | ✅ **Adopted** 2026-07-30, amendment D1 in force | tag `doctrine-adopted-2026-07-30`; `.syzygy/governance/doctrine/README.md` |
| 2 | Craft-and-care approval | ✅ **Approved** (owner decision D2) | `.syzygy/governance/policies/craft-and-care/INSTALL-RECORD.md` |
| 3 | Surface decisions | ✅ **Recorded** SDR-1…33 | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md` |
| 4 | Foundational contracts (act 1) | ⏳ **Candidate — no act performed** | acceptance record + `ACTIVE-CONTRACT-MANIFEST.txt`, `.syzygy/governance/contracts/candidates/` |
| 5 | Craft amendment CC-TEST-2 (act 2) | ⏳ **Awaiting confirmation** at the current digest | `INSTALL-RECORD.md` correction block, 2026-08-05 |
| 6 | Topology (act 3) | ⏳ **Candidate — no act performed** | `.syzygy/map/topology-candidates/BUNDLE-MANIFEST.md` |
| 7 | Project overview (act 4) | ⏳ **Draft — refactored, awaiting adoption** | `.syzygy/intent/OVERVIEW.md` header |
| 8 | Doctrine amendment D3 — bounded missions (act 5, optional) | ⏳ **Proposed** — adopt, amend, or decline | `.syzygy/governance/contracts/candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` (rev1; supersedes the original `…-DRAFT.md`) |
| 9 | Knowledge-hygiene craft policy | ⏳ **Candidate — own craft act** | `.syzygy/governance/contracts/candidates/policy-candidates/` |
| 10 | License | ⏳ **Undecided — owner/legal** | `.syzygy/governance/decisions/LICENSE-DECISION-PACKET.md` |
| 11 | Behavioral specifications (OpenSpec) | ⛔ **Not started** — blocked on gate 4 | — |
| 12 | Implementation | ⛔ **Not started** — blocked on gate 11 | — |

**No owner acceptance act has been performed.**
`.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` does not exist,
which is the correct state — it is created by the first act.

The full open-decision queue is
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`. The owner-facing
offering for gates 4–8 — exact phrases, what each act covers, what is
knowingly imperfect inside each — is
`.syzygy/governance/contracts/candidates/round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md`
(the `round-2026-08/` one is superseded and banner-marked).

## What exists in this repository

Adopted doctrine; owner-approved engineering policy; recorded owner
decisions with tracked warrant extracts; the candidate contract corpus
(RFC 0001–0011, 32 modules) with its manifest, acceptance record, fixtures,
reviews, and verification scripts; the candidate topology bundle; candidate
policy additions; the overview draft; navigation skills; documentation-only
CI. **No** `openspec/`, no accepted-contract home, no source tree, no
product CI, no implementation backlog.

## Known blocking defects

**One open, and it is the round's own gate-arithmetic:** the acceptance
record's four digest-bound act arguments were regenerated during this round's
corrections, so any act phrase must be read from the acceptance record **as
re-quoted at the round's close** — not from an earlier copy. `scripts/
check_governance.py` check CG-7 compares every act argument against its
subject artifact — CG-7d now covers every copy of every act digest anywhere in
the repository, not just the acceptance record's. Treat a CG-7 failure as "do
not perform that act", never as a formatting nit. Non-blocking
knowing-acceptance items travel with the acceptance record's owner-attention
section, not this file.

**One residual, disclosed rather than fixed:** no confirming review is bound
to the bytes now offered. The last CONFIRM (2026-08-03) named a manifest digest
that has since been superseded twice — first by RFC-0010's correction plane and
the `provides_to` removal, then by the RC-4 dependency corrections. The
2026-08-05b review battery (RC-1…RC-10) read the corpus and drove those very
changes, so with one exception each of them predates what is now offered.
Read `round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md` "Read this first"
before act 1.

**Two things this project does not have, stated plainly:** there is no
mechanical task-to-context-packet compiler — `context_load.py` measures a
selection you have already made, and every fixture's selection is
hand-authored. And the *evidence-adapter* fixture class has no fixture; the
set is seven-for-eight with one double-count.

## Next lifecycle step

The owner performs (or declines) the acts above. After act 1, the first
concrete proposal runs through `/th-projects project-feature-request` toward
an owner-approved OpenSpec delta — specification authoring, still no
implementation.

## How to verify this page

```sh
python3 .syzygy/governance/contracts/candidates/scripts/verify_final_prespec.py
python3 .syzygy/governance/contracts/candidates/scripts/build_contract_index.py --check
python3 .syzygy/governance/contracts/candidates/scripts/build_dependency_index.py --check
python3 scripts/check_governance.py
git tag --list 'doctrine-*'
```

Also run `python3 scripts/check_governance.py --selftest`, which puts each
check against a synthetic failing input. It exists because this repository has
shipped a validator that could not fail: the dependency index reported 20
asymmetric edges at every generation while its own drift check reported clean,
because regenerating a knowingly-broken graph reproduces the same
knowingly-broken file.

Current results (2026-08-05b): packet verifier PASS; both index builders report
no drift; `check_governance.py` **24 OK, 8 WARN, 0 FAIL over 32 checks**;
`--selftest` 19 fixtures, 0 failing. The eight WARNs are declared-by-design
(forward references, frozen-packet pointers, report-only budget triggers,
allowlists) and each prints its rationale. **Read the output, not the exit
code** — a PASS over zero examined items verified nothing.

Run it in a **clone**, not only here. At one commit this round the two
disagreed — 0 FAIL in the working tree, 1 FAIL in a clone — because CG-14
asked the local filesystem whether a git-excluded directory existed, and the
founder machine has one. That divergence is the whole failure mode this
repository keeps re-acquiring, and it is invisible from the machine that has
the directory.
