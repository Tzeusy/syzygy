# R-M9-POC-IDENTITY-AMENDMENT-6 — fresh-context review, round 6, Three-Surface POC identity amendment
Reviewed commit: 0ea9b4912aceb2b18fd9c080c0a660350140d3d7
Manifest SHA-256: a1c00c7cba872468df752427d358199101a34b62f0ffe77eabe369e23e4b9867
Verdict: REVISE

Reviewer: a fresh-context agent that did not draft the package. Scope: the
brief at
`.syzygy/governance/contracts/candidates/three-surface-poc-identity-amendment/REVIEW-BRIEF.md`,
including its §"Round 6" (head contract and stopping rule).

I read:

- the four patches and the manifest;
- `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md` and `OWNER-DECISION-PACKET.md`;
- the builder;
- the governing references the brief lists, plus the round-5 raw
  `docs/reviews/R-M9-POC-IDENTITY-AMENDMENT-5-RAW.md` and
  `ROUND-5-DISPOSITIONS.md`.

I ran every check in a fresh `git clone` of the worktree, detached at the
reviewed commit (`.../scratchpad/r6clone`). I applied the patches only in a
second scratch clone (`.../scratchpad/r6apply/repo`), never in the worktree.
The worktree's `git status --short` is empty after the review.

Citations written "applied spec.md:N" or "applied CONTRACT-COVERAGE.md:N"
point to the proposed bytes after `git apply` of the four patches in that
scratch clone.

## Verification log

- [Observed] **Commit and manifest digest.** In the clone, `git rev-parse
  HEAD` reads `0ea9b4912aceb2b18fd9c080c0a660350140d3d7`. `sha256sum` of
  the file `THREE-SURFACE-POC-IDENTITY-AMENDMENT-MANIFEST.txt` gives
  `a1c00c7cba872468df752427d358199101a34b62f0ffe77eabe369e23e4b9867`.
- [Observed] **Patches apply to the current signed tree.** `git apply
  --verbose` of all four patches reports "Applied patch … cleanly" for
  each, with no offset. The signed tree already carries the P-97 bytes:
  `git diff --stat 7f43802f 0ea9b491 -- openspec/` is empty. `sha256sum`
  of the six resulting subjects equals the six manifest rows. This is a
  different method from the builder's.
- [Observed] **Signed lines removed.** The `-U0` diff of the applied tree
  removes:
  - 12 matrix lines: three family-table rows, five `COMPUTED_LINES` prose
    lines, and the four Part B2 rows for RFC2-25, RFC6-1, RFC6-3 and RFC6-12;
  - in the spec, only the six `READER_NOTE_EDITS` lines, POC-REQ-060's
    block lines and POC-REQ-060's warrant lines;
  - nothing in `proposal.md`.

  The bound RFC1-26 row "Relations outside the closed table don't exist; no
  prose-widening | covered | POC-REQ-052" survives at applied
  CONTRACT-COVERAGE.md:90.
- [Observed] **`--check`** exits 0: "manifest matches 6 proposed subjects
  (4 patched, 2 unchanged); 26 requirements, Part A 78 clauses over 139
  rows; structure, regeneration and the preserved RFC1-26 row verify".
- [Observed] **`--selftest`** exits 0: "48 structure mutants, patch drift,
  manifest order and subject drift all fail closed on their own
  predicates". Diffing the builder from `e7fd5301` to the reviewed commit
  shows:
  - 13 added phrases (10 in POC-REQ-054, replacing one, and 3 in
    POC-REQ-060);
  - 3 `COVERAGE_ROW_PHRASES`;
  - 16 added mutants.

  These match the disposition's figures.
- [Observed] **`check_governance.py`** in the clone: "32 OK, 21 WARN, 0
  FAIL (53 checks)".
- [Observed] **Dependency file.** In the scratch clone,
  `build_three_surface_poc_spec_dependencies.py --check` passes over the
  applied bytes: "26 requirement(s), 90 distinct authorities".
- [Observed] **Independent recount.** My own Python over the applied matrix
  imports nothing from the builder. Part A gives 139 rows over 78 clauses:
  103 covered, 36 Unknown, and 32 rows marked "Amendment row". The applied
  spec has 26 requirement headings and 28 scenario headings (`grep -c`).
  Both agree with the ledger and the delta.
- [Observed] **Sibling builder.** At this commit,
  `build_three_surface_poc_block_provenance_amendment.py --check` exits 1:
  "GOVERNING-DEPENDENCIES.md.patch does not apply". Its bytes are already
  signed into the tree, so this is expected. It still prints the declared
  mutually-exclusive WARN for this package and the governing-intent
  package. Neither `PROJECT-STATUS.md` nor `.github/workflows/governance-docs.yml`
  names that builder (`grep -F block_provenance`, 0 lines), so no battery
  depends on it. See Finding 43.
- [Observed] **My own rule-6 probes.** A script in the scratchpad applies
  each mutation to the builder's `proposed_bytes()` and regenerates
  `GOVERNING-DEPENDENCIES.md` over each mutated spec, so the dependency
  check cannot catch a prose edit by accident. It then runs
  `structure_findings`. The baseline gives no findings. The two control
  mutants are caught, which shows the harness reaches the guards:
  - "per-element and per-record" changed to "per-element";
  - the RFC6-3 row narrowed to "each element".

  | Probe (all text added or reworded in cycle 2) | Result |
  |---|---|
  | POC-REQ-054 oracle independence: "; an element or record that renders or answers for no source record the shared model reads is attributed to no subject" deleted | survived |
  | POC-REQ-054 Observable: ", and each subject of Unknown ownership is reported Unknown for that comparison" deleted | survived |
  | POC-REQ-054: "or of Unknown ownership" deleted from the no-claim sentence | survived |
  | POC-REQ-054: "that source's subjects are of Unknown ownership and are reported Unknown" changed to "…are owned and are reported Unknown" | survived |
  | POC-REQ-054 Falsifier: "one element or record whose identity differs" changed to "one element whose identity differs" | survived |
  | POC-REQ-054 Oracle: "zero mismatched identities of owned subjects, " deleted | survived |
  | POC-REQ-054 required behavior: "every surface and the machine answer SHALL name" changed to "every surface SHALL name" | survived |
  | RFC6-1 row: ", and which subjects are owned is decided by its stated procedure" deleted | survived |
  | RFC6-3 row: the "counts elements and records attributed to no subject, …" clause deleted | survived |
  | RFC2-25 "never green" row: the other-reading clause deleted | survived |
  | RFC6-1 row: covered consequence widened to drop "for a subject a source authority owns" | survived |

## Round-5 findings: repair check

- **33 (revise) — machine-answer attribution.** Repaired as asked.
  [Observed] Each of the following now reaches records:
  - the oracle-independence sentence: "It attributes each element and
    record to its subject by the source record it renders or answers for,
    never by the identity it carries" (applied spec.md:1060–1062);
  - the ownership test (1065–1067);
  - the equality limb, "per-element and per-record identity equality"
    (1042).

  [Inferred] The round-5 phantom path is closed. A record that answers for
  S's source record but carries v′ is attributed to S, and "zero subjects
  whose elements or records carry more than one identity value" fires. A
  record that answers for no source record now falls under the new limb.

  The RFC6-1 row (applied CONTRACT-COVERAGE.md:141) and the RFC6-3 row
  (:145) quote the requirement's words. The RFC6-3 row's counting clause
  matches the oracle's three counters. The repairer's extra limb is judged
  in Finding 40, and a remaining RFC6-1 problem is Finding 39.
- **34 (note) — the scenario's denominator.** Repaired. [Observed] The
  sweep (1027–1028) and the first scenario (1095–1096) both say "the number
  of identities that appear in more than one of the surfaces and the
  machine answer".
- **35 (note) — the reading of "never green".** Repaired. [Observed] The
  row at :112 carries an `[Inferred]` tag. It names the covered reading,
  "rendered unlike Observed", and says where the other reading lands: "this
  limb is the Unknown positive-status row below". `SEMANTIC-DELTA.md` §3
  says the same, and adds that the oracle does not check the Inferred
  encoding against a positive treatment.
- **36 (note) — the identifier per source.** Repaired in form. [Observed]
  The field is declared "per source, by the implementation slice that
  lands the identity's form". Until then, ownership is Unknown "and [such
  subjects] are reported Unknown for the identity-equality limb, never as
  owned, unowned or passing" (1067–1072). The Observable carries the
  report (1035–1036).

  The repair did change what the RFC6-1 covered row rests on (Finding 39).
  It also leaves the decision rule with no Unknown outcome (Finding 41).
- **37 (note) — guards.** Repaired for the seven probes round 5 reported.
  [Observed] Each has a phrase and a mutant: records attributed by their
  identity, consistency limb for unowned subjects, ownership sentence,
  Unknown-set comparison, object-based Scope, Inferred scenario THEN, and
  RFC6-3 row narrowed. New cycle-2 text is again largely unguarded
  (Finding 42).
- **38 (note) — the sibling regeneration step.** Repaired. [Observed]
  Residual 5 in `SEMANTIC-DELTA.md` names the mutually exclusive P-100
  sibling and the `--write` regeneration and re-review.

## Findings

**Finding 39 — the identifier field is declared by the implementation slice under test, yet the RFC6-1 covered row still claims "equal to the identity that authority gives it", with no Unknown row for whether the declaration is true** (revise)

[Observed] The cycle-2 repair for Finding 36 makes the expected identity
depend on a declaration: "Which field of a source's record format is that
identifier is declared, per source, by the implementation slice that lands
the identity's form" (applied spec.md:1067–1069). The design names that
slice as slice 6, an implementation slice: `POLARIS-M9-ONE-IDENTITY-FUNNEL.md`
row "Slice 6 | L6-M5 (implementation)". The owner packet's Departure 1 says
that slice 6b "picks the form under POC-REQ-054 … It also declares, per
source, which field of that source's records is the identity the source
owns". So the same slice emits the identities and declares the field the
oracle compares them against.

[Observed] The RFC6-1 covered row (applied CONTRACT-COVERAGE.md:141) still
claims the consequence "equal to the identity that authority gives it", on
the ground that "which subjects are owned is decided by its stated
procedure". The disposition for Finding 36 says "No covered row's claim
widened". That is true of the row's words. But what the oracle observes
underneath them has changed. The oracle now observes equality with the
value in a field that the implementation under test declares. Whether
that field is the identity the authority gives is decided by no
requirement.

[Observed] The package treats the same structure differently elsewhere.
For POC-REQ-055's kind-to-class declaration, also written by the
implementing slice, the delta says "No stated procedure decides that
claim, and the slice that emits the relationships also writes the
declaration". It adds the Unknown row "The declared kind-to-class
correspondence matches RFC 0001's class definitions" (:93), and the
packet's Departure 2 says "Whether that mapping is true stays Unknown".
POC-REQ-054's declaration gets none of the three.

[Inferred] CC-SPEC-4's oracle independence requires that "the oracle is
not defined by, and does not consult, the implementation under test". A
slice 6 that declared, for code regions, whatever field it mints would
pass the equality limb by construction. Today, before any declaration, the
covered limb is observed for no subject at all (see Finding 41).

Criterion 3 is not met: the row claims a consequence the oracle observes
only through an undecided declaration, and that uncovered limb is not
listed as Unknown. Repair, by the package's own precedent:

- add an RFC6-1 Unknown amendment row, "The declared per-source identifier
  field is the identity the source authority gives";
- narrow the covered row's justification to "as read through the declared
  per-source field";
- say in delta §1 and in Departure 1 that the declaring slice is the one
  under test and that the declaration's truth stays Unknown.

**Finding 40 — the new unattributed-carrier limb falsifies subjects the shared model holds that no source record backs, including the signed POC-REQ-051 Unknown region, and "source record" is not defined** (revise)

[Observed] This is the limb the repairer added beyond the raw's ask. "An
element or record that renders or answers for no source record the shared
model reads is attributed to no subject" (applied spec.md:1062–1064). The
Oracle then counts "Zero elements or records carrying a subject identity
that are attributed to no subject" (1046–1047), and the Falsifier repeats
it (1076–1077). `SEMANTIC-DELTA.md` §1 says "that falsifies the
requirement".

[Observed] The shared model holds identity-carrying entities that are
seeded, not read from a project source record. In
`packages/three-surface-poc-core/src/poc-seeds.ts`:

- `work:whatsapp-single-event-normalization` ("Planned demonstration work
  has not been materialized");
- `evidence:focused-pytest` ("A test definition is not a captured test
  run");
- `runtime:live-satisfaction`;
- `region:unmapped-code`.

Orrery renders the last of these as POC-REQ-051's region, looked up as
`unmappedRegionEntityId: 'region:unmapped-code'`
(`apps/three-surface-poc/src/orrery.ts:188`). Signed POC-REQ-051 requires
that region: "an explicit Unknown region for the 930 unmapped files". So
the region renders many file records, or none, not one.

[Inferred] The requirement never defines "source record the shared model
reads". The oracle-independence bullet glosses it as "each subject's
owning source record, and a work item's or code region's own reference to
the claim it names", which points to project sources (git, Beads).

- **On that reading**, every element and record for the subjects above is
  "attributed to no subject", so POC-REQ-054 is falsified by subjects that
  the required behavior itself covers ("Every subject the shared model
  holds SHALL carry one identity"). One of them is a region a signed
  requirement mandates. Others are VIS-2's visible not-yet-materialized
  gaps, which the limb would push the implementation to delete rather than
  show. The oracle is then stricter than the required behavior: it forbids
  a model-held subject with no backing record, which the required behavior
  never says.
- **On a reading that counts seeds or declared mappings as source
  records**, the limb holds, but deciding which reading applies takes
  judgment. CC-SPEC-4 asks for an oracle that decides "by a stated
  procedure … without judgment".

[Observed] The same gap shows in what the package says it reaches. The
delta's "Change class" names only the relation kinds and the epistemic
union as non-compliant today. The ledger's "code population the new
requirements reach" names the nine seeded relationships, not the seeded
entities.

Criterion 2 is not met: the falsifier and decision limb are not carried by
the required behavior, and the attribution needs judgment for many-record
and no-record subjects. Repair, any of:

- define "source record" so that it includes the model's declared or
  seeded subject records, and say how a many-record element such as the
  POC-REQ-051 region is attributed;
- narrow the limb to identity values that name no subject the shared model
  holds;
- state the obligation in the required behavior ("every subject the
  shared model holds is backed by a source record") and disclose today's
  non-compliance in the change class and the ledger.

The phantom path that round 5 found must stay closed whichever repair is
chosen.

**Finding 41 — the decision rule has no Unknown outcome, so a run in which every subject is of Unknown ownership passes on the equality limb's zeros** (note)

[Observed] The Observable says that "each subject of Unknown ownership is
reported Unknown for that comparison" (1035–1036). The oracle-independence
bullet says such subjects are "never … passing" (1071–1072). The Oracle's
decision list, though, is a list of zero-counters that "decide" (1046–1055).
Its equality counter is "zero mismatched identities of owned subjects".
Unknown-ownership subjects enter no counter.

[Inferred] Until slice 6 declares a field, every subject is of Unknown
ownership. That includes Beads work items, whose tracker plainly owns
their ids. In that state, an implementation that minted its own ids for
work items and used them consistently would satisfy every zero-counter.
Each subject is honest, since it is reported Unknown. But the requirement's
decided result is not said to be Unknown when its equality limb has no
evidence, which is VIS-2's "no evidence → Unknown, never green" at the
requirement level. One sentence would close it: "where any subject's
ownership is Unknown, the equality limb's result is Unknown, never a
pass".

**Finding 42 — new cycle-2 text is largely outside the phrase guards, and the disposition says otherwise** (note)

[Observed] All 11 of my non-control probes survived `structure_findings`
(see the log). All 11 mutate text that cycle 2 added or reworded. They
include probes that invert meaning:

- undeclared sources' subjects made "owned";
- the Observable's Unknown-ownership report deleted;
- the definition of an unattributed carrier deleted;
- the RFC6-1 row's owned qualifier dropped, which widens a covered claim.

`ROUND-5-DISPOSITIONS.md`, Finding 37's repair row, says every reported
probe "now has a phrase guard and a selftest mutant, and so does every
sentence this cycle added". The first half is true. The second half is
false on these probes.

[Inferred] The manifest digest freezes the reviewed bytes, so this is
defence in depth, as in rounds 4 and 5. Criterion 5 is met: every declared
mutant fails on its own predicate. The disposition sentence, though, is an
untrue claim in a record, and it should be marked.

**Finding 43 — an unmarked stale present-tense sentence in the ledger's sibling note** (note)

[Observed] In `IMPACT-LEDGER.md`, lines 81–83 read: "[Observed 2026-10-14]
its builder's `--check` applies its spec patch with this package's in both
orders and passes over the repaired bytes". At the reviewed commit that
builder's `--check` exits 1 ("GOVERNING-DEPENDENCIES.md.patch does not
apply"), because P-97 is now signed into the tree. The cycle-2 mark below
it corrects "two later candidates" and the Question 2 sentence, but not
this one.

[Inferred] It is dated and labelled Observed, so it reads as history. The
brief asks for every stale sentence to be marked at the sentence, and this
one is not.

## Criteria summary

1. **Ruling content: met.** [Observed] POC-REQ-054 with the ribbon
   scenario, the POC-REQ-060 amendment, POC-REQ-055, Q3's repair (a new
   requirement plus disclosure, with the bound row preserved once) and
   Q4's typed landing zone are present. Both departures are labelled for
   the owner.
2. **The specification bar: not met.** Finding 40: the new
   unattributed-carrier limb is stricter than the required behavior and
   needs judgment for subjects with no backing source record or with many.
   POC-REQ-055 and the amended POC-REQ-060 meet the bar.
3. **Contract claims: not met.** Finding 39: the RFC6-1 covered row's
   authority-equality limb is observed only through an
   implementation-declared field, with no Unknown row, unlike the
   package's own treatment of POC-REQ-055's declaration. The RFC6-3,
   RFC2-25 and other rows are honest.
4. **Signed bytes: met.** [Observed] The patches apply cleanly over the
   P-97-bearing signed tree. Only the declared lines move, and the RFC1-26
   bound row survives byte for byte.
5. **Mechanics: met.** [Observed] `--check` and `--selftest` pass. All 48
   mutants fail on their own predicates. The dependency file equals
   regeneration, and the printed totals equal my independent computation.
   Finding 42 notes guard gaps.
6. **Honest claims: met, with Finding 40's disclosure gap.** [Observed] No
   adoption is claimed and no implementation is scheduled. The five
   residuals are named, and residual 1 is marked answered by the Scope A
   extension.
7. **Plain language: met.** [Inferred] The delta's sections, the two
   labelled departures and the packet's "What you would be signing" let a
   fresh reader restate what changes and what does not.

**Stopping rule.** Per `REVIEW-BRIEF.md` §"Round 6", a `REVISE` goes back
to the owner with its findings open: no further repair and no round 7
without a new owner direction.

Counts: 0 blocking, 2 revise (39, 40), 3 notes (41, 42, 43).
