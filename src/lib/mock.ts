import { getSubject, EXAM, type SubjectId } from '../content/syllabus';
import type { Question, Difficulty } from './types';
import { Rng } from './rng';

/** Target difficulty mix inside each topic (≈30/50/20). */
const MIX: Record<Difficulty, number> = { 1: 0.3, 2: 0.5, 3: 0.2 };

/**
 * Pick a 48-question mock for one subject: topic counts follow the syllabus weights
 * (Topic.mockCount), subtopics are spread round-robin, difficulty mix ≈30/50/20.
 * `exclude` lets the fixed-mock builder keep mocks disjoint.
 */
export function selectMockQuestions(bank: Question[], subject: SubjectId, seed: number, exclude: Set<string> = new Set()): Question[] {
  const subj = getSubject(subject);
  if (!subj) throw new Error(`unknown subject ${subject}`);
  const rng = new Rng(seed);
  const picked: Question[] = [];
  for (const topic of subj.topics) {
    const pool = bank.filter((q) => q.subject === subject && q.topic === topic.id && !exclude.has(q.id));
    const want = Math.min(topic.mockCount, pool.length);
    // difficulty quotas for this topic
    const quota: Record<Difficulty, number> = {
      1: Math.round(want * MIX[1]),
      3: Math.round(want * MIX[3]),
      2: 0,
    };
    quota[2] = want - quota[1] - quota[3];
    // round-robin over subtopics so that every subtopic is represented
    const bySub = new Map<string, Question[]>();
    for (const q of rng.shuffle(pool)) {
      const list = bySub.get(q.subtopic) ?? [];
      list.push(q);
      bySub.set(q.subtopic, list);
    }
    const chosen: Question[] = [];
    const taken = new Set<string>();
    const subs = rng.shuffle([...bySub.keys()]);
    // pass 1: respect quotas; pass 2: fill up with anything left
    for (const respectQuota of [true, false]) {
      let progress = true;
      while (chosen.length < want && progress) {
        progress = false;
        for (const s of subs) {
          if (chosen.length >= want) break;
          const list = bySub.get(s)!;
          const idx = list.findIndex((q) => !taken.has(q.id) && (!respectQuota || quota[q.difficulty] > 0));
          if (idx >= 0) {
            const q = list[idx];
            chosen.push(q);
            taken.add(q.id);
            quota[q.difficulty]--;
            progress = true;
          }
        }
      }
    }
    // inside a topic: easier first, like a real paper
    chosen.sort((p, q) => p.difficulty - q.difficulty);
    picked.push(...chosen);
  }
  return picked.slice(0, EXAM.questions);
}

export const MOCK_MS = EXAM.minutes * 60 * 1000;
