# Semantic delta record — round 2026-08d (structural closure)

**Non-authoritative round record**, kept under
`policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md` discipline: every
substantive normative movement this round is listed with its direction and
its warrant. "Editorial" is a reviewable claim; nothing below hides behind
it. The owner work order (`OWNER-WORK-ORDER.md`, archived verbatim) is the
warrant for every structural item; review findings are cited by identifier
where they drove the shape. No act has been performed; every subject
remains candidate.

## 1. Package structure (no clause renumbered anywhere this round)

| Δ | What moved | Warrant |
|---|---|---|
| S-1 | **RFC-0010 split** from one 781-line file into a five-module package (mission-identity-approval-and-lifecycle; prevention-envelope-and-attention; budget-reservation; effects-recovery-and-stop; portfolio-and-cross-project-consent) + README clause map. Clause bodies carried byte-identical except where a listed delta below amends them (split tool verified 25 clause bodies byte-identical before amendment) | work order §5; RD-1's "symptom of needing a package split" |
| S-2 | **RFC-0011 split** into packet-identity-provenance-and-memory + deterministic-selection-and-budget + README (12 clause bodies byte-identical before amendment) | work order §6 |
| S-3 | **Acceptance restructured into six wave acts** (A, B, C1, C2, D1, D2); `ACCEPT COMPACTED FOUNDATIONAL RFCS` retired; wave manifests generated and partition-checked by the new `build_active_manifest.py`; CG-7a/7b/7d/7e rewritten for waves | work order §4; RD-8 ("a knowing act into a surprised one") |

## 2. New clauses (appended; nothing retired, nothing renumbered)

| Δ | Clause(s) | Content | Warrant |
|---|---|---|---|
| N-1 | RFC1-33, RFC2-26, RFC3-33, RFC4-30, RFC5-27 | Binding phase-rule clauses for RFC-0001..0005 (shape-parallel with RFC6-28 et al.) — these contracts have genuinely observable consequences (registration, consent, evidence rendering) and previously had no boundary clause a selector could name | RD-5 (RFC11-4 unsatisfiable); work order §8.6 both-halves disposition |
| N-2 | RFC7-39 | Fixed human entry: `.syzygy/intent/OVERVIEW.md`, governed presentation never authority; absence renders, never silent | work order (human entry) |
| N-3 | RFC7-40 | Repository-front-door discoverability: per-repository yes/no/Unknown kernel finding; Syzygy may propose, never write (VIS-5) | work order (discoverability placement) |
| N-4 | RFC10-23 | Four effect dimensions (project mutation / external-system mutation / external disclosure / resource consumption) recorded separately; `propose-only` never rendered "no effects" where (i)/(iii)/(iv) non-empty | RD-1b B3 |
| N-5 | RFC10-24 | D3 operating precondition as a clause: no mission leaves `awaiting-approval` until the doctrine question is ruled; independent of RFC10-16 | RD-1b (precondition in prose binds nothing) |
| N-6 | RFC11-13..16 | Implementation-boundary declaration; traversal/termination rules (rule 2 lifted verbatim from fixture 9); doctrine/craft ownership metadata or stated judgment; clause-first `constrains` consumption | RD-5 findings 1–3 |

## 3. Amendments to existing clauses

| Δ | Clause | Before → after | Warrant |
|---|---|---|---|
| A-1 | RFC10-5 | Lifecycle diagram gained pre-running→expired (maximum time to first dispatch), blocked\|paused→expired (park expiry), paused→failed edges; limb 3 of the park bound restricted to **duration-typed** maxima, non-empty because undeclared wall-clock budget = zero (RFC10-7) | RD-1b B4, B5 |
| A-2 | RFC10-4 | Mission identity grounded in RFC1-7's **mission extension profile** with named minting authority | RD-1b A (identity minted by no stated authority) |
| A-3 | RFC10-7/8/10/12/22 | Envelope establisher field; propose-only project-qualified namespaces + dimension honesty + owner-act conjunct; attention debit and establisher inheritance; enforced-limit reconciliation; two closed exempt classes, hold-and-mint deferral, wall-clock expiry default; profile grounding | RD-1b B1, B2, B6, N-findings |
| A-4 | RFC10-17 (module rewrite) | Five-quantity ledger → **six quantities** (adds `recovery_reserve`); admission inequality `reserved_remaining + spent ≤ authorized − recovery_reserve`; enforced-limit admission at the RFC5-21 launch gate and RFC5-15 per-transmission headroom; resource-kind classification (hard-enforceable / provider-quota-enforceable / monitoring-only / non-delegable); overrun as residual with three sources; release table incl. child-grant maximum-time-to-first-dispatch and parent-termination rows | the RD-2/RD-3 shared blocking finding (ledger vs consumption) — the defect the round-2026-08c freeze preserved, now repaired |
| A-5 | RFC10-18/18(a)/19/19(a)/20 (module rewrite) | Establisher as envelope field; four-site effects-applied enumeration scoped to the external-mutation dimension with coverage-keyed Unknown; atomically-reversible defined narrowly, compensatable-by-force, per-effect record fields, recovery_reserve naming; halt-siblings-plus-escalation default; finite stop default, hang-is-failed-stop exit, own-kill-report admission | RD-1/RD-1b blocking findings |
| A-6 | RFC11-4 | `provides_to` removed; selection consumes RFC11-13 declarations; constrains via RFC11-16; traversal via RFC11-14. **This session:** the phase-rule parenthetical "(the module or README text carrying it)" replaced by the two-tier rule — declaration always travels (recorded verbatim when the index is not loaded), the **defining module** is forced only when the task sits on the OpenSpec seam, and an index's restatement is never the clause | RD-5; the fixture-1-vs-8 contradiction (work order §8 item 6) |
| A-7 | RFC1-7 | Mission extension profile added; profile-defining RFCs name minting authorities under RFC1-9 | consequence of A-2 |
| A-8 | RFC6-2/18/19 | Profile-entity selectability; "Why this answer?" naming with human/machine same-facts; items 1/4/7 amended + new item 8 (work state RFC8-12 and chain state RFC8-28 never folded; uncomputed reconciliation renders Unknown) | work order §9 (facet corrections) |
| A-9 | RFC9-8(a) | Portfolio layout registry moved from workspace manifest to the typed **workspace governance store** (RFC10-15) with the work order's registry-authority rule verbatim and a staged reference; **this session** lightly trimmed (7 words, meaning-preserving) against the module ceiling, and the module carries a stated oversize justification in the verifier | work order (registry authority); RD-findings on manifest-as-authority |
| A-10 | All 11 contract indexes | `implementation_boundary:` front matter added (kind + clause) | N-6's RFC11-13 |

## 4. Fixtures and validators (evidence plane, not contract text)

- All nine fixtures restructured with a **task/answer boundary** (RD-5's
  blind-derivation protocol); transcribed measurements removed — the
  machine-written anchors are each fixture's only measurements; fixture 5
  re-selected against the split packages and its false band claim removed
  and recorded; fixtures 1/8 now state the same phase-boundary rule from
  opposite sides; **fixture 10** (Trajectory work lifecycle) authored,
  closing RD-5's class double-count.
- `verify_final_prespec.py`: singleton clause declarations parsed;
  round-08d clause ends; phase-rule list extended; RFC-0009 module
  oversize justified — each new predicate mutation-tested.
- `build_active_manifest.py` new (enumerate/reject/sorted/partition,
  `--check`, four-case `--selftest`).
- `check_governance.py`: CG-7 family wave-aware; wave-manifests install
  home registered as forward reference; owner work order allowlisted for
  CG-12/CG-22 (it quotes the defects it orders fixed).
- Routing matrix: round-2026-08d section routing the eight new surface
  clauses (all OS), with the RFC10-24 CR-vs-OS doubt recorded.
- Acceptance ceremony: RD-7's eight broken pointers repaired at
  install-time (two report copies); simulation:
  `POST-INSTALL-LINK-REPORT.md` (87/87 resolve).

## 5. Deliberately not done

- RFC-0010's `depends_on` did **not** gain RFC-0011 despite a reviewer
  suggestion: the reference is §5 Integration prose — a citation, not a
  reliance (verification rule 5) — and the edge would create a dependency
  cycle. RFC-0004 **was** added (clause-anchored reliance in
  RFC10-17/18(a)).
- No OpenSpec content, no implementation artifacts, no acts performed, no
  candidate labeled accepted.
