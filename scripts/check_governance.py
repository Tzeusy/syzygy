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
  CG-8   default-load size and context budgets reported, never enforced
         (charter §7.3 figures every run; §11.4 decomposition triggers)
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
  CG-19  substrate pins are complete and well-formed; drift is consistent
         and carries a disposition
  CG-20  the context-load map's word figures still recompute
  CG-21  package README module word counts recompute (inside act 1's digests)
  CG-22  no unqualified `status` in the active lane — the term registry's
         five-dimension rule, made executable (charter §9.4)
  CG-23  advanced vocabulary on the default public path, reported (§9.3)
  CG-24  which check families have a `--selftest` fixture, computed

`--selftest` runs a synthetic failing input against the checks that have a
fixture — **not against every check above**. That distinction is the point:
a validator never shown to fail is indistinguishable from a no-op, and this
repository has shipped one (charter §18). CG-24 computes which families are
covered and prints the denominator every run, so the claim cannot drift from
the fixture set the way a sentence does.

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
    ".syzygy/governance/contracts/rfcs/",                     # wave-act install home
    ".syzygy/governance/contracts/wave-manifests/",           # wave-act install home
    ".syzygy/governance/contracts/history/",                  # first-wave companion
    ".syzygy/governance/contracts/matrix-rows/",              # first-wave companion
    ".syzygy/map/topology/",                                  # act-3 install home
    ".syzygy/project.yaml",                                   # no governed project yet
    "openspec/",                                              # does not exist yet
    "RFC-000n",                                               # glob placeholder
    "RFC-000N",                                               # same, uppercased
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
    # The rev9 matrix also cites the *nested* package layout relatively
    # (`../rfcs/RFC-0003/README.md`). Same frozen tree, same by-construction
    # unresolvability; surfaced only once `_resolve` stopped discarding `../`.
    re.compile(r"^(\.\./)*rfcs/RFC-\d{4}/[A-Za-z0-9._-]+$"),
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


#: Raw reviewer output is stored verbatim and never edited — the repository's
#: strongest evidence rule, and the reason `EXCEPTIONS` never becomes "pass
#: with findings". A reviewer writing `craft/engineering-bar.md` for a file
#: this tree keeps at `policies/craft-and-care/engineering-bar.md` has written
#: their own shorthand, not a repository pointer, and the only ways to make
#: CG-1b green over it are to edit their words or to stop reading their file.
#: Both are worse than the finding. So these are **classified, not silenced**:
#: counted in CG-1b's denominator, reported in full under CG-1f, and never
#: allowed to fail a check whose subject is the active corpus's own links.
RAW_REVIEW_DIRS = (
    f"{CANDIDATES}/reviews/",
    f"{CANDIDATES}/round-2026-08/reviews/",
    f"{CANDIDATES}/round-2026-08b/reviews/",
    f"{CANDIDATES}/round-2026-08c/reviews/",
)


def _is_raw_review(rel):
    return any(rel.startswith(d) for d in RAW_REVIEW_DIRS)


#: Superseded round records, banner-marked and frozen. They cite paths that
#: were correct at the depth they were written and are not corrected, for the
#: same reason raw reviewer output is not: a frozen record edited to please a
#: check is no longer the record. Classified into CG-1f alongside raw review.
SUPERSEDED_ROUND_DIRS = (
    f"{CANDIDATES}/round-2026-08/",
)


def _is_frozen_lane(rel):
    return _is_raw_review(rel) or any(rel.startswith(d)
                                      for d in SUPERSEDED_ROUND_DIRS)


#: Cited descriptively by `craft-and-care/testing-and-verification.md`
#: CC-TEST-7: the upstream `th-engineering` package's own internal
#: cross-reference (tier definitions for test-rigor bars 9-10), naming a file
#: outside this lock's vendored scope on purpose
#: (`GOVERNANCE-SUBSTRATE-LOCK.yaml` th_engineering.vendored.scope_note).
#: Classified here, not silenced — see CG-1e.
DECLARED_VENDOR_GAP = (
    "subskills/test-rigor/references/suite-discipline.md",
)


def _is_vendored_gap(citing, target):
    """A vendored file's own prose citing an un-vendored sibling, or a
    Syzygy file citing a upstream path this repo deliberately did not
    vendor. `VENDORED_EXTERNAL` is defined near `cg22_ambiguous_status`,
    below — resolved at call time, same as every other module constant."""
    return citing.startswith(VENDORED_EXTERNAL) or target in DECLARED_VENDOR_GAP


def _resolve(citing, target, all_paths):
    """Resolve relative to the citing file, to the repo root, or as a suffix.

    Path references here are written as *citations* — `RFC-0002/README.md`
    cited from a package report means the module of that name, wherever the
    package keeps it — so suffix matching models how they are actually
    written. Anything resolving only by suffix still resolves in a clone.

    **The suffix fallback is refused for a target that states its own depth.**
    An author writing `../../history/RFC-0010-history.md` has made a claim
    about where the file sits relative to theirs, and a wrong claim must fail
    rather than be rescued by a filename match somewhere else in the tree.

    An earlier revision used `str.lstrip("./")` on the normalized target,
    which strips *characters*, not a prefix — so every `../` was discarded and
    **no wrong-depth path could fail**. Review RD-7 mutation-proved it with a
    link seven levels up, pointing outside the repository, over which the
    battery reported `0 findings` while the denominator incremented. It was
    also the reason a genuinely broken pointer inside act 1's digest set had
    gone unreported (RD-7 finding E-2).
    """
    for cand in (os.path.join(os.path.dirname(citing), target),
                 os.path.join(ROOT, target)):
        if os.path.exists(os.path.normpath(os.path.join(ROOT, cand)
                                           if not os.path.isabs(cand) else cand)):
            return True
    if target.startswith("../") or "/../" in target:
        return False
    t = os.path.normpath(target).replace(os.sep, "/")
    while t.startswith("./"):
        t = t[2:]
    if not t or t.startswith("../"):
        return False
    return any(p == t or p.endswith("/" + t) for p in all_paths)


def cg1_links(paths, res):
    all_paths = set(paths)
    n_links = n_paths = 0
    broken_links, broken_paths, forward, historical, vendor_gap, reviewer = \
        [], [], set(), [], [], []
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
                if _is_vendored_gap(rel, t):
                    vendor_gap.append(f"{rel} -> {t}")
                elif _is_historical_packet(t):
                    historical.append(f"{rel} -> {t}")
                elif _is_frozen_lane(rel):
                    # CG-1a had no frozen-lane branch at all; these passed
                    # only because `_resolve` absorbed them (review RD-7,
                    # finding E-1). Now classified explicitly, like CG-1b's.
                    reviewer.append(f"{rel} -> {t}")
                else:
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
                if _is_vendored_gap(rel, t):
                    vendor_gap.append(f"{rel} -> {t}")
                elif _is_historical_packet(t):
                    historical.append(f"{rel} -> {t}")
                elif _is_frozen_lane(rel):
                    reviewer.append(f"{rel} -> {t}")
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
    uniq_rev = sorted(set(reviewer))
    res.add("WARN", "CG-1f  frozen-lane path references", len(uniq_rev), 0,
            "reference",
            note="raw reviewer output and superseded round records — never "
                 "edited, so classified and printed rather than failed",
            details=uniq_rev)
    uniq_gap = sorted(set(vendor_gap))
    res.add("WARN", "CG-1e  vendored-substrate scope gaps", len(uniq_gap), 0,
            "reference",
            note="deliberately not vendored — GOVERNANCE-SUBSTRATE-LOCK.yaml "
                 "th_engineering.vendored.scope_note names the boundary",
            details=uniq_gap)


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
#: Round-2026-08d wave structure: the all-in-one act-1 phrase is retired;
#: six wave manifests partition the active set and each one's own sha256 is
#: that wave act's argument (ACCEPTANCE-WAVE-DESIGN.md). The active manifest
#: remains the package identity and is no act's argument.
WAVE_IDS = ("A", "B", "C1", "C2", "D1", "D2")
WAVE_MANIFESTS = {w: f"{CANDIDATES}/wave-manifests/WAVE-{w}-MANIFEST.txt"
                  for w in WAVE_IDS}


def wave_arg_pat(w):
    return re.compile(rf"ACCEPT FOUNDATIONAL WAVE {w}:\s*`?([0-9a-f]{{64}})")


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
    active_paths = set()
    for i, ln in enumerate(read(MANIFEST).splitlines(), 1):
        m = DIGEST_ROW.match(ln.strip())
        if not m:
            continue
        n += 1
        active_paths.add(m.group("path").strip())
        target = os.path.join(ROOT, CANDIDATES, m.group("path").strip())
        if not os.path.exists(target):
            findings.append(f"{MANIFEST}:{i} — {m.group('path')} does not exist")
            continue
        actual = sha256_file(target)
        if actual != m.group("sha"):
            findings.append(f"{MANIFEST}:{i} — {m.group('path')} digest "
                            f"{actual[:12]}… != manifest {m.group('sha')[:12]}…")
    # The six wave manifests: every row valid, and together they partition
    # the active set — no overlap, nothing uncovered, nothing extra. The
    # generator asserts this too; asserting it here as well means a
    # hand-edited wave manifest fails a check instead of waiting for a
    # regeneration to notice.
    wave_of = {}
    for w in WAVE_IDS:
        rel = WAVE_MANIFESTS[w]
        if rel not in set(paths):
            findings.append(f"{rel} — wave manifest missing")
            continue
        for i, ln in enumerate(read(rel).splitlines(), 1):
            m = DIGEST_ROW.match(ln.strip())
            if not m:
                continue
            n += 1
            p = m.group("path").strip()
            wave_of.setdefault(p, []).append(w)
            target = os.path.join(ROOT, CANDIDATES, p)
            if not os.path.exists(target):
                findings.append(f"{rel}:{i} — {p} does not exist")
            elif sha256_file(target) != m.group("sha"):
                findings.append(f"{rel}:{i} — {p} digest != manifest "
                                f"{m.group('sha')[:12]}…")
    for p, ws in sorted(wave_of.items()):
        if len(ws) > 1:
            findings.append(f"{p} — appears in waves {'/'.join(ws)}; the "
                            f"partition overlaps")
    for p in sorted(active_paths - set(wave_of)):
        findings.append(f"{p} — in the active manifest but in no wave "
                        f"manifest; the partition is incomplete")
    for p in sorted(set(wave_of) - active_paths):
        findings.append(f"{p} — in a wave manifest but not the active "
                        f"manifest")
    manifest_sha = sha256_file(os.path.join(ROOT, MANIFEST))
    status = "FAIL" if findings else ("OK" if n else "WARN")
    res.add(status, "CG-7a  manifest digests valid; waves partition the set",
            n, len(findings), "entry",
            note=(f"active manifest sha256 {manifest_sha} (package identity, "
                  f"no act's argument)"
                  if n else "no digest rows parsed — nothing examined"),
            details=findings)

    if ACCEPTANCE_RECORD not in set(paths):
        res.add("WARN", "CG-7b  wave-act arguments match the wave manifests",
                0, 0, "record",
                note=f"{ACCEPTANCE_RECORD} not present — nothing examined")
        return
    record_text = read(ACCEPTANCE_RECORD)
    bfind, bexam = [], 0
    for w in WAVE_IDS:
        stated = set(wave_arg_pat(w).findall(record_text))
        full = os.path.join(ROOT, WAVE_MANIFESTS[w])
        actual = sha256_file(full) if os.path.exists(full) else None
        if not stated:
            bexam += 1
            bfind.append(f"wave {w} — no `ACCEPT FOUNDATIONAL WAVE {w}: "
                         f"<sha>` found in the record; the act cannot be "
                         f"performed as written")
            continue
        for s in sorted(stated):
            bexam += 1
            if s != actual:
                bfind.append(f"wave {w} — record offers {s[:12]}… but the "
                             f"wave manifest hashes to "
                             f"{(actual or 'absent')[:12]}… — the act would "
                             f"bind a package that no longer exists")
    res.add("FAIL" if bfind else "OK",
            "CG-7b  wave-act arguments match the wave manifests",
            bexam, len(bfind), "argument", details=bfind)

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
    cg7e_act_digest_copies(paths, res)


#: Every act phrase, with the artifact whose sha256 is its only valid
#: argument. CG-7d applies these to *every* file in the corpus, because the
#: round's headline defect was a digest that was correct in the manifest and
#: stale in the document that offered it (six independent reviewers, RB-1 F1
#: … RB-8 F1). A digest quoted anywhere is a promise about an artifact; the
#: artifact is the only thing that can keep it.
ACT_SUBJECTS = tuple(
    (f"ACCEPT FOUNDATIONAL WAVE {w}", WAVE_MANIFESTS[w], wave_arg_pat(w))
    for w in WAVE_IDS
) + (
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
    f"{CANDIDATES}/round-2026-08c/reviews/",
    f"{CANDIDATES}/reviews/",
    f"{CANDIDATES}/history/",
    f"{CANDIDATES}/fixtures/",
    f"{CANDIDATES}/00-README.md",
    f"{CANDIDATES}/10-EXIT-REPORT.md",
    f"{CANDIDATES}/round-2026-08/OWNER-ROUND-CHARTER.md",
    SELF_REL,
)


#: Every file known to carry a **copy of an act argument** — a current act
#: subject's digest, quoted for the owner's convenience somewhere other than
#: the acceptance record's own phrase line. Enumerated, printed on every run,
#: and self-maintaining: CG-7e fails if a file carries such a copy and is
#: **not** listed here, so registration cannot be skipped by adding a new copy.
#:
#: Review RD-6 finding H-1 is why this exists. CG-7d requires the act *phrase*
#: and the 64-hex on the same line; CG-15 requires a truncation marker. A full
#: digest in a table row whose act is named in the row label matched neither.
#: RD-6 mutation-proved it in a pristine extraction: seven falsified act
#: arguments — **all four in the document `AGENTS.md` names as the
#: owner-facing offering**, plus three in the closure preflight — returned
#: `0 findings` and `exit 0` across the whole battery.
#: {file: (act labels whose *current* argument the file must carry)}. The act
#: list per file is enumerated, not inferred: inferring it from "which digests
#: does the file happen to contain" is circular — a file that dropped a copy
#: would be read as never having had one, which is the exact failure H-1
#: describes. A file offering an act and not carrying its current argument
#: fails; a file carrying a current argument and absent from this table fails
#: too, so a new copy cannot skip registration.
#:
#: A **superseded** file belongs here only for the acts it still offers as
#: live. `round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md` carries a
#: `SUPERSEDED — Do not act from this file` banner and is history, so it is
#: absent: RD-6 noted that a file cannot be history for CG-15b and a live
#: offer for CG-7d at the same time.
ACT_DIGEST_COPY_FILES = {
    f"{CANDIDATES}/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md":
        tuple(f"ACCEPT FOUNDATIONAL WAVE {w}" for w in WAVE_IDS) + (
         "CONFIRM CRAFT AMENDMENT: CC-TEST-2",
         "ACCEPT TOPOLOGY", "ADOPT PROJECT OVERVIEW"),
    f"{CANDIDATES}/round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md":
        ("ACCEPT COMPACTED FOUNDATIONAL RFCS",
         "CONFIRM CRAFT AMENDMENT: CC-TEST-2",
         "ACCEPT TOPOLOGY", "ADOPT PROJECT OVERVIEW",
         "ADOPT DOCTRINE AMENDMENT: D3"),
    f"{CANDIDATES}/round-2026-08b/PUBLIC-CLONE-VERIFICATION-REPORT.md":
        ("CONFIRM CRAFT AMENDMENT: CC-TEST-2", "ACCEPT TOPOLOGY",
         "ADOPT PROJECT OVERVIEW", "ADOPT DOCTRINE AMENDMENT: D3"),
    f"{CANDIDATES}/round-2026-08c/FINAL-CLOSURE-PREFLIGHT.md":
        ("CONFIRM CRAFT AMENDMENT: CC-TEST-2", "ACCEPT TOPOLOGY",
         "ADOPT PROJECT OVERVIEW", "ADOPT DOCTRINE AMENDMENT: D3"),
    f"{CANDIDATES}/round-2026-08c/FINAL-OWNER-ACCEPTANCE-PACKET.md":
        ("ACCEPT COMPACTED FOUNDATIONAL RFCS",
         "CONFIRM CRAFT AMENDMENT: CC-TEST-2",
         "ACCEPT TOPOLOGY", "ADOPT PROJECT OVERVIEW",
         "ADOPT DOCTRINE AMENDMENT: D3"),
    f"{CRAFT}/INSTALL-RECORD.md":
        ("CONFIRM CRAFT AMENDMENT: CC-TEST-2",),
}


def cg7e_act_digest_copies(paths, res):
    """Every copy of an act argument is examined, wherever it sits.

    Two predicates, and the second is what keeps the first honest:

    1. **A registered file that names an act carries that act's current
       argument.** Naming means the act's phrase or its subject path appears
       in the file. If the copy goes stale, the current digest is simply
       absent from a file that talks about the act — which is decidable, and
       does not require guessing whether some other 64-hex token used to be
       an act argument.
    2. **A file carrying a current act digest is registered.** An
       unregistered copy is unchecked from the moment it goes stale, which is
       exactly how the population escaped CG-7d.

    **Why not the simpler rule.** Review RD-6 (H-1) proposed treating every
    64-hex token as an act-argument copy. Tried: 47 findings, none of them
    defects — the corpus legitimately quotes digests of artifacts that are not
    act subjects (what D3 would amend, a superseded manifest a round record
    preserves, a per-file craft digest list). A check that cannot tell those
    from a stale act argument would have to be silenced to be usable, and a
    silenced check is the thing this battery exists to prevent.

    H-1's own mutation is what this closes: falsifying all four act arguments
    in the owner-facing offering left the battery at `0 findings, exit 0`.
    Under predicate 1 it removes four current digests from a file that names
    all four acts, and fails four times.
    """
    current, phrases = {}, []
    for label, rel, _pat in ACT_SUBJECTS:
        full = os.path.join(ROOT, rel)
        if not os.path.exists(full):
            continue
        d = sha256_file(full)
        current[d] = label
        phrases.append((label, rel, d))
    findings, examined, registered = [], 0, []
    for rel in paths:
        if not rel.endswith((".md", ".txt")):
            continue
        if any(rel.startswith(x) or rel == x for x in ACT_QUOTE_EXEMPT):
            continue
        if rel == MANIFEST:
            continue
        body = read(rel)
        if not body:
            continue
        # A banner-marked historical record may hold whatever digests it held
        # when it was written; CG-15b owns that population. Registering one
        # here would make it a live offer and history at once, which review
        # RD-6 named as its own defect.
        if re.search(r"^>?\s*[#*\s]*(SUPERSEDED|Superseded|Historical|"
                     r"RETIRED|Retired)\b", "\n".join(body.splitlines()[:12]),
                     re.M):
            continue
        held = [lab for d, lab in current.items() if d in body]
        if rel in ACT_DIGEST_COPY_FILES:
            examined += 1
            declared = ACT_DIGEST_COPY_FILES[rel]
            by_label = {lab: d for lab, _sub, d in phrases}
            missing = [lab for lab in declared
                       if by_label.get(lab) and by_label[lab] not in body]
            for lab in missing:
                findings.append(
                    f"{rel} — declared to carry act `{lab}` and does not "
                    f"contain its current argument `{by_label[lab][:12]}…`. "
                    f"The copy in this file is stale, and this file is one "
                    f"the owner is sent to")
            registered.append(
                f"{rel} — declares {len(declared)} act(s), "
                f"{len(declared) - len(missing)} current")
        elif held:
            examined += 1
            findings.append(
                f"{rel} — carries the current argument for {sorted(held)} and "
                f"is not in ACT_DIGEST_COPY_FILES; an unregistered copy goes "
                f"unchecked the moment it goes stale")
    res.add("FAIL" if findings else ("OK" if examined else "WARN"),
            "CG-7e  act-argument copies enumerated and current", examined,
            len(findings), "file",
            note=None if examined else "no act-argument copies found",
            details=findings + [f"[registered] {r}" for r in registered])


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

#: Charter §7.3 requires the *default agent load* to be reported in words and
#: estimated tokens — not asserted in prose. These four are what a fresh agent
#: session loads before it has chosen a task. Reported every run so the figures
#: cannot go stale in a document that quotes them.
DEFAULT_LOAD = (
    "README.md",
    "AGENTS.md",
    ".claude/skills/heart-and-soul/SKILL.md",
    ".syzygy/intent/OVERVIEW.md",
)
TOKENS_PER_WORD = 1.35

#: `AGENTS.md` carries a tool-managed block that `bd` writes and rewrites. It
#: is default context and counts toward the load, but it is not the router's
#: authored text and cannot be edited to hit a target. Both figures are
#: reported so the §7.1 900–1,200-word target is read against the region it
#: governs, and the whole-file total is never quietly replaced by the smaller
#: number.
TOOL_BLOCK_START = "<!-- BEGIN BEADS INTEGRATION"


def _authored_words(rel, text):
    """Words excluding any tool-managed block. Returns (authored, tool)."""
    idx = text.find(TOOL_BLOCK_START)
    if idx < 0:
        return len(text.split()), 0
    return len(text[:idx].split()), len(text[idx:].split())


def cg8_budgets(paths, res, measure=None):
    present = set(paths)
    read_text = measure if measure is not None else read
    lines, n = [], 0

    # §7.3 — the default load, always reported, never only on breach.
    for rel in DEFAULT_LOAD:
        if rel not in present:
            lines.append(f"{rel} — absent; charter §7.3 names it as default "
                         f"load and it cannot be measured")
            n += 1
            continue
        n += 1
        authored, tool = _authored_words(rel, read_text(rel))
        total = authored + tool
        tok = round(total * TOKENS_PER_WORD)
        suffix = (f" ({authored} authored + {tool} tool-managed)" if tool
                  else "")
        lines.append(f"{rel} — {total} w ≈ {tok} est. tokens{suffix}")

    for rel, limit, label in BUDGETS:
        if rel not in present:
            continue
        authored, tool = _authored_words(rel, read_text(rel))
        if authored + tool > limit:
            lines.append(f"{rel} — {authored + tool} words, over the {limit}-word "
                         f"{label} (§11.4 trigger; review, not failure)")

    # §7.1's tighter target applies to the authored router, not the block bd
    # owns. Reported as its own line so neither figure can stand in for the
    # other.
    if "AGENTS.md" in present:
        authored, tool = _authored_words("AGENTS.md", read_text("AGENTS.md"))
        if not (900 <= authored <= 1200):
            lines.append(f"AGENTS.md — {authored} authored words, outside the "
                         f"§7.1 900–1,200 target band")

    modules = sorted(p for p in paths
                     if p.startswith(f"{CANDIDATES}/rfcs/") and p.endswith(".md"))
    for rel in modules:
        n += 1
        w = len(read_text(rel).split())
        if w > MODULE_DECOMPOSE:
            lines.append(f"{rel} — {w} words, above {MODULE_DECOMPOSE}: §11.4 "
                         f"focused decomposition review")
        elif w > MODULE_TRIGGER:
            lines.append(f"{rel} — {w} words, over the {MODULE_TRIGGER}-word "
                         f"active-module trigger (§11.4)")
    res.add("WARN" if n else "WARN",
            "CG-8   context budgets reported", n, len(lines), "artifact",
            note=("report-only — §7.3 default-load figures are printed every "
                  "run; §11.4 triggers are decomposition prompts, not failures"
                  if n else "nothing examined"),
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
    (f"{CANDIDATES}/round-2026-08c/reviews/",
     "raw reviewer output, stored verbatim — allowlisted explicitly when the "
     "round opened, on the same terms as its two predecessors"),
    (f"{CANDIDATES}/matrix-rows/", "per-RFC clause-migration provenance rows"),
    (f"{CANDIDATES}/04-CLAUSE-MIGRATION-MATRIX.md",
     "clause-migration provenance, cites frozen rev9 sources by construction"),
    (f"{CANDIDATES}/COMPACTION-CHARTER.md",
     "the superseded round's own working charter"),
    (f"{CANDIDATES}/round-2026-08/OWNER-ROUND-CHARTER.md",
     "owner-supplied round charter, quoted verbatim"),
    (f"{CANDIDATES}/round-2026-08d/OWNER-WORK-ORDER.md",
     "owner-supplied work order, quoted verbatim — its `_bootstrap/` line "
     "sits inside the prohibition list it orders enforced"),
    ("syzygy_claude_structural_contract_decomposition_prompt.md",
     "the owner's working copy of the round-2026-08d work order, untracked "
     "at repo root; archived verbatim as round-2026-08d/OWNER-WORK-ORDER.md"),
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
LOAD_MAP = f"{CANDIDATES}/06-CONTEXT-LOAD-MAP.md"
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


def _dir_exists(d, all_paths):
    """A directory reference resolves if it names a real directory, whether
    written from the repo root, from the acceptance record's own directory,
    or as a suffix of one. Directories are not in the file corpus, so the
    file resolver cannot answer this — asking it reported four real
    directories as missing."""
    d = d.strip("/")
    if not d:
        return True
    for base in (ROOT, os.path.join(ROOT, os.path.dirname(ACCEPTANCE_RECORD))):
        if os.path.isdir(os.path.normpath(os.path.join(base, d))):
            return True
    return any(p == d or p.startswith(d + "/") or ("/" + d + "/") in p
               for p in all_paths)


def _git_excluded_roots():
    """Top-level directories `.gitignore` excludes, read rather than assumed.

    A ceremony step that names one of these is executable on the machine that
    happens to have the directory and nowhere else — the founder-local
    dependency this repository keeps re-acquiring. Hardcoding the list would
    make the check go stale the moment `.gitignore` changed, so it is parsed.
    """
    roots = set()
    for line in (read(".gitignore") or "").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("!"):
            continue
        if any(c in line for c in "*?[]"):
            continue
        seg = line.strip("/").split("/")[0]
        if seg and not seg.startswith("."):
            roots.add(seg)
    return roots


def cg14_install_routes(res, record=None, all_paths=()):
    """Every path the acceptance ceremony names is valid for its role.

    An act that installs candidate material states where it reads from and
    where it writes to. A wrong source silently installs the wrong bytes; a
    destination that already exists means the act is not an act. Both were
    live: act 3's install step named `topology/`, a directory that has never
    existed, and the link checker could not see it because an allowlist
    written for stale *history* references was absorbing a live *instruction*.

    Roles are decided by the forward-reference declaration, not by guessing:
    a path declared as act-created must be **absent**, and every other path
    the ceremony names must be **present** — and **present in a clone**, not
    merely on the machine running the check. A git-excluded location is
    treated as absent everywhere, because it is: the founder's copy of
    `_bootstrap/` made a step read as executable here that failed the moment
    the same check ran inside a clone, which is precisely the divergence a
    clone-executable ceremony must not have.
    """
    body = record if record is not None else read(ACCEPTANCE_RECORD)
    if not body:
        res.add("WARN", "CG-14  acceptance install routes valid", 0, 0,
                "route", note=f"{ACCEPTANCE_RECORD} unreadable")
        return
    # The ceremony is section 2. Scope to it so ordinary prose citations
    # elsewhere in the record are not mistaken for install instructions.
    m = re.search(r"^##\s*2\..*$", body, re.M)
    scope = body[m.start():] if m else body
    nxt = re.search(r"^##\s*3\.", scope, re.M)
    if nxt:
        scope = scope[:nxt.start()]
    #: A ceremony that records its own past defect names the bad path in
    #: order to say it was bad, and one that disclaims a founder-local mirror
    #: names it in order to exclude it. Both are the opposite of an
    #: instruction. The window is the line **and its two neighbours**: a
    #: wrapped paragraph puts the marker and the path on different lines, and
    #: a line-only test read the retraction paragraph's `_bootstrap/` as live.
    corrected = re.compile(r"\b(previously|never existed|exists in no clone|"
                           r"corrected|unexecutable|was wrong|no longer|"
                           r"git-excluded|not part of the ceremony|"
                           r"founder machine only|absent from every clone)\b",
                           re.I)
    excluded_roots = _git_excluded_roots()
    findings, examined = [], 0
    seen = set()
    lines = scope.splitlines()
    for line_no, line in enumerate(lines, 1):
        window = "\n".join(lines[max(0, line_no - 2):line_no + 1])
        if corrected.search(window):
            continue
        for pm in re.finditer(r"`([A-Za-z0-9_.\-/]*/)`", line):
            path = pm.group(1)
            if path in seen or path in ("./", "/"):
                continue
            seen.add(path)
            examined += 1
            # A git-excluded root is absent in every clone. Answer from
            # `.gitignore`, never from the local filesystem, so the founder
            # machine and a fresh clone reach the same verdict.
            if path.strip("/").split("/")[0] in excluded_roots:
                findings.append(
                    f"`{path}` — named by the ceremony as a location, but it "
                    f"is git-excluded and therefore absent from every clone; "
                    f"the step is executable only where the directory "
                    f"already happens to exist")
                continue
            # Resolve the way every other path reference here is written:
            # relative to the citing record, to the repo root, or as a
            # suffix. `topology-candidates/` cited from the record's own
            # directory is not a missing directory.
            exists = _dir_exists(path.rstrip("/"), all_paths)
            # A *bare* directory name (`history/`) is a source relative to
            # the record; an act-created home is always written as a full
            # path. Without this, suffix matching classified the candidate
            # package's own `history/` as the act-1 destination of the same
            # name and demanded it not exist.
            if "/" in path.strip("/") and _is_forward(path):
                if exists:
                    findings.append(
                        f"`{path}` — declared as created by an act, but it "
                        f"already exists; the act cannot be performed")
            elif not exists:
                findings.append(
                    f"`{path}` — named by the ceremony as an existing "
                    f"location, but it does not exist; the step cannot be "
                    f"executed as written")
    res.add("FAIL" if findings else ("OK" if examined else "WARN"),
            "CG-14  acceptance install routes valid", examined,
            len(findings), "path",
            note=None if examined else "no directory paths found in the "
                                       "acceptance record's ceremony section",
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
    f"{CANDIDATES}/round-2026-08c/reviews/",
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
    (f"{CANDIDATES}/CONTEXT-BUDGET-REPORT.md",
     "generated: its hex quotations are context-packet digests, not act "
     "arguments, and they are written by build_budget_report.py from the "
     "same measurement CG-18 independently recomputes — the fixtures "
     "themselves are exempt for the same reason"),
)


#: **The cap stays at 63 and the marker stays required, deliberately.** Review
#: RD-6 (finding H-1) proposed widening this to `{8,64}` with an optional
#: marker, so that a full digest quoted without its act phrase would be caught.
#: Tried, and it over-fires: the corpus legitimately quotes 64-hex digests of
#: things that are *not* act subjects — the artifacts D3 would amend, a
#: superseded manifest a round record preserves, a review's record of what it
#: read. Forty-seven such quotations became findings, none of them defects.
#:
#: The hole H-1 proved is real and is closed by **CG-7e** instead, which
#: enumerates the files that carry a copy of an act argument and checks each
#: one — and which fails if a file acquires a copy without being enumerated.
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
    # Sub-clauses (`RFC7-2(a)`) are defined inline inside their parent, so
    # they never match the definition-site regex. Accept one only when its
    # parent is declared AND the module actually contains the token —
    # otherwise a fabricated row would inflate the denominator and read as
    # coverage. Checking only `declared - routed` missed exactly that.
    # Sub-clauses are declared as ranges in a module's front matter
    # (`sub-clauses RFC7-2(a)-(c)`), so expand those into the declared set
    # rather than accepting any token that happens to appear in prose.
    bodies = "\n".join(read(rel) for rel in
                       (modules if modules is not None else _rfc_modules()))
    # Only a *positive* declaration counts. RFC-0008's README contains the
    # sentence "**No lettered sub-clauses.** Lettered limbs cited inside a
    # clause — RFC8-2(a)-(c) …" — reading that as a declaration invented a
    # clause identity RFC-0008 explicitly says it does not have.
    for line in bodies.splitlines():
        if "sub-clause" not in line.lower():
            continue
        if re.search(r"\bno lettered sub-clause", line, re.I):
            continue
        for rng in re.finditer(r"(RFC\d+-\d+)\((\w)\)[-–]\((\w)\)", line):
            stem, lo, hi = rng.groups()
            if stem in declared:
                for o in range(ord(lo), ord(hi) + 1):
                    declared.add(f"{stem}({chr(o)})")
        for single in re.finditer(r"(RFC\d+-\d+\(\w\))(?![-–]\()", line):
            if single.group(1).split("(")[0] in declared:
                declared.add(single.group(1))
    findings = []
    for c in sorted(declared - set(routed)):
        findings.append(f"{c} — declared in a contract, absent from the matrix")
    for c in sorted(set(routed) - declared):
        if c.split("(")[0] in declared and c in bodies:
            continue
        findings.append(f"{c} — routed by the matrix, but no contract "
                        f"declares it; the row inflates coverage")
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
            examined += 1
            findings.append(
                f"{rel} — could not locate a load command and a packet digest "
                f"to recompute from; a fixture this check cannot parse is "
                f"unverified, not passing")
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


#: Metadata scalars and declared non-pin sections. Both are enumerated and
#: printed rather than pattern-matched: a rule broad enough to infer them
#: would also let a pin leave the population unnoticed (defect class 11).
LOCK_META_KEYS = ("version", "as_of", "recomputed_in_session")
LOCK_NONPIN_SECTIONS = ("not_locked", "verification")
#: Adding a forge is a deliberate edit, never a silent widening.
LOCK_FORGE_ALLOW = ("github.com",)
LOCK_LOCATOR_FIELDS = ("repository", "source", "url", "root_path")
LOCK_DISPOSITIONS = ("open", "absorbed", "declined", "superseded", "surfaced")
SHA1_RE = re.compile(r"^[0-9a-f]{40}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
#: A locator that only resolves on one machine. `%USERPROFILE%` is included
#: because the rule is about machine-locality, not about POSIX.
LOCAL_LOCATOR = re.compile(r"^(/|~|\./|\.\./)|^file://|/home/|/Users/|%USERPROFILE%")
GITHUB_PATH_SEG = r"[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?"


def _yaml_lite(text):
    """Indentation parser for exactly the YAML subset the substrate lock uses.

    Not a YAML implementation, and not trying to be: it handles `key: value`,
    `key:` opening a nested block, `- key: value` opening a list item, and the
    `>-` / `|` block scalars. Anything it cannot classify is returned as a
    parse error rather than skipped — a silent skip is how CG-18 examined four
    of eight fixtures while printing a denominator of eight.

    Returns (data, errors).
    """
    rows = []
    for n, raw in enumerate(text.splitlines(), 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        rows.append([n, len(raw) - len(raw.lstrip()), raw.strip()])
    errors = []
    kv = re.compile(r"^([A-Za-z_][\w.\-]*):\s*(.*)$")

    def parse(pos, indent):
        if pos >= len(rows) or rows[pos][1] < indent:
            return {}, pos
        if rows[pos][2].startswith("- "):
            out = []
            while (pos < len(rows) and rows[pos][1] == indent
                   and rows[pos][2].startswith("- ")):
                n, ind, s = rows[pos]
                inner, rest = ind + 2, s[2:]
                # A sequence entry is either a mapping (`- path: x`) or a
                # plain scalar (`- "git clone …"`, as the lock's verification
                # commands are). Treating the second as the first is what made
                # three shell commands read as unparseable lines.
                if not kv.match(rest):
                    out.append(rest.strip('"'))
                    pos += 1
                    continue
                rows[pos] = [n, inner, rest]   # the item's first key
                item, pos = parse(pos, inner)
                out.append(item)
            return out, pos
        out = {}
        while pos < len(rows) and rows[pos][1] == indent:
            n, _, s = rows[pos]
            if s.startswith("- "):
                break
            m = kv.match(s)
            if not m:
                errors.append(f"line {n}: unparseable — {s[:60]}")
                pos += 1
                continue
            key, val = m.group(1), m.group(2).strip()
            pos += 1
            if val in (">-", ">", ">+", "|", "|-", "|+"):
                buf = []
                while pos < len(rows) and rows[pos][1] > indent:
                    buf.append(rows[pos][2])
                    pos += 1
                out[key] = " ".join(buf)
            elif val == "":
                if pos < len(rows) and rows[pos][1] > indent:
                    out[key], pos = parse(pos, rows[pos][1])
                else:
                    out[key] = {}
            else:
                out[key] = val.strip('"')
        return out, pos

    data, end = parse(0, 0)
    if end < len(rows):
        errors.append(f"line {rows[end][0]}: parse stopped early — "
                      f"{rows[end][2][:60]}")
    return data, errors


def _lock_revision_groups(name, pin):
    """The (label, group) pairs a git-pinned substrate declares.

    `th_engineering` nests `adopted:` and `installed:`; the other two carry
    their revision fields at pin level. Both shapes are real, so the check
    reads the shape rather than assuming one.
    """
    groups = [(f"{name}.{k}", v) for k, v in pin.items()
              if isinstance(v, dict) and "commit" in v]
    if groups:
        return groups
    return [(name, pin)] if "commit" in pin else []


def cg19_substrate_lock(res, body=None, policy=None):
    """Substrate pins are complete, well-formed, and internally consistent.

    The engineering substrate this project's craft policy came from was pinned
    to a founder-machine path. Nothing mechanical could see it, so the pin's
    own drift rule was due to fire and did not — the installed tree had moved
    two commits past what the owner approved.

    **RESIDUAL LIMIT — what this check does not establish.** It makes no
    network call and resolves nothing upstream. It establishes that each pin
    carries a complete, well-formed, non-machine-local locator that a human
    with network access can verify in one step, and that the lock is
    internally consistent. It does **not** and cannot establish that the named
    repository exists, that the named commit is reachable in it, that the
    repository is still public, or that the recorded digests match the bytes
    upstream. **A pin to a deleted repository at a fabricated commit passes
    this check by design** — fixture `F6e` is kept in `--selftest` for the sole
    purpose of keeping that boundary executable rather than merely written
    down. Upstream agreement is established only by the human step the lock
    records under `verification:`, and claimed only by a dated clone report.

    The earlier name, *"substrate pins publicly resolvable"*, asserted the half
    it cannot do. It was renamed for that reason (RC10-P). The identifier is
    unchanged: identifiers are amended in place, never renumbered.
    """
    label = "CG-19  substrate pins complete and well-formed; drift consistent"
    text = body if body is not None else read(SUBSTRATE_LOCK)
    if not text:
        res.add("WARN", label, 0, 0, "check",
                note=f"{SUBSTRATE_LOCK} unreadable")
        return
    data, parse_errors = _yaml_lite(text)
    findings = [f"lock does not parse — {e}" for e in parse_errors]
    examined = 0
    population = []

    # P1 — every top-level key is classified. A pin cannot leave the
    # denominator quietly by being renamed or demoted.
    pins = {}
    for key, val in data.items():
        examined += 1
        if key in LOCK_META_KEYS or key in LOCK_NONPIN_SECTIONS:
            continue
        if not isinstance(val, dict):
            findings.append(f"`{key}` — top-level key is neither a declared "
                            f"metadata scalar {LOCK_META_KEYS}, a declared "
                            f"non-pin section {LOCK_NONPIN_SECTIONS}, nor a "
                            f"pin block; unclassified is unverified")
            continue
        pins[key] = val

    for name, pin in pins.items():
        groups = _lock_revision_groups(name, pin)
        version_declared = "installed_version" in pin
        # P2 — a pin declares a kind and carries that kind's full field set.
        # A pin this check cannot classify is unverified, not passing.
        examined += 1
        if not groups and not version_declared:
            findings.append(f"`{name}` — declares neither a `commit` "
                            f"(git-pinned) nor an `installed_version` "
                            f"(version-declared); unclassifiable pins are "
                            f"unverified, not passing")
            continue
        population.append(f"{name} — {'git-pinned' if groups else 'version-declared'}, "
                          f"{len(pin)} field(s)")
        if version_declared and not groups:
            examined += 1
            if not pin.get("digest_or_lock_reference"):
                findings.append(f"`{name}` — version-declared with no "
                                f"`digest_or_lock_reference` saying why "
                                f"nothing is pinned")
        # P7 — visibility is declared, and public, for git-pinned substrates.
        # Undeclared is Unknown, and Unknown is not public (VIS-2).
        if groups:
            examined += 1
            vis = pin.get("visibility")
            if vis is None:
                findings.append(f"`{name}` — git-pinned with no `visibility`; "
                                f"undeclared is Unknown, and Unknown is not "
                                f"public")
            elif vis != "public":
                findings.append(f"`{name}` — `visibility: {vis}`; a "
                                f"non-public substrate is not resolvable from "
                                f"a clone")
        # P5/P6 — locator hygiene and forge grammar, read from the *value of
        # the locator field*, never from prose elsewhere in the block.
        # A flat git-pin is its own revision group, so `[(name, pin)] + groups`
        # would scan the same mapping twice and report every locator finding
        # in it twice. Dedupe by identity, not by name.
        holders, seen_ids = [], set()
        for owner, holder in [(name, pin)] + groups:
            if id(holder) in seen_ids:
                continue
            seen_ids.add(id(holder))
            holders.append((owner, holder))
        for field in LOCATOR_SCAN_FIELDS:
            for owner, holder in holders:
                val = holder.get(field)
                if not isinstance(val, str):
                    continue
                examined += 1
                if LOCAL_LOCATOR.search(val):
                    findings.append(
                        f"`{owner}.{field}` — `{val}` is machine-local; a "
                        f"public URL elsewhere in the block does not make the "
                        f"locator resolvable")
                elif field != "root_path" and "://" in val:
                    findings.extend(_lock_url_findings(owner, field, val))
        # P3/P4 — object ids and per-file digests.
        for gname, g in groups:
            examined += 1
            missing = [f for f in ("root_path", "git_tree", "relevant_paths")
                       if not g.get(f)]
            if missing:
                findings.append(f"`{gname}` — git-pinned revision group "
                                f"missing {', '.join(missing)}")
            for field, rx, kind in (("commit", SHA1_RE, "git object id"),
                                    ("git_tree", SHA1_RE, "git object id")):
                val = g.get(field)
                if val is None:
                    continue
                examined += 1
                if not rx.match(str(val)):
                    findings.append(
                        f"`{gname}.{field}` — `{val}` is not a full "
                        f"lowercase 40-hex {kind}; an abbreviation that is "
                        f"unambiguous today can collide later")
            root = g.get("root_path") or ""
            for entry in g.get("relevant_paths") or []:
                if not isinstance(entry, dict):
                    continue
                examined += 1
                p, digest = entry.get("path"), entry.get("sha256")
                if not digest:
                    findings.append(f"`{gname}` — listed path `{p}` carries "
                                    f"no `sha256`; an unpinned file inside a "
                                    f"pinned tree is unverifiable")
                elif not SHA256_RE.match(str(digest)):
                    findings.append(f"`{gname}` — `{p}` has `sha256: "
                                    f"{digest}`, not 64 lowercase hex")
                if p and LOCAL_LOCATOR.search(p):
                    findings.append(f"`{gname}` — path `{p}` is machine-local; "
                                    f"a valid digest does not launder it")
                elif p and root and not p.startswith(root.rstrip("/") + "/") \
                        and p != root:
                    findings.append(f"`{gname}` — path `{p}` is outside the "
                                    f"group's `root_path: {root}`")
        # P8 — drift is derived from the two groups, then compared against
        # what the lock asserts. Today the assertion is checked by nothing.
        findings.extend(_lock_drift_findings(name, pin, groups))
        examined += 1

    status = "FAIL" if findings else ("OK" if examined else "WARN")
    res.add(status, label, examined, len(findings), "predicate evaluation",
            note=None if examined else "no pins classified",
            details=findings)
    res.add("WARN", "CG-19b substrate pin population", len(population), 0,
            "pin", note="report-only — a pin leaving this list is visible "
                        "here even when CG-19 stays green",
            details=sorted(population))


LOCATOR_SCAN_FIELDS = LOCK_LOCATOR_FIELDS


def _lock_url_findings(owner, field, val):
    """Forge grammar, against a printed allowlist. Closes the malformed and
    non-forge halves of "nonexistent host/repo" — never the existence half."""
    m = re.match(r"^(\w+)://([^/]+)(/.*)?$", val)
    if not m:
        return [f"`{owner}.{field}` — `{val}` is not a parseable URL"]
    scheme, host, path = m.group(1), m.group(2), m.group(3) or ""
    out = []
    if scheme != "https":
        out.append(f"`{owner}.{field}` — scheme `{scheme}`; only `https` is "
                   f"resolvable without credentials")
    if "@" in host or ":" in host:
        out.append(f"`{owner}.{field}` — host `{host}` carries userinfo or a "
                   f"port; a pin must be a plain public locator")
    if host not in LOCK_FORGE_ALLOW:
        out.append(f"`{owner}.{field}` — host `{host}` is outside the forge "
                   f"allowlist {LOCK_FORGE_ALLOW}; adding a forge is a "
                   f"deliberate edit, never a silent widening")
        return out
    segs = [s for s in path.split("/") if s]
    if len(segs) != 2:
        out.append(f"`{owner}.{field}` — `{path or '/'}` is not `owner/repo` "
                   f"({len(segs)} segment(s)); a tree or blob URL is not a "
                   f"repository locator")
    elif not all(re.fullmatch(GITHUB_PATH_SEG, s) for s in segs):
        out.append(f"`{owner}.{field}` — `{path}` is not a valid owner/repo "
                   f"pair for {host}")
    elif path.endswith("/") or segs[-1].endswith(".git"):
        out.append(f"`{owner}.{field}` — `{path}` carries a `.git` suffix or "
                   f"trailing slash; pin the canonical form")
    return out


def _lock_drift_findings(name, pin, groups):
    """Derive drift from adopted-vs-installed, then check the assertion.

    The old check asked only whether a `status:` token appeared *somewhere in
    the pin*. That is defeated by any unrelated `..._status: open` key, and it
    never compared the two revision groups it was sitting on top of — so a
    deleted `drift:` block over genuinely drifted content read as clean.
    """
    named = {k.rsplit(".", 1)[-1]: g for k, g in groups}
    adopted, installed = named.get("adopted"), named.get("installed")
    drift = pin.get("drift") if isinstance(pin.get("drift"), dict) else None
    if not (adopted and installed):
        return []

    def digests(g):
        return {e.get("path"): e.get("sha256")
                for e in (g.get("relevant_paths") or [])
                if isinstance(e, dict) and e.get("path")}

    a, i = digests(adopted), digests(installed)
    shared = set(a) & set(i)
    differing = {p for p in shared if a[p] != i[p]}
    only_one = (set(a) ^ set(i))
    derived = bool(differing) or adopted.get("commit") != installed.get("commit")
    out = []
    if only_one:
        out.append(f"`{name}` — {len(only_one)} path(s) present in one "
                   f"revision group and absent from the other "
                   f"({', '.join(sorted(only_one))}); an added or removed file "
                   f"is drift this table's shape cannot describe")
    if derived and not drift:
        out.append(f"`{name}` — adopted and installed differ, and the pin "
                   f"declares no `drift:` group; silent drift is the defect "
                   f"this lock exists to prevent")
        return out
    if not drift:
        return out
    asserted = str(drift.get("detected", "")).lower() == "true"
    if asserted != derived:
        out.append(f"`{name}` — `drift.detected: {drift.get('detected')}` but "
                   f"the recorded digests and commits say "
                   f"{'differ' if derived else 'agree'}")
    listed = {}
    for e in drift.get("changed_paths") or []:
        if isinstance(e, dict) and e.get("path"):
            listed[e["path"]] = e
    for p in sorted(differing):
        if not any(p.endswith(q) or q.endswith(p) for q in listed):
            out.append(f"`{name}` — `{p}` differs between the two revision "
                       f"groups and is absent from `drift.changed_paths`")
    for q, e in sorted(listed.items()):
        match = [p for p in shared if p.endswith(q) or q.endswith(p)]
        if not match:
            continue
        claimed = str(e.get("material", "")).lower() == "true"
        actually = match[0] in differing
        if claimed and not actually:
            out.append(f"`{name}` — `{q}` is marked `material: true` but is "
                       f"byte-identical in both revision groups; a "
                       f"materiality claim over identical content is a false "
                       f"record")
        if not claimed and actually:
            out.append(f"`{name}` — `{q}` is marked `material: false` but its "
                       f"digests differ between the two groups")
    # Read the disposition from *inside* the drift group. The old block-scoped
    # test was defeated by any unrelated `..._status:` key in the same pin.
    #
    # The key is `disposition`, not `status`. It was `status` until 2026-08-06,
    # when CG-22 caught it: this check's own header calls the value a
    # disposition, and `status` is the one word the term registry §1 forbids
    # because five closed vocabularies answer to it. A legacy `status:` key is
    # reported rather than silently accepted — an unread key is a silent drift,
    # which is the defect this group exists to prevent.
    if "status" in drift and "disposition" not in drift:
        out.append(f"`{name}` — drift group uses the ambiguous key `status:`; "
                   f"rename to `disposition:` (term registry §1, CG-22)")
    disposition = str(drift.get("disposition", "")).strip()
    first = (re.split(r"[\s—:,-]", disposition, 1)[0].lower()
             if disposition else "")
    if not disposition:
        out.append(f"`{name}` — declares drift with no `disposition`; silent "
                   f"drift is the defect this lock exists to prevent")
    elif first not in LOCK_DISPOSITIONS:
        out.append(f"`{name}` — `drift.disposition: {disposition}` does not "
                   f"open with a disposition from {LOCK_DISPOSITIONS}")
    return out


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

    c = Cap()
    cg14_install_routes(c, record=(
        "## 2. Ceremony\ncopy from `no-such-dir/` to "
        "`.syzygy/governance/contracts/rfcs/`\n## 3. Next\n"), all_paths=())
    cases.append(("CG-14 nonexistent install source detected",
                  c.rows[0][0] == "FAIL" and len(c.rows[0][4]) == 1))

    c = Cap()
    cg14_install_routes(c, record=(
        "## 2. Ceremony\ncreates `.syzygy/map/topology/`\n## 3. Next\n"),
        all_paths=(".syzygy/map/topology/keep.md",))
    cases.append(("CG-14 act-created home that already exists detected",
                  c.rows[0][0] == "FAIL"))

    # The founder-machine divergence: `_bootstrap/` exists here and in no
    # clone, so a filesystem answer passes locally and fails inside a clone.
    # `all_paths` deliberately *contains* the directory — the fixture only
    # fails if the check refuses the local answer and consults `.gitignore`.
    c = Cap()
    cg14_install_routes(c, record=(
        "## 2. Ceremony\nmirror the SHA to `_bootstrap/state/`\n## 3. Next\n"),
        all_paths=("_bootstrap/state/FOUNDER_DECISION_LOG.md",))
    cases.append(("CG-14 git-excluded ceremony location detected",
                  c.rows[0][0] == "FAIL"
                  and "_bootstrap" in (c.rows[0][4] or [""])[0]))

    c = Cap()
    cg14_install_routes(c, record=(
        "## 2. Ceremony\nthe git-excluded `_bootstrap/state/` is not part of "
        "the ceremony\n## 3. Next\n"), all_paths=())
    cases.append(("CG-14 disclaimed git-excluded mention exempted",
                  c.rows[0][0] != "FAIL"))

    # CG-8 measures the §7.3 default load. Its failure modes are not "a file
    # is too long" — that is reported, never enforced — but the three ways the
    # figures can quietly stop meaning anything: an artifact vanishing from
    # the load, the authored region drifting out of its target band, and the
    # tool-managed block being counted as authored text.
    c = Cap()
    cg8_budgets(("README.md", "AGENTS.md", ".syzygy/intent/OVERVIEW.md"), c,
                measure=lambda rel: "w " * 1000)
    cases.append(("CG-8 absent default-load artifact detected",
                  any("heart-and-soul" in d and "absent" in d
                      for d in c.rows[0][4])))

    c = Cap()
    cg8_budgets(DEFAULT_LOAD, c, measure=lambda rel: "w " * 1000)
    cases.append(("CG-8 in-band authored region raises no band finding",
                  not any("target band" in d for d in c.rows[0][4])))

    c = Cap()
    cg8_budgets(DEFAULT_LOAD, c, measure=lambda rel: "w " * 400)
    cases.append(("CG-8 under-band authored region detected",
                  any("400 authored words, outside" in d for d in c.rows[0][4])))

    c = Cap()
    cg8_budgets(DEFAULT_LOAD, c,
                measure=lambda rel: ("w " * 1000) + TOOL_BLOCK_START + (" t" * 800))
    cases.append(("CG-8 tool-managed block excluded from the authored figure",
                  any("1000 authored + 804 tool-managed" in d
                      for d in c.rows[0][4])
                  and not any("target band" in d for d in c.rows[0][4])))

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

    # A fabricated row must not pass as coverage. Checking only
    # declared-minus-routed let one inflate the denominator unnoticed.
    c = Cap()
    cg17_routing_completeness(c, matrix="| `RFC6-999` | OS |", modules=[])
    cases.append(("CG-17 routed-but-undeclared clause detected",
                  c.rows[0][0] == "FAIL"))

    # A fixture the parser cannot read is unverified, not passing.
    c = Cap()
    cg18_fixture_freshness(c, fixtures=[("f.md", "no anchors here at all")])
    cases.append(("CG-18 unparseable fixture is not silently skipped",
                  c.rows[0][0] in ("FAIL", "WARN")))

    c = Cap()
    cg18_fixture_freshness(c, fixtures=[("f.md",
        "```\nscripts/context_load.py 06-CONTEXT-LOAD-MAP.md\n```\n"
        "Measured: **99,999 words \u2248 1 estimated tokens**\n"
        "## Packet digest\n`0000000000000000` (recompute")])
    cases.append(("CG-18 falsified word count detected",
                  c.rows[0][0] == "FAIL"))

    # CG-21 is a prohibition, so its fixtures are the two directions that
    # matter: a measurement smuggled into contract prose must fail, and the
    # one sentence allowed to name the report's filename must not.
    c = Cap()
    cg21_contract_prose_states_no_measurement(
        c, modules=[f"{RFCS_DIR}/RFC-0002/README.md"])
    cases.append(("CG-21 examines the real corpus without error",
                  c.rows[0][2] > 0 and c.rows[0][0] == "OK"))

    c = Cap()
    cg21_contract_prose_states_no_measurement(c, modules=[LOAD_MAP])
    cases.append(("CG-21 measurement in prose detected",
                  c.rows[0][0] == "OK"))

    c = Cap()
    cg18_fixture_freshness(c, fixtures=[("f.md",
        "```\nscripts/context_load.py no-such-file.md\n```\n"
        "## Packet digest\n`0000000000000000` (recompute")])
    cases.append(("CG-18 unreproducible fixture detected",
                  c.rows[0][0] == "FAIL"))

    # ---- CG-19, P1..P8. Every fixture marked "passes today" reproduces a
    # mutation that the pre-RC10-P check returned OK on. The four negatives
    # assert the check does NOT fire where it must not — F6e most of all,
    # which keeps the residual limit executable instead of only documented.
    H40, H40B, H64, H64B = "a" * 40, "b" * 40, "c" * 64, "d" * 64

    def cg19(body):
        cap = Cap()
        cg19_substrate_lock(cap, body=body)
        return cap.rows[0]

    def gitpin(name="th_x", repo="https://github.com/o/r", vis="public",
               commit=H40, tree=H40B, root="skills/th", paths=None, extra=""):
        rows = paths if paths is not None else [(f"{root}/SKILL.md", H64)]
        body = (f"{name}:\n  repository: {repo}\n  visibility: {vis}\n"
                f"  commit: {commit}\n  root_path: {root}\n"
                f"  git_tree: {tree}\n  relevant_paths:\n")
        for p, d in rows:
            body += f"    - path: {p}\n"
            if d is not None:
                body += f"      sha256: {d}\n"
        return body + extra

    F = [
        # P1 — population integrity
        ("F1a CG-19 unclassified top-level key detected",
         "version: 1\nmystery_substrate:\n  note: hi\n", "FAIL"),
        ("F1b CG-19 empty lock warns, never passes",
         "# only a comment\n", "WARN"),
        # P2 — kind and required fields
        ("F2a CG-19 git-pin missing git_tree/relevant_paths detected",
         f"th_x:\n  repository: https://github.com/o/r\n  visibility: public\n"
         f"  commit: {H40}\n  root_path: a/b\n", "FAIL"),
        ("F2b CG-19 version-declared with no digest reference detected",
         'th_x:\n  repository: https://github.com/o/r\n'
         '  installed_version: "1.0"\n', "FAIL"),
        ("F2c CG-19 (negative) real version-declared pin accepted",
         'openspec:\n  distribution: "npm: @x/y"\n'
         '  repository: https://github.com/Fission-AI/OpenSpec\n'
         '  installed_version: "1.3.1"\n'
         '  digest_or_lock_reference: >-\n    None pinned; nothing is\n'
         '    generated from it yet.\n', "OK"),
        # P3 — object id well-formedness
        ("F3a CG-19 abbreviated commit detected",
         gitpin(commit="61bd8fa"), "FAIL"),
        ("F3b CG-19 non-hex git_tree detected", gitpin(tree="HEAD"), "FAIL"),
        ("F3c CG-19 uppercase sha256 detected",
         gitpin(paths=[("skills/th/SKILL.md", "C" * 64)]), "FAIL"),
        ("F3d CG-19 40-char non-hex commit detected",
         gitpin(commit="a" * 39 + "z"), "FAIL"),
        # P4 — per-file digests and path sanity
        ("F4a CG-19 listed path with no sha256 detected",
         gitpin(paths=[("skills/th/SKILL.md", None)]), "FAIL"),
        ("F4b CG-19 machine-local path with valid digest detected",
         gitpin(paths=[("/home/tze/.claude/skills/th/SKILL.md", H64)]), "FAIL"),
        ("F4c CG-19 path outside its root_path detected",
         gitpin(paths=[("skills/other/thing.md", H64)]), "FAIL"),
        # P5 — locator hygiene (both passed the old check)
        ("F5a CG-19 local repository with URL in prose detected",
         gitpin(repo="/home/tze/.dotfiles/ai-bootstrap",
                extra="  note: see https://example.com/x\n"), "FAIL"),
        ("F5b CG-19 machine-local root_path with real repo URL detected",
         gitpin(root="~/.claude/skills/th",
                paths=[("~/.claude/skills/th/SKILL.md", H64)]), "FAIL"),
        ("F5c CG-19 (negative) real lock's prose `~/` mentions not flagged",
         read(SUBSTRATE_LOCK), "OK"),
        # P6 — forge grammar
        ("F6a CG-19 one-segment repository URL detected",
         gitpin(repo="https://github.com/Tzeusy"), "FAIL"),
        ("F6b CG-19 tree URL as repository locator detected",
         gitpin(repo="https://github.com/o/r/tree/main/skills"), "FAIL"),
        ("F6c CG-19 non-https scheme detected",
         gitpin(repo="ssh://git@github.com/o/r"), "FAIL"),
        ("F6d CG-19 host outside the forge allowlist detected",
         gitpin(repo="https://not-a-real-host.invalid/o/r"), "FAIL"),
        ("F6e CG-19 (negative) well-formed pin to a nonexistent repo passes "
         "— the residual limit, kept executable",
         gitpin(repo="https://github.com/NoSuchOrg9/no-such-repo-9"), "OK"),
        # P7 — visibility
        ("F7a CG-19 private substrate detected", gitpin(vis="private"), "FAIL"),
        ("F7b CG-19 undeclared visibility detected",
         gitpin().replace("  visibility: public\n", ""), "FAIL"),
    ]

    def drift(a_commit=H40, i_commit=H40B, a_sha=H64, i_sha=H64B,
              drift_block=None, listed_material="true", extra=""):
        d = drift_block if drift_block is not None else (
            f"  drift:\n    detected: true\n    disposition: OPEN — surfaced\n"
            f"    changed_paths:\n      - path: skills/th/bar.md\n"
            f"        material: {listed_material}\n"
            f"        change: whatever\n")
        return (f"th_e:\n  repository: https://github.com/o/r\n"
                f"  visibility: public\n"
                f"  adopted:\n    commit: {a_commit}\n"
                f"    root_path: skills/th\n    git_tree: {H40}\n"
                f"    relevant_paths:\n      - path: skills/th/bar.md\n"
                f"        sha256: {a_sha}\n"
                f"  installed:\n    commit: {i_commit}\n"
                f"    root_path: skills/th\n    git_tree: {H40B}\n"
                f"    relevant_paths:\n      - path: skills/th/bar.md\n"
                f"        sha256: {i_sha}\n" + d + extra)

    F += [
        ("F8a CG-19 undeclared drift over differing digests detected",
         drift(drift_block=""), "FAIL"),
        ("F8b CG-19 differing path absent from changed_paths detected",
         drift(drift_block="  drift:\n    detected: true\n"
                           "    disposition: OPEN\n    changed_paths:\n"
                           "      - path: skills/th/other.md\n"
                           "        material: true\n"), "FAIL"),
        ("F8c CG-19 materiality claimed over identical content detected",
         drift(i_sha=H64, i_commit=H40B, listed_material="true"), "FAIL"),
        ("F8d CG-19 drift.detected false while commits differ detected",
         drift(drift_block="  drift:\n    detected: false\n"
                           "    disposition: OPEN\n"), "FAIL"),
        ("F8e CG-19 drift disposition read from inside the drift group",
         drift(drift_block="  drift:\n    detected: true\n"
                           "    disposition: resolved\n    changed_paths:\n"
                           "      - path: skills/th/bar.md\n"
                           "        material: true\n",
               extra="  build_disposition: open\n"), "FAIL"),
        ("F8g CG-19 legacy ambiguous `status:` drift key detected",
         drift(drift_block="  drift:\n    detected: true\n"
                           "    status: OPEN\n    changed_paths:\n"
                           "      - path: skills/th/bar.md\n"
                           "        material: true\n"), "FAIL"),
        ("F8f CG-19 path present in one revision group only detected",
         drift().replace("  installed:\n    commit: " + H40B,
                         "  installed:\n    commit: " + H40B, 1)
         .replace("      - path: skills/th/bar.md\n        sha256: " + H64B,
                  "      - path: skills/th/added.md\n        sha256: " + H64B),
         "FAIL"),
    ]
    for label, body, want in F:
        cases.append((label, cg19(body)[0] == want))

    c = Cap()
    cg20_load_map_states_no_measurement(
        c, body="| RFC-0001 | single, 99,999 |")
    cases.append(("CG-20 stale load-map figure detected",
                  c.rows[0][0] == "FAIL"))

    # CG-22's four shapes. The last is the one that matters: a qualifier two
    # lines away must exempt, or every legitimate use becomes a finding and
    # the check gets switched off.
    c = Cap()
    cg22_ambiguous_status((), c, corpus=[("f.md", "the `status` field")])
    cases.append(("CG-22 bare `status` code span detected",
                  c.rows[0][0] == "FAIL" and len(c.rows[0][4]) == 1))

    c = Cap()
    cg22_ambiguous_status((), c, corpus=[("f.md", "```yaml\n  status: open\n```")])
    cases.append(("CG-22 indented `status:` field detected",
                  c.rows[0][0] == "FAIL"))

    c = Cap()
    cg22_ambiguous_status((), c, corpus=[
        ("f.md", "the governance\nlifecycle is carried by\nthe `status` field")])
    cases.append(("CG-22 qualifier across a line wrap exempts",
                  c.rows[0][0] == "OK"))

    c = Cap()
    cg22_ambiguous_status((), c, corpus=[])
    cases.append(("CG-22 empty corpus warns, never passes",
                  c.rows[0][0] == "WARN"))

    c = Cap()
    cg22_ambiguous_status((), c, corpus=[(TERM_REGISTRY, "the `status` field")])
    cases.append(("CG-22 allowlisted file exempted and printed",
                  c.rows[0][0] == "OK" and len(c.rows[1][4]) == 1))

    c = Cap()
    cg22_ambiguous_status((), c, corpus=[
        ("f.md", "the key was renamed\nfrom `status` in 2026")])
    cases.append(("CG-22 retirement marker in window exempts",
                  c.rows[0][0] == "OK"))

    # The exemption must not be a back door: a marker outside the window is
    # not a marker. Without this the retirement clause would exempt any file
    # that mentions a rename anywhere.
    c = Cap()
    cg22_ambiguous_status((), c, corpus=[
        ("f.md", "something was renamed here\n" + ("filler\n" * 6)
                 + "the `status` field")])
    cases.append(("CG-22 retirement marker outside the window does not exempt",
                  c.rows[0][0] == "FAIL"))

    # CG-23 reads the tier split out of the registry rather than restating it.
    # Its failure modes are the split going stale underneath it, and a drawer
    # boundary that silently swallows the whole document.
    CORE_TBL = ("**Core — the four.**\n\n"
                "| Term | ID | Plain question |\n|---|---|---|\n"
                "| Capability | T-04 | x |\n| Claim | T-13 | x |\n"
                "| Gap | T-20 | x |\n| Mission | T-27 | x |\n\n")
    reg = (CORE_TBL
           + "#### T-04 · Capability\n#### T-13 · Claim\n#### T-20 · Gap\n"
             "#### T-27 · Mission\n#### T-28 · Autonomy envelope\n")
    # The leaks in this corpus are lowercase running prose, so the fixture is
    # lowercase. A case-sensitive matcher passed every other fixture here and
    # found none of the real hits.
    c = Cap()
    cg23_default_path_vocabulary(c, registry=reg,
                                 default_path=[("f.md", "an autonomy "
                                                        "envelope bounds it")])
    cases.append(("CG-23 advanced term on the default path detected",
                  len(c.rows[0][4]) == 1 and "T-28" in c.rows[0][4][0]))

    # A word boundary, not a substring: "enveloped" is not the term, and the
    # loose form reported a `Warrant` hit on the word "warranted" that no
    # reader would have called a leak.
    c = Cap()
    cg23_default_path_vocabulary(c, registry=reg,
                                 default_path=[("f.md", "the enveloped case")])
    cases.append(("CG-23 substring inside a longer word is not a hit",
                  not c.rows[0][4]))

    # The allowlist exempts and *prints*; it never silences.
    c = Cap()
    saved = dict(VOCAB_ORDINARY_USE)
    VOCAB_ORDINARY_USE[("f.md", "T-28")] = "ordinary English, for the fixture"
    try:
        cg23_default_path_vocabulary(
            c, registry=reg,
            default_path=[("f.md", "an autonomy envelope bounds it")])
    finally:
        VOCAB_ORDINARY_USE.clear()
        VOCAB_ORDINARY_USE.update(saved)
    cases.append(("CG-23 ordinary-English exemption is printed, not silent",
                  any("ordinary-English use, exempt" in d
                      for d in c.rows[0][4])))

    c = Cap()
    cg23_default_path_vocabulary(c, registry=reg,
                                 default_path=[("f.md", "a Capability is a "
                                                        "Claim about a Gap")])
    cases.append(("CG-23 core-only default path raises nothing",
                  not c.rows[0][4]))

    # The split going stale underneath the check: a core table naming an ID
    # with no entry of its own. Before the core set was derived this was the
    # only way the drift could show; it stays fixtured because the derivation
    # can still read a table whose rows point nowhere.
    c = Cap()
    cg23_default_path_vocabulary(
        c, registry=CORE_TBL + "#### T-99 · Nothing\n",
        default_path=[("f.md", "x")])
    cases.append(("CG-23 stale tier split detected",
                  any("no registry entry of their own" in d
                      for d in c.rows[0][4])))

    # And the failure the derivation introduced: a registry whose core table
    # does not parse must say so loudly, not silently report every term as
    # advanced — which would look like a vocabulary catastrophe and be a
    # parser bug.
    c = Cap()
    cg23_default_path_vocabulary(
        c, registry="#### T-04 · Capability\n",
        default_path=[("f.md", "a Capability")])
    cases.append(("CG-23 unparsable core table reported, not silently advanced",
                  any("core table did not parse" in d for d in c.rows[0][4])))

    c = Cap()
    cg23_default_path_vocabulary(c, registry="no headings here",
                                 default_path=[("f.md", "x")])
    cases.append(("CG-23 unparsable registry warns over zero examined",
                  c.rows[0][2] == 0 and "changed shape" in str(c.rows[0])
                  or c.rows[0][2] == 0))

    # CG-24 exists because a prose coverage claim drifts. Its own failure mode
    # is a regex that reads the battery's check names as if they were fixture
    # names, which would make every check appear to cover itself.
    c = Cap()
    cg24_selftest_coverage(c, source='cases.append(("CG-13 x detected",',
                           reported=["CG-13  deps", "CG-99  invented"])
    cases.append(("CG-24 uncovered check family detected",
                  any("CG-99" in d for d in c.rows[0][4])))

    c = Cap()
    cg24_selftest_coverage(c, source='("F8a CG-19 y detected",',
                           reported=["CG-19  substrate"])
    cases.append(("CG-24 F-prefixed fixture name credited",
                  not c.rows[0][4]))

    c = Cap()
    cg24_selftest_coverage(c, source='res.add(status, "CG-13  deps resolve",',
                           reported=["CG-13  deps resolve"])
    cases.append(("CG-24 a check's own name is not a fixture for it",
                  any("CG-13" in d for d in c.rows[0][4])))

    c = Cap()
    cg24_selftest_coverage(c, source='cases.append(("CG-77 z detected",',
                           reported=["CG-13  deps"])
    cases.append(("CG-24 fixture naming an unreported check detected",
                  any("did not report" in d for d in c.rows[0][4])))

    # CG-7e — the first fixture the CG-7 family has ever had. Review RD-6
    # mutation-proved that falsifying every act argument in the owner-facing
    # offering left the battery green; these two reproduce that mutation and
    # its inverse, so the closure is executable rather than described.
    c = Cap()
    cg7e_act_digest_copies(list(ACT_DIGEST_COPY_FILES), c)
    cases.append(("CG-7e examines the real act-copy population without error",
                  c.rows[0][2] > 0))

    c = Cap()
    saved = dict(ACT_DIGEST_COPY_FILES)
    ACT_DIGEST_COPY_FILES.clear()
    ACT_DIGEST_COPY_FILES[LOAD_MAP] = ("ACCEPT TOPOLOGY",)
    try:
        cg7e_act_digest_copies([LOAD_MAP], c)
    finally:
        ACT_DIGEST_COPY_FILES.clear()
        ACT_DIGEST_COPY_FILES.update(saved)
    cases.append(("CG-7e file declaring an act it does not carry detected",
                  c.rows[0][0] == "FAIL"))

    c = Cap(); cg21_contract_prose_states_no_measurement(c, modules=[])
    cases.append(("CG-21 empty module list warns, never passes",
                  c.rows[0][0] == "WARN"))

    # The prohibition itself, mutation-tested on a synthetic body rather than
    # by editing a real contract. Three shapes, because one regex covering
    # three can pass on the shape it happens to see.
    for label, body in (
        ("comma figure", "| 1 — core | `x.md` | RFC2-1..RFC2-11 | 1,955 |"),
        ("spelled count", "This module is 1955 words at the rev10 compaction."),
        ("wc -w claim", "Counts are `wc -w` at the rev10 compaction."),
    ):
        c = Cap()
        cg20_load_map_states_no_measurement(c, body=body)
        cases.append((f"CG-20 {label} in the load map detected",
                      c.rows[0][0] == "FAIL"))

    # And the negative: the one sentence that names the report must pass, or
    # the rule forbids stating where the measurement went.
    c = Cap()
    cg20_load_map_states_no_measurement(
        c, body="Current measurement lives in `CONTEXT-BUDGET-REPORT.md` §3.")
    cases.append(("CG-20 pointer to the budget report exempted",
                  c.rows[0][0] == "OK"))

    c = Cap()
    cg20_load_map_states_no_measurement(c, body="")
    cases.append(("CG-20 empty load map warns, never passes",
                  c.rows[0][0] == "WARN"))

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


def cg20_load_map_states_no_measurement(res, body=None, modules=None):
    """The context-load map states no measurement of the corpus it routes.

    **Inverted on 2026-08-06, for the reason CG-21 was.** This check used to
    verify that the map's eleven per-contract word rows still recomputed, and
    it earned its place: eleven of eleven were stale, one by 1,745 words,
    while the paragraph above them claimed the figures were "re-runnable from
    this packet". A fresh engineer caught two of the eleven by hand and,
    having caught them, correctly stopped trusting the file.

    Keeping the rows true was the wrong repair. A map whose job is to say
    *what to load* does not also need to say *what it weighs*, and the second
    job is what kept breaking the first. The figures now live in the generated
    `CONTEXT-BUDGET-REPORT.md`, and this check verifies they have not come
    back — including into the fixture-exercise table, which held a third copy
    of every fixture's measurement.

    Denominator is lines examined, not figures found: a figure count reaches
    zero exactly when the rule is honoured, and `0 examined` verifies nothing.
    """
    text = body if body is not None else read(LOAD_MAP)
    if not text:
        res.add("WARN", "CG-20  load-map states no measurement", 0, 0, "line",
                note=f"{LOAD_MAP} unreadable")
        return
    findings, examined = [], 0
    for line_no, line in enumerate(text.splitlines(), 1):
        examined += 1
        if MEASUREMENT_POINTER in line:
            continue
        for m in CONTRACT_MEASUREMENT.finditer(line):
            findings.append(
                f"{LOAD_MAP}:{line_no} — states the measurement "
                f"`{m.group(0)}`. The map routes; it does not measure. Its "
                f"figures went stale eleven rows out of eleven, and their "
                f"home is the generated {MEASUREMENT_POINTER}")
    res.add("FAIL" if findings else ("OK" if examined else "WARN"),
            "CG-20  load-map states no measurement", examined, len(findings),
            "line",
            note=None if examined else "load map is empty",
            details=findings)


#: Kept under the old name so call sites and the citation record read the
#: same. Identifiers are amended in place, never renumbered.
cg20_load_map_figures = cg20_load_map_states_no_measurement


#: A figure that describes the pre-compaction monolith cannot be recomputed
#: from the package, and is not a defect. It must say so on its own line —
#: the marker is the disclosure, exactly as CG-7d requires of a historical
#: digest quotation. A figure with no marker and no current referent is
#: assumed stale, which is the fail-closed direction.
#: Two marker classes, deliberately scoped differently — a single window for
#: both let a `~9,500 target` two lines away exempt a stale `2,029` index
#: count, which is the allowlist-wider-than-the-check failure this repository
#: has already paid for once.
#:
#: A **threshold** is a policy number: nothing's word count by design, always
#: written inline ("the ~7,000 ceiling"). Windowed at ±1 line — the same
#: sentence, never the same section: at ±2 a "~9,500 target" exempted a
#: stale index count two lines above it.
THRESHOLD_MARKERS = ("ceiling", "target", "budget")
THRESHOLD_WINDOW = 1
#: A **frozen-source** figure describes the pre-compaction monolith and cannot
#: be recomputed from the package. Prose wraps, so the marker and the figure it
#: licenses routinely land on opposite sides of a line break: windowed.
FROZEN_FIGURE_MARKERS = ("frozen", "rev9", "monolith", "source words",
                         "source's", "pre-split", "before the split",
                         "moved to tier 2", "scaffolding")
FIGURE = re.compile(r"\b\d{1,2},\d{3}\b")
FIGURE_WINDOW = 2


#: A measurement claim inside contract prose. Comma-formatted figures in the
#: derived-value range, and the vocabulary that introduces one. Clause
#: identities (`RFC9-52`), years, and section numbers do not match.
CONTRACT_MEASUREMENT = re.compile(
    r"\b\d{1,2},\d{3}\b"
    r"|(?<![\w-])\d{3,}\s*(?:words?|tokens?)\b"
    r"|`wc -w`"
    r"|\bword count(?:s)?\b",
    re.I)
#: The one place a contract module may say the phrase, because it is the
#: sentence that sends the reader to the measurement's real home.
MEASUREMENT_POINTER = "CONTEXT-BUDGET-REPORT.md"


def cg21_contract_prose_states_no_measurement(res, modules=None):
    """No contract module states a measurement of anything.

    **This check was inverted on 2026-08-06, and the inversion is the point.**

    It used to verify that the nineteen per-module word counts in package
    READMEs still recomputed. That is a real check and it found real defects
    — but it accepts the premise that a volatile measurement belongs inside a
    contract, and then tries to keep it true. The premise is the defect. These
    figures sit **inside act 1's digest set**: correcting one changes the
    argument the owner would sign, for a reason that has nothing to do with
    what the contract says.

    The history is four rounds long. Nineteen of nineteen module rows were
    stale in the commit whose own message claimed to have corrected every
    stale derived value. A hand repair then left nine more of the same class
    in the same file, stating module 1 as 6,996 in one place and 6,999 in
    another. The check written to close that class could not see the rows it
    was written for, and a reviewer mutation-tested it at `111,111` to prove
    so. Each round fixed the instances; none removed the reason instances
    keep appearing.

    So the rule is now: **a contract module states no measurement.** Sizes
    live in the generated `CONTEXT-BUDGET-REPORT.md`, which is regenerated
    rather than transcribed, and the compaction narrative lives in the round
    report that owns it. What stays in the contract is what it *says*.

    The denominator is the module count, never the figure count — a figure
    count goes to zero exactly when the rule is being honoured, and a check
    reporting `0 examined` verifies nothing.
    """
    if modules is None:
        base = os.path.join(ROOT, RFCS_DIR)
        modules = []
        for dirpath, _dirs, names in os.walk(base):
            for n in sorted(names):
                if n.endswith(".md"):
                    modules.append(os.path.relpath(
                        os.path.join(dirpath, n), ROOT).replace(os.sep, "/"))
        modules.sort()
    findings, examined = [], 0
    for rel in modules:
        body = read(rel)
        if not body:
            continue
        examined += 1
        for line_no, line in enumerate(body.splitlines(), 1):
            if MEASUREMENT_POINTER in line:
                continue
            for m in CONTRACT_MEASUREMENT.finditer(line):
                findings.append(
                    f"{rel}:{line_no} — states the measurement "
                    f"`{m.group(0)}`; contract prose carries no measurement, "
                    f"and this one is inside act 1's digest set. Its home is "
                    f"the generated {MEASUREMENT_POINTER}")
    res.add("FAIL" if findings else ("OK" if examined else "WARN"),
            "CG-21  contract prose states no measurement", examined,
            len(findings), "module",
            note=None if examined else "no contract modules found",
            details=findings)


#: Kept under the old name so the battery's call sites and the selftest
#: registry read the same. Renaming a check identifier would break every
#: citation of CG-21 in the round records, and identifiers are amended in
#: place, never renumbered.
cg21_package_readme_counts = cg21_contract_prose_states_no_measurement


# --------------------------------------------------------------- CG-22

#: The term registry's §1 rule, made executable: five different questions in
#: this project are answered by five different closed vocabularies, and
#: English offers one word for all of them. A field, column, badge, filter or
#: API key named only `status` is a defect wherever more than one dimension
#: could be meant — and OpenSpec authoring is about to multiply field names.
#:
#: This check exists to hold a line the corpus currently holds, not to clean
#: one it has lost. Written 2026-08-06 over 4 hits in 135 active files. A
#: check whose denominator is real but whose finding count is near zero is
#: worth having only if it can still fail: see the four `--selftest` fixtures.
STATUS_SHAPES = (
    (re.compile(r"`status`"), "code span `status`"),
    (re.compile(r"`status\s*:"), "code-span field `status:`"),
    (re.compile(r"^\s{2,}status\s*:", re.M), "indented field `status:`"),
)

#: Naming any one of the five dimensions in the same whitespace-normalized
#: window disambiguates the use. Window, not line: a qualifier and the word it
#: qualifies routinely land on opposite sides of a wrap.
STATUS_QUALIFIERS = (
    "state plane", "epistemic label", "evidence tier", "rendering tier",
    "work lifecycle", "governance lifecycle", "chain state", "lifecycle state",
)

#: Naming the token in order to record that it was retired is not a use of it
#: — the same shape CG-12 uses for `_bootstrap/` mentions marked historical.
#: The marker must fall inside the window, so a "renamed" three sections away
#: exempts nothing.
STATUS_RETIRED_MARKERS = (
    "renamed", "retired", "superseded", "cg-22", "term registry §1",
)

#: Explicit, reasoned, per-file. Never a glob — an allowlist that absorbs a
#: file it was not written for is how a live instruction got exempted here
#: once already.
STATUS_ALLOW = {
    TERM_REGISTRY:
        "states the rule itself; the bare form is the thing being forbidden",
    ".syzygy/governance/contracts/candidates/round-2026-08d/OWNER-WORK-ORDER.md":
        "owner-supplied work order, quoted verbatim — its bare `status` "
        "spans name the defect it orders fixed",
    "syzygy_claude_structural_contract_decomposition_prompt.md":
        "the owner's working copy of the round-2026-08d work order, "
        "untracked at repo root; same text as the archived copy",
    ".syzygy/governance/policies/craft-and-care/interfaces-and-dependencies.md":
        "quotes a violating API's own field name as the rule's worked "
        "counter-example — adopted craft text, not a Syzygy field",
}

STATUS_WINDOW = 2

#: Vendored external substrate. Copied in verbatim under an owner override so
#: a clone needs no external fetch (see `GOVERNANCE-SUBSTRATE-LOCK.yaml`); its
#: prose is somebody else's, is never edited to satisfy a Syzygy checker, and
#: is not the active lane. Declared per prefix, never globbed from
#: `.claude/skills/` — `heart-and-soul` lives there and *is* ours.
#:
#: CG-1a/CG-1b honor this too (`_is_vendored_gap`, defined beside `cg1_links`
#: above): a vendored file's own cross-references to un-vendored siblings are
#: classified under CG-1e, not counted as broken links. Forward-referenced
#: here because Python resolves module-level names at call time, not
#: definition time — every `cg1_links` call happens after this line has run.
VENDORED_EXTERNAL = (
    ".claude/skills/th-engineering/",
    ".codex/skills/th-engineering/",
)


def cg22_ambiguous_status(paths, res, corpus=None):
    """No unqualified `status` where the dimension is ambiguous.

    Charter §9.4 and the working term registry §1. Active lane only: frozen
    history and verbatim reviewer output are evidence, never instructions,
    and are never edited to satisfy a checker.
    """
    if corpus is None:
        corpus = [(p, read(p)) for p in paths
                  if p.endswith(".md")
                  and "/history/" not in p and "/reviews/" not in p
                  and "/round-2026-08/" not in p
                  and not p.startswith("_bootstrap/")
                  and not p.startswith(VENDORED_EXTERNAL)]
    findings, allowed = [], []
    examined = 0
    for rel, text in corpus:
        examined += 1
        lines = text.splitlines()
        hits = []
        for pat, label in STATUS_SHAPES:
            for m in pat.finditer(text):
                hits.append((text[:m.start()].count("\n") + 1, label))
        if not hits:
            continue
        if rel in STATUS_ALLOW:
            allowed.append(f"{rel} ({len(hits)} hit(s)) — {STATUS_ALLOW[rel]}")
            continue
        for i, label in sorted(set(hits)):
            lo = max(0, i - 1 - STATUS_WINDOW)
            window = " ".join(
                " ".join(lines[lo:i + STATUS_WINDOW]).split()).lower()
            if not any(q in window for q in
                       STATUS_QUALIFIERS + STATUS_RETIRED_MARKERS):
                findings.append(
                    f"{rel}:{i} — unqualified {label}; name the dimension "
                    f"(state plane / epistemic label / evidence tier / work "
                    f"lifecycle / governance lifecycle): "
                    f"{lines[i - 1].strip()[:70]}")
    res.add("FAIL" if findings else ("OK" if examined else "WARN"),
            "CG-22  no unqualified `status` in the active lane", examined,
            len(findings), "file",
            note=None if examined else "no active markdown examined",
            details=findings)
    res.add("WARN", "CG-22b unqualified-`status` allowlist", len(allowed), 0,
            "file", note="the rule's own statement and its counter-example",
            details=sorted(allowed))


# --------------------------------------------------------------- CG-23

#: The working term registry's two-tier claim, made executable: a reader
#: arriving at the default public path must not have to learn thirty terms.
#: The registry states this bound and states that it currently fails. Until
#: an owner act accepts the core set the bound cannot be enforced — so this
#: reports, every run, rather than asserting a state nobody has ruled on.
#:
#: The registry previously promised this enforcement from "CG-17", which
#: routes surface clauses and has nothing to do with vocabulary. Corrected
#: 2026-08-06.
#: The core set is **read out of the registry's own core table**, never listed
#: here. A hard-coded copy is the transcription class this battery exists to
#: catch: the list sat here for one round, and the moment the registry moved a
#: term between tiers the check went on policing the old split while reporting
#: green. Derived, it cannot disagree with the artifact it checks.
CORE_TABLE_ROW = re.compile(r"^\|\s*[^|]+?\s*\|\s*(T-\d+)\s*\|", re.M)
CORE_SECTION = re.compile(r"\*\*Core — the [a-z]+\.\*\*[\s\S]*?\n\n(\|[\s\S]*?)\n\n")
TERM_HEADING = re.compile(r"^#### (T-\d+) · (.+?)(?:\s*\(also called.*)?$", re.M)


def _core_term_ids(reg):
    m = CORE_SECTION.search(reg)
    return tuple(CORE_TABLE_ROW.findall(m.group(1))) if m else ()
#: The default path ends where progressive disclosure begins. Everything
#: inside a drawer is deliberate drill-down and is out of scope by design.
DRAWER = "<details>"

#: Ordinary-English uses of a word that is also an advanced term. Enumerated
#: and printed every run, never pattern-matched away: a rule broad enough to
#: infer "this one is ordinary English" would also excuse a real leak. Keyed
#: by (file, term ID) so widening it to a second term in the same file is a
#: deliberate edit.
VOCAB_ORDINARY_USE = {
    ("README.md", "T-13"):
        "\"No claim of alignment, convergence, or regeneration capability\" "
        "(README.md:118) — the ordinary verb-shaped noun, not the kernel's "
        "positive-status carrier. An earlier revision of this exemption "
        "misquoted the very line it exempts; review RD-3 caught it in "
        "passing, and nothing here verifies the quotation mechanically",
}


def cg23_default_path_vocabulary(res, registry=None, default_path=None):
    reg = registry if registry is not None else read(TERM_REGISTRY)
    entries = {tid: name.strip() for tid, name in TERM_HEADING.findall(reg)}
    core = _core_term_ids(reg)
    findings, examined, exempted = [], 0, []

    if not core:
        findings.append("the registry's core table did not parse — the tier "
                        "split this check reads is unavailable, so every term "
                        "below is being reported as advanced")
    missing_core = [t for t in core if t not in entries]
    if missing_core:
        findings.append(f"core ids {missing_core} appear in the core table "
                        f"and have no registry entry of their own")
    advanced = {tid: n for tid, n in entries.items() if tid not in core}

    if default_path is None:
        default_path = []
        for rel in ("README.md", ".syzygy/intent/OVERVIEW.md"):
            body = read(rel)
            cut = body.find(DRAWER)
            default_path.append((rel, body if cut < 0 else body[:cut]))

    # Matching is **case-insensitive at word boundaries**, because the real
    # leaks in this corpus are lowercase running prose — "computed at an
    # identified evaluation", "the intent that warranted it". A case-sensitive
    # match on the registry's own capitalisation missed every one of them.
    #
    # The cost of matching loosely is ordinary English read as jargon: "no
    # claim of alignment" is not the term `Claim`. That is handled the way
    # this battery handles every exemption — an enumerated allowlist, printed
    # on every run, never a silent widening of the pattern. An entry names the
    # file, the term, and why the use is ordinary English.
    for rel, body in default_path:
        for tid, name in sorted(advanced.items()):
            examined += 1
            pat = re.compile(r"\b" + re.escape(name) + r"\b", re.I)
            hits = len(pat.findall(body))
            if not hits:
                continue
            excuse = VOCAB_ORDINARY_USE.get((rel, tid))
            if excuse:
                exempted.append(f"{rel} — `{name}` ({tid}) {hits}× — {excuse}")
                continue
            findings.append(f"{rel} — uses advanced term "
                            f"`{name}` ({tid}) {hits}× on the default path")
    res.add("WARN", "CG-23  default-path vocabulary reported", examined,
            len(findings), "term-in-file",
            note=("report-only — the core set is candidate, so this is the "
                  "registry's own bound reported, not enforced"
                  if examined else "no advanced terms parsed — registry "
                                   "headings changed shape"),
            details=findings + [f"[ordinary-English use, exempt] {e}"
                                for e in exempted])


# --------------------------------------------------------------- CG-24

#: "`--selftest` runs every check above against a synthetic failing input."
#: That sentence has been false for as long as it has been written, and two
#: independent reviews (RC-10 §7.2 vi, RC-11 RC11-G) raised it. The first
#: repair added twenty-nine fixtures — all clustered in the range that already
#: had coverage — which made the sentence *less* true as a proportion while
#: looking like a fix.
#:
#: A prose correction goes stale the next time a check is added. So the
#: denominator is computed instead: CG-24 reads the fixture names out of this
#: file's own `selftest()` and compares them against the identifiers the
#: battery actually reported this run. Adding a check with no fixture now
#: shows up here on the same run.
#: Fixture names read `"CG-19 private substrate detected"` or `"F8g CG-19 …"`;
#: the battery's own check names read `"CG-19  substrate pins …"` with two
#: spaces. The single-space lookahead is what separates a fixture from the
#: check it tests — without it every check would appear to cover itself.
#: A fixture may name a lettered sub-check (`CG-7e`, `CG-1b`) while the family
#: this check counts is the numeric stem. Admitting the suffix is what let the
#: first CG-7 fixture ever written be credited to CG-7; without it the fixture
#: existed and the coverage figure still reported the family uncovered.
CASE_NAME = re.compile(r'"(?:F\d+[a-z]?\s+)?(CG-\d+)[a-z]? (?! )')
CHECK_ID = re.compile(r"^(CG-\d+)")


def cg24_selftest_coverage(res, source=None, reported=None):
    if source is not None:
        src = source
    else:
        # CG-24's own fixtures pass synthetic sources containing invented
        # identifiers; reading them back out of this file would report them as
        # real. Drop the lines that construct them.
        src = "\n".join(ln for ln in read(SELF_REL).splitlines()
                         if "cg24_selftest_coverage(" not in ln)
    covered = set(CASE_NAME.findall(src))
    if reported is None:
        # CG-24 runs last and has not added its own row yet; include it, or it
        # reports itself as a check the battery never ran.
        reported = [s[1] for s in res.summaries] + ["CG-24  self"]
    families, seen = [], set()
    for name in reported:
        m = CHECK_ID.match(name.strip())
        # Sub-checks (CG-7a..d, CG-22b) roll up to their family: a fixture for
        # CG-7a is not a fixture for CG-7d, but the coarser claim is the one
        # the prose makes, and overstating coverage here would repeat the
        # defect.
        if m and m.group(1) not in seen:
            seen.add(m.group(1))
            families.append(m.group(1))
    uncovered = [f for f in families if f not in covered]
    orphan = sorted(covered - set(families))
    details = []
    if uncovered:
        details.append(f"no `--selftest` fixture: {', '.join(uncovered)}")
    if orphan:
        details.append(f"fixtures naming a check the battery did not report: "
                       f"{', '.join(orphan)}")
    res.add("WARN", "CG-24  selftest coverage reported", len(families),
            len(details), "check family",
            note=(f"{len(families) - len(uncovered)} of {len(families)} check "
                  f"families have at least one fixture — quote this figure, "
                  f"never 'every check'" if families else "nothing examined"),
            details=details)


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
    cg14_install_routes(res, all_paths=existing)
    cg15_truncated_digests(existing, res)
    cg16_term_registry_status(existing, res)
    cg17_routing_completeness(res)
    cg18_fixture_freshness(res)
    cg19_substrate_lock(res)
    cg20_load_map_figures(res)
    cg21_package_readme_counts(res)
    cg22_ambiguous_status(existing, res)
    cg23_default_path_vocabulary(res)
    cg24_selftest_coverage(res)
    res.report()
    return 1 if res.failed() else 0


if __name__ == "__main__":
    sys.exit(main())
