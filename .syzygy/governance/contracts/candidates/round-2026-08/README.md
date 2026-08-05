# Round records — human-clarity refactor, 2026-08-05

> **Non-authoritative process records.** Nothing in this directory binds
> anything, adopts anything, or accepts anything. It records how one round of
> work was scoped, reviewed, and disposed, so that the round's judgments can
> be audited instead of trusted. Authority lives in
> `.syzygy/governance/doctrine/` (adopted), `.syzygy/governance/policies/`
> (owner-approved), and — only on an owner act — `../rfcs/`.

## Read in this order

| # | File | What it answers |
|---|---|---|
| 1 | [`FINAL-OWNER-ACCEPTANCE-RECORD.md`](FINAL-OWNER-ACCEPTANCE-RECORD.md) | **Start here if you are the owner.** The five acts, their exact arguments, what each covers, what is knowingly imperfect inside each, and what is *not* offered |
| 2 | [`FINAL-PRE-SPECIFICATION-READINESS-REPORT.md`](FINAL-PRE-SPECIFICATION-READINESS-REPORT.md) | The charter's five completion tests, answered with evidence; what readiness the evidence supports and what it does not |
| 3 | [`FINAL-HUMAN-CLARITY-REVIEW.md`](FINAL-HUMAN-CLARITY-REVIEW.md) | Whether the round met its governing standard, including what it got wrong |
| 4 | [`ROUND-DISPOSITIONS.md`](ROUND-DISPOSITIONS.md) | Every review verdict, what was fixed, and every finding carried with its reason |
| 5 | [`reviews/`](reviews/) | The eight raw fresh-context reviews, **stored verbatim and never edited** — the evidence behind everything above |

## Supporting records

| File | Content |
|---|---|
| `OWNER-ROUND-CHARTER.md` | The owner's round prompt, byte-verbatim. Relocated here from the repository root after review (see below) |
| `PUBLIC-CLONE-VERIFICATION-REPORT.md` | What a real `git clone` contains, what reproduces from it, and what a clone still cannot do |
| `REFRACTOR-PREFLIGHT-REPORT.md` | Repository state at round start |
| `PUBLIC-CLONE-AUTHORITY-MATRIX.md` | What a clone can and cannot read, per authority layer |
| `ACTIVE-AUTHORITY-MAP.md` | Which artifact owns which decision today |
| `ARTIFACT-INVENTORY.md` | Shape record of the tree (a shape, not a live total) |
| `HISTORICAL-ARCHIVE-INDEX.md` | Where superseded material went and why it is not authority |
| `SEMANTIC-DELTAS-THIS-ROUND.md` | SD-1…SD-12 — every normative or authority-adjacent edit, classified |
| `TERM-MIGRATION-REPORT.md` | Term registry derivation, plus contradictions C-1…C-6 |
| `CONTEXT-COMPILER-FIXTURE-REPORT.md` | The eight selection fixtures and their measurements |
| `MISSION-CONTROL-REVIEW.md` | Bounded-Mission and autonomy-envelope assessment |
| `KNOWLEDGE-HEALTH-BRIEF.md` | Corpus size, budgets, and rot risk |
| `COMPACTION-EQUIVALENCE-REPORT.md` | Semantic-preservation evidence for the compaction |
| `PROCESS-LESSONS.md` | Generalizable lessons, including the verification hazards |

## Two notes a later reader will need

**The charter moved.** `OWNER-ROUND-CHARTER.md` was the root-level file
`syzygy_fable_human_clarity_refactor_round_prompt.md` until 2026-08-05, when
RB-1 observed that a public clone's second-most prominent root file was a
working prompt for one refactor round. It moved here **byte-unchanged**
(sha256 `a33142da891cdeb0bb2fdbb1cd28615ef1fe16ae8e0be4e6ee575a3046946d07`
before and after; semantic delta SD-11). Reviewer reports cite it by its old
root path with line numbers — those line numbers still resolve, against this
file.

**The reviews predate the bytes.** The eight reviews drove a fix batch, and
that batch is why three of the four act digests changed. No review has been
run over the current bytes. This is stated as the round's principal residual
in `FINAL-OWNER-ACCEPTANCE-RECORD.md` §4 — read it before performing act 1.
