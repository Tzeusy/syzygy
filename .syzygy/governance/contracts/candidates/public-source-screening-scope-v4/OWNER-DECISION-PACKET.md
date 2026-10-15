# Owner decision packet — public-source screening scope, version 4 (P-110)

> **Candidate — binds nothing.** It carries no digest. Nothing here is a
> decision, and no act is performed by reading it. It is offered only after a
> confirming review; until then it is not offered. Rounds 1 to 3 returned
> REVISE and were repaired (`ROUND-1-DISPOSITIONS.md`, `ROUND-2-REPAIR.md`,
> `ROUND-3-REPAIR.md`); round 4 is the one review you ordered on 2026-10-15.

## What this is, in plain words

When Syzygy builds the fidelity review packet for a dossier, it withholds a
whole file if any secret detector matches anywhere in it. In the Redis trial
one badge link on the first line of the README looked like a token, so all 41
README quotations were withheld, and the reviewer could not resolve the rows
that cited them [Observed, from the bead `syzygy-olmr`]. Altogether 140 of 233
cited spans were withheld.

Version 4 withholds only the lines the detector matched, plus one line on each
side, instead of the whole file, when the file is project documentation (a
README, a guide, a changelog) and the match is a password-or-token assignment
or an `http` or `https` URL with a password in it. Source code and every file
that is not project documentation keep today's rule: one match withholds the
whole file. A configuration-like file that the path rules count as
documentation (a `.txt` file under `docs/`, or a root file such as `CHANGES`
with no suffix) is treated as documentation. A quotation that touches a withheld
line is still withheld whole, and its claim stays Unknown. Everything else in
the file can be quoted. Three cases still withhold the whole file: a
private-key match (the detector only sees the key's header line), a known
token format such as an AWS `AKIA…` key id (its secret key sits on another
line that no detector catches), and a key block: `-----BEGIN ` or
`---- BEGIN ` anywhere in the file, even mid-line, any line starting with four
or more dashes and then BEGIN, or the base64 start of a header.

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
  touching what the detectors look for, and only in documentation, where the
  trial's README is. [Inferred] It recovers the README
  quotations that do not include line 1 or 2; the bead does not give their line
  numbers, so how many of the 41 is Unknown.
- **The guide names** do nothing for the Redis trial: none of the five
  unclassified Redis names is on the list [Inferred, from the bead's list]. They
  are there because Polaris should work across projects, and these are the
  usual names of the guides RFC5-14 calls project documentation. They need a
  suffix, so a bare `INSTALL` script is not read as prose. Pick `span` if you
  would rather add names only when a run shows they are needed.

## What it costs

- **The main cost.** A documentation file where a detector matched probably
  holds credentials, and today everything in it is withheld. Under version 4
  a second secret in that file that no detector recognises reaches the review
  packet, an agent session and the draft page, unless it sits on a withheld
  line. These common shapes do, when they appear in a README or guide: an AWS
  secret access key next to a temporary `ASIA…` key id (only `AKIA…` ids keep
  the file whole), a JavaScript `secretAccessKey: "…"`, a Django
  `SECRET_KEY = "…"`, a JSON `"password": "…"`, a `STRIPE_SECRET_KEY` inside a
  heredoc, and a base64-encoded key in a Kubernetes Secret example (unless
  its encoding begins at the key header, which keeps the file whole) [the round-2
  review showed each through the builder's oracle]. So does a password
  in a `postgres://`, `mysql://`, `redis://` or other non-`http` connection
  string, because the URL detector only reads `http` and `https`. Source
  files are not affected: they stay whole-file. A configuration-like file the
  path rules count as documentation is affected like any documentation.
- [Inferred] A secret that a detector catches on one line but that continues
  two or more lines further would have its tail admitted.
- In a file with no match at all nothing changes.

## What stays withheld, and why it is not in this version

- **SECURITY.md and MANIFESTO** (part of 89 spans): a security policy is
  "policy text" and a manifesto is plausibly doctrine, which RFC5-14 calls
  `governance-text`, not project documentation. You withheld both by name in
  version 2. Reading them would need a separate rule for `governance-text` and a
  consent that lists that class.
- **TLS.md**: one project's topic name; a rule for any root `.md` would also
  admit files like AGENTS.md, which govern development.
- **redis.conf**: configuration, not prose; it fits no documentation class.
- **modules/MODULES.md**: a document below the root, outside `docs/`; no rule
  reads those, and adding one is a separate change (nested READMEs are
  withheld in version 2 because they are often a vendored library's, which
  applies here too).
- **00-RELEASENOTES and LICENSE.txt** (10 spans): withheld for active content,
  which this version does not change.
- **Treating withheld rows as non-blocking** (option C, not offered): readiness
  would then be declared over claims whose sources were never read, which VIS-2
  forbids. The author-side warning you chose instead (option D) is merged in
  PR #429.

## Order, as fact

The subject is the policy as version 3 left it, which is the policy on disk
now. Like every policy act, signing breaks both read gates, the public-target
gate and the Butlers gate, until the install re-points them at the new bytes
and teaches the screens the redaction; the install is a separate change
(`IMPACT-LEDGER.md`).

## What it does not do

It admits no repository, grants no consent or egress, changes no detector,
no active-content rule and no class, and edits no specification.
