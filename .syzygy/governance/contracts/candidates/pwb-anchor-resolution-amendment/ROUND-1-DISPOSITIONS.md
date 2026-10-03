> # Record beside the packages — not authority, binds nothing
>
> Dispositions of the one fresh-context review of the two N9 machine-channel
> amendment packages: this directory's PWB anchor-resolution amendment and
> `../three-surface-poc-block-provenance-amendment/`. This record is not a
> package artifact: neither manifest hashes it and no builder reads it. It
> offers nothing and performs no act (VIS-4).

# Round 1 dispositions — N9 machine-channel amendments (PWB and POC halves)

- **Reviewed commit:** `41ce0a9215c3985d0d219039d11b5819c78f4dc8`.
- **Verdicts (raw lines 5 and 6):** PWB `REVISE`; POC `REVISE`. Five revise
  findings (1, 2, 7, 8, 9) and seven notes (3–6, 10–12); no blocking finding.
- **Stopping rule, set in `REVIEW-BRIEF.md` before the round ran.** One round
  only. A notes-only verdict clears the bytes it read; any other verdict is
  repaired once, no second round is dispatched, and the package goes to the
  owner with the repaired bytes unreviewed.
- **Applied here:**
  - all twelve findings are repaired or answered below;
  - the repair retires the round-1 review (rule 10), so **neither package's
    repaired bytes have been reviewed**;
  - no second round is dispatched.
- **Status: not cleared.** Neither version is ready for sign-off in the sense
  Scope A item 3 requires ("a package is offered only after a round that
  returns CONFIRM, or CONFIRM WITH EXCEPTIONS with notes only"). Both go to
  the owner as pending rows P-96 and P-97, and both packets recommend one
  confirmation round before signing.
- **Re-derived figures** [Observed], from the repaired bytes:
  - `build_pwb_anchor_resolution_amendment.py --check`: 11 subjects, 2
    patched; 17 requirements, 52 scenarios. `--selftest`: 25 structure
    mutants (17 at the reviewed commit), each failing on its own predicate,
    plus patch drift and three sibling fixtures;
  - `build_three_surface_poc_block_provenance_amendment.py --check`: 6
    subjects, 2 patched; 24 requirements, 24 scenarios. `--selftest`: 19
    structure mutants (14 at the reviewed commit), plus the same four
    fixtures;
  - the evidence record was regenerated from the extended script over the
    same two captures; the headline figures (883 of 902, 772,900 bytes) are
    unchanged.

Reviewed record: docs/reviews/R-N9-MACHINE-CHANNEL-AMENDMENTS-1-RAW.md

## Dispositions

### 1 — "resolves" rests on two undefined terms (revise, PWB)

**Accepted.** The amended text now names the field and the comparison: a
record "with an `identity` field of its own whose whole value equals the
anchor's target identity". It also says that a reference field (a stamp's or
a support's source identity) is not a record's own identity, and that a
composed identity counts for nothing. The script's population was widened to
match the text: every object in the body with a string `identity` field, not
only `projectShape.sources[]`. [Observed] That population is the same 285
objects, so the figure stays 883 of 902; the record carries both counts. The
builder pins both new sentences, and mutants "resolution loosened" and
"references admitted" fail on them.

### 2 — the oracle's resolver cannot read "only the machine answer's bytes" (revise, PWB)

**Accepted.** The oracle now reads: "An independent resolver that reads only
the machine narrative's anchors and the machine answer's bytes at the same
evaluation, and imports no rendering code". The oracle-independence limb no
longer says "over the machine answer's bytes". `SEMANTIC-DELTA.md` gains a
paragraph on PWB-REQ-020's derivability rule: 883 target identities are served
verbatim, and 19 are compositions of served fields. That claim is
[Inferred] from the two composition sites in the code. The paragraph says
this delta does not change how anchors are composed.

### 3 — the pair is not said to be non-evidence; "resolve" collides with RFC7-3's verb (note, PWB)

**Accepted, both halves.**

- New sentence: "The pair is itself presentation: no evidence, snapshot input
  or status claim SHALL take it as input." The falsifier gains "a status
  claim fed … by its pair".
- New bullet: "This resolution runs from an anchor to a record of the machine
  answer. It is not the relation RFC7-3 forbids". The field name
  `anchorsResolved` came from the coordinator's ruling, so the verb was kept
  and disambiguated rather than renamed.

### 4 — the pair has no Unknown arm (note, PWB)

**Accepted.** New text: "When the machine answer at that evaluation serves no
record with an identity of its own, every pair is Unknown with its reason,
never a count." The case, oracle and falsifier each gain the matching limb:
withhold every identity, every pair Unknown, and a count where it should be
Unknown.

### 5 — "names the one block it belongs to" has no stated predicate (note, PWB)

**Accepted.** The shape bullet and the oracle now say the anchor's identity
"begins with the identity of the one block it belongs to followed by `#`".

### 6 — builder structure predicates miss semantic weakenings (note, both)

**Accepted.**

- Each of the reviewer's six mutations is now a selftest mutant and fails:
  - the authority sentence deleted;
  - a shape field dropped;
  - a "MAY be cited" line inserted;
  - "may be estimated";
  - the POC sweeps narrowed to a sample, for POC-REQ-001 and POC-REQ-010.
- A new engine predicate, `token_counts`, pins exact token counts per amended
  block:
  - PWB-REQ-014 has `citable` exactly 9 times and `MAY` zero times;
  - each POC block has `MAY` zero times.

  So an inserted permissive sentence fails even when every required phrase
  survives.
- Every mutant now names the phrase it expects to lose, and expected strings
  are compared with quotes stripped. A mutant can no longer pass on a
  different phrase's loss.
- Residual: a weakening that adds no counted token and removes no pinned
  phrase still passes the structure gate. That is why the review stays the
  gate.

### 7 — the shared shape has no slot for the capture instant (revise, POC)

**Accepted.** Both requirements now say: "The capture instant stays on the
observation beside that record, as the second half of the observation's
identity. It is not a second statement of provenance." The shared shape is
left as it is, so no fourth shape appears. "One record" is now "one record in
the shape each element of the machine answer's entity and relationship
provenance lists takes". That answers the list-or-element question.

### 8 — "name the revision nowhere else" has no oracle limb (revise, POC)

**Accepted.**

- **Obligation.** It is now "No other field of the observation, its own or an
  entry's, SHALL hold the revision as its whole value". That defines "name"
  as whole-value equality.
- **Case and oracle.** They now sweep every field of the served observation.
  Exactly one field may hold the revision (the record's) and exactly one the
  capture instant (the observation's own).
- **Falsifier.** It reads "with any other field holding the revision".
- **Builder.** The "header limb dropped" mutant fails.

### 9 — two [Observed] sweeps produced by no named script (revise, both)

**Accepted.** `scripts/measure_machine_channel_provenance.py` now computes:

- the header-repeat sweep (`headerRepeats`);
- the second method (`resolution.secondMethod`);
- the deep-dive leaf check (`deepDiveLeaves`).

The evidence record was regenerated from its output alone. Its `method` field
says nothing else in the record is a measured figure, and a
`scriptCommitNote` says the script changed after this round.

The packets' wording follows the record:

- The PWB packet no longer says the 19 "point at records the machine answer
  serves without an identity". It says they name targets served nowhere as a
  whole value, and that each is [Inferred] composed from served fields.
- PWB question 3's leaf-identity claim is now [Observed] from
  `deepDiveLeaves`.
- The POC figure is restated in the sweep's own terms: `value` in 415 of the
  415 declarations whose fact states a value.

### 10 — the whole-value rule can fire on a genuine value (note, POC)

**Accepted for the capture instant.** In POC-REQ-010 a work item's created,
updated and closed times are read from the database. They are left out of the
capture-instant comparison, and the falsifier says so. The revision arm keeps
no exception. A prefixed or truncated repeat still passes, as the reviewer
says; owner question 3 already discloses that narrowing.

### 11 — the SHALL bullets read unconditioned (note, POC)

**Accepted.** The bullets now open "The observation so produced SHALL …"
(POC-REQ-001) and "The observation so served SHALL …" (POC-REQ-010). That
ties them to the requirement's own trigger. The reviewer's judgement that the
form stays `event-response`, and that POC-REQ-001 belongs, is recorded in
`SEMANTIC-DELTA.md`.

### 12 — the bead's unrendered-fraction assertion (S6-M3) is not accounted for (note, both)

**Accepted.** Both deltas' "What explicitly does NOT change" now say that the
S6-M3 test is in neither package, needs no specification change, and belongs
in a test-only bead. [Inferred] That bead is for the coordinator to file.
