# Retained independent code/security execution evidence

Subject: `1cdb74805f09d647a9ba42a7dc9db124b53c7709`.

The JSON files in this packet are the verbatim test and probe output. The reviewer's narrative is in the sibling code/security raw. No claim of full canonical clone battery or hosted CI is made.

Focused Vitest standard output (exit 0):

```text
JSON report written to /home/tze/.cache/syzygy-p110-install-final-review-2026-10-20/full-6ef149b9-670hm284/focused-code-security-1cdb.json
```

Independent Important replay standard output (exit 0):

```text
JSON report written to /home/tze/.cache/syzygy-p110-install-final-review-2026-10-20/full-6ef149b9-670hm284/independent-security-probes-1cdb.json
```

Independent 16-case population probe output, verbatim:

```json
[
  {
    "name": "full mixed control",
    "expected": "accept",
    "status": "awaiting-rendered-review",
    "reason": null,
    "calls": 5,
    "verificationCalls": 1,
    "originalRows": 6,
    "requestedRows": 6,
    "originalOpaqueRows": 4,
    "requestOpaqueRows": 4,
    "leakedWithheld": false,
    "planSourceIds": [
      "s-20aeb0270c99efeb3752a94e",
      "s-3a166a1445aab5722f94f831",
      "s-3e4c1d4fd6f855b976f61b75",
      "s-4f9574f5ef95c6f38494ec1b",
      "s-a23b1aa9450025ca45fb6a4a",
      "s-e9d7c101371a2144f090e81a"
    ],
    "requestedIds": [
      "s-20aeb0270c99efeb3752a94e",
      "s-3a166a1445aab5722f94f831",
      "s-3e4c1d4fd6f855b976f61b75",
      "s-4f9574f5ef95c6f38494ec1b",
      "s-a23b1aa9450025ca45fb6a4a",
      "s-e9d7c101371a2144f090e81a"
    ],
    "policySha256": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd"
  },
  {
    "name": "reordered complete population",
    "expected": "accept",
    "status": "awaiting-rendered-review",
    "reason": null,
    "calls": 5,
    "verificationCalls": 1,
    "originalRows": 6,
    "requestedRows": 6,
    "originalOpaqueRows": 4,
    "requestOpaqueRows": 4,
    "leakedWithheld": false,
    "planSourceIds": [
      "s-237e36002ce91340ff442fde",
      "s-3a166a1445aab5722f94f831",
      "s-4f9574f5ef95c6f38494ec1b",
      "s-6db7e35474d61135385ea5f0",
      "s-6de3ad4c02cd5da506388acc",
      "s-a6dd452ad6b8750ecb3d8994"
    ],
    "requestedIds": [
      "s-237e36002ce91340ff442fde",
      "s-3a166a1445aab5722f94f831",
      "s-4f9574f5ef95c6f38494ec1b",
      "s-6db7e35474d61135385ea5f0",
      "s-6de3ad4c02cd5da506388acc",
      "s-a6dd452ad6b8750ecb3d8994"
    ],
    "policySha256": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd"
  },
  {
    "name": "four opaque alias changes",
    "expected": "accept",
    "status": "awaiting-rendered-review",
    "reason": null,
    "calls": 5,
    "verificationCalls": 1,
    "originalRows": 6,
    "requestedRows": 6,
    "originalOpaqueRows": 4,
    "requestOpaqueRows": 4,
    "leakedWithheld": false,
    "planSourceIds": [
      "s-3a166a1445aab5722f94f831",
      "s-4f9574f5ef95c6f38494ec1b",
      "s-888888888888888888888888",
      "s-999999999999999999999999",
      "s-aaaaaaaaaaaaaaaaaaaaaaaa",
      "s-bbbbbbbbbbbbbbbbbbbbbbbb"
    ],
    "requestedIds": [
      "s-3a166a1445aab5722f94f831",
      "s-4f9574f5ef95c6f38494ec1b",
      "s-888888888888888888888888",
      "s-999999999999999999999999",
      "s-aaaaaaaaaaaaaaaaaaaaaaaa",
      "s-bbbbbbbbbbbbbbbbbbbbbbbb"
    ],
    "policySha256": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd"
  },
  {
    "name": "missing opaque row",
    "expected": "source-refused",
    "status": "stopped",
    "reason": "source-refused",
    "calls": 0,
    "verificationCalls": 1,
    "originalRows": 6,
    "requestedRows": 5,
    "originalOpaqueRows": 4,
    "requestOpaqueRows": 3,
    "leakedWithheld": false,
    "planSourceIds": [],
    "requestedIds": [
      "s-2997a0d2d50b6ccb36010ea5",
      "s-3a166a1445aab5722f94f831",
      "s-4f9574f5ef95c6f38494ec1b",
      "s-5127f7656df18dc69344f0fd",
      "s-ce29447bc8016e363f9def6b"
    ],
    "policySha256": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd"
  },
  {
    "name": "extra opaque row",
    "expected": "source-refused",
    "status": "stopped",
    "reason": "source-refused",
    "calls": 0,
    "verificationCalls": 1,
    "originalRows": 6,
    "requestedRows": 7,
    "originalOpaqueRows": 4,
    "requestOpaqueRows": 5,
    "leakedWithheld": false,
    "planSourceIds": [],
    "requestedIds": [
      "s-3a166a1445aab5722f94f831",
      "s-4f9574f5ef95c6f38494ec1b",
      "s-8c307ec30c7767d4fd9e023d",
      "s-a2049e3fe35d6898283daa94",
      "s-f3ebf98edb8e8705b1f5a6a9",
      "s-fa2bbbc1e48f52ec59168121",
      "s-ffffffffffffffffffffffff"
    ],
    "policySha256": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd"
  },
  {
    "name": "excluded reason multiset changed",
    "expected": "source-refused",
    "status": "stopped",
    "reason": "source-refused",
    "calls": 0,
    "verificationCalls": 1,
    "originalRows": 6,
    "requestedRows": 6,
    "originalOpaqueRows": 4,
    "requestOpaqueRows": 4,
    "leakedWithheld": false,
    "planSourceIds": [],
    "requestedIds": [
      "s-170d312a53f36b997c6337ad",
      "s-3a166a1445aab5722f94f831",
      "s-4f9574f5ef95c6f38494ec1b",
      "s-716c6e6b31d5e69748722534",
      "s-8bdfb462644d766f71e51e3f",
      "s-a6a5ad317a0fdfead88ee03a"
    ],
    "policySha256": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd"
  },
  {
    "name": "duplicate opaque reason consumes bucket",
    "expected": "source-refused",
    "status": "stopped",
    "reason": "source-refused",
    "calls": 0,
    "verificationCalls": 1,
    "originalRows": 6,
    "requestedRows": 6,
    "originalOpaqueRows": 4,
    "requestOpaqueRows": 4,
    "leakedWithheld": false,
    "planSourceIds": [],
    "requestedIds": [
      "s-3a166a1445aab5722f94f831",
      "s-4f9574f5ef95c6f38494ec1b",
      "s-793be3b0d94d3579bb1fe200",
      "s-7e13901850a4c48e87a1323f",
      "s-ce33cdc8ddd5302d416e6595",
      "s-d41394d90216756b205ccb96"
    ],
    "policySha256": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd"
  },
  {
    "name": "excluded evaluation changed",
    "expected": "source-refused",
    "status": "stopped",
    "reason": "source-refused",
    "calls": 0,
    "verificationCalls": 1,
    "originalRows": 6,
    "requestedRows": 6,
    "originalOpaqueRows": 4,
    "requestOpaqueRows": 4,
    "leakedWithheld": false,
    "planSourceIds": [],
    "requestedIds": [
      "s-3114910800e1be56989fb3f0",
      "s-3a166a1445aab5722f94f831",
      "s-4f9574f5ef95c6f38494ec1b",
      "s-5cd2296638dadb572dcf4fcf",
      "s-cb5abfbc5c21dcbafa1cc1e1",
      "s-fc4c145e6b91b746546c4d25"
    ],
    "policySha256": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd"
  },
  {
    "name": "excluded classification basis changed",
    "expected": "source-refused",
    "status": "stopped",
    "reason": "source-refused",
    "calls": 0,
    "verificationCalls": 1,
    "originalRows": 6,
    "requestedRows": 6,
    "originalOpaqueRows": 4,
    "requestOpaqueRows": 4,
    "leakedWithheld": false,
    "planSourceIds": [],
    "requestedIds": [
      "s-3a166a1445aab5722f94f831",
      "s-3b58e3ec09391180173cf093",
      "s-4f9574f5ef95c6f38494ec1b",
      "s-db76185d2328568b450b975f",
      "s-e2799deeeb5442388a7b181b",
      "s-e8ab7fc5c821846ec614ea8f"
    ],
    "policySha256": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd"
  },
  {
    "name": "opaque unrelated path",
    "expected": "source-refused",
    "status": "stopped",
    "reason": "source-refused",
    "calls": 0,
    "verificationCalls": 1,
    "originalRows": 6,
    "requestedRows": 6,
    "originalOpaqueRows": 4,
    "requestOpaqueRows": 4,
    "leakedWithheld": false,
    "planSourceIds": [],
    "requestedIds": [
      "s-05547bbd1e23fd87fa433edf",
      "s-2eff663cfc9aff21fdf2b2f9",
      "s-3a166a1445aab5722f94f831",
      "s-4f9574f5ef95c6f38494ec1b",
      "s-d7bcb14c9f255011e1e3e414",
      "s-f515264364b4345751806241"
    ],
    "policySha256": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd"
  },
  {
    "name": "duplicate opaque source alias",
    "expected": "invalid-request",
    "status": "stopped",
    "reason": "invalid-request",
    "calls": 0,
    "verificationCalls": 0,
    "originalRows": 6,
    "requestedRows": 6,
    "originalOpaqueRows": 4,
    "requestOpaqueRows": 4,
    "leakedWithheld": false,
    "planSourceIds": [],
    "requestedIds": [
      "s-3a166a1445aab5722f94f831",
      "s-4f9574f5ef95c6f38494ec1b",
      "s-d36886febe9908577783a5ce",
      "s-d36886febe9908577783a5ce",
      "s-d36886febe9908577783a5ce",
      "s-d36886febe9908577783a5ce"
    ],
    "policySha256": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd"
  },
  {
    "name": "ordinary membership removed",
    "expected": "source-refused",
    "status": "stopped",
    "reason": "source-refused",
    "calls": 0,
    "verificationCalls": 1,
    "originalRows": 6,
    "requestedRows": 5,
    "originalOpaqueRows": 4,
    "requestOpaqueRows": 4,
    "leakedWithheld": false,
    "planSourceIds": [],
    "requestedIds": [
      "s-3a166a1445aab5722f94f831",
      "s-7613f5203f4e758df36d4feb",
      "s-93cc04963fb14372310c75ca",
      "s-a06f11bf194d109b3a30b90f",
      "s-c968c1cbda87a4aa3d8b19e0"
    ],
    "policySha256": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd"
  },
  {
    "name": "ordinary self-consistent forgery",
    "expected": "source-refused",
    "status": "stopped",
    "reason": "source-refused",
    "calls": 0,
    "verificationCalls": 1,
    "originalRows": 6,
    "requestedRows": 6,
    "originalOpaqueRows": 4,
    "requestOpaqueRows": 4,
    "leakedWithheld": false,
    "planSourceIds": [],
    "requestedIds": [
      "s-16d0dd255615c4916bc699aa",
      "s-373f135ce2e4e11107a63db8",
      "s-3a166a1445aab5722f94f831",
      "s-4f9574f5ef95c6f38494ec1b",
      "s-7075dfc45258a213f7f9083e",
      "s-be8b1c7fb1d0d14f4b7041d2"
    ],
    "policySha256": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd"
  },
  {
    "name": "redacted policy changed",
    "expected": "source-refused",
    "status": "stopped",
    "reason": "source-refused",
    "calls": 0,
    "verificationCalls": 1,
    "originalRows": 6,
    "requestedRows": 6,
    "originalOpaqueRows": 4,
    "requestOpaqueRows": 4,
    "leakedWithheld": false,
    "planSourceIds": [],
    "requestedIds": [
      "s-2979431fc98b141de0b602b7",
      "s-3a166a1445aab5722f94f831",
      "s-4f9574f5ef95c6f38494ec1b",
      "s-56ab2f2edd3d45fd29a3c255",
      "s-8bdea2ab351c77174886bf45",
      "s-c7569a16634c63bb301f3e3d"
    ],
    "policySha256": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd"
  },
  {
    "name": "ordinary-only control",
    "expected": "accept",
    "status": "awaiting-rendered-review",
    "reason": null,
    "calls": 5,
    "verificationCalls": 1,
    "originalRows": 1,
    "requestedRows": 1,
    "originalOpaqueRows": 0,
    "requestOpaqueRows": 0,
    "leakedWithheld": false,
    "planSourceIds": [
      "s-4f9574f5ef95c6f38494ec1b"
    ],
    "requestedIds": [
      "s-4f9574f5ef95c6f38494ec1b"
    ],
    "policySha256": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd"
  },
  {
    "name": "ordinary-only forgery",
    "expected": "source-refused",
    "status": "stopped",
    "reason": "source-refused",
    "calls": 0,
    "verificationCalls": 1,
    "originalRows": 1,
    "requestedRows": 1,
    "originalOpaqueRows": 0,
    "requestOpaqueRows": 0,
    "leakedWithheld": false,
    "planSourceIds": [],
    "requestedIds": [
      "s-4f9574f5ef95c6f38494ec1b"
    ],
    "policySha256": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd"
  }
]
```

Executing-mutant runner standard output, verbatim:

```text
row-count tests 16 failed 2 killed True
multiset-consumption tests 16 failed 2 killed True
excluded-reason tests 16 failed 2 killed True
restored-control {'exit': 0, 'tests': 16, 'passed': 16, 'failed': 0, 'sourceRestoredSha256': 'd4fbf19f6d1fa5fa260de2f3c637ae408153a206242053299f2461802475e711'}
evidence /home/tze/.cache/syzygy-p110-install-final-review-2026-10-20/full-6ef149b9-670hm284/population-mutation-1cdb-d8v0ppee
```

Typecheck output, verbatim:

```text
Command: npm run typecheck -- --force
Exit status: 0

> typecheck
> tsc -b packages/cap1-core packages/cap1-daemon packages/cap1-conformance packages/three-surface-poc-core apps/syzygy apps/three-surface-poc packages/cap1-system packages/polaris-generation-core packages/polaris-generation-consent packages/polaris-dossier --force

```
