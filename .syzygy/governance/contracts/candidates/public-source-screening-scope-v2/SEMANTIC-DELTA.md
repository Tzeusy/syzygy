# Semantic delta — public-source screening scope, version 2

> **Candidate — binds nothing.** Drafted 2026-10-04 for the dossier-quality
> gap on prose sources (`syzygy-mea`). Effect comes only from an owner
> `approve-policy` act over the exact proposed bytes. No repository body was
> read to draft it, and no act is recorded here.

## Class

Normative. It maps one RFC5-14 class to a closed set of paths in a policy that
today leaves all prose indeterminate. It adds no network route, no storage
place and no detector change.

## Subject and change

Subject: the secret-classification policy of `project:syzygy` **after** the
version-1 scope (package `public-source-screening-scope`). The builder
`scripts/build_public_source_screening_scope_v2.py` takes the policy on disk
when it already is the version-1 bytes, or derives those bytes with the
version-1 builder when it is not yet signed, and checks them against the
version-1 manifest row. Both give the same patch and the same manifest row.
`policyVersion` moves to the next minor, with the label
`public-source-candidate.1` kept.

Inside `publicSourceScope` exactly these things change; the builder fails if
anything else does:

| Part | Change |
|---|---|
| `contentClassification.classesClassified` | adds `project-documentation` after `code-content` |
| `contentClassification.rules` | adds one rule for the class, below |
| `contentClassification.indeterminate` | the same fail-closed reading, with the examples no longer naming README or licence files |
| `prerequisite` (new) | the rule classifies only while the in-force RFC-0005 vocabulary lists `project-documentation`; otherwise every file it names is indeterminate again |

## The rule

Matching folds the ASCII letters A to Z to a to z in a copy of the path and
folds, normalizes and decodes nothing else. A path with an empty, "." or ".."
segment, a backslash, or a leading or trailing slash matches nothing. A path is
`project-documentation` when it matches one of three path rules; the body is
admitted as whole-blob spans, no extractor runs.

1. **root-document.** One segment (a file at the repository root). Remove an
   optional prefix of exactly two ASCII digits 0-9 and a hyphen (literal code
   points; no Unicode digit counts), then one suffix from "none, .md, .rst,
   .txt"; the rest must be one of: readme, changelog, changes, release-notes,
   release_notes, releasenotes, contributing, license, licence, copying, notice,
   notices, news, history, authors, faq. A top level often carries its stated
   ideas in files such as 00-RELEASENOTES [Inferred, from general knowledge; no
   body was read]. architecture and manifesto are owner opt-ins, off in these
   bytes (packet Q2, Q3).
2. **docs-tree.** Two or more segments, the first being docs or doc, a file
   name ending in .md, .rst or .txt with a non-empty stem, at any depth, with
   two exclusions: no directory segment after the first may be adr, adrs,
   decisions, rfc, rfcs, spec, specs, specification, design, governance, policy,
   policies or security (exact, case-folded); and a .txt file whose name is
   cmakelists.txt or robots.txt, or starts with requirements, is a build or
   tooling file and not mapped.
3. **licenses-tree.** Exactly two segments, the first being licenses, a file
   name ending in .txt or .md with a non-empty stem.

A TypeScript consumer must compare the listed ASCII digits, not a Unicode-aware
class, and must fold only A-Z; the builder's reference reader is the oracle and
its fixtures include a long s, the Kelvin sign and Arabic-Indic digits.

None of these extensions is in the `code-content` list, so no blob has two
classes. Everything else stays indeterminate: a README below the root outside
docs or doc (vendored libraries carry their own), security and conduct
policies below the root, specification, design, decision and policy documents,
and reports, and prose in any other directory.

## Why these paths [Inferred]

RFC5-14 as amended by PR #257 names the class as the project's own prose that
describes, explains or accompanies it: README, guides, tutorials, changelogs
and release notes, contribution guides, licence and notice files, "ordinarily;
the declared policy decides each file". It says an extension or directory name
places a file in the class only through a rule of the declared policy, and a
file the policy cannot place in exactly one class fails closed. The three rules
are the owner-reviewable proposal of that decision; the amendment does not list
them.

**Policy and governance text is deliberately not mapped.** RFC5-14 places
doctrine, spec, decision and policy text in `governance-text`, and
`governanceTextPaths` stays empty here. Root files named design, governance,
security and code of conduct, and docs paths under the directories listed in
rule 2, are withheld. Withholding design is this policy's choice: the amendment
does not name design. See packet Q4.

## Prerequisite

Valid only while the RFC-0005 amendment of PR #257 is in force. The scope
carries the condition as data (`prerequisite`), and `--ready` fails while the
installed RFC-0005 text does not define the class or the version-1 act is not
recorded. A consent that does not list `project-documentation` still permits
no egress of it (RFC5-14); this policy confers no consent.

## What it does not change

The detectors (they run on every admitted body, inside inert code contexts
too), the active-content rule, the access boundary, raw-body handling,
`neverClassified` (`work-history`), the inherited rules, the Butlers scope, and
every act already performed. It admits no repository and grants no read or
egress.

## Supersession and the state after the act

This package's subject is the policy as version 1 leaves it. After the act, the
policy on disk is these bytes; the package's `--check` recognises that state
(the disk hash equals this manifest's row, and reversing the patch gives the
version-1 row) and stays current. Version 1's row is then superseded for the
`approve-policy` role, as the version-1 act superseded the 2026-10-02 re-pin
act: the v2 recorder writes a new dedicated record and the version-1 record and
recorder stay unedited, and the version-1 recorder's `--check` fails by design
[Inferred from the earlier supersession; the recorder is written after the
review].
