# Amendment acceptance and verification obligations

Candidate — binds nothing. Candidate checklist; unchecked obligations are
unperformed. This is not a dispatch plan, an adoption record or permission to
implement the proposed behavior.

## Specification acceptance

- [ ] Independent fresh-context review of the delta and its impact ledger
      (`.syzygy/governance/contracts/candidates/polaris-dossier-local-agent-mode/REVIEW-BRIEF.md`).
- [ ] The owner's ruling on question R1 of the decision packet (where
      Syzygy's records live, and the reading of REQ-polaris-generation-018,
      020 and 022 for this mode).
- [ ] The owner's adoption of a SEC-3 amendment permitting the operator's
      agent session to build and run the observed project on the host,
      drafted and reviewed as its own change
      (`POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-2026-10-05`, item 1).
      Sign-off may not precede it.
- [ ] The owner's sign-off by option selection naming v1.0, extending
      version-tag sign-off to Polaris generator specification deltas
      (`POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-2026-10-05`, item 3),
      taken with the first review's findings 6, 7 and 8 in view.
- [ ] After sign-off: a package builder that `scripts/record_versioned_signoff.py`
      accepts (installs `proposed/` into `specs/`, checks and recounts), so the
      recorder writes the sign-off record and the tag
      `polaris-dossier-local-agent-mode-v1.0`; the profile change (032) can
      reuse it.
- [ ] On adoption, in one logical change (CC-REV-2): move the candidate spec
      from `proposed/` to `specs/polaris-generation/spec.md`; generalize
      `scripts/count_polaris_effective_scenarios.py` and the check that
      classifies base and overlay files so that more than one overlay is
      composed (the profile change needs the same step; whichever is adopted
      second reuses the first's generalization); update `PROJECT-STATUS.md`'s
      effective requirement and scenario counts by recount, never by
      arithmetic; regenerate `DIRECTIVE-REGISTER.md` and replace this
      change's hand-held dependency union with a generated one.

## Required implementation and proof after applicable authorization

- [ ] `init`: consent, registry and policy evaluation; HEAD equals a consented
      revision; config validation with no default limits, zero allowed only
      for the repair and question limits; the four-condition governed
      predicate and, for a governed or silent subject, the in-force
      per-project provider statement; `brief` carries the execution rule in
      force. Exercise every
      refusal arm of REQ-polaris-generation-033 with independently prepared
      fixtures.
- [ ] Prove no provider call and no transmission: an independent capture of
      the process's network activity over a full run, not the run record.
- [ ] Object reads only: a fixture clone whose working tree differs from HEAD
      in a quoted file; the rendered quotation and source page must carry the
      committed bytes. Fixture clones with a replacement ref, an overwritten
      loose object, an alternates file and a repository-local configuration
      that names a command: each must refuse or read the original bytes, and
      no configured command may run.
- [ ] Stored records: alter a recorded byte range, check result, packet
      digest and frozen subject between steps; no rendered Observed
      quotation, source page or counted verdict may change, and the cycle
      count and instants must render with Inferred integrity. No Syzygy
      credential is issued for a run or written to the state directory.
- [ ] `check`: quotation, path, range, label, citation-by-block-kind and
      understanding-record checks with a normalisation offset map; per-predicate mutation evidence (verification rule 6) for
      altered, elided, joined, out-of-range and excluded-file quotations and
      for self-labelled Observed claims.
- [ ] Limits: repair-cycle, deadline and question limits refused by Syzygy;
      operator-declared usage labelled Inferred; undeclared usage recorded as
      not recorded, never zero.
- [ ] Review: packet contents compared byte for byte with an independently
      assembled expected packet; stale-digest, self-review, incomplete and
      inconsistent verdicts refused; an inventory declared under the
      authoring session's identifier refused; independence and inventory
      completeness disclosed as Inferred.
- [ ] Render: anchors in RFC7-10's form, class evidence artifact identifier
      with integrity digest, from the recomputed object identifier, byte
      range and revision; source pages only for screened blobs Syzygy read; the
      disclosure block and the two discovery populations in human and machine
      form with parity.
- [ ] The Claude Code skill and Codex instructions in `design.md`, installed
      only after sign-off, and one end-to-end run per tool against a consented
      fixture repository before any real target.
- [ ] Verify the complete adopted generator specification together with this
      change; this checklist does not replace unfinished requirements.
