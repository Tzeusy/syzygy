# Review brief — the Butlers source grammar written into the registry entry

> **Candidate — binds nothing.** This brief says what an independent
> reviewer is given and what they decide. It is not a review and carries
> no verdict. **Round 2.** Round 1 returned REVISE; its raw is retained
> verbatim at `docs/reviews/R-DOV24-LOADED-PROFILE-AMENDMENT-RAW.md`, and
> the packet's "Review record" table says what was done with each finding.

## What the reviewer is given, and nothing else

**The artifact** — the five files of
`.syzygy/governance/contracts/candidates/pwb-registry-loaded-profile-amendment/`
(`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`, this
brief, `PWB-LOADED-PROFILE-AMENDMENT-MANIFEST.txt`), the patch under
`proposed/`, and `scripts/build_pwb_registry_loaded_profile_amendment.py`.

**The subject** —
`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
at its current bytes, and the `.18` patch under
`.syzygy/governance/contracts/candidates/pwb-registry-currency-briefing-amendment/proposed/`
that this one is drafted on.

**Governing references** —

- `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`, row P-74.
- `.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`, for the ceremony and supersession.
- The PWB specification's reader definitions and `PWB-REQ-001`, `PWB-REQ-002`, `PWB-REQ-004` in
  `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`.
- `packages/three-surface-poc-core/src/project-shape-manifest.ts` and
  `packages/three-surface-poc-core/src/project-shape-extraction.ts`.
- `NORMATIVE-CHANGE-WORKFLOW.md` and `SEMANTIC-DELTA-TEMPLATE.md`.

- Row P-82 of the same rulings record, and question Q4 of
  `docs/design/POLARIS-M15-PIPELINE-TRUTHFULNESS-FUNNEL.md` (line 72), for
  the root-independence overlap only.
- `.syzygy/governance/decisions/POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md`
  §6, for the landing order the owner ruled.
- The round-1 raw named above.

**Withheld** — the M8 funnel under `docs/design/`. It recommends; the
ruling decides.

**Environment** — Node 22.18 or later on the path: the behaviour check
runs the observer's TypeScript directly.

## Acceptance criteria

1. **Is it a pure restatement?** For each of the fifteen `classGrammar`
   rows and eight bindings, does the code read exactly that file, heading,
   level and shape — and is there any rule in the two TypeScript files
   that neither the fields nor the `sharedReadingRules` sentence states?
   Name it if so. Is anything in `sharedReadingRules` in fact per-project?
2. **Are the nine container-shape sentences exact?** Each says what is
   read and what fails. Check each against the extraction code; a sentence
   that is looser or stricter than the code is a finding.
3. **Does the package verify, and does the verification mean anything?**
   Run `--check` and `--selftest` (190 predicates). Name any claim the
   builder makes that no mutant covers, and any sentence clause that no
   behaviour probe exercises and that the packet does not admit is checked
   by its pin alone. Did each round-1 finding get the disposition the
   packet's table says?
4. **Is anything else in the entry changed?** Only the two versions and the
   six added keys may differ from `.18`'s bytes.
5. **Is the stacking on `.18` sound?** Confirm, in each of the three
   states — `.18` pending; `.18` applied; this package applied — that
   `--check` and `--selftest` pass and compute the same manifest row, and
   that `--apply` refuses before `.18` and after this package.
6. **Does the package quote any act argument or claim authority it lacks?**
   No 64-hex digest beside an act phrase; nothing labelled accepted or in
   force.
7. **Are the open questions honest?** In particular question 3 (both
   readings of P-74's "edited on no arm"), question 9 (the overlap with
   M15's root-independence design) and the landing-order section: is any
   order attributed to the owner beyond `.21` → `.30` → `.22` → lane B?

## Out of scope

Whether to perform the act; the version numbers; N8's specification text.

## Recording

Raw output under `docs/reviews/`, file name ending `-RAW.md`, verdict
words copied exactly. A digest quoted in a raw freezes those bytes.
