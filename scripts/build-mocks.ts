/**
 * Build 3 fixed, disjoint 48-question mock exams per subject from the question bank.
 *   npx tsx scripts/build-mocks.ts
 * Writes src/content/mocks/fixed-mocks.json. Re-run after adding questions only if you
 * want new fixed mocks (existing attempt history refers to mock ids, not to contents).
 */
import fs from 'node:fs';
import path from 'node:path';
import { SUBJECTS, EXAM } from '../src/content/syllabus';
import { selectMockQuestions } from '../src/lib/mock';
import type { Question } from '../src/lib/types';

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1')), '..');
const CONTENT = path.join(ROOT, 'src', 'content');

const bank: Question[] = [];
for (const s of SUBJECTS) {
  const dir = path.join(CONTENT, s.id);
  if (!fs.existsSync(dir)) continue;
  for (const f of fs.readdirSync(dir).filter((x) => x.endsWith('.json'))) bank.push(...JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8')));
}

const out: Record<string, { id: string; title: string; qids: string[] }[]> = {};
for (const s of SUBJECTS) {
  const used = new Set<string>();
  out[s.id] = [];
  for (let i = 1; i <= 3; i++) {
    const qs = selectMockQuestions(bank, s.id, 1000 * i + s.id.length, used);
    if (qs.length < EXAM.questions) {
      console.warn(`${s.name} mock ${i}: only ${qs.length} questions available`);
      if (qs.length === 0) continue;
    }
    qs.forEach((q) => used.add(q.id));
    out[s.id].push({ id: `${s.id}-fixed-${i}`, title: `${s.name} Mock ${i}`, qids: qs.map((q) => q.id) });
    const d = [1, 2, 3].map((k) => qs.filter((q) => q.difficulty === k).length);
    console.log(`${s.name} Mock ${i}: ${qs.length} questions, difficulty ${d.join('/')}`);
  }
}
fs.writeFileSync(path.join(CONTENT, 'mocks', 'fixed-mocks.json'), JSON.stringify(out, null, 2) + '\n');
