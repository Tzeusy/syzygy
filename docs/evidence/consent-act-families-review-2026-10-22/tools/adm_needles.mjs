// adm-needles equivalence: each ADMISSION_PATHS needle's first folded spelling contains some ADMISSION_STEMS needle's first folded
// spelling, so `carries(text, path)` implies `carries(text, stem)`. fold/stemFolds copied from package-reader.ts at 9f49b6cb.
const fold = value => value.normalize('NFKC').replace(/[‐-―−﹘﹣－]/gu, '-').toLowerCase();
const stemFolds = value => {
  const base = fold(value).replace(/[_\s]+/gu, '-');
  return [base.replace(/\p{Default_Ignorable_Code_Point}/gu, ''), base.replace(/\p{Default_Ignorable_Code_Point}/gu, '-')].map(form => form.replace(/-+/g, '-'));
};
const INSTANCES_DIR = '.syzygy/governance/contracts/candidates/public-repo-admission/instances';
const EGRESS_V2_INSTANCE = '.syzygy/governance/contracts/candidates/public-egress-v2/instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md';
const STEMS = ['public-repo-admission', 'public-egress-v2', 'public-obs-', 'public-egress-anthropic', 'public-egress-'];
const PATHS = [INSTANCES_DIR, EGRESS_V2_INSTANCE, '.syzygy/governance/contracts/candidates/public-repo-admission/', '.syzygy/governance/contracts/candidates/public-egress-v2/'];
let all = true;
for (const p of PATHS) {
  const n = stemFolds(p)[0];
  const covering = STEMS.filter(s => n.includes(stemFolds(s)[0]));
  console.log(p, '->', covering.join(', ') || 'NONE');
  if (covering.length === 0) all = false;
}
console.log(all ? 'every path needle contains a stem needle' : 'SOME PATH NEEDLE CONTAINS NO STEM');
