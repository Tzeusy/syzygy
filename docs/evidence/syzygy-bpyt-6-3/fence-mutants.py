#!/usr/bin/env python3
"""Rule-6 mutants for the fence-rule checks of syzygy-bpyt.6.3 stack 3: does each check fail when the rule it pins changes?

Usage: fence-mutants.py <scratch clone at the head commit, built, with node_modules> <head commit> <expected fence-probe output>
                        <tmpdir> <out json> [--only id,id]

For each mutant: reset the clone to the head commit, replace `old` by `new` in `file` (`old` must occur exactly once), commit it,
then run the detectors:
  test      apps/three-surface-poc/src/fence-rules.test.ts (the new characterization test); a failing exit is a kill. Each failed
            test is stored with its first error line, so an assertion can be told from a load timeout.
  probe     rebuild (npm run build:poc), run fence-probe.mjs, compare with the expected output through compare-fence-probe.py.
  existing  the test files nearest the rule, which were there before this change (what the new checks add is the difference).
A mutant no detector kills is SURVIVED. PR5 and the other mutants marked `closes-a-gap` change a rule the way the recorded gaps
would be closed: they are expected to fail the pins, because the pins document the gap.
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CORE = 'packages/three-surface-poc-core/src/'
APP = 'apps/three-surface-poc/src/'
CONSENT = 'packages/polaris-generation-consent/src/'
P_CORE, P_APP, P_CONSENT = '@syzygy/three-surface-poc-core', '@syzygy/three-surface-poc-app', '@syzygy/polaris-generation-consent'

# (id, file, old, new, existing-test project, existing test files, kind)
MUTANTS = [
    ('PR1-profile-opener-indent4', CORE + 'markdown-code-context.ts', "const FENCE_OPENER = /^ {0,3}(", "const FENCE_OPENER = /^ {0,4}(", P_CORE, [CORE + 'markdown-code-context.test.ts'], 'rule'),
    ('PR2-profile-closer-any-whitespace', CORE + 'markdown-code-context.ts', "(`{3,}|~{3,}) *$/.exec(line)", "(`{3,}|~{3,})\\s*$/.exec(line)", P_CORE, [CORE + 'markdown-code-context.test.ts'], 'rule'),
    ('PR3-profile-closer-strictly-longer', CORE + 'markdown-code-context.ts', "run.length >= length", "run.length > length", P_CORE, [CORE + 'markdown-code-context.test.ts'], 'rule'),
    ('PR4-profile-backtick-info-allowed', CORE + 'markdown-code-context.ts', "if (run[0] === '`' && info.includes('`')) {", "if (false) {", P_CORE, [CORE + 'markdown-code-context.test.ts'], 'rule'),
    ('PR5-profile-opener-tolerates-CR', CORE + 'markdown-code-context.ts', "const FENCE_OPENER = /^ {0,3}(`{3,}|~{3,})(.*)$/;", "const FENCE_OPENER = /^ {0,3}(`{3,}|~{3,})([^\\n]*)$/;", P_CORE, [CORE + 'markdown-code-context.test.ts'], 'closes-a-gap'),
    ('L1-links-opener-spaces-only', CORE + 'project-shape-manifest.ts', "/^\\s{0,3}(`{3,}|~{3,})/.exec(line)", "/^ {0,3}(`{3,}|~{3,})/.exec(line)", P_CORE, [CORE + 'project-shape-manifest.test.ts'], 'rule'),
    ('L2-links-closer-any-length', CORE + 'project-shape-manifest.ts', " && (opener[1] ?? '').length >= fence.length", "", P_CORE, [CORE + 'project-shape-manifest.test.ts'], 'rule'),
    ('L3-links-closer-any-fence-char', CORE + 'project-shape-manifest.ts', ".startsWith(fence[0] ?? '')", ".startsWith('`')", P_CORE, [CORE + 'project-shape-manifest.test.ts'], 'rule'),
    ('L4-links-inline-span-needs-content', CORE + 'project-shape-manifest.ts', "line.replace(/`[^`]*`/g, '')", "line.replace(/`[^`]+`/g, '')", P_CORE, [CORE + 'project-shape-manifest.test.ts'], 'closes-a-gap'),
    ('E1-extraction-opener-indent3', CORE + 'project-shape-extraction.ts', "const FENCE = /^(`{3,}|~{3,})/;", "const FENCE = /^ {0,3}(`{3,}|~{3,})/;", P_CORE, [CORE + 'project-shape-extraction.test.ts'], 'closes-a-gap'),
    ('E2-extraction-closer-trim-both-sides', CORE + 'project-shape-extraction.ts', "line.trimEnd() === fence", "line.trim() === fence", P_CORE, [CORE + 'project-shape-extraction.test.ts'], 'closes-a-gap'),
    ('E3-extraction-closer-any-text', CORE + 'project-shape-extraction.ts', "(line.startsWith(fence) && line.trim().replace(/[`~]/g, '') === '')", "line.startsWith(fence)", P_CORE, [CORE + 'project-shape-extraction.test.ts'], 'rule'),
    ('R1-renderer-opener-indent4', APP + 'polaris-markdown.ts', "const fenceStart = /^ {0,3}(", "const fenceStart = /^ {0,4}(", P_APP, [APP + 'polaris-markdown.test.ts'], 'rule'),
    ('R2-renderer-closer-longer-than-opener', APP + 'polaris-markdown.ts', "${marker[0]}{${marker.length},}", "${marker[0]}{${marker.length + 1},}", P_APP, [APP + 'polaris-markdown.test.ts'], 'rule'),
    ('R3-renderer-heading-depth-closer-longer', APP + 'polaris-markdown.ts', "${fence.marker}{${fence.length},}", "${fence.marker}{${fence.length + 1},}", P_APP, [APP + 'polaris-markdown.test.ts'], 'rule'),
    ('K1-consent-opener-indent4', CONSENT + 'package-reader.ts', "const m = /^ {0,3}(`{3,}|~{3,})(.*)$/.exec(line);", "const m = /^ {0,4}(`{3,}|~{3,})(.*)$/.exec(line);", P_CONSENT, [CONSENT + 'package-reader.test.ts'], 'rule'),
    ('K2-consent-closer-strictly-longer', CONSENT + 'package-reader.ts', "m[1]!.length >= open.length", "m[1]!.length > open.length", P_CONSENT, [CONSENT + 'package-reader.test.ts'], 'rule'),
    ('K3-consent-closer-any-text', CONSENT + 'package-reader.ts', "&& m[2]!.trim() === '') open = null;", ") open = null;", P_CONSENT, [CONSENT + 'package-reader.test.ts'], 'rule'),
    ('K4-consent-backtick-info-opens', CONSENT + 'package-reader.ts', "!(m[1]![0] === '`' && m[2]!.includes('`'))", "true", P_CONSENT, [CONSENT + 'package-reader.test.ts'], 'rule'),
]


def run(cmd, cwd, env=None, timeout=1800):
    return subprocess.run(cmd, cwd=cwd, env={**os.environ, **(env or {})}, capture_output=True, text=True, timeout=timeout)


def failures(output):
    """The first error line of each failed test: a vitest line `× name` followed by `→ message`."""
    rows, lines = [], output.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r'^\s*[×✗]\s+(.*?)(?:\s+\d+ms)?$', line)
        if m:
            nxt = lines[i + 1].strip() if i + 1 < len(lines) else ''
            rows.append({'test': m.group(1)[:140], 'firstError': nxt[:200]})
    return rows


def vitest(clone, project, files, env):
    done = run(['npx', 'vitest', 'run', '--project', project, *files], clone, env)
    text = done.stdout + done.stderr
    tail = [l.strip() for l in text.splitlines() if re.match(r'^\s*(Tests|Test Files)\s', l)]
    return {'killed': done.returncode != 0, 'project': project, 'files': files, 'summary': tail[-2:], 'failed': failures(text)[:6], 'failedCount': len(failures(text))}


def main():
    clone, head, expected, tmpdir, out = sys.argv[1:6]
    only = set(sys.argv[sys.argv.index('--only') + 1].split(',')) if '--only' in sys.argv else None
    env = {'TMPDIR': tmpdir}
    results = []
    for mid, file, old, new, project, existing, kind in MUTANTS:
        if only and mid not in only:
            continue
        run(['git', 'checkout', '-q', '--detach', head], clone)
        run(['git', 'clean', '-fdq', '--', 'packages', 'apps'], clone)
        path = os.path.join(clone, file)
        text = open(path, encoding='utf-8').read()
        if text.count(old) != 1:
            results.append({'id': mid, 'error': f'old fragment occurs {text.count(old)} times in {file}'})
            continue
        open(path, 'w', encoding='utf-8').write(text.replace(old, new))
        run(['git', 'commit', '-qa', '-m', f'mutant {mid}'], clone)
        commit = run(['git', 'rev-parse', 'HEAD'], clone).stdout.strip()
        record = {'id': mid, 'kind': kind, 'file': file, 'old': old, 'new': new, 'commit': commit, 'detectors': {}}

        record['detectors']['test'] = vitest(clone, P_APP, [APP + 'fence-rules.test.ts'], env)

        built = run(['npm', 'run', 'build:poc'], clone, env)
        probe_out = os.path.join(tmpdir, f'fence-{mid}.json')
        ran = run(['node', os.path.join(clone, 'docs/evidence/syzygy-bpyt-6-3/fence-probe.mjs'), clone, probe_out], clone, env) if built.returncode == 0 else None
        if ran is None or ran.returncode != 0:
            record['detectors']['probe'] = {'killed': True, 'how': 'build or probe failed', 'detail': ((built.stdout + built.stderr) if ran is None else (ran.stdout + ran.stderr))[-300:]}
        else:
            cmp = run([sys.executable, os.path.join(HERE, 'compare-fence-probe.py'), expected, probe_out], clone)
            cj = json.loads(cmp.stdout)
            record['detectors']['probe'] = {'killed': cmp.returncode != 0, 'casesThatDiffer': cj['casesThatDiffer'], 'casesCompared': cj['casesCompared'], 'consentFunctionTextDiffers': cj['consentFunctionTextDiffers'],
                                            'firstDifferingCases': [d['case'] for d in cj['differing'][:5]]}
        if os.path.exists(probe_out):
            os.remove(probe_out)

        record['detectors']['existing'] = vitest(clone, project, existing, env)

        killers = [k for k, v in record['detectors'].items() if v['killed']]
        record['verdict'] = 'killed by ' + ', '.join(killers) if killers else 'SURVIVED'
        results.append(record)
        print(mid, record['verdict'], flush=True)
        run(['git', 'checkout', '-q', '--detach', head], clone)
    json.dump({'head': head, 'expectedProbeOutput': expected, 'mutants': results}, open(out, 'w'), indent=1)
    run(['npm', 'run', 'build:poc'], clone, env)


if __name__ == '__main__':
    main()
