import type { ConsentRecord, EvaluationIdentity, ProjectId, RepositoryId } from '@syzygy/cap1-core';

// Conformance fixture builders: the INPUT side only. Every conformance
// file states its expected values as hard-coded literals (AGENTS.md:
// expected values are never imported from the module under test, and
// never computed by a builder); what these builders share is the
// boilerplate a fixture needs to be a valid declaration, a consent
// record or an evaluation identity at all.

export const FIXTURE_OWNER = 'uniquosity@gmail.com';

// The as-of instant most conformance fixtures evaluate at.
export const FIXTURE_AS_OF = '2026-08-21T00:00:00Z';

export interface DeclaredRepository {
  readonly id: string;
  readonly role: 'governance-root' | 'observed-source';
  readonly consent: string;
}

export interface DeclaredRelation {
  readonly type: string;
  readonly project: string;
}

export interface ProjectYamlFields {
  readonly id: string;
  readonly name: string;
  readonly owner?: string;
  readonly repositories: readonly DeclaredRepository[];
  readonly consents: readonly string[];
  readonly relations?: readonly DeclaredRelation[];
  readonly profiles?: readonly string[];
}

// A block sequence under `key`, or the flow form `key: []` when empty.
function sequence(key: string, items: readonly string[]): string {
  return items.length === 0 ? `${key}: []\n` : `${key}:\n${items.join('')}`;
}

// The closed declaration the core reader accepts (`.syzygy/project.yaml`),
// with the fixed `declarations.spec_root` tail every fixture shares. The
// text starts and ends with a newline, as the inline fixtures did.
export function projectYaml(fields: ProjectYamlFields): string {
  const repositories = fields.repositories.map(
    (repository) =>
      `  - id: ${repository.id}\n    role: ${repository.role}\n    consent: ${repository.consent}\n`,
  );
  const consents = fields.consents.map((consent) => `  - ${consent}\n`);
  const relations = (fields.relations ?? []).map(
    (relation) => `  - type: ${relation.type}\n    project: ${relation.project}\n`,
  );
  const profiles = (fields.profiles ?? []).map((profile) => `  - ${profile}\n`);
  return [
    '\nschema_version: "1"\n',
    `project:\n  id: ${fields.id}\n  name: ${fields.name}\n`,
    `owner: ${fields.owner ?? FIXTURE_OWNER}\n`,
    sequence('repositories', repositories),
    sequence('consents', consents),
    'declarations:\n  spec_root: openspec/\n',
    sequence('relations', relations),
    sequence('profiles', profiles),
  ].join('');
}

export function evaluation(snapshot: string, asOf: string = FIXTURE_AS_OF): EvaluationIdentity {
  return { snapshot, asOf };
}

export interface ConsentFields {
  readonly id: string;
  readonly projectId: ProjectId;
  readonly repositoryId: RepositoryId;
  readonly grantState?: ConsentRecord['grantState'];
}

// An owner-attributed observe-scope consent record, in force unless the
// fixture says otherwise.
export function consent(fields: ConsentFields): ConsentRecord {
  return {
    id: fields.id,
    projectId: fields.projectId,
    repositoryId: fields.repositoryId,
    scope: 'observe',
    attribution: 'owner',
    grantState: fields.grantState ?? 'in-force',
  };
}
