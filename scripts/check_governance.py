#!/usr/bin/env python3
"""Repository-wide governance checks for Syzygy — read-only, portable.

Run from the repository root:

    python3 scripts/check_governance.py

Exit status: 0 = no findings, 1 = at least one FAIL finding, 2 = usage error.

Design constraints (charter §17, "public, portable validation"):

  * **Repository-relative.** The repo root is derived from this file's own
    location; no founder-machine absolute path appears anywhere.
  * **Standard library only**, Python 3.9+. No installs, no network.
  * **Read-only.** This script never writes, moves, or rewrites a governance
    artifact. When a check finds a defect it *reports* it; correcting a
    normative artifact is a human act under the normative-change workflow.
  * **Every summary line states its denominator.** A check that examined zero
    items reports WARN — "PASS over nothing examined" is the failure mode this
    project exists to prevent (VIS-2: no evidence yields Unknown, never green).
  * **Allowlists are declared inline, counted, and printed.** A silent
    exemption is indistinguishable from a missing check.

Checks
------
  CG-1   internal links and path references resolve
  CG-2   retired acceptance phrase / `about/` authority path absent from
         active instructions
  CG-3   stale bootstrap routing (`_bootstrap/prompts/`) absent
  CG-4   candidate homes carry candidate banners
  CG-5   canonical craft banners are truthful
  CG-6   accepted homes do not exist yet (created only by owner acts)
  CG-7   ACTIVE-CONTRACT-MANIFEST digests are valid, and the acceptance
         record's act-1 argument still matches the manifest
  CG-8   context budgets reported (never enforced — charter §11.4 triggers)
  CG-9   duplicate authority homes absent
  CG-10  pending-decision register as-of line reported
  CG-11  `.syzygy/cache/` and `.syzygy/local/` are git-ignored
  CG-12  no active artifact cites a `_bootstrap/` path as a required source
  CG-13  dependency edges resolve; a package README equals its module union
  CG-14  acceptance-record install sources and destinations are valid
  CG-15  truncated digest quotes still prefix a current argument
  CG-16  the term registry is never described as accepted
  CG-17  every RFC 0006-0011 clause is routed exactly once
  CG-18  context fixtures still recompute (digest and word count)
  CG-19  substrate pins resolve publicly, and drift carries a disposition

`--selftest` runs every check above against a synthetic failing input. A
validator that has never been shown to fail is indistinguishable from a
no-op, and this repository has shipped one (charter §18).

Status vocabulary: OK (examined > 0, no findings) · WARN (nothing examined, or
a report-only observation) · FAIL (findings that fail the run).
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SELF_REL = os.path.relpath(os.path.abspath(__file__), ROOT).replace(os.sep, "/")

CANDIDATES = ".syzygy/governance/contracts/candidates"
TOPOLOGY_CANDIDATES = ".syzygy/map/topology-candidates"
CRAFT = ".syzygy/governance/policies/craft-and-care"
DOCTRINE = ".syzygy/governance/doctrine"
DECISIONS = ".syzygy/governance/decisions"


# --------------------------------------------------------------- results

class Results:
    """One summary line per check, plus finding detail lines beneath it."""

    def __init__(self):
        self.summaries = []
        self._fail = False

    def add(self, status, name, examined, findings, unit="item",
            note=None, details=()):
        if status == "FAIL":
            self._fail = True
        self.summaries.append((status, name, examined, findings, unit, note,
                               list(details)))

    def failed(self):
        return self._fail

    @staticmethod
    def _plural(n, unit):
        if n == 1:
            return unit
        return unit[:-1] + "ies" if unit.endswith("y") else unit + "s"

    def report(self):
        for status, name, examined, findings, unit, note, details in self.summaries:
            line = (f"{status:4s}  {name} — {examined} "
                    f"{self._plural(examined, unit)} examined, "
                    f"{findings} finding{'' if findings == 1 else 's'}")
            if note:
                line += f" — {note}"
            print(line)
            for d in details:
                print(f"        {d}")
        n_fail = sum(1 for s, *_ in self.summaries if s == "FAIL")
        n_warn = sum(1 for s, *_ in self.summaries if s == "WARN")
        n_ok = sum(1 for s, *_ in self.summaries if s == "OK")
        print(f"\n{n_ok} OK, {n_warn} WARN, {n_fail} FAIL "
              f"({len(self.summaries)} checks) — counts derived, not asserted")


# --------------------------------------------------------------- corpus

def _git(*args):
    try:
        out = subprocess.run(["git", "-C", ROOT, *args],
                             capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return None
    if out.returncode != 0:
        return None
    return out.stdout.splitlines()


def corpus_paths(scope):
    """Repo-relative paths a clone would (or will) contain.

    `tracked` is `git ls-files`. The default `clone` scope adds untracked
    files that are not git-ignored — the candidate governance package is
    exactly that today, and a tracked-only corpus would give checks CG-4,
    CG-7, CG-8, CG-9 and CG-12 a **zero denominator**, i.e. a vacuous pass
    over the material those checks exist for. Both counts are printed so the
    scope is never implicit.

    Returns (paths, tracked_set, source). `source` is "git" normally and
    "walk" when git is unavailable — an exported or archived copy of the
    tree, where the corpus is a filesystem walk and *nothing is known to be
    tracked*. The walk is a degraded mode, printed as such: it cannot honor
    `--scope tracked` and it cannot distinguish ignored files, so CG-11 is
    reported Unknown rather than passed.
    """
    tracked = _git("ls-files")
    if tracked is None:
        walked = []
        for dirpath, dirnames, filenames in os.walk(ROOT):
            dirnames[:] = [d for d in dirnames
                           if d not in {".git", "__pycache__", "node_modules"}]
            for fn in filenames:
                rel = os.path.relpath(os.path.join(dirpath, fn), ROOT)
                walked.append(rel.replace(os.sep, "/"))
        return sorted(walked), set(), "walk"
    tracked = [p for p in tracked if p]
    if scope == "tracked":
        return sorted(set(tracked)), set(tracked), "git"
    others = _git("ls-files", "--others", "--exclude-standard") or []
    return (sorted(set(tracked) | {p for p in others if p}),
            set(tracked), "git")


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace") as fh:
        return fh.read()


def md_files(paths):
    return [p for p in paths if p.endswith(".md")]


def words(rel):
    return len(read(rel).split())


# --------------------------------------------------------------- CG-1

MD_LINK = re.compile(r"\[[^\]]*\]\(\s*(?P<t>[^)\s]+)")
#: Path references in this corpus are overwhelmingly inline code spans, not
#: markdown links (39 relative links against 478 code-span paths at the time
#: of writing). A link-only check would report a confident PASS over ~8% of
#: the population that can actually dangle.
CODE_PATH = re.compile(r"`(?P<t>[A-Za-z0-9_.\-/]+\.(?:md|py|sh|ya?ml|json|txt))`")
EXTERNAL = ("http://", "https://", "mailto:", "ftp://")

#: Artifacts that do not exist yet **by design** — an owner act creates them,
#: or they belong to a governed project that does not exist. A reference to
#: one is correct, not broken. Declared, counted, and printed on every run.
FORWARD_REFS = (
    ".syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md",  # created by act 1
    ".syzygy/governance/contracts/rfcs/",                     # act-1 install home
    ".syzygy/map/topology/",                                  # act-3 install home
    ".syzygy/project.yaml",                                   # no governed project yet
    "openspec/",                                              # does not exist yet
    "RFC-000n",                                               # glob placeholder
)


#: Target *shapes* that name the frozen rev9 working packet — a tree that
#: lived under the git-excluded `_bootstrap/` and whose internal layout these
#: derivation records cite relatively (`final-prespec/…`, `../rfcs/RFC-0007-
#: polaris-intent-surface.md`, `reviews/08-…`). Such a reference is
#: unresolvable in a clone by construction, which is a §18 observation about
#: history, not a broken pointer in active material. Classified — not
#: silenced: every one is printed under CG-1b-history.
HISTORICAL_PACKET_TARGET = (
    re.compile(r"^(\.\./)*final-prespec/"),
    re.compile(r"^(\.\./)*rfcs/RFC-\d{4}-[a-z0-9-]+\.md$"),
    re.compile(r"^(\.\./)*(topology|history|matrix-rows)/"),
    re.compile(r"^(\.\./)*reviews/\d{2}-"),
    re.compile(r"^(\.\./)*scripts/verify_(rfcs|rev7)\.(py|sh)$"),
)


def _is_forward(target):
    # Match both directions. A forward ref is stored as a repo-root path, but
    # it is *cited* the way every other path reference is written here — as a
    # suffix (`decisions/ACCEPTANCE-ACT-RECORD.md`). Testing only `f in target`
    # sees the root-path form and misses every suffix citation of the same
    # artifact, which is how a by-design absence gets reported as a broken link.
    return any(f in target or f.endswith("/" + target) or f == target
               for f in FORWARD_REFS)


def _is_historical_packet(target):
    return any(p.match(target) for p in HISTORICAL_PACKET_TARGET)


def _resolve(citing, target, all_paths):
    """Resolve relative to the citing file, to the repo root, or as a suffix.

    Path references here are written as *citations* — `RFC-0002/README.md`
    cited from a package report means the module of that name, wherever the
    package keeps it — so suffix matching models how they are actually
    written. Anything resolving only by suffix still resolves in a clone.
    """
    for cand in (os.path.join(os.path.dirname(citing), target),
                 os.path.join(ROOT, target)):
        if os.path.exists(os.path.normpath(os.path.join(ROOT, cand)
                                           if not os.path.isabs(cand) else cand)):
            return True
    t = os.path.normpath(target).replace(os.sep, "/").lstrip("./")
    if not t:
        return False
    return any(p == t or p.endswith("/" + t) for p in all_paths)


def cg1_links(paths, res):
    all_paths = set(paths)
    n_links = n_paths = 0
    broken_links, broken_paths, forward, historical = [], [], set(), []
    for rel in md_files(paths):
        txt = read(rel)
        for m in MD_LINK.finditer(txt):
            t = m.group("t").split("#")[0].strip()
            if not t or t.startswith(EXTERNAL):
                continue
            n_links += 1
            if _is_forward(t):
                forward.add(t)
                continue
            if not _resolve(rel, t, all_paths):
                broken_links.append(f"{rel} -> {t}")
        for m in CODE_PATH.finditer(txt):
            t = m.group("t")
            if "/" not in t or t.startswith(EXTERNAL):
                continue
            # `_bootstrap/**` is git-excluded by design; CG-12 owns it.
            if t.startswith("_bootstrap/"):
                continue
            n_paths += 1
            if _is_forward(t):
                forward.add(t)
                continue
            if not _resolve(rel, t, all_paths):
                if _is_historical_packet(t):
                    historical.append(f"{rel} -> {t}")
                else:
                    broken_paths.append(f"{rel} -> {t}")

    if n_links == 0:
        res.add("WARN", "CG-1a  markdown links resolve", 0, 0, "link",
                note="nothing examined — check verified nothing")
    else:
        res.add("FAIL" if broken_links else "OK", "CG-1a  markdown links resolve",
                n_links, len(broken_links), "link",
                details=sorted(set(broken_links)))
    if n_paths == 0:
        res.add("WARN", "CG-1b  code-span path references resolve", 0, 0, "reference",
                note="nothing examined — check verified nothing")
    else:
        res.add("FAIL" if broken_paths else "OK",
                "CG-1b  code-span path references resolve",
                n_paths, len(broken_paths), "reference",
                details=sorted(set(broken_paths)))
    res.add("WARN", "CG-1c  declared forward references", len(forward), 0, "target",
            note="skipped by design — an owner act creates these",
            details=sorted(forward))
    uniq_hist = sorted(set(historical))
    res.add("WARN", "CG-1d  frozen-packet references", len(uniq_hist), 0,
            "reference",
            note="unresolvable in a clone by construction — the rev9 working "
                 "packet lived under the git-excluded `_bootstrap/`",
            details=uniq_hist)


# --------------------------------------------------------------- CG-2

RETIRED_PHRASE = "ACCEPT FOUNDATIONAL RFCS"

#: A retirement notice must be able to name the phrase it retires, and the
#: historical record must be able to quote what was superseded. Allowlisted
#: by path prefix, each with the reason it is allowed to carry the phrase.
RETIRED_PHRASE_ALLOW = (
    (f"{CRAFT}/INSTALL-RECORD.md", "states the phrase is retired and satisfies nothing"),
    (f"{CANDIDATES}/round-2026-08/", "this round's process record and delta register"),
    (f"{CANDIDATES}/history/", "frozen rev9 corpus and per-RFC amendment history"),
    (f"{CANDIDATES}/reviews/", "raw reviewer output, stored verbatim"),
    (f"{CANDIDATES}/00-README.md", "records the phrase as retired at rev10"),
    (f"{CANDIDATES}/10-EXIT-REPORT.md", "records the phrase as retired at rev10"),
    (f"{CANDIDATES}/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md",
     "the acceptance record that retires it"),
    (f"{DECISIONS}/OWNER-ANSWERS-2026-08-01.md",
     "owner ruling that the phrase was not performed"),
    (f"{DECISIONS}/PROCESS-LESSONS.md",
     "records the acceptance-authority migration, of which the phrase's "
     "unconditional retirement is one step"),
    ("AGENTS.md", "states the phrase is retired and satisfies nothing"),
    (f"{CANDIDATES}/round-2026-08/OWNER-ROUND-CHARTER.md",
     "owner-supplied round charter; quotes the phrase as a search token"),
    (SELF_REL, "this checker names the phrase in order to detect it"),
)

#: `about/**` is the upstream skill convention; this repository deliberately
#: has no such tree. Naming it as *guidance not to create one*, or as a
#: historical divergence note, is correct. Naming it as an authority path is
#: the defect.
ABOUT_SCOPE = ("AGENTS.md", "README.md")
ABOUT_ALLOW = (
    (".claude/skills/heart-and-soul/SKILL.md", "no-about/-tree guidance"),
    (".codex/skills/heart-and-soul/SKILL.md", "no-about/-tree guidance"),
    (f"{CRAFT}/README.md", "historical note on the upstream pillar home"),
)
ABOUT_PAT = re.compile(r"(?<![\w/.-])about/")


def _allow_hit(rel, allow):
    for prefix, reason in allow:
        if rel == prefix or rel.startswith(prefix):
            return reason
    return None


def cg2_retired_tokens(paths, res):
    files = [p for p in paths
             if p.endswith((".md", ".txt", ".yaml", ".yml", ".py"))]
    findings, allowed = [], []
    for rel in files:
        txt = read(rel)
        if RETIRED_PHRASE not in txt:
            continue
        reason = _allow_hit(rel, RETIRED_PHRASE_ALLOW)
        lines = [i for i, ln in enumerate(txt.splitlines(), 1)
                 if RETIRED_PHRASE in ln]
        if reason:
            allowed.append(f"{rel}:{','.join(str(i) for i in lines)} — {reason}")
        else:
            findings += [f"{rel}:{i} — retired phrase outside the allowlist"
                         for i in lines]
    res.add("FAIL" if findings else "OK",
            "CG-2a  retired acceptance phrase confined", len(files),
            len(findings), "file", details=findings)
    res.add("WARN", "CG-2b  retired-phrase allowlist", len(allowed), 0, "file",
            note="declared historical/quoting contexts", details=sorted(allowed))

    scope = [p for p in ABOUT_SCOPE if p in set(paths)]
    hits = []
    for rel in scope:
        for i, ln in enumerate(read(rel).splitlines(), 1):
            if ABOUT_PAT.search(ln):
                hits.append(f"{rel}:{i} — `about/` named in an instruction file")
    res.add("FAIL" if hits else ("OK" if scope else "WARN"),
            "CG-2c  `about/` absent from AGENTS/README", len(scope),
            len(hits), "file",
            note=None if scope else "neither file present — nothing examined",
            details=hits)
    allow_present = [f"{p} — {r}" for p, r in ABOUT_ALLOW if p in set(paths)]
    res.add("WARN", "CG-2d  `about/` allowlist", len(allow_present), 0, "file",
            note="guidance and historical mentions, out of CG-2c scope",
            details=allow_present)


# --------------------------------------------------------------- CG-3

STALE_ROUTES = ("_bootstrap/prompts/",)


def cg3_stale_routing(paths, res):
    files = [p for p in paths if p.endswith((".md", ".txt", ".yaml", ".yml"))]
    findings = []
    for rel in files:
        if rel == SELF_REL:
            continue
        for i, ln in enumerate(read(rel).splitlines(), 1):
            for route in STALE_ROUTES:
                if route in ln:
                    findings.append(f"{rel}:{i} — routes to `{route}`")
    res.add("FAIL" if findings else "OK",
            "CG-3   stale bootstrap routing absent", len(files),
            len(findings), "file", details=findings)


# --------------------------------------------------------------- CG-4

BANNER_LINES = 10
#: A manifest is a digest list; a banner would change its digest surface, and
#: the acceptance record owns its candidate status.
BANNER_EXEMPT = (f"{TOPOLOGY_CANDIDATES}/BUNDLE-MANIFEST.md",)


def cg4_candidate_banners(paths, res):
    targets = []
    top_readme = f"{CANDIDATES}/00-README.md"
    if top_readme in set(paths):
        targets.append(top_readme)
    #: Topology bundle members are digest-bound by BUNDLE-MANIFEST.md (the
    #: act-3 subject); stuffing a banner word into each member would churn
    #: the offered digest for labeling alone. The directory-level candidate
    #: marker (TRACKING-NOTE.md, outside the member set) satisfies CG-4 for
    #: the members, provided it exists and itself carries the banner.
    topology_note = f"{TOPOLOGY_CANDIDATES}/TRACKING-NOTE.md"
    topology_note_ok = (topology_note in set(paths)
                        and "candidate" in "\n".join(
                            read(topology_note).splitlines()[:BANNER_LINES]).lower())
    for rel in paths:
        if rel.startswith(f"{CANDIDATES}/policy-candidates/") and rel.endswith(".md"):
            targets.append(rel)
        elif (rel.startswith(f"{TOPOLOGY_CANDIDATES}/") and rel.endswith(".md")
              and rel not in BANNER_EXEMPT):
            if rel == topology_note or not topology_note_ok:
                targets.append(rel)
    if topology_note in set(paths) and topology_note not in targets:
        targets.append(topology_note)
    findings = []
    for rel in sorted(set(targets)):
        head = "\n".join(read(rel).splitlines()[:BANNER_LINES]).lower()
        if "candidate" not in head:
            findings.append(f"{rel} — no 'candidate' in the first "
                            f"{BANNER_LINES} lines")
    status = "FAIL" if findings else ("OK" if targets else "WARN")
    res.add(status, "CG-4   candidate homes carry candidate banners",
            len(set(targets)), len(findings), "file",
            note=None if targets else "no candidate-home files found — nothing examined",
            details=findings)


# --------------------------------------------------------------- CG-5

FALSE_BANNERS = (
    "this copy is the bootstrap-phase record",
    "this file is the bootstrap-phase record",
    "this directory is the bootstrap-phase record",
)
CANONICAL_MARK = "canonical home"
BANNER_POSITIVE_LINES = 3
#: The install record is provenance, not a policy banner: it describes where
#: the policies came from and is expected to name the bootstrap-phase copy.
CRAFT_POSITIVE_EXEMPT = (f"{CRAFT}/INSTALL-RECORD.md",)


def cg5_craft_banners(paths, res):
    craft_files = sorted(p for p in paths
                         if p.startswith(f"{CRAFT}/") and p.endswith(".md"))
    findings = []
    for rel in craft_files:
        low = read(rel).lower()
        for bad in FALSE_BANNERS:
            if bad in low:
                findings.append(f"{rel} — claims \"{bad}\" at the canonical home")
        if rel in CRAFT_POSITIVE_EXEMPT:
            continue
        head = "\n".join(read(rel).splitlines()[:BANNER_POSITIVE_LINES]).lower()
        if CANONICAL_MARK not in head:
            findings.append(f"{rel} — banner does not name this the "
                            f"{CANONICAL_MARK} in its first "
                            f"{BANNER_POSITIVE_LINES} lines")
    status = "FAIL" if findings else ("OK" if craft_files else "WARN")
    res.add(status, "CG-5   canonical craft banners truthful", len(craft_files),
            len(findings), "file",
            note=None if craft_files else "craft tree absent — nothing examined",
            details=findings)


# --------------------------------------------------------------- CG-6

ACCEPTED_HOMES = (
    (".syzygy/governance/contracts/rfcs", "created only by owner act 1"),
    (".syzygy/map/topology", "created only by owner act 3"),
)


def cg6_accepted_homes(res):
    findings = []
    for rel, why in ACCEPTED_HOMES:
        if os.path.exists(os.path.join(ROOT, rel)):
            findings.append(f"{rel} exists — {why}; no act has been recorded")
    res.add("FAIL" if findings else "OK",
            "CG-6   accepted homes not yet created", len(ACCEPTED_HOMES),
            len(findings), "home", details=findings)


# --------------------------------------------------------------- CG-7

MANIFEST = f"{CANDIDATES}/ACTIVE-CONTRACT-MANIFEST.txt"
DIGEST_ROW = re.compile(r"^(?P<sha>[0-9a-f]{64})\s+(?P<path>\S.*)$")
#: The manifest's *own* sha256 is the argument of owner act 1, so the
#: acceptance record and the manifest must agree. They are edited by
#: different hands at different times; nothing but a check keeps them
#: together.
ACCEPTANCE_RECORD = f"{CANDIDATES}/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md"
ACT1_ARG = re.compile(r"ACCEPT COMPACTED FOUNDATIONAL RFCS:\s*(?P<sha>[0-9a-f]{64})")


def sha256_file(abspath):
    h = hashlib.sha256()
    with open(abspath, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def cg7_manifest(paths, res):
    if MANIFEST not in set(paths):
        res.add("WARN", "CG-7a  manifest digests valid", 0, 0, "entry",
                note=f"{MANIFEST} not present — nothing examined")
        res.add("WARN", "CG-7b  act-1 argument matches the manifest", 0, 0,
                "record", note="no manifest to compare against — nothing examined")
        return
    findings, n = [], 0
    for i, ln in enumerate(read(MANIFEST).splitlines(), 1):
        m = DIGEST_ROW.match(ln.strip())
        if not m:
            continue
        n += 1
        target = os.path.join(ROOT, CANDIDATES, m.group("path").strip())
        if not os.path.exists(target):
            findings.append(f"{MANIFEST}:{i} — {m.group('path')} does not exist")
            continue
        actual = sha256_file(target)
        if actual != m.group("sha"):
            findings.append(f"{MANIFEST}:{i} — {m.group('path')} digest "
                            f"{actual[:12]}… != manifest {m.group('sha')[:12]}…")
    manifest_sha = sha256_file(os.path.join(ROOT, MANIFEST))
    status = "FAIL" if findings else ("OK" if n else "WARN")
    res.add(status, "CG-7a  manifest digests valid", n, len(findings), "entry",
            note=(f"manifest sha256 {manifest_sha} (the act-1 argument)"
                  if n else "no digest rows parsed — nothing examined"),
            details=findings)

    if ACCEPTANCE_RECORD not in set(paths):
        res.add("WARN", "CG-7b  act-1 argument matches the manifest", 0, 0,
                "record", note=f"{ACCEPTANCE_RECORD} not present — nothing examined")
        return
    stated = ACT1_ARG.findall(read(ACCEPTANCE_RECORD))
    if not stated:
        res.add("WARN", "CG-7b  act-1 argument matches the manifest", 1, 0,
                "record", note="no `ACCEPT COMPACTED FOUNDATIONAL RFCS: <sha>` "
                               "found — nothing compared")
        return
    bad = [s for s in set(stated) if s != manifest_sha]
    res.add("FAIL" if bad else "OK", "CG-7b  act-1 argument matches the manifest",
            len(set(stated)), len(bad), "argument",
            details=[f"{ACCEPTANCE_RECORD} offers {s[:12]}… but the manifest "
                     f"now hashes to {manifest_sha[:12]}… — the act would bind "
                     f"a package that no longer exists" for s in sorted(bad)])

    # CG-7c — the other three digest-bound acts. Act 1 alone was checked until
    # 2026-08-05, so a truthful "1 examined" covered a population of 4 and
    # three stale act arguments passed unseen (round review RB-3 F1).
    record = read(ACCEPTANCE_RECORD)
    others = [
        ("act 2 (craft CC-TEST-2)",
         os.path.join(ROOT, CRAFT, "testing-and-verification.md"),
         re.compile(r"CC-TEST-2@([0-9a-f]{64})")),
        ("act 3 (topology bundle)",
         os.path.join(ROOT, TOPOLOGY_CANDIDATES, "BUNDLE-MANIFEST.md"),
         re.compile(r"ACCEPT TOPOLOGY:\s*`?([0-9a-f]{64})")),
        ("act 4 (project overview)",
         os.path.join(ROOT, ".syzygy/intent/OVERVIEW.md"),
         re.compile(r"ADOPT PROJECT OVERVIEW:\s*`?([0-9a-f]{64})")),
    ]
    findings, examined = [], 0
    for label, subject, pat in others:
        args = set(pat.findall(record))
        if not args:
            findings.append(f"{label} — no digest argument found in "
                            f"{ACCEPTANCE_RECORD}; the act cannot be performed "
                            f"as written")
            examined += 1
            continue
        if not os.path.exists(subject):
            findings.append(f"{label} — subject {subject} does not exist")
            examined += len(args)
            continue
        actual = sha256_file(subject)
        for a in sorted(args):
            examined += 1
            if a != actual:
                findings.append(f"{label} — record offers {a[:12]}… but the "
                                f"subject hashes to {actual[:12]}… — the act "
                                f"would bind an artifact state that no longer "
                                f"exists")
    res.add("FAIL" if findings else ("OK" if examined else "WARN"),
            "CG-7c  acts 2/3/4 arguments match their subjects",
            examined, len(findings), "argument",
            note=None if examined else "no act arguments found — nothing examined",
            details=findings)

    cg7d_quoted_elsewhere(paths, res)


#: Every act phrase, with the artifact whose sha256 is its only valid
#: argument. CG-7d applies these to *every* file in the corpus, because the
#: round's headline defect was a digest that was correct in the manifest and
#: stale in the document that offered it (six independent reviewers, RB-1 F1
#: … RB-8 F1). A digest quoted anywhere is a promise about an artifact; the
#: artifact is the only thing that can keep it.
ACT_SUBJECTS = (
    ("ACCEPT COMPACTED FOUNDATIONAL RFCS", MANIFEST,
     re.compile(r"ACCEPT COMPACTED FOUNDATIONAL RFCS:\s*`?([0-9a-f]{64})")),
    ("CONFIRM CRAFT AMENDMENT: CC-TEST-2",
     f"{CRAFT}/testing-and-verification.md",
     re.compile(r"CC-TEST-2@([0-9a-f]{64})")),
    ("ACCEPT TOPOLOGY", f"{TOPOLOGY_CANDIDATES}/BUNDLE-MANIFEST.md",
     re.compile(r"ACCEPT TOPOLOGY:\s*`?([0-9a-f]{64})")),
    ("ADOPT PROJECT OVERVIEW", ".syzygy/intent/OVERVIEW.md",
     re.compile(r"ADOPT PROJECT OVERVIEW:\s*`?([0-9a-f]{64})")),
    # Act 5 needs no phrase — VIS-4 adoption is the owner's own words. The
    # round charter offers a phrase form anyway, so it is made available and
    # checked; an optional act with an unchecked digest would be the same
    # defect as the four this check exists for.
    ("ADOPT DOCTRINE AMENDMENT: D3",
     f"{CANDIDATES}/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md",
     re.compile(r"ADOPT DOCTRINE AMENDMENT:\s*D3@([0-9a-f]{64})")),
)

#: Files that quote a stale act argument *as* a retired value, on purpose —
#: the revision table in the acceptance record and the round's own records.
#: They are read as history, so a mismatch there is the point, not a defect.
#: Raw reviewer output is never edited, so it is exempt by construction.
ACT_QUOTE_EXEMPT = (
    f"{CANDIDATES}/round-2026-08/reviews/",
    f"{CANDIDATES}/round-2026-08b/reviews/",
    f"{CANDIDATES}/reviews/",
    f"{CANDIDATES}/history/",
    f"{CANDIDATES}/fixtures/",
    f"{CANDIDATES}/00-README.md",
    f"{CANDIDATES}/10-EXIT-REPORT.md",
    f"{CANDIDATES}/round-2026-08/OWNER-ROUND-CHARTER.md",
    SELF_REL,
)


def cg7d_quoted_elsewhere(paths, res):
    """Any file quoting an act phrase must quote its subject's current digest.

    A digest is owned by the artifact it names. Quoting one elsewhere is
    convenience, and convenience goes stale silently — which is exactly how
    all four act arguments in the acceptance record came to offer packages
    that no longer existed. This check makes every copy load-bearing.
    """
    #: A digest that its own line calls retired/stale/superseded is history,
    #: not an offer. This is the one exemption granted per-line rather than
    #: per-file, so a record can keep what it used to offer without the
    #: keeping being read as an offer.
    retired = re.compile(r"\b(retired|stale|superseded|pre-amendment|"
                         r"historical)\b", re.I)
    #: The marker must sit in the 60 characters immediately *before* the
    #: quotation. A marker later in the line does not exempt it — the
    #: acceptance record's own rows say "the rev9 argument is stale" after
    #: offering the current one, and those offers must stay checked.
    LOOKBEHIND = 60
    subjects = {}
    for label, rel, pat in ACT_SUBJECTS:
        full = os.path.join(ROOT, rel)
        subjects[label] = sha256_file(full) if os.path.exists(full) else None
    findings, examined = [], 0
    for rel in paths:
        if any(rel.startswith(x) or rel == x for x in ACT_QUOTE_EXEMPT):
            continue
        if not rel.endswith(".md"):
            continue
        body = read(rel)
        if not body:
            continue
        for label, subj_rel, pat in ACT_SUBJECTS:
            for line_no, line in enumerate(body.splitlines(), 1):
                for m in pat.finditer(line):
                    arg = m.group(1)
                    if retired.search(line[max(0, m.start() - LOOKBEHIND):
                                           m.start()]):
                        continue
                    examined += 1
                    current = subjects[label]
                    if current is None:
                        findings.append(
                            f"{rel}:{line_no} — quotes `{label}` but its "
                            f"subject {subj_rel} does not exist")
                    elif arg != current:
                        findings.append(
                            f"{rel}:{line_no} — quotes `{label}: {arg[:12]}…` "
                            f"but {subj_rel} hashes to {current[:12]}… — this "
                            f"copy is stale")
    res.add("FAIL" if findings else ("OK" if examined else "WARN"),
            "CG-7d  act digests quoted anywhere match their subjects",
            examined, len(findings), "quotation",
            note=(None if examined else
                  "no act digest quoted outside the exempt history — "
                  "nothing examined"),
            details=findings)


# --------------------------------------------------------------- CG-8

#: Charter §11.4 review triggers. These are decomposition triggers, not
#: validity laws — reported, never enforced. They are deliberately tighter
#: than the 7,000-word hard ceiling that
#: `candidates/scripts/verify_final_prespec.py` enforces with declared
#: justifications; the two are different instruments, not a contradiction.
BUDGETS = (
    ("README.md", 1200, "root README review trigger"),
    ("AGENTS.md", 1500, "AGENTS review trigger"),
)
MODULE_TRIGGER = 4000
MODULE_DECOMPOSE = 5000


def cg8_budgets(paths, res):
    present = set(paths)
    lines, n = [], 0
    for rel, limit, label in BUDGETS:
        if rel not in present:
            continue
        n += 1
        w = words(rel)
        if w > limit:
            lines.append(f"{rel} — {w} words, over the {limit}-word {label} "
                         f"(§11.4 trigger; review, not failure)")
    modules = sorted(p for p in paths
                     if p.startswith(f"{CANDIDATES}/rfcs/") and p.endswith(".md"))
    for rel in modules:
        n += 1
        w = words(rel)
        if w > MODULE_DECOMPOSE:
            lines.append(f"{rel} — {w} words, above {MODULE_DECOMPOSE}: §11.4 "
                         f"focused decomposition review")
        elif w > MODULE_TRIGGER:
            lines.append(f"{rel} — {w} words, over the {MODULE_TRIGGER}-word "
                         f"active-module trigger (§11.4)")
    res.add("WARN" if (lines or n == 0) else "OK",
            "CG-8   context budgets reported", n, len(lines), "artifact",
            note=("report-only — §11.4 triggers are decomposition prompts, "
                  "not failures" if n else "nothing examined"),
            details=lines)


# --------------------------------------------------------------- CG-9

#: Each authority type has exactly one home. A second copy in the candidate
#: package is a duplicate authority home — the reader cannot tell which one
#: binds.
AUTHORITY_HOMES = (
    ("doctrine", DOCTRINE, ("/doctrine/",)),
    ("craft-and-care", CRAFT, ("/craft-and-care/",)),
)


def cg9_duplicate_homes(paths, res):
    findings, n = [], 0
    for label, home, markers in AUTHORITY_HOMES:
        for rel in paths:
            if not rel.endswith(".md"):
                continue
            if any(mk in "/" + rel for mk in markers):
                n += 1
                if not rel.startswith(home + "/"):
                    findings.append(f"{rel} — {label} material outside its one "
                                    f"home {home}/")
    status = "FAIL" if findings else ("OK" if n else "WARN")
    res.add(status, "CG-9   duplicate authority homes absent", n,
            len(findings), "file",
            note=None if n else "no authority-home files found — nothing examined",
            details=findings)


# --------------------------------------------------------------- CG-10

PENDING = f"{DECISIONS}/PENDING-OWNER-DECISIONS.md"
ASOF = re.compile(r"as[- ]of\b[^\n]*", re.I)


def cg10_pending_asof(paths, res):
    if PENDING not in set(paths):
        res.add("WARN", "CG-10  pending register as-of reported", 0, 0, "register",
                note=f"{PENDING} not present — nothing examined")
        return
    head = read(PENDING).splitlines()[:40]
    hits = [f"{PENDING}:{i} — {ASOF.search(ln).group(0).strip()}"
            for i, ln in enumerate(head, 1) if ASOF.search(ln)]
    if not hits:
        res.add("FAIL", "CG-10  pending register as-of reported", 1, 1, "register",
                details=[f"{PENDING} — no 'As-of' line in the first 40 lines"])
        return
    res.add("WARN", "CG-10  pending register as-of reported", 1, 0, "register",
            note="reported for human currency judgement, never auto-verified",
            details=hits)


# --------------------------------------------------------------- CG-11

MUST_IGNORE = (".syzygy/cache/", ".syzygy/local/")


def cg11_ignored(res):
    gi = os.path.join(ROOT, ".gitignore")
    if not os.path.exists(gi):
        res.add("FAIL", "CG-11  cache/local git-ignored", 0, 1, "pattern",
                details=[".gitignore is absent"])
        return
    txt = read(".gitignore")
    entries = {ln.strip() for ln in txt.splitlines() if ln.strip()}
    findings = [f"{p} not present in .gitignore" for p in MUST_IGNORE
                if p not in entries and p.rstrip("/") not in entries]
    res.add("FAIL" if findings else "OK", "CG-11  cache/local git-ignored",
            len(MUST_IGNORE), len(findings), "pattern", details=findings)


# --------------------------------------------------------------- CG-12

#: A `_bootstrap/` mention is acceptable when it marks the target as
#: historical, founder-local, or otherwise unavailable to a clone. It is a
#: finding when an active artifact points a reader there for meaning it
#: cannot get elsewhere.
BOOTSTRAP_MARKERS = (
    "histor", "founder-local", "excluded", "unavailable", "archive",
    "bootstrap record", "bootstrap-phase", "fd-021", "fd-037",
    "frozen", "verbatim", "preserved", "process mirror", "never edit",
    "do not load", "do not cite", "not a source", "extracted under",
    "invisible to clone", "before this round", "source:", "git-excluded",
    "machine-local", "prior draft", "supersede", "not authority",
    "bootstrap home",
)
#: A marker rarely lands on the same physical line as the path in wrapped
#: prose — "`_bootstrap/…/DIRECTIVE.md` (owner-supplied,\npreserved verbatim…)"
#: is one sentence across two lines, and a section heading that marks a whole
#: list ("Research corpus links (archived, non-authoritative)") sits two lines
#: above its first entry. The window is ±2 lines; anything needing more than
#: that is not marked clearly enough for a reader either.
#: Absence markers. A sentence that says the tree is *not* there, *not*
#: read, or deliberately removed is not a citation of it — the round's own
#: reports say so repeatedly, and Test E's whole subject is the absence.
#: Kept separate from the historical markers above because they justify a
#: mention for a different reason.
BOOTSTRAP_ABSENCE_MARKERS = (
    "no `_bootstrap", "no _bootstrap", "without `_bootstrap",
    "without _bootstrap", "-free clone", "remove access",
    "no access", "did not read", "does not read", "cannot read",
    "no hidden semantic dependency", "nothing under `_bootstrap",
    "absent", "is not present", "excluded from clones",
)

MARKER_WINDOW = 2

#: A file may instead carry one prominent disclosure covering every pointer in
#: it — the pending-decision register does exactly this. Recognised only near
#: the top, where a reader meets it before the pointers.
DISCLOSURE_LINES = 40
DISCLOSURE_MARKERS = ("git-excluded", "founder-local", "absent from clones",
                      "unavailable", "cannot resolve those pointers")


def _has_file_disclosure(all_lines):
    head = all_lines[:DISCLOSURE_LINES]
    for i, ln in enumerate(head):
        if "_bootstrap/" not in ln:
            continue
        window = "\n".join(head[max(0, i - 2):i + 3]).lower()
        if any(mk in window for mk in DISCLOSURE_MARKERS):
            return window.strip().splitlines()[0][:80]
    return None
#: Derivation and archive subtrees: their whole job is to name the frozen
#: rev9 inputs a clause was migrated from. Allowlisted by prefix, counted,
#: printed.
BOOTSTRAP_ALLOW_PREFIX = (
    (f"{CANDIDATES}/history/", "frozen rev9 corpus and amendment history"),
    (f"{CANDIDATES}/reviews/", "raw reviewer output, stored verbatim"),
    (f"{CANDIDATES}/round-2026-08/reviews/",
     "raw reviewer output, stored verbatim — never edited, so a reviewer's "
     "own mention of the excluded tree (usually to record that they did not "
     "read it) is evidence, not an active citation"),
    (f"{CANDIDATES}/round-2026-08b/reviews/",
     "raw reviewer output, stored verbatim — same rule as the prior round; "
     "each round's review directory is allowlisted explicitly when opened, "
     "never by a `round-*/` glob, so opening one is a deliberate act"),
    (f"{CANDIDATES}/matrix-rows/", "per-RFC clause-migration provenance rows"),
    (f"{CANDIDATES}/04-CLAUSE-MIGRATION-MATRIX.md",
     "clause-migration provenance, cites frozen rev9 sources by construction"),
    (f"{CANDIDATES}/COMPACTION-CHARTER.md",
     "the superseded round's own working charter"),
    (f"{CANDIDATES}/round-2026-08/OWNER-ROUND-CHARTER.md",
     "owner-supplied round charter, quoted verbatim"),
    (SELF_REL, "this checker names the path in order to detect it"),
)


def cg12_bootstrap_sources(paths, res):
    files = [p for p in paths if p.endswith((".md", ".txt", ".yaml", ".yml"))]
    findings, allowed_files = [], []
    n_lines = 0
    for rel in files:
        reason = _allow_hit(rel, BOOTSTRAP_ALLOW_PREFIX)
        all_lines = read(rel).splitlines()
        hit_lines = [(i, ln) for i, ln in enumerate(all_lines, 1)
                     if "_bootstrap/" in ln]
        if not hit_lines:
            continue
        if not reason and _has_file_disclosure(all_lines):
            reason = "file-level disclosure that these pointers are git-excluded"
        if reason:
            allowed_files.append(f"{rel} ({len(hit_lines)} line(s)) — {reason}")
            continue
        for i, ln in hit_lines:
            n_lines += 1
            lo = max(0, i - 1 - MARKER_WINDOW)
            # Whitespace-normalized: a marker and its pointer routinely
            # land on opposite sides of a line wrap, and a matcher that
            # silently misses those would manufacture findings.
            window = " ".join(" ".join(all_lines[lo:i + MARKER_WINDOW]).split()).lower()
            if not any(mk in window for mk in
                       BOOTSTRAP_MARKERS + BOOTSTRAP_ABSENCE_MARKERS):
                findings.append(f"{rel}:{i} — cites `_bootstrap/` with no "
                                f"historical/unavailable marker: {ln.strip()[:90]}")
    status = "FAIL" if findings else ("OK" if n_lines else "WARN")
    res.add(status, "CG-12  no `_bootstrap/` cited as a required source",
            n_lines, len(findings), "citation",
            note=None if n_lines else "no citations examined",
            details=findings)
    res.add("WARN", "CG-12b `_bootstrap/` citation allowlist", len(allowed_files),
            0, "file", note="derivation and archive records",
            details=sorted(allowed_files))


# ------------------------------------------------- CG-13..CG-19 (round 08b)

RFCS_DIR = f"{CANDIDATES}/rfcs"
DEPENDS_RE = re.compile(r"^depends_on:\s*\[(.*?)\]\s*$", re.M)
ROUTING_MATRIX = f"{CANDIDATES}/SURFACE-CLAUSE-ROUTING-MATRIX.md"
FIXTURES_DIR = f"{CANDIDATES}/fixtures"
SUBSTRATE_LOCK = ".syzygy/governance/policies/GOVERNANCE-SUBSTRATE-LOCK.yaml"
TERM_REGISTRY = f"{CANDIDATES}/policy-candidates/TERM-REGISTRY.md"


def _module_deps(rel):
    m = DEPENDS_RE.search(read(rel))
    if not m:
        return None
    return set(x.strip() for x in m.group(1).split(",") if x.strip())


def _rfc_modules():
    """Every contract module, repo-relative, sorted."""
    out = []
    base = os.path.join(ROOT, RFCS_DIR)
    for dirpath, _, names in os.walk(base):
        for n in sorted(names):
            if n.endswith(".md"):
                out.append(os.path.relpath(os.path.join(dirpath, n),
                                           ROOT).replace(os.sep, "/"))
    return sorted(out)


def cg13_dependency_graph(res, modules=None):
    """`depends_on` resolves, and a package README equals its modules' union.

    Two defects this makes unrepresentable-by-report rather than merely
    absent. **Dangling**: a dependency naming a contract with no module in
    the package — the graph's only remaining asymmetry class now that
    `provides_to` is derived. **README drift**: a package README's
    dependency row is the package-level view, so it must be exactly the
    union of its modules' rows. When round 08b added module-level edges,
    two READMEs silently stopped matching their own packages; nothing
    reported it, because regenerating a knowingly-drifted index reproduces
    the drift.
    """
    modules = modules if modules is not None else _rfc_modules()
    known = set()
    for rel in modules:
        m = re.search(r"(RFC-\d{4})", os.path.basename(rel)) or \
            re.search(r"(RFC-\d{4})", rel)
        if m:
            known.add(m.group(1))
    findings, examined = [], 0
    packages = {}
    for rel in modules:
        deps = _module_deps(rel)
        if deps is None:
            continue
        for d in sorted(deps):
            examined += 1
            if d not in known:
                findings.append(f"{rel} — depends_on `{d}`, which has no "
                                f"module in the package (dangling)")
        parent = os.path.dirname(rel)
        if os.path.basename(parent).startswith("RFC-"):
            packages.setdefault(parent, {})[os.path.basename(rel)] = deps
    for pkg, mods in sorted(packages.items()):
        if "README.md" not in mods:
            continue
        readme = mods["README.md"]
        union = set().union(*[v for k, v in mods.items()
                              if k != "README.md"]) if len(mods) > 1 else set()
        examined += 1
        if readme != union:
            findings.append(
                f"{pkg}/README.md — depends_on is not the union of its "
                f"modules': extra {sorted(readme - union) or '[]'}, "
                f"missing {sorted(union - readme) or '[]'}")
    res.add("FAIL" if findings else ("OK" if examined else "WARN"),
            "CG-13  dependency edges resolve; README = module union",
            examined, len(findings), "edge",
            note=None if examined else "no depends_on rows found",
            details=findings)


def cg14_install_routes(res, record=None):
    """Every install source/destination the acceptance record names is valid.

    An act that installs candidate material states where it reads from and
    where it writes to. A wrong source silently installs the wrong bytes; a
    destination that is not a declared act-created home means either the
    home already exists (the act is not an act) or the path is a typo that
    surfaces only mid-ceremony. Both were live: act 3's install source named
    a directory that had been renamed.
    """
    body = record if record is not None else read(ACCEPTANCE_RECORD)
    if not body:
        res.add("WARN", "CG-14  acceptance install routes valid", 0, 0,
                "route", note=f"{ACCEPTANCE_RECORD} unreadable")
        return
    pat = re.compile(r"`(?P<src>[A-Za-z0-9_.\-/]+/)`\s*(?:→|->)\s*"
                     r"`(?P<dst>[A-Za-z0-9_.\-/]+/)`")
    findings, examined = [], 0
    for line_no, line in enumerate(body.splitlines(), 1):
        for m in pat.finditer(line):
            examined += 1
            src, dst = m.group("src"), m.group("dst")
            if not os.path.isdir(os.path.join(ROOT, src.rstrip("/"))):
                findings.append(f"line {line_no} — install source `{src}` "
                                f"does not exist; the act would read nothing")
            if os.path.exists(os.path.join(ROOT, dst.rstrip("/"))):
                findings.append(f"line {line_no} — install destination "
                                f"`{dst}` already exists; an act that creates "
                                f"it cannot be unperformed")
            elif not _forward_declared(dst):
                findings.append(f"line {line_no} — install destination "
                                f"`{dst}` is neither present nor a declared "
                                f"forward reference; it is a typo or an "
                                f"undeclared home")
    res.add("FAIL" if findings else ("OK" if examined else "WARN"),
            "CG-14  acceptance install routes valid", examined,
            len(findings), "route",
            note=None if examined else "no `source/ → destination/` pairs "
                                       "found in the acceptance record",
            details=findings)


#: Sources whose text is evidence rather than assertion: raw reviewer output
#: stored verbatim (never edited — editing it destroys what the allowlist
#: exists to protect), owner-supplied charters quoted as given, and the
#: frozen history. A reviewer quoting a digest is recording what they read,
#: and a reviewer calling the term registry "canonical" is reporting how the
#: corpus reads to them — which is the finding, not a defect to correct.
VERBATIM_SOURCES = (
    f"{CANDIDATES}/reviews/",
    f"{CANDIDATES}/round-2026-08/reviews/",
    f"{CANDIDATES}/round-2026-08b/reviews/",
    f"{CANDIDATES}/history/",
    f"{CANDIDATES}/round-2026-08/OWNER-ROUND-CHARTER.md",
    SELF_REL,
)


#: Files whose digests name artifacts outside the act/manifest population —
#: so "prefixes no current act argument" is true and not a defect. Declared
#: rather than pattern-matched, because a rule broad enough to infer this
#: would also excuse a genuinely stale act quote.
DIGEST_SCOPE_EXEMPT = (
    (f"{DECISIONS}/LICENSE-DECISION-PACKET.md",
     "cites the digest of the founder-local directive that commissioned it, "
     "not an act argument"),
)


TRUNC_DIGEST = re.compile(r"`?\b(?P<d>[0-9a-f]{8,63})(?:…|\.\.\.)")


def cg15_truncated_digests(paths, res, corpus=None):
    """Truncated digest quotes must still prefix a current act argument.

    CG-7d is structurally blind to these: it matches a full 64-hex digest
    beside an act phrase, so `08793ddf70f3…` — no phrase, 12 characters —
    passes it unseen. Two such quotes sat stale in the artifact inventory
    while CG-7d reported zero findings over eight quotations, and a review
    that searched the way CG-7d searches concluded there were none. A
    convenience truncation is still a promise.
    """
    current = set()
    for label, rel, _pat in ACT_SUBJECTS:
        full = os.path.join(ROOT, rel)
        if os.path.exists(full):
            current.add(sha256_file(full))
    d3 = os.path.join(ROOT, CANDIDATES,
                      "DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md")
    if os.path.exists(d3):
        current.add(sha256_file(d3))
    manifest = os.path.join(ROOT, CANDIDATES, "ACTIVE-CONTRACT-MANIFEST.txt")
    if os.path.exists(manifest):
        current.add(sha256_file(manifest))
        for line in read(f"{CANDIDATES}/ACTIVE-CONTRACT-MANIFEST.txt").splitlines():
            if line and line[0] in "0123456789abcdef":
                current.add(line.split()[0])
    #: Unlike CG-7d, the marker may sit anywhere on the line. CG-7d needs a
    #: strict lookbehind because it matches full 64-hex act *arguments*, and a
    #: row that offers the current one while noting the old one is stale must
    #: stay checked. A truncated digest is never an act argument — CG-7b/c
    #: require the full 64 — so a whole-line marker cannot excuse a live offer
    #: here, and demanding a lookbehind would instead flag every honest
    #: "…is stale and satisfies nothing" row in the acceptance record.
    retired = re.compile(r"\b(retired|stale|superseded|pre-amendment|"
                         r"historical|no longer|prior|previous|mismatch|"
                         r"never carried|satisfies nothing)\b", re.I)
    #: A whole file may be historical — but only when it *says so as a
    #: banner*, not merely because the word appears in its prose. The loose
    #: form of this test exempted 49 files including the live routing matrix,
    #: which is the silent-exemption failure this checker exists to prevent.
    #: Required: a bolded or blockquoted opening line whose first words mark
    #: the whole artifact superseded or historical.
    superseded_banner = re.compile(
        r"^>?\s*[#*\s]*(SUPERSEDED|Superseded|Historical|RETIRED|Retired)\b",
        re.M)
    items = corpus if corpus is not None else [
        (rel, read(rel)) for rel in paths
        if rel.endswith(".md") and not any(
            rel.startswith(x) or rel == x for x in ACT_QUOTE_EXEMPT)]
    findings, examined, historical_files = [], 0, []
    for rel, body in items:
        if _allow_hit(rel, DIGEST_SCOPE_EXEMPT):
            continue
        lines = body.splitlines()
        if superseded_banner.search("\n".join(lines[:12])):
            historical_files.append(rel)
            continue
        for line_no, line in enumerate(lines, 1):
            for m in TRUNC_DIGEST.finditer(line):
                d = m.group("d")
                if len(d) < 8:
                    continue
                # Also the line before: a wrapped sentence puts "now retired"
                # on one line and the digest on the next, and a per-line test
                # would report the honest half of a two-line disclosure.
                prev = lines[line_no - 2] if line_no >= 2 else ""
                if retired.search(line) or retired.search(prev):
                    continue
                # A table column headed "prior/retired" marks its whole body.
                header = next((h for h in reversed(lines[:line_no - 1])
                               if h.startswith("|")
                               and not set(h) <= set("|- :")), "")
                if retired.search(header):
                    continue
                examined += 1
                if not any(c.startswith(d) for c in current):
                    findings.append(
                        f"{rel}:{line_no} — `{d}…` prefixes no current act "
                        f"argument or manifest entry; the quote is stale or "
                        f"names an artifact state that no longer exists")
    res.add("FAIL" if findings else ("OK" if examined else "WARN"),
            "CG-15  truncated digest quotes still current", examined,
            len(findings), "quotation",
            note=None if examined else "no truncated digest quotations found",
            details=findings)
    res.add("WARN", "CG-15b superseded records holding old digests",
            len(historical_files), 0, "file",
            note="carry a SUPERSEDED/Historical banner; their digests record "
                 "what was offered, not what is",
            details=sorted(historical_files))


def cg16_term_registry_status(paths, res, corpus=None):
    """Nothing may describe the term registry as accepted, adopted, or binding.

    It is candidate material with no owner act. The failure mode is not a
    lie but a drift: a summary calls it "the vocabulary", a later reader
    reads that as settled, and an unaccepted registry acquires authority by
    citation. Checked over every file that names it.
    """
    claim = re.compile(r"\b(adopted|accepted|approved|binding|authoritative|"
                       r"canonical)\b", re.I)
    items = corpus if corpus is not None else [
        (rel, read(rel)) for rel in paths if rel.endswith(".md")
        and not any(rel.startswith(x) or rel == x for x in VERBATIM_SOURCES)]
    findings, examined = [], 0
    for rel, body in items:
        if rel.endswith("TERM-REGISTRY.md"):
            continue
        for line_no, line in enumerate(body.splitlines(), 1):
            low = line.lower()
            at = low.find("term registry")
            if at < 0:
                at = line.find("TERM-REGISTRY")
            if at < 0:
                continue
            examined += 1
            # The claim word must sit next to the mention. Scanning the whole
            # line flagged a register row where "adopted" described doctrine's
            # three-state thesis two clauses away — a check that reports a
            # defect for an unrelated word is a check nobody will keep.
            window = line[max(0, at - 60):at + 90]
            m = claim.search(window)
            if m and not re.search(r"\b(not|never|un|no|candidate)\b\W{0,14}" +
                                   re.escape(m.group(0)), window, re.I):
                findings.append(f"{rel}:{line_no} — calls the term registry "
                                f"`{m.group(0)}`; it is candidate material "
                                f"with no owner act")
    res.add("FAIL" if findings else ("OK" if examined else "WARN"),
            "CG-16  term registry never described as accepted", examined,
            len(findings), "mention",
            note=None if examined else "term registry not mentioned anywhere",
            details=findings)


def cg17_routing_completeness(res, matrix=None, modules=None):
    """Every clause of RFC 0006-0011 is routed exactly once.

    The six phase rules are only as good as the enumeration behind them.
    The rev10 matrix classified 150 of 322 clauses, routed RFC-0006 not at
    all, and was cited as though it covered everything — a coverage claim
    resting on an enumeration that did not exist.
    """
    body = matrix if matrix is not None else read(ROUTING_MATRIX)
    if not body:
        res.add("WARN", "CG-17  surface clauses routed exactly once", 0, 0,
                "clause", note=f"{ROUTING_MATRIX} unreadable")
        return
    routed = {}
    for line in body.splitlines():
        m = re.match(r"\|\s*`?(RFC(?:6|7|8|9|10|11)-\d+(?:\([a-z]\))?)`?\s*\|",
                     line)
        if m:
            routed[m.group(1)] = routed.get(m.group(1), 0) + 1
    declared = set()
    for rel in (modules if modules is not None else _rfc_modules()):
        m = re.search(r"RFC-00(0[6-9]|1[01])", rel)
        if not m:
            continue
        n = int(m.group(0)[4:])
        for c in re.finditer(r"^\*\*(RFC%d-\d+(?:\([a-z]\))?)" % n,
                             read(rel), re.M):
            declared.add(c.group(1))
    findings = []
    for c in sorted(declared - set(routed)):
        findings.append(f"{c} — declared in a contract, absent from the matrix")
    for c, n in sorted(routed.items()):
        if n > 1:
            findings.append(f"{c} — routed {n} times; each clause takes one route")
    examined = len(declared | set(routed))
    res.add("FAIL" if findings else ("OK" if examined else "WARN"),
            "CG-17  surface clauses routed exactly once", examined,
            len(findings), "clause",
            note=None if examined else "no clause identities found",
            details=findings)


def _resolve_load_spec(spec):
    prefixes = {"doctrine:": DOCTRINE, "craft:": CRAFT}
    for pfx, home in prefixes.items():
        if spec.startswith(pfx):
            return os.path.join(home, spec[len(pfx):])
    return os.path.join(CANDIDATES, spec)


def cg18_fixture_freshness(res, fixtures=None):
    """Each context fixture's packet digest and word count still recompute.

    A fixture is the project's only measured evidence that one task can be
    given complete governed context without loading the corpus. When a
    contract module is edited the fixture's digest goes stale silently, and
    a stale fixture reads exactly like a fresh one.
    """
    items = fixtures
    if items is None:
        base = os.path.join(ROOT, FIXTURES_DIR)
        items = []
        if os.path.isdir(base):
            for n in sorted(os.listdir(base)):
                if n.startswith("context-selection-") and n.endswith(".md"):
                    items.append((f"{FIXTURES_DIR}/{n}",
                                  read(f"{FIXTURES_DIR}/{n}")))
    findings, examined = [], 0
    for rel, body in items:
        cmd = re.search(r"```\s*\n(scripts/context_load\.py[\s\S]*?)\n```", body)
        # The digest is the first hex quotation after the "Packet digest"
        # heading. Anchoring on the "(recompute" suffix instead silently
        # skipped the two fixtures that word-wrap before it — a parser that
        # examines 4 of 8 while reporting a count is the failure mode here.
        section = body.split("## Packet digest", 1)
        quoted = (re.search(r"`([0-9a-f]{8,64})(?:…|\.\.\.)?`", section[1])
                  if len(section) > 1 else None)
        if not cmd or not quoted:
            continue
        specs = [s for s in cmd.group(1).replace("\\\n", " ").split()
                 if s not in ("scripts/context_load.py",) and s.strip()]
        blob, words, missing = b"", 0, []
        for s in specs:
            path = os.path.join(ROOT, _resolve_load_spec(s))
            if not os.path.exists(path):
                missing.append(s)
                continue
            data = open(path, "rb").read()
            blob += data
            words += len(data.decode("utf-8", "replace").split())
        examined += 1
        if missing:
            findings.append(f"{rel} — mandatory load names {missing}, which "
                            f"do not exist; the fixture cannot be reproduced")
            continue
        actual = hashlib.sha256(blob).hexdigest()
        q = quoted.group(1)
        if not actual.startswith(q):
            findings.append(f"{rel} — packet digest `{q}…` but the declared "
                            f"mandatory set hashes to `{actual[:len(q)]}…`")
        claimed = re.search(r"Measured:\s*\*\*([\d,]+)\s*words", body)
        if claimed:
            examined += 1
            c = int(claimed.group(1).replace(",", ""))
            if c != words:
                findings.append(f"{rel} — claims {c:,} words; the declared "
                                f"mandatory set is {words:,}")
    res.add("FAIL" if findings else ("OK" if examined else "WARN"),
            "CG-18  context fixtures recompute", examined, len(findings),
            "measurement",
            note=None if examined else "no reproducible fixtures found",
            details=findings)


def cg19_substrate_lock(res, body=None):
    """Every substrate pin resolves publicly, and drift is declared.

    The engineering substrate this project's craft policy came from was
    pinned to a founder-machine path. Nothing mechanical could see it, so
    the pin's own drift rule was due to fire and did not — the installed
    tree had moved two commits past what the owner approved. A pin that
    cannot be checked from a clone is not a pin.
    """
    text = body if body is not None else read(SUBSTRATE_LOCK)
    if not text:
        res.add("WARN", "CG-19  substrate pins publicly resolvable", 0, 0,
                "pin", note=f"{SUBSTRATE_LOCK} unreadable")
        return
    findings, examined = [], 0
    blocks = re.split(r"\n(?=\w[\w_]*:\s*(?:#.*)?$)", text, flags=re.M)
    for b in blocks:
        name = re.match(r"(\w[\w_]*):\s*(?:#.*)?$", b.split("\n")[0])
        if not name:
            continue
        if not re.search(r"^\s*(repository|source|url|package):", b, re.M):
            continue
        examined += 1
        if not re.search(r"(https?://|npm:|pypi:|npm registry)", b):
            findings.append(f"`{name.group(1)}` — no public source URL; a "
                            f"reader outside this machine cannot resolve it")
        if re.search(r"^\s*drift:", b, re.M) and not re.search(
                r"status:\s*\"?(open|OPEN|absorbed|declined|surfaced)", b):
            findings.append(f"`{name.group(1)}` — declares drift with no "
                            f"disposition status; silent drift is the defect "
                            f"this lock exists to prevent")
    res.add("FAIL" if findings else ("OK" if examined else "WARN"),
            "CG-19  substrate pins publicly resolvable", examined,
            len(findings), "pin",
            note=None if examined else "no pinned substrates declared",
            details=findings)


# --------------------------------------------------------- self-test

def selftest():
    """Prove each new check can fail. A validator with no failing fixture is
    indistinguishable from a no-op, and this repository has shipped one.

    Each fixture below is a synthetic input crafted to trip exactly one
    check. The test asserts the check reports at least one finding on it —
    not that the repository is clean.
    """
    class Cap:
        def __init__(self): self.rows = []
        def add(self, status, name, examined, n, unit, note=None, details=None):
            self.rows.append((status, name, examined, n, details or []))

    cases = []

    c = Cap(); cg13_dependency_graph(c, modules=[])
    cases.append(("CG-13 empty corpus warns, never passes",
                  c.rows[0][0] == "WARN"))

    c = Cap()
    fake = ".syzygy/governance/contracts/candidates/rfcs/RFC-0001-x.md"
    cases.append(("CG-13 dangling edge detected", None))
    cases[-1] = ("CG-13 dangling edge detected",
                 _selftest_dangling())

    c = Cap(); cg14_install_routes(c, record="install `no-such-dir/` → `scripts/`")
    cases.append(("CG-14 bad source and existing destination detected",
                  c.rows[0][0] == "FAIL" and len(c.rows[0][4]) == 2))

    c = Cap()
    cg15_truncated_digests([], c, corpus=[("f.md", "digest `deadbeefcafe…`")])
    cases.append(("CG-15 stale truncated digest detected",
                  c.rows[0][0] == "FAIL"))

    c = Cap()
    cg15_truncated_digests([], c, corpus=[("f.md", "the retired `deadbeefcafe…`")])
    cases.append(("CG-15 retired-marked quote exempted",
                  c.rows[0][0] == "WARN"))

    c = Cap()
    cg16_term_registry_status([], c,
                              corpus=[("f.md", "the adopted term registry")])
    cases.append(("CG-16 'adopted term registry' detected",
                  c.rows[0][0] == "FAIL"))

    c = Cap()
    cg16_term_registry_status([], c,
                              corpus=[("f.md", "the term registry is not adopted")])
    cases.append(("CG-16 negated claim exempted", c.rows[0][0] == "OK"))

    c = Cap()
    cg17_routing_completeness(c, matrix="| `RFC6-1` | OS |\n| `RFC6-1` | OS |",
                              modules=[])
    cases.append(("CG-17 double-routed clause detected",
                  c.rows[0][0] == "FAIL"))

    c = Cap()
    cg18_fixture_freshness(c, fixtures=[("f.md",
        "```\nscripts/context_load.py no-such-file.md\n```\n"
        "## Packet digest\n`0000000000000000` (recompute")])
    cases.append(("CG-18 unreproducible fixture detected",
                  c.rows[0][0] == "FAIL"))

    c = Cap()
    cg19_substrate_lock(c, body="th_x:\n  source: /home/someone/local\n")
    cases.append(("CG-19 founder-local pin detected", c.rows[0][0] == "FAIL"))

    width = max(len(n) for n, _ in cases)
    bad = 0
    for name, ok in cases:
        print(f"  {'pass' if ok else 'FAIL'}  {name.ljust(width)}")
        bad += 0 if ok else 1
    print(f"\n{len(cases)} fixtures, {bad} failing — a check that cannot fail "
          f"is not a check")
    return 1 if bad else 0


def _selftest_dangling():
    class Cap:
        def __init__(self): self.rows = []
        def add(self, status, name, examined, n, unit, note=None, details=None):
            self.rows.append((status, name, examined, n, details or []))
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        pkg = os.path.join(d, RFCS_DIR)
        os.makedirs(pkg)
        rel = f"{RFCS_DIR}/RFC-0001-kernel.md"
        with open(os.path.join(d, rel), "w") as fh:
            fh.write("---\ndepends_on: [RFC-0099]\n---\n")
        global ROOT
        keep, ROOT = ROOT, d
        try:
            c = Cap()
            cg13_dependency_graph(c, modules=[rel])
            return c.rows[0][0] == "FAIL"
        finally:
            ROOT = keep


# --------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(
        description="Read-only governance checks. Never rewrites anything.")
    ap.add_argument("--scope", choices=("clone", "tracked"), default="clone",
                    help="clone (default): tracked files plus untracked files "
                         "git does not ignore — what a clone will contain once "
                         "committed. tracked: `git ls-files` only.")
    ap.add_argument("--selftest", action="store_true",
                    help="run each check against a synthetic failing input "
                         "and report whether it detects the defect. Proves "
                         "the checks are not no-ops; examines no repository "
                         "file.")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    paths, tracked, source = corpus_paths(args.scope)

    existing = [p for p in paths if os.path.exists(os.path.join(ROOT, p))]
    missing = len(paths) - len(existing)
    print(f"repo root: {ROOT}")
    if source == "walk":
        print(f"scope:     filesystem walk — {len(existing)} file(s) examined. "
              "git is unavailable here, so tracked/ignored status is Unknown: "
              "CG-11 cannot run and `--scope tracked` is not honored. Every "
              "other check runs over the walked corpus.\n")
    else:
        print(f"scope:     {args.scope} — {len(existing)} file(s) examined "
              f"({len(tracked)} tracked, "
              f"{len(existing) - len([p for p in existing if p in tracked])} "
              f"untracked-not-ignored"
              f"{f', {missing} listed but absent' if missing else ''})\n")

    res = Results()
    cg1_links(existing, res)
    cg2_retired_tokens(existing, res)
    cg3_stale_routing(existing, res)
    cg4_candidate_banners(existing, res)
    cg5_craft_banners(existing, res)
    cg6_accepted_homes(res)
    cg7_manifest(existing, res)
    cg8_budgets(existing, res)
    cg9_duplicate_homes(existing, res)
    cg10_pending_asof(existing, res)
    if source == "git":
        cg11_ignored(res)
    else:
        res.add("WARN", "CG-11 ignore rules", 0, 0, unit="rule",
                note="git unavailable — ignore status is Unknown, "
                     "not clean; re-run inside a git checkout")
    cg12_bootstrap_sources(existing, res)
    cg13_dependency_graph(res)
    cg14_install_routes(res)
    cg15_truncated_digests(existing, res)
    cg16_term_registry_status(existing, res)
    cg17_routing_completeness(res)
    cg18_fixture_freshness(res)
    cg19_substrate_lock(res)
    res.report()
    return 1 if res.failed() else 0


if __name__ == "__main__":
    sys.exit(main())
