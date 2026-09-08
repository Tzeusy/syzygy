/** Extractive presentation only: the original declaration always remains available. */
export interface ProjectReading {
  readonly summary: string;
  readonly full: string;
  readonly condensed: boolean;
}

function blocksOf(text: string): string[] {
  const blocks: string[] = [];
  let lines: string[] = [];
  let fence: string | undefined;
  for (const line of text.split('\n')) {
    const marker = /^\s*(`{3,}|~{3,})/.exec(line)?.[1];
    if (marker !== undefined) {
      if (fence === undefined) fence = marker;
      else if (marker[0] === fence[0] && marker.length >= fence.length) fence = undefined;
    }
    if (line.trim() === '' && fence === undefined) {
      if (lines.length > 0) blocks.push(lines.join('\n'));
      lines = [];
    } else lines.push(line);
  }
  if (lines.length > 0) blocks.push(lines.join('\n'));
  return blocks;
}

function heading(block: string): boolean {
  return /^#{1,6}\s+\S/.test(block) || (
    !block.includes('\n') && block.split(/\s+/).length <= 12 &&
    !/^[\s*`~>|\d-]/.test(block) && !/[.!?:;]$/.test(block)
  );
}

function list(block: string): boolean {
  return /^\s*(?:[-*+]\s|\d+[.)]\s)/.test(block);
}

function fenced(block: string): boolean {
  return /^\s*(?:`{3,}|~{3,})/.test(block);
}

function subheading(block: string): boolean {
  return /^\*\*[^\n]+\*\*$/.test(block);
}

/** A lexical hint can retain a qualification, never establish its absence. */
function qualifier(block: string): boolean {
  return /^(?:\*\*)?(?:except(?:ion)?|an exception|unless|however|but\b|only\b|constraints?\b|cautions?\b|must\b|never\b|not\b|cannot\b|otherwise\b|provided\b|subject to\b|no\b|do not\b)/i.test(block.trim());
}

function displayHeading(block: string): string {
  return /^#/.test(block) ? block : `### ${block}`;
}

export function projectReading(text: string, key: string): ProjectReading {
  const unchanged = { summary: text, full: text, condensed: false };
  if (key !== 'architecture') return unchanged;
  const blocks = blocksOf(text);
  // Without clear section boundaries, selection has no dependable local scope.
  if (blocks.length === 0 || !heading(blocks[0] as string)) return unchanged;
  const sections: { title: string; blocks: string[] }[] = [];
  for (const block of blocks) {
    if (heading(block)) sections.push({ title: block, blocks: [] });
    else sections.at(-1)?.blocks.push(block);
  }
  if (sections.length < 2 || sections.some((section) => section.blocks.length === 0)) return unchanged;

  const rendered = sections.map((section) => {
    const body = section.blocks;
    // Select complete opening blocks and explicit qualifications in source
    // order. These are labeled excerpts, never a substitute for the complete
    // declaration: no sentence is rewritten or cut at a word budget.
    const selected: string[] = [];
    let opening = true;
    let introduced = false;
    let listClosure = false;
    for (const block of body) {
      const isList = list(block);
      const include = opening || introduced || (listClosure && !subheading(block)) || qualifier(block);
      if (include) {
        selected.push(block);
        introduced = /:\s*$/.test(block) && !subheading(block);
        listClosure = isList;
        if (!subheading(block)) opening = false;
      } else {
        introduced = false;
        listClosure = false;
      }
    }
    return [displayHeading(section.title), ...selected].join('\n\n');
  });
  const summary = rendered.join('\n\n');
  const full = sections.map((section) => [displayHeading(section.title), ...section.blocks].join('\n\n')).join('\n\n');
  return { summary, full: text, condensed: summary !== full };
}
