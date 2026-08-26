# Syzygy Vky Validator Hardening Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> `superpowers:test-driven-development` while implementing each behavior.
> Beads issue `syzygy-vky` owns execution state; the numbered steps below are
> an execution recipe, not a second task tracker.

**Goal:** Make CG-1i verify every installed shape-M candidate fallback and
make CG-7d disclose quotation denominators per digest-bearing subject.

**Architecture:** Extend the two existing checker families in
`scripts/check_governance.py`; add no new check family and touch no governed
artifact. CG-1i derives an accepted module's candidate twin by path shape and
validates the same relative target there. CG-7d retains stale-digest matching
but reports each registered subject's population before forming its aggregate
result severity.

**Tech Stack:** Python 3 standard library, the existing `Results`/`Cap`
reporting seam, and `scripts/check_governance.py --selftest`.

## Global Constraints

- Modify only `scripts/check_governance.py`.
- Do not edit accepted RFC 0001-0009, candidate RFC 0010/0011, D3, acceptance
  records, decision registers, frozen review material, or `PROJECT-STATUS.md`.
- Preserve P-33 shape M: installed modules remain non-self-contained.
- A registered subject with zero quotations is disclosed as `WARN`, not
  converted into a fabricated quote or a stale-digest failure.
- Follow strict red-green-refactor: each new fixture must fail for the intended
  missing behavior before production logic changes.
- Keep the implementation dependency-free and deterministic.

---

### Task 1: Verify the CG-1i candidate fallback

**Files:**

- Modify: `scripts/check_governance.py`, CG-1 constants/helpers,
  `cg1_links`, `selftest`, and a new `_selftest_installed_fallback` helper.
- Test: `scripts/check_governance.py --selftest`.

**Interfaces:**

- Consumes: `CANDIDATES`, `_resolve(citing, target, all_paths)`, and the
  existing installed/candidate RFC directory shapes.
- Produces: `_candidate_twin(installed_rel, all_paths) -> str | None` and a
  CG-1i row whose result severity is `FAIL` when the selected candidate fallback is
  absent or unresolved.

1. Add the failing installed-fallback fixtures before changing CG-1i.

   Put the directory constants beside the other CG-1 constants and add this
   test helper beside `_selftest_dead_route`:

   ```python
   INSTALLED_RFCS = ".syzygy/governance/contracts/rfcs/"
   CANDIDATE_RFCS = f"{CANDIDATES}/rfcs/"


   def _selftest_installed_fallback(kind):
       class Cap:
           def __init__(self): self.rows = []
           def add(self, severity, name, examined, n, unit, note=None,
                   details=None):
               self.rows.append(
                   (severity, name, examined, n, details or []))

           def row(self, prefix):
               return next((r for r in self.rows
                            if r[1].startswith(prefix)), None)

       import shutil
       import tempfile
       d = tempfile.mkdtemp(prefix="cg1i-selftest-")
       global ROOT
       keep = ROOT
       try:
           installed = f"{INSTALLED_RFCS}RFC-0001/module.md"
           candidate = f"{CANDIDATE_RFCS}RFC-0001/module.md"
           history = f"{CANDIDATES}/history/source.md"
           target = ("../../../history/source.md" if kind == "wrong-depth"
                     else "../../history/source.md")
           paths = [installed, history]
           if kind != "missing-twin":
               paths.append(candidate)
           for rel in paths:
               full = os.path.join(d, rel)
               os.makedirs(os.path.dirname(full), exist_ok=True)
               with open(full, "w", encoding="utf-8") as fh:
                   fh.write((f"source: `{target}`\n"
                             if rel in (installed, candidate) else "source\n"))
           ROOT = d
           c = Cap()
           cg1_links(paths, c)
           return c.row("CG-1i")
       finally:
           ROOT = keep
           shutil.rmtree(d, ignore_errors=True)
   ```

   Register three fixtures in `selftest()`:

   ```python
   row = _selftest_installed_fallback("valid")
   cases.append(("CG-1i valid candidate fallback is verified and disclosed",
                 row[0] == "WARN" and row[2] == 1 and row[3] == 0))

   row = _selftest_installed_fallback("missing-twin")
   cases.append(("CG-1i missing candidate twin detected",
                 row[0] == "FAIL" and row[3] == 1))

   row = _selftest_installed_fallback("wrong-depth")
   cases.append(("CG-1i unresolved candidate fallback detected",
                 row[0] == "FAIL" and row[3] == 1))
   ```

2. Run the selftest and verify the intended red state.

   Run:

   ```bash
   python3 scripts/check_governance.py --selftest
   ```

   Expected: the valid fallback fixture passes, while both negative CG-1i
   fixtures report `FAIL` because current CG-1i classifies every installed
   reference as a warning without validating the candidate twin.

3. Add the minimal candidate-twin resolver.

   Add beside `_resolve`:

   ```python
   def _candidate_twin(installed_rel, all_paths):
       if not installed_rel.startswith(INSTALLED_RFCS):
           return None
       suffix = installed_rel[len(INSTALLED_RFCS):]
       candidate = CANDIDATE_RFCS + suffix
       return candidate if candidate in all_paths else None
   ```

4. Make the installed-reference branch verify the fallback.

   Replace the local `INSTALLED_RFCS` declaration and
   `installed_disclosed = []` with:

   ```python
   installed_examined = []
   installed_verified = []
   installed_findings = []
   ```

   Replace the first branch of `classify` with:

   ```python
   if rel.startswith(INSTALLED_RFCS):
       reference = f"{rel} -> {t}"
       installed_examined.append(reference)
       candidate = _candidate_twin(rel, all_paths)
       if candidate is None:
           installed_findings.append(
               f"{reference} — installed module has no candidate twin; "
               f"shape (M)'s fallback cannot be evaluated")
       elif not _resolve(candidate, t, all_paths):
           installed_findings.append(
               f"{reference} — candidate twin `{candidate}` does not "
               f"resolve the same relative target; shape (M)'s disclosed "
               f"fallback is false")
       else:
           installed_verified.append(reference)
   ```

   Replace the CG-1i result construction with:

   ```python
   uniq_inst = sorted(set(installed_examined))
   uniq_inst_findings = sorted(set(installed_findings))
   uniq_inst_verified = sorted(set(installed_verified))
   res.add("FAIL" if uniq_inst_findings else "WARN",
           "CG-1i  installed-tree path strings (P-33 shape (M))",
           len(uniq_inst), len(uniq_inst_findings), "reference",
           note=(("candidate-tree fallback verified for every installed "
                  "reference; installed modules remain non-self-contained "
                  "under P-33 shape (M)")
                 if not uniq_inst_findings else
                 "one or more installed references lack the candidate-tree "
                 "fallback promised by P-33 shape (M)"),
           details=(uniq_inst_findings
                    + [f"[verified candidate fallback] {r}"
                       for r in uniq_inst_verified]))
   ```

5. Run the selftest and verify green.

   Run:

   ```bash
   python3 scripts/check_governance.py --selftest
   ```

   Expected: all CG-1i fixtures pass and the whole selftest exits 0.

6. Commit the first behavior.

   ```bash
   git add scripts/check_governance.py
   git commit -m "test: verify installed RFC candidate fallbacks [syzygy-vky]"
   ```

---

### Task 2: Disclose CG-7d denominators per subject

**Files:**

- Modify: `scripts/check_governance.py`, `cg7d_quoted_elsewhere` and
  `selftest`.
- Test: `scripts/check_governance.py --selftest`.

**Interfaces:**

- Consumes: the registry-derived `ACT_SUBJECTS` tuple and the current subject
  digest calculation.
- Produces: a CG-7d aggregate row with per-subject detail; `FAIL` for stale or
  missing subjects, `WARN` when any registered subject has zero quotations,
  and `OK` only when every registered subject has a nonzero clean population.

1. Add optional synthetic inputs and the two failing fixtures before changing
   the aggregate behavior.

   Change the function signature to:

   ```python
   def cg7d_quoted_elsewhere(paths, res, act_subjects=None,
                             subject_digests=None, corpus=None):
   ```

   At the beginning of the function, normalize inputs without changing the
   existing behavior:

   ```python
   act_subjects = tuple(ACT_SUBJECTS if act_subjects is None
                        else act_subjects)
   ```

   Use `act_subjects` in place of each direct `ACT_SUBJECTS` iteration. When
   `subject_digests` is supplied, use it instead of hashing subject files.
   When `corpus` is supplied, iterate its `(rel, body)` pairs instead of
   reading `paths`.

   Register these fixtures in `selftest()`:

   ```python
   specs = (
       ("ACCEPT A", "a.md",
        re.compile(r"ACCEPT A:\s*`?([0-9a-f]{64})")),
       ("ADOPT DOCTRINE AMENDMENT: D3", "d3.md",
        re.compile(r"ADOPT DOCTRINE AMENDMENT:\s*D3:\s*`?([0-9a-f]{64})")),
   )
   digests = {
       "ACCEPT A": "a" * 64,
       "ADOPT DOCTRINE AMENDMENT: D3": "d" * 64,
   }

   c = Cap()
   cg7d_quoted_elsewhere([], c, act_subjects=specs,
                         subject_digests=digests,
                         corpus=[("f.md", "ACCEPT A: " + "a" * 64)])
   cases.append(("CG-7d zero subject denominator is disclosed",
                 c.rows[0][0] == "WARN"
                 and any("ADOPT DOCTRINE AMENDMENT: D3 — 0 quotation"
                         in d for d in c.rows[0][4])))

   c = Cap()
   cg7d_quoted_elsewhere(
       [], c, act_subjects=specs, subject_digests=digests,
       corpus=[("f.md", "ADOPT DOCTRINE AMENDMENT: D3: " + "e" * 64)])
   cases.append(("CG-7d stale D3-form quotation detected",
                 c.rows[0][0] == "FAIL"
                 and any("copy is stale" in d for d in c.rows[0][4])))
   ```

2. Run the selftest and verify the intended red state.

   Run:

   ```bash
   python3 scripts/check_governance.py --selftest
   ```

   Expected: the zero-denominator fixture fails because current CG-7d returns
   aggregate `OK`; the stale-D3 fixture must already exercise stale-digest
   detection or reveal a pattern defect that is fixed before proceeding.

3. Track and report each subject's population.

   Build these structures after subject digests are resolved:

   ```python
   counts = {label: 0 for label, _rel, _pat in act_subjects}
   subject_findings = {label: 0 for label, _rel, _pat in act_subjects}
   ```

   Increment `counts[label]` alongside `examined`. Whenever a missing-subject
   or stale-copy finding is appended, also increment
   `subject_findings[label]`.

   Construct the result with:

   ```python
   zero_subjects = [label for label, count in counts.items() if count == 0]
   subject_details = [
       f"[subject] {label} — {counts[label]} quotation(s), "
       f"{subject_findings[label]} finding(s)"
       for label in counts
   ]
   if findings:
       severity = "FAIL"
   elif zero_subjects:
       severity = "WARN"
   else:
       severity = "OK"
   note = (f"{len(counts) - len(zero_subjects)} of {len(counts)} "
           f"digest-bearing subject(s) have quotations"
           + (f"; zero: {', '.join(zero_subjects)}"
              if zero_subjects else ""))
   res.add(severity,
           "CG-7d  act digests quoted anywhere match their subjects",
           examined, len(findings), "quotation", note=note,
           details=findings + subject_details)
   ```

4. Run the selftest and verify green.

   Run:

   ```bash
   python3 scripts/check_governance.py --selftest
   ```

   Expected: both CG-7d fixtures pass and the whole selftest exits 0.

5. Commit the second behavior.

   ```bash
   git add scripts/check_governance.py
   git commit -m "test: disclose act quotation populations [syzygy-vky]"
   ```

---

### Task 3: Verify the exact implementation and open the review lane

**Files:**

- Verify only: `scripts/check_governance.py`.
- Do not modify: `PROJECT-STATUS.md` or governed artifacts.

**Interfaces:**

- Consumes: the two committed checker changes.
- Produces: exact-head local and clone evidence, an implementation PR, and a
  structured worker report for coordinator reconciliation.

1. Run the focused checker and inspect the two changed rows.

   ```bash
   python3 scripts/check_governance.py --scope tracked > /tmp/syzygy-vky-check.log
   rg -n "CG-1i|CG-7d|FAIL" /tmp/syzygy-vky-check.log
   ```

   Expected: CG-1i reports its verified fallback denominator with zero
   findings; CG-7d reports every subject, including any zero population;
   there are no `FAIL` rows.

2. Run the complete selftest and inspect its denominator.

   ```bash
   python3 scripts/check_governance.py --selftest \
     > /tmp/syzygy-vky-selftest.log
   tail -n 3 /tmp/syzygy-vky-selftest.log
   ```

   Expected: all fixtures pass, including five new fixtures, and the command
   exits 0.

3. Independently reproduce the changed populations.

   Run a Python `re` census independent of the checker helpers:

   ```bash
   python3 - <<'PY'
   from pathlib import Path
   import re

   root = Path.cwd()
   installed = root / ".syzygy/governance/contracts/rfcs"
   candidates = root / ".syzygy/governance/contracts/candidates/rfcs"
   path_re = re.compile(r"`([A-Za-z0-9_.\-/]+\.(?:md|py|sh|ya?ml|json|txt))`")
   link_re = re.compile(r"\[[^\]]*\]\(\s*([^\s)#]+)")
   forward = (
       ".syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md",
       ".syzygy/governance/contracts/rfcs/",
       ".syzygy/governance/contracts/wave-manifests/",
       ".syzygy/governance/contracts/history/",
       ".syzygy/governance/contracts/matrix-rows/",
       ".syzygy/map/topology/",
       ".syzygy/project.yaml",
       "openspec/",
       "RFC-000n",
       "RFC-000N",
   )
   examined_pairs = set()
   finding_pairs = set()
   for module in installed.rglob("*.md"):
       twin = candidates / module.relative_to(installed)
       body = module.read_text()
       targets = path_re.findall(body) + link_re.findall(body)
       for target in targets:
           if target.startswith(("http://", "https://", "mailto:", "ftp://")):
               continue
           if any(item in target or item.endswith("/" + target)
                  or item == target for item in forward):
               continue
           local = (module.parent / target).resolve()
           if local.exists():
               continue
           pair = (str(module.relative_to(root)), target)
           examined_pairs.add(pair)
           if not twin.exists() or not (twin.parent / target).resolve().exists():
               finding_pairs.add(pair)
   print(f"installed_fallbacks={len(examined_pairs)} "
         f"findings={len(finding_pairs)}")
   raise SystemExit(1 if finding_pairs else 0)
   PY
   ```

   Enumerate digest quotations directly from the registry-derived labels with
   this second standard-library script. It deliberately does not import
   `scripts/check_governance.py`:

   ```bash
   python3 - <<'PY'
   from pathlib import Path
   import re
   import subprocess

   root = Path.cwd()
   candidates = ".syzygy/governance/contracts/candidates"
   registry = root / candidates / "ACCEPTANCE-PHRASE-REGISTRY.yaml"
   active = registry.read_text().split("retired_phrases:", 1)[0]
   active = active.split("current_phrases:", 1)[1]
   blocks = re.split(r"\n(?=  - id:)", active)
   specs = []
   for block in blocks:
       label = re.search(r'^    label: "([^"]+)"$', block, re.M)
       argument = re.search(r"^    argument: (\S+)$", block, re.M)
       subject = re.search(r'^    subject: "([^"]+)"$', block, re.M)
       separator = re.search(r'^    argument_separator: "([^"]+)"$',
                             block, re.M)
       if not label or not argument or argument.group(1) != "sha256" or not subject:
           continue
       specs.append((label.group(1), subject.group(1),
                     separator.group(1) if separator else ":"))

   listed = subprocess.run(
       ["git", "ls-files", "*.md"], check=True, text=True,
       capture_output=True).stdout.splitlines()
   exact_exempt = {
       f"{candidates}/00-README.md",
       f"{candidates}/10-EXIT-REPORT.md",
       f"{candidates}/round-2026-08/OWNER-ROUND-CHARTER.md",
       f"{candidates}/round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md",
       f"{candidates}/round-2026-08c/FINAL-OWNER-ACCEPTANCE-PACKET.md",
       "scripts/check_governance.py",
   }

   def exempt(rel):
       parts = rel.split("/")
       return (rel in exact_exempt
               or rel.startswith(f"{candidates}/history/")
               or rel.startswith(f"{candidates}/fixtures/")
               or (rel.startswith(f"{candidates}/")
                   and "reviews" in parts[:-1]))

   counts = {label: 0 for label, _subject, _separator in specs}
   for rel in listed:
       if exempt(rel):
           continue
       body = (root / rel).read_text(errors="replace")
       for label, _subject, separator in specs:
           pattern = re.compile(re.escape(label) + r"\s*"
                                + re.escape(separator)
                                + r"\s*`?([0-9a-f]{64})")
           for line in body.splitlines():
               for match in pattern.finditer(line):
                   before = line[max(0, match.start() - 60):match.start()]
                   if re.search(r"\b(retired|stale|superseded|pre-amendment|historical)\b",
                                before, re.I):
                       continue
                   counts[label] += 1

   for label, count in counts.items():
       print(f"{label} — {count} quotation(s)")
   PY
   ```

   Compare every printed label and count with the CG-7d subject details.

4. Push the implementation branch so a clean clone can bind to its exact
   commit.

   ```bash
   git push -u origin agent/syzygy-vky
   ```

5. Run the canonical battery in a clean clone of the exact branch.

   ```bash
   clone_dir=$(mktemp -d)
   git clone --no-local --branch agent/syzygy-vky \
     /home/tze/GitHub/syzygy "$clone_dir/repo"
   cd "$clone_dir/repo"
   python3 scripts/check_governance.py
   python3 scripts/check_governance.py --selftest
   python3 scripts/launch_gate_results.py --selftest
   python3 scripts/validate_launch_administration.py --selftest
   python3 scripts/render_launch_administration.py --selftest
   CS=.syzygy/governance/contracts/candidates/scripts
   python3 $CS/verify_final_prespec.py
   python3 $CS/build_contract_index.py --check
   python3 $CS/build_dependency_index.py --check
   python3 $CS/build_budget_report.py --check
   python3 $CS/build_active_manifest.py --check
   python3 $CS/build_task_router.py --check
   python3 $CS/build_task_router.py --selftest
   python3 $CS/build_capability_1_views.py --check
   python3 $CS/build_capability_1_views.py --selftest
   python3 scripts/build_capability_1_spec_dependencies.py --check
   python3 scripts/build_capability_1_spec_dependencies.py --selftest
   DR=.syzygy/governance/contracts/candidates/round-2026-08f/fixtures/DRY-RUN-ADMINISTRATION.json
   python3 scripts/validate_launch_administration.py $DR
   python3 scripts/render_launch_administration.py $DR --check
   ```

   Expected: every command exits 0; inspect each command's printed
   denominator and preserve the log path in the worker report.

6. Confirm the branch owns only the approved file and record test growth.

   ```bash
   git diff --check origin/main...HEAD
   git diff --name-only origin/main...HEAD
   git status --short
   ```

   Expected: only `scripts/check_governance.py` differs, the worktree is clean,
   and the selftest denominator has increased by exactly five fixtures.

7. Open a PR and return the Beads worker report.

   The PR body must cite `syzygy-vky`, the approved design and this plan; state
   the exact head SHA, local and clean-clone gate results, the two independent
   population counts, and the five-fixture delta. The worker must not close or
   otherwise mutate Beads state.
