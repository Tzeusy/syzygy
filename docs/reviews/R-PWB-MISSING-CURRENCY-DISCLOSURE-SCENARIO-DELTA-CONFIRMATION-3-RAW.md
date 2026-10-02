PWB missing-currency disclosure scenario (P-69 Q7a) - confirmation review 3
Reviewed commit: 49ef8fde64445ea8b651c52f74c0fd0070bfa467
Manifest SHA-256: 1a64e1ea5e67528528ff1b026cf0dde5f280f6139a0c95cd373a1c9509596c42
Verdict: REVISE

Fresh-context review (CC-REV-1) per the package REVIEW-BRIEF.md. No earlier raw
for this package was read. Package: `.syzygy/governance/contracts/candidates/pwb-missing-currency-disclosure-scenario/`.
The performed `.18` registry act (2026-09-30) was treated as performed, not as a candidate or parked.

## Classification

Normative, agreed. A renderer that force-fit a freshness value onto an unbounded claim complied before and would not after; one that omits freshness for the condition did not comply before and would after. The "clarification scenario" label does not change the compliance population.

## Commands run (archive copy of 49ef8fd under scratchpad; detached worktree removed)

- `build_pwb_missing_currency_disclosure_scenario.py --check`: matches 11 subjects (6 patched, 5 unchanged). `--selftest`: passes. `--diff`: runs.
- `--apply --at-adoption` in the archive copy: all 11 rows hash to the manifest digests (11 of 11 ok). Applied tree: `check_governance.py` gives CG-7h FAIL only, which is expected after editing bound bytes; the unapplied head gives 31 OK / 21 WARN / 0 FAIL.
- Manifest file sha256sum equals the head digest and the owner-packet digest.
- Repair delta: five rows RFC6-14.r1, RFC6-14.r3, RFC6-17.r1, RFC7-16.r1, RFC7-33.r1 flip covered to unknown-uncovered; totals 132 covered / 242 Unknown over 622 regenerate. A sweep of the remaining `covered:` rows mentioning freshness found none further (RFC2-24.r1, RFC6-17.r3 and RFC6-14.r2 concern reason counts and headline status, which the scenario preserves).
- Mutations of spec.md.patch (8, in an archive copy): dropping the zero-never, owner-act-provenance, reconciliation, primary-count/route, aggregate-Unknown tokens and the fifth-value clause each fail `--check`. Mutants of the route, fifth-value and aggregate-count text failed as "corrupt patch" (hunk counts), so they did not isolate their own predicates.
- Sweep: `git ls-files -z` at 49ef8fd gives 1,772 paths (1,768 decoded, 4 PNG skipped); literal `PWB-REQ-007` appears in 119 files.

## Findings

**Finding 1 — aggregate freshness "reads `Unknown`" force-fits a fifth value into the closed freshness slot** (revise)
The scenario forbids minting "a fifth value ... for that condition" and says the member's freshness is disclosed outside the slot (`proposed/spec.md.patch:13-17`), but its last bullet makes the aggregate's own freshness read `Unknown` with reason `no-currency-bound-declared` (`proposed/spec.md.patch:25-28`). RFC2-10 (`RFC-0002/snapshot-and-evaluation-core.md:235`) closes the freshness list at `fresh/stale/broken/superseded` and bars forcing a value into it; `Unknown` is a label, not a freshness value. The delta (`SEMANTIC-DELTA.md:160`) and packet (`OWNER-DECISION-PACKET.md:80`) call this "met by an Unknown value, not excused". The scenario therefore applies one rule to a member (disclose outside the slot) and the opposite to the aggregate (put a non-vocabulary value in the slot). A reason is also attached to an aggregate freshness although aggregates are not claims. VIS-2 is satisfied in substance (nothing shown as fresh, zero or omitted), but the form contradicts RFC2-10 and the scenario's own AND clause. Repair: state the aggregate's freshness presentation as the same outside-slot named disclosure carrying the member count, or have the owner rule on an aggregate-level Unknown in the slot. Add a predicate that the aggregate bullet does not name a freshness value outside the four.

**Finding 2 — impact-ledger denominators are not reproducible at the reviewed commit and name no baseline** (revise)
`IMPACT-LEDGER.md:16` states a 1,376-file denominator, and the table gives 90 files / 443 occurrences for `PWB-REQ-007`. At 49ef8fd the tracked population is 1,772 and the literal appears in 119 files (about 111 outside this package; the tree also carries other candidate packages, M12-M14 evidence, `polaris.ts`, `polaris-copy.ts`, `project-shape-model.ts`). The ledger says "at the baseline" without a commit (rules 2, 7, 9). The consumer disposition (`apps/three-surface-poc/src/polaris*.ts`, `packages/three-surface-poc-core/src/project-shape-model.ts` unchanged on this branch) is plausible, but the population it covers is unproven. Repair: name the commit and re-derive all figures, or state which population the 1,376 describes.

**Finding 3 — present-but-ineffective arm: the RFC2-9 contradiction route is "preserved" only in prose** (note)
The scenario text exposes only the `Declare the bound in quality policy` route (`proposed/spec.md.patch:7-12`). `SEMANTIC-DELTA.md:149-152` says the RFC2-9 owner-contradiction route "is preserved unchanged", but RFC2-9 (`snapshot-and-evaluation-core.md:227-229`) requires the invalid declaration to be routed as a contradiction, and nothing in the scenario requires a renderer to show it. A renderer showing only the Declare route for an invalid declaration would satisfy the scenario and silently omit what RFC2-9 binds. The reason and route assignment to this arm is correctly tagged Inferred. Consider one clause stating that the contradiction route remains required for a present-but-ineffective declaration.

**Finding 4 — the freshness-exception sentence has no direct builder predicate** (note)
`scenario_findings` (`scripts/build_pwb_missing_currency_disclosure_scenario.py:153-186`) has no token for "for this condition only ... complete presentation" (`proposed/spec.md.patch:19-21`), the one stated tuple exception (criterion 5). Deleting it is caught only indirectly, as a regenerated dependency-digest drift. Add a direct token, and re-run the route, fifth-value and aggregate-count mutants with patch hunk headers recomputed so they exercise their own predicates (criterion 13).

## Other criteria

Quotation fidelity (RFC2-9, RFC2-10, RFC2-24 row 3, CAP1-REQ-062) matches source. The outside-slot disclosure is recoverable under PWB-REQ-020's "disclosure Polaris presents" clause (spec.md:1020-1024), so machine-answer parity holds. The patch applies over the performed opening-band, render-mode and machine-view text; the dependency patch regenerates from the proposed spec. No sentence calls `.18` a candidate or repeats its numeric bounds; the delta says the scenario is reachable only for an undeclared class or a declaration with missing or invalid provenance. The tuple, reasons, tier, challenge state and identities are preserved; no aggregate headline status is granted; the PWB-REQ-007 / RFC2-10 tension is surfaced. Authority boundary and owner packet (digest exact, silence defaults to current behavior) are acceptable. No bound byte is edited in place.

No owner-only decision prevents exact final bytes beyond Finding 1's choice between an outside-slot aggregate disclosure and an owner ruling that permits an aggregate-level Unknown.
