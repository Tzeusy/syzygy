# Review — PWB behavior recorder: opening-band wiring, round 2
Reviewed commit: 4c7f6e243849738f59f03720945811b8d2aa2608
Manifest SHA-256: n/a (recorder review; bound by commit, see line 2)
Verdict: CONFIRM WITH EXCEPTIONS

Method: detached worktree at the reviewed commit; `git diff main 4c7f6e2`; adversarial packets built from the real packet and fed to `validate_split_phrase` (script: scratchpad `adv.py`); mutants run against `--selftest` (scratchpad `mut.py`). Regexes via Python `re`, not grep.

## Criteria

1. F1 fixed: PASS. The real packet validates. Adversarial results (argument = real digest):
   - Rejected: fenced heading, tilde-fenced heading, indented (4-space) heading, blockquoted heading, fully commented heading, CRLF line endings (fail-closed), heading with trailing text, digest under a different heading name ("Other SHA-256:"), uppercase hex, two headings where the second carries a wrong digest, unclosed fence before the heading, label only inside a fence.
   - Pass, legitimate: real heading plus a trailing comment; two headings where the second is fenced (example); heading inside `<pre>` (renders visibly); nested `<!-- a <!-- b -->` before a visible heading (CommonMark ends the comment at the first `-->`); a `<!-- -->` before the digest on its line (digest still visible).
   - Pass, mislead: an unterminated `<!--` opened before the heading (or heading then `<!-- open`). See Finding 1.
2. Pins: PASS. Commit 3369410 is on main's ancestry; the packet bytes at 3369410 equal the tree's (cmp); the package dir is identical between 9162d62 (round 11) and 3369410 except the disposition file; the disposition sha256 of the tree file is 0cc80226...1fea as pinned; `## Findings` is a unique heading in the round-10 raw; the builder `--check` passes. `--selftest`: 69 fixtures, 0 failing. The non-opening-band selftest lines are identical to main's (old 51 vs new 69 differ only by the new count and the opening-band lines).
3. Rule 6 (mutant: old -> new, outcome):
   - fence strip removed -> killed (fenced fixture); comment strip removed -> killed; label check `if False` -> killed; whole-phrase check `if False` -> killed; `len != 1` -> `< 1` -> killed; binds-argument check `if False` -> killed; same-line digest (newline made optional) -> killed; manifest constants `!= 1` -> `< 1` and `== 0` -> killed; dispatch to split validator disabled -> killed; `split_phrase_packet=False` -> killed; disposition pin digit altered -> killed; `## Findings` -> `## Finding` -> killed.
   - SURVIVED: label code-span requirement loosened to bare `act.label in text`; heading `^` anchor removed; blank-line skip `(?:[ \t]*\n)*` removed. See Finding 2.
4. `check_governance.py`: 31 OK, 21 WARN, 0 FAIL. Diff touches only the recorder and the retained round-1 raw.
5. Docstring: true with one qualification. "Fenced code and HTML comments are blanked first" holds for closed comments only (Finding 1). The other sentences (exactly one heading, next non-blank line, label in a code span, no whole phrase, two constants refused) match the code.

**Finding 1 — unterminated HTML comment is not blanked, unlike an unterminated fence** (note)
`<!--.*?-->` needs a terminator; an open `<!--` before the heading leaves it counted while a renderer hides it (CommonMark runs an unterminated comment block to the end). `_strip_fenced_code` treats the unterminated fence as running to end, so the two are asymmetric. Reachable only by a drafter hiding the heading in a packet whose bytes are pinned by commit and reviewed; the owner is also shown the whole phrase at the act. Suggest blanking from an unmatched `<!--` to end of text.

**Finding 2 — three predicates lack a discriminating fixture** (note)
Survivors listed in criterion 3: bare (non-code-span) label mention; mid-line or blockquoted `Manifest SHA-256:` (the blockquote case is rejected today only because the `^` anchor exists, untested); blank line between heading and digest (the docstring promises it; the real packet has none). Add one fixture each.

**Finding 3 — CRLF packets are refused with a misleading message** (note)
A CRLF packet yields "0 Manifest SHA-256 headings". Fail-closed and correct, but the message does not say why. The real packet is LF.
