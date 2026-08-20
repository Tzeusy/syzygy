declare const brand: unique symbol;
type Branded<Base, Brand extends string> = Base & { readonly [brand]: Brand };

export type ProjectId = Branded<string, 'ProjectId'>;
export type RepositoryId = Branded<string, 'RepositoryId'>;
export type EvaluationId = Branded<string, 'EvaluationId'>;

// An "identified evaluation" is the pair (source snapshot, as-of instant)
// — the spec's reader notes fix this vocabulary.
export interface EvaluationIdentity {
  readonly snapshot: string;
  readonly asOf: string;
}
