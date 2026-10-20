# P-110 authority correction — verbatim probe command output
Reviewed commit: `efcbb78f28be88043d8dc3edffa6f153cafff724`
Command: `node --disable-warning=ExperimentalWarning reproduce-authority.mjs`
Exit status: 0

```text
┌─────────┬────────────────────────────────────────┬────────────────┬───────────────────┬────────────────────────────┬────────┬──────────────────────────────────────────┐
│ (index) │ id                                     │ expectedAdmits │ explicitSelection │ preChangeExplicitSelection │ admits │ caseId                                   │
├─────────┼────────────────────────────────────────┼────────────────┼───────────────────┼────────────────────────────┼────────┼──────────────────────────────────────────┤
│ 0       │ 'legacy-affirmative'                   │ true           │ true              │ true                       │ true   │ null                                     │
│ 1       │ 'v4-affirmative'                       │ true           │ true              │ false                      │ true   │ null                                     │
│ 2       │ 'recorder-assertion'                   │ false          │ false             │ false                      │ false  │ 'policy:state-1-not-explicitly-selected' │
│ 3       │ 'owner-words-without-explicit'         │ false          │ false             │ false                      │ false  │ 'policy:state-1-not-explicitly-selected' │
│ 4       │ 'no-selection'                         │ false          │ false             │ false                      │ false  │ 'policy:state-1-not-explicitly-selected' │
│ 5       │ 'negated-v4-selection'                 │ false          │ false             │ false                      │ false  │ 'policy:state-1-not-explicitly-selected' │
│ 6       │ 'never-v4-selection'                   │ false          │ false             │ false                      │ false  │ 'policy:state-1-not-explicitly-selected' │
│ 7       │ 'quoted-v4-example'                    │ false          │ false             │ false                      │ false  │ 'policy:state-1-not-explicitly-selected' │
│ 8       │ 'negated-legacy-selection-preexisting' │ false          │ false             │ true                       │ false  │ 'policy:state-1-not-explicitly-selected' │
│ 9       │ 'v4-only-after-head'                   │ false          │ false             │ false                      │ false  │ 'policy:state-1-not-explicitly-selected' │
│ 10      │ 'missing-provenance'                   │ false          │ null              │ null                       │ false  │ 'policy:provenance-state-missing'        │
│ 11      │ 'malformed-provenance'                 │ false          │ null              │ null                       │ false  │ 'policy:provenance-state-malformed'      │
└─────────┴────────────────────────────────────────┴────────────────┴───────────────────┴────────────────────────────┴────────┴──────────────────────────────────────────┘
{
  "reviewHead": "efcbb78f28be88043d8dc3edffa6f153cafff724",
  "caseCount": 12,
  "matched": 12,
  "failed": 0,
  "actualFrozenActParsedProvenance": {
    "kind": "present",
    "value": {
      "label": "owner-adopted (bootstrap, uncorrelated)",
      "explicitSelection": true
    }
  }
}
```

Stderr:

```text
```

Independent Python audit:

```json
{
  "reviewHead": "efcbb78f28be88043d8dc3edffa6f153cafff724",
  "correctionPredecessor": "f16ab18f448ee8a443ec67b2e7cc4c6a545583f4",
  "sameCaseDefinitionsExceptHead": true,
  "caseIds": [
    "legacy-affirmative",
    "v4-affirmative",
    "recorder-assertion",
    "owner-words-without-explicit",
    "no-selection",
    "negated-v4-selection",
    "never-v4-selection",
    "quoted-v4-example",
    "negated-legacy-selection-preexisting",
    "v4-only-after-head",
    "missing-provenance",
    "malformed-provenance"
  ],
  "matched": 12,
  "mismatchIds": [],
  "unchangedFrozenActSha256": "bd7e386c733f2c25f3cf611db277af14cdf28a7dbb576c1c5145233ac9e9ebd3",
  "unchangedFrozenActGitBlob": "727efcd1f2c64c04f6d451c1b3a506e3c720a9ba",
  "unchangedEvaluatorSha256": "647a9583590ead29fb7d82ef4689470fdaaac24be0ba58769c2bf2cba361c002",
  "unchangedArtifactExtractorSha256": "01fc903901fc09082ce4923bf7bdcf4937b492ef93e62058be5a7c04ca87395e"
}
```
