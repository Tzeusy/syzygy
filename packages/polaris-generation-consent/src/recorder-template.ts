/** A recorder's fixed output as a template: the literal text it writes, with a `{slot}` for each value it fills in, and a pattern per
 * slot. A record is in the recorder's form only when the slots read out of it render the template back to the record, byte for byte
 * (R-POLARIS-DOSSIER-GATE-SOURCES-2 finding 2): every fixed line and section is then the recorder's, and a slot the template repeats
 * (a date, an argument) carries the same text each time. */
export interface RecorderTemplate {
  /** The slots read out of `text`, or null when `text` does not have the template's shape. */
  readonly fields: (text: string) => Readonly<Record<string, string>> | null;
  readonly render: (fields: Readonly<Record<string, string>>) => string;
}

const escape = (literal: string): string => literal.replace(/[.*+?^${}()|[\]\\/]/g, '\\$&');

export function recorderTemplate(template: string, slots: Readonly<Record<string, string>>): RecorderTemplate {
  const parts = template.split(/\{([A-Za-z]+)\}/);   // even indexes literal text, odd indexes slot names
  const seen = new Set<string>();
  let source = '^';
  parts.forEach((part, i) => {
    if (i % 2 === 0) { source += escape(part); return; }
    const pattern = slots[part];
    if (pattern === undefined) throw new Error(`template slot {${part}} has no pattern`);
    source += seen.has(part) ? `\\k<${part}>` : `(?<${part}>${pattern})`;
    seen.add(part);
  });
  const re = new RegExp(`${source}$`, 'u');
  return Object.freeze({
    fields: (text: string) => { const m = re.exec(text); return m === null ? null : Object.freeze({ ...m.groups }); },
    render: (fields: Readonly<Record<string, string>>) => parts.map((part, i) => (i % 2 === 0 ? part : fields[part] ?? '')).join(''),
  });
}

/** The slots of `text` when the template renders them back to exactly `text`; null otherwise. */
export function templateFields(template: RecorderTemplate, text: string): Readonly<Record<string, string>> | null {
  const fields = template.fields(text);
  return fields !== null && template.render(fields) === text ? fields : null;
}

/** Slot patterns the recorders' values take. A `line` holds a non-space character and no line break of either kind: the recorders
 * refuse a blank selection (R-POLARIS-DOSSIER-GATE-SOURCES-3 note 3).
 *
 * `line` names its first non-space character: only spaces other than CR and LF come before it. The language is the earlier
 * `[^\r\n]*\S[^\r\n]*` one (CR and LF are both `\s`, so the leading run is still free of breaks, and any such line splits at its
 * first `\S`), and a slot followed by more template still captures the longest value the rest accepts. But the earlier pattern could
 * place its `\S` at any of the line's characters, so a record that failed late was retried once per placement in every slot; this one
 * places it once (syzygy-bpyt.8.17). */
export const SLOT = Object.freeze({
  date: '\\d{4}-\\d{2}-\\d{2}',
  instant: '\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z',
  sha256: '[0-9a-f]{64}',
  commit: '[0-9a-f]{40}',
  verdict: 'CONFIRM WITH EXCEPTIONS|CONFIRM',
  line: '[^\\S\\r\\n]*\\S[^\\r\\n]*',
});
