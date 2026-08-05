# RFC-0002 — clause migration rows (rev9 → rev10 compaction)

Source: `_bootstrap/rfc-phase/rfcs/RFC-0002-observation-evaluation-reconciliation.md`
(9,323 words, RFC2-1 … RFC2-25, five §8 questions).
Target: `../rfcs/RFC-0002/` — a four-module contract package (split authorized by the
lead after the single compacted file measured 7,554 words, above OD-R10-3's
~7,000 default-load ceiling). The single file no longer exists.
History: `../history/RFC-0002-history.md`.

**Lettered sub-clauses:** rev9 RFC 0002 has **none** — no `RFC2-n(x)`
identifier exists in the source. (Lettered forms appearing in the text —
`RFC3-16(a)`, `RFC4-13(a)/(b)`, `RFC1-18(b)`, `RFC3-17(a)`, `VIS-6 exception
(b)` — are citations of other contracts, not this RFC's sub-clauses.) Rows
below are therefore one per numbered clause plus one per §8 question.

**Clause accounting:** 25 in, 25 out. No merges, no retirements, no
renumbering; the range stays contiguous RFC2-1 … RFC2-25.

| clause | outcome | target | reason |
|---|---|---|---|
| RFC2-1 | retained with wording sharpened | `RFC-0002/snapshot-and-evaluation-core.md` | All 11 list items copied verbatim and un-renumbered; only the item-11 `*(History: …)*` parenthetical moved, and the "never renumber" warning was hoisted into the lead-in |
| RFC2-2 | retained unchanged | `RFC-0002/snapshot-and-evaluation-core.md` | Closed rule and its Unknown routing carry no removable narrative |
| RFC2-3 | retained unchanged | `RFC-0002/snapshot-and-evaluation-core.md` | Evaluation-identity rule, the kind-is-not-identity prohibition, and the VIS-7 identity test are all rule text |
| RFC2-4 | retained with wording sharpened | `RFC-0002/snapshot-and-evaluation-core.md` | Rule, five permitted inputs, and the corollary intact; the long bracketed justification for the fifth input moved to history, one clause of it kept |
| RFC2-5 | retained unchanged | `RFC-0002/snapshot-and-evaluation-core.md` | Two-level identity is already minimal |
| RFC2-6 | retained with wording sharpened | `RFC-0002/snapshot-and-evaluation-core.md` | Full contents enumeration and VIS-6 exception (b) intact; one clause reworded for length |
| RFC2-7 | retained unchanged | `RFC-0002/snapshot-and-evaluation-core.md` | Overlay recording requirements and the no-consent-no-overlay rule are rule text |
| RFC2-8 | retained unchanged | `RFC-0002/snapshot-and-evaluation-core.md` | Authority ceiling and conservative-suspension default unchanged |
| RFC2-9 | retained with wording sharpened | `RFC-0002/snapshot-and-evaluation-core.md` | Mechanism, the three Unknown outcomes and the RFC3-16(a) authorization-bearing paragraph intact; two clauses tightened. Cited as the RFC3-16(a) example — ID and semantics unchanged |
| RFC2-10 | retained unchanged | `RFC-0002/snapshot-and-evaluation-core.md` | Four freshness states and the identity-test participation are closed vocabulary |
| RFC2-11 | retained unchanged | `RFC-0002/snapshot-and-evaluation-core.md` | Evidence–revision binding is one rule, already minimal |
| RFC2-12 | retained unchanged | `RFC-0002/challenge-lifecycle.md` | Four admissibility criteria and the inadmissible list are the doctrine floor |
| RFC2-13 | retained with wording sharpened | `RFC-0002/challenge-lifecycle.md` | Every rule kept — state machine, mechanical/judgment split, both senses of "deterministic", `challenge-pending`, latency/resolution/sweep policies under RFC3-16(a) with their forgeability arguments, the B2 split table, four resolutions, provider revocation, expiry-as-eligibility, B1 sweep requirement. ~1,900 → ~1,290 words by cutting connective prose only; record-immutability and withdrawal semantics (cited by RFC-0003) unchanged |
| RFC2-14 | retained unchanged | `RFC-0002/challenge-lifecycle.md` | Suspension-is-not-erasure is one rule |
| RFC2-15 | retained unchanged | `RFC-0002/reconciliation-chain.md` | Contradiction/gap definitions and the two closed gap exits copied |
| RFC2-16 | retained unchanged | `RFC-0002/reconciliation-chain.md` | Aligned/Converged predicates and the three added operational rules kept |
| RFC2-17 | retained with wording sharpened | `RFC-0002/reconciliation-chain.md` | Both word reservations kept at full strength; the archived-corpus survey citation compressed to a pointer, detail in history |
| RFC2-18 | retained with wording sharpened | `RFC-0002/reconciliation-chain.md` | Chain state machine, snapshot-only computation rule, all four outcomes, the paired-state obligation (owner answer to q4) and the record rule intact; the q4 rationale tail and one identity restatement moved to history. §8 q3's governed-checker route added inline as the `reconciled@E` gate route |
| RFC2-19 | retained unchanged | `RFC-0002/reconciliation-chain.md` | Human-trigger rule and SDR-12 V0/V1 staging, including "a wall of such Unknowns … is correct output" |
| RFC2-20 | retained unchanged | `RFC-0002/reconciliation-chain.md` | Closure fallacy and the snapshot-only computation restatement |
| RFC2-21 | retained unchanged | `RFC-0002/reconciliation-chain.md` | Four no-gap conditions and the four explicit non-meanings |
| RFC2-22 | retained unchanged | `RFC-0002/reconciliation-chain.md` | Fixed-point rule and the per-snapshot qualification |
| RFC2-23 | retained unchanged | `RFC-0002/rendering-vocabularies.md` | Six-row failure-state table copied verbatim, including "**Unknown, never zero**" |
| RFC2-24 | retained with wording sharpened | `RFC-0002/rendering-vocabularies.md` | Twelve-row table copied verbatim in Condition and Resolution-route columns; the per-cell `*Added:*` / `*Renamed:*` amendment narratives moved to history with a backlink; closure preamble, secondary-annotation closure, A5 cite and the RFC6-17 rendering rule kept. Owner decision A5 retained in-clause |
| RFC2-25 | retained with wording sharpened | `RFC-0002/rendering-vocabularies.md` | Six-tier table copied verbatim; three sibling surface states (incl. `unadopted-draft`, cited by RFC-0003) and the `editorial-draft`/`challenge-pending` notes kept; owner decision B10 retained in-clause, its `*(History: …)*` wrapper moved |
| q1 | answered — moved to history | history §8; stub in `RFC-0002/rendering-vocabularies.md` §8 | A5: twelve reasons, #12 added, #11 retained, #10 not split. Indexed in `RFC-0002/README.md` §8 and carried by RFC2-24 |
| q2 | answered — moved to history | history §8; stub in `RFC-0002/challenge-lifecycle.md` §8 | B1: expiry stays eligibility; sweep policy required. Carried by RFC2-13 |
| q3 | answered — moved to history | history §8; stub in `RFC-0002/reconciliation-chain.md` §8 | Governed diff-satisfies-clause check is a lawful `gate-backed` route (RFC4-13 route 4 / RFC4-13(b)). Carried by RFC2-18 and RFC2-25 |
| q4 | answered — moved to history | history §8; stub in `RFC-0002/reconciliation-chain.md` §8 | Warranted-revision binding stands; one paired state. Carried by RFC2-18 |
| q5 | answered — moved to history | history §8; stub in `RFC-0002/challenge-lifecycle.md` §8 | B2: admission split by challenger. Carried by RFC2-13 |

## Also moved to history (not clause-scoped)

| item | outcome | target | reason |
|---|---|---|---|
| §6 Alternatives considered | moved to rationale/history | history §6 | Tier 2 wholesale; two load-bearing alternatives (fourth label; current-intent binding) keep one sentence each in `RFC-0002/README.md` §6 with a pointer |
| Archived-corpus citations | moved to rationale/history | history, final section | `06`/`07`/`04` briefs, `DISPOSITIONS-03`, T-F9/R-11 — informative in every case; the rules stand without them |
| End-marker provenance note | moved to rationale/history | history | Amendment record, no normative content |

## Word accounting

| | words |
|---|---|
| rev9 source | 9,323 |
| compacted contract, single file (superseded) | 7,554 |
| history file | 2,627 |
| contract-text reduction | 1,769 (19%) |

**As the four-module package** (`wc -w`):

| module | clauses | words |
|---|---|---|
| `README.md` (package index) | — | 1,818 |
| `snapshot-and-evaluation-core.md` | RFC2-1..RFC2-11 | 1,964 |
| `challenge-lifecycle.md` | RFC2-12..RFC2-14 | 2,231 |
| `reconciliation-chain.md` | RFC2-15..RFC2-22 | 2,477 |
| `rendering-vocabularies.md` | RFC2-23..RFC2-25 | 2,397 |
| **package total** | RFC2-1..RFC2-25 | **10,887** |

Every module sits inside OD-R10-3's 2,000–6,000 module band (module 1 marginally
below it) and far under the ~7,000 default-load ceiling the single file breached
— which is the point of the split: a reader answering one question now loads
~2,000–2,500 words plus the index, not 7,554.

The package total exceeds the single file by 3,333 words. That delta is
**module scaffolding, not new contract**: five sets of front matter, status
header, package pointer, serves line, reader map, and module-local integration.
Clause text is byte-identical to the single file (verified below), so no
normative content was added, moved, or duplicated.

The ~4,500-word target was **not reached**. Rev9 RFC 0002 contains roughly
1,500–1,800 words of Tier 2 material in total (`*(History: …)*`
parentheticals ~120; §6 alternatives ~250; §8 questions and answers ~1,150;
scattered amendment narrative ~250) — and that is very nearly the whole of
what was removed. The remainder is Tier 1 by the charter's own definition:
three closed vocabularies (twelve Unknown reasons, six rendering tiers, three
sibling surface states), two state machines (challenge lifecycle,
reconciliation chain), an eleven-item snapshot input list whose numbering is
cited by other RFCs, a six-row failure/degradation table, fifteen violation
cases, and 25 numbered clauses of rule text. Tables and enumerated lists alone
account for ~1,400 words that the charter requires be copied, not paraphrased.
Reaching 4,500 would require deleting roughly 3,000 words of Tier 1 — that is,
weakening obligations — so this pass stopped at the smallest faithful size
per the charter's word-target rule.

## Preservation checks run (this session, mechanically)

- 11/11 RFC2-1 list items present, in order, un-renumbered.
- RFC2-24 twelve reasons and RFC2-23 six failure states present with identical
  spellings; RFC2-25 six tiers plus three sibling surface states present.
- `unadopted-draft` (RFC2-25) and RFC2-13's record-immutability / withdrawal
  semantics unchanged — RFC-0003 citations still resolve.
- Owner decision identifiers surviving in the active file: **A5**, **B1**,
  **B2**, **B10**, and the q3/q4 acceptance answers (§8 table). None dropped.
- Security premises retained with reasoning, not just conclusion: the
  untrusted-tree / forgeable-from-inside-the-tree argument for currency bounds
  (RFC2-9), admission-latency bounds, resolution policies and sweep policies
  (RFC2-13); the B2 denial-of-truth and VIS-4 self-certification argument.
- Preserved owner language kept verbatim: "a wall of such Unknowns on a
  fleet-built project is correct output, not a defect"; "merged, not yet
  evaluated"; "reconciled against what was approved; N gaps against intent as
  it now stands"; "**Unknown, never zero**"; "the badge flipped overnight".
- Every obligation-bearing sentence in rev9 (`must` / `never` / `only` /
  `no implementation` / `forbid` — 112 sentences) was diffed against the
  compacted file. 23 had no close counterpart; each was inspected
  individually. 22 were non-normative §0/§1 summary restatements, archived
  corpus citations, §6/§8 text, or RFC2-24 table-cell amendment narrative —
  all with their rules still live in a clause or their text moved verbatim to
  history. One was a genuine precision loss ("the act itself is not subject
  to the VIS-7 identity test", RFC2-13) and was **restored** before this file
  was finalised.
- Status header matches the charter's two-state text verbatim (string
  compare). Front matter parses as YAML. No `_bootstrap/` path is cited in
  active normative text (grep: zero hits).
- Cross-RFC citations in the active file, all by clause ID, none by section
  number: RFC1-5/15/18/18(b)/25/26; RFC3-2/15/16/16(a)/16(b)/17(a);
  RFC4-13/13(a)/13(b); RFC5-13/25; RFC6-13/14/17/22/23; RFC7-16/20.

## Package-split verification (re-run after the split)

- **Clause coverage:** each of the 25 `RFC2-n` clause headings appears in
  **exactly one** module (programmatic count). Ranges are contiguous and
  exhaustive; the README lookup rule resolves any `RFC2-n` by integer alone,
  since RFC 0002 has no lettered sub-clauses.
- **Clause text:** every clause's normalized text is **byte-identical** to the
  validated single file — modules were produced by slicing it at sub-section
  boundaries, not by retyping.
- **Obligation sweep re-run** over the package union: of rev9's 112
  obligation-bearing sentences, 23 lacked a close counterpart in the single
  file (all audited and accounted for previously); against the package it is
  **22**, and **zero were newly introduced by the split**. The split surfaced
  two sentences the single file's §8 answer table had been carrying that the
  package index would have shortened away — q4's "never as two independent
  aggregates" and the end marker's "add lettered sub-clauses" permission. Both
  were **restored** (module 3 §8 stub + README §8 row; README end marker)
  before the single file was deleted.
- **Violation cases 1–15** each appear exactly once across the package; cases
  3, 5 and 11 span two modules and are held at package level per the
  owning-clause rule.
- **§8 numbering** is RFC-level and immutable: q1→module 4, q2/q5→module 2,
  q3/q4→module 3, all five indexed in `README.md` §8.
- Front matter parses as YAML in all five files; `_bootstrap/` appears in no
  active package text.
- The single file `rfcs/RFC-0002-observation-evaluation-reconciliation.md` was
  deleted only after all of the above passed.

## Judgment call flagged, not made

**q1(b) — splitting #10.** Owner decision A5 closes the Unknown-reason list
"at twelve" and does not mention the observer-failure / source-unreachable
split that q1(b) asked about. Closing at twelve with #10 intact entails "not
split", and the active RFC2-24 now states that explicitly rather than leaving
it ambiguous. This is an inference from an answer's scope, not a recorded
owner ruling; noted in `../history/RFC-0002-history.md` under q1 for the
lead's confirmation.
