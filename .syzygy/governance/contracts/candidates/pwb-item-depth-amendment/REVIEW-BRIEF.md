> **Candidate — binds nothing.** Review the exact proposed package. Do not
> interpret the candidate, manifest, commit or PR as an owner act or as
> implementation authority.

# Review brief — PWB item depth

Review in fresh context with only this package, its exact commit, the current
signed PWB package, the governing references below and these criteria. The
proposed bytes are the patches under `proposed/`; current `openspec/**` bytes
must remain unchanged.

## Governing material

- P-81 Q5 in
  `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`;
- the M14 funnel Q5 and evidence record;
- VIS-1, VIS-2, VIS-3, VIS-4, VIS-7;
- CC-REV-1/2/4/6/7, CC-SPEC-1…11, CC-IMPACT-1…7;
- RFC7-12…19, RFC7-26/27, RFC7-29, RFC7-33/34;
- PWB-REQ-011, PWB-REQ-014, current/proposed PWB-REQ-015, PWB-REQ-016 and
  PWB-REQ-020; and
- the 2026-09-05 behavior act and implementation-continuation boundary.

## Acceptance criteria

1. **Scope.** The delta changes PWB-REQ-015's subject from capability-only
   detail to the complete declared catalog-item population and nothing broader.
   Try to construct a reading that invents a capability or item.
2. **Bands.** Exactly argument, contract and reality remain, in that order and
   with one existing authority class per block. No fourth class or relaxed
   band obligation is introduced.
3. **Declared mapping only.** Test an item with no mapping, two mappings, a
   same-label requirement and generated prose. Only one captured declared
   relation may yield current intent; every other case must show honest absence.
4. **Exact intent.** Requirement, scenario, doctrine and non-goal material is
   verbatim-reachable from its owner, never stored or paraphrased in normative
   position.
5. **Identity and parity.** Every declared item has exactly one detail; item
   identity and its complete epistemic tuple survive catalog, detail and exact
   source in both channels. URL, label, path and coordinate are not identity.
6. **Proposals and reality.** Current intent remains operative; proposals are
   adjacent, separate, non-anchorable and non-status-bearing; reality uses only
   the one shared model/evaluation.
7. **Neighboring authority.** Attempt to show that PWB-REQ-011/014/016/020 or a
   cited RFC becomes false. Any successful counterexample is blocking and must
   route to the owner rather than being silently absorbed here.
8. **Package mechanics.** Run builder `--check`, `--selftest` and `--diff`.
   Re-derive all eleven rows and the manifest-file SHA-256; verify five patch
   targets, no current signed-byte edit and the stated sibling denominator.
9. **Overlap.** Fetch then-current open PWB PR patches, including PR #121 and
   PR #124 if still open, and test this spec patch before/after each. Confirm
   `.30` remains separate and explicitly leaves PWB-REQ-015 downstream.
10. **Owner boundary.** The packet's phrase is visibly not offered, no chain
    position is asserted, and adoption would still authorize no implementation.
11. **Comprehension.** A reader with no authoring context can restate the
    population, three bands, unmapped-item behavior, overlap and two later owner
    gates: amendment act, then fresh implementation authorization.

The raw review must start with the exact reviewed commit, the exact
manifest-file SHA-256, one verdict from `CONFIRM`, `CONFIRM WITH EXCEPTIONS`,
`REVISE`, and then every finding with file and line. Store it verbatim under a
new filename ending `-RAW.md`. A reviewer who authors semantic repairs retires
their review; repaired bytes need a fresh independent reviewer.
