> **Candidate — binds nothing.** Dispositions of the round-2 notes on this
> package. It is a sibling record beside the confirmed bytes, not part of
> them: under the owner ruling of 2026-09-26 (a notes-only round clears the
> exact bytes it read) the notes are answered here and the package is not
> edited. It carries no verdict and performs no act.

# Round-2 dispositions — RFC5-14 `project-documentation` class

Reviewed record: .syzygy/governance/contracts/candidates/rfc5-project-documentation-class/reviews/R-RFC5-PROJECT-DOCUMENTATION-CLASS-2-RAW.md

Revise-severity findings: 0

The raw's verdict of record is CONFIRM WITH EXCEPTIONS, three findings, all
`note`. It read commit dff2f0dc5cf6b8a876c4d4233cb0bef8e3e7dce4; the package
bytes it read are unchanged. This record quotes no digest.

**Finding 1 — "exactly one class" scope; the notebook account**


Accepted as a reading; no byte changes. [Inferred] The first half of the
signals sub-bullet ("a file the policy cannot place in exactly one class is
undeterminable and fails closed (RFC5-15)") speaks of any file, not only this
class. It restates RFC5-15 part 2 and the unchanged composite rule for every
class, so it is Clarifying and widens no consent. The delta's notebook
paragraph is incomplete in the way the reviewer says: under the composite rule
a policy may place a whole notebook in its highest embedded class (for example
`code-content`) as one class, which neither splits it nor fails closed. The
owner reads both corrections here; if the owner wants either in the text, that
is option (b) of the packet and a redraft with a new review.

**Finding 2 — the manifest header and the digest an act binds**


Accepted. The manifest header's sentence that rows bind "by the owner act that
names this file's digest" describes the typed-phrase form (packet option 2).
The recommended form, option 1, binds the manifest row, and the act recorder
(`scripts/record_rfc5_project_documentation_act.py`) is written to that form:
its argument is the manifest row, its confirmation check binds the raw's head
`Manifest SHA-256:` to the manifest file's digest, and it refuses a file digest
given as the argument. The header is not edited here, because editing it
changes the file digest the confirming raw's head binds. If the owner chooses
option 1, the act record states in its ceremony section that the act binds the
row and that the header describes the other form. If the owner chooses
option 2, the typed phrase names the file digest and the recorder takes the
file digest instead; the install change re-renders the header to match the
chosen form either way, with a new digest-binding review.

**Finding 3 — the 64-hex criterion and retained raws**


Accepted. Brief criterion 9's "no 64-hex digest may appear in any Markdown
file of the package" is read as excluding retained `-RAW.md` files, whose
four-line head must carry the manifest file's digest by the brief's own
recording rule; `check_governance.py` exempts the `-RAW.md` suffix. The brief
is not edited. Any later round's brief should state the exemption.
