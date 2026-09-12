import { digestCanonicalJson, runGenerationPipeline, stageSchema, validateStage, reviewVerdict, type PipelinePorts, type PipelineRequest } from '@syzygy/polaris-generation-core';

/** Explicit synthetic provider fixture. This demonstrates orchestration and
 * rendering, never LLM quality, real source admission or production durability.
 */
export interface SyntheticProject {
  readonly id: string;
  readonly title: string;
  readonly purpose: string;
  readonly mechanism: string;
  readonly qualification: string;
  readonly components: readonly [string, string];
}

export const syntheticProjects: readonly SyntheticProject[] = [
  {
    id: 'garden', title: 'A garden that asks for less remembering',
    purpose: 'Garden Notes helps a household remember the recurring care that keeps its plants healthy.',
    mechanism: 'Care observations feed a seasonal plan. The plan turns those observations into the next useful gardening task.',
    qualification: 'The household decides what to plant and when to act. A care plan offers guidance; it cannot observe a plant that nobody has checked.',
    components: ['Care observations', 'Seasonal plan'],
  },
  {
    id: 'archive', title: 'An archive worth finding again',
    purpose: 'Field Archive helps researchers recover the context behind their collected field observations.',
    mechanism: 'Field notes feed a subject index. The index connects related observations so a researcher can return to the original account.',
    qualification: 'An index can connect accounts, but it cannot settle disagreements between them. Conflicting observations remain visible.',
    components: ['Field notes', 'Subject index'],
  },
];

export async function runSyntheticProject(project: SyntheticProject) {
  const sources = [
    { sourceId: 'purpose', text: project.purpose },
    { sourceId: 'mechanism', text: project.mechanism },
    { sourceId: 'qualification', text: project.qualification },
  ];
  const inventory = { entries: sources.map((source, i) => ({ id: `entry-${i}`, sourceIds: [source.sourceId], statement: source.text, kind: i === 0 ? 'purpose' : i === 1 ? 'capability' : 'qualification' })) };
  const plan = { sections: [
    { id: 'how', title: 'How the pieces connect', reason: 'Explain the central relationship.', sourceIds: ['mechanism'] },
    { id: 'judgment', title: 'Where judgment stays', reason: 'Keep the material limit visible.', sourceIds: ['qualification'] },
  ] };
  const draft = {
    title: project.title,
    introduction: { id: 'opening', text: project.purpose, sourceIds: ['purpose'] },
    sections: [
      { id: 'how', title: 'How the pieces connect', paragraphs: [{ id: 'mechanism-text', text: project.mechanism, sourceIds: ['mechanism'] }] },
      { id: 'judgment', title: 'Where judgment stays', paragraphs: [{ id: 'qualification-text', text: project.qualification, sourceIds: ['qualification'] }] },
    ],
    diagrams: [{ id: 'architecture', title: 'From observation to useful context', sectionId: 'how',
      nodes: [{ id: 'left', label: project.components[0], sourceIds: ['mechanism'] }, { id: 'right', label: project.components[1], sourceIds: ['mechanism'] }],
      edges: [{ id: 'connection', from: 'left', to: 'right', label: 'feeds', sourceIds: ['mechanism'] }],
    }],
    deepDives: [{ id: 'component-depth', title: `Inside ${project.components[1].toLowerCase()}`, sectionId: 'how', paragraphs: [{ id: 'depth-text', text: project.mechanism, sourceIds: ['mechanism'] }] }],
  };
  const review = { inventoryIds: inventory.entries.map(x => x.id), blockIds: ['opening', 'mechanism-text', 'qualification-text', 'left', 'right', 'connection', 'depth-text'], findings: [] };
  const responses = { inventory, plan, author: draft, edit: draft, fidelity: review, repair: draft };
  const admitted = new Set<number>();
  const records: unknown[] = [];
  const snapshotDigest = digestCanonicalJson(sources, { maxBytes: 100_000, maxNodes: 1000, maxDepth: 10 }).digest;
  const request: PipelineRequest = {
    requestId: `synthetic-${project.id}-${snapshotDigest}`, projectId: project.id, snapshotId: snapshotDigest, providerRoute: 'synthetic-fixture', startedAt: Date.now(),
    sources, readerQuestions: ['Why does it exist?', 'How do the main pieces connect?', 'What remains a human judgment?'],
    budget: { maxCalls: 7, maxInputBytes: 500_000, maxOutputBytes: 100_000, maxUsageUnits: 100, maxElapsedMs: 30_000, maxRepairCycles: 1, accountingPolicy: 'synthetic-unit-v1' },
  };
  const ports: PipelinePorts = {
    now: () => Date.now(), verifySources: async () => true,
    admit: async input => {
      if (admitted.has(input.ordinal)) return null;
      admitted.add(input.ordinal);
      return { attemptId: `${request.requestId}:${input.ordinal}`, maxUsageUnits: 5, maxOutputBytes: 10_000 };
    },
    permitted: async () => true, releaseUnsent: async () => undefined,
    responseSchema: stageSchema, validate: validateStage, fidelity: reviewVerdict,
    generate: async input => ({ body: JSON.stringify(responses[input.stage]), model: 'synthetic-scripted-response-v1', usageUnits: 1 }),
    record: async (permit, outcome) => { records.push({ attemptId: permit.attemptId, outcome }); },
    lateReceipt: async (permit, receipt) => { records.push({ attemptId: permit.attemptId, lateReceipt: receipt }); },
  };
  const result = await runGenerationPipeline(request, ports, new AbortController().signal);
  return { sources, result, records };
}
