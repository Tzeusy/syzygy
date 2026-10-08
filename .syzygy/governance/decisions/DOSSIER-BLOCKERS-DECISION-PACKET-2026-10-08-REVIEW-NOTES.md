# Review notes — owner decision packet for the Redis dossier blockers

> **Candidate — binds nothing.** This record dispositions review notes. It
> performs no act, records no ruling and changes no reviewed byte.

Subject: `DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md` in this directory,
with register rows P-105 to P-107 and their dated note in
`PENDING-OWNER-DECISIONS.md`, at commit `897910fc`.

Review: round 2, `docs/reviews/R-PR404-DOSSIER-BLOCKERS-2-RAW.md`, verdict
`CONFIRM WITH EXCEPTIONS` (raw line 2). It has no revise-severity finding,
only three findings marked low (N1, N3, N4) and two notes (N2, N5). Under the
owner's notes-only rule
(`POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1), that round clears the
bytes it read. The notes are therefore recorded here, and the packet and the
register rows are left unedited.

Read the packet together with these corrections. Each one supersedes the
packet wording it names, for a reader of the packet.

## N1 — "No review has run" in the register (low)

`PENDING-OWNER-DECISIONS.md` rows P-105 and P-106 say "No review has run;
offered only after a confirming one." The register's dated note says no
review has run on either candidate package. Both were true at the first
commit and stopped being true once the packet's round 1 ran.

**Read as:** no *confirming* review of either candidate package has run.
Each package's own review state is in `docs/README.md`'s campaign table, and
each decision is still offered only after a confirming review of its package.

## N2 — the dated note names the pre-rebase base (note)

The register's dated note counts over `origin/main` `56c6c98c`. The branch
has since been rebased onto later main commits. The register's rows did not
change across those rebases, so the count of 34 open rows, 5 acceptance-act
rows and 39 in all still holds. The base named in the note is the one the
count was first taken over.

## N3 — "the HTML check" is narrower than the exemption (low)

The packet calls the lifted step "the HTML check", in decision 1 and in row
P-105. The scan lifted for an exempt code file also looks for:

- `javascript:`, `vbscript:`, `data:` and `file:` links;
- event-handler attributes;
- HTML comments and declarations;
- obfuscated link destinations;
- `script` and `svg` elements;
- unclosed code contexts.

**Read as:** "the active-content check (HTML tags, script, event handlers and
unsafe links)". A JavaScript file holding an `onclick=` string or a
`javascript:` URL is admitted under variant `all` as well. The page guard
still prevents any such bytes from becoming a link, element, attribute, script
or handler, and the base render rule still binds them [Inferred].

Where decision 1 says "under a policy whose `default-src` is `'none'`", the
policy meant is the page's Content-Security-Policy, not the screening policy.
Since the package's own round-1 review, that page policy must also be
enforced, delivered before any of the file's bytes, and list exactly `'none'`
for `default-src` (the package's `SEMANTIC-DELTA.md`).

## N4 — what an unattended run still needs from the authoring session (low)

Option B's "Yes, for the helper sessions" is accurate about the helpers. For
a run to progress while you are away, the authoring session must also keep
going after each verdict. That means it too runs unattended, with its tools
pre-approved. It carries the same security cost the B row states for the
helpers, over a wider tool set, since it drafts and runs `syzygy dossier`
steps. Option B alone does not make an overnight run progress unless you
also leave the authoring session running that way.

## N5 — an unlabelled consequence (note)

Decision 2's "README-based claims then cannot be reviewed and render Unknown"
is [Inferred], as the provider package's delta labels it.

## Also carried forward

The provider package's own round-1 review
(`docs/reviews/R-DOSSIER-AGENT-PROVIDER-V2-1-RAW.md`, finding 6) found the
same over-statement in that package's delta, and it applies equally to row
P-106's "inventory and review packets". **Read
as:** the fidelity review packet and the rendered site the design review
packet carries. The inventory brief carries no target bytes.
