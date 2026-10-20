# Verbatim committed policy-reader correction probes

Subject: `171e036b969776cb044c00553ad68b6325ccabbf`.

Command:

```text
node reproduce-committed-reader-correction.mjs /absolute/path/to/disposable-built-clone
```

Exit status: 0. Verbatim standard output:

```json
{
  "subject": "171e036b969776cb044c00553ad68b6325ccabbf",
  "previousSubject": "da08266afda81c1493ab61cc2c870cde3b61f336",
  "correctionIsExactlyAggregateRoutingWithListedInWording": true,
  "actualPendingSha256": "7c9162d940e47aa3c1e915965696fdb5c5471c2c36ab0ea4f8b69ed37c8d4047",
  "cases": [
    {
      "name": "committed-corrected-register",
      "expected": "ok",
      "pass": true,
      "policyReader": [
        {
          "actIdentity": "PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V4-APPROVAL-2026-10-20",
          "digest": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd",
          "inForceAt": 1792507717000,
          "until": null
        }
      ],
      "chainState": "ok",
      "chainWhy": null,
      "lastPolicyPath": ".syzygy/governance/decisions/launch-gate/TREND-LOG.md",
      "pendingSha256": "7c9162d940e47aa3c1e915965696fdb5c5471c2c36ab0ea4f8b69ed37c8d4047"
    },
    {
      "name": "previous-frozen-register-in-memory",
      "expected": "refused",
      "pass": true,
      "policyReader": {
        "name": "AdmissionRecordError",
        "code": "invalid-records",
        "message": "invalid-records"
      },
      "chainState": "refused",
      "chainWhy": "invalid-records",
      "lastPolicyPath": ".syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md",
      "pendingSha256": "337e721c234fda106029a42877cb62f6a0808ad820659cb68eec3d78536716da"
    },
    {
      "name": "previous-label-only-routed",
      "expected": "refused",
      "pass": true,
      "policyReader": {
        "name": "AdmissionRecordError",
        "code": "invalid-records",
        "message": "invalid-records"
      },
      "chainState": "refused",
      "chainWhy": "invalid-records",
      "lastPolicyPath": ".syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md",
      "pendingSha256": "ad6e619ae253451e97103e3dac5f9cb4fdec55b2397d0f6577fb1d6fa17716f8"
    },
    {
      "name": "previous-target-only-routed",
      "expected": "refused",
      "pass": true,
      "policyReader": {
        "name": "AdmissionRecordError",
        "code": "invalid-records",
        "message": "invalid-records"
      },
      "chainState": "refused",
      "chainWhy": "invalid-records",
      "lastPolicyPath": ".syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md",
      "pendingSha256": "cab84cf0cdfbe8a7b423f73d0911e832eaf5a3c52bc004171737d5e47c5ac22c"
    },
    {
      "name": "corrected-plus-unknown-withdrawal-filename",
      "expected": "refused",
      "pass": true,
      "policyReader": {
        "name": "AdmissionRecordError",
        "code": "invalid-records",
        "message": "invalid-records"
      },
      "chainState": "refused",
      "chainWhy": "invalid-records",
      "lastPolicyPath": ".syzygy/governance/decisions/PUBLIC-SOURCE-SCOPE-UNKNOWN-WITHDRAWAL-REVIEW-FIXTURE.md",
      "pendingSha256": "7c9162d940e47aa3c1e915965696fdb5c5471c2c36ab0ea4f8b69ed37c8d4047"
    },
    {
      "name": "corrected-plus-unknown-withdrawal-body",
      "expected": "refused",
      "pass": true,
      "policyReader": {
        "name": "AdmissionRecordError",
        "code": "invalid-records",
        "message": "invalid-records"
      },
      "chainState": "refused",
      "chainWhy": "invalid-records",
      "lastPolicyPath": ".syzygy/governance/decisions/ZZ-UNRECOGNIZED-REVIEW-FIXTURE.md",
      "pendingSha256": "7c9162d940e47aa3c1e915965696fdb5c5471c2c36ab0ea4f8b69ed37c8d4047"
    },
    {
      "name": "committed-corrected-restored",
      "expected": "ok",
      "pass": true,
      "policyReader": [
        {
          "actIdentity": "PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V4-APPROVAL-2026-10-20",
          "digest": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd",
          "inForceAt": 1792507717000,
          "until": null
        }
      ],
      "chainState": "ok",
      "chainWhy": null,
      "lastPolicyPath": ".syzygy/governance/decisions/launch-gate/TREND-LOG.md",
      "pendingSha256": "7c9162d940e47aa3c1e915965696fdb5c5471c2c36ab0ea4f8b69ed37c8d4047"
    }
  ]
}
```

Affected-test command:

```text
node_modules/.bin/vitest run packages/polaris-generation-consent/src/real-tree.test.ts packages/polaris-dossier/src/screen.test.ts apps/three-surface-poc/src/polaris-generation/public-source-screening.test.ts --maxWorkers 2 --reporter=json --outputFile ../citation-correction-171e.json
```

Exit status: 0. Verbatim standard output:

```text
JSON report written to /home/tze/.cache/syzygy-p110-install-final-review-2026-10-20/full-6ef149b9-670hm284/citation-correction-171e.json
```

The complete verbatim test JSON is retained as `affected-tests-171e.json` beside this raw; it records 149 passed assertions in three files.
