# Owner decision packet — public-source screening scope, version 2

> **Candidate — binds nothing.** It carries no digest. Nothing here is a
> decision, and no act is performed by reading it. It is offered only after a
> confirming review.

> **Review state.** Round 4 returned REVISE and was repaired (commit 33b15a65);
> round 5, which read that repair at commit fd4e2509, also returned REVISE. The
> round-5 repairs, 77 insertions and 37 deletions in 9 files (commit 39d83718
> over fd4e2509: this packet, the semantic delta, the review brief, the
> manifest, four patches and the builder; it excludes the retained round-5 raw,
> the round-5 dispositions and this statement), are unreviewed until round 6
> reads them. If round 6 does not confirm them, the recorder stays unfrozen and
> the owner chooses what to do next; nothing here is signed on unreviewed bytes.

## What this is, in plain words

The version-1 scope lets the generator read a public repository's source code
and nothing else. A dossier needs the project's own explanation of itself, so
this version lets it read the README, changelog, contribution and licence
files, and the guides under a top-level docs folder. What it withholds, and
what that leaves sendable, is stated once, in the generated block below.

## What becomes sendable, and what stays withheld

The lists below are generated from the rule's own constants by the package
builder, and its check fails if they differ from the policy bytes.

<!-- BEGIN GENERATED: lists -->
**In one sentence:** the rule withholds policy and governance text by name only: a path under docs or doc or licenses with one of the words adr, adrs, decision, decisions, rfc, rfcs, spec, specs, specification, specifications, design, designs, governance, policy, policies, security, conduct, doctrine, doctrines, principle, principles (and, unless the variant adds them, architecture, architectures, manifesto, manifestos) as a whole word in a directory or file name, and the root files named DESIGN, GOVERNANCE, SECURITY, CODE_OF_CONDUCT, CODE-OF-CONDUCT; such text under any other name inside the mapped paths is sendable, including names written without a separator (SecurityPolicy, ADR0001) or split by a character outside the separator list.

**Becomes readable** (and, under a consent that lists the class and a separate egress consent, sendable):

- Root-level files named README, CHANGELOG, CHANGES, RELEASE-NOTES, RELEASE_NOTES, RELEASENOTES, CONTRIBUTING, LICENSE, LICENCE, COPYING, NOTICE, NOTICES, NEWS, HISTORY, AUTHORS, FAQ (any letter case; an optional prefix of two ASCII digits and a hyphen, so 00-RELEASENOTES counts; no extension or one of .md, .rst, .txt).
- Files ending .md, .rst, .txt under a top-level docs or doc folder, at any depth, unless the path is withheld below.
- Files ending .md, .txt directly inside a top-level licenses folder, unless the file name is withheld below.
- Only in the variant you pick: variant none adds nothing; variant manifesto adds the root name MANIFESTO, and lifts the same word from the docs and licenses withholding; variant architecture adds the root name ARCHITECTURE, and lifts the same word from the docs and licenses withholding; variant both adds the root names ARCHITECTURE, MANIFESTO, and lifts the same words from the docs and licenses withholding.

**Stays withheld** (excluded from reading and from egress, hash-not-body):

- Root files named DESIGN, GOVERNANCE, SECURITY, CODE_OF_CONDUCT, CODE-OF-CONDUCT, and ARCHITECTURE and MANIFESTO unless the variant you pick adds them.
- Under a docs, doc or licenses folder, any path where a directory name (after the first) or the file name (without its extension) contains one of these as a whole word: adr, adrs, decision, decisions, rfc, rfcs, spec, specs, specification, specifications, design, designs, governance, policy, policies, security, conduct, doctrine, doctrines, principle, principles; and, unless the variant adds them, architecture, architectures, manifesto, manifestos. Names are split into words at each of '-' '_' '.' ' ' and compared after folding A-Z to a-z; so a policy-shaped document is withheld by name, and a governance document whose path carries none of these words is NOT withheld (the rule decides by name alone).
- Under a docs or doc folder, .txt files named cmakelists.txt, robots.txt or starting requirements.
- READMEs and the other root names when they sit below the root outside docs, doc and licenses (vendored libraries carry their own); a file directly inside a top-level licenses folder and ending .md or .txt is mapped whatever its stem unless a word above withholds it.
- Any other path: it is not named by the rule, so it is indeterminate and withheld.
- Any file that fails a secret detector or the active-content rule: those screens are unchanged and apply to this prose in full.
- Everything, while the RFC-0005 amendment of PR #257 is not in force.
<!-- END GENERATED: lists -->

None of this gives consent: a repository consent that does not list
`project-documentation` still sends none of it.

## The act

An `approve-policy` act over one proposed policy bytes, at one row of the
package manifest, in the form of the version-1 act: the manifest has four rows,
one per variant, and you pick exactly one at the sitting. A recorder, frozen only after a
confirming review, takes the chosen row.

## Order, as fact

This act's subject is the policy as version 1 leaves it, so it can only follow
the version-1 act, and its prerequisite is the RFC-0005 amendment of PR #257.
The package refuses to be ready before both. Each policy act breaks the Butlers
read gate until its code re-pin lands, so with both in one sitting the re-pin is
made once, against the chosen row's bytes.

## Questions

**Q1. Which variant? Default: none.** The four variants differ only in whether
two names, MANIFESTO and ARCHITECTURE, are mapped, and they are mapped (or
withheld) everywhere the rule looks: as a root file, inside the docs folder
(as a file or directory name) and as a file name directly under the licenses
folder. Everything else in the four is the same.

- **none**: neither word is mapped anywhere.
- **manifesto**: MANIFESTO is mapped.
- **architecture**: ARCHITECTURE is mapped.
- **both**: both are mapped.

*What declining costs.* MANIFESTO is plausibly the project's own statement of
its ideas, and is likely the best core-ideas source for a project that has one
[Inferred, from general knowledge; no body was read]. Without it the dossier's
core-ideas and trade-off sections rest on the README and guides only. It is
also plausibly doctrine, which RFC5-14 puts in `governance-text`, and the file
name cannot tell the generator which it is. ARCHITECTURE is usually
explanation, but RFC5-14 says that for an architecture overview the declared
policy decides, and it may be design authority. *Recommended:* none, unless you
have seen the file; or manifesto if you accept the risk that it is doctrine.
Signing a variant is the whole decision: no regeneration or review follows, and
the recorder refuses a second variant act over this manifest unless it is a
declared superseding version (the policy bytes themselves do not enforce this).

**Q2. Sign the chosen variant? Default: yes, after a confirming review,** once
the order above is met.

**Q3. Policy and governance text, withheld by name. Default: withheld.** The
rule cannot read a file's content, so it withholds by name: root files named
DESIGN, GOVERNANCE, SECURITY and CODE_OF_CONDUCT, and any docs path where a
directory or file name contains, as a whole word, decision, specification,
design, governance, policy, security, conduct, doctrine, principle, adr or rfc
(or the MANIFESTO and ARCHITECTURE words unless you pick them); the same words
withhold a file name directly under the licenses folder. The lists above show the exact words.
The cost runs both ways: a tutorial named "design-patterns" is withheld, and a
governance document whose name carries none of the words is sendable: an
unremarkable name (a protocol write-up called "wire-format"), a name written
without a separator (SecurityPolicy, CodeOfConduct, ADR0001), or one split by a
character outside the separator list ("spec(v2)"). Withholding design is this policy's
choice (RFC5-14 names doctrine, spec, decision and policy text, not design).
Build and tooling files under docs (CMakeLists.txt, requirements*.txt,
robots.txt) are withheld because they are not prose. *Recommended:* accept; the
alternative is a separate closed rule for `governance-text` with its own review.

**Q4. Nested READMEs. Default: the root README, and a README under the docs
or doc folder or directly under the licenses folder.** A README anywhere else
(for example src/README.md) is withheld, because a README below the root
outside docs is often a vendored library's. *Recommended:* accept; for
a project that bundles libraries, those READMEs stay withheld, which is the
safer side.

**The names themselves (fact, not a question).** The names, folders and denylists in the rule are a
proposal [Inferred] from the class text; a file outside them is withheld, never
guessed. Adding a name later is a further version.

## What it does not do

It loosens no secret or active-content screen, grants no consent or egress,
admits no repository, and defines no class (PR #257 does).
