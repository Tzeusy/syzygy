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
