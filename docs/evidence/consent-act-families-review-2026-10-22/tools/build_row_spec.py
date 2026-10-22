"""Build the reviewer's supplementary rule-6 spec: one mutant per form row (and per family form list) the PR's record leaves
unmutated. argv[1] = package-reader.ts at the reviewed commit, argv[2] = output spec path. Each `old` must occur exactly once."""
import json
import sys

src = open(sys.argv[1], encoding='utf-8').read()
F = 'packages/polaris-generation-consent/src/package-reader.ts'
TESTS = ['packages/polaris-generation-consent/src/act-families.test.ts', 'packages/polaris-generation-consent/src/package-reader.test.ts',
         'packages/polaris-generation-consent/src/digest-bound-act.test.ts']
D = '${date}'
mutants = [
    ('rv-pol-v1-spread', f"  identity: (date: string) => `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-APPROVAL-{D}`,\n  ...APPROVE_POLICY,\n",
     f"  identity: (date: string) => `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-APPROVAL-{D}`,\n"),
    ('rv-pol-v2-spread', f"  identity: (date: string) => `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V2-APPROVAL-{D}`,\n  ...APPROVE_POLICY,\n",
     f"  identity: (date: string) => `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V2-APPROVAL-{D}`,\n"),
    ('rv-pol-v4-spread', f"  identity: (date: string) => `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V4-APPROVAL-{D}`,\n  ...APPROVE_POLICY,\n",
     f"  identity: (date: string) => `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V4-APPROVAL-{D}`,\n"),
    ('rv-pol-v1-identity', f"PUBLIC-SOURCE-SCOPE-APPROVAL-{D}`", f"PUBLIC-SOURCE-SCOPE-APPROVED-{D}`"),
    ('rv-pol-v2-identity', f"PUBLIC-SOURCE-SCOPE-V2-APPROVAL-{D}`", f"PUBLIC-SOURCE-SCOPE-V2-APPROVED-{D}`"),
    ('rv-pol-v3-identity', f"PUBLIC-SOURCE-SCOPE-V3-APPROVAL-{D}`", f"PUBLIC-SOURCE-SCOPE-V3-APPROVED-{D}`"),
    ('rv-pol-v4-title', "(public-source screening scope, version 4)'", "(public-source screening scope, version 4 )'"),
    ('rv-adm-requests-type', "title: '# Owner act — psf/requests public-repository observation consent', type: 'consent-observation'",
     "title: '# Owner act — psf/requests public-repository observation consent', type: 'consent-egress'"),
    ('rv-adm-egress-v1-identity', "identity: d => `PUBLIC-EGRESS-ANTHROPIC-${d}`", "identity: d => `PUBLIC-EGRESS-ANTHROPIC-X-${d}`"),
    ('rv-adm-egress-v2-version', "artifact: EGRESS_V2_INSTANCE, version: 2 }", "artifact: EGRESS_V2_INSTANCE, version: 1 }"),
    ('rv-adm-egress-v2-title', "'# Owner act — public-target egress consent to Anthropic, version 2'", "'# Owner act — public-target egress consent to Anthropic, v2'"),
    ('rv-family-policy-forms', "forms: POLICY_ACT_FORMS,", "forms: POLICY_ACT_FORMS.slice(0, 3),"),
    ('rv-family-admission-forms', "forms: ADMISSION_ACT_FORMS,", "forms: ADMISSION_ACT_FORMS.slice(1),"),
    ('rv-family-class-forms', "forms: [CLASS_ACT_FORM],", "forms: [],"),
    ('rv-family-class-dialect', "const act = parseActRecord(record.text, record.form, CLASS_FAMILY.dialect);",
     "const act = parseActRecord(record.text, record.form, RECORDER_DIALECT);"),
    ('rv-family-policy-dialect', "parsed[POLICY_ACT_FORMS.indexOf(form)] = parseActRecord(text, form, POLICY_FAMILY.dialect);",
     "parsed[POLICY_ACT_FORMS.indexOf(form)] = parseActRecord(text, form, RECORDER_DIALECT);"),
]
out = []
for mid, old, new in mutants:
    n = src.count(old)
    if n != 1:
        sys.exit(f'{mid}: old occurs {n} times')
    out.append({'id': mid, 'file': F, 'old': old, 'new': new, 'tests': TESTS})
json.dump({'project': '@syzygy/polaris-generation-consent', 'mutants': out}, open(sys.argv[2], 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(len(out), 'mutants written; every old fragment occurs exactly once')
