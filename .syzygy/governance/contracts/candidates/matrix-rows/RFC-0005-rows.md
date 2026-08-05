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
