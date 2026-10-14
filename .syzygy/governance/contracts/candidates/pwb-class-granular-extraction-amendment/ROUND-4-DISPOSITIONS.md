> # Record beside the package — not authority, binds nothing
>
> Dispositions of the fourth fresh-context review of the PWB class-granular
> extraction amendment package (P-86). This record is not a package
> artifact: the manifest does not hash it and no builder reads it. It is
> the sibling record the owner's 2026-09-26 ruling provides for a
> notes-only round (`../../../decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
> §1), named by this package's brief (`REVIEW-BRIEF.md` §"Round 4"). It
> offers nothing and performs no act (VIS-4).

# Round 4 dispositions — PWB class-granular extraction amendment

Reviewed record: docs/reviews/R-PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-4-RAW.md

Manifest SHA-256: 4d398a75284cf1dd56d6f0e3a71af68f9daacfea6457b609ff5d319b10518be2

Revise-severity findings: 0

- **Reviewed commit (raw line 2):**
  `c88a621f483b8a702c15b3bcb6f894252a9b0af5`.
- **Verdict (raw line 4):** `CONFIRM WITH EXCEPTIONS`. Four findings,
  every one a note; no revise and no blocking finding (raw line 122).
- **Why the round ran.** The owner's direction of 2026-10-14 for a second
  cycle, recorded in
  `../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md`:
  repair every finding, notes included, then one fresh review under the
  same stopping rule. The brief's §"Round 4" set that rule before the
  round.
- **What clears.** Under the 2026-09-26 ruling, a round with no
  revise-severity finding clears the exact bytes it read: the manifest
  whose file digest stands above, at the reviewed commit, and the package
  prose beside it. [Observed 2026-10-14] The manifest file hashes to that
  digest on the integration branch. `git diff --stat c88a621f` over this
  directory and its builder was empty there before this record was added.
  The builder's `--check` passes there.
- **Nothing in the package is edited.** Every note below is dispositioned
  here, not in the reviewed bytes. Repairing any of them in the package
  would retire the clearance (rule 10). Each is **open** for the owner,
  with the repair the raw suggests.
- **What the clearance is not.** It is not a sign-off. Q1–Q8 stay the
  owner's (VIS-4).

## Corrections carried here instead of in the package

These sentences in the cleared bytes are no longer true as of 2026-10-14.
This record, not an edit, carries the correction:

- `OWNER-DECISION-PACKET.md` lines 23–24, `SEMANTIC-DELTA.md` lines 39–40
  and 761–762, and `ROUND-3-DISPOSITIONS.md` lines 115–116, each
  "Round-3 findings repaired once on 2026-10-14, unconfirmed pending
  round 4". Round 4 has run and returned `CONFIRM WITH EXCEPTIONS` with
  notes only, so the repaired bytes are cleared, not unconfirmed.
- `ROUND-3-DISPOSITIONS.md` lines 39–41, "No round 4 is dispatched", as
  marked "a round 4 is now prepared"; and lines 42–45, "The bytes are not
  cleared", as marked "repaired once, unconfirmed pending round 4;
  nothing is cleared or offered". Round 4 was dispatched, has run, and
  clears the bytes it read.
- `REVIEW-BRIEF.md` line 205, "This section prepares round 4; it does not
  dispatch it." Round 4 has since been dispatched. The brief is not
  edited.

Register row P-86 and `docs/README.md`'s class-granular row sit outside
the package and are updated directly.

## Composition at the integration branch

[Observed 2026-10-14] On the integration branch over `origin/main`
`8acb0795`, after P-85's regeneration landed, all four pending PWB
builders' `--check` pass: release-label, class-granular, accessible-name
and opening-index. That is the re-run note 4 asks for, at that commit
only. It does not settle the `design.md` decision-12 and
`CAPABILITY-COVERAGE.md` row-34 collision with P-85, which the P-85
round-4 raw's note 8 observed and packet Q5 routes to regeneration and
re-review of whichever is signed second.

## A residual for the sign-off recorder

[Observed 2026-10-14] This package is not registered in
`scripts/record_versioned_signoff.py`'s package table, so a sign-off
cannot be recorded until it is. Run against this raw, `parse_head` reads
the reviewed commit, the manifest digest and the verdict, and the findings
section parses as four notes.

## Dispositions

### 1 — scenario 4 exercises the built-in tree-rule cases only (note)

**Open.** Raw line 83. Nothing in scenario 4's WHEN makes an index name
another pillar's index file, so its last AND holds without the
nested-pillar case, the one case where today's code differs from the text
(packet Q8). The Case line omits it, and the loaded-profile clauses have no
scenario. The oracle and falsifier limbs still reach every clause.
Suggested repair: say "pillar indexes name" in the WHEN, and add a
nested-root fixture to the WHEN or as its own scenario.

### 2 — the structure predicate does not guard scenario 4's THEN outcomes (note)

**Open.** Raw line 95. The reviewer's mutant flipping the baseline limb to
`pillar-named-file` fails only on the generic dependency-digest finding.
`--check` still catches the edit through regeneration. Suggested repair:
add the THEN line to `REQ_REQUIRED_ONCE`, with a mutant.

### 3 — "leaves that pillar's index and named files unadmitted" reads absolute against the new precedence for nested roots (note)

**Open.** Raw line 103. For nested roots where the inner pillar is not
named, or is named ambiguously, one sentence leaves the inner `README.md`
unadmitted and the order admits it under rule 2; the code admits it. The
natural reading ("unadmitted as that pillar's") agrees with the code.
Suggested repair: scope the sentence to the first and second rules for
that pillar, or name the case in Q8.

### 4 — the release-label `--check` failed at the reviewed commit for a sibling-lane reason (note)

**Open, with the re-run recorded above.** Raw line 111. At `c88a621f` the
release-label builder's dependency patch no longer applied after the P-96
sign-off. Its lane has since regenerated (`8acb0795`) and the builder
passes on the integration branch. The `design.md` and
`CAPABILITY-COVERAGE.md` collision with P-85 stays open under Q5.
