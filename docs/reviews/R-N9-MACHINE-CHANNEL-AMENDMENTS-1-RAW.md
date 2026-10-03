# R-N9 machine-channel amendments, round 1 (PWB and POC halves)
Reviewed commit: 41ce0a9215c3985d0d219039d11b5819c78f4dc8
PWB manifest SHA-256: b78f1721f4334aea2be9a189b4ba63334ed66f30b3c76fddd521f55a16a0ce75
POC manifest SHA-256: 1aa0b09adbb803b3d184650d6ca3c5af17db192a1405720ac8d446b7068b81e3
PWB verdict: REVISE
POC verdict: REVISE

Reviewer: fresh-context subagent; did not draft either package. Read in a
fresh clone checked out at the reviewed commit. Manifest digests computed by
`git show <commit>:<path> | sha256sum`.

## Checks run (clone, reviewed commit)

[Observed] All nine commands in the brief exit 0:

- `build_pwb_anchor_resolution_amendment.py --check`: "11 proposed subjects (2 patched); 17 requirements, 52 scenarios; ... verify"
- `build_pwb_anchor_resolution_amendment.py --selftest`: "17 structure mutants, patch drift, an unclassified sibling, a vanished pending sibling and a clashing sibling all fail closed"
- `build_three_surface_poc_block_provenance_amendment.py --check`: "6 proposed subjects (2 patched); 24 requirements, 24 scenarios; ... verify"
- `build_three_surface_poc_block_provenance_amendment.py --selftest`: "14 structure mutants, ... all fail closed"
- `build_pwb_class_granular_extraction_amendment.py --check`, `build_pwb_release_label_amendment.py --check`, `build_three_surface_poc_identity_amendment.py --check`: pass.
- `check_governance.py`: "31 OK, 21 WARN, 0 FAIL (52 checks)".
- `check_spec_reconciliation.py --check`: PASS; R6 WARN (2 stale behaviour-contract pins, pre-existing, `syzygy-2g0d`).

Independent checks:

- [Observed] Applying all four patches with `git apply` in a scratch copy of
  `openspec/`: PWB spec sha256 `9324c1c7…` and POC spec `d0ba9eba…`, equal to
  the manifest rows; both GOVERNING-DEPENDENCIES rows also match. Text before
  the first requirement is unchanged in both specs; requirement ids and order
  are unchanged; the only changed blocks are PWB-REQ-014 and POC-REQ-001,
  POC-REQ-010 (criterion 6 holds).
- [Observed] Arithmetic in the evidence record: 7,952 × 50 = 397,600;
  6,950 × 54 = 375,300; sum 772,900; 772,900 / 5,751,883 = 0.134373. Per-row
  byte widths match a 32-char Dolt hash and a 40-char git sha in compact JSON,
  and `routes.ts:231` serves `JSON.stringify(model)` (compact). The packages'
  883 of 902, 697 blocks, 285 served identities and 19 unresolved (11+5+1+1+1)
  match the record exactly. I could not re-run the measurement (captures not
  retained).
- [Observed] Register note "25 ... and 5 ..., 30 in all": re-counted with
  Python `re` `^\| (P-[0-9]+[^ |]*)` per `##` section: 25 and 5, all distinct.
- [Observed] PWB impact ledger "18" files containing `citable` under
  `apps/`+`packages/` at `71b4f525`: `git grep -l -F citable` gives 18.
- [Observed] Bead notes (via read-only `bd show syzygy-u05.9`) carry the
  three coordinator rulings as the packages state.

## Findings

**Finding 1 — "resolves" rests on two undefined terms, so an independent checker cannot reproduce 883 of 902** (revise) [PWB]

Proposed text: "An anchor resolves when the machine answer at the same
evaluation serves exactly one record whose own served identity equals the
anchor's target identity. An anchor whose target the machine answer does not
serve, or serves without an identity of its own, does not resolve."

Neither "record" nor "own served identity" is defined in the amended text or
the reader definitions. The measurement script fixes the answer by fiat:
`identities = Counter(source["identity"] for source in poc["projectShape"]["sources"])`,
i.e. only `projectShape.sources[].identity`. [Observed from the types]
the same identity string is also served as `sources[].stamp.sourceIdentity`
(`EmissionStamp.sourceIdentity`, `project-shape-observation.ts:215`) and as
`sourceIdentity` on claim supports (`ProjectShapeSupport`,
`project-shape-model.ts:112`, populated at 354 and 366). [Inferred] A
checker that treats any `*Identity` key as a record's identity counts more
than one hit for most of the 883 and gets a different number; a checker that
accepts composed identities finds the 17 evidence targets
(`provenanceAnchor`: `` `${item.kind}:${item.digest ?? item.revision}` ``,
`polaris-narrative.ts:105`) as served `entities[].provenance[]` records with
`kind` and `digest`. That record would then be "served" and arguably carry
its identity. The figure depends on the definition, and the text leaves the
definition to whoever wrote the resolver. That is a CC-SPEC-4 oracle defect
("by a stated procedure ... without judgment").

Fix: name the population and the field in the text, for example "a record in
the machine answer's project-shape source population whose `identity` field,
as a whole value, equals the anchor's target identity". Or define "own
served identity" structurally (one named identity field per record class,
whole value, never a reference field such as a stamp or support), and say
that an identity composed from other fields does not count. Then make the
script's `predicate` string quote that text.

**Finding 2 — the oracle's resolver cannot read "only the machine answer's bytes"** (revise) [PWB]

Proposed oracle: "An independent resolver reading only the machine answer's
bytes reproduces each block's `anchorsResolved` pair and the narrative's pair
exactly". The anchors and their blocks are served on `GET /api/poc/polaris`,
which PWB-REQ-020 classes as a derived read-only machine view and says "is
[not] the machine answer". A resolver reading only the machine answer has no
anchors to resolve, so as written the oracle cannot run. The measurement
script itself reads both captures. The same slip appears in the
oracle-independence limb ("from that independent resolver over the machine
answer's bytes").

Related claim to make honest: SEMANTIC-DELTA says stating the predicate
against the machine answer "keeps the field inside PWB-REQ-020's rule for a
derived read-only view". The count is derivable *given* the anchor set. But
[Observed in the record] none of the 19 unresolved target identities "occurs
as a whole string value anywhere in the `/api/poc` body", so the anchor values
the pair counts over are not all literally present in the machine answer.
[Inferred] They may count as lawful compositions (`kind:digest`). The package
should say which, rather than imply the question is settled.

Fix: "An independent resolver that reads the machine narrative's anchors and
the machine answer's bytes at the same evaluation, and imports no rendering
code, reproduces …". Add one sentence on how the anchor target identities
themselves meet PWB-REQ-020's derivability bullet.

**Finding 3 — the authority boundary holds, but the pair itself is not said to be non-evidence, and "resolve" collides with RFC7-3's verb** (note) [PWB]

Assessment for criterion 3: [Inferred] I found no reading of the amended text
under which a narrative unit becomes citable. "A block whose every anchor
resolves stays `presentation-artifact` and `non-citable`; no field derived
from the pair SHALL make a narrative unit citable or stand in for an epistemic
label" is unconditional, and the signed bullet "No project artifact,
evidence, snapshot input, work warrant or internal relation SHALL cite Polaris
as its authority" stays in force and is guarded by `required_once`. Two
residues remain:

- The text forbids the pair from making a *unit* citable. It does not say
  that the pair, or "902 of 902", is never itself an evidence artifact or a
  snapshot input to a status claim (RFC7-3: "never an admissible evidence
  artifact, never a snapshot input to a status claim"). The signed bullet
  covers this only if a reader takes the pair to be "Polaris". One clause
  would close it: "The pair is itself presentation: no evidence, snapshot
  input or status claim may take it as input."
- RFC7-3 uses "resolve to … as its authority" for the forbidden relation. The
  amendment uses "resolves" for anchor → machine-answer record. A reader can
  conflate "the anchor resolves" with something resolving to Polaris. Suggest
  "an anchor *matches* …", or one sentence saying this resolution runs from
  the narrative to a record and is not RFC7-3's relation.

**Finding 4 — the pair has no Unknown arm** (note) [PWB]

"Both numbers are counted, never estimated … A count below its total SHALL
be served as counted". If the machine answer at that evaluation is not served,
or its source population is Unknown, every anchor "does not resolve" and the
text yields a measured `0 of N`, where VIS-2 requires Unknown ("No evidence
yields Unknown — never green, never zero"). Suggest: "When the machine answer
at that evaluation serves no source population, the pair is Unknown with its
reason, never a count."

**Finding 5 — "names the one block it belongs to" has no stated predicate** (note) [PWB]

Shape bullet: "its own identity, which names the one block it belongs to".
Oracle: "names the block that serves it". The measurement uses
`anchorId.startswith(blockId + "#")`, but the text could equally be met by a
separate block-id field or by the block id appearing anywhere in the anchor
id. That is checkable once fixed. Suggest stating the relation, for example
"whose identity begins with its block's identity followed by `#`", or naming
a block-identity field.

**Finding 6 — builder structure predicates miss semantic weakenings; the selftest mutants are honest but sample** (note) [both]

[Observed] Every listed selftest mutant fails on its own predicate. My own
mutations, run through `structure_findings` against the proposed spec
(scratch script, nothing written to the tree), raised **no structure
finding**. Only the derived-dependency digest mismatch fired, because the
bytes moved:

- PWB: delete "The pair counts resolution and never confers authority. ";
- PWB: delete "its revision; " from the anchor-shape field list;
- PWB: insert "  - A block at its full count MAY be cited as evidence." before the "machine-narrative field" bullet;
- PWB: replace "Both numbers are counted, never estimated," with "Both numbers may be estimated,";
- POC: "Over every served item, compare" → "Over one sampled item, compare" (POC-REQ-010);
- POC: "Over every served entry," → "Over one sampled entry," (POC-REQ-001).

A positive mutation (the "MAY be cited" insertion) passes the structure gate
on the RFC7-3 boundary. The builder's docstring discloses "a sample of the
required phrases", so this is a note, not a defect claim. Suggested fixes:
add "never confers authority", the shape's field list and the two "Over every
served …" phrases to `required_once`; add a forbidden-phrase predicate (for
example any `citable` occurrence in PWB-REQ-014 other than the listed ones,
or `MAY be cited`). Separately, the POC mutants' expected prefix "POC-REQ-001
carries 0 copies of required phrase" does not name the phrase, so a mutant
would "pass" on any other phrase's loss. The PWB mutants name theirs; do the
same.

**Finding 7 — the shared provenance shape has no slot for the capture instant, so "one record" and "the identified observation" pull apart** (revise) [POC]

Proposed: "The observation SHALL state its provenance once, as one record in
the provenance shape the machine answer's entities and relationships carry,
and that record names the revision." The reader notes define an "identified
observation" as "the pair (source revision, capture instant)". [Observed]
That shape is `PocProvenance` (`model.ts:44-56`): `kind`, `source`,
`revision`, optional `digest`, with no capture-instant field. Entities carry
a *list* of such records. An implementer has to choose between:

- leaving `capturedAt` in the header, outside the record. Is that provenance
  stated twice, or "in another shape" (a falsifier limb)?
- extending the shared shape, which arguably creates a fourth shape;
- dropping the instant, which breaks the identified-observation pair.

The rule then forbids the capture instant on every row, yet never says where
it lives. Fix: say explicitly that the capture instant stays on the
observation outside the provenance record (and is not a second statement of
provenance), or that the shared record gains a capture-instant field. Also
say whether "one record in the shape" means one element of the entities'
list form.

**Finding 8 — "SHALL name the revision nowhere else" has no oracle limb, and "name" is undefined** (revise) [POC]

Obligation: "The observation SHALL name the revision nowhere else." Falsifier:
"an observation served … naming its revision twice". The oracle sweeps only
"every served entry" and compares whole values. Nothing checks the
observation's header or its other fields, so the header could keep
`revision`/`doltRevision` beside the new record and the stated oracle would
pass. That is the exact case SEMANTIC-DELTA §1 says the clause exists to stop.
"Name" is also undefined: is a prefixed or embedded form (`git-tree:<rev>`,
an abbreviated sha) a naming? Fix: add an oracle limb, for example "over every
field of the served observation, header, record and entries, exactly one
whole value equals the revision, and it is the provenance record's", and
define "name" as whole-value equality (or say substrings count).

**Finding 9 — two [Observed] sweeps cited by the packages are produced by no named script and appear in no record** (revise) [both]

- POC SEMANTIC-DELTA: "**Nothing else in the body repeats a header this way.**
  A sweep over every list of records in the body … finds four populations …
  (`fact` 416 of 416, `value` 415 of 416)". The owner packet's Q3 rests on it
  ("[Observed] The only other repeats of this kind …"). `measure_machine_channel_provenance.py`
  has no such sweep. The evidence record carries none of these figures.
- Evidence record `secondMethod` ("every string value anywhere in the /api/poc
  body … 0") is not computed by the script, while the record's `method` says
  "output copied verbatim under figures". The PWB delta cites it as "A second
  method agrees".
- Lesser: the PWB owner packet's "[Observed] … The 19 that do not resolve point
  at records the machine answer serves without an identity of their own"
  describes a mapping the record never makes (it shows only that the
  targetIds occur nowhere), and Q3's "its identity already equals a block
  anchor's target identity" is in no record.

Under rule 11 and criterion 7, these are figures no later reader can
re-derive. Fix: add the header-repeat sweep and the second method to the
script (or a sibling script) and to the record, with their predicates
stated; otherwise relabel them [Inferred] or name the ad hoc method used.
The rest of the record is internally consistent (see Checks).

**Finding 10 — the whole-value rule can fire on a genuine value, and is narrower than "restates"** (note) [POC]

"No work-item fact SHALL carry a field whose whole value is the observation's
Dolt revision or its capture instant." [Inferred] A row's `createdAt` or
`updatedAt` read from Dolt could equal the capture instant if formats match
(low probability, but then a true fact is a falsifier). A prefixed or
truncated repeat of the revision passes. Q3 discloses the narrowing honestly
("A future block could add a new header field and repeat it per row"), so the
scope is honest. Suggest naming the coincidence case in the falsifier (a
value read from the source is not a restatement) or limiting the
capture-instant arm to fields not read from the source.

**Finding 11 — SHALL bullets in an event-response requirement: still one form, but the bullet reads unconditioned** (note) [POC]

[Inferred] The new obligations are properties of the observation produced in
response to the requirement's own trigger, and the sweep is bounded by that
response's entries, so the requirement stays event-response under CC-SPEC-4.
It does not turn into a separate prohibition. As written, though, "The
observation SHALL …" and "No inventory entry SHALL …" stand outside the WHEN
sentence. Suggest anchoring them: "The observation so produced SHALL …". I
judge POC-REQ-001's inclusion to belong: S6-F2 names `codeStructure` as one
of the three shapes, and L11-F4's figure counts the file rows.

**Finding 12 — the bead's unrendered-fraction assertion (S6-M3) is not accounted for** (note) [both]

The bead's WHAT includes "assert in a test what fraction of workItems and
codeStructure the human page renders" (S6-M3). Neither package says it was
dropped, deferred, or needs no spec change (S6-M3's own prerequisite is
"none"). Suggest one line in the PWB or POC delta saying where it goes, so
criterion 1's "rulings are carried" covers the whole bead.

## Criteria summary

1. Rulings carried: yes. The stale dov.10.1 ordering is named (POC delta) and
   the block-to-anchor link is stated as already met. S6-M3 is unaccounted
   for (F12).
2. One category per change: yes. Each patches one specification.
3. RFC7-3/7-4 not crossed: yes, with the residues in F3.
4. Predicates checkable: no for "resolves" (F1, F2) and for the POC
   "nowhere else" (F8); partly for "one shape" (F5, F7).
5. Specification bar: the form stays one (F11); oracle defects as in criterion 4.
6. Signed bytes: verified independently.
7. Honest claims: headline figures reproduce from the record; some
   [Observed] claims have no record (F9).
8. Mechanics: all pass; selftest mutants fail on their own predicates, with
   the gaps in F6.
9. Plain language: both packages restate cleanly.
