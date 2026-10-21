/** The handle shape every id in the draft and stage schemas (and, per admitted-input.ts's
 * front door, every admitted source's `sourceId`) must satisfy. One definition, so
 * admitSourcePopulation and validateGenerationSources fail closed on the exact same
 * pattern and length bound the schemas enforce, instead of duplicating the literals. */
export const SOURCE_ID_PATTERN = '^[A-Za-z0-9][A-Za-z0-9_.:-]*$';
export const SOURCE_ID_MIN_LENGTH = 1;
export const SOURCE_ID_MAX_LENGTH = 100;
/** The upper bound `validateStage`'s `sourceSchema` places on an admitted source's `text`,
 * exported for the same reason: one definition, shared with admitted-input.ts. */
export const SOURCE_TEXT_MAX_LENGTH = 100_000;
