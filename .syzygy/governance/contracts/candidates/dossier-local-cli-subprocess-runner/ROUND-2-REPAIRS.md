> **Candidate — binds nothing.** Repair map for review round 2. A repair
> performs no act; only the owner's version-tag sign-off of the one-command
> run change binds `SEMANTIC-DELTA.md` (VIS-4).

# Round 2 repairs — DOSSIER-CLI-RUNNER-1

Raw: `docs/reviews/R-DOSSIER-CLI-SUBPROCESS-2-RAW.md`, verdict `REVISE`
(line 4). Classification: `ROUND-2-DISPOSITIONS.md`, which stays unedited.

The lead directed one repair under the owner's autonomy direction (cycle 3):
take the fail-closed arm for finding 1, repair notes 2 to 5, and leave note 6
to the owner. One fresh-context round 3 follows. A notes-only round clears
these bytes, and P-111 is then owner-ready. A `REVISE` is classified, nothing
is repaired, and the lane stops.

| # | Class | Repair in `SEMANTIC-DELTA.md` |
|---|---|---|
| 1 | revise | Arm (a), fail-closed. In paragraph 2, before any session starts, Syzygy reads only the provider-relevant keys of the tool's administrator-managed settings, environment block included, at the locations the declared tool and version document. A key that names or could select another provider, endpoint or credential route refuses the run, naming the key and file. A location that exists but cannot be read or parsed refuses the run, and so does a tool version whose provider-relevant managed keys are not known; in both cases the effective provider and every dependent claim are Unknown. The launch record holds each location checked, whether it was present, and the keys found, by name. New scenario: "Managed settings redirect or cannot be read". The Case seeds a managed `env` redirect in an attended run and an unreadable layer, and the Falsifier fires when a run starts under either. |
| 2 | note | The lead's direction differs from the round-2 disposition's "admit no credential variable" wording. The allow-list now admits no variable that selects, redirects or authenticates a provider, with one exception: the single variable the operator names in the run declaration for the declared provider. It is passed unparsed and its value is never logged, stored or transmitted. Its name is in the launch record, which records it by name only and leaves its value out of the environment digest, and the run page discloses it. The credential clause excepts this pass-through, and the `--bare` row says the variable is the tool's own authentication, optional, with no API call by Syzygy. The Falsifier covers any other authenticating variable and any appearance of the declared variable's value. |
| 3 | note | The oracle, the "No provider client" scenario and the Falsifier now name the same two exceptions: the copy of the tool's own credential file and the pass-through of the declared variable. |
| 4 | note | Paragraph 2's excluded sources now name skills, custom agents, custom commands and output styles, in the operator's home and in every readable directory including the clone, other than the skills Syzygy names. The clone scenario, the Case and the Falsifier name them too. |
| 5 | note | Paragraph 1 takes the executable from the declaration alone, never from an environment variable, and a test stand-in is declared by absolute path. New scenario: "Stand-in taken from the environment". The Case seeds `SYZYGY_POLARIS_AGENT` naming another executable. Downstream impact says `polaris.ts` stops resolving it from the environment. |
| 6 | note | Not repaired: it is the owner's choice, P-111 Q2. |

The Review section of `SEMANTIC-DELTA.md` records this round.
