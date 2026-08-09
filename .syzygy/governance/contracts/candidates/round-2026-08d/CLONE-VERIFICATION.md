# Clone verification — round 2026-08d

**Non-authoritative round record**, per verification rule 7: a clone report
is valid only for the commit it was run at.

- **Commit:** `771965c` — "governance: the package split into six
  acceptable waves, the preserved defects repaired, and every fixture
  given a question it must answer blind"
- **Method:** fresh `git clone` of the repository into a scratch
  directory; the full battery run from the clone root. [Observed]

| Check | Output (verbatim tail) |
|---|---|
| `scripts/check_governance.py` | `25 OK, 15 WARN, 0 FAIL (40 checks) — counts derived, not asserted` |
| `check_governance.py --selftest` | `77 fixtures, 0 failing — a check that cannot fail is not a check` |
| `verify_final_prespec.py` | `PASS — all checks clean` |
| `build_contract_index.py --check` | `index matches regeneration — no drift` |
| `build_dependency_index.py --check` | `dependency index matches regeneration — no drift` |
| `build_budget_report.py --check` | `fixture anchors match regeneration` |
| `build_active_manifest.py --check` | `all 7 manifests match regeneration` |

The 15 WARNs are the declared-by-design classes (forward references,
frozen-packet pointers, report-only figures, allowlists); each prints its
own rationale. Read the output, not the exit code.

This report says nothing about any commit after `771965c`.
