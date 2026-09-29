# R-POLARIS-BASE-READABILITY-SUCCESSOR-1 — Polaris generator base readability successor review
Verdict: REVISE
Manifest-file SHA-256: 13d45770e2a8202892ec319b9e2ba3ec4ab127d587bf86d697e4e60efdc952d3
Reviewed commit: a68b193797fdbf9ebe868efac040d871284e616b

Subject: `.syzygy/governance/contracts/candidates/polaris-generator-base-readability-successor/`
(SUCCESSOR.json, SUCCESSOR-MANIFEST.txt, OWNER-DECISION-PACKET.md,
`proposed/openspec/changes/polaris-manifesto-generation/{proposal,design}.md.proposed`).
Paths below abbreviate the package as `PKG/` and the proposed files as
`proposal.proposed` / `design.proposed`; old files are
`openspec/changes/polaris-manifesto-generation/{proposal,design}.md` at the
reviewed commit.

## Mechanical checks

- [Observed] `python3 scripts/readability_successor.py --all --check` exits 0:
  `PASS candidate-unperformed: .../polaris-generator-base-readability-successor`
  (3 packages checked).
- [Observed] `sha256sum PKG/SUCCESSOR-MANIFEST.txt` =
  `13d45770e2a8202892ec319b9e2ba3ec4ab127d587bf86d697e4e60efdc952d3`, equal to
  the argument in the packet phrase (PKG/OWNER-DECISION-PACKET.md:20).
- [Observed] Manifest has 23 non-comment rows (packet says 23: lines 24, 50).
  Scripted comparison: 21 rows equal the sha256 of the current file; the two
  differing rows equal the proposed bytes — design.md row `baf99f77…` =
  sha256 of `design.md.proposed`, proposal.md row `f422bd22…` = sha256 of
  `proposal.md.proposed`. The 23 predecessor digests in SUCCESSOR.json equal
  the current bytes.
- [Observed] Links: installed the two proposed files into a scratch clone and
  ran `python3 scripts/check_governance.py`. Only difference from the
  un-installed run: CG-1a 497→499 links examined, CG-1b 7091→7092 references,
  both 0 findings; totals unchanged (31 OK, 21 WARN, 0 FAIL). Both new
  Markdown links (`../../../.syzygy/governance/decisions/POLARIS-GENERATOR-SPECIFICATION-ADOPTION-ACT.md`,
  `../../../.syzygy/governance/decisions/POLARIS-GENERATOR-APPLICABILITY-ACT.md`)
  and the code span `../polaris-manifesto-understanding-amendment/` resolve
  from the installed location. `docs/design/POLARIS-GENERATOR-HOST-OVERLAP.md`
  exists.
- [Observed] Readers of the change via
  `git grep -n polaris-manifesto-generation -- scripts .github apps packages`
  (excluding readability_successor.py): `build_polaris_edit_repair_deletion_scenario.py:47`
  and `record_polaris_understanding_adoption.py:199` read only
  `specs/polaris-generation/spec.md` (unchanged); `count_polaris_effective_scenarios.py:19`
  is a docstring; `polaris_generator_approval.py:21,23` is the one reader
  that hashes proposal.md/design.md (see M1). The current digests of
  proposal.md/design.md appear otherwise only in `docs/evidence/polaris-generator-*-2026-09-12.json`
  records, of which only the approval offer and review subject are read by
  scripts (`polaris_generator_approval.py:32-33`; `check_governance.py:2118`
  reads the offer only as an act subject, whose bytes do not change).
  `polaris_generator_approval.py` appears in neither `PROJECT-STATUS.md` nor
  `.github/` (grep -F, 0 hits), so "It is not in the battery" is true.

## Blocking findings

### M1 — Packet's side-effect sentence misdescribes `polaris_generator_approval.py --check`

PKG/OWNER-DECISION-PACKET.md:38-41:
> "**One side effect.** `scripts/polaris_generator_approval.py --check`
> compares the 2026-09-12 approval offer with today's bytes. After sign-off
> it reports the two restyled files as drifted, which is correct: the offer
> records what was approved then. It is not in the battery."

[Observed] At the reviewed commit, before any sign-off, the check already
fails:
`python3 scripts/polaris_generator_approval.py --check --offer docs/evidence/polaris-generator-approval-offer-2026-09-12.json --argument <sha of offer>`
→ `governing baseline drift: .syzygy/governance/contracts/candidates/05-CONTRACT-INDEX.yaml`, exit 1.

[Observed] With the two proposed files installed in a scratch clone, the same
command prints `source digest mismatch: openspec/changes/polaris-manifesto-generation/design.md`,
exit 1. `sources()` (`polaris_generator_approval.py:116-127`) raises on the
first mismatching row, so it names one file, not "the two restyled files".

So the sentence is false twice: the check doesn't pass today (sign-off only
changes the first failure it reports from governing-baseline drift to
source drift), and it doesn't report both files. The packet leaves the
owner believing the act brings in a new failure in a check that passes
today. Repair: say the check already fails at this commit on
governing-baseline drift (name the file), and that after sign-off it stops at
the first drifted source, design.md.

### M2 — Design thesis turns a qualified non-replacement into an absolute

design.proposed:3-5:
> "**The generator separates acquisition, inference and presentation, records
> every run against one authoritative lifecycle, and never replaces authored
> presentation.**"

Old text, the source of the claim (design.md:107-116):
> "Regeneration always produces a separate editorial candidate. It does not replace
> human-curated composition merely because source content or a model improved.
> ... the new candidate ... needs its own applicable reviews and per-block authorship
> act. Finalization is conditionally committed ... before any authored write."

[Observed] The old text rules out replacement *merely because* source or model
improved, and it keeps an authored-write path gated by a per-block
authorship act. The restyle's own body keeps both (design.proposed:127-137,
"never replaces human-curated composition merely because…" and "**Authored
writes.**"). The thesis drops the qualifier and says "never replaces". That
is a stronger claim than the old text or its own children support. Under
the tree-form standard the proposed files follow (a parent truly summarises
its children), a reader who stops at the thesis gets a false account.
Repair, for example: "…and never replaces authored presentation without a
human authorship act" or "…never replaces authored presentation merely
because a source or model improved".

## Non-blocking notes

### N1 — "in one act" versus three act records
proposal.proposed:3-5: "the owner adopted this specification, with scoped
applicability and implementation, in one act on 2026-09-12, recorded in
[`POLARIS-GENERATOR-SPECIFICATION-ADOPTION-ACT.md`]…". [Observed] One owner
phrase (`ADOPT POLARIS GENERATOR SPECIFICATION, SCOPED APPLICABILITY AND
IMPLEMENTATION: 48216b06…`) produced three act records dated 2026-09-12
(SPECIFICATION-ADOPTION, APPLICABILITY, IMPLEMENTATION-AUTHORIZATION;
`check_governance.py:2120-2123`, ACCEPTANCE-ACT-RECORD.md lines 365/413/461).
"In one act" is defensible as one transaction. But the implementation part
was *authorized*, not adopted, and the banner links only the adoption
record. Consider "in one transaction … recorded in the specification-adoption,
applicability and implementation-authorization acts". SUCCESSOR.json's
`supersedes` string already treats them as separate acts ("the applicability
and implementation acts keep their own scopes").

### N2 — Amendment summary omits the two added requirements
proposal.proposed:6-7: "The understanding amendment … later replaced seven of
its requirements." [Observed] POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md:28-37
confirms seven superseded blocks (002, 004, 006, 009, 012, 014, 019). It also
adds 030 and 031. The sentence is true but incomplete. The old text had no
such sentence, so nothing is dropped.

### N3 — Modified-capabilities obligation narrowed from "existing capability behavior" to "adopted PWB behavior"
Old proposal.md:40-42: "The overlap/impact review must identify any corresponding
amendment to existing capability behavior before sign-off; the earlier blanket
claim of no modified capability is not established." New proposal.proposed:48-49:
"**No blanket "nothing modified" claim.** Where integration changes adopted
PWB behavior, that change needs its own signed amendment." [Inferred] The
pre-sign-off review step is discharged by the 2026-09-12 act, so it is
correct to drop it. The scope moves from "existing capability" to "PWB".
The general rule survives at proposal.proposed:81-82 ("A departure that
changes an adopted outcome still needs its signed amendment"), so no reader
loses the obligation.

### N4 — Contract-coverage "must pass … before sign-off" softened to "subject to"
Old design.md:46-48: "Their schema and adapter registrations must pass the
contract-coverage review before sign-off." New design.proposed:55-57: "…are
subject to contract-coverage review; this design does not record that
review's outcome." The Risks bullet keeps the sign-off obligation
(design.proposed:218-220, "are sign-off obligations. This design makes no
claim that those gates have passed"), so the obligation is not lost. The two
sentences now say it with different strength. Aligning them would help.

### N5 — "must" rewritten as indicative present
proposal.md:59-60 "independently admitted projects must use the same
implementation" → proposal.proposed:65-66 "use the same implementation";
design.md:126 "The synthesis task must explain" → design.proposed:149-150 "The
task explains the project's distinctive argument, not merely extracting
headings…" (the grammar also slips: "explains …, not merely extracting");
design.md:160 "must not force" → design.proposed:184 "never forces". [Inferred]
Under the owner's present-tense direction a declarative design sentence reads
as normative, so none of these counts as a weakening. The design.proposed:149
sentence would read better as "explains …, rather than merely extracting…".

### N6 — Proposal lead sentence reads as a shipped capability
proposal.proposed:10-11: "**Polaris generates a project's manifesto: …**".
[Observed] The implementation-authorization act says it "does not claim …
implementation completion", and the spec makes completion depend on
two-project evidence. [Inferred] A capability statement in present tense is
conventional, and the owner asked for present-tense documents, so this is
acceptable. A reader could still take it as a runtime claim.

### N7 — Coexistence amendment rule broadened slightly
Old design.md:162-164: "If integration needs to change any PWB behavior above,
that becomes an explicit amendment…"; new design.proposed:188-189: "**Changing
PWB behavior** is an explicit amendment…". Dropping "above" broadens the rule
from the tabled rows to all PWB behavior. This matches proposal.proposed:48-49
and removes no reader protection.

### N8 — Structural moves checked, no loss
[Observed] "Protected effect host" was a `###` under Risks (design.md:182) and
is now its own `##` section (design.proposed:191). The coexistence table is
byte-identical (design.md:150-158 = design.proposed:174-182). Every other
sentence in both files maps to a counterpart. Checked by line-by-line
comparison, all old sentences enumerated. Pre-adoption phrases were removed
correctly: "Candidate — binds nothing", "No such judgment is effective yet"
(now bound by POLARIS-GENERATOR-APPLICABILITY-ACT.md, which adopts GNA-1…3
"only within APPLICABILITY-DECISIONS.md's exact scope"), "proposed design",
"candidate review guidance". The implementation-authorization item was
rightly dropped from the list of pending separate acts.

## Packet accuracy (other sentences)

- [Observed] "The specification, tasks, every contract document and the other
  bound sources are unchanged": the 21 unchanged manifest rows equal their
  current bytes, including `specs/polaris-generation/spec.md`, `tasks.md`,
  `.openspec.yaml` and the two `docs/design/` files.
- [Observed] "The understanding amendment's overlay is untouched; it has its
  own successor package": no understanding-amendment path is in the manifest,
  and `polaris-understanding-readability-successor` exists and passes
  `--check`.
- [Inferred] "`--record` writes the act record … then installs the two restyled
  files. Its `--check` then verifies all 23 files against their rows": this is
  consistent with `readability_successor.py` docstring lines 23-24 and
  `check()`/`record()` (lines 233-282). The tool itself was reviewed in
  another round and not re-verified here.
- [Observed] "Review: pending": true; SUCCESSOR.json pins are null.
