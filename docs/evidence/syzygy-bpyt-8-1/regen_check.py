#!/usr/bin/env python3
"""syzygy-bpyt.8.1: re-run the split generators over the input bytes they were written for and compare their output with the tree.
Usage: python3 regen_check.py <tree> <commit holding provider-draft.ts's input> <commit holding dossier-render.ts's input>
The first input is provider-draft.ts at the bead's base, the second dossier-render.ts at the origin/main the branch merged. Prints JSON:
per generated file, whether the tree's bytes equal the generator's, and both sha256s."""
import hashlib, json, pathlib, subprocess, sys, tempfile

tree, draft_commit, render_commit = pathlib.Path(sys.argv[1]).resolve(), sys.argv[2], sys.argv[3]
here = pathlib.Path(__file__).resolve().parent / 'gen'
git = lambda *args: subprocess.run(['git', '-C', str(tree), *args], capture_output=True, check=True).stdout
sha = lambda data: hashlib.sha256(data).hexdigest()
core, app = 'packages/polaris-generation-core/src', 'apps/three-surface-poc/src/polaris-generation'
runs = [
    ('split_provider_draft.py', draft_commit, f'{core}/provider-draft.ts', core, ['closed-schema.ts', 'draft-model.ts', 'provider-draft.ts']),
    ('split_dossier_render.py', render_commit, f'{app}/dossier-render.ts', app, ['dossier-site.ts', 'dossier-render.ts']),
]
out = {'tree': str(tree), 'commit': git('rev-parse', 'HEAD').decode().strip(), 'generators': []}
for script, commit, source, home, files in runs:
    with tempfile.TemporaryDirectory() as scratch:
        scratch = pathlib.Path(scratch)
        (scratch / 'input.ts').write_bytes(git('show', f'{commit}:{source}'))
        (scratch / 'out').mkdir()
        subprocess.run([sys.executable, '-I', str(here / script), str(scratch / 'input.ts'), str(scratch / 'out')], check=True)
        rows = []
        for name in files:
            generated, committed = (scratch / 'out' / name).read_bytes(), git('show', f'HEAD:{home}/{name}')
            rows.append({'file': f'{home}/{name}', 'identical': generated == committed, 'generatedSha256': sha(generated), 'treeSha256': sha(committed)})
    out['generators'].append({'script': f'gen/{script}', 'scriptSha256': sha((here / script).read_bytes()), 'input': f'{commit}:{source}',
                              'inputSha256': sha(git('show', f'{commit}:{source}')), 'files': rows})
out['allIdentical'] = all(row['identical'] for run in out['generators'] for row in run['files'])
print(json.dumps(out, indent=2))
