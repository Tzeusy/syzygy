> **Candidate — binds nothing.** A proposed amendment to one accepted contract
> module. No act exists over it and none is performed here. The proposed bytes
> are not applied to the installed or mirrored module.

# Semantic delta RFC5-PD-1 — add the `project-documentation` content class to RFC5-14

**Artifact(s):**         `.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md` and its identical mirror `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/consent-egress-secrets.md`
**Stable IDs affected:**  RFC5-14 (one table row and one bullet added; no clause renumbered, retired or moved)
**Change class:**         Normative — an egress-consent vocabulary gains a member, so content that was refused as unclassifiable can become consentable
**Author:**               lane-d drafting agent (Claude Opus 5.5); adoption is the owner's alone (VIS-4)
**Date:**                 2026-10-03

## Current meaning

RFC5-14, quoted from the module at its current bytes, which the contract readability restyle binds:

> The content-class vocabulary is closed at this RFC (amend to extend):
>
> | Class | Contents |
> |---|---|
> | `governance-text` | Doctrine, spec, decision, policy text |
> | `code-structure` | Identifiers, paths, symbols, structural graph — no bodies |
> | `code-content` | Source and test bodies |
> | `work-history` | Work items, run summaries, telemetry, cost data |
> | `evidence-content` | Evidence artifact contents (reports, logs) |
> | `derived-composites` | Prompts, summaries, embeddings composed from the above |
>
> - A composite inherits the **highest** class of any content it embeds;
>   `derived-composites` consent alone never launders an unconsented class into
>   an egress.

[Observed] A README, user guide, tutorial or licence file is none of the first
three rows' contents; under the closed vocabulary it is undeterminable and
RFC5-14 refuses its egress. The owner's 2026-10-03 answer to Q7 of
the public-repo-admission owner decision packet chose to amend RFC5-14 for
this (the public-repo-admission owner-answers direction of that date, on the
`polaris/public-repo-admission` branch of PR 215 until that lands).

## Proposed meaning

The exact proposed text is the patch
`proposed/RFC-0005/consent-egress-secrets.md.patch`; the two insertions, in
full:

Table row, between `code-content` and `work-history`:

> | `project-documentation` | A project's own prose that describes, explains or accompanies the project for its readers and does not govern its development: README, user and developer guides, tutorials, how-to and overview documents, changelogs and release notes, contribution guides, and licence and notice files, ordinarily; the declared policy decides each file |

Bullet, directly after the composite-inheritance bullet:

> - **`project-documentation` is a class of its own, decided by the declared
>   policy, per file.**
>   - A document the project's declared classification policy places as
>     doctrine, spec, decision or policy text is `governance-text`, not
>     `project-documentation`; source and test bodies, and comments or
>     docstrings inside them, are `code-content`.
>   - A file the policy cannot place in exactly one class is undeterminable and
>     fails closed (RFC5-15); a file extension, a directory name or a file's
>     own claim about itself places a file in this class only through a rule of
>     the declared policy, never on its own.
>   - A consent record that does not list `project-documentation` does not
>     permit its egress, and no consent granted before this class existed is
>     read as covering it.
>   - The class adds no ordering among classes and changes neither the composite
>     rule above nor secret screening at ingest (RFC5-16), which applies to it
>     in full.

Membership, as the proposed text states it: prose that describes, explains or
accompanies a project for its readers and does not govern its development.
Contribution guides are included as reader-facing instructions; a document that
sets binding rules for the project's own governance (a decision record, a
policy, a specification) is `governance-text`. Where one file is both, the
declared policy decides, and where it cannot, egress is refused.

The row's list is therefore ordinary membership, not a guarantee: the policy
is the tie-breaker. Four kinds of file the list does not settle by itself, and
how the proposed text resolves each:

- An architecture overview, which can be an "overview document" or design text
  the policy places as `governance-text`: the policy decides.
- A contribution guide that states binding process rules: the definition
  excludes prose that governs development, so the policy decides whether it is
  `governance-text`; the row does not assert it is documentation.
- A generated API reference built from docstrings. Docstrings inside source are
  `code-content`; a policy that places a generated reference as
  `project-documentation` thereby lets docstring text egress under a consent
  that excludes `code-content`. The declared policy, honored only under
  RFC3-16(a), is the guard; a policy should not place such a file here.
- A notebook mixes code cells (`code-content`) and prose cells. It is not
  placed in exactly one class, so it is undeterminable and fails closed
  unless the policy splits it.

**What the sub-bullet on signals says.** A file extension, a directory name or
a file's own claim about itself places a file in this class only through a rule
of the declared policy. This restates RFC3-16(a)'s point that an untrusted
claim classifies nothing; it does not forbid a policy rule keyed on a path or
extension (`docs/**`, `LICENSE*`), which is the ordinary way a policy is
written. Round 1 found an earlier wording ("places nothing") that read as
forbidding such rules; it is replaced here, and this delta keeps that wording
out of the contract.

## What explicitly does NOT change

- The other six rows, byte for byte and in order; the builder compares them.
- The composite-inheritance bullet, byte for byte. [Observed] RFC5-14 prints
  "highest" without defining an order, and the adopted generator
  specification's source policy states that no total order is invented from the
  vocabulary and that the declared policy determines a composite's inherited
  class. This delta neither defines an order nor reads one into the new row.
- RFC5-15's three-part transmission check, RFC5-16's ingest screening and
  RFC5-17's hash-not-body exclusions. Documentation is screened for secrets
  like any other content.
- That the declared classification policy is honored only under RFC3-16(a),
  and what a classification policy may contain: that is "Not this RFC's"
  (`rfcs/RFC-0005/README.md`, line 182), and no sentence of the proposed text
  constrains it.
- Every consent record. No existing or candidate egress record gains the class;
  each lists classes explicitly and a record without the new row does not
  permit it.
- Clause identities, clause leads, YAML front matter and heading lines; the
  builder verifies clause leads, front matter and headings, and
  `verify_final_prespec.py`, CG-13 and CG-17
  pass on a scratch tree holding the patched module.
- No implementation, policy, registry entry, consent or egress is authorized.

## Warrant

The owner's 2026-10-03 direction answering Q7 (option a: "Amend RFC5-14; T1
starts without") and the packet's account that without the class the
documentation files that best show what a project is for, and the licence
files the Redis licence-history proof depends on, cannot be sent.

## Evidence or decision basis

- The public-repo-admission owner decision packet, Q7 (PR 215 branch).
- RFC5-14, RFC5-15, RFC5-16 at their defining clauses in the module above.
- `openspec/changes/polaris-manifesto-generation/SOURCE-POLICY.md`, section "Carry content provenance through composition", for the no-invented-order statement.
- `docs/polaris-generation/REDIS-DOSSIER-GAP-ANALYSIS.md`, gap 16 (research note; binds nothing).

Everyone who can reach the artifact can reach these, except the first, which is
reachable on PR 215's branch until it lands.

## Terms introduced / retired

Introduced: the content class `project-documentation`. It is a vocabulary
member, not a new durable term for the term registry. Retired: none.

## Downstream impact

Method: the sweeps published, with their regexes, run form and span rule, in
`IMPACT-LEDGER.md`, run by script over the 1988 tracked files at commit
`9a6e8e31cfa842e83fa0970765f581579b40de3b` (1984 readable as UTF-8): 78 files
name a class, 82 cite RFC5-14, 20 do both, the union is 140, and a second
method (files naming at least four of the six classes) gives 7. The IMPACT-LEDGER.md classifies all of them; the findings that matter:

- [Observed] One authority text enumerates the six classes and goes stale on
  adoption: `openspec/changes/polaris-manifesto-generation/SOURCE-POLICY.md`
  ("The egress vocabulary remains governance-text, ..."). It is digest-bound by
  performed acts and cannot be edited here. See the migration plan.
- [Observed] No implementation enumerates the six classes (the 20 code files
  in the union use the strings for unrelated models).
- The generator specification's REQ-polaris-generation-025 cites "RFC5-14's
  closed vocabulary" by reference and follows the amendment without an edit.

## Migration / supersession plan

1. The module is digest-bound twice over (the bootstrap manifest binds both
   mirrors, and the readability restyle link binds them again), so the proposed
   bytes are not applied while this is a candidate. On adoption the change that
   records the owner's act applies the patch to both mirrors and regenerates
   every derived artifact CG-7h and the contract index name, in one logical
   change; a fresh digest-binding review precedes the offering.
2. `SOURCE-POLICY.md` cannot take an edit (a performed act binds its bytes).
   Its present-tense sentence "The egress vocabulary remains" the six classes
   is false after adoption, and NORMATIVE-CHANGE-WORKFLOW step 6 requires an
   invalidated authoritative artifact to be updated in the same change. The
   only lawful propagation is a readability successor
   (`scripts/readability_successor.py`) that replaces the file, which needs its
   own owner sign-off. This delta therefore departs from step 6 unless the
   owner directs that successor with the adoption; if the owner leaves the file
   as is, the disclosure lives in this delta and in the act record's
   consequences section, and REQ-025, which binds and cites the vocabulary by
   reference, is the text to read. This delta does not choose.
3. The admission package's public-source screening scope will need rules that
   place project documentation; that is a separate candidate, not a
   propagation of this one.
4. Superseded material: none leaves a reading path.

## Review

**Required class:**  digest-binding confirming review, per CC-REV-1 and CC-REV-4; fresh context, `REVIEW-BRIEF.md`
**Reviewer:**        not the drafter and not a shared session
**Verdict:**         none yet; no review has been run
