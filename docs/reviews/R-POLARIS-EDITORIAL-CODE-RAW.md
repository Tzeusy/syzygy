REVISE

Reviewed exact diff `f585c5a..5f4574c26aaaaa9e0622766ac60c3445bee9586c`.

1. **P1 — Architecture excerpts omit qualifications.** `apps/three-surface-poc/src/polaris-reading.ts:79` selects later paragraphs only through structural state or the prefix vocabulary at line 48. [Observed] Calling `projectReading` with:
   ```text
   Process Model

   Workers share records.

   Access requires explicit approval.

   Storage Model

   Records persist.
   ```
   produces a summary retaining “Workers share records.” and dropping “Access requires explicit approval.” The complete disclosure retains it, but PWB-REQ-011 requires “A reader who stops at any level SHALL retain a true, coarser account.” An excerpt label does not preserve that qualification. Retain complete sections unless omission safety is established; expanding the keyword list cannot establish it.

2. **P2 — Literal Markdown code is transformed and loses content.** `apps/three-surface-poc/src/polaris-markdown.ts:145` treats indented code as a paragraph and passes it through inline interpretation at line 152. [Observed] Input `    [literal](must-retain) **literal**` returns `<p>    literal <strong>literal</strong></p>`: the literal destination disappears and literal asterisks become formatting. Additionally, line 23 accepts a matching substring inside a longer backtick run: input `` `a``[literal](must-retain)` `` becomes two code elements and loses the interior backticks. Preserve indented code literally and require equal-length delimiter runs for inline code. Add regression cases covering both.

[Observed] Focused validation passed: five files, 51 tests covering Markdown, reading, copy, project shape and first reading. The counterexamples above were executed separately and are not covered by those passing tests.

[Inferred] The CSS navigation scoping and unchanged Unknown branches appear appropriate. Validation limits: no live admitted-source fidelity comparison, browser captures, full demo, canonical clone battery or owner walkthrough was performed by this reviewer. No Butlers checkout was read; no files were edited.
