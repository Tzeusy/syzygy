# Review — PWB behavior recorder: opening-band wiring and split-phrase packets
Reviewed commit: e236d5cc71656db6f1c2f8633e28431123782799
Manifest SHA-256: n/a (recorder review; bound by commit, see line 2)
Verdict: REVISE

Method: detached worktree at the commit; `git diff main e236d5c` (1 file, +122/-3); selftest, check_governance, hand-built packets, 8 scripted mutants of the recorder (restored after; worktree clean).

**Finding 1 — revise-severity. `validate_split_phrase` accepts a digest heading inside a fenced code block.**
Evidence: with the label present, `validate_split_phrase(f"`{label}`\n```\nManifest SHA-256:\n`{d}`\n```\n", act, d)` returns without error. The regex runs over raw text with no fence stripping, so a packet whose only digest heading sits in an example fence (not shown to the owner as the offered digest) binds. The recorder already has fence-stripping code for raws/dispositions. The real packet has no fence before line 60 (its only fences are lines 344/347), so stripping fences first would not refuse it. Criterion 2 FAIL on this construction.

**Finding 2 — note. The label check is satisfied by an incidental mention; it does not prove the owner is shown the label.**
Evidence: `OWNER-DECISION-PACKET.md:317` is the packet's only occurrence of `` `SIGN OFF PWB OPENING-BAND SCENARIO` ``. It sits in a description of future builder constants, not an offered phrase. A label inside an HTML comment also passes. The recorder cannot be strengthened without failing the real, round-11-bound packet, so this is a limit, not a defect. The act session must show the owner the whole `LABEL: digest` phrase explicitly. The comment at Act.split_phrase_packet ("shown to the owner whole at the act") should say that is the session's duty, not a validator guarantee.

**Finding 3 — note. The module docstring is stale.**
It still says "No `ACTS` entry currently names a `disposition_record` or `raw_findings_heading`; wiring one is a later, separately reviewed change." `opening-band` now does. The docstring also does not document `split_phrase_packet` or its predicates.

**Finding 4 — note. No fixture exercises the `manifest` exactly-one rule (criterion 4).**
Mutant M7 (`if len(names) != 1:` -> `if False:`) survives: 0 fixtures fail. Soundness by inspection: render-mode's builder defines only BEHAVIOR_OUT and opening-band's only MANIFEST_OUT, so both resolve. A builder naming both or neither would raise ValueError (`names` has 2 or 0 entries). Loud but unmutation-tested. Low risk.

**Finding 5 — note. The `continue` for case-(b) acts skips two generic fixtures and all render checks for opening-band.**
Skipped: "review markers outside the four-line head rejected" and the render_act / render_aggregate_block paths. The opening-band act's rendered record is never exercised in selftest. The head check (`lines[:4]`, not the first four non-blank lines) is shared code and unchanged.

**Finding 6 — note. Regex mutant survival.**
M8 (making the newline after the heading optional) survives. No fixture builds a same-line "Manifest SHA-256: `digest`" packet. Fail-closed direction is weak either way; covered only by construction.

Criteria results:
1. PASS. Commit 3369410 is on main. Packet and manifest bytes there equal the tree (`cmp` identical). The raw's first four lines bind `Manifest SHA-256: 7f80cb05...5c46` and `Verdict: CONFIRM WITH EXCEPTIONS`. `sha256sum ROUND-11-DISPOSITIONS.md` = 0cc80226...1fea, which matches the pin. `## Findings` is at raw line 67 and owns findings 49-52 (selftest "real round-11" PASS). `Reviewed record:` and `Revise-severity findings: 0` live in the disposition (lines 52, 54). The raw's "Reviewed commit" (9162d62) is provenance only.
2. FAIL (finding 1; finding 2 as limit). Rejected as required: other digest, two headings, quote-prefixed heading, CRLF, trailing text, lowercase heading, uppercase digest, label spelled differently, whole phrase also present.
3. PASS. The render-mode branch still runs the CONFIRM-only render hashes (selftest lines ~1660-1675); `validate_packet` only adds an `if` whose else is the old `count != 1` line; the diff touches no render code.
4. PASS by inspection; see finding 4 (unmutation-tested).
5. Mutants (scratch copy, restored):
   - M1 `if f"`{act.label}`" not in packet_text:` -> `if False:`; caught by "split packet without the label rejected".
   - M2 whole-phrase check -> `if False:`; caught by "also carrying a whole phrase".
   - M3 `!= 1` -> `== 0`; caught by "two split digest headings".
   - M4 `headings[0] != argument` -> `False`; caught by "bound to another digest".
   - M5 dispatch `if getattr(...)` -> `if False:`; 9 fixtures fail.
   - M6 disposition pin digest last char altered; caught by "notes-only verdict binds" (the dedicated "edited disposition rejected by its pin" still passes because any pin mismatch refuses).
   - M7 manifest length check off; SURVIVES (finding 4).
   - M8 newline after heading made optional; SURVIVES (finding 6).
6. Selftest: "64 recording fixtures, 0 failing". check_governance: "31 OK, 21 WARN, 0 FAIL (52 checks)". `--check opening-band 7f80cb05...5c46 --date 2026-10-01` prints `FAILED: manifest row does not hash the tree: openspec/changes/polaris-project-wide-butlers-model/GOVERNING-DEPENDENCIES.md`. Expected pre-act: the manifest hashes post-apply bytes, and no act exists.
7. PASS. The diff touches only `scripts/record_pwb_behavior_amendment_acts.py`. It adds an Act entry, a validator, and fixtures. No record is written and no act performed.
