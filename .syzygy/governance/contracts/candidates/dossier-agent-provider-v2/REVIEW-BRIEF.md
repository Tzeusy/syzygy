# Review brief — agent-provider statement, version 2 (round 1)

> **Candidate — binds nothing.** Not a review; carries no verdict.

## What the reviewer is given

CC-REV-1: a fresh context holding the artifact, its governing references and
these criteria.

**Artifact:** every file of
`.syzygy/governance/contracts/candidates/dossier-agent-provider-v2/` and
`scripts/build_dossier_agent_provider_v2.py`.

**References:** the version-1 record and template in
`../dossier-local-agent-acts/`; its act record
`.syzygy/governance/decisions/DOSSIER-LOCAL-AGENT-REDIS-AGENT-ANTHROPIC-ACT.md`;
RFC5-13 and RFC5-14 at their defining clauses;
`.syzygy/governance/decisions/RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md`;
the egress version-2 record as the supersession precedent;
`packages/polaris-dossier/src/gate-sources.ts`.

## Acceptance criteria

1. **Is the diff exactly the stated change?** Run the builder's `--check` and
   `--selftest`, and `git diff --no-index` the version-1 and version-2 records.
   Only the five lines in the delta's table may differ.
2. **Is the supersession sound?** Prospective (RFC5-13), from the act's own
   instant, naming version 1 by version; no edit to version 1's bytes or act.
3. **Is the class addition the whole widening?** Does adding
   `project-documentation` permit anything beyond Syzygy's packets carrying
   screening-admitted documentation spans to the operator's own Claude Code
   sessions for this one repository?
4. **Is the install list complete?** The delta names the gate-sources forms,
   the withdrawal sweep, the ambiguity refusal, the tests and the recorder. Is
   anything missing that would make the gate refuse once a version-2 act record
   exists in `decisions/`?
5. **Authority.** No file labels anything accepted or approved; no 64-hex
   digest appears in Markdown outside `instances/` and `reviews/`.

## Recording

Store the raw verbatim in this package's `reviews/` directory as
`R-DOSSIER-AGENT-PROVIDER-V2-1-RAW.md`, its first four non-blank lines the
title and exactly

```text
Reviewed commit: <40 hex>
Manifest SHA-256: <SHA-256 of the manifest FILE>
Verdict: CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE
```

Print the manifest file's digest with
`python3 scripts/build_dossier_agent_provider_v2.py --manifest-digest`.
Number findings `**Finding N — title** (blocking|revise|note)` under a
`## Findings` heading.
