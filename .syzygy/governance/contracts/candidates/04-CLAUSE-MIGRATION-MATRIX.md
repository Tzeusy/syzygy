# Clause migration matrix — rev9 → rev10 (directive §3, semantic preservation)

One row for every rev9 numbered clause, lettered sub-clause, and §8
question, each with exactly one outcome from the closed vocabulary:
`retained unchanged` · `retained with wording sharpened` · `merged into <clause>`
· `moved to rationale/history` · `routed to OpenSpec candidate` · `routed to
craft-and-care` · `retired as superseded/redundant`; §8 rows use `open —
retained` / `answered — moved to history`; rev10-new clauses are marked
`new at rev10`. Every move/merge row names its target and reason
(backlink). Conventions: limb rows (list items inside one clause body,
e.g. RFC5-6's bullets) are supplementary accountability rows, marked as
such by their pass; they are not clause identities. Each per-RFC section's
preamble carries that pass's verification-sweep results.

**Global tallies (verified by `scripts/verify_final_prespec.py`):** all 294
rev9 numbered clauses survive with identities unchanged — zero merged,
zero retired, zero renumbered, zero routed out of the active path; **1** new
sub-clause at rev10 — RFC3-16(c) — beyond the 294 + RFC10-1..16 +
RFC11-1..12 (new contracts). The single clause-text semantic resolution of the pass
(RFC8-25's superseded fallback) and every other substantive ruling are
listed in `WORKER-REPORT-DIGEST.md` §"Substantive rulings" for the
semantic-equivalence review.

---

<!-- ======== RFC-0001 ======== -->

# RFC-0001 — clause migration rows (rev9 → rev10 compaction)

Source: `_bootstrap/rfc-phase/rfcs/RFC-0001-project-graph-identity-state-planes.md`
(frozen rev9, 9,534 words). Target:
`final-prespec/rfcs/RFC-0001-project-graph-identity-state-planes.md`
(8,350 words, of which 1,919 are verbatim-copied tables and closed
enumerations). History: `final-prespec/history/RFC-0001-history.md`.

No clause was retired, merged, renumbered, or routed out. Every rev9 clause and
lettered sub-clause survives in the active contract at its original identifier.

| Clause | Outcome | Target | Reason |
|---|---|---|---|
| RFC1-1 | retained with wording sharpened | active §3.1 | Rule and both surfacing contexts unchanged; the zero-roots justification compressed to one clause. |
| RFC1-2 | retained with wording sharpened | active §3.1 | `*(History: …)*` parenthetical moved to history; the SDR §4 divergence now cites owner decision B22 explicitly. |
| RFC1-3 | retained with wording sharpened | active §3.1 | SEC-4/SEC-2 premises verbatim; only the forward-reference parenthetical shortened. |
| RFC1-4 | retained unchanged | active §3.1 | Two-authority rule already minimal. |
| RFC1-5 | retained unchanged | active §3.2 | Closed entity table copied verbatim, all 25 rows. |
| RFC1-6 | retained unchanged | active §3.2 | Both deliberate narrowings and their `[Inferred]`/`[Observed]` labels intact. |
| RFC1-7 | retained unchanged | active §3.2 | Extension-profile enumeration is a closed vocabulary. |
| RFC1-8 | retained unchanged | active §3.2 | Frozen-noun mapping is definitional. |
| RFC1-9 | retained with wording sharpened | active §3.3 | Obligation and RFC 0003 delegation verbatim in force; the collision worked-example compressed. |
| RFC1-10 | retained unchanged | active §3.3 | Opaque-identifier rule already minimal. |
| RFC1-11 | retained unchanged | active §3.3 | Split/merge successor rule and rendered-event obligation intact. |
| RFC1-12 | retained unchanged | active §3.3 | No-silent-transfer rule plus its `[Inferred]` label retained. |
| RFC1-13 | retained unchanged | active §3.3 | Map-anchor reliance list is what RFC 0009 cites. |
| RFC1-14 | retained unchanged | active §3.4 | Contains the verbatim architecture.md capability definition. |
| RFC1-15 | retained unchanged | active §3.4 | Reference-not-content rule and its `[Unknown]` label retained. |
| RFC1-16 | retained unchanged | active §3.4 | SDR-3's four classes are a closed enumeration. |
| RFC1-17 | retained unchanged | active §3.4 | Identity-based counting rule (SDR-22) already minimal. |
| RFC1-18 | retained unchanged | active §3.5 | Two-level identity (SDR-2) and the accepted-instability paragraph intact. |
| RFC1-18(a) | retained with wording sharpened | active §3.5 | Rule verbatim; only the sub-clause provenance parenthetical shortened to its consumer list. |
| RFC1-18(b) | retained with wording sharpened | active §3.5 | `*(History: …)*` moved to history; the clause now cites owner decision B3 with a backlink. |
| RFC1-19 | retained unchanged | active §3.5 | Status-claim/evidence rule (VIS-2) already minimal. |
| RFC1-20 | retained unchanged | active §3.5 | Two-exit gap rule with expiry semantics intact. |
| RFC1-21 | retained unchanged | active §3.5 | Contradiction routing and the derived-gap-is-not-a-warrant rule intact. |
| RFC1-22 | retained with wording sharpened | active §3.6 | Plane table and the closure paragraph copied verbatim; the rev8 rewording note moved to history. |
| RFC1-23 | retained unchanged | active §3.6 | Act-assignment rule and both corollaries (SDR-9) intact. |
| RFC1-24 | retained unchanged | active §3.7 | All-status-through-claims already minimal. |
| RFC1-25 | retained with wording sharpened | active §3.7 | Closed class vocabulary and all 26 relation rows copied verbatim; only the rev8 restatement note moved to history. |
| RFC1-25(a) | retained unchanged | active §3.7 | Records owner decisions A6 and A7 and the closure-vs-re-typing distinction. |
| RFC1-25(b) | retained with wording sharpened | active §3.7 | Four-sense table and the twelve-pair checkable rule verbatim; owner decision B20 now cited at the spelling decision as well as in the `[Inferred]` note. |
| RFC1-25(c) | retained with wording sharpened | active §3.7 | Non-functionality, no-primacy, contradiction, and zero-edge rules verbatim; `*(History: review 8, ML-R8)*` moved to history. |
| RFC1-25(d) | retained with wording sharpened | active §3.7 | All four binding-consequence bullets and the class-is-not-a-plane rule verbatim; the rev7-directive provenance note (directive item B5, **not** owner decision B5) moved to history. |
| RFC1-26 | retained unchanged | active §3.7 | Closure and the owner-decision amendment gate intact. |
| RFC1-27 | retained unchanged | active §3.8 | Proposal kinds and exclusivity-group refusals (VIS-1) intact. |
| RFC1-28 | retained unchanged | active §3.8 | Plan-item resolution (SDR §5 q1) intact. |
| RFC1-29 | retained with wording sharpened | active §3.8 | One-way door, constitutive-record, orphaned-work contradiction, and re-materialization rules all intact; the distributed-act framing compressed. |
| RFC1-30 | retained unchanged | active §3.8 | Decomposition/inheritance default already minimal. |
| RFC1-31 | retained unchanged | active §3.9 | Lifecycle state machine copied verbatim (cited by RFC-0003's lifecycle table and by RFC1-25's `supersedes` pair closure). |
| RFC1-32 | retained unchanged | active §3.10 | No-Feature rule (SDR-1) intact. |

## §8 questions

| Question | Outcome | Target | Reason |
|---|---|---|---|
| q1 | open — retained | active §8.1 | RFC1-12 judgment lapse on split/merge — still the owner's choice. |
| q2 | open — retained | active §8.2 | RFC1-6 no doctrine-claim/contract kernel entities at V0 — still the owner's choice. |
| q3 | open — retained | active §8.3 | RFC1-30 decomposition approval inheritance — still the owner's choice. |
| q4 | answered — moved to history | history "RFC1-18(b)" | Answered at acceptance by owner decision B3; outcome carried by RFC1-18(b) and the `succeeds` derived form. |
| q5 | answered — moved to history | history "RFC1-2" | Answered at acceptance by owner decision B22; outcome carried by RFC1-2. |
| q6 | answered — moved to history | history "RFC1-25(a)/(b)" | Answered at acceptance by owner decisions A6/A7 (with B20); outcome carried by RFC1-25, RFC1-25(a) and RFC1-25(b). The RFC9-9 legend follow-on the question raised is recorded in history as still open for RFC 0009. |

## Non-clause sections

| Section | Outcome | Target | Reason |
|---|---|---|---|
| rev9 §0 Reader's summary | retained with wording sharpened | active §1 | Merged with §1 Summary into one scope + reader map; no normative content in either. |
| rev9 §1 Summary | retained with wording sharpened | active §1 | Merged as above. |
| rev9 §2 Motivation and doctrine grounding | retained with wording sharpened | active §1 / history "§2 (rev9)" | Doctrine-grounding citations and both epistemic labels kept in active §1; the failure-mode essay moved to history. |
| rev9 §4 Violation cases | retained with wording sharpened | active §4 | All eleven cases verbatim; only the section's one-line lead-in shortened. |
| rev9 §5 Integration | retained with wording sharpened | active §5 | Both reliance and left-to-them lists retained (the Proposal identity scheme now named explicitly under 0003); forward-references-are-informative rule verbatim. |
| rev9 §6 Alternatives considered | moved to rationale/history | history "§6 (rev9)" | Moved wholesale; alternative 6.1(i) stays in active §6 as one sentence with a pointer, because RFC1-29's sequencing rule is read against it. |
| rev9 §7 Deliberately deferred | retained unchanged | active §7 | Explicit deferrals are Tier 1. |
| rev9 end-of-contract marker | retained with wording sharpened | active end marker | Now states the clause range **and** that there are no gaps, retirements, or merges. |

<!-- ======== RFC-0002 ======== -->

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

<!-- ======== RFC-0003 ======== -->

# RFC-0003 — clause migration rows (rev9 → rev10)

Source: `_bootstrap/rfc-phase/rfcs/RFC-0003-project-workspace-manifests.md`
(frozen, 10,193 words). Target: the **`../rfcs/RFC-0003/` contract package**
and `../history/RFC-0003-history.md`.

| Target module | Clauses | Words |
|---|---|---|
| `../rfcs/RFC-0003/manifests-and-namespace.md` (**M1**) | RFC3-1…RFC3-14, RFC3-18…RFC3-32 | 4,824 |
| `../rfcs/RFC-0003/governance-homes-and-owner-acts.md` (**M2**) | RFC3-15, RFC3-15(a), RFC3-16, RFC3-16(a), RFC3-16(b), RFC3-16(c), RFC3-17, RFC3-17(a) | 4,275 |
| `../rfcs/RFC-0003/README.md` (index, non-normative, duplicates no clause) | — | 920 |

Compaction produced a single 8,196-word file first; the owner-authorized split
(directive §4 pattern, OD-R10-6) then divided it into the two modules above
**without moving any clause identity**. Both modules are under the ~7,000-word
module ceiling. Lookup rule: numeric part **15–17 → M2** (with every lettered
sub-clause), **everything else → M1**.

**Clause accounting.** Rev9 carried RFC3-1 … RFC3-32 plus four lettered
sub-clauses (RFC3-15(a), RFC3-16(a), RFC3-16(b), RFC3-17(a)) = 36 clause
identities. Rev10 carries the same 36 **plus one new lettered sub-clause,
RFC3-16(c)** = 37, verified present exactly once across the package union with
no clause appearing in both modules. **No clause was merged, retired,
renumbered, or dropped; the RFC3-1 … RFC3-32 range is closed with no gaps.**
Six §8 questions keep their original numbers (q1, q2 in M1; q4 in M2; q3, q5,
q6 answered and moved to history — q3 is *not* renumbered to q1, etc.).
Violation cases keep package-wide numbering 1–14, so each module's list is
non-contiguous; case 9 is the one case split by owning clause (cache/local
limbs → M1 under RFC3-20/21; challenge-admission-record limb → M2 under
RFC3-17(a)).

Rev9 `*(History: …)*` parentheticals extracted: 12 (RFC3-1, RFC3-2 ×2,
RFC3-7, RFC3-14, RFC3-15(a), RFC3-16, RFC3-16(a), RFC3-16(b), RFC3-17(a),
RFC3-19, RFC3-30). All are in the history file verbatim.

| Clause | Outcome | Target | Reason |
|---|---|---|---|
| RFC3-1 | retained with wording sharpened |  M1 (manifests-and-namespace) | YAML-dialect conformance rule kept verbatim; rev7-review-9 provenance parenthetical moved to history. |
| RFC3-2 | retained with wording sharpened |  M1 (manifests-and-namespace) + history | Four write-authority classes, the `kernel-recorded` definition and the minting-trigger rule kept in full; the [Inferred] "why the three original classes did not fit" rationale moved to history. |
| RFC3-3 | retained unchanged |  M1 (manifests-and-namespace) | Direct-write containment; no prose to compress without touching the rule. |
| RFC3-4 | retained with wording sharpened |  M1 (manifests-and-namespace) | Location-is-designation rule unchanged; the rejected field-value alternative reduced to a one-sentence in-place pointer (full text in history §6.2) because RFC3-16(a) reuses its reasoning. |
| RFC3-5 | retained unchanged |  M1 (manifests-and-namespace) | Closed field-set table copied, not paraphrased. |
| RFC3-6 | retained unchanged |  M1 (manifests-and-namespace) | Repository-entry identity and the not-observed → Unknown rule. |
| RFC3-7 | retained with wording sharpened |  M1 (manifests-and-namespace) + history | Both consent kinds and the one-record-per-(Project, provider) rule kept verbatim; owner decision **B8** now cited inline in the clause instead of in a History parenthetical; the AS-R10 amendment narrative moved to history. |
| RFC3-8 | retained unchanged |  M1 (manifests-and-namespace) | Revocation/withdrawal semantics: claim-value, rendering, and enforcement timings all preserved. |
| RFC3-9 | retained unchanged |  M1 (manifests-and-namespace) | Drafting and repair; never-auto-repair rule intact. |
| RFC3-10 | retained with wording sharpened |  M1 (manifests-and-namespace) | VIS-6 exception (a) classification and its [Inferred] justification kept; wording tightened only. |
| RFC3-11 | retained unchanged |  M1 (manifests-and-namespace) | Closed SDR-29 field list. |
| RFC3-12 | retained with wording sharpened |  M1 (manifests-and-namespace) | SDR-30 non-authority rule and derived-portfolio rule unchanged; one clause tightened. |
| RFC3-13 | retained unchanged |  M1 (manifests-and-namespace) | References-never-mints rule and Unknown rendering. |
| RFC3-14 | retained with wording sharpened |  M1 (manifests-and-namespace) + history | Asymmetric-relation bullets and the whole `depends-on` collision consequence (RFC1-25(b) elevated to a tested invariant) kept at full strength; owner decision **B20** cited inline; the "a draft had renamed it to `relies-on-project`" amendment parenthetical moved to history. |
| RFC3-15 | retained unchanged |  M2 (governance-homes) | Five-category table and the six-name validator rule copied, not paraphrased. |
| RFC3-15(a) | retained with wording sharpened |  M2 (governance-homes) + history | B19 attribution, the durability argument and the "widen explicitly, never stretch 'exclusively'" precedent kept; the pre-B19 problem statement moved to history. |
| RFC3-16 | retained with wording sharpened |  M2 (governance-homes) + history | **Directive §2 / OD-R10-5 repair.** Closed lifecycle table copied verbatim; the effective-status text now reads status *from the owner-act record* whose verification state is two-valued per RFC3-16(c). **One rule is deliberately relaxed, not unchanged** (equivalence-review E1): rev9's unadopted trigger was "no **verifiable** owner-act record" — under which this repository's own uncorrelated bootstrap adoptions bound nothing — and rev10's is "no owner-act record **at all**", so a state-(1) bootstrap record now licenses human governance (the OD-R10-5 repair; machine authorization gates still fail the RFC3-16(a) predicate until correlation). The acceptance-never-edits rule is unchanged. Rev8-rework History parenthetical moved to history. |
| RFC3-16(a) | retained unchanged |  M2 (governance-homes) + history | Predicate, four limbs, the [Inferred] fourth-limb reading rule, the non-exhaustive example list, the untrusted-tree/SEC-3-extension premise and the "mechanism class — chosen, not open" (A1) paragraph all preserved at identical strength, including "owner-held key or attestation custody is not an open implementation alternative … requires a later owner decision". Only the AS-R1 origin parenthetical moved to history. |
| RFC3-16(b) | retained with wording sharpened |  M2 (governance-homes) + history | The nine binding items, the Bootstrap-correlation paragraph, "Effect when the predicate fails" and "One predicate, one home" all retained; the gate list compressed to bare clause IDs with its "tracks the gates; does not bound them" rule intact. Provenance parenthetical (directive item B2, **not** owner decision B2) moved to history. **One rule is inserted, not merely retained** — disclosed 2026-08-05, see the change log at the end of this file. The Bootstrap-correlation paragraph gains a **role split** absent from rev9: what a state-(1) (owner-adopted, uncorrelated) record *suffices for* now depends on how the artifact is consumed — an artifact consumed as a **constraint** binds at full strength (refusing to apply a constraint over uncorrelated provenance would widen, not narrow), while an artifact consumed as an **authorization for an effect** (a consent, an autonomy envelope, a write-expanding policy) has **not** satisfied the RFC3-16(a) predicate on a state-(1) record alone, and *Effect when the predicate fails* governs that effect until the correlation act (RFC10-9 is the worked example). **Authorizing direction:** OD-R10-5, "acceptance semantics repaired without weakening" (`02-OWNER-DIRECTION-RECORD.md`), implemented together with the RFC3-16 relaxation and RFC3-16(c); the split's direction is fail-closed. The insertion mints no clause identity, so it adds no row and does not change the new-clause tally above. |
| **RFC3-16(c)** | **new at rev10 — directive §2 repair** |  M2 (governance-homes) | Names the two provenance states — *owner-adopted (bootstrap act)* vs *Syzygy-verified (effective act)* — so RFC 0003, the acceptance record and other artifacts can cite them instead of conflating them (adversarial finding F1). Lettered so the RFC3-1..RFC3-32 range stays closed. Weakens nothing *for Syzygy's own claims* — it re-states "git commits or tags alone are never sufficient" at preserved strength and defers to RFC3-16(a)'s failure effects; the deliberate human-governance relaxation it implements is recorded on the RFC3-16 row above, not hidden here. |
| RFC3-17 | retained unchanged |  M2 (governance-homes) | `declarations/` reservation and its owner-sign-off install gate. |
| RFC3-17(a) | retained with wording sharpened |  M2 (governance-homes) + history | Home, `kernel-recorded` authority, the no-`governance/challenges/` prohibition and every "Consequences that bind" rule kept; the long "Why `records/` and nothing else" reasoning compressed in place (each exclusion still named) with the full text in history. B19 rewrite parenthetical moved to history. |
| RFC3-18 | retained unchanged |  M1 (manifests-and-namespace) | Surface-namespace class rule. |
| RFC3-19 | retained with wording sharpened |  M1 (manifests-and-namespace) + history | The pin-the-warranted-intent-revision schema obligation kept; the resolved RFC1-29 defect-handoff narrative (and its §5 companion paragraph) moved to history. |
| RFC3-20 | retained unchanged |  M1 (manifests-and-namespace) | `cache/` deletion-safety invariant and the observation-records-are-not-cache rule. |
| RFC3-21 | retained unchanged |  M1 (manifests-and-namespace) | `local/` presentation-state rule and the promotion-only path to authority. |
| RFC3-22 | retained unchanged |  M1 (manifests-and-namespace) | Version stamps as snapshot inputs. |
| RFC3-23 | retained unchanged |  M1 (manifests-and-namespace) | Identity-preserving migration list; semantic-change escalation. |
| RFC3-24 | retained unchanged |  M1 (manifests-and-namespace) | Explicit, reviewed, revertable migration; CC-REV-1 class 5. |
| RFC3-25 | retained unchanged |  M1 (manifests-and-namespace) | Forward/backward behavior; no silent downgrade. |
| RFC3-26 | retained unchanged |  M1 (manifests-and-namespace) | `openspec/**` outside Syzygy's migration authority. |
| RFC3-27 | retained unchanged |  M1 (manifests-and-namespace) | What Syzygy reads from `openspec/**`; adapter-vs-contract split. |
| RFC3-28 | retained unchanged |  M1 (manifests-and-namespace) | Spec anchors; degrade-never-guess; the [Unknown] identity-survival label preserved. |
| RFC3-29 | retained unchanged |  M1 (manifests-and-namespace) | One plane per repository; no directory-scoped sub-roots. |
| RFC3-30 | retained with wording sharpened |  M1 (manifests-and-namespace) + history | Per-pair role/consent rule, read-only observation of B's plane, and the whole observing-project-governs-policy paragraph (including its RFC3-16(a) dependency and the [Inferred] compromised-B argument) kept; AS-R7 parenthetical moved to history. |
| RFC3-31 | retained unchanged |  M1 (manifests-and-namespace) | Composition by declaration; derived recursion; cycle rendering. |
| RFC3-32 | retained with wording sharpened |  M1 (manifests-and-namespace) | Parent prohibitions and the RFC6-17 full-composition disclosure obligation kept whole; the laundering example tightened by one sentence. |

## §8 question rows

| Question | Outcome | Target | Note |
|---|---|---|---|
| q1 (monorepo subprojects, RFC3-29) | open — retained | M1 §7 | Foreclosure of many governed projects in one repository still needs the owner's word; unaffected by compaction or the split. |
| q2 (workspace manifest classification, RFC3-10) | open — retained | M1 §7 | VIS-6 exception (a) rebuildability trade still open. |
| q3 (egress consent granularity, RFC3-7) | answered — moved to history | history §8 | B8: one record per (project, provider); ruling carried inline in RFC3-7 (M1). |
| q4 (`declarations/` category, RFC3-17) | open — retained | M2 §5 | B19 settled only the challenge half; drafted default (reservation outside the constitutional five) stands, reversible by amendment. |
| q5 (owner-act provenance predicate, RFC3-16(a)) | answered — moved to history | history §8 | A1/A9: ceremony + independent audit trail; the A9 interim posture is what RFC3-16(c) now names as state (1). |
| q6 (governance home for challenges, RFC3-17(a)) | answered — moved to history | history §8 | B19: `records/` + `kernel-recorded`; carried in RFC3-15/15(a)/17(a) (M2). |

## Preservation checks run

All sweeps below were executed against the **package union** (M1 + M2
concatenated), re-run after the split; the pre-split single file was deleted
only once they passed.

- **Clause identities.** 37 clause openers found in the union — RFC3-1…RFC3-32
  plus RFC3-15(a), RFC3-16(a), RFC3-16(b), RFC3-16(c), RFC3-17(a) — with the
  intersection of the two modules' clause sets **empty**: no clause appears
  twice, none is missing, none renumbered.
- **Owner decisions and identifiers — swept, not assumed.** All 23 decision
  and provenance tokens appearing anywhere in the rev9 source (A1, A9, B2 —
  the directive item, not the owner decision —, B8, B19, B20, AS-R1, AS-R7,
  AS-R8, AS-R10, S6, CC-REV-1, FD-034, OQ-010, T15, SDR-4, SDR-7, SDR-8,
  SDR-10, SDR-28, SDR-29, SDR-30, SDR-32) were enumerated from the frozen
  source and each confirmed present in the package, README, or history.
  **Zero missing.** Separately, all 16 tokens carried by the pre-split single
  file were confirmed present in the package union alone — **the split lost
  none**. (D1/D2 and CT-* never appear in RFC 0003.)
- **Cross-RFC citations — swept twice.** 90 unique `RFCn-m` citations in rev9;
  89 survive in the active contract. The two that left — `RFC5-6` and
  `RFC4-16(2)`, both occurring only inside §6.3 and the answered §8 q5 — are
  preserved verbatim in history. The only citation with no rev9 counterpart is
  `RFC3-16(c)` itself. Across the split: single file 89 unique, package union
  89 unique, **zero lost and zero added**.
- **Security premises.** The untrusted-tree premise, the **[Inferred] SEC-3
  extension to workers' *commits*** (a standing owner-attention item), VIS-7's
  trust floor, the RFC5-25 outside-the-tree location constraint and the
  compromised-B nearest-plane argument all retain their reasoning, not only
  their conclusions. The first three live in M2 (RFC3-16(a)); the last in M1
  (RFC3-30), which cites RFC3-16(a) rather than restating it.
- **Epistemic labels.** rev9, the pre-split single file, and the package union
  each carry 12 `[Inferred]`, 4 `[Observed]`, 1 `[Unknown]` — identical across
  the split. Versus rev9 the composition differs by exactly two entries:
  RFC3-2's `[Inferred]` class-fit rationale moved to history, and RFC3-16(c)
  added its own label line. No retained claim lost its label.
- **No `_bootstrap/` paths remain in active normative text** (checked); the
  two rev9 occurrences (RFC3-16(b)'s directive reference and §3.9's seed-file
  citation) are in history or reduced to an unpathed `[Observed]`.
- **Verbatim blocks — located after the split.** RFC3-5's field table in M1;
  RFC3-15's category table, RFC3-16's lifecycle table, RFC3-16(b)'s nine items
  and RFC3-16(a)'s example list in M2. Copied, not paraphrased (990 words in
  total).
- **Violation cases.** All 13 rev9 cases retained; one new case (14) added for
  RFC3-16(c). Across the union the numbers 1–14 each appear once, except **9,
  which appears in both modules by design** — its limbs were divided by owning
  clause and each module states where the other limbs live.

<!-- ======== RFC-0004 ======== -->

# RFC-0004 — clause migration rows (rev9 → rev10 compaction)

Source: `_bootstrap/rfc-phase/rfcs/RFC-0004-observation-sources-evidence-adapters.md` (frozen, 9,621 words).
Target: `final-prespec/rfcs/RFC-0004/` — a four-module contract package
(10,558 words including index and per-module front matter; 8,882 across the
four modules). The interim single-file compaction was superseded by the
package and removed; module boundaries carry no normative weight.
History: `final-prespec/history/RFC-0004-history.md` (single file, unchanged path).

**No clause was merged, retired, renumbered, or routed out.** Active range
RFC4-1…RFC4-29 with sub-clauses RFC4-13(a) and RFC4-13(b); no gaps, and every
clause identity appears in exactly one module (verified mechanically).
"Retained with wording sharpened" here always means the *rule* is unchanged
and only amendment narrative and/or research-corpus (`_bootstrap/`) citation
paths moved to history — every MUST/never/only survives at identical strength.

| Module | Clauses | Words |
|---|---|---|
| `RFC-0004/general-contract.md` | RFC4-1..RFC4-9 | 1,680 |
| `RFC-0004/named-adapters.md` | RFC4-10..RFC4-17, incl. RFC4-13(a)/(b) | 3,685 |
| `RFC-0004/execution-record.md` | RFC4-18..RFC4-21 | 1,775 |
| `RFC-0004/fidelity-joins-and-mappings.md` | RFC4-22..RFC4-29 | 1,742 |
| `RFC-0004/README.md` (index, package-level items) | — | 1,676 |

## Numbered clauses and lettered sub-clauses

| Clause | Outcome | Target | Reason |
|---|---|---|---|
| RFC4-1 | retained unchanged | `RFC-0004/general-contract.md` §3 | Observer/adapter definitions and the one-adapter-per-authority rule; copied verbatim |
| RFC4-2 | retained with wording sharpened | `RFC-0004/general-contract.md` §3 | Seven-item declaration set copied; only the trailing `architecture.md` aside in item 1 dropped |
| RFC4-3 | retained with wording sharpened | `RFC-0004/general-contract.md` §3 | Emission obligations verbatim; the `04` §4 attribution on the capture-instant distinction moved to history |
| RFC4-4 | retained unchanged | `RFC-0004/general-contract.md` §3 | Failure-rendering and fail-closed rule; copied verbatim |
| RFC4-5 | retained with wording sharpened | `RFC-0004/general-contract.md` §3 | Both limbs and the [Inferred] past-evidence clarification retained; the `06` §5.2 adoption note moved to history |
| RFC4-6 | retained with wording sharpened | `RFC-0004/general-contract.md` §3 | Substrate-translation rule verbatim; the `04` §4 `bead_id` analysis citation moved to history |
| RFC4-7 | retained unchanged | `RFC-0004/general-contract.md` §3 | Registry clause including the full RFC3-16(a) laundering premise; copied verbatim |
| RFC4-8 | retained with wording sharpened | `RFC-0004/general-contract.md` §3 | Skew rules (a)–(e) intact; two parenthetical restatements condensed, no obligation touched |
| RFC4-9 | retained unchanged | `RFC-0004/general-contract.md` §3 | Substitution-as-registry-event rule; copied verbatim |
| RFC4-10 | retained with wording sharpened | `RFC-0004/named-adapters.md` §3 | OpenSpec anchors, stability class, and Unknown-never-rejection retained; connective prose tightened |
| RFC4-11 | retained with wording sharpened | `RFC-0004/named-adapters.md` §3 | Read surface, merge-fact exclusivity, and squash fidelity rule retained; `04` §5.4(a) citation moved to history |
| RFC4-12 | retained with wording sharpened | `RFC-0004/named-adapters.md` §3 | Secret-policy RFC3-16(a) premise and the not-path-only identity scheme retained verbatim; one connective shortened |
| RFC4-13 | retained with wording sharpened | `RFC-0004/named-adapters.md` §3 | Both predicates, all four routes, the `report-fact` cap, and the CC-TEST-2 quotation retained; the AS-R3/A2 amendment header and two `*(History: …)*` parentheticals moved to history; route 4's `return PASS` illustration now points at RFC4-13(b) rather than restating it |
| RFC4-13(a) | retained with wording sharpened | `RFC-0004/named-adapters.md` §3 | Seven-item capture-artifact list and the immutability consequences copied; the rev7 blocker-A3 origin parenthetical moved to history |
| RFC4-13(b) | retained with wording sharpened | `RFC-0004/named-adapters.md` §3 | Both artifact lists, the separation-of-authorship rule, and the `return PASS` acceptance test copied; the rev7 blocker-A5 origin parenthetical moved to history |
| RFC4-14 | retained with wording sharpened | `RFC-0004/named-adapters.md` §3 | Runtime-observer boundary and one-off-capture rule retained; one clause reworded, SEC-3 block unchanged |
| RFC4-15 | retained with wording sharpened | `RFC-0004/named-adapters.md` §3 | Never-hardcode status vocabulary, write list, and degraded modes retained; three research-corpus citations moved to history |
| RFC4-16 | retained with wording sharpened | `RFC-0004/named-adapters.md` §3 | All four items retained including both RFC3-16(a) premises and the declare-not-enforce boundary; the AS-R16 parenthetical and `06` §8.2/§8.3 citations moved to history |
| RFC4-17 | retained with wording sharpened | `RFC-0004/named-adapters.md` §3 | Warrant-pointer outward-limb rule verbatim; the `06` §5.3 failure-analysis citation moved to history |
| RFC4-18 | retained unchanged | `RFC-0004/execution-record.md` §3 | Execution Record as an Evidence kind, no new doctrine class; copied verbatim |
| RFC4-19 | retained with wording sharpened | `RFC-0004/execution-record.md` §3 | Envelope table copied cell-for-cell; the `required-where-available` rename parenthetical and three in-table research-corpus citations moved to history |
| RFC4-20 | retained with wording sharpened | `RFC-0004/execution-record.md` §3 | Enrichment-non-required rule and the full collision safeguard retained, including "a silent single record is a violation"; owner decision B11 now cited inline, its §8 q1 text in history |
| RFC4-21 | retained with wording sharpened | `RFC-0004/execution-record.md` §3 | Unknown-never-zero, Inferred cost labeling, and partial-aggregate disclosure retained; two `06` §6 citations moved to history |
| RFC4-22 | retained with wording sharpened | `RFC-0004/fidelity-joins-and-mappings.md` §3 | Declared join bases and the convention-is-not-a-guarantee rule retained; `04` §4 / `06` §7 citations moved to history |
| RFC4-23 | retained with wording sharpened | `RFC-0004/fidelity-joins-and-mappings.md` §3 | All four liveness items retained including the RFC3-16(a) staleness-bound premise; `06` §3.2a citation moved to history |
| RFC4-24 | retained with wording sharpened | `RFC-0004/fidelity-joins-and-mappings.md` §3 | Closed cause list copied in full; the in-list "added post-draft under review 3's AS-R4" attribution moved to history |
| RFC4-25 | retained unchanged | `RFC-0004/fidelity-joins-and-mappings.md` §3 | Degradation mapping duty; copied verbatim |
| RFC4-26 | retained unchanged | `RFC-0004/fidelity-joins-and-mappings.md` §3 | Declaration sites and the marker-adoption RFC3-16(a) premise; copied verbatim |
| RFC4-27 | retained unchanged | `RFC-0004/fidelity-joins-and-mappings.md` §3 | Executed mapping-coverage record behind every absence claim; copied verbatim |
| RFC4-28 | retained with wording sharpened | `RFC-0004/fidelity-joins-and-mappings.md` §3 | Derivation-first invariant copied verbatim except one rev9 line-break artifact (`branch/worktree/` + newline + `commit/PR/merge`, which renders with a stray space) joined; no other change |
| RFC4-29 | retained with wording sharpened | `RFC-0004/fidelity-joins-and-mappings.md` §3 | Enrichment roadmap and the never-required rule retained; the `06` §5.3 routing-note citation moved to history |

## §8 owner questions

| Question | Outcome | Target | Reason |
|---|---|---|---|
| q1 | answered — moved to history | history §8 q1; stub in `RFC-0004/execution-record.md` §8 | Owner decision B11 (derive, disclose collisions); a one-line answered stub with the decision ID stays with its clause and the safeguard itself is normative in RFC4-20 |
| q2 | open — retained | `RFC-0004/execution-record.md` §8 | Envelope minimality: whether `terminal outcome` R applies to field or value; proposal stated, confirmation outstanding |
| q3 | open — retained | `RFC-0004/fidelity-joins-and-mappings.md` §8 | Marker-adoption granularity (per project vs per repository); authenticity requirement unaffected at any granularity |
| q4 | open — retained | `RFC-0004/named-adapters.md` §8 | Capture-cadence confirmation; the maximum inter-pass interval value remains an undeclared open default and is flagged as such |
| q5 | answered — moved to history | history §8 q5; stub in `RFC-0004/README.md` §5 and §8 index | All four RFC 0001 defects confirmed closed; the stale-confirmation lesson preserved verbatim. Owns no clause, so it sits at package level |
| q6 | answered — moved to history | history §8 q6; stub in `RFC-0004/named-adapters.md` §8 | Owner decision A2 (four routes, route 3 bounded and expiring); the deliberately accepted green-status cost preserved verbatim |

All six appear in the package index table at `RFC-0004/README.md` §8, which
names the owning module for each.

## Supplementary — non-clause material (not required by the charter format)

| Rev9 material | Outcome | Target | Reason |
|---|---|---|---|
| §0 Reader's summary | retained with wording sharpened | `RFC-0004/README.md` package reader map + a §0 module scope in each module | Compressed from nine bullets to a package map plus four module-scope maps; every rule it summarized is normative in a clause |
| §1 Summary | retained with wording sharpened | `RFC-0004/README.md` Scope | Scope paragraph tightened; the contracts-only / no-stack-choice boundary kept verbatim |
| §2 ¶1 doctrine grounding | retained with wording sharpened | `RFC-0004/README.md` §2 | [Observed] doctrine claims and the "confident adapter" [Inferred] failure mode kept; package-level, not duplicated per module |
| §2 ¶2 substrate-audit narrative | moved to rationale/history | history §2 | Non-authoritative audit detail; each finding is separately restated with its own label by the clause that depends on it |
| §4 Violation cases 1–12 | retained unchanged | 1–3 → general-contract; 4, 6–8 → named-adapters; 9 → execution-record; 10–12 → fidelity-joins-and-mappings; 5 → `README.md` §4 | All twelve kept and distributed to the module owning the cited clause, never renumbered; case 5 spans RFC4-11 and RFC4-22 so it is held at package level |
| §5 Relies-on / Provides-to | retained with wording sharpened | `RFC-0004/README.md` §5 + a module-local §5 in each module | Package-level relies-on/provides-to in the index; each module additionally states only its own edges, so no reader assembles them from four files |
| §5 Defects 1–4 | moved to rationale/history | history §5, backlinked from `README.md` §5 | All four resolved upstream; nothing outstanding, nothing blocking — trail preserved verbatim |
| §6 Alternatives (7) | moved to rationale/history | history §6 | Tier 2 wholesale; the "first-class VCS entities" declension stays as one sentence in `README.md` §6 because RFC1-6's delegation is unreadable without it |
| §6 Post-draft adjustments (3) | moved to rationale/history | history, under RFC4-13 / RFC4-20 / RFC4-16 | Amendment-origin narrative filed under the clauses it explains |
| §7 Deliberately deferred | retained with wording sharpened | `RFC-0004/README.md` §7 | Tier 1 explicit deferrals, package-level to avoid duplication; the four undeclared open defaults (retention, inter-pass interval, staleness, currency) named explicitly |

<!-- ======== RFC-0005 ======== -->

# RFC-0005 — rev9 → rev10 migration rows

Source: `_bootstrap/rfc-phase/rfcs/RFC-0005-authentication-consent-execution-profiles.md`
(rev9, frozen, 7,819 words, RFC5-1 … RFC5-26).
Target: the **rev10 contract package** `../rfcs/RFC-0005/` — `README.md` (index),
`admission-and-boundary.md` (module 1), `consent-egress-secrets.md` (module 2),
`execution-profiles.md` (module 3) — and `../history/RFC-0005-history.md`.
The single-file rev10 draft was split under OD-R10-6 and deleted after a
clause-by-clause equality check; every difference between it and the package was
a pointer-only change (restored §3.n section numbering, cross-module § pointers
rewritten to clause IDs).

**Clause identity:** no clause was renumbered, retired, merged, or reused. The
rev10 range is `RFC5-1..RFC5-26`, contiguous, with no gaps.

**Lettered limbs:** rev9's end marker states that lettered limbs (RFC5-18(a)–(e),
RFC3-16(a)/(b) as cited) are *list items inside one clause body, not separate
sub-clauses with their own headings*. RFC 0005 therefore has **no lettered
sub-clauses** in the charter's sense. The internal limbs that are cited
elsewhere are nevertheless given rows below, marked *(limb)*, so their survival
is checkable; each moves with its parent clause.

| Clause | Outcome | Target | Reason |
|---|---|---|---|
| RFC5-1 | retained with wording sharpened | module 1 `admission-and-boundary.md` §3.1 | Closed principal set and the three (a)/(b)/(c) pre-commitments kept intact; framing prose tightened. |
| RFC5-2 | retained unchanged | module 1 `admission-and-boundary.md` §3.1 | Session/credential distinction and the non-transferability rule are already minimal. |
| RFC5-3 | retained with wording sharpened | module 1 `admission-and-boundary.md` §3.2 | Rev9 text kept in full; **rev10 addition** (directive §2 / OD-R10-5) states the two client classes are exhaustive for all present and future clients and that no later contract may introduce a third. Nothing weakened. |
| RFC5-4 | retained with wording sharpened | module 1 `admission-and-boundary.md` §3.2 + history §RFC5-4 | All five bullets and every obligation kept, including B9's binding consequence (declared maximum lifetime; undeclared = no persistence beyond the process; immediate owner-initiated revocation as the entire remaining mitigation). B9 parenthetical and the rev9 declining sentence moved to history with a backlink. |
| RFC5-5 | retained with wording sharpened | module 1 `admission-and-boundary.md` §3.2 | Rev9 text kept in full; **rev10 addition** names the official `syzygy` CLI, agent-protocol adapters (e.g. MCP), scripts, and fleet workers as machine clients without exception, admitted only under RFC5-5/RFC5-6. |
| RFC5-6 | retained unchanged | module 1 `admission-and-boundary.md` §3.3 | Contract-shape bullet list copied verbatim, not paraphrased (charter closed-list rule; work-order instruction). The internal acts-rule pointer still reads §3.5, same module. |
| RFC5-6 *(limb: identity)* | retained unchanged | module 1 `admission-and-boundary.md` §3.3 | One opaque, never-reused identity per credential; survives rotation. |
| RFC5-6 *(limb: issuance)* | retained unchanged | module 1 `admission-and-boundary.md` §3.3 | Owner-attended ceremony only; never self-issued or minted by another credential. |
| RFC5-6 *(limb: scoping)* | retained unchanged | module 1 `admission-and-boundary.md` §3.3 | Deny-by-default; an unscoped credential is invalid, not all-powerful. |
| RFC5-6 *(limb: rotation)* | retained unchanged | module 1 `admission-and-boundary.md` §3.3 | Owner-declared overlap window (may be zero); open default carried at module 1 §8 q5. |
| RFC5-6 *(limb: revocation)* | retained unchanged | module 1 `admission-and-boundary.md` §3.3 | Effective at next request under RFC5-11; recorded. |
| RFC5-6 *(limb: storage)* | retained unchanged | module 1 `admission-and-boundary.md` §3.3 | Verifier-only storage; credential record holds no secret material (SEC-5). |
| RFC5-7 | retained unchanged | module 1 `admission-and-boundary.md` §3.3 | Four-mechanism enumeration (a)–(d) copied verbatim, including the "kernel attests, TCP source address attests nothing" reading and concurrent enablement. The §8 q1 pointer is unchanged and resolves within module 1. |
| RFC5-8 | retained with wording sharpened | module 1 `admission-and-boundary.md` §3.4 | Closed exposure-mode set and the refuse-to-serve rule kept; the "per §1" cross-reference dropped as the sentence it pointed at merged into the module reader map. |
| RFC5-9 | retained unchanged | module 1 `admission-and-boundary.md` §3.4 | Per-mode table copied verbatim (charter table rule), including the device-identity-never-classification cell. |
| RFC5-10 | retained unchanged | module 1 `admission-and-boundary.md` §3.4 | Fresh-install loopback-only rule and the SEC-1 violation quote kept. |
| RFC5-11 | retained with wording sharpened | module 1 `admission-and-boundary.md` §3.5 + history §RFC5-11 | Acts/claims split, the rendering obligation, decision B4's forced evaluation, and the explicit residual all remain normative. The AS-R6 amendment marker and the "what the draft got right" reconciliation essay moved to history; the essay's operative conclusion ("schedules an evaluation, does not mutate a claim") stays in the clause. |
| RFC5-12 | retained with wording sharpened | module 2 `consent-egress-secrets.md` §3.6 + history §RFC5-12 | Four-class closed consent vocabulary and the record-field list kept. The AS-R10 history parenthetical moved; decision **B8** (one record per (project, provider); per-repository declined) stays named in the clause with a history backlink. |
| RFC5-13 | retained with wording sharpened | module 2 `consent-egress-secrets.md` §3.6 | Prospective-revocation rule, the interim-label guarantee, the no-rewrite-of-history rule, and the RFC2-13 challenge-lifecycle citation kept; connective prose tightened. |
| RFC5-14 | retained with wording sharpened | module 2 `consent-egress-secrets.md` §3.7 + history §RFC5-14 | Content-class table copied verbatim; highest-embedded-class rule, RFC3-16(a) policy-provenance argument, and the fail-closed determinability rule kept. AS-R5 amendment marker moved; the [Inferred] no-floor argument compressed to a sentence with its label, full rev9 wording in history. |
| RFC5-15 | retained with wording sharpened | module 2 `consent-egress-secrets.md` §3.7 | Single choke point and all three check parts kept at identical strength, including the "writable by fleet workers" untrusted-tree premise and the remote-backing-store rule. |
| RFC5-16 | retained with wording sharpened | module 2 `consent-egress-secrets.md` §3.8 + history §RFC5-16 | Non-exhaustive ingest enumeration, observing-project-policy rule (RFC3-30), fail-closed screening, and the full RFC3-16(a) "permissive policy an untrusted writer could mint" argument all kept. AS-R14/AS-R7 marker moved. |
| RFC5-17 | retained with wording sharpened | module 2 `consent-egress-secrets.md` §3.8 + history §RFC5-17 | Hash-not-body provenance, the closed redaction-class set, the per-class Unknown mapping, and the trust-floor sentence kept. AS-R12 marker moved; the "scoping fix, not a vocabulary extension" qualifier stays in the clause. |
| RFC5-18 | retained with wording sharpened | module 3 `execution-profiles.md` §3.9 + history §q3 | Gate conditions (a)–(e), the RFC3-16(a) cross-check, and the `execution-blocked` primary reason (RFC2-24 #12) kept. Decision **A5** stays named in the clause; the superseded `missing-evidence` position and its reasoning moved to history §q3 with a backlink. |
| RFC5-18 *(limb (a))* | retained unchanged | module 3 `execution-profiles.md` §3.9 | Acceptance of this RFC is a gate condition. |
| RFC5-18 *(limb (b))* | retained unchanged | module 3 `execution-profiles.md` §3.9 | A declared, versioned profile artifact must exist. |
| RFC5-18 *(limb (c))* | retained unchanged | module 3 `execution-profiles.md` §3.9 | Owner approval of that exact version, provenance cross-checked under RFC3-16(a); cited by violation case 13. |
| RFC5-18 *(limb (d))* | retained unchanged | module 3 `execution-profiles.md` §3.9 | Launching principal authenticated and authorized. |
| RFC5-18 *(limb (e))* | retained unchanged | module 3 `execution-profiles.md` §3.9 | Run captured as an Execution record citing profile identity and version (SDR-8); cited by RFC 0004 integration. |
| RFC5-19 | retained with wording sharpened | module 3 `execution-profiles.md` §3.9 + history §RFC5-19 | FD-018-as-amended-by-FD-029 provenance, the untrusted-regardless-of-owner rule, the permissive-profile path, the observation/execution boundary, and the confers-no-tier clarification all kept. AS-R3 marker moved; the [Inferred] sidestep argument compressed with its label, rev9 wording in history. |
| RFC5-20 | retained with wording sharpened | module 3 `execution-profiles.md` §3.9 | Six-item profile-contents list copied, including the closed network grammar (`none`, `loopback-only`, enumerated list) and the Syzygy-interface exclusion. Only the AS-R2 amendment marker was dropped to history-style brevity; the [Inferred] rationale is retained inline. |
| RFC5-21 | retained unchanged | module 3 `execution-profiles.md` §3.9 + history §RFC5-21 | Three isolation classes, the certification floor, the no-"none" rule, the `report-fact` cap, and the full violation set copied verbatim. Only the AS-R13 relocation parenthetical moved to history; the relocated rule itself stays in the violation set. |
| RFC5-22 | retained with wording sharpened | module 3 `execution-profiles.md` §3.9 + history §RFC5-22 | Four closed destructive-operation classes and the always-human-gated carve-out copied verbatim. The AS-R13 note explaining what was *removed* from this list moved to history; the removal is recorded there and the rule lives at RFC5-21. |
| RFC5-23 | retained with wording sharpened | module 3 `execution-profiles.md` §3.9 | Versioning, fresh-approval-per-version, snapshot-input identity, termination on revocation, and per-project scoping kept. |
| RFC5-24 | retained with wording sharpened | module 1 `admission-and-boundary.md` §3.10 + history §RFC5-24 | Adapter-credential population rules and the widened injection prohibition (covering machine-client credentials explicitly) kept with their SEC-3 rationale. AS-R2 marker moved. |
| RFC5-25 | retained unchanged | module 1 `admission-and-boundary.md` §3.11 + history §RFC5-25 | Audit-record field list and Evidence-artifact status kept; **the location constraint — the trail lives outside `.syzygy/**` and outside the untrusted actor class's write reach — is copied verbatim**, being the anchor of RFC 0003's A1 correlation mechanism. Only the rev7/F1 history parenthetical moved; decision **A1** stays named in the clause. |
| RFC5-26 | retained unchanged | module 1 `admission-and-boundary.md` §3.11 | Uniform revocation semantics and the no-silent-un-revocation rule are already minimal. |
| §4 violation cases (rev9 1–12) | retained with wording sharpened | distributed §4 across all three modules; case 11 in `README.md` | Tier 1. All twelve rev9 cases survive; **one case added** covering the rev10 RFC5-3/5-5 scoping (a first-party client admitted without a machine credential; a later contract defining a third class), and RFC5-25's location constraint added to the RFC5-24/25 case. |
| §5 Integration | retained with wording sharpened | §5 of each owning module; package-spanning items in `README.md` §5 | Tier 1 integration obligations. All rev9 relies/provides lines kept; **added** a provides-to line for RFC 0010 (Mission Control) and RFC 0011 (Context Compiler) stating the closed two-class client contract, the egress choke point, ingest screening, and the execution gate. |
| §6 Alternatives 6.1 | moved to rationale/history | history §6 | Load-bearing for RFC5-9 — one sentence retained in `README.md` §6 with a pointer. |
| §6 Alternatives 6.2 | moved to rationale/history | history §6 | Not load-bearing for any live clause; RFC5-12's one-class-per-record rule carries the outcome. |
| §6 Alternatives 6.3 | moved to rationale/history | history §6 | Outcome is normative at RFC5-21 ("no 'none' class"); the argument is history. |
| §6 Alternatives 6.4 | moved to rationale/history | history §6 | Owner ruling FD-018/FD-029 retained in `README.md` doctrine grounding and RFC5-19; the alternative's argument is history. |
| §6 Alternatives 6.5 | moved to rationale/history | history §6 | Outcome is normative at RFC5-11; the argument is history. |
| §6 Alternatives 6.6 | moved to rationale/history | history §6 | The declination is now carried by q1 and its rev10 scope ruling. |
| §6 Alternatives 6.7 | moved to rationale/history | history §6 | Load-bearing for interpreting RFC5-11 — one sentence retained in `README.md` §6 with a pointer. |
| §6 Alternatives 6.8 | moved to rationale/history | history §6 | Load-bearing for why RFC5-12/15/18 cite RFC3-16(a) rather than restate it — one sentence retained in `README.md` §6. |
| §7 Deliberately deferred | retained unchanged | §7 of each owning module; package-level list in `README.md` §7 | Tier 1 explicit deferrals. |
| §8 q1 (machine-client mechanism) | open — retained | module 1 `admission-and-boundary.md` §8 q1 | Still OPEN; no mechanism selected. **Annotated** with a rev10 scope ruling (directive §2 / OD-R10-5): the choice is among RFC5-7 classes that satisfy RFC5-6 identically, so it cannot alter the meaning of specifications authored against RFC5-6; classified "must close before V0 implementation", not blocking specification. |
| §8 q2 (overlay device identity) | answered — stub in module 1 §8; full text history §q2 | ANSWERED by owner decision B9 (exception declined). Question and answer preserved verbatim; the binding consequence stays in RFC5-4. |
| §8 q3 (execution-blocked reason) | answered — stub in module 3 §8; full text history §q3 | ANSWERED by owner decision A5 (option B). Question and answer preserved verbatim; the binding rendering stays in RFC5-18. |
| §8 q4 (destructive-op class closure) | open — retained | module 3 `execution-profiles.md` §8 q4 | Still OPEN; RFC5-22's four-class closure versus also gating in-scratch deletion. |
| §8 q5 (rotation overlap default) | open — retained | module 1 `admission-and-boundary.md` §8 q5 | Still OPEN; zero versus bounded nonzero grace. Proposed: zero. |
| §8 q6 (revocation re-evaluation) | answered — stub in module 1 §8; full text history §q6 | ANSWERED by owner decision B4 (stronger form (i)). Question and answer preserved verbatim; the forced-evaluation rule stays in RFC5-11. |

## Accounting summary

- **26 / 26 numbered clauses retained in the active contract package, each in
  exactly one module.** Zero merged, zero retired, zero renumbered, zero routed
  out. Clause ranges: module 1 = RFC5-1..RFC5-11 + RFC5-24..RFC5-26; module 2 =
  RFC5-12..RFC5-17; module 3 = RFC5-18..RFC5-23.
- Outcomes: `retained unchanged` ×8 (RFC5-2, 5-6, 5-7, 5-9, 5-10, 5-21, 5-25,
  5-26), `retained with wording sharpened` ×18, plus 11 *(limb)* rows all
  `retained unchanged`.
- **2 clauses sharpened under rev10 owner direction** — RFC5-3 and RFC5-5.
  Both additions are purely additive: no rev9 sentence was deleted, softened, or
  replaced. Every other `retained with wording sharpened` row is prose
  compression plus history extraction only.
- **Questions keep RFC-level immutable numbering q1..q6.** 3 open (q1, q4, q5)
  retained in their owning module; 3 answered (q2, q3, q6) reduced to a stub in
  the owning module with the question and answer verbatim in history, and their
  binding consequences left normative in RFC5-4, RFC5-18 and RFC5-11.
  `README.md` §8 carries the package question index.
- **§6: all 8 alternatives moved to history**; 3 kept as one-sentence residues
  in `README.md` §6.
- Additions beyond rev9: violation case 13 (rev10 client-class scoping), the
  RFC 0010 / RFC 0011 integration lines, the RFC5-3/RFC5-5 exhaustiveness
  paragraphs, and the q1 scope ruling.
- **Package word counts** (`wc -w`): module 1 = 3,643; module 2 = 2,351;
  module 3 = 2,197; `README.md` = 2,005. Normative module total 8,191; no module
  approaches the ~7,000 ceiling.

<!-- ======== RFC-0006 ======== -->

# RFC-0006 — clause migration rows (rev9 → rev10 compaction)

Source: `_bootstrap/rfc-phase/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`
(frozen, 5,017 words, RFC6-1…RFC6-28).
Active target: `final-prespec/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`.
History target: `final-prespec/history/RFC-0006-history.md`.
No clause was merged, retired, or renumbered; the range RFC6-1…RFC6-28 is
complete with no gaps. RFC-0006 has no lettered sub-clauses.

| Clause | Outcome | Target | Reason |
|---|---|---|---|
| RFC6-1 | retained unchanged | active §3.1 | Selection-reference definition and the no-surface-local-handle prohibition; nothing compressible without weakening. |
| RFC6-2 | retained with wording sharpened | active §3.1 (SC-1 refinement narrative → history) | Rule unchanged; the parenthetical explaining SC-1's narrower two-entity list moved to history. |
| RFC6-3 | retained unchanged | active §3.1 | Cross-surface synchronization and the explicit-skew obligation. |
| RFC6-4 | retained with wording sharpened | active §3.1 | Latest-evaluation defaulting and mandatory stamping unchanged; one connective clause tightened. |
| RFC6-5 | retained unchanged | active §3.2 | Closed nine-outcome vocabulary and its obligations table copied verbatim. |
| RFC6-6 | retained unchanged | active §3.2 | Navigation-outcomes-are-not-Unknown-reasons rule with its `[Inferred]` label. |
| RFC6-7 | retained unchanged | active §3.2 | Determinism of outcome and fact set per evaluation. |
| RFC6-8 | retained with wording sharpened | active §3.3 | What a URL pins, presentation-hint neutrality, and the deliberate non-binding of spelling; one word cut. |
| RFC6-9 | retained unchanged | active §3.3 | Rename-stability and the surface-local-handle violation test. |
| RFC6-10 | retained unchanged | active §3.3 | Two URL temporalities; the question/answer distinction retained as an interpretive aid. |
| RFC6-11 | retained unchanged | active §3.3 | Retirement rendering, never-404, never-silent-redirect, with its governance-event reasoning. |
| RFC6-12 | retained unchanged | active §3.3 | Surface-independence of URL-pinned selections. |
| RFC6-13 | retained unchanged | active §3.4 | The human/machine parity property (bidirectional SDR-27 obligation) — cited by RFC-0010/0011. |
| RFC6-14 | retained with wording sharpened | active §3.4 (closing rationale → history) | Full label-parity vocabulary and the `challenge-pending` obligation retained; one justifying clause moved. |
| RFC6-15 | retained unchanged | active §3.4 | Evaluation stamping and same-evaluation determinism of answers. |
| RFC6-16 | retained unchanged | active §3.4 | Filters-are-declared-scope; VIS-1 narrowing-not-faking rule. |
| RFC6-17 | retained with wording sharpened | active §3.4 (amendment narrative → history) | All six RFC2-25 tiers, sibling surface states, and expandability retained verbatim; the "previously omitted" narrative and one duplicate example moved. |
| RFC6-18 | retained unchanged | active §3.5 | One drawer, one fact set; kernel-defect-not-UI-inconsistency framing. |
| RFC6-19 | retained with wording sharpened | active §3.5 (class-6 justification → history) | All seven content classes and the challenge-lifecycle obligation retained; one explanatory sentence moved. |
| RFC6-20 | retained unchanged | active §3.5 | Trust-floor link rule for drawer contents and doctrine/contract citation rendering. |
| RFC6-21 | retained unchanged | active §3.5 | Minimal display is presentation depth, never a fact-set subset. |
| RFC6-22 | retained unchanged | active §3.6 | The SDR-27 equivalence definition (closed tuple). |
| RFC6-23 | retained unchanged | active §3.6 | Finer detail permitted, contradiction release-blocking. |
| RFC6-24 | retained with wording sharpened | active §3.7 (Base rename History → history) | Three scenario contexts, the non-default-revision marker, the incompatible-proposal refusal, and D1's map scope retained; the rev7 rename narrative moved. |
| RFC6-25 | retained unchanged | active §3.7 | Context travels with the selection; no silent context swap. |
| RFC6-26 | retained unchanged | active §3.8 | Unconsented renders as policy with resolution route, never as error. |
| RFC6-27 | retained unchanged | active §3.8 | Excluded is a rendered counted state; nothing derived from excluded content anywhere. |
| RFC6-28 | retained with wording sharpened | active §3.9 (History parenthetical → history) | Binding phase rule retained at identical strength and shape-parallel with RFC7-38/RFC8-32/RFC9-52; only its origin note moved. |
| q1 | open — retained | active §8 | Unpinned-URL default (RFC6-4/10) still awaits owner confirmation. |
| q2 | open — retained | active §8 | `not-applicable` scope for V0-core entities (RFC6-5) still open. |
| q3 | answered — moved to history | history §8 q3 | Answered at acceptance by owner decision A5 (RFC2-24 #11 `reference-unresolvable` retained); slot kept in active §8 so numbering never shifts, with the decision cited in active §5. |
| q4 | open — retained | active §8 | Reader-enabled successor auto-follow (RFC6-11) still open. |

**Non-clause material moved:** rev9 §0 reader's summary (compressed to the §0
reader map, two phrasings preserved in history), §1 summary (compressed into
§1 scope), the §5 RFC 0002 defect narrative (verbatim in history; one-sentence
survivor with the A5 backlink in active §5), and §6 Alternatives considered
(moved wholesale; three load-bearing rejections keep one sentence each in
active §6 pointing to history).

<!-- ======== RFC-0007 ======== -->

# RFC-0007 — clause migration rows (rev9 → rev10 compaction)

Source: `_bootstrap/rfc-phase/rfcs/RFC-0007-polaris-intent-surface.md` (frozen,
9,843 words, RFC7-1…RFC7-38 plus RFC7-11(a)).
Active target: the **`../rfcs/RFC-0007/` contract package** — `README.md` index,
`narrative-contract.md` (module 1, RFC7-1..RFC7-25), `rendering-and-surface.md`
(module 2, RFC7-26..RFC7-38). The pre-split single file
`../rfcs/RFC-0007-polaris-intent-surface.md` was deleted after the sweeps below.
History target: `../history/RFC-0007-history.md`.

No clause was merged, retired, or renumbered. All 38 numbered clauses and all
7 lettered sub-clauses survive, each in exactly one module.

## Word-count arithmetic

| Stage | Words |
|---|---|
| Frozen rev9 source | 9,843 |
| Compacted single file (pre-split) | 8,006 |
| `narrative-contract.md` | 5,167 |
| `rendering-and-surface.md` | 3,143 |
| `README.md` | 2,326 |
| Package union | 10,636 |
| **Default reading path for one task** | **7,493** (index + module 1) or **5,469** (index + module 2) |

The union exceeds the single file because the index restates the package's
scope, doctrine grounding, and integration once for both modules; no normative
clause is duplicated. Every file is under the ~7,000 ceiling. The compaction
stopped at 8,006 rather than the ~4,500 target because the residue is
charter-protected: ~500 words of copied tables, 425 of violation cases, ~450 of
security reasoning that must keep its reasoning rather than its conclusion,
~700 of closed enumerations, and RFC7-38 verbatim.

## Verification sweeps (run against the package union vs the frozen source)

1. **Clause exclusivity** — for each of RFC7-1…RFC7-38, count of `**RFC7-n —`
   headings across both modules equals exactly 1. Zero problems. RFC7-11(a)
   heading present once, in module 1.
2. **Backticked-token diff** — four tokens in source and not in the union, each
   deliberate: `05-POLARIS-BRIEF.md` (charter bars `_bootstrap/` paths in active
   normative text → history); `records/` standalone (the full path
   `.syzygy/governance/records/` is present in RFC7-31); `reduced-fidelity`
   (RFC7-37 worked example → history); and `anchored — target changed since
   authorship`, which the line-based grep misses and a newline-flattened re-grep
   confirms present in RFC7-11(a). This sweep previously caught a real defect —
   `dismissed-by-decision` had dropped out of RFC2-25's closed three-state list,
   restored in RFC7-20.
3. **Cross-RFC clause-reference diff** — every `RFCn-m` reference to another RFC
   preserved except `RFC3-31`, which appeared only in the §6 portfolio
   meta-project alternative and travelled with it to history.
4. **Doctrine-rule diff** (`VIS-*`, `SEC-*`, `SDR-*`) — zero dropped.
5. **Decision identifiers** — `A4`, `B5`, `B6`, `B7`, `B10`, `OQ-010` all
   present in the union (plus `A1` in each Status header); matches the source
   set exactly.
6. **Violation-case distribution** — 1–7, 12, 14 in module 1; 8, 9, 11 in
   module 2; 10, 13, 15 (package-spanning) in the README. All 15 accounted for,
   none renumbered, none duplicated.
7. **Stale section references** — zero `§3.x` cross-references survive in the
   modules; all were converted to clause IDs or to `README.md` §n, so no
   citation depends on a section number that moved at the split.

| Clause | Outcome | Target | Reason |
|---|---|---|---|
| RFC7-1 | retained unchanged | narrative-contract.md | Identity clause already minimal; no prose to compress. |
| RFC7-2 | retained with wording sharpened | narrative-contract.md | Three-way taxonomy and "no fourth kind" copied verbatim; the authoring-act limb tightened without changing scope. |
| RFC7-2(a) | retained unchanged | narrative-contract.md | "Anchored" definition is part of the closed taxonomy — copied, not paraphrased. |
| RFC7-2(b) | retained unchanged | narrative-contract.md | "Explicitly non-normative" definition copied verbatim; cited by RFC7-17's argument band. |
| RFC7-2(c) | retained unchanged | narrative-contract.md | "Epistemically labeled" definition copied verbatim, including the Observed/Inferred/Unknown enumeration. |
| RFC7-3 | retained unchanged | narrative-contract.md | Load-bearing non-citation invariant and deletion invariant; wording preserved at identical strength. |
| RFC7-4 | retained unchanged | narrative-contract.md | Already one sentence of obligation. |
| RFC7-5 | retained with wording sharpened | narrative-contract.md; rationale → history | Entity table copied verbatim; the presentation-profile justification (RFC1-7 reconciliation, "disconnected specification browser") moved, all five profile rules and owner decision A4 kept. |
| RFC7-6 | retained with wording sharpened | narrative-contract.md; rationale → history | Cardinality rule and "thin, never absent" kept with the v1.md quote; the RFC7-31-meaningfulness reasoning moved. |
| RFC7-7 | retained unchanged | narrative-contract.md | SDR-13 artifact-class obligations are a closed list of four properties plus the SEC-4 rules. |
| RFC7-8 | retained unchanged | narrative-contract.md | Cache/governance boundary already minimal. |
| RFC7-9 | retained with wording sharpened | narrative-contract.md; rationale → history | Granularity rule kept; the admissibility-floor derivation compressed to its binding statement, the challenger walkthrough moved. |
| RFC7-9(a) | retained unchanged | narrative-contract.md | "Covers" definition is binding and load-bearing for (c); copied verbatim. |
| RFC7-9(b) | retained unchanged | narrative-contract.md | "Minimality" and the surplus-anchor defect rule copied verbatim. |
| RFC7-9(c) | retained with wording sharpened | narrative-contract.md | "Bounding" rule, the twenty-anchor non-conformance case, and the splitting obligation kept; the meta-commentary on why covering is defined as attribution moved to history. |
| RFC7-10 | retained with wording sharpened | narrative-contract.md; analogy → history | Anchor tuple and the closed target-class enumeration copied verbatim; the RFC2-11/RFC2-18 analogy moved (the citation survives in active §5). |
| RFC7-11 | retained unchanged | narrative-contract.md | Broken-anchor degradation semantics and the four prohibitions preserved verbatim. |
| RFC7-11(a) | retained with wording sharpened | narrative-contract.md; rationale → history | Drift rendering obligation, review mark, non-drift rule, and the "mints no RFC2-24 reason" boundary kept; the third-door reasoning moved with a backlink. |
| RFC7-12 | retained unchanged | narrative-contract.md | Restatement discipline already minimal. |
| RFC7-13 | retained with wording sharpened | narrative-contract.md | Per-altitude obligation and the V0 ordering enumeration kept verbatim; owner decision B7 now cited in place of the §8 q7 pointer. |
| RFC7-14 | retained with wording sharpened | narrative-contract.md; rationale → history | Verbatim-leaf rule and the adjacency rules kept in full; the two-alternatives rationale moved, owner decision B5 cited in place of the authored-position marker. |
| RFC7-15 | retained with wording sharpened | narrative-contract.md | Catalog honesty rules kept; connective prose tightened. |
| RFC7-16 | retained with wording sharpened | narrative-contract.md; rationale → history | Minimal-density fact set (label + tier + freshness + evaluation identity + handoff) and the composite-maturity prohibition kept; the RFC6-21/RFC1-19 derivation and the reservation narrative moved. |
| RFC7-17 | retained with wording sharpened | narrative-contract.md | Three authority classes and the full three-band composition copied verbatim as a closed enumeration; owner decision B7 cited. |
| RFC7-18 | retained unchanged | narrative-contract.md | Single-drawer and no-second-copy rules already minimal. |
| RFC7-19 | retained unchanged | narrative-contract.md | Empty-block rule already one sentence. |
| RFC7-20 | retained with wording sharpened | narrative-contract.md | Draft-state rules and the SEC-2 consent degradation kept; owner decision B10's `editorial-draft`/`unadopted-draft` distinction folded in from the discharged §5 defect so the decision stays in the active file. |
| RFC7-21 | retained unchanged | narrative-contract.md | Per-claim attestation rule and the RFC3-16(a) provenance argument are a protected security premise — reasoning kept, not just the conclusion. |
| RFC7-22 | retained unchanged | narrative-contract.md | Queue ownership and rejection rules already minimal. |
| RFC7-23 | retained unchanged | narrative-contract.md | Acts-and-gates table copied verbatim, all four rows and all gate text. |
| RFC7-24 | retained unchanged | narrative-contract.md | SDR-18 seam boundaries already minimal. |
| RFC7-25 | retained with wording sharpened | narrative-contract.md; rationale → history | Deterministic floor, asymmetric declaration with owner decision B6's verbatim answer, the RFC7-11(a) review trigger, the record home and rendering duty, and the RFC3-16(a) verdict argument all kept; the VIS-4 derivation and the rot walkthrough moved. |
| RFC7-26 | retained with wording sharpened | rendering-and-surface.md | Both mode names, the Base-includes-observed rule, and the no-synonym rule kept; the trailing qualifier moved. |
| RFC7-27 | retained unchanged | rendering-and-surface.md | No-fictitious-consensus rule already minimal. |
| RFC7-28 | retained unchanged | rendering-and-surface.md | Curated-diagram obligations are a closed list; copied. |
| RFC7-29 | retained unchanged | rendering-and-surface.md | Boundary table copied verbatim, all ten rows plus the closing rule. |
| RFC7-30 | retained with wording sharpened | rendering-and-surface.md; rationale → history | All six walkthrough prompts, the second-phase check, and the non-visual-run obligation kept verbatim; the pass-every-time reasoning compressed, the duplicated record-home gloss moved. |
| RFC7-31 | retained with wording sharpened | rendering-and-surface.md; History parenthetical → history | Two floors, two homes, the deletion-invariant argument, RFC3-16(a) honoring, and `verdict-unlawful` kept; the rev7-alignment *(History: …)* parenthetical extracted verbatim. |
| RFC7-32 | retained unchanged | rendering-and-surface.md | Trigger clause already minimal. |
| RFC7-33 | retained with wording sharpened | rendering-and-surface.md | Full distinction enumeration copied verbatim; the non-citability-travels argument is a protected security premise and keeps its reasoning; the type-name rule kept. |
| RFC7-34 | retained with wording sharpened | rendering-and-surface.md; rationale → history | Both limbs — recoverability and reachability — kept with their enumerated traversals; the SDR-27 half-coverage gloss compressed. |
| RFC7-35 | retained unchanged | rendering-and-surface.md | Workspace-manifest boundary already minimal. |
| RFC7-36 | retained with wording sharpened | rendering-and-surface.md; rationale → history | Both carry-over lists, the status-assertion prohibition, and the OQ-010 note kept in full; the framing sentences moved. |
| RFC7-37 | retained with wording sharpened | rendering-and-surface.md; example → history | Declared-relation semantics and the RFC6-17 full-composition disclosure kept verbatim, including "cited, never restated here"; the worked counter-example moved. |
| RFC7-38 | retained unchanged | rendering-and-surface.md; History parenthetical → history | Binding phase rule preserved at verbatim strength (shape-parallel with RFC6-28/RFC8-32/RFC9-52); only the *(History: added at the rev8 rework, directive item 7.)* parenthetical was extracted. |
| q1 | answered — moved to history | history §8 q1; navigational row in `README.md` §8 | Materiality authority; answered by owner decision B6, whose ruling is carried in RFC7-25. |
| q2 | open — retained | `narrative-contract.md` §8 | Primary-narrative cardinality (RFC7-6); unanswered, retained compactly. |
| q3 | answered — moved to history | history §8 q3; navigational row in `README.md` §8 | Editorial-draft surface state; answered by owner decision B10, whose ruling is carried in RFC7-20. |
| q4 | open — retained | `narrative-contract.md` §8 | Rejected-draft retention (RFC7-22); unanswered, retained compactly. |
| q5 | answered — moved to history | history §8 q5; navigational row in `README.md` §8 | Presentation-profile scope; answered by owner decision A4, whose ruling is carried in RFC7-5. |
| q6 | answered — moved to history | history §8 q6; navigational row in `README.md` §8 | Verbatim leaf under a proposed reading; answered by owner decision B5, whose ruling is carried in RFC7-14. |
| q7 | answered — moved to history | history §8 q7; navigational row in `README.md` §8 | V0 disclosure enumeration; answered by owner decision B7, whose ruling is carried in RFC7-13 and RFC7-17. |

## Non-clause material

| Item | Outcome | Target | Reason |
|---|---|---|---|
| §0 Reader's summary | retained with wording sharpened | `README.md` package reader map + each module's §0; dropped bullets → history | Charter allows a short reader map; bullets that restated RFC7-13/16/30/33 verbatim moved. |
| §1 Summary | retained with wording sharpened | `README.md` Scope | SDR §2 charter quote preserved verbatim; the clause-list sentence dropped as duplicative of §0's structure line. |
| §2 Motivation | retained with wording sharpened | `README.md` §2; brief citation → history | Doctrine quotes and the SDR-13…18 ruling list retained; the `_bootstrap/` brief citation moved (charter bars `_bootstrap/` paths in active normative text). |
| §4 Violation cases | retained unchanged | distributed: modules §4, spanning cases 10, 13 and 15 in `README.md` §4 | All 15 cases retained; Tier 1 explicitly keeps violation cases. |
| §5 Integration | retained with wording sharpened | two-layer: `README.md` §5 package edges; each module §5 module-local; defects 1 and 3 narratives → history | All reliance citations kept and RFC 0003/0004/0005 added where the body actually depends on them; the discharged (B10) and resolved defect narratives moved with backlinks, decision IDs kept in the active file. |
| §6 Alternatives considered | moved to rationale/history | history §6; load-bearing pointer in `README.md` §6 | Charter moves §6 wholesale; the two alternatives load-bearing for RFC7-25 and RFC1-27 keep a one-sentence pointer in the active §6. |
| §7 Deliberately deferred | retained with wording sharpened | `README.md` §7 (package-level) | Tier 1 keeps explicit deferrals; composite-maturity deferral folded in from RFC7-16, RFC 0006 §7 re-cited as a named deferral rather than a section number. |
| End-of-contract marker | retained with wording sharpened | `README.md` end marker + per-module end markers | Restated to enumerate the full sub-clause set and assert the range is contiguous with no gaps. |
| Clause map and lookup rule | new at the split | `README.md` | Deterministic `n ≤ 25` → module 1, `n ≥ 26` → module 2; sub-clauses live with their parent; ranges contiguous and exhaustive so no search is needed. |
| Seam documentation | new at the split | `README.md` | Names the reader-group seam and enumerates the twelve cross-module citation edges, all resolvable by the lookup rule. |

<!-- ======== RFC-0008 ======== -->

# RFC-0008 — clause migration rows (rev9 → rev10 compaction)

Source: `_bootstrap/rfc-phase/rfcs/RFC-0008-trajectory-work-surface.md` (frozen,
9,791 words, RFC8-1…RFC8-32).
Active: `../rfcs/RFC-0008/` — a three-module contract package (11,169 words
including the index). History: `../history/RFC-0008-history.md`.

**Clause range after compaction:** RFC8-1..RFC8-32, contiguous. **No merges, no
retirements, no renumbering, no new clauses.** All 32 rev9 clause identifiers
survive, each in **exactly one module** (verified programmatically: 32 clause
headers, none missing, none duplicated).

| Module | File | Clauses | Words |
|---|---|---|---|
| index | `README.md` | — | 1,921 |
| 1 | `identity-authority-materialization.md` | RFC8-1..RFC8-11 | 2,686 |
| 2 | `state-vocabulary-and-cost.md` | RFC8-12..RFC8-20 | 3,507 |
| 3 | `accounting-reconciliation-and-release.md` | RFC8-21..RFC8-32 | 3,055 |

**Verified [Observed]:** 17 clauses are byte-identical to rev9 after whitespace
normalization (RFC8-1…6, 8-9, 8-11, 8-13, 8-15, 8-17, 8-20, 8-22, 8-26, 8-29,
8-30, 8-31); 15 are sharpened. RFC8-13's three derivation tables and RFC8-4's
ontology table are copied verbatim, not paraphrased. The split moved clause
text unchanged: after splitting, exactly one clause differs from the pre-split
single file — **RFC8-27**, whose stale "RFC 0004 §6" cross-reference was
repointed to `../history/RFC-0004-history.md` §6 now that RFC-0004 is itself a
package.

**Note on lettered limbs.** RFC-0008's own end-of-contract marker declares that
lettered limbs cited inside a clause (e.g. RFC8-2(a)–(c)) are *parts of that
clause — list items within one clause body — not separate sub-clauses with
their own headings*. Rows are supplied for the six that carry independently
citable content (RFC8-2(a)–(c), RFC8-8(a)–(c)) so the matrix is complete
against the charter's format; they are not separate clause identifiers, and
they resolve to their parent clause's module.

| Clause | Outcome | Target | Reason |
|---|---|---|---|
| RFC8-1 | retained unchanged | module 1 `identity-authority-materialization.md` | Plane discipline; byte-identical. |
| RFC8-2 | retained unchanged | module 1 `identity-authority-materialization.md` | Binding anti-thesis; byte-identical. |
| RFC8-2(a) | retained unchanged | module 1 `identity-authority-materialization.md` | Second-editable-store limb; cited by RFC8-7 and violation case 2. |
| RFC8-2(b) | retained unchanged | module 1 `identity-authority-materialization.md` | Closure-renders-as-done limb; cited by RFC8-15/8-30. |
| RFC8-2(c) | retained unchanged | module 1 `identity-authority-materialization.md` | Amnesiac-board limb; past-window answerability. |
| RFC8-3 | retained unchanged | module 1 `identity-authority-materialization.md` | Rebuildable projection, synchronous-adapter mutation rule; byte-identical. |
| RFC8-4 | retained unchanged | module 1 `identity-authority-materialization.md` | Ontology binding table copied verbatim (table, not paraphrased). |
| RFC8-5 | retained unchanged | module 1 `identity-authority-materialization.md` | Deliberate non-reifications; byte-identical. |
| RFC8-6 | retained unchanged | module 1 `identity-authority-materialization.md` | Compaction record definition; byte-identical. |
| RFC8-7 | retained with wording sharpened | module 1 `identity-authority-materialization.md` | All three rules kept at strength; the three-reason justification for the annotation ban and the `[Inferred]` scoping rationale moved to history. |
| RFC8-8 | retained with wording sharpened | module 1 `identity-authority-materialization.md` | Three planes, orphaned-work Contradiction, and exclusivity rules all kept; two explanatory sentences moved to history. |
| RFC8-8(a) | retained unchanged | module 1 `identity-authority-materialization.md` | Uncovered approved normative claims; V0 absence-surfacing boundary. |
| RFC8-8(b) | retained unchanged | module 1 `identity-authority-materialization.md` | Approved-but-unmaterialized intent, queue order visible. |
| RFC8-8(c) | retained unchanged | module 1 `identity-authority-materialization.md` | Open materialized items, each checked against the materialization record. |
| RFC8-9 | retained unchanged | module 1 `identity-authority-materialization.md` | SDR-18 ownership boundary against Polaris; byte-identical. |
| RFC8-10 | retained with wording sharpened | module 1 `identity-authority-materialization.md` | Three required record components and the missing-record finding kept; one restatement of RFC8-8 compressed to a cross-reference. |
| RFC8-11 | retained unchanged | module 1 `identity-authority-materialization.md` | Divergence renders, never adjudicated; byte-identical. |
| RFC8-12 | retained with wording sharpened | module 2 `state-vocabulary-and-cost.md` | Closed thirteen-value vocabulary, two-orthogonal-fields rule, non-Claim ruling, and the RFC3-16(a) authorization-bearing mapping with its full widening argument all kept; the genuineness essay and the spent §8 q5 routing note moved to history, replaced by an inline B14 cite. |
| RFC8-13 | retained unchanged | module 2 `state-vocabulary-and-cost.md` | All three derivation tables (8 live + 1 terminal + 4 absence values) copied verbatim; byte-identical. |
| RFC8-14 | retained with wording sharpened | module 2 `state-vocabulary-and-cost.md` | Rule unchanged; the spent §8 q7 routing note replaced by an inline A5/B15 cite, note moved to history. |
| RFC8-15 | retained unchanged | module 2 `state-vocabulary-and-cost.md` | Closure is not a normalized "done"; byte-identical. |
| RFC8-16 | retained with wording sharpened | module 2 `state-vocabulary-and-cost.md` | Obligation identical; the `_bootstrap/` audit path in the `[Observed]` citation replaced by "substrate audit" (charter bars `_bootstrap/` paths in active normative text), path preserved in history. |
| RFC8-17 | retained unchanged | module 2 `state-vocabulary-and-cost.md` | Closed blocked-cause taxonomy; byte-identical. |
| RFC8-18 | retained with wording sharpened | module 2 `state-vocabulary-and-cost.md` | Full measure list and the no-composite-score prohibition kept; the `declared-only`-not-`Inferred` argument condensed but its RFC2-7/SEC-2 consent premise and RFC2-8/RFC1-22 challenge-authority consequence retained (security premise may not thin). |
| RFC8-19 | retained with wording sharpened | module 2 `state-vocabulary-and-cost.md` | Rule identical; `_bootstrap/` audit path in the `[Observed]` citation replaced by "substrate audit". |
| RFC8-20 | retained unchanged | module 2 `state-vocabulary-and-cost.md` | Telemetry staging, V0/V1 split, deferral list; byte-identical. |
| RFC8-21 | retained with wording sharpened | module 3 `accounting-reconciliation-and-release.md` | Chain, join bases, and the thinness-must-render obligation kept; the enrichment enumeration and the `[Inferred]` derivation moved to history. |
| RFC8-22 | retained unchanged | module 3 `accounting-reconciliation-and-release.md` | Broken joins render, reconstruction forbidden; byte-identical. |
| RFC8-23 | retained with wording sharpened | module 3 `accounting-reconciliation-and-release.md` | Unknown-provenance state and its distinction from orphaned work kept; wording tightened only. |
| RFC8-24 | retained with wording sharpened | module 3 `accounting-reconciliation-and-release.md` | Full RFC2-24 reason list kept verbatim, including the maximum-inter-pass-interval obligation; the trailing "claim reasons only" paragraph folded into the clause body (same clause, no merge). |
| RFC8-25 | retained with wording sharpened | module 3 `accounting-reconciliation-and-release.md` | Sub-entry rule, B13 fail-closed threshold, warrant-coverage test, and fixed `asserted-by-worker` tier all kept; the `[Inferred]` fail-closed essay moved to history, and one rev9 paragraph ("Until the bound is declared, the coverage test above is the operative limit") dropped as superseded by B13 — see `WORKER-REPORT-DIGEST.md` §"Substantive rulings", ruling 3. |
| RFC8-26 | retained unchanged | module 3 `accounting-reconciliation-and-release.md` | Binding preservation set; byte-identical. |
| RFC8-27 | retained with wording sharpened | module 3 `accounting-reconciliation-and-release.md` | Every tier rule kept, including the no-upgrade rule and the `report-fact` cap; the rev7 blocker-A3 `*(History: …)*` parenthetical moved to history verbatim. |
| RFC8-28 | retained with wording sharpened | module 3 `accounting-reconciliation-and-release.md` | Four-way chain-state distinction, word reservation, and the carry-both-fields obligation kept; one restatement compressed. |
| RFC8-29 | retained unchanged | module 3 `accounting-reconciliation-and-release.md` | V0 honest-absence / V1 computation staging; byte-identical. |
| RFC8-30 | retained unchanged | module 3 `accounting-reconciliation-and-release.md` | Closure fallacy forbidden; aggregate composition disclosure; byte-identical. |
| RFC8-31 | retained unchanged | module 3 `accounting-reconciliation-and-release.md` | RFC 0006 conformance and no-surface-only-facts rule; byte-identical. |
| RFC8-32 | retained unchanged | module 3 `accounting-reconciliation-and-release.md` | **Binding phase rule.** Normative text verbatim at full strength (verified by diff); only the `*(History: added at the rev8 rework, directive item 7.)*` parenthetical moved to history. Shape-parallel with RFC6-28 / RFC7-38 / RFC9-52. |

## §8 questions

Question numbers are the stable package numbering and never shift. Per the
charter addendum, every answered question keeps a one-line stub in its owning
module's §8; full text and reasoning are in history.

| Question | Outcome | Target | Reason |
|---|---|---|---|
| q1 | answered — moved to history | history §8 q1; stub in module 2 §8 | Vocabulary closure; answered at acceptance by **A8** (thirteen values, three partitions). Ruling carried inline in RFC8-12 and by RFC8-13's derivation rows. |
| q2 | open — retained | module 1 §8 | Queue realization: work-plane fact on the approved Proposal vs a new RFC 0001 kernel lifecycle state. Paired with module 1 §5's one outstanding foundation defect. |
| q3 | open — retained | module 2 §8 | Blocked-time cause split: V1 capture obligation vs RFC4-29 enrichment-roadmap item. Blocked-time semantics remain an open default. |
| q4 | open — retained | module 3 §8 | Unknown-provenance visibility default, with its scope limit that the orphaned-work Contradiction is never filterable under any answer. |
| q5 | answered — moved to history | history §8 q5; stub in module 2 §8 | Epistemic class of the normalized state; answered by **B14** (derived rendering, not a Claim). Ruling carried inline in RFC8-12. |
| q6 | answered — moved to history | history §8 q6; stub in module 3 §8 | The "small" threshold on inherited mutations; answered by **B13** (declared per project, fails closed). Ruling carried inline in RFC8-25. |
| q7 | answered — moved to history | history §8 q7; stub in module 2 §8 | Unmapped-substrate-value rendering; answered by **A5 / B15** (no new RFC2-24 reason; `state-undetermined` stands). Ruling carried inline in RFC8-14. |

## Non-clause sections

Violation cases keep the stable package numbering and are distributed to the
module owning their clauses: 1–3 and 11 → module 1; 5–7 and 13 → module 2;
8–10 and 14 → module 3; **4 and 12 span modules and are held in the package
index** (`README.md` §4). All 14 appear exactly once across the package
(verified).

| Section | Outcome | Target | Reason |
|---|---|---|---|
| §0 Reader's summary | retained with wording sharpened | README package reader map; per-module §0 maps | Merged with §1 at compaction; no obligation lived in either. Dropped bullets recorded in history with their clause pointers. |
| §1 Summary | retained with wording sharpened | README package reader map + scope | Merged as above; the anti-thesis sentence and the semantic-contract-not-UI scope statement retained. |
| §2 Motivation | retained with wording sharpened | README §2 | Doctrine grounding, the three failure modes, and all SDR staging retained; the `_bootstrap/` audit citation path moved to history. |
| §4 Violation cases | retained unchanged | modules 1–3 §4; cases 4 and 12 in README §4 | All 14 cases retained and distributed by owning clause; four trimmed by a few words each without losing recognizability. |
| §5 Integration | retained with wording sharpened | per-module §5; package-level items in README §5 | Every relies-on citation retained and redistributed by owning clause. The **two-field RFC 0009 handoff** and its conformance rule are stated **once**, in README §5, because they cite clauses in two modules; each module's §5 points there. The one outstanding foundation defect (RFC1-28/31 queue stage) sits in module 1 §5; the four closed ones are named in README §5 with the trail in history. |
| §6 Alternatives considered | moved to rationale/history | history §6; pointer in README §6 | All seven moved wholesale; the two load-bearing ones (closure-without-merge naming; composite score) keep a one-sentence pointer in README §6 per the charter. |
| §7 Deliberately deferred | retained with wording sharpened | per-module §7; package-level items in README §7 | Every deferral retained, including the binding obligation to declare each deferred *value*. The **non-deferring column-layout obligation** is held in README §7 because it binds RFC8-12's partition across the package. |
| §3.16 phase boundary | retained unchanged | module 3 §3.16; scope note in README | RFC8-32 verbatim in module 3; README records that its clause-to-requirement coverage matrix must span RFC8-1…RFC8-31 across **all three modules**, not module 3 alone. |

<!-- ======== RFC-0009 ======== -->

# RFC-0009 — clause migration rows (rev9 → rev10 compacted package)

Source: `_bootstrap/rfc-phase/rfcs/RFC-0009-orrery-map-surface.md` (frozen,
19,269 words, RFC9-1..RFC9-52 plus eight lettered sub-clauses).
Target: the indexed contract package `final-prespec/rfcs/RFC-0009/`
(**owner direction OD-R10-6**). History: `final-prespec/history/RFC-0009-history.md`.

**Package outcome summary.** Every clause is **retained** — none merged, none
retired, none routed out of the active path, no renumbering, no gaps. 52 numbered
clauses + 8 lettered sub-clauses = 60 clause rows, plus 10 §8 question rows =
**70 rows**. Ranges are contiguous and disjoint: RFC9-1..23 → module 1,
RFC9-24..45 → module 2, RFC9-46..52 → module 3. Each lettered sub-clause lives
with its parent integer.

Target column names the owning **module file** inside `final-prespec/rfcs/RFC-0009/`.

| Clause | Outcome | Target | Reason |
|---|---|---|---|
| RFC9-1 | retained with wording sharpened | `semantic-geography.md` | Section cross-refs converted to clause IDs (§3.10 → RFC9-41); rule unchanged |
| RFC9-2 | retained unchanged | `semantic-geography.md` | Semantics-only boundary; copied verbatim |
| RFC9-3 | retained with wording sharpened | `semantic-geography.md` | Drawer-invariant reasoning compressed; rejected kernel-route alternative to history §6 |
| RFC9-4 | retained unchanged | `semantic-geography.md` | Anchoring rule and spatial hierarchy copied verbatim |
| RFC9-5 | retained with wording sharpened | `semantic-geography.md` | Closed may/may-never lists copied verbatim; §3.11 → RFC9-44 |
| RFC9-6 | retained unchanged | `semantic-geography.md` | Identity-continuity rules copied verbatim |
| RFC9-7 | retained unchanged | `semantic-geography.md` | Unmapped-code rule copied verbatim (§3.11 → RFC9-44) |
| RFC9-8 | retained with wording sharpened | `semantic-geography.md` | Portfolio append-stability justification compressed; obligation unchanged |
| RFC9-8(a) | retained with wording sharpened | `semantic-geography.md` | ML-R15 problem narrative to history; workspace-scope machinery and two limits retained |
| RFC9-9 | retained with wording sharpened | `semantic-geography.md` | Two readings, measurement bar, best-effort/not-honored rule verbatim; B12(a)/B20 cites kept, narrative to history |
| RFC9-9(a) | retained with wording sharpened | `semantic-geography.md` | Four binding parts retained in full; ML-R3 finding narrative to history |
| RFC9-9(b) | retained with wording sharpened | `semantic-geography.md` | Six-facet registry entry and closed three-value domain copied; ML-R5 narrative to history |
| RFC9-10 | retained with wording sharpened | `semantic-geography.md` | Obligations (a)–(d) and owner decision B21 with its recorded cost retained; §8 q10 pointer moved to history |
| RFC9-11 | retained unchanged | `semantic-geography.md` | Masquerade boundary copied verbatim |
| RFC9-12 | retained unchanged | `semantic-geography.md` | Lens-switch invariance copied verbatim |
| RFC9-13 | retained unchanged | `semantic-geography.md` | Personal-state rule copied verbatim |
| RFC9-13(a) | retained with wording sharpened | `semantic-geography.md` | Three obligations retained verbatim; "why contract material" narrative to history |
| RFC9-14 | retained unchanged | `semantic-geography.md` | Layout input tuple copied verbatim, including the block quote |
| RFC9-14(a) | retained with wording sharpened | `semantic-geography.md` | Three input definitions and the baseline-recording obligation retained; ML-R1 narrative to history |
| RFC9-15 | retained with wording sharpened | `semantic-geography.md` | Append-stability obligation verbatim; §3.12 → RFC9-47 |
| RFC9-15(b) | retained with wording sharpened | `semantic-geography.md` | Four binding parts and the mandatory partition retained in full; ML-R1/R4/R14 narratives to history |
| RFC9-16 | retained unchanged | `semantic-geography.md` | Closed relocation-trigger set (a)–(d) copied verbatim |
| RFC9-16(d) | retained with wording sharpened | `semantic-geography.md` | Owner gate A3, the narrow carve-out and the layout-equivalence-check correction retained; ML-R2 failure case to history |
| RFC9-17 | retained unchanged | `semantic-geography.md` | Forbidden-churn list and unbounded-reservation rule copied verbatim |
| RFC9-18 | retained with wording sharpened | `semantic-geography.md` | RFC3-16(a) honoring rule verbatim; §3.4 → §4; cross-module pointer to RFC9-26 added |
| RFC9-19 | retained with wording sharpened | `semantic-geography.md` | Three placement mechanisms copied verbatim; §3.3 → §3; no-clone aside compressed |
| RFC9-20 | retained with wording sharpened | `semantic-geography.md` | Contradiction treatment and two-`placed_in` general case retained; ML-R8 narrative and §6 alternative to history |
| RFC9-21 | retained with wording sharpened | `semantic-geography.md` | Scene-scoped disclosure trigger retained verbatim; illustrative aside compressed |
| RFC9-22 | retained unchanged | `semantic-geography.md` | Repository-overlay rule copied verbatim |
| RFC9-23 | retained unchanged | `semantic-geography.md` | Authority-overlay list copied verbatim; SEC-2/3/5 premises intact |
| RFC9-24 | retained unchanged | `visual-grammar-and-lenses.md` | Reserved state palette — closed vocabulary copied verbatim |
| RFC9-25 | retained with wording sharpened | `visual-grammar-and-lenses.md` | Saturation reservation verbatim; deferral pointer §7 dropped (now module §7) |
| RFC9-26 | retained unchanged | `visual-grammar-and-lenses.md` | Seven declared items, fail-closed rule and forged-entry security reasoning copied verbatim |
| RFC9-27 | retained with wording sharpened | `visual-grammar-and-lenses.md` | Three-scope Unknown rule and earned-emptiness rule verbatim; §3.10/§3.12 refs normalized |
| RFC9-28 | retained with wording sharpened | `visual-grammar-and-lenses.md` | Per-lens height rule verbatim; §6 alternative pointer added, alternative text to history |
| RFC9-29 | retained unchanged | `visual-grammar-and-lenses.md` | SEC-5 granularity bound and its shape-disclosure reasoning copied verbatim |
| RFC9-30 | retained unchanged | `visual-grammar-and-lenses.md` | Inference/challenge/consent degradation copied verbatim |
| RFC9-31 | retained with wording sharpened | `visual-grammar-and-lenses.md` | Lens may/may-never lists and the overlay magnitude bar verbatim; closing justification compressed |
| RFC9-32 | retained with wording sharpened | `visual-grammar-and-lenses.md` | V0 lens set and both work-state fields (closed vocabularies) copied; one staging clause compressed |
| RFC9-33 | retained unchanged | `visual-grammar-and-lenses.md` | Lens staging and SEC-3 runtime gate copied verbatim |
| RFC9-34 | retained unchanged | `visual-grammar-and-lenses.md` | No-synthesis rule copied verbatim |
| RFC9-35 | retained with wording sharpened | `visual-grammar-and-lenses.md` | Same-increment rule and the promotion predicate (B12(c)/B17) retained; §3.12 → RFC9-46; provenance parenthetical to history |
| RFC9-36 | retained unchanged | `visual-grammar-and-lenses.md` | City/Factory profile rule copied verbatim |
| RFC9-37 | retained unchanged | `visual-grammar-and-lenses.md` | Factory honesty obligations copied verbatim |
| RFC9-38 | retained with wording sharpened | `visual-grammar-and-lenses.md` | Evaluation-naming and RFC9-41 subordination verbatim; resolved defect 3 folded in as an inline note |
| RFC9-39 | retained with wording sharpened | `visual-grammar-and-lenses.md` | `Base` context rule and absence-as-obligation retained verbatim; derivation narrative compressed |
| RFC9-40 | retained unchanged | `visual-grammar-and-lenses.md` | Proposed-scene rules copied verbatim |
| RFC9-41 | retained with wording sharpened | `visual-grammar-and-lenses.md` | D1 scope and the non-binding candidate bundle retained verbatim; rev7 rewrite parenthetical to history |
| RFC9-42 | retained unchanged | `visual-grammar-and-lenses.md` | LOD epistemic invariance copied verbatim |
| RFC9-43 | retained with wording sharpened | `visual-grammar-and-lenses.md` | Full equivalence tuple, six tiers and three sibling states copied verbatim; second laundering example to history |
| RFC9-44 | retained with wording sharpened | `visual-grammar-and-lenses.md` | Never-disappears rule and identity-vs-arrangement distinction verbatim; §6 alternative to history |
| RFC9-45 | retained with wording sharpened | `visual-grammar-and-lenses.md` | Three artifacts, B12(b) default and the fail-closed `verdict-unlawful` protocol retained in full; two parentheticals to history |
| RFC9-46 | retained with wording sharpened | `interaction-parity-and-release.md` | Equivalence tuple, the two added fields and the maintenance note retained verbatim; ML-R6 attribution to history |
| RFC9-47 | retained with wording sharpened | `interaction-parity-and-release.md` | Full release-gate enumeration copied (closed checklist); ML-R9/R6 attribution compressed |
| RFC9-47(a) | retained with wording sharpened | `interaction-parity-and-release.md` | Both self-maintenance obligations verbatim; directive-item provenance to history; cross-module scope note added |
| RFC9-48 | retained unchanged | `interaction-parity-and-release.md` | Non-visual parity list copied verbatim |
| RFC9-49 | retained unchanged | `interaction-parity-and-release.md` | Declared-scope-narrowing rule and RFC6-13 divergence reasoning copied verbatim |
| RFC9-50 | retained unchanged | `interaction-parity-and-release.md` | No-ambient-motion rule copied verbatim |
| RFC9-51 | retained unchanged | `interaction-parity-and-release.md` | Illumination-as-interaction-state copied verbatim |
| RFC9-52 | retained unchanged | `interaction-parity-and-release.md` | Binding phase rule copied verbatim at identical strength; shape-parallel with RFC6-28/RFC7-38/RFC8-32 |

## §8 owner questions

| Question | Outcome | Target | Reason |
|---|---|---|---|
| q1 | answered — moved to history | `semantic-geography.md` §10 (stub) | Owner decision A7; one-line stub retained so numbering never shifts |
| q2 | open — retained | `semantic-geography.md` §10 | Undeclared shared-component placement (RFC9-20); the package's only open numbered question |
| q3 | answered — moved to history | `visual-grammar-and-lenses.md` §8 (stub) | Adopted doctrine amendment D1, in part; residual candidate-bundle approval lives as live text in RFC9-41 |
| q4 | answered — moved to history | `visual-grammar-and-lenses.md` §8 (stub) | Owner decisions B12(c)/B17; the promotion predicate is clause text at RFC9-35 |
| q5 | answered — moved to history | `semantic-geography.md` §10 (stub) | Owner decision A6; see also the open follow-on recorded below |
| q6 | answered — moved to history | `semantic-geography.md` §10 (stub) | Owner decision A3, narrowed; the gate is clause text at RFC9-16(d) |
| q7 | answered — moved to history | `semantic-geography.md` §10 (stub) | Owner decision B12(a); consequences are RFC9-9, RFC9-9(a), RFC9-9(b), RFC9-15(b) |
| q8 | answered — moved to history | `visual-grammar-and-lenses.md` §8 (stub) | Owner decision B12(b); the three-artifact gate is clause text at RFC9-45 |
| q9 | answered — moved to history | `visual-grammar-and-lenses.md` §8 (stub) | Owner decisions B12(c)/B17, with q4 and the profile-relation limb |
| q10 | answered — moved to history | `interaction-parity-and-release.md` §8 (stub) | Owner decision B21; surviving contract text at RFC9-10(c) |

**One open item beyond the numbered set** (not a rev9 clause or question, so it
carries no row above). The rev10 RFC-0001 pass established that **owner decision
A6** closed RFC-0001 §8 q6's kernel-minting half but did not address whether
**RFC9-9's legend and edge-channel rules need a pass now that a kernel-level
declared dependency relation exists**, nor the underlying *who may add a profile
relation, and under what gate* question. No normative change was made on this
pass (owner-scoped; home is RFC1-7/RFC1-26). Carried as a visible open item in
`semantic-geography.md` §10, indexed in the package README, recorded in history
§8, and flagged to the lead for the open-question triage.

## Non-clause material

| Rev9 section | Outcome | Target |
|---|---|---|
| §0 Reader's summary (non-normative) | moved to rationale/history | Distributed to README reader map + each module §0; rev9 thesis verbatim in history |
| §1 Summary | moved to rationale/history | Superseded by README scope + clause map |
| §2 Motivation and doctrine grounding | moved to rationale/history | [Observed] grounding retained verbatim in history; [Inferred] thesis compacted into README |
| §4 Violation cases 1, 2, 3, 3a, 4, 5 | retained unchanged | `semantic-geography.md` §7 |
| §4 Violation cases 6, 7, 8, 9, 10 | retained unchanged | `visual-grammar-and-lenses.md` §5 |
| §4 Violation case 11 | retained unchanged | `interaction-parity-and-release.md` §5 |
| §5 Integration (relies-on lists) | retained with wording sharpened | Split module-scoped; package-spanning items to README |
| §5 defect 1 (A7/A6) | retained with wording sharpened | `semantic-geography.md` §8 — owner decisions and the binding drafting restraint retained; full trail to history §5 |
| §5 defects 2, 3, 4, 5 | moved to rationale/history | All resolved upstream 2026-08-01; one-line status in the owning module, trail in history §5 |
| §6 Alternatives considered | moved to rationale/history | history §6; four load-bearing residues cited from RFC9-3, RFC9-20, RFC9-28, RFC9-44 |
| §7 Deliberately deferred | retained with wording sharpened | Split module-scoped (§9/§7/§7); rev9 text in full in history §7 |
| End-of-contract marker | retained with wording sharpened | Per-module end markers + README's closed-range statement |

<!-- ======== RFC-0010 / RFC-0011 (new at rev10) ======== -->

| Clause | Outcome | Target | Reason |
|---|---|---|---|
| RFC10-1..RFC10-16 | new at rev10 | `rfcs/RFC-0010-mission-control-autonomy.md` | Owner direction OD-R10-1/2 (directive §6) — Mission Control and autonomy envelopes |
| RFC11-1..RFC11-12 | new at rev10 | `rfcs/RFC-0011-context-compiler.md` | Owner direction OD-R10-3/4 (directive §7) — governed context packets |
| RFC3-16(c) | new at rev10 — directive §2 repair | `rfcs/RFC-0003/governance-homes-and-owner-acts.md` | Two-state acceptance model (also rowed in the RFC-0003 section above) |

---

## Change log — accounting corrections after the rev10 reviews

Corrections to this file's **accounting**, not to any clause text. No contract
module changed in this batch; the act-1 digest set is unaffected by rows below
that touch only this file. Authorized by the lead's §20 disposition **D2**
("digest-stable rev10-package accounting fixes"), applied 2026-08-05. The
stored equivalence review is **never** edited — its "preserved verbatim"
wording is stale on exactly the RFC3-16(b) point and stays as stored; the
staleness is recorded in `round-2026-08/COMPACTION-EQUIVALENCE-REPORT.md`.

| # | Where | Was | Now | Basis |
|---|---|---|---|---|
| 1 | RFC3-16(b) row (RFC-0003 section) | Outcome `retained unchanged`; reason said the Bootstrap-correlation paragraph and the nine binding items were "all retained", disclosing no insertion | Outcome `retained with wording sharpened`; the reason discloses the inserted **constraint/authorization role split**, its fail-closed direction, its RFC10-9 worked example, and its authorizing direction **OD-R10-5** | §20.2 semantic-preservation review, finding 3 (raw report), corroborated at `10-EXIT-REPORT.md` answer 6 and by reading `rfcs/RFC-0003/governance-homes-and-owner-acts.md` against `history/rev9-rfcs/RFC-0003-project-workspace-manifests.md` |
| 2 | Global tallies (head of file) | "**2** new sub-clauses/clauses at rev10 beyond the 294 + RFC10-1..16 + RFC11-1..12" | "**1** new sub-clause at rev10 — RFC3-16(c) — beyond the 294 + RFC10-1..16 + RFC11-1..12" | §20.2 finding 4; independently re-verified 2026-08-05 by a Python `re` clause-identity census of both corpora: rev9 = 294 numbered + 21 lettered, rev10 = 322 numbered + 22 lettered, **zero lost**, gained set = {RFC10-1…16, RFC11-1…12, RFC3-16(c)}. Agrees with `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md` ("one new sub-clause (RFC3-16(c))"). The insertion in row 1 mints no identity and is therefore not a tally item |
| 3 | RFC8-25 row (RFC-0008 section) | Pointer "see report judgment call 1" — no "judgment call" heading exists anywhere in the packet | see `WORKER-REPORT-DIGEST.md` §"Substantive rulings", ruling 3 | §20.2 finding 5 (minor) and reviewer erratum in the §20 dispositions; target confirmed by reading `WORKER-REPORT-DIGEST.md` §"Substantive rulings" ruling 3, which states the RFC8-25 fallback retirement |
| 4 | RFC-0007 "Word-count arithmetic" table | `README.md` 2,268 · Package union 10,578 · default path 7,435 / 5,411 | `README.md` **2,326** · Package union **10,636** · default path **7,493** / **5,469** | Confirming-review residual R1. Recounted by `wc -w` on the exact member files 2026-08-05: 5,167 + 3,143 + 2,326 = 10,636. The same stale figures were corrected in `rfcs/RFC-0007/README.md` in the same batch, so the two files agree; `06-CONTEXT-LOAD-MAP.md` already carried 2,326. Frozen historical figures (rev9 source 9,843; pre-split single file 8,006) are unchanged — the pre-split file no longer exists and is not recountable |

**Not corrected here** (outside this batch's authorization, reported to the
lead): the identical stale RFC-0007 word-count table in
`matrix-rows/RFC-0007-rows.md`, and the stale figures carried in
`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`, `LEAD-SWEEP-NOTES.md`,
and `06-CONTEXT-LOAD-MAP.md`'s RFC-0003 governance-homes figure. Stored
review files carry those figures as historical record and are correct as
stored.
