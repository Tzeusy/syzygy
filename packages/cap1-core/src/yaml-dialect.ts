import { parse } from 'yaml';

export type ParseDeclarationResult =
  | { ok: true; value: unknown }
  | { ok: false; error: string };

// This module IS the pinned declaration dialect (RFC3-1): one parser
// (`yaml`, pinned at an exact version in this package's manifest), its
// options fixed here and nowhere else. The dialect is a conformance item;
// no other module may call the parser with different options. Schema
// validation against the closed declaration field set is S1's, not this
// module's.
export function parseDeclarationSource(text: string): ParseDeclarationResult {
  try {
    const value: unknown = parse(text, {
      version: '1.2',
      strict: true,
      uniqueKeys: true,
    });
    return { ok: true, value };
  } catch (cause) {
    return {
      ok: false,
      error: cause instanceof Error ? cause.message : String(cause),
    };
  }
}
