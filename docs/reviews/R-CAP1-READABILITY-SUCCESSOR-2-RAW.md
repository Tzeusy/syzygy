# R-CAP1-READABILITY-SUCCESSOR-2 — Capability 1 readability successor confirmation
Verdict: CONFIRM WITH EXCEPTIONS
Manifest-file SHA-256: 10db138947497200ad7c788ce4719ba515c61832e3138f1af42201ec84a8870d
Reviewed commit: 2566371bf0e67cf0560ef7124459d8e481a53612

## Scope

Subject: `git diff d1c220a 2566371` — 12 files, two commits (35ffe93, the
generic tool and the Capability 1 package; 2566371, the repair of review 1).
Files: `scripts/readability_successor.py`, `scripts/check_governance.py`,
`scripts/check_docs_review_campaign_partition.py`, `PROJECT-STATUS.md`,
`.github/workflows/governance-docs.yml`, `docs/README.md`, the retained raw
`docs/reviews/R-CAP1-READABILITY-SUCCESSOR-1-RAW.md`, and the package
`.syzygy/governance/contracts/candidates/capability-1-readability-successor/`
(`SUCCESSOR.json`, `SUCCESSOR-MANIFEST.txt`, `OWNER-DECISION-PACKET.md`,
`proposed/.../proposal.md.proposed`, `proposed/.../design.md.proposed`).

Governing references read: AGENTS.md ("Hard prohibitions", "Epistemic and
change discipline", "Verification rules", "Governance recorders");
`CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md`;
`CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md` (by reference from the new
Impact section); `ACCEPTANCE-ACT-RECORD.md` (the general trusted-bootstrap
row 2, `sign-off-coverage-amendment`); review 1's raw. The untracked consent
candidate `openspec/changes/cap1-trusted-bootstrap-consent/` was read,
read-only, in the owner's root checkout.

All experiments ran in scratch clones `b0` (reviewed commit), `b1`
(simulated adoption) and `b2` (refusal and mutation probes) under
`scratchpad/caprev2/`; the reviewed clone was not modified.

## Facts established

1. [Observed] `sha256sum SUCCESSOR-MANIFEST.txt` at the reviewed commit
   equals the digest in the head above. The packet offers exactly one
   phrase, `SIGN OFF CAPABILITY 1 READABILITY SUCCESSOR: <that digest>`, and
   carries the digest once.
2. [Observed] Predecessor digests in `SUCCESSOR.json` equal the current
   bytes of all seven subjects. Six equal the adoption act's rows (lines
   27–33) verbatim; `CONTRACT-COVERAGE.md`'s predecessor is absent from the
   adoption act (whose row is the pre-amendment digest) and present in
   `ACCEPTANCE-ACT-RECORD.md` line 116 (row 2, `sign-off-coverage-amendment`),
   the transaction's `TRANSACTION-MANIFEST.txt` and
   `GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-ACT.md`. `tasks.md` is not a
   subject, consistent with the adoption act's lines 35–38. Manifest rows:
   five equal the predecessor; `proposal.md` and `design.md` equal the
   sha256 of their `.proposed` files.
3. [Observed] The diff touches no path under `openspec/`, `apps/`,
   `packages/` or `.syzygy/governance/decisions/` (0 of 12 files). The only
   deleted lines (2) are the battery count sentence and the docs partition
   count sentence. None of the five pre-existing changed files' base digests
   is cited by any tracked file at `d1c220a` (`git grep -F`, 0 citers each).
4. [Observed] Battery before adoption (`b0`, every line of the
   PROJECT-STATUS.md block run, `CS=`/`DR=` evaluated as assignments): 53
   commands (52 checks + `git tag`), 0 nonzero. `check_governance.py`:
   "31 OK, 21 WARN, 0 FAIL (52 checks)"; `--selftest`: "347 fixtures,
   0 failing"; CG-26: "52 published, 52 hosted, 52 shared";
   `readability_successor.py --all --check`: "PASS candidate-unperformed …
   1 successor package(s) checked"; `--selftest`: "30 fixtures, 0 failing".
   `check_docs_review_campaign_partition.py`: "total=286 assigned=286 …
   unmatched=0 overlaps=0".
5. [Observed] Simulated adoption (`b1`): committed a synthetic raw at
   `docs/reviews/R-CAP1-READABILITY-SUCCESSOR-2-RAW.md` with the four-line
   head contract over the manifest digest, pinned `manifest_sha`, `review`
   and `review_sha` in `SUCCESSOR.json`, committed; `--record --phrase
   "<exact phrase>"` exit 0 ("Recorded … subjects installed"); committed.
   Battery again: 53 commands, 0 nonzero; `check_governance.py` 0 FAIL;
   `--all --check` "PASS performed-exact"; partition "total=287 assigned=287
   unmatched=0 overlaps=0" (the `-2-RAW.md` name matches the new campaign
   pattern). The act record's table carries all seven predecessor/successor
   rows and the hard-coded "widens no implementation authority" sentence.
6. [Observed] Installed links: the four relative links in the installed
   `proposal.md` (adoption act, acceptance record, authoring decision,
   implementation-authorization act) all resolve;
   `docs/CAPABILITY-1-IMPLEMENTATION-PLAN.md` and
   `scripts/build_capability_1_spec_dependencies.py`, named in the new
   design, exist.
7. [Observed] Refusals on the real package (`b2`, each from a clean state):
   wrong label; wrong argument (one hex digit); trailing space after the
   digest; raw edited without re-pinning; `Verdict: REVISE`; two
   `Verdict:` lines; no `Manifest-file SHA-256:` line; two identical
   `Manifest-file SHA-256:` lines; a drifted unchanged subject (`spec.md`);
   an edited predecessor digest in `SUCCESSOR.json`; an edited `.proposed`
   file (stale manifest); an edited `.proposed` file after `--write` (pinned
   digest mismatch) — every one refused with its own message. A raw with
   `Verdict: CONFIRM WITH EXCEPTIONS` records.
8. [Observed] CG-7d/CG-7e: rewriting every copy of the digest in the packet,
   and separately appending a line to the manifest, each yield CG-7d FAIL and
   CG-7e FAIL.
9. [Observed] Selftest mutation spot-check (15 mutants of
   `readability_successor.py`): all 15 killed. Twelve are killed by a
   fixture's own assertion, including the aggregate-content comparison that
   survived in review 1; three (phrase-argument check, already-recorded
   check, act-absent check) only by an uncaught traceback.
10. [Observed] The consent candidate's `BASELINE.json` lists this change's
    `proposal.md` and `design.md` under `protected_predecessors` at the
    predecessor digests; its `spec_requirements_modified` is
    `CAP1-REQ-011`, `CAP1-REQ-046`; its proposal replaces 011 and "the
    consent-specific addition to CAP1-REQ-046"; its files' mtimes are
    2026-09-14; it proposes no change to `proposal.md` or `design.md`.

### Prose fidelity, claim by claim

`proposal.md` [Observed, old lines 1–119 against new lines 1–134]:

- Banner: "adopted … by an exact-digest act, recorded in" the adoption act —
  true (fact 2). "later performed acts amend its files" — true
  (trusted-bootstrap row 2; this act). "Authoring was authorized
  separately, and only as authoring" — true. The old banner's "until that
  act, this change binds nothing" is correctly removed; it was false.
- One-sentence capability — kept, as a bold lead plus three sentences.
- Why: portfolio owner, one trustworthy place, the three questions, honesty
  about what is not known, optimistic answers worse than none with all three
  examples — kept. Foundation sentence — restored in full, including "every
  machine consumer" and all six elements and the Unknown clause. "Every
  later capability's evidence is uninterpretable without it" — restored;
  the three examples and the quoted ordering rule — kept.
- What changes: one new capability, one coherent capability, one
  owner-readable product argument, one acceptance decision (SDR-37), no
  existing capability modified, first specification; six groups named as
  before plus cross-cutting no false success, parity, identity and the write
  boundary — kept. "Modified Capabilities: none" folded into "No existing
  capability is modified" — kept.
- Scope: seven in-scope items — all kept. Non-goals: all 17 of the old list
  are present (certify; health/maturity score; Polaris white paper;
  Trajectory ingestion/accounting; Orrery map; execute/monitor Missions;
  `Mission-ready` semantics with the deferred-posture qualifier; context
  packets; convergence; modify source; edit root README; create Beads work;
  select language/framework/database/renderer/graph store/deployment model;
  register or onboard a real external project during authoring; implement
  anything). "True scope boundaries" sentence — kept.
- Outcomes: six human outcomes — kept; machine outcomes (five fact classes;
  same identity, revision, evaluation identity, epistemic labels; verbatim
  vocabulary; machine-queryable plane; no endpoint-only or UI-only facts) —
  kept.
- Unknowns: four, each with its rendering — kept.
- Impact: "authorizes nothing to be built" kept, as "The specification itself
  builds nothing" and in the non-goal gloss; affected artifacts kept;
  pointer to the implementation-authorization act added (true). "No code,
  APIs, or systems exist to be affected" and "Implementation impact is
  deliberately unplanned" are dropped (see N2).
- Acceptance: exact digest, VIS-4, CC-SPEC-10, CC-SPEC-1…11, both tables with
  CC-SPEC-8/11, three bounded reviews plus one confirming review — kept.

`design.md` [Observed, old lines 1–104 against new lines 1–105]: scope note
kept (no language … deployment model chosen; nothing is an implementation
decision), with "deferred until the owner adopts" replaced by the
implementation-plan pointer (true, disclosed). Context: first
specification, four authority sources, projects shape, invents none — kept.
D1 (six groups plus cross-cutting, `CAP1-REQ-001…064`, gaps, mint/amend/
retire/never renumber, CC-SPEC-3), D2 (inline `warrants` block, six classes,
generator script, `GOVERNING-DEPENDENCIES.md` as union, CC-IMPACT-1, no
second list, cannot drift), D3 (SDR-36 site a2, CAP1-REQ-030, no per-facet
enumerations, SDR-35, RFC2-24, SDR-36 rule 3, CC-SPEC-6), D4 (served-output
oracles, checker-controlled fixtures, CC-SPEC-5, counterexample schema and
denominator, CC-SPEC-4, rule 9), D5 (two tables, CC-SPEC-11, CC-SPEC-8,
Unknown pending owner-reviewed N/A, no self-minted N/A) — all kept.
"Deliberately not designed": four items kept ("deferred until adoption"
dropped, now stale). Risks: both kept. Open questions: P-1, P-21, other open
rows untouched, no foreclosure or presumption, no pending decision as
warrant, recorded rulings list, mechanical checkability, U-01 — kept.
Glosses dropped: "implementation independence" after CC-SPEC-5; "in this
change directory" (unchanged since review 1; see N6).

## Prior findings (review 1)

- **M1 — repaired.** [Observed] New lines 86–87: "implement anything: the
  specification itself authorizes nothing to be built." The added gloss
  restates the old Impact sentence and is true against the adoption act
  (lines 43–45).
- **M2 — repaired.** [Observed] New lines 30–33 restore the foundation
  sentence, including "every machine consumer"; new line 35 reads "Every
  later capability's evidence", matching the quoted rule.
- **M3 — repaired.** [Observed] The "is therefore unaffected" sentence is
  gone. The packet's "One side effect" paragraph says the candidate is
  untracked, in the root working tree since 2026-09-14, would replace
  CAP1-REQ-011 and part of 046, touches none of the files this act changes,
  and pins the current `proposal.md` and `design.md` digests in
  `BASELINE.json`, which must be regenerated after sign-off. Each clause
  matches fact 10.
- **N1 — repaired in the docstring.** [Observed] Lines 4–7 now say headings
  and warrant blocks are kept byte for byte and body text is the review's
  job. The act-record template still says more (N4).
- **N2 — partly repaired.** [Observed] The "aggregate section content
  edited" fixture kills the previously surviving mutant (fact 9). The three
  traceback-only kills remain (N5).
- **N3 — not repaired.** See N3 below.
- **N4 — not repaired** (compressions, the Impact drops, the "7" item).
  See N2 and N6.
- **N5 — repaired.** [Observed] New campaign "Readability successors" with
  pattern `R-(?:CAP1|POLARIS-BASE|POLARIS-UNDERSTANDING)-READABILITY-SUCCESSOR-\d+-RAW\.md`
  and a `docs/README.md` row whose quoted verdict (`REVISE`, line 2) matches
  the raw; the partition has 0 unmatched and 0 overlaps before and after a
  `-2-RAW.md` lands (facts 4, 5).

## Findings

No material findings.

**N1 — The act record's prose fields sit outside every digest the owner or
the review binds.** [Observed] `body()` renders `scope`, `supersedes`,
`title` and `artifact` from `SUCCESSOR.json`, and the predecessor column
for changed subjects from its `predecessor` map; none of these feed the
manifest. In `b2`, after pinning, setting `scope` to "readability restyle;
also authorizes Capability 2 implementation." and `supersedes` to
"EVERYTHING", then `--record` with the exact phrase: "Recorded …";
the act record reads "Act type: … (successor to EVERYTHING)" and "Scope:
readability restyle; also authorizes Capability 2 implementation. …";
`check_governance.py` "0 FAIL"; `--all --check` "PASS performed-exact".
The hard-coded "widens no implementation authority" sentence still appears
beneath, so the record would contradict itself rather than grant anything.
[Inferred] The sibling POC recorder hard-codes these strings in reviewed
code; here they live in the one file the pin commit is expected to edit,
so a change there is easier to miss. Consider rendering the non-pin fields
into the manifest header (then the owner's digest binds them) or pinning a
digest of `SUCCESSOR.json` without `pins`.

**N2 — "Every claim is kept" still overstates the Impact section.**
[Observed] The packet says of `proposal.md` "Every claim is kept. 'Impact'
also names the separate implementation authorization …". Two old Impact
sentences are gone: "No code, APIs, or systems exist to be affected" and
"Implementation impact is deliberately unplanned". Both are false today
(implementation exists under the authorization act and a plan is named by
the new design), so removing them keeps the restyle true and changes no
live meaning; review 1 asked for them to be named and the packet does not.
Name them in "What changes".

**N3 — Banner "lists every bound digest" (review 1 N3, unchanged).**
[Observed] After the act, the aggregate record carries the current digest of
all seven subjects (fact 5), but not the adoption act's original seven rows,
which live in the adoption act itself. "every currently bound digest" would
be exact.

**N4 — The generic act template claims more than the tool guards.**
[Observed] `body()` line 217: "Every requirement, scenario and warrant block
is unchanged; the successor tool verifies that structure." The docstring
now says only headings and warrant blocks are guarded. For this package the
sentence is true (`spec.md` is an unchanged row); for a future package that
proposes a `spec.md` with a body edit it would be false (review 1 fact 8:
a `SHALL`→`MUST` edit passes). Align the sentence with the docstring.

**N5 — Three refusals are exercised only by tracebacks.** [Observed] Fact 9:
the phrase-argument, already-recorded and act-absent mutants make
`--selftest` exit nonzero through an uncaught non-`ValueError`, not through
a fixture's assertion; `expect()` catches only `ValueError`.

**N6 — Minor residue.** [Observed] "(CC-SPEC-5, implementation
independence)" → "(CC-SPEC-5)"; "in this change directory" dropped; the
cross-cutting group is numbered "7." under "six groups, plus cross-cutting
requirements". None changes meaning. `docs/README.md` line 112 still says
the partition figures were "re-derived for HEAD dated 2026-09-28" beside the
new 57/286 figures, which were first true on 2026-09-29 [Observed: the
sentence predates this diff apart from its counts].

## Verdict rationale

Criterion 1: every claim, scope boundary, all 17 non-goals, all outcomes,
all four Unknowns, D1–D5, both risks and every open question survive in the
restyled files; the new banner is true; the only dropped sentences are
statements made false by later acts (N2). Criterion 2: every listed refusal
fails closed on the real package, predecessor digests match the adoption act
and the trusted-bootstrap coverage row, and the selftest kills every
spot-checked mutant, three only by traceback (N5). Criterion 3: the
simulated adoption leaves all 53 battery commands at exit 0 with
`performed-exact`, and the installed links resolve. Criterion 4:
`check_governance.py` 0 FAIL, `--selftest` 0 failing, CG-26 52/52/52, and
the partition reports no unmatched or overlapping path before or after a
confirmation raw lands. Criterion 5: the packet is present tense, offers one
phrase with the recomputed digest, grants nothing beyond the restyle, and no
signed, act or implementation file changes. Review 1's three material
findings are repaired. Six notes remain, none material. The verdict is
CONFIRM WITH EXCEPTIONS.
