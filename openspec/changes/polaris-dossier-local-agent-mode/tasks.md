# Amendment acceptance and verification obligations

Candidate — binds nothing. Candidate checklist; unchecked obligations are
unperformed. This is not a dispatch plan, an adoption record or permission to
implement the proposed behavior.

## Specification acceptance

- [ ] Independent fresh-context review of the delta and its impact ledger
      (`.syzygy/governance/contracts/candidates/polaris-dossier-local-agent-mode/REVIEW-BRIEF.md`).
- [ ] Owner rulings on the questions in that package's owner decision packet,
      including the sign-off form (its O5).
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
      revision; config validation with no default limits. Exercise every
      refusal arm of REQ-polaris-generation-033 with independently prepared
      fixtures.
- [ ] Prove no provider call and no transmission: an independent capture of
      the process's network activity over a full run, not the run record.
- [ ] Object reads only: a fixture clone whose working tree differs from HEAD
      in a quoted file; the rendered quotation and source page must carry the
      committed bytes.
- [ ] `check`: quotation, path, range and label checks with a normalisation
      offset map; per-predicate mutation evidence (verification rule 6) for
      altered, elided, joined, out-of-range and excluded-file quotations and
      for self-labelled Observed claims.
- [ ] Limits: repair-cycle, deadline and question limits refused by Syzygy;
      operator-declared usage labelled Inferred; undeclared usage recorded as
      not recorded, never zero.
- [ ] Review: packet contents compared byte for byte with an independently
      assembled expected packet; stale-digest, self-review, incomplete and
      inconsistent verdicts refused; independence disclosed as Inferred.
- [ ] Render: anchors in RFC7-10's form from object identifier, byte range and
      revision; source pages only for screened blobs Syzygy read; the
      disclosure block and the two discovery populations in human and machine
      form with parity.
- [ ] The Claude Code skill and Codex instructions in `design.md`, installed
      only after sign-off, and one end-to-end run per tool against a consented
      fixture repository before any real target.
- [ ] Verify the complete adopted generator specification together with this
      change; this checklist does not replace unfinished requirements.
