/**
 * Content schema validator — run with `npm run validate:content`. Exits non-zero on any error.
 * Checks every question file, the fixed mocks, notes and formula sheets.
 */
import fs from 'node:fs';
import path from 'node:path';
import katex from 'katex';
import { SUBJECTS, allSubtopics, type SubjectId } from '../src/content/syllabus';

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1')), '..');
const CONTENT = path.join(ROOT, 'src', 'content');

export const MINIMUMS: Record<SubjectId, number> = { math: 250, physics: 180, chemistry: 150 };
const MIN_PER_SUBTOPIC = 8;

const errors: string[] = [];
const warnings: string[] = [];
const err = (m: string) => errors.push(m);
const warn = (m: string) => warnings.push(m);

interface Q {
  id: string;
  subject: string;
  topic: string;
  subtopic: string;
  difficulty: number;
  question: string;
  options: string[];
  answer: number;
  explanation: string;
  tags: string[];
}

/** Extract $…$ and $$…$$ segments; returns null if dollars are unbalanced. */
export function mathSegments(text: string): { tex: string; display: boolean }[] | null {
  const out: { tex: string; display: boolean }[] = [];
  let i = 0;
  while (i < text.length) {
    if (text[i] === '\\' && text[i + 1] === '$') {
      i += 2;
      continue;
    }
    if (text[i] === '$') {
      const display = text[i + 1] === '$';
      const open = display ? 2 : 1;
      let j = i + open;
      let found = -1;
      while (j < text.length) {
        if (text[j] === '\\') {
          j += 2;
          continue;
        }
        if (text[j] === '$' && (!display || text[j + 1] === '$')) {
          found = j;
          break;
        }
        j++;
      }
      if (found < 0) return null;
      out.push({ tex: text.slice(i + open, found), display });
      i = found + open;
    } else i++;
  }
  return out;
}

export function checkText(where: string, text: string) {
  // eslint-disable-next-line no-control-regex
  if (/[\u0000-\u0008\u000b\u000c\u000e-\u001f]/.test(text)) err(`${where}: contains a control character (did you write \\f, \\b or \\t with a single backslash in JSON?)`);
  if (/\t/.test(text)) err(`${where}: contains a TAB character (probably "\\theta"/"\\times" written with one backslash)`);
  const segs = mathSegments(text);
  if (!segs) {
    err(`${where}: unbalanced $ signs`);
    return;
  }
  for (const s of segs) {
    try {
      katex.renderToString(s.tex, { throwOnError: true, displayMode: s.display, strict: 'ignore' });
    } catch (e) {
      err(`${where}: KaTeX error in "${s.tex.slice(0, 60)}": ${(e as Error).message.split('\n')[0]}`);
    }
  }
}

function loadQuestions(): { file: string; qs: Q[] }[] {
  const out: { file: string; qs: Q[] }[] = [];
  for (const s of SUBJECTS) {
    const dir = path.join(CONTENT, s.id);
    if (!fs.existsSync(dir)) continue;
    for (const f of fs.readdirSync(dir).filter((x) => x.endsWith('.json')).sort()) {
      const file = path.join(dir, f);
      let data: unknown;
      try {
        data = JSON.parse(fs.readFileSync(file, 'utf8'));
      } catch (e) {
        err(`${s.id}/${f}: invalid JSON — ${(e as Error).message}`);
        continue;
      }
      if (!Array.isArray(data)) {
        err(`${s.id}/${f}: top level must be an array of questions`);
        continue;
      }
      out.push({ file: `${s.id}/${f}`, qs: data as Q[] });
    }
  }
  return out;
}

export function validateQuestion(q: Q, where: string, subjectDir: string) {
  const subj = SUBJECTS.find((s) => s.id === q.subject);
  const req = ['id', 'subject', 'topic', 'subtopic', 'difficulty', 'question', 'options', 'answer', 'explanation', 'tags'];
  for (const k of req) if (!(k in q)) err(`${where}: missing field "${k}"`);
  if (typeof q.id !== 'string' || !/^[a-z0-9-]+$/.test(q.id)) err(`${where}: id must be lowercase letters, digits and dashes`);
  if (!subj) return err(`${where}: unknown subject "${q.subject}"`);
  if (q.subject !== subjectDir) err(`${where}: subject "${q.subject}" but file is in ${subjectDir}/`);
  const topic = subj.topics.find((t) => t.id === q.topic);
  if (!topic) err(`${where}: unknown topic "${q.topic}" for ${q.subject}`);
  else if (!topic.subtopics.some((s) => s.id === q.subtopic)) err(`${where}: subtopic "${q.subtopic}" is not in topic "${q.topic}"`);
  if (![1, 2, 3].includes(q.difficulty)) err(`${where}: difficulty must be 1, 2 or 3`);
  if (typeof q.question !== 'string' || q.question.trim().length < 10) err(`${where}: question text missing or too short`);
  if (!Array.isArray(q.options) || q.options.length !== 4) err(`${where}: needs exactly 4 options`);
  else {
    q.options.forEach((o, i) => {
      if (typeof o !== 'string' || !o.trim()) err(`${where}: option ${i} empty`);
      else checkText(`${where} option ${'ABCD'[i]}`, o);
    });
    const norm = q.options.map((o) => String(o).replace(/\s+/g, '').toLowerCase());
    if (new Set(norm).size !== 4) err(`${where}: duplicate options`);
    if (q.options.some((o) => /all of the above|none of the above|both a and b/i.test(o))) err(`${where}: avoid "all/none of the above" options (answer positions are shuffled)`);
  }
  if (!Number.isInteger(q.answer) || q.answer < 0 || q.answer > 3) err(`${where}: answer must be an integer 0–3`);
  if (typeof q.explanation !== 'string' || q.explanation.trim().length < 20) err(`${where}: explanation missing or too short`);
  else if (/\b(option|answer|choice)\s*\(?[A-D]\)?\b/.test(q.explanation)) err(`${where}: explanation refers to an option letter — letters change when options are shuffled`);
  if (!Array.isArray(q.tags) || q.tags.some((t) => typeof t !== 'string')) err(`${where}: tags must be an array of strings`);
  if (typeof q.question === 'string') checkText(`${where} question`, q.question);
  if (typeof q.explanation === 'string') checkText(`${where} explanation`, q.explanation);
}

function main() {
  const files = loadQuestions();
  const ids = new Map<string, string>();
  const all: Q[] = [];
  for (const { file, qs } of files) {
    const dir = file.split('/')[0];
    qs.forEach((q, i) => {
      const where = `${file}#${i} (${q?.id ?? '?'})`;
      if (!q || typeof q !== 'object') return err(`${where}: not an object`);
      validateQuestion(q, where, dir);
      if (ids.has(q.id)) err(`${where}: duplicate id (also in ${ids.get(q.id)})`);
      ids.set(q.id, file);
      all.push(q);
    });
  }

  // counts
  const strict = !process.argv.includes('--lenient');
  for (const s of SUBJECTS) {
    const n = all.filter((q) => q.subject === s.id).length;
    const msg = `${s.name}: ${n} questions (minimum ${MINIMUMS[s.id]})`;
    if (n < MINIMUMS[s.id]) (strict ? err : warn)(msg);
  }
  for (const ref of allSubtopics()) {
    const qs = all.filter((q) => q.subject === ref.subject.id && q.subtopic === ref.subtopic.id);
    if (qs.length < MIN_PER_SUBTOPIC) (strict ? err : warn)(`${ref.subject.id}/${ref.subtopic.id}: only ${qs.length} questions (minimum ${MIN_PER_SUBTOPIC})`);
    const diffs = new Set(qs.map((q) => q.difficulty));
    if (qs.length >= MIN_PER_SUBTOPIC && diffs.size < 3) warn(`${ref.subject.id}/${ref.subtopic.id}: not all difficulty levels present`);
    // notes
    const note = path.join(CONTENT, 'notes', ref.subject.id, `${ref.subtopic.id}.md`);
    if (!fs.existsSync(note)) (strict ? err : warn)(`missing notes file notes/${ref.subject.id}/${ref.subtopic.id}.md`);
    else checkText(`notes/${ref.subject.id}/${ref.subtopic.id}.md`, fs.readFileSync(note, 'utf8'));
  }
  for (const s of SUBJECTS) {
    const f = path.join(CONTENT, 'formulas', `${s.id}.md`);
    if (!fs.existsSync(f)) (strict ? err : warn)(`missing formula sheet formulas/${s.id}.md`);
    else checkText(`formulas/${s.id}.md`, fs.readFileSync(f, 'utf8'));
  }

  // answer positions per subject
  for (const s of SUBJECTS) {
    const qs = all.filter((q) => q.subject === s.id);
    if (!qs.length) continue;
    const pos = [0, 0, 0, 0];
    qs.forEach((q) => pos[q.answer]++);
    const expected = qs.length / 4;
    const worst = Math.max(...pos.map((p) => Math.abs(p - expected)));
    const line = `${s.name} answer positions A/B/C/D = ${pos.join('/')}`;
    if (worst > Math.max(3, expected * 0.1)) (strict ? err : warn)(`${line} — unbalanced (run: npx tsx scripts/balance-answers.ts)`);
    else console.log(line);
  }

  // fixed mocks
  const mockFile = path.join(CONTENT, 'mocks', 'fixed-mocks.json');
  const mocks = JSON.parse(fs.readFileSync(mockFile, 'utf8')) as Record<string, { id: string; title: string; qids: string[] }[]>;
  for (const s of SUBJECTS) {
    const list = mocks[s.id] ?? [];
    if (list.length < 3) (strict ? err : warn)(`${s.name}: ${list.length} fixed mocks (need 3)`);
    for (const mk of list) {
      if (mk.qids.length !== 48) err(`mock ${mk.id}: ${mk.qids.length} questions (need 48)`);
      if (new Set(mk.qids).size !== mk.qids.length) err(`mock ${mk.id}: duplicate questions`);
      for (const id of mk.qids) {
        const q = all.find((x) => x.id === id);
        if (!q) err(`mock ${mk.id}: unknown question ${id}`);
        else if (q.subject !== s.id) err(`mock ${mk.id}: ${id} is not a ${s.id} question`);
      }
    }
  }

  for (const w of warnings) console.warn(`warning: ${w}`);
  if (errors.length) {
    for (const e of errors.slice(0, 200)) console.error(`error: ${e}`);
    if (errors.length > 200) console.error(`… and ${errors.length - 200} more`);
    console.error(`\n✗ ${errors.length} error(s) in content`);
    process.exit(1);
  }
  console.log(`✓ content OK — ${all.length} questions (${SUBJECTS.map((s) => `${s.short} ${all.filter((q) => q.subject === s.id).length}`).join(', ')})`);
}

main();
