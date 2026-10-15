# Owner decision packet — public-source screening scope, version 4 (P-110)

> **Candidate — binds nothing.** It carries no digest. Nothing here is a
> decision, and no act is performed by reading it. It is offered only after a
> confirming review; until then it is not offered.

## What this is, in plain words

When Syzygy builds the fidelity review packet for a dossier, it withholds a
whole file if any secret detector matches anywhere in it. In the Redis trial
one badge link on the first line of the README looked like a token, so all 41
README quotations were withheld, and the reviewer could not resolve the rows
that cited them [Observed, from the bead `syzygy-olmr`]. Altogether 140 of 233
cited spans were withheld.

Version 4 withholds only the lines the detector matched, plus one line on each
side, instead of the whole file. A quotation that touches a withheld line is
still withheld whole, and its claim stays Unknown. Everything else in the file
can be quoted. A private-key match still withholds the whole file, because
that detector only sees the key's header line.

This is the kind of redaction RFC5-17 already defines (`redacted-span`) and the
Polaris specification already describes; the policy has simply never turned it
on. So it needs your policy act and nothing else: no contract or specification
change.

## The one question

**Sign screening scope version 4? Pick a variant, or decline.**

| Variant | What it does | Recommended |
|---|---|---|
| `span-guides` | The line-level redaction, and root guide files with a `.md`, `.rst` or `.txt` suffix become readable as project documentation: INSTALL, BUILDING, HACKING, USAGE, TUTORIAL, OVERVIEW, GETTING-STARTED, UPGRADING, MIGRATION, TROUBLESHOOTING, SUPPORT, CONTRIBUTORS, CREDITS and a few spellings of those | **Yes** |
| `span` | The line-level redaction only | |
| decline | Nothing changes; whole-file withholding stays | |

The words for the recommended choice: **"Sign screening scope version 4,
variant span-guides"**. The variant names the manifest row; a recorder,
frozen only after a confirming review, takes that row as the act's argument.

## Why this recommendation

- **The redaction** fixes the largest single cause in the trial without
  touching what the detectors look for. [Inferred] It recovers the README
  quotations that do not include line 1 or 2; the bead does not give their line
  numbers, so how many of the 41 is Unknown.
- **The guide names** do nothing for the Redis trial: none of the five
  unclassified Redis names is on the list [Inferred, from the bead's list]. They
  are there because Polaris should work across projects, and these are the
  usual names of the guides RFC5-14 calls project documentation. They need a
  suffix, so a bare `INSTALL` script is not read as prose. Pick `span` if you
  would rather add names only when a run shows they are needed.

## What it costs

- [Inferred] A secret that a detector catches on one line but that continues
  two or more lines further would have its tail admitted; today the whole file
  is withheld in that case. Secrets the detectors never match are admitted
  either way, as today.
- Lines near a secret, beyond the guard line, can now reach the review packet,
  an agent session and the draft page.

## What stays withheld, and why it is not in this version

- **SECURITY.md and MANIFESTO** (part of 89 spans): a security policy is
  "policy text" and a manifesto is plausibly doctrine, which RFC5-14 calls
  `governance-text`, not project documentation. You withheld both by name in
  version 2. Reading them would need a separate rule for `governance-text` and a
  consent that lists that class.
- **TLS.md**: one project's topic name; a rule for any root `.md` would also
  admit files like AGENTS.md, which govern development.
- **redis.conf**: configuration, not prose; it fits no documentation class.
- **modules/MODULES.md**: a document below the root, outside `docs/`; version
  2 withholds those because they are often a vendored library's.
- **00-RELEASENOTES and LICENSE.txt** (10 spans): withheld for active content,
  which this version does not change.
- **Treating withheld rows as non-blocking** (option C, not offered): readiness
  would then be declared over claims whose sources were never read, which VIS-2
  forbids. The author-side warning you chose instead (option D) is merged in
  PR #429.

## Order, as fact

The subject is the policy as version 3 left it, which is the policy on disk
now. Like every policy act, signing breaks the public-target read gate until
the install re-points it at the new bytes and teaches the screens the
redaction; the install is a separate change (`IMPACT-LEDGER.md`).

## What it does not do

It admits no repository, grants no consent or egress, changes no detector,
no active-content rule and no class, and edits no specification.
