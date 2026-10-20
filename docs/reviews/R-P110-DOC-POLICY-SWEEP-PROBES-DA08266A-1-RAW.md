# Verbatim policy-reader isolation results

Subject: `da08266afda81c1493ab61cc2c870cde3b61f336`.

Command:

```text
node reproduce-reader-isolation.mjs /absolute/path/to/disposable-built-clone
```

Exit status: 0. Verbatim standard output:

```json
{
  "subject": "da08266afda81c1493ab61cc2c870cde3b61f336",
  "pendingPath": ".syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md",
  "literalFilenameOccurrences": 2,
  "nativeOriginalSha256": "337e721c234fda106029a42877cb62f6a0808ad820659cb68eec3d78536716da",
  "cases": [
    {
      "name": "frozen-original",
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
      "name": "only-label-routed",
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
      "name": "only-link-target-routed",
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
      "name": "both-label-and-target-routed-to-aggregate",
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
      "pendingSha256": "770d11c1c3cf1ac3cf1b2fbb270dbe5253189134d5dedf80b50fcdb1fdc13d11"
    },
    {
      "name": "pending-blank-isolation-only",
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
      "pendingSha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "name": "routed-plus-unknown-withdrawal",
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
      "pendingSha256": "770d11c1c3cf1ac3cf1b2fbb270dbe5253189134d5dedf80b50fcdb1fdc13d11"
    },
    {
      "name": "original-restored",
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
    }
  ]
}
```
