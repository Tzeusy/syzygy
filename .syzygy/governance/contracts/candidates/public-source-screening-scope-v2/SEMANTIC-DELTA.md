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
`policyVersion` moves to the next minor with the label
`public-source-candidate.1` kept and the variant's name appended, so the version
says which variant is in force.

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
`project-documentation` when it matches exactly one of three path rules; the
body is admitted as whole-blob spans, no extractor runs.

1. **root-document.** One segment (a file at the repository root). Remove an
   optional prefix of exactly two ASCII digits 0-9 and a hyphen (literal code
   points; no Unicode digit counts), then one suffix from "none, .md, .rst,
   .txt"; the rest must be one of the root names below.
2. **docs-tree.** Two or more segments, the first being docs or doc, a file name
   ending in .md, .rst or .txt with a non-empty stem, at any depth, in which no
   directory name after the first and no file name without its extension has a
   word of the denylist below, and which is not a build or tooling .txt file.
3. **licenses-tree.** Exactly two segments, the first being licenses, a file
   name ending in .txt or .md with a non-empty stem.

The lists below are generated from the rule's constants by the package builder,
and its check fails if they differ from the policy bytes. They are the only
statement of what is sendable and what is withheld.

<!-- BEGIN GENERATED: lists -->
**In one sentence:** the rule withholds policy and governance text by name only, using the listed words; such text under any other name is sendable, including names written without a separator (SecurityPolicy, ADR0001) or split by a character outside the separator list.

**Becomes readable** (and, under a consent that lists the class and a separate egress consent, sendable):

- Root-level files named README, CHANGELOG, CHANGES, RELEASE-NOTES, RELEASE_NOTES, RELEASENOTES, CONTRIBUTING, LICENSE, LICENCE, COPYING, NOTICE, NOTICES, NEWS, HISTORY, AUTHORS, FAQ (any letter case; an optional prefix of two ASCII digits and a hyphen, so 00-RELEASENOTES counts; no extension or one of .md, .rst, .txt).
- Files ending .md, .rst, .txt under a top-level docs or doc folder, at any depth, unless the path is withheld below.
- Files ending .md, .txt directly inside a top-level licenses folder.
- Only in the variant you pick: variant none adds nothing; variant manifesto adds the root name MANIFESTO, and lifts the same word from the docs withholding; variant architecture adds the root name ARCHITECTURE, and lifts the same word from the docs withholding; variant both adds the root names ARCHITECTURE, MANIFESTO, and lifts the same words from the docs withholding.

**Stays withheld** (excluded from reading and from egress, hash-not-body):

- Root files named DESIGN, GOVERNANCE, SECURITY, CODE_OF_CONDUCT, CODE-OF-CONDUCT, and ARCHITECTURE and MANIFESTO unless the variant you pick adds them.
- Under a docs or doc folder, any path where a directory name (after the first) or the file name (without its extension) contains one of these as a whole word: adr, adrs, decision, decisions, rfc, rfcs, spec, specs, specification, specifications, design, designs, governance, policy, policies, security, conduct, doctrine, doctrines, principle, principles; and, unless the variant adds them, architecture, architectures, manifesto, manifestos. Names are split into words at each of '-' '_' '.' ' ' and compared after folding A-Z to a-z; so a policy-shaped document is withheld by name, and a governance document whose path carries none of these words is NOT withheld (the rule decides by name alone).
- Under a docs or doc folder, .txt files named cmakelists.txt, robots.txt or starting requirements.
- READMEs and the other root names when they sit below the root outside docs or doc (vendored libraries carry their own).
- Any other path: it is not named by the rule, so it is indeterminate and withheld.
- Any file that fails a secret detector or the active-content rule: those screens are unchanged and apply to this prose in full.
- Everything, while the RFC-0005 amendment of PR #257 is not in force.
<!-- END GENERATED: lists -->

A TypeScript consumer must reproduce the rule literally: compare the listed
ASCII digits, not a Unicode-aware class; fold only A-Z, so a long s or the Kelvin
sign is not folded (a file whose name uses the Kelvin sign for k is therefore
not recognised as a build file, and is mapped; this is by design, the detectors
and the active-content screen still apply); and split names at the listed
separators into whole words.

None of these extensions is in the `code-content` list, so no blob has two
classes.

## Why these paths [Inferred]

RFC5-14 as amended by PR #257 names the class as the project's own prose that
describes, explains or accompanies it: README, guides, tutorials, changelogs
and release notes, contribution guides, licence and notice files, "ordinarily;
the declared policy decides each file". It says an extension or directory name
places a file in the class only through a rule of the declared policy, and a
file the policy cannot place in exactly one class fails closed. The three rules
are the owner-reviewable proposal of that decision; the amendment does not list
them.

**Policy and governance text is withheld by name, not by content.** RFC5-14 places
doctrine, spec, decision and policy text in `governance-text`, and
`governanceTextPaths` stays empty here. Root files named design, governance,
security and code of conduct, and docs paths whose names carry a word of the
denylist, are withheld. A governance document under docs whose path carries none of those
words is mapped: the rule cannot read content. Withholding design is this policy's choice: the amendment
does not name design. See packet Q3.

## Variants

The manifest carries four rows and the package four patches, one per variant:
none (the default), manifesto, architecture, both. They differ only in
`rootStems`, the docs denylist (the opt-in words are denied in the variants that do
not add them) and the `policyVersion` suffix, which names the variant; the owner picks exactly one row at the sitting (packet Q1) and
`--check` verifies all four, including that no two produce the same bytes.

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

## One variant act only

Nothing in the bytes stops a second `approve-policy` act over another row of the
manifest. The recorder (written after the review) must refuse a second variant
act over this manifest unless it is a declared superseding version; the
`policyVersion` suffix (the variant's name) tells which variant is in force, and
the digest decides.
