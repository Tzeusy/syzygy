# R-POLARIS-BASE-READABILITY-SUCCESSOR-2 — Polaris generator base readability successor confirmation
Verdict: CONFIRM WITH EXCEPTIONS
Manifest-file SHA-256: 6ab71229125b7fe6c718978185932395dd909bfbe60bfd86972c1d34f6effa59
Reviewed commit: 6c6ff295b17146f3e40c116e0ede15d9cb6235a7

Subject: `.syzygy/governance/contracts/candidates/polaris-generator-base-readability-successor/`
(SUCCESSOR.json, SUCCESSOR-MANIFEST.txt, OWNER-DECISION-PACKET.md,
`proposed/openspec/changes/polaris-manifesto-generation/{proposal,design}.md.proposed`).
Below, `PKG/` is the package; `proposal.proposed` / `design.proposed` are the
proposed files; `proposal.md` / `design.md` are the current bound files in
`openspec/changes/polaris-manifesto-generation/` at the reviewed commit.
Prior round: `docs/reviews/R-POLARIS-BASE-READABILITY-SUCCESSOR-1-RAW.md` (REVISE, M1, M2, N1-N8).

## Mechanical checks (bar item 6)

- [Observed] `python3 scripts/readability_successor.py --all --check` exits 0
  and prints `PASS candidate-unperformed: .syzygy/governance/contracts/candidates/polaris-generator-base-readability-successor`
  (3 packages checked).
- [Observed] `sha256sum PKG/SUCCESSOR-MANIFEST.txt` gives
  `6ab71229125b7fe6c718978185932395dd909bfbe60bfd86972c1d34f6effa59`. That matches
  the argument in the packet phrase (PKG/OWNER-DECISION-PACKET.md:20).
- [Observed] A Python script hashed every row. The manifest has 23 non-comment
  rows, and the packet says 23 at lines 24 and 51. 21 rows equal sha256 of the
  current file. The design.md row `19d4c147…` equals sha256 of `design.md.proposed`.
  The proposal.md row `ef7bc2a3…` equals sha256 of `proposal.md.proposed`.
  The 23 `predecessor` digests in SUCCESSOR.json are the current digests; for
  the two restyled files that is `236f9e01…` / `67970484…`, and those equal the
  `/sources` rows of the 2026-09-12 offer.
- [Observed] Links (bar item 4): I installed both proposed files in a scratch
  clone and ran `python3 scripts/check_governance.py`, before and after. The
  only differences are CG-1a going from 500 to 502 links examined and CG-1b from
  7115 to 7116 references, both with 0 findings. Both runs end 31 OK, 21 WARN,
  0 FAIL. From `openspec/changes/polaris-manifesto-generation/`, each of the
  following exists: `../../../.syzygy/governance/decisions/POLARIS-GENERATOR-SPECIFICATION-ADOPTION-ACT.md`,
  `../../../.syzygy/governance/decisions/POLARIS-GENERATOR-APPLICABILITY-ACT.md`,
  `../polaris-manifesto-understanding-amendment/`, and, from the repository root,
  `docs/design/POLARIS-GENERATOR-HOST-OVERLAP.md`, `docs/polaris-generation/README.md`
  and `docs/design/POLARIS-GENERATOR-DELIVERY.md`.
- [Observed] The coexistence table is byte-identical: design.md:150-158 equals
  design.proposed:174-182 (Python list comparison, True).

## Round-1 blocking findings

### M1 — repaired
PKG/OWNER-DECISION-PACKET.md:38-42 now reads: "**No new check failure.**
`scripts/polaris_generator_approval.py --check` compares the 2026-09-12
approval offer with today's bytes. It already fails today, on
governing-baseline drift in `05-CONTRACT-INDEX.yaml`, and is not in the
battery. After sign-off the two restyled files also differ from the offer,
which is correct: the offer records what was approved then."

- [Observed] The offer argument is `docs/evidence/polaris-generator-approval-offer-2026-09-12.json`,
  sha256 `48216b06…29dd`. It is the argument named in
  POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md:25.
- [Observed] At the reviewed commit,
  `python3 scripts/polaris_generator_approval.py --check --offer <offer> --argument 48216b06…29dd`
  prints `governing baseline drift: .syzygy/governance/contracts/candidates/05-CONTRACT-INDEX.yaml`
  and exits 1.
- [Observed] With both proposed files installed, the same command prints
  `source digest mismatch: openspec/changes/polaris-manifesto-generation/design.md`.
  "Also differ" is literally true. The packet no longer says the check reports
  both files, and no longer implies that it passes today.
- [Observed] `grep -rnF polaris_generator_approval PROJECT-STATUS.md .github`
  returns 0 hits, so "not in the battery" holds.

### M2 — repaired
design.proposed:3-5 now reads: "**The generator separates acquisition,
inference and presentation, records every run against one authoritative
lifecycle, and never replaces authored presentation merely because the source
or a model improved.**" This carries the qualifier from design.md:107-108 and
agrees with design.proposed:127-131.

## Round-1 notes: disposition observed

- N1 (one act vs three records): **addressed.** proposal.proposed:3-7 now reads
  "one owner phrase adopted this specification, decided its scoped
  applicability and authorized its implementation, recorded in
  [`POLARIS-GENERATOR-SPECIFICATION-ADOPTION-ACT.md`] … and its two sibling
  records." [Observed] The SPECIFICATION-ADOPTION, APPLICABILITY and
  IMPLEMENTATION-AUTHORIZATION act records all carry the same instant
  2026-09-12T09:27:55Z and the same transaction phrase
  `ADOPT POLARIS GENERATOR SPECIFICATION, SCOPED APPLICABILITY AND IMPLEMENTATION`.
- N2 (the two added requirements): **addressed.** proposal.proposed:8-9 reads
  "later replaced seven of its requirements and added two". [Observed]
  POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md, Scope, lists "002, 004,
  006, 009, 012, 014 and 019 take their full amended clauses …; 030 and 031 are
  added."
- N3 (the overlap review narrowed from existing capability behavior to PWB):
  **not addressed.** It is carried below as N4 and is non-blocking.
- N4 (contract coverage: "must pass" vs "subject to"): **addressed.**
  design.proposed:55-57 reads "must pass the contract-coverage review before
  sign-off; this design does not record that review's outcome".
- N5 ("must" rewritten as indicative): **addressed.** proposal.proposed:68 has
  "must use the same implementation". design.proposed:149-150 has "The task
  must explain … not merely extract headings", with the grammar slip fixed.
  design.proposed:184 has "must not force".
- N6 (the lead sentence reads as a shipped capability): **not addressed.** It is
  carried below as N5.
- N7 (the coexistence amendment rule widened slightly): unchanged
  (design.proposed:188-189). It stays acceptable, because it removes no
  protection a reader relied on.
- N8: no action was needed.

## Full-bar re-check

- Bar item 1 (nothing dropped): I compared both files sentence by sentence
  against the current bytes.
  - [Observed] Everything the current files say maps to a counterpart.
  - [Observed] The only removals are true only before adoption:
    - "Candidate — binds nothing" (proposal.md:3; design.md:1 "— candidate")
    - "proposed design" (design.md:3)
    - "No such judgment is effective yet" (proposal.md:78)
    - "candidate review guidance" (design.md:142)
    - "the current implementation proposal" (design.md:13) → "the implementation proposal"
    - the implementation authorization among the pending separate acts (proposal.md:3-4)
  - [Observed] Protected effect host moved out from under Risks (design.md:182
    `###`) to its own `##` section, now placed before Risks
    (design.proposed:191). Its three claims are all kept.
- Bar item 2 (no invention, same modality): [Observed] The new sentences check
  out against the act records:
  - "the owner's applicability act … binds them" (proposal.proposed:85-88).
    POLARIS-GENERATOR-APPLICABILITY-ACT.md: "Adopt GNA-1, GNA-2 and GNA-3 only
    within APPLICABILITY-DECISIONS.md's exact scope".
  - "authorized its implementation" (proposal.proposed:4).
    POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md: "Authorize the full
    EXECUTION-PHASES.md implementation goal".
  - "Project admission, provider consent, authorship and release remain
    separate acts" (proposal.proposed:9-10). The implementation act: "Real-project
    reads, provider egress and destination writes remain separately admitted".

  No other modality shift remains; see N3 and N4 for the residual edge cases.
- Bar item 3 (the banner is true): [Observed] The proposal banner is true
  against all four act records named above. design.proposed carries no status
  banner, only "This document is design: it is not an accepted topology, an
  implementation plan or a grant of effect authority". [Observed] The offer
  gives design.md the role `specification`, so that act adopted it; the
  sentence does not deny that, and it is true as written.
- Bar item 5 (the packet is true): all statements hold except as noted in N2
  and N6.
  - [Observed] "every REQ-polaris-generation requirement, scenario and warrant
    stays byte-identical": the spec.md row equals the current bytes.
  - [Observed] "Review: pending": all SUCCESSOR.json pins are null.
  - [Observed] "The tool refuses to record until a fresh review confirms the
    manifest digest": `validate_pins()` in readability_successor.py:156-174
    raises "unpinned" and requires the raw to carry exactly one CONFIRM verdict
    and exactly one binding.
  - [Observed] "`--record` writes the act record and its section in the
    acceptance record, then installs the two restyled files. Its `--check`
    then verifies all 23 files against their rows": `record()` at
    readability_successor.py:263-283 opens the act with "x", appends the block
    to ACCEPTANCE-ACT-RECORD.md, writes the proposed bytes, then re-runs
    `check()`, which compares every manifest subject with its row.

## Blocking findings

None.

## Non-blocking notes

### N1 — Unwrapped overlong line and an awkward phrase in the design opening
design.proposed:5 is 184 columns wide, while every other line is wrapped at
about 78. It reads: "presentation merely because the source or a model
improved.** This document is design: it is not an accepted topology, an". The
M2 repair lengthened the thesis without re-wrapping it. "This document is
design" also reads oddly; "This is a design document, not …" would be
clearer. The change is cosmetic and changes no meaning.

### N2 — Packet status line ignores the understanding amendment
PKG/OWNER-DECISION-PACKET.md:4-5 says: "Until then the generator
specification stays exactly as `POLARIS-GENERATOR-SPECIFICATION-ADOPTION-ACT.md`
bound it." [Observed] On 2026-09-13, POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md
superseded seven requirement blocks of that subject and added two. The
sentence is true for proposal.md and design.md, which are this package's
subject, but not for "the generator specification" as a whole. Line 12 of the
packet and proposal.proposed:7-9 both describe the amendment, so the risk of
misleading a reader is low. Suggested wording: "the generator proposal and
design stay exactly as … bound them".

### N3 — Host integration phrasing shifts slightly
proposal.md:37-40: "Host authentication and credential handling require
explicit integration for the new data-bearing and mutating generation
operations". proposal.proposed:45-49: "**Host integration is explicit.** The
new data-bearing and mutating generation operations need their own
authentication and credential handling". [Inferred] "Their own" leans toward
separate handling, where the current text says integration. This matches
EFFECT-HOST-DESIGN.md's separate credential stores, which proposal.proposed:79-81
also states, so no reader-relied claim changes. Noted for precision only.

### N4 — (carried from round-1 N3) Overlap-review obligation narrowed to PWB
proposal.md:40-42 says "The overlap/impact review must identify any corresponding
amendment to existing capability behavior before sign-off". proposal.proposed:50-51
says "Where integration changes adopted PWB behavior, that change needs its own
signed amendment." The review step was discharged at adoption, so dropping it
is fine. The general rule survives at proposal.proposed:83-84 ("A departure
that changes an adopted outcome still needs its signed amendment"). The
narrowing is non-blocking.

### N5 — (carried from round-1 N6) The lead sentence reads as a runtime claim
proposal.proposed:12-13: "**Polaris generates a project's manifesto: …**".
[Observed] The implementation act "does not claim … implementation completion".
[Inferred] Present tense here is the owner's directed style and reads as a
capability statement. It is acceptable.

### N6 — The packet names `--check` without its required arguments
PKG/OWNER-DECISION-PACKET.md:38: "`scripts/polaris_generator_approval.py --check`
compares the 2026-09-12 approval offer with today's bytes." [Observed] Run as
written, it exits 2 with "--offer is required". It needs
`--offer docs/evidence/polaris-generator-approval-offer-2026-09-12.json --argument 48216b06…`.
With those arguments the behavior the packet describes is exactly what I
observed. Naming the offer path would let the owner reproduce the claim
directly. Separately, the packet says "why, what changes, scope and
applicability as shallow lists" (line 31), but "Why" remains a prose
paragraph (proposal.proposed:17-20). Both are trivial.
