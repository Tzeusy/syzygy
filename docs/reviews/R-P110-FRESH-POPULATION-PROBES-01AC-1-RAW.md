# Verbatim reproduction output — 01ac fresh population

Command in the disposable clone:

```text
node_modules/.bin/vitest run apps/three-surface-poc/src/polaris-generation/p110-independent-review.test.ts --maxWorkers 1 --reporter=json --outputFile ../independent-security-probes.json
```

Exit status: 1. Standard output:

```text
JSON report written to /home/tze/.cache/syzygy-p110-install-final-review-2026-10-20/full-6ef149b9-670hm284/independent-security-probes.json
```

Positive control JSON (verbatim):

```json
{
  "result": {
    "status": "awaiting-rendered-review",
    "draft": {},
    "inventory": {},
    "review": {},
    "quoteFindings": [],
    "receipts": [
      {
        "stage": "inventory",
        "attemptId": "0",
        "reused": false,
        "providerRoute": "agent-sdk",
        "model": "synthetic",
        "inputDigest": "958294afb11a84b1408a7a7e4f9e738542834dcea9679d06d8f76ae861a791af",
        "outputDigest": "44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a",
        "promptVersion": "polaris-inventory-v1",
        "promptProfile": "manifesto",
        "promptDigest": "ea6c06ff89668f4914859b4c1133f9def4db51f2456f28b2cf86ba89fb1411af"
      },
      {
        "stage": "plan",
        "attemptId": "1",
        "reused": false,
        "providerRoute": "agent-sdk",
        "model": "synthetic",
        "inputDigest": "f859c0f699c26eec93c755735545025379eee99094a904c2095d770a76b40e9a",
        "outputDigest": "44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a",
        "promptVersion": "polaris-plan-v2",
        "promptProfile": "manifesto",
        "promptDigest": "e632eada2e46aac167345b95fa5911e04ebf6b183d1fb19e1564ede4da7db344"
      },
      {
        "stage": "author",
        "attemptId": "2",
        "reused": false,
        "providerRoute": "agent-sdk",
        "model": "synthetic",
        "inputDigest": "21d0a94cfa2ebf3f3d6d294b87c6d4d37cbc5ac878c0def405db4fd266bfb8f6",
        "outputDigest": "44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a",
        "promptVersion": "polaris-author-v2",
        "promptProfile": "manifesto",
        "promptDigest": "5ff6d41c45e7fe9cf28d5e957d0c85ff3c714aa9f3f2de17523a4c2e554c9743"
      },
      {
        "stage": "edit",
        "attemptId": "3",
        "reused": false,
        "providerRoute": "agent-sdk",
        "model": "synthetic",
        "inputDigest": "09641053da96e70d1c4a062220070b4fd8ad9f42386ea9d6043dbc536d33d970",
        "outputDigest": "44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a",
        "promptVersion": "polaris-edit-v2",
        "promptProfile": "manifesto",
        "promptDigest": "d0af06409f066c42c7a1f69f60b0c2f60b097926ea3508fd8322e6f11413e6de"
      },
      {
        "stage": "fidelity",
        "attemptId": "4",
        "reused": false,
        "providerRoute": "agent-sdk",
        "model": "synthetic",
        "inputDigest": "a643c26ddfcb0bbca2b06554fbf539195414c648bd68cda8477feab12f205a52",
        "outputDigest": "44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a",
        "promptVersion": "polaris-fidelity-v1",
        "promptProfile": "manifesto",
        "promptDigest": "ea3d5f99f5ac1520ae46a1a3f9c0fca7e0180427ca92a2aaf85a0c975f97377c"
      }
    ],
    "artifacts": [
      {
        "stage": "inventory",
        "value": {}
      },
      {
        "stage": "plan",
        "value": {}
      },
      {
        "stage": "author",
        "value": {}
      },
      {
        "stage": "edit",
        "value": {}
      },
      {
        "stage": "fidelity",
        "value": {}
      }
    ]
  },
  "audits": [
    {
      "at": 1800000000000,
      "phase": "identity",
      "stage": "inventory",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "b703240a7df64900b36a9e723c2154bbcd0e6699f69adcc09ab1ec67feee72c4"
    },
    {
      "at": 1800000000000,
      "phase": "admit",
      "stage": "inventory",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "b703240a7df64900b36a9e723c2154bbcd0e6699f69adcc09ab1ec67feee72c4"
    },
    {
      "at": 1800000000000,
      "phase": "dispatch",
      "stage": "inventory",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "b703240a7df64900b36a9e723c2154bbcd0e6699f69adcc09ab1ec67feee72c4"
    },
    {
      "at": 1800000000000,
      "phase": "identity",
      "stage": "plan",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "b703240a7df64900b36a9e723c2154bbcd0e6699f69adcc09ab1ec67feee72c4"
    },
    {
      "at": 1800000000000,
      "phase": "admit",
      "stage": "plan",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "b703240a7df64900b36a9e723c2154bbcd0e6699f69adcc09ab1ec67feee72c4"
    },
    {
      "at": 1800000000000,
      "phase": "dispatch",
      "stage": "plan",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "b703240a7df64900b36a9e723c2154bbcd0e6699f69adcc09ab1ec67feee72c4"
    },
    {
      "at": 1800000000000,
      "phase": "identity",
      "stage": "author",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "b703240a7df64900b36a9e723c2154bbcd0e6699f69adcc09ab1ec67feee72c4"
    },
    {
      "at": 1800000000000,
      "phase": "admit",
      "stage": "author",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "b703240a7df64900b36a9e723c2154bbcd0e6699f69adcc09ab1ec67feee72c4"
    },
    {
      "at": 1800000000000,
      "phase": "dispatch",
      "stage": "author",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "b703240a7df64900b36a9e723c2154bbcd0e6699f69adcc09ab1ec67feee72c4"
    },
    {
      "at": 1800000000000,
      "phase": "identity",
      "stage": "edit",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "b703240a7df64900b36a9e723c2154bbcd0e6699f69adcc09ab1ec67feee72c4"
    },
    {
      "at": 1800000000000,
      "phase": "admit",
      "stage": "edit",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "b703240a7df64900b36a9e723c2154bbcd0e6699f69adcc09ab1ec67feee72c4"
    },
    {
      "at": 1800000000000,
      "phase": "dispatch",
      "stage": "edit",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "b703240a7df64900b36a9e723c2154bbcd0e6699f69adcc09ab1ec67feee72c4"
    },
    {
      "at": 1800000000000,
      "phase": "identity",
      "stage": "fidelity",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "b703240a7df64900b36a9e723c2154bbcd0e6699f69adcc09ab1ec67feee72c4"
    },
    {
      "at": 1800000000000,
      "phase": "admit",
      "stage": "fidelity",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "b703240a7df64900b36a9e723c2154bbcd0e6699f69adcc09ab1ec67feee72c4"
    },
    {
      "at": 1800000000000,
      "phase": "dispatch",
      "stage": "fidelity",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "b703240a7df64900b36a9e723c2154bbcd0e6699f69adcc09ab1ec67feee72c4"
    }
  ],
  "originalObjectId": "02a7c5df78723ba6e088c63d531acf0b7411c85d",
  "requestObjectId": "02a7c5df78723ba6e088c63d531acf0b7411c85d",
  "pinnedObjectId": "02a7c5df78723ba6e088c63d531acf0b7411c85d",
  "redactedRows": 1,
  "sends": 5,
  "leakedSentinel": false,
  "fixtureSourceCount": 2,
  "policySha256": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd"
}```

Forged mixed-population JSON (verbatim):

```json
{
  "result": {
    "status": "awaiting-rendered-review",
    "draft": {},
    "inventory": {},
    "review": {},
    "quoteFindings": [],
    "receipts": [
      {
        "stage": "inventory",
        "attemptId": "0",
        "reused": false,
        "providerRoute": "agent-sdk",
        "model": "synthetic",
        "inputDigest": "534dcb1afdb7fee631c48540e27b7e61db65271afba4833f19a87a48c2f69d7d",
        "outputDigest": "44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a",
        "promptVersion": "polaris-inventory-v1",
        "promptProfile": "manifesto",
        "promptDigest": "ea6c06ff89668f4914859b4c1133f9def4db51f2456f28b2cf86ba89fb1411af"
      },
      {
        "stage": "plan",
        "attemptId": "1",
        "reused": false,
        "providerRoute": "agent-sdk",
        "model": "synthetic",
        "inputDigest": "f859c0f699c26eec93c755735545025379eee99094a904c2095d770a76b40e9a",
        "outputDigest": "44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a",
        "promptVersion": "polaris-plan-v2",
        "promptProfile": "manifesto",
        "promptDigest": "e632eada2e46aac167345b95fa5911e04ebf6b183d1fb19e1564ede4da7db344"
      },
      {
        "stage": "author",
        "attemptId": "2",
        "reused": false,
        "providerRoute": "agent-sdk",
        "model": "synthetic",
        "inputDigest": "21d0a94cfa2ebf3f3d6d294b87c6d4d37cbc5ac878c0def405db4fd266bfb8f6",
        "outputDigest": "44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a",
        "promptVersion": "polaris-author-v2",
        "promptProfile": "manifesto",
        "promptDigest": "5ff6d41c45e7fe9cf28d5e957d0c85ff3c714aa9f3f2de17523a4c2e554c9743"
      },
      {
        "stage": "edit",
        "attemptId": "3",
        "reused": false,
        "providerRoute": "agent-sdk",
        "model": "synthetic",
        "inputDigest": "09641053da96e70d1c4a062220070b4fd8ad9f42386ea9d6043dbc536d33d970",
        "outputDigest": "44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a",
        "promptVersion": "polaris-edit-v2",
        "promptProfile": "manifesto",
        "promptDigest": "d0af06409f066c42c7a1f69f60b0c2f60b097926ea3508fd8322e6f11413e6de"
      },
      {
        "stage": "fidelity",
        "attemptId": "4",
        "reused": false,
        "providerRoute": "agent-sdk",
        "model": "synthetic",
        "inputDigest": "a643c26ddfcb0bbca2b06554fbf539195414c648bd68cda8477feab12f205a52",
        "outputDigest": "44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a",
        "promptVersion": "polaris-fidelity-v1",
        "promptProfile": "manifesto",
        "promptDigest": "ea3d5f99f5ac1520ae46a1a3f9c0fca7e0180427ca92a2aaf85a0c975f97377c"
      }
    ],
    "artifacts": [
      {
        "stage": "inventory",
        "value": {}
      },
      {
        "stage": "plan",
        "value": {}
      },
      {
        "stage": "author",
        "value": {}
      },
      {
        "stage": "edit",
        "value": {}
      },
      {
        "stage": "fidelity",
        "value": {}
      }
    ]
  },
  "audits": [
    {
      "at": 1800000000000,
      "phase": "identity",
      "stage": "inventory",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "d09514d1bca114271594f742603a7f9cdcf3b82698148cfe00ba81d180afe448"
    },
    {
      "at": 1800000000000,
      "phase": "admit",
      "stage": "inventory",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "d09514d1bca114271594f742603a7f9cdcf3b82698148cfe00ba81d180afe448"
    },
    {
      "at": 1800000000000,
      "phase": "dispatch",
      "stage": "inventory",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "d09514d1bca114271594f742603a7f9cdcf3b82698148cfe00ba81d180afe448"
    },
    {
      "at": 1800000000000,
      "phase": "identity",
      "stage": "plan",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "d09514d1bca114271594f742603a7f9cdcf3b82698148cfe00ba81d180afe448"
    },
    {
      "at": 1800000000000,
      "phase": "admit",
      "stage": "plan",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "d09514d1bca114271594f742603a7f9cdcf3b82698148cfe00ba81d180afe448"
    },
    {
      "at": 1800000000000,
      "phase": "dispatch",
      "stage": "plan",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "d09514d1bca114271594f742603a7f9cdcf3b82698148cfe00ba81d180afe448"
    },
    {
      "at": 1800000000000,
      "phase": "identity",
      "stage": "author",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "d09514d1bca114271594f742603a7f9cdcf3b82698148cfe00ba81d180afe448"
    },
    {
      "at": 1800000000000,
      "phase": "admit",
      "stage": "author",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "d09514d1bca114271594f742603a7f9cdcf3b82698148cfe00ba81d180afe448"
    },
    {
      "at": 1800000000000,
      "phase": "dispatch",
      "stage": "author",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "d09514d1bca114271594f742603a7f9cdcf3b82698148cfe00ba81d180afe448"
    },
    {
      "at": 1800000000000,
      "phase": "identity",
      "stage": "edit",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "d09514d1bca114271594f742603a7f9cdcf3b82698148cfe00ba81d180afe448"
    },
    {
      "at": 1800000000000,
      "phase": "admit",
      "stage": "edit",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "d09514d1bca114271594f742603a7f9cdcf3b82698148cfe00ba81d180afe448"
    },
    {
      "at": 1800000000000,
      "phase": "dispatch",
      "stage": "edit",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "d09514d1bca114271594f742603a7f9cdcf3b82698148cfe00ba81d180afe448"
    },
    {
      "at": 1800000000000,
      "phase": "identity",
      "stage": "fidelity",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "d09514d1bca114271594f742603a7f9cdcf3b82698148cfe00ba81d180afe448"
    },
    {
      "at": 1800000000000,
      "phase": "admit",
      "stage": "fidelity",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "d09514d1bca114271594f742603a7f9cdcf3b82698148cfe00ba81d180afe448"
    },
    {
      "at": 1800000000000,
      "phase": "dispatch",
      "stage": "fidelity",
      "providerRoute": "agent-sdk",
      "providerId": "synthetic-provider",
      "decision": "permitted",
      "unknown": null,
      "reasons": [],
      "relied": [
        {
          "recordId": "SYNTHETIC-EGRESS",
          "version": "1",
          "digest": "2222222222222222222222222222222222222222222222222222222222222222"
        },
        {
          "recordId": "SYNTHETIC-OBS",
          "version": "1",
          "digest": "1111111111111111111111111111111111111111111111111111111111111111"
        }
      ],
      "populationDigest": "d09514d1bca114271594f742603a7f9cdcf3b82698148cfe00ba81d180afe448"
    }
  ],
  "originalObjectId": "02a7c5df78723ba6e088c63d531acf0b7411c85d",
  "requestObjectId": "97dc08cc43bf4685da4eb03e1677ba915fb08da0",
  "pinnedObjectId": "02a7c5df78723ba6e088c63d531acf0b7411c85d",
  "redactedRows": 1,
  "sends": 5,
  "leakedSentinel": true,
  "fixtureSourceCount": 2,
  "policySha256": "319e404ee413220550d65644f6c93db096ed1cda431760baec70a1e190adb0bd"
}```

Vitest JSON (verbatim):

```json
{"numTotalTestSuites":2,"numPassedTestSuites":0,"numFailedTestSuites":2,"numPendingTestSuites":0,"numTotalTests":2,"numPassedTests":1,"numFailedTests":1,"numPendingTests":0,"numTodoTests":0,"snapshot":{"added":0,"failure":false,"filesAdded":0,"filesRemoved":0,"filesRemovedList":[],"filesUnmatched":0,"filesUpdated":0,"matched":0,"total":0,"unchecked":0,"uncheckedKeysByFile":[],"unmatched":0,"updated":0,"didUpdate":false},"startTime":1792514916980,"success":false,"testResults":[{"assertionResults":[{"ancestorTitles":["independent fresh gated population check"],"fullName":"independent fresh gated population check accepts the unmodified JSON projection with real source verification and consent ports","status":"passed","title":"accepts the unmodified JSON projection with real source verification and consent ports","duration":76.03477799999996,"failureMessages":[],"meta":{}},{"ancestorTitles":["independent fresh gated population check"],"fullName":"independent fresh gated population check rejects a mixed request whose ordinary source was replaced outside the fresh pinned population","status":"failed","title":"rejects a mixed request whose ordinary source was replaced outside the fresh pinned population","duration":54.491683000000194,"failureMessages":["AssertionError: expected { …(7) } to match object { status: 'stopped', …(1) }\n(6 matching properties omitted from actual)\n    at Proxy.<anonymous> (file:///home/tze/.cache/syzygy-p110-install-final-review-2026-10-20/full-6ef149b9-670hm284/repo/node_modules/@vitest/expect/dist/index.js:1155:10)\n    at Proxy.<anonymous> (file:///home/tze/.cache/syzygy-p110-install-final-review-2026-10-20/full-6ef149b9-670hm284/repo/node_modules/@vitest/expect/dist/index.js:1029:14)\n    at Proxy.methodWrapper (file:///home/tze/.cache/syzygy-p110-install-final-review-2026-10-20/full-6ef149b9-670hm284/repo/node_modules/chai/index.js:1686:25)\n    at /home/tze/.cache/syzygy-p110-install-final-review-2026-10-20/full-6ef149b9-670hm284/repo/apps/three-surface-poc/src/polaris-generation/p110-independent-review.test.ts:55:22\n    at file:///home/tze/.cache/syzygy-p110-install-final-review-2026-10-20/full-6ef149b9-670hm284/repo/node_modules/@vitest/runner/dist/chunk-hooks.js:752:20"],"meta":{}}],"startTime":1792514918195,"endTime":1792514918325.4917,"status":"failed","message":"","name":"/home/tze/.cache/syzygy-p110-install-final-review-2026-10-20/full-6ef149b9-670hm284/repo/apps/three-surface-poc/src/polaris-generation/p110-independent-review.test.ts"}]}```
