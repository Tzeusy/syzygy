import json, sys
rec = json.load(open(sys.argv[1]))
by = {m['id']: m for m in rec['mutants']}
keep = ['M0-unmutated-control', 'M2-forms-reused-across-files', 'M4-memo-removed', 'M22a-admission-stem-removed', 'M5-slack-eager', 'M2b-forms-keyed-by-name-across-sweeps']
scratch = 'packages/polaris-generation-consent/src/zz-review-cost.test.ts'
mut = [{k: by[i][k] for k in ('id', 'file', 'old', 'new', 'tests')} for i in keep]
m0, m5 = by['M0-unmutated-control'], by['M5-slack-eager']
mut.append({'id': 'R0-control-scratch-cost', 'file': m0['file'], 'old': m0['old'], 'new': m0['new'], 'tests': [scratch]})
mut.append({'id': 'R5-slack-eager-scratch-cost', 'file': m5['file'], 'old': m5['old'], 'new': m5['new'], 'tests': [scratch]})
mut.append({'id': 'R2-forms-from-unswept-text', 'file': m0['file'], 'old': 'if (namesAct(family.sweep, rel, textForms(await swept(rel, text)))) {',
            'new': 'if (namesAct(family.sweep, rel, textForms(text))) {', 'tests': m0['tests']})
json.dump({'project': rec['project'], 'mutants': mut}, open(sys.argv[2], 'w'), indent=1)
print([m['id'] for m in mut])
