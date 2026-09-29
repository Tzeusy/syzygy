# R-CAP1-READABILITY-SUCCESSOR-1 — Capability 1 readability successor and successor tool review
Verdict: REVISE
Manifest-file SHA-256: 23e8f91c39b9504936357d43069bea59a47463a854bf27a606963c6a08a96871
Reviewed commit: 9d86800c6e95c96b1b8a20f3386035c4c0c7df20

## Scope

Subject: `git diff f359852 9d86800` (9 files, 909 insertions, 1 deletion):
`scripts/readability_successor.py` (new), `scripts/check_governance.py`
(discovery and CG-7d/CG-7e registration of generic successors, plus 3
selftest fixtures), `PROJECT-STATUS.md` and
`.github/workflows/governance-docs.yml` (two battery lines, count word
"fifty-two"), and the package
`.syzygy/governance/contracts/candidates/capability-1-readability-successor/`
(`SUCCESSOR.json`, `SUCCESSOR-MANIFEST.txt`, `OWNER-DECISION-PACKET.md`,
`proposed/.../proposal.md.proposed`, `proposed/.../design.md.proposed`).

Governing references read: AGENTS.md (named sections);
`CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md`;
`CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md`;
`CAPABILITY-1-SPECIFICATION-AUTHORING-DECISION.md` (head);
`ACCEPTANCE-ACT-RECORD.md` (row 2 of the general trusted-bootstrap
transaction); `PENDING-OWNER-DECISIONS.md` (P-1, P-21 rows).

All experiments ran in scratch clones `exp0`, `exp1`, `exp2`, `mut` under
the scratchpad; the reviewed clone was not modified.

## Facts established

1. [Observed] `sha256sum SUCCESSOR-MANIFEST.txt` = the digest in the head
   above; the packet offers exactly one phrase,
   `SIGN OFF CAPABILITY 1 READABILITY SUCCESSOR: <that digest>`.
2. [Observed] All seven `predecessor` digests in `SUCCESSOR.json` equal the
   current bytes at the reviewed commit. Six equal the adoption act's rows
   verbatim; `CONTRACT-COVERAGE.md` equals the digest in
   `ACCEPTANCE-ACT-RECORD.md` line 116 (general trusted-bootstrap row 2,
   `sign-off-coverage-amendment`) and in that transaction's
   `TRANSACTION-MANIFEST.txt`; the adoption act's own row for that file is
   the superseded pre-amendment digest. Manifest rows: 5 unchanged
   (predecessor), `proposal.md` and `design.md` = sha256 of the `.proposed`
   files.
3. [Observed] The diff touches no file under `openspec/`, `apps/`,
   `packages/` or `.syzygy/governance/decisions/` (`git diff --stat` over
   those paths empty). No signed file, performed act or implementation file
   changes.
4. [Observed] Battery at the reviewed commit (every line of the
   PROJECT-STATUS.md block, `CS=`/`DR=` evaluated as assignments): 53
   commands (52 checks + `git tag`), 0 nonzero. `check_governance.py`:
   "31 OK, 21 WARN, 0 FAIL (52 checks)"; `--selftest`: "347 fixtures,
   0 failing"; `readability_successor.py --all --check`: "PASS
   candidate-unperformed … 1 successor package(s) checked"; `--selftest`:
   "29 fixtures, 0 failing". CG-26 holds (0 FAIL).
5. [Observed] Simulated adoption (`exp1`): committed a synthetic raw at
   `docs/reviews/R-CAP1-READABILITY-SUCCESSOR-1-RAW.md` with the four-line
   head contract, pinned it in `SUCCESSOR.json`, committed; `--record
   --phrase` exit 0; committed. Battery again: 53 commands, 0 nonzero;
   `check_governance.py` 0 FAIL; `--all --check` "PASS performed-exact".
   The dedicated act and the marked aggregate section were written; the
   aggregate section carries the seven predecessor/successor rows.
6. [Observed] The installed `proposal.md`'s four relative links
   (`../../../.syzygy/governance/decisions/` + ADOPTION-ACT,
   ACCEPTANCE-ACT-RECORD, AUTHORING-DECISION, IMPLEMENTATION-AUTHORIZATION-ACT)
   all resolve; `docs/CAPABILITY-1-IMPLEMENTATION-PLAN.md` named by the new
   design exists.
7. [Observed] Refusals on the real package: `--record` at the reviewed
   commit refuses "unpinned". Post-act drift states in `exp1`, each
   `--all --check` FAIL with the expected message: proposal reverted; design
   appended; design reverted (partial install); act removed; aggregate
   section prose edited; aggregate block removed; pinned raw edited.
   Pre-act: proposal installed without act FAIL ("differs from its
   predecessor digest"); label appended to aggregate without act FAIL.
8. [Observed] Structure guard on the real CAP1 spec (`exp2`, a proposed
   `spec.md`): STRUCTURE finds 42 requirement headings, 47 scenario
   headings, 42 warrant blocks — equal to independent counts of
   `^### Requirement:`, `^#### Scenario:`, `^```yaml` and `warrants:`. A
   renamed scenario heading and an edited warrant block are both refused
   ("structure changed"). A requirement-body edit (`SHALL`→`MUST`) passes
   (see N1).
9. [Observed] CG-7d/CG-7e registration: rewriting the packet's digest copy
   (every occurrence) yields CG-7d FAIL and CG-7e FAIL; appending a line to
   the manifest yields the same two FAILs.
10. [Observed] Selftest mutation run (23 mutants of
    `readability_successor.py`): 22 killed, 1 survived — removing
    `or aggregate.count(self.block(actual)) != 1` leaves "29 fixtures,
    0 failing" (N2). Four mutants (phrase-argument check, extra-proposed
    check, act-absent check, already-recorded check) are killed only by an
    uncaught non-ValueError traceback, not by a fixture's own assertion.
11. [Observed] P-1 (deferred waves C1/C2, D1/D2) and P-21(a) are still open
    in `PENDING-OWNER-DECISIONS.md`, so the new design's "The open decision
    queue stays open" is true.
12. [Observed] `cap1-trusted-bootstrap-consent`, named by the packet, is
    absent from the tree at the reviewed commit (`git ls-tree -r` count 0;
    `git grep` finds only the packet line). An untracked copy exists in the
    owner's main working tree; its `BASELINE.json` lists
    `project-registration-and-honest-shape-visibility/proposal.md` and
    `design.md` under `protected_predecessors` at their predecessor digests
    (see M3).

### Prose fidelity, claim by claim

proposal.md [Observed, compared line by line]: one-sentence capability —
kept (split into a bold lead and three sentences). Why: portfolio owner,
three questions, honesty about unknowns, optimistic tools worse than no
answer with all three examples — kept. Ordering rule and its quotation —
kept but altered (M2). Foundation sentence — dropped (M2). What changes:
six groups named identically, cross-cutting no-false-success, parity,
identity, write boundary; no existing capability modified; first
specification; SDR-37 — kept ("future" dropped from "one future acceptance
decision", N4). Scope: seven in-scope items — all kept. Non-goals: 17
items in the old list; 16 kept; "implement anything" dropped (M1). The
"true scope boundaries" sentence — kept. Human outcomes: six — kept.
Machine outcomes: five fact classes, same identity/revision/evaluation
identity/labels, verbatim vocabulary, no endpoint-only or UI-only facts —
kept. Unknowns: four — kept. Impact: "No code, APIs, or systems exist to be
affected" dropped and "authorizes nothing to be built" replaced by a
pointer to the implementation-authorization act — the replacement is
disclosed and true against that act; the first drop is not named (N4).
Acceptance: exact digest, VIS-4, CC-SPEC-10, CC-SPEC-1…11, both tables with
CC-SPEC-8/11, three bounded reviews plus one confirming — kept.

Banner [Observed against the acts]: "adopted … by an exact-digest act,
recorded in" the adoption act — true; "later performed acts amend its
files" — true (trusted-bootstrap row 2; this act); "Authoring was
authorized separately, and only as authoring" — true, though the old
"never a product-behavior warrant" gloss is compressed away (N4);
"ACCEPTANCE-ACT-RECORD.md lists every bound digest" — true of the current
digests only once this act is recorded (N3).

design.md [Observed]: scope note — kept, with "deferred until the owner
adopts" replaced by a plan pointer (true, disclosed). Context: four
authority sources and "invents no new shape" — kept. D1 (groups, gap
numbering, mint/amend/retire/never renumber, CC-SPEC-3), D2 (inline
warrants, six classes, generated union, CC-IMPACT-1, no second list),
D3 (SDR-36 site a2, CAP1-REQ-030, no per-facet enumerations, SDR-35,
RFC2-24, SDR-36 rule 3, CC-SPEC-6), D4 (served-output oracles, CC-SPEC-5,
counterexample schema and denominator, CC-SPEC-4, rule 9), D5 (both tables,
CC-SPEC-11/8, Unknown pending owner-reviewed N/A, no self-minted N/A) — all
kept. "Deliberately not designed": four items kept; "— deferred until
adoption" on the first item dropped (stale; N4). Risks: both kept. Open
questions: P-1, P-21, other rows untouched, no pending decision as
warrant, recorded rulings list, U-01 — kept. Minor glosses dropped:
"implementation independence" after CC-SPEC-5, "in this change directory"
for GOVERNING-DEPENDENCIES.md (N4).

## Findings

**M1 — A non-goal is dropped without disclosure, and the packet says "Every
claim is kept."** [Observed] Old `proposal.md` lines 66–76 end the
non-goal list "register or onboard a real external project during
specification authoring; implement anything." The proposed file's
non-goal list (lines 67–80) ends at "…during specification authoring." and
"implement anything" appears nowhere in it. The packet's "What changes"
says of `proposal.md`: "Every claim is kept. 'Impact' now names the
separate implementation authorization…" — it discloses the Impact change
but not the removal of a Scope non-goal. Removing it is defensible (the
implementation-authorization act makes it stale), but criterion 1 and the
owner direction require every non-goal to survive or the change to be
named; as written the owner is told nothing was dropped. Repair: either
keep the non-goal with a dated qualifier, or name its removal (and the
Impact sentence "No code, APIs, or systems exist to be affected") in the
packet and correct "Every claim is kept."

**M2 — The Why section drops the foundation claim and narrows "capability"
to "view".** [Observed] Old lines 17–21: "Capability 1 establishes the
truthful project foundation every later view and every machine consumer
builds on: registration, consent boundaries, a fixed human entry, seven
independent shape answers, explanations, and repository discoverability —
with every Unknown carrying its reason." No sentence in the proposed file
carries this claim, in particular that every machine consumer builds on
Capability 1. Old line 28: "every later capability's evidence is
uninterpretable without it"; proposed line 30–31: "Every later view's
evidence is uninterpretable without it." The quoted ordering rule in both
versions speaks of capabilities, so the paraphrase no longer matches its
own quotation. Repair: restore the foundation sentence (as a list if
preferred) and "capability".

**M3 — The packet's claim that the consent candidate "is therefore
unaffected" is unverifiable at the reviewed commit and contradicted by
the only copy that exists.** [Observed] Packet lines 41–42: "The pending
consent candidate (`cap1-trusted-bootstrap-consent`, which would replace
CAP1-REQ-011 and part of 046) is therefore unaffected." That change is not
in the repository at 9d86800 (fact 12). The untracked copy in the owner's
working tree lists this change's `proposal.md` and `design.md` as
`protected_predecessors` at exactly the predecessor digests this act
replaces, so signing this successor makes that candidate's baseline stale.
[Inferred] The sentence bears on how the owner sequences two packets.
Repair: drop the sentence, or state that the consent candidate's baseline
names both files and must be regenerated after this act (or that this act
must follow it).

**N1 — The structure guard does not protect requirement bodies.**
[Observed] Fact 8: a `SHALL`→`MUST` edit inside a requirement passes
`--check`. The guard meets criterion 2 as stated (headings and warrant
blocks), and this package proposes no `spec.md`, but the module docstring
says a successor keeps "every requirement, scenario and warrant block",
and the POC predecessor builder verifies that requirement bodies preserve
their words. A future package that proposes `spec.md` relies on review
alone for body text. Consider narrowing the docstring or adding a body
guard.

**N2 — One predicate has no selftest fixture.** [Observed] Fact 10: the
aggregate-section content comparison survives deletion; the real check
does catch a prose edit inside the section (fact 7), but no fixture edits
the section body without also touching the binding line or the markers.
Add one. Four other refusals are exercised only via tracebacks, because
`expect()` catches only `ValueError`.

**N3 — Banner wording.** [Observed] "ACCEPTANCE-ACT-RECORD.md lists every
bound digest" is true of the current digests only after this act is
recorded (the 2026-08-20 adoption act's seven rows are not in the
aggregate; only the coverage amendment row is). Since the banner is
installed only by this act, it is true when it appears, but "every
currently bound digest" would say so.

**N4 — Minor undisclosed compressions.** [Observed] "one future acceptance
decision" → "one acceptance decision"; "authorization to author only, never
a product-behavior warrant" → "only as authoring"; "(CC-SPEC-5,
implementation independence)" → "(CC-SPEC-5)"; "in this change directory"
dropped; "— deferred until adoption" dropped from "Deliberately not
designed"; "No code, APIs, or systems exist to be affected" dropped. None
changes meaning beyond present-tense truth, but "What changes" in the
packet could list them. The seven-item numbered list under "six groups,
plus cross-cutting requirements" numbers the cross-cutting item "7", which
reads slightly against "six groups".

**N5 — Adoption needs a campaign row.** [Observed] With the raw at
`docs/reviews/R-CAP1-READABILITY-SUCCESSOR-1-RAW.md`,
`scripts/check_docs_review_campaign_partition.py` reports `unmatched`. It
is not in the battery or the hosted workflow, so the battery stays green;
the adopting commit should add the pattern and `docs/README.md` row per
AGENTS.md.

## Verdict rationale

The tool meets criteria 2–5 [Observed]: the manifest digest recomputes to
the pinned value, predecessor digests match the adoption act and the
trusted-bootstrap coverage row, every refusal and partial/drifted state
tested fails closed, the simulated adoption leaves all 53 battery commands
at exit 0 with `performed-exact`, CG-7d/CG-7e catch stale copies, and the
diff changes no signed, act or implementation file. Criterion 1 fails on
M1 (a non-goal dropped while the packet says every claim is kept) and M2
(the foundation claim dropped, "capability" narrowed to "view"), and
criterion 6's accuracy requirement fails on M3. Each repair is small and
confined to the two `.proposed` files and the packet, but each changes the
manifest digest, so the repaired package needs a fresh confirmation.
The verdict is REVISE.
