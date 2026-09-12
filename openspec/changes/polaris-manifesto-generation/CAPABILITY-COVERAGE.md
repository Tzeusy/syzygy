# Candidate capability coverage

Informative mapping from the reviewed product contract MG-01..MG-17 to this
first formal requirement set. It is not a CC-SPEC-8 or CC-SPEC-11 confirmation.

| Product criterion | Draft requirement IDs | Implementation evidence |
|---|---|---|
| MG-01 | REQ-polaris-generation-001, REQ-polaris-generation-015 | Not yet established for generator scope |
| MG-02 | REQ-polaris-generation-002, REQ-polaris-generation-004, REQ-polaris-generation-006, REQ-polaris-generation-014 | Not yet established for generator scope |
| MG-03 | REQ-polaris-generation-002, REQ-polaris-generation-006 | Not yet established for generator scope |
| MG-04 | REQ-polaris-generation-002, REQ-polaris-generation-003, REQ-polaris-generation-004 | Not yet established for generator scope |
| MG-05 | REQ-polaris-generation-003, REQ-polaris-generation-004, REQ-polaris-generation-006 | Not yet established for generator scope |
| MG-06 | REQ-polaris-generation-001 | Not yet established for generator scope |
| MG-07 | REQ-polaris-generation-001, REQ-polaris-generation-012 | Not yet established for generator scope |
| MG-08 | REQ-polaris-generation-005, REQ-polaris-generation-006 | Not yet established for generator scope |
| MG-09 | REQ-polaris-generation-005, REQ-polaris-generation-007 | Not yet established for generator scope |
| MG-10 | REQ-polaris-generation-008, REQ-polaris-generation-013 | Not yet established for generator scope |
| MG-11 | REQ-polaris-generation-006, REQ-polaris-generation-009 | Not yet established for generator scope |
| MG-12 | REQ-polaris-generation-003, REQ-polaris-generation-013 | Not yet established for generator scope |
| MG-13 | REQ-polaris-generation-010, REQ-polaris-generation-015 | Not yet established for generator scope |
| MG-14 | REQ-polaris-generation-004, REQ-polaris-generation-012, REQ-polaris-generation-014 | Not yet established for generator scope |
| MG-15 | REQ-polaris-generation-003, REQ-polaris-generation-004, REQ-polaris-generation-012 | Not yet established for generator scope |
| MG-16 | REQ-polaris-generation-011, REQ-polaris-generation-016 | Not yet established for generator scope |
| MG-17 | REQ-polaris-generation-009, REQ-polaris-generation-014 | Not yet established for generator scope |

Additional accepted-contract behaviors: presentation-profile admission is covered
by requirement 015; governed authored-artifact ownership/write discipline by 016.

Adapter admission/provenance and complete run-envelope behavior are explicitly
covered in draft requirements 017/018; these support MG-01/06/08/10/12 without
claiming implementation evidence.

Versioned interchange and reference integrity are covered in draft requirement
019, supporting MG-01/04/05/12/15. Executable validation remains unimplemented.

Guided request preparation and materialization are covered in draft requirement
020, supporting MG-01/08/09/10 without assuming preassembled work records.

Caller admission and audit/revocation are covered in draft requirements 021/022,
supporting MG-06/07/09/10/13; current host helpers are not complete evidence.

Primary entry/discoverability and formal walkthrough/freeze discipline are
covered in draft requirements 023/024, supporting MG-02/03/14/16/17.

Source-policy and exclusion precision is covered in draft requirement 025,
supporting MG-01/04/06/07 while keeping adopted project policy boundaries intact.

Shared navigation and full answer/aggregate semantics are covered in draft
requirements 026/027, supporting MG-02/05/12/14/15 without a second fact store.

Work-state/capture/chain precision is covered in draft requirements 028/029,
supporting MG-08/09/10/12 with the no-signal derivation explicitly unresolved.

Before sign-off, independently check this mapping against the full owner objective
and perform the applicable-contract sweep. Existing Butlers rendering evidence
does not establish the generator's synthesis, recovery or cross-project outcome.

## Phase and work projection disposition

EXECUTION-PHASES.md makes the full owner flow and real-project proof mandatory
while separating pure mechanics from live work/effect consumers. Requirements
028/029 apply to the explicit integration consumers; unsupported mapping cases
refuse the affected live admission and do not block unrelated mechanics or
become claimed support. This is a candidate behavior/phase disposition, not
an owner-bound N/A or an accepted-contract predicate amendment.
