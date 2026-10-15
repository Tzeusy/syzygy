# Round 2 classification — public-source screening scope, version 4

> **Candidate — binds nothing.** Raw: `docs/reviews/R-OLMR-SCREENING-SCOPE-V4-2-RAW.md`,
> verdict line 5: `Verdict: REVISE`, over commit `9caa9043` (main after PR
> #453). One revise finding and four notes. **Nothing is repaired.** Under
> the lead's round-2 direction (a REVISE is classified, not repaired, and the
> lane stops), the package bytes are left exactly as round 2 read them, they
> carry no confirmation, and P-110 is **not offered**.

| Finding | Severity | Classification (not repaired) |
|---|---|---|
| 1 — the packet's cost statement reads as a long tail; six common credential shapes (an `ASIA` AWS key id with its secret key, JS `secretAccessKey`, Django `SECRET_KEY`, quoted JSON `"password"`, a heredoc `STRIPE_SECRET_KEY`, a base64 private key in a Kubernetes Secret) keep the secret line where version 3 withheld the file | revise | **Design question, not wording only.** Two repair arms the raw names: (a) state the shapes plainly in the delta and packet and write `AKIA` where the packet says "an AWS key id"; (b) narrow the redaction to `project-documentation` bodies, where the trial's 41 README spans are, keeping code-content whole-file. Arm (b) changes the policy bytes and the manifest rows. Which arm is the next lane's (or the owner's) choice |
| 2 — the disclosed residuals reproduce as stated | note | Confirms the stated residual; no change needed |
| 3 — "Any PEM header" is wider than the literal `-----BEGIN ` fragment (a four-dash SSH2 key passes) | note | Wording or fragment list to be corrected with finding 1's repair |
| 4 — the builder's module docstring describes the pre-round-1 rule | note | Docstring to be updated with finding 1's repair |
| 5 — nine policy-path files are neither named nor dispositioned in the ledger; the every-offset scan's cost is unnamed | note | Ledger addition with finding 1's repair; install-time assessment |

Next lawful step: one repair lane for finding 1 (choosing arm (a) or (b)), carrying notes 3 to 5, followed by a round 3.
