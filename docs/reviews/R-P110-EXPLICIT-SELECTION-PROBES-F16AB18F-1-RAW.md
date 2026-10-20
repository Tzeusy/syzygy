# Preliminary authority probes — verbatim command output
Reviewed commit: `f16ab18f448ee8a443ec67b2e7cc4c6a545583f4`
Command: `node --disable-warning=ExperimentalWarning reproduce-authority.mjs`
Exit status: 1

```text
┌─────────┬────────────────────────────────────────┬────────────────┬───────────────────┬────────────────────────────┬────────┬──────────────────────────────────────────┐
│ (index) │ id                                     │ expectedAdmits │ explicitSelection │ preChangeExplicitSelection │ admits │ caseId                                   │
├─────────┼────────────────────────────────────────┼────────────────┼───────────────────┼────────────────────────────┼────────┼──────────────────────────────────────────┤
│ 0       │ 'legacy-affirmative'                   │ true           │ true              │ true                       │ true   │ null                                     │
│ 1       │ 'v4-affirmative'                       │ true           │ true              │ false                      │ true   │ null                                     │
│ 2       │ 'recorder-assertion'                   │ false          │ false             │ false                      │ false  │ 'policy:state-1-not-explicitly-selected' │
│ 3       │ 'owner-words-without-explicit'         │ false          │ false             │ false                      │ false  │ 'policy:state-1-not-explicitly-selected' │
│ 4       │ 'no-selection'                         │ false          │ false             │ false                      │ false  │ 'policy:state-1-not-explicitly-selected' │
│ 5       │ 'negated-v4-selection'                 │ false          │ true              │ false                      │ true   │ null                                     │
│ 6       │ 'never-v4-selection'                   │ false          │ true              │ false                      │ true   │ null                                     │
│ 7       │ 'quoted-v4-example'                    │ false          │ true              │ false                      │ true   │ null                                     │
│ 8       │ 'negated-legacy-selection-preexisting' │ false          │ true              │ true                       │ true   │ null                                     │
│ 9       │ 'v4-only-after-head'                   │ false          │ false             │ false                      │ false  │ 'policy:state-1-not-explicitly-selected' │
│ 10      │ 'missing-provenance'                   │ false          │ null              │ null                       │ false  │ 'policy:provenance-state-missing'        │
│ 11      │ 'malformed-provenance'                 │ false          │ null              │ null                       │ false  │ 'policy:provenance-state-malformed'      │
└─────────┴────────────────────────────────────────┴────────────────┴───────────────────┴────────────────────────────┴────────┴──────────────────────────────────────────┘
{
  "reviewHead": "f16ab18f448ee8a443ec67b2e7cc4c6a545583f4",
  "caseCount": 12,
  "matched": 8,
  "failed": 4,
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
