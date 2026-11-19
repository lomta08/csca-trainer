import { QUESTION_BY_ID, QUESTIONS, questionsFor } from '../content';
import { fromGeneratedId, generatorsFor, runGenerator } from './generators';
import { Rng, randomSeed } from './rng';
import type { Difficulty, Question } from './types';
import type { SubjectId } from '../content/syllabus';

export function getQuestion(id: string): Question | undefined {
  return QUESTION_BY_ID.get(id) ?? fromGeneratedId(id);
}

export interface PracticeConfig {
  subject: SubjectId;
  subtopics: string[]; // empty = all
  difficulties: Difficulty[]; // empty = all
  count: number;
  /** math only: mix in generated questions */
  includeGenerated: boolean;
  /** prefer questions not answered before */
  preferUnseen?: Set<string>;
  seed?: number;
}

/** Pick questions for a practice session. */
export function buildPractice(cfg: PracticeConfig): Question[] {
  const rng = new Rng(cfg.seed ?? randomSeed());
  const okDiff = (d: Difficulty) => cfg.difficulties.length === 0 || cfg.difficulties.includes(d);
  let pool = questionsFor(cfg.subject, cfg.subtopics).filter((q) => okDiff(q.difficulty));
  if (cfg.preferUnseen) {
    const unseen = pool.filter((q) => !cfg.preferUnseen!.has(q.id));
    const seen = pool.filter((q) => cfg.preferUnseen!.has(q.id));
    pool = [...rng.shuffle(unseen), ...rng.shuffle(seen)];
  } else pool = rng.shuffle(pool);
  let picked = pool.slice(0, cfg.count);
  if (cfg.subject === 'math' && cfg.includeGenerated) {
    const gens = generatorsFor(cfg.subtopics);
    if (gens.length) {
      // about a third generated, or fill up if the bank is short
      const want = Math.max(cfg.count - picked.length, Math.round(cfg.count / 3));
      const generated: Question[] = [];
      for (let i = 0; i < want * 4 && generated.length < want; i++) {
        const q = runGenerator(rng.pick(gens), randomSeed());
        if (okDiff(q.difficulty)) generated.push(q);
      }
      picked = rng.shuffle([...picked.slice(0, cfg.count - generated.length), ...generated]);
    }
  }
  return picked;
}

export function bankCount(subject?: SubjectId): number {
  return subject ? QUESTIONS.filter((q) => q.subject === subject).length : QUESTIONS.length;
}

export const LETTERS = ['A', 'B', 'C', 'D'];
