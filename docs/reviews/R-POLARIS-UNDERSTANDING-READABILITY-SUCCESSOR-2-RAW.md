# R-POLARIS-UNDERSTANDING-READABILITY-SUCCESSOR-2 — Polaris understanding readability successor confirmation
Verdict: CONFIRM WITH EXCEPTIONS
Manifest-file SHA-256: 2bd0892a2d6b7ca09cfc06dd4325a1bc3cd3706852a08963836b17bd2c5d3b98
Reviewed commit: 3ed9131b951b95f8ac7b68ac9f510dd5c9ef2385

Package: `.syzygy/governance/contracts/candidates/polaris-understanding-readability-successor/`
(abbreviated PKG below). Proposed files are cited as `proposal.md.proposed` and
`design.md.proposed` under `PKG/proposed/openspec/changes/polaris-manifesto-understanding-amendment/`.
The bar is the owner direction of 2026-09-27 (readability, no strict semantic equivalence;
committed docs present-tense) plus bar items 1-6 from the brief.

## Review-1 findings

- **M1 (packet said all six design sections became trees): repaired.** [Observed]
  PKG/OWNER-DECISION-PACKET.md:32-35 now reads "and the placement section becomes a short
  tree. The other five sections are unchanged." A `diff` of `design.md` lines 9-end against
  `design.md.proposed` lines 11-end shows the only difference is the
  "Placement and compatibility" bullet list (current 118-125, proposed 120-131); Product
  intent, Research and editorial loop, Record ownership and interfaces, Clarification and
  change, and Evaluation contract are byte-identical. (See N1 for the word "tree".)
- **M2 (Impact dropped "must"): repaired.** [Observed] `proposal.md.proposed:96-97`:
  "prompt, validator and renderer interfaces must consume one supported understanding",
  matching current `proposal.md:77-78`.

## Full-bar re-check

1. **No dropped content.** [Observed] Clause-by-clause comparison of both files. Every
   proposal claim in Why, What Changes, Capabilities, Amendment relation, Scope and Impact is
   present. Two things were dropped, and both were only true before adoption: the candidate
   paragraph (`proposal.md:3-5`), which the banner replaces, and "Before adoption, review
   the amendment's exact behavioral and source-class impacts." (`proposal.md:81`). In design,
   the only dropped text is "Candidate design accompanying the formal amendment."
   (`design.md:3`); the rest of that paragraph is kept at `design.md.proposed:5-7`. The
   placement bullets keep every item, including "no new queue and no silent PWB truth-store
   split" and "under the existing protected-host and audit requirements".
2. **No invented claim or modality shift.** [Observed] The Impact "must" is restored. The
   verb changes are equivalent: require→need, retain→keep, "do not create"→"create no".
   The new thesis sentences (`proposal.md.proposed:11-13`, `design.md.proposed:3-5`)
   summarize the body; see N2 and N3.
3. **Banner true.** [Observed] `POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md` has
   "Act instant: 2026-09-13T01:58:26Z". It adopts the manifest's exact bytes, and its
   instruction refers to "the reviewed formal amendment". `POLARIS-TREE-FORM-AMENDMENT-ADOPTION.md`
   says that on 2026-09-28 the owner adopted "the amended REQ-polaris-generation-004 in the
   understanding amendment's spec". The banner at `proposal.md.proposed:3-9` matches both records.
4. **Links resolve.** [Observed] From the install directory
   `openspec/changes/polaris-manifesto-understanding-amendment/`, the path
   `../../../.syzygy/governance/decisions/` resolves to the repository decisions directory.
   Both named files exist there. Design has no links.
5. **Packet facts.** [Observed] The following checked out:
   - The specification, coverage, synthesis map, tasks and `.openspec.yaml` rows equal the
     current bytes and the SUCCESSOR.json predecessor digests.
   - The manifest has eight rows.
   - The argument is 2bd0892a…b98, which is the sha256 of SUCCESSOR-MANIFEST.txt.
   - `--record` writes the act file and the aggregate section, then installs the files and
     reads them back (`scripts/readability_successor.py:263-283`).
   - Recording is refused while `pins` is null ("unpinned").

   [Observed] `record_polaris_understanding_adoption.py --check` reconciles against the
   review-bound bytes and today reports "8 historical rows, 7 unchanged". This supports the
   packet's claim that installing the restyle would fail that check
   (OWNER-DECISION-PACKET.md:40-42). [Inferred] I did not execute the failure.
   [Unknown] The follow-up recorder change (lines 42-45) is described as future work, and I
   did not verify it.
6. **Mechanical checks.** [Observed]
   - `python3 scripts/readability_successor.py --all --check` gives PASS candidate-unperformed
     for all three packages and exits 0.
   - The script computes the manifest sha256 as 2bd0892a2d6b7ca09cfc06dd4325a1bc3cd3706852a08963836b17bd2c5d3b98,
     which equals the packet phrase at OWNER-DECISION-PACKET.md:20.
   - The design.md and proposal.md rows equal the sha256 of their `.proposed` bytes. The
     other six rows equal the current files.
   - `check_governance.py` reports 31 OK, 21 WARN, 0 FAIL.

## Blocking findings

None.

## Notes

- **N1** OWNER-DECISION-PACKET.md:34-35: "and the placement section becomes a short tree."
  The placement section was already a flat four-item bullet list (`design.md:118-125`). The
  restyle adds bold labels and rewraps the lines; it adds no nesting. "Becomes a short tree"
  overstates a change of form. It misdescribes no content, so it is not blocking.
- **N2** `proposal.md.proposed:56`: "**Never archive or sync this as an unrelated competing
  change.**" The current text at `proposal.md:46` is "Do not archive/sync this as an
  unrelated competing change." The prohibition is equivalent, and bolding adds emphasis
  only.
- **N3** `proposal.md.proposed:11-12` ("asks the owner the questions that matter, and only
  then argues the project's purpose") and `design.md.proposed:3-4` ("it investigates, asks,
  argues") simplify the conditional loop: the loop asks only on a consequential unknown, and
  partial findings may be exposed while questions remain. The body keeps both
  qualifications verbatim (`proposal.md.proposed:73-78`; the mermaid loop in design), so no
  obligation changes.
